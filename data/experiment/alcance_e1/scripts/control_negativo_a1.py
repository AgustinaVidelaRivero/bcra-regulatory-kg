"""U-ALCANCE-E1, A1: lee tres consolas de selftest_prompt_r2b (el de HEAD sobre HEAD, el nuevo sobre la copia y el nuevo con
el código de HEAD) y controla que el código de HEAD falle exactamente los casos nuevos. Uso: control_negativo_a1.py H N C OUT"""
import json
import re
import sys
from pathlib import Path


def leer(p):
    ok, fail = [], []
    for l in Path(p).read_text(encoding="utf-8").splitlines():
        if l.startswith("  ok  "):
            ok.append(l[6:])
        elif l.startswith("  FAIL "):
            fail.append(l[7:])
    tot = re.search(r"RESULTADO: (\d+) ok, (\d+) FAIL", Path(p).read_text(encoding="utf-8"))
    return ok, fail, (int(tot.group(1)), int(tot.group(2)))


h_ok, h_fail, h_tot = leer(sys.argv[1])
n_ok, n_fail, n_tot = leer(sys.argv[2])
c_ok, c_fail, c_tot = leer(sys.argv[3])
nuevos = [x for x in n_ok if x not in h_ok]                 # casos nuevos o reescritos
reescritos = [x for x in nuevos if x in c_ok]               # pasan también con HEAD: los reescritos
casos_nuevos = [x for x in nuevos if x not in reescritos]
fallan = [next((x for x in casos_nuevos if f.startswith(x)), None) for f in c_fail]
res = {
    "head_sobre_head": h_tot, "nuevo_sobre_la_copia": n_tot, "nuevo_con_codigo_head": c_tot,
    "casos_nuevos": len(casos_nuevos), "casos_reescritos": reescritos,
    "de_head_que_ya_no_estan": [x for x in h_ok if x not in n_ok],
    "fallan_con_head_y_son_nuevos": sum(x is not None for x in fallan),
    "fallan_con_head_y_no_son_nuevos": [f for f, x in zip(c_fail, fallan) if x is None],
    "nuevos_que_no_fallan_con_head": [x for x in casos_nuevos if x not in fallan],
    "fallan_por_atributo_que_falta": sum("AttributeError" in f for f in c_fail),
}
res["exactamente_los_nuevos"] = (not res["fallan_con_head_y_no_son_nuevos"] and not res["nuevos_que_no_fallan_con_head"]
                                 and res["fallan_con_head_y_son_nuevos"] == len(casos_nuevos) == c_tot[1]
                                 and n_tot[1] == 0 and h_tot[1] == 0)
Path(sys.argv[4]).write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(res, ensure_ascii=False, indent=1))
