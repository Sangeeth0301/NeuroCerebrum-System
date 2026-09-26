# Neurotechnology for Preventing Seizures: Single-Neuron / High-Density Recordings of the Preictal Period, Predictive Therapy, High-Channel BCIs, Warning Systems

Scope note: research done 2026-09-25 with about 22 tool calls. I did not repeat the companion file `Novel early seizure detection ideas/closed_loop_bci.md`, which covers RNS detectors and power, the NeuroVista numbers, Epiminder, UNEEG, Empatica, the Neuralink 2019 power figures and on-chip ASICs.
- [FOUNDATIONAL] marks work from before 2018.
- "(snippet)" marks facts taken only from search-result summaries or abstracts, without a full-text read. Check these before quoting exact numbers.
- NCBI/PubMed, Wiley and Nature full texts were often blocked (captcha or 403), so several items rely on abstracts or PMC mirrors.

## 1. What do single-neuron / microelectrode recordings show in the minutes before seizures?

### Takeaway
The single-unit evidence for a consistent preictal state is **mixed and heterogeneous**:
- **Neocortical Utah-array studies** show that a subset of neurons (including interneurons, and neurons *outside* the onset zone) change firing **minutes** before onset. Multi-unit activity from arrays 2–3 cm from the onset zone could discriminate preictal from interictal periods (AUC up to about 0.9, in-sample, 5 patients).
- **Hippocampal microwire studies** (Agopyan-Miu 2023) found **no systematic firing change in the 5 min before onset**, and a criticality analysis of 20 patients found **no drift toward instability** before seizures.

The strongest, most reproducible single-unit phenomena are **ictal**, not preictal. These include:
- the ictal wavefront and the core/penumbra split;
- the loss of inhibition in neocortex versus the preservation of inhibition in the hippocampus.

Recording both individual units and multi-unit activity adds information but does not yet give a reliable minutes-ahead warning.

### Cited Findings
- **Truccolo et al. 2011, Nat Neurosci [FOUNDATIONAL]:**
  - Setup: 96-channel, 4×4 mm Utah arrays in 4 patients, recording 57–149 simultaneous neocortical neurons.
  - Spiking at seizure initiation and spread was "highly heterogeneous, not hypersynchronous".
  - Neurons **outside the region of seizure onset showed significant changes minutes before onset**.
  - 79% of interneurons and 68% of principal cells showed some preictal or ictal modulation.
  - The fraction of interneurons with a *preictal increase* was 60% larger than the corresponding fraction of principal cells.

  — [Nature Neuroscience nn.2782](https://www.nature.com/articles/nn.2782); [PubMed 21441925](https://pubmed.ncbi.nlm.nih.gov/21441925/) (snippet)
- **Hippocampal preictal firing review (Jasper's / NCBI Bookshelf):**
  - Preictal firing changes are less frequent than ictal changes: **11.8% of neurons increased and 7.5% decreased** preictally.
  - About 30% of units change firing several hundred ms before *interictal* discharges.
  - Patterns were "heterogeneous and followed no uniform pattern".
  - Babb & Crandall (1976) first recorded human seizures with microelectrodes and saw firing increase before seizures [FOUNDATIONAL].

  — [Jasper's Basic Mechanisms, Human Single-Neuron Recordings in Epilepsy](https://www.ncbi.nlm.nih.gov/books/NBK609894/) (snippet; the full text was captcha-blocked); [PMC3799238](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3799238/) (snippet); [PMC7842750](https://pmc.ncbi.nlm.nih.gov/articles/PMC7842750/) (snippet)
- **Bower et al. 2012, Epilepsia [FOUNDATIONAL]:**
  - Described as the first study of long-term firing rates leading into seizures relative to the seizure-onset zone.
  - Preictally they saw **extrafocal high-frequency power decrements that correlated with seizure spread**, meaning periictal changes extend beyond the focus.

  — [Wiley, Bower et al. 2012](https://onlinelibrary.wiley.com/doi/10.1111/j.1528-1167.2012.03417.x) (snippet)
- **Proix et al. 2019, PLOS One (Truccolo/Cash group):**
  - Setup: Utah arrays in 5 patients, placed **2–3 cm distal to the clinical onset areas**. The preictal window was **65 to 5 min before onset**.
  - Features: multi-unit activity (MUA) counts and envelope, LFP in 10 bands (0.3–500 Hz), coherence and correlation.
  - AUC reached **about 90% for at least one feature type in every patient**, and **prediction was possible from MUA alone**.
  - Limitations: only 2–3 seizures per patient, 1–2 weeks of recording, hyperparameters tuned on test data.

  — [PMC6645464](https://pmc.ncbi.nlm.nih.gov/articles/PMC6645464/); [PLOS One](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0211847)
- **Related Utah-array work:**
  - LFP from intracortical arrays predicts seizures. — [PMC6094384](https://pmc.ncbi.nlm.nih.gov/articles/PMC6094384/) (title/snippet)
  - Ongoing intracortical activity predicts upcoming interictal discharges. — [PMC7856677](https://pmc.ncbi.nlm.nih.gov/articles/PMC7856677/) (title)
  - A combined LFP+MUA *detector* reached 100% sensitivity, 2.7 s mean latency and 0.13 false alarms/h. — [search summary, TBME 2019](https://doi.org/10.1109/TBME.2019.2921448) (snippet; I did not verify which paper this number comes from)
- **Agopyan-Miu, Merricks, Smith, …, Trevelyan, Schevon 2023, Brain:**
  - Setup: 19 patients, 34 seizures, 156 single units, Behnke-Fried hybrid macro-micro depth electrodes in limbic structures.
  - During recruitment, **69.2% of neurons reduced firing and 21.8% ceased**, including fast-spiking interneurons. Only 1 of 17 fast-spiking cells showed the neocortical pattern of an increase followed by cessation.
  - Across the **5 min before onset**, there were **no systematic preictal firing changes**.
  - The authors conclude that inhibition is preserved in mesial temporal structures, "in contrast to the inhibitory collapse scenario documented in neocortex."

  — [Brain 146(12):5209](https://academic.oup.com/brain/article/146/12/5209/7236754)
- **Hagemann et al. (arXiv 2004.10642; published 2021):**
  - Single units from focal and non-focal hemispheres in 20 patients.
  - "Neither did focal areas generally operate closer to instability, nor were seizures preceded by a drift towards instability." Cortex stayed slightly subcritical.
  - This argues against a universal "approach to criticality" preictal marker at the single-unit scale.

  — [arXiv 2004.10642](https://arxiv.org/abs/2004.10642)
- **Ictal (not preictal) microelectrode findings that shape device design:**
  - The Schevon/Trevelyan "ictal wavefront" shows intense, phase-locked unit firing only in the ictal *core*. The *penumbra* shows large LFP signals without intense spiking.
  - Phase-locked high gamma (80–150 Hz) marks the core, and resecting it correlates with better outcomes.
  - Unit firing rises toward seizure end, then falls silent for many seconds.
  - Unit changes can precede LFP-defined onset.
  - Microelectrodes have "no indications" in routine clinical care. The review proposes adding them to responsive neurostimulation.

  — [Brain Communications 2020, "Microelectrode recordings in human epilepsy: a case for clinical translation"](https://academic.oup.com/braincomms/article/2/2/fcaa082/5857125)
- **Laminar recordings:** Seizure initiation exclusively involves the granular and infragranular layers. — [Nat Commun 2024, s41467-024-48746-8](https://www.nature.com/articles/s41467-024-48746-8) (snippet)
- **Merricks et al. (J Neurosci 2021)** tracked neuronal firing and waveform changes through ictal recruitment. Waveform changes during seizures complicate spike sorting. — [J Neurosci 41(4):766](https://www.jneurosci.org/content/41/4/766) (title/snippet)
- **A 2025 medRxiv preprint** reports that MUA and high-gamma dissociate in the seizure-onset zone during focal-to-bilateral tonic-clonic seizures. — [medRxiv 2025.11.03.25339320](https://www.medrxiv.org/content/10.1101/2025.11.03.25339320.full.pdf) (title)
- **Animal cell-type evidence (Miri, Vinck, Pant, Cardin, eLife 2018):**
  - Setup: mouse, induced seizures, optotagged interneurons.
  - More than 90% of PV interneurons showed a **sharp late increase in firing just before onset**.
  - SST interneurons showed a sustained preictal increase and a progressively weaker response to input over the preictal period, which was split into quartiles spanning minutes.
  - The authors caution that induced seizures may differ from spontaneous ones.

  — [eLife 40750](https://elifesciences.org/articles/40750)
- **Neuropixels in humans:**
  - Chung et al. (Neuron 2022) recorded up to about 100 single units at once, and more than 200 neurons in 2 cases over 5–10 min, intraoperatively in 11 patients undergoing anterior temporal lobectomy.
  - Units appeared within about 1 min of reaching target depth.
  - These are acute recordings of **minutes**, so they cannot capture spontaneous preictal periods.

  — [Neuron S0896627322004482](https://www.sciencedirect.com/science/article/pii/S0896627322004482); [bioRxiv](https://www.biorxiv.org/content/10.1101/2021.12.29.474489v1.full); [MGH Advances](https://advances.massgeneral.org/neuro/journal.aspx?id=2207)
- **Chronic Neuropixels in epileptic rats** (near-continuous, long-term) is feasible. — [PubMed 37369197](https://pubmed.ncbi.nlm.nih.gov/37369197)

### Inferences
- The best single-unit evidence for preictal change is **neocortical, a minority of neurons, often outside the onset zone, on a minutes scale**. Hippocampal and limbic data (the most common drug-resistant epilepsy) show little systematic preictal firing change within 5 min. A preictal biomarker from high-density arrays is therefore likely to be a *population or network* feature (MUA, spike band power, correlations or coherence, LFP band power), not the firing of any one neuron.
- MUA alone was predictive (Proix 2019). This supports **spike-sorting-free features**, which suit on-implant compute and also sidestep the unit waveform changes seen during recruitment (Merricks 2021).
- Array placement matters. The ictal core and penumbra differ sharply in spiking, and a small 4×4 mm array samples only a tiny patch. Evidence that distal neocortex carries preictal information hints that a wide-coverage, high-density device might not need to sit in the onset zone.

### Gaps
- I found **no published human preictal analysis from Neuralink, Paradromics or Precision arrays**. Their human epilepsy-surgery recordings were intraoperative and minutes long.
- I found no prospective, out-of-sample human seizure prediction using single units. All the human microelectrode prediction work is retrospective with only a few seizures per patient.
- I could not retrieve the full texts of Schevon 2012 (Nat Commun), Smith 2016 or Weiss 2013 for exact numbers. The Paulk et al. 2022 Nat Neurosci Neuropixels paper was not retrieved.

## 2. Preventive / predictive therapy triggered by rising risk rather than onset

### Takeaway
Therapy delivered in response to *risk* has good animal proof-of-concept:
- IED-triggered stimulation prevents epilepsy progression.
- On-demand optogenetics halts seizures.
- Focal cooling and on-demand drug delivery have been demonstrated.

In humans, **chronotherapy guided by cycles is still mostly modelling and observation**. RNS "risk-phase" timing is associative (see the companion file). Required warning times differ by therapy:
- seconds for stimulation or optogenetics;
- minutes to hours for fast drugs;
- hours to days for adjusting oral antiseizure medication (ASM) dosing, where multidien forecasts suffice.

### Cited Findings
- **Krook-Magnuson et al. 2013, Nat Commun [FOUNDATIONAL]:**
  - A real-time, closed-loop, on-demand optogenetic system arrested *spontaneous* seizures in the intrahippocampal kainate mouse model of temporal lobe epilepsy.
  - It worked by activating PV interneurons (or inhibiting principal cells). It is onset-triggered, not predictive.

  — [Nat Commun ncomms2376](https://www.nature.com/articles/ncomms2376); [PMC3562457](https://pmc.ncbi.nlm.nih.gov/articles/PMC3562457/)
- **Paz et al. 2013, Nat Neurosci [FOUNDATIONAL]:**
  - After cortical stroke in rats, the **thalamus was required to sustain cortical seizures**. Thalamocortical neurons became hyperexcitable, with altered HCN expression.
  - Closed-loop optogenetic intervention anywhere in the thalamocortical loop interrupted seizures.
  - This supports targeting a remote node.

  — [Nat Neurosci nn.3269](https://www.nature.com/articles/nn.3269); [PubMed 23143518](https://pubmed.ncbi.nlm.nih.gov/23143518/)
- **Ferrero et al. 2025, Nat Neurosci** (a key "prevention, not abortion" result):
  - **Trigger:** real-time detection of hippocampal IEDs (50–85 Hz band) triggered medial prefrontal cortex stimulation in kindled rats (11 closed-loop, 10 kindled controls, 7 sham).
  - **Results:** it reduced independent prefrontal IEDs and **prevented progression to bilateral convulsive seizures** (log-rank p=2.4×10⁻³). It also preserved spatial memory and abolished IED–spindle coupling.
  - **Human validation:** iEEG from 9 patients.
  - The authors' framing: "temporally targeted interventions that block the network effect of IEDs may modify disease course."

  — [PMC12321579](https://pmc.ncbi.nlm.nih.gov/articles/PMC12321579/); [Nature Neuroscience s41593-025-01988-1](https://www.nature.com/articles/s41593-025-01988-1)
- **Closed-loop vs open-loop in rodents [FOUNDATIONAL]:** closed-loop DBS triggered by icEEG patterns cut seizure frequency by 90% versus 17% for open-loop. — [PubMed 26571534](https://pubmed.ncbi.nlm.nih.gov/26571534/) (snippet)
- Closed-loop sequential localized electric fields at the focus controlled seizures in a rodent temporal lobe epilepsy model. — [Nat Commun 2022, s41467-022-35540-7](https://www.nature.com/articles/s41467-022-35540-7) (title)
- **Chronotherapy modelling (Ahern et al. 2026, Frontiers in Network Physiology):**
  - Method: **simulation only**, validated against 24 h EEG from about 100 patients.
  - For short-half-life levetiracetam, doses given **about 6 h before the peak in seizure likelihood** gave up to 20% greater reduction in epileptiform discharges.
  - Under twice-daily dosing (90% of the dose in the primary administration), optimal timing gave a 62.4% reduction versus 45.3% at the worst timing, with the same total dose.
  - Long-half-life drugs showed little dependence on dosing phase.

  — [PMC12891084](https://pmc.ncbi.nlm.nih.gov/articles/PMC12891084/)
- **Cycles and ASMs:**
  - "Seizure Cycles under Pharmacotherapy" (Ann Neurol 2024). — [Friedrichs-Maeder et al.](https://onlinelibrary.wiley.com/doi/abs/10.1002/ana.26878) (title)
  - A 2025 preprint asks whether ASM changes affect seizure timing. — [medRxiv 2025.07.10.25331313](https://www.medrxiv.org/content/10.1101/2025.07.10.25331313.full.pdf) (title)
  - Multidien interictal epileptiform activity (IEA) cycles weaken after an adjunctive ASM is started, and this correlated with seizure control for up to 12 months. — (snippet from search summary of the [Chronoepileptology review, Epilepsy Currents 2026](https://journals.sagepub.com/doi/full/10.1177/15357597251392099); exact primary source not verified)
  - Long-horizon forecasts "could be used to guide increased dosage or adjunctive medications during high-risk periods". — [Chronoepileptology 2026](https://journals.sagepub.com/doi/full/10.1177/15357597251392099) (snippet)
- **Focal cooling:**
  - In animals, cooling to 24 °C rapidly terminated seizures.
  - Cooling as low as 5 °C for up to 10 months caused no significant cortical damage.

  — [PMC10101767, focal cooling review](https://pmc.ncbi.nlm.nih.gov/articles/PMC10101767/) (snippet)
- **On-demand drug delivery:**
  - The hydroElex conductive-hydrogel microneedle array uses recorded neural signals to trigger voltage-driven drug release. — [PMC11584000](https://pmc.ncbi.nlm.nih.gov/articles/PMC11584000/) (snippet)
  - An on-demand delivery system has been demonstrated for epileptiform seizures. — [PMC8879600](https://pmc.ncbi.nlm.nih.gov/articles/PMC8879600/) (title)
  - A nanoengineered on-demand system improved pharmacotherapy efficacy. — [PMC8754409](https://pmc.ncbi.nlm.nih.gov/articles/PMC8754409/) (title)
  - A 2025 Epilepsy Currents commentary discusses a closed-loop device for direct delivery of antiseizure therapeutics ("therapeutic seizure monitoring"). — [Eyal 2025](https://journals.sagepub.com/doi/full/10.1177/15357597251320190) (title only; 403)
  - Review framing closed-loop epilepsy systems as BCI-like read–write loops. — [Applied Sciences 2026, 16(1):294](https://doi.org/10.3390/app16010294) (title)

### Inferences
- There are three plausible warning-time tiers for a prediction project:
  1. **Seconds to about 1 min** (pre-onset or early onset) for stimulation, optogenetics or local drug release.
  2. **Minutes to about 1 h** (the Proix 2019 horizon of 65–5 min) for a fast rescue drug (such as intranasal or buccal benzodiazepines) or for behavioural safety.
  3. **Hours to days** (cycle-based forecasts) for timing or boosting oral ASMs. The Ahern model suggests about 6 h of lead time helps for short-half-life drugs.
- Ferrero 2025 suggests an interesting target: treat **IED bursts / pro-ictal states** rather than individual seizures. Pro-ictal states are more frequent and more predictable, so detection is easier.

### Gaps
- I found no human RCT of therapy triggered by a *prediction* (as opposed to onset). The NeuroVista advisory did not deliver therapy.
- I found no human trial of forecast-guided chronotherapy with clinical outcomes.
- I did not retrieve human data on focal cooling for prevention.

## 3. High-channel BCIs: epilepsy relevance, data rates, features

### Takeaway
None of the high-channel BCI companies markets an epilepsy therapy.
- **Precision's** 510(k)-cleared Layer 7 thin-film array (up to 30 days) is explicitly indicated for uses including epilepsy-surgery mapping.
- **Paradromics'** first human recording took place during epilepsy surgery.
- **Neuralink** has only aspirational seizure claims, which I could not find in any primary source.

Data rates, from secondary sources, are tens of Mb/s raw. That pushes on-implant processing toward spike detection and band power (MUA or spike band power) rather than sorted units.

### Cited Findings
- **Precision Neuroscience Layer 7:**
  - FDA 510(k) K242618 (clearance announced April 2025) covers recording, monitoring and stimulation on the cortical surface for up to 30 days. Indicated uses include **epilepsy-surgery high-resolution mapping**.
  - A record 4,096 electrodes were recorded at once in a human, using four arrays at Mount Sinai in May 2024.

  — [FDA K242618](https://www.accessdata.fda.gov/cdrh_docs/pdf24/K242618.pdf); [GlobeNewswire](https://www.globenewswire.com/news-release/2025/04/17/3063418/0/en/Precision-Neuroscience-Receives-FDA-Clearance-for-High-Resolution-Cortical-Electrode-Array.html); [MedTech Dive](https://www.medtechdive.com/news/precision-neuroscience-brain-implant-fda-cleared/745913/)
- **Paradromics Connexus:**
  - 421-electrode microwire module (electrodes about 1.55 mm long). Up to 4 modules give 1,684 electrodes.
  - Preclinical benchmark above 200 bps with about 50 ms delay.
  - Infrared transcutaneous link at 100 Mbit/s.
  - Cleared to start a speech trial.

  — [Wikipedia (Paradromics)](https://en.wikipedia.org/wiki/Paradromics) (secondary); [bciintel](https://bciintel.com/devices/paradromics-connexus/) (secondary); [pharmaphorum](https://pharmaphorum.com/news/neuralink-rival-paradromics-cleared-start-speech-trial)
- **Neuralink N1:** 1,024 electrodes on 64 threads, a few hundred kbps compressed and about 2–25 Mbps raw (secondary, unverified). Paradromics claims 20× Neuralink's initial data rate. — [bciintel/Medium summary via search](https://medium.com/@dilee./paradromics-when-bandwidth-becomes-the-bottleneck-breaker-in-neural-interface-design-4a1c230f139c) (non-primary); [Paradromics blog on Neuralink](https://paradromics.com/insights/neuralink-implant/) (competitor source, biased)
- **Neuralink and seizures:**
  - Media say Neuralink cites seizures among potential medical uses; public statements focus on motor, speech and vision. — [CNBC 2022](https://www.cnbc.com/2022/12/01/elon-musks-neuralink-makes-big-claims-but-experts-are-skeptical-.html); [Fortune 2020](https://fortune.com/2020/08/27/elon-musk-brain-company-neuralink)
  - A 2019 commentary on the Neuralink white paper argued that thousands of channels could improve preictal classification and reduce false positives. This is opinion, not data. — [PMC6914250](https://pmc.ncbi.nlm.nih.gov/articles/PMC6914250/)
- A thin-film intracranial electrode (FDA-cleared) has published biocompatibility testing. — [PMC9100917](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9100917/) (title)
- **MUA is sufficient:** threshold-crossing MUA counts alone predicted seizures (see Proix 2019 in Section 1). — [PMC6645464](https://pmc.ncbi.nlm.nih.gov/articles/PMC6645464/)

### Inferences
- A realistic "Neuralink-style" seizure-prediction pipeline would stream or compute per-channel **threshold-crossing rate / spike band power (about 300–5,000 Hz power) plus low-frequency LFP band power** on the implant, then run a small model. Spike sorting is costly and unstable during seizures.
- These devices are all in or near motor, speech and sensory cortex, not mesial temporal structures. Using them for epilepsy would need placement over a neocortical focus or the distal-network approach suggested by Proix 2019.

### Gaps
- There are no primary (company) N1 or Connexus specifications for per-channel bandwidth or on-implant feature extraction, and no Synchron or Blackrock epilepsy statements. (Synchron's stentrode has 16 electrodes; this is not verified here.)
- I found no primary evidence of any Neuralink epilepsy trial.

## 4. Patient-facing warning systems: needs, false alarms, warning time

### Takeaway
- Patients value **sensitivity over specificity**: they tolerate false alarms more readily than missed seizures.
- They want both high-risk and low-risk forecasts (like a weather forecast).
- Preferred horizons vary with seizure frequency. In one survey, preferences split roughly evenly between hourly, 12 h, 24 h and more than 24 h. Older surveys favoured short imminent warnings of 3–5 min to limit anxiety.
- Commonly cited targets are ≥90% sensitivity and fewer than 1 false alarm per day.

### Cited Findings
- **Epilepsy Foundation survey 2021 (Frontiers in Neurology):**
  - N=652 (64% people with epilepsy, 36% caregivers).
  - Preferred warning window: 28% within 24 h, 23% within 12 h, 20% hourly, 20% more than 24 h. People with daily seizures preferred hourly warnings; those with 3–4 seizures a year wanted more than 24 h.
  - **65% would keep using the device after a false alarm, but only 52% would continue if a seizure occurred during a low-risk forecast.**
  - 60% wanted both high- and low-risk forecasts.
  - Uses: driving, sport, working from home, mental preparation.
  - Concern: anxiety from constantly checking forecasts.

  — [Frontiers Neurol 2021, fneur.2021.717428](https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2021.717428/full)
- **Best–worst scaling study (Epilepsy Behav 2019):**
  - Short forecasting range was the most-favoured attribute, followed by mid range and notification of a high chance of seizure.
  - Preferred notification thresholds depend on seizure frequency and anxiety.

  — [PubMed 31150998](https://pubmed.ncbi.nlm.nih.gov/31150998); [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1525505019302689) (snippet)
- **Performance targets and preferred warning times (surveys):**
  - Patients desire more than 90% detection or prediction accuracy and fewer than 1 false trigger per day. Caregiver alerts should come within 1 min. — [search summary of survey literature incl. PubMed 27607108](https://pubmed.ncbi.nlm.nih.gov/27607108/) (snippet)
  - Patients preferred wearables over implants, high-risk over low-risk identification, and **shorter warning times (3–5 min)**. Patients were more tolerant of inaccurate predictions than caregivers. — [Seizure forecasting: Where do we stand? (PMC10423299)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10423299/); [Karoly et al., Epilepsia 2025/26](https://onlinelibrary.wiley.com/doi/full/10.1002/epi.70394) (snippet)
- **Wearable forecasting performance:**
  - An E4 wristband forecast was significantly better than chance in 43% of patients, with 75.6% sensitivity at a 30-min horizon.
  - Cycle-based 24 h forecasts beat chance in 66% of subjects.
  - Clinicians often misinterpret risk probabilities.

  — [PMC10423299](https://pmc.ncbi.nlm.nih.gov/articles/PMC10423299/)
- Wearables for diaries and forecasting outside the clinic. — [Frontiers Neurol 2021, fneur.2021.690404](https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2021.690404/full) (title)
- Risk-controlling prediction calibration has been proposed to reduce false alarm rates. — [Frontiers Neurosci 2023](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2023.1184990/full) (title)

### Inferences
- For a student project, report:
  - **time-in-warning** and **false alarms per day** next to sensitivity;
  - performance at several horizons (for example 5 min, 1 h, 24 h);
  - calibrated probabilities rather than binary alarms, since users want graded low- and high-risk output.
- An accurate "low-risk" state may matter as much as a high-risk alarm. Missed seizures during low-risk forecasts erode trust more than false alarms do.

### Gaps
- Seer, Epiminder and UNEEG patient-app forecasting performance was not retrieved here; see the companion file for device status.
- I found no consensus FDA performance standard for prediction or advisory devices.

## 5. Ethics and regulatory issues for predictive alerts

### Takeaway
The main issues are:
- over-reliance on "low-risk" states (safety);
- anxiety from high-risk alerts;
- varied risk tolerance between patients;
- regulatory uncertainty about how to judge a "warning-only" device;
- reimbursement;
- device abandonment, as happened with NeuroVista.

### Cited Findings
- Ethical concerns centre on "miscalibrated reliance on low-risk states", anxiety from high-risk advisories, and varied preferences and risk tolerance. — [Karoly et al., "Seizure forecasting: the long and winding road to clinical translation", Epilepsia](https://onlinelibrary.wiley.com/doi/full/10.1002/epi.70394) (snippet; full text 403)
- **NeuroVista's failure had several causes:**
  - device-related adverse events that required explantation in two patients;
  - no clear reimbursement pathway;
  - **regulatory uncertainty about performance standards for a risk-advisory system**.

  Regulators were unsure how to justify trial risk when there was "no treatment", or how to define success.

  — [Karoly et al., Epilepsia](https://onlinelibrary.wiley.com/doi/full/10.1002/epi.70394) (snippet); [Cook et al. 2013, PubMed 23642342](https://pubmed.ncbi.nlm.nih.gov/23642342/) [FOUNDATIONAL]
- **Device abandonment** (implants left in patients after support ends) is a broader ethical concern. — [Karoly et al., Epilepsia](https://onlinelibrary.wiley.com/doi/full/10.1002/epi.70394) (snippet)
- Clinicians misinterpret probabilistic forecasts, and forecasts pose a communication problem. The ultimate measure of benefit is quality of life. — [PMC10423299](https://pmc.ncbi.nlm.nih.gov/articles/PMC10423299/)

### Inferences
- A prediction output that drives *therapy* (closed loop) is judged by clinical outcome, as RNS was. A *warning-only* output carries the unresolved "what is success" problem. Pairing prediction with an actionable intervention, such as rescue medication or stimulation, may make the regulatory path easier.
- Driving and legal use of "low-risk" forecasts is a liability area. I found no regulatory guidance on it.

### Gaps
- I found no FDA guidance document specific to seizure prediction or forecasting devices.
- I did not retrieve ethics literature specific to high-channel BCIs in epilepsy (privacy of neural data, research-only implants).
