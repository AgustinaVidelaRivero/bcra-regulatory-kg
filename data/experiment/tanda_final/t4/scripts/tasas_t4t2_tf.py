"""B6.1, tanda final, T4, segundo tramo, puntos 4 y 5 del «seguí»: las tasas, la atención y el freno, sobre la lectura sellada de la
autora, con el pre-registro firmado (docs/preregistro_tanda_final.md, firma en 4de7f2a7, §6), su versión derivada para la lectura
(tanda_final/preregistro/preregistro_tanda_final_derivada_T4.md) y los umbrales que T3 calculó con los pesos reales
(t3/muestras/umbrales_t4_tf.json). Es tanda1/t4/scripts/tasas_t4t2.py con las rutas, los nombres y los umbrales de la tanda final, y con
las líneas de base de la versión derivada. Solo lee y calcula; escribe solo en <trabajo>, <salida.json> y <distribuciones.json>. No lee el
grafo, ni estados de E3, ni reintentos.

  1. Los controles de la entrada, antes de contar:
       - cada marcada tiene el sha256 de su línea del sello (t4/lectura_autora/sello_lectura_T4.txt);
       - umbrales_t4_tf.json tiene el sha256 del «seguí»; la versión derivada y su .huecos.json, los de T3;
       - el script de la mesa (data/experiment/controles_tanda1/umbrales_t4_por_celdas_mesa.py) se importa sin cambiarlo, como en T3
         (t3/scripts/umbrales_t4_tf.py), y su salida al importarse es byte a byte su JSON. De él salen wilson, pmf, cola_sup,
         distribucion, BASE (la tanda 0) y Z;
       - cada marcada tiene, por celda, los mismos ids que su muestra (t3/muestras/), y cada veredicto es válido;
       - las N por celda de umbrales_t4_tf.json son las de t3/muestras/poblaciones_t4_t3f_tf.json (aceptadas, cola, (2) y (7)) y las de
         t3/muestras/poblaciones_t4t1_tf.json ((1), (3) y (12)), y las n por celda son las de la muestra;
       - cada línea de base de la tanda 1 (los valores T4.* del .huecos.json de la versión derivada) está tal cual en la versión derivada.
  2. La regla de las dudosas (pre-registro, §6; registro, §35): en la cola y en las dos de las aceptadas, «dudosa» cuenta como error para
     la tasa, la atención y el freno. La misma cuenta con las dudosas fuera, sobre las decididas, va al lado como sensibilidad y no decide
     nada; si diera otra decisión de atención o de freno, se declara, y rige la primera.
  3. Las aceptadas, por estrato: T = suma w_c k_c / n_c, con w_c = N_c / N (umbrales_t4_tf.json); Wilson al 95 % con
     n_ef = 1 / suma w_c^2 / n_c; la atención, P(T' >= T) bajo H0 (cada celda en la tasa de la tanda 0 del estrato, la base del script
     sellado) con la distribución de T' enumerada entera (`distribucion` de la mesa), y salta si es <= 0,05; el freno por intervalos, si
     el límite inferior del Wilson de T pasa el superior del Wilson de la tanda 0 (la misma comparación que `umbrales` de la mesa). El
     freno por la atención sobre las 60 solo se mira en un tercer tramo, si hay ampliación.
     La tasa ponderada total, p = suma W_s T_s con W_s = N_s / N, con el Wilson de n_ef = 1 / suma (W_s w_c)^2 / n_c de las ocho celdas.
     La atención propia de RI: t = suma v k / n en las cuatro celdas RI de los dos estratos, v = N_(s,c) / N_RI, con el test exacto de
     `atencion_ri` de T3 (cada celda bajo H0 en la tasa de la tanda 0 de su estrato). NG sin_raiz, por celda y sin umbral.
  4. La cola: la ponderada por celda con los pesos de la cola, su Wilson con n_ef y la regla del 25 % (se dispara si el límite superior
     pasa 0,25), como cifra y vigilancia, no como freno.
  5. Las vigilancias (1), (2), (3) y (7) y la (12): la cuenta de cada respuesta y la tasa de la que se vigila, con su Wilson. Sus muestras
     salieron por celdas y el pre-registro no fija su ponderación: van la cruda (k sobre las leídas, Wilson con esa n) y la ponderada por
     celda (Wilson con n_ef), las dos. En la (1), las no decidibles fuera de la tasa, con su cuenta (registro de decisiones, §29). En la
     (12), correctas sobre 30, con las no decidibles aparte y en el denominador (enmienda de la observación 12, :107-111); las
     incorrectas, por capa_pipeline. Los pesos de la (1), la (3) y la (12) son los de t3/muestras/poblaciones_t4t1_tf.json (la (12), con
     las aristas de extracción de la (10), sin remite_a). La (7) se leyó entera, sin celdas: solo la cruda.
  6. Cada cifra con su línea de base: la de la tanda 1, de la versión derivada, con la de la tanda 0 al lado (la base del script de la
     mesa, la de la cola de umbrales_t4_tf.json y las de la tanda 0 que dan los scripts del segundo tramo de la tanda 1).
Uso: python3 -I -B tasas_t4t2_tf.py <raíz> <trabajo> <salida.json> <distribuciones.json>
"""
import contextlib
import csv
import hashlib
import importlib.util
import io
import itertools
import json
import math
import re
import sys
from datetime import datetime
from fractions import Fraction as F
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ, W, OUT, DIST = Path(sys.argv[1]).resolve(), Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4])
TF = RAIZ / "data/experiment/tanda_final"
LA = TF / "t4/lectura_autora"
UMBRALES = TF / "t3/muestras/umbrales_t4_tf.json"
UMBRALES_SHA = "d7f7860fbf09f92443992aeb9915e22191582cfe2edaf5fd0a089baadd3ac555"
DERIVADA = TF / "preregistro/preregistro_tanda_final_derivada_T4.md"
DERIVADA_SHA = "26c29d9424ffaf634a02735a972ad29e7df8b06463b8ad430654d50d4d442fc2"
HUECOS = TF / "preregistro/preregistro_tanda_final_derivada_T4.huecos.json"
HUECOS_SHA = "4a17612bcf069beee9b00f513c6b69b7f4b0fa81b7ba590052f79d318b3862e4"
MESA = RAIZ / "data/experiment/controles_tanda1/umbrales_t4_por_celdas_mesa.py"
MESA_JSON = RAIZ / "data/experiment/controles_tanda1/umbrales_t4_por_celdas_mesa.json"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()  # noqa: E731
CELDAS = ["RI:sin_raiz", "RI:resto", "NG:sin_raiz", "NG:resto"]
ESTR = ["items", "no_items"]
RI = ["RI:sin_raiz", "RI:resto"]
# muestra -> (planilla, archivo de la muestra, respuestas válidas)
MUESTRAS = {
    "cola": ("cola", TF / "t3/muestras/cola.json", ["con error", "sin error", "dudosa"]),
    "aceptadas:items": ("aceptadas_items", TF / "t3/muestras/aceptadas_items.json", ["con error", "sin error", "dudosa"]),
    "aceptadas:no_items": ("aceptadas_no_items", TF / "t3/muestras/aceptadas_no_items.json", ["con error", "sin error", "dudosa"]),
    "vigilancia:2": ("vigilancia_2", TF / "t3/muestras/vigilancia_2.json", ["vaciamiento", "no vaciamiento", "no decidible"]),
    "vigilancia:7": ("vigilancia_7", TF / "t3/muestras/vigilancia_7.json", ["con apoyo", "sin apoyo", "no decidible"]),
    "vigilancia:1": ("vigilancia_1", TF / "t3/muestras/vigilancia_1.json", ["sí", "no", "no decidible"]),
    "vigilancia:3": ("vigilancia_3", TF / "t3/muestras/vigilancia_3.json", ["duplicación", "distintos"]),
    "observacion:12": ("observacion_12", TF / "t3/muestras/observacion_12.json", None),
}
CAPAS = ["E0", "E1-prompt", "E1-validador", "catálogo", "E2", "E3", "ensamblado"]
RE_INC = re.compile(r"^incorrecta \((.+)\)$")

# 1. Los controles de la entrada
controles = {}
sello = {}
for linea in (LA / "sello_lectura_T4.txt").read_text(encoding="utf-8").splitlines():
    if linea.strip():
        h, nombre, hora = re.split(r"\s{2,}", linea.strip())
        sello[nombre] = {"sha256": h, "hora": hora}
controles["sello: 8 líneas"] = len(sello) == 8
controles["cada marcada tiene el sha256 de su línea del sello"] = all(
    sha(LA / f"{p}_marcada.csv") == sello[f"{p}_marcada.csv"]["sha256"] for p, _, _ in MUESTRAS.values())
controles["umbrales_t4_tf.json tiene el sha256 del «seguí»"] = sha(UMBRALES) == UMBRALES_SHA
controles["la versión derivada tiene el sha256 de T3"] = sha(DERIVADA) == DERIVADA_SHA
controles["el .huecos.json de la versión derivada tiene el sha256 de T3"] = sha(HUECOS) == HUECOS_SHA
W.mkdir(parents=True, exist_ok=True)
control_out = W / "umbrales_t4_por_celdas_mesa_al_importar_t4t2_tf.json"
assert not control_out.exists(), control_out
argv, sys.argv = sys.argv, ["umbrales_t4_por_celdas_mesa.py", str(control_out)]
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    spec = importlib.util.spec_from_file_location("umbrales_t4_por_celdas_mesa", MESA)
    RU = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(RU)
sys.argv = argv
controles["el script de la mesa, importado, da su JSON byte a byte"] = control_out.read_bytes() == MESA_JSON.read_bytes()
assert RU.CELDAS == CELDAS
U = json.loads(UMBRALES.read_text(encoding="utf-8"))
POB3 = json.loads((TF / "t3/muestras/poblaciones_t4_t3f_tf.json").read_text(encoding="utf-8"))["muestras"]
POB4 = json.loads((TF / "t3/muestras/poblaciones_t4t1_tf.json").read_text(encoding="utf-8"))["muestras"]
controles["las N por celda de umbrales_t4_tf.json son las de t3/muestras/poblaciones_t4_t3f_tf.json"] = all(
    [U["aceptadas"][s]["N_por_celda"] == POB3[f"aceptadas:{s}"]["N_por_celda"] for s in ESTR]
    + [U["cola"]["N_por_celda"] == POB3["cola"]["N_por_celda"]]
    + [U["otras"][m]["N_por_celda"] == POB3[m]["N_por_celda"] for m in ("vigilancia:2", "vigilancia:7")])
controles["las N por celda de umbrales_t4_tf.json son las de t3/muestras/poblaciones_t4t1_tf.json"] = all(
    U["otras"][m]["N_por_celda"] == POB4[m]["N_por_celda"] for m in ("vigilancia:1", "vigilancia:3", "observacion:12"))
HU = json.loads(HUECOS.read_text(encoding="utf-8"))["valores"]
DER = DERIVADA.read_text(encoding="utf-8")
controles["las líneas de base de la tanda 1 (T4.*) están tal cual en la versión derivada"] = all(
    HU[k]["valor"] in DER for k in HU if k.startswith("T4."))


def leer(muestra: str) -> dict:
    """Las filas de la marcada, por celda, contra los ids de la muestra; y los veredictos, contra los válidos."""
    planilla, arch, validas = MUESTRAS[muestra]
    with open(LA / f"{planilla}_marcada.csv", encoding="utf-8", newline="") as fh:
        filas = list(csv.DictReader(fh, delimiter=";"))
    m = json.loads(arch.read_text(encoding="utf-8"))
    por_celda = {c: [f for f in filas if f["celda"] == c] for c in CELDAS}
    # una arista va en la muestra como lista [origen, relación, destino] y en la planilla con « | » (t4/scripts/planillas_t4t1.py:93-94)
    id_txt = lambda x: x if isinstance(x, str) else " | ".join(x)  # noqa: E731
    ids_ok = all(sorted(f["id"] for f in por_celda[c]) == sorted(id_txt(e) for e in m["celdas"][c]["elementos"]) for c in CELDAS) \
        and len(filas) == m["n"] == sum(len(v) for v in por_celda.values())
    n_ok = all(len(por_celda[c]) == m["n_por_celda"][c] for c in CELDAS)
    ver = [f["veredicto_autora"] for f in filas]
    if validas is None:
        val_ok = all(v in ("correcta", "no decidible") or (RE_INC.match(v) and RE_INC.match(v).group(1) in CAPAS) for v in ver)
    else:
        val_ok = all(v in validas for v in ver)
    controles[f"{muestra}: los ids por celda son los de la muestra"] = ids_ok
    controles[f"{muestra}: las n por celda son las de la muestra"] = n_ok
    controles[f"{muestra}: los veredictos son válidos"] = val_ok
    return {"filas": filas, "por_celda": por_celda, "muestra": m}


L = {m: leer(m) for m in MUESTRAS}
for s in ESTR:
    controles[f"aceptadas:{s}: las n por celda son las de umbrales_t4_tf.json"] = \
        L[f"aceptadas:{s}"]["muestra"]["n_por_celda"] == U["aceptadas"][s]["n_por_celda"]
controles["cola: las n por celda son las de umbrales_t4_tf.json"] = L["cola"]["muestra"]["n_por_celda"] == U["cola"]["n_por_celda"]
for m in ("vigilancia:1", "vigilancia:3", "observacion:12"):
    controles[f"{m}: las N por celda de la muestra son las de poblaciones_t4t1_tf.json"] = \
        L[m]["muestra"]["N_por_celda"] == POB4[m]["N_por_celda"]
for m in ("vigilancia:2", "vigilancia:7"):
    controles[f"{m}: las N por celda de la muestra son las de umbrales_t4_tf.json"] = \
        L[m]["muestra"]["N_por_celda"] == U["otras"][m]["N_por_celda"]
assert all(controles.values()), {k: v for k, v in controles.items() if not v}

r4 = lambda x: round(float(x), 4)  # noqa: E731
wil = lambda p, n: [r4(x) for x in RU.wilson(float(p), float(n))]  # noqa: E731


def cuenta(muestra: str, respuestas: list) -> dict:
    out = {c: {r: sum(1 for f in L[muestra]["por_celda"][c] if f["veredicto_autora"] == r) for r in respuestas} for c in CELDAS}
    for c in CELDAS:
        out[c]["n"] = len(L[muestra]["por_celda"][c])
    return out


def ponderada(w: dict, k: dict, n: dict) -> dict:
    """T = suma w_c k_c / n_c (las celdas con n_c > 0), n_ef de Kish y su Wilson."""
    con = [c for c in CELDAS if n[c]]
    assert all(w[c] == 0 for c in CELDAS if not n[c]), "una celda con peso y sin leídas"
    t = sum(w[c] * F(k[c], n[c]) for c in con)
    ne = 1 / sum(w[c] ** 2 / n[c] for c in con)
    return {"T": t, "n_ef": ne}


def p_valor(w: dict, n: dict, p0: float, t: F) -> tuple:
    """P(T' >= t) bajo H0, con la distribución de T' enumerada entera (`distribucion` de la mesa)."""
    con = [c for c in CELDAS if n[c]]
    if len(con) == len(CELDAS):
        d = RU.distribucion(w, n, p0)
    else:  # una celda sin leídas (n_c = 0, por la sensibilidad): se enumeran las demás, con la misma cuenta
        d = {}
        for ks in itertools.product(*[range(n[c] + 1) for c in con]):
            tt = sum(w[c] * F(kk, n[c]) for c, kk in zip(con, ks))
            d[tt] = d.get(tt, 0.0) + math.prod(RU.pmf(kk, n[c], p0) for c, kk in zip(con, ks))
    return sum(pr for tt, pr in d.items() if tt >= t), d


def tabla_dist(d: dict) -> list:
    sup = RU.cola_sup(d)
    return [[round(float(t), 6), d[t], sup[t]] for t in sorted(d)]


res = {"hora": None, "controles": controles, "regla_de_las_dudosas": (
    "en la cola y en las dos de las aceptadas, una unidad «dudosa» cuenta como error para la tasa, la atención y el freno; la misma cuenta "
    "con las dudosas fuera, sobre las decididas, va al lado como sensibilidad y no decide nada (pre-registro, §6; registro, §35)"),
    "z": RU.Z, "aceptadas": {}, "atencion_RI": {}, "NG_sin_raiz": {}, "cola": {}, "vigilancias": {}, "observacion:12": {}}
dist_out = {"que_es": "la distribución bajo H0 de la tasa ponderada, enumerada entera: [t, P(T = t), P(T >= t)]"}

# 3. Las aceptadas
R_ERR = ["con error", "sin error", "dudosa"]
Tvals = {}
for s in ESTR:
    m = f"aceptadas:{s}"
    cu = cuenta(m, R_ERR)
    Ns = U["aceptadas"][s]["N_por_celda"]
    w = {c: F(Ns[c], sum(Ns.values())) for c in CELDAS}
    p0 = RU.BASE[s]["k"] / RU.BASE[s]["n"]
    sup0 = RU.BASE[s]["wilson"][1]
    bloque = {"N_por_celda": Ns, "pesos": {c: r4(w[c]) for c in CELDAS}, "por_celda": cu,
              "p0_tanda0": p0, "wilson_tanda0": [r4(x) for x in RU.BASE[s]["wilson"]],
              "umbrales_T3": {"atencion_desde": U["aceptadas"][s]["umbrales"]["atencion"]["umbral_tasa_ponderada"],
                              "freno_por_intervalos_desde": U["aceptadas"][s]["umbrales"]["freno_por_intervalos"]["umbral_tasa_ponderada"]}}
    for nombre, kfun, nfun in (("regla", lambda c: cu[c]["con error"] + cu[c]["dudosa"], lambda c: cu[c]["n"]),
                               ("sensibilidad_sin_dudosas", lambda c: cu[c]["con error"], lambda c: cu[c]["n"] - cu[c]["dudosa"])):
        k = {c: kfun(c) for c in CELDAS}
        n = {c: nfun(c) for c in CELDAS}
        pq = ponderada(w, k, n)
        pv, d = p_valor(w, n, p0, pq["T"])
        wl = wil(pq["T"], pq["n_ef"])
        bloque[nombre] = {"k_por_celda": k, "n_por_celda": n, "errores": sum(k.values()), "leidas": sum(n.values()),
                          "tasa_ponderada": r4(pq["T"]), "tasa_ponderada_fraccion": str(pq["T"]), "n_efectivo_kish": round(float(pq["n_ef"]), 3),
                          "wilson": wl, "p_valor_atencion": round(pv, 4), "atencion": pv <= 0.05,
                          "freno_por_intervalos": RU.wilson(float(pq["T"]), float(pq["n_ef"]))[0] > sup0,
                          "puntos_de_la_distribucion": len(d), "suma_de_la_distribucion": round(sum(d.values()), 9)}
        dist_out[f"{m}:{nombre}"] = tabla_dist(d)
        Tvals[(s, nombre)] = (pq["T"], w, n)
    bloque["la_sensibilidad_da_otra_decision"] = {
        x: bloque["regla"][x] != bloque["sensibilidad_sin_dudosas"][x] for x in ("atencion", "freno_por_intervalos")}
    res["aceptadas"][s] = bloque
# la ponderada total, con las ocho celdas
Ntot = sum(U["aceptadas"][s]["N"] for s in ESTR)
Ws = {s: F(U["aceptadas"][s]["N"], Ntot) for s in ESTR}
tot = {"pesos_de_los_estratos": {s: r4(Ws[s]) for s in ESTR},
       "tanda0_con_el_mismo_metodo": U["tasa_ponderada_total"]["tanda0_con_el_mismo_metodo"]}
for nombre in ("regla", "sensibilidad_sin_dudosas"):
    p = sum(Ws[s] * Tvals[(s, nombre)][0] for s in ESTR)
    ne = 1 / sum(Ws[s] ** 2 * Tvals[(s, nombre)][1][c] ** 2 / Tvals[(s, nombre)][2][c] for s in ESTR for c in CELDAS if Tvals[(s, nombre)][2][c])
    tot[nombre] = {"tasa_ponderada": r4(p), "n_efectivo_kish": round(float(ne), 3), "wilson": wil(p, ne)}
res["aceptadas"]["total"] = tot
# la atención propia de RI
N_RI = sum(U["aceptadas"][s]["N_por_celda"][c] for s in ESTR for c in RI)
v = {(s, c): F(U["aceptadas"][s]["N_por_celda"][c], N_RI) for s in ESTR for c in RI}
celdas_ri = [(s, c) for s in ESTR for c in RI]
p0s = {s: RU.BASE[s]["k"] / RU.BASE[s]["n"] for s in ESTR}
ri = {"N_RI": N_RI, "pesos": {f"{s}:{c}": r4(v[(s, c)]) for s, c in celdas_ri},
      "umbral_T3": U["atencion_RI"]["umbral_tasa_ponderada"], "tasa_de_RI_bajo_H0": U["atencion_RI"]["tasa_de_RI_bajo_H0"]}
for nombre in ("regla", "sensibilidad_sin_dudosas"):
    k, n = {}, {}
    for s, c in celdas_ri:
        b = res["aceptadas"][s][nombre]
        k[(s, c)], n[(s, c)] = b["k_por_celda"][c], b["n_por_celda"][c]
    con = [sc for sc in celdas_ri if n[sc]]
    t = sum(v[sc] * F(k[sc], n[sc]) for sc in con)
    d = {}
    for ks in itertools.product(*[range(n[sc] + 1) for sc in con]):
        tt = sum(v[sc] * F(kk, n[sc]) for sc, kk in zip(con, ks))
        d[tt] = d.get(tt, 0.0) + math.prod(RU.pmf(kk, n[sc], p0s[sc[0]]) for sc, kk in zip(con, ks))
    pv = sum(pr for tt, pr in d.items() if tt >= t)
    ne = 1 / sum(v[sc] ** 2 / n[sc] for sc in con)
    ri[nombre] = {"k_por_celda": {f"{s}:{c}": k[(s, c)] for s, c in celdas_ri}, "n_por_celda": {f"{s}:{c}": n[(s, c)] for s, c in celdas_ri},
                  "errores": sum(k.values()), "leidas": sum(n.values()), "tasa_ponderada_RI": r4(t), "tasa_ponderada_RI_fraccion": str(t),
                  "n_efectivo_kish": round(float(ne), 3), "wilson": wil(t, ne), "p_valor_atencion": round(pv, 4), "atencion": pv <= 0.05,
                  "puntos_de_la_distribucion": len(d), "suma_de_la_distribucion": round(sum(d.values()), 9)}
    dist_out[f"atencion_RI:{nombre}"] = tabla_dist(d)
ri["la_sensibilidad_da_otra_decision"] = {"atencion": ri["regla"]["atencion"] != ri["sensibilidad_sin_dudosas"]["atencion"]}
res["atencion_RI"] = ri
# NG sin_raiz, por celda, sin umbral
for s in ESTR:
    cu = res["aceptadas"][s]["por_celda"]["NG:sin_raiz"]
    res["NG_sin_raiz"][s] = {"N": U["aceptadas"][s]["N_por_celda"]["NG:sin_raiz"], **cu,
                             "errores_con_la_regla": cu["con error"] + cu["dudosa"], "tasa_con_la_regla": r4(F(cu["con error"] + cu["dudosa"], cu["n"])),
                             "tasa_sin_dudosas": r4(F(cu["con error"], cu["n"] - cu["dudosa"])) if cu["n"] - cu["dudosa"] else None}

# 4. La cola
cu = cuenta("cola", R_ERR)
Nc = U["cola"]["N_por_celda"]
wc = {c: F(Nc[c], sum(Nc.values())) for c in CELDAS}
cola = {"N_por_celda": Nc, "pesos": {c: r4(wc[c]) for c in CELDAS}, "por_celda": cu, "base_tanda0": U["cola"]["base_tanda0"]}
for nombre, kfun, nfun in (("regla", lambda c: cu[c]["con error"] + cu[c]["dudosa"], lambda c: cu[c]["n"]),
                           ("sensibilidad_sin_dudosas", lambda c: cu[c]["con error"], lambda c: cu[c]["n"] - cu[c]["dudosa"])):
    k = {c: kfun(c) for c in CELDAS}
    n = {c: nfun(c) for c in CELDAS}
    pq = ponderada(wc, k, n)
    wl = wil(pq["T"], pq["n_ef"])
    cola[nombre] = {"k_por_celda": k, "n_por_celda": n, "errores": sum(k.values()), "leidas": sum(n.values()),
                    "tasa_ponderada": r4(pq["T"]), "n_efectivo_kish": round(float(pq["n_ef"]), 3), "wilson": wl,
                    "regla_del_25_se_dispara": RU.wilson(float(pq["T"]), float(pq["n_ef"]))[1] > 0.25}
cola["la_sensibilidad_da_otra_decision"] = {"regla_del_25": cola["regla"]["regla_del_25_se_dispara"] != cola["sensibilidad_sin_dudosas"]["regla_del_25_se_dispara"]}
res["cola"] = cola


# 5. Las vigilancias y la (12)
def vigilancia(m: str, respuestas: list, vigilada: str, fuera: list, N: dict, entera: bool) -> dict:
    cu = cuenta(m, respuestas)
    tot = {r: sum(cu[c][r] for c in CELDAS) for r in respuestas}
    k = {c: cu[c][vigilada] for c in CELDAS}
    n = {c: cu[c]["n"] - sum(cu[c][r] for r in fuera) for c in CELDAS}
    out = {"N_por_celda": N, "por_celda": cu, "por_respuesta": tot, "leidas": sum(cu[c]["n"] for c in CELDAS),
           "vigilada": vigilada, "fuera_de_la_tasa": {r: tot[r] for r in fuera}}
    kk, nn = sum(k.values()), sum(n.values())
    out["cruda"] = {"k": kk, "n": nn, "tasa": r4(F(kk, nn)) if nn else None, "wilson": wil(F(kk, nn), nn) if nn else None}
    if not entera:
        w = {c: F(N[c], sum(N.values())) for c in CELDAS}
        pq = ponderada(w, k, n)
        out["pesos"] = {c: r4(w[c]) for c in CELDAS}
        out["ponderada_por_celda"] = {"tasa": r4(pq["T"]), "n_efectivo_kish": round(float(pq["n_ef"]), 3), "wilson": wil(pq["T"], pq["n_ef"])}
    else:
        out["ponderada_por_celda"] = "se leyó entera, sin celdas: solo la cruda"
    return out


V = res["vigilancias"]
V["vigilancia:1"] = vigilancia("vigilancia:1", ["sí", "no", "no decidible"], "sí", ["no decidible"], POB4["vigilancia:1"]["N_por_celda"], False)
V["vigilancia:2"] = vigilancia("vigilancia:2", ["vaciamiento", "no vaciamiento", "no decidible"], "vaciamiento", [],
                               U["otras"]["vigilancia:2"]["N_por_celda"], False)
V["vigilancia:3"] = vigilancia("vigilancia:3", ["duplicación", "distintos"], "duplicación", [], POB4["vigilancia:3"]["N_por_celda"], False)
V["vigilancia:3"]["declaracion"] = ("el grupo es de nodos con la misma unidad y el mismo tramo, así que no ve las duplicaciones con tramos "
                                    "distintos (registro de decisiones, §29; LEEME de la lectura de T4)")
V["vigilancia:7"] = vigilancia("vigilancia:7", ["con apoyo", "sin apoyo", "no decidible"], "sin apoyo", [],
                               U["otras"]["vigilancia:7"]["N_por_celda"], True)
for m in ("vigilancia:2", "vigilancia:7"):
    V[m]["no_decidibles"] = ("en el denominador; la muestra no tiene ninguna" if not V[m]["por_respuesta"]["no decidible"]
                             else "en el denominador")
# la (12): correctas sobre 30, las no decidibles aparte y en el denominador
f12 = L["observacion:12"]
cu12 = {c: {"correcta": 0, "no decidible": 0, "incorrecta": 0, "n": len(f12["por_celda"][c])} for c in CELDAS}
capas = {}
for c in CELDAS:
    for f in f12["por_celda"][c]:
        x = f["veredicto_autora"]
        if x.startswith("incorrecta"):
            cu12[c]["incorrecta"] += 1
            capa = RE_INC.match(x).group(1)
            capas.setdefault(capa, []).append({"id": f["id"], "ficha": f["ficha"]})
        else:
            cu12[c][x] += 1
N12 = POB4["observacion:12"]["N_por_celda"]
w12 = {c: F(N12[c], sum(N12.values())) for c in CELDAS}
k12 = {c: cu12[c]["correcta"] for c in CELDAS}
n12 = {c: cu12[c]["n"] for c in CELDAS}
pq = ponderada(w12, k12, n12)
kk, nn = sum(k12.values()), sum(n12.values())
res["observacion:12"] = {
    "N_por_celda": N12, "pesos": {c: r4(w12[c]) for c in CELDAS}, "por_celda": cu12,
    "por_respuesta": {r: sum(cu12[c][r] for c in CELDAS) for r in ("correcta", "no decidible", "incorrecta")},
    "incorrectas_por_capa_pipeline": {k: {"n": len(v), "elementos": v} for k, v in sorted(capas.items())},
    "cruda": {"correctas": kk, "de": nn, "tasa": r4(F(kk, nn)), "wilson": wil(F(kk, nn), nn)},
    "ponderada_por_celda": {"tasa": r4(pq["T"]), "n_efectivo_kish": round(float(pq["n_ef"]), 3), "wilson": wil(pq["T"], pq["n_ef"])},
    "como": "correctas sobre 30, con las no decidibles aparte y en el denominador (enmienda de la observación 12, :107-111)",
    "pesos_de": "t3/muestras/poblaciones_t4t1_tf.json (las aristas de extracción de la (10), sin remite_a, en el grafo sin cola de la tanda)",
    "linea_de_base_tanda0": "25 de 30, Wilson [0,664; 0,927], con el perfil anterior (pre-registro de la tanda 1, §5.2, como lo da tanda1/t4/scripts/tasas_t4t2.py)"}

# la ampliación: salta si salta la atención de un estrato o la de RI (con la regla de las dudosas)
salta = {f"aceptadas:{s}": res["aceptadas"][s]["regla"]["atencion"] for s in ESTR} | {"RI": res["atencion_RI"]["regla"]["atencion"]}
res["ampliacion"] = {"salta": salta, "hay_ampliacion": any(salta.values()),
                     "con_la_sensibilidad": {f"aceptadas:{s}": res["aceptadas"][s]["sensibilidad_sin_dudosas"]["atencion"] for s in ESTR}
                     | {"RI": res["atencion_RI"]["sensibilidad_sin_dudosas"]["atencion"]}}
# 6. Las líneas de base: la tanda 1, de la versión derivada, y la tanda 0 al lado
b0 = lambda s: f"{RU.BASE[s]['k']} de {RU.BASE[s]['n']}, Wilson [{RU.BASE[s]['wilson'][0]:.4f}; {RU.BASE[s]['wilson'][1]:.4f}]".replace(".", ",")  # noqa: E731
t0 = U["tasa_ponderada_total"]["tanda0_con_el_mismo_metodo"]
res["lineas_de_base"] = {
    "fuente_tanda1": "los valores T4.* de tanda_final/preregistro/preregistro_tanda_final_derivada_T4.huecos.json (versión derivada para la lectura)",
    "aceptadas:items": {"tanda1": HU["T4.aceptadas_items"]["valor"], "tanda0": b0("items") + " (BASE del script de la mesa)"},
    "aceptadas:no_items": {"tanda1": HU["T4.aceptadas_no_items"]["valor"], "tanda0": b0("no_items") + " (BASE del script de la mesa)"},
    "aceptadas:total": {"tanda1": HU["T4.ponderada_total"]["valor"],
                        "tanda0": f"{t0['p']:.4f}, Wilson [{t0['wilson'][0]:.4f}; {t0['wilson'][1]:.4f}], mismo método (umbrales_t4_tf.json)".replace(".", ",")},
    "atencion_RI": {"tanda1": HU["T4.atencion_RI"]["valor"],
                    "tanda0": f"la tasa de RI bajo H0, con las tasas de la tanda 0: {U['atencion_RI']['tasa_de_RI_bajo_H0']:.4f} (umbrales_t4_tf.json)".replace(".", ",")},
    "cola": {"tanda1": HU["T4.cola"]["valor"], "tanda0": U["cola"]["base_tanda0"]},
    "vigilancias_y_12": {"tanda1": HU["T4.vigilancias_y_12"]["valor"],
                         "tanda0": {"vigilancia:1": "no se midió en la tanda 0", "vigilancia:3": "no se midió en la tanda 0",
                                    "vigilancia:2": "en la tanda 0 se midió la población, sin leer la muestra",
                                    "vigilancia:7": "en la tanda 0 se midió la población, sin leer la muestra",
                                    "observacion:12": res["observacion:12"]["linea_de_base_tanda0"],
                                    "fuente": "tanda1/t4/scripts/tablas_t4t2.py (BASEV) y tasas_t4t2.py"}}}
res["entradas"] = {"umbrales_t4_tf.json": UMBRALES_SHA, "umbrales_t4_por_celdas_mesa.py": sha(MESA),
                   "preregistro_tanda_final_derivada_T4.md": DERIVADA_SHA, "preregistro_tanda_final_derivada_T4.huecos.json": HUECOS_SHA,
                   "poblaciones_t4_t3f_tf.json (t3)": sha(TF / "t3/muestras/poblaciones_t4_t3f_tf.json"),
                   "poblaciones_t4t1_tf.json (t3)": sha(TF / "t3/muestras/poblaciones_t4t1_tf.json"),
                   "sello_lectura_T4.txt": sha(LA / "sello_lectura_T4.txt"),
                   **{f"{p}_marcada.csv": sha(LA / f"{p}_marcada.csv") for p, _, _ in MUESTRAS.values()},
                   **{f"muestra {m}": sha(a) for m, (_, a, _) in MUESTRAS.items()}}
res["hora"] = datetime.now().astimezone().isoformat(timespec="seconds")
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
DIST.write_text(json.dumps(dist_out, ensure_ascii=False) + "\n", encoding="utf-8")

# la consola
print("controles:", sum(controles.values()), "de", len(controles), "| la mesa, importada, byte a byte:",
      controles["el script de la mesa, importado, da su JSON byte a byte"])
for s in ESTR:
    b = res["aceptadas"][s]
    for nombre in ("regla", "sensibilidad_sin_dudosas"):
        x = b[nombre]
        print(f"aceptadas:{s} [{nombre}] errores {x['errores']} de {x['leidas']} | k {x['k_por_celda']} n {x['n_por_celda']} | T {x['tasa_ponderada']} "
              f"Wilson {x['wilson']} n_ef {x['n_efectivo_kish']} | p {x['p_valor_atencion']} atención {x['atencion']} | freno {x['freno_por_intervalos']}")
    print(f"   umbrales de T3: atención desde {b['umbrales_T3']['atencion_desde']}, freno desde {b['umbrales_T3']['freno_por_intervalos_desde']}; "
          f"la sensibilidad da otra decisión: {b['la_sensibilidad_da_otra_decision']}")
for nombre in ("regla", "sensibilidad_sin_dudosas"):
    print(f"total [{nombre}]", res["aceptadas"]["total"][nombre])
for nombre in ("regla", "sensibilidad_sin_dudosas"):
    x = res["atencion_RI"][nombre]
    print(f"RI [{nombre}] errores {x['errores']} de {x['leidas']} | t {x['tasa_ponderada_RI']} Wilson {x['wilson']} n_ef {x['n_efectivo_kish']} | "
          f"p {x['p_valor_atencion']} atención {x['atencion']}")
print("NG sin_raiz:", res["NG_sin_raiz"])
for nombre in ("regla", "sensibilidad_sin_dudosas"):
    x = res["cola"][nombre]
    print(f"cola [{nombre}] errores {x['errores']} de {x['leidas']} | T {x['tasa_ponderada']} Wilson {x['wilson']} n_ef {x['n_efectivo_kish']} | "
          f"regla del 25 % se dispara {x['regla_del_25_se_dispara']}")
for m, x in V.items():
    print(m, x["por_respuesta"], "| cruda", x["cruda"], "| ponderada", x["ponderada_por_celda"])
o = res["observacion:12"]
print("observacion:12", o["por_respuesta"], "| cruda", o["cruda"], "| ponderada", o["ponderada_por_celda"], "| por capa",
      {k: v["n"] for k, v in o["incorrectas_por_capa_pipeline"].items()})
print("ampliación:", res["ampliacion"])
print("salida:", OUT.name, sha(OUT), "| distribuciones:", DIST.name, sha(DIST))
