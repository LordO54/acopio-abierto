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
