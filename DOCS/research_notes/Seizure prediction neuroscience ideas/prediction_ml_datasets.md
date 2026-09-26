# ML Seizure Prediction and Forecasting (2023-2026): Honest Performance, Evaluation Protocol, and Open Datasets

Scope note: research done 2026-09-25 with ~20 search/fetch calls. Several primary pages (Lancet Neurol, Nature Sci Rep, one PMC page) were blocked (403 / captcha), so some numbers come from search-result abstracts rather than full text; this is flagged where relevant. "PS" = patient-specific, "CP" = cross-patient / patient-independent. "Foundational" = pre-2023.

## Q1. Best cross-patient (patient-independent) seizure prediction results on scalp EEG, 2023-2026

### Takeaway
Under honest leave-one-patient-out (LOPO) evaluation, cross-patient scalp-EEG prediction is modest: AUC about 0.70-0.82, sensitivity about 63-74%, and event-level false-prediction rates of about 0.3-0.6/h. That is far below the 90-99% "accuracy" figures common in the literature. On TUSZ, the only prediction benchmark (MLSPred-Bench) reports segment-level results only: 88.7% best validation accuracy, and 70% sensitivity with 60% specificity on raw-EEG ResNet. It reports no alarm-level sensitivity/FPR/h, which leaves a clear gap a student project could fill.

### Cited Findings
**TUSZ / MLSPred-Bench (CP, 2024 preprint, 2025 journal)**
- MLSPred-Bench turns the detection-annotated TUSZ corpus into 12 ML-ready prediction benchmarks. It uses SPH ∈ {2,5,15,30} min and SOP ∈ {1,2,5} min, producing more than 150 GB of data — [PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC12423417/); [bioRxiv](https://www.biorxiv.org/content/10.1101/2024.07.17.604006v1); [code](https://github.com/pcdslab/MLSPred-Bench); [PubMed](https://pubmed.ncbi.nlm.nih.gov/40949826/)
- Source data: TUSZ has 675 subjects and 1,645 sessions. After filtering to seizure-containing records, 287 subjects and 1,175 sessions remain, with more than 4,000 seizures over about 10,000 h — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12423417/)
- The split is patient-independent: 208 subjects train, 45 validation, 34 test. Preictal is defined as [onset − SOP − SPH, onset − SOP]. A seizure is included only if the gap from the previous seizure exceeds SOP+SPH. Data are cut into 5-s non-overlapping windows at 256 Hz on a 20-channel bipolar montage — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12423417/)
- Results: best validation accuracy was 88.73% (ResNet, raw EEG). Random forest with hand-crafted features reached 74.76% AUC. ResNet on raw data gave 70.32% sensitivity and 59.63% specificity. All results are segment-level, with no FPR/h or alarm-level metric. The authors note overfitting, unbalanced seizure distribution across splits, and "potential data leakage risks when using longer SPH values" — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12423417/)
- Caveat (terminology): MLSPred-Bench's use of SPH/SOP is effectively swapped relative to the Winterhalder/Maiwald convention, where SPH is the gap/intervention time and SOP is the window in which the seizure must occur. The paper calls SPH the "target prediction window" and SOP the "minimum gap" — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12423417/). Students should state which convention they use.

**CHB-MIT / Siena (CP)**
- CG-MambaNet (arXiv 2606.08226, 2026) was evaluated with LOPO repeated over 5 seeds on CHB-MIT (22 patients, ~982 h, 198 seizures) and Siena (6 patients used, ~128 h, 58 seizures), on 16 common bipolar channels — [arXiv](https://arxiv.org/html/2606.08226)
  - CHB-MIT: AUC 0.815, sensitivity 74.3%, window-level FPR 112.4/h vs event-level FPR 0.32/h, mean lead time 23.4 min.
  - Siena: AUC 0.710, sensitivity 63.2%, event-level FPR 0.55/h.
  - The event-level persistence filter cut the reported FPR about 351-fold, so the choice of FPR definition dominates the headline number.
  - Prior CP baseline (Jemal et al. 2024, domain adaptation CDAN+E): AUC 0.75 CHB-MIT / 0.61 Siena; unadapted 0.69 / 0.48 — [arXiv](https://arxiv.org/html/2606.08226)
  - The authors state that more than 96% of published seizure-prediction studies use randomised or patient-specific splits that allow leakage. They call 90-99% sensitivities "artefacts of the evaluation protocol" — [arXiv](https://arxiv.org/html/2606.08226). (This is a preprint and the 96% figure is the authors' own survey; treat it as a claim.)
- 3D-SERESNet reported 84.41% sensitivity with FPR 0.232/h in patient-independent CHB-MIT experiments. Only the search abstract was seen; LOPO details and alarm definition were not verified — [PubMed](https://pubmed.ncbi.nlm.nih.gov/41446734/)
- For comparison, a patient-independent LOPO *detection* model (not prediction) on CHB-MIT still gave 4.7 false alarms/h — [Sci Rep 2026](https://www.nature.com/articles/s41598-026-55673-9); [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13530247/). This shows how hard honest CP evaluation is.

**EPILEPSIAE (PS, for contrast)**
- Costa et al. 2024 used 40 EPILEPSIAE patients and PS models (logistic regression, SVM ensembles, shallow NN ensembles). Moving from crisp prediction to probabilistic forecasting raised seizure sensitivity by up to 146% and the number of patients above chance by up to 300% — [Sci Rep 2024 abstract via ADS](https://ui.adsabs.harvard.edu/abs/2024NatSR..14.5653C/abstract); [PubMed](https://pubmed.ncbi.nlm.nih.gov/38454117/). The full-text SPH/SOP and absolute sensitivity were not retrieved.
- Related work from the same group: "On the performance of seizure prediction ML methods across different databases: the sample and alarm-based perspectives" — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11284155/) (content not retrieved: captcha); and concept-drift adaptation for EPILEPSIAE prediction — [Sci Rep 2024](https://www.nature.com/articles/s41598-024-57744-1)

### Inferences
- Realistic CP scalp-EEG targets for a student are AUC ~0.7-0.8, alarm sensitivity ~60-75%, and FPR ~0.3-0.6/h under event-level alarm merging, with lead times of ~20 min. Any CP result above ~90% sensitivity with FPR <0.1/h should be treated as a probable leakage artefact until shown otherwise.
- The TUSZ/MLSPred-Bench gap is a clear novelty opportunity. No alarm-level evaluation exists (sensitivity per seizure, FPR/h, time-in-warning, surrogate/random-predictor test), and there is no per-seizure-type breakdown, even though TUSZ carries type labels.
- TUSZ sessions are short (routine/EMU clips). Many seizures lack long seizure-free preictal context, so long SPH/SOP configurations shrink the eligible set and inflate class imbalance. MLSPred-Bench's own leakage warning for longer SPH suggests that overlapping sessions or adjacent-seizure contamination deserve checking.

### Gaps
- No verified 2023-2026 CP prediction results for EPILEPSIAE scalp data were found (most EPILEPSIAE work is PS).
- Time-in-warning is rarely reported for CP scalp studies; none were found.
- No third-party re-evaluations of MLSPred-Bench were found.

## Q2. Rigorous evaluation standards

### Takeaway
A credible prediction study needs four things:
- chronological, out-of-sample testing on held-out seizures or patients
- alarm-level metrics (sensitivity, FPR/h or time-in-warning) at a stated SPH/SOP
- a statistical test against chance (seizure-time surrogates or an analytic random predictor)
- ideally, pseudo-prospective evaluation on held-out continuous data

The Kaggle/Melbourne 2016 contest showed that even the top algorithms lost AUC on truly held-out data (0.81 to 0.75).

### Cited Findings
- **Foundational:** Mormann, Andrzejak, Elger & Lehnertz (2007), "Seizure prediction: the long and winding road," *Brain*. This is the classic critique; it argued that earlier optimistic results failed under proper statistical validation — [ResearchGate record](https://www.researchgate.net/publication/6787018_Seizure_prediction_The_long_and_winding_road)
- **Foundational:** Seizure-time surrogates (Andrzejak et al. 2003) replace the true seizure-onset times with randomly shuffled onset times. A method is significant only if it beats its performance on the surrogates — [summary in Lehnertz et al. / Freiburg paper](https://jeti.uni-freiburg.de/papers/YEBEH2117.pdf); see also "Seizure prediction: any better than chance?" — [PubMed](https://pubmed.ncbi.nlm.nih.gov/19576849/). The analytic random-predictor test is Schelter et al. 2006, "Testing statistical significance of multivariate time series analysis techniques for epileptic seizure prediction" (Chaos). Its URL was not retrieved in this session; cite it via the Freiburg PDF above.
- **Foundational:** The Brier score was proposed for probabilistic seizure forecasts — [Springer chapter](https://link.springer.com/chapter/10.1007/978-3-540-89208-3_405)
- **Foundational:** Kuhlmann et al. 2018, "Seizure prediction — ready for a new era," *Nat Rev Neurol* — [Nature Rev Neurol](https://www.nature.com/articles/s41582-018-0055-2) (the review; details not fetched this session).
- **Foundational, Kaggle/Melbourne 2016 contest (Kuhlmann et al. 2018, Brain):**
  - Participation: 646 individuals in 478 teams submitted 10,082 algorithms.
  - Data: 3 NeuroVista patients, chosen as those with the lowest prediction performance in the original trial, with 559/393/374 days of recording.
  - Preictal = the 66 min before lead seizures (six 10-min clips). Interictal required ≥3 h before and ≥4 h after any seizure.
  - AUC: 1st place public 0.85, private 0.81, and 0.75 on held-out continuous data (pseudo-prospective).
  - For matched time-in-warning, 2 patients gained about 1.9× sensitivity over the original trial algorithm.
  - Winning features were spectral power, fractal dimension, Hurst exponent, Hjorth parameters, correlation and entropy, used in ensembles (XGBoost, RF).
  - Sources: [Brain](https://academic.oup.com/brain/article/141/9/2619/5066003); [Mayo record](https://mayoclinic.elsevierpure.com/en/publications/epilepsyecosystemorg-crowd-sourcing-reproducible-seizure-predicti)
- **Leakage and metric inflation, 2026:**
  - Randomised or patient-specific splits allow leakage; the preprint claims more than 96% of studies use them.
  - Window-level vs event-level FPR differ about 351-fold.
  - Source: [arXiv 2606.08226](https://arxiv.org/html/2606.08226)
- **Pseudo-prospective with surrogates, 2025:**
  - Nasseri et al. treated a forecast as significant only if its AUC exceeded 95% of surrogate AUCs (p<0.05).
  - They reported time-in-warning (h/day) alongside sensitivity.
  - Source: [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12344589/)
- **Nonstationarity:** Long-term iEEG prediction must deal with data nonstationarity (concept drift) — [arXiv 2201.04137](https://arxiv.org/pdf/2201.04137); [Sci Rep 2024 concept drift](https://www.nature.com/articles/s41598-024-57744-1)

### Inferences (recommended student protocol)
1. **Splits.** Use patient-disjoint splits (LOPO or fixed patient-level train/val/test, as in MLSPred-Bench). Within a patient, split chronologically. Never shuffle windows across seizures, overlapping windows, or sessions of the same patient across splits. For TUSZ, verify that subject IDs don't recur across train/dev/eval.
2. **Declare the preictal definition.** Report SPH (intervention time) and SOP (occurrence window) in the Winterhalder convention, the interictal buffer (e.g. ≥4 h from any seizure as in Kaggle 2016), and the lead-seizure definition.
3. **Report alarm-level metrics.** Give seizure sensitivity, FPR/h (event-merged, with the refractory period stated), time-in-warning (%), and AUC. Report window-level numbers only as secondary.
4. **Test against chance.** Use seizure-time surrogates (≥200 shuffles) or the analytic random predictor. Report the number of patients (or seizure types) significantly above chance. Report the improvement-over-chance (IoC = sensitivity − random-predictor sensitivity at the same time-in-warning).
5. **Fix hyperparameters and thresholds on validation data only**, including operating-point calibration, then report once on test.
6. **Report the forecasting variant too.** For probabilistic output, add the Brier score/BSS and calibration curves.

### Gaps
- Could not retrieve the full Kuhlmann 2018 Nat Rev Neurol text or the epilepsyecosystem.org leaderboard page to quote their post-contest results or recommended reporting checklist.
- No formal "reporting guideline" (e.g. a consensus checklist) for seizure-prediction ML published 2023-2026 was found.

## Q3. Seizure forecasting (probabilistic risk, multiday cycles), including wearables, 2021-2026

### Takeaway
Forecasting — risk estimates over hours to days — now outperforms crisp prediction and is feasible from implanted devices (RNS: up to 3 days ahead) and wearables (AUC ~0.70-0.78 pseudo-prospectively). Much of the skill comes from multiday (multidien) cycles rather than short-term preictal EEG changes.

### Cited Findings
- **Proix et al. 2021, Lancet Neurol (foundational, retrospective with pseudo-prospective validation):**
  - Used RNS chronic EEG from 18 patients (development) and 157 patients (validation).
  - Forecast electrographic and self-reported seizures up to 3 days in advance, using multidien interictal epileptiform activity cycles.
  - Sources: [Lancet Neurol abstract](https://www.thelancet.com/journals/laneur/article/PIIS1474-4422(20)30396-3/abstract); [eScholarship PDF](https://escholarship.org/content/qt4x778199/qt4x778199.pdf?t=s8w30i); [Wyss Center summary](https://wysscenter.ch/update/a-weather-station-for-epilepsy/). Exact AUCs were not retrieved (403).
- **Stirling et al. 2021, Front Neurol (foundational):**
  - n=11, Fitbit heart rate/sleep/steps plus e-diary for ≥6 months (mean 14.6 months), weekly retraining.
  - Mean AUC 0.74; all 11 participants were better than chance.
  - Sources: [PubMed](https://pubmed.ncbi.nlm.nih.gov/34335457/); [medRxiv](https://www.medrxiv.org/content/10.1101/2021.05.20.21257495v1.full)
- **Nasseri et al. 2025, Epilepsia (pseudo-prospective wearables):**
  - Data: 11 participants, wrist wearables (Empatica E4, Fitbit), seizures labelled by implanted/subscalp EEG (UNEEG SubQ, RNS, RC+S). Mean 337 days and 75 seizures per participant.
  - Short-horizon SWS (15-min resolution): AUC 0.78, sensitivity 77%, time-in-warning 6.3 h/day; above chance in 10/11 participants.
  - Long-horizon SRS (up to 44 days): AUC 0.72, sensitivity 81%, 4.58 h/day high-risk, BSS 0.03.
  - Daily SRS AUC was 0.64 overall (0.68 in above-chance participants).
  - Sources: [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12344589/); [Wiley](https://onlinelibrary.wiley.com/doi/10.1111/epi.18466)
- **Prospective pilot from cycles of self-reported events plus heart rate (2023, eBioMedicine)** — [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10300292/); [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2352396423002219)
- **Seizure occurrence linked to multiday cycles in diverse physiological signals** — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10733995/)
- **Other forecasting work:**
  - e-diary-alone forecasting tools were rigorously evaluated, with commentary that cycle tracking beats a prospective moving average — [Epilepsia commentary](https://onlinelibrary.wiley.com/doi/10.1002/epi.70084)
  - Systematic review/meta-analysis of automated forecasting algorithms (2024) — [J Neurol](https://link.springer.com/article/10.1007/s00415-024-12655-z)
  - "Seizure forecasting: where do we stand?" — [PubMed](https://pubmed.ncbi.nlm.nih.gov/36780237/)
  - Seizure forecasting with ultra-long-term EEG (2024) — [Clin Neurophysiol](https://www.sciencedirect.com/science/article/pii/S1388245724002761)
- **Ongoing trial:** wearable-EEG seizure prediction — [ClinicalTrials.gov NCT06978842](https://clinicaltrials.gov/study/NCT06978842)

### Inferences
- TUSZ recordings are short hospital sessions, so multiday-cycle forecasting cannot be done on TUSZ. A TUSZ project should frame itself as short-horizon (minutes) prediction and acknowledge that cycle-based forecasting needs chronic data (NeuroVista, RNS, wearables).

### Gaps
- Exact Proix 2021 AUCs/BSS were not retrieved. Karoly/Cook cycle papers (e.g. Karoly 2021 Lancet Neurol forecasting from cycles) were not fetched in this session.

## Q4. Does predictability differ by seizure type?

### Takeaway
There is almost no direct human evidence comparing predictability across seizure types. Most prediction work is on focal epilepsy (NeuroVista, RNS, EPILEPSIAE, and the RNS forecasting cohort are all focal). Generalized/absence seizures were long assumed to be abrupt, "stochastic" events, but rat absence-epilepsy models show above-chance prediction of spike-wave discharges. This is an open, novel question that TUSZ's type labels make testable.

### Cited Findings
- Generalized seizures were historically regarded as stochastic. In genetic rat models of absence epilepsy (GAERS/WAG-Rij), however, above-chance prediction of spike-wave discharges was achieved from cortico-thalamic LFP wavelet features — [eNeuro 2021](https://www.eneuro.org/content/9/1/ENEURO.0160-21.2021); [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8856717/)
- Human focal seizures could be predicted from Utah-array intracortical signals away from the seizure onset zone, with AUC reaching 90% for at least one feature type in each patient (PS, small n) — [PLOS One](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0211847)
- Proix 2021's forecasting cohort was restricted to adults with focal epilepsy — [Lancet Neurol](https://www.thelancet.com/journals/laneur/article/PIIS1474-4422(20)30396-3/abstract)
- TUSZ labels eight seizure types: FNSZ, GNSZ, ABSZ, CPSZ, TCSZ, TNSZ, SPSZ, MYSZ — [arXiv 2201.08780](https://arxiv.org/pdf/2201.08780); [TUSZ paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC6246677/)

### Inferences
- A novel TUSZ project could stratify MLSPred-Bench-style CP prediction by seizure type (focal vs generalized vs absence), with type-specific surrogate tests. Class counts for ABSZ/MYSZ/TNSZ are small, so power may be limited and confidence intervals must be reported.

### Gaps
- No 2023-2026 human study directly comparing prediction performance by seizure type was found.

## Q5. Explainable / interpretable prediction

### Takeaway
XAI in seizure prediction is dominated by SHAP applied to CNNs and gradient-boosted models, mostly on CHB-MIT with PS or leaky splits. Reported insights are that the most important channel shifts at the interictal-to-preictal transition and that importance can highlight onset channels. The classic contest winners relied on spectral power, entropy, fractal and Hjorth features.

### Cited Findings
- SHAP-driven feature analysis for seizure prediction (J Med Syst 2025) — [Springer](https://link.springer.com/article/10.1007/s10916-025-02211-1); [PubMed](https://pubmed.ncbi.nlm.nih.gov/40493270/)
- Search-abstract claims, not verified in full text:
  - A 1D-CNN with SHAP reached 98.14% accuracy on CHB-MIT, a likely PS/window-level number.
  - The top-contributing channel changes when the state switches from interictal to preictal.
  - Channel-aggregated SHAP can help localize the focus.
  - Sources: [Springer NCA 2024](https://link.springer.com/article/10.1007/s00521-024-10915-7); [J Med Syst](https://link.springer.com/article/10.1007/s10916-025-02211-1)
- Kaggle 2016 winning features: spectral power, fractal dimension, Hurst exponent, Hjorth parameters, correlation, entropy — [Brain 2018](https://academic.oup.com/brain/article/141/9/2619/5066003)
- Preictal period length optimization for DL prediction — [arXiv 2407.14876](https://arxiv.org/pdf/2407.14876)

### Inferences
- The very high XAI-paper accuracies indicate leaky or PS evaluation. A credible contribution would pair explanations with honest CP evaluation. One example: check whether SHAP channel importance on TUSZ aligns with annotated seizure-onset channels, or whether models exploit artefacts such as EMG or recording-session cues.

### Gaps
- No rigorous (LOPO, surrogate-tested) XAI prediction study was found.

## Q6. Dataset catalogue

### Takeaway
- **Scalp EEG:** TUSZ is the largest free source (675 subjects), but its sessions are short. CHB-MIT and Siena are small but have continuous multi-hour files. EPILEPSIAE has the best long preictal scalp/iEEG data but is paid.
- **Long-term iEEG:** NeuroVista (epilepsyecosystem), SWEC-ETHZ long-term (18 patients, 2,321 h), and OpenNeuro iEEG-BIDS sets.
- **Microelectrode seizure data:** scarce. The EBRAINS Utah-array dataset (5 patients, 12 seizures, 10 min preictal) is the main open option; DANDI's human single-unit sets are mostly cognitive tasks, not seizures.

### Cited Findings
| Dataset | Access | Size | Recording | Long preictal? | Source |
|---|---|---|---|---|---|
| **TUSZ** (v2.0.x) | Free after registration/data agreement at NEDC | 675 subjects; v2.0.0 = 7,377 EDF files, ~1,476 h (per one paper); MLSPred-Bench cites >4,000 seizures in ~10,000 h (contradictory hour counts; check the version README). 8 seizure types. ≥250 Hz, ≥17 channels, heterogeneous | Scalp, clinical routine/EMU | Mostly short sessions; limited, and SOP+SPH filters remove many seizures | [NEDC downloads](https://isip.piconepress.com/projects/nedc/html/tuh_eeg/); [TUSZ paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC6246677/); [arXiv 2201.08780](https://arxiv.org/pdf/2201.08780); [MLSPred-Bench](https://pmc.ncbi.nlm.nih.gov/articles/PMC12423417/) |
| **CHB-MIT** | Open, PhysioNet | 23 cases from 22 pediatric subjects; ~982 h, 198 seizures (per CG-MambaNet); 256 Hz | Scalp, bipolar | Yes: mostly 1-h continuous files, some 2-4 h, contiguous | [PhysioNet](https://physionet.org/content/chbmit/1.0.0/); [arXiv](https://arxiv.org/html/2606.08226) |
| **Siena** | Open, PhysioNet | 14 adults, 47 seizures, ~128 h, 512 Hz | Scalp 10-20 | Moderate (multi-hour files) | [PhysioNet](https://physionet.org/content/siena-scalp-eeg/1.0.0/) |
| **EPILEPSIAE** | Restricted; requires a financial contribution | 275 patients, long-term continuous, rich metadata (Freiburg, Coimbra, Paris) | Scalp and iEEG | Yes: gold standard for PS prediction | [PubMed](https://pubmed.ncbi.nlm.nih.gov/20863589/); [NITRC](https://www.nitrc.org/projects/epilepsiaedb/); [Klatt 2012](https://onlinelibrary.wiley.com/doi/10.1111/j.1528-1167.2012.03564.x) |
| **Melbourne NeuroVista (epilepsyecosystem.org)** | Contest data plus ecosystem access by agreement | Contest: 3 patients, 374-559 days each, 10-min clips; the full trial has more patients | Chronic implanted iEEG (16 ch) | Yes: months to years | [Brain 2018](https://academic.oup.com/brain/article/141/9/2619/5066003) |
| **SWEC-ETHZ iEEG** | Open download | Long-term: 18 patients, 2,321 h, 244 seizures, 512/1024 Hz; short-term: 100 recordings from 16 patients | Intracranial | Yes (long-term set, continuous implant to explant) | [SWEC-ETHZ site](http://ieeg-swez.ethz.ch/); [Zenodo mirror](https://zenodo.org/records/14578383); [arXiv 2206.09951](https://arxiv.org/pdf/2206.09951) |
| **OpenNeuro iEEG-BIDS** | Open | ds003029 (iEEG-BIDS seizure data); ds003876 multicenter interictal iEEG | iEEG | ds003029: short ictal snippets; ds003876: interictal only | [OpenNeuro ds003876](https://openneuro.org/datasets/ds003876/versions/1.0.1); ds003029 mentioned in [arXiv 2206.09951 context](https://arxiv.org/pdf/2206.09951) |
| **EBRAINS Utah-array multimodal dataset** (2025) | Open, CC BY 4.0, DOI 10.25493/ZC9M-2ES | 5 patients, 12 seizures; Utah array (96-ch) LFP plus MUA (30 kHz raw) plus ECoG/depth iEEG | Microelectrode plus iEEG | Short: 10 min preictal, 5 min postictal | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12065801/); [PubMed](https://pubmed.ncbi.nlm.nih.gov/40348768/) |
| **DANDI human single-neuron sets** | Open (NWB) | e.g. dandiset 000623 (20 patients, movie watching, single units plus LFP plus iEEG); a recognition-memory set (1,863 neurons, 59 subjects) | Behnke-Fried microwires in epilepsy patients | No seizures; cognitive tasks | [OpenNeuro/DANDI description](https://openneuro.org/datasets/ds004798/versions/1.0.5); [Sci Data 2020](https://www.nature.com/articles/s41597-020-0415-9) |
| **AJILE12** | Open (DANDI) | 55 semi-continuous days of iEEG plus pose | iEEG during clinical monitoring | Continuous, but a behavior focus | [DANDI search result](https://notebooks.dandiarchive.org/) |
| **Dataset lists** | Open | Curated list of open human electrophysiology datasets; review of epilepsy datasets | – | – | [openlists/ElectrophysiologyData](https://github.com/openlists/ElectrophysiologyData); [arXiv 2306.12292](https://arxiv.org/pdf/2306.12292) |

- Foundational microelectrode seizure studies whose data are *not* confirmed public:
  - Multiscale Utah-array seizure recordings — [PubMed 30898669](https://pubmed.ncbi.nlm.nih.gov/30898669/)
  - Single-neuron dynamics in human focal epilepsy — [PubMed 21441925](https://pubmed.ncbi.nlm.nih.gov/21441925/)
  - Pre-seizure single-neuron criticality — [arXiv 2004.10642](https://arxiv.org/pdf/2004.10642)
  - Review arguing for clinical translation of microelectrodes — [Brain Commun](https://academic.oup.com/braincomms/article/2/2/fcaa082/5857125)

### Inferences
- For a TUSZ-centred project, the best design is:
  - train and evaluate CP on TUSZ (MLSPred-Bench splits or a stricter patient-disjoint re-split with alarm-level metrics and surrogates)
  - test cross-dataset transfer to CHB-MIT and Siena, which is itself a strong, rarely-done generalization test
  - optionally use SWEC-ETHZ or NeuroVista to show longer-horizon behaviour
- Microelectrode/single-unit seizure *prediction* is not realistically feasible with open data. Only 12 seizures with 10-min preictal windows are available (EBRAINS). At most it could support an exploratory or mechanistic side-analysis, not a trained predictor.

### Gaps
- Could not confirm current TUSZ version numbering (v2.0.1 vs v2.0.3) or exact total hours. Sources conflict: ~1,476 h vs "10,000 h", which may count the full TUEG session durations. Check the NEDC README directly.
- Open RNS datasets: none confirmed openly downloadable. RNS data (Proix 2021) appear to require an agreement with NeuroPace/UCSF.
- HUP iEEG (Penn) open dataset and IEEG.org portal specifics were not verified in this session. The IEEG.org portal hosts many long-term iEEG datasets, including Mayo/UPenn Kaggle 2014 data, but no URL was checked here.
- The OpenNeuro ds003029 description was not directly fetched.
