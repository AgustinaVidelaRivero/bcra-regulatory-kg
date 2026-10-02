"""U-R2-CODIGO, R1.c — ejemplos y evidencia para el FRENO de R1.

Escribe, desde una salida e0-r2 y la E0 legada sellada:
  --out-txt  el texto de E0 legado y el e0-r2 de los chunks pedidos, y la
             herencia e0-r2 de los chunks pedidos con --herencia;
  --out-json la evidencia de la guarda G-RECUADRO en los chunks de la lista
             del mandato que no se marcan: fracción y celdas de cada tabla.
USD 0, sin LLM.

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/r2_codigo/r1c_ejemplos.py \\
    --e0-r2 <salida e0-r2> --out-txt <txt> --out-json <json> \\
    --chunks cap::2.12.2.6 cap::1.2 cap::6.2.1.1 ric::9.2.1 --herencia ric::11.2.3 \\
    --recuadros cap::4.2.1.1 ctacte::13.2 polcre::1.5
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
E0_LEGADA = REPO / "data" / "experiment" / "reextraccion_v2" / "e0_chunking" / "salida_tanda0"


def _chunk(d: Path, cid: str) -> dict:
    to = cid.split("::")[0]
    return {c["id"]: c for c in json.loads((d / f"chunks_{to}.json").read_text(
        encoding="utf-8"))}[cid]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--e0-r2", required=True)
    ap.add_argument("--out-txt", required=True)
    ap.add_argument("--out-json", required=True)
    ap.add_argument("--chunks", nargs="*", default=[])
    ap.add_argument("--herencia", nargs="*", default=[])
    ap.add_argument("--recuadros", nargs="*", default=[])
    a = ap.parse_args()
    r2 = Path(a.e0_r2)
    partes = []
    for cid in a.chunks:
        c, v = _chunk(r2, cid), _chunk(E0_LEGADA, cid)
        partes.append(f"===== {cid} — E0 legada\n{v['texto']}\n\n"
                      f"===== {cid} — e0-r2 (flags: {json.dumps(c['flags'], ensure_ascii=False)})\n"
                      f"{c['texto']}\n")
    for cid in a.herencia:
        c = _chunk(r2, cid)
        tramos = "\n".join(f"[{h['tipo']} | punto {h['unidad_origen']}]\n{h['texto']}"
                           for h in c["herencia"])
        partes.append(f"===== {cid} — herencia e0-r2\n{tramos}\n")
    Path(a.out_txt).write_text("\n".join(partes), encoding="utf-8")
    evidencia = {}
    for cid in a.recuadros:
        to = cid.split("::")[0]
        tablas = json.loads((r2 / f"tablas_{to}.json").read_text(encoding="utf-8"))["tablas"]
        evidencia[cid] = [{"tabla": t["id"], "fraccion": t["recuadro_prosa"]["fraccion"],
                           "es_recuadro": t["recuadro_prosa"]["es_recuadro"],
                           "marca": t["marca"],
                           "celdas": [s["filas"] for s in t["segmentos"]]}
                          for t in tablas if cid in t["chunks"]]
    Path(a.out_json).write_text(json.dumps(evidencia, ensure_ascii=False, indent=1) + "\n",
                                encoding="utf-8")


if __name__ == "__main__":
    main()
