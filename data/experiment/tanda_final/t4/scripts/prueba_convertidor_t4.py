"""B6.1, tanda final, T4, primer tramo (punto 6 del «seguí»): la prueba del convertidor, con exportaciones de juguete armadas fuera del
repo. Copia (sin enlaces) la carpeta t4/lectura_autora/ del repo a <dir de prueba>/lectura_autora/ y, en otra carpeta, una copia con una
planilla alterada; arma ahí las exportaciones, corre el convertidor de la copia desde su carpeta, como dice el LEEME
(`python3 -I convertir_lectura_T4.py <muestra> <exportación.csv>`), y controla para cada caso el código de salida, lo que escribe y lo
que dice. Toma el sha256 de cada archivo de t4/lectura_autora/ del repo antes y después: tienen que ser iguales.
Los veredictos de juguete son las propuestas, salvo los cambios que cada caso declara; no son una lectura.
Uso: python3 -I -B prueba_convertidor_t4.py <repo> <dir de prueba, vacío o inexistente> <salida.json>
"""
import csv
import hashlib
import io
import json
import shutil
import subprocess
import sys
from pathlib import Path

R, P, OUT = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve(), Path(sys.argv[3])
LU = R / "data/experiment/tanda_final/t4/lectura_autora"
if P.exists() and any(P.iterdir()):
    raise SystemExit("el dir de prueba no está vacío")
if R in P.parents or P == R:
    raise SystemExit("el dir de prueba no puede estar dentro del repo")
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()  # noqa: E731
antes = {p.name: sha(p) for p in sorted(LU.iterdir()) if p.is_file()}
C, C2 = P / "lectura_autora", P / "lectura_autora_planilla_alterada"
shutil.copytree(LU, C, symlinks=False)
shutil.copytree(LU, C2, symlinks=False)
enlaces = [str(x) for x in P.rglob("*") if x.is_symlink()]
copia_igual = {p.name: sha(p) for p in sorted(C.iterdir()) if p.is_file()} == antes


def leer(m: str, d: Path = C) -> list:
    return list(csv.reader(io.StringIO((d / f"{m}.csv").read_text(encoding="utf-8"), newline=""), delimiter=";"))


def exportar(nombre: str, filas: list, sep: str = ";", bom: bool = False, fin: str = "\n", d: Path = C) -> Path:
    buf = io.StringIO()
    csv.writer(buf, delimiter=sep, lineterminator=fin).writerows(filas)
    p = d / nombre
    p.write_bytes((("﻿" if bom else "") + buf.getvalue()).encode("utf-8"))
    return p


def correr(m: str, exp: str, d: Path = C) -> dict:
    r = subprocess.run(["python3", "-I", "convertir_lectura_T4.py", m, exp], cwd=d, capture_output=True, text=True)
    return {"rc": r.returncode, "salida": (r.stdout + r.stderr).strip().splitlines()}


def con_veredictos(m: str, cambios: dict | None = None) -> list:
    f = [list(x) for x in leer(m)]
    for x in f[1:]:
        x[5] = x[3]
    for i, (v, nota) in (cambios or {}).items():
        f[i][5], f[i][6] = v, nota
    return f


casos = []


def caso(nombre: str, espera_rc: int, espera_texto: str, r: dict, marcada: Path | None = None, debe_existir: bool | None = None,
         extra: dict | None = None) -> None:
    ok = r["rc"] == espera_rc and any(espera_texto in x for x in r["salida"])
    if marcada is not None and debe_existir is not None:
        ok = ok and marcada.exists() == debe_existir
    casos.append({"caso": nombre, "rc": r["rc"], "espera_rc": espera_rc, "espera_texto": espera_texto, "salida": r["salida"], "ok": ok,
                  **(extra or {})})


# 1. Válida: cola, con BOM y «;», tres cambios con su nota.
m = "cola"
exportar("cola_exportada.csv", con_veredictos(m, {1: ("con error", "nota de juguete"), 2: ("dudosa", "nota de juguete"),
                                                  12: ("sin error", "nota de juguete")}), bom=True)
r = correr(m, "cola_exportada.csv")
marc = C / "cola_marcada.csv"
fil = list(csv.reader(io.StringIO(marc.read_text(encoding="utf-8"), newline=""), delimiter=";")) if marc.exists() else []
plan = leer(m)
caso("1. válida (cola, BOM, «;», 3 cambios con nota)", 0, "OK: cola_marcada.csv", r, marc, True,
     {"marcada_sha256": sha(marc) if marc.exists() else None,
      "marcada_columnas_1_a_5_iguales_a_la_planilla": [x[:5] for x in fil] == [x[:5] for x in plan],
      "marcada_veredictos": [x[5] for x in fil[1:4]], "marcada_cambian": sum(1 for x in fil[1:] if x[5] != x[3])})
# 2. La misma otra vez: no pisa la marcada.
sha_marc = sha(marc)
r = correr(m, "cola_exportada.csv")
caso("2. otra vez la misma: no pisa la marcada", 1, "ya existe: no la piso", r, extra={"marcada_sin_cambios": sha(marc) == sha_marc})
# 3. Válida con «,», CRLF y una fila vacía al final (como puede exportar Numbers): aceptadas_items.
m = "aceptadas_items"
f = con_veredictos(m) + [[""] * 7]
exportar("aceptadas_items_exportada.csv", f, sep=",", fin="\r\n")
r = correr(m, "aceptadas_items_exportada.csv")
caso("3. válida (aceptadas_items, «,», CRLF y fila vacía al final)", 0, "saqué una fila vacía al final", r,
     C / "aceptadas_items_marcada.csv", True)
# 4. Respuestas que no cierran: una mal escrita, una vacía y un cambio sin nota (vigilancia_2).
m = "vigilancia_2"
f = con_veredictos(m)
f[1][5] = "vaciamento"
f[2][5] = ""
f[3][5] = "vaciamiento" if f[3][3] != "vaciamiento" else "no vaciamiento"
f[3][6] = ""
exportar("vigilancia_2_exportada.csv", f)
r = correr(m, "vigilancia_2_exportada.csv")
caso("4. respuesta mal escrita, vacía y cambio sin nota", 1, "3 PROBLEMA(S)", r, C / "vigilancia_2_marcada.csv", False)
# 5. Filas en otro orden (vigilancia_1).
m = "vigilancia_1"
f = con_veredictos(m)
f[1], f[2] = f[2], f[1]
exportar("vigilancia_1_exportada.csv", f)
r = correr(m, "vigilancia_1_exportada.csv")
caso("5. dos filas en otro orden", 1, "no son los de la planilla", r, C / "vigilancia_1_marcada.csv", False)
# 6. Una columna de más con texto (vigilancia_3).
m = "vigilancia_3"
f = [x + ["extra"] for x in con_veredictos(m)]
exportar("vigilancia_3_exportada.csv", f)
r = correr(m, "vigilancia_3_exportada.csv")
caso("6. columna de más con texto", 1, "columnas de más", r, C / "vigilancia_3_marcada.csv", False)
# 7. Una fila de menos (vigilancia_7).
m = "vigilancia_7"
exportar("vigilancia_7_exportada.csv", con_veredictos(m)[:-1])
r = correr(m, "vigilancia_7_exportada.csv")
caso("7. una fila de menos", 1, "filas de datos", r, C / "vigilancia_7_marcada.csv", False)
# 8. La (12): «incorrecta» sin capa no vale; «incorrecta (E1-prompt)» con nota sí (dos corridas).
m = "observacion_12"
f = con_veredictos(m)
i = next(k for k in range(1, len(f)) if f[k][3] == "correcta")
f[i][5], f[i][6] = "incorrecta", "nota de juguete"
exportar("observacion_12_exportada.csv", f)
r = correr(m, "observacion_12_exportada.csv")
caso("8a. (12): «incorrecta» sin capa", 1, "no es una de", r, C / "observacion_12_marcada.csv", False)
f[i][5] = "incorrecta (E1-prompt)"
exportar("observacion_12_exportada_2.csv", f)
r = correr(m, "observacion_12_exportada_2.csv")
caso("8b. (12): «incorrecta (E1-prompt)» con nota", 0, "OK: observacion_12_marcada.csv", r, C / "observacion_12_marcada.csv", True)
# 9. Una muestra que no existe.
r = correr("aceptadas", "cola_exportada.csv")
caso("9. muestra que no existe", 1, "no es una de", r)
# 10. La exportación es la planilla misma.
r = correr("aceptadas_no_items", "aceptadas_no_items.csv")
caso("10. la exportación es la planilla", 1, "no puede ser la planilla", r, C / "aceptadas_no_items_marcada.csv", False)
# 11. Planilla alterada (otro sha256), en la otra copia.
m = "aceptadas_no_items"
t = (C2 / f"{m}.csv").read_text(encoding="utf-8")
(C2 / f"{m}.csv").write_text(t.replace("sin error", "sin  error", 1), encoding="utf-8")
f = [list(x) for x in leer(m, C2)]
for x in f[1:]:
    x[5] = x[3]
exportar("aceptadas_no_items_exportada.csv", f, d=C2)
r = correr(m, "aceptadas_no_items_exportada.csv", d=C2)
caso("11. planilla alterada (sha256 distinto)", 1, "sha256 distinto", r, C2 / f"{m}_marcada.csv", False)
despues = {p.name: sha(p) for p in sorted(LU.iterdir()) if p.is_file()}
res = {"repo_lectura_autora_antes": antes, "repo_lectura_autora_despues": despues, "repo_sin_cambios": antes == despues,
       "copia_igual_al_repo_antes_de_probar": copia_igual, "enlaces_en_la_copia": enlaces, "casos": casos,
       "todos_ok": all(c["ok"] for c in casos) and antes == despues and copia_igual and not enlaces,
       "python3": subprocess.run(["python3", "--version"], capture_output=True, text=True).stdout.strip()}
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for c in casos:
    print(("ok  " if c["ok"] else "MAL ") + c["caso"] + f" | rc={c['rc']} | " + " / ".join(c["salida"])[:300])
print("repo sin cambios:", antes == despues, "| copia igual:", copia_igual, "| enlaces:", len(enlaces), "| todos ok:", res["todos_ok"])
sys.exit(0 if res["todos_ok"] else 1)
