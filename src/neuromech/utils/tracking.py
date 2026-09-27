"""Experiment tracking.

Uses MLflow when it is installed (the ``track`` extra); otherwise writes
parameters and metrics to a local JSON file so runs are never lost.
"""

from __future__ import annotations

import json
import time
from collections.abc import Mapping
from pathlib import Path
from typing import Any


class Tracker:
    """Minimal tracker with the same calls for MLflow and local JSON."""

    def __init__(
        self,
        experiment: str,
        run_name: str | None = None,
        output_dir: str | Path = "outputs/logs",
        use_mlflow: bool = True,
    ) -> None:
        self.experiment = experiment
        self.run_name = run_name or time.strftime("%Y%m%d-%H%M%S")
        self._mlflow: Any = None
        self._record: dict[str, Any] = {"params": {}, "metrics": {}, "tags": {}}
        self._path = Path(output_dir) / experiment / f"{self.run_name}.json"

        if use_mlflow:
            try:
                import mlflow
            except ImportError:
                mlflow = None
            if mlflow is not None:
                mlflow.set_experiment(experiment)
                mlflow.start_run(run_name=self.run_name)
                self._mlflow = mlflow

    @property
    def backend(self) -> str:
        return "mlflow" if self._mlflow is not None else "json"

    def log_params(self, params: Mapping[str, Any]) -> None:
        self._record["params"].update(params)
        if self._mlflow:
            self._mlflow.log_params({k: str(v) for k, v in params.items()})

    def log_metrics(self, metrics: Mapping[str, float], step: int | None = None) -> None:
        for key, value in metrics.items():
            self._record["metrics"].setdefault(key, []).append(
                {"step": step, "value": float(value)}
            )
        if self._mlflow:
            self._mlflow.log_metrics({k: float(v) for k, v in metrics.items()}, step=step)

    def set_tags(self, tags: Mapping[str, str]) -> None:
        self._record["tags"].update(tags)
        if self._mlflow:
            self._mlflow.set_tags(dict(tags))

    def finish(self) -> Path:
        """Close the run and write the local JSON record (always written)."""
        self._path.parent.mkdir(parents=True, exist_ok=True)
        self._path.write_text(json.dumps(self._record, indent=2), encoding="utf-8")
        if self._mlflow:
            self._mlflow.end_run()
        return self._path

    def __enter__(self) -> Tracker:
        return self

    def __exit__(self, *exc: object) -> None:
        self.finish()
