# P_2024_Koutsouvelis: Preictal period optimization for deep learning-based epileptic seizure prediction (J Neural Eng 2024)

## Citation & Link
Koutsouvelis P., Chybowski B., Gonzalez-Sulser A., Abdullateef S., Escudero J. "Preictal period optimization for deep learning-based epileptic seizure prediction." *Journal of Neural Engineering* 21(6), 2024 (published December 2024). DOI: 10.1088/1741-2552/ad9ad0. PMID 39637549.
- Journal page: https://iopscience.iop.org/article/10.1088/1741-2552/ad9ad0
- Open preprint (arXiv 2407.14876): https://arxiv.org/abs/2407.14876 (HTML: https://arxiv.org/html/2407.14876)
- University of Edinburgh repository record: https://www.research.ed.ac.uk/en/publications/preictal-period-optimization-for-deep-learning-based-epileptic-se/
- Metadata source: [Europe PMC API](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1088/1741-2552/ad9ad0&resultType=core&format=json)

## Venue type
Peer-reviewed journal (IOP *Journal of Neural Engineering*). The journal version is not open access. **All details below are from the arXiv HTML preprint**, which may differ slightly from the final version.

## Problem
The preictal period length is usually fixed arbitrarily (for example 30 or 60 min), but the true preictal state varies across patients and seizures. The paper proposes a **data-driven way to choose the optimal preictal period (OPP) per patient**. It also introduces a new metric, **CIOPR (Continuous Input-Output Performance Ratio)**, that assesses how a classifier behaves on continuous EEG leading up to a seizure. [arXiv HTML](https://arxiv.org/html/2407.14876)

## Dataset
All details from the [arXiv HTML](https://arxiv.org/html/2407.14876).
- **CHB-MIT scalp EEG**: 19 pediatric cases. chb08, chb12, chb13, chb15 and chb24 are excluded; chb01 and chb21 are treated as one case each. Recordings have 23 channels at 256 Hz.
- **Interictal definition:** the paper states data "up to 4 hours before and 1 hour after each annotated seizure" were handled specially. Read literally the wording is ambiguous; the intent appears to be that interictal data is at least 4 h before and at least 1 h after any seizure.
- **Preictal:** at most 60 min before onset. Data within 1 h after a previous seizure is excluded. Seizures with less than 1 min of preictal data are excluded, and each case needs at least 2 eligible seizures.
- **Preictal lengths tested:** 15, 30, 45 and 60 min.
- **No SPH** (preictal runs right up to onset).

## Approach
All details from the [arXiv HTML](https://arxiv.org/html/2407.14876).
- **Preprocessing:** 0.5–45 Hz FIR band-pass, common average reference, 5-s non-overlapping epochs of raw EEG.
- **Model (CNN-Transformer):** 3 conv layers (32/64/128 filters) extract spatio-temporal features, followed by 2 multi-head self-attention layers and a classifier.
- **Balancing:** preictal data is oversampled 3× by 66% overlap, and interictal data is subsampled to match.
- **Training:** 90/10 train/validation split, up to 100 epochs, early stopping.
- **CIOPR metric**, computed on the classifier's continuous output over many hours before each seizure:
  - Outputs are smoothed with an 8-min averaging window.
  - A 4-parameter logistic (sigmoid) curve is fitted to the output.
  - From the fit the paper derives:
    - **Transition Period (TP):** the 5th–95th percentile of the sigmoid;
    - **Negative Duration (ND):** the interictal-labelled stretch;
    - **Seizure Prediction Convergence (SPC):** the time before onset when the output reaches 99% of its maximum;
    - error rates in the SPC and ND regions.
  - CIOPR combines these so that the best classifier has an early SPC, low errors and a short TP.
- **OPP selection:** the preictal length with the best CIOPR. Where CIOPR is unavailable, the best F1 is used instead.
- **Statistics:** Friedman ANOVA with Bonferroni correction across preictal definitions.

## Evaluation protocol
- **Patient-specific leave-one-seizure-out CV.** [arXiv HTML](https://arxiv.org/html/2407.14876)
- Metrics are **segment-level** (5-s epochs): sensitivity, specificity, accuracy, F1 and AUC.
- **The false alarm rate (FAR) is also computed per 5-s segment** (the "EPOCH" method), **not per alarm event**. [arXiv HTML](https://arxiv.org/html/2407.14876)
- There is no SOP/SPH alarm-based evaluation and no surrogate or random-predictor test.
- **The authors flag leakage themselves:** leave-one-seizure-out lets the model train on seizures that occur after the test seizure, which may inflate performance. [arXiv HTML §IV-E](https://arxiv.org/html/2407.14876)

## Key results (numbers)
Results use each patient's OPP, from Table III of the [arXiv HTML](https://arxiv.org/html/2407.14876).

| Metric | Mean ± SD over 19 cases |
|---|---|
| Sensitivity | **99.31% ± 1.20** |
| Specificity | **95.34% ± 6.38** |
| Accuracy | 97.32% ± 3.76 |
| F1 | 97.46% ± 3.41 |
| AUC | **99.35% ± 1.61** |
| **FAR (segment-level)** | **33.6 ± 46.0 per hour** (range 1.06/h for chb01 to 190/h for chb06) |
| **SPC ("prediction time")** | **76.8 ± 36.8 min before onset** |

- **Where the "76.8 min" comes from.** It is the mean SPC: the point where the *smoothed* classifier output converges to its maximum. It is **not** a clinically validated alarm warning time.
  - It was computed only on the seizures and patients where CIOPR could be fitted; SPC is N/A for 6 of the 19 cases.
  - Values range from about 50 to 175.5 min (chb04). Elsewhere the text gives single-seizure values of 16.7–217.5 min.
  - The mean SPC exceeds the 60-min maximum preictal label because the smoothed output rises before the labelled preictal window starts.

  [arXiv HTML](https://arxiv.org/html/2407.14876)
- OPP was **60 min for most patients**. A few patients had 45, 30 or 15 min (chb20 = 15 min). Longer preictal definitions gave earlier predictions and lower errors, and 60 vs 15 min differed significantly on 8 of 11 metrics. [arXiv HTML](https://arxiv.org/html/2407.14876); [Europe PMC abstract](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1088/1741-2552/ad9ad0&resultType=core&format=json)
- The abstract headline numbers are 99.31% sensitivity, 95.34% specificity, 99.35% AUC, 97.46% F1 and 76.8 min. [arXiv abs](https://arxiv.org/abs/2407.14876)

## Limitations
- Patient-specific leave-one-seizure-out with temporal leakage, as the authors acknowledge.
- Segment-level metrics only. The segment-level FAR of **33.6/h is clinically unusable** as an alarm rate and is not comparable to event-level FPR/h values such as Truong's 0.16/h.
- Single dataset (CHB-MIT, pediatric) with no cross-patient test.
- The OPP is chosen using test-seizure behaviour (CIOPR), which is a potential selection bias.
- SPC is undefined for several patients.

## Relevance to our project
- This is the paper behind the **"76.8 min" early-warning claim**. Our project should present it carefully: the 76.8 min is an **output-convergence time** on smoothed segment outputs, obtained under leave-one-seizure-out with a 33.6/h segment-level FAR. It is **not** an event-level warning time with a controlled false-alarm rate.
- **Ideas worth reusing on TUSZ:**
  - treat preictal length as a hyperparameter per patient or cohort;
  - characterise the continuous output trajectory with a sigmoid fit to estimate when the "preictal drift" begins.
- Tuning the preictal length must happen on **validation data only**.
- **TUSZ constraint:** most TUSZ sessions are too short to contain 60+ min of clean pre-seizure EEG. SPC-style curves spanning 600 min, as in their Figure 2, are not feasible on most TUSZ records.
