#!/usr/bin/env python3
"""enmascarar_cwd_a2_2.py — Las transcripciones (`sesion_*.jsonl`) y los streams (`stream_*.jsonl`) de las sesiones pagas de A2.2
son salida literal del CLI y traen el `cwd` absoluto de la sesión, bajo la carpeta personal. En el repo van enmascarados como los
del tramo 2 de A2.1 (pre-registro, §7, A-D4, (a)): la carpeta personal reemplazada por `$HOME`, sin ningún otro cambio de bytes.
Los originales quedan fuera del repo, en `$HOME/INGENIERIA IA/TESIS/fuera_del_repo/banco_mcp_originales_A2_2/`, con las rutas del
repo, y el JSON lleva el sha256 de cada original y de su versión enmascarada.

Es `a2_1/enmascarar_cwd_a2_1.py` adaptado a las carpetas de A2.2 (las tres de a2_2/resultados/) y a su carpeta de originales. Lo
que agrega: --aplicar copia antes cada original a la carpeta de originales y controla su sha256 en la copia; si ya hay ahí un
archivo distinto, frena sin escribir nada. --originales cambia esa carpeta, solo para las pruebas sobre copias sintéticas.

La carpeta personal no se escribe en ningún archivo: sale de los datos, como el prefijo del `cwd` del evento `system/init` de cada
stream, antes de `/INGENIERIA IA/TESIS/fuera_del_repo/banco_sesiones/cwd`. Tiene que ser la misma en todos los streams, y cada vez
que aparece en un archivo tiene que ir seguida de `/`. Después del reemplazo, cada línea sigue siendo un JSON válido y el nombre
de la carpeta personal no aparece más.

Modos (USD 0; solo la biblioteca estándar):
  --calcular <raíz> <salida.json>  arma el JSON desde los originales; no toca los archivos.
  --probar <raíz> <json>           controla el sha256 de cada original y calcula en memoria su versión enmascarada, que tiene que dar el
                                   sha256 del JSON; no escribe nada.
  --aplicar <raíz> <json>          los mismos controles, para todos antes de escribir el primero; copia cada original a la carpeta de
                                   originales (y controla su sha256 ahí) y después escribe cada versión enmascarada (por un archivo
                                   temporal y un reemplazo) y controla su sha256 en el disco.
<raíz> es la carpeta que tiene `data/experiment/banco_mcp/`.
"""
import hashlib
import json
import os
import sys
from pathlib import Path

SUFIJO = "/INGENIERIA IA/TESIS/fuera_del_repo/banco_sesiones/cwd"
CARPETAS = ("data/experiment/banco_mcp/a2_2/resultados/pruebas", "data/experiment/banco_mcp/a2_2/resultados/n1",
            "data/experiment/banco_mcp/a2_2/resultados/recorridas")
ORIGINALES = "$HOME/INGENIERIA IA/TESIS/fuera_del_repo/banco_mcp_originales_A2_2/"
ORIGINALES_DIR = Path.home() / "INGENIERIA IA" / "TESIS" / "fuera_del_repo" / "banco_mcp_originales_A2_2"
sha = lambda b: hashlib.sha256(b).hexdigest()  # noqa: E731


def frena(m):
    raise SystemExit(f"FRENO: {m}")


def rutas(raiz):
    out = []
    for c in CARPETAS:
        if not (raiz / c).is_dir():
            continue
        for pre in ("sesion_", "stream_"):
            out += sorted(p.relative_to(raiz).as_posix() for p in (raiz / c).glob(f"{pre}*.jsonl"))
    return sorted(out)


def carpeta_personal(raiz):
    vistas = set()
    streams = [r for r in rutas(raiz) if Path(r).name.startswith("stream_")]
    if not streams:
        frena("no hay streams en las carpetas de A2.2")
    for r in streams:
        e = json.loads((raiz / r).read_text(encoding="utf-8").splitlines()[0])
        if e.get("type") != "system" or e.get("subtype") != "init" or not str(e.get("cwd", "")).endswith(SUFIJO):
            frena(f"{r}: la primera línea no es el init con el cwd esperado")
        vistas.add(e["cwd"][: -len(SUFIJO)])
    if len(vistas) != 1:
        frena(f"la carpeta personal no es la misma en los {len(streams)} streams ({len(vistas)} distintas)")
    if not next(iter(vistas)).startswith("/"):
        frena("el cwd de los streams no empieza con una ruta absoluta: ¿ya están enmascarados?")
    return next(iter(vistas))


def enmascarar(b, cp):
    a = cp.encode("utf-8")
    n = b.count(a)
    if n != b.count(a + b"/"):
        frena("la carpeta personal aparece sin una barra después")
    m = b.replace(a, b"$HOME")
    if os.path.basename(cp).encode("utf-8") in m:
        frena("el nombre de la carpeta personal sigue en la versión enmascarada")
    for i, l in enumerate(m.split(b"\n")):
        if l.strip():
            try:
                json.loads(l)
            except ValueError:
                frena(f"la línea {i + 1} no es un JSON válido después del reemplazo")
    return m, n


def calcular(raiz, salida):
    cp = carpeta_personal(raiz)
    filas = []
    for r in rutas(raiz):
        b = (raiz / r).read_bytes()
        m, n = enmascarar(b, cp)
        filas.append({"ruta": r, "sha256_original": sha(b), "bytes_original": len(b), "sha256_enmascarado": sha(m),
                      "bytes_enmascarado": len(m), "reemplazos": n})
    out = {"que": "el cwd de las transcripciones y los streams de las sesiones pagas de A2.2, con la carpeta personal reemplazada "
                  "por $HOME y ningún otro cambio de bytes (pre-registro de A2.2, §7, A-D4, (a))",
           "script": "data/experiment/banco_mcp/a2_2/enmascarar_cwd_a2_2.py", "originales_fuera_del_repo": ORIGINALES,
           "n_archivos": len(filas), "n_reemplazos": sum(f["reemplazos"] for f in filas), "archivos": filas}
    Path(salida).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(filas)} archivos, {out['n_reemplazos']} reemplazos")


def controlar(raiz, js):
    d = json.loads(Path(js).read_text(encoding="utf-8"))
    if sorted(f["ruta"] for f in d["archivos"]) != rutas(raiz) or d["n_archivos"] != len(d["archivos"]):
        frena("los archivos de las carpetas no son los del JSON")
    cp = carpeta_personal(raiz)
    nuevos = []
    for f in d["archivos"]:
        b = (raiz / f["ruta"]).read_bytes()
        if sha(b) != f["sha256_original"]:
            frena(f"{f['ruta']}: no es el original revisado")
        m, n = enmascarar(b, cp)
        if sha(m) != f["sha256_enmascarado"] or n != f["reemplazos"]:
            frena(f"{f['ruta']}: la versión enmascarada no es la revisada")
        nuevos.append((f, b, m))
    return nuevos


def resguardar(nuevos, originales: Path):
    """Copia cada original a la carpeta de originales, con la ruta del repo, y controla su sha256 en la copia. Frena antes de
    escribir si ya hay un archivo distinto en el destino."""
    for f, b, _ in nuevos:
        q = originales / f["ruta"]
        if q.exists() and sha(q.read_bytes()) != f["sha256_original"]:
            frena(f"{f['ruta']}: en la carpeta de originales ya hay un archivo distinto")
    for f, b, _ in nuevos:
        q = originales / f["ruta"]
        q.parent.mkdir(parents=True, exist_ok=True)
        if not q.exists():
            t = q.with_name(q.name + ".copiando")
            t.write_bytes(b)
            os.replace(t, q)
        if sha(q.read_bytes()) != f["sha256_original"]:
            frena(f"{f['ruta']}: la copia del original no dio su sha256")


def main():
    args = sys.argv[1:]
    originales = ORIGINALES_DIR
    if "--originales" in args:
        i = args.index("--originales")
        originales = Path(args[i + 1]).resolve()
        del args[i:i + 2]
    if len(args) < 3 or args[0] not in ("--calcular", "--probar", "--aplicar"):
        frena("uso: --calcular <raíz> <salida.json> | --probar <raíz> <json> | --aplicar <raíz> <json> [--originales <dir>]")
    modo, raiz = args[0], Path(args[1]).resolve()
    if modo == "--calcular":
        return calcular(raiz, args[2])
    nuevos = controlar(raiz, args[2])
    if modo == "--probar":
        print(f"PRUEBA: {len(nuevos)} de {len(nuevos)} originales y sus versiones enmascaradas dan lo revisado; no escribí nada")
        return
    if originales.resolve().is_relative_to(raiz):
        frena("la carpeta de originales no puede estar dentro de la raíz")
    resguardar(nuevos, originales)
    for f, _, m in nuevos:
        p = raiz / f["ruta"]
        t = p.with_name(p.name + ".enmascarando")
        t.write_bytes(m)
        os.chmod(t, 0o644)
        os.replace(t, p)
        if sha(p.read_bytes()) != f["sha256_enmascarado"]:
            frena(f"{f['ruta']}: en el disco no quedó la versión revisada")
    print(f"{len(nuevos)} archivos enmascarados, cada uno con el sha256 revisado; sus originales, fuera de la raíz")


if __name__ == "__main__":
    main()
