# Hippocampal network activity forecasts epileptic seizures (Khambhati et al., 2024)

## Citation & Link
Khambhati AN, Chang EF, Baud MO, Rao VR. "Hippocampal network activity forecasts epileptic seizures." *Nature Medicine* 30:2787-2790 (2024) (volume and pages from memory; verify).
- DOI: https://doi.org/10.1038/s41591-024-03149-6
- Publisher page: https://www.nature.com/articles/s41591-024-03149-6 (not open access; Europe PMC lists no PMC copy — [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.1038/s41591-024-03149-6%22&resultType=core&format=json))
- Figure code: https://github.com/khambhati-lab/pub-2024-hippocampal-seizure-forecasting
- Open-access commentary: Englot DJ, "Chasing the Holy Grail: Seizure Prediction Through Neural Cycles," *Epilepsy Currents* 2025 — https://pmc.ncbi.nlm.nih.gov/articles/PMC11556539/

**Source caveat:** the full text was paywalled. All numbers below come from the **abstract** or the **Englot commentary**, not from the primary full text.

## Venue type
Peer-reviewed journal (Nature Medicine), brief communication-style retrospective cohort study.

## Problem
Cycle-based forecasting needs months of baseline data. Can a short snapshot of background hippocampal activity (functional connectivity) indicate where a patient is in their seizure-risk cycle, and forecast risk without a long baseline? — [Europe PMC abstract](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22Hippocampal%20network%20activity%20forecasts%20epileptic%20seizures%22&resultType=core&format=json)

## Dataset
- 15 adults with **bitemporal (bilateral mesial temporal) epilepsy** with the RNS System, providing chronic intracranial hippocampal recordings. Retrospective. — [abstract](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22Hippocampal%20network%20activity%20forecasts%20epileptic%20seizures%22&resultType=core&format=json); [Englot commentary](https://pmc.ncbi.nlm.nih.gov/articles/PMC11556539/)
- Input: **90-s** interictal ECoG clips from 4 bipolar channels. — [Englot commentary](https://pmc.ncbi.nlm.nih.gov/articles/PMC11556539/)

## Approach
- Functional connectivity (phase-based, within and between hippocampi) computed from 90-s clips. Multidien IEA cycles estimated with Morlet wavelets, and connectivity patterns related to cycle phase. — [Englot commentary](https://pmc.ncbi.nlm.nih.gov/articles/PMC11556539/)
- An FC biomarker, conserved across individuals, used to forecast 24-h seizure likelihood. — [abstract](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22Hippocampal%20network%20activity%20forecasts%20epileptic%20seizures%22&resultType=core&format=json)

## Evaluation protocol
Retrospective. Compared with benchmark cycle-based (IEA) forecasting models that need months of baseline. The biomarker was reported to "generalize across individuals," which suggests cross-patient validation, but I could not confirm the exact split or the chance-comparison method from the full text. — [abstract](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22Hippocampal%20network%20activity%20forecasts%20epileptic%20seizures%22&resultType=core&format=json)

## Key results (numbers)
- Hippocampal FC fluctuated in multiday cycles that mirrored seizure-likelihood cycles. — [abstract](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22Hippocampal%20network%20activity%20forecasts%20epileptic%20seizures%22&resultType=core&format=json)
- The FC biomarker from 90-s clips forecast 24-h seizure likelihood "as accurately as" cycle-based models needing months of data. — [abstract](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22Hippocampal%20network%20activity%20forecasts%20epileptic%20seizures%22&resultType=core&format=json)
- The commentary quotes "an AUC of 0.72 +/- 0.03", but it is ambiguous whether this refers to the IEA benchmark or the FC model. **Unverified; do not cite without checking the full text.** — [Englot commentary](https://pmc.ncbi.nlm.nih.gov/articles/PMC11556539/)

## Limitations
Small cohort (n = 15) restricted to bilateral mTLE with RNS. Modest correlation between FC and IEA phase. The authors call for larger prospective studies. — [Englot commentary](https://pmc.ncbi.nlm.nih.gov/articles/PMC11556539/); [abstract](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22Hippocampal%20network%20activity%20forecasts%20epileptic%20seizures%22&resultType=core&format=json)

## Relevance to our project
- This is the strongest evidence that a **short snapshot of background activity** carries information about slow seizure-risk state. That is conceptually what we want to do with TUSZ segments.
- It uses **intracranial hippocampal** electrodes. Scalp EEG has poor access to mesial temporal sources, so transfer to TUSZ is uncertain. Scalp phase-based FC (for example, wPLI or PLV in delta, theta and alpha bands between temporal electrodes) is a reasonable proxy to test, and it must be computed with volume-conduction-robust measures.
- The 24-h horizon is much longer than what TUSZ can label. On TUSZ we can only test whether FC differs between clips far from and near to seizures.
