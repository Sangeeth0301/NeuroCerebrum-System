# Body reaction to seizures: ECG/heart rate, multimodal wearables, and video semiology

Per-paper files are in `research/papers/B_*.md`. Numbers marked (abs) come only from abstracts; (FT) were checked in full text.

## Comparison table

| Paper | Venue / year | Signals | Patients / seizures (types) | Method | Key numbers | Timing vs EEG / latency |
|---|---|---|---|---|---|---|
| Leutmezer et al. (FOUNDATIONAL) | Epilepsia 2003 | ECG (RR) + scalp EEG | 58 pts / 145 focal sz | RR-interval change-point analysis, 90 s window | Tachycardia 86.9%, bradycardia 1.4% (abs) | HR rise **13.7 s before** EEG onset (TLE), **8.2 s before** (extratemporal) (abs) |
| Kato et al. (older) | Neurology 2014 | ECG + video-EEG | 21 mTLE pts / 77 focal sz | Retrospective timing | HR rise 29/29 right, 42/48 left (abs) | **-11.5 ± 14.8 s** (right) vs **+9.2 ± 21.7 s** (left) (abs) |
| Jeppesen et al. | Epilepsia 2019 | Wearable ECG, HRV | 100 pts; 43 with sz / 126 sz (108 nonconvulsive, 18 convulsive) | 26 HRV algorithms; best = CSI-type sympathetic index + HR slope | Responders 53.5%; Se 93.1% all, 90.5% nonconvulsive; FAR 1.0/24 h (abs) | Median latency 30 s (abs) |
| Jeppesen et al. | eBioMedicine 2025 (phase 3) | ECG patch -> smartphone, CSI/ModCSI | 101 enrolled, 17 eligible / 42 sz (19 FBTC, 23 focal) | Patient-specific threshold (105% of baseline max) + app behavioural test | Se 90.5%; FBTC 100%; focal 82.6%; FAR median 1.1/24 h (FT) | Median latency 28 s (15-278) (FT) |
| Regalia et al. | Epilepsy Research 2019 | Wrist EDA + ACC (Empatica) | Pooled inpatient/outpatient data | ML on ACC+EDA | GTCS Se 92-100%; FAR 0.2-1/day inpatient, <0.5 outpatient (abs) | n/a |
| Onorati et al. (companion) | Front Neurol 2021 | Wrist EDA + ACC | 152 pts; 66 sz (12 GTC, 54 FBTC) | Frozen ML detector, 40 features | Se 0.92 ped / 0.94 adult; FAR 1.26 / 0.57 per 24 h (FT) | Latency 37.5 ± 21.1 s (FT) |
| Stirling et al. | Front Neurol 2021 | Fitbit HR, sleep, steps | 11 pts, mean 135 diary sz | Ensemble ML+NN risk forecast, weekly retraining | Better than chance 11/11 hourly, 10/11 daily (abs); mean AUC ~0.74 (secondary source) | Time in warning: 37 min (hourly), 3 days (daily) (abs) |
| Swinnen et al. (SeizeIT2) | Epilepsia Open 2026 | Behind-ear 2-ch EEG + ECG | 192 pts / 616 focal sz | Offline algorithm + human review | Alg: Se 0.73, precision 0.004; +review: Se 0.31, precision 0.83; Se 0.74 with tachycardia vs 0.60 without (abs) | Not in abstract |
| Karácsony et al. | Sci Rep 2022 | IR + depth video | 26 pts / 115 sz (FLE, TLE) | I3D + LSTM action recognition | F1 0.833 FLE/TLE, AUC 0.89; F1 0.763 3-class (FT) | 2-s clips, "near real time" |

Sources: [Leutmezer](https://pubmed.ncbi.nlm.nih.gov/12614390/), [Kato](https://www.neurology.org/doi/10.1212/WNL.0000000000000864), [Jeppesen 2019](https://onlinelibrary.wiley.com/doi/10.1111/epi.16343), [Jeppesen 2025](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12516532/fullTextXML), [Regalia](https://pubmed.ncbi.nlm.nih.gov/30846346/), [Onorati](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8418082/fullTextXML), [Stirling](https://pubmed.ncbi.nlm.nih.gov/34335457/), [SeizeIT2](https://pmc.ncbi.nlm.nih.gov/articles/PMC13238671/), [Karácsony](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9666544/fullTextXML).

## Q1: Do heart-rate/ECG changes accompany or precede seizures, and by how much?

### Takeaway
Ictal tachycardia is the dominant cardiac reaction in focal seizures (~87% of seizures in one cohort) and, on average, starts several seconds before the scalp-EEG onset, especially in (right) temporal lobe seizures. The lead varies from seizure to seizure and can be negative (HR after EEG).

### Cited Findings
- Tachycardia in 86.9% of 145 focal seizures, bradycardia in 1.4% — [Leutmezer 2003](https://pubmed.ncbi.nlm.nih.gov/12614390/)
- HR increase preceded EEG onset by 13.7 s (TLE) and 8.2 s (extratemporal); more pronounced in mesial TLE and right-hemispheric seizures — [Leutmezer 2003](https://pubmed.ncbi.nlm.nih.gov/12614390/)
- HR-onset relative to EEG: -11.5 ± 14.8 s in right mTLE vs +9.2 ± 21.7 s in left mTLE; max HR change ~41-48 bpm — [Kato 2014](https://www.neurology.org/doi/10.1212/WNL.0000000000000864)
- Ictal HR change >50 bpm identifies HRV-detection responders (PPV 87%, NPV 90%) — [Jeppesen 2019](https://onlinelibrary.wiley.com/doi/10.1111/epi.16343)
- Only 17/101 (autonomic-criterion) patients were eligible for ECG detection in a phase 3 trial — [Jeppesen 2025](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12516532/fullTextXML)

### Inferences
- The "HR before EEG" lead is relative to **scalp** EEG and likely reflects deep onset (the authors attribute it to discharges reaching the central autonomic network before surface electrodes). TUSZ onset labels are scalp-EEG based, so the same effect should be measurable there.
- Because the SD (~15-22 s) is as large as the mean lead, a per-seizure early warning from HR alone will be unreliable; population means are more robust.

### Gaps
- No full-text verification of the Leutmezer/Kato HR-onset definitions.
- No large recent (2018+) study of pre-EEG HR lead across generalized seizure types was found.

## Q2: How well do ECG/HRV and multimodal wearables detect seizures (sensitivity, FAR, latency)?

### Takeaway
Convulsive seizures are detected well by wrist EDA+ACC (Se ~0.92-0.94, FAR ~0.2-1.3/24 h) and by ECG (FBTC 100%); focal seizures are detectable by ECG only in "autonomic responders" (Se ~83-93%), and by bte-EEG+ECG only moderately. Latencies are ~28-37 s after onset, i.e. detection rather than warning.

### Cited Findings
- HRV responders: Se 93.1% (all), 90.5% (nonconvulsive), FAR 1.0/24 h, median latency 30 s — [Jeppesen 2019](https://onlinelibrary.wiley.com/doi/10.1111/epi.16343)
- Phase 3 real-time ECG: Se 90.5%, FBTC 19/19, focal 19/23, median FAR 1.1/24 h, median latency 28 s — [Jeppesen 2025](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12516532/fullTextXML)
- Embrace: Se 0.92 (pediatric) / 0.94 (adult), FAR 1.26 / 0.57 per 24 h, latency 37.46 s — [Onorati 2021](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8418082/fullTextXML)
- EDA response correlates with PGES duration (SUDEP biomarker) — [Regalia 2019](https://pubmed.ncbi.nlm.nih.gov/30846346/)
- SeizeIT2: algorithm Se 0.73 at precision 0.004; with review Se 0.31/precision 0.83; Se 0.74 when tachycardia present vs 0.60 without — [Swinnen 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC13238671/)

### Inferences
- Adding ECG helps most for temporal-lobe focal seizures with tachycardia; for seizures without autonomic reaction, ECG adds little.

### Gaps
- SeizeIT2 FAR/24 h and latency not obtained (full text blocked).

## Q3: Can body signals forecast seizures (early warning)?

### Takeaway
Yes on long timescales: wearable HR cycles (circadian, multiday) forecast risk periods better than chance in all 11 patients (hourly). On the seconds timescale, only the pre-scalp-EEG tachycardia offers a small, variable lead.

### Cited Findings
- Hourly forecast above chance in 11/11, daily in 10/11; high-risk time before seizure 37 min (hourly) / 3 days (daily); HR cycles most informative — [Stirling 2021](https://pubmed.ncbi.nlm.nih.gov/34335457/)
- Mean AUC 0.74 reported in secondary summaries — [ResearchGate listing](https://www.researchgate.net/publication/353275703_Forecasting_Seizure_Likelihood_With_Wearable_Technology) (not verified in full text)

### Inferences
- TUSZ sessions are too short for cycle-based forecasting; our project should target peri-ictal (seconds-minutes) HR change.

### Gaps
- Pseudo-prospective AUC per patient not extracted.

## Q4: Which seizure types show which body reactions? (automated semiology)

### Takeaway
Tonic-clonic seizures: rhythmic limb motion + strong sympathetic activation (tachycardia, post-ictal EDA surge). Focal temporal seizures: early tachycardia, fewer motor signs. Frontal seizures: prominent hypermotor movement that video deep learning can distinguish from temporal seizures (F1 0.83).

### Cited Findings
- FBTC: 100% detected by ECG — [Jeppesen 2025](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12516532/fullTextXML); GTC/FBTC detected by ACC+EDA — [Onorati 2021](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8418082/fullTextXML)
- Mesial TLE: more frequent and larger ictal HR increase — [Leutmezer 2003](https://pubmed.ncbi.nlm.nih.gov/12614390/)
- FLE vs TLE from 3D video: F1 0.833 ± 0.061, AUC 0.89; 3-class incl. non-epileptic F1 0.763 — [Karácsony 2022](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9666544/fullTextXML)

### Inferences
- For TUSZ labels: expect largest HR response in TCSZ/GNSZ-with-convulsion and CPSZ (often temporal), smaller in ABSZ/SPSZ. This is a hypothesis for our analysis, not a published TUSZ result.

### Gaps
- No peer-reviewed quantitative mapping from TUSZ seizure-type labels to HR response was found.

## Q5: Has anyone used the ECG channel in TUSZ?

### Takeaway
No peer-reviewed study was found that analyses the TUSZ ECG/EKG channel for seizure detection or HR timing. The TUSZ paper confirms supplementary channels exist.

### Cited Findings
- TUSZ annotation used 19 EEG channels plus supplementary channels (heart rate and photic stimulation) — [Shah et al. 2018, Front Neuroinform](https://www.frontiersin.org/journals/neuroinformatics/articles/10.3389/fninf.2018.00083/full)
- Some TUH EDF files contain EKG and EMG channels alongside EEG — [dataset report, arXiv 2306.12292](https://arxiv.org/pdf/2306.12292) (preprint)

### Inferences
- This is a genuine gap and a possible novelty point for the project; but ECG channel availability and quality per TUSZ file must be checked first.

### Gaps
- Three searches for TUSZ + ECG found none; a targeted Google Scholar search might still find conference papers.

## Insights for our project (body-reaction module and early warning)
1. Extract RR intervals from the TUSZ EKG channel; compute HR, HR slope, CSI/ModCSI (100-RR window) as in [Jeppesen 2019](https://onlinelibrary.wiley.com/doi/10.1111/epi.16343).
2. Main outputs per seizure: peak HR change (bpm, responder if >50 bpm), HR-onset time relative to TUSZ onset (s), time to max HR.
3. Report the distribution of HR-onset lead by seizure type; literature expects mean leads of ~8-14 s in focal/temporal seizures with large variance ([Leutmezer](https://pubmed.ncbi.nlm.nih.gov/12614390/), [Kato](https://www.neurology.org/doi/10.1212/WNL.0000000000000864)).
4. Treat early warning honestly: deployed ECG detectors alert ~28-30 s after onset ([Jeppesen 2025](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12516532/fullTextXML)); HR could add a few seconds of warning only for a subset of seizures.
5. External validation option: SeizeIT2 open wearable dataset with ECG ([Scientific Data 2025](https://www.nature.com/articles/s41597-025-05580-x)).
