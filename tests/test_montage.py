"""Tests for neuromech.data.montage (P1)."""

from __future__ import annotations

import numpy as np
import pytest

from neuromech.data.edf_reader import read_edf, write_edf
from neuromech.data.montage import (
    TCP_CHANNELS,
    MontageError,
    electrode_name,
    extract_ecg,
    find_ecg_label,
    montage_folder_info,
    to_tcp,
)

ELECTRODES = [
    "FP1", "FP2", "F3", "F4", "C3", "C4", "P3", "P4", "O1", "O2",
    "F7", "F8", "T3", "T4", "T5", "T6", "A1", "A2", "FZ", "CZ", "PZ",
]  # fmt: skip


def _write_referential(path, rng, suffix="REF", electrodes=ELECTRODES, ecg=True, fs=250):
    """Each electrode gets its own sine so bipolar differences are checkable."""
    t = np.arange(fs * 4) / fs
    signals, labels = [], []
    for k, e in enumerate(electrodes):
        signals.append(10 * (k + 1) * np.sin(2 * np.pi * (k + 1) * t))
        labels.append(f"EEG {e}-{suffix}")
    if ecg:
        signals.append(rng.normal(size=t.size))
        labels.append(f"EEG EKG1-{suffix}")
    return write_edf(path, np.array(signals), fs=fs, labels=labels), dict(
        zip(labels, signals, strict=True)
    )


@pytest.mark.parametrize(
    ("label", "expected"),
    [
        ("EEG FP1-REF", "FP1"),
        ("EEG T7-LE", "T3"),  # 10-10 alias
        ("EEG P8-REF", "T6"),
        ("EEG EKG1-REF", None),  # ECG is not an electrode
        ("PHOTIC-REF", "PHOTIC"),
        ("IBI", None),
        ("fp2-le", "FP2"),
    ],
)
def test_electrode_name(label, expected):
    assert electrode_name(label) == expected


def test_find_ecg_label():
    assert find_ecg_label(["EEG FP1-REF", "EEG EKG1-REF"]) == "EEG EKG1-REF"
    assert find_ecg_label(["ECG"]) == "ECG"
    assert find_ecg_label(["EEG FP1-REF"]) is None


@pytest.mark.parametrize(
    ("folder", "expected"),
    [
        ("01_tcp_ar", ("ar", True)),
        ("02_tcp_le", ("le", True)),
        ("03_tcp_ar_a", ("ar", False)),
        ("04_tcp_le_a", ("le", False)),
        ("somewhere", (None, None)),
    ],
)
def test_montage_folder_info(tmp_path, folder, expected):
    assert (
        montage_folder_info(tmp_path / "edf" / "train" / "p" / "s" / folder / "x.edf") == expected
    )


@pytest.mark.parametrize("suffix", ["REF", "LE"])
def test_to_tcp_full(tmp_path, rng, suffix):
    folder = "01_tcp_ar" if suffix == "REF" else "02_tcp_le"
    path, raw = _write_referential(tmp_path / folder / "r.edf", rng, suffix=suffix)
    tcp = to_tcp(read_edf(path))

    assert tcp.channels == TCP_CHANNELS and tcp.data.shape == (22, 1000)
    assert tcp.valid.all() and tcp.fs == 250.0
    assert tcp.reference == ("ar" if suffix == "REF" else "le")
    i = TCP_CHANNELS.index("FP1-F7")
    expected = raw[f"EEG FP1-{suffix}"] - raw[f"EEG F7-{suffix}"]
    np.testing.assert_allclose(tcp.data[i], expected, atol=0.05)


def test_to_tcp_without_ear_electrodes(tmp_path, rng):
    no_ears = [e for e in ELECTRODES if e not in {"A1", "A2"}]
    path, _ = _write_referential(tmp_path / "03_tcp_ar_a" / "r.edf", rng, electrodes=no_ears)
    tcp = to_tcp(read_edf(path))
    missing = {TCP_CHANNELS[i] for i in np.flatnonzero(~tcp.valid)}
    assert missing == {"A1-T3", "T4-A2"}
    assert tcp.n_valid == 20
    assert np.isnan(tcp.data[TCP_CHANNELS.index("A1-T3")]).all()


def test_extract_ecg(tmp_path, rng):
    path, raw = _write_referential(tmp_path / "e.edf", rng)
    ecg, fs = extract_ecg(read_edf(path))
    assert fs == 250.0 and ecg.shape == (1000,)
    path2, _ = _write_referential(tmp_path / "n.edf", rng, ecg=False)
    assert extract_ecg(read_edf(path2)) is None


def test_no_electrodes_raises(tmp_path):
    path = write_edf(tmp_path / "x.edf", np.zeros((1, 250)), fs=250, labels=["EEG EKG1-REF"])
    with pytest.raises(MontageError):
        to_tcp(read_edf(path))
