# Check-in / Check-out — Climber Safety System

→ [Leer en español](#sistema-de-seguridad-check-in--check-out)

---

The first operational tool from Cochamó Hippie Hub.

## The problem

There is no system today that tracks where visitors are in the Cochamó Valley.
Hikers on multi-day backcountry routes disappear from all communication for days.
People have died. Search and rescue operations start late because no one knows
who is missing or where they were heading.

## The solution

A dead-simple check-in/check-out system designed for the operational reality
of the territory:

- **Offline-first.** Works without internet. All data stored locally.
- **Single HTML file.** No server, no build step, no dependencies.
- **Runs on any device.** Phone, tablet, or laptop at the trailhead.
- **Bilingual.** Spanish and English interface.
- **Overdue alerts.** Visual indicators for visitors who haven't checked out on time.
- **Export capability.** Download records as JSON for backup or sync.

## How it works

1. A ranger or campsite operator opens `checkin.html` on any device
2. When a visitor enters the valley, they register: name, group size,
   destination, expected return date
3. When the visitor returns, the operator marks them as checked out
4. The dashboard shows who is currently in the valley and who is overdue
5. Records persist across browser sessions via localStorage

## Deployment

Copy `checkin.html` to any device. Open in a browser. That's it.

## Limitations

This is a prototype — v0.1. Known limitations:

- Single-device storage (no sync between devices yet)
- No LoRa integration (planned for v0.2)
- No checkpoint verification for multi-day routes (planned)
- No SAR coordination features (planned)

See [ARCHITECTURE.md](../../ARCHITECTURE.md) for the full vision of the
safety layer and open problems waiting to be solved.

---

# Sistema de seguridad: check-in / check-out

La primera herramienta operativa de Cochamó Hippie Hub.

Un sistema de check-in/check-out extremadamente simple:

- **Offline-first.** Funciona sin internet. Datos almacenados localmente.
- **Un solo archivo HTML.** Sin servidor, sin build, sin dependencias.
- **Funciona en cualquier dispositivo.** Teléfono, tablet o laptop en el trailhead.
- **Bilingüe.** Interfaz en español e inglés.
- **Alertas de atraso.** Indicadores visuales para visitantes atrasados.
- **Exportación.** Descarga registros como JSON para respaldo o sincronización.

## Despliegue

Copiar `checkin.html` a cualquier dispositivo. Abrir en un navegador. Eso es todo.

---

*El territorio manda. Las soluciones deben funcionar en el mundo real.*
