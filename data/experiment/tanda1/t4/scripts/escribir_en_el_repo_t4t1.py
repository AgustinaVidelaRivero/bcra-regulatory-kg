"""B6.1, tanda 1, T4, primer tramo: pasa al repo, archivo por archivo, los bytes que este tramo produjo en el scratchpad, con el modelo de
tanda1/t3/scripts/escribir_en_el_repo_t3f.py. Ningún generador corre sobre el repo. Dos pasos:

  armar <copia> <trabajo t4t1> <staging> <repo>
      arma en <staging> el árbol de lo que se escribe, con rutas relativas al repo, con el scratchpad escrito <SCRATCHPAD> y la carpeta
      personal $HOME (control: ningún archivo queda con «/private/tmp» ni «/Users/», salvo el NO_ABRIR_, que se copia sin abrirlo):
        - tanda1/t4/muestras/: las poblaciones, los tres sorteos de la primera corrida y su índice, la segunda corrida
          (segunda_corrida_de_los_sorteos/), el material, la versión de T3 de unidades_a_la_vista_T4.json (del T3a, git show eb0711a1,
          como unidades_a_la_vista_T4_regla_de_T3.json) y las consolas (consolas/);
        - tanda1/t4/lectura_asistida/: el JSON y el .md de la lectura, las propuestas de entrada (propuestas/) y las consolas;
        - tanda1/t4/lectura_autora/: las ocho planillas, el LEEME y el convertidor;
        - tanda1/t4/NO_ABRIR_conteos_t4.json;
        - tanda1/t3/muestras/unidades_a_la_vista_T4.json, reescrito (el único archivo de t3/ que cambia).
      Del repo solo lee, con git show, la versión del T3a.
  escribir <staging> <repo> <salida.json> [--seco]
      antes: cada ruta nueva no existe en el repo y el archivo que cambia es, byte a byte, el de HEAD (git show); después: cada archivo del
      repo es byte a byte el del staging. Frena sin escribir nada si falla un control previo.
"""
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
T3 = "data/experiment/tanda1/t3"
T4 = "data/experiment/tanda1/t4"
VISTA = f"{T3}/muestras/unidades_a_la_vista_T4.json"
VISTA_T3_SHA = "1e775850e94457c4d5e356c27bd247dbb8ba76731f302580ab7b2762306bfc12"
CAMBIAN = [VISTA]
MUESTRAS_T4 = ["vigilancia_1", "vigilancia_3", "observacion_12"]


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def armar(C: Path, W: Path, ST: Path, R: Path) -> None:
    if ST.exists():
        raise SystemExit(f"FRENO: {ST} ya existe")
    scratch = str(W.parent).encode()
    home = str(Path.home()).encode()

    def limpio(b: bytes) -> bytes:
        return b.replace(scratch, b"<SCRATCHPAD>").replace(home, b"$HOME")

    lista = {"tal_cual": [], "con_rutas_reemplazadas": []}

    def poner(rel: str, b: bytes, tal_cual: bool = False) -> None:
        d = ST / rel
        if d.exists():
            raise SystemExit(f"FRENO: dos orígenes para {rel}")
        d.parent.mkdir(parents=True, exist_ok=True)
        d.write_bytes(b if tal_cual else limpio(b))
        lista["tal_cual" if tal_cual else "con_rutas_reemplazadas"].append(rel)

    t4, a4 = W / "t4", W / "arbol_t4"
    poner(f"{T4}/NO_ABRIR_conteos_t4.json", (t4 / "NO_ABRIR_conteos_t4.json").read_bytes(), True)
    poner(f"{T4}/muestras/poblaciones_t4_tramo1.json", (t4 / "poblaciones_t4_tramo1.json").read_bytes())
    for p in sorted((t4 / "sorteos_corrida1").iterdir()):
        poner(f"{T4}/muestras/{p.name}", p.read_bytes())
    for p in sorted((t4 / "sorteos_corrida2").iterdir()):
        poner(f"{T4}/muestras/segunda_corrida_de_los_sorteos/{p.name}", p.read_bytes())
    for p in sorted(x for x in (t4 / "material").rglob("*") if x.is_file()):
        poner(f"{T4}/muestras/material/{p.relative_to(t4 / 'material').as_posix()}", p.read_bytes())
    for n in ("consola_poblaciones_t4_tramo1.txt", "consola_sorteos_t4t1_corrida1.txt", "consola_sorteos_t4t1_corrida2.txt",
              "consola_material_t4t1.txt", "consola_unidades_a_la_vista_t4t1.txt", "consola_no_abrir_t4t1.txt"):
        poner(f"{T4}/muestras/consolas/{n}", (t4 / n).read_bytes())
    poner(f"{T4}/muestras/consolas/consola_e0_con_partes_t4t1.txt", (W / "consola_e0_con_partes_t4t1.txt").read_bytes())
    # la versión de T3 de unidades_a_la_vista_T4.json, desde el T3a, antes de reescribirla
    t3a = subprocess.run(["git", "-C", str(R), "show", f"eb0711a1:{VISTA}"], capture_output=True, check=True).stdout
    assert sha(t3a) == VISTA_T3_SHA and (C / VISTA).read_bytes() == t3a, "la versión de T3 no es la del T3a"
    poner(f"{T4}/muestras/unidades_a_la_vista_T4_regla_de_T3.json", t3a, True)
    poner(VISTA, (t4 / "unidades_a_la_vista_T4.json").read_bytes())
    for p in sorted((a4 / "lectura_asistida").iterdir()):
        poner(f"{T4}/lectura_asistida/{p.name}", p.read_bytes())
    for p in sorted((W / "lectura").glob("*.json")):
        poner(f"{T4}/lectura_asistida/propuestas/{p.name}", p.read_bytes())
    for n in ("consola_planillas_t4t1.txt", "prueba_convertidor_t4t1.txt"):
        poner(f"{T4}/lectura_asistida/consolas/{n}", (t4 / n).read_bytes())
    for p in sorted((a4 / "lectura_autora").iterdir()):
        poner(f"{T4}/lectura_autora/{p.name}", p.read_bytes())
    for rel in lista["tal_cual"] + lista["con_rutas_reemplazadas"]:
        if Path(rel).name.startswith("NO_ABRIR_"):
            continue
        b = (ST / rel).read_bytes()
        assert b"/private/tmp" not in b and b"/Users/" not in b, rel
    (ST.parent / "lista_staging_t4t1.json").write_text(json.dumps(lista, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
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
        armar(*(Path(x).resolve() for x in sys.argv[2:6]))
    else:
        sys.exit(escribir(Path(sys.argv[2]).resolve(), Path(sys.argv[3]).resolve(), Path(sys.argv[4]), "--seco" in sys.argv))
