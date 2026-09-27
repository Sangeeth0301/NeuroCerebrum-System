# Data

NeuroMech-Warn uses public research EEG corpora. **None of the data is stored in this repository**, and none may be uploaded to it. `.gitignore` and a pre-commit hook block EEG files.

| Dataset | Role | Access | Approx. size |
|---|---|---|---|
| **TUSZ** — TUH EEG Seizure Corpus v2.0.x | Primary train / dev / eval | Free, signed data use agreement (NEDC) | ~80 GB (check the NEDC page for the current release) |
| **TUAR** — TUH EEG Artifact Corpus | Artifact gate (P4) | Same agreement as TUSZ | ~5 GB |
| **CHB-MIT** Scalp EEG | External test, long recordings (P9) | Open (PhysioNet) | ~43 GB |
| **Siena** Scalp EEG | External adult test (P9) | Open (PhysioNet) | ~20 GB |

> Store the datasets on a drive with enough space. On the project laptop they live on the external drive **E: (Yesh SSD)**, not on C:.

---

## 1. Request TUSZ and TUAR access (Temple University, NEDC)

1. Open the Neural Engineering Data Consortium site: <https://isip.piconepress.com/projects/nedc/html/tuh_eeg/>
2. Download the **data use agreement** form linked on that page.
3. Fill it in (name, institution, supervisor, intended research use) and sign it. Request **TUSZ (tuh_eeg_seizure)** and **TUAR (tuh_eeg_artifact)**.
4. Email it as instructed on the page. Approval usually takes a few days.
5. You receive a **username and password** for the download server.

The agreement forbids redistribution. Never commit, share or upload the files, and never publish anything that could identify a patient.

## 2. Download TUSZ onto the external drive

The NEDC server supports `rsync` over SSH (Git Bash, WSL or Linux/macOS). With the credentials you receive:

```bash
mkdir -p /e/tusz
rsync -auxvL --delete nedc-tuh-eeg@www.isip.piconepress.com:data/tuh_eeg/tuh_eeg_seizure/v2.0.3/ /e/tusz/
```

- Replace `v2.0.3` with the release offered to you (this project expects **v2.0.x**).
- In WSL the drive is `/mnt/e/tusz` instead of `/e/tusz`.
- The server path is also given in the approval email; if it differs, use that one.
- `rsync` can be re-run to resume an interrupted download.

TUAR is downloaded the same way into `/e/tuar/`.

## 3. Expected TUSZ v2 layout

```
E:/tusz/
├── DOCS/                       release notes, montage definitions, annotation spec
└── edf/
    ├── train/
    │   └── aaaaaaac/                       patient ID
    │       └── s001_2002/                  session (number_year)
    │           └── 02_tcp_le/              montage type
    │               ├── aaaaaaac_s001_t000.edf      EEG recording
    │               ├── aaaaaaac_s001_t000.csv      per-channel seizure labels
    │               └── aaaaaaac_s001_t000.csv_bi   whole-recording labels (seiz / bckg)
    ├── dev/
    └── eval/
```

Montage folders: `01_tcp_ar` (averaged reference), `02_tcp_le` (linked ears), `03_tcp_ar_a` (averaged reference without A1/A2), `04_tcp_le_a` (linked ears without A1/A2). `neuromech.data.montage` converts all of them to the same 22-channel TCP bipolar montage (20 channels + a mask when A1/A2 are absent).

Annotation files are CSV with `#` header lines followed by `channel,start_time,stop_time,label,confidence`. Seizure labels: `fnsz, gnsz, spsz, cpsz, absz, tnsz, cnsz, tcsz, atsz, mysz` (and `seiz` in `.csv_bi`); everything else is background.

## 4. Point the project at the data

Copy `.env.example` to `.env` and set:

```
TUSZ_ROOT=E:/tusz
TUAR_ROOT=E:/tuar
CHBMIT_ROOT=E:/chbmit
SIENA_ROOT=E:/siena
```

Large pipeline products can also live on the external drive; set `OUTPUT_ROOT=E:/neuromech_outputs` if C: is short on space.

## 5. Run the audit and build the splits (P1)

```bash
make audit      # python scripts/00_audit_tusz.py   -> DOCS/DATA_AUDIT.md + data/processed/metadata.parquet
make splits     # python scripts/01_make_splits.py  -> splits/*.txt
```

The audit reports recordings, patients, hours, seizure types, per-channel label coverage, ECG availability and how much EEG precedes each seizure (which sets the forecasting horizons).

## 6. External datasets (P9)

```bash
# CHB-MIT
wget -r -N -c -np -P /e/chbmit https://physionet.org/files/chbmit/1.0.0/
# Siena Scalp EEG
wget -r -N -c -np -P /e/siena https://physionet.org/files/siena-scalp-eeg/1.0.0/
```

## Citation

If you use TUSZ, cite: V. Shah et al., "The Temple University Hospital Seizure Detection Corpus," *Frontiers in Neuroinformatics*, 12:83, 2018. doi:10.3389/fninf.2018.00083
