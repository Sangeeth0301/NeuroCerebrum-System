"""Patient-disjoint TUSZ splits.

Starts from the official TUSZ ``train`` / ``dev`` / ``eval`` folders and:

1. splits ``dev`` by patient into ``dev_a`` (model selection) and ``dev_b``
   (alarm thresholds + conformal calibration), stratified so both halves get
   patients with seizures;
2. resolves patients that appear in more than one official split
   (``drop_from_train_dev`` keeps the official eval set untouched);
3. verifies that no patient is in two splits.

Split lists are plain text files in ``splits/`` (one patient ID per line) and
are committed to the repository, so every experiment uses the same patients.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from pathlib import Path

import numpy as np
import pandas as pd

from neuromech.utils.checks import assert_no_patient_overlap
from neuromech.utils.io import load_lines, save_lines

SPLIT_FILES: dict[str, str] = {
    "train": "tusz_train.txt",
    "dev_a": "tusz_dev_a.txt",
    "dev_b": "tusz_dev_b.txt",
    "eval": "tusz_eval.txt",
}
OVERLAP_POLICIES = ("drop_from_train_dev", "drop_everywhere", "error")


def make_splits(
    recordings: pd.DataFrame,
    dev_b_fraction: float = 0.5,
    seed: int = 42,
    overlap_policy: str = "drop_from_train_dev",
) -> tuple[dict[str, list[str]], list[str]]:
    """Build patient lists from the audit's recordings table.

    Args:
        recordings: needs columns ``split``, ``patient``, ``n_seizures``.
        dev_b_fraction: share of dev patients that go to ``dev_b``.
        seed: RNG seed (splits must be reproducible).
        overlap_policy: what to do with patients in several official splits.

    Returns:
        ``(splits, dropped)`` — split name -> sorted patient IDs, and the
        patients removed because of overlap.
    """
    if overlap_policy not in OVERLAP_POLICIES:
        raise ValueError(f"overlap_policy must be one of {OVERLAP_POLICIES}")
    if not 0.0 < dev_b_fraction < 1.0:
        raise ValueError("dev_b_fraction must be between 0 and 1")

    per_split = {
        s: set(recordings.loc[recordings["split"] == s, "patient"])
        for s in ("train", "dev", "eval")
    }
    counts = recordings.groupby("patient")["split"].nunique()
    overlapping = sorted(counts[counts > 1].index)
    if overlapping and overlap_policy == "error":
        raise ValueError(f"patients in several official splits: {overlapping}")

    dropped = list(overlapping)
    if overlap_policy == "drop_from_train_dev":
        for s in ("train", "dev"):
            per_split[s] -= per_split["eval"]
        per_split["train"] -= per_split["dev"]  # dev wins over train
    elif overlap_policy == "drop_everywhere":
        for s in per_split:
            per_split[s] -= set(overlapping)

    seizures = recordings.groupby("patient")["n_seizures"].sum()
    rng = np.random.default_rng(seed)
    dev_a: list[str] = []
    dev_b: list[str] = []
    for has_seizures in (True, False):
        group = sorted(p for p in per_split["dev"] if (seizures.get(p, 0) > 0) == has_seizures)
        rng.shuffle(group)
        k = int(round(len(group) * dev_b_fraction))
        dev_b += group[:k]
        dev_a += group[k:]

    splits = {
        "train": sorted(per_split["train"]),
        "dev_a": sorted(dev_a),
        "dev_b": sorted(dev_b),
        "eval": sorted(per_split["eval"]),
    }
    assert_no_patient_overlap(splits)
    return splits, dropped


def write_splits(
    splits: Mapping[str, Sequence[str]],
    folder: str | Path,
    header: str = "",
) -> dict[str, Path]:
    """Write one text file per split; returns the paths."""
    assert_no_patient_overlap(splits)
    folder = Path(folder)
    out: dict[str, Path] = {}
    for name, patients in splits.items():
        lines = [f"# {name}: {len(patients)} patients"]
        if header:
            lines += [f"# {ln}" for ln in header.splitlines()]
        out[name] = save_lines(
            lines + list(patients), folder / SPLIT_FILES.get(name, f"{name}.txt")
        )
    return out


def load_splits(
    folder: str | Path, names: Sequence[str] = tuple(SPLIT_FILES)
) -> dict[str, list[str]]:
    """Read split files written by :func:`write_splits` and re-check them for leakage."""
    folder = Path(folder)
    splits = {n: load_lines(folder / SPLIT_FILES.get(n, f"{n}.txt")) for n in names}
    assert_no_patient_overlap(splits)
    return splits


def split_of(patient: str, splits: Mapping[str, Sequence[str]]) -> str | None:
    """Name of the split containing ``patient`` (``None`` if excluded)."""
    return next((name for name, pats in splits.items() if patient in pats), None)
