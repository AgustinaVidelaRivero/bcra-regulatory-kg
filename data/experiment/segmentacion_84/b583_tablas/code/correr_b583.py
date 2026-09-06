#!/usr/bin/env python3
"""B5.8.3 — corrida del parser de tablas (e0_tablas.py) sobre los TOs
objetivo, recomputados (regla i de CLAUDE.md §4) de dos fuentes selladas:

  (1) censo B5.8.0 (censo_84.json): TOs con familia tabular 'd' o
      'd_dominante' entre sus secundarias;
  (2) corrida B5.8.1 (conteos_b581.json): TOs con páginas declaradas
      ficha_registro (roles_pagina.ficha_registro > 0) — los parciales cuyo
      material quedó fuera del parseo de prosa con destino B5.8.3.

CONTROL TESTIGO OBLIGATORIO (RX-10): capmin (dev, SOLO LECTURA) — la tabla
de montos del punto 1.2 debe parsearse con bancos 5.000 / restantes 2.500,
el par que la linealización a prosa invirtió en el grafo
(docs/backlog_reextraccion.md §RX-10). No integra el objetivo del censo:
sus artefactos van a ../testigo_capmin/.

Cero LLM, USD 0. Salidas por TO en ../<to>/: tablas_<to>.json (tablas
lógicas completas con provenance, filas, verificación de reconstrucción,
notas al pie, costuras candidatas, descartes por regla) y resumen_<to>.json.
Consolidado: ../conteos_b583.json.

Uso (desde cualquier cwd):
    python3 data/experiment/segmentacion_84/b583_tablas/code/correr_b583.py [--solo TO1,TO2]
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[5]
E0_DIR = REPO / "data/experiment/reextraccion_v2/e0_chunking"
PREP = REPO / "data/experiment/escalado_prep"
CENSO = REPO / "data/experiment/segmentacion_84/censo_84.json"
CONTEOS_B581 = REPO / "data/experiment/segmentacion_84/b581_sin_raiz/conteos_b581.json"
SALIDA = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(E0_DIR))
import e0_tablas as T  # noqa: E402

PDF_TESTIGO = REPO / "data/experiment/subset/TO_capitales_minimos_actual.pdf"


def tos_objetivo() -> tuple[list[str], list[str], list[str]]:
    """(objetivo, de_censo, de_b581) — recomputado, no transcripto."""
    censo = json.load(open(CENSO, encoding="utf-8"))
    de_censo = sorted(t for t, d in censo.items()
                      if set(d.get("secundarias", [])) & {"d", "d_dominante"})
    b581 = json.load(open(CONTEOS_B581, encoding="utf-8"))
    de_b581 = sorted(t for t, d in b581.items()
                     if d.get("roles_pagina", {}).get("ficha_registro", 0) > 0)
    return sorted(set(de_censo) | set(de_b581)), de_censo, de_b581


def correr_to(ident: str, pdf: Path) -> dict:
    t0 = time.time()
    res = T.parsear_to(pdf, ident)
    segundos = round(time.time() - t0, 1)

    d = SALIDA / ident
    d.mkdir(parents=True, exist_ok=True)
    (d / f"tablas_{ident}.json").write_text(
        json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")

    declaradas = [{"id": t["id"], "causas": t["causas"],
                   "pagina": t["segmentos"][0]["pagina"],
                   "pct_perdida_max": t["declaraciones"]["pct_perdida_max"],
                   "colapsos": t["declaraciones"]["colapsos"]}
                  for t in res["tablas_logicas"] if t["estado"] == "declarada"]
    resumen = {
        "to": ident,
        "archivo": res["archivo"],
        "paginas": res["paginas"],
        **res["conteos"],
        "declaradas_detalle": declaradas,
        "costuras_candidatas": res["costuras_candidatas"],
        "descartadas_por_regla": res["descartadas_por_regla"]["conteos"],
        "chars_perdidos_total": sum(t["declaraciones"]["chars_perdidos_total"]
                                    for t in res["tablas_logicas"]),
        "titulos_detectados": sum(1 for t in res["tablas_logicas"]
                                  if t["encabezado"]["titulo"]),
        "encabezados_determinados": sum(1 for t in res["tablas_logicas"]
                                        if t["encabezado"]["estado"] == "determinado"),
        "segundos": segundos,
    }
    (d / f"resumen_{ident}.json").write_text(
        json.dumps(resumen, ensure_ascii=False, indent=1), encoding="utf-8")
    return resumen


def correr_testigo() -> dict:
    """capmin 1.2 (RX-10): la verificación es programática y queda escrita."""
    res = T.parsear_to(PDF_TESTIGO, "capmin")
    d = SALIDA / "testigo_capmin"
    d.mkdir(parents=True, exist_ok=True)
    (d / "tablas_capmin.json").write_text(
        json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")

    tabla = next((t for t in res["tablas_logicas"]
                  if t["segmentos"][0]["pagina"] == 4), None)
    filas = tabla["segmentos"][0]["filas"] if tabla else []
    pares = (dict(zip([c.split("\n")[0] for c in filas[0]], filas[-1]))
             if filas else {})
    veredicto = {
        "defecto": "RX-10 — linealización de tablas del articulado: el chunk "
                   "de capmin 1.2 traía 'Restantes entidades Bancos … 5.000 "
                   "2.500' y el grafo quedó con los montos invertidos",
        "tabla": tabla["id"] if tabla else None,
        "estado": tabla["estado"] if tabla else None,
        "provenance": {"pagina": 4,
                       "indice_en_pagina": tabla["segmentos"][0]["indice_en_pagina"]
                       if tabla else None,
                       "bbox": tabla["segmentos"][0]["bbox"] if tabla else None},
        "filas": filas,
        "pares_por_columna": pares,
        "esperado": {"Bancos": "5.000", "Restantes entidades": "2.500"},
        "pct_perdida": tabla["declaraciones"]["pct_perdida_max"] if tabla else None,
        "resuelto": pares == {"Bancos": "5.000", "Restantes entidades": "2.500"}
        and bool(tabla) and tabla["estado"] == "parseada"
        and tabla["declaraciones"]["pct_perdida_max"] == 0.0,
    }
    (d / "testigo_rx10.json").write_text(
        json.dumps(veredicto, ensure_ascii=False, indent=1), encoding="utf-8")
    return veredicto


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo", help="lista de TOs separada por coma")
    args = ap.parse_args()

    objetivo, de_censo, de_b581 = tos_objetivo()
    print(f"objetivo: {len(objetivo)} TOs "
          f"(censo d/d_dominante: {len(de_censo)}; "
          f"ficha_registro B5.8.1: {len(de_b581)}; "
          f"solo por B5.8.1: {sorted(set(de_b581) - set(de_censo))})")
    if args.solo:
        objetivo = [t for t in objetivo if t in args.solo.split(",")]

    consolidado: dict[str, dict] = {}
    for ident in objetivo:
        pdf = PREP / "pdfs" / f"{ident}.pdf"
        r = correr_to(ident, pdf)
        consolidado[ident] = r
        print(f"  {ident}: logicas={r['tablas_logicas']} parseadas={r['parseadas']} "
              f"declaradas={r['declaradas']} segmentos={r['segmentos']} "
              f"rinde={'sí' if r['rinde'] else 'NO'} ({r['segundos']}s)")

    veredicto = correr_testigo()
    print(f"testigo capmin RX-10: resuelto={veredicto['resuelto']} "
          f"pares={veredicto['pares_por_columna']}")

    meta = {"objetivo": objetivo, "de_censo": de_censo, "de_b581": de_b581,
            "testigo_rx10_resuelto": veredicto["resuelto"]}
    (SALIDA / "conteos_b583.json").write_text(
        json.dumps({"_meta": meta, **consolidado},
                   ensure_ascii=False, indent=1), encoding="utf-8")
    rinden = sum(1 for r in consolidado.values() if r["rinde"])
    print(f"listo: rinden {rinden}/{len(consolidado)}; "
          f"consolidado en {SALIDA / 'conteos_b583.json'}")


if __name__ == "__main__":
    main()
