"""B6.1, tanda 1, T3, punto 7.3: los pesos reales y los umbrales de T4, con data/experiment/controles_tanda1/umbrales_t4_por_celdas_mesa.py
importado sin cambiarlo (pre-registro firmado, §5.4 a y b, v8b y v8c). Solo calcula; corre sobre una copia. No lee ninguna unidad.

  1. El control: el script de la mesa calcula todo al importarse y escribe su salida en sys.argv[1]. Se lo importa con sys.argv[1] en
     <trabajo>, y su salida, con los pesos proyectados de la E0, tiene que ser byte a byte data/experiment/controles_tanda1/
     umbrales_t4_por_celdas_mesa.json.
  2. Con los pesos reales (las unidades de cada celda en la población de cada muestra, de poblaciones_t4.json) y las n de cada celda
     (celdas_t4_t3f.asignar):
       - aceptadas, por estrato: la atención, el freno por intervalos y la atención sobre las 60, con `umbrales` del script de la mesa;
         y cuántos errores hacen falta en una sola celda para la atención, con `errores_minimos`;
       - la tasa ponderada total: Wilson con el n efectivo de Kish de las ocho celdas, n_ef = 1 / suma (W_s w_(s,c))^2 / n_(s,c), con
         los pesos reales de cada estrato (W_s = N_s / N) y de cada celda;
       - la atención propia de RI: test exacto unilateral al 5 % sobre la tasa ponderada de RI en los dos estratos,
         v = N_(s,c) / N_RI, con `pmf` y `cola_sup` del script de la mesa;
       - la cola: la regla del 25 % sobre el Wilson de la tasa ponderada con el n efectivo de Kish, con `wilson`.
     Las tres últimas son la misma cuenta del script de la mesa con los pesos como argumento (el script las calcula con los pesos
     proyectados en variables del módulo). Control: con los pesos proyectados dan las cifras de su salida.
  3. La probabilidad de que salte al menos una atención bajo H0 no se recalcula con los pesos reales: el pre-registro la da como
     información de la proyección, no como umbral.
Uso: python3 -I -B umbrales_t4_t3f.py <raíz> <poblaciones_t4.json> <trabajo> <salida.json>
"""
import contextlib
import importlib.util
import io
import itertools
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path

RAIZ, POB, W, OUT = Path(sys.argv[1]).resolve(), Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4])
sys.path.insert(0, str(Path(__file__).resolve().parent))
import celdas_t4_t3f as CT  # noqa: E402

MESA = RAIZ / "data/experiment/controles_tanda1/umbrales_t4_por_celdas_mesa.py"
MESA_JSON = RAIZ / "data/experiment/controles_tanda1/umbrales_t4_por_celdas_mesa.json"
W.mkdir(parents=True, exist_ok=True)
control_out = W / "umbrales_t4_por_celdas_mesa_al_importar.json"
assert not control_out.exists()
argv, sys.argv = sys.argv, ["umbrales_t4_por_celdas_mesa.py", str(control_out)]
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    spec = importlib.util.spec_from_file_location("umbrales_t4_por_celdas_mesa", MESA)
    RU = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(RU)
sys.argv = argv
(W / "consola_umbrales_mesa_al_importar.txt").write_text(buf.getvalue(), encoding="utf-8")
control = {"salida_al_importar": control_out.name, "byte_a_byte_igual_a": str(MESA_JSON.relative_to(RAIZ)),
           "igual": control_out.read_bytes() == MESA_JSON.read_bytes()}
assert RU.CELDAS == CT.CELDAS and RU.CUOTA == CT.CUOTA
ESTR = ["items", "no_items"]
RI = ["RI:sin_raiz", "RI:resto"]


def atencion_ri(v: dict, n: dict, p0: dict) -> dict:
    """La cuenta de RU.dist_ri / atencion_RI con los pesos v[(s, c)] y las n[(s, c)] como argumento."""
    celdas = [(s, c) for s in ESTR for c in RI]

    def dist(prob):
        d = {}
        for ks in itertools.product(*[range(n[sc] + 1) for sc in celdas]):
            tt = sum(v[sc] * F(k, n[sc]) for sc, k in zip(celdas, ks))
            pr = math.prod(RU.pmf(k, n[sc], prob[sc]) for sc, k in zip(celdas, ks))
            d[tt] = d.get(tt, 0.0) + pr
        return d
    sup = RU.cola_sup(dist({sc: p0[sc[0]] for sc in celdas}))
    t = min(tt for tt in sup if sup[tt] <= 0.05)
    pot = sum(pr for tt, pr in dist({sc: 2 * p0[sc[0]] for sc in celdas}).items() if tt >= t)
    return {"pesos": {f"{s}:{c}": round(float(v[(s, c)]), 4) for s, c in celdas},
            "n_efectivo_kish": round(1 / float(sum(v[sc] ** 2 / n[sc] for sc in celdas)), 3),
            "umbral_tasa_ponderada": round(float(t), 4), "p_valor_en_el_umbral": round(sup[t], 4),
            "tasa_de_RI_bajo_H0": round(sum(float(v[sc]) * p0[sc[0]] for sc in celdas), 4),
            "potencia_con_la_tasa_de_RI_duplicada": round(pot, 4)}


def neff_total(Ws: dict, w: dict, n: dict) -> float:
    return 1 / sum(float(Ws[s]) ** 2 * float(w[s][c]) ** 2 / n[s][c] for s in Ws for c in CT.CELDAS if n[s][c])


def regla_25(w: dict, n: dict) -> dict:
    con = [c for c in CT.CELDAS if n[c]]
    ne = 1 / float(sum(w[c] ** 2 / n[c] for c in con))
    return {"n_efectivo_kish": round(ne, 3), "superior_con_0_errores": round(RU.wilson(0.0, ne)[1], 4),
            "superior_con_1_error_en_cada_celda_sola": {c: round(RU.wilson(float(w[c] / n[c]), ne)[1], 4) for c in con}}


# control de las tres cuentas con los pesos proyectados
p0 = {s: RU.BASE[s]["k"] / RU.BASE[s]["n"] for s in ESTR}
ri_proy = atencion_ri(RU.v, {sc: RU.CUOTA[sc[1]] for sc in RU.v}, p0)
nt_proy = round(neff_total(RU.W_T0, {s: RU.E0w for s in ESTR}, {s: RU.CUOTA for s in ESTR}), 3)
cola_proy = regla_25(RU.E0w, RU.CUOTA)
control["cuentas_con_los_pesos_proyectados"] = {
    "atencion_RI": {k: ri_proy[k] == RU.res["atencion_RI"][k] for k in ("n_efectivo_kish", "umbral_tasa_ponderada", "p_valor_en_el_umbral",
                                                                          "tasa_de_RI_bajo_H0", "potencia_con_la_tasa_de_RI_duplicada")},
    "tasa_ponderada_total_n_efectivo": nt_proy == RU.res["tasa_ponderada_total"]["n_efectivo_proyectado"],
    "cola_regla_del_25": {k: cola_proy[k] == RU.res["cola_regla_del_25"][k] for k in ("superior_con_0_errores",
                                                                                     "superior_con_1_error_en_cada_celda_sola")}
    | {"n_efectivo_kish": cola_proy["n_efectivo_kish"] == RU.res["cola_regla_del_25"]["n_efectivo_proyectado"]}}
ok_ctrl = control["igual"] and all(all(x.values()) if isinstance(x, dict) else x for x in control["cuentas_con_los_pesos_proyectados"].values())

pob = json.loads(POB.read_text(encoding="utf-8"))["muestras"]
res = {"control": control, "control_ok": ok_ctrl, "aceptadas": {}, "cola": None, "otras": {}}
w_s, n_s = {}, {}
for s in ESTR:
    N = pob[f"aceptadas:{s}"]["N_por_celda"]
    tot = sum(N.values())
    a = CT.asignar(N)
    w = {c: F(N[c], tot) for c in CT.CELDAS}
    u = RU.umbrales(w, a["n"], RU.BASE[s])
    u["errores_minimos_en_una_sola_celda_para_la_atencion"] = RU.errores_minimos(
        w, a["n"], F(u["atencion"]["umbral_tasa_ponderada"]).limit_denominator(10**6))
    res["aceptadas"][s] = {"N_por_celda": N, "N": tot, "pesos": {c: round(float(w[c]), 4) for c in CT.CELDAS}, "n_por_celda": a["n"],
                           "notas_de_la_asignacion": a["notas"], "umbrales": u}
    w_s[s], n_s[s] = w, a["n"]
Ntot = sum(res["aceptadas"][s]["N"] for s in ESTR)
Ws = {s: F(res["aceptadas"][s]["N"], Ntot) for s in ESTR}
res["tasa_ponderada_total"] = {"pesos_de_los_estratos": {s: round(float(Ws[s]), 4) for s in ESTR},
                               "n_efectivo": round(neff_total(Ws, w_s, n_s), 3),
                               "tanda0_con_el_mismo_metodo": RU.res["tasa_ponderada_total"]["tanda0_con_el_mismo_metodo"]}
N_RI = sum(res["aceptadas"][s]["N_por_celda"][c] for s in ESTR for c in RI)
v = {(s, c): F(res["aceptadas"][s]["N_por_celda"][c], N_RI) for s in ESTR for c in RI}
res["atencion_RI"] = {"N_RI": N_RI, **atencion_ri(v, {(s, c): n_s[s][c] for s in ESTR for c in RI}, p0),
                      "ampliacion": RU.res["atencion_RI"]["ampliacion"]}
Nc = pob["cola"]["N_por_celda"]
ac = CT.asignar(Nc)
wc = {c: F(Nc[c], sum(Nc.values())) for c in CT.CELDAS}
res["cola"] = {"N_por_celda": Nc, "pesos": {c: round(float(wc[c]), 4) for c in CT.CELDAS}, "n_por_celda": ac["n"],
               "notas_de_la_asignacion": ac["notas"], "regla_del_25": regla_25(wc, ac["n"]),
               "base_tanda0": "12 de 30, Wilson [0,246; 0,577] (reext_t0/t4/salida/tasas_t4.json)"}
for m in ("vigilancia:2", "vigilancia:7", "observacion:12"):
    N = pob[m]["N_por_celda"]
    a = CT.asignar(N)
    res["otras"][m] = {"N_por_celda": N, "N": sum(N.values()),
                       "pesos": {c: (round(N[c] / sum(N.values()), 4) if sum(N.values()) else None) for c in CT.CELDAS},
                       "n_por_celda": a["n"], "entera_sin_celdas": a["entera_sin_celdas"], "notas_de_la_asignacion": a["notas"]}
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("control byte a byte:", control["igual"], "| cuentas con los pesos proyectados:", control["cuentas_con_los_pesos_proyectados"])
for s in ESTR:
    a = res["aceptadas"][s]
    u = a["umbrales"]
    print(f"{s}: N {a['N_por_celda']} n {a['n_por_celda']} n_ef {u['n_efectivo_kish']} | atención desde {u['atencion']['umbral_tasa_ponderada']} "
          f"(p {u['atencion']['p_valor_en_el_umbral']}) | freno {u['freno_por_intervalos']['umbral_tasa_ponderada']} | sobre 60 "
          f"{u['freno_por_atencion_sobre_60']['umbral_tasa_ponderada']}")
    print("   errores en una sola celda:", u["errores_minimos_en_una_sola_celda_para_la_atencion"])
print("total:", res["tasa_ponderada_total"])
print("RI:", {k: res["atencion_RI"][k] for k in ("N_RI", "n_efectivo_kish", "umbral_tasa_ponderada", "p_valor_en_el_umbral", "tasa_de_RI_bajo_H0")})
print("cola:", res["cola"]["n_por_celda"], res["cola"]["notas_de_la_asignacion"], res["cola"]["regla_del_25"])
for m, x in res["otras"].items():
    print(m, x["n_por_celda"], x["notas_de_la_asignacion"])
sys.exit(0 if ok_ctrl else 1)
