"""B6.1, tanda final, T4, primer tramo, paso 0: el sha256 de las ocho muestras de t3/muestras/ (contra la tabla T5 del FRENO T3, que
sale de sorteos_*_tf.json), de los ocho fichas_*.jsonl y fichas_*.md del material (contra material_*_tf.json, tabla T6) y de la versión
derivada de la lectura (contra 26c29d94…, del FRENO T3). Solo lee; escribe <salida.json> e imprime.
Uso: python3 -I -B paso0_sha_muestras_t4.py <repo> <salida.json>
"""
import hashlib
import json
import sys
from pathlib import Path

R, OUT = Path(sys.argv[1]).resolve(), Path(sys.argv[2])
M = R / "data/experiment/tanda_final/t3/muestras"
L = lambda p: json.loads(p.read_text(encoding="utf-8"))  # noqa: E731
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()  # noqa: E731
res = {"muestras": {}, "material": {}}
for s in ("sorteos_t4_t3f_tf.json", "sorteos_t4t1_tf.json"):
    for m, x in L(M / s)["muestras"].items():
        h = sha(M / x["archivo"])
        res["muestras"][m] = {"archivo": x["archivo"], "sha256": h, "esperado": x["sha256"], "igual": h == x["sha256"]}
for s in ("material_t4_t3f_tf.json", "material_t4t1_tf.json"):
    for m, x in L(M / "material" / s)["muestras"].items():
        nom = m.replace(":", "_")
        for ext in ("jsonl", "md"):
            n = f"fichas_{nom}.{ext}"
            h = sha(M / "material" / nom / n)
            res["material"][f"{m} {ext}"] = {"sha256": h, "esperado": x["archivos"][n], "igual": h == x["archivos"][n]}
d = R / "data/experiment/tanda_final/preregistro/preregistro_tanda_final_derivada_T4.md"
res["derivada"] = {"sha256": sha(d), "igual_a_26c29d94": sha(d).startswith("26c29d94")}
res["ok"] = all(v["igual"] for v in res["muestras"].values()) and all(v["igual"] for v in res["material"].values()) \
    and res["derivada"]["igual_a_26c29d94"] and len(res["muestras"]) == 8 and len(res["material"]) == 16
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for k, v in res["muestras"].items():
    print("muestra", k, v["sha256"], v["igual"])
for k, v in res["material"].items():
    print("material", k, v["sha256"], v["igual"])
print("derivada", res["derivada"]["sha256"], res["derivada"]["igual_a_26c29d94"])
print("ok", res["ok"])
sys.exit(0 if res["ok"] else 1)
