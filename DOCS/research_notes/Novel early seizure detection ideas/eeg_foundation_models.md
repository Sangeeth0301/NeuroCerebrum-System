# EEG Foundation Models for Seizure Detection on TUH Corpora (2023-2026)

Research date: 2026-09-25. Items marked **[UNVERIFIED]** come from background knowledge or from a secondary summary and were not confirmed against the primary source during this session. Items marked **[CONFLICT]** show sources that disagree.

---

## Q1. Model-by-model specs: parameters, pretraining corpus, input window, channel flexibility, license, code

### Takeaway
Most of the strongest open EEG foundation models (FMs) are small: CBraMod 4.0M, LaBraM-Base 5.8M, BIOT 3.2M, S-CEReBrO 2.4M, LUNA-Base 7M. They are pretrained mainly on TUEG (TUH EEG Corpus, about 2.5k–25k hours). Pretraining takes multi-GPU days, but fine-tuning these small models fits on one consumer GPU. Most use 1 s patches, fine-tuned on 5–30 s windows. Only S-CEReBrO and CaMBrain (both 2026) are designed for bounded-memory streaming or causal inference.

### Cited Findings

**LaBraM (ICLR 2024 spotlight)**
- Sizes: Base 5.8M, Large 46M, Huge 369M. Pretrained on "over 2,500 hours" from about 20 datasets. Patch is 200 samples (1 s at 200 Hz), up to 256 patches. Uses a VQ neural tokenizer with an 8192-entry codebook — [LaBraM arXiv html](https://arxiv.org/html/2405.18765)
- Code: [github.com/935963004/LaBraM](https://github.com/935963004/labram)
- Only the LaBraM-Base weights are public. Large and Huge are not — [CBraMod paper (ICLR 2025), baselines section](https://arxiv.org/pdf/2412.07236)
- Uses full self-attention over channels×patches, so cost is O((CT)²) — [S-CEReBrO, Table 1](https://arxiv.org/pdf/2607.27913)

**CBraMod (ICLR 2025)**
- 4.0M params. Pretrained on TUEG after bad-sample removal: 1,109,545 30-s samples, more than 9,000 h. Patch is 1 s at 200 Hz. Pretraining took about 5 days on 4× RTX A5000 — [CBraMod arXiv](https://arxiv.org/html/2412.07236)
- Its criss-cross (parallel spatial and temporal) attention plus asymmetric conditional positional encoding (ACPE) "can be adapted to arbitrary EEG formats", which gives it channel flexibility — [CBraMod arXiv](https://arxiv.org/html/2412.07236)
- Downstream windows: CHB-MIT 10 s with 16 bipolar channels. TUEV 5 s with 16 channels. TUAB 10 s with 16 channels — [CBraMod PDF, Table of downstream datasets](https://arxiv.org/pdf/2412.07236)
- Code: [github.com/wjq-learning/CBraMod](https://github.com/wjq-learning/CBraMod). The README uses TUAB v3.0.1 and TUEV v2.0.0 — [preprocessing README](https://github.com/wjq-learning/CBraMod/blob/main/preprocessing/README.md)
- **[CONFLICT]** The LUNA and CaMBrain tables list CBraMod at 69.3M params, next to the "excluding TUAB" numbers — [LUNA](https://arxiv.org/pdf/2510.22257), [CaMBrain](https://arxiv.org/abs/2605.28792). The CBraMod paper itself says 4.0M, and a July 2026 stress-test paper says 4.9M — [Stress-test](https://arxiv.org/html/2607.24519v1). Treat 4.0–4.9M as correct.

**BIOT (NeurIPS 2023)**
- 3.2M params — [LaBraM tables](https://arxiv.org/html/2405.18765)
- The pretrained BIOT accepts at most 18 channels, so larger montages need several BIOT models — [CBraMod appendix](https://arxiv.org/pdf/2412.07236)
- Uses 10 s input windows — [CBraMod appendix](https://arxiv.org/pdf/2412.07236)
- Uses linear attention, O(CT) — [S-CEReBrO](https://arxiv.org/pdf/2607.27913)
- BIOT's pretraining included CHB-MIT, so its seizure results on CHB-MIT are not clean transfer — [Stress-test paper](https://arxiv.org/html/2607.24519v1)
- Code: github.com/ycq091044/BIOT **[UNVERIFIED URL]**

**EEGPT (NeurIPS 2024)**
- Brain4FMs lists EEGPT at 51.04M params — [Brain4FMs](https://arxiv.org/html/2602.11558v1)
- Other claims not checked: 4 s windows at 256 Hz, up to 58 electrodes, code at github.com/BINE022/EEGPT **[UNVERIFIED]**.

**BENDR (2021; predates the focus window)**
- **[CONFLICT]** Size is given as 0.39M in [LUNA Table 1](https://arxiv.org/pdf/2510.22257), 3.97M in [Brain4FMs](https://arxiv.org/html/2602.11558v1), and 157M in the [Stress-test paper](https://arxiv.org/html/2607.24519v1). The difference probably depends on whether the contextualizer transformer is counted.
- TUAB result: BAcc 76.96±3.98, AUROC 0.8397 — [LUNA Table 1](https://arxiv.org/pdf/2510.22257)

**NeuroLM (ICLR 2025)**
- Treats EEG as a "foreign language": a VQ text-aligned tokenizer feeds an LLM. The largest variant, NeuroLM-XL, has 1.7B params. Pretrained on about 25,000 h. Tasks: TUAB, TUEV, TUSL, emotion, sleep, workload — [ICLR proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/8b4add8b0aa8749d80a34ca5d941c355-Abstract-Conference.html)
- Code: [github.com/935963004/NeuroLM](https://github.com/935963004/NeuroLM)
- Brain4FMs lists NeuroLM at 169.60M, which is probably the smallest variant — [Brain4FMs](https://arxiv.org/html/2602.11558v1)

**FEMBA (EMBC 2025) and "FEMBA on the Edge" (2026)**
- Bidirectional Mamba, so it scales linearly with sequence length. Pretrained on more than 21,000 h of unlabeled EEG. Results: TUAB BAcc 81.82%, AUROC 0.8921. TUAR AUROC 0.949. FEMBA-Tiny has 7.8M params — [FEMBA arXiv](https://arxiv.org/pdf/2502.06438)
- Variant sizes: Base 47.7M, Large 77.8M, Huge 386M — [LUNA Tables 1-2](https://arxiv.org/pdf/2510.22257)
- Weights: [huggingface.co/PulpBio/FEMBA](https://huggingface.co/PulpBio/FEMBA)
- The 2026 edge paper covers quantization and deployment on an ultra-low-power microcontroller. Low-pass ("physiologically-aware") pretraining raises TUAB AUROC from 0.863 to 0.893 — [FEMBA on the Edge](https://arxiv.org/abs/2603.26716)
- Note: FEMBA is **bidirectional**, so it is not causal as published.

**EEGFormer (arXiv Jan 2024)**
- VQ-based. Sizes: Base 2.3M, Large 3.2M. Results: TUAB AUROC 0.867. TUAR AUROC 0.847/0.852. TUSL AUROC 0.713/0.679 — [LUNA Tables 1-2](https://arxiv.org/pdf/2510.22257)
- Its abstract mentions downstream use "from seizure detection to wave analysis" — [arXiv 2401.10278](https://arxiv.org/abs/2401.10278)
- Code and exact TUSZ numbers not found (see gaps).

**Brant, Brant-2/BrainWave, Brant-X**
- Brant (NeurIPS 2023): intracranial EEG (iEEG), 500M params, 1.01 TB of iEEG — [Brant paper](https://proceedings.neurips.cc/paper_files/paper/2023/file/535915d26859036410b0533804cee788-Paper-Conference.pdf)
- Brant-2: more than 1B params, about 4 TB of mixed data (2.3 TB iEEG, 1.6 TB EEG) — [Brant-2 arXiv](https://arxiv.org/html/2402.10251v3)
- BrainWave (the renamed Brant-2 line; repo [yzz673/Brant-2 "BrainWave"](https://github.com/yzz673/Brant-2)): more than 40,000 h (13.79 TB) from about 16,000 people, EEG plus iEEG. Uses 1 s time-frequency patches plus channel attention — [search summary of BrainWave](https://arxiv.org/html/2402.10251v3)
- Brain4FMs lists BrainWave at 102.13M. BrainWave reaches about 0.90 AUROC on CHB-MIT and about 0.98 on MAYO iEEG — [Brain4FMs](https://arxiv.org/html/2602.11558v1)
- Brant-X (KDD 2024) aligns EEG with other physiological signals (EXG) — [Brant-X arXiv](https://arxiv.org/pdf/2409.00122)
- These are too large for comfortable student fine-tuning and are mostly iEEG-oriented.

**CEReBrO (2025) and S-CEReBrO (2026)**
- CEReBrO uses alternating spatial and temporal attention. Its smallest model is comparable to EEGFormer on seizure detection. An 85M model reached a maximum AUROC of 0.875 on that task — [CEReBrO arXiv](https://arxiv.org/html/2501.10885)
- TUAB: 85.15M params, BAcc 81.67, AUROC 0.8916 — [LUNA Table 1](https://arxiv.org/pdf/2510.22257)
- **[CONFLICT]** S-CEReBrO lists CEReBrO at 2.4M. CEReBrO comes in several sizes, and the two sources quote different ones — [S-CEReBrO](https://arxiv.org/pdf/2607.27913)
- **S-CEReBrO** (ETH Zurich, arXiv 2607.27913, v3 14 Sep 2026):
  - 2.4M params, pretrained on more than 25,000 h from more than 12,000 subjects (TUEG plus consumer datasets). TUAB subjects were excluded from pretraining.
  - "Windowed Alternating Attention" keeps resident memory O(1) in signal length during streaming.
  - At a 4 h signal it uses 55% of the memory of linear attention with 2.1× throughput. It handles 14 h signals, 100× longer than full attention.
  - Code: [github.com/pulp-bio/biofoundation](https://github.com/pulp-bio/biofoundation)
  - Source: [S-CEReBrO arXiv](https://arxiv.org/abs/2607.27913)

**LUNA (NeurIPS 2025)**
- Sizes: Base 7M, Large 43M, Huge 311.4M. Pretrained on TUEG plus Siena, more than 21,000 h.
- Learned-query cross-attention compresses any electrode layout into a fixed latent, so it is topology-agnostic and scales linearly with channel count. It cuts FLOPs by 300× and GPU memory by up to 10×.
- Pretraining ran on 8× A100.
- Code: [pulp-bio/biofoundation](https://github.com/pulp-bio/biofoundation)
- Source: [LUNA PDF](https://arxiv.org/pdf/2510.22257), [NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/66969a9e6bd7a26dfeccea7227178ca7-Abstract-Conference.html)

**2025-2026 newcomers**
- **REVE (NeurIPS 2025)**: masked autoencoder pretrained on more than 60,000 h from 92 datasets and 25,000 subjects. A 4D positional encoding handles any electrode layout and signal length. Code, weights and tutorials are released — [arXiv 2510.21585](https://arxiv.org/abs/2510.21585), [project page](https://brain-bzh.github.io/reve/)
  - Size is about 69–72M — [Brain4FMs](https://arxiv.org/html/2602.11558v1), [Stress-test](https://arxiv.org/html/2607.24519v1)
  - TUH makes up 44% of REVE's pretraining corpus — [Stress-test](https://arxiv.org/html/2607.24519v1)
- **CaMBrain (UCF, arXiv 2605.28792, May 2026)**:
  - A **causal, unidirectional Mamba-3** EEG FM, 36.7M params. It processes 62.5 ms patches and keeps a persistent hidden state, so it can predict in real time at 16 Hz.
  - Pretrained on TUEG (about 21k h) with causal autoregressive plus masked objectives, followed by teacher-student latent prediction.
  - Pretraining ran on H100.
  - Code availability was not stated in the text extracted.
  - Source: [CaMBrain arXiv](https://arxiv.org/abs/2605.28792)
- Also in 2025-2026:
  - CSBrain — [arXiv 2506.23075](https://arxiv.org/pdf/2506.23075)
  - SAMBA, long-context differential Mamba — [arXiv 2511.18571](https://arxiv.org/pdf/2511.18571)
  - DiffEEG: 9.6M diffusion-pretrained model, trained on 1.3M TUSZ segments — [arXiv 2607.11578](https://arxiv.org/html/2607.11578v1)
  - EEGMamba (3.3M) and BrainOmni (32.7M) appear in benchmarks — [Stress-test](https://arxiv.org/html/2607.24519v1), [Brain4FMs](https://arxiv.org/html/2602.11558v1)

### Inferences
- For a student with a single GPU, the realistic candidates are CBraMod (4M), LaBraM-Base (5.8M), BIOT (3.2M), LUNA-Base (7M), S-CEReBrO (2.4M) and FEMBA-Tiny (7.8M). Fine-tuning any of these fits in a few GB of VRAM. NeuroLM-XL, LaBraM-Huge (weights unreleased anyway), BrainWave and Brant are impractical.
- For streaming or low latency, the architectures that fit best are S-CEReBrO (O(1) memory, 2.4M, code in pulp-bio/biofoundation) and CaMBrain (causal SSM). CBraMod and LaBraM need sliding windows that recompute overlapping context.

### Gaps
- I did not verify code licenses (MIT, Apache or non-commercial) for any repo. Check each repo's LICENSE file. The LUNA paper's CC-BY 4.0 statement applies to the paper, not the code — [LUNA PDF](https://arxiv.org/pdf/2510.22257).
- EEGPT's exact parameter count and window length, BIOT's GitHub URL, and whether CaMBrain releases code were not verified.
- Pretraining hours for EEGPT, BENDR and CEReBrO were not confirmed.

---

## Q2. Reported metrics on TUSZ / TUAB / TUEV / CHB-MIT

### Takeaway
On TUAB and TUEV, published FMs beat supervised baselines. TUAB gains are modest: BAcc about 0.79 to 0.83, AUROC 0.87 to 0.92. TUEV gains are large: BAcc about 0.40 to 0.67. On CHB-MIT, FMs raise AUPRC from about 0.19–0.25 to about 0.33–0.39. However, AUPRC stays low and variance is high. Almost no FM paper reports TUSZ results in the standard seizure-detection form (event-level sensitivity or false alarms per hour).

### Cited Findings

**TUAB (abnormal vs normal, 2-class), from [CBraMod Table 14](https://arxiv.org/pdf/2412.07236) and [LaBraM](https://arxiv.org/html/2405.18765):**

| Model | Params | BAcc | AUPRC | AUROC |
|---|---|---|---|---|
| EEGNet | 0.003M | 0.7642 | 0.8299 | 0.8412 |
| SPaRCNet | 0.79M | 0.7896 | 0.8414 | 0.8676 |
| ST-Transformer | 3.5M | 0.7966 | 0.8521 | 0.8707 |
| BIOT | 3.2M | 0.7959 | 0.8792 | 0.8815 |
| LaBraM-Base | 5.8M | 0.8140 | 0.8965 | 0.9022 |
| LaBraM-Huge | 369M | 0.8258 | 0.9204 | 0.9162 |
| CBraMod (TUAB excluded from pretraining) | 4.0M | 0.8249 | 0.9221 | 0.9156 |
| CBraMod | 4.0M | 0.8289 | 0.9258 | 0.9227 |

Further TUAB results from [LUNA Table 1](https://arxiv.org/pdf/2510.22257):
- FEMBA-Huge: 81.82 / 0.9005 / 0.8921
- CEReBrO (85M): 81.67 / 0.9049 / 0.8916
- LUNA-Base: 80.63 / 0.8953 / 0.8868
- LUNA-Huge: 81.57 / 0.9029 / 0.8957
- EEGFormer: AUROC 0.867
- BENDR: AUROC 0.8397

The S-CEReBrO paper re-ran TUAB under its own protocol. AUROC ×100: best supervised 88.97, BIOT 88.56, CBraMod 89.36, LaBraM 88.30, S-CEReBrO 89.30 — [S-CEReBrO Table 4](https://arxiv.org/pdf/2607.27913). This is essentially a tie with supervised models.

**TUEV (6-class event type), from [CBraMod Table 13](https://arxiv.org/pdf/2412.07236):**

| Model | Params | BAcc | Kappa | Weighted F1 |
|---|---|---|---|---|
| EEGNet | 0.003M | 0.3876 | 0.3577 | 0.6539 |
| SPaRCNet | 0.79M | 0.4161 | 0.4233 | 0.7024 |
| ContraWR | 1.6M | 0.4384 | 0.3912 | 0.6893 |
| BIOT | 3.2M | 0.5281 | 0.5273 | 0.7492 |
| LaBraM-Base | 5.8M | 0.6409 | 0.6637 | 0.8312 |
| LaBraM-Huge | 369M | 0.6616 | 0.6745 | 0.8329 |
| CBraMod (TUEV excluded from pretraining) | 4.0M | 0.6659 | 0.6744 | 0.8331 |
| CBraMod | 4.0M | 0.6671 | 0.6772 | 0.8342 |

- EEGPT on TUEV: BAcc about 0.62, weighted F1 about 0.82 **[UNVERIFIED, from memory]**.

**CHB-MIT (seizure vs non-seizure; 10 s windows, 16 bipolar channels, subject split with patients 23/24 as test), from [CBraMod Table 8](https://arxiv.org/pdf/2412.07236):**

| Model | Params | BAcc | AUPRC | AUROC |
|---|---|---|---|---|
| EEGNet | 0.003M | 0.5658 | 0.1914 | 0.8048 |
| EEGConformer | 0.55M | 0.5976 | 0.2209 | 0.8226 |
| CNN-Transformer | 3.2M | 0.6389 | 0.2479 | 0.8662 |
| BIOT | 3.2M | 0.7068 | 0.3277 | 0.8761 |
| LaBraM-Base | 5.8M | 0.7075 | 0.3287 | 0.8679 |
| CBraMod | 4.0M | 0.7398 | 0.3689 | 0.8892 |

Further CHB-MIT results:
- [CaMBrain Table 1b](https://arxiv.org/abs/2605.28792) reports AUROC/AUPRC:
  - LUNA-L: 0.896 / 0.316
  - REVE (72M): 0.908 / 0.380
  - CaMBrain (37M): 0.921 / 0.389
  - **Caveat:** CaMBrain uses a recording-level random 80/10/10 split. The baselines appear to be copied from CBraMod's subject-split numbers, so this is not like-for-like.
- [S-CEReBrO Table 4](https://arxiv.org/pdf/2607.27913), AUROC ×100:
  - best supervised: 86.62
  - BIOT: 80.84±4.43
  - CBraMod: 84.55
  - LaBraM: 79.70±5.64
  - S-CEReBrO: 87.45±1.93
  - Re-running the FMs under S-CEReBrO's own protocol lowered them below the supervised baseline.
- [Brain4FMs](https://arxiv.org/html/2602.11558v1): BrainWave about 0.90 AUROC.
- [Stress-test paper](https://arxiv.org/html/2607.24519v1): frozen REVE 0.793 vs random-init 0.701 vs classical features 0.700. Seizure positives and negatives share recording sessions, which weakens the claim.

**TUSZ**
- NeuroAtlas uses frozen linear probes and scores event-level sensitivity averaged over 0.1–100 false alarms per hour (FA/h).
  - Across seven seizure datasets (TUSZ, SeizeIT1/2, CHB-MIT, Bonn, TUAB, NMT), the best score per dataset ranges from about 0.50 to 0.74.
  - Only NeuroLM and REVE clearly beat a random-init CBraMod baseline (about 0.55 vs 0.44).
  - "Most per-model means lie within ≈0.05 AUC of the 0.44 baseline."
  - Source: [NeuroAtlas](https://arxiv.org/html/2605.14698v1)
- LUNA and CaMBrain report TUAR (artifacts) and TUSL (slowing) but not TUSZ — [LUNA](https://arxiv.org/pdf/2510.22257)

### Inferences
- The CHB-MIT gain over CNN baselines (about +0.10 BAcc, +0.12 AUPRC in the CBraMod paper) is the most seizure-relevant FM evidence. It shrinks or reverses when others re-run the models (S-CEReBrO), and it rests on one small 2-patient test split.
- TUAB AUROC differences among the top FMs are within about 0.01–0.03. They are probably not practically meaningful for seizure work.

### Gaps
- I found no FM paper reporting standard TUSZ window-level or event-level metrics (sensitivity, FA/24h, the NEDC/SzCORE scoring used in TUSZ evaluations) in a like-for-like table. NeuroAtlas is the closest, and I did not extract its per-model TUSZ numbers.
- I did not find EEGFormer's or CEReBrO's exact TUSZ seizure-detection setup.

---

## Q3. Latency, streaming/causal inference, reduced channels, seizure-type classification

### Takeaway
Only two 2026 FMs explicitly target streaming: S-CEReBrO (bounded memory) and CaMBrain (a causal SSM with 62.5 ms update steps). CaMBrain gives the only onset-anticipation anecdote found. No FM paper found reports TUSZ detection latency in seconds or seizure-type (FNSZ/GNSZ/CPSZ/ABSZ/TNSZ/TCSZ) classification. This is an open gap and a research opportunity.

### Cited Findings
- **CaMBrain**:
  - Sustained compute at 16 Hz streaming: CaMBrain 1.23 GFLOPs/s, CBraMod 7.51, BIOT 15.80, LaBraM 16.99, LUNA-L 35.85, REVE 194.79.
  - Persistent-state inference beats resetting the state every 5 s by +0.015 AUROC. On chb22_20, the probability starts climbing about 15 s before annotated onset.
  - Per-recording results vary: chb22_25 has warm-state AUROC 0.73 vs cold 0.97.
  - Source: [CaMBrain](https://arxiv.org/abs/2605.28792)
- **S-CEReBrO**: attention memory is bounded regardless of recording length. It processes a 4 h stream with 2.1× the throughput of linear attention. Its strongest gains are on seizure tasks (CHB-MIT, Neonate) — [S-CEReBrO](https://arxiv.org/pdf/2607.27913)
- **FEMBA on the Edge**: quantized bidirectional Mamba deployed on an ultra-low-power MCU. The bidirectional design is not causal — [arXiv 2603.26716](https://arxiv.org/abs/2603.26716)
- **Channel flexibility**:
  - CBraMod's ACPE handles arbitrary formats — [CBraMod](https://arxiv.org/html/2412.07236)
  - LUNA's latent queries decouple compute from channel count, and results hold "across all evaluated electrode configurations" — [LUNA](https://arxiv.org/abs/2510.22257)
  - REVE's 4D positional encoding handles any setup — [REVE](https://arxiv.org/abs/2510.21585)
  - BIOT is capped at 18 channels per model — [CBraMod appendix](https://arxiv.org/pdf/2412.07236)
  - In the Stress-test paper, no FM beat classical features on 2-channel Sleep-EDF (68.6%) — [Stress-test](https://arxiv.org/html/2607.24519v1)
- **Seizure-type classification**: TUSZ has eight seizure types — [search summary](https://www.catalyzex.com/s/Seizure%20Detection). My search did not find any FM paper evaluating TUSZ seizure-type classification. TUEV (6 event classes: SPSW, GPED, PLED, EYEM, ARTF, BCKG) is the closest benchmark the FMs report — [CBraMod](https://arxiv.org/pdf/2412.07236)
- **Supervised context**: the ICML 2026 SzCORE challenge evaluated 28 algorithms on 4,360 h of held-out continuous EEG. The top event-based F1 was only 32% (sensitivity 37%, precision 29%). Self-reported F1 scores were much higher than challenge results — [SzCORE generalization gap, arXiv 2505.18191](https://arxiv.org/abs/2505.18191)

### Inferences
- A student project could fine-tune S-CEReBrO or CaMBrain (if weights are released) or LUNA-Base on TUSZ with a reduced montage. It could then report detection latency and FA/24h under SzCORE, and seizure-type classification. As far as I found, all three are unoccupied niches for FMs.

### Gaps
- No FM paper found reports onset-detection latency in seconds on TUSZ.
- CaMBrain's weight or code release status is unverified.
- No reduced-channel (for example 2–4 channel wearable) FM results on TUSZ were found.

---

## Q4. Criticisms: leakage, and FMs barely beating small supervised baselines

### Takeaway
Several independent 2025-2026 benchmarks conclude that EEG FMs give small or inconsistent gains over well-tuned small supervised models:
- Frozen FM representations are weak.
- Pretraining on TUEG overlaps TUAB, TUEV and TUSZ.
- Rankings change with metric and protocol.

Seizure detection is the domain where FMs look relatively best, but only after full fine-tuning.

### Cited Findings
- **EEG-FM-Bench** (arXiv 2508.17742; ICML 2026 poster; published in National Science Review):
  - Covers 14 datasets and 10 paradigms, including TUAB, TUEV, TUSL and Siena seizure data. Models: BENDR, BIOT, LaBraM, EEGPT, CBraMod, CSBrain, REVE, plus the general time-series models Mantis and Moment.
  - "Frozen-backbone transfer exhibits a substantial generalization gap."
  - Gradients of the reconstruction and classification objectives show "near-zero or negative" correlation. So pretrained models mostly act as a "time-series aware initialization."
  - Source: [arXiv](https://arxiv.org/abs/2508.17742), [ICML 2026](https://icml.cc/virtual/2026/poster/60932), [code](https://github.com/Dingkun0817/EEG-FM-Benchmark)
- **AdaBrain-Bench** (arXiv 2507.09882):
  - 13 datasets and 7 BCI tasks, including clinical anomaly detection. Models: BIOT, EEGPT, LaBraM, CBraMod.
  - Settings: cross-subject, multi-subject and few-shot.
  - Source: [arXiv](https://arxiv.org/abs/2507.09882), [code](https://github.com/Jamine-W/AdaBrain-Bench)
  - I did not extract its detailed numbers.
- **NeuroAtlas** (May 2026, KU Leuven/MIT; 42 datasets, about 260k h, 10 EEG FMs, frozen linear probes):
  - EEG FMs "do not consistently outperform time-series FMs" (Chronos, MOMENT, Moirai) that were never pretrained on EEG.
  - AUROC and event-level sensitivity give different seizure rankings (Spearman 0.61–0.81).
  - For seizures, FMs beat supervised models except on datasets they were pretrained on.
  - Source: [NeuroAtlas](https://arxiv.org/html/2605.14698v1)
- **Stress-Testing EEG FMs / Negative-Control Protocol** (Zare, July 2026):
  - Linear probes separate datasets from each other with AUROC 1.000, so dataset identity dominates the representation.
  - Frozen REVE scores 0.568 AUROC on CAUEEG dementia vs 0.769 for classical features.
  - TUAB is in-domain for REVE (44% of its corpus is TUH), and BIOT saw CHB-MIT during pretraining.
  - Recommendations: audit pretraining overlap and use stronger classical baselines.
  - Source: [arXiv 2607.24519](https://arxiv.org/html/2607.24519v1)
- **"Are Large Brainwave FMs Capable Yet?"** (Lee et al., July 2025):
  - LaBraM (5.8M) and NeuroGPT (78.5M) gain only 0.9–1.2% over EEGNet (2.4k params) and EEG-Inception (22k params).
  - NeuroGPT scores 74.5% vs EEG-Inception 73.3%, with about 3,500× more parameters.
  - Tasks were BCI and sleep, not seizure.
  - Source: [arXiv 2507.01196](https://arxiv.org/html/2507.01196)
- **Brain4FMs** (Feb 2026, 15 FMs) is a counterpoint:
  - "large-scale pretraining yields more transferable representations than task-specific supervised training in most clinical diagnosis settings."
  - SPaRCNet beat only a subset of FMs on epilepsy tasks.
  - Source: [arXiv 2602.11558](https://arxiv.org/html/2602.11558v1)
- **Leakage by the model authors themselves**:
  - CBraMod notes that TUEV is a subset of TUEG. It re-pretrained with TUEV/TUAB excluded; performance dropped slightly (TUAB AUROC 0.9227 to 0.9156) — [CBraMod](https://arxiv.org/pdf/2412.07236)
  - LUNA and S-CEReBrO explicitly exclude downstream subjects from pretraining — [LUNA](https://arxiv.org/pdf/2510.22257), [S-CEReBrO](https://arxiv.org/pdf/2607.27913)
  - LaBraM does not report an exclusion ablation. I did not verify this directly.
- **Split protocol**: the CHB-MIT test set in the BIOT/CBraMod protocol is only 2 patients (22, 23). This explains the large standard deviations of ±0.03–0.05 — [CBraMod](https://arxiv.org/pdf/2412.07236)
- **Other surveys** to consult: EEG-Bench (clinical) — [arXiv 2512.08959](https://arxiv.org/pdf/2512.08959); "EEG Foundation Models: A Critical Review" — [arXiv 2507.11783](https://arxiv.org/html/2507.11783v2). Neither was read in detail.

### Inferences
- A student should always report a strong small supervised baseline (EEGNet or a CNN-Transformer, and SzCORE-style classical features) plus a random-init version of the same FM architecture. They should also exclude any TUH subjects that appear in the pretraining corpus, or at least document the overlap.

### Gaps
- AdaBrain-Bench numbers for TUAB-style clinical anomaly detection were not extracted.
- The per-model TUSZ table in EEG-FM-Bench and NeuroAtlas was not extracted.

---

## Q5. Parameter-efficient fine-tuning (LoRA, adapters, linear probing) for EEG

### Takeaway
Linear probing of EEG FMs is consistently weak, especially for seizure detection. Full fine-tuning or partial fine-tuning (the top layer or about 9% of params) recovers most of the performance. LoRA can reduce LaBraM's trainable parameters about 85× (5.8M to 67.7k) without loss. For 2–7M-param models, full fine-tuning is already cheap on a consumer GPU, so PEFT matters mainly for larger models (REVE, LUNA-Huge, NeuroLM) or for adapting to each patient.

### Cited Findings
- **LoRA on LaBraM**: rank 2 is optimal, with 67,749 trainable params (vs 5.8M) and 77.7% mean accuracy. It works best when multiple components are adapted together. Tasks were BCI and sleep — [Lee et al. 2025](https://arxiv.org/html/2507.01196)
- **Self-supervised PEFT** (Dani & Liebe, Aug 2026): updating only the last encoder layer (about 9% of params: 0.92M of 3.19M for BIOT, 0.44M of 4.92M for CBraMod):

  | Task | Model | Linear probe | Self-supervised adaptation |
  |---|---|---|---|
  | CHB-MIT AUPRC | BIOT | 1.53% | 31.52% |
  | TUAB AUPRC | CBraMod | 56.44% | 77.16% |
  | TUEV F1 | CBraMod | 35.82% | 40.91% |

  - Peak performance needs only 20–50% of the unlabeled data.
  - Source: [arXiv 2608.24727](https://arxiv.org/html/2608.24727)
- **EEG-FM-Bench**: full-parameter fine-tuning consistently beats frozen backbones — [arXiv 2508.17742](https://arxiv.org/html/2508.17742)
- **NeuroAtlas**: frozen linear probes give limited clinical utility — [NeuroAtlas](https://arxiv.org/html/2605.14698v1)
- **Stacked LoRA** for subject-adaptive EEG FMs (motor imagery) — [arXiv 2607.03094](https://arxiv.org/html/2607.03094v1)
- **Graph Adapter** for EEG FMs (PEFT with a graph adapter) — [ResearchGate](https://www.researchgate.net/publication/386111180_Graph_Adapter_of_EEG_Foundation_Models_for_Parameter_Efficient_Fine_Tuning)
- **LoRA on burst-suppression and CHB-MIT**: one study found LoRA "can close part of the generalization gap" under out-of-distribution tests — [arXiv 2606.20074](https://arxiv.org/pdf/2606.20074). This was a search snippet only.
- **Fine-tuning cost**: CBraMod's default fine-tuning is 50 epochs, lr 1e-4, AdamW — [CBraMod](https://arxiv.org/html/2412.07236). LUNA fine-tunes with batch size 512 per GPU on A100s — [LUNA](https://arxiv.org/pdf/2510.22257). Batch size can be reduced for consumer GPUs (inference, not tested).

### Inferences
- **Practical recommendation for a student with one consumer GPU or Colab, streaming seizure detection on TUSZ:**
  1. **CBraMod (4M)** is the best-documented and strongest small baseline. It has public weights and code, and full fine-tuning is cheap. It needs 5–10 s sliding windows, so latency is roughly the window length plus the stride.
  2. **S-CEReBrO (2.4M, pulp-bio/biofoundation)** is designed for bounded-memory continuous monitoring. It is the best match for a streaming thesis, but it is new (Sept 2026) with little independent replication.
  3. **CaMBrain (37M, causal Mamba-3)** is the only truly causal FM. Check whether weights are released and whether mamba_ssm installs on the target GPU (it needs recent CUDA). Its CHB-MIT split is not comparable to the others.
  4. **LUNA-Base (7M)** suits reduced or variable-channel montages.
  5. Avoid LaBraM-Large/Huge (no weights), NeuroLM-XL, BrainWave/Brant (100M–1B+), and REVE unless using LoRA.
  - Always compare against EEGNet or a CNN-Transformer and a random-init baseline, and evaluate with event-level SzCORE metrics.

### Gaps
- I found no study of LoRA or adapters specifically on TUSZ seizure detection.
- I found no measurement of VRAM or wall-clock time for fine-tuning these FMs on a consumer GPU. The feasibility claims above follow from parameter counts, not from reported measurements.
