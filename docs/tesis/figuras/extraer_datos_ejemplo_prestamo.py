#!/usr/bin/env python3
"""Datos del ejemplo del préstamo para las figuras 1.1, 1.2, 1.3 y 2.1.

El ejemplo es el punto 5.1.1.1 del Texto Ordenado de Clasificación de deudores,
que remite al punto 3.7 («importe de referencia»). Este script junta en
ejemplo_prestamo_datos.json todo lo que las figuras muestran del ejemplo, para
que ningún generador lo tenga escrito a mano:

 (a) los textos de la norma: el campo `texto` de los fragmentos E0 de
     cla::5.1.1.1 y cla::3.7, y la frase de la unidad 5.1.1 que los encabeza
     (encabezado «5.1.1. Cartera comercial.» y texto del bloque intro
     cla::5.1.1::intro), con los cortes de línea quitados y las palabras
     partidas por guion al final de línea reunidas; nada más se cambia;
 (b) los cinco nodos y las cuatro aristas del ejemplo, leídos de kg.json del
     grafo r1 (sha256 comprobado); cada nodo se busca por tipo y etiqueta y su
     id se coteja con el del paquete de U-MED-EJEMPLO-2; si falta un nodo o una
     arista, el script se detiene;
 (c) la búsqueda léxica sobre los 1.763 fragmentos con la pregunta del
     ejemplo, variante A (busqueda_lexica_fragmentos.py): el top-5 y los rangos
     de cla::5.1.1.1 y cla::3.7;
 (d) copiados del paquete de U-MED-EJEMPLO-2, versionado en reports/u_med_ejemplo/
     (commit 200462f), con el sha256 de cada archivo de origen, los resultados de
     la variante B del Paso 1 y de la búsqueda sobre nodos del Paso 3.

Control: (c) debe reproducir el Paso 1 de U-MED-EJEMPLO-2 —cla::5.1.1.1 en el
puesto 2, cla::3.7 en el 1.523 y el mismo top-10 con los mismos puntajes—; si
no, el script se detiene sin escribir.

Solo lectura salvo el JSON de salida. Sin API ni modelos. Uso:
    PYTHONDONTWRITEBYTECODE=1 python3 docs/tesis/figuras/extraer_datos_ejemplo_prestamo.py
"""

import sys

sys.dont_write_bytecode = True  # importar el módulo hermano no deja __pycache__

import hashlib  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import re  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import busqueda_lexica_fragmentos as bl  # noqa: E402

RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", ".."))
KG_REL = "data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json"
KG_SHA256 = "0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a"
CHUNKS_CLA_REL = "data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_cla.json"
SALIDA = os.path.join(AQUI, "ejemplo_prestamo_datos.json")

# Paquete de U-MED-EJEMPLO-2, versionado en el commit 200462f. Ruta relativa a
# la raíz del repositorio.
PAQUETE = "reports/u_med_ejemplo"
PAQUETE_SHA256 = {  # reports/u_med_ejemplo/umed_manifest.txt, líneas 11, 15 y 18
    "umed2_analista_paso1_resultado.json": "a69c44b00a7f4920d1a4e5224167e6edacf4b7153d004d2185050cb2387f5408",
    "umed2_analista_paso2_resultado.json": "3d120f6dc2a756738414ef25c823678851c84b73316b9e529eff2b26cf0b6402",
    "umed2_analista_paso3_resultado.json": "047e6f6e80b6b88e300cfb090bd2223ea967de8c9cbea9e10f9c04a9c168a3cd",
}

PREGUNTA = ("Para una entidad financiera, ¿qué condiciones hacen que los créditos para "
            "consumo o vivienda deban clasificarse en la cartera comercial?")

# (a) Textos. La frase que encabeza a 5.1.1.1 se compone con el encabezado de la
# unidad 5.1.1 y el texto de su bloque intro; se coteja con la forma esperada.
PUNTOS_TEXTO = ["cla::5.1.1.1", "cla::3.7"]
INTRO_5_1_1 = "cla::5.1.1::intro"
FRASE_5_1_1 = ("5.1.1. Cartera comercial. Abarca todas las financiaciones comprendidas, "
               "con excepción de las siguientes:")
FRASE_RESALTADA = "dos veces el importe de referencia establecido en el punto 3.7."

# (b) Nodos: (clave, tipo, etiqueta en el grafo, punto de procedencia o None).
# Los tipos Operacion, Restriccion y Obligacion provienen de un punto; el Sujeto
# es un nodo de catálogo y se registra con todas sus procedencias.
NODOS = [
    ("operacion", "Operacion",
     "Inclusión en cartera comercial — créditos consumo/vivienda", "5.1.1.1"),
    ("restriccion_monto", "Restriccion",
     "Créditos consumo/vivienda — monto supera dos veces importe referencia", "5.1.1.1"),
    ("restriccion_repago", "Restriccion",
     "Crédito — repago no vinculado a ingresos fijos, vinculado a actividad productiva", "5.1.1.1"),
    ("obligacion_3_7", "Obligacion",
     "Considerar importe de referencia — ventas anuales Micro Comercio", "3.7"),
    ("sujeto", "Sujeto", "Obligados a clasificar deudores (Clasificación)", None),
]
# (origen, relación en el grafo, destino)
ARISTAS = [
    ("restriccion_monto", "limita", "operacion"),
    ("restriccion_repago", "limita", "operacion"),
    ("restriccion_monto", "referencia", "obligacion_3_7"),
    ("obligacion_3_7", "aplica_a", "sujeto"),
]

# (c) Búsqueda y su control.
TOPK = 5
OBJETIVOS = ["cla::5.1.1.1", "cla::3.7"]
RANGOS_ESPERADOS = {"cla::5.1.1.1": 2, "cla::3.7": 1523}


def sha256_archivo(ruta):
    with open(ruta, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def leer_paquete(nombre):
    ruta = f"{PAQUETE}/{nombre}"
    sha = sha256_archivo(os.path.join(RAIZ, ruta))
    if sha != PAQUETE_SHA256[nombre]:
        raise SystemExit(f"{ruta}: sha256 {sha} ≠ manifiesto {PAQUETE_SHA256[nombre]}")
    with open(os.path.join(RAIZ, ruta), encoding="utf-8") as fh:
        return json.load(fh), ruta, sha


# --------------------------------------------------------------------------- #
# (a) Textos de la norma                                                       #
# --------------------------------------------------------------------------- #
def texto_de_figura(crudo):
    """Quita los cortes de línea y reúne las palabras partidas por guion al
    final de línea. Devuelve (texto, palabras reunidas)."""
    reunidas = [f"{a}-{b} → {a}{b}" for a, b in re.findall(r"(\w+)-\n(\w+)", crudo)]
    texto = re.sub(r"(\w)-\n(\w)", r"\1\2", crudo).replace("\n", " ")
    if "  " in texto:
        raise SystemExit("quitar los cortes de línea dejó un espacio doble")
    return texto, reunidas


def extraer_textos():
    ruta = os.path.join(RAIZ, CHUNKS_CLA_REL)
    with open(ruta, encoding="utf-8") as fh:
        chunks = {c["id"]: c for c in json.load(fh)}
    salida = {}
    for cid in PUNTOS_TEXTO:
        c = chunks[cid]
        texto, reunidas = texto_de_figura(c["texto"])
        salida[cid] = {"unidad": c["unidad"], "titulo": c["titulo"], "paginas": c["paginas"],
                       "sha256_propio": c["sha256_propio"], "texto_campo": c["texto"],
                       "texto": texto, "palabras_reunidas": reunidas}
    # Frase de la unidad 5.1.1: el encabezado heredado de la unidad y el texto
    # del bloque intro, que en el texto completo del fragmento son dos líneas.
    intro = chunks[INTRO_5_1_1]
    enc = [h for h in intro["herencia"] if h["tipo"] == "encabezado" and h["unidad_origen"] == "5.1.1"]
    if len(enc) != 1:
        raise SystemExit(f"{INTRO_5_1_1}: se esperaba un encabezado de la unidad 5.1.1")
    crudo = enc[0]["texto"] + "\n" + intro["texto"]
    frase, reunidas = texto_de_figura(crudo)
    if frase != FRASE_5_1_1:
        raise SystemExit(f"la frase de 5.1.1 no es la esperada: {frase!r}")
    # La misma frase encabeza a 5.1.1.1: su herencia lleva ese encabezado y ese intro.
    her = chunks["cla::5.1.1.1"]["herencia"]
    piezas = [h["texto"] for h in her if h["unidad_origen"] == "5.1.1"]
    if piezas != [enc[0]["texto"], intro["texto"]]:
        raise SystemExit("la herencia de cla::5.1.1.1 no lleva la frase de la unidad 5.1.1")
    salida["cla::5.1.1"] = {"unidad": "5.1.1", "fragmento_origen": INTRO_5_1_1,
                            "piezas": {"encabezado_heredado": enc[0]["texto"],
                                       "texto_bloque_intro": intro["texto"]},
                            "texto": frase, "palabras_reunidas": reunidas}
    if FRASE_RESALTADA not in salida["cla::5.1.1.1"]["texto"]:
        raise SystemExit("la frase resaltada no está en el texto de cla::5.1.1.1")
    return salida, {"ruta": CHUNKS_CLA_REL, "sha256": sha256_archivo(ruta)}


# --------------------------------------------------------------------------- #
# (b) Nodos y aristas del grafo r1                                             #
# --------------------------------------------------------------------------- #
def provenances(elem):
    ps = ([elem["provenance"]] if elem.get("provenance") else []) + (elem.get("provenances") or [])
    vistos, salida = set(), []
    for p in ps:
        clave = (p.get("to"), p.get("punto"), p.get("rol_documental"))
        if clave not in vistos:
            vistos.add(clave)
            salida.append(p)
    return salida


def extraer_grafo(ids_paquete):
    ruta = os.path.join(RAIZ, KG_REL)
    with open(ruta, "rb") as fh:
        crudo = fh.read()
    sha = hashlib.sha256(crudo).hexdigest()
    if sha != KG_SHA256:
        raise SystemExit(f"kg.json no es el sellado: {sha}")
    kg = json.loads(crudo.decode("utf-8"))

    nodos = {}
    for clave, tipo, etiqueta, punto in NODOS:
        cands = [n for n in kg["nodes"] if n["type"] == tipo and n.get("label") == etiqueta]
        if len(cands) != 1:
            raise SystemExit(f"nodo {clave}: ({tipo}, {etiqueta!r}) da {len(cands)} nodos en kg.json")
        n = cands[0]
        if n["id"] not in ids_paquete:
            raise SystemExit(f"nodo {clave}: {n['id']} no está entre los del paquete (Paso 2)")
        propios = [p for p in provenances(n) if p.get("rol_documental") == "punto_propio"]
        puntos = [p["punto"] for p in propios]
        if punto is not None:
            if [(p.get("to"), p["punto"]) for p in propios] != [("cla", punto)]:
                raise SystemExit(f"nodo {clave}: procedencia {puntos}, se esperaba solo {punto}")
        nodos[clave] = {"id": n["id"], "type": n["type"], "label": n["label"], "punto": punto,
                        "chunk_id": f"cla::{punto}" if punto else None,
                        "n_procedencias_punto_propio": len(propios),
                        "procedencia_primaria": (n.get("provenance") or {}).get("chunk_id")}
        if punto is None:
            nodos[clave]["incluye_cla_3_7"] = "3.7" in puntos

    aristas = []
    for a, rel, b in ARISTAS:
        hits = [(i, e) for i, e in enumerate(kg["edges"])
                if e["source"] == nodos[a]["id"] and e["relation"] == rel
                and e["target"] == nodos[b]["id"]]
        if len(hits) != 1:
            raise SystemExit(f"arista {a} {rel} {b}: {len(hits)} coincidencias en kg.json")
        i, e = hits[0]
        aristas.append({"origen": a, "relation": rel, "destino": b, "indice": i,
                        "rol_fuente": e.get("rol_fuente"),
                        "chunk_id": (e.get("provenance") or {}).get("chunk_id")})
    return nodos, aristas, {"ruta": KG_REL, "sha256": sha,
                            "n_nodos": len(kg["nodes"]), "n_aristas": len(kg["edges"])}


# --------------------------------------------------------------------------- #
# (c) Búsqueda léxica sobre fragmentos, variante A                             #
# --------------------------------------------------------------------------- #
def extraer_busqueda(paso1):
    ids, textos, shas = bl.cargar_fragmentos()
    orden, rango, aporte, dl, avgdl, terminos, vocab = bl.bm25(ids, textos, PREGUNTA)
    unidad = {}
    for to in bl.TOS:
        with open(bl.E0 / f"chunks_{to}.json", encoding="utf-8") as fh:
            for c in json.load(fh):
                unidad[c["id"]] = c["unidad"]

    def fila(r, i, s):
        return {"rango": r, "chunk_id": ids[i], "unidad": unidad[ids[i]],
                "puntaje": round(s, 4), "puntaje_exacto": repr(s)}

    top10 = [fila(r, i, s) for r, (i, s) in enumerate(orden[:10], 1)]
    idx = {x: i for i, x in enumerate(ids)}
    objetivos = {}
    for cid in OBJETIVOS:
        i = idx[cid]
        objetivos[cid] = {"rango": rango.get(cid), "unidad": unidad[cid],
                          "puntaje": round(sum(aporte[i].values()), 4) if cid in rango else 0.0}

    # Control contra el Paso 1 de U-MED-EJEMPLO-2 (variante A).
    previo = paso1["variantes"]["A"]
    top_prev = [(t["rango"], t["chunk_id"], t["puntaje_exacto"]) for t in previo["top10"]]
    top_aqui = [(t["rango"], t["chunk_id"], t["puntaje_exacto"]) for t in top10]
    rangos_prev = {f["chunk_id"]: f["rango"] for f in previo["fichas"]}
    control = {
        "pregunta_igual": paso1["pregunta"] == PREGUNTA,
        "sha256_insumos_iguales": paso1["sha256_insumos"] == shas,
        "tokens_iguales": previo["tokens_pregunta"] == bl.tok_bm25(PREGUNTA),
        "top10_igual": top_prev == top_aqui,
        "rangos": {cid: {"aqui": objetivos[cid]["rango"], "paquete": rangos_prev.get(cid),
                         "esperado": RANGOS_ESPERADOS[cid]} for cid in OBJETIVOS},
    }
    control["pasa"] = (control["pregunta_igual"] and control["sha256_insumos_iguales"]
                       and control["tokens_iguales"] and control["top10_igual"]
                       and all(v["aqui"] == v["paquete"] == v["esperado"]
                               for v in control["rangos"].values()))
    busqueda = {"variante": "A", "descripcion": "texto completo del fragmento (encabezados "
                "heredados + propio), tokenizador tok_bm25, sin palabras vacías ni raíces",
                "k1": bl.K1, "b": bl.B, "n_fragmentos": len(ids), "sha256_insumos": shas,
                "tokens_pregunta": bl.tok_bm25(PREGUNTA), "n_con_puntaje_positivo": len(orden),
                "avgdl": round(avgdl, 2), "vocab": vocab,
                "top5": top10[:TOPK], "objetivos": objetivos, "control_paso1": control}
    return busqueda


def main():
    paso1, ruta1, sha1 = leer_paquete("umed2_analista_paso1_resultado.json")
    paso2, ruta2, sha2 = leer_paquete("umed2_analista_paso2_resultado.json")
    paso3, ruta3, sha3 = leer_paquete("umed2_analista_paso3_resultado.json")
    if paso2["kg_sha256"] != KG_SHA256:
        raise SystemExit("el Paso 2 del paquete se midió sobre otro kg.json")

    textos, fuente_chunks = extraer_textos()
    nodos, aristas, fuente_kg = extraer_grafo({n["id"] for n in paso2["nodos"]})
    busqueda = extraer_busqueda(paso1)
    if not busqueda["control_paso1"]["pasa"]:
        print(json.dumps(busqueda["control_paso1"], ensure_ascii=False, indent=1))
        raise SystemExit("FRENO: la búsqueda no reproduce el Paso 1 de U-MED-EJEMPLO-2")

    datos = {
        "pregunta": PREGUNTA,
        "fuentes": {
            "kg": fuente_kg,
            "chunks_cla": fuente_chunks,
            "extractor": {"ruta": "docs/tesis/figuras/extraer_datos_ejemplo_prestamo.py",
                          "sha256": sha256_archivo(os.path.abspath(__file__))},
            "modulo_busqueda": {"ruta": "docs/tesis/figuras/busqueda_lexica_fragmentos.py",
                                "sha256": sha256_archivo(bl.__file__),
                                "funciones_copiadas_de": bl.ORIGEN_FUNCIONES,
                                "sha256_origen_funciones": bl.ORIGEN_SHA256},
            "paquete_umed2": {ruta1: sha1, ruta2: sha2, ruta3: sha3},
        },
        "textos": {"cla::5.1.1": textos["cla::5.1.1"], "cla::5.1.1.1": textos["cla::5.1.1.1"],
                   "cla::3.7": textos["cla::3.7"], "frase_resaltada": FRASE_RESALTADA},
        "grafo": {"nodos": nodos, "aristas": aristas},
        "busqueda_fragmentos": busqueda,
        "copiado_del_paquete": {
            "variante_B_paso1": {"origen": ruta1, "sha256_origen": sha1,
                                 "variante_B_entorno": paso1["variante_B_entorno"],
                                 "variantes.B": paso1["variantes"]["B"]},
            "busqueda_nodos_paso3": {"origen": ruta3, "sha256_origen": sha3,
                                     "contenido": paso3},
        },
    }
    with open(SALIDA, "w", encoding="utf-8") as fh:
        fh.write(json.dumps(datos, ensure_ascii=False, indent=1) + "\n")

    b = busqueda
    print(f"JSON: {os.path.relpath(SALIDA, RAIZ)}   sha256 {sha256_archivo(SALIDA)}")
    print(f"kg.json sha256 {fuente_kg['sha256']} (comprobado)")
    print(f"chunks_cla.json sha256 {fuente_chunks['sha256']}")
    for nombre, (ruta, sha) in zip(("Paso 1", "Paso 2", "Paso 3"),
                                   ((ruta1, sha1), (ruta2, sha2), (ruta3, sha3))):
        print(f"paquete {nombre}: {ruta} sha256 {sha} (coincide con el manifiesto)")
    print("\n(a) TEXTOS")
    for cid in ("cla::5.1.1", "cla::5.1.1.1", "cla::3.7"):
        t = textos[cid]
        print(f"  {cid}: {t['texto']!r}  palabras reunidas: {t['palabras_reunidas']}")
    print("\n(b) NODOS")
    for clave, n in nodos.items():
        print(f"  {clave:19s} {n['type']:11s} punto {str(n['punto']):8s} {n['id']}")
        print(f"  {'':19s} etiqueta: {n['label']!r}  procedencias punto_propio: "
              f"{n['n_procedencias_punto_propio']}  primaria: {n['procedencia_primaria']}")
    print("  ARISTAS")
    for a in aristas:
        print(f"  kg['edges'][{a['indice']}] {a['origen']} --{a['relation']}--> {a['destino']}"
              f"  rol_fuente {a['rol_fuente']!r}  procedencia {a['chunk_id']}")
    print(f"\n(c) BÚSQUEDA SOBRE FRAGMENTOS, variante A ({b['n_fragmentos']} fragmentos, "
          f"k1 {b['k1']}, b {b['b']}; {b['n_con_puntaje_positivo']} con puntaje positivo)")
    for t in b["top5"]:
        print(f"  {t['rango']:2d}  {t['chunk_id']:16s} {t['puntaje_exacto']}")
    for cid, o in b["objetivos"].items():
        print(f"  {cid}: puesto {o['rango']}  puntaje {o['puntaje']}")
    print(f"  control contra el Paso 1 del paquete: {json.dumps(b['control_paso1'], ensure_ascii=False)}")
    B = paso1["variantes"]["B"]
    print(f"\n(d) COPIADO DEL PAQUETE — variante B: cla::5.1.1.1 puesto "
          f"{next(f['rango'] for f in B['fichas'] if f['chunk_id'] == 'cla::5.1.1.1')}, cla::3.7 puesto "
          f"{next(f['rango'] for f in B['fichas'] if f['chunk_id'] == 'cla::3.7')}; búsqueda sobre nodos: "
          f"5.1.1.1 mejor puesto {paso3['nodos_de_5_1_1_1']['mejor_rango']}, 3.7 mejor puesto "
          f"{paso3['nodos_de_3_7']['mejor_rango']} ({paso3['total_con_match_agente']} nodos con coincidencia)")


if __name__ == "__main__":
    main()
