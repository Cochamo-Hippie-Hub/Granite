# Check-in / Check-out — Visitor Safety Prototype

→ [Leer en español](#prototipo-de-seguridad-check-in--check-out)

---

## Why this exists

At the entrance to the Cochamó Valley there is a Visitor Center — a small
building at the end of the road, where the 13-kilometer trail into the valley
begins. It is staffed by volunteers from the Organización del Valle de Cochamó
(OVC) and operates a paper-based registry where every visitor must sign in
before entering.

That registry is the only record of who is inside the valley at any given time.

The problem is not the registry itself. The problem is that it exists in
isolation. Today, five independent systems operate in the valley without
talking to each other:

1. **The paper registry** at the Visitor Center — records who enters, but
   has no connection to campsite availability or return tracking.

2. **Five independent campsites** — each manages its own reservations
   separately (email, individual websites). There is no unified view of
   total carrying capacity across the valley.

3. **The arrieros organization** — muleteers who transport gear and people
   by horseback operate through a single email address. No booking system,
   no capacity management.

4. **The Santuario de la Naturaleza** (~3,000 ha on the north side of the
   Cochamó River) — administered by the OVC, with its own access needs.

5. **The conservation territory** (132,876 ha on the south side) — the protected
   landscape that needs visitor data for safety and management but has no
   digital connection to the Visitor Center.

The result: no one has a complete picture. A visitor can enter the valley,
hike for five days into a remote circuit with zero connectivity, and if
they don't come back, the search starts late because the paper registry
doesn't trigger alerts and the campsites don't know who was expected where.

People have died in this territory under these conditions.

---

## What this prototype demonstrates

This is **not** the final system. This is a proof of concept — a working
demonstration that the first piece of the puzzle (digital visitor registration
with overdue alerts) can be built with:

- **Zero infrastructure.** A single HTML file. No server, no database,
  no build step, no dependencies.
- **Offline-first design.** Works without internet — essential for a
  Visitor Center that has electricity but only intermittent connectivity.
- **Bilingual interface.** Spanish and English, switchable with one click —
  because half the visitors are international climbers.
- **Radical simplicity.** A volunteer with no technical training can
  operate it in minutes.

The prototype proves that the design principles described in
[ARCHITECTURE.md](../../ARCHITECTURE.md) work in practice. If we can build
a safety registry this way, we can build the rest the same way.

---

## What the full system needs to become

The real solution is a **unified access management platform** — a single
digital point of control at the Visitor Center that coordinates all five
systems described above:

**Module 1 — Visitor registry (this prototype).** Digital check-in replacing
the paper logbook. Name, nationality, group size, destination, expected return,
emergency contact. Overdue alerts. Export for backup and reporting.

**Module 2 — Campsite availability.** Real-time view of capacity across all
five campsites. Visitors see where there's space before entering the valley.
Campsite operators update availability from their end (even offline, syncing
when connectivity is available).

**Module 3 — Arriero booking.** Availability calendar for the arrieros
organization. Visitors or the Visitor Center volunteer can check mule
availability and request transport — replacing the single-email system.

**Module 4 — Horseback ride capacity.** Daily quotas for cabalgatas,
coordinated with trail impact monitoring.

**Module 5 — Data feed for OVC and Conserva Pucheguín.** Aggregated
visitor statistics, safety alerts, and carrying capacity data shared
with the organizations that administer the territory — without requiring
those organizations to operate the system themselves.

Each module follows the same design principles: offline-first, single-file
deployable, bilingual, zero dependencies, operable by non-technical users.

---

## How CHH builds this

This is an open-source project. The code is MIT-licensed. Anyone can
contribute, fork, adapt, or deploy it.

But "anyone can contribute" is not just a license statement. It is the
core operating model of Cochamó Hippie Hub:

- **The problems are real.** They come from a decade of work in the territory,
  not from a whiteboard. Every Issue in this repository describes something
  that someone in the valley actually needs.

- **The territory is the client.** Not a company, not a board of directors.
  The people who live, work, and visit this valley — arrieros, campsite
  operators, volunteers, climbers, families, rangers — they define what
  gets built.

- **The code belongs to everyone.** A developer in Berlin who knows offline
  sync can solve a problem for a volunteer in Cochamó who has never written
  a line of code. That connection is what open source is for.

- **No one needs permission to start.** See a problem? Open an Issue.
  Have a solution? Open a Pull Request. The conversation is open.

This prototype exists to prove that this model works — that a small,
open, collaborative effort can produce tools that solve real problems
in real territories.

If it works here, it can work in any protected area in the world facing
the same challenges.

---

## Try it

Open `checkin.html` in any browser. Register a visitor. Check the dashboard.
Mark them as returned. Export the data. Switch languages. Turn off your wifi
and confirm it still works.

That's the whole point.

---

## Contributing

If you have experience with any of these, we want to hear from you:

- Offline-first sync (CRDTs, PouchDB, service workers)
- Reservation systems for low-connectivity environments
- Multi-stakeholder coordination platforms
- LoRa mesh networking for visitor tracking
- UX design for non-technical operators

Open an [Issue](https://github.com/Cochamo-Hippie-Hub/Granite/issues) or
read [CONTRIBUTING.md](../../CONTRIBUTING.md).

---
---

# Prototipo de seguridad: check-in / check-out

## Por qué existe esto

En la entrada al Valle de Cochamó hay un Centro de Visitantes — una construcción
al final del camino vehicular, donde comienza el sendero de 13 kilómetros hacia
el valle. Está operado por voluntarios de la Organización del Valle de Cochamó
(OVC) y mantiene un registro en papel donde cada visitante debe anotarse antes
de entrar.

Ese registro es el único documento de quién está dentro del valle en un momento
dado.

El problema no es el registro en sí. El problema es que existe aislado. Hoy,
cinco sistemas operan en el valle sin comunicarse entre sí:

1. **El registro en papel** del Centro de Visitantes — anota quién entra, pero
   no se conecta con la disponibilidad de campings ni con el seguimiento de retorno.

2. **Cinco campings independientes** — cada uno gestiona sus reservas por separado.
   No hay una vista unificada de la capacidad de carga total del valle.

3. **La organización de arrieros** — gestionan todo con un solo correo electrónico.
   Sin sistema de reservas ni control de capacidad.

4. **El Santuario de la Naturaleza** (~3.000 ha en el lado norte del río Cochamó)
   — administrado por la OVC, con sus propias necesidades de acceso.

5. **El territorio de conservación** (132.876 ha en el lado sur) — el paisaje
   protegido que necesita datos de visitantes para seguridad y gestión pero
   no tiene conexión digital con el Centro de Visitantes.

Personas han muerto en este territorio bajo estas condiciones.

---

## Qué demuestra este prototipo

Esto **no** es el sistema final. Es una prueba de concepto — una demostración
funcional de que la primera pieza del rompecabezas (registro digital de
visitantes con alertas de atraso) se puede construir con:

- **Cero infraestructura.** Un solo archivo HTML. Sin servidor, sin base de
  datos, sin dependencias.
- **Diseño offline-first.** Funciona sin internet — esencial para un Centro
  de Visitantes que tiene electricidad pero conectividad intermitente.
- **Interfaz bilingüe.** Español e inglés, intercambiable con un click.
- **Simplicidad radical.** Un voluntario sin formación técnica puede operarlo
  en minutos.

---

## En qué debe convertirse el sistema completo

La solución real es una **plataforma unificada de gestión de acceso** — un punto
de control digital único en el Centro de Visitantes que coordine los cinco
sistemas descritos arriba: registro de seguridad, disponibilidad de campings,
reserva de arrieros, capacidad de cabalgatas y datos para OVC y Conserva Pucheguín.

Cada módulo sigue los mismos principios de diseño: offline-first, desplegable
en un solo archivo, bilingüe, sin dependencias, operable por usuarios no técnicos.

---

## Cómo construye esto CHH

Este es un proyecto open source. El código tiene licencia MIT. Cualquiera puede
contribuir, bifurcar, adaptar o desplegarlo.

Pero "cualquiera puede contribuir" no es solo una declaración de licencia. Es el
modelo operativo central de Cochamó Hippie Hub:

- **Los problemas son reales.** Vienen de una década de trabajo en el territorio.
  Cada Issue en este repositorio describe algo que alguien en el valle necesita.

- **El territorio es el cliente.** No una empresa, no un directorio. Las personas
  que viven, trabajan y visitan este valle — arrieros, operadores de camping,
  voluntarios, escaladores, familias, guardaparques — ellos definen qué se construye.

- **El código es de todos.** Un desarrollador en Berlín que sabe de sincronización
  offline puede resolver un problema para un voluntario en Cochamó que nunca ha
  escrito una línea de código. Esa conexión es para lo que existe el open source.

- **Nadie necesita pedir permiso para empezar.** ¿Ves un problema? Abre un
  Issue. ¿Tienes una solución? Abre un Pull Request. La conversación es abierta.

Si funciona aquí, puede funcionar en cualquier área protegida del mundo que
enfrente los mismos desafíos.

---

## Pruébalo

Abre `checkin.html` en cualquier navegador. Registra un visitante. Revisa el
dashboard. Márcalo como retornado. Exporta los datos. Cambia de idioma. Apaga
tu wifi y confirma que sigue funcionando.

Ese es todo el punto.

---

*Naveguemos la vanguardia.*
