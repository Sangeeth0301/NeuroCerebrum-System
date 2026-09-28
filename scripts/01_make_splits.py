"""P1 · Build patient-disjoint TUSZ splits from the audit.

Reads ``data/processed/metadata.parquet`` (from 00_audit_tusz.py) and writes
``splits/tusz_train.txt``, ``tusz_dev_a.txt``, ``tusz_dev_b.txt`` and
``tusz_eval.txt``. Commit the split files: every experiment must use them.

Usage::

    python scripts/01_make_splits.py
    python scripts/01_make_splits.py data.dry_run=true   # uses the dry-run audit output
"""

from __future__ import annotations

from pathlib import Path

import hydra
import pandas as pd
from omegaconf import DictConfig

from neuromech.data.splits import make_splits, write_splits
from neuromech.utils.logging import get_logger

log = get_logger("neuromech.splits")


def load_table(path: Path) -> pd.DataFrame:
    if path.exists():
        return pd.read_parquet(path)
    csv = path.with_suffix(".csv")
    if csv.exists():
        return pd.read_csv(csv)
    raise SystemExit(f"{path} not found. Run scripts/00_audit_tusz.py first.")


@hydra.main(config_path="../configs", config_name="config", version_base="1.3")
def main(cfg: DictConfig) -> None:
    data = cfg.data
    if data.dry_run:
        base = Path(cfg.paths.cache) / "dry_run"
        metadata_path, out_dir = base / "metadata.parquet", base / "splits"
    else:
        metadata_path, out_dir = Path(cfg.paths.metadata), Path(cfg.paths.splits)

    recordings = load_table(metadata_path)
    splits, dropped = make_splits(
        recordings,
        dev_b_fraction=float(data.splits.dev_b_fraction),
        seed=int(data.splits.seed),
        overlap_policy=str(data.splits.overlap_policy),
    )
    header = (
        f"TUSZ {data.version} | seed {data.splits.seed} | "
        f"dev_b_fraction {data.splits.dev_b_fraction} | overlap_policy {data.splits.overlap_policy}\n"
        f"patients dropped for split overlap: {len(dropped)}"
    )
    paths = write_splits(splits, out_dir, header=header)
    for name, pats in splits.items():
        log.info("%-6s %4d patients -> %s", name, len(pats), paths[name])
    if dropped:
        log.warning("Patients in several official splits handled by policy: %s", dropped)


if __name__ == "__main__":
    main()
