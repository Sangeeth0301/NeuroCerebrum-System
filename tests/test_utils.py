"""Tests for neuromech.utils (P0)."""

from __future__ import annotations

import numpy as np
import pytest

from neuromech import __version__
from neuromech.utils import (
    CausalityError,
    LeakageError,
    Timer,
    assert_causal,
    assert_no_patient_overlap,
    get_logger,
    io,
    set_seed,
)
from neuromech.utils.timing import realtime_factor
from neuromech.utils.tracking import Tracker


def test_version_is_set():
    assert isinstance(__version__, str) and __version__.count(".") == 2


# ── causality ────────────────────────────────────────────────────────────────
def test_causal_filter_passes(synthetic_recording):
    def moving_average_past(x: np.ndarray) -> np.ndarray:
        out = np.empty_like(x)
        for k in range(x.shape[-1]):
            out[..., k] = x[..., max(0, k - 9) : k + 1].mean(axis=-1)
        return out

    assert_causal(moving_average_past, synthetic_recording.signal[:2, :500])


def test_non_causal_filter_is_caught(synthetic_recording):
    def centred_average(x: np.ndarray) -> np.ndarray:
        kernel = np.ones(11) / 11
        return np.stack([np.convolve(ch, kernel, mode="same") for ch in x])

    with pytest.raises(CausalityError):
        assert_causal(centred_average, synthetic_recording.signal[:2, :500])


def test_assert_causal_rejects_bad_cut():
    with pytest.raises(ValueError):
        assert_causal(lambda x: x, np.zeros(10), cut=10)


# ── leakage ──────────────────────────────────────────────────────────────────
def test_disjoint_splits_pass(synthetic_splits):
    assert_no_patient_overlap(synthetic_splits)


def test_overlap_is_caught(synthetic_splits):
    leaky = dict(synthetic_splits)
    leaky["eval"] = [*synthetic_splits["eval"], synthetic_splits["train"][0]]
    with pytest.raises(LeakageError, match="aaaaa000"):
        assert_no_patient_overlap(leaky)


# ── seed / timing / logging ──────────────────────────────────────────────────
def test_set_seed_repeatable():
    # The legacy global API is exactly what set_seed must control.
    set_seed(7)
    a = np.random.rand(3)  # noqa: NPY002
    set_seed(7)
    b = np.random.rand(3)  # noqa: NPY002
    np.testing.assert_array_equal(a, b)


def test_timer_and_realtime_factor():
    with Timer("noop") as t:
        sum(range(1000))
    assert t.elapsed >= 0.0
    assert realtime_factor(1.0, 10.0) == pytest.approx(0.1)
    with pytest.raises(ValueError):
        realtime_factor(1.0, 0.0)


def test_get_logger_no_duplicate_handlers():
    a = get_logger("neuromech.test")
    b = get_logger("neuromech.test")
    assert a is b and len(a.handlers) == 1


# ── io ───────────────────────────────────────────────────────────────────────
def test_io_roundtrips(tmp_path):
    io.save_json({"x": np.float32(1.5), "arr": np.arange(3)}, tmp_path / "a.json")
    assert io.load_json(tmp_path / "a.json") == {"x": 1.5, "arr": [0, 1, 2]}

    io.save_yaml({"fs": 250}, tmp_path / "b.yaml")
    assert io.load_yaml(tmp_path / "b.yaml") == {"fs": 250}

    io.save_lines(["# comment", "aaaaa001", "", "aaaaa002"], tmp_path / "s.txt")
    assert io.load_lines(tmp_path / "s.txt") == ["aaaaa001", "aaaaa002"]

    io.save_npz(tmp_path / "c.npz", eeg=np.ones((2, 3)))
    np.testing.assert_array_equal(io.load_npz(tmp_path / "c.npz")["eeg"], np.ones((2, 3)))


def test_tracker_json_backend(tmp_path):
    with Tracker("unit", run_name="r1", output_dir=tmp_path, use_mlflow=False) as tr:
        tr.log_params({"lr": 1e-3})
        tr.log_metrics({"f1": 0.5}, step=1)
    record = io.load_json(tmp_path / "unit" / "r1.json")
    assert record["params"]["lr"] == 1e-3
    assert record["metrics"]["f1"][0]["value"] == 0.5


# ── synthetic fixture sanity ─────────────────────────────────────────────────
def test_synthetic_recording_shape(synthetic_recording, tcp_channels, fs):
    rec = synthetic_recording
    assert rec.signal.shape == (len(tcp_channels), int(120 * fs))
    assert rec.ecg.shape == (rec.signal.shape[1],)
    onset = int(rec.onset_s * fs)
    i = tcp_channels.index("F7-T3")
    assert rec.signal[i, onset + 750 : onset + 1500].std() > 2 * rec.signal[i, :onset].std()
