# Repositorio de conocimiento territorial

→ [Read in English](#territorial-knowledge-repository)

---

Este directorio organiza todo el conocimiento generado sobre el territorio
protegido. Se estructura en dos ejes: **dominios** (qué es la información)
y **capas transversales** (cómo se describe y conecta la información).

Esta separación es el principio estructural del sistema. Si no se respeta,
el repositorio se rompe por duplicación.

---

## I. Dominios

### 1. Conservación y sistemas ecológicos
*Base científica y ecológica del territorio*

| Subcarpeta | Contenido |
|---|---|
| `1-conservacion/conocimiento/` | Geología, flora, fauna, hidrología, clima |
| `1-conservacion/monitoreo/` | Cámaras trampa, sensores, satélite, terreno |
| `1-conservacion/gestion-ecologica/` | Planes de manejo, restauración, especies prioritarias, invasoras |
| `1-conservacion/riesgos/` | Incendios, eventos climáticos, remociones, amenazas |

### 2. Gestión del área
*Cómo funciona el territorio en la práctica*

| Subcarpeta | Contenido |
|---|---|
| `2-gestion/gobernanza/` | Roles, protocolos, toma de decisiones |
| `2-gestion/seguridad/` | Rescate, evacuación, incidentes |
| `2-gestion/infraestructura/` | Senderos, puentes, sanitarios, señalética, conectividad |
| `2-gestion/uso-publico/` | Visitantes, reservas, capacidad de carga |
| `2-gestion/operacion/` | Guardaparques, voluntariado, logística diaria |

### 3. Actividades y recreación
*Cómo se vive el territorio*

| Subcarpeta | Contenido |
|---|---|
| `3-actividades/montana/` | Trekking, escalada, trail running |
| `3-actividades/ecuestres/` | Arriería, cabalgatas |
| `3-actividades/agua/` | Kayak, ríos, cruces |
| `3-actividades/cultura-acceso/` | Ética, Leave No Trace, comportamiento visitante |
| `3-actividades/info-practica/` | Rutas, topos, tiempos, dificultad |

### 4. Base territorial, normativa e institucional
*El soporte duro del sistema*

| Subcarpeta | Contenido |
|---|---|
| `4-territorio/cartografia/` | Mapas, límites, cuencas, capas GIS |
| `4-territorio/propiedad/` | Dominio, servidumbres, DRC, superposiciones |
| `4-territorio/normativa/` | Permisos, regulaciones, ordenanzas, legislación |
| `4-territorio/institucional/` | FCP, CPP, convenios, gobernanza formal |

### 5. Comunidad, historia y patrimonio
*Dimensión humana y cultural*

| Subcarpeta | Contenido |
|---|---|
| `5-comunidad/habitantes/` | Familias, arrieros, residentes |
| `5-comunidad/practicas/` | Uso del territorio, tradiciones productivas |
| `5-comunidad/historia/` | Ocupación, relatos, hitos |
| `5-comunidad/patrimonio/` | Arqueología, rutas históricas, cultura material |

### 6. Economía territorial

| Subcarpeta | Contenido |
|---|---|
| `6-economia/servicios/` | Campings, arrieros, guías |
| `6-economia/turismo/` | Flujo, demanda, comportamiento |
| `6-economia/productivas/` | Actividades productivas compatibles, uso sustentable |
| `6-economia/financiamiento/` | Endowment, ingresos, tarifas |

---

## II. Capas transversales

Cada pieza de información debe llevar estos metadatos. Son las capas
que convierten el repositorio en un sistema inteligente.

| Capa | Qué describe | Valores posibles |
|---|---|---|
| **A. Ubicación** | Dónde ocurre | Coordenadas, polígono, ruta, punto, sector, cuenca, predio |
| **B. Escala** | A qué nivel aplica | Sitio puntual, sendero, sector, valle, cuenca, territorio completo |
| **C. Temporalidad** | Cuándo | Fecha específica, período, histórico, estado actual, proyección |
| **D. Fuente** | De dónde viene | Documento técnico, terreno, sensor, comunidad, institución, publicación |
| **E. Actor** | Quién está involucrado | Visitante, habitante, operador, institución, investigador |
| **F. Tipo de contenido** | Qué formato tiene | Mapa, informe, ficha, imagen, audio, video, dataset, norma |
| **G. Validación** | Qué tan confiable es | Validado técnico, validado comunitario, no validado, en revisión |

### Implementación en GitHub

Las capas se implementan como YAML frontmatter en el `README.md` de cada
contribución:

```yaml
---
ubicacion: Anfiteatro, confluencia Río La Junta
coordenadas: "-41.50, -72.00"
escala: sector
temporalidad: 2026-01-15 / 2026-02-28
fuente: publicacion-cientifica
actor: investigador
tipo: dataset
validacion: validado-tecnico
---
```

---

## III. Reglas de diseño

**1. Una pieza, un lugar en el árbol.**
Un contenido puede pertenecer a múltiples dominios conceptualmente.
Se resuelve con capas, no duplicando archivos.

**2. El árbol no crece hacia los lados.**
Evitar subcategorías infinitas. El crecimiento ocurre en metadatos,
no en carpetas.

**3. Primero ubicación, después contenido.**
En un repositorio territorial, lo espacial manda. Todo debe poder mapearse.

**4. Distinguir entre:**
- estructura del territorio (dominio 4)
- uso del territorio (dominios 2, 3, 6)
- conocimiento del territorio (dominios 1, 5)

**5. No todo es "ciencia".**
El conocimiento de terreno — arrieros, rutas, historia — es estructural,
no anecdótico.

---

## Cómo contribuir

1. Identifica el dominio y subcarpeta correspondiente
2. Crea una carpeta con nombre descriptivo
3. Incluye un `README.md` con el frontmatter YAML de las 7 capas
4. Envía un Pull Request o escribe a cochamohippiehub@gmail.com

---

## Cómo acceder

Todo el contenido es público y gratuito. Navega las carpetas en GitHub,
descarga con ZIP, o clona con Git.

---

## Licencia

Salvo indicación contraria, todo el contenido se publica bajo
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
