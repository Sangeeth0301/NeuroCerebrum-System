# data/

Local datasets and pipeline products. **Everything here except this README and the empty-folder markers is git-ignored.** TUSZ and TUAR are under a data use agreement and must never be committed or shared.

| Folder | Filled by | Content |
|---|---|---|
| `raw/tusz/` | you (download) | TUSZ EDF files and annotation CSVs, unchanged |
| `raw/tuar/` | you (download) | TUAR artifact corpus |
| `raw/chbmit/` | you (download) | CHB-MIT (external test) |
| `raw/siena/` | you (download) | Siena Scalp EEG (external test) |
| `interim/` | `scripts/02_preprocess.py` | montaged, filtered, resampled recordings |
| `processed/windows/` | `scripts/03_build_labels.py` | window indexes and labels (soft onset, hazard, channel masks) |
| `processed/features/` | `scripts/04_extract_features.py` | neuro-dynamics and ECG features |
| `processed/twin_posteriors/` | `scripts/08_run_sbi_posteriors.py` | SBI posteriors over A, B, G |
| `processed/metadata.parquet` | `scripts/00_audit_tusz.py` | one row per recording |
| `simulations/` | `scripts/06_simulate_wendling.py` | Wendling simulation bank |
| `cache/` | any step | temporary arrays, safe to delete |

Download instructions arrive with phase P1 in `DATA.md` at the repository root. Paths can be changed in `.env` (see `.env.example`).
