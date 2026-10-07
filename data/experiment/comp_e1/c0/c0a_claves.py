"""
c0a_claves.py — U-COMP-E1, etapa C0, punto (a). USD 0, sin API.

Qué hace (mandato docs/mandatos/UCOMP_E1_comparacion_chica_modelo.md, firmado en cbcb823, etapa C0 (a)):
  1. Arma la lista de las 87 unidades desde las fichas de T4 de U-REEXT-T0: las unidades con `mas_de_un_supuesto` de
     fichas_punto7_grupo_c.json (grupo c) y las unidades de las 60 fichas de fichas_punto8_omisiones.json (omisiones);
     recomputa el conteo por TO contra el del mandato.
  2. Para cada unidad, con el perfil r2b (prefijo 322c5a23e9b7) y `claude-haiku-4-5`, arma el pedido de E1 tal como lo
     armó el runner (perfil.build_request_kwargs) y calcula su clave de la caché local (llm_cache.compute_key sobre el
     namespace de cliente_e1.namespace_e1); comprueba que esa clave está en la base de E1 de la tanda 0
     (e1_extractor/cache/e1_extraccion.db, abierta en modo solo lectura e inmutable) y que la entrada de la herramienta
     guardada en la base coincide con `tool_input_crudo` de extracciones_e1.jsonl (el intento 0).
  3. Lee finales.jsonl (última versión por chunk_id, como runner_corpus.cargar_jsonl_last_wins) para identificar las
     unidades con n_reintentos 1 y las de la cola humana; compara validacion_final con la validación del intento 0.
  4. Escribe, en --salida: unidades.json (lista sellable), intento0_haiku.jsonl (las 87 líneas de extracciones_e1.jsonl,
     byte a byte, última versión por chunk_id), claves_c0.json (clave, namespace y controles por unidad) y
     resumen_c0a.json. Ninguna ruta absoluta en las salidas.

Corre sobre una COPIA del repo sin enlaces (CLAUDE.md §4.l), con PYTHONDONTWRITEBYTECODE=1 y python -B:
  PYTHONDONTWRITEBYTECODE=1 <venv>/bin/python -B data/experiment/comp_e1/c0/c0a_claves.py --salida DIR
"""
from __future__ import annotations

import argparse
import collections
import json
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

AQUI = Path(__file__).resolve().parent            # comp_e1/c0
REPO = AQUI.parents[3]                            # raíz (del repo o de la copia)
REX = REPO / "data" / "experiment" / "reextraccion_v2"
for sub in ("e1_extractor",):
    sys.path.insert(0, str(REX / sub))
sys.path.insert(0, str(REPO / "data" / "experiment" / "evaluacion"))
sys.path.insert(0, str(REPO / "data" / "experiment" / "pyd_r2" / "code"))
import llm_cache as lc  # noqa: E402 — capa sellada, solo import
import perfil_e1  # noqa: E402
import cliente_e1  # noqa: E402

MODELO_H = "claude-haiku-4-5"
PREFIJO = "322c5a23e9b7"
SALIDA_R2B = REX / "corpus_tanda0" / "salida_r2b"
E0 = REX / "e0_chunking" / "salida_tanda0_r2b"
DB_E1 = REX / "e1_extractor" / "cache" / "e1_extraccion.db"
T4 = REPO / "data" / "experiment" / "reext_t0" / "t4" / "salida"
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
# Conteo por TO que declara el mandato (UNIDADES): se recomputa contra las fichas.
POR_TO_MANDATO = {"cap": 15, "cla": 13, "ctacte": 7, "ext": 29, "lingob": 7, "pagjub": 2, "polcre": 3, "pro": 4, "ric": 7}


def rel(p: Path) -> str:
    return str(p.relative_to(REPO))


def ahora() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def lineas_last_wins(p: Path) -> dict[str, str]:
    """chunk_id → línea cruda (última versión), para persistir el intento 0 byte a byte."""
    out: dict[str, str] = {}
    for x in p.read_text(encoding="utf-8").splitlines():
        if x.strip():
            out[json.loads(x)["chunk_id"]] = x
    return out


def chunks_de(to: str) -> dict:
    """Chunks de la E0 r2b del TO, más las partes de particiones_por_corte.json (como reext_t0/t4/comun_t4.chunks)."""
    d = json.loads((E0 / f"chunks_{to}.json").read_text(encoding="utf-8"))
    out = {c["id"]: c for c in (d["chunks"] if isinstance(d, dict) else d)}
    p = SALIDA_R2B / to / "particiones_por_corte.json"
    if p.exists():
        for cid, v in json.loads(p.read_text(encoding="utf-8")).items():
            for parte in v["partes"]:
                base = dict(out[cid])
                base.update({k: parte[k] for k in parte if k != "id"}, id=parte["id"])
                out[parte["id"]] = base
    return out


def tool_input_de_crudo(raw_json: str):
    m = json.loads(raw_json)
    for b in m.get("content") or []:
        if isinstance(b, dict) and b.get("type") == "tool_use":
            return b.get("input")
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    a.salida.mkdir(parents=True, exist_ok=True)

    perfil = perfil_e1.perfil("r2b")
    if perfil.prefijo_hash != PREFIJO:
        raise SystemExit(f"el perfil r2b da el prefijo {perfil.prefijo_hash}, no {PREFIJO}")
    ns = cliente_e1.namespace_e1(prefijo_hash=perfil.prefijo_hash_para_namespace)
    ns_f = cliente_e1.namespace_e1(prefijo_hash=perfil.prefijo_hash_para_namespace, sufijo=cliente_e1.SUFIJO_REINTENTO_FORMA)
    import prompt_r2b  # noqa: PLC0415 — ya importado por el perfil; candados corridos

    # 1. Las 87 unidades desde las fichas de T4.
    gc = json.loads((T4 / "fichas_punto7_grupo_c.json").read_text(encoding="utf-8"))
    om = json.loads((T4 / "fichas_punto8_omisiones.json").read_text(encoding="utf-8"))
    grupo_c = [f["chunk_id"] for f in gc["fichas"] if f["mas_de_un_supuesto"]]
    om_por_unidad: dict[str, list] = collections.defaultdict(list)
    for f in om["fichas"]:
        om_por_unidad[f["chunk_id"]].append({"grupo": f["grupo"], "n": f["n"], "posicion": f["posicion"],
                                             "normativo": f["normativo"], "clase": f["clase"], "en": f["en"]})
    ids = sorted(set(grupo_c) | set(om_por_unidad))
    por_to = collections.Counter(u.split("::")[0] for u in ids)
    en_ambos = sorted(set(grupo_c) & set(om_por_unidad))

    # 2 y 3. Registros de la corrida r2b.
    e1_lineas: dict[str, str] = {}
    finales: dict[str, dict] = {}
    for to in TOS:
        e1_lineas.update(lineas_last_wins(SALIDA_R2B / to / "extracciones_e1.jsonl"))
        for cid, ln in lineas_last_wins(SALIDA_R2B / to / "finales.jsonl").items():
            finales[cid] = json.loads(ln)
    chunks: dict[str, dict] = {}
    for to in sorted({u.split("::")[0] for u in ids}):
        chunks.update(chunks_de(to))

    con = sqlite3.connect(f"file:{DB_E1}?mode=ro&immutable=1", uri=True)
    con.row_factory = sqlite3.Row

    def fila(key: str):
        return con.execute("SELECT key, namespace, model, stop_reason, input_tokens, output_tokens, cache_read_tokens, "
                           "cache_write_tokens, created_at, raw_json FROM cache WHERE key = ?", (key,)).fetchone()

    unidades, claves, intento0 = [], [], []
    cuentas = collections.Counter()
    for cid in ids:
        c = chunks[cid]
        reg = json.loads(e1_lineas[cid])
        fin = finales[cid]
        kw = perfil.build_request_kwargs(c, model=MODELO_H)
        k_base = lc.compute_key(ns, lc.canonical_request(kw))
        fb = fila(k_base)
        ctrl = {"chunk_id": cid, "namespace": ns, "clave_e1_intento0": k_base, "en_db_e1": fb is not None,
                "temperatura_pedido": kw.get("temperature"), "max_tokens_pedido": kw.get("max_tokens"),
                "tool_choice_pedido": kw.get("tool_choice"), "modelo_pedido": kw.get("model")}
        if fb is not None:
            ctrl.update({"db_model": fb["model"], "db_stop_reason": fb["stop_reason"], "db_created_at": fb["created_at"],
                         "db_usage": {"input_tokens": fb["input_tokens"], "output_tokens": fb["output_tokens"],
                                      "cache_read_tokens": fb["cache_read_tokens"], "cache_write_tokens": fb["cache_write_tokens"]}})
        marcas = [k for k in ("reintento_corte", "escalon_3", "reintento_forma", "reparacion_forma", "particion_por_corte") if k in reg]
        ctrl["marcas_intento0"] = marcas
        # Qué respuesta es `tool_input_crudo` del registro: la del pedido base, la del reintento por corte (16.384) o la
        # del reintento por forma (temperatura 1, namespace -rforma1). Se controla contra la base en cada caso.
        if "reintento_forma" in reg:
            kw_f = prompt_r2b.kwargs_reintento_forma_r2b(dict(kw, max_tokens=reg["reintento_corte"]["max_tokens_reintento"])
                                                        if "reintento_corte" in reg else kw)
            k_f = lc.compute_key(ns_f, lc.canonical_request(kw_f))
            ff = fila(k_f)
            ctrl.update({"clave_reintento_forma": k_f, "namespace_reintento_forma": ns_f, "en_db_reintento_forma": ff is not None,
                         "temperatura_reintento_forma": kw_f.get("temperature")})
            ctrl["tool_input_jsonl_igual_a_db"] = (ff is not None and tool_input_de_crudo(ff["raw_json"]) == reg["tool_input_crudo"])
            ctrl["intento_1_jsonl_igual_a_db_base"] = (fb is not None and tool_input_de_crudo(fb["raw_json"])
                                                       == reg["reintento_forma"]["intento_1"]["tool_input_crudo"])
            ctrl["respuesta_persistida"] = "reintento_por_forma"
        elif "reintento_corte" in reg:
            kw_c = dict(kw, max_tokens=reg["reintento_corte"]["max_tokens_reintento"])
            k_c = lc.compute_key(ns, lc.canonical_request(kw_c))
            fc = fila(k_c)
            ctrl.update({"clave_reintento_corte": k_c, "en_db_reintento_corte": fc is not None,
                         "db_base_stop_reason": fb["stop_reason"] if fb is not None else None})
            ctrl["tool_input_jsonl_igual_a_db"] = (fc is not None and tool_input_de_crudo(fc["raw_json"]) == reg["tool_input_crudo"])
            ctrl["respuesta_persistida"] = "reintento_por_corte"
        else:
            ctrl["tool_input_jsonl_igual_a_db"] = (fb is not None and tool_input_de_crudo(fb["raw_json"]) == reg["tool_input_crudo"])
            ctrl["respuesta_persistida"] = "pedido_base"
        ctrl["validacion_final_igual_a_intento0"] = (fin.get("validacion_final") == reg.get("validacion"))
        # Contenido: entidades, relaciones y omisiones de la validación, sin `marcas_e3` (una marca que E3 agrega a la
        # validación final al leer su veredicto; no cambia la extracción). None (cola por veredicto inutilizable) cuenta
        # como distinto.
        vf, v0 = fin.get("validacion_final"), reg.get("validacion")
        contenido = lambda v: None if v is None else {k: v.get(k) for k in ("entidades", "relaciones", "omisiones_no_prosa")}
        ctrl["contenido_final_igual_a_intento0"] = (vf is not None and contenido(vf) == contenido(v0))
        ctrl["claves_que_difieren_final_vs_intento0"] = (None if vf is None else
                                                        sorted(k for k in set(vf) | set(v0) if vf.get(k) != v0.get(k)))
        cuentas["en_db_e1"] += ctrl["en_db_e1"]
        cuentas["tool_input_igual"] += bool(ctrl["tool_input_jsonl_igual_a_db"])
        cuentas["validacion_final_igual"] += ctrl["validacion_final_igual_a_intento0"]
        cuentas["contenido_final_igual"] += ctrl["contenido_final_igual_a_intento0"]
        claves.append(ctrl)
        grupos = (["grupo_c"] if cid in grupo_c else []) + (["omisiones"] if cid in om_por_unidad else [])
        unidades.append({"chunk_id": cid, "to": cid.split("::")[0], "tipo_unidad": reg["tipo_unidad"], "titulo": reg["titulo"],
                         "grupos": grupos, "omisiones_t4": om_por_unidad.get(cid, []),
                         "n_reintentos": fin.get("n_reintentos", 0), "estado_final": fin["estado"],
                         "en_cola_humana": fin["estado"].startswith("cola_humana"),
                         "intento0_error": reg["error"], "intento0_stop_reason": reg["stop_reason"],
                         "intento0_usage": reg["usage"], "marcas_intento0": marcas,
                         "usage_db_base": ctrl.get("db_usage")})
        intento0.append(e1_lineas[cid])
    con.close()

    con_reintento = [u for u in unidades if u["n_reintentos"]]
    en_cola = [u for u in unidades if u["en_cola_humana"]]
    resumen = {
        "unidad": "U-COMP-E1, C0 (a)", "cuando_utc": ahora(), "perfil": perfil.nombre, "prefijo_hash": perfil.prefijo_hash,
        "modelo": MODELO_H, "namespace_e1": ns, "namespace_reintento_forma": ns_f,
        "db_e1": rel(DB_E1), "modo_apertura_db": "file:…?mode=ro&immutable=1",
        "fuentes": {"grupo_c": rel(T4 / "fichas_punto7_grupo_c.json"), "omisiones": rel(T4 / "fichas_punto8_omisiones.json"),
                    "e0": rel(E0), "salida_r2b": rel(SALIDA_R2B)},
        "grupo_c": {"fichas": len(gc["fichas"]), "con_mas_de_un_supuesto": len(grupo_c)},
        "omisiones": {"fichas": len(om["fichas"]), "unidades": len(om_por_unidad),
                      "unidades_con_dos_fichas": sorted(k for k, v in om_por_unidad.items() if len(v) > 1)},
        "en_los_dos_grupos": en_ambos, "total_unidades": len(ids),
        "por_to": dict(sorted(por_to.items())), "por_to_mandato": POR_TO_MANDATO,
        "por_to_coincide_con_mandato": dict(sorted(por_to.items())) == POR_TO_MANDATO,
        "todas_en_extracciones_e1": all(cid in e1_lineas for cid in ids),
        "todas_en_finales": all(cid in finales for cid in ids),
        "intento0_sin_error": sum(1 for u in unidades if u["intento0_error"] is None),
        "claves_en_db_e1": cuentas["en_db_e1"], "tool_input_jsonl_igual_a_db": cuentas["tool_input_igual"],
        "validacion_final_igual_a_intento0": cuentas["validacion_final_igual"],
        "contenido_final_igual_a_intento0": cuentas["contenido_final_igual"],
        "contenido_final_distinto": [u["chunk_id"] for u, c in zip(unidades, claves) if not c["contenido_final_igual_a_intento0"]],
        "con_reintento": {"n": len(con_reintento), "por_estado": dict(collections.Counter(u["estado_final"] for u in con_reintento)),
                          "unidades": [(u["chunk_id"], u["estado_final"]) for u in con_reintento]},
        "en_cola_humana": {"n": len(en_cola), "por_estado": dict(collections.Counter(u["estado_final"] for u in en_cola)),
                           "unidades": [(u["chunk_id"], u["estado_final"]) for u in en_cola]},
        "marcas_intento0": {u["chunk_id"]: u["marcas_intento0"] for u in unidades if u["marcas_intento0"]},
        "validacion_final_distinta": [u["chunk_id"] for u, c in zip(unidades, claves) if not c["validacion_final_igual_a_intento0"]],
        "claves_que_difieren_final_vs_intento0": {c["chunk_id"]: c["claves_que_difieren_final_vs_intento0"] for c in claves
                                                   if not c["validacion_final_igual_a_intento0"]},
    }
    (a.salida / "unidades.json").write_text(json.dumps({"unidad": "U-COMP-E1", "etapa": "C0 (a)", "cuando_utc": resumen["cuando_utc"],
                                                        "perfil": perfil.nombre, "prefijo_hash": perfil.prefijo_hash,
                                                        "modelo_linea_de_base": MODELO_H, "total": len(unidades),
                                                        "por_to": resumen["por_to"], "unidades": unidades},
                                                       ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (a.salida / "intento0_haiku.jsonl").write_text("\n".join(intento0) + "\n", encoding="utf-8")
    (a.salida / "claves_c0.json").write_text(json.dumps({"namespace_e1": ns, "namespace_reintento_forma": ns_f, "db_e1": rel(DB_E1),
                                                         "unidades": claves}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (a.salida / "resumen_c0a.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in resumen.items() if k not in ("fuentes",)}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
