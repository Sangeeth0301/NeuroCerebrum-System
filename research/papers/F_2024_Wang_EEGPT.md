# EEGPT: Pretrained Transformer for Universal and Reliable Representation of EEG Signals

## Citation & Link
- Wang G., Liu W., He Y., Xu C., Ma L., Li H. (Harbin Institute of Technology) (2024). *Advances in Neural Information Processing Systems 37 (NeurIPS 2024)*.
  - [NeurIPS proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/hash/4540d267eeec4e5dbd9dae9448f0b739-Abstract-Conference.html)
  - [PDF](https://proceedings.neurips.cc/paper_files/paper/2024/file/4540d267eeec4e5dbd9dae9448f0b739-Paper-Conference.pdf)
  - [Poster page](https://neurips.cc/virtual/2024/poster/93793)
- Code: [github.com/BINE022/EEGPT](https://github.com/BINE022/EEGPT)
- Not to be confused with other models called "EEGPT", for example the 2024–25 "EEGPT: Unleashing the potential of EEG generalist foundation model by autoregressive pre-training" preprint.

## Venue type
Peer-reviewed conference (NeurIPS 2024 main track).

## Problem
Masked reconstruction of raw EEG learns weak features because EEG has a low signal-to-noise ratio, and channel and sampling-rate mismatches break transfer. The authors propose aligning masked-part *representations* rather than only reconstructing raw signal, and they aim for strong performance under **linear probing** — [NeurIPS PDF](https://proceedings.neurips.cc/paper_files/paper/2024/file/4540d267eeec4e5dbd9dae9448f0b739-Paper-Conference.pdf)

## Dataset
- Pretraining data were BCI and task datasets: PhysioMI (MI/ME, 109 subjects), HGD (MI, 14 subjects), TSU (SSVEP, 35 subjects), SEED (emotion, 15 subjects) and M3CV (multi-paradigm, 106 subjects). **No TUH data was used in pretraining** — [NeurIPS PDF, Table 1](https://proceedings.neurips.cc/paper_files/paper/2024/file/4540d267eeec4e5dbd9dae9448f0b739-Paper-Conference.pdf)
- The paper gives no total hour count (see Gaps).
- Downstream data: BCIC-2A, BCIC-2B, Sleep-EDFx, KaggleERN, PhysioP300, **TUAB (2,383 subjects)** and **TUEV (288 subjects)**. No TUSZ or CHB-MIT — [NeurIPS PDF](https://proceedings.neurips.cc/paper_files/paper/2024/file/4540d267eeec4e5dbd9dae9448f0b739-Paper-Conference.pdf)

## Approach
- Input: **4 s crops** at 256 Hz (T = 1024), average reference, scaled to mV, over up to 58 electrodes. Patches are 64 samples (**250 ms**) per channel — [NeurIPS PDF §3](https://proceedings.neurips.cc/paper_files/paper/2024/file/4540d267eeec4e5dbd9dae9448f0b739-Paper-Conference.pdf)
- Architecture: ViT-style encoder, predictor and reconstructor. S learnable "summary tokens" (similar to CLS tokens) summarise each time patch, and a local spatio-temporal embedding handles differing electrode sets — [NeurIPS PDF](https://proceedings.neurips.cc/paper_files/paper/2024/file/4540d267eeec4e5dbd9dae9448f0b739-Paper-Conference.pdf)
- Pretraining ("dual self-supervised") has two losses:
  - Spatio-temporal representation alignment: predicted features of masked parts are aligned with the full-signal encoder features, similar to JEPA.
  - Mask-based reconstruction of the raw signal.
  - Masking covers 50% of time patches and 80% of channel patches — [NeurIPS PDF](https://proceedings.neurips.cc/paper_files/paper/2024/file/4540d267eeec4e5dbd9dae9448f0b739-Paper-Conference.pdf)
- Size: the abstract says "10 million parameters". The TUAB/TUEV tables list "Ours" as 25M and "Ours-Tiny" as 4.7M — [NeurIPS PDF](https://proceedings.neurips.cc/paper_files/paper/2024/file/4540d267eeec4e5dbd9dae9448f0b739-Paper-Conference.pdf). This inconsistency is in the paper itself.
- Adaptation: linear probing, meaning a frozen encoder with an adaptive spatial filter and a linear head. There is also a full-fine-tuning ablation — [NeurIPS PDF App. A.3](https://proceedings.neurips.cc/paper_files/paper/2024/file/4540d267eeec4e5dbd9dae9448f0b739-Paper-Conference.pdf)

## Evaluation protocol
For TUAB and TUEV the authors used "the same configuration as BIOT", meaning the official split with an 80/20 train/validation split of training patients and 5 seeds — [NeurIPS PDF](https://proceedings.neurips.cc/paper_files/paper/2024/file/4540d267eeec4e5dbd9dae9448f0b739-Paper-Conference.pdf)

## Key results (numbers)
From [NeurIPS PDF Tables 2–3, 11](https://proceedings.neurips.cc/paper_files/paper/2024/file/4540d267eeec4e5dbd9dae9448f0b739-Paper-Conference.pdf).

**TUAB**

| Model | Params | Balanced Acc | AUROC |
|---|---|---|---|
| ST-Transformer | 3.5M | 0.7966±0.0023 | 0.8707±0.0019 |
| BIOT | 3.2M | 0.7959±0.0057 | 0.8815±0.0043 |
| EEGPT-Tiny | 4.7M | 0.7959±0.0021 | 0.8716±0.0041 |
| EEGPT | 25M | 0.7983±0.0030 | 0.8718±0.0050 |
| EEGPT, no pretraining (random init) | 25M | 0.7553±0.0014 | 0.8260±0.0018 |

**TUEV**

| Model | Balanced Acc | Weighted F1 | Kappa |
|---|---|---|---|
| BIOT | 0.5281±0.0225 | 0.7492±0.0082 | 0.5273±0.0249 |
| EEGPT-Tiny | 0.5670±0.0066 | 0.7535±0.0097 | 0.5085±0.0173 |
| EEGPT | 0.6232±0.0114 | 0.8187±0.0063 | 0.6351±0.0134 |

- The authors themselves say that TUAB performance is "comparable to BIOT". On TUEV they report +9.5% balanced accuracy and +6.9% weighted F1 over BIOT — [NeurIPS PDF](https://proceedings.neurips.cc/paper_files/paper/2024/file/4540d267eeec4e5dbd9dae9448f0b739-Paper-Conference.pdf)
- EEGPT is **below LaBraM-Base** on both TUAB (balanced accuracy 0.8140 / AUROC 0.9022) and TUEV (0.6409 / kappa 0.6637) — [LaBraM](https://arxiv.org/pdf/2405.18765). The authors explain the gap: LaBraM's pretraining "also contains the TUEG dataset that is similar to the TUAB and TUEV distributions" — [NeurIPS PDF](https://proceedings.neurips.cc/paper_files/paper/2024/file/4540d267eeec4e5dbd9dae9448f0b739-Paper-Conference.pdf)
- Pretraining helps: moving from random initialisation to pretrained weights gives +4.3 points of balanced accuracy and +4.6 points of AUROC on TUAB (see the table above).

## Limitations
- The pretraining data contain no clinical or TUH EEG, which likely explains the weaker TUH results (the authors' own explanation).
- 4 s inputs at a fixed 256 Hz are very short for seizure forecasting (inference).
- Parameter count is reported inconsistently (10M vs 25M).
- The authors discuss limitations in Appendix H — [NeurIPS PDF checklist](https://proceedings.neurips.cc/paper_files/paper/2024/file/4540d267eeec4e5dbd9dae9448f0b739-Paper-Conference.pdf). The exact wording was not extracted.
- No seizure-specific evaluation.

## Relevance to our project
- EEGPT has **no TUH data in pretraining**, which makes it the cleanest option for a leakage-free TUSZ experiment. Its gains on TUH tasks are modest, however.
- Its linear-probing design allows a low-cost frozen-feature baseline: 4 s embeddings aggregated over a longer preictal horizon by a small temporal model.
- It gives direct evidence that **in-domain (TUH-like) pretraining data matter** for TUH downstream tasks.
