"""B6.1, tanda final, T4, segundo tramo: verificación independiente de tasas_t4t2_tf.py. No importa el script de la mesa ni tasas_t4t2_tf.py:
recuenta las marcadas por celda, toma los N por celda de umbrales_t4_tf.json y las tasas de la tanda 0 que da el script de la mesa (6 de 30
en ítems y 4 de 30 en no ítems, leídas de su texto con una expresión regular), y recalcula con fracciones exactas:
  - la tasa ponderada de cada estrato, su n efectivo de Kish y su Wilson (fórmula escrita aquí, z = 1,959964);
  - el p-valor de la atención, P(T' >= T) bajo H0, por convolución exacta de las binomiales de cada celda (probabilidades en Fraction);
  - el freno por intervalos: el límite inferior del Wilson de T contra el superior del Wilson de la tanda 0;
  - la atención de RI, la ponderada total, la cola y su regla del 25 %, y las vigilancias y la (12), crudas.
Compara cada cifra con la salida de tasas_t4t2_tf.py (t4/tasas/tasas_t4_tramo2.json) y escribe <salida.json>.
Uso: python3 -I -B verif_tasas_independiente_t4t2_tf.py <raíz> <salida.json>
"""
import csv
import json
import math
import re
import sys
from fractions import Fraction as F
from pathlib import Path

R, OUT = Path(sys.argv[1]).resolve(), Path(sys.argv[2])
TF = R / "data/experiment/tanda_final"
U = json.loads((TF / "t3/muestras/umbrales_t4_tf.json").read_text(encoding="utf-8"))
X = json.loads((TF / "t4/tasas/tasas_t4_tramo2.json").read_text(encoding="utf-8"))
mesa = (R / "data/experiment/controles_tanda1/umbrales_t4_por_celdas_mesa.py").read_text(encoding="utf-8")
m = re.search(r'BASE = \{"items": \{"k": (\d+), "n": (\d+).*?"no_items": \{"k": (\d+), "n": (\d+)', mesa, re.S)
BASE = {"items": (int(m.group(1)), int(m.group(2))), "no_items": (int(m.group(3)), int(m.group(4)))}
CEL = ["RI:sin_raiz", "RI:resto", "NG:sin_raiz", "NG:resto"]
Z = 1.959964


def wilson(p: float, n: float) -> list:
    c = p + Z * Z / (2 * n)
    r = Z * math.sqrt(p * (1 - p) / n + Z * Z / (4 * n * n))
    return [round((c - r) / (1 + Z * Z / n), 4), round((c + r) / (1 + Z * Z / n), 4)]


def marcada(nombre: str) -> list:
    with open(TF / f"t4/lectura_autora/{nombre}_marcada.csv", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter=";"))


def conv(w: dict, n: dict, p0: F) -> dict:
    """Distribución exacta de T' = suma w_c K_c / n_c, K_c ~ Bin(n_c, p0), con Fraction."""
    d = {F(0): F(1)}
    for c in w:
        if not n[c]:
            continue
        nd = {}
        for t, pr in d.items():
            for k in range(n[c] + 1):
                tt = t + w[c] * F(k, n[c])
                nd[tt] = nd.get(tt, F(0)) + pr * math.comb(n[c], k) * p0 ** k * (1 - p0) ** (n[c] - k)
        d = nd
    return d


res, dif = {}, []


def comparar(clave: str, mio, suyo) -> None:
    igual = (abs(mio - suyo) < 1e-4) if isinstance(mio, float) else (mio == suyo)
    res[clave] = {"independiente": mio, "tasas_t4t2_tf": suyo, "igual": igual}
    if not igual:
        dif.append(clave)


Ts = {}
for s, nom in (("items", "aceptadas_items"), ("no_items", "aceptadas_no_items")):
    f = marcada(nom)
    N = U["aceptadas"][s]["N_por_celda"]
    w = {c: F(N[c], sum(N.values())) for c in CEL}
    k = {c: sum(1 for x in f if x["celda"] == c and x["veredicto_autora"] in ("con error", "dudosa")) for c in CEL}
    n = {c: sum(1 for x in f if x["celda"] == c) for c in CEL}
    T = sum(w[c] * F(k[c], n[c]) for c in CEL if n[c])
    ne = 1 / sum(w[c] ** 2 / n[c] for c in CEL if n[c])
    p0 = F(*BASE[s])
    d = conv(w, n, p0)
    pv = sum(pr for t, pr in d.items() if t >= T)
    sup0 = wilson(float(p0), BASE[s][1])[1]
    Ts[s] = (T, w, n)
    b = X["aceptadas"][s]["regla"]
    comparar(f"aceptadas:{s}:errores", sum(k.values()), b["errores"])
    comparar(f"aceptadas:{s}:k_por_celda", k, b["k_por_celda"])
    comparar(f"aceptadas:{s}:tasa_ponderada", round(float(T), 4), b["tasa_ponderada"])
    comparar(f"aceptadas:{s}:n_efectivo", round(float(ne), 3), b["n_efectivo_kish"])
    comparar(f"aceptadas:{s}:wilson", wilson(float(T), float(ne)), b["wilson"])
    comparar(f"aceptadas:{s}:p_valor", round(float(pv), 4), b["p_valor_atencion"])
    comparar(f"aceptadas:{s}:atencion", float(pv) <= 0.05, b["atencion"])
    comparar(f"aceptadas:{s}:freno", wilson(float(T), float(ne))[0] > sup0, b["freno_por_intervalos"])
    comparar(f"aceptadas:{s}:dudosas", sum(1 for x in f if x["veredicto_autora"] == "dudosa"),
             sum(X["aceptadas"][s]["por_celda"][c]["dudosa"] for c in CEL))
Ntot = sum(U["aceptadas"][s]["N"] for s in Ts)
Ws = {s: F(U["aceptadas"][s]["N"], Ntot) for s in Ts}
p = sum(Ws[s] * Ts[s][0] for s in Ts)
ne = 1 / sum(Ws[s] ** 2 * Ts[s][1][c] ** 2 / Ts[s][2][c] for s in Ts for c in CEL if Ts[s][2][c])
comparar("total:tasa_ponderada", round(float(p), 4), X["aceptadas"]["total"]["regla"]["tasa_ponderada"])
comparar("total:wilson", wilson(float(p), float(ne)), X["aceptadas"]["total"]["regla"]["wilson"])
# RI
RI = ["RI:sin_raiz", "RI:resto"]
NRI = sum(U["aceptadas"][s]["N_por_celda"][c] for s in Ts for c in RI)
num = {}
dd = {F(0): F(1)}
t_ri = F(0)
for s, nom in (("items", "aceptadas_items"), ("no_items", "aceptadas_no_items")):
    f = marcada(nom)
    for c in RI:
        v = F(U["aceptadas"][s]["N_por_celda"][c], NRI)
        nc = sum(1 for x in f if x["celda"] == c)
        kc = sum(1 for x in f if x["celda"] == c and x["veredicto_autora"] in ("con error", "dudosa"))
        t_ri += v * F(kc, nc)
        p0 = F(*BASE[s])
        nd = {}
        for t, pr in dd.items():
            for kk in range(nc + 1):
                nd[t + v * F(kk, nc)] = nd.get(t + v * F(kk, nc), F(0)) + pr * math.comb(nc, kk) * p0 ** kk * (1 - p0) ** (nc - kk)
        dd = nd
pv_ri = sum(pr for t, pr in dd.items() if t >= t_ri)
comparar("RI:tasa", round(float(t_ri), 4), X["atencion_RI"]["regla"]["tasa_ponderada_RI"])
comparar("RI:p_valor", round(float(pv_ri), 4), X["atencion_RI"]["regla"]["p_valor_atencion"])
comparar("RI:atencion", float(pv_ri) <= 0.05, X["atencion_RI"]["regla"]["atencion"])
# la cola
f = marcada("cola")
N = U["cola"]["N_por_celda"]
w = {c: F(N[c], sum(N.values())) for c in CEL}
k = {c: sum(1 for x in f if x["celda"] == c and x["veredicto_autora"] in ("con error", "dudosa")) for c in CEL}
n = {c: sum(1 for x in f if x["celda"] == c) for c in CEL}
T = sum(w[c] * F(k[c], n[c]) for c in CEL if n[c])
ne = 1 / sum(w[c] ** 2 / n[c] for c in CEL if n[c])
comparar("cola:errores", sum(k.values()), X["cola"]["regla"]["errores"])
comparar("cola:tasa_ponderada", round(float(T), 4), X["cola"]["regla"]["tasa_ponderada"])
comparar("cola:wilson", wilson(float(T), float(ne)), X["cola"]["regla"]["wilson"])
comparar("cola:regla_del_25", wilson(float(T), float(ne))[1] > 0.25, X["cola"]["regla"]["regla_del_25_se_dispara"])
# las vigilancias y la (12), crudas
for nom, clave, vig in (("vigilancia_1", "vigilancia:1", "sí"), ("vigilancia_2", "vigilancia:2", "vaciamiento"),
                        ("vigilancia_3", "vigilancia:3", "duplicación"), ("vigilancia_7", "vigilancia:7", "sin apoyo")):
    f = marcada(nom)
    kk = sum(1 for x in f if x["veredicto_autora"] == vig)
    nn = sum(1 for x in f if x["veredicto_autora"] != "no decidible") if clave == "vigilancia:1" else len(f)
    comparar(f"{clave}:cruda", [kk, nn, wilson(kk / nn, nn)], [X["vigilancias"][clave]["cruda"]["k"], X["vigilancias"][clave]["cruda"]["n"],
                                                              X["vigilancias"][clave]["cruda"]["wilson"]])
f = marcada("observacion_12")
kk = sum(1 for x in f if x["veredicto_autora"] == "correcta")
comparar("observacion:12:cruda", [kk, len(f), wilson(kk / len(f), len(f))],
         [X["observacion:12"]["cruda"]["correctas"], X["observacion:12"]["cruda"]["de"], X["observacion:12"]["cruda"]["wilson"]])
res["_resumen"] = {"cifras": len(res), "iguales": sum(1 for v in res.values() if v.get("igual")), "distintas": dif,
                   "base_tanda0_leida_del_script_de_la_mesa": BASE}
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str) + "\n", encoding="utf-8")
print(json.dumps(res["_resumen"], ensure_ascii=False))
for k2, v in res.items():
    if k2 != "_resumen":
        print(("igual  " if v["igual"] else "DISTINTO ") + k2, v["independiente"])
sys.exit(0 if not dif else 1)
