"""
comun_adj.py — Población, muestra simétrica y fichas CIEGAS del worksheet de
adjudicación humana de EV2 (pre-registro docs/preregistro_evaluacion_fidelidad_ev2.md
§6, commit be8a84f) más la resolución de los pares que el encadenamiento §7
(data/experiment/ev2_encadenamiento/, commit 9044a04) dejó pendientes.

Todo OFFLINE (USD 0): ninguna llamada a API. Nada fuera de
data/experiment/ev2_adjudicacion/ se edita.

Insumos (solo lectura; sha registrados en cada salida):
  - corrida base de fidelidad: ev2_fidelidad_eval/out/veredictos_agregados_ciego.json
    (veredicto por respuesta base, mapping §2) + desanonimizacion/tabla_id_opaco.json;
  - encadenamiento §7: ev2_encadenamiento/reporte/veredictos_finales_ciego.json
    (agregación por par de las re-corridas) + juez_out/veredictos_agregados_ciego.json
    (veredicto por respuesta nueva) + desanonimizacion_SOLO_MESA/tabla_id_opaco_
    encadenamiento_SOLO_MESA.json;
  - respuestas: trazas base (ev2_corrida/trazas/ev2_base_*/) y de re-corrida
    (ev2_encadenamiento/trazas/ev2_enc_*/); viaja a la ficha únicamente
    trace.final_json.respuesta (sha256 verificado contra las tablas);
  - gold sellado: exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json.

Veredicto FINAL por par (pregunta, grafo), pre-adjudicación:
  - par re-corrido en §7 (63 parcial disparados + 3 auditoría): el agregado
    de las 3 re-corridas (`agregar_par`, ev2_encadenamiento/code/agregacion_enc.py);
  - resto: el veredicto de la respuesta base.

Población del worksheet:
  A) los pares con final `requiere_adjudicacion`:
     - heredados de la base (no re-corridos): la ficha lleva la respuesta BASE;
     - pendientes del §7: una ficha por CADA respuesta de re-corrida cuyo
       veredicto del juez fue `requiere_adjudicacion`; si dos re-corridas de
       un mismo par tienen texto idéntico (mismo sha256, mismo request al
       juez), comparten UNA ficha y la adjudicación se aplica a ambas
       (decisión de esta unidad, declarada en el reporte).
  B) muestra simétrica §6 sobre los veredictos FINALES, por grafo, con
     random.Random("adjudicacion-ev2-v1") sobre ids ORDENADOS (id de
     pregunta; generador nuevo por (grafo, estrato), mismo patrón que la
     auditoría §7): ceil(10 %) de los `correcto` y ceil(10 %) de los
     `parcial`+`incorrecto`. Par re-corrido → la ficha lleva la re-corrida de
     MENOR rep cuyo veredicto coincide con el final; par no re-corrido → la
     respuesta base.

Ceguera de la ficha: contiene solo número, id de ficha opaco, TO/ancla del
gold, pregunta, respuesta completa, criterios con cita textual y el espacio de
respuesta. JAMÁS grafo, label, rep, veredicto o fragmentos del juez, ni ids
EV2R-/EV2E-/EV2F-. La tabla ficha → (par, respuesta, origen, veredictos del
juez) vive en adjudicacion_SOLO_MESA/.
"""

from __future__ import annotations

import hashlib
import json
import math
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
UNIDAD_DIR = CODE_DIR.parent                       # data/experiment/ev2_adjudicacion
EXP_DIR = UNIDAD_DIR.parent                        # data/experiment
REPO_DIR = EXP_DIR.parent.parent

FIDELIDAD_EVAL_DIR = EXP_DIR / "ev2_fidelidad_eval"
ENC_DIR = EXP_DIR / "ev2_encadenamiento"
CORRIDA_DIR = EXP_DIR / "ev2_corrida"
JUEZ_DIR = EXP_DIR / "ev2_juez"

for _p in (ENC_DIR / "code", JUEZ_DIR):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))
import agregacion_enc as ag   # noqa: E402  (regla de agregación por par, sellada por commit)
import mapping                # noqa: E402  (mapping §2 del juez, sellado por commit)

# Salidas de esta unidad
ADJ_DIR = UNIDAD_DIR / "adjudicacion"                     # worksheet CIEGO
SOLO_MESA_DIR = UNIDAD_DIR / "adjudicacion_SOLO_MESA"     # tabla ficha → par
WORKSHEET_JSON = ADJ_DIR / "worksheet_adjudicacion.json"
WORKSHEET_MD = ADJ_DIR / "worksheet_adjudicacion.md"
CENSO_CIEGO = ADJ_DIR / "censo_worksheet_ciego.md"
TABLA_FICHAS = SOLO_MESA_DIR / "tabla_fichas_SOLO_MESA.json"
POBLACION_SM = SOLO_MESA_DIR / "poblacion_adjudicacion_SOLO_MESA.json"
RESUMEN_SM = SOLO_MESA_DIR / "resumen_poblacion_SOLO_MESA.md"

# Insumos
BASE_AGREGADOS = FIDELIDAD_EVAL_DIR / "out" / "veredictos_agregados_ciego.json"
BASE_TABLA = FIDELIDAD_EVAL_DIR / "desanonimizacion" / "tabla_id_opaco.json"
BASE_TRAZAS_DIR = CORRIDA_DIR / "trazas"
ENC_FINALES = ENC_DIR / "reporte" / "veredictos_finales_ciego.json"
ENC_AGREGADOS = ENC_DIR / "juez_out" / "veredictos_agregados_ciego.json"
ENC_TABLA = ENC_DIR / "desanonimizacion_SOLO_MESA" / "tabla_id_opaco_encadenamiento_SOLO_MESA.json"
ENC_TRAZAS_DIR = ENC_DIR / "trazas"
GOLD_PATH = EXP_DIR / "exploracion" / "ev2_fidelidad" / "preguntas_ev2_fidelidad.json"

GRAFOS = ["v2", "v3", "run_3"]
LABEL_BASE = {"v2": "ev2_base_v2", "v3": "ev2_base_v3", "run_3": "ev2_base_run3"}
SEMILLA_MUESTRA = "adjudicacion-ev2-v1"    # pre-registro §6
FRACCION_MUESTRA = 0.10
SEMILLA_WORKSHEET = "worksheet-ev2-v1"
SAL_ID_FICHA = "worksheet-ev2-v1"
PREFIJO_FICHA = "ADJ-"
ADJ = "requiere_adjudicacion"

# Esperados declarados por el mandato (se verifican, no se asumen)
ESPERADO_FINAL_POR_GRAFO = {          # correcto / parcial / incorrecto / requiere_adjudicacion
    "v2": {"correcto": 3, "parcial": 20, "incorrecto": 7, ADJ: 10},
    "v3": {"correcto": 4, "parcial": 17, "incorrecto": 7, ADJ: 12},
    "run_3": {"correcto": 2, "parcial": 13, "incorrecto": 17, ADJ: 8},
}
ESPERADO_HEREDADOS = 21
ESPERADO_PENDIENTES_S7 = 9
ESPERADO_VOTOS_ADJ_S7 = 24            # declarado por el mandato; se verifica y se reporta
ESPERADO_MUESTRA_CORRECTO = {"v2": 1, "v3": 1, "run_3": 1}
ESPERADO_MUESTRA_PI = {"v2": 3, "v3": 3, "run_3": 3}

ORIGENES = ("heredado_base", "s7_pendiente", "muestra_correcto", "muestra_parcial_incorrecto")


def sha256_path(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def sha256_texto(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def rel_repo(p: Path) -> str:
    return str(Path(p).resolve().relative_to(REPO_DIR))


def sellos_insumos() -> dict:
    return {rel_repo(p): sha256_path(p) for p in
            (BASE_AGREGADOS, BASE_TABLA, ENC_FINALES, ENC_AGREGADOS, ENC_TABLA, GOLD_PATH,
             ENC_DIR / "code" / "agregacion_enc.py", JUEZ_DIR / "mapping.py")}


# --------------------------------------------------------------------------- #
# Carga de insumos                                                             #
# --------------------------------------------------------------------------- #
def cargar_gold() -> dict[str, dict]:
    data = json.loads(GOLD_PATH.read_text(encoding="utf-8"))
    out = {}
    for p in data["preguntas"]:
        crits = [{"criterio": c["criterio"], "cita_textual": c["cita_textual"]}
                 for c in p["gold"]["criterios"]]
        out[p["id"]] = {"pregunta": p["pregunta"], "to": p["to"], "to_nombre": p["to_nombre"],
                        "ancla": list(p["gold"]["ancla"]), "criterios": crits}
    if len(out) != 40 or sum(len(v["criterios"]) for v in out.values()) != 164:
        raise ValueError("gold inesperado")
    return out


def cargar_insumos() -> dict:
    base_agg = json.loads(BASE_AGREGADOS.read_text(encoding="utf-8"))
    base_tab = json.loads(BASE_TABLA.read_text(encoding="utf-8"))
    enc_fin = json.loads(ENC_FINALES.read_text(encoding="utf-8"))
    enc_agg = json.loads(ENC_AGREGADOS.read_text(encoding="utf-8"))
    enc_tab = json.loads(ENC_TABLA.read_text(encoding="utf-8"))
    if base_agg["n_agregados"] != 120 or base_tab["n"] != 120:
        raise ValueError("corrida base inesperada")
    if enc_fin["n_pares_agregados"] != 66 or enc_fin["n_pares_incompletos"] != 0:
        raise ValueError("encadenamiento inesperado")
    if enc_agg["n_agregados"] != 198 or enc_tab["n"] != 198:
        raise ValueError("juez del encadenamiento inesperado")
    return {"base_agg": {a["id_opaco"]: a for a in base_agg["agregados"]},
            "base_tab": {f["id_opaco"]: f for f in base_tab["filas"]},
            "enc_pares": {p["id_opaco_base"]: p for p in enc_fin["pares"]},
            "enc_agg": {a["id_opaco"]: a for a in enc_agg["agregados"]},
            "enc_tab": {f["id_opaco"]: f for f in enc_tab["filas"]},
            "gold": cargar_gold()}


def leer_respuesta_traza(path: Path, sha_esperado: str) -> str:
    t = json.loads(path.read_text(encoding="utf-8"))
    r = (t["trace"].get("final_json") or {}).get("respuesta")
    if not isinstance(r, str) or not r.strip():
        raise ValueError(f"{path}: traza sin respuesta parseada")
    if sha256_texto(r) != sha_esperado:
        raise ValueError(f"{path}: sha256 de la respuesta no coincide con la tabla")
    return r


def respuesta_base(ins: dict, id_opaco_base: str) -> str:
    f = ins["base_tab"][id_opaco_base]
    return leer_respuesta_traza(BASE_TRAZAS_DIR / f["label"] / f"{f['id_pregunta']}.json",
                                f["sha256_respuesta"])


def respuesta_enc(ins: dict, id_opaco_enc: str) -> str:
    f = ins["enc_tab"][id_opaco_enc]
    return leer_respuesta_traza(ENC_TRAZAS_DIR / f["label"] / f"{f['id_pregunta']}.json",
                                f["sha256_respuesta"])


# --------------------------------------------------------------------------- #
# Veredicto final por par y población A                                        #
# --------------------------------------------------------------------------- #
def finales_por_par(ins: dict) -> list[dict]:
    """Un registro por par (pregunta, grafo): veredicto final pre-adjudicación,
    de dónde sale (base / enc) y los votos de re-corrida si los hay."""
    xs = []
    for idb, a in ins["base_agg"].items():
        f = ins["base_tab"][idb]
        rec = {"id_pregunta": f["id_pregunta"], "grafo": f["grafo"], "id_opaco_base": idb,
               "veredicto_base": a["veredicto_pregunta"], "modales_base": a["modales"],
               "sha256_respuesta_base": f["sha256_respuesta"]}
        p = ins["enc_pares"].get(idb)
        if p is None:
            rec.update({"re_corrido": False, "tipo_enc": None, "final": a["veredicto_pregunta"],
                        "fuente_final": "base", "ids_reps": None, "veredictos_reps": None,
                        "via_enc": None})
        else:
            rec.update({"re_corrido": True, "tipo_enc": p["tipo"], "final": p["final"],
                        "fuente_final": "enc", "ids_reps": list(p["ids_reps"]),
                        "veredictos_reps": list(p["veredictos_reps"]), "via_enc": p["via"]})
            if p["veredicto_base"] != a["veredicto_pregunta"]:
                raise ValueError(f"{idb}: veredicto base inconsistente entre unidades")
            # el agregado declarado por el §7 se re-verifica con la regla sellada
            if ag.agregar_par(p["veredictos_reps"]) != p["final"]:
                raise ValueError(f"{idb}: agregado §7 no reproduce con agregar_par")
        xs.append(rec)
    if len({(x["id_pregunta"], x["grafo"]) for x in xs}) != 120:
        raise ValueError("pares repetidos")
    return sorted(xs, key=lambda x: (x["grafo"], x["id_pregunta"]))


def tabla_final_por_grafo(fin: list[dict]) -> dict:
    return {g: {v: sum(1 for x in fin if x["grafo"] == g and x["final"] == v)
                for v in ("correcto", "parcial", "incorrecto", ADJ)} for g in GRAFOS}


def poblacion_a(fin: list[dict], ins: dict) -> dict:
    """Pares con final requiere_adjudicacion. Devuelve heredados, pendientes §7
    y los objetivos de ficha (respuesta a adjudicar) de cada uno."""
    heredados, pendientes = [], []
    for x in fin:
        if x["final"] != ADJ:
            continue
        if not x["re_corrido"]:
            heredados.append({**x, "objetivos": [
                {"id_opaco_respuesta": x["id_opaco_base"], "rep": None, "origen_respuesta": "base",
                 "sha256_respuesta": x["sha256_respuesta_base"],
                 "veredicto_juez_respuesta": x["veredicto_base"], "modales_juez": x["modales_base"]}]})
        else:
            objs = []
            for rep, (ide, v) in enumerate(zip(x["ids_reps"], x["veredictos_reps"]), start=1):
                if v != ADJ:
                    continue
                fe = ins["enc_tab"][ide]
                if fe["rep"] != rep or fe["id_opaco_base"] != x["id_opaco_base"]:
                    raise ValueError(f"{ide}: rep/par inconsistente")
                ae = ins["enc_agg"][ide]
                if ae["veredicto_pregunta"] != v:
                    raise ValueError(f"{ide}: veredicto por respuesta inconsistente")
                objs.append({"id_opaco_respuesta": ide, "rep": rep, "origen_respuesta": "enc",
                             "sha256_respuesta": fe["sha256_respuesta"],
                             "veredicto_juez_respuesta": v, "modales_juez": ae["modales"]})
            if not objs:
                raise ValueError(f"{x['id_opaco_base']}: pendiente §7 sin votos ADJ")
            pendientes.append({**x, "objetivos": objs})
    return {"heredados": heredados, "pendientes_s7": pendientes}


# --------------------------------------------------------------------------- #
# Muestra simétrica §6                                                          #
# --------------------------------------------------------------------------- #
def muestra_estrato(ids_pregunta: list[str]) -> list[str]:
    ids = sorted(ids_pregunta)
    if not ids:
        return []
    k = math.ceil(FRACCION_MUESTRA * len(ids))
    return sorted(random.Random(SEMILLA_MUESTRA).sample(ids, k))


def muestra_b(fin: list[dict], ins: dict) -> dict:
    """ceil(10 %) de los correcto y ceil(10 %) de los parcial+incorrecto por
    grafo, sobre veredictos FINALES; generador nuevo por (grafo, estrato)."""
    por_par = {(x["id_pregunta"], x["grafo"]): x for x in fin}
    out = {"correcto": [], "parcial_incorrecto": [], "detalle_estratos": {}}
    for g in GRAFOS:
        corr = [x["id_pregunta"] for x in fin if x["grafo"] == g and x["final"] == "correcto"]
        pi = [x["id_pregunta"] for x in fin if x["grafo"] == g and x["final"] in ("parcial", "incorrecto")]
        sc, sp = muestra_estrato(corr), muestra_estrato(pi)
        out["detalle_estratos"][g] = {"n_correcto": len(corr), "k_correcto": len(sc), "ids_correcto": sc,
                                      "n_parcial_incorrecto": len(pi), "k_parcial_incorrecto": len(sp),
                                      "ids_parcial_incorrecto": sp}
        for estrato, ids in (("correcto", sc), ("parcial_incorrecto", sp)):
            for q in ids:
                x = por_par[(q, g)]
                out[estrato].append({**x, "objetivos": [objetivo_muestra(x, ins)]})
    return out


def objetivo_muestra(x: dict, ins: dict) -> dict:
    """Respuesta que lleva la ficha de un par muestreado: re-corrida de menor
    rep con veredicto == final si el par fue re-corrido; la base si no."""
    if not x["re_corrido"]:
        return {"id_opaco_respuesta": x["id_opaco_base"], "rep": None, "origen_respuesta": "base",
                "sha256_respuesta": x["sha256_respuesta_base"],
                "veredicto_juez_respuesta": x["veredicto_base"], "modales_juez": x["modales_base"]}
    for rep, (ide, v) in enumerate(zip(x["ids_reps"], x["veredictos_reps"]), start=1):
        if v == x["final"]:
            fe, ae = ins["enc_tab"][ide], ins["enc_agg"][ide]
            return {"id_opaco_respuesta": ide, "rep": rep, "origen_respuesta": "enc",
                    "sha256_respuesta": fe["sha256_respuesta"],
                    "veredicto_juez_respuesta": v, "modales_juez": ae["modales"]}
    raise ValueError(f"{x['id_opaco_base']}: ninguna re-corrida coincide con el final "
                     f"{x['final']} (votos {x['veredictos_reps']})")


# --------------------------------------------------------------------------- #
# Fichas                                                                        #
# --------------------------------------------------------------------------- #
def id_ficha(id_pregunta: str, sha_resp: str) -> str:
    return PREFIJO_FICHA + sha256_texto(f"{SAL_ID_FICHA}|{id_pregunta}|{sha_resp}")[:8]


def construir_fichas(ins: dict) -> dict:
    """Devuelve {"fin", "tabla_final", "pobA", "muestra", "fichas_mesa",
    "worksheet"}. Una ficha por (id_pregunta, sha256 respuesta) distinta; cada
    ficha lista sus objetivos (par, respuesta, origen) en la tabla SOLO_MESA."""
    fin = finales_por_par(ins)
    pobA = poblacion_a(fin, ins)
    muestra = muestra_b(fin, ins)
    gold = ins["gold"]

    fichas: dict[tuple, dict] = {}

    def agregar(x: dict, obj: dict, origen: str):
        clave = (x["id_pregunta"], obj["sha256_respuesta"])
        d = fichas.get(clave)
        if d is None:
            texto = (respuesta_base(ins, obj["id_opaco_respuesta"]) if obj["origen_respuesta"] == "base"
                     else respuesta_enc(ins, obj["id_opaco_respuesta"]))
            d = fichas[clave] = {"id_pregunta": x["id_pregunta"], "sha256_respuesta": obj["sha256_respuesta"],
                                 "respuesta": texto, "objetivos": []}
        d["objetivos"].append({"origen": origen, "id_pregunta": x["id_pregunta"], "grafo": x["grafo"],
                               "id_opaco_base": x["id_opaco_base"], "final_juez_par": x["final"],
                               "fuente_final": x["fuente_final"], "veredictos_reps": x["veredictos_reps"],
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

    # una ficha no puede mezclar orígenes distintos ni pares distintos (por construcción
    # los textos duplicados solo ocurren dentro de un mismo par); se verifica
    for d in fichas.values():
        if len({o["origen"] for o in d["objetivos"]}) != 1 or len({o["id_opaco_base"] for o in d["objetivos"]}) != 1:
            raise ValueError(f"ficha con objetivos heterogéneos: {d['id_pregunta']}")

    # orden: sorted por (id_pregunta, sha256 respuesta) → shuffle con la semilla del worksheet
    claves = sorted(fichas)
    random.Random(SEMILLA_WORKSHEET).shuffle(claves)
    ws, mesa = [], []
    for n, clave in enumerate(claves, start=1):
        d = fichas[clave]
        g = gold[d["id_pregunta"]]
        fid = id_ficha(*clave)
        ws.append({"n": n, "id_ficha": fid, "to": g["to"], "to_nombre": g["to_nombre"],
                   "ancla": g["ancla"], "pregunta": g["pregunta"], "respuesta": d["respuesta"],
                   "criterios": [{"indice": j, "criterio": c["criterio"], "cita_textual": c["cita_textual"],
                                  "veredicto": None} for j, c in enumerate(g["criterios"], start=1)],
                   "observaciones": None})
        mesa.append({"n": n, "id_ficha": fid, "id_pregunta": d["id_pregunta"],
                     "sha256_respuesta": d["sha256_respuesta"], "n_criterios": len(g["criterios"]),
                     "origen": d["objetivos"][0]["origen"], "grafo": d["objetivos"][0]["grafo"],
                     "id_opaco_base": d["objetivos"][0]["id_opaco_base"],
                     "final_juez_par": d["objetivos"][0]["final_juez_par"],
                     "fuente_final": d["objetivos"][0]["fuente_final"],
                     "veredictos_reps": d["objetivos"][0]["veredictos_reps"],
                     "ids_reps": d["objetivos"][0]["ids_reps"],
                     "respuestas": [{"id_opaco_respuesta": o["id_opaco_respuesta"], "rep": o["rep"],
                                     "origen_respuesta": o["origen_respuesta"],
                                     "veredicto_juez_respuesta": o["veredicto_juez_respuesta"],
                                     "modales_juez": o["modales_juez"]} for o in d["objetivos"]]})
    ids = [f["id_ficha"] for f in ws]
    if len(set(ids)) != len(ids):
        raise ValueError("colisión de ids de ficha")
    return {"fin": fin, "tabla_final": tabla_final_por_grafo(fin), "pobA": pobA,
            "muestra": muestra, "worksheet": ws, "fichas_mesa": mesa}


# --------------------------------------------------------------------------- #
# Render                                                                        #
# --------------------------------------------------------------------------- #
INSTRUCCIONES_MD = """\
# Worksheet de adjudicación humana — EV2 fidelidad

Adjudicación según §6 del pre-registro (`docs/preregistro_evaluacion_fidelidad_ev2.md`,
commit be8a84f). Fichas en orden aleatorizado (semilla `{sem}`), numeradas
1..{n}. Cada ficha trae: TO y ancla del gold, la pregunta, la respuesta COMPLETA
del sistema y los criterios del gold sellado con su cita textual.

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
   (todos cumplidos → correcto; ninguno → incorrecto; mezcla → parcial), vía
   `code/cerrar_adjudicacion.py`.
4. Las marcas se vuelcan en `worksheet_adjudicacion.json` (campo `veredicto`
   de cada criterio, en la ficha del mismo `id_ficha`); `observaciones` es
   libre y opcional. Este `.md` es la vista de lectura.
5. Cada ficha se adjudica por sí sola. Las fichas no indican de qué sistema ni
   de qué corrida proviene la respuesta, y no debe intentarse inferirlo.

Marcas válidas: `cumplido` | `no_cumplido`.

---
"""


def render_md(ws: list[dict]) -> str:
    out = [INSTRUCCIONES_MD.format(sem=SEMILLA_WORKSHEET, n=len(ws))]
    for f in ws:
        out.append(f"\n## Ficha {f['n']} — `{f['id_ficha']}`\n")
        out.append(f"**TO:** {f['to_nombre']} (`{f['to']}`) · **Ancla del gold:** {', '.join(f['ancla'])}\n")
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


def worksheet_json(ws: list[dict]) -> dict:
    return {"worksheet": "adjudicacion-ev2-fidelidad", "semilla_orden": SEMILLA_WORKSHEET,
            "n_fichas": len(ws),
            "marcas_validas": list(mapping.VEREDICTOS_CRITERIO[:2]),   # cumplido / no_cumplido
            "instrucciones": ("Marcar `veredicto` de cada criterio con cumplido | no_cumplido, "
                              "contra el PDF del TO y el gold sellado. El veredicto de pregunta lo "
                              "computa code/cerrar_adjudicacion.py (mapping §2); no se completa a mano."),
            "fichas": ws}


def censo_ciego(res: dict) -> str:
    """Conteos publicables (sin grafo): n de fichas por origen y por n de criterios."""
    mesa = res["fichas_mesa"]
    por_origen = Counter(f["origen"] for f in mesa)
    resp_por_origen = Counter()
    for f in mesa:
        resp_por_origen[f["origen"]] += len(f["respuestas"])
    lineas = ["# Censo CIEGO del worksheet de adjudicación (sin grafo)\n",
              f"- fichas: {len(mesa)}",
              f"- por origen (fichas / respuestas cubiertas): " +
              ", ".join(f"{o} {por_origen[o]} / {resp_por_origen[o]}" for o in ORIGENES),
              f"- pares heredados de la base con final requiere_adjudicacion: {len(res['pobA']['heredados'])}",
              f"- pares pendientes del §7: {len(res['pobA']['pendientes_s7'])} "
              f"(votos requiere_adjudicacion: {sum(len(x['objetivos']) for x in res['pobA']['pendientes_s7'])})",
              f"- muestra simétrica §6: correcto {len(res['muestra']['correcto'])}, "
              f"parcial+incorrecto {len(res['muestra']['parcial_incorrecto'])}",
              f"- criterios a marcar: {sum(f['n_criterios'] for f in mesa)}",
              f"- semilla del orden: {SEMILLA_WORKSHEET}; semilla de la muestra: {SEMILLA_MUESTRA}"]
    return "\n".join(lineas) + "\n"


# --------------------------------------------------------------------------- #
# Marcadores que JAMÁS pueden aparecer en el worksheet ciego                    #
# --------------------------------------------------------------------------- #
MARCADORES_WORKSHEET = [
    # identidad de grafo / label (mismos de comun_fidelidad + encadenamiento)
    "ev2_base_v2", "ev2_base_v3", "ev2_base_run3", "reensamblado_v3", "grafo_v2",
    "run_3_ppf_core", "kg_path", "kg_sha256", "graph_fingerprint", "\"grafo\"", "'grafo'",
    "26fac8b49f6c08c1", "run3", "\"label\"", "ev2_enc_",
    # ids originales
    "EV2R-", "EV2E-", "EV2F-",
    # veredictos / metadata del juez y del par
    "\"rep\"", "\"veredicto_juez", "\"modales", "\"fragmento", "fragmentos_reps",
    "requiere_adjudicacion", "\"final", "id_opaco", "sha256", "\"origen", "heredado_base",
    "s7_pendiente", "muestra_correcto", "muestra_parcial", "\"id_pregunta\"", "SOLO_MESA",
    "veredictos_reps", "ids_reps",
]


def buscar_marcadores(texto: str) -> list[str]:
    return [m for m in MARCADORES_WORKSHEET if m in texto]
