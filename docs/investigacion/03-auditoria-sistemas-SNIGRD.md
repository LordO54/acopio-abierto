# Auditoría de sistemas de información — SNGRD / UNGRD

**Fecha de auditoría:** 27 de agosto de 2026
**Método:** consulta directa a endpoints públicos (API Socrata de datos.gov.co, portales UNGRD) y análisis de metadatos
**Alcance:** verificación empírica, no revisión documental

---

## Resumen ejecutivo

Tres hallazgos, en orden de importancia:

1. **Los campos para registrar la ayuda entregada ya existen en los datos públicos, y están vacíos en el 98–99% de los casos.** No es un problema de diseño de sistema. Es un problema de alimentación del sistema.

2. **La serie pública se corta en diciembre de 2024.** No hay dato abierto de emergencias para 2025 ni 2026 — incluido el sismo del 10 de agosto.

3. **Sí es posible calcular el tiempo de ciclo, aunque de forma marginal.** El dataset 2023–2024 trae fechas de activación y de aprobación, pero solo están diligenciadas en el 0,27% de los registros.

---

## 1. Coexisten dos SNIGRD

| | SNIGRD legado | SNIGRD nuevo |
|---|---|---|
| URL | `gestiondelriesgo.gov.co/snigrd` | `sni.gestiondelriesgo.gov.co` |
| Tecnología | ASP.NET WebForms, © 2014 | Aplicación JavaScript de página única |
| Estado | En línea y **aún enlazado** desde el portal institucional vigente | Lanzado en mayo de 2026 |
| Contenido verificable | Consolidados anuales 1998–2017, enlaces a servicios en IPs desnudas (`190.60.210.210`, `190.60.233.206`), Google Crisis Map (servicio descontinuado por Google), visores ArcGIS | Aplicación Angular, WCAG 2.1 AA, catálogo de datos abiertos y Portal BI. **Auditado en detalle — ver sección 1b** |

El portal de la UNGRD todavía apunta al sistema viejo bajo la etiqueta "Sistema Nacional de Información". Los dos conviven sin señalización de cuál es el vigente.

---

## 1b. Auditoría del SNIGRD nuevo

Portal moderno y bien construido: accesibilidad WCAG 2.1 AA declarada, control de contraste y tamaño de texto, versión en inglés, aula virtual de formación. La calidad técnica no es el problema. **El problema es qué decidieron poner adentro.**

### Módulos

| Módulo | Contenido |
|---|---|
| **Datos abiertos** | 9 datasets · 98.994 registros · GeoJSON · CC-BY-4.0 |
| **Portal BI** | Tableros agrupados según los tres procesos de la Ley 1523/2012 |
| **Ficha territorial** | Indicadores y dashboards por departamento |
| **Formulario EDAN** | Diligenciamiento en línea de daños y necesidades |
| **Trámite de certificados RUD** | Enlazado desde el aula virtual |
| Geoportal, geovisores temáticos, MEGIR, Atlas de Riesgo, fuentes de financiación | |

### Los 9 datasets abiertos

| Dataset | Categoría | Registros |
|---|---|---|
| Sedes Institucionales | Institucional | 56.857 |
| **Riesgos Comunitarios 2024–2025** | Amenaza | **21.412** |
| Empresas NATECH | NATECH | 15.341 |
| Accidentes tecnológicos y NATECH | NATECH | 2.862 |
| Índice de Priorización Municipal por Movimientos en Masa | Riesgo | 1.122 |
| Atlas de Riesgo Municipal 2019 | Riesgo | 1.122 |
| Erosión Costera 2025 | Amenaza | 211 |
| Índice de Priorización Departamental por Mov. en Masa | Riesgo | 34 |
| Atlas de Riesgo Departamental 2019 | Riesgo | 33 |

Las categorías disponibles son **Amenaza, Institucional, NATECH y Riesgo**. No existe categoría de manejo de desastres. **Ninguno de los nueve datasets se refiere a emergencias, respuesta, ayuda humanitaria o donaciones.** El catálogo de datos abiertos del SNIGRD nuevo es íntegramente de conocimiento y reducción del riesgo.

> **Hallazgo lateral:** *Riesgos Comunitarios 2024–2025* contiene 21.412 puntos georreferenciados de equipamientos (hospitales, escuelas, viviendas) con los tipos de amenaza a los que está expuesto cada uno, levantados en procesos de **mapeo comunitario**. Es lo más cercano que existe hoy a un inventario de vulnerabilidad a escala comunitaria. Descargable en GeoJSON, EPSG:4326, con diccionario de columnas publicado.

### Portal BI — dónde está el sesgo, con evidencia

Tableros publicados, por proceso de la Ley 1523:

| Proceso | Tableros |
|---|---|
| Conocimiento del riesgo | *"Próximamente · sin dashboards publicados"* — **vacío** |
| Reducción del riesgo | Matriz de asistencia técnica · Proyectos de infraestructura · Control y seguimiento presupuestal |
| **Manejo de desastres** | Distribución territorial de eventos · **Agua potable y saneamiento — Órdenes de proveeduría y Préstamos** · **Maquinaria amarilla — Órdenes de proveeduría** |

**Este es el hallazgo más importante de toda la auditoría.**

El tablero de *Agua potable y saneamiento* hace trazabilidad logística completa: filtro por vigencia, 21 departamentos, **409 asignaciones de carrotanques**, 840 tanques de almacenamiento, **441.613.266 litros por orden de proveeduría** y 94.488.132 litros por préstamo, todo mapeado territorialmente. Lo mismo existe para maquinaria amarilla.

Es decir: **la UNGRD sabe hacer trazabilidad logística, la tiene construida y la publica — pero solo para agua, saneamiento y maquinaria.** No existe un tablero equivalente para asistencia humanitaria alimentaria y no alimentaria: kits, colchonetas, frazadas, carpas. Justamente el flujo donde vive el problema de la segunda ola.

No es una limitación técnica ni presupuestal. Es una decisión sobre qué se considera digno de medirse.

En contraste, el tablero de *Distribución territorial de eventos* **no tiene filtro temporal alguno**: solo permite filtrar por departamento. No se puede saber qué periodo cubre, ni ver una serie de tiempo, ni comparar años. Sus columnas son heridos, desaparecidos, fallecidos, animales afectados, viviendas destruidas y averiadas — ninguna de ayuda entregada.

### Arquitectura técnica

La aplicación es Angular compilada a chunks estáticos. **No hay API REST.** El análisis de las 51 peticiones de red al cargar el catálogo y una ficha de dataset muestra únicamente descarga de JS, CSS, fuentes e imágenes — ninguna llamada a un servicio de datos. La etiqueta "DISPONIBILIDAD API · CC-BY" del encabezado se refiere a la licencia, no a la existencia de una API. Los datasets se sirven como archivos GeoJSON descargables. Los tableros son embebidos de Power BI.

**Consecuencia práctica:** no se puede automatizar la consulta al SNIGRD. Para monitoreo continuo hay que descargar archivos manualmente o raspar la aplicación.

---

## 2. La serie histórica pública está fragmentada

| Periodo | Fuente | Registros | Estado |
|---|---|---|---|
| 1998–2017 | Archivos `.xls`/`.xlsx` sueltos en el SNIGRD legado | — | Un archivo por año, sin esquema común |
| **2018** | — | — | **Hueco** |
| 2019–2022 | `datos.gov.co` · **`wwkg-r6te`** | 25.857 | Congelado el **7 de septiembre de 2023** |
| 2023–2024 | `datos.gov.co` · **`rgre-6ak4`** | 16.036 | Esquema distinto al anterior |
| **2025–2026** | — | — | **Nada público. Incluye el sismo del Chocó.** |

Distribución por año en `wwkg-r6te`: 2019 → 4.436 · 2020 → 3.811 · 2021 → 3.945 · 2022 → 13.665. El salto de 2022 sugiere un cambio de criterio de registro, no un cambio en la realidad.

Los dos datasets **no son compatibles entre sí**: cambian nombres de campo, se agregan columnas (`rud_personas`, `fecha_activacion`, `comentarios`) y se eliminan otras. Cualquier análisis 2019–2024 exige un trabajo de armonización previo.

---

## 3. El hallazgo central: los campos existen, el dato no

Ambos datasets incluyen, **por evento y por municipio**, columnas para la ayuda humanitaria entregada:

`kits de alimento` · `kits de aseo` · `kits de cocina` · `colchonetas` · `frazadas` · `carpas` · `hamacas` · `toldillos` · `juegos de sábanas` · `raciones de campaña` · `agua en galones` · `banco de materiales` · `maquinaria` · `subsidios de arriendo` · `transferencias económicas` — cada uno con su cantidad y su valor.

**Es exactamente lo que solicita el numeral 1 del derecho de petición dirigido a la UNGRD. Ya es público. Y está vacío.**

### Completitud medida

| | 2019–2022 (`wwkg-r6te`) | 2023–2024 (`rgre-6ak4`) |
|---|---|---|
| Registros totales | 25.857 | 16.036 |
| Con **alguna** entrega registrada | **507 (2,0%)** | **47 (0,3%)** |
| Con personas afectadas > 0 | 11.798 | 3.600 |
| **Cobertura del registro de ayuda sobre emergencias con afectación** | **4,3%** | **1,3%** |
| Con datos del RUD (`rud_personas` > 0) | n/a | **78 (0,5%)** |

Volúmenes concentrados en esos pocos registros: **777.452 kits de alimento** en 2019–2022 y **64.452** en 2023–2024.

### Lo que esto significa

Solo hay dos explicaciones posibles:

- **Si sí se entregó ayuda y no se registró** → el sistema de información no refleja la operación. La trazabilidad de la que habla la Contraloría no existe en el dato público.
- **Si efectivamente no se entregó ayuda en el 98% de las emergencias** → la cobertura de la respuesta es mucho menor de lo que se comunica.

Esta es la pregunta que hay que hacerle a la UNGRD, y **se contesta sola en cualquier dirección**.

---

## 4. El tiempo de ciclo sí es calculable, pero solo en el 0,27% de los registros

El dataset 2023–2024 incluye:

- `fecha` — fecha del evento
- `fecha_activacion`
- `fecha_aprobacion_materiales`
- `fecha_aprobacion_maquinaria`

El campo `fecha_activacion` utiliza **dos grafías distintas del mismo valor centinela** —`No registra` (10.561) y `No Registra` (5.423)—, que suman **15.984 de 16.036 registros**. Solo **52 registros (0,32%)** traen una fecha real; de esos, 2 contienen rangos en lugar de fechas y 6 registran una activación anterior al evento. **Latencias calculables: 44 — el 0,27% del dataset.**

El indicador se puede construir, pero no mide el desempeño del sistema: documenta que el sistema no se puede medir. El resultado —mediana de 14 días, media de 41, máximo de 293, sobre 44 casos— **no es una estadística de desempeño sino una prueba de la ausencia de datos**. El cálculo completo está en `04-indicador-latencia.md`.

### El campo `comentarios`

El dataset 2023–2024 trae una bitácora operativa en texto libre por evento, con la secuencia completa de reportes del CDGRD/CMGRD: quién atendió, con cuántas unidades, en qué estado quedó. Es material minable con procesamiento de lenguaje natural y es, con diferencia, la fuente cualitativa más rica y menos explotada del conjunto.

---

## 5. Estado de los sistemas legados

| Sistema | URL | Estado verificado |
|---|---|---|
| **RUD** | `rud.gestiondelriesgo.gov.co` | **Vivo.** Pie de página 2025. Módulos: Reportes · Consultas · Manuales y Formatos · Resoluciones y Circulares · Subsidios de Arriendo · Normativa RAMV · Ver Mapa. El contenido sustantivo exige sesión |
| Consolidados 1998–2017 | SNIGRD legado | En línea, archivos Excel sueltos |
| Geoportal / Tablero de alertas | `190.60.210.210:8080` | Sin respuesta útil — pendiente de verificación |
| Visores geográficos | `190.60.233.206` y ArcGIS Online | Sin verificar |
| Google Crisis Map | Embebido en el SNIGRD legado | **Servicio descontinuado por Google.** Enlace muerto |

---

## 6. Consecuencias para las peticiones ya redactadas

### Modificar el numeral 1 de la petición a la UNGRD

La redacción actual pide inventarios de AHE 2010–2026. Parte de eso ya es público y entregarlo no cuesta nada. Conviene reemplazarla por una formulación que no se pueda responder con un enlace:

> **1. Inventarios de ayuda humanitaria de emergencia.**
> a. Relación de bienes de asistencia humanitaria entregados entre el 1 de enero de **2025** y la fecha, desagregada por municipio, fecha, tipo de bien y cantidad, en formato reutilizable. Se advierte que los conjuntos de datos `wwkg-r6te` y `rgre-6ak4` publicados en datos.gov.co únicamente cubren hasta diciembre de 2024.
> b. Explicar por qué, en el conjunto `wwkg-r6te`, **25.350 de 25.857 registros (98,0%)** no reportan ninguna cantidad de ayuda entregada, y por qué en `rgre-6ak4` ocurre lo mismo en **15.989 de 16.036 registros (99,7%)**. Precisar si ello obedece a que no hubo entrega o a que la entrega no se registró.
> c. Indicar qué dependencia es responsable de diligenciar esos campos, con qué periodicidad y bajo qué procedimiento de control de calidad.
> d. Señalar la fecha prevista de publicación de los datos de 2025 y 2026.

### Agregar a la petición

- Motivo por el cual el conjunto `wwkg-r6te` no se actualiza desde el 7 de septiembre de 2023.
- Criterio que explica el salto de 3.945 registros en 2021 a 13.665 en 2022.
- Razón por la que solo el 0,5% de los registros de 2023–2024 tiene información del RUD asociada.
- Cuál de los dos portales SNIGRD es el vigente y qué pasará con el legado.

### Numeral nuevo, derivado de la auditoría del Portal BI

> **10. Tableros de trazabilidad logística.**
> El Portal BI del SNIGRD publica tableros de órdenes de proveeduría con trazabilidad territorial y filtro por vigencia para *Agua potable y saneamiento* (409 asignaciones de carrotanques, 441.613.266 litros por orden de proveeduría) y para *Maquinaria amarilla*. Se solicita:
> a. Indicar por qué no existe un tablero equivalente para la asistencia humanitaria alimentaria y no alimentaria —kits de alimento, kits de aseo, colchonetas, frazadas, carpas—, y si su construcción está prevista.
> b. Señalar qué sistema transaccional alimenta los tableros de agua y maquinaria, y si ese mismo sistema registra la asistencia humanitaria.
> c. Indicar el periodo cubierto por el tablero *Distribución territorial de eventos*, que no expone filtro temporal.
> d. Precisar si el SNIGRD dispone de una API pública de consulta; en caso negativo, si está prevista.

> **Citar los identificadores exactos de los datasets y los porcentajes medidos cambia el carácter de la petición.** Deja de ser una solicitud genérica de información y pasa a ser una pregunta técnica verificable, mucho más difícil de responder con evasivas.

---

## 7. Recomendación de secuencia

1. **Descargar los dos datasets completos** (25.857 + 16.036 registros) y armonizarlos. Un día de trabajo.
2. **Calcular la latencia evento → activación** para 2023–2024 y mapearla por municipio. Es el primer indicador de desempeño logístico publicado en Colombia.
3. **Cuantificar el vacío de registro** por departamento y por tipo de evento.
4. **Ajustar y radicar la petición a la UNGRD** con los numerales corregidos.

Los pasos 1 a 3 no dependen de nadie y producen material publicable antes de que venzan los términos de las peticiones.

---

## Fuentes consultadas

- [Emergencias UNGRD (2019–2022) — datos.gov.co, `wwkg-r6te`](https://www.datos.gov.co/Ambiente-y-Desarrollo-Sostenible/Emergencias-UNGRD-/wwkg-r6te)
- API: `https://www.datos.gov.co/resource/wwkg-r6te.json`
- Emergencias UNGRD 2023–2024 — datos.gov.co, `rgre-6ak4` · API: `https://www.datos.gov.co/resource/rgre-6ak4.json`
- [SNIGRD legado — UNGRD](https://www.gestiondelriesgo.gov.co/snigrd/)
- [Consolidado Anual de Emergencias 1998–2017](https://www.gestiondelriesgo.gov.co/snigrd/pagina.aspx?id=376)
- [SNIGRD nuevo](https://sni.gestiondelriesgo.gov.co/)
- [Registro Único de Damnificados](http://rud.gestiondelriesgo.gov.co/)
