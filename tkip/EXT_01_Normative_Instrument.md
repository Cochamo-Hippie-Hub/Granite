# TKIP Extension Profile — Normative Instrument

**Territorial Knowledge Ingestion Protocol — Extension Profile EXT_01**
*Perfil para documentación jurídica, reglamentaria y normativa de áreas protegidas*

Versión 1.2 — Stable
Abril 2026
Licencia del documento: CC-BY-4.0

Dominio asociado: `base_territorial_juridica` (principal); `gestion_del_area` (cross-indexing frecuente).

---

## Sobre este documento

Los Extension Profiles resuelven la tensión entre un núcleo de CO suficientemente compacto para toda forma de conocimiento territorial, y la necesidad de describir con rigor los tipos específicos de conocimiento que cada dominio produce.

Este Extension Profile aborda la documentación **normativa**: estatutos, reglamentos, convenios, servidumbres, declaratorias, ordenanzas, protocolos formales, actas de directorio, contratos relevantes, y todo instrumento escrito cuyo cumplimiento sea vinculante para la gestión del área protegida o para sus relaciones con terceros.

Este documento define el `profile_id = ext_normative_instrument` y constituye el primer perfil canónico desarrollado del estándar. Otros perfiles (`ext_scientific_contribution`, `ext_climbing_route`, etc.) seguirán su misma estructura.

---

## 1. Justificación del perfil

La gestión de un área protegida moderna es estructuralmente jurídica. Conservar un territorio no es solo un acto ecológico; es un acto normativo: alguien acuerda con alguien que un espacio debe preservarse de cierta manera, por cierto tiempo, con ciertos efectos frente a terceros. Todo lo que ocurre después —protocolos, presupuestos, autorizaciones— depende de esa matriz normativa.

Un repositorio territorial que no sepa indexar sus instrumentos normativos es un repositorio ciego a su propia columna vertebral. El núcleo del CO puede registrar que existe un "reglamento interno" en el dominio `base_territorial_juridica`, pero no puede decir **qué reglamento**, con **qué jerarquía**, **desde cuándo vigente**, **qué reemplazó**, **qué obligaciones genera**, ni **a quién vincula**. EXT_01 añade esos campos.

El valor práctico: un directorio, un donante, un auditor, un gestor o una autoridad puede consultar el repositorio y reconstruir, en un momento dado, el mapa normativo completo del área protegida, con trazabilidad de origen, vigencia, jerarquía y revisiones.

---

## 2. Alcance

Este perfil se aplica a todo CO cuyo contenido principal es un **instrumento normativo**. El criterio de inclusión es funcional, no formal: lo relevante es que el documento genere obligaciones, derechos o protocolos vinculantes para alguien dentro o fuera del área.

Quedan fuera del perfil:

- Informes técnicos sin efectos vinculantes (van al núcleo sin perfil).
- Publicaciones científicas (van a `ext_scientific_contribution` en el futuro).
- Correspondencia administrativa ordinaria (no es instrumento normativo).
- Presentaciones o materiales de difusión (aun si referencian normas).

Una implementación territorial PUEDE usar el perfil también para documentos de fuerza vinculante interna (compromisos con aliados, memorandos de entendimiento) aunque no tengan rango legal estricto, siempre que declare explícitamente el uso en `instrument_type: otro` con nota.

---

## 3. Esquema de campos del perfil

El bloque invocado bajo `contribution.extensions.ext_normative_instrument` contiene los siguientes campos:

```yaml
ext_normative_instrument:

  # ─── Identificación del instrumento ────────────────────────
  instrument_type: enum                      # ver 3.1
  instrument_title: string                   # título oficial
  instrument_short_title: string | null      # forma breve reconocible
  reference_number: string | null            # número oficial (rol, número de escritura, etc.)

  # ─── Autoridad emisora ─────────────────────────────────────
  issuing_authority:
    type: enum                               # ver 3.2
    name: string                             # nombre de la autoridad
    legal_personality: string | null         # personería jurídica (RUT / NIT / equivalente)
    role_within_area: enum | null            # ver 3.3

  # ─── Jerarquía normativa ───────────────────────────────────
  hierarchy:
    level: integer                           # 1 = máxima jerarquía; ver 3.4
    framework: string | null                 # marco normativo superior (ej. "Constitución", "Ley 19.253", "Estatutos FCP")
    supersedes_ids: [string]                 # ids de CO de instrumentos reemplazados
    amends_ids: [string]                     # ids de CO de instrumentos modificados (no reemplazados)
    implements_ids: [string]                 # ids de CO de instrumentos superiores que este concreta

  # ─── Vigencia temporal ─────────────────────────────────────
  temporal_effect:
    in_force_from: date                      # fecha desde la cual aplica
    in_force_until: date | null              # fecha de término si es temporal
    is_indefinite: boolean                   # true si no tiene fecha de término
    review_required_on: date | null          # fecha prevista de revisión obligatoria
    status: enum                             # ver 3.5

  # ─── Ámbito territorial y personal ─────────────────────────
  scope:
    territorial:
      applies_to_polygons: [string]          # ids de polígonos del catálogo geográfico
      applies_to_whole_area: boolean         # true si aplica a toda el área
      scope_description: string              # descripción en prosa
    personal:
      binds: [enum]                          # ver 3.6 — a quién obliga
      third_party_effects: boolean           # true si genera efectos frente a no-firmantes
      enumerated_parties: [string] | null    # nombres o roles de partes explícitamente vinculadas

  # ─── Objeto y contenido ────────────────────────────────────
  subject_matter: [enum]                     # ver 3.7 — qué regula
  obligations_summary: string                # resumen operativo de obligaciones (prosa)
  rights_summary: string | null              # resumen operativo de derechos (prosa)
  penalty_regime: string | null              # régimen sancionatorio si aplica

  # ─── Acto instrumental ─────────────────────────────────────
  instrument_act:
    act_type: enum                           # ver 3.8
    act_date: date                           # fecha del acto jurídico
    act_location: string | null              # lugar
    notary_or_officer: string | null         # notario, ministro de fe, etc.
    registration_details:
      registered: boolean
      registry: string | null                # Conservador de Bienes Raíces, Registro Civil, etc.
      folio: string | null
      number: string | null
      year: integer | null

  # ─── Custodia documental ───────────────────────────────────
  document_custody:
    original_location: string                # dónde está el original físico / digital firmado
    authenticated_copy_location: string | null
    digital_reference: string | null         # ruta al PDF/scan en el repositorio
    hash_sha256: string | null               # hash del archivo de referencia digital

  # ─── Revisión y vigilancia ─────────────────────────────────
  monitoring:
    responsible_curator: string              # id curatorial responsable del instrumento
    next_review_date: date | null
    compliance_tracking: enum                # ver 3.9
    associated_protocols: [string]           # ids de CO de protocolos derivados

  # ─── Notas curatoriales ────────────────────────────────────
  curator_annotations: string | null
  interpretative_disputes_open: [string]     # ids de disputas vigentes (ver [05:*])
```

---

## 3.1 Enum `instrument_type`

```
constitucion |
ley |
decreto |
reglamento_nacional |
ordenanza_municipal |
resolucion_administrativa |
concesion_estatal |
convenio_internacional |
tratado |
estatutos_corporacion |
estatutos_fundacion |
reglamento_interno |
pacto_accionistas_asociados |
acta_directorio |
escritura_publica |
contrato |
memorando_entendimiento |
servidumbre |
derecho_real_conservacion |
usufructo |
declaratoria |
protocolo_formal |
carta_legal |
sentencia_judicial |
laudo_arbitral |
acuerdo_comunitario |
otro
```

El enum es deliberadamente amplio porque los territorios enfrentan tipologías heterogéneas. `otro` **DEBE** acompañarse de `curator_annotations` con explicación del tipo usado.

## 3.2 Enum `issuing_authority.type`

```
estado_nacional |
estado_regional |
municipio |
directorio |
asamblea |
junta_vecinos |
notario |
tribunal |
consejo_curatorial |
parte_contratante |
comunidad |
otro
```

## 3.3 Enum `issuing_authority.role_within_area`

```
administrador |
propietario |
titular_derecho_real |
usuario_habilitado |
autoridad_supervisora |
tercero_con_interes_legitimo |
no_aplica
```

Este campo es **opcional**. Solo se completa cuando la autoridad emisora tiene rol reconocido dentro del área.

## 3.4 Jerarquía normativa

El campo `hierarchy.level` es un entero del 1 al 6 siguiendo la siguiente convención:

| Nivel | Tipo de instrumento característico |
|---|---|
| 1 | Constitución política, tratados ratificados con rango constitucional |
| 2 | Leyes generales aplicables, tratados internacionales vinculantes |
| 3 | Reglamentos, decretos supremos, concesiones estatales |
| 4 | Estatutos de personas jurídicas vinculadas al área, escrituras constitutivas |
| 5 | Reglamentos internos, protocolos formales, actas vinculantes |
| 6 | Contratos bilaterales, memorandos de entendimiento, compromisos acotados |

La jerarquía no es una ordenación de importancia práctica sino de prevalencia jurídica en caso de conflicto de aplicación. Un nivel 6 frecuentemente es más operacionalmente relevante que un nivel 1, pero en conflicto formal de aplicación prevalece el nivel 1.

Un curador temático con competencia jurídica DEBE validar este campo en track `deep`.

## 3.5 Enum `temporal_effect.status`

```
vigente |
suspendido |
derogado |
caduco |
en_tramitacion |
pendiente_de_publicacion |
interpretacion_en_disputa
```

Un instrumento `derogado` o `caduco` NO se elimina del repositorio; se mantiene con su status correspondiente. Su historicidad es parte del patrimonio normativo.

## 3.6 Enum `scope.personal.binds`

```
estado |
area_protegida_administradora |
directorio |
titulares_prediales |
operadores_comerciales |
arrieros |
escaladores |
visitantes |
comunidad_local |
investigadores |
personal_area |
terceros_enumerados |
erga_omnes
```

Un instrumento PUEDE vincular múltiples categorías simultáneamente. `erga_omnes` indica vinculación frente a todos.

## 3.7 Enum `subject_matter`

Lista (múltiple). Enumera las materias reguladas.

```
administracion_del_area |
uso_publico |
acceso |
infraestructura |
conservacion_especies |
manejo_fuego |
manejo_agua |
manejo_residuos |
actividades_comerciales |
escalada |
senderismo |
ganaderia |
turismo_cientifico |
investigacion |
filmacion_fotografia |
construccion |
servidumbres_de_paso |
derechos_de_conservacion |
gobernanza_institucional |
relaciones_con_comunidad |
relaciones_con_autoridad |
seguridad_rescate |
presupuesto_financiamiento |
responsabilidad_civil |
propiedad_intelectual |
datos_y_privacidad |
otro
```

## 3.8 Enum `instrument_act.act_type`

```
promulgacion |
publicacion_oficial |
firma |
aprobacion_asamblea |
aprobacion_directorio |
celebracion_convenio |
otorgamiento_escritura |
inscripcion |
notificacion |
dictado_sentencia |
resolucion_arbitral |
aprobacion_comunitaria
```

## 3.9 Enum `monitoring.compliance_tracking`

```
no_requiere |
anual |
semestral |
trimestral |
por_hito |
continuo |
externo
```

`externo` indica que el cumplimiento es verificado por una autoridad o tercero fuera del sistema curatorial del territorio.

---

## 4. Validaciones normativas del perfil

Las siguientes validaciones son normativas para el perfil. Un CO que las viole **NO DEBE** publicarse.

### 4.1 Coherencia temporal

Si `temporal_effect.status = vigente`, entonces `temporal_effect.in_force_from` DEBE ser anterior o igual a la fecha actual, y `temporal_effect.in_force_until` (si existe) DEBE ser posterior a la fecha actual.

Si `temporal_effect.status = derogado` o `caduco`, los CO que lo reemplazan DEBEN existir en el repositorio referenciados en `hierarchy.supersedes_ids` del nuevo instrumento.

### 4.2 Coherencia jerárquica

Un instrumento de nivel `n` **NO DEBE** invocarse como `implements_ids` de un instrumento de nivel `n+k` (con k > 0). Es decir, un reglamento interno no implementa un contrato bilateral.

Un instrumento **NO DEBE** estar simultáneamente en `supersedes_ids` y `amends_ids` del mismo instrumento.

### 4.3 Coherencia de scope

Si `scope.personal.third_party_effects = true`, el curador temático DEBE validar explícitamente el tipo de efecto en `curator_annotations`.

Si `scope.territorial.applies_to_whole_area = true`, entonces `applies_to_polygons` PUEDE estar vacío; si es `false`, DEBE contener al menos un polígono.

### 4.4 Custodia documental

Todo CO con este perfil DEBE declarar `document_custody.original_location`. No se publica un instrumento normativo sin saber dónde vive el original.

El `digital_reference` es **obligatorio** para `access.level = publica`: los instrumentos normativos publicados requieren acceso al texto digitalizado del documento.

### 4.5 Validación curatorial

Todo CO con este perfil requiere firma de **Curador Temático** con competencia en `base_territorial_juridica` o de **Curador Territorial** con asesoría temática registrada. La firma exclusiva de un Curador Comunitario **NO es suficiente**.

---

## 5. Ejemplo completo

*Ejemplo informativo; no forma parte normativa.*

```yaml
contribution:
  id: tkip-2026-0421-a4f1
  version: 1
  source:
    contributor_id: tkip-curator-andres-amengual
    contributor_role: asesor_legal
    consent:
      level: atribuido
      obtained_at: 2026-04-21T10:00:00-04:00
      obtained_by: tkip-curator-territorial-cochamo
      method: implicit_by_submission
      scope: [archivo, publicacion_abierta, uso_educativo]
      revocable: false
  channel:
    type: upload_direct
    received_at: 2026-04-21T10:00:00-04:00
  domain:
    primary: base_territorial_juridica
    cross_indexed: [gestion_del_area]
  layers:
    location:
      place_name: "Pucheguín — sector sur"
      source: manual
      confidence: alta
    scale:
      level: parque
    temporality:
      refers_to: continuo
      reference_date: 2026-01-15
    content_type: norma
    validation:
      level: experta
      validated_by: [tkip-curator-andres-amengual]
  content:
    preview: "Reglamento Interno de Uso Público del sector sur del área protegida, aprobado por Directorio FCP el 15 de enero de 2026."
    language: es-CL
  access:
    level: publica
    publication_scope: world
    review_required_every: P2Y
  status: published
  curation_track: deep
  provenance:
    - event: received
      at: 2026-04-21T10:00:00-04:00
      actor: tkip-system
      actor_type: system
    - event: curated
      at: 2026-04-21T15:00:00-04:00
      actor: tkip-curator-andres-amengual
      actor_type: human
      actor_role: curador_tematico
    - event: published
      at: 2026-04-21T17:00:00-04:00
      actor: tkip-curator-territorial-cochamo
      actor_type: human
      actor_role: curador_territorial
  licensing:
    license: CC-BY-4.0
    attribution_required: true
    commercial_use: true
    derivatives_allowed: true
    share_alike: false
  extensions:
    ext_normative_instrument:
      instrument_type: reglamento_interno
      instrument_title: "Reglamento Interno de Uso Público, Sector Sur"
      instrument_short_title: "RIUP-Sur 2026"
      reference_number: "FCP-REG-2026-001"
      issuing_authority:
        type: directorio
        name: "Directorio Fundación Conserva Pucheguín"
        legal_personality: "[RUT de la fundación]"
        role_within_area: administrador
      hierarchy:
        level: 5
        framework: "Estatutos FCP (2025)"
        supersedes_ids: []
        amends_ids: []
        implements_ids: ["tkip-2025-0612-c1d9"]  # escritura convenio administración
      temporal_effect:
        in_force_from: 2026-01-15
        is_indefinite: true
        review_required_on: 2028-01-15
        status: vigente
      scope:
        territorial:
          applies_to_whole_area: false
          applies_to_polygons: ["pgn-cochamo-sur-01"]
          scope_description: "Sector sur del área protegida, desde río X hasta límite predial Y."
        personal:
          binds: [area_protegida_administradora, visitantes, operadores_comerciales, arrieros]
          third_party_effects: true
      subject_matter:
        - uso_publico
        - acceso
        - escalada
        - senderismo
        - seguridad_rescate
      obligations_summary: "Regula horarios de ingreso, capacidad máxima, conductas permitidas, obligaciones de operadores, protocolos de emergencia y uso del centro de visitantes."
      rights_summary: "Establece derechos de acceso público regulado para actividades recreativas compatibles con la conservación."
      penalty_regime: "Régimen de advertencia, suspensión temporal y suspensión definitiva de acceso según gravedad."
      instrument_act:
        act_type: aprobacion_directorio
        act_date: 2026-01-15
        act_location: "Puerto Varas, Chile"
      document_custody:
        original_location: "Archivo Fundación Conserva Pucheguín — carpeta normativa"
        digital_reference: "granite://base_territorial_juridica/reglamentos/riup-sur-2026.pdf"
        hash_sha256: "sha256:abc123..."
      monitoring:
        responsible_curator: tkip-curator-andres-amengual
        next_review_date: 2028-01-15
        compliance_tracking: anual
        associated_protocols: []
      curator_annotations: "Primer reglamento interno del área protegida tras la constitución formal de FCP. Establece la base normativa operativa para los protocolos sectoriales que le sigan."
      interpretative_disputes_open: []
```

---

## 6. Casos de uso del perfil

### 6.1 Consulta de vigencia

Un gestor consulta "¿qué reglas operativas aplican hoy en el sector sur del parque?" y el sistema devuelve todos los CO con `ext_normative_instrument` donde:
- `scope.territorial.applies_to_polygons` incluye el polígono del sector sur **o** `applies_to_whole_area = true`.
- `temporal_effect.status = vigente`.
- `access.level != reservada` según permisos del consultante.

El resultado es un mapa normativo actual, legible y completo.

### 6.2 Trazabilidad de reemplazos

Cuando se aprueba un nuevo reglamento, el curador temático enlaza via `hierarchy.supersedes_ids` al reglamento anterior. El anterior pasa a `status: derogado` automáticamente tras validación. La cadena completa de reglamentos queda reconstruible.

### 6.3 Detección de lagunas

Un auditor puede detectar lagunas normativas consultando subject_matters que no tienen instrumentos vigentes. Por ejemplo: si ningún CO vigente con `subject_matter: filmacion_fotografia` existe, el área carece de regulación explícita sobre ese tema.

### 6.4 Fundraising y auditoría externa

Un donante o auditor externo puede solicitar el "mapa normativo del área" y recibir un informe automático generado desde los CO con este perfil: qué instrumentos rigen, de qué jerarquía, desde cuándo, con qué obligaciones, con qué custodia documental. Esta capacidad convierte al repositorio en una herramienta de gobernanza demostrable.

### 6.5 Interoperabilidad con CirculoTerritorial

Los CO con este perfil son la **base normativa** sobre la que el repositorio privado de gestión (`CirculoTerritorial`) documenta su operación: cada protocolo, cada decisión de directorio, cada auditoría referencia al CO del instrumento normativo aplicable via `associated_protocols` y cross-references estándar del núcleo.

---

## 7. Relación con otros perfiles

### 7.1 `ext_scientific_contribution` (futuro)

Una investigación regida por un permiso de investigación (un instrumento normativo en sí) genera tanto un CO con `ext_normative_instrument` (el permiso) como CO con `ext_scientific_contribution` (los resultados), enlazados entre sí.

### 7.2 `ext_management_record` (futuro)

Los registros operacionales implementan protocolos que a su vez derivan de instrumentos normativos. Un registro DEBE referenciar al menos un CO con `ext_normative_instrument` que lo sustente normativamente.

### 7.3 `ext_climbing_route` (futuro)

Las vías de escalada operan dentro del marco normativo del área. Un CO de vía referencia al reglamento que rige la escalada en su sector.

En todos los casos, `ext_normative_instrument` funciona como **capa fundacional** de derechos, obligaciones y autorizaciones sobre la que otros perfiles se apoyan.

---

## 8. Notas de implementación

### 8.1 Importación retrospectiva

Un territorio que adopta TKIP después de años de operación normativa DEBE considerar la importación retrospectiva de sus instrumentos vigentes como proyecto inicial. La operación es:

1. Inventario completo de instrumentos.
2. Digitalización si no existen escaneados.
3. Ingesta como CO con este perfil.
4. Validación curatorial temática.
5. Establecimiento de relaciones jerárquicas y de reemplazo.

Este proyecto es habitualmente **Fase 2** del piloto (mes 3-6).

### 8.2 Acoplamiento con registros externos

Cuando el instrumento está inscrito en un registro público externo (Conservador de Bienes Raíces, Registro Civil, registro ambiental), el campo `instrument_act.registration_details` lo documenta. El CO NO reemplaza al registro externo; lo referencia.

### 8.3 Interpretaciones curatoriales

El campo `curator_annotations` es el lugar donde el curador temático puede dejar interpretaciones útiles sobre el instrumento (contexto de adopción, aplicaciones concretas frecuentes, advertencias de lectura). Estas anotaciones son parte del valor curatorial añadido y **NO** sustituyen al texto normativo.

Si la interpretación es disputada, el campo `interpretative_disputes_open` se poblará con los ids del expediente del Dispute Layer `[05:*]` hasta que la disputa se resuelva.

---

## 9. Revisión del perfil

Este perfil es **stable** en v1.2. Se revisará cuando alguno de los siguientes eventos ocurra:

- Primera implementación piloto complete fase 2 (importación retrospectiva) y aporte lecciones.
- Un territorio de jurisdicción distinta a la chilena adopte el estándar y requiera extensiones.
- El Consejo de Estándar (v2) decida ampliar el enum `instrument_type` o `subject_matter`.

Las revisiones se documentan públicamente. Versiones mayores del perfil son compatibles con versiones anteriores del núcleo.

---

*Fin del TKIP Extension Profile EXT_01 — Normative Instrument v1.2.*
