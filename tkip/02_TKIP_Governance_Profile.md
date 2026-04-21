# TKIP Governance Profile

**Territorial Knowledge Ingestion Protocol — Governance Profile**
Versión 1.2 — Stable
Abril 2026
Licencia del documento: CC-BY-4.0

---

## Sobre este documento

Este documento define la gobernanza curatorial de TKIP: quién puede curar qué, con qué nivel de responsabilidad, bajo qué proceso de acreditación, y cómo se coordinan colectivamente los curadores de un territorio.

Es un documento **normativo**. Complementa al Core Standard `[01:*]` sin modificarlo. Una implementación que adopte solo el Core SIN el Governance Profile puede funcionar técnicamente, pero carece del aparato de gobierno que legitima sus publicaciones.

Este documento depende del Core Standard `[01:*]` y está informado por la Cultural Charter `[03:*]`.

---

## 1. Propósito

La curación en TKIP no es un rol técnico ni un acto administrativo. Es un **acto de confianza territorial**: una persona con legitimidad en un territorio firma con su nombre una decisión sobre qué conocimiento entra al repositorio común, en qué nivel de acceso, y con qué interpretación.

El Governance Profile existe para que ese acto de confianza sea:

1. **Atribuible** — se sabe quién curó qué, cuándo, bajo qué rol.
2. **Proporcional** — el nivel de responsabilidad crece con el alcance curatorial.
3. **Plural** — ninguna persona concentra poder curatorial sobre todo el territorio.
4. **Revisable** — toda decisión curatorial puede ser cuestionada mediante el Dispute Layer `[05:*]`.
5. **Aprendible** — existe una ruta formativa que permite pasar de contribuyente a curador en tiempos razonables.

---

## 2. Niveles curatoriales

TKIP define cuatro niveles curatoriales individuales y un órgano colegiado.

### 2.1 Curador Aprendiz

**Perfil**: persona en proceso de formación curatorial. Típicamente Cronista Joven (ver sección 9) o contribuyente regular que ha manifestado interés en asumir responsabilidad curatorial.

**Atribuciones**:
- PUEDE proponer CO para curación por niveles superiores.
- PUEDE enriquecer metadatos de un CO en track `light`.
- NO DEBE firmar publicaciones como curador único.
- DEBE trabajar bajo mentoría de un Curador Comunitario o superior.

**Duración típica en el nivel**: 6-12 meses antes de acreditación formal.

### 2.2 Curador Comunitario

**Perfil**: persona acreditada de la comunidad local (vecino, operador, arriero, escalador recurrente, referente cultural o educativo).

**Atribuciones**:
- PUEDE firmar publicaciones track `light` en su dominio de competencia.
- PUEDE participar en pares de validación para track `deep`.
- PUEDE aprobar contribuciones de Cronistas Jóvenes y Aprendices.
- NO DEBE aprobar CO con `access.level = reservada` sin concurrencia de Curador Territorial.

**Requisitos**:
- Acreditación formal (sección 7).
- Mínimo 3 meses como Aprendiz o equivalente demostrable.
- Consentimiento explícito a las obligaciones del rol.

### 2.3 Curador Temático

**Perfil**: persona con competencia específica en un dominio (científico para `conservacion_ecologica`, abogado para `base_territorial_juridica`, guardaparque para `gestion_del_area`, etc.).

**Atribuciones**:
- PUEDE firmar publicaciones en su dominio en cualquier track.
- PUEDE validar Extension Profiles invocados en su dominio.
- PUEDE proponer actualizaciones al tesauro del dominio.
- NO DEBE firmar publicaciones fuera de su dominio temático sin concurrencia.

**Requisitos**:
- Acreditación por el Consejo Curatorial con informe de competencia.
- Puede ser externo al territorio si el Consejo lo valida.
- Compromiso mínimo de 12 meses.

### 2.4 Curador Territorial

**Perfil**: persona con visión transversal del territorio. Responsable operativo de la continuidad del repositorio en un territorio específico.

**Atribuciones**:
- PUEDE firmar publicaciones en cualquier dominio y cualquier track.
- PUEDE aprobar CO con `access.level = reservada`.
- PUEDE declarar backlog de emergencia y detener canales (ver `[04:T8]`).
- PUEDE convocar al Consejo Curatorial.
- PUEDE restringir o retractar un CO publicado bajo justificación registrada.
- DEBE publicar informe trimestral al Consejo.

**Requisitos**:
- Acreditación por el Consejo Curatorial con mayoría calificada (⅔).
- Dedicación mínima estimada: 20-30% FTE durante el período.
- No puede ser simultáneamente directivo de la institución administradora del área.
- Período inicial de 2 años, renovable una vez.

### 2.5 Consejo Curatorial

Órgano colegiado definido en la sección 4.

---

## 3. Responsabilidades transversales

Todo curador, en cualquier nivel, DEBE:

1. **Registrar con firma cada acción** en la Provenance Chain del CO (Core `[01:6]`).
2. **Declarar conflictos de interés** sobre contribuciones de familia directa, socios comerciales o causas personales abiertas. Un CO con conflicto declarado DEBE ser curado por otro curador.
3. **Respetar el consentimiento** del contribuyente. Un curador NO DEBE ampliar el `source.consent.scope` sin re-consulta documentada.
4. **Escalar al nivel superior** los casos de duda material sobre acceso, sensibilidad o alcance.
5. **Mantener confidencialidad** sobre contenidos `reservada` o en `in_dispute` fuera del proceso formal.
6. **Participar en revisión entre pares** al menos una vez por trimestre.

El incumplimiento reiterado de estas obligaciones es causal de desacreditación (sección 7.4).

---

## 4. Consejo Curatorial

### 4.1 Naturaleza

El Consejo Curatorial es el órgano colegiado que gobierna la política curatorial del territorio. No es un órgano jurídico; es un órgano operativo y deliberativo vinculado al estándar.

El Consejo **NO** administra el área protegida. **NO** sustituye al directorio de la Corporación o Fundación que custodia el área. **NO** representa a la comunidad en asuntos políticos. Su mandato es estrictamente el gobierno del repositorio.

### 4.2 Composición

El Consejo se compone de:

- El **Curador Territorial** en ejercicio (miembro nato).
- 2 a 4 **Curadores Comunitarios** electos o designados según el reglamento territorial local.
- 1 a 2 **Curadores Temáticos** por rotación temática.
- 1 **miembro externo** sin rol curatorial previo, con experiencia en gobernanza de open data, conservación o cultura territorial, designado por el Consejo saliente.
- 1 **miembro joven** proveniente del Programa Cronistas (ver sección 9), con voz plena y voto por mayoría simple.

Tamaño total: **mínimo 5, máximo 9**. Composición sesgada hacia comunidad local (al menos 50% de miembros son Curadores Comunitarios o miembro joven).

### 4.3 Período

- Período ordinario: 2 años.
- No puede haber más del 50% de renovación simultánea (rotación escalonada).
- Un miembro PUEDE servir hasta 2 períodos consecutivos; tras ello, pausa mínima de 2 años antes de reelección.

### 4.4 Funciones

El Consejo Curatorial:

1. **Acredita y desacredita curadores** en todos los niveles salvo Territorial, que requiere mayoría calificada.
2. **Resuelve disputas escaladas** por el Dispute Layer `[05:*]` según el cauce C.
3. **Actualiza el tesauro controlado** de enums extensibles.
4. **Aprueba Extension Profiles territoriales** propuestos.
5. **Revisa el informe trimestral** del Curador Territorial.
6. **Actualiza el catálogo de polígonos sensibles** (`[04:T1]`).
7. **Decreta retractaciones** cuando la gravedad lo amerita.
8. **Representa al territorio** ante otras implementaciones TKIP para armonización.

### 4.5 Quórum y mayorías

- Quórum ordinario: mayoría simple de miembros.
- Decisiones ordinarias: mayoría simple de presentes.
- Desacreditación de curador: mayoría simple de todos los miembros (no solo presentes).
- Acreditación de Curador Territorial: mayoría calificada (⅔) de todos los miembros.
- Retractación de CO publicado con `access.level = publica`: mayoría calificada (⅔) de presentes.
- Aprobación de Extension Profile territorial: mayoría simple de presentes.

### 4.6 Actas

Todas las reuniones producen acta pública salvo las dedicadas a asuntos `reservada` o `in_dispute`, cuyas actas son restringidas a miembros del Consejo hasta resolución. Las actas **DEBEN** conservarse por 20 años como mínimo.

---

## 5. Matriz de permisos

Esta matriz resume qué puede hacer cada nivel curatorial según `access.level` del CO y `curation_track`.

| Acción | Aprendiz | Comunitario | Temático | Territorial | Consejo |
|---|---|---|---|---|---|
| Proponer CO | ✓ | ✓ | ✓ | ✓ | ✓ |
| Enriquecer metadatos (light) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Firmar publicación track `auto` | — | ✓* | ✓* | ✓ | — |
| Firmar publicación track `light` (pública) | — | ✓ | ✓ | ✓ | — |
| Firmar publicación track `deep` (pública) | — | ✓ (par) | ✓ | ✓ | — |
| Firmar publicación `interna` | — | — | ✓ | ✓ | — |
| Firmar publicación `reservada` | — | — | — | ✓ | ✓ (aprueba política) |
| Restringir CO publicado | — | — | Propone | ✓ | ✓ (ratifica) |
| Retractar CO publicado | — | — | — | Propone | ✓ |
| Acreditar curador Aprendiz/Comunitario | — | — | ✓ (propone) | ✓ (propone) | ✓ (decide) |
| Acreditar Curador Temático | — | — | — | ✓ (propone) | ✓ (decide) |
| Acreditar Curador Territorial | — | — | — | — | ✓ (⅔) |
| Desacreditar curador | — | — | — | ✓ (propone) | ✓ (decide) |
| Actualizar tesauro | — | — | ✓ (propone) | ✓ (propone) | ✓ (aprueba) |
| Aprobar Extension Profile territorial | — | — | ✓ (propone) | ✓ (propone) | ✓ (aprueba) |
| Declarar backlog emergencia | — | — | — | ✓ | ✓ (ratifica en 7 días) |
| Convocar al Consejo | — | — | — | ✓ | — |

*El track `auto` requiere además el catálogo de patrones autorizados vigente, que es competencia del Consejo.

"Firmar" significa registrar el evento correspondiente de la Provenance Chain con la identidad del curador. "(par)" indica que el curador participa en la dupla de validación pero no firma solo.

---

## 6. Tracks de curación

### 6.1 Definición normativa

TKIP define tres tracks de curación. La asignación inicial ocurre en la etapa de *triage* (Core `[01:3.3]`) y **PUEDE** ser reasignada por un curador.

#### 6.1.1 Track `auto`

Aplicable cuando:
- El CO proviene de canal técnico (`upload_direct`, `field_app`, `api`) con consentimiento implícito o preregistrado.
- La estructura del CO coincide con un **patrón autorizado** vigente (formato, origen, contenido).
- El nivel de acceso propuesto es `publica` o `interna`.

Firma requerida: una firma de Curador Comunitario o superior, aplicada **en bloque** a todos los CO publicados bajo un mismo patrón autorizado por período (ej. semanal). La firma en bloque **NO** exime de provenance individual: cada CO conserva su cadena propia.

Cuando un CO en track `auto` se sale del patrón (error de parsing, enum desconocido, campo faltante opcional), DEBE reasignarse automáticamente a track `light`.

#### 6.1.2 Track `light`

Aplicable cuando:
- El CO es individual y requiere revisión humana, pero no levantamiento de consenso.
- El contenido es claro, el consentimiento es explícito, y no hay ambigüedad de acceso.

Firma requerida: una firma de Curador Comunitario o superior. Tiempo objetivo de resolución: **72 horas** desde recepción.

#### 6.1.3 Track `deep`

Aplicable cuando:
- Contenido cultural sensible (historia oral con menciones a terceros, toponimia disputada, relatos comunitarios de cierta edad).
- `access.level = reservada` propuesto.
- Disputas previas sobre contenidos análogos.
- Extension Profile con validación temática obligatoria.

Firma requerida: dos firmas (par), al menos una de ellas de Curador Territorial o Temático. Tiempo objetivo de resolución: **2 semanas** máximo.

### 6.2 Distribución esperada

Sin ser normativa, la distribución esperada por volumen en un territorio maduro es:

- `auto`: 70-80% del volumen.
- `light`: 15-20%.
- `deep`: 5-10%.

Distribuciones fuertemente divergentes sostenidas (por ejemplo, >30% deep) son indicio de que el *triage* está mal calibrado o de que hay un problema estructural con la naturaleza del contenido entrante.

### 6.3 Reasignación de track

Cualquier curador, al abrir un CO, PUEDE proponer reasignar su track. La reasignación se registra en provenance con evento `triaged` y `note` explicativa. No requiere aprobación adicional.

---

## 7. Acreditación y desacreditación

### 7.1 Ruta formativa

```
Contribuyente → Aprendiz → Comunitario → Temático/Territorial → Consejo
```

La ruta no es obligatoria ni lineal. Un Curador Temático puede ingresar directamente si su perfil profesional lo justifica. Un Curador Territorial **DEBE** haber sido curador en algún nivel previo.

### 7.2 Proceso de acreditación

La acreditación de un curador sigue este proceso:

1. **Propuesta** por un curador activo o auto-propuesta por la persona interesada.
2. **Informe de trayectoria** (contribuciones previas, participación comunitaria, perfil profesional cuando corresponda).
3. **Entrevista** con al menos dos miembros del Consejo (salvo Aprendiz, que solo requiere informe).
4. **Período de prueba** con mentoría activa:
   - Aprendiz: 3 meses.
   - Comunitario: 3 meses operando como Aprendiz en misiones curatoriales reales.
   - Temático: 1-2 misiones curatoriales supervisadas en su dominio.
   - Territorial: 6 meses operando como Comunitario o Temático en el territorio.
5. **Decisión del Consejo** según mayorías de sección 4.5.
6. **Juramento operativo**: firma de compromiso con las obligaciones de su nivel y con la Cultural Charter `[03:*]`.

La acreditación genera un identificador curatorial `tkip-curator-<slug>` que firma todas sus acciones posteriores.

### 7.3 Registro público

Una implementación territorial **DEBE** mantener un registro público de curadores activos con:

- Identificador curatorial.
- Nombre o seudónimo (según preferencia declarada).
- Nivel curatorial.
- Dominios de competencia (cuando aplique).
- Fecha de acreditación.
- Fecha de próxima revisión.

El registro **NO** incluye datos personales sensibles ni historial de decisiones curatoriales individuales; esas quedan en la provenance de cada CO.

### 7.4 Desacreditación

Un curador puede ser desacreditado por:

1. **Incumplimiento reiterado** de las responsabilidades transversales (sección 3).
2. **Conflicto de interés no declarado** probado.
3. **Ruptura de confidencialidad** sobre contenidos `reservada` o `in_dispute`.
4. **Falsificación de provenance** (manipulación dolosa de la cadena).
5. **Abandono** del rol por más de 6 meses sin justificación.
6. **Solicitud propia** en cualquier momento.

El proceso:

1. Reporte formal al Consejo por cualquier curador activo o por vía del Dispute Layer `[05:*]`.
2. Suspensión preventiva del curador en caso de falta grave durante la instrucción (máximo 30 días).
3. Instrucción por una comisión de 3 miembros del Consejo (no incluye al reportado).
4. Derecho del curador a ser oído y a presentar descargos.
5. Decisión del Consejo pleno por mayoría simple.

La desacreditación se registra públicamente en el registro, con nivel de detalle que preserve dignidad personal pero garantice transparencia institucional. Un curador desacreditado PUEDE ser reacreditado tras 12 meses y un nuevo proceso.

### 7.5 Revocación de firmas

La desacreditación **NO** revoca las firmas curatoriales pasadas del curador. Las publicaciones firmadas siguen siendo válidas salvo que la causa de desacreditación sea falsificación de provenance; en ese caso, los CO firmados por el desacreditado entran en revisión automática por el Consejo.

---

## 8. Rotación y sucesión

### 8.1 Principio de rotación

Ningún rol curatorial es vitalicio. La rotación es una salvaguarda contra la captura institucional y contra la fatiga personal.

### 8.2 Preparación de sucesión

Seis meses antes del fin del período:

- El Curador Territorial **DEBE** identificar candidatos a sucesión y comenzar proceso de mentoría.
- Los Curadores Temáticos **DEBERÍAN** documentar tesauro y criterios para facilitar transición.
- El Consejo convoca proceso formal de renovación.

### 8.3 Transición

La transición entre curadores supone:

- Traspaso documentado de expedientes en curso.
- Sesión conjunta de al menos una semana de overlap operacional.
- Comunicación pública del cambio.
- Actualización del registro público.

### 8.4 Ausencia abrupta

Si un curador cesa súbitamente (fallecimiento, emergencia, renuncia inmediata):

- Un curador del mismo nivel asume interinamente por decisión del Consejo.
- El Consejo dispone de 60 días para iniciar proceso ordinario de acreditación.
- Los CO firmados interinamente se marcan con `note` de provenance explicitando la suplencia.

---

## 9. Anexo — Programa Cronistas del Valle

*Este anexo es una reference social implementation del rol curador comunitario. Forma parte normativa del Governance Profile.*

### 9.1 Propósito

El Programa Cronistas del Valle es una estrategia de activación comunitaria y formación temprana de curadores, pensada especialmente para territorios con baja densidad de actores curatoriales iniciales. Convierte a jóvenes y adultos del territorio en agentes activos del repositorio, con reconocimiento, ruta formativa y vínculo con el estándar.

### 9.2 Niveles del Programa

#### 9.2.1 Cronista Joven

**Perfil**: estudiante o joven del territorio (edad referencial 12-18 años).

**Función**:
- Entrevista a familiares, vecinos, operadores, arrieros con el consentimiento de ambas partes.
- Produce CO derivados de esas entrevistas (historia oral, toponimia, oficios, memoria).
- Participa en jornadas periódicas de revisión con su Mentor.

**Reconocimiento**:
- Certificado escolar o comunitario al completar año.
- Mención pública en el repositorio (cuando el consentimiento del aporte lo permite).
- PUEDE acceder a cupos preferentes en programas educativos territoriales.

**Tránsito**: tras un año activo con aportes curados, PUEDE postular a Cronista.

#### 9.2.2 Cronista

**Perfil**: adulto joven o adulto formado por el Programa (referencial 18+).

**Función**:
- Coordina equipos de Cronistas Jóvenes.
- Produce CO propios de mayor alcance.
- Participa como Aprendiz en el sistema curatorial.

**Reconocimiento**:
- Eventual pasantía remunerada en proyectos de conservación.
- Carta de reconocimiento de la institución custodia del área.
- Participación en formaciones especializadas.

**Tránsito**: un Cronista activo durante 2 años PUEDE ser acreditado Curador Comunitario por el Consejo.

#### 9.2.3 Cronista Avanzado

**Perfil**: Cronista con trayectoria demostrada y liderazgo formativo.

**Función**:
- Mentora a Cronistas Jóvenes.
- Representa al Programa ante el Consejo Curatorial.
- Contribuye al diseño curricular del Programa.

**Reconocimiento**:
- Es miembro joven natural del Consejo Curatorial (sección 4.2).
- Certificación formal del Programa.
- PUEDE representar al territorio en intercambios con otros TKIP territoriales.

### 9.3 Estructura operativa

Cada implementación territorial del Programa **DEBERÍA** contar con:

- Un **Coordinador del Programa** (puede ser docente local o referente cultural).
- Uno o dos **Mentores** (Cronistas Avanzados o Curadores Comunitarios).
- Vínculo formal con al menos un colegio o espacio educativo comunitario.
- Ciclo anual con al menos 3 jornadas colectivas y 2 productos visibles por cohorte.

### 9.4 Incentivos

Los incentivos son **plurales y no monetarios por defecto**. Algunos admisibles:

- Reconocimiento público en el repositorio y en espacios comunitarios.
- Participación en salidas territoriales formativas.
- Acceso preferencial a programas educativos o culturales regionales.
- Material didáctico producido por el Programa.
- Cupos en pasantías con aliados estratégicos.
- Remuneración simbólica en hitos puntuales (no como salario).

Los incentivos **NO DEBEN** convertir el rol curador en relación laboral disfrazada. El Cronista es un contribuyente reconocido, no un empleado.

### 9.5 Protección específica

Cuando participan menores de edad:

- DEBE existir consentimiento informado de madre, padre o tutor.
- Los CO producidos por un Cronista Joven **NUNCA** se publican con acceso `publica` sin revisión del Coordinador.
- La identidad del Cronista Joven **NO** se publica como autoría nominal si se trata de un menor, salvo autorización específica del tutor para cada CO.
- Las jornadas se realizan en espacios seguros con presencia de al menos un adulto responsable acreditado.

### 9.6 Articulación con el Consejo

El Cronista Avanzado que ocupa el asiento en el Consejo Curatorial:

- Tiene voz y voto plenos.
- Representa específicamente la perspectiva juvenil y formativa.
- NO tiene obligaciones de confidencialidad distintas a las de cualquier otro miembro.
- PUEDE ser acompañado por un adulto del Programa en sesiones si es menor de edad, sin derecho a voto este último.

---

## 10. Disposiciones finales

### 10.1 Adaptación territorial

Este Profile es un marco común. Cada territorio adherente **PUEDE** adaptarlo a su escala, cultura y realidad operativa siempre que:

- No contradiga requisitos **DEBE** del Core Standard `[01:*]`.
- No reduzca las salvaguardas mínimas (consentimiento, curación humana obligatoria, provenance firmada).
- Documente públicamente sus adaptaciones.

Las adaptaciones se presentan como **perfiles territoriales** que referencian a este documento.

### 10.2 Relación con la institución custodia

La institución custodia del área (Corporación, Fundación, Parque, organismo público) **NO** es parte del Consejo Curatorial por derecho propio. Un miembro de su directorio o equipo ejecutivo **PUEDE** integrar el Consejo si es acreditado por la vía ordinaria como Curador Temático o Comunitario, siguiendo las reglas de incompatibilidad (sección 2.4).

Esta separación es una salvaguarda doctrinal: el repositorio pertenece al territorio, no a la institución. La institución lo apoya; no lo captura.

### 10.3 Revisión del Profile

Este documento se revisa cada 2 años o cuando una experiencia territorial aporte lecciones sustantivas. La revisión es facilitada por el Consejo Curatorial más antiguo entre las implementaciones activas.

---

*Fin del TKIP Governance Profile v1.2.*
