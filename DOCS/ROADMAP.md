# NeuroMech-Warn — Roadmap (P0–P12)

Every file of the project belongs to exactly one phase. A phase is finished only when its **Done when** check passes and the work is reviewed and merged.

**Rules for every phase**
- Work on a branch `phase-N/<topic>`, one small commit per logical piece, then a pull request into `main`.
- Each new package folder gets an `__init__.py`; each listed test file must pass.
- Log experiments in `DOCS/EXPERIMENTS.md` and design changes in `DOCS/DECISIONS.md`.

| Phase | Name | Est. time | Depends on | Status |
|---|---|---|---|---|
| P0 | Project setup and scaffolding | ~1 wk | – | ✅ done (PR #1, fixes PR #2) |
| P1 | Data foundation and TUSZ audit | ~2 wk | P0, TUSZ | 🟡 code done · real audit + splits wait for TUSZ |
| P2 | Preprocessing, windows and labels | ~2 wk | P1 | planned |
| P3 | Evaluation framework and baselines | ~2–3 wk | P2 | planned |
| P4 | Artifact gate, neuro-dynamics bank, ECG | ~2–3 wk | P2, TUAR | planned |
| P5 | Fallback model, onset detection, first result | ~3–4 wk | P3, P4 | planned |
| P6 | Forecasting and cascaded alarm | ~3 wk | P5 | planned |
| P7 | Neural-mass digital twin (SBI) | ~3 wk | P4 (parallel to P5–P6) | planned |
| P8 | Graph Neural-Mass ODE, stability, spread | ~4 wk | P6, P7 | planned |
| P9 | Type, body, external validation, ablations | ~3 wk | P8 | planned |
| P10 | Explainability, reports, dashboard | ~2–3 wk | P9 | planned |
| P11 | Deployment and tiny model | ~2 wk | P9 | planned |
| P12 | Documentation, paper, release | ~2–3 wk | all | planned |

```
Week:  1   3   5   7   9  11  13  15  17  19  21  23  25  27  29  31
P0     █
P1      ██
P2        ██
P3          ███
P4            ███
P5               ████                 ← first full result (guaranteed)
P6                   ███
P7               ███                  ← parallel with P5–P6
P8                      ████          ← core novelty
P9                          ███
P10                            ███
P11                            ██
P12                               ███
```

---

## P0 · Project setup and scaffolding
**Goal:** clean, installable, reproducible empty project.
```
Root          README.md · LICENSE · DISCLAIMER.md · CONTRIBUTING.md · CODE_OF_CONDUCT.md
              requirements.txt · requirements-dev.txt · environment.yml · pyproject.toml
              Makefile · .gitignore · .gitattributes · .env.example
              .pre-commit-config.yaml · .editorconfig
CI / editor   .github/workflows/ci.yml
              .github/ISSUE_TEMPLATE/bug_report.md · experiment_request.md
              .github/pull_request_template.md
              .vscode/settings.json · launch.json
DOCS          ROADMAP.md · GLOSSARY.md · DECISIONS.md · EXPERIMENTS.md · figures/
Configs       configs/config.yaml · configs/paths.yaml
Source        src/neuromech/__init__.py · version.py
              src/neuromech/utils/__init__.py · io.py · logging.py · seed.py · tracking.py · timing.py · checks.py
Data/outputs  data/README.md + folder skeleton · outputs/ folder skeleton
Tests         tests/conftest.py · tests/test_utils.py (added: P0 needs a passing test)
```
**Done when:** `pip install -e .` works, tests pass, pre-commit and CI green, data/outputs git-ignored.

## P1 · Data foundation and TUSZ audit
```
Root        DATA.md
DOCS        DATA_AUDIT.md
Configs     configs/data/tusz.yaml
Splits      splits/README.md · tusz_train.txt · tusz_dev_a.txt · tusz_dev_b.txt · tusz_eval.txt
Source      src/neuromech/data/__init__.py · edf_reader.py · annotations.py · montage.py
Scripts     scripts/00_audit_tusz.py · 01_make_splits.py
Notebooks   notebooks/01_explore_tusz.ipynb
Tests       tests/test_montage.py · test_splits_no_leakage.py
Generated   data/processed/metadata.parquet
```
**Done when:** DATA_AUDIT.md reports preictal lengths, per-channel label coverage, ECG availability, type counts and chosen hazard bins; splits frozen with no patient overlap.

**Added in P1 (not in the original list):**
```
Source      src/neuromech/data/audit.py      audit logic, testable outside the script
            src/neuromech/data/splits.py     split logic + leakage checks, testable outside the script
            src/neuromech/data/synthetic.py  fake TUSZ v2 tree for tests and dry runs
Tests       tests/test_edf_reader.py · test_annotations.py · test_audit.py
```
**Status:** all code and 48 new tests done; dry run works (`data.dry_run=true`).
**Pending real data:** run `make audit` and `make splits`, commit `DOCS/DATA_AUDIT.md` and `splits/*.txt`, set hazard bins in P2.

## P2 · Preprocessing, windows and labels
```
Configs     configs/preprocess/filters.yaml · windows.yaml · labels.yaml
Source      src/neuromech/preprocessing/__init__.py · filters.py · resample.py · windowing.py
            src/neuromech/data/label_builder.py · channel_labels.py · datasets.py · samplers.py · streaming.py
Scripts     scripts/02_preprocess.py · 03_build_labels.py
Notebooks   notebooks/02_label_sanity_checks.ipynb
Tests       tests/test_causal_filters.py · test_windowing.py · test_labels.py · test_streaming.py
```
**Done when:** causality proven by test; soft onset, hazard with censoring and channel masks verified.

## P3 · Evaluation framework and baselines
```
DOCS        EVALUATION_PROTOCOL.md · METRICS.md
Configs     configs/eval/eval.yaml · configs/experiment/baseline_catboost.yaml · baseline_mlspred.yaml
Source      src/neuromech/eval/__init__.py · szcore.py · latency.py · forecasting.py · survival_metrics.py
            chance.py · spread_metrics.py · type_metrics.py · bootstrap.py · per_type.py · report_tables.py
            src/neuromech/baselines/__init__.py · catboost_zabihi.py · mlspred_resnet.py
            stft_cnn_truong.py · dcrnn_tang.py · soft_label_xu.py
Scripts     scripts/14_run_baselines.py
Tests       tests/test_metrics.py
```
**Done when:** metrics pass toy tests; baseline numbers logged — the numbers to beat.

## P4 · Artifact gate, neuro-dynamics bank and ECG
```
Configs     configs/data/tuar.yaml · configs/features/neuro_bank.yaml · ecg.yaml
Source      src/neuromech/preprocessing/artifact_gate.py · normalization.py
            src/neuromech/features/__init__.py · aperiodic.py · spectral.py · critical_slowing.py
            spikes.py · morphology.py · connectivity.py · ecg.py · feature_bank.py
Scripts     scripts/04_extract_features.py · 05_train_artifact_gate.py
Notebooks   notebooks/03_neuro_features_preictal.ipynb
Tests       tests/test_features.py · test_ecg.py
```
**Done when:** artifact gate validated on TUAR; preictal behaviour of neuro features documented.

## P5 · Fallback model, onset detection, first full result
```
Configs     configs/model/fallback.yaml · fusion.yaml · heads.yaml
            configs/train/pretrain.yaml · finetune.yaml · optim.yaml · configs/experiment/v11_fallback.yaml
Source      src/neuromech/models/__init__.py · registry.py
            models/backbones/__init__.py · fallback_ssm.py · temporal_cnn.py · graph_layers.py
            models/fusion/__init__.py · cross_attention.py · gating.py · domain_adversarial.py
            models/heads/__init__.py · onset.py
            models/pretraining/__init__.py · time_contrastive.py · masked_channel.py · next_seconds.py
            src/neuromech/losses/__init__.py · soft_bce.py · focal.py · smoothness.py · uncertainty_weighting.py
            src/neuromech/training/__init__.py · trainer.py · stages.py · callbacks.py
            src/neuromech/alarm/__init__.py · accumulation.py · k_of_n.py · thresholds.py
Scripts     scripts/09_pretrain.py · 10_finetune.py
Notebooks   notebooks/06_model_debug.ipynb
Tests       tests/test_heads.py · test_losses.py
```
**Done when:** causal latency, SzCORE F1 and FA/24h on dev beat or match P3 baselines.

## P6 · Forecasting and cascaded alarm
```
Configs     configs/alarm/cascade.yaml · calibration.yaml
Source      src/neuromech/models/heads/competing_risks.py · src/neuromech/losses/survival.py
            src/neuromech/alarm/cusum.py · cascade.py · conformal.py · src/neuromech/training/adaptation.py
Scripts     scripts/11_calibrate_alarm.py · 12_evaluate.py
Tests       tests/test_alarm_cascade.py · test_conformal.py
```
**Done when:** forecasting beats MLSPred-Bench with event metrics and chance test; cascade cuts latency within FA budget.

## P7 · Neural-mass digital twin (SBI)
```
Configs     configs/twin/wendling.yaml · sbi.yaml
Source      src/neuromech/twin/__init__.py · wendling.py · jansen_rit.py · simulate_bank.py
            summary_stats.py · sbi_posterior.py · validation.py · virtual_neurons.py
Scripts     scripts/06_simulate_wendling.py · 07_train_sbi.py · 08_run_sbi_posteriors.py
Notebooks   notebooks/04_wendling_playground.ipynb · 05_sbi_validation.ipynb
Tests       tests/test_wendling.py
```
**Done when:** simulation-based calibration passes; posteriors for all windows.

## P8 · Graph Neural-Mass ODE, stability and spread
```
Configs     configs/model/gnm_ode.yaml · configs/experiment/v2_full.yaml
Source      src/neuromech/models/backbones/gnm_ode.py · ode_solvers.py · coupling.py · observation.py
            src/neuromech/models/heads/stability.py · spread.py · src/neuromech/losses/reconstruction.py
Tests       tests/test_gnm_ode.py
```
**Done when:** GNM-ODE trains stably, reconstructs EEG and is compared with the fallback.

## P9 · Type, body, external validation and ablations
```
DOCS        ABLATIONS.md
Configs     configs/data/chbmit.yaml · siena.yaml · configs/experiment/ablation_*.yaml (10)
Splits      splits/chbmit_external.txt · siena_external.txt
Source      src/neuromech/models/heads/seizure_type.py · body.py · src/neuromech/report/semiology_table.py
            src/neuromech/data/external/__init__.py · chbmit.py · siena.py
Scripts     scripts/13_evaluate_external.py · 15_run_ablations.py
Notebooks   notebooks/07_results_analysis.ipynb
```
**Done when:** final TUSZ eval (once), external results and all ablations recorded.

## P10 · Explainability, reports and dashboard
```
Source      src/neuromech/explain/__init__.py · attributions.py · attention_maps.py · reasons.py
            src/neuromech/report/__init__.py · seizure_report.py · templates/seizure_report.md.j2
            src/neuromech/viz/__init__.py · topomap.py · brain3d.py · network.py · timeline.py · eeg_trace.py · virtual_neurons.py
App         app/dashboard.py · app/pages/1_Live_Monitor.py · 2_Brain_View.py · 3_Virtual_Neurons.py · 4_Seizure_Report.py
            app/components/ · app/assets/
```
**Done when:** dashboard replays a recording live with all views and an auto report.

## P11 · Deployment and tiny model
```
Root        Dockerfile · docker-compose.yml · .dockerignore
Configs     configs/train/distill.yaml
Source      src/neuromech/models/student/__init__.py · tiny_4ch.py · src/neuromech/training/distillation.py
            src/neuromech/deploy/__init__.py · export_onnx.py · quantize.py · benchmark.py
Scripts     scripts/16_distill_student.py · 17_export_deploy.py
```
**Done when:** student < 100k params, int8, benchmarked against the full model.

## P12 · Documentation, paper and release
```
Root        MODEL_CARD.md · CITATION.cff · CHANGELOG.md · README.md (final)
CI          .github/workflows/docs.yml
DOCS        paper/main.tex · paper/references.bib · paper/figures/
            final updates: ARCHITECTURE.md · EXPERIMENTS.md · DECISIONS.md · ROADMAP.md
Scripts     scripts/18_make_paper_figures.py
```
**Done when:** a new person can reproduce the tables from `DATA.md` + `Makefile`; paper draft complete.
