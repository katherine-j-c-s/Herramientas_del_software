"""Ejercicio 03 — limpieza con Pandas.

Responsable: Emi

CONSIGNA (resumen):
  - Fechas a formato YYYY-MM-DD; inválidas → 1932-01-01. Mostrar 10 primeras.
  - Horas a formato 24 h; inválidas → 00:00. Mostrar 10 primeras.
  - Ubicaciones: quitar caracteres especiales, mayúsculas. Mostrar 10
    primeras.
  - Patentes: limpiar, mayúsculas; error → pd.NA. Mostrar 10 últimas.
  - Eliminar filas con datos relevantes vacíos (mensaje con cantidad y
    columnas según leyenda del enunciado).
  - Detectar y eliminar outliers (mensaje con cantidad y columnas).
  - Columna exceso_velocidad_real = velocidad_registrada - velocidad_maxima.
    Mostrar 10 patentes y exceso real.
  - Columna exceso_velocidad = velocidad_registrada - velocidad_maxima
    más 5 % de la velocidad máxima. Mostrar 10 patentes y exceso.
  - Eliminar filas sin infracción según exceso_velocidad (mensaje).
  - Guardar CSV en urban_flow/data/interim/speeding_fines.csv

LIBRERÍAS SUGERIDAS:
  pandas, numpy, re (regex).

NOTAS:
  - Coordinar con Joaquín la entrada (df o path al raw).
"""
from __future__ import annotations

import pandas as pd


def run(df: pd.DataFrame | None = None) -> pd.DataFrame:
  """Implementar pipeline de limpieza; devolver df limpio."""
  from urban_flow import ejercicio_02

  if df is None or df.empty:
    return pd.DataFrame(columns=ejercicio_02._CSV_COLS)
  return df.copy()
