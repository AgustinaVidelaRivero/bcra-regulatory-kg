"""
Clustering de tipos crudos por similitud semántica.

Política (acordada con la autora):
- Sólo se clusterea tipos con frecuencia ≥ 2.
  Los singletons (freq = 1) quedan preservados con su forma normalizada superficialmente.
- Modelo: sentence-transformers multilingüe (paraphrase-multilingual-MiniLM-L12-v2).
- Métrica: cosine similarity.
- Umbral: cosine ≥ 0.85.
- Estrategia de clustering: connected components sobre el grafo de pares con sim ≥ umbral.
  Es decir, transitive closure: si A~B y B~C, entonces A,B,C son del mismo cluster.

OUTPUT: code/cache/types_cluster_proposal.json — la propuesta SIN APLICAR.
Esperar OK del usuario antes de aplicar.

REPORTA:
- Top 30 clusters por frecuencia total (suma de freq de miembros), con TODOS los miembros y freq individuales.
- Distribución de tamaño (cuántos de tamaño 2, 3, 4, 5+).
- Clusters con alta varianza de frecuencias internas (sospechosos de fusión falsa).
- Cuántos tipos con freq ≥ 2 quedan singleton tras el clustering.
"""

import json
import statistics
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from slug import slug_type

STAGING_PATH = Path(__file__).resolve().parent / "cache" / "staging.json"
PROPOSAL_PATH = Path(__file__).resolve().parent / "cache" / "types_cluster_proposal.json"

MODEL_NAME = "paraphrase-multilingual-MiniLM-L12-v2"
SIM_THRESHOLD = 0.85


def gather_types_with_freq(staging: dict) -> Counter:
    """Cuenta frecuencia de cada tipo crudo across todas las observaciones.

    La frecuencia de un type_raw es el número de OBSERVACIONES, no el número de
    nodos. Una entidad con n_observations=5 y type_raw=[A, B] contribuye 5 a A o B
    de manera no trivial — para simplificar y mantener la equivalencia con el smoke,
    asumimos que cada nodo aporta 1 a cada uno de sus type_raw distintos.

    Esta es la métrica que mejor refleja "qué tan común es el tipo" sin doble-contar."""
    c: Counter = Counter()
    for node in staging["nodes"]:
        for t in node["type_raw"]:
            c[t] += 1
    return c


def build_clusters(types_freq2: list[str], embeddings: np.ndarray, threshold: float) -> list[list[int]]:
    """Connected components sobre pares con sim ≥ threshold."""
    n = len(types_freq2)
    if n == 0:
        return []
    sim = cosine_similarity(embeddings)
    # union-find
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for i in range(n):
        for j in range(i + 1, n):
            if sim[i, j] >= threshold:
                union(i, j)

    groups: dict[int, list[int]] = defaultdict(list)
    for i in range(n):
        groups[find(i)].append(i)
    return list(groups.values())


def pick_canonical(members: list[str], freqs: list[int]) -> str:
    """Tipo canónico del cluster: forma normalizada del miembro de mayor frecuencia.
    Desempate: el más corto, luego alfabético."""
    paired = sorted(zip(members, freqs), key=lambda kv: (-kv[1], len(kv[0]), kv[0]))
    return slug_type(paired[0][0])


def main():
    print("=" * 70)
    print("CLUSTER TYPES — paso 4 (propuesta SIN aplicar)")
    print(f"Modelo: {MODEL_NAME}")
    print(f"Umbral cosine: {SIM_THRESHOLD}")
    print("=" * 70)
    print()

    staging = json.loads(STAGING_PATH.read_text())
    types_freq = gather_types_with_freq(staging)
    print(f"[input] {len(types_freq)} tipos crudos únicos (across todos los nodos)")

    types_freq2 = [t for t, n in types_freq.items() if n >= 2]
    singletons_pre = [t for t, n in types_freq.items() if n == 1]
    print(f"[input] {len(types_freq2)} tipos con freq ≥ 2 (entran al clustering)")
    print(f"[input] {len(singletons_pre)} tipos singletons (no entran al clustering, preservados como normalizados)")
    print()

    # Embeddings
    print(f"[embed] cargando modelo {MODEL_NAME} ...", flush=True)
    model = SentenceTransformer(MODEL_NAME)
    print(f"[embed] computando embeddings de {len(types_freq2)} tipos ...", flush=True)
    embeddings = model.encode(types_freq2, batch_size=64, show_progress_bar=False, normalize_embeddings=True)
    print(f"[embed] shape: {embeddings.shape}", flush=True)

    # Clustering
    clusters_idx = build_clusters(types_freq2, embeddings, SIM_THRESHOLD)
    print(f"[cluster] {len(clusters_idx)} grupos producidos sobre {len(types_freq2)} tipos")

    # Resolver clusters
    clusters = []
    n_singleton_post = 0
    for grp in clusters_idx:
        members = [types_freq2[i] for i in grp]
        freqs = [types_freq[m] for m in members]
        canonical = pick_canonical(members, freqs)
        cluster = {
            "canonical_type": canonical,
            "members": [{"type_raw": m, "freq": f, "type_normalized": slug_type(m)} for m, f in zip(members, freqs)],
            "size": len(members),
            "freq_total": sum(freqs),
            "freq_max": max(freqs),
            "freq_min": min(freqs),
            "freq_stdev": statistics.stdev(freqs) if len(freqs) > 1 else 0,
        }
        clusters.append(cluster)
        if cluster["size"] == 1:
            n_singleton_post += 1

    # Top 30 por freq_total
    sorted_clusters = sorted(clusters, key=lambda c: -c["freq_total"])
    multi_clusters = [c for c in clusters if c["size"] >= 2]
    sorted_multi = sorted(multi_clusters, key=lambda c: -c["freq_total"])

    print()
    print(f"--- Resumen del clustering ---")
    print(f"  Tipos input (freq ≥ 2)       : {len(types_freq2)}")
    print(f"  Clusters totales             : {len(clusters)}")
    print(f"  Clusters de tamaño 1         : {n_singleton_post}  ← quedaron singletons sin fusionar")
    print(f"  Clusters de tamaño ≥ 2       : {len(multi_clusters)}")
    print()

    # Distribución de tamaño
    size_dist = Counter(c["size"] for c in clusters)
    print(f"--- Distribución de tamaños de cluster ---")
    for sz in sorted(size_dist.keys()):
        n_cl = size_dist[sz]
        n_tipos = sz * n_cl
        bar = "█" * min(50, n_cl)
        print(f"  size {sz:>3}: {n_cl:>4} clusters ({n_tipos:>4} tipos)  {bar}")
    print()

    # Top 30 clusters de tamaño ≥ 2 por freq_total
    print(f"--- TOP 30 clusters de tamaño ≥ 2 por freq_total ---")
    print()
    for i, c in enumerate(sorted_multi[:30], 1):
        print(f"[{i:>2}] canonical='{c['canonical_type']}'  size={c['size']}  freq_total={c['freq_total']}  freq_stdev={c['freq_stdev']:.1f}")
        for m in sorted(c["members"], key=lambda x: -x["freq"]):
            print(f"        {m['freq']:>4}× {m['type_raw']:<60}  → {m['type_normalized']}")
        print()

    # Clusters con alta varianza (los sospechosos)
    suspect_clusters = sorted(multi_clusters, key=lambda c: -c["freq_stdev"])
    print(f"--- Top 15 clusters con MAYOR varianza interna de frecuencias (sospechosos de fusión falsa) ---")
    print()
    for i, c in enumerate(suspect_clusters[:15], 1):
        print(f"[{i:>2}] canonical='{c['canonical_type']}'  freq_stdev={c['freq_stdev']:.1f}  range=[{c['freq_min']}..{c['freq_max']}]")
        for m in sorted(c["members"], key=lambda x: -x["freq"]):
            print(f"        {m['freq']:>4}× {m['type_raw']}")
        print()

    # Persistir
    proposal = {
        "model": MODEL_NAME,
        "sim_threshold": SIM_THRESHOLD,
        "n_types_input_freq_ge_2": len(types_freq2),
        "n_types_singletons_excluded": len(singletons_pre),
        "n_clusters_total": len(clusters),
        "n_clusters_size_ge_2": len(multi_clusters),
        "n_clusters_size_1": n_singleton_post,
        "size_distribution": dict(size_dist),
        "clusters": sorted_clusters,
        "singletons_excluded_from_clustering": [
            {"type_raw": t, "type_normalized": slug_type(t)} for t in singletons_pre
        ],
    }
    PROPOSAL_PATH.write_text(json.dumps(proposal, ensure_ascii=False, indent=2))
    print(f"[proposal] → {PROPOSAL_PATH}")


if __name__ == "__main__":
    main()
