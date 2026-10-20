"""B6.1, tanda final, T3, punto 4: la E0 con las partes por corte, que rige para S31 (registro de decisiones, §29; pre-registro de la
tanda final, §7), armada dentro de una COPIA del repo (nunca el repo), con data/experiment/tanda1/t3/scripts/e0_partes_t3f.py como
modelo. Escribe en <copia>/data/experiment/tanda_final/t3/e0_con_partes/ (fuera del repo: shapes y las intrínsecas la leen con ruta
relativa) y en <salida.json>.

  1. reext_t0/t3/e0_con_partes.py, sin cambios, dos veces por E0, cada una en un proceso aparte:
       tanda_final: E0 reextraccion_v2/e0_chunking/salida_tanda_final_r2b, salida reextraccion_v2/corpus_tanda_final/salida_r2b;
       acum128:     E0 tanda_final/t3/acumulado/e0_acumulado_128_r2b, salida tanda_final/t3/acumulado/entrada_acumulado_128_r2b;
       acum60:      E0 tanda_final/t3/acumulado/e0_acumulado_60_r2b, salida tanda_final/t3/acumulado/entrada_acumulado_60_r2b.
     Control: las dos corridas, byte a byte iguales. El sha256 de cada archivo y el del conjunto (sha256 de las líneas «sha256  nombre»,
     ordenadas por nombre, con salto de línea final), y las unidades reemplazadas por sus partes.
  2. Controles contra lo sellado, archivo por archivo:
       - tanda_final: la tanda final no tuvo unidades partidas (FRENO T2): la E0 con las partes es la E0 del repo;
       - acum128 y acum60: cada archivo de un TO de las tandas 0 y 1 es el de la E0 con las partes del acumulado de la tanda 1
         (tanda1/t3/gate_decisiones/e0_con_partes_t3f.json, `acumulado`, `sha256_por_archivo`), y cada archivo de un TO de la tanda
         final es el de la E0 con las partes de la tanda final.
Uso: python3 -I -B e0_partes_tf.py <python del repo> <copia> <salida.json>
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

PY, C, OUT = sys.argv[1], Path(sys.argv[2]).resolve(), Path(sys.argv[3])
assert not (C / ".git").exists(), "correr sobre una copia del repo"
X = "data/experiment/reextraccion_v2"
A = "data/experiment/tanda_final/t3/acumulado"
DEST = "data/experiment/tanda_final/t3/e0_con_partes"
E0S = {"tanda_final": (f"{X}/e0_chunking/salida_tanda_final_r2b", f"{X}/corpus_tanda_final/salida_r2b"),
       "acum128": (f"{A}/e0_acumulado_128_r2b", f"{A}/entrada_acumulado_128_r2b"),
       "acum60": (f"{A}/e0_acumulado_60_r2b", f"{A}/entrada_acumulado_60_r2b")}
T1 = json.loads((C / "data/experiment/tanda1/t3/gate_decisiones/e0_con_partes_t3f.json").read_text(encoding="utf-8"))
T1_ACUM = T1["e0_con_partes"]["acumulado"]["sha256_por_archivo"]


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def archivos(d: Path) -> dict:
    return {p.relative_to(d).as_posix(): sha(p.read_bytes()) for p in sorted(d.rglob("*")) if p.is_file()}


def conjunto(fs: dict) -> str:
    return sha("".join(f"{h}  {n}\n" for n, h in sorted(fs.items())).encode())


if (C / DEST).exists():
    raise SystemExit(f"FRENO: {DEST} ya existe en la copia")
(C / DEST).mkdir(parents=True)
res = {"destino": DEST, "e0_con_partes": {}, "controles": {}}
for nombre, (e0, sal) in E0S.items():
    corr = []
    for k in (1, 2):
        dest = C / DEST / f"{nombre}_corrida{k}"
        q = subprocess.run([PY, "-I", "-B", str(C / "data/experiment/reext_t0/t3/e0_con_partes.py"), str(C / e0), str(C / sal), str(dest)],
                           capture_output=True, text=True)
        (C / DEST / f"consola_{nombre}_corrida{k}.txt").write_text(q.stdout + q.stderr + f"rc={q.returncode}\n", encoding="utf-8")
        fs = archivos(dest)
        corr.append({"rc": q.returncode, "reemplazos": json.loads(q.stdout)["reemplazos"] if q.returncode == 0 else None,
                     "archivos": len(fs), "sha256_conjunto": conjunto(fs), "sha256_por_archivo": fs})
    res["e0_con_partes"][nombre] = {"e0": e0, "salida": sal, "ruta_corrida1": f"{DEST}/{nombre}_corrida1",
                                    "corridas": [{k: v for k, v in c.items() if k != "sha256_por_archivo"} for c in corr],
                                    "iguales": corr[0]["sha256_por_archivo"] == corr[1]["sha256_por_archivo"] and corr[0]["rc"] == 0,
                                    "unidades_reemplazadas": sum(len(v) for v in (corr[0]["reemplazos"] or {}).values()),
                                    "sha256_conjunto": corr[0]["sha256_conjunto"], "sha256_por_archivo": corr[0]["sha256_por_archivo"]}
tf = res["e0_con_partes"]["tanda_final"]
e0_tf = archivos(C / E0S["tanda_final"][0])
res["controles"]["tanda_final_igual_a_la_e0_del_repo"] = tf["sha256_por_archivo"] == e0_tf and tf["unidades_reemplazadas"] == 0
for nombre in ("acum128", "acum60"):
    fs = res["e0_con_partes"][nombre]["sha256_por_archivo"]
    de_t1 = {n: h for n, h in fs.items() if n in T1_ACUM}
    de_tf = {n: h for n, h in fs.items() if n not in T1_ACUM}
    res["controles"][nombre] = {"archivos_de_las_tandas_0_y_1": len(de_t1), "iguales_a_la_tanda_1": all(T1_ACUM[n] == h for n, h in de_t1.items()),
                                "archivos_de_la_tanda_final": len(de_tf),
                                "iguales_a_la_tanda_final": all(tf["sha256_por_archivo"].get(n) == h for n, h in de_tf.items())}
res["ok"] = (all(v["iguales"] for v in res["e0_con_partes"].values()) and res["controles"]["tanda_final_igual_a_la_e0_del_repo"]
             and all(res["controles"][n]["iguales_a_la_tanda_1"] and res["controles"][n]["iguales_a_la_tanda_final"] for n in ("acum128", "acum60")))
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for n, v in res["e0_con_partes"].items():
    print(f"E0 con partes {n}: {v['corridas'][0]['archivos']} archivos, dos corridas iguales {v['iguales']}, unidades reemplazadas "
          f"{v['unidades_reemplazadas']} {v['corridas'][0]['reemplazos']}, conjunto {v['sha256_conjunto']}")
print("controles:", json.dumps(res["controles"], ensure_ascii=False))
print("OK" if res["ok"] else "FRENO")
sys.exit(0 if res["ok"] else 1)
