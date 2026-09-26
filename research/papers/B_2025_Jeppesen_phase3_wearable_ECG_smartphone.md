# Jeppesen et al. 2025: Seizure detection using wearable ECG connected to a smartphone (phase 3)

## Citation & Link
- Jeppesen J, Christensen J, Ahrenfeldt Petersen O, et al. "Seizure detection using wearable electrocardiogram connected to a smartphone: a phase 3 clinical validation study." *eBioMedicine* 2025 (Lancet family).
- DOI: [10.1016/j.ebiom.2025.105952](https://www.sciencedirect.com/science/article/pii/S2352396425003962)
- Open access: yes, PMC12516532 — full text read via [Europe PMC full text XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12516532/fullTextXML).
- Chosen as a replacement/upgrade for Jeppesen 2020 Epilepsia (prospective phase 2 validation, [10.1111/epi.16511](https://onlinelibrary.wiley.com/doi/abs/10.1111/epi.16511)) because it is phase 3, real-time and open access.

## Venue type
Peer-reviewed journal (eBioMedicine). Phase 3, prospective, blinded, multicentre.

## Problem
Validate in real time (ECG patch -> smartphone) an HRV-based detector for both focal-to-bilateral tonic-clonic (FBTC) and focal seizures in patients with ictal autonomic changes ([full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12516532/fullTextXML)).

## Dataset
- Two Danish EMUs (Aarhus University Hospital, Danish Epilepsy Centre), Feb 2022-Sep 2024.
- 101 enrolled; eligible cohort = 17 patients who met the autonomic criterion (HR increase **>50 bpm** during the first recorded seizure).
- 42 seizures: **19 FBTC; 23 focal (14 impaired awareness, 9 aware)**; 880 h monitoring in the eligible cohort.
- Source: [full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12516532/fullTextXML)

## Approach
- Device: Cortrium C3 ECG patch (256 Hz) streaming via Bluetooth to a smartphone.
- Features: CSI and ModCSI from Lorenz-plot analysis on sliding windows of 100 RR intervals.
- Patient-specific threshold: 105% of highest baseline value in the first 24 h (baseline included exercise, cognitive stress and video tasks).
- Smartphone app (ASSURE) launches a behavioural test (arithmetic/memory) after an alarm to confirm/reject the alarm.
- Source: [full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12516532/fullTextXML)

## Evaluation protocol
Prospective, blinded comparison against video-EEG in EMU; per-seizure and per-patient sensitivity, FAR per 24 h and per night, detection latency.

## Key results (numbers) — full text
| Metric | Value |
|---|---|
| Overall sensitivity | 90.5% (95% CI 77.4-97.3%) |
| FBTC | 100% (19/19) |
| Focal seizures | 82.6% (19/23; CI 61.2-95.1%) |
| Median per-patient sensitivity | 100% (range 50-100%) |
| FAR | mean 2.5 / 24 h; median 1.1 / 24 h |
| FAR at night | mean 0.5; median 0 |
| Median detection latency | 28 s (range 15-278 s) |
| Behavioural test | cancelled all 47 tested false alarms; confirmed 15/15 seizures |
| Signal loss | 4.5% of time |
Source: [full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12516532/fullTextXML)

## Limitations
- Only 17/101 patients eligible (autonomic responders); results do not generalize to seizures without sympathetic activation.
- 16% discontinuation due to skin irritation.
- Seizures < 20 s excluded.
- EMU setting.
- Source: [full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12516532/fullTextXML)

## Relevance to our project
- Confirms HR/HRV reaction is strong and reliable in FBTC (100%) and present in a majority of focal seizures of responders (82.6%).
- Latency (median 28 s) shows that **practical ECG detectors alert after, not before, clinical onset**, even though raw tachycardia can start before scalp EEG onset. Our early-warning claim must be framed carefully.
- The patient-specific baseline threshold (105% of max baseline) is a simple, reproducible baseline we can replicate on TUSZ ECG if enough per-patient background exists.
