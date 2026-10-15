"""Re-sellado único de la tanda 0, §7 (escrituras): pasa al repo, archivo por archivo, los bytes que la etapa produjo en la
copia. Ningún generador corre sobre el repo. Escribe solo las rutas autorizadas:
  - nuevas: los cuatro manifiestos de reextraccion_v2/manifiestos/, los cuatro ensamblados nuevos de corpus_tanda0/
    (ens_*_rs1/) y la carpeta propia de la etapa (data/experiment/resellado_t0/, sin el FRENO, que se escribe aparte);
  - que cambian: la fixture y grafos.py (solo las entradas nuevas) y los documentos con la nota del §6 y del §4.
Antes de escribir: cada ruta nueva no existe en el repo y cada archivo que cambia es, byte a byte, el de HEAD (git show) y
el que la copia tenía antes de editarse (es decir, la copia partió de él). Después: cada archivo del repo es byte a byte el de
la copia. Frena sin escribir nada si falla un control previo.
Uso: python3 -I -B escribir_en_el_repo_rs1.py <copia> <repo> <salida.json> [--seco]
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

C, R, SAL = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve(), Path(sys.argv[3])
SECO = "--seco" in sys.argv
X = "data/experiment/reextraccion_v2"
NUEVOS_DIRS = [f"{X}/corpus_tanda0/ens_diez_r2b_rs1", f"{X}/corpus_tanda0/ens_diez_r2b_sincola_rs1",
               f"{X}/corpus_tanda0/ens_desarrollo_r2b_rs1", f"{X}/corpus_tanda0/ens_desarrollo_r2b_sincola_rs1",
               "data/experiment/resellado_t0"]
NUEVOS = [f"{X}/manifiestos/tanda0_ens_{g}_rs1.json" for g in ("diez_r2b", "desarrollo_r2b", "diez_r2b_sincola",
                                                                  "desarrollo_r2b_sincola")]
CAMBIAN = ["scripts/regression_kg_esperado.json", "data/experiment/neo4j/grafos.py"]
notas = json.loads((C / "data/experiment/resellado_t0/salidas/notas_s6_rs1.json").read_text(encoding="utf-8"))
CAMBIAN += list(notas["firmados"]) + list(notas["leemes"])
for d in NUEVOS_DIRS:
    NUEVOS += sorted(p.relative_to(C).as_posix() for p in (C / d).rglob("*") if p.is_file()
                     and p.name != "FRENO_resellado_T0.md")


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def head(rel: str) -> bytes:
    return subprocess.run(["git", "-C", str(R), "show", f"HEAD:{rel}"], capture_output=True, check=True).stdout


res = {"nuevos": len(NUEVOS), "cambian": len(CAMBIAN), "previos": {}, "escritos": {}, "seco": SECO}
fallas = []
for d in NUEVOS_DIRS:
    if (R / d).exists():
        fallas.append(f"ya existe {d}")
for rel in NUEVOS:
    if (R / rel).exists():
        fallas.append(f"ya existe {rel}")
for rel in CAMBIAN:
    actual, h = (R / rel).read_bytes(), head(rel)
    if actual != h:
        fallas.append(f"{rel} no es el de HEAD")
    nuevo = (C / rel).read_bytes()
    if rel in notas["firmados"] or rel in notas["leemes"]:
        v = notas["firmados"].get(rel) or notas["leemes"].get(rel)
        if v["sha256_antes"] != sha(h) or v["sha256_despues"] != sha(nuevo) or not nuevo.startswith(h):
            fallas.append(f"{rel}: la nota no parte de HEAD o no es solo un agregado al final")
    res["previos"][rel] = {"repo_igual_a_HEAD": actual == h, "sha256_HEAD": sha(h), "sha256_nuevo": sha(nuevo)}
res["fallas_previas"] = fallas
if fallas:
    SAL.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("FRENA sin escribir:", fallas[:10])
    sys.exit(1)
if not SECO:
    for rel in NUEVOS + CAMBIAN:
        dst = R / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes((C / rel).read_bytes())
for rel in NUEVOS + CAMBIAN:
    if SECO:
        continue
    a, b = (R / rel).read_bytes(), (C / rel).read_bytes()
    res["escritos"][rel] = {"sha256": sha(a), "igual_a_la_copia": a == b}
res["ok"] = SECO or all(v["igual_a_la_copia"] for v in res["escritos"].values())
SAL.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(("SECO: " if SECO else "") + f"nuevos {len(NUEVOS)}, cambian {len(CAMBIAN)}; controles previos OK; "
      + ("" if SECO else f"escritos iguales a la copia: {sum(v['igual_a_la_copia'] for v in res['escritos'].values())} de {len(res['escritos'])}"))
