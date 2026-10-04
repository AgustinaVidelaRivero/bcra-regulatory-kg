"""
correr_p4.py — U-PROMPT-R2, P4.b: la corrida de la prueba pareada. Tope USD 2 (decisión 18), freno duro.

Brazos (P4.b del mandato; la pareada compara release contra release):
  - brazo nuevo: perfil r2b (prefijo `3817de475c93`) sobre la e0-r2 (`salida_tanda0_r2/`, `f8dedd4`; fuera de la tanda 0,
    la de e0_fuera_p4.py). Mismo camino que `runner_corpus.fase_e1` con el perfil r2: reintento por corte a 16.384
    (cliente_e1.MAX_TOKENS_REINTENTO_CORTE_R2) y reintento por forma (C2 de U-R2-CODIGO-2, punto b). La partición por
    corte no se corre: si un chunk corta dos veces, queda con su error;
  - brazo sellado: perfil v3_b54 sobre la E0 legada. En la tanda 0 sale de la caché de la corrida (USD 0): un cliente que
    falla si la clave no está; si faltara, se toma el crudo de `salida_dirigida` y se declara. Fuera de la tanda 0 (F1 y
    fuera de muestra) corre por la API, con el reintento por corte del perfil sellado;
  - pata de E3: `ratchet_e3.ciclo_ratchet` con la NOTA y la guarda (forma r2) sobre los cuatro encabezados, con la
    validación del brazo nuevo; reintento de E1 a 16.384 (runner_corpus.MAX_TOKENS_REINTENTO).

Caching (docs/decisiones_caching_extraccion.md): D1, los requests los arman los perfiles (system con breakpoint); D2, el
gasto es el de los clientes, con la fórmula de caching; D3, cada response real deja su línea de usage
(`logs/cache_usage.jsonl` de la copia, que corre); D4, todo en serie; D5, no toca la evaluación. Las bases de caché de
P4 viven en --trabajo (`cache/`); la de la tanda 0 se lee de la copia del repo. Antes de correr se escribe
`claves_antes.json` (namespace, clave y si está en alguna base) y al final `claves_despues.json`.

Escribe solo en --trabajo. Uso (desde la raíz de una COPIA del repo; la clave de la API, de data/experiment/evaluacion/.env):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p4/correr_p4.py \
      --muestra M --e0-fuera DIR --trabajo DIR [--autorizado-tope 2.0]
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
import time
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
for sub in ("e1_extractor", "e3_verificador", "e2_reduce", "corpus_v2"):
    sys.path.insert(0, str(REX / sub))
sys.path.insert(0, str(REX))
sys.path.insert(0, str(REPO / "data" / "experiment" / "evaluacion"))
import llm_cache as lc  # noqa: E402 — capa sellada, solo import
import perfil_e1  # noqa: E402
import validador_e1  # noqa: E402
import cliente_e1  # noqa: E402
import cliente_e3  # noqa: E402
import ratchet_e3  # noqa: E402
import runner_corpus as RC  # noqa: E402 — constantes y helpers del runner, solo import

TOPE_USD = 2.0
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
FUERA = ("ayccef", "expaef", "opefci", "adrei")
CRUDO = REX / "corpus_tanda0" / "salida_dirigida"
E0_LEG = REX / "e0_chunking" / "salida_tanda0"
E0_R2 = REX / "e0_chunking" / "salida_tanda0_r2"
DB_T0 = REX / "e1_extractor" / "cache" / "e1_extraccion.db"


class _SinAPI:
    """Cliente que nunca llama a la API: un miss en la caché de la tanda 0 es un error, no un gasto."""

    class _M:
        def create(self, **kwargs):
            raise LookupError("clave ausente en la caché de la tanda 0")

    messages = _M()


def chunks(d: Path, to: str) -> dict:
    return {c["id"]: c for c in json.loads((d / f"chunks_{to}.json").read_text(encoding="utf-8"))}


def jl_last_wins(p: Path) -> dict:
    out = {}
    for x in p.read_text(encoding="utf-8").splitlines():
        if x.strip():
            r = json.loads(x)
            out[r["chunk_id"]] = r
    return out


def tool_input_de(resp):
    return next((b.input for b in resp.content if getattr(b, "type", None) == "tool_use"), None)


def en_db(db: Path, key: str) -> bool:
    if not db.exists():
        return False
    con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    try:
        return con.execute("SELECT 1 FROM cache WHERE key = ?", (key,)).fetchone() is not None
    finally:
        con.close()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--muestra", type=Path, required=True)
    ap.add_argument("--e0-fuera", type=Path, required=True)
    ap.add_argument("--trabajo", type=Path, required=True)
    ap.add_argument("--autorizado-tope", type=float, default=None)
    ap.add_argument("--solo-claves", action="store_true", help="escribe claves_antes.json y sale, sin API")
    a = ap.parse_args()
    w = a.trabajo.resolve()
    if REPO in w.parents or w == REPO:
        raise SystemExit("--trabajo no puede estar dentro del repo")
    (w / "cache").mkdir(parents=True, exist_ok=True)
    m = json.loads(a.muestra.read_text(encoding="utf-8"))
    nuevo, sellado = perfil_e1.perfil("r2b"), perfil_e1.perfil("v3_b54")
    assert nuevo.prefijo_hash == "3817de475c93", nuevo.prefijo_hash
    ns_nuevo = cliente_e1.namespace_e1(prefijo_hash=nuevo.prefijo_hash_para_namespace)
    ns_sellado = cliente_e1.namespace_e1(prefijo_hash=sellado.prefijo_hash_para_namespace)
    db_e1, db_e3, db_e1r = w / "cache" / "p4_e1.db", w / "cache" / "p4_e3.db", w / "cache" / "p4_e1_reintentos.db"

    leg, r2, crudo = {}, {}, {}
    for to in TOS:
        leg.update(chunks(E0_LEG, to))
        r2.update(chunks(E0_R2, to))
        crudo.update(jl_last_wins(CRUDO / to / "extracciones_e1.jsonl"))
    fleg, fr2 = {}, {}
    for to in FUERA:
        fleg.update(chunks(a.e0_fuera / "e0_legada", to))
        fr2.update(chunks(a.e0_fuera / "e0_r2", to))

    grupos = [("fijo", c) for c in m["fijos"]]
    grupos += [("lista", c) for v in m["listas_excepciones"].values() for c in v["tomados"]]
    grupos += [(f"sorteo:{e}", c) for e in m["sorteo"] for c in m["sorteo"][e]["elegidos"]]
    grupos += [("pata_e3", c) for c in m["pata_e3"][:3]]
    grupos += [("f1", c) for c in m["f1"]]
    grupos += [("fuera", c) for v in m["fuera_de_muestra"].values() for c in v]
    en_t0 = {c for g, c in grupos if g not in ("f1", "fuera")}

    def chunk_nuevo(cid):
        return r2[cid] if cid in en_t0 else fr2[cid]

    def chunk_sellado(cid):
        return leg[cid] if cid in en_t0 else fleg[cid]

    # ---- claves antes ----
    claves = []
    for g, cid in grupos:
        for brazo, perfil, c, ns in (("nuevo", nuevo, chunk_nuevo(cid), ns_nuevo),
                                     ("sellado", sellado, chunk_sellado(cid), ns_sellado)):
            k = lc.compute_key(ns, lc.canonical_request(perfil.build_request_kwargs(c, model=RC.MODEL_E1)))
            claves.append({"chunk_id": cid, "grupo": g, "brazo": brazo, "namespace": ns, "clave": k,
                           "en_db_tanda0": en_db(DB_T0, k), "en_db_p4": en_db(db_e1, k)})
    (w / "claves_antes.json").write_text(json.dumps(claves, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    resumen_claves: dict = {}
    for k in claves:
        r = resumen_claves.setdefault(f"{k['brazo']}:{'tanda0' if k['chunk_id'] in en_t0 else 'fuera'}",
                                      {"total": 0, "en_db_tanda0": 0, "en_db_p4": 0})
        r["total"] += 1
        r["en_db_tanda0"] += k["en_db_tanda0"]
        r["en_db_p4"] += k["en_db_p4"]
    print(json.dumps({"namespaces": {"nuevo": ns_nuevo, "sellado": ns_sellado}, "claves": resumen_claves},
                     ensure_ascii=False, indent=1), flush=True)
    if a.solo_claves:
        return 0
    if a.autorizado_tope != TOPE_USD:
        raise SystemExit(f"corrida real exige --autorizado-tope {TOPE_USD}")
    try:
        from dotenv import load_dotenv  # noqa: PLC0415
        load_dotenv(REPO / "data" / "experiment" / "evaluacion" / ".env")   # como runner_pareada_b54.py:148
    except ImportError:
        pass

    guardian = RC.PresupuestoCompartido(TOPE_USD, w / "presupuesto_p4.json")
    cli = cliente_e1.ClienteE1Real(**RC.P_E1, tope_usd=TOPE_USD, run_label="p4_pareada_e1", db_path=db_e1,
                                   guardian=guardian, prefijo_hash=nuevo.prefijo_hash_para_namespace)
    cli_s = cliente_e1.ClienteE1Real(**RC.P_E1, tope_usd=TOPE_USD, run_label="p4_pareada_e1_sellado", db_path=db_e1,
                                     guardian=guardian, prefijo_hash=sellado.prefijo_hash_para_namespace)
    salida = w / "resultados_p4.jsonl"
    hechos = jl_last_wins(salida) if salida.exists() else {}
    t_ini = time.time()

    def guardar(reg):
        with salida.open("a", encoding="utf-8") as f:
            f.write(json.dumps(reg, ensure_ascii=False) + "\n")

    def extraer(cliente, perfil, c, techo, forma_r2: bool) -> dict:
        kwargs = perfil.build_request_kwargs(c, model=RC.MODEL_E1)
        par, err = RC.llamar_con_reintentos_api(
            lambda: cliente_e1.crear_con_reintento_corte(cliente, kwargs, doc=c["archivo"],
                                                         max_tokens_reintento=techo), c["id"])
        resp, cortado = par if par is not None else (None, None)
        reg = {"clave": lc.compute_key(cliente.cache.namespace, lc.canonical_request(kwargs))}
        ti, stop, usage = None, None, None
        if resp is not None:
            usage, stop, ti = RC._usage_e1(resp), getattr(resp, "stop_reason", None), tool_input_de(resp)
            if stop == "max_tokens":
                err = "max_tokens_hit_tras_reintento"
            elif ti is None:
                err = f"no_tool_use stop_reason={stop}"
        val = validador_e1.validar_salida(ti, c, esquema=perfil.esquema).as_dict() if ti is not None else None
        if forma_r2 and err is None and RC.motivo_forma_e1(val) is not None:
            kwf = dict(kwargs, max_tokens=techo) if cortado is not None else kwargs
            reg["reintento_forma"] = {"motivo": RC.motivo_forma_e1(val), "intento_1": cliente_e1.resumen_intento(resp)}
            resp_f, err_f = RC.llamar_con_reintentos_api(
                lambda: cliente_e1.crear_reintento_forma(cliente, kwf, doc=c["archivo"]), c["id"])
            if resp_f is None:
                err = err_f
            else:
                usage, stop, ti = RC._usage_e1(resp_f), getattr(resp_f, "stop_reason", None), tool_input_de(resp_f)
                val = validador_e1.validar_salida(ti, c, esquema=perfil.esquema).as_dict() if ti is not None else None
                if stop == "max_tokens" or ti is None or RC.motivo_forma_e1(val) is not None:
                    err = RC.ERROR_FORMA_TRAS_REINTENTO
        if cortado is not None:
            reg["reintento_corte"] = {"max_tokens_reintento": techo, "intento_1": cliente_e1.resumen_intento(cortado)}
        reg.update({"stop_reason": stop, "error": err, "usage": usage, "tool_input": ti, "validacion_e1": val})
        return reg

    def sellado_desde_cache(c) -> dict:
        kwargs = sellado.build_request_kwargs(c, model=RC.MODEL_E1)
        cc = lc.CachingClient(_SinAPI(), domain=cliente_e1.DOMAIN, db_path=DB_T0, namespace=ns_sellado,
                              thinking_enabled=False, run_label="p4_lectura_t0")
        try:
            reg = {"clave": lc.compute_key(ns_sellado, lc.canonical_request(kwargs)), "fuente": "cache_tanda0"}
            try:
                resp = cc.messages.create(**kwargs)
                if getattr(resp, "stop_reason", None) == "max_tokens":
                    reg["reintento_corte"] = {"max_tokens_reintento": cliente_e1.MAX_TOKENS_REINTENTO_CORTE,
                                              "intento_1": cliente_e1.resumen_intento(resp)}
                    resp = cc.messages.create(**dict(kwargs, max_tokens=cliente_e1.MAX_TOKENS_REINTENTO_CORTE))
                ti, stop, usage = tool_input_de(resp), getattr(resp, "stop_reason", None), RC._usage_e1(resp)
            except LookupError:
                r = crudo[c["id"]]
                ti, stop, usage = r.get("tool_input_crudo"), r.get("stop_reason"), r.get("usage")
                reg["fuente"] = "crudo_salida_dirigida (clave ausente en la caché)"
        finally:
            cc.close()
        ti_crudo = crudo[c["id"]].get("tool_input_crudo")
        reg.update({"igual_al_crudo_de_salida_dirigida": ti == ti_crudo, "stop_reason": stop, "error": None,
                    "usage": usage, "tool_input": ti,
                    "validacion_e1": validador_e1.validar_salida(ti, c, esquema=sellado.esquema).as_dict()})
        return reg

    try:
        # ---- brazo nuevo ----
        for g, cid in grupos:
            hk = f"{cid}|nuevo"
            if hk in hechos and hechos[hk].get("error") is None:
                continue
            reg = extraer(cli, nuevo, chunk_nuevo(cid), cliente_e1.MAX_TOKENS_REINTENTO_CORTE_R2, True)
            guardar({"chunk_id": hk, "id": cid, "grupo": g, "brazo": "nuevo", "namespace": ns_nuevo, **reg})
            print(f"[nuevo] {g:<32s} {cid:<28s} gasto USD {guardian.gasto_usd:.4f} err={reg['error']}", flush=True)
        # ---- brazo sellado ----
        for g, cid in grupos:
            hk = f"{cid}|sellado"
            if hk in hechos and hechos[hk].get("error") is None:
                continue
            if cid in en_t0:
                reg = sellado_desde_cache(chunk_sellado(cid))
            else:
                reg = extraer(cli_s, sellado, chunk_sellado(cid), cliente_e1.MAX_TOKENS_REINTENTO_CORTE, False)
                reg["fuente"] = "api"
            guardar({"chunk_id": hk, "id": cid, "grupo": g, "brazo": "sellado", "namespace": ns_sellado, **reg})
            print(f"[sellado] {g:<30s} {cid:<28s} gasto USD {guardian.gasto_usd:.4f} fuente={reg.get('fuente')}",
                  flush=True)
        # ---- pata de E3 ----
        res_nuevo = jl_last_wins(salida)
        c3 = cliente_e3.ClienteE3Real(**RC.P_E3, tope_usd=TOPE_USD, run_label="p4_pata_e3", db_path=db_e3,
                                      guardian=guardian)
        c1 = cliente_e1.ClienteE1Real(**RC.P_E1, tope_usd=TOPE_USD, run_label="p4_pata_e3_reintentos",
                                      db_path=db_e1r, guardian=guardian, prefijo_hash=nuevo.prefijo_hash_para_namespace)
        registro = ratchet_e3.RegistroE3(w / "pata_e3")
        try:
            for cid in m["pata_e3"]:
                hk = f"{cid}|pata_e3"
                if hk in hechos:
                    continue
                c = chunk_nuevo(cid)
                val = res_nuevo[f"{cid}|nuevo"]["validacion_e1"]
                todos = r2 if cid in en_t0 else fr2
                unidades = {x["unidad"] for x in todos.values() if x["to"] == c["to"]}
                exp = ratchet_e3.ciclo_ratchet(c, val, cliente_verificador=c3, cliente_extractor=c1,
                                               model_e3=RC.MODEL_E3, model_e1=RC.MODEL_E1, registro=registro,
                                               max_tokens_reintento=RC.MAX_TOKENS_REINTENTO,
                                               unidades_corpus=unidades, perfil=nuevo)
                guardar({"chunk_id": hk, "id": cid, "grupo": "pata_e3", "brazo": "pata_e3", "estado": exp["estado"],
                         "expediente": exp})
                print(f"[pata_e3] {cid:<28s} {exp['estado']} gasto USD {guardian.gasto_usd:.4f}", flush=True)
        finally:
            gasto_e3 = {"e3": c3.resumen(), "e1_reintentos": c1.resumen()}
            c3.close()
            c1.close()
    except (cliente_e1.TopeExcedido, cliente_e3.TopeExcedido) as e:
        print(f"FRENO por tope: {e}", flush=True)
        gasto_e3 = locals().get("gasto_e3")
    finally:
        gasto = {"tope_usd": TOPE_USD, "gasto_compartido_usd": round(guardian.gasto_usd, 6),
                 "e1_nuevo": cli.resumen(), "e1_sellado_api": cli_s.resumen(),
                 "pata_e3": locals().get("gasto_e3"), "segundos": round(time.time() - t_ini, 1)}
        cli.close()
        cli_s.close()
        (w / "gasto_p4.json").write_text(json.dumps(gasto, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    # ---- claves después ----
    despues = [{**k, "en_db_tanda0": en_db(DB_T0, k["clave"]), "en_db_p4": en_db(db_e1, k["clave"])} for k in claves]
    (w / "claves_despues.json").write_text(json.dumps(despues, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"gasto_compartido_usd": gasto["gasto_compartido_usd"]}, ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
