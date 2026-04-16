# Urban Flow — Trabajo Práctico Integrador (Sprint 1)

**Rama de trabajo:** `Sprint_1`

## Integrantes

| Quién | Rol en esta base |
|-------|------------------|
| **Katherine** | Ejercicio 01, Punto 07, coordinación Git / entrega |
| **Joaquín** | Ejercicio 02, Punto 06 |
| **Camardelli** | Ejercicio 03 |
| **Emi** | Ejercicio 04, Punto 05 |

Cada responsable edita principalmente su archivo en `urban_flow/` (ver tabla
abajo) y luego integra en el notebook único.

## Archivos por ejercicio

| Archivo | Contenido |
|---------|-----------|
| `urban_flow/ejercicio_01.py` | Ej. 01 — Katherine |
| `urban_flow/ejercicio_02.py` | Ej. 02 — Joaquín |
| `urban_flow/ejercicio_03.py` | Ej. 03 — Camardelli |
| `urban_flow/ejercicio_04.py` | Ej. 04 — Emi (`FineAnalyzer`) |
| `urban_flow/ejercicio_05.py` | Punto 05 — Emi (gráficos) |
| `urban_flow/ejercicio_06.py` | Punto 06 — Joaquín |
| `urban_flow/ejercicio_07_conclusion.md` | Punto 07 — Katherine (texto) |
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

Inicialización y versionado. Rama **`Sprint_1`**. Estructura de directorios:

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

Objetivo: que **cada uno tenga su propio remoto** para trabajar su ejercicio
sin pisar al resto, y un **repo grupal** donde se integra la entrega final.

### 1. Repo grupal (oficial)

- Un integrante crea el repositorio en GitHub/GitLab (ej. `urban-flow-grupo`).
- Agrega a los compañeros como colaboradores y a los mails de la cátedra.
- Rama principal de trabajo: **`Sprint_1`** (o acuerdan `main` + merge a
  entrega; lo importante es cumplir el enunciado).

### 2. Fork o clon personal

Cada uno:

- Hace **fork** del repo grupal a su cuenta **o** crea un repo vacío y añade
  dos remotos:
  - `origin` → su repo personal.
  - `grupo` → repo del grupo.

Así cada uno puede hacer `push` a **su** `origin` con libertad.

### 3. Ramas por persona o por ejercicio (recomendado)

Ejemplos de nombres:

- `feat/katherine-ej01`
- `feat/joaquin-ej02`
- `feat/camardelli-ej03`
- `feat/emi-ej04-05`

Flujo:

1. Crear rama desde `Sprint_1`.
2. Implementar solo los archivos acordados (ver tabla de responsables).
3. Commits pequeños y mensajes claros.
4. `git push` al **repo personal** (`origin`).
5. Abrir **Pull Request** al repo grupal hacia `Sprint_1` **o** acordar un día
   de integración y merge en equipo.

### 4. Integración en el grupo

- **Katherine** (o quien coordine) revisa PRs, resuelve conflictos en el
  notebook y en `CHANGELOG.md`.
- **No usar `git add .`:** por ejemplo  
  `git add urban_flow/ejercicio_02.py README.md`
- Actualizar **`CHANGELOG.md`** cada vez que se fusiona un ejercicio.

### 5. Notebook integrador

- Un solo `.ipynb` para entrega: cada sección importa el módulo
  correspondiente.
- Antes de entregar: **Reiniciar y ejecutar todo**, sin errores intermedios.

---

## Validación final

En Jupyter / IDE: *Runtime → Restart session and run all* (o equivalente) y
revisar que no falle ninguna celda.
