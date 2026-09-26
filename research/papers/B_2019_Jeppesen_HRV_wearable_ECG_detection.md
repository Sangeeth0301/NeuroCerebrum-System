# Jeppesen et al. 2019: Seizure detection based on HRV using a wearable ECG device (phase 2)

## Citation & Link
- Jeppesen J, Fuglsang-Frederiksen A, Johansen P, Christensen J, Wüstenhagen S, Tankisi H, Qerama E, Hess A, Beniczky S. "Seizure detection based on heart rate variability using a wearable electrocardiography device." *Epilepsia* 2019 (volume/pages not verified).
- DOI: [10.1111/epi.16343](https://onlinelibrary.wiley.com/doi/10.1111/epi.16343)
- PubMed ID 31538347 ([Europe PMC listing](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1111/epi.16343&format=json&resultType=core))
- Open access: not OA in Europe PMC (no PMCID); Wiley page returned 403 to us. **Numbers below are from the abstract only.**

## Venue type
Peer-reviewed journal (Epilepsia). Phase 2 prospective clinical validation study.

## Problem
Non-EEG wearables detect convulsive seizures well, but nonconvulsive (focal) seizure detection had low sensitivity or very high FAR. Can HRV from a wearable ECG detect seizures including nonconvulsive ones? ([abstract](https://onlinelibrary.wiley.com/doi/10.1111/epi.16343))

## Dataset
- 100 consecutive patients admitted to long-term video-EEG monitoring (LTM), Denmark; ECG from a dedicated wearable device (device model not named in the abstract).
- 126 seizures from 43 patients with seizures: **108 nonconvulsive, 18 convulsive** ([abstract](https://onlinelibrary.wiley.com/doi/10.1111/epi.16343)).

## Approach
- 26 automated HRV algorithms compared, computed off-line and blinded to other data.
- Best: combination of a sympathetic-activity measure (Cardiac Sympathetic Index, CSI / modified CSI derived from Lorenz/Poincaré plot of 100 consecutive RR intervals — method family described in the group's earlier [Seizure 2015 paper](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=(AUTH:%22Jeppesen%20J%22%20AND%20(heart%20rate%20variability%20seizure))&format=json&resultType=lite&pageSize=15) and summarised in [NeurologyLive coverage](https://www.neurologylive.com/view/wearable-ecg-device-detects-nonconvulsive-seizures-successfully-with-heart-rate-variability)) with a measure of **how quickly HR changes** (HR slope).
- Threshold details (patient-specific vs fixed) not stated in the abstract; the group's later phase 3 study uses a patient-specific threshold at 105% of max baseline ([eBioMedicine 2025](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12516532/fullTextXML)).

## Evaluation protocol
Prospective recruitment, off-line blinded detection, compared with expert-marked seizure time-points from video-EEG. A patient is a "responder" if >66% of their seizures are detected.

## Key results (numbers) — abstract only
- **53.5%** of patients with seizures were responders.
- Among responders: sensitivity **93.1%** (95% CI 86.6-99.6%) for all seizures and **90.5%** (95% CI 77.4-97.3%) for nonconvulsive seizures.
- FAR **1.0 / 24 h (0.11 / night)**.
- Median detection latency **30 s**.
- **Ictal HR change > 50 bpm** predicted responder status with PPV 87% and NPV 90%.
- Source: [abstract](https://onlinelibrary.wiley.com/doi/10.1111/epi.16343)

## Limitations
- Works only in patients with marked ictal autonomic change (~half of patients).
- Offline analysis in hospital; phase 2.
- Detection latency 30 s means it is a detector, not an early-warning system, despite possible pre-EEG tachycardia.

## Relevance to our project
- Direct template for our ECG body-reaction features from the TUSZ ECG channel: RR-interval extraction -> CSI/ModCSI over 100 RR intervals + HR slope.
- Key target variable: **peak ictal HR change (bpm)**; >50 bpm defines "autonomic responders". We can estimate this per seizure type in TUSZ.
- Nonconvulsive (focal) seizures can be detected via HR in responders, so body reaction is not limited to tonic-clonic seizures.
