# CBraMod: A Criss-Cross Brain Foundation Model for EEG Decoding

## Citation & Link
- Wang J., Zhao S., Luo Z., Zhou Y., Jiang H., Li S., Li T., Pan G. (Zhejiang University) (2025). *International Conference on Learning Representations (ICLR 2025)*. The PDF footer reads "Published as a conference paper at ICLR 2025". arXiv: [2412.07236](https://arxiv.org/abs/2412.07236)
- Code: [github.com/wjq-learning/CBraMod](https://github.com/wjq-learning/CBraMod) — [arXiv](https://arxiv.org/abs/2412.07236)

## Venue type
Peer-reviewed conference (ICLR 2025).

## Problem
Earlier EEG foundation models use full attention over all channel and time patches, which ignores the different nature of spatial and temporal dependencies. They also use absolute channel or position embeddings that transfer poorly across montages. CBraMod models spatial and temporal dependencies with separate "criss-cross" attention and uses asymmetric conditional positional encoding — [arXiv](https://arxiv.org/abs/2412.07236)

## Dataset
- Pretraining: **TUEG only**. Starting from 69,652 recordings (14,987 subjects), the authors kept 19 channels, applied a 0.3–75 Hz band-pass and a 60 Hz notch, resampled to 200 Hz and cut 30 s windows. They dropped windows with amplitude above 100 µV, leaving **1,109,545 samples, more than 9,000 h** — [arXiv HTML](https://arxiv.org/html/2412.07236)
- Downstream: 10 tasks and 12 datasets, including:
  - TUEV: 112,491 × 5 s samples, 16 bipolar channels at 200 Hz.
  - TUAB: 409,455 × 10 s samples.
  - **CHB-MIT**: 326,993 × 10 s samples, 16 bipolar channels. Split by subject: 1–19 train, 20–21 validation, 22–23 test.
  - No TUSZ.
  — [arXiv PDF App. E](https://arxiv.org/pdf/2412.07236)

## Approach
- Patching: **1 s patches** (200 samples). A 30 s × 19-channel sample becomes 570 patches — [arXiv HTML](https://arxiv.org/html/2412.07236)
- Patch encoder: time-domain convolution combined with FFT spectral embedding. Asymmetric conditional positional encoding (ACPE) is a convolution over the channel × time patch grid, so it adapts to any montage — [arXiv](https://arxiv.org/abs/2412.07236)
- Criss-cross transformer: 12 layers, hidden size 200, 8 heads. Half the heads attend along the spatial axis (across channels at the same time) and half along the temporal axis (across time within a channel), in parallel — [arXiv HTML](https://arxiv.org/html/2412.07236)
- Objective: masked patch reconstruction at a 50% mask ratio — [arXiv HTML](https://arxiv.org/html/2412.07236)
- Size: **4.0M parameters**; 318.9 MFLOPs per 16-channel × 10 s sample, compared with 483 MFLOPs for BIOT and LaBraM-Base and 22.8 GFLOPs for LaBraM-Huge — [arXiv PDF Table 22](https://arxiv.org/pdf/2412.07236)
- Fine-tuning: full fine-tuning with a task head.

## Evaluation protocol
Uses the BIOT/LaBraM preprocessing and splits for TUEV, TUAB and CHB-MIT, with mean ± standard deviation over seeds. **The authors additionally re-pretrained CBraMod with TUEV (or TUAB) removed from TUEG** to test for leakage — [arXiv PDF App. E.7–E.8](https://arxiv.org/pdf/2412.07236)

## Key results (numbers)
All numbers were copied from the ICLR-2025 PDF tables — [arXiv PDF Tables 8, 13, 14](https://arxiv.org/pdf/2412.07236)

**CHB-MIT (seizure detection, 10 s windows)**

| Model | Params | Balanced Acc | AUPRC | AUROC |
|---|---|---|---|---|
| EEGNet | 0.003M | 0.5658±0.0106 | 0.1914±0.0182 | 0.8048±0.0136 |
| CNN-Transformer | 3.2M | 0.6389±0.0067 | 0.2479±0.0227 | 0.8662±0.0082 |
| BIOT | 3.2M | 0.7068±0.0457 | 0.3277±0.0460 | 0.8761±0.0284 |
| LaBraM-Base | 5.8M | 0.7075±0.0358 | 0.3287±0.0402 | 0.8679±0.0199 |
| **CBraMod** | 4.0M | **0.7398±0.0284** | **0.3689±0.0382** | **0.8892±0.0154** |

**TUEV (6-class)**

| Model | Balanced Acc | Kappa | Weighted F1 |
|---|---|---|---|
| LaBraM-Base | 0.6409±0.0065 | 0.6637±0.0093 | 0.8312±0.0052 |
| LaBraM-Huge (369M) | 0.6616±0.0170 | 0.6745±0.0195 | 0.8329±0.0086 |
| CBraMod (TUEV excluded from pretraining) | 0.6659±0.0124 | 0.6744±0.0121 | 0.8331±0.0071 |
| **CBraMod** | **0.6671±0.0107** | **0.6772±0.0096** | **0.8342±0.0064** |

**TUAB (abnormal)**

| Model | Balanced Acc | AUPRC | AUROC |
|---|---|---|---|
| SPaRCNet (supervised) | 0.7896±0.0018 | 0.8414±0.0018 | 0.8676±0.0012 |
| LaBraM-Base | 0.8140±0.0019 | 0.8965±0.0016 | 0.9022±0.0009 |
| LaBraM-Huge | 0.8258±0.0011 | 0.9204±0.0011 | 0.9162±0.0016 |
| CBraMod (TUAB excluded) | 0.8249±0.0025 | 0.9221±0.0015 | 0.9156±0.0017 |
| **CBraMod** | **0.8289±0.0022** | **0.9258±0.0008** | **0.9227±0.0011** |

- Removing the downstream set from pretraining costs only about 0.1–0.4 points. The authors read this as evidence that leakage is not what drives the results — [arXiv PDF](https://arxiv.org/pdf/2412.07236)

## Limitations
- The authors note that TUEG "suffers from significant data contamination", with unmarked noise, artifacts and faulty channels. They clean it heuristically with a 100 µV threshold — [arXiv HTML App.](https://arxiv.org/html/2412.07236)
- **TUSZ overlap:** pretraining uses all of TUEG, and TUSZ sessions are drawn from the TUH EEG archive. So TUSZ test EEG (unlabelled) is very likely in the pretraining set. The paper ran exclusion ablations only for TUEV and TUAB (inference; confirm the TUSZ⊂TUEG session overlap using the TUH documentation).
- The CHB-MIT test set is only 2 patients (22, 23), and AUPRC stays around 0.37. The CHB-MIT margin over BIOT (+3.3 points of balanced accuracy) is within about 1 standard deviation of BIOT's ±0.0457.
- It evaluates window-level detection only. No event-level sensitivity, false alarms per hour, latency or forecasting horizon.
- A widely shown excerpt of this paper circulates with inflated numbers (for example TUEV balanced accuracy of about 0.85). Always quote from the PDF tables above.

## Relevance to our project
- This is the **best-performing and most efficient** open model on all three relevant benchmarks: 4M parameters, and it runs on a student GPU.
- Its 30 s pretraining context and ACPE, which is montage-agnostic, fit TUSZ's variable referential and bipolar montages.
- Its "excluding X" re-pretraining ablation is the **methodological template we should copy**: pretrain on TUEG minus all TUSZ patients before evaluating any TUSZ forecasting model.
