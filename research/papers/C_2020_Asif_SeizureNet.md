# Asif, Roy et al. 2020 — SeizureNet (with companion: Roy et al. 2019 "Setting the benchmark")

## Citation & Link
- **Main paper**: Umar Asif, Subhrajit Roy, Jianbin Tang, Stefan Harrer (IBM Research Australia). "SeizureNet: Multi-Spectral Deep Feature Learning for Seizure Type Classification." In *Machine Learning in Clinical Neuroimaging and Radiogenomics in Neuro-oncology* (MLCN / RNO-AI workshops @ MICCAI 2020), Springer LNCS, pp. 77–87, 2020. DOI: 10.1007/978-3-030-66843-3_8 — https://dl.acm.org/doi/10.1007/978-3-030-66843-3_8 ; Semantic Scholar: https://www.semanticscholar.org/paper/SeizureNet:-Multi-Spectral-Deep-Feature-Learning-Asif-Roy/15b8ba09bd4193cec0c17e9d669267d58ed5afc4
- Open access preprint (6 versions, v1 Mar 2019 → v6 Sep 2020): https://arxiv.org/abs/1903.03232
- **Companion benchmark** (preprint, not peer-reviewed): Subhrajit Roy, Umar Asif, Jianbin Tang, Stefan Harrer. "Machine Learning for Seizure Type Classification: Setting the Benchmark." arXiv:1902.01012, 2019 — https://arxiv.org/abs/1902.01012
- Preprocessing code / "IBM TUSZ pre-processed data": https://github.com/IBM/seizure-type-classification-tuh

## Venue type
SeizureNet: peer-reviewed MICCAI 2020 **workshop** paper (Springer LNCS). The Roy et al. 2019 benchmark is an **arXiv preprint only** (Semantic Scholar lists venue as arXiv.org) — https://api.semanticscholar.org/graph/v1/paper/arXiv:1902.01012

## Problem
Cross-patient multi-class seizure type classification from scalp EEG in TUSZ; the benchmark paper was the "first study" of ML for multi-class seizure type classification on TUSZ. — https://arxiv.org/abs/1902.01012

## Dataset
- TUSZ **v1.4.0 and v1.5.2** (per Semantic Scholar/arXiv summary of SeizureNet) — https://www.semanticscholar.org/paper/SeizureNet:-Multi-Spectral-Deep-Feature-Learning-Asif-Roy/15b8ba09bd4193cec0c17e9d669267d58ed5afc4
- 7 seizure types (myoclonic excluded, owing to 3 events) using the IBM preprocessing: FFT on 1-s windows, 24 frequency bands, 0.75-s overlap, 20 TCP-montage channels; this is the same preprocessed data used by Ahmedt-Aristizabal et al. 2020, whose Table I lists per-type counts from TUSZ v1.4.0: FNSZ 992 seizures/108 patients, GNSZ 415/44, SPSZ 44/2, CPSZ 342/34, ABSZ 99/12, TNSZ 67/2, TCSZ 50/11 — https://arxiv.org/pdf/1912.04968
- Rare types: not merged; SPSZ and TNSZ come from only 2 patients each, which makes patient-wise evaluation almost impossible for those classes (inference from counts above).

## Approach
- SeizureNet: ensemble of deep CNN sub-networks learning **multi-spectral feature embeddings** (inputs at different spectral resolutions); knowledge distillation of the ensemble embeddings into smaller networks for low-memory deployment. — https://arxiv.org/abs/1903.03232
- Roy 2019 benchmark: grid search over preprocessing (FFT, etc.) × classical ML (k-NN, SGD, XGBoost, AdaBoost) × CNN (ResNet50) and hyperparameters. — https://arxiv.org/abs/1902.01012
- No graph construction; no localization.

## Evaluation protocol
- Benchmark and early SeizureNet versions: headline numbers come from **seizure-wise cross-validation** (seizures, not patients, split into folds) → the same patient appears in train and test. This is inferred from the later version's explicit "seizure-wise" label on its 0.95 result and from Tang et al.'s framing; the benchmark's fold details were not read in full text (unverified). **Leakage flag: HIGH** for the headline numbers (0.907, 0.98).
- Later SeizureNet version reports both **seizure-wise** and **patient-wise** CV: wF1 up to 0.95 seizure-wise vs **0.62 patient-wise** (search-summary of the arXiv abstract) — https://www.semanticscholar.org/paper/SeizureNet:-Multi-Spectral-Deep-Feature-Learning-Asif-Roy/15b8ba09bd4193cec0c17e9d669267d58ed5afc4 . The patient-wise 0.62 (7-class, 3-fold patient-wise) is independently confirmed as the SeizureNet comparison number in Tang et al. 2022 Table 3 — https://arxiv.org/pdf/2104.08336

## Key results (numbers)
- Roy et al. 2019 benchmark: weighted F1 **up to 0.907** (seizure-wise) — abstract only — https://arxiv.org/abs/1902.01012
- Baseline wF1 numbers from the benchmark as re-tabulated by Ahmedt-Aristizabal et al. (Table II): AdaBoost 0.509, SGD 0.649, XGBoost 0.782, k-NN 0.884, CNN (ResNet50) 0.723 — https://arxiv.org/pdf/1912.04968 (note: the 0.907 abstract figure vs 0.884 k-NN here likely reflect different configurations/versions — not resolved)
- SeizureNet: wF1 **0.98** (arXiv abstract, latest version) — https://arxiv.org/abs/1903.03232 ; **0.900** as cited by Ahmedt-Aristizabal et al. 2020 Table II — https://arxiv.org/pdf/1912.04968 ; **0.95 seizure-wise / 0.62 patient-wise** in another version — https://www.semanticscholar.org/paper/SeizureNet:-Multi-Spectral-Deep-Feature-Learning-Asif-Roy/15b8ba09bd4193cec0c17e9d669267d58ed5afc4 . The conflicting numbers across arXiv versions are **not reconciled**; the published LNCS text was not accessed.
- Per-class F1: not retrieved (gap).

## Limitations
- Seizure-wise CV inflates performance; the ~0.33 gap (0.95 → 0.62) between seizure-wise and patient-wise CV is the clearest quantification of leakage on TUSZ type classification.
- 1-s FFT windows from the IBM preprocessing: windows from the same seizure are highly correlated.
- SP/CP distinction not EEG-resolvable (see Tang et al. 2022) yet kept as separate classes.
- Workshop paper; multiple inconsistent preprint versions.

## Relevance to our project
- Defines the standard TUSZ preprocessing pipeline and the "IBM TUSZ" data many later papers use — useful for comparability, but we must evaluate **patient-wise** and report the 0.62 patient-wise number as the realistic SeizureNet baseline.
- Multi-spectral ensemble idea is compatible with a GNN node-feature design (multi-resolution FFT features per electrode).
- Knowledge distillation is relevant if our type-at-onset model must run in real time.
