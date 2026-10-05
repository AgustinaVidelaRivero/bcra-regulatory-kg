"""
fixtures_p3c2.py — U-PROMPT-R2, P3c-2 (USD 0): arma las dos fixtures de los candados de los mensajes (decisión 5 de la
autora sobre el FRENO P3c-1), con los conjuntos fijos de `p3c/salida/candados_p3c.json` (438bbd5):
  - candado_mensaje_r2b.json (E1, filas F22 y F22b): los 12 chunks de `e0_chunking/salida_tanda0_r2b` (9f6361e), en el
    orden de la cobertura, más una copia SINTÉTICA de `cap::1.4.1` con `archivo` = `ri2_ci.pdf`, la única entrada de
    `rol_por_to_r2.json` sin `rol_id`, para la rama del alcance por clase de `prompt_r2b.linea_alcance`;
  - candado_mensaje_e3.json (E3, fila F23): los 6 chunks, cada uno con una validación mínima con la marca de la forma
    r2 (las NOTAS de `notas_r2`) y otra sin ella (la NOTA de siempre), más un caso SINTÉTICO con una omisión
    `meta_normativo` declarada, para la NOTA de las omisiones de esquema (que depende de la salida de E1).
Escribe solo en --salida. Uso (desde la raíz de una copia):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p3c2/fixtures_p3c2.py --salida DIR
"""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
E0_R2B = REPO / "data" / "experiment" / "reextraccion_v2" / "e0_chunking" / "salida_tanda0_r2b"
CANDADOS = AQUI.parent / "p3c" / "salida" / "candados_p3c.json"
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
BASE_SINTETICO = "cap::1.4.1"
VALIDACION_R2 = {"forma_salida": "r2", "entidades": [], "relaciones": []}
VALIDACION_V3 = {"entidades": [], "relaciones": []}
VALIDACION_OMISIONES = {"forma_salida": "r2", "entidades": [], "relaciones": [],
                        "omisiones_no_prosa": ["[meta_normativo] (tramo del candado) — (nota del candado)"]}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, required=True)
    sal = ap.parse_args().salida.resolve()
    if REPO in sal.parents or sal == REPO:
        raise SystemExit("--salida no puede estar dentro del repo")
    cand = json.loads(CANDADOS.read_text(encoding="utf-8"))
    ch = {}
    for to in TOS:
        for c in json.loads((E0_R2B / f"chunks_{to}.json").read_text(encoding="utf-8")):
            ch[c["id"]] = c
    e1 = [ch[cid] for cid in cand["e1"]["conjunto_fijo"]]
    sint = copy.deepcopy(ch[BASE_SINTETICO])
    sint["id"] = f"{BASE_SINTETICO}::sintetico_alcance_clase"
    sint["archivo"] = "ri2_ci.pdf"
    sint["sintetico"] = ("copia de cap::1.4.1 con archivo ri2_ci.pdf: ejercita la rama del alcance por clase de "
                         "linea_alcance, que ninguna unidad de la tanda 0 usa")
    doc1 = {"descripcion": "Fixture del candado del mensaje de E1 r2b (P3c-2; filas F22 y F22b de la tabla de "
                           "reprocesamiento). Los chunks se copian de la E0 para que el candado no dependa de una E0 "
                           "que puede cambiar.",
            "fuente": "data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b (9f6361e); conjunto fijo de "
                      "data/experiment/prompt_r2/p3c/salida/candados_p3c.json (438bbd5)",
            "sinteticos": [sint["id"]], "chunks": e1 + [sint]}
    casos = []
    for cid in cand["e3"]["conjunto_fijo"]:
        casos.append({"chunk": ch[cid], "validacion": VALIDACION_R2})
        casos.append({"chunk": ch[cid], "validacion": VALIDACION_V3})
    casos.append({"chunk": ch[cand["e3"]["conjunto_fijo"][0]], "validacion": VALIDACION_OMISIONES,
                  "sintetico": "validación con una omisión meta_normativo declarada: ejercita la NOTA de las "
                               "omisiones de esquema, que depende de la salida de E1"})
    doc3 = {"descripcion": "Fixture del candado del mensaje de E3 (P3c-2; fila F23 de la tabla de reprocesamiento): "
                           "cada chunk con una validación mínima con la marca de la forma r2 y otra sin ella, y un "
                           "caso sintético para la NOTA de las omisiones.",
            "fuente": "data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b (9f6361e); conjunto fijo de "
                      "data/experiment/prompt_r2/p3c/salida/candados_p3c.json (438bbd5)",
            "casos": casos}
    sal.mkdir(parents=True, exist_ok=True)
    (sal / "candado_mensaje_r2b.json").write_text(json.dumps(doc1, ensure_ascii=False, indent=1) + "\n",
                                                  encoding="utf-8")
    (sal / "candado_mensaje_e3.json").write_text(json.dumps(doc3, ensure_ascii=False, indent=1) + "\n",
                                                 encoding="utf-8")
    print(len(doc1["chunks"]), "chunks en E1;", len(casos), "casos en E3")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
