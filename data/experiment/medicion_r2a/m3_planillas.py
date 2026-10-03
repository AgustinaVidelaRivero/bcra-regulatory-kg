"""U-MED-R2A, M3 — planillas de las lecturas asistidas (reglas: data/experiment/medicion_r2a/m3/m3_reglas_lectura.md).

Solo lectura, USD 0: ninguna llamada a la API, Neo4j no se usa. Importa sin editarlos `r3d_remisiones.py` (variantes de
la paráfrasis y del texto de E0, para recomputar sobre KG-Tanda0-Diez-r2a la población de cambios de destino) y las
reglas de U-PYD (cuantías). Escribe solo en --out-dir: una planilla CSV por lectura y un resumen JSON con los tamaños de
las poblaciones, los sorteos y los controles. Todas las rutas son relativas al repo.

Uso, desde la raíz del repo:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/medicion_r2a/m3_planillas.py \
      --out-dir data/experiment/medicion_r2a/m3/planillas
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import random
import re
import sys
from collections import Counter, OrderedDict
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ = Path(__file__).resolve().parents[3]
for _p in (RAIZ / "data" / "experiment" / "pyd_r2" / "code", RAIZ / "data" / "experiment" / "r2_codigo"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))
import modelos_r2 as M                 # noqa: E402  (sin editar)
import reglas_comparacion as RCMP      # noqa: E402  (sin editar)
import r3d_remisiones as R3D           # noqa: E402  variantes y redirección de r3d (sin editar)

SEMILLA = 20261003
REX = "data/experiment/reextraccion_v2"
DIEZ = f"{REX}/corpus_tanda0/ens_diez_r2a/r2"
E0_LEGADA = f"{REX}/e0_chunking/salida_tanda0"
E0_R2 = f"{REX}/e0_chunking/salida_tanda0_r2"
MANIFIESTO = f"{REX}/manifiestos/tanda0_ens_diez.json"
PERDIDAS = "data/experiment/r2_codigo/r3_perdidas_remisiones.json"
R3D_JSON = "data/experiment/r2_codigo/r3d_remisiones.json"


def leer(p: str):
    return json.loads((RAIZ / p).read_text(encoding="utf-8"))


def chunks(dir_e0: str, tos) -> dict:
    out = {}
    for to in tos:
        d = leer(f"{dir_e0}/chunks_{to}.json")
        for c in d["chunks"] if isinstance(d, dict) else d:
            out[c["id"]] = c
    return out


def texto_propio(c: dict | None) -> str:
    return "" if c is None else (c.get("texto") or "")


def texto_heredado(c: dict | None) -> str:
    if c is None:
        return ""
    return "\n".join(f"[{h.get('tipo')} {h.get('unidad_origen')}] {h.get('texto') or ''}" for h in c.get("herencia") or [])


def escribir_csv(p: Path, filas: list[dict]) -> None:
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=list(filas[0]) if filas else ["vacio"], lineterminator="\n")
    w.writeheader()
    for f in filas:
        w.writerow(f)
    p.write_text(buf.getvalue(), encoding="utf-8")


def m3d(kg: dict, orden: list) -> tuple[list, dict]:
    """[c37]: plazos heredados sin cuantía temporal mandados a `frecuencia`, y aparte las Obligaciones con frecuencia
    de E1 sin plazo heredado."""
    unidades = M.UNIDADES_TEMPORALES + M.UNIDADES_TEMPORALES_FUERA
    lista = set(leer("data/experiment/pyd_r2/generados/enums_r2.json")["Obligacion.frecuencia"])
    pl, e1 = [], []
    for n in kg["nodes"]:
        if n["type"] != "Obligacion" or "frecuencia" not in n["properties"]:
            continue
        v = (n.get("campos_heredados_v3") or {}).get("plazo")
        es = (isinstance(v, str) and v.strip() and not any(c.unidad in unidades for c in RCMP.detectar_cuantias(v))
              and (n.get("originales") or {}).get("frecuencia") == v)
        (pl if es else e1).append(n)
    filas = []
    for grupo, ns, pref in (("plazo_heredado", pl, "D"), ("frecuencia_e1", e1, "F")):
        ns = sorted(ns, key=lambda n: (orden.index(n["provenance"]["to"]), n["id"]))
        for i, n in enumerate(ns, 1):
            v = (n.get("campos_heredados_v3") or {}).get("plazo") if grupo == "plazo_heredado" \
                else (n.get("originales") or {}).get("frecuencia", n["properties"]["frecuencia"])
            filas.append(OrderedDict([("id_lectura", f"{pref}{i:03d}"), ("grupo", grupo), ("to", n["provenance"]["to"]),
                                      ("nodo_id", n["id"]), ("chunk_id", n["provenance"].get("chunk_id")),
                                      ("valor_leido", v), ("frecuencia_asignada", n["properties"]["frecuencia"]),
                                      ("en_lista", "sí" if n["properties"]["frecuencia"] in lista else "no"),
                                      ("descripcion", n["properties"].get("descripcion"))]))
    return filas, {"plazo_heredado": len(pl), "frecuencia_e1": len(e1),
                   "plazo_heredado_fuera_de_lista": sum(1 for n in pl if "frecuencia" in (n.get("fuera_de_lista") or [])),
                   "valores_distintos_plazo_heredado": len({(n.get("campos_heredados_v3") or {}).get("plazo") for n in pl})}


def m3a(kg: dict) -> tuple[list, dict]:
    """Cambios de destino (r3d, C_diez_cambio_de_destino) recomputados sobre KG-Tanda0-Diez-r2a sin sus remite_a."""
    variante = dict(por_procedencia=False, propios="nodo", leer_termino=False)
    base = {"nodes": kg["nodes"], "edges": [e for e in kg["edges"] if e["relation"] != "remite_a"]}
    tipos = {n["id"]: n["type"] for n in kg["nodes"]}
    with R3D.redirigido("diez"):
        em = R3D.emisores()
        rpar = R3D.correr(base, em, tipos_origen=R3D.ORIG4, fuente="parafrasis", **variante)
        re0 = R3D.correr(base, em, tipos_origen=R3D.ORIG4, fuente="e0", reglas=frozenset(), **variante)
    pa, pe = R3D.pares_unidad(rpar, tipos), R3D.pares_unidad(re0, tipos)
    origenes = sorted({s for s, _ in pa} | {s for s, _ in pe})
    dpa = {o: sorted({d for s, d in pa if s == o}) for o in origenes}
    dpe = {o: sorted({d for s, d in pe if s == o}) for o in origenes}
    cambian = [o for o in origenes if dpa[o] != dpe[o]]
    muestra = random.Random(SEMILLA).sample(cambian, 30)
    nodos = {n["id"]: n for n in kg["nodes"]}
    rem = {}
    for e in kg["edges"]:
        if e["relation"] == "remite_a":
            rem.setdefault(e["source"], set()).add(e["properties"]["destino"])
    ch = chunks(E0_LEGADA, leer(MANIFIESTO)["orden_corrida"])
    filas = []
    for i, o in enumerate(muestra, 1):
        n = nodos[o]
        cid = n["provenance"].get("chunk_id")
        filas.append(OrderedDict([
            ("id_lectura", f"A{i:02d}"), ("nodo_id", o), ("tipo", n["type"]), ("to", n["provenance"].get("to")),
            ("punto", n["provenance"].get("punto")), ("chunk_id", cid), ("descripcion", n["properties"].get("descripcion")),
            ("destinos_parafrasis", " ".join(dpa[o])), ("destinos_texto_e0", " ".join(dpe[o])),
            ("solo_parafrasis", " ".join(sorted(set(dpa[o]) - set(dpe[o])))),
            ("solo_texto_e0", " ".join(sorted(set(dpe[o]) - set(dpa[o])))),
            ("destinos_remite_a_r2a_informativo", " ".join(sorted(rem.get(o, set())))),
            ("texto_e0_propio", texto_propio(ch.get(cid))), ("texto_e0_heredado", texto_heredado(ch.get(cid)))]))
    return filas, {"origenes_con_destino": len(origenes), "pares_parafrasis": len(pa), "pares_texto_e0": len(pe),
                   "pares_en_ambos": len(pa & pe), "pares_solo_parafrasis": len(pa - pe), "pares_solo_texto_e0": len(pe - pa),
                   "nodos_que_cambian_de_destino": len(cambian), "muestra": muestra,
                   "referencia_sellado_r3d": leer(R3D_JSON).get("C_diez_cambio_de_destino", {}).get(
                       "nodos_de_origen_con_destinos_distintos")}


def m3a2() -> tuple[list, dict]:
    """Los pares perdidos contra la paráfrasis de desarrollo con veredicto «SIN LECTURA»."""
    b = leer(PERDIDAS)["B_parafrasis_siete_tipos_desarrollo"]
    sel = [f for f in b["filas"] if f.get("veredicto") == "SIN LECTURA"]
    filas = []
    for i, f in enumerate(sel, 1):
        filas.append(OrderedDict([("id_lectura", f"P{i:02d}")] + [(k, f.get(k)) for k in (
            "origen", "tipo_origen", "label_origen", "texto_guardado_origen", "destino_nodo", "tipo_destino",
            "unidad_destino", "procedencia", "chunk_id", "evidencia_referencia", "texto_e0_del_punto",
            "texto_e0_superior", "causa")]))
    return filas, {"sin_lectura": len(sel), "por_veredicto": b["por_veredicto"]}


def m3b(registro: list, orden: list) -> tuple[list, dict]:
    """Citas irresolubles con causa «punto inexistente en E0» del registro de KG-Tanda0-Diez-r2a."""
    ch = chunks(E0_R2, orden)
    por_to = {}
    for cid, c in ch.items():
        por_to.setdefault(c["to"], []).append(c)
    filas, claves = [], []
    for c in registro:
        for x in c["irresolubles"]:
            if x["causa"] != "punto inexistente en E0":
                continue
            to_d, pt = x["destino"].split("::")
            claves.append((c["chunk_id"], c["evidencia"], x["destino"]))
            pref = pt.rsplit(".", 1)[0] if "." in pt else pt
            unidades = sorted(cc["unidad"] for cc in por_to.get(to_d, []) if cc.get("unidad"))
            vecinas = [u for u in unidades if u == pref or u.startswith(pref + ".")][:40]
            pat = re.compile(r"(?m)^\s*" + re.escape(pt) + r"\.?(?=\s|$)")
            ocurr = sorted(cc["id"] for cc in por_to.get(to_d, []) if pat.search(cc.get("texto") or ""))
            co = ch.get(c["chunk_id"])
            filas.append(OrderedDict([
                ("chunk_origen", c["chunk_id"]), ("procedencia_punto", c["procedencia"].get("punto")),
                ("atribucion", c.get("atribucion")), ("clase", c["clase"]), ("norma_nombrada", c.get("norma_nombrada")),
                ("evidencia", c["evidencia"]), ("destino_citado", x["destino"]),
                ("unidades_e0_vecinas_en_destino", " ".join(vecinas)),
                ("chunks_del_destino_con_el_numero_al_inicio_de_linea", " ".join(ocurr)),
                ("texto_chunk_origen", texto_propio(co)), ("texto_heredado_chunk_origen", texto_heredado(co))]))
    orden_f = sorted(range(len(filas)), key=lambda k: (filas[k]["chunk_origen"], filas[k]["destino_citado"], filas[k]["evidencia"]))
    filas = [OrderedDict([("id_lectura", f"B{i:02d}")] + list(filas[k].items())) for i, k in enumerate(orden_f, 1)]
    ref = leer(R3D_JSON).get("G_reglas_diez", {}).get("h_irresolubles", {}).get("inexistentes") or []
    ref_claves = {(r.get("chunk_id") or r.get("chunk"), r.get("evidencia") or r.get("tramo"), r.get("destino")) for r in ref}
    return filas, {"inexistentes_r2a": len(filas), "inexistentes_r3d_sellado": len(ref),
                   "coinciden_por_chunk_evidencia_destino": len(set(claves) & ref_claves),
                   "claves_r3d": sorted(ref[0]) if ref else None}


def m3c() -> tuple[list, dict]:
    tabla = leer(f"{DIEZ}/e4_pasada_residual_medida.json")
    filas = [OrderedDict([("id_lectura", f"C{i:02d}")] + [(k, json.dumps(v, ensure_ascii=False) if isinstance(v, (dict, list)) else v)
                                                         for k, v in t.items()]) for i, t in enumerate(tabla, 1)]
    resueltos = [t for t in tabla if t.get("resuelto_a") or t.get("id_resuelto") or t.get("estado") == "resuelto"]
    return filas, {"propuestos": len(tabla), "resoluciones_propuestas": len(resueltos),
                   "claves": sorted(tabla[0]) if tabla else None}


def m3e(kg: dict, orden: list) -> tuple[list, dict]:
    nodos = {n["id"]: n for n in kg["nodes"]}
    ch = chunks(E0_LEGADA, orden)
    filas, res = [], {}
    for par, pref in (("Operacion", "EO"), ("Potestad", "EP")):
        pob = sorted(((e["source"], e["target"]) for e in kg["edges"] if e.get("no_verificada_e3")
                      and e["relation"] == "condicion_de" and nodos[e["target"]]["type"] == par))
        muestra = random.Random(SEMILLA).sample(pob, 20)
        res[par] = {"poblacion": len(pob), "muestra": muestra}
        por_par = {(e["source"], e["target"]): e for e in kg["edges"] if e.get("no_verificada_e3")}
        for i, (s, t) in enumerate(muestra, 1):
            e = por_par[(s, t)]
            cid = e["provenance"].get("chunk_id")
            filas.append(OrderedDict([
                ("id_lectura", f"{pref}{i:02d}"), ("par", f"condicion_de -> {par}"), ("chunk_id", cid),
                ("origen_id", s), ("origen_descripcion", nodos[s]["properties"].get("descripcion")),
                ("destino_id", t), ("destino_tipo", nodos[t]["type"]),
                ("destino_descripcion", nodos[t]["properties"].get("descripcion")),
                ("texto_e0_propio", texto_propio(ch.get(cid))), ("texto_e0_heredado", texto_heredado(ch.get(cid)))]))
    return filas, res


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", required=True)
    a = ap.parse_args()
    out = RAIZ / a.out_dir
    out.mkdir(parents=True, exist_ok=True)
    kg = leer(f"{DIEZ}/kg.json")
    registro = leer(f"{DIEZ}/remisiones_registro.json")
    orden = leer(MANIFIESTO)["orden_corrida"]
    resumen = OrderedDict([("semilla", SEMILLA), ("kg", f"{DIEZ}/kg.json")])
    for nombre, (filas, info) in (("m3d_plazos_frecuencia", m3d(kg, orden)), ("m3a_cambios_destino", m3a(kg)),
                                  ("m3a2_perdidas_sin_lectura", m3a2()), ("m3b_puntos_inexistentes", m3b(registro, orden)),
                                  ("m3c_pasada_residual_e4", m3c()), ("m3e_matriz_no_verificadas", m3e(kg, orden))):
        escribir_csv(out / f"{nombre}.csv", filas)
        resumen[nombre] = {"filas": len(filas), **info}
    (out / "m3_planillas_resumen.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=1) + "\n",
                                                   encoding="utf-8")
    print(json.dumps({k: (v if not isinstance(v, dict) else {kk: vv for kk, vv in v.items() if kk != "muestra"})
                      for k, v in resumen.items()}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
