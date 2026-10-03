"""U-DIAG-PROCESO: detector de remisiones del perfil r2 (reglas a-i) sobre el texto propio y cada
tramo heredado de las diez fichas, en el espejo copiado. Solo lectura. Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B menciones_fichas.py <espejo> <fichas_e0r2.json> <salida_e0r2>
"""
import json, sys
from pathlib import Path
espejo = Path(sys.argv[1]).resolve()
sys.dont_write_bytecode = True
sys.path.insert(0, str(espejo / "data/experiment/reextraccion_v2/corpus_v2"))
import r1_referencias as R
assert Path(R.__file__).resolve().is_relative_to(espejo)
fichas = json.loads(Path(sys.argv[2]).read_text())
chunks = {}
for f in Path(sys.argv[3]).glob("chunks_*.json"):
    for c in json.loads(f.read_text()):
        chunks[c["id"]] = c
for fi in fichas:
    c = chunks[fi["chunk_id"]]
    propio = R.menciones_por_tramo([c["texto"]], c["to"], R.REGLAS_R2)
    hered = {}
    for h in c["herencia"]:
        ms = R.menciones_por_tramo([h["texto"]], c["to"], R.REGLAS_R2)
        if ms:
            hered.setdefault(h["unidad_origen"], []).extend(
                [{k: m.get(k) for k in ("clase", "puntos", "secciones", "evidencia")} for m in ms])
    print(fi["ficha"], fi["chunk_id"], "propio:", [{k: m.get(k) for k in ("clase", "puntos", "secciones", "evidencia")} for m in propio], "heredado:", hered)
