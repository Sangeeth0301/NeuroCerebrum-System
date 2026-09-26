# Forecasting seizure risk in adults with focal epilepsy: a development and validation study (Proix et al., 2021)

## Citation & Link
Proix T, Truccolo W, Leguia MG, Tcheng TK, King-Stephens D, Rao VR, Baud MO. "Forecasting seizure risk in adults with focal epilepsy: a development and validation study." *The Lancet Neurology* 20(2):127-135 (2021).
- DOI: https://doi.org/10.1016/S1474-4422(20)30396-3
- Open access (PMC author manuscript): https://pmc.ncbi.nlm.nih.gov/articles/PMC7968722/

## Venue type
Peer-reviewed journal (Lancet Neurology).

## Problem
Can seizure risk be forecast hours to days ahead using cycles of interictal epileptiform activity (IEA), and does this generalise to a large validation cohort using self-reported seizures? — [PMC7968722](https://pmc.ncbi.nlm.nih.gov/articles/PMC7968722/)

## Dataset
- 175 adults with drug-resistant focal epilepsy and the **RNS System**, recorded 2004-2018 at 35 US centres. Mean 1,484 days per subject (range 227-3,502). — [PMC7968722](https://pmc.ncbi.nlm.nih.gov/articles/PMC7968722/)
- Development cohort: 18 subjects with **electrographic** seizures (at least 20 each). Validation cohort: 157 subjects with **self-reported** disabling seizures (at least 20 each). — [PMC7968722](https://pmc.ncbi.nlm.nih.gov/articles/PMC7968722/)
- Test sets: 767 electrographic seizures and 27,658 self-reported seizures. Median 19% (development) and 9% (validation) of test days contained seizures. — [PMC7968722](https://pmc.ncbi.nlm.nih.gov/articles/PMC7968722/)

## Approach
Point-process generalised linear models (log link, conditionally Poisson). Features were recent seizure history, hourly IEA counts, IEA **circadian** and **multidien phase**, and the circadian seizure distribution. Seizure-days and seizure-hours were treated as binary to handle clustering. — [PMC7968722](https://pmc.ncbi.nlm.nih.gov/articles/PMC7968722/)

## Evaluation protocol
- **Pseudo-prospective:** training on the shorter of 480 days or 60% of the data, testing on later data (often more than 800 days). — [PMC7968722](https://pmc.ncbi.nlm.nih.gov/articles/PMC7968722/)
- **Chance comparison:** "improvement over chance" (IoC), where AUC was compared with 200 surrogate series (shuffled seizure times or randomised IEA phases), with FDR correction at 0.05. Brier skill score (BSS) and reliability diagrams were also reported. AUC was defined on sensitivity vs corrected proportion of time in warning. — [PMC7968722](https://pmc.ncbi.nlm.nih.gov/articles/PMC7968722/)
- Note: the Lancet Neurology paper describes the phase estimation as partly non-causal (listed as a limitation in the full text). — [PMC7968722](https://pmc.ncbi.nlm.nih.gov/articles/PMC7968722/)

## Key results (numbers)
- Daily (24 h) forecasts, development cohort: IoC in 15/18 (83%), median AUC 0.74 (IQR 0.70-0.79), median BSS 0.23 (IQR 0.18-0.30). — [PMC7968722](https://pmc.ncbi.nlm.nih.gov/articles/PMC7968722/)
- Daily forecasts, validation cohort: IoC in 104/157 (66%), median AUC 0.70 (IQR 0.65-0.75), median BSS 0.13 (IQR 0.05-0.20). — [PMC7968722](https://pmc.ncbi.nlm.nih.gov/articles/PMC7968722/)
- 3-day horizon (multidien phase only): IoC in 2/18 (11%) in development and 61/157 (39%) in validation. — [PMC7968722](https://pmc.ncbi.nlm.nih.gov/articles/PMC7968722/)
- Hourly forecasts (development only): IoC in 18/18, median AUC about 0.75, median BSS about 0.036. At a 14-h horizon, IoC in 8/18. The extracted IQR values for the hourly metrics looked garbled and should be checked against the PDF. — [PMC7968722](https://pmc.ncbi.nlm.nih.gov/articles/PMC7968722/)
- Pro-ictal (high-risk) states lasted 3-9 days in most subjects. RR in forecasted high-risk periods was 3.7 (95% CI 2.8-4.7) for electrographic seizures and 9.4 (95% CI 4.5-14.9) for self-reported seizures. — [PMC7968722](https://pmc.ncbi.nlm.nih.gov/articles/PMC7968722/)
- Calibration was good overall but overconfident above 25% forecast probability, and improved with longer training and retraining. — [PMC7968722](https://pmc.ncbi.nlm.nih.gov/articles/PMC7968722/)
- Time in warning / sensitivity at a fixed threshold is not reported as a single number; it is folded into the AUC. — [PMC7968722](https://pmc.ncbi.nlm.nih.gov/articles/PMC7968722/)

## Limitations
Requires an RNS implant. Self-reported seizures are under-reported. The validation cohort has daily resolution only. Triggers (sleep, medication, stress) were not included. The authors call the results hypothesis-generating. — [PMC7968722](https://pmc.ncbi.nlm.nih.gov/articles/PMC7968722/)

## Relevance to our project
- This is the reference **evaluation template**: pseudo-prospective split, AUC over time-in-warning, surrogate-based improvement over chance, Brier skill score, and reliability diagrams. We should copy these metrics (IoC via shuffled-label or time-shifted surrogates, plus BSS) rather than reporting only accuracy.
- The **realistic ceiling** for a biomarker-driven forecaster with years of data is AUC about 0.70-0.75. A TUSZ model claiming far higher numbers on short windows should be checked for leakage (for example, near-onset segments or patient overlap).
- The multidien component is not available on TUSZ. Our analogue is the within-recording IED rate and circadian phase.
