---
name: Experiment request
about: Propose an experiment, ablation or baseline
title: "exp: "
labels: experiment
---

## Hypothesis

<!-- What do you expect to happen, and why? Link the relevant paper or DECISIONS.md entry. -->

## Setup

- Phase:
- Config / experiment file:
- Data split(s): train / dev-A / dev-B (never eval for tuning)
- Baseline to compare against:

## Metrics

<!-- Tick what will be reported. -->
- [ ] Onset latency (median, % within 5 s / 10 s)
- [ ] SzCORE event F1, sensitivity, false alarms / 24 h
- [ ] Forecast: event sensitivity, FA/h, time in warning, warning time, chance test
- [ ] Competing-risks C-index / time-dependent AUC
- [ ] Seizure type wF1 (4-class / 7-class)
- [ ] Spread metrics (onset F1, Kendall τ, recruit error, next-channel F1)
- [ ] Per-type breakdown
- [ ] Patient-level bootstrap confidence intervals

## Success criterion

<!-- What result would confirm or reject the hypothesis? -->

## Compute estimate

<!-- GPU hours, storage. -->
