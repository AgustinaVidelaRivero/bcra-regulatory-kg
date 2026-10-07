#!/usr/bin/env python3
"""Genera la figura F2 (catálogo de sujetos) del capítulo del esquema, POR
SCRIPT desde los artefactos sellados — nunca dibujada a mano.

Versión 5: el catálogo final y el grafo de la tanda 0 con el perfil final.

Fuentes (se LEEN, jamás se editan; cada una con candado de sha256, que se
comprueba sobre los bytes ANTES de interpretar el JSON):
  data/experiment/catalogo_unico/catalogo_sujetos_r2.json — catálogo r2
      (commit bd2122d): 110 entradas vigentes (70 clases, 5 instancias y 35
      roles de alcance) más 5 lápidas, que no se dibujan.
  data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2b/r2/kg.json —
      grafo de diez documentos de la tanda 0 con el perfil r2b (commit
      bbc38dc): contra él se verifica que CADA arista dibujada existe y que
      las cuatro relaciones de pertenencia (69 subclase_de, 5 instancia_de,
      51 miembro_de, 1 parte_de) son exactamente las del catálogo.

Qué muestra la figura (cinco piezas, las mismas de la versión 4):
  1. La raíz `Sujetos` con sus 4 hijos directos — es un árbol único.
  2. La rama a profundidad completa que cita la prosa:
     Sujetos → Sujetos regulados → Entidades financieras → Bancos →
     Bancos comerciales (verificada contra el artefacto).
  3. Ramas hermanas COLAPSADAS: cada rama no expandida es un solo nodo que
     declara cuántas clases contiene. Dibujadas + colapsadas = 70, asertado.
     Si la rama contiene instancias, el nodo también las declara.
  4. Instancias: `Organismos públicos` con BCRA y SEFyC colgando por
     `instancia_de`, más un nodo colapsado con las demás instancias de esa
     clase. Forma propia (píldora), distinta de las clases.
  5. La indirección: el rol de alcance «Obligados a clasificar deudores
     (Clasificación)» dibujado FUERA del árbol, con las aristas `miembro_de`
     que entran desde las clases dibujadas que lo componen, y la obligación
     del punto 1.1 del TO de Clasificación de deudores («Clasificar clientes
     por calidad de obligados») apuntándolo con `aplica_a`. El camino
     norma → rol → clase → subclase se sigue con el dedo.

Cambios de la versión 5 frente a la 4:
  - Fuentes: el catálogo r2 y el grafo r2b de diez documentos, con candado de
    sha256; los conteos asertados son los suyos.
  - Instancias: FMI es instancia de `Organismos internacionales`, una clase
    que cae dentro del nodo colapsado de `Organismos públicos`; ese nodo la
    declara («+1 instancia»). El nodo de instancias colapsadas agrupa solo
    las que son instancia directa de `Organismos públicos`.
  - Ruteo de `miembro_de` SIN CRUCES: el diente de `Entidades financieras`
    sube recto desde su borde superior hasta el rol, y los de los otros dos
    miembros dibujados salen por un canal a la derecha del árbol, por debajo
    de la última caja de las columnas 3 y 4, suben por fuera de `Bancos
    comerciales` y se unen al diente de `Entidades financieras` antes de la
    punta. El script cuenta los cruces sobre los segmentos dibujados y FRENA
    si hay alguno.

Poda declarada (regla: podar antes que achicar la tipografía): el rol tiene
  6 miembros y se dibujan los 3 que ya son clases dibujadas del árbol; los 3
  restantes (Sociedades de garantía recíproca, Fondos de garantía de carácter
  público y PSCPP) caen dentro del nodo colapsado de `Sujetos regulados`. El
  propio rol lo declara en su caja («6 miembros · 3 dibujados»). De las 5
  instancias se dibujan 2 y se declaran 3.

Distinción en blanco y negro (el informe se imprime sin color): las tres
formas de entrada del catálogo se diferencian por FORMA y TRAZO, no por
color — clase = rectángulo de trazo continuo; clase colapsada = rectángulo
apilado de trazo discontinuo; instancia = píldora; rol = hexágono de trazo
raya-punto; norma = rectángulo con esquina plegada. Las cuatro relaciones se
diferencian por patrón de línea Y por forma de punta, y todas llevan su
nombre sobre el trazo.

Sentido de las flechas: en las cuatro relaciones el `source` es el hijo, el
miembro o la norma, y el `target` el padre o el rol; la punta señala
entonces al padre / al rol, como en la generalización UML. En el árbol
dibujado de izquierda a derecha eso hace que las puntas apunten hacia la
izquierda; es la dirección del artefacto y así se dibuja.

Salida: figura_catalogo_sujetos.svg, junto al script, o en la ruta que se
pase con --salida (para regenerar fuera del repositorio). El PDF y el PNG se
exportan aparte con rsvg-convert (ver LEEME_figura_catalogo_sujetos.md).

Determinístico: sin fechas, sin aleatoriedad, sin rutas absolutas; toda
iteración sobre conjuntos pasa por sorted() o por listas declaradas. Dos
corridas producen bytes idénticos.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
from pathlib import Path

FIG_DIR = Path(__file__).resolve().parent
REPO = FIG_DIR.parents[2]

CATALOGO = (REPO / "data" / "experiment" / "catalogo_unico"
            / "catalogo_sujetos_r2.json")
KG = (REPO / "data" / "experiment" / "reextraccion_v2" / "corpus_tanda0"
      / "ens_diez_r2b" / "r2" / "kg.json")

_ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
_ap.add_argument("--salida", type=Path,
                 default=FIG_DIR / "figura_catalogo_sujetos.svg",
                 help="ruta del SVG de salida (por omisión, junto al script)")
SALIDA = _ap.parse_args().salida

# ========================================================================== #
# 1. Carga de los artefactos + candados de versión                           #
# ========================================================================== #

# Candado de sha256 sobre los bytes de cada fuente: si el archivo cambia, la
# figura deja de describirlo y esto FRENA antes de leer una sola entrada.
SHA_CATALOGO = "c3ad15811c7ea5fa2d0f6cbd56dc775c38dcffd0ae8874c22f5f45c1e82d3a83"
SHA_KG = "a9631a64b422bdae634fb05135373c6f04c6272cdf7acd43a1be9f5b6c1f5f57"


def leer_con_candado(ruta: Path, sha_esperado: str):
    datos = ruta.read_bytes()
    sha = hashlib.sha256(datos).hexdigest()
    assert sha == sha_esperado, (
        f"candado de sha256 roto en {ruta.name}: {sha} != {sha_esperado}")
    return json.loads(datos.decode("utf-8"))


CAT = leer_con_candado(CATALOGO, SHA_CATALOGO)
assert CAT["version"] == "r2", f"catálogo r2 esperado, hay {CAT['version']}"

# Las lápidas (estado distinto de «vigente») son entradas retiradas: quedan en
# el archivo para que un id viejo no se reutilice, pero no son parte del
# catálogo vigente y no se dibujan.
VIGENTES = [s for s in CAT["sujetos"] if s["estado"]["valor"] == "vigente"]
LAPIDAS = [s for s in CAT["sujetos"] if s["estado"]["valor"] != "vigente"]
ENTRADAS = {s["id"]: s for s in VIGENTES}
assert len(ENTRADAS) == len(VIGENTES), "ids repetidos entre las vigentes"
CLASES = [s["id"] for s in VIGENTES if s["nivel"] == "clase"]
INSTANCIAS = [s["id"] for s in VIGENTES if s["nivel"] == "instancia"]
ROLES = {s["id"]: s for s in VIGENTES if s["nivel"] == "rol"}
N_CLASES = 70

assert len(CLASES) == N_CLASES, f"70 clases esperadas, hay {len(CLASES)}"
assert len(INSTANCIAS) == 5, f"5 instancias esperadas, hay {len(INSTANCIAS)}"
assert len(ROLES) == 35, f"35 roles esperados, hay {len(ROLES)}"
assert len(VIGENTES) == 110, f"110 vigentes esperadas, hay {len(VIGENTES)}"
assert len(LAPIDAS) == 5, f"5 lápidas esperadas, hay {len(LAPIDAS)}"

HIJOS = collections.defaultdict(list)
for _cid in CLASES:
    _p = ENTRADAS[_cid].get("padre")
    if _p is not None:
        assert _p in ENTRADAS, f"{_cid} cuelga de {_p}, que no está vigente"
        HIJOS[_p].append(_cid)          # orden = orden del artefacto

RAICES = [c for c in CLASES if ENTRADAS[c].get("padre") is None]
assert RAICES == ["Sujeto_sujeto"], f"raíz única esperada, hay {RAICES}"
RAIZ = RAICES[0]


def subarbol(nodo: str) -> int:
    """Clases del subárbol de `nodo`, el propio nodo incluido."""
    return 1 + sum(subarbol(h) for h in HIJOS[nodo])


# Las cuatro ramas que cuelgan de la raíz, con su tamaño (cada una cuenta su
# propia clase): 38 + 20 + 6 + 5 = 69, más la raíz, 70.
RAMAS = {"Sujeto_sujeto_regulado": 38, "Sujeto_contraparte": 20,
         "Sujeto_organismo_publico": 6, "Sujeto_estructura": 5}
assert HIJOS[RAIZ] == list(RAMAS), f"ramas de la raíz: {HIJOS[RAIZ]}"
for _r, _n in RAMAS.items():
    assert subarbol(_r) == _n, f"rama {_r}: {subarbol(_r)} clases, esperado {_n}"
assert 1 + sum(RAMAS.values()) == N_CLASES

# Pertenencia declarada en el catálogo: las cuatro relaciones de taxonomía.
PERTENENCIA_CAT = {
    "subclase_de": {(c, "subclase_de", ENTRADAS[c]["padre"]) for c in CLASES
                    if ENTRADAS[c].get("padre") is not None},
    "instancia_de": {(i, "instancia_de", ENTRADAS[i]["instancia_de"])
                     for i in INSTANCIAS},
    "miembro_de": {(m, "miembro_de", r) for r in ROLES
                   for m in ROLES[r]["rol"]["miembros"]},
    "parte_de": {(s["id"], "parte_de", s["parte_de"]) for s in VIGENTES
                 if s.get("parte_de")},
}
for _rel, _n in (("subclase_de", 69), ("instancia_de", 5),
                 ("miembro_de", 51), ("parte_de", 1)):
    assert len(PERTENENCIA_CAT[_rel]) == _n, (
        f"catálogo: {_rel} = {len(PERTENENCIA_CAT[_rel])}, esperado {_n}")
assert all(t in ENTRADAS for _a in PERTENENCIA_CAT.values() for _, _, t in _a)

# ========================================================================== #
# 2. Qué se dibuja (declarado) y qué se colapsa (derivado)                    #
# ========================================================================== #

# Cadena a profundidad completa que cita la prosa, verificada contra el
# artefacto: si el catálogo cambiara, el assert frena antes de dibujar.
CADENA = ["Sujeto_sujeto", "Sujeto_sujeto_regulado", "Sujeto_entidad_financiera",
          "Sujeto_banco", "Sujeto_banco_comercial"]
for _i, _n in enumerate(CADENA):
    _esperado = CADENA[_i - 1] if _i else None
    assert ENTRADAS[_n].get("padre") == _esperado, (
        f"la cadena citada no es la del artefacto en {_n}: padre real "
        f"{ENTRADAS[_n].get('padre')!r}, esperado {_esperado!r}")

ROL = "Sujeto_rol_obligado_a_clasificar_clasificacion"
TO_ROL = "TO_clasificacion_deudores_actual.pdf"
MIEMBROS_ROL = ROLES[ROL]["rol"]["miembros"]
assert len(MIEMBROS_ROL) == 6, f"6 miembros esperados, hay {len(MIEMBROS_ROL)}"
assert ROLES[ROL]["rol_por_to"] == [TO_ROL]
assert ROLES[ROL]["provenance_esqueleto"]["source_doc"] == TO_ROL

# Norma real del TO de Clasificación de deudores (punto 1.1) que apunta al rol
# con aplica_a. Su etiqueta y su procedencia se assertan en §3, contra el kg.
NORMA = ("Obligacion_los_clientes_de_la_entidad_tanto_residentes_en_el_pais_"
         "de_los_sectores_publico_y_8b3c06")
NORMA_LABEL_ESPERADA = "Clasificar clientes por calidad de obligados"

CLASES_DIBUJADAS = [
    "Sujeto_sujeto",
    "Sujeto_sujeto_regulado",
    "Sujeto_entidad_financiera",
    "Sujeto_banco",
    "Sujeto_banco_comercial",
    "Sujeto_entidad_cambiaria",
    "Sujeto_proveedor_no_financiero_de_credito",
    "Sujeto_empresa_no_financiera_emisora_de_tarjetas",
    "Sujeto_fiduciario_de_fideicomiso_financiero",
    "Sujeto_contraparte",
    "Sujeto_organismo_publico",
    "Sujeto_estructura",
]
SET_DIB = set(CLASES_DIBUJADAS)
assert len(SET_DIB) == len(CLASES_DIBUJADAS)
assert SET_DIB <= set(CLASES), "hay un id dibujado que no está en el catálogo"

INSTANCIAS_DIBUJADAS = ["Sujeto_bcra", "Sujeto_sefyc"]
MIEMBROS_DIBUJADOS = [m for m in MIEMBROS_ROL if m in SET_DIB]


def ancestro_dibujado(nodo: str) -> str:
    p = ENTRADAS[nodo].get("padre")
    while p is not None:
        if p in SET_DIB:
            return p
        p = ENTRADAS[p].get("padre")
    raise AssertionError(f"{nodo} no cuelga de ninguna clase dibujada")


GRUPOS: dict[str, list[str]] = collections.defaultdict(list)
for _cid in CLASES:
    if _cid not in SET_DIB:
        GRUPOS[ancestro_dibujado(_cid)].append(_cid)

# Conteo: dibujadas + colapsadas = 70, y los grupos son disjuntos y cubren
# exactamente el complemento de lo dibujado.
_union = [n for g in GRUPOS.values() for n in g]
assert len(_union) == len(set(_union)), "los grupos colapsados se solapan"
assert set(_union) == set(CLASES) - SET_DIB, "los grupos no cubren el resto"
N_COLAPSADAS = len(_union)
assert len(CLASES_DIBUJADAS) + N_COLAPSADAS == N_CLASES, (
    f"{len(CLASES_DIBUJADAS)} + {N_COLAPSADAS} != {N_CLASES}")

# Instancias. Tres destinos posibles, disjuntos: dibujada; instancia directa
# de `Organismos públicos` sin dibujar (va al nodo «+N instancias»); o
# instancia de una clase que cae dentro de un grupo colapsado (la declara el
# nodo colapsado de ese grupo). Ninguna queda sin contar.
OP = "Sujeto_organismo_publico"
assert all(ENTRADAS[i]["instancia_de"] == OP for i in INSTANCIAS_DIBUJADAS)
INSTANCIAS_COLAPSADAS = [i for i in INSTANCIAS
                         if i not in INSTANCIAS_DIBUJADAS
                         and ENTRADAS[i]["instancia_de"] == OP]
INSTANCIAS_EN_RAMA: dict[str, list[str]] = collections.defaultdict(list)
for _i in INSTANCIAS:
    if _i in INSTANCIAS_DIBUJADAS or _i in INSTANCIAS_COLAPSADAS:
        continue
    _cls = ENTRADAS[_i]["instancia_de"]
    assert _cls in set(_union), (
        f"la instancia {_i} cuelga de {_cls}, que no es dibujada ni colapsada")
    INSTANCIAS_EN_RAMA[ancestro_dibujado(_cls)].append(_i)
assert (len(INSTANCIAS_DIBUJADAS) + len(INSTANCIAS_COLAPSADAS)
        + sum(len(v) for v in INSTANCIAS_EN_RAMA.values()) == len(INSTANCIAS))

MIEMBROS_NO_DIBUJADOS = [m for m in MIEMBROS_ROL if m not in MIEMBROS_DIBUJADOS]
assert len(MIEMBROS_DIBUJADOS) + len(MIEMBROS_NO_DIBUJADOS) == len(MIEMBROS_ROL)
# Los miembros no dibujados tienen que estar DENTRO de algún grupo colapsado:
# la figura no pierde ninguno, los declara.
assert all(m in set(_union) for m in MIEMBROS_NO_DIBUJADOS)

# ========================================================================== #
# 3. Verificación contra el grafo                                            #
# ========================================================================== #

_kg = leer_con_candado(KG, SHA_KG)
NODOS_KG = {n["id"]: n for n in _kg["nodes"]}
ARISTAS_KG = {(e["source"], e["relation"], e["target"]) for e in _kg["edges"]}
_cnt = collections.Counter(e["relation"] for e in _kg["edges"])
for _rel, _n in (("subclase_de", 69), ("instancia_de", 5),
                 ("miembro_de", 51), ("parte_de", 1)):
    assert _cnt[_rel] == _n, f"kg: {_rel} = {_cnt[_rel]}, esperado {_n}"
    # Más fuerte que el conteo: las aristas del grafo son exactamente las que
    # declara el catálogo, una por una.
    _kg_rel = {(s, r, t) for s, r, t in ARISTAS_KG if r == _rel}
    assert _kg_rel == PERTENENCIA_CAT[_rel], (
        f"kg y catálogo difieren en {_rel}: "
        f"{sorted(_kg_rel ^ PERTENENCIA_CAT[_rel])[:5]}")

# El rol tiene en el grafo exactamente los miembros que declara el catálogo.
assert ({s for s, r, t in ARISTAS_KG if r == "miembro_de" and t == ROL}
        == set(MIEMBROS_ROL)), (
    "los miembro_de del rol en el kg no coinciden con el catálogo")

# Aristas EXPLÍCITAS (un trazo dibujado = una arista del grafo).
ARISTAS_EXPLICITAS: list[tuple[str, str, str]] = []
for _c in CLASES_DIBUJADAS:
    _p = ENTRADAS[_c].get("padre")
    if _p is not None:
        assert _p in SET_DIB
        ARISTAS_EXPLICITAS.append((_c, "subclase_de", _p))
for _i in INSTANCIAS_DIBUJADAS:
    ARISTAS_EXPLICITAS.append((_i, "instancia_de", ENTRADAS[_i]["instancia_de"]))
for _m in MIEMBROS_DIBUJADOS:
    ARISTAS_EXPLICITAS.append((_m, "miembro_de", ROL))
ARISTAS_EXPLICITAS.append((NORMA, "aplica_a", ROL))

# Aristas AGREGADAS: el trazo que llega a un nodo colapsado representa las
# aristas subclase_de (o instancia_de) directas de ese grupo hacia el padre
# dibujado. Se verifican una por una igual que las explícitas. Las aristas
# internas de un grupo (entre dos clases colapsadas, o la instancia_de de una
# instancia de rama) no tienen trazo: quedan dentro del nodo que las declara.
ARISTAS_AGREGADAS: dict[str, list[tuple[str, str, str]]] = {}
for _p, _g in GRUPOS.items():
    ARISTAS_AGREGADAS[_p] = sorted(
        (n, "subclase_de", _p) for n in _g if ENTRADAS[n]["padre"] == _p)
ARISTAS_AGREGADAS["__instancias__"] = sorted(
    (i, "instancia_de", ENTRADAS[i]["instancia_de"])
    for i in INSTANCIAS_COLAPSADAS)

# --- El camino que la figura existe para mostrar -------------------------- #
# Cinco nodos y cuatro aristas: la norma apunta al rol, el rol recibe a
# Entidades financieras, y de ahí el árbol baja a Bancos y a Bancos
# comerciales. Se resalta como una unidad; el resto del dibujo va atenuado.
CAMINO_NODOS = ["NORMA", "ROL", "Sujeto_entidad_financiera", "Sujeto_banco",
                "Sujeto_banco_comercial"]
CAMINO_ARISTAS = [
    (NORMA, "aplica_a", ROL),
    ("Sujeto_entidad_financiera", "miembro_de", ROL),
    ("Sujeto_banco", "subclase_de", "Sujeto_entidad_financiera"),
    ("Sujeto_banco_comercial", "subclase_de", "Sujeto_banco"),
]
# El camino es una cadena: cada arista une dos nodos consecutivos de la lista
# (en un sentido o en el otro — la dirección la pone el artefacto, no la
# lectura). Si dejara de serlo, el resalte estaría mintiendo y esto frena.
_clave = {NORMA: "NORMA", ROL: "ROL"}
assert len(CAMINO_ARISTAS) == len(CAMINO_NODOS) - 1
for _i, (_s, _r, _t) in enumerate(CAMINO_ARISTAS):
    _par = {_clave.get(_s, _s), _clave.get(_t, _t)}
    assert _par == {CAMINO_NODOS[_i], CAMINO_NODOS[_i + 1]}, (
        f"el camino no es una cadena en el paso {_i}: {_par} != "
        f"{{{CAMINO_NODOS[_i]}, {CAMINO_NODOS[_i + 1]}}}")
# Las cuatro son aristas reales y ya están entre las que la figura dibuja una
# a una (no son agregados de un nodo colapsado).
assert all(a in ARISTAS_EXPLICITAS for a in CAMINO_ARISTAS)
assert all(a in ARISTAS_KG for a in CAMINO_ARISTAS)
# El camino usa las tres relaciones de la indirección más la del árbol.
assert {r for _, r, _ in CAMINO_ARISTAS} == {"aplica_a", "miembro_de",
                                             "subclase_de"}
EN_CAMINO = set(CAMINO_NODOS)

TODAS_LAS_ARISTAS = ARISTAS_EXPLICITAS + [
    a for k in sorted(ARISTAS_AGREGADAS) for a in ARISTAS_AGREGADAS[k]]
_faltan = [a for a in TODAS_LAS_ARISTAS if a not in ARISTAS_KG]
assert not _faltan, f"aristas dibujadas ausentes del kg: {_faltan}"
assert len(TODAS_LAS_ARISTAS) == len(set(TODAS_LAS_ARISTAS)), (
    "una arista quedó representada dos veces")

# Los nodos que no vienen del catálogo (la norma y el rol) existen en el kg
# y se dibujan con SU etiqueta.
assert NORMA in NODOS_KG and NODOS_KG[NORMA]["type"] == "Obligacion"
assert ROL in NODOS_KG and NODOS_KG[ROL]["label"] == ROLES[ROL]["label"]
for _c in CLASES_DIBUJADAS + INSTANCIAS_DIBUJADAS:
    assert NODOS_KG[_c]["label"] == ENTRADAS[_c]["label"], (
        f"etiqueta distinta en el kg y en el catálogo: {_c}")

_pn = NODOS_KG[NORMA]["provenance"]
NORMA_TIPO = NODOS_KG[NORMA]["type"]
NORMA_LABEL = NODOS_KG[NORMA]["label"]
NORMA_PUNTO = _pn["punto"]
NORMA_PAGS = _pn["paginas"]
# La norma es la obligación del punto 1.1 del TO de Clasificación de deudores.
assert NORMA_LABEL == NORMA_LABEL_ESPERADA, f"etiqueta de la norma: {NORMA_LABEL!r}"
assert (_pn["to"], _pn["archivo"], NORMA_PUNTO) == (
    "cla", TO_ROL, "1.1"), f"procedencia: {_pn}"
# Y es la única Obligacion del punto 1.1 de ese TO en el grafo.
assert [n["id"] for n in _kg["nodes"] if n["type"] == "Obligacion"
        and n.get("provenance", {}).get("to") == "cla"
        and n.get("provenance", {}).get("punto") == "1.1"] == [NORMA]

# ========================================================================== #
# 4. Estilo                                                                  #
# ========================================================================== #

TIPO_SANS = "Helvetica,Arial,sans-serif"
TIPO_MONO = "Menlo,Consolas,'Courier New',monospace"

C_CLASE = "#2a6f97"        # clases del árbol
C_COLAPSADA = "#6f6f6f"    # ramas no expandidas
C_INSTANCIA = "#6d597a"    # instancias
C_ROL = "#b5179e"          # rol de alcance (la indirección)
C_NORMA = "#b23a48"        # norma
C_TEXTO = "#1a1a1a"
C_NOTA = "#5c5c5c"
BLANCO = "#ffffff"

# Tipografía. El piso es duro: ningún texto por debajo de PT_MIN puntos
# impresos a width=\linewidth. El assert vive en §6, cuando se conoce el
# ancho final del lienzo.
LINEWIDTH_MM = 150.0  # a4 con márgenes laterales de 3 cm (docs/tesis/main.tex:13)
PT_MIN = 8.0

ANCHO_MONO = 0.60    # avance por carácter de la familia monoespaciada

FS_NODO = 29
FS_SUB = 27          # subtítulo dentro de una caja (tipo, procedencia)
FS_REL = 27          # rótulo de relación
FS_LEY = 27          # leyenda

AN_BASE = 1.7
AN_ROL = 2.4
AN_APLICA = 3.0
OFF_MEM = 13          # separación vertical del diente miembro_de
INSET_ROL = 18        # sangrado de los lados oblicuos del hexágono del rol
PLIEGUE_NORMA = 16    # esquina plegada de la caja de norma

# --- Las dos intensidades ------------------------------------------------- #
# El camino resaltado se distingue por TRAZO y por SATURACIÓN DEL RELLENO,
# las dos legibles en blanco y negro; el color sigue siendo redundante.
AN_CAMINO = 4.6       # trazo de las cuatro aristas del camino
AN_ATENUADO = 1.9     # trazo del resto de las aristas
AN_NODO_CAMINO = 4.0  # borde de los cinco nodos del camino
AN_NODO_ATENUADO = 1.9
REL_CAMINO = 0.66     # relleno de los nodos del camino (más saturado)
REL_ATENUADO = 0.94   # relleno del resto (casi blanco)
TRAZO_ATENUADO = 0.42  # cuánto se aclara el color de lo que no es camino

PAD_X, PAD_Y = 13, 9
LH = 34              # interlineado del label
LH_SUB = 31


def mezcla(color: str, blanco: float) -> str:
    r, g, b = (int(color[i:i + 2], 16) for i in (1, 3, 5))
    m = [round(c + (255 - c) * blanco) for c in (r, g, b)]
    return "#{:02x}{:02x}{:02x}".format(*m)


def f(v: float) -> str:
    s = f"{v:.1f}"
    return s[:-2] if s.endswith(".0") else s


def esc(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


# --- métrica de texto (Helvetica, anchos AFM /1000) ----------------------- #
_W = {
    " ": 278, "!": 278, '"': 355, "#": 556, "$": 556, "%": 889, "&": 667,
    "'": 191, "(": 333, ")": 333, "*": 389, "+": 584, ",": 278, "-": 333,
    ".": 278, "/": 278, ":": 278, ";": 278, "?": 556, "@": 1015, "[": 278,
    "]": 278, "_": 556, "{": 334, "|": 260, "}": 334, "·": 278, "«": 333,
    "»": 333, "—": 1000, "→": 1000,
}
for _c in "0123456789":
    _W[_c] = 556
for _c, _w in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                  (667, 667, 722, 722, 667, 611, 778, 722, 278, 500, 667, 556,
                   833, 722, 778, 667, 778, 722, 667, 611, 722, 667, 944, 667,
                   667, 611)):
    _W[_c] = _w
for _c, _w in zip("abcdefghijklmnopqrstuvwxyz",
                  (556, 556, 500, 556, 556, 278, 556, 556, 222, 222, 500, 222,
                   833, 556, 556, 556, 556, 333, 500, 278, 556, 500, 722, 500,
                   500, 500)):
    _W[_c] = _w
for _a, _b in (("á", "a"), ("é", "e"), ("ó", "o"), ("ú", "u"), ("ñ", "n"),
               ("ü", "u"), ("Á", "A"), ("É", "E"), ("Í", "I"), ("Ó", "O"),
               ("Ú", "U"), ("Ñ", "N")):
    _W[_a] = _W[_b]
_W["í"] = 278


def ancho(texto: str, fs: float, bold: bool = False) -> float:
    tot = sum(_W.get(c, 556) for c in texto)
    return tot / 1000.0 * fs * (1.09 if bold else 1.0)


def envolver(texto: str, fs: float, maxw: float, bold: bool = False) -> list[str]:
    lineas: list[str] = []
    actual = ""
    for pal in texto.split():
        cand = f"{actual} {pal}".strip()
        if actual and ancho(cand, fs, bold) > maxw:
            lineas.append(actual)
            actual = pal
        else:
            actual = cand
    if actual:
        lineas.append(actual)
    return lineas


# ========================================================================== #
# 5. Cajas: medida y contenido                                               #
# ========================================================================== #

class Caja:
    """Caja medida a partir de su texto: nada se dibuja fuera de su borde.

    El label y los subtítulos se envuelven al ancho máximo de la columna y el
    constructor ASSERTA que ninguna línea desborda el interior de la caja —
    una etiqueta cortada es un defecto que no puede llegar al informe.
    """

    def __init__(self, clave, forma, lineas, sub, color, maxw):
        self.clave = clave
        self.forma = forma            # clase | colapsada | instancia | rol | norma
        self.lineas = lineas
        self.sub = sub                # líneas de subtítulo, ya envueltas
        self.color = color
        anchos = ([ancho(l, FS_NODO, True) for l in lineas]
                  + [ancho(s, FS_SUB) for s in sub])
        self.w = min(maxw, max(anchos)) + 2 * PAD_X
        self.h = len(lineas) * LH + len(sub) * LH_SUB + 2 * PAD_Y
        if forma == "instancia":
            self.w += 14              # las píldoras necesitan aire en los topes
        if forma == "rol":
            self.w += 2 * INSET_ROL   # los lados oblicuos del hexágono comen
        if forma == "norma":
            self.w += PLIEGUE_NORMA   # la esquina plegada come el ángulo
        interior = (self.w - 2 * PAD_X
                    - (2 * INSET_ROL if forma == "rol" else 0)
                    - (PLIEGUE_NORMA if forma == "norma" else 0))
        for l, fs, bold in ([(l, FS_NODO, True) for l in lineas]
                            + [(s, FS_SUB, False) for s in sub]):
            assert ancho(l, fs, bold) <= interior + 0.5, (
                f"la línea {l!r} de {clave} desborda su caja "
                f"({f(ancho(l, fs, bold))} > {f(interior)})")
        self.x = 0.0
        self.y = 0.0                  # centro vertical


# La norma sube de 300 a 310 px: con 300, «Clasificar clientes por» (300,4
# px) no entra y la etiqueta se parte en tres líneas, la última de una sola
# palabra; con 310 queda en dos.
MAXW = {0: 189, 1: 245, 2: 259, 3: 303, 4: 192,
        "rol": 400, "norma": 310}

CAJAS: dict[str, Caja] = {}


def nueva(clave, forma, texto, sub, color, col):
    maxw = MAXW[col]
    c = Caja(clave, forma,
             envolver(texto, FS_NODO, maxw, True),
             [l for s in sub for l in envolver(s, FS_SUB, maxw)],
             color, maxw)
    c.col = col
    CAJAS[clave] = c
    return c


COL_DE = {
    "Sujeto_sujeto": 0,
    "Sujeto_sujeto_regulado": 1, "Sujeto_contraparte": 1,
    "Sujeto_organismo_publico": 1, "Sujeto_estructura": 1,
    "Sujeto_entidad_financiera": 2, "Sujeto_entidad_cambiaria": 2,
    "Sujeto_proveedor_no_financiero_de_credito": 2,
    "Sujeto_fiduciario_de_fideicomiso_financiero": 2,
    "Sujeto_banco": 3, "Sujeto_empresa_no_financiera_emisora_de_tarjetas": 3,
    "Sujeto_banco_comercial": 4,
}
for _c in CLASES_DIBUJADAS:
    nueva(_c, "clase", ENTRADAS[_c]["label"], [], C_CLASE, COL_DE[_c])

COL_COLAPSADA = {
    "Sujeto_sujeto_regulado": 2, "Sujeto_contraparte": 2,
    "Sujeto_organismo_publico": 2, "Sujeto_estructura": 2,
    "Sujeto_entidad_financiera": 3, "Sujeto_entidad_cambiaria": 3,
}
def n_instancias(k: int) -> str:
    return f"+{k} instancia" + ("" if k == 1 else "s")


for _p in CLASES_DIBUJADAS:
    if _p in GRUPOS:
        n = len(GRUPOS[_p])
        # Sin subtítulo: «rama no expandida» ya lo dice la leyenda por la
        # forma, y el alto que ocupaba se gasta en tipografía. La excepción es
        # la rama que contiene instancias: el subtítulo las declara, para que
        # la figura no pierda ninguna.
        _ins = INSTANCIAS_EN_RAMA.get(_p, [])
        _caja = nueva(f"COL:{_p}", "colapsada", f"+{n} clases",
                      [n_instancias(len(_ins))] if _ins else [],
                      C_COLAPSADA, COL_COLAPSADA[_p])
        _caja.colapsa = n
        _caja.instancias = len(_ins)


def sigla(label: str) -> str:
    """La sigla con la que el catálogo abre la etiqueta de una instancia.

    Las dos instancias dibujadas traen el nombre desplegado entre paréntesis
    («BCRA (Banco Central de la República Argentina)»). En la figura entra
    solo la sigla —las instancias son el punto menos importante de la
    subsección— y el nombre completo va al epígrafe. No se inventa nada: la
    sigla es un prefijo literal del `label` del artefacto, y esto lo asserta.
    """
    s = label.split(" (")[0].strip()
    assert s and label.startswith(s) and s != label, (
        f"la etiqueta {label!r} no tiene la forma «SIGLA (nombre)»")
    return s


for _i in INSTANCIAS_DIBUJADAS:
    _caja = nueva(_i, "instancia", sigla(ENTRADAS[_i]["label"]), [],
                  C_INSTANCIA, 2)
    _caja.label_artefacto = ENTRADAS[_i]["label"]   # queda en el SVG
nueva("INSTCOL", "colapsada", n_instancias(len(INSTANCIAS_COLAPSADAS)),
      [], C_COLAPSADA, 2).colapsa = len(INSTANCIAS_COLAPSADAS)

# Una sola línea de subtítulo en cada caja de la banda, y estructural: la
# procedencia completa (documento, punto y páginas) va al epígrafe, que es
# donde no cuesta alto de figura.
nueva("ROL", "rol", ROLES[ROL]["label"],
      [f"{len(MIEMBROS_ROL)} miembros · "
       f"{len(MIEMBROS_DIBUJADOS)} dibujados"],
      C_ROL, "rol")
# El tipo va como identificador del esquema, sin tilde («Obligacion»), igual
# que en F1; la etiqueta de la norma es la del grafo, en castellano.
nueva("NORMA", "norma", NORMA_LABEL,
      [f"{NORMA_TIPO} · punto {NORMA_PUNTO}"], C_NORMA, "norma")

# ========================================================================== #
# 6. Geometría                                                               #
# ========================================================================== #

MARGEN = 26
GAPS = [48, 74, 82, 48]          # C0-C1, C1-C2, C2-C3, C3-C4

_anchos_col = {}
for _cl, _c in CAJAS.items():
    if _c.col in ("rol", "norma"):
        continue
    _anchos_col[_c.col] = max(_anchos_col.get(_c.col, 0), _c.w)

_x = float(MARGEN)
X_COL, W_COL = {}, {}
for _k in range(5):
    X_COL[_k] = _x
    W_COL[_k] = _anchos_col[_k]
    _x += _anchos_col[_k] + (GAPS[_k] if _k < 4 else 0)
X_FIN_ARBOL = _x                 # borde derecho de la última columna

for _cl, _c in CAJAS.items():
    if _c.col not in ("rol", "norma"):
        _c.x = X_COL[_c.col]        # alineación a izquierda dentro de la columna

# Troncos verticales -------------------------------------------------------
X_SUB_01 = X_COL[0] + W_COL[0] + 24          # comb de la raíz
X_SUB_12 = X_COL[1] + W_COL[1] + 24          # combs de nivel 1 → 2
X_INS_12 = X_COL[1] + W_COL[1] + 50          # instancia_de
X_MEM_23 = X_COL[2] + W_COL[2] + 18          # miembro_de: bajada de los dientes
X_SUB_23 = X_COL[2] + W_COL[2] + 42          # combs de nivel 2 → 3
X_SUB_34 = X_COL[3] + W_COL[3] + 24

# Banda superior: norma + rol ---------------------------------------------
rol, norma = CAJAS["ROL"], CAJAS["NORMA"]
_ef = CAJAS["Sujeto_entidad_financiera"]
# El diente de miembro_de de Entidades financieras sube recto desde el centro
# de su borde superior hasta el borde inferior del rol: es el tramo del camino
# y no cruza nada, porque encima de esa caja la columna 2 está vacía. El rol
# se centra sobre esa vertical si la banda lo permite; si no, se corre a la
# derecha lo justo para que el rótulo de aplica_a entre entre la norma y el
# rol. La norma se apoya en el margen izquierdo, que el árbol deja libre en
# esa banda.
X_EF_MEM = _ef.x + _ef.w / 2.0
norma.x = float(MARGEN)
_ancho_rotulo = ANCHO_MONO * FS_REL * len("aplica_a") + 20
rol.x = max(X_EF_MEM - rol.w / 2.0, norma.x + norma.w + _ancho_rotulo + 24)
assert rol.x - (norma.x + norma.w) >= _ancho_rotulo, (
    f"el tramo de aplica_a ({f(rol.x - norma.x - norma.w)} px) no alcanza "
    f"para su rótulo ({f(_ancho_rotulo)} px)")
# La punta entra por el lado plano de abajo del hexágono, no por una esquina.
assert rol.x + INSET_ROL + 8 <= X_EF_MEM <= rol.x + rol.w - INSET_ROL - 8, (
    "la vertical de Entidades financieras no cae en el lado inferior del rol")
Y_BANDA = MARGEN + max(rol.h, norma.h) / 2.0
rol.y = norma.y = Y_BANDA

# Filas del árbol ----------------------------------------------------------
FILAS = [
    ["Sujeto_banco_comercial", "Sujeto_banco"],
    ["COL:Sujeto_entidad_financiera"],
    ["COL:Sujeto_entidad_cambiaria", "Sujeto_entidad_cambiaria"],
    ["Sujeto_empresa_no_financiera_emisora_de_tarjetas",
     "Sujeto_proveedor_no_financiero_de_credito"],
    ["Sujeto_fiduciario_de_fideicomiso_financiero"],
    ["COL:Sujeto_sujeto_regulado"],
    ["COL:Sujeto_contraparte", "Sujeto_contraparte"],
    ["COL:Sujeto_organismo_publico"],
    ["Sujeto_bcra"],
    ["Sujeto_sefyc"],
    ["INSTCOL"],
    ["COL:Sujeto_estructura", "Sujeto_estructura"],
]
SEP_FILA = 14
# 56 px entre la banda y el árbol (42 en la versión 4): por ese hueco corre el
# tramo horizontal de miembro_de que une el canal de la derecha con la
# vertical de Entidades financieras, con aire a los dos lados.
Y_ARBOL = Y_BANDA + max(rol.h, norma.h) / 2.0 + 56

_y = Y_ARBOL
Y_FILA = []
for _fila in FILAS:
    _h = max(CAJAS[k].h for k in _fila)
    Y_FILA.append(_y + _h / 2.0)
    _y += _h + SEP_FILA
ALTO_ARBOL = _y - SEP_FILA

for _i, _fila in enumerate(FILAS):
    for _k in _fila:
        CAJAS[_k].y = Y_FILA[_i]

# Padres cuya y es el punto medio de sus hijos dibujados
CAJAS["Sujeto_entidad_financiera"].y = (Y_FILA[0] + Y_FILA[1]) / 2.0
CAJAS["Sujeto_organismo_publico"].y = (Y_FILA[7] + Y_FILA[10]) / 2.0
CAJAS["Sujeto_sujeto_regulado"].y = (
    CAJAS["Sujeto_entidad_financiera"].y + Y_FILA[5]) / 2.0
CAJAS["Sujeto_sujeto"].y = (
    CAJAS["Sujeto_sujeto_regulado"].y + CAJAS["Sujeto_estructura"].y) / 2.0

# Ruteo de miembro_de sin cruces -------------------------------------------
# En la versión 4 los tres dientes confluían en un tronco vertical a la
# derecha de la columna 2 que subía hasta el rol, y ese tronco cortaba las
# tres flechas subclase_de que entran por la derecha a Entidades financieras,
# Entidades cambiarias y Proveedores no financieros de crédito (3 cruces).
# Ahora:
#   - Entidades financieras (el miembro más alto, y el del camino) sube recto
#     desde su borde superior hasta el rol, en X_EF_MEM;
#   - los demás miembros dibujados sacan su diente por la derecha a X_MEM_23,
#     bajan hasta Y_MEM_CANAL (el diente del miembro más bajo), y de ahí el
#     tronco corre a la derecha por debajo de la última caja de las columnas 3
#     y 4, sube por fuera de Bancos comerciales (X_MEM_CANAL) y vuelve por el
#     hueco entre la banda y el árbol (Y_MEM_UNION) hasta la vertical de
#     Entidades financieras, donde se une antes de la punta.
_otros = [m for m in MIEMBROS_DIBUJADOS if m != "Sujeto_entidad_financiera"]
assert "Sujeto_entidad_financiera" in MIEMBROS_DIBUJADOS
assert all(CAJAS[m].col == 2 for m in MIEMBROS_DIBUJADOS)
assert all(_ef.y < CAJAS[m].y for m in _otros), (
    "Entidades financieras dejó de ser el miembro más alto: su diente ya no "
    "puede subir recto hasta el rol")
Y_MEM_CANAL = max(CAJAS[m].y + OFF_MEM for m in _otros)
Y_MEM_UNION = (rol.y + rol.h / 2.0 + Y_ARBOL) / 2.0
_cajas_34 = [c for c in CAJAS.values() if c.col in (3, 4)]
# El tramo bajo corre por debajo de TODAS las cajas de las columnas 3 y 4.
assert all(c.y + c.h / 2.0 + 10 < Y_MEM_CANAL for c in _cajas_34), (
    "el canal de miembro_de pasaría por una caja de las columnas 3 o 4")
X_MEM_CANAL = max(c.x + c.w for c in _cajas_34) + 18
ANCHO_SVG = max(X_FIN_ARBOL, X_MEM_CANAL) + MARGEN

# ========================================================================== #
# 7. Emisión del SVG                                                         #
# ========================================================================== #

O: list[str] = []
SEGMENTOS: list = []      # (a, b, grosor, es_leyenda) de cada trazo
SEG_TRAZOS: list = []     # los del dibujo (no la leyenda), con relación y peine
ROTULOS: list = []        # solicitudes de rótulo, resueltas al final


def add(s: str) -> None:
    O.append(s)


def texto(cx, y0, lineas, fs, color, bold=False, mono=False, anchor="middle",
          italic=False):
    fam = TIPO_MONO if mono else TIPO_SANS
    est = (f'font-family="{fam}" font-size="{f(fs)}" fill="{color}" '
           f'text-anchor="{anchor}"')
    if bold:
        est += ' font-weight="bold"'
    if italic:
        est += ' font-style="italic"'
    partes = [f'<text x="{f(cx)}" y="{f(y0)}" {est}>']
    for i, l in enumerate(lineas):
        dy = "0" if i == 0 else f(fs * 1.0 + (LH - fs))
        partes.append(f'<tspan x="{f(cx)}" dy="{dy}">{esc(l)}</tspan>')
    partes.append("</text>")
    add("".join(partes))


class _Pintada:
    """Vista de una caja con el color de borde ya resuelto por intensidad."""

    def __init__(self, caja, borde):
        self._c = caja
        self.color = borde

    def __getattr__(self, n):
        return getattr(self._c, n)


def dibujar_caja(c: Caja) -> None:
    en_camino = c.clave in EN_CAMINO
    dat = f' data-nodo="{esc(c.clave)}" data-forma="{c.forma}"'
    if getattr(c, "colapsa", None) is not None:
        dat += f' data-colapsa="{c.colapsa}"'
    if getattr(c, "instancias", 0):
        dat += f' data-instancias="{c.instancias}"'
    if getattr(c, "label_artefacto", None):
        dat += f' data-label-artefacto="{esc(c.label_artefacto)}"'
    if en_camino:
        dat += ' data-camino="1"'
    add(f"<g{dat}>")
    x, y, w, h = c.x, c.y - c.h / 2.0, c.w, c.h
    relleno = mezcla(c.color, REL_CAMINO if en_camino else REL_ATENUADO)
    borde = c.color if en_camino else mezcla(c.color, TRAZO_ATENUADO)
    AN_BASE = AN_NODO_CAMINO if en_camino else AN_NODO_ATENUADO
    AN_ROL = AN_BASE
    c = _Pintada(c, borde)
    if c.forma == "clase":
        add(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" '
            f'rx="3" fill="{relleno}" stroke="{c.color}" '
            f'stroke-width="{f(AN_BASE)}"/>')
    elif c.forma == "colapsada":
        for dx in (7, 3.5):
            add(f'<rect x="{f(x + dx)}" y="{f(y - dx)}" width="{f(w)}" '
                f'height="{f(h)}" rx="3" fill="{BLANCO}" stroke="{c.color}" '
                f'stroke-width="1.1" stroke-dasharray="5 3" opacity="0.75"/>')
        add(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" '
            f'rx="3" fill="{relleno}" stroke="{c.color}" '
            f'stroke-width="{f(AN_BASE)}" stroke-dasharray="7 4"/>')
    elif c.forma == "instancia":
        add(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" '
            f'rx="{f(h / 2.0)}" ry="{f(h / 2.0)}" fill="{relleno}" '
            f'stroke="{c.color}" stroke-width="{f(AN_BASE)}"/>')
    elif c.forma == "rol":
        m = INSET_ROL
        pts = [(x + m, y), (x + w - m, y), (x + w, y + h / 2.0),
               (x + w - m, y + h), (x + m, y + h), (x, y + h / 2.0)]
        d = " ".join(f"{f(px)},{f(py)}" for px, py in pts)
        add(f'<polygon points="{d}" fill="{relleno}" stroke="{c.color}" '
            f'stroke-width="{f(AN_ROL)}" stroke-dasharray="11 4 3 4"/>')
    elif c.forma == "norma":
        p = float(PLIEGUE_NORMA)
        d = (f"M{f(x)},{f(y)} L{f(x + w - p)},{f(y)} L{f(x + w)},{f(y + p)} "
             f"L{f(x + w)},{f(y + h)} L{f(x)},{f(y + h)} Z")
        add(f'<path d="{d}" fill="{relleno}" stroke="{c.color}" '
            f'stroke-width="{f(AN_BASE)}"/>')
        add(f'<path d="M{f(x + w - p)},{f(y)} L{f(x + w - p)},{f(y + p)} '
            f'L{f(x + w)},{f(y + p)}" fill="none" stroke="{c.color}" '
            f'stroke-width="1.2"/>')
    alto_txt = len(c.lineas) * LH + len(c.sub) * LH_SUB
    y0 = c.y - alto_txt / 2.0 + FS_NODO * 0.78
    texto(x + w / 2.0, y0, c.lineas, FS_NODO, C_TEXTO, bold=True)
    if c.sub:
        ys = c.y - alto_txt / 2.0 + len(c.lineas) * LH + FS_SUB * 0.85
        texto(x + w / 2.0, ys, c.sub, FS_SUB, C_NOTA, italic=True)
    add("</g>")


def anotar(hijo_clave, rel, padre_clave):
    """data-* del diente: una arista concreta, o el agregado de un colapsado."""
    if hijo_clave == "INSTCOL":
        return {"data-rel": rel, "data-dst": OP,
                "data-agrega": len(ARISTAS_AGREGADAS["__instancias__"])}
    if hijo_clave.startswith("COL:"):
        padre = hijo_clave[4:]
        return {"data-rel": rel, "data-dst": padre,
                "data-agrega": len(ARISTAS_AGREGADAS[padre]),
                "data-clases": len(GRUPOS[padre])}
    return {"data-rel": rel, "data-src": hijo_clave, "data-dst": padre_clave}


ESTILO_REL = {
    "subclase_de": (C_CLASE, AN_BASE, "none", "pt-sub"),
    "instancia_de": (C_INSTANCIA, AN_BASE, "6 4", "pt-ins"),
    "miembro_de": (C_ROL, AN_ROL, "12 4 3 4", "pt-mem"),
    "aplica_a": (C_NORMA, AN_APLICA, "none", "pt-apl"),
}


def polilinea(pts, rel, con_punta=True, datos=None, camino=False,
              leyenda=False, grupo=None):
    """Un trazo. `datos` deja en el SVG las anotaciones data-* con las que la
    figura se recuenta sin volver a correr el script (convención de F1).

    `camino=True` lo dibuja con la intensidad del camino resaltado y con la
    punta grande; sin él, el trazo va atenuado. `grupo` nombra el peine al
    que pertenece el trazo: dentro de un peine los trazos se tocan (diente,
    tronco y punta); entre peines distintos, la guarda de cruces no admite
    ni cruces ni contactos."""
    color, _, dash, mk = ESTILO_REL[rel]
    if not camino:
        color = mezcla(color, TRAZO_ATENUADO)
    an = AN_CAMINO if camino else AN_ATENUADO
    d = " ".join(("M" if i == 0 else "L") + f"{f(px)},{f(py)}"
                 for i, (px, py) in enumerate(pts))
    at = (f'fill="none" stroke="{color}" stroke-width="{f(an)}" '
          f'stroke-linejoin="round" stroke-linecap="round"')
    if dash != "none":
        at += f' stroke-dasharray="{dash}"'
    if con_punta:
        at += f' marker-end="url(#{mk}{"-cam" if camino else ""})"'
    # La muestra de la leyenda usa la misma intensidad pero NO es una
    # arista del dibujo: sin data-camino, el recuento desde el SVG da 4.
    if camino and not leyenda:
        at += ' data-camino="1"'
    if datos:
        at += "".join(f' {k}="{esc(str(v))}"' for k, v in sorted(datos.items()))
    add(f'<path d="{d}" {at}/>')
    # Registro para la guarda: todo segmento dibujado queda anotado con su
    # grosor, para medir después qué atraviesa.
    for _a, _b in zip(pts, pts[1:]):
        SEGMENTOS.append((_a, _b, an, leyenda))
        if not leyenda:
            SEG_TRAZOS.append({"a": _a, "b": _b, "rel": rel, "camino": camino,
                               "grupo": grupo})


SEP_ROTULO = 12.0      # separación mínima entre el rótulo y su tronco
MARGEN_ROTULO = 3.0    # aire exigido contra cajas, otros rótulos y trazos


def rect_rotulo(txt, x, y, anchor):
    """Rectángulo que ocupa un rótulo colocado en (x, y) con ese anclaje."""
    w = ANCHO_MONO * FS_REL * len(txt)
    x0 = {"middle": x - w / 2.0, "start": x, "end": x - w}[anchor]
    return (x0 - 5, y - FS_REL * 0.58, x0 + w + 5, y + FS_REL * 0.58)


def rotulo(txt, rel, candidatos):
    """SOLICITA un rótulo; no lo dibuja.

    Los rótulos se emiten todos juntos en una capa final (§ «capa de
    rótulos»), después de las aristas y de las cajas. Antes se dibujaban
    dentro de cada peine, y entonces su halo solo protegía de lo dibujado
    ANTES: una caja posterior podía pisarle un carácter —el defecto que se
    leía «subclase_ae»—. `candidatos` es la lista de posiciones probadas en
    orden de preferencia; la primera que pase la guarda se usa.
    """
    ROTULOS.append({"txt": txt, "rel": rel, "cand": list(candidatos)})


def bandas_libres(cajas, y_lo, y_hi):
    """Tramos de [y_lo, y_hi] que ninguna caja ocupa.

    Las bandas de las cajas se FUSIONAN antes de buscar huecos. Sin fusionar,
    dos bandas superpuestas producen un hueco fantasma —el defecto original:
    se eligió un hueco de 5,8 px entre el final de una banda y el comienzo de
    la siguiente, cuando una tercera banda lo cubría entero—.
    """
    aire = FS_REL * 0.62
    ocup = sorted((c.y - c.h / 2.0 - aire, c.y + c.h / 2.0 + aire)
                  for c in cajas)
    fus = []
    for a, b in ocup:
        if fus and a <= fus[-1][1]:
            fus[-1][1] = max(fus[-1][1], b)
        else:
            fus.append([a, b])
    libres, cursor = [], y_lo
    for a, b in fus:
        if a > cursor:
            libres.append((cursor, min(a, y_hi)))
        cursor = max(cursor, b)
        if cursor >= y_hi:
            break
    if cursor < y_hi:
        libres.append((cursor, y_hi))
    return [(a, b) for a, b in libres if b - a > 1]


def cand_tronco(x_t, y_lo, y_hi, cajas, lados=("izq", "der")):
    """Posiciones a un lado y otro del tronco, nunca encima.

    El orden de preferencia es: primero los centros de las bandas que ninguna
    caja ocupa (de la más ancha a la más angosta), y después un barrido fino
    de todo el tronco y de un margen por encima y por debajo.
    """
    pref = [ (a + b) / 2.0 for a, b in
             sorted(bandas_libres(cajas, y_lo, y_hi),
                    key=lambda t: (-(t[1] - t[0]), t[0])) ]
    barrido = [y_lo - 4.0 * i for i in range(1, 16)]
    barrido += [y_lo + 4.0 * i for i in range(int((y_hi - y_lo) // 4) + 1)]
    barrido += [y_hi + 4.0 * i for i in range(1, 16)]
    for y in pref + sorted(barrido):
        for lado in lados:
            if lado == "izq":
                yield (x_t - SEP_ROTULO, round(y, 2), "end")
            else:
                yield (x_t + SEP_ROTULO, round(y, 2), "start")


def cand_tramo(x_a, x_b, y):
    """Sobre un tramo horizontal: por encima, por debajo, y corriéndose."""
    cx = (x_a + x_b) / 2.0
    for d in (0.0, 14.0, -14.0, 28.0, -28.0, 42.0, -42.0):
        for signo in (-1.0, 1.0):
            yield (cx + d, y + signo * FS_REL * 0.95, "middle")


def comb(padre_clave, hijos_claves, x_tronco, rel, rotular=False, puerto=0.0,
         lados=("izq", "der")):
    """Dientes desde los hijos → tronco vertical → una punta en el padre.

    Un peine dibuja N aristas del artefacto con una sola punta, como en las
    figuras F1/F1b: el rótulo es único por peine. `puerto` desplaza el acceso
    sobre el borde del padre, para que dos peines que terminan en la misma
    caja (subclase_de e instancia_de sobre «Organismos públicos») no monten
    su punta en el mismo punto.
    """
    p = CAJAS[padre_clave]
    hs = [CAJAS[h] for h in hijos_claves]
    y_p = p.y + puerto
    ys = [h.y for h in hs]
    y_lo, y_hi = min(ys + [y_p]), max(ys + [y_p])
    g = f"{rel}->{padre_clave}"
    for h in hs:
        polilinea([(h.x, h.y), (x_tronco, h.y)], rel, con_punta=False,
                  datos=anotar(h.clave, rel, padre_clave), grupo=g)
    if y_hi - y_lo > 0.5:
        polilinea([(x_tronco, y_lo), (x_tronco, y_hi)], rel, con_punta=False,
                  grupo=g)
    polilinea([(x_tronco, y_p), (p.x + p.w, y_p)], rel, grupo=g)
    if rotular:
        if len(hs) >= 2:
            rotulo(rel, rel, cand_tronco(x_tronco, y_lo, y_hi, hs + [p], lados))
        else:
            rotulo(rel, rel, cand_tramo(hs[0].x, p.x + p.w, hs[0].y))


defs = []
for rel, (color0, _an, dash, mk) in sorted(ESTILO_REL.items()):
    for suf, color, k in (("", mezcla(color0, TRAZO_ATENUADO), 1.0),
                          ("-cam", color0, 1.45)):
        if rel == "subclase_de":   # triángulo hueco (generalización)
            cuerpo = (f'<path d="M0,0 L{f(11 * k)},{f(4.2 * k)} '
                      f'L0,{f(8.4 * k)} Z" fill="{BLANCO}" stroke="{color}" '
                      f'stroke-width="{f(1.5 * k)}"/>')
            w, h, rx, ry = 12 * k, 9 * k, 11 * k, 4.2 * k
        elif rel == "aplica_a":    # punta grande llena
            cuerpo = (f'<path d="M0,0 L{f(13 * k)},{f(5 * k)} '
                      f'L0,{f(10 * k)} Z" fill="{color}"/>')
            w, h, rx, ry = 13 * k, 10 * k, 13 * k, 5 * k
        elif rel == "miembro_de":  # punta llena con cola cóncava
            cuerpo = (f'<path d="M0,0 L{f(11 * k)},{f(4.2 * k)} '
                      f'L0,{f(8.4 * k)} L{f(3.2 * k)},{f(4.2 * k)} Z" '
                      f'fill="{color}"/>')
            w, h, rx, ry = 11 * k, 8.4 * k, 11 * k, 4.2 * k
        else:                      # instancia_de: punta llena chica
            cuerpo = (f'<path d="M0,0 L{f(9 * k)},{f(3.6 * k)} '
                      f'L0,{f(7.2 * k)} Z" fill="{color}"/>')
            w, h, rx, ry = 9 * k, 7.2 * k, 9 * k, 3.6 * k
        defs.append(f'<marker id="{mk}{suf}" markerUnits="userSpaceOnUse" '
                    f'markerWidth="{f(w)}" markerHeight="{f(h)}" '
                    f'refX="{f(rx)}" refY="{f(ry)}" orient="auto">'
                    f'{cuerpo}</marker>')

# --- leyenda: panel en el hueco libre de la derecha ----------------------- #
# El árbol deja vacío todo el cuadrante inferior derecho (las columnas 3 y 4
# sólo tienen contenido en las cuatro primeras filas). La leyenda va ahí: no
# agrega alto a la figura y queda a la vista mientras se lee el dibujo.
FORMAS_LEY = [
    ("clase", C_CLASE, "clase del catálogo"),
    ("colapsada", C_COLAPSADA, "rama no expandida"),
    ("instancia", C_INSTANCIA, "instancia"),
    ("rol", C_ROL, "rol de alcance"),
    ("norma", C_NORMA, "norma"),
]
RELS_LEY = ["subclase_de", "instancia_de", "miembro_de", "aplica_a"]
ETIQ_CAMINO = "camino resaltado"
NOTA_CAMINO = "norma → rol → clase → subclase"
NOTA_LEY = "La punta señala al padre o al rol."

X_PANEL = X_COL[3]
W_PANEL = ANCHO_SVG - MARGEN - X_PANEL
PAD_PANEL = 18
FILA_LEY = 38
_ultima_der = max(c.y + c.h / 2.0 for c in CAJAS.values()
                  if c.clave not in ("ROL", "NORMA") and c.col in (3, 4))
# El panel queda por debajo del tramo bajo del canal de miembro_de, que corre
# a la altura del diente del miembro dibujado más bajo.
Y_PANEL = max(_ultima_der + 52, Y_MEM_CANAL + 40)
ALTO_LINEA_NOTA = FS_LEY + 4
NOTA_LINEAS = envolver(NOTA_LEY, FS_LEY, W_PANEL - 2 * PAD_PANEL)
CAMINO_LINEAS = envolver(NOTA_CAMINO, FS_LEY, W_PANEL - 2 * PAD_PANEL)
ALTO_PANEL = (PAD_PANEL + FS_LEY + 9 + len(FORMAS_LEY) * FILA_LEY + 16
              + len(RELS_LEY) * FILA_LEY + 16
              + FILA_LEY + len(CAMINO_LINEAS) * ALTO_LINEA_NOTA + 10
              + len(NOTA_LINEAS) * ALTO_LINEA_NOTA + PAD_PANEL)
# El panel se apoya en el hueco libre; si su contenido lo desborda, el
# lienzo crece lo justo (la guarda de no-solapamiento sigue vigente).
ALTO_SVG = max(ALTO_ARBOL, Y_PANEL + ALTO_PANEL) + MARGEN


def pt(fs: float) -> float:
    """Tamano impreso, en puntos, de un cuerpo de `fs` px a ancho pleno."""
    return fs / ANCHO_SVG * LINEWIDTH_MM / 25.4 * 72


# Piso tipográfico. Es la restricción dura de esta versión de la figura: si
# el dibujo crece de ancho hasta hacer que algún cuerpo caiga por debajo de
# PT_MIN, esto FRENA — la salida es podar, nunca achicar la tipografía.
_CUERPOS = {"etiqueta de nodo": FS_NODO, "subtítulo": FS_SUB,
            "rótulo de relación": FS_REL, "leyenda": FS_LEY}
_flojos = {n: round(pt(v), 2) for n, v in _CUERPOS.items() if pt(v) < PT_MIN}
assert not _flojos, (
    f"tipografía por debajo de {PT_MIN} pt impresos a {LINEWIDTH_MM} mm: "
    f"{_flojos} (ancho del lienzo {f(ANCHO_SVG)} px)")

# --- guarda geométrica: ninguna caja se solapa con otra ni con el panel --- #
# La pregunta «¿alguna etiqueta se superpone o se corta?» se responde por
# construcción y no por inspección visual: el texto no desborda su caja
# (assert del constructor de Caja) y ninguna caja pisa a otra (assert de acá).
_RECTS = [(c.clave, c.x, c.y - c.h / 2.0, c.x + c.w, c.y + c.h / 2.0)
          for c in (CAJAS[k] for k in sorted(CAJAS))]
_RECTS.append(("PANEL_LEYENDA", X_PANEL, Y_PANEL,
               X_PANEL + W_PANEL, Y_PANEL + ALTO_PANEL))
for _i in range(len(_RECTS)):
    _na, _ax0, _ay0, _ax1, _ay1 = _RECTS[_i]
    assert _ax1 <= ANCHO_SVG - MARGEN + 0.5 and _ax0 >= MARGEN - 0.5, (
        f"{_na} se sale del lienzo horizontalmente")
    assert _ay1 <= ALTO_SVG - MARGEN + 0.5 and _ay0 >= MARGEN - 0.5, (
        f"{_na} se sale del lienzo verticalmente")
    for _j in range(_i + 1, len(_RECTS)):
        _nb, _bx0, _by0, _bx1, _by1 = _RECTS[_j]
        if (_ax0 < _bx1 - 0.5 and _bx0 < _ax1 - 0.5
                and _ay0 < _by1 - 0.5 and _by0 < _ay1 - 0.5):
            raise AssertionError(f"se solapan las cajas {_na} y {_nb}")

add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{f(ANCHO_SVG)}" '
    f'height="{f(ALTO_SVG)}" viewBox="0 0 {f(ANCHO_SVG)} {f(ALTO_SVG)}">')
add("<defs>" + "".join(defs) + "</defs>")
add(f'<rect width="{f(ANCHO_SVG)}" height="{f(ALTO_SVG)}" fill="{BLANCO}"/>')

# ---- aristas (debajo de las cajas) --------------------------------------- #
# subclase_de: raíz → 4 hijos
comb("Sujeto_sujeto",
     ["Sujeto_sujeto_regulado", "Sujeto_contraparte", "Sujeto_organismo_publico",
      "Sujeto_estructura"],
     X_SUB_01, "subclase_de", rotular=True)

# subclase_de: Sujetos regulados → 4 clases + rama colapsada
comb("Sujeto_sujeto_regulado",
     ["Sujeto_entidad_financiera", "Sujeto_entidad_cambiaria",
      "Sujeto_proveedor_no_financiero_de_credito",
      "Sujeto_fiduciario_de_fideicomiso_financiero", "COL:Sujeto_sujeto_regulado"],
     X_SUB_12, "subclase_de", rotular=True)

comb("Sujeto_contraparte", ["COL:Sujeto_contraparte"], X_SUB_12, "subclase_de")
comb("Sujeto_estructura", ["COL:Sujeto_estructura"], X_SUB_12, "subclase_de")
# Los dos peines que terminan en «Organismos públicos» entran por puertos
# distintos del mismo borde: subclase_de arriba, instancia_de abajo.
comb("Sujeto_organismo_publico", ["COL:Sujeto_organismo_publico"], X_SUB_12,
     "subclase_de", puerto=-FS_REL * 0.45)
comb("Sujeto_organismo_publico",
     ["Sujeto_bcra", "Sujeto_sefyc", "INSTCOL"], X_INS_12, "instancia_de",
     puerto=FS_REL * 0.45, rotular=True, lados=("izq",))

comb("Sujeto_entidad_financiera",
     ["Sujeto_banco", "COL:Sujeto_entidad_financiera"], X_SUB_23, "subclase_de")
comb("Sujeto_entidad_cambiaria", ["COL:Sujeto_entidad_cambiaria"], X_SUB_23,
     "subclase_de")
comb("Sujeto_proveedor_no_financiero_de_credito",
     ["Sujeto_empresa_no_financiera_emisora_de_tarjetas"], X_SUB_23,
     "subclase_de")
comb("Sujeto_banco", ["Sujeto_banco_comercial"], X_SUB_34, "subclase_de",
     rotular=True)

# miembro_de: un solo peine hacia el rol, con una sola punta (ruteo en §6).
_G_MEM = f"miembro_de->{ROL}"
_Y_ROL_ABAJO = rol.y + rol.h / 2.0
# Diente de Entidades financieras: recto hacia arriba hasta la unión.
polilinea([(X_EF_MEM, _ef.y - _ef.h / 2.0), (X_EF_MEM, Y_MEM_UNION)],
          "miembro_de", con_punta=False, grupo=_G_MEM,
          datos={"data-rel": "miembro_de", "data-src": "Sujeto_entidad_financiera",
                 "data-dst": ROL})
# Dientes de los demás miembros: a la derecha hasta X_MEM_23 y, si no están
# ya a la altura del canal, abajo hasta él.
for m in _otros:
    c = CAJAS[m]
    _pts = [(c.x + c.w, c.y + OFF_MEM), (X_MEM_23, c.y + OFF_MEM)]
    if abs(c.y + OFF_MEM - Y_MEM_CANAL) > 0.5:
        _pts.append((X_MEM_23, Y_MEM_CANAL))
    polilinea(_pts, "miembro_de", con_punta=False, grupo=_G_MEM,
              datos={"data-rel": "miembro_de", "data-src": m, "data-dst": ROL})
# Tronco: por debajo de las columnas 3 y 4, arriba por fuera de Bancos
# comerciales y de vuelta por el hueco entre la banda y el árbol.
polilinea([(X_MEM_23, Y_MEM_CANAL), (X_MEM_CANAL, Y_MEM_CANAL),
           (X_MEM_CANAL, Y_MEM_UNION), (X_EF_MEM, Y_MEM_UNION)],
          "miembro_de", con_punta=False, grupo=_G_MEM)
# Tramo común con la punta, de la unión al rol.
polilinea([(X_EF_MEM, Y_MEM_UNION), (X_EF_MEM, _Y_ROL_ABAJO)], "miembro_de",
          grupo=_G_MEM)
# El rótulo, junto a la vertical del camino (a su izquierda, que es lado
# libre: el tramo de vuelta llega a la unión por la derecha).
rotulo("miembro_de", "miembro_de",
       cand_tronco(X_EF_MEM, _Y_ROL_ABAJO, _ef.y - _ef.h / 2.0, [_ef, rol]))

# aplica_a: norma → rol
polilinea([(norma.x + norma.w, rol.y), (rol.x, rol.y)], "aplica_a",
          grupo=f"aplica_a->{ROL}",
          datos={"data-rel": "aplica_a", "data-src": NORMA, "data-dst": ROL})
rotulo("aplica_a", "aplica_a",
       cand_tramo(norma.x + norma.w, rol.x, rol.y))

# ---- el camino, por encima ------------------------------------------------ #
# Mismos vértices que los trazos ya dibujados: esta capa los repite con la
# intensidad del camino y los tapa. No agrega aristas —las cuatro ya están
# contadas y verificadas— y por eso no lleva anotaciones data-rel: lleva
# data-camino, que es lo que la distingue.
_bc, _ba = CAJAS["Sujeto_banco_comercial"], CAJAS["Sujeto_banco"]
_no = CAJAS["NORMA"]
polilinea([(_bc.x, _bc.y), (_ba.x + _ba.w, _ba.y)], "subclase_de", camino=True)
polilinea([(_ba.x, _ba.y), (X_SUB_23, _ba.y), (X_SUB_23, _ef.y),
           (_ef.x + _ef.w, _ef.y)], "subclase_de", camino=True)
# miembro_de del camino: el diente de Entidades financieras más el tramo
# común hasta la punta. El canal de los otros miembros sigue atenuado: el
# camino no pasa por él.
polilinea([(X_EF_MEM, _ef.y - _ef.h / 2.0), (X_EF_MEM, _Y_ROL_ABAJO)],
          "miembro_de", camino=True)
polilinea([(_no.x + _no.w, rol.y), (rol.x, rol.y)], "aplica_a", camino=True)

# ---- cajas --------------------------------------------------------------- #
for _cl in sorted(CAJAS):
    dibujar_caja(CAJAS[_cl])

# ---- leyenda ------------------------------------------------------------- #
add(f'<rect x="{f(X_PANEL)}" y="{f(Y_PANEL)}" width="{f(W_PANEL)}" '
    f'height="{f(ALTO_PANEL)}" rx="5" fill="#fbfbfa" stroke="#d8d8d8" '
    f'stroke-width="1"/>')
_yl = Y_PANEL + PAD_PANEL + FS_LEY
add(f'<text x="{f(X_PANEL + PAD_PANEL)}" y="{f(_yl)}" '
    f'font-family="{TIPO_SANS}" font-size="{f(FS_LEY + 1)}" fill="{C_TEXTO}" '
    f'font-weight="bold" text-anchor="start">Referencias</text>')
_yl += 9 + FILA_LEY / 2.0


def swatch(forma, color, gx, gy, gw, gh, camino=False):
    """Muestra de una forma. Por omisión, con la intensidad atenuada: es la
    del grueso del dibujo. `camino=True` la dibuja resaltada."""
    relleno = mezcla(color, REL_CAMINO if camino else REL_ATENUADO)
    borde = color if camino else mezcla(color, TRAZO_ATENUADO)
    an = AN_NODO_CAMINO if camino else AN_NODO_ATENUADO
    if forma == "clase":
        add(f'<rect x="{f(gx)}" y="{f(gy)}" width="{f(gw)}" height="{f(gh)}" '
            f'rx="3" fill="{relleno}" stroke="{borde}" stroke-width="{f(an)}"/>')
    elif forma == "colapsada":
        add(f'<rect x="{f(gx + 4)}" y="{f(gy - 4)}" width="{f(gw)}" '
            f'height="{f(gh)}" rx="3" fill="{BLANCO}" stroke="{borde}" '
            f'stroke-width="1.1" stroke-dasharray="5 3" opacity="0.75"/>')
        add(f'<rect x="{f(gx)}" y="{f(gy)}" width="{f(gw)}" height="{f(gh)}" '
            f'rx="3" fill="{relleno}" stroke="{borde}" stroke-width="{f(an)}" '
            f'stroke-dasharray="7 4"/>')
    elif forma == "instancia":
        add(f'<rect x="{f(gx)}" y="{f(gy)}" width="{f(gw)}" height="{f(gh)}" '
            f'rx="{f(gh / 2)}" ry="{f(gh / 2)}" fill="{relleno}" '
            f'stroke="{borde}" stroke-width="{f(an)}"/>')
    elif forma == "rol":
        m = 6.0
        pts = [(gx + m, gy), (gx + gw - m, gy), (gx + gw, gy + gh / 2),
               (gx + gw - m, gy + gh), (gx + m, gy + gh), (gx, gy + gh / 2)]
        add('<polygon points="' + " ".join(f"{f(a)},{f(b)}" for a, b in pts)
            + f'" fill="{relleno}" stroke="{borde}" stroke-width="{f(an)}" '
              f'stroke-dasharray="11 4 3 4"/>')
    else:
        q = 7.0
        add(f'<path d="M{f(gx)},{f(gy)} L{f(gx + gw - q)},{f(gy)} '
            f'L{f(gx + gw)},{f(gy + q)} L{f(gx + gw)},{f(gy + gh)} '
            f'L{f(gx)},{f(gy + gh)} Z" fill="{relleno}" stroke="{borde}" '
            f'stroke-width="{f(an)}"/>')

for forma, color, etiqueta in FORMAS_LEY:
    gx, gw, gh = X_PANEL + PAD_PANEL, 34.0, 19.0
    swatch(forma, color, gx, _yl - gh / 2.0, gw, gh)
    add(f'<text x="{f(gx + gw + 12)}" y="{f(_yl + FS_LEY * 0.36)}" '
        f'font-family="{TIPO_SANS}" font-size="{f(FS_LEY)}" fill="{C_NOTA}" '
        f'text-anchor="start">{esc(etiqueta)}</text>')
    _yl += FILA_LEY

_yl += 4
add(f'<line x1="{f(X_PANEL + PAD_PANEL)}" y1="{f(_yl)}" '
    f'x2="{f(X_PANEL + W_PANEL - PAD_PANEL)}" y2="{f(_yl)}" stroke="#e2e2e2" '
    f'stroke-width="1"/>')
_yl += 12

for rel in RELS_LEY:
    polilinea([(X_PANEL + PAD_PANEL + 40, _yl), (X_PANEL + PAD_PANEL, _yl)],
              rel, leyenda=True)
    add(f'<text x="{f(X_PANEL + PAD_PANEL + 51)}" y="{f(_yl + FS_LEY * 0.36)}" '
        f'font-family="{TIPO_MONO}" font-size="{f(FS_LEY)}" '
        f'fill="{ESTILO_REL[rel][0]}" text-anchor="start">{esc(rel)}</text>')
    _yl += FILA_LEY

_yl += 4
add(f'<line x1="{f(X_PANEL + PAD_PANEL)}" y1="{f(_yl)}" '
    f'x2="{f(X_PANEL + W_PANEL - PAD_PANEL)}" y2="{f(_yl)}" stroke="#e2e2e2" '
    f'stroke-width="1"/>')
_yl += 12

# --- la fila del camino: una caja resaltada, un trazo grueso, otra caja ---
_gx, _gw, _gh = X_PANEL + PAD_PANEL, 15.0, 19.0
swatch("clase", C_CLASE, _gx, _yl - _gh / 2.0, _gw, _gh, camino=True)
polilinea([(_gx + _gw + 24, _yl), (_gx + _gw + 4, _yl)], "subclase_de",
          camino=True, leyenda=True)
swatch("clase", C_CLASE, _gx + _gw + 28, _yl - _gh / 2.0, _gw, _gh, camino=True)
add(f'<text x="{f(_gx + 2 * _gw + 40)}" y="{f(_yl + FS_LEY * 0.36)}" '
    f'font-family="{TIPO_SANS}" font-size="{f(FS_LEY)}" fill="{C_TEXTO}" '
    f'font-weight="bold" text-anchor="start">{esc(ETIQ_CAMINO)}</text>')
_yl += FILA_LEY - 4

for linea in CAMINO_LINEAS:
    add(f'<text x="{f(X_PANEL + PAD_PANEL)}" y="{f(_yl)}" '
        f'font-family="{TIPO_SANS}" font-size="{f(FS_LEY)}" fill="{C_NOTA}" '
        f'font-style="italic" text-anchor="start">{esc(linea)}</text>')
    _yl += ALTO_LINEA_NOTA

_yl += 10
for linea in NOTA_LINEAS:
    add(f'<text x="{f(X_PANEL + PAD_PANEL)}" y="{f(_yl)}" '
        f'font-family="{TIPO_SANS}" font-size="{f(FS_LEY)}" fill="{C_NOTA}" '
        f'font-style="italic" text-anchor="start">{esc(linea)}</text>')
    _yl += ALTO_LINEA_NOTA

# ---- capa de rótulos + guarda de trazos ---------------------------------- #
# Los rótulos se emiten acá, al final: por encima de todas las aristas y de
# todas las cajas. Dentro de cada peine, su halo solo protegía de lo dibujado
# antes, y una caja posterior le comía caracteres.

RECT_CAJAS = [(c.clave, c.x, c.y - c.h / 2.0, c.x + c.w, c.y + c.h / 2.0)
              for c in (CAJAS[k] for k in sorted(CAJAS))]
RECT_PANEL = ("PANEL_LEYENDA", X_PANEL, Y_PANEL,
              X_PANEL + W_PANEL, Y_PANEL + ALTO_PANEL)


def _solapan(A, B, m=0.0):
    return (A[0] < B[2] + m and B[0] < A[2] + m
            and A[1] < B[3] + m and B[1] < A[3] + m)


def _segmento_toca(a, b, R, grosor, m):
    """¿El segmento a-b (recto, horizontal o vertical) entra en el rect R?

    R se agranda por el margen pedido más la mitad del grosor del trazo: lo
    que se mide es la tinta, no la línea ideal.
    """
    e = m + grosor / 2.0
    x0, y0, x1, y1 = R[0] - e, R[1] - e, R[2] + e, R[3] + e
    if abs(a[1] - b[1]) < 0.01:                       # horizontal
        return (y0 < a[1] < y1
                and max(x0, min(a[0], b[0])) < min(x1, max(a[0], b[0])))
    if abs(a[0] - b[0]) < 0.01:                       # vertical
        return (x0 < a[0] < x1
                and max(y0, min(a[1], b[1])) < min(y1, max(a[1], b[1])))
    raise AssertionError(f"segmento no ortogonal: {a} -> {b}")


def _penetra_caja(a, b, R, grosor):
    """Cuánto entra el segmento a-b DENTRO del rectángulo R, a lo largo.

    Mide longitud, no contacto: casi todos los trazos terminan sobre el borde
    de una caja (ahí va la punta de flecha, ahí arranca un diente), y eso es
    correcto. Lo que es defecto es atravesarla. La posición perpendicular se
    compara contra el interior encogido por medio grosor, de modo que se mide
    la tinta y no la línea ideal.
    """
    e = grosor / 2.0 + 1.0
    if abs(a[1] - b[1]) < 0.01:                       # horizontal
        if not (R[1] + e < a[1] < R[3] - e):
            return 0.0
        return max(0.0, min(R[2], max(a[0], b[0])) - max(R[0], min(a[0], b[0])))
    if abs(a[0] - b[0]) < 0.01:                       # vertical
        if not (R[0] + e < a[0] < R[2] - e):
            return 0.0
        return max(0.0, min(R[3], max(a[1], b[1])) - max(R[1], min(a[1], b[1])))
    raise AssertionError(f"segmento no ortogonal: {a} -> {b}")


def _rotulo_libre(R, puestos):
    if not (MARGEN - 2 <= R[0] and R[2] <= ANCHO_SVG - MARGEN + 2
            and MARGEN - 2 <= R[1] and R[3] <= ALTO_SVG - MARGEN + 2):
        return False
    for _n, *B in RECT_CAJAS + [RECT_PANEL]:
        if _solapan(R, B, MARGEN_ROTULO):
            return False
    for P in puestos:
        if _solapan(R, P, MARGEN_ROTULO):
            return False
    for a, b, grosor, ley in SEGMENTOS:
        if not ley and _segmento_toca(a, b, R, grosor, MARGEN_ROTULO):
            return False
    return True


_puestos = []
for _r in ROTULOS:
    for _i, (_x, _y, _anc) in enumerate(_r["cand"]):
        _R = rect_rotulo(_r["txt"], _x, _y, _anc)
        if _rotulo_libre(_R, _puestos):
            _r["pos"], _r["rect"], _r["cand_n"] = (_x, _y, _anc), _R, _i
            _puestos.append(_R)
            break
    else:
        raise AssertionError(
            f"no hay lugar libre para el rótulo «{_r['txt']}»: ninguno de sus "
            f"{len(_r['cand'])} candidatos queda fuera de cajas, de otros "
            f"rótulos y de todo trazo")

for _r in ROTULOS:
    _x, _y, _anc = _r["pos"]
    _color = ESTILO_REL[_r["rel"]][0]
    _R = _r["rect"]
    add(f'<rect x="{f(_R[0])}" y="{f(_R[1])}" width="{f(_R[2] - _R[0])}" '
        f'height="{f(_R[3] - _R[1])}" fill="{BLANCO}"/>')
    add(f'<text x="{f(_x)}" y="{f(_y + FS_REL * 0.36)}" '
        f'font-family="{TIPO_MONO}" font-size="{f(FS_REL)}" fill="{_color}" '
        f'text-anchor="{_anc}" data-rotulo="{esc(_r["rel"])}">'
        f'{esc(_r["txt"])}</text>')

# GUARDA NUEVA. La anterior solo comparaba caja contra caja; esta mide los
# trazos contra el interior de cada caja y contra el rectángulo de cada
# rótulo. Un trazo que cruza texto es un defecto de render, y acá frena.
TOL_PENETRACION = 3.0     # entrar menos que esto es tocar el borde, no cruzar
_VIOLA = []
for _n, *_B in RECT_CAJAS:
    for _a, _b, _g, _ley in SEGMENTOS:
        if _ley:
            continue
        _d = _penetra_caja(_a, _b, tuple(_B), _g)
        if _d > TOL_PENETRACION:
            _VIOLA.append(f"trazo {_a}->{_b} entra {_d:.1f} px en la caja {_n}")
for _r in ROTULOS:
    for _a, _b, _g, _ley in SEGMENTOS:
        if not _ley and _segmento_toca(_a, _b, _r["rect"], _g, 0.0):
            _VIOLA.append(f"trazo {_a}->{_b} cruza el rótulo «{_r['txt']}»")
    for _n, *_B in RECT_CAJAS + [RECT_PANEL]:
        if _solapan(_r["rect"], _B):
            _VIOLA.append(f"el rótulo «{_r['txt']}» pisa la caja {_n}")
assert not _VIOLA, "trazos o rótulos superpuestos:\n  " + "\n  ".join(_VIOLA)

# GUARDA DE CRUCES (versión 5). Sobre los trazos del dibujo, sin la capa del
# camino (que repite trazos ya dibujados) ni la leyenda:
#   - cruce: un tramo horizontal y uno vertical se cortan en un punto
#     interior a los dos. No se admite ninguno, sea del peine que sea.
#   - contacto: el extremo de un tramo toca otro tramo de OTRO peine. Dentro
#     de un peine es la unión de diente, tronco y punta; entre peines se
#     leería como una unión que el grafo no tiene.
#   - solape: dos tramos de peines distintos sobre la misma recta.
TOL = 0.5
_BASE = [s for s in SEG_TRAZOS if not s["camino"]]
assert all(s["grupo"] for s in _BASE), "hay un trazo del dibujo sin peine"


def _horizontal(s):
    return abs(s["a"][1] - s["b"][1]) < 0.01


def _rango(s):
    i = 0 if _horizontal(s) else 1
    return min(s["a"][i], s["b"][i]), max(s["a"][i], s["b"][i])


def _fijo(s):
    return s["a"][1] if _horizontal(s) else s["a"][0]


def _en(v, lo, hi, interior):
    return lo + TOL < v < hi - TOL if interior else lo - TOL <= v <= hi + TOL


CRUCES, CONTACTOS, SOLAPES = [], [], []
for _i in range(len(_BASE)):
    for _j in range(_i + 1, len(_BASE)):
        _s, _t = _BASE[_i], _BASE[_j]
        _mismo = _s["grupo"] == _t["grupo"]
        if _horizontal(_s) != _horizontal(_t):
            _h, _v = (_s, _t) if _horizontal(_s) else (_t, _s)
            _x, _y = _fijo(_v), _fijo(_h)
            _hlo, _hhi = _rango(_h)
            _vlo, _vhi = _rango(_v)
            if _en(_x, _hlo, _hhi, True) and _en(_y, _vlo, _vhi, True):
                CRUCES.append((round(_x, 1), round(_y, 1), _h["grupo"],
                               _v["grupo"]))
            elif (not _mismo and _en(_x, _hlo, _hhi, False)
                  and _en(_y, _vlo, _vhi, False)):
                CONTACTOS.append((round(_x, 1), round(_y, 1), _h["grupo"],
                                  _v["grupo"]))
        elif not _mismo and abs(_fijo(_s) - _fijo(_t)) < TOL:
            _lo = max(_rango(_s)[0], _rango(_t)[0])
            _hi = min(_rango(_s)[1], _rango(_t)[1])
            if _hi - _lo > -TOL:
                SOLAPES.append((_s["grupo"], _t["grupo"], round(_fijo(_s), 1)))
assert not CRUCES, f"{len(CRUCES)} cruces de línea: {CRUCES}"
assert not CONTACTOS, f"trazos de peines distintos se tocan: {CONTACTOS}"
assert not SOLAPES, f"trazos de peines distintos se solapan: {SOLAPES}"

# La capa del camino no inventa trazo: cada tramo resaltado cae entero sobre
# tramos dibujados de la misma relación, en la misma recta.
for _s in (s for s in SEG_TRAZOS if s["camino"]):
    _lo, _hi = _rango(_s)
    _cub = sorted(_rango(t) for t in _BASE
                  if t["rel"] == _s["rel"] and _horizontal(t) == _horizontal(_s)
                  and abs(_fijo(t) - _fijo(_s)) < 0.01)
    _cursor = _lo
    for _a, _b in _cub:
        if _a <= _cursor + TOL:
            _cursor = max(_cursor, _b)
    assert _cursor >= _hi - TOL, (
        f"el camino resalta un tramo que no está dibujado: {_s['a']}->{_s['b']}")

add("</svg>")

SALIDA.write_text("\n".join(O) + "\n", encoding="utf-8")

# ========================================================================== #
# 8. Reporte de verificación (a stdout, para pegar)                          #
# ========================================================================== #

try:
    _salida_txt = SALIDA.resolve().relative_to(REPO).as_posix()
except ValueError:
    _salida_txt = SALIDA.name            # fuera del repositorio: solo el nombre
print(f"SVG escrito: {_salida_txt}  ({f(ANCHO_SVG)} x {f(ALTO_SVG)})")
print()
print("FUENTES (candado de sha256 comprobado sobre los bytes)")
print(f"  catálogo  {CATALOGO.relative_to(REPO).as_posix()}  {SHA_CATALOGO[:16]}…")
print(f"  grafo     {KG.relative_to(REPO).as_posix()}  {SHA_KG[:16]}…")
print(f"  catálogo: {len(VIGENTES)} vigentes ({len(CLASES)} clases, "
      f"{len(INSTANCIAS)} instancias, {len(ROLES)} roles) + {len(LAPIDAS)} lápidas")
print("  ramas de la raíz (clases, la de la rama incluida): "
      + ", ".join(f"{ENTRADAS[r]['label']} {subarbol(r)}" for r in RAMAS))
print("  pertenencia, catálogo = grafo arista por arista: "
      + ", ".join(f"{r} {len(PERTENENCIA_CAT[r])}" for r in PERTENENCIA_CAT))
print()
print("BIYECCIÓN nodo dibujado ↔ entrada del artefacto")
print(f"  clases dibujadas       : {len(CLASES_DIBUJADAS):2d}")
for p in CLASES_DIBUJADAS:
    if p in GRUPOS:
        _ins = INSTANCIAS_EN_RAMA.get(p, [])
        print(f"  colapsada bajo {ENTRADAS[p]['label']:24s}: "
              f"+{len(GRUPOS[p]):2d} clases "
              f"({len(ARISTAS_AGREGADAS[p])} subclase_de directas)"
              + (f" + {len(_ins)} instancia(s): "
                 + ", ".join(ENTRADAS[i]["label"] for i in _ins) if _ins else ""))
print(f"  colapsadas (total)     : {N_COLAPSADAS:2d}")
print(f"  CONTEO  {len(CLASES_DIBUJADAS)} + {N_COLAPSADAS} = "
      f"{len(CLASES_DIBUJADAS) + N_COLAPSADAS}  (catálogo: {len(CLASES)})")
_n_rama = sum(len(v) for v in INSTANCIAS_EN_RAMA.values())
print(f"  instancias  {len(INSTANCIAS_DIBUJADAS)} dibujadas + "
      f"{len(INSTANCIAS_COLAPSADAS)} en el nodo de instancias + "
      f"{_n_rama} en una rama colapsada = "
      f"{len(INSTANCIAS_DIBUJADAS) + len(INSTANCIAS_COLAPSADAS) + _n_rama}  "
      f"(catálogo: {len(INSTANCIAS)})")
print(f"  roles       1 dibujado de {len(ROLES)} del catálogo; "
      f"miembros {len(MIEMBROS_DIBUJADOS)} dibujados + "
      f"{len(MIEMBROS_NO_DIBUJADOS)} declarados = {len(MIEMBROS_ROL)}")
print("  miembros NO dibujados (y el nodo colapsado que los contiene):")
for m in MIEMBROS_NO_DIBUJADOS:
    _g = next(p for p in GRUPOS if m in GRUPOS[p])
    print(f"      {ENTRADAS[m]['label']}  ->  «+{len(GRUPOS[_g])} clases» "
          f"de {ENTRADAS[_g]['label']}")
print()
print("CAMINO RESALTADO (5 nodos, 4 aristas; cadena verificada)")
for _n in CAMINO_NODOS:
    _et = (NODOS_KG[NORMA]["label"] if _n == "NORMA"
           else ROLES[ROL]["label"] if _n == "ROL"
           else ENTRADAS[_n]["label"])
    print(f"      {_et}")
for _s, _r, _t in CAMINO_ARISTAS:
    print(f"      {_s[:52]:52s} --{_r}--> {_t}")
print(f"  las 4 son aristas explícitas del dibujo y están en el kg: "
      f"{all(a in ARISTAS_EXPLICITAS and a in ARISTAS_KG for a in CAMINO_ARISTAS)}")
print(f"  tramos resaltados: {sum(1 for s in SEG_TRAZOS if s['camino'])}, "
      f"todos sobre tramos dibujados de la misma relación")
print()
print("RUTEO DE miembro_de")
print(f"  vertical de Entidades financieras en x {X_EF_MEM:.1f}, de y "
      f"{_ef.y - _ef.h / 2.0:.1f} a {_Y_ROL_ABAJO:.1f} (rol de x {rol.x:.1f} "
      f"a {rol.x + rol.w:.1f})")
print(f"  canal: bajada en x {X_MEM_23:.1f}, tramo bajo en y {Y_MEM_CANAL:.1f}, "
      f"subida en x {X_MEM_CANAL:.1f}, unión en y {Y_MEM_UNION:.1f}")
print()
print("CAPA DE RÓTULOS (emitida al final, por encima de aristas y cajas)")
for _r in ROTULOS:
    _x, _y, _anc = _r["pos"]
    _R = _r["rect"]
    print(f"      «{_r['txt']:12s}» en x {_x:7.1f} y {_y:7.1f} ({_anc:6s}) "
          f"— rect x {_R[0]:7.1f}..{_R[2]:7.1f} y {_R[1]:6.1f}..{_R[3]:6.1f} "
          f"— candidato {_r['cand_n']} de {len(_r['cand'])}")
print(f"  guarda: 0 trazos dentro de una caja (más de {TOL_PENETRACION} px) "
      f"y 0 trazos sobre un rótulo, sobre {len(RECT_CAJAS)} cajas y "
      f"{sum(1 for _s in SEGMENTOS if not _s[3])} segmentos del dibujo")
print(f"  CRUCES {len(CRUCES)}, contactos entre peines {len(CONTACTOS)}, "
      f"solapes entre peines {len(SOLAPES)}, sobre {len(_BASE)} tramos de "
      f"{len({s['grupo'] for s in _BASE})} peines (sin la capa del camino)")
print()
print("TIPOGRAFÍA impresa a width=\\linewidth "
      f"({LINEWIDTH_MM:.0f} mm; lienzo {f(ANCHO_SVG)} x {f(ALTO_SVG)} px)")
for _n, _v in _CUERPOS.items():
    print(f"      {_n:20s} {_v} px -> {pt(_v):.2f} pt")
print(f"  piso exigido {PT_MIN} pt: "
      f"{'CUMPLE' if min(pt(v) for v in _CUERPOS.values()) >= PT_MIN else 'NO'}")
print(f"  tamaño impreso: {LINEWIDTH_MM / 10:.1f} x "
      f"{ALTO_SVG / ANCHO_SVG * LINEWIDTH_MM / 10:.2f} cm")
print()
print("INSTANCIAS abreviadas (sigla dibujada / etiqueta del artefacto)")
for _i in INSTANCIAS_DIBUJADAS:
    print(f"      {sigla(ENTRADAS[_i]['label']):6s} <- {ENTRADAS[_i]['label']}")
print()
print("ARISTAS contra el grafo (ens_diez_r2b/r2/kg.json)")
print(f"  conteos globales: subclase_de={_cnt['subclase_de']} "
      f"instancia_de={_cnt['instancia_de']} miembro_de={_cnt['miembro_de']} "
      f"parte_de={_cnt['parte_de']}")
print(f"  trazos explícitos (1 trazo = 1 arista): {len(ARISTAS_EXPLICITAS)}")
for s, r, t in ARISTAS_EXPLICITAS:
    print(f"      {s}  --{r}-->  {t}")
print(f"  trazos agregados (1 trazo = N aristas hacia el nodo colapsado): "
      f"{len(TODAS_LAS_ARISTAS) - len(ARISTAS_EXPLICITAS)}")
print(f"  TOTAL aristas representadas: {len(TODAS_LAS_ARISTAS)}  "
      f"— todas presentes en el kg: "
      f"{all(a in ARISTAS_KG for a in TODAS_LAS_ARISTAS)}")
