"""B6.1, tanda 1, T4, primer tramo, punto 8 (cegamiento) y decisión de la autora del 18/10/2026, punto 1.3: la población de la vigilancia
(2) en el primer intento, por TO, solo a <salida NO_ABRIR>. No se sortea ni se reporta: el script no imprime ninguna cifra, solo el
sha256 del archivo que escribe. Corre sobre una copia.
  - Por TO, con la regla del código de la tanda 0 (data/experiment/tanda0/code/lectura_e6_tanda0.py:231-252): el primer registro de cada
    unidad en extracciones_e1.jsonl, sin error y con 0 relaciones validadas (cero_relaciones_primer_intento, sobre todas las unidades
    de E1, como ese código); y lo mismo sobre las unidades aceptadas (los tres estados de aceptación juntos), que es la contraparte de
    las 198 de la extracción final que se sortearon en T3.
Uso: python3 -I -B no_abrir_t4t1.py <raíz> <salida NO_ABRIR.json>
"""
import hashlib
import json
import sys
from datetime import datetime
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ, OUT = Path(sys.argv[1]).resolve(), Path(sys.argv[2])
assert OUT.name.startswith("NO_ABRIR_"), "la salida tiene que ser un NO_ABRIR_"
X = RAIZ / "data/experiment/reextraccion_v2"
SAL = X / "corpus_tanda1/salida_r2b"
ACEPTADOS = ("completo_ok_directo", "aceptado_con_residuales", "aceptado_tras_reintento")


def lineas(p: Path) -> list:
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()] if p.exists() else []


tos = sorted(t["id"] for t in json.loads((X / "manifiestos/tanda1_20tos_r2b.json").read_text(encoding="utf-8"))["tos"])
por_to = {}
for to in tos:
    prim = {}
    for x in lineas(SAL / to / "extracciones_e1.jsonl"):
        prim.setdefault(x["chunk_id"], x)
    ult = {}
    for r in lineas(SAL / to / "finales.jsonl"):
        ult[r["chunk_id"]] = r
    acept = {c for c, r in ult.items() if r["estado"] in ACEPTADOS}
    cero = {c for c, x in prim.items() if not x.get("error") and not (x.get("validacion") or {}).get("relaciones")}
    por_to[to] = {"unidades_e1": len(prim), "cero_relaciones_primer_intento": len(cero),
                  "cero_relaciones_primer_intento_en_las_aceptadas": len(cero & acept)}
res = {"hora": datetime.now().astimezone().isoformat(timespec="seconds"),
       "que_es": "vigilancia (2), población del primer intento por TO (decisión de la autora del 18/10/2026, punto 1.3); no se sortea "
                 "ni se reporta", "regla": "lectura_e6_tanda0.py:231-252 (primer registro por unidad en extracciones_e1.jsonl)",
       "por_to": por_to,
       "total": {k: sum(v[k] for v in por_to.values()) for k in ("unidades_e1", "cero_relaciones_primer_intento",
                                                                 "cero_relaciones_primer_intento_en_las_aceptadas")}}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("escrito", OUT.name, "sha256", hashlib.sha256(OUT.read_bytes()).hexdigest())
