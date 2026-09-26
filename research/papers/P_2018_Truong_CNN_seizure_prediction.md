# P_2018_Truong: Convolutional neural networks for seizure prediction using intracranial and scalp EEG (Neural Networks 2018)

## Citation & Link
Truong N.D., Nguyen A.D., Kuhlmann L., Bonyadi M.R., Yang J., Ippolito S., Kavehei O. "Convolutional neural networks for seizure prediction using intracranial and scalp electroencephalogram." *Neural Networks* 105:104–111, 2018. DOI: 10.1016/j.neunet.2018.04.018. PMID 29793128.
- DOI: https://doi.org/10.1016/j.neunet.2018.04.018
- PubMed: https://pubmed.ncbi.nlm.nih.gov/29793128/
- Open preprint (arXiv 1707.01976, titled "A Generalised Seizure Prediction with Convolutional Neural Networks for Intracranial and Scalp Electroencephalogram Data Analysis"): https://arxiv.org/abs/1707.01976 (PDF: https://arxiv.org/pdf/1707.01976)
- Metadata and published abstract were checked through Europe PMC: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/j.neunet.2018.04.018&resultType=core&format=json

## Venue type
Peer-reviewed journal (Elsevier *Neural Networks*). The method details and per-patient tables below come from the **arXiv PDF (Dec 2017 draft)**. I did not read the paywalled published version, so small differences are possible.
- **Version conflict on Kaggle numbers.** The published abstract gives **75%** sensitivity on the Kaggle set ([Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/j.neunet.2018.04.018&resultType=core&format=json)), and so does the arXiv Dec-2017 text (75%, 0.21/h). The **current arXiv abstract page** gives **82.3% and 0.22/h** ([arXiv abs](https://arxiv.org/abs/1707.01976)). Cite 75% / 0.21/h for the journal paper.

## Problem
Patient-specific seizure prediction, meaning classification of preictal vs interictal EEG plus alarm generation, with **one fixed preprocessing pipeline and one CNN for every patient** (no per-patient feature engineering). The same method is tested on both iEEG and scalp EEG. [arXiv PDF](https://arxiv.org/pdf/1707.01976)

## Dataset
All details from the [arXiv PDF](https://arxiv.org/pdf/1707.01976).
- **CHB-MIT scalp EEG** (the scalp set that matters for us):
  - 23 pediatric patients, 844 h, 163 seizures, 22 electrodes, 256 Hz.
  - Seizures less than 30 min after the previous one are merged into the leading seizure.
  - Only patients with fewer than 10 seizures/day are kept.
  - Patients also need at least 3 leading seizures and 3 interictal hours.
  - Result: **13 patients, 64 seizures**.
  - Interictal = at least **4 h** before onset and after seizure end.
- **Freiburg iEEG**: 13 of 21 patients, 6 channels, 256 Hz, 59 seizures, about 311 h interictal.
- **Kaggle AES 2014 challenge iEEG** (5 dogs + 2 humans, 48 seizures, 627.7 h interictal):
  - clips are 10 min;
  - preictal clips run from 66 min to 5 min before onset;
  - interictal clips are at least 1 week from any seizure.
  - This is **not** the 2016 Melbourne/NeuroVista contest described in P_2018_Kuhlmann.

## Approach
All details from the [arXiv PDF](https://arxiv.org/pdf/1707.01976).
- **Preprocessing:** only power-line noise removal (50/60 Hz and harmonics, removed in the STFT domain). No other artifact rejection.
- **Input:** STFT of **30-s windows** (spectrogram with time × frequency × channels).
- **Class balancing:** extra preictal windows are created with a 30-s window slid at step S, where S is chosen per patient so the two classes are balanced (overlap oversampling).
- **CNN:**
  - C1 has 16 kernels of size n×5×5 (n = channels), stride 1×2×2.
  - C2 and C3 have 32 and 64 kernels of 3×3 with 2×2 max-pooling, each with BatchNorm and ReLU.
  - These feed FC-256 (sigmoid), then FC-2 (softmax), with dropout 0.5 before each FC layer.
  - The network is deliberately shallow to limit overfitting.
- **Validation trick:** the **last 25% (in time)** of the preictal and interictal training data is held out for early stopping, instead of a random 20% split. The authors argue random splits leak temporal information.
- **Post-processing:** k-of-n alarm rule. The CNN outputs one prediction per 30 s, and an alarm needs at least **8 of the last 10** windows positive.

## Evaluation protocol
All details from the [arXiv PDF](https://arxiv.org/pdf/1707.01976).
- **Patient-specific leave-one-seizure-out CV.** With N seizures, the model trains on N−1 and tests on the held-out one. Interictal data is split randomly into N parts.
- Each fold is run twice and the results averaged.
- **SOP = 30 min and SPH = 5 min** for all metrics. An alarm is correct if onset falls after the SPH and inside the SOP; an alarm with no seizure in its SOP is a false alarm.
- **Chance test:** the worst-case p-value per patient is compared with an unspecific random (Poisson) predictor, where P = 1 − exp(−FPR·SOP) and a binomial test is applied over K seizures.
- **Leakage risks:**
  - Leave-one-seizure-out lets the model train on seizures that come **after** the test seizure.
  - Interictal parts are randomly partitioned, not chronologically.
  - Patient inclusion was filtered (13/23 CHB-MIT patients).

## Key results (numbers)
All numbers are with SOP 30 min / SPH 5 min, from the [arXiv PDF](https://arxiv.org/pdf/1707.01976). The headline sensitivities also appear in the [published abstract](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/j.neunet.2018.04.018&resultType=core&format=json).

| Dataset | Sensitivity | FPR (/h) | Chance test |
|---|---|---|---|
| Freiburg iEEG (13 pts, 59 sz) | **81.4%** (48/59) | **0.06** | Better than random for all patients except Pat14 |
| **CHB-MIT scalp (13 pts, 64 sz)** | **81.2%** | **0.16** | Better than random for all patients except Pat9 (p = 0.067) |
| Kaggle 2014 iEEG (5 dogs + 2 pts, 48 sz) | 75% | 0.21 | Better than random for 4/5 dogs and Pat1 |

- CHB-MIT per-patient sensitivity ranges from about 33% to 100%, and FPR from 0 to about 0.4/h. The PDF table is garbled, so these values could not be matched exactly to patient IDs.
- **AUC and warning time are not reported.**

## Limitations
- Patient-specific only, and the evaluation uses leave-one-seizure-out. It is neither chronological nor pseudo-prospective.
- On CHB-MIT, only 13 selected pediatric patients were used. There is no cross-patient generalization.
- 30-min SOP / 5-min SPH is a lenient target. The paper gives no time-in-warning or per-alarm warning-time distribution.
- The version discrepancy on Kaggle numbers (75% vs 82.3%) means cite the journal version.

## Relevance to our project
- **Canonical baseline recipe:** 30-s STFT, then a shallow CNN, then an 8-of-10 k-of-n alarm, evaluated with SOP/SPH and a random-predictor p-value. It is cheap to reimplement on TUSZ bipolar montages.
- Its CHB-MIT pipeline shows the preprocessing decisions we must make on TUSZ: merge clustered seizures into "lead" seizures, keep interictal data at least 4 h from seizures, and hold out the last 25% of training data in time for validation.
- **TUSZ caveat:** TUSZ sessions are mostly short and not continuous day-long recordings. The 4-h interictal buffer and 35-min preictal-plus-SPH window will remove most TUSZ seizures (see P_2025_Mohammad_MLSPred-Bench). We will likely need shorter SPH/SOP, or to report it as a limitation.
