#!/usr/bin/env python3
"""Figura del esquema final (capítulo 3, sección 3.10), versión 3, POR SCRIPT y nunca a mano.

Qué dibuja: los 9 tipos de entidad más Sujeto; las 13 relaciones que emite el
extractor, con sus 28 firmas, agrupadas en buses (un tramo común por relación,
como establecida_en en la figura del esquema de partida); remite_a, la relación
que deriva el código, una sola vez y en línea discontinua; y una marca en los
tipos que llevan la propiedad umbrales. Lo que el esquema final agrega
respecto del esquema de partida va en magenta solo en las cajas de los tipos
nuevos y en los rótulos de las relaciones nuevas; todas las líneas de relación
van en el gris de la figura de partida (versión 3).

Fuentes, cada una con candado de sha256 (FUENTES; si una cambia, el script
frena antes de dibujar):
  - enums_r2.json: tipos, relaciones, firmas (las 26 congeladas más la
    ampliación de r2) y tipos con la propiedad umbrales;
  - scripts/remisiones.py: la definición de remite_a (predicado, tipos de
    contenido, TextoOrdenado y la función de firma, que se evalúa sobre todos
    los pares de tipos);
  - data/experiment/grafo_v2/code/schema.py: el esquema de partida (6 tipos,
    12 relaciones, 17 firmas), para saber qué agrega el esquema final; se lee
    con ast, sin importarlo;
  - figura_esquema_partida.svg: la figura del esquema de partida, de la que se
    heredan el tamaño y el estilo de cajas y grupos, la paleta, la tipografía
    y los trazos que unen cajas que se desplazan juntas.
Todo con la biblioteca estándar; remisiones.py se ejecuta desde el texto
verificado (exec), sin importarlo, así que no escribe bytecode.

Versión 2. Ubicación de las cajas como en la figura del esquema congelado:
Potestad y Condicion en el grupo de la izquierda, debajo de Excepcion, y
Definicion en un grupo propio a la derecha, debajo del acto regulado. Las cajas
y grupos de la partida conservan tamaño y estilo y se desplazan (DESPLAZAMIENTO):
la columna de la izquierda y Operacion bajan 48 px para dejar, sobre el grupo
de la izquierda, la franja de remite_a; Sujeto pasa debajo de Operacion. Un
trazo de la partida se conserva, trasladado, cuando sus dos cajas se desplazan
lo mismo (el corredor hacia Operacion, exceptua, exceptua_obligacion,
referencia y modificada_por); los demás se trazan de nuevo (TRAZOS_NUEVOS).
remite_a es un lazo que sale del grupo de la izquierda y vuelve a él, más una
flecha hacia TextoOrdenado; la leyenda nombra los 7 tipos de contenido.

Versión 3. Mismas cajas, grupos, trazado y cruces que la versión 2. Todas las
líneas de relación y sus puntas van en el gris de la partida, también
condicion_de, las ramas nuevas de aplica_a y establecida_en, y remite_a
(discontinua). El magenta queda en el borde y el fondo de Potestad, Condicion
y Definicion y en los rótulos de condicion_de y remite_a (D["relaciones_nuevas"]).
condicion_de lleva un segundo rótulo junto a su tramo vertical, a la derecha
del grupo de la izquierda. La leyenda muestra una caja y un rótulo de ejemplo
en magenta.

Controles (verificar(); cualquier falla FRENA y no se escribe nada):
  0. grupos: cada caja dentro de su grupo y de ningún otro; Sujeto fuera de
     todos;
  1. firmas: las firmas que se leen en el dibujo (fuentes y puntas de cada red
     de trazos conectados) son exactamente las 28 del código; remite_a sale
     del grupo de la izquierda, vuelve a él y llega a TextoOrdenado, y la
     leyenda nombra exactamente los tipos de contenido del código (= 56
     firmas); el SVG emitido se relee y sus atributos data-* dan las mismas;
  2. trazado: ningún tramo diagonal; ningún extremo suelto; ningún trazo
     atraviesa una caja ni corre sobre su borde; cada flecha entra a su caja
     por un punto propio (a 10 px o más de los demás); ninguna punta toca
     otra red; tramos paralelos de redes distintas a 10 px o más;
  3. cruces: entre redes distintas solo hay cruces en X (nunca un toque ni un
     tramo superpuesto), y son exactamente los de CRUCES_DECLARADOS;
  4. textos: ningún texto toca un trazo, una punta, una caja, el borde de un
     grupo u otro texto (con el halo de los rótulos; la punta de la propia
     relación solo puede rozar el halo, como exceptua_obligacion en la figura
     de partida); cada rótulo queda a 6 px o menos de su red y al menos 5 px
     más lejos de cualquier otra (el segundo rótulo de condicion_de, a 14 px
     o menos: ver ROTULOS_NUEVOS), y hay un rótulo por red (dos en
     condicion_de); ningún texto por debajo de 7 pt impresos;
  5. margen: nada a menos de 2 mm del borde del lienzo;
  6. colores, sobre el SVG que se emitiría: toda línea de relación y toda
     punta en el gris de la partida; rótulos en magenta solo los de las
     relaciones nuevas; cajas en magenta solo las de los tipos nuevos.
Pruebas negativas (MUTACIONES; corren en cada ejecución, antes de escribir):
una caja de tipo de contenido fuera de su grupo, una línea de relación que no
es gris, un rótulo sobre una caja, un tramo diagonal, una firma de más y una
de menos; cada una tiene que frenar en el control que le corresponde.

Salidas, byte-reproducibles, a 15 cm de ancho: figura_esquema_final.svg,
.png (300 dpi, densidad grabada) y .pdf (rsvg-convert con SOURCE_DATE_EPOCH=0).

Uso (desde la raíz del repo):
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_esquema_final.py
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_esquema_final.py --salida <dir>
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_esquema_final.py --mutacion caja_fuera_de_grupo
"""

from __future__ import annotations

import argparse
import ast
import copy
import hashlib
import json
import os
import re
import shutil
import struct
import subprocess
import sys
import xml.etree.ElementTree as ET
import zlib

sys.dont_write_bytecode = True

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", ".."))
NOMBRE = "figura_esquema_final"


class Freno(Exception):
    """Falla de un control: la figura no se escribe."""


def freno(control: str, motivo: str):
    raise Freno(f"[{control}] {motivo}")


# ========================================================================== #
# Fuentes y candados                                                         #
# ========================================================================== #
FUENTES = {
    "enums": ("data/experiment/pyd_r2/generados/enums_r2.json",
              "abd197ac8bbb818f680dc80d1b9c9df3e1f1f733fce3fd46b35e7440e7ce4241"),
    "remisiones": ("scripts/remisiones.py",
                   "1da7464195875b1206ee9b1d1a15ac10f5976e5ce3700ccb230c7410bb9fde6d"),
    "partida_esquema": ("data/experiment/grafo_v2/code/schema.py",
                        "cc98e4354cf2ad507954f7fa99f12b8445e6157c9a0bcb026a13908e63de7eab"),
    "partida_figura": ("docs/tesis/figuras/figura_esquema_partida.svg",
                       "be98b797e3f6338818055cac12ed4308acb9a48df012177a923e45021f3b4a3a"),
}

SUJETO = "Sujeto"
GRUPO = "GRUPO_IZQUIERDA"     # extremo de remite_a: el grupo de la izquierda


def sha256(ruta: str) -> str:
    with open(ruta, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def leer(clave: str) -> str:
    rel, esperado = FUENTES[clave]
    with open(os.path.join(RAIZ, rel), "rb") as fh:
        crudo = fh.read()
    sha = hashlib.sha256(crudo).hexdigest()
    if sha != esperado:
        freno("fuentes", f"{rel} no es el verificado: sha256 {sha[:12]}… ≠ {esperado[:12]}…")
    return crudo.decode("utf-8")


def linea_de(texto: str, patron: str) -> int:
    """Número de línea (1-based) de la única línea que contiene `patron`."""
    hallados = [i + 1 for i, l in enumerate(texto.splitlines()) if patron in l]
    if len(hallados) != 1:
        freno("fuentes", f"{len(hallados)} líneas con {patron!r}, se esperaba una")
    return hallados[0]


def expandir(firmas: dict) -> set[tuple[str, str, str]]:
    return {(p, d, r) for p, (dom, ran) in firmas.items() for d in dom for r in ran}


def leer_datos() -> dict:
    """Lee cada fuente con su candado y devuelve los datos de la figura."""
    D: dict = {"lineas": {}}

    # --- enums_r2.json: tipos, relaciones, firmas, umbrales -----------------
    texto = leer("enums")
    en = json.loads(texto)
    for k in ("tipo_entidad", "predicado", "predicados_sujeto", "firmas_congeladas",
              "ampliacion_r2", "firmas_r2", "claves_por_tipo", "tipos_con_umbrales"):
        D["lineas"][f"enums:{k}"] = linea_de(texto, f'"{k}": ')
    tipos = list(en["tipo_entidad"])
    firmas = expandir(en["firmas_r2"])
    congeladas = expandir(en["firmas_congeladas"])
    ampliacion = {tuple(t) for t in en["ampliacion_r2"]}
    if firmas != congeladas | ampliacion or congeladas & ampliacion:
        freno("fuentes", "firmas_r2 ≠ firmas_congeladas ∪ ampliacion_r2")
    if set(en["firmas_r2"]) != set(en["predicado"]):
        freno("fuentes", "las relaciones de firmas_r2 no son las de «predicado»")
    extremos = {d for _, d, _ in firmas} | {r for _, _, r in firmas}
    if extremos != set(tipos) | {SUJETO}:
        freno("fuentes", f"extremos de las firmas {sorted(extremos)} ≠ tipos + Sujeto")
    if {p for p, d, r in firmas if SUJETO in (d, r)} != set(en["predicados_sujeto"]):
        freno("fuentes", "las relaciones con extremo Sujeto no son predicados_sujeto")
    umbrales = list(en["tipos_con_umbrales"])
    for t in umbrales:
        if t not in tipos or "umbrales" not in en["claves_por_tipo"][t]:
            freno("fuentes", f"{t} figura con umbrales pero no lleva la clave")
    if {t for t, c in en["claves_por_tipo"].items() if "umbrales" in c} != set(umbrales):
        freno("fuentes", "tipos_con_umbrales no coincide con claves_por_tipo")
    D.update(tipos=tipos, predicados=list(en["predicado"]), firmas=firmas,
             congeladas=congeladas, ampliacion=ampliacion, umbrales=umbrales)

    # --- scripts/remisiones.py: remite_a -----------------------------------
    texto = leer("remisiones")
    ns: dict = {}
    exec(compile(texto, FUENTES["remisiones"][0], "exec"), ns)
    for k, patron in (("PREDICADO_REMISION", "PREDICADO_REMISION = "),
                      ("TIPOS_CONTENIDO", "TIPOS_CONTENIDO = "),
                      ("TIPO_TEXTO_ORDENADO", "TIPO_TEXTO_ORDENADO = "),
                      ("firma_remite_a_ok", "def firma_remite_a_ok(")):
        D["lineas"][f"remisiones:{k}"] = linea_de(texto, patron)
    universo = tipos + [SUJETO]
    remite = {(o, d) for o in universo for d in universo if ns["firma_remite_a_ok"](o, d)}
    contenido = list(ns["TIPOS_CONTENIDO"])
    to = ns["TIPO_TEXTO_ORDENADO"]
    if remite != {(o, d) for o in contenido for d in contenido + [to]}:
        freno("fuentes", "firma_remite_a_ok no es contenido × (contenido ∪ TextoOrdenado)")
    if not set(contenido) <= set(tipos) or to not in tipos:
        freno("fuentes", "los tipos de remite_a no son tipos del esquema")
    dom_est = {d for p, d, _ in firmas if p == "establecida_en"}
    if dom_est != set(contenido):
        freno("fuentes", "el dominio de establecida_en no son los tipos de contenido")
    D.update(remite_a=ns["PREDICADO_REMISION"], contenido=contenido, to=to,
             firmas_remite=remite)

    # --- schema.py de partida (ast, sin importar) ---------------------------
    texto = leer("partida_esquema")
    tipos_p = dr_p = None
    for nodo in ast.parse(texto).body:
        if (isinstance(nodo, ast.Assign) and len(nodo.targets) == 1
                and getattr(nodo.targets[0], "id", None) == "ENTITY_TYPES"):
            tipos_p = ast.literal_eval(nodo.value)
            D["lineas"]["partida:ENTITY_TYPES"] = (nodo.lineno, nodo.end_lineno)
        if (isinstance(nodo, ast.AnnAssign)
                and getattr(nodo.target, "id", None) == "DOMAIN_RANGE"):
            dr_p = ast.literal_eval(nodo.value)
            D["lineas"]["partida:DOMAIN_RANGE"] = (nodo.lineno, nodo.end_lineno)
    if tipos_p is None or dr_p is None:
        freno("fuentes", "schema.py: no se encontraron ENTITY_TYPES y DOMAIN_RANGE")
    firmas_p = expandir(dr_p)
    if (len(tipos_p), len(dr_p), len(firmas_p)) != (6, 12, 17):
        freno("fuentes", "el esquema de partida no tiene 6 tipos, 12 relaciones y 17 firmas")
    if not firmas_p <= firmas or not set(tipos_p) <= set(tipos):
        freno("fuentes", "el esquema de partida no está contenido en el final")
    D.update(tipos_partida=list(tipos_p), firmas_partida=firmas_p,
             firmas_nuevas=firmas - firmas_p,
             tipos_nuevos=[t for t in tipos if t not in tipos_p],
             relaciones_nuevas=sorted(set(D["predicados"]) - set(dr_p)) + [D["remite_a"]])
    return D


# ========================================================================== #
# La figura del esquema de partida: posiciones, trazos, rótulos y estilo     #
# ========================================================================== #
def _num(v: str) -> float:
    return float(v)


def _pts_path(d: str) -> list[tuple[float, float]]:
    nums = [float(n) for n in re.findall(r"-?\d+(?:\.\d+)?", d)]
    if not d.startswith("M") or len(nums) % 2:
        freno("fuentes", f"path de la figura de partida no reconocido: {d!r}")
    return [(nums[i], nums[i + 1]) for i in range(0, len(nums), 2)]


def _direccion(a, b) -> str:
    if a[0] == b[0]:
        return "down" if b[1] > a[1] else "up"
    return "right" if b[0] > a[0] else "left"


def leer_partida(D: dict) -> dict:
    """Todo lo que la figura del esquema de partida dibuja, como datos."""
    raiz = ET.fromstring(leer("partida_figura"))
    ns = "{http://www.w3.org/2000/svg}"
    hijos = list(raiz)
    P: dict = {"W": _num(raiz.get("width")), "H": _num(raiz.get("height")),
               "sans": raiz.get("font-family"), "cajas": {}, "zonas": [], "trazos": [],
               "puntas": [], "rotulos": [], "firmas_svg": set(), "nota": None}
    textos_zona = []
    i = 0
    while i < len(hijos):
        el, tag = hijos[i], hijos[i].tag.replace(ns, "")
        if tag == "rect" and el.get("width") == "190" and el.get("height") == "46":
            nombre_el = hijos[i + 1]
            nombre = nombre_el.text
            P["cajas"][nombre] = dict(
                x=_num(el.get("x")), y=_num(el.get("y")), w=190.0, h=46.0,
                relleno=el.get("fill"), borde=el.get("stroke"),
                grosor=_num(el.get("stroke-width")), rx=_num(el.get("rx")),
                discontinua=el.get("stroke-dasharray"))
            P["caja_w"], P["caja_h"], P["caja_rx"] = 190.0, 46.0, _num(el.get("rx"))
            P["fs_nodo"] = int(nombre_el.get("font-size"))
            P["mono"] = nombre_el.get("font-family")
            P["tinta"] = nombre_el.get("fill")
            P["dy_nombre"] = _num(nombre_el.get("y")) - _num(el.get("y"))
            i += 2
            continue
        if tag == "rect" and el.get("rx") == "8":
            P["zonas"].append(dict(x0=_num(el.get("x")), y0=_num(el.get("y")),
                                   x1=_num(el.get("x")) + _num(el.get("width")),
                                   y1=_num(el.get("y")) + _num(el.get("height")),
                                   lineas=[]))
            P["fondo_zona"], P["borde_zona"] = el.get("fill"), el.get("stroke")
        elif tag == "text" and el.get("font-style") == "italic":
            textos_zona.append(dict(texto=el.text, x=_num(el.get("x")), y=_num(el.get("y")),
                                    anchor=el.get("text-anchor")))
            P["fs_zona"] = int(el.get("font-size"))
            P["gris_rotulo"] = el.get("fill")
        elif tag == "line":
            P["trazos"].append(dict(pred=None, a=(_num(el.get("x1")), _num(el.get("y1"))),
                                    b=(_num(el.get("x2")), _num(el.get("y2"))),
                                    estilo="solido", origen="partida", firma=None))
        elif tag == "path":
            pred, dom, ran = el.get("data-pred"), el.get("data-dom"), el.get("data-ran")
            P["firmas_svg"].add((pred, dom, ran))
            pts = _pts_path(el.get("d"))
            P["gris_arista"], P["grosor_arista"] = el.get("stroke"), _num(el.get("stroke-width"))
            for a, b in zip(pts, pts[1:]):
                P["trazos"].append(dict(pred=pred, a=a, b=b, estilo="solido", origen="partida",
                                        firma=(pred, dom, ran)))
            if i + 1 < len(hijos) and hijos[i + 1].tag.replace(ns, "") == "polygon":
                P["puntas"].append(dict(pred=pred, punto=pts[-1], dir=_direccion(pts[-2], pts[-1]),
                                        caja=ran, estilo="solido", firma=(pred, dom, ran)))
                i += 1
        elif tag == "text" and el.get("stroke"):
            tr = el.get("transform") or ""
            m = re.match(r"rotate\((-?\d+)", tr)
            P["rotulos"].append(dict(texto=el.text, x=_num(el.get("x")), y=_num(el.get("y")),
                                     anchor=el.get("text-anchor"),
                                     rot=int(m.group(1)) if m else 0, pred=el.text,
                                     origen="partida"))
            P["fs_rotulo"] = int(el.get("font-size"))
        i += 1

    # Rótulos de zona dentro de su zona; la nota es la de Sujeto.
    for t in textos_zona:
        dentro = [z for z in P["zonas"] if z["x0"] < t["x"] < z["x1"] and z["y0"] < t["y"] < z["y1"]]
        if len(dentro) == 1:
            dentro[0]["lineas"].append((t["texto"], t["x"], t["y"]))
        elif P["nota"] is None:
            P["nota"] = t
        else:
            freno("fuentes", f"texto en cursiva sin zona: {t['texto']!r}")

    # Los troncos (<line>) toman la relación de los dientes que llegan a ellos.
    for t in P["trazos"]:
        if t["pred"] is not None:
            continue
        preds = {u["pred"] for u in P["trazos"] if u["pred"] and
                 any(sobre_tramo(p, t["a"], t["b"]) for p in (u["a"], u["b"]))}
        if len(preds) != 1:
            freno("fuentes", f"tronco {t['a']}–{t['b']} sin relación única: {preds}")
        t["pred"] = preds.pop()

    if P["firmas_svg"] != D["firmas_partida"]:
        freno("fuentes", "la figura de partida no dibuja las 17 firmas de schema.py")
    if set(P["cajas"]) != set(D["tipos_partida"]) | {SUJETO}:
        freno("fuentes", "las cajas de la figura de partida no son sus 6 tipos y Sujeto")
    return P


def sobre_tramo(p, a, b, tol: float = 1e-6) -> bool:
    """¿El punto p está sobre el tramo a-b (incluidos sus extremos)?"""
    (px, py), (ax, ay), (bx, by) = p, a, b
    if abs((bx - ax) * (py - ay) - (by - ay) * (px - ax)) > tol:
        return False
    return (min(ax, bx) - tol <= px <= max(ax, bx) + tol and
            min(ay, by) - tol <= py <= max(ay, by) + tol)



# ========================================================================== #
# Diseño de la versión 2 (coordenadas en el marco de la figura de partida)   #
# ========================================================================== #
# Color de lo agregado: el de la figura del esquema congelado
# (generar_figuras_esquema.py, RESALTE), ausente de la paleta de tipos.
RESALTE = "#b5179e"
GROSOR_RESALTE = 2.6
MEZCLA_RELLENO_NUEVO = 0.90          # como en la figura del esquema congelado
COLOR_MARCA = "#3d3d3d"              # marca de umbrales
DASH = "7 5"                         # el de la caja Sujeto de la figura de partida
FS_LEYENDA = 15
# Versión 3: todas las líneas de relación (y sus puntas) van en el gris de la
# figura de partida; lo agregado se marca solo en las cajas de los tipos nuevos
# (borde y fondo) y en los rótulos de las relaciones nuevas (D["relaciones_nuevas"]).
ROTULOS_POR_RED = {"condicion_de": 2}      # las demás redes llevan un rótulo

W, H = 850, 860
ANCHO_CM = 15.0
PT_POR_CM = 72.0 / 2.54
DPI = 300
ANCHO_PNG_PX = round(ANCHO_CM / 2.54 * DPI)            # 1772
PT_MINIMO = 7.0
MARGEN_MM = 2.0

# Desplazamiento de las cajas de la figura de partida, que conservan tamaño y
# estilo: la columna de la izquierda y Operacion bajan 48 px (franja de
# remite_a sobre el grupo de la izquierda y lugar para el rótulo de dos
# líneas por encima de requiere); Sujeto pasa debajo de Operacion.
DESPLAZAMIENTO = {"Obligacion": (0, 48), "Restriccion": (0, 48), "Excepcion": (0, 48),
                  "Operacion": (0, 48), "TextoOrdenado": (0, 0), "Comunicacion": (0, 0),
                  SUJETO: (235, 20)}
# Cajas nuevas, como en la figura del esquema congelado: Potestad y Condicion
# debajo de Excepcion; Definicion a la derecha, debajo del acto regulado.
CAJAS_NUEVAS = {"Potestad": (90, 540), "Condicion": (90, 640), "Definicion": (620, 571)}

# Grupos. El de la izquierda reemplaza al de la partida («lo que la norma
# manda, prohíbe o exime»): mismo ancho y estilo, más alto para abarcar a
# Potestad y Condicion, y rótulo nuevo en dos líneas. El rótulo del mandato
# («lo que la norma manda, prohíbe, exime o permite, y cuándo») no entra en dos
# líneas en los 224 px del grupo: su primera línea posible, «lo que la norma
# manda, prohíbe,», mide 216,8 px y el rótulo empieza a 8 px del borde.
ROTULO_PARTIDA_IZQUIERDA = "lo que la norma manda,"     # primera línea en la partida
GRUPO_IZQUIERDA = dict(nombre="izquierda", y0=128.0, y1=702.0,
                       lineas=[("lo que manda, prohíbe, exime", 84.0, 146.0),
                               ("o permite la norma, y cuándo", 84.0, 164.0)])
GRUPO_DEFINICION = dict(nombre="definicion", x0=606.0, y0=545.0, x1=824.0, y1=631.0,
                        lineas=[("lo que la norma define", 614.0, 563.0)])
MIEMBROS = {"izquierda": ("Obligacion", "Restriccion", "Excepcion", "Potestad", "Condicion"),
            "acto regulado": ("Operacion",),
            "anclaje documental": ("TextoOrdenado", "Comunicacion"),
            "definicion": ("Definicion",)}

# Trazos nuevos: (relación, polilínea, punta) — punta = (caja de destino) o None.
TRAZOS_NUEVOS = [
    # establecida_en: peine izquierdo con los cinco dientes del grupo de la
    # izquierda (tronco x = 40) y bus derecho desde Operacion y Definicion.
    ("establecida_en", [(90, 208), (40, 208), (40, 83), (620, 83)], "TextoOrdenado"),
    ("establecida_en", [(90, 308), (40, 308)], None),
    ("establecida_en", [(90, 408), (40, 408)], None),
    ("establecida_en", [(90, 550), (40, 550)], None),
    ("establecida_en", [(90, 650), (40, 650)], None),
    ("establecida_en", [(40, 208), (40, 650)], None),
    ("establecida_en", [(710, 388), (832, 388), (832, 83), (810, 83)], "TextoOrdenado"),
    ("establecida_en", [(810, 594), (832, 594)], None),
    ("establecida_en", [(832, 388), (832, 594)], None),
    # aplica_a: un solo bus. Tronco izquierdo (x = 64) con Obligacion,
    # Restriccion y Excepcion, que gira por el hueco entre Excepcion y Potestad
    # hasta Sujeto; Potestad sube desde su borde superior y Operacion baja.
    ("aplica_a", [(90, 240), (64, 240), (64, 513), (330, 513)], SUJETO),
    ("aplica_a", [(90, 340), (64, 340)], None),
    ("aplica_a", [(90, 440), (64, 440)], None),
    ("aplica_a", [(150, 540), (150, 513)], None),
    ("aplica_a", [(555, 424), (555, 470), (310, 470), (310, 513)], None),
    # ejecuta: de Sujeto al borde inferior de Operacion.
    ("ejecuta", [(520, 523), (590, 523), (590, 424)], "Operacion"),
    # condicion_de: un bus desde el borde inferior de Condicion. Por la
    # izquierda hasta Obligacion; por la derecha de la columna hasta
    # Restriccion, Excepcion, Operacion y Potestad.
    ("condicion_de", [(180, 686), (180, 722)], None),
    ("condicion_de", [(180, 722), (16, 722), (16, 224), (90, 224)], "Obligacion"),
    ("condicion_de", [(180, 722), (292, 722), (292, 368), (268, 368), (268, 344)], "Restriccion"),
    ("condicion_de", [(292, 448), (530, 448), (530, 424)], "Operacion"),
    ("condicion_de", [(292, 490), (230, 490), (230, 444)], "Excepcion"),
    ("condicion_de", [(292, 613), (200, 613), (200, 586)], "Potestad"),
]
# remite_a, en línea discontinua: un lazo que sale del grupo de la izquierda
# y vuelve a él, y una flecha hacia TextoOrdenado, en la franja entre
# establecida_en (y = 83) y el borde superior del grupo (y = 128).
TRAZOS_REMITE = [
    ([(250, 128), (250, 101)], None),
    ([(250, 101), (620, 101)], "TextoOrdenado"),
    ([(250, 101), (120, 101), (120, 128)], GRUPO),
]

# Rótulos nuevos: (texto, x, y, anchor, rot[, distancia máxima a su red]). Los
# dos de establecida_en van donde estaban en la figura de partida. El segundo
# de condicion_de va junto a su tramo vertical (x = 292), a la derecha del
# grupo de la izquierda: el tramo corre 8 px adentro del borde del grupo y, del
# lado de adentro, las cajas y el bus de aplica_a no dejan lugar; afuera, el
# rótulo no puede tocar el borde, así que queda a 13,1 px del tramo (tope 14
# en lugar de 6), sin otra red a menos de 57 px.
ROTULOS_NUEVOS = [
    ("establecida_en", 330, 76, "middle", 0),
    ("establecida_en", 826, 273, "end", 0),
    ("aplica_a", 170, 505, "middle", 0),
    ("ejecuta", 526, 539, "start", 0),
    ("condicion_de", 98, 738, "middle", 0),
    ("condicion_de", 316.5, 625, "middle", -90, 14.0),
    ("remite_a", 430, 117, "middle", 0),
]

# Marca de umbrales: cuadro con «≤» en el extremo derecho de la caja.
MARCA = dict(dx=165, dy=14, lado=18, texto="≤", fs=15)

# Leyenda: (clave de la muestra, x de la muestra, x del texto, y, líneas).
# Cada línea es una lista de trozos (texto, monoespaciada). La línea de los
# tipos de contenido se arma con los nombres del código (ver leyenda()).
LEYENDA_FILAS = [
    ("agregado", 76, 196, 768,
     [[("tipo o relación agregados respecto del esquema de partida", False)]]),
    ("derivada", 76, 164, 794, None),
    ("umbrales", 76, 164, 838, [[("el tipo lleva la propiedad umbrales", False)]]),
]
LEYENDA_MUESTRA_ROTULO = "relación"     # rótulo de ejemplo, en magenta, junto a la caja de ejemplo
LEYENDA_MUESTRA_DX = 36                 # de la caja de ejemplo al rótulo de ejemplo
LEYENDA_INTERLINEA = 18

# Cruces entre flechas de redes distintas: 6, los mismos 6 de la versión 1 en
# número. Los 4 primeros son los de la figura de partida trasladados; los 2
# últimos, los de condicion_de (ver LEEME_figura_esquema_final.md, §5).
CRUCES_DECLARADOS = {
    (64.0, 308.0): "tronco de aplica_a × diente establecida_en de Restriccion",
    (64.0, 408.0): "tronco de aplica_a × diente establecida_en de Excepcion",
    (78.0, 308.0): "exceptua_obligacion × diente establecida_en de Restriccion",
    (78.0, 340.0): "exceptua_obligacion × diente aplica_a de Restriccion",
    (40.0, 224.0): "condicion_de hacia Obligacion × tronco izquierdo de establecida_en",
    (292.0, 513.0): "condicion_de hacia Restriccion, Excepcion y Operacion × aplica_a hacia Sujeto",
}


def hex_mix(color: str, blanco: float) -> str:
    r, g, b = (int(color[i:i + 2], 16) for i in (1, 3, 5))
    m = [round(c + (255 - c) * blanco) for c in (r, g, b)]
    return "#{:02x}{:02x}{:02x}".format(*m)


def _mover(p, d):
    return (p[0] + d[0], p[1] + d[1])


def _desplazamiento_comun(firma):
    """El desplazamiento de un trazo de la partida: el de sus dos cajas si es el
    mismo; None si se desplazan distinto (el trazo se dibuja de nuevo)."""
    _, dom, ran = firma
    a, b = DESPLAZAMIENTO[dom], DESPLAZAMIENTO[ran]
    return a if a == b else None


def leyenda(D, M) -> list[dict]:
    """Filas de la leyenda; la de remite_a nombra los tipos de contenido del
    código en el orden en que aparecen en la figura (grupo de la izquierda de
    arriba abajo, luego los de la derecha)."""
    orden = sorted(D["contenido"], key=lambda n: (M["cajas"][n]["x"] > 300,
                                                  M["cajas"][n]["y"], M["cajas"][n]["x"]))
    trozos = []
    for i, n in enumerate(orden):
        if i:
            trozos.append((" y " if i == len(orden) - 1 else ", ", False))
        trozos.append((n, True))
    filas = []
    for clave, xm, xt, y, lineas in LEYENDA_FILAS:
        if clave == "derivada":
            lineas = [[(D["remite_a"], True),
                       (f" la deriva el código y vale entre cualquier par de los {len(orden)} "
                        "tipos de contenido,", False)],
                      trozos]
        filas.append(dict(clave=clave, xm=xm, xt=xt, y=y, lineas=lineas, tipos=orden))
    return filas


def armar_modelo(D: dict, P: dict) -> dict:
    """Modelo de la versión 2: cajas y grupos de la partida desplazados, sus
    trazos conservados donde las dos cajas se desplazan juntas, y lo nuevo."""
    M: dict = {"cajas": {}, "zonas": [], "trazos": [], "puntas": [], "rotulos": [], "marcas": []}
    M["estilo"] = {k: P[k] for k in ("sans", "mono", "fs_nodo", "fs_zona", "fs_rotulo",
                                       "gris_rotulo", "gris_arista", "grosor_arista",
                                       "fondo_zona", "borde_zona", "tinta", "dy_nombre")}
    if set(DESPLAZAMIENTO) != set(P["cajas"]):
        freno("fuentes", "DESPLAZAMIENTO no nombra exactamente las cajas de la partida")
    for nombre, c in P["cajas"].items():
        M["cajas"][nombre] = dict(c, x=c["x"] + DESPLAZAMIENTO[nombre][0],
                                  y=c["y"] + DESPLAZAMIENTO[nombre][1], nueva=False)
    for nombre, (x, y) in CAJAS_NUEVAS.items():
        M["cajas"][nombre] = dict(x=float(x), y=float(y), w=P["caja_w"], h=P["caja_h"],
                                  relleno=hex_mix(RESALTE, MEZCLA_RELLENO_NUEVO), borde=RESALTE,
                                  grosor=GROSOR_RESALTE, rx=P["caja_rx"], discontinua=None,
                                  nueva=True)
    if set(M["cajas"]) != set(D["tipos"]) | {SUJETO}:
        freno("firmas", f"cajas {sorted(M['cajas'])} ≠ los 9 tipos del código y Sujeto")
    n = P["nota"]
    dx, dy = DESPLAZAMIENTO[SUJETO]
    M["nota"] = dict(n, x=n["x"] + dx, y=n["y"] + dy)

    # Grupos de la partida, desplazados con sus cajas; el de la izquierda se
    # reemplaza por el grupo ampliado.
    for z in P["zonas"]:
        dentro = [nm for nm, c in P["cajas"].items()
                  if z["x0"] <= c["x"] and c["x"] + c["w"] <= z["x1"]
                  and z["y0"] <= c["y"] and c["y"] + c["h"] <= z["y1"]]
        despl = {DESPLAZAMIENTO[nm] for nm in dentro}
        if len(despl) != 1:
            freno("fuentes", f"el grupo «{z['lineas'][0][0]}» no tiene un desplazamiento único")
        ddx, ddy = despl.pop()
        if z["lineas"][0][0] == ROTULO_PARTIDA_IZQUIERDA:
            g = GRUPO_IZQUIERDA
            M["zonas"].append(dict(nombre=g["nombre"], x0=z["x0"] + ddx, x1=z["x1"] + ddx,
                                   y0=g["y0"], y1=g["y1"], lineas=list(g["lineas"])))
        else:
            M["zonas"].append(dict(nombre=z["lineas"][0][0], x0=z["x0"] + ddx, x1=z["x1"] + ddx,
                                   y0=z["y0"] + ddy, y1=z["y1"] + ddy,
                                   lineas=[(s, x + ddx, y + ddy) for s, x, y in z["lineas"]]))
    M["zonas"].append(dict(GRUPO_DEFINICION, lineas=list(GRUPO_DEFINICION["lineas"])))
    if sorted(z["nombre"] for z in M["zonas"]) != sorted(MIEMBROS):
        freno("fuentes", f"grupos {sorted(z['nombre'] for z in M['zonas'])} ≠ MIEMBROS")

    # Trazos, puntas y rótulos de la partida que se conservan, trasladados.
    conservadas = set()
    for t in P["trazos"]:
        d = _desplazamiento_comun(t["firma"]) if t["firma"] else None
        if d is not None:
            conservadas.add(t["firma"])
            M["trazos"].append(dict(t, a=_mover(t["a"], d), b=_mover(t["b"], d),
                                    origen="partida, trasladado"))
    for p in P["puntas"]:
        d = _desplazamiento_comun(p["firma"])
        if d is not None:
            M["puntas"].append(dict(p, punto=_mover(p["punto"], d)))
    for r in P["rotulos"]:
        R = rect_texto(r["texto"], r["x"], r["y"], P["fs_rotulo"], r["anchor"], r["rot"], True)
        propios = [t for t in P["trazos"] if t["pred"] == r["pred"] and t["firma"]]
        cercano = min(propios, key=lambda t: dist_rect_tramo(R, t["a"], t["b"]))
        d = _desplazamiento_comun(cercano["firma"])
        if d is not None:
            M["rotulos"].append(dict(r, x=r["x"] + d[0], y=r["y"] + d[1],
                                     origen="partida, trasladado"))
    M["conservadas"] = conservadas

    def poner(pred, pts, destino, estilo):
        for a, b in zip(pts, pts[1:]):
            M["trazos"].append(dict(pred=pred, a=(float(a[0]), float(a[1])),
                                    b=(float(b[0]), float(b[1])), estilo=estilo, origen="nuevo",
                                    firma=None))
        if destino is not None:
            M["puntas"].append(dict(pred=pred, punto=(float(pts[-1][0]), float(pts[-1][1])),
                                    dir=_direccion(pts[-2], pts[-1]), caja=destino, estilo=estilo,
                                    firma=None))

    for pred, pts, destino in TRAZOS_NUEVOS:
        poner(pred, pts, destino, "solido")
    for pts, destino in TRAZOS_REMITE:
        poner(D["remite_a"], pts, destino, "discontinuo")
    for texto, x, y, anchor, rot, *junto in ROTULOS_NUEVOS:
        M["rotulos"].append(dict(texto=texto, x=float(x), y=float(y), anchor=anchor, rot=rot,
                                 pred=texto, origen="nuevo", junto=junto[0] if junto else JUNTO))
    M["color_lineas"] = {}      # relación → color; vacío = todas en gris (lo controla verificar)
    for t in D["umbrales"]:
        c = M["cajas"][t]
        M["marcas"].append(dict(caja=t, x=c["x"] + MARCA["dx"], y=c["y"] + MARCA["dy"],
                                lado=MARCA["lado"]))
    M["leyenda"] = leyenda(D, M)
    return M
# ========================================================================== #
# Geometría: redes de trazos, firmas dibujadas, tramos y cruces              #
# ========================================================================== #
TOL = 1e-6


def en_borde_caja(p, c, tol: float = 0.01) -> bool:
    x0, y0, x1, y1 = c["x"], c["y"], c["x"] + c["w"], c["y"] + c["h"]
    dentro = x0 - tol <= p[0] <= x1 + tol and y0 - tol <= p[1] <= y1 + tol
    return dentro and (min(abs(p[0] - x0), abs(p[0] - x1), abs(p[1] - y0), abs(p[1] - y1)) <= tol)




def zona(M, nombre: str) -> dict:
    return next(z for z in M["zonas"] if z["nombre"] == nombre)


def rect_zona(z) -> tuple:
    return (z["x0"], z["y0"], z["x1"], z["y1"])


def en_borde_grupo(p, M) -> bool:
    """¿El punto está sobre el borde del grupo de la izquierda (extremo de remite_a)?"""
    z = zona(M, GRUPO_IZQUIERDA["nombre"])
    return en_borde_caja(p, dict(x=z["x0"], y=z["y0"], w=z["x1"] - z["x0"], h=z["y1"] - z["y0"]))

def redes(M) -> list[list[int]]:
    """Componentes conexas de trazos de la misma relación y el mismo estilo."""
    T = M["trazos"]
    padre = list(range(len(T)))

    def raiz(i):
        while padre[i] != i:
            padre[i] = padre[padre[i]]
            i = padre[i]
        return i
    for i in range(len(T)):
        for j in range(i + 1, len(T)):
            a, b = T[i], T[j]
            if (a["pred"], a["estilo"]) != (b["pred"], b["estilo"]):
                continue
            if (sobre_tramo(a["a"], b["a"], b["b"]) or sobre_tramo(a["b"], b["a"], b["b"]) or
                    sobre_tramo(b["a"], a["a"], a["b"]) or sobre_tramo(b["b"], a["a"], a["b"])):
                padre[raiz(i)] = raiz(j)
    grupos: dict = {}
    for i in range(len(T)):
        grupos.setdefault(raiz(i), []).append(i)
    return sorted(grupos.values(), key=lambda g: min(g))


def caja_de(p, M):
    hits = [n for n, c in M["cajas"].items() if en_borde_caja(p, c)]
    if len(hits) > 1:
        freno("trazado", f"el punto {p} está en el borde de dos cajas: {hits}")
    if hits:
        return hits[0]
    return GRUPO if en_borde_grupo(p, M) else None


def analizar_redes(M) -> list[dict]:
    """Para cada red: sus trazos, sus fuentes (extremo sobre una caja que no es
    punta), sus puntas y las firmas que dibuja (fuentes × destinos)."""
    T, R = M["trazos"], []
    for k, idx in enumerate(redes(M)):
        pred, estilo = T[idx[0]]["pred"], T[idx[0]]["estilo"]
        puntas = [p for p in M["puntas"] if p["pred"] == pred and p["estilo"] == estilo and
                  any(sobre_tramo(p["punto"], T[i]["a"], T[i]["b"]) for i in idx)]
        tips = {p["punto"] for p in puntas}
        fuentes = []
        for i in idx:
            for e in (T[i]["a"], T[i]["b"]):
                if e in tips:
                    continue
                otros = [j for j in idx if j != i and sobre_tramo(e, T[j]["a"], T[j]["b"])]
                c = caja_de(e, M)
                if c is not None and not otros:
                    fuentes.append((c, e))
                elif c is None and not otros:
                    freno("trazado", f"extremo suelto de {pred} en {e}")
        for p in puntas:
            if caja_de(p["punto"], M) != p["caja"]:
                freno("trazado", f"la punta de {pred} en {p['punto']} no está sobre {p['caja']}")
        firmas = {(pred, c, p["caja"]) for c, _ in fuentes for p in puntas}
        R.append(dict(id=k, pred=pred, estilo=estilo, trazos=idx, puntas=puntas,
                      fuentes=sorted(set(fuentes)), firmas=firmas))
    return R


def tramos_de_red(M, red) -> list[tuple]:
    """Tramos únicos de una red: cada trazo partido en todos los puntos de la
    red que caen sobre él (los trazos repetidos se funden)."""
    T = M["trazos"]
    pts = set()
    for i in red["trazos"]:
        pts.add(T[i]["a"])
        pts.add(T[i]["b"])
    for i in red["trazos"]:
        for j in red["trazos"]:
            a, b, c, d = T[i]["a"], T[i]["b"], T[j]["a"], T[j]["b"]
            if a[0] == b[0] and c[1] == d[1]:   # vertical × horizontal
                p = (a[0], c[1])
                if sobre_tramo(p, a, b) and sobre_tramo(p, c, d):
                    pts.add(p)
    tramos = set()
    for i in red["trazos"]:
        a, b = T[i]["a"], T[i]["b"]
        sobre = sorted((p for p in pts if sobre_tramo(p, a, b)),
                       key=lambda p: (p[0] - a[0]) ** 2 + (p[1] - a[1]) ** 2)
        for p, q in zip(sobre, sobre[1:]):
            if p != q:
                tramos.add(tuple(sorted((p, q))))
    return sorted(tramos)


def recorrido(tramos, s, t) -> list[tuple]:
    """Camino más corto (en largo) de s a t por los tramos de una red."""
    ady: dict = {}
    for p, q in tramos:
        L = abs(p[0] - q[0]) + abs(p[1] - q[1])
        ady.setdefault(p, []).append((q, L, (p, q)))
        ady.setdefault(q, []).append((p, L, (p, q)))
    dist, prev, pend = {s: 0.0}, {}, {s}
    while pend:
        u = min(pend, key=lambda v: (dist[v], v))
        pend.remove(u)
        if u == t:
            break
        for v, L, tr in ady.get(u, []):
            if dist[u] + L < dist.get(v, 1e18):
                dist[v], prev[v] = dist[u] + L, (u, tr)
                pend.add(v)
    if t not in dist:
        return []
    camino, v = [], t
    while v != s:
        u, tr = prev[v]
        camino.append(tr)
        v = u
    return camino


def marcar_tramos(M, R, D) -> list[dict]:
    """Cada tramo con las firmas que pasan por él y su color (resaltado si
    todas las firmas que lo usan son nuevas respecto de la partida)."""
    nuevas = D["firmas_nuevas"]
    salida = []
    for red in R:
        tramos = tramos_de_red(M, red)
        uso: dict = {tr: set() for tr in tramos}
        for c, e in red["fuentes"]:
            for p in red["puntas"]:
                f = (red["pred"], c, p["caja"])
                for tr in recorrido(tramos, e, p["punto"]):
                    uso[tr].add(f)
        for tr, fs in uso.items():
            if not fs:
                freno("trazado", f"tramo {tr} de {red['pred']} sin ninguna firma")
            nuevo = red["estilo"] == "discontinuo" or all(f in nuevas for f in fs)
            salida.append(dict(red=red["id"], pred=red["pred"], estilo=red["estilo"],
                               a=tr[0], b=tr[1], firmas=fs, nuevo=nuevo))
        for p in red["puntas"]:
            fs = {(red["pred"], c, p["caja"]) for c, _ in red["fuentes"]}
            p["nuevo"] = red["estilo"] == "discontinuo" or all(f in nuevas for f in fs)
            p["red"] = red["id"]
    return salida


def cruces(tramos) -> tuple[dict, list[str]]:
    """Cruces en X entre tramos de redes distintas; cualquier otro contacto
    (un toque en T, un extremo compartido, un tramo superpuesto) es defecto."""
    puntos, defectos = {}, []
    for i in range(len(tramos)):
        for j in range(i + 1, len(tramos)):
            s, u = tramos[i], tramos[j]
            if s["red"] == u["red"]:
                continue
            (a, b), (c, d) = (s["a"], s["b"]), (u["a"], u["b"])
            hs, hu = a[1] == b[1], c[1] == d[1]
            if hs != hu:
                h, v = (s, u) if hs else (u, s)
                p = (v["a"][0], h["a"][1])
                if not (sobre_tramo(p, h["a"], h["b"]) and sobre_tramo(p, v["a"], v["b"])):
                    continue
                if p in (h["a"], h["b"], v["a"], v["b"]):
                    defectos.append(f"{s['pred']} y {u['pred']} se tocan en {p}")
                else:
                    puntos.setdefault(p, set()).add(tuple(sorted((s["pred"], u["pred"]))))
            else:
                eje = 1 if hs else 0
                if a[eje] != c[eje]:
                    continue
                o = 0 if hs else 1
                lo, hi = max(min(a[o], b[o]), min(c[o], d[o])), min(max(a[o], b[o]), max(c[o], d[o]))
                if lo <= hi:
                    defectos.append(f"{s['pred']} y {u['pred']} superpuestos sobre {'y' if hs else 'x'}"
                                    f" = {a[eje]}")
    return puntos, defectos


# ========================================================================== #
# Textos: medidas                                                            #
# ========================================================================== #
ANCHO_MONO = 0.602      # avance de Menlo por carácter, en em
ASC_MONO, DESC_MONO = 0.76, 0.24
ASC_SANS, DESC_SANS = 0.72, 0.22
HALO = 1.75             # mitad del stroke-width del halo de los rótulos
AIRE = 1.0
JUNTO, MARGEN_AJENA = 6.0, 5.0
DISTANCIA_PARALELAS = 10.0

# Anchos AFM de Helvetica (/1000).
_AFM = dict(zip("abcdefghijklmnopqrstuvwxyz",
                (556, 556, 500, 556, 556, 278, 556, 556, 222, 222, 500, 222, 833, 556, 556,
                 556, 556, 333, 500, 278, 556, 500, 722, 500, 500, 500)))
_AFM.update({" ": 278, ",": 278, ";": 278, "(": 333, ")": 333, "á": 556, "é": 556,
             "í": 278, "ó": 556, "ú": 556, "ñ": 556})
_AFM.update({str(d): 556 for d in range(10)})


def ancho_sans(s: str, fs: float) -> float:
    try:
        return sum(_AFM[c] for c in s) / 1000.0 * fs
    except KeyError as e:
        freno("textos", f"carácter sin medida AFM: {e}")


def rect_texto(s, x, y, fs, anchor, rot, mono) -> tuple:
    w = (ANCHO_MONO * fs * len(s)) if mono else ancho_sans(s, fs)
    asc, desc = (ASC_MONO, DESC_MONO) if mono else (ASC_SANS, DESC_SANS)
    dx0 = {"start": 0.0, "middle": -w / 2.0, "end": -w}[anchor]
    dy0, dy1 = -asc * fs, desc * fs
    if rot == 0:
        return (x + dx0, y + dy0, x + dx0 + w, y + dy1)
    if rot == -90:   # rotate(-90): (dx, dy) local → (x + dy, y − dx)
        return (x + dy0, y - dx0 - w, x + dy1, y - dx0)
    freno("textos", f"rotación no prevista: {rot}")


def crecer(R, m):
    return (R[0] - m, R[1] - m, R[2] + m, R[3] + m)


def se_solapan(A, B) -> bool:
    return A[0] < B[2] and B[0] < A[2] and A[1] < B[3] and B[1] < A[3]


def largo_dentro(a, b, R) -> float:
    """Largo del tramo a-b dentro del rectángulo R (recorte paramétrico del tramo)."""
    (x0, y0), (x1, y1) = a, b
    dx, dy = x1 - x0, y1 - y0
    t0, t1 = 0.0, 1.0
    for p, q in ((-dx, x0 - R[0]), (dx, R[2] - x0), (-dy, y0 - R[1]), (dy, R[3] - y0)):
        if abs(p) < 1e-12:
            if q < 0:
                return 0.0
            continue
        t = q / p
        if p < 0:
            t0 = max(t0, t)
        else:
            t1 = min(t1, t)
        if t0 > t1:
            return 0.0
    return (t1 - t0) * (dx * dx + dy * dy) ** 0.5


def toca(a, b, R) -> bool:
    """¿El tramo a-b toca el rectángulo R (incluido rozar su borde)?"""
    if largo_dentro(a, b, R) > 0:
        return True
    return any(R[0] <= p[0] <= R[2] and R[1] <= p[1] <= R[3] for p in (a, b))


def dist_rect_tramo(R, a, b) -> float:
    if toca(a, b, R):
        return 0.0
    if a[1] == b[1]:   # horizontal
        dx = max(R[0] - max(a[0], b[0]), 0.0, min(a[0], b[0]) - R[2])
        dy = max(R[1] - a[1], 0.0, a[1] - R[3])
    else:
        dx = max(R[0] - a[0], 0.0, a[0] - R[2])
        dy = max(R[1] - max(a[1], b[1]), 0.0, min(a[1], b[1]) - R[3])
    return (dx * dx + dy * dy) ** 0.5


def triangulo(p, direc) -> list[tuple]:
    x, y = p
    return {"right": [(x, y), (x - 9, y - 5), (x - 9, y + 5)],
            "left": [(x, y), (x + 9, y - 5), (x + 9, y + 5)],
            "up": [(x, y), (x - 5, y + 9), (x + 5, y + 9)],
            "down": [(x, y), (x - 5, y - 9), (x + 5, y - 9)]}[direc]


def bbox(pts) -> tuple:
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    return (min(xs), min(ys), max(xs), max(ys))




# ========================================================================== #
# Controles                                                                  #
# ========================================================================== #
def ancho_trozos(trozos, fs) -> float:
    return sum((ANCHO_MONO * fs * len(s)) if mono else ancho_sans(s, fs) for s, mono in trozos)


def rect_linea_leyenda(trozos, x, y) -> tuple:
    w = ancho_trozos(trozos, FS_LEYENDA)
    mono = any(m for _, m in trozos)
    asc = max(ASC_MONO if mono else 0, ASC_SANS)
    desc = max(DESC_MONO if mono else 0, DESC_SANS)
    return (x, y - asc * FS_LEYENDA, x + w, y + desc * FS_LEYENDA)


def textos_de(M) -> list[dict]:
    """Todo texto de la figura con su rectángulo."""
    E, T = M["estilo"], []
    for n, c in sorted(M["cajas"].items()):
        T.append(dict(tipo="nombre", texto=n, caja=n, halo=False, fs=E["fs_nodo"],
                      R=rect_texto(n, c["x"] + c["w"] / 2, c["y"] + E["dy_nombre"], E["fs_nodo"],
                                   "middle", 0, True)))
    for m in M["marcas"]:
        T.append(dict(tipo="marca", texto=MARCA["texto"], caja=m["caja"], halo=False, fs=MARCA["fs"],
                      R=(m["x"], m["y"], m["x"] + m["lado"], m["y"] + m["lado"])))
    for z in M["zonas"]:
        for s, x, y in z["lineas"]:
            T.append(dict(tipo="zona", texto=s, halo=False, fs=E["fs_zona"], zona=z,
                          R=rect_texto(s, x, y, E["fs_zona"], "start", 0, False)))
    n = M["nota"]
    T.append(dict(tipo="nota", texto=n["texto"], halo=False, fs=E["fs_zona"],
                  R=rect_texto(n["texto"], n["x"], n["y"], E["fs_zona"], n["anchor"], 0, False)))
    for r in M["rotulos"]:
        T.append(dict(tipo="rotulo", texto=r["texto"], halo=True, fs=E["fs_rotulo"], rotulo=r,
                      R=rect_texto(r["texto"], r["x"], r["y"], E["fs_rotulo"], r["anchor"], r["rot"],
                                   True)))
    for fila in M["leyenda"]:
        for i, trozos in enumerate(fila["lineas"]):
            y = fila["y"] + 5 + i * LEYENDA_INTERLINEA
            T.append(dict(tipo="leyenda", texto="".join(s for s, _ in trozos), halo=False,
                          fs=FS_LEYENDA, R=rect_linea_leyenda(trozos, fila["xt"], y)))
        if fila["clave"] == "agregado":
            T.append(dict(tipo="muestra", texto=LEYENDA_MUESTRA_ROTULO, halo=False, fs=FS_LEYENDA,
                          R=rect_texto(LEYENDA_MUESTRA_ROTULO, fila["xm"] + LEYENDA_MUESTRA_DX,
                                       fila["y"] + 5, FS_LEYENDA, "start", 0, True)))
    return T


def graficos_leyenda(M) -> list[tuple]:
    """Rectángulos de las muestras de la leyenda (para márgenes y solapes)."""
    res = []
    for fila in M["leyenda"]:
        ancho = {"umbrales": MARCA["lado"], "agregado": 26}.get(fila["clave"], 76)
        res.append((fila["xm"], fila["y"] - 9, fila["xm"] + ancho, fila["y"] + 9))
    return res


def verificar(M, D) -> dict:
    """Todos los controles; el primero que falla FRENA."""
    rep: dict = {}
    E = M["estilo"]
    cajas_R = {n: (c["x"], c["y"], c["x"] + c["w"], c["y"] + c["h"]) for n, c in M["cajas"].items()}

    # --- 0. grupos -------------------------------------------------------------
    miembros = [n for v in MIEMBROS.values() for n in v]
    if len(miembros) != len(set(miembros)) or set(miembros) != set(M["cajas"]) - {SUJETO}:
        freno("grupos", "MIEMBROS no reparte exactamente los 9 tipos en los grupos")
    for z in M["zonas"]:
        Z = rect_zona(z)
        for n, Rc in sorted(cajas_R.items()):
            dentro = Z[0] < Rc[0] and Rc[2] < Z[2] and Z[1] < Rc[1] and Rc[3] < Z[3]
            if n in MIEMBROS[z["nombre"]] and not dentro:
                freno("grupos", f"la caja {n} está fuera de su grupo «{z['nombre']}»")
            if n not in MIEMBROS[z["nombre"]] and se_solapan(Rc, Z):
                freno("grupos", f"la caja {n} invade el grupo «{z['nombre']}»")
    for a in M["zonas"]:
        for b in M["zonas"]:
            if a["nombre"] < b["nombre"] and se_solapan(crecer(rect_zona(a), 6), rect_zona(b)):
                freno("grupos", f"los grupos «{a['nombre']}» y «{b['nombre']}» están a menos de 6 px")
    rep["grupos"] = {z["nombre"]: list(MIEMBROS[z["nombre"]]) for z in M["zonas"]}

    # --- 1. firmas -------------------------------------------------------------
    for t in M["trazos"]:
        if t["a"] == t["b"]:
            freno("trazado", f"tramo de largo cero de {t['pred']} en {t['a']}")
    R = analizar_redes(M)
    solidas = [r for r in R if r["estilo"] == "solido"]
    discontinuas = [r for r in R if r["estilo"] == "discontinuo"]
    dibujadas = set().union(*(r["firmas"] for r in solidas))
    sobran, faltan = dibujadas - D["firmas"], D["firmas"] - dibujadas
    if sobran:
        freno("firmas", f"firmas de más en el dibujo: {sorted(sobran)}")
    if faltan:
        freno("firmas", f"firmas de menos en el dibujo: {sorted(faltan)}")
    if any(GRUPO in (f[1], f[2]) for f in dibujadas):
        freno("firmas", "una relación del extractor toca el borde del grupo de la izquierda")
    cd = [r for r in solidas if r["pred"] == "condicion_de"]
    if len(cd) != 1 or len(cd[0]["puntas"]) != 5:
        freno("firmas", "condicion_de no es un solo bus con sus 5 puntas")
    if len(discontinuas) != 1 or discontinuas[0]["pred"] != D["remite_a"]:
        freno("firmas", f"{D['remite_a']} no es una sola red discontinua")
    rem = discontinuas[0]
    if {c for c, _ in rem["fuentes"]} != {GRUPO} or \
            sorted(p["caja"] for p in rem["puntas"]) != sorted([GRUPO, D["to"]]):
        freno("firmas", f"{D['remite_a']} no sale del grupo de la izquierda, vuelve a él y llega "
                        f"a {D['to']}")
    fila = next(f for f in M["leyenda"] if f["clave"] == "derivada")
    tipos_ley = list(fila["tipos"])
    nombrados = [s for s, mono in fila["lineas"][1] if mono]
    if sorted(nombrados) != sorted(D["contenido"]) or sorted(tipos_ley) != sorted(D["contenido"]):
        freno("firmas", f"la leyenda de {D['remite_a']} nombra {nombrados}, no los tipos de "
                        f"contenido del código")
    if not set(MIEMBROS["izquierda"]) <= set(tipos_ley):
        freno("firmas", "el grupo de la izquierda tiene tipos que no son de contenido")
    remite_dibujada = {(o, d) for o in tipos_ley for d in tipos_ley + [D["to"]]}
    if remite_dibujada != D["firmas_remite"]:
        freno("firmas", f"{D['remite_a']}: el dibujo da {len(remite_dibujada)} firmas, el código "
                        f"{len(D['firmas_remite'])}")
    rep["redes"] = R
    rep["dibujadas"] = dibujadas
    rep["remite_dibujada"] = remite_dibujada

    # --- 2. trazado ------------------------------------------------------------
    for t in M["trazos"]:
        if t["a"][0] != t["b"][0] and t["a"][1] != t["b"][1]:
            freno("trazado", f"tramo diagonal de {t['pred']}: {t['a']} → {t['b']}")
    tramos = marcar_tramos(M, R, D)
    rep["tramos"] = tramos
    for tr in tramos:
        for n, Rc in cajas_R.items():
            if largo_dentro(tr["a"], tr["b"], crecer(Rc, -1.5)) > 0.5:
                freno("trazado", f"{tr['pred']} atraviesa la caja {n}")
            x0, y0, x1, y1 = Rc
            for a, b in (((x0, y0), (x1, y0)), ((x0, y1), (x1, y1)), ((x0, y0), (x0, y1)),
                         ((x1, y0), (x1, y1))):
                if (a[0] == b[0]) == (tr["a"][0] == tr["b"][0]):
                    eje = 0 if a[0] == b[0] else 1
                    o = 1 - eje
                    if a[eje] == tr["a"][eje]:
                        lo = max(min(a[o], b[o]), min(tr["a"][o], tr["b"][o]))
                        hi = min(max(a[o], b[o]), max(tr["a"][o], tr["b"][o]))
                        if hi - lo > 0.5:
                            freno("trazado", f"{tr['pred']} corre sobre el borde de {n}")
    # Cada flecha entra (o sale) por un punto propio: puntos de contacto con
    # cada caja separados al menos 10 px.
    contactos: dict = {}
    for r in R:
        for c, e in r["fuentes"]:
            contactos.setdefault(c, []).append((e, r["pred"]))
        for p in r["puntas"]:
            contactos.setdefault(p["caja"], []).append((p["punto"], r["pred"]))
    for c, lista in contactos.items():
        for i in range(len(lista)):
            for j in range(i + 1, len(lista)):
                (p, a), (q, b) = lista[i], lista[j]
                d = abs(p[0] - q[0]) + abs(p[1] - q[1])
                if d < 10:
                    freno("trazado", f"{a} y {b} llegan a {c} por puntos a {d:.0f} px")
    for p in M["puntas"]:
        T = crecer(bbox(triangulo(p["punto"], p["dir"])), 0.5)
        for tr in tramos:
            if tr["red"] != p["red"] and toca(tr["a"], tr["b"], T):
                freno("trazado", f"la punta de {p['pred']} en {p['punto']} toca {tr['pred']}")
    for i in range(len(tramos)):
        for j in range(i + 1, len(tramos)):
            s, u = tramos[i], tramos[j]
            if s["red"] == u["red"]:
                continue
            for eje in (0, 1):
                o = 1 - eje
                if s["a"][eje] == s["b"][eje] and u["a"][eje] == u["b"][eje]:
                    lo = max(min(s["a"][o], s["b"][o]), min(u["a"][o], u["b"][o]))
                    hi = min(max(s["a"][o], s["b"][o]), max(u["a"][o], u["b"][o]))
                    d = abs(s["a"][eje] - u["a"][eje])
                    if hi - lo > 0 and 0 < d < DISTANCIA_PARALELAS:
                        freno("trazado", f"{s['pred']} y {u['pred']} paralelas a {d:.0f} px")
    for a, b in ((m, n) for m in M["cajas"] for n in M["cajas"] if m < n):
        if se_solapan(crecer(cajas_R[a], 10), cajas_R[b]):
            freno("trazado", f"las cajas {a} y {b} están a menos de 10 px")

    # --- 3. cruces -------------------------------------------------------------
    puntos, defectos = cruces(tramos)
    if defectos:
        freno("cruces", "contactos que no son cruces en X: " + "; ".join(defectos))
    if set(puntos) != set(CRUCES_DECLARADOS):
        freno("cruces", f"los cruces no son los declarados: sobran "
                        f"{sorted(set(puntos) - set(CRUCES_DECLARADOS))}, faltan "
                        f"{sorted(set(CRUCES_DECLARADOS) - set(puntos))}")
    rep["cruces"] = puntos

    # --- 4. textos -------------------------------------------------------------
    T = textos_de(M)
    rep["textos"] = T
    minimo = min(t["fs"] for t in T) * ANCHO_CM * PT_POR_CM / W
    if minimo < PT_MINIMO:
        freno("textos", f"letra mínima {minimo:.2f} pt impresos < {PT_MINIMO}")
    rep["pt_minimo"] = minimo
    zonas_R = [rect_zona(z) for z in M["zonas"]]
    leyenda_R = graficos_leyenda(M)
    for i, t in enumerate(T):
        Rg = crecer(t["R"], (HALO + AIRE) if t["halo"] else AIRE)
        nombre = f"{t['tipo']} «{t['texto']}»" + (
            f" en ({t['rotulo']['x']:g}, {t['rotulo']['y']:g})" if t["tipo"] == "rotulo" else "")
        if t["tipo"] in ("nombre", "marca"):
            if not (cajas_R[t["caja"]][0] + 2 <= t["R"][0] and t["R"][2] <= cajas_R[t["caja"]][2] - 2):
                freno("textos", f"{nombre} se sale de su caja")
        else:
            for n, Rc in cajas_R.items():
                if se_solapan(Rg, Rc):
                    freno("textos", f"{nombre} toca la caja {n}")
            for z in zonas_R:
                dentro = (z[0] + 2 <= Rg[0] and Rg[2] <= z[2] - 2 and z[1] + 2 <= Rg[1]
                          and Rg[3] <= z[3] - 2)
                if not dentro and se_solapan(Rg, crecer(z, 2)):
                    freno("textos", f"{nombre} cruza el borde de un grupo")
        for tr in rep["tramos"]:
            if toca(tr["a"], tr["b"], Rg):
                freno("textos", f"{nombre} toca el trazo de {tr['pred']}")
        for p in M["puntas"]:
            # La punta de la propia relación puede rozar el halo del rótulo (así
            # está exceptua_obligacion en la figura de partida), no el texto.
            propia = t["tipo"] == "rotulo" and p["pred"] == t["rotulo"]["pred"]
            if se_solapan(t["R"] if propia else Rg, bbox(triangulo(p["punto"], p["dir"]))):
                freno("textos", f"{nombre} toca la punta de {p['pred']}")
        for L in leyenda_R:
            if se_solapan(Rg, L):
                freno("textos", f"{nombre} toca una muestra de la leyenda")
        for u in T[i + 1:]:
            Ru = crecer(u["R"], HALO if u["halo"] else 0)
            if se_solapan(Rg, Ru):
                freno("textos", f"{nombre} toca {u['tipo']} «{u['texto']}»")
    for z in M["zonas"]:
        for s, x, y in z["lineas"]:
            Rz = rect_texto(s, x, y, E["fs_zona"], "start", 0, False)
            if not (z["x0"] < Rz[0] and Rz[2] < z["x1"] and z["y0"] < Rz[1] and Rz[3] < z["y1"]):
                freno("textos", f"el rótulo de grupo «{s}» se sale de su grupo")
    # Cada rótulo de relación junto a su red y lejos de las demás.
    cerca = {}
    for t in T:
        if t["tipo"] != "rotulo":
            continue
        dist: dict = {}
        for tr in rep["tramos"]:
            dist[tr["red"]] = min(dist.get(tr["red"], 1e9), dist_rect_tramo(t["R"], tr["a"], tr["b"]))
        propias = [rid for rid in dist if R[rid]["pred"] == t["rotulo"]["pred"]]
        if not propias:
            freno("textos", f"el rótulo «{t['texto']}» no tiene red con ese nombre")
        propia = min(propias, key=lambda rid: dist[rid])
        ajena = min((rid for rid in dist if rid != propia), key=lambda rid: dist[rid])
        if dist[propia] > t["rotulo"].get("junto", JUNTO) or dist[ajena] - dist[propia] < MARGEN_AJENA:
            freno("textos", f"el rótulo «{t['texto']}» en ({t['rotulo']['x']:g}, {t['rotulo']['y']:g})"
                            f" no queda junto a su red: {dist[propia]:.1f} px de ella y "
                            f"{dist[ajena]:.1f} px de {R[ajena]['pred']}")
        cerca[(t["texto"], t["rotulo"]["x"], t["rotulo"]["y"])] = (dist[propia], R[ajena]["pred"],
                                                                  dist[ajena])
        t["rotulo"]["red"] = propia
    rep["cercania"] = cerca
    rotuladas = [t["rotulo"]["red"] for t in T if t["tipo"] == "rotulo"]
    for r in R:
        esperados = ROTULOS_POR_RED.get(r["pred"], 1)
        if rotuladas.count(r["id"]) != esperados:
            freno("textos", f"la red de {r['pred']} tiene {rotuladas.count(r['id'])} rótulos, "
                            f"no {esperados}")

    # --- 5. margen -------------------------------------------------------------
    m = MARGEN_MM * W / (ANCHO_CM * 10)
    cosas = [("texto " + t["texto"], t["R"]) for t in T]
    cosas += [("trazo " + tr["pred"], bbox([tr["a"], tr["b"]])) for tr in rep["tramos"]]
    cosas += [("punta " + p["pred"], bbox(triangulo(p["punto"], p["dir"]))) for p in M["puntas"]]
    cosas += [("caja " + n, Rc) for n, Rc in cajas_R.items()]
    cosas += [("grupo " + z["nombre"], rect_zona(z)) for z in M["zonas"]]
    cosas += [("leyenda", L) for L in leyenda_R]
    for nombre, B in cosas:
        if B[0] < m or B[1] < m or B[2] > W - m or B[3] > H - m:
            freno("margen", f"{nombre} a menos de {MARGEN_MM} mm del borde: {B}")
    rep["margen_min_mm"] = min(min(B[0], B[1], W - B[2], H - B[3]) for _, B in cosas) \
        * ANCHO_CM * 10 / W

    # --- 6. colores, sobre el SVG que se emitiría --------------------------------
    svg = dibujar(M, D, rep)
    rep["colores"] = controlar_colores(svg, M, D)
    rep["svg"] = svg
    return rep


def controlar_colores(svg: str, M, D) -> dict:
    """Toda línea de relación y toda punta en el gris de la partida, con su
    grosor; rótulos en magenta solo los de las relaciones nuevas; cajas en
    magenta solo las de los tipos nuevos."""
    E, ns = M["estilo"], "{http://www.w3.org/2000/svg}"
    raiz = ET.fromstring(svg)
    lineas = [el for el in raiz.iter(ns + "path") if el.get("data-pred")]
    for el in lineas:
        if el.get("stroke") != E["gris_arista"] or el.get("stroke-width") != f(E["grosor_arista"]):
            freno("colores", f"la línea de {el.get('data-pred')} no es gris: {el.get('stroke')}, "
                             f"{el.get('stroke-width')} px")
    puntas = [el for el in raiz.iter(ns + "polygon") if el.get("data-pred")]
    for el in puntas:
        if el.get("fill") != E["gris_arista"]:
            freno("colores", f"la punta de {el.get('data-pred')} no es gris: {el.get('fill')}")
    if len(puntas) != len(M["puntas"]):
        freno("colores", f"{len(puntas)} puntas con relación declarada, {len(M['puntas'])} dibujadas")
    rotulos = [el for el in raiz.iter(ns + "text") if el.get("stroke") == "#ffffff"]
    for el in rotulos:
        esperado = RESALTE if el.text in D["relaciones_nuevas"] else E["gris_rotulo"]
        if el.get("fill") != esperado:
            freno("colores", f"el rótulo «{el.text}» va en {el.get('fill')}, no en {esperado}")
    cajas = [el for el in raiz.iter(ns + "rect") if el.get("data-caja")]
    for el in cajas:
        nueva = el.get("data-caja") in D["tipos_nuevos"]
        if (el.get("stroke") == RESALTE) != nueva:
            freno("colores", f"la caja {el.get('data-caja')} {'no ' if nueva else ''}lleva el magenta")
    return dict(lineas=len(lineas), puntas=len(puntas), rotulos=len(rotulos), cajas=len(cajas),
                rotulos_magenta=sorted({el.text for el in rotulos if el.get("fill") == RESALTE}),
                cajas_magenta=sorted(el.get("data-caja") for el in cajas
                                     if el.get("stroke") == RESALTE))
# ========================================================================== #
# Emisión del SVG                                                            #
# ========================================================================== #
def f(v: float) -> str:
    s = f"{v:.2f}".rstrip("0").rstrip(".")
    return s if s not in ("-0", "") else "0"


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def texto_svg(s, x, y, fs, familia, color, anchor="start", peso="normal", rot=0,
              estilo="", halo=False) -> str:
    tr = f' transform="rotate({rot} {f(x)} {f(y)})"' if rot else ""
    extra = f' font-style="{estilo}"' if estilo else ""
    h = (' stroke="#ffffff" stroke-width="3.5" paint-order="stroke" stroke-linejoin="round"'
         if halo else "")
    return (f'<text x="{f(x)}" y="{f(y)}" font-size="{fs}" font-family="{familia}" '
            f'fill="{color}" text-anchor="{anchor}" font-weight="{peso}"{extra}{h}{tr}>'
            f'{esc(s)}</text>')


def punta_svg(p, color) -> str:
    pts = " ".join(f"{f(a)},{f(b)}" for a, b in triangulo(p["punto"], p["dir"]))
    dato = f' data-pred="{p["pred"]}"' if p.get("pred") else ""
    return f'<polygon points="{pts}" fill="{color}"{dato}/>'


def fichas(firmas) -> str:
    return " ".join(f"{d}>{r}" for _, d, r in sorted(firmas))


def corridas(tramos) -> list[dict]:
    """Funde tramos colineales contiguos con la misma red, color y firmas."""
    grupos: dict = {}
    for t in tramos:
        horiz = t["a"][1] == t["b"][1]
        clave = (t["red"], t["nuevo"], frozenset(t["firmas"]), horiz,
                 t["a"][1] if horiz else t["a"][0])
        grupos.setdefault(clave, []).append(t)
    res = []
    for (red, nuevo, firmas, horiz, _), lista in sorted(grupos.items(), key=lambda kv: str(kv[0])):
        o = 0 if horiz else 1
        lista = sorted(lista, key=lambda t: min(t["a"][o], t["b"][o]))
        actual = None
        for t in lista:
            lo, hi = sorted((t["a"], t["b"]), key=lambda p: p[o])
            if actual and actual["b"] == lo:
                actual["b"] = hi
            else:
                actual = dict(t, a=lo, b=hi)
                res.append(actual)
    return sorted(res, key=lambda t: (t["nuevo"], t["pred"], t["a"], t["b"]))




def dibujar(M, D, rep) -> str:
    E = M["estilo"]
    alto_cm = ANCHO_CM * H / W
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{ANCHO_CM:g}cm" height="{alto_cm:.3f}cm" '
           f'viewBox="0 0 {W} {H}" font-family="{E["sans"]}">',
           f'<rect x="0" y="0" width="{W}" height="{H}" fill="white"/>']
    for z in M["zonas"]:
        out.append(f'<rect x="{f(z["x0"])}" y="{f(z["y0"])}" width="{f(z["x1"] - z["x0"])}" '
                   f'height="{f(z["y1"] - z["y0"])}" fill="{E["fondo_zona"]}" '
                   f'stroke="{E["borde_zona"]}" rx="8" data-grupo="{z["nombre"]}" '
                   f'data-cajas="{" ".join(MIEMBROS[z["nombre"]])}"/>')
        for s, x, y in z["lineas"]:
            out.append(texto_svg(s, x, y, E["fs_zona"], E["sans"], E["gris_rotulo"], estilo="italic"))

    # Trazos sólidos, todos en el gris de la partida (versión 3).
    for t in corridas([t for t in rep["tramos"] if t["estilo"] == "solido"]):
        col = M["color_lineas"].get(t["pred"], E["gris_arista"])
        wd = E["grosor_arista"]
        out.append(f'<path d="M {f(t["a"][0])} {f(t["a"][1])} L {f(t["b"][0])} {f(t["b"][1])}" '
                   f'fill="none" stroke="{col}" stroke-width="{f(wd)}" data-pred="{t["pred"]}" '
                   f'data-firmas="{fichas(t["firmas"])}"/>')
    # remite_a: cada polilínea en un solo path, para que el discontinuo no se corte.
    for pts, destino in TRAZOS_REMITE:
        d = "M " + " L ".join(f"{f(x)} {f(y)}" for x, y in pts)
        hacia = (["grupo", D["to"]] if destino is None else
                 ["grupo"] if destino == GRUPO else [destino])
        fi = " ".join(f"grupo&gt;{h}" for h in hacia)
        col = M["color_lineas"].get(D["remite_a"], E["gris_arista"])
        out.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{f(E["grosor_arista"])}" '
                   f'stroke-dasharray="{DASH}" data-pred="{D["remite_a"]}" data-firmas="{fi}"/>')
    for p in M["puntas"]:
        out.append(punta_svg(p, M["color_lineas"].get(p["pred"], E["gris_arista"])))

    # Cajas, nombres y marcas de umbrales.
    for n in sorted(M["cajas"]):
        c = M["cajas"][n]
        dash = f' stroke-dasharray="{c["discontinua"]}"' if c["discontinua"] else ""
        out.append(f'<rect x="{f(c["x"])}" y="{f(c["y"])}" width="{f(c["w"])}" height="{f(c["h"])}" '
                   f'fill="{c["relleno"]}" stroke="{c["borde"]}" stroke-width="{f(c["grosor"])}"'
                   f'{dash} rx="{f(c["rx"])}" data-caja="{n}"/>')
        out.append(texto_svg(n, c["x"] + c["w"] / 2, c["y"] + E["dy_nombre"], E["fs_nodo"], E["mono"],
                             E["tinta"], anchor="middle", peso="bold"))
    n = M["nota"]
    out.append(texto_svg(n["texto"], n["x"], n["y"], E["fs_zona"], E["sans"], E["gris_rotulo"],
                         anchor=n["anchor"], estilo="italic"))
    for m in M["marcas"]:
        out.append(marca_svg(m["x"], m["y"], m["caja"], E))

    # Rótulos de relación, con halo blanco, encima de todo.
    for r in M["rotulos"]:
        nueva = r["texto"] in D["relaciones_nuevas"]
        out.append(texto_svg(r["texto"], r["x"], r["y"], E["fs_rotulo"], E["mono"],
                             RESALTE if nueva else E["gris_rotulo"], anchor=r["anchor"],
                             rot=r["rot"], halo=True))

    # Leyenda.
    for fila in M["leyenda"]:
        y, xm = fila["y"], fila["xm"]
        if fila["clave"] == "agregado":
            out.append(f'<rect x="{xm}" y="{y - 9}" width="26" height="18" '
                       f'fill="{hex_mix(RESALTE, MEZCLA_RELLENO_NUEVO)}" stroke="{RESALTE}" '
                       f'stroke-width="{f(GROSOR_RESALTE)}" rx="4"/>')
            out.append(texto_svg(LEYENDA_MUESTRA_ROTULO, xm + LEYENDA_MUESTRA_DX, y + 5, FS_LEYENDA,
                                 E["mono"], RESALTE))
        elif fila["clave"] == "derivada":
            out.append(f'<line x1="{xm}" y1="{y}" x2="{xm + 76}" y2="{y}" stroke="{E["gris_arista"]}" '
                       f'stroke-width="{f(E["grosor_arista"])}" stroke-dasharray="{DASH}"/>')
            out.append(punta_svg(dict(punto=(xm + 76, y), dir="right"), E["gris_arista"]))
        else:
            out.append(marca_svg(xm, y - MARCA["lado"] / 2, None, E))
        for i, trozos in enumerate(fila["lineas"]):
            yl = y + 5 + i * LEYENDA_INTERLINEA
            tsp = "".join(f'<tspan font-family="{E["mono"] if mono else E["sans"]}">{esc(s)}</tspan>'
                          for s, mono in trozos)
            dato = (f' data-tipos="{" ".join(sorted(fila["tipos"]))}"'
                    if fila["clave"] == "derivada" and i == 1 else "")
            out.append(f'<text x="{f(fila["xt"])}" y="{f(yl)}" font-size="{FS_LEYENDA}" '
                       f'font-family="{E["sans"]}" fill="{E["tinta"]}" text-anchor="start" '
                       f'xml:space="preserve"{dato}>{tsp}</text>')
    out.append("</svg>")
    return "\n".join(out) + "\n"


def marca_svg(x, y, caja, E) -> str:
    lado = MARCA["lado"]
    dato = f' data-umbrales="{caja}"' if caja else ""
    return (f'<g{dato}><rect x="{f(x)}" y="{f(y)}" width="{lado}" height="{lado}" rx="3" '
            f'fill="{COLOR_MARCA}"/>'
            + texto_svg(MARCA["texto"], x + lado / 2, y + lado / 2 + 5, MARCA["fs"], E["sans"],
                        "#ffffff", anchor="middle", peso="bold") + "</g>")


def releer_svg(svg: str, D: dict) -> None:
    """El SVG emitido, releído: sus atributos dan las 28 firmas, remite_a, los
    grupos con sus cajas, los tipos que nombra la leyenda y la marca de umbrales."""
    ns = "{http://www.w3.org/2000/svg}"
    raiz = ET.fromstring(svg)
    firmas, remite = set(), set()
    for el in raiz.iter(ns + "path"):
        pred = el.get("data-pred")
        for ficha in el.get("data-firmas", "").split():
            d, r = ficha.split(">")
            if pred == D["remite_a"]:
                remite.add((d, r))
            else:
                firmas.add((pred, d, r))
    if firmas != D["firmas"]:
        freno("firmas", f"el SVG releído da {len(firmas)} firmas, no las {len(D['firmas'])} del código")
    if remite != {("grupo", "grupo"), ("grupo", D["to"])}:
        freno("firmas", f"el SVG releído no dibuja {D['remite_a']} como se declara: {sorted(remite)}")
    grupos = {el.get("data-grupo"): tuple(el.get("data-cajas").split())
              for el in raiz.iter(ns + "rect") if el.get("data-grupo")}
    if grupos != dict(MIEMBROS):
        freno("grupos", f"el SVG releído declara los grupos {grupos}")
    ley = [el for el in raiz.iter(ns + "text") if el.get("data-tipos")]
    if len(ley) != 1 or sorted(ley[0].get("data-tipos").split()) != sorted(D["contenido"]):
        freno("firmas", "el SVG releído no nombra en la leyenda los tipos de contenido del código")
    nombrados = [t.text for t in ley[0].iter(ns + "tspan") if t.get("font-family") != raiz.get("font-family")]
    if sorted(nombrados) != sorted(D["contenido"]):
        freno("firmas", f"la leyenda releída nombra {nombrados}")
    marcas = sorted(el.get("data-umbrales") for el in raiz.iter(ns + "g") if el.get("data-umbrales"))
    if marcas != sorted(D["umbrales"]):
        freno("firmas", f"marcas de umbrales en {marcas}, el código dice {sorted(D['umbrales'])}")
    visibles = " ".join("".join(el.itertext()) for el in raiz.iter(ns + "text")).lower()
    for prohibido in (r"\bsha\b", r"\.py\b", r"\.json\b", r"\br2\b", r"\bcongelado\b"):
        if re.search(prohibido, visibles):
            freno("textos", f"nombre interno {prohibido!r} en texto visible")
# ========================================================================== #
# Exportación                                                                #
# ========================================================================== #
SOURCE_DATE_EPOCH = "0"


def grabar_densidad(ruta: str, dpi: int) -> None:
    """Inserta el bloque pHYs (píxeles por metro) después de IHDR."""
    with open(ruta, "rb") as fh:
        datos = fh.read()
    firma, resto = datos[:8], datos[8:]
    bloques, i = [], 0
    while i < len(resto):
        largo = struct.unpack(">I", resto[i:i + 4])[0]
        bloques.append((resto[i + 4:i + 8], resto[i:i + 12 + largo]))
        i += 12 + largo
    ppm = round(dpi / 0.0254)
    cuerpo = b"pHYs" + struct.pack(">IIB", ppm, ppm, 1)
    phys = struct.pack(">I", 9) + cuerpo + struct.pack(">I", zlib.crc32(cuerpo) & 0xFFFFFFFF)
    salida = firma
    for tipo, crudo in bloques:
        if tipo == b"pHYs":
            continue
        salida += crudo
        if tipo == b"IHDR":
            salida += phys
    with open(ruta, "wb") as fh:
        fh.write(salida)


def png_dimensiones(ruta: str) -> tuple[int, int]:
    with open(ruta, "rb") as fh:
        cab = fh.read(24)
    return struct.unpack(">II", cab[16:24])


def pdf_mediabox(ruta: str) -> tuple[float, float]:
    """MediaBox de la página, buscada en claro y en los flujos comprimidos."""
    with open(ruta, "rb") as fh:
        datos = fh.read()
    textos = [datos]
    for m in re.finditer(rb"stream\r?\n", datos):
        fin = datos.find(b"endstream", m.end())
        try:
            textos.append(zlib.decompress(datos[m.end():fin]))
        except zlib.error:
            pass
    for t in textos:
        m = re.search(rb"/MediaBox\s*\[\s*([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s*\]", t)
        if m:
            x0, y0, x1, y1 = (float(v) for v in m.groups())
            return (x1 - x0, y1 - y0)
    freno("exportacion", "el PDF no declara su MediaBox")


def exportar(ruta_svg: str, ruta_png: str, ruta_pdf: str) -> None:
    rsvg = shutil.which("rsvg-convert")
    if not rsvg:
        freno("exportacion", "rsvg-convert no está instalado: no se escriben el PNG ni el PDF")
    subprocess.run([rsvg, "-w", str(ANCHO_PNG_PX), "-f", "png", "-o", ruta_png, ruta_svg], check=True)
    grabar_densidad(ruta_png, DPI)
    entorno = dict(os.environ, SOURCE_DATE_EPOCH=SOURCE_DATE_EPOCH)
    subprocess.run([rsvg, "-f", "pdf", "-o", ruta_pdf, ruta_svg], check=True, env=entorno)


# ========================================================================== #
# Pruebas negativas                                                          #
# ========================================================================== #
def _mut_caja_fuera_de_grupo(M):
    M["cajas"]["Potestad"]["x"] = 330.0


def _mut_linea_no_gris(M):
    M["color_lineas"]["condicion_de"] = RESALTE


def _mut_rotulo_sobre_caja(M):
    r = next(r for r in M["rotulos"] if r["texto"] == "limita")
    c = M["cajas"]["Operacion"]
    r["x"], r["y"] = c["x"] + c["w"] / 2, c["y"] + 28


def _mut_tramo_diagonal(M):
    t = next(t for t in M["trazos"] if t["pred"] == "establecida_en" and t["a"] == (90.0, 550.0))
    t["a"] = (t["a"][0], t["a"][1] + 20)


def _mut_firma_de_mas(M):
    M["trazos"].append(dict(pred="condicion_de", a=(292.0, 613.0), b=(620.0, 613.0),
                            estilo="solido", origen="mutacion", firma=None))
    M["puntas"].append(dict(pred="condicion_de", punto=(620.0, 613.0), dir="right",
                            caja="Definicion", estilo="solido", firma=None))


def _mut_firma_de_menos(M):
    M["trazos"] = [t for t in M["trazos"]
                   if not (t["pred"] == "aplica_a" and t["a"] == (90.0, 440.0))]


# mutación → (función, control que tiene que frenar, textos que el freno tiene que nombrar)
MUTACIONES = {
    "caja_fuera_de_grupo": (_mut_caja_fuera_de_grupo, "grupos",
                            ("la caja Potestad está fuera de su grupo «izquierda»",)),
    "linea_no_gris": (_mut_linea_no_gris, "colores", ("la línea de condicion_de no es gris",)),
    "rotulo_sobre_caja": (_mut_rotulo_sobre_caja, "textos", ("«limita»", "Operacion")),
    "tramo_diagonal": (_mut_tramo_diagonal, "trazado", ("tramo diagonal de establecida_en",)),
    "firma_de_mas": (_mut_firma_de_mas, "firmas",
                     ("firmas de más en el dibujo: [('condicion_de', 'Condicion', 'Definicion')]",)),
    "firma_de_menos": (_mut_firma_de_menos, "firmas",
                       ("firmas de menos en el dibujo: [('aplica_a', 'Excepcion', 'Sujeto')]",)),
}


def probar_mutacion(nombre, M, D) -> str:
    funcion, control, esperado = MUTACIONES[nombre]
    M2 = copy.deepcopy(M)
    funcion(M2)
    try:
        verificar(M2, D)
    except Freno as e:
        msg = str(e)
        if not msg.startswith(f"[{control}]") or not all(e in msg for e in esperado):
            freno("pruebas", f"la mutación {nombre} frenó en otro control: {msg}")
        return msg
    freno("pruebas", f"la mutación {nombre} no frenó")


# ========================================================================== #
# Principal                                                                  #
# ========================================================================== #
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--salida", default=AQUI,
                    help="directorio del SVG, el PNG y el PDF (por omisión, el del script)")
    ap.add_argument("--mutacion", choices=sorted(MUTACIONES),
                    help="inyecta un defecto: el generador tiene que frenar sin escribir nada")
    args = ap.parse_args()
    try:
        D = leer_datos()
        P = leer_partida(D)
        M = armar_modelo(D, P)
        base = copy.deepcopy(M)
        if args.mutacion:
            MUTACIONES[args.mutacion][0](M)
            verificar(M, D)
            print(f"ERROR: la mutación {args.mutacion} no frenó")
            return 2
        rep = verificar(M, D)
        negativas = {n: probar_mutacion(n, base, D) for n in sorted(MUTACIONES)}
        svg = rep["svg"]
        releer_svg(svg, D)
    except Freno as e:
        print(f"FRENO {e}")
        print("No se escribe nada.")
        return 1

    print("FUENTES (sha256 comprobado):")
    for clave, (rel, sha) in FUENTES.items():
        print(f"  {clave:16s} {rel}  {sha}")
    print("LÍNEAS DE LAS FUENTES:")
    for k, v in sorted(D["lineas"].items()):
        print(f"  {k}: {v}")
    print(f"DATOS: {len(D['tipos'])} tipos + Sujeto; {len(D['predicados'])} relaciones; "
          f"{len(D['firmas'])} firmas = {len(D['congeladas'])} congeladas + {len(D['ampliacion'])} "
          f"de la ampliación; {D['remite_a']}: {len(D['firmas_remite'])} firmas; umbrales en "
          f"{', '.join(D['umbrales'])}")
    print(f"  relaciones nuevas respecto de la partida (rótulo en magenta): "
          f"{', '.join(D['relaciones_nuevas'])}")
    print(f"  respecto de la partida: tipos nuevos {', '.join(D['tipos_nuevos'])}; "
          f"{len(D['firmas_nuevas'])} firmas nuevas")
    for p, d, r in sorted(D["firmas_nuevas"]):
        print(f"      {p:15s} {d} → {r}")
    print("REDES (fuentes → puntas):")
    for red in rep["redes"]:
        fu = ", ".join(sorted({c for c, _ in red["fuentes"]}))
        pu = ", ".join(sorted(p["caja"] for p in red["puntas"]))
        print(f"  {red['pred']:15s} {red['estilo']:11s} {fu} → {pu}  ({len(red['firmas'])} firmas)")
    print("GRUPOS (cada caja dentro del suyo y de ningún otro):")
    for g, cajas in rep["grupos"].items():
        print(f"      {g:18s} {', '.join(cajas)}")
    tipos_ley = next(f for f in M["leyenda"] if f["clave"] == "derivada")["tipos"]
    print(f"FIRMAS DIBUJADAS: {len(rep['dibujadas'])} = las del código; "
          f"{D['remite_a']}: lazo en el grupo de la izquierda y flecha a {D['to']}, la leyenda nombra "
          f"{len(tipos_ley)} tipos ({', '.join(tipos_ley)}) → {len(rep['remite_dibujada'])} firmas "
          f"= las del código")
    print(f"TRAZOS DE LA PARTIDA CONSERVADOS, TRASLADADOS: "
          f"{', '.join(f'{p} {d}→{r}' for p, d, r in sorted(M['conservadas']))}")
    print(f"CRUCES entre flechas de redes distintas: {len(rep['cruces'])}, exactamente los declarados")
    for p in sorted(rep["cruces"]):
        print(f"      ({p[0]:g}, {p[1]:g})  {CRUCES_DECLARADOS[p]}")
    print("RÓTULOS: distancia a su red / a la red ajena más cercana")
    for (s, x, y), (dp, aj, da) in sorted(rep["cercania"].items()):
        print(f"      {s:15s} ({x:g}, {y:g})  {dp:4.1f} px / {da:5.1f} px ({aj})")
    print(f"TEXTOS: {len(rep['textos'])}; letra mínima {rep['pt_minimo']:.2f} pt impresos; "
          f"margen mínimo {rep['margen_min_mm']:.2f} mm")
    c = rep["colores"]
    print(f"COLORES: {c['lineas']} líneas y {c['puntas']} puntas de relación, todas en gris; rótulos "
          f"en magenta: {', '.join(c['rotulos_magenta'])} (de {c['rotulos']}); cajas en magenta: "
          f"{', '.join(c['cajas_magenta'])} (de {c['cajas']})")
    print("PRUEBAS NEGATIVAS (cada una frena en su control):")
    for n, msg in negativas.items():
        print(f"      {n:18s} {msg}")

    os.makedirs(args.salida, exist_ok=True)
    rutas = {ext: os.path.join(args.salida, f"{NOMBRE}.{ext}") for ext in ("svg", "png", "pdf")}
    with open(rutas["svg"], "w", encoding="utf-8", newline="\n") as fh:
        fh.write(svg)
    try:
        exportar(rutas["svg"], rutas["png"], rutas["pdf"])
        mb = pdf_mediabox(rutas["pdf"])
    except Freno as e:
        print(f"FRENO {e}")
        return 1
    wpx, hpx = png_dimensiones(rutas["png"])
    print(f"TAMAÑO: lienzo {W} × {H}; impreso {ANCHO_CM:.2f} × {ANCHO_CM * H / W:.2f} cm; "
          f"PNG {wpx} × {hpx} px a {DPI} dpi; PDF {mb[0]:.2f} × {mb[1]:.2f} pt "
          f"({mb[0] / PT_POR_CM:.2f} × {mb[1] / PT_POR_CM:.2f} cm)")
    for ext in ("svg", "png", "pdf"):
        print(f"{ext.upper()}: {rutas[ext]}  sha256 {sha256(rutas[ext])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
