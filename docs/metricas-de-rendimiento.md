# Cómo mide su rendimiento un centro de acopio

**Especificación de métricas · v1**
27 de agosto de 2026

---

## 0. La pregunta

Gravitas y las demás plataformas responden *"¿dónde hay un acopio y qué recibe?"*. Es el flyer, digitalizado. La pregunta sin responder es la del que **opera** el acopio:

> Recibí 40 toneladas. ¿Lo hice bien?

Hoy nadie puede contestarla, porque no existe ninguna definición operativa de "bien" para un centro de acopio. Este documento propone una.

---

## 1. El caso mínimo: dos alimentos

Un acopio con 100 kg de arroz y 2 kg de aceite puede armar 65 raciones completas. La cuenta intuitiva dice que para esas 65 raciones bastan 33 kg de arroz y que sobran 67, porque solo mira la energía.

Es incorrecto. La grasa —que es la restricción activa— exige usar **todo** el arroz: sus 600 g de grasa hacen falta para llegar a los 2.600 g que requieren 65 raciones.

Resuelto como LP:

```
D óptimo = 65 raciones
  usa 100,00 kg de arroz  → 100% del inventario
  usa   2,00 kg de aceite → 100% del inventario
duales: energía = 0 · grasa = 0,025 raciones/g
```

No sobra un gramo de masa. **El desperdicio existe, pero no es masa: es capacidad nutricional varada.**

| | |
|---|---|
| Techo por energía | 180 raciones |
| Techo por grasa | 65 raciones |
| **Días-persona de energía varados** | **115** |
| Aceite necesario para desbloquearlos | **4,6 kg** |

Ciento quince días-persona de comida completa están inmovilizados por faltar cuatro kilos y medio de aceite. Eso cuesta menos de 60.000 pesos.

La lectura correcta no es "sobra arroz". La donación no es excesiva: está desbalanceada, y el faltante es barato y específico.

### Sobre el rango de validez del precio sombra

Verificado numéricamente: el aceite vale 25 raciones/kg **solo hasta los 4,6 kg adicionales**. Después la energía se vuelve la restricción activa y el valor cae.

| Aceite adicional | D resultante | Valor marginal acumulado |
|---|---|---|
| +4,0 kg | 165 | 25,0 /kg |
| **+4,6 kg** | **180** | **25,0 /kg** |
| +7,0 kg | 210 | 20,7 /kg |
| +10,0 kg | 223 | 15,8 /kg |

Un precio sombra **no es una constante, es una pendiente local**. Publicar "el aceite vale 25" sin decir "hasta 4,6 kg" produce sobrepedido — la segunda ola otra vez, ahora provocada por el propio modelo. **Todo pedido debe llevar cantidad máxima, no solo prioridad.**

---

## 2. El principio de diseño, sacado de las dos auditorías

La UNGRD tiene los campos de ayuda entregada: vacíos en el 98–99,7%. Gravitas tiene `needs_total`, `needs_cubiertas`, `needs_abierta`: vacíos en el 100%.

> **Todo campo que exista y no sea imprescindible para operar, quedará vacío.**

De ahí la regla: **no se captura nada que pueda calcularse.** El acopio registra hechos físicos que de todos modos ocurren, y las métricas se derivan. Si una métrica exige un campo nuevo, la métrica está mal diseñada.

---

## 3. El libro mayor mínimo

Tres eventos. Nada más.

**ENTRADA** — `fecha · ítem · cantidad · unidad · donante(opcional)`
**SALIDA** — `fecha · ítem · cantidad · unidad · municipio destino · receptor`
**MERMA** — `fecha · ítem · cantidad · unidad · causal`

Causales de merma: `vencido · deteriorado · no apto · sin uso · desconocido`.

Cinco campos por evento. Un voluntario con un celular lo diligencia en veinte segundos. **Todo lo que sigue se calcula sobre estas tres tablas más una tabla nutricional de referencia.**

---

## 4. Las métricas

### M1 · Rendimiento nutricional — la métrica principal

```
R  =  D_despachado  /  D_máximo_posible
```

- `D_despachado`: días-persona de ración completa efectivamente enviados, calculados sobre las salidas.
- `D_máximo_posible`: el óptimo del LP sobre todo lo que entró.

Responde: **del potencial nutricional que entró por la puerta, ¿cuánto se convirtió en comida completa despachada?**

Un acopio con R = 0,4 recibió mucho y convirtió poco. Uno con R = 0,9 operó cerca del límite de lo que su donación permitía. Es comparable entre acopios de tamaños distintos porque es un cociente.

### M2 · Capacidad varada

```
V  =  D_techo_energía  −  D_alcanzable
```

Los 115 días-persona del ejemplo. Se reporta junto con **el pedido que la desbloquea**: `4,6 kg de aceite`. Es la métrica que convierte un diagnóstico en una acción.

### M3 · Tasa de merma

```
Merma  =  masa descartada  /  masa recibida
```

Desagregada por causal. **Es la medición directa de la segunda ola**, y hoy no existe en ninguna parte de Colombia.

### M4 · Tiempo de permanencia

```
P  =  mediana(fecha_salida − fecha_entrada)
```

Bajo supuesto PEPS. Es el mismo indicador de latencia calculado sobre los datos de la UNGRD, pero medible de verdad: ambas fechas las genera el propio acopio.

### M5 · Dispersión de destino

Número de municipios distintos atendidos y porcentaje despachado al destino principal.

Detecta el patrón que Gravitas está documentando sin nombrarlo: todo converge al mismo sitio mientras otros quedan sin nada.

### M6 · Precio sombra vigente

No es una métrica de desempeño: es la **salida operativa**. Lista corta de ítems con su valor marginal en raciones por unidad **y su cantidad máxima útil**.

---

## 5. Lo que un acopio NO puede medir solo

Hay que decirlo de frente, porque prometer más destruye la credibilidad del resto.

| No medible | Por qué |
|---|---|
| Si la ayuda llegó a quien la necesitaba | Requiere el extremo receptor, no el emisor |
| Cumplimiento contra la necesidad real | Requiere una señal de demanda que no existe |
| Duplicación entre acopios | Requiere la red, no el nodo |
| Impacto en bienestar | Fuera de alcance de cualquier sistema logístico |

**Un acopio puede medir la eficiencia de su conversión, no la eficacia de la ayuda.** Es una distinción incómoda y es correcta. Pasar de cero a M1–M5 ya es enorme; llamarlo "impacto" sería exagerar.

---

## 6. De flyer a objetivo

Así se ve hoy un acopio publicado:

> *Centro de acopio Universidad X. Carrera 38 #5-91. Recibimos alimentos no perecederos, ropa en buen estado y elementos de aseo.*

Así se vería con el modelo detrás:

> **Centro de acopio Universidad X** — Carrera 38 #5-91
> Objetivo: 500 días-persona de ración completa para Quibdó.
> Alcanzado: 65. Varado por desbalance: 115.
> **Falta ahora:** aceite — 1 litro = 25 raciones · **máximo útil 4,6 L**
> Después de eso: lenteja — 1 kg = 3,1 raciones · máximo útil 40 kg
> Rendimiento actual: R = 0,36 · Merma: 4% · Permanencia mediana: 6 días

Lo segundo es un acopio con objetivo. Y la diferencia entera cabe en una frase:

> **El flyer dice qué se puede llevar. El modelo dice qué falta, cuánto vale y cuándo parar.**

Ese "cuándo parar" no lo tiene nadie hoy, y es la mitad del problema de la segunda ola.

---

## 7. Dos refinamientos del modelo

### 7.1 Objetivo lexicográfico

Maximizar solo `D` puede dejar masa despachable inmovilizada cuando hay holgura. La formulación correcta es en dos etapas:

1. Maximizar `D`.
2. Fijar `D = D*` y maximizar la masa despachada sujeta a eso.

Así el acopio manda toda la comida útil, no únicamente la que entra en raciones completas. Cuesta una línea más de código y evita una recomendación absurda en el mundo real.

### 7.2 La red de acopios — donde está el verdadero valor

El LP de un acopio aislado resuelve un problema pequeño. **El problema grande es entre acopios.**

Si el acopio A tiene aceite con precio sombra 3 y el acopio B lo tiene en 25, mover ese aceite de A a B genera 22 raciones por kilo **sin una sola donación nueva**. Los precios sombra convierten el trueque entre bodegas en una cuenta aritmética.

Esa es la extensión natural —un problema de transbordo— y es lo que de verdad resuelve "todos mandaron arroz a Quibdó". Pero **solo funciona si varios acopios llevan el libro mayor.**

Un mapa muestra dónde están los acopios; el registro es lo único que permite calcular si sirvieron, y lo único que habilita la red.

---

## 8. Qué construir primero

1. Las tres tablas del libro mayor, en papel y en hoja de cálculo. Sin software.
2. La tabla nutricional de referencia para los 20–30 ítems que realmente circulan en Colombia.
3. El LP en PuLP que produce M1, M2 y M6 a partir de las tablas.
4. La ficha pública del acopio que muestra objetivo, avance y pedido con tope.
5. Recién entonces, la red.

Los pasos 1 a 4 son un mes de trabajo y no dependen de ninguna respuesta institucional.

---

## Anexo · Verificación numérica

Resuelto con PuLP/CBC sobre el ejemplo de dos alimentos:

| Comprobación | Resultado |
|---|---|
| D óptimo | 65,0 raciones |
| Uso de inventario | arroz 100% · aceite 100% |
| Dual de grasa | 0,025 raciones/g = **25 raciones/kg de aceite** |
| Dual de energía | 0 (restricción no activa) |
| +1 kg de aceite | D = 90,0 → **+25,0** ✓ |
| +1 kg de arroz | D = 65,15 → **+0,15** ✓ |
| Techo por energía | 180 raciones |
| Capacidad varada | 115 días-persona |
| Aceite para desbloquear | 4,6 kg |

Los precios sombra quedan confirmados, y el rango de validez termina en 4,6 kg — el detalle que evita que el motor de petición cause el problema que intenta resolver.
