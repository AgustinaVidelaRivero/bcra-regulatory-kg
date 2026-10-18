"""U-ALCANCE-E1, A3: lee tres consolas de selftest_prompt_r2b (el de HEAD sobre HEAD, el de A3 sobre su copia y el de A3 con
el código de HEAD) y controla que el código de HEAD falle exactamente el caso nuevo (criterio 5 del mandato de A3). Sigue a
control_negativo_a2.py: un caso del selftest de A3 que no está en el de HEAD es nuevo si falla con el código de HEAD, y
reescrito si pasa. Uso: control_negativo_a3.py H N C OUT"""
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
    "head_sobre_head": h_tot, "a3_sobre_su_copia": n_tot, "a3_con_codigo_head": c_tot,
    "casos_nuevos": casos_nuevos, "casos_reescritos": reescritos,
    "de_head_que_ya_no_estan": [x for x in h_ok if x not in n_ok],
    "fallan_con_head_y_son_nuevos": sum(x is not None for x in fallan),
    "fallan_con_head_y_no_son_nuevos": [f for f, x in zip(c_fail, fallan) if x is None],
    "nuevos_que_no_fallan_con_head": [x for x in casos_nuevos if x not in fallan],
    "detalle_del_fallo_con_head": [f[len(x):].strip() for f, x in zip(c_fail, fallan) if x is not None],
}
res["exactamente_el_caso_nuevo"] = (len(casos_nuevos) == 1 and not res["fallan_con_head_y_no_son_nuevos"]
                                    and not res["nuevos_que_no_fallan_con_head"]
                                    and res["fallan_con_head_y_son_nuevos"] == 1 == c_tot[1]
                                    and n_tot[1] == 0 and h_tot[1] == 0
                                    and len(res["de_head_que_ya_no_estan"]) == len(reescritos))
Path(sys.argv[4]).write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(res, ensure_ascii=False, indent=1))
