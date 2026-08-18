"""
validar_pares_v3.py — Validación completa y sellado del material nuevo tras la
fase B (o selftest con stub, $0). Lee `pares/preguntas_faseB_v3.json` (salida
del runner reusado) y produce, bajo `pares/`:

  pares_v3.json               el SET a sellar por commit: solo los pares APTOS
                              (sample_id, estrato, sub_estrato, literal,
                              antilexica, gold en anclas, tokens_prohibidos,
                              solapes, intento), más config (semilla, kg sha,
                              estratos, umbrales)
  registro_generacion_v3.json TODOS los intentos con veredicto y motivo (patrón
                              generacion_u6_registro): nada se tira
  censo_kg_refinado_v3.json   censo de las anclas gold de los aptos en KG-Refinado
                              (AnclaIndex del pipeline, sin contenedores): nodos
                              gold locales por ancla, ausentes (esperado 0: se
                              muestreó de este grafo), tamaños
  validacion_v3.json          re-verificación mecánica de las 4 puertas sobre los
                              aptos (validador.Validador.validar, sin editar),
                              distribución por estrato / sub-estrato / TO, solape
                              léxico (literal vs anti-léxica), resumen de descartes
                              por motivo, checks LLM (V1/V2/V3) agregados
  manifest_pares_v3.txt       sha256 + descripción de cada archivo del directorio

Uso: python3 -B validar_pares_v3.py                (sobre pares/preguntas_faseB_v3.json)
     python3 -B validar_pares_v3.py --selftest     (stub sobre 6 samples; escribe en un
                                                    directorio temporal, no en pares/)
"""

from __future__ import annotations

import argparse
import hashlib
import json
import statistics as st
import sys
import tempfile
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun_ablacion import (ABLACION_DIR, CELDAS_DIR, KG_REFINADO_SHA256,  # noqa: E402
                            MUESTREO_DIR, PARES_DIR, SEMILLA_V3, rel_repo,
                            verificar_piezas)

import comun as sin_comun  # noqa: E402
import runner_faseB  # noqa: E402
from generador import Generador, StubCliente, TokensProhibidos  # noqa: E402
from resolucion import AnclaIndex  # noqa: E402
from validador import SOLAPE_UMBRAL, Validador  # noqa: E402

ENTRADA = PARES_DIR / "preguntas_faseB_v3.json"


def _sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def _dump(p: Path, obj):
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)


def _muestra_por_id(samples_path: Path) -> dict:
    with samples_path.open(encoding="utf-8") as f:
        data = json.load(f)
    return {s["sample_id"]: s for s in data["samples"]}, data


def validar(entrada: Path, samples_path: Path, out_dir: Path) -> dict:
    with entrada.open(encoding="utf-8") as f:
        payload = json.load(f)
    registros = payload["registros"]
    por_id, samples_data = _muestra_por_id(samples_path)
    kg_raw = sin_comun.load_kg_raw()                      # verifica sha 26fac8b4
    idx = AnclaIndex(kg_raw)
    val = Validador(idx, sin_comun.Quemado(sin_comun.MAPA_5SETS))

    # --- 1. aptos: un registro por sample (el intento apto) ---
    aptos = {}
    for r in registros:
        if r["veredicto"] == "apto" and r["sample_id"] not in aptos:
            aptos[r["sample_id"]] = r
    pares = []
    for sid, r in sorted(aptos.items()):
        s = por_id[sid]
        pares.append({
            "sample_id": sid, "estrato": s["estrato"], "sub_estrato": s["sub_estrato"],
            "literal": r["literal"], "antilexica": r["antilexica"],
            "gold": s["gold"], "tokens_prohibidos": r["tokens_prohibidos"],
            "solape_literal": r["solape_literal"]["solape"],
            "solape_antilexica": r["solape_antilexica"]["solape"],
            "intento": r.get("intento", 1),
            "debug_ids_respuesta": s["metadatos"]["debug_ids_respuesta"],
        })

    # --- 2. re-verificación mecánica de las 4 puertas sobre los aptos ---
    reverif = {}
    for p in pares:
        v = val.validar(por_id[p["sample_id"]], p["literal"], p["antilexica"],
                        set(p["tokens_prohibidos"]))
        reverif[p["sample_id"]] = {"veredicto": v["veredicto"], "motivos": v["motivos"],
                                   "puertas_ok": [d["puerta"] for d in v["detalle_puertas"] if d["ok"]],
                                   "requiere_llm": v["requiere_llm"]}
    reverif_ok = all(v["veredicto"] == "apto" for v in reverif.values())

    # --- 3. censo en KG-Refinado ---
    censo = {}
    for p in pares:
        c = idx.censo(p["gold"]["anclas"])
        censo[p["sample_id"]] = {
            "anclas": [f"{a['to']}:{a['ancla']}" for a in p["gold"]["anclas"]],
            "resueltas": {f"{k[0]}:{k[1]}": v for k, v in c["resueltas"].items()},
            "n_nodos_gold": len(c["nodos_gold"]),
            "ausentes": [f"{k[0]}:{k[1]}" for k in c["ausentes"]],
        }
    tam = sorted(v["n_nodos_gold"] for v in censo.values()) or [0]
    censo_out = {
        "grafo": "KG-Refinado", "kg_sha256": KG_REFINADO_SHA256,
        "contenedores_excluidos": len(idx.contenedores),
        "n_pares": len(pares),
        "pares_con_ancla_ausente": [k for k, v in censo.items() if v["ausentes"]],
        "nodos_gold_por_par": {"min": tam[0], "mediana": tam[len(tam) // 2], "max": tam[-1]},
        "por_par": censo,
    }

    # --- 4. distribuciones, solape, descartes, checks LLM ---
    est = Counter(p["estrato"] for p in pares)
    sub = Counter(f"{p['estrato']}/{p['sub_estrato']}" for p in pares if p["sub_estrato"])
    to = Counter(a["to"] for p in pares for a in p["gold"]["anclas"])
    intentos_por_sample = Counter(r["sample_id"] for r in registros)
    motivos = Counter()
    for r in registros:
        if r["veredicto"] != "apto":
            for m in r["motivos"]:
                motivos[m.split(":")[0]] += 1
    llm = Counter()
    for r in registros:
        for k in ("v1_literal", "v1_antilexica"):
            llm[f"{k}_ok"] += bool(r["checks_llm"][k].get("autocontenida"))
        llm["v2_ok"] += bool(r["checks_llm"]["v2"].get("gold_unico"))
        llm["v3_ok"] += bool(r["checks_llm"]["v3"].get("misma_pregunta"))
    sol_l = [p["solape_literal"] for p in pares]
    sol_a = [p["solape_antilexica"] for p in pares]
    samples_totales = Counter(s["estrato"] for s in samples_data["samples"])
    validacion = {
        "entrada": rel_repo(entrada), "samples": rel_repo(samples_path),
        "n_registros": len(registros), "n_samples_intentados": len(intentos_por_sample),
        "n_aptos": len(pares),
        "rendimiento_aptos_sobre_samples": round(len(pares) / max(1, len(intentos_por_sample)), 3),
        "aptos_por_estrato": {e: f"{est.get(e, 0)}/{n}" for e, n in sorted(samples_totales.items())},
        "aptos_por_sub_estrato": dict(sorted(sub.items())),
        "anclas_gold_por_TO": dict(sorted(to.items())),
        "rescatados_por_reintento": sum(1 for p in pares if p["intento"] > 1),
        "descartes_por_motivo": dict(sorted(motivos.items())),
        "checks_llm_ok_sobre_registros": dict(llm),
        "solape_lexico": {
            "umbral_puerta_d": SOLAPE_UMBRAL,
            "literal": {"mediana": st.median(sol_l) if sol_l else None, "max": max(sol_l) if sol_l else None},
            "antilexica": {"mediana": st.median(sol_a) if sol_a else None, "max": max(sol_a) if sol_a else None},
        },
        "reverificacion_4_puertas_ok_todos": reverif_ok,
        "reverificacion_por_par": reverif,
    }

    # --- 4b. huérfanos de label (P6) entre los gold de los pares aptos ---
    huerf = _huerfanos_p6(pares)
    validacion["huerfanos_p6"] = huerf
    for p in pares:
        p["gold_huerfanos_de_label"] = huerf["por_par"].get(p["sample_id"], [])

    # --- 4c. gasto real leído de la db de la fase B (si existe) ---
    validacion["gasto_real_db"] = gasto_desde_db()

    # --- 5. archivos ---
    cfg = {
        "unidad": "U-A1.3", "semilla": SEMILLA_V3, "grafo": "KG-Refinado", "kg_sha256": KG_REFINADO_SHA256,
        "modelo_generador": payload["config"].get("modelo"),
        "estratos_incluidos": samples_data.get("fase_b_ablacion", {}).get("estratos_incluidos"),
        "solape_umbral": SOLAPE_UMBRAL, "n_pares": len(pares),
        "conteo_por_estrato": dict(sorted(est.items())),
    }
    _dump(out_dir / "pares_v3.json", {"config": cfg, "pares": pares})
    _dump(out_dir / "registro_generacion_v3.json",
          {"config": payload["config"], "resumen_runner": payload.get("resumen"),
           "descartes_por_motivo": dict(sorted(motivos.items())), "registros": registros})
    _dump(out_dir / "censo_kg_refinado_v3.json", censo_out)
    _dump(out_dir / "validacion_v3.json", validacion)
    return validacion


def _huerfanos_p6(pares: list) -> dict:
    """Cruza los gold de los pares aptos con la clase `huerfano_de_label` fijada
    ANTES de generar en muestreo/resumen_muestreo_v3.json (pre-registro §5 P6)."""
    resumen = MUESTREO_DIR / "resumen_muestreo_v3.json"
    with resumen.open(encoding="utf-8") as f:
        det = json.load(f)["huerfanos_label"]["detalle"]
    por_par, n_gold, n_h = {}, 0, 0
    for p in pares:
        hs = []
        for nid in p["debug_ids_respuesta"]:
            n_gold += 1
            d = det.get(f"{p['sample_id']}::{nid}")
            if d and d["huerfano_de_label"]:
                hs.append({"nodo": nid, "label": d["label"], "tokens_label": d["tokens_label"],
                           "label_completo_lo_trae_top10": d["label_completo_lo_trae_top10"]})
                n_h += 1
        if hs:
            por_par[p["sample_id"]] = hs
    por_estrato = Counter(p["estrato"] for p in pares if p["sample_id"] in por_par)
    return {"definicion": ("nodo gold cuyo label no es traído al top-10 de buscar_nodos booleano "
                           "por ningún token de contenido suelto (medido en fase A, in-memory, KG-Refinado)"),
            "fuente": rel_repo(resumen), "n_gold_en_aptos": n_gold, "n_huerfanos_en_aptos": n_h,
            "pares_con_huerfano": sorted(por_par), "n_pares_con_huerfano": len(por_par),
            "pares_con_huerfano_por_estrato": dict(sorted(por_estrato.items())), "por_par": por_par}


def gasto_desde_db(db_path: Path | None = None) -> dict | None:
    """Gasto REAL recomputado desde la db de la fase B (tabla `cache` de
    llm_cache: una fila por llamada pagada; `access_log` cuenta hits/misses).
    Precios: los del cliente reusado (cliente_faseB.PRECIO_*)."""
    import sqlite3
    from comun_ablacion import CACHE_DIR
    db_path = db_path or (CACHE_DIR / "ablacion_faseB_v3.db")
    if not db_path.exists():
        return None
    import cliente_faseB as cf
    con = sqlite3.connect(str(db_path))
    filas = con.execute("SELECT model, namespace, COUNT(*), SUM(input_tokens), SUM(output_tokens), "
                        "SUM(cache_read_tokens), SUM(cache_write_tokens) FROM cache "
                        "GROUP BY model, namespace").fetchall()
    acc = con.execute("SELECT run_label, hit, COUNT(*) FROM access_log GROUP BY run_label, hit").fetchall()
    stops = con.execute("SELECT stop_reason, COUNT(*) FROM cache GROUP BY stop_reason").fetchall()
    con.close()
    por_modelo = []
    total = 0.0
    for model, ns, n, tin, tout, cr, cw in filas:
        usd = (tin * cf.PRECIO_IN_POR_MTOK + tout * cf.PRECIO_OUT_POR_MTOK) / 1e6
        total += usd
        por_modelo.append({"model": model, "namespace": ns, "llamadas_pagadas": n, "input_tokens": tin,
                           "output_tokens": tout, "cache_read_tokens": cr, "cache_write_tokens": cw,
                           "usd": round(usd, 4)})
    return {"db": rel_repo(db_path), "precios_usd_por_mtok": {"in": cf.PRECIO_IN_POR_MTOK, "out": cf.PRECIO_OUT_POR_MTOK},
            "tope_usd_unidad": 3.0, "por_modelo": por_modelo, "usd_total": round(total, 4),
            "access_log": [{"run_label": r, "hit": bool(h), "n": n} for r, h, n in acc],
            "stop_reasons": {str(s): n for s, n in stops}}


def manifest(out_dir: Path, extra_dirs: list[Path]) -> Path:
    desc = {
        "pares_v3.json": "SET a sellar: pares aptos (literal + anti-léxica, gold en anclas)",
        "registro_generacion_v3.json": "todos los intentos del runner con veredicto y motivos",
        "censo_kg_refinado_v3.json": "censo de anclas gold de los aptos en KG-Refinado (sin contenedores)",
        "validacion_v3.json": "re-verificación de 4 puertas, distribuciones, solape, descartes, checks LLM",
        "calibracion_faseB_v3.json": "salida del runner en calibración (10 samples)",
        "preguntas_faseB_v3.json": "salida cruda del runner (calibración + resto)",
    }
    lineas = []
    for d in [out_dir] + extra_dirs:
        for p in sorted(d.iterdir()):
            if p.is_file() and p.name != "manifest_pares_v3.txt" and not p.name.endswith(".db"):
                lineas.append(f"{_sha(p)}  {rel_repo(p)}  # {desc.get(p.name, '')}".rstrip(" #"))
    for p in (ABLACION_DIR / "preregistro_ablacion.md", ABLACION_DIR / "README.md",
              ABLACION_DIR / "anexo_solapamiento_anclas.md"):
        if p.exists():
            lineas.append(f"{_sha(p)}  {rel_repo(p)}")
    m = out_dir / "manifest_pares_v3.txt"
    m.write_text("\n".join(lineas) + "\n", encoding="utf-8")
    return m


def selftest() -> int:
    """Corre el runner con STUB sobre 6 samples (0 API) a un directorio temporal
    y valida su salida con este módulo. No escribe en pares/."""
    fixtures = {
        "PALABRAS PROHIBIDAS": '{"pregunta": "¿Qué requisitos rigen para el caso reformulado sin la jerga del asunto?"}',
        "auto-contenida bajo ese criterio": '{"autocontenida": true, "motivo": "ok"}',
        "admite OTRA respuesta": '{"gold_unico": true, "respuesta_alternativa": ""}',
        "EXACTAMENTE lo mismo": '{"misma_pregunta": true, "diferencia": ""}',
    }
    stub = StubCliente(fixtures=fixtures,
                       respuesta_defecto='{"pregunta": "¿Qué establece la normativa aplicable al caso de la fixture para una entidad alcanzada?"}')
    samples_path = MUESTREO_DIR / "samples_v3.json"
    original = runner_faseB.SAMPLES_PATH
    runner_faseB.SAMPLES_PATH = samples_path
    try:
        gen, val, data = runner_faseB._preparar(stub)
        subset = runner_faseB.seleccion_calibracion(data["samples"])[:6]
        registros = runner_faseB.correr(stub, subset, reintentos=1)
    finally:
        runner_faseB.SAMPLES_PATH = original
    tmp = Path(tempfile.mkdtemp(prefix="ablacion_selftest_"))
    entrada = tmp / "preguntas_faseB_v3.json"
    _dump(entrada, {"config": {"modo": "selftest", "modelo": "stub"}, "registros": registros,
                    "resumen": {"n_registros": len(registros)}})
    v = validar(entrada, samples_path, tmp)
    m = manifest(tmp, [])
    ok = (v["n_samples_intentados"] == 6 and v["reverificacion_4_puertas_ok_todos"]
          and (tmp / "pares_v3.json").exists() and m.exists())
    print(f"selftest validar_pares_v3: samples={v['n_samples_intentados']} aptos={v['n_aptos']} "
          f"reverif_ok={v['reverificacion_4_puertas_ok_todos']} manifest={m.exists()} -> {tmp}")
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--entrada", default=str(ENTRADA))
    ap.add_argument("--samples", default=str(MUESTREO_DIR / "samples_v3_faseB.json"))
    args = ap.parse_args()
    verificar_piezas(verbose=False)
    if args.selftest:
        return selftest()
    v = validar(Path(args.entrada), Path(args.samples), PARES_DIR)
    m = manifest(PARES_DIR, [MUESTREO_DIR, CELDAS_DIR])
    print(json.dumps({k: v[k] for k in ("n_registros", "n_samples_intentados", "n_aptos",
                                        "aptos_por_estrato", "aptos_por_sub_estrato",
                                        "descartes_por_motivo", "solape_lexico",
                                        "reverificacion_4_puertas_ok_todos")},
                     ensure_ascii=False, indent=1))
    print(f"-> {rel_repo(PARES_DIR)}  manifest {rel_repo(m)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
