"""Ejercicio 03 — limpieza con Pandas.

Responsable: Emi

CONSIGNA (resumen):
  - Fechas a formato YYYY-MM-DD; inválidas → 1932-01-01. Mostrar 10 primeras.
  - Horas a formato 24 h; inválidas → 00:00. Mostrar 10 primeras.
  - Ubicaciones: quitar caracteres especiales, mayúsculas. Mostrar 10
    primeras.
  - Patentes: limpiar, mayúsculas; error → pd.NA. Mostrar 10 últimas.
  - Eliminar filas con datos relevantes vacíos.
  - Detectar y eliminar outliers.
  - Columna exceso_velocidad_real = velocidad_registrada - velocidad_maxima.
  - Columna exceso_velocidad = velocidad_registrada - velocidad_maxima
    menos el 5 % de la velocidad máxima.
  - Eliminar filas sin infracción según exceso_velocidad.
  - Guardar CSV en urban_flow/data/interim/speeding_fines.csv
"""
from __future__ import annotations

from pathlib import Path
import re

import pandas as pd


BASE_DIR = Path("urban_flow/data")
RAW_DIR = BASE_DIR / "raw"
INTERIM_DIR = BASE_DIR / "interim"
RAW_FILE = RAW_DIR / "speeding_fines.csv"
INTERIM_FILE = INTERIM_DIR / "speeding_fines.csv"

RELEVANT_COLS = [
  "fecha",
  "hora",
  "ubicacion",
  "patente",
  "velocidad_registrada",
  "velocidad_maxima",
]


def run(df: pd.DataFrame | None = None) -> pd.DataFrame:
  """Limpia el dataset y devuelve un DataFrame procesado."""
  if df is None or df.empty:
    if not RAW_FILE.exists():
      print("No se recibió DataFrame y no existe el archivo raw.")
      return pd.DataFrame()
    df = pd.read_csv(RAW_FILE)

  df_clean = df.copy()

  df_clean["fecha"] = df_clean["fecha"].apply(_limpiar_fecha)
  df_clean["hora"] = df_clean["hora"].apply(_limpiar_hora)
  df_clean["ubicacion"] = df_clean["ubicacion"].apply(_limpiar_ubicacion)
  df_clean["patente"] = df_clean["patente"].apply(_limpiar_patente)

  print("\nPrimeras 10 fechas limpias:")
  print(df_clean["fecha"].head(10))

  print("\nPrimeras 10 horas limpias:")
  print(df_clean["hora"].head(10))

  print("\nPrimeras 10 ubicaciones limpias:")
  print(df_clean["ubicacion"].head(10))

  print("\nÚltimas 10 patentes limpias:")
  print(df_clean["patente"].tail(10))

  df_clean["velocidad_registrada"] = pd.to_numeric(
    df_clean["velocidad_registrada"],
    errors="coerce",
  )
  df_clean["velocidad_maxima"] = pd.to_numeric(
    df_clean["velocidad_maxima"],
    errors="coerce",
  )

  antes_vacios = len(df_clean)
  df_clean["ubicacion"] = df_clean["ubicacion"].replace("", pd.NA)
  df_clean = df_clean.dropna(subset=RELEVANT_COLS)
  eliminadas_vacios = antes_vacios - len(df_clean)

  print("\nFilas eliminadas por datos relevantes vacíos:", eliminadas_vacios)
  print("Columnas revisadas:", RELEVANT_COLS)

  antes_outliers = len(df_clean)
  df_clean = df_clean[
    (df_clean["velocidad_registrada"] > 0)
    & (df_clean["velocidad_registrada"] <= 300)
    & (df_clean["velocidad_maxima"] > 0)
    & (df_clean["velocidad_maxima"] <= 200)
  ].copy()
  eliminadas_outliers = antes_outliers - len(df_clean)

  print("\nFilas eliminadas por outliers:", eliminadas_outliers)
  print("Columnas revisadas: velocidad_registrada, velocidad_maxima")

  df_clean["exceso_velocidad_real"] = (
    df_clean["velocidad_registrada"] - df_clean["velocidad_maxima"]
  )

  df_clean["exceso_velocidad"] = (
    df_clean["velocidad_registrada"]
    - df_clean["velocidad_maxima"]
    - (df_clean["velocidad_maxima"] * 0.05)
  )

  print("\n10 patentes y exceso_velocidad_real:")
  print(df_clean[["patente", "exceso_velocidad_real"]].head(10))

  print("\n10 patentes y exceso_velocidad:")
  print(df_clean[["patente", "exceso_velocidad"]].head(10))

  antes_infraccion = len(df_clean)
  df_clean = df_clean[df_clean["exceso_velocidad"] > 0].copy()
  eliminadas_sin_infraccion = antes_infraccion - len(df_clean)

  print(
    "\nFilas eliminadas por no constituir infracción:",
    eliminadas_sin_infraccion,
  )

  INTERIM_DIR.mkdir(parents=True, exist_ok=True)
  df_clean.to_csv(INTERIM_FILE, index=False)

  print("\nArchivo guardado en:", INTERIM_FILE)

  return df_clean


def _limpiar_fecha(value: object) -> str:
  """Convierte fechas inválidas a 1932-01-01 y válidas a YYYY-MM-DD."""
  parsed = pd.to_datetime(value, errors="coerce", format="mixed")
  if pd.isna(parsed):
    return "1932-01-01"
  return parsed.strftime("%Y-%m-%d")


def _limpiar_hora(value: object) -> str:
  """Convierte horas inválidas a 00:00 y válidas a formato 24 h."""
  parsed = pd.to_datetime(value, errors="coerce")
  if pd.isna(parsed):
    return "00:00"
  return parsed.strftime("%H:%M")


def _limpiar_ubicacion(value: object) -> str:
  """Quita caracteres especiales y pasa el texto a mayúsculas."""
  if pd.isna(value):
    return ""
  text = str(value).upper().strip()
  text = re.sub(r"[^A-Z0-9\s]", "", text)
  text = re.sub(r"\s+", " ", text).strip()
  return text


def _limpiar_patente(value: object) -> object:
  """Limpia patentes y devuelve pd.NA si queda inválida."""
  if pd.isna(value):
    return pd.NA

  text = str(value).upper().strip()
  text = re.sub(r"[^A-Z0-9]", "", text)

  if text == "":
    return pd.NA

  if len(text) < 6 or len(text) > 8:
    return pd.NA

  return text
