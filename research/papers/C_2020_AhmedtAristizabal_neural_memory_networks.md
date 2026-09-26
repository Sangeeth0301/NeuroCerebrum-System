# Ahmedt-Aristizabal et al. 2020 — Neural Memory Networks for Seizure Type Classification

## Citation & Link
- David Ahmedt-Aristizabal, Tharindu Fernando, Simon Denman, Lars Petersson, Matthew J. Aburn, Clinton Fookes. "Neural Memory Networks for Seizure Type Classification." *2020 42nd Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC)*, pp. 569–575. DOI: 10.1109/EMBC44109.2020.9175641 — https://doi.org/10.1109/embc44109.2020.9175641 ; PubMed 33018053: https://pubmed.ncbi.nlm.nih.gov/33018053/
- Open access preprint: https://arxiv.org/abs/1912.04968 (PDF https://arxiv.org/pdf/1912.04968)

## Venue type
Peer-reviewed conference (IEEE EMBC 2020). Numbers below were read from the arXiv full text.

## Problem
Cross-patient seizure-type classification; standard CNN/RNN models do not capture long-range relationships across seizures and patients, so the authors add an external memory with trainable neural plasticity. — https://arxiv.org/pdf/1912.04968

## Dataset
- TUSZ **v1.4.0**, 250 Hz, 2,012 seizures, 8 types; **myoclonic excluded** (3 events). 7 classes kept as-is (no merging), although the authors note SPSZ/CPSZ are subclasses of FNSZ and ABSZ/TNSZ/TCSZ subclasses of GNSZ. — https://arxiv.org/pdf/1912.04968
- Uses **IBM TUSZ pre-processed data (v1.0.0, method #1)**: 20 TCP-montage channel pairs, FFT on 1-s windows, 24 frequency bands, 0.75-s overlap → each sample = 1 s of EEG, shape [#samples, 20 channels, 24 bands]. — https://arxiv.org/pdf/1912.04968
- Table I (seizures / patients / 1-s samples): FNSZ 992/108/292,725; GNSZ 415/44/137,033; SPSZ 44/2/6,028; CPSZ 342/34/132,200; ABSZ 99/12/3,087; TNSZ 67/2/4,888; TCSZ 50/11/22,524. — https://arxiv.org/pdf/1912.04968
- Rare classes: no special handling (no resampling/merging described in the fetched text).

## Approach
- Encoder: 2 stacked LSTMs (inside a shallow RCNN) produce hidden states per time step.
- **Plastic Neural Memory Network (NMN)**: memory stack M (l = 25 slots), input controller forms query, attention over slots, output controller, update controller writes back; controllers combine fixed weights and Hebbian-style **plastic** components (plasticity learning rate η = 0.5); hidden size k = 80. Output → dense softmax over 7 classes.
- Trained 50 epochs, Adam, categorical cross-entropy. — https://arxiv.org/pdf/1912.04968
- No graph and no localization.

## Evaluation protocol
- 5-fold CV; **in each fold, the data samples of each seizure type are randomly split 60/20/20** train/val/test. — https://arxiv.org/pdf/1912.04968
- **Leakage flag: SEVERE.** Splitting is at the level of 1-s windows (with 75% overlap), so overlapping windows from the *same seizure* and the same patient appear in train and test. Despite the paper's "cross-patient" wording, this is not patient-independent. Tang et al. 2022 compare against it only as a reported number and themselves use patient-wise splits — https://arxiv.org/pdf/2104.08336
- Metric: weighted F1.

## Key results (numbers)
From Table II, https://arxiv.org/pdf/1912.04968

| Method | wF1 |
|---|---|
| AdaBoost / SGD / XGBoost / k-NN (Roy 2019) | 0.509 / 0.649 / 0.782 / 0.884 |
| CNN ResNet50 (Roy 2019) | 0.723 |
| CNN AlexNet [14] | 0.802 |
| SeizureNet | 0.900 |
| Adapted CNNs / LSTMs / CNN-LSTMs | 0.675–0.901 |
| Shallow CNN-LSTM (this work) | 0.824 |
| **Plastic NMN (this work)** | **0.945** |

- Per-class: only a normalized confusion matrix (Fig. 2) — hardest classes are those with few recordings (SPSZ, ABSZ, TNSZ, TCSZ); numeric per-class F1 not given in text.
- When re-implemented as a CNN-LSTM baseline under Tang et al.'s patient-wise TUSZ v1.5.2 protocol, wF1 was only 0.633 (12-s) / 0.641 (60-s) — https://arxiv.org/pdf/2104.08336

## Limitations
- Window-level random split → inflated results; 0.945 is not a patient-generalization estimate.
- 1-s windows: classifies type from 1 s of EEG, no temporal context of seizure evolution.
- 2-patient classes (SPSZ, TNSZ) effectively memorized.
- No interpretability beyond PCA of embeddings.

## Relevance to our project
- Cautionary example: huge gap between window-wise (0.945) and patient-wise (~0.63 for a similar CNN-LSTM) evaluation — we must split by patient and report it explicitly.
- Memory module idea (storing prototypes of seizure types across patients) could help rare types, analogous to prototype/few-shot approaches.
- Its CNN-LSTM is a standard baseline for our type-at-onset classifier.
