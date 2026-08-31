"""
selftest_control_esq_p1bis.py — SELFTEST OFFLINE previo al gasto de la
re-corrida del control (U-ESQ-1d.c). USD 0, sin API; escribe solo en
selftest_out/ (gitignorado).

Cubre lo exigido por el mandato:
  1. GUARDAS DEL PREFIJO NUEVO — hash recalculado tras la corrección de la
     description (== cc.PREFIJO_HASH_ABIERTO_ESPERADO, != el del control
     original, != producción), namespace particionado nuevo, schema con los
     dos campos propuestos, description corregida presente y sin ejemplos de
     valores.
  2. BYTE-IDENTIDAD DEL MODO CERRADO — sha256 completos del prefijo canónico
     y del tool schema de producción contra los candados sellados
     pre-edición (selftest_canal_abierto_e1.py:53-55), namespace cerrado
     idéntico al de producción, tool_schema_e1() devuelve EL MISMO objeto.
  3. FIXTURES DOPADAS — 10 = 5 tipo + 5 predicado, 2 por TO; cada dopada es
     su base + EXACTAMENTE una cláusula appendeada (ninguna otra clave
     cambia salvo id y texto); bases limpias, sin flags, sin mini-chunks,
     disyuntas de las 40 del control original; cláusulas NO sembradas en
     system ni tool (regla de la adenda §3.b).
  4. DOPADAS EXCLUIDAS DE TODO CONTEO DE ESQ-1 — ids con prefijo reservado
     dop:: ausentes del universo de producción y de E0; el jsonl de la
     re-corrida no está entre los insumos de producción de cadenas_esq.
  5. CONTEOS P1′ — el umbral compuesto (≥7 total Y ≥3 por mitad), el canal
     equivocado cuenta como 'otro_canal' y no suma, error == no-emite (D-g),
     C sin cambio.
  6. CORRIDA STUB END-TO-END del runner p1bis — 20 unidades, requests con el
     prefijo abierto NUEVO, reanudación idempotente, claves de producción.
  7. ANCLAS — umbrales transcriptos == adenda sellada; tope parcial 0,50.

Uso:  .venv/bin/python3 -B data/experiment/esq/code/selftest_control_esq_p1bis.py
"""

from __future__ import annotations

import copy
import hashlib
import json
import shutil
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_control_esq as cc             # noqa: E402
import runner_control_esq as rc            # noqa: E402
import runner_control_esq_p1bis as rp      # noqa: E402
import comun_e1                            # noqa: E402
import prompt_e1                           # noqa: E402
import cliente_e1                          # noqa: E402
import llm_cache as lc                     # noqa: E402

OUT = cc.SELFTEST_DIR / "control_stub_p1bis"

_checks = []


def check(nombre, cond):
    _checks.append((nombre, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {nombre}")


def canon(o):
    return json.dumps(o, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def sha(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def reg_crudo(entities=None, relations=None, error=None):
    return {"chunk_id": "fx", "unidad": "1.1", "tipo_unidad": "punto",
            "titulo": "t", "stop_reason": "tool_use", "error": error,
            "usage": {"input_tokens": 0, "output_tokens": 0,
                      "cache_write_tokens": 0, "cache_read_tokens": 0},
            "tool_input_crudo": {"entities": entities or [],
                                 "relations": relations or [],
                                 "omisiones_no_prosa": []},
            "validacion": {"entidades": [], "relaciones": [], "rechazos": []}}


def main() -> int:
    print("== selftest_control_esq_p1bis (offline, $0) ==\n")
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    # ---------------- 1. guardas del prefijo nuevo -------------------------- #
    print("· guardas del prefijo nuevo (description corregida)")
    check("hash abierto recalculado == cc.PREFIJO_HASH_ABIERTO_ESPERADO",
          prompt_e1.PREFIJO_HASH_CANAL_ABIERTO == cc.PREFIJO_HASH_ABIERTO_ESPERADO)
    check("hash abierto NUEVO != hash del control original (bca492bbf7c8) y "
          "!= producción",
          prompt_e1.PREFIJO_HASH_CANAL_ABIERTO
          != cc.PREFIJO_HASH_ABIERTO_CONTROL_ORIGINAL
          and prompt_e1.PREFIJO_HASH_CANAL_ABIERTO != prompt_e1.PREFIJO_HASH)
    ns_on = cliente_e1.namespace_e1(canal_abierto=True)
    check("namespace abierto porta el hash nuevo y NO el viejo (partición: la "
          "re-corrida jamás relee la caché del control original)",
          f"p{cc.PREFIJO_HASH_ABIERTO_ESPERADO}" in ns_on
          and cc.PREFIJO_HASH_ABIERTO_CONTROL_ORIGINAL not in ns_on)
    ts_on = prompt_e1.tool_schema_e1(canal_abierto=True)
    props_e = ts_on["input_schema"]["properties"]["entities"]["items"]["properties"]
    props_r = ts_on["input_schema"]["properties"]["relations"]["items"]["properties"]
    check("schema abierto declara tipo_propuesto y predicado_propuesto",
          "tipo_propuesto" in props_e and "predicado_propuesto" in props_r)
    desc_on = ts_on["description"]
    check("description abierta corregida: nombra los dos campos y la "
          "exclusión mutua, y ya NO dice «schema cerrado»",
          "tipo_propuesto" in desc_on and "predicado_propuesto" in desc_on
          and "mutuamente excluyentes" in desc_on
          and "schema cerrado" not in desc_on)
    # no sembrar: la description no trae valores de ejemplo de tipos ni
    # predicados (los 6 types y 12 predicates del enum pueden nombrarse solo
    # por conteo, jamás por valor nuevo; ningún string tipo "Sancion" etc.)
    enums = set(props_e["type"]["enum"]) | set(props_r["predicate"]["enum"])
    check("description abierta sin ejemplos de valores fuera de los enums "
          "(ningún token con forma de tipo/predicado nuevo sembrado)",
          not any(x in desc_on for x in
                  ("Sancion", "Presuncion", "Definicion", "Vigencia",
                   "Facultad", "equivale", "asimila", "complementa",
                   "acredita", "computa_conjuntamente")))
    check("enums del tool abierto intactos (6 types, 12 predicates)",
          len(props_e["type"]["enum"]) == 6 and len(props_r["predicate"]["enum"]) == 12
          and enums == set(props_e["type"]["enum"]) | set(props_r["predicate"]["enum"]))

    # ---------------- 2. byte-identidad del modo cerrado -------------------- #
    print("· byte-identidad del modo cerrado (candados sellados pre-edición)")
    check("sha256 completo del prefijo canónico cerrado == candado de producción",
          sha(prompt_e1.PREFIJO_CANONICO) == rp.SHA256_PREFIJO_PROD)
    check("sha256 completo del tool schema cerrado == candado de producción",
          sha(canon(prompt_e1.TOOL_SCHEMA_E1)) == rp.SHA256_TOOL_SCHEMA_PROD)
    check("tool_schema_e1() (flag apagado) devuelve EL MISMO objeto de producción",
          prompt_e1.tool_schema_e1() is prompt_e1.TOOL_SCHEMA_E1)
    check("namespace cerrado idéntico al de producción",
          cliente_e1.namespace_e1(False) == rp.NAMESPACE_PROD)
    check("description cerrada intacta (sigue diciendo «schema cerrado v2»)",
          "schema cerrado v2" in prompt_e1.TOOL_SCHEMA_E1["description"])

    # ---------------- 3. fixtures dopadas ----------------------------------- #
    print("· fixtures dopadas")
    fx = rp.cargar_fixtures()
    dop = fx["dopadas"]
    check("10 dopadas = 5 tipo + 5 predicado, 2 por TO",
          len(dop) == 10
          and sum(1 for d in dop if d["mitad"] == "tipo") == 5
          and all(sum(1 for d in dop if d["to"] == t) == 2 for t in cc.TOS))
    por_id = rc.chunks_por_id()
    ok_texto, ok_solo_texto, ok_bases = True, True, True
    universo = cc.cargar_universo()
    sel_orig = {s["chunk_id"] for s in cc.seleccionar(universo)}
    for d in dop:
        base = por_id[d["chunk_id_base"]]
        ch = d["chunk"]
        if ch["texto"] != base["texto"].rstrip() + "\n" + d["clausula_plantada"]:
            ok_texto = False
        if ch["texto"].count(d["clausula_plantada"]) != 1:
            ok_texto = False
        difieren = {k for k in set(base) | set(ch)
                    if base.get(k) != ch.get(k)}
        if difieren != {"id", "texto"}:
            ok_solo_texto = False
        reg = universo[d["chunk_id_base"]]
        if not (cc.es_limpia(reg)
                and base.get("tipo") != "mini_chunk"
                and not comun_e1.chunk_flaggeado(base)
                and d["chunk_id_base"] not in sel_orig):
            ok_bases = False
    check("cada dopada = texto base + EXACTAMENTE una cláusula appendeada",
          ok_texto)
    check("cada dopada difiere de su base SOLO en id y texto", ok_solo_texto)
    check("bases: limpias, sin flags E0, sin mini-chunks, disyuntas de las 40 "
          "del control original", ok_bases)
    sistema_on = prompt_e1.prefijo_sistema(True)
    tool_on_canon = canon(ts_on)
    check("NO SEMBRAR: ninguna cláusula plantada aparece en el system abierto "
          "ni en el tool schema abierto",
          all(d["clausula_plantada"] not in sistema_on
              and d["clausula_plantada"] not in tool_on_canon for d in dop))
    check("…y sí aparece (una vez) en el user message de su propia dopada, y "
          "en NINGÚN otro",
          all(prompt_e1.build_user_message(d["chunk"]).count(d["clausula_plantada"]) == 1
              and all(d["clausula_plantada"] not in prompt_e1.build_user_message(e["chunk"])
                      for e in dop if e is not d)
              for d in dop))

    # ---------------- 4. dopadas fuera de ESQ-1 ------------------------------ #
    print("· dopadas excluidas de todo conteo de ESQ-1")
    check("ids con prefijo reservado dop:: y ausentes del universo de "
          "producción y de E0 enm01",
          all(d["chunk_id_dopado"].startswith("dop::")
              and d["chunk_id_dopado"] not in universo
              and d["chunk_id_dopado"] not in por_id for d in dop))
    check("el jsonl de la re-corrida NO está entre los insumos de producción "
          "(cadenas_esq recibe rutas explícitas; JSONL_PRODUCCION no toca "
          "control/)",
          all("esq/control" not in str(p) for p in cc.JSONL_PRODUCCION)
          and rp.JSONL_P1BIS not in {p.name for p in cc.JSONL_PRODUCCION})

    # ---------------- 5. conteos P1' ----------------------------------------- #
    print("· conteos P1' (umbral compuesto, canal equivocado, D-g)")
    e_tipo = reg_crudo(entities=[{"local_id": "e1", "tipo_propuesto": "X"}])
    e_pred = reg_crudo(relations=[{"predicado_propuesto": "y"}])
    e_nada = reg_crudo(entities=[{"local_id": "e1", "type": "Obligacion"}])
    sel = ([{"chunk_id": f"t{i}", "to": "cap", "brazo": "A'", "mitad": "tipo",
             "espera": "tipo_propuesto", "chunk_id_base": f"bt{i}"} for i in range(5)]
           + [{"chunk_id": f"p{i}", "to": "cap", "brazo": "A'", "mitad": "predicado",
               "espera": "predicado_propuesto", "chunk_id_base": f"bp{i}"} for i in range(5)]
           + [{"chunk_id": f"c{i}", "to": "cap", "brazo": "C"} for i in range(10)])
    # caso 1: 4 tipo + 3 predicado = 7 → pasa
    regs = {f"t{i}": (e_tipo if i < 4 else e_pred) for i in range(5)}
    regs |= {f"p{i}": (e_pred if i < 3 else e_nada) for i in range(5)}
    regs |= {f"c{i}": e_nada for i in range(10)}
    co = rp.conteos_p1bis(sel, regs)
    check("4 tipo + 3 predicado = 7 total y ambas mitades ≥3 → pasa",
          co["A_prime"]["hits_total"] == 7
          and co["A_prime"]["mitad_tipo"]["hits"] == 4
          and co["A_prime"]["mitad_predicado"]["hits"] == 3
          and co["A_prime"]["pasa"] is True)
    check("dopada de tipo que emitió PREDICADO cuenta como otro_canal, no "
          "como hit (t4)",
          co["detalle_por_unidad"]["t4"]["emitio"] == "otro_canal"
          and co["detalle_por_unidad"]["t4"]["hit_esperado"] is False)
    # caso 2: 5 tipo + 2 predicado = 7 total pero mitad predicado < 3 → NO pasa
    regs2 = {f"t{i}": e_tipo for i in range(5)}
    regs2 |= {f"p{i}": (e_pred if i < 2 else e_nada) for i in range(5)}
    regs2 |= {f"c{i}": e_nada for i in range(10)}
    co2 = rp.conteos_p1bis(sel, regs2)
    check("5+2 = 7 total pero mitad predicado 2/5 → NO pasa (un canal muerto "
          "no se esconde detrás del otro)",
          co2["A_prime"]["hits_total"] == 7 and co2["A_prime"]["pasa"] is False)
    # caso 3: error == no-emite (D-g) y C
    regs3 = dict(regs)
    regs3["t0"] = reg_crudo(entities=[{"local_id": "e1", "tipo_propuesto": "X"}],
                            error="max_tokens_hit")
    regs3["c0"] = e_tipo
    regs3["c1"] = e_pred
    del regs3["c9"]
    co3 = rp.conteos_p1bis(sel, regs3)
    check("dopada con error NO cuenta pese a su propuesta (D-g); unidad sin "
          "registro listada en con_error",
          co3["A_prime"]["mitad_tipo"]["hits"] == 3
          and set(co3["con_error"]) == {"t0", "c9"})
    check("C: 1 tipo → pasa; el predicado de c1 se reporta aparte sin umbral",
          co3["C"]["emiten_tipo_propuesto"] == 1 and co3["C"]["pasa"] is True
          and co3["C"]["emiten_algun_propuesto_sin_umbral"] == 2)

    # ---------------- 6. corrida stub end-to-end ----------------------------- #
    print("· corrida stub end-to-end del runner p1bis")
    seleccion = rp.seleccion_p1bis(fx)
    check("selección: 10 A' (orden del fixture) + las 10 C selladas del "
          "control original",
          len(seleccion) == 20
          and [s["chunk_id"] for s in seleccion[:10]]
          == [d["chunk_id_dopado"] for d in dop]
          and [s["chunk_id"] for s in seleccion[10:]]
          == ["cap::1.4.2.1", "cap::5.2.1.3", "cla::2.2.1.7", "cla::4.4",
              "ext::7.6.2::cierre", "ext::7.5.7::intro", "pro::2.3.11",
              "pro::2.4::cierre", "ric::11.1::intro", "ric::8.1.4"])
    por_id_full = rp.por_id_p1bis(fx)
    guardas = rp.verificar_p1bis(fx, por_id_full[seleccion[-1]["chunk_id"]])
    check("guardas del runner p1bis pasan (incluye byte-identidad cerrada y "
          "no-siembra)", all(v is True for k, v in guardas.items()
                             if isinstance(v, bool)))
    d0 = dop[0]["chunk_id_dopado"]
    stub = rc.StubClienteControl({
        d0: {"entities": [{"local_id": "e1", "tipo_propuesto": "Zeta",
                           "label": "x", "punto": dop[0]["chunk"]["unidad"]}],
             "relations": [], "omisiones_no_prosa": []}})
    rp.persistir_orden_p1bis(seleccion, OUT / "orden")
    meta = rc.correr(stub, seleccion, OUT, cc.TOPE_PARCIAL_USD, stub=True,
                     por_id=por_id_full, jsonl_nombre=rp.JSONL_P1BIS)
    lineas = (OUT / rp.JSONL_P1BIS).read_text(encoding="utf-8").strip().split("\n")
    check("la corrida stub persiste 20 líneas sin freno",
          len(lineas) == 20 and meta["frenado"] is None and stub.llamadas == 20)
    check("las 20 requests llevan el prefijo abierto NUEVO (system == "
          "prefijo abierto; tool con description corregida)",
          len(stub.requests) == 20 and all(
              k["system"][0]["text"] == prompt_e1.prefijo_sistema(True)
              and k["tools"][0]["description"] == desc_on
              for k in stub.requests))
    check("el texto dopado (con su cláusula) viaja en el user message de la "
          "request de su unidad",
          dop[0]["clausula_plantada"] in stub.requests[0]["messages"][0]["content"])
    claves_prod = ["chunk_id", "unidad", "tipo_unidad", "titulo", "stop_reason",
                   "error", "usage", "tool_input_crudo", "validacion"]
    check("cada línea tiene EXACTAMENTE las claves de producción",
          all(list(json.loads(x).keys()) == claves_prod for x in lineas))
    check("la validación persistida corre con canal_abierto=True (la "
          "propuesta enlatada de la primera dopada no es type_invalido)",
          not any(r["motivo"] == "type_invalido"
                  for x in lineas if json.loads(x)["chunk_id"] == d0
                  for r in (json.loads(x)["validacion"] or {}).get("rechazos", [])))
    stub2 = rc.StubClienteControl()
    rc.correr(stub2, seleccion, OUT, cc.TOPE_PARCIAL_USD, stub=True,
              por_id=por_id_full, jsonl_nombre=rp.JSONL_P1BIS)
    check("reanudación idempotente: segunda corrida no llama ni escribe nada",
          stub2.llamadas == 0
          and len((OUT / rp.JSONL_P1BIS).read_text(encoding="utf-8")
                  .strip().split("\n")) == 20)
    resumen = rp.resumen_p1bis(seleccion, OUT, stub.resumen(), meta, guardas)
    check("resumen stub: A' 1/10 (1 tipo, 0 predicado) → no pasa; C 0/10 → pasa",
          resumen["conteos_P1bis"]["A_prime"]["hits_total"] == 1
          and resumen["conteos_P1bis"]["A_prime"]["pasa"] is False
          and resumen["conteos_P1bis"]["C"]["pasa"] is True
          and resumen["costo_recomputado_desde_usage_usd"] == 0.0)

    # ---------------- 7. anclas ---------------------------------------------- #
    print("· anclas")
    txt_adenda = (cc.UNIDAD_DIR / "adenda_prerregistro_esq1_P1bis.md").read_text(
        encoding="utf-8")
    check("umbrales transcriptos == adenda sellada (≥7 de 10, ≥3 de 5 por "
          "mitad, C ≤1 de 10)",
          "≥7 de 10 en total, y ≥3 de 5 en cada mitad" in txt_adenda
          and "≤1 de 10" in txt_adenda
          and (rp.UMBRAL_APRIME_TOTAL, rp.UMBRAL_APRIME_MITAD, rp.UMBRAL_C)
          == (7, 3, 1))
    check("tope parcial 0,50 (mandato) y db propia p1bis (la del control "
          "original no se toca)",
          cc.TOPE_PARCIAL_USD == 0.50
          and rp.DB_P1BIS.name == "esq_control_p1bis.db"
          and rp.DB_P1BIS != rc.DB_CONTROL)
    k_off = lc.compute_key(cliente_e1.namespace_e1(False), lc.canonical_request(
        prompt_e1.build_request_kwargs(por_id_full[seleccion[-1]["chunk_id"]],
                                       model="M")))
    k_on = lc.compute_key(ns_on, lc.canonical_request(
        prompt_e1.build_request_kwargs(por_id_full[seleccion[-1]["chunk_id"]],
                                       model="M", canal_abierto=True)))
    check("keys de caché on/off distintas para la misma unidad", k_off != k_on)

    passed = sum(ok for _, ok in _checks)
    print(f"\n  {passed}/{len(_checks)} checks OK")
    print("  RESULTADO:", "PASS" if passed == len(_checks) else "FAIL")
    return 0 if passed == len(_checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
