# Auditoría de Gravitas

**URL:** `mapa.gravitasworld.com`
**Creador:** Juan Camilo Garzón · Senza Create (Pereira). Equipo de 5 personas
**Origen:** plataforma de mapeo de potencial turístico rural, desarrollada con apoyo de ONU. Reconvertida a mapeo de emergencia **en 42 horas** tras el sismo
**Fecha de auditoría:** 27 de agosto de 2026, 23:25 (hora del último snapshot del sitio)

---

## Resumen

Gravitas es la plataforma más cercana a un registro ciudadano de acopios que existe hoy en Colombia, y está mucho mejor diseñada de lo que su cobertura de prensa sugiere. **Pero reproduce, con siete días de vida, exactamente la misma patología documentada en la UNGRD: el modelo de datos correcto, completamente vacío.**

Esto no es una crítica al equipo de Gravitas —hicieron en 42 horas lo que la institucionalidad no ha hecho en catorce años—. Es la evidencia más limpia disponible de que **el problema no es de software**.

---

## 1. Qué es y cómo funciona

Aplicación Next.js con API pública en `/api/snapshot` (JSON, sin autenticación). Cuatro categorías de reporte:

| Categoría | Descripción declarada |
|---|---|
| **Edificio** | Edificio o estructura colapsada / dañada |
| **Centro de acopio** | Centro de acopio, albergue o puesto de mando |
| **Logística** | Vehículos, rutas, carga |
| **Voluntariado** | Persona disponible para ayudar |

Fuentes declaradas: reportes ciudadanos, datos satelitales (menciona Copernicus), redes sociales —sobre todo Twitter—, grupos oficiales de WhatsApp e informes de alcaldías. Verificación mixta: administradores humanos más un sistema de IA que corrobora cuando varias personas reportan el mismo punto.

A la fecha de la nota de prensa (13 de agosto) reportaban ~250 reportes ciudadanos y ~850 internos.

---

## 2. El modelo de datos — es bueno

El esquema por registro, extraído de la API:

```
id · title · category · status · city · neighborhood · address_text
trust_level · report_count · category_fields · description
first_reported_at · last_reported_at
needs_total · needs_cubiertas · needs_abierta · responses_count
department_id · department_name · department_priority · department_is_epicenter
```

Con `category_fields` anidado: `tipo`, `capacidad_actual`, `organizacion_responsable`, `contacto`, `necesita[]`.

**Esto es un modelo de emparejamiento oferta–demanda.** `needs_total / needs_cubiertas / needs_abierta` distingue necesidad declarada, necesidad cubierta y brecha abierta. Alguien pensó bien el problema.

---

## 3. Lo que está vacío

Sobre 82 registros recuperados de la API:

| Campo | Estado |
|---|---|
| `needs_total` | **0 en el 100%** |
| `needs_cubiertas` | **0 en el 100%** |
| `needs_abierta` | **0 en el 100%** |
| `responses_count` | 0 en el 98% (3 respuestas en total) |
| `report_count` | **1 en el 100%** |
| `trust_level` | **2 en el 100%** — constante, no discrimina |
| `capacidad_actual` | **"disponible" en el 100%** — constante, no discrimina |
| `necesita[]` | presente en 20 de 82, y **con un único valor posible: "voluntarios"** |
| `neighborhood` | **0 de 82** |
| `department_is_epicenter` | **false en el 100%** |

Tres consecuencias:

1. **La capa de necesidades no tiene un solo dato.** El campo que haría útil la plataforma —cuánto se necesita, cuánto se cubrió, cuánto falta— está en cero en todos los registros.
2. **El mecanismo de corroboración nunca se ha activado.** `report_count = 1` en todos. La verificación por coincidencia de múltiples reportes, que el fundador describe como el núcleo del sistema, no tiene con qué operar. Y `trust_level` constante en 2 significa que no está diferenciando nada.
3. **`capacidad_actual` siempre dice "disponible".** Un acopio saturado y uno vacío se ven idénticos. Es justamente el dato que evitaría la concentración que la plataforma dice querer evitar.

---

## 4. La taxonomía colapsó

Conteo por categoría en la interfaz, a la fecha de auditoría:

| Categoría | Reportes |
|---|---|
| Edificio | **0** |
| Centro de acopio | **184** |
| Logística | 14 |
| Voluntariado | **0** |

**184 de 198 reportes (93%) están bajo "Centro de acopio", y la mayoría no son centros de acopio.** Ejemplos textuales tomados del listado:

- *"Ingenieros civiles, ingenieros estructurales y arquitectos que puedan apoyar las labores de evaluación"* → es voluntariado
- *"Registro ciudadano para ayudar a localizar personas desaparecidas"* → no es ninguna de las cuatro categorías
- *"APOYO PSICOLÓGICO GRATUITO - SISMO"* → servicio, no acopio
- *"Línea Salvavidas para brindar acompañamiento emocional"* → servicio
- *"Profesionales médicos para conformar una red de teleconsultas"* → voluntariado
- *"Convocatoria urgente de profesionales con disponibilidad para desplazarse al Chocó"* → voluntariado

**Voluntariado marca cero mientras decenas de convocatorias de voluntarios están archivadas como acopios.** La categoría más amplia se convirtió en el cajón de sastre, y con eso se perdió la capacidad de filtrar — que era el propósito.

---

## 5. El sesgo geográfico, que es el hallazgo grande

Distribución territorial de los 198 reportes:

| Ciudad | Reportes | ¿Afectada? |
|---|---|---|
| **Bogotá** | **68** | No |
| Nacional (sin ubicación) | 42 | — |
| **Medellín** | **19** | No |
| Cali | 12 | Sí |
| **Cartagena** | **9** | No |
| Quibdó | 5 | Sí, cerca del epicentro |
| Pereira | 4 | Sí |
| Manizales | 4 | Sí |
| Pasto | 4 | No |
| Barranquilla | 3 | No |
| Armenia, Ibagué | 3 c/u | Parcial |
| Chía, Buenaventura, Villavicencio | 2 c/u | Solo Buenaventura |
| Mosquera, Itagüí | 1 c/u | No |

**Bogotá, Medellín y Cartagena —ninguna afectada— concentran 96 reportes. Quibdó, Pereira y Manizales —las ciudades del desastre— suman 13.**

En el subconjunto de la API recuperado, `department_is_epicenter` es `false` en el 100% de los casos y **Chocó no aparece ni una vez**.

Gravitas no está mapeando dónde se necesita ayuda. **Está mapeando dónde hay gente con conexión, tiempo y ganas de ayudar.** Es el fenómeno de la segunda ola medido en tiempo real: la oferta de ayuda se organiza sola en las ciudades ricas no afectadas, mientras la demanda, en las zonas golpeadas, permanece invisible.

---

## 6. Qué significa para el proyecto

### Lo que confirma

- **El diagnóstico es compartido.** Otro equipo llegó por su cuenta al mismo planteamiento.
- **El software no es el cuello de botella.** Gravitas construyó en 42 horas un modelo de datos mejor que el de la UNGRD. Sigue vacío.
- **El cuello de botella es la captura en el punto de origen.** Nadie está parado en la puerta del acopio contando lo que entra.

### Lo que cambia

Gravitas ya tiene el mapa, la agregación y el modelo de necesidades — **y los tiene vacíos por falta de registro en el punto de origen.** Eso deja ese registro como lo único escaso, y convierte a Gravitas en **aliado natural, no en competencia**: ellos tienen el mapa y la API; les falta el dato.

### Riesgo real

Si Gravitas resuelve la captura primero, el proyecto pierde su razón de ser. Tienen ventaja de tiempo, prensa, acceso donado a alcaldías y gobernaciones, y respaldo de ONU por su trabajo previo. **Pero llevan siete días con `needs_total` en cero, lo cual sugiere que la captura es difícil por razones que no son técnicas** — que es precisamente lo que la fase de campo debe averiguar.

### Recomendación

**Contactar al creador de Gravitas en el corto plazo.** No para proponer sociedad todavía, sino para una entrevista: es el mejor informante posible sobre por qué la captura falla. Ha visto el problema desde adentro, en tiempo real, y su plataforma es la prueba documentada. Esa conversación vale más que cinco entrevistas de acopio.

Además, su API pública `/api/snapshot` es fuente de datos aprovechable ya mismo para monitorear la evolución de la respuesta ciudadana.

---

## 7. Otras plataformas ciudadanas surgidas del sismo — pendientes de auditar

| Plataforma | URL |
|---|---|
| Mapa de ayuda — Contemos | `mapa.contemos.org` |
| Economía Para la Pipol | `economiaparalapipol.com/interactivos/mapa-ayuda-colombia/` |
| Mapa del terremoto | `mapadelterremoto.com` |
| SOS Colombia: Red de Ayuda Humanitaria | `sos-colombia2026.netlify.app` |
| Elsah | plataforma de ayuda humanitaria y logística |
| Asocapitales | herramienta de búsqueda de desaparecidos |

**Al menos seis iniciativas paralelas en una semana, ninguna coordinada con otra.** La fragmentación de la respuesta digital es un hallazgo por derecho propio: replica en software la misma dispersión que critica en la logística física. Vale la pena auditarlas y documentar el solapamiento.

---

## Notas metodológicas

- Los conteos por categoría y ciudad provienen de la interfaz del sitio el 27 de agosto de 2026, sobre 198 reportes activos.
- El análisis de campos vacíos se hizo sobre 82 registros recuperados de `/api/snapshot`; la respuesta completa se truncó al descargarla. La muestra puede no ser aleatoria, pero la uniformidad absoluta —100% en cada campo— hace improbable que el resto difiera sustancialmente.
- La API es pública y sin autenticación: cualquiera puede reproducir y ampliar esta auditoría.

## Fuentes

- [Gravitas — Mapeo Ciudadano de Emergencia](https://www.mapa.gravitasworld.com/)
- API pública: `https://www.mapa.gravitasworld.com/api/snapshot`
- [El Colombiano — Terremoto en Colombia: la plataforma que usa IA para organizar ayudas, voluntarios y recursos (13 de agosto de 2026)](https://www.elcolombiano.com/tecnologia/plataforma-ia-organiza-ayudas-voluntarios-recursos-terremoto-colombia-KC39918222)
- [Infobae — Mapa en tiempo real de lugares para ayudar como voluntario](https://www.infobae.com/colombia/2026/08/14/este-es-el-mapa-en-tiempo-real-con-los-lugares-en-bogota-donde-puede-ayudar-como-voluntario-en-el-envio-de-donaciones-para-los-afectados-por-el-terremoto-en-colombia/)
- [Colombia Visible — Cinco plataformas digitales para ayudar a víctimas del terremoto](https://colombiavisible.com/cinco-apps-ayudar-afectados-terremoto-colombia/)
