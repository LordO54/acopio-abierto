# main.md — intención global y hoja de ruta

**Proyecto:** acopio-abierto
**Creado:** 27 de agosto de 2026
**Rama actual:** `main`

---

## Intención

Cambiar la unidad de medida de la ayuda humanitaria en Colombia: de **kilogramos recibidos** a **días-persona de ración completa entregados**.

De ese cambio de unidad se derivan tres cosas que hoy no existen:

1. Una definición operativa de "bien" para un centro de acopio.
2. Un motor de petición que dice qué falta, cuánto vale y **cuándo parar**.
3. Un histórico de desempeño de la ayuda.

## Por qué

La investigación de agosto de 2026 estableció que no existe información pública que permita evaluar el desempeño logístico de la respuesta humanitaria en Colombia. Los campos existen en los sistemas y están vacíos. Ver `docs/investigacion/`.

El diagnóstico de fondo no es escasez de información sino **ausencia de duración** en la que hay: "20 toneladas" es un evento sin antes ni después. "Alimenta a 400 familias durante 12 días" tiene sujeto, tiempo y consecuencia.

## Principio de diseño rector

> Todo campo que exista y no sea imprescindible para operar, quedará vacío.

Evidencia: UNGRD 98–99,7% vacío; Gravitas 100% vacío. De ahí la regla: **no se captura nada que pueda calcularse.** Si una métrica exige un campo nuevo, la métrica está mal diseñada.

## Hoja de ruta

| Fase | Nombre | Ventana | Estado |
|---|---|---|---|
| **F0** | Validación por entrevistas | 27 ago – 19 sep 2026 | en curso |
| F1 | Instrumento mínimo | 22 sep – 17 oct 2026 | pendiente |
| F2 | Piloto en bodega real | 20 oct – 21 nov 2026 | pendiente |
| F3 | Red de acopios (transbordo) | 2027 | pendiente |

Detalle en `ROADMAP.md`. Checklist autoritativo en `feature_list.json`.

## Lo que este proyecto NO es

- No es un sistema de evaluación de daños. Copernicus y UNOSAT ya lo hacen bien.
- No es un sistema de inventario institucional. Eso es LSS/SUMA y le pertenece al SNGRD.
- No es un mapa de acopios. Gravitas ya lo tiene y lo tiene mejor.
- **Es el libro mayor**: el registro de flujo que hoy no lleva nadie y sin el cual nada de lo anterior se puede evaluar.

## Límite declarado

`D` es capacidad de oferta, no cobertura de necesidad. El modelo dice cuántas raciones se pueden armar con lo que hay, **no cuántas hacen falta**. No existe señal pública de demanda por comunidad en Colombia y este proyecto no la inventa.

## Ramas

| Rama | Propósito |
|---|---|
| `main` | investigación, modelo y documentación |

Se abrirá rama cuando se implemente el motor de optimización como servicio (F1.4) y el problema de transbordo (F3), por ser lógica algorítmica no verificada.
