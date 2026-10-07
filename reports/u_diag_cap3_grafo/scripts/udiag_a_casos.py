"""Tarea a.1: las Excepcion sin `exceptua`/`exceptua_obligacion` saliente y las Condicion sin `condicion_de`
saliente de a9631a64 (y de e22fae1a), con su causa determinística desde el crudo aceptado y la validación
guardada, y las fichas de lectura de los casos que el código no decide.

Uso: PYTHONDONTWRITEBYTECODE=1 <venv>/bin/python -B udiag_a_casos.py
Escribe salida/casos_a.json y salida/fichas_lectura_a.md (no lee lectura_a.json).
"""
import collections
import json
import os
import re

from udiag_comun import (AQUI, TOS, CONTENIDO, cargar_kg, cargar_chunks, cargar_salida, chunk_base, crudo_aceptado,
                         vistos_e3, tipo_unidad, bloque_lista, gid_de, norm, sha, SRC)

OUT = os.path.join(AQUI, "salida")
os.makedirs(OUT, exist_ok=True)
VINC = {"Excepcion": {"exceptua", "exceptua_obligacion"}, "Condicion": {"condicion_de"}}
ADMISIBLE = {"Excepcion": {"Restriccion", "Obligacion"},
             "Condicion": {"Obligacion", "Restriccion", "Operacion", "Potestad", "Excepcion"}}
NO_VINCULO = {"establecida_en", "aplica_a", "ejecuta"}   # predicados del nodo que no lo unen a una regla
PAT = re.compile(r"^relations\[(\d+)\]: (\w+) --(\w+)--> (\w+)$")
PAT_COLG = re.compile(r"^relations\[(\d+)\] \((\w+)\): source='([^']*)' target='([^']*)'$")


def cargar_todo():
    chunks = cargar_chunks()
    sal = {to: cargar_salida(to) for to in TOS}
    origen = collections.defaultdict(list)       # gid -> [(cid, local_id, to)]
    ents = collections.defaultdict(list)         # cid -> entidades validadas con su gid
    regs = {}
    for to in TOS:
        for r in sal[to]["fin_r2"]:
            regs[r["chunk_id"]] = r
            v = r.get("validacion")
            if not v:
                continue
            for e in v["entidades"]:
                g = gid_de(e, {**e["provenance"], "chunk_id": r["chunk_id"]})
                origen[g].append((r["chunk_id"], e["local_id"], to))
                ents[r["chunk_id"]].append({**e, "gid": g})
    return chunks, sal, origen, ents, regs


def rechazos_por_indice(val):
    out = {}
    for x in val.get("rechazos") or []:
        d = x.get("detalle", "")
        m = PAT.match(d) or PAT_COLG.match(d)
        if m:
            out[int(m.group(1))] = x
    return out


def otros_intentos(cid, to, sal, accepted):
    """Crudos de los intentos que no entran a E2: el intento 0 si se aceptó un reintento; los reintentos
    guardados que no son el aceptado."""
    out = []
    fin = sal["finales"].get(cid) or {}
    if accepted != "e1":
        ti = (sal["e1"].get(cid) or {}).get("tool_input_crudo")
        if ti:
            out.append(("e1", ti))
    for (c, k), r in sal["reint"].items():
        if c == cid and f"reintento_{k}" != accepted and r.get("tool_input"):
            out.append((f"reintento_{k}", r["tool_input"]))
    return out


def emitio_en(ti, ent, tipo):
    """¿El crudo `ti` trae una entidad del mismo tipo y label (o descripción) con una relación de vínculo?"""
    if not isinstance(ti, dict):
        return False
    es = [e for e in ti.get("entities") or [] if isinstance(e, dict) and e.get("type") == tipo]
    lab, desc = norm(ent.get("label")), norm((ent.get("properties") or {}).get("descripcion"))
    lids = {e.get("local_id") for e in es
            if norm(e.get("label")) == lab or (desc and norm((e.get("properties") or {}).get("descripcion")) == desc)}
    rels = ti.get("relations") or []
    return any(isinstance(r, dict) and r.get("source") in lids and r.get("predicate") not in NO_VINCULO
               for r in rels)


def causa_det(n, kg_sal, chunks, sal, origen, ents, regs):
    """Causa determinística de un nodo. Lee su origen principal (la primera entrada, la del orden de E0) y
    todas las demás: basta que una haya emitido para contarla como emitida."""
    t = n["type"]
    filas = []
    for cid, lid, to in origen[n["id"]]:
        s = sal[to]
        crudo, cual = crudo_aceptado(cid, s)
        rels = (crudo or {}).get("relations") or []
        if isinstance(rels, str):
            rels = []
        rech = rechazos_por_indice(regs[cid]["validacion"])
        vis = vistos_e3(cid, s)
        emit = []
        for i, r in enumerate(rels):
            if not isinstance(r, dict) or r.get("source") != lid or r.get("predicate") in NO_VINCULO:
                continue
            x = rech.get(i)
            if x is not None:
                m = PAT.match(x.get("detalle", ""))
                firma = f"{m.group(2)} --{m.group(3)}--> {m.group(4)}" if m else None
                emit.append({"indice": i, "predicado": r.get("predicate"), "target_local": r.get("target"),
                             "rechazo": x["motivo"], "firma": firma,
                             "visto_por_e3": bool(vis) and i in vis["relaciones"]})
            else:
                emit.append({"indice": i, "predicado": r.get("predicate"), "target_local": r.get("target"),
                             "rechazo": None, "firma": None, "visto_por_e3": bool(vis) and i in vis["relaciones"]})
        c0 = chunk_base(cid, chunks)
        propias = [e for e in ents[cid] if e["gid"] != n["id"]]
        admis = [e for e in propias if e["type"] in ADMISIBLE[t]]
        ops = [e for e in propias if e["type"] == "Operacion"]
        ent = next(e for e in ents[cid] if e["local_id"] == lid)
        otro = [k for k, ti in otros_intentos(cid, to, s, cual) if emitio_en(ti, ent, t)]
        filas.append({"chunk_id": cid, "local_id": lid, "to": to, "crudo": cual, "tipo_unidad": tipo_unidad(c0),
                      "emitidas": emit, "admisibles_en_la_unidad": len(admis), "operaciones_en_la_unidad": len(ops),
                      "emitida_en_otro_intento": otro, "en_cola": cid in s["cola"]})
    f0 = filas[0]
    emitidas = [x for f in filas for x in f["emitidas"]]
    if emitidas:
        if any(x["rechazo"] is None for x in emitidas):
            clase = "EMIT-SIN-RECHAZO"
        elif t == "Excepcion" and any(x["firma"] and x["firma"].endswith("--> Operacion")
                                      and x["predicado"] in VINC[t] for x in emitidas):
            clase = "II-OP-RECHAZADA"
        elif any(x["rechazo"] == "firma_invalida" for x in emitidas):
            clase = "III-FIRMA"
        elif all(x["rechazo"] == "ref_colgante" for x in emitidas):
            clase = "III-COLGANTE"
        else:
            clase = "III-OTRO"
    else:
        if any(f["admisibles_en_la_unidad"] for f in filas) or (t == "Excepcion" and any(
                f["operaciones_en_la_unidad"] for f in filas)):
            clase = "LEER"
        else:
            clase = "I-SIN-NORMA-EN-LA-UNIDAD"
    return {"id": n["id"], "type": t, "label": n["label"], "clase_det": clase, "origenes": filas,
            "to": f0["to"], "chunk_id": f0["chunk_id"], "tipo_unidad": f0["tipo_unidad"],
            "emitida_en_otro_intento": sorted({k for f in filas for k in f["emitida_en_otro_intento"]}),
            "firmas_rechazadas": sorted({x["firma"] or x["rechazo"] for x in emitidas})}


def ficha_unidad(cid, casos, por_id, chunks, ents, sal):
    """Texto de lectura de una unidad con sus casos: la unidad, su herencia, lo que extrajo y los nodos a leer."""
    to = casos[0]["to"]
    c = chunk_base(cid, chunks)
    i = bloque_lista(c)
    lin = [f"## Unidad `{cid}` ({casos[0]['tipo_unidad']})",
           "- herencia: " + " | ".join(
               ("**[abre la lista]** " if k == i else "") + f"[{h['tipo']} {h['unidad_origen']}] {h['texto'][:500]}"
               for k, h in enumerate(c["herencia"]) if h["tipo"] != "encabezado" or k == i or k == len(c["herencia"]) - 1),
           f"- texto propio: {c['texto'][:1800]}", "- entidades de la unidad:"]
    for e in ents[cid]:
        if e["type"] == "TextoOrdenado":
            continue
        d = (e.get("properties") or {}).get("descripcion") or ""
        lin.append(f"  - `{e['local_id']}` {e['type']}: {e['label']} — {d[:200]}")
    crudo, _ = crudo_aceptado(cid, sal[to])
    rels = [r for r in (crudo or {}).get("relations") or [] if isinstance(r, dict)
            and r.get("predicate") not in ("establecida_en", "aplica_a", "ejecuta")]
    lin.append("- relaciones del crudo (sin establecida_en ni de sujeto): " + ("; ".join(
        f"{r.get('source')} {r.get('predicate')} {r.get('target')}" for r in rels) or "ninguna"))
    lin.append("- NODOS A CLASIFICAR:")
    for caso in casos:
        n = por_id[caso["id"]]
        lid = caso["origenes"][0]["local_id"]
        lin.append(f"  - **caso {caso['n']}** {caso['type']} `{lid}`: {n['label']} | descripcion: "
                   f"{(n['properties'] or {}).get('descripcion')} | tramo: {n['provenance'].get('tramo')}")
    return "\n".join(lin)


def main():
    chunks, sal, origen, ents, regs = cargar_todo()
    resultado = {}
    for nombre in ("diez", "sincola"):
        kg = cargar_kg(nombre)
        salen = collections.defaultdict(list)
        for e in kg["edges"]:
            salen[e["source"]].append(e)
        casos = []
        for t in ("Excepcion", "Condicion"):
            for n in sorted((x for x in kg["nodes"] if x["type"] == t), key=lambda x: x["id"]):
                if any(e["relation"] in VINC[t] for e in salen[n["id"]]):
                    continue
                casos.append(causa_det(n, salen, chunks, sal, origen, ents, regs))
        resultado[nombre] = casos
    # el sin cola es un subconjunto: los casos de sincola deben ser los de diez sin la cola
    ids_d = {c["id"] for c in resultado["diez"]}
    ids_s = {c["id"] for c in resultado["sincola"]}
    assert ids_s <= ids_d, "un caso del sin cola no está en el diez"
    kg = cargar_kg("diez")
    por_id = {n["id"]: n for n in kg["nodes"]}
    leer = [c for c in resultado["diez"] if c["clase_det"] == "LEER"]
    for k, c in enumerate(leer, 1):
        c["n"] = k
    fichas = ["# Fichas de lectura de la tarea a (U-DIAG-CAP3-GRAFO)", "",
              f"{len(leer)} casos, en el orden de `casos_a.json` (tipo, id). Criterio: `criterio_lectura_a.md`.", ""]
    por_unidad = collections.defaultdict(list)
    for c in leer:
        por_unidad[c["chunk_id"]].append(c)
    for cid in sorted(por_unidad, key=lambda x: min(c["n"] for c in por_unidad[x])):
        fichas.append(ficha_unidad(cid, por_unidad[cid], por_id, chunks, ents, sal))
        fichas.append("")
    open(os.path.join(OUT, "fichas_lectura_a.md"), "w", encoding="utf-8").write("\n".join(fichas))
    json.dump({"kg_sha256": {"diez": sha(os.path.join(SRC, "ens_diez", "kg.json")),
                             "sincola": sha(os.path.join(SRC, "ens_sincola", "kg.json"))},
               "diez": resultado["diez"], "ids_sincola": sorted(ids_s)},
              open(os.path.join(OUT, "casos_a.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for nombre, casos in resultado.items():
        print(nombre, {t: collections.Counter(c["clase_det"] for c in casos if c["type"] == t)
                       for t in ("Excepcion", "Condicion")})
    print("a leer:", len(leer), collections.Counter(c["type"] for c in leer))
    print("emitida en otro intento:", collections.Counter((c["type"], c["clase_det"]) for c in resultado["diez"]
                                                          if c["emitida_en_otro_intento"]))


if __name__ == "__main__":
    main()
