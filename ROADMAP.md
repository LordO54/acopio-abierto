# Roadmap

Fechas recalculadas el **27 de agosto de 2026**. La ventana original de F0 (15–21 de agosto) se desplazó por disponibilidad. El retraso cambió el encuadre del proyecto de *respuesta a emergencia* a *preparación*, que es más honesto y elimina la presión de competir contra la ventana de la catástrofe.

---

## F0 · Validación por entrevistas
**27 de agosto – 19 de septiembre de 2026**

Objetivo: descubrir en qué se equivoca el modelo antes de programarlo.

| Semana | Fechas | Foco |
|---|---|---|
| 1 | 27 ago – 3 sep | Publicar repo · radicar los cuatro derechos de petición · armar lista de contactos · primeros mensajes |
| 2–3 | 4 – 17 sep | 5 a 8 entrevistas · recolectar artefactos de registro reales · conversación con Gravitas |
| 4 | 18 – 19 sep | Síntesis: supuestos confirmados, refutados y parámetros a recalibrar |

**Criterio de salida.** Poder responder con fuente citable:
1. Qué entidad tiene el mandato legal de registrar donaciones y con qué instrumento.
2. Si ese instrumento se usó en las últimas cinco emergencias.
3. Qué métricas de desempeño logístico existen públicamente (respuesta probable: ninguna) y con qué documento se prueba.
4. Qué información dicen necesitar los coordinadores de acopio y no tienen.

**Riesgo principal.** Que `a_i` —el tope de aceptabilidad— resulte imposible de definir de forma estable. Es el parámetro más débil del modelo y solo se calibra en campo.

---

## F1 · Instrumento mínimo
**22 de septiembre – 17 de octubre de 2026**

Objetivo: que un voluntario pueda registrar un evento en menos de 30 segundos.

- Tabla de composición de 25–30 ítems reales, con fuente ICBF por fila.
- Libro mayor mínimo: entrada, salida, merma. Papel primero, hoja de cálculo después.
- Calibración de `a_i` con lo aprendido en F0.
- Motor de optimización que devuelve `D`, `R`, capacidad varada y pedido con tope.
- Análisis de sensibilidad como compuerta de publicación.

**Regla heredada de las auditorías.** No se captura nada que pueda calcularse. Si una métrica exige un campo nuevo, la métrica está mal diseñada.

---

## F2 · Piloto en bodega real
**20 de octubre – 21 de noviembre de 2026**

Un acopio lleva el libro mayor durante cuatro semanas y produce M1–M5. Se contrasta el `D` predicho contra las raciones efectivamente armadas y se explica la diferencia.

**Este es el único hito que prueba algo.** Todo lo anterior es hipótesis.

---

## F3 · Red de acopios
**2027**

Modelo de transbordo multi-bodega. Si el acopio A tiene aceite con precio sombra 0,35 y el B lo tiene en 28,90, mover ese aceite genera 28,5 raciones por kilo sin una sola donación nueva.

Es donde está el valor grande y **requiere que varios acopios lleven el libro mayor**. Por eso F1 y F2 no son preliminares: son la condición de posibilidad.

---

## Dependencias duras

```
F0.8 entrevistas ──► F1.3 calibrar a_i ──► F1.4 motor ──► F2.1 piloto ──► F3.1 red
F1.1 tabla ICBF  ──► F1.4 motor
F1.2 libro mayor ──► F2.1 piloto
```

## Protocolo de ramas

Se abre rama para lógica algorítmica no verificada. Aplica a **F1.4** (motor de optimización) y **F3.1** (transbordo). El resto se trabaja en `main`.
