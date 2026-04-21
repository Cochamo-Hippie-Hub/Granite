# Territorial Knowledge Ingestion Protocol (TKIP)

**A Foundational Standard for Listening to Territories**

*Cochamó Hippie Hub — Granite Repository*
*Version 1.0 · March 2026*

---

> *"The intelligence is not in the platform. It is in the territory. The platform only listens."*

---

## Preamble

Across the planet, conservation territories generate vast amounts of knowledge every single day. An elder remembers when the river changed course. A ranger notices unusual animal behavior. A scientist publishes a paper on forest connectivity. A farmer reads the moon to know when to prune. A child photographs a bird she has never seen before.

Most of this knowledge is lost.

It is lost because the systems designed to capture it were built for institutions, not for people. They demand logins, formats, taxonomies, and digital literacy that most knowledge holders do not have — and should never be asked to have. The woman who knows how to read the forest does not need to learn Markdown. The fisherman who knows where the river floods does not need a GitHub account. The researcher who mapped a biological corridor should not have to navigate a bureaucratic submission process.

**The Territorial Knowledge Ingestion Protocol (TKIP) exists to solve this.**

TKIP is an open standard that defines how conservation territories can capture knowledge from any source, through any channel, in any format — and transform it into structured, searchable, persistent, and actionable information. It is designed to be replicated by any territory on Earth that wants to listen to its people, its researchers, and its land.

TKIP was born in the Cochamó Valley, Chilean Patagonia — a territory where ancestral knowledge, frontier science, and community wisdom coexist in one of the most biodiverse temperate rainforests on the planet. It is the first protocol created by the [Cochamó Hippie Hub](https://github.com/Cochamo-Hippie-Hub/Granite) and carries the foundational principles of the Granite repository: open source, offline-capable, modular, replicable, community-centered.

---

## Three Axioms

TKIP is built on three non-negotiable axioms. Any implementation that violates these axioms is not TKIP-compliant.

### Axiom I — The Channel Is Chosen by the Emitter

The person contributing knowledge decides how to contribute it. Never the other way around.

A grandmother sends a voice message on WhatsApp. A professor sends an email with a shapefile. A park ranger takes a photograph. A neighbor writes a note on paper during a community meeting. A student fills out a web form. An indigenous leader speaks during a recorded assembly.

All of these are valid ingestion channels. The system adapts to the emitter. The emitter never adapts to the system.

**Corollary:** If a knowledge holder cannot contribute through the channel they already use daily, the system has failed — not the person.

### Axiom II — Knowledge Enters Raw, the System Cooks It

No contributor is ever asked to structure, format, classify, tag, translate, or organize their input. That is the system's job.

A voice message arrives as audio. The system transcribes it, classifies it, extracts entities, geolocates references, cross-references existing data, and produces a structured record. The contributor's only job was to speak.

**Corollary:** The cognitive cost of contributing must approach zero. The processing cost is absorbed by the curation layer, assisted by artificial intelligence.

### Axiom III — Every Contribution Receives Acknowledgment

The territory speaks back to those who speak to it. Every single contribution — no matter how small, how informal, how unstructured — receives a human acknowledgment confirming that the knowledge was received, valued, and incorporated.

This is not a courtesy. It is the mechanism that sustains the system. People contribute again when they know their first contribution mattered. Trust is built one acknowledgment at a time.

**Corollary:** A system that extracts knowledge without returning recognition is not a knowledge system. It is extraction. TKIP does not extract. TKIP listens.

---

## Architecture

TKIP defines four layers. Each layer is independent and can be implemented with different technologies, but all four must be present.

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│   LAYER 1 — CAPTURE                                │
│   Multiple channels, zero friction                  │
│                                                     │
│   WhatsApp · Email · Web Form · In-Person ·         │
│   Field Sensors · Satellite · Audio · Photo ·       │
│   Paper · Radio · SMS · Social Media                │
│                                                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│   LAYER 2 — CONVERGENCE                             │
│   All channels feed into a single curation queue    │
│                                                     │
│   Channel adapters normalize inputs into a          │
│   unified Contribution Object regardless of         │
│   source format or channel                          │
│                                                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│   LAYER 3 — CURATION                                │
│   Human intelligence assisted by artificial         │
│   intelligence                                      │
│                                                     │
│   Transcription · Classification · Entity           │
│   Extraction · Geolocation · Cross-referencing ·    │
│   Validation · Structuring · Attribution            │
│                                                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│   LAYER 4 — REPOSITORY                              │
│   Structured, persistent, searchable,               │
│   open knowledge                                    │
│                                                     │
│   Markdown files · GIS layers · Databases ·         │
│   Issue trackers · Linked data · APIs               │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Layer 1 — Capture

The Capture Layer defines the ingestion channels through which knowledge enters the system. TKIP does not prescribe specific channels — it prescribes that channels must be selected based on the communication habits of each contributor group.

#### Channel Selection Matrix

| Contributor Profile | Primary Channel | Fallback Channel | Input Types |
|---|---|---|---|
| **Local community** | WhatsApp (voice, photo, text) | In-person during assemblies | Audio, photos with GPS, free text, video |
| **Elders & traditional knowledge holders** | WhatsApp voice messages, recorded interviews | Paper notes transcribed by curator | Audio, oral narrative |
| **Researchers & academics** | Email with lightweight template | Web form | Papers, datasets, shapefiles, cartography, reports |
| **Government & institutions** | Email, official channels | Web form | Reports, permits, resolutions, maps |
| **Field team (rangers, monitors)** | WhatsApp group, dedicated app | Radio + transcription | Photos, GPS tracks, observations, alerts |
| **General public & allies** | Web form on project website | Email | Text, photos, documents |
| **Automated sources** | API / sensor feed | Satellite data pipelines | Sensor readings, satellite imagery, weather data |

#### Channel Requirements

Every channel implementation must satisfy:

1. **Availability** — The channel must be accessible with the connectivity conditions of the territory. In remote areas, this means offline-capable or low-bandwidth channels take priority.
2. **Familiarity** — Contributors must already know how to use the channel. No training required.
3. **Bidirectionality** — The channel must allow the system to send acknowledgments back to the contributor.
4. **Metadata preservation** — The channel must preserve or allow recovery of: timestamp, author identity (or anonymity if requested), and geolocation when available.

### Layer 2 — Convergence

The Convergence Layer transforms heterogeneous inputs from multiple channels into a standardized **Contribution Object** that can be processed by the Curation Layer.

#### The Contribution Object

Every piece of knowledge that enters TKIP is wrapped in a Contribution Object with the following schema:

```yaml
contribution:
  id: unique identifier (auto-generated)
  timestamp: ISO 8601 datetime of reception
  channel: whatsapp | email | web_form | in_person | sensor | satellite | other
  
  contributor:
    name: string (or "anonymous")
    role: community | elder | researcher | institution | field_team | public | automated
    contact: channel-appropriate contact info (for acknowledgment)
    consent: explicit | implicit | anonymous
  
  raw_input:
    type: audio | text | image | video | document | dataset | geospatial | mixed
    content: raw file(s) or text as received
    language: detected or declared language
    metadata:
      geolocation: coordinates if available
      device: device info if available
      file_formats: list of formats received
  
  processing_status: received | queued | in_curation | curated | published | rejected
  
  curation:
    curator: name of person who processed
    date_curated: ISO 8601 datetime
    category: ethnobotanical | fauna_observation | territorial_alert | 
              scientific_data | administrative | community_concern | 
              historical_record | environmental_monitoring | other
    subcategory: free text
    structured_output: path to resulting repository file(s)
    cross_references: list of related contribution IDs or repository paths
    ai_assisted: boolean
    notes: curator's notes
  
  acknowledgment:
    sent: boolean
    date: ISO 8601 datetime
    channel: same as input channel or alternative
    message: text of acknowledgment sent
```

#### Channel Adapters

Each ingestion channel requires an **adapter** — a lightweight process that converts channel-specific input into a Contribution Object. Adapters can be automated, semi-automated, or manual.

| Channel | Adapter Type | Implementation |
|---|---|---|
| WhatsApp | Semi-automated | WhatsApp Business API or manual forwarding to curation queue |
| Email | Semi-automated | Email parsing rules + manual review |
| Web Form | Automated | Form submission creates Contribution Object directly |
| In-Person | Manual | Curator creates Contribution Object from notes/recordings |
| Sensors | Automated | API integration produces Contribution Objects on schedule |
| Satellite | Automated | Processing pipeline + automated classification |

### Layer 3 — Curation

The Curation Layer is where human intelligence and artificial intelligence collaborate to transform raw contributions into structured knowledge. This is the heart of TKIP.

#### The Curator Role

The curator is the most important role in a TKIP implementation. Curators are not data entry clerks — they are **knowledge translators** who understand both the territory and the repository.

**Curator responsibilities:**

1. **Receive** — Monitor the curation queue across all channels
2. **Triage** — Prioritize urgent items (alerts, time-sensitive observations)
3. **Process** — Use AI-assisted tools to transcribe, translate, extract, and structure
4. **Validate** — Verify plausibility, check for duplicates, confirm geolocation
5. **Attribute** — Ensure proper credit to the original contributor
6. **Contextualize** — Connect the contribution to existing knowledge in the repository
7. **Publish** — Create or update repository files with the new knowledge
8. **Acknowledge** — Send confirmation back to the contributor
9. **Close** — Mark the Contribution Object as processed

#### AI-Assisted Processing Pipeline

For each raw input type, TKIP defines an AI processing pipeline that assists (never replaces) the curator:

**Audio (voice messages, recordings, interviews)**
```
Audio → Speech-to-Text Transcription → Language Detection →
Entity Extraction (species, places, dates, people) →
Category Suggestion → Draft Structured Record →
Curator Review → Publication
```

**Images (photos, scanned documents)**
```
Image → EXIF Metadata Extraction (GPS, date, device) →
Object/Species Recognition (if fauna/flora) →
OCR (if document/text in image) →
Category Suggestion → Draft Structured Record →
Curator Review → Publication
```

**Documents (PDFs, papers, reports)**
```
Document → Text Extraction → Metadata Extraction
(authors, DOI, abstract, keywords) →
Entity Extraction → Geospatial Reference Detection →
Category Suggestion → Draft Structured Record →
Curator Review → Publication
```

**Geospatial Data (shapefiles, KML, GPS tracks)**
```
Geospatial File → Format Validation → Coordinate System
Detection → Overlay with Territory Boundaries →
Intersection Analysis with Existing Layers →
Category Suggestion → Draft Structured Record →
Curator Review → Publication
```

**Free Text (WhatsApp messages, form submissions)**
```
Text → Language Detection → Entity Extraction →
Sentiment Analysis (for alerts/concerns) →
Category Suggestion → Draft Structured Record →
Curator Review → Publication
```

#### Curation Queue

The curation queue is an ordered list of pending Contribution Objects. TKIP recommends implementing it as a GitHub Issues board with the following labels:

- `tkip:received` — New contribution, not yet reviewed
- `tkip:in-curation` — Curator is actively processing
- `tkip:needs-info` — Curator needs to ask contributor for clarification
- `tkip:curated` — Processed and published to repository
- `tkip:acknowledged` — Contributor has been notified
- `tkip:closed` — Full cycle complete

Priority labels:
- `tkip:urgent` — Time-sensitive (alerts, safety, environmental emergencies)
- `tkip:scientific` — Research data requiring specialized processing
- `tkip:ancestral` — Traditional/ancestral knowledge requiring cultural sensitivity

### Layer 4 — Repository

The Repository Layer is the persistent, structured, searchable home for all curated knowledge. TKIP does not prescribe a specific repository technology, but defines requirements:

1. **Open** — Knowledge must be accessible under open licenses (with exceptions for culturally sensitive or personally identifiable information)
2. **Persistent** — Knowledge must survive technology changes, team turnover, and institutional transitions
3. **Versioned** — All changes must be tracked with full history
4. **Searchable** — Knowledge must be findable through multiple pathways (text search, geographic search, temporal search, category browsing)
5. **Interoperable** — Knowledge must be exportable in standard formats
6. **Attributable** — Every piece of knowledge must trace back to its original contributor

**Reference implementation:** Git repository with Markdown files, hosted on GitHub, with GIS layers in standard formats (GeoJSON, Shapefile), following the Granite repository structure.

---

## Knowledge Categories

TKIP defines a base taxonomy for territorial knowledge. Implementations may extend but should not reduce this taxonomy.

### Primary Categories

| Code | Category | Description | Typical Sources |
|---|---|---|---|
| `ETH` | Ethnobotanical & Traditional Knowledge | Plant use, lunar cycles, ancestral practices, traditional medicine, oral history | Elders, community members, indigenous leaders |
| `FAU` | Fauna Observations | Species sightings, tracks, behavior, migration patterns, nesting sites | Rangers, community, researchers, camera traps |
| `FLO` | Flora & Vegetation | Forest condition, tree health, invasive species, phenology, regeneration | Field team, researchers, satellite |
| `HYD` | Hydrology & Water | River levels, water quality, springs, glacial changes, flooding events | Sensors, community, researchers |
| `CLI` | Climate & Weather | Temperature, precipitation, extreme events, seasonal patterns | Weather stations, community observations |
| `GEO` | Geospatial & Cartography | Maps, boundaries, land use, trails, infrastructure, shapefiles | Researchers, institutions, GPS tracks |
| `SOC` | Community & Social | Concerns, proposals, meeting records, social dynamics, governance | Community assemblies, leaders, surveys |
| `ALR` | Territorial Alerts | Illegal extraction, fire, pollution, infrastructure damage, safety | Community, rangers, field team |
| `SCI` | Scientific Research | Papers, datasets, studies, monitoring results, technical reports | Universities, research centers, NGOs |
| `ADM` | Administrative & Legal | Permits, resolutions, regulations, legal opinions, institutional records | Government, legal advisors, institutions |
| `HIS` | Historical Record | Past events, photographic archives, oral history, territorial memory | Elders, archives, libraries, community |
| `INF` | Infrastructure & Access | Road conditions, connectivity, facilities, services, logistics | Field team, community, visitors |

### Cross-Cutting Tags

Contributions may carry multiple cross-cutting tags regardless of primary category:

- `indigenous-knowledge` — Related to indigenous or ancestral peoples
- `gender-perspective` — Captures gender-specific knowledge or perspectives
- `youth` — Contributed by or relevant to young people
- `urgent` — Requires immediate attention
- `seasonal` — Time-bound or seasonally relevant
- `baseline` — Establishes a reference point for future monitoring
- `longitudinal` — Part of an ongoing observation series

---

## Cultural Sensitivity Protocol

Not all knowledge should be made fully open. TKIP recognizes three levels of access:

### Open Knowledge
Available to anyone under the repository's open license. This is the default.

### Restricted Knowledge
Available only to authorized team members. Used for:
- Exact locations of endangered species (to prevent poaching)
- Sensitive community information shared in confidence
- Data under academic embargo

### Sacred Knowledge
Knowledge that indigenous or traditional communities share with the explicit condition that it not be published openly. TKIP mandates:
- **Prior informed consent** before any recording or transcription
- **Community approval** before any publication, even restricted
- **Right to withdraw** — the community can request removal at any time
- **No derivative use** without explicit community authorization

**The contributor always controls the access level of their contribution.**

---

## Implementation Guide

### Minimum Viable TKIP (for territories starting from zero)

A territory can implement TKIP with:

1. **One WhatsApp number** (dedicated to receiving contributions)
2. **One email address** (for researchers and institutions)
3. **One curator** (a person who checks both channels daily)
4. **One repository** (a GitHub repository with folders matching the category taxonomy)
5. **One AI tool** (any speech-to-text service for transcribing audio)
6. **One spreadsheet** (tracking contributions received, processed, and acknowledged)

Total cost: approximately zero (all tools have free tiers).
Total setup time: one day.

This is intentional. TKIP must be deployable by a single motivated person in a remote territory with limited connectivity and no budget.

### Scaling TKIP

As a territory grows its implementation, TKIP layers can be enhanced independently:

| Layer | Minimum | Intermediate | Advanced |
|---|---|---|---|
| Capture | WhatsApp + Email | + Web form + field app | + IoT sensors + satellite feeds + API integrations |
| Convergence | Manual forwarding | Semi-automated adapters | Fully automated pipeline with webhooks |
| Curation | Single curator + basic AI | Curator team + advanced AI pipeline | RAG-assisted curation + automated cross-referencing |
| Repository | GitHub + Markdown | + GIS server + database | + Knowledge graph + semantic search + public API |

---

## Metrics

A TKIP implementation tracks the following metrics to measure health:

### Flow Metrics
- **Contributions received** per channel per month
- **Average time from reception to curation** (target: < 72 hours for standard, < 4 hours for urgent)
- **Average time from curation to acknowledgment** (target: < 24 hours after curation)
- **Curation queue depth** (pending items — should trend toward zero)

### Diversity Metrics
- **Contributor diversity** — number of unique contributors per month
- **Channel diversity** — percentage of contributions per channel
- **Category diversity** — distribution across knowledge categories
- **Geographic diversity** — spatial distribution of contributions across territory

### Quality Metrics
- **Cross-reference density** — average number of connections per contribution to existing knowledge
- **Return contributor rate** — percentage of contributors who contribute more than once (target: > 40%)
- **Acknowledgment completion rate** (target: 100%)

### Impact Metrics
- **Knowledge nodes created** — new structured records in repository per month
- **Decisions informed** — management or policy decisions that cited repository knowledge
- **External citations** — references to repository knowledge by external researchers or institutions

---

## Governance

### Who Owns the Knowledge?

TKIP adopts the principle of **contributory sovereignty**: each contributor retains moral authorship of their contribution. The repository holds a license to store, structure, and share the knowledge under the terms agreed upon at contribution time.

The territory does not own the knowledge. The territory is the custodian.

### Ethical Commitments

Any TKIP implementation commits to:

1. **Never monetize individual contributions** without explicit contributor consent
2. **Never use contributed knowledge against the contributor's community**
3. **Always attribute** — anonymous contributions are anonymized by choice, not by negligence
4. **Maintain transparency** about how knowledge is processed, stored, and used
5. **Enable data portability** — contributors can request export of all their contributions at any time
6. **Resist enclosure** — TKIP knowledge must remain accessible and must not be locked behind proprietary platforms

---

## Relationship to Existing Frameworks

TKIP is designed to complement, not replace, existing frameworks:

- **FAIR Data Principles** (Findable, Accessible, Interoperable, Reusable) — TKIP adds the dimension of *equitable ingestion* that FAIR does not address
- **CARE Principles for Indigenous Data Governance** (Collective Benefit, Authority to Control, Responsibility, Ethics) — TKIP's Cultural Sensitivity Protocol directly implements CARE
- **Open Science** — TKIP extends open science to include non-academic knowledge producers
- **Citizen Science** — TKIP goes beyond citizen science by treating community members not as data collectors for scientists, but as knowledge holders in their own right
- **Traditional Ecological Knowledge (TEK) frameworks** — TKIP provides the digital infrastructure that TEK documentation has historically lacked

---

## A Note on Language

TKIP is published in English for international accessibility, but its implementations must operate in the language of the territory. In Cochamó, that means Spanish and Mapudungun. In Turku, Finnish and Swedish. In Nairobi, Swahili and English.

The protocol itself is language-agnostic. The AI processing pipeline must support the languages spoken in the territory. When a language is not yet supported by available AI tools, the curator bridges the gap manually — the language barrier is never an excuse to exclude a contributor.

---

## Versioning and Evolution

TKIP is a living document. It evolves as territories implement it and discover what works and what does not.

- **Major versions** (2.0, 3.0) introduce new axioms or architectural layers
- **Minor versions** (1.1, 1.2) add categories, refine processes, incorporate lessons learned
- **Patches** (1.0.1) fix errors or clarify language

All changes are tracked in the Granite repository. Proposals for changes follow the standard Granite contribution process: open an issue, discuss, submit a pull request, review, merge.

---

## Invitation

TKIP is not finished. It cannot be finished by one territory alone.

If you work in conservation, in community development, in indigenous rights, in citizen science, in open data, in environmental monitoring — and you recognize the problem that TKIP addresses — you are invited to implement it, adapt it, challenge it, and improve it.

The knowledge is already there. It is in the voices of the people who live in the territory. In the data collected by researchers who care. In the observations of those who walk the land every day.

All we need to do is listen.

---

*Cochamó Hippie Hub · Granite Repository*
*Let us navigate the frontier.*

---

## License

TKIP is released under the [MIT License](https://opensource.org/licenses/MIT), consistent with the Granite repository. You are free to use, modify, and distribute this protocol for any purpose. Attribution to the Cochamó Hippie Hub is appreciated but not required.

If you implement TKIP in your territory, we would love to hear from you: cochamohippiehub@gmail.com

---

*Version 1.0 — First published March 2026*
*Authors: Cochamó Hippie Hub Contributors*
*Origin: Cochamó Valley, Los Lagos Region, Chilean Patagonia*
