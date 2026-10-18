"""B6.1, tanda 1, T5: la sección de la foto del FRENO, por script, desde la foto del paso 0 y la de después (t2/foto_repo_tanda1_t2.py,
crudas), las dos listas de .pyc y la salida de la escritura (el sha256 del NO_ABRIR_, que la foto no abre). Solo lee; escribe <salida.md>
(fuera del repo) y la imprime. Copia de t4/scripts/freno_t4t2_foto.py con lo que admite T5: lo nuevo, solo en tanda1/t5/; los .DS_Store
aparte; lo demás es «fuera de lo admitido». Los NO_ABRIR_ de T2, T3 y T4, sin abrirlos: su tamaño y su hora en las dos fotos.
Uso: python3 -I -B freno_t5_foto.py <foto_antes.json> <foto_despues.json> <pyc_antes.txt> <pyc_despues.txt> <escrituras.json> <salida.md>
"""
import json
import sys
from datetime import datetime
from pathlib import Path

sys.dont_write_bytecode = True
FA, FD, PA, PD, ESC, OUT = (Path(x) for x in sys.argv[1:7])
fa, fd = (json.loads(p.read_text(encoding="utf-8")) for p in (FA, FD))
a, d = fa["archivos"], fd["archivos"]
esc = json.loads(ESC.read_text(encoding="utf-8"))["escritos"]
T5 = "data/experiment/tanda1/t5"
GRUPOS = [(f"{T5}/scripts/", "tanda1/t5/scripts/"), (f"{T5}/salidas/", "tanda1/t5/salidas/"), (f"{T5}/", "tanda1/t5/, lo demás")]
NA_VIEJOS = sorted(k for k in a if Path(k).name.startswith("NO_ABRIR_") and k.startswith("data/experiment/tanda1/t"))
mil = lambda n: f"{n:,}".replace(",", ".")  # noqa: E731


def grupo(rel: str) -> str:
    if rel.endswith(".DS_Store"):
        return ".DS_Store"
    return next((n for pre, n in GRUPOS if rel.startswith(pre)), "FUERA DE LO ADMITIDO")


nuevos = sorted(set(d) - set(a))
borrados = sorted(set(a) - set(d))
cambiados = sorted(k for k in set(a) & set(d) if a[k] != d[k])
w = ["## 12. La foto del repo, los .pyc y el grep de convenciones", "",
     "Lo genera `scripts/freno_t5_foto.py` desde la foto del paso 0 y la de después (las dos van en el paquete).", "",
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
    w.append("  - **Los `.DS_Store` que aparecieron o cambiaron** (sin abrirlos; hora de la foto de después): " + "; ".join(
        f"`{r}`, {datetime.fromtimestamp(d[r]['mtime']).strftime('%H:%M:%S')}" for r in ds) + ".")
w.append(f"  - **Los `NO_ABRIR_` de T2, T3 y T4** ({len(NA_VIEJOS)}), sin abrirlos: tamaño y hora iguales en las dos fotos: "
         f"{all(a[k] == d.get(k) for k in NA_VIEJOS)} (" + ", ".join(f"`{Path(k).name}`" for k in NA_VIEJOS) + ").")
pa, pd = (p.read_text(encoding="utf-8").splitlines() for p in (PA, PD))
w.append(f"- **Los `.pyc`:** {mil(len(pa))} líneas en el paso 0 y {mil(len(pd))} después; listas iguales: {pa == pd}.")
w += ["", "**El sha256 de los archivos de T5** (de la foto de después; el del `NO_ABRIR_`, de la escritura, porque la foto no lo abre):", "",
      "| archivo | sha256 |", "|---|---|"]
for k in nuevos:
    if k.startswith(f"{T5}/") and not k.endswith(".DS_Store"):
        h = d[k].get("sha256") or esc[k]["sha256"]
        w.append(f"| `{k[len(T5) + 1:]}` | `{h}` |")
texto = "\n".join(w) + "\n"
OUT.write_text(texto, encoding="utf-8")
print(texto)
