"""Synthetic TUSZ-format datasets for tests, dry runs and demos.

:func:`make_fake_tusz` writes a small tree in the exact TUSZ v2 layout::

    <root>/edf/<split>/<patient>/<session>/<montage>/<patient>_<session>_t000.edf
                                                      ... .csv / .csv_bi

Signals are 1/f background EEG with rhythmic focal or generalized seizures
that start on a few channels and spread. Nothing here is real patient data.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np

from neuromech.data.annotations import Event, write_annotation
from neuromech.data.edf_reader import write_edf
from neuromech.data.montage import TCP_CHANNELS, TCP_PAIRS

ELECTRODES: tuple[str, ...] = (
    "FP1", "FP2", "F3", "F4", "C3", "C4", "P3", "P4", "O1", "O2",
    "F7", "F8", "T3", "T4", "T5", "T6", "A1", "A2", "FZ", "CZ", "PZ",
)  # fmt: skip
MONTAGES: tuple[str, ...] = ("01_tcp_ar", "02_tcp_le", "03_tcp_ar_a", "04_tcp_le_a")
FOCAL_TYPES: tuple[str, ...] = ("fnsz", "cpsz")
GENERALIZED_TYPES: tuple[str, ...] = ("gnsz", "absz", "tcsz")


@dataclass(frozen=True)
class FakeSeizure:
    onset: float
    offset: float
    label: str
    onset_channels: tuple[str, ...]
    channels: dict[str, tuple[float, float]]


def _pink(rng: np.random.Generator, n_ch: int, n: int) -> np.ndarray:
    spec = np.fft.rfft(rng.standard_normal((n_ch, n)), axis=-1)
    f = np.fft.rfftfreq(n)
    f[0] = f[1]
    x = np.fft.irfft(spec / np.sqrt(f), n=n, axis=-1)
    return x / x.std(axis=-1, keepdims=True)


def _plan_seizures(rng: np.random.Generator, duration: float, n_seizures: int) -> list[FakeSeizure]:
    seizures: list[FakeSeizure] = []
    t = rng.uniform(0.25, 0.4) * duration
    for _ in range(n_seizures):
        length = float(rng.uniform(15, 40))
        if t + length > duration - 5:
            break
        focal = rng.random() < 0.6
        label = str(rng.choice(FOCAL_TYPES if focal else GENERALIZED_TYPES))
        if focal:
            start_idx = int(rng.integers(0, len(TCP_CHANNELS) - 3))
            onset_ch = TCP_CHANNELS[start_idx : start_idx + 2]
            spread_ch = TCP_CHANNELS[start_idx + 2 : start_idx + 4]
            channels = {c: (t, t + length) for c in onset_ch}
            channels |= {c: (t + 4.0, t + length) for c in spread_ch}
        else:
            onset_ch = TCP_CHANNELS
            channels = {c: (t, t + length) for c in TCP_CHANNELS}
        seizures.append(FakeSeizure(t, t + length, label, tuple(onset_ch), channels))
        t += length + rng.uniform(0.15, 0.3) * duration
    return seizures


def _render(
    rng: np.random.Generator, fs: int, duration: float, seizures: list[FakeSeizure], ears: bool
) -> tuple[np.ndarray, list[str]]:
    """Referential electrode signals whose TCP differences contain the seizures."""
    n = int(duration * fs)
    t = np.arange(n) / fs
    names = [e for e in ELECTRODES if ears or e not in {"A1", "A2"}]
    ref = 15.0 * _pink(rng, len(names), n)
    idx = {e: i for i, e in enumerate(names)}
    for sz in seizures:
        freq = 3.0 if sz.label == "absz" else 5.0
        for ch, (s, e) in sz.channels.items():
            a, _b = TCP_PAIRS[TCP_CHANNELS.index(ch)]
            if a not in idx:
                continue
            mask = (t >= s) & (t < e)
            ramp = np.clip((t - s) / 2.0, 0.0, 1.0)
            ref[idx[a]] += mask * ramp * 80.0 * np.sin(2 * np.pi * freq * t)
    return ref, names


def make_fake_tusz(
    root: str | Path,
    patients_per_split: dict[str, int] | None = None,
    duration_s: float = 120.0,
    fs: int = 250,
    seed: int = 0,
) -> Path:
    """Create a miniature TUSZ v2 dataset under ``root`` and return ``root``.

    Every third recording has no ECG; montage folders rotate through all four types;
    some recordings have no seizure.
    """
    root = Path(root)
    rng = np.random.default_rng(seed)
    patients_per_split = patients_per_split or {"train": 4, "dev": 2, "eval": 2}
    counter = 0
    for split, n_pat in patients_per_split.items():
        for _ in range(n_pat):
            counter += 1
            patient = f"aaaaa{counter:03d}"
            for s in range(1, 3):
                session = f"s{s:03d}_20{10 + s:02d}"
                montage = MONTAGES[(counter + s) % len(MONTAGES)]
                ears = not montage.endswith("_a")
                folder = root / "edf" / split / patient / session / montage
                stem = f"{patient}_s{s:03d}_t000"
                n_sz = int(rng.integers(0, 3))
                seizures = _plan_seizures(rng, duration_s, n_sz)
                ref, names = _render(rng, fs, duration_s, seizures, ears)
                suffix = "REF" if "_ar" in montage else "LE"
                labels = [f"EEG {e}-{suffix}" for e in names]
                signals = ref
                if (counter + s) % 3:
                    hr = 70 + 30 * rng.random()
                    tt = np.arange(ref.shape[1]) / fs
                    ecg = np.exp(-(((tt * hr / 60) % 1 - 0.5) ** 2) / 0.0005) * 500
                    signals = np.vstack([ref, ecg])
                    labels.append(f"EEG EKG1-{suffix}")
                write_edf(folder / f"{stem}.edf", signals, fs=fs, labels=labels)
                _write_labels(folder / stem, seizures, duration_s, ears)
    return root


def _write_labels(stem: Path, seizures: list[FakeSeizure], duration: float, ears: bool) -> None:
    usable = [c for c in TCP_CHANNELS if ears or ("A1" not in c and "A2" not in c)]
    chan_events: list[Event] = []
    for ch in usable:
        cursor = 0.0
        for sz in seizures:
            if ch not in sz.channels:
                continue
            s, e = sz.channels[ch]
            if s > cursor:
                chan_events.append(Event(ch, cursor, s, "bckg"))
            chan_events.append(Event(ch, s, e, sz.label))
            cursor = e
        chan_events.append(Event(ch, cursor, duration, "bckg"))
    term_events: list[Event] = []
    cursor = 0.0
    for sz in seizures:
        term_events += [
            Event("TERM", cursor, sz.onset, "bckg"),
            Event("TERM", sz.onset, sz.offset, "seiz"),
        ]
        cursor = sz.offset
    term_events.append(Event("TERM", cursor, duration, "bckg"))
    write_annotation(stem.with_suffix(".csv"), chan_events, duration)
    write_annotation(stem.with_suffix(".csv_bi"), term_events, duration)
