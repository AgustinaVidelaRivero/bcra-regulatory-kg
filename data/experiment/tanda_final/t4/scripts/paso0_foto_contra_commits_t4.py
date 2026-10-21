"""B6.1, tanda final, T4, primer tramo, paso 0: la foto nueva contra la foto de después de T3 (14:20:03), con lo que trajeron los tres
commits de T3 (eb5ad14b..7cbf3525, `git diff --name-status`). Solo lee; escribe <salida.json> e imprime el resumen.
  - Todo lo nuevo, lo cambiado y lo borrado tiene que estar entre las rutas de esos commits.
  - Cada ruta de los commits que esté en la foto nueva tiene que tener el sha256 de su blob en HEAD (`git cat-file`), y las borradas por
    los commits no tienen que estar.
  - Lo que la foto no abre (los NO_ABRIR_ y los .env) se compara por tamaño y fecha, como la foto.
Uso: python3 -I -B paso0_foto_contra_commits_t4.py <repo> <foto_despues_T3.json> <foto_antes_T4.json> <salida.json>
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

R, FA, FB, OUT = Path(sys.argv[1]).resolve(), Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4])
a = json.loads(FA.read_text(encoding="utf-8"))["archivos"]
b = json.loads(FB.read_text(encoding="utf-8"))["archivos"]
git = lambda *x: subprocess.run(["git", "--no-optional-locks", "-C", str(R), *x], capture_output=True, text=True, check=True).stdout  # noqa: E731
ns = [ln.split("\t") for ln in git("diff", "--name-status", "--no-renames", "eb5ad14b", "7cbf3525").splitlines() if ln]
en_commits = {x[-1]: x[0] for x in ns}
nuevos = sorted(set(b) - set(a))
borrados = sorted(set(a) - set(b))
cambiados = sorted(k for k in set(a) & set(b) if a[k] != b[k])
fuera = [r for r in nuevos + borrados + cambiados if r not in en_commits]
distinto_de_head = []
for r, st in en_commits.items():
    if st == "D":
        if r in b:
            distinto_de_head.append(r)
        continue
    if r not in b:
        distinto_de_head.append(r)
        continue
    if b[r].get("sin_abrir"):
        continue
    blob = subprocess.run(["git", "--no-optional-locks", "-C", str(R), "cat-file", "blob", f"HEAD:{r}"], capture_output=True, check=True).stdout
    if hashlib.sha256(blob).hexdigest() != b[r]["sha256"]:
        distinto_de_head.append(r)
res = {"foto_despues_T3": {"sha256": hashlib.sha256(FA.read_bytes()).hexdigest()},
       "foto_antes_T4": {"sha256": hashlib.sha256(FB.read_bytes()).hexdigest()},
       "rutas_en_los_commits": len(en_commits), "por_estado_en_los_commits": {s: sum(1 for v in en_commits.values() if v == s)
                                                                             for s in sorted(set(en_commits.values()))},
       "nuevos": len(nuevos), "borrados": len(borrados), "cambiados": len(cambiados),
       "nuevos_borrados_o_cambiados_fuera_de_los_commits": fuera, "rutas_de_los_commits_distintas_de_HEAD": distinto_de_head,
       "ok": not fuera and not distinto_de_head}
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(res, ensure_ascii=False, indent=1))
sys.exit(0 if res["ok"] else 1)
