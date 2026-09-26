# D_2023_Xu: Shorter latency of real-time epileptic seizure detection via probabilistic prediction (ESWA 2023/2024)

## Citation & Link
Xu Y., Yang J., Ming W., Wang S., Sawan M. "Shorter latency of real-time epileptic seizure detection via probabilistic prediction." Expert Systems with Applications, 2024 (ScienceDirect PII S0957417423018614).
- Journal page: https://www.sciencedirect.com/science/article/abs/pii/S0957417423018614
- Open preprint: https://arxiv.org/abs/2301.03465 (HTML: https://arxiv.org/html/2301.03465)
- Repository copy: https://publications.polymtl.ca/74111/
- Notes:
  - The first author is **Yankun Xu**, not "Wu". The task brief's "Wu, Yang et al." refers to this paper.
  - The DOI is probably 10.1016/j.eswa.2023.121112, inferred from the PII and not verified.
  - The ESWA volume was not verified.

## Venue type
Peer-reviewed journal (Elsevier ESWA). The numbers below come from the arXiv v2 preprint.

## Problem
Seizure detectors reach high sensitivity but detect late. The authors reframe detection as **probabilistic prediction** so that alarms fire sooner after EEG onset. [arXiv](https://arxiv.org/html/2301.03465)

## Dataset
- **Not TUSZ.** The paper uses **CHB-MIT** (scalp EEG; 19 patients, 99 seizures) and **SWEC-ETHZ** (intracranial EEG; 11 patients, 89 seizures). [arXiv](https://arxiv.org/html/2301.03465)
- Validation is **patient-specific** leave-one-seizure-out cross-validation, not patient-independent. [arXiv](https://arxiv.org/html/2301.03465)

## Approach
- **Crossing period**: the samples whose windows span EEG onset, i.e. those ending between onset and one window length after onset. These samples get **soft labels** instead of hard 0/1 labels. [arXiv](https://arxiv.org/html/2301.03465); [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0957417423018614)
- Features and model:
  - multiscale STFT features fed to a 3D-CNN that outputs a probability;
  - a rectified weighting strategy;
  - an **accumulative decision rule**, which raises an alarm when accumulated probability crosses a threshold.

  [ScienceDirect abstract](https://www.sciencedirect.com/science/article/abs/pii/S0957417423018614)
- Window length is 5 s for CHB-MIT and 10 s for SWEC-ETHZ. [arXiv](https://arxiv.org/html/2301.03465)

## Evaluation protocol
Latency is the time between the detection time t_d and the expert EEG onset. The paper also reports sensitivity during the crossing period, sensitivity after onset, and the false detection rate per hour (FDR/h). [arXiv](https://arxiv.org/html/2301.03465)

## Key results (numbers)

| Dataset | Detected during crossing period | Detected after onset | Latency | FDR |
|---|---|---|---|---|
| CHB-MIT | 94/99 | 100% | **2.3 ± 0.7 s** | 0.08 ± 0.14/h (about 1.9/24h) |
| SWEC-ETHZ | 84/89 | not captured | **4.7 ± 2.0 s** | 0.08 ± 0.09/h |

- The authors report latency "at least 50% shorter than previous studies".

Sources: [arXiv](https://arxiv.org/html/2301.03465); [ScienceDirect abstract](https://www.sciencedirect.com/science/article/abs/pii/S0957417423018614)

## Limitations
- It is patient-specific. The models are trained on seizures from the same patient, which is much easier than TUSZ's patient-independent setting.
- It uses small, clean datasets and no TUSZ.
- The latency numbers are **not comparable** with TUSZ patient-independent latencies of about 8-15 s (Lee 2022).

## Relevance to our project
- This is the key **method idea for earlier detection**: soft labels over the onset-crossing period plus accumulative evidence alarms. It transfers directly to TUSZ.
- A novel contribution could be applying it to TUSZ v2.0.x in the patient-independent setting and reporting latency with SzCORE metrics.
