# Indicador de latencia evento → activación, y evaluación de la calidad del dato

**Fuente:** `datos.gov.co`, conjunto `rgre-6ak4` — *Emergencias UNGRD 2023–2024*
**Universo:** 16.036 registros
**Fecha de cálculo:** 27 de agosto de 2026

---

## Advertencia previa — y una corrección propia

En el informe de auditoría anterior afirmé que el campo `fecha_activacion` estaba poblado en **10.613 registros (66%)**. **Es falso, y el error fue mío.**

Filtré por el valor centinela `'No Registra'` sin advertir que el mismo campo usa **dos grafías distintas** para decir lo mismo:

| Valor | Registros |
|---|---|
| `No registra` (minúscula) | 10.561 |
| `No Registra` (mayúscula) | 5.423 |
| **Total centinelas** | **15.984** |
| **Fechas reales** | **52** |

El campo no está poblado en el 66% de los casos. **Está poblado en el 0,32%.**

Dejo el error documentado a propósito: es exactamente el tipo de trampa que tiene este dataset, y cualquiera que lo use va a caer en ella. Que dos grafías del mismo centinela convivan en la misma columna es, por sí solo, un dato sobre el control de calidad del sistema.

---

## 1. El embudo del dato

| Etapa | Registros | % del universo |
|---|---|---|
| Registros en el dataset 2023–2024 | 16.036 | 100% |
| Con **algún** dato en `fecha_activacion` | 52 | 0,32% |
| Con fecha en formato parseable | 50 | 0,31% |
| **Con latencia calculable y coherente** | **44** | **0,27%** |

De 16.036 emergencias registradas en dos años, se puede calcular el tiempo de respuesta de **44**.

### Los dos formatos rotos

Dos registros traen rangos de días en lugar de fechas: `"14 - 17/05/2023"` y `"19-20/06/2023"`. No hay validación de formato en el campo.

### Las seis latencias imposibles

Seis registros —el **12% de los parseables**— tienen fecha de activación **anterior** a la fecha del evento:

| Latencia | Departamento | Municipio | Evento | Evento → Activación |
|---|---|---|---|---|
| **−75 d** | Norte de Santander | Ábrego | Creciente súbita | 2023-11-02 → 2023-08-19 |
| **−41 d** | La Guajira | Uribia | Inundación | 2023-12-13 → 2023-11-02 |
| **−21 d** | Risaralda | Pueblo Rico | Vendaval | 2023-07-29 → 2023-07-08 |
| **−18 d** | Bolívar | San Jacinto del Cauca | Inundación | 2023-09-20 → 2023-09-02 |
| **−12 d** | Bolívar | Magangué | Erosión | 2023-10-25 → 2023-10-13 |
| **−2 d** | Antioquia | Anorí | Vendaval | 2023-09-09 → 2023-09-07 |

No hay validación de coherencia temporal. Nada impide registrar que se respondió a una emergencia antes de que ocurriera.

### Y ningún registro de 2024

Los 52 registros con fecha de activación son **todos de 2023**. En 2024 el campo quedó vacío al 100%.

---

## 2. El indicador, con todas sus reservas

Sobre los 44 registros utilizables:

| Estadístico | Días |
|---|---|
| Mínimo | 0 |
| Percentil 25 | 3 |
| **Mediana** | **14** |
| Media | 41,1 |
| Percentil 75 | 40 |
| Percentil 90 | 124 |
| Máximo | 293 |

### Distribución

| Rango | Casos | % |
|---|---|---|
| Mismo día | 4 | 9% |
| 1–3 días | 8 | 18% |
| 4–7 días | 7 | 16% |
| 8–15 días | 5 | 11% |
| 16–30 días | 7 | 16% |
| 31–60 días | 5 | 11% |
| **Más de 60 días** | **8** | **18%** |

La brecha entre mediana (14 días) y media (41 días) revela una cola larga: casi una quinta parte de los casos documentados tardó más de dos meses en activarse, y el peor llegó a **293 días** — más de nueve meses entre el evento y la activación de la respuesta.

### Desagregaciones — leer con extrema cautela

**Por departamento** (solo los que tienen 2 o más casos):

| Departamento | n | Mediana | Rango |
|---|---|---|---|
| La Guajira | 2 | 67 d | 0–134 |
| Valle del Cauca | 2 | 35 d | 3–67 |
| Meta | 2 | 31 d | 12–50 |
| Córdoba | 5 | 26 d | 7–269 |
| Bolívar | 4 | 22 d | 1–293 |
| Antioquia | 4 | 16 d | 0–83 |
| Sucre | 7 | 15 d | 4–85 |
| Chocó | 4 | 6 d | 2–34 |
| Cundinamarca | 2 | 4 d | 3–4 |
| Caldas | 3 | 2 d | 1–7 |

**Por tipo de evento:**

| Evento | n | Mediana |
|---|---|---|
| Movimiento en masa | 2 | 58 d |
| Incendio forestal | 2 | 46 d |
| Inundación | 28 | 17 d |
| Vendaval | 5 | 7 d |
| Avenida torrencial | 2 | 4 d |

---

## 3. Evaluación honesta: qué precisión permite esto

Es tentador presentar la tabla anterior como "el tiempo de respuesta del Estado colombiano". **No lo es, y presentarlo así sería deshonesto.**

### Lo que estos números NO permiten afirmar

- **Nada a nivel nacional.** 44 casos sobre 16.036 no es una muestra: es un residuo. No fue seleccionado, es lo que quedó.
- **Nada comparativo entre departamentos.** Con n=2, la "mediana" es el promedio de dos observaciones. Que La Guajira aparezca con 67 días y Caldas con 2 no dice nada sobre esos departamentos.
- **Nada sobre tendencia.** Todos los casos son de 2023. No hay serie de tiempo.
- **Nada sobre la ayuda que llegó a la gente.** `fecha_activacion` es una fecha administrativa interna. No es la fecha en que alguien recibió un kit.

### El sesgo de selección, que es el problema de fondo

Los 44 registros no son aleatorios. Se llenaron **precisamente porque hubo una operación grande de por medio**: casi todos traen entregas de kits, varios con miles de unidades. Los eventos pequeños, los que se atendieron mal o los que no se atendieron **no dejan rastro**.

Esto significa que el sesgo apunta hacia el **optimismo**: 14 días de mediana es el desempeño en los casos que alguien se tomó el trabajo de documentar. El desempeño real en las 15.992 emergencias restantes es desconocido, y no hay razón para suponer que sea mejor.

### Incoherencias internas adicionales

- **14 de los 52 registros** reportan kits de alimento entregados pero declaran **cero personas afectadas**. O no se registró la afectación, o se entregó ayuda sin población identificada. Cualquiera de las dos rompe la trazabilidad.
- 3 de los 52 no reportan ninguna entrega, pese a tener fecha de activación.

### Lo que sí se puede afirmar, con toda firmeza

1. **El campo existe en el modelo de datos y no se diligencia.** 99,68% vacío.
2. **Cuando se diligencia, no se valida.** Dos grafías del centinela, dos formatos de fecha rotos, 12% de latencias temporalmente imposibles.
3. **No existe en Colombia información pública que permita medir la oportunidad de la respuesta humanitaria.** No es que el dato sea malo: es que no hay dato.
4. **Los 44 casos documentados sugieren dispersión extrema** —de 0 a 293 días— lo que en sí mismo indica ausencia de un estándar de servicio.

---

## 4. Por qué esto es un buen resultado, no un mal resultado

El proyecto no salió a medir el desempeño del Estado. Salió a determinar si ese desempeño **se puede medir**. La respuesta es no, y ahora está cuantificada:

> De 16.036 emergencias registradas por la UNGRD entre 2023 y 2024, es posible calcular el tiempo de respuesta de 44 —el 0,27%—, y de esas, el 12% arroja resultados temporalmente imposibles.

Esa frase es citable, verificable por cualquiera contra la API pública, y no existía antes. Es el argumento de necesidad del proyecto, con número.

Un instrumento de registro estandarizado no es una mejora incremental sobre lo que hay. **Es la diferencia entre 0,27% y algo.**

---

## 5. Consecuencias para las peticiones

Agregar a la petición de la UNGRD:

> **11. Campo `fecha_activacion`.**
> En el conjunto `rgre-6ak4` publicado en datos.gov.co, el campo `fecha_activacion` contiene un valor centinela —bajo dos grafías distintas, `No registra` y `No Registra`— en **15.984 de 16.036 registros (99,68%)**. De los 52 registros con fecha, **6 (12%) presentan fecha de activación anterior a la fecha del evento**. Se solicita:
> a. Indicar qué evento operativo representa exactamente el campo `fecha_activacion`.
> b. Precisar qué dependencia lo diligencia, en qué momento del ciclo y bajo qué procedimiento.
> c. Explicar por qué no existe validación de coherencia temporal ni de formato en el campo.
> d. Indicar si la Entidad dispone internamente de esta información completa para las emergencias de 2023 a 2026 y, en caso afirmativo, remitirla.
> e. Señalar si la UNGRD mide el tiempo transcurrido entre la ocurrencia del evento y la entrega efectiva de ayuda a la población. En caso negativo, declararlo expresamente.

El literal **e** es el que importa. Ya no se puede responder con un enlace al portal de datos abiertos.

---

## Reproducibilidad

Consulta base (API Socrata, sin autenticación):

```
https://www.datos.gov.co/resource/rgre-6ak4.json
  ?$select=fecha,fecha_activacion,departamento,municipio,evento,personas,kits_de_alimento,colchonetas
  &$where=fecha_activacion not like 'No%'
  &$limit=60
```

Conteo de centinelas:

```
https://www.datos.gov.co/resource/rgre-6ak4.json
  ?$select=fecha_activacion,count(*)&$group=fecha_activacion&$order=count desc
```

Cualquiera puede verificar estos números en menos de un minuto.
