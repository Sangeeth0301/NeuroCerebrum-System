# Craley et al. 2022 — SZTrack: automated seizure activity tracking and onset-zone localization from scalp EEG

## Citation & Link
- Jeff Craley, Christophe Jouny, Emily Johnson, David Hsu, Raheel Ahmed, Archana Venkataraman (Johns Hopkins / collaborators). "Automated seizure activity tracking and onset zone localization from scalp EEG using deep neural networks." *PLoS ONE* 17(2): e0264537, 2022. DOI: 10.1371/journal.pone.0264537 — https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0264537
- Open access (PMC8884583): https://pmc.ncbi.nlm.nih.gov/articles/PMC8884583/
- Code (lab links page): https://engineering.jhu.edu/nsa/links/
- (Author list beyond Craley, Jouny, Johnson, Venkataraman taken from memory of the paper; the search result listed "J. Craley, C. Jouny, E. Johnson, and A. Venkataraman" — verify full author list on the PLoS page.)

## Venue type
Peer-reviewed journal (PLoS ONE, open access). Numbers from PMC full text via extraction tool.

## Problem
Track the spatio-temporal **evolution/spread** of seizure activity across scalp channels and localize the onset zone (hemisphere and lobe), trained only with coarse clinical annotations. Described as the first end-to-end seizure-tracking network for scalp EEG. — https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0264537

## Dataset
- **JHH** (private): 201 seizures from 34 focal epilepsy patients, 6–77 y, 10-20 montage, 200 Hz; ~5.9 seizures/patient; mean seizure 112 s. — https://pmc.ncbi.nlm.nih.gov/articles/PMC8884583/
- **UWM** (private, external test): 53 seizures from 15 pediatric patients (8–17 y), 256 → 200 Hz. — https://pmc.ncbi.nlm.nih.gov/articles/PMC8884583/
- Labels: seizure start/end plus coarse clinical SOZ (hemisphere; lobe / anterior–posterior). Focal epilepsy only; no seizure-type labels. Data not public (IRB).

## Approach
- **Channel-wise 1-D CNN encoder** (shared across electrodes) → **recurrent layers** per channel to model temporal evolution → per-channel, per-time seizure-activity probabilities (the "tracking" map).
- Global detection = max-pool across channels; onset localization = onset-weighted aggregation of channel activations, trained against hemisphere/lobe partitions of the electrodes (weak supervision from coarse labels). — https://pmc.ncbi.nlm.nih.gov/articles/PMC8884583/

## Evaluation protocol
- **Leave-one-patient-out CV** (patient-wise; no leakage) on JHH; UWM used as an external site without retraining. — https://pmc.ncbi.nlm.nih.gov/articles/PMC8884583/
- Training on ±2 min around seizures; evaluation on full 20-min recordings.

## Key results (numbers)
From https://pmc.ncbi.nlm.nih.gov/articles/PMC8884583/
- Detection (JHH): AUROC **0.895±0.112** (CNN-BLSTM baseline 0.899); seizure-level sensitivity 0.865; 13.05 FP/h.
- Localization (JHH): lateralization accuracy **0.826**; **hemisphere and lobe both correct in 21/34 patients**; at least one of hemisphere/lobe correct in all 34.
- External UWM: AUROC 0.813 without retraining; both partitions correct in **8/15** patients; 5 more with one correct.
- Propagation: qualitative channel-by-time activity maps show seizure spread; no quantitative propagation-accuracy metric (no ground-truth spread labels).

## Limitations
Slightly worse detection than CNN-BLSTM; poor anterior–posterior discrimination (class imbalance); coarse partitions fail for fronto-temporal onsets; small private datasets; clinical validation needed. — https://pmc.ncbi.nlm.nih.gov/articles/PMC8884583/

## Relevance to our project
- **Closest existing design to our "spread map"**: per-channel activity over time from scalp EEG, weakly supervised, patient-wise evaluated. We can reuse its architecture (shared channel encoder + RNN) on TUSZ, whose v1.5.x releases include channel-level annotations (used by Tang et al. 2022 for localization scoring — https://arxiv.org/pdf/2104.08336).
- Onset hemisphere/lobe accuracy (21/34 fully correct) is a realistic benchmark for scalp-only onset localization.
- Combine with a type classifier: shared channel embeddings → (a) per-channel spread map, (b) pooled type-at-onset head.
