# Multi-day rhythms modulate seizure risk in epilepsy (Baud et al., 2018)

## Citation & Link
Baud MO, Kleen JK, Mirro EA, Andrechak JC, King-Stephens D, Chang EF, Rao VR. "Multi-day rhythms modulate seizure risk in epilepsy." *Nature Communications* 9:88 (2018).
- DOI: https://doi.org/10.1038/s41467-017-02577-y
- Open access (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC5758806/

## Venue type
Peer-reviewed journal (Nature Communications), open access.

## Problem
How is seizure timing related to fluctuating rates of interictal epileptiform activity (IEA), and do IEA rates follow cycles that could be used to estimate seizure risk? — [PMC5758806](https://pmc.ncbi.nlm.nih.gov/articles/PMC5758806/)

## Dataset
- 37 subjects (22 male, age 22-58) with drug-resistant focal epilepsy, implanted with the NeuroPace **RNS System** (responsive neurostimulation). — [PMC5758806](https://pmc.ncbi.nlm.nih.gov/articles/PMC5758806/)
- Recording duration: median 2.3 years (range 3 months to 9.9 years), with device-detected IEA counts and electrographic seizure detections. — [PMC5758806](https://pmc.ncbi.nlm.nih.gov/articles/PMC5758806/)
- Recording type: chronic intracranial (RNS). Much of the data is event counts rather than raw EEG.

## Approach
Time-series analysis of hourly IEA counts to identify circadian and multidien (multi-day) periodicities (spectral/wavelet analysis). Instantaneous phase of each rhythm was estimated at seizure times, phase-locking of seizures was tested, and relative risk was computed by phase. — [PMC5758806](https://pmc.ncbi.nlm.nih.gov/articles/PMC5758806/)

## Evaluation protocol
Retrospective, descriptive. Circular statistics tested phase-locking, and relative risk (RR) compared high- vs low-risk phases. There was no pseudo-prospective forecaster; that came later in Proix et al. 2021. — [PMC5758806](https://pmc.ncbi.nlm.nih.gov/articles/PMC5758806/)

## Key results (numbers)
- All subjects showed circadian IEA rhythms, and nearly all showed multidien rhythms. Median multidien-to-circadian amplitude ratio was 1.4 (range 0.4-5.7; above 1 in 27 subjects). — [PMC5758806](https://pmc.ncbi.nlm.nih.gov/articles/PMC5758806/)
- Most common periods were 26-30 days (N = 18) and 20-22 days (N = 16). The abstract states "most commonly 20-30 days", stable for up to 10 years in men and women. — [PMC5758806](https://pmc.ncbi.nlm.nih.gov/articles/PMC5758806/)
- Among the 14 subjects with reliable seizure detection, seizures were phase-locked to circadian rhythms in 12/14 and to multidien rhythms in 13/14. Seizures were more tightly coupled to the multidien phase (p = 0.002) and occurred preferentially on the **rising phase** of multidien IEA. — [PMC5758806](https://pmc.ncbi.nlm.nih.gov/articles/PMC5758806/)
- Combining circadian and multidien phase gave RR from 1.2 to 24.5 across subjects; unweighted RR was 6.8 (95% CI 3.1-15.1). Risk was highest when both rhythms were in phase. — [PMC5758806](https://pmc.ncbi.nlm.nih.gov/articles/PMC5758806/)
- No sex difference in periodicities (p = 0.87). Rhythms were stable despite changes to stimulation settings. — [PMC5758806](https://pmc.ncbi.nlm.nih.gov/articles/PMC5758806/)

## Limitations
Only drug-resistant focal epilepsy with RNS implants. Therapeutic stimulation may confound results. Electrographic (device-detected) rather than clinical seizures were used. Retrospective design. — [PMC5758806](https://pmc.ncbi.nlm.nih.gov/articles/PMC5758806/)

## Relevance to our project
- This is the paper that established multidien cycles. Seizure risk is modulated on timescales of weeks, which **cannot be observed within a TUSZ recording**. TUSZ sessions lack multi-week continuity, and the patient-level record linkage across sessions is sparse and irregular.
- Practical use: (1) motivate that short-window features explain only part of the variance in risk; (2) include **time of day** (circadian phase), if TUSZ timestamps allow it, as a covariate; (3) use **IED rate** within the recording as a feature, since IEA fluctuations carry risk information.
- If we claim "earlier forecasting" on TUSZ, we should frame it as a *preictal state detection* (minutes to hours), not multiday forecasting.
