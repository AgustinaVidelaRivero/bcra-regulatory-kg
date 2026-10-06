"""U-SINCOLA-T0, SC1, punto 2: comprobación en seco de `--sin-cola` sobre la cadena r2, sobre una COPIA del repo.

Importa `ensamblar_tanda0.py` como lo hace el ensamblado (su propio sys.path; patrón de
reext_t0/t3bis/pruebas_t3bis.py) y llama a `main()` con los argumentos de SC1.3 (manifiesto nuevo, --entrada
salida_r2b, --salida ens_<g>_r2b_sincola, --sin-cola, --e0-r2 salida_tanda0_r2b). Mientras corre, observa:
  - qué registros devuelve `runner_corpus.entrada_r2` por TO (los que entran a la cadena r2) y cuáles de ellos llevan
    `cola_humana`;
  - qué chunks marca `e2_lib.flaggear_cola_r2` (`chunks_de_cola`).
Después compara: (i) las unidades de la cola que entraron contra las 74 `cola_humana*` de finales.jsonl; (ii) el
sha256 del kg.json producido contra el sello del grafo r2b con cola (a9631a64… diez, 6e756043… desarrollo).
Si `--sin-cola` excluyera la cola en la cadena r2, (i) daría 0 unidades de la cola dentro y (ii) un sha distinto.

USD 0, sin red. Escribe la salida del ensamblado en la copia (--salida) y el JSON de --out.
Uso, desde la raíz de la copia:
  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B sc1_2_comprobacion_en_seco.py --grafo desarrollo --out X.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from collections import OrderedDict
from pathlib import Path

RAIZ = Path.cwd().resolve()                     # raíz de la COPIA (se corre desde ahí)
assert (RAIZ / "data/experiment/tanda0/code/ensamblar_tanda0.py").exists(), "correr desde la raíz de la copia"
sys.path.insert(0, str(RAIZ / "data" / "experiment" / "tanda0" / "code"))
import ensamblar_tanda0 as ENS  # noqa: E402  (mismo camino de imports que el runner)
import runner_corpus as RC      # noqa: E402  (en el path por ensamblar_tanda0; correr_cadena_r2 lo importa igual)
import e2_lib                   # noqa: E402

SELLOS = {"diez": "a9631a64b422bdae634fb05135373c6f04c6272cdf7acd43a1be9f5b6c1f5f57",
          "desarrollo": "6e7560433148cfe0c476cdd61199c32278187c4196d6f90dc0a38976a6d8e9a2"}
X = "data/experiment/reextraccion_v2"
T0 = f"{X}/corpus_tanda0"

ap = argparse.ArgumentParser()
ap.add_argument("--grafo", choices=("diez", "desarrollo"), required=True)
ap.add_argument("--out", required=True)
ap.add_argument("--salida", default=None, help="por defecto, corpus_tanda0/ens_<g>_r2b_sincola en la copia")
a = ap.parse_args()
g = a.grafo
salida = a.salida or f"{T0}/ens_{g}_r2b_sincola"

# 1. las 74 de finales.jsonl (última versión por chunk_id), como la precondición d
cola_finales: dict[str, str] = {}
for f in sorted((RAIZ / T0 / "salida_r2b").glob("*/finales.jsonl")):
    ultimo = {}
    for line in f.read_text(encoding="utf-8").splitlines():
        if line.strip():
            o = json.loads(line)
            ultimo[o["chunk_id"]] = o["estado"]
    cola_finales.update({k: v for k, v in ultimo.items() if str(v).startswith("cola_humana")})

# 2. observadores sobre las funciones que la cadena r2 llama (sin cambiar su comportamiento)
obs: dict = {"entrada_r2": OrderedDict(), "flaggear_cola_r2": OrderedDict(), "llamadas_entrada_r2": 0,
             "llamadas_flaggear": 0}
_entrada_r2 = RC.entrada_r2
_flaggear = e2_lib.flaggear_cola_r2


def entrada_r2_obs(to, tdir, chunks, perfil, validar):
    regs = _entrada_r2(to, tdir, chunks, perfil, validar)
    obs["llamadas_entrada_r2"] += 1
    en_cola = sorted(r["chunk_id"] for r in regs if r.get("cola_humana"))
    con_val = sum(1 for r in regs if r.get("validacion") is not None)
    obs["entrada_r2"][to] = {"registros": len(regs), "con_validacion": con_val,
                             "con_cola_humana": len(en_cola), "chunks_cola_humana": en_cola}
    return regs


def flaggear_obs(grafo, estado_por_chunk):
    r = _flaggear(grafo, estado_por_chunk)
    obs["llamadas_flaggear"] += 1
    obs["flaggear_cola_r2"][len(obs["flaggear_cola_r2"])] = r
    return r


RC.entrada_r2 = entrada_r2_obs
e2_lib.flaggear_cola_r2 = flaggear_obs

# 3. la corrida, con los argumentos de SC1.3 y --sin-cola, por main() del ensamblador
argv = ["ensamblar_tanda0.py", "--manifiesto", f"{X}/manifiestos/tanda0_ens_{g}_r2b_sincola.json",
        "--entrada", f"{T0}/salida_r2b", "--salida", salida, "--sin-cola",
        "--e0-r2", f"{X}/e0_chunking/salida_tanda0_r2b"]
sys.argv = argv
t0 = time.time()
rc = ENS.main()
dur = time.time() - t0

# 4. comparación
kg_p = RAIZ / salida / "r2" / "kg.json"
sha = hashlib.sha256(kg_p.read_bytes()).hexdigest() if kg_p.exists() else None
kg = json.loads(kg_p.read_text(encoding="utf-8")) if kg_p.exists() else {"nodes": [], "edges": []}
marca = lambda o: (o.get("properties") or {}).get("cola_humana") == "true"
entraron = sorted({c for v in obs["entrada_r2"].values() for c in v["chunks_cola_humana"]})
tos_del_grafo = sorted(obs["entrada_r2"])
cola_esperada_en_estos_tos = sorted(c for c in cola_finales if c.split("::")[0] in tos_del_grafo)
res = OrderedDict([
    ("unidad", "U-SINCOLA-T0, SC1, punto 2 (comprobación en seco de --sin-cola en la cadena r2)"),
    ("grafo", g), ("argv", argv), ("rc_main", rc), ("segundos", round(dur, 1)),
    ("cola_en_finales_jsonl", {"total": len(cola_finales),
                               "por_estado": dict(sorted(__import__("collections").Counter(cola_finales.values()).items())),
                               "en_los_tos_de_este_grafo": len(cola_esperada_en_estos_tos)}),
    ("llamadas", {"entrada_r2": obs["llamadas_entrada_r2"], "flaggear_cola_r2": obs["llamadas_flaggear"]}),
    ("entrada_r2_por_to", obs["entrada_r2"]),
    ("unidades_de_la_cola_que_entraron_a_la_cadena_r2", {"n": len(entraron), "chunks": entraron}),
    ("excluidas_por_sin_cola", {"n": len(set(cola_esperada_en_estos_tos) - set(entraron)),
                                "chunks": sorted(set(cola_esperada_en_estos_tos) - set(entraron))}),
    ("flaggear_cola_r2_por_llamada", obs["flaggear_cola_r2"]),
    ("kg_producido", {"ruta": str(kg_p.relative_to(RAIZ)) if kg_p.exists() else None, "sha256": sha,
                      "nodos": len(kg["nodes"]), "aristas": len(kg["edges"]),
                      "nodos_con_marca_cola": sum(1 for n in kg["nodes"] if marca(n)),
                      "aristas_con_marca_cola": sum(1 for e in kg["edges"] if marca(e))}),
    ("sello_r2b_con_cola", SELLOS[g]), ("kg_igual_al_sello_con_cola", sha == SELLOS[g]),
    ("veredicto", None)])
res["veredicto"] = ("--sin-cola NO excluye la cola en la cadena r2: entraron las mismas unidades y el kg es byte a byte "
                    "el sellado con cola" if (res["kg_igual_al_sello_con_cola"] and len(entraron) == len(cola_esperada_en_estos_tos))
                    else "--sin-cola cambió la cadena r2 (ver cifras)")
Path(a.out).parent.mkdir(parents=True, exist_ok=True)
Path(a.out).write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps({k: res[k] for k in ("grafo", "rc_main", "segundos", "unidades_de_la_cola_que_entraron_a_la_cadena_r2",
                                      "excluidas_por_sin_cola", "kg_producido", "kg_igual_al_sello_con_cola", "veredicto")}
                 | {"unidades_de_la_cola_que_entraron_a_la_cadena_r2": res["unidades_de_la_cola_que_entraron_a_la_cadena_r2"]["n"],
                    "excluidas_por_sin_cola": res["excluidas_por_sin_cola"]["n"]}, ensure_ascii=False, indent=1))
print("escrito:", a.out)
