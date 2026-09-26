# Leutmezer et al. 2003: ECG changes at the onset of epileptic seizures (FOUNDATIONAL, pre-2018)

## Citation & Link
- Leutmezer F, Schernthaner C, Lurger S, Pötzelberger K, Baumgartner C. "Electrocardiographic changes at the onset of epileptic seizures." *Epilepsia* 2003 (volume/pages not verified).
- DOI: [10.1046/j.1528-1157.2003.34702.x](https://onlinelibrary.wiley.com/doi/10.1046/j.1528-1157.2003.34702.x)
- PubMed: https://pubmed.ncbi.nlm.nih.gov/12614390/
- Open access: no free full text found (no PMC ID). **All numbers below come from the abstract only** (retrieved via [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1046/j.1528-1157.2003.34702.x&format=json&resultType=core)).

## Venue type
Peer-reviewed journal (Epilepsia, ILAE flagship journal). Labeled **foundational / older work**.

## Problem
How does heart rate (HR) change at the transition from preictal to ictal state in focal epilepsy, and does the HR change come before the EEG onset? ([abstract](https://pubmed.ncbi.nlm.nih.gov/12614390/))

## Dataset
- 145 seizures from 58 patients with focal epilepsy undergoing video-EEG monitoring, recorded with scalp EEG and ECG ([abstract](https://pubmed.ncbi.nlm.nih.gov/12614390/)).
- Groups: mesial TLE, non-lesional TLE, extratemporal epilepsy.

## Approach
- Consecutive RR intervals analysed over a 90-s window around seizure onset using a "newly developed mathematical method" (change-point style analysis of HR) ([abstract](https://pubmed.ncbi.nlm.nih.gov/12614390/)).
- Timing of HR increase compared with scalp-EEG seizure onset.

## Evaluation protocol
Retrospective, descriptive analysis of video-EEG-monitored seizures; group comparisons (TLE vs extratemporal; right vs left hemisphere). No classifier / no sensitivity-FAR evaluation.

## Key results (numbers) — abstract only
- Ictal-onset tachycardia in **86.9%** of seizures; bradycardia in only **1.4%**.
- HR increase **preceded scalp-EEG seizure onset by 13.7 s on average in TLE** and **8.2 s in extratemporal epilepsy** (difference significant).
- Incidence and magnitude of HR increase significantly larger in mesial TLE than non-lesional TLE or extratemporal epilepsy; right-hemispheric seizures associated with ictal-onset tachycardia.
- Two distinct temporal patterns of ictal HR change, differing between temporal and extratemporal groups.
- Source: [PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/12614390/)

## Limitations
- Single-centre, retrospective, focal epilepsy only; no generalized seizures.
- "Earlier than EEG" refers to **scalp** EEG onset; seizures probably started earlier in deep structures (the authors themselves explain that discharges influence the central autonomic network before they appear on surface electrodes — [abstract](https://pubmed.ncbi.nlm.nih.gov/12614390/)). So it is not true "prediction", just earlier detection relative to scalp EEG.
- Full methods (HR onset definition) not verified — abstract only.

## Relevance to our project
- Core justification for a body-reaction module: in focal (especially temporal) seizures the ECG channel may show tachycardia **~8-14 s before the scalp EEG onset annotated in datasets like TUSZ** (TUSZ labels are scalp-EEG based).
- Suggests we should extract HR in a window starting at least ~30-60 s before the TUSZ onset label and measure HR-onset latency relative to it.
- Expect stronger/earlier effect in temporal-lobe (in TUSZ: many FNSZ/CPSZ) seizures than extratemporal ones; right vs left lateralization matters (see also [Kato et al. 2014](https://www.neurology.org/doi/10.1212/WNL.0000000000000864)).
