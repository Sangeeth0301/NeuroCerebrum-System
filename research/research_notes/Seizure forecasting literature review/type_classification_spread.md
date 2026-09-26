# Seizure-type classification (TUSZ) and onset-zone localization / spread mapping from EEG

Per-paper files: `research/papers/C_*.md` (8 files: Tang 2022, Asif/Roy SeizureNet 2020 (+2019 benchmark), Raghu 2020, Ahmedt-Aristizabal 2020, Sun 2022 PNAS DeepSIF, Sun 2024 Adv Sci ictal DeepSIF, Craley 2022 SZTrack, Li 2021 neural fragility).

## Comparison table

| Paper | Venue (type) | Data | Split (leakage) | Input / model | Headline result |
|---|---|---|---|---|---|
| Tang et al. 2022 | ICLR (conf.) | TUSZ v1.5.2, 19 ch, 4 classes CF/GN/AB/CT | Patient-wise, official test set minus 5 overlapping patients (clean) | log-FFT; distance or correlation graph; DCRNN + self-supervised next-12-s prediction; occlusion localization | wF1 0.749 (60-s), 0.746 (12-s); det. AUROC 0.875; 25.4% focal seizures precisely localized — [arXiv](https://arxiv.org/pdf/2104.08336) |
| Asif, Roy et al. 2020 SeizureNet | MICCAI workshop (LNCS) | TUSZ v1.4/1.5.2, 7 types, IBM preprocessing | Seizure-wise (leaky) + patient-wise | Multi-spectral CNN ensemble + distillation | wF1 0.95–0.98 seizure-wise vs **0.62 patient-wise** — [S2](https://www.semanticscholar.org/paper/SeizureNet:-Multi-Spectral-Deep-Feature-Learning-Asif-Roy/15b8ba09bd4193cec0c17e9d669267d58ed5afc4), [Tang T3](https://arxiv.org/pdf/2104.08336) |
| Roy et al. 2019 benchmark | arXiv **preprint** | TUSZ, 7 types | Seizure-wise (inferred) | FFT features + k-NN/XGBoost/CNN | wF1 up to 0.907 (abstract) — [arXiv](https://arxiv.org/abs/1902.01012) |
| Raghu et al. 2020 | Neural Networks (journal) | TUSZ (v1.4.0 per secondary source), 7 types + non-seizure | Not verified (likely not patient-wise) | STFT spectrogram stack; 10 ImageNet CNNs; fine-tune or features+SVM | Acc. 82.85% (GoogLeNet TL), 88.30% (InceptionV3+SVM) — abstract only — [S2](https://api.semanticscholar.org/graph/v1/paper/10.1016/j.neunet.2020.01.017) |
| Ahmedt-Aristizabal et al. 2020 | IEEE EMBC (conf.) | TUSZ v1.4.0, 7 types, IBM 1-s FFT windows | Random 60/20/20 per-window split (severe leakage) | LSTM + plastic neural memory network | wF1 0.945 — [arXiv](https://arxiv.org/pdf/1912.04968) |
| Sun et al. 2022 DeepSIF | PNAS (journal) | Synthetic training; 20 patients, 76-ch interictal spikes | Train on simulation, test on patients | NMM-simulated data → spatial+temporal DNN, 994 regions | Precision 0.79, recall 0.49 vs resection; SOZ error 7.45±8.91 mm (n=6) — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9351497/) |
| Sun et al. 2024 ictal DeepSIF | Advanced Science (journal) | 33 patients, 76-ch **ictal** scalp EEG, iEEG/resection truth | Simulation-trained | Jansen–Rit ictal simulations → DeepSIF | SOZ distance 10.89±10.14 mm (8.03±9.01 seizure-free); dispersion 3.80±5.74 mm — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11653641/) |
| Craley et al. 2022 SZTrack | PLoS ONE (journal) | 34 pts/201 seizures (JHH) + 15 pts (UWM), 10-20 | Leave-one-patient-out + external site | Channel-wise CNN + RNN → per-channel activity over time; weak onset supervision | Hemisphere+lobe correct in 21/34; lateralization 0.826; AUROC 0.895 — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8884583/) |
| Li et al. 2021 neural fragility | Nature Neuroscience (journal) | 91 pts, 462 seizures, iEEG, 5 centres | Patient-level outcome prediction | LTV network model, node fragility heatmap | Outcome AUC 0.88; accuracy 76% vs clinicians 48% — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8547387/) |

## How well can seizure type be classified on TUSZ, and how much do splits matter?

### Takeaway
With patient-independent evaluation, TUSZ type classification sits around weighted F1 ≈ 0.62–0.65 (7 classes) and ≈ 0.75 (4 merged classes); the 0.90–0.98 figures in the literature come from seizure- or window-wise splits that leak patient identity.

### Cited Findings
- Tang et al. (ICLR 2022), TUSZ v1.5.2, patient-wise: best 4-class wF1 0.749 (60-s) and 0.746 (12-s) with self-supervised pre-training; without pre-training 0.690–0.710 — [Tang](https://arxiv.org/pdf/2104.08336)
- Same paper, 7-class, 3-fold patient-wise: Corr-DCRNN 0.650 vs SeizureNet 0.62 — [Tang](https://arxiv.org/pdf/2104.08336)
- SeizureNet reports wF1 0.95 seizure-wise vs 0.62 patient-wise; another version claims 0.98 — [Semantic Scholar](https://www.semanticscholar.org/paper/SeizureNet:-Multi-Spectral-Deep-Feature-Learning-Asif-Roy/15b8ba09bd4193cec0c17e9d669267d58ed5afc4), [arXiv](https://arxiv.org/abs/1903.03232)
- Ahmedt-Aristizabal et al. split 1-s (75%-overlap) windows randomly 60/20/20 per seizure type and report wF1 0.945 — [arXiv](https://arxiv.org/pdf/1912.04968); a CNN-LSTM "implemented following" them scores only 0.633/0.641 under Tang's patient-wise protocol — [Tang](https://arxiv.org/pdf/2104.08336)
- Roy et al. 2019 benchmark (preprint): wF1 up to 0.907 — [arXiv](https://arxiv.org/abs/1902.01012)
- Raghu et al. 2020: 82.85% / 88.30% accuracy, 8 classes including non-seizure — abstract only — [S2](https://api.semanticscholar.org/graph/v1/paper/10.1016/j.neunet.2020.01.017)

### Inferences
- The seizure-wise → patient-wise drop of ~0.33 wF1 (SeizureNet) is the best available quantification of patient leakage on TUSZ; any project claim should be patient-wise and compared with Tang (0.749/4-class) and 0.62–0.65 (7-class).
- Accuracy-based results (Raghu) are not comparable to wF1-based results.

### Gaps
- Raghu et al. split protocol and per-class metrics: full text not accessible (ScienceDirect/PubMed blocked).
- SeizureNet LNCS final-version numbers and fold details not read; which arXiv version corresponds to the published paper is unresolved.
- No paper here reports per-class F1 numerically under patient-wise splits (Tang gives per-class AUROC and confusion-matrix accuracies only).

## How are rare seizure types and label issues handled?

### Takeaway
Most papers drop myoclonic (3 events); Tang merges FN+SP+CP → CF and TN+TC → CT, arguing SP vs CP is not EEG-distinguishable, and shows self-supervised pre-training lifts rare CT accuracy by 47 points; TUSZ also contains mislabeled GN seizures.

### Cited Findings
- TUSZ v1.4.0 counts: SPSZ 44 seizures from 2 patients; TNSZ 67 from 2 patients; ABSZ 99 from 12; TCSZ 50 from 11; myoclonic 3 events (excluded) — [Ahmedt-Aristizabal](https://arxiv.org/pdf/1912.04968)
- Tang: 4 classes CF/GN/AB/CT; train CT only 48 seizures (11 patients), test CT 61 seizures (4 patients); pre-training → 74% CT accuracy (+47 pts vs Dense-CNN) — [Tang](https://arxiv.org/pdf/2104.08336)
- Neurologist review of 32 misclassified test GN seizures: 27 were actually focal — [Tang](https://arxiv.org/pdf/2104.08336)

### Inferences
- A clinically meaningful at-onset target for our project is focal vs generalized (plus AB/CT subtypes), mirroring Tang's scheme; 2-patient classes cannot be evaluated patient-wise.

### Gaps
- No reviewed paper uses the newer TUSZ v2.x releases; class counts there were not checked.

## What approaches exist for onset-zone localization and spread mapping, and how accurate are they?

### Takeaway
Three families: (1) saliency/occlusion maps from type/detection models on scalp channels (Tang: 25.4% focal seizures precisely localized); (2) weakly supervised per-channel tracking networks (SZTrack: hemisphere+lobe correct in 21/34 patients); (3) source imaging (DeepSIF: ~0.8–1.1 cm from iEEG SOZ using 76-ch EEG) and iEEG network-dynamics markers (neural fragility, AUC 0.88 for outcome).

### Cited Findings
- Tang: occlusion coverage/localization vs TUSZ channel annotations; localization > 0.8 for 25.4% (Corr-DCRNN pre-trained) vs 3.5% (Dense-CNN) of focal seizures; correlation graph localizes better than distance graph — [Tang](https://arxiv.org/pdf/2104.08336)
- SZTrack: LOPO-CV, lateralization 0.826, hemisphere+lobe 21/34 (JHH), 8/15 external (UWM); per-channel activity maps show spread qualitatively — [PMC8884583](https://pmc.ncbi.nlm.nih.gov/articles/PMC8884583/)
- DeepSIF interictal: SOZ error 7.45±8.91 mm (n=6), precision 0.79, recall 0.49 vs resection — [PMC9351497](https://pmc.ncbi.nlm.nih.gov/articles/PMC9351497/)
- DeepSIF ictal: SOZ distance 10.89±10.14 mm; ictal imaging better than spike imaging; model excludes propagation — [PMC11653641](https://pmc.ncbi.nlm.nih.gov/articles/PMC11653641/)
- Neural fragility: channel×time fragility heatmaps (250 ms windows); predicts 43/47 failures; AUC 0.88 — [PMC8547387](https://pmc.ncbi.nlm.nih.gov/articles/PMC8547387/), [abstract](https://api.semanticscholar.org/graph/v1/paper/10.1038/s41593-021-00901-w)
- Search-result snippets misattribute the 2024 ictal numbers (3.80 mm, 10.89 mm) to the 2022 PNAS paper — compare [PMC9351497](https://pmc.ncbi.nlm.nih.gov/articles/PMC9351497/) and [PMC11653641](https://pmc.ncbi.nlm.nih.gov/articles/PMC11653641/)

### Inferences
- None of the reviewed papers quantitatively validates *propagation* (spread) maps; they validate onset location only. Our project could contribute a spread metric, e.g., per-window coverage/localization vs TUSZ channel annotations over time (extending Tang's metrics).
- For 19-channel TUSZ, a practical design is: shared channel encoder (SZTrack-style) on a correlation graph (Tang-style) → (a) pooled type-at-onset head, (b) per-channel activity-over-time spread map aggregated to lobes.

### Gaps
- No peer-reviewed paper found here that jointly does type classification and spread mapping.
- Validation of DeepSIF on 19-ch clinical montages (e.g., TUSZ) not reviewed; a 2025 Clin. Neurophysiol. study on electrode configurations exists — [PMC12629399](https://pmc.ncbi.nlm.nih.gov/articles/PMC12629399/) (not read).
- Newer (2023–2026) GNN type-classification papers on TUSZ (e.g., dynamic GNNs, [arXiv 2405.09568](https://arxiv.org/html/2405.09568v1), preprint) not assessed.
