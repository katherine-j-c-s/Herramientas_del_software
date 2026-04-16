"""Ejercicio 02 — descarga e inspección inicial.

Responsable: Joaquín

CONSIGNA (resumen):
  - Descargar el dataset raw original y guardarlo en urban_flow/data/raw.
  - Mostrar las 5 primeras filas.
  - Analizar tipos de datos.
  - Contar los valores nulos.

Dataset:
  https://raw.githubusercontent.com/HAD141/datasets/refs/heads/main/
  TrabajosPracticos/urban_flow/speeding_fines.csv

LIBRERÍAS SUGERIDAS:
  pandas, urllib.request (o equivalente stdlib para descarga).

NOTAS:
  - El notebook integrador debe poder ejecutar run() y mostrar resultados
    (retornar DataFrame o imprimir según acuerden).
"""
from __future__ import annotations

import pandas as pd


_CSV_COLS = [
  "multa_id",
  "patente",
  "fecha",
  "hora",
  "velocidad_registrada",
  "velocidad_maxima",
  "ubicacion",
  "radar_id",
  "estado_multa",
]


def run() -> pd.DataFrame:
  """Implementar descarga, lectura y reportes; devolver df_raw."""
  return pd.DataFrame(columns=_CSV_COLS)
