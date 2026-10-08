"""U-UNION-ESTRECHA, U1: la regla estrecha de unión ítem–encabezado (texto en regla_u1.md), como funciones puras.

Sin E/S: `premedicion_u1.py` la aplica sobre lo guardado y `selftest_regla_u1.py` la prueba rama por rama.
Implementación de referencia, leída como código: la regla E de U-DIAG-CAP3-GRAFO
(`reports/u_diag_cap3_grafo/scripts/udiag_a_union.py`, `mini_de_bloque` y `medir`). Cambia respecto de ella:
solo la Condicion, el anuncio del bloque que abre la lista, el rango completo de `condicion_de` para contar
candidatos y la compatibilidad del destino con el anuncio.
"""
import collections
import re
import unicodedata

ROL_FUENTE = "union_item_encabezado"
PREDICADO = "condicion_de"
TIPO_ITEM = "Condicion"

# Regla, punto 2: expresiones de anuncio (lista cerrada; cada una con su fuente en regla_u1.md, sección 2).
# Se buscan sin diacríticos y en minúsculas.
SUBORDINANTES = ("siempre que", "en la medida que", "cuando", "cada vez que", "toda vez que")
NOMBRES_CON_SUBORDINANTE = ("condiciones", "requisitos", "recaudos", "situaciones", "circunstancias", "motivos")
NOMBRES_SIN_SUBORDINANTE = ("condiciones", "requisitos", "recaudos")
FRASES_SIN_SUBORDINANTE = ("las condiciones especificadas a continuacion", "las condiciones estipuladas en cada caso")
# Regla, punto 4: marcas de excepción en la oración final (lista cerrada, regla_u1.md, sección 4).
MARCAS_EXCEPCION = ("excepto", "salvo", "a menos que", "con excepcion de", "no resultara aplicable",
                    "no sera aplicable", "no sera de aplicacion", "se exceptua", "quedan exceptuad",
                    "quedaran exceptuad")
# Regla, punto 3: el rango de condicion_de en la matriz r2 (modelos_r2.FIRMAS_R2) cuenta para «único candidato».
RANGO_CONDICION_DE = ("Excepcion", "Obligacion", "Restriccion", "Operacion", "Potestad")
# Regla, punto 4: tipos destino compatibles con cada forma de anuncio. Restriccion no es compatible con ninguna.
COMPATIBLES = {
    "S": ("Potestad", "Operacion", "Obligacion", "Excepcion"),
    "N": ("Potestad", "Operacion", "Excepcion"),
    "EXC": ("Excepcion",),
}
RESULTADOS = ("union", "sin_unidad_de_encabezado", "sin_anuncio", "sin_candidato", "ambigua",
              "destino_no_compatible")

_ALT = lambda xs: "|".join(re.escape(x) for x in xs)  # noqa: E731
RE_SUBORDINANTE = re.compile(r"\b(?:%s)\b" % _ALT(SUBORDINANTES))
RE_NOMBRE_S = re.compile(r"\b(?:las|los) siguientes (?:%s)$" % _ALT(NOMBRES_CON_SUBORDINANTE))
RE_NOMBRE_N = re.compile(r"\b(?:las|los) siguientes (?:%s)$" % _ALT(NOMBRES_SIN_SUBORDINANTE))
RE_FRASE_N = re.compile(r"\b(?:%s)$" % _ALT(FRASES_SIN_SUBORDINANTE))
RE_EXCEPCION = re.compile(r"\b(?:%s)" % _ALT(MARCAS_EXCEPCION))
# Frontera de oración: «.», «;» o «:» seguidos de espacio y de mayúscula (o de comilla, paréntesis o «¿»),
# salvo detrás de las abreviaturas que preceden a un número o a una letra de comunicación.
FRONTERA = re.compile(r"(?<![Cc]om)(?<![Aa]rt)(?<![Ii]nc)(?<![Pp]to)(?<![Nn]ro)[.;:]\s+(?=[A-ZÁÉÍÓÚÑ¿“«\"(])")


def sin_diacriticos(s):
    return "".join(ch for ch in unicodedata.normalize("NFD", s) if unicodedata.category(ch) != "Mn")


def limpiar(texto):
    """Une las palabras cortadas en fin de línea y colapsa el espacio (como `norm` de la referencia, sin bajar
    a minúsculas ni quitar comillas, para no perder la frontera de oración)."""
    t = re.sub(r"-\s*\n\s*", "", texto or "")
    return re.sub(r"\s+", " ", t).strip()


def norm(s):
    """La de la referencia (`udiag_comun.norm`): para ubicar el mini-chunk del bloque."""
    s = re.sub(r"-\s*\n\s*", "", s or "")
    s = re.sub("[“”«»‘’'\"]", "", s)
    s = re.sub("[–—]", "-", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def oracion_final(texto):
    """La oración que termina en el «:» que abre la lista, sin ese «:»."""
    t = limpiar(texto)
    if not t.endswith((":", "：")):
        raise ValueError("el bloque que abre la lista no termina en «:»: " + t[-60:])
    return FRONTERA.split(t[:-1].rstrip())[-1].strip()


def anuncio(texto):
    """Regla, puntos 2 y 4: forma del anuncio del bloque (S, N o None) y marca de excepción.

    F: la oración final. G: el tramo de F después de su última coma (el que rige la lista).
    - S: un subordinante de la lista está en G y, además, G termina en «las/los siguientes» + un nombre de
      NOMBRES_CON_SUBORDINANTE (S1), o el subordinante no abre F: la cláusula principal va antes y la lista
      completa la condición (S2).
    - N: sin subordinante en G, G termina en «las/los siguientes» + un nombre de NOMBRES_SIN_SUBORDINANTE o en una
      frase de FRASES_SIN_SUBORDINANTE.
    La marca de excepción se busca en F entera.
    """
    f = sin_diacriticos(oracion_final(texto).lower())
    corte = f.rfind(",")
    inicio_g = corte + 1 if corte >= 0 else 0
    g_crudo = f[inicio_g:]
    g = g_crudo.strip()
    inicio_g += len(g_crudo) - len(g_crudo.lstrip())
    sub = RE_SUBORDINANTE.search(g)
    forma = subforma = None
    if sub:
        if RE_NOMBRE_S.search(g):
            forma, subforma = "S", "S1"
        elif re.search(r"[a-z]", f[:inicio_g + sub.start()]):
            forma, subforma = "S", "S2"
    elif RE_NOMBRE_N.search(g) or RE_FRASE_N.search(g):
        forma = subforma = "N"
    exc = RE_EXCEPCION.search(f)
    return {"forma": forma, "subforma": subforma, "subordinante": sub.group(0) if sub else None,
            "marca_excepcion": exc.group(0) if exc else None, "oracion_final": f, "segmento": g}


def compatibles(an):
    """Regla, punto 4: los tipos destino compatibles con el anuncio (vacío si no hay anuncio)."""
    if an is None or an["forma"] is None:
        return ()
    return COMPATIBLES["EXC"] if an["marca_excepcion"] else COMPATIBLES[an["forma"]]


def decidir(hay_mini_chunk, an, candidatos):
    """Regla, punto 5, en este orden: sin mini-chunk del encabezado; sin anuncio; 0 candidatos; 2 o más; el único
    candidato no compatible; unión. `candidatos`: [(id, tipo)] de los nodos del mini-chunk con tipo en el rango."""
    if not hay_mini_chunk:
        return "sin_unidad_de_encabezado"
    if an is None or an["forma"] is None:
        return "sin_anuncio"
    if not candidatos:
        return "sin_candidato"
    if len(candidatos) > 1:
        return "ambigua"
    return "union" if candidatos[0][1] in compatibles(an) else "destino_no_compatible"


def chunk_base(cid, chunks):
    """El chunk de E0 de un chunk_id; las partes `::parteK` caen en su unidad entera (como la referencia)."""
    if cid in chunks:
        return chunks[cid]
    return chunks[re.sub(r"::parte\d+$", "", cid)]


def _procedencias(n):
    return n.get("provenances") or [n["provenance"]]


def aplicar(kg, chunks, bloque_lista, es_mini_chunk):
    """Aplica la regla a un grafo guardado. Devuelve (registro, aristas, encabezados).

    `chunks`: {id: chunk de E0}. `bloque_lista` y `es_mini_chunk`: las del código del extractor
    (prompt_r2b.py y comun_e1.py), sin reescribir.
    - registro: una fila por Condicion de ítem sin condicion_de saliente, con su resultado;
    - aristas: las uniones, como aristas derivadas (sin marcas de E3);
    - encabezados: el anuncio de cada bloque que abre la lista de alguna fila.
    """
    por_id = {n["id"]: n for n in kg["nodes"]}
    con_condicion_de = {e["source"] for e in kg["edges"] if e["relation"] == PREDICADO}
    nodos_por_chunk = collections.defaultdict(set)
    for n in kg["nodes"]:
        for p in _procedencias(n):
            if p.get("chunk_id"):
                nodos_por_chunk[re.sub(r"::parte\d+$", "", p["chunk_id"])].add(n["id"])
    minis = collections.defaultdict(list)
    for c in chunks.values():
        if es_mini_chunk(c):
            minis[(c["to"], c["unidad"], c["rol_bloque"])].append(c)
    registro, aristas, encabezados = [], [], {}
    for n in sorted((x for x in kg["nodes"] if x["type"] == TIPO_ITEM), key=lambda x: x["id"]):
        if n["id"] in con_condicion_de:
            continue
        cid = n["provenance"]["chunk_id"]
        c = chunk_base(cid, chunks)
        if es_mini_chunk(c):
            continue
        i = bloque_lista(c)
        if i is None:
            continue
        h = c["herencia"][i]
        clave = f"{c['to']}::{h['unidad_origen']}[{h['tipo']}]"
        fila = {"id": n["id"], "to": c["to"], "chunk_id": cid, "bloque": clave, "encabezado": None,
                "candidatos": [], "resultado": None, "destino": None, "tipo_destino": None}
        if h["tipo"] == "encabezado":
            an, hay_mini = None, False
        else:
            m = [x for x in minis.get((c["to"], h["unidad_origen"], h["tipo"]), [])
                 if norm(h["texto"]) in norm(x["texto"])]
            if len(m) != 1:
                raise ValueError(f"{cid}: {len(m)} mini-chunks para el bloque {clave}")
            hay_mini = True
            fila["encabezado"] = m[0]["id"]
            an = anuncio(h["texto"])
            fila["candidatos"] = sorted([g, por_id[g]["type"]] for g in nodos_por_chunk.get(m[0]["id"], ())
                                        if por_id[g]["type"] in RANGO_CONDICION_DE)
        if clave not in encabezados:
            encabezados[clave] = ({k: an[k] for k in ("forma", "subforma", "subordinante", "marca_excepcion",
                                                      "segmento")} | {"compatibles": list(compatibles(an))}
                                  if an else {"forma": None, "nota": "el bloque es la línea de título: sin mini-chunk"})
        fila["resultado"] = decidir(hay_mini, an, fila["candidatos"])
        if fila["resultado"] == "union":
            fila["destino"], fila["tipo_destino"] = fila["candidatos"][0]
            aristas.append({"source": n["id"], "target": fila["destino"], "relation": PREDICADO,
                            "provenance": n["provenance"], "provenances": [n["provenance"]],
                            "rol_fuente": ROL_FUENTE})
        registro.append(fila)
    return registro, aristas, encabezados


def resumen(registro, kg):
    cuenta = collections.Counter(f["resultado"] for f in registro)
    uniones = [f for f in registro if f["resultado"] == "union"]
    cruce = collections.Counter(
        ("sin_mini_chunk" if f["encabezado"] is None else
         "sin_anuncio" if f["resultado"] == "sin_anuncio" else "con_anuncio",
         "0" if not f["candidatos"] else "1" if len(f["candidatos"]) == 1 else "2_o_mas")
        for f in registro)
    return {
        "condicion_en_el_grafo": sum(1 for n in kg["nodes"] if n["type"] == TIPO_ITEM),
        "condicion_de_item_sin_condicion_de": len(registro),
        "resultado": {r: cuenta.get(r, 0) for r in RESULTADOS},
        "uniones_por_tipo_destino": dict(sorted(collections.Counter(f["tipo_destino"] for f in uniones).items())),
        "uniones_por_to": dict(sorted(collections.Counter(f["to"] for f in uniones).items())),
        "uniones_por_bloque": dict(sorted(collections.Counter(f["bloque"] for f in uniones).items())),
        "ambiguas_por_numero_de_candidatos": dict(sorted(collections.Counter(
            len(f["candidatos"]) for f in registro if f["resultado"] == "ambigua").items())),
        "destino_no_compatible_por_tipo": dict(sorted(collections.Counter(
            f["candidatos"][0][1] for f in registro if f["resultado"] == "destino_no_compatible").items())),
        "cruce_anuncio_por_candidatos": {f"{a}|{b}": v for (a, b), v in sorted(cruce.items())},
    }
