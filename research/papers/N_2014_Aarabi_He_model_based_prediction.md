# Seizure prediction in hippocampal and neocortical epilepsy using a model-based approach (Aarabi & He, 2014) [FOUNDATIONAL / OLDER]

## Citation & Link
Aarabi A, He B. "Seizure prediction in hippocampal and neocortical epilepsy using a model-based approach." *Clinical Neurophysiology* 125(5):930-940 (2014). DOI (from memory, verify): 10.1016/j.clinph.2013.10.051
- PubMed: https://pubmed.ncbi.nlm.nih.gov/24374087/
- ScienceDirect: https://www.sciencedirect.com/science/article/abs/pii/S1388245713011942

Companion paper (not model-based): Aarabi A, He B. "Seizure prediction in patients with focal hippocampal epilepsy." *Clinical Neurophysiology* 128(7):1299-1307 (2017). DOI 10.1016/j.clinph.2017.04.026; PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC5513720/

**Source caveat:** I could not open the 2014 full text (PubMed returned a CAPTCHA, and ScienceDirect is paywalled). The 2014 numbers below come from a **search-result summary of the abstract** ([WebSearch snippet of PubMed/ScienceDirect](https://pubmed.ncbi.nlm.nih.gov/24374087/)) and should be checked against the paper.

## Venue type
Peer-reviewed journal (Clinical Neurophysiology). Older, foundational work, from before the field's shift to long-term pseudo-prospective evaluation.

## Problem
Can the parameters of a physiologically based neural mass model, fitted to iEEG, show pre-ictal changes that enable seizure prediction? — [PubMed 24374087](https://pubmed.ncbi.nlm.nih.gov/24374087/)

## Dataset
21 patients with medically intractable hippocampal or neocortical focal epilepsy, intracranial EEG. This appears to be the Freiburg iEEG database; that is my inference, not confirmed. — [PubMed 24374087](https://pubmed.ncbi.nlm.nih.gov/24374087/)

## Approach
Neural mass model (pyramidal cells plus excitatory and inhibitory interneurons, Jansen-Rit/Wendling family). **Twelve model parameters** were estimated by fitting the model to the **power spectral density** of iEEG windows. Pre-ictal parameter changes were then integrated into a prediction rule. — [PubMed 24374087](https://pubmed.ncbi.nlm.nih.gov/24374087/)

## Evaluation protocol
Standard seizure-prediction metrics of the era: sensitivity and false prediction rate per hour. From the available abstract, it is not clear whether a formal chance-level (random/periodic predictor) comparison or out-of-sample testing was used. **Treat as not pseudo-prospective.** — [PubMed 24374087](https://pubmed.ncbi.nlm.nih.gov/24374087/)

## Key results (numbers) — abstract/snippet only
- 2014 model-based: average sensitivity 87.07% and 92.6%, with average false prediction rate 0.2/h and 0.15/h (two operating settings/configurations). — [PubMed 24374087](https://pubmed.ncbi.nlm.nih.gov/24374087/) (abstract, via search snippet)
- 2017 companion (nonlinear measures such as correlation entropy, correlation dimension, Lempel-Ziv complexity, largest Lyapunov exponent, and nonlinear interdependence; **not** a neural mass model): 10 patients, 38 seizures, sensitivity 86.7% and 92.9%, FPR 0.126/h and 0.096/h, minimum prediction times 14.3 and 33.3 min. Two-thirds of seizures showed increased complexity before onset. — [PMC5513720](https://pmc.ncbi.nlm.nih.gov/articles/PMC5513720/) (abstract)

## Limitations
- Short-term iEEG (presurgical monitoring), few seizures per patient, and no reported long-term out-of-sample testing. An FPR of 0.15-0.2/h means about 3.6-4.8 false alarms per day, which is clinically high.
- Spectral fitting of a 12-parameter model is poorly identifiable (many parameter sets give similar spectra).

## Relevance to our project
- This is the closest precedent to our exact idea: **neural mass model parameters as pre-ictal features**. It shows the approach can separate pre-ictal from interictal windows in short-term iEEG, which resembles TUSZ-style short recordings, but on intracranial data.
- The PSD-fitting route (fit model spectrum to window spectrum) is simpler and more robust to implement than a Kalman filter. It is a sensible first baseline on scalp EEG, and it can be compared with the Karoly/Freestone Kalman tracking.
- We must evaluate more rigorously than this paper did: use held-out seizures/patients, report time-in-warning, and compare against a random predictor.
