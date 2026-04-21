"""Punto 06 — porcentajes.

Responsable: Joaquín

CONSIGNA (resumen):
  - Porcentaje de infracciones en la fecha 1932-01-01:
    "El porcentaje de infracciones en la fecha 1932-01-01 es XX.XX%"
  - Porcentaje de infracciones en la hora 00:00:
    "El porcentaje de infracciones a la hora 00:00 es XX.XX%"

LIBRERÍAS SUGERIDAS:
  pandas.

NOTAS:
  - Usar el dataset ya limpio / filtrado como indique el enunciado.
"""
from __future__ import annotations

import pandas as pd


def run(df: pd.DataFrame) -> None:
  """Calcula porcentajes de datos corregidos."""

  total = len(df)

  # Porcentaje fechas inválidas corregidas
  fechas_invalidas = (df["fecha"] == "1932-01-01").sum()
  porcentaje_fechas = (fechas_invalidas / total) * 100

  # Porcentaje horas inválidas corregidas
  horas_invalidas = (df["hora"] == "00:00").sum()
  porcentaje_horas = (horas_invalidas / total) * 100

  print(f"Porcentaje de fechas inválidas: {porcentaje_fechas:.2f}%")
  print(f"Porcentaje de horas inválidas: {porcentaje_horas:.2f}%")