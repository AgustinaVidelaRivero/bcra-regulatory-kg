"""B6.1, tanda 1, T4, segundo tramo: la sección de la foto del FRENO, por script, desde la foto del paso 0 y la de después
(t2/foto_repo_tanda1_t2.py, crudas), las dos listas de .pyc y la salida de las tasas (si hubo ampliación). Solo lee; escribe <salida.md>
(fuera del repo) y la imprime. Copia de freno_t4t1_foto.py con lo que admite el segundo tramo:
  - lo nuevo, solo en tanda1/t4/; t3/muestras/unidades_a_la_vista_T4.json, solo si hubo ampliación; los .DS_Store van aparte
    (indicación de la autora en el paso 0); lo demás es «fuera de lo admitido»;
  - el NO_ABRIR_ del primer tramo, sin abrirlo: su tamaño y su hora en las dos fotos (la foto no lo abre);
  - el sha256 de los archivos de este tramo y de cada script nuevo de tanda1/t4/scripts/, de la foto de después.
Uso: python3 -I -B freno_t4t2_foto.py <foto_antes.json> <foto_despues.json> <pyc_antes.txt> <pyc_despues.txt> <tasas.json> <salida.md>
"""
import json
import sys
from datetime import datetime
from pathlib import Path

sys.dont_write_bytecode = True
FA, FD, PA, PD, TASAS, OUT = (Path(x) for x in sys.argv[1:7])
fa, fd = (json.loads(p.read_text(encoding="utf-8")) for p in (FA, FD))
a, d = fa["archivos"], fd["archivos"]
amp = json.loads(TASAS.read_text(encoding="utf-8"))["ampliacion"]["hay_ampliacion"]
T4 = "data/experiment/tanda1/t4"
VISTA = "data/experiment/tanda1/t3/muestras/unidades_a_la_vista_T4.json"
NA1 = f"{T4}/NO_ABRIR_conteos_t4.json"
GRUPOS = ([(VISTA, "el archivo del punto 5 (ampliación)")] if amp else []) + [
    (f"{T4}/scripts/", "tanda1/t4/scripts/"), (f"{T4}/tasas/", "tanda1/t4/tasas/"), (f"{T4}/", "tanda1/t4/, lo demás")]


def mil(n: int) -> str:
    return f"{n:,}".replace(",", ".")


def grupo(rel: str) -> str:
    if rel.endswith(".DS_Store"):
        return ".DS_Store (paso 0)"
    return next((n for pre, n in GRUPOS if rel.startswith(pre)), "FUERA DE LO ADMITIDO")


nuevos = sorted(set(d) - set(a))
borrados = sorted(set(a) - set(d))
cambiados = sorted(k for k in set(a) & set(d) if a[k] != d[k])
w = ["## 11. La foto del repo, los .pyc y el grep de convenciones", "",
     "Lo genera `scripts/freno_t4t2_foto.py` desde la foto del paso 0 y la de después (las dos van en el paquete).", "",
     f"- **La foto** (`t2/foto_repo_tanda1_t2.py`). Paso 0: {fa['inicio'][11:]} a {fa['fin'][11:]} del {fa['inicio'][:10]}, {mil(fa['n'])} "
     f"entradas. Después: {fd['inicio'][11:]} a {fd['fin'][11:]} del {fd['inicio'][:10]}, {mil(fd['n'])} entradas, {fd['sin_abrir']} sin abrir "
     f"y {fd['enlaces']} enlaces."]
for nombre, lista in (("nuevos", nuevos), ("borrados", borrados), ("cambiados", cambiados)):
    cuenta = {}
    for r in lista:
        cuenta[grupo(r)] = cuenta.get(grupo(r), 0) + 1
    w.append(f"  - **{len(lista)} {nombre}:** " + ("; ".join(f"{n} en `{g}`" if g.startswith("tanda1") else f"{n}, {g}"
                                                           for g, n in sorted(cuenta.items())) or "ninguno") + ".")
fuera = [r for r in nuevos + borrados + cambiados if grupo(r) == "FUERA DE LO ADMITIDO"]
w.append(f"  - **Fuera de lo admitido:** {len(fuera)}" + (": " + ", ".join(f"`{r}`" for r in fuera) if fuera else "") + ".")
ds = [r for r in nuevos + cambiados if r.endswith(".DS_Store")]
if ds:
    w.append("  - **Los `.DS_Store` que aparecieron o cambiaron durante el tramo** (sin abrirlos; hora de la foto de después): " + "; ".join(
        f"`{r}`, {datetime.fromtimestamp(d[r]['mtime']).strftime('%H:%M:%S')}" for r in ds) + ".")
w.append(f"  - **El `NO_ABRIR_` del primer tramo** (`{NA1}`), sin abrirlo: {mil(a[NA1]['bytes'])} bytes y hora "
         f"{datetime.fromtimestamp(a[NA1]['mtime']).strftime('%Y-%m-%d %H:%M:%S')} en el paso 0; en la foto de después, igual: {a[NA1] == d[NA1]}.")
w.append(f"  - **`unidades_a_la_vista_T4.json`** (`t3/muestras/`): sin ampliación no se toca; igual en las dos fotos: {a[VISTA] == d[VISTA]} "
         f"(`{d[VISTA]['sha256'][:16]}…`).")
pa, pd = (p.read_text(encoding="utf-8").splitlines() for p in (PA, PD))
w.append(f"- **Los `.pyc`:** {mil(len(pa))} líneas en el paso 0 y {mil(len(pd))} después; listas iguales: {pa == pd}.")
w += ["", "**El sha256 de los archivos de este tramo, de la foto de después:**", "", "| archivo | sha256 |", "|---|---|"]
for k in nuevos:
    if k.startswith(f"{T4}/") and not k.startswith(f"{T4}/scripts/") and not k.endswith(".DS_Store"):
        w.append(f"| `{k}` | `{d[k]['sha256']}` |")
w += ["", "**Los scripts de este tramo** (`t4/scripts/`, sha256 de la foto de después):", "", "| script | sha256 |", "|---|---|"]
for k in sorted(x for x in nuevos if x.startswith(f"{T4}/scripts/")):
    w.append(f"| `{Path(k).name}` | `{d[k]['sha256']}` |")
texto = "\n".join(w) + "\n"
OUT.write_text(texto, encoding="utf-8")
print(texto)
