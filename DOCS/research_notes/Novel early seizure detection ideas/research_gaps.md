# Research Gaps and Emerging Directions in EEG Seizure Detection (TUSZ-feasible student projects, 2022-2026)

Note on method: ~22 search/fetch calls. Some items were only verified from search snippets or abstracts (flagged). Crowded vs. open status is my judgement from what the searches turned up. It is not a systematic review. Background benchmark context:
- SzCORE 2025 challenge: 30 algorithms from 19 teams, tested on a private Dianalund dataset (65 subjects, 4,360 h of continuous EEG). The best event-based F1 was 43% (sensitivity 37%, precision 45%). Algorithms often had >90% sensitivity but precision of only 10-40%, so false positives remain the central unsolved problem — [SzCORE challenge report, arXiv 2505.18191](https://arxiv.org/pdf/2505.18191); [HF paper page](https://huggingface.co/papers/2505.18191); [challenge site](https://epilepsybenchmarks.com/challenge/)
- A 2026 TUSZ "AI assurance and benchmarking framework" defines detection latency as the time from annotated onset to the first overlapping predicted interval. It found short seizures much harder: 30-90 s events had sensitivity 0.333 (4/12) vs 0.767 (214/279) for >90 s events — [Sci Rep 2026](https://www.nature.com/articles/s41598-026-41358-w)

## 1. Seizure-type-aware detection and per-type onset latency; seizure-type classification on TUSZ

### Takeaway
Seizure-type *classification* on TUSZ is crowded. Most papers report inflated seizure-wise splits, and patient-wise weighted F1 stays around 0.56-0.75. *Per-type detection latency* is under-reported: no paper found reports streaming onset latency broken down by FNSZ/GNSZ/CPSZ/ABSZ/TNSZ/TCSZ. This looks like a genuinely open, cheap, TUSZ-native gap.

### Cited Findings
- TUSZ v1.5.2 has 8 seizure types (FNSZ, GNSZ, SPSZ, CPSZ, ABSZ, TNSZ, TCSZ, MYSZ), >504 h, 5,612 recordings and 3,050 annotated seizures — [Frontiers Comput Neurosci 2024 (iterative gated GCN)](https://www.frontiersin.org/journals/computational-neuroscience/articles/10.3389/fncom.2024.1454529/full)
- IBM (Roy et al.) benchmark classified 7 types: weighted F1 up to 0.901 with a seizure-wise split vs **0.561 with a patient-wise split**. SeizureNet reached 0.95 seizure-wise vs **0.62 patient-wise** — [review, Expert Syst Appl 2023](https://www.sciencedirect.com/science/article/pii/S0957417423015427); [IBM repo](https://github.com/IBM/seizure-type-classification-tuh); [SeizureNet](https://dl.acm.org/doi/10.1007/978-3-030-66843-3_8)
- Tang et al., ICLR 2022 (self-supervised DCRNN graph model): 0.875 AUROC for detection and **0.749 weighted F1** for seizure classification. It "precisely localizes 25.4% focal seizures", 21.9 points better than CNNs — [arXiv 2104.08336](https://arxiv.org/abs/2104.08336)
- Other 2022-2024 TUSZ type classifiers: MP-SeizNet (CNN-BiLSTM) — [arXiv 2211.04628](https://arxiv.org/pdf/2211.04628); wavelet multi-class — [arXiv 2203.00511](https://arxiv.org/pdf/2203.00511); GGN gated graph (TUSZ 1.5.2) — [GitHub ICLab4DL/GGN](https://github.com/ICLab4DL/GGN); attention CNN for generalized vs focal — [Epilepsy Behav 2024](https://www.sciencedirect.com/science/article/abs/pii/S1525505024001136)
- Low-latency real-time TUSZ detection work exists (Temple group, transfer learning), but it reports aggregate latency, not per-type latency — [arXiv 2202.07796](https://arxiv.org/pdf/2202.07796); probabilistic latency reduction — [arXiv 2301.03465](https://arxiv.org/pdf/2301.03465)
- A simulated behind-the-ear 4-channel TUSZ study reports per-type sensitivity (generalized 87.62% for CNN-Merged), which shows that per-type breakdowns are informative — [arXiv 2606.11970](https://arxiv.org/html/2606.11970)

### Inferences
- **CROWDED:** clip-level seizure-type classification (especially seizure-wise splits and reported 90-99% accuracies).
- **OPEN (high novelty, high feasibility):**
  - A per-type streaming benchmark: onset latency, detection rate within 5/10/20 s, and FP/24 h per type. Focal types (FNSZ/CPSZ) are probably slow and subtle; GNSZ/ABSZ/TCSZ are probably fast.
  - "Type-conditional" or hierarchical detectors (focal vs generalized first, then type) that are optimised for latency rather than F1.
  - Type-aware early classification (type prediction within the first N seconds).
- **Feasibility:** very high. Use the TUSZ v2.0.x official splits and reproduce DCRNN or a CNN-LSTM baseline on one GPU. ABSZ/TNSZ/TCSZ have few patients, so report confidence intervals and patient-level bootstraps.

### Gaps
- I did not find the Ahmedt-Aristizabal TUSZ seizure-type numbers in this session. Please verify separately. His 2019-2020 work, e.g. neural memory networks [arXiv 1912.04968](https://arxiv.org/pdf/1912.04968), predates the 2022 window.
- I found no paper that explicitly reports per-seizure-type onset latency on TUSZ (absence of evidence, not a proof).

## 2. Cross-patient generalization, domain shift, test-time adaptation (TTA), continual/personalized adaptation

### Takeaway
Unsupervised domain adaptation for cross-patient detection is moderately crowded, but almost all of it is on CHB-MIT/Siena. TTA on TUSZ, and cross-dataset TTA (TUSZ to SzCORE/Siena/SeizeIT2), look under-explored. The SzCORE results show a large out-of-distribution gap.

### Cited Findings
- A TTA method for cross-patient detection updates lightweight parameters with single-step updates at test time. It reports CHB-MIT accuracy 95.24% (sensitivity 94.69%, specificity 95.85%) and Siena accuracy 91.88% — [Int J Neural Syst 2026](https://www.worldscientific.com/doi/10.1142/S0129065726500425) (figures from a search snippet)
- UDA for cross-subject detection — [IJNS 2024 / PubMed 39136190](https://pubmed.ncbi.nlm.nih.gov/39136190/); uncertainty-guided UDA — [Applied Intelligence 2025](https://link.springer.com/article/10.1007/s10489-025-06755-0); patient-adversarial networks — [BSPC 2023](https://www.sciencedirect.com/science/article/abs/pii/S1746809423010972)
- Online seizure *prediction* with fine-tuning and TTA — [ResearchGate 2024](https://www.researchgate.net/publication/378658829_Online_Seizure_Prediction_via_Fine-Tuning_and_Test-Time_Adaptation)
- A generalization-gap benchmark (SzCORE) quantifies performance drops on unseen data — [arXiv 2505.18191](https://arxiv.org/pdf/2505.18191)
- Stress-testing EEG foundation models: a negative-control protocol shows that dataset identity confounds clinical EEG benchmarks — [arXiv 2607.24519](https://arxiv.org/html/2607.24519v1); benchmarks of foundation models (BIOT, LaBraM, CBraMod, EEGPT) on clinical tasks — [NeuroAtlas arXiv 2605.14698](https://arxiv.org/html/2605.14698v1); [CBraMod](https://arxiv.org/pdf/2412.07236)
- Tensor kernel machines for efficient transfer or personalization on SeizeIT2 — [arXiv 2512.02626](https://arxiv.org/pdf/2512.02626)

### Inferences
- **MODERATELY CROWDED:** UDA and adversarial cross-patient detection on CHB-MIT.
- **OPEN:**
  - TTA (Tent/BN-adapt style) under *continuous streaming with rare positives*. Entropy-minimisation TTA may collapse toward "background" when seizures are rare, and this failure mode appears unstudied for seizures.
  - Cross-dataset TTA with train on TUSZ, test on Siena/CHB-MIT/SeizeIT2.
  - Label-efficient personalization, for example 1-seizure fine-tuning with patient-specific adapters.
- **Feasibility:** high. BN-statistic adaptation is cheap, and TUSZ has many patients for leave-patients-out evaluation.

### Gaps
- I could not confirm whether any TTA paper uses TUSZ specifically.

## 3. Reduced-channel / wearable EEG (behind-the-ear, 2-4 channels, SeizeIT, REACT/Ceribell)

### Takeaway
There is real clinical evidence (SeizeIT2) that behind-the-ear EEG plus ECG has high sensitivity but extremely poor precision. TUSZ-simulated low-channel studies exist (a 2026 behind-the-ear montage paper) but still use segment-based metrics. Event-based, latency-aware, cross-dataset (TUSZ-simulated to real SeizeIT2) evaluation is open.

### Cited Findings
- SeizeIT2 dataset: >11,000 h of multimodal wearable data (behind-the-ear EEG, ECG, EMG, movement), 883 focal seizures, 125 patients, 5 European centers; openly released — [Sci Data 2025](https://www.nature.com/articles/s41597-025-05580-x); [arXiv 2502.01224](https://arxiv.org/pdf/2502.01224); [challenge dataset page](https://biomedepi.github.io/seizure_detection_challenge/dataset/)
- SeizeIT2 clinical validation (192 adults, 616 focal seizures): the algorithm (behind-the-ear EEG + ECG) had sensitivity 0.73 but **6.22 FP/h**, precision 0.004 and F1 0.01. With expert review, sensitivity was 0.31, precision 0.83 and F1 0.45, at about 8 min review per 24 h. Focal-to-bilateral tonic-clonic sensitivity was 0.82 — [Epilepsia Open 2026 / PMC13238671](https://pmc.ncbi.nlm.nih.gov/articles/PMC13238671/)
- Low-density behind-the-ear simulation on TUSZ v2.0.3 (P7/T7/P8/T8, 4 channels): CNN-Merged had ROC AUC 85.89% and sensitivity 81.03%. The authors say specificity is still insufficient, that segment-wise rather than event-based detection is a limitation, and that edge optimisation is future work — [arXiv 2606.11970](https://arxiv.org/html/2606.11970)
- Earlier TUSZ channel reduction showed a gradual decline in sensitivity and specificity from 22 channels down to 20, 16, 8, 4 and 2 — [arXiv 1801.02472](https://arxiv.org/pdf/1801.02472) (pre-2022); channel-annotated interpretable detection — [BSPC 2024](https://www.sciencedirect.com/science/article/pii/S1746809424015428)
- Explainable AI for reduced-montage neonatal detection — [arXiv 2406.16908](https://arxiv.org/html/2406.16908v2)

### Inferences
- **MODERATELY CROWDED:** "fewer channels, similar AUC" papers.
- **OPEN:**
  - Per-seizure-type degradation curves as channels are removed. Generalized seizures should survive; focal frontal seizures may not, which is consistent with SeizeIT2 noting that frontal seizures are harder at behind-the-ear sites.
  - Learned channel selection optimised for *latency and FP/24 h* rather than AUC.
  - Sim-to-real transfer: train on TUSZ with simulated behind-the-ear channels, test on real SeizeIT2 behind-the-ear data.
- **Feasibility:** high. TUSZ montage subsetting is trivial and SeizeIT2 is public.

### Gaps
- I did not retrieve Ceribell/REACT or Epilog performance figures in this session.

## 4. On-device / edge / TinyML / neuromorphic SNNs

### Takeaway
SNN seizure detectors with sub-mW power exist, but they are mostly on CHB-MIT or similar, with epoch-level accuracy. SNNs on TUSZ with event-based metrics and per-type latency seem rare. This is a moderately open niche, but it needs care to be credible without hardware.

### Cited Findings
- An SNN on the Xylo neuromorphic processor got 93.3% and 92.9% test accuracy (ictal vs interictal) at **87.4 µW IO + 287.9 µW compute** — [arXiv 2410.16613](https://arxiv.org/abs/2410.16613); [PubMed 39413626](https://pubmed.ncbi.nlm.nih.gov/39413626/)
- A cross-patient SNN detector — [PMC10805904](https://pmc.ncbi.nlm.nih.gov/articles/PMC10805904/); a mixed-signal neuromorphic event-driven detector — [Sci Rep 2025](https://www.nature.com/articles/s41598-025-99272-6); deep SNNs — [Neuromorph Comput Eng 2023](https://iopscience.iop.org/article/10.1088/2634-4386/acbab8); SNN review — [Neurocomputing 2024](https://www.sciencedirect.com/science/article/abs/pii/S0925231224007057)
- Wearable edge platforms: BrainFuseNet (EEG+PPG+ACC fusion, IEEE TBioCAS 2024, cited via search) and BioGAP-Ultra — [arXiv 2508.13728](https://arxiv.org/pdf/2508.13728); an edge-AI wearable — [BMC Biomed Eng 2026](https://link.springer.com/article/10.1186/s42490-026-00116-9)

### Inferences
- **MODERATELY CROWDED** on CHB-MIT; **OPEN** on TUSZ, especially an SNN or quantised model with event-based SzCORE metrics plus estimated energy per inference (SynOps/MACs).
- **Feasibility:** medium. Energy can be estimated in simulation with snnTorch or Rockpool, but claims without hardware are weaker.

### Gaps
- I did not verify any SNN paper evaluated on TUSZ.

## 5. Early-exit / anytime / streaming causal inference, SSMs (Mamba/S4), sequential detection (CUSUM/QCD)

### Takeaway
Mamba-for-EEG is becoming crowded, with many accuracy papers on CHB-MIT. Causal streaming SSMs on TUSZ have just appeared (CaMBRAIN, 2026). Combining a learned detector with quickest-change-detection theory (CUSUM on network log-likelihood ratios, with explicit delay vs false-alarm trade-offs) for scalp EEG looks **genuinely under-explored**.

### Cited Findings
- ConvMambaNet (CNN+Mamba) reports 99% accuracy on CHB-MIT — [arXiv 2601.13234](https://arxiv.org/abs/2601.13234)
- EEGMamba (bidirectional SSM with mixture of experts) covers seizure detection among 8 datasets — [arXiv 2407.20254](https://arxiv.org/html/2407.20254v2); [OpenReview](https://openreview.net/forum?id=13PclvlVBa)
- CaMBRAIN: causal SSMs for real-time continuous EEG inference, evaluated on TUSZ — [arXiv 2605.28792](https://arxiv.org/pdf/2605.28792) (**low-confidence summary**: the PDF fetch returned a generic summary, and its "sub-100 ms latency" claim is unverified)
- CG-MambaNet does cross-patient prediction with event-level evaluation — [arXiv 2606.08226](https://arxiv.org/pdf/2606.08226)
- Sequential detection: optimal-control "quickest detection" of seizures (older) — [PMC3280702](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3280702/); an extended CUSUM person-dependent iEEG detector that needs only a short normal baseline and no hyperparameter optimisation — [ESWA 2021](https://www.sciencedirect.com/science/article/abs/pii/S095741742100957X)
- Longer temporal context with transformers for clinically viable detection — [LookAroundNet arXiv 2601.06016](https://arxiv.org/pdf/2601.06016)

### Inferences
- **CROWDED:** "Mamba beats CNN on CHB-MIT accuracy."
- **OPEN:**
  - CUSUM or Shiryaev-Roberts post-processing over deep-model outputs on TUSZ. Report detection delay vs FP/24 h curves (the QCD-native metric) instead of AUROC.
  - Early-exit or anytime classifiers that stop as soon as confidence exceeds a threshold, with per-type delay.
  - A causal-vs-bidirectional latency ablation.
- **Feasibility:** very high. It is post-processing on any trained model, low compute, and has a clear theoretical framing.

### Gaps
- I did not find early-exit (multi-exit network) papers for seizure detection. This was not searched exhaustively.

## 6. Uncertainty quantification, calibration, conformal prediction

### Takeaway
Bayesian and MC-dropout calibration papers exist, and risk-controlling calibration (Learn-then-Test) exists for *prediction*. Conformal prediction for *detection alarms*, i.e. controlling FP/24 h or miss rate with finite-sample guarantees on TUSZ, including under patient shift, looks **genuinely open**. The only CP detection paper found is from 2018 and uses hand-crafted features.

### Cited Findings
- Conformal prediction for EEG seizure detection (tree-bagging CP, DWT/FFT features) bounds the false-negative frequency — [PMLR v91, Eliades et al. 2018](http://proceedings.mlr.press/v91/eliades18a.html)
- Learn-then-Test risk-controlling calibration for seizure *prediction*: rigorous control of false alarm rate and an average 92% reduction in false alarms — [PMC10543660](https://pmc.ncbi.nlm.nih.gov/articles/PMC10543660/)
- Bayesian deep learning with noisy labels (annotation ambiguity) for detection — [arXiv 2410.19815](https://arxiv.org/pdf/2410.19815); [PMC12107695](https://pmc.ncbi.nlm.nih.gov/articles/PMC12107695/)
- An integrated calibration and uncertainty framework (ECE plus MC dropout) for seizure detection — [PubMed 42308713](https://pubmed.ncbi.nlm.nih.gov/42308713/); uncertainty estimation and calibration — [ResearchGate](https://www.researchgate.net/publication/387163463_Uncertainty_Estimation_and_Model_Calibration_in_EEG_Signal_Classification_for_Epileptic_Seizures_Detection)
- Review of uncertainty quantification in biosignals — [arXiv 2312.09454](https://arxiv.org/pdf/2312.09454)

### Inferences
- **OPEN (strong candidate):**
  - Conformal or risk-controlled *event-level* alarms on TUSZ: guarantee FP/24 h ≤ k, or sensitivity ≥ 1-α, then report the latency cost.
  - Patient-conditional or Mondrian CP per seizure type.
  - CP under patient shift, using weighted CP.
- Combining this with directions 1 and 5 (per-type latency plus a CUSUM alarm with a conformal threshold) gives a coherent, novel student thesis.
- **Feasibility:** very high. It is post-hoc, needs no retraining, and is CPU-friendly.

### Gaps
- I did not find a 2022-2026 paper applying conformal prediction to TUSZ detection alarms. This should be double-checked on Google Scholar.

## 7. Explainability (XAI), clinician trust, onset-zone / lateralization localization

### Takeaway
Post-hoc XAI (Grad-CAM, LRP, attention) is crowded. *Quantitative* localization and lateralization from scalp EEG on TUSZ is weakly benchmarked: TUSZ lacks onset-zone labels, and Tang et al. localized only 25.4% of focal seizures precisely.

### Cited Findings
- Tang et al. 2022 localized 25.4% of focal seizures precisely — [arXiv 2104.08336](https://arxiv.org/abs/2104.08336)
- SZTrack tracks seizures and localizes onset zones from scalp EEG, with lateralization accuracy up to 0.826 — [PLOS One 2022](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0264537)
- ML lateralization and localization of seizure onset in focal cortical dysplasia from ictal scalp EEG — [Frontiers Neurosci 2026](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2026.1915535/full)
- A systematic review of interpretable AI for seizure EEG — [PMC11907617](https://pmc.ncbi.nlm.nih.gov/articles/PMC11907617); an explainable hybrid DNN with localization — [BSPC 2024](https://www.sciencedirect.com/science/article/abs/pii/S174680942400380X)

### Inferences
- **CROWDED:** saliency maps as a paper add-on.
- **OPEN:**
  - Faithfulness evaluation of XAI (deletion/insertion tests) for seizure models.
  - Weakly supervised lateralization on TUSZ using channel-level annotations. TUSZ v2 has some channel-based annotation files; verify this.
- **Feasibility:** medium. Clinician-trust studies need clinicians, which is hard for a student.

### Gaps
- I did not confirm TUSZ v2 channel-level annotation availability in this session.

## 8. Multimodal early warning (ECG/HR, accelerometry, video)

### Takeaway
This is active clinically (SeizeIT2, ambulatory ECG+ACC). It is **not feasible with TUSZ alone**: TUSZ is EEG-centric, with an EKG channel in many recordings (verify), but no accelerometry or video. The cheapest TUSZ-feasible angle is EEG + the ECG lead in TUSZ recordings, e.g. testing whether ictal tachycardia gives earlier warning than EEG for certain seizure types.

### Cited Findings
- Ambulatory ECG + ACC: 78 patients, 587 seizures, 385 days, comparing HRV, ACC and combined features — [medRxiv 2025](https://www.medrxiv.org/content/10.64898/2025.12.16.25342428v1.full)
- SeizeIT2 behind-the-ear EEG + ECG: the high-sensitivity subgroup had clear ictal EEG patterns plus tachycardia (mostly temporal lobe) — [PMC13238671](https://pmc.ncbi.nlm.nih.gov/articles/PMC13238671/); ECG added to 2-channel behind-the-ear EEG — [PMC10136326](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10136326/)
- Multimodal learning review and future directions — [arXiv 2601.05095](https://arxiv.org/pdf/2601.05095)

### Inferences
- **OPEN, moderately feasible:** EEG+ECG fusion on TUSZ (using the EKG channel) with per-type lead-time analysis, or on SeizeIT2, which has ECG/EMG/ACC.

### Gaps
- I did not verify the fraction of TUSZ recordings with a usable EKG channel.

## 9. LLM / agentic / retrieval-augmented EEG reporting

### Takeaway
This is very new (2025-2026) and uncrowded but fast-moving. NeuroGRIP uses retrieval-augmented knowledge graphs to refine EEG graphs on TUSZ/CHB-MIT. Feasibility for a student is medium, and evaluation rigor (hallucination, grounding) is the open problem.

### Cited Findings
- NeuroGRIP (arXiv 2607.14314, July 2026) builds a knowledge base from clinical guidelines. It projects STGNN node embeddings into knowledge-graph space, retrieves triplets through FAISS, and assigns confidence to EEG graph edges. It reports improved detection and interpretability on TUSZ and CHB-MIT — [arXiv 2607.14314](https://arxiv.org/abs/2607.14314); [code](https://github.com/LincanLi-X/NeuroGRIP)
- LLM as a clinical graph-structure refiner for EEG seizure diagnosis — [arXiv 2604.28178](https://arxiv.org/pdf/2604.28178)
- A hybrid AI system for EEG background analysis and report generation — [arXiv 2411.09874](https://arxiv.org/pdf/2411.09874); RAG EEG-to-text — [arXiv 2605.17503](https://arxiv.org/abs/2605.17503)
- Surveys of LLMs for EEG — [arXiv 2506.06353](https://arxiv.org/pdf/2506.06353); a scoping review of generative LLMs in epilepsy care — [PMC13536540](https://pmc.ncbi.nlm.nih.gov/articles/PMC13536540/); multimodal LLM seizure classification (semiology video) — [PMC12632642](https://pmc.ncbi.nlm.nih.gov/articles/PMC12632642/)

### Inferences
- **OPEN:**
  - Grounded report generation from detector outputs (type, onset time, lateralization, confidence) with hallucination audits against TUSZ annotations. TUEG includes free-text reports, which could serve as references; verify licensing and access.
- **Feasibility:** medium. It needs LLM API or local 7B inference, and robust evaluation is the hard part.

### Gaps
- I did not retrieve NeuroGRIP's numeric results. The abstract says only "improves".

## Overall ranking for a 4-6 month TUSZ project on limited compute (my inference)
1. **Most novel and most feasible:** per-seizure-type onset-latency benchmark + CUSUM/QCD alarm layer + conformal/risk-controlled FP/24 h guarantee (combining directions 1, 5 and 6). It is post-hoc on a standard backbone and uses SzCORE event metrics.
2. Behind-the-ear/2-4-channel per-type degradation, with sim-to-real transfer to SeizeIT2 (direction 3).
3. Streaming TTA under rare positives, cross-dataset (direction 2).
4. Crowded areas to avoid as a headline claim: Mamba/transformer accuracy on CHB-MIT, seizure-wise-split type classification, and generic Grad-CAM XAI.
