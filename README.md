# acopio-abierto

**Medir la ayuda humanitaria en días-persona de ración completa, no en toneladas.**

---

Una donación de 20 toneladas no dice nada. No porque sea poca: porque no tiene duración. Es un número sin antes ni después.

"Alimenta a 400 familias durante 12 días" no tiene más datos. Tiene tiempo y consecuencia.

Este repositorio contiene el intento de hacer ese cambio de unidad calculable.

---

## El problema, con número

Colombia no puede evaluar el desempeño de su respuesta humanitaria. Lo verificamos contra las APIs públicas:

| Hallazgo | Cifra |
|---|---|
| Registros de la UNGRD sin ninguna ayuda entregada anotada | **98,0%** (2019–22) · **99,7%** (2023–24) |
| Emergencias con tiempo de respuesta calculable | **44 de 16.036** (0,27%) |
| De esas, con latencia temporalmente imposible | **12%** |
| Serie pública de emergencias | **se corta en diciembre de 2024** |
| Campos de necesidades en la principal plataforma ciudadana | **0% diligenciados** |

Los campos existen. Están vacíos. De ahí el principio de diseño del proyecto:

> **Todo campo que exista y no sea imprescindible para operar, quedará vacío.**
> Por lo tanto: no se captura nada que pueda calcularse.

Detalle en [`docs/investigacion/`](docs/investigacion/).

---

## El modelo

Programación lineal. Dado un inventario, la composición nutricional de cada ítem y el estándar humanitario Esfera, maximizar los días-persona de ración completa:

```
max  D
s.a. Σ n_ik·x_i ≥ r_k·D    ∀k    adecuación nutricional
     x_i ≤ q_i             ∀i    disponibilidad
     x_i ≤ a_i·D           ∀i    aceptabilidad
```

El **dual** entrega gratis el motor de petición: cuánto vale cada insumo adicional, y hasta qué cantidad.

### Resultado con un inventario de ejemplo

3.265 kg de alimentos donados → **1.125 días-persona** de ración completa.

| Donación adicional | Ganancia |
|---|---|
| 500 kg de arroz | **+0,0 días-persona** |
| 50 kg de aceite (~600.000 COP) | **+1.400 días-persona** |

El arroz vale cero **no porque no alimente, sino porque ya no cabe más arroz en la dieta de nadie**. El modelo lo deduce por dualidad; nadie se lo dice.

Formulación completa en [`docs/modelo-ensamblaje-alimentario.md`](docs/modelo-ensamblaje-alimentario.md). Código reproducible en [`modelo/`](modelo/).

---

## Estado

**Esto es una hipótesis, no una herramienta.** Está construido sobre inventarios de ejemplo. No ha tocado una bodega real.

La fase actual no es programar: es hablar con quienes coordinan centros de acopio y descubrir en qué nos estamos equivocando.

→ **[Cómo vamos a validarlo](docs/validacion-fase-0.md)**

Progreso en [`ROADMAP.md`](ROADMAP.md) · checklist en [`feature_list.json`](feature_list.json).

---

## Límite declarado

`D` es **capacidad de oferta, no cobertura de necesidad**. El modelo dice cuántas raciones se pueden armar con lo que hay, no cuántas hacen falta. No existe señal pública de demanda por comunidad en Colombia y este proyecto no la inventa.

Un acopio puede medir la eficiencia de su conversión, no la eficacia de la ayuda.

---

## Lo que este proyecto no es

- No es evaluación de daños — Copernicus y UNOSAT ya lo hacen bien.
- No es inventario institucional — eso es LSS/SUMA y le pertenece al SNGRD.
- No es un mapa de acopios — [Gravitas](https://www.mapa.gravitasworld.com/) ya lo tiene y lo tiene mejor.

Es el **libro mayor**: el registro de flujo que hoy no lleva nadie y sin el cual nada de lo anterior se puede evaluar.

---

## Cómo participar

- **Nutricionistas y personal de salud** — revisar los supuestos y los topes de aceptabilidad.
- **Logística humanitaria** — decirnos qué está mal.
- **Organizaciones con inventarios reales** — compartir uno y recibir el análisis de vuelta, sin costo ni compromiso. Estamos empezando, así que tomamos los primeros casos con cuidado.

## Estructura

```
.GCC/          memoria del proyecto: intención, bitácora, commits
docs/          investigación, modelo y métricas
instrumentos/  guiones de entrevista y plantillas de registro
modelo/        implementación en PuLP
feature_list.json   checklist autoritativo
ROADMAP.md
```

## Licencia

Código MIT · documentación CC BY 4.0.
