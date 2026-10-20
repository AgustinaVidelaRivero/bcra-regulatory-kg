"""B6.1, tanda final, T3: pasa al repo, archivo por archivo, los bytes que T3 produjo en la copia y en el scratchpad, con el modelo de
data/experiment/tanda1/t3/scripts/escribir_en_el_repo_t3f.py. Ningún generador corre sobre el repo. Dos pasos:

  armar <plan.json> <scratchpad> <staging>
      arma en <staging> el árbol de lo que se escribe, con rutas relativas al repo. <plan.json> es una lista de
      {"origen": <archivo o carpeta>, "destino": <ruta relativa al repo>, "modo": "tal_cual" | "saneado"}; una carpeta va entera, con
      sus rutas relativas. «saneado» reemplaza en los archivos de texto el scratchpad por <SCRATCHPAD> y la carpeta personal por $HOME
      (los binarios van tal cual), y frena si queda una ruta absoluta del scratchpad o de la carpeta personal. «tal_cual» copia los
      bytes: los ensamblados (su reporte guarda las rutas de la copia donde corrió, como los sellados de la tanda 1), los archivos que
      generó un script dentro de la copia con rutas relativas y los NO_ABRIR_, que no se abren. Frena si dos orígenes van al mismo
      destino.
  escribir <staging> <repo> <salida.json> [--seco] [--cambian <ruta> ...]
      antes: cada ruta nueva no existe en el repo y cada archivo que cambia (los de --cambian) es, byte a byte, el de HEAD (git show);
      después: cada archivo del repo es byte a byte el del staging. Frena sin escribir nada si falla un control previo.
  apartar <escritura previa.json> <repo> <destino> <salida.json> <ruta relativa al repo> [...]
      mueve fuera del repo, a <destino> (en el scratchpad), archivos que escribió una etapa anterior de esta unidad y que se reemplazan:
      una carpeta va entera. Antes: cada archivo está en <escritura previa.json> con el mismo sha256 (sigue siendo el que se escribió),
      no está en HEAD (git ls-files) y su destino no existe. Frena sin mover nada si falla un control. No borra nada.
"""
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def armar(PLAN: Path, SCR: Path, ST: Path) -> None:
    if ST.exists():
        raise SystemExit(f"FRENO: {ST} ya existe")
    scratch, home = str(SCR).encode(), str(Path.home()).encode()
    lista = {"tal_cual": [], "saneado": []}
    for e in json.loads(PLAN.read_text(encoding="utf-8")):
        o, dest, modo = Path(e["origen"]), e["destino"], e["modo"]
        assert modo in lista, modo
        pares = [(o, dest)] if o.is_file() else [(p, f"{dest}/{p.relative_to(o).as_posix()}") for p in sorted(o.rglob("*")) if p.is_file()]
        if not pares:
            raise SystemExit(f"FRENO: {o} no existe o está vacío")
        for p, rel in pares:
            d = ST / rel
            if d.exists():
                raise SystemExit(f"FRENO: dos orígenes para {rel}")
            d.parent.mkdir(parents=True, exist_ok=True)
            b = p.read_bytes()
            if modo == "saneado" and not p.name.startswith("NO_ABRIR_"):
                try:
                    b.decode("utf-8")
                    b = b.replace(scratch, b"<SCRATCHPAD>").replace(home, b"$HOME")
                    if b"/private/tmp" in b or b"/Users/" in b:
                        raise SystemExit(f"FRENO: queda una ruta absoluta en {p}")
                except UnicodeDecodeError:
                    pass
            d.write_bytes(b)
            lista[modo].append(rel)
    (ST.parent / f"lista_{ST.name}.json").write_text(json.dumps(lista, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"staging {ST.name}: {len(lista['tal_cual'])} tal cual, {len(lista['saneado'])} saneados")


def head(R: Path, rel: str) -> bytes:
    return subprocess.run(["git", "-C", str(R), "show", f"HEAD:{rel}"], capture_output=True, check=True).stdout


def escribir(ST: Path, R: Path, SAL: Path, seco: bool, cambian: list) -> int:
    archivos = sorted(p.relative_to(ST).as_posix() for p in ST.rglob("*") if p.is_file())
    assert all(c in archivos for c in cambian), "un archivo de --cambian no está en el staging"
    nuevos = [r for r in archivos if r not in cambian]
    res = {"nuevos": len(nuevos), "cambian": len(cambian), "previos": {}, "escritos": {}, "seco": seco}
    fallas = [f"ya existe {r}" for r in nuevos if (R / r).exists()]
    for rel in cambian:
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
    print(("SECO: " if seco else "") + f"nuevos {len(nuevos)}, cambian {len(cambian)}; controles previos OK"
          + ("" if seco else f"; escritos iguales al staging: {sum(v['igual_al_staging'] for v in res['escritos'].values())} de "
             f"{len(res['escritos'])}"))
    return 0 if res["ok"] else 1


def apartar(PREV: Path, R: Path, DEST: Path, SAL: Path, rels: list) -> int:
    prev = json.loads(PREV.read_text(encoding="utf-8"))["escritos"]
    archivos = []
    for rel in rels:
        p = R / rel
        archivos += sorted(x.relative_to(R).as_posix() for x in p.rglob("*") if x.is_file()) if p.is_dir() else [rel]
    en_head = set(subprocess.run(["git", "-C", str(R), "ls-files", "--", *rels], capture_output=True, text=True, check=True).stdout.split())
    fallas = []
    for rel in archivos:
        if rel not in prev:
            fallas.append(f"{rel} no está en la escritura previa")
        elif sha((R / rel).read_bytes()) != prev[rel]["sha256"]:
            fallas.append(f"{rel} cambió desde que se escribió")
        if rel in en_head:
            fallas.append(f"{rel} está en HEAD")
        if (DEST / rel).exists():
            fallas.append(f"ya existe {DEST / rel}")
    res = {"archivos": len(archivos), "fallas": fallas, "movidos": {}}
    if not fallas:
        for rel in archivos:
            d = DEST / rel
            d.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(R / rel), str(d))
            res["movidos"][rel] = sha(d.read_bytes())
        for rel in rels:                                  # las carpetas que quedaron vacías
            p = R / rel
            for q in sorted((x for x in p.rglob("*") if x.is_dir()), key=lambda x: -len(x.parts)) if p.is_dir() else []:
                q.rmdir()
            if p.is_dir():
                p.rmdir()
    res["ok"] = not fallas and all(res["movidos"][r] == prev[r]["sha256"] for r in res["movidos"])
    SAL.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"apartados {len(res['movidos'])} de {len(archivos)}" + (f"; FRENA: {fallas[:5]}" if fallas else ""))
    return 0 if res["ok"] else 1


if __name__ == "__main__":
    if sys.argv[1] == "apartar":
        a = sys.argv[2:]
        sys.exit(apartar(Path(a[0]), Path(a[1]).resolve(), Path(a[2]).resolve(), Path(a[3]), a[4:]))
    if sys.argv[1] == "armar":
        armar(Path(sys.argv[2]).resolve(), Path(sys.argv[3]).resolve(), Path(sys.argv[4]).resolve())
    else:
        a = sys.argv[2:]
        cambian = [x for x in a[a.index("--cambian") + 1:] if x != "--seco"] if "--cambian" in a else []
        sys.exit(escribir(Path(a[0]).resolve(), Path(a[1]).resolve(), Path(a[2]), "--seco" in a, cambian))
