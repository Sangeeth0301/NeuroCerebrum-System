# NeuroMech-Warn command shortcuts.
# Windows: install make (e.g. `choco install make`) or run the commands directly.
# Targets marked (Pn) are filled in when that phase lands; until then they print a notice.

PY ?= python
CONFIG ?= config

.DEFAULT_GOAL := help
.PHONY: help setup setup-dev install lint format typecheck test test-all cov clean \
        audit splits preprocess labels features artifact-gate simulate sbi posteriors \
        pretrain finetune calibrate evaluate evaluate-external baselines ablations \
        distill export figures dashboard

help:  ## Show this help
	@$(PY) -c "import re;[print(f'  {m[0]:<18} {m[1]}') for m in re.findall(r'^([a-zA-Z_-]+):.*?## (.*)$$', open('Makefile').read(), re.M)]"

# ── environment ───────────────────────────────────────────────────────────────
setup:  ## Install full runtime stack + package
	$(PY) -m pip install -r requirements.txt
	$(PY) -m pip install -e .

setup-dev:  ## Install light core + dev tools + pre-commit hooks
	$(PY) -m pip install -e ".[dev]"
	pre-commit install

# ── quality ───────────────────────────────────────────────────────────────────
lint:  ## Ruff lint + format check
	$(PY) -m ruff check src tests scripts
	$(PY) -m ruff format --check src tests scripts

format:  ## Auto-format and fix lint issues
	$(PY) -m ruff format src tests scripts
	$(PY) -m ruff check --fix src tests scripts

typecheck:  ## Mypy on src/
	$(PY) -m mypy

test:  ## Unit tests (no real data needed)
	$(PY) -m pytest -m "not data and not slow"

test-all:  ## All tests including slow and real-data ones
	$(PY) -m pytest

cov:  ## Tests with coverage report
	$(PY) -m pytest -m "not data" --cov=neuromech --cov-report=term-missing

clean:  ## Remove caches (keeps data/ and outputs/)
	$(PY) -c "import shutil,pathlib;[shutil.rmtree(p,ignore_errors=True) for p in pathlib.Path('.').rglob('*') if p.name in {'__pycache__','.pytest_cache','.ruff_cache','.mypy_cache'}]"

# ── pipeline (scripts arrive in later phases) ─────────────────────────────────
define run_script
	@if [ -f scripts/$(1) ]; then $(PY) scripts/$(1) --config-name=$(CONFIG) $(ARGS); \
	else echo "scripts/$(1) not implemented yet (phase $(2))"; fi
endef

audit:             ## (P1) TUSZ data audit -> DOCS/DATA_AUDIT.md
	$(call run_script,00_audit_tusz.py,P1)
splits:            ## (P1) Build patient-disjoint split lists
	$(call run_script,01_make_splits.py,P1)
preprocess:        ## (P2) Montage, causal filters, resampling
	$(call run_script,02_preprocess.py,P2)
labels:            ## (P2) Soft onset, hazard and channel labels
	$(call run_script,03_build_labels.py,P2)
features:          ## (P4) Neuro-dynamics bank + ECG features
	$(call run_script,04_extract_features.py,P4)
artifact-gate:     ## (P4) Train the TUAR artifact gate
	$(call run_script,05_train_artifact_gate.py,P4)
simulate:          ## (P7) Wendling simulation bank
	$(call run_script,06_simulate_wendling.py,P7)
sbi:               ## (P7) Train the SBI posterior estimator
	$(call run_script,07_train_sbi.py,P7)
posteriors:        ## (P7) Posteriors for all windows
	$(call run_script,08_run_sbi_posteriors.py,P7)
pretrain:          ## (P5) Self-supervised pretraining
	$(call run_script,09_pretrain.py,P5)
finetune:          ## (P5) Staged multi-task fine-tuning
	$(call run_script,10_finetune.py,P5)
calibrate:         ## (P6) Thresholds + conformal false-alarm budget on dev-B
	$(call run_script,11_calibrate_alarm.py,P6)
evaluate:          ## (P6) Final TUSZ eval (run once per final model)
	$(call run_script,12_evaluate.py,P6)
evaluate-external: ## (P9) CHB-MIT and Siena
	$(call run_script,13_evaluate_external.py,P9)
baselines:         ## (P3) Reproduce baselines
	$(call run_script,14_run_baselines.py,P3)
ablations:         ## (P9) Ablation study
	$(call run_script,15_run_ablations.py,P9)
distill:           ## (P11) 4-channel student
	$(call run_script,16_distill_student.py,P11)
export:            ## (P11) ONNX export, quantisation, benchmark
	$(call run_script,17_export_deploy.py,P11)
figures:           ## (P12) Paper figures
	$(call run_script,18_make_paper_figures.py,P12)

dashboard:         ## (P10) Launch the Streamlit dashboard
	@if [ -f app/dashboard.py ]; then streamlit run app/dashboard.py; \
	else echo "app/dashboard.py not implemented yet (phase P10)"; fi
