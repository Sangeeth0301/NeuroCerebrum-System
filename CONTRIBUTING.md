# Contributing

## Workflow

1. Work on a branch named after the phase or task, e.g. `phase-2/labels` or `fix/montage-le`.
2. Keep commits small and focused. Use [Conventional Commits](https://www.conventionalcommits.org/):
   `feat:`, `fix:`, `docs:`, `test:`, `build:`, `ci:`, `chore:`, `refactor:`, `perf:`, `exp:` (experiment configs/results).
3. Open a pull request into `main`. CI must be green and a reviewer must approve.
4. Record every experiment in [DOCS/EXPERIMENTS.md](DOCS/EXPERIMENTS.md) and every design change in [DOCS/DECISIONS.md](DOCS/DECISIONS.md).

## Setup

```bash
pip install -e ".[dev]"
pre-commit install
```

## Code style

- Python ≥ 3.10, formatted and linted with **ruff** (`make format`, `make lint`).
- Type hints on public functions; short docstrings stating inputs, outputs and units (µV, Hz, seconds).
- No hard-coded paths or parameters: put them in `configs/`.
- Keep signal processing **causal** unless a function is explicitly marked offline.

## Adding a module

1. Put code in the matching package under `src/neuromech/` (see [DOCS/ROADMAP.md](DOCS/ROADMAP.md)).
2. Add settings to the matching config group in `configs/`.
3. Add tests in `tests/` using the synthetic EEG fixtures in `tests/conftest.py`. Tests must not need the real dataset; mark any that do with `@pytest.mark.data`.

## Rules that protect the results

- **Never** let a patient appear in more than one split. Use the lists in `splits/`.
- **Never** tune anything on the TUSZ eval set. Thresholds and calibration use dev only; eval is run once per final model.
- **Never** commit data, checkpoints or `.env`.
- Report negative results honestly.
