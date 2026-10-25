#!/usr/bin/env python3
"""analizar_a2_2.py — El análisis de A2.2 (pre-registro FIRMADO, a78ead7b, §5), escrito y probado sobre veredictos sintéticos
antes de correr. USD 0: lee las salidas del juez, la población, las metas del agente, EV2 (solo sus anclas, por código) y la lista
de la cola; no llama a ningún modelo.

  · el veredicto final de cada pregunta en cada brazo: el de N = 1 o, si el par fue a N = 3, el agregado de sus tres re-corridas
    (§4). Una `requiere_adjudicacion` toma el veredicto que la autora adjudica al final (A-D8; --adjudicaciones, por id opaco).
    Lo que queda sin veredicto final (una sesión incompleta por R3, una respuesta sin juicio, una adjudicación pendiente) sale de
    la métrica, se lista, y la sensibilidad lo cuenta como no cumplido (§3, R5 (1); registro, §50, punto 6);
  · la métrica de una corrida: 1 si el veredicto final es «correcto» y 0 si no (A-D9, confirmada);
  · d_q = x(grafo) − x(fragmentos) por pregunta, y la prueba exacta por permutación de signos sobre d_q, de dos colas (con d_q en
    {−1, 0, 1} es la binomial exacta sobre los pares discordantes), con Holm sobre las dos comparaciones a α = 0,05: la primera a
    0,025 (§5). «El grafo supera» a una configuración si su comparación se rechaza y la diferencia favorece al grafo; la afirmación
    general, solo si supera a las dos (plan, `:339`);
  · la cifra sin la cola (A-D11, (a)): sale una pregunta si alguna de sus anclas cae en la cola. Un ancla «to:punto» de EV2 se
    resuelve sobre la E0 r2b de desarrollo como en el bake-off (`bakeoff_embeddings/code/mapeo_gold_chunk.py`, `resolver`): la
    unidad igual al punto; si no hay, las que descienden de él. Cae en la cola si alguna de sus unidades está en la lista (un id de parte, «::parteK», cuenta como su unidad);
  · las tasas de pares discordantes de cada comparación (Q5) y `c_agente` (Q6): el costo R9 medio por sesión de N = 1 de cada brazo;
  · las predicciones del §5, con lo observado y si el sentido coincide (la 6, la asimetría, es del diagnóstico posterior);
  · lo operativo de R5 por brazo: las sesiones que llegan a 30 llamadas en el log R1, las que pasan de 30 y las cortadas, con su
    fracción y su intervalo de Wilson al 95 %.

No imprime ningún veredicto ni resultado: escribe analisis_a2_2.json y dice dónde.
Uso: .venv/bin/python -B data/experiment/banco_mcp/a2_2/analizar_a2_2.py [--adjudicaciones <json>]
"""
from __future__ import annotations

import argparse
import json
import math
import statistics as st
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
if str(AQUI) not in sys.path:
    sys.path.insert(0, str(AQUI))
import comun_a2_2 as K                 # noqa: E402
import poblacion_a2_2 as PB            # noqa: E402

PENDIENTE = "requiere_adjudicacion"
Z95 = 1.959963984540054
ALFA = 0.05


# --------------------------------------------------------------------------- #
# Estadística                                                                  #
# --------------------------------------------------------------------------- #
def p_signos_exacta(d: list[int]) -> float:
    """Prueba exacta por permutación de signos, de dos colas, sobre d_q en {−1, 0, 1}: con nd pares discordantes y T = Σ d_q,
    p = P(|T*| ≥ |T|) con cada signo al azar, = Σ_{k : |2k − nd| ≥ |T|} C(nd, k) / 2^nd."""
    nd = sum(1 for x in d if x != 0)
    t = abs(sum(d))
    if nd == 0:
        return 1.0
    return min(1.0, sum(math.comb(nd, k) for k in range(nd + 1) if abs(2 * k - nd) >= t) / 2 ** nd)


def holm(ps: dict[str, float], alfa: float = ALFA) -> dict[str, dict]:
    """Holm sobre las comparaciones: la de p menor a alfa/m, la siguiente a alfa/(m − 1); se detiene en la primera que no rechaza."""
    orden = sorted(ps, key=lambda k: (ps[k], k))
    out, sigue = {}, True
    for i, k in enumerate(orden):
        umbral = alfa / (len(orden) - i)
        rechaza = sigue and ps[k] <= umbral
        sigue = rechaza
        out[k] = {"p": ps[k], "umbral_holm": umbral, "posicion": i + 1, "rechaza": rechaza}
    return out


def wilson(k: int, n: int, z: float = Z95) -> list | None:
    if n == 0:
        return None
    p = k / n
    c = (p + z * z / (2 * n)) / (1 + z * z / n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return [round(max(0.0, c - h), 6), round(min(1.0, c + h), 6)]


# --------------------------------------------------------------------------- #
# La cola (A-D11)                                                              #
# --------------------------------------------------------------------------- #
def cargar_e0(e0_dir: Path = K.E0_DIR) -> dict[str, list[dict]]:
    out = {}
    for to in K.E0_TOS:
        out[to] = json.loads((e0_dir / f"chunks_{to}.json").read_text(encoding="utf-8"))
    return out


def resolver(ancla: str, e0: dict[str, list[dict]]) -> tuple[list[str], str]:
    """(ids de unidades, vía) de un ancla «to:punto»: «a», la unidad igual al punto; «b», las que descienden de él; «ninguna»."""
    to, _, punto = ancla.partition(":")
    chunks = e0.get(to, [])
    exacto = sorted(c["id"] for c in chunks if c["unidad"] == punto)
    if exacto:
        return exacto, "a"
    desc = sorted(c["id"] for c in chunks if c["unidad"].startswith(punto + "."))
    if desc:
        return desc, "b"
    return [], "ninguna"


def unidad_de(i: str) -> str:
    """El id de la unidad de E0 de un id de la cola: sin el sufijo «::parteK» de la partición de la extracción (la cola trae
    `cap::4.2.1.2::parte1`, una parte de la unidad `cap::4.2.1.2` de la E0)."""
    return i.split("::parte", 1)[0]


def preguntas_con_cola(preguntas: dict, cola_ids: set[str], e0: dict) -> dict:
    """{qid: True si alguna de sus anclas cae en la cola} y las cuentas de la resolución. Una parte de una unidad en la cola pone
    a la unidad en la cola."""
    cola_ids = {unidad_de(i) for i in cola_ids}
    out, vias = {}, {"a": 0, "b": 0, "ninguna": 0}
    for q, v in preguntas.items():
        alguna = False
        for an in v["anclas"]:
            ids, via = resolver(an, e0)
            vias[via] += 1
            alguna = alguna or bool(set(ids) & cola_ids)
        out[q] = alguna
    return {"por_pregunta": out, "vias": vias}


# --------------------------------------------------------------------------- #
# Veredictos finales                                                           #
# --------------------------------------------------------------------------- #
def aplicar_adjudicaciones(verd: dict, adjud: dict[str, str]) -> dict:
    """Reemplaza el veredicto de una respuesta `requiere_adjudicacion` por el adjudicado (por id opaco)."""
    out = {}
    for k, a in verd.items():
        v = a["veredicto_pregunta"]
        if v == PENDIENTE and a["id_opaco"] in adjud:
            v = adjud[a["id_opaco"]]
        out[k] = dict(a, veredicto_pregunta=v)
    return out


def finales(preguntas_ids: list[str], v_n1: dict, poblacion: dict, v_rc: dict) -> dict:
    """{(qid, brazo): {"final", "origen"}}; "final" None si no hay veredicto final."""
    en_pob = {(p["qid"], p["brazo"]) for p in poblacion["pares"]}
    rc = PB.agregar_recorridas(poblacion, v_rc)
    rc_fin = {(p["qid"], p["brazo"]): p["final"] for p in rc["pares"]}
    out = {}
    for q in preguntas_ids:
        for b in K.BRAZOS:
            if (q, b) in en_pob:
                f = rc_fin.get((q, b))
                out[(q, b)] = {"final": None if f in (None, PENDIENTE) else f,
                               "origen": "re-corridas" if f not in (None, PENDIENTE) else
                               ("re-corridas pendientes de adjudicación" if f == PENDIENTE else "re-corridas incompletas")}
            else:
                a = v_n1.get((q, b, 1))
                f = a["veredicto_pregunta"] if a else None
                out[(q, b)] = {"final": None if f in (None, PENDIENTE) else f,
                               "origen": "N = 1" if f not in (None, PENDIENTE) else
                               ("N = 1 pendiente de adjudicación" if f == PENDIENTE else "N = 1 sin veredicto")}
    return out


def comparar(fin: dict, ids: list[str], sensibilidad: bool = False) -> dict:
    """Las dos comparaciones, con Holm. Con sensibilidad, lo que no tiene veredicto final cuenta como 0."""
    x = {k: (1 if v["final"] == "correcto" else 0) if v["final"] is not None else (0 if sensibilidad else None)
         for k, v in fin.items()}
    comps, ps = {}, {}
    for fr in K.FRAGMENTOS:
        pares = [q for q in ids if x[(q, K.BRAZO_GRAFO)] is not None and x[(q, fr)] is not None]
        d = [x[(q, K.BRAZO_GRAFO)] - x[(q, fr)] for q in pares]
        n10, n01 = d.count(1), d.count(-1)
        n = len(pares)
        ps[fr] = p_signos_exacta(d)
        comps[fr] = {"n_preguntas": n, "excluidas": len(ids) - n, "grafo_correctas": sum(x[(q, K.BRAZO_GRAFO)] for q in pares),
                     "fragmentos_correctas": sum(x[(q, fr)] for q in pares), "n10_grafo_si_fragmentos_no": n10,
                     "n01_grafo_no_fragmentos_si": n01, "T_suma_d": n10 - n01, "p_dos_colas": ps[fr],
                     "tasa_discordantes": round((n10 + n01) / n, 6) if n else None,
                     "tasa_n10": round(n10 / n, 6) if n else None, "tasa_n01": round(n01 / n, 6) if n else None,
                     "diferencia_de_proporciones": round((n10 - n01) / n, 6) if n else None}
    h = holm(ps)
    for fr in K.FRAGMENTOS:
        comps[fr]["holm"] = h[fr]
        comps[fr]["grafo_supera"] = h[fr]["rechaza"] and comps[fr]["T_suma_d"] > 0
        comps[fr]["fragmentos_superan"] = h[fr]["rechaza"] and comps[fr]["T_suma_d"] < 0
    return {"comparaciones": comps, "afirmacion_general_el_grafo_supera_a_los_fragmentos":
            all(comps[fr]["grafo_supera"] for fr in K.FRAGMENTOS)}


# --------------------------------------------------------------------------- #
# Lo del agente: costo, latencia y R5                                          #
# --------------------------------------------------------------------------- #
def metas(dirs: list[Path]) -> list[dict]:
    return [json.loads(p.read_text(encoding="utf-8")) for d in dirs if d.exists() for p in sorted(d.glob("meta_*.json"))]


def r5_por_brazo(ms: list[dict]) -> dict:
    out = {}
    for b in K.BRAZOS:
        xs = [m for m in ms if m["brazo"] == b]
        ll = [(m.get("hb2") or {}).get("n_llamadas_log_r1") or 0 for m in xs]
        al = sum(1 for n in ll if n >= 30)
        pasa = sum(1 for n in ll if n > 30)
        cort = sum(1 for m in xs if (m.get("hb2") or {}).get("subtype") != "success")
        n = len(xs)
        out[b] = {"n_sesiones": n, "al_tope_30_o_mas": al, "fraccion_al_tope": round(al / n, 6) if n else None,
                  "wilson_al_tope": wilson(al, n), "pasan_de_30": pasa, "wilson_pasan_de_30": wilson(pasa, n),
                  "cortadas": cort, "wilson_cortadas": wilson(cort, n), "llamadas_max": max(ll) if ll else None,
                  "llamadas_media": round(st.mean(ll), 4) if ll else None}
    return out


def costo_y_latencia(ms_n1: list[dict], ms_todas: list[dict], poblacion: dict, n_preg: int) -> dict:
    out = {}
    for b in K.BRAZOS:
        x1 = [m for m in ms_n1 if m["brazo"] == b]
        xt = [m for m in ms_todas if m["brazo"] == b]
        c1 = [m["tokens_R9"]["costo_recomputado"]["total_usd"] or 0.0 for m in x1]
        lat = [m.get("duracion_s") or 0.0 for m in x1]
        P = sum(1 for p in poblacion["pares"] if p["brazo"] == b)
        out[b] = {"c_agente_media_n1": round(st.mean(c1), 6) if c1 else None, "n_sesiones_n1": len(c1),
                  "costo_total_agente": round(sum(m["tokens_R9"]["costo_recomputado"]["total_usd"] or 0.0 for m in xt), 6),
                  "latencia_media_s_n1": round(st.mean(lat), 3) if lat else None,
                  "latencia_mediana_s_n1": round(st.median(lat), 3) if lat else None,
                  "P": P, "f_N3": round(P / n_preg, 6) if n_preg else None}
    return out


def predicciones(v_n1: dict, fin: dict, cyl: dict) -> dict:
    """Las predicciones del §5 con lo observado. Criterios cubiertos y abstenciones, sobre las respuestas de N = 1 juzgadas;
    incorrectos, sobre el veredicto final; latencia y costo, sobre las sesiones de N = 1."""
    obs = {}
    for b in K.BRAZOS:
        ags = [a for (q, bb, r), a in v_n1.items() if bb == b and r == 1]
        tot = sum(a["n_criterios"] for a in ags)
        cum = sum(sum(1 for m in a["modales"] if m == "cumplido") for a in ags)
        obs[b] = {"criterios_cubiertos": round(cum / tot, 6) if tot else None, "criterios_cumplidos": cum, "criterios": tot,
                  "incorrectos_final": sum(1 for (q, bb), v in fin.items() if bb == b and v["final"] == "incorrecto"),
                  "abstenciones_n1": sum(1 for a in ags if a["clasificacion_respuesta_modal"] == "abstencion"),
                  "latencia_media_s_n1": cyl[b]["latencia_media_s_n1"], "c_agente_media_n1": cyl[b]["c_agente_media_n1"]}
    g = obs[K.BRAZO_GRAFO]

    def sentido(f):
        try:
            return bool(f())
        except TypeError:
            return None

    pr = {
        "1_criterios_cubiertos": {"esperado": "cada configuración de fragmentos ≥ el grafo, y BM25 ≥ el denso",
                                  "coincide": sentido(lambda: all(obs[f]["criterios_cubiertos"] >= g["criterios_cubiertos"]
                                                                  for f in K.FRAGMENTOS)
                                                      and obs["fragmentos_bm25"]["criterios_cubiertos"]
                                                      >= obs["fragmentos_denso"]["criterios_cubiertos"])},
        "2_incorrectos": {"esperado": "el grafo ≥ cada configuración de fragmentos",
                          "coincide": sentido(lambda: all(g["incorrectos_final"] >= obs[f]["incorrectos_final"]
                                                          for f in K.FRAGMENTOS))},
        "3_abstenciones": {"esperado": "el grafo ≥ cada configuración de fragmentos",
                           "coincide": sentido(lambda: all(g["abstenciones_n1"] >= obs[f]["abstenciones_n1"] for f in K.FRAGMENTOS))},
        "4_latencia": {"esperado": "el grafo > cada configuración de fragmentos",
                       "coincide": sentido(lambda: all(g["latencia_media_s_n1"] > obs[f]["latencia_media_s_n1"] for f in K.FRAGMENTOS))},
        "5_costo_c_agente": {"esperado": "el grafo > cada configuración de fragmentos",
                             "coincide": sentido(lambda: all(g["c_agente_media_n1"] > obs[f]["c_agente_media_n1"] for f in K.FRAGMENTOS))},
        "6_asimetria": {"esperado": ("la ventaja de los fragmentos en criterios de cita literal; la del grafo en remisiones o "
                                     "relaciones entre unidades"),
                        "coincide": None, "nota": "cómo se separan esas preguntas es del diagnóstico posterior (§5 y §6)"},
    }
    return {"observado": obs, "predicciones": pr}


# --------------------------------------------------------------------------- #
def analizar(*, preguntas: dict, juez_dir: Path, poblacion: dict, dirs_agente: dict, cola_ids: set[str], e0: dict,
             adjudicaciones: dict[str, str]) -> dict:
    ids = sorted(preguntas)
    v_n1 = aplicar_adjudicaciones(PB.veredictos_por_par(juez_dir, "n1"), adjudicaciones)
    rc_dir = juez_dir / "recorridas"
    v_rc = aplicar_adjudicaciones(PB.veredictos_por_par(juez_dir, "recorridas"), adjudicaciones) \
        if (rc_dir / "agregados_recorridas_ciego.json").exists() else {}
    fin = finales(ids, v_n1, poblacion, v_rc)
    cola = preguntas_con_cola(preguntas, cola_ids, e0)
    sin_cola = [q for q in ids if not cola["por_pregunta"][q]]
    ms_n1 = metas([dirs_agente["n1"]])
    ms_ev2 = ms_n1 + metas([dirs_agente["recorridas"]])
    cyl = costo_y_latencia(ms_n1, ms_ev2, poblacion, len(ids))
    sin_final = sorted([{"qid": q, "brazo": b, "origen": v["origen"]} for (q, b), v in fin.items() if v["final"] is None],
                       key=lambda x: (x["brazo"], x["qid"]))
    return {"que": "el análisis de A2.2 (pre-registro, §5)", "n_preguntas": len(ids),
            "finales": {f"{q}|{b}": v for (q, b), v in sorted(fin.items())},
            "sin_veredicto_final": sin_final, "n_sin_veredicto_final": len(sin_final),
            "principal": comparar(fin, ids),
            "principal_sensibilidad_sin_final_como_0": comparar(fin, ids, sensibilidad=True),
            "sin_la_cola": {"n_preguntas": len(sin_cola), "n_fuera_por_la_cola": len(ids) - len(sin_cola),
                            "resolucion_de_anclas": cola["vias"], **comparar(fin, sin_cola)},
            "c_agente_y_latencia": cyl, **predicciones(v_n1, fin, cyl), "r5_por_brazo": r5_por_brazo(ms_ev2),
            "no_comparabilidad_con_EV2": "principio 8 (A2.1, :147): otro agente, otro grafo y otro prompt"}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--preguntas", type=Path, default=K.EV2_PATH)
    ap.add_argument("--sha-preguntas", default=K.EV2_SHA256)
    ap.add_argument("--real", action=argparse.BooleanOptionalAction, default=True)
    ap.add_argument("--juez-dir", type=Path, default=K.JUEZ_DIR)
    ap.add_argument("--poblacion", type=Path, default=K.POBLACION)
    ap.add_argument("--resultados", type=Path, default=K.RESULTADOS)
    ap.add_argument("--cola", type=Path, default=K.COLA)
    ap.add_argument("--e0", type=Path, default=K.E0_DIR)
    ap.add_argument("--adjudicaciones", type=Path, default=None, help="JSON {id_opaco: veredicto} de la autora (A-D8)")
    ap.add_argument("--salida", type=Path, default=K.AQUI / "analisis" / "analisis_a2_2.json")
    a = ap.parse_args(argv)
    preguntas = K.cargar_preguntas(a.preguntas, a.sha_preguntas, real=a.real)
    adj = json.loads(a.adjudicaciones.read_text(encoding="utf-8")) if a.adjudicaciones else {}
    cola = set(json.loads(a.cola.read_text(encoding="utf-8"))["ids"])
    res = analizar(preguntas=preguntas, juez_dir=a.juez_dir, poblacion=json.loads(a.poblacion.read_text(encoding="utf-8")),
                   dirs_agente={"n1": a.resultados / "n1", "recorridas": a.resultados / "recorridas"},
                   cola_ids=cola, e0=cargar_e0(a.e0), adjudicaciones=adj)
    a.salida.parent.mkdir(parents=True, exist_ok=True)
    a.salida.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"análisis escrito ({res['n_preguntas']} preguntas; {res['n_sin_veredicto_final']} pares sin veredicto final) ->",
          K.rel_repo(a.salida))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
