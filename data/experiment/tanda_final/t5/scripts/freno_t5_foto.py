"""B6.1, tanda final, T5: la sección de la foto del FRENO, por script, desde la foto del paso 0 (t4t2_fotos/foto_repo_antes_T5.json) y la
de después (las dos de t5/scripts/foto_repo_sin_clasificacion_t5.py, sin t4/clasificacion_freno/; en t4t2_fotos/, fuera del repo y del
paquete), las dos listas de .pyc y la salida de las cifras. Solo lee; escribe <salida.md> (fuera del repo) y la imprime. Es
t4/scripts/freno_t4t3_foto_tf.py con lo que admite T5:
  - lo nuevo, solo en tanda_final/t5/; lo cambiado, solo data/experiment/neo4j/grafos.py (las dos entradas del tramo 1); nada de t1/ a
    t4/; los archivos que se llaman exactamente .DS_Store van aparte, con su ruta; lo demás es «fuera de lo admitido»;
  - t4/clasificacion_freno/ queda fuera de las dos fotos (no se abre);
  - el sha256 de los archivos de T5 y de cada script nuevo de tanda_final/t5/scripts/, de la foto de después.
Uso: python3 -I -B freno_t5_foto.py <foto_antes.json> <foto_despues.json> <pyc_antes.txt> <pyc_despues.txt> <cifras.json> <salida.md>
"""
import hashlib
import json
import sys
from datetime import datetime
from pathlib import Path

sys.dont_write_bytecode = True
FA, FD, PA, PD, TASAS, OUT = (Path(x) for x in sys.argv[1:7])
fa, fd = (json.loads(p.read_text(encoding="utf-8")) for p in (FA, FD))
EXCL = "data/experiment/tanda_final/t4/clasificacion_freno/"
a, d = ({k: v for k, v in x["archivos"].items() if not k.startswith(EXCL)} for x in (fa, fd))
assert not any(k.startswith(EXCL) for k in fa["archivos"]) and not any(k.startswith(EXCL) for k in fd["archivos"])
assert "sello_tramo1" in json.loads(TASAS.read_text(encoding="utf-8")), "no es la salida de las cifras de T5"
T4 = "data/experiment/tanda_final/t5"
GRAFOS_PY = "data/experiment/neo4j/grafos.py"
VISTA = "data/experiment/tanda_final/t3/muestras/unidades_a_la_vista_T4.json"
GRUPOS = [(GRAFOS_PY, "neo4j/grafos.py (las dos entradas del tramo 1)"),
    (f"{T4}/scripts/", "tanda_final/t5/scripts/"), (f"{T4}/salidas/", "tanda_final/t5/salidas/"), (f"{T4}/", "tanda_final/t5/, lo demás")]


def mil(n: int) -> str:
    return f"{n:,}".replace(",", ".")


def grupo(rel: str) -> str:
    if Path(rel).name == ".DS_Store":
        return ".DS_Store (ruido de Finder)"
    return next((n for pre, n in GRUPOS if rel.startswith(pre)), "FUERA DE LO ADMITIDO")


nuevos = sorted(set(d) - set(a))
borrados = sorted(set(a) - set(d))
cambiados = sorted(k for k in set(a) & set(d) if a[k] != d[k])
w = ["## 11. La foto del repo, los .pyc y el grep de convenciones", "",
     "Lo genera `scripts/freno_t5_foto.py` desde la foto del paso 0 (`foto_repo_antes_T5.json`) y la de después, las dos sin "
     "`t4/clasificacion_freno/`. Las dos quedan en `t4t2_fotos/`, en la "
     "carpeta permanente de esta sesión (`fuera_del_repo/scratchpads/<sesión>/scratchpad/`), fuera del repo y del paquete porque "
     "nombran todas las rutas del repo.", "",
     f"- **La foto** (`t1/foto_repo_tanda_final_t1.py`). La del paso 0: {fa['inicio'][11:]} a {fa['fin'][11:]} del "
     f"{fa['inicio'][:10]}, {mil(fa['n'])} entradas, sha256 `{hashlib.sha256(FA.read_bytes()).hexdigest()}`. Después: {fd['inicio'][11:]} a {fd['fin'][11:]} del {fd['inicio'][:10]}, {mil(fd['n'])} entradas, {fd['sin_abrir']} sin abrir "
     f"y {fd['enlaces']} enlaces, sha256 `{hashlib.sha256(FD.read_bytes()).hexdigest()}`."]
for nombre, lista in (("nuevos", nuevos), ("borrados", borrados), ("cambiados", cambiados)):
    cuenta = {}
    for r in lista:
        cuenta[grupo(r)] = cuenta.get(grupo(r), 0) + 1
    w.append(f"  - **{len(lista)} {nombre}:** " + ("; ".join(f"{n} en `{g}`" if g.startswith("tanda_final") else f"{n}, {g}"
                                                           for g, n in sorted(cuenta.items())) or "ninguno") + ".")
fuera = [r for r in nuevos + borrados + cambiados if grupo(r) == "FUERA DE LO ADMITIDO"]
w.append(f"  - **Fuera de lo admitido:** {len(fuera)}" + (": " + ", ".join(f"`{r}`" for r in fuera) if fuera else "") + ".")
ds = [r for r in nuevos + cambiados if Path(r).name == ".DS_Store"]
if ds:
    w.append("  - **Los `.DS_Store` que aparecieron o cambiaron durante T5** (ruido de Finder, fuera de lo que cuenta; su tamaño y "
        "su sha256 en la foto de después, que no guarda la hora de lo que abre): " + "; ".join(
        f"`{r}`, {d[r]['bytes']} bytes, sha256 `{d[r].get('sha256', '')[:12]}…`" for r in ds) + ".")
na = [r for r in sorted(set(a) | set(d)) if r.startswith(f"{T4}/") and Path(r).name.startswith("NO_ABRIR_")]
w.append(f"  - **Los `NO_ABRIR_` en `t5/`:** {len(na)} (sin abrir; tamaño en bytes y hora de la foto de después)" + (": " + ", ".join(f"`{r}`, {d[r]['bytes']} bytes" for r in na if r in d) if na else "") + ".")
w.append(f"  - **`unidades_a_la_vista_T4.json`** (`t3/muestras/`): T5 no la toca; sha256 `{a[VISTA]['sha256']}` en el paso 0 "
         f"y `{d[VISTA]['sha256']}` después; iguales: {a[VISTA] == d[VISTA]}.")
w.append(f"  - **`neo4j/grafos.py`:** sha256 `{a[GRAFOS_PY]['sha256']}` en el paso 0 y `{d[GRAFOS_PY]['sha256']}` después.")
pa, pd = (p.read_text(encoding="utf-8").splitlines() for p in (PA, PD))
w.append(f"- **Los `.pyc`:** {mil(len(pa))} líneas en el paso 0 y {mil(len(pd))} después; listas iguales: {pa == pd}.")
w += ["", "**El sha256 de los archivos de este tramo, de la foto de después:**", "", "| archivo | sha256 |", "|---|---|"]
for k in nuevos:
    if k.startswith(f"{T4}/") and not k.startswith(f"{T4}/scripts/") and Path(k).name != ".DS_Store" and not d[k].get("sin_abrir"):
        w.append(f"| `{k}` | `{d[k]['sha256']}` |")
w += ["", "**Los scripts de este tramo** (`t4/scripts/`, sha256 de la foto de después):", "", "| script | sha256 |", "|---|---|"]
for k in sorted(x for x in nuevos if x.startswith(f"{T4}/scripts/")):
    w.append(f"| `{Path(k).name}` | `{d[k]['sha256']}` |")
texto = "\n".join(w) + "\n"
OUT.write_text(texto, encoding="utf-8")
print(texto)
