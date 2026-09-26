# D_2025_Wu: SeizureTransformer / Large EEG-U-Transformer for time-step level detection (arXiv 2025, PREPRINT)

## Citation & Link
Wu K., Zhao Z., Yener B. "Large EEG-U-Transformer for Time-Step Level Detection Without Pre-Training." arXiv:2504.00336. Submitted 1 April 2025, last revised 4 October 2025. v1 was titled "SeizureTransformer."
- arXiv abstract: https://arxiv.org/abs/2504.00336
- HTML full text: https://arxiv.org/html/2504.00336
- PDF: https://arxiv.org/pdf/2504.00336

## Venue type
**Preprint, not peer-reviewed as far as I could verify.** The arXiv page gives no journal reference. The model placed first in the 2025 Seizure Detection Challenge at the International Conference on AI in Epilepsy and Other Neurological Disorders, which was evaluated with SzCORE. [arXiv](https://arxiv.org/abs/2504.00336)

## Problem
Window-by-window classifiers need many redundant overlapping inferences and produce coarse labels. This paper predicts at the **time-step level** (one probability per sample) with a sequence-to-sequence U-shaped model trained without large-scale pretraining. [arXiv](https://arxiv.org/abs/2504.00336)

## Dataset
- **TUSZ v2.0.3**: 7,377 files, 675 patients and 1,476 h. The paper reports results on the TUSZ test (eval) set. [arXiv HTML](https://arxiv.org/html/2504.00336)
- Siena Scalp EEG (14 patients) was added to the training data. SeizeIT1 and Dianalund were used for cross-device evaluation. [arXiv HTML](https://arxiv.org/html/2504.00336)

## Approach
- Preprocessing:
  - 19 standard 10-20 electrodes, following SzCORE. The HTML summary said "18", so check the paper.
  - Fourier resampling to 256 Hz and per-channel z-score.
  - 0.5-100 Hz bandpass, with notch filters at 1 Hz and 60 Hz.

  [arXiv HTML](https://arxiv.org/html/2504.00336)
- Input is a **60 s window** (15,360 samples). Training windows overlap by 0.75; inference windows do not overlap. [arXiv HTML](https://arxiv.org/html/2504.00336)
- Architecture:
  - Encoder: 6 conv-maxpool blocks.
  - Bottleneck: a ResCNN stack plus an 8-layer transformer (dimension 512, 4 heads).
  - Decoder: upsampling.
  - Size: about 23-59M parameters, and the authors state the model follows scaling laws.

  [arXiv HTML](https://arxiv.org/html/2504.00336)
- Post-processing: threshold τ = 0.8, morphological opening and closing, and a minimum event duration of 2 s. [arXiv HTML](https://arxiv.org/html/2504.00336)

## Evaluation protocol
SzCORE event-based scoring: sensitivity, precision, F1 and FP/day. The paper does not report a latency metric. [arXiv HTML](https://arxiv.org/html/2504.00336)

## Key results (numbers)
- **TUSZ eval, event-based**:
  - **F1 0.6713**, which the authors describe as "13.01% improvement over prior best".
  - Sensitivity 0.7168 and precision 0.6312.
  - Runtime about 3.98 s per hour of EEG.

  [arXiv HTML](https://arxiv.org/html/2504.00336)
- Cross-device event F1: SeizeIT1 0.4547 and Dianalund 0.4283 (first place in the challenge; second place scored 0.36). [arXiv HTML](https://arxiv.org/html/2504.00336)
- I did not capture an FP/24h value for TUSZ.

## Limitations
- It is a preprint.
- It uses 60 s non-overlapping windows. The design is offline or batch, not low-latency streaming. Time-step output could support streaming in principle, but the paper does not evaluate that.
- Performance drops sharply on out-of-distribution data (0.67 on TUSZ to 0.43 on Dianalund).
- No latency is reported.

## Relevance to our project
- This is the **current state-of-the-art event F1 on TUSZ v2.0.3** under SzCORE, so it is the accuracy baseline to compare against. Code and weights are reportedly on the SzCORE platform; I did not verify this.
- An earlier-detection project could:
  1. run this model in causal or streaming mode with short look-ahead;
  2. measure onset latency; and
  3. show a better latency/F1 trade-off.
