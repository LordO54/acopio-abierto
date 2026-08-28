# Qué nutrientes exige Esfera y por qué el modelo usa solo tres

**27 de agosto de 2026**

---

## 1. En síntesis

Esfera no exige tres nutrientes. Exige **energía, proteína, grasa y 19 vitaminas y minerales** — 22 requerimientos en total.

El modelo usa tres. Es una simplificación deliberada, defendible en el corto plazo y **peligrosa si se sostiene en el tiempo**. Este documento explica por qué, y qué hacer al respecto.

---

## 2. Lo que Esfera especifica

### Macronutrientes — cifras de planificación

| Requerimiento | Valor | Nota |
|---|---|---|
| Energía | **2.100 kcal** por persona/día | +100 kcal por cada 5 °C bajo 0 °C en climas fríos |
| Proteína | **10–12%** de la energía total | ≈ 52–63 g |
| Grasa | **17%** de la energía total | ≈ 40 g |

El modelo usa el extremo inferior de la proteína (10% → 52,5 g). Conviene documentarlo: es una elección, no un dato.

### Micronutrientes — 19 vitaminas y minerales

La edición 2011 revisó la lista tras consulta con OMS, UNICEF, PMA, ACNUR, MSF-B y CDC, y recalculó los requerimientos poblacionales con base en las Ingestas de Nutrientes de Referencia FAO/OMS de 2004. Se revisaron **14** requerimientos; se añadieron vitamina B6, cobre y calcio; se eliminó la biotina.

Los 19:

| Vitaminas | Minerales y oligoelementos |
|---|---|
| A, D, E, K | Hierro, yodo, zinc |
| B1 (tiamina), B2 (riboflavina), B3 (niacina) | Calcio, magnesio |
| B6, B12, folato, ácido pantoténico | Selenio, cobre |
| C | |

> **Los valores numéricos exactos por persona/día están en el Apéndice 6 del Manual Esfera ("Nutritional requirements").** No se transcriben aquí porque no han sido verificados contra el documento original, y citar cifras de segunda mano sería incoherente con el resto del trabajo. **Tarea F1.1b: leerlos del PDF oficial y citarlos con página.**

### Un detalle que fortalece el modelo

Los requerimientos de Esfera **no son individuales: son medias poblacionales**, calculadas sobre un perfil demográfico de referencia que ya incorpora niños, adultos mayores y una prevalencia asumida de embarazo (2,4%) y lactancia (2,6%).

Esto corrige el supuesto B3 de la formulación, que declaraba "una ración estándar por persona-día" como *falsa en rigor*. Es más defendible que eso: **usar `r_k` como cifra por persona-día sobre una población es exactamente el uso previsto por la norma.** El supuesto sigue siendo una simplificación —no distingue subgrupos dentro de la población— pero no es un abuso del estándar.

---

## 3. Por qué tres nutrientes no bastan

La respuesta a "¿son suficientes energía, proteína y grasa?" es **no**, y la evidencia no es teórica.

Las enfermedades carenciales son **el modo de falla documentado de las poblaciones dependientes de raciones**:

| Deficiencia | Enfermedad | Aparece cuando |
|---|---|---|
| Vitamina C | Escorbuto | dieta sin fruta ni verdura fresca por semanas |
| Vitamina B1 (tiamina) | Beriberi | dieta basada en cereal pulido |
| Vitamina B3 (niacina) | Pelagra | dieta basada en maíz sin nixtamalizar |
| Hierro | Anemia | dieta sin carne, con baja biodisponibilidad |
| Vitamina A | Xeroftalmía, ceguera | ausencia de fuentes de retinol o carotenos |
| Yodo | Bocio | sal no yodada |

Hierro, vitamina A y yodo son las tres carencias más frecuentes del mundo. Y hay casos documentados en respuesta humanitaria: se registró un brote de **pelagra en Kuito, Angola, en 2004**, en población dependiente de ayuda alimentaria.

**El riesgo concreto:** una canasta de arroz, pasta, aceite y lenteja puede alcanzar el 100% de energía, proteína y grasa. El modelo la declararía "ración completa". Sostenida seis semanas, produce escorbuto.

Llamar "completa" a esa ración no es una imprecisión: es un error con consecuencia clínica.

---

## 4. Por qué aun así v1 usa tres

Cuatro razones, en orden de peso.

### 4.1 El costo no es computacional, es de datos

Agregar un nutriente al LP es **agregar una fila**. La estructura no cambia, el solver ni se entera. Lo que cuesta es `n_ik`: pasar de 3 nutrientes × 30 alimentos = 90 valores, a 22 × 30 = **660 valores**.

Y no son 660 valores equivalentes. El contenido de micronutrientes es mucho más variable e incierto que el de macronutrientes: depende de variedad, suelo, procesamiento, almacenamiento y fortificación. Un dato malo en una restricción activa produce una recomendación mala con apariencia de rigor.

### 4.2 El horizonte temporal de un acopio

La distinción es entre:

- **Población 100% dependiente de la ración durante meses** → los 22 requerimientos son obligatorios. Es el caso para el que Esfera fue escrito.
- **Acopio ciudadano en fase aguda, complementando lo que la gente todavía tiene, durante días o semanas** → el modelo de macronutrientes es defendible.

El acopio ciudadano es el segundo caso. **Pero eso hay que declararlo, no asumirlo**, y deja de valer en cuanto la operación se prolonga.

### 4.3 Con micronutrientes duros, el modelo daría cero

La vitamina C de arroz, pasta, harina, lenteja, frijol, aceite y leche en polvo es **prácticamente cero**. Si se añade la adecuación de vitamina C como restricción `≥`, el problema se vuelve **infactible**: `D = 0`.

Eso no es un defecto del modelo. Es un hallazgo:

> **Una canasta de donación ciudadana de productos secos no puede constituir una ración nutricionalmente completa a ningún volumen.** Hace falta alimento fresco, producto fortificado o suplementación.

Por eso las raciones humanitarias reales incluyen mezcla fortificada tipo CSB+, aceite fortificado con vitaminas A y D, y **sal yodada**. No es un lujo: es la única forma de cerrar el balance.

Ese resultado solo aparece si se modelan los micronutrientes.

### 4.4 Los topes de aceptabilidad todavía no están calibrados

`a_i` es el parámetro más débil del modelo y se calibra en campo. Añadir 19 nutrientes sobre una base sin calibrar multiplica la incertidumbre en vez de reducirla.

---

## 5. Decisión: capa de diagnóstico, no de restricción

Ni ignorar los micronutrientes ni convertirlos en restricción dura. La salida es una tercera vía:

### v1.1 — micronutrientes como reporte

1. Las restricciones del LP siguen siendo energía, proteína y grasa. `D` se calcula igual.
2. **Después** de resolver, se calcula la cobertura de cada micronutriente sobre la ración resultante:

   ```
   cobertura_k  =  ( Σ_i n_ik · x_i / D )  /  r_k
   ```

3. Se reporta junto a `D`, con semáforo. Ejemplo de salida:

   > **D = 1.125 días-persona**
   > ⚠ Vitamina C: **0% del requerimiento**. Riesgo de escorbuto si la dependencia supera 4 semanas.
   > ⚠ Vitamina A: 12%. ⚠ Yodo: 0% — usar sal yodada.
   > ✓ Hierro: 78%. ✓ Zinc: 91%.

**Ventajas:** no puede volver infactible el problema, no depende de datos que hoy no existen para operar, y convierte cada carencia en un pedido concreto — que es justamente lo que el motor de petición debe producir.

Y da una segunda lista de compras, distinta de la del precio sombra: no "qué maximiza raciones", sino **"qué evita enfermedad"**.

### v2 — restricciones blandas

Convertir los micronutrientes en restricciones con variable de holgura penalizada, en lugar de `≥` duras. El modelo puede violarlas, pero paga por hacerlo, y el dual de esa holgura dice cuánto vale cerrar cada brecha. Es la formulación correcta a mediano plazo y no rompe la linealidad.

---

## 6. Cómo hay que decirlo

En cualquier publicación, la frase honesta es:

> El modelo verifica adecuación de **energía, proteína y grasa** según el estándar Esfera, y **reporta** la cobertura de micronutrientes sin optimizarla. Una ración que el modelo declare completa lo es en términos de macronutrientes. Para dependencia prolongada se requiere además adecuación de micronutrientes, que una canasta de productos secos donados no puede alcanzar sin alimento fresco o fortificado.

Sin ese párrafo, la palabra "completa" promete más de lo que el modelo entrega. Con él, la limitación se convierte en un hallazgo.

---

## 7. Tareas derivadas

| Tarea | Descripción |
|---|---|
| **F1.1b** | Transcribir el Apéndice 6 de Esfera desde el PDF oficial, con cita de página |
| **F1.8** | Capa de diagnóstico de micronutrientes (cobertura + semáforo) |
| **F1.9** | Verificar el resultado de infactibilidad por vitamina C y documentarlo como hallazgo |
| **F0.13** | Consultar a un nutricionista sobre el corte temporal: ¿a partir de cuántas semanas deja de ser defendible un modelo de solo macronutrientes? |

La última es pregunta para las entrevistas de Fase 0, no para el escritorio.

---

## Fuentes

- [The Sphere Handbook (2018) — Food Security and Nutrition, Apéndice 6 "Nutritional requirements"](https://spherestandards.org/wp-content/uploads/Sphere-Handbook-2018-EN.pdf)
- [Manual Esfera interactivo](https://handbook.spherestandards.org/en/sphere/)
- [Seal A. y Thurstans S. (2013). *Derivation of nutrient requirements for disaster-affected populations: Sphere Project 2011.* Food and Nutrition Bulletin 34(1) — resumen en ENN](https://www.ennonline.net/fex/47/en/derivation-nutrient-requirements-disaster-affected-populations-sphere-project-2011)
- [WFP — Food and Nutrition Handbook (2018)](https://emergency.unhcr.org/sites/default/files/2024-01/Food%20and%20Nutrition%20Handbook_WFP%202018.pdf)
- [OMS — Addressing nutrition in emergencies](https://www.who.int/activities/addressing-nutrition-in-emergencies)
