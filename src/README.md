# src/ — Granite Tools

Operational tools for conservation territory management.

## territorial_index.py

Processes Markdown documents (meeting minutes, field logs, reports) and generates a structured JSON index for search, retrieval, and institutional memory.

**What it extracts:**
- Document metadata (title, date, type classification)
- Participants and their roles
- Agreements and formal decisions
- Action items with status and responsible parties
- Thematic classification across 8 territorial categories
- Cross-references between documents

**Usage:**

```bash
# Index a directory of meeting minutes (compact summary)
python src/territorial_index.py docs/actas/

# Full output with all extracted fields
python src/territorial_index.py docs/ --output index.json --format full --verbose

# Pipe to jq for quick queries
python src/territorial_index.py docs/actas/ | jq '.stats'
```

**Thematic categories:**
The indexer classifies documents across categories relevant to conservation territory operations: `turismo`, `biodiversidad`, `gobernanza`, `comunidad`, `infraestructura`, `conservacion`, `financiamiento`, `seguridad`.

**Requirements:** Python 3.10+ (standard library only — no external dependencies).

**Design principles:** Offline-first, zero dependencies, bilingual (ES/EN) pattern recognition.

---

→ [Back to main README](../README.md) · [Architecture](../ARCHITECTURE.md) · [Contributing](../CONTRIBUTING.md)
