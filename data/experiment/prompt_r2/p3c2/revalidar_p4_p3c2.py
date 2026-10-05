"""
revalidar_p4_p3c2.py — U-PROMPT-R2, P3c-2 (USD 0): re-valida con el validador_r2 de P3c-2 la salida guardada del brazo
nuevo de P4 (`p4/salida/resultados_p4.jsonl`) y cuenta:
  - g: las omisiones con tramo cuyo tramo verifica (exacta o por tokens): lo esperado es 56 de 70
    (`p3c/salida/insumos_p4_p3c.json`, `omisiones_verificacion_del_tramo.con_regla_g`), con los contadores
    `omisiones.tramo_solo_heredado` y `omisiones.tramo_orden_de_lectura`;
  - el contador de las omisiones `meta_normativo` con marca (decisión 2), en las 24 del brazo nuevo y en las 9 que la
    autora confirmó como normativas. Con las siete clases de la enmienda 7 (corrección del FRENO P3c-2): cuántas de
    las 9 detecta, cuáles marcadas no están entre ellas y por qué clase entró cada una, el contador por clase del
    validador y, como control, lo que dan las cuatro clases de antes (deber, facultad, condición y excepción).
La E0 es la de P4: la e0-r2 de `f8dedd4` para los diez TOs y la de los cuatro fuera de muestra (`--e0-fuera`, la que
arma p4/e0_fuera_p4.py).

Escribe solo en --salida (revalidacion_p4_p3c2.json). Uso (desde la raíz de una copia):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p3c2/revalidar_p4_p3c2.py \
      --e0-fuera DIR_E0R2_FUERA --salida DIR
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
sys.path.insert(0, str(REPO / "data" / "experiment" / "pyd_r2" / "code"))
import validador_r2 as V  # noqa: E402

P4 = AQUI.parent / "p4" / "salida"
E0_R2 = REPO / "data" / "experiment" / "reextraccion_v2" / "e0_chunking" / "salida_tanda0_r2"
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
FUERA = ("ayccef", "expaef", "opefci", "adrei")
CUATRO = ("deber", "facultad", "condicion", "excepcion")   # las clases del contador antes de la corrección
NORMATIVAS_AUTORA = ("adrei::S5", "ext::10.4.2.7", "expaef::2.2.6.5", "ctacte::4.2.1", "ctacte::5.1.2.2",
                     "cla::5.1.1::intro", "ctacte::8.3::intro", "ctacte::8.4::intro", "ext::13.4.8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--e0-fuera", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    sal = a.salida.resolve()
    if REPO in sal.parents or sal == REPO:
        raise SystemExit("--salida no puede estar dentro del repo")
    ch = {}
    for d, tos in ((E0_R2, TOS), (a.e0_fuera, FUERA)):
        for to in tos:
            for c in json.loads((d / f"chunks_{to}.json").read_text(encoding="utf-8")):
                ch[c["id"]] = c
    niveles, cont, por_clase, meta = Counter(), Counter(), Counter(), []
    for x in (P4 / "resultados_p4.jsonl").read_text(encoding="utf-8").splitlines():
        if not x.strip():
            continue
        r = json.loads(x)
        cid, brazo = r["chunk_id"].split("|")
        if brazo != "nuevo" or r.get("tool_input") is None:
            continue
        v = V.validar(r["tool_input"], ch[cid], forma="r2")
        for o in v["omisiones"]:
            if o.get("tramo") is not None:
                niveles[o["tramo_verificado"]] += 1
        om = v["contadores"].get("omisiones", {})
        for k in ("tramo_solo_heredado", "tramo_orden_de_lectura", "meta_normativo_con_marca"):
            cont[k] += om.get(k, 0)
        for k, n in om.items():
            if k.startswith("meta_normativo_con_marca:"):
                por_clase[k.split(":", 1)[1]] += n
        for o in r["tool_input"].get("omisiones") or []:
            if o.get("categoria") == "meta_normativo" and o.get("tramo"):
                meta.append({"chunk": cid, "normativa_autora": cid in NORMATIVAS_AUTORA,
                             "marcas": V.marcas_meta_normativo(o["tramo"]), "tramo": o["tramo"]})
    out = {"comando": "data/experiment/prompt_r2/p3c2/revalidar_p4_p3c2.py --e0-fuera DIR --salida DIR",
           "g": {"omisiones_con_tramo": sum(niveles.values()), "por_nivel": dict(sorted(niveles.items())),
                 "verifican": niveles["exacta"] + niveles["tokens"],
                 "tramo_solo_heredado": cont["tramo_solo_heredado"],
                 "tramo_orden_de_lectura": cont["tramo_orden_de_lectura"]},
           "meta_normativo_con_marca": {
               "omisiones_meta_normativo": len(meta),
               "con_marca": sum(bool(m["marcas"]) for m in meta),
               "contador_del_validador": cont["meta_normativo_con_marca"],
               "normativas_autora": sum(m["normativa_autora"] for m in meta),
               "normativas_autora_con_marca": sum(m["normativa_autora"] and bool(m["marcas"]) for m in meta),
               "no_normativas_con_marca": sum((not m["normativa_autora"]) and bool(m["marcas"]) for m in meta),
               "normativas_autora_sin_marca": [m["chunk"] for m in meta if m["normativa_autora"] and not m["marcas"]],
               "no_normativas_con_marca_lista": [{"chunk": m["chunk"], "marcas": m["marcas"]} for m in meta
                                                 if not m["normativa_autora"] and m["marcas"]],
               "contador_por_clase_del_validador": {c: por_clase[c] for c in V.MARCAS_META_NORMATIVO},
               "control_cuatro_clases_de_antes": {
                   "con_marca": sum(any(c in CUATRO for c in m["marcas"]) for m in meta),
                   "normativas_autora_con_marca": sum(m["normativa_autora"] and any(c in CUATRO for c in m["marcas"])
                                                      for m in meta)},
               "filas": meta}}
    sal.mkdir(parents=True, exist_ok=True)
    (sal / "revalidacion_p4_p3c2.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n",
                                                  encoding="utf-8")
    print(json.dumps(out["g"], ensure_ascii=False))
    print(json.dumps({k: v for k, v in out["meta_normativo_con_marca"].items() if k != "filas"}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
