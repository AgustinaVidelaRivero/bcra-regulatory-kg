#!/usr/bin/env python3
"""control_ev2_a2_2.py — Un control de EV2 por código que imprime solo cuentas, sin ningún id ni texto (USD 0):

  · el esquema que A2.2 lee (comun_a2_2.cargar_preguntas, con la ruta y el sha256 del pre-registro), las 40 preguntas y los 164
    criterios;
  · cuántas anclas hay (`gold.ancla`, forma «to:punto», como las lee `smoke/verificar_territorio.py:61`) y cuántas no están en la
    E0 del grafo, la E0 r2b de desarrollo (`mcp_vector/manifiestos_e0/e0_tanda0_r2b_desarrollo.json`, con el sha256 de cada
    archivo): un ancla está si su punto es una unidad de su TO o si tiene unidades que descienden de él (la regla del bake-off,
    `bakeoff_embeddings/code/mapeo_gold_chunk.py`, `resolver`, que usa analizar_a2_2.resolver). Tiene que dar 0;
  · cuántas preguntas tienen alguna ancla en la cola (A-D11, (a)), con la lista de la cola de `controles_a2_2/`.
Escribe las mismas cuentas en a2_2/controles/control_ev2_a2_2.json.
Uso: .venv/bin/python -B data/experiment/banco_mcp/a2_2/control_ev2_a2_2.py
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
if str(AQUI) not in sys.path:
    sys.path.insert(0, str(AQUI))
import comun_a2_2 as K               # noqa: E402
import analizar_a2_2 as AN           # noqa: E402

MANIFIESTO_E0 = K.BANCO_DIR / "mcp_vector" / "manifiestos_e0" / "e0_tanda0_r2b_desarrollo.json"
COLA_SHA256 = "a7342c262b4b90a5b8adb65bacaa93983f1e2c478c80761ca06b8b7bcf38a55d"
COLA_LISTA_SHA256 = "85707ea95800bd0c67c207c18cfcc2eec62f58b716f6667b7ef0f229e5db0fa9"


def controlar(preguntas_ruta: Path = K.EV2_PATH, sha: str = K.EV2_SHA256, real: bool = True, cola_ruta: Path = K.COLA,
              e0_dir: Path = K.E0_DIR, manifiesto: Path = MANIFIESTO_E0, controlar_e0: bool = True) -> dict:
    preguntas = K.cargar_preguntas(preguntas_ruta, sha, real=real)
    if controlar_e0:
        man = json.loads(manifiesto.read_text(encoding="utf-8"))
        if any(K.sha256_file(e0_dir / f) != s for f, s in man["archivos"].items()):
            raise K.FrenoA22("la E0 r2b de desarrollo no es la del manifiesto del índice")
    e0 = AN.cargar_e0(e0_dir)
    n_unidades = sum(len(v) for v in e0.values())
    cola = json.loads(Path(cola_ruta).read_text(encoding="utf-8"))
    if real and (K.sha256_file(Path(cola_ruta)) != COLA_SHA256
                 or K.sha256_texto("".join(x + "\n" for x in cola["ids"])) != COLA_LISTA_SHA256):
        raise K.FrenoA22("la lista de la cola no es la del pre-registro")
    cola_crudos = set(cola["ids"])
    cola_ids = {AN.unidad_de(i) for i in cola_crudos}
    e0_ids = {c["id"] for v in e0.values() for c in v}
    instancias = [a for v in preguntas.values() for a in v["anclas"]]
    distintas = sorted(set(instancias))
    vias_inst = {"a": 0, "b": 0, "ninguna": 0}
    for a in instancias:
        vias_inst[AN.resolver(a, e0)[1]] += 1
    vias_dist = {"a": 0, "b": 0, "ninguna": 0}
    en_cola_dist = 0
    for a in distintas:
        ids, via = AN.resolver(a, e0)
        vias_dist[via] += 1
        en_cola_dist += bool(set(ids) & cola_ids)
    pc = AN.preguntas_con_cola(preguntas, cola_ids, e0)["por_pregunta"]
    return {"n_preguntas": len(preguntas), "n_criterios": sum(len(v["criterios"]) for v in preguntas.values()),
            "esquema": "id, pregunta, to, gold.criterios[*].{criterio, cita_textual}, gold.ancla: el de comun_fidelidad.cargar_gold",
            "e0": {"n_unidades": n_unidades, "tos": list(K.E0_TOS), "controlada_contra_el_manifiesto": controlar_e0},
            "anclas": {"instancias": len(instancias), "distintas": len(distintas),
                       "preguntas_sin_ancla": sum(1 for v in preguntas.values() if not v["anclas"]),
                       "por_via_instancias": vias_inst, "por_via_distintas": vias_dist,
                       "no_estan_en_la_E0_instancias": vias_inst["ninguna"], "no_estan_en_la_E0_distintas": vias_dist["ninguna"],
                       "cola_cuenta_de_ids": len(cola_crudos), "cola_ids_que_son_partes": sum(1 for i in cola_crudos if "::parte" in i),
                       "cola_ids_que_no_estan_en_la_E0": len(cola_crudos - e0_ids),
                       "cola_unidades_que_no_estan_en_la_E0": len(cola_ids - e0_ids),
                       "distintas_que_caen_en_la_cola": en_cola_dist},
            "preguntas_con_alguna_ancla_en_la_cola": sum(pc.values()),
            "preguntas_sin_ninguna_ancla_en_la_cola": sum(1 for x in pc.values() if not x)}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, default=AQUI / "controles" / "control_ev2_a2_2.json")
    a = ap.parse_args(argv)
    try:
        r = controlar()
    except K.FrenoA22 as e:
        print("FRENO:", e)
        return 1
    a.salida.parent.mkdir(parents=True, exist_ok=True)
    a.salida.write_text(json.dumps(r, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    an = r["anclas"]
    print(f"preguntas {r['n_preguntas']}; criterios {r['n_criterios']}")
    print(f"anclas: {an['instancias']} (distintas {an['distintas']}); por vía, instancias {an['por_via_instancias']}, "
          f"distintas {an['por_via_distintas']}")
    print(f"anclas que no están en la E0 del grafo: {an['no_estan_en_la_E0_instancias']} (distintas "
          f"{an['no_estan_en_la_E0_distintas']}); ids de la cola {an['cola_cuenta_de_ids']}, de ellos partes "
          f"{an['cola_ids_que_son_partes']}; ids de la cola que no están en la E0 {an['cola_ids_que_no_estan_en_la_E0']}, "
          f"unidades {an['cola_unidades_que_no_estan_en_la_E0']}")
    print(f"preguntas con alguna ancla en la cola: {r['preguntas_con_alguna_ancla_en_la_cola']}; sin ninguna: "
          f"{r['preguntas_sin_ninguna_ancla_en_la_cola']}")
    ok = r["n_preguntas"] == K.EV2_N_PREGUNTAS and r["n_criterios"] == K.EV2_N_CRITERIOS and an["no_estan_en_la_E0_instancias"] == 0
    print("control de EV2:", "OK" if ok else "FRENO")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
