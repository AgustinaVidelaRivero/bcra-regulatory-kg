"""
t1_suite_sellados.py — U-REEXT-T0, T1, punto 4 (mandato firmado en e2027dd): la suite y las shapes sobre los grafos
sellados, para comparar el código de HEAD con el del punto 4. USD 0, sin red.

Grafos de la suite:
  - las cinco entradas de `estado_esperado` de scripts/regression_kg_esperado.json, con los parámetros de su entrada
    (KG-Refinado, KG-Reextraido-r1, KG-Base, KG-Reextraido y KG-Tanda0-Diez-r2a), con --esperado;
  - los tres ensamblados r1 de la tanda 0 (ens_cinco, ens_desarrollo y ens_diez; generación 3, cuarentena flaggeada,
    catálogo esquema_v3_clases.json) y el r2a de desarrollo (perfil r2), sin entrada en la fixture.
Shapes: perfil r2, fase r2a, sobre los dos grafos r2a, con su E0 (salida_tanda0_r2).

Corre desde la raíz de una COPIA del repo y escribe solo en --salida (fuera de la copia): un JSON por corrida y
`resumen_<etiqueta>.json` con el estado de cada ítem por grafo, la regresión contra la fixture y el resultado de cada
shape. `--comparar A B` compara dos resúmenes: ítems que cambian de estado, ítems nuevos y shapes que cambian.
  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/reext_t0/t1_suite_sellados.py \
      --salida DIR --etiqueta antes|despues
  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/reext_t0/t1_suite_sellados.py \
      --comparar DIR/resumen_antes.json DIR/resumen_despues.json
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
REX = "data/experiment/reextraccion_v2"
T0 = f"{REX}/corpus_tanda0"
CAT_V2 = "data/experiment/grafo_v2/esquema_v2_clases.json"
CAT_V3 = "data/experiment/esq_v3_miembros/esquema_v3_clases.json"
CAT_R2 = "data/experiment/catalogo_unico/generados_r2/catalogo_suite_r2.json"
FIXTURE = "scripts/regression_kg_esperado.json"
SUITE = [
    ("KG-Refinado", "data/experiment/grafo_v2/reensamblado_v3/kg.json", "2", "laudada", CAT_V2, "existente", True),
    ("KG-Reextraido-r1", f"{REX}/corpus_v2/salida_r1/kg.json", "3", "flaggeada", CAT_V2, "existente", True),
    ("KG-Base", "data/experiment/run_3_ppf_core/kg.json", "2", "laudada", CAT_V2, "existente", True),
    ("KG-Reextraido", f"{REX}/corpus_v2/salida/kg.json", "3", "flaggeada", CAT_V2, "existente", True),
    ("KG-Tanda0-Diez-r2a", f"{T0}/ens_diez_r2a/r2/kg.json", "3", "flaggeada", CAT_R2, "r2", True),
    ("KG-Tanda0-Desarrollo-r2a", f"{T0}/ens_desarrollo_r2a/r2/kg.json", "3", "flaggeada", CAT_R2, "r2", False),
    ("ens_cinco_r1", f"{T0}/ens_cinco/r1/kg.json", "3", "flaggeada", CAT_V3, "existente", False),
    ("ens_desarrollo_r1", f"{T0}/ens_desarrollo/r1/kg.json", "3", "flaggeada", CAT_V3, "existente", False),
    ("ens_diez_r1", f"{T0}/ens_diez/r1/kg.json", "3", "flaggeada", CAT_V3, "existente", False),
]
SHAPES = [("KG-Tanda0-Diez-r2a", f"{T0}/ens_diez_r2a/r2/kg.json"),
          ("KG-Tanda0-Desarrollo-r2a", f"{T0}/ens_desarrollo_r2a/r2/kg.json")]
E0_R2 = f"{REX}/e0_chunking/salida_tanda0_r2"
ENV = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}


def correr(args: list[str]) -> int:
    return subprocess.run([sys.executable, "-B", *args], cwd=REPO, env=ENV, capture_output=True, text=True).returncode


def bateria(sal: Path, etiqueta: str) -> dict:
    res: dict = {"etiqueta": etiqueta, "suite": {}, "shapes": {}}
    for nombre, kg, gen, pol, cat, perfil, con_fx in SUITE:
        out = sal / f"suite_{nombre}_{etiqueta}.md"
        cmd = ["scripts/regression_kg.py", "--kg", kg, "--generacion", gen, "--politica-cuarentena", pol,
               "--catalogo", cat, "--perfil", perfil, "--out", str(out)] + (["--esperado", FIXTURE] if con_fx else [])
        rc = correr(cmd)
        d = json.loads(out.with_suffix(".json").read_text(encoding="utf-8"))
        reg = d.get("regresion") or {}
        res["suite"][nombre] = {"rc": rc, "kg_sha256": d["parametros"]["kg_sha256"], "resumen": d["resumen"],
                                "estados": {it["id"]: it["estado"] for it in d["items"]},
                                "regresiones": [(x["item"], x["esperado"], x["medido"]) for x in reg.get("regresiones", [])],
                                "entrada": reg.get("entrada"), "sin_esperado": reg.get("sin_esperado"),
                                "nota_regresion": reg.get("nota")}
    for nombre, kg in SHAPES:
        out = sal / f"shapes_{nombre}_{etiqueta}.md"
        rc = correr(["scripts/shapes_validator.py", "--kg", kg, "--perfil", "r2", "--fase", "r2a", "--e0", E0_R2,
                     "--out", str(out)])
        d = json.loads(out.with_suffix(".json").read_text(encoding="utf-8"))
        res["shapes"][nombre] = {"rc": rc, "veredicto": d["veredicto"],
                                 "shapes": {k: [v["severidad"], v["result"], v["resumen"]] for k, v in d["shapes"].items()}}
    (sal / f"resumen_{etiqueta}.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return res


def comparar(a: dict, b: dict) -> dict:
    out: dict = {"suite": {}, "shapes": {}}
    for g in a["suite"]:
        ea, eb = a["suite"][g]["estados"], b["suite"][g]["estados"]
        out["suite"][g] = {"cambian": {i: [ea[i], eb[i]] for i in ea if i in eb and ea[i] != eb[i]},
                           "nuevos": {i: eb[i] for i in eb if i not in ea},
                           "quitados": sorted(i for i in ea if i not in eb),
                           "regresiones_antes": a["suite"][g]["regresiones"],
                           "regresiones_despues": b["suite"][g]["regresiones"],
                           "resumen": [a["suite"][g]["resumen"], b["suite"][g]["resumen"]]}
    for g in a["shapes"]:
        sa, sb = a["shapes"][g]["shapes"], b["shapes"][g]["shapes"]
        out["shapes"][g] = {"cambian": {k: [sa[k][:2], sb[k][:2]] for k in sa if k in sb and sa[k][:2] != sb[k][:2]},
                            "resumen_cambia": sorted(k for k in sa if k in sb and sa[k][2] != sb[k][2]),
                            "nuevas": {k: sb[k] for k in sb if k not in sa},
                            "veredicto": [a["shapes"][g]["veredicto"], b["shapes"][g]["veredicto"]]}
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path)
    ap.add_argument("--etiqueta")
    ap.add_argument("--comparar", nargs=2, type=Path)
    a = ap.parse_args()
    if a.comparar:
        r = comparar(*(json.loads(p.read_text(encoding="utf-8")) for p in a.comparar))
        print(json.dumps(r, ensure_ascii=False, indent=1))
        return 0
    sal = a.salida.resolve()
    if sal.is_relative_to(REPO):
        raise SystemExit("--salida no puede estar dentro de la copia")
    sal.mkdir(parents=True, exist_ok=True)
    r = bateria(sal, a.etiqueta)
    for g, v in r["suite"].items():
        print(g, v["rc"], v["resumen"], "regresiones:", v["regresiones"])
    for g, v in r["shapes"].items():
        print("shapes", g, v["rc"], v["veredicto"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
