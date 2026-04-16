"""Punto 05 — gráficos y exportación.

Responsable: Camardelli

CONSIGNA (resumen):
  Responder con un gráfico cada ítem y exportar:
  - Top 10 patentes reincidentes (mayor a menor) →
    urban_flow/data/interim/plots/fines.jpg
  - Porcentaje de infracciones por hora (torta) → hours.jpg
  - Infracciones por mes (barras horizontales, mayor a menor) → months.jpg
  - Excesos agrupados por hora (líneas) → hour.jpg
  - Excesos agrupados por fecha (líneas) → date.jpg

  (En el enunciado aparece un typo "ubran_flow"; usar urban_flow.)

LIBRERÍAS SUGERIDAS:
  matplotlib.pyplot, pandas, numpy si hace falta.

NOTAS:
  - Depende del DataFrame limpio post ejercicio 03.
"""
from __future__ import annotations

import pandas as pd


def run(df: pd.DataFrame | None = None) -> None:
  """Implementar los cinco gráficos y guardar los .jpg en PLOTS_DIR."""
  pass
