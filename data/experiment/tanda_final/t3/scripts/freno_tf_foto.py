"""B6.1, tanda final, T3: la sección de la foto del FRENO T3, por script, desde la foto del paso 0 y la de después
(tanda_final/t1/foto_repo_tanda_final_t1.py, crudas, fuera del repo) y las dos listas de .pyc, con
data/experiment/tanda1/t3/scripts/freno_t3f_foto.py como modelo. Solo lee; escribe <salida.md> y <salida.json> (fuera del repo) y
imprime el .md.
  - Lo nuevo, lo borrado y lo cambiado, agrupado por lo que el punto 9 del «seguí» admite: corpus_tanda_final/ens_*, tanda_final/t3/,
    la versión derivada de la lectura, la fixture y grafos.py; la base de Neo4j (data/experiment/neo4j/volumen/, fuera de git: la cambia
    la carga del punto 5); y, aparte, lo que caiga fuera de todo eso.
  - Los .pyc antes y después.
  - El sha256 de la fixture, de grafos.py y del registro de la vista, de la foto de después.
Uso: python3 -I -B freno_tf_foto.py <foto_antes.json> <foto_despues.json> <pyc_antes.txt> <pyc_despues.txt> <salida.md> <salida.json>
"""
import json
import sys
from pathlib import Path

FA, FD, PA, PD, OUT, OUTJ = (Path(x) for x in sys.argv[1:7])
fa, fd = (json.loads(p.read_text(encoding="utf-8")) for p in (FA, FD))
a, d = fa["archivos"], fd["archivos"]
T3 = "data/experiment/tanda_final/t3"
X = "data/experiment/reextraccion_v2/corpus_tanda_final"
GRUPOS = [("data/experiment/neo4j/volumen/", "la base de Neo4j (neo4j/volumen/, fuera de git)"),
          ("data/experiment/neo4j/grafos.py", "neo4j/grafos.py"), ("scripts/regression_kg_esperado.json", "la fixture"),
          ("data/experiment/tanda_final/preregistro/preregistro_tanda_final_derivada_T4.", "la versión derivada de la lectura"),
          (f"{X}/ens_98_r2b/", "corpus_tanda_final/ens_98_r2b/"), (f"{X}/ens_98_r2b_sincola/", "corpus_tanda_final/ens_98_r2b_sincola/"),
          (f"{X}/ens_tramo1_r2b/", "corpus_tanda_final/ens_tramo1_r2b/"),
          (f"{X}/ens_tramo1_r2b_sincola/", "corpus_tanda_final/ens_tramo1_r2b_sincola/"),
          (f"{T3}/acumulado/", "tanda_final/t3/acumulado/"), (f"{T3}/gate/", "tanda_final/t3/gate/"),
          (f"{T3}/gate_decisiones/", "tanda_final/t3/gate_decisiones/"), (f"{T3}/scripts/", "tanda_final/t3/scripts/"),
          (f"{T3}/neo4j/", "tanda_final/t3/neo4j/"), (f"{T3}/conteos_sin_leer/", "tanda_final/t3/conteos_sin_leer/"),
          (f"{T3}/salidas/", "tanda_final/t3/salidas/"), (f"{T3}/corridas/", "tanda_final/t3/corridas/"),
          (f"{T3}/nombres_remision/", "tanda_final/t3/nombres_remision/"), (f"{T3}/intrinsecas_gen3/", "tanda_final/t3/intrinsecas_gen3/"),
          (f"{T3}/selftests/", "tanda_final/t3/selftests/"), (f"{T3}/e0_con_partes/", "tanda_final/t3/e0_con_partes/"),
          (f"{T3}/prueba_raya_tramo1/", "tanda_final/t3/prueba_raya_tramo1/"),
          (f"{T3}/muestras/", "tanda_final/t3/muestras/"), (f"{T3}/", "tanda_final/t3/, lo demás")]
CLAVE = ["scripts/regression_kg_esperado.json", "data/experiment/neo4j/grafos.py", f"{T3}/registro_vista_r2b_tanda_final.py",
         "data/experiment/tanda_final/preregistro/preregistro_tanda_final_derivada_T4.md",
         "data/experiment/tanda_final/preregistro/preregistro_tanda_final_derivada_T4.huecos.json"]


def mil(n: int) -> str:
    return f"{n:,}".replace(",", ".")


def grupo(rel: str) -> str:
    return next((n for pre, n in GRUPOS if rel.startswith(pre)), "FUERA DE LO ADMITIDO")


nuevos = sorted(set(d) - set(a))
borrados = sorted(set(a) - set(d))
cambiados = sorted(k for k in set(a) & set(d) if a[k] != d[k])
import hashlib  # noqa: E402
res = {"foto_antes": {"sha256": hashlib.sha256(FA.read_bytes()).hexdigest(), "inicio": fa["inicio"], "fin": fa["fin"], "n": fa["n"],
                      "sin_abrir": fa["sin_abrir"], "enlaces": fa["enlaces"]},
       "foto_despues": {"sha256": hashlib.sha256(FD.read_bytes()).hexdigest(), "inicio": fd["inicio"], "fin": fd["fin"], "n": fd["n"],
                        "sin_abrir": fd["sin_abrir"], "enlaces": fd["enlaces"]},
       "nuevos": len(nuevos), "borrados": len(borrados), "cambiados": len(cambiados), "por_grupo": {}}
w = ["## 7. La foto del repo, los .pyc, lo escrito en el repo y el grep de convenciones", "",
     "Lo genera `scripts/freno_tf_foto.py` desde la foto del paso 0 y la de después (`tanda_final/t1/foto_repo_tanda_final_t1.py`; las "
     "dos, fuera del repo y del paquete, porque nombran todas las rutas del repo; en el paquete van su sha256 y este resumen).", "",
     f"- **La foto.** Paso 0: {fa['inicio'][11:]} a {fa['fin'][11:]} del {fa['inicio'][:10]}, {mil(fa['n'])} entradas. Después: "
     f"{fd['inicio'][11:]} a {fd['fin'][11:]} del {fd['inicio'][:10]}, {mil(fd['n'])} entradas, {fd['sin_abrir']} sin abrir y "
     f"{fd['enlaces']} enlaces."]
for nombre, lista in (("nuevos", nuevos), ("borrados", borrados), ("cambiados", cambiados)):
    cuenta = {}
    for r in lista:
        cuenta[grupo(r)] = cuenta.get(grupo(r), 0) + 1
    res["por_grupo"][nombre] = cuenta
    w.append(f"  - **{mil(len(lista))} {nombre}:** " + ("; ".join(f"{mil(n)} en `{g}`" if not g.startswith(("FUERA", "la base", "la "))
                                                                 else f"{mil(n)} {g}" for g, n in sorted(cuenta.items())) or "ninguno") + ".")
fuera = [r for r in nuevos + borrados + cambiados if grupo(r) == "FUERA DE LO ADMITIDO"]
res["fuera_de_lo_admitido"] = fuera
w.append(f"  - **Fuera de lo admitido:** {len(fuera)}" + (": " + ", ".join(f"`{r}`" for r in fuera) if fuera else "") + ".")
for r in ("scripts/regression_kg_esperado.json", "data/experiment/neo4j/grafos.py"):
    if r in cambiados:
        w.append(f"  - `{r}`: `{a[r]['sha256'][:16]}…` (HEAD) → `{d[r]['sha256'][:16]}…`, de {mil(a[r]['bytes'])} a {mil(d[r]['bytes'])} bytes.")
pa, pd = (p.read_text(encoding="utf-8").splitlines() for p in (PA, PD))
res["pyc"] = {"antes": len(pa), "despues": len(pd), "iguales": pa == pd}
w.append(f"- **Los `.pyc`:** {mil(len(pa))} líneas en el paso 0 y {mil(len(pd))} después; listas iguales: {pa == pd}.")
w += ["", "**El sha256 de los archivos clave, de la foto de después:**", "", "| archivo | sha256 |", "|---|---|"]
for k in CLAVE:
    w.append(f"| `{k}` | " + (f"`{d[k]['sha256']}`" if k in d else "no está: es de los puntos 5 o 7, que no corrí") + " |")
res["clave"] = {k: (d[k]["sha256"] if k in d else None) for k in CLAVE}
texto = "\n".join(w) + "\n"
OUT.write_text(texto, encoding="utf-8")
OUTJ.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(texto)
