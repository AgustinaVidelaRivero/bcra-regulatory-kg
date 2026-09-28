"""
Verificación independiente de U-INV-CANDIDATOS (solo lectura; sin APIs).
  1. Embudo estrictamente decreciente y último conteo = candidatos del archivo.
  2. Cada bloque de texto del .md es copia textual del campo `texto` del
     fragmento E0 cuyo id lo encabeza.
  3. Palabras recomputadas desde E0 para cada candidato.
"""
import json
import re
from collections import Counter
from pathlib import Path

REPO = Path("/Users/agustinavidelarivero/INGENIERIA IA/TESIS/bcra-regulatory-kg")
E0 = REPO / "data/experiment/reextraccion_v2/e0_chunking/salida_enm01"
OUT = Path("/tmp/u_inv_candidatos")

r = json.loads((OUT / "resultado.json").read_text())
md = (OUT / "candidatos.md").read_text()
e0 = {}
for to in ("cap", "cla", "ext", "pro", "ric"):
    for x in json.loads((E0 / f"chunks_{to}.json").read_text()):
        e0[x["id"]] = x

emb = list(r["embudo"].values())
assert all(a > b for a, b in zip(emb, emb[1:])), emb
cabeceras = re.findall(r"^### C\d+ — ", md, flags=re.M)
assert len(cabeceras) == len(r["candidatos"]) == emb[-1], (len(cabeceras), len(r["candidatos"]), emb[-1])

bloques = re.findall(r"fragmento E0 `([^`]+)` \([^)]*\):\n\n````text\n(.*?)\n````", md, flags=re.S)
malos = [fid for fid, t in bloques if e0[fid]["texto"] != t]
assert not malos, malos
n_ref = md.split("## REFERENCIA", 1)[1].count("````text") if "## REFERENCIA" in md else 0

for c in r["candidatos"]:
    wo = sum(len(e0[f]["texto"].split()) for f in c["fragmentos_O"])
    assert wo == c["palabras_O"] and wo <= 80, c["O"]
    for d, w in zip(c["D"], c["palabras_D"]):
        wd = sum(len(e0[f]["texto"].split()) for f in c["fragmentos_D"][d])
        assert wd == w and wd <= 120, d

solo_mini = [c["n"] for c in r["candidatos"]
             if any(all(e0[f]["tipo"] == "mini_chunk" for f in fs) for fs in c["fragmentos_D"].values())]
print("embudo:", emb)
print("cabeceras de candidato en el .md:", len(cabeceras))
print("bloques de texto verificados contra E0:", len(bloques), "(de ellos en REFERENCIA:", n_ref, ")")
print("candidatos por TO:", dict(Counter(c["to"] for c in r["candidatos"])))
print("candidatos con algún d cuyo único texto E0 es mini_chunk:", len(solo_mini), solo_mini)
print("candidatos con d solo por procedencia múltiple:",
      [(c["n"], c["d_solo_por_multiprocedencia"]) for c in r["candidatos"] if c["d_solo_por_multiprocedencia"]])
print("candidatos con D en otro TO:", [(c["n"], c["O"], c["D"]) for c in r["candidatos"] if "no" in c["mismo_to"]])
print("candidatos con EV2:", [(c["n"], c["O"], c["ev2"]) for c in r["candidatos"] if c["ev2"]])
print("OK")
