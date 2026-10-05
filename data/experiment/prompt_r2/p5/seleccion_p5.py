"""
seleccion_p5.py — U-PROMPT-R2, P5 (USD 0, sin API): las unidades de la medición, que se sellan antes de correr.

  - E1: las 27 unidades de P4b (p4b/salida/seleccion_p4b.json, sha256 e2551cf3…), en su orden y con su grupo.
  - E3: 10 unidades (cambio de la autora sobre el texto preparado: 10, no 5):
      - las 5 de la pata de E3 de P4b (`pata_e3`);
      - 5 más de las 27, por regla: el ítem del ejemplo (`cla::5.1.1.1`) y la unidad de f (`cap::6.2.2.6`), las dos
        con lectura propia en P4b y sin E3 todavía; y una de cada grupo c, d y e, que no tienen ninguna en la pata,
        sorteada con random.Random(f"{SEMILLA}:e3:{grupo}").choice sobre las unidades del grupo en el orden de P4b.
        Los grupos b1 y b2 (ítems) quedan sin unidad nueva: la pata ya trae sus dos encabezados.
  - El reintento por salida mal formada, forzado con temperatura 1: la unidad más corta de las 27 por texto propio
    (la regla de la llamada del tercer escalón de P4b).

Escribe solo --salida. Uso (desde la raíz del repo o de una copia):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p5/seleccion_p5.py --salida DIR
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
SEL_P4B = AQUI.parent / "p4b" / "salida" / "seleccion_p4b.json"
SHA_SEL_P4B = "e2551cf3"
E0 = REPO / "data" / "experiment" / "reextraccion_v2" / "e0_chunking" / "salida_tanda0_r2b"
SEMILLA = "U-PROMPT-R2:P5:2026-10-05"
FIJAS_E3 = ("cla::5.1.1.1", "cap::6.2.2.6")
SORTEADAS_E3 = ("c", "d", "e")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    sal = a.salida.resolve()
    if REPO in sal.parents or sal == REPO:
        raise SystemExit("--salida no puede estar dentro del repo")
    crudo = SEL_P4B.read_bytes()
    sha = hashlib.sha256(crudo).hexdigest()
    if not sha.startswith(SHA_SEL_P4B):
        raise SystemExit(f"seleccion_p4b.json no es la sellada: {sha[:12]}…")
    p4b = json.loads(crudo)
    unidades = [{"grupo": g, "id": c} for g, ids in p4b["grupos"].items() for c in ids]
    ids27 = [u["id"] for u in unidades]
    if len(ids27) != 27 or len(set(ids27)) != 27:
        raise SystemExit(f"se esperaban 27 unidades distintas: {len(ids27)}")
    pata = list(p4b["pata_e3"])
    sorteadas = {g: random.Random(f"{SEMILLA}:e3:{g}").choice(p4b["grupos"][g]) for g in SORTEADAS_E3}
    nuevas = list(FIJAS_E3) + [sorteadas[g] for g in SORTEADAS_E3]
    e3 = pata + nuevas
    if len(e3) != 10 or len(set(e3)) != 10 or not set(e3) <= set(ids27):
        raise SystemExit(f"la lista de E3 no son 10 unidades distintas de las 27: {e3}")
    chunks = {}
    for to in sorted({c.split("::")[0] for c in ids27}):
        chunks.update({c["id"]: c for c in json.loads((E0 / f"chunks_{to}.json").read_text(encoding="utf-8"))})
    chars = {c: len(chunks[c].get("texto") or "") for c in ids27}
    forma = min((chars[c], c) for c in ids27)[1]
    out = {"semilla": SEMILLA, "seleccion_p4b_sha256": sha, "e0": "data/experiment/reextraccion_v2/e0_chunking/"
           "salida_tanda0_r2b", "unidades": unidades,
           "e3": {"pata_p4b": pata, "nuevas": nuevas, "sorteadas": sorteadas, "fijas": list(FIJAS_E3), "todas": e3},
           "reintento_forma": {"unidad": forma, "chars_propio": chars[forma],
                               "regla": "la unidad más corta de las 27 por texto propio"},
           "chars_propio": chars}
    sal.mkdir(parents=True, exist_ok=True)
    texto = json.dumps(out, ensure_ascii=False, indent=1) + "\n"
    (sal / "seleccion_p5.json").write_text(texto, encoding="utf-8")
    print(json.dumps({"sha256": hashlib.sha256(texto.encode("utf-8")).hexdigest(), "e3": e3,
                      "sorteadas": sorteadas, "reintento_forma": forma}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
