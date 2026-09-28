"""TUSZ data access: EDF reading, annotation parsing, montage, audit and splits (phase P1)."""

from neuromech.data.annotations import (
    Annotation,
    Event,
    Seizure,
    annotation_paths,
    extract_seizures,
    read_annotation,
)
from neuromech.data.edf_reader import EDFHeader, EDFRecording, read_edf, read_edf_header, write_edf
from neuromech.data.montage import TCP_CHANNELS, TCPMontage, extract_ecg, to_tcp

__all__ = [
    "TCP_CHANNELS",
    "Annotation",
    "EDFHeader",
    "EDFRecording",
    "Event",
    "Seizure",
    "TCPMontage",
    "annotation_paths",
    "extract_ecg",
    "extract_seizures",
    "read_annotation",
    "read_edf",
    "read_edf_header",
    "to_tcp",
    "write_edf",
]
