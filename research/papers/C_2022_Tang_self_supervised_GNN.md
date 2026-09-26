# Tang et al. 2022 — Self-Supervised Graph Neural Networks for Improved EEG Seizure Analysis

## Citation & Link
- Siyi Tang, Jared A. Dunnmon, Khaled Saab, Xuan Zhang, Qianying Huang, Florian Dubost, Daniel L. Rubin, Christopher Lee-Messer (Stanford). "Self-Supervised Graph Neural Networks for Improved Electroencephalographic Seizure Analysis." ICLR 2022.
- arXiv (open access, v2 13 Mar 2022): https://arxiv.org/abs/2104.08336 — PDF: https://arxiv.org/pdf/2104.08336
- OpenReview: ICLR 2022 conference paper (forum ID not verified in this review; search the title on https://openreview.net)
- Code: https://github.com/tsy935/eeg-gnn-ssl (stated in the paper's reproducibility statement)
- No DOI (ICLR proceedings are published on OpenReview).

## Venue type
Peer-reviewed conference (ICLR 2022, main conference paper). All numbers below were read from the full text of the arXiv v2 PDF (camera-ready version, header "Published as a conference paper at ICLR 2022").

## Problem
Three gaps in seizure detection/type classification on scalp EEG: (1) CNNs treat EEG as Euclidean and ignore electrode geometry/connectivity; (2) rare seizure types are classified poorly; (3) no quantitative measure of whether a model can localize seizures in channels/time. Tasks: seizure detection (is there a seizure in a clip) and seizure type classification (given a seizure clip, which type), over 12-s ("fast") and 60-s ("slow") clips. — https://arxiv.org/pdf/2104.08336

## Dataset
- TUSZ **v1.5.2**: 5,612 EEGs, 3,050 annotated seizures, 8 seizure types; 19 channels of the 10-20 system. Study used 5,499 EEGs. — https://arxiv.org/pdf/2104.08336
- **Refined 4-class scheme**: FNSZ + SPSZ + CPSZ merged into Combined Focal (CF), because SP vs CP differ by consciousness (clinical), not EEG (Appendix C shows models cannot separate them); myoclonic excluded (only 3 seizures); tonic + tonic-clonic merged into Combined Tonic (CT) (only 18 TNSZ and 30 TCSZ in train). Final classes: CF, GN, AB, CT. Appendix L reports the original 8-type results. — https://arxiv.org/pdf/2104.08336
- Class counts (seizures / patients): Train CF 1,868/148, GN 409/68, AB 50/7, CT 48/11; Test CF 297/24, GN 114/11, AB 49/5, CT 61/4. — https://arxiv.org/pdf/2104.08336
- One 12-s (or 60-s) clip per seizure event for classification (so each clip has exactly one seizure type). — https://arxiv.org/pdf/2104.08336

## Approach
- **Input representation**: log-amplitude of FFT of raw EEG (frequency domain); ablation (App. B) shows frequency-domain inputs substantially beat time-domain. — https://arxiv.org/pdf/2104.08336
- **Graph construction** (two variants):
  - *Distance graph*: thresholded Gaussian kernel on Euclidean distance of standard 10-20 positions, W_ij = exp(-d²/σ²) if d ≤ κ, κ = 0.9 → one universal undirected graph resembling clinical bipolar montages.
  - *Correlation graph*: |normalized cross-correlation| between channels per clip, keep top-τ neighbours per node (+ self-edges) → per-clip directed graph (τ = 3 shown in example).
- **Model**: DCRNN (diffusion convolutional recurrent NN, originally for traffic forecasting): GRU whose matrix multiplications are replaced by bidirectional random-walk diffusion convolutions (directed corr. graph) or ChebNet convolutions (undirected dist. graph), stacked DCGRUs + FC layer.
- **Self-supervised pre-training**: seq2seq DCGRU encoder–decoder predicting the next T' = 12 s of preprocessed EEG, MAE loss; uses abundant non-seizure data; encoder weights initialise detection/classification models.
- **Localization / interpretability**: occlusion maps. For detection: zero-fill 1 s of one channel at a time → map M ∈ R^{N×T}; compare with TUSZ channel-level annotations using *coverage* (recall-like) and *localization* (precision-like) scores at threshold 0.5. For classification: drop one entire channel at a time. — https://arxiv.org/pdf/2104.08336

## Evaluation protocol
- **Patient-wise**: official TUSZ train split randomly divided by patient 90/10 into train/val; official TUSZ test set held out; 5 patients present in both official train and test sets were *removed from the test set* to avoid leakage. Train/val/test contain distinct patients. — https://arxiv.org/pdf/2104.08336
- 5 runs with different random seeds; metrics = AUROC (detection) and weighted F1 (classification).
- For comparison with SeizureNet (Asif et al.), also a 7-class task (all TUSZ types except myoclonic) on the same 3-fold patient-wise split.
- Leakage flag: **none evident** — this is one of the few TUSZ type-classification papers with a clean patient-independent test set.

## Key results (numbers)
All from Tables 2–3 and Sec. 3.2 of https://arxiv.org/pdf/2104.08336

| Model | Det. AUROC 12-s | Det. AUROC 60-s | Cls. wF1 12-s | Cls. wF1 60-s |
|---|---|---|---|---|
| Dense-CNN | 0.812±0.014 | 0.796±0.014 | 0.576±0.101 | 0.626±0.073 |
| LSTM | 0.786±0.014 | 0.715±0.016 | 0.652±0.019 | 0.686±0.020 |
| CNN-LSTM | 0.749±0.006 | 0.682±0.003 | 0.633±0.025 | 0.641±0.019 |
| Corr-DCRNN w/o PT | 0.812±0.012 | 0.804±0.015 | 0.710±0.023 | 0.701±0.030 |
| Dist-DCRNN w/o PT | 0.824±0.020 | 0.793±0.022 | 0.703±0.025 | 0.690±0.035 |
| Corr-DCRNN w/ PT | 0.861±0.005 | 0.850±0.014 | 0.723±0.017 | **0.749±0.017** |
| Dist-DCRNN w/ PT | 0.866±0.016 | **0.875±0.016** | 0.746±0.024 | **0.749±0.028** |

- **7-class, 3-fold patient-wise (Table 3, no pre-training)**: Corr-DCRNN 60-s wF1 0.650±0.008 vs SeizureNet (Asif et al. 2020) 0.62; Corr-DCRNN 12-s 0.619, Dist-DCRNN 12-s 0.585, Dist-DCRNN 60-s 0.606.
- **Per-class one-vs-rest AUROC (4-class, Table 3)**: CF 0.896–0.920, GN 0.795–0.815, AB 0.971–0.983, CT 0.890–0.939 (range across the four DCRNN variants). Iesmantas & Alzbutas (2020) reported GN 0.78 and AB 0.72.
- **Rare classes (12-s, confusion matrices)**: Dist-DCRNN w/o PT 93% accuracy on AB (+2 pts over best baseline); Dist-DCRNN w/ PT 74% on CT (+47 pts over Dense-CNN, +48 over non-pretrained DCRNN). No per-class F1 values are tabulated in the main text.
- **GN→CF confusion**: a board-certified neurologist reviewed 32 misclassified test GN seizures: 27 were actually focal seizures mislabeled as GN; only 5 were true generalized errors → label noise in TUSZ.
- **Localization**: "precisely localizes" (localization score > 0.8, correctly predicted 60-s clips) **25.4%** of focal seizures for pre-trained Corr-DCRNN, 21.8% pre-trained Dist-DCRNN, 6.3% for both non-pretrained DCRNNs, 3.5% for Dense-CNN. Corr graph localizes focal seizures better than the distance graph.
- Detection: at 25% FPR, pre-trained Dist-DCRNN 84.3% TPR vs Dense-CNN 72.8% (12-s).
- Self-supervised pre-training beat transfer learning from a 40,316-EEG in-house dataset (App. J).

## Limitations
- Localization is *channel/time saliency on scalp electrodes* (occlusion), not source localization; only 25.4% of focal seizures precisely localized, and only on correctly classified clips. — https://arxiv.org/pdf/2104.08336
- 4-class merged scheme; SP vs CP and myoclonic not addressed; CT and AB have few patients (test CT from only 4 patients, AB from 5) → high variance per-class estimates.
- Label noise (GN seizures that are actually focal) in TUSZ.
- Authors state need for multi-institution, multi-population validation and a waveform-based consensus classification scheme.
- Classification uses one 12/60-s clip per seizure starting at onset, but the model assumes the clip is known to be a seizure (it does not jointly detect onset and type).

## Relevance to our project
- **Most directly relevant baseline**: patient-wise, TUSZ v1.5.2, 4-class scheme (CF/GN/AB/CT) that we can reproduce with public code; the 12-s clip result (wF1 0.746) is effectively "type at onset" classification.
- The correlation graph + occlusion map gives a channel-level spatial saliency map that can be extended over consecutive windows to visualise *spread* (e.g., compute occlusion per second and track which nodes become salient over time).
- Coverage/localization metrics against TUSZ channel annotations are a ready-made quantitative protocol for our spread map.
- Adopt their leakage fix (remove overlapping patients) and class-merging rationale.
