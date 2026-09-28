"""Split tests: no patient may ever appear in two splits (P1)."""

from __future__ import annotations

import pandas as pd
import pytest

from neuromech.data.splits import load_splits, make_splits, split_of, write_splits
from neuromech.utils.checks import LeakageError


def _recordings(overlap: bool = False) -> pd.DataFrame:
    rows = []
    for i in range(20):
        rows.append({"split": "train", "patient": f"tr{i:02d}", "n_seizures": i % 3})
    for i in range(10):
        rows.append({"split": "dev", "patient": f"dv{i:02d}", "n_seizures": 1 if i < 4 else 0})
    for i in range(8):
        rows.append({"split": "eval", "patient": f"ev{i:02d}", "n_seizures": i % 2})
    if overlap:
        rows.append({"split": "train", "patient": "ev00", "n_seizures": 2})  # eval patient in train
        rows.append({"split": "train", "patient": "dv00", "n_seizures": 0})  # dev patient in train
    return pd.DataFrame(rows)


def test_splits_are_disjoint_and_complete():
    splits, dropped = make_splits(_recordings())
    assert dropped == []
    assert len(splits["train"]) == 20 and len(splits["eval"]) == 8
    assert len(splits["dev_a"]) + len(splits["dev_b"]) == 10
    all_patients = [p for pats in splits.values() for p in pats]
    assert len(all_patients) == len(set(all_patients))


def test_both_dev_halves_get_seizure_patients():
    splits, _ = make_splits(_recordings())
    seizure_patients = {f"dv{i:02d}" for i in range(4)}
    assert seizure_patients & set(splits["dev_a"])
    assert seizure_patients & set(splits["dev_b"])


def test_splits_are_reproducible():
    a, _ = make_splits(_recordings(), seed=7)
    b, _ = make_splits(_recordings(), seed=7)
    c, _ = make_splits(_recordings(), seed=8)
    assert a == b
    assert a["dev_a"] != c["dev_a"] or a["dev_b"] != c["dev_b"]


def test_overlap_keeps_eval_untouched():
    splits, dropped = make_splits(_recordings(overlap=True))
    assert dropped == ["dv00", "ev00"]
    assert "ev00" in splits["eval"] and "ev00" not in splits["train"]
    assert "dv00" not in splits["train"] and split_of("dv00", splits) in {"dev_a", "dev_b"}


def test_overlap_policies():
    splits, _ = make_splits(_recordings(overlap=True), overlap_policy="drop_everywhere")
    assert split_of("ev00", splits) is None and split_of("dv00", splits) is None
    with pytest.raises(ValueError):
        make_splits(_recordings(overlap=True), overlap_policy="error")
    with pytest.raises(ValueError):
        make_splits(_recordings(), overlap_policy="unknown")
    with pytest.raises(ValueError):
        make_splits(_recordings(), dev_b_fraction=1.0)


def test_write_load_roundtrip(tmp_path):
    splits, _ = make_splits(_recordings())
    paths = write_splits(splits, tmp_path, header="seed 42")
    assert paths["train"].name == "tusz_train.txt"
    assert paths["train"].read_text().startswith("# train: 20 patients")
    assert load_splits(tmp_path) == splits


def test_leaky_files_are_rejected(tmp_path):
    splits, _ = make_splits(_recordings())
    write_splits(splits, tmp_path)
    leaky = tmp_path / "tusz_eval.txt"
    leaky.write_text(leaky.read_text() + splits["train"][0] + "\n")
    with pytest.raises(LeakageError):
        load_splits(tmp_path)
    with pytest.raises(LeakageError):
        write_splits({"train": ["p1"], "eval": ["p1"]}, tmp_path / "x")
