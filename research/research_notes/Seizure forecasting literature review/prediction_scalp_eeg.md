# Seizure PREDICTION (warning before onset) from scalp EEG with ML/DL: evaluation standards, cross-patient generalization and the TUSZ gap

Per-paper files are in `research/papers/`:
- `P_2018_Kuhlmann_Epilepsyecosystem_crowdsourcing.md`
- `P_2018_Truong_CNN_seizure_prediction.md`
- `P_2022_Dissanayake_GDL_subject_independent_prediction.md`
- `P_2024_Jemal_domain_adaptation_cross_subject_prediction.md`
- `P_2024_Koutsouvelis_preictal_period_optimization.md`
- `P_2025_Meng_3D-SERESNet_multi_patient_prediction.md`
- `P_2025_Mohammad_MLSPred-Bench_TUSZ_prediction_benchmark.md`
- `P_2026_Chen_CG-MambaNet_cross_patient_prediction_PREPRINT.md`

**Terminology used in these notes (the conventional one):**
- **SPH** (seizure prediction horizon) = the gap between the alarm and the start of the window in which the seizure is expected.
- **SOP** (seizure occurrence period) = the window in which the seizure must occur.
- A correct alarm means onset falls in [alarm + SPH, alarm + SPH + SOP].
- MLSPred-Bench uses these names **the other way round** (see Q2).

## Which papers matter, and what they did

### Takeaway
Eight papers cover the field.
- **Kuhlmann 2018 and Truong 2018** set the evaluation standard: time-separated held-out data, SOP/SPH event scoring and a chance test.
- **Dissanayake 2022, Koutsouvelis 2024 and Meng 2025** report high numbers under leakage-prone protocols.
- **Jemal 2024 and CG-MambaNet 2026** (a preprint) are the true unseen-patient (LOPO) studies.
- **MLSPred-Bench 2025** is the only TUSZ prediction benchmark. It reports only segment-level validation AUC of about 0.67–0.75.

### Cited Findings

**Comparison table (all P_ papers):**

| Paper | Venue (status) | Data | Setting / split | Preictal; SPH / SOP | Model | Key numbers | Warning time |
|---|---|---|---|---|---|---|---|
| Kuhlmann 2018 | *Brain* (peer-reviewed) | NeuroVista **iEEG**, 3 pts in contest | patient-specific; held-out long-term data | 1 h preictal as 10-min clips (details in paper) | crowd-sourced feature + tree/ensemble models | top AUC **0.81**; only 6.7% drop on held-out data; pseudo-prospective sens 1.9× the original trial (**abstract-only**) | time-in-warning matched to the trial |
| Truong 2018 | *Neural Networks* (peer-reviewed) | CHB-MIT 13 pts / 64 sz (+ Freiburg, Kaggle iEEG) | patient-specific, leave-one-seizure-out | 30-min SOP / 5-min SPH; interictal ≥ 4 h | 30-s STFT, shallow CNN, 8-of-10 alarm | CHB-MIT sens **81.2%**, FPR **0.16/h**; beats chance for 12/13 | within 5–35 min (no distribution) |
| Dissanayake 2022 | IEEE JBHI (peer-reviewed) | CHB-MIT 23, Siena 15 | "subject-independent", but **pooled 10-fold CV** (not LOPO) | 1 h preictal; no SPH/SOP | MFCC, LSTM DR-Net, Chebyshev GNN | acc **95.38%** (CHB-MIT), **96.05%** (Siena) | not reported |
| Jemal 2024 | Front. Neuroinform. (peer-reviewed) | CHB-MIT 22, Siena 12 | pooled multi-subject **vs true LOPO** vs LOPO + unsupervised DA | 1 h preictal; no SPH/SOP; 10-s windows | EEGNet-like 3-layer CNN; DANN / CDAN / CDAN+E | pooled acc 97.36%, but **LOPO AUC 0.69** (CHB-MIT) / **0.48** (Siena); with DA **0.75 / 0.61** | not reported |
| Koutsouvelis 2024 | J Neural Eng (peer-reviewed; arXiv details) | CHB-MIT 19 cases | patient-specific leave-one-seizure-out | preictal 15–60 min optimized per patient; no SPH | CNN-Transformer on 5-s raw EEG | sens 99.31%, AUC 0.9935, **segment FAR 33.6/h** | "SPC" **76.8 min** (output convergence, not an alarm) |
| Meng 2025 | *iScience* (peer-reviewed) | CHB-MIT 13 pts | patient-specific leave-one-seizure-out, and "patient-independent" = **pooled multi-patient leave-one-seizure-out** (test patient in training) | SOP 30 / SPH 5; interictal ≥ 4 h | 3D STFT stack, SE-ResNet, focal loss, 8-of-10 + 30-min refractory | PS: **90.77%**, 0.090/h, AUC 0.923; multi-patient: **84.41%**, **0.232/h**, AUC 0.866 | within 5–35 min |
| MLSPred-Bench (Mohammad & Saeed) 2025 | *MethodsX* (peer-reviewed); bioRxiv 2024 | **TUSZ**, 287 pts with seizures, official patient-disjoint split | patient-independent, single fold; **validation-set** segment metrics | 12 benchmarks: preictal 2/5/15/30 min × gap 1/2/5 min (their "SPH" / "SOP") | classical ML, RF, CNN, CNN-LSTM, ResNet (SPERTL) on raw 5-s or 1,420 features | mean val AUC: ResNet raw **0.709**, RF features **0.748**; best single benchmarks 0.84 (ResNet, 15/2) and 0.88 (RF, 30/2) | not reported (lead of 3–35 min by design) |
| CG-MambaNet (Chen) 2026 | **arXiv preprint** | CHB-MIT 22, Siena 6 | **LOPO × 5 seeds** | 30-min preictal; interictal ≥ 4 h; no SPH found | depthwise CNN, learnable-adjacency GCN, bi-Mamba, BiLSTM | AUC **0.815** / **0.710**; event FPR **0.32/h** / 0.55/h; segment sens 74.3% | mean lead **23.4 min** / 21.7 min |

Sources for each row:
- Kuhlmann: [Europe PMC abstract](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1093/brain/awy210&resultType=core&format=json)
- Truong: [arXiv PDF](https://arxiv.org/pdf/1707.01976)
- Dissanayake: [QUT PDF](https://eprints.qut.edu.au/212250/1/88918403.pdf)
- Jemal: [Europe PMC full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10869477/fullTextXML)
- Koutsouvelis: [arXiv HTML](https://arxiv.org/html/2407.14876)
- Meng: [Europe PMC full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12723167/fullTextXML)
- MLSPred-Bench: [Europe PMC full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12423417/fullTextXML)
- CG-MambaNet: [arXiv abs](https://arxiv.org/abs/2606.08226); [arXiv HTML](https://arxiv.org/html/2606.08226v1)

**Systematic-review context:**
- A 2024 systematic review found only **21 of the prediction articles (about 4%) used cross-patient validation**.
  - Without adaptation, cross-patient sensitivity was 49–100%.
  - With target-patient adaptation (at least one target seizure), sensitivity was 54–95% at **0.03–0.38 FPR/h**.
  - The authors conclude that no method finds features truly shared across subjects.
  - Source: Shafiezadeh, Duma, Pozza, Testolin, J Neural Eng 21(6), 2024, DOI 10.1088/1741-2552/ad9682. This was read from the publisher page summary only, so treat it as **abstract-level**. — [IOP](https://iopscience.iop.org/article/10.1088/1741-2552/ad9682)

### Inferences
- The headline numbers in this field shrink as protocols get stricter:
  - pooled or segment-level: 95–99%;
  - patient-specific event-level: about 81–91% sensitivity at 0.09–0.16/h;
  - multi-patient event-level: 84% at 0.23/h;
  - true LOPO: AUC about 0.69–0.82;
  - TUSZ patient-disjoint: validation AUC about 0.71–0.75.
- **For a TUSZ project, only the last two rows are comparable.**

### Gaps
- No peer-reviewed, **true LOPO scalp-EEG study with event-level sensitivity, FPR/h and warning time** was found. CG-MambaNet reports FPR/h and lead time but is a preprint and does not clearly report event sensitivity. Jemal reports only segment metrics.
- **Not verified in this pass:**
  - The Liang, Peng and Zhao domain-adaptation papers, known only via Meng 2025's Table 9.
  - The CLSP-REQA preprint (arXiv 2606.00074).
  - Parani et al. (IEEE BigData 2024; CDMA 2025), follow-ups by the MLSPred group that reportedly use its benchmarks.
- The MLSPred-Bench bioRxiv per-benchmark seizure counts could not be verified, and they conflict with MethodsX.

## How preictal / SPH / SOP and evaluation protocols differ, and where leakage enters

### Takeaway
Definitions are not standardized (MLSPred even swaps the SPH and SOP names). The three biggest sources of inflation are:
1. pooled or segment-shuffled splits (Dissanayake; Meng's "patient-independent");
2. leave-one-seizure-out, which trains on future seizures (Truong; Koutsouvelis; Meng);
3. segment-level metrics presented as alarm performance (Koutsouvelis' 33.6/h FAR; CG-MambaNet's 112/h window FPR before filtering).

### Cited Findings
- **Pooled vs LOPO on the same data and network:**
  - CHB-MIT accuracy 97.36% pooled vs 63.5% LOPO (AUC 0.69).
  - Siena 96.01% pooled vs 48.69% LOPO (AUC 0.48).
  - Source: [Jemal 2024](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10869477/fullTextXML)
- **Dissanayake 2022** evaluates "subject-independent" prediction with 10-fold CV on pooled segments, with 50%-overlapping preictal windows. — [QUT PDF](https://eprints.qut.edu.au/212250/1/88918403.pdf)
- **Meng 2025's "patient-independent" setting** pools the remaining seizures of *all* patients, including the test patient, for training. — [Europe PMC full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12723167/fullTextXML)
- **Koutsouvelis 2024** acknowledges that leave-one-seizure-out trains on seizures occurring after the test seizure. It computes FAR per 5-s epoch (33.6/h). — [arXiv HTML](https://arxiv.org/html/2407.14876)
- **MLSPred-Bench naming and gaps:**
  - It defines "SPH" as the preictal window and "SOP" as the gap before onset, the reverse of Truong and Meng. Its preictal range is [T − SOP − SPH, T − SOP].
  - It gives no interictal distance rule.
  - It requires only an SPH + SOP gap from the previous seizure's end.
  - Source: [Europe PMC full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12423417/fullTextXML)
- **Conventional scoring (Truong, Meng):**
  - SPH 5 / SOP 30;
  - an 8-of-10 k-of-n alarm, plus a 30-min refractory period in Meng;
  - a chance test P = 1 − exp(−FPR·SOP) with a binomial test over seizures.
  - Sources: [Truong arXiv PDF](https://arxiv.org/pdf/1707.01976); [Meng](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12723167/fullTextXML)
- **CG-MambaNet's alarm pipeline:**
  - a causal 60-s moving average;
  - an alarm fires after at least 30 s above the Youden threshold (chosen on validation patients) and resets after at least 60 s below it;
  - this cuts window FPR from 112.4/h to an event FPR of 0.32/h on CHB-MIT;
  - the paper uses no SOP window or chance test.
  - Source: [arXiv HTML](https://arxiv.org/html/2606.08226v1)
- **Kuhlmann 2018** shows that top contest algorithms lost only 6.7% on a much larger held-out set when evaluation was time-separated (**abstract-only**). — [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1093/brain/awy210&resultType=core&format=json)

### Inferences
- Any number we compare against must be tagged with four things:
  1. split type (pooled, leave-one-seizure-out, LOPO, or official patient-disjoint);
  2. metric level (segment or event);
  3. SPH/SOP in the conventional naming;
  4. whether a chance test was run.
- Post-processing (k-of-n, persistence, refractory period) changes FPR/h by more than two orders of magnitude, so it must be fixed on validation data and reported.

### Gaps
- There is no agreed standard for "warning time":
  - Koutsouvelis uses output-convergence SPC;
  - CG-MambaNet uses mean onset-minus-alarm;
  - Truong and Meng report only the SPH/SOP window.
- The review did not find a paper that reports a lead-time distribution together with FPR/h.

## What "earlier warning" has actually been shown

### Takeaway
Claims of warning times above 60 min (Koutsouvelis' 76.8 min) are not alarm-based. Event-level systems warn within a 5–35 min window. The only cross-patient lead-time number is about 22–23 min (CG-MambaNet preprint, at 0.32–0.55 FPR/h). On TUSZ, performance is best with a 15-min preictal window and degrades at 30 min, except for one benchmark.

### Cited Findings
- **Koutsouvelis:** SPC 76.8 ± 36.8 min. It is the time smoothed segment outputs converge to their maximum; it is undefined for 6 of 19 cases and comes with a 33.6/h segment FAR. — [arXiv HTML](https://arxiv.org/html/2407.14876)
- **Koutsouvelis:** the optimal preictal period was 60 min for most patients, and longer preictal definitions gave earlier predictions. — [arXiv HTML](https://arxiv.org/html/2407.14876)
- **CG-MambaNet (preprint):** mean lead time 23.4 ± 4.8 min on CHB-MIT and 21.7 ± 5.3 min on Siena, with a 30-min preictal definition. — [arXiv HTML](https://arxiv.org/html/2606.08226v1)
- **MLSPred-Bench (TUSZ validation AUC):**
  - raw ResNet: 0.811 / 0.836 / 0.792 for a 15-min preictal window with a 1 / 2 / 5 min gap;
  - raw ResNet: 0.564 / 0.805 / 0.508 at 30 min;
  - RF on features: 0.883 at 30 min / 2 min, but 0.633–0.639 at 30 / 1 and 30 / 5.
  - Source: [Europe PMC full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12423417/fullTextXML)
- **MLSPred-Bench seizure count:** 1,282 seizures at the smallest horizon (2-min preictal + 1-min gap; 687 / 416 / 179 train / validation / test). Counts fall as the horizon grows. — [Europe PMC full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12423417/fullTextXML)

### Inferences
- The instability across adjacent MLSPred benchmarks (30 / 1 vs 30 / 2 vs 30 / 5) suggests high variance from small, changing seizure subsets and a single fold. A credible "earlier" claim on TUSZ needs:
  - confidence intervals (bootstrap over patients);
  - a fixed evaluation subset across horizons.

### Gaps
- No TUSZ study reports event-level sensitivity, FPR/h or lead time.
- It is unknown how many TUSZ eval seizures have at least 35 min (or at least 60 min) of clean pre-onset EEG in the same session. MLSPred reports these counts only in a figure.

## Implications for our TUSZ earlier-forecasting project

### Takeaway
The defensible contribution is to be first on TUSZ with **patient-disjoint, test-set (eval), event-level** prediction metrics across a grid of lead times. MLSPred-Bench is the baseline, and the Truong/Meng scoring plus CG-MambaNet-style causal alarms form the protocol.

### Cited Findings
- **MLSPred-Bench gives:** open code, the 20-channel TCP montage, the official split and baseline validation AUCs. It does **not** give test-set or event-level results. — [GitHub](https://github.com/pcdslab/MLSPred-Bench); [Europe PMC full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12423417/fullTextXML)
- **Feature-based tree ensembles are strong:**
  - RF on features had the best mean AUC on TUSZ ([MLSPred](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12423417/fullTextXML));
  - tree ensembles also featured among the winners of the Kaggle/Melbourne contest ([Kuhlmann / OUP](https://academic.oup.com/brain/article/141/9/2619/5066003)).
- **Graph + state-space temporal models** gave the best LOPO AUC on CHB-MIT and Siena, and the GCN step drove event FPR from 1.67/h to 0.32/h in ablation (**preprint**). — [arXiv HTML](https://arxiv.org/html/2606.08226v1)
- **Unsupervised DA** on unlabelled target-patient EEG raised LOPO AUC from 0.69 to 0.75 (CHB-MIT). — [Jemal 2024](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10869477/fullTextXML)

### Inferences
Recommended protocol:
1. Use the official TUSZ train/dev/eval split, patient-disjoint, and report on eval.
2. Use conventional SPH/SOP with a grid of total lead times, e.g. SPH ∈ {1, 5, 10} min × SOP ∈ {5, 15, 30} min. Report the number of eligible seizures per cell.
3. Use an interictal buffer (for example at least 30–60 min, since 4 h is infeasible for many TUSZ sessions; state this) and exclude postictal time.
4. Use causal alarms (k-of-n or firing power with a refractory period), tuned on dev.
5. Report event sensitivity, FPR/h, time-in-warning, the lead-time distribution, a Poisson/binomial chance test and segment AUC. The AUC is only for comparison with MLSPred.
6. Baselines: RF/XGBoost on MLSPred features; SPERTL-ResNet; a Truong STFT-CNN.
7. Proposed model: a graph over TCP channels plus a Mamba or transformer temporal encoder.

- **"Earlier than prior work" should be stated as:** at matched event FPR/h, a higher sensitivity at a longer SPH, or a longer median lead time, than MLSPred-Bench's best horizon (15-min preictal). It should **not** be stated against the 76.8-min SPC.

### Gaps
- We did not verify whether any 2025–2026 peer-reviewed paper (for example from the MLSPred group) already reports TUSZ prediction test-set results. The Parani et al. papers need checking before we claim "first".
- The TUSZ version used by MLSPred-Bench is not stated. Its 579 / 53 / 43 subject split suggests v2.x (our inference).
