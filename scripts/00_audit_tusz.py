"""P1 · Audit the TUSZ dataset.

Reads EDF headers and annotation files (not the signals) and writes:

- ``data/processed/metadata.parquet``  one row per recording
- ``data/processed/seizures.parquet``  one row per seizure
- ``DOCS/DATA_AUDIT.md``               human-readable summary + recommended hazard bins

Usage::

    python scripts/00_audit_tusz.py                       # real TUSZ at TUSZ_ROOT (.env)
    python scripts/00_audit_tusz.py data.audit_limit=50   # quick check on 50 files
    python scripts/00_audit_tusz.py data.dry_run=true     # synthetic TUSZ, no data needed

Dry runs write only under ``data/cache/dry_run/`` and never touch DOCS/.
"""

from __future__ import annotations

from pathlib import Path

import hydra
import pandas as pd
from omegaconf import DictConfig
from tqdm import tqdm

from neuromech.data.audit import audit_dataset, render_markdown, summarize
from neuromech.data.synthetic import make_fake_tusz
from neuromech.utils.io import ensure_dir
from neuromech.utils.logging import get_logger

log = get_logger("neuromech.audit")


def save_table(df: pd.DataFrame, path: Path) -> Path:
    """Parquet when pyarrow is installed, CSV otherwise."""
    ensure_dir(path.parent)
    try:
        df.to_parquet(path, index=False)
        return path
    except ImportError:
        csv = path.with_suffix(".csv")
        df.to_csv(csv, index=False)
        return csv


@hydra.main(config_path="../configs", config_name="config", version_base="1.3")
def main(cfg: DictConfig) -> None:
    data = cfg.data
    if data.dry_run:
        out_dir = Path(cfg.paths.cache) / "dry_run"
        root = make_fake_tusz(out_dir / "tusz", seed=int(cfg.seed))
        metadata_path = out_dir / "metadata.parquet"
        seizures_path = out_dir / "seizures.parquet"
        report_path = out_dir / "DATA_AUDIT.md"
        log.info("DRY RUN: synthetic TUSZ created at %s", root)
    else:
        root = Path(data.root)
        metadata_path = Path(cfg.paths.metadata)
        seizures_path = Path(data.seizures_table)
        report_path = Path(data.audit_report)

    log.info("Auditing %s", root)
    recordings, seizures, errors = audit_dataset(
        root, data.edf_subdir, limit=data.audit_limit, progress=lambda x: tqdm(x, unit="file")
    )
    if recordings.empty:
        raise SystemExit(f"No EDF files found under {root}/{data.edf_subdir}. Check TUSZ_ROOT.")

    summary = summarize(recordings, seizures, list(data.audit_preictal_minutes))
    saved_meta = save_table(recordings, metadata_path)
    saved_sz = save_table(seizures, seizures_path)
    ensure_dir(report_path.parent)
    report_path.write_text(render_markdown(summary, errors, str(root)), encoding="utf-8")

    log.info(
        "%d recordings, %d patients, %.1f h, %d seizures, %d unreadable",
        summary["n_recordings"],
        summary.get("n_patients", 0),
        summary.get("hours", 0.0),
        len(seizures),
        len(errors),
    )
    log.info("Recommended hazard bins (min): %s", summary.get("recommended_bins_min"))
    log.info("Wrote %s, %s, %s", saved_meta, saved_sz, report_path)


if __name__ == "__main__":
    main()
