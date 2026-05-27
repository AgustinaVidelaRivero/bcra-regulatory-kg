"""
Chunker de PDFs del subset.

- Lee un PDF del subset con pypdf.
- Convierte a texto preservando número de página.
- Agrupa páginas consecutivas en chunks de ~3000 tokens (medidos con tiktoken
  como aproximación; el modelo no es GPT-4 pero el tokenizer de cl100k_base
  es una buena referencia para presupuesto).
- Cada chunk lleva su rango de páginas (page_start, page_end) para usarse como
  provenance.location = "p.<start>" o "p.<start>-<end>" en el grafo.
- Persiste a JSON dentro de code/cache/chunks/.

Decisión sobre location_hint:
- Si pypdf no nos da estructura de secciones limpia (que es lo más probable
  con los PDFs del BCRA), reportamos solo p.<página>. Documentado en report.md.
"""

import json
import os
import sys
from pathlib import Path

from pypdf import PdfReader
import tiktoken

TARGET_TOKENS = 3000
ENC = tiktoken.get_encoding("cl100k_base")

REPO_ROOT = Path(__file__).resolve().parents[4]  # bcra-regulatory-kg/
SUBSET_DIR = REPO_ROOT / "data" / "experiment" / "subset"
CACHE_DIR = Path(__file__).resolve().parent / "cache" / "chunks"
CACHE_DIR.mkdir(parents=True, exist_ok=True)


def count_tokens(s: str) -> int:
    return len(ENC.encode(s))


def extract_pages(pdf_path: Path) -> list[dict]:
    """Devuelve [{page: int, text: str}, ...] con texto crudo por página."""
    reader = PdfReader(str(pdf_path))
    pages = []
    for i, page in enumerate(reader.pages, start=1):
        try:
            text = page.extract_text() or ""
        except Exception as e:
            print(f"[warn] page {i} failed: {e}", flush=True)
            text = ""
        # Limpieza mínima: collapse multi-newlines
        text = text.replace("\x00", " ").strip()
        pages.append({"page": i, "text": text})
    return pages


def make_chunks(pages: list[dict], target_tokens: int = TARGET_TOKENS) -> list[dict]:
    """
    Agrupa páginas consecutivas en chunks de ~target_tokens.
    Una página nunca se parte: si una sola página excede target_tokens, queda como chunk único.
    """
    chunks = []
    buf_pages: list[dict] = []
    buf_tokens = 0

    def flush():
        nonlocal buf_pages, buf_tokens
        if not buf_pages:
            return
        text = "\n\n".join(p["text"] for p in buf_pages if p["text"]).strip()
        if text:
            chunks.append({
                "chunk_id": f"chunk_{len(chunks):04d}",
                "page_start": buf_pages[0]["page"],
                "page_end": buf_pages[-1]["page"],
                "text": text,
                "n_tokens": buf_tokens,
                "n_chars": len(text),
            })
        buf_pages, buf_tokens = [], 0

    for p in pages:
        if not p["text"]:
            continue
        ptok = count_tokens(p["text"])
        if buf_tokens + ptok > target_tokens and buf_pages:
            flush()
        buf_pages.append(p)
        buf_tokens += ptok

    flush()
    return chunks


def chunk_pdf(pdf_filename: str) -> list[dict]:
    pdf_path = SUBSET_DIR / pdf_filename
    if not pdf_path.exists():
        raise FileNotFoundError(f"No existe el PDF: {pdf_path}")
    print(f"[chunk] reading {pdf_filename}", flush=True)
    pages = extract_pages(pdf_path)
    print(f"[chunk] {len(pages)} pages extracted", flush=True)
    chunks = make_chunks(pages)
    print(f"[chunk] {len(chunks)} chunks produced (target {TARGET_TOKENS} tokens)", flush=True)

    # Persistir
    base = pdf_filename.replace(".pdf", "")
    out_path = CACHE_DIR / f"{base}.json"
    payload = {
        "source_pdf": pdf_filename,
        "n_pages": len(pages),
        "n_chunks": len(chunks),
        "target_tokens": TARGET_TOKENS,
        "chunks": chunks,
    }
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    print(f"[chunk] wrote {out_path}", flush=True)
    return chunks


SUBSET_PDFS = [
    "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
    "TO_clasificacion_deudores_actual.pdf",
    "TO_capitales_minimos_actual.pdf",
    "TO_exterior_cambios_actual.pdf",
    "TO_regimen_informativo_contable_mensual_actual.pdf",
]


def main():
    if len(sys.argv) > 1:
        # chunkear solo lo pedido
        targets = sys.argv[1:]
    else:
        targets = SUBSET_PDFS
    total = 0
    for t in targets:
        n = len(chunk_pdf(t))
        total += n
    print(f"[chunk] total chunks across {len(targets)} PDFs: {total}", flush=True)


if __name__ == "__main__":
    main()
