"""
e2_lib.py — E2 (reduce) del pipeline de re-extracción v2: ensamblado
determinístico + guarda de fan-in + censo estructural. Código puro, sin LLM
(diseño vinculante: docs/diseno_reextraccion_v2.md §3-E2).

Insumos SOLO LECTURA:
  - E0: data/experiment/reextraccion_v2/e0_chunking/salida/chunks_{to}.json
        y censo_oraculo.json (mapa de unidades por TO).
  - E1: extracciones.jsonl (un registro por chunk, con `validacion` ya
        normalizada por validador_e1: entidades/relaciones con provenance
        {to, archivo, punto, rol_documental} y rechazos registrados).
  - Esquema v2: data/experiment/grafo_v2/code/schema.py (fuente única, se
        importa — misma vía que E1) y esquema_v2_clases.json (labels de
        sujetos del catálogo).

Contratos duros:
  1. Ids determinísticos slug+sha — convención VIGENTE del re-ensamblado v3
     (entity_slug_v3 de data/experiment/grafo_v2/code/assemble_v3.py). Las
     tres funciones se copian textuales porque assemble_v3 no es importable
     sin el SDK de API; selftest_e2.py verifica paridad extrayéndolas por
     AST del fuente original.
  2. Dedup EXACTO solamente: colisión = mismo type + mismo slug normalizado
     completo (el sufijo sha1 del slug entero garantiza que solo contenido
     idéntico-normalizado colisiona). La resolución con juicio es E4.
  3. Guarda de fan-in ANTES de ensamblar: esperados (mapa E0) vs recibidos
     (E1), por estado aceptado/rechazado/ausente, más duplicados (precedente
     RX-01: 102 resultados descartados en silencio por colisión de chunk_id
     en v1) e inesperados. Ausentes, duplicados o inesperados ⇒ NO se
     ensambla salvo flag explícito de parcialidad.
  4. Censo estructural contra el mapa de E0: toda unidad debe tener al menos
     un nodo de contenido; las ausencias se reportan con diagnóstico, jamás
     se inventan (test conceptual: BKL-0024, punto 3.9 de ext ausente del
     grafo v3 con cero nodos de cuerpo).
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any

BASE = Path(__file__).resolve().parent                  # e2_reduce/
REEXTRACCION = BASE.parents[0]                          # reextraccion_v2/
REPO = BASE.parents[3]                                  # raíz del repo

E0_SALIDA = REEXTRACCION / "e0_chunking" / "salida"              # calibración sellada
E0_SALIDA_ENM01 = REEXTRACCION / "e0_chunking" / "salida_enm01"  # enmienda 01 (con mini-chunks)
GRAFO_V2 = REPO / "data" / "experiment" / "grafo_v2"
GRAFO_V2_CODE = GRAFO_V2 / "code"
CATALOGO_PATH = GRAFO_V2 / "esquema_v2_clases.json"
ASSEMBLE_V3_PATH = GRAFO_V2_CODE / "assemble_v3.py"

if str(GRAFO_V2_CODE) not in sys.path:
    sys.path.insert(0, str(GRAFO_V2_CODE))

from schema import (  # noqa: E402  (esquema v2, fuente única — igual que E1)
    ENTITY_TYPES,
    PREDICATES,
    SUJETO_PREDICATES,
    SUJETOS_CATALOGO_SET,
    is_valid_triple,
)

TOS = ("cap", "cla", "ext", "pro", "ric")

# Sentinel del modo sin oráculo (U-B5.1): un corpus sin mapa de territorio no
# tiene censo-oráculo — se pasa este valor como `censo_oraculo` y el censo
# emite nivel_mapa = {"modo": "sin_oraculo"} (el nivel_chunk corre completo).
SIN_ORACULO = "SIN_ORACULO"

# Tipos que NO cuentan como "nodo de contenido" para el censo estructural.
# TextoOrdenado es meta documental (aparece en casi todo chunk y dedupea a un
# nodo por documento): contarlo volvería vacuo el censo — BKL-0024 se detectó
# precisamente como "cero nodos de cuerpo". Sujeto viene del catálogo cerrado,
# no del texto del punto.
TIPOS_NO_CONTENIDO = ("TextoOrdenado", "Sujeto")


# =========================================================================
# Ids determinísticos — COPIA TEXTUAL de la convención vigente del
# re-ensamblado v3 (data/experiment/grafo_v2/code/assemble_v3.py, líneas
# 95-129). No editar acá: cualquier cambio se hace en la fuente y se
# re-copia; selftest_e2.py falla si esta copia diverge del original.
# =========================================================================

def slugify_full(s: str) -> str:
    """Slug normalizado SIN truncar (lowercase, sin acentos, ascii)."""
    if not s:
        return "empty"
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")
    return s or "empty"


def _id_estable(full_slug: str, max_len: int = 80) -> str:
    """Id legible pero sin colisión de prefijo: 80 chars + hash del slug entero.

    El hash se calcula sobre el slug normalizado completo, no sobre el texto
    crudo, para que diferencias irrelevantes (puntuación final, acentos, espacios
    dobles) sigan mergeando como antes.
    """
    return f"{full_slug[:max_len]}_{hashlib.sha1(full_slug.encode('utf-8')).hexdigest()[:6]}"


def entity_slug_v3(e: dict[str, Any]) -> str:
    t = e["type"]
    p = e.get("properties") or {}
    label = e.get("label", "") or ""
    if t == "Comunicacion":
        return slugify_full(str(p.get("codigo") or p.get("numero") or label))
    if t == "TextoOrdenado":
        return slugify_full(str(p.get("archivo") or p.get("_doc") or p.get("materia") or label))
    if t == "Operacion":
        # v3: por label. `properties.tipo` es categórico y funde operaciones
        # distintas (ver docstring, pérdida 2).
        return _id_estable(slugify_full(label or str(p.get("tipo") or "")))
    if t in ("Restriccion", "Obligacion", "Excepcion"):
        return _id_estable(slugify_full(str(p.get("descripcion") or label)))
    return _id_estable(slugify_full(label))


# =========================================================================
# Carga de insumos
# =========================================================================

def cargar_chunks_e0(to: str, e0_dir: Path = E0_SALIDA) -> list[dict]:
    """Chunks de E0 de un TO, en el orden del archivo (orden documental).
    `e0_dir` selecciona la salida: la sellada (default) o la enm01."""
    path = e0_dir / f"chunks_{to}.json"
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def cargar_censo_oraculo(e0_dir: Path = E0_SALIDA) -> dict:
    with (e0_dir / "censo_oraculo.json").open(encoding="utf-8") as f:
        return json.load(f)


def cargar_extracciones(path: Path) -> list[dict]:
    """Registros de E1 (uno por línea). No filtra ni dedupea: la guarda de
    fan-in es la que contabiliza duplicados y ausencias."""
    registros = []
    with path.open(encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if linea:
                registros.append(json.loads(linea))
    return registros


def _labels_catalogo() -> dict[str, dict]:
    """id → {label, nivel} para clases, instancias y roles del catálogo."""
    with CATALOGO_PATH.open(encoding="utf-8") as f:
        cat = json.load(f)
    out: dict[str, dict] = {}
    for e in cat["clases"]:
        out[e["id"]] = {"label": e["label"], "nivel": e["nivel"]}
    for r in cat["roles"]:
        out[r["id"]] = {"label": r["label"], "nivel": "rol"}
    return out


# =========================================================================
# T2 — Guarda de fan-in
# =========================================================================

def _estado_registro(reg: dict) -> tuple[str, str | None]:
    """Estado de un registro de E1: aceptado | rechazado (con motivo)."""
    if reg.get("error"):
        return "rechazado", f"error_api: {reg['error']}"
    val = reg.get("validacion")
    if not isinstance(val, dict):
        return "rechazado", "sin_validacion"
    motivos_chunk = [r["motivo"] for r in val.get("rechazos", []) if r.get("nivel") == "chunk"]
    if motivos_chunk:
        return "rechazado", "; ".join(motivos_chunk)
    return "aceptado", None


def guarda_fanin(chunks: list[dict], registros: list[dict]) -> dict:
    """Esperados (E0) vs recibidos (E1). Devuelve el reporte completo; el
    campo `apto_para_ensamblar` es False si hay ausentes, duplicados o
    inesperados — jamás se ensambla un set parcial sin flag explícito."""
    esperados = [c["id"] for c in chunks]
    esperados_set = set(esperados)

    por_id: dict[str, dict] = {}
    duplicados: list[str] = []
    inesperados: list[str] = []
    for reg in registros:
        cid = reg.get("chunk_id")
        if cid in por_id:
            duplicados.append(cid)
            continue
        if cid not in esperados_set:
            inesperados.append(str(cid))
            continue
        por_id[cid] = reg

    estados: dict[str, dict] = {}
    n = {"aceptado": 0, "rechazado": 0, "ausente": 0}
    for cid in esperados:
        reg = por_id.get(cid)
        if reg is None:
            estados[cid] = {"estado": "ausente", "motivo": None}
            n["ausente"] += 1
        else:
            estado, motivo = _estado_registro(reg)
            estados[cid] = {"estado": estado, "motivo": motivo}
            n[estado] += 1

    ausentes = [cid for cid, e in estados.items() if e["estado"] == "ausente"]
    apto = not ausentes and not duplicados and not inesperados
    return {
        "esperados": len(esperados),
        "recibidos": len(registros),
        "aceptados": n["aceptado"],
        "rechazados": n["rechazado"],
        "ausentes": n["ausente"],
        "lista_ausentes": ausentes,
        "duplicados": sorted(set(duplicados)),
        "inesperados": sorted(set(inesperados)),
        "rechazados_detalle": [
            {"chunk_id": cid, "motivo": e["motivo"]}
            for cid, e in estados.items() if e["estado"] == "rechazado"
        ],
        "estados": estados,
        "apto_para_ensamblar": apto,
    }


# =========================================================================
# T1 — Ensamblador: extracciones-por-chunk → grafo
# =========================================================================

def ensamblar(chunks: list[dict], registros: list[dict]) -> dict:
    """Ensambla el grafo desde los registros ACEPTADOS de E1.

    Determinístico: los registros se procesan en el orden documental de E0
    (no en el orden de llegada del jsonl); los ids de nodo son función del
    contenido (slug+sha). Dedup EXACTO por (type, slug); provenances
    acumuladas con dedup exacto; conflictos de properties se resuelven
    first-write-wins EN ORDEN DOCUMENTAL y quedan registrados (insumo E4).
    """
    orden_e0 = {c["id"]: i for i, c in enumerate(chunks)}
    chunk_por_id = {c["id"]: c for c in chunks}
    labels_cat = _labels_catalogo()

    aceptados = []
    for reg in registros:
        cid = reg.get("chunk_id")
        if cid not in orden_e0:
            continue
        if _estado_registro(reg)[0] == "aceptado":
            aceptados.append(reg)
    aceptados.sort(key=lambda r: orden_e0[r["chunk_id"]])

    nodes_by_id: dict[str, dict] = {}
    edges: dict[tuple[str, str, str], dict] = {}
    cuarentena: dict[str, dict] = {}
    conflictos_props: list[dict] = []
    rechazos_e2: list[dict] = []
    stats = {
        "chunks_ensamblados": 0,
        "entidades_in": 0,
        "relaciones_in": 0,
        "merges_exactos": 0,
        "prov_nodo_acumuladas": 0,
        "prov_arista_acumuladas": 0,
        # Arista ya existente Y con provenance ya registrada (repetición exacta
        # dentro del mismo pasaje). Se contabiliza para que la conservación
        # cierre: relaciones_in == aristas + prov_acumuladas + repetidas + rechazos.
        "aristas_repetidas_exactas": 0,
    }

    def add_prov(obj: dict, prov: dict) -> bool:
        if prov not in obj["provenances"]:
            obj["provenances"].append(dict(prov))
            return True
        return False

    # Aporte por chunk: qué dejó cada chunk en el grafo, separando contenido
    # anclado al punto propio vs a la herencia (chapeau) vs meta (TextoOrdenado
    # /Sujeto). Insumo del diagnóstico del censo y de E3.
    aporte_por_chunk: dict[str, dict] = {}

    for reg in aceptados:
        cid = reg["chunk_id"]
        val = reg["validacion"]
        stats["chunks_ensamblados"] += 1
        local_to_global: dict[str, str] = {}
        aporte = aporte_por_chunk.setdefault(cid, {
            "contenido_propio": 0, "contenido_herencia": 0, "meta": 0,
        })

        for e in val["entidades"]:
            stats["entidades_in"] += 1
            etype = e["type"]
            prov = e["provenance"]
            if etype in TIPOS_NO_CONTENIDO:
                aporte["meta"] += 1
            elif prov["rol_documental"] == "punto_propio" \
                    or prov["rol_documental"].startswith("bloque_"):
                # bloque_<rol> = elemento de un mini-chunk (enmienda 01): el
                # bloque ES el texto propio de esa unidad.
                aporte["contenido_propio"] += 1
            else:
                aporte["contenido_herencia"] += 1
            if etype not in ENTITY_TYPES:
                # E1 ya validó types; esto solo puede dispararse con insumos
                # corruptos — se registra, no se ensambla en silencio.
                rechazos_e2.append({"chunk_id": cid, "motivo": "type_invalido",
                                    "detalle": str(etype)})
                continue
            ent = {"type": etype, "label": e["label"],
                   "properties": dict(e.get("properties") or {})}
            if etype == "TextoOrdenado":
                ent["properties"].setdefault("archivo", prov["archivo"])
            gid = f"{etype}_{entity_slug_v3(ent)}"
            local_to_global[e["local_id"]] = gid

            existente = nodes_by_id.get(gid)
            if existente is not None:
                stats["merges_exactos"] += 1
                for k, v in ent["properties"].items():
                    if k not in existente["properties"]:
                        existente["properties"][k] = v
                    elif existente["properties"][k] != v:
                        conflictos_props.append({
                            "id": gid, "property": k,
                            "conservado": existente["properties"][k],
                            "descartado": v, "chunk_id": cid,
                        })
                if add_prov(existente, prov):
                    stats["prov_nodo_acumuladas"] += 1
                continue

            nodes_by_id[gid] = {
                "id": gid, "type": etype, "label": ent["label"],
                "properties": ent["properties"],
                "provenance": dict(prov), "provenances": [dict(prov)],
            }

        def nodo_sujeto(sujeto_id: str, prov: dict) -> str:
            info = labels_cat.get(sujeto_id, {})
            if sujeto_id not in nodes_by_id:
                nodes_by_id[sujeto_id] = {
                    "id": sujeto_id, "type": "Sujeto",
                    "label": info.get("label", sujeto_id),
                    "properties": {"nivel": info.get("nivel", "")},
                    "provenance": dict(prov), "provenances": [dict(prov)],
                }
            else:
                if add_prov(nodes_by_id[sujeto_id], prov):
                    stats["prov_nodo_acumuladas"] += 1
            return sujeto_id

        def nodo_sujeto_propuesto(r: dict, prov: dict) -> str:
            # Convención v3: propuestos en cuarentena, dedup exacto por slug.
            label = str(r["sujeto_propuesto"]).strip()
            gid = f"Sujeto_propuesto_{slugify_full(label)[:80]}"
            padre = r.get("sujeto_propuesto_padre_sugerido")
            if gid not in nodes_by_id:
                props: dict[str, Any] = {"nivel": "propuesto", "cuarentena": "true"}
                if padre:
                    props["padre_sugerido"] = padre
                nodes_by_id[gid] = {
                    "id": gid, "type": "Sujeto", "label": label, "properties": props,
                    "provenance": dict(prov), "provenances": [dict(prov)],
                }
            else:
                if add_prov(nodes_by_id[gid], prov):
                    stats["prov_nodo_acumuladas"] += 1
            regc = cuarentena.setdefault(gid, {
                "id": gid, "label": label, "padres_sugeridos": [],
                "chunk_ids": [], "apariciones": 0,
            })
            regc["apariciones"] += 1
            if cid not in regc["chunk_ids"]:
                regc["chunk_ids"].append(cid)
            if padre and padre not in regc["padres_sugeridos"]:
                regc["padres_sugeridos"].append(padre)
            return gid

        def add_edge(src: str, pred: str, tgt: str, prov: dict) -> None:
            key = (src, pred, tgt)
            if key in edges:
                if add_prov(edges[key], prov):
                    stats["prov_arista_acumuladas"] += 1
                else:
                    stats["aristas_repetidas_exactas"] += 1
                return
            edges[key] = {
                "source": src, "target": tgt, "relation": pred,
                "provenance": dict(prov), "provenances": [dict(prov)],
            }

        for r in val["relaciones"]:
            stats["relaciones_in"] += 1
            pred = r["predicate"]
            prov = r["provenance"]
            if pred not in PREDICATES:
                rechazos_e2.append({"chunk_id": cid, "motivo": "predicado_invalido",
                                    "detalle": str(pred)})
                continue

            if pred in SUJETO_PREDICATES:
                extremo_local = r.get("source") if pred == "aplica_a" else r.get("target")
                ent_gid = local_to_global.get(extremo_local)
                if ent_gid is None or ent_gid not in nodes_by_id:
                    rechazos_e2.append({"chunk_id": cid, "motivo": "ref_colgante",
                                        "detalle": f"{pred}: extremo '{extremo_local}'"})
                    continue
                ent_type = nodes_by_id[ent_gid]["type"]
                firma_ok = (is_valid_triple(ent_type, pred, "Sujeto")
                            if pred == "aplica_a"
                            else is_valid_triple("Sujeto", pred, ent_type))
                if not firma_ok:
                    rechazos_e2.append({"chunk_id": cid, "motivo": "firma_invalida",
                                        "detalle": f"{ent_type} --{pred}--> Sujeto"
                                        if pred == "aplica_a"
                                        else f"Sujeto --{pred}--> {ent_type}"})
                    continue
                sujeto_id = r.get("sujeto_id")
                if sujeto_id:
                    if sujeto_id not in SUJETOS_CATALOGO_SET:
                        rechazos_e2.append({"chunk_id": cid,
                                            "motivo": "sujeto_id_fuera_de_catalogo",
                                            "detalle": str(sujeto_id)})
                        continue
                    sujeto_gid = nodo_sujeto(sujeto_id, prov)
                elif r.get("sujeto_propuesto"):
                    sujeto_gid = nodo_sujeto_propuesto(r, prov)
                else:
                    rechazos_e2.append({"chunk_id": cid, "motivo": "sujeto_extremo_ausente",
                                        "detalle": pred})
                    continue
                if pred == "aplica_a":
                    add_edge(ent_gid, pred, sujeto_gid, prov)
                else:
                    add_edge(sujeto_gid, pred, ent_gid, prov)
                continue

            src_gid = local_to_global.get(r.get("source"))
            tgt_gid = local_to_global.get(r.get("target"))
            if src_gid is None or tgt_gid is None or \
               src_gid not in nodes_by_id or tgt_gid not in nodes_by_id:
                rechazos_e2.append({"chunk_id": cid, "motivo": "ref_colgante",
                                    "detalle": f"{pred}: source='{r.get('source')}' "
                                               f"target='{r.get('target')}'"})
                continue
            if not is_valid_triple(nodes_by_id[src_gid]["type"], pred,
                                   nodes_by_id[tgt_gid]["type"]):
                rechazos_e2.append({
                    "chunk_id": cid, "motivo": "firma_invalida",
                    "detalle": f"{nodes_by_id[src_gid]['type']} --{pred}--> "
                               f"{nodes_by_id[tgt_gid]['type']}"})
                continue
            add_edge(src_gid, pred, tgt_gid, prov)

    # Canonicalización: orden estable independiente de todo salvo el contenido
    # y el orden documental (que fija provenances y first-write-wins).
    nodes = sorted(nodes_by_id.values(), key=lambda n: n["id"])
    edges_out = [edges[k] for k in sorted(edges.keys())]
    cuarentena_out = sorted(cuarentena.values(),
                            key=lambda c: (-c["apariciones"], c["id"]))

    return {
        "nodes": nodes,
        "edges": edges_out,
        "cuarentena": cuarentena_out,
        "conflictos_properties": conflictos_props,
        "rechazos_e2": rechazos_e2,
        "stats": stats,
        "chunk_por_id": chunk_por_id,
        "aporte_por_chunk": aporte_por_chunk,
    }


# =========================================================================
# T3 — Censo estructural contra el mapa de E0
# =========================================================================

# Limitaciones conocidas de E0, ex ante, por (to, unidad del mapa-oráculo).
# Fuente de cada diagnóstico: e0_chunking/salida/censo_oraculo.md (sellado en
# la unidad E0). `cubierta_por`: unidades del parser que rinden el mismo
# contenido (clase granularidad/divergencia); lista vacía = ausencia real
# conocida del documento fuente.
LIMITACIONES_E0: dict[tuple[str, str], dict] = {
    ("cap", "S10"): {
        "clase": "granularidad_indice",
        "cubierta_por": ["10.1", "10.2", "10.3"],
        "cita": "el índice de cap anuncia las Secciones 10-12 sin desglosar "
                "puntos; el cuerpo SÍ tiene puntos numerados (censo_oraculo.md §cap)."},
    ("cap", "S11"): {
        "clase": "granularidad_indice",
        "cubierta_por": ["11.1", "11.2", "11.3", "11.4", "11.5", "11.6"],
        "cita": "ídem S10 (censo_oraculo.md §cap)."},
    ("cap", "S12"): {
        "clase": "granularidad_indice",
        "cubierta_por": ["12.1", "12.2", "12.3"],
        "cita": "ídem S10 (censo_oraculo.md §cap)."},
    ("ext", "S1"): {
        "clase": "granularidad_indice",
        "cubierta_por": ["1.1", "1.2", "1.3", "1.4", "1.5", "1.6", "1.7", "1.8", "1.9"],
        "cita": "el índice de ext anuncia la Sección 1 sin desglosar; el cuerpo "
                "tiene 1.1-1.9 (censo_oraculo.md §ext)."},
    ("ric", "3.2"): {
        "clase": "divergencia_documento_fuente",
        "cubierta_por": ["3.1.4"],
        "cita": "el índice anuncia '3.2. Modelo de información'; el cuerpo lo "
                "rinde como 3.1.4 — único anunciado_sin_cuerpo de los 5 TOs; "
                "no se fabricó ningún chunk 3.2 (censo_oraculo.md §ric)."},
    ("ric", "4.4"): {
        "clase": "defecto_documento_fuente",
        "cubierta_por": [],
        "cita": "el cuerpo NO contiene un header '4.4.': tras los cuadros de "
                "4.3 aparecen directamente '4.4.3. Riesgo de cambio' y '4.4.4. "
                "Riesgo de posiciones en opciones', huérfanos de su padre. El "
                "parser los rechaza (padre_4.4_no_abierto, registrados en "
                "estructura_ric.json → rechazos_header) y su contenido queda "
                "como prosa del punto abierto precedente — no se fabrica un "
                "4.4 inexistente (censo_oraculo.md §ric)."},
    ("ric", "S1"): {
        "clase": "granularidad_indice",
        "cubierta_por": ["1.1", "1.2"],
        "cita": "granularidad del índice, misma clase que cap/ext "
                "(censo_oraculo.md §ric)."},
    ("ric", "S12"): {
        "clase": "granularidad_indice",
        "cubierta_por": ["12.1", "12.2", "12.3", "12.4"],
        "cita": "granularidad del índice, misma clase que cap/ext "
                "(censo_oraculo.md §ric)."},
}


def _puntos_de_contenido(nodes: list[dict]) -> set[str]:
    """Puntos (provenance.punto) con al menos un nodo de contenido anclado."""
    puntos: set[str] = set()
    for n in nodes:
        if n["type"] in TIPOS_NO_CONTENIDO:
            continue
        for p in n.get("provenances", []):
            puntos.add(p["punto"])
    return puntos


def _cubre(puntos: set[str], unidad: str) -> bool:
    """Una unidad está cubierta si algún nodo de contenido ancla en ella o en
    un descendiente (prefijo con '.'; evita el falso positivo 1.1 vs 1.10)."""
    if unidad in puntos:
        return True
    pref = unidad + "."
    return any(p.startswith(pref) for p in puntos)


def censo_estructural(to: str, chunks: list[dict], nodes: list[dict],
                      fanin: dict, censo_oraculo: dict | None = None,
                      aporte_por_chunk: dict[str, dict] | None = None,
                      limitaciones: dict | None = None) -> dict:
    """Censo en dos niveles contra el mapa de E0.

    Nivel chunk (terminal): toda unidad chunkeada por E0 debe tener ≥1 nodo
    de contenido anclado a su punto propio; las ausencias se diagnostican
    cruzando fan-in (rechazos E1) y flags de E0 (tabular/formula).

    Nivel mapa (oráculo): toda unidad del mapa de territorio debe quedar
    cubierta; las que E0 ya reconcilió como limitación conocida se reportan
    con su diagnóstico ex ante citado (censo_oraculo.md) — nunca se inventa
    estructura para taparlas.
    """
    if censo_oraculo is None:
        censo_oraculo = cargar_censo_oraculo()
    if limitaciones is None:
        limitaciones = LIMITACIONES_E0
    puntos = _puntos_de_contenido(nodes)
    estados_fanin = fanin.get("estados", {})

    # --- Nivel chunk ---
    ausencias_chunk: list[dict] = []
    cubiertas_chunk = 0
    for c in chunks:
        unidad = c["unidad"]
        if c.get("tipo") == "mini_chunk":
            # Un mini-chunk comparte `unidad` con otros (su punto de origen
            # tiene título, intro y cierre): la cobertura se mide por el
            # aporte PROPIO del chunk id, no por el punto (que otro chunk
            # pudo cubrir).
            ap = (aporte_por_chunk or {}).get(c["id"])
            if ap and ap["contenido_propio"] > 0:
                cubiertas_chunk += 1
                continue
        elif unidad in puntos:
            cubiertas_chunk += 1
            continue
        est = estados_fanin.get(c["id"], {"estado": "desconocido", "motivo": None})
        flags = c.get("flags") or {}
        aporte = (aporte_por_chunk or {}).get(c["id"])
        if est["estado"] in ("rechazado", "ausente"):
            diag = f"chunk {est['estado']} en fan-in E1" + \
                   (f" ({est['motivo']})" if est["motivo"] else "")
        elif flags.get("contenido_tabular") or flags.get("formula"):
            diag = "chunk flaggeado no-prosa por E0 (tabular/formula) sin nodos de contenido"
        elif c.get("tipo") == "mini_chunk":
            diag = ("mini-chunk aceptado sin nodos de contenido propios: el "
                    "extractor no encontró contenido normativo extraíble en el "
                    "bloque (candidato a E3 / bloque no normativo)")
        elif _cubre(puntos, unidad):
            diag = "sin nodo propio pero con descendientes cubiertos (anclaje en sub-unidades)"
        elif aporte and aporte["contenido_herencia"] > 0:
            diag = ("contenido anclado SOLO a la herencia (chapeau): "
                    f"{aporte['contenido_herencia']} nodo(s) de contenido en unidades "
                    "contenedoras y 0 en el punto propio (candidato a E3)")
        elif aporte and aporte["meta"] > 0 and aporte["contenido_propio"] == 0:
            diag = ("extracción solo meta (TextoOrdenado/Sujeto), sin contenido "
                    "del punto (candidato a E3)")
        else:
            diag = "chunk aceptado sin nodos de contenido anclados (candidato a E3)"
        ausencias_chunk.append({
            "unidad": unidad, "chunk_id": c["id"],
            "estado_fanin": est["estado"], "diagnostico": diag,
        })

    # --- Nivel mapa (oráculo) ---
    if censo_oraculo == SIN_ORACULO:
        # Corpus sin mapa de territorio (U-B5.1): no hay contra qué
        # reconciliar — se declara el modo, jamás se inventa un oráculo.
        return {
            "to": to,
            "criterio": "nodo de contenido = type no en "
                        f"{list(TIPOS_NO_CONTENIDO)}; anclaje por provenance.punto "
                        "(exacto a nivel chunk; exacto-o-descendiente a nivel mapa; "
                        "mini-chunks por aporte propio del chunk id — enmienda 01)",
            "nivel_chunk": {
                "unidades": len(chunks),
                "cubiertas": cubiertas_chunk,
                "ausencias": ausencias_chunk,
            },
            "nivel_mapa": {"modo": "sin_oraculo"},
        }
    oraculo_to = censo_oraculo.get(to)
    if oraculo_to is None:
        raise ValueError(
            f"censo-oráculo sin entrada para el TO '{to}': el oráculo declarado "
            f"cubre {sorted(censo_oraculo)} — un TO fuera del oráculo corre con "
            f"censo_oraculo=SIN_ORACULO (manifiesto sin mapa_territorio)")
    unidades_mapa = sorted(set(oraculo_to["coincidencias"]) | set(oraculo_to["solo_mapa"])
                           | set(oraculo_to["solo_parser"]))
    ausencias_mapa: list[dict] = []
    limitaciones_aplicadas: list[dict] = []
    cubiertas_mapa = 0
    for u in unidades_mapa:
        lim = limitaciones.get((to, u))
        if _cubre(puntos, u):
            cubiertas_mapa += 1
            continue
        if lim is not None:
            entrada = {"unidad": u, "clase": lim["clase"],
                       "cubierta_por": lim["cubierta_por"], "cita_ex_ante": lim["cita"]}
            if lim["cubierta_por"] and all(_cubre(puntos, cu) for cu in lim["cubierta_por"]):
                entrada["resolucion"] = "reconciliada: contenido rendido en las unidades del parser"
                limitaciones_aplicadas.append(entrada)
                cubiertas_mapa += 1
                continue
            entrada["resolucion"] = "ausencia_conocida_e0"
            limitaciones_aplicadas.append(entrada)
            ausencias_mapa.append({"unidad": u, "diagnostico":
                                   f"ausencia conocida ex ante ({lim['clase']}): {lim['cita']}"})
            continue
        ausencias_mapa.append({"unidad": u, "diagnostico":
                               "sin nodos de contenido y sin limitación conocida de E0 "
                               "(ausencia NO contabilizada — revisar)"})

    return {
        "to": to,
        "criterio": "nodo de contenido = type no en "
                    f"{list(TIPOS_NO_CONTENIDO)}; anclaje por provenance.punto "
                    "(exacto a nivel chunk; exacto-o-descendiente a nivel mapa; "
                    "mini-chunks por aporte propio del chunk id — enmienda 01)",
        "nivel_chunk": {
            "unidades": len(chunks),
            "cubiertas": cubiertas_chunk,
            "ausencias": ausencias_chunk,
        },
        "nivel_mapa": {
            "unidades": len(unidades_mapa),
            "cubiertas": cubiertas_mapa,
            "ausencias": ausencias_mapa,
            "limitaciones_conocidas_aplicadas": limitaciones_aplicadas,
        },
    }


# =========================================================================
# Orquestación (corrida por TO)
# =========================================================================

class FanInError(RuntimeError):
    """Set parcial sin flag: ausentes, duplicados o inesperados en fan-in."""

    def __init__(self, fanin: dict):
        self.fanin = fanin
        super().__init__(
            f"fan-in no apto: ausentes={fanin['ausentes']} "
            f"duplicados={len(fanin['duplicados'])} "
            f"inesperados={len(fanin['inesperados'])}")


def reducir(to: str, extracciones_path: Path, permitir_parcial: bool = False,
            censo_oraculo: dict | None = None, e0_dir: Path = E0_SALIDA,
            limitaciones: dict | None = None) -> dict:
    """Corrida E2 completa para un TO: guarda de fan-in → ensamblado → censo.

    Si el fan-in no es apto y no hay flag, aborta con FanInError ANTES de
    ensamblar (el reporte de fan-in viaja en la excepción). Los rechazados de
    E1 no abortan: están contabilizados y aparecen en el censo. `e0_dir`
    selecciona la salida de E0 (sellada por default; enm01 para la corrida de
    la enmienda, cuyo mapa incluye los mini-chunks como unidades esperadas).
    """
    chunks = cargar_chunks_e0(to, e0_dir=e0_dir)
    registros = cargar_extracciones(extracciones_path)
    fanin = guarda_fanin(chunks, registros)
    if not fanin["apto_para_ensamblar"] and not permitir_parcial:
        raise FanInError(fanin)

    if censo_oraculo is None:
        censo_oraculo = cargar_censo_oraculo(e0_dir)
    ens = ensamblar(chunks, registros)
    censo = censo_estructural(to, chunks, ens["nodes"], fanin, censo_oraculo,
                              aporte_por_chunk=ens["aporte_por_chunk"],
                              limitaciones=limitaciones)

    grafo = {"nodes": ens["nodes"], "edges": ens["edges"]}
    grafo_json = json.dumps(grafo, ensure_ascii=False, indent=2)
    reporte = {
        "to": to,
        "extracciones": str(extracciones_path),
        "parcial": not fanin["apto_para_ensamblar"],
        "fanin": {k: v for k, v in fanin.items() if k != "estados"},
        "nodes_total": len(ens["nodes"]),
        "edges_total": len(ens["edges"]),
        "nodes_by_type": _conteo(ens["nodes"], "type"),
        "edges_by_relation": _conteo(ens["edges"], "relation"),
        "stats": ens["stats"],
        "rechazos_e2": ens["rechazos_e2"],
        "conflictos_properties": ens["conflictos_properties"],
        "cuarentena": {"propuestos": len(ens["cuarentena"])},
        "censo": {
            "nivel_chunk": censo["nivel_chunk"],
            "nivel_mapa": censo["nivel_mapa"],
        },
        "sha256_grafo": hashlib.sha256(grafo_json.encode("utf-8")).hexdigest(),
    }
    return {"grafo": grafo, "grafo_json": grafo_json, "fanin": fanin,
            "censo": censo, "reporte": reporte, "ensamblado": ens}


def _conteo(objs: list[dict], campo: str) -> dict[str, int]:
    out: dict[str, int] = {}
    for o in objs:
        out[o[campo]] = out.get(o[campo], 0) + 1
    return dict(sorted(out.items(), key=lambda kv: (-kv[1], kv[0])))
