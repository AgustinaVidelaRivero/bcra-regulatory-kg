"""
seleccion_esq3b_v2.py — FASE (b) de U-ESQ-3b-v2 ($0): derivación MECÁNICA de
las unidades de los dos brazos, y persistencia de la selección ANTES de
extraer.

Reglas selladas que este módulo implementa sin re-decidir (pre-registro v2
`40493c9`, §0 y §2):

BRAZO OBJETIVO (§2) — 15 unidades, derivadas del worksheet de la vuelta 1 y de
la tabla `0c19dc8`; cada grupo se deriva mecánicamente y el conjunto final se
asserta contra la lista sellada del §2:
  - las 3 FALLADAS: unidades del brazo de regresión de la vuelta 1 con
    q3_migracion = incorrecta en el worksheet adjudicado (a5bdbd4);
  - anclas R1: unidades 'R1:principal' de la selección v1;
  - anclas R3: unidades 'R3:principal' + 'R3:contraste' de la selección v1;
  - R2: unidad 'R2:principal' de la selección v1;
  - R4: cryl::1.2 (ya contada como ancla R3) + la unidad 'R8:derivada' de la
    vuelta 1 cuya extracción nueva quedó VACÍA (vaciamiento de contenido
    habilitante, tabla §2 fila R8 / §4);
  - RE: las 2 unidades de P12–P13 y las 3 portadoras de emisiones avaladas de
    P14 — las 5 se verifican contra el jsonl v1: cada una emitió
    requisito_de_estructura (con las multiplicidades de P14).

BRAZO REGRESIÓN FRESCA (§0) — 12 unidades de las 687 extraídas y NO fichadas
de ESQ-2: sorteo estratificado por TO (mínimo 1 por TO, proporcional al
resto), semilla sellada '20260903:regresion_fresca_v2', generador NUEVO por TO
sobre ids ordenados (patrón de ESQ-2: random.Random(semilla).sample), con
EXCLUSIÓN EXPLÍCITA (asertada) de las 75 unidades fichadas de ESQ-2 —y por lo
tanto de todo brazo previo— y de las 15 del objetivo de esta vuelta. Cuotas
por el patrón de ESQ-2 (disparadores_esq2.cuotas_azarosas, adaptado a mínimo
1): cuota = 12·n_to/N; base = max(1, floor(cuota)); ajuste por mayor (menor)
resto, empates por el orden sellado TOS_ESQ2.

Determinismo: la salida NO lleva timestamp ni nada dependiente del entorno —
es función pura de los insumos (worksheet v1, selección v1, jsonl v1,
worksheet ESQ-2, extracciones ESQ-2), cuyos sha256 viajan en el archivo. Dos
corridas producen bytes idénticos (lo verifica el selftest).

Salida: cobertura/orden/seleccion_brazos_esq3b_v2.json  (archivo NUEVO; nada
preexistente de cobertura/ ni de esq3b/ se toca — lectura solamente)

Uso:  .venv/bin/python3 -B data/experiment/esq/code/seleccion_esq3b_v2.py
"""

from __future__ import annotations

import hashlib
import json
import math
import random
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_esq3b_v2 as cc      # noqa: E402

SALIDA = cc.ORDEN_DIR / "seleccion_brazos_esq3b_v2.json"

SEMILLA_REGRESION_FRESCA = "20260903:regresion_fresca_v2"
N_REGRESION_FRESCA = 12
N_OBJETIVO = 15

# Lista SELLADA del §2 del pre-registro v2 (contra la que se asserta la
# derivación mecánica; la fuente de verdad de la membresía es la derivación).
OBJETIVO_SELLADO_POR_GRUPO = {
    "falladas_v1": ["actgar::1.3.1::intro", "prevmi::1.2", "actgar::2.11.3"],
    "anclas_R1": ["opefci::6.3", "ctacor::1.1"],
    "anclas_R3": ["adrei::1.3.1", "cryl::1.2", "traval::1.1.1.1"],
    "R2": ["lavdin::3.3.4.3"],
    "R4": ["cryl::1.2", "opefci::2.1"],   # cryl::1.2 ya contada en anclas R3
    "RE": ["ayccef::5.1.1", "traval::3.1", "adrei::2.1.2::intro",
           "adrei::4.1.1.4", "expaef::9.1"],
}

# Multiplicidades de P14 (emisiones avaladas que deben conservarse), del §3.
RE_EMISIONES_P14 = {"adrei::2.1.2::intro": 2, "adrei::4.1.1.4": 1,
                    "expaef::9.1": 2}

REGLA_OBJETIVO = (
    "pre-registro v2 §2: las 3 falladas de la vuelta 1 (q3=incorrecta en el "
    "worksheet adjudicado a5bdbd4, brazo de regresión) + anclas R1 y R3 "
    "(principales y contraste de la selección v1) + R2 principal + R4 "
    "(cryl::1.2 ya contada + la unidad R8:derivada con extracción nueva "
    "vacía) + RE (P12, P13 y las portadoras de emisiones avaladas de P14); "
    "cada grupo derivado mecánicamente y asertado contra la lista sellada")
REGLA_REGRESION = (
    "pre-registro v2 §0: 12 unidades de las 687 extraídas y NO fichadas de "
    "ESQ-2, sorteo estratificado por TO (mínimo 1, proporcional al resto: "
    "cuota=12·n/N, base=max(1,floor(cuota)), ajuste por mayor resto con "
    "empates por el orden sellado TOS_ESQ2), semilla "
    "'20260903:regresion_fresca_v2', generador nuevo por TO sobre ids "
    "ordenados (patrón ESQ-2); exclusión explícita de las 75 fichadas y de "
    "las 15 del objetivo, verificada por assert")


def sha256_de(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for bloque in iter(lambda: f.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


def cargar_insumos():
    ws_v1 = json.loads(cc.WORKSHEET_V1.read_text(encoding="utf-8"))
    sel_v1 = json.loads(cc.SELECCION_V1.read_text(encoding="utf-8"))
    jsonl_v1 = cc.cargar_jsonl_last_wins(cc.JSONL_V1)
    ws_esq2 = json.loads(c1_worksheet_path().read_text(encoding="utf-8"))
    regs_esq2 = cc.cargar_extracciones_esq2()
    return ws_v1, sel_v1, jsonl_v1, ws_esq2, regs_esq2


def c1_worksheet_path() -> Path:
    return cc.COBERTURA_DIR / "fichas" / "worksheet_fichas_esq2.json"


def _emisiones_re(reg: dict) -> int:
    ents = (reg.get("tool_input_crudo") or {}).get("entities") or []
    return sum(1 for e in ents if isinstance(e, dict)
               and e.get("type") == "Obligacion"
               and (e.get("properties") or {}).get("tipo")
               == "requisito_de_estructura")


def _extraccion_vacia(reg: dict) -> bool:
    ents = (reg.get("tool_input_crudo") or {}).get("entities") or []
    return sum(1 for e in ents if isinstance(e, dict)
               and e.get("type") != "TextoOrdenado") == 0


def derivar_objetivo(ws_v1: dict, sel_v1: dict, jsonl_v1: dict) -> dict:
    """Los 6 grupos del §2, cada uno con su derivación mecánica y su assert
    contra la lista sellada."""
    reg_v1 = {u["chunk_id"] for u in sel_v1["regresion"]["unidades"]}
    mapa_v1 = sel_v1["objetivo"]["mapa_ficha_retoque"]
    q3 = {f["chunk_id"]: f["preguntas"]["q3_migracion"]["marca"]
          for f in ws_v1["fichas"]}

    def con_marca(retoque_papel: str) -> list[str]:
        return sorted(cid for cid, marcas in mapa_v1.items()
                      if retoque_papel in marcas)

    grupos: dict[str, list[str]] = {}
    grupos["falladas_v1"] = sorted(c for c in reg_v1 if q3.get(c) == "incorrecta")
    grupos["anclas_R1"] = con_marca("R1:principal")
    grupos["anclas_R3"] = sorted(con_marca("R3:principal")
                                 + con_marca("R3:contraste"))
    grupos["R2"] = con_marca("R2:principal")
    # R4: cryl::1.2 (ya derivada como R3 principal, el §2 la cuenta una vez) +
    # la única unidad R8:derivada cuya extracción nueva v1 quedó vacía.
    r8_vacias = sorted(cid for cid in con_marca("R8:derivada")
                       if _extraccion_vacia(jsonl_v1[cid]))
    grupos["R4"] = sorted(set(con_marca("R4:principal")) & {"cryl::1.2"}
                          | set(r8_vacias))
    # RE: P12–P13 (unidades nombradas en las predicciones selladas) + P14
    # (portadoras de avaladas). Verificación mecánica: cada una emitió
    # requisito_de_estructura en el jsonl v1, con las multiplicidades de P14.
    grupos["RE"] = sorted(["ayccef::5.1.1", "traval::3.1"]
                          + sorted(RE_EMISIONES_P14))

    verificaciones = {}
    for g, esperado in OBJETIVO_SELLADO_POR_GRUPO.items():
        ok = sorted(grupos[g]) == sorted(set(esperado))
        verificaciones[g] = {"derivado": sorted(grupos[g]),
                             "sellado_§2": sorted(set(esperado)), "coincide": ok}
        if not ok:
            raise RuntimeError(f"grupo {g}: derivación mecánica "
                               f"{sorted(grupos[g])} != lista sellada del §2 "
                               f"{sorted(set(esperado))} — se frena")
    for cid, n_esp in RE_EMISIONES_P14.items():
        n = _emisiones_re(jsonl_v1[cid])
        if n != n_esp:
            raise RuntimeError(f"P14: {cid} tiene {n} emisiones de "
                               f"requisito_de_estructura en el jsonl v1 "
                               f"(esperadas {n_esp}) — se frena")
    for cid in ("ayccef::5.1.1", "traval::3.1"):
        if _emisiones_re(jsonl_v1[cid]) < 1:
            raise RuntimeError(f"P12/P13: {cid} sin emisión de "
                               f"requisito_de_estructura en el jsonl v1")

    todas = sorted(set(c for g in grupos.values() for c in g))
    if len(todas) != N_OBJETIVO:
        raise RuntimeError(f"objetivo con {len(todas)} unidades != {N_OBJETIVO}")
    return {"grupos": grupos, "verificaciones": verificaciones, "cids": todas}


def cuotas_estratificadas(n_por_to: dict[str, int],
                          total_muestra: int = N_REGRESION_FRESCA,
                          minimo: int = 1) -> dict[str, int]:
    """Patrón de disparadores_esq2.cuotas_azarosas con mínimo 1 (§0):
    cuota = total·n/N; base = max(min, floor(cuota)); ajuste por mayor (menor)
    resto, empates por el orden sellado TOS_ESQ2."""
    n_total = sum(n_por_to.values())
    cuota = {to: total_muestra * n_por_to[to] / n_total for to in cc.TOS_ESQ2}
    base = {to: max(minimo, math.floor(cuota[to])) for to in cc.TOS_ESQ2}
    resto = {to: cuota[to] - base[to] for to in cc.TOS_ESQ2}
    diff = total_muestra - sum(base.values())
    orden_mayor = sorted(cc.TOS_ESQ2, key=lambda t: (-resto[t], cc.TOS_ESQ2.index(t)))
    orden_menor = sorted(cc.TOS_ESQ2, key=lambda t: (resto[t], cc.TOS_ESQ2.index(t)))
    i = 0
    while diff > 0:
        base[orden_mayor[i % len(orden_mayor)]] += 1
        diff -= 1
        i += 1
    i = 0
    while diff < 0:
        t = orden_menor[i % len(orden_menor)]
        if base[t] > minimo:
            base[t] -= 1
            diff += 1
        i += 1
    return base


def derivar_regresion_fresca(ws_esq2: dict, regs_esq2: dict,
                             objetivo_cids: list[str]) -> dict:
    fichadas = {f["chunk_id"] for f in ws_esq2["fichas"]}
    if len(fichadas) != 75:
        raise RuntimeError(f"worksheet ESQ-2 con {len(fichadas)} fichas != 75")
    sin_error = sorted(cid for cid, r in regs_esq2.items()
                       if r.get("error") is None)
    pool = sorted(cid for cid in sin_error if cid not in fichadas)

    # Exclusiones explícitas del §0, verificadas por assert.
    assert not set(pool) & fichadas, "el pool contiene unidades fichadas"
    assert not set(pool) & set(objetivo_cids), \
        "el pool contiene unidades del brazo objetivo"
    assert set(objetivo_cids) <= fichadas, \
        "hay unidades del objetivo fuera de las 75 fichadas (inesperado)"
    if len(pool) != 687:
        raise RuntimeError(f"pool de no fichadas = {len(pool)} != 687 "
                           f"(extraídas sin error {len(sin_error)} − 75 "
                           f"fichadas) — se frena")

    to_de = {}
    for c in cc.cargar_chunks_esq2():
        to_de[c["id"]] = c["to"]
    ids_por_to = {to: sorted(cid for cid in pool if to_de[cid] == to)
                  for to in cc.TOS_ESQ2}
    cuotas = cuotas_estratificadas({to: len(ids_por_to[to])
                                    for to in cc.TOS_ESQ2})
    if sum(cuotas.values()) != N_REGRESION_FRESCA:
        raise RuntimeError(f"cuotas suman {sum(cuotas.values())} != "
                           f"{N_REGRESION_FRESCA}")
    elegidas: list[str] = []
    for to in cc.TOS_ESQ2:
        elegidas += sorted(random.Random(SEMILLA_REGRESION_FRESCA)
                           .sample(ids_por_to[to], cuotas[to]))
    assert len(elegidas) == N_REGRESION_FRESCA
    assert not set(elegidas) & fichadas and not set(elegidas) & set(objetivo_cids)
    return {"pool_n": len(pool), "cuotas": cuotas,
            "ids_por_to_n": {to: len(ids_por_to[to]) for to in cc.TOS_ESQ2},
            "cids": elegidas}


def construir() -> dict:
    ws_v1, sel_v1, jsonl_v1, ws_esq2, regs_esq2 = cargar_insumos()
    obj = derivar_objetivo(ws_v1, sel_v1, jsonl_v1)
    reg = derivar_regresion_fresca(ws_esq2, regs_esq2, obj["cids"])

    to_de, unidad_de, tipo_de = {}, {}, {}
    for c in cc.cargar_chunks_esq2():
        to_de[c["id"]] = c["to"]
        unidad_de[c["id"]] = c["unidad"]
        tipo_de[c["id"]] = c["tipo"]

    def fila(cid: str) -> dict:
        return {"chunk_id": cid, "to": to_de[cid], "unidad": unidad_de[cid],
                "tipo_unidad": tipo_de[cid]}

    grupos_por_cid: dict[str, list[str]] = {}
    for g, cids in obj["grupos"].items():
        for cid in cids:
            grupos_por_cid.setdefault(cid, []).append(g)

    doc = {
        "unidad": "U-ESQ-3b-v2",
        "prerregistro_v2": "data/experiment/esq/prerregistro_esq3b_v2.md (40493c9)",
        "prerregistro_v1": "data/experiment/esq/prerregistro_esq3b.md (01bf046 + f1fe0d8)",
        "tabla_vuelta_1": "data/experiment/esq/esq3b/tabla_resultados_esq3b.md (0c19dc8)",
        "determinismo": ("archivo sin timestamp: función pura del worksheet "
                         "v1, la selección v1, el jsonl v1, el worksheet de "
                         "ESQ-2 y las extracciones de ESQ-2 (sha256 abajo)"),
        "insumos_sha256": {
            "esq3b/fichas/worksheet_pareado_esq3b.json": sha256_de(cc.WORKSHEET_V1),
            "cobertura/orden/seleccion_brazos_esq3b.json": sha256_de(cc.SELECCION_V1),
            "esq3b/extracciones/pareado_esq3b.jsonl": sha256_de(cc.JSONL_V1),
            "cobertura/fichas/worksheet_fichas_esq2.json": sha256_de(c1_worksheet_path()),
            **{f"cobertura/{to}/extracciones_e1_{to}.jsonl": sha256_de(
                cc.COBERTURA_DIR / to / f"extracciones_e1_{to}.jsonl")
               for to in cc.TOS_ESQ2},
        },
        "regla_objetivo": REGLA_OBJETIVO,
        "regla_regresion_fresca": REGLA_REGRESION,
        "objetivo": {
            "n_unidades": len(obj["cids"]),
            "grupos_§2": {g: sorted(cids) for g, cids in obj["grupos"].items()},
            "mapa_unidad_grupos": {cid: sorted(grupos_por_cid[cid])
                                   for cid in obj["cids"]},
            "verificacion_derivacion_vs_lista_sellada": obj["verificaciones"],
            "brazo_base": ("extracción de la VUELTA 1 "
                           "(esq3b/extracciones/pareado_esq3b.jsonl, prefijo "
                           "f0a421fb9466)"),
            "unidades": [fila(cid) for cid in obj["cids"]],
        },
        "regresion_fresca": {
            "n_unidades": len(reg["cids"]),
            "semilla": SEMILLA_REGRESION_FRESCA,
            "pool": ("las 687 unidades extraídas sin error por ESQ-2 y NO "
                     "fichadas (762 − 75); sin marcas previas; sin cruce con "
                     "el desvío (a): ninguna proviene de fichas"),
            "pool_n": reg["pool_n"],
            "pool_por_to": reg["ids_por_to_n"],
            "cuotas_por_to": reg["cuotas"],
            "exclusiones_asertadas": (
                "75 fichadas de ESQ-2 (y por lo tanto todo brazo previo) + "
                "15 del brazo objetivo de esta vuelta; verificado por assert "
                "en la derivación"),
            "brazo_base": "extracción de ESQ-2 (cobertura/, sellos a7788c1)",
            "unidades": [fila(cid) for cid in reg["cids"]],
        },
        "solapamiento_brazos": sorted(set(obj["cids"]) & set(reg["cids"])),
        "anomalias_declaradas": [],
    }
    return doc


def main() -> int:
    doc = construir()
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    texto = json.dumps(doc, ensure_ascii=False, indent=1, sort_keys=False)
    SALIDA.write_text(texto, encoding="utf-8")
    sha = hashlib.sha256(texto.encode("utf-8")).hexdigest()
    print(f"[b] objetivo: {doc['objetivo']['n_unidades']} unidades")
    print(f"[b] regresión fresca: {doc['regresion_fresca']['n_unidades']} "
          f"unidades (pool {doc['regresion_fresca']['pool_n']})")
    print(f"[b] cuotas por TO: {doc['regresion_fresca']['cuotas_por_to']}")
    print(f"[b] solapamiento entre brazos: {doc['solapamiento_brazos']} "
          f"(esperado [])")
    print(f"[b] persistido: {SALIDA.relative_to(cc.REPO_DIR)}  sha256={sha}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
