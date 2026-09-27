"""Reproducibility: seed every random number generator we use."""

from __future__ import annotations

import os
import random

import numpy as np


def set_seed(seed: int = 42, deterministic: bool = False) -> int:
    """Seed Python, NumPy and (if installed) PyTorch.

    Args:
        seed: the seed value.
        deterministic: also force deterministic cuDNN/PyTorch algorithms
            (slower, but bit-for-bit repeatable on the same hardware).

    Returns:
        The seed that was set.
    """
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)  # noqa: NPY002 - global state seeded on purpose for third-party code

    try:
        import torch
    except ImportError:
        return seed

    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    if deterministic:
        os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
        torch.use_deterministic_algorithms(True, warn_only=True)
    return seed


def make_rng(seed: int | None = None) -> np.random.Generator:
    """Return a NumPy Generator; prefer this over the global ``np.random`` state."""
    return np.random.default_rng(seed)
