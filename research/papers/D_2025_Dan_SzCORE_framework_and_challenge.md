# D_2025_Dan: SzCORE evaluation framework (Epilepsia 2025) and the 2025 Seizure Detection Challenge report

## Citation & Link
1. Dan J., Pale U., Amirshahi A., Cappelletti W., Ingolfsson T.M., Wang X., Cossettini A., Bernini A., Benini L., Beniczky S., Atienza D., Ryvlin P. "SzCORE: Seizure Community Open-Source Research Evaluation framework for the validation of electroencephalography-based automated seizure detection algorithms." Epilepsia 66(Suppl 3):14-24, 2025. DOI: 10.1111/epi.18113
   - Open access (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC12489712/
   - Publisher: https://onlinelibrary.wiley.com/doi/10.1111/epi.18113
   - Preprint: https://arxiv.org/html/2402.13005
2. Dan J., Shahbazinia A., Kechris C., Atienza D. "Quantifying the Generalization Gap in Seizure Detection: A Large-Scale Empirical Benchmark via the SzCORE Challenge." arXiv:2505.18191 (v1 May 2025, v2 May 2026). v1 was titled "SzCORE as a benchmark: report from the seizure detection challenge at the 2025 AI in Epilepsy and Neurological Disorders Conference."
   - arXiv: https://arxiv.org/abs/2505.18191
   - EPFL record: https://infoscience.epfl.ch/entities/publication/b5991dd8-dff4-490f-a449-f314b679c0d9
   - Challenge site: https://epilepsybenchmarks.com/challenge/
3. A related PubMed record, "Benchmark of EEG-based seizure detection algorithms with SzCORE" (https://pubmed.ncbi.nlm.nih.gov/41336388/), could not be accessed because of a CAPTCHA. Its journal and content are unverified.

## Venue type
- (1) is a peer-reviewed journal paper (Epilepsia supplement).
- (2) is a **preprint**. I could not verify whether it has been published in a journal.

## Problem
Seizure-detection validation varies widely in datasets, cross-validation, annotation formats and metrics, so reported results cannot be compared. SzCORE proposes one standard plus a public benchmark and an open-source scoring library. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12489712/)

## Dataset
- The EEG 10-20 benchmark uses four public datasets converted to one format: **CHB-MIT, TUSZ, Siena and SeizeIT1**. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12489712/)
- The 2025 challenge tested algorithms on a **private held-out Dianalund dataset**: 65 subjects, 4,360 h of continuous EEG, annotated by expert neurophysiologists. It ran from December 2024 to February 2025. [arXiv](https://arxiv.org/abs/2505.18191); [EPFL](https://infoscience.epfl.ch/entities/publication/b5991dd8-dff4-490f-a449-f314b679c0d9)

## Approach
SzCORE standardises how detectors are evaluated; it does not propose a detector.
- Input: the 19 electrodes of the 10-20 system in a unipolar common-average montage, at 256 Hz. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12489712/)

## Evaluation protocol
- **Event-based scoring**:
  - A detection counts if it overlaps a reference event.
  - The recommended "30-s preictal tolerance" means a detection that starts up to 30 s before onset still counts.
  - The recommended "60-s postictal tolerance" does the same after offset.

  [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12489712/)
- The SzCORE preprint also merges events closer than 90 s and splits events longer than 5 min. I did not re-verify these values in the Epilepsia version, so treat them as unconfirmed. See the [arXiv preprint](https://arxiv.org/html/2402.13005).
- **Sample-based scoring** uses 1 Hz labels. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12489712/)
- Reported metrics are sensitivity, precision, F1 and false alarms per day, for each subject. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12489712/)
- **SzCORE does not define detection latency.** [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12489712/)

## Key results (numbers)
- In the challenge, 28-30 algorithms from 19 teams were evaluated on Dianalund. [arXiv](https://arxiv.org/abs/2505.18191); [EPFL](https://infoscience.epfl.ch/entities/publication/b5991dd8-dff4-490f-a449-f314b679c0d9)
- **The sources conflict on the top score**:

  | Source | Top event F1 | Sensitivity | Precision |
  |---|---|---|---|
  | EPFL record (v1-era abstract) | 43% | 37% | 45% |
  | arXiv v2 abstract | 32% | 37% | 29% |

  The v2 revision probably recomputed the results; check the full paper. The SeizureTransformer preprint also reports its own first-place F1 as 0.43. All of these numbers are from abstracts. [EPFL](https://infoscience.epfl.ch/entities/publication/b5991dd8-dff4-490f-a449-f314b679c0d9); [arXiv](https://arxiv.org/abs/2505.18191)
- The authors report "a notable gap between self-reported efficacies and hold-out performance", and top-ranked algorithms were inconsistent across patients. [arXiv](https://arxiv.org/abs/2505.18191)

## Limitations
- There is no latency metric. The 30 s preictal and 60 s postictal tolerances mean a detection up to 60 s late still counts as correct, so SzCORE F1 cannot show whether one method is earlier than another.
- Dianalund is private, so it can only be used through submission to the challenge platform.

## Relevance to our project
- Report SzCORE event F1, sensitivity and FP/day on TUSZ so our results are comparable with SeizureTransformer and later work.
- **Add our own latency metric** (seconds from onset to first alarm), plus the fraction of seizures detected within 5 or 10 s, because SzCORE hides differences in speed.
- The generalization gap (TUSZ F1 about 0.67 versus held-out F1 of 0.32-0.43) suggests we should also test on Siena or CHB-MIT.
