"""
Probe: clustering agglomerativo con complete-linkage a varios umbrales.

A diferencia de connected-components, complete-linkage exige que TODOS los pares
dentro de un cluster cumplan el umbral de similitud (no permite cadenas).
Eso debería romper la fusión falsa del cluster #1 (76 miembros que comparten
solo la palabra "regulatorio").

Imprime cuántos clusters de tamaño ≥ 2 produce cada umbral y muestra los
top 10 más grandes para que el usuario decida.
"""

import json
import statistics
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics.pairwise import cosine_similarity

from slug import slug_type

STAGING_PATH = Path(__file__).resolve().parent / "cache" / "staging.json"
MODEL_NAME = "paraphrase-multilingual-MiniLM-L12-v2"


def gather_types(staging):
    c = Counter()
    for node in staging["nodes"]:
        for t in node["type_raw"]:
            c[t] += 1
    return c


def cluster_complete(embeddings: np.ndarray, threshold: float) -> list[int]:
    """Agglomerative con complete-linkage. Devuelve labels.

    distance_threshold = 1 - cos_threshold. Distancia coseno = 1 - sim coseno.
    """
    dist_threshold = 1.0 - threshold
    clu = AgglomerativeClustering(
        n_clusters=None,
        metric="cosine",
        linkage="complete",
        distance_threshold=dist_threshold,
    )
    labels = clu.fit_predict(embeddings)
    return labels


def main():
    staging = json.loads(STAGING_PATH.read_text())
    types_freq = gather_types(staging)
    types = [t for t, n in types_freq.items() if n >= 2]
    freqs = [types_freq[t] for t in types]
    print(f"[input] {len(types)} tipos con freq ≥ 2")

    model = SentenceTransformer(MODEL_NAME)
    emb = model.encode(types, batch_size=64, show_progress_bar=False, normalize_embeddings=True)
    print(f"[embed] {emb.shape}")
    print()

    for thr in [0.85, 0.88, 0.90, 0.92]:
        labels = cluster_complete(emb, thr)
        groups: dict[int, list[int]] = defaultdict(list)
        for i, lab in enumerate(labels):
            groups[lab].append(i)
        all_clusters = list(groups.values())
        multi = [g for g in all_clusters if len(g) >= 2]
        sizes = Counter(len(g) for g in all_clusters)
        max_size = max(sizes.keys()) if sizes else 0

        # Top 5 más grandes
        multi_sorted = sorted(multi, key=lambda g: -sum(freqs[i] for i in g))[:5]

        print(f"--- umbral cos≥{thr} (complete-linkage) ---")
        print(f"  Clusters totales: {len(all_clusters)}  |  Multi (size≥2): {len(multi)}  |  Singletons post: {len(all_clusters) - len(multi)}")
        print(f"  Max cluster size: {max_size}")
        print(f"  Distribución de tamaños: {dict(sorted(sizes.items()))}")
        print(f"  Top 5 clusters más grandes (por freq_total):")
        for g in multi_sorted:
            members = sorted([(types[i], freqs[i]) for i in g], key=lambda kv: -kv[1])
            ft = sum(f for _, f in members)
            print(f"    size={len(g)}  freq_total={ft}  members:")
            for m, f in members[:12]:
                print(f"      {f:>4}× {m}")
            if len(members) > 12:
                print(f"      ... +{len(members)-12} más")
        print()


if __name__ == "__main__":
    main()
