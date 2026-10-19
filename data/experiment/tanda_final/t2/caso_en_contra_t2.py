"""
caso_en_contra_t2.py — B6.1, tanda final, T1, punto 2.9: el caso en contra del freno por id de modelo, para la prueba de
punta a punta del lanzador. Es el de la tanda 1 (data/experiment/tanda1/t2/caso_en_contra_t2.py), con el TO por defecto de
la tanda final. Agrega a la `e1_extraccion.db` de una COPIA del repo una fila de `corpus_<TO>_e1` en
`access_log` y en `cache`, con el esquema de llm_cache.py:133-157 y un id de modelo distinto de
claude-haiku-4-5-20251001. Relanzado sobre esa copia, el lanzador tiene que frenar antes del primer TO.

Rehúsa escribir en una base que esté dentro de --repo-real (el repo): solo escribe en la copia.

Uso: <python> -B caso_en_contra_t2.py --copia <raíz de la copia> --repo-real <repo> [--to ri_bdp]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
import sys
import time
from pathlib import Path

sys.dont_write_bytecode = True
DB_REL = "data/experiment/reextraccion_v2/e1_extractor/cache/e1_extraccion.db"
ID_DISTINTO = "claude-haiku-4-5-caso-en-contra"
DOMINIO = "e1_extraccion"
NAMESPACE = "e1_extraccion|cv=e1-extractor-v1-p322c5a23e9b7|think=0"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--copia", type=Path, required=True)
    ap.add_argument("--repo-real", type=Path, required=True)
    ap.add_argument("--to", default="ri_bdp")
    a = ap.parse_args()
    db = (a.copia / DB_REL).resolve()
    if db.is_relative_to(a.repo_real.resolve()) or not db.exists():
        print("error: la base no es de una copia o no existe")
        return 2
    clave = hashlib.sha256(f"caso en contra T1 de la tanda final {a.to}".encode()).hexdigest()
    ts = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    con = sqlite3.connect(str(db))
    try:
        with con:
            con.execute("INSERT INTO cache (key, namespace, domain, created_at, model, input_tokens, output_tokens, "
                        "cache_read_tokens, cache_write_tokens, stop_reason, thinking_enabled, request_json, raw_json) "
                        "VALUES (?, ?, ?, ?, ?, 0, 0, 0, 0, 'tool_use', 0, ?, ?)",
                        (clave, NAMESPACE, DOMINIO, ts, ID_DISTINTO, json.dumps({"caso_en_contra": True}),
                         json.dumps({"model": ID_DISTINTO})))
            con.execute("INSERT INTO access_log (ts, key, domain, hit, run_label) VALUES (?, ?, ?, 0, ?)",
                        (ts, clave, DOMINIO, f"corpus_{a.to}_e1"))
        n = con.execute("SELECT count(*) FROM access_log WHERE run_label = ?", (f"corpus_{a.to}_e1",)).fetchone()[0]
    finally:
        con.close()
    print(f"fila agregada a la copia: run_label corpus_{a.to}_e1, model {ID_DISTINTO}; filas con esa etiqueta: {n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
