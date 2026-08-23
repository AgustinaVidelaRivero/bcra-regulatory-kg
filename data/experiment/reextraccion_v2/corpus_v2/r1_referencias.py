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


def detectar_y_resolver(kg: dict) -> dict:
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
