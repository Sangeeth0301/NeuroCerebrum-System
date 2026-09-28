"""Tests for neuromech.data.edf_reader (P1)."""

from __future__ import annotations

import numpy as np
import pytest

from neuromech.data.edf_reader import EDFError, read_edf, read_edf_header, write_edf


def test_roundtrip_preserves_signal(tmp_path, rng):
    x = rng.normal(0, 50, size=(3, 250 * 10))  # 10 s, microvolts
    labels = ["EEG FP1-REF", "EEG F7-REF", "EEG T3-REF"]
    path = write_edf(tmp_path / "rec.edf", x, fs=250, labels=labels)

    rec = read_edf(path)
    assert rec.labels == labels
    assert all(v == 250.0 for v in rec.fs.values())
    stacked, fs = rec.stack()
    assert fs == 250.0 and stacked.shape == x.shape
    # 16-bit quantisation over the channel's range: error well below 0.1 µV here.
    step = (x.max(axis=1) - x.min(axis=1)) / 65535
    assert np.all(np.abs(stacked - x) <= step[:, None] + 0.02)


def test_header_only(tmp_path, rng):
    x = rng.normal(size=(2, 256 * 7 + 100))  # not a whole number of seconds
    path = write_edf(tmp_path / "h.edf", x, fs=256, labels=["EEG CZ-LE", "EEG EKG1-LE"])
    hdr = read_edf_header(path)
    assert hdr.n_signals == 2
    assert hdr.n_records == 8  # padded to whole records
    assert hdr.duration_s == 8.0
    np.testing.assert_allclose(hdr.fs, [256, 256])
    assert hdr.index("EEG EKG1-LE") == 1


def test_select_channels_by_label_and_index(tmp_path, rng):
    x = rng.normal(size=(3, 500))
    labels = ["A", "B", "C"]
    path = write_edf(tmp_path / "s.edf", x, fs=250, labels=labels)
    assert read_edf(path, channels=["C", "A"]).labels == ["C", "A"]
    assert read_edf(path, channels=[1]).labels == ["B"]
    with pytest.raises(KeyError):
        read_edf(path, channels=["missing"])


def test_mixed_sampling_rates(tmp_path):
    """Hand-build a file whose second channel runs at half the rate."""
    path = write_edf(tmp_path / "m.edf", np.zeros((2, 500)), fs=250, labels=["EEG", "ECG"])
    raw = bytearray(path.read_bytes())
    ns = 2
    spr_offset = 256 + ns * (16 + 80 + 8 + 8 + 8 + 8 + 8 + 80)
    raw[spr_offset + 8 : spr_offset + 16] = b"125     "
    n_records = 2
    body = np.concatenate(
        [np.concatenate([np.full(250, 100, "<i2"), np.full(125, -100, "<i2")])] * n_records
    )
    header_len = 256 * (ns + 1)
    path.write_bytes(bytes(raw[:header_len]) + body.tobytes())

    rec = read_edf(path)
    assert rec.fs == {"EEG": 250.0, "ECG": 125.0}
    assert rec.signals["EEG"].shape == (500,) and rec.signals["ECG"].shape == (250,)
    with pytest.raises(EDFError):
        rec.stack()


def test_rejects_non_edf(tmp_path):
    bad = tmp_path / "bad.edf"
    bad.write_bytes(b"not an edf")
    with pytest.raises(EDFError):
        read_edf_header(bad)


def test_write_rejects_fractional_rate(tmp_path):
    with pytest.raises(ValueError):
        write_edf(tmp_path / "x.edf", np.zeros((1, 10)), fs=250.5, labels=["A"])
