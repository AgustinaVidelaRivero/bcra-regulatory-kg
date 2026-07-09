"""
pdf_locate.py — Localización de pasajes en los PDFs del subset (Fase 2.4).

Módulo AUTOCONTENIDO extraído de verifier_pilot.py (refactor del Paso 3 de la skill
kg-refinement). Desacopla la localización PDF del pipeline del piloto para que el
verificador agéntico nuevo (verificador.py) la consuma sin arrastrar verifier_pilot.

Depende SOLO de pypdf (lazy import) y de SUBSET_DIR (los PDFs read-only del subset).
La función `localize` mantiene su comportamiento EXACTO: maneja cuerpo-vs-índice por
prose_score, localización por punto y por página, y devuelve localizacion_pdf=ok|fallida.
"""
from __future__ import annotations

import re
from pathlib import Path

# data/experiment/evaluacion/ → parent (data/experiment) / subset.
# Equivale a loader.EVAL_DIR.parent / "subset", sin importar el loader (autocontenido).
SUBSET_DIR = Path(__file__).resolve().parent.parent / "subset"

# --------------------------------------------------------------------------- #
# Localización del pasaje del PDF (por punto / por página)                    #
# --------------------------------------------------------------------------- #
_PDF_CACHE = {}


def pdf_pages(source_doc):
    if source_doc not in _PDF_CACHE:
        import pypdf
        r = pypdf.PdfReader(str(SUBSET_DIR / source_doc))
        _PDF_CACHE[source_doc] = [(p.extract_text() or "") for p in r.pages]
    return _PDF_CACHE[source_doc]


def parse_point(location):
    # preferir el "Punto X.Y" (más específico) sobre "Sección X" cuando vienen ambos
    # (run_2 cita "Sección 3 > Punto 3.6"); fallback a Sección.
    m = re.search(r"Punto\s*(\d+(?:\.\d+)*)", location or "")
    if m: return m.group(1)
    m = re.search(r"Secci[oó]n\s*(\d+(?:\.\d+)*)", location or "")
    return m.group(1) if m else None


def parse_pages(location):
    m = re.search(r"\bpp?\.\s*(\d+)\s*(?:-\s*(\d+))?", location or "")
    if not m: return None
    a = int(m.group(1)); b = int(m.group(2)) if m.group(2) else a
    return (a, b)


def _prose_score(seg):
    """Arreglo 1: puntúa cuán 'cuerpo sustantivo' es el texto que sigue al marcador del punto,
    para descartar índice / tabla 'Origen de las disposiciones' ('1.1. "A" 5388 S/Com…').
    Texto real = muchas palabras; tabla de comunicaciones = códigos "A" N y números."""
    head = seg[:200]
    comm = len(re.findall(r'[“"]A[”"]\s*\d|S\s*/?\s*Com\.?', head))
    table_lines = len(re.findall(r'(?m)^\s*\d+(?:\.\d+)*\.\s*[“"]A[”"]', head))
    # "Sección N" justo después del punto = entrada de índice/TOC (el cuerpo casi nunca
    # encadena un 'Sección N' tras el título). No penaliza listas numeradas del cuerpo (1.1.2.x).
    sec = len(re.findall(r'Secci[oó]n\s+\d+', head))
    words = len(re.findall(r'[A-Za-zÁÉÍÓÚáéíóúñÑ]{4,}', head))
    return words - 8 * comm - 6 * table_lines - 7 * sec


def localize(source_doc, location, window=1400):
    """Devuelve {metodo, ref, pasaje, localizacion_pdf}. Punto: escanea TODAS las ocurrencias en
    el doc y elige la de mayor 'prose_score' (descarta índice y tablas de comunicaciones); si la
    mejor no supera el umbral → localizacion_pdf='fallida' (honesto, no devuelve pasaje malo).
    Página: extrae la(s) página(s) absoluta(s) 1-based."""
    pages = pdf_pages(source_doc)
    pt = parse_point(location)
    if pt:
        pat = re.compile(r"(?m)^\s*" + re.escape(pt) + r"\.\s")
        best = None  # (score, page_idx, seg)
        for i, t in enumerate(pages):
            for mm in pat.finditer(t):
                seg = t[mm.start():mm.start() + window]
                sc = _prose_score(seg)
                if best is None or sc > best[0]:
                    best = (sc, i, seg)
        THRESH = 6
        if best and best[0] >= THRESH:
            return {"metodo": "punto", "ref": f"Punto/Sección {pt} (PDF pág {best[1]+1})",
                    "pasaje": best[2].strip(), "localizacion_pdf": "ok"}
        return {"metodo": "punto",
                "ref": f"Punto/Sección {pt} (mejor score={best[0] if best else 'n/a'} < {THRESH})",
                "pasaje": None, "localizacion_pdf": "fallida"}
    pg = parse_pages(location)
    if pg:
        a, b = pg
        seg = "\n".join(pages[i-1] for i in range(a, min(b, len(pages)) + 1) if 1 <= i <= len(pages))
        seg = seg.strip()
        return {"metodo": "pagina", "ref": f"p.{a}" + (f"-{b}" if b != a else "") + " (PDF absoluto 1-based)",
                "pasaje": seg[:window*2] if seg else None,
                "localizacion_pdf": "ok" if seg else "fallida"}
    return {"metodo": "ninguno", "ref": location, "pasaje": None, "localizacion_pdf": "fallida"}
