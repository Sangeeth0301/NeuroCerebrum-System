# P_2024_Jemal: Domain adaptation for EEG-based, cross-subject epileptic seizure prediction (Front. Neuroinform. 2024)

## Citation & Link
Jemal I., Abou-Abbas L., Henni K., Mitiche A., Mezghani N. "Domain adaptation for EEG-based, cross-subject epileptic seizure prediction." *Frontiers in Neuroinformatics* 18:1303380, 2024 (published 19 Feb 2024). DOI: 10.3389/fninf.2024.1303380. PMID 38371495. PMCID PMC10869477. Licence CC BY.
- Affiliations: INRS Centre EMT, Université TÉLUQ and CHUM research centre, all in Montréal.
- Open access (PMC): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10869477/
- Full text used for this note: [Europe PMC full-text XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10869477/fullTextXML)
- Repository copy: https://r-libre.teluq.ca/3209/

## Venue type
Peer-reviewed journal (*Frontiers in Neuroinformatics*, Original Research; editor and three named reviewers listed). The numbers below come from the full text.

## Problem
Patient-specific predictors do not transfer to new patients. The paper compares three settings: **multiple-subject** (one model; pooled train/test from the same patients), **cross-subject** (leave-one-patient-out, LOPO) and **cross-subject with unsupervised domain adaptation**. The adaptation uses *unlabelled* data from the target patient. [Europe PMC full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10869477/fullTextXML)

## Dataset
All details from the [Europe PMC full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10869477/fullTextXML).
- **CHB-MIT**: 23 subjects (22 appear in the LOPO table; chb12 is absent), 940 h, 198 seizures, 256 Hz. Recordings with fewer than 23 electrodes are dropped.
- **Siena**: 14 subjects, 128 h, 47 seizures, 29 channels, 512 Hz. 12 subjects appear in the LOPO table.
- **Labels:**
  - **Preictal = 1 h before onset.** No SPH (gap) and no SOP are defined.
  - The postictal period is removed.
  - **No interictal distance buffer is stated.**
- **Segments:** non-overlapping 10-s windows, with random under-sampling of the majority class and per-channel z-scoring.
  - CHB-MIT gives 77,529 interictal and 89,783 preictal samples.
  - Siena gives 197,805 interictal and 80,845 preictal samples.
- **Preprocessing:** 50 Hz notch filter and 0.5–70 Hz band-pass (MNE-Python).

## Approach
- The network is the authors' earlier **interpretable 3-layer CNN**, similar to EEGNet and FBCSP (Jemal et al. 2022):
  - temporal 2D conv with (1,128) kernels, which learns frequency filters;
  - depth-wise spatial conv with (C,1) kernels;
  - a 2D conv of (1,64);
  - average pooling, dropout, then dense softmax.

  [Europe PMC full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10869477/fullTextXML)
- **Domain adaptation (feature-based, adversarial):** DANN, CDAN and CDAN+E (CDAN with entropy conditioning). Labelled source data come from N−1 patients, plus **unlabelled target-patient data**.
- **Training:** Adam, learning rate 0.005, up to 500 epochs, early stopping with patience 20 on a hold-out validation set. PyTorch.

## Evaluation protocol
- **Multiple-subject:** a pooled train/validation/test split over all patients' segments. This is the same leakage-prone setting as Dissanayake 2022.
- **Cross-subject: LOPO**, training on N−1 patients and testing on the held-out patient.
- **Cross-subject + DA:** LOPO, but the adversarial alignment sees **unlabelled segments of the test patient during training** (transductive). This is not leakage of labels, but the model is not a fixed off-the-shelf predictor for a new patient.
- **Metrics are segment-level only:** F1, accuracy and AUC per held-out patient. No event-level alarms, no sensitivity/FPR per hour, no warning time and no chance test. The authors state that patient-level sensitivity and specificity were out of scope.
- **Leakage and bias risks:**
  - Random under-sampling can give balanced test sets, which inflates accuracy relative to the real class prior.
  - With no interictal buffer, interictal segments may lie close to seizures.

## Key results (numbers)
All from the [Europe PMC full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10869477/fullTextXML) (Tables 3–8). Values are mean ± SD across held-out patients.

| Setting | CHB-MIT | Siena |
|---|---|---|
| Multiple-subject (pooled split): Acc / Sens / Spec | 97.36% / 98.31% / 96.97% | 96.01% / 97.24% / 94.57% (AUC 0.96) |
| **Cross-subject LOPO, no DA: F1 / Acc / AUC** | **55.34% / 63.5% / 0.69 ± 0.17** | **39.81% / 48.69% / 0.48 ± 0.09** |
| LOPO + DANN: F1 / Acc / AUC | 64.52% / 68.59% / 0.73 ± 0.16 | 56.72% / 52.18% / 0.53 ± 0.08 |
| LOPO + CDAN: F1 / Acc / AUC | 65.64% / 68.72% / 0.74 ± 0.14 | **59.77% / 60.27% / 0.61 ± 0.09** |
| LOPO + CDAN+E: F1 / Acc / AUC | **66.45% / 70.90% / 0.75 ± 0.17** | 51.91% / 51.79% / 0.52 ± 0.10 |

- **Per-patient spread under LOPO without DA (CHB-MIT):** AUC ranges from 0.29 (chb01) to 0.96 (chb11). Other patients include chb13 at 0.92 and chb22 at 0.91; chb20 has AUC 0.63 but an F1 of only 6.5%.
- The **~35-point accuracy drop** from pooled (97%) to LOPO (63%) on the same data and network is the key message.
- **Note on the abstract:** it says domain adaptation improved accuracy "by 10.30% and 7.4%" for CHB-MIT and Siena. The body instead reports +7.40% accuracy for CHB-MIT with CDAN+E and +11.58% for Siena with CDAN. The dataset attribution looks swapped. Cite the table values.

## Limitations
- Stated by the authors: under-sampling; small datasets; no extensive statistics; demographic bias of the datasets; patient-level sensitivity and specificity not assessed. [Europe PMC full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10869477/fullTextXML)
- Our additional concerns:
  - no SPH, so the "preictal" class runs right up to onset;
  - no interictal buffer;
  - segment-level metrics only;
  - DA needs target-patient data before deployment;
  - different DA methods win on each dataset, with no single best method.

## Relevance to our project
- This is the **cleanest peer-reviewed demonstration of the pooled-vs-LOPO gap** in scalp-EEG prediction. The same model scores 97% pooled and 63% (AUC 0.69) on unseen patients. It supports our use of the patient-disjoint TUSZ split, and it warns us not to compare our numbers with pooled-split papers (Dissanayake 2022; the multi-patient mode of Meng 2025).
- A realistic **cross-patient segment-AUC baseline** on CHB-MIT is about 0.69 (no DA) to 0.75 (with DA). On Siena it is about 0.48–0.61. This is consistent with MLSPred-Bench's about 0.67–0.75 on TUSZ validation.
- **Idea for TUSZ:** unsupervised DA (DANN/CDAN) against unlabelled EEG of the eval patient, for example the early part of a session, is a cheap add-on. Its transductive nature must be reported.
