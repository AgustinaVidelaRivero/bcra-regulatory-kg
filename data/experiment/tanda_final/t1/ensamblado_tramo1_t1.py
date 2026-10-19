"""
ensamblado_tramo1_t1.py — B6.1, tanda final, T1, punto 2.8 (pre-registro firmado de la tanda final, §4.1, punto 5; enmienda
9, punto 7): la prueba del ensamblado de un subconjunto, con la salida stub de los 30 del tramo 1 y el ensamblado de la
tanda 1. USD 0, sin API. Corre sobre una copia (--raiz) y escribe solo en --trabajo, fuera de la copia y del repo.

Pasos:
  1. los manifiestos de ensamblado de los 98 los deriva antes `nombres_remision/derivar_manifiesto_ensamblado_mesa.py`
     (el método del T3 de la tanda 1, con el corpus «tanda_final» de su contraste); este script los restringe a los 30
     del tramo 1 (los primeros 30 de `orden_corrida` del manifiesto de extracción): mismos `tos` y mismos
     `nombres_remision`, en el orden de corrida, con `nombre`, `descripcion` y `orden_corrida` nuevos, y `estimado_usd` y
     `checkpoint_cada` restringidos a los 30 (el tope y el margen quedan como están). El derivador frena
     con un corpus que no está en su medición, y la medición no tiene uno con los 30;
  2. corre `tanda0/code/ensamblar_tanda0.py` con los argumentos del T3 de la tanda 1
     (`tanda1/t3/scripts/cadena_t3.sh`): `--manifiesto`, `--entrada` (la salida stub del tramo 1), `--e0-r2` (la E0 de la
     tanda final) y `--salida`, y el sin cola con `--sin-cola`, cada uno en un proceso, desde la raíz de la copia, con
     PYTHONDONTWRITEBYTECODE=1 y sin la clave;
  3. carga los dos manifiestos con `manifiesto_corpus.cargar` y escribe un resumen (salida, nodos y aristas de cada
     `<salida>/r2/kg.json`, su sha256, lo que dice `reporte_ensamblado_r2.json` de su doble corrida y el `resumen` del
     ensamblado) en <trabajo>/resumen_ensamblado_tramo1_t1.json.
Uso: PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B ensamblado_tramo1_t1.py --raiz <copia> --manifiesto-98 <json>
       --manifiesto-98-sincola <json> --entrada <salida stub del tramo 1> --trabajo <dir>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
MAN_EXT_REL = "data/experiment/reextraccion_v2/manifiestos/tanda_final_98tos_r2b.json"
E0_REL = "data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b"
ENS_REL = "data/experiment/tanda0/code/ensamblar_tanda0.py"
N_TRAMO_1 = 30


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def restringir(m98: dict, tramo1: list[str], nombre: str) -> dict:
    m = json.loads(json.dumps(m98))
    por_id = {t["id"]: t for t in m["tos"]}
    m["tos"] = [por_id[t] for t in tramo1]
    m["orden_corrida"] = list(tramo1)
    lim = m["limites"]
    lim["estimado_usd"] = {t: lim["estimado_usd"][t] for t in tramo1}       # manifiesto_corpus.cargar: una clave por id
    lim["checkpoint_cada"] = {t: v for t, v in lim["checkpoint_cada"].items() if t in tramo1}
    m["nombre"] = nombre
    m["descripcion"] = (m["descripcion"] + " Restringido a los 30 TOs del tramo 1 de la tanda final (los primeros 30 de "
                        "orden_corrida de tanda_final_98tos_r2b.json), con sus nombres_remision tal cual y estimado_usd y "
                        "checkpoint_cada restringidos a los 30, para la prueba del ensamblado de un subconjunto de T1 "
                        "(data/experiment/tanda_final/t1/ensamblado_tramo1_t1.py).")
    return m


def main() -> int:
    ap = argparse.ArgumentParser()
    for k in ("--raiz", "--manifiesto-98", "--manifiesto-98-sincola", "--entrada", "--trabajo"):
        ap.add_argument(k, type=Path, required=True)
    a = ap.parse_args()
    raiz, trabajo = a.raiz.resolve(), a.trabajo.resolve()
    if trabajo.is_relative_to(raiz):
        raise SystemExit("--trabajo no puede estar dentro de la copia")
    trabajo.mkdir(parents=True, exist_ok=False)
    tramo1 = json.loads((raiz / MAN_EXT_REL).read_text(encoding="utf-8"))["orden_corrida"][:N_TRAMO_1]
    res = {"tramo_1": tramo1, "manifiesto_extraccion_sha256": sha(raiz / MAN_EXT_REL), "grafos": {}}
    sys.path.insert(0, str(raiz / "data" / "experiment" / "reextraccion_v2"))
    import manifiesto_corpus as MC                       # noqa: PLC0415
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    env.pop("ANTHROPIC_API_KEY", None)
    for nombre, m98p, sin_cola in (("tanda_final_ens_tramo1_r2b", a.manifiesto_98, False),
                                   ("tanda_final_ens_tramo1_r2b_sincola", a.manifiesto_98_sincola, True)):
        m98 = json.loads(m98p.read_text(encoding="utf-8"))
        assert [t["id"] for t in m98["tos"]] and set(tramo1) <= {t["id"] for t in m98["tos"]}
        man = trabajo / "manifiestos" / f"{nombre}.json"
        man.parent.mkdir(exist_ok=True)
        man.write_text(json.dumps(restringir(m98, tramo1, nombre), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        carga = MC.cargar(man)
        salida = trabajo / nombre.replace("tanda_final_ens_", "ens_")
        cmd = [sys.executable, "-B", ENS_REL, "--manifiesto", str(man), "--entrada", str(a.entrada.resolve()),
               "--e0-r2", E0_REL, "--salida", str(salida), "--resumen-json", str(trabajo / f"resumen_{nombre}.json")]
        if sin_cola:
            cmd.append("--sin-cola")
        with (trabajo / f"consola_{nombre}.txt").open("w", encoding="utf-8") as out:
            rc = subprocess.run(cmd, cwd=raiz, env=env, stdout=out, stderr=subprocess.STDOUT).returncode
        kg = salida / "r2" / "kg.json"                      # el ensamblado r2 escribe en <salida>/r2/
        g = {"rc": rc, "manifiesto_sha256": sha(man), "manifiesto_carga": len(carga.ids),
             "nombres_remision_tos": sum(1 for t in json.loads(man.read_text(encoding="utf-8"))["tos"] if t["nombres_remision"]),
             "kg_json": kg.is_file()}
        if kg.is_file():
            d = json.loads(kg.read_text(encoding="utf-8"))
            g.update({"kg_sha256": sha(kg), "nodos": len(d.get("nodes", d.get("nodos", []))),
                      "aristas": len(d.get("edges", d.get("aristas", d.get("relationships", [])))),
                      "archivos_de_salida": sorted(p.name for p in kg.parent.iterdir())})
            rep = kg.parent / "reporte_ensamblado_r2.json"
            if rep.is_file():
                r = json.loads(rep.read_text(encoding="utf-8"))
                g["reporte"] = {k: r.get(k) for k in ("sha256_kg", "sha256_kg_en_disco", "doble_corrida_byte_identica",
                                                      "nodes_total", "edges_total", "con_cola")}
        rj = trabajo / f"resumen_{nombre}.json"
        if rj.is_file():
            g["resumen_ensamblado"] = json.loads(rj.read_text(encoding="utf-8"))
        res["grafos"][nombre] = g
    res["corrio"] = all(g["rc"] == 0 and g["kg_json"] for g in res["grafos"].values())
    (trabajo / "resumen_ensamblado_tramo1_t1.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n",
                                                               encoding="utf-8")
    print(json.dumps({k: ({n: {x: y for x, y in g.items() if x not in ("resumen_ensamblado", "archivos_de_salida")}
                           for n, g in v.items()} if k == "grafos" else v) for k, v in res.items() if k != "tramo_1"},
                     ensure_ascii=False))
    return 0 if res["corrio"] else 1


if __name__ == "__main__":
    sys.exit(main())
