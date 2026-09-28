"""Minimal, dependency-free EDF reader and writer.

TUSZ recordings are plain EDF files (European Data Format, 16-bit). This
module reads them with NumPy only, so it works in CI and on any machine:

- :func:`read_edf_header` reads just the header (fast; used by the audit).
- :func:`read_edf` reads all or selected channels, scaled to physical units.
- :func:`write_edf` writes synthetic recordings for tests and demos.

Channels may have different sampling rates (e.g. an ECG channel), so signals
are returned per channel together with their own rate.
"""

from __future__ import annotations

import datetime as _dt
from collections.abc import Sequence
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

_FIXED_HEADER_BYTES = 256
_SIGNAL_HEADER_BYTES = 256


class EDFError(ValueError):
    """Raised for malformed or unsupported EDF files."""


@dataclass(frozen=True)
class EDFHeader:
    """Header information of one EDF file."""

    path: Path
    patient: str
    recording: str
    start: _dt.datetime | None
    header_bytes: int
    n_records: int
    record_duration: float  # seconds
    labels: list[str]
    units: list[str]
    physical_min: np.ndarray
    physical_max: np.ndarray
    digital_min: np.ndarray
    digital_max: np.ndarray
    prefilter: list[str]
    samples_per_record: np.ndarray  # (n_signals,)

    @property
    def n_signals(self) -> int:
        return len(self.labels)

    @property
    def fs(self) -> np.ndarray:
        """Sampling rate of each signal in Hz."""
        return self.samples_per_record / self.record_duration

    @property
    def duration_s(self) -> float:
        return self.n_records * self.record_duration

    def index(self, label: str) -> int:
        """Index of a channel by exact (stripped) label."""
        try:
            return self.labels.index(label.strip())
        except ValueError as err:
            raise KeyError(f"channel {label!r} not in {self.path.name}") from err


@dataclass
class EDFRecording:
    """Signals of one EDF file, in physical units (usually microvolts)."""

    header: EDFHeader
    signals: dict[str, np.ndarray] = field(default_factory=dict)
    fs: dict[str, float] = field(default_factory=dict)

    @property
    def labels(self) -> list[str]:
        return list(self.signals)

    def stack(self, labels: Sequence[str] | None = None) -> tuple[np.ndarray, float]:
        """Stack channels that share one sampling rate into ``(n_channels, n_samples)``.

        Raises:
            EDFError: if the selected channels have different sampling rates.
        """
        labels = list(labels) if labels is not None else self.labels
        rates = {self.fs[lb] for lb in labels}
        if len(rates) != 1:
            raise EDFError(f"channels have different sampling rates: {sorted(rates)}")
        n = min(self.signals[lb].shape[0] for lb in labels)
        return np.stack([self.signals[lb][:n] for lb in labels]), rates.pop()


# ── reading ───────────────────────────────────────────────────────────────────
def _text(raw: bytes) -> str:
    return raw.decode("latin-1").strip()


def _num(raw: bytes, kind: type = float) -> float | int:
    txt = _text(raw)
    try:
        return kind(float(txt)) if kind is int else float(txt)
    except ValueError as err:
        raise EDFError(f"expected a number, got {txt!r}") from err


def _parse_start(date: str, time: str) -> _dt.datetime | None:
    try:
        d, m, y = (int(x) for x in date.split("."))
        hh, mm, ss = (int(x) for x in time.split("."))
        year = 2000 + y if y < 85 else 1900 + y
        return _dt.datetime(year, m, d, hh, mm, ss)
    except (ValueError, TypeError):
        return None  # anonymised or malformed dates are common; not fatal


def read_edf_header(path: str | Path) -> EDFHeader:
    """Read only the EDF header."""
    path = Path(path)
    with path.open("rb") as f:
        fixed = f.read(_FIXED_HEADER_BYTES)
        if len(fixed) < _FIXED_HEADER_BYTES:
            raise EDFError(f"{path.name}: file too short for an EDF header")
        ns = int(_num(fixed[252:256], int))
        if ns <= 0:
            raise EDFError(f"{path.name}: invalid number of signals ({ns})")
        sig = f.read(_SIGNAL_HEADER_BYTES * ns)
        if len(sig) < _SIGNAL_HEADER_BYTES * ns:
            raise EDFError(f"{path.name}: truncated signal header")

    def field_block(offset: int, width: int) -> list[bytes]:
        start = offset * ns
        return [sig[start + i * width : start + (i + 1) * width] for i in range(ns)]

    widths = [16, 80, 8, 8, 8, 8, 8, 80, 8, 32]
    offsets = np.concatenate([[0], np.cumsum(widths)[:-1]])
    blocks = [field_block(int(o), w) for o, w in zip(offsets, widths, strict=True)]
    labels, _transducer, units, pmin, pmax, dmin, dmax, prefilter, spr, _res = blocks

    header_bytes = int(_num(fixed[184:192], int))
    n_records = int(_num(fixed[236:244], int))
    record_duration = float(_num(fixed[244:252]))
    samples_per_record = np.array([int(_num(x, int)) for x in spr], dtype=np.int64)

    if n_records < 0:  # "-1" = unknown while recording; derive from file size
        data_bytes = path.stat().st_size - header_bytes
        n_records = data_bytes // (2 * int(samples_per_record.sum()))
    if record_duration <= 0:
        raise EDFError(f"{path.name}: invalid record duration ({record_duration})")

    return EDFHeader(
        path=path,
        patient=_text(fixed[8:88]),
        recording=_text(fixed[88:168]),
        start=_parse_start(_text(fixed[168:176]), _text(fixed[176:184])),
        header_bytes=header_bytes,
        n_records=n_records,
        record_duration=record_duration,
        labels=[_text(x) for x in labels],
        units=[_text(x) for x in units],
        physical_min=np.array([_num(x) for x in pmin]),
        physical_max=np.array([_num(x) for x in pmax]),
        digital_min=np.array([_num(x) for x in dmin]),
        digital_max=np.array([_num(x) for x in dmax]),
        prefilter=[_text(x) for x in prefilter],
        samples_per_record=samples_per_record,
    )


def read_edf(
    path: str | Path,
    channels: Sequence[str | int] | None = None,
    dtype: type = np.float32,
) -> EDFRecording:
    """Read an EDF file.

    Args:
        path: EDF file.
        channels: labels or indices to read (default: all).
        dtype: output dtype of the physical signals.

    Returns:
        :class:`EDFRecording` with one array per channel in physical units.
    """
    header = read_edf_header(path)
    if channels is None:
        idx = list(range(header.n_signals))
    else:
        idx = [c if isinstance(c, int) else header.index(c) for c in channels]

    record_len = int(header.samples_per_record.sum())
    raw = np.fromfile(
        header.path,
        dtype="<i2",
        count=header.n_records * record_len,
        offset=header.header_bytes,
    )
    n_complete = raw.size // record_len
    raw = raw[: n_complete * record_len].reshape(n_complete, record_len)
    starts = np.concatenate([[0], np.cumsum(header.samples_per_record)[:-1]])

    rec = EDFRecording(header=header)
    for i in idx:
        s0 = int(starts[i])
        s1 = s0 + int(header.samples_per_record[i])
        digital = raw[:, s0:s1].reshape(-1).astype(np.float64)
        dig_range = header.digital_max[i] - header.digital_min[i]
        if dig_range == 0:
            raise EDFError(f"{header.path.name}: zero digital range on {header.labels[i]!r}")
        gain = (header.physical_max[i] - header.physical_min[i]) / dig_range
        physical = (digital - header.digital_min[i]) * gain + header.physical_min[i]
        label = header.labels[i]
        rec.signals[label] = physical.astype(dtype)
        rec.fs[label] = float(header.fs[i])
    return rec


# ── writing (tests, synthetic demos) ──────────────────────────────────────────
def _field(value: object, width: int) -> bytes:
    text = str(value)
    if len(text) > width:
        text = text[:width]
    return text.ljust(width).encode("latin-1")


def _fmt(x: float) -> str:
    """Format a number to fit the 8-character EDF numeric field."""
    for fmt in ("{:.4f}", "{:.2f}", "{:.0f}"):
        s = fmt.format(x)
        if len(s) <= 8:
            return s
    raise EDFError(f"value {x} does not fit an EDF numeric field")


def write_edf(
    path: str | Path,
    signals: np.ndarray,
    fs: float,
    labels: Sequence[str],
    unit: str = "uV",
    patient: str = "X X X X",
    recording: str = "Startdate X X X X",
    start: _dt.datetime | None = None,
) -> Path:
    """Write a 16-bit EDF file with 1-second records.

    Args:
        path: output file.
        signals: ``(n_channels, n_samples)`` in physical units.
        fs: sampling rate in Hz (must be an integer number of samples per second).
        labels: channel labels, e.g. ``"EEG FP1-REF"``.
    """
    path = Path(path)
    x = np.atleast_2d(np.asarray(signals, dtype=np.float64))
    ns, n = x.shape
    if len(labels) != ns:
        raise ValueError("one label per channel is required")
    spr = int(round(fs))
    if abs(spr - fs) > 1e-9:
        raise ValueError("fs must be an integer for 1-second EDF records")

    n_records = int(np.ceil(n / spr))
    padded = np.zeros((ns, n_records * spr))
    padded[:, :n] = x

    pmin = padded.min(axis=1)
    pmax = padded.max(axis=1)
    flat = pmax == pmin
    pmin[flat] -= 1.0
    pmax[flat] += 1.0
    # Round outwards so the formatted limits still contain the data.
    pmin = np.floor(pmin * 100) / 100
    pmax = np.ceil(pmax * 100) / 100
    dmin, dmax = -32768, 32767
    gain = (pmax - pmin) / (dmax - dmin)
    digital = np.round((padded - pmin[:, None]) / gain[:, None] + dmin)
    digital = np.clip(digital, dmin, dmax).astype("<i2")

    start = start or _dt.datetime(2000, 1, 1)
    header_bytes = _FIXED_HEADER_BYTES + _SIGNAL_HEADER_BYTES * ns
    fixed = b"".join(
        [
            _field("0", 8),
            _field(patient, 80),
            _field(recording, 80),
            _field(start.strftime("%d.%m.%y"), 8),
            _field(start.strftime("%H.%M.%S"), 8),
            _field(header_bytes, 8),
            _field("", 44),
            _field(n_records, 8),
            _field(1, 8),
            _field(ns, 4),
        ]
    )
    per_signal = [
        [_field(lb, 16) for lb in labels],
        [_field("", 80)] * ns,
        [_field(unit, 8)] * ns,
        [_field(_fmt(v), 8) for v in pmin],
        [_field(_fmt(v), 8) for v in pmax],
        [_field(dmin, 8)] * ns,
        [_field(dmax, 8)] * ns,
        [_field("", 80)] * ns,
        [_field(spr, 8)] * ns,
        [_field("", 32)] * ns,
    ]
    sig_header = b"".join(b"".join(col) for col in per_signal)

    # Records: for each second, every channel's block of spr samples.
    body = digital.reshape(ns, n_records, spr).transpose(1, 0, 2).tobytes()

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(fixed + sig_header + body)
    return path
