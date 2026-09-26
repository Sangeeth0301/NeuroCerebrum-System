# Seizure pathways: A model-based investigation (Karoly et al., 2018)

## Citation & Link
Karoly PJ, Kuhlmann L, Soudry D, Grayden DB, Cook MJ, Freestone DR. "Seizure pathways: A model-based investigation." *PLoS Computational Biology* 14(10):e1006403 (2018).
- DOI: https://doi.org/10.1371/journal.pcbi.1006403
- Open access: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006403

## Venue type
Peer-reviewed journal (PLoS Computational Biology), open access.

**Scope note:** this paper tracks neural mass model parameters **during seizures** (onset to offset) and relates them to seizure duration. It is **not** a pre-seizure forecasting study. It is included because it is the most complete demonstration of Jansen-Rit parameter tracking with a Kalman-type filter on long-term human iEEG, which is the estimation machinery our project needs. — [PLoS CB](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006403)

## Problem
Can hidden connectivity (E/I) parameters of a neural mass model be inferred continuously from ECoG, and do seizures follow stereotyped "pathways" in parameter space that explain differences such as seizure duration? — [PLoS CB](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006403)

## Dataset
NeuroVista: 12 patients with focal epilepsy, 16 intracranial contacts, 400 Hz, multi-year recordings, 3,010 seizures (about 250 per patient). — [PLoS CB](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006403)

## Approach
- **Jansen-Rit** neural mass model with pyramidal, excitatory and inhibitory populations. Five time-varying parameters were estimated: external input u, inhibitory-to-pyramidal gain alpha_ip, excitatory-to-pyramidal alpha_ep, pyramidal-to-excitatory alpha_pe, and pyramidal-to-inhibitory alpha_pi. Time constants were fixed (10 ms; tau_ip = 20 ms), with sigmoid v0 = 6 mV. — [PLoS CB](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006403)
- Estimation used an **assumed-density (Kalman-type) filter** with an exact semi-analytic moment propagation through the sigmoid. States and parameters were estimated jointly at every sample, with parameters modelled as random walks and a linear observation model. Each channel was estimated independently. — [PLoS CB](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006403)
- Filter quality: MSE 0.2-0.9 mV (signals about 25-100 mV). Parameter covariance was 0.1-10% of estimates. Numerical instability occurred in less than 1% of the data. — [PLoS CB](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006403)

## Evaluation protocol
Descriptive and correlational. Parameter trajectories were aligned to onset and offset, clustered, and correlated with duration. There was no forecasting, no pseudo-prospective test, and no chance comparison. No ground truth exists for the parameters, so consistency across seizures served as a proxy. — [PLoS CB](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006403)

## Key results (numbers)
- Seizure parameter trajectories were **highly stereotyped** within patients across hundreds of seizures and across channels. Three patterns were found: connectivity decrease (patients 7, 10, 13), increase (patients 2, 4), and decrease-then-increase (patients 1, 3, 6, 8, 9, 15). — [PLoS CB](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006403)
- **Onset dynamics did not predict duration**: "Almost no patients showed significant correlation between seizure duration and onset dynamics." Long and short seizures began similarly and diverged later. — [PLoS CB](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006403)
- In the 5 s before offset, all five parameters correlated with duration. Longer seizures had more excitatory input and less inhibition to pyramidal cells. 3/12 patients had bimodal duration distributions. — [PLoS CB](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006403)
- Computational cost: 1.5 TB of estimates, with up to one week per patient for figures. — [PLoS CB](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006403)

## Limitations
No ground truth. Single-channel models ignore inter-regional coupling. High computational cost. Small cohort. Drug-mechanism interpretations are untested. — [PLoS CB](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006403)

## Relevance to our project
- This is the **methods template** for E/I parameter estimation: Jansen-Rit plus a joint state-parameter Kalman-type filter, running per channel on raw EEG. The fixed constants and the five-parameter choice can be reused.
- The key gap it leaves open is exactly our project's hypothesis. Karoly et al. did **not** test whether the parameters (for example alpha_ip, the inhibitory gain, or the E/I ratio alpha_ep/alpha_ip) drift in the **pre-ictal** period. We would be extending it to pre-ictal windows.
- Parameters are identifiable only up to the model's assumptions. Scalp EEG is a mixture of many sources, so we should report parameter stability (covariance) and verify with simulated data before interpreting E/I changes on TUSZ.
- A likely replacement or companion for forecasting: Kuhlmann/Freestone group papers on neural-mass tracking and Aarabi & He 2014 (see N_2014 file).
