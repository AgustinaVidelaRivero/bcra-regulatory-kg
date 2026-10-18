"""B6.1, tanda 1, T3, punto 7: la composición por relación (y por rol_fuente) del universo de la observación (12) y de su muestra, para
el FRENO: el universo es el de A4.1 tal cual (todas las aristas menos `referencia` y menos el esqueleto), que en r2b incluye las
`remite_a` y las `establecida_en` que deriva el ensamblado. Solo lee muestras/poblaciones_t4.json, muestras/observacion_12.json y el
grafo sin cola. Uso: python3 -I -B composicion_obs12_t3f.py <raíz> <salida.json>"""
import json, sys
from collections import Counter
from pathlib import Path
RAIZ, OUT = Path(sys.argv[1]).resolve(), Path(sys.argv[2])
M = RAIZ / "data/experiment/tanda1/t3/muestras"
kg = json.loads((RAIZ / "data/experiment/reextraccion_v2/corpus_tanda1/ens_veinte_r2b_sincola/r2/kg.json").read_text(encoding="utf-8"))
rf = {(e["source"], e["relation"], e["target"]): (e.get("rol_fuente") or (e.get("properties") or {}).get("rol_fuente")) for e in kg["edges"]}
pob = json.loads((M / "poblaciones_t4.json").read_text(encoding="utf-8"))["muestras"]["observacion:12"]["ids_por_celda"]
mue = json.loads((M / "observacion_12.json").read_text(encoding="utf-8"))["celdas"]
def comp(ids):
    ids = [tuple(x) for x in ids]
    return {"relacion": dict(Counter(t[1] for t in ids).most_common()), "rol_fuente": dict(Counter(str(rf[t]) for t in ids).most_common())}
res = {"universo": comp([x for v in pob.values() for x in v]), "muestra": comp([x for v in mue.values() for x in v["elementos"]])}
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(res, ensure_ascii=False))
