"""Rutas y constantes compartidas entre ejercicios.

Usado por varios módulos; ``INTERIM_CSV`` y ``PLOTS_DIR`` son los que usa el
Punto 05 para leer datos y guardar los ``.jpg``.
"""
from __future__ import annotations

from pathlib import Path

_PAQUETE = Path(__file__).resolve().parent
DATA = _PAQUETE / "data"
RAW_DIR = DATA / "raw"
INTERIM_DIR = DATA / "interim"
PROCESSED_DIR = DATA / "processed"
PLOTS_DIR = INTERIM_DIR / "plots"

DATASET_URL = (
  "https://raw.githubusercontent.com/HAD141/datasets/"
  "refs/heads/main/TrabajosPracticos/urban_flow/speeding_fines.csv"
)
RAW_CSV = RAW_DIR / "speeding_fines.csv"
INTERIM_CSV = INTERIM_DIR / "speeding_fines.csv"
