"""U-OMISIONES-COD, O1 — grupo L: las 20 fichas del lote 1 del piloto de U-MED-UMBRALES rearmadas con las herramientas
adaptadas (comun_P.cuantia_del_elemento), sobre el grafo del acta o sobre otro grafo, y comparadas con las de
`p/lote1/`. Corre desde la raíz de una COPIA del repo con las herramientas adaptadas; escribe solo en --salida.
Con --kg, el grafo y su sha se redirigen en memoria (comun_P.KG, comun_P.KG_SHA256) y el acta se lee con ese sha.
Uso: python -B fichas_lote1_L.py --referencia <dir p/lote1 original> --salida <dir> [--kg <kg.json>]"""
import argparse, hashlib, json, sys
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--referencia", type=Path, required=True)
ap.add_argument("--salida", type=Path, required=True)
ap.add_argument("--kg", type=Path, default=None)
a = ap.parse_args()
raiz = Path.cwd().resolve()
assert not (raiz / ".git").exists(), "correr en una copia"
code = raiz / "data/experiment/med_umbrales/p/code"
sys.path.insert(0, str(code))
import comun_P as C  # noqa: E402
import armador_fichas_P as AF  # noqa: E402
assert Path(C.__file__).resolve().is_relative_to(raiz) and Path(AF.__file__).resolve().is_relative_to(raiz)
acta_p = raiz / "data/experiment/med_umbrales/p/acta_sorteo_P.json"
if a.kg is not None:
    b = a.kg.read_bytes()
    C.KG, C.KG_SHA256 = a.kg.resolve(), hashlib.sha256(b).hexdigest()
    acta = json.loads(acta_p.read_text(encoding="utf-8"))
    acta["grafo"]["kg_sha256"] = C.KG_SHA256
    a.salida.mkdir(parents=True, exist_ok=True)
    acta_p = a.salida / "acta_con_el_sha_del_grafo_nuevo.json"
    acta_p.write_text(json.dumps(acta, ensure_ascii=False, indent=1), encoding="utf-8")
sys.argv = ["armador_fichas_P.py", "--acta", str(acta_p), "--lote", "1", "--salida", str(a.salida), "--sin-render"]
AF.main()
res = {"iguales": [], "distintas": [], "solo_en_una": []}
nuevo = a.salida / "lote1"
for p in sorted({x.relative_to(a.referencia) for x in a.referencia.rglob("*.md")} |
                {x.relative_to(nuevo) for x in nuevo.rglob("*.md")}):
    x, y = a.referencia / p, nuevo / p
    if not x.exists() or not y.exists():
        res["solo_en_una"].append(str(p))
    elif x.read_bytes() == y.read_bytes():
        res["iguales"].append(str(p))
    else:
        res["distintas"].append(str(p))
r = json.loads((a.referencia / "fichas_lote1.json").read_text(encoding="utf-8"))
n = json.loads((nuevo / "fichas_lote1.json").read_text(encoding="utf-8"))
res["metas_de_las_fichas_iguales"] = r["fichas"] == n["fichas"]
(a.salida / "comparacion.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print({k: (len(v) if isinstance(v, list) else v) for k, v in res.items()}, res["distintas"])
