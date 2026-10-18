"""Mesa, §155 (18/10/2026), v3 de la §163: las cifras del pre-registro de la tanda final que ya se pueden calcular, todas desde sus
archivos (requisito 1 de `decisiones_149_mesa/tanda_final/requisitos_despacho_y_preregistro_tanda_final_mesa.md`). USD 0, sin API, sin
escribir en el repo (lee HEAD con `git show`). No usa nada de T4: las de T4, T5 y la revisión entre tandas son huecos.

- **El alcance:** `segmentacion_oficial_e0r2/s2/cifras/tanda_final_S2c.json` (98 TOs, sus unidades, por categoría y por modo) y los
  tramos de la §115 de la mesa (`decisiones_115_mesa/escalado/tramos_tanda_final_mesa.json`, citado en el registro de decisiones, §12),
  controlados contra la lista de S2c.
- **El alcance de cada documento:** el registro de alcance de HEAD (la tabla «## Tanda final», el 111) y la tabla de la release.
- **El costo y el tope:** la tarifa del laudo (0,021115), la razón de la tanda 1 (su gasto sobre su estimado con las líneas de alcance,
  `tanda1/t2/resumen_t2.json` y el pre-registro de la tanda 1, §3) y el tope de la enmienda 8 (1,45 × U × tarifa, `:100`).
- **Las bases del control entre tramos** (registro de decisiones, §12 y §13): desde la extracción de la tanda 1 (`resumen_t2.json`, por
  TO), con la celda de cada TO de `tanda1/t3/muestras/poblaciones_t4.json` (la de T3, commiteada en `eb0711a1`):
  - el costo por unidad de sus RI y de sus NG `sin_raiz`, ponderado por la composición del tramo 1;
  - la proporción a la cola en las 548 unidades RI o `sin_raiz` (el límite superior de Wilson si la cola tiene menos de 10);
  - como información, las salidas inválidas de E1 de la tanda 1 con la definición de la autora (decisión 3 del §9), y las unidades con
    reintento por forma de E1 (su último registro trae `reintento_forma`), sin umbral.
- **v3 (§163):**
  - la tabla «## Tanda final» del registro de alcance termina en el próximo «## », no al final del archivo;
  - `--sin <TO,TO,…>`: si la revisión entre tandas saca documentos, recalcula sin ellos, con la misma regla, U, el estimado, el tope,
    las listas de los tramos y las bases del control (estas no cambian: salen de la tanda 1). Mandan las de la versión derivada.
  - las listas de los tramos se leen del repo (`data/experiment/tanda_final/preregistro/tramos_tanda_final.json`, en HEAD) cuando ya
    entraron con el pre-registro, controladas byte a byte contra las del paquete; antes, del paquete;
  - la categoría de cada TO sale de `data/experiment/escalado_prep/inventario_tos.csv` (columna `categoria`), no de su nombre:
    `ribspc` es régimen informativo y `ri2_ci` es normativa general. Sin `--sin`, da las cifras de S2c, y el script lo controla.
Uso: python3 -I -B cifras_preregistro_tanda_final_mesa.py <paquete H> <salida.json> [--sin <TO,TO,…>]"""
import json
import math
import subprocess
import sys
from pathlib import Path

PAQ, OUT = Path(sys.argv[1]).resolve(), Path(sys.argv[2])
SIN = sorted(x for x in (sys.argv[sys.argv.index("--sin") + 1].split(",") if "--sin" in sys.argv else []) if x)
REPO = Path.home() / "INGENIERIA IA/TESIS/bcra-regulatory-kg"
git = lambda *a: subprocess.run(["git", "--no-optional-locks", "-C", str(REPO), *a], capture_output=True, check=True, text=True).stdout  # noqa: E731
show = lambda r: git("show", f"HEAD:{r}")  # noqa: E731
TARIFA, FACTOR_TOPE = 0.021115, 1.45
ESTIMADO_T1_CON_ALCANCE = 69.6592          # pre-registro de la tanda 1, §3 (3.290 × 0,021115 + 0,190841)


def wilson_sup(k, n, z=1.959963984540054):
    p = k / n
    c = (p + z * z / (2 * n) + z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))) / (1 + z * z / n)
    return c


s2c = json.loads(show("data/experiment/segmentacion_oficial_e0r2/s2/cifras/tanda_final_S2c.json"))["tanda_final"]
TR_REPO = "data/experiment/tanda_final/preregistro/tramos_tanda_final.json"   # entra con el pre-registro (v3)
tr_paq = (PAQ / "decisiones_115_mesa/escalado/tramos_tanda_final_mesa.json").read_bytes()
en_repo = subprocess.run(["git", "--no-optional-locks", "-C", str(REPO), "show", f"HEAD:{TR_REPO}"], capture_output=True)
if en_repo.returncode == 0:
    assert en_repo.stdout == tr_paq, "las listas de los tramos del repo no son las del paquete"
tr = json.loads(en_repo.stdout if en_repo.returncode == 0 else tr_paq)
t1, t2 = tr["tramo_1_tos"], tr["tramo_2_tos"]
assert sorted(list(t1) + list(t2)) == sorted(s2c["lista"]) and not set(t1) & set(t2), "los tramos no son la lista de S2c"
assert sum(t1.values()) + sum(t2.values()) == s2c["unidades"]
assert set(SIN) <= set(s2c["lista"]), f"--sin nombra documentos que no están en la tanda final: {sorted(set(SIN) - set(s2c['lista']))}"
t1 = {t: u for t, u in t1.items() if t not in SIN}
t2 = {t: u for t, u in t2.items() if t not in SIN}
LISTA = [t for t in s2c["lista"] if t not in SIN]
U = sum(t1.values()) + sum(t2.values())
import csv  # noqa: E402
import io  # noqa: E402
CAT = {r["id"]: r["categoria"] for r in csv.DictReader(io.StringIO(show("data/experiment/escalado_prep/inventario_tos.csv")))}
assert all(t in CAT for t in s2c["lista"]), "un TO de la tanda final no está en el inventario"
es_ri = lambda t: CAT[t] == "regimen_informativo"  # noqa: E731
ri1 = {t: u for t, u in t1.items() if es_ri(t)}
alcance = {"registro_sha256_HEAD": None}
reg = show("data/experiment/catalogo_unico/registro_alcance_por_tanda.md")
import hashlib  # noqa: E402
alcance["registro_sha256_HEAD"] = hashlib.sha256(reg.encode("utf-8")).hexdigest()
filas = [l for l in reg.split("## Tanda final", 1)[1].split("\n## ", 1)[0].splitlines() if l.startswith("| ") and not l.startswith("| TO ")]
dec = {}
for l in filas:
    d = [c.strip() for c in l.strip().strip("|").split("|")][2]
    dec[d] = dec.get(d, 0) + 1
rpt = json.loads(show("data/experiment/catalogo_unico/generados_r2/rol_por_to_r2.json"))
con_release = sorted(t for t in LISTA if f"{t}.pdf" in rpt)
alcance.update({"filas_de_la_tanda_final": len(filas), "por_decision": dict(sorted(dec.items())),
                "con_entrada_en_la_release": len(con_release),
                "sin_fila_ni_entrada": sorted(set(LISTA) - set(con_release) - {l.split("|")[1].strip() for l in filas})})
# el costo y el tope
res1 = json.loads(show("data/experiment/tanda1/t2/resumen_t2.json"))
razon = res1["total"]["gasto_por_to_sumado_usd"] / ESTIMADO_T1_CON_ALCANCE
costo = {"U": U, "tarifa": TARIFA, "estimado": round(U * TARIFA, 4), "razon_tanda1": round(razon, 4),
         "central_con_la_razon": round(U * TARIFA * razon, 2), "tope": round(FACTOR_TOPE * U * TARIFA, 2),
         "tramo_1_estimado": round(sum(t1.values()) * TARIFA, 4), "tramo_2_estimado": round(sum(t2.values()) * TARIFA, 4)}
# las bases del control entre tramos
pob = json.loads(show("data/experiment/tanda1/t3/muestras/poblaciones_t4.json"))
celda = pob["celda_por_to"]
RI = [t for t, c in celda.items() if c.startswith("RI:")]
NGSR = [t for t, c in celda.items() if c == "NG:sin_raiz"]
pt = res1["por_to"]
g = lambda tos, k: sum(pt[t][k] for t in tos)  # noqa: E731
c_ri, c_ng = g(RI, "gasto_usd") / g(RI, "unidades"), g(NGSR, "gasto_usd") / g(NGSR, "unidades")
n548 = g(RI, "unidades") + g(NGSR, "unidades")
cola548 = g(RI, "cola") + g(NGSR, "cola")
u_ri1, u_ng1 = sum(ri1.values()), sum(u for t, u in t1.items() if t not in ri1)
base_costo = (u_ri1 * c_ri + u_ng1 * c_ng) / (u_ri1 + u_ng1)
base_cola = cola548 / n548 if cola548 >= 10 else wilson_sup(cola548, n548)
inval = 0
tot_e1 = 0
rforma = 0
for t in pt:
    ult = {}
    for l in show(f"data/experiment/reextraccion_v2/corpus_tanda1/salida_r2b/{t}/extracciones_e1.jsonl").splitlines():
        if l.strip():
            r = json.loads(l)
            ult[r["chunk_id"]] = r
    part = json.loads(show(f"data/experiment/reextraccion_v2/corpus_tanda1/salida_r2b/{t}/particiones_por_corte.json")) \
        if f"data/experiment/reextraccion_v2/corpus_tanda1/salida_r2b/{t}/particiones_por_corte.json" in git("ls-files", f"data/experiment/reextraccion_v2/corpus_tanda1/salida_r2b/{t}") else {}
    for cid, r in ult.items():
        if cid in part:
            continue
        tot_e1 += 1
        inval += 1 if (r.get("error") or r.get("reparacion_forma")) else 0
        rforma += 1 if r.get("reintento_forma") else 0
bases = {"tos_RI": len(RI), "tos_NG_sin_raiz": NGSR, "unidades_RI": g(RI, "unidades"), "unidades_NG_sin_raiz": g(NGSR, "unidades"),
         "unidades_548": n548, "costo_por_unidad_RI": round(c_ri, 6), "costo_por_unidad_NG_sin_raiz": round(c_ng, 6),
         "tramo_1_RI_y_NG_sin_raiz": [u_ri1, u_ng1], "base_costo_por_unidad": round(base_costo, 6),
         "umbral_costo_por_unidad_1_3": round(1.3 * base_costo, 6), "costo_por_unidad_estimado": TARIFA,
         "cola_548": cola548, "base_proporcion_cola": round(base_cola, 6), "regla_de_la_base_de_la_cola":
         "la proporción" if cola548 >= 10 else "el límite superior de Wilson", "umbral_proporcion_cola_1_5": round(1.5 * base_cola, 6),
         "salidas_invalidas_E1_tanda1": [inval, tot_e1], "reintento_por_forma_E1_tanda1_informacion": [rforma, tot_e1],
         "umbral_salidas_invalidas": 0.01, "umbral_errores": 0}
UT = {**t1, **t2}
por_cat = ({k: {kk: (len(vv) if isinstance(vv, list) else vv) for kk, vv in v.items()} for k, v in s2c["por_categoria"].items()} if not SIN else
           {"normativa_general": {"tos": sum(1 for t in UT if not es_ri(t)), "unidades": sum(u for t, u in UT.items() if not es_ri(t))},
            "regimen_informativo": {"tos": sum(1 for t in UT if es_ri(t)), "unidades": sum(u for t, u in UT.items() if es_ri(t))}})
if not SIN:   # la categoría del inventario da las cifras de S2c
    assert {k: {"tos": sum(1 for t in UT if CAT[t] == k), "unidades": sum(u for t, u in UT.items() if CAT[t] == k)} for k in por_cat} == por_cat, \
        "la categoría del inventario no da S2c"
out = {"documentos_fuera": SIN, "alcance_s2c": {"tos": len(LISTA), "unidades": U,
                       "por_modo": s2c["por_modo"] if not SIN else "no se recalcula: S2c no da el modo por TO (se declara)",
                       "por_categoria": por_cat},
       "tramos": {"tramo_1": {"tos": len(t1), "unidades": sum(t1.values()), "RI": [len(ri1), u_ri1], "NG_sin_raiz": [len(t1) - len(ri1), u_ng1]},
                  "tramo_2": {"tos": len(t2), "unidades": sum(t2.values())}},
       "alcance": alcance, "costo": costo, "bases_control_entre_tramos": bases}
OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(out, ensure_ascii=False, indent=1))
