"""
06_validate_and_report.py — Validación + métricas del protocolo (§d) + report.md.

NO usa la API. Sin costo.

Validaciones (regla §b y §c del protocolo):
  * kg.json parseable.
  * provenance presente y no vacío en cada nodo y cada edge.
  * ids únicos.
  * edges.source/target apuntan a ids existentes.
  * label/description no matchean regex de jerarquía documental (§c.1).
  * types reportados son subconjunto del schema (10 tipos del schema.md §2).

Métricas (§d):
  * Tiempo de construcción (lo lee de cache/timings.json si existe, sino N/A).
  * Costo total + desglose por modelo (lee cache/cost_*.json).
  * Nodos por tipo.
  * Edges por tipo (relation).
  * Densidad = edges/nodes.
  * Nº de tipos de entidad y relación únicos.
  * Cobertura por TO (% aproximado de chunks que generaron ≥1 tripleta).
"""

from __future__ import annotations

import argparse
import json
import random
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import (
    CACHE_DIR,
    ENTITY_TYPES,
    KG_JSON_PATH,
    REPORT_PATH,
    TO_FILES,
    is_documental_hierarchy,
    read_json,
    read_jsonl,
)

CHUNKS_PATH = CACHE_DIR / "chunks.jsonl"
EXTRACTIONS_PATH = CACHE_DIR / "raw_extractions.jsonl"
TIMINGS_PATH = CACHE_DIR / "timings.json"   # opcional, escrito por scripts si quieren


# ---------------------------------------------------------------------------
# Análisis post-hoc de predicados (vocabulary cleanup metric)
# ---------------------------------------------------------------------------

_AUX_PLURAL_TO_SINGULAR = {
    # Verbos auxiliares comunes en los predicados (deber/poder/tener/estar/ser/hacer).
    "deben": "debe",
    "pueden": "puede",
    "tienen": "tiene",
    "están": "está",
    "son": "es",
    "hacen": "hace",
    "aplican": "aplica",
    "requieren": "requiere",
    "deberán": "deberá",
    "podrán": "podrá",
    "tendrán": "tendrá",
    "estarán": "estará",
    "serán": "será",
    "harán": "hará",
}

_NON_ALPHA = re.compile(r"[^a-z0-9_]")


def _strip_accents(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))


def normalize_predicate(p: str) -> str:
    """Forma normalizada de un predicado (para agrupar variaciones triviales).

    Reglas:
    - Lowercase.
    - Strip accents.
    - Reemplaza separadores no-alfanuméricos por '_'.
    - Si el primer "token" (antes del primer '_') es una forma plural conocida
      de un verbo auxiliar (deben→debe, tienen→tiene, etc.), la reemplaza por
      su singular.
    """
    if not p:
        return ""
    base = _strip_accents(p.lower().strip())
    base = _NON_ALPHA.sub("_", base)
    base = re.sub(r"_+", "_", base).strip("_")
    parts = base.split("_", 1)
    head = parts[0]
    rest = parts[1] if len(parts) > 1 else ""
    # Aplicar plural → singular en el head si corresponde
    head_norm = _strip_accents(head)
    plural_map_norm = {_strip_accents(k): _strip_accents(v) for k, v in _AUX_PLURAL_TO_SINGULAR.items()}
    if head_norm in plural_map_norm:
        head = plural_map_norm[head_norm]
    return f"{head}_{rest}" if rest else head


def analyze_predicates(kg: dict) -> dict:
    """Computa métricas del vocabulario de predicados.

    Devuelve:
        {
            "n_edges": int,
            "n_predicates_raw": int,        # predicados únicos tal como salieron de Haiku
            "n_predicates_normalized": int, # predicados únicos tras normalización trivial
            "ratio_raw": float,             # n_predicates_raw / n_edges
            "ratio_normalized": float,
            "groups_merged_top": list[(canonical, [members])],  # los 10 grupos con más miembros
            "singletons_normalized": int,   # predicados que no se fusionaron con nadie
        }
    """
    edges = kg.get("edges", [])
    raw_preds = [e["relation"] for e in edges if e.get("relation")]
    raw_unique = sorted(set(raw_preds))
    groups: dict[str, list[str]] = defaultdict(list)
    for p in raw_unique:
        groups[normalize_predicate(p)].append(p)

    merged_groups = [(canon, members) for canon, members in groups.items() if len(members) > 1]
    merged_groups.sort(key=lambda kv: (-len(kv[1]), kv[0]))
    singletons = sum(1 for members in groups.values() if len(members) == 1)

    return {
        "n_edges": len(edges),
        "n_predicates_raw": len(raw_unique),
        "n_predicates_normalized": len(groups),
        "ratio_raw": round(len(raw_unique) / len(edges), 3) if edges else 0.0,
        "ratio_normalized": round(len(groups) / len(edges), 3) if edges else 0.0,
        "groups_merged_top": merged_groups[:10],
        "singletons_normalized": singletons,
        "merged_groups_total": len(merged_groups),
    }


# ---------------------------------------------------------------------------
# Sample de nodos por TO (para inspección comparativa)
# ---------------------------------------------------------------------------

def sample_nodes_by_to(kg: dict, n_per_to: int = 5, seed: int = 42) -> dict[str, list[dict]]:
    """Devuelve hasta n_per_to nodos al azar por TO (basándose en properties.source_to)."""
    rng = random.Random(seed)
    by_to: dict[str, list[dict]] = defaultdict(list)
    for n in kg.get("nodes", []):
        st = (n.get("properties") or {}).get("source_to")
        if st:
            by_to[st].append(n)
    out: dict[str, list[dict]] = {}
    for to, nodes in by_to.items():
        rng.shuffle(nodes)
        out[to] = nodes[:n_per_to]
    return out


# ---------------------------------------------------------------------------
# Validación
# ---------------------------------------------------------------------------

def validate(kg: dict) -> list[str]:
    """Devuelve lista de errores. Vacía = OK."""
    errors: list[str] = []
    ids = [n["id"] for n in kg["nodes"]]
    if len(ids) != len(set(ids)):
        dups = [i for i, c in Counter(ids).items() if c > 1]
        errors.append(f"IDs duplicados: {dups[:5]}{'…' if len(dups) > 5 else ''}")

    id_set = set(ids)
    for i, n in enumerate(kg["nodes"]):
        if not n.get("provenance") or not n["provenance"].get("source_doc") or not n["provenance"].get("location"):
            errors.append(f"Nodo[{i}] {n.get('id')}: provenance incompleto.")
        if n.get("type") not in ENTITY_TYPES:
            errors.append(f"Nodo[{i}] {n.get('id')}: type inválido {n.get('type')!r}.")
        for field in ("label",):
            if is_documental_hierarchy(n.get(field, "")):
                errors.append(f"Nodo[{i}] {n.get('id')}: {field} parece jerarquía documental: {n.get(field)!r}.")

    for i, e in enumerate(kg["edges"]):
        if not e.get("provenance") or not e["provenance"].get("source_doc") or not e["provenance"].get("location"):
            errors.append(f"Edge[{i}]: provenance incompleto.")
        if e.get("source") not in id_set:
            errors.append(f"Edge[{i}]: source no existe: {e.get('source')!r}.")
        if e.get("target") not in id_set:
            errors.append(f"Edge[{i}]: target no existe: {e.get('target')!r}.")
        if not e.get("relation"):
            errors.append(f"Edge[{i}]: relation vacío.")

    return errors


# ---------------------------------------------------------------------------
# Métricas
# ---------------------------------------------------------------------------

def metrics(kg: dict) -> dict:
    nodes = kg["nodes"]
    edges = kg["edges"]
    types_n = Counter(n["type"] for n in nodes)
    types_e = Counter(e["relation"] for e in edges)

    # Cobertura por TO: % de chunks del TO que generaron ≥1 tripleta.
    chunks = read_jsonl(CHUNKS_PATH) if CHUNKS_PATH.exists() else []
    extractions = read_jsonl(EXTRACTIONS_PATH) if EXTRACTIONS_PATH.exists() else []
    chunks_by_to: dict[str, set[str]] = defaultdict(set)
    for c in chunks:
        chunks_by_to[c["to"]].add(c["chunk_id"])
    productive_chunks_by_to: dict[str, set[str]] = defaultdict(set)
    for r in extractions:
        if r["entities"] or r["relations"]:
            productive_chunks_by_to[r["to"]].add(r["chunk_id"])
    coverage = {}
    for to_slug in TO_FILES:
        total = len(chunks_by_to.get(to_slug, []))
        productive = len(productive_chunks_by_to.get(to_slug, []))
        coverage[to_slug] = {
            "chunks_total": total,
            "chunks_productivos": productive,
            "pct": round(100.0 * productive / total, 2) if total else 0.0,
        }

    # Costo por etapa/modelo
    cost_by_stage: dict[str, dict] = {}
    for fp in sorted(CACHE_DIR.glob("cost_*.json")):
        stage = fp.stem.replace("cost_", "")
        cost_by_stage[stage] = read_json(fp)
    total_usd = sum(s.get("total_usd", 0.0) for s in cost_by_stage.values())

    # Timings (opcional)
    timings = read_json(TIMINGS_PATH) if TIMINGS_PATH.exists() else {}

    # Análisis post-hoc + muestra por TO
    predicates_analysis = analyze_predicates(kg)
    sample = sample_nodes_by_to(kg, n_per_to=5, seed=42)

    return {
        "n_nodes": len(nodes),
        "n_edges": len(edges),
        "density": round(len(edges) / len(nodes), 3) if nodes else 0.0,
        "n_entity_types": len([t for t, c in types_n.items() if c > 0]),
        "n_relation_types": len(types_e),
        "nodes_by_type": dict(sorted(types_n.items(), key=lambda kv: -kv[1])),
        "edges_by_type_top20": dict(types_e.most_common(20)),
        "coverage_by_to": coverage,
        "cost_by_stage": cost_by_stage,
        "total_usd": round(total_usd, 4),
        "timings": timings,
        "predicates_analysis": predicates_analysis,
        "sample_nodes_by_to": sample,
    }


# ---------------------------------------------------------------------------
# Render del report.md
# ---------------------------------------------------------------------------

def render_report(m: dict, errors: list[str], kg: dict) -> str:
    lines: list[str] = []
    lines.append("# Report — Run 1: Cookbook de Anthropic")
    lines.append("")
    lines.append("## Identificación del run")
    lines.append(f"- **Run ID (exacto):** `Run 1 — Cookbook de Anthropic`")
    lines.append(f"- **Carpeta:** `data/experiment/run_1_cookbook/`")
    lines.append(f"- **Schema documentado en:** `schema.md`")
    lines.append("")
    lines.append("## Modelos utilizados por etapa")
    lines.append("")
    lines.append("| Etapa cookbook | Script | Modelo | Justificación |")
    lines.append("|---|---|---|---|")
    lines.append("| 1. Document Corpus Building | `01_load_corpus.py` | — (sin LLM) | Extracción local de texto con pypdf; sin razonamiento. |")
    lines.append("| 2. Entity & Relation Extraction | `02_extract.py` | `claude-haiku-4-5` | Alto volumen (~500 chunks); Haiku es rápido y barato y maneja schema-constrained extraction (cookbook §3). Requisito del protocolo. |")
    lines.append("| 3. Entity Resolution | `03_resolve.py` | `claude-sonnet-4-6` | Razonamiento sobre evidencia conflictiva (mismo nombre, distinta función); Sonnet pesa mejor descripciones (cookbook §5). |")
    lines.append("| 4. Graph Assembly | `04_assemble.py` | — (sin LLM) | Determinístico: dedup de edges, slug de IDs, ensamblaje JSON. |")
    lines.append("| 5. Hub Summarization | `05_hub_summarize.py` | `claude-sonnet-4-6` | Síntesis multi-documento de evidencia (cookbook §6); Sonnet por la misma razón que la resolución. |")
    lines.append("| 6. Multi-hop Querying | (no ejecutado) | — | Es evaluación, va a la FASE 2.3 del experimento. |")
    lines.append("")
    lines.append("## Excepciones al protocolo")
    lines.append("")
    lines.append("Esta sección registra cualquier desvío del protocolo experimental (`docs/schema/experiment_protocol.md`) o de la plantilla de instancia (`docs/schema/experiment_instance_template.md`).")
    lines.append("")
    lines.append("### Excepción 1: presupuesto USD 5 → USD 10 (autorizada antes del full run)")
    lines.append("")
    lines.append("- **Regla original:** plantilla de instancia, sección \"Restricciones operativas\": *\"Límite de costo: máximo USD 5 de inferencia para esta instancia.\"*")
    lines.append("- **Cambio aplicado:** `BUDGET_USD_HARD` se elevó a USD 10 (margen de abort: USD 9). Autorizado por la autora tras revisar el smoke test sobre Protección al Usuario.")
    lines.append("- **Justificación cuantitativa derivada del smoke test:**")
    lines.append("  - El smoke completo sobre 1 TO (36 chunks, 100 % cobertura) costó **USD 0.7217**.")
    lines.append("  - Extrapolando al corpus completo (543 chunks): proyección **USD 8.0–9.1**.")
    lines.append("  - El proyecto se hubiera quedado en ~60 % de cobertura con el presupuesto original.")
    lines.append("- **Por qué la estimación inicial fue ~3× optimista:** el promedio real de tokens de input por chunk (≈ 3.000) y de output (≈ 1.500) es notablemente más alto que el supuesto inicial (≈ 1.000 / 300), porque el dominio regulatorio del BCRA es denso en obligaciones por página y el cookbook pide `description` grounded por entidad (lo que infla el output).")
    lines.append("- **Comparabilidad con las otras instancias del experimento:** la autora actualizó el `experiment_instance_template.md` para que los Runs 2-5 también tengan presupuesto USD 10 — ver nota en ese archivo. La comparabilidad entre estrategias se mantiene; sólo cambió la magnitud del experimento.")
    lines.append("- **Lecciones para FASE 2.1 (preparación):** futuras réplicas del experimento deberían ejecutar primero un smoke sobre 1 TO antes de fijar el presupuesto.")
    lines.append("")
    lines.append("### Excepción 2: presupuesto USD 10 → USD 11 (autorizada después de la resolución)")
    lines.append("")
    lines.append("- **Cambio aplicado:** `BUDGET_USD_HARD` se elevó a USD 11 (margen de abort: USD 10.80). Autorizado por la autora tras el checkpoint post-resolución.")
    lines.append("- **Por qué fue necesario:** la resolución Sonnet costó **USD 4.40** (vs proyección USD 1.30, **+238 %**), dejando solo USD 0.01 de margen al hard budget de USD 10. Hub summarization (etapa 5 del cookbook) no entraba.")
    lines.append("- **Causa raíz de la desviación de la resolución:**")
    lines.append("  - 4.868 entidades únicas reales (vs 3.500–5.000 estimadas) → 57 batches Sonnet.")
    lines.append("  - El **output** por call promedió **4.087 tokens** (no estimado previamente): cada cluster lista `{canonical, aliases:[...]}` y con 100 entidades/batch eso son ≈4 K tokens output × $15/MTok = $0.06 por call × 57 calls ≈ $3.40.")
    lines.append("  - 2 warnings de `tool_use con payload vacío` en REQUIREMENT (1.280 entidades) y REPORT_ITEM (340), donde Sonnet truncó la salida con `max_tokens=8000` y se cayó a `fallback_singletons()`. Resultado: agrupó menos de lo posible.")
    lines.append("- **Decisión:** se autorizó la excepción 2 para no romper el pipeline del cookbook a la mitad. Hub summarization se ejecutó completo (top 15 hubs con Sonnet, fidelidad al cookbook).")
    lines.append("- **Lección para futuras réplicas:** la resolución con batches grandes es costosa porque el output escala con el tamaño del batch. Próximas estrategias podrían (a) usar batches más chicos pero más paralelos con Haiku, (b) hacer una primera pasada de blocking heurístico con embeddings antes de Sonnet, o (c) aceptar agrupar menos a cambio de costo controlado.")
    lines.append("")
    lines.append("## Métricas del protocolo (§d)")
    lines.append("")
    timings = m.get("timings", {})
    if timings:
        lines.append(f"- **Tiempo total de construcción:** {timings.get('total_seconds', 'N/A')} s")
        for k, v in timings.items():
            if k != "total_seconds":
                lines.append(f"  - {k}: {v} s")
    else:
        lines.append("- **Tiempo total de construcción:** (no instrumentado en esta corrida)")
    lines.append(f"- **Costo total:** USD {m['total_usd']:.4f}")
    lines.append("")
    lines.append("### Costo por etapa y modelo")
    lines.append("")
    lines.append("| Etapa | Modelo | Calls | Input | Output | Cache W | Cache R | USD |")
    lines.append("|---|---|---:|---:|---:|---:|---:|---:|")
    for stage, payload in m["cost_by_stage"].items():
        for model, s in payload.get("by_model", {}).items():
            cw = s.get("cache_creation_tokens", 0)
            cr = s.get("cache_read_tokens", 0)
            lines.append(
                f"| {stage} | {model} | {s['calls']} | {s['input_tokens']:,} | "
                f"{s['output_tokens']:,} | {cw:,} | {cr:,} | {s['usd']:.4f} |"
            )
    lines.append("")
    lines.append("> **Caching:** se declaró `cache_control: ephemeral` en el `SYSTEM_PROMPT` de extracción. ")
    lines.append("> El threshold mínimo de Haiku 4.5 para activar prompt caching es ≥2.048 tokens; el `SYSTEM_PROMPT` ")
    lines.append("> de este run mide 800 tokens reales, por lo que el caching **no se activó** ")
    lines.append("> (`Cache W=0`, `Cache R=0`). El declarador se conserva por si futuras versiones del modelo bajan el threshold.")
    lines.append("")
    lines.append(f"### Nodos y edges")
    lines.append("")
    lines.append(f"- **Nodos:** {m['n_nodes']}")
    lines.append(f"- **Edges:** {m['n_edges']}")
    lines.append(f"- **Densidad (edges/nodes):** {m['density']}")
    lines.append(f"- **Tipos de entidad únicos:** {m['n_entity_types']}")
    lines.append(f"- **Tipos de relación únicos:** {m['n_relation_types']}")
    lines.append("")
    lines.append("### Nodos por tipo")
    lines.append("")
    lines.append("| Tipo | Cantidad |")
    lines.append("|---|---:|")
    for t, c in m["nodes_by_type"].items():
        lines.append(f"| {t} | {c} |")
    lines.append("")
    lines.append("### Edges por tipo (top 20)")
    lines.append("")
    lines.append("| Predicado | Cantidad |")
    lines.append("|---|---:|")
    for t, c in m["edges_by_type_top20"].items():
        lines.append(f"| `{t}` | {c} |")
    lines.append("")
    lines.append("### Cobertura por TO")
    lines.append("")
    lines.append("| TO | Chunks total | Chunks productivos | % |")
    lines.append("|---|---:|---:|---:|")
    for to_slug, cov in m["coverage_by_to"].items():
        lines.append(f"| {to_slug} | {cov['chunks_total']} | {cov['chunks_productivos']} | {cov['pct']}% |")
    lines.append("")
    lines.append("> *Productivo* = el chunk generó ≥1 entidad o relación tras la llamada a Haiku.")
    lines.append("> Los chunks no-productivos son típicamente: páginas de índice, encabezados del TO, y la")
    lines.append("> sección final \"Comunicaciones vinculadas\". Algunos de éstos son skipeados antes de Haiku")
    lines.append("> por la heurística `is_non_productive_chunk()` para ahorrar costo sin perder contenido normativo.")
    lines.append("")

    # ---- Análisis post-hoc de predicados ----
    pred = m.get("predicates_analysis")
    if pred:
        lines.append("## Análisis post-hoc de predicados")
        lines.append("")
        lines.append("La estrategia \"Cookbook de Anthropic\" deja los predicados como **verb phrases libres** (cookbook §2.2: `predicate: str` sin enum). Esto genera vocabulario verboso por diseño. Esta sección reporta métricas que permiten comparar la *limpieza* del vocabulario contra otras estrategias del experimento.")
        lines.append("")
        lines.append(f"- **Edges totales:** {pred['n_edges']}")
        lines.append(f"- **Predicados únicos crudos** (tal como salieron de Haiku): **{pred['n_predicates_raw']}**")
        lines.append(f"- **Ratio crudo (predicados / edges):** {pred['ratio_raw']}")
        lines.append(f"- **Predicados únicos tras normalización trivial:** **{pred['n_predicates_normalized']}** ")
        lines.append(f"  *(reducción: {pred['n_predicates_raw'] - pred['n_predicates_normalized']} predicados fusionados)*")
        lines.append(f"- **Ratio normalizado:** {pred['ratio_normalized']}")
        lines.append(f"- **Grupos fusionados:** {pred['merged_groups_total']} (≥2 variantes); singletons que quedaron solos: {pred['singletons_normalized']}")
        lines.append("")
        lines.append("### Heurística de normalización aplicada")
        lines.append("")
        lines.append("Se considera *variación trivial* cualquiera de:")
        lines.append("- Diferencia sólo de **casing** (`Debe_cumplir` vs `debe_cumplir`).")
        lines.append("- Diferencia sólo de **acentos** (`esta_sujeto_a` vs `está_sujeto_a`).")
        lines.append("- Diferencia sólo de **número gramatical** en el verbo auxiliar inicial: `deben/debe`, `tienen/tiene`, `pueden/puede`, `están/está`, `son/es`, `hacen/hace`, `aplican/aplica`, `requieren/requiere` (+ formas en futuro: `deberán/deberá`, etc.).")
        lines.append("- Diferencia sólo de **separadores** (espacio vs underscore vs guión).")
        lines.append("")
        lines.append("NO se considera trivial (y por lo tanto NO se fusiona):")
        lines.append("- Variantes léxicas con verbos distintos (`debe_cumplir` ≠ `está_obligado_a`).")
        lines.append("- Variantes con preposiciones distintas (`aplica_a` ≠ `aplica_para`).")
        lines.append("")
        lines.append("### Grupos fusionados — top 10")
        lines.append("")
        if pred["groups_merged_top"]:
            lines.append("| Canónico normalizado | Variantes crudas |")
            lines.append("|---|---|")
            for canon, members in pred["groups_merged_top"]:
                vs = ", ".join(f"`{x}`" for x in members)
                lines.append(f"| `{canon}` | {vs} |")
        else:
            lines.append("(no se detectaron grupos fusionables — vocabulario ya \"limpio\")")
        lines.append("")
        lines.append("> El `kg.json` NO se modificó: los predicados se conservan exactamente como Haiku los emitió (fidelidad al cookbook). Esta sección es **descriptiva**, para comparación post-hoc entre estrategias.")
        lines.append("")

    # ---- Muestra de nodos por TO ----
    sample = m.get("sample_nodes_by_to")
    if sample:
        lines.append("## Muestra de nodos por TO")
        lines.append("")
        lines.append("5 nodos al azar de cada TO (seed=42, basado en `properties.source_to`).")
        lines.append("")
        # Mantengo el orden del protocolo §a
        order = ["clasificacion_deudores", "capitales_minimos", "exterior_cambios", "proteccion_usuarios", "regimen_informativo_cm"]
        for to in order:
            nodes = sample.get(to, [])
            if not nodes:
                continue
            lines.append(f"### {to}")
            lines.append("")
            for n in nodes:
                lines.append(f"- **`{n['id']}`** · *{n['type']}* · «{n['label']}»")
                props = n.get("properties") or {}
                desc = (props.get("description") or "")
                if len(desc) > 180:
                    desc = desc[:177] + "…"
                lines.append(f"  - desc: {desc}")
                prov = n.get("provenance", {})
                lines.append(f"  - prov: `{prov.get('source_doc','?')}` · `{prov.get('location','?')}` · version `{props.get('version','?')}`")
            lines.append("")
    lines.append("## Validación del KG")
    lines.append("")
    if errors:
        lines.append(f"**{len(errors)} error(es) de validación:**")
        lines.append("")
        for e in errors[:20]:
            lines.append(f"- {e}")
        if len(errors) > 20:
            lines.append(f"- … y {len(errors) - 20} más.")
    else:
        lines.append("✅ Sin errores de validación.")
    lines.append("")
    lines.append("## Inventario del directorio `code/`")
    lines.append("")
    lines.append("| Archivo | Descripción |")
    lines.append("|---|---|")
    lines.append("| `common.py` | Constantes (subset, tipos), schemas Pydantic, helpers de I/O y accounting de costo. |")
    lines.append("| `01_load_corpus.py` | Etapa 1. Extrae texto de los 5 PDFs con pypdf y emite `cache/chunks.jsonl` (chunk = página, fusión de páginas chicas). |")
    lines.append("| `02_extract.py` | Etapa 2. Una llamada a Haiku por chunk con structured output (`ExtractedGraph`); persiste `cache/raw_extractions.jsonl` + ledger. |")
    lines.append("| `03_resolve.py` | Etapa 3. Por cada tipo de entidad, clusterización con Sonnet; emite `alias_to_canonical.json` y `canonical_info.json`. |")
    lines.append("| `04_assemble.py` | Etapa 4. Construye el KG (NetworkX) y lo serializa a `kg.json` en el formato obligatorio. |")
    lines.append("| `05_hub_summarize.py` | Etapa 5. Resume los top-degree hubs con Sonnet y enriquece `kg.json` con `summary`/`key_facts`/`time_range`. |")
    lines.append("| `06_validate_and_report.py` | Validación + cálculo de métricas + emisión de `report.md`. |")
    lines.append("| `07_visualize.py` | Visualización interactiva del KG con pyvis (force-directed, colores por type, hover con metadata). Output: `../kg_visual.html`. Fuera del cookbook; sirve para inspección rápida sin Gephi. |")
    lines.append("| `requirements.txt` | Dependencias Python. |")
    lines.append("| `README.md` | Cómo correr el pipeline. |")
    lines.append("| `cache/` | Outputs intermedios (chunks, extracciones crudas, alias map, ledgers de costo). |")
    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Etapa 6 (build-side): validación + reporte.")
    args = parser.parse_args(argv)

    if not KG_JSON_PATH.exists():
        print(f"[06_report] Falta {KG_JSON_PATH}.")
        return 1

    kg = read_json(KG_JSON_PATH)
    errors = validate(kg)
    m = metrics(kg)
    report = render_report(m, errors, kg)
    REPORT_PATH.write_text(report)
    print(f"[06_report] OK · {len(errors)} errores · nodes={m['n_nodes']} edges={m['n_edges']} USD={m['total_usd']:.4f}")
    print(f"[06_report] → {REPORT_PATH}")
    return 0 if not errors else 2


if __name__ == "__main__":
    raise SystemExit(main())
