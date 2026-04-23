"""Ejercicio 04 — clase FineAnalyzer.

Responsable: Camardelli (Ej. 04 y Punto 07 en feature/camardelli)

CONSIGNA (resumen):
  Clase FineAnalyzer que:
  - Reciba el DataFrame limpio en __init__ y encapsule los datos.
  - ranking_patentes(top 5): DataFrame índice 1..n, columnas patente y
    cantidad.
  - ranking_horarios(top 5): idem con hora y cantidad.
  - promedio_exceso(): float (sobre columna exceso_velocidad).
  - promedio_exceso_real(): float.
  - multas_por_ubicacion(): DataFrame ordenado por ubicación con cantidad.

  En el notebook: crear instancia e invocar cada método en celdas separadas.

LIBRERÍAS SUGERIDAS:
  pandas.

NOTAS:
  - Type hints y docstrings en funciones/métodos según consigna de estilo.
"""
from __future__ import annotations

import pandas as pd


class FineAnalyzer:
  """Analizador de multas; encapsula el dataset limpio para consultas."""

  def __init__(self, data: pd.DataFrame) -> None:
    self._data = data.copy()

  def ranking_patentes(self, top: int = 5) -> pd.DataFrame:
    """Top patentes por cantidad de multas."""
    result = (
      self._data["patente"]
      .value_counts(dropna=True)
      .head(top)
      .rename_axis("patente")
      .reset_index(name="cantidad")
    )
    result.index = pd.RangeIndex(start=1, stop=len(result) + 1)
    return result

  def ranking_horarios(self, top: int = 5) -> pd.DataFrame:
    """Top horas por cantidad de multas."""
    result = (
      self._data["hora"]
      .value_counts(dropna=True)
      .head(top)
      .rename_axis("hora")
      .reset_index(name="cantidad")
    )
    result.index = pd.RangeIndex(start=1, stop=len(result) + 1)
    return result

  def promedio_exceso(self) -> float:
    """Promedio de exceso_velocidad."""
    return float(self._data["exceso_velocidad"].mean(skipna=True))

  def promedio_exceso_real(self) -> float:
    """Promedio de exceso_velocidad_real."""
    return float(self._data["exceso_velocidad_real"].mean(skipna=True))

  def multas_por_ubicacion(self) -> pd.DataFrame:
    """Conteo por ubicación ordenado alfabéticamente."""
    result = (
      self._data["ubicacion"]
      .value_counts(dropna=True)
      .rename_axis("ubicacion")
      .reset_index(name="cantidad")
      .sort_values(by="ubicacion")
      .reset_index(drop=True)
    )
    result.index = pd.RangeIndex(start=1, stop=len(result) + 1)
    return result
