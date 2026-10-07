"""Tarea b: procedencia hacia un ancestro en a9631a64 (y e22fae1a).

1. Población: los nodos de contenido cuyo `punto` es un ancestro de su unidad (222 en a9631a64), clasificados con la
   regla de VERIF-CAP3-COHERENCIA, tarea d (mismo orden: título del ancestro, párrafo, cruce, texto propio, no
   ubicado; misma normalización), para fijar los 113 cuyo tramo no está en el párrafo del ancestro.
2. Diagnóstico de los 113 con la verificación de tramo del validador r2 (`verificar_tramo`, tomada por AST de la
   copia de `validador_r2.py`, holgura 2 de la política r2), por bloque: texto propio de la unidad, título y párrafo
   de cada ancestro; el tramo compuesto «encabezado […] ítem» se ubica por su segundo segmento.
3. Corrección G propuesta (procedencia por tramo), aplicada a los 8.510 nodos de contenido: `punto` = la unidad si
   el tramo (o el segmento del ítem del tramo compuesto) está en su texto propio; si no, el ancestro cuyo bloque
   heredado lo contiene (párrafo, título o el cruce de los dos), con `rol_documental` = el tipo de ese bloque (en el
   cruce, el del párrafo); si el tramo no se ubica, sin cambio. Efecto en la unidad acreditable (por `punto`,
   regla de coincidencia exacta de A0.2) y en los ids (la clave de fusión r2b incluye el punto).

Uso: PYTHONDONTWRITEBYTECODE=1 <venv>/bin/python -B udiag_b_procedencia.py
Escribe salida/procedencia_b.json y salida/casos_b_20.md.
"""
import ast
import collections
import json
import os
import random
import re
import unicodedata

from udiag_comun import AQUI, SRC, CONTENIDO, cargar_kg, cargar_chunks, chunk_base, gid_de, norm, es_mini_chunk, \
    bloque_lista

OUT = os.path.join(AQUI, "salida")
SEMILLA = 20261007
HOLGURA = 2   # politica_campos_r2.json, parametros.mencion_holgura_tokens.valor (sha 82e8752a…)
SEP = re.compile(r"\s*\[\s*(?:…|\.\.\.)\s*\]\s*")


def _cargar_verificador():
    p = os.path.join(SRC, "code", "validador_r2.py")
    src = open(p, encoding="utf-8").read()
    nombres = {"_GUION", "_ALNUM", "fold", "tokens_con_spans", "norm_tokens", "_ventana_minima", "verificar_tramo"}
    partes = [ast.get_source_segment(src, n) for n in ast.parse(src).body
              if (isinstance(n, ast.FunctionDef) and n.name in nombres)
              or (isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id in nombres for t in n.targets))]
    from collections import Counter
    from typing import Optional
    g = {"re": re, "unicodedata": unicodedata, "Counter": Counter, "Optional": Optional}
    exec("\n\n".join(partes), g)
    return g["verificar_tramo"]


verificar_tramo = _cargar_verificador()


def unidad_de(cid):
    return cid.split("::")[1]


def contiene(p, u):
    if p == u:
        return False
    if p.startswith("S"):
        s = p[1:]
        return u == s or u.startswith(s + ".")
    return u.startswith(p + ".")


def clase_verif(p, ch):
    """La clasificación de VERIF-CAP3-COHERENCIA, tarea d (verif_cap3_tarea_d_cadena_procedencia.py, bloque 3)."""
    t = norm(p.get("tramo"))
    en_tit = any(t and t in norm(h["texto"]) for h in ch["herencia"]
                 if h["unidad_origen"] == p["punto"] and h["tipo"] == "encabezado")
    en_par = any(t and t in norm(h["texto"]) for h in ch["herencia"]
                 if h["unidad_origen"] == p["punto"] and h["tipo"] != "encabezado")
    en_propio = bool(t) and t in norm(ch["texto"])
    unido = norm("\n".join(h["texto"] for h in ch["herencia"] if h["unidad_origen"] == p["punto"]))
    en_unido = bool(t) and t in unido
    return ("titulo_del_ancestro" if en_tit else "parrafo_del_ancestro" if en_par
            else "cruza_titulo_y_parrafo_del_ancestro" if en_unido
            else "texto_propio_de_la_unidad" if en_propio else "no_ubicado")


def ok(nivel):
    return nivel in ("exacta", "tokens")


def ubicar(tramo, ch):
    """Dónde está el tramo, con la verificación del validador. Devuelve (lugar, ancestro, tipo_de_bloque, nivel)."""
    if not tramo:
        return ("sin_tramo", None, None, None)
    segs = SEP.split(tramo)
    compuesto = len(segs) == 2
    aguja = segs[-1] if compuesto else tramo
    n_prop = verificar_tramo(aguja, ch.get("texto") or "", HOLGURA)[0]
    if ok(n_prop):
        return ("compuesto_item_en_texto_propio" if compuesto else "texto_propio", ch["unidad"], None, n_prop)
    if compuesto:
        aguja = tramo.replace("[…]", " ").replace("[...]", " ")
    # ancestros, del más cercano al más lejano
    orden = []
    for h in ch["herencia"]:
        if h["unidad_origen"] not in orden:
            orden.append(h["unidad_origen"])
    if es_mini_chunk(ch):
        # el título de la propia unidad del mini-chunk (último bloque heredado) es parte de su unidad
        propios = [h["texto"] for h in ch["herencia"] if h["unidad_origen"] == ch["unidad"]]
        if propios and ok(verificar_tramo(aguja, "\n".join(propios + [ch.get("texto") or ""]), HOLGURA)[0]):
            return ("texto_propio", ch["unidad"], None, "exacta_o_tokens_con_el_titulo_propio")
    for q in reversed(orden):
        if es_mini_chunk(ch) and q == ch["unidad"]:
            continue
        bloques = [h for h in ch["herencia"] if h["unidad_origen"] == q]
        par = [h for h in bloques if h["tipo"] != "encabezado"]
        tit = [h for h in bloques if h["tipo"] == "encabezado"]
        for h in par:
            n = verificar_tramo(aguja, h["texto"], HOLGURA)[0]
            if ok(n):
                return ("parrafo", q, h["tipo"], n)
        for h in tit:
            n = verificar_tramo(aguja, h["texto"], HOLGURA)[0]
            if ok(n):
                return ("titulo", q, "encabezado", n)
        n = verificar_tramo(aguja, "\n".join(h["texto"] for h in bloques), HOLGURA)[0]
        if ok(n):
            return ("cruza_titulo_y_parrafo", q, (par[0]["tipo"] if par else "encabezado"), n)
    n = verificar_tramo(aguja, "\n".join([h["texto"] for h in ch["herencia"]] + [ch.get("texto") or ""]), HOLGURA)[0]
    if ok(n):
        return ("cruza_herencia_y_texto_propio", None, None, n)
    return ("no_ubicado", None, None, None)


def correccion_g(p, ch, restringida=False):
    """(punto, rol) que daría la corrección G, o None si no cambia nada (tramo no ubicado o sin tramo).
    `restringida` (G-r): el punto solo se corrige si el modelo lo puso en un ancestro; si lo puso en la unidad,
    queda la unidad (la norma compuesta de un ítem es del ítem, P3C-d2) y no cambia nada."""
    if restringida and p["punto"] == ch["unidad"]:
        return None
    lugar, q, tipo, _ = ubicar(p.get("tramo"), ch)
    if lugar in ("texto_propio", "compuesto_item_en_texto_propio"):
        return ch["unidad"], (f"bloque_{ch['rol_bloque']}" if es_mini_chunk(ch) else "punto_propio")
    if lugar in ("parrafo", "titulo", "cruza_titulo_y_parrafo"):
        return q, f"herencia_{tipo}"
    return None


def efecto_g(cont, chunks, ids, restringida, hermanas):
    cambios, colisiones = [], 0
    for n in cont:
        p = n["provenance"]
        ch = chunk_base(p["chunk_id"], chunks)
        g = correccion_g(p, ch, restringida)
        if not g:
            continue
        nuevo_punto, nuevo_rol = g
        if nuevo_punto == p["punto"] and nuevo_rol == p["rol_documental"]:
            continue
        u = ch["unidad"]
        if nuevo_punto == p["punto"]:
            cambio = "no"
        else:
            cambio = ("unidad" if p["punto"] == u else "ancestro") + "->" + ("unidad" if nuevo_punto == u else "ancestro")
        c = {"id": n["id"], "type": n["type"], "to": p["to"], "chunk_id": p["chunk_id"], "punto": p["punto"],
             "punto_g": nuevo_punto, "rol": p["rol_documental"], "rol_g": nuevo_rol, "cambio_punto": cambio,
             "tipo_unidad": "item" if bloque_lista(ch) is not None else ("mini" if es_mini_chunk(ch) else "punto")}
        if cambio != "no":
            gid = gid_de({"type": n["type"], "label": n["label"], "properties": n.get("properties") or {}},
                         {**p, "punto": nuevo_punto})
            c["id_g"] = gid
            c["fusiona_con_nodo_existente"] = gid in ids and gid != n["id"]
            colisiones += c["fusiona_con_nodo_existente"]
            # lectura del §5.6 del pre-registro de tripletas: subgrafos de unidades hermanas (otros descendientes del
            # punto viejo) que dejan de incluir el nodo cuando el punto pasa del ancestro a la unidad
            if cambio == "ancestro->unidad":
                c["hermanas_que_lo_pierden"] = len([x for x in hermanas.get((p["to"], p["punto"]), ()) if x != u
                                                    and not x.startswith(u + ".")])
        cambios.append(c)
    return cambios, colisiones


def medir(nombre, chunks):
    kg = cargar_kg(nombre)
    cont = [n for n in kg["nodes"] if n["type"] in CONTENIDO]
    ids = {n["id"] for n in kg["nodes"]}
    poblacion = [n for n in cont if contiene(n["provenance"]["punto"], unidad_de(n["provenance"]["chunk_id"]))]
    filas = []
    for n in sorted(poblacion, key=lambda x: x["id"]):
        p = n["provenance"]
        ch = chunk_base(p["chunk_id"], chunks)
        lugar, q, tipo, nivel = ubicar(p.get("tramo"), ch)
        g = correccion_g(p, ch)
        filas.append({"id": n["id"], "type": n["type"], "label": n["label"], "to": p["to"], "chunk_id": p["chunk_id"],
                      "punto": p["punto"], "rol_documental": p["rol_documental"], "tramo": p.get("tramo"),
                      "tramo_verificado": p.get("tramo_verificado"), "clase_verif": clase_verif(p, ch),
                      "lugar": lugar, "ancestro_del_tramo": q, "bloque": tipo, "nivel": nivel,
                      "punto_g": g[0] if g else p["punto"], "rol_g": g[1] if g else p["rol_documental"],
                      "lista_abierta_por_el_titulo": any(h["tipo"] == "encabezado" and h["unidad_origen"] == p["punto"]
                                                         and " ".join(h["texto"].split()).endswith(":")
                                                         for h in ch["herencia"])})
    hermanas = collections.defaultdict(set)
    for c in chunks.values():
        for h in c["herencia"]:
            hermanas[(c["to"], h["unidad_origen"])].add(c["unidad"])
    cambios, colisiones = efecto_g(cont, chunks, ids, False, hermanas)
    cambios_r, colisiones_r = efecto_g(cont, chunks, ids, True, hermanas)
    return kg, poblacion, filas, (cambios, colisiones), (cambios_r, colisiones_r)


def resumen_g(cambios, colisiones):
    cp = [c for c in cambios if c["cambio_punto"] != "no"]
    return {
        "nodos_que_cambian_algo": len(cambios),
        "cambian_punto": len(cp),
        "cambio_punto": dict(collections.Counter(c["cambio_punto"] for c in cp).most_common()),
        "cambian_punto_por_tipo": dict(collections.Counter(c["type"] for c in cp).most_common()),
        "cambian_punto_por_to": dict(collections.Counter(c["to"] for c in cp).most_common()),
        "cambian_punto_por_tipo_de_unidad_y_sentido": dict(collections.Counter(
            f"{c['tipo_unidad']}:{c['cambio_punto']}" for c in cp).most_common()),
        "cambian_solo_rol": sum(c["cambio_punto"] == "no" for c in cambios),
        "rol_antes_despues_solo_rol": dict(collections.Counter(f"{c['rol']} -> {c['rol_g']}" for c in cambios
                                                               if c["cambio_punto"] == "no").most_common()),
        "ids_que_fusionarian_con_un_nodo_existente": colisiones,
        "pertenencias_a_subgrafos_de_hermanas_que_se_pierden": sum(c.get("hermanas_que_lo_pierden", 0) for c in cp)}


def resumen(filas, g_lit, g_r):
    los113 = [f for f in filas if f["clase_verif"] != "parrafo_del_ancestro"]

    def diag(f):
        if f["lugar"] in ("texto_propio", "compuesto_item_en_texto_propio"):
            return "punto_mal_atribuido:a_la_unidad"
        if f["lugar"] in ("parrafo", "titulo", "cruza_titulo_y_parrafo") and f["ancestro_del_tramo"] != f["punto"]:
            return "punto_mal_atribuido:a_otro_ancestro"
        if f["lugar"] in ("parrafo", "cruza_titulo_y_parrafo"):
            return "rol_mal:deberia_ser_el_parrafo_heredado"
        if f["lugar"] == "titulo":
            return "punto_y_rol_coherentes:tramo_en_el_titulo_del_ancestro"
        return "no_ubicado"

    for f in filas:
        f["diagnostico"] = diag(f)
    return {
        "poblacion": len(filas),
        "clase_verif": dict(collections.Counter(f["clase_verif"] for f in filas).most_common()),
        "tramo_fuera_del_parrafo_del_ancestro": len(los113),
        "fuera_del_parrafo_por_clase_verif": dict(collections.Counter(f["clase_verif"] for f in los113).most_common()),
        "fuera_del_parrafo_por_diagnostico": dict(collections.Counter(f["diagnostico"] for f in los113).most_common()),
        "fuera_del_parrafo_diagnostico_por_clase_verif": {k: dict(collections.Counter(
            f["diagnostico"] for f in los113 if f["clase_verif"] == k).most_common())
            for k in sorted({f["clase_verif"] for f in los113})},
        "fuera_del_parrafo_por_nivel": dict(collections.Counter(f["nivel"] for f in los113).most_common()),
        "poblacion_por_diagnostico": dict(collections.Counter(f["diagnostico"] for f in filas).most_common()),
        "poblacion_con_lista_abierta_por_el_titulo": sum(f["lista_abierta_por_el_titulo"] for f in filas),
        "g_restringida_en_la_poblacion": {
            "cambia_punto": sum(f["punto_g"] != f["punto"] for f in filas),
            "cambia_punto_por_tipo": dict(collections.Counter(f["type"] for f in filas
                                                              if f["punto_g"] != f["punto"]).most_common()),
            "cambia_solo_rol": sum(f["punto_g"] == f["punto"] and f["rol_g"] != f["rol_documental"] for f in filas),
            "sin_cambio": sum(f["punto_g"] == f["punto"] and f["rol_g"] == f["rol_documental"] for f in filas)},
        "g_literal_en_todos_los_nodos_de_contenido": resumen_g(*g_lit),
        "g_restringida_en_todos_los_nodos_de_contenido": resumen_g(*g_r)}


def main():
    chunks = cargar_chunks()
    out = {"semilla": SEMILLA, "holgura": HOLGURA}
    for nombre in ("diez", "sincola"):
        kg, pob, filas, g_lit, g_r = medir(nombre, chunks)
        out[nombre] = {"resumen": resumen(filas, g_lit, g_r), "filas": filas, "cambios_g_literal": g_lit[0],
                       "cambios_g_restringida": g_r[0]}
    # 20 casos de los 113 del diez, estratificados por diagnóstico (semilla declarada)
    los113 = [f for f in out["diez"]["filas"] if f["clase_verif"] != "parrafo_del_ancestro"]
    rng = random.Random(SEMILLA)
    por = collections.defaultdict(list)
    for f in los113:
        por[f["diagnostico"]].append(f)
    cuota = {k: max(1, round(20 * len(v) / len(los113))) for k, v in por.items()}
    while sum(cuota.values()) > 20:
        k = max(cuota, key=lambda x: cuota[x])
        cuota[k] -= 1
    while sum(cuota.values()) < 20:
        k = max(por, key=lambda x: len(por[x]) - cuota[x])
        cuota[k] += 1
    sel = []
    for k in sorted(por):
        sel += sorted(rng.sample(por[k], min(cuota[k], len(por[k]))), key=lambda x: x["id"])
    lin = ["# Tarea b: 20 de los 113 nodos con el punto en un ancestro y el tramo fuera de su párrafo",
           "", f"Muestra estratificada por diagnóstico, semilla {SEMILLA}; cuotas {cuota}.", ""]
    for i, f in enumerate(sel, 1):
        ch = chunk_base(f["chunk_id"], chunks)
        anc = [h for h in ch["herencia"] if h["unidad_origen"] in (f["punto"], f["ancestro_del_tramo"])]
        lin += [f"## B{i}. {f['type']} «{f['label']}» — {f['diagnostico']}",
                f"- `{f['chunk_id']}`; punto {f['punto']}; rol {f['rol_documental']}; clase de VERIF {f['clase_verif']}; "
                f"lugar del tramo: {f['lugar']} (ancestro {f['ancestro_del_tramo']}, bloque {f['bloque']}, nivel {f['nivel']})",
                f"- tramo: {f['tramo']}",
                "- bloques del ancestro: " + " | ".join(f"[{h['tipo']} {h['unidad_origen']}] {h['texto'][:300]}" for h in anc),
                f"- texto propio: {ch['texto'][:500]}",
                f"- con G: punto {f['punto_g']}, rol {f['rol_g']}", ""]
    open(os.path.join(OUT, "casos_b_20.md"), "w", encoding="utf-8").write("\n".join(lin))
    json.dump(out, open(os.path.join(OUT, "procedencia_b.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps({k: out[k]["resumen"] for k in ("diez", "sincola")}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
