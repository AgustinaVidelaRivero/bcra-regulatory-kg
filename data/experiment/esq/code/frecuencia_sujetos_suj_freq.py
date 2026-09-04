#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""U-SUJ-FREQ — Analisis de frecuencia de sujeto_propuesto (insumo de B5.4).

Lee, en modo SOLO LECTURA:

  UNIVERSO PRIMARIO (una extraccion por unidad, esquema de produccion):
    - dev (corpus_v2): data/experiment/reextraccion_v2/corpus_v2/salida/
      {cap,cla,ext,pro,ric}/extracciones_e1.jsonl (~1.769 registros E1; las
      unidades con reextraccion dirigida aparecen dos veces y se queda el
      ULTIMO registro del archivo, que es la reextraccion que la supersede).
    - ESQ-2 (cobertura): data/experiment/esq/cobertura/*/extracciones_e1_*.jsonl
      (762 extracciones, 10 TOs).

  TABLA LATERAL (descriptiva, SIN peso en el corte):
    - data/experiment/esq/esq3b/extracciones/pareado_esq3b.jsonl (43) y
      data/experiment/esq/esq3b_v2/extracciones/pareado_esq3b_v2.jsonl (27):
      re-extracciones de unidades ya contadas en el primario, bajo esquema
      retocado. No tienen capa `validacion`: se leen de `tool_input_crudo`.

y produce:

  1. El inventario EXACTO del catalogo vigente de sujetos contra el tool
     schema de produccion (prompt_e1.TOOL_SCHEMA_E1, enum de sujeto_id), no
     contra la prosa del prompt; con label/alias/nivel/padre desde
     data/experiment/grafo_v2/esquema_v2_clases.json.
  2. La distribucion de sujeto_id y de sujeto_propuesto sobre TODAS las
     relaciones con sujeto (aplica_a / ejecuta) del universo primario.
  3. La agrupacion MECANICA (sin LLM) de los sujeto_propuesto por nucleo
     nominal (dos primeras palabras de contenido, reducidas a raiz), con el
     criterio de corte sellado en el mandato ANTES de mirar distribucion
     alguna: >= 20 unidades Y >= 5 TOs, de los cuales >= 2 de ESQ-2.
  4. La tabla lateral: los mismos grupos sobre las 70 re-extracciones
     retocadas, descriptiva y separada del primario.

Costo de API: USD 0 — el script no hace ninguna llamada LLM.

Reproduccion:
    python3 data/experiment/esq/code/frecuencia_sujetos_suj_freq.py
    python3 data/experiment/esq/code/frecuencia_sujetos_suj_freq.py --selftest

Salidas (unicos archivos que el script escribe):
    data/experiment/esq/cobertura/frecuencia_sujetos_suj_freq.json
    data/experiment/esq/cobertura/frecuencia_sujetos_suj_freq.md

El normalizador, la lista de palabras funcionales y el recorte de raiz estan
COPIADOS de frecuencia_subtipos_r9.py (patron U-R9-FREQ); ese archivo no se
toca. El script no escribe ni modifica ningun otro archivo.
"""

from __future__ import annotations

import argparse
import collections
import glob
import hashlib
import json
import os
import re
import sys
import unicodedata

# ---------------------------------------------------------------------------
# Rutas
# ---------------------------------------------------------------------------

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
DIR_COBERTURA = os.path.join(RAIZ, "data", "experiment", "esq", "cobertura")
DIR_CORPUS_V2 = os.path.join(RAIZ, "data", "experiment", "reextraccion_v2", "corpus_v2", "salida")
DIR_E1 = os.path.join(RAIZ, "data", "experiment", "reextraccion_v2", "e1_extractor")
RUTA_CATALOGO_JSON = os.path.join(RAIZ, "data", "experiment", "grafo_v2", "esquema_v2_clases.json")

DEV_TOS = ("cap", "cla", "ext", "pro", "ric")
ESQ2_TOS = ("actgar", "adrei", "ayccef", "cryl", "ctacor",
            "expaef", "lavdin", "opefci", "prevmi", "traval")

PATRON_ESQ2 = os.path.join(DIR_COBERTURA, "*", "extracciones_e1_*.jsonl")
RUTAS_LATERAL = (
    ("esq3b", os.path.join(RAIZ, "data", "experiment", "esq", "esq3b",
                           "extracciones", "pareado_esq3b.jsonl")),
    ("esq3b_v2", os.path.join(RAIZ, "data", "experiment", "esq", "esq3b_v2",
                              "extracciones", "pareado_esq3b_v2.jsonl")),
)

SALIDA_JSON = os.path.join(DIR_COBERTURA, "frecuencia_sujetos_suj_freq.json")
SALIDA_MD = os.path.join(DIR_COBERTURA, "frecuencia_sujetos_suj_freq.md")

# ---------------------------------------------------------------------------
# Criterio de corte — SELLADO en el mandato de la unidad, ANTES de mirar
# distribucion alguna. No calibrado: su virtud es ser anterior y auditable.
# ---------------------------------------------------------------------------

MIN_UNIDADES = 20
MIN_TOS = 5
MIN_TOS_ESQ2 = 2

PREDICADOS_SUJETO = ("aplica_a", "ejecuta")

# ---------------------------------------------------------------------------
# Agrupador mecanico — todas las reglas son visibles aca. Sin LLM.
#
# Un sujeto_propuesto es una frase NOMINAL ("las empresas de seguros", "bancos
# del exterior"), no una clausula con predicado deontico. El nucleo nominal
# son las DOS primeras palabras de contenido de la frase normalizada (en los
# sujetos del corpus la cabeza suele ser generica —"empresas", "entidades",
# "proveedores"— y lo que distingue es el primer modificador). Cada palabra se
# reduce a raiz con el recorte morfologico de U-R9-FREQ. La clave del grupo es
# "raiz1+raiz2" (o "raiz1" si la frase tiene una sola palabra de contenido).
# Sin tabla de sinonimos: los grupos imperfectos quedan a la vista y los
# conteos por grupo son cota inferior de la frecuencia del contenido.
#
# normalizar(), PALABRAS_FUNCIONALES, MARCADORES_DEONTICOS, ENCLITICOS,
# SUFIJOS y raiz() copiados sin cambios de frecuencia_subtipos_r9.py.
# ---------------------------------------------------------------------------

PALABRAS_FUNCIONALES = set(
    """
    el la los las un una unos unas de del al a en con por para sin sobre entre
    segun contra desde hasta durante ante bajo tras
    como que cual cuales quien quienes cuyo cuya cuyos cuyas y o u e ni pero sino
    se le les lo me nos su sus mi mis tu tus
    este esta estos estas ese esa esos esas aquel aquella aquellos aquellas
    cuando donde mientras si no tal tales todo toda todos todas
    cada cualquier cualquiera otro otra otros otras
    mismo misma mismos mismas dicho dicha dichos dichas ello ella
    ademas asimismo tambien solo solamente unicamente incluso aun aunque asi ya
    mas menos muy tan tanto tanta tantos tantas ambos ambas
    ser sido siendo estar estado haber habido
    """.split()
)

MARCADORES_DEONTICOS = set(
    """
    debe deben debera deberan debia debian deberia deberian deber debiendo
    puede pueden podra podran podria podrian poder pudiendo
    tiene tienen tendra tendran tenga tengan
    es son era eran sera seran fue fueron fuere seria serian sea sean
    esta estan estara estaran esten
    ha han habra habran haya hayan hubiere hubieren
    queda quedan quedara quedaran quede queden
    corresponde corresponden correspondera correspondan
    """.split()
)

ENCLITICOS = ("arse", "erse", "irse", "arlo", "arla", "arle", "arles")

SUFIJOS = [
    "aciones", "acion", "ciones", "cion",
    "mientos", "miento", "ancias", "ancia", "encias", "encia",
    "idades", "idad", "ables", "able", "ibles", "ible",
    "aran", "eran", "iran", "arian", "erian", "irian",
    "ando", "iendo", "endo", "aron", "ieron",
    "aba", "aban", "ara", "are", "aren",
    "ados", "adas", "ado", "ada", "idos", "idas", "ido", "ida",
    "ores", "ora", "oras", "or", "ivos", "ivas", "ivo", "iva",
    "ales", "al", "ar", "er", "ir", "an", "en",
    "as", "os", "es", "a", "e", "o", "s",
]

LONG_MIN_RAIZ = 4
LONG_MIN_TOKEN = 3

CLAVE_SIN_NUCLEO = "(sin_nucleo)"


def normalizar(texto: str) -> str:
    """Minusculas, sin diacriticos, solo letras, espacios colapsados."""
    descompuesto = unicodedata.normalize("NFD", (texto or "").lower())
    plano = "".join(c for c in descompuesto if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-zñ]+", " ", plano).strip()


def raiz(token: str) -> str:
    """Recorta enclitico + un sufijo + vocal tematica final. Reglas visibles."""
    for enc in ENCLITICOS:
        if token.endswith(enc):
            token = token[: -2] if enc in ("arse", "erse", "irse") else token[: -len(enc) + 2]
            break
    for suf in SUFIJOS:
        if token.endswith(suf) and len(token) - len(suf) >= LONG_MIN_RAIZ:
            token = token[: -len(suf)]
            break
    if len(token) >= LONG_MIN_RAIZ + 1 and token[-1] in "aeio":
        token = token[:-1]
    return token


def palabras_de_contenido(texto: str) -> list:
    """Tokens normalizados de >= 3 letras que no son funcionales ni marcadores."""
    return [
        t for t in normalizar(texto).split()
        if len(t) >= LONG_MIN_TOKEN
        and t not in PALABRAS_FUNCIONALES
        and t not in MARCADORES_DEONTICOS
    ]


def clave_grupo(texto: str) -> str:
    """Clave del grupo: raiz de las dos primeras palabras de contenido."""
    tokens = palabras_de_contenido(texto)
    if not tokens:
        return CLAVE_SIN_NUCLEO
    r1 = raiz(tokens[0])
    if len(tokens) == 1:
        return r1
    return f"{r1}+{raiz(tokens[1])}"


# ---------------------------------------------------------------------------
# Inventario del catalogo vigente (contra el tool schema, no contra la prosa)
# ---------------------------------------------------------------------------

def inventario_catalogo():
    if DIR_E1 not in sys.path:
        sys.path.insert(0, DIR_E1)
    import prompt_e1  # noqa: E402  (produccion; no hace llamadas LLM)

    schema_rel = (prompt_e1.TOOL_SCHEMA_E1["input_schema"]["properties"]
                  ["relations"]["items"]["properties"])
    enum_sujeto_id = list(schema_rel["sujeto_id"]["enum"])
    enum_padre = list(schema_rel["sujeto_propuesto_padre_sugerido"]["enum"])

    with open(RUTA_CATALOGO_JSON, encoding="utf-8") as fh:
        cat = json.load(fh)
    por_id = {}
    for e in cat["clases"]:
        por_id[e["id"]] = {
            "nivel": e["nivel"],
            "label": e["label"],
            "alias": list(e.get("alias") or []),
            "padre": e.get("padre") or e.get("instancia_de"),
        }
    for r in cat["roles"]:
        por_id[r["id"]] = {
            "nivel": "rol",
            "label": r["label"],
            "alias": [],
            "padre": None,
            "to": r["to"],
            "miembros": list(r["miembros"]),
        }

    # Prosa instructiva = prefijo de sistema SIN el bloque del catalogo
    # interpolado (SUJETOS_PROMPT lista los 70 ids por construccion; lo que
    # interesa es cuantos ids nombra la prosa de reglas y ejemplos).
    prosa = prompt_e1.prefijo_sistema(False).replace(prompt_e1.SUJETOS_PROMPT, "")
    entradas = []
    for sid in enum_sujeto_id:
        info = por_id.get(sid, {"nivel": "(fuera del json)", "label": "", "alias": [], "padre": None})
        entradas.append({
            "id": sid,
            "nivel": info["nivel"],
            "label": info["label"],
            "alias": info["alias"],
            "padre": info.get("padre"),
            "to_del_rol": info.get("to"),
            "nombrado_en_prosa_instructiva": bool(re.search(rf"\b{re.escape(sid)}\b", prosa)),
        })

    # Coherencia del enum con los prompts retocado / v2 / congelado (informativa).
    coherencia = {}
    dir_esq_code = os.path.dirname(os.path.abspath(__file__))
    if dir_esq_code not in sys.path:
        sys.path.insert(0, dir_esq_code)
    for nombre, modulo, attr in (
        ("retocado_esq3b", "prompt_esq3b", "TOOL_SCHEMA_RETOCADO"),
        ("v2_esq3b", "prompt_esq3b_v2", "TOOL_SCHEMA_V2"),
        ("congelado", "prompt_congelado", "TOOL_SCHEMA_CONGELADO"),
    ):
        try:
            mod = __import__(modulo)
            otro = (getattr(mod, attr)["input_schema"]["properties"]
                    ["relations"]["items"]["properties"]["sujeto_id"]["enum"])
            coherencia[nombre] = ("identico" if list(otro) == enum_sujeto_id
                                  else "DISTINTO")
        except Exception as exc:  # no rompe el analisis principal
            coherencia[nombre] = f"no verificable ({type(exc).__name__})"

    return {
        "fuente": "prompt_e1.TOOL_SCHEMA_E1 -> input_schema.properties.relations.items.properties.sujeto_id.enum",
        "version_catalogo": cat["version"],
        "n_ids": len(enum_sujeto_id),
        "n_clases": sum(1 for e in entradas if e["nivel"] == "clase"),
        "n_instancias": sum(1 for e in entradas if e["nivel"] == "instancia"),
        "n_roles": sum(1 for e in entradas if e["nivel"] == "rol"),
        "enum_padre_sugerido_identico": enum_padre == enum_sujeto_id,
        "n_nombrados_en_prosa_instructiva": sum(
            1 for e in entradas if e["nombrado_en_prosa_instructiva"]),
        "ids_nombrados_en_prosa_instructiva": sorted(
            e["id"] for e in entradas if e["nombrado_en_prosa_instructiva"]),
        "nota_definicion": ("el catalogo (esquema_v2_clases.json) no tiene campo "
                            "'definicion': cada entrada trae label, alias, nivel y padre; "
                            "eso es lo que existe y lo que se lista"),
        "coherencia_enum_prompts_posteriores": coherencia,
        "ids": entradas,
    }


# ---------------------------------------------------------------------------
# Lectura (solo lectura)
# ---------------------------------------------------------------------------

def sha256(ruta: str) -> str:
    h = hashlib.sha256()
    with open(ruta, "rb") as fh:
        for bloque in iter(lambda: fh.read(1 << 16), b""):
            h.update(bloque)
    return h.hexdigest()


def _leer_jsonl(ruta: str) -> list:
    regs = []
    with open(ruta, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.strip()
            if linea:
                regs.append(json.loads(linea))
    return regs


def cargar_universo_primario():
    """Relaciones con sujeto del universo primario (validacion.relaciones).

    dev: una extraccion por unidad — ante chunk_id duplicado (reextraccion
    dirigida) se queda el ULTIMO registro del archivo, en la posicion de
    lectura del primero. ESQ-2: se verifica que no haya duplicados.
    """
    relaciones = []
    meta_archivos = {}
    contadores = {
        "dev": {"n_registros_leidos": 0, "n_unidades": 0, "n_duplicados_supersedidos": 0,
                "n_con_error": 0, "n_rel_total_validacion": 0, "n_rel_sujeto_crudo": 0},
        "esq2": {"n_registros_leidos": 0, "n_unidades": 0, "n_duplicados_supersedidos": 0,
                 "n_con_error": 0, "n_rel_total_validacion": 0, "n_rel_sujeto_crudo": 0},
    }
    unidades_duplicadas = []

    rutas = [(os.path.join(DIR_CORPUS_V2, to, "extracciones_e1.jsonl"), "dev") for to in DEV_TOS]
    rutas += [(r, "esq2") for r in sorted(glob.glob(PATRON_ESQ2))]

    for ruta, origen in rutas:
        regs = _leer_jsonl(ruta)
        meta_archivos[os.path.relpath(ruta, RAIZ)] = sha256(ruta)
        contadores[origen]["n_registros_leidos"] += len(regs)
        por_unidad = {}  # chunk_id -> registro; conserva orden de primera aparicion
        for d in regs:
            cid = d["chunk_id"]
            if cid in por_unidad:
                contadores[origen]["n_duplicados_supersedidos"] += 1
                unidades_duplicadas.append(cid)
            por_unidad[cid] = d
        contadores[origen]["n_unidades"] += len(por_unidad)
        for cid, d in por_unidad.items():
            if d.get("error"):
                contadores[origen]["n_con_error"] += 1
            to = cid.split("::")[0]
            contadores[origen]["n_rel_sujeto_crudo"] += sum(
                1 for r in (d.get("tool_input_crudo") or {}).get("relations", [])
                if r.get("predicate") in PREDICADOS_SUJETO
            )
            for r in (d.get("validacion") or {}).get("relaciones", []):
                contadores[origen]["n_rel_total_validacion"] += 1
                if r.get("predicate") not in PREDICADOS_SUJETO:
                    continue
                relaciones.append({
                    "to": to,
                    "chunk_id": cid,
                    "origen": origen,
                    "predicate": r.get("predicate"),
                    "sujeto_id": r.get("sujeto_id"),
                    "sujeto_propuesto": (r.get("sujeto_propuesto") or "").strip() or None,
                    "padre_sugerido": r.get("sujeto_propuesto_padre_sugerido"),
                })

    meta = {
        "archivos_sha256": meta_archivos,
        "n_archivos": len(meta_archivos),
        "contadores": contadores,
        "unidades_duplicadas_dev": sorted(unidades_duplicadas),
        "regla_dedupe": ("una extraccion por unidad: ante chunk_id repetido se queda el "
                         "ultimo registro del archivo (la reextraccion dirigida posterior)"),
    }
    return relaciones, meta


def cargar_lateral():
    """Relaciones con sujeto de las 70 re-extracciones retocadas (crudo).

    Estos registros no tienen capa `validacion`: se lee tool_input_crudo.
    """
    relaciones = []
    meta_archivos = {}
    n_por_corrida = {}
    for corrida, ruta in RUTAS_LATERAL:
        regs = _leer_jsonl(ruta)
        meta_archivos[os.path.relpath(ruta, RAIZ)] = sha256(ruta)
        n_por_corrida[corrida] = len(regs)
        for d in regs:
            cid = d["chunk_id"]
            for r in (d.get("tool_input_crudo") or {}).get("relations", []):
                if r.get("predicate") not in PREDICADOS_SUJETO:
                    continue
                relaciones.append({
                    "to": cid.split("::")[0],
                    "chunk_id": cid,
                    "corrida": corrida,
                    "predicate": r.get("predicate"),
                    "sujeto_id": r.get("sujeto_id"),
                    "sujeto_propuesto": (r.get("sujeto_propuesto") or "").strip() or None,
                    "padre_sugerido": r.get("sujeto_propuesto_padre_sugerido"),
                })
    meta = {
        "archivos_sha256": meta_archivos,
        "n_registros_por_corrida": n_por_corrida,
        "capa": "tool_input_crudo (estos registros no tienen capa validacion)",
    }
    return relaciones, meta


# ---------------------------------------------------------------------------
# Analisis
# ---------------------------------------------------------------------------

def totales_canales(relaciones, clave_origen=None):
    t = {
        "n_rel_sujeto": len(relaciones),
        "por_predicado": dict(sorted(collections.Counter(r["predicate"] for r in relaciones).items())),
        "n_con_sujeto_id": sum(1 for r in relaciones if r["sujeto_id"]),
        "n_con_sujeto_propuesto": sum(1 for r in relaciones if r["sujeto_propuesto"]),
        "n_con_ambos": sum(1 for r in relaciones if r["sujeto_id"] and r["sujeto_propuesto"]),
        "n_sin_sujeto": sum(1 for r in relaciones if not r["sujeto_id"] and not r["sujeto_propuesto"]),
    }
    if clave_origen:
        t["por_origen"] = {}
        for val in sorted({r[clave_origen] for r in relaciones}):
            sub = [r for r in relaciones if r[clave_origen] == val]
            t["por_origen"][val] = {
                "n_rel_sujeto": len(sub),
                "n_con_sujeto_id": sum(1 for r in sub if r["sujeto_id"]),
                "n_con_sujeto_propuesto": sum(1 for r in sub if r["sujeto_propuesto"]),
            }
    return t


def distribucion_sujeto_id(relaciones, labels_por_id, ids_catalogo):
    conteo = collections.Counter()
    unidades = collections.defaultdict(set)
    tos = collections.defaultdict(set)
    por_origen = collections.defaultdict(collections.Counter)
    for r in relaciones:
        sid = r["sujeto_id"]
        if not sid:
            continue
        conteo[sid] += 1
        unidades[sid].add(r["chunk_id"])
        tos[sid].add(r["to"])
        por_origen[sid][r["origen"]] += 1
    filas = []
    for sid, n in sorted(conteo.items(), key=lambda kv: (-kv[1], kv[0])):
        filas.append({
            "sujeto_id": sid,
            "label": labels_por_id.get(sid, ""),
            "n": n,
            "n_dev": por_origen[sid]["dev"],
            "n_esq2": por_origen[sid]["esq2"],
            "unidades": len(unidades[sid]),
            "n_tos": len(tos[sid]),
            "tos": sorted(tos[sid]),
            "en_catalogo": sid in ids_catalogo,
        })
    sin_uso = sorted(set(ids_catalogo) - set(conteo))
    return filas, sin_uso


def distribucion_propuestos_cruda(relaciones):
    conteo = collections.Counter()
    unidades = collections.defaultdict(set)
    for r in relaciones:
        sp = r["sujeto_propuesto"]
        if not sp:
            continue
        conteo[sp] += 1
        unidades[sp].add(r["chunk_id"])
    filas = [{"texto": t, "n": n, "unidades": len(unidades[t])}
             for t, n in sorted(conteo.items(), key=lambda kv: (-kv[1], kv[0]))]
    return filas


def agrupar_propuestos(relaciones, con_corte: bool):
    """Grupos por clave nominal. con_corte=True aplica el criterio sellado
    (solo tiene sentido en el universo primario)."""
    props = [r for r in relaciones if r["sujeto_propuesto"]]
    conteo = collections.Counter()
    unidades = collections.defaultdict(set)
    tos = collections.defaultdict(set)
    formas = collections.defaultdict(collections.Counter)
    padres = collections.defaultdict(collections.Counter)
    por_predicado = collections.defaultdict(collections.Counter)
    por_origen = collections.defaultdict(collections.Counter)
    por_corrida = collections.defaultdict(collections.Counter)
    ejemplos = collections.defaultdict(list)
    for r in props:
        clave = clave_grupo(r["sujeto_propuesto"])
        conteo[clave] += 1
        unidades[clave].add(r["chunk_id"])
        tos[clave].add(r["to"])
        formas[clave][r["sujeto_propuesto"]] += 1
        if r["padre_sugerido"]:
            padres[clave][r["padre_sugerido"]] += 1
        por_predicado[clave][r["predicate"]] += 1
        if "origen" in r:
            por_origen[clave][r["origen"]] += 1
        if "corrida" in r:
            por_corrida[clave][r["corrida"]] += 1
        ejemplos[clave].append({"chunk_id": r["chunk_id"], "texto": r["sujeto_propuesto"]})

    grupos = []
    for clave, n in sorted(conteo.items(), key=lambda kv: (-kv[1], kv[0])):
        n_unidades = len(unidades[clave])
        tos_grupo = sorted(tos[clave])
        n_tos = len(tos_grupo)
        tos_esq2 = [t for t in tos_grupo if t in ESQ2_TOS]
        # ejemplos: los tres primeros en orden de lectura, de unidades distintas
        # cuando es posible (asi el verbatim no repite la misma unidad).
        vistos = set()
        muestra = []
        for ej in ejemplos[clave]:
            if ej["chunk_id"] in vistos:
                continue
            vistos.add(ej["chunk_id"])
            muestra.append(ej)
            if len(muestra) == 3:
                break
        for ej in ejemplos[clave]:
            if len(muestra) == 3:
                break
            if ej not in muestra:
                muestra.append(ej)
        g = {
            "clave": clave,
            "etiqueta": formas[clave].most_common(1)[0][0],
            "n": n,
            "n_unidades": n_unidades,
            "n_tos": n_tos,
            "tos": tos_grupo,
            "n_tos_esq2": len(tos_esq2),
            "tos_esq2": tos_esq2,
            "formas_superficie": [f for f, _ in sorted(formas[clave].items(), key=lambda kv: (-kv[1], kv[0]))],
            "padres_sugeridos": [{"id": p, "n": c} for p, c in
                                 sorted(padres[clave].items(), key=lambda kv: (-kv[1], kv[0]))],
            "por_predicado": dict(sorted(por_predicado[clave].items())),
            "ejemplos": muestra,
        }
        if por_origen.get(clave):
            g["n_dev"] = por_origen[clave]["dev"]
            g["n_esq2"] = por_origen[clave]["esq2"]
        if por_corrida.get(clave):
            g["por_corrida"] = dict(sorted(por_corrida[clave].items()))
        if con_corte:
            pasa = (n_unidades >= MIN_UNIDADES and n_tos >= MIN_TOS
                    and len(tos_esq2) >= MIN_TOS_ESQ2)
            g["pasa_criterio"] = pasa
            if not pasa:
                motivo = []
                if n_unidades < MIN_UNIDADES:
                    motivo.append(f"unidades {n_unidades} < {MIN_UNIDADES}")
                if n_tos < MIN_TOS:
                    motivo.append(f"TOs {n_tos} < {MIN_TOS}")
                if len(tos_esq2) < MIN_TOS_ESQ2:
                    motivo.append(f"TOs ESQ-2 {len(tos_esq2)} < {MIN_TOS_ESQ2}")
                g["falla_por"] = "; ".join(motivo)
        grupos.append(g)
    return grupos, len(props)


# ---------------------------------------------------------------------------
# Selftest del agrupador (casos sinteticos + invariantes, patron R9)
# ---------------------------------------------------------------------------

CASOS_SELFTEST = [
    # (nombre, texto_a, texto_b, deben_agrupar_juntos)
    ("plural, articulo y flexion",
     "las empresas de seguros", "empresa de seguros", True),
    ("tildes y mayusculas",
     "Compañías de Seguros", "companias de seguros", True),
    ("modificador distinto separa",
     "empresas de seguros", "empresas emisoras de tarjetas", False),
    ("sinonimos NO se funden (limite declarado del agrupador)",
     "aseguradoras", "empresas de seguros", False),
    ("una sola palabra de contenido, flexion",
     "aseguradoras", "aseguradora", True),
    ("preposiciones y articulos salteados",
     "los proveedores de servicios de pago", "proveedores de servicios de pago", True),
    ("tercer modificador invisible para la clave (limite declarado)",
     "entidades aseguradoras", "entidades aseguradoras del exterior", True),
    ("misma cabeza generica, distinto modificador",
     "casas de cambio", "agencias de cambio", False),
]


def selftest() -> int:
    fallos = []
    for nombre, a, b, juntas in CASOS_SELFTEST:
        ka, kb = clave_grupo(a), clave_grupo(b)
        ok = (ka == kb) if juntas else (ka != kb)
        estado = "OK " if ok else "FALLA"
        print(f"[{estado}] {nombre}: {ka!r} vs {kb!r} (esperado {'juntos' if juntas else 'separados'})")
        if not ok:
            fallos.append(nombre)
    invariantes = [
        (normalizar("Compañías  de SEGUROS."), "companias de seguros"),
        (raiz("empresas"), raiz("empresa")),
        (clave_grupo("las entidades financieras"), "entidad+financier"),
        (clave_grupo("bancos del exterior"), clave_grupo("banco del exterior")),
        (clave_grupo(""), CLAVE_SIN_NUCLEO),
        (clave_grupo("de la de"), CLAVE_SIN_NUCLEO),
        (clave_grupo("las empresas de seguros"), clave_grupo("las empresas de seguros")),
    ]
    for i, (obtenido, esperado) in enumerate(invariantes, 1):
        ok = obtenido == esperado
        print(f"[{'OK ' if ok else 'FALLA'}] invariante {i}: {obtenido!r} == {esperado!r}")
        if not ok:
            fallos.append(f"invariante {i}")
    print()
    if fallos:
        print(f"SELFTEST EN ROJO — {len(fallos)} caso(s): {fallos}")
        return 1
    print(f"SELFTEST EN VERDE — {len(CASOS_SELFTEST)} casos + {len(invariantes)} invariantes")
    return 0


# ---------------------------------------------------------------------------
# Salida
# ---------------------------------------------------------------------------

CMD = "python3 data/experiment/esq/code/frecuencia_sujetos_suj_freq.py"


def _md_alias(alias):
    return ", ".join(alias) if alias else "—"


def render_md(res) -> str:
    inv = res["inventario_catalogo"]
    mp = res["universo_primario"]["meta"]
    tp = res["universo_primario"]["totales"]
    ml = res["lateral"]["meta"]
    L = []
    L.append("# U-SUJ-FREQ — Frecuencia de `sujeto_propuesto` (insumo de B5.4)")
    L.append("")
    L.append("Analisis de frecuencia para el catalogo de sujetos v3 (diseño")
    L.append("`docs/diseno_B5.4_catalogo_sujetos_v3.md` §0.2): que sujetos reales, hoy en")
    L.append("`sujeto_propuesto`, tienen evidencia medida para candidatearse a id del")
    L.append("catalogo. La lista final del catalogo es de la autora con B5.4: este")
    L.append("documento entrega la medicion y NO propone esa lista.")
    L.append("")
    L.append(f"Reproduce todos los numeros de este documento: `{CMD}`")
    L.append(f"Selftest del agrupador: `{CMD} --selftest`")
    L.append("Costo de API: USD 0 (el script no hace ninguna llamada LLM).")
    L.append("")

    L.append("## 0. Universo leido")
    L.append("")
    L.append("**Universo primario** (una extraccion por unidad, esquema de produccion):")
    L.append("")
    for origen, titulo, rutas in (
        ("dev", "dev / corpus_v2 (5 TOs: " + ", ".join(DEV_TOS) + ")",
         "`data/experiment/reextraccion_v2/corpus_v2/salida/<to>/extracciones_e1.jsonl`"),
        ("esq2", "ESQ-2 / cobertura (10 TOs: " + ", ".join(ESQ2_TOS) + ")",
         "`data/experiment/esq/cobertura/<to>/extracciones_e1_<to>.jsonl`"),
    ):
        c = mp["contadores"][origen]
        L.append(f"- **{titulo}** — {rutas}: {c['n_registros_leidos']} registros E1, "
                 f"**{c['n_unidades']} unidades** (duplicados supersedidos: "
                 f"{c['n_duplicados_supersedidos']}; con error: {c['n_con_error']}).")
    L.append("")
    L.append(f"- Regla de dedupe: {mp['regla_dedupe']}.")
    if mp["unidades_duplicadas_dev"]:
        L.append(f"- Unidades dev con reextraccion dirigida ({len(mp['unidades_duplicadas_dev'])}): "
                 + ", ".join(f"`{u}`" for u in mp["unidades_duplicadas_dev"]) + ".")
    L.append("- Capa leida: `validacion.relaciones` (la persistida por produccion). Control:")
    for origen in ("dev", "esq2"):
        c = mp["contadores"][origen]
        L.append(f"  - {origen}: relaciones `aplica_a`/`ejecuta` en `tool_input_crudo`: "
                 f"{c['n_rel_sujeto_crudo']} (la diferencia con la tabla de abajo son los "
                 f"rechazos del validador; no se juzga aca).")
    L.append("")
    L.append("**Tabla lateral** (descriptiva, SIN peso en el corte): "
             f"{ml['n_registros_por_corrida']['esq3b']} re-extracciones de ESQ-3b + "
             f"{ml['n_registros_por_corrida']['esq3b_v2']} de la vuelta 2, mismas unidades bajo "
             "esquema retocado; capa `tool_input_crudo` (no tienen `validacion`). No se mezcla "
             "con el primario en ninguna tabla de este documento.")
    L.append("")
    L.append("Los sha256 de todos los archivos de entrada estan en el JSON compañero")
    L.append("(`universo_primario.meta.archivos_sha256` y `lateral.meta.archivos_sha256`).")
    L.append("El script no escribe nada salvo sus dos propias salidas.")
    L.append("")

    L.append("## 1. Inventario EXACTO del catalogo vigente de sujetos")
    L.append("")
    L.append(f"Fuente: {inv['fuente']} — es el enum del tool schema de PRODUCCION, no la")
    L.append(f"prosa del prompt (la prosa instructiva, sin el bloque del catalogo interpolado,")
    L.append(f"nombra {inv['n_nombrados_en_prosa_instructiva']} ids: "
             + ", ".join(f"`{s}`" for s in inv["ids_nombrados_en_prosa_instructiva"])
             + f"; el enum tiene **{inv['n_ids']}**).")
    L.append("")
    L.append(f"- Version del catalogo: **{inv['version_catalogo']}** "
             f"(`data/experiment/grafo_v2/esquema_v2_clases.json`).")
    L.append(f"- Composicion: **{inv['n_clases']} clases + {inv['n_instancias']} instancias + "
             f"{inv['n_roles']} roles de alcance = {inv['n_ids']} ids**.")
    L.append(f"- El enum de `sujeto_propuesto_padre_sugerido` es identico al de `sujeto_id`: "
             f"{'si' if inv['enum_padre_sugerido_identico'] else 'NO'}.")
    L.append(f"- Definiciones: {inv['nota_definicion']}.")
    coh = inv["coherencia_enum_prompts_posteriores"]
    L.append("- Coherencia del enum con los prompts posteriores (informativa): "
             + "; ".join(f"{k}: {v}" for k, v in sorted(coh.items())) + ".")
    L.append("")
    L.append("| id | nivel | label | alias | padre |")
    L.append("|---|---|---|---|---|")
    for e in inv["ids"]:
        padre = e["padre"] or (f"rol del TO {e['to_del_rol']}" if e["to_del_rol"] else "—")
        L.append(f"| `{e['id']}` | {e['nivel']} | {e['label']} | {_md_alias(e['alias'])} | {padre} |")
    L.append("")

    L.append("## 2. Relaciones con sujeto del universo primario")
    L.append("")
    L.append(f"- Relaciones `aplica_a`/`ejecuta` (validadas): **{tp['n_rel_sujeto']}** "
             f"({', '.join(f'{k}: {v}' for k, v in tp['por_predicado'].items())}).")
    L.append(f"- Con `sujeto_id` del catalogo: **{tp['n_con_sujeto_id']}**. "
             f"Con `sujeto_propuesto`: **{tp['n_con_sujeto_propuesto']}**. "
             f"Con ambos (violacion de exclusion mutua): {tp['n_con_ambos']}. "
             f"Sin ninguno: {tp['n_sin_sujeto']}.")
    for origen, sub in tp.get("por_origen", {}).items():
        L.append(f"  - {origen}: {sub['n_rel_sujeto']} relaciones con sujeto — "
                 f"`sujeto_id` {sub['n_con_sujeto_id']}, `sujeto_propuesto` "
                 f"{sub['n_con_sujeto_propuesto']}.")
    L.append("")
    L.append("### 2.a Distribucion de `sujeto_id` (catalogo)")
    L.append("")
    L.append("| # | sujeto_id | n | dev | ESQ-2 | unidades | TOs |")
    L.append("|---:|---|---:|---:|---:|---:|---:|")
    for i, f in enumerate(res["distribucion_sujeto_id"], 1):
        L.append(f"| {i} | `{f['sujeto_id']}` | {f['n']} | {f['n_dev']} | {f['n_esq2']} | "
                 f"{f['unidades']} | {f['n_tos']} |")
    L.append("")
    L.append(f"Ids del catalogo SIN uso en el universo primario ({len(res['ids_sin_uso'])} de "
             f"{inv['n_ids']}): " + ", ".join(f"`{s}`" for s in res["ids_sin_uso"]) + ".")
    L.append("")
    L.append("### 2.b Distribucion cruda de `sujeto_propuesto` (los 25 textos mas frecuentes)")
    L.append("")
    L.append("| texto (libre, tal como se emitio) | n | unidades |")
    L.append("|---|---:|---:|")
    for f in res["distribucion_propuestos_cruda"][:25]:
        L.append(f"| {f['texto']} | {f['n']} | {f['unidades']} |")
    L.append("")
    L.append(f"Textos distintos: **{len(res['distribucion_propuestos_cruda'])}**; la lista")
    L.append("completa esta en el JSON compañero (`distribucion_propuestos_cruda`).")
    L.append("")

    L.append("## 3. Agrupacion mecanica de los `sujeto_propuesto`")
    L.append("")
    L.append("Regla del agrupador (sin LLM, todas las reglas visibles en el codigo; el")
    L.append("normalizador y el recorte de raiz son los de U-R9-FREQ, copiados sin cambios):")
    L.append("")
    L.append("1. Normalizacion: minusculas, sin diacriticos, solo letras, espacios colapsados.")
    L.append("2. Nucleo NOMINAL: las **dos primeras palabras de contenido** de la frase (los")
    L.append("   sujetos son frases nominales cuya cabeza suele ser generica — 'empresas',")
    L.append("   'entidades', 'proveedores' — y lo que distingue es el primer modificador).")
    L.append("   Palabras funcionales y marcadores se saltean por lista cerrada.")
    L.append("3. Cada palabra se reduce a raiz (enclitico + un sufijo + vocal tematica, raiz")
    L.append("   minima de 4). Clave del grupo: `raiz1+raiz2` (o `raiz1` si hay una sola).")
    L.append("4. **No hay tabla semantica de sinonimos**: sujetos sinonimos caen en grupos")
    L.append("   distintos y los grupos imperfectos quedan a la vista (columna de formas de")
    L.append("   superficie). Los conteos por grupo son **cota inferior** de la frecuencia del")
    L.append("   contenido.")
    L.append("")
    L.append(f"- `sujeto_propuesto` agrupados: **{res['total_propuestos']}**")
    L.append(f"- Grupos formados: **{res['n_grupos']}**")
    L.append(f"- Suma de los grupos: **{res['suma_grupos']}** "
             f"(consistente: {'si' if res['suma_grupos'] == res['total_propuestos'] else 'NO'})")
    L.append("")

    L.append("## 4. Criterio de corte aplicado")
    L.append("")
    L.append(f"Criterio **sellado en el mandato antes de mirar distribucion alguna** (no")
    L.append(f"calibrado): un grupo se candidatea a id del catalogo si aparece en")
    L.append(f"**>= {MIN_UNIDADES} unidades** Y en **>= {MIN_TOS} TOs**, de los cuales")
    L.append(f"**>= {MIN_TOS_ESQ2} son TOs de ESQ-2**. Pasan o no pasan; orden entre los que")
    L.append("pasan por conteo descendente. Sin techo: la lista final es de la autora con B5.4.")
    L.append("")
    pasan = [g for g in res["grupos"] if g["pasa_criterio"]]
    L.append(f"Grupos que pasan: **{len(pasan)}** de {res['n_grupos']}.")
    L.append("")
    L.append("### 4.a Grupos que PASAN")
    L.append("")
    if not pasan:
        L.append("(ninguno: ningun grupo de `sujeto_propuesto` alcanza el criterio sellado)")
        L.append("")
    L.append("| # | clave | etiqueta | n | dev | ESQ-2 | unidades | TOs | TOs ESQ-2 | padre sugerido mas frecuente |")
    L.append("|---:|---|---|---:|---:|---:|---:|---:|---:|---|")
    for i, g in enumerate(pasan, 1):
        padre_top = (f"`{g['padres_sugeridos'][0]['id']}` ({g['padres_sugeridos'][0]['n']})"
                     if g["padres_sugeridos"] else "—")
        L.append(f"| {i} | `{g['clave']}` | {g['etiqueta']} | {g['n']} | {g.get('n_dev', 0)} | "
                 f"{g.get('n_esq2', 0)} | **{g['n_unidades']}** | **{g['n_tos']}** | "
                 f"**{g['n_tos_esq2']}** | {padre_top} |")
    L.append("")
    for g in pasan:
        L.append(f"**`{g['clave']}`** — TOs: {', '.join(g['tos'])} (ESQ-2: {', '.join(g['tos_esq2'])})")
        L.append("")
        L.append(f"- Formas de superficie ({len(g['formas_superficie'])}): "
                 + "; ".join(f"\"{f}\"" for f in g["formas_superficie"][:6])
                 + (" …" if len(g["formas_superficie"]) > 6 else "") + ".")
        for ej in g["ejemplos"]:
            L.append(f"- `{ej['chunk_id']}` — \"{ej['texto']}\"")
        L.append("")

    no_pasan = [g for g in res["grupos"] if not g["pasa_criterio"]]
    L.append("### 4.b Grupos que NO pasan (los 30 mayores)")
    L.append("")
    L.append("| clave | etiqueta | n | unidades | TOs | TOs ESQ-2 | falla por |")
    L.append("|---|---|---:|---:|---:|---:|---|")
    for g in no_pasan[:30]:
        L.append(f"| `{g['clave']}` | {g['etiqueta']} | {g['n']} | {g['n_unidades']} | "
                 f"{g['n_tos']} | {g['n_tos_esq2']} | {g['falla_por']} |")
    L.append("")
    L.append(f"Los {len(no_pasan)} grupos que no pasan estan completos, con sus ejemplos")
    L.append("verbatim, sus TOs y sus padres sugeridos, en el JSON compañero, campo `grupos`.")
    L.append("")
    L.append("### 4.c Sensibilidad del umbral (informativa — NO se aplica)")
    L.append("")
    L.append("El criterio aplicado es el sellado. Esta tabla solo muestra cuan cerca del")
    L.append("borde quedo el resultado; no reemplaza ni recalibra el corte.")
    L.append("")
    L.append("| umbral unidades | umbral TOs | umbral TOs ESQ-2 | grupos que pasarian |")
    L.append("|---:|---:|---:|---|")
    for fila in res["sensibilidad_umbral"]:
        marca = " **(sellado)**" if fila["es_el_criterio_sellado"] else ""
        L.append(f"| {fila['min_unidades']}{marca} | {fila['min_tos']} | {fila['min_tos_esq2']} "
                 f"| {fila['n']}: {', '.join('`' + c + '`' for c in fila['claves']) or '(ninguno)'} |")
    L.append("")

    L.append("## 5. Tabla LATERAL — los mismos grupos sobre las 70 re-extracciones retocadas")
    L.append("")
    tl = res["lateral"]["totales"]
    L.append("Descriptiva y SIN peso en el corte: son las mismas unidades del primario,")
    L.append("re-extraidas bajo el prefijo retocado (ESQ-3b) y su vuelta 2 (v2). Pregunta que")
    L.append("responde: ¿los propuestos persisten bajo el prefijo retocado? Capa")
    L.append("`tool_input_crudo` (sin validacion), no comparable 1:1 con las tablas de arriba.")
    L.append("")
    L.append(f"- Relaciones `aplica_a`/`ejecuta`: {tl['n_rel_sujeto']} "
             f"({', '.join(f'{k}: {v}' for k, v in tl['por_predicado'].items())}); "
             f"con `sujeto_id`: {tl['n_con_sujeto_id']}; con `sujeto_propuesto`: "
             f"**{tl['n_con_sujeto_propuesto']}**; sin ninguno: {tl['n_sin_sujeto']}.")
    L.append("")
    L.append("| clave | etiqueta | n | 3b | v2 | unidades | TOs | ¿clave presente en el primario? |")
    L.append("|---|---|---:|---:|---:|---:|---:|---|")
    for g in res["lateral"]["grupos"]:
        pc = g.get("por_corrida", {})
        L.append(f"| `{g['clave']}` | {g['etiqueta']} | {g['n']} | {pc.get('esq3b', 0)} | "
                 f"{pc.get('esq3b_v2', 0)} | {g['n_unidades']} | {g['n_tos']} | {g['relacion_con_primario']} |")
    L.append("")

    L.append("## 6. Alcance")
    L.append("")
    L.append("Este documento entrega la medicion. **No propone ni decide** la lista final del")
    L.append("catalogo de sujetos: eso es de la autora con B5.4 (las dos variantes del diseño")
    L.append("la reciben como insumo comun).")
    L.append("")
    L.append("Limitaciones conocidas del agrupador, declaradas antes de leer la tabla:")
    L.append("")
    L.append("- Sin tabla de sinonimos: sujetos sinonimos ('aseguradoras' / 'empresas de")
    L.append("  seguros') quedan en grupos distintos — los conteos por grupo son cota inferior.")
    L.append("- La clave ve solo las dos primeras palabras de contenido: un tercer modificador")
    L.append("  ('… del exterior' en tercera posicion) no separa grupos. Las formas de")
    L.append("  superficie del JSON dejan esos matices a la vista.")
    L.append("- El recorte morfologico es de un solo sufijo con raiz minima de 4: pares")
    L.append("  morfologicamente lejanos no se funden. Se deja asi, no se fuerza.")
    return "\n".join(L) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--selftest", action="store_true", help="corre solo el selftest del agrupador")
    args = ap.parse_args()

    if args.selftest:
        return selftest()

    print("== selftest previo ==")
    if selftest() != 0:
        print("Selftest en rojo: no se generan salidas.")
        return 1
    print()

    inv = inventario_catalogo()
    labels_por_id = {e["id"]: e["label"] for e in inv["ids"]}
    ids_catalogo = [e["id"] for e in inv["ids"]]

    rel_prim, meta_prim = cargar_universo_primario()
    rel_lat, meta_lat = cargar_lateral()

    tot_prim = totales_canales(rel_prim, clave_origen="origen")
    dist_id, sin_uso = distribucion_sujeto_id(rel_prim, labels_por_id, ids_catalogo)
    dist_cruda = distribucion_propuestos_cruda(rel_prim)
    grupos, total_props = agrupar_propuestos(rel_prim, con_corte=True)

    tot_lat = totales_canales(rel_lat)
    grupos_lat, total_props_lat = agrupar_propuestos(rel_lat, con_corte=False)
    claves_prim = {g["clave"]: g["pasa_criterio"] for g in grupos}
    for g in grupos_lat:
        if g["clave"] in claves_prim:
            g["relacion_con_primario"] = ("si — PASA el corte" if claves_prim[g["clave"]]
                                          else "si — no pasa el corte")
        else:
            g["relacion_con_primario"] = "no (grupo nuevo del retocado)"

    sens = []
    for mu, mt, me in ((10, 3, 1), (15, 4, 2), (20, 4, 2), (MIN_UNIDADES, MIN_TOS, MIN_TOS_ESQ2),
                       (25, 5, 2), (20, 6, 3)):
        claves = [g["clave"] for g in grupos
                  if g["n_unidades"] >= mu and g["n_tos"] >= mt and g["n_tos_esq2"] >= me]
        sens.append({"min_unidades": mu, "min_tos": mt, "min_tos_esq2": me,
                     "n": len(claves), "claves": claves,
                     "es_el_criterio_sellado": (mu, mt, me) == (MIN_UNIDADES, MIN_TOS, MIN_TOS_ESQ2)})

    res = {
        "unidad": "U-SUJ-FREQ",
        "comando": CMD,
        "costo_api_usd": 0,
        "criterio_de_corte": {
            "min_unidades": MIN_UNIDADES,
            "min_tos": MIN_TOS,
            "min_tos_esq2": MIN_TOS_ESQ2,
            "sellado": "en el mandato de la unidad, antes de mirar distribucion alguna; no calibrado",
        },
        "tos_dev": list(DEV_TOS),
        "tos_esq2": list(ESQ2_TOS),
        "inventario_catalogo": inv,
        "universo_primario": {"meta": meta_prim, "totales": tot_prim},
        "distribucion_sujeto_id": dist_id,
        "ids_sin_uso": sin_uso,
        "distribucion_propuestos_cruda": dist_cruda,
        "total_propuestos": total_props,
        "n_grupos": len(grupos),
        "suma_grupos": sum(g["n"] for g in grupos),
        "grupos": grupos,
        "sensibilidad_umbral": sens,
        "lateral": {
            "meta": meta_lat,
            "totales": tot_lat,
            "total_propuestos": total_props_lat,
            "n_grupos": len(grupos_lat),
            "suma_grupos": sum(g["n"] for g in grupos_lat),
            "grupos": grupos_lat,
        },
    }

    assert res["suma_grupos"] == res["total_propuestos"], "suma de grupos != total de propuestos"
    assert res["lateral"]["suma_grupos"] == res["lateral"]["total_propuestos"], \
        "lateral: suma de grupos != total de propuestos"
    assert tot_prim["n_con_sujeto_id"] == sum(f["n"] for f in dist_id), \
        "distribucion de sujeto_id != total del canal"
    assert tot_prim["n_con_sujeto_propuesto"] == total_props, \
        "distribucion de propuestos != total del canal"

    with open(SALIDA_JSON, "w", encoding="utf-8") as fh:
        json.dump(res, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    with open(SALIDA_MD, "w", encoding="utf-8") as fh:
        fh.write(render_md(res))

    pasan = sum(1 for g in grupos if g["pasa_criterio"])
    print(f"Primario: rel sujeto {tot_prim['n_rel_sujeto']} | sujeto_id {tot_prim['n_con_sujeto_id']} | "
          f"propuestos {total_props} | grupos {len(grupos)} | pasan {pasan}")
    print(f"Lateral: rel sujeto {tot_lat['n_rel_sujeto']} | propuestos {total_props_lat} | "
          f"grupos {len(grupos_lat)}")
    print(f"Escrito: {os.path.relpath(SALIDA_JSON, RAIZ)}")
    print(f"Escrito: {os.path.relpath(SALIDA_MD, RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
