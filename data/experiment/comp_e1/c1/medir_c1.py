"""
medir_c1.py — U-COMP-E1, C1: M3 y M4 por script (USD 0), sobre resultados_<etiqueta>.jsonl de --salida.

M3 (variación entre las dos corridas de cada brazo): unidades iguales byte a byte (la salida canónica de la herramienta,
json.dumps con claves ordenadas) con la misma clave de caché; cortes, respuestas sin herramienta, mal formadas y rechazos
(refusal), por corrida; las dos unidades cuyo intento 0 de Haiku es un reintento llevan su marca.
M4 (por brazo y corrida): elementos con tramo no verificable por código (nivel «no») sobre lo emitido, con los niveles
«exacta» y «tokens», de validador_r2 (entidades: contadores.tramo_entidad; omisiones: tramo_verificado); elementos fuera
del esquema o del tool schema (rechazos de validador_r2 por motivo; tipos y predicados resueltos por forma o alias;
campos no definidos); costo por unidad y por brazo con tokens de entrada (variable, lectura y escritura de caché) y de
salida. Escribe m3_c1.json, m4_c1.json y m3_m4_c1.md. Doble corrida byte a byte: salida determinística (sin horas).
  PYTHONDONTWRITEBYTECODE=1 <venv>/bin/python -B data/experiment/comp_e1/c1/medir_c1.py --salida DIR
"""
from __future__ import annotations

import argparse
import collections
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun_c1 as C  # noqa: E402

ETIQUETAS = ("S1", "S2", "O1", "O2")


def canon(x) -> str:
    return json.dumps(x, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def m3(res: dict) -> dict:
    out = {}
    for b in ("S", "O"):
        c1, c2 = res.get(f"{b}1", {}), res.get(f"{b}2", {})
        comunes = sorted(set(c1) & set(c2))
        iguales = [cid for cid in comunes if c1[cid].get("tool_input_crudo") is not None
                   and canon(c1[cid]["tool_input_crudo"]) == canon(c2[cid]["tool_input_crudo"])]
        clave_igual = [cid for cid in comunes if c1[cid]["llamadas"] and c2[cid]["llamadas"]
                       and c1[cid]["llamadas"][0]["clave"] == c2[cid]["llamadas"][0]["clave"]]
        ambas_ok = [cid for cid in comunes if c1[cid].get("error") is None and c2[cid].get("error") is None]

        def cuenta(c):
            return {"registradas": len(c), "con_error": sum(1 for v in c.values() if v.get("error")),
                    "cortes": sum(1 for v in c.values() if v.get("reintento_corte")),
                    "cortes_tras_reintento": sum(1 for v in c.values() if v.get("error") == "max_tokens_hit_tras_reintento"),
                    "sin_herramienta": sum(1 for v in c.values() if (v.get("reintento_forma") or {}).get("causa") == "sin_herramienta"),
                    "mal_formadas": sum(1 for v in c.values() if (v.get("reintento_forma") or {}).get("causa") == "mal_formada"),
                    "sin_herramienta_o_mal_formadas_tras_reintento": sum(1 for v in c.values() if "tras_reintento" in (v.get("error") or "")
                                                                         and v.get("error") != "max_tokens_hit_tras_reintento"),
                    "refusals": sum(1 for v in c.values() if v.get("stop_reason") == "refusal" or "refusal" in (v.get("error") or "")),
                    "errores_api": sum(1 for v in c.values() if (v.get("error") or "").startswith("api_error")),
                    "errores": {k: v["error"] for k, v in sorted(c.items()) if v.get("error")}}
        out[b] = {"modelo": C.MODELOS[b], "unidades_en_las_dos": len(comunes), "misma_clave": len(clave_igual),
                  "iguales_byte_a_byte": len(iguales), "iguales_byte_a_byte_ids": iguales,
                  "ambas_sin_error": len(ambas_ok),
                  "iguales_sobre_ambas_sin_error": f"{len([c for c in iguales if c in ambas_ok])}/{len(ambas_ok)}",
                  "corrida_1": cuenta(c1), "corrida_2": cuenta(c2),
                  "marcas_intento0_haiku": {cid: m for cid, m in C.MARCAS_INTENTO0_HAIKU.items()}}
    return out


def tramos_omisiones(val_r2: dict) -> collections.Counter:
    c = collections.Counter()
    for o in (val_r2 or {}).get("omisiones") or []:
        c[o.get("tramo_verificado") or "sin_campo"] += 1
    return c


def m4(res: dict, intento0: dict) -> dict:
    out = {}
    for et in ETIQUETAS:
        c = res.get(et)
        if not c:
            continue
        b = et[0]
        p = C.PRECIOS[b]
        tramo_ent = collections.Counter()
        tramo_om = collections.Counter()
        rechazos = collections.Counter()
        tipo_trat = collections.Counter()
        pred_trat = collections.Counter()
        campos_nd = collections.Counter()
        n_ent = n_rel = n_om = 0
        por_unidad = []
        for cid, v in sorted(c.items()):
            vr = v.get("validacion_r2") or {}
            cont = vr.get("contadores") or {}
            for k, n in (cont.get("tramo_entidad") or {}).items():
                tramo_ent[k] += n
            for k, n in tramos_omisiones(vr).items():
                tramo_om[k] += n
            for k, n in ((vr.get("metricas") or {}).get("rechazos_por_motivo") or {}).items():
                rechazos[k] += n
            for k, n in (cont.get("tipo_entidad") or {}).items():
                tipo_trat[k] += n
            for k, n in (cont.get("predicado") or {}).items():
                pred_trat[k] += n
            for campo in ("campos_del_item_entidad", "campos_de_la_salida", "campos_del_item_relacion", "claves"):
                for k, n in (cont.get(campo) or {}).items():
                    campos_nd[f"{campo}.{k}"] += n
            m = vr.get("metricas") or {}
            n_ent += m.get("entities_out", 0); n_rel += m.get("relations_out", 0); n_om += m.get("omisiones_out", 0)
            u = v.get("usage_total") or {}
            h = (intento0.get(cid) or {}).get("usage") or {}
            por_unidad.append({"chunk_id": cid, "error": v.get("error"), "n_llamadas": v.get("n_llamadas"),
                               "entrada_variable": u.get("input_tokens"), "cache_read": u.get("cache_read_tokens"),
                               "cache_write": u.get("cache_write_tokens"), "salida": u.get("output_tokens"),
                               "salida_haiku_intento0": h.get("output_tokens"),
                               "costo_usd": v.get("costo_usd"), "segundos": v.get("segundos"),
                               "entidades": m.get("entities_out"), "relaciones": m.get("relations_out"), "omisiones": m.get("omisiones_out"),
                               "tramo_entidad": cont.get("tramo_entidad"), "tramo_omisiones": dict(tramos_omisiones(vr)) or None})
        tot = {k: sum((v.get("usage_total") or {}).get(k, 0) for v in c.values())
               for k in ("input_tokens", "output_tokens", "cache_write_tokens", "cache_read_tokens")}
        costo = sum(v.get("costo_usd", 0.0) for v in c.values())
        emitidos_ent = sum(tramo_ent.values())
        emitidos_om = sum(tramo_om.values())
        out[et] = {"modelo": C.MODELOS[b], "unidades": len(c), "con_error": sum(1 for v in c.values() if v.get("error")),
                   "elementos_emitidos": {"entidades": n_ent, "relaciones": n_rel, "omisiones": n_om},
                   "tramo_entidades": {"niveles": dict(tramo_ent), "no_verificable": f"{tramo_ent.get('no', 0)}/{emitidos_ent}"},
                   "tramo_omisiones": {"niveles": dict(tramo_om), "no_verificable": f"{tramo_om.get('no', 0)}/{emitidos_om}"},
                   "fuera_del_esquema_o_del_tool_schema": {"rechazos_validador_r2_por_motivo": dict(sorted(rechazos.items())),
                                                           "tipo_entidad_por_tratamiento": dict(sorted(tipo_trat.items())),
                                                           "predicado_por_tratamiento": dict(sorted(pred_trat.items())),
                                                           "campos_no_definidos_y_claves": dict(sorted(campos_nd.items()))},
                   "tokens": tot, "costo_usd": round(costo, 4),
                   "costo_usd_por_unidad": round(costo / len(c), 6) if c else None,
                   "salida_total_haiku_intento0": sum((intento0.get(cid) or {}).get("usage", {}).get("output_tokens", 0) for cid in c),
                   "por_unidad": por_unidad}
    return out


def tabla(m3d: dict, m4d: dict) -> str:
    l = ["# M3 y M4 de C1 — U-COMP-E1 (generado por medir_c1.py)", "",
         "## M3 — variación entre las dos corridas de cada brazo", "",
         "| brazo | en las dos | misma clave | iguales byte a byte | ambas sin error | iguales / ambas sin error | cortes c1/c2 | sin herramienta c1/c2 | mal formadas c1/c2 | refusals c1/c2 | errores c1/c2 |",
         "|---|---|---|---|---|---|---|---|---|---|---|"]
    for b, d in m3d.items():
        a, c = d["corrida_1"], d["corrida_2"]
        l.append(f"| {b} ({d['modelo']}) | {d['unidades_en_las_dos']} | {d['misma_clave']} | {d['iguales_byte_a_byte']} | {d['ambas_sin_error']} | "
                 f"{d['iguales_sobre_ambas_sin_error']} | {a['cortes']}/{c['cortes']} | {a['sin_herramienta']}/{c['sin_herramienta']} | "
                 f"{a['mal_formadas']}/{c['mal_formadas']} | {a['refusals']}/{c['refusals']} | {a['con_error']}/{c['con_error']} |")
    l += ["", "Marcas del intento 0 de Haiku (C0 (a); nota al pie del 06/10/2026): " +
          "; ".join(f"`{k}`: {v}" for k, v in C.MARCAS_INTENTO0_HAIKU.items()), "",
          "## M4 — por brazo y corrida", "",
          "| corrida | unidades | con error | entidades / relaciones / omisiones | tramo de entidad no verificable | tramo de omisión no verificable | rechazos r2 | entrada variable | cache read | cache write | salida | salida Haiku (intento 0) | USD | USD/unidad |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for et, d in m4d.items():
        e = d["elementos_emitidos"]; t = d["tokens"]
        l.append(f"| {et} | {d['unidades']} | {d['con_error']} | {e['entidades']} / {e['relaciones']} / {e['omisiones']} | "
                 f"{d['tramo_entidades']['no_verificable']} | {d['tramo_omisiones']['no_verificable']} | "
                 f"{sum(d['fuera_del_esquema_o_del_tool_schema']['rechazos_validador_r2_por_motivo'].values())} | "
                 f"{t['input_tokens']} | {t['cache_read_tokens']} | {t['cache_write_tokens']} | {t['output_tokens']} | "
                 f"{d['salida_total_haiku_intento0']} | {d['costo_usd']} | {d['costo_usd_por_unidad']} |")
    return "\n".join(l) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    res = {et: C.jsonl_last_wins(a.salida / f"resultados_{et}.jsonl") for et in ETIQUETAS
           if (a.salida / f"resultados_{et}.jsonl").exists()}
    intento0 = C.jsonl_last_wins(C.INTENTO0_JSONL)
    m3d, m4d = m3(res), m4(res, intento0)
    (a.salida / "m3_c1.json").write_text(json.dumps(m3d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (a.salida / "m4_c1.json").write_text(json.dumps(m4d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (a.salida / "m3_m4_c1.md").write_text(tabla(m3d, m4d), encoding="utf-8")
    print(tabla(m3d, m4d))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
