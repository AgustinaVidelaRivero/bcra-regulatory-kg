"""Mesa, §237 (22/10/2026): controla que la marcada sellada de la clasificación del freno de T4 sea la que da el convertidor sobre la
exportación de Numbers que quedó al lado. Copia a una carpeta temporal, byte a byte (cp -c), la planilla, su sha256, el convertidor y la
exportación; corre el convertidor ahí, con su salida a la nada (lista ids y notas, que la mesa no lee), y compara el sha256 de la marcada
que da con el de la marcada del repo. La carpeta temporal se borra al terminar. No imprime nada de la planilla ni de la exportación.
Uso: python3 -I -B reconvertir_clasificacion_freno_T4_mesa.py <carpeta clasificacion_freno> <salida.json>"""
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

D, OUT = Path(sys.argv[1]), Path(sys.argv[2])
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()  # noqa: E731
N = ["clasificacion_freno_T4.csv", "planilla_clasificacion_freno_T4.sha256", "convertir_clasificacion_freno_T4.py",
     "clasificacion_freno_T4_exportada.csv"]
antes = {p.name: sha(p) for p in D.iterdir()}
with tempfile.TemporaryDirectory(prefix="reconv_mesa_") as t:
    T = Path(t)
    for n in N:
        subprocess.run(["cp", "-c", str(D / n), str(T / n)], check=True)
    p = subprocess.run([sys.executable, "-I", "-B", "convertir_clasificacion_freno_T4.py", "clasificacion_freno_T4_exportada.csv"], cwd=T,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    m = T / "clasificacion_freno_T4_marcada.csv"
    res = {"convertidor_rc_0": p.returncode == 0,
           "marcada_igual_a_la_del_repo": m.exists() and sha(m) == sha(D / "clasificacion_freno_T4_marcada.csv"),
           "sha256_de_la_marcada_del_repo": sha(D / "clasificacion_freno_T4_marcada.csv")}
res["carpeta_del_repo_sin_cambios"] = {p.name: sha(p) for p in D.iterdir()} == antes
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(res, ensure_ascii=False, indent=1))
sys.exit(0 if res["convertidor_rc_0"] and res["marcada_igual_a_la_del_repo"] and res["carpeta_del_repo_sin_cambios"] else 1)
