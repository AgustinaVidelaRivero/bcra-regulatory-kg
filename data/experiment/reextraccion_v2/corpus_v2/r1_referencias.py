"""
r1_referencias.py — B1.3: referencias cruzadas norma→norma, detector
DETERMINÍSTICO (regex) sobre label + properties de texto de cada nodo de
contenido, con resolución contra (a) el inventario de TOs del subset y (b)
las unidades estructurales de E0 (chunks_<to>.json ∪ estructura_<to>.json,
salida_enm01). Nada se inventa: remisión sin destino resoluble = registro
en `irresolubles`, no arista.

Patrones (castellano normativo BCRA):
  MENCIÓN DE NORMA: «normas sobre "Z"», «TO sobre Z», «Texto Ordenado de/sobre Z»,
     «de dicho ordenamiento» (no resuelve sola: exige punto previo) — Z se
     resuelve contra el inventario por palabras clave normalizadas:
        capitales mínimos → cap · clasificación de deudores → cla ·
        exterior y cambios → ext · protección de (los) usuarios → pro ·
        régimen informativo contable mensual → ric.
     Z fuera del inventario (garantías, previsiones mínimas, …) = irresoluble
     (fuera del subset), registrado con la norma nombrada.
  PUNTOS: «punto(s) N.N[.N]*», listas «, y» y rangos «a» (expansión solo
     cuando comparten prefijo y difieren en el último componente numérico).
  SECCIÓN: «Sección N» → unidad "S<N>" de E0.
  Alcance de la mención: los puntos/secciones que aparecen en los 120
     caracteres ANTERIORES a «… de las normas sobre Z» se atribuyen a esa
     norma; los puntos sin norma en su ventana posterior (90 chars) remiten
     al MISMO TO (remisión interna).
Destino de la arista `referencia` (source = nodo origen):
  - punto/sección resoluble en E0 y con nodos de contenido anclados
    (provenance.punto == destino, cualquier rol) → una arista por nodo
    destino (fan-out declarado), excluyendo el nodo origen;
  - punto existente en E0 sin nodos anclados → irresoluble
    `punto_sin_nodos` (frontera ancla/chunk: hallazgo_frontera_ancla_chunk.md);
  - solo la norma (sin punto) → arista al TextoOrdenado canónico del TO;
  - el punto propio del nodo origen nunca es destino (autorreferencia).
Provenance de la arista = la del nodo origen; `properties.evidencia` =
fragmento exacto; rol_fuente = referencia_cruzada. `referencia` nodo→nodo
NO está en schema.DOMAIN_RANGE (solo TextoOrdenado→Comunicacion); se
declara, no se edita el esquema.
"""

from __future__ import annotations

import json
import random
import re

import r1_comun as C

SEMILLA_MUESTRA = 20260823
TAM_MUESTRA = 30
VENTANA_ANTES = 120
VENTANA_DESPUES = 90
TIPOS_ORIGEN = ("Obligacion", "Restriccion", "Excepcion", "Operacion")
PROPS_TEXTO = ("descripcion", "condicion", "alcance", "umbral", "plazo", "detalle")

INVENTARIO_TOS = {
    "cap": ("capitales minimos",),
    "cla": ("clasificacion de deudores",),
    "ext": ("exterior y cambios",),
    "pro": ("proteccion de los usuarios de servicios financieros",
            "proteccion de usuarios de servicios financieros"),
    "ric": ("regimen informativo contable mensual",),
}

RE_NORMA = re.compile(
    r"(?:[Nn]ormas?\s+sobre|\bT\.?O\.?\s+(?:sobre|de)|[Tt]exto\s+[Oo]rdenado\s+(?:sobre|de))\s*"
    r"[\"“'«]?\s*([^\"”'»\.;\)]{3,90})")
RE_DICHO = re.compile(r"de\s+(?:dicho|ese|este)\s+(?:ordenamiento|texto\s+ordenado)", re.I)
RE_PUNTOS = re.compile(r"\bpuntos?\s+((?:\d+(?:\.\d+)+\.?)(?:\s*(?:,|y|al|a|e|ó|o|hasta)\s*\d+(?:\.\d+)+\.?)*)", re.I)
RE_NUM = re.compile(r"\d+(?:\.\d+)+")
RE_SECCION = re.compile(r"\bSecci(?:o|ó)n(?:es)?\s+(\d+)(?:\s*(?:,|y)\s*(\d+))?", re.I)
RE_PUNTOS_SUELTOS = re.compile(r"\bpuntos?\s+\d+(?:\.\d+)+", re.I)


def _texto(n: dict) -> str:
    partes = [n.get("label") or ""]
    for k in PROPS_TEXTO:
        v = (n.get("properties") or {}).get(k)
        if isinstance(v, str) and v:
            partes.append(v)
    return " | ".join(partes)


def resolver_norma(z: str) -> str | None:
    zn = C.norm(z)
    for to, claves in INVENTARIO_TOS.items():
        if any(k in zn for k in claves):
            return to
    return None


def _expandir_puntos(expr: str) -> list[str]:
    nums = [m.group(0).rstrip(".") for m in RE_NUM.finditer(expr)]
    if not nums:
        return []
    out: list[str] = []
    tokens = re.split(r"(\s*(?:,|\by\b|\bal\b|\ba\b|\bhasta\b|\be\b|\bó\b|\bo\b)\s*)", expr)
    # reconstruye: si el separador entre dos números es " a " → rango
    seq: list[tuple[str, str]] = []   # (sep_previo, num)
    sep = ""
    for t in tokens:
        m = RE_NUM.search(t)
        if m:
            seq.append((sep.strip().lower(), m.group(0).rstrip(".")))
            sep = ""
        else:
            sep = t
    for i, (s, num) in enumerate(seq):
        if s in ("a", "al", "hasta") and i > 0:
            a, b = seq[i - 1][1].split("."), num.split(".")
            if len(a) == len(b) and a[:-1] == b[:-1] and b[-1].isdigit() and a[-1].isdigit() \
                    and int(b[-1]) > int(a[-1]) and int(b[-1]) - int(a[-1]) <= 30:
                for k in range(int(a[-1]) + 1, int(b[-1]) + 1):
                    out.append(".".join(a[:-1] + [str(k)]))
                continue
        if num not in out:
            out.append(num)
    return out


def unidades_e0(to: str) -> set[str]:
    u: set[str] = set()
    for c in C.cargar_chunks_enm01(to):
        u.add(c["unidad"])
        for h in c.get("herencia", []):
            u.add(h["unidad_origen"])
    est = C.cargar_estructura_enm01(to)

    def rec(nodo: dict) -> None:
        if nodo.get("tipo") == "seccion":
            u.add(f"S{nodo['numero']}")
        elif nodo.get("numero"):
            u.add(str(nodo["numero"]))
        for h in nodo.get("hijos", []):
            rec(h)
    for s in est.get("secciones", []):
        rec(s)
    return u


def detectar_menciones(texto: str, to_origen: str) -> list[dict]:
    """Devuelve menciones {to_destino|norma, puntos, secciones, evidencia,
    clase}. Determinístico: recorre el texto en orden."""
    menciones: list[dict] = []
    consumidos: list[tuple[int, int]] = []
    for m in RE_NORMA.finditer(texto):
        z = m.group(1).strip()
        to_dest = resolver_norma(z)
        ini = max(0, m.start() - VENTANA_ANTES)
        ventana = texto[ini:m.start()]
        puntos, secciones = [], []
        spans: list[tuple[int, int]] = []
        for pm in RE_PUNTOS.finditer(ventana):
            puntos += _expandir_puntos(pm.group(1))
            spans.append((ini + pm.start(), ini + pm.end()))
        for sm in RE_SECCION.finditer(ventana):
            secciones += [x for x in sm.groups() if x]
            spans.append((ini + sm.start(), ini + sm.end()))
        consumidos += spans
        ev_ini = min([s[0] for s in spans] + [m.start()])
        menciones.append({"clase": "externa", "norma_nombrada": z, "to_destino": to_dest,
                          "puntos": puntos, "secciones": secciones,
                          "evidencia": texto[ev_ini:m.end()].strip()})
    # "de dicho ordenamiento": puntos previos que apuntan a la última norma citada
    for m in RE_DICHO.finditer(texto):
        prev = [x for x in menciones if x["clase"] == "externa" and x["to_destino"]]
        ini = max(0, m.start() - VENTANA_ANTES)
        ventana = texto[ini:m.start()]
        puntos = []
        for pm in RE_PUNTOS.finditer(ventana):
            puntos += _expandir_puntos(pm.group(1))
            consumidos.append((ini + pm.start(), ini + pm.end()))
        menciones.append({"clase": "externa_anaforica", "norma_nombrada": "dicho ordenamiento",
                          "to_destino": prev[-1]["to_destino"] if prev else None,
                          "puntos": puntos, "secciones": [],
                          "evidencia": texto[ini:m.end()].strip()[-160:]})

    def consumido(a: int, b: int) -> bool:
        return any(a >= x and b <= y for x, y in consumidos)

    for pm in RE_PUNTOS.finditer(texto):
        if consumido(pm.start(), pm.end()):
            continue
        despues = texto[pm.end():pm.end() + VENTANA_DESPUES]
        if RE_NORMA.search(despues) or RE_DICHO.search(despues):
            continue   # la ventana anterior de esa norma ya lo captura (o lo capturará)
        menciones.append({"clase": "interna", "norma_nombrada": None, "to_destino": to_origen,
                          "puntos": _expandir_puntos(pm.group(1)), "secciones": [],
                          "evidencia": texto[max(0, pm.start() - 60):pm.end() + 20].strip()})
    for sm in RE_SECCION.finditer(texto):
        if consumido(sm.start(), sm.end()):
            continue
        despues = texto[sm.end():sm.end() + VENTANA_DESPUES]
        if RE_NORMA.search(despues) or RE_DICHO.search(despues):
            continue
        menciones.append({"clase": "interna", "norma_nombrada": None, "to_destino": to_origen,
                          "puntos": [], "secciones": [x for x in sm.groups() if x],
                          "evidencia": texto[max(0, sm.start() - 60):sm.end() + 20].strip()})
    return menciones


def detectar_y_resolver(kg: dict, perfil: str | None = None, **opciones_r2) -> dict:
    """Remisiones del ensamblado. Sin perfil (o con los perfiles existentes),
    la arista `referencia` con `rol_fuente = referencia_cruzada`, byte a byte
    como en los ensamblados sellados. Con el perfil r2, `remite_a`
    (`detectar_y_resolver_r2`; enmienda 2 de L-ESQ-R2, FIRMADA en 5f9a731)."""
    if perfil == PERFIL_R2:
        return detectar_y_resolver_r2(kg, **opciones_r2)
    if opciones_r2:
        raise TypeError(f"opciones del perfil r2 sin el perfil r2: {sorted(opciones_r2)}")
    nodes_by_id = {n["id"]: n for n in kg["nodes"]}
    unidades = {to: unidades_e0(to) for to in C.TOS_ORDEN}
    # índice (to, punto) → ids de nodos de contenido anclados
    anclados: dict[tuple[str, str], list[str]] = {}
    to_canon: dict[str, str] = {}
    for n in kg["nodes"]:
        if n["type"] == "TextoOrdenado":
            tos = {p["to"] for p in n["provenances"] if p.get("to")}
            for t in tos:
                to_canon[t] = n["id"]
            continue
        if n["type"] in ("Sujeto", "Comunicacion"):
            continue
        for p in n.get("provenances", []):
            if p.get("to") and p.get("punto"):
                anclados.setdefault((p["to"], p["punto"]), []).append(n["id"])
    for k in anclados:
        anclados[k] = sorted(set(anclados[k]))

    triplas = {(e["source"], e["relation"], e["target"]) for e in kg["edges"]}
    remisiones: list[dict] = []
    irresolubles: list[dict] = []
    nuevas: list[dict] = []
    por_to = {to: {"nodos_con_remision": 0, "menciones": 0, "resueltas": 0,
                   "irresolubles": 0, "aristas": 0} for to in C.TOS_ORDEN}

    def agregar(src: dict, tgt_id: str, men: dict, destino: str, via: str) -> None:
        k = (src["id"], "referencia", tgt_id)
        if k in triplas or tgt_id == src["id"]:
            return
        e = {"source": src["id"], "target": tgt_id, "relation": "referencia",
             "provenance": dict(src["provenance"]),
             "provenances": [dict(p) for p in src["provenances"]],
             "rol_fuente": "referencia_cruzada",
             "properties": {"evidencia": men["evidencia"], "clase": men["clase"],
                            "destino": destino, "via": via}}
        kg["edges"].append(e)
        nuevas.append(e)
        triplas.add(k)
        por_to[src["provenance"]["to"]]["aristas"] += 1

    for n in sorted(kg["nodes"], key=lambda x: x["id"]):
        if n["type"] not in TIPOS_ORIGEN:
            continue
        to_o = n["provenance"].get("to")
        if to_o not in C.TOS_ORDEN:
            continue
        texto = _texto(n)
        menciones = detectar_menciones(texto, to_o)
        if not menciones:
            continue
        por_to[to_o]["nodos_con_remision"] += 1
        propios = {p["punto"] for p in n["provenances"]}
        for men in menciones:
            por_to[to_o]["menciones"] += 1
            reg = {"nodo": n["id"], "to_origen": to_o, "punto_origen": n["provenance"]["punto"],
                   **{k: v for k, v in men.items()}}
            remisiones.append(reg)
            if men["to_destino"] is None:
                reg["estado"] = "irresoluble"
                reg["motivo"] = ("norma fuera del inventario del subset" if men["clase"] == "externa"
                                 else "anáfora sin norma previa resoluble")
                irresolubles.append(reg)
                por_to[to_o]["irresolubles"] += 1
                continue
            td = men["to_destino"]
            destinos = [(p, "punto") for p in men["puntos"]] + [(f"S{s}", "seccion") for s in men["secciones"]]
            if not destinos:
                if men["clase"] == "interna":
                    reg["estado"] = "irresoluble"; reg["motivo"] = "mención interna sin punto"
                    irresolubles.append(reg); por_to[to_o]["irresolubles"] += 1
                    continue
                agregar(n, to_canon[td], men, f"{td}::TO", "texto_ordenado")
                reg["estado"] = "resuelta"; reg["destinos"] = [f"{td}::TO"]
                por_to[to_o]["resueltas"] += 1
                continue
            res, irr = [], []
            for d, clase in destinos:
                if td == to_o and d in propios:
                    irr.append({"destino": d, "motivo": "autorreferencia al punto propio"})
                    continue
                if d not in unidades[td]:
                    irr.append({"destino": d, "motivo": f"{clase} inexistente en E0 de {td}"})
                    continue
                ids = [i for i in anclados.get((td, d), []) if i != n["id"]]
                if not ids:
                    irr.append({"destino": d, "motivo": "punto_sin_nodos (existe en E0; contenido "
                                                        "solo en descendientes/contenedor — frontera ancla/chunk)"})
                    continue
                for i in ids:
                    agregar(n, i, men, f"{td}::{d}", "nodos_del_punto")
                res.append({"destino": f"{td}::{d}", "n_nodos": len(ids)})
            reg["destinos"] = res
            reg["irresolubles_parciales"] = irr
            if res:
                reg["estado"] = "resuelta" if not irr else "parcial"
                por_to[to_o]["resueltas"] += 1
            else:
                reg["estado"] = "irresoluble"
                reg["motivo"] = "; ".join(sorted({x["motivo"] for x in irr}))
                irresolubles.append(reg)
                por_to[to_o]["irresolubles"] += 1

    rng = random.Random(SEMILLA_MUESTRA)
    muestra_idx = sorted(rng.sample(range(len(nuevas)), min(TAM_MUESTRA, len(nuevas))))
    muestra = []
    for k, i in enumerate(muestra_idx, 1):
        e = nuevas[i]
        s, t = nodes_by_id[e["source"]], nodes_by_id[e["target"]]
        muestra.append({
            "n": k, "indice_en_nuevas": i,
            "source": e["source"], "source_label": s["label"],
            "source_ancla": f"{s['provenance']['to']}::{s['provenance']['punto']}",
            "target": e["target"], "target_type": t["type"], "target_label": t["label"],
            "target_ancla": f"{t['provenance'].get('to')}::{t['provenance'].get('punto')}",
            "target_anclas_todas": sorted({f"{p.get('to')}::{p.get('punto')}" for p in t["provenances"]}),
            "destino": e["properties"]["destino"], "clase": e["properties"]["clase"],
            "evidencia_verbatim": e["properties"]["evidencia"],
            "texto_origen_completo": _texto(s),
        })
    fanout = C.conteo([{"d": e["properties"]["destino"]} for e in nuevas], "d")
    resumen = {
        "semilla_muestra": SEMILLA_MUESTRA,
        "nodos_con_remision": sum(v["nodos_con_remision"] for v in por_to.values()),
        "menciones": len(remisiones),
        "resueltas": sum(1 for r in remisiones if r["estado"] in ("resuelta", "parcial")),
        "parciales": sum(1 for r in remisiones if r["estado"] == "parcial"),
        "irresolubles": len(irresolubles),
        "aristas_referencia_nuevas": len(nuevas),
        "aristas_a_texto_ordenado": sum(1 for e in nuevas if e["properties"]["via"] == "texto_ordenado"),
        "aristas_cross_to": sum(1 for e in nuevas if e["properties"]["destino"].split("::")[0]
                                != e["provenance"]["to"]),
        "por_to": por_to,
        "por_clase": C.conteo([{"c": r["clase"]} for r in remisiones], "c"),
        "irresolubles_por_motivo": C.conteo([{"m": r.get("motivo", "")} for r in irresolubles], "m"),
        "normas_fuera_inventario": C.conteo(
            [{"z": C.norm(r["norma_nombrada"])} for r in irresolubles
             if r["clase"] == "externa" and r["to_destino"] is None], "z"),
        "fanout_max_destino": max(fanout.values()) if fanout else 0,
        "declaracion_esquema": "referencia nodo→nodo no está en schema.DOMAIN_RANGE "
                               "(solo TextoOrdenado→Comunicacion); aristas con rol_fuente="
                               "referencia_cruzada; no se edita schema.py.",
    }
    return {"resumen": resumen, "remisiones": remisiones, "irresolubles": irresolubles,
            "muestra": muestra, "nuevas": nuevas}


# ----------------------------------------------------------------------- #
# Perfil r2: `remite_a` (enmienda 2 de L-ESQ-R2, FIRMADA en 5f9a731;       #
# enmienda 1 al mandato de U-R2-CODIGO, R3.d; decisión 11 del mandato)    #
# ----------------------------------------------------------------------- #
PERFIL_R2 = "r2"
PREDICADO_R2 = "remite_a"
# §2: los siete tipos de contenido son origen y destino (H1: se suman
# Condicion, Potestad y Definicion a TIPOS_ORIGEN).
TIPOS_CONTENIDO_R2 = ("Operacion", "Restriccion", "Excepcion", "Obligacion", "Potestad",
                      "Condicion", "Definicion")
# H4: el resolvedor lee también `termino` (texto de los nodos para la
# atribución D1 y para la variante sobre la paráfrasis de los controles).
PROPS_TEXTO_R2 = PROPS_TEXTO + ("termino",)
ALCANCES_R2 = ("to_entero", "interna", "externa")
# Rótulo de unidad al comienzo de línea («6.1. …», «6.10.Declaración…»,
# «Sección 8. …»): insumo del criterio de texto de cuerpo de las variantes.
RE_ROTULO_UNIDAD = re.compile(r"^\s*(?:\d+(?:\.\d+)*\.\s*\S|Secci(?:o|ó)n\s+\d+\b)")
# Cita a una Comunicación (decisión 7 de la enmienda 2): «Comunicación “A” 6847»,
# «Comunicaciones "A" 1234 y 5678», «Com. A 6847». Cada número es una cita.
RE_COMUNICACION = re.compile(
    r"\bCom(?:unicaci(?:o|ó)n(?:es)?|\.)\s*[\"“”'«»]?\s*((?-i:[ABC]))\s*[\"“”'«»]?\s*"
    r"(N[°º]\s*)?(\d{1,2}\.?\d{3}|\d{1,4})((?:\s*(?:,|y|e)\s*\d{1,2}\.?\d{3}|\s*(?:,|y|e)\s*\d{1,4})*)",
    re.I)
RE_NUM_COM = re.compile(r"\d{1,2}\.?\d{3}|\d{1,4}")
# Pie de página que E0 no recortó (caso conocido: ctacte::6.1.2.3): la línea
# de la cita tiene la forma del pie del BCRA.
RE_PIE_NO_RECORTADO = re.compile(r"Versi(?:o|ó)n:|Vigencia:|P(?:a|á)gina\s+\d+", re.I)


def normalizar_e0(texto: str) -> tuple[str, list[int]]:
    """Texto de E0 para la detección: el corte de palabra al final de línea
    («nor-\nmas») se une y todo otro salto de línea pasa a espacio. Devuelve
    el texto normalizado y, por cada carácter, su posición en el original,
    para que la evidencia sea un tramo literal del texto de E0."""
    out, mapa = [], []
    i, n = 0, len(texto)
    while i < n:
        c = texto[i]
        if (c == "-" and i + 1 < n and texto[i + 1] == "\n" and i > 0 and texto[i - 1].isalpha()
                and i + 2 < n and texto[i + 2].isalpha()):
            i += 2
            continue
        out.append(" " if c == "\n" else c)
        mapa.append(i)
        i += 1
    return "".join(out), mapa


def evidencia_literal(original: str, norm: str, mapa: list[int], evidencia: str) -> str:
    """Tramo del texto original que corresponde a `evidencia` (una subcadena
    del texto normalizado)."""
    i = norm.find(evidencia)
    if i == -1 or not evidencia:
        return evidencia
    return original[mapa[i]:mapa[i + len(evidencia) - 1] + 1]


def _texto_r2(n: dict, leer_termino: bool = True) -> str:
    """Texto guardado del nodo: label y las claves de PROPS_TEXTO(_R2), donde
    estén en el nodo r2 (properties, campos_heredados_v3 o
    properties_no_definidas)."""
    claves = PROPS_TEXTO_R2 if leer_termino else PROPS_TEXTO
    partes = [n.get("label") or ""]
    fuentes = [n.get("properties") or {}, n.get("campos_heredados_v3") or {},
               n.get("properties_no_definidas") or {}]
    for k in claves:
        for f in fuentes:
            v = f.get(k)
            if isinstance(v, str) and v:
                partes.append(v)
                break
    return " | ".join(partes)


def tiene_texto_de_cuerpo(texto: str) -> bool:
    """Criterio declarado para las variantes `::rep<k>` (regla L): un chunk
    tiene texto de cuerpo si, quitando cada línea que es un rótulo de unidad y
    la línea que sigue a cada rótulo (la cola de un título partido), queda
    alguna línea con texto. Una línea de índice («6.1. Solicitud de
    participación.», con o sin su cola) no tiene texto de cuerpo."""
    lineas = (texto or "").split("\n")
    quitar = set()
    for i, l in enumerate(lineas):
        if RE_ROTULO_UNIDAD.match(l):
            quitar.add(i)
            if i + 1 < len(lineas) and not RE_ROTULO_UNIDAD.match(lineas[i + 1]):
                quitar.add(i + 1)
    return any(l.strip() for i, l in enumerate(lineas) if i not in quitar)


def _variantes(chunks: list[dict]) -> dict[str, dict]:
    """id canónico → {canonico, variantes (ids en orden documental),
    con_cuerpo (ids con texto de cuerpo)}, solo para ids con variantes."""
    grupos: dict[str, list[dict]] = {}
    for c in chunks:
        grupos.setdefault(c.get("id_e0_original") or c["id"], []).append(c)
    out = {}
    for base, g in grupos.items():
        if len(g) > 1:
            out[base] = {"canonico": base, "variantes": [c["id"] for c in g],
                         "con_cuerpo": [c["id"] for c in g if tiene_texto_de_cuerpo(c["texto"])]}
    return out


def _chunk_de_procedencia(p: dict, emisores: dict | None) -> str | None:
    """chunk_id de una procedencia: el que trae (E2 del perfil r2) o el que
    asigna la regla de r1_provenance (punto propio, bloque, primer emisor de
    la herencia)."""
    if p.get("chunk_id"):
        return p["chunk_id"]
    to, punto, rol = p.get("to"), p.get("punto"), p.get("rol_documental") or ""
    if rol == "punto_propio":
        return f"{to}::{punto}"
    if rol.startswith("bloque_"):
        return f"{to}::{punto}::{rol[len('bloque_'):]}"
    em = (emisores or {}).get((to, punto, rol)) or []
    return em[0] if em else None


def _texto_e0_de(p: dict, chunk: dict) -> str:
    """Texto de E0 del punto de la procedencia dentro de su chunk: el texto
    propio (punto propio o bloque) o el tramo heredado de esa unidad."""
    rol = p.get("rol_documental") or ""
    if rol.startswith("herencia_"):
        tipo = rol[len("herencia_"):]
        return "\n".join(h["texto"] for h in chunk.get("herencia", [])
                         if h["unidad_origen"] == p.get("punto") and h.get("tipo") == tipo)
    return chunk.get("texto") or ""


def _contiene_unidad(texto: str, men: dict) -> bool:
    """D1: el texto guardado del nodo contiene la unidad citada (un punto o
    una sección de la cita, o la norma nombrada si la cita nombra solo la
    norma)."""
    for d in men["puntos"]:
        if re.search(r"(?<![\d.])" + re.escape(d) + r"(?![\d])", texto):
            return True
    for s_ in men["secciones"]:
        if re.search(r"\bSecci(?:o|ó)n(?:es)?\s+(?:\d+\s*(?:,|y)\s*)*" + re.escape(s_) + r"\b", texto, re.I):
            return True
    if not men["puntos"] and not men["secciones"] and men.get("to_destino"):
        return any(resolver_norma(m.group(1)) == men["to_destino"] for m in RE_NORMA.finditer(texto))
    return False


def alcance_remision(td: str, to_procedencia: str, a_texto_ordenado: bool) -> str:
    """§3: to_entero si el destino es un TextoOrdenado; si no, interna cuando
    la unidad citada es del mismo TO que la procedencia de resolución y
    externa cuando es de otro. No se copia la clase de la mención."""
    if a_texto_ordenado:
        return "to_entero"
    return "interna" if td == to_procedencia else "externa"


def registro_comunicaciones(chunks_por_to: dict[str, list[dict]]) -> dict:
    """Decisión 7: citas a Comunicaciones en el texto propio de los chunks de
    E0, sin arista. Por TO y por ensamblado: citas, chunks y Comunicaciones
    distintas; aparte, las citas cuya línea tiene la forma de un pie de página
    que E0 no recortó."""
    filas, por_to = [], {}
    for to in sorted(chunks_por_to):
        for c in chunks_por_to[to]:
            original = c.get("texto") or ""
            texto, mapa = normalizar_e0(original)
            for m in RE_COMUNICACION.finditer(texto):
                letra = m.group(1)
                nums = [m.group(3)] + RE_NUM_COM.findall(m.group(4) or "")
                o_ini, o_fin = mapa[m.start()], mapa[m.end() - 1] + 1
                ini = original.rfind("\n", 0, o_ini) + 1
                fin = original.find("\n", o_fin)
                linea = original[ini:fin if fin != -1 else len(original)]
                pie = bool(RE_PIE_NO_RECORTADO.search(linea))
                for x in nums:
                    filas.append({"to": to, "chunk_id": c["id"], "comunicacion": f"{letra} {x.replace('.', '')}",
                                  "tramo": original[o_ini:o_fin], "pie_no_recortado": pie})
    for to in sorted(chunks_por_to):
        fs = [f for f in filas if f["to"] == to]
        por_to[to] = {"citas": len(fs), "chunks": len({f["chunk_id"] for f in fs}),
                      "comunicaciones_distintas": len({f["comunicacion"] for f in fs}),
                      "citas_en_pie_no_recortado": sum(f["pie_no_recortado"] for f in fs)}
    return {"criterio": "RE_COMUNICACION sobre el texto propio de cada chunk de E0 (normalizar_e0); "
                        "un número = una cita",
            "total": {"citas": len(filas), "chunks": len({f["chunk_id"] for f in filas}),
                      "comunicaciones_distintas": len({f["comunicacion"] for f in filas}),
                      "citas_en_pie_no_recortado": sum(f["pie_no_recortado"] for f in filas)},
            "por_to": por_to,
            "pies_no_recortados": [f for f in filas if f["pie_no_recortado"]],
            "filas": filas}


def detectar_y_resolver_r2(kg: dict, emisores: dict | None = None, fuente: str = "e0",
                           tipos_origen: tuple = TIPOS_CONTENIDO_R2, leer_termino: bool = True,
                           por_procedencia: bool = True, propios: str = "procedencia",
                           predicado: str = PREDICADO_R2) -> dict:
    """Remisiones del perfil r2. Por defecto, la regla firmada: detección sobre
    el texto de E0 del punto de origen (por chunk_id), desde cada procedencia
    de los siete tipos de contenido, con atribución D1, `alcance`, `destino` y
    `evidencia` en la arista y sin `rol_fuente`, `clase` ni `via`.

    Las opciones existen solo para los controles de la unidad (r2_codigo/
    r3d_remisiones.py): `fuente="parafrasis"` lee el texto guardado de cada
    nodo, como la cadena r1; `por_procedencia=False` resuelve desde la
    procedencia primaria; `propios="nodo"` excluye, como la cadena r1, todo
    punto de las procedencias del nodo de origen. Con (parafrasis, False,
    "nodo", sin termino) y los cuatro tipos de la cadena r1, los pares origen →
    destino son los de las aristas `referencia` de la cadena r1."""
    if fuente not in ("e0", "parafrasis") or propios not in ("procedencia", "nodo"):
        raise ValueError(f"opción desconocida: fuente={fuente!r} propios={propios!r}")
    nodes_by_id = {n["id"]: n for n in kg["nodes"]}
    unidades = {to: unidades_e0(to) for to in C.TOS_ORDEN}
    chunks_por_to = {to: C.cargar_chunks_enm01(to) for to in C.TOS_ORDEN}
    chunk_por_id = {c["id"]: c for cs in chunks_por_to.values() for c in cs}
    variantes = {k: v for cs in chunks_por_to.values() for k, v in _variantes(cs).items()}

    anclados: dict[tuple[str, str], list[str]] = {}
    anclados_chunk: dict[tuple[str, str, str], list[str]] = {}
    to_canon: dict[str, str] = {}
    for n in kg["nodes"]:
        if n["type"] == "TextoOrdenado":
            for t in sorted({p["to"] for p in n["provenances"] if p.get("to")}):
                to_canon[t] = n["id"]
            continue
        if n["type"] not in TIPOS_CONTENIDO_R2:
            continue
        for p in n.get("provenances", []):
            if p.get("to") and p.get("punto"):
                anclados.setdefault((p["to"], p["punto"]), []).append(n["id"])
                if p.get("chunk_id"):
                    anclados_chunk.setdefault((p["to"], p["punto"], p["chunk_id"]), []).append(n["id"])
    for d_ in (anclados, anclados_chunk):
        for k in d_:
            d_[k] = sorted(set(d_[k]))

    aristas: dict[tuple[str, str, str], dict] = {}
    registro: list[dict] = []
    conteo = {"procedencias_con_texto": 0, "procedencias_sin_texto_e0": 0,
              "atribucion_d1": {"nodos_que_contienen_la_unidad": 0, "todos_los_nodos_del_punto": 0},
              "aristas_con_varias_procedencias": 0, "citas_a_unidad_con_variantes": 0,
              "procedencias_sin_texto_e0_detalle": []}

    def agregar(src: str, tgt: str, procedencia: dict, men: dict, destino: str, alcance: str) -> bool:
        k = (src, predicado, tgt)
        if tgt == src:
            return False
        e = aristas.get(k)
        if e is not None:
            if procedencia not in e["provenances"]:
                e["provenances"].append(dict(procedencia))
                if len(e["provenances"]) == 2:
                    conteo["aristas_con_varias_procedencias"] += 1
            return False
        aristas[k] = {"source": src, "target": tgt, "relation": predicado,
                      "provenance": dict(procedencia), "provenances": [dict(procedencia)],
                      "properties": {"alcance": alcance, "destino": destino,
                                     "evidencia": men["evidencia"]}}
        return True

    def resolver(origenes: list[str], procedencia: dict, propios_set: set, men: dict) -> dict:
        to_o = procedencia["to"]
        cita = {"origenes": origenes, "procedencia": {k: procedencia.get(k) for k in
                                                     ("to", "punto", "rol_documental", "chunk_id")},
                "clase": men["clase"], "norma_nombrada": men["norma_nombrada"],
                "to_destino": men["to_destino"], "puntos": men["puntos"],
                "secciones": men["secciones"], "evidencia": men["evidencia"],
                "destinos": [], "irresolubles": [], "aristas_nuevas": 0}
        if men["to_destino"] is None:
            cita["irresolubles"].append({"destino": None, "causa": (
                "norma fuera del inventario" if men["clase"] == "externa"
                else "anáfora sin norma previa resoluble")})
            return cita
        td = men["to_destino"]
        destinos = [(p_, "punto") for p_ in men["puntos"]] + [(f"S{s_}", "seccion") for s_ in men["secciones"]]
        if not destinos:
            if men["clase"] == "interna":
                cita["irresolubles"].append({"destino": None, "causa": "mención interna sin punto"})
                return cita
            if td not in to_canon:
                cita["irresolubles"].append({"destino": f"{td}::TO", "causa": "texto ordenado sin nodo"})
                return cita
            n_new = sum(agregar(o, to_canon[td], procedencia, men, f"{td}::TO", "to_entero") for o in origenes)
            cita["destinos"].append({"destino": f"{td}::TO", "alcance": "to_entero", "nodos": [to_canon[td]]})
            cita["aristas_nuevas"] += n_new
            return cita
        for d, clase in destinos:
            if td == to_o and d in propios_set:
                cita["irresolubles"].append({"destino": f"{td}::{d}", "causa": "autorreferencia al punto propio"})
                continue
            if d not in unidades[td]:
                cita["irresolubles"].append({"destino": f"{td}::{d}", "causa": f"{clase} inexistente en E0"})
                continue
            ids = anclados.get((td, d), [])
            var = variantes.get(f"{td}::{d}")
            if var is not None:
                conteo["citas_a_unidad_con_variantes"] += 1
                if len(var["con_cuerpo"]) > 1:
                    cita["irresolubles"].append({"destino": f"{td}::{d}", "causa": "destino ambiguo",
                                                 "variantes_con_cuerpo": var["con_cuerpo"]})
                    continue
                con_chunk = anclados_chunk.get((td, d, var["canonico"]))
                if con_chunk is not None or any(anclados_chunk.get((td, d, v)) for v in var["variantes"]):
                    ids = con_chunk or []
            if not any(i != o for o in origenes for i in ids):
                cita["irresolubles"].append({"destino": f"{td}::{d}", "causa": "punto_sin_nodos"})
                continue
            alc = alcance_remision(td, to_o, False)
            n_new = 0
            for o in origenes:
                for i in ids:
                    n_new += agregar(o, i, procedencia, men, f"{td}::{d}", alc)
            cita["destinos"].append({"destino": f"{td}::{d}", "alcance": alc, "nodos": ids})
            cita["aristas_nuevas"] += n_new
        return cita

    origen_nodos = sorted((n for n in kg["nodes"] if n["type"] in tipos_origen and n["type"] in TIPOS_CONTENIDO_R2),
                          key=lambda x: x["id"])
    if fuente == "parafrasis":
        for n in origen_nodos:
            procs = n["provenances"] if por_procedencia else [n["provenance"]]
            vistas = []
            for p in procs:
                if p in vistas or p.get("to") not in C.TOS_ORDEN:
                    continue
                vistas.append(p)
                texto = _texto(n) if not leer_termino else _texto_r2(n, True)
                propios_set = ({q["punto"] for q in n["provenances"]} if propios == "nodo" else {p["punto"]})
                for men in detectar_menciones(texto, p["to"]):
                    registro.append(resolver([n["id"]], p, propios_set, men))
    else:
        por_proc: dict[str, tuple[dict, list[str]]] = {}
        for n in origen_nodos:
            procs = n["provenances"] if por_procedencia else [n["provenance"]]
            for p in procs:
                if p.get("to") not in C.TOS_ORDEN or p.get("rol_documental") == "esqueleto":
                    continue
                cid = _chunk_de_procedencia(p, emisores)
                prov_canonica = dict(p)
                if cid and not p.get("chunk_id"):
                    prov_canonica = {**p, "chunk_id": cid}
                k = C.prov_key({kk: prov_canonica.get(kk) for kk in ("to", "punto", "rol_documental", "chunk_id")})
                if k not in por_proc:
                    por_proc[k] = (prov_canonica, [])
                if n["id"] not in por_proc[k][1]:
                    por_proc[k][1].append(n["id"])
        for k in sorted(por_proc):
            p, nodos = por_proc[k]
            cid = p.get("chunk_id")
            chunk = chunk_por_id.get(cid) if cid else None
            if chunk is None:
                conteo["procedencias_sin_texto_e0"] += 1
                conteo["procedencias_sin_texto_e0_detalle"].append({kk: p.get(kk) for kk in
                                                                    ("to", "punto", "rol_documental", "chunk_id")})
                continue
            original = _texto_e0_de(p, chunk)
            texto, mapa = normalizar_e0(original)
            conteo["procedencias_con_texto"] += 1
            propios_set = ({q["punto"] for i in nodos for q in nodes_by_id[i]["provenances"]}
                           if propios == "nodo" else {p["punto"]})
            for men in detectar_menciones(texto, p["to"]):
                men["evidencia"] = evidencia_literal(original, texto, mapa, men["evidencia"])
                contienen = [i for i in nodos if _contiene_unidad(_texto_r2(nodes_by_id[i], leer_termino), men)]
                if contienen:
                    conteo["atribucion_d1"]["nodos_que_contienen_la_unidad"] += 1
                else:
                    conteo["atribucion_d1"]["todos_los_nodos_del_punto"] += 1
                cita = resolver(contienen or list(nodos), p, propios_set, men)
                cita["atribucion"] = "contiene_la_unidad" if contienen else "todos_los_nodos_del_punto"
                cita["chunk_id"] = cid
                registro.append(cita)

    nuevas = [aristas[k] for k in sorted(aristas)]
    tipo = {n["id"]: n["type"] for n in kg["nodes"]}
    triplas = {(e["source"], e["relation"], e["target"]) for e in kg["edges"]}
    agregadas = [e for e in nuevas if (e["source"], e["relation"], e["target"]) not in triplas]
    kg["edges"].extend(agregadas)

    def por(objs, f):
        out: dict[str, int] = {}
        for o in objs:
            k = f(o)
            out[k] = out.get(k, 0) + 1
        return dict(sorted(out.items()))

    # Unidad de conteo de §5 de la enmienda 2: la cita = (chunk de origen,
    # tramo, unidad citada). Una cita cuenta en cada firma (tipo de origen →
    # tipo de destino) de sus pares; la suma por firma puede superar el total.
    def clave_origen(c: dict) -> str:
        return c.get("chunk_id") or C.prov_key(c["procedencia"])

    citas_res: dict[tuple, dict] = {}
    citas_irr: dict[tuple, str] = {}
    for c in registro:
        for d in c["destinos"]:
            k = (clave_origen(c), c["evidencia"], d["destino"])
            x = citas_res.setdefault(k, {"alcance": d["alcance"], "firmas": set()})
            x["firmas"] |= {f"{tipo[o]}->{tipo[t]}" for o in c["origenes"] for t in d["nodos"] if o != t}
        for x in c["irresolubles"]:
            citas_irr.setdefault((clave_origen(c), c["evidencia"], x["destino"]), x["causa"])
    citas_firma: dict[str, int] = {}
    for x in citas_res.values():
        for f in x["firmas"]:
            citas_firma[f] = citas_firma.get(f, 0) + 1
    resumen = {
        "perfil": PERFIL_R2, "predicado": predicado,
        "opciones": {"fuente": fuente, "tipos_origen": list(tipos_origen), "leer_termino": leer_termino,
                     "por_procedencia": por_procedencia, "propios": propios},
        "unidad_de_cita": "(chunk de origen, tramo, unidad citada)",
        "menciones_detectadas": len(registro),
        "citas_resueltas": len(citas_res),
        "citas_resueltas_por_alcance": por(citas_res.values(), lambda x: x["alcance"]),
        "citas_resueltas_por_firma": dict(sorted(citas_firma.items())),
        "citas_irresolubles": len(citas_irr),
        "irresolubles_por_causa": por(citas_irr.values(), lambda x: x),
        "aristas": len(nuevas),
        "aristas_agregadas": len(agregadas),
        "aristas_por_alcance": por(nuevas, lambda e: e["properties"]["alcance"]),
        "aristas_por_firma": por(nuevas, lambda e: f"{tipo[e['source']]}->{tipo[e['target']]}"),
        "atribucion_d1": conteo["atribucion_d1"] if fuente == "e0" else None,
        "procedencias_con_texto": conteo["procedencias_con_texto"],
        "procedencias_sin_texto_e0": conteo["procedencias_sin_texto_e0"],
        "aristas_con_varias_procedencias": conteo["aristas_con_varias_procedencias"],
        "citas_a_unidad_con_variantes": conteo["citas_a_unidad_con_variantes"],
    }
    return {"resumen": resumen, "registro": registro, "nuevas": nuevas,
            "procedencias_sin_texto_e0": conteo["procedencias_sin_texto_e0_detalle"],
            "comunicaciones": registro_comunicaciones(chunks_por_to)}
