"""
muestreo_v3.py — FASE A ($0): muestreo en seco del material nuevo de la ablación
con el pipeline de pares sintéticos IMPORTADO sin editar
(`data/experiment/exploracion/sinteticas/`, commits a611ed2 / 5ceb816).

Único cambio respecto de la corrida que alimentó EV2: la SEMILLA
(`sinteticas-faseA-v3`). Mismo grafo (KG-Refinado, sha 26fac8b4 verificado por
`comun.load_kg_raw` antes de muestrear), mismo mapa de quemado (5 sets), mismos
estratos, volúmenes, umbrales y puertas.

Produce (todo bajo `muestreo/`):
  - samples_v3.json          salida de `sampler.Sampler.muestrear_todo(20)` (único
                             post-proceso: `config.kg_path`/`config.mapa` relativos al repo)
  - resumen_muestreo_v3.json en seco: qué anclas saldrían, distribución por
                             estrato/sub-estrato/TO, tamaños de población,
                             descartes por motivo, censo en KG-Refinado (AnclaIndex),
                             puertas mecánicas a/c sobre los samples, censo de
                             huérfanos de label (retriever booleano in-memory),
                             doble corrida byte-idéntica, selftest del runner con
                             cliente stub (0 API)
  - estimacion_faseB_v3.json estimación de costo con la fórmula del pipeline
                             (`estimacion.estimar`) + estimador empírico de 5ceb816

Principio 7: no abre samples.json ni preguntas_faseB.json de sinteticas/out (el
runner del pipeline lee su SAMPLES_PATH por atributo de módulo; acá se lo apunta
al archivo propio ANTES de llamarlo). El solapamiento de anclas con EV2 lo mide
la mesa en revisión, no este script.

Uso: python3 -B muestreo_v3.py
"""

from __future__ import annotations

import hashlib
import io
import json
import sys
from collections import Counter, defaultdict
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun_ablacion import (KG_REFINADO_SHA256, MUESTREO_DIR, SEMILLA_V3,  # noqa: E402
                            rel_repo, verificar_piezas)

# pipeline de sintéticas — SOLO import
import comun as sin_comun  # noqa: E402
import estimacion  # noqa: E402
import runner_faseB  # noqa: E402
import sampler  # noqa: E402
from generador import TokensProhibidos  # noqa: E402
from resolucion import AnclaIndex  # noqa: E402
from validador import Validador  # noqa: E402

SAMPLES_PATH = MUESTREO_DIR / "samples_v3.json"
RESUMEN_PATH = MUESTREO_DIR / "resumen_muestreo_v3.json"
ESTIMACION_PATH = MUESTREO_DIR / "estimacion_faseB_v3.json"
VOLUMEN = sampler.VOLUMEN_POR_ESTRATO      # 20 (= corrida de EV2)

# Precios para resolver la fórmula (USD/MTok). Sonnet 5, tarifa introductoria
# vigente hasta 2026-08-31 (documentación oficial, verificada el 2026-08-17);
# tarifa de lista posterior 3 / 15. La autorización de la fase B re-verifica.
PRECIOS = {"sonnet5_intro_hasta_2026-08-31": (2.0, 10.0),
           "sonnet5_lista": (3.0, 15.0)}
# Estimador empírico de la fase B ejecutada (README de sinteticas, 5ceb816):
FASEB_5CEB816 = {"samples": 98, "aptos": 64, "intentos": 147, "llamadas": 810,
                 "gasto_usd": 2.20, "estimado_sellado_usd": 2.55}


def _sha_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def _dump(obj) -> bytes:
    return json.dumps(obj, ensure_ascii=False, indent=1).encode("utf-8")


# --------------------------------------------------------------------------- #
# 1. Muestreo (doble corrida, byte-idéntica)                                   #
# --------------------------------------------------------------------------- #
def muestrear() -> tuple[dict, dict]:
    s1 = sampler.Sampler(semilla=SEMILLA_V3)      # load_kg_raw verifica sha 26fac8b4
    res1 = s1.muestrear_todo(VOLUMEN)
    s2 = sampler.Sampler(semilla=SEMILLA_V3)
    res2 = s2.muestrear_todo(VOLUMEN)
    # Único post-proceso: rutas absolutas de la máquina -> relativas al repo
    # (el contenido muestreado no se toca).
    for r in (res1, res2):
        r["config"]["kg_path"] = rel_repo(r["config"]["kg_path"])
        r["config"]["mapa"] = rel_repo(r["config"]["mapa"])
    b1, b2 = _dump(res1), _dump(res2)
    assert res1["config"]["kg_sha256"] == KG_REFINADO_SHA256
    MUESTREO_DIR.mkdir(parents=True, exist_ok=True)
    SAMPLES_PATH.write_bytes(b1)
    doble = {"corrida_1_sha256": _sha_bytes(b1), "corrida_2_sha256": _sha_bytes(b2),
             "byte_identicas": b1 == b2}
    return res1, {"doble_corrida": doble, "sampler": s1}


# --------------------------------------------------------------------------- #
# 2. Poblaciones por estrato (tamaño del universo del que se muestrea)         #
# --------------------------------------------------------------------------- #
def poblaciones(s: sampler.Sampler) -> dict:
    g = s.g
    ea = sum(1 for e in g.edges
             if s._elegible_dirigido(e["source"]) is None
             and s._elegible_dirigido(e["target"]) is None)
    hubs = [nid for nid, gr in g.grado.items()
            if gr >= sampler.HUB_UMBRAL_GRADO and s._elegible_dirigido(nid) is None]
    hubs_con_familia = 0
    for hub in hubs:
        grupos: dict = defaultdict(list)
        for (v, e, d) in g.vecinos_undirected(hub):
            if s._elegible_dirigido(v) is None:
                grupos[(e["relation"], d)].append(v)
        if any(sampler.FAMILIA_MIN <= len(vs) <= sampler.FAMILIA_MAX for vs in grupos.values()):
            hubs_con_familia += 1
    pares = s._pares_ed()
    inter = sum(1 for p in pares if s._es_inter_to(p))
    ee_con_ancla = sum(1 for nid in g.por_id if g.anclas(nid))
    return {
        "E-A_aristas_elegibles": ea,
        "E-B_nodos_inicio_elegibles": sum(1 for n in g.nodes if s._elegible_dirigido(n["id"]) is None),
        "E-C_hubs_elegibles_grado_ge_10": len(hubs),
        "E-C_hubs_con_familia_3_25": hubs_con_familia,
        "E-D_pares_candidatos": len(pares),
        "E-D_pares_inter_to": inter,
        "E-D_pares_intra_to": len(pares) - inter,
        "E-E_nodos_total": len(g.nodes),
        "E-E_nodos_con_ancla_pdf": ee_con_ancla,
        "nota": ("Poblaciones ANTES del gate de quemado (5 sets) y de la unicidad de nodo en E-D. "
                 "Sirven para que la mesa estime el solapamiento esperado con la muestra de EV2 "
                 "(misma población, otra semilla) sin abrir material EV2."),
    }


# --------------------------------------------------------------------------- #
# 3. Resumen en seco de los samples                                            #
# --------------------------------------------------------------------------- #
def resumen_samples(res: dict) -> dict:
    samples = res["samples"]
    por_estrato = Counter(s["estrato"] for s in samples)
    por_sub = Counter(f"{s['estrato']}/{s['sub_estrato']}" for s in samples if s["sub_estrato"])
    anclas_por_sample = {s["sample_id"]: [f"{a['to']}:{a['ancla']}" for a in s["gold"]["anclas"]]
                         for s in samples}
    to_gold = Counter(a["to"] for s in samples for a in s["gold"]["anclas"])
    to_por_estrato = {e: Counter(a["to"] for s in samples if s["estrato"] == e for a in s["gold"]["anclas"])
                      for e in sorted(por_estrato)}
    n_anclas = [len(s["gold"]["anclas"]) for s in samples]
    anclas_unicas = sorted({x for xs in anclas_por_sample.values() for x in xs})
    descartes = Counter()
    for d in res["descartes"]:
        m = d["motivo"]
        descartes[(d["estrato"], m.split(":")[0] if m.startswith("quemado") else m)] += 1
    return {
        "n_samples": len(samples),
        "conteo_por_estrato": dict(sorted(por_estrato.items())),
        "conteo_por_sub_estrato": dict(sorted(por_sub.items())),
        "anclas_gold_por_sample": anclas_por_sample,
        "anclas_gold_unicas": anclas_unicas,
        "n_anclas_gold_unicas": len(anclas_unicas),
        "anclas_por_sample": {"min": min(n_anclas), "max": max(n_anclas),
                              "media": round(sum(n_anclas) / len(n_anclas), 2),
                              "total": sum(n_anclas)},
        "anclas_gold_por_TO": dict(sorted(to_gold.items())),
        "anclas_gold_por_TO_y_estrato": {e: dict(sorted(c.items())) for e, c in to_por_estrato.items()},
        "descartes_del_sampler_por_estrato_y_motivo": {f"{e}|{m}": n for (e, m), n in sorted(descartes.items())},
        "n_descartes_del_sampler": len(res["descartes"]),
        "sample_ids": [s["sample_id"] for s in samples],
    }


# --------------------------------------------------------------------------- #
# 4. Censo en KG-Refinado + puertas mecánicas (a) y (c) sobre los samples       #
# --------------------------------------------------------------------------- #
def censo_y_puertas(res: dict, kg_raw: dict) -> dict:
    idx = AnclaIndex(kg_raw)
    val = Validador(idx, sin_comun.Quemado(sin_comun.MAPA_5SETS))
    por_sample, ausentes, censo_grande = {}, [], []
    fallas_a, fallas_c = [], []
    for s in res["samples"]:
        c = idx.censo(s["gold"]["anclas"])
        pa, pc = val.puerta_a(s), val.puerta_c(s)
        por_sample[s["sample_id"]] = {
            "n_anclas": len(s["gold"]["anclas"]),
            "n_nodos_gold_censo": len(c["nodos_gold"]),
            "anclas_ausentes": [list(k) for k in c["ausentes"]],
            "censo_por_ancla": {f"{k[0]}:{k[1]}": len(v) for k, v in c["resueltas"].items()},
            "puerta_a_ok": pa["ok"], "puerta_c_ok": pc["ok"],
            "censo_grande_diagnostico": pa["censo"]["censo_grande_diagnostico"],
        }
        if c["ausentes"]:
            ausentes.append(s["sample_id"])
        if pa["censo"]["censo_grande_diagnostico"]:
            censo_grande.append(s["sample_id"])
        if not pa["ok"]:
            fallas_a.append((s["sample_id"], pa["motivos"]))
        if not pc["ok"]:
            fallas_c.append((s["sample_id"], pc["motivos"]))
    tam = [v["n_nodos_gold_censo"] for v in por_sample.values()]
    tam_sorted = sorted(tam)
    return {
        "grafo": "KG-Refinado", "kg_sha256": KG_REFINADO_SHA256,
        "contenedores_excluidos_del_censo": len(idx.contenedores),
        "samples_con_alguna_ancla_ausente": ausentes,
        "samples_con_censo_grande_gt50": censo_grande,
        "nodos_gold_por_sample": {"min": tam_sorted[0], "mediana": tam_sorted[len(tam) // 2],
                                  "max": tam_sorted[-1]},
        "puerta_a_fallas": fallas_a, "puerta_c_fallas": fallas_c,
        "puertas_a_c_ok_todos": not fallas_a and not fallas_c,
        "por_sample": por_sample,
    }


# --------------------------------------------------------------------------- #
# 5. Huérfanos de label (retriever booleano del harness, in-memory)             #
# --------------------------------------------------------------------------- #
def huerfanos_label(res: dict, kg_raw: dict) -> dict:
    """Clase medible pre-registrada para P6: un nodo gold es HUÉRFANO DE LABEL
    (tipo BKL-0022) si NINGÚN token de contenido de su label, buscado solo con
    buscar_nodos(token, 10) del harness (booleano), lo trae al top-10; se
    registra además si el label completo lo trae. Medido con GraphIndex in-memory
    sobre KG-Refinado (= celda control, byte-idéntico a Neo4j paridad)."""
    index = sin_comun.index_runtime()
    por_id = {n["id"]: n for n in kg_raw["nodes"]}
    detalle, por_estrato = {}, defaultdict(lambda: {"nodos": 0, "huerfanos": 0, "samples_con_huerfano": 0})
    for s in res["samples"]:
        hay = False
        for nid in s["metadatos"]["debug_ids_respuesta"]:
            label = por_id[nid].get("label") or ""
            toks = sorted(sin_comun.tokens_contenido(label))
            trae_token = [t for t in toks
                          if any(r["id"] == nid for r in index.buscar_nodos(t, 10)["resultados"])]
            top_label = [r["id"] for r in index.buscar_nodos(label, 10)["resultados"]]
            huerfano = (len(toks) > 0 and not trae_token)
            detalle[f"{s['sample_id']}::{nid}"] = {
                "estrato": s["estrato"], "label": label, "tokens_label": toks,
                "tokens_que_lo_traen_top10": trae_token,
                "label_completo_lo_trae_top10": nid in top_label,
                "huerfano_de_label": huerfano,
            }
            por_estrato[s["estrato"]]["nodos"] += 1
            if huerfano:
                por_estrato[s["estrato"]]["huerfanos"] += 1
                hay = True
        if hay:
            por_estrato[s["estrato"]]["samples_con_huerfano"] += 1
    n_h = sum(1 for d in detalle.values() if d["huerfano_de_label"])
    return {"definicion": huerfanos_label.__doc__.strip(),
            "n_nodos_gold_evaluados": len(detalle), "n_huerfanos_de_label": n_h,
            "samples_con_huerfano": sorted({k.split("::")[0] for k, d in detalle.items() if d["huerfano_de_label"]}),
            "por_estrato": {k: dict(v) for k, v in sorted(por_estrato.items())},
            "detalle": detalle}


# --------------------------------------------------------------------------- #
# 6. Selftest del runner de fase B con cliente STUB (0 API) sobre samples_v3    #
# --------------------------------------------------------------------------- #
def selftest_runner() -> dict:
    """Apunta runner_faseB.SAMPLES_PATH (atributo de módulo) al archivo propio y
    corre su modo_selftest (stub; verifica estructura + 6 llamadas por sample)."""
    original = runner_faseB.SAMPLES_PATH
    runner_faseB.SAMPLES_PATH = SAMPLES_PATH
    buf = io.StringIO()
    try:
        with redirect_stdout(buf):
            rc = runner_faseB.modo_selftest()
    finally:
        runner_faseB.SAMPLES_PATH = original
    return {"exit_code": rc, "stdout": buf.getvalue().strip(),
            "samples_path_inyectado": rel_repo(SAMPLES_PATH)}


# --------------------------------------------------------------------------- #
# 7. Estimación de costo de la fase B (fórmula del pipeline + empírico)         #
# --------------------------------------------------------------------------- #
def estimar_faseB(res: dict) -> dict:
    est = estimacion.estimar(samples_path=SAMPLES_PATH)
    tin, tout = est["totales"]["tokens_in"], est["totales"]["tokens_out"]
    n = len(res["samples"])
    por_precio = {k: round((tin * pi + tout * po) / 1e6, 4) for k, (pi, po) in PRECIOS.items()}
    emp = FASEB_5CEB816
    empirico = {
        "usd_por_sample_5ceb816": round(emp["gasto_usd"] / emp["samples"], 5),
        "usd_estimado_para_n": round(emp["gasto_usd"] / emp["samples"] * n, 3),
        "aptos_esperados_al_rendimiento_5ceb816": round(emp["aptos"] / emp["samples"] * n, 1),
        "llamadas_esperadas": round(emp["llamadas"] / emp["samples"] * n),
        "intentos_esperados": round(emp["intentos"] / emp["samples"] * n),
    }
    alternativa = {}
    for n_alt in (46, 60, 98):
        alternativa[str(n_alt)] = {
            "usd_formula_intro": round((tin * PRECIOS["sonnet5_intro_hasta_2026-08-31"][0]
                                        + tout * PRECIOS["sonnet5_intro_hasta_2026-08-31"][1]) / 1e6 * n_alt / n, 3),
            "usd_empirico": round(emp["gasto_usd"] / emp["samples"] * n_alt, 3),
            "aptos_esperados": round(emp["aptos"] / emp["samples"] * n_alt, 1),
        }
    return {
        "n_samples": n,
        "formula_pipeline": est,      # supuestos S1–S5, líneas por ítem, tokens totales
        "precios_usd_por_mtok": PRECIOS,
        "costo_por_precio_usd": por_precio,
        "empirico_5ceb816": {**emp, **empirico},
        "escenarios_N": alternativa,
        "tope_fase_B_esta_unidad_usd": 3.0,
        "nota": ("La fórmula del pipeline (S4 factor 1,6 de descarte, output 400/200 chars) sobre-"
                 "estimó la fase B real de 5ceb816 (2,55 sellado vs 2,20 real); el estimador empírico "
                 "usa el gasto real por sample de esa corrida. Ambos quedan por debajo del tope de 3."),
    }


def main() -> int:
    print("piezas selladas:")
    verificar_piezas()
    print(f"\nmuestreo semilla {SEMILLA_V3} sobre KG-Refinado …")
    res, extra = muestrear()
    print(f"  samples: {res['conteo_por_estrato']}  descartes: {len(res['descartes'])}  "
          f"doble corrida byte-idéntica: {extra['doble_corrida']['byte_identicas']}")
    kg_raw = sin_comun.load_kg_raw()      # verifica sha
    resumen = {
        "unidad": "U-A1.3", "fase": "A (en seco, $0)",
        "config_sampler": res["config"],
        "distribucion_grados": res["distribucion_grados"],
        "doble_corrida": extra["doble_corrida"],
        "samples_v3_sha256": _sha_bytes(SAMPLES_PATH.read_bytes()),
        "poblaciones": poblaciones(extra["sampler"]),
        "resumen": resumen_samples(res),
        "censo_kg_refinado_y_puertas_a_c": censo_y_puertas(res, kg_raw),
        "huerfanos_label": huerfanos_label(res, kg_raw),
        "selftest_runner_stub": selftest_runner(),
    }
    RESUMEN_PATH.write_bytes(_dump(resumen))
    est = estimar_faseB(res)
    ESTIMACION_PATH.write_bytes(_dump(est))
    r = resumen["resumen"]
    print(f"  anclas gold únicas: {r['n_anclas_gold_unicas']}  por TO: {r['anclas_gold_por_TO']}")
    print(f"  poblaciones: {resumen['poblaciones']}")
    c = resumen["censo_kg_refinado_y_puertas_a_c"]
    print(f"  censo: ausentes={c['samples_con_alguna_ancla_ausente']}  puertas a/c ok todos={c['puertas_a_c_ok_todos']}"
          f"  nodos gold/sample min/med/max={c['nodos_gold_por_sample']}")
    h = resumen["huerfanos_label"]
    print(f"  huérfanos de label: {h['n_huerfanos_de_label']}/{h['n_nodos_gold_evaluados']} nodos gold; "
          f"por estrato {h['por_estrato']}")
    print(f"  selftest runner (stub): exit={resumen['selftest_runner_stub']['exit_code']}  "
          f"{resumen['selftest_runner_stub']['stdout'].splitlines()[-1]}")
    print(f"  estimación fase B: {est['costo_por_precio_usd']}  empírico {est['empirico_5ceb816']['usd_estimado_para_n']}"
          f"  aptos esperados {est['empirico_5ceb816']['aptos_esperados_al_rendimiento_5ceb816']}")
    print(f"-> {rel_repo(SAMPLES_PATH)}\n-> {rel_repo(RESUMEN_PATH)}\n-> {rel_repo(ESTIMACION_PATH)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
