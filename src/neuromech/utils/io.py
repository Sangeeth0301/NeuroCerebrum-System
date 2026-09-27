"""File input/output helpers.

Heavy formats (parquet, HDF5) import their libraries lazily so the core
package stays light; install the ``eeg`` extra to use them.
"""

from __future__ import annotations

import json
from collections.abc import Mapping
from pathlib import Path
from typing import Any

import numpy as np
import yaml

PathLike = str | Path


def ensure_dir(path: PathLike) -> Path:
    """Create ``path`` (and parents) if missing and return it as a Path."""
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def _parent(path: PathLike) -> Path:
    p = Path(path)
    ensure_dir(p.parent)
    return p


# ── JSON ──────────────────────────────────────────────────────────────────────
class _NumpyEncoder(json.JSONEncoder):
    """Serialise numpy scalars and arrays."""

    def default(self, o: Any) -> Any:
        if isinstance(o, np.integer):
            return int(o)
        if isinstance(o, np.floating):
            return float(o)
        if isinstance(o, np.ndarray):
            return o.tolist()
        if isinstance(o, Path):
            return str(o)
        return super().default(o)


def save_json(obj: Any, path: PathLike, indent: int = 2) -> Path:
    p = _parent(path)
    p.write_text(json.dumps(obj, indent=indent, cls=_NumpyEncoder), encoding="utf-8")
    return p


def load_json(path: PathLike) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


# ── YAML ──────────────────────────────────────────────────────────────────────
def save_yaml(obj: Mapping[str, Any], path: PathLike) -> Path:
    p = _parent(path)
    p.write_text(yaml.safe_dump(dict(obj), sort_keys=False), encoding="utf-8")
    return p


def load_yaml(path: PathLike) -> Any:
    return yaml.safe_load(Path(path).read_text(encoding="utf-8"))


# ── Plain text lists (e.g. splits/*.txt) ──────────────────────────────────────
def save_lines(lines: list[str], path: PathLike) -> Path:
    p = _parent(path)
    p.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return p


def load_lines(path: PathLike) -> list[str]:
    """Read non-empty lines, ignoring comments that start with '#'."""
    text = Path(path).read_text(encoding="utf-8")
    return [ln.strip() for ln in text.splitlines() if ln.strip() and not ln.startswith("#")]


# ── NumPy ─────────────────────────────────────────────────────────────────────
def save_npz(path: PathLike, **arrays: np.ndarray) -> Path:
    p = _parent(path)
    np.savez_compressed(p, **arrays)
    return p


def load_npz(path: PathLike) -> dict[str, np.ndarray]:
    with np.load(Path(path)) as data:
        return {k: data[k] for k in data.files}


# ── Parquet (pandas + pyarrow) ────────────────────────────────────────────────
def save_parquet(df: Any, path: PathLike) -> Path:
    p = _parent(path)
    df.to_parquet(p, index=False)
    return p


def load_parquet(path: PathLike) -> Any:
    import pandas as pd

    return pd.read_parquet(Path(path))


# ── HDF5 ──────────────────────────────────────────────────────────────────────
def save_hdf5(path: PathLike, **arrays: np.ndarray) -> Path:
    import h5py  # lazy: part of the "eeg" extra

    p = _parent(path)
    with h5py.File(p, "w") as f:
        for key, value in arrays.items():
            f.create_dataset(key, data=value, compression="gzip")
    return p


def load_hdf5(path: PathLike) -> dict[str, np.ndarray]:
    import h5py

    with h5py.File(Path(path), "r") as f:
        return {k: f[k][()] for k in f}
