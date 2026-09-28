"""U-ESTUDIO-MATRIZ, paso 3 — muestra de 60 relaciones rechazadas para juicio
de la autora (solo lectura, sin API).

Población: los 982 rechazos firma_invalida de E1 (reports/u_audit_tipos_v3/
p4_filas.json), restringida a los pares candidatos (n >= 10 en p4_resumen).
Estratos: un estrato por par candidato.
Asignación: proporcional a la frecuencia con mínimo 5 por estrato —
  iterativa: se calcula la cuota proporcional sobre el total restante; los
  estratos con cuota < 5 quedan fijos en 5 y se recalcula sobre el resto
  hasta que ninguno quede por debajo; redondeo por restos mayores,
  desempate por n descendente y luego por el nombre del par.
Sorteo: por estrato, lista ordenada por (to, chunk_id, idx) y
  random.Random(20260928).sample(lista, k) — una instancia nueva con la misma
  semilla por estrato (el resultado no depende del orden de los estratos).
Orden de filas: estratos por n descendente; dentro de cada estrato, las
  filas sorteadas por (to, chunk_id, idx); ids M01..M60 en ese orden.
CSV (UTF-8 con BOM, para planillas): id de muestra, par, chunk_id, texto del
  fragmento de E0 (herencia + texto propio, verificado contra sha256_completo),
  entidad origen y destino tal como las emitió el extractor (tipo, etiqueta,
  descripcion de properties), predicado, y columnas vacías veredicto y nota.
  Para el extremo Sujeto de aplica_a el extractor emite solo un id de catálogo
  (o un sujeto_propuesto): se transcribe ese valor como etiqueta y la
  descripción queda vacía. Ninguna columna anticipa el veredicto.
Salidas: uestmat_muestra_60.csv, uestmat_paso3_muestra.json (procedimiento,
  conteos por estrato y la clave to/linea/idx de cada fila, para trazar).
"""
from __future__ import annotations

import csv
import json
import math
import random
from pathlib import Path

import uestmat_comun as U

OUT = Path("/tmp/u_estudio_matriz")
SEMILLA = 20260928
N_MUESTRA = 60
MINIMO = 5


def par_str(s, p, t):
    return f"{s} --{p}--> {t}"


def asignar(n_por_estrato: dict[str, int], total: int, minimo: int) -> tuple[dict[str, int], list[dict]]:
    fijos: set[str] = set()
    traza = []
    while True:
        libres = [h for h in n_por_estrato if h not in fijos]
        resto = total - minimo * len(fijos)
        suma = sum(n_por_estrato[h] for h in libres)
        cuota = {h: resto * n_por_estrato[h] / suma for h in libres}
        bajos = [h for h in libres if cuota[h] < minimo]
        traza.append({"fijos_en_minimo": len(fijos), "total_a_repartir": resto,
                      "cuotas": {h: round(q, 4) for h, q in cuota.items()}})
        if not bajos:
            break
        fijos.update(bajos)
    asig = {h: minimo for h in fijos}
    base = {h: math.floor(cuota[h]) for h in libres}
    faltan = resto - sum(base.values())
    orden = sorted(libres, key=lambda h: (-(cuota[h] - base[h]), -n_por_estrato[h], h))
    for h in orden[:faltan]:
        base[h] += 1
    asig.update(base)
    assert sum(asig.values()) == total and all(v >= minimo for v in asig.values())
    return asig, traza


def main() -> None:
    p4 = json.loads((U.AUDIT / "p4_resumen.json").read_text(encoding="utf-8"))
    filas = json.loads((U.AUDIT / "p4_filas.json").read_text(encoding="utf-8"))
    cand = sorted(((x["origen"], x["predicado"], x["destino"], x["n"]) for x in p4["por_par"] if x["n"] >= 10),
                  key=lambda x: (-x[3], x[0], x[1], x[2]))
    n_por = {par_str(s, p, t): n for s, p, t, n in cand}
    estratos = {h: [] for h in n_por}
    for f in filas:
        h = par_str(f["origen"], f["predicado"], f["destino"])
        if h in estratos:
            estratos[h].append(f)
    for h, lista in estratos.items():
        assert len(lista) == n_por[h], h
        lista.sort(key=lambda f: (f["to"], f["chunk_id"], f["idx"]))
        claves = [(f["to"], f["chunk_id"], f["idx"]) for f in lista]
        assert len(set(claves)) == len(claves), f"clave (to, chunk_id, idx) repetida en {h}"

    asig, traza = asignar(n_por, N_MUESTRA, MINIMO)

    e1 = {to: U.leer_jsonl(U.SALIDA / to / "extracciones_e1.jsonl") for to in U.TOS_10}
    chunks = {to: {c["id"]: c for c in U.cargar_chunks(to)} for to in U.TOS_10}
    labels_cat = U.perfil_v3().labels_catalogo

    filas_csv = []
    traza_filas = []
    n_id = 0
    for h in n_por:
        sel = random.Random(SEMILLA).sample(estratos[h], asig[h])
        sel.sort(key=lambda f: (f["to"], f["chunk_id"], f["idx"]))
        for f in sel:
            n_id += 1
            d = e1[f["to"]][f["linea"] - 1]
            assert d["chunk_id"] == f["chunk_id"]
            cr = d["tool_input_crudo"]
            rel = cr["relations"][f["idx"]]
            ents = {e["local_id"]: e for e in cr["entities"]}
            src = ents[rel["source"]]
            if f["predicado"] == "aplica_a":
                sid = rel.get("sujeto_id") or rel.get("sujeto_propuesto")
                dst = {"type": "Sujeto", "label": sid, "properties": {}}
                assert rel.get("sujeto_id") is None or rel["sujeto_id"] in labels_cat
            else:
                dst = ents[rel["target"]]
            assert (src["type"], rel["predicate"], dst["type"]) == (f["origen"], f["predicado"], f["destino"])
            ch = chunks[f["to"]][f["chunk_id"]]
            mid = f"M{n_id:02d}"
            filas_csv.append({
                "id_muestra": mid,
                "par": h,
                "chunk_id": f["chunk_id"],
                "texto_fragmento_e0": U.texto_completo(ch),
                "origen_tipo": src["type"],
                "origen_etiqueta": src.get("label", ""),
                "origen_descripcion": (src.get("properties") or {}).get("descripcion", ""),
                "predicado": rel["predicate"],
                "destino_tipo": dst["type"],
                "destino_etiqueta": dst.get("label", ""),
                "destino_descripcion": (dst.get("properties") or {}).get("descripcion", ""),
                "veredicto": "",
                "nota": "",
            })
            traza_filas.append({"id_muestra": mid, "par": h, "to": f["to"], "linea_e1": f["linea"],
                                "chunk_id": f["chunk_id"], "idx": f["idx"]})

    campos = list(filas_csv[0].keys())
    with open(OUT / "uestmat_muestra_60.csv", "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=campos, quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(filas_csv)

    res = {
        "unidad": "U-ESTUDIO-MATRIZ",
        "poblacion": "reports/u_audit_tipos_v3/p4_filas.json (982 rechazos firma_invalida de E1, 10 TOs)",
        "estratos": "pares candidatos (n >= 10 en p4_resumen.json)",
        "poblacion_en_estratos": sum(n_por.values()),
        "semilla": SEMILLA,
        "procedimiento": ("por estrato: lista ordenada por (to, chunk_id, idx); "
                          "random.Random(20260928).sample(lista, k), instancia nueva por estrato"),
        "asignacion": "proporcional con mínimo 5, iterativa, restos mayores",
        "traza_asignacion": traza,
        "conteos_por_estrato": [{"par": h, "n_poblacion": n_por[h], "n_muestra": asig[h]} for h in n_por],
        "total_muestra": sum(asig.values()),
        "columnas_csv": campos,
        "filas": traza_filas,
    }
    (OUT / "uestmat_paso3_muestra.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    for c in res["conteos_por_estrato"]:
        print(c)
    print("total", res["total_muestra"])


if __name__ == "__main__":
    main()
