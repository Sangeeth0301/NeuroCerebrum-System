"""Tests for neuromech.data.audit and neuromech.data.synthetic (P1)."""

from __future__ import annotations

import pandas as pd
import pytest

from neuromech.data.audit import (
    audit_dataset,
    iter_recordings,
    preictal_table,
    recommend_hazard_bins,
    render_markdown,
    summarize,
)
from neuromech.data.synthetic import make_fake_tusz


@pytest.fixture(scope="module")
def fake_tusz(tmp_path_factory):
    root = tmp_path_factory.mktemp("tusz")
    return make_fake_tusz(root, {"train": 3, "dev": 2, "eval": 2}, duration_s=90, seed=3)


def test_fake_tree_has_tusz_layout(fake_tusz):
    recs = list(iter_recordings(fake_tusz))
    assert len(recs) == 14  # 7 patients x 2 sessions
    rp = recs[0]
    assert rp.split in {"train", "dev", "eval"}
    assert rp.montage.endswith(("tcp_ar", "tcp_le", "tcp_ar_a", "tcp_le_a"))
    assert rp.path.with_suffix(".csv").exists() and rp.path.with_suffix(".csv_bi").exists()


def test_audit_tables(fake_tusz):
    recordings, seizures, errors = audit_dataset(fake_tusz)
    assert errors == []
    assert len(recordings) == 14
    assert set(recordings["split"]) == {"train", "dev", "eval"}
    assert recordings["duration_s"].eq(90).all()
    assert recordings["fs"].eq(250).all()
    assert recordings["has_ecg"].any() and not recordings["has_ecg"].all()
    assert recordings["has_channel_annotations"].all()
    assert recordings["n_seizures"].sum() == len(seizures)
    if len(seizures):
        assert (seizures["offset_s"] > seizures["onset_s"]).all()
        assert (seizures["preictal_available_s"] >= 0).all()
        assert set(seizures["group"]) <= {"focal", "generalized"}
        assert seizures["onset_channels"].str.len().gt(0).all()


def test_audit_limit_and_errors(fake_tusz):
    rec, _, _ = audit_dataset(fake_tusz, limit=3)
    assert len(rec) == 3
    broken = next(iter_recordings(fake_tusz)).path
    backup = broken.read_bytes()
    try:
        broken.write_bytes(b"corrupt")
        rec, _, errors = audit_dataset(fake_tusz)
        assert len(errors) == 1 and len(rec) == 13
    finally:
        broken.write_bytes(backup)


def test_missing_root_raises(tmp_path):
    with pytest.raises(FileNotFoundError):
        list(iter_recordings(tmp_path / "nope"))


def test_preictal_table_and_bins():
    seizures = pd.DataFrame(
        {
            "split": ["train"] * 150 + ["eval"] * 30,
            "patient": [f"p{i % 40}" for i in range(180)],
            "preictal_available_s": [600.0] * 120 + [60.0] * 30 + [900.0] * 25 + [30.0] * 5,
        }
    )
    table = preictal_table(seizures, [1, 5, 10, 15])
    assert table.set_index("min_preictal_min").loc[1, "all"] == 175
    assert table.set_index("min_preictal_min").loc[10, "train"] == 120
    assert recommend_hazard_bins(table) == [1, 5, 10]


def test_summary_and_markdown(fake_tusz):
    recordings, seizures, errors = audit_dataset(fake_tusz)
    summary = summarize(recordings, seizures, [1, 2, 5])
    assert summary["n_patients"] == 7
    assert summary["patients_in_multiple_splits"] == []
    md = render_markdown(summary, errors, str(fake_tusz))
    assert md.startswith("# TUSZ Data Audit")
    assert "## By split" in md and "Recordings: **14**" in md


def test_summary_empty():
    assert summarize(pd.DataFrame(), pd.DataFrame(), [1]) == {"n_recordings": 0}
