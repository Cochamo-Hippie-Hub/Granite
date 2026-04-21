# TKIP Dispute Layer

**Territorial Knowledge Ingestion Protocol — Dispute Layer**
Versión 1.2 — Draft
Abril 2026
Licencia del documento: CC-BY-4.0

---

## Sobre este documento

Un repositorio territorial vivo va a tener conflicto. No puede no tenerlo. Donde conviven memorias, ciencias, oficios, intereses económicos, narrativas familiares y versiones contrapuestas de la historia, hay tensión. Negarlo es ingenuo; organizarlo es profesional.

Este documento define el **Dispute Layer**: el conjunto de cauces, plazos y decisiones mediante los cuales TKIP tramita desacuerdos sobre contenidos del repositorio. No reemplaza al sistema jurídico ni pretende ser un tribunal; ofrece cauces dentro del estándar para que los conflictos no destruyan al repositorio antes de llegar, si corresponde, a instancias externas.

El Dispute Layer está en estado **draft** porque hasta que no haya tramitado al menos una disputa real no se puede confirmar la robustez de sus cauces.

---

## 1. Principios

### 1.1 El conflicto es parte del sistema

El sistema se diseña con la presunción de que habrá disputas reales, no anómalas. Esperar que no las haya produce procesos improvisados cuando llegan.

### 1.2 Prefiere el cauce más liviano

Cada disputa se encauza primero por el proceso menos formal posible. Solo escalan los casos que el cauce ligero no resuelve. Esto protege recursos curatoriales y evita burocratización innecesaria.

### 1.3 El tiempo es parte del dispositivo

Un cauce sin plazos no es cauce. Un plazo sin consecuencias tampoco. Cada cauce declara tiempos máximos y acciones por defecto si esos tiempos se vencen.

### 1.4 La decisión se documenta

Toda disputa, independiente de su resultado, deja registro íntegro en provenance. La historia del conflicto es parte de la historia del CO.

### 1.5 No toda disputa se resuelve como "verdad única"

A veces el resultado es la coexistencia registrada de versiones. Forzar una verdad única donde el territorio tiene varias es hacer violencia interpretativa y TKIP la rehúye.

### 1.6 El sistema no sustituye al sistema jurídico

Cuando una disputa contiene elementos que requieren tribunales ordinarios (acusación penal, derechos de propiedad, difamación material), el Dispute Layer NO PRETENDE sustituirlos. Encauza internamente lo que le corresponde y deja constancia de lo que excede su ámbito.

---

## 2. Legitimados para iniciar disputa

Pueden iniciar una disputa formal:

- El **contribuyente original** de un CO.
- Cualquier **curador activo** acreditado.
- Un **tercero mencionado** nominalmente en un CO (con acreditación mínima de identidad).
- Una **comunidad organizada** a través de representante reconocido.
- Un **miembro del Consejo Curatorial** por oficio.
- Una **autoridad competente** por marco legal aplicable (ver `[04:T12]`).

Las disputas anónimas **NO DEBEN** tramitarse. Se permite reserva de identidad frente a terceros mientras dura la disputa, pero no ante el cauce que la tramita.

---

## 3. Tipos de disputa

El estándar reconoce los siguientes tipos canónicos. Cada tipo tiene un cauce preferente pero puede escalar.

### 3.1 Disputa de consentimiento

Afirmación de que el consentimiento registrado es inválido, caducado, revocado o falsificado.

Cauce preferente: **A** (diálogo directo con facilitación).

### 3.2 Disputa de atribución

Afirmación de que la autoría o la fuente está mal consignada. Incluye tanto atribución indebida como falta de atribución merecida.

Cauce preferente: **A**.

### 3.3 Disputa interpretativa

Afirmación de que la interpretación dada por los curadores (clasificación, tesauro, toponimia, alcance) es sustantivamente errónea.

Cauce preferente: **B** (panel curatorial ad hoc).

### 3.4 Disputa fáctica

Afirmación de que los hechos relatados en un CO son materialmente falsos.

Cauce preferente: **B**, con apoyo documental.

### 3.5 Disputa de sensibilidad

Afirmación de que el `access.level` asignado es incorrecto por defecto o por exceso.

Cauce preferente: **B**.

### 3.6 Disputa cultural

Afirmación de que el CO viola protocolos culturales propios de una comunidad (toponimia, uso de términos, referencias patrimoniales).

Cauce preferente: **B** con presencia obligatoria de representante de la comunidad afectada.

### 3.7 Disputa patrimonial

Afirmación de que el CO afecta derechos patrimoniales materiales (propiedad, derechos de explotación, marca).

Cauce preferente: **C** (Consejo Curatorial) y escalamiento externo si corresponde.

### 3.8 Disputa estructural

Afirmación de que el CO fue producido mediante irregularidad curatorial grave (conflicto de interés, provenance alterada, captura).

Cauce preferente: **C** con traslado directo y posible suspensión preventiva del curador involucrado (`[02:7.4]`).

### 3.9 Disputa de impacto

Afirmación de que la publicación del CO produce daño concreto a personas, especies o comunidad.

Cauce preferente: **B** con medida cautelar inmediata (reducción de `access.level`) durante la instrucción.

---

## 4. Cauces

TKIP define tres cauces de resolución. Van de lo más liviano a lo más formal.

### 4.1 Cauce A — Diálogo directo facilitado

Aplicable a disputas de baja complejidad o alta recuperabilidad (consentimiento, atribución, correcciones menores).

**Proceso**:

1. Apertura formal por el legitimado mediante canal habilitado. Se genera evento `disputed` en provenance del CO.
2. Un **curador facilitador** es asignado por el Curador Territorial en un plazo máximo de **5 días hábiles**. El facilitador NO es parte del conflicto ni tiene conflicto de interés declarado.
3. El facilitador convoca a las partes a una conversación (presencial, remota o asíncrona según el caso) en un plazo máximo de **10 días hábiles** desde su designación.
4. Las partes exponen y el facilitador busca acuerdo.
5. Si hay acuerdo: se registra con firma de ambas partes y el facilitador lo ejecuta operacionalmente (corrección, cambio de atribución, revocación de consentimiento, etc.). Se registra evento `dispute_resolved`.
6. Si no hay acuerdo: el facilitador escala a cauce B con informe de lo actuado.

**Tiempo máximo total**: 30 días hábiles desde apertura.

**Por defecto si se vence el plazo**: escalamiento automático a cauce B.

### 4.2 Cauce B — Panel curatorial ad hoc

Aplicable a disputas interpretativas, fácticas, de sensibilidad o culturales.

**Proceso**:

1. Apertura formal por el legitimado o por escalamiento desde cauce A.
2. Constitución del panel en un plazo máximo de **10 días hábiles**. El panel se compone de:
   - Un Curador Temático del dominio afectado (o de dominio análogo si no hay específico).
   - Un Curador Comunitario con legitimidad local.
   - Un Curador externo al territorio, invitado de otra implementación TKIP o de confianza del Consejo.
   - Para disputas culturales (3.6): presencia obligatoria de representante de la comunidad afectada como miembro pleno del panel.
3. El panel recibe el expediente: el CO, su provenance completa, los argumentos de las partes, la documentación aportada.
4. Audiencia con las partes en plazo máximo de **15 días hábiles** desde constitución. La audiencia PUEDE ser asíncrona si una parte lo requiere por razones de accesibilidad o seguridad.
5. Deliberación y decisión en plazo máximo de **10 días hábiles** desde audiencia.
6. La decisión es motivada, escrita y firmada por los miembros del panel.
7. Resultados posibles:
   - **Confirmación del CO tal como está**.
   - **Corrección específica del CO** (campos, atribución, access.level, etc.).
   - **Coexistencia registrada** de versiones (ver 5.1).
   - **Retracción del CO**.
   - **Escalamiento a cauce C** por exceder competencia del panel.
8. Registro de evento `dispute_resolved` en provenance.

**Tiempo máximo total**: 40 días hábiles desde apertura (60 días calendario referenciales).

**Por defecto si se vence el plazo**: escalamiento a cauce C.

### 4.3 Cauce C — Consejo Curatorial

Aplicable a disputas patrimoniales, estructurales, escalamientos desde A o B, o casos en que el propio Consejo toma la disputa por oficio.

**Proceso**:

1. Convocatoria extraordinaria del Consejo en plazo máximo de **15 días hábiles** desde apertura o escalamiento.
2. El Consejo PUEDE encargar a una comisión instructora de 3 miembros la preparación del expediente (especialmente útil en disputas estructurales).
3. Audiencia con las partes y recolección de pruebas en plazo de hasta **30 días hábiles**.
4. Deliberación y resolución en plazo de hasta **15 días hábiles** desde cierre de audiencia.
5. La decisión es motivada, escrita y firmada por todos los miembros presentes. Se registran disidencias individuales si las hay.
6. Resultados posibles:
   - Todos los del cauce B, más:
   - **Desacreditación de curador** en caso de disputa estructural con falta probada.
   - **Modificación de política curatorial** si el caso revela problema sistémico.
   - **Escalamiento a jurisdicción externa** cuando el caso excede el ámbito del estándar (ver sección 7).
7. Registro de evento `dispute_resolved` y, si corresponde, eventos específicos adicionales (`retracted`, `desacredited`, etc.).

**Tiempo máximo total**: 60 días hábiles desde apertura.

---

## 5. Resultados posibles

### 5.1 Coexistencia registrada

Cuando una disputa interpretativa o cultural no admite verdad única, el cauce puede resolver mediante **coexistencia registrada**: el CO se mantiene publicado pero acompañado de:

- Una **nota curatorial** pública indicando la existencia de versiones alternativas.
- Uno o más **CO hermanos** que contienen las versiones alternativas, con sus respectivos consentimientos.
- Un **vínculo explícito** entre todos ellos en el campo `references.related_contributions`.

Esta es la resolución preferida para disputas toponímicas, memoriales o de narrativa histórica donde la imposición de una versión única dañaría el principio de pluralidad `[03:3.4]`.

### 5.2 Retracción

Un CO retractado:

- Registra evento `retracted` en provenance con motivo obligatorio.
- Deja de ser accesible en su `access.level` público.
- **NO** se elimina físicamente (Core `[01:3.4]`).
- Queda disponible para auditoría curatorial y jurídica.
- **PUEDE** ser republicado si la causa de retracción cesa (ej. consentimiento recuperado, hecho aclarado). La republicación registra evento `republished`.

La retracción en Cauce A requiere acuerdo de partes. En Cauce B requiere decisión del panel. En Cauce C requiere mayoría calificada (⅔) del Consejo si el CO es `publica`.

### 5.3 Corrección

Una corrección es una modificación acotada del CO que:

- Registra evento `corrected` o, si es mayor, incrementa `version` del CO.
- Mantiene la Provenance Chain íntegra.
- Preserva la versión previa como histórica, accesible vía provenance.

La corrección es la resolución más frecuente. No requiere los recursos ceremoniales de una retracción y PUEDE ocurrir en cualquier cauce.

### 5.4 Confirmación

El CO se mantiene tal como está. La disputa queda documentada en provenance con su resolución. El CO no pierde legitimidad; gana trazabilidad: cualquiera que lo consulte en el futuro verá que fue disputado y confirmado.

### 5.5 Medida cautelar

Antes o durante la instrucción, el cauce PUEDE dictar medida cautelar:

- Reducción temporal de `access.level` (ej. de `publica` a `interna`).
- Etiquetado del CO como `in_dispute` visible al usuario final.
- Suspensión preventiva de curador involucrado en caso de disputa estructural.

Las medidas cautelares son siempre temporales y cesan con la resolución definitiva o con el vencimiento del cauce.

---

## 6. Derechos durante la disputa

### 6.1 Derecho de audiencia

Toda parte legitimada tiene derecho a ser oída antes de la resolución. La negación de audiencia es causal de nulidad del cauce.

### 6.2 Derecho a reserva parcial

Una parte PUEDE solicitar que ciertos elementos de su exposición no se publiquen aún en provenance mientras dura la disputa. El cauce PUEDE aceptarla salvo que afecte el derecho de audiencia de la contraparte.

### 6.3 Derecho a acompañamiento

Las partes PUEDEN hacerse acompañar por personas de confianza en la audiencia, incluidas figuras legales. Esto no convierte al cauce en un proceso judicial pero reconoce la asimetría de recursos entre partes.

### 6.4 Derecho a traducción e interpretación

Si una de las partes se expresa en lengua distinta a la operacional del cauce, se provee interpretación apropiada. En territorios multilingües esto PUEDE requerir presencia de hablante competente.

### 6.5 Derecho a recurrir

La decisión en cauce A es recurrible ante cauce B. La decisión en cauce B es recurrible ante cauce C. La decisión en cauce C es final dentro del estándar; tras ella solo cabe jurisdicción externa (sección 7).

El recurso tiene plazo de **15 días hábiles** desde notificación y debe fundarse en vicio procesal, elemento nuevo o error material evidente. No hay recurso de mera disconformidad.

---

## 7. Límites del Dispute Layer y jurisdicción externa

### 7.1 Lo que el Dispute Layer NO resuelve

El Dispute Layer no:

- Dirime **derechos de propiedad** sobre tierras, aguas, bienes.
- Determina **responsabilidad civil o penal** de las personas.
- Impone **sanciones económicas** fuera del ámbito curatorial.
- Reemplaza **procedimientos administrativos** reglados de la institución custodia.
- Resuelve **conflictos comunitarios de fondo** anteriores al repositorio.

Cuando una disputa contiene elementos de este tipo, el Dispute Layer:

1. Tramita la parte que sí le corresponde (acceso, atribución, publicación, consentimiento).
2. Declara expresamente cuál parte excede su competencia.
3. Documenta el envío a jurisdicción externa si la parte interesada decide escalarlo.

### 7.2 Relación con el sistema jurídico

TKIP opera **dentro** del marco legal aplicable al territorio. Nada en este documento contradice obligaciones legales de las personas o instituciones. Si una resolución de cauce queda sin efecto por decisión judicial posterior, esa decisión se registra como evento adicional en provenance y el CO se ajusta en consecuencia.

### 7.3 Interacción con requerimientos de autoridad

Los requerimientos formales de autoridad pública se tramitan según `[04:T12]`. El Dispute Layer NO sustituye ese protocolo pero PUEDE ser activado paralelamente si el requerimiento mismo genera disputa legítima entre partes.

---

## 8. Registro y aprendizaje

### 8.1 Repositorio público de decisiones

Las resoluciones del Dispute Layer se publican en un **repositorio de decisiones** de cada territorio, con:

- Tipo de disputa (anonimizado si es necesario).
- Cauce utilizado.
- Resumen del caso y de la decisión.
- Fundamentación.
- Disidencias si las hay.

El repositorio cumple tres funciones: transparencia territorial, formación curatorial continua, y construcción de jurisprudencia del estándar.

### 8.2 Contribución al estándar

Las decisiones relevantes **DEBERÍAN** ser contribuidas de vuelta a la discusión del estándar. Un patrón de resolución recurrente que se estabiliza en múltiples territorios puede ser formalizado en versiones futuras del Dispute Layer.

### 8.3 Revisión periódica del layer

Cada 2 años el Consejo Curatorial revisa los casos tramitados y propone mejoras. La versión incrementa cuando hay aprendizajes estructurales.

---

## 9. Disposiciones operativas

### 9.1 Apertura formal

Una disputa se abre por:

- Formulario público habilitado por cada territorio.
- Correo al punto de contacto del Curador Territorial.
- Solicitud presencial canalizada por un curador activo.

El Curador Territorial DEBE acusar recibo en un plazo máximo de **3 días hábiles** con identificador de expediente (`tkip-dispute-YYYY-<slug>`) y asignación inicial de cauce.

### 9.2 Confidencialidad procesal

Durante la tramitación:

- Las comunicaciones entre partes y cauce son confidenciales salvo acuerdo expreso en contrario.
- Tras la resolución, la decisión es pública en los términos de la sección 8.1.
- Los miembros del cauce están obligados a reserva durante la tramitación.

### 9.3 Costos

El Dispute Layer es gratuito para las partes. Los costos operativos son absorbidos por la implementación territorial. Esto es doctrinal: la posibilidad de disputar **NO DEBE** depender de capacidad económica.

### 9.4 Integración con provenance

Cada acto procesal relevante genera evento en la provenance del CO disputado:

- `disputed` al abrir.
- `dispute_cauce_assigned` al asignar cauce.
- `dispute_hearing_held` tras audiencia.
- `dispute_measure_taken` si hay cautelar.
- `dispute_resolved` al cerrar.

Los eventos llevan como `note` una referencia al expediente de disputa, sin incluir su contenido completo (que vive en el repositorio de decisiones).

---

## 10. Casos ilustrativos

*Esta sección es informativa. No forma parte normativa.*

### 10.1 Caso 1 — Toponimia disputada

Dos familias reclaman que el CO publicado sobre el nombre histórico de un sector del valle es incorrecto; cada una sostiene un topónimo distinto con fuentes propias.

**Cauce esperado**: B. **Resolución probable**: coexistencia registrada con ambas toponimias documentadas, sus respectivas comunidades de reconocimiento y sus fuentes.

### 10.2 Caso 2 — Consentimiento revocado de historia oral

Un adulto mayor, tras escuchar su testimonio publicado, siente incomodidad y pide retirarlo.

**Cauce esperado**: A. **Resolución probable**: restricción inmediata por 15 días según Core `[01:12.2]`, diálogo facilitado, y decisión conjunta (muy probablemente retracción o coexistencia con versión acotada).

### 10.3 Caso 3 — CO con geolocalización que afecta especie amenazada

Un investigador publica CO con coordenadas de madriguera de huemul. Organización de conservación solicita medida urgente.

**Cauce esperado**: B con medida cautelar inmediata (`access.level` baja a `reservada` al ingresar la disputa). **Resolución probable**: corrección a nivel de precisión (borrado de dígitos finales de GPS o polígono difuso) y mantención del CO.

### 10.4 Caso 4 — Disputa estructural sobre curador

Un contribuyente aporta evidencia de que un curador tramitó su CO con conflicto de interés no declarado (lazo familiar con tercero mencionado negativamente).

**Cauce esperado**: C con suspensión preventiva del curador durante instrucción. **Resolución probable**: re-curación del CO por otro curador + evaluación del curador según `[02:7.4]`.

---

*Fin del TKIP Dispute Layer v1.2 (draft).*
