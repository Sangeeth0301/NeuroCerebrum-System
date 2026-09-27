# NeuroMech-Warn — Final Architecture (v2)

**Graph Neural-Mass Dynamics for forecasting when, where and what type of seizure is coming — and explaining it through the brain's own loss of stability.**

**Status:** final design v2 (no code yet). Built on the literature review (`research/reports/Seizure forecasting literature review.md`), validated against the problem statement (`NeuroMech-Warn_Problem_Statement.md`), and novelty-checked against 2022–2026 work. Every objective is served by at least one component.

> "Earlier and better than previous work" is the design goal. Only experiments on TUSZ can prove it, so the design keeps a strong fallback (v1.1 backbone) and an ablation plan that shows which part produces each gain.

---

## 1. Architecture at a glance

```
 EEG (22-ch) ──► 0. Causal front-end + artifact gate ──► SLOW (60 s/10 s)   FAST (4 s/1 s)
 ECG ──────────► R-peaks · HR · HRV ──────────────────────────┐        │              │
                                                              │        ▼              ▼
          ┌──────────────────────────────┐    ┌─────────────────────────────────────────────┐
          │ 1. Neuro-dynamics bank       │───►│ 3. GRAPH NEURAL-MASS ODE  (backbone)         │
          │ 1/f · CSD · spikes · wPLI    │ W  │  per-electrode E/I populations (Wendling)    │
          └──────────────────────────────┘ ij │  + graph coupling W_ij(t) + NN residual      │
          ┌──────────────────────────────┐    │  gains A_i,B_i,G_i(t) drift ← SBI prior      │
          │ 2. SBI twin (prior for gains)│───►│  must reproduce the real EEG                 │
          └──────────────────────────────┘    └──────┬──────────┬──────────┬────────────────┘
                                                     │ state x(t) │ Jacobian │ roll-forward
                                                     ▼            ▼          ▼
                        ┌───────────────────────────────────────────────────────────────┐
                        │ 4. Neuro-guided fusion (+ ECG tokens, missing-modality safe)   │
                        └───┬─────────────┬───────────────┬──────────────┬────────────┬──┘
                            ▼             ▼               ▼              ▼            ▼
                 ┌──────────────┐┌─────────────┐┌───────────────┐┌─────────────┐┌─────────┐
                 │H1 COMPETING- ││H2 STABILITY ││H3 ONSET (soft ││H4 SPREAD:   ││H5 TYPE +│
                 │ RISKS HAZARD ││ MARGIN m(t) ││ labels, per s)││ learned     ││ BODY    │
                 │ when·type·   ││ −Re λ_max   ││               ││ + ODE       ││         │
                 │ where        ││ per node    ││               ││ rollout     ││         │
                 └──────┬───────┘└──────┬──────┘└──────┬────────┘└──────┬──────┘└────┬────┘
                        └───────┬───────┘              │                │            │
                                ▼                      ▼                ▼            ▼
                 ┌─────────────────────────────────────────┐   ┌──────────────────────────┐
                 │ 6. CASCADED ALARM                       │──►│ 7. Report · dashboard    │
                 │ A: hazard + stability + HRV → CUSUM     │   │ virtual neurons = model  │
                 │ B: onset + tachycardia → accumulation   │   │ state · spread preview   │
                 │ bounded threshold drop · per-type thr.  │   └──────────────────────────┘
                 │ one conformal false-alarm budget        │    8. distilled 4-ch student
                 └─────────────────────────────────────────┘
```

### Built on
| Base | Paper | What we take |
|---|---|---|
| Soft-label onset + evidence-accumulation alarm | Xu 2024, *Expert Syst. Appl.* | Main "earlier" mechanism at onset |
| Electrode-graph spatiotemporal modelling | Tang 2022 (ICLR), Craley 2022 (*PLoS ONE*, SZTrack) | Per-electrode outputs, graph coupling |
| Brain-dynamics early-warning features | Duma 2025 (*BMC Med.*), Maturana 2020 (*Nat. Commun.*) | 1/f exponent, critical slowing, connectivity |
| Neural-mass modelling | Wendling 2002, Karoly 2018, Sun 2024 (DeepSIF), SBI (Hashemi) | E/I populations, simulation-based priors |
| Supporting | Jemal 2024, Meng 2025, Zabihi 2026, Jeppesen 2025, Liu 2026, Lemoine (EEGSurvNet) | Domain adaptation, k-of-n alarm, alarm-budget protocol, ECG, small models, survival heads |

---

## 2. Components

### 0 — Causal front-end
| Part | What it does |
|---|---|
| Montage | TUSZ → 22-ch TCP bipolar, 250 Hz; handles AR1/LE2/AR3/LE4 references (MLSPred-Bench code) |
| Causal filters | IIR 60 Hz notch + 0.5–45 Hz, forward-only |
| Artifact gate | Small CNN trained on TUAR; flags eye/muscle/electrode artifacts per channel; down-weights, does not delete |
| Two clocks | SLOW: 60-s windows every 10 s over last 30 min (forecasting). FAST: 4-s windows every 1 s (onset) |
| ECG path | EKG channel when present → R-peaks → HR, HRV (minutes) and tachycardia onset (seconds) |

### 1 — Neuro-dynamics bank ("brain-state tokens")
Per channel, causal, kept as trajectories: aperiodic 1/f exponent + offset (specparam), band powers δθαβγ, critical slowing (variance, lag-1 AC, decay), interictal spike rate, line length / Hjorth / entropy, wPLI/PLV per band + directed in/out flow. **Slow wPLI** (forecasting) and **fast 4-s wPLI** (onset) both feed the graph coupling.

### 2 — SBI twin (prior for the gains)
Offline: Wendling model simulations → amortized neural posterior estimator. Online: per channel, per slow window → posterior over **A, B, G** (time constants fixed first) → initial/prior values for the backbone's gains. Validated with simulation-based calibration and posterior-predictive checks.

### 3 — Graph Neural-Mass ODE backbone (GNM-ODE) — *core novelty*
```
Each electrode i: latent E/I population  x_i = [pyramidal, excitatory, slow-inhibitory, fast-inhibitory]

   dx_i/dt =  Wendling_f( x_i ; A_i(t), B_i(t), G_i(t) )     ← mechanistic E/I dynamics
            + Σ_j  W_ij(t) · S(x_j)                           ← graph coupling = spread
            + NN_residual( x_i, context )                     ← learned correction

   A_i, B_i, G_i (t) : slowly drifting gains, updated every slow window (SBI prior)
   W_ij(t)           : dynamic coupling = live wPLI + electrode distance + learned
   EEG_i ≈ observation(x_i)  → reconstruction loss keeps the latent physiological
```
- Runs on a ~50 Hz latent, fixed-step solver, short rollouts.
- The model's hidden state **is** a population of excitatory and inhibitory neurons: the dashboard's virtual neurons are the model itself.
- **Fallback backbone:** v1.1 shared temporal CNN → dynamic graph attention → causal state-space model (Mamba-style/GRU). Kept for ablation and as a guaranteed baseline.

### 4 — Neuro-guided fusion
Gated cross-attention between each electrode's state and its own + neighbours' brain-state tokens; **ECG tokens** with missing-modality dropout; **running robust patient baseline** (EW median of artifact-free, low-risk windows; population baseline at start); domain-adversarial training (DANN).

---

## 3. Heads
| Head | Output | Training | Novel? |
|---|---|---|---|
| **H1 Competing-risks hazard** | For bins chosen by data audit (e.g. 0–1, 1–2, 2–5, 5–10, 10+ min): P(focal seizure starting at electrode *i*), P(generalized seizure), P(none yet) | Discrete-time competing-risks survival NLL; censoring for short follow-up | ✅ when + type + where **before onset** |
| **H2 Stability margin** | m(t) = −Re λ_max of the GNM-ODE Jacobian, per electrode and global | Self-supervised from the learned dynamics; smoothed over slow windows | ✅ learned-dynamics tipping-point signal |
| **H3 Onset** | Per-second ictal probability | Soft labels across onset-crossing windows (Xu) | ✅ first cross-patient on TUSZ |
| **H4 Spread** | Per-electrode activity now; recruitment in next 5/10 s; generalization risk | Learned head (TUSZ per-channel labels) + GNM-ODE roll-forward ensemble | ✅ physics-based spread forecast + numeric metrics |
| **H5 Type + body** | 4-class type (primary) / 7-class (secondary); HR change, tachycardia; inferred awareness / automatisms / convulsions | Noise-robust hierarchical loss; ECG features + semiology table (labelled inferred) | ✅ TUSZ ECG unused so far |

**Numeric spread metrics:** onset-channel F1 · recruitment-order Kendall τ · time-to-recruit error (s) · next-channel F1 at 5 s / 10 s.

---

## 4. Cascaded alarm (component 6)
```
Stage A · FORECAST   hazard (H1) + stability margin (H2) + HRV trend
                     → log-likelihood ratio → CUSUM → k-of-n + 30-min refractory
                     → "⚠ focal seizure likely in ~X min, left temporal"

Stage B · ONSET      onset prob (H3) + tachycardia onset → accumulated evidence → alarm
                     while A is active: threshold lowered by a BOUNDED amount (≤ 20%)

Calibration          per-type thresholds; whole cascade calibrated to ONE false-alarm budget
                     dev split by patient: half for thresholds, half for conformal calibration
```

## 5. Outputs (7, 8)
Explainer (feature-group + gain + stability contributions, graph-attention maps) · auto seizure report · dashboard: scalp map, 3D brain (fsaverage + eLORETA), live network, **virtual neurons = model state**, spread preview from ODE rollout, risk timeline · **distilled 4-channel student** (<100k params, int8, MFLOPs reported).

---

## 6. Training
| Stage | What | Data |
|---|---|---|
| S0 Data audit | Preictal durations, per-channel labels, ECG availability → hazard bins | TUSZ |
| S1 SBI twin | Wendling simulations → posterior estimator | Simulations |
| S2 Pretraining | Time-contrastive + masked-channel + next-seconds prediction | TUSZ train only (or TUEG minus eval patients) |
| S3 Staged fine-tuning | H3 → H1/H2 → H4/H5; losses balanced by uncertainty weighting | TUSZ train; selection on dev-A |
| S4 Calibration | Per-type thresholds, conformal budget, safe test-time adaptation rules | TUSZ dev-B (then frozen) |
| S5 Distillation | 4-channel student | TUSZ train |
| External test | Long-horizon forecasting, cross-site | CHB-MIT, Siena |

```
L = w1·CompetingRisksNLL(H1) + w2·SoftBCE(H3) + w3·ChannelBCE + w4·SpreadBCE(H4)
  + w5·NoiseRobustCE(H5-type) + w6·BodyMSE(H5) + w7·EEG-Reconstruction(GNM-ODE)
  + w8·DomainAdversarial + w9·TemporalSmoothness        (w's learned by uncertainty weighting)
```

---

## 7. Novel contributions (positioned against prior work)
| # | Contribution | Closest prior work | Why ours is new |
|---|---|---|---|
| N1 | Graph Neural-Mass ODE backbone (trainable E/I dynamics per electrode, graph-coupled) | Kuramoto neural ODE on TUSZ (EMBC 2025); HP-GNN (PLOS One 2026) | E/I physiology, not phase oscillators; the twin *is* the model |
| N2 | Stability margin from the learned Jacobian as early warning | Generic deep tipping-point warnings (PNAS 2021) | Measured on learned brain dynamics, per electrode |
| N3 | Competing-risks hazard: when + type + where before onset | EEGSurvNet (days–years, no type/location) | Minute-scale, streaming, type & onset zone pre-onset |
| N4 | Mechanistic spread rollout + numeric spread metrics on TUSZ | SZTrack (qualitative maps) | Physics-based forecast scored on per-channel labels |
| N5 | Cascaded forecast → onset alarm, bounded prior boost, one conformal budget | Separate systems | Joint and calibrated |
| N6 | Cardio-neural cascade (HRV minutes + tachycardia seconds) | EEG+ECG fusion, patient-specific (2016) | Cross-patient, TUSZ, missing-modality safe |
| N7 | Per-type earliness and per-type thresholds | — | First on TUSZ |
| N8 | Distilled 4-channel student of a mechanistic forecaster | Wearable detectors | Distilled from a neural-mass model |

Dynamic connectivity graphs alone (AFC-GCN 2024, graph-generative GNN 2022, ODEBrain 2026) are **not** claimed as novel.

---

## 8. Targets and honest likelihood
| Target (TUSZ eval, unseen patients) | Best previous | Target | Likelihood |
|---|---|---|---|
| Onset latency, median | ~8–16 s (Lee 2022) | ≤ 5 s at matched FA | Medium-high |
| Detection sensitivity @ FA | 0.75 @ 0.68 FA/h (Zabihi 2026, offline) | ≥ 0.75 @ ≤ 0.5 FA/h, causal | Medium |
| Forecast | Window AUC 0.71–0.75, no warning time (MLSPred-Bench) | Beat MLSPred; event sens ≥ 60% @ ≤ 0.3 FA/h; median warning ≥ 5 min; beats random predictor | Beat MLSPred: medium-high · AUC ≥ 0.80: medium-low |
| Type before onset (focal vs generalized) | none | Above chance, reported per bin | Medium (first ever) |
| Type at onset, 4-class wF1 | 0.749 (Tang 2022) | ≥ 0.77 | Medium |
| Spread metrics | none on TUSZ | First numbers | High |
| Per-type earliness + ECG | none | First numbers | High |

## 9. Ablations
GNM-ODE vs v1.1 backbone · no neuro bank · no SBI prior · no stability margin · binary instead of competing-risks head · hard instead of soft onset labels · no cascade · no ECG · no patient baseline · static vs dynamic coupling.

## 10. Risks and build order
| Risk | Handling |
|---|---|
| Neural ODE slow/unstable | 50 Hz latent, fixed-step, short rollouts, SBI-initialised gains, v1.1 fallback |
| Gain identifiability | 3 gains first; SBC + posterior checks; gated input; report nulls honestly |
| Noisy Jacobian eigenvalues | Smoothed; one input among several |
| Short TUSZ preictal data | Data audit sets bins; censoring; long horizons on CHB-MIT/Siena |
| ECG missing in some files | Missing-modality dropout |
| Label noise in types | Noise-robust loss; 4-class primary |
| Leakage | TUSZ-train-only pretraining; dev split for thresholds vs conformal; eval used once |
| Scope | Build order below |

**Build order:** S0 data audit → front-end + v1.1 backbone + H3 onset + alarm Stage B (first full result) → neuro bank + H1 + Stage A → SBI twin → GNM-ODE backbone + H2 stability + H4 rollout → H5 + ECG → dashboard → distilled student.

## References for positioning
- Lemoine et al., EEGSurvNet, *Epilepsia* — https://doi.org/10.1002/epi.70101
- Physics-informed Kuramoto neural ODE on TUSZ (EMBC 2025) — https://pubmed.ncbi.nlm.nih.gov/41336412/
- HP-GNN, *PLOS One* 2026 — https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0345470
- E/I dynamic polynomial network — https://pmc.ncbi.nlm.nih.gov/articles/PMC13258883/
- Bury et al., deep learning tipping points, *PNAS* 2021 — https://www.pnas.org/doi/10.1073/pnas.2106140118
- AFC-GCN 2024 — https://pubmed.ncbi.nlm.nih.gov/39269793/
- Graph-generative GNN, *Sci. Rep.* 2022 — https://www.nature.com/articles/s41598-022-23656-1
- Hashemi et al., SBI for whole-brain epilepsy models — https://www.medrxiv.org/content/10.1101/2022.06.02.22275860v1.full
- SBI validity audit for neural mass models (2026) — https://arxiv.org/pdf/2607.24874
- EEG+ECG fusion for onset detection (2016) — https://pubmed.ncbi.nlm.nih.gov/27057745/
- TUSZ corpus paper (per-channel annotations) — https://pmc.ncbi.nlm.nih.gov/articles/PMC6246677/
