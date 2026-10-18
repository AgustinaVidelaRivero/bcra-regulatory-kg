"""B6.1, tanda 1, T3, punto 4: la clase de cada regresión de la suite en los cuatro grafos nuevos. Solo lee los suite_perfil_r2.json.
  - declarada: una de las tres que declara el laudo de la release r2, §3, punto 2 (RT-C5-3, RT-C6-1 y RT-C6-2);
  - no declarada, también en el acumulado: la da el grafo acumulado (que tiene los 30 TOs) contra la entrada sellada del grafo anterior;
  - no declarada, solo sin los TOs de la tanda 0: la da el grafo de la tanda 1 solo y no el acumulado, con el mismo código y las mismas
    expectativas; el ítem se cumple cuando están los TOs de la tanda 0. Se lista con su detalle, para leer si su ancla es de un TO que el
    grafo de la tanda 1 no tiene.
Uso: python3 -I -B clasificar_regresiones_t3.py --suite <nombre>=<suite_perfil_r2.json> [...] --acumulado <nombre> --out <json>
"""
import argparse
import json
from pathlib import Path

DECLARADAS = ("RT-C5-3", "RT-C6-1", "RT-C6-2")   # docs/laudo_release_r2_pipeline.md:70-72


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--suite", action="append", required=True)
    ap.add_argument("--acumulado", action="append", required=True, help="nombre de un --suite que es un acumulado")
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    su = {}
    for x in a.suite:
        n, p = x.split("=", 1)
        su[n] = json.loads(Path(p).read_text(encoding="utf-8"))
    reg = {n: {r["item"]: r for r in (s.get("regresion") or {}).get("regresiones", [])} for n, s in su.items()}
    items = {n: {i["id"]: i for i in s["items"]} for n, s in su.items()}
    en_acum = set().union(*(set(reg[n]) for n in a.acumulado))
    res = {}
    for n in su:
        filas = []
        for iid, r in reg[n].items():
            clase = ("declarada" if iid in DECLARADAS else "no declarada, también en el acumulado" if iid in en_acum
                     else "no declarada, solo sin los TOs de la tanda 0")
            acum_estado = {m: items[m][iid]["estado"] for m in a.acumulado}
            filas.append({"item": iid, "clase": clase, "esperado": r.get("esperado"), "medido": r.get("medido"),
                          "en_los_acumulados": acum_estado, "detalle": str(items[n][iid].get("detalle"))[:300]})
        cuenta = {}
        for f in filas:
            cuenta[f["clase"]] = cuenta.get(f["clase"], 0) + 1
        res[n] = {"entrada": (su[n].get("regresion") or {}).get("entrada"), "regresiones": len(filas), "por_clase": cuenta,
                  "filas": sorted(filas, key=lambda f: (f["clase"], f["item"]))}
    a.out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for n, r in res.items():
        print(f"{n}: {r['regresiones']} regresiones {r['por_clase']} (entrada {r['entrada']})")
        for f in r["filas"]:
            if f["clase"] != "declarada":
                print(f"   {f['item']:<26} {f['esperado']} → {f['medido']:<13} [{f['clase']}] acumulados={f['en_los_acumulados']} | {f['detalle'][:150]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
