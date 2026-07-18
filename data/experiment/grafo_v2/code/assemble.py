"""Ensambla kg.json a partir de los resultados cacheados por chunk.

Aprendizajes Run 1 + Run 2:
- Dedup por slug normalizado (lowercase, sin acentos, sin espacios → underscore).
- IDs únicos: <tipo>_<slug>. Si colisionan tipo+slug, se mergea (first-write-wins para
  properties, primera provenance vista).
- Validación adicional contra DOMAIN_RANGE en el ensamblaje (defensa en profundidad).
- provenance OBLIGATORIA en cada nodo y cada edge (protocolo b).

Uso:
    python assemble.py smoke    # ensambla desde cache/smoke/
    python assemble.py full     # ensambla desde cache/full/
"""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any

from schema import DOMAIN_RANGE, ENTITY_TYPES, PREDICATES, is_valid_triple


RUN_DIR = Path(__file__).resolve().parents[1]
CACHE_DIR = RUN_DIR / "code" / "cache"


# Materias asignadas por nombre de archivo
DOC_MATERIA = {
    "TO_capitales_minimos_actual.pdf": "capitales_minimos",
    "TO_clasificacion_deudores_actual.pdf": "clasificacion_deudores",
    "TO_exterior_cambios_actual.pdf": "exterior_cambios",
    "TO_proteccion_usuarios_servicios_financieros_actual.pdf": "proteccion_usuarios",
    "TO_regimen_informativo_contable_mensual_actual.pdf": "regimen_informativo",
}


def slugify(s: str, max_len: int = 80) -> str:
    """Normaliza a slug: lowercase, sin acentos, ascii, _ entre palabras."""
    if not s:
        return "empty"
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "_", s)
    s = s.strip("_")
    if not s:
        return "empty"
    return s[:max_len]


# Stopwords que NO se singularizan (palabras cortas, articulos, preposiciones, palabras que terminan en 's' sin ser plural)
_SINGULARIZE_SKIP = {
    "los", "las", "des", "tres", "seis", "mas", "es", "los", "las", "es",
    "bcra", "alyc", "epe", "efnb", "sa", "srl",
}


# Consonantes que pueden terminar legítimamente un sustantivo singular en castellano
# (red, mes, ciudad, vez, reloj, sol, an[i]mal, etc). NO incluye t, p, k, b porque
# son raras en posición final en español; 'clientes'→'client' sería falso positivo.
_VALID_SINGULAR_END_CONSONANTS = set("lnrdzjcg")


def _singularize_word(w: str) -> str:
    """Heurística best-effort para singularizar castellano.

    Reglas:
    1. Palabras < 4 chars o en stopwords: no tocar.
    2. Si termina en 'es' y al quitar 'es' queda terminación consonante válida
       (red, entidad, camion, comision): quitar 'es'.
    3. Si termina en 's' (incluido 'es' que no cumple regla 2): quitar solo 's'.

    Casos correctos: bancos→banco, entidades→entidad, clientes→cliente,
    sujetos→sujeto, redes→red, comisiones→comision, usuarios→usuario.
    """
    if len(w) < 4:
        return w
    if w in _SINGULARIZE_SKIP:
        return w
    if not w.endswith("s"):
        return w
    if w.endswith("es") and len(w) > 4:
        candidate = w[:-2]
        if candidate and candidate[-1] in _VALID_SINGULAR_END_CONSONANTS:
            return candidate
    return w[:-1]


def singularize_slug(slug: str) -> str:
    """Aplica singularización a cada palabra del slug."""
    return "_".join(_singularize_word(w) for w in slug.split("_") if w)


def entity_slug(entity: dict[str, Any]) -> str:
    """Slug clave para dedup por tipo de entidad."""
    t = entity["type"]
    props = entity.get("properties", {})
    label = entity.get("label", "")
    if t == "Comunicacion":
        code = props.get("codigo") or props.get("numero") or label
        return slugify(str(code))
    if t == "TextoOrdenado":
        # Dedup por archivo (invariante por PDF), NO por materia (text-libre del LLM).
        # Esto garantiza exactamente 1 TextoOrdenado por PDF.
        archivo = props.get("archivo") or props.get("_doc") or ""
        if not archivo:
            archivo = props.get("materia") or label
        return slugify(str(archivo))
    if t == "EntidadFinanciera":
        # H2a: dedup por LABEL normalizado (no por categoria), con singularización.
        # Label es la forma canónica que el LLM da; categoria es text-libre auxiliar.
        # Si label viene vacío, fallback a categoria.
        base = label or props.get("categoria", "")
        return singularize_slug(slugify(str(base)))
    if t == "Operacion":
        tipo = props.get("tipo") or label
        return slugify(str(tipo))
    if t in ("Restriccion", "Obligacion", "Excepcion"):
        # Estos son hechos normativos concretos: cada extracción es prácticamente única.
        # Slug = type + descripción acortada para que rara vez colisione, salvo paráfrasis casi exactas.
        desc = props.get("descripcion") or label
        return slugify(str(desc), max_len=80)
    return slugify(label)


def assemble(cache_root: Path, kg_out: Path, report_out: Path) -> dict[str, Any]:
    """Lee todos los chunks cacheados en cache_root y ensambla kg.json."""
    files = sorted(cache_root.glob("*.json"))
    if not files:
        raise RuntimeError(f"No hay archivos en {cache_root}")

    # ----------------------------------------------------------------
    # Dedup por chunk_id: el chunker puede producir múltiples chunks con
    # el mismo chunk_id (ej. cuando "1.1." aparece varias veces en el texto:
    # una vez como header real, otras como referencias cruzadas). En el cache
    # quedan varios .json para el mismo chunk_id. Acá agrupamos y elegimos
    # el "mejor" — el que más entidades extrajo (asumido como el header real).
    # ----------------------------------------------------------------
    results_by_chunk_id: dict[str, list[dict[str, Any]]] = {}
    for fp in files:
        try:
            data = json.loads(fp.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"  WARN: no pude leer {fp.name}: {e}", flush=True)
            continue
        cid = data.get("chunk_id") or fp.stem
        results_by_chunk_id.setdefault(cid, []).append(data)

    best_results: list[dict[str, Any]] = []
    dedup_redundant = 0
    for cid, group in results_by_chunk_id.items():
        if len(group) == 1:
            best_results.append(group[0])
            continue
        # Hay duplicados. Filtrar primero los que tuvieron error.
        valid = [r for r in group if not r.get("error")]
        if not valid:
            best_results.append(group[0])  # mantener uno para registro
            dedup_redundant += len(group) - 1
            continue
        # De los válidos, elegir el de más entidades (luego más relaciones).
        best = max(valid, key=lambda r: (len(r.get("entities", [])), len(r.get("relations", []))))
        best_results.append(best)
        dedup_redundant += len(group) - 1

    nodes_by_id: dict[str, dict[str, Any]] = {}
    edges_set: dict[tuple[str, str, str], dict[str, Any]] = {}  # (src, pred, tgt) → edge

    chunks_with_error = 0
    chunks_ok = 0
    chunks_total = 0

    raw_entities = 0
    raw_relations = 0
    dropped_invalid_type = 0
    dropped_invalid_predicate = 0
    dropped_dangling = 0
    dropped_domain_range = 0
    dropped_duplicate_edge = 0
    merged_entities = 0

    per_doc_chunks_with_content: dict[str, int] = {}
    per_doc_chunks_total: dict[str, int] = {}

    for data in best_results:
        chunks_total += 1
        doc = data.get("doc", "")
        location = data.get("location", "")
        per_doc_chunks_total[doc] = per_doc_chunks_total.get(doc, 0) + 1

        if data.get("error"):
            chunks_with_error += 1
            continue
        chunks_ok += 1

        local_to_global: dict[str, str] = {}

        entities = data.get("entities", [])
        relations = data.get("relations", [])

        if entities:
            per_doc_chunks_with_content[doc] = per_doc_chunks_with_content.get(doc, 0) + 1

        for e in entities:
            raw_entities += 1
            etype = e.get("type")
            if etype not in ENTITY_TYPES:
                dropped_invalid_type += 1
                continue
            # Inyectar archivo en properties de TextoOrdenado ANTES del slug
            # para que el dedup sea por archivo (1 nodo por PDF, garantizado).
            if etype == "TextoOrdenado":
                e_props = e.setdefault("properties", {})
                if "archivo" not in e_props and doc:
                    e_props["archivo"] = doc
            slug = entity_slug(e)
            gid = f"{etype}_{slug}"

            # H2a (extra): para EntidadFinanciera, si el gid no existe pero hay
            # un prefijo del slug (sin última palabra) que sí existe, mergear ahí.
            # Captura casos como "Sujetos obligados regulados" → "Sujetos obligados".
            # Conservador: solo prueba quitar la última palabra (1 nivel).
            if etype == "EntidadFinanciera" and gid not in nodes_by_id:
                tokens = slug.split("_")
                if len(tokens) >= 3:  # mínimo 2 palabras + 1 calificador para considerar truncar
                    truncated_slug = "_".join(tokens[:-1])
                    truncated_gid = f"EntidadFinanciera_{truncated_slug}"
                    if truncated_gid in nodes_by_id:
                        gid = truncated_gid
                        slug = truncated_slug

            local_to_global[e["local_id"]] = gid

            if gid in nodes_by_id:
                # Merge: first-write-wins para properties (no sobreescribimos),
                # pero acumulamos en `properties` los campos nuevos no vistos.
                existing = nodes_by_id[gid]
                for k, v in e.get("properties", {}).items():
                    if k not in existing["properties"]:
                        existing["properties"][k] = v
                merged_entities += 1
                continue

            # TextoOrdenado: si el chunk no trae materia, la inferimos del nombre de archivo
            props = dict(e.get("properties", {}))
            if etype == "TextoOrdenado":
                if "archivo" not in props and doc:
                    props["archivo"] = doc
                if "materia" not in props and doc in DOC_MATERIA:
                    props["materia"] = DOC_MATERIA[doc]
                if "version" not in props:
                    props["version"] = "vigente"

            nodes_by_id[gid] = {
                "id": gid,
                "type": etype,
                "label": e.get("label", ""),
                "properties": props,
                "provenance": {
                    "source_doc": doc,
                    "location": location,
                },
            }

        for r in relations:
            raw_relations += 1
            pred = r.get("predicate")
            if pred not in PREDICATES:
                dropped_invalid_predicate += 1
                continue
            src_local = r.get("source")
            tgt_local = r.get("target")
            src_gid = local_to_global.get(src_local)
            tgt_gid = local_to_global.get(tgt_local)
            if src_gid is None or tgt_gid is None:
                dropped_dangling += 1
                continue
            src_node = nodes_by_id.get(src_gid)
            tgt_node = nodes_by_id.get(tgt_gid)
            if src_node is None or tgt_node is None:
                dropped_dangling += 1
                continue
            if not is_valid_triple(src_node["type"], pred, tgt_node["type"]):
                dropped_domain_range += 1
                continue
            key = (src_gid, pred, tgt_gid)
            if key in edges_set:
                dropped_duplicate_edge += 1
                continue
            edges_set[key] = {
                "source": src_gid,
                "target": tgt_gid,
                "relation": pred,
                "provenance": {
                    "source_doc": doc,
                    "location": location,
                },
            }

    # ============================================================
    # Pasada post-hoc: dedup de EntidadFinanciera por `categoria` normalizada.
    # Cuando el LLM produce dos labels distintos (ej. "Otros proveedores no
    # financieros de crédito" vs "Proveedores no financieros de crédito") pero
    # asigna la MISMA categoria, son la misma entidad regulatoria. Mergeamos.
    # Aplica solo a EntidadFinanciera (otros tipos no tienen `categoria`).
    # ============================================================
    ef_groups: dict[str, list[str]] = {}
    for gid, node in nodes_by_id.items():
        if node["type"] != "EntidadFinanciera":
            continue
        cat_raw = node["properties"].get("categoria", "")
        if not cat_raw:
            continue
        cat_norm = singularize_slug(slugify(str(cat_raw)))
        if not cat_norm:
            continue
        ef_groups.setdefault(cat_norm, []).append(gid)

    gid_redirect: dict[str, str] = {}
    ef_merged_by_categoria = 0
    for cat_norm, gids in ef_groups.items():
        if len(gids) <= 1:
            continue
        # Ganador: label más corto (más canónico). Empate → primer gid lexicográficamente.
        winner = min(gids, key=lambda g: (len(nodes_by_id[g]["label"]), g))
        win_node = nodes_by_id[winner]
        win_props = win_node["properties"]
        additional_provs: list[dict[str, Any]] = []
        for g in gids:
            if g == winner:
                continue
            loser = nodes_by_id[g]
            # Properties: union, ganador wins en conflictos
            for k, v in loser["properties"].items():
                if k not in win_props:
                    win_props[k] = v
            # Provenance: agregar la del perdedor al array adicional
            additional_provs.append(loser["provenance"])
            gid_redirect[g] = winner
            ef_merged_by_categoria += 1
        if additional_provs:
            existing_additional = win_node.get("additional_provenance", [])
            win_node["additional_provenance"] = existing_additional + additional_provs

    # Eliminar los nodos perdedores
    for loser_gid in gid_redirect:
        nodes_by_id.pop(loser_gid, None)

    # Redirigir edges que apunten a los gids perdedores
    edges_redirected = 0
    edges_dropped_after_redirect = 0
    new_edges_set: dict[tuple[str, str, str], dict[str, Any]] = {}
    for (src, pred, tgt), edge in edges_set.items():
        new_src = gid_redirect.get(src, src)
        new_tgt = gid_redirect.get(tgt, tgt)
        if new_src != src or new_tgt != tgt:
            edges_redirected += 1
        new_key = (new_src, pred, new_tgt)
        if new_key in new_edges_set:
            edges_dropped_after_redirect += 1
            continue
        edge["source"] = new_src
        edge["target"] = new_tgt
        new_edges_set[new_key] = edge
    edges_set = new_edges_set

    nodes = list(nodes_by_id.values())
    edges = list(edges_set.values())

    kg = {"nodes": nodes, "edges": edges}
    kg_out.parent.mkdir(parents=True, exist_ok=True)
    kg_out.write_text(json.dumps(kg, ensure_ascii=False, indent=2), encoding="utf-8")

    # Reporte de ensamblaje
    by_type: dict[str, int] = {}
    for n in nodes:
        by_type[n["type"]] = by_type.get(n["type"], 0) + 1
    by_relation: dict[str, int] = {}
    for ed in edges:
        by_relation[ed["relation"]] = by_relation.get(ed["relation"], 0) + 1

    coverage: dict[str, dict[str, Any]] = {}
    for d, total in per_doc_chunks_total.items():
        with_content = per_doc_chunks_with_content.get(d, 0)
        coverage[d] = {
            "chunks_total": total,
            "chunks_with_content": with_content,
            "coverage_pct": round(with_content / total * 100, 1) if total else 0.0,
        }

    report = {
        "cache_root": str(cache_root),
        "cache_files": len(files),
        "unique_chunk_ids": len(results_by_chunk_id),
        "redundant_cache_files_dedup": dedup_redundant,
        "chunks_total": chunks_total,
        "chunks_ok": chunks_ok,
        "chunks_with_error": chunks_with_error,
        "raw_entities": raw_entities,
        "raw_relations": raw_relations,
        "merged_entities": merged_entities,
        "ef_merged_by_categoria": ef_merged_by_categoria,
        "edges_redirected_after_ef_merge": edges_redirected,
        "edges_dropped_after_redirect": edges_dropped_after_redirect,
        "dropped_invalid_type": dropped_invalid_type,
        "dropped_invalid_predicate": dropped_invalid_predicate,
        "dropped_dangling": dropped_dangling,
        "dropped_domain_range": dropped_domain_range,
        "dropped_duplicate_edge": dropped_duplicate_edge,
        "nodes_total": len(nodes),
        "edges_total": len(edges),
        "density": round(len(edges) / max(len(nodes), 1), 3),
        "nodes_by_type": by_type,
        "edges_by_relation": by_relation,
        "coverage_by_doc": coverage,
    }
    report_out.parent.mkdir(parents=True, exist_ok=True)
    report_out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    return report


def main() -> int:
    if len(sys.argv) < 2 or sys.argv[1] not in ("smoke", "full"):
        print("Uso: python assemble.py {smoke|full}")
        return 1
    mode = sys.argv[1]
    cache_root = CACHE_DIR / mode

    if mode == "smoke":
        kg_out = RUN_DIR / "code" / "cache" / "kg_smoke.json"
        report_out = RUN_DIR / "code" / "cache" / "assemble_smoke.json"
    else:
        kg_out = RUN_DIR / "kg.json"
        report_out = RUN_DIR / "code" / "cache" / "assemble_full.json"

    report = assemble(cache_root, kg_out, report_out)
    print(f"\nEnsamblado {mode}:", flush=True)
    print(json.dumps(report, indent=2, ensure_ascii=False), flush=True)
    print(f"\nKG: {kg_out}", flush=True)
    print(f"Reporte: {report_out}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
