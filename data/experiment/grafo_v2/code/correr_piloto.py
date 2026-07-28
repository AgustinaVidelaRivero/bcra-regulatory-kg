"""Driver del piloto multi-modelo (B1) — extrae SOLO los chunks de la muestra.

Namespace de caché por modelo Y por réplica:
    cache_v2/piloto/<model_id_saneado>/replica_<N>/
Un mismo chunk bajo dos modelos (o dos réplicas) produce rutas DISTINTAS; la
key del chunk sigue incluyendo el hash del SYSTEM_PROMPT (candado heredado).

Corrida fresca = cero cache hits, verificado con assert AUTOMÁTICO antes de
llamar a la API (si el namespace ya tiene resultados válidos de la muestra, el
driver FRENA: una réplica con caché de la anterior no es réplica) y re-afirmado
al terminar.

Uso:
    python correr_piloto.py --model <id> --muestra ../piloto/muestra_piloto.json --replica 1
    python correr_piloto.py --model <id> --muestra ... --replica 1 --dry-run   # sin API
"""

from __future__ import annotations

import argparse
import asyncio
import json
import re
import sys
from pathlib import Path

from chunker import Chunk
from extract import CACHE_ROOT_V2, MODEL, PROMPT_HASH, chunk_cache_path, extract_chunks

PILOTO_DIR = Path(__file__).resolve().parent.parent / "piloto"
CONFIG_PATH = PILOTO_DIR / "piloto_config.json"

# Supuestos de estimación del dry-run (declarados; medidos en U4c sobre Protección):
# - overhead fijo de input por llamada (system prompt con catálogo + plantilla de
#   mensaje): ~9.600 tokens (U4c: 385.056 in / 37 chunks, con ~2.600 chars/chunk).
# - texto del chunk: ~3,5 chars/token (castellano regulatorio).
# - output: 2.100 tokens/chunk para TODOS los modelos (promedio U4b/U4c con Haiku;
#   SUPUESTO declarado — modelos mayores pueden emitir más).
EST_FIXED_IN_TOK = 9_600
EST_CHARS_POR_TOKEN = 3.5
EST_OUT_TOK_POR_CHUNK = 2_100


def sanitizar(model_id: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]", "_", model_id)


def cargar_muestra(path: Path) -> list[Chunk]:
    data = json.loads(path.read_text(encoding="utf-8"))
    chunks = [
        Chunk(chunk_id=m["chunk_id"], doc=m["doc"], location=m["location"],
              text=m["texto"], char_count=len(m["texto"]))
        for m in data
    ]
    if not chunks:
        raise SystemExit("La muestra está vacía.")
    return chunks


def contar_cacheados(chunks: list[Chunk], cache_root: Path) -> int:
    """Cuántos chunks de la muestra YA tienen resultado válido en el namespace."""
    n = 0
    for c in chunks:
        p = chunk_cache_path(c, cache_root)
        if p.exists():
            try:
                if json.loads(p.read_text(encoding="utf-8")).get("error") is None:
                    n += 1
            except Exception:
                pass
    return n


def estimar_costo(chunks: list[Chunk], model_id: str) -> dict:
    cfg = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    precios = {m["id"]: m for m in cfg["modelos"]}
    in_tok = sum(EST_FIXED_IN_TOK + int(len(c.text) / EST_CHARS_POR_TOKEN) for c in chunks)
    out_tok = EST_OUT_TOK_POR_CHUNK * len(chunks)
    est = {"llamadas": len(chunks), "in_tokens_est": in_tok, "out_tokens_est": out_tok}
    if model_id in precios:
        p = precios[model_id]
        est["costo_usd_est"] = round(
            in_tok / 1e6 * p["precio_in_por_mtok"] + out_tok / 1e6 * p["precio_out_por_mtok"], 3
        )
    else:
        est["costo_usd_est"] = None
        est["nota"] = f"modelo {model_id} sin precio en piloto_config.json"
    return est


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True, help="id exacto de la API (debe estar en piloto_config.json)")
    ap.add_argument("--muestra", required=True, type=Path)
    ap.add_argument("--replica", required=True, type=int)
    ap.add_argument("--dry-run", action="store_true", help="mostrar plan y estimación, sin llamar a la API")
    args = ap.parse_args()

    cfg = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    ids_config = [m["id"] for m in cfg["modelos"]]
    if args.model not in ids_config:
        print(f"ERROR: {args.model} no está en piloto_config.json ({ids_config}). "
              f"El piloto corre SOLO modelos confirmados en el config.")
        return 1

    chunks = cargar_muestra(args.muestra)
    cache_root = CACHE_ROOT_V2 / "piloto" / sanitizar(args.model) / f"replica_{args.replica}"

    print(f"Piloto | model={args.model} | replica={args.replica} | chunks={len(chunks)} | "
          f"prompt_hash={PROMPT_HASH}", flush=True)
    print(f"Namespace de caché: {cache_root}", flush=True)

    est = estimar_costo(chunks, args.model)
    print(f"Estimación: {est['llamadas']} llamadas | in≈{est['in_tokens_est']:,} tok | "
          f"out≈{est['out_tokens_est']:,} tok (supuesto {EST_OUT_TOK_POR_CHUNK}/chunk) | "
          f"costo≈USD {est['costo_usd_est']}", flush=True)

    if args.dry_run:
        print("DRY-RUN: no se llamó a la API. Rutas de ejemplo del namespace:")
        for c in chunks[:2]:
            print("  ", chunk_cache_path(c, cache_root))
        return 0

    # Corrida fresca: el namespace no debe tener resultados válidos de la muestra.
    pre = contar_cacheados(chunks, cache_root)
    assert pre == 0, (
        f"FRENO: {pre} chunks de la muestra ya tienen resultado válido en {cache_root} — "
        f"una corrida con caché previa no es fresca (réplica ≠ replay). "
        f"Usá otro número de réplica o archivá el namespace."
    )

    results = asyncio.run(extract_chunks(chunks, cache_root, model=args.model))

    # cache_hits de ESTA corrida = resultados válidos que existían antes (pre).
    cache_hits = pre
    assert cache_hits == 0, (
        f"FRENO: cache_hits={cache_hits} != 0 en el namespace {cache_root}"
    )
    n_fail = sum(1 for r in results if r.get("error"))
    print(f"OK corrida fresca: cache_hits=0 (namespace {cache_root}) | "
          f"resultados={len(results)} | fallidos={n_fail}", flush=True)
    return 0 if n_fail == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
