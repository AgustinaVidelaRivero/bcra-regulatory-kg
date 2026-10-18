"""B6.1, tanda 1, T4, primer tramo: la sección de la foto del FRENO, por script, desde la foto del paso 0 y la de después
(t2/foto_repo_tanda1_t2.py, crudas) y las dos listas de .pyc. Solo lee; escribe <salida.md> (fuera del repo) y la imprime.
  - Lo nuevo, lo borrado y lo cambiado, agrupado por lo que el mandato admite: lo nuevo en tanda1/t4/ y el archivo del punto 5
    (tanda1/t3/muestras/unidades_a_la_vista_T4.json); los .DS_Store van aparte (indicación de la autora en el paso 0); lo demás es
    «fuera de lo admitido».
  - Los .pyc antes y después.
  - El sha256 de los archivos clave y de cada script de tanda1/t4/scripts/, de la foto de después. El del NO_ABRIR_ no está en la foto
    (no se abre): sale de la escritura (<escrituras.json>).
Uso: python3 -I -B freno_t4t1_foto.py <foto_antes.json> <foto_despues.json> <pyc_antes.txt> <pyc_despues.txt> <escrituras.json> <salida.md>
"""
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
FA, FD, PA, PD, ESC, OUT = (Path(x) for x in sys.argv[1:7])
fa, fd = (json.loads(p.read_text(encoding="utf-8")) for p in (FA, FD))
a, d = fa["archivos"], fd["archivos"]
esc = json.loads(ESC.read_text(encoding="utf-8"))
T4 = "data/experiment/tanda1/t4"
VISTA = "data/experiment/tanda1/t3/muestras/unidades_a_la_vista_T4.json"
GRUPOS = [(VISTA, "el archivo del punto 5"), (f"{T4}/scripts/", "tanda1/t4/scripts/"), (f"{T4}/muestras/", "tanda1/t4/muestras/"),
          (f"{T4}/lectura_asistida/", "tanda1/t4/lectura_asistida/"), (f"{T4}/lectura_autora/", "tanda1/t4/lectura_autora/"),
          (f"{T4}/", "tanda1/t4/, lo demás")]


def mil(n: int) -> str:
    return f"{n:,}".replace(",", ".")


def grupo(rel: str) -> str:
    if rel.endswith(".DS_Store"):
        return ".DS_Store (paso 0)"
    return next((n for pre, n in GRUPOS if rel.startswith(pre)), "FUERA DE LO ADMITIDO")


nuevos = sorted(set(d) - set(a))
borrados = sorted(set(a) - set(d))
cambiados = sorted(k for k in set(a) & set(d) if a[k] != d[k])
w = ["## La foto del repo, los .pyc y el grep de convenciones", "",
     "Lo genera `scripts/freno_t4t1_foto.py` desde la foto del paso 0 y la de después (las dos van en el paquete).", "",
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
if VISTA in cambiados:
    w.append(f"  - `unidades_a_la_vista_T4.json`: `{a[VISTA]['sha256'][:16]}…` (HEAD, el del T3a) → `{d[VISTA]['sha256'][:16]}…`.")
pa, pd = (p.read_text(encoding="utf-8").splitlines() for p in (PA, PD))
w.append(f"- **Los `.pyc`:** {mil(len(pa))} líneas en el paso 0 y {mil(len(pd))} después; listas iguales: {pa == pd}.")
w += ["", "**El sha256 de los archivos clave, de la foto de después** (el del `NO_ABRIR_`, de la escritura):", "", "| archivo | sha256 |", "|---|---|"]
for k in (VISTA, f"{T4}/muestras/unidades_a_la_vista_T4_regla_de_T3.json", f"{T4}/muestras/poblaciones_t4_tramo1.json",
          f"{T4}/muestras/sorteos_t4_tramo1.json", f"{T4}/muestras/material/material_t4_tramo1.json",
          f"{T4}/lectura_asistida/lectura_asistida_t4_tramo1.json", f"{T4}/tablas_t4_tramo1.md"):
    w.append(f"| `{k}` | `{d[k]['sha256']}` |")
na = f"{T4}/NO_ABRIR_conteos_t4.json"
w.append(f"| `{na}` | `{esc['escritos'][na]['sha256']}` |")
w += ["", "**Los scripts de este tramo** (`t4/scripts/`, sha256 de la foto de después):", "", "| script | sha256 |", "|---|---|"]
for k in sorted(x for x in nuevos if x.startswith(f"{T4}/scripts/")):
    w.append(f"| `{Path(k).name}` | `{d[k]['sha256']}` |")
texto = "\n".join(w) + "\n"
OUT.write_text(texto, encoding="utf-8")
print(texto)
