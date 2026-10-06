#!/usr/bin/env python3
"""Figura «el ejemplo después del ensamblado» (capítulo 4, sección 4.5), versión 3.

Continuación de la figura de la salida del extractor (sección 4.2, versión 3):
el mismo fragmento de grafo del punto 5.1.1.1 de Clasificación de deudores,
leído ahora del grafo ensamblado. Lo que ya estaba en la figura del extractor
conserva su disposición, su estilo y sus rótulos (baja entero, sin otro cambio,
para dejar arriba una franja nueva); lo que agrega el ensamblado se dibuja así:
- el nodo de destino de la remisión al punto 3.7, como una caja más, con su
  tipo y su etiqueta, en la franja de arriba;
- cada remite_a, en línea discontinua gris y rotulada, como la de la figura del
  esquema final;
- el umbral de la condición del monto, junto a su caja (arriba), con la marca
  «≤» de la figura del esquema final y sus campos valor, unidad, comparación y
  base, con el nombre del campo en castellano y la comparación leída en
  castellano (LECTURA_COMPARACION).
No se dibujan, a propósito, las relaciones que cumplen EXCLUIR: las
establecida_en que el ensamblado deriva de la procedencia (EXCLUIDAS; en el
grafo de la versión 3, ninguna: el extractor devolvió las cuatro). El
inventario las descuenta y el script las informa.
Si algo de lo que ya estaba cambió en el grafo (una etiqueta, un nodo unido,
una relación retirada), se dibuja como está en el grafo y el script lo informa:
en la versión 3, la exceptua de la excepción a la operación, que el validador
rechaza, no está en el grafo y no se dibuja.
Nada se marca en color y no hay leyenda.

Versión 1 (04/10/2026): dibujaba también las dos establecida_en derivadas (con
un cruce) y el valor interno de la comparación (minimo_estricto).
Versión 2 (04/10/2026): sobre KG-Tanda0-Desarrollo-r2a y la figura del
extractor versión 2 (perfil del esquema congelado).
Versión 3: sobre el grafo sellado de la re-extracción de la tanda 0 con el
perfil r2b (KG-Tanda0-Diez-r2b) y la figura del extractor versión 3.

Fuentes, con candado de sha256:
- el grafo (--grafo y --sha256-grafo; por omisión, KG-Tanda0-Diez-r2b, el
  grafo sellado de la re-extracción de la tanda 0 con el perfil r2b). Se
  dibuja su vecindario de la unidad: las aristas que tienen a cla::5.1.1.1 entre
  sus procedencias, salvo las excluidas, y sus extremos (entre ellos, el destino
  de la remisión al 3.7). El script frena si un nodo que viene solo de la
  unidad tiene una arista fuera del vecindario, si un nodo de la unidad no
  tiene aristas, si un extremo ajeno a la unidad no es el destino de una
  remite_a, o si las aristas que cumplen EXCLUIR no son las de EXCLUIDAS;
- la figura del extractor, recompuesta con su generador (que lee su registro y
  su catálogo con sus candados): tiene que dar byte a byte el SVG registrado en
  su LEEME (SVG_EXTRACTOR). De ahí salen las cajas, las flechas y los rótulos
  de lo que ya estaba;
- el estilo, de figura_esquema_final.svg (versión 3): el de cajas, tipos,
  rótulos y flechas lo lee el generador de la figura del extractor; el
  discontinuo de remite_a y la marca de umbrales se leen acá;
- reglas_comparacion.py, cuyo docstring define cada valor de la comparación:
  LECTURA_COMPARACION da la lectura de cada uno, con las líneas de su
  definición, y el script comprueba que cada valor figure en ese archivo.

Controles, en cada corrida (el script frena si fallan); los siete primeros son
los de la figura del extractor, reutilizados:
- inventario: el SVG se relee y, solo desde su geometría, se rearman las cajas
  y las relaciones; tienen que ser exactamente los nodos y las aristas del
  vecindario, sin las excluidas;
- contenido, textos, cajas, trazos, flechas y margen: como en la figura del
  extractor (letra de 7 pt o más a 15 cm, nada superpuesto, rótulos junto a su
  flecha, cajas separadas, solo tramos horizontales y verticales, flechas de
  borde a borde, 2 mm de margen);
- cruces: entre flechas distintas solo cruces en X, y exactamente los de
  CRUCES_DECLARADOS (ninguno);
- conservación: cada elemento del SVG de la figura del extractor, bajado DY,
  está en este SVG con los mismos atributos y el mismo texto, salvo los
  cambios que el grafo trae y el script declara;
- remisiones: las flechas discontinuas son exactamente las rotuladas
  remite_a, con el discontinuo de la figura del esquema final;
- umbral: el panel se relee del SVG y da los campos del grafo (la comparación,
  en su lectura), con la marca en su primera fila, y su caja es la que tiene
  debajo, a 40 o menos, con el centro del panel sobre ella; ningún texto ni la
  marca a menos de 9 de una flecha;
- registro: cada elemento del SVG está registrado.
Antes de componer la figura corren diez pruebas negativas: las cinco de la
figura del extractor (una relación de más, una entidad de menos, un rótulo
sobre una caja, un tramo diagonal y un cruce de más) y cinco nuevas (una
remite_a continua, un campo de umbral de menos, el umbral lejos de su caja,
una caja de las que ya estaban corrida y una relación retirada dibujada; en la
versión 2, la última era una relación excluida dibujada, y en el grafo de la
versión 3 no hay relaciones excluidas).
Cada una tiene que hacer fallar su control. Con --perturbar <caso> se compone
la figura con ese defecto: los controles fallan y no se escribe nada.

Reutiliza por importación, sin modificarlos, generar_figura_extractor_ejemplo.py
(la figura de la que parte, el estilo, la medida y el dibujo de textos y cajas,
la relectura del inventario y sus controles), generar_figura_esquema_final.py
(la marca de umbrales, las puntas, el texto con halo, la geometría, el conteo
de cruces y la exportación) y, de generar_figura_proceso_extraccion.py, el
medidor con las métricas reales de Helvetica.

Salidas, byte-reproducibles: figura_ensamblado_ejemplo.svg, .png (300 dpi,
densidad grabada) y .pdf (fecha de creación fijada por SOURCE_DATE_EPOCH).

Uso (desde la raíz del repo):
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_ensamblado_ejemplo.py
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_ensamblado_ejemplo.py \\
        --grafo <kg.json> --sha256-grafo <sha256> [--salida <directorio>]
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_ensamblado_ejemplo.py \\
        --perturbar {relacion_de_mas,entidad_de_menos,rotulo_sobre_caja,tramo_diagonal,cruce_de_flechas,\\
                     remite_continua,umbral_campo_de_menos,umbral_lejos,caja_movida,retirada_dibujada}
"""

import argparse
import hashlib
import json
import math
import os
import sys
import xml.etree.ElementTree as ET
from collections import Counter

sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import generar_figura_esquema_final as EF            # noqa: E402
import generar_figura_extractor_ejemplo as EX        # noqa: E402
import generar_figura_proceso_extraccion as proc     # noqa: E402

NOMBRE = "figura_ensamblado_ejemplo"
NS = EX.NS
freno = EX.freno
# Los controles de la figura del extractor leen su registro de elementos
# dibujados; esta figura usa ese mismo registro.
REG = EX.REG

# --------------------------------------------------------------------------- #
# Fuentes y candados                                                           #
# --------------------------------------------------------------------------- #
# KG-Tanda0-Diez-r2b: re-extracción de la tanda 0 con el perfil r2b
# (U-REEXT-T0; ensamblado en bbc38dc, sello en c9540c0); se reemplaza con
# --grafo y --sha256-grafo (por ejemplo, con el grafo del escalado).
GRAFO_POR_OMISION = ("data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2b/r2/kg.json",
                     "a9631a64b422bdae634fb05135373c6f04c6272cdf7acd43a1be9f5b6c1f5f57")
# SVG de la figura del extractor (versión 3), el registrado en su LEEME.
SVG_EXTRACTOR = "9a393b325cae953f3da697658cb435fdace001cf91cb8eee1ea28980b7dfe64d"
UNIDAD = EX.UNIDAD
REMISION = "remite_a"

# Claves de un elemento de umbrales; una fuera de esta lista frena el script.
# Se dibujan las de CAMPOS_UMBRAL, con el nombre en castellano.
CLAVES_UMBRAL = ("tramo", "valor", "unidad", "comparacion", "base", "regla_comparacion", "origen",
                 "tramo_verificado", "base_destino", "base_via")
CAMPOS_UMBRAL = (("valor", "valor"), ("unidad", "unidad"), ("comparacion", "comparación"), ("base", "base"))
# Definiciones de los valores de la comparación: el docstring de
# reglas_comparacion.py (U-PYD), en la versión con la que se ensambló el grafo
# (la de 9f6361e, igual en bbc38dc; la versión 2 leía la de 57a8dd2).
REGLAS_COMPARACION = ("data/experiment/pyd_r2/code/reglas_comparacion.py",
                      "69c48d24387bcb788925cd1513496e015b7594f0469124f45f5082f3465b9d79")
# Lectura en castellano de cada valor de la comparación, con las líneas del
# docstring de reglas_comparacion.py que lo definen y sus formas.
LECTURA_COMPARACION = {
    "minimo_estricto": "mayor que",            # :15-18 «super-», «exced-», «más de», «mayor(es) a»
    "maximo_estricto": "menor que",            # :18 «inferior(es) a», «menos de», «menor(es) a»
    "minimo_inclusivo": "mayor o igual que",   # :40-42 «igual o superior/mayor», «al menos», «como mínimo»
    "maximo_inclusivo": "menor o igual que",   # :42-43 «igual o inferior/menor», «como máximo», «hasta»
    "igual": "igual a",                        # :52-53 «igual(es) a/al», «equivalente(s) a/al»
    "coeficiente": "coeficiente",              # :11-12 «pondera…», «ponderador», «coeficiente», «factor»
    "no_determinada": "no determinada",        # :68 cuantía sin marcador
}
# Relaciones del vecindario que no se dibujan, a propósito: las que cumplen
# EXCLUIR (las establecida_en que el ensamblado deriva de la procedencia). Las
# que cumplen la regla tienen que ser exactamente EXCLUIDAS (por rol); si el
# grafo trae otras, el script frena.
EXCLUIR = {"relation": "establecida_en", "rol_fuente": "derivada_de_procedencia"}
EXCLUIDAS = ()                              # el extractor devolvió las cuatro establecida_en

# --------------------------------------------------------------------------- #
# Disposición                                                                  #
# --------------------------------------------------------------------------- #
W, ANCHO_CM, MARGEN = EX.W, EX.ANCHO_CM, EX.MARGEN
CAJA_W = EX.CAJA_W
CLAVE_SUJETO = EX.CLAVE_SUJETO
# Nodos nuevos: rol -> (tipo, procedencias). El destino de la remisión al 3.7
# va en la franja de arriba, sobre la operación (el umbral ocupa el centro,
# sobre la condición del monto).
NUEVOS = {"nodo_3.7": ("Definicion", ("cla::3.7",))}
LUGAR_NUEVOS = {"nodo_3.7": (EX.X_COL[0], MARGEN)}
# Lo que ya estaba baja el alto de una caja más una calle (DY, calculado en
# geometria_vieja), para dejar arriba la franja del nodo del 3.7 y del umbral.
# Umbral: el panel va arriba de la caja de su nodo, con su última línea a
# SEP_UMBRAL del borde superior de la caja; nombres en Menlo, valores en
# Helvetica envueltos en ANCHO_VALOR.
UMBRAL_DE = "e3"
SEP_UMBRAL = 35
SEP_MARCA = 8
SEP_VALOR = 10
ANCHO_VALOR = 185
UMBRAL_JUNTO = 40                           # del panel a su caja, como máximo
UMBRAL_A_FLECHA = 9                         # de cualquier texto del panel a una flecha, como mínimo
# Cruces declarados: ninguno.
CRUCES_DECLARADOS = {}


def rutas_nuevas(C):
    """Puntos y rótulo de cada relación nueva, a partir de los rectángulos
    (x0, y0, x1, y1) de las cajas por rol. Rótulo: (tramo, lado, centro o
    None para el medio del tramo)."""
    m, o, n = C["e3"], C["e1"], C["nodo_3.7"]
    x_hueco = m[0] - 33                           # entre la columna de la izquierda y la condición del monto
    calle = (n[3] + m[1]) / 2.0                   # entre la franja de arriba y la fila de la condición
    return {
        # remite_a de la condición del monto: sale por su lado izquierdo, arriba
        # de la condicion_de, sube por el hueco y entra de costado a la caja
        # del 3.7.
        ("e3", REMISION, "nodo_3.7"): ([(m[0], m[1] + 16), (x_hueco, m[1] + 16), (x_hueco, (n[1] + n[3]) / 2.0),
                                        (n[2], (n[1] + n[3]) / 2.0)], (1, "izquierda", calle)),
        # remite_a de la operación: recta hacia arriba, a la izquierda de la
        # condicion_de que le llega.
        ("e1", REMISION, "nodo_3.7"): ([(o[0] + 46, o[1]), (o[0] + 46, n[3])], (0, "derecha", calle)),
    }


# Prueba negativa de la relación retirada dibujada: la exceptua que el
# validador rechaza, con su recorrido de la figura del extractor.
RETIRADA_DE_PRUEBA = ("e2", "exceptua", "e1")


# --------------------------------------------------------------------------- #
# Fuentes                                                                      #
# --------------------------------------------------------------------------- #
def procedencias(x):
    return [p.get("chunk_id") for p in (x.get("provenances") or [x.get("provenance") or {}])]


def es_excluida(e):
    return all(e.get(k) == v for k, v in EXCLUIR.items())


def leer_lecturas():
    """Cada valor de LECTURA_COMPARACION figura, como literal, en
    reglas_comparacion.py (leído con su candado)."""
    texto = EX.leer_con_candado(*REGLAS_COMPARACION).decode("utf-8")
    faltan = sorted(v for v in LECTURA_COMPARACION if f'"{v}"' not in texto)
    if faltan:
        freno(f"valores de comparación que no están en {REGLAS_COMPARACION[0]}: {faltan}")


def leer_vecindario(ruta, sha):
    """Vecindario de la unidad en el grafo: aristas con la unidad entre sus
    procedencias y sus extremos."""
    kg = json.loads(EX.leer_con_candado(ruta, sha).decode("utf-8"))
    nodos = {}
    for n in kg["nodes"]:
        if n["id"] in nodos:
            freno(f"el grafo tiene dos nodos {n['id']}")
        nodos[n["id"]] = n
    aristas = [e for e in kg["edges"] if UNIDAD in procedencias(e)]
    claves = Counter((e["source"], e["relation"], e["target"]) for e in aristas)
    if any(v > 1 for v in claves.values()):
        freno("el vecindario tiene dos aristas con el mismo origen, nombre y destino")
    extremos = {e["source"] for e in aristas} | {e["target"] for e in aristas}
    if extremos - set(nodos):
        freno(f"aristas del vecindario con extremos que no son nodos del grafo: {sorted(extremos - set(nodos))}")
    de_la_unidad = {i for i, n in nodos.items() if UNIDAD in procedencias(n)}
    solo_unidad = {i for i, n in nodos.items() if procedencias(n) == [UNIDAD]}
    if de_la_unidad - extremos:
        freno(f"nodos de {UNIDAD} sin aristas en el vecindario: {sorted(de_la_unidad - extremos)}")
    fuera = [e for e in kg["edges"] if UNIDAD not in procedencias(e)
             and (e["source"] in solo_unidad or e["target"] in solo_unidad)]
    if fuera:
        freno(f"{len(fuera)} aristas de nodos que vienen solo de {UNIDAD} quedan fuera del vecindario")
    ajenos = extremos - de_la_unidad
    for i in sorted(ajenos):
        llegan = [e for e in aristas if i in (e["source"], e["target"])]
        if any(e["relation"] != REMISION or e["target"] != i for e in llegan):
            freno(f"el nodo {i}, ajeno a {UNIDAD}, no es solo destino de {REMISION}")
        for e in llegan:
            destino = ((e.get("properties") or {}).get("destino"))
            if procedencias(nodos[i]) != [destino]:
                freno(f"la {REMISION} hacia {i} declara destino {destino!r} y el nodo viene de "
                      f"{procedencias(nodos[i])}")
    excluidas = [e for e in aristas if es_excluida(e)]
    return {"nodos": {i: nodos[i] for i in sorted(extremos)}, "aristas": aristas, "ajenos": sorted(ajenos),
            "excluidas": excluidas, "dibujadas": [e for e in aristas if not es_excluida(e)],
            "solo_unidad": solo_unidad, "n_nodos": len(kg["nodes"]), "n_aristas": len(kg["edges"])}


def leer_estilo_nuevo():
    """De la figura del esquema final: el discontinuo de remite_a y la marca de
    umbrales; los dos tienen que ser únicos y coincidir con su generador."""
    raiz = ET.fromstring(EX.leer_con_candado(*EX.ESTILO).decode("utf-8"))
    remite = {(p.get("stroke"), p.get("stroke-width"), p.get("stroke-dasharray"))
              for p in raiz.iter(NS + "path") if p.get("data-pred") == REMISION}
    discontinuas = {p.get("data-pred") for p in raiz.iter(NS + "path") if p.get("stroke-dasharray")}
    marcas = set()
    for g in raiz.iter(NS + "g"):
        if g.get("data-umbrales") is not None:
            rs, ts = list(g.iter(NS + "rect")), list(g.iter(NS + "text"))
            if len(rs) != 1 or len(ts) != 1:
                freno("una marca de umbrales de la figura del esquema final no es un cuadro y un texto")
            (r,), (t,) = rs, ts
            marcas.add((r.get("width"), r.get("height"), r.get("rx"), r.get("fill"), t.text, t.get("fill"),
                        t.get("font-size"), t.get("font-weight")))
    if len(remite) != 1 or discontinuas != {REMISION} or len(marcas) != 1:
        freno(f"el discontinuo de {REMISION} o la marca de umbrales de la figura del esquema final no es "
              f"único: {remite} {discontinuas} {marcas}")
    (gris, grosor, dash), = remite
    (mw, mh, mrx, mfill, mtexto, mtinta, mfs, mpeso), = marcas
    if (float(mw), float(mh), mfill, mtexto, int(mfs)) != (EF.MARCA["lado"], EF.MARCA["lado"], EF.COLOR_MARCA,
                                                           EF.MARCA["texto"], EF.MARCA["fs"]):
        freno("la marca de umbrales de la figura del esquema final no es la de su generador")
    return {"gris_remite": gris, "grosor_remite": float(grosor), "dash": dash,
            "marca": {"lado": float(mw), "rx": mrx, "fill": mfill, "texto": mtexto, "tinta": mtinta,
                      "fs": int(mfs), "peso": mpeso}}


def figura_vieja():
    """La figura del extractor, recompuesta con su generador y sus fuentes por
    omisión; su SVG tiene que ser el registrado."""
    ns = argparse.Namespace(registro=EX.REGISTRO_POR_OMISION[0], sha256=EX.REGISTRO_POR_OMISION[1],
                            catalogo=EX.CATALOGO_POR_OMISION[0], sha256_catalogo=EX.CATALOGO_POR_OMISION[1])
    res = EX.resolver(ns)
    E = EX.leer_estilo()
    svg, _, geo = EX.componer(res, E)
    sha = hashlib.sha256(svg.encode("utf-8")).hexdigest()
    if sha != SVG_EXTRACTOR:
        freno(f"la figura del extractor recompuesta no es la registrada: sha256 {sha} ≠ {SVG_EXTRACTOR}")
    return {"res": res, "svg": svg, "geo": geo,
            "cajas": {k: dict(v) for k, v in REG["cajas"].items()},
            "flechas": [dict(fl) for fl in REG["flechas"]],
            "rotulos": {t["pieza"][1]: dict(t) for t in REG["textos"] if t["pieza"][0] == "rotulo"}}


def emparejar(viejo, vec):
    """Cada caja de la figura del extractor con su nodo del grafo (mismo tipo y
    misma etiqueta; si no hay, el único nodo de la unidad con ese tipo, y la
    etiqueta cambió), los nodos nuevos con su rol declarado y las relaciones
    conservadas, nuevas y retiradas."""
    nodos, libres, rol, cambios = vec["nodos"], set(vec["nodos"]), {}, []
    for k in sorted(viejo["res"]["nodos"]):
        n = viejo["res"]["nodos"][k]
        c = sorted(i for i in libres if (nodos[i]["type"], nodos[i]["label"]) == (n["tipo"], n["etiqueta"]))
        if len(c) > 1:
            freno(f"la caja {k} de la figura del extractor tiene {len(c)} nodos iguales en el grafo")
        if c:
            rol[k] = c[0]
            libres.discard(c[0])
    for k in sorted(set(viejo["res"]["nodos"]) - set(rol)):
        n = viejo["res"]["nodos"][k]
        c = sorted(i for i in libres if nodos[i]["type"] == n["tipo"] and UNIDAD in procedencias(nodos[i]))
        if len(c) != 1:
            freno(f"la caja {k} ({n['tipo']}, {n['etiqueta']!r}) de la figura del extractor no tiene un nodo "
                  f"en el grafo ({len(c)} candidatos): declarar el cambio")
        rol[k] = c[0]
        libres.discard(c[0])
        cambios.append({"tipo": "etiqueta", "rol": k, "antes": n["etiqueta"], "despues": nodos[c[0]]["label"]})
    for i in sorted(libres):
        clave = (nodos[i]["type"], tuple(procedencias(nodos[i])))
        roles = [r for r, c in NUEVOS.items() if c == clave]
        if len(roles) != 1 or roles[0] in rol:
            freno(f"el nodo {i} {clave} no tiene lugar declarado en NUEVOS")
        rol[roles[0]] = i
    if sorted(rol) != sorted(set(viejo["res"]["nodos"]) | set(NUEVOS)):
        freno(f"roles sin nodo en el grafo: {sorted(set(NUEVOS) - set(rol))}")
    inv = {v: k for k, v in rol.items()}
    viejas = [(r["origen"], r["nombre"], r["destino"]) for r in viejo["res"]["relaciones"]]
    excluidas = sorted((inv[e["source"]], e["relation"], inv[e["target"]]) for e in vec["excluidas"])
    if excluidas != sorted(EXCLUIDAS) or set(excluidas) & set(viejas):
        freno(f"las aristas que cumplen EXCLUIR {excluidas} no son las declaradas en EXCLUIDAS, o una es de "
              "la figura del extractor")
    del_grafo = sorted((inv[e["source"]], e["relation"], inv[e["target"]]) for e in vec["dibujadas"])
    retiradas = [c for c in viejas if c not in del_grafo]
    nuevas = [c for c in del_grafo if c not in viejas]
    cambios += [{"tipo": "retirada", "relacion": c} for c in retiradas]
    return rol, inv, cambios, nuevas, retiradas


def leer_umbral(vec, rol):
    """El umbral de la condición del monto, con sus campos; ningún otro nodo del
    vecindario lleva umbrales (no tendría lugar)."""
    con = sorted(i for i, n in vec["nodos"].items() if (n.get("properties") or {}).get("umbrales"))
    if con != [rol[UMBRAL_DE]]:
        freno(f"los nodos con umbrales del vecindario no son exactamente el de {UMBRAL_DE}: {con}")
    lista = vec["nodos"][con[0]]["properties"]["umbrales"]
    if len(lista) != 1:
        freno(f"el nodo de {UMBRAL_DE} tiene {len(lista)} umbrales; la figura prevé uno")
    u = lista[0]
    extra = sorted(k for k in u if k not in CLAVES_UMBRAL)
    if extra:
        freno(f"el umbral tiene claves no previstas {extra}")
    campos = []
    for clave, nombre in CAMPOS_UMBRAL:
        if not isinstance(u.get(clave), str) or not u[clave]:
            freno(f"el umbral no tiene {clave}")
        valor = u[clave]
        if clave == "comparacion":
            if valor not in LECTURA_COMPARACION:
                freno(f"la comparación {valor!r} no tiene lectura en LECTURA_COMPARACION")
            valor = LECTURA_COMPARACION[valor]
        campos.append((clave, nombre, valor))
    return {"nodo": con[0], "tipo": vec["nodos"][con[0]]["type"], "crudo": u, "campos": campos}


# --------------------------------------------------------------------------- #
# Composición                                                                  #
# --------------------------------------------------------------------------- #
def geometria(viejo, vec, rol, perturbacion):
    """Cajas por rol: las de la figura del extractor, bajadas DY; las nuevas,
    en su lugar declarado, con el tamaño común."""
    alto = viejo["geo"]["alto_caja"]
    dy = alto + EX.CALLE_V
    ancho = CAJA_W - 2 * EX.PAD_X
    max_lineas = max(len(EX.envolver(n["etiqueta"], ancho, EX.FS_ETIQUETA))
                     for n in viejo["res"]["nodos"].values())
    cajas = {}
    for k, i in sorted(rol.items()):
        n = vec["nodos"][i]
        lineas = EX.envolver(n["label"], ancho, EX.FS_ETIQUETA)
        if k in viejo["cajas"]:
            x0, y0, x1, y1 = viejo["cajas"][k]["R"]
            vieja = EX.envolver(viejo["res"]["nodos"][k]["etiqueta"], ancho, EX.FS_ETIQUETA)
            if len(lineas) != len(vieja):
                freno(f"la etiqueta de {k} cambió y ocupa {len(lineas)} líneas en lugar de {len(vieja)}")
            x, y = x0, y0 + dy
        else:
            if len(lineas) > max_lineas:
                freno(f"la etiqueta de {k} no entra en el alto común de las cajas")
            x, y = LUGAR_NUEVOS[k]
        if perturbacion == "caja_movida" and k == "e3":
            x += 12
        cajas[k] = {"x": float(x), "y": float(y), "w": float(CAJA_W), "h": float(alto), "lineas": lineas,
                    "tipo": n["type"], "etiqueta": n["label"]}
    return cajas, alto, dy


def lugar_rotulo(pts, tramo, lado, centro, E):
    """Ancla y alineación de un rótulo junto a un tramo, a DIST_ROTULO."""
    fs = E["fs_rotulo"]
    p, q = pts[tramo], pts[tramo + 1]
    asc, desc = EF.ASC_MONO * fs, EF.DESC_MONO * fs
    if lado == "arriba":
        x = (p[0] + q[0]) / 2.0 if centro is None else centro
        return x, p[1] - EX.DIST_ROTULO - desc, "middle"
    ym = ((p[1] + q[1]) / 2.0 if centro is None else centro) + (asc - desc) / 2.0
    if lado == "izquierda":
        return p[0] - EX.DIST_ROTULO, ym, "end"
    return p[0] + EX.DIST_ROTULO, ym, "start"


def flechas(viejo, cajas, dy, nuevas, retiradas, E, perturbacion):
    """Las flechas conservadas (con su rótulo de la figura del extractor,
    bajados DY) y las nuevas (con su ruta declarada)."""
    out = []
    for j, fl in enumerate(viejo["flechas"]):
        if fl["clave"] in retiradas:
            continue
        pts = [(x, y + dy) for x, y in fl["pts"]]
        r = viejo["rotulos"][j]
        out.append({"clave": fl["clave"], "pts": pts, "rotulo": (r["x"], r["y"] + dy, r["anchor"])})
    C = {k: (c["x"], c["y"], c["x"] + c["w"], c["y"] + c["h"]) for k, c in cajas.items()}
    declaradas = rutas_nuevas(C)
    if sorted(declaradas) != sorted(nuevas):
        freno(f"las rutas nuevas declaradas no son las relaciones nuevas del grafo: "
              f"declaradas {sorted(declaradas)}, nuevas {sorted(nuevas)}")
    for clave in nuevas:
        pts, (tramo, lado, centro) = declaradas[clave]
        out.append({"clave": clave, "pts": pts, "rotulo": lugar_rotulo(pts, tramo, lado, centro, E)})
    if perturbacion == "retirada_dibujada":
        if RETIRADA_DE_PRUEBA not in retiradas:
            freno(f"la relación de la prueba negativa {RETIRADA_DE_PRUEBA} no es una retirada")
        j = next(j for j, fl in enumerate(viejo["flechas"]) if fl["clave"] == RETIRADA_DE_PRUEBA)
        r = viejo["rotulos"][j]
        out.append({"clave": RETIRADA_DE_PRUEBA, "pts": [(x, y + dy) for x, y in viejo["flechas"][j]["pts"]],
                    "rotulo": (r["x"], r["y"] + dy, r["anchor"])})
    if perturbacion == "relacion_de_mas":
        a, b = C[EX.RELACION_DE_MAS[0]], C[EX.RELACION_DE_MAS[2]]
        ym = (a[1] + a[3]) / 2.0
        out.append({"clave": EX.RELACION_DE_MAS, "pts": [(a[2], ym), (b[0], ym)],
                    "rotulo": lugar_rotulo([(a[2], ym), (b[0], ym)], 0, "arriba", None, E)})
    for i, fl in enumerate(out):
        fl["i"] = i
        fl["pts"] = [(float(x), float(y)) for x, y in fl["pts"]]
        fl["discontinua"] = fl["clave"][1] == REMISION and not (
            perturbacion == "remite_continua" and fl["clave"] == (UMBRAL_DE, REMISION, "nodo_3.7"))
        # Las pruebas del cruce y del tramo diagonal, con los recorridos de la
        # figura del extractor.
        fl["pts"] = [(float(x), float(y)) for x, y in EX.perturbar_ruta(fl["clave"], fl["pts"], C, perturbacion)]
        if perturbacion == "rotulo_sobre_caja" and fl["clave"] == EX.ROTULO_SOBRE_CAJA[0]:
            c = cajas[EX.ROTULO_SOBRE_CAJA[1]]
            fl["rotulo"] = (c["x"] + c["w"] / 2.0, c["y"] + c["h"] / 2.0, "middle")
    return out


def registrar_texto(partes, E, s, x, y, fs, mono, anchor, pieza, color, peso="normal"):
    """Un texto del panel del umbral: va dentro de su grupo, así que se
    registra para los controles pero no como elemento de primer nivel."""
    x, y = float(EF.f(x)), float(EF.f(y))
    partes.append(EF.texto_svg(s, x, y, fs, E["mono"] if mono else E["sans"], color, anchor=anchor, peso=peso))
    REG["textos"].append({"s": s, "x": x, "y": y, "fs": fs, "mono": mono, "anchor": anchor, "pieza": pieza,
                          "caja": None, "halo": False, "R": EX.rect_texto(s, x, y, fs, mono, anchor)})


def panel_umbral(umbral, caja, E, N, perturbacion):
    """Panel del umbral arriba de su caja: la marca en la primera fila; cada
    campo con su nombre (Menlo, gris) y su valor (Helvetica), envuelto."""
    filas = []
    for clave, nombre, valor in umbral["campos"]:
        if perturbacion == "umbral_campo_de_menos" and clave == "unidad":
            continue
        lineas = EX.envolver(valor, ANCHO_VALOR, EX.FS_ETIQUETA)
        filas += [(nombre if j == 0 else None, s, clave) for j, s in enumerate(lineas)]
    fs, lado = EX.FS_ETIQUETA, N["marca"]["lado"]
    x0 = caja["x"] + ((EX.X_COL[2] - EX.X_COL[0]) if perturbacion == "umbral_lejos" else 0)
    y_ult = caja["y"] - SEP_UMBRAL
    y1 = y_ult - (len(filas) - 1) * EX.IL_ETIQUETA
    x_nombre = x0 + lado + SEP_MARCA
    x_valor = x_nombre + max(EF.ANCHO_MONO * fs * len(n) for _, n, _ in umbral["campos"]) + SEP_VALOR
    partes = [f'<g data-umbral="{UMBRAL_DE}">']
    y_marca = y1 - (lado / 2.0 + 5)
    partes.append(EF.marca_svg(x0, y_marca, umbral["tipo"], E))
    REG["textos"].append({"s": N["marca"]["texto"], "x": x0 + lado / 2.0, "y": y1, "fs": N["marca"]["fs"],
                          "mono": False, "anchor": "middle", "pieza": ("marca",), "caja": None, "halo": False,
                          "R": (x0, y_marca, x0 + lado, y_marca + lado)})
    for j, (nombre, s, clave) in enumerate(filas):
        y = y1 + j * EX.IL_ETIQUETA
        if nombre is not None:
            registrar_texto(partes, E, nombre, x_nombre, y, fs, True, "start", ("umbral_nombre", clave),
                            E["gris_rotulo"])
        registrar_texto(partes, E, s, x_valor, y, fs, False, "start", ("umbral_valor", clave), E["tinta"])
    partes.append("</g>")
    return partes, {"x": x0, "y_marca": y_marca, "lado": lado}


def textos_fijados(vec, rol, fls, umbral):
    t = {}
    for k, i in rol.items():
        t[("tipo", k)] = vec["nodos"][i]["type"]
        t[("etiqueta", k)] = vec["nodos"][i]["label"]
    for fl in fls:
        t[("rotulo", fl["i"])] = fl["clave"][1]
    t[("marca",)] = EF.MARCA["texto"]
    for clave, nombre, valor in umbral["campos"]:
        t[("umbral_nombre", clave)] = nombre
        t[("umbral_valor", clave)] = valor
    return t


def componer(viejo, vec, rol, nuevas, retiradas, umbral, E, N, perturbacion=None):
    for k in ("textos", "flechas", "dibujados"):
        del REG[k][:]
    REG["cajas"].clear()
    cajas, alto, dy = geometria(viejo, vec, rol, perturbacion)
    fls = flechas(viejo, cajas, dy, nuevas, retiradas, E, perturbacion)
    T = textos_fijados(vec, rol, fls, umbral)
    dibujar = dict(cajas)
    if perturbacion == "entidad_de_menos":
        del dibujar["nodo_3.7"]
    partes = []
    # Flechas y puntas, debajo de las cajas (el orden de la figura del extractor).
    for fl in fls:
        d = "M " + " L ".join(f"{EF.f(x)} {EF.f(y)}" for x, y in fl["pts"])
        dash = f' stroke-dasharray="{N["dash"]}"' if fl["discontinua"] else ""
        partes.append(f'<path d="{d}" fill="none" stroke="{E["gris"]}" stroke-width="{EF.f(E["grosor"])}"{dash}/>')
        REG["dibujados"].append("path")
        (xa, ya), (xb, yb) = fl["pts"][-2], fl["pts"][-1]
        direc = ("down" if yb > ya else "up") if xa == xb else ("right" if xb > xa else "left")
        partes.append(EF.punta_svg({"punto": (xb, yb), "dir": direc}, E["gris"]))
        REG["dibujados"].append("polygon")
        REG["flechas"].append({"i": fl["i"], "clave": fl["clave"], "pts": fl["pts"],
                               "punta": EF.triangulo((xb, yb), direc)})
    # Cajas: tipo en negrita y etiqueta debajo, centrados (como en la figura del extractor).
    for k in sorted(dibujar):
        c = dibujar[k]
        st = E["cajas"][c["tipo"]]
        dash = f' stroke-dasharray="{st["discontinua"]}"' if st["discontinua"] else ""
        partes.append(f'<rect x="{EF.f(c["x"])}" y="{EF.f(c["y"])}" width="{EF.f(c["w"])}" '
                      f'height="{EF.f(c["h"])}" fill="{st["relleno"]}" stroke="{st["borde"]}" '
                      f'stroke-width="{EF.f(st["grosor"])}"{dash} rx="{EF.f(st["rx"])}"/>')
        REG["dibujados"].append("rect")
        REG["cajas"][k] = {"R": (c["x"], c["y"], c["x"] + c["w"], c["y"] + c["h"]), "grosor": st["grosor"]}
        arriba = c["y"] + (c["h"] - EX.alto_contenido(E, len(c["lineas"]))) / 2.0
        xm = c["x"] + c["w"] / 2.0
        EX.texto(partes, E, T[("tipo", k)], xm, arriba + EF.ASC_MONO * E["fs_tipo"], E["fs_tipo"], True,
                 "middle", ("tipo", k), peso="bold", caja=k)
        y0 = arriba + E["fs_tipo"] + EX.SEP_TIPO + EX.ASC_SANS * EX.FS_ETIQUETA
        for j, s in enumerate(c["lineas"]):
            EX.texto(partes, E, s, xm, y0 + j * EX.IL_ETIQUETA, EX.FS_ETIQUETA, False, "middle",
                     ("etiqueta", k), caja=k)
    # Umbral, arriba de su caja.
    p_umbral, geo_umbral = panel_umbral(umbral, cajas[UMBRAL_DE], E, N, perturbacion)
    partes += p_umbral
    REG["dibujados"].append("g")
    # Rótulos, con halo, encima de todo.
    for fl in fls:
        x, y, anchor = fl["rotulo"]
        EX.texto(partes, E, fl["clave"][1], x, y, E["fs_rotulo"], True, anchor, ("rotulo", fl["i"]),
                 color=E["gris_rotulo"], halo=True)
    bordes = [c["y"] + c["h"] for c in cajas.values()] + [y for fl in fls for _, y in fl["pts"]]
    alto_total = math.ceil(max(bordes) + MARGEN)
    cabeza = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{ANCHO_CM:g}cm" '
              f'height="{ANCHO_CM * alto_total / W:.3f}cm" viewBox="0 0 {W} {alto_total}" '
              f'font-family="{E["sans"]}">',
              f'<rect x="0" y="0" width="{W}" height="{alto_total}" fill="white"/>']
    svg = "\n".join(cabeza + partes + ["</svg>"]) + "\n"
    return svg, T, {"alto": alto_total, "alto_caja": alto, "dy": dy, "cajas": cajas, "flechas": fls,
                    "umbral": geo_umbral}


# --------------------------------------------------------------------------- #
# Controles nuevos (los demás son los de la figura del extractor)              #
# --------------------------------------------------------------------------- #
def controlar_inventario(svg, E, vec):
    """Cajas y relaciones releídas del SVG contra el vecindario del grafo, sin
    las relaciones excluidas a propósito."""
    cajas, relaciones, fallas = EX.inventario_svg(svg, E)
    par = {i: (n["type"], n["label"]) for i, n in vec["nodos"].items()}
    esperadas = [(("caja", list(par.values())), cajas),
                 (("relación", [(par[e["source"]], e["relation"], par[e["target"]]) for e in vec["dibujadas"]]),
                  relaciones)]
    for (nombre, esp), dib in esperadas:
        for x in sorted((Counter(esp) - Counter(dib)).elements(), key=str):
            fallas.append(f"{nombre} del grafo que no está en la figura: {x}")
        for x in sorted((Counter(dib) - Counter(esp)).elements(), key=str):
            fallas.append(f"{nombre} de la figura que no está en el grafo o está excluida: {x}")
    return fallas, cajas, relaciones


def controlar_cruces():
    """Cruces en X entre flechas distintas, con el conteo de la figura del
    esquema final; tienen que ser exactamente los declarados."""
    tramos = [{"red": fl["i"], "pred": fl["clave"], "a": a, "b": b}
              for fl in REG["flechas"] for a, b in zip(fl["pts"], fl["pts"][1:])
              if a[0] == b[0] or a[1] == b[1]]
    puntos, defectos = EF.cruces(tramos)
    fallas = list(defectos)
    if {p: sorted(v) for p, v in puntos.items()} != {p: [par] for p, par in CRUCES_DECLARADOS.items()}:
        fallas.append(f"{len(puntos)} cruce(s) entre flechas, declarados {len(CRUCES_DECLARADOS)}: "
                      + "; ".join(f"{sorted(v)} en {p}" for p, v in sorted(puntos.items())))
    return fallas, puntos


def canonico(el, dy):
    """Un elemento de primer nivel del SVG, con sus coordenadas verticales
    bajadas dy, como tupla comparable."""
    tag = el.tag.replace(NS, "")
    at = dict(el.attrib)
    if tag in ("rect", "text"):
        at["y"] = EF.f(float(at["y"]) + dy)
    elif tag == "path":
        v = EX.numeros(at["d"])
        at["d"] = "M " + " L ".join(f"{EF.f(v[k])} {EF.f(v[k + 1] + dy)}" for k in range(0, len(v), 2))
    elif tag == "polygon":
        v = EX.numeros(at["points"])
        at["points"] = " ".join(f"{EF.f(v[k])},{EF.f(v[k + 1] + dy)}" for k in range(0, len(v), 2))
    return (tag, tuple(sorted(at.items())), el.text or "")


def controlar_conservacion(svg, viejo, cambios, dy):
    """Cada elemento de la figura del extractor, bajado dy, está en esta con los
    mismos atributos y el mismo texto, salvo los cambios declarados: una
    etiqueta cambiada se dibuja en el mismo lugar con el texto del grafo; una
    relación retirada no se dibuja."""
    viejos_el = list(ET.fromstring(viejo["svg"]))[1:]
    viejos = Counter(canonico(el, dy) for el in viejos_el)
    nuevos = Counter(canonico(el, 0) for el in list(ET.fromstring(svg))[1:])
    salen, entran = Counter(), Counter()
    ancho = CAJA_W - 2 * EX.PAD_X
    for c in cambios:
        if c["tipo"] == "etiqueta":
            R = viejo["cajas"][c["rol"]]["R"]
            dentro = sorted((el for el in viejos_el if el.tag == NS + "text" and el.get("font-weight") != "bold"
                             and R[0] < float(el.get("x")) < R[2] and R[1] < float(el.get("y")) < R[3]),
                            key=lambda el: float(el.get("y")))
            for el, s in zip(dentro, EX.envolver(c["despues"], ancho, EX.FS_ETIQUETA)):
                k = canonico(el, dy)
                salen[k] += 1
                entran[(k[0], k[1], s)] += 1
        else:
            j = next(j for j, fl in enumerate(viejo["flechas"]) if fl["clave"] == c["relacion"])
            fl, r = viejo["flechas"][j], viejo["rotulos"][j]
            for el in viejos_el:
                tag = el.tag.replace(NS, "")
                v = EX.numeros(el.get("d") or el.get("points") or "")
                if (tag == "path" and [(v[k], v[k + 1]) for k in range(0, len(v), 2)] == fl["pts"]) or \
                        (tag == "polygon" and (v[0], v[1]) == fl["pts"][-1]) or \
                        (tag == "text" and el.get("stroke") and (float(el.get("x")), float(el.get("y")))
                         == (r["x"], r["y"])):
                    salen[canonico(el, dy)] += 1
    fallas = []
    faltan = viejos - nuevos
    for k in sorted((faltan - salen).elements(), key=str):
        fallas.append(f"elemento de la figura del extractor que no está (bajado {dy:g}): {k[0]} {k[2]!r} "
                      f"{dict(k[1])}")
    for k in sorted((salen - faltan).elements(), key=str):
        fallas.append(f"cambio declarado que no se ve en la figura: {k[0]} {k[2]!r}")
    for k in sorted((entran - nuevos).elements(), key=str):
        fallas.append(f"etiqueta cambiada que no está en su lugar: {k[2]!r}")
    return fallas, sum((viejos - salen).values()), sum(viejos.values())


def controlar_remisiones(svg, N):
    """Las flechas discontinuas son exactamente las rotuladas remite_a, con el
    discontinuo, el gris y el grosor de la figura del esquema final."""
    fallas, raiz = [], ET.fromstring(svg)
    caminos = [el for el in raiz if el.tag == NS + "path"]
    tramos = []
    for el in caminos:
        v = EX.numeros(el.get("d"))
        pts = [(v[k], v[k + 1]) for k in range(0, len(v), 2)]
        tramos.append(list(zip(pts, pts[1:])))
    rotulo = {}
    for t in (el for el in raiz if el.tag == NS + "text" and el.get("stroke")):
        R = EX.rect_texto(t.text, float(t.get("x")), float(t.get("y")), float(t.get("font-size")), True,
                          t.get("text-anchor"))
        d = sorted((min(EF.dist_rect_tramo(R, a, b) for a, b in tr), k) for k, tr in enumerate(tramos))
        if d:
            rotulo.setdefault(d[0][1], []).append(t.text)
    n = 0
    for k, el in enumerate(caminos):
        dash = el.get("stroke-dasharray")
        es_remision = rotulo.get(k) == [REMISION]
        n += bool(dash)
        if bool(dash) != es_remision:
            fallas.append(f"camino {k + 1} ({el.get('d')}): discontinuo {dash!r}, rótulo {rotulo.get(k)}")
        if dash and (dash, el.get("stroke"), float(el.get("stroke-width"))) != (N["dash"], N["gris_remite"],
                                                                              N["grosor_remite"]):
            fallas.append(f"camino {k + 1}: discontinuo, gris o grosor distintos de la figura del esquema final")
    return fallas, n


def controlar_umbral(svg, E, N, umbral, vec):
    """El panel releído del SVG: los campos del grafo, la marca en la primera
    fila, su caja debajo (la que tiene el centro del panel encima, a
    UMBRAL_JUNTO o menos) y nada a menos de UMBRAL_A_FLECHA de una flecha."""
    fallas, raiz = [], ET.fromstring(svg)
    grupos = [el for el in raiz if el.tag == NS + "g" and el.get("data-umbral") is not None]
    if len(grupos) != 1:
        return [f"{len(grupos)} paneles de umbral en el SVG, no uno"], {}
    g = grupos[0]
    marcas = [m for m in g.iter(NS + "g") if m.get("data-umbrales") is not None]
    if len(marcas) != 1:
        return [f"{len(marcas)} marcas en el panel, no una"], {}
    rs, ts = list(marcas[0].iter(NS + "rect")), list(marcas[0].iter(NS + "text"))
    if len(rs) != 1 or len(ts) != 1:
        return ["la marca del panel no es un cuadro y un texto"], {}
    (mr,), (mt,) = rs, ts
    if (float(mr.get("width")), mr.get("fill"), mt.text) != (N["marca"]["lado"], N["marca"]["fill"],
                                                              N["marca"]["texto"]):
        fallas.append("la marca del panel no es la de la figura del esquema final")
    M = (float(mr.get("x")), float(mr.get("y")), float(mr.get("x")) + float(mr.get("width")),
         float(mr.get("y")) + float(mr.get("height")))
    textos = [t for t in g if t.tag == NS + "text"]
    filas = {}
    for t in textos:
        mono = t.get("font-family") == E["mono"]
        filas.setdefault(float(t.get("y")), {}).setdefault("nombre" if mono else "valor", []).append(t)
    campos, actual = [], None
    for y in sorted(filas):
        f = filas[y]
        if len(f.get("valor", [])) != 1 or len(f.get("nombre", [])) > 1:
            fallas.append(f"fila del panel en y = {y:g} sin un valor o con dos nombres")
            continue
        if f.get("nombre"):
            actual = [f["nombre"][0].text, f["valor"][0].text]
            campos.append(actual)
        elif actual is None:
            fallas.append("el panel empieza con una línea sin nombre de campo")
        else:
            actual[1] += " " + f["valor"][0].text
    esperados = [[nombre, valor] for _, nombre, valor in umbral["campos"]]
    if campos != esperados:
        fallas.append(f"campos del panel {campos} ≠ del grafo {esperados}")
    primera = min(filas) if filas else None
    nombre1 = (filas.get(primera) or {}).get("nombre") or []
    if not nombre1 or not M[1] <= primera <= M[3] or M[2] >= float(nombre1[0].get("x")):
        fallas.append("la marca no está a la izquierda de la primera fila del panel")
    rects = [M] + [EX.rect_texto(t.text, float(t.get("x")), float(t.get("y")), float(t.get("font-size")),
                                 t.get("font-family") == E["mono"], t.get("text-anchor")) for t in textos]
    P = EF.bbox([(r[0], r[1]) for r in rects] + [(r[2], r[3]) for r in rects])
    # Cajas releídas del SVG (rectángulo, tipo y etiqueta).
    cajas_svg = []
    hijos = list(raiz)[1:]
    for el in hijos:
        if el.tag == NS + "rect":
            x, y = float(el.get("x")), float(el.get("y"))
            R = (x, y, x + float(el.get("width")), y + float(el.get("height")))
            dentro = sorted((t for t in hijos if t.tag == NS + "text" and not t.get("stroke")
                             and R[0] < float(t.get("x")) < R[2] and R[1] < float(t.get("y")) < R[3]),
                            key=lambda t: (float(t.get("y")), float(t.get("x"))))
            if dentro:
                cajas_svg.append((R, (dentro[0].text, " ".join(t.text for t in dentro[1:]))))
    propia = (vec["nodos"][umbral["nodo"]]["type"], vec["nodos"][umbral["nodo"]]["label"])
    xc = (P[0] + P[2]) / 2.0
    debajo = sorted((R[1] - P[3], par) for R, par in cajas_svg if R[0] <= xc <= R[2] and R[1] >= P[3])
    dist = debajo[0][0] if debajo else math.inf
    if not debajo or debajo[0][1] != propia or dist > UMBRAL_JUNTO:
        fallas.append(f"el panel no está junto a su caja: debajo de su centro {debajo[:1]}, "
                      f"esperada {propia} a {UMBRAL_JUNTO} o menos")
    for R, par in cajas_svg:
        if EF.se_solapan(P, R):
            fallas.append(f"el panel se superpone con la caja {par}")
    a_flecha = min((EF.dist_rect_tramo(r, a, b) for r in rects for fl in REG["flechas"]
                    for a, b in zip(fl["pts"], fl["pts"][1:])), default=math.inf)
    if a_flecha < UMBRAL_A_FLECHA:
        fallas.append(f"un texto o la marca del panel a {a_flecha:.1f} de una flecha (mínimo {UMBRAL_A_FLECHA})")
    return fallas, {"campos": campos, "caja": dist, "a_flecha": a_flecha, "bbox": P}


def controlar_margen_marca(alto_total, geo_umbral):
    x, y, lado = geo_umbral["x"], geo_umbral["y_marca"], geo_umbral["lado"]
    d = min(x, y, W - (x + lado), alto_total - (y + lado))
    return ([f"la marca del umbral a {d:.1f} unidades de un borde"] if d < EX.MARGEN_MIN else []), d


def controlar(viejo, vec, rol, cambios, nuevas, retiradas, umbral, E, N, perturbacion=None):
    """Compone la figura y corre todos los controles."""
    svg, T, geo = componer(viejo, vec, rol, nuevas, retiradas, umbral, E, N, perturbacion)
    alto_total = geo["alto"]
    c, x = {}, {}
    c["inventario"], x["cajas"], x["relaciones"] = controlar_inventario(svg, E, vec)
    c["contenido"] = EX.controlar_contenido(T)
    c["textos"], x["tamanos"], x["minimos"] = EX.controlar_textos(alto_total)
    c["cajas"] = EX.controlar_cajas()
    c["trazos"], x["n_tramos"] = EX.controlar_trazos_svg(svg)
    c["flechas"] = EX.controlar_flechas()
    c["cruces"], x["cruces"] = controlar_cruces()
    x["minimos_margen"], c["margen"], x["n_elem"] = EX.controlar_margen(alto_total)
    falla_marca, x["margen_marca"] = controlar_margen_marca(alto_total, geo["umbral"])
    c["margen"] += falla_marca
    c["conservacion"], x["conservados"], x["viejos"] = controlar_conservacion(svg, viejo, cambios, geo["dy"])
    c["remisiones"], x["n_discontinuas"] = controlar_remisiones(svg, N)
    c["umbral"], x["umbral"] = controlar_umbral(svg, E, N, umbral, vec)
    c["registro"] = EX.controlar_registro(svg)
    return svg, T, geo, c, x


# Prueba negativa -> control que tiene que fallar.
PRUEBAS_NEGATIVAS = (("relacion_de_mas", "inventario"), ("entidad_de_menos", "inventario"),
                     ("rotulo_sobre_caja", "textos"), ("tramo_diagonal", "trazos"),
                     ("cruce_de_flechas", "cruces"), ("remite_continua", "remisiones"),
                     ("umbral_campo_de_menos", "umbral"), ("umbral_lejos", "umbral"),
                     ("caja_movida", "conservacion"), ("retirada_dibujada", "inventario"))


def pruebas_negativas(*a):
    vivas = []
    for caso, control in PRUEBAS_NEGATIVAS:
        _, _, _, c, _ = controlar(*a, perturbacion=caso)
        if not c[control]:
            freno(f"la prueba negativa {caso} no hizo fallar el control de {control}")
        vivas.append((caso, control, c[control][0], sorted(k for k, v in c.items() if v and k != control)))
    return vivas


# --------------------------------------------------------------------------- #
# Principal                                                                    #
# --------------------------------------------------------------------------- #
def argumentos():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--grafo", default=GRAFO_POR_OMISION[0], help="grafo ensamblado (kg.json)")
    ap.add_argument("--sha256-grafo", default=None, help="candado del grafo")
    ap.add_argument("--salida", default=AQUI,
                    help="directorio donde escribir el SVG, el PNG y el PDF (por omisión, el del script)")
    ap.add_argument("--perturbar", choices=[c for c, _ in PRUEBAS_NEGATIVAS], default=None,
                    help="compone la figura con ese defecto: los controles fallan y no se escribe nada")
    args = ap.parse_args()
    if args.sha256_grafo is None:
        if args.grafo != GRAFO_POR_OMISION[0]:
            freno("--grafo distinto del de omisión sin su candado (--sha256-grafo)")
        args.sha256_grafo = GRAFO_POR_OMISION[1]
    return args


def main():
    args = argumentos()
    EX.MEDIR = proc.medidor()
    if EX.MEDIR is None:
        freno("sin las métricas reales de Helvetica (PIL y la fuente del sistema) no se compone la figura")
    viejo = figura_vieja()
    vec = leer_vecindario(args.grafo, args.sha256_grafo)
    E = EX.leer_estilo()
    N = leer_estilo_nuevo()
    leer_lecturas()
    rol, inv, cambios, nuevas, retiradas = emparejar(viejo, vec)
    umbral = leer_umbral(vec, rol)

    print("FUENTES (sha256 comprobado):")
    print(f"  grafo              {args.grafo}   {args.sha256_grafo}")
    print(f"  figura extractor   recompuesta con su generador, SVG {SVG_EXTRACTOR}")
    print(f"  estilo             {EX.ESTILO[0]}   {EX.ESTILO[1]}")
    print(f"  comparación        {REGLAS_COMPARACION[0]}   {REGLAS_COMPARACION[1]}")
    print(f"GRAFO: {vec['n_nodos']} nodos y {vec['n_aristas']} aristas; vecindario de {UNIDAD}: "
          f"{len(vec['nodos'])} nodos y {len(vec['aristas'])} aristas, {len(vec['excluidas'])} de ellas "
          f"excluidas a propósito ({EXCLUIR})")
    for k in sorted(rol):
        n = vec["nodos"][rol[k]]
        prov = procedencias(n)
        print(f"  nodo {k:<12} {n['type']} {n['label']!r}  ({len(prov)} procedencia(s)"
              + (", solo de la unidad" if rol[k] in vec["solo_unidad"] else "") + ")")
    for e in vec["aristas"]:
        clave = (inv[e["source"]], e["relation"], inv[e["target"]])
        extra = {k: v for k, v in e.items() if k not in ("source", "target", "relation", "provenance",
                                                         "provenances")}
        estado = "excluida  " if es_excluida(e) else "nueva     " if clave in nuevas else "conservada"
        print(f"  arista {estado} {clave}  {extra}")
    print(f"CAMBIOS respecto de la figura del extractor: {len(cambios)}")
    for ch in cambios:
        print(f"  {ch}")
    print(f"UMBRAL de {UMBRAL_DE}: {umbral['crudo']}")
    print(f"  comparación {umbral['crudo']['comparacion']!r} -> "
          f"{LECTURA_COMPARACION[umbral['crudo']['comparacion']]!r} (LECTURA_COMPARACION: "
          + "; ".join(f"{k} -> {v}" for k, v in LECTURA_COMPARACION.items()) + ")")
    print(f"ESTILO nuevo (de la figura del esquema final): remite_a {N['gris_remite']} de {N['grosor_remite']:g}, "
          f"discontinua {N['dash']}; marca {N['marca']}")

    a = (viejo, vec, rol, cambios, nuevas, retiradas, umbral, E, N)
    vivas = pruebas_negativas(*a)
    print(f"PRUEBAS NEGATIVAS: {len(vivas)} de {len(PRUEBAS_NEGATIVAS)} hacen fallar su control")
    for caso, control, falla, otros in vivas:
        print(f"  {caso} -> {control}: {falla}" + (f" (fallan también: {', '.join(otros)})" if otros else ""))

    svg, T, geo, c, x = controlar(*a, perturbacion=args.perturbar)
    alto_total = geo["alto"]
    if args.perturbar:
        print(f"PERTURBACIÓN: {args.perturbar}")
    print(f"DISPOSICIÓN: lo que ya estaba baja {geo['dy']:g}; cajas de {CAJA_W} x {geo['alto_caja']}")
    for k, cj in sorted(geo["cajas"].items()):
        print(f"  caja {k:<12} ({cj['x']:g}, {cj['y']:g})")
    for fl in geo["flechas"]:
        print(f"  flecha {fl['clave']}: {[(round(p, 1), round(q, 1)) for p, q in fl['pts']]}"
              + (" discontinua" if fl["discontinua"] else ""))
    print(f"INVENTARIO (releído del SVG): {len(x['cajas'])} cajas y {len(x['relaciones'])} relaciones contra "
          f"{len(vec['nodos'])} y {len(vec['dibujadas'])} del vecindario ({len(vec['aristas'])} aristas, "
          f"{len(vec['excluidas'])} excluidas a propósito); fallas: {len(c['inventario'])}")
    for n in x["cajas"]:
        print(f"  caja     {n[0]} | {n[1]}")
    for o, nombre, d in x["relaciones"]:
        print(f"  relación {o[0]} «{o[1]}» --{nombre}--> {d[0]} «{d[1]}»")
    u = x.get("umbral") or {}
    nombres = {"contenido": f"{len(REG['textos'])} textos, {len(T)} piezas",
               "textos": f"{len(REG['textos'])} textos contra {len(REG['cajas'])} cajas y {len(REG['flechas'])} "
                         "flechas; distancias mínimas "
                         + "; ".join(f"{k} {v:.1f}" for k, v in x["minimos"].items() if math.isfinite(v)),
               "cajas": f"{len(REG['cajas'])} cajas",
               "trazos": f"{x['n_tramos']} tramos en el SVG",
               "flechas": f"{len(REG['flechas'])} flechas",
               "cruces": f"{len(x['cruces'])} cruce(s) entre flechas, declarados {len(CRUCES_DECLARADOS)}"
                         + "".join(f"; {sorted(v)} en {p}" for p, v in sorted(x["cruces"].items())),
               "margen": f"{x['n_elem']} elementos y la marca del umbral; mínimo a cada borde "
                         + ", ".join(f"{b} {v:.1f} u = {v * ANCHO_CM * 10 / W:.2f} mm"
                                     for b, v in x["minimos_margen"].items())
                         + f"; marca {x['margen_marca']:.1f} u; exigido {EX.MARGEN_MM:.1f} mm ({EX.MARGEN_MIN:.1f} u)",
               "conservacion": f"{x['conservados']} de {x['viejos']} elementos de la figura del extractor "
                               f"iguales (bajados {geo['dy']:g}); cambios declarados {len(cambios)}",
               "remisiones": f"{x['n_discontinuas']} flechas discontinuas",
               "umbral": (f"campos {u.get('campos')}; a {u.get('caja', math.inf):.1f} de su caja; "
                          f"a {u.get('a_flecha', math.inf):.1f} de la flecha más cercana"),
               "registro": f"{len(REG['dibujados'])} elementos de primer nivel del SVG"}
    for k in c:
        if k != "inventario":
            print(f"{k.upper()}: {nombres[k]}; fallas: {len(c[k])}")
        for falla in c[k]:
            print(f"  MAL {falla}")
    if any(c.values()):
        raise SystemExit("FALLA: la figura tiene defectos; no se escribe nada")
    for fs in sorted(x["tamanos"]):
        print(f"LETRA {fs} unidades -> {x['tamanos'][fs]:.2f} pt impresos a {ANCHO_CM:g} cm")
    print(f"ALTO: lienzo {W} x {alto_total}, impreso a {ANCHO_CM:.2f} x {ANCHO_CM * alto_total / W:.2f} cm")

    os.makedirs(args.salida, exist_ok=True)
    rutas_s = {e: os.path.join(args.salida, f"{NOMBRE}.{e}") for e in ("svg", "png", "pdf")}
    with open(rutas_s["svg"], "w", encoding="utf-8", newline="\n") as fh:
        fh.write(svg)
    EF.exportar(rutas_s["svg"], rutas_s["png"], rutas_s["pdf"])
    contenido, fecha, caja_pdf = EX.invariantes_pdf(rutas_s["pdf"])
    for e in ("svg", "png", "pdf"):
        print(f"{e.upper()}: {rutas_s[e]}   sha256 {EX.sha256(rutas_s[e])}")
    print(f"     PNG {EF.png_dimensiones(rutas_s['png'])} px; PDF {caja_pdf[0]:.1f} x {caja_pdf[1]:.1f} pt; "
          f"/CreationDate {fecha!r} (SOURCE_DATE_EPOCH={EF.SOURCE_DATE_EPOCH}); "
          f"stream de contenido sha256 {contenido}")


if __name__ == "__main__":
    try:
        main()
    except EF.Freno as e:
        raise SystemExit(f"FRENO {e}")
