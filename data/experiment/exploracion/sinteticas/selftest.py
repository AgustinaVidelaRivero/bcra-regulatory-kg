"""
selftest.py — Selftest OFFLINE integral de la fase A (T6). Sin red, sin API.

Secciones:
  1. SAMPLER   — misma semilla => output idéntico byte a byte (dos instancias
                 independientes); volumen y estructura; verificación
                 independiente del sub-estrato entrante de E-B contra la
                 adyacencia real.
  2. VALIDADOR — rechaza fixtures malas diseñadas para cada puerta (a, b, c,
                 d) y acepta un caso bien formado.
  3. MÉTRICA   — los 3 casos (visto+consultado / visto-sin-consultar /
                 no-visto) contra 3 trazas REALES de u6_exploracion con golds
                 fabricados a mano (fixtures/casos_metrica.json), y replay
                 determinístico verificado contra los outputs persistidos.
  4. RESOLUCIÓN— 5/5 anclas conocidas (fixtures/anclas_conocidas.json), con
                 esperados derivados de un censo independiente.
  5. GENERADOR — stub inyectable produce el par literal/anti-léxica desde
                 fixtures; extracción de tokens prohibidos no vacía y sin
                 stopwords; la métrica de solape distingue un caso alto de
                 uno bajo (ejemplos del reporte).

Uso:  python3 selftest.py        (exit 0 = todo PASS)
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))

from comun import KG_VIGENTE, Quemado, index_runtime, tokens_contenido  # noqa: E402
from generador import Generador, StubCliente, TokensProhibidos  # noqa: E402
from metrica import evaluar_traza  # noqa: E402
from resolucion import AnclaIndex  # noqa: E402
from sampler import Sampler  # noqa: E402
from validador import SOLAPE_UMBRAL, Validador  # noqa: E402

TRAZAS_DIR = (AQUI.parents[1] / "evaluacion" / "posthoc_run" / "traces"
              / "u6_exploracion" / "reensamblado_v3")

RESULTADOS = []


def check(nombre: str, cond: bool, detalle: str = ""):
    RESULTADOS.append((nombre, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {nombre}"
          + (f" — {detalle}" if detalle and not cond else ""))


# --------------------------------------------------------------------------- #
def test_sampler():
    print("\n== 1. SAMPLER: determinismo y estructura ==")
    r1 = Sampler(semilla="selftest-semilla").muestrear_todo(volumen=5)
    r2 = Sampler(semilla="selftest-semilla").muestrear_todo(volumen=5)
    check("misma semilla => output idéntico",
          json.dumps(r1, sort_keys=True, ensure_ascii=False)
          == json.dumps(r2, sort_keys=True, ensure_ascii=False))
    r3 = Sampler(semilla="selftest-otra").muestrear_todo(volumen=5)
    check("otra semilla => output distinto",
          json.dumps(r1, sort_keys=True) != json.dumps(r3, sort_keys=True))
    check("5 estratos presentes", set(r1["conteo_por_estrato"]) ==
          {"E-A", "E-B", "E-C", "E-D", "E-E"})
    for s in r1["samples"]:
        if not s["gold"]["anclas"]:
            check("todo sample tiene gold con anclas", False, s["sample_id"])
            break
    else:
        check("todo sample tiene gold con anclas", True)

    # E-B: verificación independiente del sub-estrato contra la adyacencia real
    smp = Sampler(semilla="selftest-semilla")
    full = smp.muestrear_todo(volumen=8)
    eb = [s for s in full["samples"] if s["estrato"] == "E-B"]
    ok_sub = True
    for s in eb:
        tramos = s["metadatos"]["pregunta_sobre"]["tramos"]
        tiene = any(not smp.g.existe_saliente(t["de"], t["a"]) for t in tramos)
        declara = any(t["solo_via_entrante"] for t in tramos)
        if tiene != declara or (s["sub_estrato"] == "entrante") != tiene:
            ok_sub = False
            break
    check("E-B: sub-estrato entrante coincide con la adyacencia real",
          ok_sub and any(s["sub_estrato"] == "entrante" for s in eb))

    # quemado: ningún sample aceptado porta anclas no aptas
    q = Quemado()
    ok_q = True
    for s in full["samples"]:
        anclas = [a for n in s["subgrafo"]["nodos"] for a in n["anclas"]]
        if not q.todas_aptas(anclas)[0]:
            ok_q = False
            break
    check("ningún sample aceptado toca territorio quemado", ok_q)


# --------------------------------------------------------------------------- #
def _mini_sample(anclas, nodos=None, sample_id="FX-001"):
    nodos = nodos or [{"id": "Nodo_fixture_x", "type": "Obligacion",
                       "label": "Fixture", "descripcion": "",
                       "properties_extra": {}, "anclas": anclas}]
    return {"sample_id": sample_id, "estrato": "E-E", "sub_estrato": None,
            "semilla": "fixture",
            "subgrafo": {"nodos": nodos, "aristas": []},
            "gold": {"anclas": [{**a, "source_doc": "fx", "location_ejemplo": "fx"}
                                for a in anclas]},
            "metadatos": {"pregunta_sobre": {},
                          "debug_ids_respuesta": [n["id"] for n in nodos],
                          "debug_ids_subgrafo": [n["id"] for n in nodos]}}


def test_validador(ancla_idx):
    print("\n== 2. VALIDADOR: fixtures malas por puerta ==")
    v = Validador(ancla_idx, Quemado())
    PREGUNTA_OK = ("¿Qué obligaciones de liquidación en el mercado de cambios "
                   "alcanzan a un exportador de servicios ante un cobro "
                   "anticipado desde el exterior?")

    # (a) gold que no resuelve: ancla inexistente
    mala_a = _mini_sample([{"to": "ext", "ancla": "99.99"}])
    r = v.validar(mala_a, PREGUNTA_OK)
    check("puerta a: descarta gold que no resuelve",
          r["veredicto"] == "descartado"
          and any(m.startswith("a_gold_no_resuelve") for m in r["motivos"])
          and any(m.startswith("a_ancla_sin_unidad") for m in r["motivos"]))

    # (b) deíctico / fuga de generación / sin pregunta
    buena_c = _mini_sample([{"to": "cap", "ancla": "2.2"}])  # cap 2.2 disponible
    r = v.validar(buena_c, "¿Qué establece el punto anterior sobre capitales?")
    check("puerta b: descarta deíctico ('el punto anterior')",
          r["veredicto"] == "descartado"
          and any("b_deictico" in m for m in r["motivos"]))
    r = v.validar(buena_c, "¿Qué regula el nodo Obligacion_encaje_x según el grafo?")
    check("puerta b: descarta fuga de generación (nodo/grafo/id técnico)",
          r["veredicto"] == "descartado"
          and any("b_fuga_generacion" in m for m in r["motivos"]))
    r = v.validar(buena_c, "Enumerá las obligaciones de encaje en pesos y su "
                           "alcance para bancos comerciales.")
    check("puerta b: descarta texto sin interrogación",
          r["veredicto"] == "descartado"
          and "b_sin_interrogacion" in r["motivos"])

    # (b) fuga de ancla — fixture propia (caso real: EE-002 de la calibración)
    fx_ancla = json.load(open(AQUI / "fixtures" / "fuga_ancla.json",
                              encoding="utf-8"))
    ok_rechaza = all(
        any("b_fuga_ancla" in m for m in v.puerta_b(c["pregunta"])["motivos"])
        for c in fx_ancla["rechaza"])
    ok_acepta = all(
        not any("b_fuga_ancla" in m for m in v.puerta_b(c["pregunta"])["motivos"])
        for c in fx_ancla["acepta"])
    check(f"puerta b: b_fuga_ancla dispara en {len(fx_ancla['rechaza'])}/"
          f"{len(fx_ancla['rechaza'])} casos (incl. EE-002 real)", ok_rechaza)
    check("puerta b: b_fuga_ancla NO dispara en preguntas sin ancla",
          ok_acepta)

    # (c) territorio quemado: unidad quemada entera y parcial-que-abarca
    mala_c1 = _mini_sample([{"to": "cap", "ancla": "1.1.3"}])   # 1.1 quemada entera
    r = v.validar(mala_c1, PREGUNTA_OK)
    check("puerta c: descarta descendiente de unidad quemada entera",
          r["veredicto"] == "descartado"
          and any("unidad_quemada_entera" in m for m in r["motivos"]))
    mala_c2 = _mini_sample([{"to": "cap", "ancla": "1.4"}])     # parcial: abarca
    r = v.validar(mala_c2, PREGUNTA_OK)
    check("puerta c: descarta ancla que abarca subpuntos quemados (parciales)",
          r["veredicto"] == "descartado"
          and any("abarca" in m for m in r["motivos"]))

    # (d) anti-léxica con solape alto vs baja
    prohibidos = {"liquidacion", "divisas", "exportacion", "mercado", "cambios"}
    anti_mala = ("¿Qué liquidación de divisas de exportación exige el mercado "
                 "de cambios?")
    anti_buena = ("¿Qué debe hacer una empresa que cobra ventas al exterior "
                  "con los fondos recibidos?")
    r_mala = v.puerta_d(anti_mala, prohibidos, {})
    r_buena = v.puerta_d(anti_buena, prohibidos, {})
    check(f"puerta d: descarta solape {r_mala['solape']['solape']:.2f} > "
          f"{SOLAPE_UMBRAL}", not r_mala["ok"])
    check(f"puerta d: acepta solape {r_buena['solape']['solape']:.2f} <= "
          f"{SOLAPE_UMBRAL}", r_buena["ok"])
    check("puerta d: gold declarado distinto => descarte",
          not v.puerta_d(anti_buena, prohibidos, {"anclas": [1]},
                         gold_declarado={"anclas": [2]})["ok"])

    # caso bien formado pasa a, b, c
    r = v.validar(buena_c, PREGUNTA_OK)
    check("caso bien formado: apto (puertas a+b+c)",
          r["veredicto"] == "apto", str(r["motivos"]))
    check("flags requiere_llm declarados",
          set(r["requiere_llm"]) >= {"a_unicidad_semantica_de_la_pregunta",
                                     "b_comprensibilidad_sin_contexto"})


# --------------------------------------------------------------------------- #
def test_metrica(idx_runtime):
    print("\n== 3. MÉTRICA: 3 casos contra trazas reales ==")
    fx = json.load(open(AQUI / "fixtures" / "casos_metrica.json",
                        encoding="utf-8"))
    for caso in fx["casos"]:
        rep = json.load(open(TRAZAS_DIR / caso["traza"], encoding="utf-8"))[0]
        ev = evaluar_traza(rep["trace"], caso["gold_ids"], idx_runtime,
                           verificar_replay=True)
        esperado = caso["esperado"]
        ok = all(ev[k] == esperado[k] for k in esperado)
        check(f"caso {caso['caso']} ({caso['traza']})", ok,
              f"esperado {esperado}, obtenido "
              f"{ {k: ev[k] for k in esperado} }")
        check(f"replay determinístico OK en {caso['traza']}", ev["replay_ok"],
              str(ev["replay_fallas"][:2]))


# --------------------------------------------------------------------------- #
def test_resolucion(ancla_idx):
    print("\n== 4. RESOLUCIÓN: 5 anclas conocidas ==")
    fx = json.load(open(AQUI / "fixtures" / "anclas_conocidas.json",
                        encoding="utf-8"))
    aciertos = 0
    for a in fx["anclas"]:
        ids = ancla_idx.resolver(a["to"], a["ancla"])
        if "esperado_exacto" in a:
            ok = ids == a["esperado_exacto"]
            det = f"esperado {a['esperado_exacto']}, obtenido {ids[:3]}"
        else:
            con = ancla_idx.resolver(a["to"], a["ancla"],
                                     incluir_contenedores=True)
            ok = (len(ids) == a["esperado_n_sin_contenedores"]
                  and len(con) == a["esperado_n_con_contenedores"]
                  and a["contenedor_excluido"] not in ids
                  and a["contenedor_excluido"] in con)
            det = f"sin={len(ids)} con={len(con)}"
        aciertos += ok
        check(f"{a['to']}:{a['ancla']}", ok, det)
    check("resolución 5/5", aciertos == 5)


# --------------------------------------------------------------------------- #
def test_generador():
    print("\n== 5. GENERADOR: stub inyectable + tokens prohibidos ==")
    smp = Sampler(semilla="selftest-semilla")
    full = smp.muestrear_todo(volumen=3)
    sample = full["samples"][0]
    tp = TokensProhibidos({"nodes": smp.g.nodes})
    prohibidos = tp.de_sample(sample)
    check("tokens prohibidos no vacíos", bool(prohibidos))
    check("tokens prohibidos incluyen el label del nodo respuesta",
          bool(prohibidos & tokens_contenido(
              smp.g.por_id[sample["metadatos"]["debug_ids_respuesta"][0]]
              .get("label") or "")))
    from comun import STOPWORDS_ES
    check("tokens prohibidos sin stopwords",
          not (prohibidos & STOPWORDS_ES))

    stub = StubCliente(fixtures={
        "PALABRAS PROHIBIDAS": '{"pregunta": "¿Qué requisitos rigen para el caso reformulado de la fixture?"}',
    }, respuesta_defecto='{"pregunta": "¿Qué establece la norma de la fixture literal?"}')
    gen = Generador(stub, tp)
    par = gen.generar_par(sample)
    check("stub: literal desde fixture por defecto",
          par["literal"].startswith("¿Qué establece"))
    check("stub: anti-léxica desde fixture de evolución",
          par["antilexica"].startswith("¿Qué requisitos"))
    check("stub: 2 llamadas registradas (generación + evolución)",
          len(stub.llamadas) == 2)
    check("prompt de evolución contiene los tokens prohibidos",
          all(t in stub.llamadas[1] for t in sorted(prohibidos)[:3]))
    check("prompt de generación no expone ids técnicos",
          sample["metadatos"]["debug_ids_respuesta"][0]
          not in stub.llamadas[0])


# --------------------------------------------------------------------------- #
def main():
    print(f"Selftest fase A — grafo: {KG_VIGENTE.name} (sha verificado al cargar)")
    ancla_idx = AnclaIndex.desde_path(KG_VIGENTE)
    idx_runtime = index_runtime(KG_VIGENTE)
    test_sampler()
    test_validador(ancla_idx)
    test_metrica(idx_runtime)
    test_resolucion(ancla_idx)
    test_generador()
    fallas = [n for n, ok in RESULTADOS if not ok]
    print(f"\n== RESULTADO: {len(RESULTADOS) - len(fallas)}/{len(RESULTADOS)} PASS ==")
    if fallas:
        print("FALLAS:", *fallas, sep="\n  - ")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
