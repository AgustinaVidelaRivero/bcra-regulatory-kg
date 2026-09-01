"""
disparadores_esq2.py — FASE (e) de U-ESQ-2 ($0): disparadores mecánicos y
selección de la muestra de lectura (pre-registro §3, 2240c9c).

Corre SOLO sobre la extracción completa persistida por la fase (d). Nada acá
adjudica: los disparadores SELECCIONAN unidades para lectura dirigida; la
lectura es de la autora.

DISPARADORES (operacionalización mecánica declarada; sobre tool_input_crudo).
La cuarentena D5 del rol NO dispara: ningún disparador mira sujeto_id,
sujeto_propuesto ni rechazos de validación por sujetos.

  d1_nominalizacion — entidad de tipo normativo (Operacion, Obligacion,
     Restriccion, Excepcion) cuyo label, normalizado (minúsculas, sin
     acentos), tiene primera palabra que (i) termina en sufijo deverbal
     {cion, sion, miento, mento, ncia, anza, aje} o (ii) pertenece a la
     lista cerrada {computo, uso, acceso, manejo, empleo, destino}.
     PROXY DECLARADO de la firma (b): sobre-inclusivo por diseño (captura
     labels legítimos como «Presentación…»); el exceso lo absorbe el ranking
     determinístico y la adjudicación de la autora — nunca se cuenta un
     disparo como hallazgo.
  d2_tipo_otra — entidad con properties.tipo == "otra" (normalizado
     strip/minúsculas).
  d3_sin_relaciones_semanticas — entidad normativa (mismos 4 tipos) cuyo
     local_id no aparece como source ni target de NINGUNA relación cruda con
     predicate != "establecida_en". aplica_a/ejecuta cuentan como semánticas
     tenga la relación sujeto_id o sujeto_propuesto (la cuarentena no
     dispara ni descuenta).
  d4_densidad_anomala — densidad = (entidades crudas excl. TextoOrdenado +
     relaciones crudas) / max(1, chars_propio) × 1000. Dispara si queda fuera
     de [mediana − 3·MADn, mediana + 3·MADn] sobre las 762 (MADn = 1,4826 ×
     mediana de desvíos absolutos; dos colas), o si la extracción es vacía
     (0 entidades no-TO) con chars_propio ≥ 400.

MUESTRA (75 = 38 azarosas + 37 dirigidas, disjuntas):
  - Azarosa (38), estratificada por TO proporcional a las unidades extraídas
    con mínimo 2. Redondeo determinístico declarado: cuota = 38·n_to/N;
    base = max(2, floor(cuota)); los faltantes (o sobrantes) se ajustan por
    mayor (menor) resto cuota−base, empates por el orden sellado de TOS_ESQ2.
    Sorteo: generador NUEVO por TO — random.Random(20260901).sample(ids
    ordenados del TO, k) — patrón de las unidades previas (EV2:
    ev2_adjudicacion/code/comun_adj.py, muestra_estrato).
  - Dirigida (37): candidatos = unidades sin error que disparan y NO están
    en la azarosa. Ranking por la REGLA CORREGIDA de la fe de erratas del
    pre-registro (data/experiment/esq/fe_erratas_prerregistro_esq2_ranking.md
    §4, sellada en 930f289; reemplaza el pasaje «Si los candidatos exceden
    37…» del §3): round-robin ANIDADO por disparador × TO — disparadores en
    el orden declarado d1→d2→d3→d4; dentro del turno de cada disparador, los
    TOs en ciclo por orden alfabético de id; en cada par (disparador, TO) el
    candidato pendiente de menor chunk_id como desempate; pares agotados se
    saltean. Resto del §3 sin cambio: exclusión de unidades ya
    seleccionadas, déficit → se reasigna a la azarosa (sorteo extra
    declarado: generador nuevo random.Random(20260901) sobre el pool
    restante ordenado) y se declara en el reporte.
    [La regla original (round-robin por disparador, orden global por
    chunk_id) degeneró en 36/37 fichas en actgar — evidencia y causa en la
    fe de erratas §1-§2; corregida con 0 fichas leídas y azarosa intacta.]

Universo de muestreo: unidades con registro persistido sin error (una unidad
con error no tiene extracción que parear); el conteo se declara.

Salidas:
  cobertura/orden/disparadores_esq2.json   (conteos + detalle por unidad)
  cobertura/orden/seleccion_muestra_esq2.json  (regla, semilla, cuotas,
    listas azarosa/dirigida con su origen — el origen vive ACÁ, no en las
    fichas)

Uso:  .venv/bin/python3 -B data/experiment/esq/code/disparadores_esq2.py
"""

from __future__ import annotations

import json
import math
import random
import sys
import unicodedata
from datetime import datetime
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_cobertura_esq2 as cc      # noqa: E402

TIPOS_NORMATIVOS = ("Operacion", "Obligacion", "Restriccion", "Excepcion")
SUFIJOS_DEVERBALES = ("cion", "sion", "miento", "mento", "ncia", "anza", "aje")
LISTA_DEVERBAL = frozenset({"computo", "uso", "acceso", "manejo", "empleo",
                            "destino"})
N_AZAROSA = 38
N_DIRIGIDA = 37
DENSIDAD_VACIA_CHARS_MIN = 400

# Ciclo de TOs de la regla corregida (fe de erratas §4): orden alfabético de id.
TOS_ALFABETICO = tuple(sorted(cc.TOS_ESQ2))


def normalizar(s: str) -> str:
    s = unicodedata.normalize("NFD", s or "")
    s = "".join(ch for ch in s if unicodedata.category(ch) != "Mn")
    return s.lower().strip()


def ents_crudo(reg: dict) -> list:
    ents = (reg.get("tool_input_crudo") or {}).get("entities")
    return [e for e in ents if isinstance(e, dict)] if isinstance(ents, list) else []


def rels_crudo(reg: dict) -> list:
    rels = (reg.get("tool_input_crudo") or {}).get("relations")
    return [r for r in rels if isinstance(r, dict)] if isinstance(rels, list) else []


# ----------------------------- disparadores -------------------------------- #
def d1_nominalizacion(reg: dict) -> list[str]:
    hallados = []
    for e in ents_crudo(reg):
        if e.get("type") not in TIPOS_NORMATIVOS:
            continue
        label = normalizar(str(e.get("label") or ""))
        primera = label.split()[0] if label.split() else ""
        primera = primera.split("—")[0].split("-")[0].strip(":;,.")
        if primera and (primera in LISTA_DEVERBAL
                        or any(primera.endswith(suf) for suf in SUFIJOS_DEVERBALES)):
            hallados.append(f"{e.get('local_id')}:{e.get('label')}")
    return hallados


def d2_tipo_otra(reg: dict) -> list[str]:
    hallados = []
    for e in ents_crudo(reg):
        props = e.get("properties") or {}
        if isinstance(props, dict) and normalizar(str(props.get("tipo") or "")) == "otra":
            hallados.append(f"{e.get('local_id')}:{e.get('label')}")
    return hallados


def d3_sin_relaciones_semanticas(reg: dict) -> list[str]:
    con_semantica: set[str] = set()
    for r in rels_crudo(reg):
        if r.get("predicate") == "establecida_en":
            continue
        for extremo in (r.get("source"), r.get("target")):
            if isinstance(extremo, str):
                con_semantica.add(extremo)
    hallados = []
    for e in ents_crudo(reg):
        if e.get("type") in TIPOS_NORMATIVOS and e.get("local_id") not in con_semantica:
            hallados.append(f"{e.get('local_id')}:{e.get('label')}")
    return hallados


def densidad_de(reg: dict, chars_propio: int) -> float:
    n = (sum(1 for e in ents_crudo(reg) if e.get("type") != "TextoOrdenado")
         + len(rels_crudo(reg)))
    return n / max(1, chars_propio) * 1000


def banda_densidad(densidades: list[float]) -> tuple[float, float, float, float]:
    orden = sorted(densidades)
    n = len(orden)
    mediana = (orden[n // 2] if n % 2 else (orden[n // 2 - 1] + orden[n // 2]) / 2)
    desvios = sorted(abs(d - mediana) for d in densidades)
    mad = (desvios[n // 2] if n % 2 else (desvios[n // 2 - 1] + desvios[n // 2]) / 2)
    madn = 1.4826 * mad
    return mediana, madn, mediana - 3 * madn, mediana + 3 * madn


# ----------------------------- ranking dirigida ----------------------------- #
def ranking_dirigida_anidado(candidatos: dict[str, list[str]],
                             excluidas: set[str], n_objetivo: int,
                             tos: tuple[str, ...] = TOS_ALFABETICO) -> list[dict]:
    """Regla corregida VINCULANTE (fe de erratas del pre-registro §4, sellada
    en 930f289): round-robin anidado por disparador × TO.

    - Los disparadores se recorren en el orden de las claves de `candidatos`
      (el orden declarado d1→d4).
    - Dentro del turno de cada disparador, los TOs en ciclo por orden
      alfabético de id; cada disparador mantiene SU posición en el ciclo.
    - En cada par (disparador, TO) se toma el candidato PENDIENTE de menor
      chunk_id (desempate); pendiente = no seleccionado aún (por ningún
      disparador) ni excluido (azarosa).
    - Pares agotados se saltean; un disparador sin pendientes en ningún TO
      cede su turno completo.

    Determinística y pura: mismas listas → misma selección. El TO de un
    chunk_id es su prefijo antes de '::'."""
    por_par = {d: {to: sorted(c for c in lst if c.split("::")[0] == to)
                   for to in tos}
               for d, lst in candidatos.items()}
    pos_to = {d: 0 for d in candidatos}
    elegidos: list[dict] = []
    tomados: set[str] = set(excluidas)
    orden_d = list(candidatos.keys())
    while len(elegidos) < n_objetivo:
        avanzo = False
        for d in orden_d:
            if len(elegidos) >= n_objetivo:
                break
            for intento in range(len(tos)):
                to = tos[(pos_to[d] + intento) % len(tos)]
                lst = por_par[d][to]
                while lst and lst[0] in tomados:
                    lst.pop(0)
                if lst:
                    cid = lst.pop(0)
                    elegidos.append({"chunk_id": cid, "to": to,
                                     "disparador_ranking": d})
                    tomados.add(cid)
                    pos_to[d] = (pos_to[d] + intento + 1) % len(tos)
                    avanzo = True
                    break
        if not avanzo:
            break
    return elegidos


# ----------------------------- muestra -------------------------------------- #
def cuotas_azarosas(n_por_to: dict[str, int], total_muestra: int = N_AZAROSA) -> dict[str, int]:
    n_total = sum(n_por_to.values())
    cuota = {to: total_muestra * n_por_to[to] / n_total for to in cc.TOS_ESQ2}
    base = {to: max(2, math.floor(cuota[to])) for to in cc.TOS_ESQ2}
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
        if base[t] > 2:
            base[t] -= 1
            diff += 1
        i += 1
    return base


def main() -> int:
    # --- extracción completa persistida ---
    regs: dict[str, dict] = {}
    chars_propio: dict[str, int] = {}
    to_de: dict[str, str] = {}
    for to in cc.TOS_ESQ2:
        jsonl = cc.COBERTURA_DIR / to / f"extracciones_e1_{to}.jsonl"
        regs.update(cc.cargar_jsonl_last_wins(jsonl))
    for c in cc.cargar_chunks_esq2():
        chars_propio[c["id"]] = c.get("chars_propio") or len(c.get("texto") or "")
        to_de[c["id"]] = c["to"]
    faltantes = [cid for cid in chars_propio if cid not in regs]
    if faltantes:
        raise RuntimeError(f"fase (e) requiere la extracción completa: faltan "
                           f"{len(faltantes)} unidades (p.ej. {faltantes[:3]})")

    universo = sorted(cid for cid, r in regs.items() if r.get("error") is None)
    con_error = sorted(cid for cid, r in regs.items() if r.get("error") is not None)

    # --- disparadores sobre TODAS las unidades sin error ---
    densidades = {cid: densidad_de(regs[cid], chars_propio[cid]) for cid in universo}
    mediana, madn, lo, hi = banda_densidad(list(densidades.values()))
    detalle: dict[str, dict] = {}
    candidatos = {"d1_nominalizacion": [], "d2_tipo_otra": [],
                  "d3_sin_relaciones_semanticas": [], "d4_densidad_anomala": []}
    for cid in universo:
        reg = regs[cid]
        d1 = d1_nominalizacion(reg)
        d2 = d2_tipo_otra(reg)
        d3 = d3_sin_relaciones_semanticas(reg)
        dens = densidades[cid]
        vacia = (sum(1 for e in ents_crudo(reg) if e.get("type") != "TextoOrdenado") == 0
                 and chars_propio[cid] >= DENSIDAD_VACIA_CHARS_MIN)
        d4 = (dens < lo or dens > hi or vacia)
        detalle[cid] = {"d1": d1, "d2": d2, "d3": d3,
                        "d4": {"densidad_x1000chars": round(dens, 4),
                               "fuera_de_banda": dens < lo or dens > hi,
                               "extraccion_vacia_texto_sustantivo": vacia,
                               "dispara": d4}}
        if d1:
            candidatos["d1_nominalizacion"].append(cid)
        if d2:
            candidatos["d2_tipo_otra"].append(cid)
        if d3:
            candidatos["d3_sin_relaciones_semanticas"].append(cid)
        if d4:
            candidatos["d4_densidad_anomala"].append(cid)
    for k in candidatos:
        candidatos[k].sort()

    # --- azarosa: 38 estratificadas, generador nuevo por TO ---
    ids_por_to = {to: sorted(cid for cid in universo if to_de[cid] == to)
                  for to in cc.TOS_ESQ2}
    cuotas = cuotas_azarosas({to: len(ids_por_to[to]) for to in cc.TOS_ESQ2})
    azarosa: list[str] = []
    for to in cc.TOS_ESQ2:
        azarosa += sorted(random.Random(cc.SEMILLA_MUESTRA)
                          .sample(ids_por_to[to], cuotas[to]))
    set_azarosa = set(azarosa)

    # --- guarda de la fe de erratas: la azarosa NO se regenera ---
    # Si existe una selección persistida, la azarosa recomputada debe ser
    # IDÉNTICA a la persistida (mismo sorteo, semilla 20260901); si difiere,
    # se aborta sin escribir nada.
    sel_path = cc.ORDEN_DIR / "seleccion_muestra_esq2.json"
    if sel_path.exists():
        previa = json.loads(sel_path.read_text(encoding="utf-8"))
        if previa.get("azarosa") != azarosa:
            raise RuntimeError(
                "la azarosa recomputada difiere de la persistida — la fe de "
                "erratas exige azarosa intacta; no se escribe nada")
        print("[e] guarda fe de erratas: azarosa recomputada == persistida "
              f"({len(azarosa)} unidades)")

    # --- dirigida: 37 por round-robin ANIDADO disparador × TO ---
    # (regla corregida, fe de erratas §4 sellada en 930f289)
    elegidos_dir = ranking_dirigida_anidado(candidatos, set_azarosa, N_DIRIGIDA)
    dirigida = [{"chunk_id": e["chunk_id"], "to": e["to"],
                 "disparador_ranking": e["disparador_ranking"]}
                for e in elegidos_dir]
    elegidos: set[str] = {e["chunk_id"] for e in elegidos_dir}
    deficit = N_DIRIGIDA - len(dirigida)
    reasignadas: list[str] = []
    if deficit > 0:
        pool = sorted(set(universo) - set_azarosa - elegidos)
        reasignadas = sorted(random.Random(cc.SEMILLA_MUESTRA).sample(pool, deficit))
        azarosa += reasignadas
        set_azarosa |= set(reasignadas)

    # --- persistencia ---
    cc.ORDEN_DIR.mkdir(parents=True, exist_ok=True)
    (cc.ORDEN_DIR / "disparadores_esq2.json").write_text(json.dumps({
        "generado": datetime.now().isoformat(timespec="seconds"),
        "regla": "docstring de disparadores_esq2.py (operacionalización "
                 "mecánica declarada de pre-registro §3; la cuarentena D5 "
                 "del rol no dispara: ningún disparador mira sujetos)",
        "universo_sin_error": len(universo),
        "unidades_con_error_excluidas": con_error,
        "banda_densidad": {"mediana_x1000chars": round(mediana, 4),
                           "madn": round(madn, 4),
                           "banda": [round(lo, 4), round(hi, 4)],
                           "regla_vacia": f"0 entidades no-TO con chars_propio >= {DENSIDAD_VACIA_CHARS_MIN}"},
        "conteo_candidatos_por_disparador": {k: len(v) for k, v in candidatos.items()},
        "candidatos_por_disparador": candidatos,
        "detalle_por_unidad": detalle,
    }, ensure_ascii=False, indent=1), encoding="utf-8")

    (cc.ORDEN_DIR / "seleccion_muestra_esq2.json").write_text(json.dumps({
        "generado": datetime.now().isoformat(timespec="seconds"),
        "semilla": cc.SEMILLA_MUESTRA,
        "regla_azarosa": ("38 estratificadas por TO, proporcional a unidades "
                          "sin error con mínimo 2; cuota=38·n/N, base=max(2,"
                          "floor(cuota)), ajuste por mayor resto (empates por "
                          "orden sellado TOS_ESQ2); generador NUEVO por TO: "
                          "random.Random(20260901).sample(ids ordenados, k) — "
                          "patrón EV2 comun_adj.muestra_estrato"),
        "regla_dirigida": ("REGLA CORREGIDA (fe de erratas del pre-registro "
                           "§4, 930f289): 37 por round-robin ANIDADO "
                           "disparador × TO — disparadores d1→d2→d3→d4; "
                           "dentro del turno de cada disparador, TOs en "
                           "ciclo alfabético; en cada par (disparador, TO) "
                           "el candidato pendiente de menor chunk_id; pares "
                           "agotados se saltean; sin repetidos ni unidades "
                           "de la azarosa; déficit reasignado a la azarosa "
                           "con generador nuevo sobre el pool restante "
                           "ordenado"),
        "fe_erratas": "data/experiment/esq/fe_erratas_prerregistro_esq2_ranking.md (930f289)",
        "cuotas_azarosas": cuotas,
        "n_azarosa": len(azarosa),
        "n_dirigida": len(dirigida),
        "deficit_dirigida_reasignado": deficit if deficit > 0 else 0,
        "reasignadas_a_azarosa": reasignadas,
        "azarosa": azarosa,
        "dirigida": dirigida,
    }, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"[e] universo sin error: {len(universo)}/762 "
          f"(con error: {len(con_error)})")
    print(f"[e] candidatos por disparador: "
          f"{ {k: len(v) for k, v in candidatos.items()} }")
    print(f"[e] banda densidad: mediana={mediana:.3f} madn={madn:.3f} "
          f"banda=[{lo:.3f}, {hi:.3f}]")
    print(f"[e] cuotas azarosas: {cuotas}")
    print(f"[e] azarosa={len(azarosa)} dirigida={len(dirigida)} "
          f"déficit_reasignado={max(0, deficit)}")
    solap = set_azarosa & {d['chunk_id'] for d in dirigida}
    print(f"[e] solapamiento azarosa∩dirigida: {len(solap)} (esperado 0)")
    print("[PASS] fase (e): disparadores y selección persistidos en orden/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
