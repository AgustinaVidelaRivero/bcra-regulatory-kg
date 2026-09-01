"""
selftest_descubrimiento_cal.py — SELFTEST OFFLINE previo al gasto de la
calibración del instrumento de descubrimiento (U-ESQ-2-cal.b). USD 0, sin
API; escribe solo en selftest_out/ (gitignorado).

Cubre lo exigido por el mandato:
  1. PRE-REGISTRO Y VARA — pre-registro FIRMADO; fixtures dopadas_p1bis.json
     byte-idénticos por sha256 al valor sellado en c25273f (cero cambios,
     aprobación vigente); tope parcial 0,50.
  2. NO SEMBRAR (mecánico contra el manifiesto de dopadas) — ninguna cláusula
     plantada NI concepto plantado aparece en el contrato del instrumento;
     marcadores de los 10 conceptos ausentes del contrato normalizado; la
     plantilla fija del user message tampoco siembra; cada cláusula viaja
     SOLO en el user message de su propia dopada.
  3. EL INSTRUMENTO NO EXTRAE — el contrato no contiene los canales ni el
     vocabulario del extractor (tool de extracción, campos propuestos,
     entities/relations/local_id); pide describir y justificar, con lista
     vacía como resultado válido; los 6 tipos y 12 predicados transcriptos
     coinciden con schema.py (verificado desde afuera: el módulo es puro).
  4. PRODUCCIÓN INTACTA POR DISEÑO — descubrimiento_cal importa CERO módulos
     del pipeline (verificado en subproceso limpio); candados byte-idénticos
     de producción (prefijo, tool schema, namespace) intactos tras importar
     todo el código nuevo.
  5. NAMESPACE Y CACHÉ PROPIOS — dominio nuevo, sin colisión con los tres
     namespaces de la escalera ni con producción; .db propia.
  6. PARSER — fixtures sintéticos: salida vacía OK, hallazgos múltiples OK,
     malformadas (no-dict, sin clave, contenedor no-lista, campo faltante,
     campo vacío) levantan SalidaMalformada; en la corrida la malformada se
     persiste con error y main sale con EXIT 2 (jamás salteo silencioso).
  7. GATE DEL FRENO (a) — el runner se niega sin manifiesto APROBADO o con
     sha desactualizado.
  8. CORRIDA STUB END-TO-END — 20 unidades (vara sellada), reanudación
     idempotente, conteo mecánico sin veredicto P-cal, exit codes 0/2/3.

Uso:  .venv/bin/python3 -B data/experiment/esq/code/selftest_descubrimiento_cal.py
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_control_esq as cc             # noqa: E402
import runner_control_esq as rc            # noqa: E402
import runner_control_esq_p1bis as rp      # noqa: E402
import runner_control_esq_p1ter as rt      # noqa: E402
import descubrimiento_cal as dc            # noqa: E402
import runner_descubrimiento_cal as rd     # noqa: E402
import prompt_e1                           # noqa: E402
import cliente_e1                          # noqa: E402
import schema                              # noqa: E402  (fuente única del esquema v2)

OUT = cc.SELFTEST_DIR / "descubrimiento_cal_stub"

_checks = []


def check(nombre, cond):
    _checks.append((nombre, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {nombre}")


def canon(o):
    return json.dumps(o, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":"))


def main() -> int:
    print("== selftest_descubrimiento_cal (offline, $0) ==\n")
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    # ---------------- 1. pre-registro y vara -------------------------------- #
    print("· pre-registro y vara (sellados, cero cambios)")
    prer = (cc.UNIDAD_DIR / "prerregistro_descubrimiento_cal.md").read_text(
        encoding="utf-8")
    check("pre-registro FIRMADO y con la vara declarada (A' >=7/10 y >=3/5 "
          "por mitad; C <=1/10)",
          "FIRMADO" in prer and "≥7 de 10" in prer and "≥3 de 5" in prer
          and "≤1 de 10" in prer)
    check("fixtures dopadas_p1bis.json sha256 == valor sellado en c25273f "
          f"({rt.SHA256_DOPADAS_C25273F[:16]}…)",
          rd._sha(rp.FIXTURES.read_text(encoding="utf-8"))
          == rt.SHA256_DOPADAS_C25273F)
    fx = rp.cargar_fixtures()
    dop = fx["dopadas"]
    check("10 dopadas = 5 tipo + 5 predicado; aprobado_por_autora true",
          len(dop) == 10
          and sum(1 for d in dop if d["mitad"] == "tipo") == 5
          and fx.get("aprobado_por_autora") is True)
    check("tope parcial 0,50 (mandato, gasto solo en fase c)",
          cc.TOPE_PARCIAL_USD == 0.50)

    # ---------------- 2. no sembrar (mecánico) ------------------------------- #
    print("· no sembrar (verificación mecánica contra el manifiesto de dopadas)")
    contrato = dc.CONTRATO_CANONICO_DESC
    contrato_norm = rd._norm(contrato)
    conceptos = rd.conceptos_del_manifiesto()
    check("10 conceptos plantados parseados del manifiesto de dopadas",
          len(conceptos) == 10
          and set(conceptos) == {d["chunk_id_dopado"] for d in dop})
    check("ninguna CLÁUSULA plantada aparece en el contrato del instrumento",
          all(d["clausula_plantada"] not in contrato for d in dop))
    check("ningún CONCEPTO plantado (verbatim) aparece en el contrato",
          all(c not in contrato for c in conceptos.values()))
    check("ningún marcador de concepto aparece en el contrato normalizado "
          f"({len(rd.MARCADORES_CONCEPTOS)} marcadores)",
          all(m not in contrato_norm for m in rd.MARCADORES_CONCEPTOS))
    chunk_dummy = {"archivo": "x.pdf", "to": "cap", "unidad": "1.1",
                   "titulo": "t", "tipo": "punto", "texto": "TEXTO_NEUTRO",
                   "herencia": [], "flags": {}}
    msg_dummy = dc.build_user_message_descubrimiento(chunk_dummy)
    plantilla = msg_dummy.replace("TEXTO_NEUTRO", "")
    plantilla_norm = rd._norm(plantilla)
    check("la plantilla fija del user message tampoco siembra (cláusulas, "
          "conceptos y marcadores ausentes)",
          all(d["clausula_plantada"] not in plantilla for d in dop)
          and all(c not in plantilla for c in conceptos.values())
          and all(m not in plantilla_norm for m in rd.MARCADORES_CONCEPTOS))
    check("cada cláusula plantada viaja EXACTAMENTE una vez en el user "
          "message de su propia dopada y en NINGÚN otro",
          all(dc.build_user_message_descubrimiento(d["chunk"])
              .count(d["clausula_plantada"]) == 1
              and all(d["clausula_plantada"]
                      not in dc.build_user_message_descubrimiento(e["chunk"])
                      for e in dop if e is not d)
              for d in dop))

    # ---------------- 3. el instrumento no extrae ---------------------------- #
    print("· el instrumento pregunta, no extrae")
    check("el contrato NO contiene los canales/vocabulario del extractor "
          "(extraer_kg_e1, tipo_propuesto, predicado_propuesto, "
          "sujeto_propuesto, entities, relations, local_id)",
          all(x not in contrato for x in
              ("extraer_kg_e1", "tipo_propuesto", "predicado_propuesto",
               "sujeto_propuesto", '"entities"', '"relations"', "local_id")))
    check("la tarea pide describir + justificar y declara la lista vacía "
          "como resultado válido",
          "NO extraigas" in dc.PREFIJO_DESCUBRIMIENTO
          and "NO propongas nombres" in dc.PREFIJO_DESCUBRIMIENTO
          and "lista VACÍA" in dc.PREFIJO_DESCUBRIMIENTO
          and "por_que_no_encaja" in dc.PREFIJO_DESCUBRIMIENTO)
    check("tool schema: SOLO 'hallazgos', items con exactamente "
          "descripcion + por_que_no_encaja requeridos, sin extras",
          list(dc.TOOL_DESCUBRIMIENTO["input_schema"]["properties"])
          == ["hallazgos"]
          and dc.TOOL_DESCUBRIMIENTO["input_schema"]["required"] == ["hallazgos"]
          and dc.TOOL_DESCUBRIMIENTO["input_schema"]["properties"]["hallazgos"]
          ["items"]["required"] == ["descripcion", "por_que_no_encaja"]
          and dc.TOOL_DESCUBRIMIENTO["input_schema"]["properties"]["hallazgos"]
          ["items"]["additionalProperties"] is False)
    check("los 6 tipos transcriptos == schema.ENTITY_TYPES y los 12 "
          "predicados == schema.PREDICATES (fuente única, verificado desde "
          "afuera del módulo puro)",
          set(dc.TIPOS_6) == set(schema.ENTITY_TYPES)
          and len(dc.TIPOS_6) == len(schema.ENTITY_TYPES) == 6
          and set(dc.PREDICADOS_12) == set(schema.PREDICATES)
          and len(dc.PREDICADOS_12) == len(schema.PREDICATES) == 12)
    check("cada tipo y cada predicado aparece en el texto del system (la "
          "referencia está completa)",
          all(t in dc.PREFIJO_DESCUBRIMIENTO for t in dc.TIPOS_6)
          and all(p in dc.PREFIJO_DESCUBRIMIENTO for p in dc.PREDICADOS_12))
    check("modelo del instrumento == modelo del extractor (el censo correría "
          "con él) y tarifas ancladas",
          dc.MODEL_DESC == cc.MODEL_E1)

    # ---------------- 4. producción intacta por diseño ----------------------- #
    print("· producción intacta por diseño")
    codigo = ("import sys; sys.path.insert(0, r'" + str(CODE_DIR) + "'); "
              "import descubrimiento_cal; "
              "prohibidos = {'prompt_e1', 'cliente_e1', 'validador_e1', "
              "'comun_e1', 'schema', 'llm_cache', 'anthropic'}; "
              "cargados = prohibidos & set(sys.modules); "
              "print('CARGADOS:' + ','.join(sorted(cargados)))")
    res = subprocess.run([sys.executable, "-c", codigo],
                         capture_output=True, text=True)
    check("descubrimiento_cal es PURO: en subproceso limpio no carga ningún "
          "módulo del pipeline (cero imports que modifiquen producción)",
          res.returncode == 0 and res.stdout.strip() == "CARGADOS:")
    check("candados de producción intactos tras importar todo el código "
          "nuevo: sha prefijo cerrado, sha tool schema cerrado, namespace "
          "cerrado",
          rd._sha(prompt_e1.PREFIJO_CANONICO) == rp.SHA256_PREFIJO_PROD
          and rd._sha(canon(prompt_e1.TOOL_SCHEMA_E1)) == rp.SHA256_TOOL_SCHEMA_PROD
          and cliente_e1.namespace_e1(False) == rp.NAMESPACE_PROD)

    # ---------------- 5. namespace y caché propios --------------------------- #
    print("· namespace y caché propios (sin colisión)")
    ns = rd.namespace_descubrimiento()
    ns_escalera = [
        f"p{h}" for h in (cc.PREFIJO_HASH_ABIERTO_CONTROL_ORIGINAL,
                          cc.PREFIJO_HASH_ABIERTO_P1BIS,
                          cc.PREFIJO_HASH_ABIERTO_ESPERADO)]
    check("namespace propio: dominio esq_descubrimiento_cal, porta el hash "
          "del contrato y NINGÚN hash de la escalera ni el de producción",
          ns.startswith("esq_descubrimiento_cal|")
          and f"p{dc.PREFIJO_HASH_DESC}" in ns
          and all(x not in ns for x in ns_escalera)
          and "4793d6152608" not in ns and ns != rp.NAMESPACE_PROD)
    check("db propia esq_descubrimiento_cal.db (las de la escalera no se "
          "tocan)",
          rd.DB_DESC.name == "esq_descubrimiento_cal.db"
          and rd.DB_DESC not in (rc.DB_CONTROL, rp.DB_P1BIS, rt.DB_P1TER))
    check("jsonl del descubrimiento NO está entre los insumos de producción",
          all("esq/control" not in str(p) for p in cc.JSONL_PRODUCCION)
          and rd.JSONL_DESC not in {p.name for p in cc.JSONL_PRODUCCION})

    # ---------------- 6. parser ---------------------------------------------- #
    print("· parser (fixtures sintéticos)")
    check("salida vacía: hallazgos=[] parsea a lista vacía (resultado válido)",
          dc.parsear_descubrimiento({"hallazgos": []}) == [])
    multi = {"hallazgos": [
        {"descripcion": "d1", "por_que_no_encaja": "p1"},
        {"descripcion": "d2", "por_que_no_encaja": "p2"}]}
    check("salida con hallazgos múltiples: parsea 2 con ambos campos",
          dc.parsear_descubrimiento(multi) == multi["hallazgos"])

    def _malformada(ti):
        try:
            dc.parsear_descubrimiento(ti)
            return False
        except dc.SalidaMalformada:
            return True

    check("malformadas levantan SalidaMalformada: no-dict, sin clave, "
          "contenedor no-lista, item no-dict, campo faltante, campo vacío",
          _malformada(None) and _malformada([])
          and _malformada({}) and _malformada({"hallazgos": "x"})
          and _malformada({"hallazgos": ["x"]})
          and _malformada({"hallazgos": [{"descripcion": "d"}]})
          and _malformada({"hallazgos": [{"descripcion": "",
                                          "por_que_no_encaja": "p"}]}))

    # ---------------- 7. gate del freno (a) ---------------------------------- #
    print("· gate del freno (a): manifiesto del prompt")
    man_pend = OUT / "manifiesto_pendiente.md"
    man_pend.write_text(dc.render_manifiesto(), encoding="utf-8")
    g1 = rd.manifiesto_prompt_aprobado(man_pend)
    check("manifiesto recién generado: existe, sha coincide, NO aprobado "
          "(el runner se negaría a gastar)",
          g1["existe"] and g1["sha_coincide"] and not g1["aprobado"])
    man_ok = OUT / "manifiesto_aprobado.md"
    man_ok.write_text(dc.render_manifiesto().replace(
        "Estado: PENDIENTE DE APROBACIÓN", "Estado: APROBADO"),
        encoding="utf-8")
    g2 = rd.manifiesto_prompt_aprobado(man_ok)
    check("manifiesto con Estado: APROBADO y sha vigente: gate abre",
          g2["existe"] and g2["aprobado"] and g2["sha_coincide"])
    man_stale = OUT / "manifiesto_stale.md"
    man_stale.write_text(man_ok.read_text(encoding="utf-8").replace(
        dc.SHA256_CONTRATO_DESC, "0" * 64), encoding="utf-8")
    g3 = rd.manifiesto_prompt_aprobado(man_stale)
    check("manifiesto aprobado pero con sha VIEJO: gate cierra (editar el "
          "instrumento invalida la aprobación)",
          g3["aprobado"] and not g3["sha_coincide"])
    check("gate ausente: cierra",
          not rd.manifiesto_prompt_aprobado(OUT / "no_existe.md")["existe"])

    # ---------------- 8. guardas + corrida stub end-to-end -------------------- #
    print("· guardas + corrida stub end-to-end")
    guardas = rd.verificar_descubrimiento(fx)
    check("verificar_descubrimiento() en PASS completo "
          f"({sum(guardas['checks'].values())}/{len(guardas['checks'])} "
          "sub-checks)", all(guardas["checks"].values()))
    for k, v in guardas["checks"].items():
        print(f"      - {k}: {'PASS' if v else 'FAIL'}")

    seleccion = rp.seleccion_p1bis(fx)
    check("selección == vara sellada de P1' (mismas 20 unidades, mismo "
          "orden): 10 A' + las 10 C selladas",
          len(seleccion) == 20
          and seleccion == json.loads(
              (cc.ORDEN_DIR / rp.ORDEN_P1BIS).read_text(encoding="utf-8"))
          ["seleccion"])
    por_id = rp.por_id_p1bis(fx)
    rd.persistir_orden_descubrimiento(seleccion, OUT / "orden")

    d0 = dop[0]["chunk_id_dopado"]
    c_mal = seleccion[-1]["chunk_id"]   # una C con salida malformada
    stub = rd.StubClienteDescubrimiento({
        d0: {"hallazgos": [{"descripcion": "hallazgo de prueba",
                            "por_que_no_encaja": "razón de prueba"}]},
        c_mal: {"hallazgos": "no-una-lista"},
    })
    meta = rd.correr_descubrimiento(stub, seleccion, OUT,
                                    cc.TOPE_PARCIAL_USD, stub=True,
                                    por_id=por_id)
    lineas = (OUT / rd.JSONL_DESC).read_text(encoding="utf-8").strip().split("\n")
    check("la corrida stub persiste 20 líneas sin freno (20 llamadas)",
          len(lineas) == 20 and meta["frenado"] is None
          and stub.llamadas == 20)
    check("las 20 requests llevan el contrato del instrumento (system, tool, "
          "tool_choice forzado, model, max_tokens)",
          len(stub.requests) == 20 and all(
              k["system"][0]["text"] == dc.PREFIJO_DESCUBRIMIENTO
              and k["tools"] == [dc.TOOL_DESCUBRIMIENTO]
              and k["tool_choice"]["name"] == dc.NOMBRE_TOOL_DESC
              and k["model"] == dc.MODEL_DESC
              and k["max_tokens"] == dc.MAX_OUTPUT_TOKENS_DESC
              for k in stub.requests))
    check("el texto dopado (con su cláusula) viaja en el user message de la "
          "request de su unidad",
          dop[0]["clausula_plantada"] in stub.requests[0]["messages"][0]["content"])
    claves = ["chunk_id", "unidad", "tipo_unidad", "titulo", "stop_reason",
              "error", "usage", "tool_input_crudo", "hallazgos", "n_hallazgos"]
    check("cada línea del jsonl tiene EXACTAMENTE las claves declaradas",
          all(list(json.loads(x).keys()) == claves for x in lineas))
    regs = rc.cargar_jsonl_last_wins(OUT / rd.JSONL_DESC)
    check("la malformada quedó persistida con su crudo y error "
          "salida_malformada (contenedor no-lista), sin salteo",
          str(regs[c_mal]["error"]).startswith("salida_malformada")
          and regs[c_mal]["tool_input_crudo"] == {"hallazgos": "no-una-lista"}
          and regs[c_mal]["hallazgos"] is None)
    check("codigo_salida == 2 con la malformada presente (no salteo "
          "silencioso) y == 3 si hubiera freno de tope",
          rd.codigo_salida(seleccion, regs, None) == 2
          and rd.codigo_salida(seleccion, regs, "tope") == 3)

    resumen = rd.resumen_descubrimiento(seleccion, OUT, stub.resumen(), meta,
                                        guardas)
    cm = resumen["conteo_mecanico"]
    check("conteo mecánico: A' 9/10 cero-hallazgos y 1 con hallazgos; C con "
          "la malformada fuera de ambos conteos y en con_error",
          cm["n_cero_hallazgos"]["A'"] == 9
          and cm["con_hallazgos"]["A'"] == [d0]
          and c_mal not in cm["cero_hallazgos"]["C"]
          and c_mal not in cm["con_hallazgos"]["C"]
          and c_mal in cm["con_error"]
          and c_mal in cm["contenedores_no_lista"])
    check("el resumen NO computa P-cal (sin 'pasa', sin umbral aplicado; "
          "nota de adjudicación presente)",
          "pasa" not in json.dumps(cm, ensure_ascii=False)
          and "adjudica la autora" in cm["nota"]
          and resumen["costo_recomputado_desde_usage_usd"] == 0.0)

    # Reanudación: la malformada (error) se reintenta; las 19 OK no.
    stub2 = rd.StubClienteDescubrimiento({c_mal: {"hallazgos": []}})
    meta2 = rd.correr_descubrimiento(stub2, seleccion, OUT,
                                     cc.TOPE_PARCIAL_USD, stub=True,
                                     por_id=por_id)
    regs2 = rc.cargar_jsonl_last_wins(OUT / rd.JSONL_DESC)
    check("reanudación idempotente: solo la unidad con error se re-llama "
          "(1 llamada), queda sin error y el exit code pasa a 0",
          stub2.llamadas == 1 and meta2["frenado"] is None
          and regs2[c_mal]["error"] is None
          and rd.codigo_salida(seleccion, regs2, None) == 0)

    passed = sum(ok for _, ok in _checks)
    print(f"\n  {passed}/{len(_checks)} checks OK")
    print("  RESULTADO:", "PASS" if passed == len(_checks) else "FAIL")
    return 0 if passed == len(_checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
