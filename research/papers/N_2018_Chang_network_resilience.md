# Loss of neuronal network resilience precedes seizures and determines the ictogenic nature of interictal synaptic perturbations (Chang et al., 2018)

## Citation & Link
Chang WC, Kudlacek J, Hlinka J, Chvojka J, Hadrava M, Kumpost V, Powell AD, Janca R, Maturana MI, Karoly PJ, Freestone DR, Cook MJ, Palus M, Otahal J, Jefferys JGR, Jiruska P. "Loss of neuronal network resilience precedes seizures and determines the ictogenic nature of interictal synaptic perturbations." *Nature Neuroscience* 21:1742-1752 (2018). (The full author list is from memory; the first three authors and the title are confirmed in [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22Loss%20of%20neuronal%20network%20resilience%20precedes%20seizures%22&resultType=core&format=json).)
- DOI: https://doi.org/10.1038/s41593-018-0278-y
- Author manuscript (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC7617160/
- Note: the title in the literature-review brief ("...in chronic epilepsy") is not the exact title. The correct title is given above.

## Venue type
Peer-reviewed journal (Nature Neuroscience). The paper is mainly mechanistic, with a human proof of concept, and does not propose a forecasting algorithm.

## Problem
Is the transition to seizure sudden, or a slow loss of resilience governed by critical slowing? And why do interictal epileptiform discharges (IEDs) sometimes prevent and sometimes trigger seizures? — [PMC7617160](https://pmc.ncbi.nlm.nih.gov/articles/PMC7617160/)

## Dataset
- In vitro: rat hippocampal slices perfused with high K+ (8-10 mM). 73 isolated CA1 slices and 67 intact hippocampal slices; for example, 114 seizures across 17 isolated CA1 slices and 83 seizures across 15 intact slices. — [PMC7617160](https://pmc.ncbi.nlm.nih.gov/articles/PMC7617160/)
- In vivo: tetanus toxin model of temporal lobe epilepsy (6 Wistar rats), with hippocampal and motor cortex depth electrodes. — [PMC7617160](https://pmc.ncbi.nlm.nih.gov/articles/PMC7617160/)
- Human: NeuroVista intracranial data, 12 patients with more than 10 seizures, 16 electrodes at 400 Hz, 1,890 preictal periods. — [PMC7617160](https://pmc.ncbi.nlm.nih.gov/articles/PMC7617160/)

## Approach
- Early-warning signals of CSD: variance, autocorrelation (lag 5 ms in slices), spectral slowing (first spectral moment in the 100-500 Hz band), spatial correlation, and firing rates. Active probing: Schaffer collateral stimulation to measure how the network responds to perturbations. — [PMC7617160](https://pmc.ncbi.nlm.nih.gov/articles/PMC7617160/)
- Modelling: a slow-fast dynamical model and a modified **Epileptor** reproduce the state-dependent pro- and anti-seizure effects of perturbations. — [PMC7617160](https://pmc.ncbi.nlm.nih.gov/articles/PMC7617160/)

## Evaluation protocol
Statistical comparison of early vs late interictal periods (ANOVA and Mann-Whitney tests). There was no forecasting evaluation, no pseudo-prospective test, and no chance-level forecaster. — [PMC7617160](https://pmc.ncbi.nlm.nih.gov/articles/PMC7617160/)

## Key results (numbers)
- Isolated CA1: progressive increase in variance (n = 76 interictal periods / 17 slices, F(1,7500) = 154, P < 0.001) and in autocorrelation (F(1,7500) = 1821, P < 0.001). — [PMC7617160](https://pmc.ncbi.nlm.nih.gov/articles/PMC7617160/)
- Interictal period: 69.8 +/- 2.1 s in intact slices vs 50.3 +/- 2.4 s in isolated CA1. Blocking IEDs (NBQX + APV) shortened the interictal period from 53.6 +/- 2.1 to 41.4 +/- 2.3 s, meaning IEDs had a net anti-seizure effect early in the cycle. — [PMC7617160](https://pmc.ncbi.nlm.nih.gov/articles/PMC7617160/)
- Stimulation early in the interictal period triggered seizures in 38% of trials (300 uA), versus 100% late. The same perturbation is pro-ictal only when the network is near the transition. — [PMC7617160](https://pmc.ncbi.nlm.nih.gov/articles/PMC7617160/)
- Rat in vivo: changes developed over inter-cluster periods of about 2.7 +/- 0.2 h. — [PMC7617160](https://pmc.ncbi.nlm.nih.gov/articles/PMC7617160/)
- **Human: only 4/12 patients showed a significant increase in lag-1 autocorrelation in the 30 min before seizures, and 4 showed decreases.** In 4/13 patients, "heralding" spikes matched earlier IED morphology at more than 98%. — [PMC7617160](https://pmc.ncbi.nlm.nih.gov/articles/PMC7617160/)

## Limitations
Mostly acute high-K+ preparations. Human results are heterogeneous (only a third of patients show the expected CSD direction). Timescales differ across preparations (seconds, hours, and 30-min windows). Causal inference is limited. — [PMC7617160](https://pmc.ncbi.nlm.nih.gov/articles/PMC7617160/)

## Relevance to our project
- This paper gives the mechanistic rationale for CSD-based features (variance, autocorrelation, spectral slowing) and for treating **IED rate as a state-dependent feature** rather than a simple risk indicator.
- The human results are a warning: at the minutes-to-30-min scale, CSD in autocorrelation was not consistent (4 up, 4 down out of 12). On TUSZ we should expect patient-specific directions and test effects per patient with surrogates, not assume a universal increase.
- Its use of a modified Epileptor supports the use of neural mass or phenomenological models to explain preictal changes.
