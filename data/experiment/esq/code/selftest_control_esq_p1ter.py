"""
selftest_control_esq_p1ter.py — SELFTEST OFFLINE previo al gasto de la
re-corrida P1″ del control (U-ESQ-1e.b). USD 0, sin API; escribe solo en
selftest_out/ (gitignorado).

Cubre lo exigido por el mandato:
  0. UNA SOLA VARIABLE (adenda P1″ §1/§5.a) — fixtures dopadas_p1bis.json
     byte-idénticos por sha256 al valor sellado en c25273f; los dos textos de
     reemplazo del código verbatim contra los blockquotes de la adenda; el
     system abierto de P1′ reconstruido ancla a su hash sellado
     (d923bf876580, no circular); el system abierto P1″ == P1′ con
     EXACTAMENTE los dos reemplazos y nada más; description y tool schema
     abiertos sin cambio. Imprime el diff unificado completo P1′ → P1″.
  1. GUARDAS DEL PREFIJO NUEVO — hash recalculado tras la neutralización
     (== cc.PREFIJO_HASH_ABIERTO_ESPERADO, != P1′, != control original,
     != producción), namespace particionado nuevo.
  2. BYTE-IDENTIDAD DEL MODO CERRADO — sha256 completos contra los candados
     sellados pre-edición, namespace cerrado de producción, mismo objeto.
  3. FIXTURES DOPADAS — mismas invariantes que en U-ESQ-1d (10 = 5+5, texto
     base + una cláusula, cláusulas NO sembradas en el system P1″ ni el tool).
  4. DOPADAS EXCLUIDAS DE TODO CONTEO DE ESQ-1.
  5. CONTEOS P1″ (== P1′) — umbral compuesto, cruce de canal como
     otro_canal, D-g.
  6. CORRIDA STUB END-TO-END del runner p1ter — 20 unidades con el prefijo
     P1″, reanudación idempotente, claves de producción, comparación pareada
     presente en el resumen.
  7. ANCLAS — umbrales == adenda sellada, tope 0,50, db propia, keys de
     caché p1ter distintas de p1bis y de producción.

Uso:  .venv/bin/python3 -B data/experiment/esq/code/selftest_control_esq_p1ter.py
"""

from __future__ import annotations

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
import runner_control_esq_p1ter as rt      # noqa: E402
import comun_e1                            # noqa: E402
import prompt_e1                           # noqa: E402
import cliente_e1                          # noqa: E402
import llm_cache as lc                     # noqa: E402

OUT = cc.SELFTEST_DIR / "control_stub_p1ter"

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
    print("== selftest_control_esq_p1ter (offline, $0) ==\n")
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    # ---------------- 0. una sola variable ---------------------------------- #
    print("· UNA SOLA VARIABLE (adenda P1'' §1/§5.a)")
    check("fixtures dopadas_p1bis.json sha256 == valor sellado en c25273f "
          f"({rt.SHA256_DOPADAS_C25273F[:16]}…)",
          sha(rp.FIXTURES.read_text(encoding="utf-8"))
          == rt.SHA256_DOPADAS_C25273F)
    ad_i, ad_ii = rt.cierres_de_adenda()
    check("texto (i) del código verbatim == blockquote (i) de la adenda",
          prompt_e1.CIERRE_CATALOGO_ABIERTO == ad_i)
    check("texto (ii) del código verbatim == blockquote (ii) de la adenda",
          prompt_e1.CIERRE_REGLA4_ABIERTO == ad_ii)
    check("system abierto P1' reconstruido ancla a su hash SELLADO "
          "d923bf876580 (la base del diff no es circular)",
          rt.hash_prefijo_p1bis_reconstruido() == cc.PREFIJO_HASH_ABIERTO_P1BIS)
    uv = rt.verificar_una_variable()
    check("verificar_una_variable() en PASS completo "
          f"({sum(uv.values())}/{len(uv)} sub-checks)", all(uv.values()))
    for k, v in uv.items():
        print(f"      - {k}: {'PASS' if v else 'FAIL'}")
    print("\n--- diff unificado system abierto P1' -> P1'' (completo) ---")
    print(rt.diff_system_abierto())
    print("--- fin diff ---\n")

    # ---------------- 1. guardas del prefijo nuevo -------------------------- #
    print("· guardas del prefijo nuevo (cierres neutralizados)")
    check("hash abierto recalculado == cc.PREFIJO_HASH_ABIERTO_ESPERADO",
          prompt_e1.PREFIJO_HASH_CANAL_ABIERTO == cc.PREFIJO_HASH_ABIERTO_ESPERADO)
    check("hash abierto NUEVO != P1' (d923bf876580), != control original "
          "(bca492bbf7c8), != producción",
          prompt_e1.PREFIJO_HASH_CANAL_ABIERTO not in (
              cc.PREFIJO_HASH_ABIERTO_P1BIS,
              cc.PREFIJO_HASH_ABIERTO_CONTROL_ORIGINAL,
              prompt_e1.PREFIJO_HASH))
    ns_on = cliente_e1.namespace_e1(canal_abierto=True)
    check("namespace abierto porta el hash nuevo y NINGUNO de los dos viejos "
          "(partición: P1'' jamás relee la caché de P1' ni del original)",
          f"p{cc.PREFIJO_HASH_ABIERTO_ESPERADO}" in ns_on
          and cc.PREFIJO_HASH_ABIERTO_P1BIS not in ns_on
          and cc.PREFIJO_HASH_ABIERTO_CONTROL_ORIGINAL not in ns_on)
    ts_on = prompt_e1.tool_schema_e1(canal_abierto=True)
    props_e = ts_on["input_schema"]["properties"]["entities"]["items"]["properties"]
    props_r = ts_on["input_schema"]["properties"]["relations"]["items"]["properties"]
    check("schema abierto declara tipo_propuesto y predicado_propuesto",
          "tipo_propuesto" in props_e and "predicado_propuesto" in props_r)
    check("enums del tool abierto intactos (6 types, 12 predicates)",
          len(props_e["type"]["enum"]) == 6
          and len(props_r["predicate"]["enum"]) == 12)
    sistema_on = prompt_e1.prefijo_sistema(True)
    check("no sembrar: los textos nuevos de la adenda no traen valores de "
          "ejemplo de tipos/predicados fuera de los enums",
          not any(x in prompt_e1.CIERRE_CATALOGO_ABIERTO
                  + prompt_e1.CIERRE_REGLA4_ABIERTO for x in
                  ("Sancion", "Presuncion", "Definicion", "Vigencia",
                   "Facultad", "equivale", "asimila", "complementa",
                   "acredita", "computa_conjuntamente")))

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
    check("prefijo_sistema(False) devuelve PREFIJO_SISTEMA sin transformación "
          "(los cierres de producción siguen presentes en el cerrado)",
          prompt_e1.prefijo_sistema(False) is prompt_e1.PREFIJO_SISTEMA
          and prompt_e1.CIERRE_CATALOGO_PROD in prompt_e1.PREFIJO_SISTEMA
          and prompt_e1.CIERRE_REGLA4_PROD in prompt_e1.PREFIJO_SISTEMA)

    # ---------------- 3. fixtures dopadas ----------------------------------- #
    print("· fixtures dopadas (aprobación vigente por sha; invariantes U-ESQ-1d)")
    fx = rp.cargar_fixtures()
    dop = fx["dopadas"]
    check("10 dopadas = 5 tipo + 5 predicado, 2 por TO",
          len(dop) == 10
          and sum(1 for d in dop if d["mitad"] == "tipo") == 5
          and all(sum(1 for d in dop if d["to"] == t) == 2 for t in cc.TOS))
    check("aprobado_por_autora sigue true en el fixture sellado",
          fx.get("aprobado_por_autora") is True)
    tool_on_canon = canon(ts_on)
    check("NO SEMBRAR: ninguna cláusula plantada aparece en el system P1'' "
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
    universo = cc.cargar_universo()
    por_id = rc.chunks_por_id()
    check("ids con prefijo reservado dop:: y ausentes del universo de "
          "producción y de E0 enm01",
          all(d["chunk_id_dopado"].startswith("dop::")
              and d["chunk_id_dopado"] not in universo
              and d["chunk_id_dopado"] not in por_id for d in dop))
    check("el jsonl de P1'' NO está entre los insumos de producción",
          all("esq/control" not in str(p) for p in cc.JSONL_PRODUCCION)
          and rt.JSONL_P1TER not in {p.name for p in cc.JSONL_PRODUCCION})

    # ---------------- 5. conteos P1'' (== P1') ------------------------------- #
    print("· conteos P1'' (umbral compuesto heredado, cruce de canal, D-g)")
    e_tipo = reg_crudo(entities=[{"local_id": "e1", "tipo_propuesto": "X"}])
    e_pred = reg_crudo(relations=[{"predicado_propuesto": "y"}])
    e_nada = reg_crudo(entities=[{"local_id": "e1", "type": "Obligacion"}])
    sel = ([{"chunk_id": f"t{i}", "to": "cap", "brazo": "A'", "mitad": "tipo",
             "espera": "tipo_propuesto", "chunk_id_base": f"bt{i}"} for i in range(5)]
           + [{"chunk_id": f"p{i}", "to": "cap", "brazo": "A'", "mitad": "predicado",
               "espera": "predicado_propuesto", "chunk_id_base": f"bp{i}"} for i in range(5)]
           + [{"chunk_id": f"c{i}", "to": "cap", "brazo": "C"} for i in range(10)])
    regs = {f"t{i}": (e_tipo if i < 4 else e_pred) for i in range(5)}
    regs |= {f"p{i}": (e_pred if i < 3 else e_nada) for i in range(5)}
    regs |= {f"c{i}": e_nada for i in range(10)}
    co = rp.conteos_p1bis(sel, regs)
    check("4 tipo + 3 predicado = 7 total y ambas mitades ≥3 → pasa",
          co["A_prime"]["hits_total"] == 7 and co["A_prime"]["pasa"] is True)
    check("dopada de tipo que emitió PREDICADO cuenta como otro_canal (cruce "
          "reportado, no esperado)",
          co["detalle_por_unidad"]["t4"]["emitio"] == "otro_canal"
          and co["detalle_por_unidad"]["t4"]["hit_esperado"] is False)
    regs2 = {f"t{i}": e_tipo for i in range(5)}
    regs2 |= {f"p{i}": (e_pred if i < 2 else e_nada) for i in range(5)}
    regs2 |= {f"c{i}": e_nada for i in range(10)}
    co2 = rp.conteos_p1bis(sel, regs2)
    check("5+2 = 7 total pero mitad predicado 2/5 → NO pasa",
          co2["A_prime"]["hits_total"] == 7 and co2["A_prime"]["pasa"] is False)
    regs3 = dict(regs)
    regs3["t0"] = reg_crudo(entities=[{"local_id": "e1", "tipo_propuesto": "X"}],
                            error="max_tokens_hit")
    co3 = rp.conteos_p1bis(sel, regs3)
    check("dopada con error NO cuenta pese a su propuesta (D-g)",
          co3["A_prime"]["mitad_tipo"]["hits"] == 3
          and "t0" in co3["con_error"])

    # ---------------- 6. corrida stub end-to-end ----------------------------- #
    print("· corrida stub end-to-end del runner p1ter")
    seleccion = rp.seleccion_p1bis(fx)
    check("selección IDÉNTICA a la de P1' (misma función, mismos fixtures): "
          "10 A' + las 10 C selladas",
          len(seleccion) == 20
          and seleccion == json.loads(
              (cc.ORDEN_DIR / rp.ORDEN_P1BIS).read_text(encoding="utf-8"))["seleccion"])
    por_id_full = rp.por_id_p1bis(fx)
    guardas = rt.verificar_p1ter(fx, por_id_full[seleccion[-1]["chunk_id"]])
    check("guardas del runner p1ter pasan (incluye una_sola_variable)",
          all(v is True for k, v in guardas.items() if isinstance(v, bool))
          and all(guardas["una_sola_variable"].values()))
    d0 = dop[0]["chunk_id_dopado"]
    stub = rc.StubClienteControl({
        d0: {"entities": [{"local_id": "e1", "tipo_propuesto": "Zeta",
                           "label": "x", "punto": dop[0]["chunk"]["unidad"]}],
             "relations": [], "omisiones_no_prosa": []}})
    rt.persistir_orden_p1ter(seleccion, OUT / "orden")
    meta = rc.correr(stub, seleccion, OUT, cc.TOPE_PARCIAL_USD, stub=True,
                     por_id=por_id_full, jsonl_nombre=rt.JSONL_P1TER)
    lineas = (OUT / rt.JSONL_P1TER).read_text(encoding="utf-8").strip().split("\n")
    check("la corrida stub persiste 20 líneas sin freno",
          len(lineas) == 20 and meta["frenado"] is None and stub.llamadas == 20)
    check("las 20 requests llevan el system P1'' (cierres neutralizados) y "
          "la description de P1' sin cambio",
          len(stub.requests) == 20 and all(
              k["system"][0]["text"] == sistema_on
              and prompt_e1.CIERRE_CATALOGO_ABIERTO in k["system"][0]["text"]
              and prompt_e1.CIERRE_REGLA4_ABIERTO in k["system"][0]["text"]
              and prompt_e1.CIERRE_CATALOGO_PROD not in k["system"][0]["text"]
              and prompt_e1.CIERRE_REGLA4_PROD not in k["system"][0]["text"]
              and k["tools"][0]["description"]
              == prompt_e1.TOOL_SCHEMA_E1_CANAL_ABIERTO["description"]
              for k in stub.requests))
    check("el texto dopado (con su cláusula) viaja en el user message de la "
          "request de su unidad",
          dop[0]["clausula_plantada"] in stub.requests[0]["messages"][0]["content"])
    claves_prod = ["chunk_id", "unidad", "tipo_unidad", "titulo", "stop_reason",
                   "error", "usage", "tool_input_crudo", "validacion"]
    check("cada línea tiene EXACTAMENTE las claves de producción",
          all(list(json.loads(x).keys()) == claves_prod for x in lineas))
    check("la validación persistida corre con canal_abierto=True",
          not any(r["motivo"] == "type_invalido"
                  for x in lineas if json.loads(x)["chunk_id"] == d0
                  for r in (json.loads(x)["validacion"] or {}).get("rechazos", [])))
    stub2 = rc.StubClienteControl()
    rc.correr(stub2, seleccion, OUT, cc.TOPE_PARCIAL_USD, stub=True,
              por_id=por_id_full, jsonl_nombre=rt.JSONL_P1TER)
    check("reanudación idempotente: segunda corrida no llama ni escribe nada",
          stub2.llamadas == 0
          and len((OUT / rt.JSONL_P1TER).read_text(encoding="utf-8")
                  .strip().split("\n")) == 20)
    resumen = rt.resumen_p1ter(seleccion, OUT, stub.resumen(), meta, guardas)
    check("resumen stub: A' 1/10 (1 tipo, 0 predicado) → no pasa; C 0/10 → "
          "pasa; costo 0",
          resumen["conteos_P1ter"]["A_prime"]["hits_total"] == 1
          and resumen["conteos_P1ter"]["A_prime"]["pasa"] is False
          and resumen["conteos_P1ter"]["C"]["pasa"] is True
          and resumen["costo_recomputado_desde_usage_usd"] == 0.0)
    par = resumen["comparacion_pareada_P1bis"]
    check("comparación pareada contra P1' presente: 20 unidades, conteos P1' "
          "recomputados de su jsonl (A' 0, C 0), y la dopada stub marca cambio "
          "nada → esperado",
          len(par["por_unidad"]) == 20
          and par["conteos_p1bis_recomputados"]["A_prime_hits_total"] == 0
          and par["conteos_p1bis_recomputados"]["C_emiten_tipo_propuesto"] == 0
          and par["por_unidad"][d0]["p1bis_emitio"] == "nada"
          and par["por_unidad"][d0]["p1ter_emitio"] == "esperado"
          and par["por_unidad"][d0]["cambio"] is True)
    check("el diff P1'->P1'' viaja en el resumen (evidencia persistida)",
          "TIPOS DE ENTIDAD DEL CATÁLOGO (6)"
          in resumen["diff_system_abierto_p1bis_a_p1ter"])

    # ---------------- 7. anclas ---------------------------------------------- #
    print("· anclas")
    txt_adenda = rt.ADENDA_P1TER.read_text(encoding="utf-8")
    check("adenda P1'' FIRMADA y con umbrales idénticos a P1' (≥7/10, ≥3/5 "
          "por mitad, C ≤1/10) — transcripción == constantes",
          "Estado: FIRMADO" in txt_adenda
          and "≥7/10 en total y ≥3/5 en cada mitad" in txt_adenda
          and "C: ≤1/10" in txt_adenda
          and (rt.UMBRAL_APRIME_TOTAL, rt.UMBRAL_APRIME_MITAD, rt.UMBRAL_C)
          == (7, 3, 1))
    check("tope parcial 0,50 (mandato) y db propia p1ter (las de U-ESQ-1c y "
          "U-ESQ-1d no se tocan)",
          cc.TOPE_PARCIAL_USD == 0.50
          and rt.DB_P1TER.name == "esq_control_p1ter.db"
          and rt.DB_P1TER != rp.DB_P1BIS and rt.DB_P1TER != rc.DB_CONTROL)
    ch = por_id_full[seleccion[-1]["chunk_id"]]
    k_off = lc.compute_key(cliente_e1.namespace_e1(False), lc.canonical_request(
        prompt_e1.build_request_kwargs(ch, model="M")))
    k_on = lc.compute_key(ns_on, lc.canonical_request(
        prompt_e1.build_request_kwargs(ch, model="M", canal_abierto=True)))
    ns_p1bis = lc.make_namespace(
        cliente_e1.DOMAIN,
        code_ver=f"{cliente_e1.CODE_VER}-p{cc.PREFIJO_HASH_ABIERTO_P1BIS}",
        thinking=False)
    check("keys de caché: abierta P1'' != cerrada, y namespace P1'' != "
          "namespace P1' (partición efectiva)",
          k_off != k_on and ns_on != ns_p1bis)

    passed = sum(ok for _, ok in _checks)
    print(f"\n  {passed}/{len(_checks)} checks OK")
    print("  RESULTADO:", "PASS" if passed == len(_checks) else "FAIL")
    return 0 if passed == len(_checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
