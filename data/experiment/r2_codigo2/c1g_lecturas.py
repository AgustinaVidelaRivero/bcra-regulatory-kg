"""U-R2-CODIGO-2, C1.g — verificación de dos lecturas de M3.b contra el PDF, sin cambiar los veredictos (USD 0).
Solo escribe --out.

  B02 (`cap::5.3.1.2` cita «el tratamiento del punto 3.6.»): si el punto 3.6 de cap existe en el PDF. Se listan las
      líneas de la Sección 3 que empiezan con un número de punto de dos niveles, en el índice y en el cuerpo, y toda
      línea que nombra «3.6» fuera de un número más largo.
  B20 (`ric::12.1.2` cita «los requisitos previstos en el punto 5.1.2.1.»): si el párrafo nombra otra norma antes de
      la cita. Se transcriben las líneas de 12.1 a 12.1.2 de la página del PDF y toda línea que nombra «5.1.2».

Las líneas salen de `e0_lib.extraer_lineas` (solo lectura) y el rol de cada página de `e0_lib.clasificar_paginas`.

Uso, desde la raíz de una copia del repo:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/r2_codigo2/c1g_lecturas.py \
      --out data/experiment/r2_codigo2/salidas/c1g_lecturas.json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(RAIZ / "data" / "experiment" / "reextraccion_v2" / "e0_chunking"))
import e0_lib as L   # noqa: E402

SUBSET = RAIZ / "data" / "experiment" / "subset"


def lineas(pdf: str):
    pags = L.extraer_lineas(SUBSET / pdf)
    return pags, L.clasificar_paginas(pags)


def fila(pagina: int, rol: str, ln) -> dict:
    return {"pagina": pagina, "rol_pagina": rol, "x0": ln.x0, "texto": ln.texto}


def b02() -> dict:
    pags, roles = lineas("TO_capitales_minimos_actual.pdf")
    seccion3, menciones = [], []
    for i, p in enumerate(pags, 1):
        for ln in p:
            t = ln.texto.strip()
            if re.match(r"^3\.\d+\.\s", t) or (re.match(r"^Secci[oó]n 3\.", t) and roles[i - 1] == "indice"):
                seccion3.append(fila(i, roles[i - 1], ln))
            if re.search(r"(?<![\d.])3\.6(?![\d])", t):
                menciones.append(fila(i, roles[i - 1], ln))
    pag_cita = menciones[0]["pagina"] if menciones else None
    contexto = [fila(pag_cita, roles[pag_cita - 1], ln) for ln in pags[pag_cita - 1]
                if "retitulizaciones" in ln.texto or "3.6" in ln.texto] if pag_cita else []
    return OrderedDict([("pdf", "TO_capitales_minimos_actual.pdf"), ("lineas_de_la_seccion_3", seccion3),
                        ("lineas_que_nombran_3_6", menciones), ("cita", contexto),
                        ("existe_un_encabezado_3_6", any(re.match(r"^3\.6\.\s", m["texto"].strip()) for m in menciones))])


def b20() -> dict:
    pags, roles = lineas("TO_regimen_informativo_contable_mensual_actual.pdf")
    menciones, parrafo = [], []
    for i, p in enumerate(pags, 1):
        for ln in p:
            if "5.1.2" in ln.texto:
                menciones.append(fila(i, roles[i - 1], ln))
    pag = next(m["pagina"] for m in menciones if "5.1.2.1" in m["texto"])
    dentro = False
    for ln in pags[pag - 1]:
        t = ln.texto.strip()
        if t.startswith("12.1."):
            dentro = True
        if t.startswith("12.2."):
            dentro = False
        if dentro:
            parrafo.append(fila(pag, roles[pag - 1], ln))
    texto_1212 = " ".join(x["texto"] for x in parrafo[[i for i, x in enumerate(parrafo)
                                                       if x["texto"].strip().startswith("12.1.2.")][0]:])
    previo = texto_1212[:texto_1212.find("5.1.2.1")]
    return OrderedDict([
        ("pdf", "TO_regimen_informativo_contable_mensual_actual.pdf"), ("pagina_de_la_cita", pag),
        ("lineas_de_12_1_a_12_1_2", parrafo), ("lineas_que_nombran_5_1_2", menciones),
        ("texto_de_12_1_2", texto_1212),
        ("norma_nombrada_antes_de_la_cita_en_12_1_2", bool(re.search(
            r"normas?\s+sobre|[“\"«][A-Z]|Comunicaci[oó]n|texto\s+ordenado|\bT\.?O\.", previo))),
        ("existe_un_encabezado_5_1_2_1", any(m["texto"].strip().startswith("5.1.2.1.") for m in menciones))])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    out = OrderedDict([("B02", b02()), ("B20", b20())])
    (RAIZ / a.out).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("B02 encabezado 3.6:", out["B02"]["existe_un_encabezado_3_6"], "| B20 norma antes:",
          out["B20"]["norma_nombrada_antes_de_la_cita_en_12_1_2"], "encabezado 5.1.2.1:",
          out["B20"]["existe_un_encabezado_5_1_2_1"])


if __name__ == "__main__":
    main()
