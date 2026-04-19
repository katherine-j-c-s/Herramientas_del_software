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
from pathlib import Path
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

URL = "https://raw.githubusercontent.com/HAD141/datasets/refs/heads/main/TrabajosPracticos/urban_flow/speeding_fines.csv"

BASE_DIR = Path("urban_flow/data")
RAW_DIR = BASE_DIR / "raw"
FILE_PATH = RAW_DIR / "speeding_fines.csv"

def run() -> pd.DataFrame:
  """Implementar descarga, lectura y reportes; devolver df_raw."""
  # Crear carpeta si no existe
  RAW_DIR.mkdir(parents=True, exist_ok=True)

  # Descargar si no existe
  if not FILE_PATH.exists():
    df_tmp = pd.read_csv(URL)
    df_tmp.to_csv(FILE_PATH, index=False)

  df_raw = pd.read_csv(FILE_PATH)

  print("\nPrimeras 5 filas:")
  print(df_raw.head())

  print("\nTipos de datos:")
  print(df_raw.dtypes)

  print("\nValores nulos por columna:")
  print(df_raw.isnull().sum())

  return df_raw
