"""U-ALCANCE-E1, A3 (USD 0, sin API; solo lectura): la lista de los archivos leídos para los valores y las mediciones de A3
(despacho de A3, punto 5), con la ruta y el sha256 de cada uno en la base, para el control del commit: que cada uno siga en
HEAD igual que en la base de la copia.

Junta tres fuentes:
  1. el registro de lecturas de los procesos de Python (sitecustomize del hook, por PYTHONPATH: eventos «open», incluidos
     los imports) de las corridas que se pasan con --registro; cada ruta abierta para leer dentro de una copia (o de la raíz
     mínima de E0, que copia archivos de la copia con su misma ruta relativa) pasa a su ruta en el repo;
  2. los archivos que leen las herramientas de la consola en esas corridas (cmp, diff, shasum), que se pasan con --manual
     como ruta del repo; y los que leí en la sesión para entender el trabajo, con --sesion;
  3. las 78 rutas de data/experiment/controles_tanda1/codigo_de_la_cadena_47c9f1b3_mesa.json, todas.
Por cada ruta: si se rastrea, su sha256 en la base (git show <base>:<ruta>) y el de hoy en el árbol del repo (para el
control del commit, que repite la mesa), y en qué fuentes aparece. Un PDF no se rastrea: su sha256 va contra
manifest_pdfs.sha256 o la tabla de INFORME_E0.md (pdfs_contra_manifiesto_a3.py). Controla además:
  - que ningún proceso haya abierto una ruta del repo, salvo el intérprete y sus bibliotecas (.venv);
  - que ninguno haya abierto un archivo bajo las carpetas de salidas de la tanda 1 (T2 a T5), en una copia o en el repo;
  - que ninguno haya escrito dentro de una copia (solo en la salida de la corrida).
Un evento «open» sobre una ruta que no existe en la copia no es una lectura: son los .pyc que Python busca y las copias no
tienen (van sin __pycache__), los nombres de compilación («<string>») y las aperturas de shutil.rmtree, relativas a un
descriptor de carpeta (dir_fd) de una carpeta temporal, que el hook resuelve contra el directorio actual. Se cuentan aparte.
Un archivo no rastreado que sí se leyó (las bases de la caché, que .gitignore excluye) va con el sha256 de cada copia.
Uso: python3 -I -B lecturas_a3.py --repo R --base B --raiz ETIQUETA=RUTA ... --registro ETIQUETA=CARPETA ...
       [--generado ETIQUETA=RUTA ...] [--manual ARCHIVO] [--sesion ARCHIVO] --salida JSON
"""
import argparse
import hashlib
import json
import os
import subprocess
import sys
from collections import Counter, OrderedDict
from pathlib import Path

SIN_ABRIR = ("data/experiment/reextraccion_v2/corpus_tanda1/", "data/experiment/tanda1/t2/", "data/experiment/tanda1/t3/",
             "data/experiment/tanda1/t4/", "data/experiment/tanda1/t5/")
CADENA = "data/experiment/controles_tanda1/codigo_de_la_cadena_47c9f1b3_mesa.json"
GRUPOS_DEL_DESPACHO = OrderedDict([
    ("el registro de alcance", ["data/experiment/catalogo_unico/registro_alcance_por_tanda.md"]),
    ("derivar_registro_alcance_r2b.py, sellar_a2.py y candado_mensaje_r2b.json",
     ["data/experiment/catalogo_unico/code/derivar_registro_alcance_r2b.py",
      "data/experiment/alcance_e1/a2/scripts/sellar_a2.py",
      "data/experiment/reextraccion_v2/e1_extractor/candado_mensaje_r2b.json"]),
    ("el prefijo de E1, sus parches y sus reemplazos",
     ["data/experiment/b54_catalogo_v3/code/prompt_v3_b54.py",
      "data/experiment/reextraccion_v2/e1_extractor/prompt_r2b_reemplazos.json",
      "data/experiment/reextraccion_v2/e1_extractor/prompt_r2b_parche_p3b.json",
      "data/experiment/reextraccion_v2/e1_extractor/prompt_r2b_parche_p3c.json"]),
    ("rol_por_to_r2.json y el catálogo",
     ["data/experiment/catalogo_unico/generados_r2/rol_por_to_r2.json",
      "data/experiment/catalogo_unico/catalogo_sujetos_r2.json",
      "data/experiment/catalogo_unico/generados_r2/bloque_catalogo_r2.txt",
      "data/experiment/catalogo_unico/generados_r2/labels_e2_r2.json"]),
])


def par(xs):
    return [tuple(x.split("=", 1)) for x in xs or []]


ap = argparse.ArgumentParser()
ap.add_argument("--repo", required=True)
ap.add_argument("--base", required=True)
ap.add_argument("--raiz", action="append", required=True)
ap.add_argument("--registro", action="append", required=True)
ap.add_argument("--generado", action="append")
ap.add_argument("--manual")
ap.add_argument("--sesion")
ap.add_argument("--salida", required=True)
a = ap.parse_args()
REPO = os.path.realpath(a.repo)
raices = sorted(((e, os.path.realpath(p)) for e, p in par(a.raiz)), key=lambda x: -len(x[1]))
generados = sorted(((e, os.path.realpath(p)) for e, p in par(a.generado)), key=lambda x: -len(x[1]))


def git(*args: str) -> bytes:
    return subprocess.run(["git", "--no-optional-locks", "-C", REPO, *args], capture_output=True, check=True).stdout


rastreados = {}
for reg in git("ls-tree", "-r", "-z", a.base).split(b"\0"):
    if reg:
        meta, ruta = reg.decode("utf-8").split("\t", 1)
        rastreados[ruta] = meta.split()[2]


def es_lectura(modo: str, flags: str) -> bool:
    if modo not in ("None", ""):
        return "r" in modo and "+" not in modo and not any(c in modo for c in "wax")
    try:
        return int(flags) & 3 == 0
    except ValueError:
        return True


lecturas, escrituras_en_copias, en_el_repo, en_salidas_t1 = {}, Counter(), Counter(), Counter()
no_existen, ejemplos_no_existen, raiz_de = Counter(), {}, {}
fuera, carpetas, gen = Counter(), Counter(), Counter()
for etiqueta, carpeta in par(a.registro):
    for log in sorted(Path(carpeta).glob("lecturas_*.tsv")):
        for linea in log.read_text(encoding="utf-8", errors="replace").splitlines():
            ruta, modo, flags = (linea.split("\t") + ["", ""])[:3]
            real = os.path.realpath(ruta)
            lee = es_lectura(modo, flags)
            raiz = next(((e, r) for e, r in raices if real == r or real.startswith(r + "/")), None)
            if raiz is not None:
                rel = os.path.relpath(real, raiz[1])
                if rel.startswith(SIN_ABRIR):
                    en_salidas_t1[(etiqueta, raiz[0])] += 1
                    continue
                if not lee:
                    escrituras_en_copias[(etiqueta, raiz[0], rel)] += 1
                    continue
                if "<" in rel or not os.path.exists(real):
                    clase = ("un .pyc que la copia no tiene" if rel.endswith(".pyc") else
                             "un nombre de compilación" if "<" in rel else
                             "otra ruta que no existe (shutil.rmtree con dir_fd, u otra que no está)")
                    no_existen[clase] += 1
                    ejemplos_no_existen.setdefault(clase, set()).add(rel)
                    continue
                if os.path.isdir(real):
                    carpetas[rel] += 1
                    continue
                lecturas.setdefault(rel, set()).add(f"{etiqueta}:{raiz[0]}")
                raiz_de.setdefault(rel, set()).add(raiz[1])
                continue
            g = next((e for e, r in generados if real == r or real.startswith(r + "/")), None)
            if g is not None:
                gen[(g, "lectura" if lee else "escritura")] += 1
                continue
            if real == REPO or real.startswith(REPO + "/"):
                rel = os.path.relpath(real, REPO)
                if rel.startswith(".venv/") or rel == ".venv":
                    fuera["el intérprete del repo y sus bibliotecas (.venv)"] += 1
                elif rel.startswith(SIN_ABRIR):
                    en_salidas_t1[(etiqueta, "repo")] += 1
                else:
                    en_el_repo[rel] += 1
                continue
            fuera["fuera del repo y de las copias (biblioteca estándar, caches del sistema)"] += 1


def leer_lista(p):
    if not p:
        return []
    return [x.split("\t") for x in Path(p).read_text(encoding="utf-8").splitlines() if x.strip() and not x.startswith("#")]


manual = leer_lista(a.manual)
sesion = leer_lista(a.sesion)
cadena = [r["ruta"] for r in json.loads(git("show", f"{a.base}:{CADENA}"))["rutas"]]
todas = OrderedDict()
for rel in sorted(lecturas):
    todas.setdefault(rel, OrderedDict([("fuentes", sorted(lecturas[rel]))]))
for rel, motivo in manual:
    todas.setdefault(rel, OrderedDict([("fuentes", [])]))["fuentes"].append(f"consola: {motivo}")
for rel, motivo in sesion:
    todas.setdefault(rel, OrderedDict([("fuentes", [])]))["fuentes"].append(f"sesión: {motivo}")
for rel in cadena:
    todas.setdefault(rel, OrderedDict([("fuentes", [])]))["fuentes"].append("las 78 de la cadena")

no_rastreados = []
for rel, d in todas.items():
    d["rastreado"] = rel in rastreados
    if rel in rastreados:
        b = git("show", f"{a.base}:{rel}")
        d["sha256_base"] = hashlib.sha256(b).hexdigest()
        p = Path(REPO) / rel
        hoy = hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else None
        d["sha256_en_el_repo_al_armar_la_lista"] = hoy
        d["igual_a_la_base_al_armar_la_lista"] = hoy == d["sha256_base"]
    else:
        d["sha256_base"] = None
        d["nota"] = ("PDF sin rastrear (.gitignore): su sha256 se controla contra manifest_pdfs.sha256 o INFORME_E0.md"
                     if rel.endswith(".pdf") else "NO RASTREADO")
        if not rel.endswith(".pdf"):
            no_rastreados.append(rel)
            d["sha256_en_las_copias"] = OrderedDict(
                (os.path.basename(r), hashlib.sha256((Path(r) / rel).read_bytes()).hexdigest())
                for r in sorted(raiz_de.get(rel, ())))
grupos = OrderedDict((g, OrderedDict((r, r in todas and any(not f.startswith("las 78") for f in todas[r]["fuentes"]))
                                     for r in rs)) for g, rs in GRUPOS_DEL_DESPACHO.items())
res = OrderedDict([
    ("base", a.base), ("repo_head_al_armar_la_lista", git("rev-parse", "HEAD").decode().strip()),
    ("archivos", len(todas)),
    ("rastreados", sum(d["rastreado"] for d in todas.values())),
    ("pdfs_sin_rastrear", sum(r.endswith(".pdf") and not d["rastreado"] for r, d in todas.items())),
    ("no_rastreados_que_no_son_pdf", no_rastreados),
    ("intentos_sobre_rutas_que_no_existen", OrderedDict(
        (k, OrderedDict([("eventos", v), ("rutas", len(ejemplos_no_existen[k])),
                         ("ejemplos", sorted(ejemplos_no_existen[k])[:5])])) for k, v in sorted(no_existen.items()))),
    ("rastreados_distintos_de_la_base_al_armar_la_lista",
     [r for r, d in todas.items() if d["rastreado"] and not d["igual_a_la_base_al_armar_la_lista"]]),
    # Para el control del commit: las entradas de los valores (lo que abrió un proceso, lo que leyó la consola y las 78
    # rutas de la cadena); lo leído solo en la sesión, para entender el trabajo, no entra (registro de decisiones, §36).
    ("entradas_de_los_valores", sum(any(not f.startswith("sesión") for f in d["fuentes"]) for d in todas.values())),
    ("leidos_solo_en_la_sesion", sum(all(f.startswith("sesión") for f in d["fuentes"]) for d in todas.values())),
    ("entradas_de_los_valores_rastreadas_distintas_de_la_base_al_armar_la_lista",
     [r for r, d in todas.items() if d["rastreado"] and not d["igual_a_la_base_al_armar_la_lista"]
      and any(not f.startswith("sesión") for f in d["fuentes"])]),
    ("grupos_del_despacho_leidos", grupos),
    ("bases_de_la_cache_abiertas", OrderedDict((r, d["fuentes"]) for r, d in todas.items() if r.endswith(".db"))),
    ("carpetas_abiertas_para_listar", len(carpetas)),
    ("aperturas_de_archivos_generados_por_a3", {f"{g} ({k})": v for (g, k), v in sorted(gen.items())}),
    ("aperturas_fuera", dict(fuera)),
    ("aperturas_en_el_repo_fuera_del_venv", dict(en_el_repo)),
    ("aperturas_en_carpetas_de_salidas_de_la_tanda_1", {f"{e} en {r}": v for (e, r), v in sorted(en_salidas_t1.items())}),
    ("escrituras_dentro_de_las_copias", [list(k) + [v] for k, v in sorted(escrituras_en_copias.items())]),
    ("lista", todas)])
Path(a.salida).write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in res.items() if k != "lista"}, ensure_ascii=False, indent=1))
sys.exit(0 if not en_el_repo and not en_salidas_t1 and not escrituras_en_copias else 1)
