"""Métricas intrínsecas del grafo — implementación de la spec sellada.

Gobernada por `docs/spec_evaluacion_intrinseca.md` (sellada en commit cdf90e6).
Implementa M1..M10 EXACTAMENTE como la tabla §4 de la spec; M11 (cobertura CQ)
NO se computa acá: su régimen especial (§6) exige una medición única separada —
queda el stub con el puntero.

Restricciones (§9 de la spec):
- Solo lectura de todo insumo del repo. Cero llamadas a API. Cero LLM.
- Salida ÚNICAMENTE a `data/experiment/metricas_intrinsecas/` (un JSON por
  grafo). Los artefactos de custodia (re-ensamblados de verificación) van a
  /tmp, nunca al repo.
- Reproducible enteramente desde archivos del repositorio + PDFs del subset.

Método de atribución nodo→chunk (auditoría de custodia U0, replicada acá):
1. CUSTODIA: se re-corre el ensamblador REAL (assemble.py / assemble_v3.py,
   importados sin modificación) desde el caché, con salida a /tmp, y se
   verifica igualdad exacta de ids de nodos y triples de aristas contra el
   kg.json congelado. Si la custodia falla, el script aborta: ninguna
   atribución es válida sobre un grafo que el caché no reproduce.
2. MAPEO: una réplica mínima del loop de entidades de cada ensamblador
   (usando las MISMAS funciones de slug importadas) produce, por chunk, las
   menciones extraídas y el gid al que cada una mapea. De ahí salen:
   menciones_fusionadas por nodo (M3), rol del chunk creador por nodo (M7 en
   v2; en v3 el campo `rol_fuente` ya viene en el kg), y aporte por chunk
   (M10). La réplica se valida por igualdad de conjuntos contra el kg real.

Grafos: grafo_v2 (defecto de ensamblado), reensamblado_v3, run_3_ppf_core.
Para run_3, M3/M7/M10 se reportan no_computable (pipeline de otra fase, sin
caché en el formato de cache_v2 ni vocabulario de roles aplicable).

Uso:
    .venv/bin/python scripts/metricas_intrinsecas.py
"""

from __future__ import annotations

import hashlib
import json
import math
import re
import sys
import unicodedata
from collections import deque
from datetime import date
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parents[1]
V2_CODE = REPO / "data" / "experiment" / "grafo_v2" / "code"
sys.path.insert(0, str(V2_CODE))

from rapidfuzz import fuzz, process  # noqa: E402

import chunk_roles as CR  # noqa: E402
import assemble as A2  # noqa: E402  (ensamblador v2 real: build_skeleton, entity_slug)
import assemble_v3 as A3  # noqa: E402  (ensamblador v3 real: entity_slug_v3, cargar_chunks_con_rol)

SPEC = REPO / "docs" / "spec_evaluacion_intrinseca.md"
SPEC_COMMIT = "cdf90e6"  # commit de sellado del pre-registro
OUT_DIR = REPO / "data" / "experiment" / "metricas_intrinsecas"
TMP_DIR = Path("/tmp/metricas_intrinsecas_custodia")

KG_V2 = REPO / "data" / "experiment" / "grafo_v2" / "kg.json"
KG_V3 = REPO / "data" / "experiment" / "grafo_v2" / "reensamblado_v3" / "kg.json"
KG_R3 = REPO / "data" / "experiment" / "run_3_ppf_core" / "kg.json"
CACHE_FULL = V2_CODE / "cache_v2" / "full"
CUARENTENA_V2 = REPO / "data" / "experiment" / "grafo_v2" / "cuarentena.json"

UMBRAL_SIMILITUD = 75.0  # protocolo de [05] §5.1 (spec §4, filas M1/M2)
ROLES_NO_NORMATIVOS = {CR.ROL_INDICE, CR.ROL_TABLA}  # rol normativo = cuerpo (spec §4 M7)


# ----------------------------------------------------------------------------
# Utilidades
# ----------------------------------------------------------------------------

def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def cargar_kg(p: Path) -> tuple[list[dict], list[dict]]:
    kg = json.loads(p.read_text(encoding="utf-8"))
    return kg["nodes"], kg["edges"]


def normalizar_superficie(s: str) -> str:
    """Normalización de superficie de M2 (spec §4): minúsculas, sin tildes,
    colapso de espacios y puntuación. SIN dominancia de substring (la
    similitud es `ratio` sobre cadenas completas)."""
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", " ", s).strip()
    return s


# ----------------------------------------------------------------------------
# Clustering de similitud (M1 / M2)
# ----------------------------------------------------------------------------

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[max(ra, rb)] = min(ra, rb)


def conteo_duplicados(nodes: list[dict], scorer, key_fn) -> tuple[int, dict[str, int], int]:
    """Protocolo de [05] §5.1 etapa 1: pares intra-tipo con similitud >= 75,
    grafo de similitud no dirigido, clusters = componentes conexas,
    conteo = Σ (|C| - 1). Devuelve (conteo_total, conteo_por_tipo, labels_vacios)."""
    por_tipo: dict[str, list[str]] = {}
    vacios = 0
    for n in nodes:
        key = key_fn(n.get("label", "") or "")
        if key == "":
            vacios += 1
        por_tipo.setdefault(n["type"], []).append(key)

    total = 0
    por_tipo_out: dict[str, int] = {}
    for t, labels in sorted(por_tipo.items()):
        m = len(labels)
        if m < 2:
            continue
        # Matriz de similitud intra-tipo (C-backed, determinística).
        matriz = process.cdist(labels, labels, scorer=scorer, dtype=None)
        uf = UnionFind(m)
        for i in range(m):
            fila = matriz[i]
            for j in range(i + 1, m):
                if fila[j] >= UMBRAL_SIMILITUD:
                    uf.union(i, j)
        tam: dict[int, int] = {}
        for i in range(m):
            r = uf.find(i)
            tam[r] = tam.get(r, 0) + 1
        c = sum(sz - 1 for sz in tam.values() if sz > 1)
        if c:
            por_tipo_out[t] = c
        total += c
    return total, por_tipo_out, vacios


# ----------------------------------------------------------------------------
# Métricas estructurales (M4, M5, M6, M8, M9)
# ----------------------------------------------------------------------------

def estructura(nodes: list[dict], edges: list[dict]) -> dict[str, Any]:
    """Aristas únicas por triple exacto, grados, componentes, caminos.
    Convenciones fijadas en la spec §4 (M4/M5/M8): dedup por
    (source, target, relation); self-loops conservados (aportan 2 al grado,
    excluidos del numerador de densidad); M5 sobre la componente conexa mayor
    de la versión no dirigida."""
    ids = [n["id"] for n in nodes]
    id_set = set(ids)
    ids_duplicados = len(ids) - len(id_set)
    N = len(ids)  # nodos totales = entradas de la lista (spec: nodos del grafo)

    unicas: set[tuple[str, str, str]] = set()
    repetidas = 0
    dangling = 0
    for e in edges:
        k = (e["source"], e["target"], e["relation"])
        if k in unicas:
            repetidas += 1
            continue
        unicas.add(k)
        if e["source"] not in id_set or e["target"] not in id_set:
            dangling += 1

    self_loops = sum(1 for (s, t, _r) in unicas if s == t)

    grado: dict[str, int] = {i: 0 for i in id_set}
    ady: dict[str, set[str]] = {i: set() for i in id_set}
    for (s, t, _r) in unicas:
        if s in grado:
            grado[s] += 1
        if t in grado:
            grado[t] += 1
        # (self-loop: s == t suma 2 al mismo nodo, convención M4)
        if s in ady and t in ady and s != t:
            ady[s].add(t)
            ady[t].add(s)

    suma_grados = sum(grado.values())

    # Componentes conexas (no dirigido, aristas únicas).
    visto: set[str] = set()
    componentes: list[list[str]] = []
    for nid in sorted(id_set):
        if nid in visto:
            continue
        comp = []
        q = deque([nid])
        visto.add(nid)
        while q:
            u = q.popleft()
            comp.append(u)
            for v in ady[u]:
                if v not in visto:
                    visto.add(v)
                    q.append(v)
        componentes.append(comp)
    componentes.sort(key=len, reverse=True)
    mayor = componentes[0] if componentes else []
    aislados = sum(1 for nid in id_set if grado[nid] == 0)

    # M5: BFS todo-pares sobre la componente mayor (pares ordenados distintos).
    suma_dist = 0
    n_lcc = len(mayor)
    lcc_set = set(mayor)
    for src in mayor:
        dist = {src: 0}
        q = deque([src])
        while q:
            u = q.popleft()
            du = dist[u]
            for v in ady[u]:
                if v not in dist:
                    dist[v] = du + 1
                    q.append(v)
        suma_dist += sum(d for nid, d in dist.items() if nid != src and nid in lcc_set)
    pares_lcc = n_lcc * (n_lcc - 1)

    # M6: concentración de grado.
    grados_orden = sorted(grado.values())  # ascendente
    k_top = max(1, math.ceil(0.01 * N))
    top = sorted(grado.values(), reverse=True)[:k_top]
    suma_top = sum(top)
    n = len(grados_orden)
    if suma_grados > 0 and n > 0:
        gini = sum((2 * (i + 1) - n - 1) * x for i, x in enumerate(grados_orden)) / (n * suma_grados)
    else:
        gini = 0.0

    return {
        "N": N,
        "ids_duplicados": ids_duplicados,
        "aristas_unicas": len(unicas),
        "aristas_repetidas_removidas": repetidas,
        "aristas_dangling": dangling,
        "self_loops": self_loops,
        "suma_grados": suma_grados,
        "grado_max": max(grado.values()) if grado else 0,
        "k_top1pct": k_top,
        "suma_grados_top1pct": suma_top,
        "gini_grado": gini,
        "aislados": aislados,
        "n_componentes": len(componentes),
        "n_lcc": n_lcc,
        "suma_dist_lcc": suma_dist,
        "pares_lcc": pares_lcc,
    }


# ----------------------------------------------------------------------------
# Custodia (método U0): el ensamblador real reproduce el kg congelado
# ----------------------------------------------------------------------------

def custodia_v2() -> dict[str, Any]:
    out = TMP_DIR / "v2"
    out.mkdir(parents=True, exist_ok=True)
    A2.assemble(CACHE_FULL, out / "kg.json", out / "report.json", out / "cuarentena.json")
    nodes_r, edges_r = cargar_kg(out / "kg.json")
    nodes_f, edges_f = cargar_kg(KG_V2)
    return _comparar("grafo_v2", nodes_r, edges_r, nodes_f, edges_f)


def custodia_v3() -> dict[str, Any]:
    out = TMP_DIR / "v3"
    out.mkdir(parents=True, exist_ok=True)
    original = A3.OUT_DIR
    try:
        A3.OUT_DIR = out
        A3.assemble_v3(A3.ROLES_DEFAULT)
    finally:
        A3.OUT_DIR = original
    nodes_r, edges_r = cargar_kg(out / "kg.json")
    nodes_f, edges_f = cargar_kg(KG_V3)
    return _comparar("reensamblado_v3", nodes_r, edges_r, nodes_f, edges_f)


def _comparar(nombre: str, nodes_r, edges_r, nodes_f, edges_f) -> dict[str, Any]:
    ids_r = sorted(n["id"] for n in nodes_r)
    ids_f = sorted(n["id"] for n in nodes_f)
    tr_r = sorted((e["source"], e["target"], e["relation"]) for e in edges_r)
    tr_f = sorted((e["source"], e["target"], e["relation"]) for e in edges_f)
    ok = ids_r == ids_f and tr_r == tr_f
    if not ok:
        raise RuntimeError(
            f"CUSTODIA FALLIDA ({nombre}): el ensamblador real no reproduce el kg congelado "
            f"(nodos {len(ids_r)} vs {len(ids_f)}, aristas {len(tr_r)} vs {len(tr_f)}). "
            f"Ninguna atribución nodo→chunk es válida; FRENO."
        )
    return {"grafo": nombre, "custodia": "OK",
            "nodos": len(ids_f), "aristas_triples": len(tr_f)}


# ----------------------------------------------------------------------------
# Mapeo mención→nodo (réplica mínima del loop de entidades de cada ensamblador)
# ----------------------------------------------------------------------------

def stream_v2(chunks_con_rol: list[dict]) -> tuple[list[dict], dict[str, str]]:
    """Reproduce la selección de resultados del ensamblado v2 (glob ordenado,
    agrupar por chunk_id, desempate por (entities, relations)) — assemble.py.
    Devuelve (resultados_elegidos, rol_por_nombre_de_archivo)."""
    rol_por_archivo = {c["_cache_path"].name: c["rol"] for c in chunks_con_rol}
    files = sorted(CACHE_FULL.glob("*.json"))
    grupos: dict[str, list[tuple[str, dict]]] = {}
    for fp in files:
        data = json.loads(fp.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or "chunk_id" not in data:
            continue
        grupos.setdefault(data["chunk_id"], []).append((fp.name, data))
    elegidos: list[dict] = []
    for cid, group in grupos.items():
        if len(group) == 1:
            fn, data = group[0]
        else:
            valid = [(f, d) for f, d in group if not d.get("error")]
            if not valid:
                fn, data = group[0]
            else:
                fn, data = max(valid, key=lambda fd: (len(fd[1].get("entities", [])),
                                                      len(fd[1].get("relations", []))))
        data["_archivo"] = fn
        elegidos.append(data)
    return elegidos, rol_por_archivo


def mapear_menciones(resultados: list[dict], rol_por_archivo: dict[str, str],
                     slug_fn, node_ids: set[str]) -> dict[str, Any]:
    """Loop de entidades replicado: menciones válidas → gid. Cuenta menciones
    por gid, primer chunk creador por gid, y aporte por chunk."""
    menciones_por_gid: dict[str, int] = {}
    rol_creador: dict[str, str] = {}
    aporte_por_chunk: list[dict[str, Any]] = []
    menciones_tipo_invalido = 0
    gids_fuera_del_kg: set[str] = set()
    vistos: set[str] = set()

    for data in resultados:
        rol = rol_por_archivo[data["_archivo"]]
        gids_chunk: set[str] = set()
        n_menciones = 0
        if not data.get("error"):
            for e in data.get("entities", []):
                etype = e.get("type")
                if etype not in A2.ENTITY_TYPES:
                    menciones_tipo_invalido += 1
                    continue
                n_menciones += 1
                if etype == "TextoOrdenado":
                    e.setdefault("properties", {}).setdefault("archivo", data.get("doc", ""))
                gid = f"{etype}_{slug_fn(e)}"
                menciones_por_gid[gid] = menciones_por_gid.get(gid, 0) + 1
                if gid not in vistos:
                    vistos.add(gid)
                    rol_creador[gid] = rol
                if gid in node_ids:
                    gids_chunk.add(gid)
                else:
                    gids_fuera_del_kg.add(gid)
        aporte_por_chunk.append({
            "chunk_id": data["chunk_id"], "archivo": data["_archivo"], "rol": rol,
            "menciones_validas": n_menciones, "nodos_alcanzados": len(gids_chunk),
        })
    return {
        "menciones_por_gid": menciones_por_gid,
        "rol_creador": rol_creador,
        "aporte_por_chunk": aporte_por_chunk,
        "menciones_tipo_invalido": menciones_tipo_invalido,
        "gids_fuera_del_kg": sorted(gids_fuera_del_kg),
    }


def denominador_menciones(chunks_con_rol: list[dict]) -> dict[str, int]:
    """M3, denominador: menciones de entidad extraídas totales en el caché
    (508 resultados, sin los que terminaron en error) — aguas arriba de todo
    ensamblado, compartido por v2 y v3."""
    total = 0
    con_error = 0
    for c in chunks_con_rol:
        data = json.loads(c["_cache_path"].read_text(encoding="utf-8"))
        if data.get("error"):
            con_error += 1
            continue
        total += len(data.get("entities", []))
    return {"menciones_totales": total, "chunks_con_error": con_error,
            "chunks_en_cache": len(chunks_con_rol)}


# ----------------------------------------------------------------------------
# Armado del reporte por grafo
# ----------------------------------------------------------------------------

def _met(valor, numerador, denominador, convencion, cota, notas) -> dict[str, Any]:
    return {"valor": valor, "numerador": numerador, "denominador": denominador,
            "convencion": convencion, "cota": cota, "notas": notas}


def _no_computable(motivo: str) -> dict[str, Any]:
    return {"status": "no_computable", "motivo": motivo}


def medir_grafo(nombre: str, kg_path: Path,
                atribucion: dict[str, Any] | None,
                denominador_m3: dict[str, int] | None,
                roles_chunks: list[dict] | None,
                rol_nodos_extra: dict[str, str] | None) -> dict[str, Any]:
    """Computa M1..M10 para un grafo. `atribucion` (mapeo mención→nodo),
    `denominador_m3` y `roles_chunks` son None para grafos sin caché v2
    (run_3) → M3/M7/M10 no_computable."""
    nodes, edges = cargar_kg(kg_path)
    est = estructura(nodes, edges)
    N = est["N"]

    m1_num, m1_por_tipo, vacios_raw = conteo_duplicados(
        nodes, fuzz.partial_ratio, key_fn=lambda s: s)
    m2_num, m2_por_tipo, vacios_norm = conteo_duplicados(
        nodes, fuzz.ratio, key_fn=normalizar_superficie)

    metricas: dict[str, Any] = {}
    metricas["M1_tasa_duplicacion_publicada"] = _met(
        round(m1_num / N, 6), m1_num, N,
        "partial_ratio RapidFuzz sobre label crudo, pares intra-tipo >= 75, "
        "componentes conexas, Σ(|C|-1) / nodos totales ([05] §5.1, etapa 1)",
        "superior", {
            "por_tipo": m1_por_tipo,
            "labels_vacios": vacios_raw,
            "rol": "descriptiva; DECLARADA INFLADA para este corpus (spec §5.b)",
        })
    metricas["M2_tasa_duplicacion_gate"] = _met(
        round(m2_num / N, 6), m2_num, N,
        "ratio RapidFuzz (Levenshtein normalizado, cadenas completas) sobre label "
        "con normalización de superficie (minúsculas, sin tildes, colapso de "
        "espacios/puntuación), >= 75, mismo clustering que M1",
        "superior", {
            "por_tipo": m2_por_tipo,
            "labels_vacios_tras_normalizar": vacios_norm,
            "rol": "bloqueante en la pasada 2",
        })

    if atribucion is None:
        metricas["M3_tasa_conflacion"] = _no_computable(
            "run_3 es de otro pipeline (Fase 2.2): sin caché de extracción en el "
            "formato de cache_v2, no hay conteo de menciones pre-fusión atribuible")
    else:
        menciones = atribucion["menciones_por_gid"]
        node_ids = {n["id"] for n in nodes}
        m3_num = sum(m - 1 for gid, m in menciones.items() if gid in node_ids and m > 1)
        den = denominador_m3["menciones_totales"]
        metricas["M3_tasa_conflacion"] = _met(
            round(m3_num / den, 6), m3_num, den,
            "Σ max(menciones_fusionadas - 1, 0) sobre nodos del grafo / menciones de "
            "entidad extraídas totales del caché (508 resultados sin error; aguas "
            "arriba, compartido por v2 y v3). Nodos sin mención extraída (esqueleto, "
            "sujetos propuestos) aportan 0. Menciones = entidades de tipo válido.",
            "superior (de sobre-fusión: parte de las fusiones son legítimas)", {
                "rol": "bloqueante en la pasada 2",
                "nodos_con_fusion": sum(1 for gid, m in menciones.items()
                                        if gid in node_ids and m > 1),
                "menciones_tipo_invalido_excluidas": atribucion["menciones_tipo_invalido"],
                "chunks_con_error_en_cache": denominador_m3["chunks_con_error"],
            })

    metricas["M4_average_degree"] = _met(
        round(est["suma_grados"] / N, 6), est["suma_grados"], N,
        "aristas deduplicadas por triple exacto (source, target, relation); grado = "
        "entrantes + salientes; self-loops aportan 2; average = Σ grados / nodos",
        "exacta", {
            "aristas_unicas": est["aristas_unicas"],
            "aristas_repetidas_removidas": est["aristas_repetidas_removidas"],
            "self_loops": est["self_loops"],
            "aristas_dangling": est["aristas_dangling"],
            "ids_de_nodo_duplicados": est["ids_duplicados"],
            "rol": "descriptiva; NO se reporta sin M6",
        })
    metricas["M5_avg_shortest_path"] = _met(
        round(est["suma_dist_lcc"] / est["pares_lcc"], 6) if est["pares_lcc"] else None,
        est["suma_dist_lcc"], est["pares_lcc"],
        "BFS no ponderado sobre la versión no dirigida del grafo de aristas únicas, "
        "solo componente conexa mayor, promedio sobre pares ordenados distintos; "
        "nodos fuera de la componente mayor excluidos y reportados vía M9",
        "exacta", {
            "n_componente_mayor": est["n_lcc"],
            "nodos_fuera_de_lcc": N - est["n_lcc"],
            "rol": "descriptiva; NO se reporta sin M6 ni M9",
        })
    metricas["M6_concentracion_de_grado"] = _met(
        {"grado_max": est["grado_max"],
         "participacion_top1pct": round(est["suma_grados_top1pct"] / est["suma_grados"], 6)
         if est["suma_grados"] else None,
         "gini_grado": round(est["gini_grado"], 6)},
        est["suma_grados_top1pct"], est["suma_grados"],
        "top 1% = techo(0.01·N) nodos de mayor grado; participación = Σ grados top / "
        "Σ grados; Gini sobre la distribución de grados de M4",
        "exacta", {
            "k_top1pct": est["k_top1pct"],
            "rol": "descriptiva de reporte OBLIGATORIO junto a M4 y M5; "
                   "especie del backlog: hub_contaminado",
        })

    if atribucion is None:
        metricas["M7_tasa_ruido_por_rol"] = _no_computable(
            "run_3 es de otro pipeline: chunk_roles.py reproduce el chunker de "
            "grafo_v2; los chunks de run_3 no tienen rol documental atribuible")
    else:
        node_ids = {n["id"] for n in nodes}
        if rol_nodos_extra is not None:
            rol_de_nodo = rol_nodos_extra
        else:
            rol_de_nodo = {n["id"]: n.get("rol_fuente", "") for n in nodes}
        m7_detalle: dict[str, int] = {}
        m7_nodos: list[str] = []
        for nid in sorted(node_ids):
            rol = rol_de_nodo.get(nid, "")
            if rol in ROLES_NO_NORMATIVOS:
                m7_detalle[rol] = m7_detalle.get(rol, 0) + 1
                m7_nodos.append(nid)
        m7_num = len(m7_nodos)
        metricas["M7_tasa_ruido_por_rol"] = _met(
            round(m7_num / N, 6), m7_num, N,
            "nodos cuyo chunk de origen tiene rol documental no normativo "
            "(indice, tabla_norma_origen; rol normativo = cuerpo — vocabulario real "
            "de chunk_roles.py); nodos sin chunk (esqueleto) no cuentan en el numerador",
            "inferior (no captura cáscaras nacidas de chunks normativos)", {
                "por_rol": m7_detalle,
                "nodos": m7_nodos,
                "rol": "bloqueante en la pasada 2; especie del backlog: cascara",
            })

    metricas["M8_densidad"] = _met(
        round((est["aristas_unicas"] - est["self_loops"]) / (N * (N - 1)), 8),
        est["aristas_unicas"] - est["self_loops"], N * (N - 1),
        "densidad de grafo dirigido simple: aristas únicas sin self-loops / N·(N-1)",
        "exacta", {"rol": "descriptiva"})
    metricas["M9_nodos_aislados_y_componentes"] = _met(
        {"nodos_aislados": est["aislados"],
         "componentes_conexas": est["n_componentes"],
         "fraccion_en_componente_mayor": round(est["n_lcc"] / N, 6)},
        est["n_lcc"], N,
        "versión no dirigida del grafo de aristas únicas; aislados = grado 0; "
        "fracción = nodos de la componente mayor / nodos totales",
        "exacta", {"rol": "descriptiva; reporte obligatorio junto a M5"})

    if atribucion is None or roles_chunks is None:
        metricas["M10_chunks_mudos"] = _no_computable(
            "run_3 es de otro pipeline: sin roles documentales ni atribución "
            "chunk→nodo replicable desde cache_v2 (misma razón que M3/M7)")
    else:
        aportes = atribucion["aporte_por_chunk"]
        activos = [a for a in aportes if a["rol"] == CR.ROL_CUERPO]
        elegidos_archivos = {a["archivo"] for a in aportes}
        # Chunks de cuerpo del corpus que NI SIQUIERA entraron al ensamblado
        # (descartados por el desempate de v2): mudos por construcción.
        descartados_cuerpo = [
            {"chunk_id": c["chunk_id"], "archivo": c["_cache_path"].name,
             "rol": c["rol"], "menciones_validas": None, "nodos_alcanzados": 0,
             "motivo": "descartado_por_desempate"}
            for c in roles_chunks
            if c["rol"] == CR.ROL_CUERPO and c["_cache_path"].name not in elegidos_archivos
        ]
        mudos = [a for a in activos if a["nodos_alcanzados"] == 0] + descartados_cuerpo
        den_m10 = sum(1 for c in roles_chunks if c["rol"] == CR.ROL_CUERPO)
        metricas["M10_chunks_mudos"] = _met(
            round(len(mudos) / den_m10, 6), len(mudos), den_m10,
            "chunk activo = chunk de entrada a extracción con rol cuerpo (spec §4 "
            "M10); mudo = ninguna mención del chunk mapea a un nodo presente en el "
            "grafo (incluye chunks descartados antes del ensamblado); denominador = "
            "chunks de cuerpo de chunks_all.json (aguas arriba)",
            "exacta", {
                "mudos_detalle": [{k: v for k, v in m.items() if k != "archivo"}
                                  for m in mudos],
                "dirección_de_mejora": "cero",
                "rol": "bloqueante en la pasada 2",
            })

    metricas["M11_cobertura_CQ"] = {
        "status": "no_medida_en_esta_unidad",
        "motivo": "régimen especial de la spec §6: medición única y separada sobre el "
                  "set quemado; jamás objetivo de optimización",
    }
    return {"grafo": nombre, "kg_path": str(kg_path.relative_to(REPO)),
            "nodos_totales": N, "metricas": metricas}


# ----------------------------------------------------------------------------
# main
# ----------------------------------------------------------------------------

def main() -> int:
    import rapidfuzz

    print("== Custodia (método U0): el ensamblador real reproduce el kg congelado ==",
          flush=True)
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    cust = [custodia_v2(), custodia_v3()]
    for c in cust:
        print(f"  {c['grafo']}: {c['custodia']} "
              f"({c['nodos']} nodos, {c['aristas_triples']} triples)", flush=True)

    print("== Roles documentales y mapeo mención→nodo ==", flush=True)
    chunks_con_rol = A3.cargar_chunks_con_rol()
    den_m3 = denominador_menciones(chunks_con_rol)

    # --- v2: stream con desempate replicado + slug v2 ---
    nodes_v2, _ = cargar_kg(KG_V2)
    ids_v2 = {n["id"] for n in nodes_v2}
    elegidos_v2, rol_por_archivo = stream_v2(chunks_con_rol)
    atr_v2 = mapear_menciones(elegidos_v2, rol_por_archivo,
                              A2.entity_slug, ids_v2)
    # Validación de la réplica: todo gid mapeado debe existir en el kg real.
    if atr_v2["gids_fuera_del_kg"]:
        raise RuntimeError(
            f"Réplica v2 inválida: {len(atr_v2['gids_fuera_del_kg'])} gids mapeados "
            f"no existen en kg.json. Primeros: {atr_v2['gids_fuera_del_kg'][:5]}. FRENO.")
    # Rol de los Sujeto_propuesto de v2: primer chunk_id de cuarentena.json.
    rol_por_chunk_id = {a["chunk_id"]: a["rol"] for a in atr_v2["aporte_por_chunk"]}
    rol_nodos_v2 = dict(atr_v2["rol_creador"])
    for reg in json.loads(CUARENTENA_V2.read_text(encoding="utf-8")):
        if reg["chunk_ids"]:
            rol_nodos_v2[reg["id"]] = rol_por_chunk_id.get(reg["chunk_ids"][0], "")

    # --- v3: chunks activos (cuerpo + tabla) + slug v3 ---
    nodes_v3, _ = cargar_kg(KG_V3)
    ids_v3 = {n["id"] for n in nodes_v3}
    activos_v3 = []
    for c in chunks_con_rol:
        if c["rol"] not in A3.ROLES_DEFAULT:
            continue
        data = json.loads(c["_cache_path"].read_text(encoding="utf-8"))
        data["_archivo"] = c["_cache_path"].name
        activos_v3.append(data)
    atr_v3 = mapear_menciones(activos_v3, rol_por_archivo,
                              lambda e: A3.entity_slug_v3(e), ids_v3)
    if atr_v3["gids_fuera_del_kg"]:
        raise RuntimeError(
            f"Réplica v3 inválida: {len(atr_v3['gids_fuera_del_kg'])} gids mapeados "
            f"no existen en kg.json. Primeros: {atr_v3['gids_fuera_del_kg'][:5]}. FRENO.")

    print("== Métricas por grafo ==", flush=True)
    script_hash = sha256_file(Path(__file__))
    meta = {
        "spec": str(SPEC.relative_to(REPO)),
        "spec_commit_sellado": SPEC_COMMIT,
        "spec_sha256": sha256_file(SPEC),
        "script_sha256": script_hash,
        "rapidfuzz_version": rapidfuzz.__version__,
        "umbral_similitud": UMBRAL_SIMILITUD,
        "fecha": date.today().isoformat(),
        "custodia": cust,
    }

    trabajos = [
        ("grafo_v2", KG_V2, atr_v2, den_m3, chunks_con_rol, rol_nodos_v2),
        ("reensamblado_v3", KG_V3, atr_v3, den_m3, chunks_con_rol, None),
        ("run_3_ppf_core", KG_R3, None, None, None, None),
    ]
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for nombre, path, atr, den, roles, rol_extra in trabajos:
        print(f"  midiendo {nombre}...", flush=True)
        rep = medir_grafo(nombre, path, atr, den, roles, rol_extra)
        rep = {**meta, **rep}
        out = OUT_DIR / f"{nombre}.json"
        out.write_text(json.dumps(rep, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"  -> {out.relative_to(REPO)}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
