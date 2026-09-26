# D_2018_Shah: The Temple University Hospital Seizure Detection Corpus (Frontiers in Neuroinformatics 2018)

## Citation & Link
Shah V., von Weltin E., Lopez S., McHugh J.R., Veloso L., Golmohammadi M., Obeid I., Picone J. "The Temple University Hospital Seizure Detection Corpus." Frontiers in Neuroinformatics 12:83, 2018. DOI: 10.3389/fninf.2018.00083
- Open access: https://www.frontiersin.org/journals/neuroinformatics/articles/10.3389/fninf.2018.00083/full
- PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC6246677/

## Venue type
Peer-reviewed journal. This is a dataset/resource paper. It predates 2019 but is included because it is the canonical reference for TUSZ.

## Problem
Seizure-detection research relied on small corpora such as CHB-MIT (23 subjects), whose results "have not been representative of clinical performance." The paper releases a large, clinically realistic corpus of annotated seizures. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6246677/)

## Dataset
- TUSZ **v1.2.0** (December 2017): 315 patients (265 train, 50 eval), 822 sessions (280 with seizures), over 504 hours, of which about 36 h (7%) is seizure. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6246677/)
- The train/eval split is patient-disjoint. The eval set was enriched to about 34% seizure prevalence and demographically balanced. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6246677/)
- Sessions were selected in three steps: NLP of neurologist reports (NegEx, 99% accuracy), Persyst P13, and the AutoEEG deep-learning system. Trained students then annotated them, and the annotations were validated against neurologists. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6246677/)

## Approach
Not applicable: this is a corpus paper, not a detector.

## Evaluation protocol
Not included in this paper. The NEDC group defines OVLP and TAES scoring in separate papers that are not reviewed here.

## Key results (numbers)
My extraction found no baseline sensitivity/FA numbers and no discussion of latency in this paper. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6246677/)

## Limitations
- The paper describes v1.2.0. Later work uses v1.4 (Saab 2020), v1.5.2 (Lee 2022) and v2.0.x (SeizureTransformer and Zabihi 2026), which have more patients and revised annotations. Results across versions are not strictly comparable.
- The eval set is enriched with seizures, so it does not reflect real-world prevalence.

## Relevance to our project
- Cite it as the dataset reference.
- Our project should use the official **v2.0.x Train/Dev/Eval** partition, stay patient-independent, and state the version we use, because splits and versions differ across the literature.
