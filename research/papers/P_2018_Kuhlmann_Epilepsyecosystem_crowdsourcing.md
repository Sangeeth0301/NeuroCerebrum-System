# P_2018_Kuhlmann: Epilepsyecosystem.org, crowd-sourcing reproducible seizure prediction with long-term human iEEG (Brain 2018)

## Citation & Link
Kuhlmann L., Karoly P., Freestone D.R., Brinkmann B.H., et al. (25 authors in total). "Epilepsyecosystem.org: crowd-sourcing reproducible seizure prediction with long-term human intracranial EEG." *Brain* 141(9):2619–2630, 2018. DOI: 10.1093/brain/awy210. PMID 30101347. PMCID PMC6136083.
- Europe PMC lists these first four authors plus "21 additional authors". The full author list was not retrieved.
- Journal page: https://academic.oup.com/brain/article/141/9/2619/5066003
- Open-access full text: https://europepmc.org/articles/PMC6136083 (PDF: https://europepmc.org/articles/PMC6136083?pdf=render)
- PubMed: https://pubmed.ncbi.nlm.nih.gov/30101347/
- Metadata and abstract source: [Europe PMC API](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1093/brain/awy210&resultType=core&format=json)

## Venue type
Peer-reviewed journal (*Brain*, Oxford University Press), open access in PMC. It is included here as the **evaluation-standard reference** for prediction. It is an iEEG study, **not scalp EEG**.
- **Most numbers below come from the abstract.** Full-text retrieval was blocked (PMC captcha, Europe PMC HTTP 500/403). A summary of the OUP full-text page supplied the winning-feature details.

## Problem
Seizure prediction algorithms are usually built on small, short datasets and are rarely reproduced. The question is whether crowd-sourcing on high-quality long-term data yields algorithms that generalize to held-out data. The paper also tests whether "prediction-resistant" patients from the NeuroVista trial can in fact be predicted. [Europe PMC abstract](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1093/brain/awy210&resultType=core&format=json)

## Dataset
- **Long-term continuous iEEG from the NeuroVista Seizure Advisory System trial.** The patients were those with the **lowest** prediction performance in the original clinical trial. [Abstract](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1093/brain/awy210&resultType=core&format=json)
- The contest used 3 patients. [OUP](https://academic.oup.com/brain/article/141/9/2619/5066003)
- The abstract's phrase "442 days of recordings and 211 lead seizures per patient" is ambiguous. Read it as averages or totals and check the full text. [Abstract](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1093/brain/awy210&resultType=core&format=json)
- Recording set-up: 16 channels (4×4 strip electrodes on the focal hemisphere), 400 Hz. [Barachant challenge write-up](https://alexandre.barachant.org/challenges/06-kaggle-seizure-predictions/)
- Task framing: distinguish **10-min clips** of preictal vs inter-seizure data. The one-hour preictal period is split into six 10-min clips. [Abstract](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1093/brain/awy210&resultType=core&format=json); [Barachant](https://alexandre.barachant.org/challenges/06-kaggle-seizure-predictions/)

## Approach
- **Crowd-sourcing ecosystem** with three parts. [Abstract](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1093/brain/awy210&resultType=core&format=json)
  1. The Kaggle "Melbourne-University AES-MathWorks-NIH Seizure Prediction Challenge".
  2. A follow-up evaluation of the top algorithms on a **much larger held-out dataset**.
  3. The **Epilepsyecosystem.org** platform, which keeps benchmarking new algorithms.
- **Winning methods:**
  - The first-place entry used hand-crafted features: spectral power, distribution statistics, AR error, fractal dimensions, Hurst exponent and others.
  - It combined several classifiers by rank averaging.
  - Tree ensembles such as XGBoost were more common than in earlier contests.

  [OUP page summary](https://academic.oup.com/brain/article/141/9/2619/5066003)
- **Pseudo-prospective evaluation:** algorithm outputs are used alone or **weighted by circadian information** and compared with the original trial's performance at matched time in warning. [Abstract](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1093/brain/awy210&resultType=core&format=json)

## Evaluation protocol
- The contest metric is **clip-level AUC** on preictal vs interictal 10-min clips, scored on public and private leaderboards.
- The top algorithms were then re-run on held-out data from the same patients (a reproducibility check).
- The pseudo-prospective analysis reports **sensitivity at matched time-in-warning**, compared with the NeuroVista trial benchmark.

  [Abstract](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1093/brain/awy210&resultType=core&format=json)
- **Leakage lesson for our project:** clip-level random splits of adjacent 10-min clips from the same hour inflate AUC. The paper's key message is that **held-out, time-separated evaluation** is required. The exact contest-leakage details were not verified in the full text.

## Key results (numbers)
All numbers are **abstract-only**. [Europe PMC abstract](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1093/brain/awy210&resultType=core&format=json)

| Item | Value |
|---|---|
| Participants | 646 individuals in 478 teams |
| Algorithm submissions | 10,082 (>10,000) |
| Top contest AUC | **0.81** |
| Drop on held-out data | only **6.7%** |
| Pseudo-prospective | average sensitivity **1.9×** the original NeuroVista trial sensitivity at matched time in warning |
| Conclusion | different algorithms were best for different patients, which supports patient-specific algorithms and long-term monitoring |

## Limitations
- Intracranial, implanted-device data from 3 contest patients. It does not transfer directly to scalp EEG.
- The AUC metric is clip-level. Clinical metrics (sensitivity / time in warning) appear only in the pseudo-prospective part.
- Algorithms were best for different patients, so no single universal model emerged.

## Relevance to our project
- Use it as the **methodological yardstick** for our TUSZ project:
  - report AUC **and** event-level sensitivity and FPR/h or time-in-warning;
  - evaluate on time-separated held-out data;
  - compare against a chance or circadian benchmark.
- It shows that **feature-engineered gradient-boosted ensembles** were competitive with deep models in the most rigorous prediction contest. An XGBoost-on-spectral-features baseline is therefore mandatory for our TUSZ comparison.
- TUSZ lacks the months-long continuous recordings that made the held-out and pseudo-prospective analysis possible. This is a structural limitation to state explicitly in our project.
