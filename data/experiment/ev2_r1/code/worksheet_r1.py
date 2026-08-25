"""
worksheet_r1.py — Worksheet CIEGO de adjudicación humana de U-B1.8 (molde
ev2_adjudicacion/code/comun_adj.py + construir_worksheet.py, commit 03ebe83,
adaptado a un solo grafo; autorización de la mesa en el freno 3). USD 0.

Población A (8 pares con final requiere_adjudicacion):
  - 5 heredados de la etapa 1 (no re-corridos): ficha sobre la respuesta BASE;
  - 3 pendientes del §7: una ficha por CADA voto ADJ de re-corrida; si dos
    re-corridas del par tienen texto idéntico comparten UNA ficha y la
    adjudicación se aplica a ambas (regla del molde). El par decidido por
    invariancia NO genera ficha (su voto ADJ queda sin veredicto propio,
    contado — comportamiento de la base).
Población B (muestra simétrica sobre los veredictos FINALES post-§7):
  semilla `adjudicacion-ev2-r1`, generador nuevo por estrato sobre ids
  ordenados: ceil(10 %) de los 5 correcto = 1; ceil(10 %) de los 27
  parcial+incorrecto = 3. Par re-corrido → ficha con la re-corrida de MENOR
  rep cuyo veredicto coincide con el final; no re-corrido → la base. La
  muestra mide la tasa de error del juez; NO reemplaza veredictos.

Ceguera de la ficha (molde): solo número, id ADJ1-, TO/ancla del gold,
pregunta, respuesta completa y criterios con cita. JAMÁS grafo, label, rep,
veredicto, fragmentos del juez ni ids EV2R1-/EV2E1-/EV2F-. La tabla
ficha → (par, respuesta, origen, veredictos del juez) va a SOLO_MESA.
El selftest no-fuga (selftest_nofuga_r1.py) es OBLIGATORIO antes de entregar.

Salidas: adjudicacion/worksheet_adjudicacion_r1.{json,md} +
adjudicacion/censo_worksheet_r1_ciego.md (publicables) y
adjudicacion_SOLO_MESA/{tabla_fichas_r1,poblacion_adjudicacion_r1}_SOLO_MESA.json.

Uso:  .venv/bin/python -B data/experiment/ev2_r1/code/worksheet_r1.py
"""

from __future__ import annotations

import json
import math
import random
import sys
from collections import Counter
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_r1 as cr                      # noqa: E402
import agregacion_enc as ag                # noqa: E402  (regla sellada 9044a04)
from comun_r1 import cf, mapping           # noqa: E402

ADJ_DIR = cr.UNIDAD_DIR / "adjudicacion"
SOLO_MESA_DIR = cr.UNIDAD_DIR / "adjudicacion_SOLO_MESA"
WORKSHEET_JSON = ADJ_DIR / "worksheet_adjudicacion_r1.json"
WORKSHEET_MD = ADJ_DIR / "worksheet_adjudicacion_r1.md"
CENSO_CIEGO = ADJ_DIR / "censo_worksheet_r1_ciego.md"
TABLA_FICHAS = SOLO_MESA_DIR / "tabla_fichas_r1_SOLO_MESA.json"
POBLACION_SM = SOLO_MESA_DIR / "poblacion_adjudicacion_r1_SOLO_MESA.json"

ADJ = "requiere_adjudicacion"
FRACCION_MUESTRA = 0.10
ORIGENES = ("heredado_base", "s7_pendiente", "muestra_correcto", "muestra_parcial_incorrecto")

# Esperados de la autorización del freno 3 (se verifican, no se asumen)
ESPERADO_FINAL = {"correcto": 5, "parcial": 19, "incorrecto": 8, ADJ: 8}
ESPERADO_HEREDADOS = 5
ESPERADO_PENDIENTES_S7 = 3
ESPERADO_MUESTRA = {"correcto": 1, "parcial_incorrecto": 3}


def cargar_gold_fichas() -> dict[str, dict]:
    """Gold con TO, nombre y ancla (lo que la ficha muestra), vía el archivo
    sellado — mismo shape que comun_adj.cargar_gold."""
    data = json.loads(cf.GOLD_PATH.read_text(encoding="utf-8"))
    out = {}
    for p in data["preguntas"]:
        out[p["id"]] = {"pregunta": p["pregunta"], "to": p["to"],
                        "to_nombre": p["to_nombre"], "ancla": list(p["gold"]["ancla"]),
                        "criterios": [{"criterio": c["criterio"],
                                       "cita_textual": c["cita_textual"]}
                                      for c in p["gold"]["criterios"]]}
    if len(out) != 40 or sum(len(v["criterios"]) for v in out.values()) != 164:
        raise ValueError("gold inesperado")
    return out


def cargar_insumos() -> dict:
    base_agg = json.loads((cr.JUEZ_OUT_DIR / "veredictos_agregados_ciego.json")
                          .read_text(encoding="utf-8"))
    base_tab = json.loads((cr.DESANON_DIR / "tabla_id_opaco_r1_SOLO_MESA.json")
                          .read_text(encoding="utf-8"))
    enc_fin = json.loads((cr.UNIDAD_DIR / "reporte" / "veredictos_finales_s7_r1.json")
                         .read_text(encoding="utf-8"))
    enc_agg = json.loads((cr.UNIDAD_DIR / "juez_out_enc" / "veredictos_agregados_ciego.json")
                         .read_text(encoding="utf-8"))
    enc_tab = json.loads((cr.DESANON_DIR / "tabla_id_opaco_s7_r1_SOLO_MESA.json")
                         .read_text(encoding="utf-8"))
    if base_agg["n_agregados"] != 40 or base_tab["n"] != 40:
        raise ValueError("base de r1 inesperada")
    if enc_fin["n_pares_agregados"] != 24 or enc_fin["n_pares_incompletos"] != 0:
        raise ValueError("§7 inesperado")
    if enc_agg["n_agregados"] != 72 or enc_tab["n"] != 72:
        raise ValueError("juez §7 inesperado")
    return {"base_agg": {a["id_opaco"]: a for a in base_agg["agregados"]},
            "base_tab": {f["id_opaco"]: f for f in base_tab["filas"]},
            "enc_pares": {p["id_opaco_base"]: p for p in enc_fin["pares"]},
            "enc_agg": {a["id_opaco"]: a for a in enc_agg["agregados"]},
            "enc_tab": {f["id_opaco"]: f for f in enc_tab["filas"]},
            "gold": cargar_gold_fichas()}


def leer_respuesta_traza(path: Path, sha_esperado: str) -> str:
    t = json.loads(path.read_text(encoding="utf-8"))
    r = (t["trace"].get("final_json") or {}).get("respuesta")
    if not isinstance(r, str) or not r.strip():
        raise ValueError(f"{path}: traza sin respuesta parseada")
    if cr.sha256_texto(r) != sha_esperado:
        raise ValueError(f"{path}: sha256 de la respuesta no coincide con la tabla")
    return r


def respuesta_de(ins: dict, id_opaco: str, origen: str) -> str:
    if origen == "base":
        f = ins["base_tab"][id_opaco]
        return leer_respuesta_traza(cr.TRAZAS_DIR / f["label"] / f"{f['id_pregunta']}.json",
                                    f["sha256_respuesta"])
    f = ins["enc_tab"][id_opaco]
    return leer_respuesta_traza(cr.TRAZAS_DIR / f["label"] / f"{f['id_pregunta']}.json",
                                f["sha256_respuesta"])


# --------------------------------------------------------------------------- #
# Finales por par y poblaciones (molde comun_adj, un solo grafo)               #
# --------------------------------------------------------------------------- #
def finales_por_par(ins: dict) -> list[dict]:
    xs = []
    for idb, a in ins["base_agg"].items():
        f = ins["base_tab"][idb]
        rec = {"id_pregunta": f["id_pregunta"], "id_opaco_base": idb,
               "veredicto_base": a["veredicto_pregunta"], "modales_base": a["modales"],
               "sha256_respuesta_base": f["sha256_respuesta"]}
        p = ins["enc_pares"].get(idb)
        if p is None:
            rec.update({"re_corrido": False, "tipo_enc": None,
                        "final": a["veredicto_pregunta"], "fuente_final": "base",
                        "ids_reps": None, "veredictos_reps": None, "via_enc": None})
        else:
            if p["veredicto_base"] != a["veredicto_pregunta"]:
                raise ValueError(f"{idb}: veredicto base inconsistente entre etapas")
            if ag.agregar_par(p["veredictos_reps"]) != p["final"]:
                raise ValueError(f"{idb}: agregado §7 no reproduce con agregar_par")
            rec.update({"re_corrido": True, "tipo_enc": p["tipo"], "final": p["final"],
                        "fuente_final": "s7", "ids_reps": list(p["ids_reps"]),
                        "veredictos_reps": list(p["veredictos_reps"]),
                        "via_enc": p["via"]})
        xs.append(rec)
    if len({x["id_pregunta"] for x in xs}) != 40:
        raise ValueError("pares repetidos")
    dist = dict(Counter(x["final"] for x in xs))
    if dist != ESPERADO_FINAL:
        raise ValueError(f"finales fuera de lo autorizado: {dist}")
    return sorted(xs, key=lambda x: x["id_pregunta"])


def poblacion_a(fin: list[dict], ins: dict) -> dict:
    heredados, pendientes = [], []
    for x in fin:
        if x["final"] != ADJ:
            continue
        if not x["re_corrido"]:
            heredados.append({**x, "objetivos": [
                {"id_opaco_respuesta": x["id_opaco_base"], "rep": None,
                 "origen_respuesta": "base",
                 "sha256_respuesta": x["sha256_respuesta_base"],
                 "veredicto_juez_respuesta": x["veredicto_base"],
                 "modales_juez": x["modales_base"]}]})
        else:
            objs = []
            for rep, (ide, v) in enumerate(zip(x["ids_reps"], x["veredictos_reps"]),
                                           start=1):
                if v != ADJ:
                    continue
                fe = ins["enc_tab"][ide]
                if fe["rep"] != rep or fe["id_opaco_base"] != x["id_opaco_base"]:
                    raise ValueError(f"{ide}: rep/par inconsistente")
                ae = ins["enc_agg"][ide]
                if ae["veredicto_pregunta"] != v:
                    raise ValueError(f"{ide}: veredicto por respuesta inconsistente")
                objs.append({"id_opaco_respuesta": ide, "rep": rep,
                             "origen_respuesta": "enc",
                             "sha256_respuesta": fe["sha256_respuesta"],
                             "veredicto_juez_respuesta": v,
                             "modales_juez": ae["modales"]})
            if not objs:
                raise ValueError(f"{x['id_opaco_base']}: pendiente §7 sin votos ADJ")
            pendientes.append({**x, "objetivos": objs})
    if len(heredados) != ESPERADO_HEREDADOS or len(pendientes) != ESPERADO_PENDIENTES_S7:
        raise ValueError(f"población A fuera de lo autorizado: "
                         f"{len(heredados)} heredados, {len(pendientes)} pendientes")
    return {"heredados": heredados, "pendientes_s7": pendientes}


def muestra_estrato(ids_pregunta: list[str]) -> list[str]:
    ids = sorted(ids_pregunta)
    if not ids:
        return []
    k = math.ceil(FRACCION_MUESTRA * len(ids))
    return sorted(random.Random(cr.SEMILLA_MUESTRA).sample(ids, k))


def objetivo_muestra(x: dict, ins: dict) -> dict:
    if not x["re_corrido"]:
        return {"id_opaco_respuesta": x["id_opaco_base"], "rep": None,
                "origen_respuesta": "base",
                "sha256_respuesta": x["sha256_respuesta_base"],
                "veredicto_juez_respuesta": x["veredicto_base"],
                "modales_juez": x["modales_base"]}
    for rep, (ide, v) in enumerate(zip(x["ids_reps"], x["veredictos_reps"]), start=1):
        if v == x["final"]:
            fe, ae = ins["enc_tab"][ide], ins["enc_agg"][ide]
            return {"id_opaco_respuesta": ide, "rep": rep, "origen_respuesta": "enc",
                    "sha256_respuesta": fe["sha256_respuesta"],
                    "veredicto_juez_respuesta": v, "modales_juez": ae["modales"]}
    raise ValueError(f"{x['id_opaco_base']}: ninguna re-corrida coincide con el final")


def muestra_b(fin: list[dict], ins: dict) -> dict:
    por_q = {x["id_pregunta"]: x for x in fin}
    corr = [x["id_pregunta"] for x in fin if x["final"] == "correcto"]
    pi = [x["id_pregunta"] for x in fin if x["final"] in ("parcial", "incorrecto")]
    sc, sp = muestra_estrato(corr), muestra_estrato(pi)
    if len(sc) != ESPERADO_MUESTRA["correcto"] or len(sp) != ESPERADO_MUESTRA["parcial_incorrecto"]:
        raise ValueError(f"muestra fuera de lo autorizado: {len(sc)}/{len(sp)}")
    out = {"detalle_estratos": {"correcto": {"n": len(corr), "k": len(sc), "ids": sc},
                                "parcial_incorrecto": {"n": len(pi), "k": len(sp), "ids": sp}},
           "correcto": [], "parcial_incorrecto": []}
    for estrato, ids in (("correcto", sc), ("parcial_incorrecto", sp)):
        for q in ids:
            x = por_q[q]
            out[estrato].append({**x, "objetivos": [objetivo_muestra(x, ins)]})
    return out


# --------------------------------------------------------------------------- #
# Fichas (molde construir_fichas, ficha compartida por texto idéntico)         #
# --------------------------------------------------------------------------- #
def construir_fichas(ins: dict) -> dict:
    fin = finales_por_par(ins)
    pobA = poblacion_a(fin, ins)
    muestra = muestra_b(fin, ins)
    gold = ins["gold"]

    fichas: dict[tuple, dict] = {}

    def agregar(x: dict, obj: dict, origen: str):
        clave = (x["id_pregunta"], obj["sha256_respuesta"])
        d = fichas.get(clave)
        if d is None:
            texto = respuesta_de(ins, obj["id_opaco_respuesta"],
                                 obj["origen_respuesta"])
            d = fichas[clave] = {"id_pregunta": x["id_pregunta"],
                                 "sha256_respuesta": obj["sha256_respuesta"],
                                 "respuesta": texto, "objetivos": []}
        d["objetivos"].append({"origen": origen, "id_pregunta": x["id_pregunta"],
                               "id_opaco_base": x["id_opaco_base"],
                               "final_juez_par": x["final"],
                               "fuente_final": x["fuente_final"],
                               "veredictos_reps": x["veredictos_reps"],
                               "ids_reps": x["ids_reps"], **obj})

    for x in pobA["heredados"]:
        for o in x["objetivos"]:
            agregar(x, o, "heredado_base")
    for x in pobA["pendientes_s7"]:
        for o in x["objetivos"]:
            agregar(x, o, "s7_pendiente")
    for x in muestra["correcto"]:
        for o in x["objetivos"]:
            agregar(x, o, "muestra_correcto")
    for x in muestra["parcial_incorrecto"]:
        for o in x["objetivos"]:
            agregar(x, o, "muestra_parcial_incorrecto")

    for d in fichas.values():
        if len({o["origen"] for o in d["objetivos"]}) != 1 \
                or len({o["id_opaco_base"] for o in d["objetivos"]}) != 1:
            raise ValueError(f"ficha con objetivos heterogéneos: {d['id_pregunta']}")

    claves = sorted(fichas)
    random.Random(cr.SEMILLA_WORKSHEET).shuffle(claves)
    ws, mesa = [], []
    for n, clave in enumerate(claves, start=1):
        d = fichas[clave]
        g = gold[d["id_pregunta"]]
        fid = cr.id_ficha(*clave)
        ws.append({"n": n, "id_ficha": fid, "to": g["to"], "to_nombre": g["to_nombre"],
                   "ancla": g["ancla"], "pregunta": g["pregunta"],
                   "respuesta": d["respuesta"],
                   "criterios": [{"indice": j, "criterio": c["criterio"],
                                  "cita_textual": c["cita_textual"], "veredicto": None}
                                 for j, c in enumerate(g["criterios"], start=1)],
                   "observaciones": None})
        mesa.append({"n": n, "id_ficha": fid, "id_pregunta": d["id_pregunta"],
                     "sha256_respuesta": d["sha256_respuesta"],
                     "n_criterios": len(g["criterios"]),
                     "origen": d["objetivos"][0]["origen"],
                     "id_opaco_base": d["objetivos"][0]["id_opaco_base"],
                     "final_juez_par": d["objetivos"][0]["final_juez_par"],
                     "fuente_final": d["objetivos"][0]["fuente_final"],
                     "veredictos_reps": d["objetivos"][0]["veredictos_reps"],
                     "ids_reps": d["objetivos"][0]["ids_reps"],
                     "respuestas": [{"id_opaco_respuesta": o["id_opaco_respuesta"],
                                     "rep": o["rep"],
                                     "origen_respuesta": o["origen_respuesta"],
                                     "veredicto_juez_respuesta": o["veredicto_juez_respuesta"],
                                     "modales_juez": o["modales_juez"]}
                                    for o in d["objetivos"]]})
    ids = [f["id_ficha"] for f in ws]
    if len(set(ids)) != len(ids):
        raise ValueError("colisión de ids de ficha")
    return {"fin": fin, "pobA": pobA, "muestra": muestra,
            "worksheet": ws, "fichas_mesa": mesa}


# --------------------------------------------------------------------------- #
# Render (molde 03ebe83)                                                       #
# --------------------------------------------------------------------------- #
INSTRUCCIONES_MD = """\
# Worksheet de adjudicación humana — fidelidad EV2 de KG-Reextraído-r1 (U-B1.8)

Adjudicación según §6 del pre-registro del método
(`docs/preregistro_evaluacion_fidelidad_ev2.md`, commit be8a84f) y el
pre-registro de la unidad (`data/experiment/ev2_r1/preregistro_ev2_r1.md`,
commit 6c5507b). Fichas en orden aleatorizado (semilla `{sem}`), numeradas
1..{n}. Cada ficha trae: TO y ancla del gold, la pregunta, la respuesta
COMPLETA del sistema y los criterios del gold sellado con su cita textual.

## Instrucciones

1. Adjudicar contra el PDF del Texto Ordenado indicado (ancla como punto de
   partida) y contra el gold sellado
   (`data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json`),
   **criterio por criterio**.
2. Para cada criterio marcar exactamente uno: `cumplido` (la respuesta
   satisface lo que el criterio exige, conforme a la norma) o `no_cumplido`
   (no lo satisface, lo contradice, o no lo trata). No hay opción "dudoso":
   la adjudicación resuelve.
3. **No poner veredicto de pregunta a ojo.** El veredicto de la pregunta lo
   computa el mapping §2 en código a partir de las marcas por criterio
   (todos cumplidos → correcto; ninguno → incorrecto; mezcla → parcial).
4. Las marcas se vuelcan en `worksheet_adjudicacion_r1.json` (campo
   `veredicto` de cada criterio, en la ficha del mismo `id_ficha`);
   `observaciones` es libre y opcional. Este `.md` es la vista de lectura.
5. Cada ficha se adjudica por sí sola. Las fichas no indican de qué corrida
   proviene la respuesta ni qué veredicto recibió, y no debe intentarse
   inferirlo.

Marcas válidas: `cumplido` | `no_cumplido`.

---
"""


def render_md(ws: list[dict]) -> str:
    out = [INSTRUCCIONES_MD.format(sem=cr.SEMILLA_WORKSHEET, n=len(ws))]
    for f in ws:
        out.append(f"\n## Ficha {f['n']} — `{f['id_ficha']}`\n")
        out.append(f"**TO:** {f['to_nombre']} (`{f['to']}`) · **Ancla del gold:** "
                   f"{', '.join(f['ancla'])}\n")
        out.append(f"**Pregunta:**\n\n{f['pregunta']}\n")
        out.append("**Respuesta del sistema (completa):**\n")
        out.append("\n".join("> " + ln for ln in f["respuesta"].splitlines()) + "\n")
        out.append("**Criterios del gold (marcar cumplido / no_cumplido):**\n")
        for c in f["criterios"]:
            out.append(f"- **C{c['indice']}.** {c['criterio']}")
            out.append(f"  - Cita textual del TO: «{c['cita_textual']}»")
            out.append(f"  - Marca: `____________`  (cumplido / no_cumplido)")
        out.append("\n**Observaciones (opcional):** ______________________________________\n")
        out.append("---\n")
    return "\n".join(out)


def censo_ciego(res: dict) -> str:
    mesa = res["fichas_mesa"]
    por_origen = Counter(f["origen"] for f in mesa)
    resp_por_origen = Counter()
    for f in mesa:
        resp_por_origen[f["origen"]] += len(f["respuestas"])
    lineas = ["# Censo CIEGO del worksheet de adjudicación de r1 (U-B1.8)\n",
              f"- fichas: {len(mesa)}",
              "- por origen (fichas / respuestas cubiertas): " +
              ", ".join(f"{o} {por_origen[o]} / {resp_por_origen[o]}"
                        for o in ORIGENES if por_origen[o]),
              f"- pares heredados de la etapa 1 con final requiere_adjudicacion: "
              f"{len(res['pobA']['heredados'])}",
              f"- pares pendientes del §7: {len(res['pobA']['pendientes_s7'])} "
              f"(votos requiere_adjudicacion con ficha: "
              f"{sum(len(x['objetivos']) for x in res['pobA']['pendientes_s7'])})",
              f"- muestra simétrica: correcto {len(res['muestra']['correcto'])}, "
              f"parcial+incorrecto {len(res['muestra']['parcial_incorrecto'])} "
              f"(mide la tasa de error del juez; no reemplaza veredictos)",
              f"- criterios a marcar: {sum(f['n_criterios'] for f in mesa)}",
              f"- semilla del orden: {cr.SEMILLA_WORKSHEET}; semilla de la muestra: "
              f"{cr.SEMILLA_MUESTRA}"]
    return "\n".join(lineas) + "\n"


def main() -> int:
    print("== Worksheet ciego de adjudicación de r1 (U-B1.8, $0) ==")
    sellos = cr.verificar_sellos()
    ins = cargar_insumos()
    res = construir_fichas(ins)
    ADJ_DIR.mkdir(parents=True, exist_ok=True)
    SOLO_MESA_DIR.mkdir(parents=True, exist_ok=True)
    ws_json = {"worksheet": "adjudicacion-ev2-r1-fidelidad",
               "semilla_orden": cr.SEMILLA_WORKSHEET,
               "n_fichas": len(res["worksheet"]),
               "marcas_validas": list(mapping.VEREDICTOS_CRITERIO[:2]),
               "instrucciones": ("Marcar `veredicto` de cada criterio con cumplido | "
                                 "no_cumplido, contra el PDF del TO y el gold sellado. "
                                 "El veredicto de pregunta lo computa el mapping §2 en "
                                 "código; no se completa a mano."),
               "fichas": res["worksheet"]}
    for p, contenido in ((WORKSHEET_JSON, json.dumps(ws_json, ensure_ascii=False, indent=2)),
                         (WORKSHEET_MD, render_md(res["worksheet"])),
                         (CENSO_CIEGO, censo_ciego(res))):
        if p.exists() and p.read_text(encoding="utf-8") != contenido:
            raise RuntimeError(f"{p} ya existe y difiere de lo recomputado")
        p.write_text(contenido, encoding="utf-8")
    tabla = {"SOLO_MESA": True, "salt_id_ficha": cr.SAL_ID_FICHA,
             "prefijo": cr.PREFIJO_FICHA,
             "regla": "id_ficha = prefijo + sha256(salt|id_pregunta|sha256(respuesta))[:8]",
             "n": len(res["fichas_mesa"]), "fichas": res["fichas_mesa"]}
    pob = {"SOLO_MESA": True,
           "finales_por_par": res["fin"],
           "distribucion_finales": dict(Counter(x["final"] for x in res["fin"])),
           "poblacion_a": {"heredados": res["pobA"]["heredados"],
                           "pendientes_s7": res["pobA"]["pendientes_s7"]},
           "muestra_b": res["muestra"]}
    for p, obj in ((TABLA_FICHAS, tabla), (POBLACION_SM, pob)):
        contenido = json.dumps(obj, ensure_ascii=False, indent=2)
        if p.exists() and p.read_text(encoding="utf-8") != contenido:
            raise RuntimeError(f"{p} ya existe y difiere de lo recomputado")
        p.write_text(contenido, encoding="utf-8")
    if cr.verificar_sellos() != sellos:
        raise RuntimeError("sellos cambiaron durante la construcción")
    mesa = res["fichas_mesa"]
    print(f"  fichas: {len(mesa)} — por origen "
          f"{dict(Counter(f['origen'] for f in mesa))}")
    print(f"  criterios a marcar: {sum(f['n_criterios'] for f in mesa)}")
    print(f"  -> {WORKSHEET_MD}")
    print(f"  -> {TABLA_FICHAS}")
    print("  SIGUIENTE PASO OBLIGATORIO: selftest_nofuga_r1.py antes de entregar")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
