"""TUSZ data access: EDF reading, annotation parsing, montage, audit and splits (phase P1)."""

from neuromech.data.edf_reader import EDFHeader, EDFRecording, read_edf, read_edf_header, write_edf

__all__ = ["EDFHeader", "EDFRecording", "read_edf", "read_edf_header", "write_edf"]
