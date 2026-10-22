"""Mesa, §237 (22/10/2026): el control por fecha de la autora sobre las carpetas de salida de la tanda final, reproducido por código, para el
sello del tramo 1 (enmienda 9 al protocolo entre tandas, §1, punto 6: el sha256 de las carpetas del tramo 1 al cerrarlo no se tomó, se
declara). Solo lee el repo: stat de cada archivo (sin seguir enlaces y sin abrir ninguno) y git con --no-optional-locks. No escribe nombres
de archivos ni cuántos tiene cada carpeta.
  1. En reextraccion_v2/corpus_tanda_final/salida_r2b/<TO>/, la hora de modificación (mtime) del último archivo de los 30 TOs del tramo 1 y
     la del primero de los 68 del tramo 2 (los tramos, de tanda_final/preregistro/tramos_tanda_final.json), y si la primera es anterior a
     la segunda. Lo mismo con la hora de cambio de estado (ctime), que ninguna herramienta común fija a mano: cambia con cualquier escritura
     o cambio de metadatos. Y las de las carpetas mismas (la del TO y sus subcarpetas), que cambian si se agrega, se borra o se renombra
     un archivo, lo que las horas de los archivos no ven: la última de las carpetas del tramo 1, contra el primer archivo del tramo 2.
  2. Desde b17746be (la extracción de los 98): `git diff --name-only b17746be HEAD` y `git status --porcelain -uall` sobre salida_r2b/, los
     dos vacíos; y cuántos archivos de salida_r2b/ ignora git (`git status --ignored`), que esos dos no ven: los cubre el punto 1.
Las horas, en la del sistema (UTC−3).
Uso: python3 -I -B control_fechas_salida_tramo1_mesa.py <repo> <salida.json>"""
import json
import os
import subprocess
import sys
import time
from pathlib import Path

R, OUT = Path(sys.argv[1]), Path(sys.argv[2])
REL = "data/experiment/reextraccion_v2/corpus_tanda_final/salida_r2b"
S = R / REL
git = lambda *a: subprocess.run(["git", "--no-optional-locks", "-C", str(R), *a], capture_output=True, check=True, text=True).stdout  # noqa: E731
tr = json.loads((R / "data/experiment/tanda_final/preregistro/tramos_tanda_final.json").read_text(encoding="utf-8"))
T1, T2 = list(tr["tramo_1_tos"]), list(tr["tramo_2_tos"])
hora = lambda t: time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(t))  # noqa: E731


def tiempos(to):
    m, c, n_enlaces, dm, dc = [], [], 0, [], []
    for raiz, _, archivos in os.walk(S / to, followlinks=False):
        st = os.lstat(raiz)
        dm.append(st.st_mtime)
        dc.append(st.st_ctime)
        for a in archivos:
            st = os.lstat(os.path.join(raiz, a))
            if os.path.islink(os.path.join(raiz, a)):
                n_enlaces += 1
            m.append(st.st_mtime)
            c.append(st.st_ctime)
    return m, c, n_enlaces, dm, dc


res = {"carpetas_de_los_98_existen": all((S / t).is_dir() for t in T1 + T2) and len(T1) == 30 and len(T2) == 68}
t1 = [tiempos(t) for t in T1]
t2 = [tiempos(t) for t in T2]
res["ninguna_carpeta_vacia"] = all(x[0] for x in t1 + t2)
res["enlaces_simbolicos"] = sum(x[2] for x in t1 + t2)
m1, m2 = max(max(x[0]) for x in t1), min(min(x[0]) for x in t2)
c1, c2 = max(max(x[1]) for x in t1), min(min(x[1]) for x in t2)
res["mtime_ultimo_archivo_tramo_1"] = hora(m1)
res["mtime_primer_archivo_tramo_2"] = hora(m2)
res["mtime_tramo_1_anterior_al_tramo_2"] = m1 < m2
res["ctime_ultimo_archivo_tramo_1"] = hora(c1)
res["ctime_primer_archivo_tramo_2"] = hora(c2)
res["ctime_tramo_1_anterior_al_tramo_2"] = c1 < c2
d1 = max(max(max(x[3]), max(x[4])) for x in t1)
res["ultima_hora_de_las_carpetas_del_tramo_1_mtime_o_ctime"] = hora(d1)
res["carpetas_del_tramo_1_sin_cambios_desde_el_primer_archivo_del_tramo_2"] = d1 < min(m2, c2)
res["b17746be"] = git("log", "-1", "--format=%h %ad", "--date=format:%d/%m/%Y %H:%M:%S", "b17746be").strip()
res["diff_desde_b17746be_vacio"] = git("diff", "--name-only", "b17746be", "HEAD", "--", REL) == ""
res["status_con_sin_rastrear_vacio"] = git("status", "--porcelain=v1", "-uall", "--", REL) == ""
res["archivos_ignorados_por_git"] = sum(1 for l in git("status", "--porcelain=v1", "-uall", "--ignored", "--", REL).splitlines() if l.startswith("!! "))
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(res, ensure_ascii=False, indent=1))
sys.exit(0 if res["carpetas_de_los_98_existen"] and res["mtime_tramo_1_anterior_al_tramo_2"] and res["ctime_tramo_1_anterior_al_tramo_2"]
         and res["carpetas_del_tramo_1_sin_cambios_desde_el_primer_archivo_del_tramo_2"] and res["diff_desde_b17746be_vacio"]
         and res["status_con_sin_rastrear_vacio"] else 1)
