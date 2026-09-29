"""
lectura_e6_tanda0.py — U-TANDA0-2A, etapa E6 a: lecturas de grafo de la tanda 0
contra las líneas de base de A4 del pre-registro (docs/preregistro_tanda0.md,
c80b03f), sin umbral (decisión 6), y los pedidos de lectura asentados en la
fila B6.0 fase 2a del plan («LECTURA DE E6 — agregados», puntos 1, 2 y 6).
USD 0, sin API, solo lectura sobre los ensamblados sellados en 1b8916c y las
salidas de E1 a E3 en corpus_tanda0/salida_dirigida/ (entrada de E3).

Qué computa (cada bloque con la fórmula del pre-registro cuando la tiene):
  obs10  — aristas de extracción por unidad = total − referencia −
           rol_fuente esqueleto, sobre 1.763 / 671 / 2.434 unidades (A4.1).
  obs11  — clave `referencias` de reporte_ensamblado_r1.json (A4.2); además,
           mención por mención, las remisiones de los cinco TOs de desarrollo
           que nombran a uno de los cinco nuevos: fuera del inventario en el
           ensamblado de desarrollo y su estado en el de diez.
  vigilancias (1) a (9) — con los instrumentos de A4.3. Solo la parte
           determinística: donde A4.3 pide muestreo y lectura («a definir en
           fase 2»), el mandato no lo definió y se reporta la población.
  plan (1) aristas `referencia` por tipo de nodo de origen.
  plan (2) rechazos de E1 por par (reports/u_audit_tipos_v3/p4_resumen.json).
  plan (6) aristas entre documentos distintos por relación (ver
           DOCUMENTO_DE_NODO).
  aplica_a — condición de cierre del checklist del gate (plan, «Retiro de las
           3 aristas aplica_a»): ninguna de las tres en los kg.json.
  suite  — los 46 ítems de desarrollo contra la entrada KG-Reextraido-r1 de la
           fixture 696f3f94; cinco y diez, informativos.
  intrínsecas y shapes — resumen de las salidas del gate de release (E3).
  costos — gasto real de 2a desde los ledgers y las dbs: E2 (presupuesto
           compartido del runner y fases de estado_corpus.json), re-extracción
           dirigida (su presupuesto) y E5 (tabla_celdas_E5.json, desde las dbs),
           contra la estimación A7 de 69,18 y el tope de 100.

Salidas: reports/tanda0/lectura_e6_tanda0.json y .md (sin fechas: dos corridas
dan archivos byte-idénticos).

Uso:  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/tanda0/code/lectura_e6_tanda0.py
"""

from __future__ import annotations

import hashlib
import json
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
REPO = CODE_DIR.parents[3]
EXP = REPO / "data" / "experiment"
RV2 = EXP / "reextraccion_v2"
ENS = RV2 / "corpus_tanda0"
SALIDA = ENS / "salida_dirigida"                # entrada de E3 (U-TANDA0-2A-DIR)
R1 = RV2 / "corpus_v2" / "salida_r1"
REPORTS = REPO / "reports" / "tanda0"
OUT_JSON = REPORTS / "lectura_e6_tanda0.json"
OUT_MD = REPORTS / "lectura_e6_tanda0.md"

TOS_DEV = ("pro", "cla", "ric", "cap", "ext")
TOS_NUEVOS = ("ctacte", "lingob", "polcre", "pagjub", "docvig")
ENSAMBLADOS = {
    "desarrollo": {"dir": "ens_desarrollo", "unidades": 1763, "tos": TOS_DEV,
                   "sha": "eab2fdd01dec4dad026d596a793919e666920fab127d7efb14b5b00857ae64ef",
                   "nombre": "KG-Tanda0-Desarrollo-r1"},
    "cinco": {"dir": "ens_cinco", "unidades": 671, "tos": TOS_NUEVOS,
              "sha": "4097d4fd3f300cb1c2cf09bef59e3ccb9a30b1de18334e6230102a5a3106d00a",
              "nombre": "ens_cinco/r1"},
    "diez": {"dir": "ens_diez", "unidades": 2434, "tos": TOS_DEV + TOS_NUEVOS,
             "sha": "dd42d6d9c0c8379da90ec4ed4e4659157a960a0d1ceaf8af5a008bdd9cad9010",
             "nombre": "KG-Tanda0-Diez-r1"},
}
SHA_R1 = "0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a"
SHA_P4 = "e63e2618faa96708c56fb2f650cacaacd0fcb60600c67b63c788096fa6c2f5f5"
SHA_FIXTURE = "696f3f941e0d64c3a2def37159d45f7814b546f9d461f6727f43db3eda160f5e"
SHA_INTR_R1 = "d1fa3ee0f49c3957783d6271ca37962283f08df6b8bca01ccf977d0394bfeb57"

# A4.1 (bandas pre-declaradas como ayuda de lectura, no umbral)
BANDAS_OBS10 = {"desarrollo": (6.81, 8.0), "cinco": (5.0, 8.0)}
BASE_OBS10 = {"total": 17772, "referencia": 5680, "esqueleto": 82, "extraccion": 12010,
              "por_unidad": 6.81}
# A4.2
BASE_OBS11 = {"menciones": 1089, "resueltas": 837, "parciales": 20, "irresolubles": 252,
              "aristas_referencia_nuevas": 5645, "aristas_cross_to": 188, "fuera_inventario": 106,
              "normas_fuera_inventario": 54}
CLAVES_CRUCE = {"ctacte": ["cuenta corriente"], "lingob": ["gobierno societario"],
                "polcre": ["politica de credito"],
                "pagjub": ["seguridad social", "anses", "pago de beneficios"],
                "docvig": ["documentos de identificacion"]}
MOTIVO_FUERA = "norma fuera del inventario del subset"
# A4.3 vigilancia (8): 124 / (3.905 + 124)
BASE_V8 = {"sujeto_propuesto": 124, "sujeto_id": 3905, "tasa_pct": 3.08}
ID_V9 = "Sujeto_entidad_originante_de_transferencia"
PREFIJO_V7 = "Sujeto_rol_alcance_"
# Checklist del gate: las tres aplica_a adjudicadas como falsedad (U-COB-A)
APLICA_A_RETIRO = [("Transferencias entre cuentas CVU mismo PSPCP", "Sujeto_pspcp"),
                   ("Transferencias entre cuentas CVU mismo PSPCP", "Sujeto_entidad_financiera"),
                   ("Presentación de informaciones al BCRA", "Sujeto_pscpp")]
DOCUMENTO_DE_NODO = ("documento de un nodo = conjunto de valores `to` de sus `provenances`; una arista "
                     "va entre documentos distintos si origen y destino tienen un solo documento cada "
                     "uno y son distintos; si alguno tiene más de un documento (Sujeto del catálogo, "
                     "nodos fundidos) se cuenta aparte como «con nodo multidocumento»")


def sha256(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def rel(p: Path) -> str:
    return str(Path(p).resolve().relative_to(REPO))


def leer(p: Path):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def norm(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", (s or "").lower())
                   if unicodedata.category(c) != "Mn")


def rol_fuente(e: dict):
    return e.get("rol_fuente") or (e.get("provenance") or {}).get("rol_fuente")


def cargar_kg(clave: str) -> dict:
    p = ENS / ENSAMBLADOS[clave]["dir"] / "r1" / "kg.json"
    if sha256(p) != ENSAMBLADOS[clave]["sha"]:
        raise RuntimeError(f"{rel(p)} con sha distinto del sellado")
    return leer(p)


def docs_de(n: dict) -> frozenset:
    return frozenset(p.get("to") for p in (n.get("provenances") or []) if p.get("to"))


# --------------------------------------------------------------------------- #
# Observación (10)                                                             #
# --------------------------------------------------------------------------- #
def obs10(kgs: dict) -> dict:
    out = {"formula": "extraccion = total − referencia − rol_fuente esqueleto (A4.1); por unidad sobre "
                      "las unidades de E0", "linea_de_base_r1": BASE_OBS10, "ensamblados": {}}
    for c, kg in kgs.items():
        E = kg["edges"]
        tot, ref = len(E), sum(e["relation"] == "referencia" for e in E)
        esq = sum(rol_fuente(e) == "esqueleto" for e in E)
        ps = sum(e["relation"] == "padre_sugerido" for e in E)
        ext = tot - ref - esq
        u = ENSAMBLADOS[c]["unidades"]
        x = {"total": tot, "referencia": ref, "esqueleto": esq, "padre_sugerido": ps,
             "extraccion": ext, "unidades": u, "por_unidad": round(ext / u, 2),
             "sin_padre_sugerido": ext - ps, "por_unidad_sin_padre_sugerido": round((ext - ps) / u, 2)}
        if c in BANDAS_OBS10:
            lo, hi = BANDAS_OBS10[c]
            x["banda"] = [lo, hi]
            x["lectura"] = ("dentro de la banda" if lo <= x["por_unidad"] <= hi else
                            "debajo de la banda" if x["por_unidad"] < lo else "encima de la banda")
        else:
            x["lectura"] = "informativo (A4.1 no predice sobre el ensamblado de diez)"
        out["ensamblados"][c] = x
    return out


# --------------------------------------------------------------------------- #
# Observación (11)                                                             #
# --------------------------------------------------------------------------- #
def obs11() -> dict:
    out = {"linea_de_base_r1": BASE_OBS11, "ensamblados": {}}
    for c, e in ENSAMBLADOS.items():
        r = leer(ENS / e["dir"] / "r1" / "reporte_ensamblado_r1.json")["referencias"]
        out["ensamblados"][c] = {
            **{k: r[k] for k in ("menciones", "resueltas", "parciales", "irresolubles",
                                 "aristas_referencia_nuevas", "aristas_cross_to")},
            "fuera_inventario": r["irresolubles_por_motivo"].get(MOTIVO_FUERA, 0),
            "normas_fuera_inventario": len(r["normas_fuera_inventario"])}
    d, z = out["ensamblados"]["desarrollo"], out["ensamblados"]["diez"]
    out["predicciones"] = [
        {"metrica": "aristas_cross_to en el grafo de desarrollo re-extraído", "predicho": "188 ± 20",
         "observado": d["aristas_cross_to"],
         "lectura": "dentro" if 168 <= d["aristas_cross_to"] <= 208 else "fuera"},
        {"metrica": "aristas_cross_to en el ensamblado de diez", "predicho": "mayor que 188",
         "observado": z["aristas_cross_to"],
         "lectura": "cumple" if z["aristas_cross_to"] > 188 else "no cumple"}]
    # mención por mención: remisiones de desarrollo que nombran a uno de los cinco
    def nombra(m):
        n = norm(m.get("norma_nombrada") or "")
        return next((to for to, ks in CLAVES_CRUCE.items() if any(k in n for k in ks)), None)
    rem_d = leer(ENS / "ens_desarrollo" / "r1" / "referencias_remisiones.json")
    rem_z = leer(ENS / "ens_diez" / "r1" / "referencias_remisiones.json")
    fuera_d = [m for m in rem_d if m["to_origen"] in TOS_DEV and m.get("motivo") == MOTIVO_FUERA]
    nombran_d = Counter(nombra(m) for m in fuera_d if nombra(m))
    hacia_nuevos_z = [m for m in rem_z if m["to_origen"] in TOS_DEV and m["to_destino"] in TOS_NUEVOS]
    siguen_fuera_z = [m for m in rem_z if m["to_origen"] in TOS_DEV and m.get("motivo") == MOTIVO_FUERA
                      and nombra(m)]
    out["menciones_desarrollo_a_los_cinco"] = {
        "regla": ("remisiones con to_origen en los cinco de desarrollo; en desarrollo, las de motivo "
                  f"«{MOTIVO_FUERA}» cuya norma_nombrada normalizada contiene una clave del cruce de "
                  "A4.2; en diez, las que tienen to_destino en uno de los cinco nuevos"),
        "fuera_del_inventario_en_desarrollo_por_to": dict(sorted(nombran_d.items())),
        "fuera_del_inventario_en_desarrollo_total": sum(nombran_d.values()),
        "en_diez_hacia_los_cinco_por_estado": dict(Counter(m["estado"] for m in hacia_nuevos_z)),
        "en_diez_hacia_los_cinco_por_to": dict(Counter(m["to_destino"] for m in hacia_nuevos_z)),
        "en_diez_hacia_los_cinco_con_destino_de_punto": sum(
            1 for m in hacia_nuevos_z if m["estado"] != "irresoluble" and m.get("puntos")),
        "en_diez_siguen_fuera_del_inventario": len(siguen_fuera_z),
        "prediccion": "4 de 106 (las 2 de polcre y las 2 de docvig, sobre las menciones de r1)",
        "nota": ("las menciones salen de la extracción (E1), no del texto de E0: el ensamblado de "
                 f"desarrollo tiene {d['menciones']} contra {BASE_OBS11['menciones']} de r1, así que las 106 "
                 "de r1 no se pueden seguir una por una; el conteo comparable es el de esta clave")}
    return out


# --------------------------------------------------------------------------- #
# Vigilancias (1) a (9)                                                        #
# --------------------------------------------------------------------------- #
def lineas(p: Path):
    for ln in Path(p).read_text(encoding="utf-8").splitlines():
        if ln.strip():
            yield json.loads(ln)


def vigilancias(kgs: dict) -> dict:
    todos = TOS_DEV + TOS_NUEVOS
    v = {}
    # (1) Condicion: población
    v["1"] = {"nombre": "migraciones tipo-Condicion contra la guarda de modalidad",
              "linea_de_base": "1/12 en fresca", "medida": "no medida: el muestreo quedó «a definir en "
              "fase 2» (A4.3) y el mandato no lo definió; se reporta la población",
              "poblacion": {c: {"nodos_Condicion": sum(n["type"] == "Condicion" for n in kg["nodes"]),
                                "aristas_condicion_de": sum(e["relation"] == "condicion_de" for e in kg["edges"])}
                            for c, kg in kgs.items()}}
    # (2) vaciamientos: unidades con 0 relaciones aceptadas
    vac = {}
    for to in todos:
        prim = {}
        for x in lineas(SALIDA / to / "extracciones_e1.jsonl"):
            prim.setdefault(x["chunk_id"], x)           # primer intento por unidad
        fin = {}
        for x in lineas(SALIDA / to / f"extracciones_finales_{to}.jsonl"):
            fin[x["chunk_id"]] = x                      # último registro por unidad
        prim, fin = list(prim.values()), list(fin.values())
        vac[to] = {"unidades_e1": len(prim), "unidades_finales": len(fin),
                   "cero_relaciones_primer_intento": sum(1 for x in prim if not x.get("error")
                                                         and not (x.get("validacion") or {}).get("relaciones")),
                   "cero_relaciones_final": sum(1 for x in fin if not x.get("error")
                                                and not (x.get("validacion") or {}).get("relaciones")),
                   "con_error_final": sum(1 for x in fin if x.get("error"))}
    v["2"] = {"nombre": "vaciamientos (unidad sin relaciones aceptadas)", "linea_de_base": "v1 2/43 · v2 2/27",
              "medida": "conteo de unidades con 0 relaciones aceptadas; la lectura de muestra que A4.3 "
                        "cruza con ese conteo no se hizo (muestreo no definido)",
              "por_to": vac,
              "total_cero_relaciones_final": sum(x["cero_relaciones_final"] for x in vac.values()),
              "total_unidades": sum(x["unidades_e1"] for x in vac.values())}
    # (3) duplicación entre cajas
    v["3"] = {"nombre": "duplicación de contenido entre cajas", "linea_de_base": "5 casos v1",
              "medida": "no medida: A4.3 deja el muestreo «a definir en fase 2» y el mandato no fijó "
                        "instrumento"}
    # (4) TextoOrdenado por TO
    to_por = {}
    for c, kg in kgs.items():
        cnt = Counter()
        for n in kg["nodes"]:
            if n["type"] == "TextoOrdenado":
                for d in docs_de(n) or {"(sin to)"}:
                    cnt[d] += 1
        to_por[c] = dict(sorted(cnt.items()))
    v["4"] = {"nombre": "un nodo TextoOrdenado por TO", "linea_de_base": "2 archivos afectados en lecturas",
              "por_ensamblado": to_por,
              "todos_uno": all(set(x.values()) == {1} and set(x) == set(ENSAMBLADOS[c]["tos"])
                               for c, x in to_por.items())}
    # (5) vocabulario retirado + S20
    res = {to: leer(SALIDA / to / "resumen_e1.json") for to in todos}
    s20 = next((x["validacion"]["metricas"] for x in lineas(SALIDA / "ext" / "extracciones_e1.jsonl")
                if x["chunk_id"] == "ext::10.4.3.1"), None)
    v["5"] = {"nombre": "emisiones residuales de requisito_de_estructura", "linea_de_base": "0 por construcción",
              "tipo_obligacion_requisito_de_estructura": {to: res[to]["tipo_obligacion_requisito_de_estructura"] for to in todos},
              "tipo_obligacion_normalizados": {to: res[to]["tipo_obligacion_normalizados"] for to in todos},
              "hallazgo_S20_ext_10_4_3_1": {k: s20[k] for k in ("tipo_obligacion_normalizados",
                                                               "tipo_obligacion_requisito_de_estructura",
                                                               "relations_in", "relations_out", "rechazos_por_motivo")}}
    # (6) unidades propias vacías: health-check de E0 (E1 de 2a)
    hc = leer(REPORTS / "healthcheck_e0_tanda0_cinco.json")
    v["6"] = {"nombre": "unidades propias vacías (health-check de E0)", "linea_de_base": "sin línea de base numérica",
              "fuente": rel(REPORTS / "healthcheck_e0_tanda0_cinco.json"),
              "por_to": {to: {"veredicto": hc[to].get("veredicto"),
                              "senales": hc[to].get("senales")} for to in TOS_NUEVOS}}
    # (7) ejecuta con sujeto rol_alcance
    v["7"] = {"nombre": "roles de alcance en ejecuta", "linea_de_base": "n = 1 en la muestra pareada de B5.4",
              "medida": "población (aristas ejecuta con origen Sujeto_rol_alcance_<to>); la tasa sin apoyo "
                        "textual pide muestreo, no definido",
              "por_ensamblado": {c: {"ejecuta": sum(e["relation"] == "ejecuta" for e in kg["edges"]),
                                     "ejecuta_con_rol_alcance": sum(
                                         1 for e in kg["edges"] if e["relation"] == "ejecuta"
                                         and str(e["source"]).startswith(PREFIJO_V7))}
                                 for c, kg in kgs.items()}}
    # (8) sujeto_propuesto contra sujeto_id en las relaciones aceptadas de E1
    def cont8(tos):
        prop = sid = 0
        for to in tos:
            for x in lineas(SALIDA / to / f"extracciones_finales_{to}.jsonl"):
                for r in (x.get("validacion") or {}).get("relaciones") or []:
                    if r.get("sujeto_propuesto"):
                        prop += 1
                    elif r.get("sujeto_id"):
                        sid += 1
        return {"sujeto_propuesto": prop, "sujeto_id": sid,
                "tasa_pct": round(100 * prop / (prop + sid), 2) if prop + sid else None}
    v["8"] = {"nombre": "tasa de sujeto_propuesto", "linea_de_base": BASE_V8,
              "fuente": "validacion.relaciones de extracciones_finales_<to>.jsonl (relaciones aceptadas de E1)",
              "desarrollo": cont8(TOS_DEV), "cinco": cont8(TOS_NUEVOS), "diez": cont8(todos)}
    # (9) emisiones del id originante
    em = {}
    for to in todos:
        em[to] = sum(1 for x in lineas(SALIDA / to / f"extracciones_finales_{to}.jsonl")
                     for r in (x.get("validacion") or {}).get("relaciones") or []
                     if r.get("sujeto_id") == ID_V9)
    v["9"] = {"nombre": f"emisiones de {ID_V9}", "linea_de_base": "13 menciones / 5 TOs en fase 1; 2→1 en la unidad adversarial",
              "emisiones_E1_por_to": em,
              "aristas_en_kg": {c: sum(1 for e in kg["edges"] if ID_V9 in (e["source"], e["target"]))
                                for c, kg in kgs.items()},
              "nota": "A4.3: ninguno de los cinco nuevos es del dominio de pagos"}
    return v


# --------------------------------------------------------------------------- #
# Pedidos del plan (1), (2) y (6)                                              #
# --------------------------------------------------------------------------- #
def plan1(kgs: dict) -> dict:
    out = {}
    for c, kg in kgs.items():
        tipo = {n["id"]: n["type"] for n in kg["nodes"]}
        cnt = Counter(tipo.get(e["source"], "(desconocido)") for e in kg["edges"] if e["relation"] == "referencia")
        out[c] = {"por_tipo_de_origen": dict(sorted(cnt.items())),
                  "desde_Condicion_Potestad_Definicion": sum(cnt.get(t, 0) for t in ("Condicion", "Potestad", "Definicion"))}
    return out


def plan2() -> dict:
    p = REPO / "reports" / "u_audit_tipos_v3" / "p4_resumen.json"
    if sha256(p) != SHA_P4:
        raise RuntimeError("p4_resumen.json con sha distinto")
    d = leer(p)
    pares = sorted(d["por_par"], key=lambda x: -x["n"])
    return {"fuente": rel(p), "sha256": SHA_P4, "rechazos_firma_invalida": d["rechazos_firma_invalida"],
            "n_pares": len(pares), "por_to": d["por_to"], "primeros_pares": pares[:8],
            "suma_por_par": d["suma_por_par"]}


def plan6(kgs: dict) -> dict:
    out = {"regla": DOCUMENTO_DE_NODO, "ensamblados": {}}
    for c, kg in kgs.items():
        docs = {n["id"]: docs_de(n) for n in kg["nodes"]}
        por = defaultdict(Counter)
        for e in kg["edges"]:
            a, b = docs.get(e["source"], frozenset()), docs.get(e["target"], frozenset())
            if not a or not b:
                cat = "sin_procedencia"
            elif len(a) > 1 or len(b) > 1:
                cat = "con_nodo_multidocumento"
            elif a == b:
                cat = "mismo_documento"
            else:
                cat = "entre_documentos"
            grupo = ("referencia" if e["relation"] == "referencia" else
                     "esqueleto" if rol_fuente(e) == "esqueleto" else "extraccion")
            por[(grupo, e["relation"])][cat] += 1
        tot = Counter()
        for (g, _), cc in por.items():
            for k, n in cc.items():
                tot[(g, k)] += n
        out["ensamblados"][c] = {
            "por_grupo": {g: {k: tot[(g, k)] for k in ("mismo_documento", "entre_documentos",
                                                       "con_nodo_multidocumento", "sin_procedencia")}
                          for g in ("extraccion", "referencia", "esqueleto")},
            "entre_documentos_por_relacion": {f"{g}:{r}": cc["entre_documentos"]
                                              for (g, r), cc in sorted(por.items()) if cc["entre_documentos"]},
            "nodos_multidocumento": sum(1 for d in docs.values() if len(d) > 1)}
    return out


def aplica_a(kgs: dict) -> dict:
    out = {}
    for c, kg in kgs.items():
        lab = {n["id"]: n.get("label") for n in kg["nodes"]}
        hall = [(o, s) for o, s in APLICA_A_RETIRO
                if any(e["relation"] == "aplica_a" and lab.get(e["source"]) == o and e["target"] == s
                       for e in kg["edges"])]
        out[c] = {"presentes": len(hall),
                  "nodos_de_ri_tii_o_ri_pscpp": sum(1 for n in kg["nodes"] if docs_de(n) & {"ri_tii", "ri_pscpp"})}
    return {"condicion": "el kg.json de la tanda no contiene ninguna de las tres (checklist del gate)",
            "por_ensamblado": out,
            "nota": "control vacuo en la tanda 0: ri_tii y ri_pscpp no están en ningún ensamblado"}


def suite() -> dict:
    fx_p = REPO / "scripts" / "regression_kg_esperado.json"
    if sha256(fx_p) != SHA_FIXTURE:
        raise RuntimeError("fixture con sha distinto")
    r1 = leer(fx_p)["estado_esperado"]["KG-Reextraido-r1"]
    if r1["kg_sha256"] != SHA_R1:
        raise RuntimeError("entrada de r1 inesperada en la fixture")
    out = {"fixture": rel(fx_p), "fixture_sha256": SHA_FIXTURE, "ensamblados": {}}
    for c in ENSAMBLADOS:
        rep = leer(REPORTS / f"regression_ens_{c}.json")
        est = {it["id"]: it["estado"] for it in rep["items"]}
        x = {"resumen": rep["resumen"], "reporte": rel(REPORTS / f"regression_ens_{c}.json")}
        if c == "desarrollo":
            base = {k: v["estado"] for k, v in r1["items"].items()}
            if set(base) != set(est):
                raise RuntimeError("ítems de la suite distintos de la fixture")
            x["transiciones_desde_r1"] = {f"{a} → {b}": n for (a, b), n in
                                          sorted(Counter((base[i], est[i]) for i in base).items())}
            x["cambian"] = sorted(i for i in base if base[i] != est[i])
            x["por_item"] = [{"id": i, "r1": base[i], "desarrollo": est[i]} for i in sorted(base)]
        out["ensamblados"][c] = x
    return out


def intrinsecas() -> dict:
    p_r1 = EXP / "metricas_intrinsecas" / "kg_reextraido_r1.json"
    if sha256(p_r1) != SHA_INTR_R1:
        raise RuntimeError("línea de base de intrínsecas de r1 con sha distinto")
    def resumir(p):
        m = leer(p)["metricas"]
        return {k: (v.get("valor") if isinstance(v, dict) else v) for k, v in sorted(m.items())}
    out = {"r1": resumir(p_r1)}
    for c in ENSAMBLADOS:
        out[c] = resumir(EXP / "metricas_intrinsecas" / f"tanda0_ens_{c}.json")
    return out


def shapes() -> dict:
    out = {}
    for c in ENSAMBLADOS:
        s = leer(REPORTS / f"shapes_ens_{c}.json")
        out[c] = {"veredicto": s["veredicto"], "bloqueantes_en_fail": s["bloqueantes_en_fail"],
                  "resultado_por_shape": {k: v.get("result") for k, v in sorted(s["shapes"].items())}}
    return out


def costos() -> dict:
    pc = leer(ENS / "salida" / "presupuesto_compartido.json")
    fases = leer(ENS / "salida" / "estado_corpus.json")["fases_cerradas"]
    e1 = round(sum(v["gasto_usd"] for k, v in fases.items() if k.endswith(":e1")), 6)
    e3 = round(sum(v["gasto_usd"] for k, v in fases.items() if k.endswith(":e3")), 6)
    if round(e1 + e3, 6) != round(pc["gasto_usd"], 6):
        raise RuntimeError("fases de E2 no cierran contra el presupuesto compartido")
    dirig = leer(SALIDA / "presupuesto_reextraccion_dirigida.json")["gasto_usd"]
    t5 = leer(REPORTS / "tabla_celdas_E5.json")
    e5 = t5["gasto_E5"]
    total = round(pc["gasto_usd"] + dirig + e5, 6)
    return {"E2": {"usd": pc["gasto_usd"], "E1": e1, "E3_con_reintentos_de_E1": e3,
                   "fuente": rel(ENS / "salida" / "presupuesto_compartido.json") + " y estado_corpus.json#fases_cerradas",
                   "tope": pc["tope_usd"]},
            "reextraccion_dirigida": {"usd": dirig, "fuente": rel(SALIDA / "presupuesto_reextraccion_dirigida.json"),
                                      "tope": 1.0},
            "E5": {"usd": e5, "por_celda": {c: t5["celdas"][c]["gasto_total"] for c in ("C2", "C3", "C4", "C5")},
                   "fuente": rel(REPORTS / "tabla_celdas_E5.json") + " (desde las dbs de ev2_tanda0/cache/)", "tope": 40.0},
            "E5c_adjudicacion_y_cierre": {"usd": 0.0},
            "total_2a": total, "estimacion_A7": 69.18, "tope_unidad": 100.0,
            "total_sobre_estimacion": round(total / 69.18, 3)}


# --------------------------------------------------------------------------- #
def computar() -> dict:
    kgs = {c: cargar_kg(c) for c in ENSAMBLADOS}
    if sha256(R1 / "kg.json") != SHA_R1:
        raise RuntimeError("kg.json de r1 con sha distinto")
    return {"unidad": "U-TANDA0-2A E6 a (USD 0)",
            "insumos": {"ensamblados": {c: {"kg": rel(ENS / e["dir"] / "r1" / "kg.json"), "sha256": e["sha"],
                                            "nombre": e["nombre"]} for c, e in ENSAMBLADOS.items()},
                        "entrada_E3": rel(SALIDA)},
            "obs10": obs10(kgs), "obs11": obs11(), "vigilancias": vigilancias(kgs),
            "plan1_referencia_por_tipo_de_origen": plan1(kgs), "plan2_rechazos_E1_por_par": plan2(),
            "plan6_aristas_entre_documentos": plan6(kgs), "aplica_a": aplica_a(kgs),
            "suite": suite(), "intrinsecas": intrinsecas(), "shapes": shapes(), "costos": costos()}


def render_md(r: dict) -> str:
    L = ["# Lecturas de grafo de E6 (U-TANDA0-2A, tanda 0)", "",
         "Generado por `data/experiment/tanda0/code/lectura_e6_tanda0.py` desde "
         "`reports/tanda0/lectura_e6_tanda0.json`. Sin umbral (decisión 6 del pre-registro).", "",
         "## Observación (10): aristas de extracción por unidad (A4.1)", "",
         "| ensamblado | total | referencia | esqueleto | extracción | unidades | por unidad | banda | lectura |",
         "|---|---|---|---|---|---|---|---|---|",
         f"| r1 (base) | 17772 | 5680 | 82 | 12010 | 1763 | 6.81 | | |"]
    for c, x in r["obs10"]["ensamblados"].items():
        L.append(f"| {c} | {x['total']} | {x['referencia']} | {x['esqueleto']} | {x['extraccion']} | "
                 f"{x['unidades']} | {x['por_unidad']} | {x.get('banda', '')} | {x['lectura']} |")
    o = r["obs11"]
    L += ["", "## Observación (11): remisiones y aristas entre documentos (A4.2)", "",
          "| ensamblado | menciones | resueltas | parciales | irresolubles | fuera del inventario | aristas_cross_to |",
          "|---|---|---|---|---|---|---|",
          "| r1 (base) | 1089 | 837 | 20 | 252 | 106 | 188 |"]
    for c, x in o["ensamblados"].items():
        L.append(f"| {c} | {x['menciones']} | {x['resueltas']} | {x['parciales']} | {x['irresolubles']} | "
                 f"{x['fuera_inventario']} | {x['aristas_cross_to']} |")
    L += [""] + [f"- {p['metrica']}: predicho {p['predicho']}, observado {p['observado']} ({p['lectura']})"
                 for p in o["predicciones"]]
    m = o["menciones_desarrollo_a_los_cinco"]
    L += [f"- remisiones de desarrollo a los cinco: fuera del inventario en desarrollo "
          f"{m['fuera_del_inventario_en_desarrollo_total']} {m['fuera_del_inventario_en_desarrollo_por_to']}; "
          f"en diez hacia los cinco, por estado {m['en_diez_hacia_los_cinco_por_estado']}, por TO "
          f"{m['en_diez_hacia_los_cinco_por_to']}; siguen fuera del inventario {m['en_diez_siguen_fuera_del_inventario']}",
          f"- {m['nota']}", "", "## Vigilancias (1) a (9) (A4.3)", ""]
    for k, x in r["vigilancias"].items():
        cuerpo = {kk: vv for kk, vv in x.items() if kk not in ("nombre", "linea_de_base")}
        L.append(f"- ({k}) {x['nombre']} — línea de base: {x['linea_de_base']}. "
                 f"{json.dumps(cuerpo, ensure_ascii=False, sort_keys=True)}")
    L += ["", "## Plan (1): aristas referencia por tipo de origen", ""]
    for c, x in r["plan1_referencia_por_tipo_de_origen"].items():
        L.append(f"- {c}: {x['por_tipo_de_origen']}; desde Condicion, Potestad o Definicion: "
                 f"{x['desde_Condicion_Potestad_Definicion']}")
    p2 = r["plan2_rechazos_E1_por_par"]
    L += ["", "## Plan (2): rechazos de E1 por par", "",
          f"- {p2['rechazos_firma_invalida']} rechazos `firma_invalida` en {p2['n_pares']} pares "
          f"(`{p2['fuente']}`, sha256 `{p2['sha256'][:16]}…`); primeros pares: "
          + "; ".join(f"{x['origen']} –{x['predicado']}→ {x['destino']} {x['n']}" for x in p2["primeros_pares"]),
          "", "## Plan (6): aristas entre documentos distintos", "", f"Regla: {r['plan6_aristas_entre_documentos']['regla']}.", ""]
    for c, x in r["plan6_aristas_entre_documentos"]["ensamblados"].items():
        L.append(f"- {c}: {x['por_grupo']}; nodos multidocumento {x['nodos_multidocumento']}")
        L.append(f"  - entre documentos por relación: {x['entre_documentos_por_relacion']}")
    a = r["aplica_a"]
    L += ["", "## Control de las tres aplica_a (checklist del gate)", "",
          f"- {a['por_ensamblado']}; {a['nota']}", "", "## Suite de regresión", ""]
    for c, x in r["suite"]["ensamblados"].items():
        L.append(f"- {c}: {x['resumen']}")
    d = r["suite"]["ensamblados"]["desarrollo"]
    L += [f"- desarrollo contra la entrada KG-Reextraido-r1 de la fixture: {d['transiciones_desde_r1']}", "",
          "| ítem | r1 (fixture) | desarrollo |", "|---|---|---|"]
    L += [f"| {x['id']} | {x['r1']} | {x['desarrollo']} |" for x in d["por_item"]]
    L += ["", "## Intrínsecas (generación 3) y shapes", "",
          "| métrica | r1 | desarrollo | cinco | diez |", "|---|---|---|---|---|"]
    it = r["intrinsecas"]
    for k in it["r1"]:
        L.append(f"| {k} | {it['r1'][k]} | {it['desarrollo'].get(k)} | {it['cinco'].get(k)} | {it['diez'].get(k)} |")
    L += [""] + [f"- shapes {c}: {x['veredicto']}; bloqueantes en FAIL {x['bloqueantes_en_fail']}"
                 for c, x in r["shapes"].items()]
    k = r["costos"]
    L += ["", "## Costo real de 2a", "", "| etapa | USD | tope |", "|---|---|---|",
          f"| E2 (E1 {k['E2']['E1']} + E3 con reintentos {k['E2']['E3_con_reintentos_de_E1']}) | {k['E2']['usd']} | {k['E2']['tope']} |",
          f"| re-extracción dirigida | {k['reextraccion_dirigida']['usd']} | {k['reextraccion_dirigida']['tope']} |",
          f"| E5 {k['E5']['por_celda']} | {k['E5']['usd']} | {k['E5']['tope']} |",
          "| E5.c (adjudicación y cierre) | 0.0 | |",
          f"| **total 2a** | **{k['total_2a']}** | {k['tope_unidad']} (estimación A7 {k['estimacion_A7']}) |"]
    return "\n".join(L) + "\n"


def main() -> int:
    r1, r2 = computar(), computar()
    if json.dumps(r1, sort_keys=True, ensure_ascii=False) != json.dumps(r2, sort_keys=True, ensure_ascii=False):
        raise RuntimeError("doble cómputo NO idéntico")
    OUT_JSON.write_text(json.dumps(r1, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_md(json.loads(OUT_JSON.read_text(encoding="utf-8"))), encoding="utf-8")
    print(f"-> {rel(OUT_JSON)}\n-> {rel(OUT_MD)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
