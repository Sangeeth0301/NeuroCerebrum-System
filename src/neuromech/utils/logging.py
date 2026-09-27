"""Consistent console/file logging for scripts and modules."""

from __future__ import annotations

import logging
import sys
from pathlib import Path

_FORMAT = "%(asctime)s | %(levelname)-7s | %(name)s | %(message)s"
_DATEFMT = "%Y-%m-%d %H:%M:%S"


def get_logger(
    name: str = "neuromech",
    level: int | str = logging.INFO,
    log_file: str | Path | None = None,
) -> logging.Logger:
    """Return a configured logger.

    Handlers are added once per logger name, so repeated calls are safe.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False

    if not any(isinstance(h, logging.StreamHandler) for h in logger.handlers):
        stream = logging.StreamHandler(sys.stdout)
        stream.setFormatter(logging.Formatter(_FORMAT, _DATEFMT))
        logger.addHandler(stream)

    if log_file is not None:
        path = Path(log_file)
        path.parent.mkdir(parents=True, exist_ok=True)
        if not any(
            isinstance(h, logging.FileHandler) and Path(h.baseFilename) == path.resolve()
            for h in logger.handlers
        ):
            fh = logging.FileHandler(path, encoding="utf-8")
            fh.setFormatter(logging.Formatter(_FORMAT, _DATEFMT))
            logger.addHandler(fh)

    return logger
