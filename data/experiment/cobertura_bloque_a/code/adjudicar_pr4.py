"""Adjudicacion de causa del 16,9 % de PR-4: reparto entre las tres
explicaciones, medido y no leido. Sin API. Uso: python3 adjudicar_pr4.py

Insumos: la particion manual de los 24 casos (clasificada DESPUES de sellar
`criterio_destinatario.md`), el censo de forma, la medicion de A.2 y el
corpus de desarrollo.
"""
from __future__ import annotations

import glob
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import comun_coba as C  # noqa: E402
import senal_sujeto as SS  # noqa: E402

E1 = C.EXPERIMENT / "reextraccion_v2/e1_extractor"
if str(E1) not in sys.path:
    sys.path.insert(0, str(E1))
import prompt_e1 as P  # noqa: E402

CRITERIO_SHA = "f5066c12a906b2e3720e2b62d1cb9db2cb45bdcfc91bb91d46c77d3ab843204a"
E0_DEV = C.EXPERIMENT / "reextraccion_v2/e0_chunking/salida_enm01"


def main() -> int:
    sha = hashlib.sha256(
        (C.UNIDAD / "criterio_destinatario.md").read_bytes()).hexdigest()
    assert sha == CRITERIO_SHA, f"el criterio cambio: {sha}"

    part = json.loads((C.UNIDAD / "particion_24_casos.json").read_text(encoding="utf-8"))
    med = json.loads((C.UNIDAD / "medicion_a2.json").read_text(encoding="utf-8"))
    censo = json.loads((C.UNIDAD / "censo_forma.json").read_text(encoding="utf-8"))
    p2 = Counter(c["clase"] for c in part["prioridad_2"])
    p1 = Counter(c["clase"] for c in part["prioridad_1"])
    cr = med["PR4_cruce_2x2"]["agregado"]
    conc = cr["CONCORDANTE"]

    # --- (a) reparto de los 22 de P2 ---
    reparto = {
        "(ii) falla de la MARCA — la mencion NO era destinatario": {
            "casos": p2["B"], "de": 22, "fraccion": round(p2["B"] / 22, 3),
            "subclases": dict(Counter(c["subclase"] for c in part["prioridad_2"]
                                      if c["clase"] == "B")),
        },
        "(i) falla del MODELO — destinatario no emitido": {
            "casos": p2["A"], "de": 22, "fraccion": round(p2["A"] / 22, 3),
            "de_ellos_chapeau_huerfano": sum(
                1 for c in part["prioridad_2"]
                if c["clase"] == "A" and "CHAPEAU HUERFANO" in c["lectura"]),
            "de_ellos_ambiguos_resueltos_contra_el_instrumento": sum(
                1 for c in part["prioridad_2"]
                if c["clase"] == "A" and c["lectura"].startswith("AMBIGUO")),
        },
    }

    # --- (b) las 14 de ri_tii contra el censo de forma ---
    pag = {d["pagina"]: d for d in censo["bloque_a_extraccion"]["ri_tii"]["paginas_detalle"]}
    tii = [c for c in med["PR4_cruce_2x2"]["casos"]
           ["MENCION LITERAL SIN EMISION - PRIORIDAD 2"] if c["to"] == "ri_tii"]
    b = Counter()
    for c in tii:
        p = int(c["chunk_id"].split("::p")[1].split(".")[0])
        b[(pag[p]["clase_forma"], pag[p]["tabla_b583"])] += 1
    contra_censo = {
        "casos_de_ri_tii_en_P2": len(tii),
        "reparto_clase_forma_x_tabla_b583": {f"{k[0]} / tabla={k[1]}": v
                                             for k, v in b.items()},
        "paginas_con_tabla_del_TO": censo["bloque_a_extraccion"]["ri_tii"]["b583_paginas_con_tabla"],
        "conclusion": "las 14 caen TODAS en paginas de prosa SIN tabla logica: "
                      "la contaminacion tabular NO las explica",
    }

    # --- (c) el arnes contra el corpus de desarrollo ---
    dev = []
    for f in sorted(glob.glob(str(E0_DEV / "chunks_*.json"))):
        dev += json.loads(Path(f).read_text(encoding="utf-8"))
    pats = SS.formas_de_superficie()
    men = lambda t: any(p.search(t or "") for p in pats.values())  # noqa: E731
    con_titulo = sum(1 for c in dev if (c.get("titulo") or "").strip())
    solo_tit = sum(1 for c in dev if men(c.get("titulo")) and not men(c.get("texto")))
    cuerpo = sum(1 for c in dev if men(c.get("texto")))
    rotulo_dev = [l for l in P.build_user_message(
        next(c for c in dev if c.get("tipo") == "punto_terminal")).splitlines()
        if l.startswith("Tipo de unidad")][0]
    arnes = {
        "dev_unidades": len(dev),
        "dev_con_titulo_no_vacio": f"{con_titulo}/{len(dev)} = {con_titulo/len(dev):.1%}",
        "A2_con_titulo_no_vacio": "0/191 = 0,0 %",
        "dev_valores_de_tipo": dict(Counter(c.get("tipo") for c in dev)),
        "chunk_de_punto_es_valor_de_tipo": "chunk de punto" in
                                           {c.get("tipo") for c in dev},
        "rotulo_que_imprime_dev": rotulo_dev,
        "rotulo_que_imprime_A2": "Tipo de unidad: chunk de punto",
        "rotulos_identicos": rotulo_dev == "Tipo de unidad: chunk de punto",
        "iii_a_dev_unica_mencion_en_titulo":
            f"{solo_tit}/{len(dev)} = {solo_tit/len(dev):.1%}",
        "iii_a_desplazamiento_del_techo":
            f"{cuerpo}/{len(dev)} = {cuerpo/len(dev):.1%} -> "
            f"{cuerpo+solo_tit}/{len(dev)} = {(cuerpo+solo_tit)/len(dev):.1%}",
    }

    # --- recalculo del piso sobre destinatarios IDENTIFICADOS ---
    dest = conc + p2["A"] + p1["C"]
    piso = {
        "_salvedad": "los CONCORDANTE no fueron revisados por el criterio: se "
                     "cuentan como destinatario sin verificar, que es la "
                     "lectura MAS favorable al piso",
        "marcadas_por_la_marca_literal": conc + p2["B"] + p2["A"],
        "con_destinatario_identificado": dest,
        "detalle": f"{conc} CONCORDANTE (no revisados) + {p2['A']} clase A + "
                   f"{p1['C']} clase C (fuera de la marca)",
        "piso_declarado_en_el_prerregistro": "33/77 = 42,9 %",
        "piso_recalculado": f"{dest}/77 = {dest/77:.1%}",
        "emitido": f"13/77 = {13/77:.1%}",
        "recuperacion_sobre_destinatarios_identificados":
            f"13/{dest} = {13/dest:.1%}",
    }

    out = {"_meta": {"criterio_sha256": CRITERIO_SHA,
                     "orden": "criterio sellado ANTES de clasificar",
                     "_ETAPA": "1 de 3 — SUPERSEDED. Previo a revisar los 11 "
                               "CONCORDANTE y a censar los 42 silencios; las "
                               "cifras vigentes estan en "
                               "recomputo_concordantes.json"},
           "a_reparto_de_los_22": reparto,
           "a_prioridad_1": {"clases": dict(p1),
                             "conclusion": "cero invencion (D); los 2 son "
                                           "FALSOS NEGATIVOS de la marca"},
           "b_ri_tii_contra_censo": contra_censo,
           "c_arnes_contra_dev": arnes,
           "recalculo_del_piso": piso}

    salida = C.UNIDAD / "adjudicacion_pr4.json"
    salida.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n",
                      encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=1))
    print(f"\nescrito: {salida.relative_to(C.REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
