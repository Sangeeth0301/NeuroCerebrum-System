# Raghu et al. 2020 — EEG-based multi-class seizure type classification using CNN and transfer learning

## Citation & Link
- S. Raghu, N. Sriraam, Y. Temel, S. V. Rao, P. L. Kubben. "EEG based multi-class seizure type classification using convolutional neural network and transfer learning." *Neural Networks* 124:202–212, 2020. DOI: 10.1016/j.neunet.2020.01.017; PMID 32018158 — https://www.sciencedirect.com/science/article/abs/pii/S0893608020300198 ; metadata: https://api.semanticscholar.org/graph/v1/paper/10.1016/j.neunet.2020.01.017
- Open-access (green) record at Maastricht University CRIS (PDF listed, Taverne licence; direct download failed in this review): https://cris.maastrichtuniversity.nl/en/publications/eeg-based-multi-class-seizure-type-classification-using-convoluti/

## Venue type
Peer-reviewed journal (Neural Networks, Elsevier). **Only the abstract was accessible** (ScienceDirect and PubMed blocked; CRIS PDF not downloadable). All numbers below are **abstract-only** unless noted.

## Problem
Classify seven seizure variants plus non-seizure EEG (8 classes) from scalp EEG, motivated by pre-surgical evaluation. — https://api.semanticscholar.org/graph/v1/paper/10.1016/j.neunet.2020.01.017

## Dataset
- Temple University Hospital EEG corpus, TUSZ **v1.4.0** (version per search-result summary, not verified in full text) — https://www.semanticscholar.org/paper/EEG-based-multi-class-seizure-type-classification-Raghu-Sriraam/d3da7fe00d8a1767726e865256b62b081b2b8630
- Classes: simple partial, complex partial, focal non-specific, generalized non-specific, absence, tonic, tonic-clonic, and non-seizure (myoclonic excluded). — abstract, https://api.semanticscholar.org/graph/v1/paper/10.1016/j.neunet.2020.01.017
- How rare types were handled (SPSZ and TNSZ each come from only 2 patients in TUSZ v1.4.0 per https://arxiv.org/pdf/1912.04968): not determined (gap).

## Approach
- 19-channel EEG converted to a **spectrogram stack** (STFT) and fed as an image to CNNs. — abstract
- Two modalities: (1) transfer learning / fine-tuning of an ImageNet-pretrained CNN; (2) pretrained CNN as fixed feature extractor + SVM classifier.
- Ten pretrained networks compared: AlexNet, VGG16, VGG19, SqueezeNet, GoogLeNet, InceptionV3, DenseNet201, ResNet18, ResNet50, ResNet101. — abstract
- No graph construction; no localization.

## Evaluation protocol
- Split details (patient-wise vs segment/seizure-wise, k-fold) **could not be verified** — full text not accessible. **Leakage flag: UNKNOWN / likely non-patient-wise.** Tang et al. 2022 list Raghu et al. among prior studies whose performance differs between majority and minority types, and compare only against works that "test on unseen patients" (Asif; Iesmantas & Alzbutas) — they did not include Raghu in that comparison, which suggests Raghu's protocol was not patient-independent (inference) — https://arxiv.org/pdf/2104.08336
- Metric: accuracy (not weighted F1) reported in the abstract, so not directly comparable with the wF1-based TUSZ literature.

## Key results (numbers)
- Best accuracy **82.85%** (GoogLeNet, transfer learning) and **88.30%** (InceptionV3 features + SVM). — abstract only, https://api.semanticscholar.org/graph/v1/paper/10.1016/j.neunet.2020.01.017
- "CNN based approach outperformed conventional feature and clustering based approaches" — abstract.
- Per-class F1 / weighted F1: not available (gap).

## Limitations
- Accuracy on an 8-class, heavily imbalanced set is dominated by majority classes (non-seizure, FNSZ, GNSZ).
- Unclear patient independence; 2-patient classes (SPSZ, TNSZ) cannot be patient-wise tested.
- ImageNet-pretrained 2-D CNNs treat the spectrogram stack as an image, ignoring electrode topology (criticism in https://arxiv.org/pdf/2104.08336).
- No spatial/localization output.

## Relevance to our project
- Useful as a representative "spectrogram + pretrained CNN" baseline and for the idea of including a **non-seizure** class (joint detection + typing), which matches a pipeline that must decide seizure/no-seizure and type at onset.
- Its numbers should not be used as a head-to-head target because metric (accuracy) and split are not comparable to patient-wise wF1.
