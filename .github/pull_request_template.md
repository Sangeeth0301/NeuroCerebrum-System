## Summary

<!-- What does this PR add or change? -->

## Phase

- Phase: P?
- Files from DOCS/ROADMAP.md covered by this PR:

## Checklist

- [ ] `make lint` and `make test` pass locally
- [ ] New modules have tests using synthetic fixtures (no real data in tests)
- [ ] Settings live in `configs/`, not hard-coded
- [ ] Real-time code is causal (`assert_causal` test where relevant)
- [ ] No patient overlap between splits; eval set not used for tuning
- [ ] No data, checkpoints or `.env` committed
- [ ] `DOCS/EXPERIMENTS.md` / `DOCS/DECISIONS.md` updated if results or design changed

## Results (if any)

<!-- Metrics table, figures, run IDs. -->
