"""
correr_p4b.py — U-PROMPT-R2, P4b: la corrida de la prueba corta. Tope USD 1,5 (decisión 4 de la nota del mandato del
04/10/2026, `:776-800`), freno duro.

Release contra release: cada brazo corre desde una COPIA del repo en su commit, con el código de ese commit (prefijo,
mensaje y lista de tablas forzadas), sobre la misma e0-r2 de C2 (`e0_chunking/salida_tanda0_r2b/`):
  - brazo «anterior»: la copia de `44c6e1b`, el padre de `66cde30` (P3c-2); perfil r2b, prefijo `3817de475c93`;
  - brazo «p3c»: la copia de `bb212f1` (la corrección de la clase modalidad); perfil r2b, prefijo `322c5a23e9b7`.
El script es el mismo en las dos copias; el camino de E1 es el de `runner_corpus.fase_e1` con el perfil r2 de cada
release: reintento por corte a 16.384 (cliente_e1.MAX_TOKENS_REINTENTO_CORTE_R2), tercer escalón donde el release lo
tiene (P3c-2, solo `bb212f1`) y reintento por forma (C2 de U-R2-CODIGO-2, punto b). La partición por corte no se corre:
una unidad que corta y se puede partir queda con su error, como en P4.

Modos (cada uno, un proceso; en serie, decisión 4 de caching):
  - claves: namespace, clave y tamaño del mensaje de cada unidad del brazo, y si la clave está en la base de la tanda 0,
    en la de P4 o en la de P4b (`claves_<cuando>_<brazo>.json`); sin API;
  - e1: E1 de las unidades del brazo (`resultados_p4b.jsonl`, una línea por unidad y brazo);
  - escalon3 (solo «p3c»): una llamada con el techo completo del tercer escalón (40.960) sobre la unidad más corta del
    brazo, por el cliente con transmisión: confirma que la API acepta ese techo (`escalon3_p4b.json`);
  - e3 (solo «p3c»): la pata de E3, `ratchet_e3.ciclo_ratchet` con la validación del brazo «p3c» sobre las unidades de
    `pata_e3` de la selección; reintento de E1 a 16.384.

Caching (docs/decisiones_caching_extraccion.md): D1, los requests los arman los perfiles; D2, el gasto es el de los
clientes, con la fórmula de caching; D3, cada response real deja su línea en `logs/cache_usage.jsonl` de la copia que
corre; D4, todo en serie; D5, no toca la evaluación. Las bases de P4b viven en --trabajo/cache (propias; no se
reutilizan en U-REEXT-T0). El presupuesto es uno para toda la corrida (`presupuesto_p4b.json` en --trabajo,
runner_corpus.PresupuestoCompartido, que se recarga en cada proceso).

Escribe solo en --trabajo. Uso (desde la raíz de la COPIA del commit del brazo; la clave de la API, de
data/experiment/evaluacion/.env del repo, por --env):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p4b/correr_p4b.py --modo M --brazo B \
      --seleccion S --trabajo DIR [--bases-previas DIR_T0_DB P4_DB] [--env ENV --autorizado-tope 1.5]
"""
from __future__ import annotations

import argparse
import inspect
import json
import sqlite3
import sys
import time
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
import runner_corpus as RC  # noqa: E402 — constantes y helpers del runner, solo import

TOPE_USD = 1.5
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
E0 = REX / "e0_chunking" / "salida_tanda0_r2b"
PREFIJO = {"anterior": "3817de475c93", "p3c": "322c5a23e9b7"}
TERCER_ESCALON = hasattr(cliente_e1, "MAX_TOKENS_ESCALON_3_R2")


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


def en_db(db: Path | None, key: str) -> bool:
    if db is None or not Path(db).exists():
        return False
    con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    try:
        return con.execute("SELECT 1 FROM cache WHERE key = ?", (key,)).fetchone() is not None
    finally:
        con.close()


def unidades(sel: dict) -> list[tuple[str, str]]:
    return [(g, c) for g, ids in sel["grupos"].items() for c in ids]


def cliente(perfil, w: Path, guardian, run_label: str, db: Path):
    kw = dict(**RC.P_E1, tope_usd=TOPE_USD, run_label=run_label, db_path=db, guardian=guardian,
              prefijo_hash=perfil.prefijo_hash_para_namespace)
    if "transmision" in inspect.signature(cliente_e1.ClienteE1Real.__init__).parameters:
        kw["transmision"] = True        # el perfil r2 del release de P3c-2 (runner_corpus: transmision=PERFIL_R2)
    return cliente_e1.ClienteE1Real(**kw)


def extraer(cli, perfil, c) -> dict:
    """El camino de E1 del perfil r2 de este release (runner_corpus.fase_e1), sin la partición por corte."""
    techo = cliente_e1.MAX_TOKENS_REINTENTO_CORTE_R2
    kwargs = perfil.build_request_kwargs(c, model=RC.MODEL_E1)
    escalon3 = False
    if TERCER_ESCALON:
        par, err = RC.llamar_con_reintentos_api(
            lambda: cliente_e1.crear_con_reintento_corte(cli, kwargs, doc=c["archivo"], max_tokens_reintento=techo,
                                                         escalon_3=lambda: RC.corresponde_escalon_3(c)), c["id"])
        resp, cortados = par if par is not None else (None, ())
        cortado = cortados[0] if cortados else None
        escalon3 = len(cortados) == 2
    else:
        par, err = RC.llamar_con_reintentos_api(
            lambda: cliente_e1.crear_con_reintento_corte(cli, kwargs, doc=c["archivo"], max_tokens_reintento=techo),
            c["id"])
        resp, cortado = par if par is not None else (None, None)
    reg = {"clave": lc.compute_key(cli.cache.namespace, lc.canonical_request(kwargs))}
    ti, stop, usage = None, None, None
    if resp is not None:
        usage, stop, ti = RC._usage_e1(resp), getattr(resp, "stop_reason", None), tool_input_de(resp)
        if stop == "max_tokens":
            err = RC.ERROR_TRAS_ESCALON_3 if escalon3 else "max_tokens_hit_tras_reintento"
        elif ti is None:
            err = f"no_tool_use stop_reason={stop}"
    val = validador_e1.validar_salida(ti, c, esquema=perfil.esquema).as_dict() if ti is not None else None
    if err is None and RC.motivo_forma_e1(val) is not None:
        kwf = (dict(kwargs, max_tokens=cliente_e1.MAX_TOKENS_ESCALON_3_R2) if escalon3
               else dict(kwargs, max_tokens=techo) if cortado is not None else kwargs)
        reg["reintento_forma"] = {"motivo": RC.motivo_forma_e1(val), "intento_1": cliente_e1.resumen_intento(resp)}
        resp_f, err_f = RC.llamar_con_reintentos_api(
            lambda: cliente_e1.crear_reintento_forma(cli, kwf, doc=c["archivo"]), c["id"])
        if resp_f is None:
            err = err_f
        else:
            usage, stop, ti = RC._usage_e1(resp_f), getattr(resp_f, "stop_reason", None), tool_input_de(resp_f)
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
    ap.add_argument("--modo", choices=("claves", "e1", "escalon3", "e3"), required=True)
    ap.add_argument("--brazo", choices=("anterior", "p3c"), required=True)
    ap.add_argument("--seleccion", type=Path, required=True)
    ap.add_argument("--trabajo", type=Path, required=True)
    ap.add_argument("--cuando", choices=("antes", "despues"), default="antes")
    ap.add_argument("--bases-previas", type=Path, nargs=2, default=(None, None),
                    help="copias, fuera del repo, de la base de la tanda 0 y de la de P4")
    ap.add_argument("--env", type=Path, default=None)
    ap.add_argument("--autorizado-tope", type=float, default=None)
    a = ap.parse_args()
    w = a.trabajo.resolve()
    if REPO in w.parents or w == REPO:
        raise SystemExit("--trabajo no puede estar dentro del repo")
    (w / "cache").mkdir(parents=True, exist_ok=True)
    perfil = perfil_e1.perfil("r2b")
    if perfil.prefijo_hash != PREFIJO[a.brazo]:
        raise SystemExit(f"brazo {a.brazo}: la copia da el prefijo {perfil.prefijo_hash}, no {PREFIJO[a.brazo]}")
    ns = cliente_e1.namespace_e1(prefijo_hash=perfil.prefijo_hash_para_namespace)
    sel = json.loads(a.seleccion.read_text(encoding="utf-8"))
    ch = chunks()
    db_e1, db_e3, db_e1r = w / "cache" / "p4b_e1.db", w / "cache" / "p4b_e3.db", w / "cache" / "p4b_e1_reintentos.db"

    if a.modo == "claves":
        filas = []
        for g, cid in unidades(sel):
            kw = perfil.build_request_kwargs(ch[cid], model=RC.MODEL_E1)
            k = lc.compute_key(ns, lc.canonical_request(kw))
            usuario = "".join(b.get("text", "") if isinstance(b, dict) else str(b)
                              for m in kw["messages"] for b in (m["content"] if isinstance(m["content"], list)
                                                                 else [{"text": m["content"]}]))
            filas.append({"chunk_id": cid, "grupo": g, "brazo": a.brazo, "namespace": ns, "clave": k,
                          "chars_mensaje": len(usuario), "max_tokens": kw.get("max_tokens"),
                          "en_db_tanda0": en_db(a.bases_previas[0], k), "en_db_p4": en_db(a.bases_previas[1], k),
                          "en_db_p4b": en_db(db_e1, k)})
        (w / f"claves_{a.cuando}_{a.brazo}.json").write_text(json.dumps(filas, ensure_ascii=False, indent=1) + "\n",
                                                            encoding="utf-8")
        print(json.dumps({"brazo": a.brazo, "namespace": ns, "unidades": len(filas),
                          **{x: sum(f[x] for f in filas) for x in ("en_db_tanda0", "en_db_p4", "en_db_p4b")}},
                         ensure_ascii=False), flush=True)
        return 0

    if a.autorizado_tope != TOPE_USD:
        raise SystemExit(f"corrida real exige --autorizado-tope {TOPE_USD}")
    if a.env is None:
        raise SystemExit("corrida real exige --env (data/experiment/evaluacion/.env)")
    from dotenv import load_dotenv  # noqa: PLC0415
    load_dotenv(a.env)              # como runner_pareada_b54.py:148; la clave no se imprime
    guardian = RC.PresupuestoCompartido(TOPE_USD, w / "presupuesto_p4b.json")
    salida = w / "resultados_p4b.jsonl"
    t_ini = time.time()

    def guardar(reg):
        with salida.open("a", encoding="utf-8") as f:
            f.write(json.dumps(reg, ensure_ascii=False) + "\n")

    resumen: dict = {"modo": a.modo, "brazo": a.brazo, "namespace": ns, "tercer_escalon_en_el_release": TERCER_ESCALON}
    cli = cliente(perfil, w, guardian, f"p4b_{a.modo}_{a.brazo}", db_e1)
    try:
        if a.modo == "e1":
            hechos = jl_last_wins(salida)
            for g, cid in unidades(sel):
                hk = f"{cid}|{a.brazo}"
                if hk in hechos and hechos[hk].get("error") is None:
                    continue
                reg = extraer(cli, perfil, ch[cid])
                guardar({"chunk_id": hk, "id": cid, "grupo": g, "brazo": a.brazo, "namespace": ns, **reg})
                print(f"[{a.brazo}] {g:<14s} {cid:<22s} gasto USD {guardian.gasto_usd:.4f} err={reg['error']}"
                      + (" CORTE" if "reintento_corte" in reg else "") + (" ESCALON_3" if "escalon_3" in reg else "")
                      + (" FORMA" if "reintento_forma" in reg else ""), flush=True)
        elif a.modo == "escalon3":
            if a.brazo != "p3c" or not TERCER_ESCALON:
                raise SystemExit("el modo escalon3 corre solo con el brazo p3c (release con tercer escalón)")
            cid = min((len(ch[c].get("texto") or ""), c) for _, c in unidades(sel))[1]
            kw = dict(perfil.build_request_kwargs(ch[cid], model=RC.MODEL_E1),
                      max_tokens=cliente_e1.MAX_TOKENS_ESCALON_3_R2)
            out = {"unidad": cid, "max_tokens": kw["max_tokens"], "transmite": cli._transmite(kw),
                   "limite_sin_transmision": cliente_e1.LIMITE_SIN_TRANSMISION,
                   "clave": lc.compute_key(ns, lc.canonical_request(kw))}
            try:
                resp = cli.create(doc=ch[cid]["archivo"], **kw)
                out.update({"aceptada": True, "stop_reason": getattr(resp, "stop_reason", None),
                            "usage": RC._usage_e1(resp), "tool_use": tool_input_de(resp) is not None,
                            "id_respuesta": getattr(resp, "id", None)})
            except cliente_e1.TopeExcedido:
                raise
            except Exception as e:  # noqa: BLE001 — se registra la respuesta de la API tal cual
                out.update({"aceptada": False, "error": f"{type(e).__name__}: {e}"[:2000]})
            (w / "escalon3_p4b.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n",
                                                 encoding="utf-8")
            print(json.dumps(out, ensure_ascii=False), flush=True)
        else:  # e3
            if a.brazo != "p3c":
                raise SystemExit("la pata de E3 corre con el brazo p3c")
            import ratchet_e3  # noqa: PLC0415
            res = jl_last_wins(salida)
            c3 = cliente_e3.ClienteE3Real(**RC.P_E3, tope_usd=TOPE_USD, run_label="p4b_pata_e3", db_path=db_e3,
                                          guardian=guardian)
            c1 = cliente(perfil, w, guardian, "p4b_pata_e3_reintentos", db_e1r)
            registro = ratchet_e3.RegistroE3(w / "pata_e3")
            try:
                for cid in sel["pata_e3"]:
                    hk = f"{cid}|pata_e3"
                    if hk in res:
                        continue
                    c = ch[cid]
                    val = res[f"{cid}|p3c"]["validacion_e1"]
                    unidades_to = {x["unidad"] for x in ch.values() if x["to"] == c["to"]}
                    exp = ratchet_e3.ciclo_ratchet(c, val, cliente_verificador=c3, cliente_extractor=c1,
                                                   model_e3=RC.MODEL_E3, model_e1=RC.MODEL_E1, registro=registro,
                                                   max_tokens_reintento=RC.MAX_TOKENS_REINTENTO,
                                                   unidades_corpus=unidades_to, perfil=perfil)
                    guardar({"chunk_id": hk, "id": cid, "grupo": "pata_e3", "brazo": "pata_e3", "estado": exp["estado"],
                             "expediente": exp})
                    print(f"[pata_e3] {cid:<22s} {exp['estado']} gasto USD {guardian.gasto_usd:.4f}", flush=True)
            finally:
                resumen["e3"], resumen["e1_reintentos"] = c3.resumen(), c1.resumen()
                c3.close()
                c1.close()
    except (cliente_e1.TopeExcedido, cliente_e3.TopeExcedido) as e:
        print(f"FRENO por tope: {e}", flush=True)
        resumen["freno"] = str(e)
    finally:
        resumen.update({"tope_usd": TOPE_USD, "gasto_compartido_usd": round(guardian.gasto_usd, 6),
                        "e1": cli.resumen(), "segundos": round(time.time() - t_ini, 1)})
        cli.close()
        with (w / "gasto_p4b.jsonl").open("a", encoding="utf-8") as f:
            f.write(json.dumps(resumen, ensure_ascii=False) + "\n")
    print(json.dumps({"gasto_compartido_usd": resumen["gasto_compartido_usd"]}, ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
