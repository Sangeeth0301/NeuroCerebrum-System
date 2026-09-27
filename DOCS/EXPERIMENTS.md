# Experiment Log

Every run that produces a number goes here, including failed and negative ones.

**Rules**
- Tune only on TUSZ train / dev-A / dev-B. The eval set is run **once** per final model and marked `EVAL`.
- Give the run ID from MLflow (or the JSON file in `outputs/logs/`) so results can be traced to a config and commit.
- Report patient-level bootstrap 95% CIs for headline numbers.

## Template

```
### EXP-NNN · YYYY-MM-DD · <short title>
- Phase / branch / commit:
- Config: configs/experiment/<name>.yaml  (+ overrides)
- Data split: train → dev-A | dev-B | EVAL
- Hypothesis:
- Result:
  | metric | value | 95% CI | baseline |
  |---|---|---|---|
- Conclusion / next step:
- Run ID:
```

---

## Runs

_No experiments yet. P0 (setup) contains no training runs; the first entries arrive with the P1 data audit and P3 baselines._
