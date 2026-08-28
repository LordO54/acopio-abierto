# log.md — rama `main`

Traza de ejecución Observación–Pensamiento–Acción.

---

## OTA-001 · 2026-08-27

**Observación.** No existe repositorio. La descripción del video 2 para LinkedIn requiere un enlace público al protocolo de validación; sin él el post pierde la verificabilidad que es su principal argumento de credibilidad.

**Pensamiento.** El repositorio es dependencia dura de la publicación, no un entregable paralelo. Debe inicializarse antes de publicar el segundo video. El primero no depende de enlace y puede salir ya.

**Acción.** Inicializar estructura GCC, `feature_list.json`, `ROADMAP.md` y `docs/validacion-fase-0.md` como destino del enlace.

---

## OTA-002 · 2026-08-27

**Observación.** Los documentos de investigación producidos llevan fecha 16–17 de agosto. La fecha real es 27 de agosto. El error provino de leer el timestamp de última actualización del portal Gravitas ("lunes, 17 de agosto") como fecha del sistema.

**Pensamiento.** Un proyecto cuyo argumento central es la calidad del dato no puede tener metadatos incorrectos. El error es menor en consecuencia y grave en señal.

**Acción.** Corregir el encabezado de los siete documentos al incorporarlos a `docs/investigacion/`. Registrar la corrección en `commit.md` en lugar de borrarla.

---

## OTA-003 · 2026-08-27

**Observación.** F0 estaba planeada del 15 al 21 de agosto. Se ejecutó parcialmente y con retraso por disponibilidad del operador.

**Pensamiento.** El retraso cambia el encuadre de forma favorable, no desfavorable. Publicar en día 17 del sismo con tono de urgencia envejece mal y raya en aprovechamiento de la coyuntura. El encuadre preventivo —"esto se aprende ahora para tenerlo listo antes de la próxima"— es más honesto y elimina la competencia contra la ventana de emergencia.

**Acción.** Recalcular todas las ventanas de F0–F2 desde el 27 de agosto. Ajustar el tono de los textos de publicación al encuadre preventivo.

---

## OTA-004 · 2026-08-27

**Observación.** El operador reporta que el kit de contacto y la hoja de triage están hechos. Ninguno de los dos artefactos está en el repositorio ni fue verificado.

**Pensamiento.** El protocolo prohíbe declarar completa una feature sin verificación. Un `passes: true` sin artefacto verificable reproduce exactamente la patología que el proyecto denuncia: el campo lleno sin dato detrás.

**Acción.** F0.1 y F0.2 quedan en `false` con nota. Se marcan `true` cuando los archivos estén en `instrumentos/` y hayan sido revisados.

---

## OTA-005 · 2026-08-27

**Observación.** El video 2 ofrece análisis gratuito de inventarios reales a organizaciones. El motor de optimización todavía no existe como servicio: hay un script reproducible sobre inventario de ejemplo.

**Pensamiento.** Prometer capacidad inexistente es el riesgo reputacional más alto del lanzamiento. Si responden cinco organizaciones simultáneamente no se puede cumplir.

**Acción.** Moderar la oferta a "estamos empezando y podemos tomar los primeros casos". Crear F1.5 para la capacidad real de atender inventarios externos.

---

## OTA-006 · 2026-08-27

**Observación.** Los documentos de `docs/investigacion/` y las especificaciones de `docs/` conservaban marcas de su origen conversacional: segunda persona dirigida al autor ("tu proyecto", "lo que imaginas"), autocorrecciones narradas ("afirmé que…", bloque `⚠️ CORRECCIÓN`) y coletillas que interpretaban cada hallazgo en clave de justificación del proyecto ("Esa ausencia de tubería es el proyecto").

**Pensamiento.** Estos documentos son la evidencia pública del repositorio y deben sostenerse ante un lector externo —una entidad que responda una petición, un evaluador, un periodista— que no conoce el plan interno. Las autocorrecciones narradas restan autoridad sin aportar el hallazgo; el hallazgo metodológico (dos grafías del centinela `fecha_activacion`) se conserva, la narración del error se elimina. El encuadre de producto vive en `README.md` y `docs/validacion-fase-0.md`, no en cada descripción.

**Acción.** Reescritura de los seis documentos de investigación y de `metricas-de-rendimiento.md` y `modelo-ensamblaje-alimentario.md` a registro impersonal. Corregida la referencia rota a `06-indicador-latencia-y-calidad-datos.md` → `04-indicador-latencia.md` y eliminado el paso obsoleto "auditar el SNIGRD cuando haya navegador", ya ejecutado en la sección 1b. Las peticiones, `README.md` y `ROADMAP.md` se dejan intactas: su primera persona es la del peticionario y la del equipo, no un residuo.

---

## OTA-007 · 2026-08-27

**Observación.** Nuevo documento de alcance nutricional en `docs/`, guardado con nombre corto 8.3 (`NUTRIE~1.MD`) y con las mismas marcas conversacionales que se limpiaron en OTA-006: primera persona plural del equipo y remates que justifican el proyecto dentro de las descripciones.

**Pensamiento.** El documento declara un límite clínico del modelo —una canasta de secos puede marcar 100% de macronutrientes y producir escorbuto a las seis semanas—. Ese contenido debe leerse como advertencia técnica verificable, no como argumento a favor del proyecto, porque su valor está justamente en que acota lo que el modelo promete. El nombre 8.3 además rompe la convención de `docs/`.

**Acción.** Renombrado a `docs/nutrientes-esfera.md` y filtrado al mismo registro impersonal. Verificado que las cuatro tareas que deriva (F1.1b, F1.8, F1.9, F0.13) ya existen en `feature_list.json`. Queda sin incorporar `instrumentos/HOJA-T~2.PDF`, también con nombre 8.3.

---

## OTA-008 · 2026-08-27

**Observación.** La hoja de triage llegó al repositorio con nombre 8.3 (`HOJA-T~2.PDF`). Su contenido —extraído del stream del PDF— es una hoja de clasificación de donaciones para recepción, no el guion de entrevista que describe F0.2. Git además la clasificaba como texto (1.029 líneas en `numstat`) porque su stream de contenido está sin comprimir y no contiene bytes NUL en los primeros 8 KB.

**Pensamiento.** Con `core.autocrlf=true` y el archivo tratado como texto, cualquier checkout habría reescrito los saltos de línea dentro del PDF y lo habría corrompido de forma silenciosa. El artefacto tampoco satisface F0.2: marcar esa feature como completada por su llegada reproduciría exactamente la patología documentada en las auditorías, un `passes` sin el artefacto que dice representar.

**Acción.** Renombrado a `instrumentos/hoja-triage-donaciones.pdf`. Creado `.gitattributes` con `*.pdf binary` y verificado que `numstat` ahora reporta binario. F0.2 permanece en `false`, con la distinción anotada en `instrumentos/README.md`. Incorporados los cambios de `feature_list.json`: reformato a objetos multilínea y cuatro features nuevas —F0.13, F1.1b, F1.8, F1.9— derivadas del documento de nutrientes; sin entradas eliminadas ni booleanos alterados.

---

## OTA-009 · 2026-08-27

**Observación.** Tres instrumentos nuevos en `instrumentos/`, otra vez con nombres 8.3. Sus referencias cruzadas declaraban los nombres correctos —`formatos-mensajes.md` enlaza a `kit-contacto.md` y viceversa—, así que el renombrado no era una elección sino una restitución. El contenido arrastraba tres capas de deriva: la relación personal con quien da el respaldo institucional escrita en el texto ("tu amiga", "ella"), el calendario de la ventana F0 original de agosto 15–21 que el ROADMAP ya declaró desplazada, y referencias a features cuyos identificadores hoy significan otra cosa (F0.4 como hoja de triage, F0.9 como autorización, un Gate G1 inexistente).

**Pensamiento.** Un kit de contacto se ejecuta bajo presión y por quien esté disponible, no necesariamente por quien lo escribió: cada dato que solo es cierto para una persona es una instrucción que el siguiente lector no puede seguir. Los identificadores de feature equivocados son peores que ausentes, porque enlazan a una entrada real con otro significado. El calendario absoluto caducó; la secuencia relativa T+0..T+3 sobrevive a cualquier reprogramación.

**Acción.** Renombrados a `kit-contacto.md`, `formatos-mensajes.md` y `entrevista-plantilla.md`. Generalizado el protocolo de respaldo a "quien da el respaldo" sin perder su contenido de protección. Calendario absoluto sustituido por la secuencia relativa. Identificadores corregidos: O4 apunta a F0.9 y desbloquea F1.3 y F1.4; eliminadas las citas a F0.4, F0.5 y G1. Añadida la pregunta de oro al cierre de la plantilla de entrevista, exigida por el criterio de aceptación de F0.2 y por `docs/validacion-fase-0.md`, y ausente del formulario. F0.1 y F0.2 siguen en `false`: los artefactos ya están en el repositorio, pero la revisión que exige su criterio es del operador. Documentadas en el README las dos rutas que los instrumentos dan por existentes y no existen.
