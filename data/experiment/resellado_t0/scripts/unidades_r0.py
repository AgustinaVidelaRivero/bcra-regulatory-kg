"""Las 20 unidades de R0: los chunk_id de los renglones que R0 anexó a corpus_tanda0/salida_r2b/{ext,docvig}/finales.jsonl
(la versión de 2d0f5277 menos la de 1d690df3, renglón a renglón), contra la lista sellada de O3 (cc6b0cd6…) y contra
r0/esperados_r0.json. Solo lee (git show). Uso, desde la raíz de una copia con .git a mano o del repo:
python -I -B unidades_r0.py <repo> <salida.json>"""
import hashlib, json, subprocess, sys
from pathlib import Path
R = Path(sys.argv[1])
T = "data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b"
def show(c, p):
    return subprocess.run(["git", "-C", str(R), "show", f"{c}:{p}"], capture_output=True, check=True).stdout
anexadas = {}
for to in ("ext", "docvig"):
    antes = show("1d690df3", f"{T}/{to}/finales.jsonl").decode("utf-8").splitlines()
    despues = show("2d0f5277", f"{T}/{to}/finales.jsonl").decode("utf-8").splitlines()
    assert despues[:len(antes)] == antes, "no es un anexo"
    for l in despues[len(antes):]:
        o = json.loads(l)
        anexadas[o["chunk_id"]] = o["estado"]
lista_raw = show("2d0f5277", "data/experiment/e3_listas/o3/lista_unidades_afectadas_tanda0.json")
lista = json.loads(lista_raw)
items = lista if isinstance(lista, list) else (lista.get("unidades") or lista.get("lista") or [])
ids = sorted({(x["chunk_id"] if isinstance(x, dict) else x) for x in items})
res = {"unidades_r0": sorted(anexadas), "n": len(anexadas), "estado_final": dict(sorted(anexadas.items())),
       "lista_sellada_sha256": hashlib.sha256(lista_raw).hexdigest(), "lista_sellada_n": len(ids),
       "igual_a_la_lista_sellada": sorted(anexadas) == ids}
Path(sys.argv[2]).write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in res.items() if k != "estado_final"}, ensure_ascii=False))
