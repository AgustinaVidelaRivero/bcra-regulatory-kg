"""
comun_control_esq.py — Paths, selección de las 40 unidades y funciones de
conteo del CONTROL DE INSTRUMENTO de ESQ-1 (tres brazos; scoping_esq1.md §6,
pre-registro P1, laudo 94bb7a7 D2). Código puro, offline: nada de este módulo
llama a ninguna API.

Diseño heredado, no re-decidido acá:
  - Brazo A (20 u): unidades con `omisiones_no_prosa` en `validacion` (la
    lista ya viene filtrada a strings con texto por validador_e1.py:128, que
    implementa la regla «se descartan las omisiones sin texto» declarada en
    docs/fe_erratas_D10_causa_regimen_informativo.md → pool de 74).
    Estratificación del scoping §6.1: 10 cap, 8 ric, 2 de ext∪cla.
    Umbral sellado: ≥10 de 20 emiten algún propuesto.
  - Brazo B (10 u): unidades con `firma_invalida` registrada para
    `Operacion --aplica_a--> Sujeto` o `Excepcion --aplica_a--> Sujeto`
    (scoping §6.2, pool de 164). Umbral: ≥7 de 10 vuelven a reportar la
    relación (canal abierto o firma_invalida registrada).
  - Brazo C (10 u): unidades limpias en modo cerrado (scoping §6.3: sin
    rechazos, sin sujeto_propuesto, sin omisiones_no_prosa). Umbral sellado:
    ≤1 de 10 emite un tipo propuesto.
  - La medición de «propuestos» se hace sobre `tool_input_crudo`, no sobre
    `validacion` (fe de erratas `docs/fe_erratas_prerregistro_esq1_alcance.md`
    (b), commit 7072626).

Decisiones operativas de ESTA unidad (U-ESQ-1c), declaradas porque el scoping
las dejó abiertas; todas anteriores a la corrida:
  D-a. Semilla de selección: 20260827 — la misma sellada por el laudo para la
       selección de documentos (prerregistro §1). Un único objeto Random
       consumido en orden fijo: A(cap) → A(ric) → A(ext∪cla) → B → C(cap) →
       C(cla) → C(ext) → C(pro) → C(ric). Pools ordenados por chunk_id.
  D-b. Brazos disyuntos: 40 unidades distintas. El pool B excluye las ya
       elegidas para A (A∩B = 8 unidades en el universo; una unidad corrida
       dos veces sería la misma request → un solo dato).
  D-c. Brazo C estratificado 2 por TO (5 TOs × 2 = 10): el scoping no fija
       regla y el pool (1.363) está dominado por ext (749); 2×TO evita que el
       control negativo mire un solo documento.
  D-d. «Limpia» exige además extracción con sustancia: ≥1 entidad validada
       con type != TextoOrdenado (espejo de `extrajo_algo`,
       validador_e1.py:334) y registro sin `error`. Un chunk vacío pasaría el
       umbral negativo trivialmente y no probaría nada.
  D-e. «Sin sujeto_propuesto» se evalúa sobre el crudo (más estricto que el
       validado; coherente con 7072626).
  D-f. Universo de selección: los cinco jsonl de producción con dedup
       last-wins por chunk_id (semántica de reanudación de runner_corpus.py)
       → 1.763 unidades únicas (los archivos tienen 1.769 líneas; 6 son
       duplicados de reanudación). Los FACTORES de tarifa (§5.2 del scoping)
       se recomputan sobre las 1.769 líneas con usage, igual que el comando
       sellado del scoping, para reproducir sus números exactos.
  D-g. Una unidad del control cuyo registro quede con `error` (sin tool_use,
       max_tokens) cuenta en el denominador de su brazo como «no emite»; no
       se re-corre ni se reemplaza.

Tarifas: MODEL_E1 y P_E1 verbatim de
`data/experiment/reextraccion_v2/corpus_v2/runner_corpus.py:76-78`
(claude-haiku-4-5 — 1,00 / 5,00 / 1,25 / 0,10 USD/MTok). El selftest verifica
la transcripción contra ese archivo sin importarlo.
"""

from __future__ import annotations

import json
import random
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent          # data/experiment/esq/code
UNIDAD_DIR = CODE_DIR.parent                        # data/experiment/esq
EXP_DIR = UNIDAD_DIR.parent                         # data/experiment
REPO_DIR = EXP_DIR.parent.parent                    # raíz del repo

CONTROL_DIR = UNIDAD_DIR / "control"
ORDEN_DIR = CONTROL_DIR / "orden"
CACHE_DIR = UNIDAD_DIR / "cache"                    # gitignorada (.gitignore de esq/)
SELFTEST_DIR = UNIDAD_DIR / "selftest_out"          # gitignorada

E1_DIR = EXP_DIR / "reextraccion_v2" / "e1_extractor"
if str(E1_DIR) not in sys.path:
    sys.path.insert(0, str(E1_DIR))

JSONL_PRODUCCION = sorted(
    (EXP_DIR / "reextraccion_v2" / "corpus_v2" / "salida").glob(
        "*/extracciones_e1.jsonl"))

# Tarifa verbatim de runner_corpus.py:76-78 (corrida sellada del corpus).
MODEL_E1 = "claude-haiku-4-5"
P_E1 = dict(precio_in_por_mtok=1.00, precio_out_por_mtok=5.00,
            precio_cache_write_por_mtok=1.25, precio_cache_read_por_mtok=0.10)

SEMILLA = 20260827
TOS = ("cap", "cla", "ext", "pro", "ric")

# Umbrales sellados (prerregistro_esq1.md P1; scoping §6.1-6.3).
UMBRAL_A = 10   # de 20 — emiten algún propuesto (tipo o predicado)
UMBRAL_B = 7    # de 10 — vuelven a reportar la relación
UMBRAL_C = 1    # de 10 — a lo sumo 1 emite un tipo propuesto

N_A_POR_TO = {"cap": 10, "ric": 8}   # + 2 de ext∪cla (scoping §6.1)
N_A_EXTCLA = 2
N_B = 10
N_C_POR_TO = 2                        # decisión D-c

FIRMAS_B = ("Operacion --aplica_a--> Sujeto", "Excepcion --aplica_a--> Sujeto")

# Presupuesto y tope de la unidad (mandato U-ESQ-1c; scoping §5.3 «Control»).
PRESUPUESTO_USD = 0.32
TOPE_PARCIAL_USD = 0.50

# Namespace esperado del modo abierto. El hash cambió en U-ESQ-1d al
# corregirse la description del tool en modo abierto (adenda P1′, entrada
# 4.ii) y cambió de nuevo en U-ESQ-1e al neutralizarse los dos cierres del
# system en modo abierto (adenda P1″ §3). Los hashes de las corridas previas
# quedan registrados como constantes para leer su material persistido:
#   - control original (U-ESQ-1c, verificado en 8f52f3b): "bca492bbf7c8"
#   - re-corrida P1′ (U-ESQ-1d, sellada en c25273f):       "d923bf876580"
# El vigente es el de los cierres neutralizados.
PREFIJO_HASH_ABIERTO_ESPERADO = "48cb397b79c5"
PREFIJO_HASH_ABIERTO_P1BIS = "d923bf876580"
PREFIJO_HASH_ABIERTO_CONTROL_ORIGINAL = "bca492bbf7c8"

# Factores de producción sellados (scoping §5.2, recomputables con
# factores_produccion()). Solo referencia para cruces; el código recomputa.
R_MARG_SELLADO = 0.00717677
T_OUT_SELLADO = 995.51
T_CR_SELLADO = 9960.43
PREF_ABIERTO_SUPUESTO_TOK = 10383   # supuesto +400 del scoping §5.2.1


# --------------------------------------------------------------------------- #
# Universo y pools                                                             #
# --------------------------------------------------------------------------- #
def cargar_universo(paths=None) -> dict[str, dict]:
    """chunk_id → último registro persistido (last-wins, semántica de
    reanudación de runner_corpus.cargar_jsonl_last_wins). Solo lectura."""
    regs: dict[str, dict] = {}
    for p in (paths or JSONL_PRODUCCION):
        with open(p, encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea:
                    r = json.loads(linea)
                    regs[r["chunk_id"]] = r
    return regs


def to_de(chunk_id: str) -> str:
    return chunk_id.split("::", 1)[0]


def _omisiones(reg: dict) -> list:
    return (reg.get("validacion") or {}).get("omisiones_no_prosa") or []


def _rels_crudo(reg: dict) -> list:
    """Relaciones del crudo con la regla vigente de contenedores del
    instrumento (cadenas_esq): un contenedor que no es lista se trata como
    ausente; la pérdida se cuenta aparte (contenedor_no_lista)."""
    rels = (reg.get("tool_input_crudo") or {}).get("relations")
    return rels if isinstance(rels, list) else []


def _ents_crudo(reg: dict) -> list:
    ents = (reg.get("tool_input_crudo") or {}).get("entities")
    return ents if isinstance(ents, list) else []


def _str_con_texto(v) -> bool:
    return isinstance(v, str) and bool(v.strip())


def tiene_firma_b(reg: dict) -> bool:
    """Unidad con firma_invalida registrada para alguna de las dos firmas del
    brazo B (formato del detalle: validador_e1.py:286)."""
    for x in (reg.get("validacion") or {}).get("rechazos") or []:
        if (isinstance(x, dict) and x.get("motivo") == "firma_invalida"
                and any(f in (x.get("detalle") or "") for f in FIRMAS_B)):
            return True
    return False


def tiene_sujeto_propuesto_crudo(reg: dict) -> bool:
    return any(isinstance(r, dict) and _str_con_texto(r.get("sujeto_propuesto"))
               for r in _rels_crudo(reg))


def es_limpia(reg: dict) -> bool:
    """Brazo C (scoping §6.3 + decisiones D-d/D-e): sin error, sin rechazos,
    sin omisiones, sin sujeto_propuesto en el crudo, con ≥1 entidad validada
    de type != TextoOrdenado."""
    v = reg.get("validacion") or {}
    if reg.get("error") is not None:
        return False
    if v.get("rechazos"):
        return False
    if _omisiones(reg):
        return False
    if tiene_sujeto_propuesto_crudo(reg):
        return False
    return any(e.get("type") != "TextoOrdenado" for e in v.get("entidades") or [])


def pools(universo: dict[str, dict]) -> dict:
    a = {to: [] for to in TOS}
    b: list[str] = []
    c = {to: [] for to in TOS}
    for cid in sorted(universo):
        reg = universo[cid]
        to = to_de(cid)
        if to not in a:
            continue
        if _omisiones(reg):
            a[to].append(cid)
        if tiene_firma_b(reg):
            b.append(cid)
        if es_limpia(reg):
            c[to].append(cid)
    return {"A": a, "B": b, "C": c}


def seleccionar(universo: dict[str, dict]) -> list[dict]:
    """Las 40 unidades del control, deterministas (semilla 20260827, orden de
    consumo del Random declarado en la docstring del módulo). Devuelve
    [{chunk_id, to, brazo}] en el orden de corrida (A, B, C)."""
    po = pools(universo)
    rng = random.Random(SEMILLA)

    sel_a = []
    sel_a += rng.sample(po["A"]["cap"], N_A_POR_TO["cap"])
    sel_a += rng.sample(po["A"]["ric"], N_A_POR_TO["ric"])
    extcla = sorted(po["A"]["ext"] + po["A"]["cla"])
    sel_a += rng.sample(extcla, N_A_EXTCLA)

    pool_b = [cid for cid in po["B"] if cid not in set(sel_a)]   # decisión D-b
    sel_b = rng.sample(pool_b, N_B)

    sel_c = []
    for to in TOS:                                               # decisión D-c
        sel_c += rng.sample(po["C"][to], N_C_POR_TO)

    return ([{"chunk_id": cid, "to": to_de(cid), "brazo": "A"} for cid in sel_a]
            + [{"chunk_id": cid, "to": to_de(cid), "brazo": "B"} for cid in sel_b]
            + [{"chunk_id": cid, "to": to_de(cid), "brazo": "C"} for cid in sel_c])


# --------------------------------------------------------------------------- #
# Conteos por brazo (sobre los registros de la corrida del control)            #
# --------------------------------------------------------------------------- #
def emite_propuesto(reg: dict) -> dict:
    """Medición sobre el crudo (7072626): la unidad emite tipo_propuesto /
    predicado_propuesto con texto en tool_input_crudo."""
    tipo = any(isinstance(e, dict) and _str_con_texto(e.get("tipo_propuesto"))
               for e in _ents_crudo(reg))
    pred = any(isinstance(r, dict) and _str_con_texto(r.get("predicado_propuesto"))
               for r in _rels_crudo(reg))
    return {"tipo": tipo, "predicado": pred, "alguno": tipo or pred}


def contenedor_no_lista(reg: dict) -> bool:
    """Crudo presente pero con entities o relations que no son lista (cortes
    por max_tokens; decisión del 28/08: la pérdida se reporta, no se oculta)."""
    ti = reg.get("tool_input_crudo")
    if not isinstance(ti, dict):
        return False
    return not (isinstance(ti.get("entities"), list)
                and isinstance(ti.get("relations"), list))


def reporta_relacion_b(reg: dict) -> dict:
    """Brazo B: la unidad «vuelve a reportar la relación» (scoping §6.2: por
    el canal abierto, o como firma_invalida registrada). Operacionalización
    declarada, tres componentes; cuenta la unión:
      - firma_registrada: firma_invalida con alguna de las dos firmas en
        validacion.rechazos (misma detección que armó el pool).
      - crudo_aplica_a: relación cruda con predicate == "aplica_a" cuyo
        source resuelve a una entidad cruda de type Operacion/Excepcion (el
        mismo intento visto en el crudo, robusto a rechazos previos).
      - canal_abierto: relación cruda con predicado_propuesto con texto cuyo
        source resuelve a una entidad cruda de type Operacion/Excepcion (la
        relación re-expresada por el canal nuevo). Una entidad que a su vez
        use tipo_propuesto no cuenta como Operacion/Excepcion (no hay forma
        mecánica de saberlo; se declara)."""
    ents = {e.get("local_id"): e for e in _ents_crudo(reg) if isinstance(e, dict)}

    def _src_op_exc(r):
        e = ents.get(r.get("source"))
        return isinstance(e, dict) and e.get("type") in ("Operacion", "Excepcion")

    firma = tiene_firma_b(reg)
    crudo = any(isinstance(r, dict) and r.get("predicate") == "aplica_a"
                and _src_op_exc(r) for r in _rels_crudo(reg))
    canal = any(isinstance(r, dict) and _str_con_texto(r.get("predicado_propuesto"))
                and _src_op_exc(r) for r in _rels_crudo(reg))
    return {"firma_registrada": firma, "crudo_aplica_a": crudo,
            "canal_abierto": canal, "reporta": firma or crudo or canal}


def conteos_por_brazo(seleccion: list[dict], regs_control: dict[str, dict]) -> dict:
    """Conteos de los tres brazos contra sus umbrales sellados. Una unidad sin
    registro o con error cuenta como no-emite / no-reporta (decisión D-g)."""
    por_brazo = {"A": [], "B": [], "C": []}
    for s in seleccion:
        por_brazo[s["brazo"]].append(s["chunk_id"])

    detalle = {}
    for cid in [s["chunk_id"] for s in seleccion]:
        reg = regs_control.get(cid)
        if reg is None or reg.get("error") is not None:
            detalle[cid] = {"error": None if reg is None else reg.get("error"),
                            "sin_registro": reg is None,
                            "emite": {"tipo": False, "predicado": False, "alguno": False},
                            "brazo_b": {"firma_registrada": False, "crudo_aplica_a": False,
                                        "canal_abierto": False, "reporta": False},
                            "contenedor_no_lista": bool(reg) and contenedor_no_lista(reg)}
        else:
            detalle[cid] = {"error": None, "sin_registro": False,
                            "emite": emite_propuesto(reg),
                            "brazo_b": reporta_relacion_b(reg),
                            "contenedor_no_lista": contenedor_no_lista(reg)}

    n_a = sum(detalle[c]["emite"]["alguno"] for c in por_brazo["A"])
    n_b = sum(detalle[c]["brazo_b"]["reporta"] for c in por_brazo["B"])
    n_c_tipo = sum(detalle[c]["emite"]["tipo"] for c in por_brazo["C"])
    n_c_alguno = sum(detalle[c]["emite"]["alguno"] for c in por_brazo["C"])
    return {
        "A": {"n": len(por_brazo["A"]), "emiten_algun_propuesto": n_a,
              "umbral": f">={UMBRAL_A} de 20", "pasa": n_a >= UMBRAL_A,
              "emiten_tipo": sum(detalle[c]["emite"]["tipo"] for c in por_brazo["A"]),
              "emiten_predicado": sum(detalle[c]["emite"]["predicado"] for c in por_brazo["A"])},
        "B": {"n": len(por_brazo["B"]), "reportan_relacion": n_b,
              "umbral": f">={UMBRAL_B} de 10", "pasa": n_b >= UMBRAL_B,
              "componentes": {k: sum(detalle[c]["brazo_b"][k] for c in por_brazo["B"])
                              for k in ("firma_registrada", "crudo_aplica_a", "canal_abierto")}},
        "C": {"n": len(por_brazo["C"]), "emiten_tipo_propuesto": n_c_tipo,
              "umbral": f"<={UMBRAL_C} de 10 (tipo propuesto, redaccion sellada de P1)",
              "pasa": n_c_tipo <= UMBRAL_C,
              "emiten_algun_propuesto_sin_umbral": n_c_alguno},
        "contenedores_no_lista": sorted(c for c in detalle if detalle[c]["contenedor_no_lista"]),
        "con_error": sorted(c for c in detalle
                            if detalle[c]["error"] is not None or detalle[c]["sin_registro"]),
        "detalle_por_unidad": detalle,
    }


# --------------------------------------------------------------------------- #
# Tarifas y recargo (D7)                                                       #
# --------------------------------------------------------------------------- #
def costo_usd_desde_usage(agg: dict, p: dict = P_E1) -> float:
    """Fórmula D2 (docs/decisiones_caching_extraccion.md:32-42):
    in×P_in + out×P_out + cw×P_cw + cr×P_cr, tokens en MTok."""
    return (agg.get("input_tokens", 0) * p["precio_in_por_mtok"]
            + agg.get("output_tokens", 0) * p["precio_out_por_mtok"]
            + agg.get("cache_write_tokens", 0) * p["precio_cache_write_por_mtok"]
            + agg.get("cache_read_tokens", 0) * p["precio_cache_read_por_mtok"]) / 1e6


def agregar_usage(usages: list[dict]) -> dict:
    agg = {"n": 0, "input_tokens": 0, "output_tokens": 0,
           "cache_write_tokens": 0, "cache_read_tokens": 0, "n_escrituras": 0}
    for u in usages:
        if not u:
            continue
        agg["n"] += 1
        for k in ("input_tokens", "output_tokens",
                  "cache_write_tokens", "cache_read_tokens"):
            agg[k] += u.get(k, 0) or 0
        if (u.get("cache_write_tokens") or 0) > 0:
            agg["n_escrituras"] += 1
    return agg


def tarifa_marginal(agg: dict, p: dict = P_E1) -> float:
    """Tarifa marginal por unidad SIN cache_write (scoping §5.2: las
    escrituras de prefijo van como línea aparte, exactamente una vez)."""
    if not agg["n"]:
        return 0.0
    return (agg["input_tokens"] * p["precio_in_por_mtok"]
            + agg["output_tokens"] * p["precio_out_por_mtok"]
            + agg["cache_read_tokens"] * p["precio_cache_read_por_mtok"]) / agg["n"] / 1e6


def factores_produccion(paths=None) -> dict:
    """Recomputo de los factores de §5.2 del scoping sobre TODAS las líneas
    con usage de los cinco jsonl (1.769; mismo alcance que el comando sellado
    del scoping — decisión D-f)."""
    usages = []
    for p in (paths or JSONL_PRODUCCION):
        with open(p, encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea:
                    u = json.loads(linea).get("usage") or {}
                    if u:
                        usages.append(u)
    agg = agregar_usage(usages)
    n = agg["n"]
    return {"agg": agg,
            "t_in": agg["input_tokens"] / n,
            "t_out": agg["output_tokens"] / n,
            "t_cr": agg["cache_read_tokens"] / n,
            "pref_tok": (agg["cache_write_tokens"] // agg["n_escrituras"]
                         if agg["n_escrituras"] else 0),
            "r_marg": tarifa_marginal(agg)}


def usage_produccion_de(universo: dict[str, dict], chunk_ids: list[str]) -> dict:
    """Usage agregado de ESAS unidades en la corrida cerrada de producción
    (referencia pareada del recargo)."""
    return agregar_usage([(universo.get(c) or {}).get("usage") or {} for c in chunk_ids])


def recargo_medido(agg_control: dict, factores: dict, agg_prod_40: dict) -> dict:
    """El dato de D7: recargo del modo abierto, medido.

    Dos lecturas, ambas con su aritmética; ninguna se interpreta acá:
      - global: r_open_medido − r_marg (la letra de D7: «vs la tarifa marginal
        de producción»). Sesgo declarado: las 40 unidades del control se
        eligieron por patología (omisiones, firmas, limpieza), no al azar.
      - pareada: r_open_medido − r_prod_40, con r_prod_40 la tarifa marginal
        de LAS MISMAS 40 unidades en la corrida cerrada — aísla el efecto del
        modo del efecto de la selección de unidades."""
    r_open = tarifa_marginal(agg_control)
    r_prod_40 = tarifa_marginal(agg_prod_40)
    n = agg_control["n"] or 1
    n40 = agg_prod_40["n"] or 1
    return {
        "r_open_medido_usd_u": r_open,
        "r_marg_produccion_usd_u": factores["r_marg"],
        "r_prod_mismas_40_usd_u": r_prod_40,
        "recargo_global_usd_u": r_open - factores["r_marg"],
        "recargo_pareado_usd_u": r_open - r_prod_40,
        "out_tok_u_control": agg_control["output_tokens"] / n,
        "out_tok_u_prod_40": agg_prod_40["output_tokens"] / n40,
        "delta_out_tok_u_pareado": (agg_control["output_tokens"] / n
                                    - agg_prod_40["output_tokens"] / n40),
        "in_tok_u_control": agg_control["input_tokens"] / n,
        "in_tok_u_prod_40": agg_prod_40["input_tokens"] / n40,
        "cr_tok_u_control": agg_control["cache_read_tokens"] / n,
        "pref_abierto_medido_tok": (agg_control["cache_write_tokens"]
                                    // agg_control["n_escrituras"]
                                    if agg_control["n_escrituras"] else None),
        "pref_cerrado_medido_tok": factores["pref_tok"],
    }


def re_presupuesto_esq1(recargo: dict, pref_abierto_tok: int | None) -> dict:
    """Re-presupuesto de la corrida de ESQ-1 (762 unidades, scoping §5.3) con
    el recargo MEDIDO en lugar del supuesto de +10 % (D7). Se computa con las
    dos lecturas del recargo; la elección es de la autora."""
    pref = pref_abierto_tok or PREF_ABIERTO_SUPUESTO_TOK
    escritura = pref * P_E1["precio_cache_write_por_mtok"] / 1e6
    out = {}
    for k in ("recargo_global_usd_u", "recargo_pareado_usd_u"):
        r_u = recargo["r_marg_produccion_usd_u"] + recargo[k]
        out[k.replace("_usd_u", "")] = {
            "tarifa_usd_u": r_u,
            "corrida_762_usd": 762 * r_u,
            "escrituras_2_usd": 2 * escritura,
            "total_usd": 762 * r_u + 2 * escritura,
        }
    out["pref_tok_usado"] = pref
    out["formula"] = ("762 × (r_marg + recargo) + 2 × pref × 1,25/1e6 ; "
                      "r_marg recomputado de §5.2, tarifas runner_corpus.py:76-78")
    return out
