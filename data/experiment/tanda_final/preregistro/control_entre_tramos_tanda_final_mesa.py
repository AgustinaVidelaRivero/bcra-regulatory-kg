"""El control entre los dos tramos de la tanda final (mesa, §155, 18/10/2026; v3 de la §163; para sellar con el pre-registro de la tanda
final).

Decisiones de la autora del 15/10/2026 (registro de decisiones, §12 y §13): corre al cerrar el tramo 1 y antes de lanzar el tramo 2,
con los umbrales fijados antes; si salta, frena y decide la autora; si no, sigue sin leer nada.
- **Lo que mide, en las unidades de los TOs del tramo 1** (sin las partidas por corte, que reemplazan sus partes):
  1. el costo por unidad real (el gasto de sus dos fases, del estado del runner, sobre sus unidades de E0), contra 1,3 veces la base;
  2. las salidas inválidas de E1 (el último registro de E1 trae `error` o `reparacion_forma`; decisión 3 de la autora), contra el 1 %;
  3. los errores definitivos (los que cuenta `resumen_t2.resumir`), contra 0;
  4. la proporción a la cola (los tres estados de cola juntos), contra 1,5 veces la base.
- **Además, sin umbral** (decisión 3 de la autora, v3): cuántas unidades tuvieron reintento por forma de E1 (su último registro trae
  `reintento_forma`). Es información: no entra a los criterios.
- **Las bases** salen de la tanda 1 por `cifras_preregistro_tanda_final_mesa.py` (JSON `bases_control_entre_tramos`): una sola base con
  las 548 unidades RI o `sin_raiz`, el límite superior de Wilson si su cola tiene menos de 10, y el costo ponderado por la composición
  del tramo 1.
- **El cegamiento de U-MED-VERIF:** usa `resumen_t2.resumir` (`data/experiment/tanda1/t2/resumen_t2.py`), que junta los estados de
  aceptación y de cola y no lee los reintentos de E3. No lee ningún `NO_ABRIR_`.
- Solo lee. Corre desde una copia del repo (CLAUDE.md §4.l). USD 0.
Uso: python3 -I -B control_entre_tramos_tanda_final_mesa.py --repo <copia> --manifiesto <ruta relativa> --salida <salida del runner>
     --tramo <JSON con la lista de TOs del tramo 1> --bases <JSON de las cifras> [--out <JSON>]
Sale con 0 si los cuatro dan OK y con 3 si alguno da FRENO."""
import argparse
import json
import sys
from pathlib import Path


def evaluar(m: dict, b: dict) -> list:
    """Los cuatro criterios: (nombre, valor, umbral, OK o FRENO)."""
    u = m["unidades"]
    crit = [("costo por unidad", m["gasto_usd"] / u, b["umbral_costo_por_unidad_1_3"], m["gasto_usd"] / u <= b["umbral_costo_por_unidad_1_3"]),
            ("salidas inválidas de E1", m["salidas_invalidas_e1"] / u, b["umbral_salidas_invalidas"],
             m["salidas_invalidas_e1"] / u <= b["umbral_salidas_invalidas"]),
            ("errores definitivos", m["errores"], b["umbral_errores"], m["errores"] <= b["umbral_errores"]),
            ("proporción a la cola", m["cola"] / u, b["umbral_proporcion_cola_1_5"], m["cola"] / u <= b["umbral_proporcion_cola_1_5"])]
    return [(n, round(v, 6), t, "OK" if ok else "FRENO") for n, v, t, ok in crit]


def medir(repo: Path, manifiesto: str, salida: Path, tramo: list) -> dict:
    sys.path.insert(0, str(repo / "data/experiment/tanda1/t2"))
    import resumen_t2 as RT  # noqa: PLC0415
    assert Path(RT.__file__).resolve().is_relative_to(repo.resolve()), "resumen_t2 no es el de la copia"
    RT.MANIFIESTO_REL = manifiesto
    r = RT.resumir(repo, salida, repo / "no_existe_y_no_se_lee")
    falta = [t for t in tramo if t not in r["por_to"]]
    if falta:
        raise SystemExit(f"FRENO: TOs del tramo que no están en el manifiesto: {falta}")
    inval = rforma = 0
    for t in tramo:
        tdir = salida / t
        partes = json.loads((tdir / "particiones_por_corte.json").read_text(encoding="utf-8")) \
            if (tdir / "particiones_por_corte.json").exists() else {}
        ult = RT.last_wins(tdir / "extracciones_e1.jsonl")
        inval += sum(1 for cid, x in ult.items() if cid not in partes and (x.get("error") or x.get("reparacion_forma")))
        rforma += sum(1 for cid, x in ult.items() if cid not in partes and x.get("reintento_forma"))
    f = {t: r["por_to"][t] for t in tramo}
    return {"tos": len(tramo), "fases_cerradas": all(x["fases_cerradas"] for x in f.values()),
            "unidades": sum(x["unidades"] for x in f.values()), "gasto_usd": round(sum(x["gasto_usd"] for x in f.values()), 6),
            "errores": sum(x["errores"] for x in f.values()), "cola": sum(x["cola"] for x in f.values()), "salidas_invalidas_e1": inval,
            "reintento_por_forma_e1_informacion": rforma}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, required=True)
    ap.add_argument("--manifiesto", required=True)
    ap.add_argument("--salida", type=Path, required=True)
    ap.add_argument("--tramo", type=Path, required=True)
    ap.add_argument("--bases", type=Path, required=True)
    ap.add_argument("--out", type=Path, default=None)
    a = ap.parse_args()
    tramo = json.loads(a.tramo.read_text(encoding="utf-8"))
    tramo = list(tramo) if isinstance(tramo, (list, dict)) else tramo
    b = json.loads(a.bases.read_text(encoding="utf-8"))["bases_control_entre_tramos"]
    m = medir(a.repo, a.manifiesto, a.salida, tramo)
    if not m["fases_cerradas"]:
        print("FRENO: el tramo no tiene las dos fases cerradas en todos sus TOs")
        return 3
    ev = evaluar(m, b)
    for n, v, t, e in ev:
        print(f"{e:<5} {n}: {v} (umbral {t})")
    print(f"info  reintento por forma de E1: {m['reintento_por_forma_e1_informacion']} de {m['unidades']} unidades (sin umbral)")
    if a.out:
        a.out.write_text(json.dumps({"medido": m, "criterios": ev}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return 0 if all(e == "OK" for *_, e in ev) else 3


if __name__ == "__main__":
    sys.exit(main())
