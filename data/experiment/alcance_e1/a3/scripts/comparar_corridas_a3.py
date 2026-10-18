"""U-ALCANCE-E1, A3 (USD 0, sin API; solo lee): compara, archivo por archivo, las salidas de dos corridas de bateria_a3.sh (la
oficial y la de la reproducción), con la carpeta de trabajo de cada una reemplazada por «$W» antes de comparar (algunas
salidas escriben rutas). No compara las fotos ni el log, que llevan horas. No imprime el contenido de nada.
Uso: python3 -I -B comparar_corridas_a3.py SALIDA_A TRABAJO_A SALIDA_B TRABAJO_B RESULTADO.json
"""
import json
import os
import sys
from pathlib import Path

ma, ta, mb, tb, out = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3]), sys.argv[4], Path(sys.argv[5])


def norm(p: Path, t: str) -> bytes:
    b = p.read_bytes()
    for x in sorted({t, os.path.realpath(t)}, key=len, reverse=True):
        b = b.replace(x.encode("utf-8"), b"$W")
    return b


def archivos(m: Path) -> set:
    return {p.relative_to(m).as_posix() for p in m.rglob("*") if p.is_file()
            and not p.relative_to(m).as_posix().startswith("fotos/") and p.name not in ("bateria_a3.log", "marca_git_antes")}


a, b = archivos(ma), archivos(mb)
res = {"solo_en_la_oficial": sorted(a - b), "solo_en_la_reproduccion": sorted(b - a), "comparados": len(a & b),
       "iguales_byte_a_byte": [], "iguales_con_la_carpeta_de_trabajo_reemplazada": [], "distintos": []}
for r in sorted(a & b):
    if (ma / r).read_bytes() == (mb / r).read_bytes():
        res["iguales_byte_a_byte"].append(r)
    elif norm(ma / r, ta) == norm(mb / r, tb):
        res["iguales_con_la_carpeta_de_trabajo_reemplazada"].append(r)
    else:
        res["distintos"].append(r)
out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"comparados {res['comparados']}: iguales byte a byte {len(res['iguales_byte_a_byte'])}, iguales con la carpeta de "
      f"trabajo reemplazada {len(res['iguales_con_la_carpeta_de_trabajo_reemplazada'])} "
      f"{res['iguales_con_la_carpeta_de_trabajo_reemplazada']}, distintos {res['distintos']}; solo en la oficial "
      f"{res['solo_en_la_oficial']}; solo en la reproducción {res['solo_en_la_reproduccion']}")
sys.exit(0 if not res["distintos"] and not res["solo_en_la_oficial"] and not res["solo_en_la_reproduccion"] else 1)
