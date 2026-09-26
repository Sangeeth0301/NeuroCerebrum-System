# EEG Foundation Models and Their Results on TUH (TUAB/TUEV/TUSZ) and CHB-MIT

Per-paper notes are in `research/papers/`:
- `F_2021_Kostas_BENDR.md`
- `F_2023_Yang_BIOT.md`
- `F_2024_Jiang_LaBraM.md`
- `F_2024_Wang_EEGPT.md`
- `F_2025_Wang_CBraMod.md`
- `F_2025_Kastrati_EEG-Bench.md`
- `F_2026_Liu_EEG-FM-Compass.md`

## Which peer-reviewed EEG foundation models matter, and what did they do?

### Takeaway
Five peer-reviewed models form the lineage: BENDR (2021) → BIOT (NeurIPS 2023) → LaBraM (ICLR 2024) → EEGPT (NeurIPS 2024) → CBraMod (ICLR 2025). Two peer-reviewed benchmarks (EEG-Bench, NeurIPS 2025, likely a workshop; and EEG-FM-Compass, *National Science Review* 2026) test whether these models beat simple models. On the shared BIOT protocol, CBraMod (4M parameters, TUEG-pretrained) currently holds the best TUAB, TUEV and CHB-MIT numbers.

### Comparison table

| Model (venue) | Params | Pretraining data | Includes TUH? | Patch / input | Objective | Source |
|---|---|---|---|---|---|---|
| BENDR (Front. Hum. Neurosci. 2021) | unclear | TUEG v1.1/1.2, about 1.5 TB, more than 10k subjects | **Yes, all of TUEG** | conv-downsampled tokens; 60 s at 256 Hz, 20 channels | wav2vec2 contrastive masked spans | [Frontiers](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2021.653659/full) |
| BIOT (NeurIPS 2023) | 3.2M | SHHS + proprietary PREST + ECG; the "6 EEG" model also used supervised training sets of CHB-MIT/TUAB/TUEV/IIIC | TUAB and TUEV *training sets* (supervised) | per-channel FFT segment tokens; 10 s (TUAB/CHB-MIT), 5 s (TUEV) at 200 Hz | contrastive + supervised multi-task | [arXiv](https://arxiv.org/pdf/2305.10351) |
| LaBraM (ICLR 2024) | 5.8M / 46M / 369M | about 2,535 h from about 20 datasets | **Yes: TUSZ 1,138.53 h, TUEP 591.22 h, TUAR 92.22 h, TUSL** | 1 s patches, at most 256 patches | VQ neural-spectrum tokeniser + masked code prediction | [arXiv](https://arxiv.org/pdf/2405.18765) |
| EEGPT (NeurIPS 2024) | "10M" in abstract; 25M / 4.7M in tables | PhysioMI, HGD, TSU, SEED, M3CV | **No** | 250 ms patches, 4 s at 256 Hz, up to 58 channels | representation alignment + masked reconstruction; linear probing | [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2024/file/4540d267eeec4e5dbd9dae9448f0b739-Paper-Conference.pdf) |
| CBraMod (ICLR 2025) | 4.0M | TUEG cleaned: 1,109,545 × 30 s, more than 9,000 h | **Yes, all of TUEG** (plus ablations excluding TUAB and TUEV) | 1 s patches, 30 s pretraining windows | criss-cross masked patch reconstruction (50%) | [arXiv](https://arxiv.org/pdf/2412.07236) |

### Results table (same BIOT protocol: official TUH split with 80/20 validation; CHB-MIT subjects 1–19 / 20–21 / 22–23; 16 bipolar channels at 200 Hz; 10 s TUAB/CHB-MIT and 5 s TUEV windows)

| Model | TUAB BAcc | TUAB AUPRC | TUAB AUROC | TUEV BAcc | TUEV κ | TUEV wF1 | CHB-MIT BAcc | CHB-MIT AUPRC | CHB-MIT AUROC |
|---|---|---|---|---|---|---|---|---|---|
| Best supervised (SPaRCNet / ST-T / CNN-T) | 0.7966 | 0.8521 | 0.8707 | 0.4384 | 0.4233 | 0.7024 | 0.6389 | 0.2479 | 0.8662 |
| BIOT (6 EEG) | 0.7959 | 0.8792 | 0.8815 | 0.5281 | 0.5273 | 0.7492 | 0.7068 | 0.3277 | 0.8761 |
| LaBraM-Base | 0.8140 | 0.8965 | 0.9022 | 0.6409 | 0.6637 | 0.8312 | 0.7075* | 0.3287* | 0.8679* |
| LaBraM-Huge | 0.8258 | 0.9204 | 0.9162 | 0.6616 | 0.6745 | 0.8329 | – | – | – |
| EEGPT (25M) | 0.7983 | – | 0.8718 | 0.6232 | 0.6351 | 0.8187 | – | – | – |
| **CBraMod** | **0.8289** | **0.9258** | **0.9227** | **0.6671** | **0.6772** | **0.8342** | **0.7398*** | **0.3689*** | **0.8892*** |

\* CHB-MIT figures for LaBraM and CBraMod come from the CBraMod paper, not from LaBraM.

Supervised baseline rows use the best value per column, taken from the BIOT/LaBraM/CBraMod tables. On TUAB, ST-Transformer is best for BAcc, AUPRC and AUROC. On TUEV, ContraWR is best for BAcc and SPaRCNet for κ and wF1. On CHB-MIT, CNN-Transformer is best.

Sources: [CBraMod Tables 8/13/14](https://arxiv.org/pdf/2412.07236); [LaBraM Tables 1–2](https://arxiv.org/pdf/2405.18765); [BIOT Tables 2, 4, 5](https://arxiv.org/pdf/2305.10351); [EEGPT Tables 2–3](https://proceedings.neurips.cc/paper_files/paper/2024/file/4540d267eeec4e5dbd9dae9448f0b739-Paper-Conference.pdf)

### Cited Findings
- **No paper in this set reports TUSZ downstream results.** LaBraM uses TUSZ only as *pretraining* data (1,138.53 h). Seizure evaluation across these papers is CHB-MIT 10 s window detection — [LaBraM](https://arxiv.org/pdf/2405.18765); [CBraMod](https://arxiv.org/pdf/2412.07236); [BIOT](https://arxiv.org/pdf/2305.10351)
- CBraMod beats LaBraM-Huge (369M) with 4.0M parameters, and needs 318.9 MFLOPs against LaBraM-Huge's 22.8 GFLOPs per 16-channel × 10 s sample — [CBraMod Table 22](https://arxiv.org/pdf/2412.07236)
- Re-pretraining CBraMod without TUAB or TUEV changed results by at most 0.4 points (TUAB BAcc 0.8289 → 0.8249; TUEV 0.6671 → 0.6659) — [CBraMod](https://arxiv.org/pdf/2412.07236)
- LaBraM scaling from Base to Huge (5.8M → 369M) added only 1.18 points of TUAB BAcc and 2.07 points of TUEV BAcc — [LaBraM](https://arxiv.org/pdf/2405.18765)
- EEGPT, which has no TUH pretraining, sits at BIOT level on TUAB (0.7983 vs 0.7959). Its authors attribute LaBraM's advantage to TUEG data in LaBraM's pretraining — [EEGPT](https://proceedings.neurips.cc/paper_files/paper/2024/file/4540d267eeec4e5dbd9dae9448f0b739-Paper-Conference.pdf)
- BIOT's headline "6 EEG datasets" checkpoint was trained with supervision on the CHB-MIT, TUAB and TUEV training sets before fine-tuning — [BIOT §3.6](https://arxiv.org/pdf/2305.10351)
- A widely circulated summary of the CBraMod paper contains fabricated numbers (for example TUEV BAcc 0.8523). The real figure in the PDF is 0.6671, so always cite the PDF tables — [CBraMod PDF](https://arxiv.org/pdf/2412.07236)

### Inferences
- The TUAB/TUEV benchmark is nearly saturated among foundation models: the top three are within about 1.5 points of BAcc. CHB-MIT, with 2 test patients and ±3–5 point standard deviations, cannot reliably separate them.

### Gaps
- There are no published foundation-model results on TUSZ seizure detection or forecasting under the BIOT/LaBraM protocol in these papers.
- BENDR's parameter count could not be verified.
- EEGPT does not report its total pretraining hours.

## Do foundation models really beat small supervised models?

### Takeaway
Only partly. On TUAB and on CHB-MIT AUROC the gains over the best supervised model are small (about 3 points of TUAB BAcc and 0.02 AUROC on CHB-MIT). On TUEV they are large (+20 points of BAcc). Independent peer-reviewed benchmarks find that classical models and specialists stay competitive, especially for seizure detection and under linear probing.

### Cited Findings
- TUAB: the best supervised model (ST-Transformer, 3.5M) scores BAcc 0.7966 / AUROC 0.8707, against CBraMod's 0.8289 / 0.9227 — [CBraMod Table 14](https://arxiv.org/pdf/2412.07236)
- TUEV: the best supervised BAcc is about 0.44 against 0.67 for CBraMod. This is the largest foundation-model gain in the whole set — [CBraMod Table 13](https://arxiv.org/pdf/2412.07236)
- CHB-MIT: supervised CNN-Transformer AUROC is 0.8662 against CBraMod's 0.8892. AUPRC is 0.25 against 0.37. All models stay below 0.37 AUPRC — [CBraMod Table 8](https://arxiv.org/pdf/2412.07236)
- EEG-Bench seizure task (balanced accuracy): SVM 0.572, LaBraM 0.588, BENDR 0.501, Neuro-GPT 0.500. On sleep staging, LDA scored 0.671 against LaBraM's 0.192 — [EEG-Bench](https://tik-db.ee.ethz.ch/file/1e09e7f339cb0dfcf9ec74bd2bb51c24/)
- EEG-FM-Compass (NSR 2026; 12 foundation models, 13 datasets): "linear probing is frequently insufficient", specialists "remain competitive across many tasks", and "larger FMs do not necessarily yield better generalization" — [arXiv abstract](https://arxiv.org/abs/2601.17883); [NSR](https://academic.oup.com/nsr/advance-article/doi/10.1093/nsr/nwag466/8750569)
- **Preprint (not peer-reviewed):** EEG-FM-Audit reports that supervised TS-SEFFNet matches or beats LaBraM and EEGPT on TUAB/TUEV. This is from a search snippet only — [arXiv 2605.26910](https://arxiv.org/pdf/2605.26910)
- Critical review (peer-reviewed, *J. Neural Eng.*) — [IOPscience](https://iopscience.iop.org/article/10.1088/1741-2552/ae4455)

### Inferences
- The supervised baselines in the BIOT/LaBraM tables are generic architectures that were not heavily tuned, so the reported gaps are probably upper bounds.
- Pretraining appears to help most for multi-class, morphology-heavy tasks such as TUEV, and least for rare-event seizure windows.

### Gaps
- I could not extract EEG-FM-Compass per-dataset numbers or confirm whether it includes TUH or seizure datasets, because the full text exceeded the fetch limit.

## Limitations: leakage, window length versus latency, and compute

### Takeaway
Leakage through the TUH archive is the key risk for a TUSZ project. Short context windows (4–10 s at fine-tuning) and window-level metrics also make the published numbers poor proxies for seizure forecasting.

### Cited Findings
- LaBraM pretrains on TUSZ directly (1,138.53 h) — [LaBraM](https://arxiv.org/pdf/2405.18765)
- CBraMod and BENDR pretrain on all of TUEG — [CBraMod](https://arxiv.org/html/2412.07236); [BENDR](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2021.653659/full)
- CBraMod shows how to control for leakage by re-pretraining with the downstream corpus excluded — [CBraMod](https://arxiv.org/pdf/2412.07236)
- Input lengths:
  - EEGPT: 4 s — [EEGPT](https://proceedings.neurips.cc/paper_files/paper/2024/file/4540d267eeec4e5dbd9dae9448f0b739-Paper-Conference.pdf)
  - LaBraM: at most 256 patches (4 s with 64 channels, 8 s with 32 channels) — [LaBraM](https://arxiv.org/pdf/2405.18765)
  - Benchmark windows: 10 s for TUAB/CHB-MIT and 5 s for TUEV — [BIOT](https://arxiv.org/pdf/2305.10351)
  - CBraMod pretraining: 30 s — [CBraMod](https://arxiv.org/html/2412.07236)
- EEG-Bench handled minutes-to-hours clinical recordings by chunking them and averaging embeddings, because the models accept only 4–60 s — [EEG-Bench](https://tik-db.ee.ethz.ch/file/1e09e7f339cb0dfcf9ec74bd2bb51c24/)
- Compute: LaBraM-Huge needs 22.8 GFLOPs per sample. CBraMod needs 0.32 GFLOPs and EEGNet 8.9 MFLOPs — [CBraMod Table 22](https://arxiv.org/pdf/2412.07236)

### Inferences
- TUSZ is derived from the TUH EEG archive. So any TUEG-pretrained checkpoint (BENDR, CBraMod) very likely saw TUSZ eval-patient EEG without labels. Confirm session-level overlap using TUH file names or patient IDs.
- For forecasting, per-window embeddings of 4–30 s will need a second-stage temporal model spanning minutes of preictal context.
- Window-level AUROC on CHB-MIT does not reflect event-level sensitivity, false alarms per hour or warning time.

### Gaps
- No foundation-model paper here reports latency, false alarms per hour or event-level metrics.

## Relevance to our project (earlier seizure forecasting on TUSZ)

### Takeaway
Use a small, montage-flexible, open model (CBraMod or BIOT) as a frozen or fine-tuned per-window encoder. Pretrain it on TUEG minus all TUSZ patients, or disclose the overlap. Always compare against a classical baseline and a supervised CNN baseline.

### Cited Findings
- CBraMod: 4M parameters, montage-agnostic positional encoding, 30 s pretraining, public code — [GitHub](https://github.com/wjq-learning/CBraMod); [arXiv](https://arxiv.org/abs/2412.07236)
- BIOT: 3.2M parameters, handles missing channels and segments — [arXiv](https://arxiv.org/pdf/2305.10351); [GitHub](https://github.com/ycq091044/BIOT)
- EEGPT has no TUH data in pretraining, making it a leakage-free control — [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2024/file/4540d267eeec4e5dbd9dae9448f0b739-Paper-Conference.pdf); [GitHub](https://github.com/BINE022/EEGPT)
- The EEG-Bench code provides ready-made loaders and baselines for TUAB, TUEP, TUAR and CHB-MIT — [GitHub](https://github.com/ETH-DISCO/EEG-Bench)

### Inferences
Suggested experimental plan:
1. Reproduce CHB-MIT 10 s detection with CBraMod as a sanity check.
2. Build TUSZ preictal-versus-interictal windows using patient-wise splits.
3. Compare four models:
   - A. SVM on spectral and line-length features.
   - B. A small CNN such as EEGNet.
   - C. EEGPT with linear probing (no leakage).
   - D. CBraMod fine-tuned (TUEG checkpoint, overlap disclosed) plus a GRU over window embeddings.
4. Report AUPRC, sensitivity, false alarms per hour and warning time, not only AUROC.

### Gaps
- None of the reviewed papers addresses forecasting (preictal) labels.
