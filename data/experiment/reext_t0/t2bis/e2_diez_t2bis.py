"""T2-bis, condición 2 de la corrección de cerrar_e2: con el runner corregido, el E2 (perfil de E1) y el E2 r2 de los
diez TOs, regenerados sin red sobre la salida de T2 de una COPIA, salen byte a byte iguales a los del repo.
Uso: python -B e2_diez_t2bis.py <copia> <repo>"""
import hashlib, importlib.util, json, sys
from pathlib import Path
COPIA, REPO = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
RUNNER = COPIA / "data/experiment/reextraccion_v2/corpus_v2/runner_corpus.py"
sys.path[0] = str(RUNNER.parent)          # modo script, como `python runner_corpus.py`
spec = importlib.util.spec_from_file_location("runner_corpus", RUNNER)
RC = importlib.util.module_from_spec(spec); sys.modules["runner_corpus"] = RC; spec.loader.exec_module(RC)
RC.configurar(RC.manifiesto_corpus.cargar(COPIA / "data/experiment/reextraccion_v2/manifiestos/tanda0_10tos_r2b.json"))
RC.PERFIL_R2 = RC.perfil_forma_r2(RC.PERFIL)
import os
os.chdir(COPIA)                           # la ruta de salida va relativa, como en la corrida real (el reporte la guarda)
SAL = Path("data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b")
SAL_R = REPO / "data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b"
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
res = {}
for to in RC.TOS_ORDEN:
    RC.cerrar_e2(to, SAL)
    RC.cerrar_e2_r2(to, SAL)
    a = {p.name: sha(p) for p in sorted((SAL_R / to).iterdir()) if p.is_file()}
    b = {p.name: sha(p) for p in sorted((SAL / to).iterdir()) if p.is_file()}
    res[to] = {"archivos": len(b), "iguales": sum(a.get(k) == v for k, v in b.items()),
               "distintos": sorted(k for k, v in b.items() if a.get(k) != v)}
print(json.dumps(res, ensure_ascii=False, indent=1))
print("TOTAL: todos iguales" if all(not r["distintos"] for r in res.values()) else "TOTAL: HAY DIFERENCIAS")
