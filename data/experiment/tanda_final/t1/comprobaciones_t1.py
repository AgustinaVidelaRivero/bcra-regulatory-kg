"""
comprobaciones_t1.py — B6.1, tanda final, T1: las comparaciones de reproducción del FRENO T1 que no salen de otro script, con su
salida en un JSON (pre-registro firmado de la tanda final, §7). USD 0, sin API. Solo lee; escribe --out.

  1. la E0 del repo (salida_tanda_final_r2b/) contra el primer nivel de la corrida 1 de los 98: nombres, sha256 y bytes;
  2. el manifiesto del repo contra el del primer armado (--manifiesto-armado-1): byte a byte;
  3. la versión derivada regenerada en el paso 0 (--derivada-dir) contra la commiteada: byte a byte;
  4. la corrida en seco: mis cuatro salidas, la consola y el resumen, entre las corridas 1, 2 y 3 (--seco-1, --seco-2,
     --seco-3, cada una con su runner/, y --consolas con las tres consolas y los tres resúmenes); y los archivos del runner de
     las corridas 1 y 2: cuántos difieren y de qué clase (checkpoint, reporte_e2 con la ruta de la salida normalizada, otros);
  5. el ensamblado del tramo 1: el kg.json de dos procesos distintos (--ens-1, --ens-2), completo y sin cola;
  6. las tres bases de la caché del repo contra su sha256 de antes de las pruebas del freno (--bases-antes, formato shasum).
Uso: python3 -I -B comprobaciones_t1.py --repo <raíz> --e0-corrida-1 <dir> --manifiesto-armado-1 <json> --derivada-dir <dir>
       --seco-1 <dir> --seco-2 <dir> --seco-3 <dir> --consolas <dir> --ens-1 <dir> --ens-2 <dir> --bases-antes <txt> --out <json>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.dont_write_bytecode = True
E0 = "data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b"
MAN = "data/experiment/reextraccion_v2/manifiestos/tanda_final_98tos_r2b.json"
PRE = "data/experiment/tanda_final/preregistro"
MIAS = ("corrida_en_seco_t1.json", "pedidos_t1.jsonl", "censo_unidades_grandes_t1.json", "estimado_por_to_t1.json")


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def arbol(d: Path) -> dict[str, str]:
    return {str(p.relative_to(d)): sha(p) for p in sorted(d.rglob("*")) if p.is_file()}


def main() -> int:
    ap = argparse.ArgumentParser()
    for k in ("--repo", "--e0-corrida-1", "--manifiesto-armado-1", "--derivada-dir", "--seco-1", "--seco-2", "--seco-3",
              "--consolas", "--ens-1", "--ens-2", "--bases-antes", "--out"):
        ap.add_argument(k, type=Path, required=True)
    a = ap.parse_args()
    r = a.repo.resolve()
    res: dict = {}

    # 1
    rep = {p.name: (sha(p), p.stat().st_size) for p in (r / E0).iterdir() if p.is_file()}
    c1 = {p.name: (sha(p), p.stat().st_size) for p in a.e0_corrida_1.iterdir() if p.is_file()}
    res["1_e0_repo_contra_corrida_1"] = {"repo": len(rep), "corrida_1": len(c1), "iguales": rep == c1,
                                         "distintos": sorted(k for k in set(rep) | set(c1) if rep.get(k) != c1.get(k))}
    # 2
    res["2_manifiesto_repo_contra_primer_armado"] = {"repo_sha256": sha(r / MAN), "armado_1_sha256": sha(a.manifiesto_armado_1),
                                                    "iguales": (r / MAN).read_bytes() == a.manifiesto_armado_1.read_bytes()}
    # 3
    res["3_derivada_regenerada"] = {
        n: {"regenerada": sha(a.derivada_dir / f"derivada_T1{suf}"), "commiteada": sha(r / PRE / f"preregistro_tanda_final_derivada_T1{suf}"),
            "iguales": (a.derivada_dir / f"derivada_T1{suf}").read_bytes() == (r / PRE / f"preregistro_tanda_final_derivada_T1{suf}").read_bytes()}
        for n, suf in (("md", ".md"), ("huecos", ".huecos.json"))}
    # 4
    s = [a.seco_1, a.seco_2, a.seco_3]
    mias = {f: [sha(d / f) for d in s] for f in MIAS}
    cons = {k: [sha(a.consolas / f"{k}_{i}.txt") for i in (1, 2, 3)] for k in ("consola_runner", "resumen")}
    j = [json.loads((d / "corrida_en_seco_t1.json").read_text(encoding="utf-8")) for d in s]
    t1, t2 = arbol(s[0] / "runner"), arbol(s[1] / "runner")
    dif = sorted(k for k in set(t1) | set(t2) if t1.get(k) != t2.get(k))
    clase = Counter()
    for k in dif:
        n = Path(k).name
        if n.startswith("checkpoint") or n == "ultimo_checkpoint.json":
            clase["checkpoint_o_ultimo_checkpoint"] += 1
        elif n.startswith("reporte_e2"):
            x = (s[0] / "runner" / k).read_text(encoding="utf-8").replace(str(s[0]), "<salida>")
            y = (s[1] / "runner" / k).read_text(encoding="utf-8").replace(str(s[1]), "<salida>")
            clase["reporte_e2_igual_con_la_ruta_normalizada" if x == y else "reporte_e2_distinto"] += 1
        else:
            clase["otros"] += 1
    res["4_corrida_en_seco"] = {
        "mis_salidas_1_y_2_iguales": all(v[0] == v[1] for v in mias.values()),
        "mis_salidas_3_igual_salvo_corrida_en_seco_t1": all(v[1] == v[2] for f, v in mias.items() if f != "corrida_en_seco_t1.json"),
        "corrida_en_seco_t1_3_contra_2": {"claves_nuevas": sorted(set(j[2]) - set(j[1])), "quitadas": sorted(set(j[1]) - set(j[2])),
                                          "distintas": sorted(k for k in j[1] if k in j[2] and j[1][k] != j[2][k]),
                                          "stub_con_texto_ordenado": j[2].get("stub_con_texto_ordenado")},
        "consola_y_resumen_iguales_en_las_tres": all(len(set(v)) == 1 for v in cons.values()),
        "runner_archivos": len(t1), "runner_archivos_2": len(t2), "runner_difieren": len(dif),
        "runner_difieren_por_clase": dict(sorted(clase.items()))}
    # 5
    ens = {}
    for v in ("ens_tramo1_r2b", "ens_tramo1_r2b_sincola"):
        x, y = a.ens_1 / v / "r2" / "kg.json", a.ens_2 / v / "r2" / "kg.json"
        ens[v] = {"proceso_1": sha(x), "proceso_2": sha(y), "iguales": x.read_bytes() == y.read_bytes()}
    res["5_ensamblado_tramo1_dos_procesos"] = ens
    # 6
    bases = {}
    for linea in a.bases_antes.read_text(encoding="utf-8").splitlines():
        m = re.match(r"([0-9a-f]{64})  (.+)$", linea)
        if m:
            bases[m.group(2)] = {"antes": m.group(1), "ahora": sha(r / m.group(2)), "iguales": m.group(1) == sha(r / m.group(2))}
    res["6_bases_de_la_cache_del_repo"] = bases
    res["todo_igual"] = (res["1_e0_repo_contra_corrida_1"]["iguales"] and res["2_manifiesto_repo_contra_primer_armado"]["iguales"]
                         and all(v["iguales"] for v in res["3_derivada_regenerada"].values())
                         and res["4_corrida_en_seco"]["mis_salidas_1_y_2_iguales"]
                         and res["4_corrida_en_seco"]["mis_salidas_3_igual_salvo_corrida_en_seco_t1"]
                         and res["4_corrida_en_seco"]["consola_y_resumen_iguales_en_las_tres"]
                         and not res["4_corrida_en_seco"]["runner_difieren_por_clase"].get("otros")
                         and not res["4_corrida_en_seco"]["runner_difieren_por_clase"].get("reporte_e2_distinto")
                         and all(v["iguales"] for v in ens.values()) and all(v["iguales"] for v in bases.values()))
    a.out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(res, ensure_ascii=False, indent=1))
    return 0 if res["todo_igual"] else 1


if __name__ == "__main__":
    sys.exit(main())
