"""B6.1, tanda 1, T3, punto 3: los `nombres_remision` de cada TO en los manifiestos de ensamblado del acumulado, contra los del manifiesto
de su tanda (la tanda 0 re-sellada y la tanda 1). Solo compara los campos de los manifiestos; no mide qué remisiones mueve el cambio.
Solo lee <raíz>; escribe <salida.json> y lo imprime.
Uso: python3 -I -B nombres_acumulado_t3.py <raíz> <salida.json>
"""
import json
import sys
from pathlib import Path

RAIZ, OUT = Path(sys.argv[1]), Path(sys.argv[2])
M = "data/experiment/reextraccion_v2/manifiestos"
A = "data/experiment/tanda1/t3/acumulado/manifiestos"
PARES = {"acumulado_ens_treinta_r2b": {"tanda0": f"{M}/tanda0_ens_diez_r2b_rs1.json", "tanda1": f"{M}/tanda1_ens_veinte_r2b.json"},
         "acumulado_ens_treinta_r2b_sincola": {"tanda0": f"{M}/tanda0_ens_diez_r2b_sincola_rs1.json",
                                               "tanda1": f"{M}/tanda1_ens_veinte_r2b_sincola.json"}}


def tos(rel: str) -> dict:
    return {t["id"]: t.get("nombres_remision") for t in json.loads((RAIZ / rel).read_text(encoding="utf-8"))["tos"]}


res = {}
for acu, origen in PARES.items():
    a = tos(f"{A}/{acu}.json")
    r = {"acumulado": f"{A}/{acu}.json", "tos": len(a), "con_nombres": sum(1 for v in a.values() if v)}
    for tanda, rel in origen.items():
        o = tos(rel)
        r[tanda] = {"manifiesto": rel, "tos": len(o), "con_nombres_en_su_manifiesto": sum(1 for v in o.values() if v),
                    "con_nombres_en_el_acumulado": sum(1 for k in o if a[k]),
                    "distintos": sorted(k for k in o if a[k] != o[k])}
    res[acu] = r
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for acu, r in res.items():
    print(f"{acu}: {r['tos']} TOs, {r['con_nombres']} con nombres")
    for tanda in ("tanda0", "tanda1"):
        t = r[tanda]
        print(f"  {tanda}: {t['tos']} TOs; con nombres en su manifiesto {t['con_nombres_en_su_manifiesto']}, en el acumulado "
              f"{t['con_nombres_en_el_acumulado']}; distintos {len(t['distintos'])}: {t['distintos']}")
