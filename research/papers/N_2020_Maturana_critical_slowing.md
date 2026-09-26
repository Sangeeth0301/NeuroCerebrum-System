# Critical slowing down as a biomarker for seizure susceptibility (Maturana et al., 2020)

## Citation & Link
Maturana MI, Meisel C, Dell K, Karoly PJ, D'Souza W, Grayden DB, Burkitt AN, Jiruska P, Kudlacek J, Hlinka J, Cook MJ, Kuhlmann L, Freestone DR. "Critical slowing down as a biomarker for seizure susceptibility." *Nature Communications* 11:2172 (2020).
- DOI: https://doi.org/10.1038/s41467-020-15908-3
- Open access (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC7195436/

## Venue type
Peer-reviewed journal (Nature Communications), open access.

## Problem
Dynamical-systems theory predicts that a system approaching a critical transition shows "critical slowing down" (CSD): rising variance and rising autocorrelation. The paper asks whether iEEG shows CSD signatures before seizures, on what timescales, and whether CSD markers can forecast seizure risk. — [PMC7195436](https://pmc.ncbi.nlm.nih.gov/articles/PMC7195436/)

## Dataset
- NeuroVista first-in-human trial (Cook et al. 2013): 14 patients with focal epilepsy, 16 subdural electrodes at 400 Hz; one patient (Patient 3) excluded because of 78.3% data dropout. — [PMC7195436](https://pmc.ncbi.nlm.nih.gov/articles/PMC7195436/)
- 2,871 seizures; recordings 185 to 767 days per patient (continuous, ambulatory, intracranial). — [PMC7195436](https://pmc.ncbi.nlm.nih.gov/articles/PMC7195436/)
- Mean data dropout 22.37% (up to 40.11%). — [PMC7195436](https://pmc.ncbi.nlm.nih.gov/articles/PMC7195436/)
- Recording type: **intracranial (subdural ECoG), not scalp.**

## Approach
- CSD markers: signal **variance** and **autocorrelation width (ACFW, width at half-maximum of the autocorrelation function)** computed from 1-s iEEG snapshots taken every 2 minutes (low-pass 170 Hz). Interictal epileptiform discharge (spike) rate was also computed. — [PMC7195436](https://pmc.ncbi.nlm.nih.gov/articles/PMC7195436/)
- Signals decomposed into long rhythms (>2 days; 2-day causal moving average) and short rhythms (<=1 day; 40-min smoothing). Cycles: circadian in all patients; multidien 3-30 day cycles in most patients; mean short cycle 0.64 +/- 0.16 days, long cycle 10.5 +/- 4.1 days. — [PMC7195436](https://pmc.ncbi.nlm.nih.gov/articles/PMC7195436/)
- Forecaster: seizure probability conditional on the **phase** of the variance, autocorrelation and spike-rate cycles; independent probability distributions multiplied; thresholds split time into low/medium/high risk (optimising time in low risk and seizures in high risk). — [PMC7195436](https://pmc.ncbi.nlm.nih.gov/articles/PMC7195436/)

## Evaluation protocol
- M1: anti-causal "optimal" model using all data (upper bound).
- M2: **pseudo-prospective**, causal filtering, seizure-phase distributions updated after each seizure over 50-day rolling windows; forecasting started after the 10th seizure.
- Chance comparison: performance product (sensitivity x time in low risk) compared with chance (9.6%). — [PMC7195436](https://pmc.ncbi.nlm.nih.gov/articles/PMC7195436/)

## Key results (numbers)
- Sensitivity (seizures in high-risk state): M1 84 +/- 16%, M2 77 +/- 8%. Time in low risk (reported as "specificity"): M1 95%, M2 91%. — [PMC7195436](https://pmc.ncbi.nlm.nih.gov/articles/PMC7195436/)
- Both methods significantly better than chance (chance performance product 9.6%, p < 1e-9); no significant difference between M1 and M2. — [PMC7195436](https://pmc.ncbi.nlm.nih.gov/articles/PMC7195436/)
- Seizures phase-locked to the rising phase of variance/autocorrelation cycles; synchronization index > 0.5 for short cycles in nearly all patients. — [PMC7195436](https://pmc.ncbi.nlm.nih.gov/articles/PMC7195436/)
- CSD at short timescales around seizure onset in 13/14 patients; gradual rise of autocorrelation/variance tens of minutes to hours before seizures in 9/14 patients. — [PMC7195436](https://pmc.ncbi.nlm.nih.gov/articles/PMC7195436/)
- M2 reported to outperform prior crowd-sourced/ML algorithms on the same dataset (Supplementary Table 2). — [PMC7195436](https://pmc.ncbi.nlm.nih.gov/articles/PMC7195436/)
- No per-patient ROC-AUC values tabulated (as extracted from the full text). — [PMC7195436](https://pmc.ncbi.nlm.nih.gov/articles/PMC7195436/)

## Limitations
- High data dropout, with gaps filled with Gaussian noise; one patient excluded.
- Seizure-onset marking subjective; non-stationarity over months (handled with rolling windows).
- Focal epilepsy, 14 patients, implanted device only.
- The key information is in the **hours-to-days** fluctuations, which need long continuous recordings. — [PMC7195436](https://pmc.ncbi.nlm.nih.gov/articles/PMC7195436/)

## Relevance to our project
- **Directly usable features:** variance and lag autocorrelation / ACFW of short windows are cheap to compute on scalp EEG and are the standard CSD early-warning signals.
- **Caveat for TUSZ:** most of the forecasting power came from phase in circadian/multidien cycles, which a TUSZ session (usually minutes to a few hours, sometimes about a day of LTM) cannot capture. On TUSZ we can only test the *short-timescale* claim, i.e. whether variance/autocorrelation rise in the minutes before onset compared with interictal segments (Maturana saw this in 9/14 patients at long timescales, 13/14 near onset).
- We should report results against a chance/surrogate baseline, as the paper does.
- Scalp EEG is more affected by artifacts (muscle, movement), which can inflate variance. Artifact rejection and per-channel normalization are needed before interpreting any "variance rise" as CSD.
