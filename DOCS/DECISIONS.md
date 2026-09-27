# Design Decisions

A short record of each important decision: what was decided, why, and what was rejected. Newest at the bottom. Format: `D-NNN · date · status`.

---

## D-001 · 2026-09-27 · accepted
**TUSZ as the primary dataset; CHB-MIT and Siena as external tests.**
- *Why:* TUSZ is the largest public seizure corpus with patient-disjoint official splits, seizure-type labels and **per-channel** annotations (needed for spread). Its recordings are short, so long-horizon forecasting is also tested on CHB-MIT/Siena.
- *Rejected:* CHB-MIT as primary (23 children, no type labels).

## D-002 · 2026-09-27 · accepted
**Primary objective is earliness under fair evaluation.**
- *Why:* the literature review found no fair onset-latency or alarm-level forecasting results on TUSZ; headline accuracies elsewhere are inflated by leakage.
- *Consequence:* patient-disjoint splits, event-level metrics, false-alarm budget, chance test, eval used once.

## D-003 · 2026-09-27 · accepted
**Final architecture v2: Graph Neural-Mass Dynamics** (see `ARCHITECTURE.md`).
- *Why:* combines the three strongest literature families (soft-label onset + accumulation; electrode graphs; neuroscience markers) with novel parts (GNM-ODE, stability margin, competing-risks hazard, spread roll-out, cascaded EEG+ECG alarm).
- *Rejected:* large foundation model backbone (little gain for seizures, TUH overlap, compute); plain dynamic-graph GNN (not novel).

## D-004 · 2026-09-27 · accepted
**Keep the v1.1 backbone as a fallback.**
- *Why:* the neural-mass ODE is the riskiest part. A working fallback (CNN → graph attention → causal SSM/GRU) guarantees a full result by P5.

## D-005 · 2026-09-27 · accepted
**MIT license for code.**
- *Why:* simple and permissive for a research project. Datasets keep their own terms and are never redistributed.

## D-006 · 2026-09-27 · accepted
**Hydra + OmegaConf for configuration; light core package with optional extras.**
- *Why:* every experiment is reproducible from a config; CI and laptops install only the core (`numpy`, `scipy`, `pandas`, config libs), heavy stacks (`torch`, `mne`, `sbi`) come as extras.

## D-007 · 2026-09-27 · accepted
**GRU as the default temporal block on Windows; Mamba only on Linux/WSL2.**
- *Why:* `mamba-ssm` needs Linux + CUDA. The choice does not change the architecture.

## D-008 · 2026-09-27 · accepted
**Branch per phase, small conventional commits, review before merge.**
- *Why:* the owner reviews each phase before it enters `main`.

## D-009 · 2026-09-27 · accepted
**Reference PDFs already tracked in `ref/` stay tracked for now.**
- *Why:* they were committed before P0. If the repository becomes public, consider removing them (publisher copyright) and keeping only `ref/MISSING_PAPERS.md`-style link lists.
