#!/usr/bin/env python3
"""Figura «anatomía de una tripleta» para el marco teórico (§2.1.1).

Una sola tripleta real del grafo r1: la Restricción del punto 3.17.1.4 del
Texto Ordenado de Exterior y Cambios —limita→ la Operación del mismo punto.
Dos nodos con su etiqueta corta y «punto N», la arista con el nombre de la
relación tal como está en el grafo, y tres llamadas en gris que nombran las
partes de la tripleta: nodo de origen, relación (nombre y dirección) y nodo de
destino. Sin leyenda.

La arista es de extracción, no de remisión: se dibuja en trazo continuo con el
gris oscuro de la paleta compartida, porque el naranja está reservado a las
remisiones en las figuras de la Introducción.

Reutiliza por importación, de generar_figura_norma_a_grafo.py: la paleta por
tipo de nodo, los grises, la tipografía, la tabla de métricas de Helvetica, el
envoltorio de texto y las etiquetas cortas de los nodos; y de
generar_figura_proceso_extraccion.py: el ancho impreso de 12,75 cm con su
lienzo de 720 unidades, la exportación a PNG a 300 dpi con la densidad
grabada y el medidor con métricas reales de Helvetica.

Los dos nodos y la arista no se tipean: se resuelven por consulta a kg.json
con las mismas comprobaciones que la figura del proceso: el archivo debe ser
el sellado (candado de sha256); cada búsqueda por (documento, tipo, punto de
procedencia con rol punto_propio) debe dar exactamente un nodo; la arista
(origen, relación, destino) debe existir exactamente una vez, en el índice
esperado, con una firma (tipo de origen, relación, tipo de destino) admitida
por la matriz de dominio y rango del esquema congelado y sin rol_fuente (las
aristas de la resolución de remisiones llevan rol_fuente = referencia_cruzada
y no son de extracción). Lo resuelto se imprime al correr.

Uso (desde cualquier directorio):
    PYTHONDONTWRITEBYTECODE=1 python3 docs/tesis/figuras/generar_figura_tripleta.py
    PYTHONDONTWRITEBYTECODE=1 python3 docs/tesis/figuras/generar_figura_tripleta.py --verificar

Con --verificar, además, mide cada texto con las métricas reales de Helvetica
(requiere PIL y la fuente del sistema; si faltan, lo informa y sigue) y
comprueba que ningún texto exceda su caja, se superponga con otro texto o con
un nodo ajeno, salga del lienzo ni quede por debajo del tamaño mínimo impreso.
"""

import hashlib
import json
import os
import shutil
import subprocess
import sys

sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import generar_figura_norma_a_grafo as base          # noqa: E402
import generar_figura_proceso_extraccion as proc     # noqa: E402

SALIDA_SVG = os.path.join(AQUI, "figura_tripleta.svg")
SALIDA_PNG = os.path.join(AQUI, "figura_tripleta.png")
RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", ".."))
KG = os.path.join(RAIZ, "data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json")
# sha256 del kg.json sobre el que se verificó la tripleta (el mismo candado que
# la figura del proceso, reports/verificacion_figura_proceso.md §1). Si el
# archivo cambia, el script frena: la figura afirma que esta arista está ahí.
KG_SHA256 = "0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a"

# --------------------------------------------------------------------------- #
# Tamaño impreso: el de la figura del proceso (12,75 cm = 0,85 del ancho de     #
# texto; lienzo de 720 unidades; una unidad imprime a 361,4 / 720 pt).          #
# --------------------------------------------------------------------------- #
W = proc.W                                            # 720
ANCHO_FIGURA_CM = proc.ANCHO_FIGURA_CM                # 12,75
ANCHO_FIGURA_PT = proc.ANCHO_FIGURA_PT                # 361,4
DPI = proc.DPI                                        # 300
ANCHO_PNG_PX = proc.ANCHO_PNG_PX                      # 1506
PT_MINIMO = 7.0                                       # letra mínima impresa (mandato)
puntos_impresos = proc.puntos_impresos

# --------------------------------------------------------------------------- #
# Paleta, tipografía y métricas: las del generador base                        #
# --------------------------------------------------------------------------- #
TIPOGRAFIA = base.TIPOGRAFIA
COLOR_TIPO = base.COLOR_TIPO
GRIS_ARISTA = base.GRIS_ARISTA      # líneas de llamada
GRIS_ROTULO = base.GRIS_ROTULO      # texto de las llamadas
# Trazo y rótulo de la arista: el gris oscuro de la paleta compartida (borde de
# las etapas determinísticas en generar_figura_proceso_extraccion.py,
# DETERMINISTICA["borde"]). No es el naranja ACENTO del generador base, que
# las figuras de la Introducción reservan a las remisiones.
TRAZO_ARISTA = "#4a5a6a"
ancho, envolver, esc, f = base.ancho, base.envolver, base.esc, base.f
# El punto medio de las llamadas no está en la tabla del generador base (que
# asigna 556 a lo desconocido); en Helvetica mide 278/1000 em, como el punto.
base._W.setdefault("·", 278)

FS_NODO = 17          # etiqueta y «punto N» de los nodos (8,53 pt)
FS_ARISTA = 17        # rótulo de la arista, en negrita (8,53 pt)
FS_LLAMADA = 15       # las tres llamadas en gris (7,53 pt)
IL_NODO = 21          # interlínea dentro del nodo

# --------------------------------------------------------------------------- #
# Contenido                                                                    #
# --------------------------------------------------------------------------- #
TO_FIGURA = "ext"
# (clave, tipo, punto de procedencia con rol punto_propio). La búsqueda en
# kg.json debe dar exactamente un nodo, del que salen id, etiqueta y punto.
NODOS_FIGURA = [
    ("R", "Restriccion", "3.17.1.4"),   # nodo de origen
    ("OP", "Operacion", "3.17.1.4"),    # nodo de destino
]
# (origen, relación en el grafo, destino). Debe existir exactamente una arista
# así en kg.json, en el índice esperado de kg['edges'] (las aristas del grafo
# no tienen id propio).
ARISTA_FIGURA = ("R", "limita", "OP")
INDICE_ARISTA = 16669
# Clase de la arista y su comprobación. "extraccion": la firma (tipo de
# origen, relación, tipo de destino) debe estar en la matriz de dominio y rango
# del esquema congelado (DOMAIN_RANGE_CONGELADO,
# data/experiment/esq/code/prompt_congelado.py:97-99, que hereda la fila
# `limita` de data/experiment/esq/code/prompt_esq3b.py:172) y la arista no
# lleva rol_fuente. "remision": la arista la produce la resolución de
# remisiones y lleva rol_fuente = referencia_cruzada
# (data/experiment/reextraccion_v2/corpus_v2/r1_referencias.py:231-234).
CLASE_ARISTA = "extraccion"
FIRMAS_ADMITIDAS = {
    ("Restriccion", "limita", "Operacion"),
}
ROL_REMISION = "referencia_cruzada"
# Rótulo de la arista: el nombre de la relación tal como está en el grafo (la
# figura muestra la anatomía de la tripleta, no su lectura en castellano).
ROTULO_ARISTA = "limita"
# Las tres llamadas, en gris. Los dos nodos toman tipo y punto de lo resuelto.
LLAMADA_ORIGEN = "nodo de origen · tipo {tipo} · punto {punto}"
LLAMADA_RELACION = "relación · nombre y dirección"
LLAMADA_DESTINO = "nodo de destino · tipo {tipo} · punto {punto}"
NOMBRE_TIPO = {"Restriccion": "Restricción", "Obligacion": "Obligación",
               "Operacion": "Operación", "Sujeto": "Sujeto"}
LINEAS_ETIQUETA = 2   # una etiqueta corta entra en una o dos líneas


def cargar_grafo():
    """Lee kg.json, comprueba su sha y resuelve los dos nodos y la arista.

    Devuelve (nodos, arista): `nodos` mapea clave -> dict con id, tipo, punto,
    etiqueta del grafo, etiqueta a dibujar y demás puntos propios; `arista` es
    un dict con origen, destino, relación, índice en kg['edges'], rol_fuente
    tal como figura (o su ausencia), procedencia y propiedades.
    """
    with open(KG, "rb") as fh:
        crudo = fh.read()
    sha = hashlib.sha256(crudo).hexdigest()
    if sha != KG_SHA256:
        raise SystemExit(f"kg.json no es el verificado: sha {sha[:12]}… ≠ {KG_SHA256[:12]}…")
    kg = json.loads(crudo.decode("utf-8"))

    nodos = {}
    for clave, tipo, punto in NODOS_FIGURA:
        cands = [n for n in kg["nodes"] if n["type"] == tipo and any(
            p.get("to") == TO_FIGURA and p.get("punto") == punto
            and p.get("rol_documental") == "punto_propio" for p in base.provenances(n))]
        if len(cands) != 1:
            raise SystemExit(f"nodo {clave}: ({TO_FIGURA}, {tipo}, {punto}) da "
                             f"{len(cands)} nodos, no uno: {[n['id'] for n in cands]}")
        n = cands[0]
        corta, original = base.etiqueta_de({n["id"]: n}, n["id"])
        if len(corta) > base.MAX_ETIQUETA:
            raise SystemExit(f"nodo {clave}: etiqueta de {len(corta)} caracteres, "
                             f"máximo {base.MAX_ETIQUETA}")
        nodos[clave] = {"id": n["id"], "tipo": tipo, "punto": punto,
                        "etiqueta": original, "corta": corta,
                        "otros_puntos": [p for p in base.puntos_propios(n) if p != punto]}

    a, rel, b = ARISTA_FIGURA
    ida, idb = nodos[a]["id"], nodos[b]["id"]
    hits = [(i, e) for i, e in enumerate(kg["edges"])
            if e["source"] == ida and e["target"] == idb and e["relation"] == rel]
    if len(hits) != 1:
        raise SystemExit(f"arista {a} {rel} {b}: {len(hits)} coincidencias en kg.json, no una")
    i, e = hits[0]
    if i != INDICE_ARISTA:
        raise SystemExit(f"arista {a} {rel} {b}: índice {i} en kg['edges'], esperado {INDICE_ARISTA}")
    if CLASE_ARISTA == "remision":
        if e.get("rol_fuente") != ROL_REMISION:
            raise SystemExit(f"arista {a} {rel} {b}: rol_fuente {e.get('rol_fuente')!r} "
                             f"≠ {ROL_REMISION!r}")
    else:
        firma = (nodos[a]["tipo"], rel, nodos[b]["tipo"])
        if firma not in FIRMAS_ADMITIDAS:
            raise SystemExit(f"arista fuera de la matriz del esquema: {firma}")
        if "rol_fuente" in e:
            raise SystemExit(f"arista {a} {rel} {b}: rol_fuente inesperado {e['rol_fuente']!r}")
    inversas = [k for k, x in enumerate(kg["edges"]) if x["source"] == idb and x["target"] == ida]
    arista = {"a": a, "b": b, "relacion": rel, "indice": i, "clase": CLASE_ARISTA,
              "rol_fuente": e["rol_fuente"] if "rol_fuente" in e else "(clave ausente)",
              "propiedades": e.get("properties"),
              "provenance": e.get("provenance") or {},
              "inversas": inversas}
    return nodos, arista


# --------------------------------------------------------------------------- #
# Primitivas de dibujo. Todo texto pasa por `texto()`, que lo deja registrado  #
# para la verificación de medidas.                                             #
# --------------------------------------------------------------------------- #
REGISTRO = []
CAJAS_NODO = []


def texto(partes, x, y, s, fs, negrita=False, relleno="#1f1f1f", anclaje="middle",
          ancho_max=None, dentro_de=None, contexto=""):
    """Texto con línea de base `y`; `anclaje` es start, middle o end."""
    peso = "bold" if negrita else "normal"
    partes.append(f'<text x="{f(x)}" y="{f(y)}" text-anchor="{anclaje}" '
                  f'font-size="{fs}" font-weight="{peso}" fill="{relleno}">'
                  f'{esc(s)}</text>')
    REGISTRO.append({"s": s, "fs": fs, "negrita": negrita, "x": x, "y": y,
                     "anclaje": anclaje, "ancho_max": ancho_max,
                     "dentro_de": dentro_de, "contexto": contexto})


def linea(partes, x0, y0, x1, y1, color, grosor, marcador=None, opacidad="1"):
    m = f' marker-end="url(#{marcador})"' if marcador else ""
    partes.append(f'<path d="M{f(x0)},{f(y0)} L{f(x1)},{f(y1)}" fill="none" '
                  f'stroke="{color}" stroke-width="{grosor}" opacity="{opacidad}"{m}/>')


# --------------------------------------------------------------------------- #
# Geometría: una fila de dos nodos unidos por la arista; las llamadas de los    #
# nodos arriba, la de la relación abajo, cada una con una línea de llamada.     #
# --------------------------------------------------------------------------- #
MARGEN = 24
W_NODO = 260
PAD_NODO = 12
LARGO_LLAMADA = 18      # línea de llamada entre el texto y el elemento
HOLGURA_LLAMADA = 5     # aire entre la línea de llamada y el texto o el nodo


def lineas_nodo(nodo):
    """Líneas de texto del nodo: la etiqueta corta envuelta y «punto N»."""
    lineas = [(l, False) for l, _ in envolver(nodo["corta"], FS_NODO, W_NODO - 2 * PAD_NODO)]
    if len(lineas) > LINEAS_ETIQUETA:
        raise SystemExit(f"la etiqueta {nodo['corta']!r} ocupa {len(lineas)} líneas, "
                         f"máximo {LINEAS_ETIQUETA}")
    lineas.append(("punto " + nodo["punto"], True))
    return lineas


def componer(nodos, arista):
    del REGISTRO[:]
    del CAJAS_NODO[:]
    partes = []
    n_lineas = max(len(lineas_nodo(nodos[k])) for k, _, _ in NODOS_FIGURA)
    h_nodo = 2 * PAD_NODO + n_lineas * IL_NODO

    # Fila superior: las dos llamadas de los nodos y sus líneas de llamada.
    y_llam = MARGEN + FS_LLAMADA
    y_nodo = y_llam + HOLGURA_LLAMADA + LARGO_LLAMADA + HOLGURA_LLAMADA
    pos = {"R": MARGEN, "OP": W - MARGEN - W_NODO}
    centro = {k: x + W_NODO / 2.0 for k, x in pos.items()}
    cy = y_nodo + h_nodo / 2.0

    for clave, llamada, x_txt, anclaje in (
            ("R", LLAMADA_ORIGEN, MARGEN, "start"),
            ("OP", LLAMADA_DESTINO, W - MARGEN, "end")):
        nodo = nodos[clave]
        s = llamada.format(tipo=NOMBRE_TIPO[nodo["tipo"]], punto=nodo["punto"])
        texto(partes, x_txt, y_llam, s, FS_LLAMADA, False, GRIS_ROTULO, anclaje,
              W - 2 * MARGEN, None, f"llamada {clave}")
        linea(partes, centro[clave], y_llam + HOLGURA_LLAMADA,
              centro[clave], y_nodo - HOLGURA_LLAMADA, GRIS_ARISTA, "1.0")

    # La arista: del borde derecho del origen al borde izquierdo del destino,
    # trazo continuo en el gris oscuro, con su rótulo encima.
    x0, x1 = pos["R"] + W_NODO + 2, pos["OP"] - 2
    linea(partes, x0, cy, x1, cy, TRAZO_ARISTA, "2.6", "arL", "0.95")
    x_medio = (x0 + x1) / 2.0
    texto(partes, x_medio, cy - 9, ROTULO_ARISTA, FS_ARISTA, True, TRAZO_ARISTA, "middle",
          x1 - x0 - 2 * HOLGURA_LLAMADA, None, "rótulo de la arista")

    # Los dos nodos: caja del color de su tipo, etiqueta y «punto N» en blanco.
    for clave, _, _ in NODOS_FIGURA:
        nodo = nodos[clave]
        px = pos[clave]
        partes.append(f'<rect x="{f(px)}" y="{f(y_nodo)}" width="{f(W_NODO)}" '
                      f'height="{f(h_nodo)}" fill="{COLOR_TIPO[nodo["tipo"]]}" '
                      f'fill-opacity="0.95" stroke="black" stroke-width="1.8" rx="7"/>')
        CAJAS_NODO.append((clave, (px, y_nodo, px + W_NODO, y_nodo + h_nodo)))
        lineas = lineas_nodo(nodo)
        yy = y_nodo + (h_nodo - len(lineas) * IL_NODO) / 2.0 + FS_NODO - 2
        for s, negrita in lineas:
            texto(partes, centro[clave], yy, s, FS_NODO, negrita, "white", "middle",
                  W_NODO - 2 * PAD_NODO, clave, f"nodo {clave}")
            yy += IL_NODO

    # Fila inferior: la llamada de la relación, con su línea desde la arista.
    y_llam_rel = y_nodo + h_nodo + HOLGURA_LLAMADA + FS_LLAMADA
    linea(partes, x_medio, cy + HOLGURA_LLAMADA, x_medio, y_llam_rel - FS_LLAMADA - HOLGURA_LLAMADA,
          GRIS_ARISTA, "1.0")
    texto(partes, x_medio, y_llam_rel, LLAMADA_RELACION, FS_LLAMADA, False, GRIS_ROTULO,
          "middle", None, None, "llamada relación")
    alto_total = y_llam_rel + HOLGURA_LLAMADA + MARGEN

    alto_cm = ANCHO_FIGURA_CM * alto_total / W
    cabeza = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{ANCHO_FIGURA_CM:.2f}cm" '
        f'height="{alto_cm:.2f}cm" viewBox="0 0 {W} {f(alto_total)}" '
        f'font-family="{TIPOGRAFIA}">',
        f'<rect width="{W}" height="{f(alto_total)}" fill="white"/>',
        '<defs>'
        '<marker id="arL" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
        f'markerHeight="6" orient="auto"><path d="M0,0L10,5L0,10z" fill="{TRAZO_ARISTA}"/></marker>'
        '</defs>',
    ]
    return "\n".join(cabeza + partes + ["</svg>"]) + "\n", alto_total


def exportar_png():
    rsvg = shutil.which("rsvg-convert")
    if not rsvg:
        print("rsvg-convert no está instalado: se escribió el SVG y no el PNG.")
        return False
    subprocess.run([rsvg, "-w", str(ANCHO_PNG_PX), "-f", "png", "-o", SALIDA_PNG,
                    SALIDA_SVG], check=True)
    proc.grabar_densidad(SALIDA_PNG, DPI)
    return True


# --------------------------------------------------------------------------- #
# Verificación de medidas                                                      #
# --------------------------------------------------------------------------- #
def verificar(alto_total):
    medir = proc.medidor()
    fuente = "métricas reales de Helvetica" if medir else "tabla de métricas del script"
    if not medir:
        print("PIL o la fuente del sistema no están: se verifica con la tabla del script.")
        medir = ancho
    print(f"\nVERIFICACIÓN DE MEDIDAS ({fuente})")
    fallas, cajas = [], []
    for r in REGISTRO:
        a = medir(r["s"], r["fs"], r["negrita"])
        x0 = {"start": r["x"], "middle": r["x"] - a / 2.0, "end": r["x"] - a}[r["anclaje"]]
        bb = (x0, r["y"] - r["fs"] * 0.78, x0 + a, r["y"] + r["fs"] * 0.22)
        cajas.append((r, bb))
        pt = puntos_impresos(r["fs"])
        estado = []
        if pt < PT_MINIMO:
            estado.append(f"letra {pt:.2f} pt < {PT_MINIMO}")
        if r["ancho_max"] is not None and a > r["ancho_max"]:
            estado.append(f"ancho {a:.1f} > caja {r['ancho_max']:.1f}")
        if bb[0] < 0 or bb[2] > W or bb[1] < 0 or bb[3] > alto_total:
            estado.append("fuera del lienzo")
        for clave, nb in CAJAS_NODO:
            cruza = bb[0] < nb[2] and nb[0] < bb[2] and bb[1] < nb[3] and nb[1] < bb[3]
            if r["dentro_de"] == clave:
                if not (nb[0] <= bb[0] and bb[2] <= nb[2] and nb[1] <= bb[1] and bb[3] <= nb[3]):
                    estado.append(f"sale del nodo {clave}")
            elif cruza:
                estado.append(f"pisa el nodo {clave}")
        tope = f"{r['ancho_max']:6.1f}" if r["ancho_max"] is not None else "     –"
        print(f"  {'MAL' if estado else 'ok '} {pt:5.2f} pt  ancho {a:6.1f} / {tope}  "
              f"{r['contexto']:20s} {r['s']!r}" + ("  <-- " + "; ".join(estado) if estado else ""))
        fallas += [(r["s"], e) for e in estado]
    for i in range(len(cajas)):
        for j in range(i + 1, len(cajas)):
            (ra, a), (rb, b) = cajas[i], cajas[j]
            if a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]:
                fallas.append((ra["s"], f"se superpone con {rb['s']!r}"))
                print(f"  MAL superposición: {ra['s']!r} / {rb['s']!r}")
    print(f"  textos medidos: {len(REGISTRO)}   fallas: {len(fallas)}")
    return not fallas


def main():
    nodos, arista = cargar_grafo()
    print(f"GRAFO: {os.path.relpath(KG, RAIZ)}   sha256 {KG_SHA256[:12]}… (comprobado)")
    for clave, _, _ in NODOS_FIGURA:
        n = nodos[clave]
        otros = f"  (además en {', '.join(n['otros_puntos'])})" if n["otros_puntos"] else ""
        print(f"  nodo {clave:2s} {n['tipo']:11s} punto {n['punto']:9s} {n['id']}{otros}")
        marca = "" if n["corta"] == n["etiqueta"] else f"  (acortada de {len(n['etiqueta'])})"
        print(f"          etiqueta en el grafo: {n['etiqueta']!r}")
        print(f"          etiqueta dibujada [{len(n['corta'])}]: {n['corta']!r}{marca}")
    pv = arista["provenance"]
    print(f"  arista kg['edges'][{arista['indice']}]  {arista['a']} --{arista['relacion']}--> "
          f"{arista['b']}  clase {arista['clase']}  rol_fuente {arista['rol_fuente']}")
    print(f"          firma ({nodos[arista['a']]['tipo']}, {arista['relacion']}, "
          f"{nodos[arista['b']]['tipo']}) admitida por la matriz del esquema")
    print(f"          procedencia {pv.get('chunk_id')!r}  páginas {pv.get('paginas')!r}  "
          f"rol_documental {pv.get('rol_documental')!r}")
    print(f"          properties: {json.dumps(arista['propiedades'], ensure_ascii=False)}")
    print(f"          aristas en sentido inverso ({arista['b']} -> {arista['a']}): {len(arista['inversas'])}")

    svg, alto_total = componer(nodos, arista)
    with open(SALIDA_SVG, "w", encoding="utf-8") as fh:
        fh.write(svg)
    print(f"SVG: {SALIDA_SVG}   lienzo {W} x {alto_total:.0f}")
    print(f"Impresa a {ANCHO_FIGURA_CM:.2f} cm de ancho ({ANCHO_FIGURA_PT:.1f} pt), "
          f"alto {ANCHO_FIGURA_CM * alto_total / W:.2f} cm:")
    for nombre, fs in (("etiqueta y punto de los nodos", FS_NODO),
                       ("rótulo de la arista", FS_ARISTA),
                       ("llamadas", FS_LLAMADA)):
        print(f"    {nombre:32s} {fs} -> {puntos_impresos(fs):5.2f} pt (mínimo {PT_MINIMO})")
    if exportar_png():
        print(f"PNG: {SALIDA_PNG}   {ANCHO_PNG_PX} px de ancho, {DPI} dpi")
    if "--verificar" in sys.argv[1:]:
        if not verificar(alto_total):
            raise SystemExit("FALLA: la verificación de medidas encontró defectos")


if __name__ == "__main__":
    main()
