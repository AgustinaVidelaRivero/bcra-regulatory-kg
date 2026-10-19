"""
05_controles.py — U-TRIP-V, paso h: los controles, recomputados desde el grafo y la E0 de la copia (no desde las salidas
de los pasos anteriores, salvo el acta, que es lo que se controla).

  1. El sorteo se reproduce con la semilla: la población recomputada desde el kg.json da el sha256 sellado, la asignación
     recomputada da los mismos n_h, y las 100, el pool, el orden y los lotes dan los mismos sha256.
  2. Cada procedencia de las 120 está en la E0 (la unidad, con el mismo TO, archivo y páginas) y cada página (de la
     procedencia y de lo heredado) existe en su PDF (`pdfinfo`, Pages).
  3. Ninguna ficha trae vacío un campo que la evidencia tenga: descripción, propiedades conservadas, texto propio,
     heredado, páginas, tramos de cada extremo en la unidad, tramo del sujeto y calificador.
  4. Las 100 y el pool son disjuntos.
  5. Controles negativos: ninguna ficha trae una clave de la lista de marcas o de juicio (comun_v.CLAVES_PROHIBIDAS); el
     orden de las horas es asignación < sorteo ≤ sello < fichas; las hojas vacías tienen las filas del lote sellado y
     ninguna celda de juicio llena.
  python3 -I -B 05_controles.py --copia <copia> --raiz <tripletas_v> --salida <json>
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import io
import json
import random
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun_v as V  # noqa: E402

spec = importlib.util.spec_from_file_location("pob", Path(__file__).resolve().parent / "01_poblacion_asignacion.py")
POB = importlib.util.module_from_spec(spec)
spec.loader.exec_module(POB)


def claves_en(x, acc: set):
    if isinstance(x, dict):
        for k, v in x.items():
            acc.add(k)
            claves_en(v, acc)
    elif isinstance(x, list):
        for v in x:
            claves_en(v, acc)
    return acc


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--copia", type=Path, required=True)
    ap.add_argument("--raiz", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    R = a.raiz
    res: dict = {"hora": V.hora()}
    acta_p, sello_p = R / "salidas" / "acta_sorteo_V.json", R / "salidas" / "sello_sorteo_V.txt"
    s_acta = V.sha_archivo(acta_p)
    sello = sello_p.read_text(encoding="utf-8").split()
    acta = json.loads(acta_p.read_text(encoding="utf-8"))
    so = acta["sorteo"]
    res["0_sello"] = {"acta_sha256": s_acta, "sello": sello[0], "ok": s_acta == sello[0]}

    # 1. reproducción
    kg, s_kg = V.cargar_kg(a.copia)
    cont = [e for e in kg["edges"] if e["relation"] in V.CONTENIDO]
    N_pred = {p: sum(1 for e in cont if e["relation"] == p) for p in V.CONTENIDO}
    est = {p: (p if N_pred[p] >= V.UMBRAL_ESTRATO else V.ESTRATO_OTROS) for p in V.CONTENIDO}
    filas = sorted([[V.clave(e), e["relation"], est[e["relation"]], [p["chunk_id"] for p in e["provenances"]],
                     [p["to"] for p in e["provenances"]]] for e in cont], key=lambda f: f[0])
    N_h = {h: sum(1 for f in filas if f[2] == h) for h in acta["asignacion"]["n"]}
    asign, _, _ = POB.asignar(N_h, V.N_MUESTRA)
    por_e: dict = {}
    for f in filas:
        por_e.setdefault(f[2], []).append(f[0])
    muestra = {h: random.Random(f"{V.SEMILLA}:{h}").sample(sorted(por_e[h]), asign[h]) for h in asign}
    en = {k for v in muestra.values() for k in v}
    pool = random.Random(f"{V.SEMILLA}:pool").sample(sorted(f[0] for f in filas if f[0] not in en), V.N_POOL)
    orden = sorted(en)
    random.Random(f"{V.SEMILLA}:orden").shuffle(orden)
    lotes = {"piloto": orden[:V.N_PILOTO]} | {f"lote_{i + 1:02d}": orden[V.N_PILOTO + i * 10: V.N_PILOTO + (i + 1) * 10]
                                              for i in range(V.N_LOTES)}
    rep = {"kg_sha256": s_kg == acta["grafo"]["sha256"],
           "poblacion_sha256_lista": V.sha(V.canon(filas)) == acta["poblacion"]["sha256_lista"],
           "poblacion_filas_iguales_al_acta": filas == acta["poblacion"]["filas"],
           "asignacion": asign == acta["asignacion"]["n"],
           "muestra": V.sha(V.canon(muestra)) == so["sha256_muestra"],
           "pool": V.sha(V.canon(pool)) == so["sha256_pool"],
           "orden": V.sha(V.canon(orden)) == so["sha256_orden"],
           "lotes": V.sha(V.canon(lotes)) == so["sha256_lotes"]}
    res["1_reproduccion"] = {**rep, "ok": all(rep.values())}

    # fichas
    fichas = [json.loads(x) for x in (R / "fichas" / "fichas_V.jsonl").read_text(encoding="utf-8").splitlines() if x]
    cab = json.loads((R / "fichas" / "fichas_V_cabecera.json").read_text(encoding="utf-8"))
    claves_f = [f["clave"] for f in fichas]
    res["fichas"] = {"n": len(fichas), "en_el_orden_sellado": claves_f == orden + pool,
                     "cabecera_acta": cab["acta_sorteo_V.json_sha256"] == s_acta,
                     "jsonl_sha256": V.sha_archivo(R / "fichas" / "fichas_V.jsonl") == cab["fichas_V.jsonl_sha256"]}

    # 2. E0 y PDF
    e0 = {to: V.chunks_e0(a.copia, to) for to in V.TOS_V}
    paginas_pdf = {}
    for p in sorted((a.copia / V.PDF_DIR_REL).glob("*.pdf")):
        info = subprocess.run(["pdfinfo", str(p)], capture_output=True, text=True, check=True).stdout
        paginas_pdf[p.name] = int(re.search(r"^Pages:\s+(\d+)", info, re.M).group(1))
    aristas = {V.clave(e): e for e in cont}
    problemas_e0, problemas_pdf, n_herencia, n_proc, n_pag = [], [], [], 0, 0
    for k in orden + pool:
        for p in aristas[k]["provenances"]:
            n_proc += 1
            base = V.base_chunk(p["chunk_id"])
            c = e0.get(p["to"], {}).get(base)
            if c is None:
                problemas_e0.append({"clave": k, "chunk_id": p["chunk_id"], "problema": "no está en la E0"})
                continue
            # páginas esperadas con la regla de la procedencia rica (ensamblar_tanda0.py:1247-1254): en una procedencia
            # herencia_*, las del heredado de su punto; si no, las de la unidad
            if (p.get("rol_documental") or "").startswith("herencia_"):
                esperadas = sorted({pg for h in c.get("herencia") or [] if h["unidad_origen"] == p["punto"]
                                    for pg in h.get("paginas", [])})
                n_herencia.append({"clave": k, "chunk_id": p["chunk_id"], "punto": p["punto"],
                                   "paginas": p["paginas"], "paginas_de_la_unidad": c.get("paginas")})
            else:
                esperadas = list(c.get("paginas") or [])
            for campo, v_e0 in (("to", c.get("to")), ("archivo", c.get("archivo")), ("paginas", esperadas)):
                if v_e0 != p.get(campo):
                    problemas_e0.append({"clave": k, "chunk_id": p["chunk_id"], "problema": f"{campo} distinto",
                                         "e0": v_e0, "procedencia": p.get(campo)})
            pags = list(p["paginas"]) + [pg for h in c.get("herencia") or [] for pg in (h.get("paginas") or [])]
            for pg in pags:
                n_pag += 1
                tot = paginas_pdf.get(p["archivo"])
                if tot is None or not (1 <= pg <= tot):
                    problemas_pdf.append({"clave": k, "archivo": p["archivo"], "pagina": pg, "paginas_del_pdf": tot})
    res["2_e0_y_pdf"] = {"procedencias": n_proc, "paginas_controladas": n_pag, "paginas_por_pdf": paginas_pdf,
                         "regla_de_paginas": "en una procedencia herencia_*, las del heredado de su punto; si no, las "
                                             "de la unidad (ensamblar_tanda0.py:1247-1254)",
                         "procedencias_herencia": n_herencia,
                         "problemas_e0": problemas_e0, "problemas_pdf": problemas_pdf,
                         "ok": not problemas_e0 and not problemas_pdf and n_proc == 120}

    # 3. campos vacíos que la evidencia tiene
    nodos = {n["id"]: n for n in kg["nodes"]}
    vacios = []
    def falta(ref, campo):
        vacios.append({"ref": ref, "campo": campo})
    for f in fichas:
        e = aristas[f["clave"]]
        for rot, nid in (("origen", e["source"]), ("destino", e["target"])):
            n, fn = nodos[nid], f[rot]
            if (n.get("properties") or {}).get("descripcion") and fn["descripcion"] != n["properties"]["descripcion"]:
                falta(f["ref"], f"{rot}.descripcion")
            for pk, pv in (n.get("properties") or {}).items():
                if pk in ("descripcion",) or pk in V.PROPS_NODO_FUERA or pv in (None, "", [], {}):
                    continue
                if fn["propiedades"].get(pk) in (None, "", [], {}):
                    falta(f["ref"], f"{rot}.propiedades.{pk}")
            for pk, pv in (n.get("properties_no_definidas") or {}).items():
                if pk not in V.NO_DEFINIDAS_FUERA and pv not in (None, "", [], {}) and \
                        (fn.get("propiedades_no_definidas_en_el_esquema") or {}).get(pk) in (None, "", [], {}):
                    falta(f["ref"], f"{rot}.propiedades_no_definidas.{pk}")
            for u_kg, u_f in zip(n["properties"].get("umbrales") or [], fn["propiedades"].get("umbrales") or []):
                for c in V.UMBRAL_CAMPOS:
                    if u_kg.get(c) not in (None, "") and u_f.get(c) in (None, ""):
                        falta(f["ref"], f"{rot}.umbrales.{c}")
        if e.get("calificador") and f["arista"].get("calificador") != e["calificador"]:
            falta(f["ref"], "arista.calificador")
        if e.get("properties_no_definidas") and not f["arista"].get("propiedades_no_definidas_en_el_esquema"):
            falta(f["ref"], "arista.propiedades_no_definidas")
        if e["relation"] in V.PREDICADOS_SUJETO and e.get("sujeto_mencion") and \
                (f["arista"].get("tramo_del_sujeto") or {}).get("texto") != e["sujeto_mencion"]:
            falta(f["ref"], "arista.tramo_del_sujeto")
        if len(f["evidencia"]) != len(e["provenances"]):
            falta(f["ref"], "evidencia (número de procedencias)")
        for p, ev in zip(e["provenances"], f["evidencia"]):
            c = e0[p["to"]][V.base_chunk(p["chunk_id"])]
            if (c.get("texto") or "") != ev["texto_propio"] or (c.get("texto") and not ev["texto_propio"]):
                falta(f["ref"], f"{p['chunk_id']}.texto_propio")
            her = c.get("herencia") or []
            if len(her) != len(ev["heredado"]) or any((h.get("texto") or "") != (x.get("texto") or "")
                                                      for h, x in zip(her, ev["heredado"])):
                falta(f["ref"], f"{p['chunk_id']}.heredado")
            if p.get("paginas") and ev["paginas"] != p["paginas"]:
                falta(f["ref"], f"{p['chunk_id']}.paginas")
            if not ev["pdf"]["con_pagina"] or not (a.copia / ev["pdf"]["ruta"]).exists():
                falta(f["ref"], f"{p['chunk_id']}.pdf")
            for rot, nid in (("origen", e["source"]), ("destino", e["target"])):
                t_kg = [q["tramo"] for q in nodos[nid]["provenances"] if q.get("chunk_id") == p["chunk_id"]
                        and q.get("tramo")]
                t_f = [t["texto"] for t in ev[f"tramos_{rot}"]]
                if sorted(set(t_kg)) != sorted(set(t_f)):
                    falta(f["ref"], f"{p['chunk_id']}.tramos_{rot}")
            if not ev["titulo_e0"] and c.get("titulo"):
                falta(f["ref"], f"{p['chunk_id']}.titulo")
    res["3_campos_vacios"] = {"faltan": vacios, "ok": not vacios}

    # 4. disjuntos
    disj = set(orden) & set(pool)
    res["4_disjuntos"] = {"interseccion": sorted(disj), "n_muestra": len(set(orden)), "n_pool": len(set(pool)),
                          "ok": not disj and len(set(orden)) == 100 and len(set(pool)) == 20}

    # 5. negativos
    claves_fichas = set()
    for f in fichas:
        claves_en(f, claves_fichas)
    prohibidas = sorted(claves_fichas & set(V.CLAVES_PROHIBIDAS))
    h_asig = datetime.fromisoformat(acta["asignacion"]["hora"])
    h_sort = datetime.fromisoformat(so["hora"])
    h_sello = datetime.fromisoformat(sello[2])
    h_fich = datetime.fromisoformat(cab["hora"])
    horas_ok = h_asig < h_sort <= h_sello < h_fich
    refs = {k: f"V{i + 1:03d}" for i, k in enumerate(orden)}
    hojas = {}
    for lote, ks in list(lotes.items()) + [("pool", pool)]:
        p = R / "lectura" / f"hoja_{lote}.csv"
        filas_h = [x for x in csv.reader(io.StringIO(p.read_text(encoding="utf-8"))) if any(x)]
        cuerpo = filas_h[5:]
        esperado = [(str(i), (refs[k] if lote != "pool" else f"P{i:02d}"), k) for i, k in enumerate(ks, 1)]
        hojas[p.name] = {"sha256": V.sha_archivo(p),
                         "filas_del_lote_sellado": [(r[0], r[1], r[3]) for r in cuerpo] == esperado,
                         "celdas_de_juicio_vacias": all(not c for r in cuerpo for c in r[4:]),
                         "horas_vacias": filas_h[2][1:] in ([], [""]) and filas_h[3][1:] in ([], [""])}
    res["5_negativos"] = {"claves_prohibidas_en_fichas": prohibidas,
                          "horas": {"asignacion": acta["asignacion"]["hora"], "sorteo": so["hora"], "sello": sello[2],
                                    "fichas": cab["hora"], "ok": horas_ok},
                          "hojas": hojas,
                          "ok": not prohibidas and horas_ok and all(all(v for kk, v in h.items() if kk != "sha256")
                                                                    for h in hojas.values())}
    res["ok"] = all(v.get("ok", True) for v in res.values() if isinstance(v, dict)) and all(res["fichas"].values())
    V.escribir_json(a.salida, res)
    print(json.dumps({k: (v if not isinstance(v, dict) else {kk: vv for kk, vv in v.items()
                                                               if kk not in ("hojas", "paginas_por_pdf")})
                      for k, v in res.items()}, ensure_ascii=False, indent=1))
    return 0 if res["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
