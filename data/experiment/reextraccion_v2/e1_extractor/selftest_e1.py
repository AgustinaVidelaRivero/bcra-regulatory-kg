"""
selftest_e1.py — Selftest OFFLINE de E1 (T4). Cero llamadas a APIs de LLM:
el único cliente que se instancia es StubClienteE1.

Verifica:
  A. Prefijo estable IDÉNTICO entre chunks (condición del caching, Decisión 1):
     system + tools + tool_choice byte-idénticos para los 1.477 chunks, con el
     breakpoint cache_control {"type":"ephemeral"} declarado en el último
     bloque del system, y nada variable antes del breakpoint.
  B. Prompt determinístico: mismo chunk → mismo request byte a byte (incluida
     una reconstrucción del chunk vía re-parseo JSON, contra riesgos de orden).
  C. Tratamiento de flaggeados: el bloque FLAGS E0 (con su evidencia) aparece
     exactamente en los chunks flaggeados y en ningún otro.
  D. Stub → parseo → validación: fixtures buenas aceptadas íntegras (con
     provenance normalizada completa); fixtures malas rechazadas con el motivo
     esperado; tratamiento de flags registrado (omisión declarada vs
     advertencia).
  E. Keys de caché local (llm_cache puro, sin DB): determinísticas por chunk,
     distintas entre chunks, sensibles al prefijo.
  F. Estimación reproducible: dos corridas → resultado idéntico.
  G. Enmienda 01: el selftest corre sobre la salida E0 enm01 (1.763 unidades
     = 1.477 chunks + 286 mini-chunks). Checks nuevos: rotación declarada del
     prefijo/namespace vs el sellado; mensaje del hijo instruye NO extraer de
     bloques heredados; mensaje del mini declara el bloque como unidad;
     puntos admitidos del mini = SOLO su unidad de origen (el validador
     rechaza anclajes a ancestros); puntos admitidos del hijo = propia +
     unidades con tramo encabezado (extensión sin cambio: no-op declarado);
     rol_documental de elementos de mini = bloque_<rol>. La estimación (F)
     sigue anclada a la salida sellada (sus números 88/1.477 son de la
     calibración sellada).

Uso:  python3 selftest_e1.py
"""

from __future__ import annotations

import json
import sys

import comun_e1
from comun_e1 import (BASE, E0_SALIDA_ENM01, cargar_chunks, chunk_flaggeado,
                      es_mini_chunk, puntos_admitidos, rol_documental_de_punto)
import prompt_e1
import cliente_e1
import validador_e1
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
    chunks = cargar_chunks(e0_dir=E0_SALIDA_ENM01)
    por_id = {c["id"]: c for c in chunks}
    print(f"chunks E0 (enm01) cargados: {len(chunks)}")
    check("salida enm01: 1.763 unidades = 1.477 chunks + 286 mini-chunks",
          len(chunks) == 1763
          and sum(1 for c in chunks if es_mini_chunk(c)) == 286)

    # ---------------- A. Prefijo estable e idéntico entre chunks -----------
    print("\n[A] prefijo estable")
    ref = None
    prefijo_identico = True
    texto_en_prefijo = False
    for c in chunks:
        kw = prompt_e1.build_request_kwargs(c, model="MODELO_FASE_B")
        pref = canon({"system": kw["system"], "tools": kw["tools"],
                      "tool_choice": kw["tool_choice"]})
        if ref is None:
            ref = pref
        elif pref != ref:
            prefijo_identico = False
            break
        # fuga de texto variable al prefijo: solo textos con longitud
        # discriminante (los mini-chunks diminutos —'n1', 2 chars— matchean
        # cualquier prosa por azar y no son evidencia de fuga)
        if len(c["texto"]) >= 40 and c["texto"][:80] in pref:
            texto_en_prefijo = True
            break
    check("prefijo (system+tools+tool_choice) idéntico en las 1.763 unidades (chunks + minis)",
          prefijo_identico and ref is not None)
    check("nada del texto variable (≥40 chars) aparece en el prefijo", not texto_en_prefijo)

    kw0 = prompt_e1.build_request_kwargs(chunks[0], model="MODELO_FASE_B")
    sistema = kw0["system"]
    check("system es lista de bloques (jamás string plano)", isinstance(sistema, list))
    check("breakpoint cache_control ephemeral en el ÚLTIMO bloque del system",
          isinstance(sistema, list) and sistema
          and sistema[-1].get("cache_control") == {"type": "ephemeral"})
    check("un solo bloque de system (todo lo estable antes del breakpoint)",
          isinstance(sistema, list) and len(sistema) == 1)
    check("lo variable va en messages, después del breakpoint",
          chunks[0]["texto"][:80] in kw0["messages"][0]["content"])
    check("catálogo de sujetos embebido en el prefijo (enum del tool schema)",
          "Sujeto_entidad_financiera" in canon(kw0["tools"]))

    # cobertura del rol por-TO: los 5 archivos tienen rol de alcance
    from schema import ROL_POR_TO
    archivos = {c["archivo"] for c in chunks}
    check("los 5 TOs de E0 tienen rol de alcance en el catálogo",
          archivos <= set(ROL_POR_TO.keys()), f"faltan: {archivos - set(ROL_POR_TO)}")

    # ---------------- B. Determinismo ---------------------------------------
    print("\n[B] determinismo del prompt")
    muestra = chunks[::150] + [c for c in chunks if chunk_flaggeado(c)][:5]
    det = all(
        canon(prompt_e1.build_request_kwargs(c, model="M")) ==
        canon(prompt_e1.build_request_kwargs(c, model="M"))
        for c in muestra
    )
    check(f"mismo chunk → mismo request byte a byte ({len(muestra)} chunks)", det)
    c0 = json.loads(json.dumps(chunks[0]))  # re-parseo: chunk reconstruido
    check("chunk re-parseado desde JSON → request idéntico",
          canon(prompt_e1.build_request_kwargs(c0, model="M")) ==
          canon(prompt_e1.build_request_kwargs(chunks[0], model="M")))

    # ---------------- C. Flaggeados -----------------------------------------
    print("\n[C] tratamiento de flaggeados")
    flaggeados = [c for c in chunks if chunk_flaggeado(c)]
    check(f"E0 enm01 declara 65 unidades flaggeadas (hay {len(flaggeados)})", len(flaggeados) == 65)
    con_bloque = sum("FLAGS E0" in prompt_e1.build_user_message(c) for c in flaggeados)
    sin_bloque = sum("FLAGS E0" in prompt_e1.build_user_message(c)
                     for c in chunks if not chunk_flaggeado(c))
    check("bloque FLAGS E0 presente en TODOS los flaggeados", con_bloque == len(flaggeados))
    check("bloque FLAGS E0 ausente en TODOS los no flaggeados", sin_bloque == 0)
    ric = por_id["ric::3.1.2"]
    msg_ric = prompt_e1.build_user_message(ric)
    check("la evidencia determinística de E0 viaja en el mensaje",
          "C = (k x 0,08 x APR ) + INC" in msg_ric)
    check("instrucción no-prosa referenciada en el mensaje flaggeado",
          "omisiones_no_prosa" in msg_ric)

    # ---------------- D. Stub → parseo → validación -------------------------
    print("\n[D] stub → parseo → validación (fixtures)")
    with (BASE / "fixtures" / "fixtures_e1.json").open(encoding="utf-8") as f:
        fixtures = json.load(f)

    for fx in fixtures["buenas"]:
        chunk = por_id[fx["chunk_id"]]
        stub = cliente_e1.StubClienteE1([fx["tool_input"]])
        out = cliente_e1.extraer_chunk(stub, chunk, model="MODELO_FASE_B")
        res = validador_e1.validar_salida(out["tool_input"], chunk)
        esp = fx["espera"]
        check(f"buena[{fx['nota'][:50]}…] aceptada",
              out["error"] is None
              and len(res.entidades) == esp["entidades"]
              and len(res.relaciones) == esp["relaciones"]
              and len(res.rechazos) == esp["rechazos"],
              f"ent={len(res.entidades)} rel={len(res.relaciones)} rech={res.rechazos}")
        check("  …provenance completa en todo elemento",
              all(set(e["provenance"]) == {"to", "archivo", "punto", "rol_documental"}
                  for e in res.entidades + res.relaciones))

    # provenance de herencia: el elemento con punto '1.1' sale como herencia_encabezado
    chunk111 = por_id["pro::1.1.1"]
    res_b1 = validador_e1.validar_salida(fixtures["buenas"][0]["tool_input"], chunk111)
    e_her = [e for e in res_b1.entidades if e["provenance"]["punto"] == "1.1"]
    check("elemento anclado a herencia lleva rol_documental de su origen",
          len(e_her) == 1 and e_her[0]["provenance"]["rol_documental"] == "herencia_encabezado",
          str([e["provenance"] for e in res_b1.entidades]))
    # slip tolerado: target espurio en aplica_a anulado
    res_b2 = validador_e1.validar_salida(fixtures["buenas"][1]["tool_input"], chunk111)
    ap = [r for r in res_b2.relaciones if r["predicate"] == "aplica_a"]
    check("target espurio en aplica_a anulado (slip tolerado, herencia v2)",
          len(ap) == 1 and ap[0]["target"] is None and ap[0]["sujeto_propuesto"] is not None)

    for fx in fixtures["malas"]:
        chunk = por_id[fx["chunk_id"]]
        res = validador_e1.validar_salida(fx["tool_input"], chunk)
        motivos = {r["motivo"] for r in res.rechazos}
        check(f"mala[{fx['nota'][:55]}…] → {fx['espera_motivo']}",
              fx["espera_motivo"] in motivos, f"motivos={motivos}")

    fl = fixtures["flaggeado"]
    chunk_fl = por_id[fl["chunk_id"]]
    res_ok = validador_e1.validar_salida(fl["tool_input_conforme"], chunk_fl)
    check("flaggeado conforme: omisión registrada, cero rechazos, cero advertencias",
          not res_ok.rechazos and not res_ok.advertencias
          and len(res_ok.omisiones_no_prosa) == 1,
          f"rech={res_ok.rechazos} adv={res_ok.advertencias}")
    res_sd = validador_e1.validar_salida(fl["tool_input_sin_declarar"], chunk_fl)
    check("flaggeado sin declarar omisiones → advertencia registrada",
          any(a["tipo"] == "flag_sin_omisiones_declaradas" for a in res_sd.advertencias),
          str(res_sd.advertencias))

    # el stub recibió exactamente el request canónico del chunk
    stub = cliente_e1.StubClienteE1([fixtures["buenas"][0]["tool_input"]])
    cliente_e1.extraer_chunk(stub, chunk111, model="MODELO_FASE_B")
    check("el stub recibe el request canónico de build_request_kwargs",
          canon(stub.requests_recibidos[0]) ==
          canon(prompt_e1.build_request_kwargs(chunk111, model="MODELO_FASE_B")))

    # ---------------- E. Keys de caché local (puras, sin DB) ----------------
    print("\n[E] keys de caché local (never-pay-twice, offline)")
    ns = cliente_e1.namespace_e1()
    k_a1 = lc.compute_key(ns, lc.canonical_request(
        prompt_e1.build_request_kwargs(chunks[0], model="M")))
    k_a2 = lc.compute_key(ns, lc.canonical_request(
        prompt_e1.build_request_kwargs(chunks[0], model="M")))
    k_b = lc.compute_key(ns, lc.canonical_request(
        prompt_e1.build_request_kwargs(chunks[1], model="M")))
    check("key determinística por chunk", k_a1 == k_a2)
    check("keys distintas entre chunks", k_a1 != k_b)
    check("namespace lleva code-version propio y hash del prefijo",
          "e1-extractor-v1" in ns and prompt_e1.PREFIJO_HASH in ns and "think=0" in ns, ns)

    # ---------------- G. Enmienda 01: mini-chunks y división de responsabilidad
    print("\n[G] enmienda 01: mini-chunks y contexto-que-ancla")
    resumen_sellado = json.loads(
        (BASE / "salida" / "faseB_pro" / "resumen_faseB.json").read_text(encoding="utf-8"))
    check("el prefijo E1 ROTÓ respecto del sellado (candado de la enmienda: "
          "cambio de prompt → namespace nuevo, corrida se paga completa)",
          prompt_e1.PREFIJO_HASH != resumen_sellado["prefijo_hash"],
          f"{prompt_e1.PREFIJO_HASH} vs {resumen_sellado['prefijo_hash']}")
    check("el namespace de caché porta el hash nuevo",
          prompt_e1.PREFIJO_HASH in cliente_e1.namespace_e1())

    mini = por_id["pro::2.7::intro"]
    hijo = por_id["pro::2.7.1"]
    msg_mini = prompt_e1.build_user_message(mini)
    msg_hijo = prompt_e1.build_user_message(hijo)
    check("mensaje del mini declara el bloque como unidad de extracción",
          "MINI-CHUNK" in msg_mini and "TU unidad de extracción" in msg_mini)
    check("mensaje del mini: cadena de títulos marcada como no-extraíble",
          "NO es contenido a extraer" in msg_mini)
    check("mensaje del hijo instruye NO extraer de los bloques heredados",
          "NO extraigas" in msg_hijo and "Tipo de unidad: chunk de punto" in msg_hijo)
    check("prefijo del sistema instruye 'EL CONTEXTO ANCLA, LA UNIDAD EXTRAE'",
          "EL CONTEXTO ANCLA, LA UNIDAD EXTRAE" in prompt_e1.PREFIJO_SISTEMA)

    check("puntos admitidos del mini = SOLO su unidad de origen",
          puntos_admitidos(mini) == ["2.7"])
    minis_todos = [c for c in chunks if es_mini_chunk(c)]
    check("…para los 286 minis",
          all(puntos_admitidos(m) == [m["unidad"]] for m in minis_todos))
    check("puntos admitidos del hijo: propia + unidades con tramo encabezado "
          "(extensión sin cambio — no-op declarado en comun_e1)",
          all(set(puntos_admitidos(c)) ==
              {c["unidad"]} | {h["unidad_origen"] for h in c.get("herencia", [])
                               if h["tipo"] == "encabezado"}
              for c in chunks if not es_mini_chunk(c)))

    # el validador rechaza un elemento del mini anclado a un ancestro
    ti_mal = {"entities": [
        {"local_id": "to", "type": "TextoOrdenado", "label": "TO Protección",
         "punto": "2.7", "properties": {}},
        {"local_id": "e1", "type": "Obligacion", "label": "Hipervínculos de baja",
         "punto": "S2", "properties": {"descripcion": "x"}}],
        "relations": []}
    res_mal = validador_e1.validar_salida(ti_mal, mini)
    check("validador: elemento de mini anclado a ancestro (S2) → "
          "punto_fuera_de_admitidos",
          any(r["motivo"] == "punto_fuera_de_admitidos" for r in res_mal.rechazos)
          and len(res_mal.entidades) == 1)
    ti_ok = {"entities": [
        {"local_id": "to", "type": "TextoOrdenado", "label": "TO Protección",
         "punto": "2.7", "properties": {}},
        {"local_id": "e1", "type": "Obligacion", "label": "Hipervínculos de baja",
         "punto": "2.7", "properties": {"descripcion": "x"}}],
        "relations": []}
    res_ok2 = validador_e1.validar_salida(ti_ok, mini)
    check("validador: elemento del mini anclado a su unidad → aceptado con "
          "rol_documental bloque_<rol>",
          not res_ok2.rechazos
          and len(res_ok2.entidades) == 2
          and all(e["provenance"]["rol_documental"] == "bloque_intro"
                  for e in res_ok2.entidades))
    check("rol_documental_de_punto(mini) = bloque_intro",
          rol_documental_de_punto(mini, "2.7") == "bloque_intro")

    # ---------------- F. Estimación reproducible ----------------------------
    print("\n[F] estimación reproducible (anclada a la salida sellada)")
    import estimacion_e1
    r1 = estimacion_e1.estimar()
    r2 = estimacion_e1.estimar()
    check("dos corridas de la estimación → resultado idéntico", canon(r1) == canon(r2))
    check("calibración = 88 chunks de pro", r1["calibracion"]["n_chunks"] == 88)
    check("corpus = 1.477 chunks", r1["corpus"]["n_chunks"] == 1477)

    print(f"\nRESULTADO: {OK} ok, {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
