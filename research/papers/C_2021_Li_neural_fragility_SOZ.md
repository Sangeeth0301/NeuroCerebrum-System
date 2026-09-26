# Li et al. 2021 — Neural fragility as an EEG marker of the seizure onset zone

## Citation & Link
- Adam Li, Chester Huynh, Zachary Fitzgerald, Iahn Cajigas, Damian Brusko, Jonathan Jagid, Angel O. Claudio, Andres M. Kanner, Jennifer Hopp, Stephanie Chen, Jennifer Haagensen, Emily Johnson, William Anderson, Nathan Crone, Sara Inati, Kareem A. Zaghloul, Juan Bulacio, Jorge Gonzalez-Martinez, Sridevi V. Sarma. "Neural fragility as an EEG marker of the seizure onset zone." *Nature Neuroscience* 24:1465–1474, 2021. DOI: 10.1038/s41593-021-00901-w — metadata https://api.semanticscholar.org/graph/v1/paper/10.1038/s41593-021-00901-w
- Open access (PMC8547387): https://pmc.ncbi.nlm.nih.gov/articles/PMC8547387/
- Semantic Scholar lists year 2019 because a bioRxiv preprint appeared first; journal publication is 2021 (volume/pages from memory — verify).

## Venue type
Peer-reviewed journal (Nature Neuroscience). Intracranial EEG (not scalp). Numbers via PMC full text extraction and abstract.

## Problem
No validated EEG biomarker of the SOZ; surgical success 30–70%. Propose a network-dynamics marker ("neural fragility") that localizes the SOZ and tracks how it evolves around seizure onset. — https://api.semanticscholar.org/graph/v1/paper/10.1038/s41593-021-00901-w

## Dataset
91 patients, 5 centres (JHH, NIH, Cleveland Clinic, UMMC, U. Miami), 462 seizures, ECoG or SEEG; 44 successful and 47 failed surgical outcomes. Raw iEEG shared on OpenNeuro in BIDS-iEEG format. — https://pmc.ncbi.nlm.nih.gov/articles/PMC8547387/

## Approach
- Fit a **linear time-varying network model** x(t+1) = A x(t) in sliding windows (250 ms, 125 ms step).
- Node fragility = minimum-norm perturbation of that node's connections that destabilizes the network; yields a **channel × time fragility heatmap** around electrographic onset that visualizes where instability starts and how it spreads.
- Random Forest on fragility distributions of clinically annotated SOZ vs non-SOZ predicts surgical outcome (proxy for whether the fragile region = removed region). — https://pmc.ncbi.nlm.nih.gov/articles/PMC8547387/

## Evaluation protocol
Outcome prediction with cross-validation across patients (details in paper; not verified whether folds were stratified by centre). Compared against 20 features (6 spectral bands, 14 graph-theoretic measures). Leakage risk low (patient-level outcome labels), but only indirect SOZ validation.

## Key results (numbers)
- Fragility predicts **43 of 47 surgical failures**; overall accuracy **76%** vs clinicians **48%** (abstract) — https://api.semanticscholar.org/graph/v1/paper/10.1038/s41593-021-00901-w (full-text extraction gave clinical baseline ≈47%; minor discrepancy).
- AUC **0.88±0.064** vs 0.82 for next-best feature; PPV 0.903±0.103; NPV 0.872±0.136; Cohen's d = 1.507. — https://pmc.ncbi.nlm.nih.gov/articles/PMC8547387/
- In failed outcomes, fragile regions that were left untreated were identified. — abstract

## Limitations
Retrospective; needs prospective validation; invasive iEEG only; small per-centre samples; linear model; validation via outcomes rather than direct SOZ truth. — https://pmc.ncbi.nlm.nih.gov/articles/PMC8547387/

## Relevance to our project
- Supplies an interpretable, **connectivity/dynamics-based spread map** (channel × time heatmap) that could be computed on scalp EEG windows as an unsupervised complement to a learned spread map (applicability to scalp EEG is untested in this paper).
- Its public multi-centre iEEG data (OpenNeuro) could be used to validate onset-localization methods against clinical SOZ labels.
- Not a type-classification paper; serves the "where it starts and how it spreads" half of our project.
