"""Mesa, §227 (21/10/2026): prueba el convertidor de la ampliación de T4 (convertir_lectura_T4_ampliacion.py, del paquete de la mesa)
en carpetas temporales, con exportaciones de juguete armadas desde la planilla en blanco. No imprime ninguna fila, propuesta ni cuenta:
solo si cada caso termina como debe. USD 0, sin escribir en el repo.
Uso: python3 -I -B probar_convertidor_ampliacion_mesa.py <convertidor> <planilla en blanco del repo> <salida.json>"""
import csv
import io
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

CONV, PL, OUT = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
filas = list(csv.reader(io.StringIO(PL.read_text(encoding="utf-8"), newline=""), delimiter=";"))
otra = {"con error": "sin error", "sin error": "con error", "dudosa": "sin error"}
res = {}


def caso(nombre, editar, rc_esperado, con_marcada_previa=False, planilla_cambiada=False):
    with tempfile.TemporaryDirectory(prefix="conv_ampl_mesa_") as t:
        T = Path(t)
        shutil.copy2(CONV, T / CONV.name)
        shutil.copy2(PL, T / PL.name)
        if planilla_cambiada:
            (T / PL.name).write_bytes((T / PL.name).read_bytes() + b"\n")
        if con_marcada_previa:
            (T / "aceptadas_no_items_ampliacion_marcada.csv").write_text("x\n", encoding="utf-8")
        f = [list(r) for r in filas]
        for r in f[1:]:
            r[5], r[6] = r[3], ""
        editar(f)
        buf = io.StringIO()
        csv.writer(buf, delimiter=";", lineterminator="\n").writerows(f)
        (T / "exportada.csv").write_bytes(b"\xef\xbb\xbf" + buf.getvalue().encode("utf-8"))
        p = subprocess.run([sys.executable, "-I", "-B", CONV.name, "aceptadas_no_items_ampliacion", "exportada.csv"], cwd=t,
                           capture_output=True, text=True)
        m = T / "aceptadas_no_items_ampliacion_marcada.csv"
        bien = p.returncode == rc_esperado
        if rc_esperado == 0:
            mk = list(csv.reader(io.StringIO(m.read_text(encoding="utf-8"), newline=""), delimiter=";"))
            bien = bien and [r[:5] for r in mk] == [r[:5] for r in filas] and all(r[5] == e[5] and r[6] == e[6] for r, e in zip(mk[1:], f[1:]))
        else:
            bien = bien and (not m.exists() or con_marcada_previa) and ("FRENO" in p.stdout or "PROBLEMA" in p.stdout)
        res[nombre] = bien


caso("la propuesta en cada fila, con BOM y «;»: escribe la marcada, igual a la planilla con el veredicto", lambda f: None, 0)
caso("un veredicto cambiado con su razón: escribe la marcada", lambda f: (f[1].__setitem__(5, otra[f[1][3]]), f[1].__setitem__(6, "razón")), 0)
caso("un veredicto cambiado sin razón: frena sin escribir", lambda f: f[1].__setitem__(5, otra[f[1][3]]), 1)
caso("un veredicto que no es una respuesta válida: frena", lambda f: f[2].__setitem__(5, "correcta"), 1)
caso("un veredicto vacío: frena", lambda f: f[3].__setitem__(5, ""), 1)
caso("dos filas cambiadas de lugar: frena", lambda f: f.__setitem__(slice(1, 3), [f[2], f[1]]), 1)
caso("una fila de menos: frena", lambda f: f.pop(), 1)
caso("una planilla con otro sha256: frena", lambda f: None, 1, planilla_cambiada=True)
caso("una marcada que ya existe: no la pisa", lambda f: None, 1, con_marcada_previa=True)
res["la planilla: 30 filas de datos y las 7 columnas"] = len(filas) == 31 and all(len(r) == 7 for r in filas)
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for k, v in res.items():
    print("OK " if v else "MAL", k)
sys.exit(0 if all(res.values()) else 1)
