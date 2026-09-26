# Seizure Detection in Brain Implants, BCIs and Closed-Loop Neurostimulation: Latency, Power and Accuracy Requirements

Scope note: Research ran on 2026-09-25 with about 20 tool calls. Items marked [FOUNDATIONAL] are from before 2023. Some numbers come from search-result snippets and not from full-text reads. Those are flagged "(snippet)" and should be checked before anyone quotes them as precise.

## 1. NeuroPace RNS: detectors, latency, stimulation, power, outcomes, stored data

### Takeaway
RNS is the reference clinical closed-loop seizure device. It runs very simple, clinician-tuned, per-channel detectors (line-length, area and bandpass/"half-wave") on 4 ECoG channels, sampled so that nothing above 125 Hz is visible. It delivers short 100–200 ms, 200 Hz bursts. Its battery lasts more than 10 years only if therapies stay under a few thousand per day. Its 9-year outcome is a 75% median seizure reduction. Detection usually lands seconds after electrographic onset, not milliseconds. Growing evidence suggests much of the benefit is chronic neuromodulation and not acute abortion of seizures.

### Cited Findings
- RNS continuously analyses 4 channels. For each, it compares a simple preselected feature (signal intensity/area, line-length or half-wave count) against a threshold. — [arXiv review 2109.05848](https://arxiv.org/pdf/2109.05848) (snippet)
- Detection tools are line-length, area and bandpass detectors. Example settings from a 2026 Neurotherapeutics programming review:
  - Line-length: a "66% change in the length of the EEG line over 2 s compared with a 2-min sliding window".
  - Area: a "≥88% increase in area ... over 2 s relative to a 2-min baseline".
  - Gamma bandpass detectors: 35.2–125 Hz, 0.26–0.38 s minimum duration.
  - "The sampling rate of the RNS device does not allow detection of activities >125 Hz."

  — [Responsive neurostimulation (RNS) programming, Neurotherapeutics 2026 (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13285825/)
- Stimulation: 200 Hz is the most common frequency (125–142.5 Hz for thalamic targets). Cortical bursts are short (100–200 ms); thalamic bursts are 5 s. Charge density starts at 0.5 µC/cm², rises in 0.5–1.0 µC/cm² steps every 3 months, and must stay below 25 µC/cm². A low-frequency alternative (5 s at 5 Hz, then 5 s at 2 Hz) is also described. — [same](https://pmc.ncbi.nlm.nih.gov/articles/PMC13285825/)
- Power budget in practice:
  - "Battery life for RNS model 320 with short burst (100–200 ms), high frequency stimulation is over a decade."
  - "When daily therapies exceed 6000 ... battery life is at risk." Over-detection therefore costs battery directly.

  — [same](https://pmc.ncbi.nlm.nih.gov/articles/PMC13285825/)
- Stored data:
  - "Long Episodes" (sustained detection, often 30 s; 25–40+ s in the programming review).
  - Saturation events.
  - Daily trending counts of "All Events" and "Long Episodes".
  - The first detector is often tuned to catch the seizure *body* so that onset falls inside the Long Episode ECoG storage window.

  — [RNS programming review](https://pmc.ncbi.nlm.nih.gov/articles/PMC13285825/); [search summary of same review](https://www.sciencedirect.com/science/article/pii/S1878747926001145)
- 9-year prospective outcomes (230 patients, 34 centres) [FOUNDATIONAL, 2020]:
  - Median seizure reduction of 75%.
  - 73% of patients had a ≥50% reduction.
  - About 33% had a ≥90% reduction.
  - About 1 in 5 were seizure-free in the prior 3 months.
  - QOL and cognition improved.

  — [Nayak/Nair et al., Neurology 2020, PubMed 32690786](https://pubmed.ncbi.nlm.nih.gov/32690786/); [NeurologyLive](https://www.neurologylive.com/view/neuropace-rns-system-shows-improvements-over-9-year-period); [NeuroPace press release](https://neuropace.com/press-release/neuropace-announces-final-results-largest-prospective-clinical-study/)
- Timing and mechanism:
  - "Stimulation in super-responders was concentrated in the rising phase from low to high seizure risk" (multiday cycles), with the opposite pattern in low responders.
  - A2 gamma detections in the seizure onset zone peak in the days *before* seizures.
  - Two recent lines of evidence challenge the assumptions that leads must target the focus and that stimulation must be triggered by epileptiform activity. Chronic neuromodulation may explain why closed-loop and open-loop outcomes are similar.

  — [RNS programming review 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC13285825/); [Communications Medicine 2023, "Unearthing the mechanisms of RNS"](https://www.nature.com/articles/s43856-023-00401-x)
- Detection delay: one report found that an adaptive detection approach cut median detection delay from 12.3 s to 4.8 s in the 5 subjects with the longest delays (snippet; I could not confirm the primary paper). A deep net trained on RNS ECoG (Peterson et al., Epilepsia 2023) predicted electrographic onset time to within about 3.4 s. — [Peterson et al., Epilepsia 2023](https://onlinelibrary.wiley.com/doi/abs/10.1111/epi.17666) (snippet)
- RNS stimulation features such as frequency and charge are associated with seizure control. — [Kokkinos et al., JAMA Neurol 2019, PubMed 30985902](https://pubmed.ncbi.nlm.nih.gov/30985902/) [FOUNDATIONAL] (title only)

### Inferences
- A useful implant detector should be judged against RNS: about 4 channels, features computed over ~2 s windows with ~2 min baselines, per-patient thresholds, and false positives that cost battery (the 6,000/day cap). A student's early detector should report false detections per hour or day next to latency.
- RNS itself is tuned for **high sensitivity with many "detections" per day**. The clinical cost of a false positive (a 100–200 ms burst) is small, but the energy cost is real. This is a different operating point from scalp-EEG alarm systems, where false alarms go to clinicians.

### Gaps
- I found no official NeuroPace figure for the end-to-end latency from detection to stimulation onset. Engineering sources describe it as effectively immediate after the detector fires, but I have no citable number.
- I did not retrieve the RNS pivotal trial numbers (Morrell 2011) from a primary source.

## 2. Other devices: Medtronic Percept/ANT DBS, Epiminder, UNEEG, NeuroVista, Seer/forecasting, Empatica, Ceribell

### Takeaway
Most implanted epilepsy devices on the market in 2025–2026 do **monitoring or open-loop stimulation**, not closed-loop seizure abortion. The first FDA-approved adaptive DBS (Medtronic, Feb 2025) is for Parkinson's. The sub-scalp EEG monitors (Epiminder Minder, De Novo; UNEEG EpiSight/SubQ, 510(k) June 2026) record and store data for seizure counting and forecasting. Wearables (EmbracePlus/EpiMonitor) and rapid-EEG AI (Ceribell Clarity) show the accuracy and false-alarm bar the FDA accepts.

### Cited Findings
- **Medtronic Percept / BrainSense**:
  - The FDA approved BrainSense Adaptive DBS (aDBS) and Electrode Identifier in Feb 2025. It is the world's first adaptive DBS and is indicated for **Parkinson's disease**; it uses LFPs to adjust stimulation.
  - Percept PC can record LFPs from the stimulation lead. It is being studied for anterior thalamic (ANT) stimulation in epilepsy.

  — [Medtronic news 2025-02-24](https://news.medtronic.com/2025-02-24-Medtronic-earns-U-S-FDA-approval-for-the-worlds-first-Adaptive-deep-brain-stimulation-system-for-people-with-Parkinsons); [Percept BrainSense thalamic epilepsy recordings (PMC11299490)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11299490/)
- **Epiminder Minder**:
  - FDA De Novo authorisation. It is the first implantable, long-term continuous EEG monitor authorised in the US.
  - Sub-scalp electrodes continuously acquire, transmit and store EEG.
  - In the UMPIRE trial, clinically relevant findings were seen in 88% of drug-resistant patients, including frequent unreported seizures. One participant was recorded continuously for 5 years.
  - US launch was planned for H2 2025.

  — [Epiminder FDA news](https://epiminder.com/news/fda-authorisation); [FDA De Novo DEN240062 review](https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN240062.pdf); [NeurologyLive](https://www.neurologylive.com/view/fda-grants-authorization-epiminder-implantable-continuous-eeg-monitor-epilepsy-treatment); [UMPIRE publication news](https://epiminder.com/news/umpire-clinical-trial-publication)
- **UNEEG SubQ / EpiSight**:
  - A subcutaneous EEG device behind the ear. FDA 510(k) clearance for the EpiSight system was announced June 2026.
  - EU approval for 3-year continuous use came in June 2025.
  - It is MR-conditional at 1.5 T and 3 T.

  — [GS MedTech news](https://news.gsmedtech.com/uneeg-medical-fda-510k-clearance-for-uneeg-episight-system/); [Neurofounders](https://www.neurofounders.co/articles/uneeg-wins-fda-clearance-for-subcutaneous-eeg-monitoring); [UNEEG](https://www.uneeg.com/)
- **NeuroVista Seizure Advisory System (Cook et al., Lancet Neurol 2013)** [FOUNDATIONAL]:
  - 15 patients were implanted for 6 months to 3 years. The algorithm met enabling criteria in 11.
  - High-likelihood warning sensitivity ranged from 65% to 100%. The best patient reached 100% sensitivity with 3% time-in-warning; the worst reached 17% sensitivity with 41% time-in-warning.
  - Three patients' algorithms failed criteria; one device was explanted after an adverse event.

  — [PubMed 23642342](https://pubmed.ncbi.nlm.nih.gov/23642342/); [Lancet Neurol abstract](https://www.thelancet.com/journals/laneur/article/PIIS1474-4422(13)70075-9/abstract)
- The NeuroVista data seeded the Epilepsyecosystem.org crowd-sourced prediction contest. — [Kuhlmann et al., Brain 2018](https://academic.oup.com/brain/article/141/9/2619/5066003) [FOUNDATIONAL]
- **Empatica EmbracePlus / EpiMonitor** (FDA 510(k) K232915, K242737, K250515):
  - The EpiMonitor algorithm reports 98% accuracy.
  - False alarm rate is 0.05/day for children and 0.02/day for adults at rest.
  - It has "high" and "low" sensitivity modes for rest and low activity. It detects generalized tonic-clonic seizures, not focal seizures.

  — [Empatica EpiMonitor how it works](https://www.empatica.com/epimonitor/how-it-works/); [FDA K232915](https://www.accessdata.fda.gov/cdrh_docs/pdf23/K232915.pdf); [FDA K250515](https://www.accessdata.fda.gov/cdrh_docs/pdf25/K250515.pdf)
- **Ceribell Clarity** (rapid-response EEG AI):
  - 94% sensitivity and 95% specificity for ≥90% seizure burden, with 99% NPV.
  - 95% sensitivity and 97% specificity for status epilepticus.
  - 510(k) clearance for neonates in Nov 2025.

  — [Ceribell Clarity](https://ceribell.com/product/clarity/); [Ceribell neonate 510(k) PR](https://ceribell.gcs-web.com/news-releases/news-release-details/ceribell-receives-fda-510k-clearance-use-clarity-algorithm); [FDA K191301](https://www.accessdata.fda.gov/cdrh_docs/pdf19/K191301.pdf)

### Inferences
- The real deployment targets for a scalp or TUSZ-type detector are the minimal-channel sub-scalp devices (Minder, SubQ) and ICU rapid EEG (Ceribell). The regulatory bar there is about ≥90–95% sensitivity with false alarms around ≤1 per day, far lower than what most TUSZ papers report per 24 h.

### Gaps
- I did not retrieve SANTE (ANT DBS) trial numbers or the status of ANT sensing-based closed-loop epilepsy trials. I also found no Seer Medical-specific regulatory or performance data.

## 3. Neuralink, Paradromics, Synchron, Precision: epilepsy relevance and on-chip compute limits

### Takeaway
None of the high-channel BCI companies has a stated closed-loop epilepsy therapy product. Paradromics' first-in-human recording took place during an epilepsy resection. Neuralink's published figures (2019) give about 5.2 µW per analog channel, about 6 mW per ASIC and 550–750 mW for the whole system. The on-implant budget for any extra seizure model is therefore in the µW to low-mW range, which fits tiny models (roughly thousands to tens of thousands of parameters, or fixed-point features plus a linear/tree classifier), not large transformers.

### Cited Findings
- Neuralink 2019 white paper (rodent system):
  - Each analog pixel uses 5.2 µW; the whole ASIC uses about 6 mW including clock drivers.
  - System A (1,536 channels) drew 550 mW in total; System B (3,072 channels) drew 750 mW.
  - On-chip spike detection is used for compression. The white paper does not mention epilepsy.

  — [Musk & Neuralink, JMIR 2019 (PMC6914248)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6914248/) [FOUNDATIONAL]
- Secondary blogs claim the N1 has 1,024 channels, uses "6.6 µW" and does on-chip spike detection with more than 200× compression in about 900 ns. These are unverified, non-primary claims and conflict in units with the white paper; treat them as unreliable. — [Medium (Haji)](https://mikaelhaji.medium.com/a-technical-deep-dive-on-elon-musks-neuralink-in-40-mins-71e1100f54d4)
- Paradromics Connexus: the first-in-human procedure (June 2025, University of Michigan) placed the device temporarily during an epilepsy resection surgery. It was implanted, recorded and removed intact in under 20 minutes. The stated target application is communication restoration. — [Michigan Medicine](https://www.michiganmedicine.org/news-release/university-michigan-implants-first-human-paradromics-wireless-brain-computer-interface-designed); [MassDevice](https://www.massdevice.com/paradromics-reports-first-in-human-connexus-bci-procedure/)
- Paradromics notes that ECoG has a long clinical history in epilepsy monitoring and mapping. — [Paradromics blog](https://paradromics.com/blog/electrocorticography/)
- A 68-channel neural PSoC in 22 nm FDSOI with on-chip feature extraction and accelerators shows the current direction for implant-grade compute. — [arXiv 2407.09166](https://arxiv.org/pdf/2407.09166)

### Inferences
- Thermal limits (the tissue-heating limit of about 1 °C, commonly cited as roughly 40 mW/cm²; not sourced here) and battery or inductive power push implant seizure detection toward models of about 1–100 µW per channel.

### Gaps
- I found no official Neuralink, Synchron or Precision statement of an epilepsy application or plan. I found no primary current (2024–2026) N1 power figure.

## 4. How early must detection be? Closed-loop latencies and stimulation timing

### Takeaway
Two timescales matter:
- **Acute abortion:** stimulation needs to arrive near electrographic onset, before the seizure spreads. Chip literature targets sub-second to about 1 s latency, while clinical RNS detections land a few seconds to more than 10 s after onset.
- **Chronic neuromodulation:** timing relative to *multiday risk cycles* may matter more than per-seizure latency.

Direct clinical evidence that earlier detection gives better RNS outcomes is sparse.

### Cited Findings
- A closed-loop neuromodulation chipset reports 0.76 s seizure detection latency, 97.8% sensitivity and 0.5 ms stimulation artifact rejection. — [search summary of JSSC SoC literature](https://www.researchgate.net/publication/261045332_A_Fully_Integrated_8-Channel_Closed-Loop_Neural-Prosthetic_CMOS_SoC_for_Real-Time_Epileptic_Seizure_Control) (snippet; the exact chip should be checked)
- RNS onset detection errors or delays are about 3–12 s (see Section 1). — [Peterson et al., Epilepsia 2023](https://onlinelibrary.wiley.com/doi/abs/10.1111/epi.17666) (snippet)
- RNS programming explicitly targets "pro-ictal, pre-ictal, ictal onset, and seizure body biomarkers" for the best stimulation timing. Stimulation concentrated in the rising phase of multiday risk is linked with super-response. — [RNS programming review 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC13285825/)
- The chronic-neuromodulation hypothesis (open-loop and closed-loop outcomes are similar) weakens a strict need for millisecond latency. — [Communications Medicine 2023](https://www.nature.com/articles/s43856-023-00401-x)

### Inferences
- For a TUSZ project, a reasonable target is: detection within about 1–5 s of annotated onset, well ahead of clinical onset, with false detections of a few per hour or fewer. Scalp EEG lags iEEG onset, so scalp latency is a pessimistic proxy.

### Gaps
- I found no recent randomized comparison of early versus late stimulation in humans.

## 5. Forecasting vs prediction vs detection; useful warning times

### Takeaway
- **Detection** finds a seizure that is happening; the useful horizon is seconds.
- **Prediction** gives a deterministic warning minutes before a seizure (for example NeuroVista).
- **Forecasting** gives a probabilistic risk over hours to days, driven by multiday (multidien) cycles.

Patients prefer short warnings but also value knowing when they are in a risky period, and they rank sensitivity above specificity.

### Cited Findings
- Hippocampal functional connectivity from 90-s recordings forecast 24-h seizure likelihood as well as cycle models that need months of data. This was a retrospective study of 15 adults with bitemporal RNS. — [Nature Medicine 2024](https://www.nature.com/articles/s41591-024-03149-6)
- Multiday cycles appear in diverse physiological signals (wearables, heart rate) and are linked to seizures. — [Karoly et al. 2023 (PMC10733995)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10733995/); [Baud/Rao, Nat Rev Neurol 2021 "Cycles in epilepsy"](https://www.nature.com/articles/s41582-021-00464-1) [FOUNDATIONAL]
- Prospective real-world validation and regulatory approval of patient-facing forecasting remain rare as of 2025–2026. — [Karoly et al., Epilepsia "Seizure forecasting: the long and winding road to clinical translation"](https://onlinelibrary.wiley.com/doi/full/10.1002/epi.70394); [Forecasting cycles of seizure likelihood, Epilepsia 2020](https://onlinelibrary.wiley.com/doi/abs/10.1111/epi.16485); [medRxiv 2025, tracking cycles vs moving average](https://www.medrxiv.org/content/10.1101/2025.11.03.25338700v1)
- Patient surveys (Freiburg and Coimbra) show short prediction windows are preferred, but seizure-prone periods are also valued. Sensitivity matters more than specificity. Few patients are willing to wear EEG electrodes long term. — [Schulze-Bonhage et al., Epilepsy Behav 2010 (PubMed 20624689)](https://pubmed.ncbi.nlm.nih.gov/20624689) [FOUNDATIONAL]
- Wearable preferences study. — [Neurology 2022](https://www.neurology.org/doi/10.1212/WNL.0000000000200794)

### Gaps
- I did not retrieve exact preferred warning durations in minutes from the survey full texts.

## 6. Scalp-to-intracranial transfer and TUSZ relevance

### Takeaway
Direct TUSZ-to-iEEG transfer studies are scarce. The closest work is simultaneous scalp and intracranial deep learning (Mayo/MTLE), plus emerging foundation models that align scalp EEG and iEEG. TUSZ is mainly useful for developing algorithms with low latency and low false alarms, for pretraining, and for sub-scalp or few-channel devices. It is not a stand-in for implant ECoG.

### Cited Findings
- Deep learning on simultaneous iEEG and scalp EEG was used for prediction, detection and lateralization of mesial temporal seizures, comparing iEEG only, scalp only and joint models. — [PMC8632629](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8632629/) [FOUNDATIONAL, 2021]
- Cross-modal harmonization pretrains a unified transformer across scalp EEG and iEEG. — [arXiv 2506.17068](https://arxiv.org/pdf/2506.17068)
- Low-latency real-time seizure detection with transfer deep learning. — [ResearchGate](https://www.researchgate.net/publication/358655398_Low_Latency_Real-Time_Seizure_Detection_Using_Transfer_Deep_Learning)
- TUSZ v2.0.1 has 675 patients, more than 280 with seizures, and more than 3,500 seizures. — [search snippet (DistilCLIP-EEG)](https://arxiv.org/pdf/2510.13497)

### Gaps
- I found no study that pretrains on TUSZ and fine-tunes on RNS or iEEG with reported gains.

## 7. On-chip seizure detection ASICs and neuromorphic chips

### Takeaway
Seizure detection ASICs run at tens to hundreds of µW, with latency under about 1 s and sensitivity of about 93–98%. This sets a practical model-size ceiling for implant-compatible early detectors.

### Cited Findings
- The Xylo SNN neuromorphic processor draws 87.4 µW (IO) plus 287.9 µW (compute), which is below 1 mW. It reaches 93.3% ictal and 92.9% interictal classification accuracy. — [arXiv 2410.16613](https://arxiv.org/abs/2410.16613)
- NeuralTree: a 256-channel SoC using 0.227 µJ per classification for closed-loop neuromodulation. — [arXiv 2205.06090](https://arxiv.org/pdf/2205.06090)
- JSSC closed-loop SoC lineage:
  - 16-channel onset and termination detection with a transcranial stimulator (2015).
  - Patient-specific one-shot learning (2022).
  - A chipset with 97.8% sensitivity and 0.76 s latency.

  — [search summary](https://arxiv.org/pdf/2109.05848)
- Memristive CNN seizure detection. — [arXiv 2206.09951](https://arxiv.org/pdf/2206.09951)

### Gaps
- I did not verify the exact µW per channel for each JSSC chip.
