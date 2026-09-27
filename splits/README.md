# splits/

Patient lists used by **every** experiment. One patient ID per line; lines starting with `#` are comments. These files are committed so results are reproducible and leakage can be audited.

| File | Source | Used for |
|---|---|---|
| `tusz_train.txt` | official TUSZ `train` | training |
| `tusz_dev_a.txt` | half of official `dev` (by patient) | model selection, early stopping |
| `tusz_dev_b.txt` | other half of official `dev` | alarm thresholds, conformal false-alarm calibration |
| `tusz_eval.txt` | official TUSZ `eval` | **final test only — run once per final model** |
| `chbmit_external.txt` | CHB-MIT (phase P9) | external long-horizon test |
| `siena_external.txt` | Siena (phase P9) | external adult test |

## How they are made

```bash
python scripts/00_audit_tusz.py     # needs TUSZ
python scripts/01_make_splits.py
```

Rules (`src/neuromech/data/splits.py`, settings in `configs/data/tusz.yaml`):

1. Start from the official TUSZ folders so results stay comparable with published work.
2. Split `dev` by patient into `dev_a` / `dev_b` (default 50/50, seed 42), stratified so both halves contain patients with seizures.
3. A patient found in more than one official split is removed from train/dev (`overlap_policy: drop_from_train_dev`), leaving eval untouched.
4. Every read and write re-checks that no patient is in two files (`assert_no_patient_overlap`).

**Status:** not generated yet — waiting for the TUSZ dataset. Never edit these files by hand; re-run the script and commit the result.
