#!/usr/bin/env python3
"""Figura «la salida del extractor para el ejemplo» (capítulo 4, sección 4.2), versión 3.

Lo que devolvió el extractor para la unidad del punto 5.1.1.1 de Clasificación
de deudores, el ejemplo que recorre la tesis, dibujado como lo que es en el
capítulo de construcción: un fragmento de grafo. Una caja por entidad, con su
tipo en negrita y su etiqueta debajo; una caja por sujeto del catálogo al que
llega una relación, con su nombre legible; una flecha por relación, de origen a
destino, rotulada con su nombre. La figura no tiene panel de la unidad (el texto
de entrada está en la figura de las unidades, sección 3.2), no marca
deformaciones ni errores y no lleva leyenda: cada caja dice su tipo.

Versión 1 (03/10/2026): el formato de la figura de la ficha (sección 3.8), con
la unidad a la izquierda y la lista de entidades y relaciones a la derecha.
Versión 2 (04/10/2026): el fragmento de grafo, con el estilo de la figura del
esquema final (sección 3.10, versión 3), sobre la salida del perfil del
esquema congelado (v3_b54).
Versión 3: la misma figura sobre la salida del perfil final (r2b) en la
re-extracción de la tanda 0; dibuja todas las entidades y relaciones de la
salida cruda, también la que el validador rechaza, sin marcarla. Esa salida no
trae relaciones con un sujeto, así que no hay caja de sujeto ni se lee el
catálogo.

Nada del contenido se tipea ni se supone (con candado de sha256):
- la extracción es el `tool_input_crudo` del único registro de la unidad en el
  archivo de registros de E1 que se pasa con --registro y --sha256 (por
  omisión, el de la re-extracción de la tanda 0 con el perfil r2b); si el
  archivo tiene cero o más de un registro de la unidad, el script frena; las
  omisiones, los tramos y los umbrales de la salida no son entidades ni
  relaciones: no se dibujan y el script los informa;
- el nombre de cada sujeto, si la salida trae relaciones con uno, es el
  `label` de su entrada en el catálogo de sujetos que se pasa con --catalogo y
  --sha256-catalogo (por omisión, el catálogo v3); el catálogo se lee solo en
  ese caso; el identificador interno no se dibuja;
- el estilo de cada caja (relleno, borde, grosor, esquinas y la discontinua
  del sujeto), la tipografía de tipos y rótulos, el gris y el grosor de las
  flechas se leen de figura_esquema_final.svg (versión 3); las puntas son las
  de su generador;
- las etiquetas, los tipos y los nombres de las relaciones se dibujan como los
  devolvió el modelo, envueltos por palabras en el ancho de la caja, sin
  abreviar.
La disposición (DISPOSICION y RUTAS) es la de este registro: cada entidad, cada
sujeto y cada relación tiene su lugar declarado, y cada relación su recorrido
y el lugar de su rótulo; si el registro trae una que no lo tiene, el script
frena (regenerar con otra corrida pide una disposición nueva).

Controles, en cada corrida (el script frena si fallan):
- inventario: el SVG se relee y, solo desde su geometría, se rearman las cajas
  (tipo y etiqueta) y las relaciones (la caja donde empieza cada flecha, la
  caja donde termina su punta y el rótulo más cercano); tienen que ser
  exactamente las entidades del registro, los sujetos que nombra y sus
  relaciones, sin ninguna de menos ni de más;
- contenido: lo dibujado reconstruye cada texto de su fuente; ningún texto
  lleva identificadores internos (locales, de sujeto o de unidad), nombres de
  archivo ni hashes;
- textos: ninguno por debajo de 7 pt impresos a 15 cm; tipo y etiqueta dentro
  de su caja; ningún texto superpuesto a otro; ningún rótulo (con su halo)
  toca una línea, una punta o una caja; cada rótulo queda a 6 o menos de su
  flecha y al menos 5 más lejos de cualquier otra;
- cajas: no se cruzan y quedan a 10 o más entre sí;
- trazos: ningún tramo diagonal ni elemento girado en el SVG;
- flechas: cada una empieza en el borde de su caja de origen y su punta
  termina en el borde de la de destino; ningún tramo atraviesa una caja;
  ninguna punta toca otra caja; tramos paralelos de flechas distintas a 10 o
  más;
- cruces: entre flechas distintas solo cruces en X, contados, y tienen que ser
  exactamente CRUCES_DECLARADOS (ninguno);
- margen: nada a menos de 2 mm de un borde;
- registro: cada elemento del SVG está registrado en los controles anteriores.
Antes de componer la figura, el script corre cinco pruebas negativas (una
relación de más, una entidad de menos, un rótulo sobre una caja, un tramo
diagonal y un cruce de flechas) y frena si alguna no hace fallar el control
que le corresponde. Con --perturbar <caso> compone la figura con ese defecto:
los controles fallan y no se escribe nada.

Reutiliza por importación, sin modificarlo, generar_figura_esquema_final.py
(el tamaño de 15 cm sobre 850 unidades, el texto con halo, las puntas, la
medida de Menlo, la geometría de tramos y textos, el conteo de cruces y la
exportación) y, de generar_figura_proceso_extraccion.py, el medidor con las
métricas reales de Helvetica para las etiquetas.

Salidas, byte-reproducibles: figura_extractor_ejemplo.svg, .png (300 dpi,
densidad grabada) y .pdf (fecha de creación fijada por SOURCE_DATE_EPOCH).

Uso (desde la raíz del repo):
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_extractor_ejemplo.py
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_extractor_ejemplo.py \\
        --registro <extracciones_e1.jsonl> --sha256 <sha256> [--catalogo <catalogo.json> \\
        --sha256-catalogo <sha256>] [--salida <directorio>]
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_extractor_ejemplo.py \\
        --perturbar {relacion_de_mas,entidad_de_menos,rotulo_sobre_caja,tramo_diagonal,cruce_de_flechas}
"""

import argparse
import hashlib
import json
import math
import os
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter

sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import generar_figura_esquema_final as EF            # noqa: E402
import generar_figura_proceso_extraccion as proc     # noqa: E402

RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", ".."))
NOMBRE = "figura_extractor_ejemplo"
NS = "{http://www.w3.org/2000/svg}"

# --------------------------------------------------------------------------- #
# Fuentes y candados                                                           #
# --------------------------------------------------------------------------- #
# Registros de E1 de la re-extracción de la tanda 0 con el perfil r2b
# (U-REEXT-T0, 3d793aa) para el documento del ejemplo; se reemplaza con
# --registro y --sha256.
REGISTRO_POR_OMISION = ("data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b/cla/extracciones_e1.jsonl",
                        "47bf7b584902fe396cc14a291f56fb61237c21a4ab8bd546422eb0a63d5fde59")
# Catálogo de sujetos del perfil v3_b54; se reemplaza con --catalogo y
# --sha256-catalogo.
CATALOGO_POR_OMISION = ("data/experiment/catalogo_unico/catalogo_sujetos_v3.json",
                        "9a2522e41e1086d26bb73a37070efd9913f98ec36e2f957e198b460d21ca6c58")
# Estilo: la figura del esquema final, versión 3.
ESTILO = ("docs/tesis/figuras/figura_esquema_final.svg",
          "dfdb16d471bb93c6351aa03b1e609452b75c428baa354c52354ce1dfe9797bb3")
UNIDAD = "cla::5.1.1.1"
SUJETO = "Sujeto"

# Claves del registro que se conocen; una clave fuera de estas listas frena el
# script: la figura no descarta en silencio algo que el modelo devolvió.
CLAVES_SALIDA = ("entities", "relations", "omisiones_no_prosa", "omisiones")
CLAVES_ENTIDAD = ("local_id", "type", "label", "punto", "properties", "tramo", "umbrales")
# Claves que la figura no dibuja (no son entidades ni relaciones): el script
# las informa.
NO_DIBUJADAS_SALIDA = ("omisiones_no_prosa", "omisiones")
NO_DIBUJADAS_ENTIDAD = ("punto", "properties", "tramo", "umbrales")
CLAVES_RELACION = ("source", "predicate", "target", "sujeto_id", "punto")

# Nada de esto puede aparecer en un texto dibujado.
PROHIBIDOS = (re.compile(r"::"), re.compile(r"Sujeto_"), re.compile(r"\be[0-9]+\b"),
              re.compile(r"\.(jsonl?|pdf|py|md|tex|db)\b"), re.compile(r"\b[0-9a-f]{7,64}\b"),
              re.compile(r"chunk|tanda|registro|v3_b54", re.I))

# --------------------------------------------------------------------------- #
# Tamaño y disposición                                                         #
# --------------------------------------------------------------------------- #
W = EF.W                                    # 850 unidades = 15 cm, como el esquema final
ANCHO_CM = EF.ANCHO_CM
PT_MINIMO = EF.PT_MINIMO
MARGEN_MM = EF.MARGEN_MM
MARGEN_MIN = MARGEN_MM * W / (ANCHO_CM * 10)          # 11,3 unidades
MARGEN = 14
FS_ETIQUETA = 15                            # el cuerpo de los rótulos y de las notas del esquema final
IL_ETIQUETA = 18
ASC_SANS, DESC_SANS = 0.78, 0.22            # caja del texto en Helvetica (la de la figura de la ficha)
CAJA_W = 230                                # ancho de caja: tres columnas en 15 cm
PAD_X, PAD_Y = 12, 9                        # aire interior de las cajas
SEP_TIPO = 6                                # del tipo a la etiqueta
CALLE_V = 58                                # entre filas: por acá corren las flechas verticales y sus rótulos
SEP_CAJAS = 10                              # mínimo entre cajas
JUNTO, MARGEN_AJENA = EF.JUNTO, EF.MARGEN_AJENA       # 6 y 5: rótulo junto a su flecha
HALO_AIRE = EF.HALO + EF.AIRE                          # 2,75: halo del rótulo y aire
DIST_ROTULO = 4.0                           # del rótulo a su flecha
DISTANCIA_PARALELAS = EF.DISTANCIA_PARALELAS           # 10
CRUCES_DECLARADOS = {}                      # ninguno

# Columnas y filas. La operación y el Texto Ordenado son los dos extremos a los
# que llegan las otras tres entidades: van en la fila del medio, a la
# izquierda y a la derecha, unidos por su establecida_en. Arriba, en el
# centro, la condición del monto; abajo, la excepción (debajo de la
# operación) y la condición del repago (en el centro).
X_COL = (MARGEN, (MARGEN + W - MARGEN - CAJA_W) / 2.0, W - MARGEN - CAJA_W)
CLAVE_SUJETO = "sujeto:Sujeto_rol_obligado_a_clasificar_clasificacion"   # versión 2; esta salida no trae sujetos
DISPOSICION = {"e3": (X_COL[1], 0),
               "e1": (X_COL[0], 1), "to": (X_COL[2], 1),
               "e2": (X_COL[0], 2), "e4": (X_COL[1], 2)}
CANAL = 24                                  # debajo de la fila de abajo, para la establecida_en de la excepción
ENTRADA = 20                                # de la altura media de la operación y del Texto Ordenado


def rutas_declaradas(C):
    """Recorrido y rótulo de cada relación, a partir de los rectángulos
    (x0, y0, x1, y1) de las cajas por identificador local. Rótulo: (tramo,
    lado, centro o None para el medio del tramo); los de los tramos
    verticales van en la calle entre filas."""
    m, o, t, x, r = C["e3"], C["e1"], C["to"], C["e2"], C["e4"]
    xo, xt = (o[0] + o[2]) / 2.0, (t[0] + t[2]) / 2.0
    ym_m, ym_o = (m[1] + m[3]) / 2.0, (o[1] + o[3]) / 2.0
    calle_01, calle_12 = (m[3] + o[1]) / 2.0, (o[3] + r[1]) / 2.0
    ya, yb = ym_o + ENTRADA, x[3] + CANAL
    return {
        # La condición del monto, por sus dos lados, baja a la operación y al
        # Texto Ordenado.
        ("e3", "condicion_de", "e1"): ([(m[0], ym_m), (xo, ym_m), (xo, o[1])], (1, "derecha", calle_01)),
        ("e3", "establecida_en", "to"): ([(m[2], ym_m), (xt, ym_m), (xt, t[1])], (1, "izquierda", calle_01)),
        # La operación, al Texto Ordenado, recta.
        ("e1", "establecida_en", "to"): ([(o[2], ym_o), (t[0], ym_o)], (0, "arriba", None)),
        # La condición del repago sube por la fila del medio y entra de costado
        # a la operación y al Texto Ordenado.
        ("e4", "condicion_de", "e1"): ([(r[0] + 20, r[1]), (r[0] + 20, ya), (o[2], ya)], (0, "derecha", calle_12)),
        ("e4", "establecida_en", "to"): ([(r[2] - 20, r[1]), (r[2] - 20, ya), (t[0], ya)], (0, "derecha", calle_12)),
        # La excepción sube recta a la operación y llega al Texto Ordenado por
        # debajo de la fila de abajo.
        ("e2", "exceptua", "e1"): ([(xo, x[1]), (xo, o[3])], (0, "derecha", None)),
        ("e2", "establecida_en", "to"): ([(xo, x[3]), (xo, yb), (xt, yb), (xt, t[3])],
                                         (2, "izquierda", (r[1] + r[3]) / 2.0)),
    }


RUTAS = tuple(rutas_declaradas({k: (0, 0, 1, 1) for k in DISPOSICION}))


def freno(motivo):
    raise SystemExit(f"FRENO: {motivo}")


# --------------------------------------------------------------------------- #
# Fuentes                                                                      #
# --------------------------------------------------------------------------- #
def leer_con_candado(rel, esperado):
    ruta = rel if os.path.isabs(rel) else os.path.join(RAIZ, rel)
    with open(ruta, "rb") as fh:
        crudo = fh.read()
    sha = hashlib.sha256(crudo).hexdigest()
    if sha != esperado:
        freno(f"{rel} no es el verificado: sha256 {sha} ≠ {esperado}")
    return crudo


def leer_estilo():
    """Estilo de la figura del esquema final: cajas por tipo, tipografía de
    tipos y rótulos, gris y grosor de las flechas; cada uno tiene que ser
    único en esa figura."""
    raiz = ET.fromstring(leer_con_candado(*ESTILO).decode("utf-8"))
    cajas = {}
    for el in raiz.iter(NS + "rect"):
        t = el.get("data-caja")
        if t:
            if t in cajas:
                freno(f"la figura del esquema final tiene dos cajas {t}")
            cajas[t] = {"relleno": el.get("fill"), "borde": el.get("stroke"),
                        "grosor": float(el.get("stroke-width")), "rx": float(el.get("rx")),
                        "discontinua": el.get("stroke-dasharray")}
    textos = list(raiz.iter(NS + "text"))
    nombres = {(t.get("font-family"), t.get("font-size"), t.get("fill")) for t in textos
               if t.get("font-weight") == "bold" and t.text in cajas}
    # Rótulos: el gris de la figura; el magenta (EF.RESALTE) marca allí las
    # relaciones agregadas respecto de la partida, y esta figura no marca nada.
    rotulos = {(t.get("font-family"), t.get("font-size"), t.get("fill"), t.get("stroke"))
               for t in textos if t.get("stroke") and t.get("fill") != EF.RESALTE}
    lineas = {(p.get("stroke"), p.get("stroke-width")) for p in raiz.iter(NS + "path")}
    puntas = {p.get("fill") for p in raiz.iter(NS + "polygon")}
    if len(nombres) != 1 or len(rotulos) != 1 or len(lineas) != 1 or len(puntas) != 1:
        freno("el estilo de nombres, rótulos o flechas de la figura del esquema final no es único: "
              f"{nombres} {rotulos} {lineas} {puntas}")
    (mono, fs_tipo, tinta), = nombres
    (mono_r, fs_rotulo, gris_rotulo, halo), = rotulos
    (gris, grosor), = lineas
    if puntas != {gris} or halo != "#ffffff" or mono_r != mono:
        freno("las puntas, el halo o la tipografía de los rótulos de la figura del esquema final no son "
              "los esperados")
    return {"cajas": cajas, "sans": raiz.get("font-family"), "mono": mono, "fs_tipo": int(fs_tipo),
            "tinta": tinta, "fs_rotulo": int(fs_rotulo), "gris_rotulo": gris_rotulo,
            "gris": gris, "grosor": float(grosor)}


def resolver(args):
    """Lee las fuentes con su candado y devuelve lo que la figura dibuja."""
    crudo = leer_con_candado(args.registro, args.sha256).decode("utf-8")
    regs = [(n, json.loads(s)) for n, s in enumerate(crudo.split("\n"), start=1) if s.strip()]
    de_la_unidad = [(n, r) for n, r in regs if r.get("chunk_id") == UNIDAD]
    if len(de_la_unidad) != 1:
        freno(f"el archivo de registros tiene {len(de_la_unidad)} registros de {UNIDAD}, no uno "
              f"(líneas {[n for n, _ in de_la_unidad]})")
    linea, reg = de_la_unidad[0]
    if reg.get("error") is not None or reg.get("stop_reason") != "tool_use":
        freno(f"el registro de {UNIDAD} tiene error {reg.get('error')!r} o stop_reason "
              f"{reg.get('stop_reason')!r}")
    ext = reg.get("tool_input_crudo")
    if not isinstance(ext, dict) or not isinstance(ext.get("entities"), list) \
            or not isinstance(ext.get("relations"), list):
        freno("el registro no tiene una salida cruda con listas de entidades y de relaciones")
    extra = sorted(k for k in ext if k not in CLAVES_SALIDA)
    if extra:
        freno(f"la salida cruda tiene claves no previstas {extra}")
    no_dibujado = [(k, ext[k]) for k in NO_DIBUJADAS_SALIDA if ext.get(k)]
    nodos = {}
    for i, e in enumerate(ext["entities"]):
        extra = sorted(k for k in e if k not in CLAVES_ENTIDAD)
        if extra:
            freno(f"entidad {i + 1}: claves no previstas {extra}")
        if not all(isinstance(e.get(k), str) and e[k] for k in ("local_id", "type", "label")):
            freno(f"entidad {i + 1}: sin identificador, tipo o etiqueta")
        if e["local_id"] in nodos:
            freno(f"identificador local repetido: {e['local_id']}")
        nodos[e["local_id"]] = {"tipo": e["type"], "etiqueta": e["label"]}
        no_dibujado += [(f"{e['local_id']}.{k}", e[k]) for k in NO_DIBUJADAS_ENTIDAD if e.get(k)]

    # Sujetos: el nombre legible de su entrada en el catálogo, que se lee solo
    # si alguna relación llega a un sujeto.
    if any("sujeto_id" in r for r in ext["relations"]):
        crudo_cat = leer_con_candado(args.catalogo, args.sha256_catalogo).decode("utf-8")
        cat, lineas_cat = json.loads(crudo_cat), crudo_cat.split("\n")
    relaciones, sujetos = [], {}
    for i, r in enumerate(ext["relations"]):
        extra = sorted(k for k in r if k not in CLAVES_RELACION)
        if extra:
            freno(f"relación {i + 1}: claves no previstas {extra}")
        destinos = [k for k in ("target", "sujeto_id") if k in r]
        if "source" not in r or len(destinos) != 1:
            freno(f"relación {i + 1}: forma no prevista {sorted(r)}")
        if "sujeto_id" in r:
            sid = r["sujeto_id"]
            entradas = [s for s in cat["sujetos"] if s.get("id") == sid]
            if len(entradas) != 1 or not entradas[0].get("label"):
                freno(f"el catálogo tiene {len(entradas)} entradas con nombre para {sid}")
            if (entradas[0].get("estado") or {}).get("valor") != "vigente":
                freno(f"la entrada del catálogo de {sid} no está vigente")
            destino = f"sujeto:{sid}"
            n_id = [k for k, s in enumerate(lineas_cat, start=1) if f'"id": "{sid}"' in s]
            n_label = [k for k, s in enumerate(lineas_cat, start=1)
                       if s.strip() == f'"label": {json.dumps(entradas[0]["label"], ensure_ascii=False)},'
                       and n_id and n_id[0] < k <= n_id[0] + 3]
            sujetos[destino] = {"tipo": SUJETO, "etiqueta": entradas[0]["label"], "id": sid,
                                "lineas": n_id + n_label}
        else:
            destino = r["target"]
        if r["source"] not in nodos or (destino not in nodos and destino not in sujetos):
            freno(f"relación {i + 1}: origen o destino que no es una entidad ni un sujeto")
        relaciones.append({"origen": r["source"], "nombre": r["predicate"], "destino": destino})
    nodos.update(sujetos)
    if any(v > 1 for v in Counter((n["tipo"], n["etiqueta"]) for n in nodos.values()).values()):
        freno("dos cajas tendrían el mismo tipo y la misma etiqueta: la figura no las distinguiría")
    sin_lugar = sorted(set(nodos) ^ set(DISPOSICION))
    if sin_lugar:
        freno(f"la disposición no coincide con las cajas del registro: {sin_lugar}")
    claves_r = [(r["origen"], r["nombre"], r["destino"]) for r in relaciones]
    if sorted(claves_r) != sorted(RUTAS) or len(set(claves_r)) != len(claves_r):
        freno("las rutas declaradas no son exactamente las relaciones del registro")
    sha_linea = hashlib.sha256((crudo.split("\n")[linea - 1] + "\n").encode("utf-8")).hexdigest()
    return {"linea": linea, "n_regs": len(regs), "reg": reg, "ext": ext, "nodos": nodos,
            "relaciones": relaciones, "sujetos": sujetos, "no_dibujado": no_dibujado, "sha_linea": sha_linea}


# --------------------------------------------------------------------------- #
# Composición: todo lo que se dibuja queda registrado                          #
# --------------------------------------------------------------------------- #
REG = {"textos": [], "cajas": {}, "flechas": [], "dibujados": []}
MEDIR = None


def envolver(s, ancho, fs):
    lineas, actual = [], ""
    for palabra in s.split(" "):
        cand = palabra if not actual else actual + " " + palabra
        if actual and MEDIR(cand, fs, False) > ancho:
            lineas.append(actual)
            actual = palabra
        else:
            actual = cand
    lineas.append(actual)
    return lineas


def rect_texto(s, x, y, fs, mono, anchor):
    if mono:
        return EF.rect_texto(s, x, y, fs, anchor, 0, True)
    w = MEDIR(s, fs, False)
    dx = {"start": 0.0, "middle": -w / 2.0, "end": -w}[anchor]
    return (x + dx, y - ASC_SANS * fs, x + dx + w, y + DESC_SANS * fs)


def texto(partes, E, s, x, y, fs, mono, anchor, pieza, peso="normal", color=None, caja=None, halo=False):
    x, y = float(EF.f(x)), float(EF.f(y))
    partes.append(EF.texto_svg(s, x, y, fs, E["mono"] if mono else E["sans"], color or E["tinta"],
                               anchor=anchor, peso=peso, halo=halo))
    REG["dibujados"].append("text")
    REG["textos"].append({"s": s, "x": x, "y": y, "fs": fs, "mono": mono, "anchor": anchor,
                          "pieza": pieza, "caja": caja, "halo": halo,
                          "R": rect_texto(s, x, y, fs, mono, anchor)})


def alto_contenido(E, n_lineas):
    return E["fs_tipo"] + SEP_TIPO + (ASC_SANS + DESC_SANS) * FS_ETIQUETA + (n_lineas - 1) * IL_ETIQUETA


def geometria(res, E):
    """Cajas: tamaño común (el de la caja con más líneas) y lugar declarado."""
    ancho = CAJA_W - 2 * PAD_X
    lineas = {k: envolver(n["etiqueta"], ancho, FS_ETIQUETA) for k, n in res["nodos"].items()}
    alto = math.ceil(alto_contenido(E, max(len(v) for v in lineas.values())) + 2 * PAD_Y)
    filas = tuple(MARGEN + f * (alto + CALLE_V) for f in range(1 + max(f for _, f in DISPOSICION.values())))
    return {k: {"x": float(x), "y": float(filas[fila]), "w": float(CAJA_W), "h": float(alto),
                "lineas": lineas[k]} for k, (x, fila) in DISPOSICION.items()}, alto


# Relaciones que plantan las pruebas negativas (son las mismas en la figura del
# ensamblado, que las reutiliza).
RELACION_DE_MAS = ("e2", "regula", "e4")
RUTA_CON_CRUCE = ("e4", "condicion_de", "e1")      # sube por encima de la establecida_en de la operación
RUTA_DIAGONAL = ("e1", "establecida_en", "to")
ROTULO_SOBRE_CAJA = (("e1", "establecida_en", "to"), "to")


def perturbar_ruta(clave, pts, C, perturbacion):
    """Los recorridos de las pruebas negativas del cruce y del tramo diagonal."""
    if perturbacion == "cruce_de_flechas" and clave == RUTA_CON_CRUCE:
        o = C["e1"]
        y = (o[1] + o[3]) / 2.0 - ENTRADA
        return [pts[0], (pts[0][0], y), (o[2], y)]
    if perturbacion == "tramo_diagonal" and clave == RUTA_DIAGONAL:
        return [pts[0], (pts[-1][0], pts[-1][1] + 30)]
    return pts


def rutas(res, cajas, perturbacion):
    """Puntos de cada flecha y lugar de su rótulo."""
    lista = [(r["origen"], r["nombre"], r["destino"]) for r in res["relaciones"]]
    if perturbacion == "relacion_de_mas":
        lista.append(RELACION_DE_MAS)
    C = {k: (c["x"], c["y"], c["x"] + c["w"], c["y"] + c["h"]) for k, c in cajas.items()}
    declaradas = rutas_declaradas(C)
    out = []
    for i, clave in enumerate(lista):
        if clave in declaradas:
            pts, rotulo = declaradas[clave]
        else:
            a, b = C[clave[0]], C[clave[2]]
            ym = (a[1] + a[3]) / 2.0
            pts, rotulo = [(a[2], ym), (b[0], ym)], (0, "arriba", None)
        pts = perturbar_ruta(clave, pts, C, perturbacion)
        out.append({"i": i, "clave": clave, "pts": [(float(p), float(q)) for p, q in pts], "rotulo": rotulo})
    return out


def lugar_rotulo(fl, E):
    """Ancla y alineación del rótulo, junto al tramo declarado de su flecha:
    arriba de un tramo horizontal o al costado de uno vertical, a
    DIST_ROTULO, en el centro declarado o en el medio del tramo."""
    fs = E["fs_rotulo"]
    tramo, lado, centro = fl["rotulo"]
    p, q = fl["pts"][tramo], fl["pts"][tramo + 1]
    asc, desc = EF.ASC_MONO * fs, EF.DESC_MONO * fs
    if lado == "arriba":
        x = (p[0] + q[0]) / 2.0 if centro is None else centro
        return x, p[1] - DIST_ROTULO - desc, "middle"
    ym = ((p[1] + q[1]) / 2.0 if centro is None else centro) + (asc - desc) / 2.0
    if lado == "izquierda":
        return p[0] - DIST_ROTULO, ym, "end"
    return p[0] + DIST_ROTULO, ym, "start"


def textos_fijados(res):
    """Texto esperado de cada pieza dibujada, derivado de las fuentes."""
    t = {}
    for k, n in res["nodos"].items():
        t[("tipo", k)] = n["tipo"]
        t[("etiqueta", k)] = n["etiqueta"]
    for i, r in enumerate(res["relaciones"]):
        t[("rotulo", i)] = r["nombre"]
    return t


def componer(res, E, perturbacion=None):
    for k in ("textos", "flechas", "dibujados"):
        del REG[k][:]
    REG["cajas"].clear()
    T = textos_fijados(res)
    todas, alto = geometria(res, E)
    cajas = dict(todas)
    if perturbacion == "entidad_de_menos":
        del cajas["e1"]
    flechas = rutas(res, todas, perturbacion)
    partes = []
    # Flechas y puntas, debajo de las cajas (el orden de la figura del esquema final).
    for fl in flechas:
        d = "M " + " L ".join(f"{EF.f(x)} {EF.f(y)}" for x, y in fl["pts"])
        partes.append(f'<path d="{d}" fill="none" stroke="{E["gris"]}" stroke-width="{EF.f(E["grosor"])}"/>')
        REG["dibujados"].append("path")
        (xa, ya), (xb, yb) = fl["pts"][-2], fl["pts"][-1]
        direc = ("down" if yb > ya else "up") if xa == xb else ("right" if xb > xa else "left")
        partes.append(EF.punta_svg({"punto": (xb, yb), "dir": direc}, E["gris"]))
        REG["dibujados"].append("polygon")
        REG["flechas"].append(dict(fl, punta=EF.triangulo((xb, yb), direc)))
    # Cajas: tipo en negrita y etiqueta debajo, centrados.
    for k in sorted(cajas):
        c, n = cajas[k], res["nodos"][k]
        st = E["cajas"][n["tipo"]]
        dash = f' stroke-dasharray="{st["discontinua"]}"' if st["discontinua"] else ""
        partes.append(f'<rect x="{EF.f(c["x"])}" y="{EF.f(c["y"])}" width="{EF.f(c["w"])}" '
                      f'height="{EF.f(c["h"])}" fill="{st["relleno"]}" stroke="{st["borde"]}" '
                      f'stroke-width="{EF.f(st["grosor"])}"{dash} rx="{EF.f(st["rx"])}"/>')
        REG["dibujados"].append("rect")
        REG["cajas"][k] = {"R": (c["x"], c["y"], c["x"] + c["w"], c["y"] + c["h"]), "grosor": st["grosor"]}
        arriba = c["y"] + (c["h"] - alto_contenido(E, len(c["lineas"]))) / 2.0
        xm = c["x"] + c["w"] / 2.0
        texto(partes, E, T[("tipo", k)], xm, arriba + EF.ASC_MONO * E["fs_tipo"], E["fs_tipo"], True,
              "middle", ("tipo", k), peso="bold", caja=k)
        y0 = arriba + E["fs_tipo"] + SEP_TIPO + ASC_SANS * FS_ETIQUETA
        for j, s in enumerate(c["lineas"]):
            texto(partes, E, s, xm, y0 + j * IL_ETIQUETA, FS_ETIQUETA, False, "middle", ("etiqueta", k), caja=k)
    # Rótulos, con halo, encima de todo.
    for fl in flechas:
        x, y, anchor = lugar_rotulo(fl, E)
        if perturbacion == "rotulo_sobre_caja" and fl["clave"] == ROTULO_SOBRE_CAJA[0]:
            c = cajas[ROTULO_SOBRE_CAJA[1]]
            x, y, anchor = c["x"] + c["w"] / 2.0, c["y"] + c["h"] / 2.0, "middle"
        texto(partes, E, fl["clave"][1], x, y, E["fs_rotulo"], True, anchor, ("rotulo", fl["i"]),
              color=E["gris_rotulo"], halo=True)
    alto_total = math.ceil(max([c["y"] + c["h"] for c in todas.values()]
                               + [y for fl in flechas for _, y in fl["pts"]]) + MARGEN)
    cabeza = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{ANCHO_CM:g}cm" '
              f'height="{ANCHO_CM * alto_total / W:.3f}cm" viewBox="0 0 {W} {alto_total}" '
              f'font-family="{E["sans"]}">',
              f'<rect x="0" y="0" width="{W}" height="{alto_total}" fill="white"/>']
    return "\n".join(cabeza + partes + ["</svg>"]) + "\n", T, {"alto": alto_total, "alto_caja": alto}


# --------------------------------------------------------------------------- #
# Controles                                                                    #
# --------------------------------------------------------------------------- #
def numeros(s):
    return [float(x) for x in re.findall(r"-?\d+(?:\.\d+)?", s)]


def en_borde(p, R, tol=0.01):
    dentro = R[0] - tol <= p[0] <= R[2] + tol and R[1] - tol <= p[1] <= R[3] + tol
    return dentro and min(abs(p[0] - R[0]), abs(p[0] - R[2]), abs(p[1] - R[1]), abs(p[1] - R[3])) <= tol


def inventario_svg(svg, E):
    """Cajas y relaciones rearmadas solo desde la geometría del SVG: una caja
    por rectángulo (el texto en negrita es el tipo; el resto, la etiqueta);
    una relación por camino (la caja en cuyo borde empieza, la caja en cuyo
    borde está la punta y el rótulo más cercano, sin ambigüedad)."""
    cajas, textos, caminos, puntas, anomalias = [], [], [], [], []
    for el in list(ET.fromstring(svg))[1:]:
        tag = el.tag.replace(NS, "")
        if tag == "rect":
            x, y = float(el.get("x")), float(el.get("y"))
            cajas.append((x, y, x + float(el.get("width")), y + float(el.get("height"))))
        elif tag == "text":
            x, y, fs = float(el.get("x")), float(el.get("y")), float(el.get("font-size"))
            s = el.text or ""
            textos.append({"s": s, "x": x, "y": y, "negrita": el.get("font-weight") == "bold",
                           "halo": bool(el.get("stroke")),
                           "R": rect_texto(s, x, y, fs, el.get("font-family") == E["mono"],
                                           el.get("text-anchor"))})
        elif tag == "path":
            v = numeros(el.get("d"))
            caminos.append([(v[k], v[k + 1]) for k in range(0, len(v), 2)])
        elif tag == "polygon":
            v = numeros(el.get("points"))
            puntas.append((v[0], v[1]))
    nodos = []
    for R in cajas:
        dentro = sorted((t for t in textos if not t["halo"] and R[0] < t["x"] < R[2] and R[1] < t["y"] < R[3]),
                        key=lambda t: (t["y"], t["x"]))
        if not dentro or not dentro[0]["negrita"] or sum(t["negrita"] for t in dentro) != 1:
            anomalias.append(f"la caja en ({R[0]:g}, {R[1]:g}) no tiene un tipo arriba")
            nodos.append(None)
            continue
        nodos.append((dentro[0]["s"], " ".join(t["s"] for t in dentro[1:])))
    relaciones = []
    for pts in caminos:
        o = [k for k, R in enumerate(cajas) if en_borde(pts[0], R)]
        d = [k for k, R in enumerate(cajas) if en_borde(pts[-1], R)]
        if len(o) != 1 or len(d) != 1:
            anomalias.append(f"flecha de {pts[0]} a {pts[-1]}: {len(o)} caja(s) de origen y {len(d)} de destino")
            continue
        if pts[-1] not in puntas:
            anomalias.append(f"flecha de {pts[0]} a {pts[-1]} sin punta en su extremo")
        relaciones.append({"o": nodos[o[0]], "d": nodos[d[0]], "tramos": list(zip(pts, pts[1:])),
                           "rotulo": None})
    for t in (t for t in textos if t["halo"]):
        dist = sorted((min(EF.dist_rect_tramo(t["R"], a, b) for a, b in r["tramos"]), k)
                      for k, r in enumerate(relaciones))
        if not dist or (len(dist) > 1 and dist[1][0] < dist[0][0] + MARGEN_AJENA):
            anomalias.append(f"rótulo {t['s']!r} sin una flecha que sea, sin ambigüedad, la más cercana")
            continue
        r = relaciones[dist[0][1]]
        if r["rotulo"] is not None:
            anomalias.append(f"la flecha de {r['o']} a {r['d']} tiene dos rótulos")
        r["rotulo"] = t["s"]
    return [n for n in nodos if n], [(r["o"], r["rotulo"], r["d"]) for r in relaciones], anomalias


def controlar_inventario(svg, E, res):
    """Las cajas y las relaciones de la figura son exactamente las del
    registro (con sus sujetos), ni una de menos ni una de más."""
    cajas, relaciones, fallas = inventario_svg(svg, E)
    nodos = res["nodos"]
    par = {k: (n["tipo"], n["etiqueta"]) for k, n in nodos.items()}
    esperadas_c = list(par.values())
    esperadas_r = [(par[r["origen"]], r["nombre"], par[r["destino"]]) for r in res["relaciones"]]
    for nombre, dib, esp in (("caja", cajas, esperadas_c), ("relación", relaciones, esperadas_r)):
        for x in sorted((Counter(esp) - Counter(dib)).elements(), key=str):
            fallas.append(f"{nombre} del registro que no está en la figura: {x}")
        for x in sorted((Counter(dib) - Counter(esp)).elements(), key=str):
            fallas.append(f"{nombre} de la figura que no está en el registro: {x}")
    return fallas, cajas, relaciones


def controlar_contenido(T):
    """Lo dibujado reconstruye cada pieza y no lleva nada prohibido."""
    fallas, por_pieza = [], {}
    for r in REG["textos"]:
        por_pieza.setdefault(r["pieza"], []).append(r["s"])
        for rx in PROHIBIDOS:
            if rx.search(r["s"]):
                fallas.append(f"{r['s']!r} lleva {rx.pattern!r}")
    for clave, esperado in T.items():
        dibujado = " ".join(por_pieza.pop(clave, []))
        if dibujado != esperado:
            fallas.append(f"{clave}: dibujado {dibujado!r} ≠ fuente {esperado!r}")
    for clave in por_pieza:
        fallas.append(f"texto dibujado sin pieza fijada: {clave}")
    return fallas


def tramos_flechas():
    return [{"red": fl["i"], "pred": f"{fl['clave'][1]} ({fl['i'] + 1})", "a": a, "b": b}
            for fl in REG["flechas"] for a, b in zip(fl["pts"], fl["pts"][1:])]


def controlar_textos(alto_total):
    fallas, tamanos = [], {}
    minimos = {"texto-texto": math.inf, "rótulo-su flecha": math.inf, "rótulo-otra flecha": math.inf,
               "texto-borde de su caja": math.inf}
    for r in REG["textos"]:
        R = r["R"]
        pt = r["fs"] * EF.PT_POR_CM * ANCHO_CM / W
        tamanos[r["fs"]] = pt
        if pt < PT_MINIMO:
            fallas.append(f"{r['s']!r}: letra {pt:.2f} pt < {PT_MINIMO}")
        if R[0] < 0 or R[1] < 0 or R[2] > W or R[3] > alto_total:
            fallas.append(f"{r['s']!r}: fuera del lienzo")
        if r["caja"] is not None:
            C = REG["cajas"][r["caja"]]
            holg = min(R[0] - C["R"][0], C["R"][2] - R[2], R[1] - C["R"][1], C["R"][3] - R[3])
            minimos["texto-borde de su caja"] = min(minimos["texto-borde de su caja"], holg)
            if holg < C["grosor"] / 2.0 + 1.5:
                fallas.append(f"{r['s']!r}: a {holg:.1f} del borde de su caja")
        Rh = EF.crecer(R, HALO_AIRE) if r["halo"] else R
        for k, C in REG["cajas"].items():
            if k != r["caja"] and EF.se_solapan(Rh, EF.crecer(C["R"], C["grosor"] / 2.0)):
                fallas.append(f"{r['s']!r}: se superpone con la caja de {k}")
        for t in tramos_flechas():
            if EF.toca(t["a"], t["b"], Rh):
                fallas.append(f"{r['s']!r}: lo toca la flecha {t['pred']}")
        for fl in REG["flechas"]:
            if EF.se_solapan(Rh, EF.bbox(fl["punta"])):
                fallas.append(f"{r['s']!r}: lo toca la punta de la flecha {fl['i'] + 1}")
        if r["halo"]:
            dist = {fl["i"]: min(EF.dist_rect_tramo(R, a, b) for a, b in zip(fl["pts"], fl["pts"][1:]))
                    for fl in REG["flechas"]}
            propia = dist.get(r["pieza"][1], math.inf)
            ajena = min((v for i, v in dist.items() if i != r["pieza"][1]), default=math.inf)
            minimos["rótulo-su flecha"] = min(minimos["rótulo-su flecha"], propia)
            minimos["rótulo-otra flecha"] = min(minimos["rótulo-otra flecha"], ajena)
            if propia > JUNTO:
                fallas.append(f"rótulo {r['s']!r}: a {propia:.1f} de su flecha (más de {JUNTO})")
            if ajena < propia + MARGEN_AJENA:
                fallas.append(f"rótulo {r['s']!r}: otra flecha a {ajena:.1f}, su flecha a {propia:.1f}")
    textos = REG["textos"]
    for i in range(len(textos)):
        for j in range(i + 1, len(textos)):
            a, b = textos[i], textos[j]
            Ra = EF.crecer(a["R"], HALO_AIRE) if a["halo"] else a["R"]
            Rb = EF.crecer(b["R"], HALO_AIRE) if b["halo"] else b["R"]
            if EF.se_solapan(Ra, Rb):
                fallas.append(f"{a['s']!r} se superpone con {b['s']!r}")
            dx = max(b["R"][0] - a["R"][2], 0.0, a["R"][0] - b["R"][2])
            dy = max(b["R"][1] - a["R"][3], 0.0, a["R"][1] - b["R"][3])
            minimos["texto-texto"] = min(minimos["texto-texto"], math.hypot(dx, dy))
    return fallas, tamanos, minimos


def controlar_cajas():
    fallas, claves = [], sorted(REG["cajas"])
    for i in range(len(claves)):
        for j in range(i + 1, len(claves)):
            A, B = REG["cajas"][claves[i]], REG["cajas"][claves[j]]
            if EF.se_solapan(EF.crecer(A["R"], A["grosor"] / 2.0 + SEP_CAJAS), B["R"]):
                fallas.append(f"las cajas de {claves[i]} y {claves[j]} están a menos de {SEP_CAJAS}")
    return fallas


def controlar_trazos_svg(svg):
    """Ningún tramo recto diagonal ni elemento girado en el SVG (no se admite
    ningún transform: tampoco hay rótulos girados)."""
    fallas, n = [], 0
    for el in ET.fromstring(svg).iter():
        tag = el.tag.replace(NS, "")
        if el.get("transform"):
            fallas.append(f"elemento {tag} con transform {el.get('transform')!r}")
        if tag == "path":
            if re.sub(r"[ML0-9.\s-]", "", el.get("d", "")):
                fallas.append(f"camino con comandos no controlados: {el.get('d')!r}")
            v = numeros(el.get("d"))
        elif tag == "line":
            v = [float(el.get(a)) for a in ("x1", "y1", "x2", "y2")]
        elif tag == "polyline":
            v = numeros(el.get("points"))
        else:
            continue
        pts = [(v[k], v[k + 1]) for k in range(0, len(v), 2)]
        for (xa, ya), (xb, yb) in zip(pts, pts[1:]):
            n += 1
            if abs(xb - xa) > 0.005 and abs(yb - ya) > 0.005:
                fallas.append(f"tramo diagonal de ({xa:g}, {ya:g}) a ({xb:g}, {yb:g})")
    return fallas, n


def controlar_flechas():
    """Extremos en el borde de sus cajas, ningún tramo dentro de una caja,
    ninguna punta sobre otra caja, paralelas de flechas distintas separadas."""
    fallas = []
    for fl in REG["flechas"]:
        o, _, d = fl["clave"]
        for extremo, k in ((fl["pts"][0], o), (fl["pts"][-1], d)):
            if k not in REG["cajas"] or not en_borde(extremo, REG["cajas"][k]["R"]):
                fallas.append(f"flecha {fl['i'] + 1}: el extremo {extremo} no está en el borde de la caja de {k}")
        for a, b in zip(fl["pts"], fl["pts"][1:]):
            for k, C in REG["cajas"].items():
                if EF.largo_dentro(a, b, EF.crecer(C["R"], -0.5)) > 0:
                    fallas.append(f"flecha {fl['i'] + 1}: el tramo {a}-{b} atraviesa la caja de {k}")
        for k, C in REG["cajas"].items():
            if k != d and EF.se_solapan(EF.bbox(fl["punta"]), EF.crecer(C["R"], C["grosor"] / 2.0)):
                fallas.append(f"flecha {fl['i'] + 1}: la punta toca la caja de {k}")
    tramos = tramos_flechas()
    for i in range(len(tramos)):
        for j in range(i + 1, len(tramos)):
            s, u = tramos[i], tramos[j]
            hs, hu = s["a"][1] == s["b"][1], u["a"][1] == u["b"][1]
            if s["red"] == u["red"] or hs != hu:
                continue
            eje, o = (1, 0) if hs else (0, 1)
            lo = max(min(s["a"][o], s["b"][o]), min(u["a"][o], u["b"][o]))
            hi = min(max(s["a"][o], s["b"][o]), max(u["a"][o], u["b"][o]))
            if lo < hi and abs(s["a"][eje] - u["a"][eje]) < DISTANCIA_PARALELAS:
                fallas.append(f"{s['pred']} y {u['pred']} corren paralelas a menos de {DISTANCIA_PARALELAS}")
    return fallas


def controlar_cruces():
    """Cruces en X entre flechas distintas (con el conteo de la figura del
    esquema final); tienen que ser exactamente los declarados."""
    rectos = [t for t in tramos_flechas() if t["a"][0] == t["b"][0] or t["a"][1] == t["b"][1]]
    puntos, defectos = EF.cruces(rectos)
    fallas = list(defectos)
    if {p: sorted(v) for p, v in puntos.items()} != CRUCES_DECLARADOS:
        fallas.append(f"{len(puntos)} cruce(s) entre flechas, declarados {len(CRUCES_DECLARADOS)}: "
                      + "; ".join(f"{sorted(v)} en {p}" for p, v in sorted(puntos.items())))
    return fallas, len(puntos)


def controlar_margen(alto_total):
    todas = [(f"texto {r['s']!r}", EF.crecer(r["R"], HALO_AIRE) if r["halo"] else r["R"]) for r in REG["textos"]]
    todas += [(f"caja de {k}", EF.crecer(C["R"], C["grosor"] / 2.0)) for k, C in REG["cajas"].items()]
    todas += [(f"flecha {fl['i'] + 1}", EF.bbox(fl["pts"] + fl["punta"])) for fl in REG["flechas"]]
    distancia = {"izquierdo": lambda R: R[0], "superior": lambda R: R[1],
                 "derecho": lambda R: W - R[2], "inferior": lambda R: alto_total - R[3]}
    minimos, fallas = {}, []
    for borde, d in distancia.items():
        minimos[borde] = min(d(R) for _, R in todas)
        fallas += [f"{nombre}: a {d(R):.1f} unidades del borde {borde}" for nombre, R in todas if d(R) < MARGEN_MIN]
    return minimos, fallas, len(todas)


def controlar_registro(svg):
    """Cada elemento del SVG (salvo el fondo) está registrado, en el mismo orden."""
    hijos = [el.tag.replace(NS, "") for el in ET.fromstring(svg)]
    if hijos[:1] != ["rect"]:
        return [f"el SVG no empieza con el fondo: {hijos[:1]}"]
    if hijos[1:] != REG["dibujados"]:
        return [f"elementos del SVG {Counter(hijos[1:])} ≠ registrados {Counter(REG['dibujados'])}"]
    return []


def controlar(res, E, perturbacion=None):
    """Compone la figura y corre todos los controles."""
    svg, T, geo = componer(res, E, perturbacion)
    alto_total = geo["alto"]
    c, x = {}, {}
    c["inventario"], x["cajas"], x["relaciones"] = controlar_inventario(svg, E, res)
    c["contenido"] = controlar_contenido(T)
    c["textos"], x["tamanos"], x["minimos"] = controlar_textos(alto_total)
    c["cajas"] = controlar_cajas()
    c["trazos"], x["n_tramos"] = controlar_trazos_svg(svg)
    c["flechas"] = controlar_flechas()
    c["cruces"], x["n_cruces"] = controlar_cruces()
    x["minimos_margen"], c["margen"], x["n_elem"] = controlar_margen(alto_total)
    c["registro"] = controlar_registro(svg)
    return svg, T, geo, c, x


# Prueba negativa -> control que tiene que fallar.
PRUEBAS_NEGATIVAS = (("relacion_de_mas", "inventario"), ("entidad_de_menos", "inventario"),
                     ("rotulo_sobre_caja", "textos"), ("tramo_diagonal", "trazos"),
                     ("cruce_de_flechas", "cruces"))


def pruebas_negativas(res, E):
    """Cada defecto plantado tiene que hacer fallar su control."""
    vivas = []
    for caso, control in PRUEBAS_NEGATIVAS:
        _, _, _, c, _ = controlar(res, E, caso)
        if not c[control]:
            freno(f"la prueba negativa {caso} no hizo fallar el control de {control}")
        vivas.append((caso, control, c[control][0], sorted(k for k, v in c.items() if v and k != control)))
    return vivas


# --------------------------------------------------------------------------- #
# Principal                                                                    #
# --------------------------------------------------------------------------- #
def sha256(ruta):
    with open(ruta, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def invariantes_pdf(ruta_pdf):
    from pypdf import PdfReader
    lector = PdfReader(ruta_pdf)
    pagina = lector.pages[0]
    fecha = (lector.metadata or {}).get("/CreationDate")
    contenido = hashlib.sha256(pagina.get_contents().get_data()).hexdigest()
    return contenido, fecha, (float(pagina.mediabox.width), float(pagina.mediabox.height))


def argumentos():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--registro", default=REGISTRO_POR_OMISION[0],
                    help="archivo de registros de E1 (jsonl) con la salida cruda de la unidad")
    ap.add_argument("--sha256", default=None, help="candado del archivo de registros")
    ap.add_argument("--catalogo", default=CATALOGO_POR_OMISION[0], help="catálogo de sujetos (json)")
    ap.add_argument("--sha256-catalogo", default=None, help="candado del catálogo de sujetos")
    ap.add_argument("--salida", default=AQUI,
                    help="directorio donde escribir el SVG, el PNG y el PDF (por omisión, el del script)")
    ap.add_argument("--perturbar", choices=[c for c, _ in PRUEBAS_NEGATIVAS], default=None,
                    help="compone la figura con ese defecto: los controles fallan y no se escribe nada")
    args = ap.parse_args()
    for ruta, candado, omision in (("registro", "sha256", REGISTRO_POR_OMISION),
                                   ("catalogo", "sha256_catalogo", CATALOGO_POR_OMISION)):
        if getattr(args, candado) is None:
            if getattr(args, ruta) != omision[0]:
                freno(f"--{ruta} distinto del de omisión sin su candado (--{candado.replace('_', '-')})")
            setattr(args, candado, omision[1])
    return args


def main():
    global MEDIR
    args = argumentos()
    res = resolver(args)
    E = leer_estilo()
    MEDIR = proc.medidor()
    if MEDIR is None:
        freno("sin las métricas reales de Helvetica (PIL y la fuente del sistema) no se compone la figura")
    ext = res["ext"]
    print("FUENTES (sha256 comprobado):")
    print(f"  registro  {args.registro}:{res['linea']}   {args.sha256}")
    if res["sujetos"]:
        print(f"  catálogo  {args.catalogo}   {args.sha256_catalogo}")
    print(f"  estilo    {ESTILO[0]}   {ESTILO[1]}")
    print(f"REGISTRO: línea {res['linea']} de {res['n_regs']} registros del archivo, el único de {UNIDAD} "
          f"(sha256 de la línea {res['sha_linea']}); stop_reason {res['reg']['stop_reason']!r}, sin error; "
          f"{len(ext['entities'])} entidades y {len(ext['relations'])} relaciones en la salida cruda")
    for k, v in res["no_dibujado"]:
        print(f"NO DIBUJADO (no es entidad ni relación): {k} = {json.dumps(v, ensure_ascii=False)}")
    if not res["sujetos"]:
        print("SUJETOS: ninguna relación de la salida llega a un sujeto; no hay caja de sujeto y el catálogo "
              "no se lee")
    for _, s in sorted(res["sujetos"].items()):
        print(f"SUJETO: {s['id']} -> {s['etiqueta']!r} (catálogo, líneas {s['lineas']}: id y label)")
    print("ESTILO por tipo (de la figura del esquema final): "
          + "; ".join(f"{t} {E['cajas'][t]['relleno']}/{E['cajas'][t]['borde']}/{E['cajas'][t]['grosor']:g}"
                      + (f"/discontinua {E['cajas'][t]['discontinua']}" if E["cajas"][t]["discontinua"] else "")
                      for t in sorted({n['tipo'] for n in res['nodos'].values()}))
          + f"; tipos {E['fs_tipo']} en negrita, etiquetas {FS_ETIQUETA}, rótulos {E['fs_rotulo']}; "
            f"flechas {E['gris']} de {E['grosor']:g}")

    vivas = pruebas_negativas(res, E)
    print(f"PRUEBAS NEGATIVAS: {len(vivas)} de {len(PRUEBAS_NEGATIVAS)} hacen fallar su control")
    for caso, control, falla, otros in vivas:
        print(f"  {caso} -> {control}: {falla}" + (f" (fallan también: {', '.join(otros)})" if otros else ""))

    svg, T, geo, c, x = controlar(res, E, args.perturbar)
    alto_total = geo["alto"]
    if args.perturbar:
        print(f"PERTURBACIÓN: {args.perturbar}")
    print(f"INVENTARIO (releído del SVG): {len(x['cajas'])} cajas y {len(x['relaciones'])} relaciones contra "
          f"{len(res['nodos'])} y {len(res['relaciones'])} del registro; fallas: {len(c['inventario'])}")
    for n in x["cajas"]:
        print(f"  caja     {n[0]} | {n[1]}")
    for o, nombre, d in x["relaciones"]:
        print(f"  relación {o[0]} «{o[1]}» --{nombre}--> {d[0]} «{d[1]}»")
    nombres = {"contenido": f"{len(REG['textos'])} textos, {len(T)} piezas",
               "textos": f"{len(REG['textos'])} textos contra {len(REG['cajas'])} cajas y {len(REG['flechas'])} "
                         "flechas; distancias mínimas "
                         + "; ".join(f"{k} {v:.1f}" for k, v in x["minimos"].items() if math.isfinite(v)),
               "cajas": f"{len(REG['cajas'])} cajas",
               "trazos": f"{x['n_tramos']} tramos en el SVG",
               "flechas": f"{len(REG['flechas'])} flechas",
               "cruces": f"{x['n_cruces']} cruce(s) entre flechas, declarados {len(CRUCES_DECLARADOS)}",
               "margen": f"{x['n_elem']} elementos; mínimo a cada borde "
                         + ", ".join(f"{b} {v:.1f} u = {v * ANCHO_CM * 10 / W:.2f} mm"
                                     for b, v in x["minimos_margen"].items())
                         + f"; exigido {MARGEN_MM:.1f} mm ({MARGEN_MIN:.1f} u)",
               "registro": f"{len(REG['dibujados'])} elementos del SVG"}
    for k in c:
        if k != "inventario":
            print(f"{k.upper()}: {nombres[k]}; fallas: {len(c[k])}")
        for falla in c[k]:
            print(f"  MAL {falla}")
    if any(c.values()):
        raise SystemExit("FALLA: la figura tiene defectos; no se escribe nada")
    for fs in sorted(x["tamanos"]):
        print(f"LETRA {fs} unidades -> {x['tamanos'][fs]:.2f} pt impresos a {ANCHO_CM:g} cm")
    print(f"ALTO: lienzo {W} x {alto_total}, impreso a {ANCHO_CM:.2f} x {ANCHO_CM * alto_total / W:.2f} cm "
          f"(cajas de {CAJA_W} x {geo['alto_caja']})")

    os.makedirs(args.salida, exist_ok=True)
    rutas_s = {e: os.path.join(args.salida, f"{NOMBRE}.{e}") for e in ("svg", "png", "pdf")}
    with open(rutas_s["svg"], "w", encoding="utf-8", newline="\n") as fh:
        fh.write(svg)
    EF.exportar(rutas_s["svg"], rutas_s["png"], rutas_s["pdf"])
    contenido, fecha, caja_pdf = invariantes_pdf(rutas_s["pdf"])
    for e in ("svg", "png", "pdf"):
        print(f"{e.upper()}: {rutas_s[e]}   sha256 {sha256(rutas_s[e])}")
    print(f"     PNG {EF.png_dimensiones(rutas_s['png'])} px; PDF {caja_pdf[0]:.1f} x {caja_pdf[1]:.1f} pt; "
          f"/CreationDate {fecha!r} (SOURCE_DATE_EPOCH={EF.SOURCE_DATE_EPOCH}); "
          f"stream de contenido sha256 {contenido}")


if __name__ == "__main__":
    try:
        main()
    except EF.Freno as e:
        raise SystemExit(f"FRENO {e}")
