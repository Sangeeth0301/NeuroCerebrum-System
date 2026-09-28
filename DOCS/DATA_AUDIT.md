# TUSZ Data Audit

> **Status: not run yet — waiting for the TUSZ dataset.**
> This file is overwritten by `scripts/00_audit_tusz.py` (`make audit`) once `TUSZ_ROOT` points to the data (see [DATA.md](../DATA.md)). Do not edit it by hand.

A dry run on synthetic data already works:

```bash
python scripts/00_audit_tusz.py data.dry_run=true
```

## What the audit will report

| Section | Why it matters |
|---|---|
| Recordings, patients, hours per split | Size of train / dev / eval |
| Recordings with ECG | Coverage of the body module (H5) and the cardio part of the alarm |
| Recordings with per-channel labels | Coverage of the spread head (H4) and onset-zone metrics |
| Patients in more than one official split | Leakage check before splits are frozen |
| Seizure types per split | Class balance for the type head; rare types |
| EEG available before each seizure | How many seizures support each forecasting horizon |
| **Recommended hazard bins** | Horizons with ≥ 100 train and ≥ 20 eval seizures; sets H1's bins |
| Montage folders and sampling rates | Montage conversion and resampling plan for P2 |
| Seizure duration | Short-seizure share (a known failure case) |
| Unreadable files | Data problems to fix before P2 |
