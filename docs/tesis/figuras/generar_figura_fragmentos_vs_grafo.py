#!/usr/bin/env python3
"""Figura «la misma pregunta con dos formas de consultar» (Figura 1.2), versión 2.

Dos columnas bajo una pregunta común. Izquierda, «Recuperación por
fragmentos», igual que en la versión 1: los dos puntos del ejemplo del
préstamo como fragmentos —5.1.1.1, recuperado, con la frase que remite al
punto 3.7 resaltada; 3.7, en gris, fuera de lo recuperado— con su puesto en la
búsqueda por palabras (BM25) sobre los fragmentos, y una línea con los otros
cuatro fragmentos del top-5; debajo, la respuesta que se puede redactar solo
con lo recuperado. La búsqueda se recalcula con la misma pregunta y el mismo
índice que la versión 1 (los 1.763 fragmentos de salida_enm01) y el script
informa si los puestos cambian.

Derecha, «Consulta del grafo», sobre el grafo de desarrollo r2b: «1 · Buscar»
con la misma pregunta, por BM25 (la misma función y los mismos parámetros que
la columna de fragmentos) sobre la etiqueta, la descripción y el id de cada
nodo, y el puesto de la Operacion del 5.1.1.1; «2 · Abrir el nodo encontrado»,
la Operacion; «3 · Seguir las aristas»: la remite_a hasta la Definicion del
3.7 y las dos condicion_de que le llegan desde las Condicion del 5.1.1.1.
Debajo, la respuesta con lo que esos nodos dicen. Si la Operacion queda fuera
del top-5 (LIMITE_RECUPERACION, el mismo umbral que la columna de fragmentos),
el script frena.

El lado derecho muestra el camino que el grafo pone al alcance desde el nodo
encontrado; no es la traza de una corrida del agente. El primer nodo del
5.1.1.1 que devuelve la búsqueda no es la Operacion sino la Excepcion, que en
el grafo no tiene más arista que su establecida_en: el script lo comprueba y
lo informa, y la figura no la dibuja.

Versión 1 (28/09/2026; generador en fbe69d4): sobre KG-Reextraído-r1, abría la
Restriccion del monto y seguía referencia y limita; la búsqueda de nodos era
la del índice de texto completo de Neo4j, copiada de un paquete de mediciones.

Reutiliza por importación, sin modificarlos, generar_figura_norma_a_grafo.py
(versión 2: textos, subgrafo y sus candados, colores de tipo, medidas, nodos,
leyenda, controles y exportación) y busqueda_lexica_fragmentos.py (tok_bm25 y
bm25). Fuentes propias, con candado de sha256: el módulo de búsqueda y los
cinco chunks_<to>.json de salida_enm01 (los de la versión 1). Con
--observacion-harness, además, corre buscar_nodos del harness congelado
(harness.py y loader.py, con candado) con la misma pregunta e informa los
puestos; no se dibuja.

Controles, en cada corrida: los de la figura 1.1 (inventario de nodos y aristas
releído del SVG contra el grafo, y geometría con 0 cruces), los puestos de la
búsqueda, y el alto máximo del PNG. Antes de componer corren tres pruebas
negativas (una arista de más, un cruce y un rótulo sobre una caja).

Salidas, byte-reproducibles: figura_fragmentos_vs_grafo.svg, .png (300 dpi,
densidad grabada) y .pdf (SOURCE_DATE_EPOCH=0).

Uso (desde la raíz del repo):
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_fragmentos_vs_grafo.py
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_fragmentos_vs_grafo.py --salida DIR
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_fragmentos_vs_grafo.py --observacion-harness
"""

import sys

sys.dont_write_bytecode = True  # importar los módulos hermanos no deja __pycache__

import argparse  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import generar_figura_norma_a_grafo as base  # noqa: E402

NOMBRE = "figura_fragmentos_vs_grafo"
freno = base.freno

# --------------------------------------------------------------------------- #
# Fuentes propias y candados                                                   #
# --------------------------------------------------------------------------- #
BUSQUEDA = ("docs/tesis/figuras/busqueda_lexica_fragmentos.py",
            "13caa596ad25b9aae3e19ab5e1c4cf30821cf853418320090e2b5ed4cdbcf9d3")
# Los cinco chunks_<to>.json del índice de la versión 1 (salida_enm01); sus
# sha256 son los de ejemplo_prestamo_datos.json, busqueda_fragmentos.
E0_V1 = "data/experiment/reextraccion_v2/e0_chunking/salida_enm01"
# Harness congelado, solo para la observación (--observacion-harness).
HARNESS = ("data/experiment/evaluacion/harness.py",
           "fd267e833866f86850e43130e627b08d78e05523b97484696de0ab0c8c9fba9e")
LOADER = ("data/experiment/evaluacion/loader.py",
          "5aba8b7a0aa46e8d5c4c83b33884b8cae7d0a099884a7d3bc935de4d3097af8b")

# --------------------------------------------------------------------------- #
# Contenido                                                                    #
# --------------------------------------------------------------------------- #
LIMITE_RECUPERACION = 5
FRAGMENTOS = ["cla::5.1.1.1", "cla::3.7"]    # en este orden, de arriba abajo
SUBTITULO_FRAGMENTOS = "Los dos puntos del ejemplo"
ETIQUETA_RECUPERADO = "recuperado · puesto {puesto}"
ETIQUETA_NO_RECUPERADO = "fuera de lo recuperado · puesto {puesto}"
ETIQUETA_RESTO = "resto del top-5: {unidades}"

# Consulta del grafo: el nodo que se abre (por su clave en base.NODOS) y las
# aristas que se siguen; cada una tiene que estar en el subgrafo de la figura 1.1.
NODO_ENCONTRADO = "operacion"
ARISTAS_CONSULTA = [
    ("operacion", "remite_a", "definicion_3_7"),
    ("condicion_monto", "condicion_de", "operacion"),
    ("condicion_repago", "condicion_de", "operacion"),
]
NODOS_ALCANZADOS = ["definicion_3_7", "condicion_monto", "condicion_repago"]
# Primer nodo del 5.1.1.1 en la búsqueda: no se dibuja; el script comprueba que
# es la Excepcion declarada en base.NO_DIBUJADOS.
PRIMERO_NO_DIBUJADO = base.NO_DIBUJADOS[0]
# Texto de cada nodo para la búsqueda: etiqueta, descripción e id.
CAMPOS_NODO = ("label", "descripcion", "id")
TEXTO_BUSQUEDA = ("BM25 sobre las etiquetas y las descripciones de los nodos: "
                  "la Operacion queda en el puesto {puesto}.")

# Respuestas: los únicos textos del ejemplo escritos a mano en la figura.
RESPUESTA_IZQUIERDA = ("Pasan a la cartera comercial si superan dos veces el importe de "
                       "referencia establecido en el punto 3.7 y su repago depende de la "
                       "actividad productiva o comercial del cliente (punto 5.1.1.1).")
RESPUESTA_IZQUIERDA_FALTA = "el importe de referencia (punto 3.7): no recuperado"
RESPUESTA_DERECHA = ("Pasan a la cartera comercial si se cumplen las dos condiciones "
                     "del punto 5.1.1.1:")
# (nodo del que sale la fila, texto, sangría). La fila se escribe «punto ·
# texto», con el punto del nodo leído del grafo y la franja del color de su
# tipo. La fila del 3.7 precisa la del monto y va con sangría debajo de ella.
SANGRIA_FILA = 24
RESPUESTA_DERECHA_FILAS = [
    ("condicion_monto", "superan dos veces el importe de referencia", 0),
    ("definicion_3_7", "el importe de referencia es el nivel máximo de ventas anuales", SANGRIA_FILA),
    ("condicion_repago", "su repago está vinculado a la actividad productiva o comercial", 0),
]

# --------------------------------------------------------------------------- #
# Geometría (la de la versión 1, salvo la columna de la consulta)              #
# --------------------------------------------------------------------------- #
W = base.W
MARGEN = base.MARGEN
MARGEN_V = 8
ANCHO_TOTAL = base.ANCHO_PANEL
SEPARACION = 20
ANCHO_COL = (ANCHO_TOTAL - SEPARACION) / 2.0     # 396
PAD = 14
PAD_V = 12

FS_TITULO = base.FS_TITULO_PANEL         # 17
FS_TEXTO = base.FS_TEXTO                 # 17
FS_ENCABEZADO = 17
FS_NODO = base.FS_NODO + 2               # 17
FS_ROTULO = base.FS_ROTULO + 2           # 15
FS_LEYENDA = base.FS_LEYENDA + 2         # 15
INTERLINEA = base.INTERLINEA
PASO_NODO = 19
PASO_ROTULO = 17

ANCHO_IMPRESO_CM = 12.75
ALTO_MAX_PNG_PX = 1850                   # el de la versión 1
PT_MIN_TEXTO = 7.0

GRIS_TEXTO_APAGADO = "#9a9a9a"
GRIS_BORDE_APAGADO = "#bdbdbd"
FONDO_APAGADO = "#f1f1f1"
COLOR_FLUJO = "#555"

ancho, envolver, esc, f = base.ancho, base.envolver, base.esc, base.f
ancho_negrita = base.ancho_negrita


def puntos_impresos(px):
    return base.puntos_impresos(px, ANCHO_IMPRESO_CM, W)


def miles(n):
    """Entero con punto de miles: 1523 -> «1.523»."""
    return f"{n:,}".replace(",", ".")


# --------------------------------------------------------------------------- #
# Búsquedas                                                                    #
# --------------------------------------------------------------------------- #
def importar_busqueda():
    base.leer_con_candado(*BUSQUEDA)
    import busqueda_lexica_fragmentos as bl
    if os.path.abspath(bl.__file__) != os.path.join(base.RAIZ, BUSQUEDA[0]):
        freno(f"se importó otro módulo de búsqueda: {bl.__file__}")
    return bl


def busqueda_fragmentos(bl, cont):
    """BM25 sobre los fragmentos de la versión 1, recalculada; los puestos se
    comparan con los de la versión 1."""
    v1 = cont["v1"]["busqueda_fragmentos"]
    for nombre, sha in sorted(v1["sha256_insumos"].items()):
        base.leer_con_candado(f"{E0_V1}/{nombre}", sha)
    ids, textos, shas = bl.cargar_fragmentos()
    if shas != v1["sha256_insumos"]:
        freno("los fragmentos leídos no son los de la versión 1")
    orden, rango, *_ = bl.bm25(ids, textos, cont["pregunta"])
    top = [{"chunk_id": ids[i], "puntaje": s} for i, s in orden[:LIMITE_RECUPERACION]]
    unidad = {c: c.split("::", 1)[1] for c in ids}
    v1_top = [t["chunk_id"] for t in v1["top5"]]
    v1_rango = {c: v1["objetivos"][c]["rango"] for c in FRAGMENTOS}
    cambian = ([t["chunk_id"] for t in top] != v1_top) or any(rango.get(c) != v1_rango[c] for c in FRAGMENTOS)
    return {"n": len(ids), "top": top, "rango": {c: rango.get(c) for c in FRAGMENTOS}, "unidad": unidad,
            "cambian": cambian, "v1_top": v1_top, "v1_rango": v1_rango,
            "puntajes": {ids[i]: s for i, s in orden}}


def texto_nodo(n):
    pr = n.get("properties") or {}
    partes = {"label": n.get("label") or "", "descripcion": pr.get("descripcion") or pr.get("description") or "",
              "id": n["id"]}
    return "\n".join(partes[c] for c in CAMPOS_NODO)


def busqueda_nodos(bl, cont, sub):
    """BM25 (la función de la columna de fragmentos) sobre etiqueta,
    descripción e id de los nodos del grafo de desarrollo."""
    kg = json.loads(base.leer_con_candado(*base.GRAFO).decode("utf-8"))
    con_ambas = [n["id"] for n in kg["nodes"]
                 if (n.get("properties") or {}).get("descripcion") and (n.get("properties") or {}).get("description")]
    if con_ambas:
        freno(f"{len(con_ambas)} nodos con descripcion y description: la búsqueda tomaría una sola")
    ids = sorted(n["id"] for n in kg["nodes"])
    por_id = {n["id"]: n for n in kg["nodes"]}
    orden, rango, *_ = bl.bm25(ids, [texto_nodo(por_id[i]) for i in ids], cont["pregunta"])
    de_la_unidad = sorted(((rango.get(i), por_id[i]["type"], por_id[i]["label"], len(base.chunks_de(por_id[i])))
                           for i in ids if base.UNIDAD in base.chunks_de(por_id[i])),
                          key=lambda t: (t[0] is None, t[0] or 0))
    primero = de_la_unidad[0]
    if (primero[1], primero[2]) != PRIMERO_NO_DIBUJADO:
        freno(f"el primer nodo de {base.UNIDAD} en la búsqueda no es el declarado: {primero}")
    if sub["no_dibujados"][PRIMERO_NO_DIBUJADO] != [("sale", "establecida_en", "TextoOrdenado")]:
        freno("la Excepcion del 5.1.1.1 tiene otras aristas que establecida_en")
    puesto = {k: rango.get(n["id"]) for k, n in sub["nodos"].items()}
    if puesto[NODO_ENCONTRADO] is None or puesto[NODO_ENCONTRADO] > LIMITE_RECUPERACION:
        freno(f"la {sub['nodos'][NODO_ENCONTRADO]['type']} queda en el puesto {puesto[NODO_ENCONTRADO]}, "
              f"fuera del top-{LIMITE_RECUPERACION}")
    top = [(r, por_id[ids[i]]["type"], por_id[ids[i]]["label"], round(s, 4))
           for r, (i, s) in enumerate(orden[:10], 1)]
    return {"n": len(ids), "con_puntaje": len(orden), "puesto": puesto, "de_la_unidad": de_la_unidad,
            "top10": top}


def observacion_harness(cont, sub):
    """buscar_nodos del harness congelado, con la misma pregunta, sobre el grafo
    de desarrollo: puestos de los nodos dibujados y de la Excepcion. No se
    dibuja."""
    base.leer_con_candado(*HARNESS)
    base.leer_con_candado(*LOADER)
    eval_dir = os.path.join(base.RAIZ, os.path.dirname(HARNESS[0]))
    sys.path.insert(0, eval_dir)
    import harness
    import loader
    for mod, par in ((harness, HARNESS), (loader, LOADER)):
        if os.path.abspath(mod.__file__) != os.path.join(base.RAIZ, par[0]):
            freno(f"se importó otro {par[0]}: {mod.__file__}")
    base.leer_con_candado(*base.GRAFO)
    kg = loader.load_graph_from_path(os.path.join(base.RAIZ, base.GRAFO[0]))
    idx = harness.GraphIndex(kg)
    q = set(harness._tokens(cont["pregunta"]))
    sc = sorted(((len(q & idx._node_tokens[n.id]), len(n.label or ""), n.id) for n in kg.nodes
                 if q & idx._node_tokens[n.id]), key=lambda t: (-t[0], t[1], t[2]))
    rango = {t[2]: (r, t[0]) for r, t in enumerate(sc, 1)}
    res = idx.buscar_nodos(cont["pregunta"])
    if [r["id"] for r in res["resultados"]] != [t[2] for t in sc[:10]] or res["total_con_match"] != len(sc):
        freno("el orden recalculado no es el de harness.GraphIndex.buscar_nodos")
    raw = {n["id"]: n for n in json.loads(base.leer_con_candado(*base.GRAFO).decode("utf-8"))["nodes"]}
    excep = [i for i, n in raw.items() if (n["type"], n["label"]) == PRIMERO_NO_DIBUJADO]
    filas = [(k, n["type"], n["label"], rango.get(n["id"])) for k, n in sub["nodos"].items()]
    filas.append(("excepcion", PRIMERO_NO_DIBUJADO[0], PRIMERO_NO_DIBUJADO[1], rango.get(excep[0])))
    return {"tokens": sorted(q), "total_con_match": len(sc), "filas": filas,
            "limite_por_omision": len(res["resultados"]),
            "resultados": [(r["type"], r["label"], r["tokens_matcheados"]) for r in res["resultados"]]}


# --------------------------------------------------------------------------- #
# Piezas                                                                       #
# --------------------------------------------------------------------------- #
def panel(x, y, w, h):
    return (f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" '
            f'fill="{base.FONDO_PANEL}" stroke="{base.BORDE_PANEL}" rx="5"/>')


def flecha_flujo(x, y1, y2):
    return (f'<path d="M{f(x)},{f(y1)} L{f(x)},{f(y2)}" fill="none" stroke="{COLOR_FLUJO}" '
            f'stroke-width="1.5" marker-end="url(#arF)"/>')


LINEA_MARCA = 24
SALTO_TEXTO = 28
PIE_FRAGMENTO = 12
GAP_FRAGMENTOS = 12
ALTO_SUBTITULO = 22
ALTO_RESTO = 30


def bloque_fragmento(cont, cid, recuperado):
    t = cont["textos"][cid]
    b = {"texto": t["texto"], "unidad": t["unidad"],
         "resaltar": cont["frase_resaltada"] if recuperado else None}
    if b["resaltar"] and b["resaltar"] not in b["texto"]:
        freno(f"la frase resaltada no está en el texto de {cid}")
    return b


def lineas_fragmento(b, w):
    return base.envolver_estilos(b["texto"], base.estilo_de(b), FS_TEXTO, w - 2 * PAD)


def alto_fragmento(b, w):
    return LINEA_MARCA + SALTO_TEXTO + (len(lineas_fragmento(b, w)) - 1) * INTERLINEA + PIE_FRAGMENTO


def dibujar_fragmento(b, puesto, recuperado, x, y, w):
    partes = []
    alto = alto_fragmento(b, w)
    if recuperado:
        partes.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(alto)}" '
                      f'fill="white" stroke="#333" stroke-width="1.8" rx="4"/>')
        partes.append(f'<text x="{f(x + PAD)}" y="{f(y + LINEA_MARCA)}" font-size="{FS_ROTULO}" '
                      f'font-weight="bold" fill="#333">{esc(ETIQUETA_RECUPERADO.format(puesto=miles(puesto)))}</text>')
    else:
        partes.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(alto)}" '
                      f'fill="{FONDO_APAGADO}" stroke="{GRIS_BORDE_APAGADO}" stroke-width="1.0" '
                      f'stroke-dasharray="5,4" rx="4"/>')
        partes.append(f'<text x="{f(x + PAD)}" y="{f(y + LINEA_MARCA)}" font-size="{FS_ROTULO}" '
                      f'font-style="italic" fill="{base.GRIS_ROTULO}">'
                      f'{esc(ETIQUETA_NO_RECUPERADO.format(puesto=miles(puesto)))}</text>')
    base.texto_estilado(partes, base.estilo_de(b), lineas_fragmento(b, w), x + PAD,
                        y + LINEA_MARCA + SALTO_TEXTO, FS_TEXTO, INTERLINEA,
                        "#1f1f1f" if recuperado else GRIS_TEXTO_APAGADO, base.ACENTO_TEXTO)
    return partes, alto


def alto_columna_fragmentos(bloques):
    w = ANCHO_COL - 2 * PAD
    total = PAD_V + ALTO_SUBTITULO
    total += sum(alto_fragmento(b, w) for b, _, _ in bloques)
    total += GAP_FRAGMENTOS * (len(bloques) - 1)
    return total + ALTO_RESTO + PAD_V


def dibujar_columna_fragmentos(bloques, resto, x0, y0, alto):
    partes = [panel(x0, y0, ANCHO_COL, alto)]
    partes.append(f'<text x="{f(x0 + PAD)}" y="{f(y0 + PAD_V + 12)}" font-size="{FS_ROTULO}" '
                  f'font-weight="bold" fill="#444">{esc(SUBTITULO_FRAGMENTOS)}</text>')
    y = y0 + PAD_V + ALTO_SUBTITULO
    for b, puesto, recuperado in bloques:
        piezas, h = dibujar_fragmento(b, puesto, recuperado, x0 + PAD, y, ANCHO_COL - 2 * PAD)
        partes += piezas
        y += h + GAP_FRAGMENTOS
    linea = ETIQUETA_RESTO.format(unidades=" · ".join(resto))
    if ancho(linea, FS_ROTULO) > ANCHO_COL - 2 * PAD:
        freno("la línea del resto del top-5 no entra en la columna")
    partes.append(f'<text x="{f(x0 + PAD)}" y="{f(y - GAP_FRAGMENTOS + ALTO_RESTO - 6)}" '
                  f'font-size="{FS_ROTULO}" fill="#444">{esc(linea)}</text>')
    return partes


# Disposición de la columna de la consulta (coordenadas relativas a su
# esquina). Las alturas salen del número de líneas; los anchos y las
# separaciones son fijos. Las aristas que tocan al nodo abierto bajan por
# troncos a la izquierda (TRONCOS, uno por nodo alcanzado: el de más arriba usa
# el tronco de más adentro, así ninguna arista cruza a otra) y entran o salen
# por el costado izquierdo del nodo alcanzado.
X_PILDORA, ANCHO_PILDORA = 14, 368
X_R, ANCHO_R = 14, 320
X_NODO, ANCHO_NODO = 136, 246
TRONCOS = {"definicion_3_7": 52, "condicion_monto": 38, "condicion_repago": 24}
X_FLECHA_BUSQUEDA = 300
SALTO_PASO = 18
BAJO_PASO = 8
GAP_NODOS = 10


def alto_nodo(nodo, w):
    return len(base.lineas_nodo(nodo, w - 22, FS_NODO)) * PASO_NODO + 8


def disposicion_grafo(cont, sub, busq):
    nodos = sub["nodos"]
    d = {"pasos": {}, "cajas": {}}
    y = PAD_V + 13
    d["pasos"][1] = (PAD + 4, y)
    lineas = envolver(cont["pregunta"], FS_ROTULO, ANCHO_PILDORA - 44)
    y += BAJO_PASO
    d["pildora"] = {"y": y, "h": len(lineas) * PASO_ROTULO + 12, "lineas": lineas}
    y += d["pildora"]["h"] + 8
    resultado = envolver(TEXTO_BUSQUEDA.format(puesto=busq["puesto"][NODO_ENCONTRADO]), FS_ROTULO,
                         ANCHO_PILDORA)
    d["resultado"] = {"y": y + FS_ROTULO, "lineas": resultado}
    y += len(resultado) * PASO_ROTULO + 4
    y += SALTO_PASO
    d["pasos"][2] = (PAD + 4, y)
    y += BAJO_PASO
    h = alto_nodo(nodos[NODO_ENCONTRADO], ANCHO_R)
    d["cajas"][NODO_ENCONTRADO] = {"cx": X_R + ANCHO_R / 2.0, "cy": y + h / 2.0, "w": ANCHO_R, "h": h}
    y += h + SALTO_PASO
    d["pasos"][3] = (X_NODO, y)
    y += BAJO_PASO
    for k, clave in enumerate(NODOS_ALCANZADOS):
        if k:
            y += GAP_NODOS
        h = alto_nodo(nodos[clave], ANCHO_NODO)
        d["cajas"][clave] = {"cx": X_NODO + ANCHO_NODO / 2.0, "cy": y + h / 2.0, "w": ANCHO_NODO, "h": h}
        y += h
    d["alto"] = y + PAD_V
    return d


def dibujar_columna_grafo(cont, sub, colores, disp, x0, y0, alto, aristas):
    nodos = sub["nodos"]
    partes = [panel(x0, y0, ANCHO_COL, alto)]
    cajas = disp["cajas"]

    def paso(n, texto):
        x, y = disp["pasos"][n]
        return (f'<text x="{f(x0 + x)}" y="{f(y0 + y)}" font-size="{FS_ROTULO}" '
                f'font-weight="bold" fill="#444">{esc(texto)}</text>')

    partes.append(paso(1, "1 · Buscar"))
    p = disp["pildora"]
    partes.append(f'<rect x="{f(x0 + X_PILDORA)}" y="{f(y0 + p["y"])}" width="{f(ANCHO_PILDORA)}" '
                  f'height="{f(p["h"])}" fill="white" stroke="#999" stroke-width="1.2" rx="20"/>')
    yl = y0 + p["y"] + p["h"] / 2.0 - (len(p["lineas"]) - 1) * PASO_ROTULO / 2.0 + 5
    for linea, _ in p["lineas"]:
        partes.append(f'<text x="{f(x0 + X_PILDORA + ANCHO_PILDORA / 2.0)}" y="{f(yl)}" text-anchor="middle" '
                      f'font-size="{FS_ROTULO}" font-style="italic" fill="#333">{esc(linea)}</text>')
        yl += PASO_ROTULO
    r = disp["resultado"]
    yl = y0 + r["y"]
    for linea, _ in r["lineas"]:
        partes.append(f'<text x="{f(x0 + X_PILDORA)}" y="{f(yl)}" font-size="{FS_ROTULO}" fill="#444">'
                      f'{esc(linea)}</text>')
        yl += PASO_ROTULO

    c = cajas[NODO_ENCONTRADO]
    partes.append(paso(2, "2 · Abrir el nodo encontrado"))
    partes.append(flecha_flujo(x0 + X_FLECHA_BUSQUEDA, yl - PASO_ROTULO + 7, y0 + c["cy"] - c["h"] / 2.0 - 3))

    partes.append(paso(3, "3 · Seguir las aristas"))
    y_base = y0 + c["cy"] + c["h"] / 2.0
    rotulos = []
    for k, (o, rel, d) in enumerate(aristas):
        resaltada = rel == base.RELACION_RESALTADA
        if o == NODO_ENCONTRADO:
            otro, sale = d, True
        elif d == NODO_ENCONTRADO:
            otro, sale = o, False
        else:
            freno(f"arista que no toca al nodo abierto: {o} {rel} {d}")
        cb = cajas[otro]
        tx = x0 + TRONCOS[otro]
        x_borde = x0 + cb["cx"] - cb["w"] / 2.0
        cy = y0 + cb["cy"]
        pts = [(tx, y_base), (tx, cy), (x_borde, cy)]
        if not sale:
            pts = pts[::-1]
        mx = (tx + x_borde) / 2.0
        at = ancho_negrita(rel, FS_ROTULO) if resaltada else ancho(rel, FS_ROTULO)
        if at + 8 > x_borde - tx:
            freno(f"el rótulo {rel!r} no entra en el tramo horizontal")
        d_attr = "M" + " L".join(f"{f(x)},{f(y)}" for x, y in pts)
        color = base.ACENTO if resaltada else base.GRIS_ARISTA
        grosor = "2.6" if resaltada else "1.5"
        dash = "" if resaltada else ' stroke-dasharray="4,4"'
        marca = "arA" if resaltada else "arG"
        partes.append(f'<path d="{d_attr}" fill="none" stroke="{color}" stroke-width="{grosor}"{dash} '
                      f'stroke-linejoin="round" marker-end="url(#{marca})" data-arista="{k}"/>')
        rotulos.append((k, mx, cy - 12, rel, resaltada))
    for k, mx, my, texto, resaltada in rotulos:
        at = ancho_negrita(texto, FS_ROTULO) if resaltada else ancho(texto, FS_ROTULO)
        partes.append(f'<rect x="{f(mx - at / 2 - 1)}" y="{f(my - FS_ROTULO + 1)}" width="{f(at + 2)}" '
                      f'height="{f(FS_ROTULO + 4)}" fill="{base.FONDO_PANEL}" opacity="0.94" rx="2"/>')
        partes.append(f'<text x="{f(mx)}" y="{f(my + 2)}" text-anchor="middle" font-size="{FS_ROTULO}" '
                      f'font-weight="{"bold" if resaltada else "normal"}" '
                      f'fill="{base.ACENTO_TEXTO if resaltada else base.GRIS_ROTULO}" data-rotulo="{k}">'
                      f'{esc(texto)}</text>')
    for clave, cj in cajas.items():
        lineas = base.lineas_nodo(nodos[clave], cj["w"] - 22, FS_NODO)
        base.caja_nodo(partes, nodos[clave], colores, x0 + cj["cx"], y0 + cj["cy"], cj["w"], cj["h"],
                       lineas, FS_NODO, PASO_NODO, clave)
    return partes


# --------------------------------------------------------------------------- #
# Respuestas (como en la versión 1)                                            #
# --------------------------------------------------------------------------- #
ALTO_FILA = 26
GAP_FILA = 4
X_TEXTO_FILA = 14
X_TEXTO_FALTA = 34


def filas_derecha(sub):
    filas = []
    for clave, texto, sangria in RESPUESTA_DERECHA_FILAS:
        n = sub["nodos"][clave]
        filas.append((f"{n['punto']} · {texto}", len(n["punto"]), n["type"], sangria))
    return filas


def lineas_fila(texto, n_negrita, x_texto, sangria=0):
    estilo = ["N"] * n_negrita + [""] * (len(texto) - n_negrita)
    return base.envolver_estilos(texto, estilo, FS_TEXTO, ANCHO_COL - 2 * PAD - sangria - x_texto - 6), estilo


def alto_filas(filas, x_texto):
    return sum(ALTO_FILA + (len(lineas_fila(t, n, x_texto, sg)[0]) - 1) * INTERLINEA + GAP_FILA
               for t, n, _, sg in filas) - GAP_FILA


def alto_respuesta(entrada, filas, x_texto):
    n = len(envolver(entrada, FS_TEXTO, ANCHO_COL - 2 * PAD))
    return PAD_V + FS_ENCABEZADO + 6 + n * INTERLINEA + 6 + alto_filas(filas, x_texto) + PAD_V


def dibujar_respuesta(titulo, entrada, filas, completas, colores, x0, y0, alto):
    partes = [panel(x0, y0, ANCHO_COL, alto)]
    partes.append(f'<text x="{f(x0 + PAD)}" y="{f(y0 + PAD_V + FS_ENCABEZADO - 2)}" '
                  f'font-size="{FS_ENCABEZADO}" font-weight="bold" fill="#333">{esc(titulo)}</text>')
    yl = y0 + PAD_V + FS_ENCABEZADO + 6 + FS_TEXTO
    lineas = envolver(entrada, FS_TEXTO, ANCHO_COL - 2 * PAD)
    for linea, _ in lineas:
        partes.append(f'<text x="{f(x0 + PAD)}" y="{f(yl)}" font-size="{FS_TEXTO}" fill="#1f1f1f">{esc(linea)}</text>')
        yl += INTERLINEA
    y = y0 + PAD_V + FS_ENCABEZADO + 6 + len(lineas) * INTERLINEA + 6
    x_texto = X_TEXTO_FILA if completas else X_TEXTO_FALTA
    for texto, n_negrita, tipo, sangria in filas:
        x, w = x0 + PAD + sangria, ANCHO_COL - 2 * PAD - sangria
        lf, estilo = lineas_fila(texto, n_negrita, x_texto, sangria)
        h = ALTO_FILA + (len(lf) - 1) * INTERLINEA
        y_txt = y + ALTO_FILA / 2.0 + 6
        if completas:
            partes.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" fill="white" '
                          f'stroke="#d8d8d8" rx="4"/>')
            partes.append(f'<rect x="{f(x)}" y="{f(y)}" width="6" height="{f(h)}" '
                          f'fill="{colores[tipo]["borde"]}" rx="2"/>')
            base.texto_estilado(partes, estilo, lf, x + x_texto, y_txt, FS_TEXTO, INTERLINEA, "#1f1f1f",
                                base.ACENTO_TEXTO)
        else:
            cy = y + ALTO_FILA / 2.0
            partes.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" fill="none" '
                          f'stroke="{GRIS_BORDE_APAGADO}" stroke-width="1.2" stroke-dasharray="5,4" rx="4"/>')
            for dx1, dy1, dx2, dy2 in [(-5, -5, 5, 5), (-5, 5, 5, -5)]:
                partes.append(f'<path d="M{f(x + 19 + dx1)},{f(cy + dy1)} L{f(x + 19 + dx2)},{f(cy + dy2)}" '
                              f'stroke="{base.GRIS_ROTULO}" stroke-width="2"/>')
            for linea, _ in lf:
                partes.append(f'<text x="{f(x + x_texto)}" y="{f(y_txt)}" font-size="{FS_TEXTO}" '
                              f'font-style="italic" fill="{base.GRIS_ROTULO}">{esc(linea)}</text>')
                y_txt += INTERLINEA
        y += h + GAP_FILA
    return partes


# --------------------------------------------------------------------------- #
# Composición                                                                  #
# --------------------------------------------------------------------------- #
PRUEBAS_NEGATIVAS = (("arista_de_mas", "inventario", "arista de la figura que no está en el grafo"),
                     ("cruce", "geometria", "cruce(s) entre trazos"),
                     ("rotulo_sobre_caja", "geometria", "texto sobre la caja"))


def componer(cont, sub, colores, frag, busq, perturbacion=None):
    bloques = []
    for cid in FRAGMENTOS:
        puesto = frag["rango"][cid]
        recuperado = puesto is not None and puesto <= LIMITE_RECUPERACION
        bloques.append((bloque_fragmento(cont, cid, recuperado), puesto, recuperado))
    resto = [frag["unidad"][t["chunk_id"]] for t in frag["top"] if t["chunk_id"] not in FRAGMENTOS]
    if len(resto) != LIMITE_RECUPERACION - sum(1 for _, _, r in bloques if r):
        freno("el resto del top-5 no suma cinco con los fragmentos recuperados")
    aristas = list(ARISTAS_CONSULTA)
    if perturbacion == "arista_de_mas":
        aristas.append(("operacion", "condicion_de", "condicion_repago"))
    filas_izq = [(RESPUESTA_IZQUIERDA_FALTA, 0, None, 0)]
    filas_der = filas_derecha(sub)

    ancho_pregunta = ANCHO_TOTAL - 2 * PAD
    pregunta = cont["pregunta"]
    lineas_pregunta = base.envolver_estilos(pregunta, ["N"] * len(pregunta), FS_TEXTO, ancho_pregunta)
    alto_pregunta = 8 + FS_ROTULO + 3 + len(lineas_pregunta) * INTERLINEA + 4
    y_pregunta = MARGEN_V
    y_titulos = y_pregunta + alto_pregunta + 34
    y_cols = y_titulos + 9
    disp = disposicion_grafo(cont, sub, busq)
    alto_cols = max(alto_columna_fragmentos(bloques), disp["alto"])
    y_resp = y_cols + alto_cols + 18
    alto_resp = max(alto_respuesta(RESPUESTA_IZQUIERDA, filas_izq, X_TEXTO_FALTA),
                    alto_respuesta(RESPUESTA_DERECHA, filas_der, X_TEXTO_FILA))
    y_leyenda = y_resp + alto_resp + 8
    alto_leyenda = 46
    alto_total = y_leyenda + alto_leyenda + MARGEN_V
    x_izq = MARGEN
    x_der = MARGEN + ANCHO_COL + SEPARACION

    out = [base.cabecera_svg(W, alto_total, ANCHO_IMPRESO_CM),
           f'<rect width="{W}" height="{f(alto_total)}" fill="white"/>',
           base.marcadores((("arF", COLOR_FLUJO),))]
    out.append(f'<rect x="{f(MARGEN)}" y="{f(y_pregunta)}" width="{f(ANCHO_TOTAL)}" '
               f'height="{f(alto_pregunta)}" fill="white" stroke="#333" stroke-width="1.4" rx="5"/>')
    out.append(f'<text x="{f(W / 2.0)}" y="{f(y_pregunta + 8 + FS_ROTULO - 2)}" text-anchor="middle" '
               f'font-size="{FS_ROTULO}" font-weight="bold" fill="{base.GRIS_ROTULO}">La misma pregunta</text>')
    yl = y_pregunta + 8 + FS_ROTULO + 3 + FS_TEXTO
    for linea, _ in lineas_pregunta:
        out.append(f'<text x="{f(W / 2.0)}" y="{f(yl)}" text-anchor="middle" font-size="{FS_TEXTO}" '
                   f'font-weight="bold" fill="#1f1f1f">{esc(linea)}</text>')
        yl += INTERLINEA
    for x_col, titulo in [(x_izq, "Recuperación por fragmentos"), (x_der, "Consulta del grafo")]:
        out.append(flecha_flujo(x_col + ANCHO_COL / 2.0, y_pregunta + alto_pregunta, y_titulos - FS_TITULO - 3))
        out.append(f'<text x="{f(x_col + ANCHO_COL / 2.0)}" y="{f(y_titulos)}" text-anchor="middle" '
                   f'font-size="{FS_TITULO}" font-weight="bold">{esc(titulo)}</text>')
    out += dibujar_columna_fragmentos(bloques, resto, x_izq, y_cols, alto_cols)
    col = dibujar_columna_grafo(cont, sub, colores, disp, x_der, y_cols, alto_cols, aristas)
    if perturbacion == "cruce":
        c1, c2 = disp["cajas"]["definicion_3_7"], disp["cajas"]["condicion_repago"]
        x = x_der + TRONCOS["condicion_repago"] - 10
        col.append(f'<path d="M{f(x_der + X_NODO)},{f(y_cols + c1["cy"])} L{f(x)},{f(y_cols + c1["cy"])} '
                   f'L{f(x)},{f(y_cols + c2["cy"] + 10)} L{f(x_der + X_NODO)},{f(y_cols + c2["cy"] + 10)}" '
                   f'fill="none" stroke="{base.GRIS_ARISTA}" marker-end="url(#arG)"/>')
    if perturbacion == "rotulo_sobre_caja":
        c = disp["cajas"]["condicion_monto"]
        col.append(f'<text x="{f(x_der + c["cx"])}" y="{f(y_cols + c["cy"] - c["h"] / 2 + 3)}" '
                   f'text-anchor="middle" font-size="{FS_ROTULO}" fill="{base.GRIS_ROTULO}">remite_a</text>')
    out += col
    for x_col in (x_izq, x_der):
        out.append(flecha_flujo(x_col + ANCHO_COL / 2.0, y_cols + alto_cols, y_resp - 3))
    out += dibujar_respuesta("Respuesta con lo recuperado", RESPUESTA_IZQUIERDA, filas_izq, False, colores,
                             x_izq, y_resp, alto_resp)
    out += dibujar_respuesta("Respuesta con lo consultado", RESPUESTA_DERECHA, filas_der, True, colores,
                             x_der, y_resp, alto_resp)
    out += base.dibujar_leyenda(y_leyenda, alto_leyenda, fs=FS_LEYENDA)
    out.append("</svg>")
    return "\n".join(out) + "\n", {"alto": alto_total, "bloques": bloques, "resto": resto, "disp": disp,
                                   "filas_der": filas_der, "alto_cols": (alto_columna_fragmentos(bloques),
                                                                         disp["alto"])}


def controlar(cont, sub, colores, frag, busq, perturbacion=None):
    svg, geo = componer(cont, sub, colores, frag, busq, perturbacion)
    c = {}
    nodos_dib = {k: sub["nodos"][k] for k in [NODO_ENCONTRADO] + NODOS_ALCANZADOS}
    c["inventario"], nodos_svg, aristas_svg = base.controlar_inventario(svg, nodos_dib, ARISTAS_CONSULTA)
    c["geometria"], info = base.controlar_geometria(svg, ANCHO_IMPRESO_CM, W)
    if puntos_impresos(FS_TEXTO) < PT_MIN_TEXTO:
        c["geometria"].append(f"el texto corrido imprime a {puntos_impresos(FS_TEXTO):.2f} pt")
    alto_png = round(round(ANCHO_IMPRESO_CM / 2.54 * base.DPI) * geo["alto"] / W)
    c["alto"] = [] if alto_png <= ALTO_MAX_PNG_PX else [f"el PNG mediría {alto_png} px de alto, máximo {ALTO_MAX_PNG_PX}"]
    return svg, geo, c, info, nodos_svg, aristas_svg


def pruebas_negativas(*a):
    vivas = []
    for caso, control, patron in PRUEBAS_NEGATIVAS:
        _, _, c, _, _, _ = controlar(*a, perturbacion=caso)
        propia = [x for x in c[control] if patron in x]
        if not propia:
            freno(f"la prueba negativa {caso} no hizo fallar el control de {control} con «{patron}»")
        vivas.append((caso, control, propia[0], sorted(k for k, v in c.items() if v and k != control)))
    return vivas


def argumentos():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--salida", default=AQUI,
                    help="directorio donde escribir el SVG, el PNG y el PDF (por omisión, el del script)")
    ap.add_argument("--perturbar", choices=[c for c, _, _ in PRUEBAS_NEGATIVAS], default=None,
                    help="compone la figura con ese defecto: los controles fallan y no se escribe nada")
    ap.add_argument("--observacion-harness", action="store_true",
                    help="informa además los puestos de buscar_nodos del harness congelado (no se dibuja)")
    return ap.parse_args()


def main():
    args = argumentos()
    cont = base.cargar_textos()
    sub = base.cargar_subgrafo(base.GRAFO)
    colores = base.leer_colores_tipo()
    en_sub = {(a["origen"], a["relation"], a["destino"]) for a in sub["aristas"]}
    for arista in ARISTAS_CONSULTA:
        if arista not in en_sub:
            freno(f"arista de la consulta ausente del subgrafo: {arista}")
    bl = importar_busqueda()
    frag = busqueda_fragmentos(bl, cont)
    busq = busqueda_nodos(bl, cont, sub)

    print("FUENTES (sha256 comprobado):")
    for nombre, par in (("grafo", base.GRAFO), ("chunks_cla", base.CHUNKS_CLA), ("datos v1", base.DATOS_V1),
                        ("extractor v1", base.EXTRACTOR_V1), ("estilo", base.ESTILO), ("búsqueda", BUSQUEDA)):
        print(f"  {nombre:13s} {par[0]}   {par[1]}")
    for nombre, sha in sorted(cont["v1"]["busqueda_fragmentos"]["sha256_insumos"].items()):
        print(f"  índice v1     {E0_V1}/{nombre}   {sha}")
    print(f"PREGUNTA: {cont['pregunta']}")
    print(f"BÚSQUEDA EN LOS FRAGMENTOS (BM25, {frag['n']} fragmentos de salida_enm01, recalculada):")
    for r, t in enumerate(frag["top"], 1):
        print(f"  {r}. {t['chunk_id']:14s} {t['puntaje']:.4f}")
    for cid in FRAGMENTOS:
        print(f"  {cid}: puesto {frag['rango'][cid]} (versión 1: {frag['v1_rango'][cid]}), "
              f"puntaje {frag['puntajes'][cid]:.4f}")
    print(f"  ¿cambian los puestos respecto de la versión 1? {'SÍ' if frag['cambian'] else 'no'} "
          f"(top-5 v1 {frag['v1_top']})")
    print(f"BÚSQUEDA EN LOS NODOS (BM25 sobre {' + '.join(CAMPOS_NODO)}, {busq['n']} nodos del grafo de "
          f"desarrollo, {busq['con_puntaje']} con puntaje):")
    for fila in busq["top10"]:
        print(f"  {fila}")
    print(f"  nodos de {base.UNIDAD} (puesto, tipo, etiqueta, procedencias):")
    for fila in busq["de_la_unidad"]:
        print(f"    {fila}")
    for k in [NODO_ENCONTRADO] + NODOS_ALCANZADOS:
        print(f"  {k:17s} puesto {busq['puesto'][k]}")
    print(f"  primer nodo de {base.UNIDAD}: {busq['de_la_unidad'][0][1]} (puesto {busq['de_la_unidad'][0][0]}), "
          f"aristas {sub['no_dibujados'][PRIMERO_NO_DIBUJADO]}; no se dibuja")
    if args.observacion_harness:
        o = observacion_harness(cont, sub)
        print(f"OBSERVACIÓN (no se dibuja): buscar_nodos del harness congelado ({HARNESS[0]}, sha256 "
              f"{HARNESS[1]}), tokens {o['tokens']}; {o['total_con_match']} nodos con coincidencia")
        for k, tipo, etiqueta, r in o["filas"]:
            print(f"  {k:17s} {tipo:10s} {etiqueta!r}: puesto y tokens en común {r}")
        print(f"  con el límite por omisión devuelve {o['limite_por_omision']}:")
        for fila in o["resultados"]:
            print(f"    {fila}")

    a = (cont, sub, colores, frag, busq)
    vivas = pruebas_negativas(*a)
    print(f"PRUEBAS NEGATIVAS: {len(vivas)} de {len(PRUEBAS_NEGATIVAS)} hacen fallar su control")
    for caso, control, falla, otros in vivas:
        print(f"  {caso} -> {control}: {falla}" + (f" (fallan también: {', '.join(otros)})" if otros else ""))
    svg, geo, c, info, nodos_svg, aristas_svg = controlar(*a, perturbacion=args.perturbar)
    if args.perturbar:
        print(f"PERTURBACIÓN: {args.perturbar}")
    print(f"INVENTARIO (releído del SVG): {len(nodos_svg)} nodos y {len(aristas_svg)} aristas; "
          f"fallas: {len(c['inventario'])}")
    for n in nodos_svg:
        print(f"  nodo   {n}")
    for o_, rel, d in aristas_svg:
        print(f"  arista {o_[0] if o_ else None} {o_[1] if o_ else ''} --{rel}--> {d[0] if d else None} "
              f"{d[1] if d else ''}")
    print(f"GEOMETRÍA: {info['textos']} textos, {info['cajas']} cajas, {info['trazos']} trazos con flecha; "
          f"cruces {len(info['cruces'])}; fallas: {len(c['geometria'])}")
    for k in c:
        for falla in c[k]:
            print(f"  MAL [{k}] {falla}")
    if any(c.values()):
        raise SystemExit("FALLA: la figura tiene defectos; no se escribe nada")
    alto = geo["alto"]
    print(f"TAMAÑO: lienzo {W} x {f(alto)}, impreso a {ANCHO_IMPRESO_CM:.2f} x "
          f"{ANCHO_IMPRESO_CM * alto / W:.2f} cm; alto de las columnas: fragmentos {geo['alto_cols'][0]:.0f}, "
          f"consulta {geo['alto_cols'][1]:.0f}")
    for fs, pt in sorted(info["tamanos"].items()):
        print(f"  letra {fs:g} unidades -> {pt:.2f} pt")
    print("RESPUESTAS")
    print(f"  izquierda: {RESPUESTA_IZQUIERDA}")
    print(f"             ✗ {RESPUESTA_IZQUIERDA_FALTA}")
    print(f"  derecha:   {RESPUESTA_DERECHA}")
    for texto, _, tipo, sangria in geo["filas_der"]:
        print(f"             - {'  ' if sangria else ''}{texto}   [{tipo}; sangría {sangria}]")
    rutas = base.exportar(svg, args.salida, NOMBRE, ANCHO_IMPRESO_CM)
    for e in ("svg", "png", "pdf"):
        print(f"{e.upper()}: {os.path.relpath(rutas[e], base.RAIZ)}   sha256 {base.sha256(rutas[e])}")
    ancho_px, alto_px = base.png_dimensiones(rutas["png"])
    if alto_px > ALTO_MAX_PNG_PX:
        freno(f"el PNG mide {alto_px} px de alto, máximo {ALTO_MAX_PNG_PX}")
    print(f"  PNG ({ancho_px}, {alto_px}) px a {base.DPI} dpi (máximo {ALTO_MAX_PNG_PX} de alto); {base.version_rsvg()}")


if __name__ == "__main__":
    try:
        main()
    except base.Freno as e:
        raise SystemExit(f"FRENO {e}")
