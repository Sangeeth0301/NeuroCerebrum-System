# Seizure DETECTION on TUSZ and low-latency / real-time detection (2018-2026)

Per-paper files are in `research/papers/`:
- `D_2018_Shah_TUSZ_corpus.md`
- `D_2020_Saab_weak_supervision_seizure_detection.md`
- `D_2022_Lee_realtime_seizure_detection.md`
- `D_2023_Xu_shorter_latency_probabilistic_prediction.md`
- `D_2025_Dan_SzCORE_framework_and_challenge.md`
- `D_2025_Wu_SeizureTransformer_EEG_U_Transformer.md`
- `D_2026_Zabihi_TUSZ_CatBoost_benchmark.md`

## Which papers matter, and what they did (venue, dataset, approach)

### Takeaway
Six detection papers plus the TUSZ corpus paper cover the ground. Only Lee 2022 (CHIL) reports patient-independent onset latency on TUSZ. SeizureTransformer (a preprint) holds the best TUSZ event F1. Xu 2023 (ESWA) has the best low-latency method, but it is patient-specific and tested on CHB-MIT, not TUSZ.

### Cited Findings

Comparison table:

| Paper | Venue (review status) | Data / split | Window / model | Scoring | Sens. | FA | F1 | Latency |
|---|---|---|---|---|---|---|---|---|
| Shah 2018 | Front. Neuroinform. (peer-reviewed) | TUSZ v1.2.0; 265 train / 50 eval patients | corpus only | - | - | - | - | - |
| Saab 2020 | npj Digit. Med. (peer-reviewed) | Stanford + TUSZ v1.4, official split | 12 s / 60 s clips; Inception CNN | clip AUROC and F1 | - | - | 0.49-0.77 (Stanford) | clip length only |
| Lee 2022 | CHIL, PMLR 174 (peer-reviewed) | TUSZ v1.5.2; 26 test patients from dev | 4 s window, 1 s shift; CNN/ResNet+LSTM | OVLP / TAES / MARGIN | 0.75 (OVLP) | 47.06 FA/24h (OVLP) | - | **7.76-15.83 s** mean onset |
| Xu 2023 | ESWA (peer-reviewed) | CHB-MIT, SWEC-ETHZ; patient-specific | 5-10 s; STFT + 3D-CNN, soft labels | per seizure | 94/99 in crossing period | 0.08/h | - | **2.3 s** (CHB-MIT) |
| Dan 2025 SzCORE | Epilepsia (peer-reviewed) | benchmark: CHB-MIT, TUSZ, Siena, SeizeIT1 | framework | event scoring, -30/+60 s tolerance | - | FP/day | - | not defined |
| Dan 2025/26 challenge | arXiv (preprint) | private Dianalund, 4,360 h, 65 subjects | 28-30 algorithms | SzCORE | 37% | - | 43% or 32% (conflict) | - |
| Wu 2025 SeizureTransformer | arXiv (**preprint**) | TUSZ v2.0.3 + Siena | 60 s; U-Net + transformer, time-step output | SzCORE event | 0.717 | not captured | **0.671** | not reported |
| Zabihi 2026 | Sci. Rep. (peer-reviewed) | TUSZ v2.0.3, official Train/Dev/Eval | 60 s / 15 s; features + CatBoost | ≥10 s overlap | 0.75 | 0.68/h (about 16.4/24h) | window macro-F1 0.81 | median 0 s (dilation artifact) |

Sources for each row:
- Lee 2022: sensitivity 0.75 with TNR 0.82 and 47.06 FA/24h under OVLP; TAES gives 0.33 sensitivity at 1.03 FA/24h. Mean onset latency is 10.55 s for CNN2D+LSTM, and 7.76-15.83 s for the best models. The best model, ResNet-short+LSTM, reaches AUROC 0.92. — [PMLR PDF](https://proceedings.mlr.press/v174/lee22a/lee22a.pdf)
- Saab 2020: F1 values above are for Stanford data; see the per-paper file for TUSZ transfer results. — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7170880/)
- Shah 2018 — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6246677/)
- Xu 2023: sensitivity is 94/99 detected during the crossing period and 100% after onset. — [arXiv](https://arxiv.org/html/2301.03465)
- SzCORE 2025: tolerances are 30 s preictal and 60 s postictal. — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12489712/)
- Challenge: sensitivity 37%. Top F1 is 43% with precision 45% per [EPFL](https://infoscience.epfl.ch/entities/publication/b5991dd8-dff4-490f-a449-f314b679c0d9), but 32% with precision 29% per [arXiv v2](https://arxiv.org/abs/2505.18191). Both are abstract-level numbers.
- SeizureTransformer: sensitivity 0.717, precision 0.631, F1 0.671; Dianalund F1 0.428. — [arXiv HTML](https://arxiv.org/html/2504.00336)
- Zabihi 2026: sensitivity 0.749; AUROC 0.92; 77.5% of detections were already active before onset because of ±30 s dilation. — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13049040/)

### Inferences
- The realistic **patient-independent TUSZ latency baseline is about 8-15 s** mean onset latency (Lee 2022). The 2-5 s latencies in the literature come from patient-specific CHB-MIT / SWEC-ETHZ studies and are not comparable.
- **Accuracy SOTA** (SeizureTransformer, Zabihi) uses 60 s windows with offline post-processing and reports no causal latency. That leaves a clear gap: *good event F1 under SzCORE together with a causal, measured onset latency on TUSZ v2.0.x.*

### Gaps
- I could not find a peer-reviewed paper reporting **both** SzCORE event F1 and causal onset latency on TUSZ v2.x.
- Golmohammadi / NEDC deep-learning TUSZ detection results (e.g. the CNN/LSTM chapter, about 30% sensitivity at a few FA/24h) were not verified in this pass, so they are not included. See [isip.piconepress.com](https://isip.piconepress.com/publications/).
- The absolute TUSZ AUROC in Saab 2020 was not extracted.
- The FP/24h for SeizureTransformer on TUSZ was not captured.
- The ESWA DOI and volume for Xu 2023 were not verified.
- The PubMed item 41336388, "Benchmark of EEG-based seizure detection algorithms with SzCORE", was blocked by a CAPTCHA.

## How evaluation and latency are defined, and why it matters

### Takeaway
The scoring method changes the headline numbers several-fold, and the dominant standard, SzCORE, has no latency metric while tolerating detections up to 60 s late.

### Cited Findings
- On the same CNN2D+LSTM model, OVLP gives sensitivity 0.75 with 47 FA/24h, while TAES gives 0.33 with 1.03 FA/24h. — [Lee 2022](https://proceedings.mlr.press/v174/lee22a/lee22a.pdf)
- Lee defines onset latency as "the average latency from the label onset to hypothesis onset". MARGIN scores onset and offset accuracy within ±3 or ±5 s. — [Lee 2022](https://proceedings.mlr.press/v174/lee22a/lee22a.pdf)
- SzCORE uses event scoring with a 30 s preictal and 60 s postictal tolerance, reports sensitivity, precision, F1 and FP/day per subject, and defines no latency. — [SzCORE](https://pmc.ncbi.nlm.nih.gov/articles/PMC12489712/)
- Zabihi's ±30 s dilation produced a median latency of 0 s, with 77.5% of detections active before onset. The authors state this reflects interval expansion, not true preictal detection. — [Zabihi 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC13049040/)
- Many TUSZ studies use non-standard splits or evaluate only seizure segments, which inflates results. — [Zabihi 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC13049040/)

### Inferences
Our project should report all of the following:
- SzCORE event F1, sensitivity and FP/24h, on the official TUSZ v2.0.x eval split with thresholds frozen on dev;
- **causal** onset latency (first alarm minus annotated onset) as a median/IQR and as the share of seizures detected within 5 s and 10 s;
- a latency-versus-FA/24h curve.

Any dilation or non-causal smoothing must be excluded from the latency measurement.

### Gaps
There is no community standard for latency on TUSZ, so our definition must be stated explicitly.

## Implications for an earlier-detection project on TUSZ

### Takeaway
The most promising direction combines Xu-style soft labels and evidence accumulation with a SeizureTransformer-style time-step model run causally on short streaming windows, evaluated with the Zabihi / SzCORE protocol.

### Cited Findings
- Xu 2023 cut latency to 2.3 s on CHB-MIT with 0.08 FD/h, using crossing-period soft labels and an accumulative decision rule. — [arXiv](https://arxiv.org/html/2301.03465)
- Shorter context hurts accuracy: Saab's adult F1 is 0.49 with 12 s clips versus 0.76 with 60 s clips. — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7170880/)
- Pretraining on external data and then fine-tuning on TUSZ gave about +10 AUROC. — [Saab 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7170880/)
- SeizureTransformer outputs a per-time-step probability at 3.98 s of runtime per hour of EEG. — [arXiv HTML](https://arxiv.org/html/2504.00336)
- There is a large generalization gap: SeizureTransformer drops from F1 0.67 on TUSZ to 0.43 on Dianalund. — [arXiv HTML](https://arxiv.org/html/2504.00336)
- Lee's ResNet-short+LSTM needs 0.94 s per window on CPU, which is close to the 1 s real-time budget. — [Lee 2022](https://proceedings.mlr.press/v174/lee22a/lee22a.pdf)

### Inferences
- A defensible claim of "earlier than prior work on TUSZ" should beat about 7.8 s mean latency (Lee 2022's best, measured at TNR > 0.95), at comparable FA/24h and on a comparable split. Ideally we would also re-run Lee's code on v2.0.x for a like-for-like comparison.
- Short focal seizures are the hardest case: Zabihi detects only 33% of 30-90 s focal seizures. Stratifying latency by seizure type would add value.

### Gaps
No TUSZ study was found that applies soft-label or accumulative early detection in the patient-independent setting. This looks like an open niche, although a more exhaustive search, for example on Semantic Scholar, is needed to confirm it.
