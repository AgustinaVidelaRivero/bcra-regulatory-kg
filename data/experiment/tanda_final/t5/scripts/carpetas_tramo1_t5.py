"""B6.1, tanda final, T5, punto 8 (enmienda 9, §1, punto 6): el sha256 de las carpetas de salida de los 30 TOs del tramo 1
(reextraccion_v2/corpus_tanda_final/salida_r2b/<TO>/), hoy. El de cada carpeta es el sha256 de su lista ordenada «ruta sha256», con la
ruta relativa a la carpeta (el formato de la lista de t3/scripts/armar_acumulados_tf.py). No escribe nombres de archivos ni cuántos tiene
cada carpeta: cuántos TOs tienen un archivo de E3 es una cifra de E3 (cegamiento). Los 30 TOs y su orden salen de
tanda_final/preregistro/tramos_tanda_final.json (tramo_1_tos). Solo lee; escribe <salida.json> e imprime el resumen.
Uso: python3 -I -B carpetas_tramo1_t5.py <raíz> <salida.json>
"""
import hashlib
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
R, OUT = Path(sys.argv[1]).resolve(), Path(sys.argv[2])
S = R / "data/experiment/reextraccion_v2/corpus_tanda_final/salida_r2b"
tos = json.loads((R / "data/experiment/tanda_final/preregistro/tramos_tanda_final.json").read_text(encoding="utf-8"))["tramo_1_tos"]


def sha(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


por_to = {}
for to in tos:
    d = S / to
    assert d.is_dir(), to
    lista = hashlib.sha256()
    for p in sorted(x for x in d.rglob("*") if x.is_file()):
        lista.update(f"{p.relative_to(d)} {sha(p)}\n".encode())
    por_to[to] = lista.hexdigest()
todas = hashlib.sha256("".join(f"{to} {h}\n" for to, h in por_to.items()).encode()).hexdigest()
res = {"tos": len(tos), "formato": "sha256 de la lista ordenada «ruta sha256» de cada carpeta; el de las 30, de la lista «TO sha256»",
       "sha256_por_carpeta": por_to, "sha256_de_las_30": todas}
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps({"tos": res["tos"], "sha256_de_las_30": todas}, ensure_ascii=False))
