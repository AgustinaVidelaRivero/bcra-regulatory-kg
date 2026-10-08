"""U-ALCANCE-E1, A1: suma a candado_mensaje_r2b.json (de la copia que se pasa como argumento) cuatro copias sintéticas de
cap::1.4.1 con documentos del registro de alcance por tanda. Escribe solo ese archivo. Uso: sinteticos_fixture.py RAIZ"""
import copy
import json
import sys
from pathlib import Path

ruta = Path(sys.argv[1]) / "data/experiment/reextraccion_v2/e1_extractor/candado_mensaje_r2b.json"
doc = json.loads(ruta.read_text(encoding="utf-8"))
assert len(doc["chunks"]) == 13 and doc["sinteticos"] == ["cap::1.4.1::sintetico_alcance_clase"]
base = next(c for c in doc["chunks"] if c["id"] == "cap::1.4.1")
CASOS = (("registro_clase", "ri_ccna.pdf", "con una clase (Sujeto_caja_de_credito)"),
         ("registro_dos_clases", "snp_cheq.pdf", "con dos clases"),
         ("registro_rol_reutilizado", "ri_rml.pdf", "con un rol reutilizado (Sujeto_rol_entidad_comprendida_reginf)"),
         ("registro_sin_alcance", "ri_oc.pdf", "de un documento declarado sin alcance, que va sin línea"))
for rama, archivo, que in CASOS:
    c = copy.deepcopy(base)
    c["id"] = f"cap::1.4.1::sintetico_{rama}"
    c["archivo"] = archivo
    c["sintetico"] = (f"copia de cap::1.4.1 con archivo {archivo}: ejercita la rama del registro de alcance por tanda "
                      f"{que} (U-ALCANCE-E1)")
    doc["chunks"].append(c)
    doc["sinteticos"].append(c["id"])
doc["descripcion"] += (" U-ALCANCE-E1 (A1, 08/10/2026): cuatro copias sintéticas más de cap::1.4.1 con documentos del "
                       "registro de alcance por tanda (una clase, dos clases, un rol reutilizado y uno declarado sin "
                       "alcance).")
ruta.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(len(doc["chunks"]), doc["sinteticos"])
