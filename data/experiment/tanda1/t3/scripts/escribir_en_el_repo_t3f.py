"""B6.1, tanda 1, T3 (desde el punto 4): pasa al repo, archivo por archivo, los bytes que esta parte produjo en la copia y en el scratchpad,
con el modelo de escribir_en_el_repo_t3.py. Ningún generador corre sobre el repo. Dos pasos:

  armar <copia> <trabajo t3f> <staging>
      arma en <staging> el árbol de lo que se escribe, con rutas relativas al repo:
        - tal cual, desde la copia: data/experiment/neo4j/grafos.py (solo dos entradas nuevas) y
          data/experiment/tanda1/t3/registro_vista_r2b_tanda1.py, que generó editar_grafos_t3f.py; y lo que ya está saneado en la copia:
          tanda1/t3/gate_decisiones/, tanda1/t3/conteos_sin_leer/ y tanda1/t3/NO_ABRIR_conteos_t3.json (se copia sin abrirlo);
        - con las rutas reemplazadas (el scratchpad por <SCRATCHPAD> y la carpeta personal por $HOME): las salidas del cargador y del
          control de la cola (la copia, tanda1/t3/neo4j/), sus consolas, la corrida en seco del registro y el sha256 del cargador
          antes y después (tanda1/t3/neo4j/); y la preparación de T4 (tanda1/t3/muestras/): las poblaciones, los umbrales y su
          control, los sorteos de la primera corrida (cada muestra en muestras/<muestra>.json y el índice sorteos_t4.json), la
          segunda corrida (muestras/segunda_corrida_de_los_sorteos/), el material y unidades_a_la_vista_T4.json.
  escribir <staging> <repo> <salida.json> [--seco]
      antes: cada ruta nueva no existe en el repo y cada archivo que cambia (grafos.py) es, byte a byte, el de HEAD (git show); después:
      cada archivo del repo es byte a byte el del staging. Frena sin escribir nada si falla un control previo.
"""
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

T3 = "data/experiment/tanda1/t3"
CAMBIAN = ["data/experiment/neo4j/grafos.py"]


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def armar(C: Path, W: Path, ST: Path) -> None:
    if ST.exists():
        raise SystemExit(f"FRENO: {ST} ya existe")
    scratch = str(W.parent).encode()
    home = str(Path.home()).encode()

    def limpio(b: bytes) -> bytes:
        return b.replace(scratch, b"<SCRATCHPAD>").replace(home, b"$HOME")

    lista = {"tal_cual": [], "con_rutas_reemplazadas": []}

    def poner(rel: str, b: bytes, tal_cual: bool) -> None:
        d = ST / rel
        if d.exists():
            raise SystemExit(f"FRENO: dos orígenes para {rel}")
        d.parent.mkdir(parents=True, exist_ok=True)
        d.write_bytes(b if tal_cual else limpio(b))
        lista["tal_cual" if tal_cual else "con_rutas_reemplazadas"].append(rel)

    for rel in CAMBIAN + [f"{T3}/registro_vista_r2b_tanda1.py", f"{T3}/NO_ABRIR_conteos_t3.json"]:
        poner(rel, (C / rel).read_bytes(), True)
    for sub in ("gate_decisiones", "conteos_sin_leer"):
        for p in sorted(x for x in (C / T3 / sub).rglob("*") if x.is_file()):
            poner(p.relative_to(C).as_posix(), p.read_bytes(), True)
    for p in sorted(x for x in (C / T3 / "neo4j").rglob("*") if x.is_file()):
        poner(p.relative_to(C).as_posix(), p.read_bytes(), False)
    for p in sorted((W / "neo4j_consolas").glob("*.txt")):
        poner(f"{T3}/neo4j/consolas/{p.name}", p.read_bytes(), False)
    for n in ("sha_cargador_antes.txt", "sha_cargador_despues.txt", "dry_registro_t3f.json", "consola_dry_registro_t3f.txt",
              "consola_editar_grafos_t3f.txt"):
        poner(f"{T3}/neo4j/{n}", (W / n).read_bytes(), False)
    t4 = W / "t4"
    for n in ("poblaciones_t4.json", "consola_poblaciones_t4.txt", "umbrales_t4_reales.json", "consola_umbrales_t4.txt",
              "base_semillas_3b61f154.txt", "consola_sorteos_corrida1.txt", "consola_sorteos_corrida2.txt", "consola_material_t4.txt",
              "control_material_t4.txt", "unidades_a_la_vista_T4.json", "consola_unidades_a_la_vista.txt"):
        poner(f"{T3}/muestras/{n}", (t4 / n).read_bytes(), False)
    for p in sorted((t4 / "umbrales_trabajo").iterdir()):
        poner(f"{T3}/muestras/umbrales_control/{p.name}", p.read_bytes(), False)
    for p in sorted((t4 / "sorteos_corrida1").iterdir()):
        poner(f"{T3}/muestras/{p.name}", p.read_bytes(), False)
    for p in sorted((t4 / "sorteos_corrida2").iterdir()):
        poner(f"{T3}/muestras/segunda_corrida_de_los_sorteos/{p.name}", p.read_bytes(), False)
    for p in sorted(x for x in (t4 / "material").rglob("*") if x.is_file()):
        poner(f"{T3}/muestras/material/{p.relative_to(t4 / 'material').as_posix()}", p.read_bytes(), False)
    for rel in lista["tal_cual"] + lista["con_rutas_reemplazadas"]:
        if Path(rel).name.startswith("NO_ABRIR_"):
            continue
        b = (ST / rel).read_bytes()
        assert b"/private/tmp" not in b and b"/Users/" not in b, rel
    (ST.parent / "lista_staging_t3f.json").write_text(json.dumps(lista, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
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
