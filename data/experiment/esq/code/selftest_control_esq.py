"""
selftest_control_esq.py — SELFTEST OFFLINE del runner del control de
instrumento de ESQ-1 (USD 0, sin API; los jsonl de producción se LEEN y no se
tocan; todo lo que se escribe va a selftest_out/, gitignorado).

Cubre lo exigido por el mandato U-ESQ-1c.b y los bordes que hacen confiable
al instrumento:

  1. CONTEO POR BRAZO — fixtures sintéticos con la forma real de los
     registros: tipo/predicado propuestos en el crudo (con trampas cruzadas:
     un tipo_propuesto en relaciones no cuenta), strings vacíos como
     ausentes, contenedor no-lista tratado como ausente Y contado aparte,
     unidad con error como no-emite (decisión D-g), y los tres componentes
     del brazo B (firma_registrada / crudo_aplica_a / canal_abierto) con sus
     negativos.
  2. CÁLCULO DEL RECARGO (D7) — usage sintético con valores cerrados a mano:
     tarifa marginal, recargo global y pareado, delta de output, prefijo
     medido, y el re-presupuesto de la corrida de 762 unidades.
  3. FLAG ENCENDIDO EN LA REQUEST — sobre un chunk real: el system es el
     prefijo abierto (≠ cerrado), el tool schema declara tipo_propuesto y
     predicado_propuesto (y el cerrado NO), el hash es bca492bbf7c8 y el
     namespace es el particionado pbca492bbf7c8.
  4. SELECCIÓN — sobre el universo real: pools 74 (33/1/3/37) / 164 / C>0
     por TO; 40 únicas y disyuntas; estratos exactos; A⊆poolA, B⊆poolB∖A,
     C⊆poolC; determinismo; los 40 chunk_ids resuelven en E0 enm01; la
     guarda de orden persistido frena ante una selección distinta.
  5. CORRIDA STUB END-TO-END — el runner corre las 40 con cliente stub en
     selftest_out/: jsonl con las MISMAS claves que producción, reanudación
     idempotente (segunda corrida: 0 pendientes, ni una línea más), resumen
     con los conteos exactos de los enlatados y freno de gasto en cero.
  6. ANCLAS — tarifas transcriptas == runner_corpus.py:76-78 (sin
     importarlo); factores de §5.2 recomputados == sellados (r_marg
     0,00717677, t_out 995,51, prefijo 9.983, 1.769 líneas con usage);
     umbrales == los sellados en el pre-registro (P1).

Uso:  .venv/bin/python3 -B data/experiment/esq/code/selftest_control_esq.py
"""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_control_esq as cc             # noqa: E402
import runner_control_esq as rc            # noqa: E402
import comun_e1                            # noqa: E402
import prompt_e1                           # noqa: E402
import cliente_e1                          # noqa: E402

OUT = cc.SELFTEST_DIR / "control_stub"

_checks = []


def check(nombre, cond):
    _checks.append((nombre, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {nombre}")


# --------------------------------------------------------------------------- #
# Fixtures                                                                     #
# --------------------------------------------------------------------------- #
def reg(crudo_entities=None, crudo_relations=None, rechazos=(), error=None,
        crudo=...):
    """Registro sintético con la forma real de los jsonl de E1 (claves
    verificadas contra corpus_v2/salida/cap/extracciones_e1.jsonl)."""
    if crudo is ...:
        crudo = {"entities": crudo_entities if crudo_entities is not None else [],
                 "relations": crudo_relations if crudo_relations is not None else [],
                 "omisiones_no_prosa": []}
    return {"chunk_id": "fx::1.1", "unidad": "1.1", "tipo_unidad": "punto",
            "titulo": "t", "stop_reason": "tool_use", "error": error,
            "usage": {"input_tokens": 0, "output_tokens": 0,
                      "cache_write_tokens": 0, "cache_read_tokens": 0},
            "tool_input_crudo": crudo,
            "validacion": {"chunk_id": "fx::1.1", "entidades": [], "relaciones": [],
                           "omisiones_no_prosa": [], "rechazos": list(rechazos),
                           "advertencias": [], "metricas": {}}}


def main() -> int:
    print("== selftest_control_esq (offline, $0) ==\n")
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    # ---------------- 1. conteo por brazo: emite_propuesto ------------------ #
    print("· conteo por brazo — emite_propuesto")
    e_tipo = reg(crudo_entities=[{"local_id": "e1", "tipo_propuesto": "TablaParametros"}])
    e_pred = reg(crudo_relations=[{"predicado_propuesto": "fija_parametro"}])
    e_ambos = reg(crudo_entities=[{"local_id": "e1", "tipo_propuesto": "X"}],
                  crudo_relations=[{"predicado_propuesto": "y"}])
    e_nada = reg(crudo_entities=[{"local_id": "e1", "type": "Obligacion"}],
                 crudo_relations=[{"predicate": "aplica_a"}])
    check("tipo_propuesto en entidad → tipo=True, predicado=False",
          cc.emite_propuesto(e_tipo) == {"tipo": True, "predicado": False, "alguno": True})
    check("predicado_propuesto en relación → predicado=True, tipo=False",
          cc.emite_propuesto(e_pred) == {"tipo": False, "predicado": True, "alguno": True})
    check("ambos → alguno=True con ambos flags",
          cc.emite_propuesto(e_ambos) == {"tipo": True, "predicado": True, "alguno": True})
    check("sin propuestos → todo False", cc.emite_propuesto(e_nada)["alguno"] is False)

    e_cruzado = reg(crudo_entities=[{"local_id": "e1", "predicado_propuesto": "x"}],
                    crudo_relations=[{"tipo_propuesto": "Y"}])
    check("TRAMPA CRUZADA: tipo_propuesto en relaciones / predicado_propuesto "
          "en entidades NO cuentan", cc.emite_propuesto(e_cruzado)["alguno"] is False)
    e_vacio = reg(crudo_entities=[{"local_id": "e1", "tipo_propuesto": "   "}],
                  crudo_relations=[{"predicado_propuesto": ""}])
    check("strings vacíos/espacios se tratan como ausentes",
          cc.emite_propuesto(e_vacio)["alguno"] is False)

    e_nolista = reg(crudo={"entities": "[]", "relations": [
        {"predicado_propuesto": "x"}], "omisiones_no_prosa": []})
    check("contenedor no-lista: se trata como ausente (regla vigente) y se "
          "flaggea contenedor_no_lista",
          cc.emite_propuesto(e_nolista) == {"tipo": False, "predicado": True, "alguno": True}
          and cc.contenedor_no_lista(e_nolista) is True
          and cc.contenedor_no_lista(e_tipo) is False)

    # ---------------- 1b. conteo por brazo: brazo B ------------------------- #
    print("· conteo por brazo — reporta_relacion_b")
    b_firma = reg(rechazos=[{"nivel": "relacion", "motivo": "firma_invalida",
                             "detalle": "relations[0]: Operacion --aplica_a--> Sujeto"}])
    b_crudo = reg(crudo_entities=[{"local_id": "e1", "type": "Operacion"}],
                  crudo_relations=[{"predicate": "aplica_a", "source": "e1",
                                    "sujeto_id": "S1"}])
    b_canal = reg(crudo_entities=[{"local_id": "e2", "type": "Excepcion"}],
                  crudo_relations=[{"predicado_propuesto": "aplica_a_excepcion",
                                    "source": "e2"}])
    b_no = reg(crudo_entities=[{"local_id": "e1", "type": "Obligacion"}],
               crudo_relations=[{"predicate": "aplica_a", "source": "e1"}],
               rechazos=[{"nivel": "relacion", "motivo": "firma_invalida",
                          "detalle": "relations[0]: Restriccion --condiciona--> Operacion"}])
    b_tipo_prop = reg(crudo_entities=[{"local_id": "e1", "tipo_propuesto": "Operacion"}],
                      crudo_relations=[{"predicate": "aplica_a", "source": "e1"}])
    r1 = cc.reporta_relacion_b(b_firma)
    r2 = cc.reporta_relacion_b(b_crudo)
    r3 = cc.reporta_relacion_b(b_canal)
    check("componente firma_registrada dispara solo con las dos firmas del brazo B",
          r1 == {"firma_registrada": True, "crudo_aplica_a": False,
                 "canal_abierto": False, "reporta": True}
          and cc.reporta_relacion_b(b_no)["reporta"] is False)
    check("componente crudo_aplica_a: aplica_a con source Operacion/Excepcion",
          r2 == {"firma_registrada": False, "crudo_aplica_a": True,
                 "canal_abierto": False, "reporta": True})
    check("componente canal_abierto: predicado_propuesto con source Op/Exc",
          r3 == {"firma_registrada": False, "crudo_aplica_a": False,
                 "canal_abierto": True, "reporta": True})
    check("entidad con tipo_propuesto NO cuenta como Operacion (declarado)",
          cc.reporta_relacion_b(b_tipo_prop)["reporta"] is False)

    # ---------------- 1c. conteos_por_brazo con umbrales -------------------- #
    print("· conteos_por_brazo — agregado y decisión D-g")
    selecc = ([{"chunk_id": f"a{i}", "to": "cap", "brazo": "A"} for i in range(20)]
              + [{"chunk_id": f"b{i}", "to": "cap", "brazo": "B"} for i in range(10)]
              + [{"chunk_id": f"c{i}", "to": "cap", "brazo": "C"} for i in range(10)])
    regs = {}
    for i in range(20):   # 10 A emiten (5 tipo, 5 predicado), 10 no
        regs[f"a{i}"] = e_tipo if i < 5 else (e_pred if i < 10 else e_nada)
    for i in range(10):   # b0..b5 reportan; b6 con error (D-g); b7..b9 no
        regs[f"b{i}"] = b_firma if i < 7 else b_no
    regs["b6"] = reg(error="max_tokens_hit", rechazos=[
        {"nivel": "relacion", "motivo": "firma_invalida",
         "detalle": "relations[0]: Operacion --aplica_a--> Sujeto"}])
    for i in range(10):   # 1 C emite tipo, 1 emite predicado (sin umbral), resto nada
        regs[f"c{i}"] = e_tipo if i == 0 else (e_pred if i == 1 else e_nada)
    del regs["c9"]        # unidad sin registro (D-g)
    co = cc.conteos_por_brazo(selecc, regs)
    check("brazo A: 10/20 emiten (5 tipo + 5 predicado) → pasa el umbral ≥10",
          co["A"] == {"n": 20, "emiten_algun_propuesto": 10, "umbral": ">=10 de 20",
                      "pasa": True, "emiten_tipo": 5, "emiten_predicado": 5})
    check("brazo B: 6/10 reportan (b6 con error NO cuenta pese a su firma, D-g) "
          "→ no pasa el umbral ≥7",
          co["B"]["reportan_relacion"] == 6 and co["B"]["pasa"] is False
          and co["B"]["componentes"]["firma_registrada"] == 6)
    check("brazo C: 1/10 emite tipo → pasa el umbral ≤1; el predicado se "
          "reporta aparte sin umbral",
          co["C"]["emiten_tipo_propuesto"] == 1 and co["C"]["pasa"] is True
          and co["C"]["emiten_algun_propuesto_sin_umbral"] == 2)
    check("unidades con error o sin registro quedan listadas",
          co["con_error"] == ["b6", "c9"])
    regs["b8"] = b_firma  # 7mo reporta
    check("borde del umbral B: con 7/10 pasa",
          cc.conteos_por_brazo(selecc, regs)["B"]["pasa"] is True)

    # ---------------- 2. cálculo del recargo (D7) --------------------------- #
    print("· recargo medido (D7)")
    check("fórmula D2 a mano: in=1000 out=2000 cw=500 cr=10000 → USD 0,012625",
          abs(cc.costo_usd_desde_usage({"input_tokens": 1000, "output_tokens": 2000,
                                        "cache_write_tokens": 500,
                                        "cache_read_tokens": 10000}) - 0.012625) < 1e-12)
    agg_c = {"n": 40, "input_tokens": 48000, "output_tokens": 52000,
             "cache_write_tokens": 10500, "cache_read_tokens": 409500,
             "n_escrituras": 1}
    agg_p = {"n": 40, "input_tokens": 48000, "output_tokens": 40000,
             "cache_write_tokens": 0, "cache_read_tokens": 398400,
             "n_escrituras": 0}
    fact = {"r_marg": 0.00717677, "pref_tok": 9983}
    rec = cc.recargo_medido(agg_c, fact, agg_p)
    check("tarifa abierta medida: (48000×1 + 52000×5 + 409500×0,1)/40/1e6 = 0,00872375",
          abs(rec["r_open_medido_usd_u"] - 0.00872375) < 1e-12)
    check("recargo global = 0,00872375 − 0,00717677 = 0,00154698",
          abs(rec["recargo_global_usd_u"] - 0.00154698) < 1e-12)
    check("recargo pareado = 0,00872375 − 0,0071960 = 0,00152775",
          abs(rec["r_prod_mismas_40_usd_u"] - 0.0071960) < 1e-12
          and abs(rec["recargo_pareado_usd_u"] - 0.00152775) < 1e-12)
    check("delta de output pareado = 52000/40 − 40000/40 = 300 tok/u",
          abs(rec["delta_out_tok_u_pareado"] - 300.0) < 1e-9)
    check("prefijo abierto medido = 10500 tok (única escritura)",
          rec["pref_abierto_medido_tok"] == 10500)
    rp = cc.re_presupuesto_esq1(rec, rec["pref_abierto_medido_tok"])
    esperado = 762 * (0.00717677 + 0.00152775) + 2 * 10500 * 1.25 / 1e6
    check("re-presupuesto 762 u con recargo pareado = "
          f"{esperado:.8f} (762×0,00870452 + 2×0,0131250)",
          abs(rp["recargo_pareado"]["total_usd"] - esperado) < 1e-9
          and rp["pref_tok_usado"] == 10500)

    # ---------------- 3. flag encendido en la request ----------------------- #
    print("· flag encendido en la request")
    chunk_real = comun_e1.cargar_chunks(("cap",), e0_dir=comun_e1.E0_SALIDA_ENM01)[0]
    guardas = rc.verificar_canal_abierto(chunk_real)
    check("guardas del runner pasan sobre un chunk real",
          guardas["namespace_particionado"] and guardas["tool_schema_tipo_propuesto"]
          and guardas["tool_schema_predicado_propuesto"]
          and guardas["system_es_prefijo_abierto"])
    check("prefijo abierto bca492bbf7c8 y namespace pbca492bbf7c8",
          guardas["prefijo_hash_abierto"] == "bca492bbf7c8"
          and "pbca492bbf7c8" in guardas["namespace"])
    kw_off = prompt_e1.build_request_kwargs(chunk_real, model=cc.MODEL_E1)
    props_off = kw_off["tools"][0]["input_schema"]["properties"]
    check("CONTRASTE: la request con flag apagado NO trae los campos ni el "
          "prefijo abierto",
          "tipo_propuesto" not in props_off["entities"]["items"]["properties"]
          and "predicado_propuesto" not in props_off["relations"]["items"]["properties"]
          and kw_off["system"][0]["text"] != prompt_e1.prefijo_sistema(True)
          and cliente_e1.namespace_e1(False) != cliente_e1.namespace_e1(True))

    # ---------------- 4. selección ------------------------------------------ #
    print("· selección de las 40")
    universo = cc.cargar_universo()
    po = cc.pools(universo)
    check("pool A = 74 (cap 33, cla 1, ext 3, ric 37) — scoping §6.1",
          sum(len(v) for v in po["A"].values()) == 74
          and {t: len(v) for t, v in po["A"].items()}
          == {"cap": 33, "cla": 1, "ext": 3, "pro": 0, "ric": 37})
    check("pool B = 164 — scoping §6.2", len(po["B"]) == 164)
    check("pool C: las 5 TOs tienen ≥2 limpias (decisión D-c es ejecutable)",
          all(len(po["C"][t]) >= 2 for t in cc.TOS))

    sel = cc.seleccionar(universo)
    ids = [s["chunk_id"] for s in sel]
    a = [s for s in sel if s["brazo"] == "A"]
    b = [s for s in sel if s["brazo"] == "B"]
    c = [s for s in sel if s["brazo"] == "C"]
    check("40 unidades, todas distintas (brazos disyuntos, D-b)",
          len(sel) == 40 and len(set(ids)) == 40)
    check("estratos A: 10 cap + 8 ric + 2 de ext∪cla",
          len(a) == 20
          and sum(1 for s in a if s["to"] == "cap") == 10
          and sum(1 for s in a if s["to"] == "ric") == 8
          and sum(1 for s in a if s["to"] in ("ext", "cla")) == 2)
    check("estratos B: 10; estratos C: 2 por TO",
          len(b) == 10 and len(c) == 10
          and all(sum(1 for s in c if s["to"] == t) == 2 for t in cc.TOS))
    pool_a_all = {x for v in po["A"].values() for x in v}
    pool_c_all = {x for v in po["C"].values() for x in v}
    check("membresía: A⊆poolA, B⊆poolB∖A, C⊆poolC",
          all(s["chunk_id"] in pool_a_all for s in a)
          and all(s["chunk_id"] in set(po["B"]) - {x["chunk_id"] for x in a} for s in b)
          and all(s["chunk_id"] in pool_c_all for s in c))
    check("determinismo: dos selecciones dan la misma lista",
          cc.seleccionar(universo) == sel)
    por_id = rc.chunks_por_id()
    check("los 40 chunk_ids resuelven en E0 enm01",
          all(i in por_id for i in ids))

    orden_dir = OUT / "orden"
    rc.persistir_orden(sel, universo, orden_dir)
    ok_guarda = False
    try:
        sel_mut = [dict(s) for s in sel]
        sel_mut[0], sel_mut[1] = sel_mut[1], sel_mut[0]
        rc.persistir_orden(sel_mut, universo, orden_dir)
    except rc.Freno:
        ok_guarda = True
    check("guarda de orden: una selección distinta contra el archivo "
          "persistido frena en vez de pisar", ok_guarda)

    # ---------------- 5. corrida stub end-to-end ---------------------------- #
    print("· corrida stub end-to-end")
    a0, a1 = a[0]["chunk_id"], a[1]["chunk_id"]
    b0, c0 = b[0]["chunk_id"], c[0]["chunk_id"]
    enlatados = {
        a0: {"entities": [{"local_id": "e1", "tipo_propuesto": "TablaParametros",
                           "label": "x", "punto": "1.1"}],
             "relations": [], "omisiones_no_prosa": []},
        a1: {"entities": [], "relations": [{"predicado_propuesto": "fija_parametro"}],
             "omisiones_no_prosa": []},
        b0: {"entities": [{"local_id": "e1", "type": "Operacion"}],
             "relations": [{"predicate": "aplica_a", "source": "e1",
                            "sujeto_id": "S1"}], "omisiones_no_prosa": []},
        c0: {"entities": [{"local_id": "e1", "tipo_propuesto": "Zeta"}],
             "relations": [], "omisiones_no_prosa": []},
    }
    stub = rc.StubClienteControl(dict(enlatados))
    meta = rc.correr(stub, sel, OUT, cc.TOPE_PARCIAL_USD, stub=True)
    lineas = (OUT / rc.JSONL_CONTROL).read_text(encoding="utf-8").strip().split("\n")
    check("la corrida stub persiste 40 líneas sin freno",
          len(lineas) == 40 and meta["frenado"] is None and stub.llamadas == 40)
    check("las 40 requests que el runner ARMÓ llevan el flag encendido "
          "(tool schema con los dos campos y system == prefijo abierto)",
          len(stub.requests) == 40 and all(
              "tipo_propuesto" in k["tools"][0]["input_schema"]["properties"][
                  "entities"]["items"]["properties"]
              and "predicado_propuesto" in k["tools"][0]["input_schema"][
                  "properties"]["relations"]["items"]["properties"]
              and k["system"][0]["text"] == prompt_e1.prefijo_sistema(True)
              for k in stub.requests))
    claves_prod = ["chunk_id", "unidad", "tipo_unidad", "titulo", "stop_reason",
                   "error", "usage", "tool_input_crudo", "validacion"]
    check("cada línea tiene EXACTAMENTE las claves de producción "
          "(runner_corpus.fase_e1)",
          all(list(json.loads(x).keys()) == claves_prod for x in lineas))
    check("la validación persistida corre con canal_abierto=True (la entidad "
          "propuesta de a0 NO es rechazada por type_invalido)",
          not any(r["motivo"] in ("type_invalido",)
                  for x in lineas
                  for r in (json.loads(x)["validacion"] or {}).get("rechazos", [])
                  if json.loads(x)["chunk_id"] == a0))
    stub2 = rc.StubClienteControl(dict(enlatados))
    rc.correr(stub2, sel, OUT, cc.TOPE_PARCIAL_USD, stub=True)
    lineas2 = (OUT / rc.JSONL_CONTROL).read_text(encoding="utf-8").strip().split("\n")
    check("reanudación idempotente: segunda corrida no llama ni escribe nada",
          stub2.llamadas == 0 and len(lineas2) == 40)

    resumen = rc.resumen_control(sel, OUT, universo, stub.resumen(), meta, None)
    cb = resumen["conteos_por_brazo"]
    check("resumen stub: A=2/20 (1 tipo + 1 predicado), B=1/10 (crudo_aplica_a), "
          "C=1/10 tipo → C pasa, A y B no",
          cb["A"]["emiten_algun_propuesto"] == 2 and cb["A"]["pasa"] is False
          and cb["B"]["reportan_relacion"] == 1 and cb["B"]["pasa"] is False
          and cb["B"]["componentes"]["crudo_aplica_a"] == 1
          and cb["C"]["emiten_tipo_propuesto"] == 1 and cb["C"]["pasa"] is True)
    check("resumen stub: gasto cero y costo desde usage cero",
          resumen["costo_recomputado_desde_usage_usd"] == 0.0)
    check("resumen stub: contenedores no-lista vacío con enlatados bien formados",
          resumen["conteos_por_brazo"]["contenedores_no_lista"] == [])

    # ---------------- 6. anclas --------------------------------------------- #
    print("· anclas")
    txt_rc = (cc.EXP_DIR / "reextraccion_v2" / "corpus_v2"
              / "runner_corpus.py").read_text(encoding="utf-8")
    check("tarifas transcriptas == runner_corpus.py:76-78 (sin importarlo)",
          'MODEL_E1 = "claude-haiku-4-5"' in txt_rc
          and "precio_in_por_mtok=1.00, precio_out_por_mtok=5.00" in txt_rc
          and "precio_cache_write_por_mtok=1.25, precio_cache_read_por_mtok=0.10" in txt_rc
          and cc.MODEL_E1 == "claude-haiku-4-5"
          and (cc.P_E1["precio_in_por_mtok"], cc.P_E1["precio_out_por_mtok"],
               cc.P_E1["precio_cache_write_por_mtok"],
               cc.P_E1["precio_cache_read_por_mtok"]) == (1.00, 5.00, 1.25, 0.10))
    fac = cc.factores_produccion()
    check("factores §5.2 recomputados: 1.769 líneas con usage, r_marg 0,00717677, "
          "t_out 995,51, prefijo 9.983",
          fac["agg"]["n"] == 1769
          and abs(fac["r_marg"] - cc.R_MARG_SELLADO) < 1e-7
          and abs(fac["t_out"] - cc.T_OUT_SELLADO) < 0.01
          and fac["pref_tok"] == 9983)
    txt_pre = (cc.UNIDAD_DIR / "prerregistro_esq1.md").read_text(encoding="utf-8")
    check("umbrales == P1 del pre-registro (≥10 de 20, ≥7 de 10, ≤1 de 10)",
          "≥10 de 20" in txt_pre and "≥7 de 10" in txt_pre and "≤1 de 10" in txt_pre
          and (cc.UMBRAL_A, cc.UMBRAL_B, cc.UMBRAL_C) == (10, 7, 1))
    check("presupuesto 0,32 y tope parcial 0,50 (mandato; scoping §5.3)",
          (cc.PRESUPUESTO_USD, cc.TOPE_PARCIAL_USD) == (0.32, 0.50))
    check("los 5 jsonl de producción existen y solo se leyeron",
          len(cc.JSONL_PRODUCCION) == 5 and all(p.exists() for p in cc.JSONL_PRODUCCION))

    passed = sum(ok for _, ok in _checks)
    print(f"\n  {passed}/{len(_checks)} checks OK")
    print("  RESULTADO:", "PASS" if passed == len(_checks) else "FAIL")
    return 0 if passed == len(_checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
