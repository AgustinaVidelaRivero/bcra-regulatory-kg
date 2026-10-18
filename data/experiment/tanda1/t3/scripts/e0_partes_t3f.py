"""B6.1, tanda 1, T3 (desde el punto 4, con la decisión 1 de la autora del 18/10/2026): la E0 con las partes por corte, que rige para
S31, rearmada fuera del repo y controlada. Corre sobre una COPIA del repo (nunca el repo); escribe en <trabajo>.

  1. La entrada del acumulado no está en el repo (FRENO T3 parcial, sección 5): se rearma en la copia con armar_acumulado_t3.py, después
     de mover aparte, a <trabajo>/acumulado_aparte/, lo que ese script escribe y la copia ya trae del repo (el manifiesto de extracción,
     la E0 combinada y armado_acumulado_t3.json). Control: lo rearmado es byte a byte lo del repo.
  2. reext_t0/t3/e0_con_partes.py, sin cambios, dos veces por E0, cada una en un proceso aparte:
       tanda1:    E0 reextraccion_v2/e0_chunking/salida_tanda1_r2b, salida reextraccion_v2/corpus_tanda1/salida_r2b;
       acumulado: E0 tanda1/t3/acumulado/e0_acumulado_r2b, salida tanda1/t3/acumulado/entrada_acumulado_r2b.
     Control: las dos corridas, byte a byte iguales. El sha256 de cada archivo y el del conjunto (sha256 de las líneas «sha256  nombre»,
     ordenadas por nombre, con salto de línea final).
  3. El control de shapes: scripts/gate_t3.sh shapes con la primera corrida de cada E0, sobre los cuatro grafos; la salida (.md, .json y la
     consola) se compara con la del FRENO parcial (tanda1/t3/gate/shapes_con_e0_con_partes/<grafo>/), byte a byte o igual con las rutas
     normalizadas (la copia, la E0 y la carpeta personal por un marcador) y la fecha de la corrida normalizada: la línea «- **Fecha:** …»
     del .md y el campo "fecha" del .json, nada más (indicación de la autora del 18/10/2026, con el control a la vista). Se guarda el
     diff crudo de cada archivo, antes de normalizar, con el scratchpad escrito <SCRATCHPAD> y la carpeta personal $HOME; cualquier otra
     diferencia es FRENO.
Uso: python3 -I -B e0_partes_t3f.py <python del repo> <copia> <trabajo> <salida.json>
"""
import difflib
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

PY, C, W, OUT = sys.argv[1], Path(sys.argv[2]).resolve(), Path(sys.argv[3]).resolve(), Path(sys.argv[4])
X = "data/experiment/reextraccion_v2"
A = "data/experiment/tanda1/t3/acumulado"
T3 = "data/experiment/tanda1/t3"
E0S = {"tanda1": (f"{X}/e0_chunking/salida_tanda1_r2b", f"{X}/corpus_tanda1/salida_r2b"),
       "acumulado": (f"{A}/e0_acumulado_r2b", f"{A}/entrada_acumulado_r2b")}
GRAFOS = {"ens_veinte_r2b": (f"{X}/corpus_tanda1/ens_veinte_r2b", "tanda1"),
          "ens_veinte_r2b_sincola": (f"{X}/corpus_tanda1/ens_veinte_r2b_sincola", "tanda1"),
          "ens_treinta_r2b": (f"{A}/ens_treinta_r2b", "acumulado"),
          "ens_treinta_r2b_sincola": (f"{A}/ens_treinta_r2b_sincola", "acumulado")}
E0_DE_AYER = {"tanda1": "<SCRATCHPAD>/t3/e0_tanda1_r2b_con_partes", "acumulado": "<SCRATCHPAD>/t3/e0_acumulado_r2b_con_partes"}


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def archivos(d: Path) -> dict:
    return {p.relative_to(d).as_posix(): sha(p.read_bytes()) for p in sorted(d.rglob("*")) if p.is_file()}


def conjunto(fs: dict) -> str:
    return sha("".join(f"{h}  {n}\n" for n, h in sorted(fs.items())).encode())


res = {"copia": "<COPIA>", "acumulado": {}, "e0_con_partes": {}, "shapes": {}}
if W.exists() and any(W.iterdir()):
    raise SystemExit(f"FRENO: {W} no está vacío")
W.mkdir(parents=True, exist_ok=True)

# 1. la entrada del acumulado
aparte = W / "acumulado_aparte"
aparte.mkdir()
mov = [f"{A}/manifiestos/acumulado_30tos_r2b.json", f"{A}/e0_acumulado_r2b", f"{A}/armado_acumulado_t3.json"]
if (C / A / "entrada_acumulado_r2b").exists():
    raise SystemExit("FRENO: la copia ya tiene la entrada del acumulado")
for rel in mov:
    shutil.move(str(C / rel), str(aparte / Path(rel).name))
p = subprocess.run([PY, "-I", "-B", str(C / T3 / "scripts/armar_acumulado_t3.py"), str(C)], capture_output=True, text=True)
res["acumulado"]["armar_rc"] = p.returncode
res["acumulado"]["armar_salida"] = p.stdout.strip()
iguales = {}
for rel in mov:
    a, b = C / rel, aparte / Path(rel).name
    if a.is_dir():
        fa, fb = archivos(a), archivos(b)
        iguales[rel] = {"archivos": len(fa), "iguales": fa == fb}
    else:
        iguales[rel] = {"iguales": a.read_bytes() == b.read_bytes()}
res["acumulado"]["rearmado_igual_al_repo"] = iguales
ent = C / A / "entrada_acumulado_r2b"
res["acumulado"]["entrada"] = {"archivos": len(archivos(ent)), "bytes": sum(q.stat().st_size for q in ent.rglob("*") if q.is_file())}
if p.returncode != 0 or not all(v["iguales"] for v in iguales.values()):
    OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    raise SystemExit("FRENO: el acumulado rearmado no es el del repo")

# 2. la E0 con las partes, dos veces
for nombre, (e0, sal) in E0S.items():
    corr = []
    for k in (1, 2):
        dest = W / "e0_con_partes" / f"{nombre}_corrida{k}"
        dest.parent.mkdir(parents=True, exist_ok=True)
        q = subprocess.run([PY, "-I", "-B", str(C / "data/experiment/reext_t0/t3/e0_con_partes.py"), str(C / e0), str(C / sal), str(dest)],
                           capture_output=True, text=True)
        (W / "e0_con_partes" / f"consola_{nombre}_corrida{k}.txt").write_text(q.stdout + q.stderr + f"rc={q.returncode}\n", encoding="utf-8")
        fs = archivos(dest)
        corr.append({"rc": q.returncode, "reemplazos": json.loads(q.stdout)["reemplazos"] if q.returncode == 0 else None,
                     "archivos": len(fs), "sha256_conjunto": conjunto(fs), "sha256_por_archivo": fs})
    res["e0_con_partes"][nombre] = {"e0": e0, "salida": sal, "corridas": [{k: v for k, v in c.items() if k != "sha256_por_archivo"} for c in corr],
                                    "iguales": corr[0]["sha256_por_archivo"] == corr[1]["sha256_por_archivo"],
                                    "sha256_conjunto": corr[0]["sha256_conjunto"],
                                    "sha256_por_archivo": corr[0]["sha256_por_archivo"]}

# 3. el control de shapes
home = str(Path.home())
SCR = str(W.parent.parent)                                 # <trabajo> es <scratchpad>/t3f/<algo>
FECHA_MD = re.compile(r"^- \*\*Fecha:\*\* \d{4}-\d{2}-\d{2}$", re.M)
FECHA_JSON = re.compile(r'^  "fecha": "\d{4}-\d{2}-\d{2}",$', re.M)


def visible(t: str) -> str:
    return t.replace(SCR, "<SCRATCHPAD>").replace(home, "$HOME")


def normal(b: bytes, e0_hoy: str, e0_ayer: str) -> bytes:
    t = b.decode("utf-8")
    t = t.replace(e0_hoy, "<E0>").replace(e0_ayer, "<E0>").replace(str(C), "<COPIA>").replace("<SCRATCHPAD>/t3/copia_t3", "<COPIA>")
    t = FECHA_MD.sub("- **Fecha:** <FECHA>", t)
    t = FECHA_JSON.sub('  "fecha": "<FECHA>",', t)
    return t.replace(home, "$HOME").encode("utf-8")


for g, (ens, cual) in GRAFOS.items():
    e0 = W / "e0_con_partes" / f"{cual}_corrida1"
    o = W / "shapes_con_partes" / g
    q = subprocess.run(["bash", str(C / T3 / "scripts/gate_t3.sh"), PY, str(C), ens, str(e0), str(o), "shapes"], capture_output=True, text=True)
    ayer = C / T3 / "gate/shapes_con_e0_con_partes" / g
    comp = {}
    for n in ("shapes_perfil_r2_fase_r2b.md", "shapes_perfil_r2_fase_r2b.json", "consola_shapes.txt"):
        hoy_b, ayer_b = (o / n).read_bytes(), (ayer / n).read_bytes()
        crudo = list(difflib.unified_diff(visible(ayer_b.decode("utf-8")).splitlines(), visible(hoy_b.decode("utf-8")).splitlines(),
                                          f"parcial/{g}/{n}", f"hoy/{g}/{n}", lineterm="", n=0))
        (o / f"diff_crudo_{n}.txt").write_text("\n".join(crudo) + ("\n" if crudo else ""), encoding="utf-8")
        na, nh = normal(ayer_b, str(e0), E0_DE_AYER[cual]).decode("utf-8"), normal(hoy_b, str(e0), E0_DE_AYER[cual]).decode("utf-8")
        resto = [x for x in difflib.unified_diff(na.splitlines(), nh.splitlines(), lineterm="", n=0)
                 if x[:1] in "+-" and not x.startswith(("+++", "---"))]
        comp[n] = {"byte_a_byte": hoy_b == ayer_b, "lineas_distintas_en_el_diff_crudo": sum(1 for x in crudo if x[:1] in "+-" and not
                                                                                            x.startswith(("+++", "---"))),
                   "igual_con_las_rutas_y_la_fecha_normalizadas": not resto, "distintas_despues_de_normalizar": resto}
    sh = json.loads((o / "shapes_perfil_r2_fase_r2b.json").read_text(encoding="utf-8"))
    res["shapes"][g] = {"rc_gate": q.returncode, "comparacion_con_el_parcial": comp,
                        "control": all(v["byte_a_byte"] or v["igual_con_las_rutas_y_la_fecha_normalizadas"] for v in comp.values())}
res["ok"] = (all(v["iguales"] for v in res["e0_con_partes"].values()) and all(v["control"] for v in res["shapes"].values()))
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for n, v in res["e0_con_partes"].items():
    print(f"E0 con partes {n}: {v['corridas'][0]['archivos']} archivos, dos corridas iguales: {v['iguales']}, conjunto {v['sha256_conjunto']}")
for g, v in res["shapes"].items():
    print(f"shapes {g}: " + "; ".join(f"{n}: byte a byte {c['byte_a_byte']}, crudo {c['lineas_distintas_en_el_diff_crudo']} líneas, "
                                      f"normalizado igual {c['igual_con_las_rutas_y_la_fecha_normalizadas']}"
                                      for n, c in v["comparacion_con_el_parcial"].items()) + f" → control {v['control']}")
print("acumulado rearmado igual al repo:", res["acumulado"]["rearmado_igual_al_repo"], "| entrada:", res["acumulado"]["entrada"])
print("OK" if res["ok"] else "FRENO")
sys.exit(0 if res["ok"] else 1)
