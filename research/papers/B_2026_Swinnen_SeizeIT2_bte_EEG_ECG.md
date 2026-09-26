# Swinnen et al. 2026: SeizeIT2 — multicentre validation of a behind-the-ear EEG + ECG wearable for focal seizures

## Citation & Link
- Swinnen L, Bhagubai M, Chatzichristos C, Weber Y, Wolking S, Ermis U, Schriewer E, Schulze-Bonhage A, Dümpelmann M, Zabler N, Epitashvilli N, Mahler B, Sen A, Symmonds M, Richardson MP, Biondi A, Sales F, Sulaiman A, De Vos M, Van Paesschen W. "A multicenter, video-EEG-based validation of a multimodal wearable device for focal seizure detection in adults: The SeizeIT2 study." *Epilepsia Open* 2026;11:883-894 (volume/pages from [search summary](https://onlinelibrary.wiley.com/doi/full/10.1002/epi4.70260), not independently checked).
- DOI: [10.1002/epi4.70260](https://onlinelibrary.wiley.com/doi/full/10.1002/epi4.70260); open access [PMC13238671](https://pmc.ncbi.nlm.nih.gov/articles/PMC13238671/). ClinicalTrials.gov NCT04284072.
- Full text blocked for our fetch tool (403/CAPTCHA); **numbers are from the abstract** ([Europe PMC record](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1002/epi4.70260&format=json&resultType=core)).
- Note: the brief mentioned "Epilepsia 2024/2025"; the main validation paper is in **Epilepsia Open 2026**. The companion open dataset is [SeizeIT2, Scientific Data 2025](https://www.nature.com/articles/s41597-025-05580-x).

## Venue type
Peer-reviewed journal (Epilepsia Open, ILAE). Multicentre prospective validation.

## Problem
Existing wearables mostly detect major motor seizures or need subscalp implants; need non-invasive detection of diverse focal seizures out of hospital ([abstract](https://pmc.ncbi.nlm.nih.gov/articles/PMC13238671/)).

## Dataset
- 192 adults with refractory focal epilepsy in long-term video-EEG monitoring (multiple European centres); **616 focal seizures**; mean 5 days of wearable monitoring ([abstract](https://pmc.ncbi.nlm.nih.gov/articles/PMC13238671/)).
- Device: Sensor Dot (Byteflies) — 2-channel behind-the-ear EEG + ECG (the dataset also includes EMG and accelerometer/gyroscope, >11,000 h: [Scientific Data](https://www.nature.com/articles/s41597-025-05580-x)).

## Approach
Offline automated detection algorithm on wearable data, then blinded human-expert review of algorithm-flagged segments; compared with video-EEG ground truth ([abstract](https://pmc.ncbi.nlm.nih.gov/articles/PMC13238671/)).

## Evaluation protocol
Event-based sensitivity, precision, F1 vs video-EEG; post-hoc subgroup analysis by seizure characteristics (type, visible bte-EEG pattern, ictal tachycardia).

## Key results (numbers) — abstract only
- Algorithm alone: sensitivity **0.73**, precision **0.004**, F1 **0.01** (i.e., huge number of false detections).
- Algorithm + human review: precision **0.83**, sensitivity **0.31**, F1 **0.45**.
- Detection depended on seizure type (FIAS vs FBTCS) and presence of a distinct ictal pattern on behind-the-ear EEG (mostly temporal lobe seizures).
- Subgroup with clear ictal EEG pattern **and ictal tachycardia**: sensitivity **0.74**; with EEG pattern but **no tachycardia**: **0.60**.
- Comparable sensitivity to diary self-report but higher precision (0.83 vs 0.60).
- Source: [abstract](https://pmc.ncbi.nlm.nih.gov/articles/PMC13238671/)
- FAR per 24 h and latency not stated in the abstract (gap).

## Limitations
- Unselected focal seizures -> low overall performance; subgroups defined post hoc from ground truth.
- Human-in-the-loop review; not real time.

## Relevance to our project
- Strongest recent evidence that **adding ECG (tachycardia) helps** focal seizure detection: 0.74 vs 0.60 sensitivity when tachycardia is present.
- Temporal-lobe seizures with tachycardia are the "sweet spot" — consistent with Leutmezer 2003 and Jeppesen.
- SeizeIT2 open dataset (bte-EEG + ECG + ACC + EMG) could serve as an external dataset to validate a TUSZ-trained ECG body-reaction model. A dedicated ECG-only analysis on SeizeIT2 also exists ([PMC12736484](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12736484/), not reviewed).
