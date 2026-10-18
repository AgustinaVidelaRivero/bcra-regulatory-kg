"""
mensajes_runner_a3.py — U-ALCANCE-E1, A3 (USD 0, sin API): corrida en seco del mensaje de E1 por el camino del runner, en las
tres tandas. Sigue a mensajes_runner_a2.py de A2, con la tanda final.

Importa runner_corpus de la copia que se pasa con --raiz (solo se agrega al sys.path el directorio del runner, como al
ejecutarlo: el runner agrega e1_extractor y lo demás) y lo configura con el manifiesto r2b de la tanda 0
(runner_corpus.configurar → perfil_e1.perfil("r2b") → prompt_r2b, con sus candados), como A2. Arma el pedido de E1 de cada
unidad con runner_corpus.PERFIL.build_request_kwargs, como fase_e1, y escribe en --salida (fuera de la copia), por unidad,
el mensaje de usuario y su línea de alcance:
  - tanda 0: las 2.439 unidades de salida_tanda0_r2b (runner_corpus.E0_DIR, con chunks_sin_ids_repetidos), y el sha256 de
    los mensajes unidos en el orden de `tos` del manifiesto, como r2_2_medicion.control_mensaje_e1 (R2-2);
  - tanda 1: los 20 documentos de `lista_final` de la lista de la tanda 1 (--lista), con sus unidades de la E0 corregida
    regenerada (--e0), cargadas como fase_e1: comun_e1.cargar_chunks y chunks_sin_ids_repetidos;
  - tanda final: los 98 documentos de `tanda_final.lista` de la cifra de S2c (--tanda-final), con sus unidades de la misma
    E0 corregida, cargadas igual. Las partes de una unidad que E1 parta por corte en la corrida no están: salen de la
    corrida;
  - las unidades de la fixture del candado del mensaje.
Además, de control: carga el manifiesto de la tanda 1 (el que usó su extracción) con manifiesto_corpus.cargar, que lo valida
contra la tabla TO→rol del perfil; y controla que todo módulo de data/experiment cargado, salvo este script, venga de la
copia. Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B mensajes_runner_a3.py --raiz COPIA --e0 DIR --lista JSON \\
      --tanda-final JSON --salida DIR --etiqueta head|a3
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

MANIFIESTO = "data/experiment/reextraccion_v2/manifiestos/tanda0_10tos_r2b.json"
MANIFIESTO_TANDA1 = "data/experiment/reextraccion_v2/manifiestos/tanda1_20tos_r2b.json"
FIXTURE = "data/experiment/reextraccion_v2/e1_extractor/candado_mensaje_r2b.json"


def sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--raiz", type=Path, required=True)
    ap.add_argument("--e0", type=Path, required=True)
    ap.add_argument("--lista", type=Path, required=True)
    ap.add_argument("--tanda-final", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    ap.add_argument("--etiqueta", required=True)
    a = ap.parse_args()
    raiz, sal, e0 = a.raiz.resolve(), a.salida.resolve(), a.e0.resolve()
    if raiz in sal.parents or sal == raiz:
        raise SystemExit("--salida no puede estar dentro de la copia")
    lista = json.loads(a.lista.read_text(encoding="utf-8"))
    tanda1 = [to for k in sorted(lista["lista_final"], key=int) for to in lista["lista_final"][k]]
    tanda_final = list(json.loads(a.tanda_final.read_text(encoding="utf-8"))["tanda_final"]["lista"])
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
    por_to = {"tanda1_e0_corregida": {}, "tandafinal_e0_corregida": {}}
    for origen, tos in (("tanda1_e0_corregida", tanda1), ("tandafinal_e0_corregida", tanda_final)):
        for to in tos:
            cs = RC.chunks_sin_ids_repetidos(RC.comun_e1.cargar_chunks((to,), e0_dir=e0), to)
            por_to[origen][to] = len(cs)
            filas += [fila(c, origen) for c in cs]
    fx = json.loads((raiz / FIXTURE).read_text(encoding="utf-8"))["chunks"]
    filas += [fila(c, "fixture_candado") for c in fx]
    man1 = RC.manifiesto_corpus.cargar(raiz / MANIFIESTO_TANDA1)   # frena si no valida contra el perfil
    import prompt_r2b  # noqa: PLC0415 — ya importado por el perfil
    ajenos = sorted(m.__file__ for n, m in list(sys.modules.items())
                    if n != "__main__" and getattr(m, "__file__", None) and "/data/experiment/" in m.__file__
                    and raiz not in Path(m.__file__).resolve().parents)
    resumen = {"etiqueta": a.etiqueta, "perfil": RC.PERFIL.nombre, "prefijo_hash": RC.PERFIL.prefijo_hash,
               "e0_dir_tanda0": str(Path(RC.E0_DIR).resolve().relative_to(raiz)),
               "prompt_r2b": str(Path(prompt_r2b.__file__).resolve().relative_to(raiz)),
               "derivado_en_el_modulo": len(prompt_r2b.REGISTRO_ALCANCE_R2B),
               "derivado_sha256_en_el_modulo": prompt_r2b.REGISTRO_ALCANCE_R2B_SHA256_ESPERADO,
               "manifiesto_tanda1_carga_con_sus_20": sorted(man1.ids) == sorted(tanda1),
               "modulos_de_data_experiment_fuera_de_la_copia": ajenos,
               "tanda0_unidades": len(mensajes_t0), "tanda0_tos": [t["id"] for t in man["tos"]],
               "tanda0_sha256_mensajes": sha("\n\x1e\n".join(mensajes_t0)),
               "tanda1_tos": tanda1, "tanda1_unidades_por_to": por_to["tanda1_e0_corregida"],
               "tanda1_unidades": sum(por_to["tanda1_e0_corregida"].values()),
               "tandafinal_tos": tanda_final, "tandafinal_unidades_por_to": por_to["tandafinal_e0_corregida"],
               "tandafinal_unidades": sum(por_to["tandafinal_e0_corregida"].values()),
               "fixture_sha256_mensajes": prompt_r2b.sha256_mensajes(fx), "fixture_unidades": len(fx),
               "filas": len(filas)}
    sal.mkdir(parents=True, exist_ok=True)
    with (sal / f"mensajes_{a.etiqueta}.jsonl").open("w", encoding="utf-8") as fh:
        for f in filas:
            fh.write(json.dumps(f, ensure_ascii=False) + "\n")
    (sal / f"resumen_{a.etiqueta}.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=1) + "\n",
                                                    encoding="utf-8")
    print(json.dumps({k: v for k, v in resumen.items() if not k.endswith("_por_to")}, ensure_ascii=False, indent=1))
    return 0 if not ajenos else 1


if __name__ == "__main__":
    raise SystemExit(main())
