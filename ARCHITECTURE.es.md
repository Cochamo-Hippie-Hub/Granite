# Arquitectura

→ [Read in English](ARCHITECTURE.md)

Granite se organiza en tres capas. Cada capa puede desarrollarse de forma independiente.
No necesitas entender el stack completo para contribuir a una parte de él.

El territorio es la restricción. Un paisaje silvestre que abarca cientos de miles de
hectáreas a lo largo del valle y la cordillera de Cochamó. 15.000 visitantes por
temporada, un camino de tierra de acceso, sin cobertura móvil más allá del inicio
del sendero. Cada decisión técnica parte desde ahí.

---

## Capa 1 — Terreno (captura de datos)

La capa silvestre. Hardware desplegado en terreno remoto sin conectividad confiable.

**Sensores ecológicos**
- Cámaras trampa para detección de fauna e identificación de especies
- Grabadores acústicos para monitoreo de aves y anfibios
- Estaciones meteorológicas (temperatura, lluvia, viento)
- Sensores hidrológicos (caudal, calidad del agua)
- Monitoreo de erosión de senderos — hay sectores del camino principal donde
  los caminantes van por debajo del nivel del suelo, acelerado por el tráfico de caballos

**Monitoreo satelital**
- Sentinel-2 (ESA) — índices de vegetación, cambios de cobertura
- Landsat 8/9 (NASA) — tendencias de largo plazo del ecosistema
- Radar SAR — detección de cambios con penetración de nubes

**Conectividad**
- Starlink en puntos estratégicos de base
- Redes LoRa para comunicación de sensores de bajo consumo
- Protocolos store-and-forward para zonas de conectividad intermitente

**Problemas abiertos en esta capa**
- ¿Cómo transmiten datos sensores en zonas como Río Steffen, en el límite con Argentina,
  sin acceso por camino?
- ¿Cuál es el kit de hardware mínimo viable para una estación de monitoreo que opere
  de forma autónoma por 3 a 6 meses en clima patagónico?
- ¿Cómo monitoreamos la erosión del sendero sin presencia en terreno?
- ¿Podemos automatizar la detección del impacto del tráfico de caballos en los senderos?

---

## Capa 2 — Inteligencia (análisis)

La capa de procesamiento. Algoritmos que convierten datos brutos de sensores
en información accionable.

**Identificación de especies**
- Modelos de visión computacional para clasificación de imágenes de cámaras trampa
- Análisis bioacústico para detección de especies desde grabaciones de audio
- Especies prioritarias: huemul, puma, pudú, anfibios en peligro
- Nota: no existe dataset de fauna de Cochamó — hay que construirlo desde cero.
  Las imágenes de cámaras trampa publicadas por la BBC son un punto de partida.

**Monitoreo ambiental**
- Detección de incendios y cambios de vegetación desde imágenes satelitales
- Estimación de stock de carbono y cuantificación de biomasa
- Monitoreo de glaciares y manto de nieve
- Mapeo de erosión de senderos desde imágenes satelitales y drones

**Analítica de visitantes**
- Modelamiento de saturación de senderos
- Predicción de flujos de visitantes y gestión de capacidad de carga
- Identificación de camping remotos subvisitados para distribuir la presión

**Problemas abiertos en esta capa**
- ¿Cómo construimos un dataset de fauna para un territorio donde casi no existen
  datos de ocurrencia de especies?
- ¿Cómo corremos modelos de IA en el borde de la red con energía solar y cómputo limitado?
- ¿Qué umbral de cambio satelital dispara una revisión humana?
- ¿Puede un drone automatizar la evaluación del estado de los senderos?

---

## Capa 3 — Gestión (operaciones)

La capa humana. Aquí la tecnología se encuentra con la complejidad real del valle:
arrieros, voluntarios, familias locales, guardaparques y miles de visitantes
navegando una enorme área silvestre con casi ninguna infraestructura digital.

### Reservas y capacidad de carga

El valle no tiene un sistema de reservas online unificado.
Cinco camping gestionan reservas de forma independiente por correo electrónico.
La capacidad de carga se regula manualmente — los dueños de camping comunican
cuotas diarias a un centro de visitantes atendido por voluntarios, que verifican
que cada caminante que entra al valle tenga su comprobante impreso.

Funciona. Apenas. Y no escala.

**Lo que hay que construir**
- Sistema de reservas online unificado para todos los camping del valle
- Dashboard de capacidad de carga en tiempo real para guardaparques y camping
- Mecanismos de incentivo para distribuir visitantes hacia camping remotos,
  apoyando economías locales en sectores aislados
- Sistema de reservas para arrieros — hoy un solo correo electrónico gestiona
  todas las solicitudes de mulas del territorio
- Regulación de capacidad de cabalgatas y monitoreo de impacto en senderos

**Problemas abiertos**
- ¿Cómo construimos un sistema de reservas que funcione sin conectividad en el valle,
  donde la señal es intermitente?
- ¿Cómo diseñamos incentivos que hagan atractivos los camping remotos
  sin sobrecargar ecosistemas frágiles?
- ¿Cómo integramos los horarios de los arrieros con el flujo de visitantes en tiempo real?

### Seguridad y búsqueda y rescate

Personas han muerto en este territorio. Caminantes se han perdido por días
en senderos de dificultad media-alta alrededor de los camping principales.
Los circuitos altos — La Junta, Lago Vidal Gormaz, Valle del Manso —
involucran 1.000 metros de desnivel, rutas de varios días y sin conectividad.

Hoy no existe ningún sistema que rastree dónde están los visitantes.

**Lo que hay que construir**
- Rastreo de ubicación de visitantes en rutas de varios días en la cordillera
- Sistema de verificación en puntos de control — confirmación automatizada
  de que caminantes en circuitos de 5 a 6 días han pasado por puntos designados
- Herramientas de coordinación de búsqueda y rescate para guardaparques
- Protocolos de despliegue de drones para localización de emergencia

**Problemas abiertos**
- ¿Cuál es la solución de rastreo mínima viable para un caminante sin señal
  de smartphone por 5 días?
- ¿Cómo diseñamos verificación en puntos de control sin infraestructura
  en terreno sin caminos?
- ¿Pueden balizas de bajo consumo con LoRa proveer datos de ubicación
  suficientes para búsqueda y rescate?

### Dashboard territorial

**Lo que hay que construir**
- Mapa en tiempo real integrando datos de sensores, ubicación de visitantes,
  clima y alertas
- Reporte de incidentes y coordinación de guardaparques
- Interfaz diseñada para guardaparques con experiencia tecnológica limitada

**Problemas abiertos**
- ¿Cómo se ve un dashboard para un guardaparque que no es usuario tech?
- ¿Cómo desplegamos datos complejos de múltiples capas sin abrumar al operador?

### Infraestructura y gestión ambiental

El valle recibe 15.000 visitantes por temporada en un ecosistema prístino.
La infraestructura física de la conservación es tan importante como la digital.

**Problemas abiertos**
- Gestión de baños secos en camping remotos — manejo de residuos en zonas
  sin infraestructura sanitaria
- Gestión de residuos y reciclaje en zonas de alta frecuentación
- Monitoreo y priorización de mantenimiento de erosión de senderos
- Planificación de ruta escénica — hay un tramo vial proyectado dentro del territorio.
  ¿Qué podemos aprender de la gestión de rutas escénicas en California, Noruega
  o Nueva Zelanda que aplique aquí?

### Comunidad y cultura

El valle no está vacío. Familias han vivido en la cordillera por generaciones —
en La Herradura, en los sectores de altura, en comunidades que se apagan lentamente.
Los arrieros no son proveedores logísticos. Son la conexión viva entre el valle
y su historia.

**Lo que hay que construir**
- Herramientas que apoyen la coordinación de arrieros sin reemplazar su rol
- Gestión del programa de voluntarios — 1.500 postulantes la temporada pasada
  para un programa que partió con 3 personas
- Documentación del patrimonio cultural — historia oral, uso tradicional del territorio,
  conocimiento ecológico local
- Herramientas de oportunidad económica que mantengan a los jóvenes en el valle

---

## Principios de diseño

**Offline-first** — asumir que no hay conectividad. Sincronizar cuando esté disponible.

**Bajo consumo** — los sensores funcionan con solar y batería por meses sin mantenimiento.

**Modular** — cada componente funciona de forma independiente. Puedes desplegar
la Capa 3 sin la Capa 1.

**Replicable** — cada solución debe poder ser desplegada por otra área protegida
con mínima adaptación. Si solo funciona en Cochamó, fallamos.

**Datos abiertos** — todos los datos de biodiversidad recopilados por este sistema
se publican bajo licencias abiertas.

**Centrado en la comunidad** — la tecnología sirve a las personas que viven y trabajan
en el territorio. No las reemplaza.

---

## El territorio

Un paisaje silvestre que abarca cientos de miles de hectáreas a lo largo del
valle y la cordillera de Cochamó. Murallas de granito de hasta 1.000 metros —
entre las más grandes del planeta, superando en altura y complejidad al Capitán
en Yosemite.

Hogar del huemul, el puma, el pudú y miles de especies no documentadas.
Las primeras imágenes de huemul con cámara trampa en este territorio
fueron publicadas por la BBC y recorrieron el mundo.

15.000 visitantes por temporada. Un camino de tierra de acceso.
Sin cobertura móvil más allá del inicio del sendero.
Arrieros a caballo como red logística principal.
Familias viviendo a 1.200 metros de altura con casi ninguna conexión con el exterior.

Esta es la restricción del mundo real que impulsa cada decisión técnica.

---

*Si ves un problema aquí que sabes cómo resolver, abre un Issue.*
