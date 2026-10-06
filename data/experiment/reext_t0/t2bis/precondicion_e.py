"""Precondición e de T2-bis: particionar_por_corte de cap::4.2.1.2 (E0 r2b), sobre una copia, con llamado directo."""
import json, sys
from pathlib import Path
REX = Path("data/experiment/reextraccion_v2").resolve()
sys.path.insert(0, str(REX / "e1_extractor")); sys.path.insert(0, str(REX / "e0_chunking"))
import comun_e1, correr_e0
E0 = REX / "e0_chunking" / "salida_tanda0_r2b"
c = next(x for x in comun_e1.cargar_chunks(("cap",), e0_dir=E0) if x["id"] == "cap::4.2.1.2")
print("unidad", c["id"], "| caracteres del texto:", len(c["texto"]), "| claves:", sorted(c)[:12])
partes, informe = correr_e0.particionar_por_corte(c)
print("partes:", None if partes is None else [(p["id"], len(p["texto"])) for p in partes])
print("informe:", json.dumps(informe, ensure_ascii=False)[:600])
