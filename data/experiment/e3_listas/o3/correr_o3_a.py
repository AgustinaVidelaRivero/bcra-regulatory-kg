"""U-E3-LISTAS, O3 (a): E3 corregido, primera verificación sin ratchet, sobre las 20 unidades afectadas de la tanda 0.

Lo que hace:
  - Importa el código de E3 de UNA COPIA del commit de O2 (`--copia`, armada con git archive): la NOTA del ítem, D1 y
    D2. Nada del código de E3 se toca.
  - Para cada unidad de la lista sellada de O1 (`--lista`, sha256 controlado), arma el mensaje de E3 con la extracción
    que E3 vio en la verificación del intento 0 de la tanda 0 (`extracciones_e1.jsonl`, la validación) y controla que su
    sha256 sea el de la medición de O2 (`--medicion-o2`, universo r2b con la marca). Si una unidad no coincide, frena
    antes de toda llamada.
  - Con `--seco`, solo controla y estima el costo; con `--correr`, llama a E3 en secuencia (decisión 4), con
    `cliente_e3.ClienteE3Real`, el modelo y los precios de E3 de la tanda 0 (`runner_corpus.MODEL_E3`, `P_E3`, leídos de
    la fuente sin importar el runner), una base PROPIA (`--db`) y el tope duro (`--tope`); el usage de cada respuesta
    real va a `logs/cache_usage.jsonl` del repo (decisión 3). Sin ratchet: una sola verificación por unidad; el veredicto
    se evalúa con `ratchet_e3.evaluar_veredicto` (citas con la marca r2, D1), sin reintento.
  - Escribe, en `--salida`: `respuestas_e3_o3.jsonl` (tool input crudo, stop_reason, usage, costo por llamada),
    `evaluacion_e3_o3.jsonl` y `presupuesto.json` (gasto acumulado después de cada llamada).

Uso (desde cualquier lugar; la clave se carga de data/experiment/evaluacion/.env del repo y no se imprime):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B correr_o3_a.py --repo <repo> --copia <copia de O2> --lista <lista>
      --medicion-o2 <medicion jsonl> --salida <dir> --db <db> --tope 1.0 (--seco | --correr)
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

LISTA_SHA256 = "cc6b0cd6c56831c486d60bf7da64712cea391a1eb2948eef822448567df9bab6"
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")


def jl(p: Path) -> list[dict]:
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()] if p.exists() else []


def constantes_runner(runner: Path) -> dict:
    """MODEL_E3 y P_E3 de runner_corpus.py, leídos de la fuente (sin importar el runner)."""
    out = {}
    for n in ast.parse(runner.read_text(encoding="utf-8")).body:
        if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Name) and n.targets[0].id in ("MODEL_E3", "P_E3"):
            v = n.value
            if isinstance(v, ast.Call) and getattr(v.func, "id", None) == "dict" and not v.args:  # P_E3 = dict(...)
                out[n.targets[0].id] = {kw.arg: ast.literal_eval(kw.value) for kw in v.keywords}
            else:
                out[n.targets[0].id] = ast.literal_eval(v)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, required=True)
    ap.add_argument("--copia", type=Path, required=True)
    ap.add_argument("--lista", type=Path, required=True)
    ap.add_argument("--medicion-o2", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    ap.add_argument("--db", type=Path, required=True)
    ap.add_argument("--tope", type=float, default=1.0)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--seco", action="store_true")
    g.add_argument("--correr", action="store_true")
    a = ap.parse_args()
    repo, copia = a.repo.resolve(), a.copia.resolve()
    if copia == repo or repo in copia.parents:
        raise SystemExit("el código se importa de una copia, no del repo")
    if a.tope > 1.0:
        raise SystemExit("el tope de O3 es USD 1")
    if hashlib.sha256(a.lista.read_bytes()).hexdigest() != LISTA_SHA256:
        raise SystemExit("la lista sellada no tiene el sha256 cc6b0cd6…")
    rex = copia / "data" / "experiment" / "reextraccion_v2"
    sys.path.insert(0, str(rex / "e3_verificador"))
    import prompt_e3 as P  # noqa: E402  (candados del prefijo y del mensaje de E3, con la fixture de O2)
    import comun_e3  # noqa: E402
    import cliente_e3  # noqa: E402
    import ratchet_e3  # noqa: E402
    assert Path(P.__file__).resolve().is_relative_to(copia) and hasattr(P, "NOTA_E3_ITEM_LISTA")
    k = constantes_runner(rex / "corpus_v2" / "runner_corpus.py")
    model_e3, precios = k["MODEL_E3"], k["P_E3"]
    lista = json.loads(a.lista.read_text(encoding="utf-8"))
    unidades = [u["chunk_id"] for u in lista["unidades"]]
    assert len(unidades) == len(set(unidades)) == 20
    med = {r["chunk_id"]: r for r in jl(a.medicion_o2) if r.get("universo") == "r2b" and r.get("con_marca_r2")}
    sr, e0 = rex / "corpus_tanda0" / "salida_r2b", rex / "e0_chunking" / "salida_tanda0_r2b"
    casos, control = [], []
    for cid in unidades:
        to = cid.split("::")[0]
        ch = {c["id"]: c for c in json.loads((e0 / f"chunks_{to}.json").read_text(encoding="utf-8"))}
        c = ch[cid]
        val = {r["chunk_id"]: r for r in jl(sr / to / "extracciones_e1.jsonl")}[cid]["validacion"]
        msg = P.build_user_message(c, val)
        sha = hashlib.sha256(msg.encode("utf-8")).hexdigest()
        ok = sha == (med.get(cid) or {}).get("sha_msg")
        control.append({"chunk_id": cid, "sha_msg": sha, "igual_a_la_medicion_de_o2": ok, "len_msg": len(msg),
                        "forma_r2": val.get("forma_salida") == "r2", "es_item": bool(comun_e3.indices_bloque_lista(c))})
        unidades_to = {x["unidad"] for x in ch.values()}
        casos.append((cid, c, val, unidades_to))
    a.salida.mkdir(parents=True, exist_ok=True)
    # estimación: con la tarifa de E3 observada en la tanda 0 (resúmenes de E3 de los diez TOs) y el mensaje de cada unidad
    st = [json.loads((sr / to / "resumen_e3.json").read_text(encoding="utf-8"))["cliente_e3"] for to in TOS]
    llam = sum(x["llamadas"] for x in st)
    cs = {k2: sum(x["cache_stats"][k2] for x in st) for k2 in ("tokens_in", "tokens_out", "cache_read", "cache_write")}
    marg = json.loads((Path(__file__).resolve().parent / "razon_tokens_e1.json").read_text(encoding="utf-8"))
    tok_msg = [marg["a_tokens_fijos"] + marg["b_tokens_por_char"] * x["len_msg"] for x in control]
    prefijo = round(cs["cache_read"] / llam)  # tokens del prefijo leídos de la caché por llamada en la tanda 0
    salida_media = cs["tokens_out"] / llam
    est = {"llamadas": len(casos), "modelo": model_e3, "precios_por_mtok": precios,
           "tanda0_e3": {"llamadas": llam, **cs, "prefijo_por_llamada": prefijo, "salida_media": round(salida_media, 1)},
           "tokens_mensaje_estimados": round(sum(tok_msg)),
           "usd_sin_escritura_del_prefijo": round((sum(tok_msg) * precios["precio_in_por_mtok"]
                                                   + len(casos) * prefijo * precios["precio_cache_read_por_mtok"]
                                                   + len(casos) * salida_media * precios["precio_out_por_mtok"]) / 1e6, 4),
           "usd_si_la_primera_escribe_el_prefijo": round(prefijo * (precios["precio_cache_write_por_mtok"]
                                                                    - precios["precio_cache_read_por_mtok"]) / 1e6, 4)}
    est["usd_estimado_total"] = round(est["usd_sin_escritura_del_prefijo"] + est["usd_si_la_primera_escribe_el_prefijo"], 4)
    (a.salida / "control_mensajes_o2.json").write_text(json.dumps(control, ensure_ascii=False, indent=1) + "\n",
                                                       encoding="utf-8")
    (a.salida / "estimacion_o3.json").write_text(json.dumps(est, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"mensajes_iguales_a_o2": sum(x["igual_a_la_medicion_de_o2"] for x in control), "de": len(control),
                      "estimacion_usd": est["usd_estimado_total"], "modelo": model_e3}, ensure_ascii=False))
    if not all(x["igual_a_la_medicion_de_o2"] and x["forma_r2"] and x["es_item"] for x in control):
        raise SystemExit("FRENO: algún mensaje no es el de la medición de O2 (o la unidad no es un ítem r2)")
    if a.seco:
        return 0
    if est["usd_estimado_total"] > a.tope:
        raise SystemExit("FRENO: la estimación supera el tope")
    from dotenv import load_dotenv  # noqa: PLC0415
    import os  # noqa: PLC0415
    load_dotenv(repo / "data" / "experiment" / "evaluacion" / ".env")
    if not os.environ.get("ANTHROPIC_API_KEY", "").strip():
        raise SystemExit("falta la clave de la API en data/experiment/evaluacion/.env")
    cliente_e3.CACHE_USAGE_LOG = repo / "logs" / "cache_usage.jsonl"  # decisión 3: el log del repo, no el de la copia
    cli = cliente_e3.ClienteE3Real(**precios, tope_usd=a.tope, run_label="UE3_LISTAS_O3", db_path=a.db.resolve())
    pres = {"tope_usd": a.tope, "modelo": model_e3, "precios_por_mtok": precios, "llamadas": []}
    resp_p, eval_p = a.salida / "respuestas_e3_o3.jsonl", a.salida / "evaluacion_e3_o3.jsonl"
    for p in (resp_p, eval_p):
        if p.exists():
            raise SystemExit(f"{p.name} ya existe: no se pisa (la base propia devuelve los hits sin pagar)")
    try:
        for cid, c, val, unidades_to in casos:
            antes = cli.gasto_usd
            st0 = dict(cli.cache._stats)
            crudo = cliente_e3.verificar_chunk(cli, c, val, model=model_e3)
            st1 = cli.cache._stats
            uso = {k2: st1[k2] - st0[k2] for k2 in ("tokens_in", "tokens_out", "cache_read", "cache_write")}
            fue_hit = st1["hits"] > st0["hits"]
            reg = {"chunk_id": cid, **crudo, "usage_delta": uso, "hit_cache_local": fue_hit,
                   "usd": round(cli.gasto_usd - antes, 6), "usd_acumulado": round(cli.gasto_usd, 6),
                   "hora": datetime.now(timezone.utc).isoformat(timespec="seconds")}
            with resp_p.open("a", encoding="utf-8") as f:
                f.write(json.dumps(reg, ensure_ascii=False) + "\n")
            ev = ratchet_e3.evaluar_veredicto(crudo["tool_input"], c, unidades_to, val)
            with eval_p.open("a", encoding="utf-8") as f:
                f.write(json.dumps({"chunk_id": cid, "evaluacion": ev}, ensure_ascii=False) + "\n")
            pres["llamadas"].append({k2: reg[k2] for k2 in ("chunk_id", "usd", "usd_acumulado", "hit_cache_local", "hora")})
            pres["gasto_usd"] = round(cli.gasto_usd, 6)
            (a.salida / "presupuesto.json").write_text(json.dumps(pres, ensure_ascii=False, indent=1) + "\n",
                                                       encoding="utf-8")
            print(f"{cid}: USD {reg['usd']:.4f} (acumulado {cli.gasto_usd:.4f}) stop={crudo['stop_reason']} "
                  f"faltantes={len(ev['faltantes'])} bloqueantes={len(ev['faltantes_bloqueantes'])}")
    except cliente_e3.TopeExcedido as exc:
        pres["freno"] = str(exc)
        (a.salida / "presupuesto.json").write_text(json.dumps(pres, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print("FRENO por tope:", exc)
        return 2
    finally:
        pres["resumen_cliente"] = cli.resumen()
        (a.salida / "presupuesto.json").write_text(json.dumps(pres, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        cli.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
