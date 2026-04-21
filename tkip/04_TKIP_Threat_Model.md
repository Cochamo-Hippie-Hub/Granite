# TKIP Threat Model

**Territorial Knowledge Ingestion Protocol — Threat Model**
Versión 1.2 — Draft
Abril 2026
Licencia del documento: CC-BY-4.0

---

## Sobre este documento

Este documento identifica las amenazas estructurales que cualquier implementación TKIP enfrentará, clasifica su severidad y prescribe controles. Está deliberadamente escrito en clave operacional: lo que hay que hacer, no lo que sería deseable en abstracto.

Un territorio que implemente TKIP sin aplicar los controles marcados como **obligatorios** publicará un repositorio técnicamente conforme pero estructuralmente frágil. Este documento es el filtro entre una implementación ingenua y una implementación madura.

El Threat Model está en estado **draft** porque requiere un ejercicio red-team antes del piloto de Cochamó para refinarse con amenazas observadas en terreno real.

---

## 1. Principios

### 1.1 Ingenuidad no es neutralidad

Un sistema de conocimiento territorial recibe contribuciones de todo tipo de actores. Algunos tienen buena fe, otros no. Asumir que todos la tienen produce sistemas capturables. Asumir que ninguno la tiene produce sistemas inutilizables. TKIP opera desde el supuesto de que la mayoría son bienintencionados y el sistema debe resistir a la minoría que no lo es.

### 1.2 Amenazas reales, no teóricas

Este documento se concentra en amenazas que TKIP enfrentará por la naturaleza de su ámbito: territorios con valor ecológico, jurídico y económico, donde distintos actores tienen intereses no siempre alineados. No cataloga amenazas genéricas de sistemas de información (XSS, SQLi, etc.) que tienen abundante literatura propia.

### 1.3 Controles proporcionales

Los controles se escalan al riesgo real del territorio. Una reserva privada de 1.000 ha no necesita los mismos controles que una área protegida de 130.000 ha adyacente a operaciones extractivas activas. El Consejo Curatorial **DEBE** revisar este documento en su contexto territorial y declarar cuáles controles aplica como obligatorios.

### 1.4 Resiliencia antes que perfección

Ningún sistema es invulnerable. TKIP prioriza resiliencia: la capacidad de detectar incidentes, limitar daño y recuperarse, por sobre la promesa ilusoria de prevención absoluta.

---

## 2. Modelo de amenazas

### 2.1 Actores adversarios potenciales

Este inventario no es acusatorio. Es un ejercicio de diseño defensivo: prever a quién puede perjudicar un repositorio territorial abierto y cómo podrían intentar instrumentalizarlo.

| Actor | Interés adverso potencial |
|---|---|
| Intereses extractivos (minería, forestales, proyectos hidroeléctricos) | Suprimir evidencia ecológica, debilitar argumentos jurídicos territoriales |
| Actores inmobiliarios especulativos | Extraer información predial, localizar vacíos jurídicos, forzar interpretaciones a su favor |
| Cazadores furtivos y tráfico de especies | Obtener ubicaciones precisas de fauna amenazada, accesos, horarios |
| Actores políticos hostiles al proyecto | Deslegitimar el repositorio, sembrar dudas sobre procedencia, forzar retractaciones |
| Competidores comerciales en ecoturismo | Capturar datos de reservas, operadores, visitantes |
| Medios sensacionalistas | Extraer material sensible fuera de contexto, tergiversar narrativas comunitarias |
| Actores internos mal intencionados | Curadores o contribuyentes que traicionan la confianza |
| Estado hostil o autoridad arbitraria | Exigir datos restringidos sin marco legal adecuado, presionar al Consejo |
| Investigadores extractivos | Publicar con datos comunitarios sin atribución ni consentimiento |
| Entidades que solicitan "transparencia total" de mala fe | Usar la apertura contra la integridad del sistema |

### 2.2 Vectores de ataque comunes

| Vector | Descripción sintética |
|---|---|
| Geolocalización indeseada | Publicar coordenadas que facilitan daño a especies, sitios culturales o personas |
| Ingesta masiva automatizada | Saturar el sistema con contribuciones falsas o de calidad marginal |
| Consentimiento falsificado o presionado | Obtener firmas o menciones sin consentimiento real |
| Captura curatorial | Concentrar control curatorial en un subconjunto alineado con un interés externo |
| Inyección de falso patrimonio | Introducir relatos fabricados con apariencia de tradición |
| Doxing de contribuyentes | Exponer identidades reservadas por inferencia cruzada |
| Apropiación extractiva | Usar contenido del repositorio sin atribución ni respeto al consentimiento |
| Denegación reputacional | Atacar la legitimidad del repositorio mediante campañas externas |
| Manipulación de provenance | Alterar la cadena para encubrir decisiones o borrar responsabilidades |
| Inundación legal | Exigir acceso a contenido `reservada` por vías administrativas o judiciales |

---

## 3. Controles normativos

Los siguientes controles son numerados como `T1`...`T15`. Cada control declara su estado (**obligatorio** u **recomendado**) y su aplicabilidad.

### T1 — Catálogo de polígonos sensibles

**Estado**: obligatorio.

Cada territorio DEBE mantener un catálogo interno de áreas donde la divulgación de coordenadas constituye riesgo:

- Sitios de nidificación o madrigueras de especies amenazadas.
- Sitios arqueológicos o patrimoniales no abiertos al público.
- Accesos vulnerables a sectores de alto valor ecológico.
- Propiedades privadas cuya ubicación exacta no ha sido consentida para publicación.

El *triage* DEBE confrontar todo CO con GPS contra el catálogo. Si el CO cae dentro de un polígono sensible:

- El CO entra automáticamente a track `deep`.
- El `access.level` se propone `interna` o `reservada`.
- Un curador humano decide la publicación.

El catálogo es mantenido por el Consejo Curatorial y se actualiza trimestralmente. Su contenido es `reservada`.

### T2 — Matriz de licenciamiento aplicada desde el día 1

**Estado**: obligatorio.

La matriz del Core `[01:9.1]` DEBE aplicarse a todo CO desde la primera publicación. Publicar sin licencia declarada es considerado error estructural y habilita retractación automática.

### T3 — Provenance append-only verificable

**Estado**: obligatorio.

La Provenance Chain DEBE residir en un sistema de almacenamiento que:

- No permita modificación retroactiva sin dejar rastro (Git con branch principal protegido como mínimo).
- Permita auditoría independiente.
- Respalde hashes periódicos en infraestructura externa (ej. commits firmados, backups cruzados).

En v2 se incorporan firmas criptográficas obligatorias para eventos críticos (Core `[01:6.4]`).

### T4 — Rotación curatorial

**Estado**: obligatorio.

Ningún curador ocupa un rol por más de 4 años consecutivos (sección Governance 4.3 y 8). La concentración de poder curatorial por encima de este umbral es indicador estructural de captura potencial.

### T5 — Acreditación formal de curadores

**Estado**: obligatorio.

Ningún curador opera sin acreditación formal según el proceso del Governance Profile `[02:7]`. "Consulta informal" o "curación de buena fe" no equivalen a curación formal.

### T6 — Consentimiento estricto

**Estado**: obligatorio.

El *triage* DEBE validar automáticamente la coherencia entre `source.consent.scope` y `access.level`. Incoherencias producen rechazo del CO en esta etapa. No hay publicación pública sin al menos los alcances `archivo` y `publicacion_abierta`.

### T7 — Doxing por inferencia

**Estado**: obligatorio.

Dos o más CO en estado `reservada` referidos a una misma persona identificable **NO DEBEN** publicarse simultáneamente si su combinación revela la identidad. El Consejo Curatorial evalúa coherencia inter-CO en revisiones trimestrales.

Ejemplo: un CO con consentimiento `reservado` que menciona a un contribuyente por seudónimo, combinado con otro CO con `atribuido` que revela el mismo evento, puede permitir inferir la identidad del primero. El segundo CO DEBE ser revisado antes de publicación.

### T8 — Dimensionamiento operativo

**Estado**: obligatorio.

El Curador Territorial DEBE declarar **backlog de emergencia** y detener canales cuando:

- La cola de curación excede 30 días de antigüedad media.
- Se reciben más de 10 CO/hora sostenidos por más de 24 horas (indicador de ingesta automatizada).
- Hay evidencia de campaña coordinada de ingesta.

Los canales detenidos se reactivan por decisión del Consejo con plan explícito de absorción del backlog.

### T9 — Revisión de fuentes externas

**Estado**: obligatorio cuando aplica.

Los CO que citan fuentes externas (DOI, ISBN, URL) DEBEN validar que la fuente existe al momento de la publicación. Un CO con referencia externa muerta o inventada es rechazado.

### T10 — Ejercicio red-team anual

**Estado**: recomendado (obligatorio para territorios > 50.000 ha o con alto valor ecológico).

Una vez al año, el Consejo Curatorial convoca una revisión externa donde un equipo independiente intenta identificar debilidades del sistema. El informe es público en su parte no-sensible.

### T11 — Backup y recuperación

**Estado**: obligatorio.

La infraestructura DEBE mantener:

- Backup diario incremental de los últimos 30 días.
- Backup semanal íntegro offline de los últimos 12 meses.
- Backup anual archivado de forma indefinida.
- Plan de recuperación documentado con prueba exitosa al menos anual.

### T12 — Protocolo ante requerimiento legal

**Estado**: obligatorio.

Ante requerimiento de autoridad administrativa o judicial sobre contenido `reservada`:

1. El Curador Territorial convoca al Consejo en sesión extraordinaria en un plazo máximo de 72 horas.
2. El Consejo evalúa el marco legal del requerimiento.
3. Se solicita acompañamiento legal calificado antes de cualquier entrega.
4. Los contribuyentes afectados son notificados salvo prohibición legal expresa.
5. La respuesta se documenta en provenance con evento `legal_request_responded`.

Este protocolo **NO** significa resistencia al Estado de Derecho. Significa cumplimiento informado y preservación de derechos de contribuyentes.

### T13 — Protocolo ante incidente de seguridad

**Estado**: obligatorio.

Ante evidencia de compromiso (acceso no autorizado, alteración de provenance, filtración de `reservada`):

1. Detención inmediata de canales afectados.
2. Informe al Consejo en 24 horas.
3. Notificación a contribuyentes afectados en 72 horas.
4. Análisis forense sobre la Provenance Chain.
5. Informe público de incidente con anonimización adecuada, dentro de 30 días.

### T14 — Defensa ante apropiación extractiva

**Estado**: recomendado.

Cuando se detecta que contenido del repositorio es republicado o reutilizado sin respeto a la licencia o al consentimiento:

- Primera acción: contacto directo con el responsable solicitando corrección.
- Segunda acción: comunicación pública documentando la apropiación.
- Tercera acción: acción legal si la licencia y el marco jurídico lo permiten.

La apropiación extractiva es corrosiva para la confianza de contribuyentes; el silencio institucional ante ella es peor que el incidente mismo.

### T15 — Transparencia del propio Threat Model

**Estado**: obligatorio.

Este documento en su versión territorial aplicada DEBE ser público. La publicación del modelo no facilita ataques; dificulta la captura porque obliga a adversarios a trabajar contra un sistema que declara conocer su propio terreno.

Los polígonos sensibles (T1) son la única excepción pública: se publica que existen, no su contenido.

---

## 4. Clasificación de severidad

| Amenaza (código interno) | Probabilidad | Impacto | Severidad | Controles relevantes |
|---|---|---|---|---|
| Geolocalización indeseada | Alta | Alto | **Crítica** | T1, T6, T7 |
| Captura curatorial | Media | Alto | **Crítica** | T4, T5, gobernanza plural |
| Consentimiento falsificado | Media | Alto | **Crítica** | T6, T5 |
| Apropiación extractiva | Alta | Medio | **Alta** | T2, T14 |
| Ingesta masiva automatizada | Media | Medio | **Alta** | T8, *triage* |
| Manipulación de provenance | Baja | Alto | **Alta** | T3, T13 |
| Doxing por inferencia | Media | Medio | **Alta** | T7 |
| Inyección de falso patrimonio | Baja | Medio | **Media** | T5, *deep* obligatorio |
| Inundación legal | Media | Medio | **Media** | T12 |
| Denegación reputacional | Media | Bajo | **Media** | T15, comunicación |
| Requerimiento legal abusivo | Baja | Medio | **Media** | T12 |

Las amenazas clasificadas como **crítica** DEBEN tener controles activos desde el día 1 de operación. Las **altas** DEBEN estar activas antes del sexto mes de operación. Las **medias** DEBERÍAN estar activas antes del primer año.

---

## 5. Protocolos de incidente

### 5.1 Clasificación de incidentes

- **Nivel 1** — incidente menor: error operativo sin impacto material (ej. CO mal curado que se corrige normalmente).
- **Nivel 2** — incidente relevante: daño reputacional limitado o compromiso parcial de datos `interna`.
- **Nivel 3** — incidente mayor: compromiso de datos `reservada`, filtración extensa, captura curatorial probada.
- **Nivel 4** — incidente crítico: daño a personas, especies o comunidades como consecuencia directa del incidente.

### 5.2 Respuesta por nivel

| Nivel | Acciones |
|---|---|
| 1 | Registro en provenance, corrección por curador responsable. |
| 2 | Informe al Consejo en ciclo regular. Análisis de causa-raíz. |
| 3 | Sesión extraordinaria del Consejo en 72 horas. Suspensión preventiva si hay personas implicadas. Notificación a contribuyentes afectados. Informe público en 30 días. |
| 4 | Todos los controles anteriores + comunicación institucional inmediata + involucramiento de autoridades competentes cuando corresponda + revisión estructural del Threat Model. |

---

## 6. Revisión del Threat Model

Este documento se revisa:

- Después de cada ejercicio red-team anual (T10).
- Después de cada incidente Nivel 3 o 4.
- Al menos cada 2 años aunque no haya incidentes.

Las revisiones se publican con versión incrementada. La historia del documento se preserva en el repositorio del estándar como registro epistémico de qué amenazas fuimos capaces de anticipar en cada momento y cuáles nos superaron.

---

*Fin del TKIP Threat Model v1.2 (draft).*
