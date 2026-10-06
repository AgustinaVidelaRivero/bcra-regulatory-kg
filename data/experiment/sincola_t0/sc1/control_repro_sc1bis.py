"""U-SINCOLA-T0, SC1-bis, control (i) de la enmienda 1: copia de data/experiment/reext_t0/t3/control_repro_t3.py con
tres cambios declarados: (1) el python se pasa por --python (la fuente es una copia del repo, sin .venv); (2) el sha256
de la fuente se toma recorriendo sus archivos (la copia no tiene .git); (3) se agrega, para los dos r2b, la corrida sin
la bandera con el código nuevo (manifiestos tanda0_ens_<x>_r2b.json, --entrada salida_r2b, --e0-r2 salida_tanda0_r2b)
comparada byte a byte con el kg sellado y, para el reporte, con los dos campos nuevos (`con_cola`,
`cola_descartada_por_to`) quitados y la ruta normalizada. Lo demás es el control de T3 (E0 legada, los tres r1, los dos
r2a contra los sha del cierre de C2, suite y shapes r2a).

Uso: <python> control_repro_sc1bis.py <fuente (copia del repo con el código nuevo)> <dir de trabajo> --python <python del repo> [--out <json>]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("repo", type=Path)
ap.add_argument("trabajo", type=Path)
ap.add_argument("--python", required=True)
ap.add_argument("--out", type=Path, default=None)
A = ap.parse_args()
REPO = A.repo.resolve()
TRAB = A.trabajo.resolve()
assert REPO not in TRAB.parents and TRAB != REPO, "el directorio de trabajo no puede estar dentro de la fuente"
PY = A.python
COPIA = TRAB / "copia"
OUT = TRAB / "salidas"
ENV = {"PYTHONDONTWRITEBYTECODE": "1", "PATH": "/usr/bin:/bin"}
REX = "data/experiment/reextraccion_v2"
MAN = f"{REX}/manifiestos"
SUITE = ["scripts/regression_kg.py", "--perfil", "r2", "--generacion", "3", "--catalogo",
         "data/experiment/catalogo_unico/generados_r2/catalogo_suite_r2.json", "--politica-cuarentena", "flaggeada",
         "--esperado", "scripts/regression_kg_esperado.json"]
res: dict = {}
SHA_C2 = {"diez": "70d51e429b0e2cc1aafa697e32bc83462d371dfdd5edafb34e92fe4f7be45bdd",
          "desarrollo": "fa4c1043d859081e49dce6cb940a9f5d4c09fc6d449efb85355f95312257178a"}
SHA_R2B = {"diez": "a9631a64b422bdae634fb05135373c6f04c6272cdf7acd43a1be9f5b6c1f5f57",
           "desarrollo": "6e7560433148cfe0c476cdd61199c32278187c4196d6f90dc0a38976a6d8e9a2"}
CAMPOS_NUEVOS = ("con_cola", "cola_descartada_por_to")


def sha_fuente() -> dict:
    out = {}
    for r, ds, fs in os.walk(REPO):
        ds[:] = [d for d in ds if d not in ("__pycache__",)]
        for f in fs:
            p = Path(r) / f
            if p.is_file():
                out[str(p.relative_to(REPO))] = hashlib.sha256(p.read_bytes()).hexdigest()
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


def reporte_sin_campos_nuevos(p: Path, quitar_rutas: tuple) -> str:
    d = json.loads(p.read_text(encoding="utf-8"))
    for k in CAMPOS_NUEVOS:
        d.pop(k, None)
    t = json.dumps(d, ensure_ascii=False, indent=1, sort_keys=True)
    for viejo, nuevo in quitar_rutas:
        t = t.replace(viejo, nuevo)
    return t


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    antes = sha_fuente()
    res["fuente_archivos"] = len(antes)
    if COPIA.exists():
        subprocess.run(["rm", "-rf", str(COPIA)], check=True)
    subprocess.run(["rsync", "-a", "--no-links", "--exclude", ".git", "--exclude", ".venv", "--exclude", ".env",
                    "--exclude", "data/raw", "--exclude", "__pycache__", "--exclude", "*.pyc", f"{REPO}/", f"{COPIA}/"],
                   check=True)
    enlaces = sum(1 for _r, ds, fs in os.walk(COPIA) for x in ds + fs if os.path.islink(os.path.join(_r, x)))
    res["copia_enlaces"] = enlaces
    assert enlaces == 0
    # a. E0 legada
    sal = OUT / "e0_legada"
    rc = correr([f"{REX}/e0_chunking/correr_e0.py", "--manifiesto", f"{MAN}/tanda0_10tos.json", "--salida", str(sal)],
                "e0_legada")
    res["e0_legada"] = {"rc": rc, **comparar_dir(REPO / REX / "e0_chunking" / "salida_tanda0", sal)}
    entrada = str(COPIA / REX / "corpus_tanda0" / "salida_dirigida")
    # b. ensamblados sellados r1, con --entrada de ruta absoluta
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
    # f. (nuevo) los dos r2b sin la bandera, con el código nuevo: kg byte a byte el sellado; reporte igual salvo los
    #    campos nuevos y la ruta
    entrada_r2b = f"{REX}/corpus_tanda0/salida_r2b"
    for x in ("diez", "desarrollo"):
        sal = OUT / f"ens_{x}_r2b_sin_bandera"
        rc = correr(["data/experiment/tanda0/code/ensamblar_tanda0.py", "--manifiesto", f"{MAN}/tanda0_ens_{x}_r2b.json",
                     "--entrada", entrada_r2b, "--e0-r2", f"{REX}/e0_chunking/salida_tanda0_r2b",
                     "--salida", str(sal)], f"ens_{x}_r2b_sin_bandera")
        kg = sal / "r2" / "kg.json"
        sellado_dir = REPO / REX / "corpus_tanda0" / f"ens_{x}_r2b"
        rep_nuevo = json.loads((sal / "r2" / "reporte_ensamblado_r2.json").read_text(encoding="utf-8"))
        norm = ((str(sal), "<SALIDA>"), (f"{REX}/corpus_tanda0/ens_{x}_r2b", "<SALIDA>"), (str(COPIA) + "/", ""),
                (str(REPO) + "/", ""))
        res[f"ens_{x}_r2b_sin_bandera"] = {
            "rc": rc, "sha256_kg": sha(kg) if kg.exists() else None, "sha256_sellado": SHA_R2B[x],
            "kg_byte_a_byte_igual_al_sellado": kg.exists() and kg.read_bytes() == (sellado_dir / "r2" / "kg.json").read_bytes(),
            "reporte_con_cola_declarado": rep_nuevo.get("con_cola"),
            "reporte_cola_descartada_por_to": rep_nuevo.get("cola_descartada_por_to"),
            "reporte_igual_al_sellado_sin_los_campos_nuevos_y_con_ruta_normalizada":
                reporte_sin_campos_nuevos(sal / "r2" / "reporte_ensamblado_r2.json", norm)
                == reporte_sin_campos_nuevos(sellado_dir / "r2" / "reporte_ensamblado_r2.json", norm),
            "directorio_r2": comparar_dir(sellado_dir / "r2", sal / "r2", norm)}
    despues = sha_fuente()
    res["fuente_igual_antes_y_despues"] = antes == despues
    res["fuente_archivos_que_cambiaron"] = sorted(k for k in set(antes) | set(despues) if antes.get(k) != despues.get(k))
    texto = json.dumps(res, ensure_ascii=False, indent=1).replace(str(TRAB), "<TRABAJO>").replace(str(REPO), "<FUENTE>")
    (OUT / "control_repro.json").write_text(texto + "\n", encoding="utf-8")
    if A.out is not None:
        A.out.write_text(texto + "\n", encoding="utf-8")
    print(json.dumps({k: (v if not isinstance(v, dict) else {kk: vv for kk, vv in v.items()
                                                             if kk in ("rc", "iguales", "distintos", "total_repo",
                                                                       "sha256_kg", "igual_al_cierre_c2",
                                                                       "kg_byte_a_byte_igual_al_sellado",
                                                                       "reporte_igual_al_sellado_sin_los_campos_nuevos_y_con_ruta_normalizada")})
                      for k, v in res.items()}, ensure_ascii=False))


if __name__ == "__main__":
    main()
