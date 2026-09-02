#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""U-R9-FREQ — Analisis de frecuencia del subtipo de Obligacion (retoque R9).

Lee, en modo SOLO LECTURA, las 762 extracciones persistidas de
data/experiment/esq/cobertura/*/extracciones_e1_*.jsonl y produce:

  1. La distribucion completa de properties.tipo sobre TODAS las entidades
     Obligacion (conteo, % sobre el total de Obligacion, TOs en los que
     aparece), mas la verificacion del 76 % de "otra" medido en la lectura
     de U-ESQ-2 sobre el subconjunto de las 75 fichas.
  2. Una agrupacion MECANICA (sin LLM) de las Obligacion con tipo="otra" por
     el nucleo de su descripcion, con etiqueta, conteo, unidades, TOs
     distintos y tres descripciones verbatim de ejemplo por grupo.
  3. La aplicacion del criterio de corte sellado ANTES de mirar la
     distribucion: un grupo merece valor propio si aparece en >= 15 unidades
     y en >= 4 de los 10 TOs.

Costo de API: USD 0 — el script no hace ninguna llamada LLM.

Reproduccion:
    python3 data/experiment/esq/code/frecuencia_subtipos_r9.py
    python3 data/experiment/esq/code/frecuencia_subtipos_r9.py --selftest

Salidas (unicos archivos que el script escribe):
    data/experiment/esq/cobertura/frecuencia_subtipos_r9.json
    data/experiment/esq/cobertura/frecuencia_subtipos_r9.md

El script NO escribe ni modifica ningun otro archivo de cobertura/, ni la db,
ni el worksheet de fichas.
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
PATRON_EXTRACCIONES = os.path.join(DIR_COBERTURA, "*", "extracciones_e1_*.jsonl")
WORKSHEET_FICHAS = os.path.join(DIR_COBERTURA, "fichas", "worksheet_fichas_esq2.json")
SALIDA_JSON = os.path.join(DIR_COBERTURA, "frecuencia_subtipos_r9.json")
SALIDA_MD = os.path.join(DIR_COBERTURA, "frecuencia_subtipos_r9.md")

# ---------------------------------------------------------------------------
# Criterio de corte — SELLADO en el mandato de la unidad, ANTES de mirar
# distribucion alguna. No calibrado: su virtud es ser anterior y auditable.
# ---------------------------------------------------------------------------

MIN_UNIDADES = 15
MIN_TOS = 4

# Enum vigente de Obligacion.properties.tipo
# (data/experiment/reextraccion_v2/e1_extractor/prompt_e1.py:77)
ENUM_VIGENTE = [
    "presentacion_informativa",
    "calculo",
    "asignacion",
    "comunicacion_a_cliente",
    "otra",
]

# ---------------------------------------------------------------------------
# Agrupador mecanico — todas las reglas son visibles aca. Sin LLM.
#
# Idea: la descripcion de una Obligacion es prosa normativa. El NUCLEO de la
# descripcion es la primera palabra de contenido que sigue al primer marcador
# deontico/copulativo ("deberan", "podra", "sera", ...); si la descripcion no
# tiene marcador, el nucleo es su primera palabra de contenido. El nucleo se
# reduce a una RAIZ con un recorte morfologico de sufijos (lista visible), y
# los grupos se forman por raiz. Las raices se dejan como salen: no hay tabla
# semantica de sinonimos, asi que los grupos imperfectos quedan a la vista.
# ---------------------------------------------------------------------------

# Palabras funcionales: articulos, preposiciones, pronombres, conjunciones,
# cuantificadores, demostrativos y los auxiliares de la pasiva perifrastica.
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

# Marcadores deonticos y copulativos: introducen el predicado de la obligacion.
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

# Encliticos pronominales: se recortan antes del sufijo ("observarse" -> "observar").
ENCLITICOS = ("arse", "erse", "irse", "arlo", "arla", "arle", "arles")

# Formas finitas de futuro y condicional. En castellano llevan tilde obligatoria,
# asi que el patron se prueba sobre el token CON tildes: eso lo separa de los
# sustantivos en -era / -ara ("manera", "cartera", "financiera"), que no la llevan.
# Sirve para el prescriptivo sin modal ("La entidad presentara el regimen ...").
SUFIJOS_FUTURO_CONDICIONAL = (
    "ará", "arán", "erá", "erán", "irá", "irán",
    "aría", "arían", "ería", "erían", "iría", "irían",
)

# Sufijos flexivos y derivativos, en orden de aplicacion (mas largo primero).
# Se recorta UNO solo, y solo si la raiz resultante conserva >= LONG_MIN_RAIZ
# caracteres.
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


def normalizar_con_tildes(texto: str) -> str:
    """Igual que normalizar() pero conserva las tildes (las necesita el patron
    de futuro/condicional)."""
    return re.sub(r"[^a-záéíóúüñ]+", " ", (texto or "").lower()).strip()


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


def nucleo(descripcion: str):
    """Nucleo de la descripcion, en este orden de prioridad:

    1. La primera palabra de contenido posterior al primer marcador deontico o
       copulativo ("deberan presentar" -> "presentar").
    2. Si no hay marcador: la primera forma finita de futuro/condicional, que es
       el otro modo prescriptivo del corpus ("la entidad presentara" -> "presentara").
    3. Si tampoco la hay: la primera palabra de contenido de la descripcion (cubre
       tanto el infinitivo inicial, "Reforzar las capacidades ...", como los
       fragmentos nominales sin verbo).

    Devuelve None si la descripcion no tiene ninguna palabra de contenido.
    """
    con_tildes = normalizar_con_tildes(descripcion).split()
    tokens = [normalizar(t) for t in con_tildes]
    pares = [(t, ct) for t, ct in zip(tokens, con_tildes) if len(t) >= LONG_MIN_TOKEN]

    for i, (t, _ct) in enumerate(pares):
        if t in MARCADORES_DEONTICOS:
            for t2, _ct2 in pares[i + 1:]:
                if t2 in PALABRAS_FUNCIONALES or t2 in MARCADORES_DEONTICOS:
                    continue
                return t2
            break

    for t, ct in pares:
        if t in PALABRAS_FUNCIONALES or t in MARCADORES_DEONTICOS:
            continue
        if ct.endswith(SUFIJOS_FUTURO_CONDICIONAL):
            return t

    for t, _ct in pares:
        if t in PALABRAS_FUNCIONALES or t in MARCADORES_DEONTICOS:
            continue
        return t
    return None


def clave_grupo(descripcion: str) -> str:
    t = nucleo(descripcion)
    return raiz(t) if t else CLAVE_SIN_NUCLEO


def etiqueta_grupo(clave: str, formas: collections.Counter, continuaciones: collections.Counter) -> str:
    """Etiqueta descriptiva derivada mecanicamente del propio grupo.

    forma de superficie mas frecuente + continuacion de dos tokens mas frecuente.
    """
    if clave == CLAVE_SIN_NUCLEO:
        return "(descripcion sin palabra de contenido)"
    forma = formas.most_common(1)[0][0]
    cont = continuaciones.most_common(1)[0][0] if continuaciones else ""
    return f"{forma} {cont}".strip()


# ---------------------------------------------------------------------------
# Lectura (solo lectura)
# ---------------------------------------------------------------------------

def sha256(ruta: str) -> str:
    h = hashlib.sha256()
    with open(ruta, "rb") as fh:
        for bloque in iter(lambda: fh.read(1 << 16), b""):
            h.update(bloque)
    return h.hexdigest()


def cargar_obligaciones():
    """Devuelve (obligaciones, meta). Cada obligacion: dict con to, chunk_id, tipo, descripcion."""
    archivos = sorted(glob.glob(PATRON_EXTRACCIONES))
    if not archivos:
        raise SystemExit(f"No hay extracciones bajo {PATRON_EXTRACCIONES}")
    obligaciones = []
    n_lineas = 0
    n_errores = 0
    crudo = 0
    for ruta in archivos:
        with open(ruta, encoding="utf-8") as fh:
            for linea in fh:
                linea = linea.strip()
                if not linea:
                    continue
                n_lineas += 1
                d = json.loads(linea)
                if d.get("error"):
                    n_errores += 1
                chunk_id = d["chunk_id"]
                to = chunk_id.split("::")[0]
                crudo += sum(
                    1 for e in (d.get("tool_input_crudo") or {}).get("entities", [])
                    if e.get("type") == "Obligacion"
                )
                for e in (d.get("validacion") or {}).get("entidades", []):
                    if e.get("type") != "Obligacion":
                        continue
                    props = e.get("properties") or {}
                    obligaciones.append({
                        "to": to,
                        "chunk_id": chunk_id,
                        "unidad": d.get("unidad"),
                        "local_id": e.get("local_id"),
                        "label": e.get("label"),
                        "tipo": props.get("tipo"),
                        "descripcion": props.get("descripcion") or "",
                    })
    meta = {
        "archivos": [os.path.relpath(r, RAIZ) for r in archivos],
        "sha256_archivos": {os.path.relpath(r, RAIZ): sha256(r) for r in archivos},
        "n_extracciones": n_lineas,
        "n_extracciones_con_error": n_errores,
        "n_obligaciones_validacion": len(obligaciones),
        "n_obligaciones_tool_input_crudo": crudo,
        "coinciden_crudo_y_validacion": crudo == len(obligaciones),
    }
    return obligaciones, meta


def chunks_de_fichas():
    """chunk_ids de las 75 fichas leidas en U-ESQ-2 (solo lectura del worksheet)."""
    if not os.path.exists(WORKSHEET_FICHAS):
        return None
    with open(WORKSHEET_FICHAS, encoding="utf-8") as fh:
        d = json.load(fh)
    return {f["chunk_id"] for f in d.get("fichas", [])}


# ---------------------------------------------------------------------------
# Analisis
# ---------------------------------------------------------------------------

def distribucion_tipo(obligaciones):
    conteo = collections.Counter()
    tos = collections.defaultdict(set)
    unidades = collections.defaultdict(set)
    for o in obligaciones:
        t = o["tipo"] if o["tipo"] is not None else "(sin propiedad tipo)"
        conteo[t] += 1
        tos[t].add(o["to"])
        unidades[t].add(o["chunk_id"])
    total = sum(conteo.values())
    filas = []
    for valor, n in conteo.most_common():
        filas.append({
            "valor": valor,
            "n": n,
            "pct_sobre_obligacion": round(100.0 * n / total, 1) if total else 0.0,
            "unidades": len(unidades[valor]),
            "tos": sorted(tos[valor]),
            "n_tos": len(tos[valor]),
            "en_enum_vigente": valor in ENUM_VIGENTE,
        })
    return filas, total


def agrupar_otras(obligaciones):
    otras = [o for o in obligaciones if o["tipo"] == "otra"]
    conteo = collections.Counter()
    formas = collections.defaultdict(collections.Counter)
    continuaciones = collections.defaultdict(collections.Counter)
    tos = collections.defaultdict(set)
    unidades = collections.defaultdict(set)
    ejemplos = collections.defaultdict(list)
    for o in otras:
        desc = o["descripcion"]
        tok = nucleo(desc)
        clave = raiz(tok) if tok else CLAVE_SIN_NUCLEO
        conteo[clave] += 1
        if tok:
            formas[clave][tok] += 1
            tokens = normalizar(desc).split()
            if tok in tokens:
                i = tokens.index(tok)
                cont = " ".join(tokens[i + 1:i + 3])
                if cont:
                    continuaciones[clave][cont] += 1
        tos[clave].add(o["to"])
        unidades[clave].add(o["chunk_id"])
        ejemplos[clave].append({"chunk_id": o["chunk_id"], "descripcion": desc})
    grupos = []
    for clave, n in sorted(conteo.items(), key=lambda kv: (-kv[1], kv[0])):
        n_unidades = len(unidades[clave])
        n_tos = len(tos[clave])
        pasa = n_unidades >= MIN_UNIDADES and n_tos >= MIN_TOS
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
        grupos.append({
            "clave_raiz": clave,
            "etiqueta": etiqueta_grupo(clave, formas[clave], continuaciones[clave]),
            "n_obligaciones": n,
            "n_unidades": n_unidades,
            "n_tos": n_tos,
            "tos": sorted(tos[clave]),
            "formas_superficie": [f for f, _ in formas[clave].most_common()],
            "pasa_criterio": pasa,
            "ejemplos": muestra,
        })
    return grupos, len(otras)


# ---------------------------------------------------------------------------
# Selftest del agrupador
# ---------------------------------------------------------------------------

CASOS_SELFTEST = [
    # (nombre, descripcion_a, descripcion_b, deben_agrupar_juntas)
    ("mismo verbo, distinta flexion",
     "Las entidades deberán presentar el régimen informativo correspondiente.",
     "La entidad presentará la información dentro del plazo previsto.", True),
    ("verbo y su nominalizacion caen juntos",
     "Las entidades deberán notificar al cliente la modificación.",
     "Notificación al cliente de la modificación de comisiones.", True),
    ("dos verbos sinonimos NO se funden (limite declarado del agrupador)",
     "Las entidades deberán presentar el régimen informativo.",
     "Las entidades deberán remitir el régimen informativo.", False),
    ("mismo verbo con enclitico",
     "Los registros deberán conservarse por diez años.",
     "Las entidades deberán conservar los registros por diez años.", True),
    ("verbos distintos no se agrupan",
     "Las entidades deberán presentar el régimen informativo.",
     "Las entidades deberán conservar la documentación respaldatoria.", False),
    ("nucleo nominal cuando no hay verbo de contenido",
     "Líneas de crédito del exterior recibidas para la liquidación.",
     "Líneas de crédito otorgadas por bancos del exterior.", True),
    ("marcador deontico salteado, no se agrupa por el sujeto",
     "Las entidades deberán presentar el régimen informativo.",
     "Las entidades deberán conservar la documentación.", False),
]


def selftest() -> int:
    fallos = []
    for nombre, a, b, juntas in CASOS_SELFTEST:
        ka, kb = clave_grupo(a), clave_grupo(b)
        ok = (ka == kb) if juntas else (ka != kb)
        estado = "OK " if ok else "FALLA"
        print(f"[{estado}] {nombre}: {ka!r} vs {kb!r} (esperado {'juntas' if juntas else 'separadas'})")
        if not ok:
            fallos.append(nombre)
    # invariantes del normalizador
    invariantes = [
        (normalizar("Deberán  PRESENTAR, según el punto 3.2."), "deberan presentar segun el punto"),
        (raiz("presentacion"), raiz("presentar")),
        (raiz("conservarse"), raiz("conservar")),
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

CMD = "python3 data/experiment/esq/code/frecuencia_subtipos_r9.py"


def render_md(res) -> str:
    m = res["meta"]
    L = []
    L.append("# U-R9-FREQ — Frecuencia del subtipo de Obligacion")
    L.append("")
    L.append("Analisis de frecuencia para el retoque R9 del laudo ESQ-3a: que valores")
    L.append("merecen entrar al enum de `Obligacion.properties.tipo`")
    L.append("(`data/experiment/reextraccion_v2/e1_extractor/prompt_e1.py:77`).")
    L.append("")
    L.append(f"Reproduce todos los numeros de este documento: `{CMD}`")
    L.append(f"Selftest del agrupador: `{CMD} --selftest`")
    L.append("Costo de API: USD 0 (el script no hace ninguna llamada LLM).")
    L.append("")
    L.append("## 0. Base de datos leida")
    L.append("")
    L.append(f"- Archivos: {len(m['archivos'])} (`data/experiment/esq/cobertura/*/extracciones_e1_*.jsonl`)")
    L.append(f"- Extracciones: **{m['n_extracciones']}** (con error: {m['n_extracciones_con_error']})")
    L.append(f"- Entidades `Obligacion`: **{m['n_obligaciones_validacion']}** en `validacion.entidades`")
    L.append(f"- Control: `tool_input_crudo.entities` da {m['n_obligaciones_tool_input_crudo']} — "
             f"coinciden: {'si' if m['coinciden_crudo_y_validacion'] else 'NO'}")
    L.append("")
    L.append("Los sha256 de los diez archivos de entrada estan en el JSON companero, campo")
    L.append("`meta.sha256_archivos`. El script no escribe nada bajo `cobertura/` salvo sus")
    L.append("dos propias salidas.")
    L.append("")

    L.append("## 1. Distribucion de `Obligacion.properties.tipo` (las 977)")
    L.append("")
    L.append("| valor | n | % de Obligacion | unidades | TOs | en enum vigente |")
    L.append("|---|---:|---:|---:|---:|---|")
    for f in res["distribucion_tipo"]:
        L.append(f"| `{f['valor']}` | {f['n']} | {f['pct_sobre_obligacion']} % | {f['unidades']} | "
                 f"{f['n_tos']} | {'si' if f['en_enum_vigente'] else '**NO**'} |")
    L.append(f"| **total** | **{res['total_obligaciones']}** | 100 % | | | |")
    L.append("")
    for f in res["distribucion_tipo"]:
        if not f["en_enum_vigente"]:
            L.append(f"- Valor fuera del enum vigente: `{f['valor']}` ({f['n']}), TOs {f['tos']}.")
    L.append("")

    v = res["verificacion_76_pct"]
    L.append("### 1.b Verificacion del 76 % de `otra` medido en la lectura")
    L.append("")
    if v.get("disponible"):
        L.append(f"- Sobre las **{v['n_fichas']} fichas** leidas en U-ESQ-2: "
                 f"`otra` en **{v['n_otra']} de {v['n_obligaciones']}** = **{v['pct']} %**.")
        L.append(f"- Sobre el corpus completo de {res['total_obligaciones']} `Obligacion`: "
                 f"**{res['pct_otra_corpus']} %**.")
        L.append("")
        L.append("El 76,4 % es el numero de la lectura y se reproduce exactamente sobre el")
        L.append("subconjunto de las fichas; la cifra del corpus completo es mas baja. La")
        L.append("nota contemporanea que registra ese 76,4 % (68/89) esta en la observacion")
        L.append("de la **ficha 12** del worksheet, y la **ficha 17** la vuelve a citar; el")
        L.append("mandato de esta unidad la atribuye a la ficha 39, cuya observacion trata")
        L.append("otro asunto. Se reporta la discrepancia sin resolverla: manda el archivo.")
    else:
        L.append("- Worksheet de fichas no disponible; verificacion no realizada.")
    L.append("")

    L.append("## 2. Agrupacion mecanica de las `otra`")
    L.append("")
    L.append("Regla del agrupador (sin LLM, todas las reglas visibles en el codigo):")
    L.append("")
    L.append("1. Normalizacion: minusculas, sin diacriticos, solo letras, espacios colapsados.")
    L.append("2. Nucleo, en este orden: (i) primera palabra de contenido **posterior al primer")
    L.append("   marcador deontico o copulativo** (`deberan`, `podra`, `sera`, `queda`, ...);")
    L.append("   (ii) si no hay marcador, la primera forma finita de **futuro o condicional**")
    L.append("   —se prueba sobre el token con tildes, que es lo que la separa de sustantivos")
    L.append("   en -era/-ara—; (iii) si tampoco la hay, la primera palabra de contenido. Las")
    L.append("   palabras funcionales (articulos, preposiciones, pronombres, conjunciones,")
    L.append("   demostrativos, auxiliares de pasiva) se saltean por lista cerrada.")
    L.append("3. Raiz = nucleo menos enclitico pronominal, menos **un** sufijo de la lista")
    L.append("   ordenada, menos vocal tematica final; con raiz minima de 4 caracteres.")
    L.append("4. Un grupo = una raiz. **No hay tabla semantica de sinonimos**: verbos distintos")
    L.append("   con el mismo sentido caen en grupos distintos, y los grupos imperfectos quedan")
    L.append("   a la vista (columna `formas de superficie`).")
    L.append("")
    L.append(f"- `otra` agrupadas: **{res['total_otra']}**")
    L.append(f"- Grupos formados: **{res['n_grupos']}**")
    L.append(f"- Suma de los grupos: **{res['suma_grupos']}** "
             f"(consistente: {'si' if res['suma_grupos'] == res['total_otra'] else 'NO'})")
    L.append("")

    L.append("## 3. Criterio de corte aplicado")
    L.append("")
    L.append(f"Criterio **sellado en el mandato antes de mirar distribucion alguna** (no")
    L.append(f"calibrado): un grupo merece valor propio si aparece en **>= {MIN_UNIDADES} unidades**")
    L.append(f"y en **>= {MIN_TOS} de los 10 TOs**. Orden entre los que pasan: conteo descendente.")
    L.append("")
    pasan = [g for g in res["grupos"] if g["pasa_criterio"]]
    L.append(f"Grupos que pasan: **{len(pasan)}** de {res['n_grupos']}.")
    L.append("")
    L.append("### 3.a Grupos que PASAN")
    L.append("")
    L.append("| # | raiz | etiqueta | n | unidades | TOs | formas de superficie |")
    L.append("|---:|---|---|---:|---:|---:|---|")
    for i, g in enumerate(pasan, 1):
        L.append(f"| {i} | `{g['clave_raiz']}` | {g['etiqueta']} | {g['n_obligaciones']} | "
                 f"**{g['n_unidades']}** | **{g['n_tos']}** | {', '.join(g['formas_superficie'][:8])} |")
    L.append("")
    for g in pasan:
        L.append(f"**`{g['clave_raiz']}`** — TOs: {', '.join(g['tos'])}")
        L.append("")
        for ej in g["ejemplos"]:
            L.append(f"- `{ej['chunk_id']}` — \"{ej['descripcion']}\"")
        L.append("")

    L.append("### 3.b Grupos que NO pasan (los 30 mayores)")
    L.append("")
    L.append("| raiz | etiqueta | n | unidades | TOs | falla por |")
    L.append("|---|---|---:|---:|---:|---|")
    no_pasan = [g for g in res["grupos"] if not g["pasa_criterio"]]
    for g in no_pasan[:30]:
        motivo = []
        if g["n_unidades"] < MIN_UNIDADES:
            motivo.append(f"unidades {g['n_unidades']} < {MIN_UNIDADES}")
        if g["n_tos"] < MIN_TOS:
            motivo.append(f"TOs {g['n_tos']} < {MIN_TOS}")
        L.append(f"| `{g['clave_raiz']}` | {g['etiqueta']} | {g['n_obligaciones']} | "
                 f"{g['n_unidades']} | {g['n_tos']} | {'; '.join(motivo)} |")
    L.append("")
    L.append(f"Los {len(no_pasan)} grupos que no pasan estan completos, con sus ejemplos")
    L.append("verbatim y sus TOs, en `frecuencia_subtipos_r9.json`, campo `grupos`.")
    L.append("")
    L.append("### 3.c Sensibilidad del umbral (informativa — NO se aplica)")
    L.append("")
    L.append("El criterio aplicado es el sellado. Esta tabla solo muestra cuan cerca del")
    L.append("borde quedo el resultado; no reemplaza ni recalibra el corte.")
    L.append("")
    L.append("| umbral unidades | umbral TOs | grupos que pasarian |")
    L.append("|---:|---:|---|")
    for fila in res["sensibilidad_umbral"]:
        L.append(f"| {fila['min_unidades']}{' **(sellado)**' if fila['es_el_criterio_sellado'] else ''} "
                 f"| {fila['min_tos']} | {fila['n']}: "
                 f"{', '.join('`' + c + '`' for c in fila['claves']) or '(ninguno)'} |")
    L.append("")
    L.append("## 4. Alcance")
    L.append("")
    L.append("Este documento entrega la medicion. **No propone ni decide** la lista final de")
    L.append("valores del enum: el laudo ESQ-3a fija el maximo en 3 valores adicionales sobre")
    L.append("`reporte_al_supervisor`, ya anclado, y la seleccion es de la autora con la mesa.")
    L.append("")
    L.append("Limitaciones conocidas del agrupador, declaradas antes de leer la tabla:")
    L.append("")
    L.append("- Sin tabla de sinonimos: raices semanticamente vecinas quedan separadas, de modo")
    L.append("  que los conteos por grupo son **cota inferior** de la frecuencia del contenido.")
    L.append("- El nucleo se toma tras el **primer** marcador deontico: en una descripcion cuya")
    L.append("  primera copula pertenece a una relativa del sujeto, el nucleo cae en el sujeto y")
    L.append("  no en el predicado. Esos casos forman grupos nominales visibles.")
    L.append("- El recorte morfologico es de un solo sufijo con raiz minima de 4: pares como")
    L.append("  `pago` / `pagar` no se funden. Se deja asi, no se fuerza.")
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

    obligaciones, meta = cargar_obligaciones()
    filas, total = distribucion_tipo(obligaciones)
    grupos, total_otra = agrupar_otras(obligaciones)

    fichas = chunks_de_fichas()
    if fichas:
        obl_f = [o for o in obligaciones if o["chunk_id"] in fichas]
        n_otra_f = sum(1 for o in obl_f if o["tipo"] == "otra")
        verif = {
            "disponible": True,
            "n_fichas": len(fichas),
            "n_obligaciones": len(obl_f),
            "n_otra": n_otra_f,
            "pct": round(100.0 * n_otra_f / len(obl_f), 1) if obl_f else 0.0,
        }
    else:
        verif = {"disponible": False}

    n_otra_corpus = sum(1 for o in obligaciones if o["tipo"] == "otra")
    res = {
        "unidad": "U-R9-FREQ",
        "comando": CMD,
        "costo_api_usd": 0,
        "criterio_de_corte": {
            "min_unidades": MIN_UNIDADES,
            "min_tos": MIN_TOS,
            "sellado": "en el mandato de la unidad, antes de mirar distribucion alguna; no calibrado",
        },
        "enum_vigente": ENUM_VIGENTE,
        "meta": meta,
        "total_obligaciones": total,
        "distribucion_tipo": filas,
        "pct_otra_corpus": round(100.0 * n_otra_corpus / total, 1) if total else 0.0,
        "verificacion_76_pct": verif,
        "total_otra": total_otra,
        "n_grupos": len(grupos),
        "suma_grupos": sum(g["n_obligaciones"] for g in grupos),
        "grupos": grupos,
    }

    sens = []
    for mu, mt in ((10, 3), (10, 4), (15, 3), (MIN_UNIDADES, MIN_TOS), (20, 4), (15, 5)):
        claves = [g["clave_raiz"] for g in grupos if g["n_unidades"] >= mu and g["n_tos"] >= mt]
        sens.append({"min_unidades": mu, "min_tos": mt, "n": len(claves), "claves": claves,
                     "es_el_criterio_sellado": (mu, mt) == (MIN_UNIDADES, MIN_TOS)})
    res["sensibilidad_umbral"] = sens

    assert res["suma_grupos"] == res["total_otra"], "suma de grupos != total de 'otra'"
    assert sum(f["n"] for f in filas) == total, "suma de la distribucion != total de Obligacion"

    with open(SALIDA_JSON, "w", encoding="utf-8") as fh:
        json.dump(res, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    with open(SALIDA_MD, "w", encoding="utf-8") as fh:
        fh.write(render_md(res))

    print(f"Obligacion: {total} | 'otra': {total_otra} ({res['pct_otra_corpus']} %) | "
          f"grupos: {len(grupos)} | pasan criterio: {sum(1 for g in grupos if g['pasa_criterio'])}")
    print(f"Escrito: {os.path.relpath(SALIDA_JSON, RAIZ)}")
    print(f"Escrito: {os.path.relpath(SALIDA_MD, RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
