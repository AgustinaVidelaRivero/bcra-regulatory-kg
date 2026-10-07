"""Tarea a: fichas de los controles de lectura (semilla 20261007, criterio_lectura_a.md):
  (1) 30 nodos sorteados entre los que el código asigna a (i) sin leer (I-SIN-NORMA-EN-LA-UNIDAD);
  (2) las 41 relaciones (Excepcion, exceptua, Operacion) rechazadas por firma;
  (3) 25 casos sorteados (semilla 20261008) de los 255 leídos, para la relectura de concordancia de esta sesión.
Uso: PYTHONDONTWRITEBYTECODE=1 <venv>/bin/python -B udiag_a_controles.py
Escribe salida/fichas_control_i.md, salida/fichas_control_f.md y salida/fichas_relectura_25.md.
"""
import json
import os
import random
import re

from udiag_comun import AQUI, TOS, cargar_kg, cargar_chunks, cargar_salida, chunk_base, bloque_lista, gid_de
import udiag_a_casos as A

OUT = os.path.join(AQUI, "salida")


def main():
    chunks, sal, origen, ents, regs = A.cargar_todo()
    kg = cargar_kg("diez")
    por_id = {n["id"]: n for n in kg["nodes"]}
    casos = json.load(open(os.path.join(OUT, "casos_a.json"), encoding="utf-8"))["diez"]
    # (1)
    sin = [c for c in casos if c["clase_det"] == "I-SIN-NORMA-EN-LA-UNIDAD"]
    m1 = random.Random(20261007).sample(sin, 30)
    lin = ["# Control (1): 30 nodos que el código asigna a la causa (i) sin leer (semilla 20261007)", ""]
    for k, c in enumerate(m1, 1):
        c = dict(c, n=f"C{k}")
        lin.append(A.ficha_unidad(c["chunk_id"], [c], por_id, chunks, ents, sal))
        lin.append("")
    open(os.path.join(OUT, "fichas_control_i.md"), "w", encoding="utf-8").write("\n".join(lin))
    json.dump([{"control": f"C{k}", "id": c["id"]} for k, c in enumerate(m1, 1)],
              open(os.path.join(OUT, "muestra_control_i.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    # (2)
    pat = re.compile(r"^relations\[(\d+)\]: Excepcion --exceptua--> Operacion$")
    lin = ["# Control (2): las 41 relaciones (Excepcion, exceptua, Operacion) rechazadas por firma", ""]
    filas = []
    for to in TOS:
        for r in sal[to]["fin_r2"]:
            v = r.get("validacion")
            if not v:
                continue
            loc = {e["local_id"]: e for e in v["entidades"]}
            for x in v["rechazos"]:
                if not pat.match(x.get("detalle", "")):
                    continue
                filas.append((r["chunk_id"], x["elemento"], loc))
    for k, (cid, el, loc) in enumerate(filas, 1):
        ex, op = loc[el["source"]], loc[el["target"]]
        c = chunk_base(cid, chunks)
        i = bloque_lista(c)
        lin += [f"## F{k}. `{cid}`: `{el['source']}` exceptua `{el['target']}`",
                "- herencia: " + " | ".join(f"[{h['tipo']} {h['unidad_origen']}] {h['texto'][:300]}"
                                            for j, h in enumerate(c["herencia"]) if h["tipo"] != "encabezado" or j == i
                                            or j == len(c["herencia"]) - 1),
                f"- texto propio: {c['texto'][:1500]}",
                f"- Excepcion: {ex['label']} | {(ex.get('properties') or {}).get('descripcion')} | tramo: "
                f"{(ex.get('provenance') or {}).get('tramo')}",
                f"- Operacion: {op['label']} | {(op.get('properties') or {}).get('descripcion')} | tramo: "
                f"{(op.get('provenance') or {}).get('tramo')}",
                "- otras entidades de la unidad: " + "; ".join(f"`{e['local_id']}` {e['type']}: {e['label']}"
                                                              for e in v_ents(regs, cid) if e["local_id"] not in
                                                              (el["source"], el["target"]) and e["type"] != "TextoOrdenado"),
                ""]
    open(os.path.join(OUT, "fichas_control_f.md"), "w", encoding="utf-8").write("\n".join(lin))
    # (3)
    leidos = [c for c in casos if c["clase_det"] == "LEER"]
    for k, c in enumerate(leidos, 1):
        c["n"] = k
    m3 = sorted(random.Random(20261008).sample(leidos, 25), key=lambda c: c["n"])
    lin = ["# Relectura de concordancia: 25 de los 255 casos leídos (semilla 20261008), sin ver los códigos", ""]
    for c in m3:
        lin.append(A.ficha_unidad(c["chunk_id"], [c], por_id, chunks, ents, sal))
        lin.append("")
    open(os.path.join(OUT, "fichas_relectura_25.md"), "w", encoding="utf-8").write("\n".join(lin))
    print(len(m1), len(filas), len(m3), [c["n"] for c in m3])


def v_ents(regs, cid):
    return (regs[cid].get("validacion") or {}).get("entidades") or []


if __name__ == "__main__":
    main()


def resto_i():
    """(4) Los 108 nodos del grupo I-SIN-NORMA-EN-LA-UNIDAD que el control (1) no leyó, en dos partes, para
    leerlos todos con el mismo criterio (decisión de esta unidad tras el control (1): 13 de 30 confirman (i))."""
    chunks, sal, origen, ents, regs = A.cargar_todo()
    kg = cargar_kg("diez")
    por_id = {n["id"]: n for n in kg["nodes"]}
    casos = json.load(open(os.path.join(OUT, "casos_a.json"), encoding="utf-8"))["diez"]
    leidos = {x["id"] for x in json.load(open(os.path.join(OUT, "muestra_control_i.json"), encoding="utf-8"))}
    resto = [c for c in casos if c["clase_det"] == "I-SIN-NORMA-EN-LA-UNIDAD" and c["id"] not in leidos]
    for k, c in enumerate(resto, 1):
        c["n"] = f"R{k}"
    mitad = (len(resto) + 1) // 2
    for parte, grupo in ((1, resto[:mitad]), (2, resto[mitad:])):
        lin = [f"# Grupo (i) por código, resto sin leer, parte {parte}", ""]
        for c in grupo:
            lin.append(A.ficha_unidad(c["chunk_id"], [c], por_id, chunks, ents, sal))
            lin.append("")
        open(os.path.join(OUT, f"fichas_resto_i_parte{parte}.md"), "w", encoding="utf-8").write("\n".join(lin))
    json.dump([{"resto": c["n"], "id": c["id"]} for c in resto],
              open(os.path.join(OUT, "muestra_resto_i.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(resto), mitad)


def unir_lecturas():
    """Une las cuatro partes de la lectura de los 255 casos en salida/lectura_a.json (ordenado por caso) y controla
    que estén los 255 una sola vez y con un código del criterio."""
    validos = {"I-ENC", "I-OTRA", "II-OP", "IV-OMI", "IV-NOEXT", "V-DEF", "V-OTRA"}
    todo = []
    for i in range(1, 5):
        todo += json.load(open(os.path.join(OUT, f"lectura_a_parte{i}.json"), encoding="utf-8"))
    assert sorted(x["caso"] for x in todo) == list(range(1, 256)), "faltan o sobran casos"
    assert all(x["codigo"] in validos for x in todo), "código fuera del criterio"
    json.dump(sorted(todo, key=lambda x: x["caso"]), open(os.path.join(OUT, "lectura_a.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(len(todo))


def partir_fichas():
    """Parte salida/fichas_lectura_a.md en cuatro archivos por bloque de unidad, de tamaño parecido (la lectura de
    los 255 casos se repartió en cuatro lectores)."""
    s = open(os.path.join(OUT, "fichas_lectura_a.md"), encoding="utf-8").read()
    bloques = ["## Unidad " + b for b in s.split("\n## Unidad ")[1:]]
    objetivo = sum(len(b) for b in bloques) / 4
    grupos, tam = [[]], 0
    for b in bloques:
        if tam > objetivo and len(grupos) < 4:
            grupos.append([])
            tam = 0
        grupos[-1].append(b)
        tam += len(b)
    for i, g in enumerate(grupos, 1):
        open(os.path.join(OUT, f"fichas_lectura_a_parte{i}.md"), "w", encoding="utf-8").write("\n".join(g))
    print([len(g) for g in grupos])
