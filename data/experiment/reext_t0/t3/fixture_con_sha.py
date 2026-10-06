"""U-REEXT-T0, T3: copia de la fixture de la suite con el kg_sha256 de las dos entradas r2b completado con el sha256 de
los grafos ensamblados, para que regression_kg elija la entrada sellada (selecciona por kg_sha256). Solo sobre una COPIA:
la fixture del repo no se toca; el kg_sha256 lo completa la autora. Comprueba que lo único distinto son esos dos campos.

Uso: python -B fixture_con_sha.py <fixture_origen> <fixture_destino> <sha_diez> <sha_desarrollo>"""
import json
import sys

ORIGEN, DESTINO, SHA_DIEZ, SHA_DES = sys.argv[1:5]
d = json.loads(open(ORIGEN, encoding="utf-8").read())
ee = d["estado_esperado"]
for nombre, sha in (("KG-Tanda0-Diez-r2b", SHA_DIEZ), ("KG-Tanda0-Desarrollo-r2b", SHA_DES)):
    assert ee[nombre]["kg_sha256"] is None, nombre
    ee[nombre]["kg_sha256"] = sha
txt = json.dumps(d, ensure_ascii=False, indent=1) + "\n"
open(DESTINO, "w", encoding="utf-8").write(txt)
a = json.loads(open(ORIGEN, encoding="utf-8").read())
b = json.loads(txt)
for nombre in ("KG-Tanda0-Diez-r2b", "KG-Tanda0-Desarrollo-r2b"):
    b["estado_esperado"][nombre]["kg_sha256"] = None
print("solo cambian los dos kg_sha256:", a == b)
