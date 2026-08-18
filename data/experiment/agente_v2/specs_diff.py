"""
specs_diff.py — Diff de las specs que lee el modelo: bloque TOOLS del harness
(harness.py, líneas ~240-286, importado sin editar) vs specs_tools_v2.json
(U-A1.2). Salida: specs_diff_v1_v2.txt (tabla para la Metodología) + diff del
prompt del sistema (harness vs SYSTEM_PROMPT_V2_PROPUESTO, INERTE, pendiente de laudo).
Determinístico.
"""

from __future__ import annotations

import difflib
import json
import sys
from pathlib import Path

AGENTE_V2_DIR = Path(__file__).resolve().parent
NEO4J_DIR = AGENTE_V2_DIR.parent / "neo4j"
for _p in (str(NEO4J_DIR), str(AGENTE_V2_DIR)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from tools_v2 import TOOLS_V2  # noqa: E402  (agrega EVAL_DIR al path vía grafos)
from harness import TOOLS, SYSTEM_PROMPT  # noqa: E402  (solo import)
from agente_v2 import SYSTEM_PROMPT_V2_PROPUESTO  # noqa: E402

SALIDA = AGENTE_V2_DIR / "specs_diff_v1_v2.txt"


def _js(x) -> list:
    return json.dumps(x, ensure_ascii=False, indent=2).splitlines()


def main():
    partes = []
    partes.append("# Specs de tools que lee el modelo — v1 (harness.TOOLS) vs v2 (specs_tools_v2.json)\n")
    for t1, t2 in zip(TOOLS, TOOLS_V2):
        assert t1["name"] == t2["name"]
        d = list(difflib.unified_diff(_js(t1), _js(t2), fromfile=f"harness.TOOLS[{t1['name']}]",
                                      tofile=f"specs_tools_v2.json[{t2['name']}]", lineterm="", n=2))
        partes.append(f"\n## {t1['name']}\n")
        partes.append("\n".join(d) if d else "(sin cambios: byte-idéntico)")
    partes.append("\n\n# Prompt del sistema — harness.SYSTEM_PROMPT vs SYSTEM_PROMPT_V2_PROPUESTO (INERTE, pendiente de laudo)\n")
    d = list(difflib.unified_diff(SYSTEM_PROMPT.splitlines(), SYSTEM_PROMPT_V2_PROPUESTO.splitlines(),
                                  fromfile="harness.SYSTEM_PROMPT", tofile="SYSTEM_PROMPT_V2_PROPUESTO", lineterm="", n=1))
    partes.append("\n".join(d))
    txt = "\n".join(partes) + "\n"
    SALIDA.write_text(txt, encoding="utf-8")
    print(txt)


if __name__ == "__main__":
    main()
