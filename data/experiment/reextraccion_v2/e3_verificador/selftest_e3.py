"""
selftest_e3.py — Selftest OFFLINE de E3 (T4). Cero llamadas a APIs de LLM:
los únicos clientes que se instancian son StubClienteE3 y StubClienteE1.

Verifica:
  A. Prefijo E3 estable e idéntico entre unidades (condición del caching):
     system + tools + tool_choice byte-idénticos en las 87 unidades aceptadas,
     breakpoint ephemeral en el último bloque, nada variable antes del
     breakpoint.
  B. CONTEXTO FRESCO verificable (principio 2.c): el request de E3 no
     contiene NADA del prompt del extractor — ni sus instrucciones, ni su
     tool, ni su system; el mensaje lleva solo fuente + extracción como datos.
  C. Determinismo: mismos datos → mismo request byte a byte.
  D. Calibradores: 4, resueltos, con citas que verifican contra su fuente
     (incluida la normalización de guiones de corte de línea del PDF) y el
     completo_ok igual a la extracción real de fase B.
  E. Capa determinística de citas: positivo con guiones, negativo con cita
     fabricada, insensible a espacios/saltos.
  F. Flujo del mini-ratchet con fixtures (stub): amputación detectada →
     reintento con prefijo E1 byte-idéntico y feedback después del breakpoint
     → re-validación → re-verificación → aceptado; completa pasa directo;
     tope 1 respetado → cola humana con flag y TODO persistidos; veredicto
     incoherente y cita fabricada manejados.
  G. Keys de caché local (llm_cache puro, sin DB) y namespace propio.
  H. Estimación reproducible.

Uso:  python3 selftest_e3.py
"""

from __future__ import annotations

import json
import shutil
import sys

import comun_e3
from comun_e3 import (BASE, cargar_chunks, cita_en_fuente, fuente_integro,
                      normalizar_para_cita, pares_calibracion, render_extraccion)
import prompt_e3
import cliente_e3
import ratchet_e3

import prompt_e1
import cliente_e1
import llm_cache as lc

OK, FAIL = 0, 0


def check(nombre: str, cond: bool, detalle: str = "") -> None:
    global OK, FAIL
    if cond:
        OK += 1
        print(f"  ok  {nombre}")
    else:
        FAIL += 1
        print(f" FAIL {nombre}  {detalle}")


def canon(obj) -> str:
    return json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def main() -> int:
    pares = pares_calibracion()
    chunks_pro = {c["id"]: c for c in cargar_chunks(("pro",))}
    print(f"pares (chunk aceptado, validación E1) cargados: {len(pares)}")

    # ---------------- A. Prefijo estable e idéntico entre unidades --------- #
    print("\n[A] prefijo estable")
    check("la calibración E3 son 87 unidades aceptadas (fan-in E2: 88 − 1)",
          len(pares) == 87, f"hay {len(pares)}")
    ref = None
    prefijo_identico = True
    texto_en_prefijo = False
    for chunk, val in pares:
        kw = prompt_e3.build_request_kwargs(chunk, val, model="MODELO_FASE_B")
        pref = canon({"system": kw["system"], "tools": kw["tools"],
                      "tool_choice": kw["tool_choice"]})
        if ref is None:
            ref = pref
        elif pref != ref:
            prefijo_identico = False
            break
        if chunk["texto"][:60] in pref and chunk["id"] not in (
                "ric::7.1", "pro::1.1.2.5", "cla::6.5.1.1"):  # los calibradores sí viven en el prefijo
            texto_en_prefijo = True
            break
    check("prefijo (system+tools+tool_choice) idéntico en las 87 unidades",
          prefijo_identico and ref is not None)
    check("nada del texto variable (fuera de calibradores) aparece en el prefijo",
          not texto_en_prefijo)

    ch0, val0 = pares[0]
    kw0 = prompt_e3.build_request_kwargs(ch0, val0, model="MODELO_FASE_B")
    sistema = kw0["system"]
    check("system es lista de bloques (jamás string plano)", isinstance(sistema, list))
    check("breakpoint cache_control ephemeral en el ÚLTIMO bloque del system",
          isinstance(sistema, list) and sistema
          and sistema[-1].get("cache_control") == {"type": "ephemeral"})
    check("un solo bloque de system (todo lo estable antes del breakpoint)",
          isinstance(sistema, list) and len(sistema) == 1)
    check("lo variable va en messages, después del breakpoint",
          ch0["texto"][:60] in kw0["messages"][0]["content"])
    check("tool_choice fuerza la tool del verificador",
          kw0["tool_choice"] == {"type": "tool", "name": prompt_e3.NOMBRE_TOOL})

    # ---------------- B. Contexto fresco (principio 2.c) ------------------- #
    print("\n[B] contexto fresco: nada del extractor en el request de E3")
    req_canon = canon(kw0)
    centinelas_e1 = [
        "Sos un extractor de tripletas",          # apertura del system E1
        "REGLAS NO NEGOCIABLES",                  # sección del system E1
        "extraer_kg_e1",                          # tool del extractor
        "ANTI-FUSIÓN",                            # regla 5 del system E1
        "Puntos admitidos para `punto`",          # mensaje de usuario E1
    ]
    for c in centinelas_e1:
        check(f"centinela E1 ausente del request E3: «{c[:40]}»", c not in req_canon)
    msg = kw0["messages"][0]["content"]
    check("el mensaje E3 contiene el fuente íntegro de la unidad (datos)",
          fuente_integro(ch0) in msg)
    check("el mensaje E3 contiene la extracción renderizada (datos)",
          render_extraccion(val0) in msg)

    # ---------------- C. Determinismo -------------------------------------- #
    print("\n[C] determinismo del prompt")
    muestra = pares[::17]
    det = all(
        canon(prompt_e3.build_request_kwargs(c, v, model="M")) ==
        canon(prompt_e3.build_request_kwargs(c, v, model="M"))
        for c, v in muestra
    )
    check(f"mismos datos → mismo request byte a byte ({len(muestra)} unidades)", det)
    c0 = json.loads(json.dumps(ch0))
    v0 = json.loads(json.dumps(val0))
    check("datos re-parseados desde JSON → request idéntico",
          canon(prompt_e3.build_request_kwargs(c0, v0, model="M")) ==
          canon(prompt_e3.build_request_kwargs(ch0, val0, model="M")))

    # tratamiento de flaggeados (ningún chunk de pro está flaggeado: se
    # ejercita con un chunk flaggeado real de otro TO y validación mínima)
    ch_flag = {c["id"]: c for c in cargar_chunks(("ric",))}["ric::3.1.2"]
    val_min = {"entidades": [], "relaciones": [], "omisiones_no_prosa": []}
    check("chunk flaggeado por E0 → el mensaje E3 instruye evaluar "
          "contenido_tabular_no_declarado",
          "contenido_tabular_no_declarado" in prompt_e3.build_user_message(ch_flag, val_min)
          and "contenido_tabular_no_declarado" not in prompt_e3.build_user_message(ch0, val0))

    # ---------------- D. Calibradores --------------------------------------- #
    print("\n[D] calibradores resueltos")
    cals = prompt_e3.CALIBRADORES
    check("hay exactamente 4 calibradores", len(cals) == 4)
    check("tipos cubiertos: calificador_despojado, excepcion_ausente, "
          "enumeracion_incompleta y completo_ok",
          [c["veredicto"]["veredicto"] for c in cals] ==
          ["faltantes_detectados"] * 3 + ["completo_ok"]
          and [f["tipo"] for c in cals[:3] for f in c["veredicto"]["faltantes"]] ==
          ["calificador_despojado", "calificador_despojado",
           "excepcion_ausente", "enumeracion_incompleta"])
    todos_chunks = {c["id"]: c for c in cargar_chunks(("cla", "pro", "ric"))}
    citas_ok = all(
        cita_en_fuente(f["cita_textual_del_fuente"], todos_chunks[cal["chunk_id"]])
        for cal in cals for f in cal["veredicto"]["faltantes"]
    )
    check("toda cita de calibrador verifica contra el fuente real de su chunk", citas_ok)
    cal3 = cals[2]
    check("la cita del calibrador 3 cruza un guion de corte de línea del PDF "
          "('si-\\nguientes') y aun así verifica",
          "si-\nguientes" in cal3["fuente"]
          and "siguientes" in cal3["veredicto"]["faltantes"][0]["cita_textual_del_fuente"]
          and cita_en_fuente(cal3["veredicto"]["faltantes"][0]["cita_textual_del_fuente"],
                             todos_chunks["cla::6.5.1.1"]))
    import calibradores_e3 as _cal_mod
    from comun_e3 import cargar_extracciones_faseB
    val_real = cargar_extracciones_faseB()["pro::1.1.2.5"]["validacion"]
    cal4 = cals[3]
    check("el calibrador completo_ok ES la extracción real de fase B (byte a byte)",
          canon(cal4["extraccion"]["entidades"]) == canon(val_real["entidades"])
          and canon(cal4["extraccion"]["relaciones"]) == canon(val_real["relaciones"]))
    check("el par mínimo CAL-2/CAL-4 comparte fuente y difiere en extracción",
          cals[1]["fuente"] == cal4["fuente"]
          and canon(cals[1]["extraccion"]) != canon(cal4["extraccion"]))
    cal1 = cals[0]
    extr1_desc = next(e for e in cal1["extraccion"]["entidades"]
                      if e["local_id"] == "e3")["properties"]["descripcion"]
    check("CAL-1 reproduce la amputación C7: la extracción NO contiene los dos "
          "calificadores y el fuente SÍ",
          "Responsabilidad Patrimonial Computable informada" not in extr1_desc
          and "calculada según datos del mes n" not in extr1_desc
          and normalizar_para_cita("Responsabilidad Patrimonial Computable informada en el mes n")
          in normalizar_para_cita(cal1["fuente"]))

    # ---------------- E. Capa determinística de citas ----------------------- #
    print("\n[E] verificación determinística de citas")
    ch_ric = todos_chunks["ric::7.1"]
    check("positivo: cita que cruza guiones del PDF verifica "
          "('dismi-\\nnución de la exigencia')",
          cita_en_fuente("disminución de la exigencia", ch_ric))
    check("negativo: cita fabricada NO verifica",
          not cita_en_fuente("los sujetos presentarán declaración jurada anual", ch_ric))
    check("insensible a espacios y saltos de línea",
          cita_en_fuente("Franquicia   informada\nen el mes n", ch_ric))
    check("cita vacía NO verifica", not cita_en_fuente("   ", ch_ric))

    # casos REALES caídos en la calibración fase B (laudo: normalización
    # extendida + fuente sin rótulos). Chunk real: pro::2.3.1.1.
    ch_2311 = chunks_pro["pro::2.3.1.1"]
    cita_guion_espacio = ("ix) El derecho de solicitar la apertura de la Caja de Ahorros "
                          "en pesos con las presta- ciones previstas en el punto 1.8. del "
                          "TO sobre Depósitos de Ahorro, Cuenta Sueldo y Especiales, las "
                          "cuales serán gratuitas.")
    check("caso real fase B: cita con guion+espacio del PDF («presta- ciones») "
          "verifica con la normalización extendida",
          cita_en_fuente(cita_guion_espacio, ch_2311))
    cita_cruza_bloques = ("x) Los restantes requisitos normativamente reglamentados "
                          "según el producto o servicio de que se trate.")
    check("caso real fase B: cita que cruza una frontera de bloques intersticiales "
          "cortada a mitad de palabra ('servi-'/'cio') verifica contra el fuente "
          "sin rótulos",
          cita_en_fuente(cita_cruza_bloques, ch_2311)
          and "servi-" in comun_e3.fuente_integro(ch_2311)
          and "[intersticial | punto 2.3.1]" not in comun_e3.fuente_para_citas(ch_2311))

    # ---------------- F. Flujo del mini-ratchet (fixtures + stubs) ---------- #
    print("\n[F] mini-ratchet con stubs (fixtures)")
    with (BASE / "fixtures" / "fixtures_e3.json").open(encoding="utf-8") as f:
        fx = json.load(f)

    out_dir = BASE / "salida" / "selftest_out"
    if out_dir.exists():
        shutil.rmtree(out_dir)

    # F.1 — amputada: detección → reintento → aceptado
    fa = fx["amputada"]
    chunk_a = chunks_pro[fa["chunk_id"]]
    check("la fixture amputada NO contiene el calificador y el fuente SÍ",
          all(fa["calificador_eliminado"] not in canon(e)
              for e in fa["validacion_amputada"]["entidades"])
          and cita_en_fuente(fa["calificador_eliminado"], chunk_a))

    stub_e3 = cliente_e3.StubClienteE3([fa["veredicto_stub_faltante"], fa["veredicto_stub_ok"]])
    stub_e1 = cliente_e1.StubClienteE1([fa["tool_input_reintento"]])
    registro = ratchet_e3.RegistroE3(out_dir)
    exp = ratchet_e3.ciclo_ratchet(
        chunk_a, fa["validacion_amputada"],
        cliente_verificador=stub_e3, cliente_extractor=stub_e1,
        model_e3="MODELO_FUERTE", model_e1="MODELO_CHICO", registro=registro)
    check("amputada: estado aceptado_tras_reintento",
          exp["estado"] == "aceptado_tras_reintento", exp["estado"])
    check("amputada: la extracción final SÍ contiene el calificador",
          fa["calificador_eliminado"] in canon(exp["validacion_final"]["entidades"]))
    check("amputada: 2 llamadas E3 (verificación + re-verificación), 1 E1 (reintento)",
          len(stub_e3.requests_recibidos) == 2 and len(stub_e1.requests_recibidos) == 1)

    # el reintento preserva el prefijo E1 byte a byte (feedback tras el breakpoint)
    kw_orig = prompt_e1.build_request_kwargs(chunk_a, model="MODELO_CHICO")
    kw_reint = stub_e1.requests_recibidos[0]
    check("reintento: system + tools + tool_choice E1 byte-idénticos al request "
          "original (el caché del prefijo NO se invalida)",
          canon({"system": kw_reint["system"], "tools": kw_reint["tools"],
                 "tool_choice": kw_reint["tool_choice"]}) ==
          canon({"system": kw_orig["system"], "tools": kw_orig["tools"],
                 "tool_choice": kw_orig["tool_choice"]}))
    msg_reint = kw_reint["messages"][0]["content"]
    msg_orig = kw_orig["messages"][0]["content"]
    check("reintento: el mensaje E1 original es PREFIJO del mensaje del reintento "
          "(el feedback va anexado al final, después del breakpoint)",
          msg_reint.startswith(msg_orig) and msg_reint != msg_orig)
    check("reintento: marcado como reintento, con la cita del faltante",
          ratchet_e3.MARCA_REINTENTO in msg_reint
          and fa["calificador_eliminado"] in msg_reint)

    # F.2 — completa: pasa directo, sin tocar al extractor
    fc = fx["completa"]
    stub_e3b = cliente_e3.StubClienteE3([fc["veredicto_stub_ok"]])
    stub_e1b = cliente_e1.StubClienteE1([])
    exp_ok = ratchet_e3.ciclo_ratchet(
        chunks_pro[fc["chunk_id"]], fc["validacion"],
        cliente_verificador=stub_e3b, cliente_extractor=stub_e1b,
        model_e3="MODELO_FUERTE", model_e1="MODELO_CHICO", registro=registro)
    check("completa: estado completo_ok_directo con 1 sola llamada E3 y 0 E1",
          exp_ok["estado"] == "completo_ok_directo"
          and len(stub_e3b.requests_recibidos) == 1
          and len(stub_e1b.requests_recibidos) == 0)
    check("completa: la validación final es la original, intacta",
          canon(exp_ok["validacion_final"]) == canon(fc["validacion"]))

    # F.3 — tope agotado: faltantes persistentes → cola humana con flag y TODO
    stub_e3c = cliente_e3.StubClienteE3([fa["veredicto_stub_faltante"],
                                         fa["veredicto_stub_faltante"]])
    stub_e1c = cliente_e1.StubClienteE1([fa["tool_input_reintento"]])
    exp_tope = ratchet_e3.ciclo_ratchet(
        chunk_a, fa["validacion_amputada"],
        cliente_verificador=stub_e3c, cliente_extractor=stub_e1c,
        model_e3="MODELO_FUERTE", model_e1="MODELO_CHICO", registro=registro)
    check("tope: estado cola_humana tras exactamente 1 reintento "
          "(2 llamadas E3, 1 llamada E1)",
          exp_tope["estado"] == "cola_humana"
          and len(stub_e3c.requests_recibidos) == 2
          and len(stub_e1c.requests_recibidos) == 1)
    check("tope: validacion_final es None — nada ingresa al grafo en silencio",
          exp_tope["validacion_final"] is None)

    # F.4 — veredicto incoherente y cita fabricada
    ev_inc = ratchet_e3.evaluar_veredicto(fx["veredicto_incoherente"], chunk_a)
    check("veredicto incoherente (completo_ok con faltantes) NO cuenta como ok",
          not ev_inc["es_completo_ok"]
          and "completo_ok_con_faltantes" in ev_inc["incoherencias"])
    ev_fab = ratchet_e3.evaluar_veredicto(fx["veredicto_cita_inventada"], chunk_a)
    check("cita fabricada: faltante registrado pero NO utilizable para el ratchet",
          len(ev_fab["faltantes"]) == 1 and not ev_fab["faltantes_utilizables"])
    stub_e3d = cliente_e3.StubClienteE3([fx["veredicto_cita_inventada"]])
    stub_e1d = cliente_e1.StubClienteE1([])
    exp_fab = ratchet_e3.ciclo_ratchet(
        chunk_a, fa["validacion_amputada"],
        cliente_verificador=stub_e3d, cliente_extractor=stub_e1d,
        model_e3="MODELO_FUERTE", model_e1="MODELO_CHICO", registro=registro)
    check("veredicto sin ninguna cita verificable → cola humana con flag propio, "
          "sin re-extraer sobre citas fabricadas",
          exp_fab["estado"] == "cola_humana_veredicto_inutilizable"
          and len(stub_e1d.requests_recibidos) == 0)

    # F.5 — persistencia: TODOS los veredictos + cola humana con TODO
    with (out_dir / "veredictos.jsonl").open(encoding="utf-8") as f:
        veredictos = [json.loads(l) for l in f]
    with (out_dir / "cola_humana.jsonl").open(encoding="utf-8") as f:
        cola = [json.loads(l) for l in f]
    check("todos los veredictos persistidos (2 amputada + 1 completa + 2 tope "
          "+ 1 fabricada = 6)", len(veredictos) == 6, f"hay {len(veredictos)}")
    check("cola humana: 2 entradas (tope + veredicto inutilizable), cada una "
          "con flag y TODO",
          len(cola) == 2
          and all(c["flag"] and c["todo"].startswith("TODO:") for c in cola)
          and {c["flag"] for c in cola} ==
          {"cola_humana", "cola_humana_veredicto_inutilizable"})

    # ---------------- G. Keys de caché local y namespace -------------------- #
    print("\n[G] keys de caché local (never-pay-twice, offline)")
    ns = cliente_e3.namespace_e3()
    k1 = lc.compute_key(ns, lc.canonical_request(
        prompt_e3.build_request_kwargs(*pares[0], model="M")))
    k2 = lc.compute_key(ns, lc.canonical_request(
        prompt_e3.build_request_kwargs(*pares[0], model="M")))
    k3 = lc.compute_key(ns, lc.canonical_request(
        prompt_e3.build_request_kwargs(*pares[1], model="M")))
    check("key determinística por unidad", k1 == k2)
    check("keys distintas entre unidades", k1 != k3)
    check("namespace propio: dominio e3_verificacion + code-version + hash del "
          "prompt del verificador",
          ns.startswith("e3_verificacion") and "e3-verificador-v1" in ns
          and prompt_e3.PREFIJO_HASH in ns and "think=0" in ns, ns)
    check("el hash del prompt E3 difiere del de E1 (contratos independientes)",
          prompt_e3.PREFIJO_HASH != prompt_e1.PREFIJO_HASH)

    # ---------------- H. Estimación reproducible ---------------------------- #
    print("\n[H] estimación reproducible")
    import estimacion_e3
    r1 = estimacion_e3.estimar()
    r2 = estimacion_e3.estimar()
    check("dos corridas de la estimación → resultado idéntico", canon(r1) == canon(r2))
    check("calibración = 87 unidades aceptadas; corpus = 1.477",
          r1["calibracion"]["n_unidades"] == 87 and r1["corpus"]["n_unidades"] == 1477)

    print(f"\nprefijo E3: hash {prompt_e3.PREFIJO_HASH} | namespace {ns}")
    print(f"RESULTADO: {OK} ok, {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
