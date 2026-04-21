# TKIP Pilot Profile — Cochamó

**Perfil de Piloto para el Territorio de Cochamó**
Versión 1.2 — Draft
Abril 2026
Licencia del documento: CC-BY-4.0

---

## Sobre este documento

Este documento es el **perfil piloto** de TKIP para Cochamó. Define el subconjunto operativo mínimo con el que iniciar el protocolo en terreno, sin esperar madurez completa del estándar.

Es deliberadamente austero. No reproduce el Core Standard ni la Governance Profile; los referencia y recorta. Toda ambigüedad de este documento se resuelve consultando los documentos superiores.

El objetivo del piloto es **probar que TKIP funciona en un territorio real** dentro de un plazo de 12 meses, con el menor aparato posible.

Este documento está en estado **draft** y está sujeto a ajuste durante la ejecución. Los cambios se documentan en una bitácora pública del piloto.

---

## 1. Alcance del piloto

**Territorio**: comuna de Cochamó, Región de Los Lagos, Chile.
**Duración**: 12 meses desde activación.
**Meta cuantitativa**: 100 CO publicados, 10 curadores acreditados, 0 incidentes críticos irresueltos.
**Meta cualitativa**: al cierre del piloto, al menos 3 familias, 3 operadores y 2 instituciones reconocen el repositorio como útil para su actividad.

---

## 2. Recortes al estándar durante el piloto

Para no sobrediseñar, el piloto opera con las siguientes restricciones:

### 2.1 Canales activos

Solo dos canales durante el piloto:

- **WhatsApp** (canal primario para comunidad local y Cronistas).
- **Formulario web** (canal para investigadores, visitantes, operadores técnicos).

Los canales `email`, `voice_phone`, `upload_direct`, `field_app` y `paper_digitized` quedan fuera del piloto. Pueden activarse en fase 2.

### 2.2 Niveles curatoriales activos

Solo tres niveles durante el piloto:

- Curador Aprendiz (para primeros Cronistas del Valle).
- Curador Comunitario (al menos 3 personas acreditadas).
- Curador Territorial (1 persona responsable).

Los niveles Temático y Consejo Curatorial se constituyen en fase 2. Durante el piloto, las funciones del Consejo son ejercidas por un **Comité de Arranque** de 3 personas que incluye al Curador Territorial, un referente CPP y un referente FCP, con carácter transitorio.

### 2.3 Extension profiles activos

Solo un perfil durante el piloto:

- `ext_normative_instrument` (EXT_01), para comenzar a estructurar el sistema normativo del área protegida desde el inicio.

Otros perfiles se activan por prioridad según demanda: `ext_scientific_contribution` probablemente en mes 6, `ext_climbing_route` probablemente en mes 9.

### 2.4 Dominios activos

Los seis dominios del Core quedan habilitados, pero con énfasis desigual durante el piloto:

| Dominio | Énfasis en piloto |
|---|---|
| `comunidad_historia_patrimonio` | Alto (activación prioritaria via Cronistas) |
| `base_territorial_juridica` | Alto (via EXT_01) |
| `conservacion_ecologica` | Medio |
| `gestion_del_area` | Medio |
| `actividades_y_recreacion` | Bajo-Medio (se incorpora desde mes 6) |
| `economia_territorial` | Bajo |

### 2.5 Tracks de curación

Los tres tracks (auto, light, deep) se mantienen pero con proporciones ajustadas al arranque:

- En los primeros 3 meses, prácticamente todo entra por **light** o **deep**. El track auto se activa cuando hay masa crítica de CO aprobados que permita identificar patrones repetitivos confiables.
- El piloto **NO** automatiza publicación por `auto` durante los primeros 6 meses aunque el sistema sugiera el track; todo pasa por curador humano explícito.

### 2.6 Dispute Layer reducido

Durante el piloto, solo se operan los cauces A y C del Dispute Layer `[05:4]`:

- **Cauce A** (diálogo directo con facilitación) para la mayoría de casos.
- **Cauce C** (Comité de Arranque en lugar de Consejo) para casos mayores.
- El **Cauce B** (panel curatorial ad hoc) se activa solo si surge un caso que ninguno de los otros cauces pueda absorber.

---

## 3. Schema mínimo del CO en piloto

Durante el piloto, el CO usa el schema del Core `[01:4.3]` con las siguientes simplificaciones:

### 3.1 Campos obligatorios del piloto

Son exactamente los del Core mínimo `[01:4.2]`, once campos:

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

### 3.2 Campos recomendados pero no obligatorios

- `source.contributor_display` si el consentimiento es `atribuido`.
- `layers.location.place_name` siempre que se conozca.
- `layers.temporality.refers_to` siempre que aplique.
- `licensing.license` con valor por defecto asignado según la matriz del Core `[01:9.1]`.

### 3.3 Campos diferidos (no usar en piloto)

- `extensions.*` distintos de `ext_normative_instrument`.
- `provenance.*.signature` (firmas criptográficas; diferido a v2).
- `references.external_sources` con DOI/ISBN (no crítico en piloto).

---

## 4. Flujo de aprobación del piloto

El flujo operativo del piloto es este:

```
1. Contribuyente envía por WhatsApp o Formulario.
2. Bot/backend genera CO base con campos mínimos y
   evento provenance.received.
3. Triage automático asigna track (por defecto light).
4. Curador Comunitario o Aprendiz abre el CO en cola
   y registra evento provenance.reviewed.
5. Curador revisa, enriquece metadatos, aplica tesauro,
   registra evento provenance.curated.
6. Segundo curador (Comunitario o Territorial) valida 
   si corresponde (track deep) y registra 
   provenance.validated.
7. Curador Territorial (o autorizado) publica:
   evento provenance.published.
8. Devolución al contribuyente por canal original.
9. CO queda disponible en el nivel de acceso definido.
```

El flujo completo para track light debería resolverse en **72 horas máximo** desde recepción. Track deep puede tomar hasta 2 semanas.

---

## 5. Roles y personas durante el piloto

| Rol | Nº personas | Perfil |
|---|---|---|
| Curador Territorial | 1 | figura con dedicación de 20-30% FTE, conocimiento territorial, habilidad relacional |
| Curador Comunitario | 3-5 | vecinos, operadores u organizaciones con legitimidad local y disponibilidad regular |
| Curador Aprendiz | 5-10 | primeros Cronistas del Valle activos |
| Coordinador Programa Cronistas | 1 | docente o referente educativo local |
| Mentor Cronistas | 1-2 | adulto formado, puede ser el Coordinador |
| Comité de Arranque | 3 | Territorial + referente CPP + referente FCP |
| Soporte técnico | 1 | persona que mantiene la infraestructura |

Total esperado: **10-15 personas activas** al cierre del mes 6 del piloto.

---

## 6. Infraestructura técnica mínima del piloto

### 6.1 Componentes obligatorios

- **Repositorio Git** (Granite o repositorio derivado) para CO y sus documentos asociados.
- **Bot de WhatsApp** con persistencia de payloads y cola de ingesta.
- **Formulario web** público con validación de campos y captcha.
- **Backend de *triage*** simple (puede ser scripts + base SQLite inicialmente).
- **Dashboard de curación** básico (puede ser interfaz mínima sobre el repositorio Git).
- **Backup diario** cifrado, retención mínima 30 días.
- **Sistema de notificaciones** al contribuyente y al curador (WhatsApp + email).

### 6.2 Componentes diferidos (no en piloto)

- Firmas criptográficas en Provenance Chain.
- API pública de consulta programática.
- Sincronización multi-territorio.
- Integración con bases externas (SNASPE, SII, CBR).
- Field app offline.

---

## 7. Controles de seguridad activos en piloto

Del Threat Model `[04:*]`, los controles obligatorios durante el piloto son:

| Control | Descripción |
|---|---|
| T1 — Polígonos sensibles | Catálogo interno de sitios sensibles cargado en el *triage* antes del primer CO |
| T6 — Consentimiento estricto | Validación automática de coherencia entre `scope` y `access.level` |
| T3 — Provenance append-only | Git con branch principal protegido, auditoría semanal |
| T11 — Backup | Diario + offline semanal |
| T8 — Dimensionamiento | Detener canales si backlog > 30 días |
| T2 — Licenciamiento | Matriz aplicada desde el día 1 |

Los controles restantes del Threat Model se implementan progresivamente durante el piloto con calendario documentado.

---

## 8. Indicadores del piloto

Panel semanal simple con:

- CO recibidos, curados, publicados por semana.
- Tiempo medio de resolución por track.
- Distribución por dominio.
- Distribución por sector geográfico del territorio.
- Curadores activos.
- Contribuyentes únicos.
- Disputas abiertas y cerradas.
- Backlog pendiente.

Revisión del panel en reuniones quincenales del Comité de Arranque.

---

## 9. Criterios de cierre del piloto

Al cabo de 12 meses, el piloto se considera **exitoso** si cumple al menos 6 de los siguientes 8 criterios:

1. ≥ 100 CO publicados con estado `published`.
2. ≥ 10 curadores activos al cierre.
3. Al menos 3 Cronistas Avanzados formados.
4. Al menos 1 disputa real tramitada y resuelta por el Dispute Layer.
5. Cobertura territorial en al menos 4 sectores distintos de la comuna.
6. Al menos 20 CO en dominio `base_territorial_juridica` usando `ext_normative_instrument`.
7. Menos de 5% de retracciones sobre CO publicados.
8. Encuesta simple a curadores y contribuyentes con satisfacción ≥ 70%.

Si cumple los 8, el territorio adherente pasa a régimen permanente. Si cumple 6 o 7, pasa a régimen con plan de mejora. Si cumple 4 o 5, se extiende el piloto 6 meses con correcciones. Si cumple menos, se evalúa rediseño sustantivo.

---

## 10. Bitácora del piloto

Durante la ejecución del piloto, el Curador Territorial mantiene una **bitácora pública** con:

- decisiones operativas relevantes,
- cambios a este Pilot Profile y su fundamentación,
- lecciones aprendidas,
- propuestas de mejora para el estándar general.

La bitácora es insumo directo para la siguiente versión del estándar.

---

## 11. Plan de fases del piloto

| Fase | Meses | Hitos |
|---|---|---|
| **Fase 0 — Preparación** | Previo al día 1 | Infraestructura técnica instalada. Catálogo de polígonos sensibles cargado. Comité de Arranque constituido. Plantillas de formulario listas. |
| **Fase 1 — Arranque comunitario** | 1-3 | Primera cohorte Cronistas formada. Primeras 20 contribuciones comunitarias. Primer curador comunitario acreditado. |
| **Fase 2 — Apertura normativa** | 3-6 | EXT_01 activo. Primeros 10 instrumentos normativos ingresados. Segundo y tercer curador comunitario acreditados. |
| **Fase 3 — Expansión** | 6-9 | Apertura a curador científico asociado. Activación de segundo Extension Profile. Primera disputa real tramitada. |
| **Fase 4 — Consolidación** | 9-12 | Evaluación según criterios sección 9. Producción de Informe Curatorial Público. Propuestas para v2 del estándar. |

---

## 12. Qué NO hace el piloto

Para evitar sobrediseño, el piloto **NO**:

- Constituye el Consejo Curatorial formal (solo Comité de Arranque).
- Activa todos los canales (solo WhatsApp + Formulario).
- Implementa firmas criptográficas (append-only por proceso).
- Formaliza jurídicamente el rol curador (designación operativa, sin personería propia).
- Publica una API pública.
- Desarrolla más de un Extension Profile (EXT_01).
- Replica el sistema en otros territorios.
- Produce versiones en idiomas distintos al español.

Todas estas son tareas del régimen permanente, no del piloto.

---

## 13. Decisiones pendientes antes del día 1

Este documento no resuelve por sí solo algunas decisiones que requieren el Comité de Arranque y acuerdo con CPP/FCP:

1. **Stack técnico definitivo** para el bot de WhatsApp y el backend de *triage* (opciones: WhatsApp Business API oficial vs. wrapper no oficial; hosting local vs. nube; SQLite vs. Postgres).
2. **Ubicación del Git repositorio**: público desde el inicio vs. privado hasta fase 2.
3. **Identidad del Curador Territorial** durante el piloto.
4. **Alianza formal con colegio(s)** para Programa Cronistas.
5. **Presupuesto y fuente** (operación del piloto + infraestructura + incentivos Cronistas + comunicaciones).
6. **Relación institucional de TKIP con CPP y FCP**: TKIP no es CPP ni FCP; opera como estándar independiente. Formalizar esta independencia en documento corto firmado por el Comité de Arranque.

Estas decisiones son condición para activación del piloto.

---

*Fin del TKIP Pilot Profile — Cochamó v1.2 (draft).*
