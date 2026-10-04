"""U-R2-CODIGO-2, C1.b — salidas de E1 mal formadas y diseño del reintento (USD 0, sin API ni Neo4j). Solo escribe --out.

Qué mide, sobre la salida guardada de la tanda 0 (`corpus_tanda0/salida_dirigida`, la entrada de los dos grafos r2a):
  1. Las unidades cuya validación de E1 rechaza el chunk entero, en los diez TOs, con el crudo caracterizado: claves
     y tipos del `tool_input`, `stop_reason`, tokens de salida y, si un campo viene como texto, por qué no es JSON.
  2. Dónde las rechaza la cadena: `validador_e1.validar_salida` (la E1 de la corrida) y `validador_r2.validar` (la
     entrada r2 de los grafos r2a), con el motivo.
  3. Reparación determinística (opción para la autora, no adoptada): por caso, si existe una transformación que no
     agrega contenido y qué validarían los dos validadores con ella.
  4. Clave de la caché local: la del request de la primera pasada (perfil `v3_b54`, el de la corrida) está en
     `e1_extractor/cache/e1_extraccion.db` con el mismo crudo; la de un reintento con el request idéntico y el
     namespace propuesto (`…-rforma1`) es otra y no está en la db. La db se abre en modo inmutable.

Uso, desde la raíz de una copia del repo:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/r2_codigo2/c1b_reintento.py \
      --out data/experiment/r2_codigo2/salidas/c1b_reintento.json
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import urllib.parse
from collections import Counter, OrderedDict

import c1_comun as K

import comun_e1                         # noqa: E402  (en el path por ensamblar_tanda0)
import cliente_e1                       # noqa: E402
import validador_e1                     # noqa: E402

REX = K.RAIZ / K.REX
SALIDA = K.RAIZ / K.ENTRADA
E0_LEGADA = K.RAIZ / K.E0_LEGADA
DB_E1 = REX / "e1_extractor" / "cache" / "e1_extraccion.db"
MODEL_E1 = "claude-haiku-4-5"      # runner_corpus.py:89
MOTIVOS_FORMA = ("salida_no_parseable", "salida_no_dict", "entities_o_relations_invalidos")
SUFIJO_NAMESPACE_REINTENTO = "rforma1"
DIEZ = json.loads((K.RAIZ / K.GRAFOS["diez"]["manifiesto"]).read_text(encoding="utf-8"))
DESARROLLO = json.loads((K.RAIZ / K.GRAFOS["desarrollo"]["manifiesto"]).read_text(encoding="utf-8"))


def _ids(man: dict) -> list[str]:
    return [t["id"] for t in man["tos"]]


def cargar_e1(to: str) -> dict[str, dict]:
    regs = {}
    for linea in (SALIDA / to / "extracciones_e1.jsonl").read_text(encoding="utf-8").splitlines():
        if linea.strip():
            r = json.loads(linea)
            regs[r["chunk_id"]] = r
    return regs


def por_que_no_es_json(s: str) -> dict:
    try:
        json.loads(s)
        return {"json_valido": True}
    except json.JSONDecodeError as e:
        return {"json_valido": False, "error": e.msg, "posicion": e.pos,
                "contexto": s[max(0, e.pos - 60):e.pos + 40]}


def reparacion(ti: dict) -> dict:
    """Transformaciones que no agregan contenido. (i) El campo `entities` es el resto del objeto serializado
    («[…],\\n"relations": […],\\n"omisiones_no_prosa": […]\\n}»): `{"entities": ` + el texto es el objeto. (ii) Falta
    `relations` y `entities` es una lista: relaciones vacías (pierde las relaciones, que el modelo no emitió). Si no
    hay transformación, la razón."""
    ent = ti.get("entities")
    if isinstance(ent, str):
        try:
            obj = json.loads('{"entities": ' + ent)
        except json.JSONDecodeError as e:
            return {"tipo": None, "motivo": f"entities no es JSON ni el resto de un objeto: {e.msg} en {e.pos}"}
        otros = {k: v for k, v in ti.items() if k != "entities"}
        choque = sorted(set(otros) & set(obj) - {"entities"})
        if choque:
            return {"tipo": None, "motivo": f"el texto trae claves que el tool_input ya tiene: {choque}"}
        return {"tipo": "objeto_serializado_en_entities", "tool_input": {**obj, **otros},
                "claves_recuperadas": sorted(set(obj) - {"entities"})}
    if isinstance(ent, list) and "relations" not in ti:
        return {"tipo": "relations_ausente", "tool_input": {**ti, "relations": []}, "claves_recuperadas": []}
    return {"tipo": None, "motivo": "sin transformación que no agregue contenido"}


def resumen_validacion(v) -> dict:
    d = v if isinstance(v, dict) else v.as_dict()
    rech = d.get("rechazos") or []
    return {"entidades": len(d.get("entidades") or []), "relaciones": len(d.get("relaciones") or []),
            "rechazos_por_nivel_y_motivo": dict(sorted(Counter(f"{r['nivel']}:{r['motivo']}" for r in rech).items()))}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    perfil = K.ENS.perfil_e1.perfil(DIEZ["perfil_e1"])
    import runner_corpus as RC          # noqa: PLC0415 — el de la copia
    validar_r2, pol = RC.validador_perfil_r2(perfil)
    ns = cliente_e1.namespace_e1(prefijo_hash=perfil.prefijo_hash_para_namespace)
    ns_reintento = cliente_e1.lc.make_namespace(
        cliente_e1.DOMAIN, code_ver=f"{cliente_e1.CODE_VER}-p{perfil.prefijo_hash_para_namespace}-"
                                    f"{SUFIJO_NAMESPACE_REINTENTO}", thinking=False)
    con = sqlite3.connect(f"file:{urllib.parse.quote(str(DB_E1.resolve()))}?mode=ro&immutable=1", uri=True)
    unidades, censo = [], {}
    try:
        for to in _ids(DIEZ):
            regs = cargar_e1(to)
            chunks = {c["id"]: c for c in comun_e1.cargar_chunks((to,), e0_dir=E0_LEGADA)}
            mal = [r for r in regs.values() if r.get("validacion") is not None
                   and any(x["nivel"] == "chunk" for x in r["validacion"]["rechazos"])]
            censo[to] = {"unidades_e1": len(regs), "rechazadas_a_nivel_chunk": len(mal),
                         "con_error_de_llamada": sum(1 for r in regs.values() if r.get("error"))}
            for r in sorted(mal, key=lambda x: x["chunk_id"]):
                c = chunks[r["chunk_id"]]
                ti = r["tool_input_crudo"]
                kw = perfil.build_request_kwargs(c, model=MODEL_E1)
                canon = cliente_e1.lc.canonical_request(kw)
                clave = cliente_e1.lc.compute_key(ns, canon)
                clave_r = cliente_e1.lc.compute_key(ns_reintento, canon)
                fila = con.execute("select raw_json from cache where key = ?", (clave,)).fetchone()
                crudo_db = None
                if fila is not None:
                    msg = json.loads(fila[0])
                    crudo_db = next((b.get("input") for b in msg.get("content") or []
                                     if isinstance(b, dict) and b.get("type") == "tool_use"), None)
                rep = reparacion(ti) if isinstance(ti, dict) else {"tipo": None, "motivo": "tool_input no es un dict"}
                con_rep = None
                if rep.get("tool_input") is not None:
                    con_rep = {"validador_e1": resumen_validacion(validador_e1.validar_salida(
                                   rep["tool_input"], c, esquema=perfil.esquema)),
                               "validador_r2": resumen_validacion(validar_r2(rep["tool_input"], c))}
                unidades.append(OrderedDict([
                    ("chunk_id", r["chunk_id"]), ("to", to),
                    ("en_los_grafos", ["diez"] + (["desarrollo"] if to in _ids(DESARROLLO) else [])),
                    ("stop_reason", r["stop_reason"]), ("error_de_llamada", r.get("error")),
                    ("usage", r["usage"]), ("max_tokens_del_request", kw["max_tokens"]),
                    ("claves_tool_input", {k: type(v).__name__ for k, v in (ti or {}).items()}),
                    ("campos_como_texto", {k: {"largo": len(v), **por_que_no_es_json(v)}
                                           for k, v in (ti or {}).items() if isinstance(v, str)}),
                    ("rechazo_validador_e1", resumen_validacion(r["validacion"])),
                    ("rechazo_validador_r2", resumen_validacion(validar_r2(ti, c))),
                    ("reparacion_deterministica", {k: v for k, v in rep.items() if k != "tool_input"}),
                    ("validacion_con_la_reparacion", con_rep),
                    ("cache_local", OrderedDict([
                        ("namespace", ns), ("clave", clave), ("en_la_db", fila is not None),
                        ("crudo_de_la_db_igual_al_guardado", crudo_db == ti),
                        ("namespace_reintento_propuesto", ns_reintento), ("clave_reintento", clave_r),
                        ("clave_reintento_en_la_db", con.execute("select 1 from cache where key = ?",
                                                                 (clave_r,)).fetchone() is not None),
                        ("request_del_reintento_igual_al_base", True)])),
                ]))
    finally:
        con.close()
    out = OrderedDict([
        ("perfil_de_la_corrida", perfil.nombre), ("motivos_de_forma", list(MOTIVOS_FORMA)),
        ("censo_por_to", censo),
        ("total_rechazadas_a_nivel_chunk", sum(v["rechazadas_a_nivel_chunk"] for v in censo.values())),
        ("por_motivo", dict(sorted(Counter(m for u in unidades for m in u["rechazo_validador_e1"]
                                           ["rechazos_por_nivel_y_motivo"]).items()))),
        ("unidades", unidades)])
    K.escribir_json(K.RAIZ / a.out, out)
    for u in unidades:
        print(u["chunk_id"], u["claves_tool_input"], u["reparacion_deterministica"].get("tipo"),
              u["cache_local"]["en_la_db"], u["cache_local"]["crudo_de_la_db_igual_al_guardado"],
              u["cache_local"]["clave_reintento_en_la_db"])


if __name__ == "__main__":
    main()
