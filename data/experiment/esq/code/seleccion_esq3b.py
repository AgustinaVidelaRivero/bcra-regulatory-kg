"""
seleccion_esq3b.py — FASE (b) de U-ESQ-3b ($0): derivación MECÁNICA de las
unidades de los dos brazos desde el worksheet de ESQ-2, y persistencia de la
selección ANTES de extraer.

Reglas selladas que este módulo implementa sin re-decidir (pre-registro
`01bf046` §2 y §3):

BRAZO OBJETIVO (§2) — unidades nombradas por número de ficha, más las de R8:
  R1  f. 26, f. 15
  R2  f. 39
  R3  f. 25, f. 46  ·  contraste anti-atracción f. 37
  R4  f. 46, f. 19
  R5  f. 63, f. 38
  R6a f. 44  ·  corroboran f. 62, f. 65
  R7  f. 32
  R8  «unidades de las 75 fichas cuyas extracciones persistidas contienen
      tripletas `aplica_a` descartadas por `firma_invalida` (derivación
      mecánica desde el campo de validación)» — se DERIVA acá, no se
      transcribe.
  R9  f. 67
El mapeo ficha n → chunk_id sale del worksheet (`cobertura/fichas/
worksheet_fichas_esq2.json`), nunca de una lista copiada a mano.

BRAZO REGRESIÓN (§3, CORREGIDO por la Adenda 1 §2, `f1fe0d8`) — «todas las
fichas con q1 = sí_completo y q2 = ninguna, más — hasta completar 35 unidades —
fichas azarosas con q2 = ninguna en orden por `chunk_id`, y DESPUÉS fichas
dirigidas con q2 = ninguna en orden por `chunk_id`; excluidas las unidades del
brazo objetivo».
Fe de erratas registrada en la adenda: el «35» del pre-registro original era el
conteo bruto de fichas q2=ninguna del worksheet SIN aplicar la exclusión del
brazo objetivo, con lo que era inalcanzable por construcción (la regla original
producía 22). El completado abierto a dirigidas da 26 con el worksheet actual;
la métrica, la predicción única y la regla de falla del §3 no cambian.
El origen (azarosa / dirigida) sale de `cobertura/orden/
seleccion_muestra_esq2.json`; las marcas q1/q2 salen del worksheet.

Determinismo: la salida NO lleva timestamp ni nada dependiente del entorno —
es función pura de los tres insumos (worksheet, selección de muestra,
extracciones persistidas), cuyos sha256 viaja en el archivo. Dos corridas
producen bytes idénticos (lo verifica el selftest).

Salida: cobertura/orden/seleccion_brazos_esq3b.json  (archivo NUEVO; nada
preexistente de cobertura/ se toca — lectura solamente)

Uso:  .venv/bin/python3 -B data/experiment/esq/code/seleccion_esq3b.py
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_esq3b as cc      # noqa: E402

SALIDA = cc.ORDEN_DIR / "seleccion_brazos_esq3b.json"

# Unidades nombradas del brazo objetivo, por número de ficha (pre-registro §2
# verbatim). R8 NO figura acá: se deriva.
OBJETIVO_POR_RETOQUE: dict[str, dict] = {
    "R1": {"principales": [26, 15], "papel": "tipo nuevo Potestad"},
    "R2": {"principales": [39], "papel": "tipo Condicion + predicado condicion_de"},
    "R3": {"principales": [25, 46], "contraste": [37],
           "papel": "tipo Definicion (f. 37 es la anti-atracción: sigue en Operacion)"},
    "R4": {"principales": [46, 19], "papel": "regla de omisión de meta-normativo"},
    "R5": {"principales": [63, 38], "papel": "partición sin tipo nuevo"},
    "R6a": {"principales": [44], "corroboran": [62, 65],
            "papel": "predicado exceptua_operacion"},
    "R7": {"principales": [32], "papel": "campo descripcion en Operacion"},
    "R9": {"principales": [67], "papel": "enum de Obligacion.tipo"},
}

REGLA_OBJETIVO = (
    "pre-registro ESQ-3b §2: unidades nombradas por número de ficha (R1–R7, R9) "
    "resueltas contra el worksheet de ESQ-2, más las unidades de R8 derivadas "
    "mecánicamente de las extracciones persistidas (tripletas aplica_a "
    "rechazadas con motivo firma_invalida)")
REGLA_REGRESION = (
    "pre-registro ESQ-3b §3 CORREGIDO por la Adenda 1 §2 (f1fe0d8): todas las "
    "fichas con q1=si_completo y q2=ninguna, más — hasta completar 35 "
    "unidades — fichas azarosas con q2=ninguna en orden por chunk_id y "
    "DESPUÉS fichas dirigidas con q2=ninguna en orden por chunk_id; excluidas "
    "las unidades del brazo objetivo")


def sha256_de(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for bloque in iter(lambda: f.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


def cargar_insumos():
    ws = json.loads(cc.WORKSHEET_ESQ2.read_text(encoding="utf-8"))
    sel = json.loads((cc.ORDEN_DIR / "seleccion_muestra_esq2.json"
                      ).read_text(encoding="utf-8"))
    regs = cc.cargar_extracciones_esq2()
    return ws, sel, regs


def derivar_r8(fichas_por_cid: dict[str, dict], regs: dict[str, dict]) -> dict:
    """R8, mecánico: unidades de las 75 fichas con al menos una tripleta
    `aplica_a` rechazada por `firma_invalida` en la validación persistida.
    Devuelve también el detalle transversal de TODOS los firma_invalida, para
    que el conteo del pre-registro sea auditable."""
    unidades: dict[str, int] = {}
    todos_firma_invalida: list[dict] = []
    otros_motivos_firma: list[dict] = []
    for cid in sorted(fichas_por_cid):
        rechazos = (regs[cid].get("validacion") or {}).get("rechazos") or []
        for r in rechazos:
            motivo = r.get("motivo")
            elem = r.get("elemento") or {}
            if motivo == "firma_invalida":
                todos_firma_invalida.append(
                    {"chunk_id": cid, "detalle": r.get("detalle"),
                     "predicate": elem.get("predicate")})
                if elem.get("predicate") == "aplica_a":
                    unidades[cid] = unidades.get(cid, 0) + 1
            elif motivo == "sujeto_extremo_invalido":
                otros_motivos_firma.append(
                    {"chunk_id": cid, "motivo": motivo, "detalle": r.get("detalle")})
    return {
        "unidades": unidades,
        "tripletas_aplica_a_firma_invalida": sum(unidades.values()),
        "tripletas_firma_invalida_todas": len(todos_firma_invalida),
        "tripletas_sujeto_extremo_invalido": len(otros_motivos_firma),
        "detalle_firma_invalida": todos_firma_invalida,
    }


def construir() -> dict:
    ws, sel, regs = cargar_insumos()
    fichas = ws["fichas"]
    por_n = {f["n"]: f for f in fichas}
    por_cid = {f["chunk_id"]: f for f in fichas}
    azarosas = set(sel["azarosa"])

    if len(fichas) != 75:
        raise RuntimeError(f"worksheet con {len(fichas)} fichas != 75")

    # ---------------- brazo objetivo ---------------- #
    retoques_por_cid: dict[str, list[str]] = {}

    def marcar(n: int, retoque: str, papel: str) -> str:
        cid = por_n[n]["chunk_id"]
        retoques_por_cid.setdefault(cid, []).append(f"{retoque}:{papel}")
        return cid

    for retoque, spec in OBJETIVO_POR_RETOQUE.items():
        for n in spec.get("principales", []):
            marcar(n, retoque, "principal")
        for n in spec.get("contraste", []):
            marcar(n, retoque, "contraste")
        for n in spec.get("corroboran", []):
            marcar(n, retoque, "corrobora")

    r8 = derivar_r8(por_cid, regs)
    for cid in sorted(r8["unidades"]):
        retoques_por_cid.setdefault(cid, []).append("R8:derivada")

    objetivo_cids = sorted(retoques_por_cid)

    # ---------------- brazo regresión ---------------- #
    def q1(cid: str) -> str:
        return por_cid[cid]["preguntas"]["q1_representado"]["marca"]

    def q2(cid: str) -> str:
        return por_cid[cid]["preguntas"]["q2_deformacion"]["firma"]

    excluidas = set(objetivo_cids)
    grupo1 = sorted(cid for cid in por_cid
                    if q1(cid) == "si_completo" and q2(cid) == "ninguna"
                    and cid not in excluidas)
    ya = set(grupo1)
    # Adenda 1 §2: primero azarosas, DESPUÉS dirigidas, ambas por chunk_id.
    pool_azarosas = sorted(cid for cid in por_cid
                           if cid in azarosas and q2(cid) == "ninguna"
                           and cid not in excluidas and cid not in ya)
    pool_dirigidas = sorted(cid for cid in por_cid
                            if cid not in azarosas and q2(cid) == "ninguna"
                            and cid not in excluidas and cid not in ya)
    completado_az = pool_azarosas[:max(0, 35 - len(grupo1))]
    completado_dir = pool_dirigidas[:max(0, 35 - len(grupo1) - len(completado_az))]
    regresion_cids = grupo1 + completado_az + completado_dir

    # Anomalía declarada si aun con la regla corregida el pool no alcanza 35.
    anomalias: list[str] = []
    if len(regresion_cids) < 35:
        n_obj_q2_ninguna = sum(1 for cid in objetivo_cids if q2(cid) == "ninguna")
        n_q2_ninguna = sum(1 for cid in por_cid if q2(cid) == "ninguna")
        anomalias.append(
            f"El brazo de regresión alcanza {len(regresion_cids)} unidades y no "
            f"las 35 nominales: agotado el pool de q2=ninguna fuera del brazo "
            f"objetivo (grupo q1=si_completo: {len(grupo1)}; azarosas: "
            f"{len(pool_azarosas)}; dirigidas: {len(pool_dirigidas)}). Es el "
            f"resultado ESPERADO por la Adenda 1 §2, que ya registró la fe de "
            f"erratas: las fichas con q2=ninguna son {n_q2_ninguna} sobre 75 y "
            f"{n_obj_q2_ninguna} están en el brazo objetivo, de modo que el "
            f"techo alcanzable es {n_q2_ninguna - n_obj_q2_ninguna}. No es un "
            f"desvío nuevo: la métrica, la predicción y la regla de falla del "
            f"§3 no cambian.")

    def fila(cid: str) -> dict:
        f = por_cid[cid]
        return {"n_ficha": f["n"], "chunk_id": cid, "to": f["to"],
                "unidad": f["unidad"], "tipo_unidad": f["tipo_unidad"],
                "q1_esq2": q1(cid), "q2_esq2": q2(cid),
                "origen_muestra_esq2": "azarosa" if cid in azarosas else "dirigida"}

    doc = {
        "unidad": "U-ESQ-3b",
        "laudo": "data/experiment/esq/laudo_ESQ-3a_retoques.md (0a76549)",
        "prerregistro": "data/experiment/esq/prerregistro_esq3b.md (01bf046)",
        "determinismo": ("archivo sin timestamp: función pura del worksheet, la "
                         "selección de muestra de ESQ-2 y las extracciones "
                         "persistidas (sha256 abajo)"),
        "insumos_sha256": {
            "cobertura/fichas/worksheet_fichas_esq2.json": sha256_de(cc.WORKSHEET_ESQ2),
            "cobertura/orden/seleccion_muestra_esq2.json": sha256_de(
                cc.ORDEN_DIR / "seleccion_muestra_esq2.json"),
            **{f"cobertura/{to}/extracciones_e1_{to}.jsonl": sha256_de(
                cc.COBERTURA_DIR / to / f"extracciones_e1_{to}.jsonl")
               for to in cc.TOS_ESQ2},
        },
        "regla_objetivo": REGLA_OBJETIVO,
        "regla_regresion": REGLA_REGRESION,
        "objetivo": {
            "n_unidades": len(objetivo_cids),
            "mapa_ficha_retoque": {
                cid: sorted(retoques_por_cid[cid]) for cid in objetivo_cids},
            "alcance_veredicto_r6a": (
                "Adenda 1 §3 (f1fe0d8): las unidades marcadas 'R6a:corrobora' "
                "(f. 62 y f. 65) están en el brazo objetivo como CORROBORACIÓN "
                "SIN predicción sellada — van en fila aparte de la tabla de "
                "resultados y NO cuentan para el veredicto de R6a, que se "
                "adjudica SOLO sobre la unidad marcada 'R6a:principal' "
                "(f. 44). Igual criterio de lectura para 'R3:contraste' "
                "(f. 37), que es la anti-atracción sellada de R3 y sí tiene "
                "predicción propia en el §2."),
            "unidades": [fila(cid) for cid in objetivo_cids],
        },
        "r8_derivacion": {
            "regla": ("tripletas aplica_a rechazadas por firma_invalida en la "
                      "validación persistida de las 75 fichas"),
            "unidades": {cid: n for cid, n in sorted(r8["unidades"].items())},
            "tripletas_aplica_a_firma_invalida": r8["tripletas_aplica_a_firma_invalida"],
            "conteo_transversal_firma_invalida_75_fichas":
                r8["tripletas_firma_invalida_todas"],
            "conteo_transversal_sujeto_extremo_invalido_75_fichas":
                r8["tripletas_sujeto_extremo_invalido"],
            "detalle_firma_invalida": r8["detalle_firma_invalida"],
        },
        "regresion": {
            "n_unidades": len(regresion_cids),
            "n_objetivo_35": 35,
            "grupo1_si_completo_q2_ninguna": len(grupo1),
            "completado_azarosas_q2_ninguna": len(completado_az),
            "completado_dirigidas_q2_ninguna": len(completado_dir),
            "pool_azarosas_disponible": len(pool_azarosas),
            "pool_dirigidas_disponible": len(pool_dirigidas),
            "unidades": [fila(cid) for cid in regresion_cids],
        },
        "solapamiento_brazos": sorted(set(objetivo_cids) & set(regresion_cids)),
        "anomalias_declaradas": anomalias,
    }
    return doc


def main() -> int:
    doc = construir()
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    texto = json.dumps(doc, ensure_ascii=False, indent=1, sort_keys=False)
    SALIDA.write_text(texto, encoding="utf-8")
    sha = hashlib.sha256(texto.encode("utf-8")).hexdigest()
    print(f"[b] objetivo: {doc['objetivo']['n_unidades']} unidades")
    print(f"[b] regresión: {doc['regresion']['n_unidades']} unidades "
          f"(objetivo del pre-registro: 35)")
    print(f"[b] solapamiento entre brazos: {doc['solapamiento_brazos']} (esperado [])")
    print(f"[b] R8 derivada: {len(doc['r8_derivacion']['unidades'])} unidades, "
          f"{doc['r8_derivacion']['tripletas_aplica_a_firma_invalida']} tripletas "
          f"aplica_a firma_invalida")
    for a in doc["anomalias_declaradas"]:
        print(f"[b] ANOMALÍA DECLARADA: {a}")
    print(f"[b] persistido: {SALIDA.relative_to(cc.REPO_DIR)}  sha256={sha}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
