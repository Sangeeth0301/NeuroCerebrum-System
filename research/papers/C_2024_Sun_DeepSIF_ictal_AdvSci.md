# Sun et al. 2024 (Advanced Science) — Seizure sources imaged from scalp EEG with biophysically constrained DNNs (ictal DeepSIF)

## Citation & Link
- Rui Sun, Abbas Sohrabpour, Boney Joseph, Gregory Worrell, Bin He. "Seizure Sources Can Be Imaged from Scalp EEG by Means of Biophysically Constrained Deep Neural Networks." *Advanced Science* 11(47), 2024. DOI: 10.1002/advs.202405246 — https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202405246
- Open access (PMC11653641): https://pmc.ncbi.nlm.nih.gov/articles/PMC11653641/

## Venue type
Peer-reviewed journal (Advanced Science, Wiley). Numbers read via the PMC full text (through an extraction tool).

## Problem
Extend DeepSIF (PNAS 2022, interictal spikes) to **ictal** EEG: noninvasively image where seizures originate, as an alternative/complement to invasive iEEG in drug-resistant focal epilepsy. — https://pmc.ncbi.nlm.nih.gov/articles/PMC11653641/

## Dataset
- 33 drug-resistant focal epilepsy patients (20 F; 32±14 y), **76-channel** high-density scalp EEG (10-10); 29 had iEEG implantation (16 with CT electrode localization); 27 had post-op MRI; 21 seizure-free (ILAE 1–2). — https://pmc.ncbi.nlm.nih.gov/articles/PMC11653641/
- Training data: ~1.24 M synthetic samples from a modified Jansen–Rit neural mass model generating six ictal patterns (background, sporadic spikes, sustained discharges, rhythmic activity, low-voltage fast activity, quasi-sinusoidal), SNR 5–20 dB; template fsaverage5 head, 994 cortical regions, 3-shell BEM. — https://pmc.ncbi.nlm.nih.gov/articles/PMC11653641/

## Approach
Spatial pre-filtering module + temporal module with recurrent layers and skip connections (DeepSIF), trained on simulated ictal source–sensor pairs, applied to the early ictal segment of recorded seizures. Benchmarked against sLORETA, FDI, LCMV beamformer. — https://pmc.ncbi.nlm.nih.gov/articles/PMC11653641/

## Evaluation protocol
Imaged ictal source vs. resection volume (sensitivity/specificity, dispersion) and vs. iEEG-defined SOZ electrodes (distance); also ictal vs interictal-spike imaging within the same patients. Trained entirely on simulations → no patient leakage; template head model.

## Key results (numbers)
From https://pmc.ncbi.nlm.nih.gov/articles/PMC11653641/
- Simulation: spatial specificity 0.98±0.03; temporal correlation 0.98±0.04 / 0.92±0.07; LE ≈ 1.34–1.35 mm.
- Patients: spatial specificity reported as "0.96 ± 0.90" by the extraction tool (the SD is implausible for a proportion; likely 0.96±0.09 — **verify in the PDF**); spatial dispersion **3.80±5.74 mm**; SOZ distance **10.89±10.14 mm** (all patients with iEEG) and **8.03±9.01 mm** in seizure-free patients (n=9); temporal correlation with EEG 0.81±0.14.
- Geometric mean of sensitivity & specificity **0.62±0.22** vs 0.47–0.60 for sLORETA/FDI/LCMV.
- Ictal imaging significantly better than interictal spike imaging, especially in non-seizure-free patients.

## Limitations
Template (not individual) head model; the ictal source model focuses on the **early seizure stage and excludes propagation**; resection is an imperfect ground truth; single centre; piece-wise stationarity assumption. — https://pmc.ncbi.nlm.nih.gov/articles/PMC11653641/

## Relevance to our project
- Directly addresses **onset-zone localization from scalp ictal EEG** with quantitative validation against iEEG SOZ (~1 cm error), setting a realistic accuracy target for any "where did it start" output.
- Explicitly does *not* model propagation — a gap our spread-map component could target (e.g., apply per-window source/channel saliency across the seizure).
- Requires 76-ch EEG and synthetic training; for TUSZ (19-ch) we would likely use channel/lobe-level mapping instead.
