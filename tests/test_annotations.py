"""Tests for neuromech.data.annotations (P1)."""

from __future__ import annotations

import pytest

from neuromech.data.annotations import (
    AnnotationError,
    Event,
    annotation_paths,
    extract_seizures,
    read_annotation,
    write_annotation,
)

TUSZ_CSV = """# version = csv_v1.0.0
# bname = aaaaaaac_s001_t000
# duration = 301.00 secs
# montage_file = $NEDC_NFC/lib/nedc_eas_default_montage.txt
#
channel,start_time,stop_time,label,confidence
FP1-F7,0.0000,36.8868,bckg,1.0000
FP1-F7,36.8868,112.0000,cpsz,1.0000
F7-T3,36.2000,112.0000,cpsz,1.0000
T3-T5,41.5000,110.0000,cpsz,1.0000
FP1-F7,112.0000,301.0000,bckg,1.0000
"""

TUSZ_CSV_BI = """# version = csv_v1.0.0
# bname = aaaaaaac_s001_t000
# duration = 301.00 secs
#
channel,start_time,stop_time,label,confidence
TERM,0.0000,36.2000,bckg,1.0000
TERM,36.2000,112.0000,seiz,1.0000
TERM,112.0000,301.0000,bckg,1.0000
"""


@pytest.fixture
def csv_pair(tmp_path):
    edf = tmp_path / "aaaaaaac_s001_t000.edf"
    edf.write_bytes(b"")
    (tmp_path / "aaaaaaac_s001_t000.csv").write_text(TUSZ_CSV)
    (tmp_path / "aaaaaaac_s001_t000.csv_bi").write_text(TUSZ_CSV_BI)
    return edf


def test_parse_channel_file(csv_pair):
    ann = read_annotation(csv_pair.with_suffix(".csv"))
    assert ann.kind == "channel"
    assert ann.duration_s == 301.0
    assert ann.meta["bname"] == "aaaaaaac_s001_t000"
    assert len(ann.events) == 5
    assert ann.channels == ["F7-T3", "FP1-F7", "T3-T5"]
    assert len(ann.seizure_events()) == 3


def test_channel_seizure_onset_zone_and_type(csv_pair):
    ann = read_annotation(csv_pair.with_suffix(".csv"))
    (sz,) = extract_seizures(ann)
    assert sz.onset == pytest.approx(36.2)
    assert sz.offset == pytest.approx(112.0)
    assert sz.label == "cpsz" and sz.group == "focal" and sz.four_class == "CF"
    # T3-T5 starts 5.3 s later: recruited, not onset.
    assert sz.onset_channels == ["F7-T3", "FP1-F7"]
    assert set(sz.channels) == {"F7-T3", "FP1-F7", "T3-T5"}


def test_term_file_matches_channel_file(csv_pair):
    term = read_annotation(csv_pair.with_suffix(".csv_bi"))
    assert term.kind == "term"
    (sz,) = extract_seizures(term)
    assert (sz.onset, sz.offset, sz.label, sz.channels) == (36.2, 112.0, "seiz", {})


def test_annotation_paths(csv_pair, tmp_path):
    paths = annotation_paths(csv_pair)
    assert paths["channel"].name.endswith(".csv") and paths["term"].name.endswith(".csv_bi")
    lonely = tmp_path / "other.edf"
    assert annotation_paths(lonely) == {"channel": None, "term": None}


def test_merge_gap_and_dominant_label(tmp_path):
    events = [
        Event("TERM", 10, 20, "fnsz"),
        Event("TERM", 22, 40, "tcsz"),  # 2 s gap, longer -> dominant
        Event("TERM", 100, 110, "seiz"),
    ]
    path = write_annotation(tmp_path / "x.csv_bi", events, duration_s=200)
    ann = read_annotation(path)
    assert len(extract_seizures(ann, merge_gap=0)) == 3
    merged = extract_seizures(ann, merge_gap=5)
    assert len(merged) == 2
    assert merged[0].label == "tcsz" and merged[0].group == "generalized"
    assert merged[1].label == "seiz" and merged[1].group == "unknown"
    assert merged[1].four_class is None


def test_roundtrip_write_read(tmp_path):
    events = [Event("FP1-F7", 1.5, 3.25, "gnsz", 0.9)]
    ann = read_annotation(write_annotation(tmp_path / "r.csv", events, duration_s=10))
    assert ann.events == events and ann.duration_s == 10.0


@pytest.mark.parametrize(
    "body",
    [
        "# only comments\n",
        "channel,start_time,stop_time,label,confidence\nFP1-F7,5,2,fnsz,1\n",
        "channel,start_time,stop_time,label,confidence\nFP1-F7,a,2,fnsz,1\n",
        "chan,start,stop\nFP1-F7,1,2\n",
    ],
)
def test_malformed_files_raise(tmp_path, body):
    path = tmp_path / "bad.csv"
    path.write_text(body)
    with pytest.raises(AnnotationError):
        read_annotation(path)
