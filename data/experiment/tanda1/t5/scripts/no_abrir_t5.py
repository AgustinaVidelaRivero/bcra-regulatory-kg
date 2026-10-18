"""B6.1, tanda 1, T5, punto 9 (cegamiento de U-MED-VERIF): junta en <salida NO_ABRIR> las dos partes que escriben cifras_t5.py (las
cuentas por id de modelo de E3 y de los reintentos de E1 de la fase de E3) y selftest_t5.py (los conteos del selftest de claves). No
imprime nada de su contenido: solo el sha256 del archivo que escribe. Reemplaza en el texto, sin mirarlo, la ruta del scratchpad por
<SCRATCHPAD> y la carpeta personal por $HOME. Los NO_ABRIR_ de T2, T3 y T4 no se tocan ni se abren.
Uso: python3 -I -B no_abrir_t5.py <parte de cifras> <parte del selftest> <scratchpad> <salida NO_ABRIR_conteos_t5.json>
"""
import hashlib
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
P1, P2, SCR, OUT = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3], Path(sys.argv[4])
assert OUT.name == "NO_ABRIR_conteos_t5.json" and P1.name.startswith("NO_ABRIR_") and P2.name.startswith("NO_ABRIR_")
assert not OUT.exists()
d = {"que_es": "T5 de la tanda 1: lo que usa los reintentos de E3 o cuenta lo que el cegamiento de U-MED-VERIF veda",
     "ids_de_modelo": json.loads(P1.read_text(encoding="utf-8")), "selftest_de_claves": json.loads(P2.read_text(encoding="utf-8"))}
texto = json.dumps(d, ensure_ascii=False, indent=1, sort_keys=True) + "\n"
texto = texto.replace(str(Path(SCR).resolve()), "<SCRATCHPAD>").replace(SCR, "<SCRATCHPAD>").replace(str(Path.home()), "$HOME")
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(texto, encoding="utf-8")
print(hashlib.sha256(OUT.read_bytes()).hexdigest(), OUT.name)
