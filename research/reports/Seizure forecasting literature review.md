# Fair evaluation shrinks every seizure-forecasting headline

**Main finding: when tests use new, unseen patients and count whole seizures, almost every impressive number in this field becomes much smaller. On TUSZ, nobody has yet reported honest, alarm-level seizure prediction or causal onset latency.** We reviewed 47 papers in six areas. Here is what the fair baselines look like. For prediction, the only TUSZ benchmark (MLSPred-Bench, 2025) reports only a **segment-level validation AUC of about 0.71–0.75**. Honest cross-patient prediction on other scalp datasets reaches **AUC 0.69–0.82**, and the best event-level result gives about **23 minutes of warning at 0.32 false alarms per hour**, but that result is a preprint. For detection, the best TUSZ event F1 is **0.671** (SeizureTransformer, also a preprint), and the only patient-independent latency on TUSZ is **7.8–15.8 s mean onset latency** (Lee 2022). For seizure type, fair patient-wise evaluation gives a **weighted F1 of about 0.75 for 4 classes and 0.62–0.65 for 7 classes**. The 0.90–0.98 values in some papers come from leaky splits. Spread across brain regions has never been validated with numbers on scalp EEG. The best localization results are "hemisphere and lobe correct in 21 of 34 patients" (SZTrack) and **about 8–11 mm onset-zone error** using 76-channel EEG (DeepSIF). Neural-mass-model (NMM) E/I estimation works on intracranial EEG, but no paper tests it before seizures on scalp EEG. The only scalp E/I study found a preictal shift toward **inhibition**, not excitation. No paper uses the ECG channel inside TUSZ. For NeuroMech-Warn this means one thing: the main contribution does not have to be a new architecture. It can be the first **fair, causal, event-level, type-stratified** measurement on TUSZ, with each extra module (type, spread, body, E/I model) scored against the small set of honest baselines listed below.

**How to read this report.** "(abs)" means the number comes only from the abstract or a search summary, because we could not read the full text. "(PREPRINT)" means the paper is not peer-reviewed. Each paper ID links to our local summary file. Web links in brackets go to the original source.

## Key terms in plain words

| Term | Simple meaning |
|---|---|
| **Prediction / forecasting** | Warning *before* the seizure starts (minutes to days ahead). |
| **Detection** | Recognizing a seizure *after* it has started. "Early detection" means doing this in as few seconds as possible. |
| **Onset latency** | Seconds from the expert-marked seizure start to the first alarm. This is different from computer processing time. |
| **Preictal / interictal / ictal / postictal** | The period before a seizure / the period far from seizures / during the seizure / just after it. |
| **SPH (seizure prediction horizon)** | Conventional meaning: the gap between the alarm and the start of the window in which the seizure is expected. |
| **SOP (seizure occurrence period)** | Conventional meaning: the window in which the seizure must happen for the alarm to count as correct. |
| **Patient-independent / cross-patient / LOPO** | The test patients are never used in training. LOPO = leave-one-patient-out. This is the fair setting. |
| **Pooled / segment-shuffled split** | Windows from the same patient appear in both training and test sets. This causes leakage and inflates scores. |
| **Leave-one-seizure-out** | Train on all seizures of one patient except one, then test on that one. The model sees the same patient and even *future* seizures. |
| **Segment-level vs event-level metrics** | Scoring every small window vs scoring each whole seizure (found or missed) and each false alarm. Only event-level metrics describe a real alarm system. |
| **FPR/h, FA/24h** | False alarms per hour or per day. |
| **Causal model** | A model that uses only past and present EEG, never future samples, so it can run live. |
| **wF1 (weighted F1)** | F1 averaged over classes, weighted by class size. Used for seizure-type classification. |
| **AUROC / AUPRC** | Area under the ROC or precision–recall curve. Threshold-free scores (1.0 = perfect, 0.5 = chance for AUROC). |
| **SOZ** | Seizure onset zone: the brain area where the seizure starts. |
| **NMM (neural mass model)** | A small mathematical model of a population of excitatory and inhibitory neurons (for example Jansen–Rit or Wendling). Its parameters act as E/I (excitation/inhibition) gains. |
| **CSD (critical slowing down)** | The idea that a system close to a sudden change recovers more slowly, so variance and autocorrelation rise. |
| **Foundation model (FM)** | A large network pretrained without labels on thousands of hours of EEG, then fine-tuned for a task. |
| **TUSZ / TUEG / TUAB / TUEV** | Temple University Hospital datasets: seizure corpus / whole EEG archive / abnormal-vs-normal / EEG events. |

## Index of all 47 papers reviewed

Topic codes: **P** = prediction, **D** = detection and latency, **C** = type classification and spread, **N** = neuroscience/biophysical forecasting, **F** = foundation models, **B** = body/multimodal. Of the 47 files, 36 are journal papers, 9 are conference papers and 2 are preprints. Two files also cover a companion preprint.

| ID / file | Authors | Year | Venue | Type | Topic |
|---|---|---|---|---|---|
| [P_2018_Kuhlmann](../papers/P_2018_Kuhlmann_Epilepsyecosystem_crowdsourcing.md) | Kuhlmann, Karoly, Freestone, Brinkmann et al. | 2018 | *Brain* | Journal | Crowd-sourced iEEG prediction; evaluation standard |
| [P_2018_Truong](../papers/P_2018_Truong_CNN_seizure_prediction.md) | Truong, Nguyen, Kuhlmann, … Kavehei | 2018 | *Neural Networks* | Journal | STFT-CNN patient-specific prediction (CHB-MIT, Freiburg, Kaggle) |
| [P_2022_Dissanayake](../papers/P_2022_Dissanayake_GDL_subject_independent_prediction.md) | Dissanayake, Fernando, Denman, Sridharan, Fookes | 2022 | IEEE JBHI | Journal | GNN "subject-independent" prediction (pooled CV) |
| [P_2024_Jemal](../papers/P_2024_Jemal_domain_adaptation_cross_subject_prediction.md) | Jemal, Abou-Abbas, Henni, Mitiche, Mezghani | 2024 | *Front. Neuroinform.* | Journal | Pooled vs LOPO vs domain adaptation |
| [P_2024_Koutsouvelis](../papers/P_2024_Koutsouvelis_preictal_period_optimization.md) | Koutsouvelis, Chybowski, Gonzalez-Sulser, Abdullateef, Escudero | 2024 | *J. Neural Eng.* | Journal | Per-patient optimal preictal period |
| [P_2025_Meng](../papers/P_2025_Meng_3D-SERESNet_multi_patient_prediction.md) | Meng, Zhou, Zhang, Xie | 2025 | *iScience* | Journal | 3D-SERESNet, event-level, multi-patient |
| [P_2025_Mohammad](../papers/P_2025_Mohammad_MLSPred-Bench_TUSZ_prediction_benchmark.md) | Mohammad, Saeed | 2025 | *MethodsX* (bioRxiv 2024) | Journal | **Only TUSZ prediction benchmark** (MLSPred-Bench) |
| [P_2026_Chen](../papers/P_2026_Chen_CG-MambaNet_cross_patient_prediction_PREPRINT.md) | Chen, Wu, Huang, … Ren | 2026 | arXiv 2606.08226 | **Preprint** | CG-MambaNet, LOPO, event-level lead time |
| [D_2018_Shah](../papers/D_2018_Shah_TUSZ_corpus.md) | Shah, von Weltin, Lopez, … Obeid, Picone | 2018 | *Front. Neuroinform.* | Journal | TUSZ corpus paper |
| [D_2020_Saab](../papers/D_2020_Saab_weak_supervision_seizure_detection.md) | Saab, Dunnmon, Ré, Rubin, Lee-Messer | 2020 | *npj Digit. Med.* | Journal | Weak supervision; 12 s vs 60 s clips |
| [D_2022_Lee](../papers/D_2022_Lee_realtime_seizure_detection.md) | Lee, Jeong, Kim, Yang, Kang, Choi | 2022 | CHIL (PMLR 174) | Conference | Real-time TUSZ detection; onset latency |
| [D_2023_Xu](../papers/D_2023_Xu_shorter_latency_probabilistic_prediction.md) | Xu, Yang, Ming, Wang, Sawan | 2023/24 | *Expert Syst. Appl.* | Journal | Soft labels + accumulative alarm; short latency |
| [D_2025_Dan](../papers/D_2025_Dan_SzCORE_framework_and_challenge.md) | Dan, Pale, … Ryvlin (+ challenge report) | 2025 | *Epilepsia* (+ arXiv 2505.18191) | Journal (+ **preprint** challenge report) | SzCORE scoring standard; 2025 challenge |
| [D_2025_Wu](../papers/D_2025_Wu_SeizureTransformer_EEG_U_Transformer.md) | Wu, Zhao, Yener | 2025 | arXiv 2504.00336 | **Preprint** | SeizureTransformer; best TUSZ event F1 |
| [D_2026_Zabihi](../papers/D_2026_Zabihi_TUSZ_CatBoost_benchmark.md) | Zabihi, Gilmore, Ding, Rosenthal | 2026 | *Sci. Rep.* | Journal | Transparent TUSZ benchmark; CatBoost |
| [C_2020_AhmedtAristizabal](../papers/C_2020_AhmedtAristizabal_neural_memory_networks.md) | Ahmedt-Aristizabal, Fernando, Denman, Petersson, Aburn, Fookes | 2020 | IEEE EMBC | Conference | Memory-network type classification (leaky split) |
| [C_2020_Asif](../papers/C_2020_Asif_SeizureNet.md) | Asif, Roy, Tang, Harrer (+ Roy et al. 2019) | 2020 | MICCAI workshop, LNCS (+ arXiv 1902.01012) | Conference (+ **preprint** benchmark) | SeizureNet; seizure-wise vs patient-wise |
| [C_2020_Raghu](../papers/C_2020_Raghu_CNN_transfer_learning.md) | Raghu, Sriraam, Temel, Rao, Kubben | 2020 | *Neural Networks* | Journal | ImageNet-CNN transfer for type (abs) |
| [C_2021_Li](../papers/C_2021_Li_neural_fragility_SOZ.md) | Li, Huynh, … Sarma | 2021 | *Nature Neuroscience* | Journal | Neural fragility SOZ marker (iEEG) |
| [C_2022_Craley](../papers/C_2022_Craley_SZTrack_seizure_tracking.md) | Craley, Jouny, Johnson, … Venkataraman | 2022 | *PLoS ONE* | Journal | SZTrack: spread tracking + onset localization |
| [C_2022_Sun_PNAS](../papers/C_2022_Sun_DeepSIF_PNAS.md) | Sun, Sohrabpour, Worrell, He | 2022 | *PNAS* | Journal | DeepSIF: NMM-trained source imaging |
| [C_2022_Tang](../papers/C_2022_Tang_self_supervised_GNN.md) | Tang, Dunnmon, Saab, … Lee-Messer | 2022 | ICLR | Conference | Self-supervised GNN; type + localization |
| [C_2024_Sun_AdvSci](../papers/C_2024_Sun_DeepSIF_ictal_AdvSci.md) | Sun, Sohrabpour, Joseph, Worrell, He | 2024 | *Advanced Science* | Journal | Ictal DeepSIF source imaging |
| [N_2014_Aarabi_He](../papers/N_2014_Aarabi_He_model_based_prediction.md) | Aarabi, He | 2014 | *Clin. Neurophysiol.* | Journal | NMM-parameter prediction on iEEG (abs) |
| [N_2018_Baud](../papers/N_2018_Baud_multidien_rhythms.md) | Baud, Kleen, … Rao | 2018 | *Nat. Commun.* | Journal | Multi-day seizure-risk cycles |
| [N_2018_Chang](../papers/N_2018_Chang_network_resilience.md) | Chang, Kudlacek, Hlinka, … Jiruska | 2018 | *Nature Neuroscience* | Journal | Loss of resilience / CSD |
| [N_2018_Karoly](../papers/N_2018_Karoly_seizure_pathways_JansenRit.md) | Karoly, Kuhlmann, Soudry, Grayden, Cook, Freestone | 2018 | *PLoS Comput. Biol.* | Journal | Jansen–Rit parameter tracking (Kalman) |
| [N_2020_Maturana](../papers/N_2020_Maturana_critical_slowing.md) | Maturana, Meisel, … Freestone | 2020 | *Nat. Commun.* | Journal | CSD biomarker forecasting |
| [N_2021_Proix](../papers/N_2021_Proix_forecasting_seizure_risk.md) | Proix, Truccolo, Leguia, … Baud | 2021 | *Lancet Neurol.* | Journal | Cycle-based forecasting, 175 patients |
| [N_2024_Khambhati](../papers/N_2024_Khambhati_hippocampal_connectivity.md) | Khambhati, Chang, Baud, Rao | 2024 | *Nature Medicine* | Journal | 90-s connectivity forecasting (abs) |
| [N_2025_Duma](../papers/N_2025_Duma_aperiodic_EI_balance.md) | Duma, Cuozzo, … Bonanni, Pellegrino | 2025 | *BMC Medicine* | Journal | Scalp aperiodic exponent (E/I) before seizures |
| [N_foundational](../papers/N_foundational_Wendling2002_Jirsa2014_models.md) | Wendling et al.; Jirsa et al. | 2002; 2014 | *Eur. J. Neurosci.*; *Brain* | Journal | Wendling NMM; Epileptor |
| [F_2021_Kostas](../papers/F_2021_Kostas_BENDR.md) | Kostas, Aroca-Ouellette, Rudzicz | 2021 | *Front. Hum. Neurosci.* | Journal | BENDR foundation model |
| [F_2023_Yang](../papers/F_2023_Yang_BIOT.md) | Yang, Westover, Sun | 2023 | NeurIPS | Conference | BIOT biosignal transformer |
| [F_2024_Jiang](../papers/F_2024_Jiang_LaBraM.md) | Jiang, Zhao, Lu | 2024 | ICLR | Conference | LaBraM |
| [F_2024_Wang_EEGPT](../papers/F_2024_Wang_EEGPT.md) | Wang, Liu, He, Xu, Ma, Li | 2024 | NeurIPS | Conference | EEGPT (no TUH pretraining) |
| [F_2025_Kastrati](../papers/F_2025_Kastrati_EEG-Bench.md) | Kastrati, Bürki, Lauer, Xuan, Iaquinto, Wattenhofer | 2025 | NeurIPS (likely workshop) | Conference | EEG-Bench clinical FM benchmark |
| [F_2025_Wang_CBraMod](../papers/F_2025_Wang_CBraMod.md) | Wang, Zhao, Luo, … Pan | 2025 | ICLR | Conference | CBraMod |
| [F_2026_Liu](../papers/F_2026_Liu_EEG-FM-Compass.md) | Liu, Chen, … Wu | 2026 | *National Science Review* | Journal | EEG-FM-Compass review + benchmark |
| [B_2003_Leutmezer](../papers/B_2003_Leutmezer_ECG_onset_tachycardia.md) | Leutmezer, Schernthaner, Lurger, Pötzelberger, Baumgartner | 2003 | *Epilepsia* | Journal | Heart rate at seizure onset (abs) |
| [B_2014_Kato](../papers/B_2014_Kato_right_left_tachycardia_timing.md) | Kato, Jin, … Nakasato | 2014 | *Neurology* | Journal | Right vs left tachycardia timing (abs) |
| [B_2019_Jeppesen](../papers/B_2019_Jeppesen_HRV_wearable_ECG_detection.md) | Jeppesen, Fuglsang-Frederiksen, … Beniczky | 2019 | *Epilepsia* | Journal | HRV wearable ECG detection, phase 2 (abs) |
| [B_2019_Regalia](../papers/B_2019_Regalia_Empatica_multimodal_wristband.md) | Regalia, Onorati, Lai, Caborni, Picard (+ Onorati et al. 2021) | 2019 (+2021) | *Epilepsy Res.* (+ *Front. Neurol.*) | Journal | Wrist EDA + accelerometry |
| [B_2021_Stirling](../papers/B_2021_Stirling_wearable_forecasting_Fitbit.md) | Stirling, Grayden, … Karoly | 2021 | *Front. Neurol.* | Journal | Smartwatch forecasting (abs) |
| [B_2022_Karacsony](../papers/B_2022_Karacsony_3D_video_semiology_classification.md) | Karácsony, Loesch-Biffar, Vollmar, Rémi, Noachtar, Cunha | 2022 | *Sci. Rep.* | Journal | 3D video semiology classification |
| [B_2025_Jeppesen](../papers/B_2025_Jeppesen_phase3_wearable_ECG_smartphone.md) | Jeppesen, Christensen, Ahrenfeldt Petersen et al. | 2025 | *eBioMedicine* | Journal | Phase 3 real-time ECG detection |
| [B_2026_Swinnen](../papers/B_2026_Swinnen_SeizeIT2_bte_EEG_ECG.md) | Swinnen, Bhagubai, … Van Paesschen | 2026 | *Epilepsia Open* | Journal | SeizeIT2 behind-ear EEG + ECG (abs) |

## Prediction on scalp EEG: honest numbers fall from 97% to AUC 0.7

### What the papers did

Eight prediction papers form a clear ladder, from the least strict evaluation to the most strict. At the top of the ladder, **Kuhlmann 2018** (crowd-sourced Kaggle contest on NeuroVista implant EEG) and **Truong 2018** (a short-time-Fourier-transform CNN, one model per patient) set the evaluation rules still used today. These rules are: test on data separated in time, score whole seizures with SPH/SOP windows, and compare against a random predictor. Truong reached **81.2% sensitivity at 0.16 false alarms per hour on 13 CHB-MIT patients**, better than chance in 12 of 13 patients, with SOP 30 min and SPH 5 min ([arXiv](https://arxiv.org/pdf/1707.01976)). Kuhlmann's top contest AUC was **0.81**, and it dropped only 6.7% on a larger held-out set (abs) ([Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1093/brain/awy210&resultType=core&format=json)). Hand-crafted features with tree ensembles were among the winners.

Three later papers report very high numbers under protocols that let the same patient appear in training and test. **Dissanayake 2022** calls its graph neural network "subject-independent", but it uses 10-fold cross-validation on pooled segments with 50%-overlapping windows. This gives **95.38% accuracy (CHB-MIT) and 96.05% (Siena)** ([QUT PDF](https://eprints.qut.edu.au/212250/1/88918403.pdf)). **Koutsouvelis 2024** reports **sensitivity 99.31% and AUC 0.9935** and a "prediction time" of **76.8 min**. However, the false-alarm rate is **33.6 per hour** because it is counted per 5-s segment. The 76.8 min is the time at which the smoothed model output converges, not the time of a real alarm ([arXiv](https://arxiv.org/html/2407.14876)). **Meng 2025** is careful about event-level alarms (8-of-10 rule, 30-min refractory period, chance test). Its "patient-independent" model, however, is trained on the other seizures of *all* patients, including the test patient. It reaches **84.41% sensitivity at 0.232/h** ([Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12723167/fullTextXML)).

Only two papers test on truly unseen patients. **Jemal 2024** ran the same small CNN three ways. It gave **97.36% accuracy when pooled** but only **63.5% accuracy (AUC 0.69) with leave-one-patient-out on CHB-MIT**, and **AUC 0.48 (chance level) on Siena**. Unsupervised domain adaptation, which uses unlabelled EEG of the new patient, raised AUC to **0.75 / 0.61** ([Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10869477/fullTextXML)). **CG-MambaNet 2026 (PREPRINT)** combines a CNN, a learnable graph, Mamba and a BiLSTM. It reports **LOPO AUC 0.815 (CHB-MIT) and 0.710 (Siena)**, an **event false-alarm rate of 0.32/h** and a **mean warning time of 23.4 min** ([arXiv](https://arxiv.org/html/2606.08226v1)). Its window-level false-alarm rate before smoothing was **112.4/h**. This shows that the alarm logic, not the classifier alone, controls false alarms.

**MLSPred-Bench 2025** is the only paper that turns TUSZ into a prediction benchmark. It uses the official patient-disjoint split (208/45/34 seizure patients for train/validation/test), 5-s windows and 12 horizon settings. It reports only **segment-level AUC on the validation set**, with no test-set and no alarm-level numbers ([Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12423417/fullTextXML)). Be careful: this paper swaps the usual names. Its "SPH" is the preictal window and its "SOP" is the gap before onset.

### Results comparison

| Paper | Data | Split (fair?) | Window setting (conventional naming) | Key numbers | Warning time |
|---|---|---|---|---|---|
| [Kuhlmann 2018](../papers/P_2018_Kuhlmann_Epilepsyecosystem_crowdsourcing.md) | NeuroVista iEEG, 3 pts | Patient-specific, time-separated held-out | 1 h preictal as 10-min clips | AUC **0.81**; −6.7% on held-out; sensitivity 1.9× the original trial (abs) | Matched time-in-warning |
| [Truong 2018](../papers/P_2018_Truong_CNN_seizure_prediction.md) | CHB-MIT 13 pts / 64 sz; Freiburg; Kaggle | Patient-specific, leave-one-seizure-out | SOP 30 / SPH 5 | CHB-MIT **81.2%, 0.16/h**; Freiburg 81.4%, 0.06/h; Kaggle 75%, 0.21/h | 5–35 min window |
| [Dissanayake 2022](../papers/P_2022_Dissanayake_GDL_subject_independent_prediction.md) | CHB-MIT 23, Siena 15 | **Pooled 10-fold CV (leaky)** | 1 h preictal, no SPH/SOP | Acc 95.38% / 96.05% | Not reported |
| [Jemal 2024](../papers/P_2024_Jemal_domain_adaptation_cross_subject_prediction.md) | CHB-MIT 22, Siena 12 | Pooled vs **true LOPO** | 1 h preictal, 10-s windows | Pooled acc 97.36%; **LOPO AUC 0.69 / 0.48**; with DA **0.75 / 0.61** | Not reported |
| [Koutsouvelis 2024](../papers/P_2024_Koutsouvelis_preictal_period_optimization.md) | CHB-MIT 19 cases | Leave-one-seizure-out (uses future seizures) | Preictal 15–60 min per patient | Sens 99.31%, AUC 0.9935, **segment FAR 33.6/h** | "SPC" 76.8 ± 36.8 min (not an alarm) |
| [Meng 2025](../papers/P_2025_Meng_3D-SERESNet_multi_patient_prediction.md) | CHB-MIT 13 | Patient-specific; "multi-patient" includes test patient | SOP 30 / SPH 5 | PS **90.77%, 0.090/h**, AUC 0.923; multi-patient **84.41%, 0.232/h**, AUC 0.866 | 5–35 min window |
| [MLSPred-Bench 2025](../papers/P_2025_Mohammad_MLSPred-Bench_TUSZ_prediction_benchmark.md) | **TUSZ**, 287 pts with seizures | **Official patient-disjoint**, validation only | Preictal 2–30 min × gap 1–5 min | Mean val AUC: ResNet raw **0.709**, RF features **0.748**; best 15-min 0.836; 30/2 RF 0.884 (unstable: 0.633–0.639 at 30/1 and 30/5) | Not reported |
| [CG-MambaNet 2026](../papers/P_2026_Chen_CG-MambaNet_cross_patient_prediction_PREPRINT.md) **(PREPRINT)** | CHB-MIT 22, Siena 6 | **LOPO × 5 seeds** | 30-min preictal, no SPH | AUC **0.815 / 0.710**; event FPR **0.32 / 0.55 /h**; segment sens 74.3% | Mean lead **23.4 / 21.7 min** |

### What we learn

The same kind of model loses about 35 accuracy points when the split changes from pooled to leave-one-patient-out. Only the last two rows of the table can be compared with a patient-independent TUSZ project. A 2024 systematic review found that only **about 4% of prediction papers (21 articles) used cross-patient validation** (abs) ([IOP](https://iopscience.iop.org/article/10.1088/1741-2552/ad9682)). A 2026 review of 17 scalp-EEG prediction studies (outside our 47-paper set) found that **none used TUSZ and none had a low risk of bias** ([Alasade 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC13318060/)). There is also no agreed definition of "warning time". Each paper uses a different one: SOP window, output convergence, or mean onset-minus-alarm. TUSZ adds a data problem: its sessions are short, so fewer seizures qualify as the horizon grows. MLSPred-Bench has **1,282 seizures at a 3-min total horizon** and fewer at 35 min, and its longest horizon is 30 + 5 min ([Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12423417/fullTextXML)).

## Detection and latency: accuracy is high, but "how early?" is not measured

### What the papers did

**Shah 2018** introduced TUSZ (v1.2.0: 315 patients, 504 hours, about 36 hours of seizures, with a patient-disjoint train/eval split and a seizure-enriched eval set) ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6246677/)). **Saab 2020** trained a CNN with weak labels from routine clinical work. Short clips were much worse than long clips: adult F1 was **0.49 with 12-s clips vs 0.76 with 60-s clips**. Pretraining on outside data and then fine-tuning on TUSZ added about **10 AUROC points** ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7170880/)). **Lee 2022** is the only paper that measures patient-independent onset latency on TUSZ. It streams 4-s windows every 1 s through 15 architectures, and it shows that the scoring method changes everything. The same CNN2D+LSTM gets **sensitivity 0.75 at 47.06 FA/24h under any-overlap (OVLP) scoring**, but **0.33 at 1.03 FA/24h under time-aligned (TAES) scoring**. Mean onset latency is **10.55 s** for that model and **7.76–15.83 s** for the best models ([PMLR](https://proceedings.mlr.press/v174/lee22a/lee22a.pdf)). Its test set has only 26 patients taken from the dev split.

**Xu 2023** gives "soft" labels to windows that cross the seizure onset and uses an accumulative decision rule. It reaches **2.3 ± 0.7 s latency on CHB-MIT and 4.7 ± 2.0 s on SWEC-ETHZ at about 0.08 false detections per hour**, but with one model per patient ([arXiv](https://arxiv.org/html/2301.03465)). **SzCORE (Dan 2025)** is now the standard scoring framework. It uses event scoring with a **30-s tolerance before onset and 60-s after offset**, and **it has no latency metric** ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12489712/)). In the related 2025 challenge (PREPRINT report), algorithms trained on public data were tested on 4,360 hours of private hospital EEG. The top F1 was **43% or 32%**, because two versions of the abstract disagree (abs) ([arXiv](https://arxiv.org/abs/2505.18191); [EPFL](https://infoscience.epfl.ch/entities/publication/b5991dd8-dff4-490f-a449-f314b679c0d9)). **SeizureTransformer (PREPRINT)**, a U-Net plus transformer with one output per time step and 60-s windows, holds the best TUSZ v2.0.3 eval event F1 of **0.671 (sensitivity 0.717, precision 0.631)**. It falls to **0.43 on the unseen Dianalund site** ([arXiv](https://arxiv.org/html/2504.00336)). **Zabihi 2026** is an honest benchmark with CatBoost on hand-crafted features, the official split, and thresholds frozen on dev. It reports **event sensitivity 0.75 at 0.68 FA/h (about 16.4/24h) and window AUROC 0.92**. It detects only **33% of short (30–90 s) focal seizures**. Its "0 s median latency" comes from ±30 s dilation of the predicted intervals, not from real early detection ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13049040/)).

### Results comparison

| Paper | Data / split | Window, model | Scoring | Sens. | False alarms | F1 | Latency |
|---|---|---|---|---|---|---|---|
| [Shah 2018](../papers/D_2018_Shah_TUSZ_corpus.md) | TUSZ v1.2.0; 265 train / 50 eval pts | Corpus only | – | – | – | – | – |
| [Saab 2020](../papers/D_2020_Saab_weak_supervision_seizure_detection.md) | Stanford + TUSZ v1.4 official split | 12 s / 60 s clips; Inception CNN | Clip AUROC, F1 | – | Per clip only | 0.49–0.77 (Stanford) | Clip length only |
| [Lee 2022](../papers/D_2022_Lee_realtime_seizure_detection.md) | TUSZ v1.5.2; 26 test pts from dev | 4 s / 1 s stream; CNN/ResNet + LSTM | OVLP / TAES / MARGIN | 0.75 (OVLP); 0.33 (TAES) | 47.06 / 1.03 per 24h | – | **7.76–15.83 s mean** |
| [Xu 2023](../papers/D_2023_Xu_shorter_latency_probabilistic_prediction.md) | CHB-MIT, SWEC-ETHZ; **patient-specific** | 5–10 s; STFT + 3D-CNN, soft labels | Per seizure | 94/99 during onset crossing | 0.08/h | – | **2.3 s** / 4.7 s |
| [SzCORE, Dan 2025](../papers/D_2025_Dan_SzCORE_framework_and_challenge.md) | Framework; challenge on private data **(PREPRINT report)** | 28–30 algorithms | Event, −30/+60 s tolerance | 37% (challenge) | FP/day | 43% or 32% (abs, conflict) | Not defined |
| [SeizureTransformer 2025](../papers/D_2025_Wu_SeizureTransformer_EEG_U_Transformer.md) **(PREPRINT)** | TUSZ v2.0.3 eval + Siena | 60 s; U-Net + transformer | SzCORE event | 0.717 | Not captured | **0.671** | Not reported |
| [Zabihi 2026](../papers/D_2026_Zabihi_TUSZ_CatBoost_benchmark.md) | TUSZ v2.0.3 official Train/Dev/Eval | 60 s / 15 s; features + CatBoost | ≥10 s overlap | **0.749** | **0.68/h** (≈16.4/24h) | Window macro-F1 0.81 | "0 s" = dilation artifact |

### What we learn

Accuracy on TUSZ is now fairly well measured, but speed is not. SzCORE accepts an alarm that is up to 60 s late, so a model that fires after 25 s and one that fires after 1 s get the same score. The only patient-independent TUSZ latency (**about 8–16 s**, Lee 2022) comes from an older TUSZ version and a small dev-derived test set. The 2–5 s latencies in the literature are patient-specific CHB-MIT or iEEG results and cannot be compared with it. Offline tricks (60-s windows, future context, dilation) make latency look zero or even negative. Short focal seizures are the hardest case, yet no paper reports latency separately for each seizure type. Our background scan also found a causal Temple University real-time system that reached only **42% sensitivity at 5.78 FA/24h** on TUSZ v1.5.2 dev (outside the 47-paper set) ([arXiv 2202.07796](https://arxiv.org/abs/2202.07796)). This shows the accuracy cost of running truly live.

## Seizure type and spread: fair type scores sit near 0.65–0.75, and spread is only shown in pictures

### What the papers did

**Type classification on TUSZ.** **Tang 2022 (ICLR)** is the reference paper. It uses a graph neural network (DCRNN) over the 19 electrodes, with either a distance graph or a correlation graph. It is pretrained with a self-supervised task (predict the next 12 s of EEG) and tested patient-wise on TUSZ v1.5.2. It merges the types into 4 clinically sensible classes: combined focal (CF), generalized (GN), absence (AB) and combined tonic (CT). It reaches **wF1 0.749 (60-s clips) and 0.746 (12-s clips)**, and **0.650 for 7 classes** with 3-fold patient-wise evaluation. Pretraining raised accuracy on the rare CT class by **47 points**. A neurologist checked 32 misclassified "generalized" test seizures and found that **27 were actually focal**. This is evidence of label noise in TUSZ ([arXiv](https://arxiv.org/pdf/2104.08336)). **SeizureNet 2020** (multi-spectral CNN ensemble) gives the clearest proof of leakage: **wF1 0.95–0.98 with seizure-wise splits but 0.62 with patient-wise splits** ([Semantic Scholar](https://www.semanticscholar.org/paper/SeizureNet:-Multi-Spectral-Deep-Feature-Learning-Asif-Roy/15b8ba09bd4193cec0c17e9d669267d58ed5afc4)). Its companion benchmark (Roy 2019, PREPRINT) reports wF1 up to 0.907 (abs). **Ahmedt-Aristizabal 2020** randomly split 1-s windows 60/20/20 and reports wF1 **0.945**. A similar CNN-LSTM scores only **0.633–0.641** under Tang's patient-wise protocol ([arXiv](https://arxiv.org/pdf/1912.04968)). **Raghu 2020** reports **82.85% and 88.30% accuracy** for 8 classes (abs), and its split protocol could not be checked.

**Onset zone and spread.** Three families exist. First, *saliency maps* from classifiers: Tang's occlusion maps "precisely localize" (score > 0.8) **25.4% of focal seizures**, compared with 3.5% for a plain CNN. Second, *per-channel tracking networks*: **SZTrack (Craley 2022)** outputs seizure activity for each channel over time. With LOPO on 34 patients, it gets **lateralization 0.826, hemisphere and lobe both correct in 21/34 patients, and detection AUROC 0.895**, and on an external pediatric site 8/15 correct. The spread maps are only qualitative, because there is no ground-truth spread label ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8884583/)). Third, *source imaging and network markers*: **DeepSIF** trains a network on neural-mass-model simulations and maps 76-channel EEG to 994 cortical regions. Its onset-zone error is **7.45 ± 8.91 mm for interictal spikes** ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9351497/)) and **10.89 ± 10.14 mm for ictal EEG** (8.03 mm in seizure-free patients) ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11653641/)). **Neural fragility (Li 2021)** is a network-stability marker on intracranial EEG. It predicts surgical outcome with **AUC 0.88 (76% accuracy vs 48% for clinicians)** ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8547387/)).

### Results comparison

| Paper | Data | Split (leak?) | Model | Headline result |
|---|---|---|---|---|
| [Tang 2022](../papers/C_2022_Tang_self_supervised_GNN.md) | TUSZ v1.5.2, 19 ch | **Patient-wise (clean)** | DCRNN graph + self-supervised pretraining | 4-class wF1 **0.749** (60 s) / 0.746 (12 s); 7-class **0.650**; detection AUROC 0.875; 25.4% focal localized |
| [SeizureNet, Asif 2020](../papers/C_2020_Asif_SeizureNet.md) | TUSZ v1.4/1.5.2, 7 types | Seizure-wise **(leaky)** and patient-wise | Multi-spectral CNN ensemble | wF1 0.95–0.98 leaky vs **0.62 patient-wise** |
| Roy 2019 (in same file) **(PREPRINT)** | TUSZ, 7 types | Seizure-wise (inferred) | FFT + kNN/XGBoost/CNN | wF1 up to 0.907 (abs) |
| [Ahmedt-Aristizabal 2020](../papers/C_2020_AhmedtAristizabal_neural_memory_networks.md) | TUSZ v1.4.0, 7 types | **Random window split (severe leak)** | LSTM + memory network | wF1 0.945 |
| [Raghu 2020](../papers/C_2020_Raghu_CNN_transfer_learning.md) | TUSZ (v1.4.0?), 8 classes incl. non-seizure | Not verified | ImageNet CNNs, SVM | Acc 82.85% / 88.30% (abs) |
| [SZTrack, Craley 2022](../papers/C_2022_Craley_SZTrack_seizure_tracking.md) | 34 pts / 201 sz + 15 external pts | **LOPO + external site** | Channel-wise CNN + RNN | Lateralization 0.826; hemisphere+lobe 21/34; external 8/15 |
| [DeepSIF, Sun 2022](../papers/C_2022_Sun_DeepSIF_PNAS.md) | 20 pts, 76-ch interictal | Simulation-trained | NMM simulation → DNN | SOZ error 7.45 ± 8.91 mm; precision 0.79, recall 0.49 vs resection |
| [Ictal DeepSIF, Sun 2024](../papers/C_2024_Sun_DeepSIF_ictal_AdvSci.md) | 33 pts, 76-ch ictal | Simulation-trained | Jansen–Rit ictal simulation → DNN | SOZ distance 10.89 ± 10.14 mm |
| [Neural fragility, Li 2021](../papers/C_2021_Li_neural_fragility_SOZ.md) | 91 pts, 462 sz, **iEEG** | Patient-level outcome | Linear time-varying network model | Outcome AUC 0.88 |

### What we learn

Patient leakage inflates type scores by about **0.33 wF1** on TUSZ. Classes with only 2 patients (simple partial, tonic) cannot be evaluated patient-wise, which is why merging into 4 classes (Tang) is the fair standard. Accuracy numbers (Raghu) cannot be compared with wF1 numbers. No reviewed paper does type classification and spread mapping together, and **none measures spread accuracy with numbers**. All of them validate only the onset location. DeepSIF needs high-density (76-channel) EEG and has not been tested on 19-channel clinical montages like TUSZ in the papers we read.

## Neuroscience models: real warning signals live mostly in slow cycles

### What the papers did

The strongest forecasting evidence comes from months or years of intracranial recordings, not from minutes of scalp EEG. **Baud 2018** showed that interictal spike rates follow **multi-day cycles (most often 20–30 days)** and that seizures cluster on the rising phase in 13/14 patients (relative risk 6.8) ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5758806/)). **Proix 2021** built on these cycles and forecast daily risk in 175 patients with a chronological split and surrogate tests. It reached **AUC 0.74 (development) and 0.70 (validation)**, better than chance in 83% and 66% of patients ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7968722/)). **Maturana 2020** tested critical slowing down (rising variance and autocorrelation). Its pseudo-prospective forecaster reached **77 ± 8% sensitivity with 91% of time in low risk** in 13 patients, clearly above chance ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7195436/)). **Chang 2018** gives the counterpoint: in human iEEG over the 30 min before seizures, autocorrelation rose significantly in only **4/12 patients and fell in 4/12**, so the direction is patient-specific ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7617160/)). **Khambhati 2024** claims that a 90-s hippocampal connectivity snapshot forecasts 24-h risk "as accurately as" cycle models (abs; full text paywalled) ([Nature](https://www.nature.com/articles/s41591-024-03149-6)).

For the E/I "digital twin" idea, the tools exist, but the scalp evidence is thin. **Wendling 2002** explains fast onset activity through impaired dendritic inhibition in an NMM. **Jirsa 2014 (Epileptor)** frames seizure onset and offset as bifurcations, meaning sudden changes of dynamic state ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4107736/)). **Karoly 2018** tracked 5 Jansen–Rit parameters with a Kalman-type filter across **3,010 seizures** and found stereotyped parameter "pathways" during seizures. It is not a pre-seizure study ([PLoS CB](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006403)). **Aarabi & He 2014** fitted a 12-parameter NMM to iEEG spectra and reported **87.07% / 92.6% sensitivity at 0.2 / 0.15 false predictions per hour** in 21 patients (abs; evaluation details unknown) ([PubMed](https://pubmed.ncbi.nlm.nih.gov/24374087/)). **Duma 2025** is the only scalp study (128-channel EEG, 20 patients, 29 seizures). It found that the aperiodic (1/f) exponent **rose (a shift toward inhibition) in the ~13 min before seizures** (t = 6.94, p < 0.001). The change was global, not limited to the epileptic region, and the paper reports no prediction metrics ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12581463/)).

### Results comparison

| Paper | Recording | Patients / duration | Marker / model | Pseudo-prospective? | Headline numbers |
|---|---|---|---|---|---|
| [Maturana 2020](../papers/N_2020_Maturana_critical_slowing.md) | iEEG (NeuroVista) | 13 analysed, 185–767 days, 2,871 sz | CSD + spike rate + cycles | Yes | Sens **77 ± 8%**, 91% time low-risk |
| [Chang 2018](../papers/N_2018_Chang_network_resilience.md) | Slices, rats, human iEEG | 12 humans, 1,890 preictal periods | CSD / resilience | No | Autocorrelation up in 4/12, down in 4/12 |
| [Baud 2018](../papers/N_2018_Baud_multidien_rhythms.md) | RNS implant | 37 pts, median 2.3 y | Circadian + multi-day cycles | No | Phase-locked 13/14; RR 6.8 |
| [Proix 2021](../papers/N_2021_Proix_forecasting_seizure_risk.md) | RNS implant | 18 dev + 157 val | Point-process model on cycle phases | Yes | 24-h AUC **0.74 / 0.70** |
| [Khambhati 2024](../papers/N_2024_Khambhati_hippocampal_connectivity.md) | RNS hippocampal | 15 pts | 90-s connectivity | Unclear | "As accurate as" cycle models (abs) |
| [Duma 2025](../papers/N_2025_Duma_aperiodic_EI_balance.md) | **Scalp hd-EEG 128 ch** | 20 pts, 29 sz | Aperiodic exponent (E/I proxy) | No | Exponent rises preictally (t = 6.94); no prediction metric |
| [Karoly 2018](../papers/N_2018_Karoly_seizure_pathways_JansenRit.md) | iEEG | 12 pts, 3,010 sz | Jansen–Rit + Kalman filter | No (ictal only) | Stereotyped pathways; MSE 0.2–0.9 mV |
| [Aarabi & He 2014](../papers/N_2014_Aarabi_He_model_based_prediction.md) | iEEG, short-term | 21 pts | 12-parameter NMM fitted to spectra | Not evident | Sens 87.07% / 92.6%, FPR 0.2 / 0.15 per h (abs) |
| [Wendling 2002; Jirsa 2014](../papers/N_foundational_Wendling2002_Jirsa2014_models.md) | SEEG; in vitro | – | Wendling NMM; Epileptor | – | Mechanism only |

### What we learn

Honest biomarker forecasting reaches about **AUC 0.70–0.80**, and most of the signal comes from day-to-week cycles. TUSZ sessions are too short to capture these cycles. A TUSZ study can only test minutes-scale markers: variance, autocorrelation, aperiodic exponent, NMM gains and spike rate. The project's working hypothesis ("E/I shifts toward excitation before seizures") is **not** what the one scalp study found. No peer-reviewed paper tracks NMM parameters on preictal *scalp* EEG for forecasting. Sleep, drowsiness and artifacts also change the aperiodic exponent and variance, so they must be controlled.

## Foundation models: small gains for seizures, and a hidden TUSZ overlap

### What the papers did

Five peer-reviewed models form a lineage: **BENDR 2021 → BIOT (NeurIPS 2023) → LaBraM (ICLR 2024) → EEGPT (NeurIPS 2024) → CBraMod (ICLR 2025)**. They share one benchmark protocol (TUAB, TUEV, and CHB-MIT 10-s window detection with only 2 test patients). **None reports TUSZ seizure results.** CBraMod (4.0M parameters, pretrained on the whole TUH archive) leads on all three benchmarks ([arXiv](https://arxiv.org/pdf/2412.07236)). LaBraM put **1,138.53 hours of TUSZ directly into pretraining** ([arXiv](https://arxiv.org/pdf/2405.18765)). BENDR and CBraMod pretrain on the whole TUEG archive, which contains TUSZ. EEGPT used no TUH data, so it is a leakage-free control ([NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2024/file/4540d267eeec4e5dbd9dae9448f0b739-Paper-Conference.pdf)). Two independent benchmarks check whether FMs really help. **EEG-Bench (NeurIPS 2025, likely workshop)** found that on its seizure task **LaBraM (0.588 balanced accuracy) beat an SVM (0.572) by only 1.6 points**, and BENDR scored at chance ([ETH PDF](https://tik-db.ee.ethz.ch/file/1e09e7f339cb0dfcf9ec74bd2bb51c24/)). **EEG-FM-Compass (NSR 2026)**, which covers 12 FMs, concludes that specialist models "remain competitive" and that bigger FMs do not necessarily generalize better ([arXiv](https://arxiv.org/abs/2601.17883)).

### Results comparison (same BIOT protocol)

| Model | Params | TUH in pretraining? | TUAB BAcc / AUROC | TUEV BAcc / wF1 | CHB-MIT BAcc / AUPRC / AUROC |
|---|---|---|---|---|---|
| Best supervised baseline | ~3.5M | – | 0.7966 / 0.8707 | 0.4384 / 0.7024 | 0.6389 / 0.2479 / 0.8662 |
| [BIOT](../papers/F_2023_Yang_BIOT.md) | 3.2M | TUAB/TUEV train sets (supervised) | 0.7959 / 0.8815 | 0.5281 / 0.7492 | 0.7068 / 0.3277 / 0.8761 |
| [LaBraM-Base](../papers/F_2024_Jiang_LaBraM.md) | 5.8M | **Yes, incl. TUSZ** | 0.8140 / 0.9022 | 0.6409 / 0.8312 | 0.7075 / 0.3287 / 0.8679* |
| LaBraM-Huge | 369M | Yes | 0.8258 / 0.9162 | 0.6616 / 0.8329 | – |
| [EEGPT](../papers/F_2024_Wang_EEGPT.md) | 25M | **No** | 0.7983 / 0.8718 | 0.6232 / 0.8187 | – |
| [CBraMod](../papers/F_2025_Wang_CBraMod.md) | 4.0M | **Yes, all TUEG** | **0.8289 / 0.9227** | **0.6671 / 0.8342** | **0.7398 / 0.3689 / 0.8892*** |
| [BENDR](../papers/F_2021_Kostas_BENDR.md) | – | Yes, all TUEG | No TUH/CHB-MIT downstream | – | – |
| [EEG-Bench](../papers/F_2025_Kastrati_EEG-Bench.md) seizure task | – | – | SVM 0.572 vs LaBraM 0.588 (BAcc) | – | – |
| [EEG-FM-Compass](../papers/F_2026_Liu_EEG-FM-Compass.md) | 12 FMs | – | Qualitative: specialists competitive | – | – |

\* CHB-MIT numbers for LaBraM and CBraMod come from the CBraMod paper.

### What we learn

For seizures, FMs add about **+0.02 AUROC on CHB-MIT** over the best supervised model, and AUPRC stays below 0.37. The big gain (+20 points balanced accuracy) appears only on TUEV event typing. All these models use 4–30-s windows and window-level metrics. None reports latency, false alarms per hour or event metrics. Any TUEG-pretrained checkpoint has very likely already seen TUSZ eval-patient EEG (without labels). CBraMod shows how to test this: re-pretraining without the downstream corpus changed results by at most 0.4 points ([arXiv](https://arxiv.org/pdf/2412.07236)).

## Body reaction: the heart often reacts seconds before scalp EEG, but not reliably

### What the papers did

**Leutmezer 2003** found tachycardia (fast heart rate) in **86.9% of 145 focal seizures**, starting **13.7 s before scalp-EEG onset in temporal-lobe seizures and 8.2 s before in extratemporal seizures** (abs) ([PubMed](https://pubmed.ncbi.nlm.nih.gov/12614390/)). **Kato 2014** found the heart-rate rise at **−11.5 ± 14.8 s (before EEG) in right mesial temporal seizures but +9.2 ± 21.7 s (after EEG) in left** (abs) ([Neurology](https://www.neurology.org/doi/10.1212/WNL.0000000000000864)). Wearable detection studies then used these heart changes. **Jeppesen 2019** (heart-rate variability from wearable ECG) reached **93.1% sensitivity at 1.0 FA/24h with 30-s median latency, but only in "responders"** (53.5% of patients) (abs) ([Wiley](https://onlinelibrary.wiley.com/doi/10.1111/epi.16343)). The phase-3 real-time follow-up (**Jeppesen 2025**) got **90.5% sensitivity (100% for focal-to-bilateral tonic-clonic, 82.6% for focal) at a median 1.1 FA/24h and 28-s latency**, but only **17 of 101 enrolled patients** met the autonomic criterion ([Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12516532/fullTextXML)). The Empatica wrist device (**Regalia 2019 / Onorati 2021**) detects convulsive seizures with **sensitivity 0.92–0.94 at 0.57–1.26 FA/24h and 37.5-s latency** ([Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8418082/fullTextXML)). **SeizeIT2 (Swinnen 2026)** tested behind-the-ear EEG plus ECG on 616 focal seizures. It reached **sensitivity 0.73 but precision 0.004**, and sensitivity was **0.74 with tachycardia vs 0.60 without** (abs) ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13238671/)). **Stirling 2021** used Fitbit heart-rate cycles to forecast risk better than chance in **11/11 patients (hourly)** (abs) ([PubMed](https://pubmed.ncbi.nlm.nih.gov/34335457/)). **Karácsony 2022** classified frontal vs temporal seizures from 3D video with **F1 0.833 and AUC 0.89** ([Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9666544/fullTextXML)).

### Results comparison

| Paper | Signals | Patients / seizures | Key numbers | Timing vs EEG |
|---|---|---|---|---|
| [Leutmezer 2003](../papers/B_2003_Leutmezer_ECG_onset_tachycardia.md) | ECG + scalp EEG | 58 / 145 focal | Tachycardia 86.9% (abs) | HR rise **13.7 s / 8.2 s before** EEG (abs) |
| [Kato 2014](../papers/B_2014_Kato_right_left_tachycardia_timing.md) | ECG + video-EEG | 21 / 77 mTLE | HR rise 29/29 right, 42/48 left (abs) | **−11.5 s** right vs **+9.2 s** left (abs) |
| [Jeppesen 2019](../papers/B_2019_Jeppesen_HRV_wearable_ECG_detection.md) | Wearable ECG, HRV | 100 / 126 sz | Se 93.1%, FAR 1.0/24h, responders only (abs) | Median latency 30 s after onset |
| [Jeppesen 2025](../papers/B_2025_Jeppesen_phase3_wearable_ECG_smartphone.md) | ECG patch → phone | 17 eligible / 42 sz | Se 90.5%; FBTC 100%; focal 82.6%; FAR 1.1/24h | Median latency 28 s |
| [Regalia 2019 / Onorati 2021](../papers/B_2019_Regalia_Empatica_multimodal_wristband.md) | Wrist EDA + accelerometer | 152 / 66 convulsive | Se 0.92 / 0.94; FAR 1.26 / 0.57 per 24h | Latency 37.5 s |
| [Stirling 2021](../papers/B_2021_Stirling_wearable_forecasting_Fitbit.md) | Fitbit HR, sleep, steps | 11 pts | Above chance 11/11 hourly, 10/11 daily (abs) | 37 min in warning (hourly) |
| [Swinnen 2026](../papers/B_2026_Swinnen_SeizeIT2_bte_EEG_ECG.md) | Behind-ear EEG + ECG | 192 / 616 focal | Se 0.73, precision 0.004 (abs) | Not in abstract |
| [Karácsony 2022](../papers/B_2022_Karacsony_3D_video_semiology_classification.md) | IR + depth video | 26 / 115 sz | FLE vs TLE F1 0.833, AUC 0.89 | 2-s clips |

### What we learn

The heart often starts to react **about 8–14 s before scalp-EEG onset in focal (especially right temporal) seizures**. However, the spread (±15–22 s) is as large as the mean, so heart rate alone cannot give reliable per-seizure early warning. Deployed body-signal detectors alarm **28–38 s after onset**, so they are detectors, not predictors. They work best for convulsive seizures and for patients with a large heart response (>50 bpm). The TUSZ paper confirms that supplementary channels (including heart rate) exist ([Frontiers](https://www.frontiersin.org/journals/neuroinformatics/articles/10.3389/fninf.2018.00083/full)), but **no reviewed paper analyses the TUSZ ECG/EKG channel**. Also, no paper maps TUSZ seizure-type labels to heart-rate response.

## Baselines to beat for each NeuroMech-Warn objective

| Objective | Best fair baseline (TUSZ if possible) | Exact number | Comparable? | Stronger but non-comparable reference |
|---|---|---|---|---|
| **1. Forecast earlier (prediction)** | [MLSPred-Bench](../papers/P_2025_Mohammad_MLSPred-Bench_TUSZ_prediction_benchmark.md) (TUSZ, patient-disjoint) | Mean val AUC 0.709 (ResNet raw), **0.748 (RF features)**; 15-min preictal 0.811–0.836; segment-level, validation only | Yes (TUSZ), but segment-level only | [CG-MambaNet](../papers/P_2026_Chen_CG-MambaNet_cross_patient_prediction_PREPRINT.md) (PREPRINT) LOPO AUC 0.815, **0.32 FA/h, 23.4 min lead** (CHB-MIT); [Jemal](../papers/P_2024_Jemal_domain_adaptation_cross_subject_prediction.md) LOPO AUC 0.69 → 0.75 with DA |
| **1b. Classic protocol reference** | [Truong 2018](../papers/P_2018_Truong_CNN_seizure_prediction.md) STFT-CNN | 81.2% sens, 0.16 FA/h (CHB-MIT, SOP 30 / SPH 5) | No (patient-specific) | [Meng 2025](../papers/P_2025_Meng_3D-SERESNet_multi_patient_prediction.md) 90.77% / 0.090 FA/h (patient-specific) |
| **2. Detect earlier (latency)** | [Lee 2022](../papers/D_2022_Lee_realtime_seizure_detection.md) streaming CNN-LSTM | **7.76 s** best mean onset latency (range 7.76–15.83 s) at TNR > 0.95; OVLP 0.75 sens at 47.06 FA/24h | Partly (TUSZ v1.5.2, 26 dev pts) | [Xu 2023](../papers/D_2023_Xu_shorter_latency_probabilistic_prediction.md) 2.3 s (patient-specific CHB-MIT) |
| **2b. Keep detection accuracy** | [SeizureTransformer](../papers/D_2025_Wu_SeizureTransformer_EEG_U_Transformer.md) (PREPRINT); [Zabihi 2026](../papers/D_2026_Zabihi_TUSZ_CatBoost_benchmark.md) | Event F1 **0.671**, sens 0.717 (SzCORE, v2.0.3 eval); sens **0.749 at 0.68 FA/h**, AUROC 0.92 | Yes (TUSZ v2.0.3 eval) | Cross-site: challenge F1 0.32–0.43 |
| **3. Seizure type at onset** | [Tang 2022](../papers/C_2022_Tang_self_supervised_GNN.md) | 4-class wF1 **0.746 (12 s) / 0.749 (60 s)**; 7-class **0.650**; CT accuracy 74% | Yes (TUSZ v1.5.2, patient-wise) | Leaky: SeizureNet 0.95–0.98; Ahmedt-Aristizabal 0.945 |
| **4. Spread / localization** | [SZTrack](../papers/C_2022_Craley_SZTrack_seizure_tracking.md); [Tang 2022](../papers/C_2022_Tang_self_supervised_GNN.md) | Hemisphere+lobe 21/34, lateralization 0.826; 25.4% focal seizures localized (>0.8) | Partly (SZTrack on private data; Tang on TUSZ) | [DeepSIF](../papers/C_2024_Sun_DeepSIF_ictal_AdvSci.md) 10.89 mm ictal (76-ch); [fragility](../papers/C_2021_Li_neural_fragility_SOZ.md) AUC 0.88 (iEEG) |
| **5. Body-reaction estimation** | [Leutmezer 2003](../papers/B_2003_Leutmezer_ECG_onset_tachycardia.md); [Kato 2014](../papers/B_2014_Kato_right_left_tachycardia_timing.md) | HR rise 13.7 s / 8.2 s before EEG; −11.5 s (right) / +9.2 s (left) (abs) | No TUSZ baseline exists | [Jeppesen 2025](../papers/B_2025_Jeppesen_phase3_wearable_ECG_smartphone.md) Se 90.5%, 1.1 FA/24h, 28 s latency |
| **6. NMM E/I digital twin** | [Aarabi & He 2014](../papers/N_2014_Aarabi_He_model_based_prediction.md); [Duma 2025](../papers/N_2025_Duma_aperiodic_EI_balance.md) | 87.07% / 92.6% sens at 0.2 / 0.15 per h (iEEG, abs); scalp exponent rise t = 6.94 (no prediction metric) | No scalp/TUSZ baseline | Forecast ceiling: [Proix](../papers/N_2021_Proix_forecasting_seizure_risk.md) AUC 0.70–0.74; [Maturana](../papers/N_2020_Maturana_critical_slowing.md) 77% sens |
| **7. Brain visualization** | None quantitative | Only qualitative maps (SZTrack, Tang occlusion, DeepSIF, fragility heatmaps) | – | – |
| **(Backbone choice)** | [CBraMod](../papers/F_2025_Wang_CBraMod.md) vs supervised | CHB-MIT AUROC 0.8892 vs 0.8662; AUPRC 0.3689 vs 0.2479 | Not TUSZ; 2 test patients | [EEG-Bench](../papers/F_2025_Kastrati_EEG-Bench.md): LaBraM 0.588 vs SVM 0.572 |

## Common pitfalls that inflate or confuse results

**Patient leakage is the biggest problem.** Pooled or segment-shuffled splits put the same patient in training and test. Measured on the same data and model, this adds about **35 accuracy points in prediction** (Jemal: 97.36% pooled vs 63.5% LOPO) and about **0.33 wF1 in type classification** (SeizureNet: 0.95 vs 0.62). Watch for misleading names: "subject-independent" (Dissanayake) and "patient-independent" (Meng) can still include the test patient. Leave-one-seizure-out also trains on the same patient's *future* seizures (Truong, Koutsouvelis, Meng). A newer, hidden form of leakage is **foundation-model pretraining on TUEG or TUSZ**. LaBraM, BENDR and CBraMod have probably seen TUSZ eval-patient EEG before fine-tuning.

**Scoring differences change the numbers more than the models do.** Segment-level false alarms differ from event-level ones by **more than 300 times** (CG-MambaNet: 112.4/h vs 0.32/h). The same TUSZ detector gives 0.75 sensitivity under OVLP but 0.33 under TAES (Lee). SzCORE's −30/+60 s tolerance makes early and late alarms look the same. Offline dilation or future context produces fake "0 s" or negative latency (Zabihi). The words "prediction time" and "warning time" have at least three definitions. MLSPred-Bench **swaps the SPH and SOP names**, so its "SPH 30 / SOP 5" means conventional "SOP 30 / SPH 5". Accuracy, wF1, balanced accuracy and AUROC are not interchangeable. Results reported on a validation set that was also used for tuning and early stopping (MLSPred-Bench) are optimistic.

**Dataset versions and subsets differ.** TUSZ v1.2.0, v1.4, v1.5.2 and v2.0.3 have different annotations and splits. Lee used a 26-patient subset of dev, while others use the full eval set. MLSPred-Bench does not state its TUSZ version. TUSZ labels also contain noise: 27 of 32 checked "generalized" errors were really focal seizures (Tang). In prediction, preictal windows can include postictal EEG from the previous seizure, and interictal windows can sit close to seizures, when no buffer is enforced (MLSPred-Bench).

**Some numbers are abstract-only, preprint or internally inconsistent.** Abstract-only numbers in this review: Kuhlmann, Aarabi & He, Khambhati, Raghu, Roy 2019, Leutmezer, Kato, Jeppesen 2019, Regalia, Stirling, Swinnen and the SzCORE challenge. Preprints: SeizureTransformer, CG-MambaNet, the challenge report and Roy 2019. Documented inconsistencies: the challenge top F1 (43% vs 32%); MLSPred-Bench table copy errors and a bioRxiv vs journal seizure-count conflict (1,847 vs 1,282); a CG-MambaNet ablation vs main-table sensitivity mismatch (71.8% vs 74.3%) and a mis-cited Jemal baseline; Jemal's abstract swapping the dataset improvements; and two Truong Kaggle versions (75% / 0.21/h in the journal vs 82.3% / 0.22/h on arXiv). A widely circulated summary of CBraMod contains made-up numbers (TUEV BAcc 0.8523 vs the real 0.6671). Always cite the PDF tables.

**Small test sets hide variance.** CHB-MIT FM benchmarks use only **2 test patients**. MLSPred-Bench uses a single fold, and its AUC jumps from 0.564 to 0.805 to 0.508 across neighbouring horizons. Per-patient LOPO AUCs in Jemal range from **0.29 to 0.96**. Without confidence intervals computed across patients, small differences are not meaningful.

## Gaps that NeuroMech-Warn can fill

| Gap | Evidence it is open | Objective |
|---|---|---|
| **No test-set, event-level, patient-independent prediction on TUSZ** (sensitivity, FA/h, warning-time distribution, chance test) | MLSPred-Bench reports validation segment AUC only; no other TUSZ prediction paper was found (the Parani et al. 2024/2025 follow-ups were not checked) | 1 |
| **No causal onset latency with SzCORE F1 on TUSZ v2.x** | Lee 2022 is on v1.5.2 with 26 dev patients; SeizureTransformer and Zabihi report no causal latency; SzCORE has no latency metric | 2 |
| **No patient-independent soft-label / evidence-accumulation early detection on TUSZ** | Xu 2023 is patient-specific on CHB-MIT/SWEC-ETHZ | 2 |
| **No latency or prediction results per seizure type** | Zabihi detects only 33% of short focal seizures but does not stratify by type; no reviewed paper reports this | 1–3 |
| **No joint type-at-onset + spread model, and no numerical spread metric** | Tang, SZTrack and DeepSIF validate onset location only; spread maps are qualitative | 3–4, 7 |
| **No DeepSIF-style source imaging tested on 19-channel TUSZ** | DeepSIF used 76-channel hd-EEG | 4, 7 |
| **No use of the TUSZ ECG/EKG channel**; no type-to-heart-rate mapping | Three searches found none; channel availability is unverified | 5 |
| **No NMM E/I tracking on preictal scalp EEG for forecasting**; E/I direction unclear | Karoly is ictal iEEG; Aarabi & He is iEEG (abs); Duma found an inhibition shift with no prediction metric | 6 |
| **No FM results on TUSZ seizure forecasting, latency or type**; overlap not controlled | All FM papers use TUAB/TUEV/CHB-MIT windows | Backbone |
| **No standard warning-time definition or lead-time distribution reported with FA/h** | Truong, Koutsouvelis and CG-MambaNet each define it differently | 1 |

Two limits must be stated honestly. First, TUSZ cannot test the multi-day cycles that drive most validated forecasting skill, so "earlier" on TUSZ means minutes, not days. Second, the literature gives no human evidence yet that earlier alarms improve clinical outcomes. This is an engineering goal, not a proven clinical benefit.

## Implications for approach selection

1. Adopt a fixed, published protocol before choosing models. Use the official TUSZ v2.0.x split, thresholds frozen on dev, SzCORE event metrics, conventional SPH/SOP naming, an interictal and postictal buffer, and a chance or surrogate test.
2. Define latency and warning time explicitly and causally. Report distributions (median/IQR, % detected within 5 s and 10 s), latency vs false alarms per day, and results per seizure type.
3. Include cheap strong baselines: RF/CatBoost on hand-crafted features (MLSPred, Zabihi) and a Truong-style STFT-CNN, next to any deep or FM model.
4. If a foundation model is used, compare it with a random-initialized copy of the same model and a leakage-free control (EEGPT), and check TUEG/TUSZ patient overlap.
5. Treat alarm post-processing (k-of-n, persistence, refractory period, accumulation) as a tuned and reported part of the system, because it controls false alarms more than the classifier does.
6. For type and spread, use patient-wise 4-class labels (Tang scheme) and design a numerical spread metric from TUSZ channel annotations.
7. For E/I and body modules, allow both E/I directions, control for sleep and artifacts, and first check ECG channel availability and quality in TUSZ.
8. Add at least one external dataset (Siena or CHB-MIT) because of the large cross-site generalization gap.

## Conclusion

The literature does not lack models. It lacks **fair, comparable measurements of time**. Across all six areas, the size of a reported result mostly tracks how leaky the evaluation was, not how clever the model was. Fair numbers cluster in a narrow, modest band: AUC about 0.7–0.8 for prediction, event F1 about 0.67 for TUSZ detection, and wF1 about 0.65–0.75 for type. So a project that reports honest numbers inside this band, *together with* the time dimension that others skip (lead time, onset latency, per-type delay), would be a real contribution even without beating any accuracy record.

The biophysical and body-signal ideas in NeuroMech-Warn are the least explored parts, and also the riskiest. The one scalp E/I study points in the opposite direction from the project hypothesis. The heart-rate lead is real on average but too variable for individual warnings. And the TUSZ ECG channel has never been checked. These modules are best framed as testable scientific questions with pre-registered success criteria, not as guaranteed performance gains. Their value comes from being first to measure them fairly on a large public corpus.
