# Karácsony et al. 2022: 3D video action-recognition deep learning for near real-time seizure classification

## Citation & Link
- Karácsony T, Loesch-Biffar AM, Vollmar C, Rémi J, Noachtar S, Cunha JPS. "Novel 3D video action recognition deep learning approach for near real time epileptic seizure classification." *Scientific Reports* 2022 (volume/article number not verified).
- DOI: [10.1038/s41598-022-23133-9](https://www.nature.com/articles/s41598-022-23133-9); PubMed [36379994](https://pubmed.ncbi.nlm.nih.gov/36379994/); open access [PMC9666544](https://pmc.ncbi.nlm.nih.gov/articles/PMC9666544) (full text read via [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9666544/fullTextXML)).

## Venue type
Peer-reviewed open-access journal (Scientific Reports).

## Problem
Automate semiology analysis (movement) from video to classify seizures as frontal lobe (FLE) vs temporal lobe (TLE) epilepsy vs non-epileptic events, aiming at 24/7 monitoring ([full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9666544/fullTextXML)).

## Dataset
- University of Munich epilepsy centre; 26 patients (15 FLE, 11 TLE); **115 seizures (78 FLE, 37 TLE)**; 686,664 frames (427 GB).
- Infrared + depth (3D) video from Kinect v2, 512x424, 30 fps.
- Source: [full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9666544/fullTextXML)

## Approach
- Preprocessing: Mask R-CNN patient detection (96.52% success) and depth-based cropping (95.65%).
- Clips of 60 frames (**2 s**).
- Features: Inflated 3D ConvNet (I3D), ImageNet-pretrained and Kinetics-400 fine-tuned.
- Classifiers: I3D head, LSTM (128/64 units), extended LSTM for temporal augmentation.
- Source: [full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9666544/fullTextXML)

## Evaluation protocol
5-fold cross-validation with leave-subjects-out splits; macro-averaged metrics for class imbalance ([full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9666544/fullTextXML)).

## Key results (numbers) — full text
- FLE vs TLE (LSTM): F1 **0.833 ± 0.061**, AUC **0.89 ± 0.08**, sensitivity (TLE) 0.870 ± 0.041, specificity 0.794 ± 0.157.
- FLE vs TLE vs non-epileptic (extended LSTM): F1 **0.763 ± 0.083**; per-class specificity 0.922-0.962, sensitivity 0.639-0.947.
- Near real time: operates on 2-s clips; explicit inference time not reported.
- Source: [full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9666544/fullTextXML)

## Limitations
Small, imbalanced single-centre dataset; subject-specific feature risk; temporal augmentation overfitted; special 3D camera setup.

## Relevance to our project
- Shows movement semiology carries type-discriminative information (FLE hypermotor vs TLE automatisms) — a "body reaction" per seizure type.
- TUSZ has no video; this is a literature prior only. It supports the idea that body reaction differs by seizure origin, which is what our module maps from seizure type.
- Not an early-warning method: classification after semiology appears. A review of the field: [Deep learning approaches for seizure video analysis (arXiv 2312.10930)](https://arxiv.org/pdf/2312.10930) (preprint, not peer-reviewed as fetched).
