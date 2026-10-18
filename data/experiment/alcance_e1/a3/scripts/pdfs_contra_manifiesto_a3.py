"""U-ALCANCE-E1, A3 (USD 0, sin API; solo lectura): los PDFs no se rastrean (`.gitignore`: data/experiment/**/*.pdf), así que no
tienen blob en la base. Se controlan contra los dos registros rastreados que dan su sha256 (y cuyo blob se controla con
blobs_contra_base_a3.py):
  - los 152 de escalado_prep/pdfs/, contra data/experiment/escalado_prep/manifest_pdfs.sha256 (formato de shasum);
  - los 5 de subset/, contra la tabla de data/experiment/reextraccion_v2/e0_chunking/INFORME_E0.md.
También controla que en cada carpeta no haya otro PDF. Uso: python3 -I -B pdfs_contra_manifiesto_a3.py <copia> <salida.json>
"""
import hashlib
import json
import re
import sys
from pathlib import Path

c, salida = Path(sys.argv[1]), Path(sys.argv[2])


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def contra(carpeta: Path, esperado: dict) -> dict:
    hay = {p.name: sha(p) for p in sorted(carpeta.glob("*.pdf"))}
    return {"carpeta": str(carpeta.relative_to(c)), "esperados": len(esperado), "en_la_copia": len(hay),
            "iguales": sum(hay.get(n) == s for n, s in esperado.items()),
            "distintos_o_faltantes": sorted(n for n, s in esperado.items() if hay.get(n) != s),
            "de_mas": sorted(set(hay) - set(esperado))}


man = {}
for linea in (c / "data/experiment/escalado_prep/manifest_pdfs.sha256").read_text(encoding="utf-8").splitlines():
    s, n = linea.split(None, 1)
    man[n.strip()] = s
inf = dict((n, s) for s, n in re.findall(r"^\| `([0-9a-f]{64})` \| (\S+\.pdf) \|$",
                                          (c / "data/experiment/reextraccion_v2/e0_chunking/INFORME_E0.md")
                                          .read_text(encoding="utf-8"), flags=re.M))
res = {"escalado_prep": contra(c / "data/experiment/escalado_prep/pdfs", man),
       "subset": contra(c / "data/experiment/subset", inf)}
res["todo_igual"] = all(not r["distintos_o_faltantes"] and not r["de_mas"] and r["iguales"] == r["esperados"]
                        for r in res.values())
salida.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(res, ensure_ascii=False))
sys.exit(0 if res["todo_igual"] else 1)
