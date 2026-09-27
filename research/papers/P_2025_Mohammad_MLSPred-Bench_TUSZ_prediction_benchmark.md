# P_2025_Mohammad: MLSPred-Bench, turning TUSZ into ML-ready seizure-prediction benchmarks (MethodsX 2025)

## Citation & Link
Mohammad U., Saeed F. "MLSPred-bench: Transforming electroencephalography (EEG) datasets into machine learning-ready epileptic seizure prediction benchmarks." *MethodsX* 15:103574, 2025 (published online 22 Aug 2025). DOI: 10.1016/j.mex.2025.103574. PMID 40949826. PMCID PMC12423417. Licence CC BY-NC.
- Affiliations: Florida International University (Saeed, corresponding author) and Union College (Mohammad).
- Open-access full text (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC12423417/
- Full text used for this note: [Europe PMC full-text XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12423417/fullTextXML)
- Publisher page: https://www.sciencedirect.com/science/article/pii/S2215016125004182
- PubMed: https://pubmed.ncbi.nlm.nih.gov/40949826/
- Earlier preprint: bioRxiv 2024.07.17.604006, titled "MLSPred-Bench: ML-Ready Benchmark Leveraging Seizure Detection EEG data for Predictive Models" — https://www.biorxiv.org/content/10.1101/2024.07.17.604006v1
- Code: https://github.com/pcdslab/MLSPred-Bench. Project page: https://pcdslab.github.io/projects/MLSPred-Bench
- Conflict of interest: Saeed founded AI-NeoTech LLC, a start-up that builds ML tools for epilepsy. [Europe PMC full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12423417/fullTextXML)

## Venue type
Peer-reviewed methods journal (Elsevier *MethodsX*). It is a **data-wrangling / benchmark method paper, not a model paper**. The ML/DL results are a "technical validation" only. Everything below comes from the MethodsX full text unless marked otherwise.

## Problem
Public EEG corpora annotate only seizure onset and offset (for detection). Prediction needs preictal and interictal labels. The paper builds a tool that turns detection-annotated EEG into ML-ready prediction data and applies it to TUSZ. The authors argue that TUSZ is large and diverse but "not ML-ready", and that this explains why few prediction models use it. Most deep prediction work uses the smaller CHB-MIT set (23 subjects). [Europe PMC full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12423417/fullTextXML)

## Dataset
All details from the [MethodsX full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12423417/fullTextXML).
- **TUSZ.** The paper describes it as 675 subjects, 1,645 sessions, 7,377 EDF files, more than 4,000 seizures and about 10,000 h.
- **TUSZ version not stated.** The subject split is 579 train / 53 validation / 43 test. These counts look like TUSZ v2.0.x (our inference, not stated in the paper).
- **Subjects used:**
  - 388 seizure-free subjects (570 sessions) are excluded.
  - 287 subjects with at least one seizure are kept: 1,175 sessions, 528 of them with seizures.
  - Sessions with seizures supply the preictal samples. The 547 seizure-free sessions of these subjects are mainly used for interictal samples.
- **Split: the official TUSZ subject-level split, so subjects are disjoint.**
  - Subjects with seizures: 208 train / 45 validation / 34 test.
  - Sessions with seizures: 352 / 113 / 63.
  - The paper calls this "patient-independent", single-fold.
- **Channels:**
  - 17 electrodes common to the AR1, AR3, LE2 and LE4 reference types give a **20-channel bipolar (TCP-like) montage**: FP1-F7, F7-T3, T3-T5, T5-O1, FP2-F8, F8-T4, T4-T6, T6-O2, T3-C3, C3-CZ, CZ-C4, C4-T4, FP1-F3, F3-C3, C3-P3, P3-O1, FP2-F4, F4-C4, C4-P4, P4-O2.
  - Everything is resampled to 256 Hz with crude methods: zero-padding 250 Hz segments, decimating 512 Hz, and pick-and-pad for 400 and 1000 Hz.
- **Sessions are treated as continuous**, meaning the EDF records within a session are concatenated. Different sessions of the same subject are treated as discontinuous.

### SPH / SOP definitions (**note: the naming is swapped relative to the usual convention**)
- In MLSPred-Bench, **"SPH" = the length of the preictal window** ("the period during which a seizure must be predicted"). **"SOP" = the gap** between the end of that window and onset ("the duration by which we want to guarantee prediction").
- Preictal samples are taken from [T_start − SOP − SPH, T_start − SOP].
- In the convention used by Truong 2018, Meng 2025 and most of the literature, these roles are reversed: SPH is the gap or intervention time, and SOP is the window in which the seizure must occur. When comparing, **MLSPred "SPH 30 / SOP 5" ≈ conventional "SOP 30 / SPH 5"**. The authors acknowledge that the terms "may be used interchangeably in the literature". [Europe PMC full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12423417/fullTextXML)
- **12 benchmarks** combine SPH ∈ {2, 5, 15, 30} min with SOP ∈ {1, 2, 5} min. BM1 = SPH 2 / SOP 1, and so on up to BM12 = SPH 30 / SOP 5. BM11 = SPH 30 / SOP 2.
- **Seizure inclusion:**
  - A seizure enters benchmark b only if the time from the previous seizure's **end** to its onset is at least SPH_b + SOP_b.
  - An interictal stretch equal in length to the preictal window must also be extractable.
- **Seizure counts:** only BM1 is given in the text: **1,282 seizures (687 train / 416 validation / 179 test)**. Other benchmarks appear in Fig. 4 only, and counts fall as SPH + SOP grows.
  - The bioRxiv preprint appears to give a per-benchmark table (e.g. 1,847 seizures for BM1). This was read only through an automated summary, **could not be verified, and conflicts with the MethodsX number**. Cite the MethodsX 1,282. [bioRxiv](https://www.biorxiv.org/content/10.1101/2024.07.17.604006v1)
- **Segments:** non-overlapping **5-s windows**, giving 20 × 1,280 samples per segment. Classes are balanced 1:1 per seizure. Interictal segments are **randomly sampled**. The data is not normalized or filtered, and total size is over 150 GB.
- **Interictal definition:** the MethodsX text does not state a minimum distance (e.g. 4 h) from any seizure. The interictal data come "mainly" from seizure-free sessions, but can come from non-seizure parts of seizure sessions.

## Approach
From the [MethodsX full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12423417/fullTextXML).
- **Four-stage pipeline:**
  1. per-session metadata, in a CHB-MIT-style summary format;
  2. raw-EEG concatenation and bipolar montage;
  3. seizure profiling and interim per-seizure datasets;
  4. final HDF5 + CSV train/validation/test files per benchmark.
- **Validation models:**
  - Classical: LR, SVM, NB, kNN, DT and LDA.
  - Ensembles: RF, AdaBoost and Bagging.
  - Deep: a 1D CNN with 9 conv blocks, a CNN + Bi-LSTM, and a ResNet (the authors' earlier **SPERTL** design, BHI 2022, with 4 residual blocks and kernel size 7).
  - Deep-model settings: learning rate 1e-3, dropout 0.8 (0.75 for the ResNet), at most 25 epochs, early stopping.
- **Two input types:**
  - raw 20 × 1,280 segments (flattened to 25,600 features for classical ML);
  - 1,420 handcrafted features (71 per channel): mean and variance, 64 band mean-amplitude-spectrum features and ratios, and 5 db5 wavelet energies.

## Evaluation protocol
- **Segment-level (5-s) metrics** on the **validation (TUSZ dev) set**: ROC-AUC, accuracy, sensitivity and specificity. Table 2 is explicitly titled "Validation ROC-AUC scores". The paper does **not report held-out test-set (eval) numbers**, and it has **no event-level alarm metrics** (no event sensitivity, FPR/h or warning time). [Europe PMC full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12423417/fullTextXML)
- Continuous evaluation is shown only qualitatively (Fig. 6): the ResNet's output and firing power on one validation session ("vld_tgc_s002_ar1"). Models trained on BM1, BM2, BM6 and BM9 alert correctly on it. BM11 gives excessive alerts, and BM4 and BM5 give none.
- **Leakage and bias risks:**
  - Subject-disjoint split: good, with no cross-patient leakage.
  - Random interictal sampling with no stated distance from seizures means interictal segments may sit close to seizures (label noise).
  - Preictal windows can start right after the previous seizure ends, since only SPH + SOP of gap is required. They may therefore contain postictal EEG, a confound that makes preictal easier to separate.
  - Balancing per seizure (1:1) is not a realistic class prior.
  - The ML/DL models were tuned and early-stopped on the same validation set that is reported.

## Key results (numbers)
All values are **segment-level validation metrics**, from Tables 2–3 of the [MethodsX full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12423417/fullTextXML).

**Average validation AUC over the 12 benchmarks (Table 3):**

| Model | Raw EEG: AUC / Acc / Spec / Sens | Handcrafted features: AUC / Acc / Spec / Sens |
|---|---|---|
| **ResNet (SPERTL)** | **70.91% / 64.98% / 59.63% / 70.32%** | 70.23% / 64.56% / 55.06% / 74.06% |
| RF | 66.98% / 61.86% / 46.70% / 77.02% | **74.76% / 68.50% / 61.81% / 75.19%** |
| CNN | 67.48% / 59.26% / 55.93% / 62.59% | 69.06% / 62.85% / 55.82% / 69.87% |
| CNN-LSTM | 67.69% / 64.28% / 45.38% / 83.18% | 67.45% / 62.23% / 68.92% / 55.54% |
| LR | 52.15% / 52.03% / 43.59% / 60.47% | 70.29% / 65.90% / 59.43% / 72.36% |
| AdaBoost | 63.34% / 57.79% / 28.78% / 86.79% | 71.66% / 64.33% / 42.98% / 85.68% |

**Per-benchmark validation AUC, selected models (Table 2):**

| Benchmark (SPH/SOP in the paper's naming) | ResNet raw | RF raw | RF features |
|---|---|---|---|
| BM1 (2/1) | 66.8% | 72.7% | 73.0% |
| BM3 (2/5) | 69.4% | 73.7% | 73.4% |
| BM7 (15/1) | 81.1% | 52.9% | 77.6% |
| BM8 (15/2) | **83.6%** | 52.2% | 80.1% |
| BM9 (15/5) | 79.2% | 59.5% | 80.1% |
| BM10 (30/1) | 56.4% | 70.1% | 63.3% |
| BM11 (30/2) | 80.5% | **88.4%** | **88.3%** |
| BM12 (30/5) | 50.8% | 68.4% | 63.9% |

- The raw ResNet reaches 81–84% AUC on the 15-min-preictal benchmarks BM7–BM9. Almost every model scores 80–89% on BM11. BM10 and BM12 largely fail, and "even the best models" fail on BM12.
- The highlights claim "up-to 88.73% validation accuracy". This figure does not appear in the tables; it probably relates to a BM11 AUC. **Treat it as unverified.**
- **Internal inconsistencies to flag:**
  - In raw-data Table 2, the "CNN" row equals the AdaBoost row and the "LSTM" row equals the Bagging row, which looks like a copy error. The Table 2 average for the CNN (63.3%) also disagrees with the Table 3 average (67.48%).
  - The text gives CNN-LSTM raw AUC as 68.31%, but Table 3 gives 67.69%.
  - The ResNet raw average AUC is 69.9% in Table 2 but 70.91% in Table 3.
  - The text says ResNet is "the only technique" above 70% AUC on raw data.
  - The text attributes 64.80% specificity and 66.81% accuracy to AdaBoost-features, but the table places them on the Bagging row.
- **Overfitting:** training AUC is high (near 1 for deep models) with a large train–validation gap, especially for SPH 2 min and SPH 30 min.
- **Cost:** feature extraction takes about 12.5 s per 5-s segment (not real-time). Deep-model inference is in the millisecond range per segment.

## Limitations
- Stated by the authors: single fold only, with no cross-validation; no imbalance handling or scaling; fixed 5-s segments and fixed SPH/SOP grid; no filtering or artifact removal in the benchmark; overfitting. [Europe PMC full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12423417/fullTextXML)
- Our additional concerns:
  - validation-only, segment-level results with no event-level sensitivity, FPR/h or test-set numbers;
  - swapped SPH/SOP naming;
  - no interictal distance buffer;
  - possible postictal contamination of preictal windows;
  - crude resampling (zero-padding at segment edges);
  - table errors;
  - the preprint and journal seizure counts conflict.
- The longest preictal window is 30 min plus a 5-min gap. The benchmark cannot test **"earlier than 35 min" forecasting** because TUSZ sessions are short.

## Relevance to our project
- **This is the only published TUSZ-based prediction benchmark we found, and it is our direct baseline.** "Earlier than prior work on TUSZ" can be framed as beating MLSPred-Bench's validation AUC at larger total lead time (SPH + SOP in their naming), and reporting **test-set, event-level** metrics that they do not provide.
- Baselines to beat (segment-level, validation):
  - about 0.71 average AUC for the raw ResNet;
  - 0.75 for RF on handcrafted features;
  - at a 15-min preictal window: 0.81–0.84 (raw ResNet) and 0.78–0.80 (RF on features);
  - at 30 min / 2 min: 0.88 (RF), a strong result but unstable across benchmarks.
- **Reuse:**
  - their GitHub pipeline for session concatenation, the 20-channel TCP montage and seizure eligibility (the gap from the previous seizure's end must be at least the lead time);
  - the official patient-disjoint TUSZ split.
- **Fix:**
  - convert to the conventional SPH/SOP naming;
  - add an interictal buffer and exclude postictal time from preictal windows;
  - report on TUSZ eval (test);
  - add event-level alarms (k-of-n or firing power) with FPR/h and warning time;
  - add a random/Poisson-predictor chance test.
- Seizure counts shrink as lead time grows (1,282 seizures at a 3-min total horizon, fewer at 35 min). This is the core **data-availability trade-off** for any "earlier warning" claim on TUSZ, so report n seizures per horizon.
- Follow-up work from the same group reportedly uses these benchmarks with transformers, ViTs and LLMs: Parani et al., IEEE BigData 2024, DOI 10.1109/BigData62323.2024.10825319; and CDMA 2025, DOI 10.1109/CDMA61895.2025.00028. These are cited in the reference list of the [MethodsX paper](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12423417/fullTextXML). **Their results were not reviewed here.**
