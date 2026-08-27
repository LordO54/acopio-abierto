# Modelo de ensamblaje alimentario en centro de acopio

**Formulación v2 · componente alimentos**
27 de agosto de 2026

---

## 1. Enunciado

Un centro de acopio recibe donaciones heterogéneas de alimentos, en cantidades que no controla. Debe decidir **qué combinación de lo que tiene despachar**, y **qué pedir a continuación**.

Formalmente:

> Dado un inventario de insumos con composición nutricional conocida, un requerimiento nutricional diario por persona y límites de aceptabilidad por insumo, determinar la asignación que maximiza el número de días-persona de ración nutricionalmente completa, y el valor marginal de cada insumo adicional.

La unidad de medida del resultado es **el día-persona de ración completa**, no el kilogramo. Ese cambio de unidad es la decisión de diseño más importante del modelo.

---

## 2. Conjuntos, parámetros y variables

### Conjuntos

| Símbolo | Significado |
|---|---|
| `i ∈ I` | insumos alimentarios disponibles |
| `k ∈ K` | nutrientes considerados (energía, proteína, grasa) |

### Parámetros — datos, no decisiones

| Símbolo | Significado | Unidad | Origen |
|---|---|---|---|
| `q_i` | inventario disponible del insumo `i` | g | libro mayor del acopio |
| `n_ik` | contenido del nutriente `k` por gramo de `i` | g o kcal / g | tabla de composición (ICBF / FAO) |
| `r_k` | requerimiento diario del nutriente `k` por persona | g o kcal | norma Esfera |
| `a_i` | máximo aceptable del insumo `i` por persona-día | g | criterio nutricional y cultural |

### Variables de decisión

| Símbolo | Significado | Dominio |
|---|---|---|
| `x_i` | gramos del insumo `i` asignados al armado de raciones | `x_i ≥ 0` |
| `D` | días-persona de ración completa producidos | `D ≥ 0` |

`D` es variable, no parámetro. Esa es la diferencia entre este modelo y una receta.

---

## 3. Formulación

### Etapa 1 — maximizar raciones completas

```
max   D

s.a.  Σ_i  n_ik · x_i  ≥  r_k · D        ∀ k ∈ K      (adecuación nutricional)
      x_i  ≤  q_i                        ∀ i ∈ I      (disponibilidad)
      x_i  ≤  a_i · D                    ∀ i ∈ I      (aceptabilidad)
      x_i ≥ 0,  D ≥ 0
```

Tres familias de restricciones, todas lineales.

- **Adecuación**: lo aportado de cada nutriente debe cubrir lo que exigen `D` personas.
- **Disponibilidad**: no se usa más de lo que hay.
- **Aceptabilidad**: nadie come 900 g de aceite. Sin esta restricción el modelo produce recomendaciones absurdas. Nótese que `a_i · D` es lineal porque `a_i` es constante — la restricción acopla `x_i` con `D` sin romper la linealidad.

Si algún nutriente tiene tope superior —sodio, azúcar—, se agrega `Σ_i n_ik x_i ≤ r̄_k · D`. La estructura no cambia.

### Etapa 2 — no dejar comida en la bodega

Maximizar `D` solo puede dejar inmovilizada masa despachable. Se resuelve con un segundo LP:

```
max   Σ_i  x_i
s.a.  las mismas restricciones, con D fijado en D*
```

Como las restricciones nutricionales son de tipo `≥`, es posible aumentar la masa manteniendo `D = D*`. El acopio despacha toda la comida útil, no solo la que cierra raciones exactas.

**El orden importa y es una decisión ética explícita:** primero completitud nutricional, después volumen. Invertirlo produce el comportamiento actual —repartir bulto— con apariencia de optimización.

---

## 4. El dual: el motor de petición

Asociando `y_k` a adecuación, `λ_i` a disponibilidad y `μ_i` a aceptabilidad:

```
min   Σ_i  q_i · λ_i

s.a.  Σ_k  r_k · y_k  −  Σ_i  a_i · μ_i  ≥  1
      λ_i  +  μ_i  ≥  Σ_k  n_ik · y_k              ∀ i
      y, λ, μ  ≥  0
```

De la segunda familia, en el óptimo:

```
λ_i  =  max( 0 ,  Σ_k n_ik · y_k  −  μ_i )
```

**Lectura, que es el corazón del modelo:**

> El valor marginal de un alimento es el valor de los nutrientes que aporta, **menos** lo que se pierde porque la gente no puede comer cantidades ilimitadas de él.

Y por holgura complementaria:

- Si sobra el insumo `i` en la bodega → `λ_i = 0` → **pedir más de eso no sirve de nada**.
- Si el insumo `i` topó su límite de aceptabilidad → `μ_i > 0` cancela su valor nutricional bruto → **tampoco sirve**.

Las dos reglas que hoy nadie aplica salen como consecuencia matemática, no como opinión.

---

## 5. Premisas

### A. Premisas verificadas — establecidas por la investigación previa

| # | Premisa | Evidencia |
|---|---|---|
| A1 | No existe registro público del flujo de donaciones en Colombia | Campos de ayuda entregada vacíos en 98,0% (2019–22) y 99,7% (2023–24) de los registros de la UNGRD |
| A2 | Todo campo opcional queda vacío | UNGRD 98–99,7%; Gravitas: `needs_total`, `needs_cubiertas`, `needs_abierta` en 0% de los registros |
| A3 | Las plataformas existentes describen acopios, no los operan | Auditoría de Gravitas: 184 de 198 reportes son fichas de ubicación sin datos de flujo |
| A4 | Las normas de referencia son públicas y estables | Esfera: 2.100 kcal, ≥10% de la energía en proteína, ≥17% en grasa |
| A5 | La donación ciudadana llega desbalanceada, no escasa | Literatura de *material convergence*; sesgo geográfico de Gravitas (96 reportes en ciudades no afectadas vs 13 en las afectadas) |

**Consecuencia de A1–A3:** `q_i` no se puede obtener de ninguna fuente existente. El modelo obliga a crear el libro mayor. No es un requisito del modelo: es su aporte.

### B. Supuestos del modelo — asunciones falsables

| # | Supuesto | Solidez |
|---|---|---|
| B1 | Los nutrientes se suman sin interacción | Muy alta. No hay sinergia que genere calorías extra |
| B2 | Los insumos son divisibles (33,7 kg es válido) | Alta a granel. Falsa para latas, con error despreciable a escala de tonelada |
| B3 | Una ración estándar por persona-día | Falsa en rigor —niños, gestantes, enfermos— pero es la convención de Esfera y la usa todo el sector |
| B4 | El inventario está disponible simultáneamente | Requiere el libro mayor al día |
| B5 | La aceptabilidad se expresa como tope lineal por persona-día | Simplificación de un fenómeno cultural. Es el parámetro más discutible y debe calibrarse en campo |

### C. Lo que el modelo ignora deliberadamente

| # | Ignora | Por qué se puede |
|---|---|---|
| C1 | Micronutrientes y preferencia cultural específica | Ampliable agregando filas a `K`; no cambia la estructura |
| C2 | Costo, transporte y capacidad de bodega | Otro problema, otro modelo. Mezclarlos ahora impide validar este |
| C3 | Caducidad y dimensión temporal | El primer refinamiento necesario tras la validación en campo |
| **C4** | **Demanda real por comunidad** | **`D` es capacidad de oferta, no cobertura de necesidad. El modelo dice cuántas raciones puedo armar, no cuántas hacen falta** |

**C4 es la limitación que hay que declarar en voz alta.** No existe señal de demanda por comunidad en Colombia —eso es lo que estableció toda la investigación previa—. El modelo mide lo que el acopio hace con lo que tiene. No mide si eso alcanzó.

---

## 6. Instancia numérica

Inventario típico de acopio ciudadano, con el sesgo real hacia cereales. Resuelto con PuLP/CBC.

| Insumo | Inventario (kg) | Usado (kg) | % uso | g/persona-día | Tope |
|---|---|---|---|---|---|
| Arroz | 2.000,0 | 450,2 | 23% | **400,0** | 400 |
| Pasta | 400,0 | 225,1 | 56% | **200,0** | 200 |
| Harina de maíz | 300,0 | 300,0 | 100% | 266,6 | 300 |
| Panela | 250,0 | **0,0** | 0% | 0,0 | 60 |
| Frijol | 120,0 | 120,0 | 100% | 106,6 | 120 |
| Lenteja | 80,0 | 80,0 | 100% | 71,1 | 120 |
| Atún en lata | 60,0 | 60,0 | 100% | 53,3 | 120 |
| Leche en polvo | 30,0 | 30,0 | 100% | 26,7 | 60 |
| Aceite | 25,0 | 25,0 | 100% | 22,2 | 40 |
| **Total** | **3.265,0** | **1.290,3** | **40%** | | |

**Resultado: D\* = 1.125 días-persona de ración completa a partir de 3,3 toneladas.**

### Restricción activa

Solo una: **grasa**, con `y_grasa = 0,0289` raciones por gramo.

### Precios sombra — verificados numéricamente

| Insumo | Raciones por kg adicional |
|---|---|
| **Aceite** | **28,90** |
| Leche en polvo | 7,80 |
| Frijol | 0,35 |
| Harina de maíz / lenteja / atún | 0,29 |
| **Arroz** | **0,00** |
| **Pasta** | **0,00** |
| **Panela** | **0,00** |

La estructura dual se confirma exactamente. El arroz aporta 0,006 g de grasa por gramo, que a `y_grasa` valen 0,000173 — pero su dual de aceptabilidad es **también** 0,000173, y ambos se cancelan:

```
λ_arroz = 0,000173 − 0,000173 = 0
```

**El arroz no vale cero porque no alimente. Vale cero porque ya no cabe más arroz en la dieta de nadie.** Eso es exactamente lo que ocurre en un acopio real, y el modelo lo deduce sin que nadie se lo diga.

### Capacidad varada

| | Raciones |
|---|---|
| Techo por energía | 5.583 |
| Techo por proteína | 5.142 |
| **Alcanzado** | **1.125** |
| **Varado** | **4.016 días-persona** |

### La comparación que resume todo

| Donación adicional | Ganancia |
|---|---|
| **500 kg de arroz** | **+0,0 días-persona** |
| 200 kg de panela | +0,0 días-persona |
| **50 kg de aceite** (~600.000 COP) | **+1.400 días-persona** |

**429 pesos por día-persona adicional de comida completa.**

Media tonelada de arroz no aporta absolutamente nada. Cincuenta kilos de aceite duplican con creces la capacidad del acopio.

### Rango de validez del precio sombra

El aceite vale 28,9 raciones/kg **hasta ~35 kg adicionales**; después cae a 26,6. Un precio sombra es una pendiente local. **Todo pedido publicado debe llevar tope de cantidad**, o el motor de petición genera la segunda ola que intenta evitar.

### Masa no despachable

Etapa 2 eleva la masa despachada de 1.290 a 1.358 kg. Sobre 3.265 kg recibidos, **1.907 kg (58%) no son despachables** dentro de raciones aceptables — casi todo arroz y panela. Ese 58% es la segunda ola, cuantificada en una bodega concreta.

---

## 7. El valor que resulta

### 1 · Una cifra comparable donde no había ninguna

`D` convierte "recibimos 40 toneladas" en "podemos alimentar completo a 1.125 personas por un día". Comparable entre acopios de distinto tamaño, agregable a nivel de ciudad, y con significado para cualquier persona.

### 2 · El pedido correcto, gratis

El dual entrega qué pedir, en qué orden, cuánto vale y hasta qué cantidad — sin construir nada aparte. Es un subproducto de haber modelado bien, no un módulo adicional.

Un acopio pasa de *"recibimos alimentos no perecederos"* a *"necesitamos 35 litros de aceite; cada litro son 29 raciones; después de eso, leche en polvo"*.

### 3 · El argumento político, con número

*"El 58% de lo donado no puede convertirse en comida completa, y 4.016 días-persona están varados por faltar 50 kg de aceite"* es una frase que mueve voluntades. *"Falta coordinación"* no.

### 4 · La red — donde está el valor grande

Si el acopio A tiene aceite con `λ = 0,35` y el acopio B lo tiene en `28,90`, mover ese aceite genera 28,5 raciones por kilo **sin una sola donación nueva**. Los precios sombra vuelven aritmética el intercambio entre bodegas.

Es la extensión natural del modelo —un problema de transbordo— y es lo único que resuelve de verdad el patrón "todos mandaron arroz al mismo sitio". **Requiere que varios acopios lleven el libro mayor**, y por eso el registro, no el mapa, es el activo defendible.

### 5 · El histórico que hoy no existe

Cada corrida deja `D`, `R`, merma, permanencia y precios sombra fechados. Al cabo de una emergencia hay una serie. Al cabo de tres, una base de evidencia sobre qué donaciones sirven — **exactamente lo que la investigación demostró que Colombia no tiene**.

---

## 8. Qué falta antes de codificar

1. **Tabla de composición** de los 25–30 ítems que realmente circulan, con fuente citada (ICBF).
2. **Calibrar `a_i`** — el parámetro más débil. Se calibra en las entrevistas de Fase 0, no en el escritorio.
3. **Decidir `K`.** Empezar con energía, proteína y grasa. Micronutrientes después.
4. **Análisis de sensibilidad**: si mover `a_i` un 30% cambia el orden del pedido, ese pedido no se publica.
5. **Validar con una bodega real** antes de generalizar.

---

## Anexo · Reproducibilidad

Resuelto con PuLP + CBC. Parámetros nutricionales por gramo, requerimientos Esfera (2.100 kcal · 52,5 g proteína · 40 g grasa), topes de aceptabilidad declarados en el cuerpo del documento.

Comprobaciones:

| Verificación | Resultado |
|---|---|
| `D*` | 1.125,4 |
| Única restricción nutricional activa | grasa, `y = 0,028902` |
| `λ_aceite` = `1,0 × y_grasa` | 0,028902 /g = **28,90 /kg** ✓ |
| `λ_leche` = `0,27 × y_grasa` | 0,007803 /g = **7,80 /kg** ✓ |
| `λ_arroz` = `0,006 y − μ_arroz` | 0,000173 − 0,000173 = **0** ✓ |
| `λ_pasta` = `0,015 y − μ_pasta` | 0,000434 − 0,000434 = **0** ✓ |
| +1 kg aceite (perturbación directa) | +28,90 raciones ✓ |
| +500 kg arroz | +0,0 raciones ✓ |

Los precios sombra calculados por dualidad coinciden con la perturbación directa del inventario en todos los casos.
