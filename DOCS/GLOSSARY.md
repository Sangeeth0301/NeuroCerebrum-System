# Glossary

Plain-English meanings of terms used in this project.

## Seizures and EEG

| Term | Meaning |
|---|---|
| **EEG** | Electroencephalogram: electrical brain activity recorded from electrodes on the scalp. |
| **ECG / EKG** | Electrocardiogram: electrical activity of the heart. TUSZ includes it in some recordings. |
| **Interictal** | The period far from any seizure ("calm"). |
| **Preictal** | The period just before a seizure (minutes). The warning window. |
| **Ictal** | During the seizure. |
| **Postictal** | Just after the seizure (recovery). |
| **Onset** | The moment an expert marks the seizure as starting on EEG. |
| **Focal seizure** | Starts in one area of the brain (FNSZ, CPSZ, SPSZ in TUSZ). |
| **Generalized seizure** | Involves both sides of the brain from the start (GNSZ, ABSZ, TNSZ, TCSZ, MYSZ, ATSZ). |
| **SOZ** | Seizure onset zone: where the seizure starts. |
| **Spread / recruitment** | Other brain regions joining the seizure after onset. |
| **Semiology** | What the seizure looks like in the body (staring, automatisms, stiffening, convulsions). |
| **Montage** | How electrodes are paired into channels. |
| **TCP montage** | Temporal central parasagittal: the 22-channel bipolar montage used by TUSZ. |
| **Artifact** | Non-brain signal in EEG: eye blinks, muscle, electrode pops. |

## Datasets

| Term | Meaning |
|---|---|
| **TUSZ** | Temple University Hospital EEG Seizure Corpus. Main dataset, with per-channel seizure labels. |
| **TUAR** | TUH EEG Artifact Corpus. Used to train the artifact gate. |
| **TUEG** | The full TUH EEG archive (contains TUSZ). |
| **CHB-MIT** | Children's Hospital Boston scalp EEG. External test with long recordings. |
| **Siena** | Siena Scalp EEG database. External adult test set. |
| **DUA** | Data use agreement. TUSZ/TUAR may not be redistributed. |

## Evaluation

| Term | Meaning |
|---|---|
| **Patient-independent** | Test patients are never used in training. The fair setting. |
| **LOPO** | Leave-one-patient-out cross-validation. |
| **Leakage** | Information from the test set reaching training (e.g. same patient in both). Inflates results. |
| **Causal** | Uses only past and present samples, so it can run live. |
| **Onset latency** | Seconds from expert onset to the first alarm. |
| **Warning time** | Minutes from a forecast alarm to seizure onset. |
| **SPH** | Seizure prediction horizon: gap between the alarm and the window where the seizure is expected. |
| **SOP** | Seizure occurrence period: the window in which the seizure must happen for the alarm to count. |
| **FA/h, FA/24h** | False alarms per hour / per day. |
| **Event-level metric** | Scores whole seizures and alarms, not small windows. |
| **SzCORE** | Standard event-based seizure detection scoring framework. |
| **Chance / random predictor test** | Checks that a forecaster beats random alarms with the same alarm rate. |
| **wF1** | F1 averaged over classes, weighted by class size. |
| **AUROC / AUPRC** | Threshold-free ranking scores; AUROC 0.5 = chance. |
| **C-index** | Concordance: how well predicted risk orders times-to-event. |
| **Bootstrap CI** | Confidence interval from resampling patients. |
| **Ablation** | Removing one component to measure its contribution. |

## Neuroscience

| Term | Meaning |
|---|---|
| **E/I balance** | Balance between excitation and inhibition in the brain. |
| **Aperiodic (1/f) exponent** | Slope of the EEG power spectrum; higher values suggest more inhibition. |
| **Critical slowing down (CSD)** | A system near a sudden change recovers more slowly; variance and autocorrelation rise. |
| **wPLI / PLV** | Measures of phase synchrony between two channels. |
| **Directed flow** | Which region drives another (e.g. Granger causality). |
| **Neural mass model** | Equations describing the average activity of a population of neurons. |
| **Wendling model** | Neural mass model with pyramidal cells, excitatory interneurons and slow + fast inhibitory interneurons. Gains A (excitation), B (slow inhibition), G (fast inhibition). |
| **Jansen–Rit model** | Simpler neural mass model (one inhibitory population). |
| **Bifurcation / tipping point** | Where a small change flips the system into a new state (e.g. seizure). |

## Methods in the architecture

| Term | Meaning |
|---|---|
| **GNM-ODE** | Graph Neural-Mass ODE: our backbone; each electrode is a small E/I population, coupled through a graph. |
| **ODE** | Ordinary differential equation: describes how a state changes over time. |
| **Jacobian / λ_max** | Matrix of how the dynamics respond to small changes; its leading eigenvalue near 0 means low stability. |
| **Stability margin** | −Re λ_max: shrinks toward 0 as a seizure approaches. |
| **SBI** | Simulation-based inference: learn to infer model parameters by training on simulations. |
| **Amortized posterior** | An SBI network trained once that gives parameter estimates instantly for any new window. |
| **Soft labels** | Labels between 0 and 1 for windows that are partly seizure. |
| **Competing-risks hazard** | Survival model giving the probability of each event type (focal / generalized) in each future time bin. |
| **Censoring** | When a recording ends before we know whether a seizure happened. |
| **CUSUM** | Cumulative-sum test that raises an alarm when evidence for a change builds up. |
| **k-of-n** | Alarm only if k of the last n decisions are positive. |
| **Refractory period** | Time after an alarm during which new alarms are suppressed. |
| **Conformal calibration** | Statistical method that sets thresholds to guarantee an error rate (here, a false-alarm budget). |
| **DANN** | Domain-adversarial training: makes features that do not reveal which patient they came from. |
| **Distillation** | Training a small "student" model to copy a large "teacher". |
| **Hydra** | Configuration system used for all settings (`configs/`). |
