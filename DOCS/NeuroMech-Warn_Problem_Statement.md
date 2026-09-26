# NeuroMech-Warn

**Earlier Than Ever: A Neuroscience-Grounded System for Forecasting, Classifying, and Understanding Epileptic Seizures Before They Strike**

Dataset: Temple University Hospital EEG Seizure Corpus (TUSZ)

---

## 1. The Problem

Epilepsy affects around 50 million people worldwide. The most dangerous part of epilepsy is that seizures strike without warning.

- Current AI systems mostly detect a seizure only **after** it has already begun, often seconds too late to act.
- On TUSZ, real-time systems alarm around **15 seconds after onset**, and the strongest recent models do not even report how early they detect.
- Prediction studies on TUSZ report only window-level accuracy (~70% sensitivity, ~60% specificity) with **no fair measure of warning time**.
- Most published prediction results (90–99%) come from patient-specific or leaky evaluations that do not hold for new patients.
- Existing systems act as **black boxes**: they say "seizure" but not what kind, where it started, how it spreads, what it will do to the body, or what is happening inside the brain.

---

## 2. Primary Objective

To **detect and forecast epileptic seizures EARLIER** than previous and recent state-of-the-art methods, measured as:

- **(a)** a **longer pre-onset warning time** (minutes before the seizure), and
- **(b)** a **shorter onset-detection latency** (seconds after the seizure begins),

on the TUSZ dataset under a fair, patient-independent evaluation, while keeping sensitivity equal or higher and false alarms equal or lower.

### Headline claim (to be proven)

> "On unseen patients, our system warns **X minutes** before seizure onset, compared with **Y minutes** for the best previous methods, at the same false-alarm rate and equal or higher sensitivity, and detects onset **Z seconds** earlier, across every seizure type."

### Benchmarks to beat

| Stage | Best previous result | What we must beat |
|---|---|---|
| Onset detection (TUSZ) | ~15 s latency (real-time systems); SeizureTransformer and 2026 TUSZ benchmarks report no latency | Earlier alarm at the same false alarms/24h |
| Onset detection (cross-patient reference, CHB-MIT / SWEC-ETHZ) | ~8–16 s latency | Match or beat on external test |
| Prediction (TUSZ) | MLSPred-Bench: ~70% sensitivity, ~60% specificity, AUC ~0.75–0.80, no warning time | Higher sensitivity at a longer, per-seizure warning time |
| Prediction (cross-patient reference, CHB-MIT 2026) | ~23 min lead, 74% sensitivity, 0.32 false alarms/hour | Longer or equal lead at ≤ 0.32 false alarms/hour |

All baselines are re-run under one identical, fair protocol.

---

## 3. Supporting Objectives

Each one either makes the system earlier or explains the early warning.

### 3.1 Forecast using the brain's hidden warning signs
Use neuroscience-based pre-seizure signals that previous deep learning methods ignore (critical slowing down, rising synchrony between regions, shifts in the 1/f spectral slope, interictal spike changes) to raise an alert minutes before onset. **This is the main source of "earlier."**

### 3.2 Reveal hidden neural dynamics (Neural Mass Digital Twin)
Scalp EEG reflects the summed activity of millions of neurons, so single neurons cannot be read directly. To bridge scalp voltage and neural activity, the project integrates biophysical neural mass models:

- **Jansen-Rit model:** pyramidal cells, excitatory interneurons and inhibitory interneurons, linked by sigmoid voltage-to-firing-rate and synaptic firing-rate-to-voltage transformations.
- **Wendling model:** its epilepsy-specific extension, adding fast and slow inhibition.

Using **simulation-based inference**, the system estimates, for every EEG window, the excitatory gain (**A**), slow inhibitory gain (**B**), fast inhibitory gain (**G**) and synaptic time constants (**a, b, g**), with uncertainty ranges. Tracking these over time shows how the excitation/inhibition balance shifts as the brain approaches a seizure, providing an additional early-warning signal and a scientific explanation of it.

### 3.3 Classify the seizure type at onset
Identify exactly what kind of seizure is occurring:

- **Level 1:** focal vs generalized
- **Level 2:** focal non-specific (FNSZ), generalized non-specific (GNSZ), complex partial (CPSZ), absence (ABSZ), tonic (TNSZ), tonic-clonic (TCSZ), and rarer types (SPSZ, MYSZ, ATSZ), with confidence.

Report how early each seizure type can be forecast, showing where the system is earliest and why some types are harder.

### 3.4 Map the spread: how other brain regions react
Find the onset zone, track which regions are recruited and in what order, which regions resist, and predict where the seizure will spread next and whether it will generalize. Catching the seizure while it is still local contributes to earlier detection.

### 3.5 Predict the body's reaction
Estimate how the body will respond, and quantify how much time the warning gives **before** physical symptoms appear.

- **Measured:** heart-rate change from the ECG channel; muscle activity from EEG.
- **Inferred:** awareness loss, staring, automatisms, stiffening or convulsions, from seizure type and spread.

Measured and inferred reactions are always clearly labelled.

### 3.6 Visualize the brain at every moment
A synchronized visual window into the brain along a timeline (**calm → warning signs → onset → spread → end**):

- live EEG and ECG
- 2D scalp activity map
- 3D brain surface showing estimated source activity
- brain-network graph of interacting regions and hubs
- **virtual neurons**: a simulated excitatory/inhibitory neural population (digital twin) driven by the patient's estimated parameters
- risk meter showing when and why the warning was raised

### 3.7 Explain and report every event
Auto-generate a complete seizure analysis report: warning timeline and reasons, warning time gained, seizure type, onset zone, spread path, body reaction, duration, seizure burden, status epilepticus risk, and an uncertainty flag for expert review.

### 3.8 Be trustworthy and deployable
Filter clinical artifacts (eye blinks, muscle, electrode noise) to keep false alarms low, which a fair earliness claim requires. Work on patients never seen before, run in real time, and demonstrate a tiny, few-channel version suitable for wearables and brain implants.

---

## 4. Fair Evaluation Principles

- **Patient-independent:** training and testing patients never overlap.
- Earliness is only claimed at **matched sensitivity and false-alarm rate**.
- Warning time and detection latency reported **per seizure, per type**.
- Performance compared against a **random / chance predictor**.
- Previous methods **re-evaluated on the same data and protocol**.
- Confirmed on a **second, external dataset**.

---

## 5. Who It Helps

- **Patients:** more minutes of warning to get safe, call for help, or take rescue medication, before symptoms begin.
- **Hospitals & doctors:** earlier ICU alarms, automatic seizure typing, onset localization, spread maps, and ready-made reports.
- **Neuroscience:** new evidence on how seizures build up, how excitation/inhibition changes before a seizure, and how each seizure type differs.
- **Neurotechnology** (Neuralink-style implants, wearables, closed-loop devices): a compact, early, explainable forecasting brain that could one day trigger preventive stimulation or medication before a seizure takes hold.

---

## 6. What Makes It Novel

- Aims to be **earlier than existing methods**, proven fairly on the same data at the same false-alarm rate.
- **First fair warning-time and latency comparison on TUSZ**, per seizure type.
- Combines neuroscience warning signs and **neural mass model (E/I) estimates** with AI, rather than a black-box classifier.
- Covers the **full seizure life cycle** (before, onset, spread, body) in one system.
- Offers a **visual window into the brain**, including a patient-driven digital twin of excitatory and inhibitory neural activity.
- Designed with a **path toward wearables and brain implants**.

---

## 7. Honest Scope

- Scalp EEG measures large neural populations, not individual neurons; neuron-level views are **model-based simulations driven by real EEG**.
- Forecasting targets **minutes ahead**, limited by TUSZ recording lengths.
- Body reactions beyond heart rate and muscle activity are **inferred**.
- Research prototype, **not a certified medical device**.

---

## 8. Expected Outcomes

- A seizure forecasting system that **warns earlier than previous methods** under fair evaluation.
- Seizure-type classification, spread mapping, body-reaction estimation, and full event reports.
- An interactive **brain visualization dashboard** with a neural digital twin.
- Scientific findings on pre-seizure brain dynamics and per-type warning times, contributing to **clinical AI, computational neuroscience, and neurotechnology**.
