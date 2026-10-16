"""Mesa, 16/10/2026: la atención, el freno y el intervalo de las aceptadas de T4 con las celdas fijas por clase y modo (decisión de la
autora del 16/10/2026), contra la línea de base de la tanda 0. Solo calcula: no lee el grafo ni usa la API.
  - Celdas de cada muestra de 30: RI sin_raiz 10, RI resto 5, NG sin_raiz 5, NG resto 10. En las aceptadas, lo mismo en cada estrato.
  - La tasa de un estrato es la ponderada por las unidades de cada celda: T = suma de w_c * k_c / n_c, con w_c = N_c / N (las unidades de
    la celda en la población que se muestrea, que se cuentan en T4 antes de leer).
  - Atención: test exacto unilateral al 5 % contra la tasa de la tanda 0 del estrato (p0). Bajo H0 cada celda tiene tasa p0 y k_c sigue
    una binomial (n_c, p0); la distribución de T se enumera entera. Hay atención si P(T >= t observado) <= 0,05.
  - Intervalo de T: Wilson al 95 % con el tamaño efectivo de Kish, n_ef = 1 / suma de w_c^2 / n_c. Con un sorteo simple (w_c = n_c / n) es
    el Wilson de siempre.
  - Freno: si el intervalo de T no se solapa con el Wilson de la tanda 0 (su límite inferior pasa el superior de la tanda 0), o si la
    atención se confirma sobre las 60 (cada celda con el doble de unidades).
  - Control: con w_c = n_c / 30 tiene que reproducir los cuatro umbrales de un sorteo simple (11 y 8 de 30; 17 y 14 de 30).
  - La atención propia de RI (decisión de la autora del 16/10/2026): junta los dos estratos, sus 30 unidades leídas (15 de ítems y 15 de
    no ítems), con la tasa ponderada por las unidades de sus cuatro celdas, v = N_(s,c) / N_RI. Test exacto unilateral al 5 % con cada
    celda, bajo H0, en la tasa de la tanda 0 de su estrato. NG no lleva atención propia.
  - La probabilidad de que salte al menos una atención (la de ítems, la de no ítems o la de RI) con todas las celdas en la tasa de la
    tanda 0 se calcula exacta, condicionando en las cuatro celdas RI, que comparten las tres atenciones.
Uso: python3 -I -B <este> <salida.json>"""
import itertools, json, math, sys
from fractions import Fraction as F
Z = 1.959964
CELDAS = ["RI:sin_raiz", "RI:resto", "NG:sin_raiz", "NG:resto"]
CUOTA = {"RI:sin_raiz": 10, "RI:resto": 5, "NG:sin_raiz": 5, "NG:resto": 10}
# Unidades de la E0 de la tanda 1 por celda (lista de S2, sha256 22f33a17…): la proyección de los pesos, si la aceptación y la proporción de
# ítems no dependen de la celda. Los pesos de verdad salen en T4 de la población de cada muestra.
E0 = {"RI:sin_raiz": 297, "RI:resto": 157, "NG:sin_raiz": 94, "NG:resto": 2742}
BASE = {"items": {"k": 6, "n": 30, "wilson": [0.09505107121882947, 0.3730569656380418]},
        "no_items": {"k": 4, "n": 30, "wilson": [0.05309655447112463, 0.2968132683539402]}}  # estimadores_l2.json
W_T0 = {"items": 1003 / 2366, "no_items": 1363 / 2366}  # pesos de los estratos de la tanda 0 (estimadores_l2.json)
def wilson(p, n, z=Z):
    if n <= 0: return [0.0, 1.0]
    d = 1 + z * z / n; c = (p + z * z / (2 * n)) / d; m = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return [max(0.0, c - m), min(1.0, c + m)]
def pmf(k, n, p): return math.comb(n, k) * p ** k * (1 - p) ** (n - k)
def distribucion(w, n, p):
    """Distribución exacta de T = suma w_c k_c / n_c, con k_c ~ Bin(n_c, p) independientes (w en Fraction)."""
    dist = {}
    for ks in itertools.product(*[range(n[c] + 1) for c in CELDAS]):
        t = sum(w[c] * F(k, n[c]) for c, k in zip(CELDAS, ks))
        pr = math.prod(pmf(k, n[c], p) for c, k in zip(CELDAS, ks))
        dist[t] = dist.get(t, 0.0) + pr
    return dist
def cola_sup(dist): 
    vals = sorted(dist); acum = 0.0; out = {}
    for t in reversed(vals): acum += dist[t]; out[t] = acum
    return out
def umbrales(w, n, base):
    p0 = F(base["k"], base["n"]); neff = 1 / float(sum(w[c] ** 2 / n[c] for c in CELDAS))
    d0 = distribucion(w, n, float(p0)); sup = cola_sup(d0)
    t_at = min(t for t in sup if sup[t] <= 0.05)
    t_fr = min((t for t in sup if wilson(float(t), neff)[0] > base["wilson"][1]), default=None)
    n60 = {c: 2 * n[c] for c in CELDAS}; sup60 = cola_sup(distribucion(w, n60, float(p0)))
    t_at60 = min(t for t in sup60 if sup60[t] <= 0.05)
    poder = {}
    for nombre, p1 in (("tasa_doble_en_todas_las_celdas", {c: 2 * float(p0) for c in CELDAS}),
                       ("sin_raiz_a_0,5_y_el_resto_en_p0", {c: (0.5 if "sin_raiz" in c else float(p0)) for c in CELDAS})):
        # potencia del test por celdas: P(T >= t_at) con cada celda en su tasa
        pr = 0.0
        for ks in itertools.product(*[range(n[c] + 1) for c in CELDAS]):
            if sum(w[c] * F(k, n[c]) for c, k in zip(CELDAS, ks)) >= t_at:
                pr += math.prod(pmf(k, n[c], p1[c]) for c, k in zip(CELDAS, ks))
        # la del sorteo simple de 30 sobre la misma población: k ~ Bin(30, tasa ponderada), umbral binomial
        pw = sum(float(E0w[c]) * p1[c] for c in CELDAS); k_srs = min(k for k in range(31) if sum(pmf(j, 30, float(p0)) for j in range(k, 31)) <= 0.05)
        poder[nombre] = {"celdas": round(pr, 4), "sorteo_simple": round(sum(pmf(j, 30, pw) for j in range(k_srs, 31)), 4), "tasa_ponderada_verdadera": round(pw, 4)}
    return {"p0": float(p0), "n_efectivo_kish": round(neff, 3),
            "atencion": {"umbral_tasa_ponderada": round(float(t_at), 4), "p_valor_en_el_umbral": round(sup[t_at], 4)},
            "freno_por_intervalos": {"umbral_tasa_ponderada": round(float(t_fr), 4) if t_fr is not None else None,
                                     "wilson_en_el_umbral": [round(x, 4) for x in wilson(float(t_fr), neff)] if t_fr is not None else None,
                                     "superior_tanda0": round(base["wilson"][1], 4)},
            "freno_por_atencion_sobre_60": {"umbral_tasa_ponderada": round(float(t_at60), 4), "p_valor": round(sup60[t_at60], 4)},
            "potencia_de_la_atencion": poder}
def errores_minimos(w, n, t):
    """Cuántos errores hacen falta, todos en una celda, para llegar a t (None si no alcanza)."""
    out = {}
    for c in CELDAS:
        k = next((k for k in range(n[c] + 1) if w[c] * F(k, n[c]) >= t), None); out[c] = f"{k} de {n[c]}" if k is not None else "no alcanza sola"
    return out
res = {"unidad": "muestras de T4 por celdas (pre-registro de la tanda 1, v8)", "z": Z, "cuotas": CUOTA, "unidades_e0_por_celda": E0}
N = sum(E0.values()); E0w = {c: F(E0[c], N) for c in CELDAS}
SRSw = {c: F(CUOTA[c], 30) for c in CELDAS}
res["control_sorteo_simple"] = {s: umbrales(SRSw, CUOTA, BASE[s]) for s in BASE}
for s, esperado in (("items", (11, 17, 22)), ("no_items", (8, 14, 16))):
    u = res["control_sorteo_simple"][s]
    assert round(u["atencion"]["umbral_tasa_ponderada"] * 30) == esperado[0], (s, u)
    assert round(u["freno_por_intervalos"]["umbral_tasa_ponderada"] * 30) == esperado[1], (s, u)
res["control_sorteo_simple"]["reproduce_11_8_17_14"] = True
res["proyeccion_pesos_e0"] = {"pesos": {c: round(float(E0w[c]), 4) for c in CELDAS}}
for s in BASE:
    u = umbrales(E0w, CUOTA, BASE[s])
    u["errores_minimos_en_una_sola_celda_para_la_atencion"] = errores_minimos(E0w, CUOTA, F(u["atencion"]["umbral_tasa_ponderada"]).limit_denominator(10**6))
    res["proyeccion_pesos_e0"][s] = u
# Tasa ponderada total (los dos estratos): Wilson con el n efectivo de Kish de las ocho celdas.
def neff_total(Ws, w, n): return 1 / sum(float(Ws[s]) ** 2 * float(w[c]) ** 2 / n[c] for s in Ws for c in CELDAS)
res["tasa_ponderada_total"] = {
    "metodo": "p = suma W_s T_s; Wilson al 95 % con n_ef = 1 / suma (W_s w_c)^2 / n_c, con los pesos de los estratos y de las celdas de T4",
    "n_efectivo_proyectado": round(neff_total(W_T0, E0w, CUOTA), 3),
    "tanda0_con_el_mismo_metodo": {"p": round(W_T0["items"] * 6 / 30 + W_T0["no_items"] * 4 / 30, 4),
                                   "n_efectivo": round(1 / (W_T0["items"] ** 2 / 30 + W_T0["no_items"] ** 2 / 30), 3)}}
t0 = res["tasa_ponderada_total"]["tanda0_con_el_mismo_metodo"]; t0["wilson"] = [round(x, 4) for x in wilson(t0["p"], t0["n_efectivo"])]
t0["como_se_reporto_en_la_tanda0"] = {"p": 0.1616, "intervalo95_normal": [0.0689, 0.2543], "conservador95": [0.0709, 0.3291]}
# La cola: la regla del 25 % (límite superior de Wilson) con los pesos proyectados.
ne = 1 / float(sum(E0w[c] ** 2 / CUOTA[c] for c in CELDAS))
res["cola_regla_del_25"] = {"n_efectivo_proyectado": round(ne, 3), "superior_con_0_errores": round(wilson(0.0, ne)[1], 4),
    "superior_con_1_error_en_cada_celda_sola": {c: round(wilson(float(E0w[c] / CUOTA[c]), ne)[1], 4) for c in CELDAS},
    "en_el_sorteo_simple": "tolera hasta 2 errores de 30 (superior 21,3 %; con 3, 25,6 %)"}
# La atención propia de RI, con los pesos proyectados: cada celda, en los dos estratos, con la proporción de ítems de la tanda 0.
RI = ["RI:sin_raiz", "RI:resto"]; ESTR = ["items", "no_items"]
N_RI = sum(E0[c] for c in RI)
v = {(s, c): F(E0[c], N_RI) * F(W_T0[s]).limit_denominator(10**9) for s in ESTR for c in RI}
p0 = {s: BASE[s]["k"] / BASE[s]["n"] for s in ESTR}
celdas_ri = [(s, c) for s in ESTR for c in RI]
def dist_ri(prob):
    d = {}
    for ks in itertools.product(*[range(CUOTA[c] + 1) for s, c in celdas_ri]):
        tt = sum(v[sc] * F(k, CUOTA[sc[1]]) for sc, k in zip(celdas_ri, ks))
        pr = math.prod(pmf(k, CUOTA[sc[1]], prob[sc]) for sc, k in zip(celdas_ri, ks))
        d[tt] = d.get(tt, 0.0) + pr
    return d
sup_ri = cola_sup(dist_ri({sc: p0[sc[0]] for sc in celdas_ri}))
t_ri = min(tt for tt in sup_ri if sup_ri[tt] <= 0.05)
pot_ri = sum(pr for tt, pr in dist_ri({sc: 2 * p0[sc[0]] for sc in celdas_ri}).items() if tt >= t_ri)
# Al menos una atención bajo H0: se condiciona en las celdas RI de cada estrato.
t_estr = {s: F(res["proyeccion_pesos_e0"][s]["atencion"]["umbral_tasa_ponderada"]).limit_denominator(10**6) for s in ESTR}
t_estr_exacto = {}
for s in ESTR:
    sup = cola_sup(distribucion(E0w, CUOTA, p0[s])); t_estr_exacto[s] = min(tt for tt in sup if sup[tt] <= 0.05)
def p_estrato_sin_atencion(s, k_sr, k_re):
    base_ri = E0w["RI:sin_raiz"] * F(k_sr, CUOTA["RI:sin_raiz"]) + E0w["RI:resto"] * F(k_re, CUOTA["RI:resto"])
    tot = 0.0
    for k1 in range(CUOTA["NG:sin_raiz"] + 1):
        for k2 in range(CUOTA["NG:resto"] + 1):
            tt = base_ri + E0w["NG:sin_raiz"] * F(k1, CUOTA["NG:sin_raiz"]) + E0w["NG:resto"] * F(k2, CUOTA["NG:resto"])
            if tt < t_estr_exacto[s]: tot += pmf(k1, CUOTA["NG:sin_raiz"], p0[s]) * pmf(k2, CUOTA["NG:resto"], p0[s])
    return tot
ninguna = 0.0
for ks in itertools.product(*[range(CUOTA[c] + 1) for s, c in celdas_ri]):
    k = dict(zip(celdas_ri, ks))
    tt = sum(v[sc] * F(k[sc], CUOTA[sc[1]]) for sc in celdas_ri)
    if tt >= t_ri: continue
    pr = math.prod(pmf(k[sc], CUOTA[sc[1]], p0[sc[0]]) for sc in celdas_ri)
    ninguna += pr * p_estrato_sin_atencion("items", k[("items", "RI:sin_raiz")], k[("items", "RI:resto")]) \
                  * p_estrato_sin_atencion("no_items", k[("no_items", "RI:sin_raiz")], k[("no_items", "RI:resto")])
res["atencion_RI"] = {
    "metodo": "test exacto unilateral al 5 % sobre la tasa ponderada de RI en los dos estratos; bajo H0, cada celda en la tasa de la tanda 0 de su estrato",
    "pesos_proyectados": {f"{s}:{c}": round(float(v[(s, c)]), 4) for s, c in celdas_ri},
    "n_efectivo_kish": round(1 / float(sum(v[sc] ** 2 / CUOTA[sc[1]] for sc in celdas_ri)), 3),
    "umbral_tasa_ponderada": round(float(t_ri), 4), "p_valor_en_el_umbral": round(sup_ri[t_ri], 4),
    "tasa_de_RI_bajo_H0": round(sum(float(v[sc]) * p0[sc[0]] for sc in celdas_ri), 4),
    "potencia_con_la_tasa_de_RI_duplicada": round(pot_ri, 4),
    "al_menos_una_atencion_bajo_H0": {"items_no_items_o_RI": round(1 - ninguna, 4),
                                       "solo_las_dos_de_los_estratos": round(1 - (1 - cola_sup(distribucion(E0w, CUOTA, p0["items"]))[t_estr_exacto["items"]]) * (1 - cola_sup(distribucion(E0w, CUOTA, p0["no_items"]))[t_estr_exacto["no_items"]]), 4)},
    "ampliacion": "si salta, 30 unidades RI más: 15 por estrato, con las cuotas de RI (10 sin_raiz y 5 del resto) y las cadenas de la ampliación"}
open(sys.argv[1], "w", encoding="utf-8").write(json.dumps(res, ensure_ascii=False, indent=1) + "\n")
print("RI:", {k: res["atencion_RI"][k] for k in ("n_efectivo_kish", "umbral_tasa_ponderada", "p_valor_en_el_umbral", "tasa_de_RI_bajo_H0", "potencia_con_la_tasa_de_RI_duplicada", "al_menos_una_atencion_bajo_H0")})
for s in BASE:
    u = res["proyeccion_pesos_e0"][s]
    print(s, "n_ef", u["n_efectivo_kish"], "| atención desde", u["atencion"], "| freno", u["freno_por_intervalos"]["umbral_tasa_ponderada"], "| sobre 60", u["freno_por_atencion_sobre_60"]["umbral_tasa_ponderada"])
    print("   potencia", u["potencia_de_la_atencion"]); print("   errores en una sola celda", u["errores_minimos_en_una_sola_celda_para_la_atencion"])
print("total", res["tasa_ponderada_total"]["n_efectivo_proyectado"], t0); print("cola", res["cola_regla_del_25"])
