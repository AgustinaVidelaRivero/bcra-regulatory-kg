"""Mesa, §237 (22/10/2026): las vigilancias de la tanda final contra su línea de base de la tanda 1, con un criterio propuesto por la mesa
(el de T5 es suyo y la meta no lo fija). Es el test de la atención de las lecturas (pre-registro de la tanda 1, 95b18217, §5.4 y §5.4 bis):
exacto, unilateral, al 5 %, contra la tasa de la tanda 1, en dos versiones: la cuenta cruda (binomial) y la tasa ponderada por celda (la
distribución de T = suma de w_c · k_c / n_c enumerada entera bajo la nula, cada celda con la tasa de la tanda 1). «Fuera» si p < 0,05; si
las dos versiones no dan lo mismo, va como hallazgo («ante la duda, hallazgo», decisión de la autora del 22/10/2026). Las contadas sin
leer: (4) y (5) son invariantes (1 TextoOrdenado por TO; 0 emisiones), (9) cuenta las emisiones fuera del dominio de pagos (los TOs snp_*),
y (8), la tasa, con el mismo test binomial. Lee t4/tasas/tasas_t4_tramo3.json y lo contado sin leer de T3 de las dos tandas; solo lee.
Uso: python3 -I -B criterio_vigilancias_mesa.py <repo> <salida.json>"""
import itertools
import json
import math
import re
import sys
from pathlib import Path

R, OUT = Path(sys.argv[1]), Path(sys.argv[2])
L = lambda p: json.loads((R / p).read_text(encoding="utf-8"))  # noqa: E731
t4 = L("data/experiment/tanda_final/t4/tasas/tasas_t4_tramo3.json")
base_txt = t4["lineas_de_base"]["vigilancias_y_12"]["tanda1"]
base = {f"vigilancia:{a}": (int(k), int(n)) for a, k, n in re.findall(r"\((\d+)\) (\d+) [^;]*? de (\d+)", base_txt) if a != "12"}
binom = lambda k, n, p: math.exp(math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1) + k * math.log(p)  # noqa: E731
                                 + (n - k) * math.log(1 - p))   # en logaritmos: las n de (8) desbordan la potencia
cola_sup = lambda k, n, p: sum(binom(i, n, p) for i in range(k, n + 1))  # noqa: E731
res = {"vigilancias_leidas": {}}
for m, (k0, n0) in base.items():
    v = t4["vigilancias"][m]
    p0 = k0 / n0
    k, n = v["cruda"]["k"], v["cruda"]["n"]
    x = {"tanda_final": f"{k} de {n}", "tanda1": f"{k0} de {n0}", "empeora": k / n > p0,
         "p_crudo_unilateral": round(cola_sup(k, n, p0), 4)}
    if "por_celda" in v and v.get("pesos"):
        cel = [(v["pesos"][c], v["por_celda"][c]["n"], v["por_celda"][c]["sí"] if "sí" in v["por_celda"][c] else None) for c in v["pesos"]]
        if all(c[2] is not None for c in cel):
            t_obs = sum(w * kk / nn for w, nn, kk in cel)
            p = 0.0
            for ks in itertools.product(*(range(nn + 1) for _, nn, _ in cel)):
                if sum(w * kk / nn for (w, nn, _), kk in zip(cel, ks)) >= t_obs - 1e-12:
                    p += math.prod(binom(kk, nn, p0) for (_, nn, _), kk in zip(cel, ks))
            x["ponderada"] = round(t_obs, 4)
            x["p_ponderado_unilateral"] = round(p, 4)
    fc = x["p_crudo_unilateral"] < 0.05
    fp = x.get("p_ponderado_unilateral", 1.0) < 0.05 if "p_ponderado_unilateral" in x else fc
    x["fuera_crudo"], x["fuera_ponderado"] = fc, fp
    x["hallazgo"] = x["empeora"] and (fc or fp)
    x["por_que"] = ("las dos versiones dan fuera" if fc and fp else "las dos versiones no dan lo mismo: ante la duda, hallazgo" if fc != fp
                    else "ninguna da fuera") if x["empeora"] else "no empeora"
    res["vigilancias_leidas"][m] = x
cs = {g: L(f)["grafos"][g]["vigilancias"] for f, g in (("data/experiment/tanda_final/t3/conteos_sin_leer/contado_sin_leer_tf.json", "tf98"),
                                                       ("data/experiment/tanda1/t3/conteos_sin_leer/contado_sin_leer_t3f.json", "veinte"))}
tf, t1 = cs["tf98"], cs["veinte"]
fuera_pagos = lambda v: sum(x for to, x in v["9"]["emisiones_E1_por_to"].items() if not to.startswith("snp_"))  # noqa: E731
p8 = t1["8"]["sujeto_propuesto"] / t1["8"]["sujeto_id"]
res["contadas_sin_leer"] = {
    "4_un_TextoOrdenado_por_TO": {"tanda_final": tf["4"]["uno_por_to"], "tanda1": t1["4"]["uno_por_to"], "hallazgo": not tf["4"]["uno_por_to"]},
    "5_emisiones_de_vocabulario_retirado": {"tanda_final": tf["5"]["total"], "hallazgo": sum(tf["5"]["total"].values()) != 0},
    "8_sujeto_propuesto": {"tanda_final": f"{tf['8']['sujeto_propuesto']} de {tf['8']['sujeto_id']} ({tf['8']['tasa_pct']} %)",
                           "tanda1": f"{t1['8']['sujeto_propuesto']} de {t1['8']['sujeto_id']} ({t1['8']['tasa_pct']} %)",
                           "p_unilateral": round(cola_sup(tf["8"]["sujeto_propuesto"], tf["8"]["sujeto_id"], p8), 4),
                           "hallazgo": cola_sup(tf["8"]["sujeto_propuesto"], tf["8"]["sujeto_id"], p8) < 0.05},
    "9_originante_fuera_de_pagos": {"tanda_final": {"total": tf["9"]["emisiones_E1_total"], "fuera_de_los_TOs_snp": fuera_pagos(tf)},
                                    "tanda1": {"total": t1["9"]["emisiones_E1_total"], "fuera_de_los_TOs_snp": fuera_pagos(t1)},
                                    "hallazgo": fuera_pagos(tf) > 0}}
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(res, ensure_ascii=False, indent=1))
