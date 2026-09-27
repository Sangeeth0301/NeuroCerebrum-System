# P_2025_Meng: 3D-SERESNet for patient-specific and multi-patient seizure prediction with event-level evaluation (iScience 2025)

## Citation & Link
Meng L., Zhou L., Zhang W., Xie K. "Robust epileptic seizure prediction: A 3D-SERESNet framework for patient-specific and multi-patient generalization." *iScience* 28(12):114171, December 2025. DOI: 10.1016/j.isci.2025.114171. PMID 41446734. PMCID PMC12723167.
- Open access (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC12723167/
- Full text used for this note: [Europe PMC full-text XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12723167/fullTextXML)
- Metadata and abstract: [Europe PMC API](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:41446734%20AND%20SRC:MED&resultType=core&format=json)

## Venue type
Peer-reviewed journal (Cell Press *iScience*, open access). It is included because it is a recent peer-reviewed scalp-EEG study that reports **event-level sensitivity, FPR/h and AUC in a "patient-independent" setting**. That setting is **not** evaluation on unseen patients; see the evaluation protocol below.

## Problem
Segment-level accuracy has little clinical value. The paper proposes a 3D time-frequency-space CNN with focal loss and **event-based** alarm evaluation. It tests the model both patient-specifically and in a single multi-patient ("patient-independent") model. [Europe PMC full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12723167/fullTextXML)

## Dataset
All details from the [Europe PMC full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12723167/fullTextXML).
- **CHB-MIT, 13 patients** (chb01, 02, 03, 05, 09, 10, 13, 14, 18, 19, 20, 21, 23). This follows the Truong 2018 selection.
- **18 bipolar channels** common to all patients.
- **Labels:**
  - preictal = 30 min before onset;
  - postictal = 5 min after the seizure;
  - interictal = at least 4 h from any seizure;
  - seizures less than 30 min apart are merged.
- **Class ratio:** preictal-to-interictal ratio per patient is 0.06–0.83. For example, chb19 has 1.5 h preictal vs 24.9 h interictal.
- **Preprocessing:** 60 Hz notch filter and non-overlapping **10-s segments**. STFT maps (129 × 79 per channel) are stacked across channels into a 3D input of 129 × 79 × 18.

## Approach
- **Model:** a 3D conv stem, three **SE (squeeze-and-excitation) residual blocks** for channel attention, and a classifier.
- **Focal loss:** α is set to the training-set preictal ratio, computed on training data only.
- **Two data regimes:**
  - "imbalanced", using all non-overlapping data;
  - "balanced", with preictal oversampled by a 5-s-overlap sliding window and interictal randomly undersampled, applied to the training set.
- **Alarm post-processing:** a k-of-n rule (8 of 10 windows) plus a **30-min refractory period**.
- **Optimizer:** AdamW (learning rate 0.003) with cosine warm restarts, 100 epochs.

  [Europe PMC full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12723167/fullTextXML)

## Evaluation protocol
All details from the [Europe PMC full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12723167/fullTextXML).
- **Conventional SPH = 5 min and SOP = 30 min**, the same as Truong 2018. An alarm is correct if onset falls after the SPH and inside the SOP.
- **Metrics:** event sensitivity, FPR/h, segment AUC, and a per-patient p-value against an **unspecific random predictor**, P = 1 − e^(−FPR·SOP) with a binomial test.
- **Patient-specific:** leave-one-seizure-out, with the **last 20% (in time) of training data** used as validation.
- **"Patient-independent":**
  - 7 rounds are run. In each round, one seizure per patient is held out, and the **remaining seizures of all patients (including the test patient's other seizures)** are pooled for training and validation.
  - **So the test patient is seen in training.** This is multi-patient leave-one-seizure-out, **not LOPO**, and it leaks patient identity. The authors explicitly contrast it with domain adaptation, which *adapts* to target patients.
- **Other leakage risks:**
  - Leave-one-seizure-out uses future seizures in training.
  - The authors say they "deliberately avoid hyperparameter tuning on the validation set" in the patient-independent setting.
  - They note that other studies tuned on the test set, a risk that does not apply here.

## Key results (numbers)
From Tables 2–6 and 9 of the [Europe PMC full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12723167/fullTextXML). Values are CHB-MIT means over 13 patients, with SPH 5 / SOP 30.

| Setting | Sensitivity | FPR (/h) | AUC |
|---|---|---|---|
| Patient-specific, imbalanced | 87.82% | 0.148 | 0.882 |
| Patient-specific, balanced | **90.77%** | **0.090** | 0.923 |
| "Patient-independent" (multi-patient), imbalanced | 81.21% | 0.353 | 0.847 |
| "Patient-independent" (multi-patient), balanced | **84.41%** | **0.232** | 0.866 |

- **Chance test:** in the multi-patient setting, chb02 (p = 0.189) and chb14 (p = 0.598 imbalanced, 0.258 balanced) are **not better than chance**. chb14 has FPR 0.906/h in every setting.
- **Baselines** (patient-specific, imbalanced), sensitivity / FPR / AUC:
  - 3D-CNN: 82.05% / 0.643 / 0.711;
  - 3D-ResNet: 70.72% / 0.592 / 0.716;
  - 3D-SERESNet: 87.82% / 0.148 / 0.882.
- **The paper's Table 9 summarizes cross-patient domain-adaptation work on CHB-MIT** (secondary source; numbers not checked against the originals), as sensitivity / FPR / AUC:
  - Liang et al. (supervised DA, SPH/SOP 5/30): 79.0% / 0.265 / 0.812;
  - Liang et al. (semi-supervised DA): 83.2% / 0.251 / 0.830;
  - Peng et al.: 82.0% / 0.13 / 0.84 and 73.0% / 0.25 / 0.75;
  - Zhao et al. (source-free unsupervised DA): 70.5% / 0.381 / 0.683;
  - Wu et al.: 94.8% / 0.10, flagged by Meng as leakage-prone because it shuffled data in 5-fold CV.
- **Warning time is not reported** beyond the 5–35 min window implied by SPH/SOP.

## Limitations
- The "patient-independent" results include the test patient's other seizures in training, so they **overstate generalization to new patients**.
- 13 selected CHB-MIT patients, a single dataset, and leave-one-seizure-out.
- The balanced regime oversamples preictal data only in training; the test data remains natural.
- No lead-time distribution is reported.

## Relevance to our project
- A good **peer-reviewed template for event-level scoring**: SPH 5 / SOP 30, k-of-n 8/10, a 30-min refractory period, and a per-patient Poisson/binomial chance test. We should adopt the same scoring on TUSZ, with a shorter SOP if sessions are short.
- A cautionary example of **terminology inflation**: "patient-independent" here means one pooled model, not unseen patients. Its 84.4% / 0.23 per h should not be compared with true LOPO numbers (CG-MambaNet; Jemal) or with TUSZ patient-disjoint numbers.
- Its Table 9 is a handy index of supervised and semi-supervised DA cross-patient papers (Liang, Peng, Zhao). These report about 70–83% sensitivity at 0.13–0.38 per h. Most of those methods (the "SDA" ones) use **labelled** target-patient seizures, which is not possible for new TUSZ patients. Zhao's source-free method uses only unlabelled target data.
