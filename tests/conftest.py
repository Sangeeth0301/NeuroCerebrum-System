"""Shared pytest fixtures.

All fixtures are synthetic: tests never need the real TUSZ data.
Tests that do need real data must be marked ``@pytest.mark.data``.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pytest

# TUSZ 22-channel TCP bipolar montage (NEDC standard order).
TCP_CHANNELS: list[str] = [
    "FP1-F7", "F7-T3", "T3-T5", "T5-O1",
    "FP2-F8", "F8-T4", "T4-T6", "T6-O2",
    "A1-T3", "T3-C3", "C3-CZ", "CZ-C4", "C4-T4", "T4-A2",
    "FP1-F3", "F3-C3", "C3-P3", "P3-O1",
    "FP2-F4", "F4-C4", "C4-P4", "P4-O2",
]  # fmt: skip

FS = 250.0  # Hz, project sampling rate


@dataclass(frozen=True)
class SyntheticRecording:
    """A fake EEG recording with one focal seizure."""

    signal: np.ndarray  # (n_channels, n_samples), microvolts
    fs: float  # Hz
    channels: list[str]
    onset_s: float  # seizure onset, seconds
    offset_s: float  # seizure offset, seconds
    onset_channels: list[str]  # where the seizure starts
    ecg: np.ndarray  # (n_samples,), arbitrary units

    @property
    def duration_s(self) -> float:
        return self.signal.shape[-1] / self.fs


def _pink_noise(rng: np.random.Generator, n_ch: int, n: int) -> np.ndarray:
    """Approximate 1/f background EEG."""
    white = rng.standard_normal((n_ch, n))
    spectrum = np.fft.rfft(white, axis=-1)
    freqs = np.fft.rfftfreq(n)
    freqs[0] = freqs[1]
    spectrum /= np.sqrt(freqs)
    pink = np.fft.irfft(spectrum, n=n, axis=-1)
    return pink / pink.std(axis=-1, keepdims=True)


def make_recording(
    seed: int = 0,
    duration_s: float = 120.0,
    onset_s: float = 80.0,
    seizure_len_s: float = 20.0,
    fs: float = FS,
) -> SyntheticRecording:
    """Background 1/f EEG + a rhythmic 4 Hz seizure starting on left temporal
    channels and spreading to their neighbours 5 s later; ECG with a heart-rate
    rise shortly before onset."""
    rng = np.random.default_rng(seed)
    n = int(duration_s * fs)
    t = np.arange(n) / fs
    eeg = 20.0 * _pink_noise(rng, len(TCP_CHANNELS), n)

    onset_ch = ["F7-T3", "T3-T5"]
    spread_ch = ["FP1-F7", "T5-O1", "T3-C3"]
    offset_s = onset_s + seizure_len_s
    for ch, delay in [(c, 0.0) for c in onset_ch] + [(c, 5.0) for c in spread_ch]:
        i = TCP_CHANNELS.index(ch)
        start = onset_s + delay
        mask = (t >= start) & (t < offset_s)
        ramp = np.clip((t - start) / 3.0, 0.0, 1.0)
        eeg[i] += mask * ramp * 120.0 * np.sin(2 * np.pi * 4.0 * t)

    # ECG: 70 bpm baseline, rising to 110 bpm from 10 s before onset.
    hr = np.where(t < onset_s - 10, 70.0, 70.0 + np.clip((t - (onset_s - 10)) / 10, 0, 1) * 40)
    phase = np.cumsum(hr / 60.0) / fs
    ecg = np.exp(-(((phase % 1.0) - 0.5) ** 2) / 0.0005) + 0.05 * rng.standard_normal(n)

    return SyntheticRecording(
        signal=eeg.astype(np.float32),
        fs=fs,
        channels=list(TCP_CHANNELS),
        onset_s=onset_s,
        offset_s=offset_s,
        onset_channels=onset_ch,
        ecg=ecg.astype(np.float32),
    )


@pytest.fixture(scope="session")
def tcp_channels() -> list[str]:
    return list(TCP_CHANNELS)


@pytest.fixture(scope="session")
def fs() -> float:
    return FS


@pytest.fixture
def rng() -> np.random.Generator:
    return np.random.default_rng(1234)


@pytest.fixture(scope="session")
def synthetic_recording() -> SyntheticRecording:
    """Two minutes of 22-channel EEG with one focal seizure at 80 s."""
    return make_recording()


@pytest.fixture(scope="session")
def synthetic_splits() -> dict[str, list[str]]:
    """Patient-disjoint split lists in the same shape as splits/*.txt."""
    return {
        "train": [f"aaaaa{i:03d}" for i in range(0, 20)],
        "dev_a": [f"aaaaa{i:03d}" for i in range(20, 25)],
        "dev_b": [f"aaaaa{i:03d}" for i in range(25, 30)],
        "eval": [f"aaaaa{i:03d}" for i in range(30, 36)],
    }
