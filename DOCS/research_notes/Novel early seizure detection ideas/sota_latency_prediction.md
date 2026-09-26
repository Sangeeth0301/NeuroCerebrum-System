# SOTA (2023-2026) in Low-Latency Seizure Detection and Short-Horizon Seizure Prediction from EEG (emphasis: TUSZ)

Source-quality legend used below: [FULL] = numbers read from full text (HTML/PDF); [ABS] = numbers from abstract/landing page only; [SNIP] = numbers seen only in a search-engine snippet (not verified against the paper; treat as unconfirmed).

A distinction matters throughout: several papers report *system/processing latency* (compute delay, e.g. 300 ms), which is not the same as *onset detection latency* (seconds from the expert-marked EEG onset to the first alarm). Many TUSZ papers report neither.

## Q1. Which TUSZ papers (v1.5.x / v2.0.x) report onset detection latency, and what are the numbers?

### Takeaway
I found no 2023-2026 TUSZ paper that reports a clear onset-to-alarm detection latency in seconds. The TUSZ literature reports event F1/sensitivity/FA rates, and sometimes compute latency. The NEDC/Picone "low latency" system's 300 ms is a *processing* latency, not seconds-from-onset. The TUSZ baselines to beat are SeizureTransformer (TUSZ v2.0.3 eval, event F1 0.671 under SzCORE scoring) and the Sci Rep 2026 CatBoost benchmark (event sensitivity 0.75 at 0.68 FA/h, which is about 16.3 FA/24h).

### Cited Findings
**SeizureTransformer (Wu, Zhao, Yener; arXiv 2504.00336, won the 2025 Seizure Detection Challenge)** [FULL]
- Trained on TUSZ v2.0.3 plus Siena Scalp EEG, at 256 Hz with 18 channels and 60 s windows (15,360 samples). — [arXiv HTML v3](https://arxiv.org/html/2504.00336v3)
- TUSZ v2.0.3 predefined test set, event-based: F1 0.6713, sensitivity 0.7168, precision 0.6312. Sample-based: F1 0.5730, sensitivity 0.4724, precision 0.7281. — [arXiv HTML v3](https://arxiv.org/html/2504.00336v3)
- Cross-device results. SeizeIT1: event F1 0.4547, sample F1 0.2821. Dianalund: event F1 0.4283, sample F1 0.2282. — [arXiv HTML v3](https://arxiv.org/html/2504.00336v3)
- Post-processing: threshold τ=0.8, binary opening and closing, minimum seizure duration 2 s. Runtime is 3.98 s per hour of EEG (169.96 s for all of TUSZ eval), about 10x faster than EEGWaveNet (39.59 s/h). — [arXiv HTML v3](https://arxiv.org/html/2504.00336v3)
- The paper does not report onset latency. Its design (60 s windows, a 2 s minimum duration and morphological closing) is offline and non-causal. — [arXiv HTML v3](https://arxiv.org/html/2504.00336v3) (the "no latency" point is my reading of the extracted content)

**Sci Rep 2026 TUSZ CatBoost benchmark: "A transparent AI assurance and benchmarking framework for EEG seizure detection on TUSZ seeded with a reproducible gradient-boosting ensemble", Sci Rep 16:11283 (2026)** [SNIP/ABS; full text blocked by a Nature login redirect]
- Offline binary detection on TUSZ v2.0.3 using the official Train/Dev/Eval split, evaluated on continuous EEG. It uses 60 s windows with a 15 s stride, expert features, and three CatBoost ensembles: a within-window base model plus "full" and "high-sensitivity" temporal-context models. — [Sci Rep](https://www.nature.com/articles/s41598-026-41358-w)
- Operating point chosen as an alarm-budget problem: specificity ≥0.93 and FA ≤0.69/h. Eval results: event sensitivity 0.75 at 0.68 FA/h. Window level: AUROC 0.92, balanced accuracy 0.83. Time-based PPV 0.57, recall 0.76. — [Sci Rep](https://www.nature.com/articles/s41598-026-41358-w)
- I could not confirm any onset latency or per-seizure-type numbers, because the full text was inaccessible. — [Sci Rep](https://www.nature.com/articles/s41598-026-41358-w)
- A search snippet (source page not verified) said that seizures shorter than 90 s are detected much less often than longer events. — [search result cluster incl. Sci Rep](https://www.nature.com/articles/s41598-026-41358-w)

**NEDC / Picone real-time systems** [FULL for the 2021 paper]
- Khalkhali, Shawki, Shah, Golmohammadi, Obeid, Picone, "Low Latency Real-Time Seizure Detection Using Transfer Deep Learning" (IEEE SPMB 2021; arXiv 2202.07796). On the TUSZ v1.5.2 *dev* set: 42.05% sensitivity at 5.78 FA/24h (OVLP scoring). Runs at 0.58 xRT on a single 1.7 GHz CPU core, uses 16 GB memory, and has a **latency of 300 ms (system/processing latency)**. — [arXiv 2202.07796](https://arxiv.org/abs/2202.07796); [NEDC PDF](https://isip.piconepress.com/conferences/ieee_spmb/2021/papers/l01_02.pdf)
- The same paper says it lags the top systems of the Neureka 2020 Epilepsy Challenge (TAES-weighted scoring). It also notes that high-performing prior systems are often non-causal, multi-pass and high-latency. — [NEDC PDF](https://isip.piconepress.com/conferences/ieee_spmb/2021/papers/l01_02.pdf)
- Older foundational work (pre-2023): "A Deep Learning-Based Real-time Seizure Detection System" (NEDC, around 2020). I could not open the NSF PAR page. A search snippet says that "feature extraction ... adds 1.1 seconds of delay" in TUSZ real-time systems. — [NSF PAR](https://par.nsf.gov/biblio/10199689-deep-learning-based-real-time-seizure-detection-system) [SNIP]
- The Neureka 2020 challenge winner reached 12.37% sensitivity at 1.44 FP/day (as cited by the SzCORE challenge paper; foundational). — [arXiv 2505.18191](https://arxiv.org/abs/2505.18191)

**REST (Afzal et al., ICML 2024; arXiv 2406.16906)** [FULL]
- Uses TUSZ v2.0.0 (5,545 files; 579 training and 43 evaluation patients) and CHB-MIT (24 patients split 18/3/3). — [arXiv HTML](https://arxiv.org/html/2406.16906)
- Clip-level detection AUROC. TUSZ, 10 s clips: REST 83.6±0.2 vs DCRNN w/SS 82.1 vs Transformer 85.5. CHB-MIT, 4 s clips: REST 96.7 vs DCRNN 88.7. Seizure-type classification weighted F1 is 0.60 (DCRNN w/SS 0.62). — [arXiv HTML](https://arxiv.org/html/2406.16906)
- Efficiency: 1.29 ms inference, 37 KB model, 8.4-9.3K parameters, 9x faster than DCRNN. Clip lengths from 4 to 14 s were tested. It reports no seconds-from-onset latency, only clip-length sweeps. — [arXiv HTML](https://arxiv.org/html/2406.16906)

**Related 2026 streaming work (TUH family, but not a TUSZ latency result)**
- CaMBrain (Durgam et al., arXiv 2605.28792, May 2026): a causal state-space model that runs one recurrent step per 62.5 ms patch and carries its hidden state across the whole recording. On continuous **CHB-MIT**, persistent state vs a 5 s windowed reset gives mean probability at onset 25.2 vs 11.8, probability at the onset patch 21.6 vs 6.2, and patch AUROC 88.9 vs 87.4. These are onset-probability metrics, not latency in seconds. — [arXiv 2605.28792](https://arxiv.org/abs/2605.28792) [FULL, from PDF text]

### Inferences
- No TUSZ paper I found gives "seconds from onset" as a headline metric. A student who reports onset latency distributions (median and IQR per seizure) on the TUSZ v2.0.x eval set under SzCORE scoring would be filling a real gap. The SeizureTransformer eval numbers (event F1 0.671, sensitivity 0.717) are the accuracy bar to hold while cutting latency.
- The SzCORE 30 s pre-ictal tolerance means an event counts as detected even if the alarm fires up to 30 s before onset. Event F1 therefore says nothing about how early the detection came, so latency must be reported separately.
- The 300 ms NEDC figure should not be compared to the 2.3 s CHB-MIT figure. They measure different things.

### Gaps
- Full text of Sci Rep s41598-026-41358-w: whether it reports latency or per-type results is unverified.
- NEDC 2020 real-time system: exact sensitivity/FA/latency not retrieved (NSF PAR fetch failed).
- I did not locate a TUSZ paper reporting median onset-detection delay in seconds for 2023-2026.

## Q2. Latency results on CHB-MIT, Siena, SWEC-ETHZ, EPILEPSIAE, Bonn (patient-specific vs cross-patient)

### Takeaway
Onset-latency reporting lives almost entirely on CHB-MIT and SWEC-ETHZ, and it is mostly patient-specific. Reported values run from about 1.2-2.3 s (newest claims, some from snippets only) up to 8-16 s (cross-patient 1D-CNN and SVM/MLP). The latency definitions vary: some measure from the end of the classified window, some from its start.

### Cited Findings
**Xu, Yang, Ming, Wang, Sawan, "Shorter Latency of Real-time Epileptic Seizure Detection via Probabilistic Prediction" (arXiv 2301.03465; Expert Systems with Applications 2024)** [FULL]
- **Patient-specific, leave-one-seizure-out.** They reframe detection as probabilistic prediction using soft labels over the transition period. — [arXiv abs](https://arxiv.org/abs/2301.03465); [ESWA](https://www.sciencedirect.com/science/article/abs/pii/S0957417423018614)
- CHB-MIT: latency **2.3 ± 0.7 s**, 94/99 seizures detected "during crossing period" (100% after EEG onset), FDR 0.08 ± 0.14/h. — [arXiv HTML](https://arxiv.org/html/2301.03465)
- SWEC-ETHZ (iEEG): latency **4.7 ± 2.0 s**, 84/89 seizures, FDR 0.08 ± 0.09/h. — [arXiv HTML](https://arxiv.org/html/2301.03465)
- Latency definition: the delay between the expert-marked EEG onset and the time the accumulated probability crosses threshold. The authors stress that they measure from the *end of the detected sample* and claim latencies at least 50% shorter than the prior best (4.2 s and 8.1 s). — [arXiv HTML](https://arxiv.org/html/2301.03465)
- Prior-work table in that paper (older and foundational):
  - Shoeb 2010: SVM, CHB-MIT, patient-specific, 0.08 FD/h, 4.6 s.
  - Kharbouch 2011: iEEG, patient-specific, 97% sensitivity, 0.03/h, 5.0 s.
  - Vidyaratne 2016: RNN, CHB-MIT, patient-specific, 100%, 0.08/h, 7.0 s.
  - Wang 2021: 1D-CNN, **non-patient-specific**. CHB-MIT 99.31%, 0.2/h, 8.1 s. SWEC-ETHZ 97.52%, 0.07/h, 13.2 s.
  - Burrello 2020: SWEC-ETHZ, non-patient-specific, 0.0/h, 15.9 s.
  - [arXiv HTML](https://arxiv.org/html/2301.03465)

**Other CHB-MIT / Siena latency claims** [SNIP: verify before citing]
- MGF-Net (montage-guided fusion network; PMC13574979): CHB-MIT, 65/65 test events detected, 100% sensitivity, 0.82 FD/h, **2.03 s latency**. — [PMC13574979](https://pmc.ncbi.nlm.nih.gov/articles/PMC13574979/)
- Persistent-homology detector: CHB-MIT event sensitivity 100%, **1.22 s mean latency**. On Siena, accuracy 96.42%, sensitivity 95.23%, specificity 97.6%, with no Siena latency given in the snippet. — [PMC10773586](https://pmc.ncbi.nlm.nih.gov/articles/PMC10773586/)
- An unnamed study reports a 3.29 s average delay on CHB-MIT and 94.1% accuracy / 90.77% sensitivity on Siena. Another 2023 study reports 3.4 s latency, 97% recall and 0.219 FA/h on CHB-MIT. I could not identify the primary sources for either. — (search snippets only; see Gaps)

**EPILEPSIAE**
- A BiLSTM-wavelet near-real-time detector (Brain Sciences 2026): 161 patients, 1,032 seizures, reduced electrodes. Its "response time" is the time to classify a 0.5 s frame (<0.1 s), a compute latency and not onset latency. — [MDPI Brain Sci 16(1):119](https://www.mdpi.com/2076-3425/16/1/119); [PMC12838899](https://pmc.ncbi.nlm.nih.gov/articles/PMC12838899/) [SNIP]
- The NEDC paper cites an older EPILEPSIAE result: 98.0% accuracy, 98.3% specificity, and 1.0 FA/h for 80% of patients. — [NEDC PDF](https://isip.piconepress.com/conferences/ieee_spmb/2021/papers/l01_02.pdf)

**Siena and cross-dataset evaluation (SzCORE-style)**
- SeizureTransformer trained on TUSZ+Siena drops from event F1 0.67 on TUSZ to 0.43-0.45 on Dianalund and SeizeIT1, a large cross-site generalization gap. — [arXiv HTML v3](https://arxiv.org/html/2504.00336v3)

### Inferences
- Bonn contains isolated 23.6 s single-channel segments with no continuous onset annotation, so it cannot support onset-latency claims. Treat Bonn "latency" numbers with skepticism. (This is my inference; I found no Bonn latency paper.)
- Nearly all sub-5 s latency claims are patient-specific (LOSO within patient) on CHB-MIT. Cross-patient latencies from the same era are around 8-16 s. A cross-patient TUSZ latency under 10 s at a low FA rate would be a notable result.

### Gaps
- Primary sources for the 3.29 s and 3.4 s CHB-MIT latencies are unidentified.
- I found no Siena-specific onset-latency number and no verified EPILEPSIAE onset-latency number from 2023-2026.

## Q3. TUSZ for seizure prediction (MLSPred-Bench) and CHB-MIT prediction horizons and pitfalls

### Takeaway
MLSPred-Bench is the main TUSZ prediction benchmark. It is patient-independent, with SPH of 2/5/15/30 min and SOP of 1/2/5 min. Its best numbers are modest (for example AUC 80.5% and sensitivity 70.3% at SPH 30 / SOP 2). By contrast, CHB-MIT prediction claims such as "76.8 min before onset" are patient-specific, and their false-positive rates are computed per segment rather than per alarm.

### Cited Findings
**MLSPred-Bench (pcdslab; bioRxiv 2024; MethodsX 2025, DOI 10.1016/j.mex.2025.103574)** [FULL via PMC]
- Converts TUSZ (675 subjects, about 4,000 seizures, about 10,000 h) into 12 ML-ready benchmarks, >150 GB in total. SPH ∈ {2, 5, 15, 30} min × SOP ∈ {1, 2, 5} min. — [PMC12423417](https://pmc.ncbi.nlm.nih.gov/articles/PMC12423417/); [bioRxiv](https://www.biorxiv.org/content/10.1101/2024.07.17.604006v1.full); [GitHub](https://github.com/pcdslab/MLSPred-Bench)
- Patient-independent split following the TUSZ partitions. Train: 208 subjects with seizures (579 total). Validation: 45 with seizures (53 total). Test: 34 with seizures (43 total). — [PMC12423417](https://pmc.ncbi.nlm.nih.gov/articles/PMC12423417/)
- Preictal is defined as [t_start − SOP − SPH, t_start − SOP], cut into 5 s non-overlapping segments at 256 Hz. A seizure is included only if the gap since the previous seizure is ≥ SPH+SOP. — [PMC12423417](https://pmc.ncbi.nlm.nih.gov/articles/PMC12423417/)
- Models tested: 6 classical ML, 3 ensembles, and CNN, CNN-LSTM and ResNet. ResNet was best, with up to 88.73% validation accuracy. Benchmark 11 (SPH 30 / SOP 2): AUC 80.5%, accuracy 64.98%, sensitivity 70.32%, specificity 59.63%. There is no alarm-level false prediction rate per hour, so the metrics are segment-level. — [PMC12423417](https://pmc.ncbi.nlm.nih.gov/articles/PMC12423417/)

**Koutsouvelis, Chybowski, Gonzalez-Sulser, Abdullateef, Escudero, "Preictal period optimization for deep learning-based epileptic seizure prediction", J Neural Eng 2024 (10.1088/1741-2552/ad9ad0)** [ABS]
- CNN-Transformer, **subject-specific**, leave-one-seizure-out on 19 pediatric CHB-MIT patients. Preictal lengths of 60/45/30/15 min were tested. — [IOPscience](https://iopscience.iop.org/article/10.1088/1741-2552/ad9ad0)
- Predictions came on average **76.8 ± 36.8 min before onset**. Sensitivity 99.31 ± 1.20%, balanced accuracy 97.32 ± 3.76%. **FPR is 33.6 per hour (segment-wise)**, which is far from clinically usable alarm rates. They introduce the CIOPR metric, which combines prediction time, output stability and interictal-to-preictal transition time. — [IOPscience](https://iopscience.iop.org/article/10.1088/1741-2552/ad9ad0)

**Other CHB-MIT prediction reference points** [SNIP]
- TGCNN (Transformer-guided CNN): sensitivity 91.5%, FPR 0.145/h on CHB-MIT. — [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0263224122011447)
- Multidimensional transformer + RNN: 22 patients, 88 merged seizures, sensitivity 76.4%, FPR 0.09/h. — [PMC11451120](https://pmc.ncbi.nlm.nih.gov/articles/PMC11451120/)

**Evaluation pitfalls**
- Random, segment-level splits put autocorrelated EEG from the same subject or seizure into both train and test, which inflates results. Segment-based CHB-MIT studies report much higher sensitivity (around 91.88%) than cross-subject event-based ones. — [Ali et al., R Soc Open Sci 2024](https://royalsocietypublishing.org/doi/10.1098/rsos.230601); [PMC11286169](https://pmc.ncbi.nlm.nih.gov/articles/PMC11286169/)
- A systematic review of neonatal EEG detection models documents widespread data leakage and weak validation that inflate reported performance. — [BioData Mining 2025](https://link.springer.com/article/10.1186/s13040-025-00516-y)
- Other pitfalls visible in the cited work:
  - Segment-level FPR (33.6/h) in place of alarm-level false prediction rate.
  - Patient-specific leave-one-seizure-out, which is not deployable cold-start.
  - Choosing the preictal length after the fact.
  - Averaging per patient over only 19 of the 24 CHB-MIT subjects.
  - [IOPscience](https://iopscience.iop.org/article/10.1088/1741-2552/ad9ad0); [PMC12423417](https://pmc.ncbi.nlm.nih.gov/articles/PMC12423417/)

### Inferences
- For short-horizon prediction on TUSZ, MLSPred-Bench SPH 2-5 min / SOP 1-2 min is the natural patient-independent baseline. Reporting alarm-level sensitivity, false prediction rate per hour, and time-in-warning would already exceed the benchmark's own reporting.
- A "76.8 min horizon" should not be treated as a baseline to beat under cross-patient TUSZ protocols. It is a different task setting.

### Gaps
- The clinically-relevant-windows systematic review (PMC13318060) was blocked by a CAPTCHA, so its SPH/SOP statistics were not retrieved.
- I found no TUSZ prediction paper that reports alarm-level FPR/h with an SPH ≤5 min.

## Q4. The 2025 Seizure Detection Challenge (AIEPILEPSY-NEURO 2025 / epilepsybenchmarks / SzCORE)

### Takeaway
The challenge was organized by EPFL ESL (Jonathan Dan et al.) at the AIEPILEPSY-NEURO 2025 conference and sponsored by Ceribell. It received 30 algorithms from 19 teams, trained on public data (TUSZ etc.) and tested on a private Dianalund dataset of 65 subjects and 4,360 h. The winner, SeizureTransformer, reached event F1 32%, sensitivity 37%, precision 29% at about 1 FP/day under the SzCORE event scoring.

### Cited Findings
- Challenge page: Seizure Detection Challenge (2025), AIEPILEPSY-NEURO 2025. It ran December 2024 to February 2025 (the page itself says "February 2024", an evident typo). Test data was the private Dianalund scalp EEG. Metrics were F1, sensitivity, precision and FP/day, both event-based and sample-based. — [epilepsybenchmarks.com/challenge](https://epilepsybenchmarks.com/challenge/)
- Challenge paper: "Quantifying the Generalization Gap in Seizure Detection: A Large-Scale Empirical Benchmark via the SzCORE Challenge" (Dan, Shahbazinia, Kechris, Atienza; arXiv 2505.18191, v2 May 2026). Test set: 65 subjects, 4,360 h, recordings of 18-98 h each, median age 34 (5-66), eight children, annotated by three board-certified neurophysiologists. 28 algorithms were successfully evaluated. — [arXiv 2505.18191](https://arxiv.org/abs/2505.18191) [FULL, from PDF]
- Event-based leaderboard (F1 / Sens / Prec / FP/day) [FULL]:
  - SeizureTransformer 32/37/29/1
  - Van Gogh Detector 30/39/25/3
  - DeepSOZ-HEM 30/58/21/14
  - S4Seizure v2 27/30/25/2
  - S4Seizure v1 27/49/19/7
  - HySEIZa v1 24/60/15/13
  - S4Seizure v3 22/56/14/13
  - zhu-transformer 19/46/12/24
  - HySEIZa v2 14/72/8/29
  - eventNet 14/60/8/20
  - SeizUnet 11/16/9/4
  - EEGWaveNet 2/92/1/237
  - The text states the top result as F1 32%, sensitivity 37%, precision 29% at **1.34 FP/day**.
  - [arXiv 2505.18191](https://arxiv.org/abs/2505.18191)
- **Conflict:** the SeizureTransformer paper gives its challenge event F1 as 0.43 and lists other teams as Van Gogh 0.36, S4Seizure 0.34 and DeepSOZ-HEM 0.31. The organizers' paper gives 0.32 / 0.30 / 0.27 / 0.30. The likely cause is a different aggregation (organizers average per subject) or a preliminary leaderboard. The organizers' paper should be treated as authoritative. — [arXiv HTML v3](https://arxiv.org/html/2504.00336v3) vs [arXiv 2505.18191](https://arxiv.org/abs/2505.18191)
- The challenge did not score latency. — [arXiv 2505.18191](https://arxiv.org/abs/2505.18191) (the latency term is absent from the scoring section)

### Inferences
- Even the best models trained on TUSZ lose about half their event F1 when tested on a new EMU (0.67 on TUSZ vs 0.32-0.43 on Dianalund). Any "early detection" claim should be checked for cross-site robustness.

### Gaps
- Sample-based leaderboard values were not extracted.

## Q5. Latency-aware metrics (SzCORE event scoring, latency definitions, early-detection scores)

### Takeaway
SzCORE/timescoring event scoring is the de facto standard, but it is latency-blind. It has a 30 s pre-ictal and 60 s post-ictal tolerance, counts any overlap, merges events closer than 90 s, and splits events longer than 5 min. Latency definitions are paper-specific. Older NEDC metrics (OVLP, TAES) weight overlap duration but also do not directly score earliness.

### Cited Findings
- SzCORE (Dan et al., arXiv 2402.13005, Epilepsia 2024) standardizes datasets, formats, cross-validation and metrics. Metric parameters are defined in the timescoring library. — [arXiv 2402.13005](https://arxiv.org/abs/2402.13005) [ABS]
- timescoring defaults: toleranceStart 30 s, toleranceEnd 60 s, minOverlap 0, maxEventDuration 300 s, minDurationBetweenEvents 90 s. Outputs are sensitivity, precision, F1 and FP/24h. There is no latency output. — [GitHub esl-epfl/timescoring](https://github.com/esl-epfl/timescoring)
- In the challenge, scores are computed per subject by summing TP/FP/FN over recordings, then taking the arithmetic mean across subjects. — [arXiv 2505.18191](https://arxiv.org/abs/2505.18191)
- NEDC scoring (OVLP, TAES, etc.) was used for TUSZ and the Neureka 2020 challenge, with a TAES-based weighted score. — [NEDC PDF](https://isip.piconepress.com/conferences/ieee_spmb/2021/papers/l01_02.pdf)
- Onset-latency definition, per Xu et al.: the time from expert EEG onset to the moment the accumulated probability crosses threshold, measured from the end of the analysis window. Sensitivity is split into detections "during crossing period" vs after onset. — [arXiv HTML](https://arxiv.org/html/2301.03465)
- The CIOPR metric (J Neural Eng 2024) combines prediction time, output stability, transition time and error rates for prediction systems. — [IOPscience](https://iopscience.iop.org/article/10.1088/1741-2552/ad9ad0)
- CaMBrain reports onset-probability metrics (mean and peak probability at or near onset) as a proxy for early detection. — [arXiv 2605.28792](https://arxiv.org/abs/2605.28792)

### Inferences
- A latency-aware protocol for TUSZ could keep SzCORE event scoring for comparability and add:
  - per-event onset latency (median and IQR, with detections inside the pre-ictal tolerance counted as negative latency);
  - a sensitivity-at-≤X-s curve (for example X = 5/10/20 s);
  - FP/24h at matched operating points.
- The "end-of-window vs start-of-window" convention changes latency by up to one window length, so it must be stated explicitly.

### Gaps
- I found no published standardized "early detection score" (such as a latency-weighted F1) adopted by SzCORE or NEDC.

## Q6. Per-seizure-type detection latency on TUSZ?

### Takeaway
I found no paper reporting per-seizure-type *latency* on TUSZ. Per-type *sensitivity* shows focal seizures are much harder to detect than generalized ones.

### Cited Findings
- Reported TUSZ detection sensitivity is 23.02-37.61% for focal seizures vs 59.50-81.10% for generalized seizures across authors (via a TUSZ multi-type review/meta-analysis snippet). — [ScienceDirect review, ESWA 2023](https://www.sciencedirect.com/science/article/pii/S0957417423015427); [PMC10525492](https://pmc.ncbi.nlm.nih.gov/articles/PMC10525492/) [SNIP]
- Attention-based deep CNN for generalized vs focal *classification* on TUSZ v1.5.2: 92.1% weighted accuracy, 90.2% F1. This is not latency. — [Epilepsy & Behavior 2024](https://www.sciencedirect.com/science/article/abs/pii/S1525505024001136) [SNIP]
- REST reports seizure-type classification weighted F1 of 0.60 on TUSZ, but no per-type latency. — [arXiv HTML](https://arxiv.org/html/2406.16906)

### Inferences
- Per-type onset latency on TUSZ appears to be open ground. Focal-onset seizures (FNSZ, CPSZ) likely produce the longest delays, given their low sensitivity and spatially restricted onset. Short seizures (<90 s) are a known failure mode (per the unverified snippet). Stratifying latency by type (FNSZ/GNSZ/CPSZ/ABSZ/TNSZ/TCSZ) and by duration is a novel contribution a student can make.

### Gaps
- I could not verify whether the Sci Rep 2026 CatBoost paper includes per-type or per-duration breakdowns (full text inaccessible).
