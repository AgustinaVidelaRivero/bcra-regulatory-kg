"""
analisis_ablacion.py — Pipeline de ANÁLISIS de la ablación (U-A1.4), sobre los
resultados del replay (`resultados/replay_<celda>.json`). Determinístico, $0.
Todo umbral y semilla vienen de `comun_corrida` POR REFERENCIA al pre-registro
sellado (§4 métrica, §5 predicciones y regla de lectura); ninguno se toca.

Qué computa (mandato fase B (5)–(10)):
  (5) TABLA CENTRAL — por celda × variante: n_casos, n_anclas (denominador
      micro), vistas, consultadas, brecha v-s-c, recall vista/consultada MICRO
      (pooled por ancla) y MACRO (promedio por caso), exactamente como
      `ev2_corrida/navegabilidad/agregados_navegabilidad_ev2.py`; grupos:
      `todos`, cohorte núcleo limpio E-E, cohorte dirigida E-A..E-D (SEPARADAS,
      jamás promediadas entre sí), por estrato y por sub-estrato. Brecha
      Δ = literal − anti-léxica por celda y grupo (vista/consultada, micro/macro).
  (6) DIFERENCIAS APAREADAS por par entre celdas: punto sobre los pares
      apareados (presentes en las 4 celdas) e IC bootstrap 95 % percentil
      (remuestreo de PARES con reposición, semilla `bootstrap-ablacion-v1`,
      10.000 remuestreos, `random.Random` — determinístico): recall consultada
      micro y macro y recall vista micro por variante para C10−C00, C01−C00,
      C11−C00, C11−C10, C11−C01; diferencias de brecha Δ_c(A)−Δ_c(B) y el
      término de interacción de P5. Ningún test se agrega después de ver datos.
  (7) EVALUACIÓN MECÁNICA P1–P6 contra los umbrales sellados, regla de lectura
      textual: veredictos `cumplida` / `no cumplida` / `no evaluable` (clase con
      < 8 pares ⇒ no evaluable a priori); si P1 no se cumple, P2–P6 se declaran
      `no evaluable` y se REPORTAN igual con sus valores. Nivel de agregación
      de P1–P5: grupo `todos`, recall MICRO (el mismo nivel de la referencia
      publicada 0,958 → 0,620 de EV2 §4/§5); lecturas por cohorte, aparte.
  (8) P4 sobre E-B/entrante y sobre la clase {hit_tool_limit ∨ n_brecha>0 en C00};
      P6 sobre los nodos gold huérfanos marcados ex-ante (pares_v3 / validacion_v3).
  (9) tasas de hit_tool_limit, abstención (parse_ok y `respondible == false`),
      parse_ok, error técnico persistido, por celda (y por variante).
 (10) latencia end-to-end por pregunta (p50/p95 por celda y variante) y por
      tool (p50/p95 de la latencia por llamada, por celda).

Operacionalizaciones que el pre-registro deja implícitas se DECLARAN en
`analisis["operacionalizaciones"]` (la lectura interpretativa es de la mesa).

Uso:  .venv/bin/python -B analisis_ablacion.py   → resultados/analisis_ablacion.json
                                                    + resultados/reporte_analisis.md
"""

from __future__ import annotations

import json
import random
import sys
from pathlib import Path

CORRIDA_DIR = Path(__file__).resolve().parent
if str(CORRIDA_DIR) not in sys.path:
    sys.path.insert(0, str(CORRIDA_DIR))

from comun_corrida import (COHORTE_DIRIGIDA, ESTRATOS, N_BOOTSTRAP, ORDEN_CELDAS,  # noqa: E402
                           RESULTADOS_DIR, SEMILLA_BOOTSTRAP, UMBRALES, VARIANTES,
                           cargar_pares, huerfanos_p6, rel_repo)

C00, C10, C01, C11 = ORDEN_CELDAS
COMPARACIONES = [(C10, C00), (C01, C00), (C11, C00), (C11, C10), (C11, C01)]
COMPARACIONES_BRECHA = [(C10, C00), (C11, C01), (C01, C00), (C11, C10)]
GRUPOS_COHORTE = {"todos": None, "cohorte_nucleo_limpio_EE": {"E-E"},
                  "cohorte_dirigida_EA_ED": COHORTE_DIRIGIDA}
SUB_ESTRATOS = ["E-B/entrante", "E-B/saliente", "E-D/intra_to", "E-D/inter_to"]

OPERACIONALIZACIONES = {
    "nivel_P1_P5": "grupo `todos` (todos los pares apareados), recall MICRO pooled por ancla — mismo nivel que la referencia EV2 (0,958→0,620); las cohortes E-E y E-A..E-D se reportan aparte y no entran promediadas",
    "pares_apareados": "solo pares con las 2 variantes presentes en las 4 celdas entran a la tabla central, a las diferencias y a P1–P6; los faltantes se listan",
    "P4_i": "sub-estrato E-B/entrante; recall consultada micro POOLED sobre ambas variantes (el pre-registro no fija variante); se reporta además por variante",
    "P4_ii_a": "tasa de hit_tool_limit = trazas con hit_tool_limit / trazas de la celda (ambas variantes)",
    "P4_ii_b": "clase K = (par, variante) cuya traza en C00 tiene hit_tool_limit o n_brecha > 0; 'pasa a consultada' = recall_consultada(C01) > recall_consultada(C00) (estrictamente mayor); se compara la fracción en K vs el resto; evaluable si K y resto tienen >= 8 pares distintos",
    "P4_iii": "efecto de T = recall_c anti micro (C01 − C00); efecto de R = (C10 − C00); cumplida si T < R",
    "P4_veredicto": "cumplida si (i), (ii-a), (ii-b) y (iii) cumplidas; no cumplida si alguna no cumplida; no evaluable si alguna no evaluable y ninguna no cumplida",
    "P5": "mejor celda = C11 estrictamente máxima en recall consultada micro anti-léxica; aditividad |(C11−C00) − [(C10−C00)+(C01−C00)]| <= 0,10",
    "P6": "unidad = (par, variante, nodo gold huérfano de label) sobre los 11 pares marcados ex-ante; (i) fracción vista C10 <= C00 + 0,10; (ii) fracción consultada en celdas v2 (C01 ∪ C11 pooled) > celdas v1 (C00 ∪ C10 pooled), y además por par de celdas; tasa de paginación = llamadas ver_vecinos con pagina > 1 / llamadas ver_vecinos, en celdas v2",
    "abstencion": "traza con parse_ok y final_json.respondible == false",
    "error_tecnico": "traza con trace.error no nulo (persistida; la métrica se computa sobre sus steps)",
    "percentil": "interpolación lineal entre órdenes (tipo numpy default) sobre los valores presentes",
    "no_evaluable_n": f"una clase con < {UMBRALES['n_min_pares_clase']} pares distintos es no evaluable a priori",
}


# --------------------------------------------------------------------------- #
# Utilidades                                                                    #
# --------------------------------------------------------------------------- #
def _r(x, nd=4):
    return None if x is None else round(x, nd)


def percentil(vals: list[float], q: float) -> float | None:
    v = sorted(x for x in vals if x is not None)
    if not v:
        return None
    if len(v) == 1:
        return v[0]
    pos = (len(v) - 1) * q
    lo, hi = int(pos), min(int(pos) + 1, len(v) - 1)
    return v[lo] + (v[hi] - v[lo]) * (pos - lo)


def celda_agg(casos: list[dict]) -> dict:
    """Agregado de una celda de la tabla (patrón agregados_navegabilidad_ev2.celda)."""
    n = len(casos)
    if n == 0:
        return {"n_casos": 0, "n_pares": 0}
    na = sum(c["n_anclas"] for c in casos)
    nv = sum(c["n_vistas"] for c in casos)
    nc = sum(c["n_consultadas"] for c in casos)
    nb = sum(c["n_brecha"] for c in casos)
    con_r = [c for c in casos if c["recall_vista"] is not None]
    return {
        "n_casos": n, "n_pares": len({c["sample_id"] for c in casos}),
        "n_anclas": na, "n_vistas": nv, "n_consultadas": nc, "n_brecha_vista_sin_consultar": nb,
        "recall_vista_micro": _r(nv / na) if na else None,
        "recall_consultada_micro": _r(nc / na) if na else None,
        "recall_vista_macro": _r(sum(c["recall_vista"] for c in con_r) / len(con_r)) if con_r else None,
        "recall_consultada_macro": _r(sum(c["recall_consultada"] for c in con_r) / len(con_r)) if con_r else None,
    }


def _brecha(lit: dict, anti: dict) -> dict:
    out = {}
    for k in ("recall_vista_micro", "recall_consultada_micro", "recall_vista_macro", "recall_consultada_macro"):
        a, b = lit.get(k), anti.get(k)
        out[k] = _r(a - b) if (a is not None and b is not None) else None
    return out


# --------------------------------------------------------------------------- #
# Carga                                                                        #
# --------------------------------------------------------------------------- #
def cargar_replays(res_dir: Path | None = None) -> dict[str, dict]:
    res_dir = res_dir or RESULTADOS_DIR
    out = {}
    for cid in ORDEN_CELDAS:
        p = res_dir / f"replay_{cid}.json"
        with p.open(encoding="utf-8") as f:
            out[cid] = json.load(f)
    return out


def _indexar(replays: dict[str, dict]) -> dict[str, dict[str, dict]]:
    """{celda: {caso_id: resultado}}"""
    return {cid: {r["caso_id"]: r for r in rep["resultados"]} for cid, rep in replays.items()}


def pares_apareados(idx: dict[str, dict[str, dict]]) -> tuple[list[str], dict]:
    """sample_ids con las dos variantes presentes en las 4 celdas + detalle de faltantes."""
    comunes = None
    for cid in ORDEN_CELDAS:
        s = set(idx[cid])
        comunes = s if comunes is None else (comunes & s)
    comunes = comunes or set()
    sids = sorted({c.split("::")[0] for c in comunes})
    apareados = [s for s in sids if all(f"{s}::{v}" in comunes for v in VARIANTES)]
    todos = set()
    for cid in ORDEN_CELDAS:
        todos |= set(idx[cid])
    faltantes = {cid: sorted(todos - set(idx[cid])) for cid in ORDEN_CELDAS}
    return apareados, {"n_casos_union": len(todos), "faltantes_por_celda": faltantes,
                       "excluidos_por_no_apareados": sorted({c.split("::")[0] for c in todos} - set(apareados))}


# --------------------------------------------------------------------------- #
# (5) Tabla central                                                            #
# --------------------------------------------------------------------------- #
def tabla_central(idx, apareados: list[str]) -> dict:
    out = {}
    for cid in ORDEN_CELDAS:
        casos = [idx[cid][f"{s}::{v}"] for s in apareados for v in VARIANTES]
        g = {}
        for gname, estr in GRUPOS_COHORTE.items():
            sub = [c for c in casos if estr is None or c["estrato"] in estr]
            g[gname] = {v: celda_agg([c for c in sub if c["variante"] == v]) for v in VARIANTES}
            g[gname]["brecha_literal_menos_antilexica"] = _brecha(g[gname]["literal"], g[gname]["antilexica"])
        pe = {}
        for e in ESTRATOS:
            for v in VARIANTES:
                pe[f"{e}::{v}"] = celda_agg([c for c in casos if c["estrato"] == e and c["variante"] == v])
            pe[f"{e}::brecha"] = _brecha(pe[f"{e}::literal"], pe[f"{e}::antilexica"])
        ps = {}
        for se in SUB_ESTRATOS:
            for v in VARIANTES:
                ps[f"{se}::{v}"] = celda_agg([c for c in casos if c.get("sub_estrato") == se.split("/")[1]
                                              and c["estrato"] == se.split("/")[0] and c["variante"] == v])
            ps[f"{se}::ambas"] = celda_agg([c for c in casos if c.get("sub_estrato") == se.split("/")[1]
                                            and c["estrato"] == se.split("/")[0]])
        g["por_estrato_variante"] = pe
        g["por_sub_estrato"] = ps
        out[cid] = g
    return out


# --------------------------------------------------------------------------- #
# (6) Diferencias apareadas con bootstrap                                      #
# --------------------------------------------------------------------------- #
def _stats_muestra(idx, sids: list[str]) -> dict:
    """{celda: {variante: (micro_c, macro_c, micro_v)}} sobre la lista de pares dada
    (con repetición: la lista es un remuestreo)."""
    out = {}
    for cid in ORDEN_CELDAS:
        d = {}
        for v in VARIANTES:
            na = nv = nc = 0
            rs, n = 0.0, 0
            for s in sids:
                c = idx[cid][f"{s}::{v}"]
                na += c["n_anclas"]; nv += c["n_vistas"]; nc += c["n_consultadas"]
                if c["recall_consultada"] is not None:
                    rs += c["recall_consultada"]; n += 1
            d[v] = ((nc / na) if na else None, (rs / n) if n else None, (nv / na) if na else None)
        out[cid] = d
    return out


def _estadisticos(st: dict) -> dict:
    """Vector de estadísticos de interés a partir de _stats_muestra."""
    e = {}
    for a, b in COMPARACIONES:
        for v in VARIANTES:
            e[f"dif_consultada_micro::{v}::{a}-{b}"] = st[a][v][0] - st[b][v][0]
            e[f"dif_consultada_macro::{v}::{a}-{b}"] = st[a][v][1] - st[b][v][1]
            e[f"dif_vista_micro::{v}::{a}-{b}"] = st[a][v][2] - st[b][v][2]
    delta = {cid: st[cid]["literal"][0] - st[cid]["antilexica"][0] for cid in ORDEN_CELDAS}
    for cid in ORDEN_CELDAS:
        e[f"delta_c_micro::{cid}"] = delta[cid]
    for a, b in COMPARACIONES_BRECHA:
        e[f"dif_delta_c_micro::{a}-{b}"] = delta[a] - delta[b]
    anti = {cid: st[cid]["antilexica"][0] for cid in ORDEN_CELDAS}
    e["interaccion_anti_micro::(C11-C00)-[(C10-C00)+(C01-C00)]"] = (
        (anti[C11] - anti[C00]) - ((anti[C10] - anti[C00]) + (anti[C01] - anti[C00])))
    return e


def diferencias_apareadas(idx, apareados: list[str], semilla: str = SEMILLA_BOOTSTRAP,
                          n_boot: int = N_BOOTSTRAP) -> dict:
    if not apareados:
        return {"n_pares": 0, "estadisticos": {}}
    punto = _estadisticos(_stats_muestra(idx, apareados))
    rng = random.Random(semilla)
    dist = {k: [] for k in punto}
    n = len(apareados)
    for _ in range(n_boot):
        muestra = [apareados[rng.randrange(n)] for _ in range(n)]
        try:
            e = _estadisticos(_stats_muestra(idx, muestra))
        except TypeError:      # remuestreo degenerado (algún None); se omite y se cuenta
            continue
        for k, val in e.items():
            dist[k].append(val)
    out = {}
    for k, val in punto.items():
        d = dist[k]
        out[k] = {"punto": _r(val), "ic95_inf": _r(percentil(d, 0.025)), "ic95_sup": _r(percentil(d, 0.975)),
                  "n_remuestreos_validos": len(d)}
    return {"n_pares": n, "semilla": semilla, "n_remuestreos": n_boot,
            "metodo": "percentil 2,5–97,5 sobre remuestreo de pares con reposición (ambas variantes viajan con el par)",
            "estadisticos": out}


# --------------------------------------------------------------------------- #
# (9)/(10) tasas y latencias                                                   #
# --------------------------------------------------------------------------- #
def tasas_y_latencias(idx, apareados: list[str], replays: dict) -> dict:
    out = {}
    for cid in ORDEN_CELDAS:
        todas = list(idx[cid].values())      # todas las trazas presentes (no solo apareadas)
        def _t(cs):
            n = len(cs)
            if not n:
                return {"n_trazas": 0}
            cl = [c["clases"] for c in cs]
            lat = [x["latency_s"] for x in cl if x.get("latency_s") is not None]
            return {
                "n_trazas": n,
                "hit_tool_limit": sum(1 for x in cl if x["hit_tool_limit"]),
                "tasa_hit_tool_limit": _r(sum(1 for x in cl if x["hit_tool_limit"]) / n),
                "abstenciones": sum(1 for x in cl if x["abstencion"]),
                "tasa_abstencion": _r(sum(1 for x in cl if x["abstencion"]) / n),
                "parse_ok": sum(1 for x in cl if x["parse_ok"]),
                "tasa_parse_ok": _r(sum(1 for x in cl if x["parse_ok"]) / n),
                "errores_tecnicos": [{"caso_id": c["caso_id"], "error": c["clases"]["error"]}
                                     for c in cs if c["clases"]["error"]],
                "truncated_max_tokens": sum(1 for x in cl if x["truncated_max_tokens"]),
                "tool_calls_media": _r(sum(x["tool_calls_used"] or 0 for x in cl) / n),
                "latencia_s_p50": _r(percentil(lat, 0.5), 3), "latencia_s_p95": _r(percentil(lat, 0.95), 3),
                "latencia_s_media": _r(sum(lat) / len(lat), 3) if lat else None,
                "tokens_in": sum(x["tokens_in"] or 0 for x in cl), "tokens_out": sum(x["tokens_out"] or 0 for x in cl),
                "cache_read": sum(x["cache_read"] or 0 for x in cl), "cache_write": sum(x["cache_write"] or 0 for x in cl),
                "costo_usd_cli": _r(sum(x["costo_usd_cli"] or 0 for x in cl), 4),
                "costo_usd_harness": _r(sum(x["cost_usd_harness"] or 0 for x in cl), 4),
            }
        por_tool = {}
        for c in todas:
            for tool, ls in c["clases"].get("latencias_por_tool_s", {}).items():
                por_tool.setdefault(tool, []).extend(ls)
        n_vv = sum(c["clases"]["llamadas_por_tool"].get("ver_vecinos", 0) for c in todas)
        n_pag = sum(c["clases"]["n_ver_vecinos_pagina_gt1"] for c in todas)
        n_rel = sum(c["clases"]["n_ver_vecinos_con_relacion"] for c in todas)
        out[cid] = {
            "todas": _t(todas),
            "por_variante": {v: _t([c for c in todas if c["variante"] == v]) for v in VARIANTES},
            "latencia_por_tool_s": {t: {"n": len(ls), "p50": _r(percentil(ls, 0.5), 4), "p95": _r(percentil(ls, 0.95), 4)}
                                    for t, ls in sorted(por_tool.items())},
            "llamadas_por_tool": {t: sum(c["clases"]["llamadas_por_tool"].get(t, 0) for c in todas)
                                  for t in ("buscar_nodos", "ver_nodo", "ver_vecinos")},
            "ver_vecinos_pagina_gt1": {"n": n_pag, "de": n_vv, "tasa": _r(n_pag / n_vv) if n_vv else None},
            "ver_vecinos_con_relacion": {"n": n_rel, "de": n_vv, "tasa": _r(n_rel / n_vv) if n_vv else None},
            "replay_ok_todos": replays[cid]["replay_ok_todos"],
            "replay_fuerte_ok_todos": replays[cid]["replay_fuerte_ok_todos"],
            "cruce_inmemory_ok_todos": replays[cid].get("cruce_inmemory_ok_todos"),
        }
    return out


# --------------------------------------------------------------------------- #
# (7)/(8) Predicciones P1–P6 (mecánicas)                                       #
# --------------------------------------------------------------------------- #
def _ver(cond: bool | None, evaluable: bool = True, motivo: str | None = None) -> dict:
    if not evaluable:
        return {"veredicto": "no evaluable", "motivo": motivo}
    return {"veredicto": "cumplida" if cond else "no cumplida"}


def _combinar(subs: dict) -> str:
    vs = [s["veredicto"] for s in subs.values()]
    if any(v == "no cumplida" for v in vs):
        return "no cumplida"
    if any(v == "no evaluable" for v in vs):
        return "no evaluable"
    return "cumplida"


def evaluar_predicciones(tabla: dict, idx, apareados: list[str], huerfanos: dict,
                         umbrales: dict = UMBRALES) -> dict:
    U = umbrales
    nmin = U["n_min_pares_clase"]
    n_pares = len(apareados)
    T = {cid: tabla[cid]["todos"] for cid in ORDEN_CELDAS}
    rc = {cid: {v: T[cid][v].get("recall_consultada_micro") for v in VARIANTES} for cid in ORDEN_CELDAS}
    rv = {cid: {v: T[cid][v].get("recall_vista_micro") for v in VARIANTES} for cid in ORDEN_CELDAS}
    delta = {cid: T[cid]["brecha_literal_menos_antilexica"]["recall_consultada_micro"] for cid in ORDEN_CELDAS}
    P = {}

    # ---- P1 (gate) ----
    ev1 = n_pares >= nmin and delta[C00] is not None
    p1 = _ver(delta[C00] is not None and delta[C00] >= U["P1_gate_delta_c"], ev1,
              f"n_pares={n_pares} < {nmin}" if not ev1 else None)
    p1.update({"delta_c_C00": delta[C00], "umbral": U["P1_gate_delta_c"], "n_pares": n_pares,
               "recall_c_lit_C00": rc[C00]["literal"], "recall_c_anti_C00": rc[C00]["antilexica"],
               "referencia_ev2": {"delta_c": 0.338, "lit": 0.958, "anti": 0.620}})
    P["P1"] = p1
    gate = p1["veredicto"] == "cumplida"
    motivo_gate = None if gate else f"P1 {p1['veredicto']} (gate): P2–P6 se declaran no evaluables y se reportan igual"

    def _gate(d: dict) -> dict:
        if not gate:
            d["veredicto_propio"] = d["veredicto"]
            d["veredicto"] = "no evaluable"
            d["motivo"] = motivo_gate
        return d

    # ---- P2 ----
    def _le(a, b):
        return None if (a is None or b is None) else (a <= b)
    c_a = _le(delta[C10], U["P2_factor_brecha"] * delta[C00]) if delta[C00] is not None else None
    c_b = _le(delta[C11], U["P2_factor_brecha"] * delta[C01]) if delta[C01] is not None else None
    ev2 = n_pares >= nmin and c_a is not None and c_b is not None
    p2 = _ver(bool(c_a and c_b), ev2, "faltan valores" if not ev2 else None)
    p2.update({"delta_c": delta, "factor": U["P2_factor_brecha"],
               "C10_vs_C00": {"delta_C10": delta[C10], "mitad_delta_C00": _r(0.5 * delta[C00]) if delta[C00] is not None else None,
                              "cumple": c_a, "ratio": _r(delta[C10] / delta[C00]) if delta[C00] else None},
               "C11_vs_C01": {"delta_C11": delta[C11], "mitad_delta_C01": _r(0.5 * delta[C01]) if delta[C01] is not None else None,
                              "cumple": c_b, "ratio": _r(delta[C11] / delta[C01]) if delta[C01] else None}})
    P["P2"] = _gate(p2)

    # ---- P3 ----
    m = U["P3_margen"]
    conds = {
        "consultada_lit_C10_vs_C00": (rc[C10]["literal"], rc[C00]["literal"]),
        "consultada_lit_C11_vs_C01": (rc[C11]["literal"], rc[C01]["literal"]),
        "vista_lit_C10_vs_C00": (rv[C10]["literal"], rv[C00]["literal"]),
        "vista_lit_C11_vs_C01": (rv[C11]["literal"], rv[C01]["literal"]),
    }
    det3 = {k: {"bm25": a, "booleano": b, "cumple": (None if (a is None or b is None) else (a >= b - m - 1e-12))}
            for k, (a, b) in conds.items()}
    ev3 = n_pares >= nmin and all(d["cumple"] is not None for d in det3.values())
    p3 = _ver(all(d["cumple"] for d in det3.values()), ev3, "faltan valores" if not ev3 else None)
    p3.update({"margen": m, "condiciones": det3})
    P["P3"] = _gate(p3)

    # ---- P4 ----
    sub4 = {}
    # (i) E-B/entrante pooled ambas variantes
    ebe = {cid: tabla[cid]["por_sub_estrato"]["E-B/entrante::ambas"] for cid in ORDEN_CELDAS}
    n_ebe = ebe[C00].get("n_pares", 0)
    r_ebe = {cid: ebe[cid].get("recall_consultada_micro") for cid in ORDEN_CELDAS}
    ev4i = n_ebe >= nmin and all(r_ebe[c] is not None for c in ORDEN_CELDAS)
    c4i = ev4i and (r_ebe[C01] > r_ebe[C00]) and (r_ebe[C11] > r_ebe[C10])
    s = _ver(c4i, ev4i, f"E-B/entrante n_pares={n_ebe} < {nmin}" if not ev4i else None)
    s.update({"n_pares": n_ebe, "recall_c_micro_ambas": r_ebe,
              "por_variante": {v: {cid: tabla[cid]["por_sub_estrato"][f"E-B/entrante::{v}"].get("recall_consultada_micro")
                                   for cid in ORDEN_CELDAS} for v in VARIANTES},
              "C01_gt_C00": (r_ebe[C01] > r_ebe[C00]) if ev4i else None,
              "C11_gt_C10": (r_ebe[C11] > r_ebe[C10]) if ev4i else None})
    sub4["i_EB_entrante"] = s
    # (ii-a) tasa hit_tool_limit baja v1 -> v2 con el mismo retriever
    def _tasa_htl(cid):
        cs = [idx[cid][f"{sid}::{v}"] for sid in apareados for v in VARIANTES]
        return (sum(1 for c in cs if c["clases"]["hit_tool_limit"]) / len(cs)) if cs else None
    htl = {cid: _r(_tasa_htl(cid)) for cid in ORDEN_CELDAS}
    ev4a = n_pares >= nmin and all(htl[c] is not None for c in ORDEN_CELDAS)
    c4a = ev4a and htl[C01] < htl[C00] and htl[C11] < htl[C10]
    s = _ver(c4a, ev4a, "faltan valores" if not ev4a else None)
    s.update({"tasa_hit_tool_limit": htl, "C01_lt_C00": (htl[C01] < htl[C00]) if ev4a else None,
              "C11_lt_C10": (htl[C11] < htl[C10]) if ev4a else None})
    sub4["ii_a_hit_tool_limit_baja"] = s
    # (ii-b) clase K en C00: hit_tool_limit o n_brecha>0; fracción que mejora en C01 vs resto
    K, resto = [], []
    for sid in apareados:
        for v in VARIANTES:
            c0 = idx[C00][f"{sid}::{v}"]
            (K if (c0["clases"]["hit_tool_limit"] or c0["n_brecha"] > 0) else resto).append((sid, v))
    def _frac_mejora(units):
        if not units:
            return None, 0
        mej = 0
        for sid, v in units:
            a, b = idx[C01][f"{sid}::{v}"]["recall_consultada"], idx[C00][f"{sid}::{v}"]["recall_consultada"]
            if a is not None and b is not None and a > b:
                mej += 1
        return mej / len(units), mej
    fK, mK = _frac_mejora(K)
    fR, mR = _frac_mejora(resto)
    nK, nR = len({s for s, _ in K}), len({s for s, _ in resto})
    ev4b = nK >= nmin and nR >= nmin and fK is not None and fR is not None
    s = _ver(ev4b and fK > fR, ev4b, f"clase K n_pares={nK}, resto n_pares={nR}; mínimo {nmin}" if not ev4b else None)
    s.update({"K_definicion": OPERACIONALIZACIONES["P4_ii_b"], "K_n_unidades": len(K), "K_n_pares": nK,
              "K_mejoran_en_C01": mK, "K_fraccion": _r(fK), "resto_n_unidades": len(resto), "resto_n_pares": nR,
              "resto_mejoran_en_C01": mR, "resto_fraccion": _r(fR)})
    sub4["ii_b_clase_K_mejora_mas"] = s
    # (iii) efecto T < efecto R (anti-léxica micro consultada)
    ef_T = (rc[C01]["antilexica"] - rc[C00]["antilexica"]) if None not in (rc[C01]["antilexica"], rc[C00]["antilexica"]) else None
    ef_R = (rc[C10]["antilexica"] - rc[C00]["antilexica"]) if None not in (rc[C10]["antilexica"], rc[C00]["antilexica"]) else None
    ev4c = n_pares >= nmin and ef_T is not None and ef_R is not None
    s = _ver(ev4c and ef_T < ef_R, ev4c, "faltan valores" if not ev4c else None)
    s.update({"efecto_T_C01_menos_C00": _r(ef_T), "efecto_R_C10_menos_C00": _r(ef_R)})
    sub4["iii_efecto_T_menor_que_R"] = s
    p4 = {"veredicto": _combinar(sub4), "sub": sub4}
    P["P4"] = _gate(p4)

    # ---- P5 ----
    anti = {cid: rc[cid]["antilexica"] for cid in ORDEN_CELDAS}
    ev5 = n_pares >= nmin and all(anti[c] is not None for c in ORDEN_CELDAS)
    mejor = max(anti, key=lambda c: anti[c]) if ev5 else None
    c11_estricta = ev5 and all(anti[C11] > anti[c] for c in ORDEN_CELDAS if c != C11)
    inter = ((anti[C11] - anti[C00]) - ((anti[C10] - anti[C00]) + (anti[C01] - anti[C00]))) if ev5 else None
    adit = (abs(inter) <= U["P5_aditividad"] + 1e-12) if ev5 else None
    s = _ver(bool(c11_estricta and adit), ev5, "faltan valores" if not ev5 else None)
    s.update({"recall_c_anti_micro": anti, "mejor_celda": mejor, "C11_estrictamente_maxima": c11_estricta if ev5 else None,
              "interaccion": _r(inter), "umbral_aditividad": U["P5_aditividad"], "aditiva": adit,
              "empates_con_C11": [c for c in ORDEN_CELDAS if ev5 and c != C11 and anti[c] == anti[C11]]})
    P["P5"] = _gate(s)

    # ---- P6 ----
    pares_h = [sid for sid in apareados if huerfanos.get(sid)]
    n_h = len(pares_h)
    def _frac_h(cids, campo):
        num = den = 0
        for cid in cids:
            for sid in pares_h:
                for v in VARIANTES:
                    for h in idx[cid][f"{sid}::{v}"].get("huerfanos_p6", []):
                        den += 1
                        num += 1 if h[campo] else 0
        return (_r(num / den) if den else None), num, den
    fv = {cid: _frac_h([cid], "visto") for cid in ORDEN_CELDAS}
    fc = {cid: _frac_h([cid], "consultado") for cid in ORDEN_CELDAS}
    fc_v1, fc_v2 = _frac_h([C00, C10], "consultado"), _frac_h([C01, C11], "consultado")
    ev6 = n_h >= nmin and fv[C10][0] is not None and fv[C00][0] is not None and fc_v1[0] is not None and fc_v2[0] is not None
    c6i = ev6 and (fv[C10][0] <= fv[C00][0] + U["P6_margen_vista"] + 1e-12)
    c6ii = ev6 and (fc_v2[0] > fc_v1[0])
    # tasa de paginación en celdas v2 (llamadas ver_vecinos con pagina>1 / llamadas ver_vecinos)
    def _pag(cid):
        cs = list(idx[cid].values())
        n_vv = sum(c["clases"]["llamadas_por_tool"].get("ver_vecinos", 0) for c in cs)
        n_p = sum(c["clases"]["n_ver_vecinos_pagina_gt1"] for c in cs)
        return {"pagina_gt1": n_p, "ver_vecinos": n_vv, "tasa": _r(n_p / n_vv) if n_vv else None}
    s = _ver(bool(c6i and c6ii), ev6, f"pares con huérfano n={n_h} < {nmin} o faltan valores" if not ev6 else None)
    s.update({"n_pares_con_huerfano": n_h, "pares": pares_h,
              "i_vista": {"fraccion_vista": {cid: fv[cid][0] for cid in ORDEN_CELDAS},
                          "num_den": {cid: (fv[cid][1], fv[cid][2]) for cid in ORDEN_CELDAS},
                          "margen": U["P6_margen_vista"], "cumple_C10_le_C00_mas_margen": c6i if ev6 else None},
              "ii_consultada": {"fraccion_consultada": {cid: fc[cid][0] for cid in ORDEN_CELDAS},
                                "num_den": {cid: (fc[cid][1], fc[cid][2]) for cid in ORDEN_CELDAS},
                                "v1_pooled": fc_v1[0], "v2_pooled": fc_v2[0], "cumple_v2_gt_v1": c6ii if ev6 else None,
                                "C01_gt_C00": (fc[C01][0] > fc[C00][0]) if ev6 else None,
                                "C11_gt_C10": (fc[C11][0] > fc[C10][0]) if ev6 else None},
              "tasa_paginacion_v2": {cid: _pag(cid) for cid in (C01, C11)},
              "sub": {"i": _ver(c6i, ev6), "ii": _ver(c6ii, ev6)}})
    P["P6"] = _gate(s)

    P["resumen"] = {k: P[k]["veredicto"] for k in ("P1", "P2", "P3", "P4", "P5", "P6")}
    P["gate_P1"] = gate
    P["umbrales"] = dict(U)
    return P


# --------------------------------------------------------------------------- #
# Lecturas por cohorte (informativas; separadas, jamás promediadas)            #
# --------------------------------------------------------------------------- #
def lecturas_por_cohorte(tabla: dict, umbrales: dict = UMBRALES) -> dict:
    out = {}
    for g in ("cohorte_nucleo_limpio_EE", "cohorte_dirigida_EA_ED"):
        d = {}
        n_p = tabla[C00][g]["literal"].get("n_pares", 0)
        for cid in ORDEN_CELDAS:
            t = tabla[cid][g]
            d[cid] = {"n_pares": t["literal"].get("n_pares"),
                      "recall_c_micro": {v: t[v].get("recall_consultada_micro") for v in VARIANTES},
                      "recall_v_micro": {v: t[v].get("recall_vista_micro") for v in VARIANTES},
                      "delta_c_micro": t["brecha_literal_menos_antilexica"]["recall_consultada_micro"]}
        d["evaluable_n"] = n_p >= umbrales["n_min_pares_clase"]
        out[g] = d
    return out


# --------------------------------------------------------------------------- #
# Orquestación                                                                 #
# --------------------------------------------------------------------------- #
def analizar(replays: dict[str, dict], huerfanos: dict, umbrales: dict = UMBRALES,
             semilla: str = SEMILLA_BOOTSTRAP, n_boot: int = N_BOOTSTRAP) -> dict:
    idx = _indexar(replays)
    apareados, detalle_ap = pares_apareados(idx)
    tabla = tabla_central(idx, apareados)
    difs = diferencias_apareadas(idx, apareados, semilla, n_boot)
    preds = evaluar_predicciones(tabla, idx, apareados, huerfanos, umbrales)
    tasas = tasas_y_latencias(idx, apareados, replays)
    return {
        "unidad": "U-A1.4",
        "operacionalizaciones": OPERACIONALIZACIONES,
        "n_pares_apareados": len(apareados), "pares_apareados": apareados, "apareamiento": detalle_ap,
        "n_trazas_por_celda": {cid: len(idx[cid]) for cid in ORDEN_CELDAS},
        "replay": {cid: {"replay_ok_todos": replays[cid]["replay_ok_todos"],
                         "replay_fuerte_ok_todos": replays[cid]["replay_fuerte_ok_todos"],
                         "cruce_inmemory_ok_todos": replays[cid].get("cruce_inmemory_ok_todos"),
                         "n_divergencias": replays[cid].get("n_divergencias")} for cid in ORDEN_CELDAS},
        "tabla_central": tabla,
        "diferencias_apareadas": difs,
        "predicciones": preds,
        "lecturas_por_cohorte": lecturas_por_cohorte(tabla, umbrales),
        "tasas_y_latencias": tasas,
    }


# --------------------------------------------------------------------------- #
# Render markdown                                                              #
# --------------------------------------------------------------------------- #
def _f(x, nd=4):
    return "—" if x is None else (f"{x:.{nd}f}" if isinstance(x, float) else str(x))


def render_md(an: dict) -> str:
    L = []
    L.append("# Análisis de la ablación de retrieval — U-A1.4 (generado por analisis_ablacion.py)\n")
    L.append(f"Pares apareados (presentes en las 4 celdas): **{an['n_pares_apareados']}**; trazas por celda: "
             f"{an['n_trazas_por_celda']}; faltantes por celda: {an['apareamiento']['faltantes_por_celda']}.\n")
    L.append("Replay: " + "; ".join(f"{c}: estándar={v['replay_ok_todos']} fuerte={v['replay_fuerte_ok_todos']}"
                                     + (f" cruce_inmemory={v['cruce_inmemory_ok_todos']}" if v['cruce_inmemory_ok_todos'] is not None else "")
                                     for c, v in an["replay"].items()) + "\n")
    L.append("## Tabla central (grupo `todos`, pares apareados)\n")
    L.append("| celda | variante | n_casos | n_anclas | vistas | consultadas | brecha v-s-c | recall vista micro | recall vista macro | recall consultada micro | recall consultada macro |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|")
    for cid in ORDEN_CELDAS:
        for v in VARIANTES:
            t = an["tabla_central"][cid]["todos"][v]
            L.append(f"| {cid} | {v} | {t.get('n_casos')} | {t.get('n_anclas')} | {t.get('n_vistas')} | {t.get('n_consultadas')} | "
                     f"{t.get('n_brecha_vista_sin_consultar')} | {_f(t.get('recall_vista_micro'))} | {_f(t.get('recall_vista_macro'))} | "
                     f"{_f(t.get('recall_consultada_micro'))} | {_f(t.get('recall_consultada_macro'))} |")
    L.append("\nBrecha Δ = literal − anti-léxica por celda (grupo `todos`):\n")
    L.append("| celda | Δ vista micro | Δ vista macro | Δ consultada micro | Δ consultada macro |")
    L.append("|---|---|---|---|---|")
    for cid in ORDEN_CELDAS:
        b = an["tabla_central"][cid]["todos"]["brecha_literal_menos_antilexica"]
        L.append(f"| {cid} | {_f(b['recall_vista_micro'])} | {_f(b['recall_vista_macro'])} | {_f(b['recall_consultada_micro'])} | {_f(b['recall_consultada_macro'])} |")
    for g, titulo in (("cohorte_nucleo_limpio_EE", "Cohorte núcleo limpio (E-E)"), ("cohorte_dirigida_EA_ED", "Cohorte dirigida (E-A..E-D)")):
        L.append(f"\n## {titulo} — separada, no promediada con la otra\n")
        L.append("| celda | variante | n_casos | n_anclas | vistas | consultadas | brecha v-s-c | recall vista micro | recall consultada micro | recall consultada macro |")
        L.append("|---|---|---|---|---|---|---|---|---|---|")
        for cid in ORDEN_CELDAS:
            for v in VARIANTES:
                t = an["tabla_central"][cid][g][v]
                L.append(f"| {cid} | {v} | {t.get('n_casos')} | {t.get('n_anclas')} | {t.get('n_vistas')} | {t.get('n_consultadas')} | "
                         f"{t.get('n_brecha_vista_sin_consultar')} | {_f(t.get('recall_vista_micro'))} | {_f(t.get('recall_consultada_micro'))} | {_f(t.get('recall_consultada_macro'))} |")
    L.append("\n## Por estrato × variante (recall micro; macro en el JSON)\n")
    L.append("| celda | estrato | variante | n_casos | n_anclas | vistas | consultadas | brecha | recall vista micro | recall consultada micro |")
    L.append("|---|---|---|---|---|---|---|---|---|---|")
    for cid in ORDEN_CELDAS:
        for e in ESTRATOS:
            for v in VARIANTES:
                t = an["tabla_central"][cid]["por_estrato_variante"][f"{e}::{v}"]
                L.append(f"| {cid} | {e} | {v} | {t.get('n_casos')} | {t.get('n_anclas')} | {t.get('n_vistas')} | {t.get('n_consultadas')} | "
                         f"{t.get('n_brecha_vista_sin_consultar')} | {_f(t.get('recall_vista_micro'))} | {_f(t.get('recall_consultada_micro'))} |")
    L.append("\n## Diferencias apareadas (punto e IC bootstrap 95 %, "
             f"semilla `{an['diferencias_apareadas'].get('semilla')}`, {an['diferencias_apareadas'].get('n_remuestreos')} remuestreos, n_pares={an['diferencias_apareadas'].get('n_pares')})\n")
    L.append("| estadístico | punto | IC95 inf | IC95 sup |")
    L.append("|---|---|---|---|")
    for k, v in an["diferencias_apareadas"].get("estadisticos", {}).items():
        L.append(f"| {k} | {_f(v['punto'])} | {_f(v['ic95_inf'])} | {_f(v['ic95_sup'])} |")
    P = an["predicciones"]
    L.append("\n## Predicciones P1–P6 (evaluación mecánica, umbrales sellados; regla de lectura textual)\n")
    L.append("| predicción | veredicto | detalle |")
    L.append("|---|---|---|")
    L.append(f"| P1 (gate Δ_c(C00) ≥ {P['P1']['umbral']}) | **{P['P1']['veredicto']}** | Δ_c(C00) = {_f(P['P1']['delta_c_C00'])} (lit {_f(P['P1']['recall_c_lit_C00'])} → anti {_f(P['P1']['recall_c_anti_C00'])}); n_pares {P['P1']['n_pares']} |")
    p2 = P["P2"]
    L.append(f"| P2 (Δ_c(C10) ≤ ½Δ_c(C00) y Δ_c(C11) ≤ ½Δ_c(C01)) | **{p2['veredicto']}** | Δ_c = {p2['delta_c']}; C10/C00 ratio {_f(p2['C10_vs_C00']['ratio'])} ({p2['C10_vs_C00']['cumple']}); C11/C01 ratio {_f(p2['C11_vs_C01']['ratio'])} ({p2['C11_vs_C01']['cumple']}){' — ' + str(p2.get('motivo')) if p2.get('motivo') else ''} |")
    p3 = P["P3"]
    L.append(f"| P3 (no regresión literal, margen {p3['margen']}) | **{p3['veredicto']}** | " +
             "; ".join(f"{k}: {_f(d['bm25'])} vs {_f(d['booleano'])} → {d['cumple']}" for k, d in p3["condiciones"].items()) +
             (' — ' + str(p3.get('motivo')) if p3.get('motivo') else '') + " |")
    p4 = P["P4"]
    L.append(f"| P4 (tools v2, direccional) | **{p4['veredicto']}** | " +
             "; ".join(f"{k}: {s['veredicto']}" for k, s in p4["sub"].items()) +
             (' — ' + str(p4.get('motivo')) if p4.get('motivo') else '') + " |")
    p5 = P["P5"]
    L.append(f"| P5 (C11 mejor y aditiva ≤ {p5['umbral_aditividad']}) | **{p5['veredicto']}** | anti micro {p5['recall_c_anti_micro']}; mejor {p5['mejor_celda']}; interacción {_f(p5['interaccion'])}{' — ' + str(p5.get('motivo')) if p5.get('motivo') else ''} |")
    p6 = P["P6"]
    L.append(f"| P6 (huérfanos de label, {p6['n_pares_con_huerfano']} pares) | **{p6['veredicto']}** | vista {p6['i_vista']['fraccion_vista']} (C10 ≤ C00+{p6['i_vista']['margen']}: {p6['i_vista']['cumple_C10_le_C00_mas_margen']}); consultada v1 {_f(p6['ii_consultada']['v1_pooled'])} vs v2 {_f(p6['ii_consultada']['v2_pooled'])} ({p6['ii_consultada']['cumple_v2_gt_v1']}); paginación v2 {p6['tasa_paginacion_v2']}{' — ' + str(p6.get('motivo')) if p6.get('motivo') else ''} |")
    L.append("\nDetalle P4:\n")
    for k, s in p4["sub"].items():
        L.append(f"- `{k}`: **{s['veredicto']}** — " + json.dumps({kk: vv for kk, vv in s.items() if kk not in ('veredicto', 'K_definicion')}, ensure_ascii=False))
    L.append("\n## Tasas y latencias por celda\n")
    L.append("| celda | n_trazas | hit_tool_limit (tasa) | abstención (tasa) | parse_ok (tasa) | errores técnicos | tool calls media | latencia p50 s | latencia p95 s | costo USD (CLI) | replay OK |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|")
    for cid in ORDEN_CELDAS:
        t = an["tasas_y_latencias"][cid]["todas"]
        rp = an["tasas_y_latencias"][cid]
        L.append(f"| {cid} | {t.get('n_trazas')} | {t.get('hit_tool_limit')} ({_f(t.get('tasa_hit_tool_limit'))}) | {t.get('abstenciones')} ({_f(t.get('tasa_abstencion'))}) | "
                 f"{t.get('parse_ok')} ({_f(t.get('tasa_parse_ok'))}) | {len(t.get('errores_tecnicos', []))} | {_f(t.get('tool_calls_media'), 2)} | {_f(t.get('latencia_s_p50'), 3)} | {_f(t.get('latencia_s_p95'), 3)} | "
                 f"{_f(t.get('costo_usd_cli'))} | {rp['replay_ok_todos'] and rp['replay_fuerte_ok_todos']} |")
    L.append("\nLatencia por tool (p50 / p95, s) y uso de paginación/filtro en ver_vecinos:\n")
    for cid in ORDEN_CELDAS:
        r = an["tasas_y_latencias"][cid]
        L.append(f"- {cid}: " + "; ".join(f"{t} n={d['n']} p50={_f(d['p50'])} p95={_f(d['p95'])}" for t, d in r["latencia_por_tool_s"].items())
                 + f"; llamadas {r['llamadas_por_tool']}; pagina>1 {r['ver_vecinos_pagina_gt1']}; con relación {r['ver_vecinos_con_relacion']}")
    L.append("\n## Operacionalizaciones declaradas\n")
    for k, v in an["operacionalizaciones"].items():
        L.append(f"- **{k}**: {v}")
    return "\n".join(L) + "\n"


def main() -> int:
    replays = cargar_replays()
    an = analizar(replays, huerfanos_p6())
    RESULTADOS_DIR.mkdir(parents=True, exist_ok=True)
    pj = RESULTADOS_DIR / "analisis_ablacion.json"
    pj.write_text(json.dumps(an, ensure_ascii=False, indent=2), encoding="utf-8")
    pm = RESULTADOS_DIR / "reporte_analisis.md"
    pm.write_text(render_md(an), encoding="utf-8")
    print(f"análisis → {rel_repo(pj)} / {rel_repo(pm)}")
    print("veredictos:", an["predicciones"]["resumen"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
