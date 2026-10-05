"""
analisis_p4b.py — U-PROMPT-R2, P4b (USD 0, sin API): validación de las dos salidas con el validador de `bb212f1`, los
hechos mecánicos de cada grupo, las fichas cegadas y las mediciones c, d, e y f del «seguí» de P4b.

Validación: las dos salidas, con `runner_corpus.validador_perfil_r2` del perfil r2b de `bb212f1` (forma «r2»), sobre
el chunk de la e0-r2b, con `vistos_e3` = lo que validador_e1 de cada release le pasaría a E3 (`vistos_por_e3` sobre la
`validacion_e1` guardada del brazo). Así el contador de omisiones `meta_normativo` es el mismo en los dos brazos.

Mediciones:
  - c: normas (Obligacion, Restriccion y Potestad) del crudo con `aplica_a` de origen en ellas, como la referencia
    de P4 (129 de 143 con el prefijo sellado y 111 de 157 con el de P3b-2, que este script reproduce);
  - d: el contador del validador: `omisiones.meta_normativo_con_marca`, sus siete clases y las tres subclases de
    modalidad, y `omisiones.categoria:meta_normativo`; por omisión, el tramo, sus clases y subclases, y si queda
    marcada solo por la subclase forma;
  - e: tokens de salida por unidad y por carácter de texto propio;
  - f: en `cap::6.2.2.6`, los porcentajes de las celdas de `cap::tabla037` (su bloque en `tablas_cap.json` de la
    e0-r2b) que no están en la prosa de la unidad y aparecen en la salida, fuera de las omisiones, y la omisión `tabla`;
  - los hechos por grupo que la lectura asistida necesita (tipos, relaciones, Condicion con su `condicion_de`,
    `exceptua` y rechazos, el contador `tramo_entidad.solo_heredado:heredado_compuesto`, menciones de sujeto).
Fichas: una por unidad con los dos brazos, sin grupo ni origen, en el orden de
random.Random(f"{SEMILLA}:fichas").shuffle sobre los ids ordenados.

Escribe solo en --salida. Uso (desde la raíz de la copia de `bb212f1`):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p4b/analisis_p4b.py --trabajo DIR --salida DIR
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
REX = REPO / "data" / "experiment" / "reextraccion_v2"
for sub in ("e1_extractor", "e3_verificador", "e2_reduce", "corpus_v2", "e0_chunking"):
    sys.path.insert(0, str(REX / sub))
sys.path.insert(0, str(REX))
sys.path.insert(0, str(REPO / "data" / "experiment" / "pyd_r2" / "code"))
import perfil_e1  # noqa: E402
import prompt_r2b as PR  # noqa: E402
import runner_corpus as RC  # noqa: E402
import validador_r2 as V  # noqa: E402

SEMILLA = "U-PROMPT-R2:P4b:2026-10-04"
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
E0 = REX / "e0_chunking" / "salida_tanda0_r2b"
BRAZOS = ("anterior", "p3c")
NORMAS = ("Obligacion", "Restriccion", "Potestad")
SUJETO = ("aplica_a", "ejecuta")


def jl(p: Path) -> dict:
    out = {}
    for x in p.read_text(encoding="utf-8").splitlines():
        if x.strip():
            r = json.loads(x)
            out[r["chunk_id"]] = r
    return out


def corto(s, n=220):
    s = " ".join(str(s or "").split())
    return s if len(s) <= n else s[:n] + "…"


def normas_con_sujeto(ti: dict | None) -> tuple[int, int]:
    """(normas con aplica_a de origen en ellas, normas), en el crudo: la medida de la referencia de P4."""
    if not ti:
        return 0, 0
    ents = [e for e in ti.get("entities") or [] if isinstance(e, dict) and e.get("type") in NORMAS]
    rels = [r for r in ti.get("relations") or [] if isinstance(r, dict)]
    con = sum(any(r.get("predicate") == "aplica_a" and r.get("source") == e.get("local_id") for r in rels) for e in ents)
    return con, len(ents)


def omisiones_meta(val: dict | None) -> list[dict]:
    out = []
    for o in (val or {}).get("omisiones") or []:
        if o.get("categoria") != "meta_normativo":
            continue
        t = o.get("tramo")
        cl = V.marcas_meta_normativo(t) if t else []
        sub = V.subclases_modalidad(t) if t and "modalidad" in cl else []
        out.append({"tramo": t, "verificacion": o.get("tramo_verificado"), "nota": o.get("nota"), "clases": cl,
                    "subclases_modalidad": sub, "solo_forma": cl == ["modalidad"] and sub == ["forma"]})
    return out


def hechos(val: dict | None) -> dict:
    if not val:
        return {"sin_validacion": True}
    ents = {e["local_id"]: e for e in val.get("entidades") or []}
    lab = {k: f"{e['type']}:{corto(e['label'], 70)}" for k, e in ents.items()}
    rels = val.get("relaciones") or []
    cont = val.get("contadores") or {}
    return {
        "entidades": [{"tipo": e["type"], "label": corto(e["label"], 90),
                       "descripcion": corto((e.get("properties") or {}).get("descripcion"), 300),
                       "tramo": corto((e.get("provenance") or {}).get("tramo"), 200),
                       "tramo_verificado": (e.get("provenance") or {}).get("tramo_verificado"),
                       "umbrales": e.get("umbrales_tramos") or None,
                       "no_definidas": e.get("properties_no_definidas") or None}
                      for e in ents.values() if e["type"] != "TextoOrdenado"],
        "relaciones": [f"{lab.get(r.get('source'), r.get('source') or '[sujeto]')} --{r['predicate']}--> "
                       f"{lab.get(r.get('target'), r.get('sujeto_id_resuelto') or r.get('sujeto_mencion') or r.get('target'))}"
                       for r in rels],
        "menciones": [{"pred": r["predicate"], "mencion": corto(r.get("sujeto_mencion"), 80),
                       "verificada": r.get("mencion_verificada"),
                       "sujeto_id": r.get("sujeto_id_resuelto") or r.get("sujeto_id")}
                      for r in rels if r.get("predicate") in SUJETO],
        "condicion_de": [{"de": lab.get(r.get("source")), "a": lab.get(r.get("target"))}
                         for r in rels if r.get("predicate") == "condicion_de"],
        "rechazos": [f"{x['motivo']}: {corto(x.get('detalle'), 100)}" for x in val.get("rechazos") or []],
        "omisiones": [{"categoria": o.get("categoria"), "tramo": corto(o.get("tramo"), 160),
                       "verificacion": o.get("tramo_verificado"), "nota": corto(o.get("nota"), 140)}
                      for o in val.get("omisiones") or []],
        "heredado_compuesto": ((cont.get("tramo_entidad") or {}).get("solo_heredado:heredado_compuesto", 0)),
        "contador_omisiones": {k: v for k, v in (cont.get("omisiones") or {}).items()
                               if k.startswith(("meta_normativo_con_marca", "categoria:"))},
    }


def porcentajes_tabla(bloque: str) -> list[str]:
    """Los porcentajes de las celdas de una tabla serializada de E0 (su bloque), sin repetir: «40», «30»…"""
    return sorted({m for m in re.findall(r"= (\d+(?:,\d+)?)\s?%", bloque)}, key=lambda x: float(x.replace(",", ".")))


def copias(ti: dict, valores: list[str]) -> dict:
    """Dónde aparece cada porcentaje de la tabla en la salida, fuera de las omisiones: en un texto («40%», «40 %») o
    como valor de un umbral."""
    out: dict = {}

    def recorrer(x, ruta):
        if isinstance(x, dict):
            for k, v in x.items():
                if k == "omisiones":
                    continue
                if k in ("valor", "valor_numerico") and str(v).replace(".", ",") in valores:
                    out.setdefault(str(v).replace(".", ","), []).append(f"{ruta}.{k}")
                recorrer(v, f"{ruta}.{k}")
        elif isinstance(x, list):
            for i, v in enumerate(x):
                recorrer(v, f"{ruta}[{i}]")
        elif isinstance(x, str):
            for val in valores:
                if re.search(r"(?<![\d,])" + re.escape(val) + r"\s?%", x):
                    out.setdefault(val, []).append(ruta)
    recorrer(ti or {}, "")
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
    sel = json.loads((AQUI / "salida" / "seleccion_p4b.json").read_text(encoding="utf-8"))
    res = jl(a.trabajo / "resultados_p4b.jsonl")
    perfil = perfil_e1.perfil("r2b")
    assert perfil.prefijo_hash == "322c5a23e9b7", perfil.prefijo_hash
    val_r2, pol = RC.validador_perfil_r2(perfil)
    ch = {}
    for to in TOS:
        ch.update({c["id"]: c for c in json.loads((E0 / f"chunks_{to}.json").read_text(encoding="utf-8"))})
    grupo = {c: g for g, ids in sel["grupos"].items() for c in ids}

    filas, por_brazo = {}, {b: {"contador": Counter(), "normas": [0, 0], "meta": [], "salida": 0, "chars": 0,
                                "errores": [], "cortes": [], "escalon_3": [], "forma": []} for b in BRAZOS}
    for cid in sorted(grupo):
        f = {"grupo": grupo[cid], "chars_propio": len(ch[cid].get("texto") or ""), "es_item": PR.es_item(ch[cid])}
        for b in BRAZOS:
            r = res.get(f"{cid}|{b}")
            if r is None:
                f[b] = {"falta": True}
                continue
            vistos = RC.vistos_por_e3(r.get("validacion_e1"))
            v = val_r2(r["tool_input"], ch[cid], vistos_e3=vistos) if r.get("tool_input") is not None and vistos else None
            h = hechos(v)
            meta = omisiones_meta(v)
            nc = normas_con_sujeto(r.get("tool_input"))
            pb = por_brazo[b]
            pb["contador"].update(h.get("contador_omisiones") or {})
            pb["normas"][0] += nc[0]
            pb["normas"][1] += nc[1]
            pb["meta"] += [{"id": cid, **m} for m in meta]
            out_t = (r.get("usage") or {}).get("output_tokens") or 0
            pb["salida"] += out_t
            pb["chars"] += f["chars_propio"]
            for k, lst in (("error", "errores"), ("reintento_corte", "cortes"), ("escalon_3", "escalon_3"),
                           ("reintento_forma", "forma")):
                if r.get(k):
                    pb[lst].append(cid)
            f[b] = {"error": r.get("error"), "usage": r.get("usage"), "normas_con_aplica_a": nc,
                    "tokens_salida_por_caracter": round(out_t / f["chars_propio"], 3) if f["chars_propio"] else None,
                    "hechos": h, "meta_normativo": meta}
        filas[cid] = f

    # ---- f: cap::6.2.2.6 y los valores de cap::tabla037 ----
    tablas = json.loads((E0 / "tablas_cap.json").read_text(encoding="utf-8"))["tablas"]
    bloque = next(t["serializacion"]["bloque"] for t in tablas if t["id"] == "cap::tabla037")
    texto = ch["cap::6.2.2.6"]["texto"]
    prosa = texto[:texto.find("[TABLA cap::tabla037")] + texto[texto.find("[FIN TABLA cap::tabla037]"):]
    vals37 = [v for v in porcentajes_tabla(bloque) if not re.search(r"(?<![\d,])" + re.escape(v) + r"\s?%", prosa)]
    med_f = {"porcentajes_tabla037_que_no_estan_en_la_prosa": vals37}
    for b in BRAZOS:
        r = res.get(f"cap::6.2.2.6|{b}") or {}
        oms = (r.get("tool_input") or {}).get("omisiones") or []
        med_f[b] = {"copias": copias(r.get("tool_input"), vals37),
                    "omision_tabla": [corto(o.get("tramo"), 160) for o in oms if isinstance(o, dict)
                                      and o.get("categoria") == "tabla"]}

    # ---- fichas cegadas ----
    ids = sorted(filas)
    orden = list(ids)
    random.Random(f"{SEMILLA}:fichas").shuffle(orden)
    md = ["# Fichas de P4b (cegadas: sin grupo ni origen)", "",
          f"Orden: random.Random('{SEMILLA}:fichas').shuffle sobre los {len(ids)} ids ordenados. ANTERIOR = prefijo "
          "`3817de475c93` con el código de `44c6e1b`; P3C = prefijo `322c5a23e9b7` con el código de `bb212f1`; la misma "
          "e0-r2b; las dos salidas, validadas con el validador de `bb212f1`.", ""]
    for n, cid in enumerate(orden, 1):
        c = ch[cid]
        md += [f"## Ficha {n} — `{cid}`", "", "**Texto propio:**", "", "```", (c.get("texto") or "").strip()[:3500], "```",
               f"**Heredado:** {' / '.join(corto(h.get('texto'), 260) for h in c.get('herencia') or [])}", ""]
        for b in BRAZOS:
            x = filas[cid][b]
            if x.get("falta"):
                md += [f"**{b.upper()}** — sin salida", ""]
                continue
            h = x["hechos"]
            md += [f"**{b.upper()}** — error: {x['error']}; salida: {(x['usage'] or {}).get('output_tokens')} tokens", ""]
            md += [f"- {e['tipo']} «{e['label']}»: {e['descripcion']}"
                   + (f" ‖ tramo ({e['tramo_verificado']}): «{e['tramo']}»" if e.get("tramo") else "")
                   + (f" ‖ umbrales: {e['umbrales']}" if e.get("umbrales") else "")
                   + (f" ‖ no definidas: {json.dumps(e['no_definidas'], ensure_ascii=False)}" if e.get("no_definidas") else "")
                   for e in h.get("entidades", [])]
            md += [f"  - {r}" for r in h.get("relaciones", [])]
            md += [f"  - rechazo: {r}" for r in h.get("rechazos", [])]
            md += [f"  - omisión {o['categoria']} ({o['verificacion']}): «{o['tramo']}» — nota: {o['nota']}"
                   for o in h.get("omisiones", [])]
            md += [f"  - heredado_compuesto: {h.get('heredado_compuesto')}", ""]
    (sal / "fichas_p4b.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    # ---- resumen por brazo ----
    resumen = {}
    for b in BRAZOS:
        pb = por_brazo[b]
        cont = pb["contador"]
        marc = [m for m in pb["meta"] if m["clases"]]
        resumen[b] = {
            "unidades_con_salida": sum(1 for f in filas.values() if not f[b].get("falta")),
            "errores": pb["errores"], "reintento_corte": pb["cortes"], "escalon_3": pb["escalon_3"],
            "reintento_forma": pb["forma"],
            "normas_con_aplica_a": {"con": pb["normas"][0], "normas": pb["normas"][1]},
            "omisiones_meta_normativo": {
                "total_validador": cont.get("categoria:meta_normativo", 0), "total_leidas": len(pb["meta"]),
                "con_marca_validador": cont.get("meta_normativo_con_marca", 0), "con_marca": len(marc),
                "por_clase": {c: cont.get(f"meta_normativo_con_marca:{c}", 0) for c in V.MARCAS_META_NORMATIVO},
                "por_subclase_modalidad": {s: cont.get(f"meta_normativo_con_marca:modalidad.{s}", 0)
                                           for s in V.SUBCLASES_MODALIDAD},
                "solo_forma": sum(m["solo_forma"] for m in pb["meta"])},
            "salida": {"tokens": pb["salida"], "chars_propio": pb["chars"],
                       "tokens_por_caracter_agregado": round(pb["salida"] / pb["chars"], 3) if pb["chars"] else None,
                       "mediana_tokens_por_unidad": st.median([(f[b].get("usage") or {}).get("output_tokens") or 0
                                                               for f in filas.values() if not f[b].get("falta")])}}
    out = {"comando": "data/experiment/prompt_r2/p4b/analisis_p4b.py --trabajo DIR --salida DIR",
           "orden_fichas": orden, "resumen": resumen, "medicion_f": med_f,
           "meta_normativo": {b: por_brazo[b]["meta"] for b in BRAZOS}, "filas": filas}
    (sal / "analisis_p4b.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"fichas": len(orden), "resumen": resumen, "medicion_f": med_f}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
