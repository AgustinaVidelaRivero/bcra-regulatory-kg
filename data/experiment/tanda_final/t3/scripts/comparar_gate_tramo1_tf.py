"""B6.1, tanda final, T3: el gate de los dos grafos del tramo 1 con la variante con la raya (la que rige, por la decisión de la autora
sobre el FRENO T3 parcial) contra el de la variante con los manifiestos de T1 (el del FRENO parcial, apartado en el scratchpad). El
`kg.json` es el mismo; cambian el manifiesto (sus `nombres_remision`) y el reporte del ensamblado. Para cada archivo de shapes y de la
suite: si es byte a byte igual y, si no, los renglones distintos después de normalizar la fecha de la corrida (la línea «- **Fecha:** …»
del .md y el campo "fecha" del .json) y los de la consola que dan la hora; los renglones distintos van enteros a la salida. Solo lee.
Uso: python3 -I -B comparar_gate_tramo1_tf.py <gate nuevo> <gate de la variante de T1> <salida.json>
"""
import difflib
import json
import re
import sys
from pathlib import Path

N, V, OUT = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
FECHA = [(re.compile(r"^- \*\*Fecha:\*\* .*$", re.M), "- **Fecha:** <FECHA>"), (re.compile(r'^(\s*)"fecha": "[^"]*",?$', re.M), r'\1"fecha": "<FECHA>",')]
res = {}
for e0 in ("e0_del_grafo", "e0_con_partes"):
    for g in ("tf_tramo1", "tf_tramo1_sincola"):
        a, b = N / e0 / g, V / e0 / g
        fa = sorted(p.name for p in a.iterdir() if p.is_file())
        fb = sorted(p.name for p in b.iterdir() if p.is_file())
        r = {"mismos_archivos": fa == fb, "archivos": {}}
        for n in sorted(set(fa) & set(fb)):
            x, y = (a / n).read_text(encoding="utf-8"), (b / n).read_text(encoding="utf-8")
            if x == y:
                r["archivos"][n] = {"byte_a_byte": True}
                continue
            for rx, rp in FECHA:
                x, y = rx.sub(rp, x), rx.sub(rp, y)
            dif = [d for d in difflib.unified_diff(y.splitlines(), x.splitlines(), lineterm="", n=0)
                   if d[:1] in "+-" and not d.startswith(("+++", "---"))]
            r["archivos"][n] = {"byte_a_byte": False, "renglones_distintos_con_la_fecha_normalizada": len(dif), "distintos": dif[:40]}
        res[f"{e0}/{g}"] = r
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for k, r in res.items():
    print(k, r["mismos_archivos"], {n: (v["byte_a_byte"] or v["renglones_distintos_con_la_fecha_normalizada"]) for n, v in r["archivos"].items()})
