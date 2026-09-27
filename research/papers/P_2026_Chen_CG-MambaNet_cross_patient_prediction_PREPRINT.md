# P_2026_Chen: CG-MambaNet, cross-patient seizure prediction with CNN-GCN-Mamba-BiLSTM and event-level evaluation (arXiv 2026, PREPRINT)

## Citation & Link
Chen M., Wu Q., Huang B., Lai X., Chen Z., Ouyang X., Zhang T., Yang X., Ren Q. "CG-MambaNet: A spatiotemporal framework for cross-patient epileptic seizure prediction using CNN-GCN-Mamba-BiLSTM with event-level clinical evaluation." arXiv:2606.08226 [eess.SP], v1, submitted 6 June 2026.
- Abstract page: https://arxiv.org/abs/2606.08226
- HTML full text: https://arxiv.org/html/2606.08226v1
- PDF: https://arxiv.org/pdf/2606.08226
- The HTML version lists affiliations including Peking University, Beihang University, the Chinese Academy of Sciences and the University of Oxford. [arXiv HTML](https://arxiv.org/html/2606.08226v1)
- No DOI. No code release was found in the paper. [arXiv HTML](https://arxiv.org/html/2606.08226v1)

## Venue type
**PREPRINT, not peer-reviewed.** The arXiv record has no journal reference. [arXiv abs](https://arxiv.org/abs/2606.08226)
- The details below come from an automated extraction of the arXiv HTML. Headline numbers (AUC 0.8152 / 0.7104 and 0.32 alarms/h) are confirmed in the abstract. **All other numbers should be checked against the PDF before citing.**

## Problem
The paper names three problems in deep-learning seizure prediction:
1. channels are modelled independently, so inter-channel synchrony is ignored;
2. models work on raw time samples without frequency decomposition;
3. splits allow patient-level leakage, which gives optimistic results.

It proposes a cross-patient model evaluated with strict leave-one-patient-out and **event-level** alarm metrics. The motivation is closed-loop neurostimulation. [arXiv abs](https://arxiv.org/abs/2606.08226)

## Dataset
All details from the [arXiv HTML](https://arxiv.org/html/2606.08226v1).
- **CHB-MIT: n = 22** (paediatric, bipolar montage, 256 Hz). chb12 is excluded because of its non-standard channel set.
- **Siena: n = 6 of 14** (adult, referential montage, 512 Hz). Eight patients are excluded because they lack 30 uninterrupted minutes of pre-ictal EEG before at least one seizure.
- **Preictal = 30 min before onset.** Interictal = at least 4 h from any seizure.
- **No explicit SPH (intervention gap) was identified** in the extraction. Treat the preictal window as running up to onset unless the PDF says otherwise.
- **Channels:** 16 bipolar pairs common to both datasets.
- **Preprocessing:**
  - 0.5–40 Hz 4th-order zero-phase Butterworth band-pass, plus a 60 Hz or 50 Hz notch;
  - resampling to 200 Hz;
  - per-channel ±500 µV artifact rejection;
  - non-overlapping **10-s windows**;
  - per-channel z-scoring using training statistics only.

## Approach
All details from the [arXiv HTML](https://arxiv.org/html/2606.08226v1).
- **Serial pipeline:** frequency decomposition, then spatial mixing, then temporal integration.
  1. **Depthwise-separable CNN front-end** with kernels of 5 and 15 samples at 200 Hz. It captures delta–gamma bands with about 928 parameters.
  2. **2-layer GCN** with a fully learnable, symmetric-normalized 16×16 adjacency. It needs no electrode coordinates, so it works on both bipolar and referential montages.
  3. **Bidirectional Mamba encoder** (12 blocks, reported as "EEGMamba").
  4. **2-layer BiLSTM** with hidden size 128.
  5. 2-layer MLP producing the output.
- Input tensor: batch × 16 channels × 10 patches × 200 samples.
- **Training:** AdamW (learning rate 3e-4, weight decay 1e-4), cosine schedule, 50 epochs with 5 warm-up epochs, batch size 64, dropout 0.3, and **inverse-frequency weighted BCE** (no undersampling of the test set).

## Evaluation protocol
All details from the [arXiv HTML](https://arxiv.org/html/2606.08226v1).
- **LOPO × 5 random seeds**: 22 × 5 = 110 test folds for CHB-MIT and 6 × 5 = 30 for Siena.
  - Validation is an 80/20 split *within the N−1 training patients*.
  - The test patient's data is kept at its natural imbalance.
- **Segment metrics:** AUC-ROC (primary), plus sensitivity, specificity and accuracy at the Youden-optimal threshold.
- **Event-level alarms:**
  - a 60-s **causal** moving average of window probabilities gives the risk R(t);
  - the threshold θ* is Youden-optimal on the validation fold;
  - an alarm fires if R(t) ≥ θ* for at least 30 s, and resets after at least 60 s below θ*.
  - Metrics are event sensitivity, **event FPR (alarms/h over interictal time)** and mean lead time (onset − alarm).
- **Leakage risks:**
  - Low for patients (LOPO, training-only normalization, validation within training patients).
  - The paper uses no SOP/SPH-window scoring or chance test (random predictor or surrogate). "Lead time" is therefore not tied to a fixed SOP, so an alarm 25 min before onset counts regardless of how many false alarms preceded it.
  - Siena n = 6 is very small.

## Key results (numbers)
Values are LOPO × 5 seeds, mean ± SD. Headline AUC and CHB-MIT event FPR are confirmed in the [arXiv abstract](https://arxiv.org/abs/2606.08226). All other values are from the [arXiv HTML](https://arxiv.org/html/2606.08226v1) and are **preprint numbers, unverified in the PDF**.

| Metric | CHB-MIT (n = 22) | Siena (n = 6) |
|---|---|---|
| **AUC-ROC** | **0.8152 ± 0.0176** | **0.7104 ± 0.0261** |
| Sensitivity (segment, Youden) | 74.3 ± 9.1% | 63.2 ± 5.0% |
| Specificity (segment) | 76.5 ± 8.9% | 67.4 ± 3.2% |
| Accuracy (segment) | 75.4 ± 8.9% | 65.3 ± 3.9% |
| Window-level FPR | 112.4 ± 13.8 /h | 89.3 ± 16.2 /h |
| **Event-level FPR** | **0.32 ± 0.16 /h** | **0.55 ± 0.13 /h** |
| **Mean lead (warning) time** | **23.4 ± 4.8 min** | **21.7 ± 5.3 min** |
| Event-level sensitivity | not captured in the extraction; check the PDF | not captured |

- **Ablation (CHB-MIT)**, AUC / sensitivity / event FPR:
  - Mamba-BiLSTM only: 0.7426 / 68.8% / 2.34 per h;
  - adding the CNN front-end: 0.7734 / 70.1% / 1.67 per h;
  - adding the GCN (full model): 0.8152 / 71.8% / 0.32 per h.
  - The full-model ablation sensitivity (71.8%) **differs from the main-table 74.3%**, an internal inconsistency.
  - The paper reports McNemar p < 0.05 for both components.
- **Comparison table in the paper** (CHB-MIT / Siena AUC):
  - Jemal 2024 without DA: 0.69 / 0.48;
  - Jemal 2024 "CDAN+E": 0.75 / 0.61;
  - CLSP-REQA 2026 (another arXiv preprint, 2606.00074): 0.7426 / 0.7012;
  - CG-MambaNet: 0.8152 / 0.7104.
  - **Our check against the Jemal paper:** Jemal's best Siena AUC of 0.61 came from **CDAN**, not CDAN+E; CDAN+E on Siena gave 0.52. See P_2024_Jemal. The abstract's claim of "surpassing all published cross-patient methods without domain adaptation" is also a narrower claim than the table implies.
- The 0.32 alarms/h event FPR comes from persistence filtering a window-level FPR of about 112 per hour. **Post-processing, not the classifier, provides most of the false-alarm control.**

## Limitations
- Stated by the authors: retrospective and offline; fixed 30-min preictal; scalp only; no online personalization; no edge or embedded profiling. [arXiv HTML](https://arxiv.org/html/2606.08226v1)
- Our additional concerns:
  - not peer-reviewed;
  - no SPH, so alarms at 1–5 min before onset still count, which is clinically weak;
  - no surrogate or random-predictor test;
  - Siena n = 6;
  - ablation and main-table inconsistency;
  - misattributed comparison numbers;
  - no code;
  - event sensitivity not clearly reported.

## Relevance to our project
- This is the **closest template to our intended protocol**: patient-held-out evaluation, a learnable-adjacency GCN over bipolar channels (maps directly onto the TUSZ 20-channel TCP montage), a Mamba/state-space temporal encoder, and **event-level FPR/h plus lead time** from a causal risk curve with a persistence filter.
- **Numbers to beat (preprint):** cross-patient AUC 0.815, event FPR 0.32/h and mean lead time 23.4 min on CHB-MIT, with a 30-min preictal window.
  - Our TUSZ claim of "earlier forecasting" should report lead time **with** event FPR/h and event sensitivity.
  - It should also add an SPH and a chance test, which CG-MambaNet lacks.
- **Caveat:** CHB-MIT gives long, continuous paediatric recordings. TUSZ sessions are short and heterogeneous (adult, clinical), so 30 min of clean preictal EEG with a 4-h interictal buffer will exclude many TUSZ seizures (see P_2025_Mohammad_MLSPred-Bench).
