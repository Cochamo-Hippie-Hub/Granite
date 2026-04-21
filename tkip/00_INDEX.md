# TKIP v1.2 — Conjunto documental

**Territorial Knowledge Ingestion Protocol**
Versión 1.2 — especificación estructurada en capas
Abril 2026

---

## Propósito del conjunto

TKIP v1.1 fue una especificación conceptual unificada. La crítica a v1.1 identificó tres limitaciones estructurales: (i) el documento mezclaba protocolo, gobernanza y doctrina en un solo texto, lo que reducía su portabilidad; (ii) le faltaba disciplina normativa (lenguaje RFC, enums cerrados, versionado); y (iii) carecía de capas críticas —dispute layer, threat model— sin las cuales ningún piloto serio podría sostenerse.

v1.2 responde a esas tres limitaciones. El protocolo se separa en tres documentos portables, se agregan dos documentos críticos previos al piloto, se produce un perfil piloto austero y operable, y se inaugura el mecanismo de **extension profiles** con un primer perfil canónico desarrollado.

El conjunto es diseñado para ser leído por lectores distintos. Un implementador técnico puede leer solo el Core. Un curador puede leer solo el Governance. Una organización territorial puede leer solo la Charter. Un equipo piloto puede leer solo el Pilot Profile.

---

## Estructura del conjunto

```
TKIP v1.2/
│
├── 00_INDEX.md                          [este documento]
│
├── 01_TKIP_Core_Standard.md             [normativo — el protocolo técnico]
├── 02_TKIP_Governance_Profile.md        [normativo — curadores y consejo]
├── 03_TKIP_Cultural_Charter.md          [doctrinal — axiomas y tesis]
│
├── 04_TKIP_Threat_Model.md              [normativo — amenazas y controles]
├── 05_TKIP_Dispute_Layer.md             [normativo — conflicto y apelación]
│
├── 06_TKIP_Pilot_Profile_Cochamo.md     [operativo — piloto austero]
│
└── EXT_01_Normative_Instrument.md       [extension profile canónico]
```

---

## Orden de lectura recomendado por perfil

| Lector | Orden sugerido |
|---|---|
| Implementador técnico | 01 → EXT_01 → 04 |
| Curador o futuro miembro del Consejo | 03 → 02 → 05 |
| Abogado del área protegida | 03 → EXT_01 → 02 → 05 |
| Científico contribuyente | 01 → 03 → 04 |
| Equipo piloto Cochamó | 06 → 04 → 05 → 01 |
| Organización territorial que evalúa adoptar TKIP | 03 → 01 → 02 |
| Donante o stakeholder estratégico | 03 → 06 |

---

## Qué cambió respecto de v1.1

| Dimensión | v1.1 | v1.2 |
|---|---|---|
| Estructura documental | 1 documento unificado | 3 documentos portables + 2 críticos + 1 piloto + perfiles |
| Lenguaje | narrativo | normativo con DEBE / DEBERÍA / PUEDE (equivalente RFC 2119) |
| Schema | YAML ejemplo | Core schema + mecanismo de extension profiles |
| Amplitud temática | sesgo hacia cultura comunitaria | cobertura pareja de los 6 dominios mediante perfiles |
| Gobernanza | integrada al protocolo | documento propio + dispute layer separado |
| Amenazas | no tratadas | documento propio con modelo explícito |
| Conflictos | tratados tangencialmente | dispute layer normativo con protocolo completo |
| Cronistas del Valle | sección interna | reference social implementation en anexo del Governance Profile |
| Licenciamiento | CC-BY-4.0 por defecto | matriz de licenciamiento diferenciada |
| Piloto | roadmap genérico | Pilot Profile austero de 6 páginas |

---

## Dependencia lógica entre documentos

El Core Standard es autosuficiente. El Governance Profile depende del Core. La Cultural Charter es independiente pero informa a ambos como documento de origen. El Threat Model y el Dispute Layer dependen de los tres anteriores. El Pilot Profile depende de los cinco anteriores y es un subconjunto operable. Los Extension Profiles dependen solo del Core.

```
                 Cultural Charter (03)
                       ↓ informa
              Core Standard (01)
                  ↓
        ┌─────────┼─────────┐
        ↓         ↓         ↓
  Governance  Ext. Profiles  Threat Model
     (02)      (EXT_*)        (04)
        ↓                     ↓
        └─────────┬───────────┘
                  ↓
            Dispute Layer (05)
                  ↓
          Pilot Profile (06)
```

---

## Madurez del set

Cada documento declara su propio estado. El consolidado a abril 2026 es:

| Documento | Estado | Revisión |
|---|---|---|
| 01 Core Standard | stable | requiere publicación de JSON Schema machine-readable para alcanzar candidato a v2 |
| 02 Governance Profile | stable | |
| 03 Cultural Charter | stable | |
| 04 Threat Model | draft | requiere ejercicio red-team antes del piloto |
| 05 Dispute Layer | draft | requiere primera prueba jurisdiccional real |
| 06 Pilot Profile Cochamó | draft | sujeto a adaptación durante ejecución |
| EXT_01 Normative Instrument | stable | |

"Stable" significa que el documento está cerrado para ajustes de diseño mayores. "Draft" significa que puede sufrir cambios estructurales antes del piloto.

---

## Principios editoriales del set

Los siete documentos comparten disciplina editorial:

1. **Palabras normativas**: DEBE, DEBERÍA, PUEDE, NO DEBE, NO DEBERÍA se usan en versalita y tienen el mismo significado que en RFC 2119.
2. **Enums**: todo valor controlado se declara explícitamente. No se admite valor implícito.
3. **Identificadores**: todos los identificadores internos siguen el formato `tkip-<ámbito>-<slug>` o similar declarado por documento.
4. **Ejemplos**: son marcados como informativos y no forman parte normativa del estándar.
5. **Referencias cruzadas**: se expresan como `[DOC:SECCIÓN]` (ejemplo: `[01:4.2]` = Core Standard sección 4.2).
6. **Versionado**: cada documento tiene versión propia. Un cambio en cualquiera de ellos incrementa la versión del conjunto solo si es un cambio compatible con la misma línea v1.x; cambios incompatibles producen v2.0.

---

## Licencias

- **Documentos** (01-06, EXT_*): CC-BY-4.0. Cualquier organización puede adoptar, adaptar y extender TKIP con atribución.
- **Implementaciones de referencia** (software): MIT.
- **Contenido ingestado mediante TKIP**: matriz de licenciamiento definida en el Core Standard, sección 9.

---

## Cómo contribuir a TKIP

TKIP se desarrolla como open standard. Cualquier organización que implemente TKIP DEBERÍA contribuir de vuelta sus extensiones, perfiles y aprendizajes a la especificación común. El proceso de contribución al estándar se documentará en v2 cuando exista un Consejo de Estándar propio, distinto del Consejo Curatorial de un territorio particular.

Hasta entonces, las contribuciones se canalizan vía el repositorio público del proyecto.

---

*Naveguemos la vanguardia.*
