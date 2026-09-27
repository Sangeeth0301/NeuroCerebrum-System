"""Timing helpers (profiling pipeline steps and real-time speed)."""

from __future__ import annotations

import time
from types import TracebackType

from neuromech.utils.logging import get_logger


class Timer:
    """Context manager that measures wall-clock time.

    Example:
        >>> with Timer("feature extraction") as t:
        ...     pass
        >>> t.elapsed >= 0
        True
    """

    def __init__(self, name: str = "block", log: bool = False) -> None:
        self.name = name
        self.log = log
        self.start: float | None = None
        self.elapsed: float = 0.0

    def __enter__(self) -> Timer:
        self.start = time.perf_counter()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        assert self.start is not None
        self.elapsed = time.perf_counter() - self.start
        if self.log:
            get_logger("neuromech.timing").info("%s took %.3f s", self.name, self.elapsed)


def realtime_factor(processing_seconds: float, signal_seconds: float) -> float:
    """Processing time divided by signal duration; < 1.0 means faster than real time."""
    if signal_seconds <= 0:
        raise ValueError("signal_seconds must be positive")
    return processing_seconds / signal_seconds
