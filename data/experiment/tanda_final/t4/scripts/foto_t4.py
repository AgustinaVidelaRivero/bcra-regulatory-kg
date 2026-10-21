"""B6.1, tanda final, T4, primer tramo: el resumen de la foto del repo para el FRENO, desde la foto del paso 0 y la de después
(tanda_final/t1/foto_repo_tanda_final_t1.py; las dos, fuera del repo y del paquete, porque nombran todas las rutas del repo) y las dos
listas de .pyc. Solo lee; escribe <salida.json> e imprime el resumen.
  - Lo nuevo, lo borrado y lo cambiado, dentro de data/experiment/tanda_final/t4/ y fuera de ella. El «seguí» admite lo nuevo solo en
    tanda_final/t4/ y nada borrado ni cambiado.
  - Los .pyc antes y después.
Uso: python3 -I -B foto_t4.py <foto_antes.json> <foto_despues.json> <pyc_antes.txt> <pyc_despues.txt> <salida.json>
"""
import hashlib
import json
import sys
from pathlib import Path

FA, FD, PA, PD, OUT = (Path(x) for x in sys.argv[1:6])
fa, fd = (json.loads(p.read_text(encoding="utf-8")) for p in (FA, FD))
a, d = fa["archivos"], fd["archivos"]
T4 = "data/experiment/tanda_final/t4/"
nuevos = sorted(set(d) - set(a))
borrados = sorted(set(a) - set(d))
cambiados = sorted(k for k in set(a) & set(d) if a[k] != d[k])
pa, pd = (p.read_text(encoding="utf-8").splitlines() for p in (PA, PD))
res = {"foto_antes": {"sha256": hashlib.sha256(FA.read_bytes()).hexdigest(), "inicio": fa["inicio"], "fin": fa["fin"], "n": fa["n"]},
       "foto_despues": {"sha256": hashlib.sha256(FD.read_bytes()).hexdigest(), "inicio": fd["inicio"], "fin": fd["fin"], "n": fd["n"],
                        "sin_abrir": fd["sin_abrir"], "enlaces": fd["enlaces"]},
       "nuevos_en_t4": [r[len(T4):] for r in nuevos if r.startswith(T4)], "nuevos_fuera_de_t4": [r for r in nuevos if not r.startswith(T4)],
       "borrados": borrados, "cambiados": cambiados,
       "pyc": {"antes": len(pa), "despues": len(pd), "iguales": pa == pd}}
res["ok"] = not res["nuevos_fuera_de_t4"] and not borrados and not cambiados and res["pyc"]["iguales"]
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps({k: (len(v) if isinstance(v, list) else v) for k, v in res.items()}, ensure_ascii=False, indent=1))
sys.exit(0 if res["ok"] else 1)
