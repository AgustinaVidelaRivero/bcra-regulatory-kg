"""
Verificación independiente de U-INV-CANDIDATOS-2 (solo lectura; sin APIs).
  1. Embudo estrictamente decreciente; último valor = fichas de v2_candidatos.md.
  2. Cada bloque de texto del .md es copia textual del campo `texto` del
     fragmento E0 cuyo id lo encabeza.
  3. Palabras y criterio 6 recomputados desde E0 para cada candidato.
  4. D(O) de cada candidato recomputado desde kg.json (provenance / destino).
  5. Suma del embudo por Texto Ordenado = embudo total.
"""
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path("/Users/agustinavidelarivero/INGENIERIA IA/TESIS/bcra-regulatory-kg")
KG = REPO / "data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json"
E0 = REPO / "data/experiment/reextraccion_v2/e0_chunking/salida_enm01"
OUT = Path("/tmp/u_inv_candidatos")

r = json.loads((OUT / "v2_resultado.json").read_text())
md = (OUT / "v2_candidatos.md").read_text()
e0 = {}
for to in ("cap", "cla", "ext", "pro", "ric"):
    for x in json.loads((E0 / f"chunks_{to}.json").read_text()):
        e0[x["id"]] = x

emb = [r["embudo"][c] for c in "123456"]
assert all(a > b for a, b in zip(emb, emb[1:])), emb
for c in "123456":
    assert sum(v[c] for v in r["embudo_por_to"].values()) == r["embudo"][c], c
fichas = re.findall(r"^### V\d+ — ", md, flags=re.M)
assert len(fichas) == len(r["candidatos"]) == emb[-1], (len(fichas), len(r["candidatos"]), emb[-1])

bloques = re.findall(r"fragmento E0 `([^`]+)` \([^)]*\):\n\n````text\n(.*?)\n````", md, flags=re.S)
assert len(bloques) == md.count("````text"), (len(bloques), md.count("````text"))
malos = [fid for fid, t in bloques if e0[fid]["texto"] != t]
assert not malos, malos
n_ref = md.split("## REFERENCIA", 1)[1].count("````text")

kg = json.loads(KG.read_text())
D = defaultdict(set)
for e in kg["edges"]:
    if e["relation"] == "referencia" and e.get("rol_fuente") == "referencia_cruzada":
        dest = e["properties"]["destino"]
        if re.fullmatch(r"\d+(\.\d+)*", dest.split("::", 1)[1]):
            D[f"{e['provenance']['to']}::{e['provenance']['punto']}"].add(dest)

for c in r["candidatos"]:
    assert sorted(D[c["O"]]) == sorted(c["D"]), (c["O"], sorted(D[c["O"]]), c["D"])
    wo = sum(len(e0[f]["texto"].split()) for f in c["fragmentos_O"])
    assert wo == c["palabras_O"] and wo <= 80, c["O"]
    assert any(e0[f]["tipo"] == "punto_terminal" for f in c["fragmentos_O"]), c["O"]
    for d, w in zip(c["D"], c["palabras_D"]):
        wd = sum(len(e0[f]["texto"].split()) for f in c["fragmentos_D"][d])
        assert wd == w and wd <= 120, d
        assert any(e0[f]["tipo"] == "punto_terminal" for f in c["fragmentos_D"][d]), d

assert sum(r["pro_conteo"].values()) == r["embudo_por_to"]["pro"]["1"] == len(r["pro"])
print("embudo:", emb)
print("embudo por TO:", {k: [v[c] for c in "123456"] for k, v in r["embudo_por_to"].items()})
print("fichas de candidato en el .md:", len(fichas))
print("bloques de texto verificados contra E0:", len(bloques), "(de ellos en REFERENCIA:", n_ref, ")")
print("D(O) recomputado desde kg.json coincide en los", len(r["candidatos"]), "candidatos")
print("candidatos por TO:", dict(Counter(c["to"] for c in r["candidatos"])))
print("pro: pares en criterio 1 =", len(r["pro"]), "; conteo por primer criterio no cumplido =", r["pro_conteo"])
print("OK")
