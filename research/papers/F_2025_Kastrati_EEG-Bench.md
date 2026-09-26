# EEG-Bench: A Benchmark for EEG Foundation Models in Clinical Applications

## Citation & Link
- Kastrati A., Bürki J., Lauer J., Xuan C., Iaquinto R., Wattenhofer R. (ETH Zurich) (2025). The paper footer reads "39th Conference on Neural Information Processing Systems (NeurIPS 2025)".
  - PDF: [ETH TIK publication server](https://tik-db.ee.ethz.ch/file/1e09e7f339cb0dfcf9ec74bd2bb51c24/)
  - Also on [ResearchGate](https://www.researchgate.net/publication/398560481_EEG-Bench_A_Benchmark_for_EEG_Foundation_Models_in_Clinical_Applications)
- Code: [github.com/ETH-DISCO/EEG-Bench](https://github.com/ETH-DISCO/EEG-Bench) (GPL-3.0) — [PDF](https://tik-db.ee.ethz.ch/file/1e09e7f339cb0dfcf9ec74bd2bb51c24/)

## Venue type
Peer-reviewed at NeurIPS 2025. **Caveat:** the 4-page format suggests a NeurIPS 2025 *workshop* paper rather than a main-track or Datasets & Benchmarks paper, because workshop papers also carry this footer. I could not confirm which track, so label it "NeurIPS 2025 (likely workshop)".

## Problem
Foundation models are usually tested on BCI tasks plus TUAB and TUEV. This paper asks whether they actually beat simple classical baselines on a broad set of *clinical* diagnostic and event-detection tasks under strict cross-subject evaluation — [PDF](https://tik-db.ee.ethz.ch/file/1e09e7f339cb0dfcf9ec74bd2bb51c24/)

## Dataset
14 public datasets and 11 tasks:
- TUAB (abnormal): 2,383 subjects, 47.5 days of EEG.
- TUEP (epilepsy): 200 subjects.
- TUAR (artifacts).
- **CHB-MIT (seizure)**: 23 subjects, 686 recordings, 41 days.
- Sleep-Telemetry.
- Parkinson's, OCD, mild TBI and schizophrenia cohorts.
The seizure task has 3,515,547 non-seizure and 11,525 seizure samples, which is extreme class imbalance — [PDF Tables 1–2](https://tik-db.ee.ethz.ch/file/1e09e7f339cb0dfcf9ec74bd2bb51c24/)

## Approach
- Classical baselines: LDA and SVM on handcrafted features from the Brainfeatures toolbox — [PDF](https://tik-db.ee.ethz.ch/file/1e09e7f339cb0dfcf9ec74bd2bb51c24/)
- Foundation models: BENDR, Neuro-GPT and LaBraM-Base, all using the released weights with full fine-tuning (Neuro-GPT encoder only). Signals were band-passed at 0.1–75 Hz, notch-filtered and resampled to 200 Hz. BENDR and Neuro-GPT need fixed channels, so missing channels were zero-padded or mapped arbitrarily. Long recordings were split into chunks, embedded, and the embeddings averaged — [PDF](https://tik-db.ee.ethz.ch/file/1e09e7f339cb0dfcf9ec74bd2bb51c24/)

## Evaluation protocol
Strict cross-subject splits with fixed test splits, 5 seeds and balanced accuracy (weighted F1 in the appendix). Compute totalled 270 A100-hours — [PDF](https://tik-db.ee.ethz.ch/file/1e09e7f339cb0dfcf9ec74bd2bb51c24/)

## Key results (numbers)
Balanced accuracy — [PDF Table 3](https://tik-db.ee.ethz.ch/file/1e09e7f339cb0dfcf9ec74bd2bb51c24/)

| Task | SVM | LDA | BENDR | Neuro-GPT | LaBraM |
|---|---|---|---|---|---|
| Abnormal (TUAB) | 0.722 | 0.677 | 0.717±.003 | 0.696±.005 | **0.838±.011** |
| Epilepsy (TUEP) | 0.531 | 0.531 | **0.740±.015** | 0.734±.010 | 0.565±.017 |
| **Seizure** | 0.572 | 0.529 | 0.501±.001 | 0.500±.000 | **0.588±.011** |
| Binary artifact | 0.745 | 0.705 | 0.535 | 0.711 | **0.756** |
| Multiclass artifact | **0.437** | 0.325 | 0.192 | 0.226 | 0.430 |
| Sleep stages | 0.652 | **0.671** | 0.169 | 0.166 | 0.192 |
| mTBI | 0.626 | **0.813** | 0.640 | 0.646 | 0.740 |
| Schizophrenia | **0.679** | 0.547 | 0.471 | 0.545 | 0.543 |

- The authors conclude that "simpler models often remain competitive, particularly under clinical distribution shifts". BENDR and Neuro-GPT learned nothing on seizure detection and sleep staging, which the authors attribute to those datasets sharing no channels with the pretraining setup — [PDF](https://tik-db.ee.ethz.ch/file/1e09e7f339cb0dfcf9ec74bd2bb51c24/)
- On seizure detection, **LaBraM (0.588) beat an SVM on handcrafted features by only 1.6 points** — [PDF](https://tik-db.ee.ethz.ch/file/1e09e7f339cb0dfcf9ec74bd2bb51c24/)

## Limitations
- The authors say only a few foundation models and classical pipelines were included, and specialised models such as dedicated seizure detectors are missing — [PDF](https://tik-db.ee.ethz.ch/file/1e09e7f339cb0dfcf9ec74bd2bb51c24/)
- Newer models (CBraMod, EEGPT, BIOT) are not evaluated. Only balanced accuracy is reported, and there are no event-level seizure metrics.
- LaBraM was pretrained on TUEP and TUAR ([LaBraM](https://arxiv.org/pdf/2405.18765)), which are also test tasks here, so those rows may be optimistic for LaBraM (inference). Its weak TUEP score (0.565) shows that overlap does not guarantee a gain.
- The venue track (main or workshop) is unconfirmed.

## Relevance to our project
- This is the strongest peer-reviewed evidence that **off-the-shelf foundation models are nearly useless for seizure-level tasks without careful adaptation**. Balanced accuracy of about 0.50–0.59 on seizure detection is roughly at the level of a handcrafted-feature SVM.
- We should always include a classical baseline (SVM or LDA on spectral and line-length features) and a small supervised CNN alongside any foundation model.
- Fixed-channel models (BENDR, Neuro-GPT) should be avoided for TUSZ because of its variable montages.
