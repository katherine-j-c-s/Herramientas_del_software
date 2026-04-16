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
  """Analizador de multas; reemplazar stubs por la lógica del enunciado."""

  def __init__(self, data: pd.DataFrame) -> None:
    self._data = data.copy()

  def ranking_patentes(self, top: int = 5) -> pd.DataFrame:
    """Top patentes por cantidad de multas."""
    return pd.DataFrame(columns=["patente", "cantidad"])

  def ranking_horarios(self, top: int = 5) -> pd.DataFrame:
    """Top horas por cantidad de multas."""
    return pd.DataFrame(columns=["hora", "cantidad"])

  def promedio_exceso(self) -> float:
    """Promedio de exceso_velocidad."""
    return 0.0

  def promedio_exceso_real(self) -> float:
    """Promedio de exceso_velocidad_real."""
    return 0.0

  def multas_por_ubicacion(self) -> pd.DataFrame:
    """Conteo por ubicación ordenado alfabéticamente."""
    return pd.DataFrame(columns=["ubicacion", "cantidad"])
