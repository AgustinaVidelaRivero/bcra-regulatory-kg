"""U-RERESOL-CAT, R2-1 — resumen de los controles (USD 0): junta en un JSON lo que dejaron controles_r2_1.sh, las
corridas de reresolver_catalogo.py (prueba con T1 a T4 dos veces por grafo; catálogo sin ampliaciones, con la cola y sin
ella) y los selftests, todo dentro de una copia del repo. Solo lee la copia y escribe --out.

Uso, desde la raíz de la copia:
  <python> -B data/experiment/reresolucion_catalogo/r2_1_resumen_controles.py --trabajo _r2_1 --out <json>
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import OrderedDict
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
T = "data/experiment/reextraccion_v2/corpus_tanda0"
ESPERADO = OrderedDict([
    ("r2a_diez", ("70d51e429b0e2cc1aafa697e32bc83462d371dfdd5edafb34e92fe4f7be45bdd", None)),
    ("r2a_desarrollo", ("fa4c1043d859081e49dce6cb940a9f5d4c09fc6d449efb85355f95312257178a", None)),
    ("r2b_diez", ("a9631a64b422bdae634fb05135373c6f04c6272cdf7acd43a1be9f5b6c1f5f57", "ens_diez_r2b")),
    ("r2b_desarrollo", ("6e7560433148cfe0c476cdd61199c32278187c4196d6f90dc0a38976a6d8e9a2", "ens_desarrollo_r2b")),
    ("r2b_sincola_diez", ("e22fae1afc3cf37fbe5b49ee0b220d51d0ec5febc13abeb6ebf7b74226da34fb", "ens_diez_r2b_sincola")),
    ("r2b_sincola_desarrollo", ("2922b72dca2c2bcb204a04f53fc89f265ac2c57e83e6aaab2ce1af8b82d413e4",
                                "ens_desarrollo_r2b_sincola")),
])

def sha(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def comparar_dir(a: Path, b: Path, normalizar: tuple = ()) -> dict:
    fa = {str(p.relative_to(a)) for p in a.rglob("*") if p.is_file()}
    fb = {str(p.relative_to(b)) for p in b.rglob("*") if p.is_file()}
    iguales, iguales_norm, distintos = 0, [], []
    for rel in sorted(fa & fb):
        x, y = (a / rel).read_bytes(), (b / rel).read_bytes()
        if x == y:
            iguales += 1
            continue
        tx, ty = x.decode("utf-8", "replace"), y.decode("utf-8", "replace")
        for viejo, nuevo in normalizar:
            tx, ty = tx.replace(viejo, nuevo), ty.replace(viejo, nuevo)
        (iguales_norm if tx == ty else distintos).append(rel)
    return {"solo_en_a": sorted(fa - fb), "solo_en_b": sorted(fb - fa), "iguales": iguales,
            "iguales_con_ruta_normalizada": iguales_norm, "distintos": distintos}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--trabajo", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    W = a.trabajo
    out = OrderedDict()
    # cadenas sin parámetro (controles_r2_1.sh cadenas) y catálogo sin ampliaciones por la línea de comando
    cad = OrderedDict()
    for n, (esp, sellado) in ESPERADO.items():
        d = W / "control" / "cadenas" / n / "r2"
        fila = {"sha256": sha(d / "kg.json"), "esperado": esp, "igual": sha(d / "kg.json") == esp,
                "rc": (W / "control" / "cadenas" / f"consola_{n}.txt").read_text(encoding="utf-8").strip().splitlines()[-1]}
        if sellado:
            c = comparar_dir(RAIZ / T / sellado / "r2", d)
            fila["contra_el_sellado"] = {"iguales": c["iguales"], "distintos": c["distintos"],
                                         "solo_en_el_sellado": c["solo_en_a"], "solo_en_la_corrida": c["solo_en_b"]}
        cad[n] = fila
    out["cadenas_sin_parametro"] = cad
    vac = OrderedDict()
    for n, sellado in (("vacio_r2b_diez", "ens_diez_r2b"), ("vacio_r2b_sincola_diez", "ens_diez_r2b_sincola")):
        d = W / "control" / "catalogo_vacio" / n / "r2"
        c = comparar_dir(RAIZ / T / sellado / "r2", d)
        rep = json.loads((d / "reporte_ensamblado_r2.json").read_text(encoding="utf-8"))
        vac[n] = {"sha256": sha(d / "kg.json"), "igual_al_sellado": sha(d / "kg.json") == sha(RAIZ / T / sellado / "r2" / "kg.json"),
                  "contra_el_sellado": {"iguales": c["iguales"], "distintos": c["distintos"], "solo_en_el_sellado": c["solo_en_a"]},
                  "reporte_catalogo_resolucion": rep.get("catalogo_resolucion"), "reporte_con_cola": rep.get("con_cola")}
    out["cli_con_catalogo_sin_ampliaciones"] = vac
    # suite sobre las entradas selladas, código de HEAD contra código nuevo
    su = OrderedDict()
    for p in sorted((W / "control" / "suite").glob("suite_viejo_*.json")):
        n = p.stem.replace("suite_viejo_", "")
        q = p.with_name(f"suite_nuevo_{n}.json")
        su[n] = {"json_igual": p.read_bytes() == q.read_bytes(),
                 "md_igual": p.with_suffix(".md").read_bytes() == q.with_suffix(".md").read_bytes(),
                 "resumen": json.loads(q.read_text(encoding="utf-8"))["resumen"]}
    out["suite_head_contra_nuevo"] = su
    st = OrderedDict()
    for p in sorted((W / "control" / "selftests").glob("nuevo_*.txt")):
        t = p.read_text(encoding="utf-8").strip().splitlines()
        v = p.with_name(p.name.replace("nuevo_", "viejo_"))
        st[p.stem.replace("nuevo_", "")] = {"nuevo": t[-2:], "viejo": v.read_text(encoding="utf-8").strip().splitlines()[-2:]
                                            if v.exists() else None}
    out["selftests"] = st
    # corridas del script
    co = OrderedDict()
    for p in sorted((W / "corridas").glob("*/reporte_reresolucion.json")):
        r = json.loads(p.read_text(encoding="utf-8"))
        d = p.parent / "r2"
        ant = RAIZ / r["entrada"]["anterior"]
        co[p.parent.name] = OrderedDict([
            ("rc", (p.parent.parent / f"{p.parent.name}.log").read_text(encoding="utf-8").strip().splitlines()[-1]),
            ("no_explicado", r["no_explicado"]), ("sha256_kg", r["camino_b"]["sha256_kg"]),
            ("kg_igual_al_anterior", sha(d / "kg.json") == sha(ant / "kg.json")),
            ("registro_acumulado_igual_al_anterior", sha(d / "no_mapeados_sujetos.jsonl") == sha(ant / "no_mapeados_sujetos.jsonl")),
            ("resolucion_igual_a_la_anterior", sha(d / "resolucion_sujetos.jsonl") == sha(ant / "resolucion_sujetos.jsonl")),
            ("a_resueltas", r["camino_a"]["resueltas_ahora"]), ("a_mas_cambian", r["camino_a_mas"]["cambian_por_tipo"]),
            ("a_mas_reproduce", r["camino_a_mas"]["reproduce_la_decision_guardada"]),
            ("resolucion_b_igual_a_a_mas", r["resolucion_b_contra_a_mas"]["iguales"]),
            ("rechazos_e2", r["camino_b"]["rechazos_e2_por_motivo"]),
            ("registro", {k: r["registro_acumulado"][k] for k in ("filas_anterior", "filas_b", "filas_acumulado",
                                                                  "por_estado_acumulado", "por_estado_b",
                                                                  "1_sin_resolver_iguales_a_b_salvo_version",
                                                                  "2_destino_de_las_resueltas_igual_a_b",
                                                                  "3_filas_de_b_fuera_del_anterior")}
             | {"estado_distinto_de_b": len(r["registro_acumulado"]["estado_distinto_de_b"])}),
            ("gate", {"shapes": r.get("gate", {}).get("salida", {}).get("shapes_veredicto"),
                      "suite": r.get("gate", {}).get("salida", {}).get("suite_resumen"),
                      "ln6": (r.get("gate", {}).get("salida", {}).get("ln6") or {}).get("estado"),
                      "suite_estados_que_cambian": r.get("gate", {}).get("comparacion", {}).get("suite_estados_que_cambian")})])
    out["corridas_del_script"] = co
    dob = OrderedDict()
    for g in ("diez", "desarrollo"):
        a1, a2 = W / "corridas" / f"prueba_{g}_1", W / "corridas" / f"prueba_{g}_2"
        if a1.exists() and a2.exists():
            c = comparar_dir(a1, a2, ((f"prueba_{g}_1", "<SALIDA>"), (f"prueba_{g}_2", "<SALIDA>")))
            dob[g] = {"iguales": c["iguales"], "iguales_con_ruta_normalizada": c["iguales_con_ruta_normalizada"],
                      "distintos": c["distintos"], "solo_en_una": c["solo_en_a"] + c["solo_en_b"]}
    out["doble_corrida_prueba"] = dob
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{sha(a.out)}  {a.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
