"""Tarea a.2: la regla de unión ítem–encabezado (grupo E de U-OMISIONES-COD v2) y la firma
(Excepcion, exceptua, Operacion) (grupo F), medidas sobre lo guardado, sin re-extraer.

Regla E (propuesta; se aplicaría en el ensamblado, después del merge entre TOs y antes de las aristas derivadas):
  Para cada nodo X de tipo Excepcion sin `exceptua` ni `exceptua_obligacion` saliente, o de tipo Condicion sin
  `condicion_de` saliente, cuya procedencia principal es un ítem de lista (`prompt_r2b.es_item` sobre su chunk de
  E0), sea H la unidad del bloque que abre su lista (`bloque_lista`): el mini-chunk de E0 con la misma unidad de
  origen, el mismo rol y el mismo texto. Los candidatos son los nodos del grafo con alguna procedencia en H y un
  tipo que la matriz admite como destino de X:
    - Excepcion: Restriccion (`exceptua`) u Obligacion (`exceptua_obligacion`); con la firma F, también Operacion
      (`exceptua`);
    - Condicion: Excepcion, Obligacion, Restriccion, Operacion o Potestad (`condicion_de`).
  Con un candidato, la arista X → candidato, marcada `rol_fuente = union_item_encabezado` (derivada, no la vio E3);
  con más de uno, ambigua (no se une; queda en el registro); con ninguno, sin norma en el encabezado; si el bloque
  que abre la lista es la línea de título (no hay mini-chunk), sin unidad de encabezado.
  Variante «prioridad»: en la Condicion, si H tiene exactamente una Excepcion, se une a ella (P3C-b2: los ítems
  son las condiciones de una sola excepción, que el encabezado extrae unida a su norma).
  Variante «estricta»: solo si la unidad de X no extrajo ningún nodo de un tipo admisible (si lo extrajo, el
  destino puede estar en el ítem).

Uso: PYTHONDONTWRITEBYTECODE=1 <venv>/bin/python -B udiag_a_union.py
Escribe salida/union_e.json, salida/firma_f.json y salida/muestra_union_e.md (30 uniones, semilla 20261007).
"""
import collections
import json
import os
import random

from udiag_comun import AQUI, TOS, cargar_kg, cargar_chunks, cargar_salida, chunk_base, bloque_lista, es_mini_chunk, \
    norm, tipo_unidad, vistos_e3, gid_de

OUT = os.path.join(AQUI, "salida")
SEMILLA = 20261007
VINC = {"Excepcion": {"exceptua", "exceptua_obligacion"}, "Condicion": {"condicion_de"}}
DESTINO = {"Excepcion": {"Restriccion": "exceptua", "Obligacion": "exceptua_obligacion"},
           "Condicion": {t: "condicion_de" for t in ("Excepcion", "Obligacion", "Restriccion", "Operacion", "Potestad")}}
DESTINO_F = {"Operacion": "exceptua"}


def mini_de_bloque(c, chunks_por_unidad):
    i = bloque_lista(c)
    if i is None:
        return None, None
    h = c["herencia"][i]
    if h["tipo"] == "encabezado":
        return "linea_de_titulo", h
    cands = [m for m in chunks_por_unidad.get((c["to"], h["unidad_origen"], h["tipo"]), [])
             if norm(h["texto"]) in norm(m["texto"])]
    assert len(cands) == 1, (c["id"], len(cands))
    return cands[0]["id"], h


def medir(nombre, chunks, chunks_por_unidad, propias_por_chunk):
    kg = cargar_kg(nombre)
    por_id = {n["id"]: n for n in kg["nodes"]}
    salen = collections.defaultdict(list)
    for e in kg["edges"]:
        salen[e["source"]].append(e)
    por_chunk = collections.defaultdict(list)
    for n in kg["nodes"]:
        for p in n.get("provenances") or [n["provenance"]]:
            if p.get("chunk_id"):
                por_chunk[p["chunk_id"]].append(n["id"])
    filas = []
    for t in ("Excepcion", "Condicion"):
        for n in sorted((x for x in kg["nodes"] if x["type"] == t), key=lambda x: x["id"]):
            if any(e["relation"] in VINC[t] for e in salen[n["id"]]):
                continue
            cid = n["provenance"]["chunk_id"]
            c = chunk_base(cid, chunks)
            if es_mini_chunk(c) or bloque_lista(c) is None:
                continue
            h_id, h = mini_de_bloque(c, chunks_por_unidad)
            fila = {"id": n["id"], "type": t, "to": c["to"], "chunk_id": cid, "encabezado": h_id,
                    "bloque": f"[{h['tipo']} {h['unidad_origen']}] {h['texto']}"}
            propios_admisibles = [g for g in propias_por_chunk.get(cid, []) if g != n["id"]
                                  and por_id.get(g, {}).get("type") in DESTINO[t]]
            fila["unidad_con_admisible_propio"] = bool(propios_admisibles)
            if h_id == "linea_de_titulo":
                fila["resultado"] = "sin_unidad_de_encabezado"
                filas.append(fila)
                continue
            cand = sorted({g for g in por_chunk.get(h_id, []) if por_id[g]["type"] in DESTINO[t]})
            cand_f = sorted({g for g in por_chunk.get(h_id, []) if t == "Excepcion"
                             and por_id[g]["type"] in DESTINO_F})
            fila["candidatos"] = [(g, por_id[g]["type"]) for g in cand]
            fila["candidatos_operacion_f"] = cand_f
            fila["resultado"] = ("union" if len(cand) == 1 else "ambigua" if cand else "sin_norma_en_el_encabezado")
            if t == "Excepcion":
                cf = cand + cand_f
                fila["resultado_con_f"] = ("union" if len(cf) == 1 else "ambigua" if cf else
                                           "sin_norma_en_el_encabezado")
            if t == "Condicion":
                exc = [g for g in cand if por_id[g]["type"] == "Excepcion"]
                fila["resultado_prioridad"] = ("union" if len(exc) == 1 or len(cand) == 1 else
                                               "ambigua" if cand else "sin_norma_en_el_encabezado")
            filas.append(fila)
    return kg, por_id, filas


def resumen(filas):
    out = {}
    for t in ("Excepcion", "Condicion"):
        fs = [f for f in filas if f["type"] == t]
        out[t] = {"items_sin_vinculo": len(fs),
                  "resultado": dict(collections.Counter(f["resultado"] for f in fs).most_common()),
                  "resultado_estricta": dict(collections.Counter(
                      f["resultado"] if not f["unidad_con_admisible_propio"] else "excluida_por_admisible_propio"
                      for f in fs).most_common()),
                  "por_to_union": dict(collections.Counter(f["to"] for f in fs if f["resultado"] == "union").most_common()),
                  "tipo_destino_union": dict(collections.Counter(f["candidatos"][0][1] for f in fs
                                                                 if f["resultado"] == "union").most_common()),
                  "candidatos_en_ambiguas": dict(collections.Counter(len(f["candidatos"]) for f in fs
                                                                     if f["resultado"] == "ambigua").most_common())}
        if t == "Excepcion":
            out[t]["resultado_con_f"] = dict(collections.Counter(f.get("resultado_con_f", f["resultado"])
                                                                 for f in fs).most_common())
        else:
            out[t]["resultado_prioridad"] = dict(collections.Counter(f.get("resultado_prioridad", f["resultado"])
                                                                     for f in fs).most_common())
    return out


def firma_f(chunks):
    """Los rechazos (Excepcion, exceptua, Operacion) y (Excepcion, exceptua_obligacion, Operacion): unidad, si E3
    vio la relación, en qué validador cayó y si la unidad está en la cola."""
    import re
    pat = re.compile(r"^relations\[(\d+)\]: (\w+) --(\w+)--> (\w+)$")
    filas = []
    for to in TOS:
        s = cargar_salida(to)
        for r in s["fin_r2"]:
            v = r.get("validacion")
            if not v:
                continue
            loc = {e["local_id"]: e for e in v["entidades"]}
            for x in v["rechazos"]:
                m = pat.match(x.get("detalle", ""))
                if not m or m.group(2) != "Excepcion" or m.group(4) != "Operacion":
                    continue
                i = int(m.group(1))
                vis = vistos_e3(r["chunk_id"], s)
                en_e1 = [y["motivo"] for y in vis["rechazos_e1"] if y.get("detalle", "").startswith(f"relations[{i}]")]
                el = x["elemento"]
                src, tgt = loc.get(el["source"]), loc.get(el["target"])
                filas.append({"chunk_id": r["chunk_id"], "to": to, "indice": i, "predicado": m.group(3),
                              "excepcion": gid_de(src, {**src["provenance"], "chunk_id": r["chunk_id"]}),
                              "operacion": gid_de(tgt, {**tgt["provenance"], "chunk_id": r["chunk_id"]}),
                              "estado_e3": r.get("estado_e3"), "crudo": r.get("origen_crudo"),
                              "visto_por_e3": i in vis["relaciones"], "rechazo_en_validador_e1": en_e1,
                              "en_cola": r["chunk_id"] in s["cola"],
                              "tipo_unidad": tipo_unidad(chunk_base(r["chunk_id"], chunks))})
    return filas


def main():
    chunks = cargar_chunks()
    chunks_por_unidad = collections.defaultdict(list)
    for c in chunks.values():
        if es_mini_chunk(c):
            chunks_por_unidad[(c["to"], c["unidad"], c["rol_bloque"])].append(c)
    propias = collections.defaultdict(list)
    for to in TOS:
        for r in cargar_salida(to)["fin_r2"]:
            for e in (r.get("validacion") or {}).get("entidades") or []:
                propias[r["chunk_id"]].append(gid_de(e, {**e["provenance"], "chunk_id": r["chunk_id"]}))
    out = {"semilla": SEMILLA}
    muestras = {}
    for nombre in ("diez", "sincola"):
        kg, por_id, filas = medir(nombre, chunks, chunks_por_unidad, propias)
        out[nombre] = {"resumen": resumen(filas), "filas": filas}
        if nombre == "diez":
            uniones = [f for f in filas if f["resultado"] == "union"]
            muestras = (random.Random(SEMILLA).sample(uniones, 30), por_id)
    json.dump(out, open(os.path.join(OUT, "union_e.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    ff = firma_f(chunks)
    json.dump({"filas": ff, "resumen": {
        "rechazos": len(ff), "por_predicado": dict(collections.Counter(f["predicado"] for f in ff)),
        "nodos_excepcion": len({f["excepcion"] for f in ff}), "unidades": len({f["chunk_id"] for f in ff}),
        "vistos_por_e3": sum(f["visto_por_e3"] for f in ff),
        "rechazados_ya_en_validador_e1": sum(bool(f["rechazo_en_validador_e1"]) for f in ff),
        "en_cola": sum(f["en_cola"] for f in ff),
        "por_to": dict(collections.Counter(f["to"] for f in ff).most_common()),
        "por_estado_e3": dict(collections.Counter(f["estado_e3"] for f in ff).most_common()),
        "por_tipo_unidad": dict(collections.Counter(f["tipo_unidad"] for f in ff).most_common()),
        "unidades_por_to": dict(collections.Counter(c.split("::")[0] for c in sorted({f["chunk_id"] for f in ff})).most_common())}},
        open(os.path.join(OUT, "firma_f.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    sample, por_id = muestras
    lin = ["# Muestra de 30 uniones propuestas por la regla E (semilla 20261007), para leer", ""]
    for k, f in enumerate(sample, 1):
        x, d = por_id[f["id"]], por_id[f["candidatos"][0][0]]
        c = chunk_base(f["chunk_id"], chunks)
        lin += [f"## U{k}. {x['type']} → {d['type']} (`{f['chunk_id']}` → `{f['encabezado']}`)",
                f"- bloque que abre la lista: {f['bloque']}",
                f"- texto del ítem: {c['texto'][:900]}",
                f"- nodo del ítem: {x['label']} | {(x['properties'] or {}).get('descripcion')} | tramo: "
                f"{x['provenance'].get('tramo')}",
                f"- destino propuesto: {d['label']} | {(d['properties'] or {}).get('descripcion')} | tramo: "
                f"{d['provenance'].get('tramo')}", ""]
    open(os.path.join(OUT, "muestra_union_e.md"), "w", encoding="utf-8").write("\n".join(lin))
    print(json.dumps({k: out[k]["resumen"] for k in ("diez", "sincola")}, ensure_ascii=False, indent=1))
    print(json.dumps(json.load(open(os.path.join(OUT, "firma_f.json")))["resumen"], ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
