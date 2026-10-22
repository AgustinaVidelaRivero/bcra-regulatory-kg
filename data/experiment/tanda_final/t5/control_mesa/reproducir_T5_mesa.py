"""Mesa, §237 (22/10/2026): reproduce T5 de la tanda final sobre una copia del repo, sin imprimir ninguna cifra: corre de nuevo, en el
orden de T5, los diez scripts de t5/scripts/ que dan sus salidas y compara cada salida y cada consola con la del repo (igual o distinto).
USD 0, sin API ni Neo4j, sin escribir en el repo: todo corre sobre <copia> (rsync sin .git, .env, NO_ABRIR_ ni la carpeta de la
clasificación) y escribe en una carpeta temporal. Lo único del repo que se lee de otro modo es git: el grafos.py de HEAD (el de antes de
T5) con git show, y el clon desnudo <git> para el git show de la tanda 1 del script de cifras (GIT_DIR). Los NO_ABRIR_ que se rearman no
se abren: se comparan por sha256 con el del repo, que tampoco se abre.
  1. editar_grafos_t5.py, sobre la copia con el grafos.py de HEAD y sin la vista: el grafos.py y la vista que da, contra los del repo.
  2. ids_modelo_t5.py; 3. entrada_acumulado_60_t5.py; 4. contado_tramo1_t5.py (desde la raíz de la copia); 5. carpetas_tramo1_t5.py;
  6. control_registro_tramo1_t5.py, con el grafos.py de HEAD como original; 7. cifras_t5_tf.py, dos veces, a dos salidas;
  8. columnas_tablero_t5.py; 9. reporte_t5_tf.py; 10. no_abrir_t5.py, con los dos NO_ABRIR_ de 2 y 4.
Los scripts corren con <python> (el del .venv del repo, que trae el paquete neo4j que importa la carga; con -I -B no escribe nada).
Uso: python3 -I -B reproducir_T5_mesa.py <repo> <copia> <git desnudo> <salida.json> <python>"""
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO, C, GD, OUT, PY = Path(sys.argv[1]), Path(sys.argv[2]).resolve(), Path(sys.argv[3]).resolve(), Path(sys.argv[4]), sys.argv[5]
T5 = "data/experiment/tanda_final/t5"
SC = C / T5 / "scripts"
GP = "data/experiment/neo4j/grafos.py"
VISTA = f"{T5}/registro_vista_r2b_tramo1.py"
sha = lambda b: hashlib.sha256(b).hexdigest()  # noqa: E731
git = lambda *a: subprocess.run(["git", "--no-optional-locks", "-C", str(REPO), *a], capture_output=True, check=True).stdout  # noqa: E731
res = {}


def foto():
    return sha(git("rev-parse", "HEAD") + git("status", "--porcelain=v1", "-uall") + git("diff") + git("diff", "--cached"))


def correr(nombre, *a, env=None):
    p = subprocess.run([PY, "-I", "-B", str(SC / nombre), *map(str, a)], capture_output=True, cwd=C, env=env)
    if p.returncode:
        print("MAL", nombre, "rc", p.returncode, p.stderr.decode(errors="replace").strip().splitlines()[-1][:200])
    return p.returncode, p.stdout


def igual(clave, a, ruta_repo):
    res[clave] = a is not None and a == (REPO / ruta_repo).read_bytes()


def lee(p: Path):
    return p.read_bytes() if p.exists() else None


antes = foto()
assert not (C / ".git").exists()
with tempfile.TemporaryDirectory(prefix="t5_mesa_") as t:
    T = Path(t)
    # 1. el editor, desde el grafos.py de HEAD y sin la vista
    g_head = git("show", f"HEAD:{GP}")
    res["grafos_py_de_HEAD_es_el_de_antes_de_T5"] = sha(g_head) == "89aaaaca7f7e550c0837cfa5f3d2189bebf8d9a724ba4f2a851ce7bee5361c22"
    (T / "grafos_HEAD.py").write_bytes(g_head)
    (C / GP).write_bytes(g_head)
    (C / VISTA).unlink()
    rc, so = correr("editar_grafos_t5.py", C)
    res["1_editar_rc_0"] = rc == 0
    igual("1_grafos_py_igual_al_del_repo", lee(C / GP), GP)
    igual("1_vista_igual_a_la_del_repo", lee(C / VISTA), VISTA)
    igual("1_consola_igual", so, f"{T5}/salidas/consola_editar_grafos_t5.txt")
    # 2. los ids de modelo
    rc, so = correr("ids_modelo_t5.py", C, T / "trabajo_ids", T / "ids.json", T / "NO_ABRIR_ids.json")
    res["2_ids_rc_0"] = rc == 0
    igual("2_ids_modelo_igual", lee(T / "ids.json"), f"{T5}/salidas/ids_modelo_t5.json")
    # 3. la entrada del acumulado de 60
    rc, so = correr("entrada_acumulado_60_t5.py", C, T / "entrada.json")
    res["3_entrada_rc_0"] = rc == 0
    igual("3_entrada_acumulado_60_igual", lee(T / "entrada.json"), f"{T5}/salidas/entrada_acumulado_60_t5.json")
    # 4. lo contado del tramo 1
    rc, so = correr("contado_tramo1_t5.py", C, T / "contado_tramo1_t5.json", T / "NO_ABRIR_contado_tramo1_t5.json")
    res["4_contado_rc_0"] = rc == 0
    igual("4_contado_tramo1_igual", lee(T / "contado_tramo1_t5.json"), f"{T5}/salidas/contado_tramo1_t5.json")
    igual("4_consola_igual", so, f"{T5}/salidas/consola_contado_tramo1_t5.txt")
    # 5. las carpetas del tramo 1
    rc, so = correr("carpetas_tramo1_t5.py", C, T / "carpetas.json")
    res["5_carpetas_rc_0"] = rc == 0
    igual("5_carpetas_tramo1_igual", lee(T / "carpetas.json"), f"{T5}/salidas/carpetas_tramo1_t5.json")
    # 6. el control del registro
    rc, so = correr("control_registro_tramo1_t5.py", C, T / "grafos_HEAD.py", "--out", T / "control.json")
    res["6_control_rc_0"] = rc == 0
    igual("6_control_registro_igual", lee(T / "control.json"), f"{T5}/salidas/control_registro_tramo1_t5.json")
    igual("6_consola_igual", so, f"{T5}/salidas/consola_control_registro_tramo1_t5.txt")
    # 7. las cifras, dos veces
    env = {"PATH": os.environ["PATH"], "HOME": os.environ["HOME"], "GIT_DIR": str(GD), "PYTHONDONTWRITEBYTECODE": "1"}
    for k in ("a", "b"):
        (T / f"cifras_{k}").mkdir()
        rc, so = correr("cifras_t5_tf.py", C, T / f"cifras_{k}", env=env)
        res[f"7{k}_cifras_rc_0"] = rc == 0
        igual(f"7{k}_cifras_t5_igual", lee(T / f"cifras_{k}/cifras_t5.json"), f"{T5}/salidas/cifras_t5.json")
    # 8 y 9. las columnas y el reporte, en la copia
    for n in ("columna_tanda_final_tablero_PROPUESTA.md", "columna_tramo1_tablero_PROPUESTA.md", "reporte_tanda_final.md",
              "propuestas_backlog_t5.jsonl"):
        (C / T5 / n).unlink()
    rc, so = correr("columnas_tablero_t5.py", C)
    res["8_columnas_rc_0"] = rc == 0
    for n in ("columna_tanda_final_tablero_PROPUESTA.md", "columna_tramo1_tablero_PROPUESTA.md"):
        igual(f"8_{n}_igual", lee(C / T5 / n), f"{T5}/{n}")
    igual("8_consola_igual", so, f"{T5}/salidas/consola_columnas_tablero_t5.txt")
    rc, so = correr("reporte_t5_tf.py", C)
    res["9_reporte_rc_0"] = rc == 0
    for n in ("reporte_tanda_final.md", "propuestas_backlog_t5.jsonl"):
        igual(f"9_{n}_igual", lee(C / T5 / n), f"{T5}/{n}")
    igual("9_consola_igual", so, f"{T5}/salidas/consola_reporte_t5.txt")
    # 10. el NO_ABRIR_ de T5, por sha256
    rc, so = correr("no_abrir_t5.py", T / "NO_ABRIR_contado_tramo1_t5.json", T / "NO_ABRIR_ids.json", T / "NO_ABRIR_conteos_t5.json")
    res["10_no_abrir_rc_0"] = rc == 0
    res["10_no_abrir_mismo_sha256_que_el_del_repo"] = rc == 0 and sha((T / "NO_ABRIR_conteos_t5.json").read_bytes()) == sha(
        (REPO / T5 / "NO_ABRIR_conteos_t5.json").read_bytes())
res["repo_sin_cambios"] = foto() == antes
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for k, x in res.items():
    print("OK " if x else "MAL", k)
sys.exit(0 if all(res.values()) else 1)
