"""
01_load_corpus.py — Etapa 1 del cookbook: Document Corpus Building.

Lee los 5 PDFs del subset (READ-ONLY), extrae texto por página con pypdf,
fusiona páginas chicas (<200 tokens) con la siguiente y emite chunks.jsonl
con metadata de provenance fina (TO + rango de páginas).

NO usa la API. Sin costo.

Output: cache/chunks.jsonl
  cada línea = {
      "chunk_id": "capitales_minimos_p007",
      "to": "capitales_minimos",
      "source_doc": "TO_capitales_minimos_actual.pdf",
      "page_start": 7,
      "page_end": 7,
      "location_label": "p. 7",      # para provenance.location
      "version": "A 8418",
      "n_chars": 3421,
      "n_tokens_approx": 850,
      "text": "..."
  }
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Permite correr el script directamente (python 01_load_corpus.py)
sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import (
    CACHE_DIR,
    SUBSET_DIR,
    TO_FILES,
    TO_VERSIONS,
    write_jsonl,
)

CHUNKS_PATH = CACHE_DIR / "chunks.jsonl"
MIN_TOKENS_PER_CHUNK = 200          # umbral de fusión
TOKEN_RATIO = 0.25                  # ~4 chars/token para español, aprox conservadora


# ---------------------------------------------------------------------------
# Extracción de versión (Com. "A" vigente) de la primera página del PDF
# ---------------------------------------------------------------------------

VERSION_PATTERNS = [
    re.compile(r'Última comunicación incorporada:\s*[“"]?A[”"]?\s*(\d{3,5})', re.IGNORECASE),
    re.compile(r'Última comunicación incorporada:\s*A\s*(\d{3,5})', re.IGNORECASE),
]


def extract_version_from_first_page(text: str) -> str | None:
    """Saca la última Com. A del header del TO (ej. 'A 8418'). None si no matchea."""
    for pat in VERSION_PATTERNS:
        m = pat.search(text)
        if m:
            return f"A {m.group(1)}"
    return None


# ---------------------------------------------------------------------------
# Lógica de chunking
# ---------------------------------------------------------------------------

def approx_tokens(text: str) -> int:
    """Estimación grosera: 1 token ≈ 4 chars en español. Para chunk-merging only."""
    return max(1, int(len(text) * TOKEN_RATIO))


def build_page_chunks(pages_text: list[str], to_slug: str, source_doc: str, version: str) -> list[dict]:
    """
    A partir de la lista de textos por página, emite chunks con merging de páginas chicas.

    Si page[i] tiene < MIN_TOKENS_PER_CHUNK, se fusiona con page[i+1] (y si esa también es chica,
    sigue acumulando). Provenance.location se registra como rango "pp. 7-9".
    """
    chunks: list[dict] = []
    buffer_text: list[str] = []
    buffer_pages: list[int] = []

    def flush():
        if not buffer_text:
            return
        text = "\n\n".join(buffer_text).strip()
        if not text:
            buffer_text.clear()
            buffer_pages.clear()
            return
        pstart, pend = buffer_pages[0], buffer_pages[-1]
        loc = f"p. {pstart}" if pstart == pend else f"pp. {pstart}-{pend}"
        chunk_id = f"{to_slug}_p{pstart:03d}" if pstart == pend else f"{to_slug}_p{pstart:03d}_{pend:03d}"
        chunks.append({
            "chunk_id": chunk_id,
            "to": to_slug,
            "source_doc": source_doc,
            "page_start": pstart,
            "page_end": pend,
            "location_label": loc,
            "version": version,
            "n_chars": len(text),
            "n_tokens_approx": approx_tokens(text),
            "text": text,
        })
        buffer_text.clear()
        buffer_pages.clear()

    for i, page_text in enumerate(pages_text, start=1):
        page_text = (page_text or "").strip()
        if not page_text:
            continue
        buffer_text.append(page_text)
        buffer_pages.append(i)
        current_tokens = approx_tokens("\n\n".join(buffer_text))
        if current_tokens >= MIN_TOKENS_PER_CHUNK:
            flush()
    flush()  # último buffer

    return chunks


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Etapa 1: extraer texto y chunkear los 5 TOs.")
    parser.add_argument("--force", action="store_true", help="Re-genera chunks.jsonl aunque exista.")
    args = parser.parse_args(argv)

    if CHUNKS_PATH.exists() and not args.force:
        print(f"[01_load_corpus] {CHUNKS_PATH} ya existe. Usá --force para regenerar.")
        return 0

    # Importar pypdf acá: no es responsabilidad de common.py
    from pypdf import PdfReader

    all_chunks: list[dict] = []
    for to_slug, filename in TO_FILES.items():
        pdf_path = SUBSET_DIR / filename
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF faltante en subset: {pdf_path}")

        reader = PdfReader(str(pdf_path))
        n_pages = len(reader.pages)
        pages_text = [(reader.pages[i].extract_text() or "") for i in range(n_pages)]

        # Versión: del header de la primera página, fallback al hardcode de common.py
        version = extract_version_from_first_page(pages_text[0] if pages_text else "")
        if not version:
            version = TO_VERSIONS[to_slug]

        chunks = build_page_chunks(pages_text, to_slug, filename, version)
        all_chunks.extend(chunks)
        print(f"[01_load_corpus] {to_slug}: {n_pages} págs → {len(chunks)} chunks (versión: {version})")

    write_jsonl(CHUNKS_PATH, all_chunks)
    print(f"[01_load_corpus] OK · {len(all_chunks)} chunks → {CHUNKS_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
