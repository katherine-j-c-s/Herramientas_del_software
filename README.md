# Urban Flow — Trabajo Práctico Integrador (Sprint 1)

**Git (equipo):** `main` (estable) ← **`Sprint_1`** (integración) ←
**`feature/<nombre>`** (una rama por persona). El detalle está en la sección
**Cómo trabajamos nosotros con Git** más abajo.

## Integrantes

| Quién | Qué hace |
|-------|----------|
| **Katherine** | Ejercicio 01, Punto 05, coordinación Git |
| **Joaquín** | Ejercicio 02, Punto 06 |
| **Emi** | Ejercicio 03 |
| **Camardelli** | Ejercicio 04 (`FineAnalyzer`), Punto 07 (conclusión) |

Cada uno avanza en **su rama** `feature/<nombre>`; los cambios se integran
primero en **`Sprint_1`** y, cuando esté validado, en **`main`**.

## Archivos por ejercicio

| Archivo | Contenido |
|---------|-----------|
| `urban_flow/ejercicio_01.py` | Ej. 01 — Katherine |
| `urban_flow/ejercicio_02.py` | Ej. 02 — Joaquín |
| `urban_flow/ejercicio_03.py` | Ej. 03 — Emi |
| `urban_flow/ejercicio_04.py` | Ej. 04 — Camardelli (`FineAnalyzer`) |
| `urban_flow/ejercicio_05.py` | Punto 05 — Katherine (gráficos) |
| `urban_flow/ejercicio_06.py` | Punto 06 — Joaquín |
| `urban_flow/ejercicio_07_conclusion.md` | Punto 07 — Camardelli (texto) |
| `urban_flow/contexto.py` | Rutas y URL del dataset (compartido) |
| `01_Urban_Flow-Apellidos_Nombres.ipynb` | **Integrador**: imports + llamadas |

Renombrar el `.ipynb` según la nomenclatura de la cátedra al entregar.

---

## Tecnologías y librerías (total)

- **Lenguaje:** Python 3.
- **Entorno:** Jupyter / VS Code / Cursor con kernel Python (o Colab si la
  materia lo permite; ajustar rutas).
- **Versionado:** Git + remoto en la nube (GitHub, GitLab, etc.) con token.
- **Librerías alineadas a la cursada:** `pandas`, `numpy`, `matplotlib`,
  expresiones regulares vía módulo `re` (stdlib).
- **Stdlib útil:** `pathlib`, `urllib.request`, `subprocess` (si automatizan
  Git desde código).

Instalación típica:

`pip install pandas numpy matplotlib`

---

## Cómo se organizan los profes (resumen de consigna)

### Organización del notebook

- Una celda **antes del Ejercicio 01** con **todas** las importaciones.
- Título en cada celda; cada funcionalidad en una celda con título; agrupar
  lo afín.
- **Imports** solo en la primera celda de código, arriba de la descripción
  del Ejercicio 01.

### Versionado y equipo

- Grupos de hasta 6 personas; la defensa es individual.
- Cualquier integrante puede modificar; se espera trabajo colaborativo.
- **Control de versiones** obligatorio; vincular con token al servicio en la
  nube.
- **Colaboradores** del remoto del grupo: `lcd-sa182@ugr.edu.ar`,
  `fpasinato@ugr.edu.ar`.
- **CHANGELOG.md:** un registro por día de trabajo / por ejercicio.
- Variable **`desactivar_git_push`:** debe permitir desactivar los
  `git push` (definida en el notebook).
- **No** usar `git add .` (agregar archivos por ruta explícita).

### Entrega y formato

- Archivo **`.ipynb`** ejecutado, con datos precargados o rutas coherentes.
- Copia sobre la **plantilla** que indique la cátedra.
- Validar con *Reiniciar sesión y ejecutar todo* antes de entregar.
- **No** usar Google Drive para datos; **no** sustituir herramientas de la
  cursada por alternativas no vistas.
- Estilo: **2 espacios** de indentación, líneas ~**80** caracteres, **type
  hints**, comentarios solo donde pide el enunciado (funciones, clases,
  métodos, propiedades).

### Herramientas permitidas

Principalmente: NumPy, Matplotlib, Pandas, regex, Kaggle/datasets según lo
visto en la materia. Extras solo con criterio fundado.

---

## Consignas por ejercicio (texto de la materia)

### Objetivo general

Aplicar versionado, organización, limpieza de código y uso de **Pandas** sobre
datos de multas por exceso de velocidad.

### Contexto

Vaalserberg (Bélgica), datos heredados con errores de formato y faltantes.
Dataset:
[speeding_fines.csv](https://raw.githubusercontent.com/HAD141/datasets/refs/heads/main/TrabajosPracticos/urban_flow/speeding_fines.csv)

### Ejercicio 01 (1 punto)

Inicialización y versionado. El enunciado de la materia menciona la rama
**`Sprint_1`**; en este grupo las ramas de trabajo siguen el modelo
**`main` / `Sprint_1` / `feature/<nombre>`** (ver README). Estructura de
directorios:

```text
urban_flow/
├── data/
│   ├── interim/   (datasets intermedios; dentro: plots/)
│   ├── processed/
│   └── raw/
```

### Ejercicio 02 (1 punto)

- Descargar el dataset raw y guardarlo en `urban_flow/data/raw`.
- Mostrar las 5 primeras filas.
- Analizar tipos de datos.
- Contar valores nulos.

### Ejercicio 03 (2 puntos)

Con Pandas:

- Fechas a `YYYY-MM-DD`; inválidas → `1932-01-01`. Mostrar 10 primeras fechas.
- Horas a formato 24 h; inválidas → `00:00`. Mostrar 10 primeras horas.
- Ubicaciones: sin caracteres especiales, mayúsculas. Mostrar 10 primeras.
- Patentes: limpiar, mayúsculas; error → `pd.NA`. Mostrar 10 últimas.
- Eliminar filas con datos relevantes vacíos (mensaje con cantidad y columnas
  según leyenda).
- Outliers: detectar, eliminar (mensaje con cantidad y columnas).
- Columna **`exceso_velocidad_real`** = `velocidad_registrada` −
  `velocidad_maxima`. Mostrar 10 patentes y exceso real.
- Columna **`exceso_velocidad`** = `velocidad_registrada` −
  `velocidad_maxima` − 5 % de la máxima (según enunciado: diferencia respecto
  a la máxima más un 5 % de la máxima). Mostrar 10 patentes y exceso.
- Quitar filas **sin infracción** según `exceso_velocidad` (mensaje).
- Guardar CSV en `urban_flow/data/interim/speeding_fines.csv`.

### Ejercicio 04 (2 puntos)

Clase **`FineAnalyzer`**:

- Recibe el DataFrame limpio en el constructor y encapsula los datos.
- `ranking_patentes` (top 5): DataFrame, índice desde 1, columnas patente y
  cantidad.
- `ranking_horarios` (top 5): hora y cantidad.
- `promedio_exceso` y `promedio_exceso_real`: flotantes.
- `multas_por_ubicacion`: DataFrame ordenado por ubicación.

Crear el objeto e invocar **cada método en celdas separadas** en el notebook.

### Punto 05 (2 puntos)

Un gráfico por ítem; exportar a `urban_flow/data/interim/plots/`:

| Archivo | Contenido |
|---------|-----------|
| `fines.jpg` | Top 10 patentes más reincidentes (mayor a menor) |
| `hours.jpg` | Porcentaje de infracciones por hora (torta) |
| `months.jpg` | Infracciones por mes, barras horizontales, mayor a menor |
| `hour.jpg` | Líneas: excesos agrupados por hora |
| `date.jpg` | Líneas: excesos agrupados por fecha |

(En el PDF a veces aparece el typo **ubran_flow**; usar **urban_flow**.)

### Punto 06 (1 punto)

- Porcentaje de infracciones en fecha **1932-01-01** (formato de texto pedido).
- Porcentaje de infracciones en hora **00:00** (formato pedido).

### Punto 07 (1 punto)

Conclusión escrita sobre el dataset (celda Markdown en el notebook; borrador
en `ejercicio_07_conclusion.md`).

---

## Cómo trabajamos nosotros con Git (repos personales)

Objetivo: **cada integrante** trabaja en **su rama** `feature/<nombre>` con
**todos los ejercicios que le tocan**; eso se integra en **`Sprint_1`**, y solo
cuando el equipo valida **`Sprint_1`**, se mergea a **`main`**.

### Ramas del equipo

| Rama | Rol |
|------|-----|
| **`main`** | Código estable y listo para entrega. Solo recibe merge desde `Sprint_1` cuando todos acuerdan. |
| **`Sprint_1`** | Integración: aquí se fusionan las ramas personales cuando hay algo listo para probar en conjunto. |
| **`feature/katherine`** | Katherine: Ej. 01, Punto 05. |
| **`feature/joaquin`** | Joaquín: Ej. 02, Punto 06. |
| **`feature/emi`** | Emi: Ej. 03. |
| **`feature/camardelli`** | Camardelli: Ej. 04, Punto 07. |

Usar **nombres en minúsculas y sin tildes** en el nombre de la rama (convención
Git). Si preferís `feature/joaquin` sin tilde, está bien.

### Flujo de trabajo

1. Partir de **`Sprint_1`** actualizado:  
   `git checkout Sprint_1` → `git pull`.
2. Crear o usar la rama personal:  
   `git checkout -b feature/emi` (ejemplo si aún no existe).
3. Implementar **todos** los puntos del TP asignados a esa persona en los
   archivos correspondientes. **No usar `git add .`**; por ejemplo:  
   `git add urban_flow/ejercicio_03.py`
4. Subir: `git push -u origin feature/emi`
5. Abrir **Pull Request** **`feature/<nombre>` → `Sprint_1`** (o merge local
   acordado). Resolver conflictos en el notebook o `CHANGELOG.md` si aparecen.
6. Cuando **`Sprint_1`** esté completo y el notebook pase *Reiniciar y ejecutar
   todo*, merge **`Sprint_1` → `main`**.

### Repo grupal y remotos

- Un integrante crea el repositorio en GitHub/GitLab y agrega compañeros y
  cuentas de la cátedra (`lcd-sa182@ugr.edu.ar`, `fpasinato@ugr.edu.ar`).
- Opcional: **fork** personal o segundo remoto para practicar `push` sin
  tocar el remoto del grupo; el flujo `main` / `Sprint_1` / `feature/<nombre>`
  es el mismo.

### Integración y entrega

- **Katherine** (o quien coordine) puede ayudar a revisar PRs hacia `Sprint_1`
  y el merge final `Sprint_1` → `main`.
- Actualizar **`CHANGELOG.md`** al integrar cada merge a `Sprint_1` y al cerrar
  `main`.
- **Notebook:** un solo `.ipynb`; antes de subir a `main`: **Reiniciar y
  ejecutar todo**, sin errores intermedios.

### Enunciado y rama `Sprint_1`

La consigna del Ejercicio 01 cita la rama **`Sprint_1`**. En este grupo es
también la rama donde se integran las **`feature/<nombre>`** antes de pasar a
**`main`**.

---

## Validación final

En Jupyter / IDE: *Runtime → Restart session and run all* (o equivalente) y
revisar que no falle ninguna celda.
