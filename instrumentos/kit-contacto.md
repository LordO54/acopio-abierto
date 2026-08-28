# Fase 0 — Kit de contacto
### Secuencia multicanal, plantillas y guion de entrevista

**Perfil del contacto:** conocido profesional · **Canales:** WhatsApp + correo · **Alcance:** contacto principal + 3-5 organizaciones en paralelo.

---

## 0. Campos a reemplazar

Todas las plantillas usan estos campos. Se completan una vez aquí y se reemplazan en bloque; así ningún mensaje sale con un `[corchete]` sin llenar, que es el error que más rápido destruye la credibilidad de un correo.

| Campo | Valor | Aparece en |
|---|---|---|
| `[TU_NOMBRE]` | | Todas |
| `[TU_ROL]` | ej. responsable técnico del proyecto | B, D, D2, formatos públicos |
| `[TU_CORREO]` | | B, D, D2, P2, P3, P5 |
| `[TU_TELEFONO]` | | B, D2, P5 |
| `[TU_CIUDAD]` | | D, D2, P3 |
| `[REPO_URL]` | repositorio o enlace a la hoja | B, D2, P3, P5 |
| **`[ASOCIACION]`** | **nombre exacto y completo de la organización que respalda** | D2, P1, P2, P3, P4, P5 |
| `[ASOCIACION_CIUDAD]` | sede de la organización | D2 |
| `[REPRESENTANTE]` | nombre de quien la representa | D2, P5 |
| `[REPRESENTANTE_CARGO]` | cargo exacto, tal como esa persona lo autorice | D2, P5 |
| `[REPRESENTANTE_CORREO]` | correo institucional, si lo hay | D2 |
| `[FORMULA_RESPALDO]` | la frase textual autorizada por escrito | D2, P1, P2, P3, P4, P5 |
| `[NOMBRE]` / `[ORGANIZACION]` | destinatario, varía por mensaje | A, B, C, E |

**Regla sobre `[ASOCIACION]` y `[FORMULA_RESPALDO]`:** el nombre va **completo y exacto**, sin abreviar ni inventar sigla. Y `[FORMULA_RESPALDO]` se copia **literal** de lo autorizado por escrito — no se parafrasea ni se "mejora". Si la autorización dice *"acompaña a título personal"*, eso es lo que se escribe, aunque suene menos impresionante.

Verificación antes de enviar cualquier mensaje: buscar `[` en el texto. Si aparece algo, no se envía.

---

## 1. Principio de diseño: la hoja va primero

La hoja de triage **no es recompensa por responder**. Se entrega sin condición.

| Modelo | Pedido implícito | Costo para el coordinador | Tasa de respuesta esperada |
|---|---|---|---|
| Recompensa posterior | "Responde 12 preguntas y te doy algo" | Alto (trabajo) | Baja |
| **Entrega incondicional** | "Toma esto. Si te sirve, critícalo" | Bajo (opinar) | Alta |

Corregir a alguien es más fácil y más satisfactorio que llenar una encuesta. Además, una crítica específica sobre un artefacto concreto vale más como dato que una descripción general de su operación.

**Consecuencia de secuencia:** la hoja de triage pasa a ser **prerrequisito** del correo, no su epílogo.

---

## 2. Secuencia

Días relativos al primer contacto, no fechas fijas: la secuencia se reinicia con cada organización.

| Momento | Canal | Acción | Objetivo |
|---|---|---|---|
| T+0 | WhatsApp | Mensaje A — apertura | Agendar llamada + pedir foto de la planilla |
| T+1 | — | Tener lista la hoja de triage | Que el correo llegue con el artefacto |
| T+1 | WhatsApp | Solicitud de autorización de respaldo | Habilitar el respaldo organizacional por escrito |
| T+2 | Correo | Mensaje B — formal, con hoja adjunta | Acreditarse + entregar valor + confirmar cita |
| T+2 | Correo | Mensaje D2 (con respaldo) o D (sin él) — 3-5 organizaciones | Eliminar el punto único de falla |
| T+3 | Llamada | Guion de entrevista (§4) | Datos reales |
| +24 h post-llamada | Correo | Mensaje E — gracias + crítica | Cerrar el ciclo con la petición de crítica |
| 48 h de silencio | WhatsApp | Mensaje C | Un solo reintento, sin insistir |

**Regla de reintento:** un recordatorio, nunca dos. Un tercer mensaje a alguien que gestiona una emergencia quema el contacto de forma permanente.

---

## 3. Plantillas

> **Para copiar y pegar sin leer el resto:** [formatos-mensajes.md](formatos-mensajes.md)
> contiene únicamente los textos, con la tabla de campos y las reglas mínimas.
> Este documento explica el porqué de cada uno.

Reemplazar `[...]`. No alargar los textos: cada línea añadida baja la probabilidad de respuesta.

### Mensaje A · WhatsApp — apertura (T+0)

> Hola [Nombre], ¿cómo vas? Sé que están a mil con lo del terremoto, así que voy directo.
>
> Estoy armando una guía de clasificación de donaciones para centros de acopio, apoyada en el estándar Esfera y en la taxonomía SUMA de la OPS. La idea es que un voluntario sin experiencia pueda decidir en segundos qué sirve y qué no, y que el acopio pueda pedirle a la gente exactamente lo que le falta en vez de recibir a ciegas.
>
> Antes de escribir una línea más quiero entender cómo lo están haciendo ustedes de verdad, no cómo debería ser en el papel.
>
> Dos cosas, y ninguna te obliga a nada:
>
> 1. ¿Tienes 15 minutos esta semana para una llamada? El día y la hora los pones tú, me acomodo a lo que sea.
> 2. Si es más rápido: una foto de la planilla o el cuaderno con el que llevan el registro hoy. Con eso solo aprendo más que con media hora de preguntas.
>
> Mañana te mando por correo la primera hoja de triage que armé: una página, para imprimir y pegar en recepción. Es tuya la uses o no. Y si me la destrozas a críticas, mejor todavía — para eso te la mando.
>
> Gracias, [Tu nombre]

**Por qué funciona:** el pedido de la foto es de menor esfuerzo que el de la llamada (regla de la escalera descendente); "el día y la hora los pones tú" elimina la negociación; la hoja se promete sin condición, lo que desactiva la lectura transaccional del mensaje.

**Lo que deliberadamente NO lleva:** las 12 preguntas, un enlace a un formulario, un PDF adjunto sin contexto, y la palabra "encuesta".

---

### Mensaje B · Correo — formalización con la hoja adjunta (T+2)

**Asunto:** `Hoja de clasificación de donaciones para [Organización] — 1 página, imprimible`

El asunto anuncia el regalo, no el pedido. Si dice "solicitud de entrevista" o "propuesta de colaboración", se archiva sin abrir.

> Buenos días [Nombre],
>
> Como te comenté por WhatsApp, te adjunto la hoja de triage de donaciones v0. Es una página, en blanco y negro, pensada para imprimirse y pegarse en el punto de recepción. Está construida sobre el estándar Esfera y sobre la taxonomía de clasificación SUMA de la OPS, y complementada con la guía de "qué donar y no donar" de la Alcaldía de Bogotá. Cada regla tiene su fuente citada.
>
> Es de uso libre. No necesito nada a cambio para que la usen.
>
> **Sobre qué estoy haciendo.** Trabajo en un modelo que, a partir del inventario real de un acopio, calcula cuántos días-persona de alimentación completa se pueden armar y cuál es el nutriente que está limitando el total. La salida práctica es un mensaje del tipo *"con lo que hay se cubren N días-persona; no pidan más arroz, pidan aceite y atún"*. Hoy los acopios miden toneladas recibidas, que no dice nada sobre cuánta gente se puede alimentar realmente.
>
> **Lo que te pido.** Quince minutos de llamada, cuando puedas. Quiero entender cómo reciben, clasifican y despachan hoy, y sobre todo dónde se les traba el proceso. No voy a proponerte nada durante esa llamada: solo escuchar.
>
> **Y algo que vale más que la llamada:** si me puedes compartir el inventario o el registro que llevan hoy —en el formato que sea, foto de cuaderno, Excel, exportación, lo que tengan— puedo correr el modelo sobre sus datos reales y devolverles el análisis en un par de días, sin costo. Eso les serviría a ustedes directamente y a mí me diría si el modelo sirve o si está equivocado.
>
> **Sobre el manejo de la información:**
>
> - No represento a ninguna organización, no pido ni recibo dinero, y esto no tiene fin comercial.
> - No publico datos suyos sin autorización escrita.
> - Si el material se usa como caso, va anonimizado salvo que ustedes prefieran ser nombrados.
> - Si en algún momento quieren que borre lo compartido, lo borro y les confirmo.
>
> Si prefieres responder por escrito en vez de hablar, te mando las preguntas y las contestas cuando tengas un hueco.
>
> Gracias por el tiempo, y de verdad: úsenla o critíquenla, cualquiera de las dos me sirve.
>
> [Tu nombre]
> [Teléfono] · [Correo] · [Repositorio, si ya existe]

---

### Mensaje C · WhatsApp — recordatorio único (48 h de silencio)

> Hola [Nombre], solo por si se perdió entre todo: te dejé la hoja de triage en el correo, es de uso libre sin ningún compromiso. Si en algún momento de la semana te sobran 15 minutos, me encantaría escucharte; si no, sin problema, sé cómo están. Un abrazo.

Sin culpa, sin urgencia, con salida honrosa. Si no responde a esto, se cierra el canal y se documenta.

---

### Mensaje D · Correo frío — 3-5 organizaciones adicionales

**Asunto:** `Hoja de clasificación de donaciones, 1 página — uso libre para su centro de acopio`

> Buenos días,
>
> Les escribo desde [ciudad]. Adjunto una hoja de una página para clasificar donaciones en punto de recepción: pensada para que un voluntario sin experiencia decida en segundos qué sirve, qué no, y a qué pila va cada cosa. Está basada en el estándar Esfera y en la taxonomía SUMA de la OPS, con las fuentes citadas.
>
> Es de uso libre, sin ninguna contraprestación. Si les sirve, imprímanla; si no, ignórenla sin problema.
>
> Si alguien de su equipo tuviera 15 minutos esta semana, me ayudaría muchísimo entender cómo reciben y clasifican hoy y dónde se les acumula el trabajo. Estoy construyendo un modelo que calcula, a partir del inventario real, cuánta gente se puede alimentar completamente con lo que hay y qué es lo que hace falta pedir. Si me comparten su inventario en cualquier formato, les devuelvo ese análisis sin costo.
>
> No represento a ninguna organización ni pido donaciones. No publico información de nadie sin autorización.
>
> Gracias por lo que están haciendo,
> [Tu nombre] · [Contacto]

**A quién enviarlo:** canales oficiales publicados de los acopios activos (alcaldías de Bogotá, Cali, Pereira, Manizales, Quibdó), Cruz Roja seccional, bancos de alimentos regionales, y coordinaciones universitarias de voluntariado. Prioriza a quien publicó un número de contacto: significa que alguien lo está mirando.

---

### Mensaje D2 · Correo frío con respaldo organizacional

**Usar solo con la autorización escrita ya archivada.** Ver §3.1 antes de enviar.

**Asunto:** `[ASOCIACION] — hoja de clasificación de donaciones para su centro de acopio (1 página)`

> Buenos días,
>
> Les escribimos desde **[ASOCIACION]**, con sede en [ASOCIACION_CIUDAD]. Adjuntamos una hoja de una página para clasificar donaciones en el punto de recepción: está pensada para que un voluntario sin experiencia previa decida en segundos qué sirve, qué no, y a qué pila va cada artículo. Está construida sobre el estándar Esfera y sobre la taxonomía de clasificación SUMA de la OPS, con cada regla citada a su fuente.
>
> Es de uso libre y sin ninguna contraprestación. Si les sirve, imprímanla; si no, descártenla sin problema.
>
> **Qué estamos construyendo.** Un modelo que, a partir del inventario real de un centro de acopio, calcula cuántos días-persona de alimentación completa pueden armarse con lo que hay y cuál es el nutriente que limita ese total. La salida práctica es un mensaje accionable del tipo *"con el inventario actual se cubren N días-persona; el limitante son las grasas, conviene pedir aceite y no más cereal"*. Hoy la mayoría de acopios mide toneladas recibidas, que es una cifra que no dice nada sobre cuántas personas pueden alimentarse de verdad.
>
> **Nuestra propuesta concreta.** Si nos comparten su inventario actual —en el formato que tengan: Excel, foto del cuaderno, exportación, lo que sea— les devolvemos ese análisis en un plazo de dos días, sin costo y sin compromiso. A ustedes les sirve para dirigir sus campañas de donación; a nosotros nos permite validar si el modelo funciona con datos reales o si está equivocado.
>
> También agradeceríamos 15 minutos de conversación con alguien de su equipo operativo para entender cómo reciben y clasifican hoy, y en qué punto se les acumula el trabajo.
>
> **Sobre el manejo de la información:**
>
> - Iniciativa sin fines comerciales. No solicitamos ni recibimos dinero ni donaciones.
> - No publicamos información de terceros sin autorización escrita.
> - Cualquier uso público del material va anonimizado, salvo que ustedes prefieran ser nombrados.
> - Eliminamos lo compartido a solicitud, con confirmación.
> - No recibimos ni procesamos datos personales de damnificados. Solo inventarios y procesos.
>
> Quedamos atentos y agradecidos por el trabajo que están haciendo.
>
> [REPRESENTANTE]
> [REPRESENTANTE_CARGO] · [ASOCIACION]
> [REPRESENTANTE_CORREO] · [TU_TELEFONO]
>
> [TU_NOMBRE]
> [TU_ROL] · [TU_CORREO] · [REPO_URL]

---

## 3.1 Uso del respaldo organizacional — protocolo obligatorio

### El riesgo real

El respaldo institucional no es un adorno de firma: es lo que hace que un coordinador entregue el inventario de su acopio. Es decir, **la afirmación induce materialmente la entrega de los datos**. Eso la vuelve una afirmación que tiene que ser exacta, no aproximada.

Escenario de falla concreto: salen 5 correos diciendo "con el respaldo de [Organización]". Una alcaldía llama a la organización para verificar. La dirección no sabe nada. Resultado: quien dio el respaldo queda expuesto laboralmente, la organización se deslinda públicamente, y el proyecto queda marcado en el único sector donde necesita trabajar. El costo de evitarlo es un mensaje de WhatsApp.

### Tres niveles de afirmación

Usar el más alto que se pueda **respaldar por escrito**, nunca uno por encima.

| Nivel | Formulación | Qué requiere | Cuándo usarlo |
|---|---|---|---|
| **A · Personal** | "[Nombre], [cargo] de [Org], acompaña esta iniciativa a título personal" | Consentimiento por escrito de esa persona | Si no hay autorización de la dirección en 24 h |
| **B · Institucional** | "Esta iniciativa cuenta con el respaldo de [Organización]" | Autorización escrita de quien puede comprometer a la organización | **Recomendado.** Es el punto óptimo entre fuerza y verificabilidad |
| **C · Alianza / logo** | "En alianza con [Org]" + uso de marca | Aprobación formal, alcance definido y responsabilidades por escrito | Solo con documento. Nunca por acuerdo verbal |

**Regla dura:** ninguna de las tres se usa sin respaldo escrito. Un "sí, dale, usa el nombre" dicho por chat **sí cuenta** como escrito, siempre que quede el registro y quien lo dice tenga la atribución para darlo.

### La pregunta que hay que hacer

No es "¿me prestas la imagen?". Es: **"¿tienes atribución para comprometer el nombre de la organización, o necesitas que alguien más lo autorice?"**

Es una pregunta incómoda —más aún si media una relación personal— y es exactamente la que protege a quien da el respaldo. Si la respuesta es que no tiene esa atribución, no se acabó el asunto: se usa el Nivel A, que sigue siendo mucho más fuerte que no tener nada.

### Plantilla de autorización (para que la respuesta quede por escrito)

> Hola [Nombre], para dejarlo formal y que no te quede expuesto a ti:
>
> ¿Me confirmas por este medio que puedo mencionar a [Organización] en los correos de contacto con centros de acopio, en estos términos exactos: *"esta iniciativa cuenta con el respaldo de [Organización]"*?
>
> Concretamente sería para: correos a coordinaciones de acopio pidiendo (a) una conversación de 15 minutos y (b) su inventario para análisis nutricional, sin costo y sin fines comerciales.
>
> Tres cosas para tu tranquilidad:
> - No pido dinero ni donaciones a nombre de nadie.
> - No publico nada con el nombre de la organización sin pasártelo antes.
> - Si en algún momento quieres que deje de usarlo, lo retiro ese mismo día, sin preguntas.
>
> Y la pregunta importante: ¿esto lo puedes autorizar tú, o necesitamos que lo apruebe alguien de dirección? Prefiero mil veces demorarme dos días que ponerte en una situación incómoda.

Guardar la respuesta en `datos/autorizaciones/` (directorio por crear). Sin ese archivo, el Mensaje D2 no se envía y se usa el Mensaje D.

### Táctica: co-firma en lugar de mención

**Un correo enviado desde el dominio institucional de la organización, o con su representante en copia, vale más que cualquier frase de respaldo escrita por un tercero.**

Deja de ser una afirmación sobre un tercero y pasa a ser un hecho verificable en el encabezado del correo. Además le da a la organización control real sobre lo que se dice en su nombre, lo cual hace mucho más probable que acepte.

Orden de preferencia:

1. La organización envía el correo; el responsable técnico va en copia y firma como tal.
2. El correo sale del proyecto, con la representante en copia visible y en la firma.
3. El correo sale del proyecto y solo la menciona en el cuerpo. *(Lo más débil y lo más riesgoso.)*

### Qué recibe la organización a cambio

Un respaldo unilateral es inestable: se retira apenas aparece la primera fricción. Convertido en un intercambio real, deja de ser un favor.

- Crédito explícito en el repositorio y en cualquier publicación del proyecto.
- El análisis de inventario, gratis y prioritario, para su propia operación.
- La hoja de triage con su identidad institucional, si la quieren usar internamente.
- Rol nombrado: contraparte institucional del proyecto, no "contacto que prestó el logo".

Si además la organización **efectivamente usa** la hoja, la afirmación de respaldo deja de ser prestada y pasa a ser un hecho. Ese es el objetivo: que el respaldo sea verdadero, no que suene bien.

---

## 3.2 Iniciativas sin contacto publicado

Muchos acopios ciudadanos aparecen en una historia de Instagram, en un cartel o en un grupo de barrio, y no publican correo ni teléfono. Son con frecuencia los que más falta les hace la hoja, porque nacieron improvisados y sin protocolo.

### La regla que gobierna todo este bloque

**En público solo se ofrece. Nunca se pide.**

Un comentario es visible para cualquiera. Si en público pides el inventario de una organización, tres cosas pasan a la vez: pareces alguien extrayendo datos, expones a la organización ante sus propios donantes, y le das a cualquiera un modelo de cómo pedir datos haciéndose pasar por ayuda. El pedido de inventario **solo existe en canal privado**, y solo después de que ellos abrieron ese canal.

En público el objetivo es uno y solo uno: **conseguir un canal privado**.

### Cinco reglas de etiqueta, no negociables

1. **No comentar en publicaciones sobre víctimas, fallecidos, desaparecidos o rescates.** Solo en publicaciones logísticas: convocatorias de acopio, listas de qué donar, llamados a voluntarios. Aparecer con una herramienta debajo de una foto de un rescate es indefendible por bienintencionado que sea.
2. **Un comentario por cuenta.** Si no responden, no se insiste. Si borran el comentario, tampoco.
3. **No pegar el mismo texto idéntico en muchas cuentas.** Se ve como spam, y las plataformas lo detectan y lo ocultan. Conviene cambiar el orden de las frases en cada uno.
4. **Sin emojis, sin hashtags, sin mayúsculas sostenidas, sin signos de admiración.** El registro es sobrio.
5. **Sin enlaces en el primer comentario.** En Instagram no son clicables y en varias plataformas activan filtros de spam. El enlace va en privado.

---

### Formato P1 · Comentario público en una publicación de acopio

Dos o tres líneas. Ofrecer y pedir canal. Nada más.

> Buenas. Desde [ASOCIACION] armamos una hoja de una página para clasificar donaciones en el punto de recepción, basada en el estándar Esfera y en la guía de la Alcaldía de Bogotá. Es gratuita y de uso libre, sin ningún compromiso. Si les sirve se la enviamos por mensaje directo: díganme por dónde y se las paso. Gracias por lo que están haciendo.

**Variante corta**, para publicaciones con muchos comentarios:

> Desde [ASOCIACION]: tenemos una hoja de una página para clasificar donaciones en recepción, gratuita y de uso libre. Si les sirve, escríbannos por directo y se las enviamos.

---

### Formato P2 · Mensaje directo

Aquí sí se puede desarrollar. Sigue sin pedirse el inventario en el primer mensaje.

> Buenas, les escribo desde [ASOCIACION]. [FORMULA_RESPALDO].
>
> Vi que están recibiendo donaciones y quería dejarles algo que puede ahorrarles tiempo en recepción: una hoja de una página para clasificar lo que llega, pensada para que un voluntario sin experiencia decida en pocos segundos qué sirve, qué no y a qué pila va cada cosa. Está basada en el estándar humanitario Esfera, en la taxonomía SUMA de la OPS y en la guía de qué donar y no donar de la Alcaldía de Bogotá, con las fuentes citadas.
>
> Es gratuita y de uso libre. Si me pasan un correo se las envío en PDF, lista para imprimir. También la tengo en tamaño grande para pegar en la pared del punto de recepción.
>
> Si en algún momento les interesa, hacemos algo más: a partir del inventario que tengan calculamos cuántas personas se pueden alimentar completo con lo que hay y qué es lo que conviene pedir. Sin costo. Pero eso lo vemos si les sirve, no hay ninguna prisa.
>
> [TU_NOMBRE] · [TU_CORREO]

---

### Formato P3 · Formulario web de contacto

Los formularios genéricos suelen tener límite de caracteres y no garantizan respuesta. Todo tiene que caber y quedar autoexplicado.

> **Asunto / motivo:** Hoja de clasificación de donaciones, uso libre
>
> Buenas. Escribo desde [ASOCIACION], en [TU_CIUDAD]. [FORMULA_RESPALDO].
>
> Tenemos una hoja de una página para clasificar donaciones en el punto de recepción, basada en el estándar Esfera, la taxonomía SUMA de la OPS y la guía de la Alcaldía de Bogotá. Sirve para que un voluntario sin experiencia clasifique rápido y para reducir lo que termina descartado. Es gratuita y de uso libre, no vendemos nada y no pedimos donaciones.
>
> Se las envío en PDF si me responden a este correo: [TU_CORREO]. También está disponible en [REPO_URL].
>
> Si les interesa, podemos analizar su inventario sin costo y decirles qué les hace falta pedir. Quedo atento.
>
> [TU_NOMBRE] · [TU_ROL] · [TU_CORREO]

---

### Formato P4 · Guion presencial en el punto de acopio

**El de mayor rendimiento de todos.** Nada convence más que aparecer con la hoja impresa en la mano.

**Antes de ir:**

- Llevar **20 copias impresas** de la hoja A4 y 2 en A3. Se entregan, no se muestran.
- Ir en hora valle: media mañana entre semana. Nunca en pico de recepción ni al cierre.
- No ayudar y proponer al mismo tiempo. Quien se ofrece como voluntario, ese día es voluntario.

**Los 30 segundos:**

> — Buenas, ¿quién está coordinando la recepción?
>
> *(esperar, no explicarle nada a quien no decide)*
>
> — Hola, soy [TU_NOMBRE], de [ASOCIACION]. No vengo a pedirles nada. Les traje esto: es una hoja de una página para clasificar lo que llega, basada en el estándar Esfera y en la guía de la Alcaldía de Bogotá. La grande es para pegar en la pared, estas son para los voluntarios.
>
> *(entregar físicamente y callar)*
>
> — Si les sirve, úsenla; si no, la botan sin problema. Lo único que les pediría, cuando tengan un rato, es que me digan qué le falta o qué está mal, porque la estamos mejorando con gente que sí está en el terreno.
>
> — Les dejo mi contacto por si acaso. Gracias por lo que están haciendo.

**Lo que no se hace:** no explicar el modelo matemático, no pedir el inventario en la primera visita, no quedarse más de lo necesario, no interrumpir la operación. Si preguntan más, se responde; si no, se sale. La segunda conversación se gana con la primera.

---

### Formato P5 · Tarjeta física para dejar

Media carta, se imprimen 8 por hoja y se cortan. Es lo que queda después de la visita.

```
------------------------------------------------
  HOJA DE TRIAGE DE DONACIONES        uso libre
------------------------------------------------
  Clasificación rápida en punto de recepción.
  Basada en el estándar Esfera, taxonomía SUMA
  (OPS) y la guía de la Alcaldía de Bogotá.

  Descarga:  [REPO_URL]

  También hacemos, sin costo:
  a partir de su inventario, cuántas personas se
  pueden alimentar completo y qué falta pedir.

  [ASOCIACION]
  [TU_NOMBRE] · [TU_CORREO] · [TU_TELEFONO]

  Nos sirve mucho su crítica: díganos qué le
  falta o qué está mal.
------------------------------------------------
```

---

### Formato P6 · Cuando responden en público

Mover a privado de inmediato, sin conversar de logística a la vista de todos.

> Gracias. Le escribo por directo ahora mismo y le paso la hoja en PDF. Cualquier cosa que necesite, quedo atento por ahí.

---

### Registro de estos contactos

Van en el mismo `datos/contactos.csv`, con dos columnas adicionales, porque el rendimiento de los canales públicos es muy distinto al del correo y conviene poder compararlos:

| Campo extra | Para qué |
|---|---|
| `canal_origen` | comentario, DM, formulario, presencial |
| `respuesta_publica` | sí / no — permite medir si comentar en público sirve o es ruido |

Si al cierre de F0 ningún canal público produjo respuesta, se documenta y **no se repite la táctica** en la siguiente iteración. Es una hipótesis a falsar, no una convicción.

---

### Mensaje E · Correo post-entrevista (dentro de 24 h)

> [Nombre], gracias por los 15 minutos.
>
> Te resumo lo que entendí, para que me corrijas si me equivoqué en algo:
>
> 1. [afirmación textual del coordinador]
> 2. [afirmación]
> 3. [afirmación]
>
> Lo que más me sirvió fue [hallazgo concreto], porque cambia [decisión específica de diseño].
>
> Dos cosas puntuales sobre la hoja que te mandé, si tienes un minuto:
>
> - ¿Qué regla le sobra o está de más?
> - ¿Qué decisión toman ustedes a diario que no aparece ahí?
>
> Con cualquiera de las dos respuestas ya sale la v1, y te la mando apenas esté.
>
> [Tu nombre]

Devolver el resumen cumple tres funciones a la vez: valida las notas, demuestra que hubo escucha, y hace que la petición de crítica sea el paso natural en lugar de un segundo favor.

---

## 4. Guion de entrevista — 15 minutos

Reordenado por valor de información por minuto. Si solo hay 5 minutos, se hacen los bloques 1 y 2 y nada más.

**Antes de empezar:** *"¿Te molesta si tomo notas? No grabo nada sin que me digas que sí."*

**Bloque 1 · Cómo funciona hoy (min 0-5)**

1. Cuéntame el recorrido de una caja: desde que llega al andén hasta que sale hacia el destino. *(Pregunta narrativa, no analítica — produce mucho más detalle.)*
2. ¿Cómo registran lo que entra? ¿Cuaderno, Excel, WhatsApp, nada?
3. ¿Cuántas personas reciben y clasifican por turno y cuánto dura el turno?

**Bloque 2 · El cuello de botella (min 5-9) — el núcleo de la entrevista**

4. **¿Qué es lo que más los frena hoy?** *(Pregunta abierta. No sugieras opciones. Después de preguntar, cállate y espera, aunque el silencio sea incómodo: la primera respuesta suele ser genérica y la segunda es la verdadera.)*
5. Cuéntame la última vez que algo se atascó de verdad. ¿Qué pasó exactamente? *(Un incidente concreto revela más que cualquier generalización.)*
6. ¿Qué haría que rechazaran de entrada una herramienta nueva?

**Bloque 3 · Desperdicio y decisiones (min 9-12)**

7. ¿Qué porcentaje de lo que llega se descarta, y por qué motivo principal?
8. ¿Qué les sobra hoy? ¿Qué les falta?
9. ¿Cómo deciden qué va en cada envío o kit?

**Bloque 4 · Entorno y cierre (min 12-15)**

10. ¿Reciben información de vuelta de quien recibe la ayuda?
11. ¿Hay señal en el acopio? ¿Y en el punto de entrega? ¿Qué teléfonos usan los voluntarios?
12. ¿Usan alguna guía o protocolo? ¿SUMA, Esfera, algo de la UNGRD?

**Cierre:** *"¿Hay algo que debí preguntarte y no se me ocurrió?"* — suele ser la respuesta más valiosa de toda la entrevista.

**Cuatro reglas de disciplina:**

- No proponer soluciones durante la llamada. Es una recolección, no una venta. Proponer contamina todas las respuestas siguientes.
- Pedir números siempre que se pueda: "¿cuántos?", "¿cuánto tiempo?", "¿cada cuánto?".
- Preferir "cuéntame la última vez que..." sobre "normalmente qué hacen...". El pasado concreto es dato; el presente habitual es opinión.
- Si la respuesta contradice el diseño, esa es la información más valiosa de la llamada. Anotarla literal, sin suavizarla.

---

## 5. Métricas de la Fase 0

| ID | Métrica | Objetivo | Umbral de alarma |
|---|---|---|---|
| O1 | Tasa de respuesta (respuestas / contactados) | ≥ 30 % | < 20 % → revisar asunto y primera línea |
| O2 | Horas hasta la primera respuesta | ≤ 24 h | > 48 h → activar Mensaje C |
| O3 | Entrevistas conseguidas | ≥ 2 | 0 tras la primera semana → ampliar la lista de contactos |
| O4 | Artefactos de registro obtenidos (F0.9) | ≥ 1 | 0 → F1.3 y F1.4 quedan sin datos reales |
| O5 | Críticas concretas a la hoja | ≥ 1 | 0 → el ciclo de devolución no cierra |

**O4 es la métrica dominante de toda la fase.** Un solo inventario real desbloquea la calibración de `a_i` (F1.3) y el motor de optimización (F1.4). Dos entrevistas sin un solo artefacto de datos valen menos que un artefacto sin entrevista.

---

## 6. Registro de contactos

Llevar en `datos/contactos.csv` (archivo por crear). Un contacto sin fecha de próximo seguimiento es un contacto perdido.

| Organización | Ciudad | Persona | Canal | Enviado | Respuesta | Entrevista | Artefacto | Estado | Próximo paso |
|---|---|---|---|---|---|---|---|---|---|
| | | | WA + correo | | | | | enviado | recordatorio a 48 h |
| | | | correo | | | | | | |

---

## 7. Compromisos de manejo de datos

No negociables. Van explícitos en el Mensaje B y se cumplen sin excepción.

- Sin fines comerciales. Sin solicitud de dinero.
- Sin publicación de datos de terceros sin autorización escrita.
- Anonimización por defecto en cualquier uso público.
- Borrado a solicitud, con confirmación al solicitante.
- Sin grabación de llamadas sin consentimiento explícito previo.
- Sin datos personales de damnificados: solo inventarios y procesos. Si alguien comparte por error una lista con nombres o cédulas de beneficiarios, se elimina de inmediato y se avisa.

El último punto es el que más fácil se viola por accidente y el de peores consecuencias. Un Excel de acopio suele traer una pestaña con nombres de beneficiarios.

---

## Fuentes

- [Sphere Handbook — Standards](https://handbook.spherestandards.org/en/sphere/)
- [SUMA/LSS — Sistema de manejo de suministros humanitarios, OPS/OMS](https://www.paho.org/disasters/index.php?option=com_content&view=article&id=697:suma-lss-humanitarian-supply-management-system&Itemid=924&lang=es)
- [Qué donar y no donar en Bogotá — Alcaldía de Bogotá](https://bogota.gov.co/mi-ciudad/ambiente/que-donar-y-no-donar-en-bogota-para-damnificados-terremoto-colombia)
- [Centros de acopio habilitados en Colombia — Infobae](https://www.infobae.com/colombia/2026/08/10/centros-de-acopio-habilitados-en-colombia-tras-el-terremoto-guia-por-ciudad-para-donar-y-ayudar-a-las-victimas/)
