# NeuroMech-Warn

**Earlier Than Ever: forecasting, classifying and understanding epileptic seizures before they strike.**

NeuroMech-Warn is a research project on the Temple University Hospital EEG Seizure Corpus (TUSZ). Its goal is to warn **earlier** than previous methods, under fair patient-independent evaluation, and to explain each warning: what type of seizure is coming, where it starts, how it spreads and how the body reacts.

> ⚠️ Research prototype. Not a medical device. See [DISCLAIMER.md](DISCLAIMER.md).

## Status

| Phase | Scope | Status |
|---|---|---|
| P0 | Project setup and scaffolding | ✅ done |
| P1 | Data foundation and TUSZ audit | ⏳ waiting for dataset |
| P2–P12 | Pipeline, models, evaluation, dashboard, deployment, paper | planned |

The full plan is in [DOCS/ROADMAP.md](DOCS/ROADMAP.md).

## Documentation

| Document | Content |
|---|---|
| [DOCS/README.md](DOCS/README.md) | Objectives and visual idea |
| [DOCS/NeuroMech-Warn_Problem_Statement.md](DOCS/NeuroMech-Warn_Problem_Statement.md) | Problem statement |
| [DOCS/ARCHITECTURE.md](DOCS/ARCHITECTURE.md) | Final architecture (v2, Graph Neural-Mass Dynamics) |
| [DOCS/ROADMAP.md](DOCS/ROADMAP.md) | Phases P0–P12 and every file in each phase |
| [research/reports/](research/reports/) | Literature review of 47 papers |
| [DOCS/DECISIONS.md](DOCS/DECISIONS.md) | Design decisions and reasons |

## Install

Python 3.10+ (3.11 recommended).

```bash
# conda (recommended, includes CUDA PyTorch)
conda env create -f environment.yml
conda activate neuromech
```

```bash
# or pip
python -m venv .venv
.venv\Scripts\activate          # Windows  (Linux/macOS: source .venv/bin/activate)
pip install -r requirements.txt -r requirements-dev.txt
pip install -e .
```

Light install for development and tests only:

```bash
pip install -e ".[dev]"
```

Then copy `.env.example` to `.env` and set the dataset paths.

## Common commands

```bash
make test       # run the test suite
make lint       # ruff lint + format check
make format     # auto-format
```

Windows without `make`: run the same commands shown in the [Makefile](Makefile) directly, e.g. `python -m pytest`.

## Data

TUSZ and TUAR are available from the Temple University Neural Engineering Data Consortium after signing their data use agreement. The data is **never** committed to this repository. Download instructions arrive with phase P1 in `DATA.md`.

## Repository layout

```
configs/    Hydra configuration (data, model, training, alarm, evaluation)
src/neuromech/   Python package
scripts/    numbered pipeline scripts (00_audit … 18_figures)
tests/      unit tests (synthetic EEG, no real data needed)
data/       local datasets (git-ignored)
outputs/    checkpoints, logs, results (git-ignored)
DOCS/       problem statement, architecture, roadmap, decisions
research/   literature review
ref/        reference paper list with download links (PDFs kept locally, not in git)
```

## License

Code: [MIT](LICENSE). The license does not cover TUSZ, TUAR, CHB-MIT or Siena data, which keep their own terms.
