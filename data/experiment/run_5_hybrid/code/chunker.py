"""
Chunker de TOs del BCRA — Run 5.

Los TOs son texto narrativo-dispositivo con jerarquía numerada (1., 1.1., 1.1.1.,
hasta 1.1.1.1.1.). Cortamos en puntos de profundidad <= MAX_CUT_DEPTH (los más
profundos quedan acumulados en el padre) para que cada chunk tenga ~2.5-3.5 K
caracteres en lugar de ~500 (corte ingenuo) o ~30 K (corte por sección entera).

La salida es una lista de Chunk(chunk_id, source_doc, location, text). El campo
`location` queda como ruta jerárquica reconstruida ("Punto 1.2.3 ...") y se
inyecta luego en cada nodo/edge como `provenance.location` (decisión 3.7).
"""

from __future__ import annotations

import re
import unicodedata
from pathlib import Path

from pypdf import PdfReader

from models import Chunk


# Profundidad máxima a la que se permite cortar. Subpuntos de profundidad mayor
# se acumulan dentro del padre. Empezamos en 2 (lección Run 2 punto 1).
MAX_CUT_DEPTH = 2

# Tamaño máximo aproximado de chunk antes de forzar un sub-corte por párrafo.
HARD_CHUNK_CHAR_LIMIT = 6000

# Tamaño mínimo: por debajo, fusiona con el siguiente para evitar chunks ridículos.
SOFT_CHUNK_CHAR_MIN = 400

# Regex de inicio de punto numerado al comienzo de línea: "1.", "1.1.", "1.1.1.",
# hasta una profundidad razonable. Tolera espacios al inicio (PDFs los meten).
NUMBERED_POINT_RE = re.compile(r"^\s*((?:\d+\.){1,6})\s*(.*)$")


def _read_pdf_text(pdf_path: Path) -> str:
    reader = PdfReader(str(pdf_path))
    pages = []
    for page in reader.pages:
        try:
            pages.append(page.extract_text() or "")
        except Exception:
            pages.append("")
    return "\n".join(pages)


def _strip_combining(s: str) -> str:
    """Quita acentos y combining marks (para slugs)."""
    return "".join(
        c for c in unicodedata.normalize("NFD", s) if not unicodedata.combining(c)
    )


def _slugify(s: str, max_len: int = 60) -> str:
    s = _strip_combining(s).lower()
    s = re.sub(r"[^a-z0-9]+", "_", s).strip("_")
    return s[:max_len]


def _point_depth(numbering: str) -> int:
    """'1.2.3.' → 3."""
    return numbering.strip(".").count(".") + 1


def _split_by_numbered_points(
    text: str, max_depth: int
) -> list[tuple[str, str]]:
    """
    Devuelve [(location, body), ...].
    Corta solo en puntos de profundidad <= max_depth. Subpuntos más profundos
    quedan adentro del body del padre.
    """
    lines = text.splitlines()
    chunks: list[tuple[str, list[str]]] = []
    current_location = "Preámbulo"
    current_body: list[str] = []

    for line in lines:
        m = NUMBERED_POINT_RE.match(line)
        if m:
            numbering, rest = m.group(1), m.group(2).strip()
            depth = _point_depth(numbering)
            if depth <= max_depth:
                # Cerramos el chunk previo si tiene contenido.
                if current_body:
                    chunks.append((current_location, current_body))
                # Abrimos nuevo, usando el numeral + cabecera como location.
                head = f"Punto {numbering.rstrip('.')}"
                if rest:
                    head = f"{head} — {rest[:80]}"
                current_location = head
                current_body = []
                continue
        current_body.append(line)

    if current_body:
        chunks.append((current_location, current_body))

    return [(loc, "\n".join(body).strip()) for loc, body in chunks if any(b.strip() for b in body)]


def _merge_small_chunks(
    chunks: list[tuple[str, str]], min_chars: int
) -> list[tuple[str, str]]:
    """Fusiona chunks chicos consecutivos para evitar ruido."""
    if not chunks:
        return chunks
    merged: list[tuple[str, str]] = []
    buf_loc, buf_text = chunks[0]
    for loc, text in chunks[1:]:
        if len(buf_text) < min_chars:
            buf_loc = f"{buf_loc} + {loc}"
            buf_text = (buf_text + "\n\n" + text).strip()
        else:
            merged.append((buf_loc, buf_text))
            buf_loc, buf_text = loc, text
    merged.append((buf_loc, buf_text))
    return merged


def _split_unit_by_size(text: str, max_chars: int) -> list[str]:
    """Cascada de cortes para una unidad textual sin párrafos: oraciones → líneas → bruto."""
    if len(text) <= max_chars:
        return [text]

    # Nivel 1: oraciones (terminadas en . ! ?, opcionalmente seguidas de cierre).
    sentences = re.split(r"(?<=[\.!?])\s+", text)
    if len(sentences) > 1:
        out: list[str] = []
        buf: list[str] = []
        buf_len = 0
        for s in sentences:
            if buf_len + len(s) > max_chars and buf:
                out.append(" ".join(buf).strip())
                buf, buf_len = [], 0
            if len(s) > max_chars:
                # Una oración sola > max_chars: pasa al siguiente nivel.
                if buf:
                    out.append(" ".join(buf).strip())
                    buf, buf_len = [], 0
                out.extend(_split_unit_by_size(s, max_chars))
                continue
            buf.append(s)
            buf_len += len(s) + 1
        if buf:
            out.append(" ".join(buf).strip())
        if len(out) > 1:
            return out

    # Nivel 2: líneas.
    lines = text.splitlines()
    if len(lines) > 1:
        out2: list[str] = []
        buf2: list[str] = []
        buf2_len = 0
        for ln in lines:
            if buf2_len + len(ln) > max_chars and buf2:
                out2.append("\n".join(buf2).strip())
                buf2, buf2_len = [], 0
            if len(ln) > max_chars:
                if buf2:
                    out2.append("\n".join(buf2).strip())
                    buf2, buf2_len = [], 0
                out2.extend(_split_unit_by_size(ln, max_chars))
                continue
            buf2.append(ln)
            buf2_len += len(ln) + 1
        if buf2:
            out2.append("\n".join(buf2).strip())
        if len(out2) > 1:
            return out2

    # Nivel 3: corte bruto por longitud (rompe palabras solo en casos extremos).
    return [text[i : i + max_chars] for i in range(0, len(text), max_chars)]


def _hard_split_large(
    chunks: list[tuple[str, str]], max_chars: int
) -> list[tuple[str, str]]:
    """
    Si un chunk excede max_chars, lo parte. Primero intenta por párrafos (\n\s*\n);
    si queda algún sub-bloque que aún excede, cae a oraciones, luego a líneas,
    luego a corte bruto. Preserva location anotando "(parte K)".
    """
    out: list[tuple[str, str]] = []
    for loc, text in chunks:
        if len(text) <= max_chars:
            out.append((loc, text))
            continue
        # Nivel 0: párrafos separados por línea en blanco.
        paragraphs = re.split(r"\n\s*\n", text)
        # Si solo hay un párrafo (PDFs que no preservan blanks), cascada por unidad.
        if len(paragraphs) == 1:
            pieces = _split_unit_by_size(text, max_chars)
        else:
            pieces = []
            buf: list[str] = []
            buf_len = 0
            for p in paragraphs:
                if buf_len + len(p) > max_chars and buf:
                    pieces.append("\n\n".join(buf).strip())
                    buf, buf_len = [], 0
                if len(p) > max_chars:
                    if buf:
                        pieces.append("\n\n".join(buf).strip())
                        buf, buf_len = [], 0
                    pieces.extend(_split_unit_by_size(p, max_chars))
                    continue
                buf.append(p)
                buf_len += len(p) + 2
            if buf:
                pieces.append("\n\n".join(buf).strip())

        for ix, piece in enumerate(pieces, start=1):
            suffix = f" (parte {ix}/{len(pieces)})" if len(pieces) > 1 else ""
            out.append((f"{loc}{suffix}", piece.strip()))
    return out


def chunk_pdf(pdf_path: Path) -> list[Chunk]:
    """Pipeline completo: PDF → texto → corte por numeración → merge → hard-split."""
    source_doc = pdf_path.name
    raw_text = _read_pdf_text(pdf_path)

    pairs = _split_by_numbered_points(raw_text, MAX_CUT_DEPTH)
    pairs = _merge_small_chunks(pairs, SOFT_CHUNK_CHAR_MIN)
    pairs = _hard_split_large(pairs, HARD_CHUNK_CHAR_LIMIT)

    chunks: list[Chunk] = []
    doc_slug = _slugify(source_doc.replace(".pdf", ""), max_len=40)
    for ix, (loc, text) in enumerate(pairs):
        chunk_id = f"{doc_slug}__{ix:04d}__{_slugify(loc, max_len=40)}"
        chunks.append(
            Chunk(
                chunk_id=chunk_id,
                source_doc=source_doc,
                location=loc,
                text=text,
            )
        )
    return chunks


if __name__ == "__main__":
    # Smoke local del chunker: cuenta chunks y muestra distribución de tamaños.
    import sys

    pdf = Path(sys.argv[1])
    chs = chunk_pdf(pdf)
    sizes = [len(c.text) for c in chs]
    print(f"PDF: {pdf.name}")
    print(f"Chunks: {len(chs)}")
    if sizes:
        sizes_sorted = sorted(sizes)
        print(f"  min={sizes_sorted[0]}  median={sizes_sorted[len(sizes)//2]}  max={sizes_sorted[-1]}")
        print(f"  total_chars={sum(sizes)}")
    print("\nPrimeros 3 locations:")
    for c in chs[:3]:
        print(f"  - {c.location}  ({len(c.text)} chars)")
