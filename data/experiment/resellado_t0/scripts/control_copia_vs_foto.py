"""Control: la copia tiene exactamente los archivos de la foto del repo menos los excluidos por la cláusula (y el volumen
de Neo4j), con el mismo sha256. Solo lee. Uso: python -I -B control_copia_vs_foto.py <foto.json> <copia> <salida.json>"""
import hashlib, json, os, sys
from pathlib import Path
foto = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))["archivos"]
C = Path(sys.argv[2])
def excluido(rel, v):
    partes = rel.split("/")
    n = partes[-1]
    if partes[0] in (".venv", ".venv-app"): return "venv"
    if "__pycache__" in partes: return "__pycache__"
    if n == ".DS_Store": return ".DS_Store"
    if v.startswith("sin_abrir:"): return "entorno_o_NO_ABRIR"
    if v.startswith("enlace:"): return "enlace"
    if rel.startswith("data/experiment/neo4j/volumen/"): return "volumen_neo4j"
    return None
from collections import Counter
exc = Counter(); esperados = {}
for rel, v in foto.items():
    e = excluido(rel, v)
    if e: exc[e] += 1
    else: esperados[rel] = v
copia = {}
for raiz, dirs, archs in os.walk(C):
    for a in archs:
        p = Path(raiz) / a
        copia[p.relative_to(C).as_posix()] = p
faltan = sorted(set(esperados) - set(copia)); sobran = sorted(set(copia) - set(esperados))
distintos = []
for rel in sorted(set(esperados) & set(copia)):
    h = hashlib.sha256(copia[rel].read_bytes()).hexdigest()
    if h != esperados[rel]: distintos.append(rel)
res = {"excluidos_por_clase": dict(exc), "esperados": len(esperados), "en_la_copia": len(copia),
       "faltan": faltan, "sobran": sobran, "distintos": distintos}
Path(sys.argv[3]).write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print({k: (len(v) if isinstance(v, list) else v) for k, v in res.items()})
