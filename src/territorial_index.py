#!/usr/bin/env python3
"""
territorial_index.py — Territorial Document Indexer

Processes Markdown documents (meeting minutes, field logs, reports) from a
conservation territory repository and generates a structured JSON index
for search, retrieval, and institutional memory.

Part of Cochamó Hippie Hub / Granite.
License: MIT

Usage:
    python territorial_index.py <input_dir> [--output index.json] [--format compact|full]
    python territorial_index.py docs/actas/ --output territorial_index.json
    python territorial_index.py docs/ --format full --verbose

The indexer extracts:
    - Document metadata (title, date, type)
    - Participants and their roles
    - Agreements and commitments with responsible parties
    - Action items with status tracking
    - Thematic tags based on content analysis
    - Cross-references between documents
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional


# ── Thematic categories for territorial conservation ──────────────────
# These reflect real operational categories used in the Cochamó territory.
TERRITORIAL_THEMES = {
    "turismo": ["visitante", "turismo", "camping", "sendero", "trail",
                "visitor", "tourism", "arriero", "cabalgata", "trekking",
                "escalada", "climbing", "bivouac", "refugio"],
    "biodiversidad": ["biodiversidad", "fauna", "flora", "huemul", "puma",
                      "cóndor", "alerce", "bosque", "wildlife", "species",
                      "cámara trampa", "camera trap", "monitoreo", "mink"],
    "gobernanza": ["gobernanza", "governance", "directorio", "consejo",
                   "municipalidad", "conaf", "seremi", "autoridad",
                   "reglamento", "normativa", "ordenanza"],
    "comunidad": ["comunidad", "community", "vecino", "junta", "local",
                  "participación", "taller", "workshop", "encuesta",
                  "survey", "territorio", "stakeholder"],
    "infraestructura": ["infraestructura", "camino", "road", "puente",
                        "bridge", "señalética", "signage", "baño",
                        "sanitation", "basura", "waste", "agua", "water"],
    "conservacion": ["conservación", "conservation", "protección",
                     "santuario", "sanctuary", "servidumbre", "DRC",
                     "corredor", "corridor", "restauración"],
    "financiamiento": ["financiamiento", "funding", "fundraising",
                       "donación", "donation", "presupuesto", "budget",
                       "grant", "sponsor"],
    "seguridad": ["seguridad", "safety", "emergencia", "emergency",
                  "rescate", "rescue", "riesgo", "risk", "incendio",
                  "fire", "check-in", "registro"],
}


def parse_document(filepath: Path) -> dict:
    """Parse a single Markdown document and extract structured metadata."""
    text = filepath.read_text(encoding="utf-8", errors="replace")
    lines = text.split("\n")

    doc = {
        "file": str(filepath.name),
        "path": str(filepath),
        "title": _extract_title(lines),
        "date": _extract_date(text, filepath.name),
        "type": _classify_type(filepath.name, text),
        "participants": _extract_participants(text),
        "agreements": _extract_agreements(text),
        "action_items": _extract_action_items(text),
        "themes": _extract_themes(text),
        "word_count": len(text.split()),
        "references": _extract_references(text),
    }
    return doc


def _extract_title(lines: list[str]) -> str:
    """Extract document title from first H1 or H2 heading."""
    for line in lines[:20]:
        line = line.strip()
        if line.startswith("# "):
            return line.lstrip("# ").strip()
        if line.startswith("## "):
            return line.lstrip("# ").strip()
    return "(sin título)"


def _extract_date(text: str, filename: str) -> Optional[str]:
    """Extract date from content or filename."""
    # Try ISO format in text: 2024-09-15, 2025-01-20
    iso_match = re.search(r"(\d{4}-\d{2}-\d{2})", text[:500])
    if iso_match:
        return iso_match.group(1)

    # Try Spanish format: 15 de septiembre de 2024
    months_es = {
        "enero": "01", "febrero": "02", "marzo": "03", "abril": "04",
        "mayo": "05", "junio": "06", "julio": "07", "agosto": "08",
        "septiembre": "09", "octubre": "10", "noviembre": "11",
        "diciembre": "12",
    }
    es_match = re.search(
        r"(\d{1,2})\s+de\s+(" + "|".join(months_es.keys()) + r")\s+de\s+(\d{4})",
        text[:1000], re.IGNORECASE
    )
    if es_match:
        day = es_match.group(1).zfill(2)
        month = months_es[es_match.group(2).lower()]
        year = es_match.group(3)
        return f"{year}-{month}-{day}"

    # Try date in filename: acta-2024-09-15.md or 20240915_notes.md
    fn_match = re.search(r"(\d{4})-?(\d{2})-?(\d{2})", filename)
    if fn_match:
        return f"{fn_match.group(1)}-{fn_match.group(2)}-{fn_match.group(3)}"

    return None


def _classify_type(filename: str, text: str) -> str:
    """Classify the document type based on filename and content patterns."""
    fname = filename.lower()
    tlow = text[:500].lower()

    if "acta" in fname or "acta" in tlow or "minutes" in tlow:
        return "acta"
    if "informe" in fname or "report" in fname or "informe" in tlow:
        return "informe"
    if "log" in fname or "bitácora" in fname or "field" in fname:
        return "bitacora"
    if "plan" in fname or "plan" in tlow:
        return "plan"
    if "encuesta" in fname or "survey" in fname:
        return "encuesta"
    return "documento"


def _extract_participants(text: str) -> list[str]:
    """Extract participant names from common patterns in meeting minutes."""
    participants = []

    # Pattern: "Participantes:" or "Asistentes:" followed by list
    block_match = re.search(
        r"(?:participantes|asistentes|presentes|attendees)[:\s]*\n((?:[-*]\s+.+\n?)+)",
        text, re.IGNORECASE
    )
    if block_match:
        for line in block_match.group(1).split("\n"):
            line = line.strip().lstrip("-* ").strip()
            if line and len(line) < 100:
                # Clean role annotations: "Juan Pérez (coordinador)"
                name = re.sub(r"\s*\(.*?\)\s*$", "", line).strip()
                if name:
                    participants.append(name)

    # Pattern: "Participantes: A, B, C" on one line
    if not participants:
        inline_match = re.search(
            r"(?:participantes|asistentes|presentes)[:\s]+(.+)",
            text, re.IGNORECASE
        )
        if inline_match:
            names = re.split(r"[,;]", inline_match.group(1))
            for name in names:
                name = name.strip().rstrip(".")
                if name and len(name) < 80:
                    participants.append(name)

    return participants


def _extract_agreements(text: str) -> list[str]:
    """Extract formal agreements and decisions from meeting minutes."""
    agreements = []
    seen = set()

    def _add(item: str):
        # Normalize for dedup: strip numbering prefix like "Acuerdo 1: "
        clean = re.sub(r"^(?:acuerdo|decisión)\s*\d*[:\s.]*", "", item,
                       flags=re.IGNORECASE).strip().rstrip(".")
        if clean and len(clean) > 10 and clean.lower() not in seen:
            seen.add(clean.lower())
            agreements.append(clean)

    # 1) Bullet list under "Acuerdos" heading (most structured, preferred)
    section = re.search(
        r"#+\s*(?:acuerdos|agreements|decisiones)\s*\n((?:[-*]\s+.+\n?)+)",
        text, re.IGNORECASE
    )
    if section:
        for line in section.group(1).split("\n"):
            line = line.strip().lstrip("-* ").strip()
            _add(line)

    # 2) Inline patterns: "Se acuerda ...", "Acuerdo N: ..."
    for pattern in [
        r"(?:se acuerda|se decide|agreement)[:\s]+(.+)",
        r"(?:acuerdo|decisión)\s+\d+[:\s.]+(.+)",
    ]:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            _add(match.group(1))

    return agreements


def _extract_action_items(text: str) -> list[dict]:
    """Extract action items with responsible party and status."""
    items = []

    # Pattern: "[ ] Task" or "[x] Task" (GitHub checkbox)
    for match in re.finditer(r"\[([ xX])\]\s+(.+)", text):
        done = match.group(1).lower() == "x"
        description = match.group(2).strip()

        # Try to extract responsible: "Task — @person" or "Task (Responsable: X)"
        responsible = None
        resp_match = re.search(r"(?:—|–|-)\s*@?(\w[\w\s]+?)$", description)
        if not resp_match:
            resp_match = re.search(r"\((?:responsable|a cargo)[:\s]+(.+?)\)", description, re.IGNORECASE)
        if resp_match:
            responsible = resp_match.group(1).strip()
            description = description[:resp_match.start()].strip().rstrip("—–- ")

        items.append({
            "description": description,
            "done": done,
            "responsible": responsible,
        })

    # Pattern: "Tarea:" or "Pendiente:" lines
    for match in re.finditer(r"(?:tarea|pendiente|todo|action)[:\s]+(.+)", text, re.IGNORECASE):
        task = match.group(1).strip()
        if task and len(task) > 5:
            items.append({
                "description": task,
                "done": False,
                "responsible": None,
            })

    return items


def _extract_themes(text: str) -> list[str]:
    """Classify document themes based on keyword presence."""
    text_lower = text.lower()
    found = []
    for theme, keywords in TERRITORIAL_THEMES.items():
        hits = sum(1 for kw in keywords if kw in text_lower)
        if hits >= 2:  # Require at least 2 keyword matches
            found.append(theme)
    return sorted(found)


def _extract_references(text: str) -> list[str]:
    """Extract cross-references to other documents or issues."""
    refs = []

    # GitHub issue references: #1, #42
    for match in re.finditer(r"(?<!\w)#(\d+)\b", text):
        ref = f"#{match.group(1)}"
        if ref not in refs:
            refs.append(ref)

    # Explicit document references
    seen = set(refs)
    for match in re.finditer(r"(?:ver|see|ref|véase)[:\s]+([^\n,]+)", text, re.IGNORECASE):
        ref = match.group(1).strip().rstrip(".")
        if ref and len(ref) < 120 and ref not in seen:
            refs.append(ref)
            seen.add(ref)

    return refs


def build_index(input_dir: Path, output_format: str = "compact",
                verbose: bool = False) -> dict:
    """Process all Markdown files in a directory and build the index."""
    md_files = sorted(input_dir.rglob("*.md"))

    if not md_files:
        print(f"⚠  No Markdown files found in {input_dir}", file=sys.stderr)
        return {"documents": [], "stats": {}}

    documents = []
    all_themes = set()
    all_participants = set()
    total_agreements = 0
    total_actions = 0

    for filepath in md_files:
        if verbose:
            print(f"  📄 Processing: {filepath.name}")

        doc = parse_document(filepath)
        documents.append(doc)

        all_themes.update(doc["themes"])
        all_participants.update(doc["participants"])
        total_agreements += len(doc["agreements"])
        total_actions += len(doc["action_items"])

    # Sort by date (documents without date go last)
    documents.sort(key=lambda d: d.get("date") or "9999-99-99")

    # Build summary statistics
    stats = {
        "total_documents": len(documents),
        "date_range": _date_range(documents),
        "unique_participants": len(all_participants),
        "participant_list": sorted(all_participants),
        "total_agreements": total_agreements,
        "total_action_items": total_actions,
        "pending_actions": sum(
            1 for d in documents
            for a in d["action_items"]
            if not a["done"]
        ),
        "themes_covered": sorted(all_themes),
        "document_types": _count_types(documents),
    }

    index = {
        "generated_at": datetime.now(tz=None).astimezone().isoformat(),
        "source_directory": str(input_dir),
        "generator": "territorial_index.py — Cochamó Hippie Hub / Granite",
        "stats": stats,
        "documents": documents if output_format == "full" else _compact(documents),
    }
    return index


def _date_range(documents: list[dict]) -> dict:
    """Compute the date range of indexed documents."""
    dates = [d["date"] for d in documents if d.get("date")]
    if not dates:
        return {"earliest": None, "latest": None}
    return {"earliest": min(dates), "latest": max(dates)}


def _count_types(documents: list[dict]) -> dict:
    """Count documents by type."""
    counts = {}
    for doc in documents:
        t = doc.get("type", "documento")
        counts[t] = counts.get(t, 0) + 1
    return counts


def _compact(documents: list[dict]) -> list[dict]:
    """Reduce documents to essential fields for compact output."""
    return [
        {
            "file": d["file"],
            "title": d["title"],
            "date": d["date"],
            "type": d["type"],
            "themes": d["themes"],
            "participants_count": len(d["participants"]),
            "agreements_count": len(d["agreements"]),
            "action_items_count": len(d["action_items"]),
            "pending_actions": sum(1 for a in d["action_items"] if not a["done"]),
        }
        for d in documents
    ]


def main():
    parser = argparse.ArgumentParser(
        description="Territorial Document Indexer — Cochamó Hippie Hub / Granite",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python territorial_index.py docs/actas/
  python territorial_index.py docs/ --output index.json --format full
  python territorial_index.py . --verbose

Part of the Granite open-source framework for conservation territory management.
https://github.com/Cochamo-Hippie-Hub/Granite
        """,
    )
    parser.add_argument("input_dir", type=Path,
                        help="Directory containing Markdown documents")
    parser.add_argument("--output", "-o", type=Path, default=None,
                        help="Output JSON file (default: stdout)")
    parser.add_argument("--format", "-f", choices=["compact", "full"],
                        default="compact",
                        help="Output format: compact (summary) or full (all fields)")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Print progress to stderr")
    args = parser.parse_args()

    if not args.input_dir.is_dir():
        print(f"Error: {args.input_dir} is not a directory", file=sys.stderr)
        sys.exit(1)

    if args.verbose:
        print(f"\n🌿 Territorial Document Indexer", file=sys.stderr)
        print(f"   Scanning: {args.input_dir}\n", file=sys.stderr)

    index = build_index(args.input_dir, args.format, args.verbose)

    output_json = json.dumps(index, ensure_ascii=False, indent=2)

    if args.output:
        args.output.write_text(output_json, encoding="utf-8")
        if args.verbose:
            stats = index["stats"]
            print(f"\n✅ Index written to {args.output}", file=sys.stderr)
            print(f"   {stats['total_documents']} documents indexed",
                  file=sys.stderr)
            print(f"   {stats['unique_participants']} unique participants",
                  file=sys.stderr)
            print(f"   {stats['total_agreements']} agreements tracked",
                  file=sys.stderr)
            print(f"   {stats['total_action_items']} action items "
                  f"({stats['pending_actions']} pending)", file=sys.stderr)
    else:
        print(output_json)


if __name__ == "__main__":
    main()
