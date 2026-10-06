"""U-REEXT-T0, T3, punto 2 (decisión 2): copia de r2_codigo2/c2_control_repro.py con dos cambios — la copia excluye
los .env (no se copia ningún archivo de clave) y el sha256 de los dos r2a se compara con los del cierre de C2 —.

U-R2-CODIGO-2, C2 — control de reproducción con el código de C2 (USD 0, sin API ni Neo4j), sobre una COPIA del repo
(CLAUDE.md §4, reglas k y l). Es el control de P3b-2 de U-PROMPT-R2 (`prompt_r2/p3b2/control_reproduccion_p3b2.py`)
con lo que pide el mandato de U-R2-CODIGO-2 para C2:

  1. sha256 de los archivos del repo (rastreados y no ignorados) antes;
  2. copia sin enlaces simbólicos (rsync --copy-links), sin .git, .venv ni data/raw; se controla que no tenga enlaces;
  3. en la copia:
     a. E0 legada de la tanda 0 (correr_e0.py sin --version-e0, manifiesto tanda0_10tos) → los 34 archivos de
        e0_chunking/salida_tanda0 del repo, byte a byte;
     b. los tres ensamblados sellados (tanda0_ens_cinco, _diez y _desarrollo, motor replica), con --entrada de
        ruta absoluta → los 13 archivos de corpus_tanda0/ens_<x> del repo;
     c. los dos grafos r2a (--perfil-r2 con la e0-r2 de f8dedd4): el sha256 del grafo, que difiere del sellado por
        los cambios declarados de C2 (los lista `c2_cadena.py`);
     d. la suite del perfil r2 sobre los dos grafos de (c): los estados de los ítems contra los sellados
        (`estado_esperado`, KG-Tanda0-Diez-r2a, de scripts/regression_kg_esperado.json; para desarrollo, la corrida
        de M2, medicion_r2a/m2/suite_desarrollo.json); todo ítem que cambia de estado se lista;
     e. las shapes del perfil r2, fase r2a, sobre los grafos de (c) y sobre los sellados (en la copia): todo shape
        que cambia de resultado se lista;
  4. sha256 del repo después: tiene que ser igual.
Las comparaciones de reportes normalizan la ruta de salida (los reportes la registran).

Uso: <python del repo> c2_control_repro.py <repo> <dir de trabajo fuera del repo> [--out <json>]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("repo", type=Path)
ap.add_argument("trabajo", type=Path)
ap.add_argument("--out", type=Path, default=None)
A = ap.parse_args()
REPO = A.repo.resolve()
TRAB = A.trabajo.resolve()
assert REPO not in TRAB.parents and TRAB != REPO, "el directorio de trabajo no puede estar dentro del repo"
PY = str(REPO / ".venv" / "bin" / "python")
COPIA = TRAB / "copia"
OUT = TRAB / "salidas"
ENV = {"PYTHONDONTWRITEBYTECODE": "1", "PATH": "/usr/bin:/bin"}
REX = "data/experiment/reextraccion_v2"
MAN = f"{REX}/manifiestos"
SUITE = ["scripts/regression_kg.py", "--perfil", "r2", "--generacion", "3", "--catalogo",
         "data/experiment/catalogo_unico/generados_r2/catalogo_suite_r2.json", "--politica-cuarentena", "flaggeada",
         "--esperado", "scripts/regression_kg_esperado.json"]
res: dict = {}
# los del cierre de C2 de U-R2-CODIGO-2 (r2_codigo2/salidas/c2_control_repro.json; decisión 2 de la autora)
SHA_C2 = {"diez": "70d51e429b0e2cc1aafa697e32bc83462d371dfdd5edafb34e92fe4f7be45bdd",
          "desarrollo": "fa4c1043d859081e49dce6cb940a9f5d4c09fc6d449efb85355f95312257178a"}


def sha_repo() -> dict:
    r = subprocess.run(["git", "ls-files", "-z", "-co", "--exclude-standard"], cwd=REPO, capture_output=True,
                       check=True)
    out = {}
    for rel in sorted(x for x in r.stdout.decode().split("\0") if x):
        p = REPO / rel
        if p.is_file():
            out[rel] = hashlib.sha256(p.read_bytes()).hexdigest()
    return out


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def comparar_dir(a: Path, b: Path, normalizar: tuple = ()) -> dict:
    fa = {str(p.relative_to(a)) for p in a.rglob("*") if p.is_file()}
    fb = {str(p.relative_to(b)) for p in b.rglob("*") if p.is_file()}
    iguales, iguales_norm, distintos = [], [], []
    for rel in sorted(fa & fb):
        x, y = (a / rel).read_bytes(), (b / rel).read_bytes()
        if x == y:
            iguales.append(rel)
            continue
        tx, ty = x.decode("utf-8", "replace"), y.decode("utf-8", "replace")
        for viejo, nuevo in normalizar:
            tx, ty = tx.replace(viejo, nuevo), ty.replace(viejo, nuevo)
        (iguales_norm if tx == ty else distintos).append(rel)
    return {"solo_en_repo": sorted(fa - fb), "solo_en_copia": sorted(fb - fa), "iguales": len(iguales),
            "iguales_con_ruta_normalizada": iguales_norm, "distintos": distintos, "total_repo": len(fa)}


def correr(args: list[str], nombre: str) -> int:
    r = subprocess.run([PY, "-B", *args], cwd=COPIA, env=ENV, capture_output=True, text=True)
    (OUT / f"{nombre}.log").write_text(r.stdout[-20000:] + "\n--- stderr ---\n" + r.stderr[-20000:], encoding="utf-8")
    return r.returncode


def estados_suite(p: Path) -> dict:
    d = json.loads(p.read_text(encoding="utf-8"))
    return {it["id"]: it["estado"] for it in d["items"]}


def resultados_shapes(p: Path) -> dict:
    d = json.loads(p.read_text(encoding="utf-8"))
    return {k: v.get("result") for k, v in d["shapes"].items()}


def cambios(a: dict, b: dict) -> dict:
    return {k: [a.get(k), b.get(k)] for k in sorted(set(a) | set(b)) if a.get(k) != b.get(k)}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    antes = sha_repo()
    res["repo_archivos"] = len(antes)
    if COPIA.exists():
        subprocess.run(["rm", "-rf", str(COPIA)], check=True)
    subprocess.run(["rsync", "-a", "--copy-links", "--exclude", ".git", "--exclude", ".venv", "--exclude", ".env", "--exclude", "data/raw",
                    "--exclude", "__pycache__", "--exclude", "*.pyc", f"{REPO}/", f"{COPIA}/"], check=True)
    enlaces = sum(1 for _r, ds, fs in os.walk(COPIA) for x in ds + fs if os.path.islink(os.path.join(_r, x)))
    res["copia_enlaces"] = enlaces
    assert enlaces == 0
    # a. E0 legada
    sal = OUT / "e0_legada"
    rc = correr([f"{REX}/e0_chunking/correr_e0.py", "--manifiesto", f"{MAN}/tanda0_10tos.json", "--salida", str(sal)],
                "e0_legada")
    res["e0_legada"] = {"rc": rc, **comparar_dir(REPO / REX / "e0_chunking" / "salida_tanda0", sal)}
    entrada = str(COPIA / REX / "corpus_tanda0" / "salida_dirigida")
    # b. ensamblados sellados, con --entrada de ruta absoluta
    for x in ("cinco", "diez", "desarrollo"):
        sal = OUT / f"ens_{x}"
        rc = correr(["data/experiment/tanda0/code/ensamblar_tanda0.py", "--manifiesto", f"{MAN}/tanda0_ens_{x}.json",
                     "--entrada", entrada, "--salida", str(sal)], f"ens_{x}")
        res[f"ens_{x}"] = {"rc": rc, **comparar_dir(
            REPO / REX / "corpus_tanda0" / f"ens_{x}", sal,
            ((str(sal), "<SALIDA>"), (entrada, f"{REX}/corpus_tanda0/salida_dirigida"), (str(COPIA) + "/", ""),
             (str(REPO) + "/", ""), (f"{REX}/corpus_tanda0/ens_{x}", "<SALIDA>")))}
    # c, d, e. r2a, suite y shapes
    fixture = json.loads((REPO / "scripts" / "regression_kg_esperado.json").read_text(encoding="utf-8"))
    sellado_suite = {"diez": {k: v["estado"] for k, v in
                              fixture["estado_esperado"]["KG-Tanda0-Diez-r2a"]["items"].items()},
                     "desarrollo": estados_suite(REPO / "data/experiment/medicion_r2a/m2/suite_desarrollo.json")}
    for x in ("diez", "desarrollo"):
        sal = OUT / f"ens_{x}_r2a"
        rc = correr(["data/experiment/tanda0/code/ensamblar_tanda0.py", "--manifiesto", f"{MAN}/tanda0_ens_{x}.json",
                     "--entrada", entrada, "--perfil-r2", "--e0-r2", f"{REX}/e0_chunking/salida_tanda0_r2",
                     "--salida", str(sal)], f"ens_{x}_r2a")
        kg = sal / "r2" / "kg.json"
        sellado = REPO / REX / "corpus_tanda0" / f"ens_{x}_r2a" / "r2" / "kg.json"
        fila = {"rc": rc, "sha256_kg": sha(kg) if kg.exists() else None, "sha256_sellado": sha(sellado),
                "sha256_cierre_c2": SHA_C2[x], "igual_al_cierre_c2": kg.exists() and sha(kg) == SHA_C2[x]}
        rc_s = correr([*SUITE, "--kg", str(kg), "--registro-dir", str(sal / "r2"), "--out", str(OUT / f"suite_{x}.md")],
                      f"suite_{x}")
        nuevo = estados_suite(OUT / f"suite_{x}.json")
        fila["suite"] = {"rc": rc_s, "resumen": json.loads((OUT / f"suite_{x}.json").read_text(encoding="utf-8"))[
            "resumen"], "items_que_cambian_de_estado": cambios(sellado_suite[x], nuevo)}
        sh = {}
        for etiqueta, g, reg in (("nuevo", kg, sal / "r2"),
                                 ("sellado", COPIA / REX / "corpus_tanda0" / f"ens_{x}_r2a" / "r2" / "kg.json",
                                  COPIA / REX / "corpus_tanda0" / f"ens_{x}_r2a" / "r2")):
            o = OUT / f"shapes_{x}_{etiqueta}.md"
            rc_h = correr(["scripts/shapes_validator.py", "--kg", str(g), "--perfil", "r2", "--fase", "r2a",
                           "--registro-dir", str(reg), "--e0", f"{REX}/e0_chunking/salida_tanda0_r2", "--out", str(o)],
                          f"shapes_{x}_{etiqueta}")
            sh[etiqueta] = (rc_h, resultados_shapes(o.with_suffix(".json")))
        fila["shapes"] = {"rc": [sh["sellado"][0], sh["nuevo"][0]],
                          "shapes_que_cambian": cambios(sh["sellado"][1], sh["nuevo"][1]),
                          "fail_nuevo": sorted(k for k, v in sh["nuevo"][1].items() if v == "FAIL")}
        res[f"ens_{x}_r2a"] = fila
    despues = sha_repo()
    res["repo_igual_antes_y_despues"] = antes == despues
    res["repo_archivos_que_cambiaron"] = sorted(k for k in set(antes) | set(despues) if antes.get(k) != despues.get(k))
    texto = json.dumps(res, ensure_ascii=False, indent=1).replace(str(TRAB), "<TRABAJO>")
    (OUT / "control_repro.json").write_text(texto + "\n", encoding="utf-8")
    if A.out is not None:
        A.out.write_text(texto + "\n", encoding="utf-8")
    print(json.dumps({k: (v if not isinstance(v, dict) else {kk: vv for kk, vv in v.items()
                                                             if kk in ("rc", "iguales", "distintos", "total_repo",
                                                                       "sha256_kg", "igual_al_cierre_c2")})
                      for k, v in res.items()}, ensure_ascii=False))


if __name__ == "__main__":
    main()
