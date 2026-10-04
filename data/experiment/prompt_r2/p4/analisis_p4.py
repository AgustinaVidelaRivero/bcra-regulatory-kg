"""
analisis_p4.py — U-PROMPT-R2, P4.b y P4.c (USD 0, sin API): validación r2 de las dos salidas de la pareada, contadores
del validador por brazo, hechos mecánicos de cada dimensión de las fichas, fichas pareadas cegadas y las mediciones
mecánicas (a, c y e del «seguí» de P4).

Validación (la de la cadena de cada release, `runner_corpus.validador_perfil_r2`, con sus candados):
  - brazo sellado: forma «v3» sobre el chunk de la E0 legada, como la cadena r2a;
  - brazo nuevo: forma «r2» sobre el chunk de la e0-r2, con `vistos_e3` = lo que validador_e1 le pasaría a E3
    (`runner_corpus.vistos_por_e3`): la pareada no corre E3 salvo en su pata.
Contadores por brazo (FRENO P4): vocabulario retirado (claves heredadas de v3, `sujeto_propuesto` leído como
mención, tipos y predicados resueltos por alias o forma), valores fuera de lista (`fuera_de_lista`) y tramos no
verificados (tramo de evidencia de la entidad, mención del sujeto, tramo de la omisión y tramo de umbral, este con
`validador_r2.verificar_tramo` contra el texto propio y heredado).
Fichas: una por chunk con los dos brazos, sin grupo, estrato ni origen (protocolo de ESQ-3b), en el orden de
random.Random(f"{SEMILLA}:fichas").shuffle sobre los ids ordenados.

Escribe solo en --salida. Uso (desde la raíz de una COPIA del repo):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p4/analisis_p4.py \
      --muestra M --e0-fuera DIR --resultados R --salida DIR
"""
from __future__ import annotations

import argparse
import json
import random
import statistics as st
import sys
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
for sub in ("e1_extractor", "e3_verificador", "e2_reduce", "corpus_v2"):
    sys.path.insert(0, str(REX / sub))
sys.path.insert(0, str(REX))
sys.path.insert(0, str(REPO / "data" / "experiment" / "pyd_r2" / "code"))
import perfil_e1  # noqa: E402
import prompt_r2b as PR  # noqa: E402
import runner_corpus as RC  # noqa: E402
import validador_r2 as V  # noqa: E402
import reglas_comparacion as RCMP  # noqa: E402

SEMILLA = "U-PROMPT-R2:P4:2026-10-04"
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
FUERA = ("ayccef", "expaef", "opefci", "adrei")
E0_LEG = REX / "e0_chunking" / "salida_tanda0"
E0_R2 = REX / "e0_chunking" / "salida_tanda0_r2"
SUJETO = ("aplica_a", "ejecuta")
NORMATIVOS = ("Obligacion", "Restriccion", "Potestad", "Excepcion")


def chunks(d: Path, to: str) -> dict:
    return {c["id"]: c for c in json.loads((d / f"chunks_{to}.json").read_text(encoding="utf-8"))}


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


def contadores(val: dict, chunk: dict, pol) -> dict:
    """Los tres contadores del FRENO P4 sobre una validación de validador_r2."""
    c = Counter()
    if not val:
        return dict(c)
    for k, v in (val.get("adaptacion_v3") or {}).items():
        if k in ("sujeto_propuesto_como_mencion", "omision_v3_leida"):
            c[f"retirado:{k}"] += v
    cont = val.get("contadores") or {}
    for campo in ("tipo_entidad", "predicado"):
        for trat, n in (cont.get(campo) or {}).items():
            if trat not in ("en_lista",) and "rechaz" not in trat:
                c[f"retirado:{campo}:{trat}"] += n
    texto = V.texto_completo(chunk)
    for e in val.get("entidades") or []:
        if e.get("campos_heredados_v3"):
            c["retirado:claves_heredadas_v3"] += len(e["campos_heredados_v3"])
        c["fuera_de_lista"] += len(e.get("fuera_de_lista") or [])
        if e["type"] != "TextoOrdenado":
            c[f"tramo_entidad:{(e.get('provenance') or {}).get('tramo_verificado') or 'sin_tramo'}"] += 1
        for t in e.get("umbrales_tramos") or []:
            c[f"tramo_umbral:{V.verificar_tramo(t, texto, pol.holgura)[0]}"] += 1
    for r in val.get("relaciones") or []:
        if r.get("predicate") in SUJETO:
            c[f"mencion:{r.get('mencion_verificada') or 'sin_marca'}"] += 1
    for o in val.get("omisiones") or []:
        c[f"omision_tramo:{o.get('tramo_verificado')}"] += 1
        c[f"omision_categoria:{o.get('categoria') or 'sin_categoria'}"] += 1
    return dict(c)


def hechos(val: dict, chunk: dict, pol) -> dict:
    """Los hechos mecánicos de las dimensiones de la ficha (P4.b del mandato)."""
    if not val:
        return {"sin_validacion": True}
    ents = {e["local_id"]: e for e in val.get("entidades") or []}
    lab = {k: f"{e['type']}:{corto(e['label'], 60)}" for k, e in ents.items()}
    texto = V.texto_completo(chunk)
    rels = val.get("relaciones") or []
    return {
        "cuantias_en_el_texto": len(RCMP.detectar_cuantias(chunk.get("texto") or "")),
        "umbrales": [{"entidad": lab[k], "tramo": corto(t, 120),
                      "verificacion": V.verificar_tramo(t, texto, pol.holgura)[0]}
                     for k, e in ents.items() for t in e.get("umbrales_tramos") or []],
        "menciones": [{"pred": r["predicate"], "mencion": corto(r.get("sujeto_mencion"), 80),
                       "verificada": r.get("mencion_verificada"), "sujeto_id": r.get("sujeto_id_resuelto")
                       or r.get("sujeto_id")} for r in rels if r.get("predicate") in SUJETO],
        "omisiones": [{"categoria": o.get("categoria"), "tramo": corto(o.get("tramo"), 100),
                       "verificacion": o.get("tramo_verificado"), "nota": corto(o.get("nota"), 100)}
                      for o in val.get("omisiones") or []],
        "condicion_de": [{"de": lab.get(r.get("source"), r.get("source")), "a": lab.get(r.get("target"), r.get("target")),
                          "firma_nueva": r.get("tipo_target") in ("Operacion", "Potestad")}
                         for r in rels if r.get("predicate") == "condicion_de"],
        "limita": [{"de": lab.get(r.get("source"), r.get("source")), "a": lab.get(r.get("target"), r.get("target"))}
                   for r in rels if r.get("predicate") == "limita"],
    }


def resumen_salida(val: dict) -> dict:
    if not val:
        return {}
    ents = {e["local_id"]: e for e in val.get("entidades") or []}
    lab = {k: f"{e['type']}:{corto(e['label'], 60)}" for k, e in ents.items()}
    return {"entidades": [{"tipo": e["type"], "label": corto(e["label"], 80),
                           "descripcion": corto((e.get("properties") or {}).get("descripcion"), 240),
                           "tramo": corto((e.get("provenance") or {}).get("tramo"), 160),
                           "tramo_verificado": (e.get("provenance") or {}).get("tramo_verificado"),
                           "no_definidas": e.get("properties_no_definidas") or None}
                          for e in ents.values() if e["type"] != "TextoOrdenado"],
            "relaciones": [f"{lab.get(r.get('source'), r.get('source') or '[sujeto]')} --{r['predicate']}--> "
                           f"{lab.get(r.get('target'), r.get('sujeto_id_resuelto') or r.get('sujeto_mencion') or r.get('target'))}"
                           for r in val.get("relaciones") or []],
            "rechazos": [f"{x['motivo']}: {corto(x.get('detalle'), 80)}" for x in val.get("rechazos") or []]}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--muestra", type=Path, required=True)
    ap.add_argument("--e0-fuera", type=Path, required=True)
    ap.add_argument("--resultados", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    sal = a.salida.resolve()
    if REPO in sal.parents or sal == REPO:
        raise SystemExit("--salida no puede estar dentro del repo")
    sal.mkdir(parents=True, exist_ok=True)
    m = json.loads(a.muestra.read_text(encoding="utf-8"))
    res = jl(a.resultados)
    nuevo, sellado = perfil_e1.perfil("r2b"), perfil_e1.perfil("v3_b54")
    val_s, pol = RC.validador_perfil_r2(sellado)
    val_n, _ = RC.validador_perfil_r2(nuevo)
    leg, r2 = {}, {}
    for to in TOS:
        leg.update(chunks(E0_LEG, to))
        r2.update(chunks(E0_R2, to))
    for to in FUERA:
        leg.update(chunks(a.e0_fuera / "e0_legada", to))
        r2.update(chunks(a.e0_fuera / "e0_r2", to))

    grupo = {c: f"sorteo:{e}" for e in m["sorteo"] for c in m["sorteo"][e]["elegidos"]}
    grupo |= {c: "fijo" for c in m["fijos"]} | {c: "f1" for c in m["f1"]} | {c: "pata_e3" for c in m["pata_e3"][:3]}
    grupo |= {c: "lista" for v in m["listas_excepciones"].values() for c in v["tomados"]}
    grupo |= {c: "fuera" for v in m["fuera_de_muestra"].values() for c in v}
    filas, cont_por_brazo = {}, {"sellado": Counter(), "nuevo": Counter()}
    for cid in sorted(grupo):
        rs, rn = res.get(f"{cid}|sellado"), res.get(f"{cid}|nuevo")
        if rs is None or rn is None:
            filas[cid] = {"falta_brazo": [b for b, r in (("sellado", rs), ("nuevo", rn)) if r is None]}
            continue
        vs = val_s(rs["tool_input"], leg[cid]) if rs.get("tool_input") is not None else None
        vistos = RC.vistos_por_e3(rn.get("validacion_e1"))
        vn = val_n(rn["tool_input"], r2[cid], vistos_e3=vistos) if rn.get("tool_input") is not None and vistos else None
        cs, cn = contadores(vs, leg[cid], pol), contadores(vn, r2[cid], pol)
        cont_por_brazo["sellado"].update(cs)
        cont_por_brazo["nuevo"].update(cn)
        filas[cid] = {"grupo": grupo[cid], "error": {"sellado": rs.get("error"), "nuevo": rn.get("error")},
                      "usage": {"sellado": rs.get("usage"), "nuevo": rn.get("usage")},
                      "contadores": {"sellado": cs, "nuevo": cn},
                      "hechos": {"sellado": hechos(vs, leg[cid], pol), "nuevo": hechos(vn, r2[cid], pol)},
                      "salida": {"sellado": resumen_salida(vs), "nuevo": resumen_salida(vn)},
                      "es_item": PR.es_item(r2[cid]), "mini_a_mitad": PR.mini_a_mitad(r2[cid]),
                      "chars_propio": len(r2[cid].get("texto") or ""),
                      "no_definidas_p3b": [e.get("properties_no_definidas") for e in (vn or {}).get("entidades") or []
                                           if any(k in (e.get("properties_no_definidas") or {})
                                                  for k in ("modalidad", "consecuencia", "modalidad_clasificada"))],
                      "condicion_item_sin_condicion_de": [
                          corto(e["label"], 80) for e in (vn or {}).get("entidades") or []
                          if e["type"] == "Condicion" and PR.es_item(r2[cid])
                          and not any(r.get("source") == e["local_id"] and r.get("predicate") == "condicion_de"
                                      for r in (vn or {}).get("relaciones") or [])],
                      "orden_de_lectura": ((vn or {}).get("contadores") or {}).get("tramo_entidad", {})}
    # ---- fichas cegadas ----
    ids = sorted(c for c in filas if "falta_brazo" not in filas[c])
    orden = list(ids)
    random.Random(f"{SEMILLA}:fichas").shuffle(orden)
    md = ["# Fichas pareadas de P4 (cegadas: sin grupo, estrato ni origen)", "",
          f"Orden: random.Random('{SEMILLA}:fichas').shuffle sobre los {len(ids)} ids ordenados. SELLADO = prefijo v3_b54 "
          "con la E0 legada; NUEVO = prefijo r2b `3817de475c93` con la e0-r2 (release contra release).", ""]
    for n, cid in enumerate(orden, 1):
        f = filas[cid]
        c = r2[cid]
        md += [f"## Ficha {n} — `{cid}`", "", "**Texto propio:**", "", "```", (c.get("texto") or "").strip()[:3000], "```",
               f"**Último bloque heredado:** {corto((c.get('herencia') or [{}])[-1].get('texto'), 300)}", ""]
        for b in ("sellado", "nuevo"):
            s = f["salida"][b]
            md += [f"**{b.upper()}** — error: {f['error'][b]}", ""]
            md += [f"- {e['tipo']} «{e['label']}»: {e['descripcion']}" + (f" ‖ tramo ({e['tramo_verificado']}): «{e['tramo']}»"
                   if e.get("tramo") else "") + (f" ‖ no definidas: {json.dumps(e['no_definidas'], ensure_ascii=False)}"
                                                 if e.get("no_definidas") else "")
                   for e in s.get("entidades", [])]
            md += [f"  - {r}" for r in s.get("relaciones", [])]
            md += [f"  - rechazo: {r}" for r in s.get("rechazos", [])]
            h = f["hechos"][b]
            md += [f"- hechos: umbrales {json.dumps(h.get('umbrales'), ensure_ascii=False)}; menciones "
                   f"{json.dumps(h.get('menciones'), ensure_ascii=False)}; omisiones {json.dumps(h.get('omisiones'), ensure_ascii=False)}; "
                   f"condicion_de {json.dumps(h.get('condicion_de'), ensure_ascii=False)}; limita "
                   f"{json.dumps(h.get('limita'), ensure_ascii=False)}", ""]
        md += [f"*Cuantías en el texto propio: {f['hechos']['nuevo'].get('cuantias_en_el_texto')}.*", ""]
    (sal / "fichas_p4.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    # ---- e: tokens de salida por carácter de texto propio (3.000 caracteres o más) ----
    def ratio(b, cid):
        u = filas[cid]["usage"][b]
        n = len((leg if b == "sellado" else r2)[cid].get("texto") or "")
        return u["output_tokens"] / n if u and n else None
    grandes = [cid for cid in ids if filas[cid]["chars_propio"] >= 3000]
    e_med = {b: [ratio(b, c) for c in grandes if ratio(b, c) is not None] for b in ("sellado", "nuevo")}
    out = {"comando": "data/experiment/prompt_r2/p4/analisis_p4.py --muestra M --e0-fuera DIR --resultados R --salida DIR",
           "orden_fichas": orden, "contadores_por_brazo": {b: dict(sorted(v.items())) for b, v in cont_por_brazo.items()},
           "medicion_e": {"unidades_3000_o_mas": grandes,
                          "mediana": {b: (round(st.median(v), 3) if v else None) for b, v in e_med.items()},
                          "por_unidad": {c: {b: (round(ratio(b, c), 3) if ratio(b, c) else None) for b in ("sellado", "nuevo")}
                                         for c in grandes}},
           "filas": filas}
    (sal / "analisis_p4.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"fichas": len(orden), "contadores_por_brazo": out["contadores_por_brazo"],
                      "medicion_e": out["medicion_e"]["mediana"]}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
