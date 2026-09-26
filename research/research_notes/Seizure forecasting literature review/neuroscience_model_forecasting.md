# Neuroscience- and biophysical-model-based seizure forecasting (CSD, multidien cycles, E/I balance, neural mass models)

Per-paper files: `research/papers/N_*.md` (9 files).

## Comparison table

| Paper | Venue / year | Recording | Patients / duration | Biomarker / model | Pseudo-prospective? | Chance comparison? | Headline numbers | Source |
|---|---|---|---|---|---|---|---|---|
| Maturana et al. | Nat Commun 2020 | iEEG (NeuroVista, 16 ch) | 14 pts (1 excluded), 185-767 days, 2,871 seizures | CSD: variance and autocorrelation width + spike rate; cycle phase | Yes (M2, rolling 50-day, after 10th seizure) | Yes (chance product 9.6%, p<1e-9) | Sens 77 +/- 8% (M2), 91% time in low risk; 84 +/- 16% / 95% (M1) | [PMC7195436](https://pmc.ncbi.nlm.nih.gov/articles/PMC7195436/) |
| Chang et al. | Nat Neurosci 2018 | Slices, rat TeNT, human iEEG | 12 humans, 1,890 preictal periods | CSD / resilience; IED state-dependence; Epileptor | No | No (statistics only) | Slice variance and AC rise (F=154, F=1821); human: only 4/12 AC increase, 4/12 decrease | [PMC7617160](https://pmc.ncbi.nlm.nih.gov/articles/PMC7617160/) |
| Baud et al. | Nat Commun 2018 | RNS (chronic iEEG) | 37 pts, median 2.3 y (up to 9.9 y) | Circadian + multidien IEA cycles | No | Phase-locking tests | Multidien 20-30 d; phase-locked in 13/14; RR 6.8 (95% CI 3.1-15.1) | [PMC5758806](https://pmc.ncbi.nlm.nih.gov/articles/PMC5758806/) |
| Proix et al. | Lancet Neurol 2021 | RNS | 18 dev + 157 val; mean 1,484 d | PP-GLM on IEA cycle phases | Yes (chronological split) | Yes (200 surrogates, IoC) | 24 h AUC 0.74 (dev), 0.70 (val); IoC 83% / 66%; RR 3.7 / 9.4 | [PMC7968722](https://pmc.ncbi.nlm.nih.gov/articles/PMC7968722/) |
| Khambhati et al. | Nat Med 2024 | RNS hippocampal | 15 pts bitemporal | Functional connectivity from 90-s clips | Unclear (retrospective, cross-subject) | vs cycle-based benchmark | "as accurately as" cycle models (abstract); AUC 0.72 +/- 0.03 quoted in commentary, ambiguous | [Nature](https://www.nature.com/articles/s41591-024-03149-6); [Englot](https://pmc.ncbi.nlm.nih.gov/articles/PMC11556539/) |
| Duma, Cuozzo et al. | BMC Med 2025 | **Scalp hd-EEG 128 ch** | 20 pts, 29 seizures, ~13 min preictal | Aperiodic exponent (SPRiNT), E/I proxy | No | No | Exponent rises preictally (non-epileptic t=6.94, p<0.001), global; theta increases | [PMC12581463](https://pmc.ncbi.nlm.nih.gov/articles/PMC12581463/) |
| Karoly et al. | PLoS CB 2018 | iEEG (NeuroVista) | 12 pts, 3,010 seizures | Jansen-Rit, 5 params, assumed-density Kalman filter | No (ictal only) | No | Stereotyped pathways; onset does not predict duration; pre-offset params correlate with duration | [PLoS CB](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006403) |
| Aarabi & He (foundational) | Clin Neurophysiol 2014 | iEEG (short-term) | 21 pts | Neural mass model, 12 params fitted to PSD | Not evident | Not evident | Sens 87.07% / 92.6%, FPR 0.2 / 0.15 per h (abstract only) | [PubMed](https://pubmed.ncbi.nlm.nih.gov/24374087/) |
| Wendling 2002; Jirsa 2014 (foundational) | Eur J Neurosci; Brain | SEEG; in vitro | n/a | Wendling NMM (A, B, G); Epileptor | n/a | n/a | Impaired dendritic inhibition explains fast onset; onset/offset are bifurcations | [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=(TITLE:%22Epileptic%20fast%20activity%20can%20be%20explained%20by%20a%20model%20of%20impaired%20GABAergic%20dendritic%20inhibition%22)&resultType=core&format=json); [PMC4107736](https://pmc.ncbi.nlm.nih.gov/articles/PMC4107736/) |

## Do neuroscience warning signs (critical slowing, cycles) forecast seizures, and how well?

### Takeaway
Yes, with chronic intracranial data. The best-validated results come from long, cycle-based forecasting (daily AUC about 0.70-0.74, clearly above chance in two-thirds or more of patients). Most of the signal lives in slow circadian and multidien fluctuations, not in the minutes before onset.

### Cited Findings
- CSD markers (variance, autocorrelation) fluctuate over hours to days, and seizures occur on their rising phase. A pseudo-prospective forecaster reached 77 +/- 8% sensitivity with 91% time in low risk, significantly above chance. — [Maturana 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7195436/)
- Short-timescale CSD near onset appeared in 13/14 patients, and gradual rises tens of minutes to hours before seizures in 9/14. — [Maturana 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7195436/)
- In human iEEG over 30 min pre-seizure, lag-1 autocorrelation increased significantly in only 4/12 patients and decreased in 4. — [Chang 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC7617160/)
- IEDs have state-dependent effects: anti-ictal early (blocking IEDs shortened interictal periods from 53.6 to 41.4 s), pro-ictal near the transition (stimulation triggered seizures in 38% early vs 100% late). — [Chang 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC7617160/)
- Multidien IEA cycles (most often 20-30 days) are stable for years. Seizures phase-lock to the rising phase (13/14), with combined-phase RR 6.8. — [Baud 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5758806/)
- Pseudo-prospective 24-h forecasts: AUC 0.74 in development and 0.70 in validation; better than chance in 83% and 66% of patients; at 3-day horizon only 11% and 39%. — [Proix 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC7968722/)
- A 90-s hippocampal FC snapshot forecasts 24-h risk as well as cycle models needing months of baseline (abstract claim). — [Khambhati 2024](https://www.nature.com/articles/s41591-024-03149-6)

### Inferences
- A realistic performance ceiling for biomarker forecasting is AUC about 0.7-0.8. TUSZ results far above that on short windows likely reflect leakage or near-onset (detection-like) signal rather than a true preictal state.
- CSD direction is patient-specific at short timescales (Chang 2018). Features should be evaluated per patient against surrogates, not assumed to rise universally.

### Gaps
- Khambhati 2024 full-text numbers (exact AUC, split, chance test) could not be verified because the paper is paywalled.
- No peer-reviewed study found that validates CSD-based forecasting on **scalp** EEG with pseudo-prospective evaluation.

## Can E/I balance and neural mass model parameters be estimated, and do they change before seizures?

### Takeaway
Estimation is feasible (Kalman-type tracking of Jansen-Rit on years of iEEG; PSD fitting of 12-parameter models). Evidence that the estimates change *before* seizures is limited to older short-term iEEG work (Aarabi & He 2014) and a scalp aperiodic-exponent study showing a global preictal shift toward **inhibition**.

### Cited Findings
- Jansen-Rit parameters (u, alpha_ip, alpha_ep, alpha_pe, alpha_pi) were tracked per channel with an assumed-density Kalman filter over 3,010 seizures. MSE 0.2-0.9 mV; instability in less than 1% of data. — [Karoly 2018](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006403)
- Ictal parameter pathways are stereotyped. Onset dynamics did not predict seizure duration, but pre-offset parameters did. — [Karoly 2018](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006403)
- Fitting a 12-parameter neural mass model to the iEEG PSD yielded sensitivity 87.07% / 92.6% at FPR 0.2 / 0.15 per h in 21 patients (abstract/snippet only). — [Aarabi & He 2014](https://pubmed.ncbi.nlm.nih.gov/24374087/)
- On 128-channel scalp EEG, the aperiodic exponent increased in the approximately 13 min before seizures (steeper than interictal, t = 6.94, p < 0.001 in non-epileptic regions). The change was global, with no epileptic vs non-epileptic difference (p = 0.16). No predictive metrics were reported. — [Duma 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12581463/)
- The Wendling model attributes fast ictal onset to impaired dendritic GABAergic inhibition. — [Wendling 2002](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=(TITLE:%22Epileptic%20fast%20activity%20can%20be%20explained%20by%20a%20model%20of%20impaired%20GABAergic%20dendritic%20inhibition%22)&resultType=core&format=json)
- The Epileptor frames onset and offset as bifurcations driven by a slow variable. — [Jirsa 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC4107736/)

### Inferences
- The project hypothesis "E/I shifts toward excitation before seizures" is **not** what the one scalp study found. Duma 2025 found a shift toward inhibition, measured by the aperiodic exponent. Neural mass model E/I estimates should be cross-checked against the aperiodic exponent, and both directions should be allowed.
- The PSD-fitting route (Aarabi & He) is the simplest baseline for TUSZ. Kalman tracking (Karoly) gives continuous trajectories but is costly and less identifiable on scalp data.

### Gaps
- Aarabi & He 2014 full text was not accessible, so the evaluation details (chance test, out-of-sample) are unknown.
- I found no peer-reviewed study applying Jansen-Rit/Wendling parameter tracking to **pre-ictal scalp EEG** for forecasting. This is the gap our project fills. It is a risk as well as a novelty.

## What this means for scalp EEG / TUSZ and our project

### Takeaway
TUSZ can test short-timescale (minutes to hours) preictal markers: CSD variance and autocorrelation, aperiodic exponent, neural mass model E/I parameters, and IED rate. It cannot test the multidien cycles that drive most validated forecasting performance.

### Cited Findings
- Most forecasting power in validated work comes from cycle phase over days to weeks. — [Proix 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC7968722/); [Baud 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5758806/); [Maturana 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7195436/)
- A scalp-EEG preictal E/I signature exists at the minutes scale (aperiodic exponent, theta and delta increases), using 60-s SPRiNT windows with 90% overlap over 1-40 Hz. — [Duma 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12581463/)
- Recommended evaluation: chronological or held-out split, AUC over time in warning, surrogate-based improvement over chance, Brier skill score, and reliability diagrams. — [Proix 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC7968722/)

### Inferences
- Suggested feature set for TUSZ: (1) variance and lag-1 autocorrelation / ACFW per channel; (2) aperiodic exponent (specparam); (3) Jansen-Rit or Wendling E/I parameters (A/B, alpha_ep/alpha_ip); (4) IED rate; (5) time of day if available. Compare each against a random/surrogate predictor, per patient.
- Frame the claim as "earlier preictal-state detection within a recording", not as "multiday forecasting".
- Control for sleep and drowsiness and for artifacts. Both change the aperiodic exponent and variance independently of seizures.

### Gaps
- None of the reviewed papers used TUSZ. Transfer of any effect size to TUSZ is untested.
