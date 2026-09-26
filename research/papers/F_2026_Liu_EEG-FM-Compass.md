# EEG-FM-Compass: Progress, Benchmarking, and Future Directions for EEG Foundation Models

## Citation & Link
- Liu D., Chen Y., Chen Z., Cui Z., Wen Y., An J., Luo J., Wu D. (2026). *National Science Review*, advance article (published 3 Aug 2026). DOI: [10.1093/nsr/nwag466](https://academic.oup.com/nsr/advance-article/doi/10.1093/nsr/nwag466/8750569)
- arXiv: [2601.17883](https://arxiv.org/abs/2601.17883). v1 was titled "EEG Foundation Models: Progresses, Benchmarking, and Open Problems" — [HF papers](https://huggingface.co/papers/2601.17883)

## Venue type
Peer-reviewed journal (National Science Review, Oxford University Press), 2026. It combines a review with a benchmark.

## Problem
EEG foundation models are compared under inconsistent protocols. This paper asks whether they really beat specialist supervised models when evaluated in a standardised way, whether linear probing is enough, and whether bigger models generalise better — [arXiv abstract](https://arxiv.org/abs/2601.17883)

## Dataset
13 datasets covering 9 BCI paradigms. Evaluation uses cross-subject generalisation and within-subject few-shot calibration — [arXiv abstract](https://arxiv.org/abs/2601.17883); [NSR](https://academic.oup.com/nsr/advance-article/doi/10.1093/nsr/nwag466/8750569)
- **I could not confirm whether TUAB, TUEV, TUSZ or CHB-MIT are among the 13 datasets.** The full text exceeded the fetch size limit, so treat this paper as BCI-centred evidence.

## Approach
- A review of **55** representative EEG foundation models, organised in a taxonomy of data standardisation, architecture and self-supervised pretraining strategy — [arXiv abstract](https://arxiv.org/abs/2601.17883)
- A benchmark of **12 open-source foundation models** against specialist baselines trained from scratch. It compares full fine-tuning with linear probing — [arXiv abstract](https://arxiv.org/abs/2601.17883)
- A secondary summary says that under linear probing "many foundation models fail to match or surpass task-specific baseline EEGConformer". This quote comes from search-engine summaries of the paper, not the full text — [search result summary of arXiv 2601.17883](https://www.alphaxiv.org/abs/2601.17883)

## Evaluation protocol
Cross-subject leave-out splits and few-shot within-subject calibration, each run under both full fine-tuning and linear probing — [arXiv](https://arxiv.org/abs/2601.17883). Split details are unverified.

## Key results (numbers)
- I could not extract per-dataset numbers (see Gaps). The three headline conclusions, verbatim from the abstract:
  1. "linear probing is frequently insufficient"
  2. specialist models trained from scratch "remain competitive across many tasks"
  3. "larger FMs do not necessarily yield better generalization performance under current data regimes and training practices"
  — [arXiv abstract](https://arxiv.org/abs/2601.17883); [NSR](https://academic.oup.com/nsr/advance-article/doi/10.1093/nsr/nwag466/8750569)

## Limitations
- The task set is centred on BCI paradigms. Clinical TUH and seizure coverage is unconfirmed.
- I could not verify the exact numbers or which 12 models were included, so re-extract Tables from the NSR PDF before quoting any figure.

## Relevance to our project
- This is the peer-reviewed, journal-level "reality check". It supports planning a **specialist baseline, full fine-tuning (not only linear probing), and a Base-size model** instead of chasing scale.
- Related work agrees:
  - A peer-reviewed critical review in *Journal of Neural Engineering* (2026) — [IOPscience 10.1088/1741-2552/ae4455](https://iopscience.iop.org/article/10.1088/1741-2552/ae4455)
  - The **preprint** EEG-FM-Audit (2026) reports that a supervised TS-SEFFNet matches or beats LaBraM and EEGPT on TUAB/TUEV, with a TUAB F1 difference of about 0.008. This is from a search snippet only and not verified — [arXiv 2605.26910](https://arxiv.org/pdf/2605.26910)
