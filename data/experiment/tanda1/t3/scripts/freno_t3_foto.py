"""B6.1, tanda 1, T3: la sección de la foto del FRENO T3, por script (decisión 1.5 del «seguí»), desde las dos fotos del repo
(t2/foto_repo_tanda1_t2.py, crudas) y las dos listas de .pyc. Solo lee; escribe <salida.md> (fuera del repo) y la imprime.
  - lo nuevo, lo borrado y lo cambiado, agrupado por las rutas que el «seguí» admite (corpus_tanda1/ens_*, tanda1/t3/, la fixture y
    grafos.py) y, aparte, lo que caiga fuera de ellas;
  - los .pyc antes y después;
  - el sha256 de los archivos clave (los cuatro kg.json, los manifiestos del acumulado y la fixture) y de cada script de t3/scripts/,
    tomados de la foto de después.
Uso: python3 -I -B freno_t3_foto.py <foto_antes.json> <foto_despues.json> <pyc_antes.txt> <pyc_despues.txt> <salida.md>
"""
import json
import sys
from pathlib import Path

FA, FD, PA, PD, OUT = (Path(x) for x in sys.argv[1:6])
fa, fd = (json.loads(p.read_text(encoding="utf-8")) for p in (FA, FD))
a, d = fa["archivos"], fd["archivos"]
X = "data/experiment/reextraccion_v2"
T3 = "data/experiment/tanda1/t3"
FIXTURE = "scripts/regression_kg_esperado.json"
GRUPOS = [(f"{X}/corpus_tanda1/ens_veinte_r2b/", "corpus_tanda1/ens_veinte_r2b/"),
          (f"{X}/corpus_tanda1/ens_veinte_r2b_sincola/", "corpus_tanda1/ens_veinte_r2b_sincola/"),
          (f"{T3}/acumulado/", "tanda1/t3/acumulado/"), (f"{T3}/scripts/", "tanda1/t3/scripts/"), (f"{T3}/", "tanda1/t3/, lo demás")]


def mil(n: int) -> str:
    return f"{n:,}".replace(",", ".")


def grupo(rel: str) -> str:
    return next((n for pre, n in GRUPOS if rel.startswith(pre)), "FUERA DE LAS RUTAS ADMITIDAS")


nuevos = sorted(set(d) - set(a))
borrados = sorted(set(a) - set(d))
cambiados = sorted(k for k in set(a) & set(d) if a[k] != d[k])
w = []
w.append("## 7. La foto del repo, los .pyc y el grep de convenciones\n")
w.append(f"- **La foto** (`t2/foto_repo_tanda1_t2.py`). Antes: {fa['inicio'][11:]} a {fa['fin'][11:]} del {fa['inicio'][:10]}, {mil(fa['n'])} "
         f"entradas. Después: {fd['inicio'][11:]} a {fd['fin'][11:]} del {fd['inicio'][:10]}, {mil(fd['n'])} entradas, {fd['sin_abrir']} sin "
         f"abrir y {fd['enlaces']} enlaces.")
cuenta = {}
for r in nuevos:
    cuenta[grupo(r)] = cuenta.get(grupo(r), 0) + 1
w.append(f"  - **{len(nuevos)} nuevos:** " + "; ".join(f"{n} en `{g}`" if not g.startswith("FUERA") else f"{n} {g}"
                                                    for g, n in sorted(cuenta.items(), key=lambda x: x[0])) + ".")
fuera_n = [r for r in nuevos if grupo(r).startswith("FUERA")]
for r in fuera_n:
    w.append(f"    - fuera de las rutas admitidas: `{r}`")
w.append(f"  - **{len(borrados)} borrados**" + (": " + ", ".join(f"`{r}`" for r in borrados) if borrados else "") + ".")
w.append(f"  - **{len(cambiados)} {'cambiado' if len(cambiados) == 1 else 'cambiados'}**" + (":" if cambiados else "."))
for r in cambiados:
    if a[r].get("sin_abrir") or d[r].get("sin_abrir"):
        w.append(f"    - `{r}`, solo por tamaño y fecha: de {a[r].get('bytes')} a {d[r].get('bytes')} bytes;")
    elif "sha256" in a[r] and "sha256" in d[r]:
        w.append(f"    - `{r}`: `{a[r]['sha256'][:16]}…` → `{d[r]['sha256'][:16]}…`, de {mil(a[r]['bytes'])} a {mil(d[r]['bytes'])} bytes;")
    else:
        w.append(f"    - `{r}`: {a[r]} → {d[r]};")
otros = [r for r in cambiados if r != FIXTURE]
w.append(f"  - Fuera de las rutas admitidas: {len(fuera_n)} nuevos, {len(borrados)} borrados y {len(otros)} cambiados además de la fixture. "
         f"Algún `grafos.py` nuevo o cambiado: {any(Path(r).name == 'grafos.py' for r in nuevos + cambiados)}.")
pa, pd = (p.read_text(encoding="utf-8").splitlines() for p in (PA, PD))
w.append(f"- **Los `.pyc`:** {mil(len(pa))} líneas antes y {mil(len(pd))} después; listas iguales: {pa == pd}.")
w.append("\n**El sha256 de los archivos clave, de la foto de después:**\n")
w.append("| archivo | sha256 |")
w.append("|---|---|")
clave = [f"{X}/corpus_tanda1/ens_veinte_r2b/r2/kg.json", f"{X}/corpus_tanda1/ens_veinte_r2b_sincola/r2/kg.json",
         f"{T3}/acumulado/ens_treinta_r2b/r2/kg.json", f"{T3}/acumulado/ens_treinta_r2b_sincola/r2/kg.json",
         f"{T3}/acumulado/manifiestos/acumulado_30tos_r2b.json", f"{T3}/acumulado/manifiestos/acumulado_ens_treinta_r2b.json",
         f"{T3}/acumulado/manifiestos/acumulado_ens_treinta_r2b_sincola.json", FIXTURE]
for r in clave:
    w.append(f"| `{r}` | `{d[r]['sha256']}` |")
w.append(f"\nLa fixture en HEAD (foto de antes): `{a[FIXTURE]['sha256']}`.")
w.append("\n**Los scripts de T3** (`t3/scripts/`, sha256 de la foto de después):\n")
w.append("| script | sha256 |")
w.append("|---|---|")
for r in sorted(k for k in d if k.startswith(f"{T3}/scripts/")):
    w.append(f"| `{Path(r).name}` | `{d[r]['sha256']}` |")
texto = "\n".join(w) + "\n"
OUT.write_text(texto, encoding="utf-8")
print(texto)
