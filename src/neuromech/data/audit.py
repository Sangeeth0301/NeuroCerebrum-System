"""TUSZ data audit.

Scans a TUSZ v2 tree and produces two tables plus a summary:

- **recordings**: one row per EDF file (split, patient, session, montage,
  duration, sampling rate, ECG, annotation files, seizure count …).
- **seizures**: one row per seizure (onset, offset, type, group, channels,
  onset channels, EEG available before and after it …).
- **summary**: counts and the preictal-availability table used to choose the
  forecasting (hazard) bins.

Only headers and annotation files are read, so the audit is fast.

Preictal availability is measured **within one EDF file**: the EEG between the
start of the file (or the end of the previous seizure in that file) and the
onset. TUSZ sessions can be split across files with gaps, so this is the
conservative choice.
"""

from __future__ import annotations

import re
from collections.abc import Callable, Iterable, Iterator, Sequence
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd

from neuromech.data.annotations import (
    AnnotationError,
    annotation_paths,
    extract_seizures,
    read_annotation,
)
from neuromech.data.edf_reader import EDFError, read_edf_header
from neuromech.data.montage import electrode_name, find_ecg_label, montage_folder_info

_SESSION_RE = re.compile(r"^s(\d+)(?:_(\d{4}))?$")


@dataclass(frozen=True)
class RecordingPath:
    """Where one EDF sits in the TUSZ tree."""

    path: Path
    split: str
    patient: str
    session: str
    montage: str


def iter_recordings(root: str | Path, edf_subdir: str = "edf") -> Iterator[RecordingPath]:
    """Yield every EDF under ``<root>/<edf_subdir>/<split>/<patient>/<session>/<montage>/``."""
    base = Path(root) / edf_subdir
    if not base.is_dir():
        raise FileNotFoundError(f"TUSZ folder not found: {base}")
    for edf in sorted(base.rglob("*.edf")):
        rel = edf.relative_to(base).parts
        if len(rel) < 5:
            continue  # not in the expected layout
        split, patient, session, montage = rel[0], rel[1], rel[2], rel[-2]
        yield RecordingPath(edf, split, patient, session, montage)


def audit_recording(rp: RecordingPath) -> tuple[dict, list[dict]]:
    """Audit one EDF + its annotations. Returns (recording row, seizure rows)."""
    header = read_edf_header(rp.path)
    eeg_idx = [i for i, lb in enumerate(header.labels) if electrode_name(lb) is not None]
    eeg_fs = header.fs[eeg_idx] if eeg_idx else np.array([np.nan])
    ecg_label = find_ecg_label(header.labels)
    reference, has_ears = montage_folder_info(rp.path)
    ann_paths = annotation_paths(rp.path)
    session_match = _SESSION_RE.match(rp.session)

    row = {
        "split": rp.split,
        "patient": rp.patient,
        "session": rp.session,
        "session_year": int(session_match.group(2))
        if session_match and session_match.group(2)
        else None,
        "montage": rp.montage,
        "reference": reference,
        "has_ear_electrodes": has_ears,
        "file": rp.path.name,
        "path": str(rp.path),
        "duration_s": header.duration_s,
        "fs": float(np.nanmedian(eeg_fs)),
        "fs_mixed": bool(np.unique(eeg_fs).size > 1),
        "n_signals": header.n_signals,
        "n_eeg_channels": len(eeg_idx),
        "has_ecg": ecg_label is not None,
        "ecg_fs": float(header.fs[header.index(ecg_label)]) if ecg_label else None,
        "has_channel_annotations": ann_paths["channel"] is not None,
        "has_term_annotations": ann_paths["term"] is not None,
        "n_seizures": 0,
        "seizure_seconds": 0.0,
        "seizure_types": "",
    }

    source = ann_paths["channel"] or ann_paths["term"]
    if source is None:
        return row, []
    seizures = extract_seizures(read_annotation(source))
    row["n_seizures"] = len(seizures)
    row["seizure_seconds"] = float(sum(s.duration for s in seizures))
    row["seizure_types"] = ",".join(sorted({s.label for s in seizures}))

    rows: list[dict] = []
    prev_end = 0.0
    for k, sz in enumerate(seizures):
        next_start = seizures[k + 1].onset if k + 1 < len(seizures) else header.duration_s
        rows.append(
            {
                "split": rp.split,
                "patient": rp.patient,
                "session": rp.session,
                "file": rp.path.name,
                "index_in_file": k,
                "onset_s": sz.onset,
                "offset_s": sz.offset,
                "duration_s": sz.duration,
                "type": sz.label,
                "group": sz.group,
                "four_class": sz.four_class,
                "n_channels_involved": len(sz.channels),
                "onset_channels": ",".join(sz.onset_channels),
                "has_channel_labels": bool(sz.channels),
                "preictal_available_s": max(0.0, sz.onset - prev_end),
                "postictal_available_s": max(0.0, next_start - sz.offset),
                "is_lead_seizure": k == 0,
                "has_ecg": row["has_ecg"],
            }
        )
        prev_end = sz.offset
    return row, rows


def audit_dataset(
    root: str | Path,
    edf_subdir: str = "edf",
    limit: int | None = None,
    progress: Callable[[Iterable], Iterable] | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame, list[str]]:
    """Audit the whole dataset.

    Returns:
        ``(recordings, seizures, errors)`` — errors are ``"path: message"`` strings
        for files that could not be read; they do not stop the audit.
    """
    paths = list(iter_recordings(root, edf_subdir))
    if limit is not None:
        paths = paths[:limit]
    iterable = progress(paths) if progress else paths
    rec_rows: list[dict] = []
    sz_rows: list[dict] = []
    errors: list[str] = []
    for rp in iterable:
        try:
            row, rows = audit_recording(rp)
        except (EDFError, AnnotationError, OSError, KeyError) as err:
            errors.append(f"{rp.path}: {err}")
            continue
        rec_rows.append(row)
        sz_rows.extend(rows)
    return pd.DataFrame(rec_rows), pd.DataFrame(sz_rows), errors


def preictal_table(seizures: pd.DataFrame, minutes: Sequence[int]) -> pd.DataFrame:
    """How many seizures have at least N minutes of EEG before onset, per split."""
    rows = []
    for m in minutes:
        ok = seizures[seizures["preictal_available_s"] >= 60 * m] if len(seizures) else seizures
        row = {"min_preictal_min": m, "all": len(ok)}
        for split in ("train", "dev", "eval"):
            row[split] = int((ok["split"] == split).sum()) if len(ok) else 0
        row["patients"] = ok["patient"].nunique() if len(ok) else 0
        rows.append(row)
    return pd.DataFrame(rows)


def recommend_hazard_bins(
    table: pd.DataFrame, min_train_seizures: int = 100, min_eval_seizures: int = 20
) -> list[int]:
    """Largest set of horizons (minutes) with enough seizures in train and eval."""
    ok = table[(table["train"] >= min_train_seizures) & (table["eval"] >= min_eval_seizures)]
    return [int(m) for m in ok["min_preictal_min"]]


def summarize(
    recordings: pd.DataFrame, seizures: pd.DataFrame, preictal_minutes: Sequence[int]
) -> dict:
    """Headline numbers and tables for DATA_AUDIT.md."""
    summary: dict = {"n_recordings": len(recordings)}
    if recordings.empty:
        return summary
    by_split = recordings.groupby("split").agg(
        recordings=("file", "size"),
        patients=("patient", "nunique"),
        sessions=("session", "size"),
        hours=("duration_s", lambda s: round(s.sum() / 3600, 2)),
        with_ecg=("has_ecg", "sum"),
        with_channel_labels=("has_channel_annotations", "sum"),
        seizures=("n_seizures", "sum"),
    )
    summary |= {
        "n_patients": recordings["patient"].nunique(),
        "hours": round(recordings["duration_s"].sum() / 3600, 2),
        "seizure_hours": round(recordings["seizure_seconds"].sum() / 3600, 2),
        "ecg_fraction": round(float(recordings["has_ecg"].mean()), 3),
        "channel_label_fraction": round(float(recordings["has_channel_annotations"].mean()), 3),
        "by_split": by_split.reset_index(),
        "montages": recordings["montage"]
        .value_counts()
        .rename_axis("montage")
        .reset_index(name="recordings"),
        "sampling_rates": recordings["fs"]
        .value_counts()
        .rename_axis("fs_hz")
        .reset_index(name="recordings"),
        "patients_in_multiple_splits": sorted(
            p for p, g in recordings.groupby("patient") if g["split"].nunique() > 1
        ),
    }
    if not seizures.empty:
        summary["types"] = (
            seizures.groupby(["type", "split"]).size().unstack(fill_value=0).reset_index()
        )
        summary["seizure_duration_s"] = seizures["duration_s"].describe().round(1).to_dict()
        summary["preictal"] = preictal_table(seizures, preictal_minutes)
        summary["recommended_bins_min"] = recommend_hazard_bins(summary["preictal"])
    return summary


def _md_table(df: pd.DataFrame) -> str:
    cols = [str(c) for c in df.columns]
    lines = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    lines += ["| " + " | ".join(str(v) for v in row) + " |" for row in df.itertuples(index=False)]
    return "\n".join(lines)


def render_markdown(summary: dict, errors: Sequence[str], source: str) -> str:
    """DATA_AUDIT.md content."""
    out = [
        "# TUSZ Data Audit",
        "",
        f"Generated by `scripts/00_audit_tusz.py` from `{source}`. Do not edit by hand; re-run the audit.",
        "",
        "## Headline",
        "",
        f"- Recordings: **{summary.get('n_recordings', 0)}**",
        f"- Patients: **{summary.get('n_patients', 0)}**",
        f"- EEG hours: **{summary.get('hours', 0)}** (seizure hours: {summary.get('seizure_hours', 0)})",
        f"- Recordings with ECG: **{summary.get('ecg_fraction', 0):.0%}**",
        f"- Recordings with per-channel labels: **{summary.get('channel_label_fraction', 0):.0%}**",
        f"- Unreadable files: **{len(errors)}**",
    ]
    multi = summary.get("patients_in_multiple_splits", [])
    out.append(
        f"- Patients in more than one official split: **{len(multi)}** {multi[:10] if multi else ''}"
    )
    for title, key in [
        ("By split", "by_split"),
        ("Seizure types (seizures per split)", "types"),
        ("EEG available before each seizure (sets the forecasting horizons)", "preictal"),
        ("Montage folders", "montages"),
        ("Sampling rates", "sampling_rates"),
    ]:
        if key in summary:
            out += ["", f"## {title}", "", _md_table(summary[key])]
    if "recommended_bins_min" in summary:
        out += [
            "",
            "## Recommended hazard bins",
            "",
            "Horizons with at least 100 train and 20 eval seizures having that much preceding EEG: "
            f"**{summary['recommended_bins_min'] or 'none — use shorter horizons or add CHB-MIT/Siena'}** minutes.",
        ]
    if "seizure_duration_s" in summary:
        d = summary["seizure_duration_s"]
        out += ["", "## Seizure duration (s)", "", ", ".join(f"{k}: {v}" for k, v in d.items())]
    if errors:
        out += ["", "## Unreadable files (first 20)", ""] + [f"- `{e}`" for e in errors[:20]]
    return "\n".join(out) + "\n"
