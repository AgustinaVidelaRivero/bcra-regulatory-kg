"""B6.1, tanda final, T4, segundo tramo: el control del material de la ampliación (material_ampliacion_t4t2_tf.py), con el de T3
(t3/scripts/control_material_tf.py), que relee lo escrito: cuántas fichas, cuántas claves del estado o de las marcas de E3 quedan (tienen que ser 0),
de qué E0 sale el texto de cada ficha, cuántas no tienen texto y si algún .md trae «"estado». No muestra el contenido de ninguna ficha.
Uso: python3 -I -B control_material_tf.py <material> <salida.json>
"""
import json
import sys
from collections import Counter
from pathlib import Path

MAT, OUT = Path(sys.argv[1]), Path(sys.argv[2])
FUERA = {"estado", "estado_e3", "n_reintentos", "residuales", "marcas_e3", "copia_nota_e3", "no_verificada_e3", "cola_humana",
         "cola_chunks"}


def claves(x, acc: Counter) -> None:
    if isinstance(x, dict):
        for k, v in x.items():
            acc[k] += 1
            claves(v, acc)
    elif isinstance(x, list):
        for v in x:
            claves(v, acc)


res = {}
for indice in ("material_ampliacion_t4t2_tf.json",):
    for m in json.loads((MAT / indice).read_text(encoding="utf-8"))["muestras"]:
        nom = m.replace(":", "_")
        ctl = {"fichas": 0, "claves_vedadas": 0, "texto_de": Counter(), "sin_texto": 0}
        for x in (MAT / nom / f"fichas_{nom}.jsonl").read_text(encoding="utf-8").splitlines():
            if not x.strip():
                continue
            f = json.loads(x)
            ctl["fichas"] += 1
            acc = Counter()
            claves(f, acc)
            ctl["claves_vedadas"] += sum(acc[k] for k in FUERA)
            t = f["material"].get("texto_e3")
            if t and t.get("texto"):
                ctl["texto_de"][t["chunk_de"]] += 1
            else:
                ctl["sin_texto"] += 1
        ctl["texto_de"] = dict(ctl["texto_de"])
        ctl["estado_en_el_md"] = (MAT / nom / f"fichas_{nom}.md").read_text(encoding="utf-8").count('"estado')
        res[m] = ctl
res["ok"] = all(v["claves_vedadas"] == 0 and v["estado_en_el_md"] == 0 and v["sin_texto"] == 0 for k, v in res.items() if k != "ok")
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(res, ensure_ascii=False))
sys.exit(0 if res["ok"] else 1)
