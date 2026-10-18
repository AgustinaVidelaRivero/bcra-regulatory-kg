"""B6.1, tanda 1, T3 (desde el punto 4): la sección de la foto del FRENO T3 final, por script, desde la foto del paso 0 y la de después
(t2/foto_repo_tanda1_t2.py, crudas) y las dos listas de .pyc. Solo lee; escribe <salida.md> (fuera del repo) y la imprime.
  - Lo nuevo, lo borrado y lo cambiado, agrupado por las rutas que el mandato admite (tanda1/t3/, grafos.py y el FRENO parcial
    renombrado), la base de Neo4j (data/experiment/neo4j/volumen/, fuera de git: la cambia la carga del punto 5), el .DS_Store de
    escalado_prep/ (indicación de la autora en el paso 0) y, aparte, lo que caiga fuera de todo eso.
  - Los .pyc antes y después.
  - El sha256 de grafos.py y del registro de la vista, y el de cada script nuevo de tanda1/t3/scripts/, de la foto de después. El de
    NO_ABRIR_conteos_t3.json no está en la foto (no se abre): sale de la escritura (<escrituras.json>).
Uso: python3 -I -B freno_t3f_foto.py <foto_antes.json> <foto_despues.json> <pyc_antes.txt> <pyc_despues.txt> <escrituras.json> <salida.md>
"""
import json
import sys
from pathlib import Path

FA, FD, PA, PD, ESC, OUT = (Path(x) for x in sys.argv[1:7])
fa, fd = (json.loads(p.read_text(encoding="utf-8")) for p in (FA, FD))
a, d = fa["archivos"], fd["archivos"]
esc = json.loads(ESC.read_text(encoding="utf-8"))
T3 = "data/experiment/tanda1/t3"
GRUPOS = [("data/experiment/neo4j/volumen/", "la base de Neo4j (neo4j/volumen/, fuera de git)"),
          ("data/experiment/neo4j/grafos.py", "neo4j/grafos.py"),
          ("data/experiment/escalado_prep/.DS_Store", "escalado_prep/.DS_Store"),
          (f"{T3}/FRENO_T3_parcial.md", "tanda1/t3/FRENO_T3_parcial.md (el renombre)"),
          (f"{T3}/FRENO_T3.md", "tanda1/t3/FRENO_T3.md (renombrado al parcial; el final se escribe después de la foto)"),
          (f"{T3}/scripts/", "tanda1/t3/scripts/"), (f"{T3}/gate_decisiones/", "tanda1/t3/gate_decisiones/"),
          (f"{T3}/neo4j/", "tanda1/t3/neo4j/"), (f"{T3}/conteos_sin_leer/", "tanda1/t3/conteos_sin_leer/"),
          (f"{T3}/muestras/", "tanda1/t3/muestras/"), (f"{T3}/", "tanda1/t3/, lo demás")]


def mil(n: int) -> str:
    return f"{n:,}".replace(",", ".")


def grupo(rel: str) -> str:
    return next((n for pre, n in GRUPOS if rel.startswith(pre)), "FUERA DE LO ADMITIDO")


nuevos = sorted(set(d) - set(a))
borrados = sorted(set(a) - set(d))
cambiados = sorted(k for k in set(a) & set(d) if a[k] != d[k])
w = ["## La foto del repo, los .pyc y el grep de convenciones", "",
     f"Lo genera `scripts/freno_t3f_foto.py` desde la foto del paso 0 y la de después (las dos van en el paquete).", "",
     f"- **La foto** (`t2/foto_repo_tanda1_t2.py`). Paso 0: {fa['inicio'][11:]} a {fa['fin'][11:]} del {fa['inicio'][:10]}, {mil(fa['n'])} "
     f"entradas. Después: {fd['inicio'][11:]} a {fd['fin'][11:]} del {fd['inicio'][:10]}, {mil(fd['n'])} entradas, {fd['sin_abrir']} sin abrir "
     f"y {fd['enlaces']} enlaces."]
for nombre, lista in (("nuevos", nuevos), ("borrados", borrados), ("cambiados", cambiados)):
    cuenta = {}
    for r in lista:
        cuenta[grupo(r)] = cuenta.get(grupo(r), 0) + 1
    w.append(f"  - **{len(lista)} {nombre}:** " + ("; ".join(f"{n} en `{g}`" if not g.startswith(("FUERA", "la base")) else f"{n} {g}"
                                                           for g, n in sorted(cuenta.items())) or "ninguno") + ".")
fuera = [r for r in nuevos + borrados + cambiados if grupo(r) == "FUERA DE LO ADMITIDO"]
w.append(f"  - **Fuera de lo admitido:** {len(fuera)}" + (": " + ", ".join(f"`{r}`" for r in fuera) if fuera else "") + ".")
r = "data/experiment/neo4j/grafos.py"
if r in cambiados:
    w.append(f"  - `grafos.py`: `{a[r]['sha256'][:16]}…` (HEAD) → `{d[r]['sha256'][:16]}…`, de {mil(a[r]['bytes'])} a {mil(d[r]['bytes'])} bytes.")
pa, pd = (p.read_text(encoding="utf-8").splitlines() for p in (PA, PD))
w.append(f"- **Los `.pyc`:** {mil(len(pa))} líneas en el paso 0 y {mil(len(pd))} después; listas iguales: {pa == pd}.")
w += ["", "**El sha256 de los archivos clave, de la foto de después** (el del `NO_ABRIR_`, de la escritura):", "", "| archivo | sha256 |", "|---|---|"]
for k in ("data/experiment/neo4j/grafos.py", f"{T3}/registro_vista_r2b_tanda1.py", f"{T3}/FRENO_T3_parcial.md",
          f"{T3}/gate_decisiones/veredicto_gate_t3f.json", f"{T3}/conteos_sin_leer/contado_sin_leer_t3f.json",
          f"{T3}/muestras/poblaciones_t4.json", f"{T3}/muestras/umbrales_t4_reales.json", f"{T3}/muestras/sorteos_t4.json",
          f"{T3}/muestras/material/material_t4.json", f"{T3}/muestras/unidades_a_la_vista_T4.json"):
    w.append(f"| `{k}` | `{d[k]['sha256']}` |")
na = f"{T3}/NO_ABRIR_conteos_t3.json"
w.append(f"| `{na}` | `{esc['escritos'][na]['sha256']}` |")
w += ["", "**Los scripts nuevos de esta parte** (`t3/scripts/`, sha256 de la foto de después):", "", "| script | sha256 |", "|---|---|"]
for k in sorted(x for x in nuevos if x.startswith(f"{T3}/scripts/")):
    w.append(f"| `{Path(k).name}` | `{d[k]['sha256']}` |")
viejos = [x for x in a if x.startswith(f"{T3}/scripts/")]
w.append(f"\nLos {len(viejos)} scripts del FRENO parcial no cambiaron: {all(a[x] == d.get(x) for x in viejos)}.")
texto = "\n".join(w) + "\n"
OUT.write_text(texto, encoding="utf-8")
print(texto)
