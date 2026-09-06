#!/usr/bin/env python3
"""B5.8.0 — Mediciones mecánicas por TO sobre los 84 «necesita reglas».

Diagnóstico puro: cero LLM, cero cambios al pipeline. Importa e0_lib (el
E0 VIGENTE, post-B5.2) en modo lectura para medir con los regex reales qué
reconoce hoy la clasificación de páginas y el marcador de sección, y sonda
con reglas laxas declaradas qué variantes de marcador existen y no matchean.

Salida: mediciones/<to>.json (una por TO, reanudable) y mediciones_84.json
(consolidado). La clasificación por familia la hace clasificar_84.py sobre
este artefacto; acá no se decide nada.

Uso (desde cualquier cwd):
    python3 data/experiment/segmentacion_84/code/medir_84.py [--solo TO1,TO2]
"""

import argparse
import collections
import json
import re
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
E0_DIR = REPO / "data/experiment/reextraccion_v2/e0_chunking"
PREP = REPO / "data/experiment/escalado_prep"
SALIDA = REPO / "data/experiment/segmentacion_84"
MEDICIONES = SALIDA / "mediciones"

sys.path.insert(0, str(E0_DIR))
import e0_lib  # noqa: E402  (lectura pura: regex y clasificación vigentes)

import pdfplumber  # noqa: E402

# ---------------------------------------------------------------- sondas laxas
# Candidato a marcador de índice que el regex vigente NO contempla. FUERTE =
# con guiones o con inicial mayúscula (los marcadores reales medidos en el
# corpus son 'Índice' / 'Indice' / '-Indice-'); DÉBIL = 'índice' minúscula a
# línea entera (contraejemplo medido en cap: cola envuelta de prosa; se
# registra pero no decide familia).
RE_IDX_LAXO = re.compile(
    r"^\s*[-–—]?\s*([ÍIíi]NDICE|[ÍIíi]ndice)\s*"
    r"(GENERAL|general|DE\s+CONTENIDOS?|de\s+contenidos?|TEM[ÁA]TICO|tem[aá]tico)?"
    r"\s*[-–—]?\s*$"
)

# Variantes de encabezado de sección/jerarquía que RE_SECCION vigente no toma.
SONDAS_SECCION = [
    ("SECCION_MAYUSCULAS", re.compile(r"^\s*SECCI[ÓO]N\s+(\d+|[IVXLC]+)\b")),
    ("seccion_romana", re.compile(r"^\s*Secci[oó]n\s+([IVXLC]+)\b")),
    ("capitulo", re.compile(r"^\s*(CAP[ÍI]TULO|Cap[ií]tulo)\s+(\d+|[IVXLC]+)\b")),
    ("titulo_jerarquico", re.compile(r"^\s*(T[ÍI]TULO|T[ií]tulo)\s+(\d+|[IVXLC]+)\b")),
    ("anexo", re.compile(r"^\s*(ANEXO|Anexo)\s*(\d+|[IVXLC]+)?\s*[.:—–-]?\s*$")),
    ("parte", re.compile(r"^\s*(PARTE|Parte)\s+(\d+|[IVXLC]+)\b")),
    ("numero_guion_titulo", re.compile(r"^\s*(\d{1,2})\s*[-–—]\s+[A-ZÁÉÍÓÚ]")),
]

# Señales léxicas de familia de contenido (reglas propias de esta unidad,
# ancladas a las muestras verbatim del scoping U-B5.6-0 §1.4: plandecuentas
# '311106 Cuentas corrientes…' y manual p.501 'Capítulo/Rubro/Imputación…').
RE_LISTA_CODIGO = re.compile(r"^\d{6}(?:\.\d+)?\s+\D")
RE_FICHA_CAMPO = re.compile(
    r"^(Cap[ií]tulo|Rubro|Moneda(/Residencia)?|Otros Atributos|Imputaci[oó]n|Incluye)\b"
)

# Regla de tabla de CONTENIDO (re-declaración de la regla del scoping §1.4:
# ≥3 filas, ≥2 columnas, bbox no contenido íntegramente en el 12 % superior
# ni en el 10 % inferior de la página; excluye banner B.C.R.A. y pie).
TOP_FRAC, BOT_FRAC = 0.12, 0.10
MIN_FILAS, MIN_COLS = 3, 2

MAX_MUESTRAS = 8  # verbatims por sonda y TO


def es_tabla_contenido(tabla, alto_pagina):
    filas = tabla.rows
    if len(filas) < MIN_FILAS:
        return False
    ncols = max((len(r.cells) for r in filas), default=0)
    if ncols < MIN_COLS:
        return False
    x0, top, x1, bottom = tabla.bbox
    if bottom <= alto_pagina * TOP_FRAC:
        return False
    if top >= alto_pagina * (1 - BOT_FRAC):
        return False
    return True


def medir_to(ident: str, pdf_path: Path) -> dict:
    t0 = time.time()
    paginas = e0_lib.extraer_lineas(pdf_path)
    roles = e0_lib.clasificar_paginas(paginas)
    n_pag = len(paginas)

    d = {
        "id": ident,
        "paginas": n_pag,
        "roles_vigente": dict(collections.Counter(roles)),
        "paginas_cuerpo_vigente": roles.count(e0_lib.ROL_CUERPO),
        "paginas_indice_vigente": roles.count(e0_lib.ROL_INDICE),
        "chars_texto": 0,
        "lineas_texto": 0,
        "idx_vigente": [],       # matches de los regex de índice vigentes
        "idx_laxo_fuerte": [],   # candidato no contemplado (guiones o mayúscula)
        "idx_laxo_debil": [],    # 'índice' minúscula a línea entera
        "secciones_vigente": {"total": 0, "en_cuerpo": 0,
                              "numeros_distintos": [], "muestras": []},
        "sondas_seccion": {},    # variante -> {total, muestras}
        "espina": {"labels_total": 0, "labels_en_cuerpo": 0,
                   "raices_distintas": [], "prof_max": 0, "muestras": []},
        "lista_codigo": {"lineas": 0, "pct_lineas": 0.0, "muestras": []},
        "ficha_campo": {"lineas": 0, "pct_lineas": 0.0, "muestras": []},
    }

    numeros_secc, raices = set(), set()
    sondas = {k: {"total": 0, "muestras": []} for k, _ in SONDAS_SECCION}
    n_lineas = 0
    for pi, (lineas, rol) in enumerate(zip(paginas, roles), start=1):
        for li, ln in enumerate(lineas):
            t = ln.texto.strip()
            if not t:
                continue
            n_lineas += 1
            d["chars_texto"] += len(t)

            if e0_lib.RE_MARCA_INDICE.match(t) or (
                    li < e0_lib.POS_MARCA_INDICE
                    and e0_lib.RE_MARCA_INDICE_SIN_GUIONES.match(t)):
                if len(d["idx_vigente"]) < MAX_MUESTRAS:
                    d["idx_vigente"].append({"pag": pi, "linea": li, "texto": t})
            elif RE_IDX_LAXO.match(t):
                fuerte = ("-" in t or "–" in t or "—" in t
                          or t.lstrip()[:1] in "ÍI")
                clave = "idx_laxo_fuerte" if fuerte else "idx_laxo_debil"
                if len(d[clave]) < MAX_MUESTRAS:
                    d[clave].append({"pag": pi, "linea": li, "rol": rol, "texto": t})

            m = e0_lib.RE_SECCION.match(t)
            if m:
                d["secciones_vigente"]["total"] += 1
                numeros_secc.add(m.group(1))
                if rol == e0_lib.ROL_CUERPO:
                    d["secciones_vigente"]["en_cuerpo"] += 1
                if len(d["secciones_vigente"]["muestras"]) < MAX_MUESTRAS:
                    d["secciones_vigente"]["muestras"].append(
                        {"pag": pi, "rol": rol, "texto": t[:100]})
            else:
                for nombre, rx in SONDAS_SECCION:
                    if rx.match(t):
                        sondas[nombre]["total"] += 1
                        if len(sondas[nombre]["muestras"]) < MAX_MUESTRAS:
                            sondas[nombre]["muestras"].append(
                                {"pag": pi, "rol": rol, "texto": t[:100]})
                        break

            tok = t.split()[0] if t.split() else ""
            resto = t[len(tok):].strip()
            mnum = (e0_lib.RE_NUM_TOKEN.match(tok)
                    or e0_lib.RE_NUM_TOKEN_SIN_PUNTO.match(tok))
            if mnum and resto:
                comps = mnum.group(1).split(".")
                if int(comps[0]) <= e0_lib.MAX_RAIZ:
                    d["espina"]["labels_total"] += 1
                    raices.add(comps[0])
                    d["espina"]["prof_max"] = max(d["espina"]["prof_max"], len(comps))
                    if rol == e0_lib.ROL_CUERPO:
                        d["espina"]["labels_en_cuerpo"] += 1
                    if len(d["espina"]["muestras"]) < MAX_MUESTRAS:
                        d["espina"]["muestras"].append(
                            {"pag": pi, "rol": rol, "texto": t[:100]})

            if RE_LISTA_CODIGO.match(t):
                d["lista_codigo"]["lineas"] += 1
                if len(d["lista_codigo"]["muestras"]) < 3:
                    d["lista_codigo"]["muestras"].append({"pag": pi, "texto": t[:80]})
            if RE_FICHA_CAMPO.match(t):
                d["ficha_campo"]["lineas"] += 1
                if len(d["ficha_campo"]["muestras"]) < 3:
                    d["ficha_campo"]["muestras"].append({"pag": pi, "texto": t[:80]})

    d["lineas_texto"] = n_lineas
    d["secciones_vigente"]["numeros_distintos"] = sorted(numeros_secc, key=int)
    d["espina"]["raices_distintas"] = sorted(raices, key=int)
    d["sondas_seccion"] = {k: v for k, v in sondas.items() if v["total"]}
    if n_lineas:
        d["lista_codigo"]["pct_lineas"] = round(100 * d["lista_codigo"]["lineas"] / n_lineas, 1)
        d["ficha_campo"]["pct_lineas"] = round(100 * d["ficha_campo"]["lineas"] / n_lineas, 1)

    # pasada de tablas (regla de tabla de contenido del scoping, re-declarada)
    n_tab = pag_tab = filas_tab = w_in = w_tot = 0
    with pdfplumber.open(str(pdf_path)) as pdf:
        for page in pdf.pages:
            words = page.extract_words()
            w_tot += len(words)
            tablas = [tb for tb in page.find_tables()
                      if es_tabla_contenido(tb, page.height)]
            if tablas:
                pag_tab += 1
                n_tab += len(tablas)
                filas_tab += sum(len(tb.rows) for tb in tablas)
                cajas = [tb.bbox for tb in tablas]
                for w in words:
                    cx = (w["x0"] + w["x1"]) / 2
                    cy = (w["top"] + w["bottom"]) / 2
                    if any(x0 <= cx <= x1 and top <= cy <= bottom
                           for (x0, top, x1, bottom) in cajas):
                        w_in += 1
    d["tablas"] = {
        "tablas_contenido": n_tab,
        "paginas_con_tabla": pag_tab,
        "filas": filas_tab,
        "palabras_en_tabla": w_in,
        "palabras_total": w_tot,
        "pct_palabras_tabla": round(100 * w_in / w_tot, 1) if w_tot else 0.0,
    }
    d["segundos"] = round(time.time() - t0, 1)
    return d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo", help="ids separados por coma (default: los 84)")
    args = ap.parse_args()

    veredictos = json.load(open(PREP / "veredictos_generalizacion.json"))["por_to"]
    universo = sorted(k for k, v in veredictos.items()
                      if v["veredicto"] == "necesita reglas")
    assert len(universo) == 84, f"universo != 84: {len(universo)}"
    if args.solo:
        universo = [t for t in universo if t in set(args.solo.split(","))]

    MEDICIONES.mkdir(exist_ok=True)
    hechos = 0
    for ident in universo:
        destino = MEDICIONES / f"{ident}.json"
        if destino.exists():
            hechos += 1
            continue
        pdf_path = PREP / "pdfs" / f"{ident}.pdf"
        d = medir_to(ident, pdf_path)
        destino.write_text(json.dumps(d, ensure_ascii=False, indent=1))
        hechos += 1
        print(f"[{hechos}/{len(universo)}] {ident}: {d['paginas']} pág, "
              f"cuerpo_vig={d['paginas_cuerpo_vigente']}, "
              f"secc_vig={d['secciones_vigente']['total']}, "
              f"espina={d['espina']['labels_total']}, "
              f"tab%={d['tablas']['pct_palabras_tabla']} "
              f"({d['segundos']}s)", flush=True)

    consolidado = {}
    for ident in universo:
        consolidado[ident] = json.loads((MEDICIONES / f"{ident}.json").read_text())
    (SALIDA / "mediciones_84.json").write_text(
        json.dumps(consolidado, ensure_ascii=False, indent=1))
    print(f"consolidado: {len(consolidado)} TOs -> mediciones_84.json")


if __name__ == "__main__":
    main()
