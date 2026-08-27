# Fase 0 · Cómo vamos a validar esto

**Actualizado:** 27 de agosto de 2026
**Ventana:** 27 de agosto – 19 de septiembre de 2026

Esta es la página a la que apunta el enlace del segundo video. Explica qué estamos probando, cómo, y en qué puede fallar.

---

## Qué estamos probando exactamente

El modelo afirma que un centro de acopio puede medir su rendimiento en **días-persona de ración completa**, y que de ese cálculo sale automáticamente qué pedir a continuación.

Eso es una hipótesis construida sobre inventarios de ejemplo. **No ha tocado una bodega real.** Fase 0 existe para descubrir en qué está equivocada antes de escribir más código.

---

## Los cuatro supuestos que pueden tumbar el modelo

Están ordenados por probabilidad de ser falsos.

### 1. Que el acopio conozca su inventario

El modelo necesita `q_i`: cuánto hay de cada ítem. Damos por hecho que es observable.

**Puede ser falso si:** las donaciones llegan en bolsas mezcladas sin pesar, la rotación es más rápida que la capacidad de contar, o nadie tiene tiempo para inventariar durante la fase aguda.

**Cómo lo probamos:** preguntando qué se sabe hoy del inventario, en qué momento se sabe y quién lo sabe.

### 2. Que los topes de aceptabilidad sean estables

`a_i` es el máximo de un alimento que una persona acepta por día. Es el parámetro **más débil** del modelo, porque es cultural y no técnico.

**Puede ser falso si:** varía tanto por región, edad o costumbre que no admite un número único, o si en emergencia la gente acepta cosas que en condiciones normales no.

**Cómo lo probamos:** preguntando qué alimentos se devuelven, cuáles sobran siempre y cuáles se acaban primero.

### 3. Que el registro sea posible durante la emergencia

Todo el proyecto depende de que alguien anote entradas y salidas mientras la bodega está saturada.

**Puede ser falso si:** el costo de registrar compite con el de operar. Es la hipótesis más importante, porque **dos plataformas ya fracasaron en esto**: los campos de ayuda entregada de la UNGRD están vacíos en el 98–99,7% de los registros, y los campos de necesidades de Gravitas en el 100%.

**Cómo lo probamos:** pidiendo ver el formato real que usan hoy, aunque sea un cuaderno, y preguntando qué se dejó de anotar y por qué.

### 4. Que la ración completa sea el objetivo correcto

El modelo maximiza raciones nutricionalmente completas. Es una decisión ética, no técnica: prefiere alimentar bien a pocos antes que mal a muchos.

**Puede ser falso si:** en la práctica el criterio real es otro —cubrir el mayor número de familias, vaciar la bodega antes de que se dañe, atender primero a quien llegó—.

**Cómo lo probamos:** preguntando cómo se decide hoy qué sale primero.

---

## Con quién hablamos

Coordinadores de centros de acopio, priorizando los que operaron en zona afectada. Meta: **entre 5 y 8 entrevistas.** No buscamos representatividad estadística: buscamos encontrar el error.

También queremos hablar con equipos que ya construyeron plataformas de respuesta, porque su experiencia sobre por qué falla la captura vale más que varias entrevistas de acopio.

---

## Cómo lo hacemos

1. **Primer contacto** por WhatsApp: breve, con la contrapartida anunciada por adelantado.
2. **Correo** para agendar y dar contexto formal.
3. **Entrevista** de 30–40 minutos. Los formatos de registro se piden **durante** la conversación, no antes: pedirle a un desconocido sus documentos internos en el primer mensaje se lee como extracción de datos.
4. **Devolución**: entregamos el análisis de su inventario.
5. **Crítica**, una o dos semanas después. Nadie critica útilmente algo que acaba de recibir.

### Compromisos

- Pedimos plantillas **en blanco o anonimizadas**. No queremos datos de beneficiarios.
- Las transcripciones se anonimizan antes de publicarse.
- Nadie queda mencionado sin autorización escrita.
- Lo que se aprenda se publica, incluido lo que nos deje mal.

---

## La pregunta de oro

Al final de cada entrevista:

> **¿Qué información necesitabas y no tenías?**

Contestada por alguien que acaba de coordinar un acopio real, esa respuesta vale más que todo el análisis de escritorio de este repositorio.

---

## Qué pasa si el modelo falla

Se documenta y se publica. Un resultado negativo bien establecido —"medir raciones completas no es viable en campo porque X"— es un aporte real y evita que otro lo intente de nuevo por el mismo camino.

Lo que no vamos a hacer es ajustar la narrativa para que el modelo sobreviva.

---

## En paralelo: derechos de petición

Radicados ante UNGRD, DANE, Contraloría General y DNP para establecer si existe información no publicada sobre desempeño logístico. Término legal: 10 días hábiles.

Si responden "no tenemos esa información", **esa negativa es el hallazgo** y se publica igual.

Textos completos en [`docs/investigacion/`](investigacion/).

---

## Cómo participar

- **Nutricionistas y personal de salud:** revisar los supuestos nutricionales y los topes de aceptabilidad.
- **Logística humanitaria:** decirnos qué está mal.
- **Organizaciones con inventarios reales:** compartir un inventario y recibir el análisis de vuelta, sin costo ni compromiso.

Estamos empezando, así que podemos tomar los primeros casos con cuidado. Si coordinas o conoces un centro de acopio, escríbenos.
