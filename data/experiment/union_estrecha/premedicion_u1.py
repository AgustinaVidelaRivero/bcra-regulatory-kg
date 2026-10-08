"""U-UNION-ESTRECHA, U1: pre-medición de la regla estrecha (regla_u1.md) sobre lo guardado, sin leer ninguna unión.

Uso: PYTHONDONTWRITEBYTECODE=1 <venv>/bin/python -B premedicion_u1.py <dir_fuentes> <dir_control> <dir_salida>
- <dir_fuentes>: copias de `git show <commit>:<ruta>` (ver comandos_u1.sh): code/ (prompt_r2b.py, comun_e1.py,
  modelos_r2.py), e0_r2b/chunks_<to>.json de los diez TOs, ens_diez/kg.json (a9631a64) y ens_sincola/kg.json
  (e22fae1a).
- <dir_control>: union_e.json y muestra_union_e.md de U-DIAG-CAP3-GRAFO (ids de la lectura de control de la regla E;
  sin veredictos). La muestra se reproduce con su semilla y se compara con los encabezados de muestra_union_e.md.
- Escribe en <dir_salida>: premedicion_u1.json, premedicion_u1.md, registro_u1_diez.json, registro_u1_sincola.json,
  encabezados_u1.json y marco_u2_diez.json. Sin hora ni rutas absolutas: dos corridas dan los mismos bytes.
"""
import ast
import collections
import hashlib
import json
import os
import random
import re
import sys
import unicodedata

import regla_u1 as R

TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
SHA_GRAFOS = {
    "diez": "a9631a64b422bdae634fb05135373c6f04c6272cdf7acd43a1be9f5b6c1f5f57",
    "sincola": "e22fae1afc3cf37fbe5b49ee0b220d51d0ec5febc13abeb6ebf7b74226da34fb",
}
DIR_GRAFO = {"diez": "ens_diez", "sincola": "ens_sincola"}
SEMILLA_CONTROL = 20261007
N_CONTROL = 30
N_MUESTRA_U2 = 30


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def _tomar(path, nombres, extra=None):
    """Asignaciones y funciones de un módulo, tomadas por AST y ejecutadas aisladas (sin importar el módulo)."""
    src = open(path, encoding="utf-8").read()
    partes = []
    for nodo in ast.parse(src).body:
        if isinstance(nodo, ast.FunctionDef) and nodo.name in nombres:
            partes.append(ast.get_source_segment(src, nodo))
        elif isinstance(nodo, ast.Assign) and any(isinstance(t, ast.Name) and t.id in nombres for t in nodo.targets):
            partes.append(ast.get_source_segment(src, nodo))
        elif isinstance(nodo, ast.AnnAssign) and isinstance(nodo.target, ast.Name) and nodo.target.id in nombres:
            partes.append(ast.get_source_segment(src, nodo))
    g = {"re": re, "unicodedata": unicodedata}
    g.update(extra or {})
    exec("from __future__ import annotations\n" + "\n\n".join(partes), g)
    faltan = set(nombres) - set(g)
    if faltan:
        raise ValueError(f"{os.path.basename(path)}: no están {sorted(faltan)}")
    return g


def cargar_codigo(fuentes):
    code = os.path.join(fuentes, "code")
    ce = _tomar(os.path.join(code, "comun_e1.py"), {"es_mini_chunk"})
    pb = _tomar(os.path.join(code, "prompt_r2b.py"), {"bloque_lista"}, {"es_mini_chunk": ce["es_mini_chunk"]})
    mo = _tomar(os.path.join(code, "modelos_r2.py"),
                {"TIPO_SUJETO", "FIRMAS_CONGELADAS", "AMPLIACION_R2", "_matriz_r2"})
    rango = mo["_matriz_r2"]()["condicion_de"][1]
    return {"bloque_lista": pb["bloque_lista"], "es_mini_chunk": ce["es_mini_chunk"], "rango": tuple(rango),
            "sha": {f: sha(os.path.join(code, f)) for f in ("comun_e1.py", "prompt_r2b.py", "modelos_r2.py")}}


def cargar_chunks(fuentes):
    out = {}
    for t in TOS:
        for c in json.load(open(os.path.join(fuentes, "e0_r2b", f"chunks_{t}.json"), encoding="utf-8")):
            out[c["id"]] = c
    return out


def inventario_bloques(chunks, cod):
    """Todo bloque heredado que abre una lista en los diez TOs, con su anuncio (regla, punto 2)."""
    vistos = {}
    for c in chunks.values():
        if cod["es_mini_chunk"](c):
            continue
        i = cod["bloque_lista"](c)
        if i is None:
            continue
        h = c["herencia"][i]
        clave = f"{c['to']}::{h['unidad_origen']}[{h['tipo']}]"
        if clave not in vistos:
            an = R.anuncio(h["texto"])
            vistos[clave] = {"items": 0, "tipo_bloque": h["tipo"], "forma": an["forma"], "subforma": an["subforma"],
                             "subordinante": an["subordinante"], "marca_excepcion": an["marca_excepcion"],
                             "compatibles": list(R.compatibles(an)), "segmento": an["segmento"]}
        vistos[clave]["items"] += 1
    return dict(sorted(vistos.items()))


def control_diagnostico(control):
    """Los 30 de la lectura de control de la regla E: la muestra de udiag_a_union.py, reproducida con su semilla
    sobre union_e.json y comparada, posición por posición, con los encabezados de muestra_union_e.md."""
    ue = json.load(open(os.path.join(control, "union_e.json"), encoding="utf-8"))
    if ue.get("semilla") != SEMILLA_CONTROL:
        raise ValueError(f"semilla de union_e.json: {ue.get('semilla')}")
    uniones = [f for f in ue["diez"]["filas"] if f["resultado"] == "union"]
    muestra = random.Random(SEMILLA_CONTROL).sample(uniones, N_CONTROL)
    pat = re.compile(r"^## U(\d+)\. (\w+) → (\w+) \(`([^`]+)` → `([^`]+)`\)$")
    cab = [m.groups() for m in (pat.match(x) for x in open(os.path.join(control, "muestra_union_e.md"),
                                                          encoding="utf-8").read().splitlines()) if m]
    esperado = [(str(k), f["type"], f["candidatos"][0][1], f["chunk_id"], f["encabezado"])
                for k, f in enumerate(muestra, 1)]
    if cab != esperado:
        raise ValueError("la muestra reproducida no coincide con muestra_union_e.md")
    return {"ids": [f["id"] for f in muestra], "tipos": dict(sorted(collections.Counter(f["type"] for f in muestra).items())),
            "destino": {f["id"]: f["candidatos"][0][0] for f in muestra},
            "uniones_regla_e_diez": {(f["id"], f["candidatos"][0][0]) for f in uniones},
            "sha": {f: sha(os.path.join(control, f)) for f in ("union_e.json", "muestra_union_e.md")}}


def tabla_md(titulo, d):
    lin = [f"| {titulo} | n |", "|---|---:|"] + [f"| {k} | {v} |" for k, v in d.items()]
    return lin + [f"| total | {sum(d.values())} |", ""]


def main():
    fuentes, control, salida = sys.argv[1:4]
    os.makedirs(salida, exist_ok=True)
    cod = cargar_codigo(fuentes)
    if tuple(sorted(cod["rango"])) != tuple(sorted(R.RANGO_CONDICION_DE)):
        raise ValueError(f"rango de condicion_de en modelos_r2: {cod['rango']}")
    chunks = cargar_chunks(fuentes)
    ctl = control_diagnostico(control)
    ids_control = set(ctl["ids"])
    out = {"entradas": {"grafos": {}, "codigo": cod["sha"], "control": ctl["sha"],
                        "chunks_e0": {t: sha(os.path.join(fuentes, "e0_r2b", f"chunks_{t}.json")) for t in TOS}},
           "control_diagnostico": {"semilla": SEMILLA_CONTROL, "n": len(ctl["ids"]), "por_tipo": ctl["tipos"]}}
    inv = inventario_bloques(chunks, cod)
    out["bloques_que_abren_lista"] = {
        "bloques": len(inv), "items": sum(b["items"] for b in inv.values()),
        "por_forma": dict(sorted(collections.Counter(str(b["forma"]) for b in inv.values()).items())),
        "por_subforma": dict(sorted(collections.Counter(str(b["subforma"]) for b in inv.values()).items())),
        "con_marca_de_excepcion_y_anuncio": sum(1 for b in inv.values() if b["forma"] and b["marca_excepcion"])}
    json.dump(inv, open(os.path.join(salida, "encabezados_u1.json"), "w", encoding="utf-8"), ensure_ascii=False,
              indent=1)
    md = ["# U-UNION-ESTRECHA, U1: pre-medición de la regla (sin leer ninguna unión)", "",
          "Generado por `premedicion_u1.py` (regla en `regla_u1.md`, código en `regla_u1.py`). Fuentes: "
          "`premedicion_u1.json`, sección `entradas`.", "",
          f"Bloques que abren lista en los diez TOs: {len(inv)} ({out['bloques_que_abren_lista']['items']} ítems); "
          "por forma de anuncio: " + "; ".join(f"{k} {v}" for k, v in out["bloques_que_abren_lista"]["por_forma"].items())
          + ". El anuncio de cada uno, en `encabezados_u1.json`.", ""]
    for nombre in ("diez", "sincola"):
        p = os.path.join(fuentes, DIR_GRAFO[nombre], "kg.json")
        s = sha(p)
        if s != SHA_GRAFOS[nombre]:
            raise ValueError(f"sha del grafo {nombre}: {s}")
        out["entradas"]["grafos"][nombre] = s
        kg = json.load(open(p, encoding="utf-8"))
        registro, aristas, encabezados = R.aplicar(kg, chunks, cod["bloque_lista"], cod["es_mini_chunk"])
        for f in registro:
            f["en_control_diagnostico"] = f["id"] in ids_control
        res = R.resumen(registro, kg)
        uniones = [f for f in registro if f["resultado"] == "union"]
        en_ctl = [f for f in uniones if f["en_control_diagnostico"]]
        res["control_diagnostico"] = {
            "condicion_del_control_en_el_registro": sum(1 for f in registro if f["en_control_diagnostico"]),
            "resultado_de_las_condicion_del_control": dict(sorted(collections.Counter(
                f["resultado"] for f in registro if f["en_control_diagnostico"]).items())),
            "uniones_entre_las_30": len(en_ctl),
            "uniones_entre_las_30_con_el_mismo_destino": sum(1 for f in en_ctl if ctl["destino"][f["id"]] == f["destino"])}
        res["uniones_tambien_de_la_regla_e"] = (sum(1 for f in uniones if (f["id"], f["destino"])
                                                    in ctl["uniones_regla_e_diez"]) if nombre == "diez" else None)
        if nombre == "diez":
            marco = sorted(f["id"] for f in uniones if not f["en_control_diagnostico"])
            res["marco_u2"] = {"uniones_fuera_del_control": len(marco), "muestra_prevista": N_MUESTRA_U2,
                               "alcanza_para_la_muestra": len(marco) >= N_MUESTRA_U2}
            json.dump({"grafo": s, "excluidas_por_el_control": sorted(f["id"] for f in en_ctl), "marco": marco},
                      open(os.path.join(salida, "marco_u2_diez.json"), "w", encoding="utf-8"), ensure_ascii=False,
                      indent=1)
        out[nombre] = res
        json.dump({"grafo": s, "registro": registro, "aristas": aristas, "encabezados": dict(sorted(encabezados.items()))},
                  open(os.path.join(salida, f"registro_u1_{nombre}.json"), "w", encoding="utf-8"), ensure_ascii=False,
                  indent=1)
        md += [f"## {nombre} (`{s[:8]}…`)", "",
               f"Condicion en el grafo: {res['condicion_en_el_grafo']}; Condicion de ítem sin `condicion_de` saliente: "
               f"{res['condicion_de_item_sin_condicion_de']}.", ""]
        md += tabla_md("resultado", res["resultado"])
        md += tabla_md("uniones por tipo de destino", res["uniones_por_tipo_destino"])
        md += tabla_md("uniones por TO", res["uniones_por_to"])
        md += tabla_md("ambiguas por número de candidatos", res["ambiguas_por_numero_de_candidatos"])
        md += tabla_md("destino no compatible, por tipo del único candidato", res["destino_no_compatible_por_tipo"])
        md += tabla_md("cruce anuncio | candidatos", res["cruce_anuncio_por_candidatos"])
        c = res["control_diagnostico"]
        md += [f"Lectura de control del diagnóstico (30 ids, semilla {SEMILLA_CONTROL}): Condicion del control en el "
               f"registro {c['condicion_del_control_en_el_registro']}; uniones de esta regla entre las 30: "
               f"{c['uniones_entre_las_30']} (con el mismo destino: {c['uniones_entre_las_30_con_el_mismo_destino']}).", ""]
        if nombre == "diez":
            m = res["marco_u2"]
            md += [f"Uniones también de la regla E: {res['uniones_tambien_de_la_regla_e']}. Marco de U2 (uniones fuera "
                   f"del control): {m['uniones_fuera_del_control']}; alcanza para una muestra de {N_MUESTRA_U2}: "
                   f"{'sí' if m['alcanza_para_la_muestra'] else 'NO'}.", ""]
    json.dump(out, open(os.path.join(salida, "premedicion_u1.json"), "w", encoding="utf-8"), ensure_ascii=False,
              indent=1)
    open(os.path.join(salida, "premedicion_u1.md"), "w", encoding="utf-8").write("\n".join(md))
    print(json.dumps({k: out[k] for k in ("diez", "sincola", "bloques_que_abren_lista")}, ensure_ascii=False,
                     indent=1))


if __name__ == "__main__":
    main()
