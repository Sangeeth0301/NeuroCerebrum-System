# D_2022_Lee: Real-Time Seizure Detection using EEG (CHIL 2022)

## Citation & Link
Lee K., Jeong H., Kim S., Yang D., Kang H.-C., Choi E. "Real-Time Seizure Detection using EEG: A Comprehensive Comparison of Recent Approaches under a Realistic Setting." Proceedings of the Conference on Health, Inference, and Learning (CHIL), PMLR vol. 174, pp. 311-337, 2022.
- Open-access PDF (PMLR): https://proceedings.mlr.press/v174/lee22a/lee22a.pdf
- arXiv preprint: https://arxiv.org/abs/2201.08780
- Code: https://github.com/AITRICS/EEG_real_time_seizure_detection
- Note: PMLR does not issue DOIs, so this paper has none.

## Venue type
Peer-reviewed conference proceedings (CHIL 2022, PMLR vol. 174).

## Problem
Seizure-detection papers are hard to compare because they use different datasets, splits, tasks and metrics, and many models were never tested under real-time (streaming) constraints. The authors benchmark 15 architectures and 6 feature extractors in one real-time framework. They also propose MARGIN, a metric for how accurately a model finds seizure onset and offset.

## Dataset
- TUSZ **v1.5.2**, with slight modifications described in their Appendix A.1. It contains 7,034 signal streaks from 642 patients. 304 of those patients have at least one seizure, and 338 are normal controls. [PDF](https://proceedings.mlr.press/v174/lee22a/lee22a.pdf)
- Split: the official train set has 589 subjects. The official dev set (51 subjects) was split by patient into validation (25 subjects) and test (26 subjects). The split is **patient-independent**, but the test set is small. [PDF](https://proceedings.mlr.press/v174/lee22a/lee22a.pdf)
- Signals were resampled to 200 Hz. The authors tested unipolar and transverse bipolar montages. Bipolar channels were built by subtracting unipolar leads, following SeizureNet's bipolar list. [PDF](https://proceedings.mlr.press/v174/lee22a/lee22a.pdf)

## Approach
- Real-time setting: the model receives a **4 s window every 1 s** (1 s shift) and must process each window within the 1 s shift. They chose the window and shift after searching windows of 1-12 s and shifts of 1-5 s. [PDF](https://proceedings.mlr.press/v174/lee22a/lee22a.pdf)
- Models (15 total): CNN2D+LSTM, CNN2D+BLSTM, ResNet-short+LSTM, ResNet-short+Dilation+LSTM, MobileNetV3-short+LSTM, CNN1D+LSTM/BLSTM, ResNet18, MobileNetV3, AlexNet, DenseNet, ChronoNet, TDNN+LSTM, Feature Transformer and Guided Feature Transformer. [PDF](https://proceedings.mlr.press/v174/lee22a/lee22a.pdf)
- Feature extractors: raw signal, SincNet, STFT (0.125 s frames), frequency bands, LFCC (0.3 s window, 0.15 s shift) and downsampled raw. [PDF](https://proceedings.mlr.press/v174/lee22a/lee22a.pdf)
- Training batches were balanced across four signal types (non-ictal from patients, non-ictal from controls, mixed, and ictal) to limit dataset shift. [PDF](https://proceedings.mlr.press/v174/lee22a/lee22a.pdf)

## Evaluation protocol
- Four scoring methods: OVLP (any-overlap), TAES (time-aligned event scoring), EPOCH (per window), and their new **MARGIN** metric. MARGIN counts an onset or offset as correct only if it falls within a fixed margin of 3 s or 5 s of the label. [PDF](https://proceedings.mlr.press/v174/lee22a/lee22a.pdf)
- **Onset latency** is "the average latency from the label onset to hypothesis onset". MARGIN and latency are measured at an operating point with TNR > 0.95. TPR, TNR and FA/24h are reported at the point that maximises TPR+TNR. [PDF](https://proceedings.mlr.press/v174/lee22a/lee22a.pdf)
- Results are averaged over 5 runs.

## Key results (numbers)
All numbers below come from the full PMLR PDF, Tables 2-4 and Appendix Table 13, not only the abstract.
- Best models with raw bipolar input: **ResNet-short+LSTM** had AUROC 0.92, AUPRC 0.91, TPR 0.83, TNR 0.85, MARGIN(5 s) onset/offset accuracy 0.62/0.65, and took 0.941 s per window on CPU (0.013 s on GPU). ResNet-short+Dilation+LSTM had AUROC 0.91, TPR 0.84 and TNR 0.83. CNN2D+LSTM had AUROC 0.89, TPR 0.81 and TNR 0.83, at 0.079 s per window on CPU. [PDF, Table 2](https://proceedings.mlr.press/v174/lee22a/lee22a.pdf)
- Feature extractors with CNN2D+LSTM: frequency bands reached AUROC 0.92 and TPR 0.85. STFT reached AUROC 0.91 and TPR 0.85. [PDF, Table 3](https://proceedings.mlr.press/v174/lee22a/lee22a.pdf)
- CNN2D+LSTM across scoring methods:

  | Scoring | Sensitivity (TPR) | Specificity (TNR) | FA/24h |
  |---|---|---|---|
  | OVLP | 0.75 | 0.82 | **47.06** |
  | TAES | 0.33 | 1.0 | 1.03 |

  Its MARGIN onset/offset accuracy was 0.41/0.50 at 3 s and 0.56/0.51 at 5 s. **Average onset latency was 10.55 s.** [PDF, Table 4](https://proceedings.mlr.press/v174/lee22a/lee22a.pdf)
- Onset latency for other models (Appendix Table 13, TNR > 0.95):

  | Model | Onset latency (s) |
  |---|---|
  | ResNet-short+Dilation+LSTM | **7.76** |
  | CNN2D+BLSTM | 13.69 |
  | ResNet-short+LSTM | 15.23 |
  | MobileNetV3+LSTM | 15.83 |
  | Some weaker models | 20-43 |

  I matched latency values to model names from the order of rows in the extracted PDF text. Please re-check them against the table itself. [PDF](https://proceedings.mlr.press/v174/lee22a/lee22a.pdf)

## Limitations
- The test set has only 26 patients, taken from the dev split rather than the official eval set, so the results are not directly comparable with the eval-set numbers in other papers.
- The authors modified TUSZ v1.5.2, and v2.x has since changed the annotations.
- The FA/24h at the balanced operating point is high: 47 FA/24h under OVLP.
- Latency is averaged only over detected seizures, and the paper does not publish the full latency distribution.

## Relevance to our project
- This is the most direct **TUSZ latency baseline**: about **7.8-15 s mean onset latency** for 4 s/1 s streaming CNN-LSTM models. Our goal of detecting "earlier than prior work" should be measured against it with the same definition (label onset to hypothesis onset).
- MARGIN (±3/±5 s) is a good way to report onset accuracy.
- The open code gives us a reproducible real-time pipeline.
- Recommendation: report latency and FA/24h together, at a fixed specificity or false-alarm budget.
