"""B6.1, tanda final, T4, segundo tramo: la sección de la foto del FRENO, por script, desde la foto de las 12:16:33 (la del paso 0, que
la autora fijó como punto de comparación) y la de después (t1/foto_repo_tanda_final_t1.py, crudas; las dos, en t4t2_fotos/, fuera del
repo y del paquete), las dos listas de .pyc y la salida de las tasas. Solo lee; escribe <salida.md> (fuera del repo) y la imprime. Es
tanda1/t4/scripts/freno_t4t2_foto.py con lo que admite el segundo tramo de la tanda final:
  - lo nuevo, solo en tanda_final/t4/; t3/muestras/unidades_a_la_vista_T4.json, solo si hubo ampliación; los archivos que se llaman
    exactamente .DS_Store van aparte, con su ruta (decisión de la autora sobre el FRENO del paso 0, punto 2); lo demás es «fuera de lo
    admitido»;
  - el primer tramo no escribió ningún NO_ABRIR_ en t4/: se controla que no haya ninguno en las dos fotos;
  - el sha256 de los archivos de este tramo y de cada script nuevo de tanda_final/t4/scripts/, de la foto de después.
Uso: python3 -I -B freno_t4t2_foto_tf.py <foto_antes.json> <foto_despues.json> <pyc_antes.txt> <pyc_despues.txt> <tasas.json> <salida.md>
"""
import hashlib
import json
import sys
from datetime import datetime
from pathlib import Path

sys.dont_write_bytecode = True
FA, FD, PA, PD, TASAS, OUT = (Path(x) for x in sys.argv[1:7])
fa, fd = (json.loads(p.read_text(encoding="utf-8")) for p in (FA, FD))
a, d = fa["archivos"], fd["archivos"]
amp = json.loads(TASAS.read_text(encoding="utf-8"))["ampliacion"]["hay_ampliacion"]
T4 = "data/experiment/tanda_final/t4"
VISTA = "data/experiment/tanda_final/t3/muestras/unidades_a_la_vista_T4.json"
GRUPOS = ([(VISTA, "el archivo del punto 5 (ampliación)")] if amp else []) + [
    (f"{T4}/scripts/", "tanda_final/t4/scripts/"), (f"{T4}/tasas/", "tanda_final/t4/tasas/"),
    (f"{T4}/ampliacion/", "tanda_final/t4/ampliacion/"), (f"{T4}/", "tanda_final/t4/, lo demás")]


def mil(n: int) -> str:
    return f"{n:,}".replace(",", ".")


def grupo(rel: str) -> str:
    if Path(rel).name == ".DS_Store":
        return ".DS_Store (ruido de Finder)"
    return next((n for pre, n in GRUPOS if rel.startswith(pre)), "FUERA DE LO ADMITIDO")


nuevos = sorted(set(d) - set(a))
borrados = sorted(set(a) - set(d))
cambiados = sorted(k for k in set(a) & set(d) if a[k] != d[k])
w = ["## 12. La foto del repo, los .pyc y el grep de convenciones", "",
     "Lo genera `scripts/freno_t4t2_foto_tf.py` desde la foto de las 12:16:33 y la de después. Las dos quedan en `t4t2_fotos/`, en la "
     "carpeta permanente de esta sesión (`fuera_del_repo/scratchpads/<sesión>/scratchpad/`), fuera del repo y del paquete porque "
     "nombran todas las rutas del repo.", "",
     f"- **La foto** (`t1/foto_repo_tanda_final_t1.py`). La de las 12:16:33: {fa['inicio'][11:]} a {fa['fin'][11:]} del "
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
    w.append("  - **Los `.DS_Store` que aparecieron o cambiaron durante el tramo** (ruido de Finder, fuera de lo que cuenta; sin abrirlos; hora "
        "de la foto de después): " + "; ".join(
        f"`{r}`, {datetime.fromtimestamp(d[r]['mtime']).strftime('%H:%M:%S')}" for r in ds) + ".")
na = [r for r in sorted(set(a) | set(d)) if r.startswith(f"{T4}/") and Path(r).name.startswith("NO_ABRIR_")]
w.append(f"  - **Los `NO_ABRIR_` en `t4/`:** {len(na)} en las dos fotos" + (": " + ", ".join(f"`{r}`" for r in na) if na else "") + ".")
w.append(f"  - **`unidades_a_la_vista_T4.json`** (`t3/muestras/`): " + ("con la ampliación cambia" if amp else "sin ampliación no se toca")
         + f"; sha256 `{a[VISTA]['sha256']}` a las 12:16:33 y `{d[VISTA]['sha256']}` después; iguales: {a[VISTA] == d[VISTA]}.")
pa, pd = (p.read_text(encoding="utf-8").splitlines() for p in (PA, PD))
w.append(f"- **Los `.pyc`:** {mil(len(pa))} líneas en el paso 0 y {mil(len(pd))} después; listas iguales: {pa == pd}.")
w += ["", "**El sha256 de los archivos de este tramo, de la foto de después:**", "", "| archivo | sha256 |", "|---|---|"]
for k in nuevos:
    if k.startswith(f"{T4}/") and not k.startswith(f"{T4}/scripts/") and Path(k).name != ".DS_Store":
        w.append(f"| `{k}` | `{d[k]['sha256']}` |")
w += ["", "**Los scripts de este tramo** (`t4/scripts/`, sha256 de la foto de después):", "", "| script | sha256 |", "|---|---|"]
for k in sorted(x for x in nuevos if x.startswith(f"{T4}/scripts/")):
    w.append(f"| `{Path(k).name}` | `{d[k]['sha256']}` |")
texto = "\n".join(w) + "\n"
OUT.write_text(texto, encoding="utf-8")
print(texto)
