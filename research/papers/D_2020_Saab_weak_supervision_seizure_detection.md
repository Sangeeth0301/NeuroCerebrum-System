# D_2020_Saab: Weak supervision for automated seizure detection (npj Digital Medicine 2020)

## Citation & Link
Saab K., Dunnmon J., Ré C., Rubin D., Lee-Messer C. "Weak supervision as an efficient approach for automated seizure detection in electroencephalography." npj Digital Medicine 3:59, 2020. DOI: 10.1038/s41746-020-0264-0
- Open access (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC7170880/
- Publisher: https://www.nature.com/articles/s41746-020-0264-0

## Venue type
Peer-reviewed journal (Nature portfolio).

## Problem
CNNs for seizure detection need large labeled datasets, but expert labels are expensive. The paper asks whether the imperfect "weak" annotations that are already produced in routine clinical workflows can train good real-time detectors that work across patients. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7170880/)

## Dataset
- Stanford pediatric data: 5,076 patients and 36,644 EEGs. Stanford adult data: 7,363 patients and 99,721 EEGs. The test sets are 498 pediatric and 480 adult clips with gold-standard labels. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7170880/)
- The weak labels had "precision of 0.37 and recall of 0.45" when checked against expert review. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7170880/)
- **TUSZ v1.4**: the training set had 1,984 signals from 264 patients (1,327 seizure clips). The evaluation set had 1,013 files from 50 patients (685 seizure clips), split evenly into validation and test. The split is patient-independent because it uses the official TUSZ partition. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7170880/)

## Approach
- 19-channel 10-20 EEG resampled to 200 Hz. The model is a densely connected Inception CNN with about 12.7M parameters. The authors undersampled negatives to get a 50% positive training set. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7170880/)
- Two clip lengths:
  - **12 s clips** for "fast" seizure onset detection
  - **60 s clips** for "slow" detection

  [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7170880/)
- They also tested transfer across institutions (Stanford to TUH and TUH to Stanford) and fine-tuning. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7170880/)

## Evaluation protocol
- The task is clip-level seizure-onset classification, scored with AUROC and F1 against gold-standard clips.
- It is **not** continuous-EEG event scoring. The paper reports no FA/24h and no latency in seconds.

## Key results (numbers)
- AUROC:

  | Population | 12 s clips | 60 s clips |
  |---|---|---|
  | Pediatric | 0.91 | 0.93 |
  | Adult | 0.82 | 0.94 |

  [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7170880/)
- F1, weak-label CNN compared with Persyst-13:

  | Setting | Weak-label CNN | Persyst-13 |
  |---|---|---|
  | Pediatric 12 s | 0.67 | 0.07 |
  | Pediatric 60 s | 0.77 | 0.61 |
  | Adult 12 s | 0.49 | 0 |
  | Adult 60 s | 0.76 | 0.65 |

  This is the 18-point (pediatric) and 11-point (adult) F1 gain reported in the abstract. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7170880/)
- TUSZ transfer results:
  - The Stanford-trained model scored 4 AUROC points lower on TUH than a TUH-trained model.
  - The TUH-trained model scored 24 points lower on Stanford data.
  - Fine-tuning the Stanford model on TUH gained about 10 AUROC points over training on TUH alone.

  The absolute AUROC values on TUSZ were not captured in my extraction. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7170880/)
- Example clinical operating point (pediatric, fast detection): 90% TPR at 25% FPR. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7170880/)

## Limitations
- The evaluation is clip-based, not continuous. Its FPR is per clip, which is not comparable with FA/24h.
- The main data are private Stanford data. TUSZ is used only as a secondary or transfer set.
- The only latency information is the clip length: 12 s ("fast") versus 60 s.

## Relevance to our project
- It shows a clear trade-off between window length and speed. The 12 s clips were much worse for adults (F1 0.49) than 60 s clips (F1 0.76), so shorter context costs accuracy. Our earlier-detection method needs to close this gap.
- It shows that pretraining on a large external set, then fine-tuning on TUSZ, helps (+10 AUROC).
- Its 12 s / 60 s clip setup was later reused in TUSZ graph-network work (Tang et al., ICLR 2022; not reviewed here).
