"""Referential EEG -> 22-channel TCP bipolar montage.

TUSZ EDF channels are referential, labelled like ``EEG FP1-REF`` (averaged
reference, ``*_tcp_ar*`` folders) or ``EEG FP1-LE`` (linked ears,
``*_tcp_le*`` folders). The TCP montage takes differences of neighbouring
electrodes (``FP1-F7 = FP1 - F7``); because both electrodes share the same
reference, the reference cancels and all four montage folders give the same
bipolar channels.

Folders ending in ``_a`` have no A1/A2 electrodes, so ``A1-T3`` and
``T4-A2`` are returned as NaN with ``valid = False``.
"""

from __future__ import annotations

import re
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from neuromech.data.edf_reader import EDFRecording

TCP_PAIRS: tuple[tuple[str, str], ...] = (
    ("FP1", "F7"), ("F7", "T3"), ("T3", "T5"), ("T5", "O1"),
    ("FP2", "F8"), ("F8", "T4"), ("T4", "T6"), ("T6", "O2"),
    ("A1", "T3"), ("T3", "C3"), ("C3", "CZ"), ("CZ", "C4"), ("C4", "T4"), ("T4", "A2"),
    ("FP1", "F3"), ("F3", "C3"), ("C3", "P3"), ("P3", "O1"),
    ("FP2", "F4"), ("F4", "C4"), ("C4", "P4"), ("P4", "O2"),
)  # fmt: skip
TCP_CHANNELS: tuple[str, ...] = tuple(f"{a}-{b}" for a, b in TCP_PAIRS)

ELECTRODE_ALIASES: dict[str, str] = {"T7": "T3", "T8": "T4", "P7": "T5", "P8": "T6"}
CHANNEL_LABEL_RE = re.compile(r"^(?:EEG\s+)?([A-Z0-9]+)-(?:REF|LE|AR|AVG)$", re.IGNORECASE)
ECG_LABEL_RE = re.compile(r"^(?:EEG\s+)?(?:EKG|ECG)\d*(?:-(?:REF|LE))?$", re.IGNORECASE)
MONTAGE_FOLDER_RE = re.compile(r"^\d{2}_tcp_(ar|le)(_a)?$", re.IGNORECASE)


class MontageError(ValueError):
    """Raised when a recording cannot be converted to the TCP montage."""


@dataclass
class TCPMontage:
    """A recording in the 22-channel TCP bipolar montage."""

    data: np.ndarray  # (22, n_samples), physical units; NaN where invalid
    fs: float  # Hz
    channels: tuple[str, ...]  # TCP channel names, in order
    valid: np.ndarray  # (22,) bool: False when an electrode was missing
    reference: str | None  # "ar", "le" or None if unknown

    @property
    def n_valid(self) -> int:
        return int(self.valid.sum())

    @property
    def duration_s(self) -> float:
        return self.data.shape[-1] / self.fs


def electrode_name(
    label: str,
    aliases: Mapping[str, str] = ELECTRODE_ALIASES,
    pattern: re.Pattern[str] = CHANNEL_LABEL_RE,
) -> str | None:
    """``"EEG T7-REF"`` -> ``"T3"``; ``None`` for non-EEG channels (ECG, photic…)."""
    match = pattern.match(label.strip())
    if not match:
        return None
    name = match.group(1).upper()
    if name.startswith(("EKG", "ECG")):
        return None
    return aliases.get(name, name)


def find_ecg_label(labels: Sequence[str], pattern: re.Pattern[str] = ECG_LABEL_RE) -> str | None:
    """First channel label that looks like ECG/EKG, or ``None``."""
    return next((lb for lb in labels if pattern.match(lb.strip())), None)


def montage_folder_info(path: str | Path) -> tuple[str | None, bool | None]:
    """Return ``(reference, has_ears)`` from a TUSZ montage folder in ``path``.

    ``.../02_tcp_le/x.edf`` -> ``("le", True)``; unknown -> ``(None, None)``.
    """
    for part in reversed(Path(path).parts):
        match = MONTAGE_FOLDER_RE.match(part)
        if match:
            return match.group(1).lower(), match.group(2) is None
    return None, None


def to_tcp(
    recording: EDFRecording,
    pairs: Sequence[tuple[str, str]] = TCP_PAIRS,
    aliases: Mapping[str, str] = ELECTRODE_ALIASES,
    dtype: type = np.float32,
) -> TCPMontage:
    """Convert a referential recording to the TCP bipolar montage.

    Raises:
        MontageError: if no pair can be built or electrodes use different rates.
    """
    electrodes: dict[str, str] = {}
    for label in recording.labels:
        name = electrode_name(label, aliases)
        if name is not None and name not in electrodes:
            electrodes[name] = label

    needed = {e for pair in pairs for e in pair if e in electrodes}
    if not needed:
        raise MontageError(f"no TCP electrodes found in {recording.header.path.name}")
    rates = {recording.fs[electrodes[e]] for e in needed}
    if len(rates) != 1:
        raise MontageError(f"electrodes have different sampling rates: {sorted(rates)}")
    fs = rates.pop()
    n = min(recording.signals[electrodes[e]].shape[0] for e in needed)

    data = np.full((len(pairs), n), np.nan, dtype=dtype)
    valid = np.zeros(len(pairs), dtype=bool)
    for i, (a, b) in enumerate(pairs):
        if a in electrodes and b in electrodes:
            xa = recording.signals[electrodes[a]][:n].astype(np.float64)
            xb = recording.signals[electrodes[b]][:n].astype(np.float64)
            data[i] = (xa - xb).astype(dtype)
            valid[i] = True

    reference, _ = montage_folder_info(recording.header.path)
    return TCPMontage(
        data=data,
        fs=float(fs),
        channels=tuple(f"{a}-{b}" for a, b in pairs),
        valid=valid,
        reference=reference,
    )


def extract_ecg(recording: EDFRecording) -> tuple[np.ndarray, float] | None:
    """ECG signal and its sampling rate, or ``None`` if the recording has no ECG."""
    label = find_ecg_label(recording.labels)
    if label is None:
        return None
    return recording.signals[label], recording.fs[label]
