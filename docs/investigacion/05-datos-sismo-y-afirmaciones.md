# Qué podemos afirmar, qué datos hay del sismo, y por qué el problema no es de velocidad

**Fecha:** 27 de agosto de 2026

---

## 1. Qué podemos afirmar hoy y qué sigue siendo premisa

La distinción importa: si sobreafirmas, la primera entidad que responda con un dato te desmonta el argumento entero. Separemos.

### Afirmable hoy, verificable por cualquiera, sin esperar a nadie

1. **No existe información pública que permita evaluar la oportunidad de la respuesta humanitaria en Colombia.** De 16.036 emergencias registradas por la UNGRD en 2023–2024, el tiempo de respuesta es calculable en 44 (0,27%), y el 12% de esas arroja resultados temporalmente imposibles.
2. **No existe información pública sobre la ayuda entregada.** Los campos existen en los conjuntos de datos y están vacíos en el 98–99,7% de los registros.
3. **La serie pública de emergencias se corta en diciembre de 2024.** No hay dato abierto de 2025 ni 2026.
4. **El SNIGRD publica tableros de trazabilidad logística para agua, saneamiento y maquinaria amarilla, pero no para asistencia humanitaria alimentaria y no alimentaria.** Ninguno de sus 9 datasets abiertos trata de emergencias, respuesta o donaciones.
5. **No existe registro público alguno de lo que entra y sale de un centro de acopio.**

Estas cinco son hechos. Cualquiera puede reproducirlos contra APIs públicas en menos de una hora.

### Premisa, hasta que respondan las entidades

- Que la UNGRD **tampoco tenga** la información internamente.
- Que **no exista** un instrumento de medición de desempeño en algún manual no publicado.
- Que el subregistro obedezca a que no se entregó ayuda y no a que no se registró.

**Recomendación:** afirma lo primero con toda firmeza y formula lo segundo como pregunta abierta. La frase que aguanta cualquier escrutinio es:

> *"No existe información pública que permita evaluar el desempeño logístico de la respuesta humanitaria en Colombia. Radicamos derechos de petición para establecer si existe información no publicada, y este documento se actualizará con las respuestas."*

Esa formulación es más fuerte, no más débil: le pone un plazo a la contraparte y convierte cualquier respuesta —incluido el silencio— en evidencia. Es exactamente para lo que sirven las peticiones ya radicadas.

---

## 2. Qué datos existen realmente sobre el sismo del 10 de agosto

Más de lo que esperabas. Y esto cambia el diagnóstico del proyecto.

### Evaluación de daños georreferenciada

| Fuente | Qué es | Estado |
|---|---|---|
| **Copernicus EMS — activación EMSR916** | Rapid Mapping de daños por sismo solicitado **el mismo 10 de agosto**. Cobertura declarada: Quibdó, Pereira, Manizales, Cali. Cartografía de delineación y de graduación de daños, gratuita y descargable en vectorial | Activo · [Situational reporting](https://storymaps.arcgis.com/stories/faac12172e564e31b558b1dff08c91d6) |
| **UNOSAT / UNITAR** | *Building Damage Assessment in Viterbo Town, Caldas* — evaluación **edificio por edificio** con imagen satelital, fecha de datos 12 de agosto | Publicado en HDX el 14 de agosto, actualizado el 16. Formatos **GeoJSON, SHP, CSV, Geodatabase**. Licencia CC-BY-SA |
| **USGS** — evento `us6000tjl2` | ShakeMap de intensidad y PAGER con estimación de población expuesta por nivel de sacudida | Público desde el día 1 |
| **SGC — Servicio Geológico Colombiano** | Localización, profundidad (103 km) y catálogo de réplicas | Público |

### Evaluación de necesidades y situación

| Fuente | Qué aporta |
|---|---|
| **OCHA — Flash Updates** (002 del 10 de agosto en adelante) | Afectación por departamento y municipio. Sectores prioritarios identificados: alojamiento, salud, seguridad alimentaria, educación y protección |
| **OPS/OMS — Informe de Situación 1** | Sector salud: afectación de centros, capacidad hospitalaria |
| **Análisis de Género Rápido** (13 de agosto) | Necesidades diferenciadas por género |
| **ONU Colombia** — página de actualizaciones | Consolidado de agencias |
| **UNGRD** — reportes de situación | Cifras oficiales: fallecidos, heridos, viviendas destruidas y averiadas, municipios |
| **HDX — CODs de Colombia** | Límites administrativos y población de referencia, para cruzar cualquier cosa |

### Lo que NO existe, y es justamente lo tuyo

- Qué entró a cada centro de acopio.
- Qué salió, hacia dónde y cuándo.
- Qué se descartó por inservible o vencido.
- Qué comunidad ya fue atendida y cuál no.
- Qué necesita hoy cada comunidad, en unidades y cantidades.

**Ninguna de las fuentes anteriores toca el flujo de donaciones.** Miden el daño y estiman la necesidad sectorial. Nadie mide la respuesta ciudadana.

---

## 3. ¿Es poco realista querer estos datos tan rápido?

No. Y la evidencia es incómoda: **la información ya se produjo, y rápido.**

- Copernicus se activó **el mismo día del sismo**.
- UNOSAT publicó una evaluación de daños **edificio por edificio** cuatro días después del evento, en formato descargable y con licencia abierta.
- OCHA publicó afectación desagregada por departamento **el día 1**.

O sea que mientras los centros de acopio se llenaban de ropa usada, ya existía una capa vectorial pública que decía qué edificios estaban destruidos en Viterbo.

### Por eso hay que corregir la hipótesis

Tu planteamiento fue: *los acopios se crearon sin plan de riesgo, entonces las donaciones se hicieron donde se creyó correcto, no con un objetivo.* Es correcto en el efecto, pero la causa es otra.

**El problema no es que la información no exista. Es que no llega.**

La información de daños y necesidades se produce en GeoJSON sobre HDX, en StoryMaps de ArcGIS, en PDF bilingües de OCHA y en cartografía de Copernicus. El voluntario que coordina un acopio en Cali no sabe que esa capa existe, no la podría abrir si la tuviera, y aunque pudiera, no le diría cuántos kits de aseo pedir.

Hay un abismo entre dos mundos que nunca se tocan:

| Mundo de la evaluación | Mundo del acopio |
|---|---|
| Satélite, GIS, clusters, agencias ONU | Iglesia, junta de acción comunal, colegio, empresa |
| Produce GeoJSON y PDF en 48–96 horas | Produce camiones en 12 horas |
| Sabe dónde está el daño | Tiene los bienes |
| No mueve bienes | No sabe hacia dónde moverlos |

**No hay tubería entre los dos.** Esa ausencia de tubería es el proyecto.

### Consecuencia para el diseño

Cambia lo que hay que construir. No es un sistema de evaluación —ese existe y funciona razonablemente— ni un sistema de inventario —ese es SUMA y le pertenece a la institucionalidad—. Es **el puente**:

1. Traducir la evaluación existente a una lista de necesidades en unidades que un acopio entienda (kits, litros, colchonetas), por municipio.
2. Registrar de forma estandarizada lo que cada acopio recibe y despacha.
3. Devolver la agregación para que se vea qué comunidad quedó sin cubrir y cuál recibió tres veces.

Los pasos 1 y 3 solo son posibles si el paso 2 existe. **El paso 2 son tus hojas.** Ese es el orden correcto de construcción, y explica por qué la fase de campo importa tanto: sin adopción en el acopio, los otros dos pasos no tienen insumo.

---

## 4. Sobre "evaluación y luego acción"

El modelo secuencial —evaluar, después actuar— es correcto en teoría y no funciona en las primeras 72 horas. La donación ciudadana se moviliza por impulso emocional en las primeras horas, mucho antes de que exista cualquier evaluación formal. Pelear contra eso es perder.

Lo que sí funciona, y está documentado en la literatura de *material convergence*, es **gestionar la demanda en el origen**: mensajería temprana que canalice el impulso hacia donación monetaria y hacia bienes específicamente solicitados, en lugar de intentar ordenar la avalancha una vez que llegó al acopio.

Traducido a tu proyecto: la lista de necesidades no sirve solo para despachar bien. **Sirve, sobre todo, para decirle a la gente qué donar antes de que done.** Ese es el punto de mayor apalancamiento de todo el sistema, y es barato.

---

## Fuentes

- [Copernicus EMS — Earthquake in Colombia, EMSR916](https://mapping.emergency.copernicus.eu/news/earthquake-in-colombia-emsr916/)
- [UNOSAT — Building Damage Assessment in Viterbo Town, Caldas (HDX)](https://data.humdata.org/dataset/building-damage-assessment-in-viterbo-town-caldas-department-colombia-as-of-12-august-2026)
- [OCHA — Colombia Flash Update 002, 10 de agosto de 2026](https://www.unocha.org/publications/report/colombia/colombia-flash-update-002-afectaciones-por-terremoto-en-12-departamentos-de-colombia-10-agosto-de-2026-spen)
- [OPS/OMS — Informe de Situación 1, Colombia terremoto agosto 2026](https://www.paho.org/es/documentos/informe-situacion-1-colombia-terremoto-agosto-2026-10-agosto-2026)
- [USGS — M 7.4, 5 km S of San José del Palmar](https://earthquake.usgs.gov/earthquakes/eventpage/us6000tjl2)
- [ONU Colombia — información y actualizaciones sobre el terremoto](https://colombia.un.org/es/320793-informaci%C3%B3n-y-actualizaciones-sobre-el-terremoto-en-colombia)
- [Análisis de Género Rápido — terremoto de Colombia](https://www.learning.foundation/es/2026/08/13/analisis-de-genero-rapido-terremoto-de-colombia-10-de-agosto-de-2026/)
- [OCHA Colombia — Humanitarian Data Exchange](https://data.humdata.org/organization/ocha-colombia)
- [Reducing material convergence in disaster environments — ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1366554522001272)
