# Stirling et al. 2021: Forecasting seizure likelihood with wearable technology

## Citation & Link
- Stirling RE, Grayden DB, D'Souza W, Cook MJ, Nurse E, Freestone DR, Payne DE, Brinkmann BH, Pal Attia T, Viana PF, Richardson MP, Karoly PJ. "Forecasting Seizure Likelihood With Wearable Technology." *Frontiers in Neurology* 2021;12:704060.
- DOI: 10.3389/fneur.2021.704060; PubMed [34335457](https://pubmed.ncbi.nlm.nih.gov/34335457/); open access PMC8320020 (abstract retrieved via [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.3389/fneur.2021.704060&format=json&resultType=core); preprint full text at [medRxiv](https://www.medrxiv.org/content/10.1101/2021.05.20.21257495v1.full)).
- **Numbers below are from the abstract**, except the mean AUC 0.74, which appears in search-result summaries of the paper ([ResearchGate listing](https://www.researchgate.net/publication/353275703_Forecasting_Seizure_Likelihood_With_Wearable_Technology)) and was not verified in the full text.

## Venue type
Peer-reviewed open-access journal (Frontiers in Neurology). Feasibility study.

## Problem
Can consumer wearables (smartwatch HR, sleep, steps) forecast high- vs low-risk seizure periods, using HR as a biomarker of circadian and multiday seizure cycles? ([abstract](https://pubmed.ncbi.nlm.nih.gov/34335457/))

## Dataset
- 11 participants with refractory epilepsy, >=20 self-reported seizures (mean 135, SD 123).
- Fitbit smartwatch HR, sleep and step counts + smartphone seizure diary, >=6 months (mean 14.6, SD 3.8 months).
- Source: [abstract](https://pubmed.ncbi.nlm.nih.gov/34335457/)

## Approach
- Ensemble of machine learning and neural network models estimating seizure risk **daily or hourly**; retrained weekly as data accumulate.
- Features include cyclic features (circadian and multiday HR cycles), sleep and steps.

## Evaluation protocol
Retrospective evaluation vs a rate-matched random forecast using AUC; plus pseudo-prospective evaluation on held-out data ([abstract](https://pubmed.ncbi.nlm.nih.gov/34335457/)).

## Key results (numbers)
- Hourly forecast better than chance in **11/11 (100%)** participants; daily forecast in **10/11 (91%)**.
- Average time in high-risk state before a seizure (prediction time): **37 min (hourly)** and **3 days (daily)**.
- Cyclic features, especially **circadian and multiday HR cycles**, added the most predictive value.
- Mean AUC ~0.74 (secondary source only; flag).
- Source: [abstract](https://pubmed.ncbi.nlm.nih.gov/34335457/)

## Limitations
- n = 11; seizure labels from self-report diaries (under-reporting of focal seizures is well known).
- Minute-level consumer HR (PPG), not ECG.
- Forecasting of risk periods, not onset-level warning.

## Relevance to our project
- Shows body signals give early warning on a **forecasting** timescale (hours-days) through HR **cycles**, not on the seconds timescale of ictal tachycardia.
- TUSZ recordings are short clinical EEGs (minutes to hours), so we cannot reproduce multiday cycles; we should explicitly scope our claim to peri-ictal (seconds-minutes) HR changes.
- Follow-up prospective study from the same group: [Stirling et al. 2023 eBioMedicine](https://www.sciencedirect.com/science/article/pii/S2352396423002219) (not reviewed in detail here).
