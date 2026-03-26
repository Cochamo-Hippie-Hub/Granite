# Repositorio de conocimiento territorial

→ [Read in English](#territorial-knowledge-repository)

---

Este directorio es el corazón de Granite. Aquí se almacena, organiza y comparte
todo el conocimiento generado sobre el territorio protegido: investigaciones
científicas, registros de biodiversidad, protocolos de seguridad, rutas deportivas,
normativas, datos de monitoreo y memoria comunitaria.

Cada carpeta corresponde a un dominio temático de la gestión territorial.
Cada dominio tiene su propio `README.md` que explica qué contiene, cómo
contribuir información y cómo acceder a lo que ya existe.

---

## Dominios temáticos

| Dominio | Carpeta | Qué contiene |
|---|---|---|
| **Administración** | `administracion/` | Gobernanza, organigramas, reglamentos internos, políticas operativas |
| **Ciencia** | `ciencia/` | Investigaciones, expediciones, datasets, publicaciones científicas |
| **Conservación** | `conservacion/` | Planes de manejo, restauración, especies prioritarias e invasoras, incendios |
| **Monitoreo** | `monitoreo/` | Cámaras trampa, imágenes satelitales, datos meteorológicos, estado de senderos |
| **Deportes y recreación** | `deportes-recreacion/` | Escalada, trekking, cabalgatas, trail running, kayak, protocolos por actividad |
| **Seguridad** | `seguridad/` | Protocolos de emergencia, rescate, gestión de riesgo, zonas de peligro |
| **Legal** | `legal/` | Propiedad, Derecho Real de Conservación, permisos, normativa ambiental, convenios |
| **Comunidad** | `comunidad/` | Familias locales, arrieros, pueblos originarios, desarrollo económico, participación |
| **Patrimonio** | `patrimonio/` | Historia oral, conocimiento tradicional, sitios arqueológicos, rutas históricas |
| **Infraestructura** | `infraestructura/` | Senderos, señalética, saneamiento, conectividad, energía, edificaciones |
| **Visitantes** | `visitantes/` | Educación ambiental, capacidad de carga, reservas, interpretación, voluntariado |
| **Territorio** | `territorio/` | Cartografía, límites, uso de suelo, cuencas hidrográficas, zonificación |

---

## Cómo contribuir información

Cualquier persona puede aportar datos, documentos o conocimiento a este repositorio.
El proceso es el mismo para todos los dominios:

**Opción 1 — Desde GitHub (recomendada)**

1. Haz un fork de este repositorio
2. Agrega tu material en la carpeta correspondiente
3. Incluye un archivo `README.md` que describa: qué es, quién lo generó, cuándo, bajo qué licencia
4. Envía un Pull Request

**Opción 2 — Por email**

Si no usas GitHub, envía tu material a cochamohippiehub@gmail.com indicando:
- Qué es el material
- Quién lo generó
- Si autorizas su publicación bajo licencia abierta

Un administrador lo subirá al repositorio con los créditos correspondientes.

---

## Cómo acceder a la información

Todo el contenido de este repositorio es público y gratuito.

- **Navegar online:** entra a cualquier carpeta desde GitHub y lee los archivos directamente
- **Descargar todo:** clic en "Code → Download ZIP" en la página principal del repositorio
- **Clonar con Git:** `git clone https://github.com/Cochamo-Hippie-Hub/Granite.git`
- **Citar:** cada carpeta indica la autoría y licencia de sus contenidos

---

## Estándares de formato

Para mantener la información accesible y duradera:

- **Texto:** Markdown (`.md`) como formato principal. Evitar formatos propietarios
- **Datos tabulares:** CSV (`.csv`) con encabezados descriptivos
- **Imágenes:** JPEG o PNG. Máximo 10 MB por archivo en GitHub. Para conjuntos grandes, usar links externos
- **Datos geoespaciales:** GeoJSON (`.geojson`) cuando sea posible. Shapefiles en carpeta comprimida
- **Archivos pesados (>100 MB):** subir a Zenodo u otro repositorio científico y enlazar desde aquí
- **Idioma:** español o inglés. Ambos son bienvenidos

---

## Estructura de una contribución tipo

Cuando deposites información, sigue este modelo:

```
ciencia/geologia/nombre-del-estudio/
├── README.md          ← descripción del estudio, autores, fecha, licencia
├── datos/             ← archivos de datos (CSV, GeoJSON, imágenes)
├── resultados/        ← figuras, mapas, modelos
└── publicacion.pdf    ← artículo o informe si existe (o link externo)
```

El `README.md` de cada contribución es obligatorio. Es lo que permite que otra
persona entienda qué hay en la carpeta sin tener que abrir cada archivo.

---

## Licencia

Salvo indicación contraria de los autores, todo el contenido de este directorio
se publica bajo [Creative Commons Attribution 4.0 (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

Los autores pueden especificar una licencia diferente para sus contribuciones
indicándolo en el `README.md` de su carpeta.
