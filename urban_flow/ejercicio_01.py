"""Ejercicio 01 — estructura y Git.

Responsable: Katherine

CONSIGNA (resumen):
  Inicialización y configuración de la herramienta de versionado. Crear la
  estructura bajo urban_flow/data/ y trabajar sobre la rama Sprint_1.

  urban_flow/
  ├── data/
  │   ├── interim/   (plots dentro: interim/plots/)
  │   ├── processed/
  │   └── raw/

LIBRERÍAS SUGERIDAS:
  pathlib, subprocess (stdlib).

NOTAS:
  - Variable desactivar_git_push va en el notebook si automatizan push.
  - Evitar git add . en los comandos que documenten.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

from urban_flow import contexto


def run() -> None:
  """Crea carpetas del enunciado y deja el repositorio en rama Sprint_1."""
  _crear_carpetas()
  _checkout_sprint_1()
  print("Ej. 01 listo — carpetas bajo", contexto.DATA)


def _crear_carpetas() -> None:
  """data/raw, data/interim, data/processed, data/interim/plots."""
  for ruta in (
    contexto.RAW_DIR,
    contexto.INTERIM_DIR,
    contexto.PROCESSED_DIR,
    contexto.PLOTS_DIR,
  ):
    ruta.mkdir(parents=True, exist_ok=True)


def _checkout_sprint_1() -> None:
  """Repo en la raíz del proyecto; rama Sprint_1 como pide la consigna."""
  raiz = Path(__file__).resolve().parent.parent
  try:
    ok = subprocess.run(
      ["git", "rev-parse", "--is-inside-work-tree"],
      cwd=raiz,
      capture_output=True,
      text=True,
    )
    if ok.returncode != 0:
      subprocess.run(["git", "init"], cwd=raiz, check=True)
    ramas = subprocess.run(
      ["git", "branch", "--list", "Sprint_1"],
      cwd=raiz,
      capture_output=True,
      text=True,
      check=True,
    )
    if "Sprint_1" not in ramas.stdout:
      subprocess.run(
        ["git", "checkout", "-b", "Sprint_1"],
        cwd=raiz,
        check=True,
      )
    else:
      subprocess.run(["git", "checkout", "Sprint_1"], cwd=raiz, check=True)
  except (FileNotFoundError, subprocess.CalledProcessError):
    pass
