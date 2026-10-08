"""U-E3-LISTAS, O5: para cada candidato del lado «sí es faltante», si el tramo declarado [meta_normativo] está también en
alguna entidad extraída (ventanas de 5 tokens compartidas con su label o su descripción). Solo lectura sobre la copia.
Uso: python ue3_o5_tramo_extraido.py <copia> <candidatos.json>"""
import json, sys
from pathlib import Path
C, CAND = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
REX = C / "data/experiment/reextraccion_v2"
sys.path.insert(0, str(C / "data/experiment/pyd_r2/code"))
import validador_r2 as V  # noqa: E402

def ventanas(t):
    k = V.norm_tokens(t or ""); return {tuple(k[i:i + 5]) for i in range(len(k) - 4)}

d = json.loads(CAND.read_text(encoding="utf-8"))
for f in d["si_es_faltante"]:
    to = f["chunk_id"].split("::")[0]
    x = next(json.loads(l) for l in (REX / f"corpus_tanda0/salida_r2b/{to}/extracciones_e1.jsonl").read_text(encoding="utf-8").splitlines()
             if json.loads(l)["chunk_id"] == f["chunk_id"])
    wt = ventanas(f["tramo"])
    cubre = [(e["local_id"], e["type"], len(wt & ventanas(e.get("label", "") + " " + (e.get("properties") or {}).get("descripcion", ""))))
             for e in x["validacion"]["entidades"] if e["type"] != "TextoOrdenado"]
    cubre = [c for c in cubre if c[2]]
    print(f["chunk_id"], "| ventanas del tramo:", len(wt), "| entidades que lo comparten:", cubre)
