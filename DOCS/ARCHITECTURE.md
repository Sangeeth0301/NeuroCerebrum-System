# NeuroMech-Warn — Proposed Architecture

**Status:** design proposal v1 (no code yet). Built from the strongest recent approaches in the literature review (`research/reports/Seizure forecasting literature review.md`) plus new components that fill the gaps found there. Every objective in `NeuroMech-Warn_Problem_Statement.md` is served by at least one component.

> "Earlier and better than previous work" is the design goal. Only experiments on TUSZ can prove it, so the design includes an ablation plan that shows which part produces each gain.

---

## 1. The big picture

```
                         ┌───────────────────────────────────────────────┐
  TUSZ EEG (22-ch TCP)   │ 0. CAUSAL FRONT-END                          │
  + ECG channel ────────►│  montage · causal filters · artifact gate    │
                         │  two clocks: FAST (1 s hop) + SLOW (10 s hop)│
                         └───────┬───────────────┬───────────────┬──────┘
                                 │               │               │
        ┌────────────────────────▼───┐ ┌─────────▼──────────┐ ┌──▼─────────────────┐
        │ 1. NEURO-DYNAMICS BANK     │ │ 2. NEURAL-MASS     │ │ 3. ELECTRODE-GRAPH │
        │ (per channel, minutes)     │ │    DIGITAL TWIN    │ │    ENCODER         │
        │ 1/f exponent · band powers │ │ Wendling model +   │ │ shared per-channel │
        │ critical slowing (var, AC) │ │ amortized SBI →    │ │ temporal CNN →     │
        │ spike rate · line length   │ │ A, B, G, a, b, g   │ │ dynamic graph      │
        │ PLV / directed flow        │ │ + uncertainty      │ │ attention → causal │
        └────────────┬───────────────┘ └─────────┬──────────┘ │ state-space model  │
                     │ "brain-state tokens"      │ "physiology│ (per node + global)│
                     └───────────────┬───────────┘  tokens"   └──────────┬─────────┘
                                     ▼                                   │
                      ┌──────────────────────────────────────────────────▼──┐
                      │ 4. NEURO-GUIDED FUSION                               │
                      │ node embeddings ⟷ cross-attention with brain-state   │
                      │ & physiology tokens (gated) · patient-baseline norm  │
                      └──────┬──────────┬──────────┬──────────┬──────────┬───┘
                             ▼          ▼          ▼          ▼          ▼
                     ┌───────────┐┌──────────┐┌──────────┐┌─────────┐┌──────────┐
          5. HEADS   │H1 TIME-TO-││H2 ONSET  ││H3 PER-   ││H4 TYPE  ││H5 BODY   │
                     │  SEIZURE  ││ (soft    ││ ELECTRODE││focal/gen││HR from   │
                     │  hazard   ││ labels)  ││ + SPREAD ││→ 4 → 7  ││ECG +     │
                     │ (minutes) ││(seconds) ││ FORECAST ││ classes ││semiology │
                     └─────┬─────┘└────┬─────┘└────┬─────┘└────┬────┘└────┬─────┘
                           └─────┬─────┘           │           │          │
                                 ▼                 │           │          │
                 ┌──────────────────────────────┐  │           │          │
      6. ALARM   │ CASCADED EVIDENCE ENGINE     │  │           │          │
                 │ forecast alarm (CUSUM + k/n) │  │           │          │
                 │  └► lowers onset threshold   │  │           │          │
                 │ onset alarm (accumulation)   │  │           │          │
                 │ conformal false-alarm budget │  │           │          │
                 └──────────────┬───────────────┘  │           │          │
                                ▼                  ▼           ▼          ▼
                 ┌────────────────────────────────────────────────────────────┐
      7. OUTPUT  │ Explainer · Seizure report · Brain dashboard (scalp map,   │
                 │ 3D brain, network, virtual neurons, timeline)              │
                 └────────────────────────────────────────────────────────────┘
      8. DEPLOY: distilled tiny 4-channel student model (wearable / implant)
```

### Base approaches it builds on

| Base | Paper | What we take |
|---|---|---|
| #1 Soft-label onset + evidence-accumulation alarm | Xu 2024, *Expert Syst. Appl.* | The main "earlier" mechanism (2.3 s latency, patient-specific) |
| #2 Electrode-graph spatiotemporal encoder | Tang 2022 (ICLR), Craley 2022 (*PLoS ONE*, SZTrack) | Per-electrode outputs (spread, onset zone), graph pooling (type) |
| #3 Brain-dynamics early-warning features | Duma 2025 (*BMC Med.*), Maturana 2020 (*Nat. Commun.*) | 1/f exponent, critical slowing, connectivity |
| Supporting | Jemal 2024, Meng 2025, Zabihi 2026, Karoly 2018, Sun 2024 (DeepSIF), Jeppesen 2025, Liu 2026 | Domain adaptation, k-of-n alarm, alarm-budget protocol, neural-mass modelling, ECG, small models |

---

## 2. Components

### Component 0 — Causal front-end
| Part | What it does | Based on |
|---|---|---|
| Montage | TUSZ → standard 22-channel TCP bipolar, resampled to 250 Hz; handles the 4 reference types (AR1, LE2, AR3, LE4) | MLSPred-Bench, Zabihi 2026 |
| **Causal** filters | IIR notch 60 Hz + 0.5–45 Hz, forward-only (no future samples) | Fixes non-causal filtering in Zabihi, Koutsouvelis |
| ECG extraction | EKG channel when present → R-peaks → heart rate | Jeppesen 2025 |
| **Artifact gate** | Small CNN trained on **TUAR** flags eye / muscle / electrode artifacts per channel; flagged channels are down-weighted, not deleted | Zabihi: artifacts cause most false alarms |
| **Two clocks** | FAST: 4-s windows every 1 s (onset). SLOW: 60-s windows every 10 s over the last 30 min (forecasting) | New: one model, two timescales |

### Component 1 — Neuro-dynamics feature bank ("brain-state tokens")
Per channel, on the slow stream, all causal.

| Feature group | What it captures | Evidence |
|---|---|---|
| **Aperiodic 1/f exponent + offset** (specparam) | Excitation/inhibition balance | Duma 2025 — rises ~13 min before seizures |
| Periodic band powers δ θ α β γ | Rhythm shifts | Duma (δ/θ rise), Zabihi (θ bursts) |
| **Critical slowing**: variance, lag-1 autocorrelation, decay time | Loss of stability | Maturana 2020, Chang 2018 |
| Interictal spike rate | Network irritability | Baud 2018 |
| Line length, Hjorth, entropy | Roughness / complexity | Zabihi top features |
| **Connectivity**: wPLI/PLV per band + directed in/out flow | Rising synchrony; which region drives others | Duma (outflow from epileptic zone), Khambhati 2024 |

Each feature is a **trajectory over time**; the model sees how fast it is changing.

### Component 2 — Neural-mass digital twin
```
OFFLINE:  Wendling model (pyramidal + excitatory + slow & fast inhibitory
          interneurons) → simulate ~200k signals over a wide range of A, B, G, a, b, g
          → train an amortized neural posterior estimator (sbi library)
          input: spectrum + 1/f + stats of one channel-window
          output: probability distribution over A, B, G, a, b, g

ONLINE:   every slow window, every channel → posterior in milliseconds
          → E/I indicators: A/(B+G), A/G, uncertainty width
          → "physiology tokens" for the fusion layer
          → drives the virtual-neuron simulation in the dashboard
```
- Interpretable brain parameters (Wendling 2002, Karoly 2018).
- Amortized simulation-based inference: train once, instant per window, runs live (SBI / VBI, DeepSIF idea).
- **Direction-agnostic**: learns whether E/I rises or falls before seizures (Duma found a shift toward inhibition).
- Uncertainty is kept as a signal.
- **Novel:** simulation-based neural-mass estimation on scalp EEG as a live forecasting input.

### Component 3 — Electrode-graph encoder
```
Fast window per electrode (4 s)
 → SHARED temporal CNN (EEGNet-style: frequency filters → features)    [SZTrack, Jemal]
 → node embedding h_i(t) for each of the 22 electrodes
 → DYNAMIC GRAPH: edges = learned + electrode distance + LIVE connectivity (wPLI)
 → 2 graph-attention layers                                              [Tang]
 → CAUSAL temporal model per node: selective state-space (Mamba-style) or GRU
                                                                          [fixes SZTrack BiLSTM]
 → per-node states + attention-pooled global state
```
- Per-electrode outputs → spread map, onset zone; works with fewer channels.
- **Graph rewires as synchrony rises** — the graph itself is an early-warning signal (new).
- Target size 1–3M parameters (Liu 2026: small specialists compete with foundation models).

### Component 4 — Neuro-guided fusion
- **Cross-attention:** each electrode's embedding attends to its own and its neighbours' brain-state + physiology tokens.
- **Gating:** learned trust between neuroscience and learned features (e.g. trust 1/f more under artifact).
- **Patient-baseline normalization:** features also expressed as z-scores against the patient's first calm minutes in the session (cheap test-time adaptation, new for TUSZ).
- **Domain-adversarial training** (DANN, Jemal 2024) so features don't encode patient identity.

### Component 5 — Multi-task heads
| Head | Output | Training signal | Novel? |
|---|---|---|---|
| **H1 Time-to-seizure** | Probability the seizure starts in 0–1, 1–2, 2–5, 5–10, 10–20, 20–30 min, or not within 30 min (discrete-time hazard) | TUSZ onset times; censoring where follow-up is short | ✅ "Seizure likely in ~X min" instead of yes/no preictal |
| **H2 Onset** | Per-second ictal probability | Soft labels across onset-crossing windows (Xu) | ✅ First cross-patient use on TUSZ |
| **H3 Per-electrode + spread forecast** | Seizure probability per electrode now; electrodes recruited in next 5/10 s; generalization risk | TUSZ channel-level annotations (to verify) | ✅ Spread forecast + numerical spread metric |
| **H4 Seizure type** | Focal/generalized → 4 classes (Tang) → 7 TUSZ types | Hierarchical focal loss, updated each second | Improves on Tang with neuro features |
| **H5 Body** | Measured: HR change, tachycardia onset, muscle power. Inferred: awareness, automatisms, convulsions | ECG features + type/spread → semiology table (labelled inferred) | ✅ No TUSZ paper uses its ECG |
| Uncertainty | Confidence per output | Ensemble / evidential + conformal | "Needs expert review" flag |

**Soft preictal ramp** (Xu's idea extended from seconds to minutes):
```
label
 1.0 |                                  ████ ictal
     |                           ▁▂▃▅▆▇█
 0.0 |▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▃▅          ← gradual rise, not a hard 0→1 step
     └──── interictal ──────┴── preictal ──┴── onset
```

### Component 6 — Cascaded alarm engine
```
Stage A: FORECAST ALARM
  hazard H1 → log-likelihood ratio → CUSUM accumulator (quickest change detection)
  + k-of-n confirmation + 30-min refractory period                          [Meng]
  → "⚠ Seizure likely in ~X min" + reasons

Stage B: ONSET ALARM
  onset prob H2 → accumulated rising evidence → alarm                        [Xu]
  CASCADE: if Stage A is active, Stage B's threshold is LOWERED (prior boost)  NEW

Calibration: thresholds tuned on TUSZ dev under an explicit false-alarm budget,
             then frozen                                                      [Zabihi]
             conformal risk control guarantees the FA budget                   NEW
```

### Component 7 — Explanation, report, dashboard
- Alarm explanation: contribution per feature group (1/f, slowing, connectivity, E/I parameters, learned graph) + graph-attention maps.
- Auto report (template-based, as in README §4.3).
- Dashboard: scalp topomap (MNE), 3D brain sources (MNE fsaverage + eLORETA), live network graph, **virtual neurons** (Wendling model simulated with the patient's inferred A/B/G), risk timeline.

### Component 8 — Tiny deployable model
- Knowledge distillation into a **4-channel student** (behind-the-ear montage, as SeizeIT2), target < 100k parameters, int8.
- Report MFLOPs per second of EEG → path to wearables and implants.

---

## 3. Training plan
| Stage | What trains | Data |
|---|---|---|
| S1 Offline twin | Wendling simulator → SBI posterior estimator | Simulations only |
| S2 Self-supervised pretraining | Graph encoder predicts next seconds + masked channels | TUSZ **train split only** |
| S3 Multi-task fine-tuning | Everything jointly | TUSZ train; selection on dev |
| S4 Calibration & distillation | Alarm thresholds, conformal budget, tiny student | TUSZ dev (then frozen) |

**Loss**
```
L = λ1·Hazard-NLL(H1) + λ2·SoftBCE(H2) + λ3·ChannelBCE(H3) + λ4·SpreadBCE(H3-forecast)
  + λ5·HierarchicalFocalCE(H4) + λ6·BodyMSE(H5)
  + λ7·DomainAdversarial + λ8·TemporalSmoothness
```

---

## 4. Novel contributions
| # | Contribution | Built on | Gap filled |
|---|---|---|---|
| N1 | Time-to-seizure hazard forecasting with soft preictal ramps | Xu, survival analysis | Nobody predicts "in how many minutes" |
| N2 | Neuro-guided dynamic electrode graph (edges = live connectivity, nodes carry E/I physiology) | Tang, SZTrack, Duma | No model mixes neuroscience markers into a graph network |
| N3 | Amortized neural-mass digital twin on scalp EEG as live forecasting input | Karoly, DeepSIF, SBI | Never done on scalp EEG / for forecasting |
| N4 | Cascaded forecast → onset alarm with CUSUM + conformal FA guarantee | Xu, Meng, Zabihi | Forecasting and detection always separate |
| N5 | Spread forecasting + first numerical spread metric on TUSZ | SZTrack | Spread only shown as pictures |
| N6 | Patient-baseline normalization + domain-adversarial training | Jemal | Cross-patient collapse |
| N7 | Per-seizure-type earliness + ECG body module on TUSZ | Zabihi's limitation | Not reported by anyone |
| N8 | Distilled 4-channel wearable/implant version | SeizeIT2, Liu | Links research to neurotech |

---

## 5. Targets vs previous results (to test, not promises)
| Metric (TUSZ eval, unseen patients) | Best previous | Target |
|---|---|---|
| Onset latency, median | ~8–16 s (Lee 2022, older TUSZ) | ≤ 5 s at matched false alarms |
| Detection sensitivity @ false alarms | 0.75 @ 0.68 FA/h (Zabihi 2026) | ≥ 0.75 @ ≤ 0.5 FA/h |
| Forecast | Window AUC 0.71–0.75, no warning time (MLSPred-Bench) | AUC ≥ 0.80; event sensitivity ≥ 60% @ ≤ 0.3 FA/h; median warning ≥ 5 min; beats random predictor |
| Seizure type (4-class wF1) | 0.749 (Tang 2022) | ≥ 0.77 |
| Spread / onset zone | 21/34 hemisphere+lobe (SZTrack, other data) | First TUSZ numbers + spread-forecast score |
| Short focal seizures | 33% detected (Zabihi) | Report per type and improve |

## 6. Ablation plan
Remove one at a time and measure warning time, latency, sensitivity, false alarms:
1. no neuro-dynamics bank · 2. no digital twin · 3. static instead of dynamic graph · 4. hard labels instead of soft ramps · 5. binary head instead of hazard head · 6. no cascade · 7. no patient-baseline normalization.

## 7. Risks
- **Short TUSZ sessions** cap the hazard head at ~30 min; many seizures have little preictal data. Check data first.
- **Per-electrode spread labels** depend on TUSZ v2 channel annotations — verify.
- **ECG** missing in some recordings — body module must degrade gracefully.
- **Digital twin** is the riskiest scientific bet; if E/I parameters add nothing, report it honestly.
- **Scope is large.** Build order: 0 → 3 → 1 → H2/H1 → alarm → 2 → H3–H5 → dashboard → tiny model.
