# =================================================================
# Ejercicio 05 — Gráficos y Exportación
# Responsable: Katherine
# =================================================================
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
from urban_flow import contexto, ejercicio_04


def _estilo_grafico(ax, titulo, x, y=None):
    """Aplica un diseño limpio y evita que las letras se amontonen."""
    ax.set_title(titulo, fontweight='bold', pad=10)
    ax.set_xlabel(x)
    if y: ax.set_ylabel(y)
    ax.grid(True, alpha=0.3, linestyle='--')
    # Inclina las etiquetas del eje X si son muchas (como las fechas)
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

def run(df: pd.DataFrame):
    """Genera los 5 gráficos requeridos por la consigna."""
    if df is None or df.empty:
        print("Punto 05: No hay datos para graficar.")
        return

    # Aseguramos que los excesos sean números para evitar TypeError
    df["exceso_velocidad_real"] = pd.to_numeric(df["exceso_velocidad_real"], errors="coerce")
    
    analyzer = ejercicio_04.FineAnalyzer(df)
    contexto.PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    # 1. TOP 10 PATENTES (fines.jpg)
    fig, ax = plt.subplots(figsize=(8, 5))
    top10 = analyzer.ranking_patentes(top=10).set_index("patente")["cantidad"].sort_values()
    top10.plot(kind="barh", ax=ax, color="steelblue")
    _estilo_grafico(ax, "Top 10 Patentes Reincidentes", "Cantidad de Multas")
    fig.savefig(contexto.PLOTS_DIR / "fines.jpg", bbox_inches='tight')

    # 2. % POR HORA (hours.jpg - Torta)
    # Extraemos la hora del reloj (0-23)
    horas = pd.to_datetime(df["hora"], format="%H:%M", errors="coerce").dt.hour
    conteo_h = horas.value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.pie(conteo_h, labels=[f"{int(h)}h" for h in conteo_h.index], autopct='%1.1f%%', startangle=90)
    ax.set_title("Distribución de Infracciones por Hora")
    fig.savefig(contexto.PLOTS_DIR / "hours.jpg")

    # 3. MESES (months.jpg - Histograma para evitar amontonamiento)
    # Agrupamos los meses para ver rangos de frecuencia
    fig, ax = plt.subplots(figsize=(8, 5))
    meses_conteo = pd.to_datetime(df["fecha"]).dt.to_period("M").value_counts()
    meses_conteo.plot(kind="hist", bins=10, ax=ax, color="darkorange", rwidth=0.9)
    _estilo_grafico(ax, "Frecuencia de Multas Mensuales", "Rango de Multas", "Cant. de Meses")
    fig.savefig(contexto.PLOTS_DIR / "months.jpg", bbox_inches='tight')

    # 4. EXCESOS POR HORA Y FECHA (hour.jpg y date.jpg - Líneas)
    for nombre, col_agrupadora, color in [("hour", horas, "green"), ("date", "fecha", "purple")]:
        fig, ax = plt.subplots(figsize=(10, 4))
        df.groupby(col_agrupadora)["exceso_velocidad_real"].sum().plot(ax=ax, color=color, marker='.')
        _estilo_grafico(ax, f"Suma de Exceso Real por {nombre.capitalize()}", nombre, "km/h")
        fig.savefig(contexto.PLOTS_DIR / f"{nombre}.jpg", bbox_inches='tight')

    plt.close('all')
    print(f"✅ Punto 05 finalizado. Gráficos guardados en {contexto.PLOTS_DIR}")