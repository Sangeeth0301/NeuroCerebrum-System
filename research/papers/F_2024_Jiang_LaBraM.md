# LaBraM: Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI

## Citation & Link
- Jiang W.-B., Zhao L.-M., Lu B.-L. (2024). *International Conference on Learning Representations (ICLR 2024)*. The PDF header reads "Published as a conference paper at ICLR 2024". arXiv: [2405.18765](https://arxiv.org/abs/2405.18765)
- OpenReview: https://openreview.net/forum?id=QzTpTRVtrP. This ID comes from memory and was not opened in this session, so verify it before citing.
- Code: [github.com/935963004/LaBraM](https://github.com/935963004/LaBraM) (link given in the paper — [arXiv PDF](https://arxiv.org/pdf/2405.18765))

## Venue type
Peer-reviewed conference (ICLR 2024).

## Problem
Can a single large EEG model be pretrained on thousands of hours of heterogeneous EEG, with varying channels and lengths, and then fine-tuned to beat task-specific models on diverse downstream tasks? The paper asks two questions: how to use large unlabelled EEG, and how much data is needed — [arXiv](https://arxiv.org/pdf/2405.18765)

## Dataset
- Pretraining: about 2,500 hours (2,534.78 h in the appendix) from around 20 datasets, including the authors' own recordings — [arXiv](https://arxiv.org/pdf/2405.18765)
- **TUH subsets inside the pretraining set:**
  - TUAR: 92.22 h
  - TUEP: 591.22 h
  - **TUSZ: 1,138.53 h**, the largest single source
  - TUSL
  — [arXiv App. (dataset list)](https://arxiv.org/pdf/2405.18765)
- Downstream TUH data: TUAB with 409,455 × 10 s samples and TUEV with 112,491 × 5 s samples, both 23 channels at 256 Hz. These downstream sets were kept out of pretraining — [arXiv](https://arxiv.org/pdf/2405.18765); also [WebFetch summary of arXiv HTML](https://arxiv.org/html/2405.18765)
- Other downstream tasks: emotion recognition (SEED-V) and gait prediction. No TUSZ or CHB-MIT downstream results — [arXiv](https://arxiv.org/pdf/2405.18765)

## Approach
- Patching: each channel is cut into 1 s patches (w = 200 samples at 200 Hz) and passed through a temporal CNN encoder. Learnable spatial (electrode) and temporal embeddings are added. Sequence length is capped at 256 patches, so 64 channels give 4 s and 32 channels give 8 s of context. Pretraining stride is 4 s — [arXiv §2–3](https://arxiv.org/pdf/2405.18765)
- Tokeniser: vector-quantised neural spectrum prediction. A VQ tokeniser (codebook of 8,192 × 64) is trained to predict each patch's Fourier amplitude and phase, which produces discrete "neural codes" — [arXiv HTML](https://arxiv.org/html/2405.18765)
- Pretraining objective: masked EEG modelling. The transformer predicts the neural codes of masked patches, using symmetric masking at ratio 0.5 — [arXiv HTML](https://arxiv.org/html/2405.18765)
- Sizes: LaBraM-Base 5.8M, Large 46M and Huge 369M parameters — [arXiv Table 1](https://arxiv.org/pdf/2405.18765)
- Fine-tuning: full fine-tuning of the model with a task head.

## Evaluation protocol
Follows BIOT exactly. TUAB/TUEV use the official train/test split, with training patients split 80/20 into train/validation; 16 bipolar channels at 200 Hz; 10 s TUAB and 5 s TUEV windows. Results are mean ± standard deviation over 5 seeds — [arXiv](https://arxiv.org/pdf/2405.18765); protocol detail in [CBraMod App. E](https://arxiv.org/abs/2412.07236)

## Key results (numbers)
From [arXiv Tables 1–2](https://arxiv.org/pdf/2405.18765), cross-checked against [CBraMod Tables 13–14](https://arxiv.org/abs/2412.07236).

**TUAB (abnormal, binary)**

| Model | Params | Balanced Acc | AUPRC | AUROC |
|---|---|---|---|---|
| SPaRCNet (supervised) | 0.79M | 0.7896±0.0018 | 0.8414±0.0018 | 0.8676±0.0012 |
| ST-Transformer (supervised) | 3.5M | 0.7966±0.0023 | 0.8521±0.0026 | 0.8707±0.0019 |
| BIOT | 3.2M | 0.7959±0.0057 | 0.8792±0.0023 | 0.8815±0.0043 |
| LaBraM-Base | 5.8M | 0.8140±0.0019 | 0.8965±0.0016 | 0.9022±0.0009 |
| LaBraM-Large | 46M | 0.8226±0.0015 | 0.9130±0.0005 | 0.9127±0.0005 |
| LaBraM-Huge | 369M | **0.8258±0.0011** | **0.9204±0.0011** | **0.9162±0.0016** |

**TUEV (6-class events)**

| Model | Balanced Acc | Kappa | Weighted F1 |
|---|---|---|---|
| BIOT | 0.5281±0.0225 | 0.5273±0.0249 | 0.7492±0.0082 |
| LaBraM-Base | 0.6409±0.0065 | 0.6637±0.0093 | 0.8312±0.0052 |
| LaBraM-Large | 0.6581±0.0156 | 0.6622±0.0136 | 0.8315±0.0040 |
| LaBraM-Huge | **0.6616±0.0170** | **0.6745±0.0195** | **0.8329±0.0086** |

- CHB-MIT, reported by CBraMod rather than by LaBraM: LaBraM-Base scored balanced accuracy 0.7075±0.0358, AUPRC 0.3287±0.0402 and AUROC 0.8679±0.0199, which is statistically indistinguishable from BIOT (0.7068 / 0.3277 / 0.8761) — [CBraMod Table 8](https://arxiv.org/abs/2412.07236)
- Independent clinical benchmark: fine-tuned LaBraM-Base scored balanced accuracy 0.838 on TUAB abnormal, but 0.565 on TUEP epilepsy (below BENDR's 0.740) and **0.588 on seizure detection** — [EEG-Bench](https://tik-db.ee.ethz.ch/file/1e09e7f339cb0dfcf9ec74bd2bb51c24/)
- Ablation: removing the spatial embedding cut TUEV balanced accuracy from 0.6409 to 0.5949 — [arXiv](https://arxiv.org/pdf/2405.18765)

## Limitations
- Stated by the authors:
  - 2,500 h is still far from the data scale of vision and language models.
  - It needs full fine-tuning, which is costly.
  - It uses EEG only.
  — [arXiv App. M](https://arxiv.org/pdf/2405.18765)
- **Direct TUSZ leakage for our project:** TUSZ (1,138.53 h) is inside LaBraM's pretraining data ([arXiv](https://arxiv.org/pdf/2405.18765)). Fine-tuning the released checkpoint and testing on TUSZ dev/eval therefore evaluates on EEG the encoder has already seen (unlabelled), which is optimistic. To be clean we would need to re-pretrain without TUSZ or use a CBraMod-style "excluding" ablation (inference).
- TUEP and TUAR are also in pretraining, and EEG-Bench evaluates on both, so that benchmark contains some overlap too (inference from [LaBraM](https://arxiv.org/pdf/2405.18765) and [EEG-Bench](https://tik-db.ee.ethz.ch/file/1e09e7f339cb0dfcf9ec74bd2bb51c24/)).
- Compute: LaBraM-Huge needs 22.8 GFLOPs per 16-channel × 10 s sample, compared with 0.48 GFLOPs for Base — [CBraMod Table 22](https://arxiv.org/abs/2412.07236)
- Context is limited to 256 patches, only a few seconds for many channels. That is too short for preictal dynamics that unfold over minutes (inference).

## Relevance to our project
- LaBraM is the main reference model. Its TUAB/TUEV numbers are the standard ones to quote.
- Scaling from Base to Huge gave only about +1.2 points of TUAB balanced accuracy for about 64× the parameters. A Base-size model is enough for a student project.
- The TUSZ-in-pretraining issue must be declared in any TUSZ experiment that uses the released weights.
