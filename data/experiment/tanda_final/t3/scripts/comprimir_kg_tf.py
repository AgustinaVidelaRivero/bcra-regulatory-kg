"""B6.1, tanda final, T3, punto 3: los `kg.json` de más de 100 MB (100.000.000 bytes) de los ocho ensamblados, comprimidos con
scripts/kg_gz.py y su sello al lado (registro de decisiones, §30; pre-registro de la tanda final, §8), sobre una COPIA del repo, y la
prueba de que cada `.gz` se restaura byte a byte. USD 0. Por grafo:
  1. si el `kg.json` pasa de 100.000.000 bytes, `kg_gz.py comprimir <kg.json>` en la copia (escribe `kg.json.gz` y `kg.json.gz.sello.json`
     al lado);
  2. la restauración: el `.gz` y el sello, solos, a <prueba>/<grafo>/, y `kg_gz.py restaurar` ahí; el `kg.json` restaurado tiene que ser
     byte a byte el de la copia, y `kg_gz.py verificar --kg` sobre la copia tiene que dar OK.
Además lista los archivos del ensamblado que pasan de 50.000.000 bytes, para ver que solo el `kg.json` se acerca al límite de git.
Uso: python3 -I -B comprimir_kg_tf.py <python del repo> <copia> <prueba> <salida.json>
"""
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

PY, C, P, OUT = sys.argv[1], Path(sys.argv[2]).resolve(), Path(sys.argv[3]).resolve(), Path(sys.argv[4])
X = "data/experiment/reextraccion_v2/corpus_tanda_final"
A = "data/experiment/tanda_final/t3/acumulado"
GRAFOS = {"tf98": f"{X}/ens_98_r2b", "tf98_sincola": f"{X}/ens_98_r2b_sincola", "tf_tramo1": f"{X}/ens_tramo1_r2b",
          "tf_tramo1_sincola": f"{X}/ens_tramo1_r2b_sincola", "acum128": f"{A}/ens_128_r2b", "acum128_sincola": f"{A}/ens_128_r2b_sincola",
          "acum60": f"{A}/ens_60_tramo1_r2b", "acum60_sincola": f"{A}/ens_60_tramo1_r2b_sincola"}
LIMITE, AVISO = 100_000_000, 50_000_000
KG_GZ = C / "scripts/kg_gz.py"


def sha(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def corre(*args, cwd=None) -> dict:
    q = subprocess.run([PY, "-I", "-B", str(KG_GZ), *map(str, args)], capture_output=True, text=True, cwd=cwd)
    return {"rc": q.returncode, "salida": (q.stdout + q.stderr).strip().replace(str(C), "<COPIA>").replace(str(P), "<PRUEBA>")}


if P.exists():
    raise SystemExit(f"FRENO: {P} ya existe")
res = {"limite_bytes": LIMITE, "grafos": {}}
for g, d in GRAFOS.items():
    kg = C / d / "r2/kg.json"
    n = kg.stat().st_size
    grandes = {f.relative_to(C / d).as_posix(): f.stat().st_size for f in (C / d).rglob("*") if f.is_file() and f.stat().st_size > AVISO}
    r = {"carpeta": d, "kg_bytes": n, "kg_sha256": sha(kg), "pasa_de_100_MB": n > LIMITE, "archivos_de_mas_de_50_MB": grandes}
    if n > LIMITE:
        r["comprimir"] = corre("comprimir", kg)
        gz, sello = kg.with_name("kg.json.gz"), kg.with_name("kg.json.gz.sello.json")
        s = json.loads(sello.read_text(encoding="utf-8"))
        dest = P / g
        dest.mkdir(parents=True)
        shutil.copy2(gz, dest / gz.name)
        shutil.copy2(sello, dest / sello.name)
        r["restaurar"] = corre("restaurar", dest / gz.name)
        r["restaurado_sha256"] = sha(dest / "kg.json")
        r["restaurado_igual_byte_a_byte"] = (dest / "kg.json").read_bytes() == kg.read_bytes()
        r["verificar"] = corre("verificar", gz, "--kg", kg)
        r["sello"] = {k: s[k] for k in ("kg_json_sha256", "kg_json_bytes", "gz_sha256", "gz_bytes")} | {
            "zlib": s["compresor"]["zlib"], "python": s["compresor"]["python"]}
        r["ok"] = (r["comprimir"]["rc"] == 0 and r["restaurar"]["rc"] == 0 and r["verificar"]["rc"] == 0 and r["restaurado_igual_byte_a_byte"]
                   and s["kg_json_sha256"] == r["kg_sha256"] and sha(gz) == s["gz_sha256"])
        (dest / "kg.json").unlink()
    else:
        r["ok"] = True
    r["ok"] = r["ok"] and all(k == "r2/kg.json" or v <= LIMITE for k, v in grandes.items())
    res["grafos"][g] = r
res["ok"] = all(r["ok"] for r in res["grafos"].values())
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for g, r in res["grafos"].items():
    print(g, r["kg_bytes"], "comprimido" if r["pasa_de_100_MB"] else "sin comprimir",
          (f"gz {r['sello']['gz_bytes']} {r['sello']['gz_sha256'][:12]}… restaurado igual {r['restaurado_igual_byte_a_byte']}"
           if r["pasa_de_100_MB"] else ""), "| de más de 50 MB:", r["archivos_de_mas_de_50_MB"], "| ok", r["ok"])
print("OK" if res["ok"] else "FRENO")
sys.exit(0 if res["ok"] else 1)
