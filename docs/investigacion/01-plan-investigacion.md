# Plan de investigación — Logística de donaciones en emergencias (Colombia)

**Fecha:** 27 de agosto de 2026
**Propósito:** dar alcance al proyecto antes de ejecutar Fase 0

---

## 0. Contexto que cambia el marco del proyecto

El 10 de agosto de 2026 un sismo de magnitud 7,4 con epicentro en San José del Palmar (Chocó) afectó **15 departamentos y 437 municipios**. Reportes de la UNGRD hasta el 14 de agosto: ~287 fallecidos, ~3.975 heridos, ~378 desaparecidos, 10.677 viviendas destruidas y 65.841 averiadas. Hay centros de acopio activos en todas las capitales y el Banco Mundial desembolsó USD 200 millones.

Este no es un ejercicio académico. **La "segunda ola" está ocurriendo ahora mismo**, y eso implica tres cosas para la investigación:

1. Los datos de esta emergencia se están generando en este momento y son irrecuperables después. Registrar lo que está pasando en los acopios hoy vale más que reconstruir Mocoa 2017.
2. Los actores a entrevistar están saturados. Fase 0 debe ser extremadamente breve o esperar 3–4 semanas.
3. Existe una ventana política y de financiación abierta que no estará abierta en seis meses.

---

## 1. Mapa institucional: quién responde en Colombia

Marco: **Ley 1523 de 2012**, que crea el Sistema Nacional de Gestión del Riesgo de Desastres (SNGRD) y reemplaza al antiguo SNPAD.

### Nivel de dirección

| Instancia | Rol |
|---|---|
| **Presidencia** | Dirige el sistema; declara situación de desastre / calamidad pública |
| **CNGRD** (Consejo Nacional) | Ministros + director DNP + director UNGRD. Instancia superior de decisión |
| **UNGRD** | Unidad Nacional para la Gestión del Riesgo de Desastres. Coordinador operativo nacional. Adscrita a Presidencia |
| **DNP** | Planeación, evaluación de política (vía Sinergia), índices de riesgo municipal |
| **MinHacienda / FNGRD** | Fondo Nacional de Gestión del Riesgo de Desastres — el vehículo financiero |

### Nivel territorial (donde realmente se ejecuta el acopio)

- **CDGRD** — Consejos Departamentales de Gestión del Riesgo, presididos por el gobernador
- **CMGRD** — Consejos Municipales, presididos por el alcalde
- Son la unidad de decisión real sobre distribución local. **Aquí está el interlocutor de Fase 0**, no en la UNGRD.

### Operadores en terreno

Cruz Roja Colombiana · Defensa Civil Colombiana · Cuerpos de Bomberos · Fuerzas Militares y Policía · Alcaldías · ONG internacionales coordinadas por OCHA · iglesias y juntas de acción comunal (el actor invisible que más mueve volumen).

### Cooperación internacional

**OCHA Colombia** (coordinación, sistema 4W) · **OPS/OMS** (LSS/SUMA, EDAN en salud) · ACNUR · PMA · Banco Mundial/GFDRR · BID.

---

## 2. Sistemas y software que ya existen

Este es el punto de partida obligado antes de construir nada: **buena parte de lo que se imaginaría como solución ya fue diseñado. El problema no es que no exista software, es que no se usa, no se alimenta o no es público.**

| Sistema | Qué hace | Estado / limitación |
|---|---|---|
| **LSS/SUMA** (OPS/OMS) | Registro, clasificación, priorización e inventario de suministros humanitarios desde la oferta del donante hasta la distribución. Colombia lo adoptó formalmente por decreto ministerial | Diseñado en los 90. Centrado en **inventario**, no en **necesidad**. Requiere equipos entrenados desplegados. Su uso real en emergencias recientes es una pregunta abierta pendiente de verificar |
| **EDAN** | Evaluación de Daños y Análisis de Necesidades. Metodología oficial + formatos. Aplicativo web en `rud.gestiondelriesgo.gov.co` | Levantamiento lento, primero en papel. Resultados **no públicos**. Granularidad municipal, no comunitaria |
| **RUD** | Registro Único de Damnificados. Creado por Decreto 4830 de 2010; DANE diseñó y procesó | Solo se activó a gran escala en la Ola Invernal 2010–11 (proyecto "REUNIDOS"). Identifica personas, no necesidades por bien |
| **SNIGRD** | Nueva plataforma de la UNGRD lanzada en mayo de 2026: riesgos, emergencias históricas, inversión pública, maquinaria y capacidades, en tiempo real. `sni.gestiondelriesgo.gov.co` | **Recién lanzada — requiere auditoría directa.** Es la fuente más prometedora y la menos explorada |
| **DesInventar** | Base histórica de pérdidas y daños desde 1921 (~6.000 registros). LA RED + OSSO + UNISDR | Registra **efectos**, no respuesta. No dice qué se entregó ni si sirvió |
| **Datos Abiertos** | Dataset "Emergencias UNGRD" en `datos.gov.co` | Eventos y afectación. Sin datos de ayuda entregada |
| **4W de OCHA** | Quién hace qué, dónde y cuándo. Parte del SIDI. Publicado en HDX y Monitor OCHA | Rastrea **proyectos de organizaciones**, no necesidades de hogares. Cobertura sesgada al conflicto armado |

### Herramientas internacionales comparables (para benchmark)
KoBoToolbox · ActivityInfo · Sahana Eden · RAMP (IFRC) · CommCare · Last Mile Mobile Solutions (World Vision).

---

## 3. ¿Existen datos históricos de eficacia? Respuesta corta: casi no

### Lo que sí existe

- **Evaluación institucional y de resultados del SNGRD** — DNP/Sinergia, junio 2019. Evalúa diseño, coordinación horizontal y vertical, recursos y capacidad institucional a partir de la Ley 1523. Es el documento más cercano a una evaluación de desempeño sistémico.
- **Auditorías de la Contraloría** sobre la UNGRD. Hallazgos recurrentes: desorden en el manejo físico y documental de bienes de asistencia humanitaria, **vacíos críticos en la cadena de custodia**, sobrecostos y faltantes en kits, baja ejecución presupuestal.
- **Valoración de daños y pérdidas de la Ola Invernal 2010–2011** (CEPAL/BID/DNP) y el sistema de consulta REUNIDOS del DANE.
- **CONPES** 3318 (2004), 4058, 4135 — política y financiamiento.
- Informes de OPS y Cruz Roja sobre Mocoa 2017 (lecciones aprendidas del sector salud).
- Literatura académica sobre **"material convergence"** (Holguín-Veras et al.) — la saturación de los canales logísticos con bienes no solicitados tras un desastre, con modelos de asignación de recursos y evidencia de que la mensajería a donantes reduce el flujo de bienes de baja prioridad.

### Lo que NO existe (la brecha)

Ninguna fuente pública colombiana permite responder:

- ¿Cuánto tiempo pasó entre que una comunidad reportó una necesidad y recibió el bien? (*tiempo de ciclo*)
- ¿Qué porcentaje de lo solicitado se entregó efectivamente? (*fill rate*)
- ¿Qué porcentaje de lo donado terminó descartado por inservible, vencido o no prioritario? (*tasa de desperdicio*)
- ¿Qué comunidades quedaron sin cobertura y cuáles recibieron entregas duplicadas?
- ¿Qué necesitan específicamente hoy las comunidades afectadas?

**La Contraloría mide legalidad fiscal, no eficacia logística.** Nadie en Colombia publica métricas de desempeño de la cadena de suministro humanitaria.

---

## 4. Plan de investigación

### Línea 1 — Normativa e institucional (desk, 1 semana)

**Preguntas:** ¿Qué obliga la ley a registrar sobre donaciones? ¿Quién es legalmente responsable del inventario en un acopio? ¿Qué protocolo aplica el CMGRD?

**Fuentes:** Ley 1523/2012 · Decreto 2157/2017 · Estrategia Nacional de Respuesta a Emergencias · protocolos de coordinación público-privada (ANDI) · guías metodológicas de la UNGRD (repositorio y catálogo CEDIR).

**Entregable:** mapa de actores con responsabilidad formal sobre el dato.

---

### Línea 2 — Auditoría técnica de sistemas existentes (2 semanas)

**Preguntas:** ¿Qué expone realmente el SNIGRD? ¿Tiene API? ¿SUMA está desplegado hoy en el sismo del Chocó? ¿El aplicativo EDAN sigue operando?

**Acciones:**
1. Recorrer `sni.gestiondelriesgo.gov.co` y documentar cada módulo, granularidad y actualización.
2. Descargar el dataset "Emergencias UNGRD" de `datos.gov.co` y evaluar campos y frescura.
3. Revisar HDX y Monitor OCHA Colombia para el sismo de agosto 2026.
4. Probar acceso a `rud.gestiondelriesgo.gov.co`.

**Entregable:** matriz de sistemas — qué dato produce cada uno, a qué granularidad, si es público, si es consumible por máquina.

---

### Línea 3 — Evidencia histórica por casos (2–3 semanas)

Cinco casos, mismo protocolo de análisis:

| Caso | Año | Por qué |
|---|---|---|
| Ola Invernal | 2010–11 | Mayor esfuerzo de registro (RUD/REUNIDOS) y de fiscalización (Colombia Humanitaria) |
| Salgar | 2015 | Avenida torrencial, escala municipal |
| Mocoa | 2017 | Caso más documentado; colapso de acopio bien reportado |
| Iota / Providencia | 2020 | Insularidad — restricción logística extrema |
| Sismo Chocó | 2026 | **En curso. Registro en tiempo real** |

**Por caso, reconstruir:** qué se donó, quién coordinó, qué se registró, qué se descartó, qué reportó la prensa vs. qué reportó el Estado.

---

### Línea 4 — Solicitud formal de datos (arranca de inmediato, corre en paralelo)

Es la palanca de mayor retorno de todo el plan.

**El derecho de petición** (art. 23 Constitución, Ley 1755/2015) obliga a toda entidad pública a responder en **15 días hábiles**. Es gratuito, no requiere abogado y se radica por correo electrónico.

Radicar a:

- **UNGRD** — inventarios de ayuda humanitaria entregada por municipio, por emergencia; manual de operación de centros de acopio; estado de uso de LSS/SUMA
- **DANE** — microdatos y metodología del RUD
- **Contraloría** — informes de auditoría completos sobre gestión de bienes de asistencia humanitaria
- **DNP/Sinergia** — anexos de la evaluación de 2019
- **Cruz Roja Colombiana** (no obligada, pero suele responder) — protocolos y formatos de registro en acopio

**Entregable:** repositorio de respuestas oficiales. Aunque respondan "no tenemos esa información", **esa negativa documentada es evidencia de la brecha** y es citable.

---

### Línea 5 — Campo (Fase 0, reprogramada)

Se mantiene el diseño previsto —WhatsApp para contacto, correo para agendar, artefactos durante la entrevista, hojas como reciprocidad anunciada por adelantado, crítica en un cuarto contacto— con dos ajustes por el contexto:

- **Bajar el objetivo de la primera ronda a 5–8 entrevistas.** La gente está en emergencia.
- **Agregar una pregunta clave:** *"¿qué información necesitabas hoy y no tenías?"* Contestada durante una emergencia real, esa respuesta vale más que todo el desk research.

---

## 5. Alcance propuesto

### El proyecto NO debería ser

Un reemplazo de SUMA ni un sistema nacional de gestión de inventarios. Ese espacio está ocupado por instituciones con mandato legal y no hay puerta de entrada para un actor externo.

### El proyecto SÍ debería ser

**Visibilidad del lado de la demanda.** El vacío confirmado no es "no sabemos qué hay en las bodegas" — es **"no sabemos qué necesita cada comunidad ni quién ya fue atendido"**. Todos los sistemas existentes son centrados en oferta e inventario. Ninguno es centrado en necesidad y por comunidad.

Concretamente, tres capas en orden de dificultad:

1. **Capa de registro estandarizado** — las hojas de registro en diseño. Bajo costo, valor inmediato; es la puerta de entrada a los acopios.
2. **Capa de agregación** — consolidar registros de múltiples acopios en una vista comparable. Aquí aparece el dato que hoy no existe.
3. **Capa de necesidad comunitaria** — reporte desde la comunidad, no desde el acopio. Es lo más valioso y lo más difícil; requiere confianza construida en las capas 1 y 2.

**Esta fase empieza y termina en la capa 1.** La capa 3 es la tesis; la capa 1 es lo que da acceso y datos para defenderla.

---

## 6. Criterio de éxito de la investigación

La investigación está completa cuando sea posible responder, con fuente citable:

1. Qué entidad tiene el mandato legal de registrar donaciones, y con qué instrumento.
2. Si ese instrumento se usó en las últimas cinco emergencias, sí o no.
3. Qué métricas de desempeño logístico existen públicamente en Colombia (probable respuesta: ninguna) y con qué documento se prueba.
4. Qué información dicen necesitar los coordinadores de acopio y no tienen.

Con esas cuatro respuestas hay marco, justificación, brecha y validación de usuario. Es suficiente para definir producto.

---

## Fuentes

- [Ley 1523 de 2012 — Función Pública](https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=47141)
- [Estructura del SNGRD — UNGRD](https://portal.gestiondelriesgo.gov.co/paginas/estructura.aspx)
- [SNIGRD — UNGRD](https://sni.gestiondelriesgo.gov.co/)
- [Colombia fortalece la gestión del riesgo con un sistema nacional en tiempo real — MinTIC](https://mintic.gov.co/portal/inicio/Sala-de-prensa/Noticias/438084:Colombia-fortalece-la-gestion-del-riesgo-con-un-sistema-nacional-que-integrara-datos-y-decisiones-en-tiempo-real)
- [SUMA/LSS — Sistema de manejo de suministros humanitarios, OPS/OMS](https://www.paho.org/disasters/index.php?option=com_content&view=article&id=697:suma-lss-humanitarian-supply-management-system&Itemid=924&lang=es)
- [SUMA: el sistema de manejo de suministros humanitarios (PDF) — IRIS PAHO](https://iris.paho.org/bitstream/handle/10665.2/45934/suma.pdf?sequence=1&isAllowed=y)
- [Guía metodológica EDAN (documento preliminar) — MinAmbiente](https://www.minambiente.gov.co/wp-content/uploads/2021/12/Documento-preliminar-EDANA-C-V3-Diciembre-29.pdf)
- [Registro Único de Damnificados / REUNIDOS 2010–2011 — DANE](https://www.dane.gov.co/index.php/estadisticas-por-tema/ambientales/reunidos)
- [Valoración de daños y pérdidas, Ola Invernal 2010–2011 (PDF)](https://archivo.minambiente.gov.co/images/cambioclimatico/pdf/Plan_nacional_de_adaptacion/3._Da%C3%B1os_y_p%C3%A9rdidas_ola_invernal.pdf)
- [Evaluación institucional y de resultados de la Política Nacional de GRD (2019) — DNP Sinergia](https://colaboracion.dnp.gov.co/CDT/Sinergia/Documentos/2019_06_12_Evaluacion_SN_Gestion_Riesgo_Desastres_Estudio_Informe.pdf)
- [Catálogo de la evaluación — ANDA DNP](https://anda.dnp.gov.co/index.php/catalog/113)
- [DesInventar — sitio oficial](https://www.desinventar.org/)
- [Emergencias UNGRD — Datos Abiertos Colombia](https://www.datos.gov.co/Ambiente-y-Desarrollo-Sostenible/Emergencias-UNGRD-/wwkg-r6te)
- [Sistema de Información 4W — OCHA Colombia Wiki](https://wikicolombia.unocha.org/index.php?title=Sistema_de_Informaci%C3%B3n_4W)
- [Monitor Humanitario OCHA Colombia](https://monitor.unocha.org/colombia)
- [OCHA Colombia — Humanitarian Data Exchange](https://data.humdata.org/organization/ocha-colombia)
- [Protocolo de coordinación en la respuesta a emergencias y desastres — ANDI (PDF)](https://www.andi.com.co/Uploads/PROTOCOLO%20DE%20LECTURA.pdf)
- [Contraloría: fallo de responsabilidad fiscal por ayudas — El Tiempo](https://www.eltiempo.com/justicia/investigacion/contraloria-fallo-responsabilidad-fiscal-por-2-517-millones-a-exfuncionarios-de-la-ungrd-por-ayudas-de-pandemia-3462338)
- [Avalancha en Mocoa, un desafío para la respuesta en salud — OPS](https://www3.paho.org/disasters/newsletter/580-colombia-avalanche-in-mocoa-a-challenge-for-the-health-response-277-379-en.html)
- [Terremoto de Colombia de 2026 — Wikipedia](https://es.wikipedia.org/wiki/Terremoto_de_Colombia_de_2026)
- [Balance del terremoto — El Colombiano](https://www.elcolombiano.com/colombia/muertos-terremoto-en-colombia-heridos-replicas-choco-hoy-GC39809690)
- [Centros de acopio tras el terremoto — Radio Nacional](https://www.radionacional.co/actualidad/estos-son-los-puntos-de-acopio-y-recepcion-de-ayudas-en-ciudades-de-colombia)
- [Material Convergence: An Important and Understudied Disaster Phenomenon](https://www.semanticscholar.org/paper/Material-Convergence:-Important-and-Understudied-Holgu%C3%ADn-Veras-Jaller/1570bca314d5082754cd164d8ae70e10809739f8)
- [Resource allocation models for material convergence — ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0925527320300463)
- [Reducing material convergence in disaster environments — ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1366554522001272)
