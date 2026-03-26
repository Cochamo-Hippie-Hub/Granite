# Monitoreo

Datos de monitoreo continuo del territorio: cámaras trampa, imágenes
satelitales, estaciones meteorológicas y estado de senderos.

## Subcarpetas

| Carpeta | Contenido |
|---|---|
| `camaras-trampa/` | Imágenes y registros de cámaras trampa, identificación de especies, metadata |
| `satelital/` | Índices de vegetación (NDVI), cambio de uso de suelo, detección de perturbaciones |
| `meteorologia/` | Datos de temperatura, precipitación, viento, humedad por estación |
| `senderos/` | Registro de estado de senderos, puntos de erosión, necesidades de mantención |

## Cómo contribuir

**Cámaras trampa:** Crea carpeta por estación (`camaras-trampa/estacion-nombre-AAAA/`), incluye README con ubicación, modelo de cámara, período. Imágenes nombradas `AAAA-MM-DD_HHMM_especie.jpg`. Incluye `registro.csv` con fecha, hora, especie, individuos, comportamiento. Conjuntos >100 MB en Zenodo.

**Datos satelitales:** Indica fuente (Sentinel-2, Landsat, SAR), fechas, resolución. Incluye scripts de procesamiento si los hay.

**Meteorología:** CSV con columnas: fecha (ISO 8601), variable, valor, unidad, estacion.

**Senderos:** Reportes con fecha, sector, tipo de problema, fotografías, coordenadas GPS.
