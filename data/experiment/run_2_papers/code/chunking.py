"""
chunking.py — Extracción de texto de PDFs del subset y chunking.

Estrategia:
- pypdf para extraer texto por página.
- Chunking por "punto" detectado por regex (los TOs del BCRA están
  estructurados en puntos numerados N.N.N.N).
- Si un punto es demasiado grande (>3500 caracteres), se subdivide
  por párrafo en sub-chunks que mantienen el mismo prefijo de location.
- Si un fragmento queda muy chico (<200 caracteres), se concatena al
  siguiente para evitar chunks triviales.
- Cache local en code/cache/<doc_id>/chunks.json para que rerunds no
  rehagan el OCR/chunking.

NOTA: el subset es READ-ONLY. Todos los caches viven en code/cache/.
"""

from __future__ import annotations

import json
import os
import re
import sys
import unicodedata
from dataclasses import dataclass, asdict
from pathlib import Path

import pypdf


# Patrones para detectar headers estructurales del TO
RE_PUNTO_NUMERADO = re.compile(r"^\s*(\d+(?:\.\d+){0,4})\.\s+(.+)$")
RE_SECCION = re.compile(r"^\s*Secci[oó]n\s+([IVXLCDM]+|\d+)\.?\s*[-—]?\s*(.*)$", re.IGNORECASE)
RE_CAPITULO = re.compile(r"^\s*Cap[ií]tulo\s+([IVXLCDM]+|\d+)\.?\s*[-—]?\s*(.*)$", re.IGNORECASE)
RE_ANEXO = re.compile(r"^\s*Anexo\s+([IVXLCDM]+|\d+|\w+)\.?\s*[-—]?\s*(.*)$", re.IGNORECASE)

MAX_CHUNK_CHARS = 6000
MIN_CHUNK_CHARS = 800
# Solo cortamos en puntos numerados de profundidad ≤ MAX_CUT_DEPTH.
# Subpuntos más profundos (p. ej. 1.1.1.1) quedan acumulados dentro del chunk
# del padre. Esto reduce drásticamente el número de chunks (presupuesto-driven).
MAX_CUT_DEPTH = 2


@dataclass
class Chunk:
    """Unidad mínima sobre la que se ejecuta una llamada de extracción."""

    chunk_id: str            # único dentro del corpus, p. ej. "TO_pusf_chunk_007"
    source_doc: str          # filename del PDF
    location: str            # p. ej. "Sección 1, Punto 3.16.3.4" o "p. 12"
    text: str                # el texto del chunk (limpio)
    page_start: int
    page_end: int

    def to_dict(self) -> dict:
        return asdict(self)


def _normalize_whitespace(s: str) -> str:
    # NFKC + colapsar whitespace, conservar saltos de línea para parsing estructural
    s = unicodedata.normalize("NFKC", s)
    # Quitar control chars excepto \n
    s = "".join(ch for ch in s if ch == "\n" or unicodedata.category(ch)[0] != "C")
    # Colapsar espacios pero conservar líneas
    lines = [re.sub(r"[ \t]+", " ", ln).strip() for ln in s.split("\n")]
    # Quitar líneas vacías triples
    out: list[str] = []
    blank = 0
    for ln in lines:
        if not ln:
            blank += 1
            if blank > 1:
                continue
        else:
            blank = 0
        out.append(ln)
    return "\n".join(out)


def _extract_pages(pdf_path: Path) -> list[str]:
    """Texto por página, con normalización mínima."""
    reader = pypdf.PdfReader(str(pdf_path))
    pages: list[str] = []
    for p in reader.pages:
        try:
            t = p.extract_text() or ""
        except Exception:
            t = ""
        pages.append(_normalize_whitespace(t))
    return pages


def _detect_header(line: str) -> Optional[tuple[str, str, int]]:  # type: ignore[name-defined]
    """Retorna (tipo_header, location_text, depth) o None.

    `depth` solo aplica a 'punto' (nivel del punto numerado).
    Para sección/capítulo/anexo, depth=0.
    """
    m = RE_PUNTO_NUMERADO.match(line)
    if m:
        num = m.group(1)
        depth = num.count(".") + 1  # "3.16.3.4" → 4
        return ("punto", f"Punto {num}", depth)
    m = RE_SECCION.match(line)
    if m:
        return ("seccion", f"Sección {m.group(1)}", 0)
    m = RE_CAPITULO.match(line)
    if m:
        return ("capitulo", f"Capítulo {m.group(1)}", 0)
    m = RE_ANEXO.match(line)
    if m:
        return ("anexo", f"Anexo {m.group(1)}", 0)
    return None


from typing import Optional  # noqa: E402


def _split_oversized(text: str, max_chars: int) -> list[str]:
    """Subdivide un bloque grande por párrafo (doble newline)."""
    if len(text) <= max_chars:
        return [text]
    paragraphs = text.split("\n\n") if "\n\n" in text else text.split("\n")
    out: list[str] = []
    cur: list[str] = []
    cur_len = 0
    for p in paragraphs:
        plen = len(p) + 2
        if cur_len + plen > max_chars and cur:
            out.append("\n\n".join(cur))
            cur = [p]
            cur_len = plen
        else:
            cur.append(p)
            cur_len += plen
    if cur:
        out.append("\n\n".join(cur))
    return out


def chunk_pdf(pdf_path: Path, doc_id: str) -> list[Chunk]:
    """
    Estrategia: barrer página por página detectando puntos numerados.
    Cada vez que aparece un nuevo punto numerado, cerramos el chunk
    anterior y abrimos uno nuevo. Sección/Capítulo se acumulan como
    contexto en `location`. Si un chunk supera MAX_CHUNK_CHARS, se
    subdivide en sub-chunks con sufijo /a /b /c en la location.
    """
    pages = _extract_pages(pdf_path)
    source_doc = pdf_path.name

    # Estado del barrido
    chunks: list[Chunk] = []
    section_ctx = ""
    chapter_ctx = ""
    annex_ctx = ""

    cur_text: list[str] = []
    cur_location = "Encabezado"
    cur_page_start = 1
    cur_page_end = 1

    def flush():
        nonlocal cur_text
        text = "\n".join(cur_text).strip()
        if not text:
            cur_text = []
            return
        ctx_parts = [x for x in [chapter_ctx, section_ctx, annex_ctx, cur_location] if x]
        full_location = " > ".join(ctx_parts)
        for i, sub in enumerate(_split_oversized(text, MAX_CHUNK_CHARS)):
            suffix = "" if len(_split_oversized(text, MAX_CHUNK_CHARS)) == 1 else f" /{chr(ord('a') + i)}"
            cid = f"{doc_id}_chunk_{len(chunks):04d}"
            chunks.append(Chunk(
                chunk_id=cid,
                source_doc=source_doc,
                location=full_location + suffix,
                text=sub.strip(),
                page_start=cur_page_start,
                page_end=cur_page_end,
            ))
        cur_text = []

    for page_idx, page_text in enumerate(pages, start=1):
        for line in page_text.split("\n"):
            if not line.strip():
                cur_text.append("")
                continue
            hdr = _detect_header(line)
            if hdr is None:
                cur_text.append(line)
                cur_page_end = page_idx
                if cur_page_start == 1 and not cur_text and page_idx > 1:
                    cur_page_start = page_idx
                continue
            kind, loc, depth = hdr
            if kind == "punto":
                if depth > MAX_CUT_DEPTH:
                    # Punto profundo: no cortamos. Lo incluimos como contenido
                    # del chunk actual, conservando el header literal en el texto.
                    cur_text.append(line)
                    cur_page_end = page_idx
                    continue
                # cerrar el anterior y abrir nuevo punto
                flush()
                cur_location = loc
                cur_page_start = page_idx
                cur_page_end = page_idx
                # el resto de la línea (después del header) es contenido
                rest = line.split(loc.split()[-1], 1)[-1].strip(" .-:")
                if rest:
                    cur_text.append(rest)
            elif kind == "seccion":
                flush()
                section_ctx = loc
                cur_location = loc + " — preámbulo"
                cur_page_start = page_idx
                cur_page_end = page_idx
            elif kind == "capitulo":
                flush()
                chapter_ctx = loc
                section_ctx = ""
                cur_location = loc + " — preámbulo"
                cur_page_start = page_idx
                cur_page_end = page_idx
            elif kind == "anexo":
                flush()
                annex_ctx = loc
                cur_location = loc + " — preámbulo"
                cur_page_start = page_idx
                cur_page_end = page_idx

    flush()

    # Filtrar chunks triviales y mergear con vecino
    merged: list[Chunk] = []
    for c in chunks:
        if len(c.text) < MIN_CHUNK_CHARS and merged:
            prev = merged[-1]
            prev.text = (prev.text + "\n\n" + c.text).strip()
            prev.page_end = max(prev.page_end, c.page_end)
        else:
            merged.append(c)

    return merged


def chunk_subset(subset_dir: Path, cache_dir: Path, only_doc: Optional[str] = None) -> dict[str, list[Chunk]]:
    """
    Procesa los PDFs del subset y devuelve {doc_id: [Chunk, ...]}.
    Cachea por doc en cache_dir/<doc_id>/chunks.json.
    """
    cache_dir.mkdir(parents=True, exist_ok=True)
    pdfs = sorted(subset_dir.glob("*.pdf"))
    out: dict[str, list[Chunk]] = {}
    for pdf in pdfs:
        doc_id = pdf.stem
        if only_doc and doc_id != only_doc:
            continue
        target = cache_dir / doc_id / "chunks.json"
        if target.exists():
            with target.open() as f:
                raw = json.load(f)
            out[doc_id] = [Chunk(**c) for c in raw]
            continue
        chunks = chunk_pdf(pdf, doc_id)
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("w") as f:
            json.dump([c.to_dict() for c in chunks], f, ensure_ascii=False, indent=2)
        out[doc_id] = chunks
    return out


if __name__ == "__main__":
    # CLI rápida: python chunking.py <subset_dir> <cache_dir> [doc_id]
    args = sys.argv[1:]
    subset = Path(args[0])
    cache = Path(args[1])
    only = args[2] if len(args) > 2 else None
    result = chunk_subset(subset, cache, only_doc=only)
    for doc, chunks in result.items():
        total_chars = sum(len(c.text) for c in chunks)
        print(f"{doc}: {len(chunks)} chunks  ({total_chars:,} chars)")
