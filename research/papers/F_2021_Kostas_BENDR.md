# BENDR: Using Transformers and a Contrastive Self-Supervised Learning Task to Learn From Massive Amounts of EEG Data

## Citation & Link
- Kostas D., Aroca-Ouellette S., Rudzicz F. (2021). *Frontiers in Human Neuroscience*. DOI: 10.3389/fnhum.2021.653659 — [Frontiers full text](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2021.653659/full)
- Code + pretrained weights: [github.com/SPOClab-ca/BENDR](https://github.com/SPOClab-ca/BENDR) (link given in the paper — [Frontiers](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2021.653659/full))

## Venue type
Peer-reviewed journal article (Frontiers in Human Neuroscience, 2021). Historical "first-generation" EEG foundation model; included as the baseline everything after it compares against.

## Problem
Can a wav2vec-2.0-style self-supervised model pretrained on a very large unlabelled clinical EEG corpus learn representations that transfer to many downstream EEG tasks and subjects? — [Frontiers](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2021.653659/full)

## Dataset
- Pretraining: Temple University Hospital EEG Corpus (TUEG) v1.1 and v1.2, about 1.5 TB of EDF recordings from more than 10,000 subjects — [Frontiers](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2021.653659/full)
- Downstream: MMI (motor imagery), BCIC IV-2a, ERN, sleep staging (SSC) and P300. **No TUAB/TUEV/TUSZ/CHB-MIT downstream evaluation** — [Frontiers](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2021.653659/full)

## Approach
- Input: 19 standard 10-20 channels plus 1 amplitude/reference channel (20 in total), resampled to 256 Hz; 60 s pretraining windows (15,360 samples) — [Frontiers](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2021.653659/full)
- Tokenisation and architecture: six 1D convolutional blocks with 512 filters each. They downsample the signal 96× (effective rate of about 2.67 Hz), producing "BENDR" vectors. A transformer (8 layers, 8 heads, model dimension 1536) with convolutional position encoding runs on top — [Frontiers](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2021.653659/full)
- Objective: a contrastive masked-span task adapted from wav2vec 2.0. Spans are masked and each masked position must pick out its true encoding from 20 distractors (cosine similarity, temperature 0.1) — [Frontiers](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2021.653659/full)
- Fine-tuning: task-specific heads on the pretrained encoder, with and without the transformer.

## Evaluation protocol
Five downstream datasets with downstream windows of 2–30 s, evaluated across subjects — [Frontiers](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2021.653659/full)

## Key results (numbers)
- Best reported results were MMI balanced accuracy 86.7%, BCIC accuracy 42.6%, ERN AUROC 0.65, SSC balanced accuracy 0.72 and P300 AUROC 0.72. These come from a summary of Table 2 and should be re-checked against the PDF before quoting — [Frontiers](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2021.653659/full)
- Later papers compared against BENDR under their own protocols. EEGPT (NeurIPS 2024) reports BENDR at BCIC-2A balanced accuracy 0.4899, BCIC-2B 0.7067, Sleep-EDFx 0.6655, KaggleERN 0.5672 and PhysioP300 0.6114 — [EEGPT, NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/4540d267eeec4e5dbd9dae9448f0b739-Abstract-Conference.html)
- In the clinical EEG-Bench, fully fine-tuned BENDR scored balanced accuracy 0.717 on TUAB abnormal detection, 0.740 on TUEP epilepsy and 0.501 on seizure detection (chance level) — [EEG-Bench (ETH)](https://tik-db.ee.ethz.ch/file/1e09e7f339cb0dfcf9ec74bd2bb51c24/)

## Limitations
- The authors say the results were "not competitive with more targeted solutions" except on MMI and SSC. They also note that spatial and temporal operations are not cleanly separated and that the convolutional position encoding has a limited receptive field (about 9 s) — [Frontiers](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2021.653659/full)
- It needs a fixed channel set. EEG-Bench had to zero-pad or arbitrarily map channels for CHB-MIT, and BENDR then failed on seizure detection (balanced accuracy 0.501) — [EEG-Bench](https://tik-db.ee.ethz.ch/file/1e09e7f339cb0dfcf9ec74bd2bb51c24/)
- **Leakage risk for our project:** BENDR was pretrained on all of TUEG v1.1/1.2. Because TUSZ recordings come from the TUH archive, a BENDR checkpoint may already have seen (unlabelled) TUSZ test-patient EEG. This is an inference; check which TUEG sessions overlap the TUSZ dev/eval splits.
- The paper does not report model parameter count or compute cost clearly. The summariser tool returned "over one billion parameters", which I could not confirm, so treat it as unverified.

## Relevance to our project
- This is the historical baseline and shows that raw TUEG self-supervision alone does not give strong transfer.
- It is a poor fit for seizure forecasting: fixed channels, 60 s pretraining context, and chance-level seizure detection in an independent clinical benchmark.
- Its main use for us is as a cautionary example about TUEG pretraining overlapping with TUSZ evaluation.
