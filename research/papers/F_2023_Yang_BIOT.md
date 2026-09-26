# BIOT: Biosignal Transformer for Cross-data Learning in the Wild

## Citation & Link
- Yang C., Westover M. B., Sun J. (2023). *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*. arXiv: [2305.10351](https://arxiv.org/abs/2305.10351)
- Code: [github.com/ycq091044/BIOT](https://github.com/ycq091044/BIOT). The paper says the codebase and pretrained models are released on GitHub — [arXiv PDF](https://arxiv.org/pdf/2305.10351). The repository URL is the commonly cited one and was not opened in this session.
- Note: the numbers below come from arXiv v1 (May 2023, marked "Preprint. Under review"). The identical TUAB/TUEV/CHB-MIT numbers are reproduced as "BIOT" in the ICLR-2024 LaBraM and ICLR-2025 CBraMod papers ([LaBraM](https://arxiv.org/abs/2405.18765), [CBraMod](https://arxiv.org/abs/2412.07236)), so they match the published version.

## Venue type
Peer-reviewed conference (NeurIPS 2023). Numbers were verified from the arXiv version.

## Problem
Biosignal datasets differ in channels, sampling rates, lengths and missing segments. Can one model tokenise any format, so that it can pretrain on and transfer across heterogeneous datasets (EEG, ECG, activity)? — [arXiv](https://arxiv.org/pdf/2305.10351)

## Dataset
- Unsupervised pretraining data:
  - SHHS sleep EEG: 5,445 recordings, 5,093,522 samples of 30 s at 125 Hz.
  - PREST: a **proprietary** resting EEG set with 6,478 recordings and 5,110,992 samples of 10 s, 16 montages at 200 Hz.
  - Cardiology ECG.
  — [arXiv Table 1](https://arxiv.org/pdf/2305.10351)
- Downstream data:
  - CHB-MIT: 686 recordings, 16 bipolar montages, 10 s windows, 326,993 samples.
  - TUAB: 2,339 recordings, 10 s windows, 409,455 samples.
  - TUEV: 11,914 recordings, 5 s windows, 112,491 samples.
  - IIIC Seizure, PTB-XL and HAR.
  — [arXiv Table 1](https://arxiv.org/pdf/2305.10351)
- The "Pre-trained BIOT (6 EEG datasets)" model is the one that later papers cite. It was built by loading the PREST+SHHS model and then **further training it with supervision on the training sets of CHB-MIT, IIIC Seizure, TUAB and TUEV**, with a separate head for each task — [arXiv §3.6](https://arxiv.org/pdf/2305.10351)

## Approach
- Tokenisation: resample every signal to 200 Hz and normalise each channel. Each channel is cut into overlapping segments, and each segment is turned into an FFT energy vector and passed through a fully connected layer to give a token. A learned channel embedding (spatial) and a sinusoidal relative position embedding (temporal) are added. All channel tokens are flattened into one "biosignal sentence" — [arXiv §2.1](https://arxiv.org/pdf/2305.10351)
- Architecture: a linear-complexity (linear attention) transformer, about 3.2M parameters — [arXiv](https://arxiv.org/pdf/2305.10351); parameter count also in [CBraMod Table 22](https://arxiv.org/abs/2412.07236)
- Pretraining: unsupervised contrastive pretraining on PREST, SHHS and ECG, plus supervised cross-task pretraining (Settings 3–5) — [arXiv §3.4–3.6](https://arxiv.org/pdf/2305.10351)
- Fine-tuning: the full model is fine-tuned on each downstream training set. Loss is BCE for TUAB, focal loss for CHB-MIT (about 0.6% positives in training) and cross-entropy for TUEV — [arXiv §3.2](https://arxiv.org/pdf/2305.10351)

## Evaluation protocol
- 5 random seeds, reported as mean ± standard deviation. Models are selected on validation and scored on test — [arXiv](https://arxiv.org/pdf/2305.10351)
- CHB-MIT: 16 montages, 10 s non-overlapping windows, with seizure regions windowed at a 5 s overlap to increase positives — [arXiv](https://arxiv.org/pdf/2305.10351). The patient split used by followers is subjects 1–19 train, 20–21 validation, 22–23 test — [CBraMod App. E](https://arxiv.org/abs/2412.07236)
- TUAB/TUEV: the official train/test split, with training patients further split 80/20 into train/validation — [CBraMod App. E](https://arxiv.org/abs/2412.07236)

## Key results (numbers)
All figures are from [arXiv v1](https://arxiv.org/pdf/2305.10351), Table 2 and Appendix Tables 4–5.

| Dataset | Model | Balanced Acc | AUPRC | AUROC |
|---|---|---|---|---|
| CHB-MIT | Vanilla BIOT (from scratch) | 0.6640±0.0037 | 0.2573±0.0088 | 0.8646±0.0030 |
| CHB-MIT | Pretrained (PREST) | 0.6942±0.0431 | 0.3072±0.1187 | 0.8679±0.0106 |
| CHB-MIT | Pretrained (6 EEG datasets) | **0.7068±0.0457** | **0.3277±0.0460** | **0.8761±0.0284** |
| CHB-MIT | Best supervised baseline (CNN-Transformer) | 0.6389±0.0067 | 0.2479±0.0227 | 0.8662±0.0082 |
| TUAB | Vanilla BIOT | 0.7925±0.0035 | 0.8707±0.0087 | 0.8691±0.0033 |
| TUAB | Pretrained (6 EEG datasets) | 0.7959±0.0057 | 0.8792±0.0023 | 0.8815±0.0043 |
| TUAB | ST-Transformer (supervised) | 0.7966±0.0023 | 0.8521±0.0026 | 0.8707±0.0019 |

| TUEV | Balanced Acc | Kappa | Weighted F1 |
|---|---|---|---|
| Vanilla BIOT | 0.4682±0.0125 | 0.4482±0.0285 | 0.7085±0.0184 |
| Pretrained (PREST) | 0.5207±0.0285 | 0.4932±0.0301 | 0.7381±0.0169 |
| Pretrained (6 EEG datasets, "ultimate") | **0.5281±0.0225** | **0.5273±0.0249** | **0.7492±0.0082** |
| Best supervised baseline (ContraWR, by BAcc) | 0.4384±0.0349 | 0.3912±0.0237 | 0.6893±0.0136 |

## Limitations
- **Supervised leakage in the headline model:** the "6 EEG datasets" checkpoint was trained on the *labelled training sets* of CHB-MIT, TUAB and TUEV before fine-tuning — [arXiv §3.6](https://arxiv.org/pdf/2305.10351). This is multi-task supervised pretraining rather than pure self-supervision, so it is not directly comparable to SSL-only models (inference).
- PREST, the main unlabelled EEG pretraining set, is proprietary, so the pretraining cannot be reproduced — [arXiv](https://arxiv.org/pdf/2305.10351)
- The TUAB gain over supervised ST-Transformer is small (balanced accuracy 0.7959 vs 0.7966, AUROC 0.8815 vs 0.8707) — [arXiv](https://arxiv.org/pdf/2305.10351)
- CHB-MIT uses only 2 test patients (22, 23) ([CBraMod App. E](https://arxiv.org/abs/2412.07236)), so standard deviations are large (balanced accuracy ±0.0457) and AUPRC is low (0.33) because only about 0.6% of windows are seizure — [arXiv](https://arxiv.org/pdf/2305.10351)
- It uses 10 s window classification (detection), not forecasting. No TUSZ evaluation.

## Relevance to our project
- The most practical architecture for us. It is small (3.2M parameters), has a low-cost FFT tokeniser, handles variable channels and lengths, and tolerates missing segments. That suits TUSZ's heterogeneous montages.
- Its 10 s CHB-MIT detection protocol is the de facto foundation-model seizure benchmark. We should reproduce it as a sanity check, and then move to patient-wise TUSZ preictal-versus-interictal labelling.
- The reported 0.6% positive rate and AUPRC of about 0.33 show that event-level metrics and calibrated thresholds matter more than AUROC for rare-event tasks.
