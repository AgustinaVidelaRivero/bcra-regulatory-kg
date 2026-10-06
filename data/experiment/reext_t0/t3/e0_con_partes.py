"""U-REEXT-T0, T3, punto 2 (intrínsecas, informativas): una E0 de medición con las partes por corte, armada como la arma
el runner (runner_corpus.chunks_con_partes: cada unidad partida reemplazada por sus partes, en su lugar del orden
documental), para que scripts/metricas_intrinsecas.py --gen3 atribuya las provenances de las partes. Se escribe solo
fuera del repo (una copia o el scratchpad); la E0 del repo no se toca.

Uso: python -B e0_con_partes.py <e0_dir> <salida_r2b> <destino>"""
import json
import shutil
import sys
from pathlib import Path

E0, SAL, DEST = (Path(x) for x in sys.argv[1:4])
assert not DEST.exists(), f"{DEST} ya existe"
shutil.copytree(E0, DEST)
reemplazos = {}
for p in sorted(SAL.glob("*/particiones_por_corte.json")):
    to = p.parent.name
    partes = json.loads(p.read_text(encoding="utf-8"))
    f = DEST / f"chunks_{to}.json"
    chunks = json.loads(f.read_text(encoding="utf-8"))
    out = []
    for c in chunks:
        out.extend(partes[c["id"]]["partes"] if c["id"] in partes else [c])
    f.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    reemplazos[to] = {cid: [x["id"] for x in v["partes"]] for cid, v in partes.items()}
print(json.dumps({"reemplazos": reemplazos}, ensure_ascii=False))
