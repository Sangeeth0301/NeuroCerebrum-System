# Dynamic excitation/inhibition balance preceding seizure onset and its link to functional and structural brain architecture (Duma, Cuozzo et al., 2025)

## Citation & Link
Duma GM, Cuozzo S, et al. (senior authors Bonanni P, Pellegrino G). "Dynamic excitation/inhibition balance preceding seizure onset and its link to functional and structural brain architecture." *BMC Medicine* (2025).
- DOI: https://doi.org/10.1186/s12916-025-04447-7
- Open access: https://bmcmedicine.biomedcentral.com/articles/10.1186/s12916-025-04447-7 ; PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC12581463/ ; PubMed 41184927
- Preprint: medRxiv 10.1101/2025.06.16.25329680 — https://www.medrxiv.org/content/10.1101/2025.06.16.25329680v1

## Venue type
Peer-reviewed journal (BMC Medicine), open access.

## Problem
Does the E/I balance, indexed by the aperiodic (1/f) exponent of the EEG power spectrum, change in the minutes before focal seizures on **non-invasive** EEG, and does the change relate to epileptogenic vs non-epileptogenic regions, connectivity, cortical structure and receptor maps? — [PMC12581463](https://pmc.ncbi.nlm.nih.gov/articles/PMC12581463/)

## Dataset
- 20 patients with focal epilepsy (85% drug-resistant; mean age 35.5 +/- 16.9; 9 female). **128-channel scalp high-density EEG**, 512 Hz. — [PMC12581463](https://pmc.ncbi.nlm.nih.gov/articles/PMC12581463/)
- 29 seizures (1-3 per patient). About 13 min of pre-seizure signal analysed (at least 5 min after artifact cleaning). 75% of seizures occurred during wakefulness. Control: 10-min resting EEG at least 3 h from a seizure. — [PMC12581463](https://pmc.ncbi.nlm.nih.gov/articles/PMC12581463/)

## Approach
- Source reconstruction (FreeSurfer, Brainstorm, 3-shell BEM, weighted minimum norm) onto 68 Desikan-Killiany regions. — [PMC12581463](https://pmc.ncbi.nlm.nih.gov/articles/PMC12581463/)
- Time-resolved aperiodic exponent via **SPRiNT** (specparam in sliding windows): 60-s windows with 90% overlap, 1-40 Hz, peak width 0.5-12 Hz, max 3 peaks, min peak height 3 dB. — [PMC12581463](https://pmc.ncbi.nlm.nih.gov/articles/PMC12581463/)
- Slopes of the exponent over time compared (pre-ictal vs interictal). Delta-band Granger causality. Correlations with cortical thickness and receptor-density maps (spin permutation, 5,000 rotations). — [PMC12581463](https://pmc.ncbi.nlm.nih.gov/articles/PMC12581463/)

## Evaluation protocol
Group-level statistics (linear regression slope contrasts, Spearman with FDR). **No forecasting or classification, no pseudo-prospective test, no chance-level forecaster.** The authors state the markers are "candidate markers rather than established predictors." — [PMC12581463](https://pmc.ncbi.nlm.nih.gov/articles/PMC12581463/)

## Key results (numbers)
- The aperiodic exponent **rose progressively** before seizures, meaning a steeper spectrum, interpreted as a **shift toward inhibition**. The pre-ictal slope was steeper than interictal in epileptic regions (t = 2.032, p = 0.046) and non-epileptic regions (t = 6.94, p < 0.001). There was no difference between epileptic and non-epileptic regions (t = 1.38, p = 0.16), so the change is **global**. The rise was concentrated in the final pre-ictal phase. — [PMC12581463](https://pmc.ncbi.nlm.nih.gov/articles/PMC12581463/)
- Pre-ictal theta increased (epileptic t = 3.50, p < 0.001; non-epileptic t = 6.50, p < 0.001), and delta increased in non-epileptic regions (t = 3.44, p = 0.001). — [PMC12581463](https://pmc.ncbi.nlm.nih.gov/articles/PMC12581463/)
- Epileptic regions showed more outward than inward delta Granger connections (t = 2.12, p = 0.042). — [PMC12581463](https://pmc.ncbi.nlm.nih.gov/articles/PMC12581463/)
- Exponent correlated with cortical thickness in non-epileptic regions (rho = 0.21, p <= 0.001) but not epileptic regions (rho = -0.04, p = 0.61). Muscarinic receptor density correlated negatively with the pre-ictal exponent (rho = -0.433, p = 0.013, FDR-surviving). — [PMC12581463](https://pmc.ncbi.nlm.nih.gov/articles/PMC12581463/)

## Limitations
Small retrospective cohort (20 patients, 29 seizures). Heterogeneous seizures. Sleep/wake could not be controlled. The aperiodic exponent is not a pure E/I measure. No predictive validation. — [PMC12581463](https://pmc.ncbi.nlm.nih.gov/articles/PMC12581463/)

## Relevance to our project
- This is the **most directly transferable paper to TUSZ**: scalp EEG, minutes-scale pre-ictal window, and an E/I proxy computable with specparam/FOOOF on standard montages.
- Sign convention matters. Here the exponent **increases**, a shift toward inhibition, before seizures. A naive "E/I shifts toward excitation before seizures" hypothesis is not what this data shows. Our neural mass model E/I estimates should be checked for consistency with the aperiodic exponent.
- Confounders we must control on TUSZ: sleep stage and drowsiness (which also steepen the spectrum), and artifacts (EMG flattens the high-frequency spectrum). A 60-s window with 90% overlap is a reasonable starting setting.
- TUSZ uses about 19-21 channels (10-20 system), not 128, so source reconstruction will be crude. Sensor-level exponents are the pragmatic choice.
