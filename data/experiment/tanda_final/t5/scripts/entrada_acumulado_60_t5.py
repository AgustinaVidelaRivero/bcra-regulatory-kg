"""B6.1, tanda final, T5, punto 8 (la columna del tramo 1): la entrada del acumulado de las tandas 0 y 1 con el tramo 1
(entrada_acumulado_60_r2b/<TO>/), que T3 armó solo en su copia del repo y no está en el repo. La arma en <copia> (nunca en el repo) con el
mismo código que t3/scripts/armar_acumulados_tf.py (los mismos orígenes, el mismo orden y la misma lista «ruta sha256»), sin tocar la E0
ni los manifiestos del acumulado, que ya están. Controla que dé lo que T3 registró en t3/acumulado/armado_acumulado_60_tf.json («entrada»:
archivos, bytes y sha256 de la lista). No escribe los nombres de los archivos de la entrada (cegamiento: cuántos TOs tienen un archivo de
E3 es una cifra de E3). Solo escribe en <copia> y en <salida.json>.
Uso: python3 -I -B entrada_acumulado_60_t5.py <copia> <salida.json>
"""
import hashlib
import json
import shutil
import sys
from pathlib import Path

sys.dont_write_bytecode = True
C, OUT = Path(sys.argv[1]).resolve(), Path(sys.argv[2])
assert not (C / ".git").exists(), "corre sobre una copia del repo"
REX = C / "data/experiment/reextraccion_v2"
ACU = C / "data/experiment/tanda_final/t3/acumulado"
MAN = {"tanda0": REX / "manifiestos/tanda0_10tos_r2b.json", "tanda1": REX / "manifiestos/tanda1_20tos_r2b.json",
       "tanda_final": REX / "manifiestos/tanda_final_98tos_r2b.json"}
ENT = {"tanda0": REX / "corpus_tanda0/salida_r2b", "tanda1": REX / "corpus_tanda1/salida_r2b",
       "tanda_final": REX / "corpus_tanda_final/salida_r2b"}


def sha(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


m = {k: json.loads(p.read_text(encoding="utf-8")) for k, p in MAN.items()}
tramo1 = m["tanda_final"]["orden_corrida"][:30]
ids = {"tanda0": [t["id"] for t in m["tanda0"]["tos"]], "tanda1": [t["id"] for t in m["tanda1"]["tos"]],
       "tanda_final": [t["id"] for t in m["tanda_final"]["tos"] if t["id"] in tramo1]}
orden = m["tanda0"]["orden_corrida"] + m["tanda1"]["orden_corrida"] + list(tramo1)
tanda = {t: k for k in ids for t in ids[k]}
man60 = json.loads((ACU / "manifiestos/acumulado_60tos_r2b.json").read_text(encoding="utf-8"))
assert man60["orden_corrida"] == orden, "el orden no es el del manifiesto del acumulado de 60"
dest = ACU / "entrada_acumulado_60_r2b"
if dest.exists():
    raise SystemExit(f"FRENO: {dest} ya existe")
dest.mkdir(parents=True)
lista, iguales, n, b = hashlib.sha256(), True, 0, 0
for to in orden:
    o = ENT[tanda[to]] / to
    if not o.is_dir():
        raise SystemExit(f"FRENO: falta la carpeta del TO {to}")
    d = dest / to
    shutil.copytree(o, d)
    for p in sorted(x for x in o.rglob("*") if x.is_file()):
        q = d / p.relative_to(o)
        sq = sha(q)
        iguales = iguales and sq == sha(p)
        n += 1
        b += q.stat().st_size
        lista.update(f"{q.relative_to(dest)} {sq}\n".encode())
t3 = json.loads((ACU / "armado_acumulado_60_tf.json").read_text(encoding="utf-8"))["entrada"]
res = {"entrada": {"archivos": n, "bytes": b, "sha256_de_la_lista": lista.hexdigest(), "todos_iguales_al_origen": iguales},
       "la_de_T3": t3, "tos": len(orden), "por_tanda": {k: len(v) for k, v in ids.items()}}
res["igual_a_la_de_T3"] = res["entrada"] == t3
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(res, ensure_ascii=False))
sys.exit(0 if res["igual_a_la_de_T3"] else 1)
