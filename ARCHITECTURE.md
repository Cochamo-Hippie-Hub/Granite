# Architecture

→ [Leer en español](ARCHITECTURE.es.md)

Granite is organized in three layers. Each layer can be developed independently.
You don't need to understand the full stack to contribute to one part of it.

A wilderness landscape spanning hundreds of thousands of hectares across the Cochamó valley and cordillera,
15,000 visitors per season, one dirt road in, no mobile coverage beyond the trailhead.
Every technical decision starts there.

---

## Layer 1 — Field (data capture)

The wilderness layer. Hardware deployed in remote terrain with no reliable connectivity.

**Ecological sensors**
- Camera traps for wildlife detection and species identification
- Acoustic recorders for bird and amphibian monitoring
- Meteorological stations (temperature, rainfall, wind)
- Hydrological sensors (river flow, water quality)
- Trail erosion monitoring — sections of the main valley trail have eroded
  so deeply that hikers walk below ground level, accelerated by horse traffic

**Satellite monitoring**
- Sentinel-2 (ESA) — vegetation indices, land cover change
- Landsat 8/9 (NASA) — long-term ecosystem trends
- SAR radar — cloud-penetrating change detection

**Connectivity**
- Starlink at strategic base points
- LoRa networks for low-power sensor communication
- Store-and-forward protocols for intermittent connectivity zones

**Open problems in this layer**
- How do sensors in areas like Río Steffen (bordering Argentina, no road access)
  transmit data reliably?
- What is the minimum viable hardware kit for a new monitoring station that
  operates unattended for 3-6 months in Patagonian weather?
- How do we monitor trail erosion continuously without on-site presence?
- Can we automate detection of horse traffic impact on trail conditions?

---

## Layer 2 — Intelligence (analysis)

The processing layer. Algorithms that turn raw sensor data into actionable information.

**Species identification**
- Computer vision models for camera trap image classification
- Bioacoustic analysis for species detection from audio recordings
- Priority species: huemul deer, puma, pudú, endangered amphibians
- Note: no ML dataset exists for Cochamó wildlife — we need to build it from scratch.
  Camera trap images published by BBC and international media are a starting point.

**Environmental monitoring**
- Fire detection and vegetation change from satellite imagery
- Carbon stock estimation and biomass quantification
- Glacier and snowpack monitoring
- Trail erosion mapping from satellite and drone imagery

**Visitor analytics**
- Trail saturation modeling
- Visitor flow prediction and capacity management
- Identification of undervisited remote campsites to distribute pressure

**Open problems in this layer**
- How do we build a wildlife dataset for a territory where almost no species
  occurrence data exists?
- How do we run inference at the edge with solar power and limited compute?
- What satellite change-detection threshold triggers a human review?
- Can drone imagery automate trail condition assessment?

---

## Layer 3 — Management (operations)

The human layer. This is where technology meets the valley's real complexity:
arrieros, volunteers, local families, rangers, and thousands of visitors
navigating an enormous wilderness with almost no digital infrastructure.

### Reservations and carrying capacity

Today the valley has no unified online reservation system.
Five campsites manage bookings independently via email.
Carrying capacity is regulated manually — campsite owners communicate daily quotas
to a visitor center staffed by volunteers, who verify that every hiker entering
the valley has a printed reservation voucher.

It works. Barely. And it does not scale.

**What needs to be built**
- Unified online reservation system for all valley campsites
- Real-time carrying capacity dashboard for rangers and campsite owners
- Incentive mechanisms to distribute visitors toward remote campsites,
  supporting local economies in isolated areas
- Arriero booking system — today a single email address manages all
  mule train requests for the entire territory
- Cabalgata (horseback) capacity regulation and trail impact monitoring

**Open problems**
- How do we build a reservation system that works offline in the valley,
  where connectivity is intermittent?
- How do we design incentives that make remote campsites attractive
  without overloading fragile ecosystems?
- How do we integrate arriero schedules with visitor flow in real time?

### Safety and search and rescue

People have died in this territory. Hikers have been lost for days
in trails of medium-high difficulty surrounding the main campsites.
The upper circuits — La Junta, Lago Vidal Gormaz, Valle del Manso —
involve 1,000-meter elevation gain, multi-day routes, and no connectivity.

There is no system today that tracks where visitors are.

**What needs to be built**
- Visitor location tracking for multi-day backcountry routes
- Check-point verification system — automated confirmation that hikers
  on 5-6 day circuits have passed through designated points
- Search and rescue coordination tools for rangers
- Drone deployment protocols for emergency location

**Open problems**
- What is the minimum viable tracking solution for a hiker with no smartphone
  signal for 5 days?
- How do we design check-point verification without requiring infrastructure
  in roadless terrain?
- Can low-power beacons + LoRa provide sufficient location data for SAR?

### Territorial dashboard

**What needs to be built**
- Real-time map integrating sensor data, visitor location, weather, and alerts
- Incident reporting and ranger coordination
- Interface designed for rangers with limited technology experience

**Open problems**
- What does a dashboard look like for a park ranger who is not a tech user?
- How do we display complex multi-layer data without overwhelming the operator?

### Infrastructure and environmental management

The valley receives 15,000 visitors per season through a pristine ecosystem.
The physical infrastructure of conservation is as important as the digital.

**Open problems**
- Dry toilet management at remote campsites — waste handling in areas
  with no sanitation infrastructure
- Waste and recycling management for high-traffic backcountry zones
- Trail erosion monitoring and maintenance prioritization
- Scenic byway planning — a road section is planned through the territory.
  What can we learn from scenic byway management in California, Norway,
  or New Zealand that applies here?

### Community and culture

The valley is not empty. Families have lived in the cordillera for generations —
in La Herradura, in the high-altitude sectors, in communities that are
slowly disappearing. Arrieros are not logistics providers. They are the
living connection between the valley and its history.

**What needs to be built**
- Tools that support arriero coordination without replacing their role
- Volunteer program management — 1,500 applicants last season for
  a program that started with 3
- Cultural heritage documentation — oral history, traditional land use,
  local ecological knowledge
- Economic opportunity tools that keep young people in the valley

---

## Design principles

**Offline-first** — assume no connectivity. Sync when available.

**Low-power** — sensors run on solar and battery for months without maintenance.

**Modular** — each component works independently. You can deploy Layer 3
without Layer 1.

**Replicable** — every solution must be deployable by another protected area
with minimal adaptation. If it only works in Cochamó, we failed.

**Open data** — all biodiversity data collected through this system is
published under open licenses.

**Community-centered** — technology serves the people who live and work
in the territory. It does not replace them.

---

## The territory

132,876 hectares. 30% of the Cochamó municipality.
Granite walls rising 1,000 meters — among the largest on the planet,
surpassing El Capitan in Yosemite in height and complexity.

Home to huemul deer, puma, pudú, and thousands of undocumented species.
The first camera trap images of huemul in this territory were published
by the BBC and circled the globe.

15,000 visitors per season. One dirt road in.
No mobile coverage beyond the trailhead.
Muleteers on horseback as the primary logistics network.
Families living at 1,200 meters with almost no connection to the outside world.

This is the real-world constraint that drives every technical decision.

---

*If you see a problem here you know how to solve, open an Issue.*
