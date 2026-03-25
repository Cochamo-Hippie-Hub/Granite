# The Territory

→ [Leer en español](#el-territorio)

---

This document describes the real-world context that drives every technical decision
in Cochamó Hippie Hub. If you're thinking about contributing, this is the landscape
your code needs to survive in.

---

## The numbers

| | |
|---|---|
| **Location** | Cochamó municipality, Los Lagos Region, Chilean Patagonia |
| **Coordinates** | 41°30'S, 72°00'W |
| **Protected area** | 132,876 hectares (328,000+ acres) |
| **Primary forest** | 58,819 hectares — including ~11% of Earth's remaining alerce trees |
| **Glaciers** | 507 hectares |
| **Granite walls** | 1,000+ meters — among the tallest on the planet |
| **Visitors per season** | ~15,000 |
| **Mobile coverage** | None beyond the trailhead |
| **Road access** | One dirt road to the trailhead; 13 km trail on foot/horseback to the valley |

---

## What makes this territory unique

**Geology.** The granite domes of Cochamó rival Yosemite in height and quality —
crack systems, clean rock faces, and multi-pitch routes that attract climbers from
around the world. Cerro Trinidad, El Monstruo, and El Anfiteatro are world-class
big wall destinations.

**Forests.** The territory contains one of the largest remaining stands of alerce
(*Fitzroya cupressoides*), a conifer species that can live over 5,000 years. These
trees store more carbon per hectare than Amazonian rainforest. They are a Monumento
Natural under Chilean law.

**Biodiversity.** Camera trap monitoring has confirmed the presence of huemul deer
(*Hippocamelus bisulcus*) — Chile's national animal, critically endangered. The
population documented here may be the northernmost in Chilean Patagonia. Other
confirmed species include puma, pudú, vizcacha, and Darwin's frog.

**Water.** The territory feeds the Cochamó and Puelo river systems — pristine
watersheds that flow into the Reloncaví Fjord. The Puelo River was recently
granted official protection as an environmental flow reserve.

**Biological corridor.** The protected area connects 1.64 million hectares of
parks and reserves across Chile and Argentina, forming one of the most significant
biological corridors in South America.

---

## The operational reality

This is what any technology deployed here must deal with:

**No connectivity.** There is no cellular signal in the valley. Starlink at
strategic base points is the only current option for internet access. Any system
must work offline and sync when connectivity is available.

**Extreme weather.** Rainfall exceeds 4,000 mm/year in some sectors. Temperature
swings of 30°C in a single day are common. Snow, wind, and rain can arrive without
warning. Hardware must survive Patagonian conditions unattended for months.

**Access by horse or foot only.** The 13-kilometer trail from the road to the main
camping area (La Junta) is muddy, steep, and crosses multiple river fords. All
supplies — including any technology — must be carried in on horseback by arrieros.

**Multiple stakeholders.** The territory involves campsite operators, arrieros,
local families, volunteer programs (1,500 applicants last season), park rangers,
climbing communities, scientific researchers, and conservation organizations.
Any system must serve all of them without replacing any of them.

**Erosion.** Key trail sections have eroded so deeply that hikers walk below
ground level, accelerated by horse traffic during peak season. Monitoring and
managing trail conditions is a continuous challenge.

---

## The safety problem

People have died in this territory. Hikers have been lost for days on trails of
medium-high difficulty. The upper circuits — La Junta to Lago Vidal Gormaz, Valle
del Manso, the high-altitude crossings — involve 1,000-meter elevation gains,
multi-day routes, and zero connectivity.

There is currently no system that tracks where visitors are.

Climbers on the granite walls face additional risks: weather changes, route-finding
errors on descent, and the difficulty of rescue in roadless terrain. The territory
has no helicopter landing zone in the main valley.

This is the problem that drove the creation of the first CHH prototype: a climber
check-in/check-out system designed to work offline, with minimal infrastructure,
in a place where a smartphone is a brick.

---

## What this means for contributors

If you're writing code for this territory:

- **Assume no internet.** Design offline-first, sync later.
- **Assume no power grid.** Solar and battery for months.
- **Assume the user is not technical.** Rangers, arrieros, campsite operators.
- **Assume the hardware arrives on a horse.** Weight and durability matter.
- **Assume rain.** Everything gets wet eventually.

If your solution only works with a stable 4G connection and a React dashboard,
it won't survive the first week.

If it works on a Raspberry Pi with a solar panel and a LoRa antenna in a
waterproof case strapped to a mule — we're interested.

---

*The territory rules. Solutions must work in the real world, not just in the lab.*

---
---

# El territorio

Este documento describe el contexto real que impulsa cada decisión técnica en
Cochamó Hippie Hub. Si estás pensando en contribuir, este es el paisaje donde
tu código necesita sobrevivir.

---

## Los números

| | |
|---|---|
| **Ubicación** | Comuna de Cochamó, Región de Los Lagos, Patagonia chilena |
| **Coordenadas** | 41°30'S, 72°00'W |
| **Área protegida** | 132.876 hectáreas |
| **Bosque primario** | 58.819 hectáreas — incluyendo ~11% de los alerces del planeta |
| **Glaciares** | 507 hectáreas |
| **Murallas de granito** | 1.000+ metros — entre las más altas del planeta |
| **Visitantes por temporada** | ~15.000 |
| **Cobertura móvil** | Ninguna más allá del inicio del sendero |
| **Acceso vehicular** | Un camino de tierra hasta el trailhead; 13 km a pie/caballo al valle |

---

## Qué hace único a este territorio

**Geología.** Los domos de granito de Cochamó rivalizan con Yosemite en altura y
calidad — sistemas de fisuras, paredes de roca limpia y rutas de varios largos que
atraen escaladores de todo el mundo.

**Bosques.** El territorio contiene una de las mayores poblaciones remanentes de
alerce (*Fitzroya cupressoides*), una conífera que puede vivir más de 5.000 años.
Estos árboles almacenan más carbono por hectárea que la selva amazónica.

**Biodiversidad.** El monitoreo con cámaras trampa ha confirmado la presencia de
huemul (*Hippocamelus bisulcus*) — el animal nacional de Chile, en peligro crítico.

**Agua.** El territorio alimenta los sistemas fluviales del Cochamó y el Puelo —
cuencas prístinas que desembocan en el Fiordo Reloncaví.

**Corredor biológico.** El área protegida conecta 1,64 millones de hectáreas de
parques y reservas entre Chile y Argentina.

---

## La realidad operativa

**Sin conectividad.** No hay señal celular en el valle. Starlink en puntos base
estratégicos es la única opción actual de acceso a internet.

**Clima extremo.** Las precipitaciones superan los 4.000 mm/año en algunos sectores.
Variaciones de temperatura de 30°C en un solo día son comunes.

**Acceso solo a caballo o a pie.** El sendero de 13 kilómetros desde el camino
hasta La Junta es barroso, empinado y cruza múltiples vados. Todos los suministros
— incluida cualquier tecnología — deben ser transportados a caballo por arrieros.

**Múltiples actores.** El territorio involucra operadores de campings, arrieros,
familias locales, programas de voluntariado (1.500 postulantes la temporada pasada),
guardaparques, comunidades de escalada, investigadores científicos y organizaciones
de conservación. Cualquier sistema debe servir a todos sin reemplazar a ninguno.

**Erosión.** Secciones clave del sendero se han erosionado tan profundamente que
los caminantes descienden bajo el nivel del suelo, acelerado por el tráfico de
caballos en temporada alta.

---

## El problema de seguridad

Personas han muerto en este territorio. Excursionistas se han perdido durante días
en senderos de dificultad media-alta. Los circuitos altos implican desniveles de
1.000 metros, rutas de varios días y conectividad cero.

Actualmente no existe ningún sistema que rastree dónde están los visitantes.

Este es el problema que impulsó la creación del primer prototipo de CHH: un sistema
de check-in/check-out para escaladores diseñado para funcionar offline, con
infraestructura mínima, en un lugar donde un smartphone es un ladrillo.

---

## Qué significa esto para los contribuidores

Si estás escribiendo código para este territorio:

- **Asume que no hay internet.** Diseña offline-first, sincroniza después.
- **Asume que no hay red eléctrica.** Solar y batería durante meses.
- **Asume que el usuario no es técnico.** Guardaparques, arrieros, operadores de camping.
- **Asume que el hardware llega a caballo.** El peso y la durabilidad importan.
- **Asume lluvia.** Todo se moja eventualmente.

Si tu solución solo funciona con una conexión 4G estable y un dashboard en React,
no sobrevivirá la primera semana.

Si funciona en una Raspberry Pi con panel solar y una antena LoRa en un estuche
impermeable amarrado a una mula — nos interesa.

---

*El territorio manda. Las soluciones deben funcionar en el mundo real, no solo en el laboratorio.*
