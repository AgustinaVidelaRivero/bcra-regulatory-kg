#!/usr/bin/env python3
"""analizar_n6_con_lectura_tolerante.py — La regla de N4 sobre los agregados de N6 con la lectura tolerante (decisión de la autora
del 27/10/2026, recibida a las 23:26:23, punto 1; mesa, §312), con las funciones del análisis sellado (analizar_n6.py, sin editarlo)
y sin abrir el archivo de preguntas de N3. USD 0: no llama a ningún modelo.

El análisis sellado carga las preguntas de N3 (correr_n6.cargar_entrada) para dos cosas: la cantidad de criterios de cada pregunta y
sus conjuntos (las 30 y las Qk). Este script toma:
  · la cantidad de criterios, de los agregados que usa (n_criterios de cada id opaco, con el id recomputado desde la sesión como lo
    hace analizar_n6.cargar_sesiones), que tiene que ser una sola por pregunta;
  · los conjuntos, de los que escribió el análisis sellado (`conjuntos` de analisis_n6.json).
Con eso arma las filas con analizar_n6.cargar_sesiones, sobre una copia de agente/ de la salida de N6 y los agregados que se le
pasan, y las medidas y la regla con analizar_n6.fidelidad, operativo, regla, no_cumplidos y clases_n1, como analizar_n6.analizar.
Las citas no dependen del juez: van las del análisis sellado, declaradas.

La reproducción: con los agregados sellados (juez/agregados_n6_ciego.json), lo que calcula tiene que ser igual, clave por clave, a
analisis_n6.json; con --solo-reproducir imprime solo si cada clave es igual y no escribe ninguna cifra. Con los de la lectura
tolerante escribe --salida.

  python -B analizar_n6_con_lectura_tolerante.py --salida-n6 <banco_n6> --agregados <json> --trabajo <dir nuevo>
      [--clon <carpeta n6 de una copia de HEAD>] [--sha256-entrada <hex>] (--solo-reproducir | --salida <json>)
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
SHA_ENTRADA = "d6a5a0a367ee22b1acbe9a43c44f9d09c656ac06699abf952f943216d9696df8"
CLAVES = ("entrada_sha256", "conjuntos", "n_sesiones", "clases", "medidas", "regla", "regla_sensibilidad", "clases_n1",
          "no_cumplidos_para_n1", "caso_jerarquia", "sin_veredicto")


def sha(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def rt(x):
    return json.loads(json.dumps(x, ensure_ascii=False))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida-n6", type=Path, required=True)
    ap.add_argument("--agregados", type=Path, required=True)
    ap.add_argument("--trabajo", type=Path, required=True)
    ap.add_argument("--clon", type=Path, default=AQUI)
    ap.add_argument("--sha256-entrada", default=SHA_ENTRADA)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--solo-reproducir", action="store_true")
    g.add_argument("--salida", type=Path)
    a = ap.parse_args(argv)
    clon = a.clon.resolve()
    for p in (str(AQUI), str(clon)):
        if p not in sys.path:
            sys.path.insert(0, p)
    import correr_n6 as CN                      # noqa: PLC0415  (solo import)
    import analizar_n6 as AN                    # noqa: PLC0415  (solo import)
    N6 = a.salida_n6.resolve()
    if a.trabajo.exists():
        raise SystemExit("ABORTO: --trabajo ya existe")
    sellado_p = N6 / "analisis" / "analisis_n6.json"
    sellado = json.loads(sellado_p.read_text(encoding="utf-8"))
    ent_p = clon / "entrada_n6.json"
    if sha(ent_p) != a.sha256_entrada or sellado["entrada_sha256"] != a.sha256_entrada:
        raise SystemExit("ABORTO: la entrada o el análisis sellado no son los de N6")
    e = json.loads(ent_p.read_text(encoding="utf-8"))
    cfg_p = CN.BANCO_DIR / e["config_agentes"]["ruta"]
    if sha(cfg_p) != e["config_agentes"]["sha256"]:
        raise SystemExit("ABORTO: la configuración de los agentes no da su sha256")
    e["_cfg"], e["_sha"] = json.loads(cfg_p.read_text(encoding="utf-8")), a.sha256_entrada

    # La salida de trabajo: una copia de agente/ (sin enlaces) y los agregados que se usan.
    sal = a.trabajo / "salida"
    shutil.copytree(N6 / "agente", sal / "agente", symlinks=False,
                    ignore=shutil.ignore_patterns("*SOLO_MESA*", "NO_ABRIR_*"))
    (sal / "juez").mkdir(parents=True)
    shutil.copyfile(a.agregados, sal / "juez" / "agregados_n6_ciego.json")
    agg = {x["id_opaco"]: x for x in json.loads(a.agregados.read_text(encoding="utf-8"))["agregados"]}

    # La cantidad de criterios de cada pregunta, desde los agregados, con el id opaco recomputado desde la sesión.
    st = CN.estado(e, sal)
    n_de: dict[str, set] = {}
    for k, v in st["por_sesion"].items():
        s, f = v["sesion"], v["final"]
        if not f or f["clase"] != "completa":
            continue
        m = json.loads((Path(f["carpeta"]) / f"meta_{f['id']}.json").read_text(encoding="utf-8"))
        r = (m.get("final_json_R4") or {}).get("respuesta")
        if isinstance(r, str) and r.strip():
            x = agg.get(CN.id_opaco(s["qid"], s["configuracion"], s["rep"], CN.sha256_texto(r)))
            if x is not None:
                n_de.setdefault(s["qid"], set()).add(x["n_criterios"])
    qids = {s["qid"] for s in e["orden"]["sesiones"]}
    if set(n_de) != qids or any(len(v) != 1 for v in n_de.values()):
        raise SystemExit("ABORTO: alguna pregunta sin una sola cantidad de criterios en los agregados")
    e["_preguntas"] = {q: {"criterios": [None] * next(iter(n_de[q]))} for q in sorted(qids)}

    filas = AN.cargar_sesiones(e, sal)
    c = sellado["conjuntos"]
    Qs = {"30": set(c["30"]), **{k: set(c[str(k)]) for k in (1, 2, 3, 4, 5, 6)}}
    tiene_vp = {b["configuracion_n6"]: "mcp__kg__ver_punto" in b["tools_esperadas"]
                for b in e["_cfg"]["brazos"].values() if b.get("servidor") == "kg"}
    caso = json.loads((clon / "caso_jerarquia_N6.json").read_text(encoding="utf-8"))
    medidas = {}
    for conf in list(e["_cfg"]["configuraciones_n6"]):
        m = {"30": AN.fidelidad(filas, Qs["30"], conf), "30_sensibilidad": AN.fidelidad(filas, Qs["30"], conf, sensibilidad=True),
             "sin_FUERA_D9": AN.fidelidad(filas, Qs["30"] - set(AN.FUERA_D9), conf)}
        for k in (1, 2, 3, 4, 5, 6):
            m[f"Q{k}"] = AN.fidelidad(filas, Qs[k], conf)
        if conf in AN.REPETIDAS:
            m["por_corrida"] = {r: AN.fidelidad(filas, Qs["30"], conf, rep=r) for r in (1, 2, 3)}
        verif = {f["qid"] for f in filas if f["configuracion"] == conf and f["vio_marca"]}
        m["vio_una_marca"] = AN.fidelidad([f for f in filas if f["vio_marca"]], Qs["30"], conf)
        m["no_vio_ninguna_marca"] = AN.fidelidad([f for f in filas if not f["vio_marca"]], Qs["30"], conf)
        m["preguntas_con_marca_vista"] = len(verif)
        m["operativo"] = AN.operativo(filas, conf, Qs["30"])
        medidas[conf] = m
    r = {"entrada_sha256": a.sha256_entrada, "conjuntos": {str(k): sorted(v) for k, v in Qs.items()}, "n_sesiones": len(filas),
         "clases": dict(AN.Counter(f["clase"] for f in filas)), "medidas": medidas, "regla": AN.regla(filas, Qs, caso, tiene_vp),
         "regla_sensibilidad": AN.regla(filas, Qs, caso, tiene_vp, sensibilidad=True), "clases_n1": AN.clases_n1(None, None, filas),
         "no_cumplidos_para_n1": AN.no_cumplidos(filas),
         "caso_jerarquia": {k: caso.get(k) for k in ("configuracion", "llamadas", "llega_en_2_llamadas_o_menos")},
         "sin_veredicto": sorted(f["id"] for f in filas if f["modales"] is None)}
    r = rt(r)
    if a.solo_reproducir:
        iguales = {k: r[k] == sellado[k] for k in CLAVES}
        print(json.dumps({"agregados": a.agregados.name, "agregados_sha256": sha(a.agregados), "reproduce_por_clave": iguales,
                          "reproduce": all(iguales.values())}, ensure_ascii=False, indent=1))
        return 0 if all(iguales.values()) else 1
    out = {"unidad": "U-NAV-DISENO, N6 — la regla de N4 con la lectura tolerante (decisión de la autora del 27/10/2026, opción B)",
           "codigo": {Path(__file__).name: sha(Path(__file__)), "analizar_n6.py": sha(Path(AN.__file__))},
           "agregados": {"ruta": a.agregados.name, "sha256": sha(a.agregados), "n": len(agg)},
           "analisis_sellado": {"ruta": "analisis/analisis_n6.json", "sha256": sha(sellado_p)},
           **r, "citas": sellado["citas"],
           "citas_de_donde": "las del análisis sellado: no dependen del juez (analizar_n6.citas lee las metas y los logs R1)"}
    a.salida.parent.mkdir(parents=True, exist_ok=True)
    a.salida.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"análisis con la lectura tolerante: {len(filas)} sesiones, {len(r['sin_veredicto'])} sin veredicto -> {a.salida.name} "
          f"({sha(a.salida)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
