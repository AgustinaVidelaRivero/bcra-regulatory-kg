"""
correr_p5.py — U-PROMPT-R2, P5: la medición de la temperatura de E1. Tope USD 1,5 (nota del mandato del 05/10/2026),
freno duro. Corre desde una COPIA del repo con el código de P5 (perfil r2b, prefijo `322c5a23e9b7`, pedido con
`temperature` 0 y reintento por salida mal formada con `temperature` 1), sobre la e0-r2 de C2
(`e0_chunking/salida_tanda0_r2b/`) y las unidades selladas en seleccion_p5.json.

Modos (cada uno, un proceso; en serie, decisión 4 de caching):
  - claves: namespace y clave de E1 de las 27 unidades (y la del reintento forzado), y si están en la base de la
    tanda 0, en la de P4, en la de P4b o en las de P5; contra la clave de P4b de cada unidad (`claves_<cuando>.json`).
    Sin API.
  - e1 --corrida a|b: E1 de las 27 unidades, cada corrida en su base propia (`p5_e1_<corrida>.db`): con una sola, la
    segunda saldría de la caché local. El camino es el de runner_corpus.fase_e1 con el perfil r2 (reintento por
    corte a 16.384, tercer escalón, reintento por salida mal formada con runner_corpus.kwargs_reintento_forma), sin la
    partición por corte (una unidad que corta y se puede partir queda con su error, como en P4 y P4b).
  - forma: el reintento por salida mal formada, forzado, sobre la unidad de `reintento_forma` de la selección: el
    pedido que arma runner_corpus.kwargs_reintento_forma, por cliente_e1.crear_reintento_forma, en la base de la
    corrida a (la misma db, namespace `-rforma1`). Corre inmediatamente después de la corrida a: su `usage` dice si
    el prefijo se lee de la caché de prompts de la API entre un pedido con temperatura 0 y uno con temperatura 1.
  - e3 --corrida a|b: la primera verificación de E3 (cliente_e3.verificar_chunk y ratchet_e3.evaluar_veredicto), sin
    el ciclo de reintentos, sobre la salida de E1 de la corrida a de las 10 unidades de `e3.todas`; cada corrida en su
    base propia (`p5_e3_<corrida>.db`). E3 corre sin temperatura fijada (decisión de la autora del 05/10/2026).

Caching (docs/decisiones_caching_extraccion.md): D1, los pedidos los arma el perfil; D2, el gasto es el de los
clientes, con la fórmula de caching; D3, cada respuesta real deja su línea en `logs/cache_usage.jsonl` de la copia que
corre; D4, todo en serie; D5, no toca la evaluación. Las bases de P5 viven en --trabajo/cache (propias; no se
reutilizan en U-REEXT-T0). El presupuesto es uno para toda la corrida (`presupuesto_p5.json` en --trabajo,
runner_corpus.PresupuestoCompartido, que se recarga en cada proceso).

Escribe solo en --trabajo. Uso (desde la raíz de la COPIA; la clave de la API, de data/experiment/evaluacion/.env del
repo, por --env):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p5/correr_p5.py --modo M [--corrida a|b] \
      --seleccion S --trabajo DIR [--bases-previas T0 P4 P4B] [--env ENV --autorizado-tope 1.5]
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
for sub in ("e1_extractor", "e3_verificador", "e2_reduce", "corpus_v2", "e0_chunking"):
    sys.path.insert(0, str(REX / sub))
sys.path.insert(0, str(REX))
sys.path.insert(0, str(REPO / "data" / "experiment" / "evaluacion"))
import llm_cache as lc  # noqa: E402 — capa sellada, solo import
import perfil_e1  # noqa: E402
import validador_e1  # noqa: E402
import cliente_e1  # noqa: E402
import cliente_e3  # noqa: E402
import prompt_e3  # noqa: E402
import ratchet_e3  # noqa: E402
import runner_corpus as RC  # noqa: E402 — constantes y helpers del runner, solo import

TOPE_USD = 1.5
PREFIJO = "322c5a23e9b7"
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
E0 = REX / "e0_chunking" / "salida_tanda0_r2b"
CLAVES_P4B = AQUI.parent / "p4b" / "salida" / "claves_antes_p3c.json"


def ahora() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def chunks() -> dict:
    out = {}
    for to in TOS:
        out.update({c["id"]: c for c in json.loads((E0 / f"chunks_{to}.json").read_text(encoding="utf-8"))})
    return out


def jl_last_wins(p: Path) -> dict:
    out = {}
    if p.exists():
        for x in p.read_text(encoding="utf-8").splitlines():
            if x.strip():
                r = json.loads(x)
                out[r["chunk_id"]] = r
    return out


def tool_input_de(resp):
    return next((b.input for b in resp.content if getattr(b, "type", None) == "tool_use"), None)


def usage_completo(resp) -> dict:
    return RC._usage_e1(resp)


def en_db(db: Path | None, key: str) -> bool:
    if db is None or not Path(db).exists():
        return False
    con = sqlite3.connect(f"file:{db}?mode=ro&immutable=1", uri=True)
    try:
        return con.execute("SELECT 1 FROM cache WHERE key = ?", (key,)).fetchone() is not None
    finally:
        con.close()


def cliente(perfil, guardian, run_label: str, db: Path):
    return cliente_e1.ClienteE1Real(**RC.P_E1, tope_usd=TOPE_USD, run_label=run_label, db_path=db, guardian=guardian,
                                    prefijo_hash=perfil.prefijo_hash_para_namespace, transmision=True)


def extraer(cli, perfil, c) -> dict:
    """El camino de E1 del perfil r2 (runner_corpus.fase_e1), sin la partición por corte."""
    techo = cliente_e1.MAX_TOKENS_REINTENTO_CORTE_R2
    kwargs = perfil.build_request_kwargs(c, model=RC.MODEL_E1)
    par, err = RC.llamar_con_reintentos_api(
        lambda: cliente_e1.crear_con_reintento_corte(cli, kwargs, doc=c["archivo"], max_tokens_reintento=techo,
                                                     escalon_3=lambda: RC.corresponde_escalon_3(c)), c["id"])
    resp, cortados = par if par is not None else (None, ())
    cortado = cortados[0] if cortados else None
    escalon3 = len(cortados) == 2
    reg = {"clave": lc.compute_key(cli.cache.namespace, lc.canonical_request(kwargs)),
           "temperatura_pedido": kwargs.get("temperature"), "cuando_utc": ahora()}
    ti, stop, usage = None, None, None
    if resp is not None:
        usage, stop, ti = usage_completo(resp), getattr(resp, "stop_reason", None), tool_input_de(resp)
        reg["id_respuesta"] = getattr(resp, "id", None)
        if stop == "max_tokens":
            err = RC.ERROR_TRAS_ESCALON_3 if escalon3 else "max_tokens_hit_tras_reintento"
        elif ti is None:
            err = f"no_tool_use stop_reason={stop}"
    val = validador_e1.validar_salida(ti, c, esquema=perfil.esquema).as_dict() if ti is not None else None
    if err is None and RC.motivo_forma_e1(val) is not None:
        kwf = RC.kwargs_reintento_forma(
            dict(kwargs, max_tokens=cliente_e1.MAX_TOKENS_ESCALON_3_R2) if escalon3
            else dict(kwargs, max_tokens=techo) if cortado is not None else kwargs, perfil)
        reg["reintento_forma"] = {"motivo": RC.motivo_forma_e1(val), "temperatura": kwf.get("temperature"),
                                  "intento_1": cliente_e1.resumen_intento(resp)}
        resp_f, err_f = RC.llamar_con_reintentos_api(
            lambda: cliente_e1.crear_reintento_forma(cli, kwf, doc=c["archivo"]), c["id"])
        if resp_f is None:
            err = err_f
        else:
            usage, stop, ti = usage_completo(resp_f), getattr(resp_f, "stop_reason", None), tool_input_de(resp_f)
            val = validador_e1.validar_salida(ti, c, esquema=perfil.esquema).as_dict() if ti is not None else None
            if stop == "max_tokens" or ti is None or RC.motivo_forma_e1(val) is not None:
                err = RC.ERROR_FORMA_TRAS_REINTENTO
    if cortado is not None:
        reg["reintento_corte"] = {"max_tokens_reintento": techo, "intento_1": cliente_e1.resumen_intento(cortado)}
    if escalon3:
        reg["escalon_3"] = {"max_tokens": cliente_e1.MAX_TOKENS_ESCALON_3_R2,
                            "intento_2": cliente_e1.resumen_intento(cortados[1])}
    reg.update({"stop_reason": stop, "error": err, "usage": usage, "tool_input": ti, "validacion_e1": val})
    return reg


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--modo", choices=("claves", "e1", "forma", "e3"), required=True)
    ap.add_argument("--corrida", choices=("a", "b"), default=None)
    ap.add_argument("--seleccion", type=Path, required=True)
    ap.add_argument("--trabajo", type=Path, required=True)
    ap.add_argument("--cuando", choices=("antes", "despues"), default="antes")
    ap.add_argument("--bases-previas", type=Path, nargs=3, default=(None, None, None),
                    help="copias, fuera del repo, de la base de E1 de la tanda 0, de la de P4 y de la de P4b")
    ap.add_argument("--env", type=Path, default=None)
    ap.add_argument("--autorizado-tope", type=float, default=None)
    a = ap.parse_args()
    w = a.trabajo.resolve()
    if REPO in w.parents or w == REPO:
        raise SystemExit("--trabajo no puede estar dentro del repo")
    (w / "cache").mkdir(parents=True, exist_ok=True)
    perfil = perfil_e1.perfil("r2b")
    if perfil.prefijo_hash != PREFIJO:
        raise SystemExit(f"la copia da el prefijo {perfil.prefijo_hash}, no {PREFIJO}")
    ns = cliente_e1.namespace_e1(prefijo_hash=perfil.prefijo_hash_para_namespace)
    ns_f = cliente_e1.namespace_e1(prefijo_hash=perfil.prefijo_hash_para_namespace,
                                   sufijo=cliente_e1.SUFIJO_REINTENTO_FORMA)
    sel = json.loads(a.seleccion.read_text(encoding="utf-8"))
    ch = chunks()
    db = {k: w / "cache" / f"p5_{k}.db" for k in ("e1_a", "e1_b", "e3_a", "e3_b")}

    if a.modo == "claves":
        p4b = {f["chunk_id"]: f["clave"] for f in json.loads(CLAVES_P4B.read_text(encoding="utf-8"))}
        filas = []
        for u in sel["unidades"]:
            kw = perfil.build_request_kwargs(ch[u["id"]], model=RC.MODEL_E1)
            k = lc.compute_key(ns, lc.canonical_request(kw))
            filas.append({"chunk_id": u["id"], "grupo": u["grupo"], "namespace": ns, "clave": k,
                          "temperatura": kw.get("temperature"), "clave_p4b": p4b.get(u["id"]),
                          "igual_a_p4b": k == p4b.get(u["id"]),
                          "en_db_tanda0": en_db(a.bases_previas[0], k), "en_db_p4": en_db(a.bases_previas[1], k),
                          "en_db_p4b": en_db(a.bases_previas[2], k),
                          "en_db_p5_a": en_db(db["e1_a"], k), "en_db_p5_b": en_db(db["e1_b"], k)})
        uf = sel["reintento_forma"]["unidad"]
        kw = perfil.build_request_kwargs(ch[uf], model=RC.MODEL_E1)
        kwf = RC.kwargs_reintento_forma(kw, perfil)
        kf = lc.compute_key(ns_f, lc.canonical_request(kwf))
        forma = {"chunk_id": uf, "namespace": ns_f, "clave": kf, "temperatura": kwf.get("temperature"),
                 **{f"en_db_{n}": en_db(p, kf) for n, p in zip(("tanda0", "p4", "p4b"), a.bases_previas)},
                 "en_db_p5_a": en_db(db["e1_a"], kf)}
        out = {"cuando": a.cuando, "namespace": ns, "namespace_reintento_forma": ns_f, "unidades": filas,
               "reintento_forma": forma}
        (w / f"claves_{a.cuando}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n",
                                                  encoding="utf-8")
        print(json.dumps({"namespace": ns, "unidades": len(filas),
                          **{x: sum(f[x] for f in filas) for x in ("igual_a_p4b", "en_db_tanda0", "en_db_p4",
                                                                   "en_db_p4b", "en_db_p5_a", "en_db_p5_b")},
                          "reintento_forma": forma}, ensure_ascii=False), flush=True)
        return 0

    if a.autorizado_tope != TOPE_USD:
        raise SystemExit(f"corrida real exige --autorizado-tope {TOPE_USD}")
    if a.env is None:
        raise SystemExit("corrida real exige --env (data/experiment/evaluacion/.env)")
    if a.modo in ("e1", "e3") and a.corrida is None:
        raise SystemExit("los modos e1 y e3 exigen --corrida a|b")
    from dotenv import load_dotenv  # noqa: PLC0415
    load_dotenv(a.env)              # como runner_pareada_b54.py:148; la clave no se imprime
    guardian = RC.PresupuestoCompartido(TOPE_USD, w / "presupuesto_p5.json")
    salida = w / "resultados_p5.jsonl"
    t_ini = time.time()

    def guardar(reg):
        with salida.open("a", encoding="utf-8") as f:
            f.write(json.dumps(reg, ensure_ascii=False) + "\n")

    resumen: dict = {"modo": a.modo, "corrida": a.corrida, "namespace": ns, "inicio_utc": ahora()}
    clis = []
    try:
        if a.modo == "e1":
            cli = cliente(perfil, guardian, f"p5_e1_{a.corrida}", db[f"e1_{a.corrida}"])
            clis.append(("e1", cli))
            hechos = jl_last_wins(salida)
            for u in sel["unidades"]:
                hk = f"{u['id']}|{a.corrida}"
                if hk in hechos and hechos[hk].get("error") is None:
                    continue
                reg = extraer(cli, perfil, ch[u["id"]])
                guardar({"chunk_id": hk, "id": u["id"], "grupo": u["grupo"], "corrida": a.corrida, "namespace": ns,
                         **reg})
                print(f"[{a.corrida}] {u['grupo']:<14s} {u['id']:<22s} gasto USD {guardian.gasto_usd:.4f} "
                      f"err={reg['error']}" + (" CORTE" if "reintento_corte" in reg else "")
                      + (" ESCALON_3" if "escalon_3" in reg else "") + (" FORMA" if "reintento_forma" in reg else ""),
                      flush=True)
        elif a.modo == "forma":
            cli = cliente(perfil, guardian, "p5_forma", db["e1_a"])
            clis.append(("forma", cli))
            res = jl_last_wins(salida)
            previos = [r["cuando_utc"] for k, r in res.items() if k.endswith("|a") and r.get("cuando_utc")]
            uf = sel["reintento_forma"]["unidad"]
            c = ch[uf]
            kw = perfil.build_request_kwargs(c, model=RC.MODEL_E1)
            kwf = RC.kwargs_reintento_forma(kw, perfil)
            out = {"unidad": uf, "namespace": ns_f, "clave": lc.compute_key(ns_f, lc.canonical_request(kwf)),
                   "clave_primer_intento": lc.compute_key(ns, lc.canonical_request(kw)),
                   "temperatura_primer_intento": kw.get("temperature"), "temperatura": kwf.get("temperature"),
                   "difiere_del_primer_intento_solo_en_la_temperatura":
                       {k: v for k, v in kwf.items() if k != "temperature"}
                       == {k: v for k, v in kw.items() if k != "temperature"},
                   "pedido_sin_mensajes": {k: v for k, v in kwf.items() if k not in ("system", "tools", "messages")},
                   "ultima_llamada_de_la_corrida_a_utc": max(previos) if previos else None, "cuando_utc": ahora()}
            resp = cliente_e1.crear_reintento_forma(cli, kwf, doc=c["archivo"])
            ti = tool_input_de(resp)
            val = validador_e1.validar_salida(ti, c, esquema=perfil.esquema).as_dict() if ti is not None else None
            out.update({"stop_reason": getattr(resp, "stop_reason", None), "usage": usage_completo(resp),
                        "id_respuesta": getattr(resp, "id", None), "tool_use": ti is not None,
                        "motivo_forma": RC.motivo_forma_e1(val), "hit_cache_local": cli.llamadas_hit > 0})
            guardar({"chunk_id": f"{uf}|forma", "id": uf, "corrida": "forma", **out, "tool_input": ti})
            (w / "reintento_forma_p5.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n",
                                                       encoding="utf-8")
            print(json.dumps(out, ensure_ascii=False), flush=True)
        else:  # e3
            res = jl_last_wins(salida)
            c3 = cliente_e3.ClienteE3Real(**RC.P_E3, tope_usd=TOPE_USD, run_label=f"p5_e3_{a.corrida}",
                                          db_path=db[f"e3_{a.corrida}"], guardian=guardian)
            clis.append(("e3", c3))
            ns3 = cliente_e3.namespace_e3()
            for cid in sel["e3"]["todas"]:
                hk = f"{cid}|e3{a.corrida}"
                if hk in res:
                    continue
                c = ch[cid]
                val = res[f"{cid}|a"]["validacion_e1"]
                kw3 = prompt_e3.build_request_kwargs(c, val, model=RC.MODEL_E3)
                unidades_to = {x["unidad"] for x in ch.values() if x["to"] == c["to"]}
                crudo, err = RC.llamar_con_reintentos_api(
                    lambda: cliente_e3.verificar_chunk(c3, c, val, model=RC.MODEL_E3), cid)
                if crudo is None:
                    guardar({"chunk_id": hk, "id": cid, "corrida": f"e3{a.corrida}", "error": err})
                    continue
                ev = ratchet_e3.evaluar_veredicto(crudo["tool_input"], c, unidades_to, val)
                guardar({"chunk_id": hk, "id": cid, "corrida": f"e3{a.corrida}", "namespace": ns3,
                         "clave": lc.compute_key(ns3, lc.canonical_request(kw3)),
                         "temperatura_pedido": kw3.get("temperature"), "stop_reason": crudo["stop_reason"],
                         "error": crudo["error"], "tool_input": crudo["tool_input"],
                         "es_completo_ok": ev["es_completo_ok"], "aceptable": ev["aceptable"],
                         "n_faltantes": len(ev["faltantes"]), "n_bloqueantes": len(ev["faltantes_bloqueantes"]),
                         "n_residuales": len(ev["residuales"]), "incoherencias": ev["incoherencias"],
                         "faltantes": ev["faltantes"], "cuando_utc": ahora()})
                print(f"[e3{a.corrida}] {cid:<22s} completo_ok={ev['es_completo_ok']} aceptable={ev['aceptable']} "
                      f"faltantes={len(ev['faltantes'])} gasto USD {guardian.gasto_usd:.4f}", flush=True)
    except (cliente_e1.TopeExcedido, cliente_e3.TopeExcedido) as e:
        print(f"FRENO por tope: {e}", flush=True)
        resumen["freno"] = str(e)
    finally:
        resumen.update({"tope_usd": TOPE_USD, "gasto_compartido_usd": round(guardian.gasto_usd, 6),
                        "segundos": round(time.time() - t_ini, 1), "fin_utc": ahora()})
        for nombre, c in clis:
            resumen[nombre] = c.resumen()
            c.close()
        with (w / "gasto_p5.jsonl").open("a", encoding="utf-8") as f:
            f.write(json.dumps(resumen, ensure_ascii=False) + "\n")
    print(json.dumps({"gasto_compartido_usd": resumen["gasto_compartido_usd"]}, ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
