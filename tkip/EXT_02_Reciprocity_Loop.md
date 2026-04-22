# TKIP Extension Profile — Reciprocity Loop

**Territorial Knowledge Ingestion Protocol — Extension Profile EXT_02**
*Perfil para restitución informada al contribuyente individual*

Versión 1.2 — Draft
Abril 2026
Licencia del documento: CC-BY-4.0

Dominio asociado: ninguno específico (transversal a los seis dominios).

---

## Sobre este documento

Los Extension Profiles añaden campos opcionales al Contribution Object para cubrir necesidades que el núcleo no resuelve sin engrosarse. Este perfil aborda un ámbito que la Cultural Charter `[03:2.3]` declara como axioma (Reciprocidad informacional) y que el Principio de Devolución `[03:3.2]` enmarca, pero que el Core Standard `[01:*]` no operacionaliza: **cómo un CO registra de qué manera concreta se cierra el ciclo de retribución al contribuyente individual que lo aportó**.

Este documento define el `profile_id = ext_reciprocity_loop`. Es opcional. Un territorio PUEDE adoptar TKIP sin activar este perfil y seguir siendo conforme. Un territorio que lo adopta asume el compromiso operativo de devolver algo al contribuyente por cada CO relevante que entra al repositorio.

---

## 1. Justificación del perfil

La reciprocidad informacional es un axioma de TKIP (Charter `[03:2.3]`). El axioma afirma: *toda persona que alimenta el sistema recibe algo útil a cambio*. El Principio de Devolución `[03:3.2]` desarrolla este axioma en clave cualitativa, rechaza el reconocimiento métrico, e introduce la metáfora del arbolito de navidad comunitario: cada contribución deja huella visible-pero-no-estridente en un conjunto que pertenece al territorio, no a quien aportó.

Sin un perfil que lo operacionalice, el axioma corre dos riesgos. Primero, el riesgo del gesto simbólico vacío: un acuse genérico ("gracias por tu contribución") que cumple la letra del principio sin cumplir su espíritu. Segundo, el riesgo opuesto: la burocratización de la devolución, con rankings, métricas, gamificación y todas las patologías que el Principio 3.2 rechaza explícitamente.

Este perfil resuelve ambos riesgos codificando cuatro mecanismos concretos, proporcionales y cualitativos: **certificado vivo de contribución**, **eco de uso**, **linaje de conocimiento**, y **opt-out del ciclo de restitución**. Estos mecanismos son deliberadamente específicos: cada uno cierra un momento distinto del ciclo de vida de un aporte y cada uno se registra como metadato auditable del CO.

## 2. Principios de diseño del perfil

Los siguientes principios son invariantes del perfil y se derivan directamente del Principio de Devolución de la Charter:

1. **Reconocimiento cualitativo, nunca métrico.** El perfil NO DEBE usarse para producir rankings, ordenamientos comparables entre contribuyentes, ni indicadores públicos de "top contribuidores". Un territorio que use este perfil para gamificar contribuciones ha violado el principio fundante.
2. **Materialidad plural.** La devolución PUEDE ser digital, impresa, oral o presencial. El perfil registra la devolución sin privilegiar un medio sobre otro.
3. **Canal simétrico.** La devolución se entrega por defecto por el mismo canal por el que ingresó el CO, salvo que el contribuyente haya declarado un canal de retorno distinto.
4. **Consentimiento de participación.** El contribuyente PUEDE optar por no recibir devoluciones (`opt_out`). El sistema respeta la decisión sin excluir al contribuyente de los demás derechos del estándar.
5. **Discreción por defecto.** Las devoluciones son gestos entre el sistema y el contribuyente. No se publican ni exhiben en paneles públicos.

---

## 3. Campos del perfil

Un CO que activa este perfil añade bajo `contribution.extensions.ext_reciprocity_loop` el siguiente bloque:

```yaml
ext_reciprocity_loop:

  # ─── Participación del contribuyente en el ciclo ────────────
  opt_out: boolean                     # si true, no se envían devoluciones
  opt_out_reason: string | null        # opcional, libre

  # ─── Canal de retorno ──────────────────────────────────────
  return_channel: enum                 # ver 4.1 (por defecto = channel.type)
  return_channel_reference: string | null

  # ─── Certificado vivo de contribución ──────────────────────
  certificate:
    delivered_at: datetime | null
    delivery_channel: enum | null      # ver 4.1
    payload_ref: string | null         # ruta al certificado generado
    generator: enum | null             # ver 4.2
    reviewed_by: string | null         # id del anfitrión/curador que validó

  # ─── Eco de uso ────────────────────────────────────────────
  usage_echoes:
    - at: datetime
      kind: enum                       # ver 4.3
      reference: string                # id del objeto que consultó o usó este CO
      note: string | null
      delivered_to_contributor_at: datetime | null

  # ─── Linaje de conocimiento ────────────────────────────────
  lineage_links:
    - related_contribution_id: string  # id del otro CO con el que linajó
      link_type: enum                  # ver 4.4
      at: datetime
      note: string | null
      delivered_to_contributor_at: datetime | null

  # ─── Ritualización colectiva (agregación anual) ────────────
  included_in_annual_compilation: [string]   # ids de compilaciones anuales
                                             # donde apareció este CO
```

Todos los subcampos son opcionales en términos de schema. Un CO PUEDE activar el perfil solo con `opt_out: false` para declarar su participación en el ciclo, y el resto de campos se irán poblando a medida que ocurran los eventos correspondientes.

---

## 4. Enums del perfil

### 4.1 `return_channel` y `delivery_channel`

```
whatsapp | email | voz_telefonica | presencial |
correo_fisico | radio_comunitaria | cartelera_publica |
compilacion_impresa_anual | ninguno
```

El valor `ninguno` es válido solo si `opt_out: true`.

### 4.2 `certificate.generator`

```
ai_assisted | human_authored | hybrid
```

- `ai_assisted`: generado por IA del repositorio con revisión humana antes del envío.
- `human_authored`: redactado íntegramente por un humano (típicamente el anfitrión territorial o un curador comunitario).
- `hybrid`: borrador por IA, reelaborado sustancialmente por humano antes del envío.

### 4.3 `usage_echoes.kind`

```
consulta_publica | consulta_curatorial | decision_gestion |
publicacion_derivada | cita_externa | compilacion_ritual |
otro
```

### 4.4 `lineage_links.link_type`

```
enriquecimiento_mutuo | corroboracion | complemento |
contraste_respetuoso | correccion | continuidad_temporal
```

`contraste_respetuoso` se usa cuando dos CO presentan versiones distintas de un mismo hecho o topónimo sin que haya disputa formal abierta. Si la divergencia escala, se tramita por el Dispute Layer `[05:*]`.

---

## 5. Ciclo operativo

### 5.1 Momento de activación

Una implementación que soporta este perfil DEBERÍA ofrecer al contribuyente, al momento de obtener consentimiento, la opción de participar o no participar del ciclo de restitución. La opción se registra como `opt_out` en el CO.

### 5.2 Certificado vivo de contribución

Cuando un CO alcanza estado `published`, la implementación DEBERÍA generar un certificado vivo dirigido al contribuyente, salvo que `opt_out: true`. El certificado contiene, como mínimo:

- Referencia específica al contenido aportado.
- Ubicación del CO en el repositorio (dominio, sector, enlace si aplica).
- Menciones a CO relacionados (si ya existen linajes).
- Fecha y canal de entrega.

El certificado NO es un PDF formal ni un recibo; es una pieza breve, legible y cercana al canal de retorno. Su registro en el CO cumple función de auditoría, no de exhibición pública.

### 5.3 Eco de uso

Cuando un CO es consultado, citado o usado en una decisión curatorial o de gestión, el sistema DEBERÍA registrar un evento en `usage_echoes`. La notificación al contribuyente NO es inmediata: se agrupa y se envía con frecuencia máxima **una vez al mes** por contribuyente, para evitar convertir la restitución en ruido de notificaciones.

El contenido del eco es narrativo, no estadístico. No se entregan conteos ("tu aporte fue consultado 43 veces") sino sucesos específicos ("tu reporte del vado del río fue consultado esta semana al planificar un cierre temporal de sendero").

### 5.4 Linaje de conocimiento

Cuando un curador establece que dos CO de contribuyentes distintos se enriquecen mutuamente, se registra la relación en `lineage_links` de ambos CO. Ambos contribuyentes reciben notificación específica del linaje, respetando el consentimiento de visibilidad cruzada (un contribuyente anónimo PUEDE ser referido solo de forma genérica al otro).

### 5.5 Ritualización colectiva

Las implementaciones que producen compilaciones anuales impresas (modelo Cochamó) DEBERÍAN registrar en `included_in_annual_compilation` los identificadores de los ejemplares donde el CO apareció. Esto preserva trazabilidad sin producir métricas comparables.

---

## 6. Articulación con otros documentos del estándar

### 6.1 Con el Core `[01:*]`

- La Provenance Chain registra el momento en que el ciclo de restitución afecta al CO. Los eventos `dialog_opened` y `dialog_closed` (Core `[01:6.3]`) pertenecen al diálogo pre-ingesta, son distintos de la restitución y son independientes de este perfil.
- El `source.consent.scope` debe permitir al menos `archivo` para que el contribuyente pueda recibir certificado vivo (la devolución referencia contenido archivado).
- El `channel.type` de origen determina el `return_channel` por defecto, pero el contribuyente PUEDE sobrescribirlo al momento del consentimiento.

### 6.2 Con el Governance Profile `[02:*]`

- El rol de **facilitador** (Core `[01:6.3]`, eventos de diálogo) y de **validador del certificado** (campo `certificate.reviewed_by` de este perfil) PUEDE recaer en Curadores Comunitarios o Curadores Aprendices bajo mentoría, siempre que la responsabilidad sea individual y firmada.
- La producción de la compilación anual impresa es competencia del Consejo Curatorial o del Comité de Arranque en territorios en fase piloto.

### 6.3 Con el Threat Model `[04:*]`

- Este perfil introduce un vector de ataque potencial: si un actor hostil genera contribuciones masivas para recibir devoluciones o para mapear la red de contribuyentes a través de los linajes. Las implementaciones DEBEN monitorear patrones anómalos de activación del perfil y suspender el ciclo de restitución si se detecta abuso.
- Los `lineage_links` NO DEBEN revelar identidades de contribuyentes con `source.consent.level: anonimo` ni `reservado` (ver Control T7 del Threat Model).

### 6.4 Con el Dispute Layer `[05:*]`

- Un contribuyente PUEDE disputar un certificado vivo específico si considera que tergiversa su aporte. Cauce preferente: A (diálogo directo facilitado).
- La revocación de consentimiento (Core `[01:12.2]`) dispara automáticamente `opt_out: true` en este perfil y detiene futuras devoluciones, sin borrar las ya registradas en provenance.

---

## 7. Ejemplo de invocación

```yaml
contribution:
  id: tkip-2026-0421-c4f9
  # ... núcleo del CO ...
  source:
    contributor_id: anon-wa-82a3
    contributor_role: [vecino, arriero]
    consent:
      level: atribuido
      scope: [archivo, publicacion_comunitaria, atribucion_nominal]
  channel:
    type: whatsapp
  # ... resto del CO ...
  extensions:
    ext_reciprocity_loop:
      opt_out: false
      return_channel: whatsapp
      certificate:
        delivered_at: 2026-04-23T14:12:00-04:00
        delivery_channel: whatsapp
        payload_ref: certs/tkip-2026-0421-c4f9-cert.md
        generator: ai_assisted
        reviewed_by: tkip-curator-anfitrion-cochamo
      usage_echoes:
        - at: 2026-05-14T09:30:00-04:00
          kind: decision_gestion
          reference: tkip-dispute-2026-006
          note: "El aporte informó el cierre temporal del sendero norte por nidificación."
          delivered_to_contributor_at: 2026-05-31T10:00:00-04:00
      lineage_links:
        - related_contribution_id: tkip-2026-0315-3b71
          link_type: enriquecimiento_mutuo
          at: 2026-05-02T16:45:00-04:00
          delivered_to_contributor_at: 2026-05-31T10:00:00-04:00
      included_in_annual_compilation: []
```

---

## 8. Disposiciones finales

### 8.1 Adopción opcional

Este perfil es opcional. Una implementación TKIP PUEDE declararse conforme al Core sin activar este perfil. La activación se declara territorialmente, idealmente en el Pilot Profile o en su equivalente de régimen permanente.

### 8.2 Condición mínima de activación responsable

Un territorio que active este perfil DEBE poder sostener operativamente el ciclo completo: generación de certificados, eco mensual de usos, registro de linajes, y (si corresponde) compilación ritualizada. Activar el perfil sin capacidad operativa es peor que no activarlo: produce expectativa incumplida.

El Consejo Curatorial —o el Comité de Arranque en fase piloto— evalúa la capacidad antes de activar.

### 8.3 Revisión del perfil

Este perfil está en estado **draft** hasta que una implementación territorial haya operado el ciclo completo durante al menos 6 meses. Tras esa experiencia, el perfil se revisa con los aprendizajes observados y pasa a estado **stable** si supera la revisión.

### 8.4 Relación con la Charter

Todo lo aquí operacionalizado encuentra su fundamento doctrinario en el Axioma III `[03:2.3]` y en el Principio de Devolución `[03:3.2]`. Si alguna disposición de este perfil entra en conflicto aparente con la Charter, la Charter prevalece.

---

*Fin del TKIP Extension Profile EXT_02 — Reciprocity Loop v1.2 (draft).*
