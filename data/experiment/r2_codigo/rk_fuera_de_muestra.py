"""U-R2-CODIGO, ajuste K — censo informativo fuera de muestra de la regla de
encabezados de e0-r2.

La regla (e0_lib.titulos_mayusculas_repetidos y separar_encabezado_pie con
`mayusculas_repetidas`) se aprobó midiendo los diez TOs de la tanda 0. Este
script la aplica, con el código de e0-r2 (correr_e0.lineas_conservadas_k), a
los PDFs del corpus escalado que no son de la tanda 0, con un tope de páginas
por TO, y lista por TO las líneas que la regla conserva (las que el descarte
histórico quitaba) y los TOs con una sola página de cuerpo (en ellos ningún
texto se repite, así que la regla conserva toda línea en mayúsculas de la
zona de título). Roles de página del camino vigente de E0. USD 0.

Por línea: `lectura` (lectura propia de la página, sin revisión de la
autora; clave (TO, página) en LECTURA, porque en ninguna página las líneas
conservadas mezclan contenido y encabezado) y `mecanismo`, computado:
«regla» si la línea, sola, no pasa el descarte de e0-r2 (mayúsculas sin
repetirse); «arrastre» si sola se descartaría («B.C.R.A.», línea de sección,
texto repetido o cola de título) y queda porque el recorrido de la zona de
encabezado se detuvo en una línea anterior conservada.

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B \\
    data/experiment/r2_codigo/rk_fuera_de_muestra.py --max-paginas 300 --out <json>
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

import pdfplumber

REPO = Path(__file__).resolve().parents[3]
E0DIR = REPO / "data" / "experiment" / "reextraccion_v2" / "e0_chunking"
PDFS = REPO / "data" / "experiment" / "escalado_prep" / "pdfs"
sys.path.insert(0, str(E0DIR))
import correr_e0 as C  # noqa: E402
import e0_lib as E0  # noqa: E402

TANDA0_NUEVOS = ("ctacte", "docvig", "lingob", "pagjub", "polcre")
LECTURA: dict[tuple[str, int], str] = {
    ('adfsp', 30): 'contenido: rótulos del modelo del anexo de la Sección 6',
    ('adrei', 17): 'encabezado de página: segunda línea del título, partida distinto en esta página; arrastra «B.C.R.A.» y la sección',
    ('apnf', 6): 'contenido: rótulo de la fórmula modelo',
    ('apnf', 7): 'contenido: título de la fórmula modelo',
    ('apnf', 8): 'contenido: título de la fórmula modelo',
    ('cateloc', 5): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 6): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 7): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 8): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 9): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 10): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 11): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 12): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 13): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 14): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 15): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 16): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 17): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 18): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 19): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 20): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 21): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 22): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 23): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 24): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 25): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 26): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 27): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 28): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 29): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 30): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 31): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 32): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 33): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 34): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 35): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 36): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 37): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 38): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 39): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 40): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 41): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 42): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 43): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 44): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 45): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 46): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 47): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 48): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 49): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 50): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 51): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 52): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 53): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 54): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 55): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 56): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 57): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 58): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 59): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 60): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cateloc', 61): 'contenido: primera fila de datos del cuadro de localidades en la página',
    ('cirmo3', 7): 'contenido: encabezado de columnas de la tabla de billetes',
    ('cryl', 12): 'encabezado de página: título del TO partido distinto en esta página; arrastra «B.C.R.A.» y la sección',
    ('cryl', 16): 'encabezado de página: título del TO partido distinto en esta página; arrastra «B.C.R.A» y la sección con su cola',
    ('inspag', 31): 'contenido: rótulo numerado del punto (2.17 a 2.23), en mayúsculas',
    ('inspag', 32): 'contenido: rótulo numerado del punto (2.17 a 2.23), en mayúsculas',
    ('inspag', 35): 'contenido: rótulo numerado del punto (2.17 a 2.23), en mayúsculas',
    ('inspag', 36): 'contenido: rótulo numerado del punto (2.17 a 2.23), en mayúsculas',
    ('inspag', 37): 'contenido: rótulo numerado del punto (2.17 a 2.23), en mayúsculas',
    ('inspag', 38): 'contenido: rótulo numerado del punto (2.17 a 2.23), en mayúsculas',
    ('lingeef', 43): 'encabezado de página: segunda línea del título, separada de «B.C.R.A.» en esta página; arrastra la sección',
    ('manori', 33): 'contenido: títulos y rótulos de formularios y cláusulas modelo',
    ('manori', 34): 'contenido: títulos y rótulos de formularios y cláusulas modelo',
    ('manori', 35): 'contenido: títulos y rótulos de formularios y cláusulas modelo',
    ('manori', 36): 'contenido: títulos y rótulos de formularios y cláusulas modelo',
    ('manori', 37): 'contenido: títulos y rótulos de formularios y cláusulas modelo',
    ('manori', 38): 'contenido: títulos y rótulos de formularios y cláusulas modelo',
    ('manori', 41): 'contenido: títulos y rótulos de formularios y cláusulas modelo',
    ('manori', 46): 'contenido: títulos y rótulos de formularios y cláusulas modelo',
    ('manori', 81): 'contenido: títulos y rótulos de formularios y cláusulas modelo',
    ('manori', 82): 'contenido: títulos y rótulos de formularios y cláusulas modelo',
    ('manori', 83): 'contenido: títulos y rótulos de formularios y cláusulas modelo',
    ('manori', 85): 'contenido: títulos y rótulos de formularios y cláusulas modelo',
    ('micemp', 3): 'encabezado de página: título del TO de una sola página de cuerpo (nada se repite); arrastra «B.C.R.A.»',
    ('nmcief', 2): 'contenido: títulos de capítulo del Anexo I',
    ('nmcief', 8): 'contenido: título de capítulo del Anexo I',
    ('opecam', 10): 'contenido: título de la fórmula modelo',
    ('ordcom', 7): 'contenido: membrete del modelo de Comunicación',
    ('ri2_ae', 3): 'contenido: título del anexo, en su primera página',
    ('ri2_ae', 13): 'contenido: título del anexo, en su primera página',
    ('ri2_ae', 21): 'contenido: título del anexo, en su primera página',
    ('ri_ai', 3): 'encabezado de página: título del TO partido distinto en esta página; arrastra «B.C.R.A.»',
    ('ri_ai', 7): 'encabezado de página: título del TO partido distinto en esta página; arrastra «B.C.R.A.» y la sección',
    ('ri_ai', 8): 'contenido: encabezado de columnas del modelo de información',
    ('ri_cc', 54): 'contenido: rótulo numerado del punto 1.8, en mayúsculas',
    ('ri_cc', 79): 'contenido: encabezado de columna de la tabla de tipos de dictamen',
    ('ri_cc', 89): 'contenido: subtítulo del estado (ejercicio)',
    ('ri_cc', 93): 'contenido: rótulo del anexo del modelo de publicación',
    ('ri_cc', 94): 'contenido: rótulo del anexo del modelo de publicación',
    ('ri_cc', 95): 'contenido: rótulo del anexo del modelo de publicación',
    ('ri_cc', 96): 'contenido: rótulo del anexo del modelo de publicación',
    ('ri_cc', 97): 'contenido: rótulo del anexo del modelo de publicación',
    ('ri_cc', 98): 'contenido: rótulo del anexo del modelo de publicación',
    ('ri_cc', 99): 'contenido: rótulo del anexo del modelo de publicación',
    ('ri_cc', 100): 'contenido: rótulo del anexo del modelo de publicación',
    ('ri_cc', 101): 'contenido: rótulo del anexo del modelo de publicación',
    ('ri_cc', 102): 'contenido: rótulo del anexo del modelo de publicación',
    ('ri_cc', 103): 'contenido: rótulo del anexo del modelo de publicación',
    ('ri_cc', 106): 'contenido: título del modelo',
    ('ri_cc', 110): 'contenido: rubro del modelo de estado',
    ('ri_cc', 113): 'contenido: rubro del modelo de estado',
    ('ri_cc', 115): 'contenido: rubro del modelo de estado',
    ('ri_ccna', 2): 'contenido: título del anexo o capítulo, en su primera página',
    ('ri_ccna', 10): 'contenido: título del anexo o capítulo, en su primera página',
    ('ri_ccna', 15): 'contenido: título del anexo o capítulo, en su primera página',
    ('ri_ccna', 22): 'contenido: título del anexo o capítulo, en su primera página',
    ('ri_ccna', 31): 'contenido: membrete y título de formulario modelo (página sin encabezado del TO)',
    ('ri_ccna', 32): 'contenido: membrete y título de formulario modelo (página sin encabezado del TO)',
    ('ri_ccna', 33): 'contenido: membrete y título de formulario modelo (página sin encabezado del TO)',
    ('ri_ccna', 39): 'contenido: membrete y título de formulario modelo (página sin encabezado del TO)',
    ('ri_ccna', 40): 'contenido: membrete y título de formulario modelo (página sin encabezado del TO)',
    ('ri_ccna', 41): 'contenido: membrete y título de formulario modelo (página sin encabezado del TO)',
    ('ri_ccna', 43): 'contenido: título del anexo o capítulo, en su primera página',
    ('ri_ccna', 46): 'contenido: título del anexo o capítulo, en su primera página',
    ('ri_ccna', 49): 'contenido: título del anexo o capítulo, en su primera página',
    ('ri_ccna', 58): 'contenido: título del anexo o capítulo, en su primera página',
    ('ri_ccna', 60): 'contenido: título del anexo o capítulo, en su primera página',
    ('ri_rml', 27): 'contenido: encabezado de columnas de la tabla de códigos',
    ('ri_rml', 38): 'contenido: rótulo numerado de disposición transitoria, en mayúsculas',
    ('ri_rml', 39): 'contenido: rótulo numerado de disposición transitoria, en mayúsculas',
    ('ri_rml', 49): 'contenido: encabezado de columnas de la tabla de códigos',
    ('ri_rml', 53): 'contenido: encabezado de columnas de la tabla de códigos',
    ('ri_rml', 69): 'contenido: rótulo numerado de disposición transitoria, en mayúsculas',
    ('ri_rml', 70): 'contenido: fila de la guía de correlación (código y concepto)',
    ('ri_rml', 74): 'contenido: fila de la guía de correlación (código y concepto)',
    ('ri_rml', 75): 'contenido: fila de la guía de correlación (código y concepto)',
    ('ri_transpa', 20): 'contenido: título de capítulo y anexo del modelo',
    ('ri_transpa', 23): 'contenido: título de capítulo y anexo',
    ('ri_tsa', 92): 'encabezado de página: segunda línea del título del capítulo 11 del régimen, que ocupa una sola página',
    ('rmrtsd', 6): 'encabezado de página: título del TO partido distinto en esta página; arrastra «B.C.R.A.» y la sección',
    ('snp_cheq', 4): 'contenido: título numerado de la sección, repetido en el cuerpo',
    ('snp_cheq', 5): 'contenido: título numerado de la sección, repetido en el cuerpo',
    ('snp_cheq', 12): 'contenido: título numerado de la sección, repetido en el cuerpo',
    ('snp_cheq', 16): 'contenido: rótulo de diagrama',
    ('snp_cheq', 21): 'contenido: rótulo de cuadro',
    ('snp_cheq', 23): 'encabezado de página: título con guion final en esta página; arrastra «B.C.R.A.», la segunda línea del título y la sección',
    ('snp_cheq', 63): 'contenido: título numerado de la sección, repetido en el cuerpo',
    ('snp_cheq', 66): 'contenido: título numerado de la sección, repetido en el cuerpo',
    ('snp_dd', 3): 'contenido: título de la sección, repetido en el cuerpo',
    ('snp_dd', 4): 'contenido: título de la sección, repetido en el cuerpo',
    ('snp_dd', 9): 'contenido: título de la sección, repetido en el cuerpo',
    ('snp_dd', 26): 'contenido: título de la sección, repetido en el cuerpo',
    ('snp_dd', 28): 'contenido: título de la sección, repetido en el cuerpo',
    ('snp_debin', 12): 'contenido: rótulo numerado del punto 3.5.1.1',
    ('snp_mep', 15): 'contenido: título del convenio modelo',
    ('snp_tr', 31): 'contenido: códigos de una lista (tipo de clave fiscal)',
    ('traval', 7): 'contenido: título de la fórmula modelo',
}


def mecanismo(texto: str, repetidos: set[str]) -> str:
    t = texto.strip()
    sola_se_conserva = (E0._es_titulo_mayusculas(t) and "B.C.R.A." not in t
                        and not E0.RE_SECCION.match(t)
                        and "".join(t.split()) not in repetidos)
    return "regla" if sola_se_conserva else "arrastre"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-paginas", type=int, required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    omitidos, por_to, una_pagina = [], {}, []
    for pdf in sorted(PDFS.glob("*.pdf")):
        to = pdf.stem
        if to in TANDA0_NUEVOS:
            continue
        with pdfplumber.open(str(pdf)) as d:
            n = len(d.pages)
        if n > a.max_paginas:
            omitidos.append({"to": to, "paginas": n})
            continue
        paginas = E0.extraer_lineas(pdf)
        roles = E0.clasificar_paginas(paginas)
        cuerpo = sum(1 for r in roles if r == E0.ROL_CUERPO)
        rep = E0.titulos_mayusculas_repetidos(paginas, roles)
        cons = C.lineas_conservadas_k(paginas, roles, rep)
        if cuerpo == 1:
            una_pagina.append(to)
        if cons:
            por_to[to] = [{"pagina": l.pagina, "texto": l.texto,
                           "lectura": LECTURA.get((to, l.pagina), "SIN LECTURA"),
                           "mecanismo": mecanismo(l.texto, rep)}
                          for l in cons]
    todas = [(to, l) for to, ls in por_to.items() for l in ls]
    clase = Counter(l["lectura"].split(":")[0] for _, l in todas)
    cruce = Counter((l["lectura"].split(":")[0], l["mecanismo"]) for _, l in todas)
    out = {"unidad": "U-R2-CODIGO", "etapa": "ajuste K, fuera de muestra", "informativo": True,
           "max_paginas": a.max_paginas, "tos_omitidos_por_tamano": omitidos,
           "tos_con_una_pagina_de_cuerpo": una_pagina,
           "lineas_conservadas_total": len(todas),
           "tos_con_lineas_conservadas": len(por_to),
           "por_lectura": dict(sorted(clase.items())),
           "por_lectura_y_mecanismo": {f"{a_} / {b_}": n for (a_, b_), n in sorted(cruce.items())},
           "lineas_de_seccion_que_quedan_en_el_cuerpo": sorted(
               f"{to} p{l['pagina']}" for to, l in todas if E0.RE_SECCION.match(l["texto"].strip())),
           "tos_con_encabezado_conservado": sorted({to for to, l in todas
                                                    if l["lectura"].startswith("encabezado")}),
           "por_to": por_to}
    Path(a.out).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
