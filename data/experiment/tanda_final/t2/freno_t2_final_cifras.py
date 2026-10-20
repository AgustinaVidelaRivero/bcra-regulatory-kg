"""
freno_t2_final_cifras.py — B6.1, tanda final, T2: las cifras y las tablas del FRENO T2 final, con los dos lanzamientos (pre-registro
firmado de la tanda final, §7: «toda cifra del FRENO sale por script»). USD 0, sin API. Solo lee (git solo con `log` y
`ls-files`); escribe --md y --json. No abre ningún NO_ABRIR_ ni la salida del runner. El del FRENO T2 parcial 1
(`freno_t2_cifras.py`) queda como estaba, con sus salidas.

Fuentes (relativas a --repo, salvo los logs y las fotos):
  - data/experiment/tanda_final/t2/avance_t2.jsonl: los dos lanzamientos, por TO (tramo, inicio, fin, código, freno por modelo
    con sus ids, gasto global) y los dos controles entre tramos;
  - --resumen (resumen_t2_final.json): las unidades, las aceptadas, la cola, los errores, los ids repetidos, la cobertura y el
    gasto por TO;
  - el manifiesto (el estimado repartido), data/experiment/tanda_final/t1/seco/estimado_por_to_t1.json (el plano: la tarifa del
    §3 más las líneas de alcance de A3), salida_cifras_preregistro_tanda_final.json (el §3 por tramo) y las estimaciones de T1;
  - --log (dos veces): la salida de pantalla de cada lanzamiento, con el renglón `rc=`;
  - --foto-antes, --foto-despues y --comparacion: solo cuentas por carpeta; las rutas que no son de T2 se atribuyen a los commits
    de la autora entre --head-antes y HEAD (`git log -- <ruta>`), o se declaran sin commit.
Uso: python3 -I -B freno_t2_final_cifras.py --repo <raíz> --resumen <json> --log <l1> --log <l2> --foto-antes <json>
       --foto-despues <json> --comparacion <json> --head-antes <commit> --md <md> --json <json>
"""
from __future__ import annotations

import argparse
import json
import subprocess
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
MIAS = ("data/experiment/reextraccion_v2/corpus_tanda_final/", "data/experiment/tanda_final/t2/",
        "data/experiment/reextraccion_v2/e1_extractor/cache/", "data/experiment/reextraccion_v2/e3_verificador/cache/",
        "logs/cache_usage.jsonl", "data/experiment/neo4j/volumen/")
D = lambda x: Decimal(str(x))  # noqa: E731
q = lambda x, n=4: str(D(x).quantize(Decimal(1).scaleb(-n), ROUND_HALF_UP))  # noqa: E731
ts = lambda s: datetime.strptime(s, "%Y-%m-%dT%H:%M:%S%z")  # noqa: E731


def main() -> int:
    ap = argparse.ArgumentParser()
    for k in ("--repo", "--resumen", "--foto-antes", "--foto-despues", "--comparacion", "--md", "--json"):
        ap.add_argument(k, type=Path, required=True)
    ap.add_argument("--log", type=Path, action="append", required=True)
    ap.add_argument("--head-antes", required=True)
    a = ap.parse_args()
    r = a.repo.resolve()
    leer = lambda p: json.loads((p if Path(p).is_absolute() else r / p).read_text(encoding="utf-8"))  # noqa: E731
    git = lambda *x: subprocess.run(["git", "-C", str(r), *x], capture_output=True, text=True, check=True).stdout  # noqa: E731
    md, out = [], {}

    def tabla(t, cab, filas):
        md.append(f"\n### {t}\n")
        md.append("| " + " | ".join(cab) + " |")
        md.append("|" + "|".join("---" for _ in cab) + "|")
        md.extend("| " + " | ".join(str(x) for x in f) + " |" for f in filas)

    # el registro, partido por lanzamiento
    ev = [json.loads(x) for x in (r / T2 / "avance_t2.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
    lanz, cur = [], None
    for e in ev:
        if e["evento"] == "inicio_lanzador":
            cur = []
            lanz.append(cur)
        cur.append(e)
    rcs = [next(x for x in p.read_text(encoding="utf-8").splitlines() if x.startswith("rc=")) for p in a.log]

    # 1. los lanzamientos
    filas = []
    for n, L in enumerate(lanz):
        ini = L[0]
        fin = next(e for e in L if e["evento"] == "fin_lanzador")
        cp = next(e for e in L if e["evento"] == "controles_previos")
        fa = next(e for e in L if e["evento"] == "freno_modelo_antes")
        filas.append([n + 1, ini["ts"], ini["pid"], fin["ts"], round((ts(fin["ts"]) - ts(ini["ts"])).total_seconds() / 60, 1),
                      rcs[n] if n < len(rcs) else "—", f"autorizado_tramo_2={ini['autorizado_tramo_2']}, retomar_tras_pausa="
                      f"{ini['retomar_tras_pausa']}, stub={ini['stub']}", f"{cp['ok']} ({', '.join(cp['rutas_78'])}; SDK {cp['sdk']}; "
                      f"sha256 {cp['manifiesto_sha256_ok']}; tope {cp['tope_ok']})", f"{fa['resultado']} {fa['ids_e1']} {fa['ids_e3']}",
                      "; ".join(e["motivo"] for e in L if e["evento"] == "parada") or "—", fin["copia_de_trabajo_borrada"]])
    out["lanzamientos"] = filas
    tabla("1. Los lanzamientos", ["#", "inicio", "pid", "fin", "minutos", "salida", "opciones", "controles previos",
                                  "freno antes", "parada", "copia de trabajo borrada"], filas)

    # 2. por TO, del registro: los 98 que corrieron y la pasada del lanzamiento 2 por el tramo 1
    efect, pasada = [], []
    for n, L in enumerate(lanz):
        for e in L:
            if e["evento"] != "to_fin":
                continue
            fila = [n + 1, e["to"], e["tramo"], e["inicio"][:19].replace("T", " "), e["fin"][11:19],
                    round((ts(e["fin"]) - ts(e["inicio"])).total_seconds() / 60, 1), e["rc"], e["freno_modelo"],
                    ", ".join(e["ids_e1"]), ", ".join(e["ids_e3"]), e["gasto_global_usd"]]
            (pasada if (n == 1 and e["tramo"] == 1) else efect).append(fila)
    out["por_to"] = {"corridos": len(efect), "pasada_lanzamiento_2_tramo_1": len(pasada)}
    tabla("2. Por TO, del registro de avance: los 98 que corrieron", ["lanz.", "TO", "tramo", "inicio", "fin", "min", "rc", "freno",
                                                                     "ids E1", "ids E3", "gasto global USD"], efect)
    gpas = sorted({f[10] for f in pasada})
    md.append(f"\nLa pasada del lanzamiento 2 por el tramo 1: {len(pasada)} TOs, rc {sorted({f[6] for f in pasada})}, freno "
              f"{sorted({f[7] for f in pasada})}, gasto global {gpas} (sin gasto nuevo), de {pasada[0][3]} a {pasada[-1][4]}.")

    # 3. los controles entre tramos
    cts = [(n + 1, e) for n, L in enumerate(lanz) for e in L if e["evento"] == "control_entre_tramos"]
    out["controles_entre_tramos"] = [{"lanzamiento": n, "ts": e["ts"], "rc": e["rc"], "resultado": e["resultado"], "salida": e["salida"]} for n, e in cts]
    tabla("3. Los controles entre tramos", ["lanz.", "hora", "rc", "resultado", "salida", "control sha256"],
          [[n, e["ts"], e["rc"], e["resultado"], " / ".join(e["salida"]), e["control_sha256"][:12] + "…"] for n, e in cts])

    # 4. resumen_t2 por TO y por tramo
    rs = leer(a.resumen)
    man = leer(MAN)
    tramos = {"tramo 1": man["orden_corrida"][:30], "tramo 2": man["orden_corrida"][30:]}
    k = ("unidades", "unidades_con_partes", "aceptadas", "cola", "errores", "sin_destino", "ids_repetidos")
    filas = []
    for tn, tos in tramos.items():
        for to in tos:
            f = rs["por_to"][to]
            filas.append([to, tn] + [f[x] for x in k] + [f["cobertura_completa"], f["cobertura_exacta_e0"], f["fases_cerradas"], f["gasto_usd"]])
    tot = {tn: {x: sum(rs["por_to"][t][x] for t in tos) for x in k} | {"gasto_usd": str(sum(D(rs["por_to"][t]["gasto_usd"]) for t in tos))}
           for tn, tos in tramos.items()}
    out["resumen"] = {"por_tramo": tot, "total": rs["total"], "gasto_global_usd": rs["gasto_global_usd"], "tope_usd": rs["tope_usd"],
                      "dentro_del_tope": rs["dentro_del_tope"],
                      "lineas_del_runner": dict(Counter(x["linea"].split(":")[0] for x in rs["lineas_del_runner"]))}
    tabla("4. resumen_t2.py por TO", ["TO", "tramo"] + list(k) + ["cobertura", "cobertura E0", "fases cerradas", "gasto USD"],
          filas + [[f"total del {tn}", ""] + [v[x] for x in k] + ["", "", "", v["gasto_usd"]] for tn, v in tot.items()]
          + [["total", ""] + [rs["total"][x] for x in k] + ["", "", rs["total"]["tos_cerrados"], rs["total"]["gasto_por_to_sumado_usd"]]])

    # 5 y 6. el costo
    plano = {to: D(v["total_usd"]) for to, v in leer(PLANO)["por_to"].items()}
    rep = {to: D(v["e1"]) + D(v["e3"]) for to, v in man["limites"]["estimado_usd"].items()}
    cif = leer(CIFRAS)["costo"]
    filas = []
    for tn, tos in tramos.items():
        for to in tos:
            g = D(rs["por_to"][to]["gasto_usd"])
            filas.append([to, tn, q(g, 6), q(plano[to], 6), q(g / plano[to]), q(rep[to], 6), q(g / rep[to])])
    tabla("5. El costo por TO: real contra el §3 más las líneas de alcance y contra el repartido",
          ["TO", "tramo", "gasto real", "§3 + líneas", "real / §3", "repartido", "real / repartido"], filas)
    costo, cfilas = {}, []
    s3 = {"tramo 1": D(cif["tramo_1_estimado"]), "tramo 2": D(cif["tramo_2_estimado"])}
    tarifa = D(cif["tarifa"])
    for tn, tos in tramos.items():
        g = sum(D(rs["por_to"][t]["gasto_usd"]) for t in tos)
        pl, rp = sum(plano[t] for t in tos), sum(rep[t] for t in tos)
        u = sum(rs["por_to"][t]["unidades"] for t in tos)
        ut = u * tarifa
        costo[tn] = {"gasto": str(g), "s3_del_preregistro": str(s3[tn]), "u_por_tarifa": str(ut), "lineas": str(pl - ut),
                     "s3_mas_lineas": str(pl), "real_sobre_s3_mas_lineas": q(g / pl), "repartido": str(rp), "real_sobre_repartido": q(g / rp)}
        cfilas.append([tn, q(g, 6), str(s3[tn]), q(ut, 6), q(pl - ut, 6), q(pl, 6), q(g / pl), q(rp, 6), q(g / rp)])
    gt = sum(D(rs["por_to"][t]["gasto_usd"]) for t in man["orden_corrida"])
    plt, rpt = sum(plano.values()), sum(rep.values())
    gg, tope = D(rs["gasto_global_usd"]), D(man["limites"]["tope_global_usd"])
    s3t = D(cif["estimado"])
    utt = D(cif["U"]) * tarifa
    costo["total"] = {"gasto_por_to": str(gt), "gasto_global": str(gg), "s3_del_preregistro": str(s3t), "u_por_tarifa": str(utt),
                      "lineas": str(plt - utt), "s3_mas_lineas": str(plt), "real_sobre_s3_mas_lineas": q(gg / plt),
                      "repartido": str(rpt), "real_sobre_repartido": q(gg / rpt), "estimado_104_7498": q(plt), "tope": str(tope),
                      "gasto_sobre_tope": q(gg / tope), "margen_al_tope": q(tope - gg, 6)}
    cfilas.append(["total", q(gg, 6), str(s3t), q(utt, 6), q(plt - utt, 6), q(plt, 6), q(gg / plt), q(rpt, 6), q(gg / rpt)])
    out["costo"] = costo
    tabla("6. El costo por tramo y total (el §3 del pre-registro va redondeado a cuatro decimales; las líneas de A3 se restan de U × "
          "tarifa exacto)", ["", "gasto real", "§3 del pre-registro", "U × tarifa", "líneas de A3", "§3 + líneas", "real / (§3 + líneas)",
                             "repartido", "real / repartido"], cfilas)
    md.append(f"\nContra el tope de USD {tope}: {q(gg / tope)} del tope, con un margen de {q(tope - gg, 6)}. El gasto por TO sumado da "
              f"{q(gt, 6)} y el global del runner, {q(gg, 6)}.")
    rat = [(f[0], D(f[4])) for f in filas]
    rr = [(f[0], D(f[6])) for f in filas]
    md.append(f"\nPor TO, real / (§3 + líneas): de {min(rat, key=lambda x: x[1])} a {max(rat, key=lambda x: x[1])}; real / repartido: de "
              f"{min(rr, key=lambda x: x[1])} a {max(rr, key=lambda x: x[1])}.")

    # 7. la duración
    es = leer(ESTIM)["duracion"]
    dur = [f[4] for f in out["lanzamientos"]]
    por_tramo_real = {tn: round(sum(f[5] for f in efect if f[2] == (1 if tn == "tramo 1" else 2)), 1) for tn in tramos}
    out["duracion"] = {"lanzamientos_min": dur, "suma_min": round(sum(dur), 1), "por_tramo_suma_de_los_TO_min": por_tramo_real,
                       "proyectado_unidades": {"total": es["por_unidades"]["min"], "tramo 1": es["por_unidades"]["tramo_1"]["min"],
                                               "tramo 2": es["por_unidades"]["tramo_2"]["min"]},
                       "proyectado_caracteres": {"total": es["por_caracteres_informacion"]["min"],
                                                 "tramo 1": es["por_caracteres_informacion"]["tramo_1"]["min"],
                                                 "tramo 2": es["por_caracteres_informacion"]["tramo_2"]["min"]}}
    d = out["duracion"]
    tabla("7. La duración", ["", "real (min)", "proyectado por unidades (min)", "proyectado por caracteres (min)"],
          [["tramo 1 (suma de sus TOs, lanzamiento 1)", d["por_tramo_suma_de_los_TO_min"]["tramo 1"], d["proyectado_unidades"]["tramo 1"], d["proyectado_caracteres"]["tramo 1"]],
           ["tramo 2 (suma de sus TOs, lanzamiento 2)", d["por_tramo_suma_de_los_TO_min"]["tramo 2"], d["proyectado_unidades"]["tramo 2"], d["proyectado_caracteres"]["tramo 2"]],
           ["los dos lanzamientos, de inicio a fin", f"{dur} → {d['suma_min']}", d["proyectado_unidades"]["total"], d["proyectado_caracteres"]["total"]]])
    fin1 = next(e for e in lanz[0] if e["evento"] == "fin_lanzador")["ts"]
    ini2 = lanz[1][0]["ts"] if len(lanz) > 1 else None
    if ini2:
        entre = (ts(ini2) - ts(fin1)).total_seconds()
        pas = [e for e in lanz[1] if e["evento"] in ("to_inicio", "to_fin") and e.get("tramo") == 1]
        pas_min = round((ts(pas[-1]["fin"]) - ts(pas[0]["inicio"])).total_seconds() / 60, 2) if pas else None
        out["duracion"].update({"entre_lanzamientos_s": int(entre), "pasada_tramo_1_lanzamiento_2_min": pas_min})
        md.append(f"\nEntre el fin del lanzamiento 1 ({fin1}) y el inicio del 2 ({ini2}): {int(entre) // 3600} h {int(entre) % 3600 // 60} min "
                  f"{int(entre) % 60} s, que no cuentan. La pasada del lanzamiento 2 por el tramo 1: {pas_min} min.")

    # 8. la foto
    cm = leer(a.comparacion)
    fa_, fd_ = leer(a.foto_antes), leer(a.foto_despues)
    rango = f"{a.head_antes}..HEAD"
    commits = [x.split(" ", 1) for x in git("log", "--format=%h %s", rango).splitlines()]

    def atribuir(ruta):
        h = git("log", "--format=%h", rango, "--", ruta).split()
        if h:
            return "commit " + ", ".join(h)
        return "rastreado sin commit en el período" if git("ls-files", "--", ruta).strip() else "sin rastrear y sin commit"
    clase = lambda kk: next((p for p in MIAS if kk.startswith(p)), None)  # noqa: E731
    ajenas = {c_: sorted(kk for kk in cm[c_] if clase(kk) is None) for c_ in ("nuevos", "borrados", "cambiados")}
    atrib = {c_: {kk: atribuir(kk) for kk in v} for c_, v in ajenas.items()}
    out["foto"] = {"antes": {x: fa_[x] for x in ("inicio", "fin", "n", "sin_abrir", "enlaces")},
                   "despues": {x: fd_[x] for x in ("inicio", "fin", "n", "sin_abrir", "enlaces")},
                   **{c_: dict(Counter(clase(kk) or "de los commits de la autora u otra unidad" for kk in cm[c_])) for c_ in ("nuevos", "borrados", "cambiados")},
                   "commits": commits, "ajenas_por_commit": {c_: dict(Counter(v.values())) for c_, v in atrib.items()},
                   "ajenas_sin_commit": {c_: sorted(kk for kk, v in vv.items() if not v.startswith("commit")) for c_, vv in atrib.items()}}
    f = out["foto"]
    tabla("8. La foto del repo: antes, después y lo que cambia", ["cifra", "valor"],
          [["antes (inicio, fin, entradas, sin abrir, enlaces)", list(f["antes"].values())],
           ["después (inicio, fin, entradas, sin abrir, enlaces)", list(f["despues"].values())],
           ["nuevos, por carpeta", f["nuevos"]], ["borrados", f["borrados"]], ["cambiados, por carpeta", f["cambiados"]],
           ["commits de la autora en el período", len(commits)],
           ["rutas ajenas a T2, por commit (nuevas)", f["ajenas_por_commit"]["nuevos"]],
           ["rutas ajenas a T2, por commit (cambiadas)", f["ajenas_por_commit"]["cambiados"]],
           ["rutas ajenas a T2 sin commit", f["ajenas_sin_commit"]]])
    tabla("8b. Los commits de la autora durante T2", ["hash", "asunto"], commits)

    a.md.write_text("# Cifras del FRENO T2 final de la tanda final (las genera freno_t2_final_cifras.py)\n" + "\n".join(md) + "\n", encoding="utf-8")
    a.json.write_text(json.dumps(out, ensure_ascii=False, indent=1, default=str) + "\n", encoding="utf-8")
    print(f"{a.md.name}: {len(md)} renglones; {a.json.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
