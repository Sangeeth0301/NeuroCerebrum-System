# ref/ — reference papers

The PDFs are **not stored in this repository** (publisher copyright; the repository is public). Each researcher keeps a local copy in this folder; `ref/*.pdf` is git-ignored.

- **Summaries of all 47 papers:** [`research/papers/`](../research/papers/)
- **Literature review:** [`research/reports/`](../research/reports/)
- **Paywalled / manual-download papers:** [MISSING_PAPERS.md](MISSING_PAPERS.md)

## Open-access papers (30) — download and save with the file name shown

| Save as | Source |
|---|---|
| `2018_Baud_multidien_rhythms.pdf` | https://www.nature.com/articles/s41467-017-02577-y.pdf |
| `2018_Karoly_seizure_pathways.pdf` | https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1006403&type=printable |
| `2018_Shah_TUSZ_corpus.pdf` | https://www.frontiersin.org/journals/neuroinformatics/articles/10.3389/fninf.2018.00083/pdf |
| `2018_Truong_CNN_seizure_prediction.pdf` | https://arxiv.org/pdf/1707.01976 |
| `2019_Roy_seizure_type_benchmark_PREPRINT.pdf` | https://arxiv.org/pdf/1902.01012 |
| `2020_AhmedtAristizabal_neural_memory.pdf` | https://arxiv.org/pdf/1912.04968 |
| `2020_Asif_SeizureNet.pdf` | https://arxiv.org/pdf/1903.03232 |
| `2020_Maturana_critical_slowing.pdf` | https://www.nature.com/articles/s41467-020-15908-3.pdf |
| `2020_Saab_weak_supervision.pdf` | https://www.nature.com/articles/s41746-020-0264-0.pdf |
| `2021_Kostas_BENDR.pdf` | https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2021.653659/pdf |
| `2021_Stirling_wearable_forecasting.pdf` | https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2021.704060/pdf |
| `2022_Craley_SZTrack.pdf` | https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0264537&type=printable |
| `2022_Karacsony_video_semiology.pdf` | https://www.nature.com/articles/s41598-022-23133-9.pdf |
| `2022_Lee_realtime_detection_CHIL.pdf` | https://proceedings.mlr.press/v174/lee22a/lee22a.pdf |
| `2022_Tang_self_supervised_GNN_ICLR.pdf` | https://arxiv.org/pdf/2104.08336 |
| `2023_Xu_shorter_latency.pdf` | https://arxiv.org/pdf/2301.03465 |
| `2023_Yang_BIOT.pdf` | https://arxiv.org/pdf/2305.10351 |
| `2024_Jemal_domain_adaptation.pdf` | https://www.frontiersin.org/journals/neuroinformatics/articles/10.3389/fninf.2024.1303380/pdf |
| `2024_Jiang_LaBraM.pdf` | https://arxiv.org/pdf/2405.18765 |
| `2024_Koutsouvelis_preictal_period.pdf` | https://arxiv.org/pdf/2407.14876 |
| `2024_Wang_EEGPT_NeurIPS.pdf` | https://proceedings.neurips.cc/paper_files/paper/2024/file/4540d267eeec4e5dbd9dae9448f0b739-Paper-Conference.pdf |
| `2025_Dan_Seizure_Detection_Challenge_PREPRINT.pdf` | https://arxiv.org/pdf/2505.18191 |
| `2025_Duma_aperiodic_EI.pdf` | https://bmcmedicine.biomedcentral.com/counter/pdf/10.1186/s12916-025-04447-7.pdf |
| `2025_Kastrati_EEG-Bench.pdf` | https://tik-db.ee.ethz.ch/file/1e09e7f339cb0dfcf9ec74bd2bb51c24/ |
| `2025_Mohammad_MLSPred-Bench_bioRxiv.pdf` | https://www.biorxiv.org/content/10.1101/2024.07.17.604006v1.full.pdf |
| `2025_Wang_CBraMod.pdf` | https://arxiv.org/pdf/2412.07236 |
| `2025_Wu_SeizureTransformer_PREPRINT.pdf` | https://arxiv.org/pdf/2504.00336 |
| `2026_Chen_CG-MambaNet_PREPRINT.pdf` | https://arxiv.org/pdf/2606.08226 |
| `2026_Liu_EEG-FM-Compass.pdf` | https://arxiv.org/pdf/2601.17883 |
| `2026_Zabihi_TUSZ_CatBoost.pdf` | https://www.nature.com/articles/s41598-026-41358-w.pdf |

## Download them all at once

From the repository root (Git Bash / Linux / macOS):

```bash
while IFS='|' read -r _ name url _; do
  name=$(echo "$name" | tr -d ' `'); url=$(echo "$url" | tr -d ' ')
  [[ "$name" == *.pdf ]] && curl -sL -A "Mozilla/5.0" -o "ref/$name" "$url"
done < ref/README.md
```
