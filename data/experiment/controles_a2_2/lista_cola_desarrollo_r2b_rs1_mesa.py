"""lista_cola_desarrollo_r2b_rs1_mesa.py — mesa, §267: la lista de ids de las unidades de la cola humana del grafo de desarrollo
re-sellado (`KG_Tanda0_Desarrollo_r2b_rs1`, `acb26dca…`), que el pre-registro de A2.2 usa para la cifra sin la cola (D5; A2.1, `:142`).
No hay un archivo aparte con la lista: la cola es la regla de `data/experiment/resellado_t0/registro_vista_r2b_rs1.py:80-87` (las
unidades con estado `cola_humana*` como última versión en `corpus_tanda0/salida_r2b/*/finales.jsonl`), sobre los cinco documentos del
grafo, leída en el commit del sello (`4fe6ece`). La controla contra las marcas del `kg.json` sellado (`cola_humana` y `cola_chunks` de
cada nodo) y contra `resellado_t0/salidas/cola_y_poblacion_rs1.json` (54, y por documento). Solo lectura del repo, por `git show`.
USD 0. Uso: python3 -I -B lista_cola_desarrollo_r2b_rs1_mesa.py <repo> <salida.json>"""
import hashlib
import json
import subprocess
import sys
from collections import Counter

REPO, OUT = sys.argv[1], sys.argv[2]
SELLO = "4fe6ece"
T = "data/experiment/reextraccion_v2/corpus_tanda0/"
KG = T + "ens_desarrollo_r2b_rs1/r2/kg.json"
KG_SC = T + "ens_desarrollo_r2b_sincola_rs1/r2/kg.json"
CP = "data/experiment/resellado_t0/salidas/cola_y_poblacion_rs1.json"
TOS = ["cap", "cla", "ext", "pro", "ric"]
sha = lambda b: hashlib.sha256(b).hexdigest()  # noqa: E731
show = lambda c, p: subprocess.run(["git", "--no-optional-locks", "-C", REPO, "show", f"{c}:{p}"], capture_output=True, check=True).stdout  # noqa: E731
res = []


def c(n, ok, det=""):
    res.append(bool(ok))
    print("OK " if ok else "MAL", n, det)


fuentes, ult = {}, {}
for to in TOS:
    p = T + f"salida_r2b/{to}/finales.jsonl"
    b = show(SELLO, p)
    fuentes[p] = {"sha256_en_4fe6ece": sha(b), "igual_en_HEAD": sha(show("HEAD", p)) == sha(b)}
    for linea in b.decode("utf-8").splitlines():
        if linea.strip():
            o = json.loads(linea)
            ult[o["chunk_id"]] = o["estado"]
cola = sorted(k for k, v in ult.items() if str(v).startswith("cola_humana"))
kgb = show(SELLO, KG)
c("el kg.json del sello es el acb26dca y es el de HEAD", sha(kgb).startswith("acb26dca") and sha(show("HEAD", KG)) == sha(kgb))
kg = json.loads(kgb)
marcadas = set()
for n in kg["nodes"]:
    pr = n.get("properties") or {}
    if pr.get("cola_humana"):
        marcadas.update(pr.get("cola_chunks") or [])
c("las unidades marcadas en el kg.json son las de la regla", marcadas == set(cola), f"{len(marcadas)} y {len(cola)}")
cp = json.loads(show(SELLO, CP))
des = cp["grafos_nuevos"]["desarrollo_sin_cola"]
porto = Counter(x.split("::")[0] for x in cola)
c("54 y por documento, como cola_y_poblacion_rs1.json (desarrollo sin cola)", len(cola) == des["n_descartadas"] == 54
  and {k: v for k, v in des["cola_descartada_por_to"].items() if v} == dict(porto), str(dict(porto)))
sc = json.loads(show(SELLO, KG_SC))
c("el grafo sin la cola no lleva ningún nodo marcado", not any((n.get("properties") or {}).get("cola_humana") for n in sc["nodes"]))
texto = "".join(x + "\n" for x in cola)
salida = {"grafo": "KG_Tanda0_Desarrollo_r2b_rs1", "kg_json": KG, "kg_sha256": sha(kgb), "commit_sellado": SELLO,
          "regla": "data/experiment/resellado_t0/registro_vista_r2b_rs1.py:80-87 (estado cola_humana* como última versión en finales.jsonl)",
          "fuentes": fuentes, "n": len(cola), "por_documento": dict(sorted(porto.items())),
          "por_estado": dict(sorted(Counter(ult[x] for x in cola).items())), "ids": cola,
          "sha256_de_la_lista": sha(texto.encode()), "forma_de_la_lista": "los ids ordenados, uno por renglón, con salto final"}
open(OUT, "w", encoding="utf-8").write(json.dumps(salida, ensure_ascii=False, indent=2) + "\n")
print("n", len(cola), "| por documento", dict(sorted(porto.items())), "| sha256 de la lista", salida["sha256_de_la_lista"])
print("fuentes iguales en HEAD:", all(f["igual_en_HEAD"] for f in fuentes.values()))
print(f"controles: {sum(res)} de {len(res)}")
sys.exit(0 if all(res) else 1)
