"""
mensajes_runner_a1.py — U-ALCANCE-E1, A1 (USD 0, sin API): corrida en seco del mensaje de E1 por el camino del runner.

Importa runner_corpus de la copia que se pasa con --raiz (solo se agrega al sys.path el directorio del runner, como al
ejecutarlo: el runner agrega e1_extractor y lo demás), lo configura con el manifiesto r2b de la tanda 0
(runner_corpus.configurar → perfil_e1.perfil("r2b") → prompt_r2b, con sus candados) y arma el pedido de E1 de cada unidad
con runner_corpus.PERFIL.build_request_kwargs, como fase_e1. Escribe en --salida (fuera de la copia), por unidad, el mensaje
de usuario y su línea de alcance:
  - tanda 0: las 2.439 unidades de salida_tanda0_r2b (runner_corpus.E0_DIR, con chunks_sin_ids_repetidos), y el sha256 de
    los mensajes unidos en el orden de `tos` del manifiesto, como r2_2_medicion.control_mensaje_e1 (R2-2);
  - tanda 1: los 20 documentos del ejemplo del §7 del protocolo (ri_pgn en lugar de ri_cc), con sus unidades de la
    partición vigente (segmentacion_84/b584_particion) y, de referencia, de la salida de S1 de U-SEG-OFICIAL en disco;
  - las 17 unidades de la fixture del candado del mensaje.
Controla que todo módulo de data/experiment cargado, salvo este script, venga de la copia. Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B mensajes_runner_a1.py --raiz COPIA --salida DIR --etiqueta head|nuevo
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

TANDA1 = ("ayccef", "expaef", "opefci", "adrei", "ri_ccna", "ri_pgn", "ri_rml", "ri_gerc", "snp_cheq", "ceninf", "cirmo3",
          "snp_tr", "lingeef", "depaho", "cajasc", "manori", "efemin", "nmcief", "ri_dcpc", "ri_oc")
MANIFIESTO = "data/experiment/reextraccion_v2/manifiestos/tanda0_10tos_r2b.json"
B584 = "data/experiment/segmentacion_84/b584_particion"
S1 = "data/experiment/segmentacion_oficial_e0r2/s1/e0"
FIXTURE = "data/experiment/reextraccion_v2/e1_extractor/candado_mensaje_r2b.json"


def sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--raiz", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    ap.add_argument("--etiqueta", required=True)
    a = ap.parse_args()
    raiz, sal = a.raiz.resolve(), a.salida.resolve()
    if raiz in sal.parents or sal == raiz:
        raise SystemExit("--salida no puede estar dentro de la copia")
    sys.path.insert(0, str(raiz / "data" / "experiment" / "reextraccion_v2" / "corpus_v2"))
    import runner_corpus as RC  # noqa: PLC0415 — el runner, con su sys.path
    RC.configurar(RC.manifiesto_corpus.cargar(raiz / MANIFIESTO))
    if RC.PERFIL.nombre != "r2b":
        raise SystemExit(f"perfil {RC.PERFIL.nombre}")

    def mensaje(c: dict) -> str:
        return RC.PERFIL.build_request_kwargs(c, model=RC.MODEL_E1)["messages"][0]["content"]

    def fila(c: dict, origen: str) -> dict:
        m = mensaje(c)
        alc = [x for x in m.split("\n") if x.startswith("Alcance de este TO")]
        return {"origen": origen, "to": c["to"], "id": c["id"], "archivo": c["archivo"], "sha256": sha(m),
                "caracteres": len(m), "linea_alcance": alc[0] if alc else None, "mensaje": m}

    filas, mensajes_t0 = [], []
    man = json.loads((raiz / MANIFIESTO).read_text(encoding="utf-8"))
    for t in man["tos"]:
        for c in RC.chunks_sin_ids_repetidos(RC.comun_e1.cargar_chunks((t["id"],), e0_dir=RC.E0_DIR), t["id"]):
            f = fila(c, "tanda0_salida_tanda0_r2b")
            filas.append(f)
            mensajes_t0.append(f["mensaje"])
    for to in TANDA1:
        for origen, d in (("tanda1_b584", raiz / B584 / to), ("tanda1_s1", raiz / S1)):
            for c in RC.comun_e1.cargar_chunks((to,), e0_dir=d):
                filas.append(fila(c, origen))
    fx = json.loads((raiz / FIXTURE).read_text(encoding="utf-8"))["chunks"]
    filas += [fila(c, "fixture_candado") for c in fx]
    import prompt_r2b  # noqa: PLC0415 — ya importado por el perfil
    ajenos = sorted(m.__file__ for n, m in list(sys.modules.items())
                    if n != "__main__" and getattr(m, "__file__", None) and "/data/experiment/" in m.__file__
                    and raiz not in Path(m.__file__).resolve().parents)
    resumen = {"etiqueta": a.etiqueta, "perfil": RC.PERFIL.nombre, "prefijo_hash": RC.PERFIL.prefijo_hash,
               "e0_dir": str(Path(RC.E0_DIR).resolve().relative_to(raiz)),
               "prompt_r2b": str(Path(prompt_r2b.__file__).resolve().relative_to(raiz)),
               "modulos_de_data_experiment_fuera_de_la_copia": ajenos,
               "tanda0_unidades": len(mensajes_t0), "tanda0_tos": [t["id"] for t in man["tos"]],
               "tanda0_sha256_mensajes": sha("\n\x1e\n".join(mensajes_t0)),
               "fixture_sha256_mensajes": prompt_r2b.sha256_mensajes(fx), "fixture_unidades": len(fx),
               "filas": len(filas)}
    sal.mkdir(parents=True, exist_ok=True)
    with (sal / f"mensajes_{a.etiqueta}.jsonl").open("w", encoding="utf-8") as fh:
        for f in filas:
            fh.write(json.dumps(f, ensure_ascii=False) + "\n")
    (sal / f"resumen_{a.etiqueta}.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=1) + "\n",
                                                    encoding="utf-8")
    print(json.dumps(resumen, ensure_ascii=False, indent=1))
    return 0 if not ajenos else 1


if __name__ == "__main__":
    raise SystemExit(main())
