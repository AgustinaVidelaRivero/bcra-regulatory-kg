#!/usr/bin/env python3
"""Validador de shapes v0 (capas 1 y 2) para los kg.json del experimento.

Reglas determinísticas (sin LLM) S1-S12 y S15 sobre la estructura del grafo.
El kg.json de entrada es SOLO LECTURA: este script no lo modifica jamás.
Lo único que escribe es el reporte Markdown indicado por --out, y solo si esa
opción se pasa.

Uso:
    python3 scripts/shapes_validator.py [--kg RUTA] [--out RUTA]
                                        [--excepciones RUTA]
                                        [--perfil congelado]

`--out` NO tiene default: sin esa opción el validador reporta por consola y no
escribe archivo alguno. Antes apuntaba a un reporte commiteado del repo y lo
sobrescribía en silencio (ver el comentario de DEFAULT_OUT).

S15 (U-ESQ-V3) es la guarda de la taxonomía de roles: un rol sin aristas
`miembro_de` entrantes es un nodo aislado del árbol, y las normas del TO que
lo declara dejan de ser alcanzables por navegación taxonómica — el mecanismo
que el capítulo del esquema presenta como aporte del grafo frente al
fragmento. Su tercera cláusula obliga a que la deuda quede VISIBLE Y CONTADA:
los roles sin miembro adjudicable se declaran en una lista, y el validador
compara la cuenta declarada contra la medida.

`--excepciones` apunta al artefacto que declara esa lista (el bloque
`excepciones_s15` de un esquema de clases, p. ej.
`data/experiment/esq_v3_miembros/esquema_v3_clases.json`). SIN esa opción la
lista declarada es vacía y cualquier rol huérfano es FAIL, que es el
comportamiento seguro por defecto.

S13, S14, S16 y S17 NO están implementadas y no se inventan: el orden de
reporte es la lista explícita S1..S12 + S15, sin huecos silenciosos.

PERFIL «CONGELADO» (U-B2.2 fase 2). Sin `--perfil`, el comportamiento es el
de siempre: mismo reporte, misma consola, mismo código de salida. Con
`--perfil congelado` el validador evalúa el grafo contra el esquema congelado
de la generación 3:

- El vocabulario (9 tipos, 13 predicados, matriz dominio/rango, enum de
  Obligacion.tipo y sus valores retirados) se LEE de
  `data/experiment/esq/code/prompt_congelado.py`; nada de eso se copia acá.
  El único dato propio es el candado: el sha256 del texto del prefijo
  congelado (`e69feaaa…`, laudo_esquema_congelado.md §4). Si el módulo no lo
  reproduce, el validador FRENA con código de salida 2 antes de evaluar nada.
- El catálogo de sujetos (ids de `clases` ∪ `roles`) se lee del mismo
  artefacto de `--excepciones` que S15.
- Severidad en dos secciones y veredicto global PASA / NO PASA:
  BLOQUEANTES = S1, S2, S3, S4, S5, S6, S15, S19 (catálogo) y S20 (enum);
  INFORMATIVAS con conteo = S7, S8, S9, S10, S11, S12, S21, S22 y S23.
  Código de salida 1 cuando el veredicto es NO PASA.
- Tolerancia: referencia nodo→nodo (rol_fuente=referencia_cruzada) y
  padre_sugerido se ADMITEN en S1/S3 y no se exigen; su coherencia interna se
  mide en S21 y S22 (informativas).
- Junto al reporte .md se escribe un .json con los conteos de cada shape y
  el veredicto, para comparar grafos sin parsear markdown.
- Numeración: S18 ya está declarado en docs/esquema_v2_diseño.md con otro
  enunciado (umbral de `limita`), así que las shapes nuevas del perfil se
  numeran desde S19 (ver NUMERACION_PERFIL). S9 (descripción canónica) se
  evalúa en el perfil como informativa, con el mismo cómputo que v0.

Solo stdlib (sin dependencias de terceros). El módulo de vocabulario se
importa con `sys.dont_write_bytecode = True` para no dejar __pycache__.
"""

import argparse
import datetime
import hashlib
import importlib.util
import json
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_KG = os.path.join(
    REPO_ROOT,
    "data", "experiment", "run_3_ppf_core", "kg.json",
)
# SIN default de salida (U-ESQ-V3). Hasta acá el default era
# reports/shapes_run_3_v0.md, un reporte COMMITEADO: correr la herramienta sin
# --out sobrescribía un artefacto del repo en silencio. El incidente está
# registrado desde el 02/08/2026 (data/backlog/retests/C3_retest_2026-08-02.md
# §Incidente: «escritura fuera del mandato, revertida con git checkout») y
# volvió a dispararse sobre el mismo archivo durante U-ESQ-V3. El checklist de
# un gate obliga a quien lo lee; el default obliga a cualquiera que corra la
# herramienta, así que el arreglo va acá.
#
# Sin --out el validador NO escribe: reporta por consola y listo. Es el mismo
# criterio que ya había adoptado la adaptación v2 de esta herramienta
# (data/experiment/grafo_v2/code/shapes_v2.py: `--out default=None`).
DEFAULT_OUT = None

RELACIONES_12 = {
    "aplica_a", "regula", "prohibe", "limita", "exceptua",
    "exceptua_obligacion", "requiere", "condiciona", "ejecuta",
    "establecida_en", "referencia", "modificada_por",
}

# S3 — matriz de firmas: relación -> (dominios permitidos, rango)
FIRMAS = {
    "establecida_en": ({"Obligacion", "Restriccion", "Operacion", "Excepcion"}, "TextoOrdenado"),
    "aplica_a": ({"Obligacion", "Restriccion"}, "EntidadFinanciera"),
    "regula": ({"Obligacion", "Restriccion"}, "Operacion"),
    "limita": ({"Restriccion"}, "Operacion"),
    "prohibe": ({"Restriccion"}, "Operacion"),
    "condiciona": ({"Obligacion"}, "Operacion"),
    "requiere": ({"Operacion"}, "Obligacion"),
    "exceptua": ({"Excepcion"}, "Restriccion"),
    "exceptua_obligacion": ({"Excepcion"}, "Obligacion"),
    "ejecuta": ({"EntidadFinanciera"}, "Operacion"),
    "referencia": ({"TextoOrdenado"}, "Comunicacion"),
    "modificada_por": ({"TextoOrdenado"}, "Comunicacion"),
}

UNIDADES_REGULATORIAS = ("Obligacion", "Restriccion", "Excepcion")

# S15 — orden de reporte. S13, S14, S16 y S17 no están implementadas: la lista
# es explícita para que su ausencia se lea, en vez de esconderse en un range().
ORDEN_SHAPES = [f"S{i}" for i in range(1, 13)] + ["S15"]
SHAPES_NO_IMPLEMENTADAS = ("S13", "S14", "S16", "S17")

# ---------------------------------------------------------------------------
# Perfil «congelado» (U-B2.2 fase 2) — constantes
# ---------------------------------------------------------------------------
PERFILES = ("congelado",)

# Módulo del que se LEE el vocabulario congelado. No se copia nada de su
# contenido acá: tipos, predicados, matriz y enum se leen al cargar.
RUTA_PROMPT_CONGELADO = os.path.join(
    REPO_ROOT, "data", "experiment", "esq", "code", "prompt_congelado.py")

# Candado: sha256 del TEXTO del prefijo congelado, tal como lo registra el
# laudo de esquema congelado §4 (data/experiment/esq/laudo_esquema_congelado.md,
# líneas 136-137). Es el único dato del vocabulario que vive en este archivo,
# y vive acá porque es lo que se verifica contra el módulo, no algo que se
# lea de él.
SHA256_PREFIJO_CONGELADO_ESPERADO = (
    "e69feaaa04779bd6347cc9e3974d2c1749519f1230e70a0459e66f46517cd720")

# Valor cuyo retiro del enum el laudo §4 materializó; el validador exige que
# el módulo lo declare entre los retirados (si no, el módulo no es el que el
# laudo describe y se frena).
VALOR_RETIRADO_OBLIGATORIO = "requisito_de_estructura"

RELACIONES_ESQUELETO = ("subclase_de", "miembro_de", "instancia_de", "parte_de")
RELACION_PADRE_SUGERIDO = "padre_sugerido"
ROL_FUENTE_REFERENCIA_CRUZADA = "referencia_cruzada"
ROL_DOCUMENTAL_ESQUELETO = "esqueleto"
CLAVES_PROVENANCE_G3 = ("to", "archivo", "punto", "rol_documental")
NIVELES_SUJETO = ("clase", "instancia", "rol", "propuesto")
NIVELES_PADRE = ("clase", "rol")

BLOQUEANTES_CONGELADO = ("S1", "S2", "S3", "S4", "S5", "S6", "S15", "S19", "S20")
INFORMATIVAS_CONGELADO = ("S7", "S8", "S9", "S10", "S11", "S12", "S21", "S22", "S23")
ORDEN_SHAPES_CONGELADO = list(BLOQUEANTES_CONGELADO) + list(INFORMATIVAS_CONGELADO)

# Tabla número -> enunciado de las shapes NUEVAS del perfil. Los números
# S13/S14/S16/S17 (no implementadas, docs/esquema_v2_diseño.md:318-322) y S18
# (docs/esquema_v2_diseño.md:325: «Si una Restricción tiene arista limita,
# tiene property umbral») están declarados con enunciados que NO coinciden
# con lo que este perfil implementa, así que no se reutilizan.
NUMERACION_PERFIL = {
    "S19": "Catálogo de sujetos (bloqueante): todo Sujeto tiene nivel válido; "
           "si no es propuesto, su id está en el catálogo; si es propuesto, "
           "tiene cuarentena y padre_sugerido.",
    "S20": "Enum de Obligacion.tipo (bloqueante): todo Obligacion.tipo está en "
           "el enum congelado; conteos separados de valores retirados y de "
           "otros valores fuera del enum.",
    "S21": "Coherencia de referencias nodo→nodo (informativa): destino sin "
           "prefijo <to>:: pertenece al conjunto de puntos del nodo destino; "
           "desglose por via.",
    "S22": "Coherencia de padre_sugerido (informativa): destino de la arista = "
           "properties.padre_sugerido del origen y el origen está en "
           "cuarentena.",
    "S23": "aplica_a hacia sujetos en cuarentena (informativa): aristas "
           "aplica_a cuyo destino es Sujeto de nivel propuesto.",
}

# Shapes de v0 que quedan FUERA del perfil, declaradas para que el hueco se
# lea (mismo criterio que SHAPES_NO_IMPLEMENTADAS). Hoy ninguna: S9 entró al
# perfil como informativa al cierre de la unidad. El mecanismo se conserva.
FUERA_DEL_PERFIL = {}


class VocabularioCongeladoError(RuntimeError):
    """El módulo de vocabulario no es el que el laudo describe: se frena."""


class CandadoShaError(VocabularioCongeladoError):
    """El sha del prefijo congelado no coincide con el esperado."""


def cargar_excepciones_s15(ruta):
    """Lee el bloque `excepciones_s15` del artefacto indicado.

    Devuelve (ids_declarados, total_declarado, por_causa, defecto). `defecto`
    describe un problema del propio artefacto (ilegible, sin bloque, cuenta
    interna inconsistente) y hace fallar S15: una lista de excepciones que no
    se puede leer no es una deuda declarada."""
    if not ruta:
        return set(), 0, {}, None
    try:
        with open(ruta, encoding="utf-8") as f:
            d = json.load(f)
    except Exception as e:
        return set(), 0, {}, f"no se pudo leer {ruta}: {e}"
    bloque = d.get("excepciones_s15")
    if not isinstance(bloque, dict):
        return set(), 0, {}, f"{ruta} no declara un bloque 'excepciones_s15'"
    filas = bloque.get("roles") or []
    ids = {r.get("rol_id") for r in filas if r.get("rol_id")}
    total = bloque.get("total")
    por_causa = bloque.get("por_causa") or {}
    if total != len(filas):
        return ids, total, por_causa, (
            f"el artefacto se contradice: declara total={total} y lista {len(filas)} roles")
    if por_causa and sum(por_causa.values()) != len(filas):
        return ids, total, por_causa, (
            f"el artefacto se contradice: la suma por causa ({sum(por_causa.values())}) "
            f"no reproduce el total listado ({len(filas)})")
    return ids, total, por_causa, None


def cargar_catalogo_sujetos(ruta):
    """Lee el catálogo de sujetos del artefacto de --excepciones: los ids de
    `clases` ∪ `roles` (esquema_v3_clases.json). Devuelve
    (ids, n_clases, n_roles, defecto). Sin ruta el catálogo es vacío y el
    defecto lo dice: todo Sujeto no propuesto queda fuera del catálogo, que
    es el comportamiento seguro por defecto (mismo criterio que S15)."""
    if not ruta:
        return set(), 0, 0, "no se pasó --excepciones: el catálogo de sujetos es vacío"
    try:
        with open(ruta, encoding="utf-8") as f:
            d = json.load(f)
    except Exception as e:
        return set(), 0, 0, f"no se pudo leer {ruta}: {e}"
    clases = d.get("clases")
    roles = d.get("roles")
    if not isinstance(clases, list) or not isinstance(roles, list):
        return set(), 0, 0, f"{ruta} no declara las listas 'clases' y 'roles'"
    ids = {c.get("id") for c in clases if isinstance(c, dict) and c.get("id")}
    ids |= {r.get("id") for r in roles if isinstance(r, dict) and r.get("id")}
    return ids, len(clases), len(roles), None


def cargar_vocabulario_congelado(ruta=RUTA_PROMPT_CONGELADO,
                                 sha_esperado=SHA256_PREFIJO_CONGELADO_ESPERADO):
    """Importa prompt_congelado.py y devuelve su vocabulario como dict.

    FRENA (CandadoShaError) si el sha256 del texto del prefijo congelado que
    el módulo calcula no es el esperado, y (VocabularioCongeladoError) si el
    módulo no declara `requisito_de_estructura` entre los valores retirados
    del enum. Los valores retirados se derivan del propio módulo: los del
    enum v2 que importa (`pr2.OBLIGACION_TIPO_V2`) que no están en
    `OBLIGACION_TIPO_CONGELADO`."""
    sys.dont_write_bytecode = True  # el import no debe dejar __pycache__
    if not os.path.isfile(ruta):
        raise VocabularioCongeladoError(f"no existe el módulo de vocabulario {ruta}")
    spec = importlib.util.spec_from_file_location("prompt_congelado", ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    sha = getattr(mod, "PREFIJO_SHA256_CONGELADO", None)
    if sha != sha_esperado:
        raise CandadoShaError(
            f"candado del sha: el módulo {ruta} declara PREFIJO_SHA256_CONGELADO="
            f"{sha}, esperado {sha_esperado} — el vocabulario no es el sellado, se frena")
    enum = tuple(mod.OBLIGACION_TIPO_CONGELADO)
    retirados = tuple(v for v in mod.pr2.OBLIGACION_TIPO_V2 if v not in enum)
    if VALOR_RETIRADO_OBLIGATORIO not in retirados:
        raise VocabularioCongeladoError(
            f"el módulo no declara '{VALOR_RETIRADO_OBLIGATORIO}' entre los valores "
            f"retirados del enum (retirados={retirados}) — se frena")
    return {
        "modulo": ruta,
        "sha256_prefijo": sha,
        "hash_prefijo": getattr(mod, "PREFIJO_HASH_CONGELADO", None),
        "entity_types": tuple(mod.ENTITY_TYPES_CONGELADO),
        "predicates": tuple(mod.PREDICATES_CONGELADO),
        "domain_range": {p: (set(d), set(r)) for p, (d, r) in mod.DOMAIN_RANGE_CONGELADO.items()},
        "obligacion_tipo": enum,
        "retirados": retirados,
    }


def norm(s):
    """NFD + remoción de diacríticos + lowercase (normalización de los censos)."""
    if not isinstance(s, str):
        s = str(s)
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn").lower()


def check_provenance(prov):
    """Devuelve lista de defectos de un dict de provenance según S4."""
    defectos = []
    if not isinstance(prov, dict):
        return [f"provenance no es dict (es {type(prov).__name__})"]
    keys = set(prov.keys())
    if keys != {"source_doc", "location"}:
        defectos.append(f"keys {sorted(keys)} != ['location', 'source_doc']")
    for k in ("source_doc", "location"):
        v = prov.get(k)
        if not isinstance(v, str) or not v.strip():
            defectos.append(f"{k} vacío o no-string")
    return defectos


def check_provenance_g3(prov, provs):
    """Defectos de provenance de la generación 3 (S4 del perfil congelado):
    dict con al menos {to, archivo, punto, rol_documental}; `provenances` lista
    no vacía con provenance == provenances[0]; para rol_documental distinto de
    esqueleto, `to` y `archivo` strings no vacíos (para esqueleto se admiten
    to nulo, chunk_id nulo y paginas vacía)."""
    if not isinstance(prov, dict):
        return [f"provenance no es dict (es {type(prov).__name__})"]
    defectos = []
    faltan = [k for k in CLAVES_PROVENANCE_G3 if k not in prov]
    if faltan:
        defectos.append(f"faltan claves {faltan}")
    rol = prov.get("rol_documental")
    if rol != ROL_DOCUMENTAL_ESQUELETO:
        for k in ("to", "archivo"):
            v = prov.get(k)
            if not isinstance(v, str) or not v.strip():
                defectos.append(f"{k} vacío o no-string (rol_documental={rol!r})")
    if not isinstance(provs, list) or not provs:
        defectos.append("provenances vacía o no-lista")
    elif provs[0] != prov:
        defectos.append("provenance != provenances[0]")
    return defectos


def _res(rid, enunciado, result, resumen, detalle_md, detalle_consola=None, conteos=None):
    """Registro de resultado de una shape (mismo contrato que `registrar` de
    main; `conteos` es la vista numérica que va al .json del perfil)."""
    return {
        "rid": rid,
        "enunciado": enunciado,
        "result": result,
        "resumen": resumen,
        "detalle_md": detalle_md,
        "detalle_consola": detalle_consola if detalle_consola is not None else detalle_md,
        "conteos": conteos or {},
    }


def lista_consola(items, limite=50):
    if len(items) <= limite:
        return items
    return items[:limite] + [f"... ({len(items)} en total; lista completa en el reporte)"]


def nivel_de(n):
    return ((n or {}).get("properties") or {}).get("nivel")


def en_cuarentena(props):
    """`cuarentena` verdadera: True o la string 'true' (es lo que emite r1)."""
    v = (props or {}).get("cuarentena")
    return v is True or (isinstance(v, str) and v.strip().lower() == "true")


def destino_sin_prefijo(destino):
    """`cap::4.1` -> `4.1` (el prefijo es el código del TO seguido de `::`)."""
    if not isinstance(destino, str):
        return destino
    return destino.split("::", 1)[1] if "::" in destino else destino


# ---------------------------------------------------------------------------
# Shapes compartidas por v0 y por el perfil (mismo cómputo, extraídas de main)
# ---------------------------------------------------------------------------
def shape_s2(edges, node_by_id):
    viol = []
    for i, e in enumerate(edges):
        faltan = [x for x in ("source", "target") if e[x] not in node_by_id]
        if faltan:
            viol.append(f"idx {i}: {e['relation']} {e['source']} -> {e['target']} (inexistente: {', '.join(faltan)})")
    return _res(
        "S2", "Integridad referencial: origen y destino de toda arista existen como nodos.",
        "PASS" if not viol else "FAIL",
        f"{len(viol)} aristas colgantes sobre {len(edges)}.",
        viol,
        conteos={"aristas": len(edges), "colgantes": len(viol)},
    )


def shape_s7(nodes):
    grupos = defaultdict(list)
    for n in nodes:
        grupos[(n["type"], norm(n["label"]))].append(n)
    dups = {k: v for k, v in grupos.items() if len(v) > 1}
    detalle = []
    for (t, l), ns in sorted(dups.items()):
        detalle.append(f"[{t}] '{l}' ({len(ns)} nodos):")
        for n in ns:
            detalle.append(f"    - {n['id']}  (label: '{n['label']}')")
    return _res(
        "S7", "ERROR — Unicidad exacta: no puede haber dos nodos con el mismo (type, label normalizado).",
        "PASS" if not dups else "FAIL",
        f"{len(dups)} grupos violatorios ({sum(len(v) for v in dups.values())} nodos involucrados).",
        detalle,
        conteos={"grupos": len(dups), "nodos_involucrados": sum(len(v) for v in dups.values())},
    )


def shape_s8(nodes):
    grupos2 = defaultdict(list)
    for n in nodes:
        grupos2[norm(n["label"])].append(n)
    cross = {l: ns for l, ns in grupos2.items()
             if len(ns) > 1 and len({n["type"] for n in ns}) > 1}
    detalle = []
    for l, ns in sorted(cross.items()):
        detalle.append(f"'{l}' ({len(ns)} nodos):")
        for n in ns:
            detalle.append(f"    - [{n['type']}] {n['id']}")
    return _res(
        "S8", "WARN — Colisión de label normalizado entre types distintos.",
        "PASS" if not cross else "WARN",
        f"{len(cross)} grupos con el mismo label normalizado en types distintos.",
        detalle,
        conteos={"grupos": len(cross)},
    )


def shape_s9(nodes):
    ambas = [n for n in nodes
             if "descripcion" in (n.get("properties") or {}) and "description" in (n.get("properties") or {})]
    tabla = []
    for t in sorted({n["type"] for n in nodes}):
        ns = [n for n in nodes if n["type"] == t]
        c_desc = sum(1 for n in ns if "descripcion" in (n.get("properties") or {}))
        c_engl = sum(1 for n in ns if "description" in (n.get("properties") or {}))
        c_ambas = sum(1 for n in ns
                      if "descripcion" in (n.get("properties") or {}) and "description" in (n.get("properties") or {}))
        c_ninguna = sum(1 for n in ns
                        if "descripcion" not in (n.get("properties") or {}) and "description" not in (n.get("properties") or {}))
        tabla.append(f"{t}: descripcion={c_desc}, description={c_engl}, ambas={c_ambas}, ninguna={c_ninguna} (total {len(ns)})")
    detalle = ["Tabla por type (usa cada key / ambas / ninguna):"] + [f"  {r}" for r in tabla] + \
              ["", f"Nodos con AMBAS keys ({len(ambas)}):"] + [f"    - [{n['type']}] {n['id']}" for n in ambas]
    return _res(
        "S9", "ERROR — Descripción canónica: ningún nodo tiene a la vez 'descripcion' y 'description'.",
        "PASS" if not ambas else "FAIL",
        f"{len(ambas)} nodos con ambas keys.",
        detalle,
        conteos={"nodos_con_ambas_keys": len(ambas)},
    )


def shape_s10(nodes, out_edges, tipos=UNIDADES_REGULATORIAS, enunciado=None):
    sin_est = defaultdict(list)
    for n in nodes:
        if n["type"] in tipos:
            if not any(norm(e["relation"]) == "establecida_en" for e in out_edges[n["id"]]):
                sin_est[n["type"]].append(n["id"])
    total_sin = sum(len(v) for v in sin_est.values())
    detalle = []
    for t in tipos:
        detalle.append(f"{t}: {len(sin_est[t])} sin establecida_en")
        for i in sin_est[t]:
            detalle.append(f"    - {i}")
    return _res(
        "S10",
        enunciado or f"ERROR — Toda unidad regulatoria ({'/'.join(tipos)}) tiene >=1 arista saliente establecida_en.",
        "PASS" if total_sin == 0 else "FAIL",
        "Sin establecida_en: " + ", ".join(f"{t}={len(sin_est[t])}" for t in tipos) + f" (total {total_sin}).",
        detalle,
        conteos={"total_sin_establecida_en": total_sin, "por_tipo": {t: len(sin_est[t]) for t in tipos}},
    )


def shape_s11(nodes, out_edges, tipos=("Obligacion", "Restriccion"), enunciado=None):
    sin_apl = defaultdict(list)
    for n in nodes:
        if n["type"] in tipos:
            if not any(norm(e["relation"]) == "aplica_a" for e in out_edges[n["id"]]):
                sin_apl[n["type"]].append(n["id"])
    total_sin = sum(len(v) for v in sin_apl.values())
    detalle = []
    for t in tipos:
        detalle.append(f"{t}: {len(sin_apl[t])} sin aplica_a")
        for i in sin_apl[t]:
            detalle.append(f"    - {i}")
    return _res(
        "S11",
        enunciado or f"WARN — Toda {' y '.join(tipos)} tiene >=1 arista saliente aplica_a.",
        "PASS" if total_sin == 0 else "WARN",
        "Sin aplica_a: " + ", ".join(f"{t}={len(sin_apl[t])}" for t in tipos) + f" (total {total_sin}).",
        detalle,
        detalle_consola=[f"{t}: {len(sin_apl[t])} sin aplica_a" for t in tipos]
        + [f"(ids completos en el reporte; total {total_sin})"],
        conteos={"total_sin_aplica_a": total_sin, "por_tipo": {t: len(sin_apl[t]) for t in tipos}},
    )


def shape_s12(nodes, out_edges):
    sin_exc = []
    for n in nodes:
        if n["type"] == "Excepcion":
            if not any(norm(e["relation"]) in ("exceptua", "exceptua_obligacion") for e in out_edges[n["id"]]):
                sin_exc.append(n["id"])
    return _res(
        "S12", "ERROR — Toda Excepcion tiene >=1 arista saliente exceptua o exceptua_obligacion.",
        "PASS" if not sin_exc else "FAIL",
        f"{len(sin_exc)} Excepciones sin salida exceptua/exceptua_obligacion.",
        [f"    - {i}" for i in sin_exc],
        conteos={"excepciones_sin_salida": len(sin_exc)},
    )


def shape_s15(nodes, edges, node_by_id, excepciones_ruta):
    # Todo rol tiene miembro_de no vacío O figura en la lista declarada de
    # roles sin miembro adjudicable; los miembros son clases del árbol; y el
    # validador REPORTA la lista con su cuenta.
    decl_ids, decl_total, decl_causa, decl_defecto = cargar_excepciones_s15(excepciones_ruta)

    roles = [n for n in nodes if (n.get("properties") or {}).get("nivel") == "rol"]
    miembros_de = defaultdict(list)
    for e in edges:
        if norm(e["relation"]) == "miembro_de":
            miembros_de[e["target"]].append(e["source"])

    huerfanos = sorted(r["id"] for r in roles if not miembros_de.get(r["id"]))
    no_declarados = [r for r in huerfanos if r not in decl_ids]
    declarados_con_miembro = sorted(i for i in decl_ids if miembros_de.get(i))

    # Segunda cláusula: el miembro es una clase del árbol. Sobre el grafo
    # vigente los 17 miembros son de nivel 'clase' (medido), y la adjudicación
    # de U-ESQ-V3 rechazó por laudo los candidatos de nivel instancia, así que
    # la regla describe lo que el grafo efectivamente tiene.
    miembros_no_clase = []
    for rol_id, ms in sorted(miembros_de.items()):
        for m in ms:
            n = node_by_id.get(m)
            niv = (n.get("properties") or {}).get("nivel") if n else None
            if niv != "clase":
                miembros_no_clase.append(
                    f"{m} --miembro_de--> {rol_id} (nivel del miembro: {niv or 'inexistente'})")

    cuenta_ok = (decl_total == len(huerfanos)) if excepciones_ruta else True

    viol_s15 = []
    if decl_defecto:
        viol_s15.append(f"lista de excepciones inválida: {decl_defecto}")
    viol_s15 += [f"rol huérfano NO declarado: {i}" for i in no_declarados]
    viol_s15 += [f"miembro que no es clase del árbol: {x}" for x in miembros_no_clase]
    if not cuenta_ok:
        viol_s15.append(
            f"la cuenta declarada ({decl_total}) no coincide con la medida "
            f"({len(huerfanos)} roles huérfanos en el grafo)")

    detalle_s15 = list(viol_s15)
    if decl_ids:
        detalle_s15.append("")
        detalle_s15.append(f"Lista declarada ({decl_total} roles"
                           + (f"; por causa: {decl_causa}" if decl_causa else "") + "):")
        detalle_s15 += [f"    - {i}" + ("  [YA TIENE MIEMBRO: declaración obsoleta]"
                                        if i in declarados_con_miembro else "")
                        for i in sorted(decl_ids)]

    return _res(
        "S15",
        "ERROR — Todo rol tiene miembro_de no vacío O figura en la lista declarada de roles sin "
        "miembro adjudicable; los miembros son clases del árbol; la cuenta declarada coincide "
        "con la medida.",
        "PASS" if not viol_s15 else "FAIL",
        f"{len(roles)} roles, {sum(len(v) for v in miembros_de.values())} aristas miembro_de; "
        f"{len(huerfanos)} huérfanos ({len(huerfanos) - len(no_declarados)} declarados, "
        f"{len(no_declarados)} sin declarar); {len(miembros_no_clase)} miembros que no son clase."
        + (f" Lista declarada: {decl_total}" + (f" ({decl_causa})" if decl_causa else "") + "."
           if excepciones_ruta else " Sin lista declarada (--excepciones no fue pasada)."),
        detalle_s15,
        conteos={
            "roles": len(roles),
            "aristas_miembro_de": sum(len(v) for v in miembros_de.values()),
            "huerfanos": len(huerfanos),
            "huerfanos_declarados": len(huerfanos) - len(no_declarados),
            "huerfanos_sin_declarar": len(no_declarados),
            "miembros_no_clase": len(miembros_no_clase),
            "lista_declarada_total": decl_total if excepciones_ruta else None,
            "cuenta_coincide": cuenta_ok,
            "lista_defecto": decl_defecto,
        },
    )


# ---------------------------------------------------------------------------
# Shapes propias del perfil congelado
# ---------------------------------------------------------------------------
def shape_s1_congelado(edges, vocab):
    admitidas = set(vocab["predicates"]) | set(RELACIONES_ESQUELETO) | {RELACION_PADRE_SUGERIDO}
    viol = [f"idx {i}: relation='{e['relation']}'"
            for i, e in enumerate(edges) if norm(e["relation"]) not in admitidas]
    return _res(
        "S1",
        f"Toda arista usa una relación admitida por el perfil congelado: los "
        f"{len(vocab['predicates'])} predicados de PREDICATES_CONGELADO ∪ las "
        f"{len(RELACIONES_ESQUELETO)} de esqueleto ({'/'.join(RELACIONES_ESQUELETO)}) ∪ "
        f"{RELACION_PADRE_SUGERIDO} (nombre normalizado).",
        "PASS" if not viol else "FAIL",
        f"{len(edges) - len(viol)}/{len(edges)} aristas con relación admitida ({len(admitidas)} "
        f"relaciones admitidas); {len(viol)} violaciones.",
        viol,
        conteos={"aristas": len(edges), "violaciones": len(viol),
                 "relaciones_admitidas": len(admitidas)},
    )


def shape_s3_congelado(edges, node_by_id, vocab):
    dr = vocab["domain_range"]
    viol = []
    n_ref_cruzada = n_esq = n_padre = n_matriz = 0
    for i, e in enumerate(edges):
        rel = norm(e["relation"])
        if e["source"] not in node_by_id or e["target"] not in node_by_id:
            continue  # capturado por S2
        sn, tn = node_by_id[e["source"]], node_by_id[e["target"]]
        st, dt = sn["type"], tn["type"]
        if rel in dr:
            if rel == "referencia" and e.get("rol_fuente") == ROL_FUENTE_REFERENCIA_CRUZADA:
                n_ref_cruzada += 1
                continue  # referencia nodo→nodo admitida por rol_fuente
            n_matriz += 1
            dominios, rangos = dr[rel]
            ok = st in dominios and dt in rangos
            etiqueta = "matriz congelada"
        elif rel in RELACIONES_ESQUELETO:
            n_esq += 1
            ok = st == "Sujeto" and dt == "Sujeto"
            etiqueta = "esqueleto solo Sujeto->Sujeto"
        elif rel == RELACION_PADRE_SUGERIDO:
            n_padre += 1
            ok = (st == "Sujeto" and dt == "Sujeto"
                  and nivel_de(sn) == "propuesto" and nivel_de(tn) in NIVELES_PADRE)
            etiqueta = "padre_sugerido solo propuesto->clase|rol"
        else:
            continue  # capturado por S1
        if not ok:
            viol.append(
                f"idx {i}: {rel} {st}[{nivel_de(sn) or '-'}] -> {dt}[{nivel_de(tn) or '-'}] "
                f"({e['source']} -> {e['target']}; rol_fuente={e.get('rol_fuente')!r}; {etiqueta})")
    return _res(
        "S3",
        "Toda arista respeta las firmas del perfil congelado: DOMAIN_RANGE_CONGELADO (Sujeto como "
        "pseudo-tipo) ∪ esqueleto solo Sujeto->Sujeto ∪ referencia nodo->nodo solo si "
        "rol_fuente=referencia_cruzada ∪ padre_sugerido solo de Sujeto propuesto a Sujeto "
        "clase|rol. La referencia TextoOrdenado->Comunicacion sigue por la matriz.",
        "PASS" if not viol else "FAIL",
        f"{len(edges) - len(viol)}/{len(edges)} aristas conformes a firma; {len(viol)} violaciones. "
        f"Evaluadas: {n_matriz} por matriz, {n_esq} de esqueleto, {n_padre} padre_sugerido; "
        f"{n_ref_cruzada} referencias nodo->nodo admitidas por rol_fuente.",
        viol,
        conteos={"aristas": len(edges), "violaciones": len(viol),
                 "evaluadas_matriz": n_matriz, "evaluadas_esqueleto": n_esq,
                 "evaluadas_padre_sugerido": n_padre,
                 "referencias_cruzadas_admitidas": n_ref_cruzada},
    )


def shape_s4_congelado(nodes, edges):
    viol = []
    nodos_ok = 0
    for n in nodes:
        d = check_provenance_g3(n.get("provenance"), n.get("provenances"))
        if d:
            viol.append(f"nodo {n['id']}: {'; '.join(d)}")
        else:
            nodos_ok += 1
    aristas_ok = 0
    for i, e in enumerate(edges):
        d = check_provenance_g3(e.get("provenance"), e.get("provenances"))
        if d:
            viol.append(f"arista idx {i} ({e['relation']} {e['source']} -> {e['target']}): {'; '.join(d)}")
        else:
            aristas_ok += 1
    return _res(
        "S4",
        "Todo nodo y toda arista tienen provenance dict con al menos {to, archivo, punto, "
        "rol_documental}, provenances lista no vacía con provenance == provenances[0]; para "
        "rol_documental distinto de esqueleto, to y archivo no vacíos (para esqueleto se "
        "admiten to nulo, chunk_id nulo y paginas vacía).",
        "PASS" if not viol else "FAIL",
        f"Nodos OK: {nodos_ok}/{len(nodes)}. Aristas OK: {aristas_ok}/{len(edges)}. Violaciones: {len(viol)}.",
        viol,
        conteos={"nodos_ok": nodos_ok, "nodos": len(nodes), "aristas_ok": aristas_ok,
                 "aristas": len(edges), "violaciones": len(viol)},
    )


def _punto_ok(prov):
    if not isinstance(prov, dict):
        return False
    p = prov.get("punto")
    return isinstance(p, str) and bool(p.strip())


def shape_s5_congelado(nodes, edges):
    viol = []
    n_nodos = n_aristas = 0
    for n in nodes:
        if _punto_ok(n.get("provenance")):
            n_nodos += 1
        else:
            viol.append(f"nodo {n['id']}: punto={(n.get('provenance') or {}).get('punto') if isinstance(n.get('provenance'), dict) else None!r}")
    for i, e in enumerate(edges):
        if _punto_ok(e.get("provenance")):
            n_aristas += 1
        else:
            viol.append(f"arista idx {i} ({e['relation']}): punto={(e.get('provenance') or {}).get('punto') if isinstance(e.get('provenance'), dict) else None!r}")
    return _res(
        "S5", "Todo provenance.punto (de nodo y de arista) es una string no vacía.",
        "PASS" if not viol else "FAIL",
        f"Nodos con punto: {n_nodos}/{len(nodes)}. Aristas: {n_aristas}/{len(edges)}. Violaciones: {len(viol)}.",
        viol,
        conteos={"nodos_con_punto": n_nodos, "nodos": len(nodes),
                 "aristas_con_punto": n_aristas, "aristas": len(edges), "violaciones": len(viol)},
    )


def shape_s6_congelado(nodes, edges):
    archivos_to = {(n.get("properties") or {}).get("archivo") for n in nodes if n["type"] == "TextoOrdenado"}
    archivos_to = {a for a in archivos_to if isinstance(a, str) and a}
    archivos_esq = set()
    for x in list(nodes) + list(edges):
        for p in (x.get("provenances") or []):
            if isinstance(p, dict) and p.get("rol_documental") == ROL_DOCUMENTAL_ESQUELETO:
                a = p.get("archivo")
                if isinstance(a, str) and a:
                    archivos_esq.add(a)
    archivos = archivos_to | archivos_esq
    viol = []
    for n in nodes:
        prov = n.get("provenance")
        a = prov.get("archivo") if isinstance(prov, dict) else None
        if a not in archivos:
            viol.append(f"nodo {n['id']}: archivo={a!r}")
    for i, e in enumerate(edges):
        prov = e.get("provenance")
        a = prov.get("archivo") if isinstance(prov, dict) else None
        if a not in archivos:
            viol.append(f"arista idx {i} ({e['relation']}): archivo={a!r}")
    return _res(
        "S6",
        "Todo provenance.archivo pertenece a {properties.archivo de los nodos TextoOrdenado} ∪ "
        "{archivo de las provenances con rol_documental=esqueleto}; nada codificado a mano.",
        "PASS" if not viol else "FAIL",
        f"Archivos válidos ({len(archivos)}): TextoOrdenado {sorted(archivos_to)} ∪ esqueleto "
        f"{sorted(archivos_esq - archivos_to)}. Violaciones: {len(viol)}.",
        viol,
        conteos={"archivos_validos": len(archivos), "archivos_texto_ordenado": len(archivos_to),
                 "archivos_esqueleto_adicionales": len(archivos_esq - archivos_to),
                 "violaciones": len(viol)},
    )


def shape_s19_catalogo(nodes, catalogo_ids, defecto_catalogo):
    sujetos = [n for n in nodes if n["type"] == "Sujeto"]
    por_nivel = Counter()
    viol = []
    fuera = nivel_invalido = incompletos = 0
    if defecto_catalogo:
        viol.append(f"catálogo inválido: {defecto_catalogo}")
    for n in sujetos:
        props = n.get("properties") or {}
        niv = props.get("nivel")
        por_nivel[niv if niv in NIVELES_SUJETO else "invalido"] += 1
        if niv not in NIVELES_SUJETO:
            nivel_invalido += 1
            viol.append(f"{n['id']}: nivel={niv!r} no está en {list(NIVELES_SUJETO)}")
            continue
        if niv != "propuesto":
            if n["id"] not in catalogo_ids:
                fuera += 1
                viol.append(f"{n['id']} (nivel {niv}): id fuera del catálogo")
        else:
            faltan = [k for k in ("cuarentena", "padre_sugerido") if not props.get(k)]
            if faltan:
                incompletos += 1
                viol.append(f"{n['id']} (propuesto): sin properties.{' ni properties.'.join(faltan)}")
    return _res(
        "S19",
        "ERROR — Catálogo de sujetos: todo Sujeto tiene nivel ∈ {clase, instancia, rol, propuesto}; "
        "si nivel ≠ propuesto, su id está en el catálogo (clases ∪ roles) del artefacto de "
        "--excepciones; si nivel = propuesto, tiene properties.cuarentena y properties.padre_sugerido.",
        "PASS" if not viol else "FAIL",
        f"{len(sujetos)} Sujetos ({dict(sorted(por_nivel.items(), key=lambda kv: str(kv[0])))}); "
        f"catálogo de {len(catalogo_ids)} ids; {fuera} fuera del catálogo, {nivel_invalido} con nivel "
        f"inválido, {incompletos} propuestos incompletos"
        + (f"; catálogo inválido: {defecto_catalogo}" if defecto_catalogo else "") + ".",
        viol,
        conteos={"sujetos": len(sujetos), "por_nivel": dict(por_nivel), "catalogo_ids": len(catalogo_ids),
                 "fuera_de_catalogo": fuera, "nivel_invalido": nivel_invalido,
                 "propuestos_incompletos": incompletos, "catalogo_defecto": defecto_catalogo},
    )


def shape_s20_enum(nodes, vocab):
    enum = tuple(vocab["obligacion_tipo"])
    retirados = set(vocab["retirados"])
    c_ret, c_otros = Counter(), Counter()
    viol = []
    obligaciones = [n for n in nodes if n["type"] == "Obligacion"]
    for n in obligaciones:
        tipo = (n.get("properties") or {}).get("tipo")
        if tipo in enum:
            continue
        if tipo in retirados:
            c_ret[tipo] += 1
            viol.append(f"nodo {n['id']}: tipo={tipo!r} (valor RETIRADO del enum)")
        else:
            # clave como str plano (None -> 'None'): sin comillas anidadas al
            # imprimir el Counter en el resumen y en el .json.
            c_otros[str(tipo)] += 1
            viol.append(f"nodo {n['id']}: tipo={tipo!r} (fuera del enum)")
    n_ret, n_otros = sum(c_ret.values()), sum(c_otros.values())
    return _res(
        "S20",
        f"ERROR — Enum de Obligacion.tipo: para todo nodo Obligacion, properties.tipo ∈ "
        f"{{{'|'.join(enum)}}}. Valores retirados ({', '.join(sorted(retirados))}) y otros valores "
        f"fuera del enum se cuentan por separado; bloqueante si cualquiera de los dos es distinto de 0.",
        "PASS" if not viol else "FAIL",
        f"{len(obligaciones) - len(viol)}/{len(obligaciones)} Obligaciones con tipo en el enum. "
        f"Valores retirados: {n_ret} ({dict(c_ret)}). Otros valores fuera del enum: {n_otros} ({dict(c_otros)}).",
        viol,
        conteos={"obligaciones": len(obligaciones), "en_enum": len(obligaciones) - len(viol),
                 "retirados": {"total": n_ret, "por_valor": dict(c_ret)},
                 "otros_fuera_del_enum": {"total": n_otros, "por_valor": dict(c_otros)}},
    )


def shape_s21_referencias(edges, node_by_id):
    total_via, incoh_via = Counter(), Counter()
    n_refs = 0
    viol = []
    for i, e in enumerate(edges):
        if norm(e["relation"]) != "referencia" or e.get("rol_fuente") != ROL_FUENTE_REFERENCIA_CRUZADA:
            continue
        n_refs += 1
        props = e.get("properties") or {}
        via = props.get("via")
        destino = props.get("destino")
        total_via[via] += 1
        punto = destino_sin_prefijo(destino)
        tn = node_by_id.get(e["target"])
        puntos = {p.get("punto") for p in ((tn or {}).get("provenances") or []) if isinstance(p, dict)}
        if punto not in puntos:
            incoh_via[via] += 1
            muestra = sorted(str(p) for p in puntos)
            viol.append(
                f"idx {i}: {e['source']} -> {e['target']} destino={destino!r} via={via!r}: "
                f"punto {punto!r} ∉ puntos del destino {muestra[:5]}{'...' if len(muestra) > 5 else ''}")
    n_incoh = sum(incoh_via.values())
    return _res(
        "S21",
        "INFORMATIVA — Coherencia de referencias nodo->nodo (rol_fuente=referencia_cruzada): "
        "properties.destino sin el prefijo <to>:: pertenece al CONJUNTO {p.punto for p in provenances} "
        "del nodo destino (nunca solo provenance[0]); desglose por properties.via.",
        "PASS" if not viol else "WARN",
        f"{n_refs} referencias nodo->nodo ({dict(total_via)}); {n_incoh} incoherentes "
        f"(por via: {dict(incoh_via)}).",
        viol,
        conteos={"referencias_cruzadas": n_refs, "por_via": dict(total_via),
                 "incoherentes": n_incoh, "incoherentes_por_via": dict(incoh_via)},
    )


def shape_s22_padre_sugerido(edges, node_by_id):
    n_ps = destino_distinto = sin_cuarentena = 0
    viol = []
    for i, e in enumerate(edges):
        if norm(e["relation"]) != RELACION_PADRE_SUGERIDO:
            continue
        n_ps += 1
        sn = node_by_id.get(e["source"])
        props = (sn or {}).get("properties") or {}
        problemas = []
        if e["target"] != props.get("padre_sugerido"):
            destino_distinto += 1
            problemas.append(f"destino ≠ properties.padre_sugerido del origen ({props.get('padre_sugerido')!r})")
        if not en_cuarentena(props):
            sin_cuarentena += 1
            problemas.append(f"origen no está en cuarentena (cuarentena={props.get('cuarentena')!r})")
        if problemas:
            viol.append(f"idx {i}: {e['source']} -> {e['target']}: {'; '.join(problemas)}")
    return _res(
        "S22",
        "INFORMATIVA — Coherencia de padre_sugerido: el destino de la arista es "
        "properties.padre_sugerido del origen y el origen está en cuarentena.",
        "PASS" if not viol else "WARN",
        f"{n_ps} aristas padre_sugerido; {len(viol)} incoherentes ({destino_distinto} con destino "
        f"distinto, {sin_cuarentena} con origen fuera de cuarentena).",
        viol,
        conteos={"aristas_padre_sugerido": n_ps, "incoherentes": len(viol),
                 "destino_distinto": destino_distinto, "origen_sin_cuarentena": sin_cuarentena},
    )


def shape_s23_aplica_a_cuarentena(edges, node_by_id):
    n_aplica = 0
    hacia = []
    destinos = Counter()
    for i, e in enumerate(edges):
        if norm(e["relation"]) != "aplica_a":
            continue
        n_aplica += 1
        tn = node_by_id.get(e["target"])
        if tn and tn["type"] == "Sujeto" and nivel_de(tn) == "propuesto":
            destinos[e["target"]] += 1
            hacia.append(f"idx {i}: {e['source']} -> {e['target']}")
    return _res(
        "S23",
        "INFORMATIVA — aplica_a hacia sujetos en cuarentena: aristas aplica_a cuyo destino es un "
        "Sujeto de nivel propuesto (conteo; nunca bloqueante).",
        "PASS" if not hacia else "WARN",
        f"{n_aplica} aristas aplica_a; {len(hacia)} hacia Sujetos propuestos "
        f"({len(destinos)} destinos distintos).",
        hacia,
        conteos={"aplica_a": n_aplica, "hacia_propuestos": len(hacia),
                 "destinos_distintos": len(destinos)},
    )


def evaluar_perfil_congelado(g, vocab, excepciones_ruta):
    """Evalúa el grafo `g` bajo el perfil congelado. Devuelve
    (resultados ordenados por ORDEN_SHAPES_CONGELADO, veredicto, meta)."""
    nodes, edges = g["nodes"], g["edges"]
    node_by_id = {n["id"]: n for n in nodes}
    out_edges = defaultdict(list)
    for e in edges:
        out_edges[e["source"]].append(e)

    catalogo_ids, n_clases, n_roles, defecto_cat = cargar_catalogo_sujetos(excepciones_ruta)
    dom_est = tuple(sorted(vocab["domain_range"]["establecida_en"][0]))
    dom_apl = tuple(sorted(vocab["domain_range"]["aplica_a"][0]))

    lista = [
        shape_s1_congelado(edges, vocab),
        shape_s2(edges, node_by_id),
        shape_s3_congelado(edges, node_by_id, vocab),
        shape_s4_congelado(nodes, edges),
        shape_s5_congelado(nodes, edges),
        shape_s6_congelado(nodes, edges),
        shape_s15(nodes, edges, node_by_id, excepciones_ruta),
        shape_s19_catalogo(nodes, catalogo_ids, defecto_cat),
        shape_s20_enum(nodes, vocab),
        shape_s7(nodes),
        shape_s8(nodes),
        shape_s9(nodes),
        shape_s10(nodes, out_edges, tipos=dom_est,
                  enunciado=f"ERROR — Todo nodo del dominio congelado de establecida_en "
                            f"({'/'.join(dom_est)}) tiene >=1 arista saliente establecida_en."),
        shape_s11(nodes, out_edges, tipos=dom_apl,
                  enunciado=f"WARN — Todo nodo del dominio congelado de aplica_a "
                            f"({'/'.join(dom_apl)}) tiene >=1 arista saliente aplica_a."),
        shape_s12(nodes, out_edges),
        shape_s21_referencias(edges, node_by_id),
        shape_s22_padre_sugerido(edges, node_by_id),
        shape_s23_aplica_a_cuarentena(edges, node_by_id),
    ]
    resultados = {r["rid"]: r for r in lista}
    assert list(resultados) == ORDEN_SHAPES_CONGELADO, "orden de shapes del perfil roto"
    bloqueantes_fail = [rid for rid in BLOQUEANTES_CONGELADO if resultados[rid]["result"] != "PASS"]
    veredicto = "PASA" if not bloqueantes_fail else "NO PASA"
    meta = {
        "catalogo": {"ruta": excepciones_ruta, "n_ids": len(catalogo_ids),
                     "n_clases": n_clases, "n_roles": n_roles, "defecto": defecto_cat},
        "bloqueantes_en_fail": bloqueantes_fail,
    }
    return resultados, veredicto, meta


def sha256_archivo(ruta):
    h = hashlib.sha256()
    with open(ruta, "rb") as f:
        for bloque in iter(lambda: f.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


def correr_perfil_congelado(args, g):
    """Camino completo del perfil: carga el vocabulario (FRENA si el candado
    no cierra), evalúa, escribe .md + .json si hay --out, imprime por consola
    y devuelve el código de salida (0 PASA, 1 NO PASA, 2 freno del candado)."""
    try:
        vocab = cargar_vocabulario_congelado()
    except VocabularioCongeladoError as e:
        print(f"FRENO — perfil congelado: {e}", file=sys.stderr)
        return 2

    nodes, edges = g["nodes"], g["edges"]
    resultados, veredicto, meta = evaluar_perfil_congelado(g, vocab, args.excepciones)
    fecha = datetime.date.today().isoformat()
    sha_grafo = sha256_archivo(args.kg)
    cat = meta["catalogo"]

    cabecera = [
        f"- **Grafo:** `{args.kg}`",
        f"- **sha256 del grafo:** `{sha_grafo}`",
        f"- **Fecha:** {fecha}",
        f"- **Nodos:** {len(nodes)}",
        f"- **Aristas:** {len(edges)}",
        "- **Perfil:** congelado",
        f"- **Vocabulario:** `{vocab['modulo']}` — sha256 del prefijo `{vocab['sha256_prefijo']}` "
        f"(hash system+tools `{vocab['hash_prefijo']}`); {len(vocab['entity_types'])} tipos, "
        f"{len(vocab['predicates'])} predicados, enum Obligacion.tipo de {len(vocab['obligacion_tipo'])} "
        f"(retirados: {', '.join(vocab['retirados'])})",
        f"- **Catálogo de sujetos:** `{cat['ruta']}` — {cat['n_ids']} ids ({cat['n_clases']} clases, "
        f"{cat['n_roles']} roles)" + (f"; DEFECTO: {cat['defecto']}" if cat["defecto"] else ""),
        f"- **Veredicto global: {veredicto}**"
        + (f" — bloqueantes en FAIL: {', '.join(meta['bloqueantes_en_fail'])}"
           if meta["bloqueantes_en_fail"] else " — todas las bloqueantes en PASS"),
    ]

    def seccion(titulo, rids):
        out = [f"## {titulo}", ""]
        for rid in rids:
            r = resultados[rid]
            out += [f"### {rid} — {r['result']}", "", r["enunciado"], "", f"**Resultado:** {r['resumen']}", ""]
            if r["detalle_md"]:
                out += ["```"] + r["detalle_md"] + ["```", ""]
            else:
                out += ["Sin violaciones.", ""]
        return out

    lineas = ["# Validador de shapes — perfil congelado", ""] + cabecera + [""]
    lineas += seccion("Bloqueantes", BLOQUEANTES_CONGELADO)
    lineas += seccion("Informativas", INFORMATIVAS_CONGELADO)
    lineas += ["## Tabla resumen", "", "| Severidad | Regla | Resultado | Resumen |", "|---|---|---|---|"]
    for rid in ORDEN_SHAPES_CONGELADO:
        r = resultados[rid]
        sev = "bloqueante" if rid in BLOQUEANTES_CONGELADO else "informativa"
        lineas.append(f"| {sev} | {rid} | {r['result']} | {r['resumen']} |")
    lineas += ["", f"**Veredicto global: {veredicto}**", ""]
    lineas += ["## Numeración de las shapes nuevas del perfil", ""]
    lineas += [f"- {rid}: {enun}" for rid, enun in NUMERACION_PERFIL.items()]
    lineas += ["", "## Fuera del perfil", ""]
    lineas += [f"- {rid}: {motivo}" for rid, motivo in FUERA_DEL_PERFIL.items()]
    lineas += [f"- {', '.join(SHAPES_NO_IMPLEMENTADAS)}: no implementadas (se declaran para que su "
               "ausencia se lea; no se inventan).",
               "- S18: número ya declarado en docs/esquema_v2_diseño.md con otro enunciado "
               "(umbral de limita); no se reutiliza.", ""]

    salida_json = {
        "perfil": "congelado",
        "grafo": args.kg,
        "sha256_grafo": sha_grafo,
        "fecha": fecha,
        "nodos": len(nodes),
        "aristas": len(edges),
        "vocabulario": {
            "modulo": vocab["modulo"],
            "sha256_prefijo": vocab["sha256_prefijo"],
            "hash_prefijo": vocab["hash_prefijo"],
            "n_tipos": len(vocab["entity_types"]),
            "n_predicados": len(vocab["predicates"]),
            "enum_obligacion_tipo": list(vocab["obligacion_tipo"]),
            "retirados": list(vocab["retirados"]),
        },
        "catalogo": cat,
        "veredicto": veredicto,
        "bloqueantes_en_fail": meta["bloqueantes_en_fail"],
        "shapes": {
            rid: {
                "severidad": "bloqueante" if rid in BLOQUEANTES_CONGELADO else "informativa",
                "result": resultados[rid]["result"],
                "resumen": resultados[rid]["resumen"],
                "conteos": resultados[rid]["conteos"],
            } for rid in ORDEN_SHAPES_CONGELADO
        },
        "numeracion_perfil": NUMERACION_PERFIL,
        "fuera_del_perfil": dict(FUERA_DEL_PERFIL, **{s: "no implementada" for s in SHAPES_NO_IMPLEMENTADAS}),
    }

    ruta_json = None
    if args.out:
        os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as f:
            f.write("\n".join(lineas))
        ruta_json = os.path.splitext(args.out)[0] + ".json"
        with open(ruta_json, "w", encoding="utf-8") as f:
            json.dump(salida_json, f, ensure_ascii=False, indent=2)
            f.write("\n")

    # ---------- Consola ----------
    print(f"Grafo: {args.kg}")
    print(f"Nodos: {len(nodes)} | Aristas: {len(edges)} | Perfil: congelado")
    print(f"Vocabulario: {vocab['modulo']} (sha256 prefijo {vocab['sha256_prefijo'][:12]}…)")
    print(f"Catálogo: {cat['ruta']} ({cat['n_ids']} ids)\n")
    for titulo, rids in (("BLOQUEANTES", BLOQUEANTES_CONGELADO), ("INFORMATIVAS", INFORMATIVAS_CONGELADO)):
        print(f"=== {titulo} ===")
        for rid in rids:
            r = resultados[rid]
            print(f"[{r['result']:4s}] {rid} — {r['resumen']}")
            for linea in lista_consola(r["detalle_consola"]):
                print(f"        {linea}")
        print()
    print("=== TABLA RESUMEN ===")
    print(f"{'Sever.':12s} {'Regla':6s} {'Resultado':10s} Resumen")
    for rid in ORDEN_SHAPES_CONGELADO:
        r = resultados[rid]
        sev = "bloqueante" if rid in BLOQUEANTES_CONGELADO else "informativa"
        print(f"{sev:12s} {rid:6s} {r['result']:10s} {r['resumen']}")
    print(f"\nVEREDICTO GLOBAL: {veredicto}"
          + (f" (bloqueantes en FAIL: {', '.join(meta['bloqueantes_en_fail'])})"
             if meta["bloqueantes_en_fail"] else ""))
    if args.out:
        print(f"\nReporte escrito en: {os.path.abspath(args.out)}")
        print(f"Conteos escritos en: {os.path.abspath(ruta_json)}")
    else:
        print("\n(sin --out: no se escribió ningún archivo)")
    return 0 if veredicto == "PASA" else 1


def main():
    ap = argparse.ArgumentParser(description="Validador de shapes v0 (capas 1 y 2)")
    ap.add_argument("--kg", default=DEFAULT_KG, help="Ruta al kg.json (solo lectura)")
    ap.add_argument("--out", default=DEFAULT_OUT,
                    help="Ruta del reporte Markdown. SIN default: si no se pasa, el "
                         "validador reporta por consola y no escribe ningún archivo.")
    ap.add_argument("--excepciones", default=None,
                    help="Artefacto con el bloque 'excepciones_s15' (S15). Sin esta opción "
                         "la lista declarada es vacía y todo rol huérfano es FAIL.")
    ap.add_argument("--perfil", default=None, choices=PERFILES,
                    help="Perfil de validación. Sin esta opción el comportamiento es el de "
                         "siempre (v0). 'congelado': esquema congelado de la generación 3, "
                         "vocabulario leído de prompt_congelado.py, catálogo de sujetos "
                         "leído de --excepciones, veredicto PASA/NO PASA y .json de conteos.")
    args = ap.parse_args()

    with open(args.kg, encoding="utf-8") as f:
        g = json.load(f)

    if args.perfil == "congelado":
        sys.exit(correr_perfil_congelado(args, g))

    nodes, edges = g["nodes"], g["edges"]
    node_by_id = {n["id"]: n for n in nodes}
    out_edges = defaultdict(list)
    for e in edges:
        out_edges[e["source"]].append(e)

    resultados = {}   # regla -> dict(result, resumen, detalle_md, detalle_consola)

    def registrar(rid, enunciado, result, resumen, detalle_md, detalle_consola=None):
        resultados[rid] = {
            "enunciado": enunciado,
            "result": result,
            "resumen": resumen,
            "detalle_md": detalle_md,
            "detalle_consola": detalle_consola if detalle_consola is not None else detalle_md,
        }

    def registrar_res(r):
        resultados[r["rid"]] = r

    # ---------- S1 ----------
    viol = [f"idx {i}: relation='{e['relation']}'"
            for i, e in enumerate(edges) if norm(e["relation"]) not in RELACIONES_12]
    registrar(
        "S1", "Toda arista usa una de las 12 relaciones del esquema (nombre normalizado).",
        "PASS" if not viol else "FAIL",
        f"{len(edges) - len(viol)}/{len(edges)} aristas con relación válida; {len(viol)} violaciones.",
        viol,
    )

    # ---------- S2 ----------
    registrar_res(shape_s2(edges, node_by_id))

    # ---------- S3 ----------
    viol = []
    for i, e in enumerate(edges):
        rel = norm(e["relation"])
        if rel not in FIRMAS or e["source"] not in node_by_id or e["target"] not in node_by_id:
            continue  # capturado por S1/S2
        dominios, rango = FIRMAS[rel]
        st = node_by_id[e["source"]]["type"]
        dt = node_by_id[e["target"]]["type"]
        if st not in dominios or dt != rango:
            viol.append(f"idx {i}: {rel} {st} -> {dt} ({e['source']} -> {e['target']})")
    registrar(
        "S3", "Toda arista respeta la matriz de firmas dominio -> rango declarada en FIRMAS.",
        "PASS" if not viol else "FAIL",
        f"{len(edges) - len(viol)}/{len(edges)} aristas conformes a firma; {len(viol)} violaciones.",
        viol,
    )

    # ---------- S4 ----------
    viol = []
    nodos_ok = 0
    for n in nodes:
        d = check_provenance(n.get("provenance"))
        if d:
            viol.append(f"nodo {n['id']}: {'; '.join(d)}")
        else:
            nodos_ok += 1
    aristas_ok = 0
    for i, e in enumerate(edges):
        d = check_provenance(e.get("provenance"))
        if d:
            viol.append(f"arista idx {i} ({e['relation']} {e['source']} -> {e['target']}): {'; '.join(d)}")
        else:
            aristas_ok += 1
    registrar(
        "S4", "Todo nodo y toda arista tienen provenance dict con exactamente source_doc y location, strings no vacías.",
        "PASS" if not viol else "FAIL",
        f"Nodos OK: {nodos_ok}/{len(nodes)}. Aristas OK: {aristas_ok}/{len(edges)}. Violaciones: {len(viol)}.",
        viol,
    )

    # ---------- S5 ----------
    viol = []
    n_loc_nodos = n_loc_aristas = 0
    for n in nodes:
        loc = (n.get("provenance") or {}).get("location", "")
        if "punto" in norm(loc):
            n_loc_nodos += 1
        else:
            viol.append(f"nodo {n['id']}: location='{loc[:80]}'")
    for i, e in enumerate(edges):
        loc = (e.get("provenance") or {}).get("location", "")
        if "punto" in norm(loc):
            n_loc_aristas += 1
        else:
            viol.append(f"arista idx {i} ({e['relation']}): location='{loc[:80]}'")
    registrar(
        "S5", "Todo location (de nodo y de arista) contiene 'punto' (normalizado).",
        "PASS" if not viol else "FAIL",
        f"Nodos con 'punto': {n_loc_nodos}/{len(nodes)}. Aristas: {n_loc_aristas}/{len(edges)}. Violaciones: {len(viol)}.",
        viol,
    )

    # ---------- S6 ----------
    archivos = {n["properties"].get("archivo") for n in nodes if n["type"] == "TextoOrdenado"}
    archivos.discard(None)
    viol = []
    for n in nodes:
        sd = (n.get("provenance") or {}).get("source_doc")
        if sd not in archivos:
            viol.append(f"nodo {n['id']}: source_doc='{sd}'")
    for i, e in enumerate(edges):
        sd = (e.get("provenance") or {}).get("source_doc")
        if sd not in archivos:
            viol.append(f"arista idx {i} ({e['relation']}): source_doc='{sd}'")
    registrar(
        "S6", "Todo source_doc pertenece al conjunto de valores de 'archivo' de los nodos TextoOrdenado.",
        "PASS" if not viol else "FAIL",
        f"Archivos válidos ({len(archivos)}): {sorted(archivos)}. Violaciones: {len(viol)}.",
        viol,
    )

    # ---------- S7 ----------
    registrar_res(shape_s7(nodes))

    # ---------- S8 ----------
    registrar_res(shape_s8(nodes))

    # ---------- S9 ----------
    registrar_res(shape_s9(nodes))

    # ---------- S10 ----------
    registrar_res(shape_s10(nodes, out_edges))

    # ---------- S11 ----------
    registrar_res(shape_s11(nodes, out_edges))

    # ---------- S12 ----------
    registrar_res(shape_s12(nodes, out_edges))

    # ---------- S15 (U-ESQ-V3) ----------
    registrar_res(shape_s15(nodes, edges, node_by_id, args.excepciones))

    # ---------- Reporte ----------
    if args.out:
        os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    fecha = datetime.date.today().isoformat()
    orden = list(ORDEN_SHAPES)
    lineas = [
        "# Validador de shapes v0 — capas 1 y 2",
        "",
        f"- **Grafo:** `{args.kg}`",
        f"- **Fecha:** {fecha}",
        f"- **Nodos:** {len(nodes)}",
        f"- **Aristas:** {len(edges)}",
        "",
    ]
    for rid in orden:
        r = resultados[rid]
        lineas += [f"## {rid} — {r['result']}", "", r["enunciado"], "", f"**Resultado:** {r['resumen']}", ""]
        if r["detalle_md"]:
            lineas += ["```"] + r["detalle_md"] + ["```", ""]
        else:
            lineas += ["Sin violaciones.", ""]
    lineas += ["## Tabla resumen", "", "| Regla | Resultado | Resumen |", "|---|---|---|"]
    for rid in orden:
        r = resultados[rid]
        lineas.append(f"| {rid} | {r['result']} | {r['resumen']} |")
    lineas.append("")
    lineas += [
        f"## Shapes no implementadas: {', '.join(SHAPES_NO_IMPLEMENTADAS)}",
        "",
        "Se declaran para que su ausencia se lea. No se inventan: implementarlas es otra unidad.",
        "",
    ]
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write("\n".join(lineas))

    # ---------- Consola ----------
    print(f"Grafo: {args.kg}")
    print(f"Nodos: {len(nodes)} | Aristas: {len(edges)}\n")
    for rid in orden:
        r = resultados[rid]
        print(f"[{r['result']:4s}] {rid} — {r['resumen']}")
        for linea in lista_consola(r["detalle_consola"]):
            print(f"        {linea}")
    print("\n=== TABLA RESUMEN ===")
    print(f"{'Regla':6s} {'Resultado':10s} Resumen")
    for rid in orden:
        r = resultados[rid]
        print(f"{rid:6s} {r['result']:10s} {r['resumen']}")
    if args.out:
        print(f"\nReporte escrito en: {os.path.abspath(args.out)}")
    else:
        print("\n(sin --out: no se escribió ningún archivo)")


if __name__ == "__main__":
    main()
