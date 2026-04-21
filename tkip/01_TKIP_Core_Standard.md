# TKIP Core Standard

**Territorial Knowledge Ingestion Protocol — Core Standard**
Versión 1.2 — Stable
Abril 2026
Licencia del documento: CC-BY-4.0

---

## Convenciones normativas

Las palabras **DEBE**, **NO DEBE**, **DEBERÍA**, **NO DEBERÍA**, **PUEDE** y **NO PUEDE** en este documento se interpretan conforme a la convención RFC 2119. Su uso en versalita indica requisito normativo.

El contenido marcado como *Informativo* no forma parte normativa del estándar. Los ejemplos son informativos salvo que se diga lo contrario.

---

## 1. Alcance

Este documento define el protocolo técnico común para ingesta de conocimiento territorial. Especifica la estructura de datos, los estados de flujo, los canales admisibles, el mecanismo de trazabilidad y el sistema de extensión temática.

Este documento **NO** define gobernanza curatorial (ver `[02:*]`), doctrina (ver `[03:*]`), amenazas (ver `[04:*]`), resolución de conflictos (ver `[05:*]`), ni configuraciones piloto (ver `[06:*]`).

Una implementación conforme DEBE satisfacer todos los requisitos **DEBE** de este documento. PUEDE satisfacer requisitos **DEBERÍA** y **PUEDE**.

---

## 2. Términos y definiciones

**Contribution Object (CO)** — unidad atómica de ingesta. Estructura de datos serializable en YAML o JSON que contiene contenido y metadatos.

**Canal** — medio técnico por el cual un CO ingresa al sistema.

**Curador** — rol humano o sistémico que participa en la evolución de un CO dentro del pipeline. Definido en `[02:*]`.

**Dominio** — una de las seis áreas temáticas canónicas en que el contenido territorial se clasifica primariamente.

**Capa transversal** — una de las siete dimensiones de metadatos aplicables a cualquier CO.

**Extension Profile** — módulo opcional que añade campos específicos a un CO para cubrir las necesidades de un dominio o comunidad de práctica.

**Pipeline** — la secuencia ordenada de estados por los que pasa un CO.

**Provenance Chain** — lista append-only de eventos que documenta la trayectoria de un CO.

**Repositorio** — sistema de almacenamiento final donde los CO publicados quedan indexados y accesibles.

**Track de curación** — velocidad de procesamiento asignada a un CO (auto, light, deep).

---

## 3. Arquitectura del pipeline

Todo CO en el sistema DEBE recorrer, en orden estricto, las cuatro etapas del pipeline:

```
CAPTURA → CONVERGENCIA → CURACIÓN → REPOSITORIO
```

### 3.1 Captura

Un emisor envía contenido por un canal admisible (sección 5). El sistema de captura DEBE generar un identificador único, DEBE registrar fecha de recepción en ISO-8601 con zona horaria, y DEBE preservar el payload crudo original.

### 3.2 Convergencia

El sistema DEBE transformar el payload crudo en un CO conforme al schema definido en la sección 4. Las transformaciones automáticas admisibles incluyen: transcripción de audio, extracción de EXIF, limpieza de texto, resolución de ubicación, generación de vista previa, cálculo de hash.

Toda transformación automática DEBE registrar un evento `enriched` en la Provenance Chain del CO.

### 3.3 Curación

El CO DEBE ser asignado a un track de curación (auto, light o deep) por un proceso de *triage*. Toda publicación final DEBE estar firmada por al menos un curador humano. No existe publicación directa sin curación humana.

La definición de los tracks, sus umbrales y la matriz de permisos curatoriales se especifican en `[02:*]`.

### 3.4 Repositorio

Un CO publicado DEBE persistirse en un repositorio indexable. El repositorio DEBE soportar consulta por cualquiera de las siete capas transversales (sección 4.5) y por dominio.

Un CO publicado NO DEBE eliminarse físicamente. Puede ser retractado o archivado, pero la Provenance Chain persiste.

---

## 4. Contribution Object — schema

### 4.1 Principios

El schema sigue los siguientes principios invariantes:

- **Auto-contenido**: un CO DEBE contener toda la información necesaria para trazar su origen, procesamiento y destino.
- **Extensible por metadatos, no por subcarpetas**: el crecimiento es horizontal, en campos, no vertical en jerarquías.
- **Append-only en provenance**: la Provenance Chain (sección 6) es inmutable por contrato.
- **Multimedia agnóstico**: el schema no privilegia texto sobre audio, imagen, video o dato tabular.
- **Consentimiento primero**: todo CO con autoría identificable DEBE contener consentimiento explícito.

### 4.2 Campos obligatorios mínimos (MVP)

Un CO DEBE contener, como mínimo, los siguientes campos poblados:

1. `id`
2. `source.contributor_id`
3. `source.consent.level`
4. `channel.type`
5. `channel.received_at`
6. `domain.primary`
7. `layers.content_type`
8. `content.raw_ref` o `content.preview`
9. `access.level`
10. `status`
11. `provenance` con al menos un evento `received`

La ausencia de cualquiera de estos campos produce un CO inválido. Un CO inválido NO DEBE pasar a estado `published`.

### 4.3 Schema completo

```yaml
contribution:

  # ─── Identificación ────────────────────────────────────────
  id: string                         # formato: tkip-YYYY-MMDD-<hash4>
  version: integer                   # empieza en 1, incrementa en curaciones mayores
  parent_id: string | null           # id del CO del que deriva, si aplica
  supersedes: [string]               # ids reemplazados por este CO

  # ─── Origen y consentimiento ───────────────────────────────
  source:
    contributor_id: string           # id estable y anónimo por canal
    contributor_display: string | null
    contributor_role: enum           # ver 4.4
    contributor_organization: string | null
    consent:
      level: enum                    # ver 4.4
      obtained_at: datetime          # ISO-8601 con timezone
      obtained_by: string            # id del agente que obtuvo el consentimiento
      method: enum                   # ver 4.4
      scope: [enum]                  # ver 4.4 (uno o más)
      revocable: boolean
      expires_at: datetime | null

  # ─── Canal de entrada ──────────────────────────────────────
  channel:
    type: enum                       # ver 4.4
    reference: string                # id original del canal (ej. wamid, email msg-id)
    received_at: datetime
    captured_by: string              # id del agente receptor
    raw_payload_ref: string          # ruta al payload crudo preservado

  # ─── Dominio temático (uno solo) ───────────────────────────
  domain:
    primary: enum                    # ver 4.4
    cross_indexed: [enum]            # otros dominios que aplican transversalmente
    subdomain: string | null         # libre, sujeto a tesauro controlado

  # ─── Capas transversales (las siete) ───────────────────────
  layers:
    location:
      place_name: string | null
      gps: [number, number] | null   # [lat, lon] WGS84
      precision_m: number | null
      source: enum                   # ver 4.4
      confidence: enum               # ver 4.4
    scale:
      level: enum                    # ver 4.4
    temporality:
      refers_to: enum                # ver 4.4
      period_start: integer | null   # año
      period_end: integer | null
      reference_date: date | null
    origin_layer:
      original_source: string
      medium: enum                   # ver 4.4
      contributor_relationship: string | null
    actor:
      relates_to: [enum]             # ver 4.4
      roles_mentioned: [string]
    content_type: enum               # ver 4.4
    validation:
      level: enum                    # ver 4.4
      validated_by: [string]         # ids de curadores
      cross_references: [string]     # ids de CO que corroboran

  # ─── Contenido ─────────────────────────────────────────────
  content:
    raw_ref: string | null
    processed_ref: string | null
    preview: string | null           # ≤ 500 caracteres
    language: string                 # BCP-47 (ej. "es-CL", "en")
    word_count: integer | null
    duration_seconds: number | null
    attachments: [attachment]        # ver 4.3.1

  # ─── Acceso ─────────────────────────────────────────────────
  access:
    level: enum                      # ver 4.4
    publication_scope: enum          # ver 4.4
    restricted_reason: string | null # obligatorio si level != publica
    restricted_until: date | null
    opens_by_default_on: date | null
    review_required_every: duration | null # ej. "P2Y" = cada 2 años

  # ─── Pipeline ───────────────────────────────────────────────
  status: enum                       # ver 4.4
  curation_track: enum               # ver 4.4
  curator_notes: string | null

  # ─── Provenance Chain (sección 6) ───────────────────────────
  provenance: [provenance_event]

  # ─── Extension Profiles (sección 8) ─────────────────────────
  extensions:
    # objeto clave-valor donde clave es el id del profile
    # valor es el bloque de campos definido por ese profile
    <profile_id>: { ... }

  # ─── Referencias cruzadas ───────────────────────────────────
  references:
    related_contributions: [string]
    repository_nodes: [string]
    external_sources: [string]       # URLs, DOIs, ISBN

  # ─── Licenciamiento (sección 9) ─────────────────────────────
  licensing:
    license: enum                    # ver sección 9
    attribution_required: boolean
    attribution_text: string | null
    commercial_use: boolean
    derivatives_allowed: boolean
    share_alike: boolean
```

#### 4.3.1 Estructura de `attachment`

```yaml
attachment:
  type: enum                         # image | audio | video | document | dataset | other
  ref: string                        # ruta al archivo
  description: string | null
  hash: string                       # sha256:<hex>
  exif_preserved: boolean
  size_bytes: integer
```

### 4.4 Enums canónicos

Los siguientes enums son normativos. Una implementación conforme NO DEBE admitir valores fuera de estas listas para los campos indicados, salvo que el campo permita extensión por tesauro controlado (indicado explícitamente).

#### 4.4.1 `source.contributor_role`

```
vecino | operador | arriero | escalador | investigador | cronista |
visitante | guardaparque | asesor_legal | equipo_gestion | 
autoridad | organizacion | otro
```

#### 4.4.2 `source.consent.level`

```
anonimo | atribuido | reservado
```

**Definiciones**:
- `anonimo`: el contribuyente no desea ser identificado. `contributor_display` DEBE ser `null`.
- `atribuido`: el contribuyente consiente atribución pública de su aporte.
- `reservado`: se registra identidad a efectos de trazabilidad pero no se publica.

#### 4.4.3 `source.consent.method`

```
whatsapp_acknowledged | form_checkbox | signed_document | 
verbal_confirmed | email_reply | implicit_by_submission
```

`implicit_by_submission` sólo es admisible para CO aportados en canales profesionales donde el envío constituye consentimiento operativo (ej. carga directa por equipo técnico propio).

#### 4.4.4 `source.consent.scope`

Lista (puede ser múltiple). Cada alcance es consentido explícitamente.

```
archivo | publicacion_comunitaria | publicacion_abierta |
atribucion_nominal | uso_educativo | uso_cientifico |
uso_comercial | derivados | redistribucion
```

Un CO con `access.level: publica` DEBE tener en su consentimiento los alcances `archivo` y `publicacion_abierta` como mínimo.

#### 4.4.5 `channel.type`

```
whatsapp | email | form_web | upload_direct | voice_phone |
field_app | api | paper_digitized
```

#### 4.4.6 `domain.primary`

Los seis dominios canónicos:

```
conservacion_ecologica |
gestion_del_area |
actividades_y_recreacion |
base_territorial_juridica |
comunidad_historia_patrimonio |
economia_territorial
```

#### 4.4.7 `layers.location.source`

```
manual | exif | gps_device | map_click | assumed | derived
```

#### 4.4.8 `layers.location.confidence`

```
alta | media | baja | desconocida
```

#### 4.4.9 `layers.scale.level`

```
parque | sector | predio | punto | corredor | region | cuenca
```

#### 4.4.10 `layers.temporality.refers_to`

```
actual | historico | periodico | puntual | continuo | prospectivo
```

#### 4.4.11 `layers.origin_layer.medium`

```
texto | voz | foto | video | mapa | tabla | sensor |
combinado | documento_escaneado
```

#### 4.4.12 `layers.actor.relates_to`

Lista (puede ser múltiple). Extensible por tesauro controlado gestionado por el órgano curatorial.

```
arriero | ganadero | escalador | investigador | guardaparque |
autoridad | comunidad_indigena | operador_turistico | vecino |
deportista | visitante | otro
```

#### 4.4.13 `layers.content_type`

```
dato | imagen | audio | video | texto | mapa | tabla |
historia_oral | cancion | receta | toponimo | observacion |
protocolo | norma | reporte | testimonio
```

#### 4.4.14 `layers.validation.level`

```
automatica | comunitaria | experta | institucional | sin_validar
```

#### 4.4.15 `access.level`

Armonizado con los tres niveles de CHH:

```
publica | interna | reservada
```

#### 4.4.16 `access.publication_scope`

```
world | community | curators_only | private
```

#### 4.4.17 `status`

Estados canónicos del pipeline:

```
received | triaged | enriched | in_review | curated |
validated | published | restricted | archived | rejected |
retracted | in_dispute
```

El estado `in_dispute` se especifica en `[05:*]`.

#### 4.4.18 `curation_track`

```
auto | light | deep
```

---

## 5. Canales

Los canales de ingesta admisibles se listan en el enum `channel.type`. Toda implementación DEBE soportar al menos un canal y DEBERÍA documentar cuáles soporta.

### 5.1 Requisitos por canal

#### 5.1.1 WhatsApp

Una implementación que soporte WhatsApp DEBE:
- Preservar el `wamid` original en `channel.reference`.
- Descargar y almacenar localmente todo archivo adjunto antes del procesamiento.
- Registrar la fecha de recepción del mensaje, no la fecha de procesamiento.
- Obtener consentimiento explícito mediante mensaje de confirmación al contribuyente antes de la primera publicación.

#### 5.1.2 Email

Una implementación que soporte email DEBE:
- Preservar el `Message-ID` en `channel.reference`.
- Almacenar el mensaje completo incluyendo headers.
- Tratar cada adjunto como una entrada independiente en `content.attachments`.

#### 5.1.3 Formulario web

Una implementación que soporte formulario web DEBE:
- Incluir campo explícito de consentimiento con alcances (`source.consent.scope`).
- Registrar hash del payload del formulario.
- Ofrecer el formulario en los idiomas usados por las comunidades objetivo.

#### 5.1.4 Carga directa

Una implementación que soporte carga directa DEBE:
- Requerir autenticación del contribuyente.
- Permitir carga batch (múltiples CO en una sola operación) con validación previa.

#### 5.1.5 Voz telefónica

Una implementación que soporte voz telefónica DEBERÍA:
- Transcribir automáticamente con herramienta auditable (ej. Whisper o equivalente).
- Conservar el audio crudo como `content.raw_ref`.
- Solicitar consentimiento verbal al inicio de la grabación.

#### 5.1.6 Field app

Una implementación que soporte captura de campo DEBE:
- Operar offline-first.
- Georreferenciar automáticamente con el GPS del dispositivo.
- Sincronizar al servidor central mediante cola persistente resistente a pérdida de conectividad.

### 5.2 Nuevos canales

Cualquier implementación PUEDE proponer canales adicionales. Un nuevo canal canónico en este estándar DEBE:

1. Declararse en un documento propio.
2. Especificar cómo se obtiene consentimiento en ese canal.
3. Especificar cómo se preserva el payload crudo.
4. Especificar el mapeo a `channel.type` y su referencia.

Los canales no canónicos se registran como `other` y requieren documentación anexa por implementación.

---

## 6. Provenance Chain

### 6.1 Propiedades invariantes

La Provenance Chain de un CO:

- **DEBE** ser append-only. Ningún evento registrado puede eliminarse ni modificarse.
- **DEBE** estar ordenada cronológicamente por el campo `at`.
- **DEBE** contener al menos un evento `received` como primer elemento.
- **DEBE** registrar todo cambio de estado (sección 4.4.17).
- **DEBE** registrar todo actor humano o sistémico que haya tocado el CO.
- **NO DEBE** contener eventos con fecha posterior al estado actual del CO en el repositorio.

### 6.2 Estructura de un evento

```yaml
provenance_event:
  event: enum                   # ver 6.3
  at: datetime                  # ISO-8601 con timezone
  actor: string                 # id del actor
  actor_type: enum              # human | system
  actor_role: string | null     # nivel curatorial si es humano (ver [02:*])
  note: string | null           # descripción breve
  payload_hash: string | null   # sha256 del estado del CO tras este evento
  signature: string | null      # firma criptográfica (v2+)
  refs:
    previous_event_index: integer | null
    affected_fields: [string]
    related_events: [string]    # ids de eventos en otros CO
```

### 6.3 Eventos canónicos

Los siguientes eventos son normativos. Una implementación conforme NO DEBE introducir eventos nuevos en el schema, pero PUEDE añadir información al campo `note`.

| Evento | Actor típico | Significado |
|---|---|---|
| `received` | sistema | entró al pipeline por un canal |
| `triaged` | sistema | clasificado automáticamente y asignado a track |
| `enriched` | sistema | metadatos derivados añadidos |
| `reviewed` | curador humano | abierto por curador por primera vez |
| `curated` | curador humano | revisado y listo para publicar |
| `validated` | curador humano | segunda revisión por par o superior |
| `published` | curador humano | publicado en su nivel de acceso |
| `restricted` | curador territorial | nivel de acceso reducido post-publicación |
| `declassified` | curador territorial | nivel de acceso ampliado |
| `forked` | curador humano | se creó un CO derivado |
| `merged` | curador humano | consolidado con otro CO |
| `corrected` | curador humano | corrección menor sin cambio de versión |
| `archived` | curador territorial | retirado de vista activa |
| `rejected` | curador humano | no apto; motivo obligatorio |
| `retracted` | Consejo Curatorial | retirado post-publicación; motivo obligatorio |
| `republished` | curador humano | vuelto a publicar tras retracción |
| `consent_revoked` | sistema o curador | contribuyente revocó consentimiento |
| `disputed` | sistema o curador | entró en proceso de disputa (`[05:*]`) |
| `dispute_resolved` | instancia de disputa | disputa cerrada con decisión |

### 6.4 Firma criptográfica

En v1.2 las firmas son **opcionales**. En v2.0 serán **obligatorias** para los eventos `curated`, `validated`, `published`, `restricted`, `retracted` y `dispute_resolved`.

---

## 7. Regla de residencia y cross-indexing

Cada CO tiene un **dominio de residencia canónica** (`domain.primary`) y PUEDE tener uno o más dominios de **indexación transversal** (`domain.cross_indexed`).

La regla de residencia canónica opera como sigue:

1. El CO reside físicamente en el dominio de `domain.primary`.
2. Los dominios listados en `domain.cross_indexed` generan referencias de búsqueda pero no duplican el contenido.
3. Las capas transversales (sección 4.5) son el mecanismo primario de conexión entre dominios. El cross-indexing es secundario.

Un CO **NO DEBE** tener más de un `domain.primary`. Un CO **PUEDE** tener múltiples `domain.cross_indexed`.

Esta regla reemplaza la formulación previa "un contenido vive en un dominio" y clarifica que la restricción es de persistencia, no de ontología: un contenido puede ser conceptualmente multitemático y estar transversalmente indexado como tal.

---

## 8. Extension Profiles

### 8.1 Propósito

El núcleo del CO cubre las propiedades comunes a todo conocimiento territorial. Ciertos dominios requieren campos especializados que no caben en el núcleo sin engrosarlo. Los Extension Profiles resuelven esto: añaden bloques opcionales bajo `contribution.extensions.<profile_id>` sin alterar la compatibilidad del núcleo.

### 8.2 Reglas para definir un Extension Profile

Un Extension Profile DEBE:

1. Declarar un `profile_id` único en formato `ext_<slug>` (ej. `ext_normative_instrument`).
2. Declarar su versión y estado (draft, stable, deprecated).
3. Declarar a qué `domain.primary` se asocia (uno o varios).
4. Especificar sus campos, sus tipos, sus enums y sus validaciones.
5. No introducir campos que duplican o contradicen el núcleo.
6. Publicarse como documento independiente `EXT_<NN>_<n>.md`.
7. Permanecer opcional: un CO **NUNCA** está obligado a usar un Extension Profile.

### 8.3 Perfiles canónicos previstos

El estándar reconoce los siguientes perfiles como canónicos (prioridad de desarrollo en este orden):

1. `ext_normative_instrument` — documentación jurídica, reglamentaria y normativa del área. **Desarrollado en EXT_01.**
2. `ext_scientific_contribution` — metodología, instrumentación, dataset, DOI, replicabilidad.
3. `ext_management_record` — registros operacionales del área, protocolos aplicados, alertas.
4. `ext_climbing_route` — vías de escalada, grado, equipamiento, estado, ética de apertura.
5. `ext_ranger_incident` — incidentes, evidencia, cadena de custodia, derivaciones.
6. `ext_research_expedition` — expediciones científicas, permisos, compromisos, outputs.
7. `ext_wildlife_observation` — observación de fauna, especie, comportamiento, condiciones.
8. `ext_visitor_flow` — registro de visitantes, check-in, ruta, tiempo, retorno.

### 8.4 Cómo se invoca un profile en un CO

```yaml
contribution:
  id: tkip-2026-0421-b8d2
  # ... resto del CO ...
  extensions:
    ext_normative_instrument:
      # campos definidos por EXT_01
      instrument_type: reglamento_interno
      issuing_authority: directorio_fcp
      hierarchy_level: 3
      in_force_from: 2026-01-15
      # ... etc
```

### 8.5 Validación

Un CO que usa uno o más Extension Profiles DEBE:

1. Validar correctamente contra el schema del núcleo.
2. Validar correctamente contra el schema de cada profile invocado.

La validación de un profile es independiente del núcleo.

---


## 9. Licenciamiento

### 9.1 Matriz de licenciamiento del contenido

El `licensing.license` de un CO DEBE ser uno de los siguientes, elegido conforme a la matriz:

| Tipo de contenido | Licencia por defecto | Alternativas admisibles |
|---|---|---|
| Historia oral comunitaria | CC-BY-NC-SA-4.0 | CC-BY-NC-4.0, licencia territorial propia |
| Instrumento normativo del área | Dominio público / CC0 | CC-BY-4.0 |
| Publicación científica del CO | CC-BY-4.0 | CC-BY-SA-4.0 |
| Dataset técnico u observacional | CC-BY-4.0 | ODbL, CC0 |
| Fotografía o audiovisual comunitario | CC-BY-NC-4.0 | CC-BY-NC-SA-4.0 |
| Protocolo o norma operativa interna | CC-BY-4.0 | uso restringido por `access.level` |
| Cartografía | CC-BY-SA-4.0 | ODbL |
| Software o implementación | MIT | Apache-2.0, GPL-3.0 |

Una implementación PUEDE añadir licencias territoriales propias siempre que declare compatibilidad con el consentimiento otorgado.

### 9.2 Licencia del documento vs. licencia del contenido

La licencia del documento del estándar (CC-BY-4.0, declarada en cada documento del set) NO determina la licencia del contenido ingestado. Cada CO lleva su propia licencia en `licensing.license`, coherente con el `source.consent.scope`.

### 9.3 Coherencia obligatoria

Para todo CO publicado, la siguiente coherencia DEBE cumplirse:

- Si `licensing.commercial_use = false`, entonces `source.consent.scope` NO DEBE incluir `uso_comercial`.
- Si `licensing.derivatives_allowed = false`, entonces `source.consent.scope` NO DEBE incluir `derivados`.
- Si `access.level = reservada`, entonces `licensing.license` PUEDE ser marcada como "uso restringido" y no requiere licencia Creative Commons estándar.

Una violación de esta coherencia DEBE producir rechazo del CO en etapa de curación.

---

## 10. Interoperabilidad

### 10.1 Formatos de serialización

El schema del CO DEBE ser serializable en YAML 1.2 y JSON. Una implementación DEBE ofrecer al menos una forma canónica de serialización.

### 10.2 Convenciones de identificadores

Todos los identificadores internos siguen el formato `tkip-<ámbito>-<slug>`:

- `tkip-YYYY-MMDD-<hash4>` para CO.
- `tkip-prov-<hash4>` para eventos de provenance (cuando se requiera id propio).
- `tkip-curator-<slug>` para identidades curatoriales.
- `tkip-territory-<slug>` para territorios adherentes.

El `<hash4>` es el primer cuadrante (4 caracteres hexadecimales) de un hash sha256 del payload completo al momento de la creación del objeto.

### 10.3 Exportación

Una implementación conforme DEBERÍA permitir exportar cualquier CO publicado como archivo YAML autocontenido que incluya: el CO completo, su Provenance Chain, referencias a attachments por hash, y un manifiesto de verificación.

### 10.4 Importación entre territorios

Un CO producido por una implementación TKIP PUEDE ser importado por otra implementación TKIP del mismo estándar. Al importar:

- El `id` original DEBE preservarse como `parent_id` si el territorio receptor reasigna id propio, o mantenerse si se mantiene la continuidad.
- La Provenance Chain original DEBE preservarse íntegra.
- Un nuevo evento `imported` DEBE añadirse con el id del territorio receptor.
- El consentimiento original DEBE seguir aplicando; un `source.consent.scope` que no incluya `redistribucion` impide la importación salvo autorización expresa del contribuyente original.

---

## 11. Versionado

### 11.1 Versionado del estándar

El estándar TKIP sigue versionado semántico `MAJOR.MINOR`:

- **MAJOR** cambia cuando hay cambios incompatibles con versiones anteriores (ruptura de schema, eliminación de enums, cambio de semántica de un campo).
- **MINOR** cambia cuando hay adiciones compatibles (nuevos campos opcionales, nuevos enums, nuevos Extension Profiles canónicos).

v1.2 es compatible hacia atrás con v1.1. v2.0 introducirá firmas criptográficas obligatorias en eventos críticos (sección 6.4), lo que constituye cambio MAJOR.

### 11.2 Versionado del CO

Cada CO lleva un campo `version: integer`. Se incrementa cuando:

- Se modifica un campo obligatorio del núcleo.
- Se corrige un error sustantivo de interpretación curatorial.
- Se añade o retira un Extension Profile.

Los cambios que no alteran la interpretación del CO (correcciones tipográficas, enriquecimientos puramente técnicos) **NO** incrementan `version` pero sí generan evento `enriched` o `corrected` en provenance.

### 11.3 Declaración de conformidad

Toda implementación DEBE declarar en su documentación pública:

1. La versión del estándar que implementa (ej. `TKIP v1.2`).
2. Qué canales soporta.
3. Qué Extension Profiles soporta.
4. Qué eventos de provenance firma (si alguno).
5. Desviaciones respecto del estándar, si las hay, debidamente justificadas.

---

## 12. Manejo de errores y casos límite

### 12.1 CO malformados

Un payload recibido que no puede convertirse en CO válido DEBE ser retenido en una cola de errores con:

- El payload crudo intacto.
- La causa del rechazo (campo faltante, enum no válido, error de parsing).
- Fecha de error.
- Curador notificado.

El payload **NO DEBE** descartarse automáticamente. Un curador humano decide si se puede recuperar, si se responde al emisor para corrección, o si se archiva definitivamente.

### 12.2 Consentimiento revocado

Cuando un contribuyente revoca su consentimiento:

1. Se registra evento `consent_revoked` en provenance.
2. Si el CO está en estado `published`, su `access.level` baja automáticamente a `reservada` y se registra evento `restricted`.
3. El Curador Territorial tiene **15 días** para decidir si el CO se retracta definitivamente o se mantiene en estado reservado.
4. El contribuyente recibe notificación por el canal original con la decisión.

El contenido ingestado **NO** se elimina del repositorio físico; se oculta del acceso público. La provenance de la revocación se conserva como parte del historial del CO.

### 12.3 Contribuyente fallecido

Si un contribuyente identificable fallece y no hay voluntad expresa dejada en vida:

- Los CO con `consent.level = atribuido` permanecen tal cual, en reconocimiento de la voluntad expresada en vida.
- El Consejo Curatorial PUEDE solicitar a la familia pronunciamiento sobre CO en estado `reservada`.
- Las sesiones futuras con personas de su círculo íntimo PUEDEN incorporar referencias a su legado siguiendo el cauce normal de curación.

### 12.4 Disputa sobre el contenido

Un CO en disputa entra al estado `in_dispute` y su tratamiento se rige por `[05:*]`. Durante la disputa:

- El CO **NO** se modifica (salvo por el propio proceso de disputa).
- El CO **NO** se retira automáticamente del acceso; la restricción es decisión del cauce de disputa que corresponda.
- Todo evento del proceso se registra en provenance con prefijo `dispute_*`.

### 12.5 Pérdida de infraestructura

En caso de pérdida parcial o total del repositorio físico, la reconstrucción DEBE basarse en:

1. El backup más reciente íntegro.
2. La Provenance Chain de cada CO como prueba de integridad.
3. Los payloads crudos preservados (sección 3.1).

Un CO cuya Provenance Chain no pueda verificarse post-recuperación DEBE marcarse como `in_review` hasta re-validación curatorial.

---

## 13. Conformidad

### 13.1 Declaración de conformidad

Una implementación se declara **TKIP v1.2 conforme** cuando:

1. Cumple todos los requisitos **DEBE** de este documento.
2. Cumple los requisitos **DEBE** del Governance Profile `[02:*]` en lo aplicable.
3. Cumple los controles obligatorios del Threat Model `[04:*]`.
4. Cumple el protocolo del Dispute Layer `[05:*]` en lo aplicable.
5. Documenta públicamente sus desviaciones y Extension Profiles activos.

### 13.2 Conformidad parcial

Una implementación que cumple el Core pero no el resto del conjunto se declara **TKIP Core v1.2 conforme**. Esta declaración es legítima pero insuficiente para operar un repositorio territorial completo; es adecuada, por ejemplo, para herramientas que solo generan o consumen CO pero no curan ni gobiernan.

### 13.3 Auditoría

El estándar no establece un organismo de certificación. La conformidad se declara de buena fe por la implementación. Cualquier tercero PUEDE auditar la conformidad revisando la documentación pública y un muestreo de CO publicados.

En v2.0, el Consejo de Estándar TKIP (aún no constituido) ofrecerá un proceso de conformidad revisada por pares.

---

*Fin del TKIP Core Standard v1.2.*
