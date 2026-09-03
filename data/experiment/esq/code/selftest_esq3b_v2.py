"""
selftest_esq3b_v2.py — selftest previo al gasto de U-ESQ-3b-v2 ($0, sin API).
Patrón [PASS]/[FAIL] de la saga ESQ.

Guardas verificadas:
  1. Candados de base: el prefijo de PRODUCCIÓN sigue siendo el de ESQ-2, el
     prefijo V1 sigue siendo el sellado en la Adenda 1 (`f0a421fb9466`), los
     22 sellos de ESQ-2 están intactos y los insumos de la vuelta 1 (jsonl,
     worksheet adjudicado, selección v1) coinciden con los sha256 que la
     selección v2 registró.
  2. Prefijo v2: determinístico, sha estable, distinto del v1 y del de
     producción, con los TEXTOS EXACTOS del §1 presentes verbatim, la
     remoción COMPLETA de exceptua_operacion (texto, enum y matriz) y los
     conteos actualizados (9 tipos / 13 predicados).
  3. Matriz dominio/rango v2 CONSISTENTE: cubre los 13 predicados, extremos
     en vocabulario, y el diff contra la matriz v1 es EXACTAMENTE la remoción
     de exceptua_operacion.
  4. Tool schema v2: enums = vocabulario v2, catálogo de sujetos sin tocar,
     required/additionalProperties de producción, sin mutar el schema v1.
  5. NO-FILTRACIÓN EN DOS NIVELES (§5): ventanas de 5 palabras de TODAS las
     unidades seleccionadas (texto propio + contexto heredado) contra el
     texto agregado/modificado, MÁS bigramas/trigramas de contenido de las
     unidades de P1–P14 contra las delimitaciones nuevas. Preexistentes
     v1/producción: declaradas, no bloquean.
  6. Selección de brazos byte-reproducible; brazos disjuntos; 15 + 12 = 27;
     derivación mecánica == lista sellada del §2; pool de regresión fresca =
     687 con exclusiones asertadas; cuotas estratificadas (mínimo 1 por TO,
     suman 12).
  7. Caché/namespace propios sin colisión: db nueva; namespace propio ausente
     de TODAS las dbs existentes (producción, saga ESQ y VUELTA 1 incluida).
  8. Tope duro USD 0,40 cableado: chequear_tope frena y el create() del
     cliente frena por proyección ANTES de tocar caché o red.
  9. Tarifas/modelo: transcripción verbatim contra runner_corpus.py.
 10. Instrumento (§5, prerrequisito de la lectura): entrada de textos largos
     (>1024 bytes sin pérdida, alarma, :f, round-trip) Y el ARREGLO DEL BUG
     DE PEGADO: un render REAL de ficha pegado en un campo de respuesta se
     descarta entero y el campo queda limpio.
 11. Runner v2 con stub, salida propia en selftest_out/: reanudación
     idempotente; gate de pareo DOBLE (objetivo→db v1, fresca→db ESQ-2) en
     verde a USD 0.
 12. Fichas pareadas del stub: cegadas (ninguna clave prohibida), marcas en
     null (q4 incluida), orden determinístico por semilla, las dos
     extracciones presentes, DUDA en todas las preguntas, observaciones por
     unidad.

Uso:  .venv/bin/python3 -B data/experiment/esq/code/selftest_esq3b_v2.py
"""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import sqlite3
import subprocess
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_esq3b_v2 as cc         # noqa: E402
import prompt_esq3b_v2 as pr        # noqa: E402
import prompt_esq3b as pr1          # noqa: E402
import seleccion_esq3b_v2 as sel    # noqa: E402
import fichas_esq3b_v2 as fic       # noqa: E402
import entrada_larga_v2 as el       # noqa: E402
import no_filtracion_v2 as nf       # noqa: E402
import prompt_e1                    # noqa: E402

FALLAS: list[str] = []
N = 0


def check(nombre: str, cond: bool, detalle: str = "") -> None:
    global N
    N += 1
    if cond:
        print(f"[PASS] {nombre}" + (f" — {detalle}" if detalle else ""))
    else:
        print(f"[FAIL] {nombre}" + (f" — {detalle}" if detalle else ""))
        FALLAS.append(nombre)


def sha256_de(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def main() -> int:  # noqa: C901 — selftest lineal, se lee de arriba abajo
    # ---- 1. candados de base ------------------------------------------------
    check("prefijo de PRODUCCIÓN == candado de ESQ-2",
          prompt_e1.prefijo_hash(False) == cc.PREFIJO_HASH_PRODUCCION_ESPERADO,
          prompt_e1.prefijo_hash(False))
    check("prefijo V1 == candado de la Adenda 1 (f0a421fb9466)",
          pr1.PREFIJO_HASH_RETOCADO == cc.PREFIJO_HASH_V1_ESPERADO,
          pr1.PREFIJO_HASH_RETOCADO)
    sellos = json.loads((cc.COBERTURA_DIR / "sellos_produccion_sha256.json"
                         ).read_text(encoding="utf-8"))
    dif = []
    for rel, sha in sellos["archivos"].items():
        p = cc.REPO_DIR / rel
        actual = sha256_de(p) if p.exists() else "AUSENTE"
        if actual != sha:
            dif.append(f"{rel}: {sha[:12]}→{actual[:12]}")
    check("producción + cobertura intactas por sha256 (sellos de ESQ-2)",
          not dif, f"{len(sellos['archivos'])} archivos; divergentes: {dif}")
    sel_persistida_path = cc.ORDEN_DIR / "seleccion_brazos_esq3b_v2.json"
    sel_doc = json.loads(sel_persistida_path.read_text(encoding="utf-8"))
    v1_dif = []
    for rel, sha in sel_doc["insumos_sha256"].items():
        p = cc.UNIDAD_DIR / rel
        actual = sha256_de(p) if p.exists() else "AUSENTE"
        if actual != sha:
            v1_dif.append(f"{rel}: {sha[:12]}→{actual[:12]}")
    check("insumos de la vuelta 1 y de ESQ-2 intactos contra los sha de la "
          "selección v2", not v1_dif, str(v1_dif))

    # ---- 2. prefijo v2 ------------------------------------------------------
    a = pr.prefijo_sistema_v2()
    b = pr.prefijo_sistema_v2()
    check("prefijo v2 DETERMINÍSTICO (dos construcciones, mismos bytes)",
          a == b == pr.PREFIJO_SISTEMA_V2,
          f"sha256={pr.PREFIJO_SHA256_V2[:16]}…")
    check("sha256 del prefijo v2 estable (recomputado == constante)",
          hashlib.sha256(pr.PREFIJO_SISTEMA_V2.encode("utf-8")).hexdigest()
          == pr.PREFIJO_SHA256_V2)
    check("prefijo v2 != prefijo v1 y != prefijo de producción",
          pr.PREFIJO_SISTEMA_V2 != pr1.PREFIJO_SISTEMA_RETOCADO
          and pr.PREFIJO_SISTEMA_V2 != prompt_e1.PREFIJO_SISTEMA,
          f"{len(pr1.PREFIJO_SISTEMA_RETOCADO)} → "
          f"{len(pr.PREFIJO_SISTEMA_V2)} chars")
    check("hash del prefijo v2 != v1, != producción, != canal abierto",
          pr.PREFIJO_HASH_V2 not in (pr1.PREFIJO_HASH_RETOCADO,
                                     prompt_e1.prefijo_hash(False),
                                     prompt_e1.prefijo_hash(True)),
          pr.PREFIJO_HASH_V2)
    t = pr.PREFIJO_SISTEMA_V2
    for nombre, texto in pr.DELIMITACIONES_NUEVAS_V2.items():
        check(f"§1 · texto EXACTO presente verbatim: {nombre}",
              texto in t, f"{len(texto)} chars")
    check("§1 · los textos nuevos NO están en el prefijo v1 (son agregados "
          "de esta vuelta)",
          all(texto not in pr1.PREFIJO_SISTEMA_RETOCADO
              for texto in pr.DELIMITACIONES_NUEVAS_V2.values()))
    check("RE · la descripción VIEJA de requisito_de_estructura ya no está",
          "distinto de ejecutar un acto puntual" not in t)
    check("R6a · exceptua_operacion REMOVIDO por completo del texto",
          "exceptua_operacion" not in t)
    check("R6a · exceptua_operacion fuera del catálogo (13 predicados) y de "
          "la matriz",
          "exceptua_operacion" not in pr.PREDICATES_V2
          and len(pr.PREDICATES_V2) == 13
          and "exceptua_operacion" not in pr.DOMAIN_RANGE_V2)
    check("conteos del prefijo actualizados (9 tipos / 13 predicados) y sin "
          "rastro de los viejos",
          "exactamente 9, ningún otro" in t and "exactamente 13, ningún otro" in t
          and "exactamente 14, ningún otro" not in t
          and "los 9 tipos de entidad o 13 predicados" in t
          and "o 14 predicados" not in t)
    check("el prefijo v2 NO trae el canal abierto",
          "tipo_propuesto" not in t and "predicado_propuesto" not in t
          and "CANAL ABIERTO" not in t)
    check("los 9 tipos y el enum de Obligacion.tipo NO cambian en la vuelta 2",
          pr.ENTITY_TYPES_V2 == pr1.ENTITY_TYPES_RETOCADO
          and pr.OBLIGACION_TIPO_V2 == pr1.OBLIGACION_TIPO_RETOCADO)

    # ---- 3. matriz dominio/rango -------------------------------------------
    m, m1 = pr.DOMAIN_RANGE_V2, pr1.DOMAIN_RANGE_RETOCADO
    check("la matriz v2 cubre los 13 predicados del vocabulario",
          set(m) == set(pr.PREDICATES_V2) and len(m) == 13)
    vocab = set(pr.ENTITY_TYPES_V2) | {"Sujeto"}
    fuera = {p: (d | r) - vocab for p, (d, r) in m.items() if (d | r) - vocab}
    check("todos los extremos de la matriz están en el vocabulario v2",
          not fuera, str(fuera))
    check("diff matriz v2 vs v1 == EXACTAMENTE la remoción de "
          "exceptua_operacion (ninguna otra fila cambia)",
          set(m1) - set(m) == {"exceptua_operacion"}
          and all(m[p] == m1[p] for p in m))
    casos_ok = [("Potestad", "establecida_en", "TextoOrdenado"),
                ("Condicion", "condicion_de", "Obligacion"),
                ("Operacion", "aplica_a", "Sujeto"),
                ("Definicion", "establecida_en", "TextoOrdenado")]
    casos_no = [("Excepcion", "exceptua_operacion", "Operacion"),
                ("Definicion", "condicion_de", "Obligacion"),
                ("Potestad", "regula", "Operacion"),
                ("Restriccion", "predicado_inexistente", "Operacion")]
    check("firma_valida acepta las firmas vigentes",
          all(pr.firma_valida(*c) for c in casos_ok))
    check("firma_valida rechaza exceptua_operacion y lo no aprobado",
          not any(pr.firma_valida(*c) for c in casos_no))

    # ---- 4. tool schema -----------------------------------------------------
    ts, t1 = pr.TOOL_SCHEMA_V2, pr1.TOOL_SCHEMA_RETOCADO
    e_new = ts["input_schema"]["properties"]["entities"]["items"]
    e_old = t1["input_schema"]["properties"]["entities"]["items"]
    r_new = ts["input_schema"]["properties"]["relations"]["items"]
    r_old = t1["input_schema"]["properties"]["relations"]["items"]
    check("enum de type = 9 tipos; enum de predicate = 13 (sin "
          "exceptua_operacion)",
          e_new["properties"]["type"]["enum"] == list(pr.ENTITY_TYPES_V2)
          and r_new["properties"]["predicate"]["enum"] == list(pr.PREDICATES_V2))
    check("catálogo de sujetos SIN tocar en el tool schema",
          r_new["properties"]["sujeto_id"]["enum"]
          == r_old["properties"]["sujeto_id"]["enum"]
          and r_new["properties"]["sujeto_propuesto_padre_sugerido"]["enum"]
          == r_old["properties"]["sujeto_propuesto_padre_sugerido"]["enum"])
    check("required y additionalProperties idénticos a producción/v1",
          e_new["required"] == e_old["required"]
          and r_new["required"] == r_old["required"]
          and e_new["additionalProperties"] is False
          and r_new["additionalProperties"] is False
          and ts["input_schema"]["additionalProperties"] is False)
    check("el tool schema v2 no agrega ni saca campos",
          set(e_new["properties"]) == set(e_old["properties"])
          and set(r_new["properties"]) == set(r_old["properties"]))
    check("TOOL_SCHEMA_RETOCADO (v1) no fue mutado por la construcción del v2",
          r_old["properties"]["predicate"]["enum"]
          == list(pr1.PREDICATES_RETOCADO)
          and "14 predicados" in t1["description"])
    kw = pr.build_request_kwargs_v2(cc.cargar_chunks_esq2(("ayccef",))[0],
                                    model=cc.MODEL_E1)
    check("request: system en bloques con cache_control ephemeral (D1) y nada "
          "variable antes del breakpoint",
          isinstance(kw["system"], list) and len(kw["system"]) == 1
          and kw["system"][0]["cache_control"] == {"type": "ephemeral"}
          and kw["system"][0]["text"] == pr.PREFIJO_SISTEMA_V2)
    check("request: tool_choice y max_tokens iguales a producción",
          kw["tool_choice"] == {"type": "tool", "name": pr.NOMBRE_TOOL}
          and kw["max_tokens"] == prompt_e1.MAX_OUTPUT_TOKENS)

    # ---- 5. no-filtración en DOS niveles ------------------------------------
    res_nf = nf.verificar()
    nf.imprimir(res_nf)
    check("NO-FILTRACIÓN nivel 1 (ventanas de 5 palabras, 27 unidades, texto "
          "propio + heredado): 0 colisiones nuevas",
          not res_nf["nivel1_colisiones_nuevas"]["objetivo"]
          and not res_nf["nivel1_colisiones_nuevas"]["regresion_fresca"])
    check("NO-FILTRACIÓN nivel 2 (bigramas/trigramas de P1–P14 vs "
          "delimitaciones nuevas): 0 colisiones nuevas",
          not res_nf["nivel2_colisiones_nuevas"])
    n_pre = (len(res_nf["nivel1_preexistentes_v1_o_produccion"]["objetivo"])
             + len(res_nf["nivel1_preexistentes_v1_o_produccion"]["regresion_fresca"])
             + len(res_nf["nivel2_preexistentes_v1_o_produccion"]))
    check("coincidencias PREEXISTENTES v1/producción: declaradas, no bloquean",
          True, f"{n_pre} coincidencia(s)")

    # ---- 6. selección de brazos ---------------------------------------------
    s1 = json.dumps(sel.construir(), ensure_ascii=False, indent=1)
    s2 = json.dumps(sel.construir(), ensure_ascii=False, indent=1)
    persistida = sel_persistida_path.read_text(encoding="utf-8")
    check("selección BYTE-REPRODUCIBLE (dos derivaciones y el archivo "
          "persistido coinciden byte a byte)",
          s1 == s2 == persistida,
          f"sha256={hashlib.sha256(s1.encode()).hexdigest()[:16]}…")
    obj_cids = {u["chunk_id"] for u in sel_doc["objetivo"]["unidades"]}
    reg_cids = {u["chunk_id"] for u in sel_doc["regresion_fresca"]["unidades"]}
    check("brazos DISJUNTOS", not (obj_cids & reg_cids), str(obj_cids & reg_cids))
    check("conteos del pre-registro v2: objetivo 15 · regresión fresca 12 · "
          "total 27",
          len(obj_cids) == 15 and len(reg_cids) == 12,
          f"objetivo={len(obj_cids)} fresca={len(reg_cids)}")
    check("derivación mecánica == lista sellada del §2 (verificación por "
          "grupo registrada en la selección)",
          all(v["coincide"] for v in
              sel_doc["objetivo"]["verificacion_derivacion_vs_lista_sellada"].values()),
          str({g: v["coincide"] for g, v in
               sel_doc["objetivo"]["verificacion_derivacion_vs_lista_sellada"].items()}))
    ws_esq2 = json.loads((cc.COBERTURA_DIR / "fichas" /
                          "worksheet_fichas_esq2.json").read_text(encoding="utf-8"))
    fichadas = {f["chunk_id"] for f in ws_esq2["fichas"]}
    check("EXCLUSIONES del §0 asertadas: ninguna unidad fresca está entre las "
          "75 fichadas ni en el objetivo",
          not (reg_cids & fichadas) and not (reg_cids & obj_cids))
    check("pool de regresión fresca = 687 (762 extraídas sin error − 75 "
          "fichadas)",
          sel_doc["regresion_fresca"]["pool_n"] == 687)
    cuotas = sel_doc["regresion_fresca"]["cuotas_por_to"]
    check("cuotas estratificadas: 10 TOs, mínimo 1, suman 12",
          len(cuotas) == 10 and min(cuotas.values()) >= 1
          and sum(cuotas.values()) == 12, str(cuotas))
    to_de = {u["chunk_id"]: u["to"] for u in sel_doc["regresion_fresca"]["unidades"]}
    reales = {}
    for cid, to in to_de.items():
        reales[to] = reales.get(to, 0) + 1
    check("las 12 frescas respetan las cuotas por TO", reales == cuotas,
          str(reales))
    check("semilla sellada registrada en la selección",
          sel_doc["regresion_fresca"]["semilla"] == "20260903:regresion_fresca_v2")

    # ---- 7. caché / namespace ----------------------------------------------
    ns = cc.namespace_v2()
    check("db propia NUEVA, distinta de producción, de la saga ESQ y de la "
          "VUELTA 1",
          str(cc.DB_V2) not in {str(p) for p in cc.DBS_AJENAS},
          str(cc.DB_V2.relative_to(cc.REPO_DIR)))
    check("namespace propio distinto del de producción, del de ESQ-2 y del "
          "de la vuelta 1",
          ns != cc.namespace_produccion() and ns != cc.namespace_cobertura_esq2()
          and ns != cc.namespace_v1(), ns)
    presentes = []
    for db in cc.DBS_AJENAS:
        if not db.exists():
            continue
        try:
            conn = cc.conectar_db_readonly(db)
            n_filas = conn.execute(
                "SELECT COUNT(*) FROM cache WHERE namespace = ?", (ns,)).fetchone()[0]
            conn.close()
        except sqlite3.Error as e:
            presentes.append(f"{db.name}: {e}")
            continue
        if n_filas:
            presentes.append(f"{db.name}: {n_filas} filas")
    check("el namespace propio NO existe en ninguna db ajena (lectura "
          "read-only; esq_3b.db de la vuelta 1 incluida)",
          not presentes, str(presentes))

    # ---- 8. tope duro USD 0,40 ----------------------------------------------
    check("TOPE_USD del código == tope del pre-registro v2 §6",
          cc.TOPE_USD == 0.40)
    freno = False
    try:
        cc.chequear_tope(0.38, 0.05, cc.TOPE_USD)
    except cc.TopeExcedido:
        freno = True
    check("chequear_tope frena al superar el tope USD 0,40", freno)
    try:
        cc.chequear_tope(0.10, 0.05, cc.TOPE_USD)
        paso = True
    except cc.TopeExcedido:
        paso = False
    check("chequear_tope deja pasar por debajo del tope", paso)
    fake = cc.ClienteEsq3bV2.__new__(cc.ClienteEsq3bV2)   # sin __init__: sin API
    fake.gasto_usd, fake.tope_usd, fake._proyeccion_usd = 0.39, cc.TOPE_USD, 0.05
    freno2 = False
    try:
        fake.create(doc="x", messages=[])
    except cc.TopeExcedido:
        freno2 = True
    except AttributeError:
        freno2 = False   # llegó a tocar la caché: el freno NO es lo primero
    check("create() del cliente frena por proyección ANTES de tocar caché o red",
          freno2)

    # ---- 9. tarifas verbatim ------------------------------------------------
    rc = (cc.EXP_DIR / "reextraccion_v2" / "corpus_v2" / "runner_corpus.py"
          ).read_text(encoding="utf-8")
    nums = re.findall(r"precio_(?:in|out|cache_write|cache_read)_por_mtok\s*=\s*([\d.]+)",
                      rc)[:4]
    check("tarifas transcriptas verbatim de runner_corpus.py",
          [float(x) for x in nums] == [cc.P_E1["precio_in_por_mtok"],
                                       cc.P_E1["precio_out_por_mtok"],
                                       cc.P_E1["precio_cache_write_por_mtok"],
                                       cc.P_E1["precio_cache_read_por_mtok"]],
          str(nums))
    check("modelo == el de la corrida sellada del corpus",
          f'"{cc.MODEL_E1}"' in rc, cc.MODEL_E1)
    check("fórmula de costo D2 (caso de prueba a mano)",
          abs(cc.costo_usd_desde_usage(
              {"input_tokens": 1_000_000, "output_tokens": 1_000_000,
               "cache_write_tokens": 1_000_000, "cache_read_tokens": 1_000_000})
              - (1.00 + 5.00 + 1.25 + 0.10)) < 1e-9)

    # ---- 10. instrumento: entrada larga + BUG DE PEGADO ---------------------
    largo = ("A" * 700 + " ") * 5
    lineas = [("A" * 700) for _ in range(5)] + ["."]
    it = iter(lineas)
    res = el.leer_texto_largo("x", lector=lambda _p: next(it),
                              salida=lambda s: None)
    check("entrada multilínea: >1024 bytes sin pérdida",
          res.bytes_totales == 5 * 700 + 4 and res.texto == "\n".join(lineas[:5]),
          f"{res.bytes_totales} bytes en {res.lineas} líneas")
    it2 = iter([("B" * 1200), "."])
    avisos2: list[str] = []
    res2 = el.leer_texto_largo("x", lector=lambda _p: next(it2),
                               salida=lambda s: avisos2.append(str(s)))
    check("ALARMA de truncamiento ante una línea de ≥1000 bytes",
          res2.lineas_sospechosas == [1]
          and any("SILENCIOSA" in a for a in avisos2),
          f"{res2.bytes_totales} bytes")
    cc.SELFTEST_DIR.mkdir(parents=True, exist_ok=True)
    tmp = cc.SELFTEST_DIR / "esq3b_v2_entrada_larga.txt"
    tmp.write_text(largo, encoding="utf-8")
    it3 = iter([f":f {tmp}"])
    res3 = el.leer_texto_largo("x", lector=lambda _p: next(it3),
                               salida=lambda s: None)
    check("entrada por archivo (`:f`): contenido íntegro",
          res3.mecanismo == "archivo" and res3.texto == largo.strip("\n"),
          f"{res3.bytes_totales} bytes")
    rt = json.loads(json.dumps({"campo": res.texto}, ensure_ascii=False))["campo"]
    check("round-trip por el JSON del worksheet sin truncar",
          rt == res.texto and len(rt.encode("utf-8")) > 1024)
    obligado = iter(["", ".", "algo", "."])
    res4 = el.leer_texto_largo("x", obligatorio=True,
                               lector=lambda _p: next(obligado),
                               salida=lambda s: None)
    check("campo obligatorio: no acepta vacío y vuelve a pedir",
          res4.texto == "algo")

    # ---- 11. runner v2 con stub, reanudación --------------------------------
    out = cc.SELFTEST_DIR / "esq3b_v2_stub"
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    jsonl = out / "pareado_esq3b_v2.jsonl"
    py = sys.executable
    runner = str(CODE_DIR / "runner_esq3b_v2.py")
    r1 = subprocess.run([py, "-B", runner, "--stub", "--salida", str(jsonl),
                         "--abortar-tras", "7"], capture_output=True, text=True)
    n1 = len(cc.cargar_jsonl_last_wins(jsonl))
    r2 = subprocess.run([py, "-B", runner, "--stub", "--salida", str(jsonl)],
                        capture_output=True, text=True)
    n2 = len(cc.cargar_jsonl_last_wins(jsonl))
    r3 = subprocess.run([py, "-B", runner, "--stub", "--salida", str(jsonl)],
                        capture_output=True, text=True)
    n3 = len(cc.cargar_jsonl_last_wins(jsonl))
    total_sel = len(obj_cids) + len(reg_cids)
    check("stub: corrida abortada persiste lo hecho y sale con 9",
          r1.returncode == 9 and n1 == 7, f"rc={r1.returncode} n={n1}")
    check("stub: la re-corrida SALTEA lo persistido y completa la selección",
          r2.returncode == 0 and n2 == total_sel
          and "pendientes=%d" % (total_sel - 7) in r2.stdout,
          f"n={n2}/{total_sel}")
    check("stub: la tercera corrida no llama nada (idempotente)",
          r3.returncode == 0 and n3 == total_sel and "pendientes=0" in r3.stdout)
    check("stub: el gate de pareo DOBLE read-only encontró el brazo base de "
          "las 27 unidades (objetivo→db v1, fresca→db ESQ-2), USD 0",
          f"[gate pareo doble USD 0] {total_sel} unidades" in r2.stdout
          or f"[gate pareo doble USD 0] {total_sel} unidades" in r1.stdout)
    chequeos = [r.get("chequeo_esquema_v2")
                for r in cc.cargar_jsonl_last_wins(jsonl).values()]
    check("stub: el chequeo contra el esquema v2 acepta los tipos y "
          "predicados vigentes",
          all(c and c["entidades_ok"] == 4 and c["relaciones_ok"] == 2
              for c in chequeos),
          f"{len(chequeos)} registros")

    # ---- 12. fichas pareadas del stub ---------------------------------------
    ws_out = out / "worksheet_pareado_esq3b_v2.json"
    rc_f = fic.main(extracciones_jsonl=jsonl, salida=ws_out)
    doc = json.loads(ws_out.read_text(encoding="utf-8"))
    claves: set[str] = set()
    for f in doc["fichas"]:
        fic._claves(f, claves)
    check("fichas: generador OK y ninguna clave prohibida (cegado, entrada 10)",
          rc_f == 0 and not (claves & set(fic.CLAVES_PROHIBIDAS)),
          str(sorted(claves & set(fic.CLAVES_PROHIBIDAS))))
    check("fichas: una por unidad seleccionada, con las DOS extracciones "
          "(base + nueva)",
          len(doc["fichas"]) == total_sel
          and all(f["extraccion_base"]["entities"] is not None
                  and f["extraccion_nueva"]["entities"] is not None
                  for f in doc["fichas"]))
    check("fichas: todas las marcas en null, q4 incluida (el ejecutor no "
          "adjudica NADA — tampoco P1–P14)",
          all(f["preguntas"][q]["marca"] is None
              for f in doc["fichas"] for q in ("q1_cambio", "q2_fidelidad",
                                               "q3_migracion"))
          and all(e["marca"] is None
                  for f in doc["fichas"]
                  for e in f["preguntas"]["q4_requisito_estructura"]["emisiones"]))
    check("q4: el stub emite requisito_de_estructura y la ficha trae su "
          "entrada de adjudicación por emisión",
          all(len(f["preguntas"]["q4_requisito_estructura"]["emisiones"]) == 1
              for f in doc["fichas"]))
    check("DUDA declarada en las preguntas, con campo de nota libre, y "
          "observaciones por unidad",
          all("duda" in f["preguntas"][q]["pregunta"].lower()
              and "observaciones" in f
              for f in doc["fichas"] for q in ("q1_cambio", "q2_fidelidad",
                                               "q3_migracion",
                                               "q4_requisito_estructura"))
          and "regla_duda" in doc)
    import leer_fichas_esq3b_v2 as lec
    check("instrumento: 'd' es marca válida y mapea a duda en q1–q3 y q4",
          all(lec.MARCAS[q].get("d") == "duda"
              for q in ("q1_cambio", "q2_fidelidad", "q3_migracion"))
          and lec.MARCAS_Q4.get("d") == "duda")
    ws_out2 = out / "worksheet_pareado_esq3b_v2_bis.json"
    fic.main(extracciones_jsonl=jsonl, salida=ws_out2)
    doc2 = json.loads(ws_out2.read_text(encoding="utf-8"))
    check("fichas: orden aleatorizado DETERMINÍSTICO por la semilla declarada",
          [f["chunk_id"] for f in doc["fichas"]]
          == [f["chunk_id"] for f in doc2["fichas"]],
          doc["semilla_orden_lectura"])
    check("fichas: el orden NO es el de la selección (está efectivamente "
          "barajado)",
          [f["chunk_id"] for f in doc["fichas"]]
          != sorted(f["chunk_id"] for f in doc["fichas"]))

    # ---- 10-bis. BUG DE PEGADO: render REAL pegado → campo limpio -----------
    # (después de la fase 12 porque necesita una ficha real del stub)
    ficha_real = doc["fichas"][0]
    render = lec.render_ficha(ficha_real, len(doc["fichas"]))
    check("bug de pegado: el render real dispara la detección de firmas",
          len(el.lineas_render(render)) >= 4,
          f"{len(el.lineas_render(render))} líneas con firma en un render de "
          f"{len(render)} chars")
    entrada = render.splitlines() + ["."] + ["mi respuesta legítima", "."]
    it5 = iter(entrada)
    avisos5: list[str] = []
    res5 = el.leer_texto_largo("campo", lector=lambda _p: next(it5),
                               salida=lambda s: avisos5.append(str(s)))
    check("bug de pegado: render pegado → campo DESCARTADO entero, re-pedido, "
          "y la respuesta posterior queda LIMPIA",
          res5.texto == "mi respuesta legítima"
          and res5.descartes_por_render == 1
          and any("RENDER DE FICHA DETECTADO" in a for a in avisos5),
          f"{res5.descartes_por_render} descarte(s)")
    check("bug de pegado: el campo final no contiene ninguna línea del render",
          not el.lineas_render(res5.texto)
          and "EXTRACCIONES PAREADAS" not in res5.texto)
    it6 = iter(["una observación común, con guiones - y puntos.", "."])
    res6 = el.leer_texto_largo("campo", lector=lambda _p: next(it6),
                               salida=lambda s: None)
    check("bug de pegado: una respuesta legítima NO dispara la detección",
          res6.texto == "una observación común, con guiones - y puntos."
          and res6.descartes_por_render == 0)

    # ---- cierre -------------------------------------------------------------
    print("\n" + "=" * 78)
    if FALLAS:
        print(f"RESULTADO: {len(FALLAS)}/{N} checks FALLARON → {FALLAS}")
        return 1
    print(f"RESULTADO: {N}/{N} checks PASAN. El selftest no llama a la API y "
          f"no gasta nada; la corrida de la fase (e) espera la APROBACIÓN del "
          f"freno 1 (manifiesto_esq3b_v2.py).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
