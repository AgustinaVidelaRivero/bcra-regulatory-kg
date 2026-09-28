"""
reextraccion_dirigida_tanda0.py — U-TANDA0-2A-DIR: re-extracción dirigida de
las tres unidades de cap que E2 de la tanda 0 dejó sin extraer (ad6d5ad),
antes de la etapa E3 (ensamblados) de U-TANDA0-2A.

Contexto. En E2 las tres unidades cortaron a 8.192 tokens de salida y el
reintento por corte a 32.768 (cliente_e1.py:60) fue rechazado por la guarda
del SDK antes de salir a la red (3.600 × 32.768 / 128.000 = 921,6 s > 600 s):
quedaron como errores definitivos en cap/resumen_e1.json. A 16.384 la guarda
no actúa (460,8 s).

Réplica de la lógica de corpus_v2/reextraccion_dirigida.py (5273c0c), que NO
se corre ni se edita (escribe en corpus_v2/salida, aborta por su assert de
fase cerrada y arma el request con el prompt v2, el validador sin esquema y el
ratchet sin perfil). Diferencias contra ese script, todas por mandato:
  - runner_corpus.configurar con el manifiesto tanda0_10tos.json: perfil
    v3_b54, E0 de salida_tanda0, censo sin oráculo;
  - request E1 = PERFIL.build_request_kwargs(chunk, model=MODEL_E1,
    max_tokens=16384): el MISMO request de E2 con solo max_tokens cambiado
    (probado por clave de caché en --prueba-request);
  - validar_salida con esquema=PERFIL.esquema y ciclo_ratchet con
    perfil=PERFIL;
  - clientes E1 y de reintentos con prefijo_hash del perfil (namespace v3,
    como runner_corpus.py:800-803 y :820-824); run_label propios;
  - tope USD 1,00 COMPARTIDO por los tres clientes (PresupuestoCompartido,
    runner_corpus.py:149) sobre presupuesto_reextraccion_dirigida.json, más la
    guarda pre-unidad del runner (runner_corpus.py:466 y :614) con el
    margen_unidad_usd del manifiesto;
  - solo las tres unidades de cap (sin los tres casos de reintento marcado
    de r1, que en la tanda 0 no existen);
  - salida: corpus_tanda0/salida_dirigida/ (copia completa de salida/, D1.a).
    corpus_tanda0/salida/ y corpus_v2/ quedan vedados por guarda de ruta.

Una sola llamada E1 por unidad, SIN reintento por corte: si la respuesta a
16.384 vuelve a cortar, la unidad va a cola humana con su expediente (el
error se registra como max_tokens_hit_tras_reintento, el marcador definitivo
del runner vigente, runner_corpus.py:486-488; max_tokens_hit queda reservado
para el reintentable pendiente, runner_corpus.py:411-422).

Persistencia sobre la copia, como r1: append a cap/extracciones_e1.jsonl y
cap/finales.jsonl (last-wins), veredictos y cola por RegistroE3, fase
reextraccion_dirigida en estado_corpus.json, compactar_e1 y cerrar_e2 solo de
cap, resumen en reextraccion_dirigida.json. Reanudable: una unidad con
registro E1 dirigido y registro en finales se saltea; lo ya pagado es hit de
la caché local.

Caching (docs/decisiones_caching_extraccion.md): el request lo construye el
perfil sellado (system en bloque con cache_control, D1); gasto con la fórmula
de caching (D2) en los clientes y en --gasto-dbs; los clientes loguean usage
(D3); llamadas secuenciales (D4); el pipeline de evaluación no se toca (D5).

Uso (siempre con PYTHONDONTWRITEBYTECODE=1 y .venv/bin/python):
  reextraccion_dirigida_tanda0.py --prueba-request        # D1.c, sin red
  reextraccion_dirigida_tanda0.py --autorizado-tope 1.0   # D2, corrida real
  reextraccion_dirigida_tanda0.py --gasto-dbs             # D2.b, sin red
  reextraccion_dirigida_tanda0.py --registro-modelos      # D2.c, sin red
"""

from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
import time
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).resolve().parent                    # tanda0/code
REPO = AQUI.parents[3]                                    # raíz del repo
REX = REPO / "data" / "experiment" / "reextraccion_v2"
CORPUS_V2 = REX / "corpus_v2"
if str(CORPUS_V2) not in sys.path:
    sys.path.insert(0, str(CORPUS_V2))

import runner_corpus as rc          # noqa: E402  (agrega e1/e2/e3 y REX al path)
import manifiesto_corpus            # noqa: E402
import comun_e1                     # noqa: E402
import cliente_e1                   # noqa: E402
import cliente_e3                   # noqa: E402
import validador_e1                 # noqa: E402
import ratchet_e3                   # noqa: E402
import llm_cache as lc              # noqa: E402  (solo import; sellado)

MANIFIESTO = REX / "manifiestos" / "tanda0_10tos.json"
rc.configurar(manifiesto_corpus.cargar(MANIFIESTO))
PERFIL = rc.PERFIL
if PERFIL.nombre != "v3_b54" or rc.E0_DIR != REX / "e0_chunking" / "salida_tanda0":
    raise RuntimeError(f"configuración inesperada: perfil {PERFIL.nombre}, "
                       f"E0 {rc.E0_DIR} — se frena")

import prompt_v3_b54 as _v3         # noqa: E402  (en path vía perfil_e1; sellado)

TO = "cap"
CASOS = ("cap::3.1.14.1", "cap::4.2.1.2", "cap::4.3.3.1")
MODO = "max_tokens_16384"
MAX_TOKENS_DIRIGIDA = rc.MAX_TOKENS_REINTENTO            # runner_corpus.py:87
MAX_TOKENS_E2 = _v3.MAX_OUTPUT_TOKENS                    # techo del request base de E2
assert MAX_TOKENS_DIRIGIDA == 16384 and MAX_TOKENS_E2 == 8192

TOPE_USD = 1.00
SALIDA_E2 = REX / "corpus_tanda0" / "salida"             # E2 commiteada: solo lectura
SALIDA = REX / "corpus_tanda0" / "salida_dirigida"
PRESUPUESTO = "presupuesto_reextraccion_dirigida.json"
RESUMEN = "reextraccion_dirigida.json"
FASE = "reextraccion_dirigida"
RUN_LABELS = {"e1": "tanda0_dirigida_e1", "e3": "tanda0_dirigida_e3",
              "reint": "tanda0_dirigida_reint"}
ERROR_CORTE = "max_tokens_hit_tras_reintento"
ESTADO_COLA = "cola_humana_reextraccion_dirigida"

DBS = {"e1": cliente_e1.DB_PATH, "e3": cliente_e3.DB_PATH,
       "reint": rc.DB_REINTENTOS_E1}
PRECIOS = {"e1": rc.P_E1, "e3": rc.P_E3, "reint": rc.P_E1}
REGISTRO_MODELOS = REPO / "reports" / "tanda0" / "registro_modelos_2a_dirigida.json"

# Filas de E2 con las que se prueba la identidad del request (D1.c).
RUN_LABEL_E2 = "corpus_cap_e1"
FECHA_E2 = "2026-09-27"


# ----------------------------- request ----------------------------------- #
def construir_request(chunk: dict, max_tokens: int = MAX_TOKENS_DIRIGIDA) -> dict:
    """Request E1 del chunk con el perfil de la corrida: el de E2 con solo
    max_tokens cambiado (el techo no integra el prefijo cacheado)."""
    return PERFIL.build_request_kwargs(chunk, model=rc.MODEL_E1,
                                       max_tokens=max_tokens)


def namespace_e1() -> str:
    return cliente_e1.namespace_e1(prefijo_hash=PERFIL.prefijo_hash_para_namespace)


def clave(kwargs: dict, namespace: str | None = None) -> str:
    return lc.compute_key(namespace or namespace_e1(), lc.canonical_request(kwargs))


def cargar_cap() -> tuple[list[dict], dict[str, dict]]:
    chunks = comun_e1.cargar_chunks((TO,), e0_dir=rc.E0_DIR)
    por_id = {c["id"]: c for c in chunks}
    faltan = [cid for cid in CASOS if cid not in por_id]
    if faltan:
        raise RuntimeError(f"unidades ausentes del E0 de la tanda 0: {faltan}")
    return chunks, {cid: por_id[cid] for cid in CASOS}


def _crear(cliente, kwargs: dict, doc: str):
    """Una llamada, sin reintento por corte (nunca crear_con_reintento_corte:
    re-llamaría a 32.768 y la guarda del SDK la rechazaría de nuevo)."""
    if isinstance(cliente, cliente_e1.ClienteE1Real):
        return cliente.create(doc=doc, **kwargs)
    return cliente.messages.create(**kwargs)


# ----------------------------- guardas ----------------------------------- #
def validar_salida_dir(salida: Path) -> Path:
    s = Path(salida).resolve()
    for vedada in (SALIDA_E2.resolve(), CORPUS_V2.resolve()):
        if s == vedada or vedada in s.parents:
            raise RuntimeError(f"salida vedada por mandato: {s}")
    if not (s / "estado_corpus.json").is_file() or not (s / TO).is_dir():
        raise RuntimeError(f"{s} no es una copia completa de corpus_tanda0/salida/")
    return s


def construir_clientes(guardian, tope_usd: float = TOPE_USD,
                       dbs: dict[str, Path] | None = None) -> dict:
    """Los tres clientes reales, con el guardián COMPARTIDO. `dbs` solo se
    sobreescribe en el selftest (dbs temporales; en la corrida, las de
    siempre: never-pay-twice)."""
    dbs = dict(DBS) if dbs is None else dbs
    ph = PERFIL.prefijo_hash_para_namespace
    return {
        "e1": cliente_e1.ClienteE1Real(
            **rc.P_E1, tope_usd=tope_usd, run_label=RUN_LABELS["e1"],
            db_path=dbs["e1"], guardian=guardian, prefijo_hash=ph),
        "e3": cliente_e3.ClienteE3Real(
            **rc.P_E3, tope_usd=tope_usd, run_label=RUN_LABELS["e3"],
            db_path=dbs["e3"], guardian=guardian),
        "reint": cliente_e1.ClienteE1Real(
            **rc.P_E1, tope_usd=tope_usd, run_label=RUN_LABELS["reint"],
            db_path=dbs["reint"], guardian=guardian, prefijo_hash=ph),
    }


# ----------------------------- corrida ----------------------------------- #
def _usage(resp) -> dict:
    u = resp.usage
    return {"input_tokens": getattr(u, "input_tokens", 0) or 0,
            "output_tokens": getattr(u, "output_tokens", 0) or 0,
            "cache_write_tokens": getattr(u, "cache_creation_input_tokens", 0) or 0,
            "cache_read_tokens": getattr(u, "cache_read_input_tokens", 0) or 0}


def _desenlace_persistido(fin: dict, e1: dict) -> dict:
    val_f = fin.get("validacion_final")
    val_e1 = e1.get("validacion") or {}
    cola = fin["estado"] == ESTADO_COLA
    d = {"modo": MODO, "resultado": "cola_humana" if cola else fin["estado"],
         "n_reintentos": fin.get("n_reintentos", 0),
         "residuales": len(fin.get("residuales") or []),
         "stop_reason_e1": e1.get("stop_reason"), "usage_e1": e1.get("usage"),
         "entidades_e1": len(val_e1.get("entidades", [])),
         "relaciones_e1": len(val_e1.get("relaciones", []))}
    if val_f is not None:
        d["entidades_final"] = len(val_f.get("entidades", []))
        d["relaciones_final"] = len(val_f.get("relaciones", []))
    if cola:
        d["estado_finales"] = ESTADO_COLA
        d["motivo"] = e1.get("error")
    return d


def correr(salida: Path, clientes: dict, guardian, *,
           tope_usd: float = TOPE_USD,
           margen_unidad_usd: float | None = None) -> dict:
    """Re-extracción dirigida sobre `salida`. Devuelve el resumen; ante tope
    agotado o falla de API sin resolver levanta rc.Freno / TopeExcedido con
    el estado persistido y SIN cerrar la fase (relanzar reanuda)."""
    salida = validar_salida_dir(salida)
    margen = rc.MARGEN_UNIDAD_USD if margen_unidad_usd is None else margen_unidad_usd
    tdir = salida / TO
    estado = rc.Estado(salida)
    if estado.fase_cerrada(FASE):
        raise RuntimeError("la re-extracción dirigida ya corrió (fase cerrada en el ledger)")

    chunks, casos = cargar_cap()
    unidades_corpus = {c["unidad"] for c in chunks}
    regs_e1 = rc.cargar_jsonl_last_wins(tdir / "extracciones_e1.jsonl")
    finales = rc.cargar_jsonl_last_wins(tdir / "finales.jsonl")
    hechas = {cid for cid in CASOS
              if "reextraccion_dirigida" in regs_e1.get(cid, {}) and cid in finales}
    for cid in CASOS:
        if cid in hechas or "reextraccion_dirigida" in regs_e1.get(cid, {}):
            continue
        if cid not in regs_e1 or regs_e1[cid].get("error") is None or cid in finales:
            raise RuntimeError(f"precondición: {cid} no figura como error de E1 "
                               f"sin verificar en {tdir}")

    cli_e1, cli_e3, cli_re = clientes["e1"], clientes["e3"], clientes["reint"]
    registro = ratchet_e3.RegistroE3(tdir)
    desenlaces: dict[str, dict] = {}
    t0 = time.time()
    for cid in CASOS:
        if cid in hechas:
            desenlaces[cid] = _desenlace_persistido(finales[cid], regs_e1[cid])
            print(f"[{cid}] ya persistida por esta fase — se saltea", flush=True)
            continue
        if guardian.gasto_usd + margen > tope_usd:
            raise rc.Freno(f"tope compartido antes de {cid}: gasto USD "
                           f"{guardian.gasto_usd:.4f} + margen {margen} > {tope_usd}")
        chunk = casos[cid]
        kwargs = construir_request(chunk)
        resp, err_api = rc.llamar_con_reintentos_api(
            lambda: _crear(cli_e1, kwargs, chunk["archivo"]), cid)
        if resp is None:
            raise rc.Freno(f"{cid}: llamada E1 falló tras reintentos de API ({err_api})")
        usage = _usage(resp)
        stop = getattr(resp, "stop_reason", None)
        tool_input = next((b.input for b in resp.content
                           if getattr(b, "type", None) == "tool_use"), None)
        err = None
        if tool_input is None:
            err = f"no_tool_use stop_reason={stop}"
        elif stop == "max_tokens":
            err = ERROR_CORTE
        val = (validador_e1.validar_salida(tool_input, chunk,
                                           esquema=PERFIL.esquema).as_dict()
               if tool_input is not None else None)
        rechazo_chunk = bool(val and any(r["nivel"] == "chunk" for r in val["rechazos"]))

        rc.append_jsonl(tdir / "extracciones_e1.jsonl", {
            "chunk_id": cid, "unidad": chunk["unidad"],
            "tipo_unidad": chunk["tipo"], "titulo": chunk["titulo"],
            "stop_reason": stop,
            "error": err or ("reextraccion_dirigida_invalida" if rechazo_chunk else None),
            "reextraccion_dirigida": MODO,
            "usage": usage, "tool_input_crudo": tool_input, "validacion": val})

        if err or val is None or rechazo_chunk:
            motivo = err or "; ".join(r["motivo"] for r in val["rechazos"]
                                      if r["nivel"] == "chunk")
            registro.cola_humana(cid, ESTADO_COLA, {
                "faltantes": [],
                "incoherencias": [f"re-extracción dirigida falló: {motivo}"]})
            rc.append_jsonl(tdir / "finales.jsonl", {
                "chunk_id": cid, "tipo_unidad": chunk["tipo"],
                "estado": ESTADO_COLA, "n_reintentos": 0, "residuales": [],
                "validacion_final": None})
            desenlaces[cid] = {"modo": MODO, "resultado": "cola_humana",
                               "estado_finales": ESTADO_COLA, "motivo": motivo,
                               "stop_reason_e1": stop, "usage_e1": usage}
            print(f"[{cid}] FALLÓ de nuevo ({motivo}) → cola humana "
                  f"| gasto combinado USD {guardian.gasto_usd:.4f}", flush=True)
            continue

        exp, err_r = rc.llamar_con_reintentos_api(
            lambda: ratchet_e3.ciclo_ratchet(
                chunk, val, cliente_verificador=cli_e3, cliente_extractor=cli_re,
                model_e3=rc.MODEL_E3, model_e1=rc.MODEL_E1, registro=registro,
                max_tokens_reintento=rc.MAX_TOKENS_REINTENTO,
                unidades_corpus=unidades_corpus, perfil=PERFIL), cid)
        if exp is None:
            raise rc.Freno(f"{cid}: ciclo de ratchet falló tras reintentos de API "
                           f"({err_r}) — relanzar reanuda acá")
        rc.append_jsonl(tdir / "finales.jsonl", {
            "chunk_id": cid, "tipo_unidad": chunk["tipo"],
            "estado": exp["estado"], "n_reintentos": len(exp["reintentos"]),
            "residuales": exp["residuales"],
            "validacion_final": exp["validacion_final"]})
        vf = exp["validacion_final"]
        desenlaces[cid] = {
            "modo": MODO, "resultado": exp["estado"],
            "n_reintentos": len(exp["reintentos"]),
            "residuales": len(exp["residuales"]),
            "stop_reason_e1": stop, "usage_e1": usage,
            "entidades_e1": len(val["entidades"]),
            "relaciones_e1": len(val["relaciones"])}
        if vf is not None:
            desenlaces[cid]["entidades_final"] = len(vf["entidades"])
            desenlaces[cid]["relaciones_final"] = len(vf["relaciones"])
        print(f"[{cid}] validación OK ({len(val['entidades'])} ent / "
              f"{len(val['relaciones'])} rel) → E3: {exp['estado']} "
              f"| gasto combinado USD {guardian.gasto_usd:.4f}", flush=True)

    # E2 de cap (fan-in estricto) sobre la copia; el ensamblado es de la
    # etapa E3 de U-TANDA0-2A, aparte.
    rc.compactar_e1(TO, salida)
    rep = rc.cerrar_e2(TO, salida)
    resumen = {
        "unidad": "U-TANDA0-2A-DIR", "manifiesto": MANIFIESTO.name,
        "perfil_e1": PERFIL.nombre, "namespace_e1": namespace_e1(),
        "max_tokens": MAX_TOKENS_DIRIGIDA, "run_labels": RUN_LABELS,
        "casos": desenlaces,
        "gasto_combinado_usd": round(guardian.gasto_usd, 6),
        "tope_usd": tope_usd, "margen_unidad_usd": margen,
        "clientes": {k: c.resumen() for k, c in clientes.items()},
        "e2_cap": {"nodes_total": rep["nodes_total"], "edges_total": rep["edges_total"],
                   "sha256_grafo": rep["sha256_grafo"], "fanin": rep["fanin"]},
        "wall_min": round((time.time() - t0) / 60, 1)}
    (salida / RESUMEN).write_text(json.dumps(resumen, ensure_ascii=False, indent=1),
                                  encoding="utf-8")
    estado.d["fases_cerradas"][FASE] = {
        "gasto_usd": round(guardian.gasto_usd, 6),
        "resumen": {"n": len(desenlaces),
                    "desenlaces": {k: v["resultado"] for k, v in desenlaces.items()}}}
    estado.persistir()
    return resumen


# ----------------------------- lectura de dbs (sin red) ------------------ #
def _abrir_ro(db: Path) -> sqlite3.Connection:
    """Solo lectura sin archivos laterales (immutable): las dbs no tienen
    -wal pendiente y nadie escribe durante la lectura."""
    if Path(str(db) + "-wal").exists():
        raise RuntimeError(f"{db} tiene -wal pendiente: lectura immutable no fiable")
    con = sqlite3.connect(f"file:{db}?immutable=1", uri=True)
    con.row_factory = sqlite3.Row
    return con


def _punto_de_request(request_json: str) -> str | None:
    msg = json.loads(request_json)["messages"][0]["content"]
    for linea in msg.splitlines():
        if linea.startswith("Punto del chunk:"):
            return linea.split(":", 1)[1].strip().split(" ", 1)[0]
    return None


def prueba_request(dbs: dict[str, Path] | None = None) -> dict:
    """D1.c: la clave del request del módulo a 8.192 debe coincidir con la de
    la fila de e1_extraccion.db (run_label corpus_cap_e1, stop_reason
    max_tokens, 27/09/2026) de la misma unidad. La unidad de cada fila se lee
    de su request_json, no de la clave (sin circularidad)."""
    dbs = dict(DBS) if dbs is None else dbs
    _, casos = cargar_cap()
    ns = namespace_e1()
    con = _abrir_ro(dbs["e1"])
    filas = con.execute(
        "SELECT DISTINCT c.key, c.namespace, c.created_at, c.stop_reason, "
        "c.request_json FROM cache c JOIN access_log a ON a.key = c.key "
        "WHERE a.run_label = ? AND c.stop_reason = 'max_tokens' "
        "AND c.created_at LIKE ? ORDER BY c.created_at",
        (RUN_LABEL_E2, FECHA_E2 + "%")).fetchall()
    por_unidad = {f"{TO}::{_punto_de_request(f['request_json'])}": f for f in filas}
    out = {"namespace_modulo": ns, "n_filas_db": len(filas), "unidades": {}}
    for cid, chunk in casos.items():
        k8 = clave(construir_request(chunk, MAX_TOKENS_E2), ns)
        k16 = clave(construir_request(chunk, MAX_TOKENS_DIRIGIDA), ns)
        f = por_unidad.get(cid)
        d = {"clave_modulo_8192": k8, "clave_db": f["key"] if f else None,
             "coinciden": bool(f) and k8 == f["key"]}
        if f:
            d.update({"created_at_db": f["created_at"], "namespace_db": f["namespace"],
                      "clave_db_recomputada": lc.compute_key(f["namespace"],
                                                             f["request_json"])})
        # el request a 16.384 es nuevo: no puede estar ya pagado en la db
        d["clave_modulo_16384"] = k16
        d["clave_16384_en_db"] = con.execute(
            "SELECT COUNT(*) FROM cache WHERE key = ?", (k16,)).fetchone()[0]
        out["unidades"][cid] = d
    con.close()
    libres = {}
    for k, lab in RUN_LABELS.items():
        c = _abrir_ro(dbs[k])
        libres[lab] = c.execute("SELECT COUNT(*) FROM access_log WHERE run_label = ?",
                                (lab,)).fetchone()[0]
        c.close()
    out["accesos_previos_por_run_label"] = libres
    out["ok"] = (len(filas) == 3 and all(
        u["coinciden"] and u["clave_db_recomputada"] == u["clave_db"]
        and u["namespace_db"] == ns and u["clave_16384_en_db"] == 0
        for u in out["unidades"].values()) and not any(libres.values()))
    return out


def _filas_run_labels(dbs: dict[str, Path]) -> list[dict]:
    filas = []
    for k, lab in RUN_LABELS.items():
        con = _abrir_ro(dbs[k])
        for r in con.execute(
                "SELECT a.ts, a.run_label, a.key, a.hit, c.model, c.namespace, "
                "c.input_tokens, c.output_tokens, c.cache_write_tokens, "
                "c.cache_read_tokens, c.stop_reason, c.request_json "
                "FROM access_log a JOIN cache c ON c.key = a.key "
                "WHERE a.run_label = ? ORDER BY a.ts", (lab,)):
            filas.append({"db": k, **dict(r)})
        con.close()
    return filas


def gasto_dbs(dbs: dict[str, Path] | None = None) -> dict:
    """D2.b: gasto por run_label desde las dbs, fórmula D2 (solo misses)."""
    dbs = dict(DBS) if dbs is None else dbs
    out: dict = {"por_run_label": {}, "total_usd": 0.0}
    for f in _filas_run_labels(dbs):
        lab = f["run_label"]
        d = out["por_run_label"].setdefault(lab, {
            "db": f["db"], "accesos": 0, "misses": 0, "hits": 0, "tokens_in": 0,
            "tokens_out": 0, "cache_write": 0, "cache_read": 0, "usd": 0.0})
        d["accesos"] += 1
        if f["hit"]:
            d["hits"] += 1
            continue
        p = PRECIOS[f["db"]]
        d["misses"] += 1
        d["tokens_in"] += f["input_tokens"]
        d["tokens_out"] += f["output_tokens"]
        d["cache_write"] += f["cache_write_tokens"]
        d["cache_read"] += f["cache_read_tokens"]
        d["usd"] += (f["input_tokens"] * p["precio_in_por_mtok"]
                     + f["output_tokens"] * p["precio_out_por_mtok"]
                     + f["cache_write_tokens"] * p["precio_cache_write_por_mtok"]
                     + f["cache_read_tokens"] * p["precio_cache_read_por_mtok"]) / 1e6
    for d in out["por_run_label"].values():
        out["total_usd"] += d["usd"]
        d["usd"] = round(d["usd"], 6)
    out["total_usd"] = round(out["total_usd"], 6)
    out["tope_usd"] = TOPE_USD
    return out


def registro_modelos(dbs: dict[str, Path] | None = None) -> dict:
    """D2.c: registro de modelos por llamada de las tres run_label (formato
    de reports/tanda0/registro_modelos_2a.json)."""
    dbs = dict(DBS) if dbs is None else dbs
    filas = _filas_run_labels(dbs)
    por_llamada, agg_mod, agg_temp, agg_ns = [], Counter(), Counter(), Counter()
    for f in filas:
        rq = json.loads(f["request_json"])
        temp = ("default del proveedor" if "temperature" not in rq
                else rq["temperature"])
        por_llamada.append([f["ts"], f["run_label"], f["key"][:12], f["model"],
                            None if f["hit"] else temp, f["hit"]])
        if not f["hit"]:
            agg_mod[(f["db"], f["model"], rq["model"])] += 1
            agg_temp[(f["db"], json.dumps(temp, ensure_ascii=False))] += 1
            agg_ns[(f["db"], f["namespace"])] += 1
    def rel(p) -> str:
        p = Path(p).resolve()
        return str(p.relative_to(REPO)) if REPO in p.parents else str(p)

    return {"unidad": "U-TANDA0-2A-DIR", "etapas": {"D2": {
        "etapa": "D2",
        "filtro": {"access_log.run_label": list(RUN_LABELS.values())},
        "fuente": "cache.model (id devuelto por la API) + request_json "
                  "(temperature) de las dbs de llm_cache; access_log por run_label",
        "dbs": {k: rel(p) for k, p in dbs.items()},
        "modelos_en_codigo": {"E1": f"{rc.MODEL_E1} (runner_corpus.py:89)",
                              "E3": f"{rc.MODEL_E3} (runner_corpus.py:92)"},
        "agregado_por_modelo": [{"db": d, "modelo_segun_api": m, "modelo_pedido": mp,
                                 "n_misses": n} for (d, m, mp), n in sorted(agg_mod.items())],
        "temperatura_por_db": [{"db": d, "temperatura": json.loads(t), "n_misses": n}
                               for (d, t), n in sorted(agg_temp.items())],
        "namespaces": [{"db": d, "namespace": ns, "n_misses": n}
                       for (d, ns), n in sorted(agg_ns.items())],
        "via": "API Anthropic directa (anthropic.Anthropic(max_retries=3) "
               "envuelto en llm_cache.CachingClient)",
        "n_llamadas_total": len(filas),
        "n_hits": sum(1 for f in filas if f["hit"]),
        "n_misses": sum(1 for f in filas if not f["hit"]),
        "por_llamada": por_llamada,
        "por_llamada_columnas": ["ts", "run_label", "key12", "modelo_segun_api",
                                 "temperatura(None=hit)", "hit"]}}}


# ----------------------------- main -------------------------------------- #
def main() -> int:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--prueba-request", action="store_true")
    g.add_argument("--gasto-dbs", action="store_true")
    g.add_argument("--registro-modelos", action="store_true")
    ap.add_argument("--autorizado-tope", type=float, default=None,
                    help=f"eco de la autorización de la corrida real (= {TOPE_USD})")
    args = ap.parse_args()

    if args.prueba_request:
        r = prueba_request()
        print(json.dumps(r, ensure_ascii=False, indent=1))
        return 0 if r["ok"] else 1
    if args.gasto_dbs:
        print(json.dumps(gasto_dbs(), ensure_ascii=False, indent=1))
        return 0
    if args.registro_modelos:
        REGISTRO_MODELOS.write_text(json.dumps(registro_modelos(), ensure_ascii=False,
                                               indent=1), encoding="utf-8")
        print(f"escrito {REGISTRO_MODELOS.relative_to(REPO)}")
        return 0

    if args.autorizado_tope != TOPE_USD:
        print(f"corrida real exige --autorizado-tope {TOPE_USD} (eco de la autorización)")
        return 2
    from dotenv import load_dotenv
    load_dotenv(rc.EVAL_DIR / ".env")
    if not os.environ.get("ANTHROPIC_API_KEY", "").strip():
        print(f"ANTHROPIC_API_KEY ausente (esperada en {rc.EVAL_DIR / '.env'})")
        return 1
    salida = validar_salida_dir(SALIDA)
    guardian = rc.PresupuestoCompartido(TOPE_USD, salida / PRESUPUESTO)
    clientes = construir_clientes(guardian)
    print(f"re-extracción dirigida tanda 0 | perfil {PERFIL.nombre} | namespace "
          f"{namespace_e1()} | max_tokens {MAX_TOKENS_DIRIGIDA} | tope compartido "
          f"USD {TOPE_USD} | casos {list(CASOS)}", flush=True)
    try:
        resumen = correr(salida, clientes, guardian)
    except (rc.Freno, cliente_e1.TopeExcedido, cliente_e3.TopeExcedido) as e:
        print(f"\nFRENO: {e} | gasto combinado USD {guardian.gasto_usd:.4f}", flush=True)
        (salida / RESUMEN).write_text(json.dumps(
            {"freno": str(e), "gasto_combinado_usd": round(guardian.gasto_usd, 6),
             "tope_usd": TOPE_USD,
             "clientes": {k: c.resumen() for k, c in clientes.items()}},
            ensure_ascii=False, indent=1), encoding="utf-8")
        return 3
    finally:
        for c in clientes.values():
            c.close()
    print(json.dumps(resumen["casos"], ensure_ascii=False, indent=1))
    print(f"gasto combinado: USD {resumen['gasto_combinado_usd']} (tope {TOPE_USD}) "
          f"| grafo_cap {resumen['e2_cap']['nodes_total']} nodos / "
          f"{resumen['e2_cap']['edges_total']} aristas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
