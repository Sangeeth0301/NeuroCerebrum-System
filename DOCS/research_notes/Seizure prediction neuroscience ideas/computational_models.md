# Computational Neuroscience Models for Inferring Hidden Synaptic/Neuronal States from EEG, and Their Use in Seizure Prediction

Scope note: the research used about 17 search/fetch calls. Several publisher pages (ScienceDirect, PubMed) blocked fetching, so some details come from search-result abstracts and are marked as such. Work from before 2018 is labelled [FOUNDATIONAL].

## 1. Neural mass / neural field models: which parameters map to synaptic gains and E/I?

### Takeaway
Jansen-Rit and its extension, the Wendling model, are the standard "cortical column" models that can be fitted to EEG. Their parameters can be read directly as physiology: average excitatory and inhibitory synaptic gains (A, B, G), PSP time constants, connectivity constants between populations, and firing thresholds. So a fitted A/B or A/(B+G) ratio is a proxy for E/I balance. The Epileptor is different. It is phenomenological: one excitability parameter (x0) and a slow "permittivity" variable set how close a region is to seizure. It is used for whole-brain virtual patients, not for synaptic read-out.

### Cited Findings
- [FOUNDATIONAL] Wendling et al. 2002 (Eur J Neurosci), "Epileptic fast activity can be explained by a model of impaired GABAergic dendritic inhibition." It extends Jansen-Rit with a second inhibitory population, giving slow dendritic (GABA_A,slow) and fast somatic (GABA_A,fast) inhibition. It explains the gamma-band fast activity at focal seizure onset through reduced dendritic inhibition — [PubMed 12028360](https://pubmed.ncbi.nlm.nih.gov/12028360/); [Wiley](https://onlinelibrary.wiley.com/doi/abs/10.1046/j.1460-9568.2002.01985.x)
- The Wendling model has 4 neural masses: pyramidal cells, excitatory interneurons, slow inhibitory interneurons and fast inhibitory interneurons. Standard parameters are A = 3.25 mV (average excitatory synaptic gain), B = 22 mV (slow dendritic inhibitory gain), G = 20 mV (fast somatic inhibitory gain), about 10 ms excitatory PSP time constant and about 35 ms inhibitory time constant — [U Twente thesis summarising model](https://www.utwente.nl/en/eemcs/magnus/teaching/Thesis/hebbink-jurgen-activity-types-in-a-neural-mass-model-fp-report-final.pdf); [bifurcation analysis, J Integr Neurosci 2016](https://www.worldscientific.com/doi/abs/10.1142/S0219635216500254)
- Recent theory on Wendling-type models still continues, for example a 2025 Scientific Reports analysis of normal and epileptic output using a cyclic small-gain theorem — [Sci Rep 2025](https://www.nature.com/articles/s41598-025-20315-z)
- Jansen-Rit reduces a cortical column to three interacting populations (pyramidal neurons, excitatory interneurons, inhibitory interneurons). It has been combined with a head model (Ary's model) that projects intracranial sources to the scalp — [Escuain-Poole et al., Front Appl Math Stat 2018 / arXiv 1708.05282](https://www.frontiersin.org/articles/10.3389/fams.2018.00046/full)
- [FOUNDATIONAL] Epileptor, Jirsa et al. 2014, Brain, "On the nature of seizure dynamics": 5 state variables. A slow "permittivity" variable controls seizure onset and offset. Seizures typically begin through a saddle-node bifurcation and end through a homoclinic bifurcation, and this holds in human, zebrafish and mouse. The authors argue that many biophysical mechanisms can map onto the same invariant dynamics — [PMC4107736](https://pmc.ncbi.nlm.nih.gov/articles/PMC4107736/); [Brain](https://academic.oup.com/brain/article/137/8/2210/2847958)
- In the Aarabi & He model-based predictor, a Jansen-Rit-type model (pyramidal cells, excitatory and inhibitory interneurons) had 12 estimated parameters. Parameter changes consistent with seizure physiology include higher PSP amplitudes, a longer inhibitory PSP time constant, a lower firing threshold at onset, and a higher threshold as the seizure moves toward termination (from search-result abstract) — [PubMed 24374087](https://pubmed.ncbi.nlm.nih.gov/24374087/)
- A 2024 Physical Review E paper, "Sensitivity-analysis-guided Bayesian parameter estimation for neural mass models: applications in epilepsy," points out that NMMs are high-dimensional and it is unclear which parameters can be estimated reliably. It uses sensitivity analysis to choose which parameters to infer — [Phys Rev E 110, 044208](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.110.044208); [bioRxiv preprint](https://www.biorxiv.org/content/10.1101/2023.04.03.535345.full.pdf)

### Inferences
- For a student project, fitted A, B, G (Wendling) or the Jansen-Rit connectivity constants are the most interpretable "synaptic" read-outs. Ratios such as A/B or A/G give a model-based E/I index. x0 in the Epileptor is better understood as "regional epileptogenicity" than as a synaptic quantity.
- Identifiability is a real problem: many parameter combinations produce similar spectra. Sensitivity analysis (as in the PRE 2024 paper) should come before any claim that a synaptic gain is "tracked."

### Gaps
- No primary 2018–2026 sources were retrieved for the Liley model or the Lopes da Silva (1974) alpha model. Their parameter mappings are not documented here, so the writer should not make specific claims about them without further sourcing.

## 2. Model inversion from EEG: Kalman/UKF, DCM, SBI, PINNs

### Takeaway
Four families exist. (1) Kalman-type filters (UKF, or an assumed-density filter with a semi-analytic solution) track time-varying NMM parameters sample by sample. (2) DCM fits spectra window by window with variational Bayes and hierarchical parametric empirical Bayes (PEB). (3) SBI trains a neural density estimator on simulations for amortized posteriors, which is fast at test time. (4) PINNs are an emerging option with only early EEG/ECoG work. For long, continuous recordings, Kalman methods and amortized SBI are the practical choices.

### Cited Findings
- **Kalman / assumed-density filtering.** Karoly et al. 2018, PLoS Comput Biol, "Seizure pathways": Jansen-Rit model fitted to NeuroVista iEEG (16 channels) with an assumed-density Kalman filter that has an exact semi-analytic solution for nonlinear propagation. The data were 12 patients and 3,010 seizures (about 250 per patient). Code: github.com/pkaroly/Data-Driven-Estimation — [PLoS CB](https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1006403); [GitHub](https://github.com/pkaroly/Data-Driven-Estimation)
- [FOUNDATIONAL] Freestone, Kuhlmann et al. (about 2013–2014) presented deterministic and stochastic online state and parameter estimation for NMMs, applied to synthetic data and real seizure ECoG — [Semantic Scholar](https://www.semanticscholar.org/paper/Patient-specific-neural-mass-modeling-stochastic-Freestone-Kuhlmann/ab5fe83ad9862006279983ce19f73d712497f8dd); [BMC Neurosci abstract, "Seizure dynamics: variability in seizure mechanisms"](https://link.springer.com/article/10.1186/1471-2202-15-S1-P152)
- A UKF was used to estimate Jansen-Rit parameters from scalp EEG ("extracranial") through a head model on synthetic data. This shows scalp-level inversion is possible in principle — [arXiv 1708.05282](https://arxiv.org/abs/1708.05282); [Frontiers 2018](https://www.frontiersin.org/articles/10.3389/fams.2018.00046/full)
- A UKF with Jansen-Rit has also tracked anesthetic brain states in human EEG, which shows the approach works on non-invasive recordings — [NeuroImage, ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1053811916002445)
- A 2025 BSPC paper, "Data fitting for the neural mass model using Unscented Kalman Filters," builds personalised NMMs for epileptic patients during seizures, calibrated on individual iEEG (from search snippet) — [ScienceDirect S1746809425008146](https://www.sciencedirect.com/science/article/abs/pii/S1746809425008146)
- **DCM.** [FOUNDATIONAL] Papadopoulou et al. 2015, NeuroImage, "Tracking slow modulations in synaptic gain using dynamic causal modelling: validation in epilepsy" — [PubMed 25498428](https://pubmed.ncbi.nlm.nih.gov/25498428/)
- Papadopoulou et al. 2017 applied DCM to kainic-acid rat hippocampal recordings. Hierarchical PEB described seizure onset as slow fluctuations in synaptic excitability. Lower deep-pyramidal synaptic time constants and lower interneuron self-inhibition were enough to explain the spectral changes — [PubMed 27639356](https://pubmed.ncbi.nlm.nih.gov/27639356); [Bristol repository](https://research-information.bris.ac.uk/en/publications/dynamic-causal-modelling-of-seizure-activity-in-a-rat-model/)
- Rosch et al. 2018, PLoS Comput Biol: whole-brain light-sheet calcium imaging in PTZ zebrafish, with DCM on neural mass models to infer changes in effective connectivity and synaptic dynamics during seizures — [PLoS CB](https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1006375); [PMC6124808](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6124808/)
- **SBI.** Hashemi et al. developed SBI-VEP, which amortizes the posterior over Epileptor-network parameters (the extent of the epileptogenic and propagation zones) from low-dimensional features of sparse SEEG. Published in Neural Networks 2023 as "Amortized Bayesian inference on generative dynamical network models of epilepsy using deep neural density estimators" — [PubMed 37060871](https://pubmed.ncbi.nlm.nih.gov/37060871/); [medRxiv](https://www.medrxiv.org/content/10.1101/2022.06.02.22275860v1)
- A review, "Simulation-based inference on virtual brain models of disorders" (Mach Learn: Sci Technol, 2024) — [IOPscience](https://iopscience.iop.org/article/10.1088/2632-2153/ad6230)
- The `sbi` package is described in "sbi reloaded: a toolkit for simulation-based inference workflows" (arXiv 2411.17337) — [arXiv](https://arxiv.org/pdf/2411.17337)
- The earlier Bayesian VEP uses MCMC/HMC to infer epileptogenicity maps. Code: github.com/ins-amu/BVEP — [GitHub BVEP](https://github.com/ins-amu/BVEP)
- **Deep learning inversion.** "Deep Learning-Based Parameter Estimation for Neurophysiological Models of Neuroimaging Data" (bioRxiv 2022) — [bioRxiv](https://www.biorxiv.org/content/10.1101/2022.05.19.492664.full.pdf)
- **PINNs.** "Estimating the Excitatory-Inhibitory Balance from Electrocorticography Data using Physics-Informed Neural Networks" (ACM ICBRA, about 2024) embeds NMM E/I equations in a PINN and fits ECoG — [ACM DL](https://dl.acm.org/doi/10.1145/3700666.3700701)
- "Physics-informed model of epileptic seizure dynamics" (about 2025) combines Kuramoto oscillators with neural ODEs for multichannel EEG seizure dynamics (from search snippet) — [PubMed 41336412](https://pubmed.ncbi.nlm.nih.gov/41336412/)

### Inferences
- A student could realistically use two inversion routes on scalp data: (a) spectral fitting of a Jansen-Rit/Wendling model per sliding window, done with UKF or amortized SBI (`sbi` NPE trained once and applied to every window in milliseconds), or (b) Karoly's semi-analytic Kalman code as a baseline.
- DCM (in SPM, MATLAB) is well validated but slow per window, and is better suited to hypothesis testing on selected epochs than to continuous forecasting.
- PINN-based EEG inversion is at conference-paper maturity. It is a novelty opportunity, but also a risk.

### Gaps
- There is no head-to-head benchmark of UKF vs DCM vs SBI parameter recovery on the same epilepsy EEG data.
- The ACM PINN paper's quantitative results and dataset could not be retrieved.

## 3. Virtual Epileptic Patient / TVB digital twins; EPINOV; 2023–2026 results

### Takeaway
The VEP (TVB plus Epileptor plus patient connectome, with Bayesian or SBI inversion on SEEG) is aimed at localising the epileptogenic zone for surgery, not at forecasting seizures in time. EPINOV is a randomised trial in France (more than 300 patients, 10 centres, launched 2018, active phase closed in November 2023). As of the sources found, only case-level results are public (EBRAINS Summit 2025). No primary efficacy results were located.

### Cited Findings
- Wang et al. 2023, Science Translational Medicine, "Delineating epileptogenic networks using brain imaging data and personalized modeling in drug-resistant epilepsy": the VEP method behind EPINOV — [Science TM](https://www.science.org/doi/10.1126/scitranslmed.abp8982); [HBP news](https://www.humanbrainproject.eu/en/follow-hbp/news/2023/01/26/personalised-brain-modeling-technique-may-lead-breakthroughs-clinical-epilepsy-trial/)
- EPINOV design: prospective, randomised, multicentre; more than 300 DRE patients across 10 French hospitals. Primary endpoints are the 1-year surgical outcome (seizure frequency) and the influence of the VEP on surgical strategy and morbidity. Launched in January 2018 for 5 years, with a closing ceremony on 8 November 2023. The page gives no efficacy results — [INS-AMU EPINOV page](https://ins-amu.fr/epinov)
- At EBRAINS Summit 2025, two case studies were presented. In one, VEP modelling suggested that a smaller, more targeted resection could have achieved seizure freedom. Background: about 40% of drug-resistant patients still have seizures after surgery (from search snippet of the summit programme) — [EBRAINS Summit 2025 news](https://summit2025.ebrains.eu/news/epinov-clinical-trial-virtual-brain-technology-to-support-surgery-in-drug-resistant-epilepsy); [Summit session "Epinov trial: impacts and lessons learned"](https://summit2025.ebrains.eu/programme/epinov-trial-impacts-and-lessons-learned)
- Related work: "Effects of the spatial resolution of the Virtual Epileptic Patient on the identification of epileptogenic networks" (Imaging Neuroscience, 2024) — [MIT Press](https://direct.mit.edu/imag/article/doi/10.1162/imag_a_00153/120596/Effects-of-the-spatial-resolution-of-the-Virtual); "High-resolution Bayesian Virtual Epileptic Patient using neural field models" — [PMC13108505](https://pmc.ncbi.nlm.nih.gov/articles/PMC13108505/); Lancet Neurology 2023 review "Personalised virtual brain models in epilepsy" — [Lancet Neurol](https://www.thelancet.com/journals/laneur/article/PIIS1474-4422(23)00008-X/abstract); 2025 review "Emerging personalized virtual brain models: next-generation resection neurosurgery for drug-resistant epilepsy?" — [PubMed 40217351](https://pubmed.ncbi.nlm.nih.gov/40217351/)
- VBI toolkit (Ziaeemehr, Woodman, Domide, Petkoski, Jirsa, Hashemi; eLife 2025): SBI on whole-brain models, supporting Wilson-Cowan, Jansen-Rit, Stuart-Landau, Epileptor, Montbrió and Wong-Wang. Features include PSD, FC, FCD and seizure-envelope onset. GPU-accelerated with CuPy/PyTorch/Numba and runs on EBRAINS — [eLife 106194](https://elifesciences.org/articles/106194); [PMC12700528](https://pmc.ncbi.nlm.nih.gov/articles/PMC12700528/)

### Inferences
- The VEP/TVB line of work answers "where," not "when." Adapting it to answer "when" (tracking x0 or coupling over hours) is largely untested.
- EPINOV's primary results could appear in 2026. The writer should say they were not found as of these notes, not that they are negative.

### Gaps
- No peer-reviewed EPINOV primary-outcome publication was found.
- No VEP/TVB study was found that uses the digital twin for temporal seizure forecasting.

## 4. Studies tracking estimated synaptic/E-I parameters drifting toward seizures, and prediction performance

### Takeaway
Fitted-NMM predictors exist and have reported clinically plausible numbers. Aarabi & He (2014) reported 75–81% sensitivity at 0.06–0.21 false predictions per hour, including scalp EEG (CHB-MIT). The best-characterised parameter trajectories (Karoly 2018) are locked to seizure onset and patient-specific. They are not long preictal drifts. Model-free E/I proxies (the aperiodic exponent) show changes in the roughly 13 minutes before seizures on hd-EEG, but these are only correlates.

### Cited Findings
- [FOUNDATIONAL, 2014] Aarabi & He, Clinical Neurophysiology 2014: 21 patients with hippocampal/neocortical epilepsy. 12 NMM parameters were fitted to iEEG PSD. Sensitivity and false prediction rate were **81% / 0.06 per h (Freiburg iEEG), 79% / 0.16 per h (CHB-MIT scalp EEG), 75% / 0.21 per h (AES Kaggle challenge)** (from search-result abstract; full text blocked) — [PubMed 24374087](https://pubmed.ncbi.nlm.nih.gov/24374087/); [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1388245713011942); companion "Neural mass modeling for predicting seizures" — [PubMed 24326320](https://pubmed.ncbi.nlm.nih.gov/24326320/)
- Karoly et al. 2018 (12 patients, 3,010 seizures): five connectivity parameters (external input to pyramidal cells, inhibitory→pyramidal, excitatory→pyramidal, pyramidal→excitatory, pyramidal→inhibitory) changed around seizures, most strongly the inputs to pyramidal cells. Trajectories were stereotyped within each patient. Onset mechanisms fell into three types: decreased, increased, or decreased-then-increased pyramidal input connectivity. Onset appeared deterministic and termination more stochastic. No forecasting metric was reported — [PLoS CB](https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1006403)
- Review: "The role of multiple-scale modelling of epilepsy in seizure forecasting" (Kuhlmann et al., J Clin Neurophysiol 2015) — [PMC4455036](https://ncbi.nlm.nih.gov/pmc/articles/PMC4455036) [FOUNDATIONAL]
- NMM parameters estimated at seizure onset have been used as features to predict seizure duration (IEEE EMBC 2023) — [PubMed 38083551](https://pubmed.ncbi.nlm.nih.gov/38083551/)
- A 2024 Neural Networks paper fitted NMMs to a tetanus-toxin rat epilepsy model to relate neural dynamics to seizures — [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0893608024006701); [bioRxiv](https://www.biorxiv.org/content/10.1101/2024.01.15.575784.full.pdf)
- Duma et al. 2025, BMC Medicine: 20 patients with focal epilepsy, 29 seizures, 128-channel hd-EEG, source-localised to 68 ROIs, with SPRiNT/specparam applied over the 13 minutes before onset. The aperiodic exponent **increased progressively** (a steeper slope, meaning a shift toward inhibition) in both epileptic and non-epileptic regions. The authors propose a compensatory inhibition that fails at the ictal threshold. **No prediction performance was reported**, and the authors say the findings are correlates, not predictors — [PMC12581463](https://pmc.ncbi.nlm.nih.gov/articles/PMC12581463/); [BMC Med](https://link.springer.com/article/10.1186/s12916-025-04447-7)
- The aperiodic exponent also indexes hyperexcitability in generalized epilepsy (2024) — [PMC11376430](https://pmc.ncbi.nlm.nih.gov/articles/PMC11376430/); circadian aperiodic changes correlate with RNS response in mesial TLE — [PMC11138949](https://pmc.ncbi.nlm.nih.gov/articles/PMC11138949/)

### Inferences
- Duma 2025 found a preictal shift toward inhibition, which conflicts with the naive "rising excitation" story. This is a scientifically interesting tension that a model-based E/I estimate (A/B or A/G fitted by SBI) could test directly.
- Aarabi & He's scalp-EEG result on CHB-MIT suggests NMM features can carry preictal information non-invasively. The 2014 evaluation predates current strict forecasting standards (pseudo-prospective splits, comparison with chance), so it would need re-evaluation.

### Gaps
- No 2018–2026 study was found that reports prospective forecasting performance (AUC, time-in-warning) using fitted NMM parameters.
- No study was found that tracks fitted synaptic parameters over hours to days before seizures (as opposed to minutes, or onset-locked windows).

## 5. Hybrid approaches: deep learning with biophysical models, neural ODEs, latent dynamics (LFADS, CEBRA)

### Takeaway
The most mature hybrid is simulation-trained deep learning. DeepSIF trains a network on modified Jansen-Rit simulations to image seizure sources from scalp EEG. Neural-ODE seizure detectors exist but are black-box. No LFADS or CEBRA application to human epilepsy EEG was found.

### Cited Findings
- Sun, Sohrabpour, Joseph, Worrell & He 2024, Advanced Science: DeepSIF is trained on modified Jansen-Rit simulations, which produce 5 ictal signal types. On 76-channel hd-EEG from 33 patients with drug-resistant focal epilepsy it achieved spatial specificity of 96%, 10.9 ± 10.1 mm distance to the SOZ, and temporal correlation of 0.81 with EEG. Code: github.com/bfinl/DeepSIF — [PMC11653641](https://pmc.ncbi.nlm.nih.gov/articles/PMC11653641/); [GitHub](https://github.com/bfinl/DeepSIF)
- A neural-ODE-enhanced epilepsy detector reports 98.2% average accuracy on public datasets and about 30% lower latency than CNN/LSTM (a detection task, not prediction; journal quality unclear) — [ScienceDirect](https://www.sciencedirect.com/org/science/article/pii/S1526149225001699)
- Kuramoto combined with neural ODE in a physics-informed model of seizure dynamics — [PubMed 41336412](https://pubmed.ncbi.nlm.nih.gov/41336412/)
- "BrainDyn: A Sheaf Neural ODE for Generative Brain Dynamics" (arXiv 2026) — [arXiv 2605.19324](https://arxiv.org/pdf/2605.19324)
- A new NMM-driven method for early seizure detection (2022) — [PMC9371613](https://pmc.ncbi.nlm.nih.gov/articles/PMC9371613/)

### Inferences
- A natural hybrid is to feed fitted NMM parameter trajectories (A, B, G, time constants) together with specparam features into a small sequence model, and compare against a pure-DL baseline. This keeps the model interpretable while testing whether the biophysics adds information.

### Gaps
- No peer-reviewed LFADS or CEBRA application to human seizure EEG or iEEG was found in this search. This is either a real gap or a search limitation.

## 6. Practical tooling, compute cost, and applicability to scalp EEG (TUSZ)

### Takeaway
The whole pipeline can be built in Python: MNE for I/O and preprocessing, specparam/SPRiNT for aperiodic E/I proxies, a Jansen-Rit/Wendling simulator (neurolib, TVB, or a custom NumPy/Numba implementation), and `sbi` or VBI for inversion. Amortized SBI on a single neural mass is cheap: minutes to about an hour of training on one GPU. TUSZ is scalp EEG at 250 Hz, 10-20 montage, with seizure-type labels, but no one appears to have fitted NMMs to it.

### Cited Findings
- VBI (eLife 2025) compute benchmarks: Jansen-Rit with 50k simulations took about 45 min to train. Epileptor with 10k simulations took under 1 min to generate and about 13 min to train. Wilson-Cowan with 260k simulations took about 2 h. Montbrió with 500k simulations took about 10 h. Posterior sampling takes seconds, and MAF trains 2–4× faster than NSF — [eLife 106194](https://elifesciences.org/articles/106194)
- neurolib (Cakan, Jajcay & Obermayer, Cognitive Computation 2021): Python whole-brain NMM framework with parallel parameter exploration and evolutionary-algorithm fitting, MIT license — [Springer](https://link.springer.com/article/10.1007/s12559-021-09931-9); [GitHub](https://github.com/neurolib-dev/neurolib)
- `sbi` toolkit — [arXiv 2411.17337](https://arxiv.org/pdf/2411.17337)
- BVEP (TVB/Epileptor Bayesian VEP) — [GitHub ins-amu/BVEP](https://github.com/ins-amu/BVEP)
- Karoly Kalman NMM estimation code — [GitHub pkaroly/Data-Driven-Estimation](https://github.com/pkaroly/Data-Driven-Estimation)
- DeepSIF (Jansen-Rit-trained source imaging) — [GitHub bfinl/DeepSIF](https://github.com/bfinl/DeepSIF)
- SPRiNT/specparam was used for time-resolved aperiodic E/I proxies on hd-EEG — [PMC12581463](https://pmc.ncbi.nlm.nih.gov/articles/PMC12581463/)
- TUSZ: 315 subjects and 822 sessions in an early release. Standard 10-20 channels at 250 Hz. Seizure subtypes include FNSZ, SPSZ, CPSZ, GNSZ, TCSZ, ABSZ, MYSZ and TNSZ — [Shah et al., Front Neuroinform 2018](https://www.frontiersin.org/journals/neuroinformatics/articles/10.3389/fninf.2018.00083/full); [arXiv 1801.08085](https://arxiv.org/pdf/1801.08085); [seizure-type review](https://www.sciencedirect.com/science/article/pii/S0957417423015427)
- Scalp-level NMM inversion is feasible in simulation (UKF with a head model) — [arXiv 1708.05282](https://arxiv.org/abs/1708.05282). NMM-based features worked on CHB-MIT scalp EEG — [PubMed 24374087](https://pubmed.ncbi.nlm.nih.gov/24374087/)

### Inferences
- Rough budget for a single-channel or single-source Jansen-Rit/Wendling SBI: 50k–100k simulations of a few seconds each, trained on one consumer GPU in under 1–2 h based on the VBI numbers. After that, inference is effectively free per window, so thousands of TUSZ windows can be processed on a laptop.
- TUSZ recordings are mostly short clinical EEGs, often under 1 h, with few long preictal stretches. That suits seizure-type-specific *onset/peri-ictal* E/I trajectories better than long-horizon forecasting. Genuine forecasting needs long recordings such as CHB-MIT, Siena, Freiburg or EPILEPSIAE, or NeuroVista-like iEEG.
- Scalp volume conduction blurs sources, so the student should either fit per-channel "effective" NMMs and treat the parameters as lumped proxies, or first source-localise (MNE) to ROIs as Duma 2025 did.

### Gaps
- No compute benchmarks were found for UKF or DCM on long continuous EEG.
- No published work was found that fits NMMs to TUSZ.

## 7. What remains unaddressed: feasible 4–6 month student projects

### Takeaway
There is a clear open niche: amortized SBI fits of Wendling/Jansen-Rit models to scalp EEG, used to extract seizure-type-specific E/I parameter trajectories and tested as preictal features under modern evaluation. The pieces exist (VBI/sbi, neurolib, MNE, specparam, public datasets), but no one appears to have combined them this way.

### Cited Findings (evidence of the gaps)
- The fitted-NMM prediction evidence is old (2014) and not evaluated pseudo-prospectively — [PubMed 24374087](https://pubmed.ncbi.nlm.nih.gov/24374087/)
- Seizure pathways differ by patient and by mechanism (3 onset types), which motivates stratified analysis — [Karoly 2018](https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1006403)
- The aperiodic preictal shift toward inhibition has no prediction metrics reported — [Duma 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12581463/)
- NMM parameter identifiability is an open issue — [Phys Rev E 2024](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.110.044208)
- SBI on virtual brain models has focused on spatial EZ inference, not temporal forecasting — [Hashemi 2023](https://pubmed.ncbi.nlm.nih.gov/37060871/); [VBI](https://elifesciences.org/articles/106194)

### Inferences (candidate projects)
1. **Per-seizure-type E/I trajectories on TUSZ.** Train an NPE (with `sbi`) on Wendling-model PSDs, with priors over A, B, G and time constants. Apply it to 2–4 s windows around each TUSZ seizure. Compare posterior trajectories of A/B and A/G across FNSZ, GNSZ, ABSZ and TCSZ. Scale is feasible on a single GPU.
2. **SBI-based preictal detection.** On CHB-MIT or Siena (long scalp recordings), use posterior means and uncertainties as features. Evaluate with pseudo-prospective splits, time-in-warning, and comparison with a chance predictor, against specparam-only and raw-DL baselines. This is a direct modern re-test of Aarabi & He 2014.
3. **Reconcile the model and aperiodic E/I proxies.** Test whether the specparam exponent's preictal increase (Duma 2025) matches a rise in fitted inhibitory gain or a change in time constants. This connects a phenomenological marker to a mechanism.
4. **Identifiability audit on scalp EEG.** Use sensitivity analysis and posterior-contraction tests to find which Wendling parameters are recoverable from 19-channel, 250 Hz data. This is a useful negative/positive result in its own right.
5. **Replicate Karoly's pathways on scalp EEG.** Run the open Kalman code, or SBI, on long-term scalp recordings to see whether patient-specific onset pathways appear non-invasively.

### Gaps
- Whether scalp-derived NMM parameters are stable enough across sessions and montages to support forecasting is unknown.
- Seizure-type labels in TUSZ are clinical annotations and may be noisy. How much they reflect distinct mechanisms is not established in the sources reviewed.
