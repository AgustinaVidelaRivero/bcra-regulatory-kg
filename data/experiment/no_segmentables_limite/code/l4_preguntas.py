"""U-NOSEG-LIMITE, L4 — verificación del «solo» de las preguntas candidatas.

Para cada pregunta candidata (redactada desde una página leída de la muestra), busca sus términos
literales en el texto de los otros TOs: los chunks de la partición de los 138 reconocidos plenos
(`b584_particion/<to>/chunks_<to>.json`, texto propio y herencia) y los chunks de E0 de los cinco de
desarrollo (`e0_chunking/salida_enm01/chunks_<to>.json`). Normaliza mayúsculas, acentos y cortes de
línea con guion. Escribe `l4_preguntas.json`; la decisión de descartar o conservar cada candidata
queda en el campo `decision` del JSON de entrada, no la toma el script.

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/no_segmentables_limite/code/l4_preguntas.py
"""

from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
PART = REPO / "data" / "experiment" / "segmentacion_84" / "b584_particion"
DEV = REPO / "data" / "experiment" / "reextraccion_v2" / "e0_chunking" / "salida_enm01"
OUT = REPO / "data" / "experiment" / "no_segmentables_limite"
DEV_TOS = ("cap", "cla", "ext", "pro", "ric")


def norm(s: str) -> str:
    s = re.sub(r"-\n", "", s)
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", s)


def textos() -> dict[str, str]:
    part = json.loads((PART / "particion_152.json").read_text(encoding="utf-8"))["por_to"]
    res = {}
    for to, v in sorted(part.items()):
        if v["clase"] != "reconocido_pleno":
            continue
        ch = json.loads((PART / to / f"chunks_{to}.json").read_text(encoding="utf-8"))
        ch = ch["chunks"] if isinstance(ch, dict) else ch
        res[to] = norm("\n".join([c["texto"] for c in ch] + [h["texto"] for c in ch for h in c.get("herencia", [])]))
    for to in DEV_TOS:
        ch = json.loads((DEV / f"chunks_{to}.json").read_text(encoding="utf-8"))
        ch = ch["chunks"] if isinstance(ch, dict) else ch
        res[to] = norm("\n".join([c["texto"] for c in ch] + [h["texto"] for c in ch for h in c.get("herencia", [])]))
    return res


def main() -> None:
    cand = json.loads((OUT / "l4_preguntas_candidatas.json").read_text(encoding="utf-8"))
    tx = textos()
    assert len(tx) == 143, len(tx)
    for q in cand["candidatas"]:
        q["busqueda"] = {}
        for t in q["terminos"]:
            nt = norm(t)
            hits = {to: s.count(nt) for to, s in tx.items() if nt in s}
            ctx = {}
            for to in list(hits)[:5]:
                i = tx[to].find(nt)
                ctx[to] = tx[to][max(0, i - 120): i + len(nt) + 120]
            q["busqueda"][t] = {"tos_con_el_termino": hits, "contexto": ctx}
    cand["_meta"]["corpus_de_busqueda"] = {"tos": len(tx), "reconocidos_plenos": len(tx) - len(DEV_TOS),
                                           "desarrollo": list(DEV_TOS)}
    (OUT / "l4_preguntas.json").write_text(json.dumps(cand, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for q in cand["candidatas"]:
        print(q["id"], q["to"], q["pagina"], {t: sorted(b["tos_con_el_termino"]) for t, b in q["busqueda"].items()})


if __name__ == "__main__":
    main()
