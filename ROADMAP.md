# Roadmap: Sistema unificado de acceso al Valle de Cochamó

→ [Read in English](#roadmap-unified-access-system-for-the-cochamó-valley)

---

El primer proyecto operativo de Cochamó Hippie Hub: reemplazar los cinco
sistemas desconectados que hoy gestionan el acceso al valle por una
plataforma digital unificada, abierta y sin propietario.

**Deadline inamovible:** diciembre 2026 (inicio de temporada de visitantes).

---

## Fase 1 — Escuchar (abril – mayo 2026)

Antes de escribir una línea de código, escuchar a cada actor del valle
para documentar exactamente qué necesita.

### Reuniones con directivos OVC (semana 1-2)
- Entender el flujo actual del Centro de Visitantes
- Documentar qué datos registran hoy en papel
- Identificar qué información necesitan que hoy no tienen
- Preguntar: ¿qué haría su trabajo más fácil?
- **Entregable:** Issue en Granite con necesidades OVC

### Reuniones con operadores de camping (semana 2-4)
- Visitar o contactar a cada uno de los cinco campings
- Entender cómo gestionan reservas hoy (email, web, teléfono)
- Preguntar qué información comparten con el Centro de Visitantes
- Identificar resistencias: ¿qué temen perder con un sistema unificado?
- Preguntar: ¿usarían un sistema si fuera gratis, simple y no les quitara autonomía?
- **Entregable:** Issue en Granite con necesidades de campings

### Reuniones con dirigentes de arrieros (semana 3-4)
- Documentar cómo funciona hoy el correo único de solicitudes
- Entender cuántas solicitudes reciben por temporada
- Preguntar qué información necesitarían ver (calendario, solicitudes pendientes)
- **Entregable:** Issue en Granite con necesidades de arrieros

### Documento de necesidades (semana 5-6)
- Consolidar los tres Issues en un documento de requisitos
- Publicar en Granite como especificación abierta
- Compartir con todos los actores para validación
- **Entregable:** `docs/requisitos-sistema-acceso.md` en Granite

---

## Fase 2 — Diseñar (junio 2026)

Traducir las necesidades en arquitectura técnica.

### Modelo de datos (semana 7-8)
- Definir qué información se comparte entre todos (registro, alertas)
- Definir qué información es privada de cada actor (notas internas, datos de contacto)
- Diseñar el esquema JSON que sincroniza entre dispositivos
- **Entregable:** `docs/modelo-datos.md` en Granite

### Diseño de vistas por rol (semana 9-10)
- Centro de Visitantes: ve todo (registro + campings + arrieros + alertas)
- Camping individual: ve solo su capacidad y sus reservas
- Arrieros: ven solo solicitudes de transporte y calendario
- Conservation management: dashboard de lectura con estadísticas agregadas
- **Entregable:** mockups simples publicados como Issue en Granite

### Validación con actores (semana 11)
- Presentar los mockups a OVC, campings y arrieros
- Recoger feedback antes de construir
- Ajustar diseño según feedback
- **Entregable:** Issue cerrado con aprobación de los actores

---

## Fase 3 — Construir (julio – septiembre 2026)

Desarrollo iterativo. Cada versión es funcional y desplegable.

### v0.2 — Sincronización + roles (semana 12-15)
- Agregar Service Worker para sync offline/online
- Implementar selector de rol al inicio ("¿Quién eres?")
- Backend mínimo: archivo JSON en servidor gratuito (Firebase/Supabase/GitHub)
- Cuando hay internet: envía datos nuevos, descarga datos de los demás
- Cuando no hay internet: funciona igual que v0.1, acumula y sincroniza después
- **Entregable:** checkin.html v0.2 con sync funcional

### v0.3 — Módulo de campings (semana 16-18)
- Vista para operadores de camping: marcar capacidad disponible
- Vista para Centro de Visitantes: ver disponibilidad de todos los campings
- Alerta cuando un camping está lleno
- **Entregable:** checkin.html v0.3 con módulo de campings

### v0.4 — Módulo de arrieros (semana 19-20)
- Vista para arrieros: calendario de solicitudes, marcar disponibilidad
- Vista para Centro de Visitantes: solicitar transporte desde el registro
- **Entregable:** checkin.html v0.4 con módulo de arrieros

---

## Fase 4 — Probar (octubre – noviembre 2026)

Piloto en terreno antes de la temporada.

### Instalación en Centro de Visitantes (semana 21)
- Desplegar v0.4 en el dispositivo del Centro
- Capacitar al primer voluntario
- Verificar que funciona offline y sincroniza con Starlink

### Prueba con 2 campings (semana 22-24)
- Seleccionar los 2 campings más dispuestos a probar
- Entregarles acceso al sistema
- Recoger feedback semanal durante 3 semanas
- Documentar problemas y ajustes necesarios

### Ajustes y correcciones (semana 25-26)
- Corregir bugs reportados durante el piloto
- Ajustar interfaz según feedback de usuarios reales
- **Entregable:** checkin.html v0.5 (versión candidata para temporada)

---

## Fase 5 — Desplegar (diciembre 2026)

Lanzamiento operativo para la temporada.

### Capacitación de voluntarios (semana 27)
- Sesión práctica con todos los voluntarios del Centro de Visitantes
- Documento impreso de instrucciones básicas (1 página)
- Contacto de soporte para dudas durante temporada

### Integración completa (semana 28)
- Los cinco campings conectados al sistema
- Arrieros conectados al sistema
- Dashboard de lectura disponible para OVC y gestión del territorio

### Temporada operativa (diciembre 2026 en adelante)
- Sistema en producción
- Monitoreo de uso y recolección de feedback
- Iteraciones mensuales durante temporada si es necesario

---

## Principios de ejecución

**El código se escribe después de escuchar.** La Fase 1 no produce software.
Produce Issues en GitHub con las palabras exactas de las personas que van
a usar el sistema. Esos Issues son la especificación.

**Cada versión funciona sola.** Si el proyecto se detiene en v0.2, el Centro
de Visitantes igual tiene un registro digital con sync. Si se detiene en v0.3,
además tiene vista de campings. No hay versión que no sea útil por sí misma.

**Los actores validan antes de construir.** Ningún módulo se desarrolla sin
que las personas que lo van a usar hayan visto un mockup y dicho "sí, esto
me sirve". Esto evita construir cosas que nadie adopta.

**Todo se publica en Granite.** Cada Issue de necesidades, cada decisión de
diseño, cada versión del código queda documentada en el repositorio público.
Cualquier persona puede auditar el proceso, contribuir código, o replicar
el sistema en otro territorio.

**El sistema no tiene propietario.** Licencia MIT. Código abierto. Cada actor
alimenta sus datos y consume lo que necesita. El soporte técnico es
comunitario, no institucional.

---

## Recursos necesarios

| Recurso | Fuente | Costo |
|---|---|---|
| Desarrollo de software | CHH (open source + contribuciones voluntarias) | $0 |
| Articulación con actores | CHH coordinator (4-6 hrs/semana) | Tiempo voluntario |
| Dispositivo en Centro de Visitantes | Ya existe (laptop/tablet) | $0 |
| Conectividad Starlink | Ya existe en el Centro | $0 |
| Hosting del servidor de sync | Firebase/Supabase tier gratuito | $0 |
| Capacitación de voluntarios | 1 sesión presencial | Tiempo personal |

**Costo total estimado del proyecto: $0 en dinero. ~200 horas de trabajo
distribuidas en 8 meses.**

---

## Hitos clave

| Fecha | Hito |
|---|---|
| Abril 2026 | Primera reunión con OVC sobre el sistema |
| Mayo 2026 | Issues publicados con necesidades de todos los actores |
| Junio 2026 | Mockups validados por los actores |
| Agosto 2026 | v0.3 funcional (registro + sync + campings) |
| Octubre 2026 | Piloto instalado en Centro de Visitantes |
| Noviembre 2026 | 2+ campings probando el sistema |
| Diciembre 2026 | Sistema operativo para la temporada |

---

*Naveguemos la vanguardia.*
