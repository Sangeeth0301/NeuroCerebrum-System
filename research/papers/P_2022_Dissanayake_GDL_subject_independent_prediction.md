# P_2022_Dissanayake: Geometric deep learning for subject-independent epileptic seizure prediction using scalp EEG (IEEE JBHI 2022)

## Citation & Link
Dissanayake T., Fernando T., Denman S., Sridharan S., Fookes C. "Geometric Deep Learning for Subject Independent Epileptic Seizure Prediction Using Scalp EEG Signals." *IEEE Journal of Biomedical and Health Informatics* 26(2):527–538, 2022 (online July 2021). DOI: 10.1109/JBHI.2021.3100297. PMID 34314363.
- DOI: https://doi.org/10.1109/JBHI.2021.3100297
- Open-access accepted manuscript (QUT ePrints): https://eprints.qut.edu.au/212250/1/88918403.pdf
- Metadata and abstract: [Europe PMC API](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1109/JBHI.2021.3100297&resultType=core&format=json)
- **Companion paper by the same group:** "Deep Learning for Patient-Independent Epileptic Seizure Prediction Using Scalp EEG Signals," *IEEE Sensors Journal*, 2021.
  - QUT record: https://eprints.qut.edu.au/211270/
  - arXiv 2011.09581: https://arxiv.org/abs/2011.09581
  - Uses MFCC features with CNN and Siamese models. Accuracy is 88.81% and 91.54% on CHB-MIT. [arXiv](https://arxiv.org/abs/2011.09581)

## Venue type
Peer-reviewed journal (IEEE JBHI). The details below come from the author-accepted manuscript on QUT ePrints.

## Problem
Subject-specific predictors fail when a new patient has little or no labeled data. The paper builds **one subject-independent model** for preictal-vs-interictal classification on scalp EEG. It uses graph neural networks, and graphs are either fixed from the physical electrode grid or **synthesized per subject** by a network. [QUT PDF](https://eprints.qut.edu.au/212250/1/88918403.pdf)

## Dataset
All details from the [QUT PDF](https://eprints.qut.edu.au/212250/1/88918403.pdf).
- **CHB-MIT**: 23 subjects, 23 bipolar channels. Recordings with 22 channels are padded by duplicating the physically closest channel.
- **Siena Scalp EEG**: 15 subjects, 29 channels (referential). The paper describes this as the first subject-independent prediction study on Siena.
- **Preictal = 1 h before onset.** The paper's phrase "one-hour early seizure prediction window" is the assumed preictal duration, **not** an SPH. No SPH or SOP is defined.
- **Interictal (CHB-MIT)**: segments from before the preictal period and more than 4 h after seizure onset.
  - For Siena, the small dataset forced sampling interictal segments **immediately before the preictal window** for most subjects.
- **Segments**: 10 s. Preictal segments overlap by 50% (for balance) and interictal segments do not overlap. This gives a balanced set of about 300k samples on CHB-MIT.

## Approach
All details from the [QUT PDF](https://eprints.qut.edu.au/212250/1/88918403.pdf).
- **Features:** MFCC feature maps per channel (node features), carried over from the group's 2021 work.
- **DR-Net:** an LSTM-based dimensionality-reduction network that maps per-channel MFCC maps to node embeddings. For example, CHB-MIT input [23×26×254] becomes output [23×72].
- **C-GNN:** a Chebyshev spectral graph convolution network (polynomial order K) that classifies preictal vs interictal.
- **Graphs:**
  1. **Distance-based adjacency** A0–A5 from the 10-20 grid, thresholded at different node degrees.
  2. **GSN (graph synthesis network)**, which learns subject-specific adjacency. It has two settings:
     - *Fully-Learned*: adjacency learned from scratch under connectivity constraints [n, e].
     - *Partially-Learned*: A0 plus learned edges.
- **Loss:** 0.8·BCE + 0.1·consistency loss + 0.1·L1-matrix loss.
- **Training:** Adam, learning rate 0.001, PyTorch.

## Evaluation protocol
- **10-fold cross-validation on pooled segments from all subjects.** [QUT PDF, Tables III–VI](https://eprints.qut.edu.au/212250/1/88918403.pdf)
- This is **not leave-one-subject-out.** Segments from the same subject, and from the same seizure (with 50%-overlapping preictal windows), can appear in both train and test folds. "Subject-independent" here means a single pooled model, **not** generalization to unseen patients. This is a **major leakage risk** and likely inflates accuracy.
- The paper states that cross-dataset evaluation (CHB-MIT to Siena) was not possible because of differing montages. [QUT PDF](https://eprints.qut.edu.au/212250/1/88918403.pdf)
- There is no event-level alarm evaluation, no SOP/SPH, no FPR/h and no surrogate or random-predictor test.

## Key results (numbers)

| Setting | CHB-MIT accuracy | Siena accuracy |
|---|---|---|
| Best distance-based adjacency (10-fold CV) | **95.38%** (A0) | **96.05%** (A3) |
| Other distance-based matrices | 95.08–95.27% | 95.67–95.86% |
| Fully-/Partially-Learned GSN graphs | about 94.3–95.1% | about 95.1–95.6% |

Sources: [abstract](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1109/JBHI.2021.3100297&resultType=core&format=json); [QUT PDF Tables IV–V](https://eprints.qut.edu.au/212250/1/88918403.pdf)

- Table VI of the manuscript also lists sensitivity, specificity and AUC-ROC for the proposed models. AUC values fall roughly between 0.969 and 0.992. The PDF text extraction garbled the column alignment, so **the exact per-model sensitivity, specificity and AUC could not be verified.** Check the original Table VI before citing.
- The paper compares against its own prior subject-independent work on CHB-MIT, which reported 91.54% accuracy. [arXiv 2011.09581](https://arxiv.org/abs/2011.09581)

## Limitations
- The authors acknowledge:
  - graph synthesis is non-deterministic;
  - t-SNE shows the LSTM embedding does not fully separate subjects;
  - no cross-domain test was possible.

  [QUT PDF](https://eprints.qut.edu.au/212250/1/88918403.pdf)
- Our additional concerns:
  - pooled 10-fold CV, not leave-one-subject-out;
  - segment-level accuracy only, with no alarm or FPR/h;
  - interictal segments are taken immediately before the preictal window on Siena (a non-standard, leakage-prone choice);
  - a 1-h preictal window with no SPH.

## Relevance to our project
- It is the most-cited "subject-independent scalp-EEG prediction" paper, but its **protocol is not truly cross-patient**. Do not use its 95% as a cross-patient baseline number. Cite it as an example of the evaluation pitfall.
- Useful ideas for TUSZ:
  - a graph over bipolar channels, where the TUSZ TCP montage maps naturally to a fixed adjacency;
  - MFCC or spectral node features;
  - subject-adaptive graphs.
- Our TUSZ study should re-evaluate this kind of model with **patient-disjoint splits**. The official TUSZ train/dev/eval splits are patient-disjoint.
