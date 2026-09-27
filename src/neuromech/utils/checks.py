"""Safety checks that protect the validity of the results.

Two rules the whole project depends on:

1. **Causality** – a real-time model may only use past and present samples.
2. **No leakage** – a patient may appear in only one data split.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable, Mapping

import numpy as np


class CausalityError(AssertionError):
    """Raised when an output depends on future input samples."""


class LeakageError(AssertionError):
    """Raised when the same patient appears in more than one split."""


def assert_causal(
    fn: Callable[[np.ndarray], np.ndarray],
    signal: np.ndarray,
    cut: int | None = None,
    atol: float = 1e-8,
    seed: int = 0,
) -> None:
    """Check that ``fn`` is causal along the last axis.

    The samples after ``cut`` are replaced with random noise. A causal
    function must return identical output up to ``cut``.

    Args:
        fn: maps an array ``(..., n_samples)`` to an array ``(..., n_samples)``.
        signal: test input.
        cut: index after which the future is perturbed (default: middle).
        atol: numerical tolerance.
        seed: RNG seed for the perturbation.

    Raises:
        CausalityError: if outputs before ``cut`` change.
    """
    x = np.asarray(signal, dtype=float)
    n = x.shape[-1]
    cut = n // 2 if cut is None else cut
    if not 0 < cut < n:
        raise ValueError(f"cut must be inside (0, {n}); got {cut}")

    rng = np.random.default_rng(seed)
    perturbed = x.copy()
    perturbed[..., cut:] = rng.normal(
        0.0, 10.0 * (np.std(x) + 1.0), size=perturbed[..., cut:].shape
    )

    y_ref = np.asarray(fn(x))[..., :cut]
    y_new = np.asarray(fn(perturbed))[..., :cut]
    if not np.allclose(y_ref, y_new, atol=atol):
        max_diff = float(np.max(np.abs(y_ref - y_new)))
        raise CausalityError(
            f"output before sample {cut} changed by up to {max_diff:.3g} "
            "when only future samples were modified"
        )


def assert_no_patient_overlap(splits: Mapping[str, Iterable[str]]) -> None:
    """Check that no patient ID appears in more than one split.

    Args:
        splits: e.g. ``{"train": [...], "dev_a": [...], "eval": [...]}``.

    Raises:
        LeakageError: listing every shared patient and the splits involved.
    """
    seen: dict[str, str] = {}
    clashes: list[str] = []
    for split_name, patients in splits.items():
        for pid in set(patients):
            if pid in seen and seen[pid] != split_name:
                clashes.append(f"{pid} ({seen[pid]} & {split_name})")
            else:
                seen[pid] = split_name
    if clashes:
        raise LeakageError("patients in more than one split: " + ", ".join(sorted(clashes)))
