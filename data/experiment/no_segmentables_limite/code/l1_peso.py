"""U-NOSEG-LIMITE, L1 — peso de los 14 TOs fuera de las tandas sobre el universo de 152.

Solo lectura, USD 0. Lee la partición de B5.8.4 y las salidas medidas de U-COB-A;
escribe `l1_peso.json` y `l1_peso.md` en el directorio de la unidad.

Fuentes (todas rastreadas):
  - data/experiment/segmentacion_84/b584_particion/particion_152.json (`por_to`, `agregados`)
  - data/experiment/segmentacion_84/b584_particion/conteos_b584.json (`roles_pagina`)
  - data/experiment/segmentacion_84/b584_particion/adjudicaciones_b584.json (`e_no_segmentables`)
  - data/experiment/escalado_prep/inventario_tos.csv (`categoria`)
  - data/experiment/cobertura_bloque_a/chunks_a2.json (191 unidades `bloque_pagina`, campo `brazo`)
  - data/experiment/no_segmentables_limite/l2_regla_parciales.json (salida de l2_parciales.py),
    si existe, para el volumen de la parte por punto de los parciales.

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/no_segmentables_limite/code/l1_peso.py
"""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
PART = REPO / "data" / "experiment" / "segmentacion_84" / "b584_particion"
INV = REPO / "data" / "experiment" / "escalado_prep" / "inventario_tos.csv"
COBA = REPO / "data" / "experiment" / "cobertura_bloque_a"
OUT = REPO / "data" / "experiment" / "no_segmentables_limite"

ROLES = ("ficha_registro", "cuerpo", "historial", "indice", "portada", "tabla_norma_origen")


def pct(a: int, b: int) -> str:
    return f"{100 * a / b:.1f}".replace(".", ",")


def main() -> None:
    part = json.loads((PART / "particion_152.json").read_text(encoding="utf-8"))
    cont = json.loads((PART / "conteos_b584.json").read_text(encoding="utf-8"))
    adj = json.loads((PART / "adjudicaciones_b584.json").read_text(encoding="utf-8"))
    with INV.open(encoding="utf-8") as f:
        cat = {r["id"]: r["categoria"] for r in csv.DictReader(f)}

    por_to = part["por_to"]
    tot_pag = sum(v["paginas"] for v in por_to.values())
    tot_uni = sum(v["unidades"] for v in por_to.values())
    assert len(por_to) == 152
    # control contra el agregado declarado por el propio artefacto
    agr = part["agregados"]
    assert tot_pag == sum(a["paginas"] for a in agr.values())
    assert tot_uni == sum(a["unidades"] for a in agr.values())

    catorce = sorted(t for t, v in por_to.items() if v["clase"] != "reconocido_pleno")
    no_seg = {e["to"] for e in adj["e_no_segmentables"]}
    filas = []
    for t in catorce:
        v = por_to[t]
        roles = cont[t]["roles_pagina"]
        assert sum(roles.values()) == v["paginas"], t
        filas.append({
            "to": t,
            "clase": v["clase"],
            "categoria_inventario": cat[t],
            "paginas": v["paginas"],
            "pct_paginas_universo": pct(v["paginas"], tot_pag),
            "unidades_particion": v["unidades"],
            "pct_unidades_universo": pct(v["unidades"], tot_uni),
            "roles_pagina": {r: roles.get(r, 0) for r in ROLES},
            "modo_lectura": cont[t]["modo_lectura"],
            "en_e_no_segmentables": t in no_seg,
        })

    def suma(sel):
        s = [f for f in filas if sel(f)]
        roles = Counter()
        for f in s:
            roles.update(f["roles_pagina"])
        p = sum(f["paginas"] for f in s)
        u = sum(f["unidades_particion"] for f in s)
        return {"tos": len(s), "paginas": p, "pct_paginas": pct(p, tot_pag),
                "unidades": u, "pct_unidades": pct(u, tot_uni),
                "roles_pagina": {r: roles.get(r, 0) for r in ROLES}}

    clases = {
        "parcial_declarado": suma(lambda f: f["clase"] == "parcial_declarado"),
        "no_segmentable_declarado": suma(lambda f: f["clase"] == "no_segmentable_declarado"),
        "los_14": suma(lambda f: True),
    }
    assert clases["los_14"]["tos"] == 14

    # páginas de ficha en todo el universo y dentro de TOs que sí entran
    ficha_total = sum(c["roles_pagina"].get("ficha_registro", 0) for c in cont.values())
    ficha_que_entran = {t: c["roles_pagina"]["ficha_registro"] for t, c in sorted(cont.items())
                        if c["roles_pagina"].get("ficha_registro", 0) and t not in catorce}

    # volumen medido de U-COB-A por brazo (chunks_a2.json)
    a2 = json.loads((COBA / "chunks_a2.json").read_text(encoding="utf-8"))
    brazo = Counter(c["brazo"] for c in a2)
    brazo_to = Counter((c["to"], c["brazo"]) for c in a2)
    pags_brazo = {b: len({(c["to"], p) for c in a2 if c["brazo"] == b for p in c["paginas"]})
                  for b in brazo}

    l2 = OUT / "l2_regla_parciales.json"
    l2d = json.loads(l2.read_text(encoding="utf-8")) if l2.exists() else None

    res = {
        "_meta": {
            "unidad": "U-NOSEG-LIMITE, L1",
            "denominadores": {"tos": 152, "paginas": tot_pag, "unidades_particion": tot_uni},
            "fuentes": [str(p.relative_to(REPO)) for p in (PART / "particion_152.json",
                        PART / "conteos_b584.json", PART / "adjudicaciones_b584.json", INV,
                        COBA / "chunks_a2.json")],
        },
        "por_clase": clases,
        "por_to": filas,
        "ficha_registro": {"total_universo": ficha_total,
                           "en_parciales": {f["to"]: f["roles_pagina"]["ficha_registro"]
                                            for f in filas if f["clase"] == "parcial_declarado"},
                           "en_no_segmentables": {f["to"]: f["roles_pagina"]["ficha_registro"]
                                                  for f in filas if f["clase"] == "no_segmentable_declarado"
                                                  and f["roles_pagina"]["ficha_registro"]},
                           "en_tos_que_entran": ficha_que_entran},
        "u_cob_a_medido": {"unidades_por_brazo": dict(brazo),
                           "paginas_por_brazo": pags_brazo,
                           "unidades_por_to_y_brazo": {f"{t}|{b}": n for (t, b), n in sorted(brazo_to.items())}},
        "parciales_regla_l2": (l2d["resumen"] if l2d else "l2_regla_parciales.json ausente"),
    }
    (OUT / "l1_peso.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    # tabla en markdown
    L = ["# L1 — peso de los 14 TOs fuera de las tandas (generado por code/l1_peso.py)", "",
         f"Denominadores: 152 TOs, {tot_pag} páginas, {tot_uni} unidades de la partición "
         "(`particion_152.json`, `por_to`; controlado contra `agregados`).", "",
         "| clase | TOs | páginas | % pág. | unidades | % unid. | ficha | cuerpo | historial | índice | portada | tabla origen |",
         "|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|"]
    for k, c in clases.items():
        r = c["roles_pagina"]
        L.append(f"| {k} | {c['tos']} | {c['paginas']} | {c['pct_paginas']} | {c['unidades']} | {c['pct_unidades']} | "
                 + " | ".join(str(r[x]) for x in ROLES) + " |")
    L += ["", "| TO | clase | categoría | páginas | % pág. | unidades | ficha | cuerpo | historial | índice | portada | tabla origen | modo |",
          "|---|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|"]
    for f in filas:
        r = f["roles_pagina"]
        L.append(f"| {f['to']} | {f['clase']} | {f['categoria_inventario']} | {f['paginas']} | {f['pct_paginas_universo']} | "
                 f"{f['unidades_particion']} | " + " | ".join(str(r[x]) for x in ROLES) + f" | {f['modo_lectura']} |")
    L += ["", f"Páginas `ficha_registro` en el universo: {ficha_total}. En TOs que entran a las tandas: "
          + ", ".join(f"{t} {n}" for t, n in ficha_que_entran.items()) + ".", ""]
    (OUT / "l1_peso.md").write_text("\n".join(L), encoding="utf-8")
    print(json.dumps({"por_clase": clases, "ficha": res["ficha_registro"], "u_cob_a": res["u_cob_a_medido"]},
                     ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
