"""
analisis_p5.py — U-PROMPT-R2, P5 (USD 0, sin API): las mediciones b, c, e, f, g y h del «seguí» de P5 sobre la salida
de la corrida (`resultados_p5.jsonl`, `reintento_forma_p5.json`), contra P4b (`p4b/salida/resultados_p4b.jsonl`,
brazo «p3c»: el mismo prefijo y las mismas unidades, sin temperatura fijada), y las fichas para la lectura de d.

Las definiciones son las de P4b (`p4b/analisis_p4b.py`, que se importa): normas (Obligacion, Restriccion y
Potestad), `hechos`, `omisiones_meta`, `normas_con_sujeto`, los porcentajes de `cap::tabla037` y sus copias. Cada
salida se valida con `runner_corpus.validador_perfil_r2` del perfil r2b, con `vistos_e3` = lo que validador_e1 le
pasaría a E3, como en P4b.

Mediciones:
  - b: E1 contra E1. Por unidad, si el `tool_input` de las dos corridas es igual byte a byte (su serialización JSON
    en el orden de la respuesta, sin espacios) y, si no, si lo es con las claves ordenadas; en las que difieren, los
    nodos por tipo, las normas, las relaciones y las omisiones de cada corrida, y la diferencia. Lo mismo de cada
    corrida contra P4b.
  - c: los hechos del ejemplo (`cla::5.1.1::intro` y `cla::5.1.1.1`) en cada corrida y en los dos brazos de P4b; el
    juicio de «una Condicion por cada condición» es de la lectura (marcas_p5.py).
  - e: tokens de salida por unidad y por carácter de texto propio, por corrida, contra P4b.
  - f: E3 contra E3 en las 10 unidades: el veredicto (`veredicto` del tool input y la evaluación determinística de
    ratchet_e3: completo, aceptable, faltantes y bloqueantes) y, donde difieren, los faltantes de cada corrida.
  - g y h: el pedido del reintento forzado y su `usage`.
  - `cap::6.2.2.6`: los porcentajes de `cap::tabla037` copiados y la omisión `tabla`, por corrida.
Fichas: una por unidad con las dos corridas, sin grupo ni origen, en el orden de
random.Random(f"{SEMILLA}:fichas").shuffle sobre los ids ordenados.

Escribe solo en --salida. Uso (desde la raíz de una copia con el código de P5):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p5/analisis_p5.py --trabajo DIR --salida DIR
"""
from __future__ import annotations

import argparse
import json
import random
import re
import statistics as st
import sys
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
sys.path.insert(0, str(AQUI.parent / "p4b"))
import analisis_p4b as A4  # noqa: E402 — las definiciones de P4b (pone en el path el pipeline)
import perfil_e1  # noqa: E402
import runner_corpus as RC  # noqa: E402

SEMILLA = "U-PROMPT-R2:P5:2026-10-05"
CORRIDAS = ("a", "b")
FUENTES = ("a", "b", "p4b")          # p4b = brazo p3c de P4b
RES_P4B = AQUI.parent / "p4b" / "salida" / "resultados_p4b.jsonl"
EJEMPLO = ("cla::5.1.1::intro", "cla::5.1.1.1")


def ser(ti, ordenado: bool = False) -> str:
    return json.dumps(ti, ensure_ascii=False, separators=(",", ":"), sort_keys=ordenado)


def forma_salida(ti: dict | None) -> dict:
    ti = ti if isinstance(ti, dict) else {}
    ents = [e for e in ti.get("entities") or [] if isinstance(e, dict)]
    rels = [r for r in ti.get("relations") or [] if isinstance(r, dict)]
    oms = [o for o in ti.get("omisiones") or [] if isinstance(o, dict)]
    tipos = Counter(e.get("type") for e in ents)
    return {"entidades": len(ents), "tipos": dict(sorted(tipos.items())),
            "normas": sum(tipos[t] for t in A4.NORMAS), "relaciones": len(rels),
            "predicados": dict(sorted(Counter(r.get("predicate") for r in rels).items())),
            "omisiones": len(oms), "omisiones_por_categoria": dict(sorted(Counter(o.get("categoria") for o in oms).items()))}


def diferencia(x: dict, y: dict) -> dict:
    tipos = sorted(set(x["tipos"]) | set(y["tipos"]))
    dt = {t: y["tipos"].get(t, 0) - x["tipos"].get(t, 0) for t in tipos}
    return {"tipos": {t: d for t, d in dt.items() if d}, "normas": y["normas"] - x["normas"],
            "relaciones": y["relaciones"] - x["relaciones"], "omisiones": y["omisiones"] - x["omisiones"],
            "nodos_movidos": sum(abs(d) for d in dt.values())}


def comparar(t1, t2) -> dict:
    igual = ser(t1) == ser(t2)
    out = {"igual_byte_a_byte": igual, "igual_con_claves_ordenadas": ser(t1, True) == ser(t2, True)}
    if not igual:
        f1, f2 = forma_salida(t1), forma_salida(t2)
        out.update({"primera": f1, "segunda": f2, "diferencia": diferencia(f1, f2)})
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--trabajo", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    sal = a.salida.resolve()
    if REPO in sal.parents or sal == REPO:
        raise SystemExit("--salida no puede estar dentro del repo")
    sal.mkdir(parents=True, exist_ok=True)
    sel = json.loads((AQUI / "salida" / "seleccion_p5.json").read_text(encoding="utf-8"))
    res = A4.jl(a.trabajo / "resultados_p5.jsonl")
    p4b = A4.jl(RES_P4B)
    perfil = perfil_e1.perfil("r2b")
    assert perfil.prefijo_hash == "322c5a23e9b7", perfil.prefijo_hash
    val_r2, _ = RC.validador_perfil_r2(perfil)
    ch = {}
    for to in A4.TOS:
        ch.update({c["id"]: c for c in json.loads((A4.E0 / f"chunks_{to}.json").read_text(encoding="utf-8"))})
    grupo = {u["id"]: u["grupo"] for u in sel["unidades"]}
    ids = [u["id"] for u in sel["unidades"]]

    def fuente(cid: str, f: str) -> dict | None:
        return res.get(f"{cid}|{f}") if f in CORRIDAS else p4b.get(f"{cid}|p3c")

    filas, por = {}, {f: {"salida": 0, "entrada": 0, "chars": 0, "normas": [0, 0], "errores": [], "cortes": [],
                          "escalon_3": [], "forma": [], "temperaturas": Counter()} for f in FUENTES}
    for cid in ids:
        fila = {"grupo": grupo[cid], "chars_propio": len(ch[cid].get("texto") or "")}
        for f in FUENTES:
            r = fuente(cid, f)
            if r is None:
                fila[f] = {"falta": True}
                continue
            ti = r.get("tool_input")
            vistos = RC.vistos_por_e3(r.get("validacion_e1"))
            v = val_r2(ti, ch[cid], vistos_e3=vistos) if ti is not None and vistos else None
            u = r.get("usage") or {}
            pf = por[f]
            pf["salida"] += u.get("output_tokens") or 0
            pf["entrada"] += u.get("input_tokens") or 0
            pf["chars"] += fila["chars_propio"]
            nc = A4.normas_con_sujeto(ti)
            pf["normas"][0] += nc[0]
            pf["normas"][1] += nc[1]
            pf["temperaturas"][repr(r.get("temperatura_pedido"))] += 1
            for k, lst in (("error", "errores"), ("reintento_corte", "cortes"), ("escalon_3", "escalon_3"),
                           ("reintento_forma", "forma")):
                if r.get(k):
                    pf[lst].append(cid)
            fila[f] = {"error": r.get("error"), "usage": u, "clave": r.get("clave"),
                       "tokens_salida_por_caracter": round((u.get("output_tokens") or 0) / fila["chars_propio"], 3)
                       if fila["chars_propio"] else None, "forma": forma_salida(ti), "normas_con_aplica_a": nc,
                       "hechos": A4.hechos(v), "meta_normativo": A4.omisiones_meta(v)}
        ra, rb, rp = (fuente(cid, f) for f in FUENTES)
        fila["a_contra_b"] = comparar(ra.get("tool_input"), rb.get("tool_input")) if ra and rb else None
        fila["a_contra_p4b"] = comparar(rp.get("tool_input"), ra.get("tool_input")) if ra and rp else None
        fila["b_contra_p4b"] = comparar(rp.get("tool_input"), rb.get("tool_input")) if rb and rp else None
        filas[cid] = fila

    # ---- b: identidad entre corridas ----
    def tabla_identidad(k: str) -> dict:
        iguales = [c for c in ids if (filas[c][k] or {}).get("igual_byte_a_byte")]
        ordenadas = [c for c in ids if (filas[c][k] or {}).get("igual_con_claves_ordenadas")]
        difieren = [c for c in ids if filas[c][k] is not None and not filas[c][k]["igual_byte_a_byte"]]
        return {"iguales_byte_a_byte": len(iguales), "iguales_con_claves_ordenadas": len(ordenadas),
                "de": sum(1 for c in ids if filas[c][k] is not None), "unidades_iguales": iguales,
                "difieren": {c: {"diferencia": filas[c][k]["diferencia"],
                                 "primera": {x: filas[c][k]["primera"][x] for x in ("tipos", "normas", "relaciones",
                                                                                   "omisiones")},
                                 "segunda": {x: filas[c][k]["segunda"][x] for x in ("tipos", "normas", "relaciones",
                                                                                   "omisiones")}}
                             for c in difieren}}
    med_b = {k: tabla_identidad(k) for k in ("a_contra_b", "a_contra_p4b", "b_contra_p4b")}
    for k in med_b:
        d = med_b[k]["difieren"].values()
        med_b[k]["resumen_de_las_que_difieren"] = {
            "unidades": len(d),
            "con_otro_numero_de_nodos_por_tipo": sum(1 for x in d if x["diferencia"]["tipos"]),
            "con_otro_numero_de_normas": sum(1 for x in d if x["diferencia"]["normas"]),
            "con_otro_numero_de_relaciones": sum(1 for x in d if x["diferencia"]["relaciones"]),
            "con_otro_numero_de_omisiones": sum(1 for x in d if x["diferencia"]["omisiones"]),
            "nodos_movidos_total": sum(x["diferencia"]["nodos_movidos"] for x in d),
            "nodos_movidos_max": max((x["diferencia"]["nodos_movidos"] for x in d), default=0)}

    # ---- c: el ejemplo ----
    med_c = {}
    for cid in EJEMPLO:
        med_c[cid] = {}
        for f, r in (("a", fuente(cid, "a")), ("b", fuente(cid, "b")), ("p4b_p3c", p4b.get(f"{cid}|p3c")),
                     ("p4b_anterior", p4b.get(f"{cid}|anterior"))):
            ti = (r or {}).get("tool_input") or {}
            ents = [e for e in ti.get("entities") or [] if isinstance(e, dict)]
            med_c[cid][f] = {"tipos": forma_salida(ti)["tipos"],
                             "definicion": [e.get("label") for e in ents if e.get("type") == "Definicion"],
                             "excepcion": [e.get("label") for e in ents if e.get("type") == "Excepcion"],
                             "operacion": [e.get("label") for e in ents if e.get("type") == "Operacion"],
                             "condicion": [e.get("label") for e in ents if e.get("type") == "Condicion"],
                             "omisiones": [(o.get("categoria"), A4.corto(o.get("tramo"), 120))
                                           for o in ti.get("omisiones") or [] if isinstance(o, dict)]}

    # ---- e: salida ----
    med_e = {}
    for f in FUENTES:
        pf = por[f]
        med_e[f] = {"tokens_salida": pf["salida"], "tokens_entrada_sin_cache": pf["entrada"], "chars_propio": pf["chars"],
                    "tokens_por_caracter": round(pf["salida"] / pf["chars"], 3) if pf["chars"] else None,
                    "mediana_por_unidad": st.median([(filas[c][f].get("usage") or {}).get("output_tokens") or 0
                                                     for c in ids if not filas[c][f].get("falta")])}
    for f in CORRIDAS:
        med_e[f]["salida_sobre_p4b"] = round(por[f]["salida"] / por["p4b"]["salida"], 3)
        med_e[f]["entrada_sobre_p4b"] = round(por[f]["entrada"] / por["p4b"]["entrada"], 3)
    med_e["b_sobre_a"] = round(por["b"]["salida"] / por["a"]["salida"], 3)
    med_e["por_unidad"] = {c: {f: (filas[c][f].get("usage") or {}).get("output_tokens") for f in FUENTES} for c in ids}

    # ---- cap::6.2.2.6 ----
    tablas = json.loads((A4.E0 / "tablas_cap.json").read_text(encoding="utf-8"))["tablas"]
    bloque = next(t["serializacion"]["bloque"] for t in tablas if t["id"] == "cap::tabla037")
    texto = ch["cap::6.2.2.6"]["texto"]
    prosa = texto[:texto.find("[TABLA cap::tabla037")] + texto[texto.find("[FIN TABLA cap::tabla037]"):]
    vals37 = [v for v in A4.porcentajes_tabla(bloque)
              if not re.search(r"(?<![\d,])" + re.escape(v) + r"\s?%", prosa)]
    med_f37 = {"porcentajes_tabla037_que_no_estan_en_la_prosa": vals37}
    for f in FUENTES:
        r = fuente("cap::6.2.2.6", f) or {}
        oms = (r.get("tool_input") or {}).get("omisiones") or []
        med_f37[f] = {"copias": A4.copias(r.get("tool_input"), vals37),
                      "omision_tabla": [A4.corto(o.get("tramo"), 160) for o in oms if isinstance(o, dict)
                                        and o.get("categoria") == "tabla"],
                      "forma": filas["cap::6.2.2.6"][f].get("forma")}

    # ---- E3 contra E3 ----
    med_e3 = {}
    for cid in sel["e3"]["todas"]:
        x, y = res.get(f"{cid}|e3a"), res.get(f"{cid}|e3b")
        if not x or not y:
            med_e3[cid] = {"falta": [k for k, v in (("e3a", x), ("e3b", y)) if not v]}
            continue

        def resumen(r):
            ti = r.get("tool_input") or {}
            return {"veredicto": ti.get("veredicto"), "es_completo_ok": r["es_completo_ok"], "aceptable": r["aceptable"],
                    "n_faltantes": r["n_faltantes"], "n_bloqueantes": r["n_bloqueantes"],
                    "faltantes": [{"tipo": f.get("tipo"), "severidad": f.get("severidad"), "ubicacion": f.get("ubicacion"),
                                   "cita": A4.corto(f.get("cita_textual_del_fuente"), 160),
                                   "cita_verificada": f.get("cita_verificada"), "nota": A4.corto(f.get("nota"), 260)}
                                  for f in r.get("faltantes") or []]}
        ra, rb = resumen(x), resumen(y)
        med_e3[cid] = {"misma_clave": x.get("clave") == y.get("clave"),
                       "igual_byte_a_byte": ser(x.get("tool_input")) == ser(y.get("tool_input")),
                       "mismo_veredicto": ra["veredicto"] == rb["veredicto"],
                       "misma_evaluacion": all(ra[k] == rb[k] for k in ("es_completo_ok", "aceptable", "n_bloqueantes")),
                       "a": ra, "b": rb}
    hechos_e3 = [v for v in med_e3.values() if "falta" not in v]
    med_e3_res = {"unidades": len(med_e3), "con_las_dos": len(hechos_e3),
                  "mismo_veredicto": sum(v["mismo_veredicto"] for v in hechos_e3),
                  "misma_evaluacion": sum(v["misma_evaluacion"] for v in hechos_e3),
                  "igual_byte_a_byte": sum(v["igual_byte_a_byte"] for v in hechos_e3),
                  "misma_clave": sum(v["misma_clave"] for v in hechos_e3)}

    # ---- g y h ----
    forma = json.loads((a.trabajo / "reintento_forma_p5.json").read_text(encoding="utf-8"))

    # ---- fichas ----
    orden = sorted(ids)
    random.Random(f"{SEMILLA}:fichas").shuffle(orden)
    md = ["# Fichas de P5 (sin grupo ni origen)", "",
          f"Orden: random.Random('{SEMILLA}:fichas').shuffle sobre los {len(ids)} ids ordenados. A y B = las dos "
          "corridas de E1 con temperatura 0 (prefijo `322c5a23e9b7`, el código de P5), validadas con el validador "
          "del perfil r2b. Si las dos salidas son iguales byte a byte, la ficha lo dice y muestra una.", ""]
    for n, cid in enumerate(orden, 1):
        c = ch[cid]
        md += [f"## Ficha {n} — `{cid}`", "", "**Texto propio:**", "", "```", (c.get("texto") or "").strip()[:3500],
               "```", f"**Heredado:** {' / '.join(A4.corto(h.get('texto'), 260) for h in c.get('herencia') or [])}", ""]
        iguales = (filas[cid]["a_contra_b"] or {}).get("igual_byte_a_byte")
        for f in (("a",) if iguales else CORRIDAS):
            x = filas[cid][f]
            if x.get("falta"):
                md += [f"**{f.upper()}** — sin salida", ""]
                continue
            h = x["hechos"]
            md += [f"**{'A = B (iguales byte a byte)' if iguales else f.upper()}** — error: {x['error']}; salida: "
                   f"{(x['usage'] or {}).get('output_tokens')} tokens", ""]
            md += [f"- {e['tipo']} «{e['label']}»: {e['descripcion']}"
                   + (f" ‖ tramo ({e['tramo_verificado']}): «{e['tramo']}»" if e.get("tramo") else "")
                   + (f" ‖ umbrales: {e['umbrales']}" if e.get("umbrales") else "")
                   + (f" ‖ no definidas: {json.dumps(e['no_definidas'], ensure_ascii=False)}" if e.get("no_definidas")
                      else "")
                   for e in h.get("entidades", [])]
            md += [f"  - {r}" for r in h.get("relaciones", [])]
            md += [f"  - mención: {m['pred']} «{m['mencion']}» (verificada: {m['verificada']})"
                   for m in h.get("menciones", [])]
            md += [f"  - rechazo: {r}" for r in h.get("rechazos", [])]
            md += [f"  - omisión {o['categoria']} ({o['verificacion']}): «{o['tramo']}» — nota: {o['nota']}"
                   for o in h.get("omisiones", [])]
            md += [f"  - heredado_compuesto: {h.get('heredado_compuesto')}", ""]
    (sal / "fichas_p5.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    def menciones(f: str) -> dict:
        ms = [m for c in ids for m in ((filas[c][f].get("hechos") or {}).get("menciones") or [])]
        return {"menciones": len(ms), "verifican": sum(1 for m in ms if m.get("verificada") not in (None, "no")),
                "unidades_con_mencion_que_no_verifica": sorted({c for c in ids for m in ((filas[c][f].get("hechos")
                                                                or {}).get("menciones") or [])
                                                                if m.get("verificada") in (None, "no")})}

    def meta(f: str) -> dict:
        ms = [m for c in ids for m in filas[c][f].get("meta_normativo") or []]
        return {"omisiones": len(ms), "con_marca": sum(1 for m in ms if m["clases"]),
                "unidades": sorted({c for c in ids if filas[c][f].get("meta_normativo")})}

    resumen = {f: {"unidades_con_salida": sum(1 for c in ids if not filas[c][f].get("falta")),
                   "errores": por[f]["errores"], "reintento_corte": por[f]["cortes"], "escalon_3": por[f]["escalon_3"],
                   "reintento_forma": por[f]["forma"], "temperaturas_del_pedido": dict(por[f]["temperaturas"]),
                   "normas_con_aplica_a": {"con": por[f]["normas"][0], "normas": por[f]["normas"][1]},
                   "menciones_de_sujeto": menciones(f), "omisiones_meta_normativo": meta(f)}
               for f in FUENTES}
    out = {"comando": "data/experiment/prompt_r2/p5/analisis_p5.py --trabajo DIR --salida DIR",
           "orden_fichas": orden, "resumen": resumen, "medicion_b": med_b, "medicion_c": med_c, "medicion_e": med_e,
           "cap_6_2_2_6": med_f37, "medicion_f_e3": {"resumen": med_e3_res, "unidades": med_e3},
           "medicion_g_h": forma,
           "meta_normativo": {f: [{"id": c, **m} for c in ids for m in filas[c][f].get("meta_normativo") or []]
                              for f in FUENTES},
           "filas": filas}
    (sal / "analisis_p5.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"resumen": resumen, "b": {k: {x: v[x] for x in ("iguales_byte_a_byte",
                                                                      "iguales_con_claves_ordenadas", "de",
                                                                      "resumen_de_las_que_difieren")}
                                                for k, v in med_b.items()},
                      "e": {k: v for k, v in med_e.items() if k != "por_unidad"}, "e3": med_e3_res}, ensure_ascii=False,
                     indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
