"""
freno_t2_cifras.py — B6.1, tanda final, T2: las cifras y las tablas del FRENO T2 (parcial o final), desde sus archivos
(pre-registro firmado de la tanda final, §7: «toda cifra del FRENO sale por script»). USD 0, sin API. Solo lee; escribe --md
y --json. No abre ningún NO_ABRIR_ ni la salida del runner: lee el registro de avance, la salida de `resumen_t2.py` (que el
cegamiento deja reportar), el JSON del control entre tramos, el manifiesto, el estimado plano de T1 y las cifras del
pre-registro.

Fuentes (relativas a --repo, salvo --log y --foto-*):
  - data/experiment/tanda_final/t2/avance_t2.jsonl: el lanzamiento, por TO (tramo, inicio, fin, código, freno por modelo con
    sus ids, gasto global);
  - data/experiment/tanda_final/t2/resumen_t2_tramo1.json (--resumen): las unidades, las aceptadas, la cola, los errores, los
    ids repetidos, la cobertura y el gasto por TO;
  - data/experiment/tanda_final/t2/control_entre_tramos_tanda_final.json;
  - el manifiesto (el estimado repartido por TO), data/experiment/tanda_final/t1/seco/estimado_por_to_t1.json (el estimado
    plano por TO: la tarifa del §3 más las líneas de alcance de A3) y salida_cifras_preregistro_tanda_final.json (las cifras
    del §3 por tramo);
  - data/experiment/tanda_final/t1/estimaciones/estimaciones_t2_t1.json (la duración proyectada);
  - --log: la salida de pantalla del lanzador, con el renglón `rc=` que agrega la consola;
  - --foto-antes, --foto-despues y --comparacion: las fotos del repo y su comparación (solo se cuentan rutas por carpeta).
Uso: python3 -I -B freno_t2_cifras.py --repo <raíz> --resumen <json> --log <log> --foto-antes <json> --foto-despues <json>
       --comparacion <json> --md <md> --json <json>
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import datetime
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

sys.dont_write_bytecode = True
T2 = "data/experiment/tanda_final/t2"
MAN = "data/experiment/reextraccion_v2/manifiestos/tanda_final_98tos_r2b.json"
PLANO = "data/experiment/tanda_final/t1/seco/estimado_por_to_t1.json"
CIFRAS = "data/experiment/tanda_final/preregistro/salida_cifras_preregistro_tanda_final.json"
ESTIM = "data/experiment/tanda_final/t1/estimaciones/estimaciones_t2_t1.json"
CARPETAS = ("data/experiment/reextraccion_v2/corpus_tanda_final/", "data/experiment/tanda_final/t2/",
            "data/experiment/neo4j/volumen/", "data/experiment/reextraccion_v2/e1_extractor/cache/",
            "data/experiment/reextraccion_v2/e3_verificador/cache/", "logs/cache_usage.jsonl")
D = lambda x: Decimal(str(x))  # noqa: E731
q = lambda x, n=4: str(D(x).quantize(Decimal(1).scaleb(-n), ROUND_HALF_UP))  # noqa: E731


def main() -> int:
    ap = argparse.ArgumentParser()
    for k in ("--repo", "--resumen", "--log", "--foto-antes", "--foto-despues", "--comparacion", "--md", "--json"):
        ap.add_argument(k, type=Path, required=True)
    a = ap.parse_args()
    r = a.repo.resolve()
    leer = lambda p: json.loads((p if p.is_absolute() else r / p).read_text(encoding="utf-8"))  # noqa: E731
    md, out = [], {}

    def tabla(t, cab, filas):
        md.append(f"\n### {t}\n")
        md.append("| " + " | ".join(cab) + " |")
        md.append("|" + "|".join("---" for _ in cab) + "|")
        md.extend("| " + " | ".join(str(x) for x in f) + " |" for f in filas)

    # 1. el lanzamiento
    ev = [json.loads(x) for x in (r / T2 / "avance_t2.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
    ini = [e for e in ev if e["evento"] == "inicio_lanzador"]
    fin = [e for e in ev if e["evento"] == "fin_lanzador"]
    rc = [x for x in a.log.read_text(encoding="utf-8").splitlines() if x.startswith("rc=")]
    ts = lambda s: datetime.strptime(s, "%Y-%m-%dT%H:%M:%S%z")  # noqa: E731
    dur = [round((ts(f["ts"]) - ts(i["ts"])).total_seconds() / 60, 1) for i, f in zip(ini, fin)]
    out["lanzamientos"] = [{"inicio": i["ts"], "pid": i["pid"], "fin": f["ts"], "min": m, "copia_de_trabajo_borrada": f["copia_de_trabajo_borrada"]}
                           for i, f, m in zip(ini, fin, dur)]
    out["codigo_de_salida"] = rc
    out["paradas"] = [e["motivo"] for e in ev if e["evento"] == "parada"]
    tabla("1. Los lanzamientos", ["#", "inicio", "pid", "fin", "minutos", "copia de trabajo borrada", "salida", "parada"],
          [[n + 1, x["inicio"], x["pid"], x["fin"], x["min"], x["copia_de_trabajo_borrada"], rc[n] if n < len(rc) else "—",
            "; ".join(out["paradas"]) or "—"] for n, x in enumerate(out["lanzamientos"])])
    cp = next(e for e in ev if e["evento"] == "controles_previos")
    fa = next(e for e in ev if e["evento"] == "freno_modelo_antes")
    md.append(f"\nControles previos: ok={cp['ok']}; {cp['libres_kb']} KB libres; {', '.join(cp['rutas_78'])}; SDK {cp['sdk']}; "
              f"sha256 del manifiesto {cp['manifiesto_sha256_ok']}; tope {cp['tope_ok']}; tramos {cp['tramos_ok']}. Freno por modelo "
              f"antes del primer TO, sobre {fa['tos']} TOs: {fa['resultado']} (ids de E1 {fa['ids_e1']}, de E3 {fa['ids_e3']}).")

    # 2. por TO, del registro de avance
    fins = {e["to"]: e for e in ev if e["evento"] == "to_fin"}
    filas = []
    for e in ev:
        if e["evento"] != "to_fin":
            continue
        m = round((ts(e["fin"]) - ts(e["inicio"])).total_seconds() / 60, 1)
        filas.append([e["to"], e["tramo"], e["inicio"][11:19], e["fin"][11:19], m, e["rc"], e["freno_modelo"],
                      ", ".join(e["ids_e1"]), ", ".join(e["ids_e3"]), e["gasto_global_usd"]])
    out["por_to_avance"] = filas
    tabla("2. Por TO, del registro de avance", ["TO", "tramo", "inicio", "fin", "min", "rc", "freno", "ids E1", "ids E3",
                                                "gasto global USD"], filas)

    # 3. el control entre tramos
    ct = leer(Path(T2) / "control_entre_tramos_tanda_final.json")
    out["control_entre_tramos"] = ct
    tabla("3. El control entre tramos", ["criterio", "valor", "umbral", "resultado"], [list(c) for c in ct["criterios"]])
    md.append(f"\nMedido: {json.dumps(ct['medido'], ensure_ascii=False)}.")

    # 4. resumen_t2, por TO del tramo 1 y totales
    rs = leer(a.resumen)
    man = leer(Path(MAN))
    t1 = man["orden_corrida"][:30]
    t2 = man["orden_corrida"][30:]
    k = ("unidades", "unidades_con_partes", "aceptadas", "cola", "errores", "sin_destino", "ids_repetidos")
    f_res = [[to] + [rs["por_to"][to][x] for x in k] + [rs["por_to"][to]["cobertura_completa"], rs["por_to"][to]["cobertura_exacta_e0"],
                                                          rs["por_to"][to]["fases_cerradas"], rs["por_to"][to]["gasto_usd"]] for to in t1]
    tot = {x: sum(rs["por_to"][to][x] for to in t1) for x in k}
    gasto_t1 = sum(D(rs["por_to"][to]["gasto_usd"]) for to in t1)
    out["resumen_tramo_1"] = {"totales": tot, "gasto_usd": str(gasto_t1),
                              "tramo_2_tos_con_alguna_fase": sum(1 for to in t2 if rs["por_to"][to]["gasto_usd"] or rs["por_to"][to]["fases_cerradas"]),
                              "total_resumen": rs["total"], "gasto_global_usd": rs["gasto_global_usd"], "tope_usd": rs["tope_usd"],
                              "dentro_del_tope": rs["dentro_del_tope"], "lineas_del_runner": Counter(x["linea"].split(":")[0] for x in rs["lineas_del_runner"])}
    tabla("4. resumen_t2.py, el tramo 1 por TO", ["TO"] + list(k) + ["cobertura", "cobertura E0", "fases cerradas", "gasto USD"],
          f_res + [["total del tramo 1"] + [tot[x] for x in k] + ["", "", sum(rs["por_to"][to]["fases_cerradas"] for to in t1), str(gasto_t1)]])
    md.append(f"\nTotal de resumen_t2 (los 98): {json.dumps(rs['total'], ensure_ascii=False)}; gasto global USD {rs['gasto_global_usd']} "
              f"de un tope de {rs['tope_usd']} (dentro: {rs['dentro_del_tope']}). Los 68 del tramo 2: con alguna fase o gasto, "
              f"{out['resumen_tramo_1']['tramo_2_tos_con_alguna_fase']}. Líneas del runner que toma resumen_t2: "
              f"{dict(out['resumen_tramo_1']['lineas_del_runner'])}.")

    # 5. el costo
    plano = leer(Path(PLANO))["por_to"]
    cif = leer(Path(CIFRAS))["costo"]
    rep = {to: D(v["e1"]) + D(v["e3"]) for to, v in man["limites"]["estimado_usd"].items()}
    pl = {to: D(plano[to]["total_usd"]) for to in plano}
    filas = []
    for to in t1:
        g = D(rs["por_to"][to]["gasto_usd"])
        filas.append([to, q(g, 6), q(pl[to], 6), q(g / pl[to]), q(rep[to], 6), q(g / rep[to])])
    e_pl1, e_rep1 = sum(pl[t] for t in t1), sum(rep[t] for t in t1)
    e_pl2, e_rep2 = sum(pl[t] for t in t2), sum(rep[t] for t in t2)
    lineas1 = e_pl1 - D(601) * D("0.021115")
    tope = D(man["limites"]["tope_global_usd"])
    gg = D(rs["gasto_global_usd"])
    out["costo"] = {"gasto_tramo_1_usd": str(gasto_t1), "gasto_global_usd": str(gg),
                    "tramo_1_estimado_s3_usd": cif["tramo_1_estimado"], "lineas_de_alcance_tramo_1_usd": str(lineas1),
                    "tramo_1_estimado_s3_mas_lineas_usd": str(e_pl1), "tramo_1_estimado_reparto_usd": str(e_rep1),
                    "gasto_sobre_s3_mas_lineas": q(gasto_t1 / e_pl1), "gasto_sobre_reparto": q(gasto_t1 / e_rep1),
                    "tramo_2_estimado_s3_mas_lineas_usd": str(e_pl2), "tramo_2_estimado_reparto_usd": str(e_rep2),
                    "total_estimado_usd": str(sum(rep.values())), "gasto_sobre_total_estimado": q(gg / sum(rep.values())),
                    "tope_usd": str(tope), "gasto_sobre_tope": q(gg / tope), "margen_al_tope_usd": q(tope - gg, 6),
                    "por_to_real_sobre_s3_min_max": [min(filas, key=lambda f: D(f[3]))[0:4:3], max(filas, key=lambda f: D(f[3]))[0:4:3]],
                    "por_to_real_sobre_reparto_min_max": [min(filas, key=lambda f: D(f[5]))[0:6:5], max(filas, key=lambda f: D(f[5]))[0:6:5]]}
    tabla("5. El costo del tramo 1 por TO: real contra el estimado del §3 (tarifa más líneas de alcance) y contra el repartido",
          ["TO", "gasto real", "§3 + líneas", "real / §3", "repartido", "real / repartido"], filas)
    c = out["costo"]
    tabla("6. El costo: totales", ["cifra", "valor"],
          [["gasto real del tramo 1 (suma por TO, resumen_t2)", c["gasto_tramo_1_usd"]], ["gasto global (estado del runner)", c["gasto_global_usd"]],
           ["tramo 1, estimado del §3 (601 × 0,021115)", c["tramo_1_estimado_s3_usd"]], ["tramo 1, líneas de alcance de A3", c["lineas_de_alcance_tramo_1_usd"]],
           ["tramo 1, §3 más las líneas", c["tramo_1_estimado_s3_mas_lineas_usd"]], ["tramo 1, real / (§3 más las líneas)", c["gasto_sobre_s3_mas_lineas"]],
           ["tramo 1, estimado repartido (manifiesto)", c["tramo_1_estimado_reparto_usd"]], ["tramo 1, real / repartido", c["gasto_sobre_reparto"]],
           ["tramo 2, §3 más las líneas y repartido (sin correr)", f"{c['tramo_2_estimado_s3_mas_lineas_usd']} y {c['tramo_2_estimado_reparto_usd']}"],
           ["total estimado (USD 104,7498) y gasto global / total", f"{c['total_estimado_usd']} y {c['gasto_sobre_total_estimado']}"],
           ["tope, gasto global / tope y margen", f"{c['tope_usd']}, {c['gasto_sobre_tope']} y {c['margen_al_tope_usd']}"],
           ["por TO, real / §3: mínimo y máximo", f"{c['por_to_real_sobre_s3_min_max'][0]} y {c['por_to_real_sobre_s3_min_max'][1]}"],
           ["por TO, real / repartido: mínimo y máximo", f"{c['por_to_real_sobre_reparto_min_max'][0]} y {c['por_to_real_sobre_reparto_min_max'][1]}"]])

    # 7. la duración
    es = leer(Path(ESTIM))["duracion"]
    out["duracion"] = {"lanzamientos_min": dur, "tramo_1_proyectado_por_unidades_min": es["por_unidades"]["tramo_1"]["min"],
                       "tramo_1_proyectado_por_caracteres_min": es["por_caracteres_informacion"]["tramo_1"]["min"],
                       "tanda_proyectada_por_unidades_min": es["por_unidades"]["min"],
                       "tanda_proyectada_por_caracteres_min": es["por_caracteres_informacion"]["min"],
                       "suma_de_los_to_min": round(sum(f[4] for f in out["por_to_avance"]), 1)}
    d = out["duracion"]
    tabla("7. La duración", ["cifra", "valor"],
          [["lanzamiento (inicio_lanzador a fin_lanzador, min)", dur], ["suma de los TOs (to_inicio a to_fin, min)", d["suma_de_los_to_min"]],
           ["tramo 1 proyectado por unidades y por caracteres (min)", f"{d['tramo_1_proyectado_por_unidades_min']} y {d['tramo_1_proyectado_por_caracteres_min']}"],
           ["la tanda proyectada por unidades y por caracteres (min)", f"{d['tanda_proyectada_por_unidades_min']} y {d['tanda_proyectada_por_caracteres_min']}"]])

    # 8. la foto del repo
    cm = leer(a.comparacion)
    fa_, fd_ = leer(a.foto_antes), leer(a.foto_despues)
    g = lambda kk: next((p for p in CARPETAS if kk.startswith(p)), "otra ruta")  # noqa: E731
    out["foto"] = {"antes": {x: fa_[x] for x in ("inicio", "fin", "n", "sin_abrir", "enlaces")},
                   "despues": {x: fd_[x] for x in ("inicio", "fin", "n", "sin_abrir", "enlaces")},
                   **{c_: dict(Counter(g(kk) for kk in cm[c_])) for c_ in ("nuevos", "borrados", "cambiados")}}
    tabla("8. La foto del repo: antes, después y lo que cambia, por carpeta", ["cifra", "valor"],
          [["antes (inicio, fin, entradas, sin abrir, enlaces)", list(out["foto"]["antes"].values())],
           ["después (inicio, fin, entradas, sin abrir, enlaces)", list(out["foto"]["despues"].values())],
           ["nuevos", out["foto"]["nuevos"]], ["borrados", out["foto"]["borrados"]], ["cambiados", out["foto"]["cambiados"]]])

    a.md.write_text("# Cifras del FRENO T2 de la tanda final (las genera freno_t2_cifras.py)\n" + "\n".join(md) + "\n", encoding="utf-8")
    a.json.write_text(json.dumps(out, ensure_ascii=False, indent=1, default=str) + "\n", encoding="utf-8")
    print(f"{a.md.name}: {len(md)} renglones; {a.json.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
