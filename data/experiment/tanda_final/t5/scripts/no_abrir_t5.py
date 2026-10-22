"""B6.1, tanda final, T5, punto 9: junta en <t5>/NO_ABRIR_conteos_t5.json las dos salidas bajo el cegamiento de U-MED-VERIF que escriben
contado_tramo1_t5.py (la cola por estado, el crudo del reintento de E3 y las properties_no_definidas de los grafos del tramo 1) e
ids_modelo_t5.py (cuántas llamadas devolvió cada id en E3 y en los reintentos de E1 de su fase). No las interpreta: pega su texto, tal
cual, como valores de un objeto JSON. Imprime solo el sha256 de lo escrito; nada de su contenido.
Uso: python3 -I -B no_abrir_t5.py <NO_ABRIR del contado> <NO_ABRIR de los ids> <salida>
"""
import hashlib
import sys
from pathlib import Path

A, B, OUT = (Path(x) for x in sys.argv[1:4])
assert A.name.startswith("NO_ABRIR_") and B.name.startswith("NO_ABRIR_") and OUT.name.startswith("NO_ABRIR_")
assert not OUT.exists(), OUT
OUT.write_text('{"contado_tramo1_t5": ' + A.read_text(encoding="utf-8").strip() + ',\n"ids_modelo_t5": '
               + B.read_text(encoding="utf-8").strip() + '}\n', encoding="utf-8")
print(OUT.name, hashlib.sha256(OUT.read_bytes()).hexdigest())
