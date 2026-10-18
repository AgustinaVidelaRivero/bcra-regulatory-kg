"""B6.1, tanda 1, T3: pasa al repo, archivo por archivo, los bytes que la etapa produjo en la copia y en el scratchpad, con el modelo
de data/experiment/resellado_t0/scripts/escribir_en_el_repo_rs1.py. Ningún generador corre sobre el repo. Dos pasos:

  armar <copia> <trabajo> <staging>
      arma en <staging> el árbol de lo que se escribe, con rutas relativas al repo:
        - tal cual, las salidas de los generadores en las carpetas de los ensamblados (como las selladas de la tanda 0, que guardan las
          rutas absolutas de donde corrieron): corpus_tanda1/ens_veinte_r2b{,_sincola}/ y tanda1/t3/acumulado/ens_treinta_r2b{,_sincola}/,
          sin las consolas de gate_t3.sh; los manifiestos, la E0 combinada y armado_acumulado_t3.json del acumulado; y la fixture;
        - con las rutas reemplazadas (el scratchpad por <SCRATCHPAD> y la carpeta personal por $HOME), todo lo demás que va a
          data/experiment/tanda1/t3/: las consolas de las cadenas y del gate, las salidas de los controles, las shapes con la E0 con las
          partes, las intrínsecas, los selftests y la lista de lo borrado por nombre del clon de git.
      No se escriben: la entrada combinada del acumulado (entrada_acumulado_r2b/, 557 archivos copiados de las salidas selladas; se
      rearma con armar_acumulado_t3.py y su sha256 por archivo está en armado_acumulado_t3.json), las segundas corridas y las de
      reproducibilidad (sus sha256 están en salidas/cadenas_sha256_t3.tsv) y las E0 con las partes (se rearman con
      reext_t0/t3/e0_con_partes.py).
  escribir <staging> <repo> <salida.json> [--seco]
      antes: cada ruta nueva no existe en el repo y cada archivo que cambia es, byte a byte, el de HEAD (git show); después: cada
      archivo del repo es byte a byte el del staging. Frena sin escribir nada si falla un control previo.
"""
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

X = "data/experiment/reextraccion_v2"
T3 = "data/experiment/tanda1/t3"
A = f"{T3}/acumulado"
ENSAMBLADOS = [f"{X}/corpus_tanda1/ens_veinte_r2b", f"{X}/corpus_tanda1/ens_veinte_r2b_sincola", f"{A}/ens_treinta_r2b",
               f"{A}/ens_treinta_r2b_sincola"]
CAMBIAN = ["scripts/regression_kg_esperado.json"]


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def armar(C: Path, W: Path, ST: Path) -> None:
    if ST.exists():
        raise SystemExit(f"FRENO: {ST} ya existe")
    scratch = str(W.parent).encode()                      # <scratchpad>/t3 → su padre es el scratchpad

    def limpio(b: bytes) -> bytes:
        return b.replace(scratch, b"<SCRATCHPAD>").replace(str(Path.home()).encode(), b"$HOME")

    def poner(rel: str, b: bytes) -> None:
        d = ST / rel
        d.parent.mkdir(parents=True, exist_ok=True)
        d.write_bytes(b)
    lista = {"tal_cual": [], "con_rutas_reemplazadas": []}
    for e in ENSAMBLADOS:
        for p in sorted(x for x in (C / e).rglob("*") if x.is_file()):
            rel = p.relative_to(C).as_posix()
            if p.parent == C / e and p.name.startswith("consola_"):
                poner(f"{T3}/gate/consolas/{Path(e).name}/{p.name}", limpio(p.read_bytes()))
                lista["con_rutas_reemplazadas"].append(f"{T3}/gate/consolas/{Path(e).name}/{p.name}")
                continue
            poner(rel, p.read_bytes()); lista["tal_cual"].append(rel)
    for sub in ("manifiestos", "e0_acumulado_r2b"):
        for p in sorted((C / A / sub).iterdir()):
            rel = p.relative_to(C).as_posix(); poner(rel, p.read_bytes()); lista["tal_cual"].append(rel)
    for rel in [f"{A}/armado_acumulado_t3.json"] + CAMBIAN:
        poner(rel, (C / rel).read_bytes()); lista["tal_cual"].append(rel)
    origenes = [("salidas", "salidas"), ("intrinsecas_gen3", "intrinsecas_gen3"), ("selftests", "selftests"),
                ("gate_informativo_con_partes", "gate/shapes_con_e0_con_partes")]
    for o, d in origenes:
        for p in sorted(x for x in (W / o).rglob("*") if x.is_file()):
            rel = f"{T3}/{d}/{p.relative_to(W / o).as_posix()}"; poner(rel, limpio(p.read_bytes()))
            lista["con_rutas_reemplazadas"].append(rel)
    for p in [W / "corridas/lote_t3.txt", W / "corridas/lote_t3_rc.json", W / "corridas/lote_t3.log"] + sorted(
            (W / "corridas").glob("*/consola_*.txt")):
        rel = f"{T3}/corridas/{p.relative_to(W / 'corridas').as_posix()}"; poner(rel, limpio(p.read_bytes()))
        lista["con_rutas_reemplazadas"].append(rel)
    for n, d in (("consola_e0_con_partes_t1.txt", "e0_con_partes"), ("consola_e0_con_partes_acumulado.txt", "e0_con_partes"),
                 ("clon_git_borrados_por_nombre.txt", ".")):
        rel = f"{T3}/{d}/{n}" if d != "." else f"{T3}/{n}"; poner(rel, limpio((W / n).read_bytes()))
        lista["con_rutas_reemplazadas"].append(rel)
    for rel in lista["con_rutas_reemplazadas"]:
        assert b"/private/tmp" not in (ST / rel).read_bytes() and b"/Users/" not in (ST / rel).read_bytes(), rel
    (ST.parent / "lista_staging_t3.json").write_text(json.dumps(lista, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"staging: {len(lista['tal_cual'])} tal cual, {len(lista['con_rutas_reemplazadas'])} con las rutas reemplazadas")


def head(R: Path, rel: str) -> bytes:
    return subprocess.run(["git", "-C", str(R), "show", f"HEAD:{rel}"], capture_output=True, check=True).stdout


def escribir(ST: Path, R: Path, SAL: Path, seco: bool) -> int:
    archivos = sorted(p.relative_to(ST).as_posix() for p in ST.rglob("*") if p.is_file())
    nuevos = [r for r in archivos if r not in CAMBIAN]
    res = {"nuevos": len(nuevos), "cambian": len(CAMBIAN), "previos": {}, "escritos": {}, "seco": seco}
    fallas = [f"ya existe {r}" for r in nuevos if (R / r).exists()]
    for rel in CAMBIAN:
        actual, h = (R / rel).read_bytes(), head(R, rel)
        if actual != h:
            fallas.append(f"{rel} no es el de HEAD")
        res["previos"][rel] = {"repo_igual_a_HEAD": actual == h, "sha256_HEAD": sha(h), "sha256_nuevo": sha((ST / rel).read_bytes())}
    res["fallas_previas"] = fallas
    if fallas:
        SAL.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print("FRENA sin escribir:", fallas[:10])
        return 1
    if not seco:
        for rel in archivos:
            d = R / rel
            d.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ST / rel, d)
        for rel in archivos:
            a, b = (R / rel).read_bytes(), (ST / rel).read_bytes()
            res["escritos"][rel] = {"sha256": sha(a), "igual_al_staging": a == b}
    res["ok"] = seco or all(v["igual_al_staging"] for v in res["escritos"].values())
    SAL.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(("SECO: " if seco else "") + f"nuevos {len(nuevos)}, cambian {len(CAMBIAN)}; controles previos OK"
          + ("" if seco else f"; escritos iguales al staging: {sum(v['igual_al_staging'] for v in res['escritos'].values())} de "
             f"{len(res['escritos'])}"))
    return 0 if res["ok"] else 1


if __name__ == "__main__":
    if sys.argv[1] == "armar":
        armar(Path(sys.argv[2]).resolve(), Path(sys.argv[3]).resolve(), Path(sys.argv[4]).resolve())
    else:
        sys.exit(escribir(Path(sys.argv[2]).resolve(), Path(sys.argv[3]).resolve(), Path(sys.argv[4]), "--seco" in sys.argv))
