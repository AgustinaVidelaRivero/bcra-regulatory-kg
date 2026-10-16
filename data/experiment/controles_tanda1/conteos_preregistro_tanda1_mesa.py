"""Conteos del borrador del pre-registro de la tanda 1 (mesa, 09/10/2026).

Solo lectura del repo: abre archivos en modo lectura, no escribe nada, no llama a ninguna API.
Uso (desde cualquier directorio):
    python3 -I -B conteos_preregistro_tanda1_mesa.py "<raiz del repo>"
Imprime cada cifra con la ruta de la que sale.
"""
import csv
import glob
import json
import os
import sys
from collections import Counter
from math import comb, sqrt

RAIZ = sys.argv[1] if len(sys.argv) > 1 else "."
Z = 1.959964


def ruta(*p):
    return os.path.join(RAIZ, *p)


def wilson(k, n, z=Z):
    p = k / n
    den = 1 + z * z / n
    centro = (p + z * z / (2 * n)) / den
    medio = z * sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return centro - medio, centro + medio


def cola_superior(k, n, p):
    return sum(comb(n, i) * p**i * (1 - p) ** (n - i) for i in range(k, n + 1))


print("== 1. Tarifa de referencia (protocolo_entre_tandas.md:501-506)")
e1, e3_obs, agregado = 0.010135, 0.010226, 0.000754
e3 = round(e3_obs + agregado, 6)
t = round(e1 + e3, 6)
print(f"E3 = {e3_obs} + {agregado} = {e3}; tarifa = {e1} + {e3} = {t}")
print(f"3292 x {t} = {3292 * t:.4f}")

print("\n== 2. Ejemplo del §7 (protocolo_entre_tandas.md:282-284), sobre la particion legada")
ejemplo = ["ayccef", "expaef", "opefci", "adrei", "ri_ccna", "ri_cc", "ri_rml", "ri_gerc",
           "snp_cheq", "ceninf", "cirmo3", "snp_tr", "lingeef", "depaho", "cajasc",
           "manori", "efemin", "nmcief", "ri_dcpc", "ri_oc"]
assert len(ejemplo) == 20 and len(set(ejemplo)) == 20
conteos = json.load(open(ruta("data/experiment/segmentacion_84/b584_particion/conteos_b584.json"), encoding="utf-8"))
ver = json.load(open(ruta("data/experiment/escalado_prep/veredictos_generalizacion.json"), encoding="utf-8"))["por_to"]
cat = {r["id"]: r["categoria"] for r in csv.DictReader(open(ruta("data/experiment/escalado_prep/inventario_tos.csv"), encoding="utf-8"))}
inv_u = {r["id"]: r for r in csv.DictReader(open(ruta("data/experiment/escalado_prep/inventario_unidades.csv"), encoding="utf-8"))}


def resumen(lista, rotulo):
    u = sum(conteos[x]["unidades_extraccion"] for x in lista)
    v = Counter(ver[x]["veredicto"] for x in lista)
    vi = Counter(inv_u[x]["veredicto"] for x in lista)
    c = Counter(cat[x] for x in lista)
    modos = Counter(conteos[x]["modo_lectura"] for x in lista)
    print(f"{rotulo}: TOs {len(lista)}; unidades (conteos_b584.json, unidades_extraccion) {u}; "
          f"x {t} = {u * t:.4f} USD")
    print(f"  veredicto (veredictos_generalizacion.json) {dict(v)}; veredicto (inventario_unidades.csv) {dict(vi)}")
    print(f"  categoria (inventario_tos.csv) {dict(c)}; modo_lectura {dict(modos)}")
    return u


u_cc = resumen(ejemplo, "ejemplo con ri_cc")
con_pgn = [("ri_pgn" if x == "ri_cc" else x) for x in ejemplo]
u_pgn = resumen(con_pgn, "ejemplo con ri_pgn en lugar de ri_cc")
print(f"  ri_cc {conteos['ri_cc']['unidades_extraccion']} unidades; ri_pgn {conteos['ri_pgn']['unidades_extraccion']}; "
      f"diferencia {u_pgn - u_cc}")

print("\n== 3. Cola humana de la tanda 0 en r2b (corpus_tanda0/salida_r2b/*/finales.jsonl, campo estado)")
est = Counter()
n = 0
for f in sorted(glob.glob(ruta("data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b/*/finales.jsonl"))):
    for linea in open(f, encoding="utf-8"):
        est[json.loads(linea)["estado"]] += 1
        n += 1
cola = {k: v for k, v in est.items() if k.startswith("cola_humana")}
print(f"registros {n}; cola {cola}; total cola {sum(cola.values())}")
print(f"74/2439 = {74 / 2439:.4f}; 74/{n} = {74 / n:.4f}")

print("\n== 4. Intervalos de Wilson al 95 % (z = 1,959964)")
for k, nn, rot in [(12, 30, "cola T4"), (25, 30, "obs (12) tanda 0"), (6, 30, "L2 items"), (4, 30, "L2 no items")]:
    a, b = wilson(k, nn)
    print(f"{rot}: {k}/{nn} -> [{a:.4f}; {b:.4f}]")
print("Regla de la cola con muestra de 30, limite superior por k:",
      [(k, round(100 * wilson(k, 30)[1], 1)) for k in range(4)])

print("\n== 5. Vigilancia de las aceptadas (dos niveles por estrato)")
for rot, k0 in [("items", 6), ("no items", 4)]:
    p0 = k0 / 30
    ls0 = wilson(k0, 30)[1]
    k_at = next(k for k in range(31) if cola_superior(k, 30, p0) <= 0.05)
    k_fr = next(k for k in range(31) if wilson(k, 30)[0] > ls0)
    print(f"{rot}: p0 {p0:.4f}; atencion (binomial exacta unilateral al 5 %) desde {k_at}/30 "
          f"(P = {cola_superior(k_at, 30, p0):.4f}); freno por intervalos disjuntos desde {k_fr}/30 "
          f"(LI {wilson(k_fr, 30)[0]:.4f} > LS tanda 0 {ls0:.4f})")
