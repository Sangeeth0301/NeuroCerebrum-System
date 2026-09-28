"""TUSZ v2 annotation files.

Each EDF recording ``<name>.edf`` has two CSV annotation files:

- ``<name>.csv``    per-channel events: ``channel`` is a TCP pair such as ``FP1-F7``.
- ``<name>.csv_bi`` whole-recording events: ``channel`` is ``TERM``, labels ``seiz`` / ``bckg``.

Both start with ``#`` metadata lines followed by the columns
``channel,start_time,stop_time,label,confidence`` (times in seconds).

This module parses them and turns per-channel events into :class:`Seizure`
objects with onset, offset, type, involved channels and onset channels.
"""

from __future__ import annotations

import re
from collections import Counter
from collections.abc import Iterable, Sequence
from dataclasses import dataclass, field
from pathlib import Path

SEIZURE_LABELS: frozenset[str] = frozenset(
    {"seiz", "fnsz", "gnsz", "spsz", "cpsz", "absz", "tnsz", "cnsz", "tcsz", "atsz", "mysz"}
)
FOCAL_LABELS: frozenset[str] = frozenset({"fnsz", "spsz", "cpsz"})
GENERALIZED_LABELS: frozenset[str] = frozenset(
    {"gnsz", "absz", "tnsz", "cnsz", "tcsz", "atsz", "mysz"}
)
FOUR_CLASS: dict[str, str] = {
    "fnsz": "CF", "spsz": "CF", "cpsz": "CF",
    "gnsz": "GN",
    "absz": "AB",
    "tnsz": "CT", "tcsz": "CT", "cnsz": "CT",
}  # fmt: skip

TERM_CHANNEL = "TERM"
_COLUMNS = ["channel", "start_time", "stop_time", "label", "confidence"]


class AnnotationError(ValueError):
    """Raised for malformed annotation files."""


@dataclass(frozen=True)
class Event:
    """One annotated interval on one channel (or on ``TERM``)."""

    channel: str
    start: float
    stop: float
    label: str
    confidence: float = 1.0

    @property
    def duration(self) -> float:
        return self.stop - self.start

    def is_seizure(self, seizure_labels: Iterable[str] = SEIZURE_LABELS) -> bool:
        return self.label in set(seizure_labels)


@dataclass
class Annotation:
    """Contents of one ``.csv`` or ``.csv_bi`` file."""

    path: Path
    kind: str  # "channel" or "term"
    meta: dict[str, str] = field(default_factory=dict)
    events: list[Event] = field(default_factory=list)

    @property
    def duration_s(self) -> float | None:
        raw = self.meta.get("duration")
        if raw is None:
            return None
        match = re.search(r"[-+]?\d*\.?\d+", raw)
        return float(match.group()) if match else None

    @property
    def channels(self) -> list[str]:
        return sorted({e.channel for e in self.events})

    def seizure_events(self, seizure_labels: Iterable[str] = SEIZURE_LABELS) -> list[Event]:
        labels = set(seizure_labels)
        return [e for e in self.events if e.label in labels]


@dataclass
class Seizure:
    """One seizure built from annotation events."""

    onset: float
    offset: float
    label: str  # dominant seizure type, e.g. "fnsz"
    channels: dict[str, tuple[float, float]] = field(default_factory=dict)
    onset_channels: list[str] = field(default_factory=list)

    @property
    def duration(self) -> float:
        return self.offset - self.onset

    @property
    def group(self) -> str:
        """``focal``, ``generalized`` or ``unknown``."""
        if self.label in FOCAL_LABELS:
            return "focal"
        if self.label in GENERALIZED_LABELS:
            return "generalized"
        return "unknown"

    @property
    def four_class(self) -> str | None:
        """Tang et al. (2022) 4-class label, or ``None`` for rare types."""
        return FOUR_CLASS.get(self.label)


# ── parsing ──────────────────────────────────────────────────────────────────
def read_annotation(path: str | Path) -> Annotation:
    """Parse a TUSZ ``.csv`` / ``.csv_bi`` annotation file."""
    path = Path(path)
    kind = "term" if path.suffix == ".csv_bi" else "channel"
    ann = Annotation(path=path, kind=kind)
    header_seen = False

    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw.strip()
        if not line:
            continue
        if line.startswith("#"):
            key, sep, value = line.lstrip("#").partition("=")
            if sep:
                ann.meta[key.strip()] = value.strip()
            continue
        parts = [p.strip() for p in line.split(",")]
        if not header_seen:
            if [p.lower() for p in parts[:5]] != _COLUMNS:
                raise AnnotationError(f"{path.name}:{lineno}: unexpected header {parts}")
            header_seen = True
            continue
        if len(parts) < 4:
            raise AnnotationError(f"{path.name}:{lineno}: expected 5 columns, got {parts}")
        try:
            start, stop = float(parts[1]), float(parts[2])
            confidence = float(parts[4]) if len(parts) > 4 and parts[4] else 1.0
        except ValueError as err:
            raise AnnotationError(f"{path.name}:{lineno}: bad number in {parts}") from err
        if stop < start:
            raise AnnotationError(f"{path.name}:{lineno}: stop before start")
        ann.events.append(Event(parts[0].upper(), start, stop, parts[3].lower(), confidence))

    if not header_seen:
        raise AnnotationError(f"{path.name}: no column header found")
    return ann


def annotation_paths(edf_path: str | Path) -> dict[str, Path | None]:
    """Return the ``.csv`` and ``.csv_bi`` files next to an EDF (``None`` if missing)."""
    edf_path = Path(edf_path)
    out: dict[str, Path | None] = {}
    for kind, suffix in (("channel", ".csv"), ("term", ".csv_bi")):
        candidate = edf_path.with_suffix(suffix)
        out[kind] = candidate if candidate.exists() else None
    return out


# ── seizures ─────────────────────────────────────────────────────────────────
def _merge_intervals(events: Sequence[Event], gap: float) -> list[list[Event]]:
    """Group events whose intervals overlap or are closer than ``gap`` seconds."""
    groups: list[list[Event]] = []
    end = float("-inf")
    for ev in sorted(events, key=lambda e: e.start):
        if groups and ev.start <= end + gap:
            groups[-1].append(ev)
            end = max(end, ev.stop)
        else:
            groups.append([ev])
            end = ev.stop
    return groups


def _dominant_label(events: Sequence[Event]) -> str:
    """Most time-weighted specific type; the generic ``seiz`` only if nothing else."""
    weights: Counter[str] = Counter()
    for ev in events:
        weights[ev.label] += ev.duration
    specific = {k: v for k, v in weights.items() if k != "seiz"}
    pool = specific or weights
    return max(sorted(pool), key=lambda k: pool[k])


def extract_seizures(
    annotation: Annotation,
    merge_gap: float = 0.0,
    onset_tolerance: float = 1.0,
    seizure_labels: Iterable[str] = SEIZURE_LABELS,
) -> list[Seizure]:
    """Turn annotation events into seizures.

    Args:
        annotation: parsed ``.csv`` (per channel) or ``.csv_bi`` (TERM) file.
        merge_gap: events closer than this (seconds) belong to the same seizure.
        onset_tolerance: channels starting within this many seconds of the
            earliest channel are reported as onset channels.
        seizure_labels: labels that count as seizure.

    Returns:
        Seizures sorted by onset.
    """
    events = annotation.seizure_events(seizure_labels)
    seizures: list[Seizure] = []
    for group in _merge_intervals(events, merge_gap):
        onset = min(e.start for e in group)
        offset = max(e.stop for e in group)
        per_channel: dict[str, tuple[float, float]] = {}
        for ev in group:
            if ev.channel == TERM_CHANNEL:
                continue
            s, t = per_channel.get(ev.channel, (ev.start, ev.stop))
            per_channel[ev.channel] = (min(s, ev.start), max(t, ev.stop))
        first = min((s for s, _ in per_channel.values()), default=onset)
        onset_channels = sorted(
            ch for ch, (s, _) in per_channel.items() if s <= first + onset_tolerance
        )
        seizures.append(
            Seizure(
                onset=onset,
                offset=offset,
                label=_dominant_label(group),
                channels=dict(sorted(per_channel.items())),
                onset_channels=onset_channels,
            )
        )
    return seizures


# ── writing (tests, synthetic demos) ─────────────────────────────────────────
def write_annotation(
    path: str | Path,
    events: Iterable[Event],
    duration_s: float,
    bname: str | None = None,
) -> Path:
    """Write events in the TUSZ v2 CSV format."""
    path = Path(path)
    lines = [
        "# version = csv_v1.0.0",
        f"# bname = {bname or path.stem}",
        f"# duration = {duration_s:.2f} secs",
        "#",
        ",".join(_COLUMNS),
    ]
    lines += [
        f"{e.channel},{e.start:.4f},{e.stop:.4f},{e.label},{e.confidence:.4f}" for e in events
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path
