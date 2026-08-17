"""
runner_enc.py — Re-corridas N=3 del AGENTE sobre la población disparada
(protocolo §3: 63 pares "parcial" + auditoría simétrica del 10 % de los
"correcto"), con el harness congelado TAL COMO corrió en la corrida base.

Reutiliza sin editar `runner_ev2.correr_grafo` (data/experiment/ev2_corrida/code):
mismo FullCaptureAgent (harness.GraphAgent + captura íntegra de outputs de
tool), mismo modelo hardcodeado en harness.MODEL, misma vista runtime de cada
grafo (comun_ev2.cargar_runtime, grafos verificados por sha 3/3), misma
persistencia por caso (traza + steps_full + raw_turns_agent + metadata). A
cada traza persistida se le AGREGA `meta.encadenamiento` (unidad, rep, tipo de
disparo, veredicto base, id opaco base); ninguna clave de la base se altera
(`meta.n_rep` sigue en 1: cada repetición es una corrida N=1 bajo su propio
label).

Anti-cache (protocolo §4, patrón rt_c6_n3): label `ev2_enc_<grafo>_r{n}` y db
propia `cache/ev2_enc_<grafo>_r{n}.db` por (grafo, rep). Como el primer turno de
una pregunta es idéntico en toda repetición (mismo system, tools y pregunta),
compartir db entre reps —o con la base— replayaría la conversación desde caché
en vez de re-muestrear; por eso cada rep tiene su db y el reporte exige 0 hits
en el access_log de cada db (definición operativa de "0 cross-hits" del patrón
rt_c6_n3: 0 hits de agente por rep).

Orden: por grafo, los casos disparados en el orden resuelto del protocolo §5
(orden-ev2-v1 filtrado; orden/orden_agente_por_grafo.json), idéntico en las
tres reps. Ejecución grafo-mayor, rep-menor.

Gasto y freno: tope PROPIO de esta etapa (--tope-agente, obligatorio con
--autorizado-fase-b), freno por proyección de correr_grafo (gasto acumulado por
harness.cost_usd proyectado al total de corridas de la etapa; se detiene ANTES
de la siguiente corrida). Gasto real desde las dbs (tokens de la tabla cache;
precios solo por CLI). Retomable: se saltean los casos con traza persistida.

Uso (fase B, solo con autorización explícita):
  .venv/bin/python -B data/experiment/ev2_encadenamiento/code/runner_enc.py \
      --autorizado-fase-b --tope-agente <USD> \
      [--precio-in --precio-out --precio-cw --precio-cr]   (USD/MTok, para el gasto)
  --solo-resumen recomputa índice y gasto desde trazas/dbs sin llamar a la API.
"""

from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_enc as en                       # noqa: E402
import runner_ev2 as rv                      # noqa: E402  (corrida base, sin editar)
from comun_ev2 import cargar_runtime         # noqa: E402

DB_AGENTE = "ev2_enc_{grafo}_r{rep}.db"


def db_agente(grafo: str, rep: int, cache_dir: Path = en.CACHE_DIR) -> Path:
    return cache_dir / DB_AGENTE.format(grafo=grafo.replace("_", ""), rep=rep)


# --------------------------------------------------------------------------- #
# Una (grafo, rep): correr_grafo de la base + metadata de encadenamiento       #
# --------------------------------------------------------------------------- #
def correr_grafo_rep(pob: dict, grafo: str, rep: int, *, client_real, cache_dir: Path,
                     trazas_dir: Path, estado_gasto: dict | None,
                     casos: list[dict] | None = None) -> dict | None:
    label = en.label_agente(grafo, rep)
    outdir = trazas_dir / label
    outdir.mkdir(parents=True, exist_ok=True)
    casos = list(casos if casos is not None else en.casos_agente(pob, grafo))
    pend = [c for c in casos if not (outdir / f"{rv._sanitizar(c['caso_id'])}.json").exists()]
    print(f"== encadenamiento {grafo} rep {rep} ({label}): {len(casos)} casos, "
          f"{len(casos) - len(pend)} ya persistidos, {len(pend)} pendientes ==", flush=True)
    resumen = None
    if pend:
        resumen = rv.correr_grafo(grafo, client_real=client_real, db_path=db_agente(grafo, rep, cache_dir),
                                  label=label, casos=pend, outdir=outdir, estado_gasto=estado_gasto)
    # metadata de encadenamiento (agregada; nada de la base se altera)
    por_par = {p["id_pregunta"]: p for p in pob["pares"] if p["grafo"] == grafo}
    for c in casos:
        f = outdir / f"{rv._sanitizar(c['caso_id'])}.json"
        if not f.exists():
            continue                                    # frenado antes de este caso
        t = json.loads(f.read_text(encoding="utf-8"))
        if "encadenamiento" in t["meta"]:
            continue
        p = por_par[c["caso_id"]]
        t["meta"]["encadenamiento"] = {
            "unidad": "ev2_encadenamiento", "rep": rep, "reps_previstas": en.REPS_AGENTE,
            "label": label, "tipo": p["tipo"], "veredicto_base": p["veredicto_base"],
            "id_opaco_base": p["id_opaco_base"], "label_base": p["label_base"],
            "sha256_respuesta_base": p["sha256_respuesta_base"],
            "regla": ("protocolo §3: re-corrida N=3 disparada por veredicto base 'parcial'; "
                      "auditoria_correcto = muestra 10 % de 'correcto' con semilla auditoria-ev2-v1"),
        }
        f.write_text(json.dumps(t, ensure_ascii=False, indent=2), encoding="utf-8")
    return resumen


# --------------------------------------------------------------------------- #
# Índice de trazas + gasto desde dbs + hits                                    #
# --------------------------------------------------------------------------- #
def gasto_dbs_agente(cache_dir: Path, grafos, reps: int, precios: dict | None) -> dict:
    """Tokens (y USD si hay precios) desde la tabla cache de cada db (una fila por
    miss pagado) + hits por run_label desde access_log (0 exigido)."""
    por_db, tot = {}, Counter()
    for g in grafos:
        for rep in range(1, reps + 1):
            p = db_agente(g, rep, cache_dir)
            if not p.exists():
                por_db[p.name] = None
                continue
            conn = sqlite3.connect(str(p))
            n, i, o, cr, cw = conn.execute(
                "SELECT COUNT(*), COALESCE(SUM(input_tokens),0), COALESCE(SUM(output_tokens),0), "
                "COALESCE(SUM(cache_read_tokens),0), COALESCE(SUM(cache_write_tokens),0) FROM cache").fetchone()
            hits = {k: int(v or 0) for k, v in conn.execute(
                "SELECT run_label, SUM(hit) FROM access_log GROUP BY run_label")}
            accesos = conn.execute("SELECT COUNT(*) FROM access_log").fetchone()[0]
            dominios = sorted(r[0] for r in conn.execute("SELECT DISTINCT domain FROM cache"))
            conn.close()
            d = {"filas": n, "input_tokens": i, "output_tokens": o, "cache_read_tokens": cr,
                 "cache_write_tokens": cw, "accesos": accesos, "hits_por_label": hits,
                 "hits": sum(hits.values()), "dominios": dominios}
            if precios:
                d["usd"] = round((i * precios["in"] + o * precios["out"] + cw * precios["cw"]
                                  + cr * precios["cr"]) / 1e6, 4)
            por_db[p.name] = d
            for k in ("filas", "input_tokens", "output_tokens", "cache_read_tokens",
                      "cache_write_tokens", "accesos", "hits"):
                tot[k] += d[k]
    out = {"por_db": por_db, "total": dict(tot),
           "hits_total": tot["hits"], "dbs_existentes": sum(v is not None for v in por_db.values())}
    if precios:
        out["precios_usd_mtok"] = precios
        out["total"]["usd"] = round(sum(v["usd"] for v in por_db.values() if v), 4)
    return out


def indice_trazas(pob: dict, trazas_dir: Path, reps: int) -> dict:
    """Estado de las 198 corridas previstas: persistidas / con respuesta parseada /
    con error o sin parse (incompletas, para laudo)."""
    filas, faltan = [], []
    for p in pob["pares"]:
        for rep in range(1, reps + 1):
            lab = en.label_agente(p["grafo"], rep)
            f = trazas_dir / lab / f"{p['id_pregunta']}.json"
            if not f.exists():
                faltan.append({"grafo": p["grafo"], "rep": rep, "id_pregunta": p["id_pregunta"]})
                continue
            t = json.loads(f.read_text(encoding="utf-8"))
            tr, m = t["trace"], t["meta"]
            filas.append({"grafo": p["grafo"], "rep": rep, "id_pregunta": p["id_pregunta"], "label": lab,
                          "tipo": p["tipo"], "parse_ok": bool(tr.get("parse_ok")), "error": tr.get("error"),
                          "respuesta_ok": bool(tr.get("parse_ok")) and isinstance((tr.get("final_json") or {}).get("respuesta"), str)
                          and bool((tr.get("final_json") or {}).get("respuesta", "").strip()),
                          "tools": tr.get("tool_calls_used"), "hit_tool_limit": tr.get("hit_tool_limit"),
                          "tokens_in": tr.get("tokens_in"), "tokens_out": tr.get("tokens_out"),
                          "cache_read": tr.get("cache_read"), "cache_write": tr.get("cache_write"),
                          "cost_usd_harness": tr.get("cost_usd"),
                          "cache_turnos": m.get("cache_turnos"), "model": m.get("model"),
                          "graph_fingerprint": m.get("graph_fingerprint"),
                          "encadenamiento_meta": "encadenamiento" in m,
                          "sha256_respuesta": en.sha256_texto((tr.get("final_json") or {}).get("respuesta") or "")})
    incompletas = [x for x in filas if not x["respuesta_ok"]]
    return {"n_previstas": len(pob["pares"]) * reps, "n_persistidas": len(filas),
            "n_faltantes": len(faltan), "faltantes": faltan,
            "n_incompletas": len(incompletas), "incompletas": incompletas,
            "por_grafo_rep": dict(Counter(f"{x['grafo']}_r{x['rep']}" for x in filas)),
            "modelos": sorted({x["model"] for x in filas}),
            "hits_turnos_trazas": sum((x["cache_turnos"] or {}).get("hits", 0) for x in filas),
            "turnos_trazas": sum((x["cache_turnos"] or {}).get("total", 0) for x in filas),
            "costo_harness_usd": round(sum(x["cost_usd_harness"] or 0 for x in filas), 4),
            "tokens_trazas": {k: sum(x[k] or 0 for x in filas)
                              for k in ("tokens_in", "tokens_out", "cache_read", "cache_write")},
            "hit_tool_limit": sum(bool(x["hit_tool_limit"]) for x in filas),
            "filas": filas}


def escribir_resumen(pob: dict, trazas_dir: Path, cache_dir: Path, reps: int, precios: dict | None,
                     extra: dict | None = None) -> dict:
    idx = indice_trazas(pob, trazas_dir, reps)
    gasto = gasto_dbs_agente(cache_dir, en.GRAFOS, reps, precios)
    res = {"ts": datetime.now().isoformat(timespec="seconds"), "reps": reps,
           "indice": {k: v for k, v in idx.items() if k != "filas"},
           "gasto_dbs": gasto, **(extra or {})}
    en.REPORTE_DIR.mkdir(parents=True, exist_ok=True)
    (en.REPORTE_DIR / "resumen_agente.json").write_text(json.dumps(res, ensure_ascii=False, indent=2),
                                                        encoding="utf-8")
    (en.REPORTE_DIR / "indice_trazas_agente.json").write_text(json.dumps(idx, ensure_ascii=False, indent=2),
                                                              encoding="utf-8")
    return res


# --------------------------------------------------------------------------- #
# Etapa completa                                                              #
# --------------------------------------------------------------------------- #
def correr_etapa(pob: dict, *, client_real, cache_dir: Path = en.CACHE_DIR,
                 trazas_dir: Path = en.TRAZAS_DIR, tope_usd: float | None,
                 grafos=None, reps: int = en.REPS_AGENTE) -> dict:
    grafos = list(grafos or en.GRAFOS)
    total = sum(len(en.casos_agente(pob, g)) for g in grafos) * reps
    estado = None if tope_usd is None else {"gastado": 0.0, "corridos": 0, "total": total,
                                             "tope_usd": tope_usd}
    frenado = False
    for g in grafos:
        for rep in range(1, reps + 1):
            correr_grafo_rep(pob, g, rep, client_real=client_real, cache_dir=cache_dir,
                             trazas_dir=trazas_dir, estado_gasto=estado)
            if estado and estado["corridos"] >= 3 and \
                    estado["gastado"] / estado["corridos"] * estado["total"] > tope_usd:
                print("Etapa detenida por freno de proyección.", flush=True)
                frenado = True
                break
        if frenado:
            break
    return {"estado_gasto": estado, "frenado_por_proyeccion": frenado, "total_previsto": total}


def main() -> int:
    ap = argparse.ArgumentParser(description="Re-corridas N=3 del agente (encadenamiento EV2, fase B)")
    ap.add_argument("--autorizado-fase-b", action="store_true")
    ap.add_argument("--tope-agente", type=float, default=None, help="tope USD de ESTA etapa (freno por proyección)")
    ap.add_argument("--precio-in", type=float, default=None)
    ap.add_argument("--precio-out", type=float, default=None)
    ap.add_argument("--precio-cw", type=float, default=None, help="USD/MTok cache write")
    ap.add_argument("--precio-cr", type=float, default=None, help="USD/MTok cache read")
    ap.add_argument("--solo-resumen", action="store_true", help="índice + gasto sin llamar a la API")
    args = ap.parse_args()

    precios = None
    if None not in (args.precio_in, args.precio_out, args.precio_cw, args.precio_cr):
        precios = {"in": args.precio_in, "out": args.precio_out, "cw": args.precio_cw, "cr": args.precio_cr}

    sellos = en.verificar_sellos(verbose=True)
    pob = en.cargar_poblacion()
    if args.solo_resumen:
        res = escribir_resumen(pob, en.TRAZAS_DIR, en.CACHE_DIR, en.REPS_AGENTE, precios)
        print(json.dumps({k: v for k, v in res.items() if k != "gasto_dbs"} | {"gasto_total": res["gasto_dbs"]["total"],
                          "hits_total": res["gasto_dbs"]["hits_total"]}, ensure_ascii=False, indent=2))
        return 0
    if not args.autorizado_fase_b or args.tope_agente is None:
        print("ABORTADO: la fase B exige --autorizado-fase-b y --tope-agente <USD>. Nada se llamó.")
        return 2
    en.escribir_sellos("sellos_inicio_faseB_agente.txt")
    real = rv._real_client()
    print(f"población: {pob['n_pares']} pares × {en.REPS_AGENTE} reps = {pob['n_corridas_agente']} corridas | "
          f"tope etapa USD {args.tope_agente}", flush=True)
    r = correr_etapa(pob, client_real=real, tope_usd=args.tope_agente)
    res = escribir_resumen(pob, en.TRAZAS_DIR, en.CACHE_DIR, en.REPS_AGENTE, precios,
                           extra={"tope_agente_usd": args.tope_agente, "corrida": r})
    fin = en.escribir_sellos("sellos_fin_faseB_agente.txt")
    if en.verificar_sellos() != sellos:
        raise RuntimeError("sellos cambiaron durante la corrida")
    print(json.dumps({"corrida": r, "indice": res["indice"], "gasto_total": res["gasto_dbs"]["total"],
                      "hits_total": res["gasto_dbs"]["hits_total"], "sellos_fin": en.rel_repo(fin)},
                     ensure_ascii=False, indent=2))
    return 1 if r["frenado_por_proyeccion"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
