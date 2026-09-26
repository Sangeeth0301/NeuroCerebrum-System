# Neuroscience of the Preictal State: Mechanisms to Measurable EEG Biomarkers

Legend used throughout: **[Evidence: strong / moderate / weak / contested]**; **[Time: seconds / minutes / hours / days]**; **[Scale: scalp / iEEG-only / microelectrode-only / animal/slice-only]**. "Foundational" = pre-2018 work. A few foundational URLs are from memory rather than fetched in this session; those are marked "(URL not re-verified this session)".

---

## 1. Cellular/synaptic mechanisms of ictogenesis (E/I, interneurons, K+, Cl-/KCC2, recruitment)

### Takeaway
At the micro-scale the final seconds-to-minutes before focal onset are dominated by an *interneuron-driven* sequence: fast-spiking (PV) interneurons fire intensely, extracellular K+ accumulates, interneurons enter depolarization block, and pyramidal cells are released (disinhibition) within ~1 s; neuronal recruitment is spatially restrained by an "inhibitory veto" ahead of an ictal wavefront. Almost none of this is directly visible on scalp EEG. What reaches the scalp is only the downstream population consequence (changes in variance/autocorrelation, spectral slope, spike rate, rhythmic build-up) once ~10+ cm^2 of cortex becomes synchronized.

### Cited Findings
**Interneurons and depolarization block (seconds before onset; slice/animal)**
- 4-AP slice model, simultaneous whole-cell recordings: during the preictal phase interneurons fire at high frequency and then enter depolarization block. Block onset coincides with the peak rate of extracellular K+ accumulation. Pyramidal cells stay mostly silent during the interneuron hyperactivity and start firing 1.1 ± 0.3 s after block onset. The sequence appeared in 100% of recordings. Authors conclude that disinhibition, not excitatory GABA, gates the transition (2025, IJMS). [Evidence: moderate, single model; Time: seconds; Scale: slice-only] — [PMC12295800](https://pmc.ncbi.nlm.nih.gov/articles/PMC12295800/)
- Miri, Vinck, Pant & Cardin 2018 (eLife), mouse CA1 with PTZ/pilocarpine and optotagged tetrodes: PV cells show a sharp late firing increase just before seizure onset (minutes). SST cells show sustained elevation without that late surge. Synaptic inhibition stays intact through the preictal period. PV firing becomes more regular and loses 20–28 Hz spike-field coherence. SST cells become progressively less responsive to input. Interpretation: onset reflects disrupted temporal coordination of inhibition rather than outright failure of GABA release. [Evidence: moderate; Time: minutes; Scale: animal microelectrode-only] — [eLife 40750](https://elifesciences.org/articles/40750)
- Review: GABAergic circuits can *drive* focal seizures, i.e. the "inhibition paradox" — [Neurobiol Dis review](https://www.sciencedirect.com/science/article/pii/S096999612300116X)

**Chloride / KCC2 / potassium (seconds–minutes; slice)**
- KCC2 extrudes Cl- to restore E_GABA, but it co-transports K+, so it raises extracellular K+, which can depolarize neurons and potentiate seizures. Both pro- and anticonvulsant effects of KCC2 inhibition have been reported. [Evidence: contested/paradoxical] — [Nat Commun 2019, KCC2 overexpression](https://www.nature.com/articles/s41467-019-08933-4); [eNeuro 2021, KCC2 in ictal termination](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7986536/)
- Human TLE neocortical slices: KCC2 activity dampens the occurrence and propagation of induced ictal-like activity in supragranular neocortex — [PMC12893269](https://pmc.ncbi.nlm.nih.gov/articles/PMC12893269/)
- Model of reduced KCC2 efficacy promoting epileptic oscillations in subiculum (J Neurosci 2016, foundational) — [J Neurosci 36/46/11619](https://www.jneurosci.org/content/36/46/11619)
- Review: KCC2 as a drug target — [Acta Pharmacol Sin 2023](https://www.nature.com/articles/s41401-023-01149-9)

**Neuronal recruitment and inhibitory restraint (seconds; human microelectrodes; foundational)**
- Truccolo et al. 2011 (Nat Neurosci, Utah arrays in human neocortex): single-unit spiking during seizure initiation and spread is highly *heterogeneous*, not hypersynchronous. It becomes more homogeneous toward termination. [Foundational; Scale: microelectrode-only] — [Nat Neurosci nn.2782](https://www.nature.com/articles/nn.2782); commentary [nn.2811](https://www.nature.com/articles/nn.2811)
- Schevon et al. 2012 (Nat Commun): a sharp boundary separates the recruited "ictal core" (hypersynchronous firing) from the "ictal penumbra" (low-level, unstructured firing). Penumbral field potentials are time-locked to the core but consist of mixed excitatory and inhibitory input, i.e. an inhibitory veto restrains pyramidal firing. Macroscale EEG cannot distinguish core from penumbra. [Foundational] — [Nat Commun ncomms2056](https://www.nature.com/articles/ncomms2056)
- Feedforward inhibition ahead of ictal wavefronts comes from both PV and SST interneurons (Parrish et al. 2019, J Physiol) — [JP277749](https://physoc.onlinelibrary.wiley.com/doi/10.1113/JP277749); inhibitory control modulates focal seizure spread (Brain 2018) — [Brain 141/7/2083](https://academic.oup.com/brain/article/141/7/2083/4994808)
- Trevelyan et al. 2006 (J Neurosci), "inhibitory veto" in slices [Foundational] — [J Neurosci 26/48/12447](https://www.jneurosci.org/content/26/48/12447) (URL not re-verified this session)

**Synaptic perturbations and resilience (minutes–hours; animal)**
- Chang et al. 2018 (Nat Neurosci): the transition to seizure is not sudden. It is a slow, progressive loss of network resilience governed by critical slowing. Whether an interictal synaptic perturbation (an IED) triggers a seizure depends on the current resilience state. This links a synaptic event (IED = synchronous synaptic input) to a measurable dynamical biomarker (slower recovery after perturbations). [Evidence: strong mechanistic, animal/LFP] — [Nat Neurosci s41593-018-0278-y](https://www.nature.com/articles/s41593-018-0278-y); [author manuscript](https://www.open-access.bcu.ac.uk/6526/2/Chang_NN_Manuscript.pdf); commentary [Ahmed & John 2019](https://doi.org/10.1177/1535759719835349)

### Inferences
- The mechanisms act on a seconds timescale (depolarization block, K+ surge) and at sub-millimetre scale. They set the *trigger*. The minutes-to-days "preictal/pro-ictal" state is better understood as a slowly varying *susceptibility* (resilience, E/I set-point) that EEG can index only indirectly.
- Scalp-feasible proxies of these mechanisms: (a) recovery rate / autocorrelation after spontaneous IEDs, a direct analog of Chang 2018's perturbation-recovery that could be computed on TUSZ at spike-triggered epochs; (b) aperiodic slope (Section 3); (c) spike rate.
- Interneuron hyperactivity before onset could appear as a relative *increase in inhibitory signatures* just before onset. This fits the scalp aperiodic-exponent increase reported by Duma et al. 2025 (Section 3), but that link is speculative.

### Gaps
- No human in-vivo measurement of preictal extracellular K+ or Cl- dynamics at minutes-to-hours scale was found.
- The details of Chang 2018 (species and preparations, exact recovery metric) were not extracted because the PDF was unreadable here. The report writer should state only the abstract-level claims above.
- No direct evidence that PV depolarization block produces a specific scalp-EEG signature.

---

## 2. Network / dynamical-systems biomarkers (critical slowing, bifurcations, synchrony, complexity)

### Takeaway
Critical slowing down (CSD: rising variance and lag autocorrelation, slower recovery) is the best-supported dynamical biomarker. In long-term human iEEG it tracks circadian and multiday *susceptibility* cycles, and in 9/14 patients it rises over tens of minutes to hours before lead seizures. However, whether CSD appears depends on the bifurcation route, and some 2025 work argues it marks a "pro-ictal" state rather than an imminent seizure. Classic synchrony findings (a preictal *drop* in synchronization, then hypersynchrony at onset) come from pre-2010 iEEG and were never robustly validated for prediction.

### Cited Findings
**Critical slowing down**
- Maturana et al. 2020 (Nat Commun). NeuroVista iEEG, 14 patients, 2,871 seizures, 7,246 recording days (233–767 days per patient). Features: autocorrelation width at half maximum and variance, from 1-s snapshots every 2 min. Findings:
  - Both features cycle with circadian (~0.64 ± 0.16 d) and multidien (10.5 ± 4.1 d) periods, and seizures occur preferentially on the rising phase.
  - "A gradual increase … in the tens-of-minutes to hours prior to lead seizures in most patients (9 of 14)".
  - Pseudoprospective forecast (autocorrelation + variance + spike rate): sensitivity 77 ± 8% with 8 ± 6% time in high risk. The chance predictor reached ~9% sensitivity, and the random-predictor comparison used a Markov model.
  - Combining CSD with spikes beat spike rate alone. Autocorrelation was the most informative feature.
  - Caveat from the paper itself: CSD is expected only when the system is driven slowly toward a bifurcation, not in perturbation-driven transitions. One patient showed no CSD.
  - [Evidence: strong for cycles and moderate for short-term preictal rise; Time: tens of min–days; Scale: iEEG (subdural, long-term)] — [PMC7195436](https://pmc.ncbi.nlm.nih.gov/articles/PMC7195436/); [Nat Commun](https://www.nature.com/articles/s41467-020-15908-3); code: [GitHub](https://github.com/tempo-beme/Critical_Slowing_Epilepsy)
- 2025 Clin Neurophysiol paper, "Pro-ictal, rather than pre-ictal, brain state marked by global critical slowing and local gamma power increase". The title claims CSD marks a *pro-ictal* (elevated-risk) state rather than a specific imminent pre-seizure state. Full text was not accessible (403). [Evidence: contested interpretation] — [ScienceDirect S1388245725005942](https://www.sciencedirect.com/science/article/pii/S1388245725005942)
- Active probing as an alternative to passive CSD: seizure forecasting by tracking the cortical response to electrical stimulation (a direct measure of resilience) — [PMC12611449](https://pmc.ncbi.nlm.nih.gov/articles/PMC12611449/)

**Bifurcation types (determine which precursors can exist)**
- Saggio et al. 2020 (eLife) taxonomy. There are 4 onset × 4 offset bifurcations, giving 16 "dynamotypes", and all 16 were found in >2,000 focal seizures from multiple centers. One onset type and one offset type require a DC shift to identify. Patients can show multiple dynamotypes. This builds on the Epileptor (Jirsa et al. 2014, Brain, foundational: a slow permittivity variable drives the system through onset and offset bifurcations) — [eLife 55632](https://elifesciences.org/articles/55632); Jirsa 2014 [Brain 137/8/2210](https://academic.oup.com/brain/article/137/8/2210/2847958) (URL not re-verified this session)
- Guendelman, Vekslar & Shriki 2025 applied the taxonomy to **scalp** EEG (EPILEPSIAE, 158 patients, 1,177 seizures):
  - Only ~49.5% of seizures had an identifiable onset bifurcation and 40.3% an identifiable offset.
  - With no DC on scalp, SN/SubH at onset and SH/SNIC at offset had to be merged.
  - Detection was better for occipital and worse for frontal seizures.
  - SNIC and supercritical Hopf onsets were more frequent in wake than in NREM (especially N3).
  - [Evidence: moderate; Scale: scalp-feasible with caveats] — [PMC11747977](https://pmc.ncbi.nlm.nih.gov/articles/PMC11747977/)
- Related tools: DynamoSort ML classification — [PMC11870418](https://pmc.ncbi.nlm.nih.gov/articles/PMC11870418/); synthetic seizure toolbox (eNeuro 2025) — [ENEURO.0200-25.2025](https://www.eneuro.org/content/12/10/ENEURO.0200-25.2025)

**Synchronization and connectivity**
- Mormann et al. 2003 (Epilepsy Res, foundational), iEEG in 18 patients over 117 h: a significant preictal *drop* in phase synchronization before ~80% of seizures, sometimes hours ahead — [PubMed 12694925](https://pubmed.ncbi.nlm.nih.gov/12694925/); long-term follow-up: preictal synchronization state seen hours before 36/52 (70%) seizures, involving both increases and decreases, mostly at 4–15 Hz and near the epileptogenic zone — [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1388245704004626)
- Caveat: the 2007 Mormann Brain review concluded that evidence for prediction was insufficient once statistical controls were applied (summarized in [Kuhlmann et al. 2018](https://www.nature.com/articles/s41582-018-0055-2)). Hippocampal synchronization is not a preseizure indicator unless the onset-channel state is considered — [PMC5225267](https://pmc.ncbi.nlm.nih.gov/articles/PMC5225267/). [Evidence: contested]
- Khambhati, Chang, Baud & Rao 2024 (Nat Med), RNS in 15 bitemporal patients:
  - Hippocampal functional connectivity fluctuates in multiday cycles that mirror seizure-likelihood cycles.
  - A connectivity biomarker from **90-s** background snapshots generalized *across* individuals and forecast 24-h seizure likelihood as well as cycle models that need months of data.
  - [Evidence: strong for iEEG; Time: 24 h; Scale: iEEG-only (hippocampal)] — [Nat Med s41591-024-03149-6](https://www.nature.com/articles/s41591-024-03149-6); commentary [Englot 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11556539/)
- Functional networks show multiscale periodicities correlated with seizure onset — [PMC7268013](https://pmc.ncbi.nlm.nih.gov/articles/PMC7268013/)
- Volume conduction can create spurious phase synchronization from superimposed signals, which matters for scalp connectivity — [arXiv 1409.4251](https://arxiv.org/pdf/1409.4251)

**Entropy / complexity**
- Segal et al. 2025 (Front Neurosci), **scalp** EEG from 21 patients (54 seizures, 644 h). Method: Mahalanobis-distance outlier detection in a 10-D feature space. Results: a preictal state was detected in 89.5% of seizures, starting 83 ± 60 min before onset and lasting 56 ± 47 min. Spectral entropy and Hjorth mobility were consistently top features. Preictal changes often appeared *contralateral* to or away from the seizure-onset zone. Limitations: retrospective, small sample, no prospective test, first-of-cluster seizures only. [Evidence: weak–moderate; Scale: scalp] — [PMC12082717](https://pmc.ncbi.nlm.nih.gov/articles/PMC12082717/)

### Inferences
- For a TUSZ project: variance and lag-1 autocorrelation per channel, together with IED-triggered recovery time, are cheap and physically interpretable. Expect confounding by vigilance state, and expect TUSZ records (mostly short, often <24 h) to capture only the minutes-to-hours tail of CSD, not the multiday cycles.
- The bifurcation-type result predicts heterogeneity: CSD should be absent for perturbation- or noise-driven onsets. A student could stratify seizures by onset dynamotype and test whether CSD appears only for SN/SNIC-type onsets, a novel and testable hypothesis.
- Scalp connectivity estimates need volume-conduction-robust measures (imaginary coherence, wPLI) or source-space analysis.

### Gaps
- No rigorous scalp-EEG CSD forecasting study with surrogate testing was found. The CSD evidence is iEEG (Maturana) or animal (Chang).
- Access to the "pro-ictal vs pre-ictal" 2025 paper was blocked, so its cohort and statistics are unknown.

---

## 3. EEG spectral biomarkers (aperiodic 1/f exponent, band power, IED rate, HFOs, infraslow/DC)

### Takeaway
The aperiodic exponent is the most "mechanism-linked" scalp-accessible spectral marker (steeper slope is read as more inhibition). Surprisingly, the best preictal evidence shows it *increasing* (a shift toward inhibition) in the minutes to hours before seizures, on both scalp hd-EEG and intracranial recordings. The exponent is also strongly confounded by vigilance state and anti-seizure medications (ASMs). IED rate is a robust *cycle* marker, but it often *decreases* just before seizures. Scalp HFOs and DC shifts are technically possible but are unlikely to be usable in TUSZ-grade data.

### Cited Findings
**Aperiodic exponent**
- Duma et al. 2025 (BMC Medicine), 20 patients, 29 seizures, **128-channel scalp EEG** (512 Hz), time-resolved spectral parameterization (SPRiNT). Findings:
  - The aperiodic exponent rises progressively over the 13-min preictal window, i.e. a global shift toward inhibition.
  - The shift is widespread, with no epileptic vs non-epileptic region difference.
  - It correlates with cortical thickness (ρ = 0.21) and inversely with muscarinic receptor density (ρ = −0.43), tested with spin permutations.
  - Authors suggest a compensatory inhibition that fails at onset.
  - [Evidence: moderate, small n; Time: minutes; Scale: scalp hd-EEG] — [PMC12581463](https://pmc.ncbi.nlm.nih.gov/articles/PMC12581463/)
- Brain Stimulation 2025, "Aperiodic activity as a biomarker of seizures and neuromodulation" (RNS intracranial):
  - A pre-ictal rise in the aperiodic exponent over the 12 h before seizures, ipsilateral and contralateral to onset, visibly apparent in most participants.
  - Acute stimulation *decreased* the exponent, consistent with reversing a pro-ictal state.
  - Full text blocked (403); these points come from search-result abstracts. [Evidence: moderate; Time: hours; Scale: iEEG] — [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1935861X25000798)
- Charlebois et al. 2024 (Epilepsia): larger circadian changes in the aperiodic exponent and alpha power over the first 3 months of RNS correlate with better seizure reduction — [PMC11138949](https://pmc.ncbi.nlm.nih.gov/articles/PMC11138949/)
- Theory and method: Gao, Peterson & Voytek 2017 (NeuroImage) link the spectral exponent to the E/I ratio (foundational; model plus propofol and rat data) — [doi 10.1016/j.neuroimage.2017.06.078](https://doi.org/10.1016/j.neuroimage.2017.06.078); FOOOF/specparam, Donoghue et al. 2020 Nat Neurosci — [s41593-020-00744-x](https://www.nature.com/articles/s41593-020-00744-x) (both URLs not re-verified this session)
- Confounds:
  - The exponent varies with vigilance state in mice and humans — [PMC11315276](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11315276/)
  - ASMs alter aperiodic activity (bioRxiv 2025) — [biorxiv 2025.11.02.686141](https://www.biorxiv.org/content/10.1101/2025.11.02.686141.full.pdf)
  - Pharmacological manipulations shift periodic and aperiodic components — [biorxiv 2023.09.21.558828](https://www.biorxiv.org/content/10.1101/2023.09.21.558828.full.pdf)
  - Aperiodic fits are distorted by pathological waveform shapes such as spikes in focal epilepsy — [PubMed 41213802](https://pubmed.ncbi.nlm.nih.gov/41213802/). This matters because IEDs can masquerade as E/I shifts. [Evidence: contested interpretation of exponent = E/I]

**Interictal epileptiform discharge (IED/spike) rate**
- Karoly et al. 2016 (Brain, foundational; NeuroVista): spikes and seizures share circadian and longer rhythms. Spike rate *decreases* before seizures, which is inconsistent with spikes simply triggering seizures (possibly protective, or a symptom of the approach to seizure) — [Brain 139/4/1066](https://academic.oup.com/brain/article-abstract/139/4/1066/2464379)
- Baud et al. 2018 (Nat Commun), RNS in 37 subjects over years: IED rate oscillates with circadian and multidien periods (most often 20–30 days), stable for up to 10 years. Seizures cluster on the *rising phase* of multidien IED cycles, and combining circadian and multidien phase gave large effect sizes. [Evidence: strong; Time: days–weeks; Scale: iEEG] — [s41467-017-02577-y](https://www.nature.com/articles/s41467-017-02577-y)
- Chang 2018: IEDs are synaptic perturbations whose ictogenic effect depends on the resilience state (Section 1) — [link](https://www.nature.com/articles/s41593-018-0278-y)

**HFOs (80–500 Hz)**
- Scalp HFOs (mostly ripples, 80–250 Hz) are detectable in adults and children. Evidence mainly concerns disease activity, epileptogenicity after a first seizure, and treatment response, not minute-scale prediction. Scalp HFOs are less sensitive but more specific than spikes for outcome prediction. [Scale: scalp possible, needs high sampling rate and low noise] — [systematic review, Clin Neurophysiol 2022](https://www.sciencedirect.com/science/article/pii/S1388245722000153); [Klotz 2021 Ann Neurol](https://onlinelibrary.wiley.com/doi/10.1002/ana.25939); [Sci Rep 2019, scalp HFOs track seizure frequency](https://www.nature.com/articles/s41598-019-52700-w)

**Infraslow / DC shifts**
- iEEG: coupling between infraslow activity and HFOs surges a few minutes (~10 min) before seizure onset — [PMC7469835](https://pmc.ncbi.nlm.nih.gov/articles/PMC7469835/)
- Scalp: ictal DC shifts can be shown on scalp EEG only with a long time constant (≥2 s), a proof-of-principle abstract — [Neurology 2023 abstract](https://www.neurology.org/doi/10.1212/WNL.0000000000205645)
- Review of ictal baseline shifts and infraslow activity — [J Clin Neurophysiol](https://www.ovid.com/jnls/clinicalneurophys/fulltext/10.1097/wnp.0b013e31826242b3~ictal-onset-baseline-shifts-and-infraslow-activity)
- Most of these shifts are *ictal-onset* markers, not preictal ones. [Evidence: weak for prediction]

### Inferences
- In TUSZ (AC-coupled clinical EEG, typically 250–256 Hz sampling) HFOs above ~100 Hz and DC shifts are essentially unmeasurable. Aperiodic exponent, band power and IED rate are feasible.
- The *direction* of the preictal aperiodic change (steepening) contradicts the naive "seizure = more excitation" reading. A student project could test whether it survives controls for sleep stage, IED removal and time of day, and whether it is focal or global on the standard 10–20 montage.

### Gaps
- No preictal aperiodic-exponent study on TUSZ specifically was found.
- The cohort sizes of the Brain Stimulation 2025 study could not be retrieved.

---

## 4. Multiday/circadian cycles of seizure risk and EEG estimation

### Takeaway
Seizure risk is modulated by circadian and multidien (often ~weeklong to 20–30 day) cycles, visible in IED rate, CSD metrics, connectivity, and even heart rate. Cycle phase gives day-scale forecasts that beat chance. Estimating multidien phase needs weeks of data, so it is impractical from short TUSZ-style routine or EMU scalp records, although circadian phase (time of day, sleep stage) is available.

### Cited Findings
- Baud et al. 2018: see Section 3. IED multidien cycles of 20–30 days; seizures occur on the rising phase — [Nat Commun](https://www.nature.com/articles/s41467-017-02577-y); commentary [Menendez de la Prida 2018](https://doi.org/10.5698/1535-7597.18.3.194)
- Proix et al. 2021 (Lancet Neurol 20:127–135): forecasting models built on RNS hourly IED counts and cyclical features predicted seizure risk at 1-day and 3-day horizons, scored with Brier skill score and AUC against rate-matched chance. Exact numbers were not extracted here. [Evidence: strong; Scale: iEEG] — [Lancet Neurol abstract](https://www.thelancet.com/journals/laneur/article/PIIS1474-4422(20)30396-3/abstract); [eScholarship PDF](https://escholarship.org/content/qt4x778199/qt4x778199.pdf?t=s8w30i); comment [Lancet Neurol](https://www.thelancet.com/journals/laneur/article/PIIS1474-4422(20)30414-2/abstract)
- Maturana 2020: CSD metrics show circadian and ~10-day cycles phase-locked to seizures — [PMC7195436](https://pmc.ncbi.nlm.nih.gov/articles/PMC7195436/)
- Khambhati 2024: 90-s hippocampal connectivity snapshots index multiday cycle state — [Nat Med](https://www.nature.com/articles/s41591-024-03149-6)
- Karoly et al.: circadian and circaseptan rhythms (Lancet Neurol 2018); forecasting from self-reported cycles (Epilepsia 2020, 50 app users, pseudoprospective); multiday heart-rate cycles associated with seizure likelihood (eBioMedicine 2021); review "Seizure forecasting: the long and winding road to clinical translation" (Epilepsia 2025/26) — [Epilepsia 2020](https://onlinelibrary.wiley.com/doi/abs/10.1111/epi.16485); [eBioMedicine 2021](https://www.thelancet.com/journals/ebiom/article/PIIS2352-3964(21)00412-6/fulltext); [Epilepsia review](https://onlinelibrary.wiley.com/doi/abs/10.1002/epi.70394)
  - Note: the requester's "Karoly 2021 Lancet Neurol" appears to conflate these. The Lancet Neurol 2021 forecasting paper is **Proix et al.**, and Karoly's Lancet Neurol paper is 2018 (circadian/circaseptan).
- Stirling et al. 2021, "Seizure forecasting and cyclic control of seizures" (Epilepsia) — [epi.16541](https://onlinelibrary.wiley.com/doi/abs/10.1111/epi.16541)

### Inferences
- In TUSZ, time of day and sleep stage (circadian proxies) can be added as covariates. Multidien phase cannot be estimated from sessions lasting hours.
- A plausible project: test whether CSD or aperiodic features in scalp EEG vary with time of day in the same direction as seizure occurrence.

### Gaps
- It is unknown whether scalp EEG features alone, without implants, can recover multidien phase. Wearable heart-rate studies suggest cycles are observable non-invasively.

---

## 5. Which biomarkers were tested with rigorous stats (surrogate/random predictor), and results

### Takeaway
Rigorous (random-predictor or pseudoprospective) validation exists mainly for long-term **iEEG** biomarkers: NeuroVista, Maturana CSD, Baud and Proix IED cycles, and the Khambhati connectivity snapshot. Scalp EEG prediction studies report high sensitivity but almost all carry high or unclear risk of bias (leakage, patient-specific splits), and none used TUSZ.

### Cited Findings
- Kuhlmann et al. 2018 (Nat Rev Neurol) reviewed the field: the 2007 Mormann review found insufficient evidence for prediction, and the first prospective prediction came from the NeuroVista implanted-device trial in a small number of patients. They refine guidelines (surrogate or random-predictor testing, out-of-sample and pseudoprospective evaluation) — [s41582-018-0055-2](https://www.nature.com/articles/s41582-018-0055-2)
- Maturana 2020: pseudoprospective sensitivity 77 ± 8% at 8 ± 6% time in warning vs a Markov random predictor (~9%) — [PMC7195436](https://pmc.ncbi.nlm.nih.gov/articles/PMC7195436/)
- Alasade et al. 2026 systematic review of scalp-EEG prediction (17 studies, 2016–2025):
  - Datasets: 76.5% used CHB-MIT and **0 used TUSZ**.
  - Reported sensitivity 55–100%, false-positive rate 0.039–0.73/h, and highly inconsistent SPH/SOP definitions.
  - No study had low risk of bias (47% high, 53% unclear). The dominant issue was leakage from overlapping windows or non-independent train/test.
  - Recommendations: chronological or patient-wise splits, false-positive rate per hour, time in warning, and prospective validation.
  - [PMC13318060](https://pmc.ncbi.nlm.nih.gov/articles/PMC13318060/)
- Nonstationarity in long-term iEEG undermines fixed preictal/interictal classifiers (arXiv 2022) — [arXiv 2201.04137](https://arxiv.org/pdf/2201.04137)

### Inferences
- Any student project on TUSZ should include a rate-matched random predictor or seizure-time surrogates (shuffle seizure onset times, keep features), chronological splitting, and a report of time in warning. This alone would put it above most published scalp work.
- TUSZ is a detection corpus: records are often short, with few seizures per patient and few long interictal baselines. Classic patient-specific prediction is hard there. Population-level, mechanistically motivated feature studies (e.g. does the exponent or autocorrelation change in the last 10–30 min, compared with matched interictal segments?) fit the data better.

### Gaps
- No published prospective scalp-EEG seizure prediction trial with a random-predictor test was found.

---

## 6. What scalp EEG physically can and cannot tell about neurons/synapses

### Takeaway
Scalp EEG mainly reflects summed postsynaptic currents of pyramidal neurons in synchronously active cortical patches of roughly 10–20 cm^2 (gyral crowns favored). It cannot resolve single-unit heterogeneity, interneuron subtypes, depolarization block, K+/Cl- dynamics, the core vs penumbra distinction, or (in routine recordings) HFOs and DC shifts. It *can* index population-level dynamics: spectral slope, variance and autocorrelation, rhythms, IEDs, and sleep/vigilance state.

### Cited Findings
- Tao et al. 2005 (Epilepsia, foundational), simultaneous scalp and 46–98-channel iEEG in 16 TLE patients: scalp-visible interictal spikes usually need synchronous activation of about 10–20 cm^2 of gyral cortex — [Wiley](https://onlinelibrary.wiley.com/doi/10.1111/j.1528-1167.2005.11404.x); [PubMed 15857432](https://pubmed.ncbi.nlm.nih.gov/15857432/); ictal-pattern extension, Tao 2007 — [Wiley](https://onlinelibrary.wiley.com/doi/10.1111/j.1528-1167.2007.01224.x)
- Hippocampal spikes have heterogeneous scalp correlates, and deep sources are often invisible on scalp — [Epilepsy Res 2022](https://www.sciencedirect.com/science/article/abs/pii/S0920121122000651)
- Counterpoint: sparse asynchronous cortical generators can still produce measurable scalp signals (NeuroImage 2016). The 10 cm^2 rule applies to *visible spikes*, not to all spectral features. [Evidence: contested nuance] — [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1053811916301884)
- Biophysics review (Beniczky & Schomer 2020): volume conduction, reference and montage effects — [Epileptic Disord](https://onlinelibrary.wiley.com/doi/full/10.1684/epd.2020.1217)
- Simulation with realistic elderly head models: detectability of spikes depends on source size and location — [Clin EEG Neurosci 2025](https://doi.org/10.1177/15500594251323625)
- On scalp, seizures appear later than intracranially, especially from deep sources. Missing DC and volume conduction limit bifurcation typing to ~40–50% of seizures — [PMC11747977](https://pmc.ncbi.nlm.nih.gov/articles/PMC11747977/)

### Inferences
Mechanism-to-scalp mapping table:

| Mechanism | Scalp proxy | Time before onset | Scale where measured | Evidence |
|---|---|---|---|---|
| Loss of resilience (slow approach to bifurcation) | variance, lag-1 AC, IED-triggered recovery | 10s of min–h; days (cycles) | iEEG; scalp untested | strong (iEEG), none rigorous on scalp |
| E/I set-point shift | aperiodic exponent (increase reported) | 13 min (scalp); 12 h (RNS) | scalp hd-EEG + iEEG | moderate, confounded |
| IED rate (synaptic perturbations) | spike rate | cycles (days); may drop pre-seizure | scalp and iEEG | strong for cycles, contested short-term |
| Interneuron hyperactivity / depolarization block / K+ | none direct (possible high-gamma on iEEG) | seconds | slice/animal/microelectrode | moderate (animal) |
| Core recruitment vs penumbra | none | seconds | microelectrode | foundational |
| Network synchrony change | wPLI/imag. coherence (scalp); connectivity (iEEG) | min–h | iEEG; scalp confounded by volume conduction | contested/strong (Nat Med 2024 iEEG) |
| Infraslow/DC, HFO coupling | not in routine scalp | ~10 min | iEEG; DC scalp with long TC | weak for prediction |
| Complexity (spectral entropy, Hjorth) | yes | ~83 ± 60 min | scalp | weak–moderate |

### Gaps
- No quantitative estimate was found of what fraction of TUSZ seizures have scalp-visible preictal changes. The Segal 2025 figure (89.5%) comes from a different, small cohort without prospective validation.
