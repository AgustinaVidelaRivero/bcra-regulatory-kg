"""U-R2-CODIGO, R1.e — qué paso de la E0 legada perdió las líneas de
encabezado de tabla de `cap::2.12.2.6` y `ric::S2`, y si e0-r2 las recupera.

Para cada caso: corre `separar_encabezado_pie` de e0_lib (sin editarlo, solo
lectura del PDF) sobre la página de la tabla, lista las líneas que descarta
como encabezado de página y, de ellas, las que tienen el texto de una fila de
la tabla; dice si esas líneas están en el texto del chunk legado y en el del
chunk e0-r2 (dentro de su bloque, si la tabla se serializó). USD 0.

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B \\
    data/experiment/r2_codigo/r1e_lineas_perdidas.py --e0-r2 <salida e0-r2> --out <json>
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
sys.path.insert(0, str(REX / "e0_chunking"))
import e0_lib as E0  # noqa: E402

E0_LEGADA = REX / "e0_chunking" / "salida_tanda0"
CASOS = (
    {"chunk": "cap::2.12.2.6", "tabla": "cap::tabla2f002", "pagina": 24,
     "pdf": REPO / "data" / "experiment" / "subset" / "TO_capitales_minimos_actual.pdf"},
    {"chunk": "ric::S2", "tabla": "ric::tabla000", "pagina": 4,
     "pdf": REPO / "data" / "experiment" / "subset"
     / "TO_regimen_informativo_contable_mensual_actual.pdf"},
)


def _tokens(t: str) -> list[str]:
    return [w for w in t.replace("\n", " ").split() if w]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--e0-r2", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    out = {"unidad": "U-R2-CODIGO", "etapa": "R1.e",
           "paso": "e0_lib.separar_encabezado_pie: zona de encabezado (primeras 5 líneas "
                   "de la página); descarta la línea si _es_titulo_mayusculas (sin "
                   "minúsculas) o contiene 'B.C.R.A.'",
           "casos": []}
    for caso in CASOS:
        to = caso["chunk"].split("::")[0]
        paginas = E0.extraer_lineas(caso["pdf"])
        _, descartadas, _ = E0.separar_encabezado_pie(paginas[caso["pagina"] - 1])
        tabla = next(t for t in json.loads((Path(a.e0_r2) / f"tablas_{to}.json")
                                           .read_text(encoding="utf-8"))["tablas"]
                     if t["id"] == caso["tabla"])
        tokens_celdas = {w for s in tabla["segmentos"] for f in s["filas"] for c in f
                         for w in _tokens(c or "")}
        de_tabla = [l for l in descartadas
                    if _tokens(l.texto) and all(w in tokens_celdas for w in _tokens(l.texto))]
        leg = {c["id"]: c for c in json.loads((E0_LEGADA / f"chunks_{to}.json")
                                              .read_text(encoding="utf-8"))}[caso["chunk"]]
        r2 = {c["id"]: c for c in json.loads((Path(a.e0_r2) / f"chunks_{to}.json")
                                             .read_text(encoding="utf-8"))}[caso["chunk"]]
        ser = tabla["serializacion"]
        bloque = ser.get("bloque") or ""
        lineas = []
        for l in de_tabla:
            tok = _tokens(l.texto)
            lineas.append({
                "pagina": l.pagina, "top": l.top, "texto": l.texto,
                "titulo_mayusculas": E0._es_titulo_mayusculas(l.texto.strip()),
                "en_texto_legado": l.texto in leg["texto"].split("\n"),
                "tokens_en_bloque_e0r2": bool(bloque) and all(w in _tokens(bloque) for w in tok),
            })
        out["casos"].append({
            "chunk": caso["chunk"], "tabla": caso["tabla"], "pagina": caso["pagina"],
            "descartadas_como_encabezado": [{"top": l.top, "texto": l.texto}
                                            for l in descartadas],
            "lineas_de_la_tabla_descartadas": lineas,
            "serializada_en_e0r2": ser["serializada"],
            "motivo_no_serializada": ser.get("motivo"),
            "recuperadas_en_e0r2": bool(lineas) and all(x["tokens_en_bloque_e0r2"]
                                                         for x in lineas),
            "texto_r2_igual_al_legado": r2["texto"] == leg["texto"],
        })
    Path(a.out).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n",
                           encoding="utf-8")


if __name__ == "__main__":
    main()
