"""
03_fichas.py — U-TRIP-V, paso f: las 120 fichas (las 100 en el orden de lectura sellado y las 20 del pool), DESPUÉS del
sello del sorteo. Sin ninguna salida de un modelo que juzgue (§3.3 y §6.2): ni propuesta, ni veredicto, ni estrato, ni
solapamiento.

Por arista (§3.3):
  - el nodo de origen y el de destino: id, tipo, etiqueta, descripción y propiedades, sin las marcas del pipeline
    (comun_v: PROPS_NODO_FUERA, NO_DEFINIDAS_FUERA, CAMPOS_NODO_FUERA; en `umbrales`, solo UMBRAL_CAMPOS);
  - el predicado y, si la arista los tiene, su calificador y sus propiedades no definidas; en aplica_a y ejecuta, el
    tramo del sujeto (la mención del texto que la arista toma como sujeto) con su condición de literal;
  - la evidencia de cada procedencia: el texto propio y el heredado de la unidad (E0 r2b de desarrollo; una parte de una
    partición por corte usa el chunk de su unidad), los avisos de E0 que valen true (tabla, fórmula), el tramo literal
    de cada extremo en esa unidad si lo hay (con su condición de literal: exacta, tokens o no), las páginas y la ruta del
    PDF con la página.
Controles: el sha256 del acta es el de su sello; la hora de las fichas es posterior a la del sello; las 100 y el pool
se recomputan desde el acta.

Escribe --salida/fichas_V.jsonl, --salida/fichas_<lote>.md (piloto, lote_01…lote_09, pool) y
--salida/fichas_V_cabecera.json.
  python3 -I -B 03_fichas.py --copia <copia> --acta <acta_sorteo_V.json> --sello <sello_sorteo_V.txt> --salida <dir>
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun_v as V  # noqa: E402


def norm(s) -> str:
    return re.sub(r"\s+", " ", s or "").strip()


def vista_nodo(n: dict) -> dict:
    props = {}
    for k, v in (n.get("properties") or {}).items():
        if k == "descripcion" or k in V.PROPS_NODO_FUERA:
            continue
        if k == "umbrales" and isinstance(v, list):
            v = [{c: u[c] for c in V.UMBRAL_CAMPOS if c in u} for u in v]
        props[k] = v
    nd = {k: v for k, v in (n.get("properties_no_definidas") or {}).items() if k not in V.NO_DEFINIDAS_FUERA}
    out = {"id": n["id"], "tipo": n["type"], "etiqueta": n["label"],
           "descripcion": (n.get("properties") or {}).get("descripcion"), "propiedades": props}
    if nd:
        out["propiedades_no_definidas_en_el_esquema"] = nd
    return out


def tramos_en(n: dict, cid: str) -> list[dict]:
    out = []
    for p in n["provenances"]:
        if p.get("chunk_id") == cid and p.get("tramo"):
            t = {"texto": p["tramo"], "literal": p.get("tramo_verificado")}
            if t not in out:
                out.append(t)
    return out


def fmt_valor(v) -> str:
    return v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)


def md_nodo(rot: str, n: dict) -> list[str]:
    l = [f"**{rot}** — {n['tipo']} «{n['etiqueta']}» (`{n['id']}`)", ""]
    l.append(f"- descripción: {norm(n['descripcion'])}" if n["descripcion"] else "- descripción: —")
    for k, v in n["propiedades"].items():
        if k == "umbrales" and isinstance(v, list):
            l.append(f"- umbrales ({len(v)}):")
            l += [f"  - " + "; ".join(f"{c}: {fmt_valor(u[c])}" for c in u) for u in v]
        else:
            l.append(f"- {k}: {fmt_valor(v)}")
    for k, v in (n.get("propiedades_no_definidas_en_el_esquema") or {}).items():
        l.append(f"- {k} (no definida en el esquema): {fmt_valor(v)}")
    return l + [""]


def md_ficha(f: dict) -> list[str]:
    l = [f"## {f['ref']} · `{f['predicado']}`" + (f" · {f['lote']}, {f['posicion']} de 10" if f["lote"] != "pool"
                                                     else f" · pool, {f['posicion']} de 20"), ""]
    l += md_nodo("Origen", f["origen"])
    l += [f"**Predicado** — `{f['predicado']}`", ""]
    ar = f["arista"]
    if ar:
        if "calificador" in ar:
            l.append(f"- calificador de la arista: «{ar['calificador']}»")
        for k, v in (ar.get("propiedades_no_definidas_en_el_esquema") or {}).items():
            l.append(f"- {k} (de la arista, no definida en el esquema): {fmt_valor(v)}")
        if "tramo_del_sujeto" in ar:
            t = ar["tramo_del_sujeto"]
            l.append(f"- tramo del sujeto: «{t['texto']}» (literal: {t['literal']})")
        l.append("")
    l += md_nodo("Destino", f["destino"])
    for i, ev in enumerate(f["evidencia"], 1):
        pags = ", ".join(map(str, ev["paginas"]))
        l += [f"**Evidencia {i} de {len(f['evidencia'])}** — `{ev['chunk_id']}` · {ev['to']} · punto {ev['punto']} · "
              f"{ev['rol_documental']} · págs. {pags}"
              + (f" · parte de la unidad `{ev['unidad_e0']}`" if ev["parte_de_particion"] else ""), ""]
        l.append(f"- PDF: " + " · ".join(f"`{x}`" for x in ev["pdf"]["con_pagina"]))
        if ev.get("avisos_e0"):
            l.append(f"- avisos de E0: {json.dumps(ev['avisos_e0'], ensure_ascii=False)}")
        l.append("")
        for h in ev["heredado"]:
            hp = ", ".join(map(str, h.get("paginas") or []))
            l.append(f"> *heredado ({h['tipo']}, {h['unidad_origen']}{', p. ' + hp if hp else ''}):* {norm(h['texto'])}")
            l.append(">")
        l += [f"> *propio:* {norm(ev['texto_propio'])}", ""]
        for rot, clave_t in (("origen", "tramos_origen"), ("destino", "tramos_destino")):
            if ev[clave_t]:
                for t in ev[clave_t]:
                    l.append(f"- tramo del {rot}: «{norm(t['texto'])}» (literal: {t['literal']})")
            else:
                l.append(f"- tramo del {rot}: —")
        l.append("")
    return l + ["---", ""]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--copia", type=Path, required=True)
    ap.add_argument("--acta", type=Path, required=True)
    ap.add_argument("--sello", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()

    s_acta = V.sha_archivo(a.acta)
    sello = a.sello.read_text(encoding="utf-8").split()
    if sello[0] != s_acta:
        raise SystemExit(f"el acta da {s_acta}, el sello dice {sello[0]}")
    hora_sello = sello[2]
    hora_f = V.hora()
    if datetime.fromisoformat(hora_f) <= datetime.fromisoformat(hora_sello):
        raise SystemExit(f"hora de las fichas {hora_f} no posterior al sello {hora_sello}")
    acta = json.loads(a.acta.read_text(encoding="utf-8"))
    so = acta["sorteo"]
    orden, lotes = so["orden"], so["lotes"]
    pool = [x["clave"] for x in so["pool"]]
    if V.sha(V.canon(orden)) != so["sha256_orden"] or V.sha(V.canon(pool)) != so["sha256_pool"]:
        raise SystemExit("el orden o el pool no dan su sha256 sellado")

    kg, s_kg = V.cargar_kg(a.copia)
    if s_kg != acta["grafo"]["sha256"]:
        raise SystemExit("el grafo no es el del acta")
    nodos = {n["id"]: n for n in kg["nodes"]}
    aristas = {V.clave(e): e for e in kg["edges"] if e["relation"] in V.CONTENIDO}
    e0 = {to: V.chunks_e0(a.copia, to) for to in V.TOS_V}

    lote_de = {k: (lote, i) for lote, ks in lotes.items() for i, k in enumerate(ks, 1)}
    lote_de |= {k: ("pool", i) for i, k in enumerate(pool, 1)}
    refs = {k: f"V{i + 1:03d}" for i, k in enumerate(orden)} | {k: f"P{i + 1:02d}" for i, k in enumerate(pool)}

    fichas = []
    for k in orden + pool:
        e = aristas[k]
        o, d = nodos[e["source"]], nodos[e["target"]]
        ar = {}
        if e.get("calificador"):
            ar["calificador"] = e["calificador"]
        if e.get("properties_no_definidas"):
            ar["propiedades_no_definidas_en_el_esquema"] = e["properties_no_definidas"]
        if e["relation"] in V.PREDICADOS_SUJETO and e.get("sujeto_mencion"):
            ar["tramo_del_sujeto"] = {"texto": e["sujeto_mencion"], "literal": e.get("mencion_verificada")}
        evidencia = []
        for p in e["provenances"]:
            cid = p["chunk_id"]
            base = V.base_chunk(cid)
            c = e0[p["to"]][base]
            pdf = f"{V.PDF_DIR_REL}/{p['archivo']}"
            evidencia.append({
                "chunk_id": cid, "unidad_e0": base, "parte_de_particion": cid != base, "to": p["to"],
                "archivo": p["archivo"], "punto": p["punto"], "rol_documental": p["rol_documental"],
                "titulo_e0": c.get("titulo"), "paginas": p["paginas"],
                "texto_propio": c.get("texto") or "",
                "heredado": [{"tipo": h.get("tipo"), "unidad_origen": h.get("unidad_origen"), "texto": h.get("texto"),
                              "paginas": h.get("paginas")} for h in c.get("herencia") or []],
                "avisos_e0": {kk: vv for kk, vv in (c.get("flags") or {}).items() if vv},
                "tramos_origen": tramos_en(o, cid), "tramos_destino": tramos_en(d, cid),
                "pdf": {"ruta": pdf, "paginas": p["paginas"], "con_pagina": [f"{pdf}#page={pg}" for pg in p["paginas"]]}})
        lote, pos = lote_de[k]
        fichas.append({"ref": refs[k], "lote": lote, "posicion": pos, "clave": k, "predicado": e["relation"],
                       "origen": vista_nodo(o), "destino": vista_nodo(d), "arista": ar, "evidencia": evidencia})

    if len(fichas) != V.N_MUESTRA + V.N_POOL:
        raise SystemExit("no son 120 fichas")
    a.salida.mkdir(parents=True, exist_ok=True)
    (a.salida / "fichas_V.jsonl").write_text("\n".join(json.dumps(f, ensure_ascii=False) for f in fichas) + "\n",
                                             encoding="utf-8")
    shas_md = {}
    for lote in list(lotes) + ["pool"]:
        fs = [f for f in fichas if f["lote"] == lote]
        titulo = {"piloto": "del lote piloto (10)", "pool": "del pool de calibración (20)"}.get(
            lote, f"del {lote.replace('_', ' ')} (10)")
        md = [f"# U-TRIP-V: fichas {titulo}", "",
              f"Acta del sorteo `acta_sorteo_V.json` (sha256 `{s_acta}`), sellada a las {hora_sello}; fichas generadas a "
              f"las {hora_f}. Grafo {acta['grafo']['nombre']} (`{s_kg[:8]}…`). Las fichas van en el orden sellado. "
              "Criterio (§3.4 del pre-registro): la evidencia sostiene la relación entre esos dos nodos, con sus sujetos, "
              "valores, calificadores y modalidad.", "",
              "Cada ficha trae los dos nodos (tipo, etiqueta, descripción y propiedades), el predicado y la evidencia de "
              "cada procedencia: el texto heredado y el propio de la unidad de E0, el tramo literal de cada extremo en "
              "esa unidad si lo hay, las páginas y la ruta del PDF con la página. «literal» dice si el tramo está tal "
              "cual en el texto (exacta), por tokens (tokens) o no (no).", ""]
        for f in fs:
            md += md_ficha(f)
        p = a.salida / f"fichas_{lote}.md"
        p.write_text("\n".join(md) + "\n", encoding="utf-8")
        shas_md[p.name] = V.sha_archivo(p)
    cab = {"unidad": "U-TRIP-V, paso f: las 120 fichas (sin juicio)", "hora": hora_f, "hora_sello": hora_sello,
           "acta_sorteo_V.json_sha256": s_acta, "kg_sha256": s_kg, "fichas": len(fichas),
           "fichas_V.jsonl_sha256": V.sha_archivo(a.salida / "fichas_V.jsonl"), "md_sha256": shas_md,
           "campos_fuera": {"propiedades_del_nodo": list(V.PROPS_NODO_FUERA),
                            "propiedades_no_definidas": list(V.NO_DEFINIDAS_FUERA),
                            "campos_del_nodo": list(V.CAMPOS_NODO_FUERA), "en_cada_umbral": list(V.UMBRAL_FUERA),
                            "campos_de_la_arista": list(V.ARISTA_FUERA)},
           "03_fichas.py_sha256": V.sha_archivo(Path(__file__)), "comun_v.py_sha256": V.sha_archivo(
               Path(__file__).resolve().parent / "comun_v.py")}
    V.escribir_json(a.salida / "fichas_V_cabecera.json", cab)
    print(json.dumps({"hora": hora_f, "fichas": len(fichas), "jsonl": cab["fichas_V.jsonl_sha256"],
                      "md": {k: v[:16] for k, v in shas_md.items()},
                      "procedencias": sum(len(f["evidencia"]) for f in fichas),
                      "con_dos_procedencias": [f["ref"] for f in fichas if len(f["evidencia"]) > 1],
                      "partes": [f["ref"] for f in fichas if any(ev["parte_de_particion"] for ev in f["evidencia"])]},
                     ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
