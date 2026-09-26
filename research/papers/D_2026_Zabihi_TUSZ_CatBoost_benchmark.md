# D_2026_Zabihi: Transparent AI assurance and benchmarking framework on TUSZ with a gradient-boosting ensemble (Scientific Reports 2026)

## Citation & Link
Zabihi M., Gilmore E.J., Ding K., Rosenthal E.S. "A transparent AI assurance and benchmarking framework for EEG seizure detection on TUSZ seeded with a reproducible gradient-boosting ensemble." Scientific Reports 16:11283, 2026 (published 27 February 2026). DOI: 10.1038/s41598-026-41358-w
- Publisher: https://www.nature.com/articles/s41598-026-41358-w
- Open access (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC13049040/
- Code: https://github.com/Mzabihi/A-Transparent-AI-Assurance-and-Benchmarking-Framework-for-EEG-Seizure-Detection-on-TUSZ

## Venue type
Peer-reviewed journal (Nature portfolio, open access).

## Problem
TUSZ studies often use non-standard splits, mix patients across partitions, or evaluate only on seizure segments. As a result, reported numbers are inflated and cannot be compared. The paper releases a transparent, reproducible benchmark on the official split with continuous-EEG evaluation. [Europe PMC abstract](https://pmc.ncbi.nlm.nih.gov/articles/PMC13049040/)

## Dataset
- **TUSZ v2.0.3**, using the official Train/Dev/Eval partition, so it is patient-independent. Evaluation runs on continuous EEG. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13049040/)
- Montage: 18 longitudinal bipolar derivations covering the temporal and parasagittal chains. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13049040/)

## Approach
- **60 s windows with a 15 s stride.** [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13049040/)
- Hand-crafted features [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13049040/):
  - time domain: RMS, line length, zero-crossings;
  - spectral: band powers, dominant frequency, spectral entropy;
  - connectivity: PLV, coherence;
  - wavelet and envelope features;
  - temporal-context statistics over ±5 windows.
- Three CatBoost ensembles: a base model that looks within one window, plus a full and a high-sensitivity temporal-context model. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13049040/)
- Post-processing [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13049040/):
  - 3-window moving average;
  - threshold 0.44;
  - **±30 s dilation**;
  - merging of gaps ≤ 40 s;
  - minimum event duration 10 s.
- The operating point is framed as an "alarm budget". On Dev, the threshold and post-processing are chosen together to maximise event sensitivity while keeping specificity ≥ 0.93 and FA ≤ 0.69/h. The chosen settings are then frozen and applied once to Eval. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13049040/)

## Evaluation protocol
- An event counts as detected if a predicted interval overlaps it by at least 10 s.
- Window-level metrics are also reported.
- Latency is reported. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13049040/)

## Key results (numbers)
- Eval set:
  - window-level AUROC **0.92** and balanced accuracy 0.83;
  - **event sensitivity 0.75** (0.749) at **0.68 FA/h**, which is about **16.4 FA/24h**;
  - time-based PPV 0.57 and recall 0.76;
  - window-level macro-F1 0.809 (95% CI 0.750-0.850).

  [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13049040/)
- **Latency**:
  - The median latency was reported as 0.0 s (IQR 0.0-0.0; range 0-1200 s) across 218 detected seizures.
  - 169 of 218 (77.5%) had a predicted interval already active before onset.
  - The authors attribute this to the conservative interval expansion (±30 s dilation), not to true pre-ictal detection.

  [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13049040/)
- Short focal seizures (30-90 s) had a detection rate of only 0.333. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13049040/)
- The paper compares itself with studies that inflate results by using non-standard protocols, e.g. Wong 2025 (event sensitivity 0.97, about 1.7 FA/h) and Liu 2025 (0.926 on a non-standard split). [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13049040/)

## Limitations
- It is an offline detector: 60 s windows, ±30 s dilation, and temporal context that includes future windows.
- **Its "0 s latency" is an artifact of the offline dilation and must not be cited as real-time latency.**
- The false-alarm burden is high (about 16 FA/24h).
- Short focal seizures are poorly detected.
- It uses TUSZ only and is not stratified by seizure type. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13049040/)

## Relevance to our project
- It is a strong, honest **protocol template**: official v2.0.3 split, thresholds frozen on Dev, continuous evaluation and an alarm budget.
- It is also a reproducible non-deep baseline.
- **Warning for our latency claims**: post-processing that dilates or uses future context makes latency look artificially small or negative. Our latency must be measured with a strictly causal pipeline.
