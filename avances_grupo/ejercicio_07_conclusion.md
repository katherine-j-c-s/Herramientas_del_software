# Punto 07 — Conclusión sobre el dataset

**Responsable:** Camardelli

**CONSIGNA (resumen):**

Redactar una conclusión acerca de los datos que contiene el dataset.

---

## Conclusión: Análisis del Dataset de Multas por Exceso de Velocidad en Vaalserberg

### Contexto y volumen de datos

El dataset analizado contiene 4,000 registros de multas por exceso de velocidad levantadas en Vaalserberg, Bélgica. Tras la limpieza y validación de datos, se conservaron 1,547 multas (38.7% del dataset original), lo que refleja la importancia de la preparación y calidad de datos en análisis reales. Las 2,453 filas eliminadas corresponden a registros incompletos, velocidades registradas fuera de rango o infracciones sin validez según los criterios de exceso de velocidad.

### Patrones de reincidencia vehicular

El análisis identifica un grupo reducido pero significativo de conductores reincidentes. Las patentes **WEFLYN**, **HF3461** y **M431ZW** encabezan el ranking con 38, 37 y 34 multas respectivamente, indicando que una pequeña proporción de vehículos es responsable de una porción importante de las infracciones. Este patrón sugiere la posibilidad de implementar medidas dirigidas hacia conductores de alto riesgo, como campanías educativas o restricciones de circulación.

### Anomalías y patrones temporales

Durante el proceso de normalización de datos se identificó una concentración atípica de 310 multas registradas a las 00:00. Este pico se asocia a registros que presentaban horas inválidas o inconsistentes en el dataset original, las cuales fueron ajustadas a un valor estándar. Este comportamiento sugiere que cerca del 20% de los datos contenía información temporal defectuosa, evidenciando posibles fallas en la captura o transmisión de los datos del sistema de radares.

En contraste, las multas con horarios válidos (como 09:04, 09:23 o 10:38) muestran una distribución más dispersa y coherente, propia de los períodos de operación. Esta diferencia resalta la utilidad del procesamiento de datos para detectar anomalías y evaluar la calidad de la información de origen.

### Distribución geográfica

Las tres avenidas monitoradas concentran el 70.4% de las multas: **Avenida Libertador** (648), **Avenida Siempre Viva** (460) y **Ruta 9** (439). Esta concentración sugiere que estas vías son las principales rutas de tráfico donde los excesos de velocidad representan un riesgo significativo, destacándose como prioritarias para implementar medidas de seguridad vial.

### Magnitud de infracciones

El promedio de exceso de velocidad es de **39.45 km/h**, mientras que el exceso real promedio (considerando un margen de tolerancia del 5%) es de **42.48 km/h**. Esta diferencia es relativamente marginal, indicando que los límites de velocidad establecidos son consistentes en su aplicación. Los excesos significativos (superiores a 30 km/h) representan un riesgo considerable y justifican las sanciones implementadas.
