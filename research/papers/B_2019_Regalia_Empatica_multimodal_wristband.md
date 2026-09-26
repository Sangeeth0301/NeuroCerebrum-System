# Regalia et al. 2019: Multimodal wrist-worn devices for seizure detection (Empatica Embrace/E4) + prospective validation (Onorati et al. 2021)

This file covers two linked papers: the 2019 Epilepsy Research review/position paper requested, and the 2021 prospective multicentre validation of the same EDA+accelerometry detector, which gives the hard numbers.

## Citation & Link
1. Regalia G, Onorati F, Lai M, Caborni C, Picard RW. "Multimodal wrist-worn devices for seizure detection and advancing research: Focus on the Empatica wristbands." *Epilepsy Research* 2019.
   - DOI: [10.1016/j.eplepsyres.2019.02.007](https://www.sciencedirect.com/science/article/abs/pii/S0920121118305849); PubMed [30846346](https://pubmed.ncbi.nlm.nih.gov/30846346/)
   - Open-access author manuscript: [MIT DSpace](https://dspace.mit.edu/handle/1721.1/123804) (PDF could not be fetched by our tool; **Regalia numbers are from the abstract only**, via [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/j.eplepsyres.2019.02.007&format=json&resultType=core)).
2. Onorati F, Regalia G, Caborni C, LaFrance WC Jr, Blum AS, Bidwell J, De Liso P, El Atrache R, Loddenkemper T, Mohammadpour-Touserkani F, Sarkis RA, Friedman D, Jeschke J, Picard RW. "Prospective Study of a Multimodal Convulsive Seizure Detection Wearable System on Pediatric and Adult Patients in the Epilepsy Monitoring Unit." *Frontiers in Neurology* 2021.
   - DOI: 10.3389/fneur.2021.724904; open access [PMC8418082](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8418082/) (full text read via [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8418082/fullTextXML)).

## Venue type
(1) Peer-reviewed journal, review/summary of company-affiliated evidence (authors from Empatica / MIT Media Lab — note conflict of interest). (2) Peer-reviewed journal, prospective multicentre validation.

## Problem
Detect generalized tonic-clonic seizures (GTCS, incl. focal-to-bilateral TC) with a wrist device to give alerts and reduce SUDEP risk; also quantify seizure-induced autonomic dysfunction ([Regalia abstract](https://pubmed.ncbi.nlm.nih.gov/30846346/)).

## Dataset
- Regalia 2019: summary of retrospective and prospective inpatient datasets plus outpatient real-life data collected with E4/Embrace, labelled by video-EEG ([abstract](https://pubmed.ncbi.nlm.nih.gov/30846346/)); patient counts not given in abstract.
- Onorati 2021: 152 patients (85 pediatric 6-20 y; 67 adults 21-63 y) at 7 Level IV epilepsy centres (US + Rome); 36 had seizures; **66 convulsive seizures (12 GTC, 54 FBTC)** ([full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8418082/fullTextXML)).

## Approach
- Signals: 3-axis accelerometer (32 Hz) and electrodermal activity (EDA, 4 Hz) at the wrist.
- Machine-learning detector on 40 ACC+EDA features over 10-s windows (75% overlap); algorithm "fixed and frozen" before testing on an independent cohort ([Onorati full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8418082/fullTextXML)).

## Evaluation protocol
Onorati 2021: prospective, video-EEG reference, 3 blinded neurologists with 2-of-3 majority labelling; sensitivity with CI, FAR/24 h, latency ([full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8418082/fullTextXML)).

## Key results (numbers)
Regalia 2019 (abstract only):
- Sensitivity to GTCS **92-100%**; FAR reduced from ~2 to **0.2-1 false alarms/day** in inpatient settings; outpatient FAR from ~6 down to **<0.5/day** after algorithm adjustment ([abstract](https://pubmed.ncbi.nlm.nih.gov/30846346/)).
- EDA response correlates with duration of **post-ictal generalized EEG suppression (PGES)**, a biomarker seen in 100% of monitored SUDEP cases ([abstract](https://pubmed.ncbi.nlm.nih.gov/30846346/)).

Onorati 2021 (full text):
| Mode | Group | Sensitivity [CI] | FAR / 24 h [CI] |
|---|---|---|---|
| FDA-cleared | Pediatric | 0.92 [0.85-1.00] | 1.26 [0.87-1.73] |
| FDA-cleared | Adult | 0.94 [0.89-1.00] | 0.57 [0.36-0.81] |
| Active | Pediatric | 0.85 [0.72-0.98] | 0.40 [0.23-0.59] |
| Active | Adult | 0.94 [0.89-1.00] | 0.18 [0.10-0.28] |
- Mean detection latency **37.46 s (SD 21.09)**; FAR = 0 during rest periods.
- Source: [full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8418082/fullTextXML)

## Limitations
- Only convulsive (GTC/FBTC) seizures; no focal non-motor seizures.
- EMU setting; industry-affiliated authors.
- Detection latency ~37 s => detection, not warning.

## Relevance to our project
- Establishes the "body reaction" for tonic-clonic seizures: rhythmic motion (ACC) + sympathetic sweating (EDA surge, mostly post-ictal) — useful as the expected reaction profile for TUSZ GNSZ/TCSZ/FBTC-type labels.
- EDA is **post-ictal** and linked to PGES/SUDEP risk -> body-reaction module can output a severity/after-effect estimate, not only onset.
- TUSZ has no EDA/ACC; our module can only borrow these as literature priors.
