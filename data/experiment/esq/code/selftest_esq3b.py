"""
selftest_esq3b.py — selftest previo al gasto de U-ESQ-3b ($0, sin API).
Patrón [PASS]/[FAIL] de la saga ESQ.

Guardas verificadas:
  1. Candados de base: el prefijo de PRODUCCIÓN sigue siendo el medido en
     ESQ-2 (hash y sha256 contra los sellos `a7788c1`) y `cobertura/` está
     intacta — el retoque se aplica sobre el mismo texto base.
  2. Prefijo retocado: determinístico (dos construcciones → mismos bytes), sha
     estable, distinto del de producción, y contiene EXACTAMENTE los retoques
     del laudo: 9 tipos, 14 predicados, conteos actualizados, R9 con los DOS
     valores del pre-registro §0 y ninguno más, R4 como regla de omisión,
     R7 como campo de Operacion.
  3. Matriz dominio/rango nueva CONSISTENTE: cubre los 14 predicados, sus
     extremos están en el vocabulario retocado, y el diff contra la matriz de
     producción es exactamente el que el laudo aprueba.
  4. Tool schema retocado: enums = vocabulario retocado, catálogo de sujetos
     sin tocar, sin campos del canal abierto, `additionalProperties` en False,
     `required` igual al de producción.
  5. NO-FILTRACIÓN, en LOS DOS BRAZOS (Adenda 1 / laudo del freno 1, punto 6):
     ninguna ventana de 5 palabras del texto de las unidades —objetivo Y
     regresión— aparece en el texto AGREGADO por el retoque (el test no puede
     estar escrito dentro del prompt que testea). Las coincidencias que ya
     estaban en el prefijo de PRODUCCIÓN se listan aparte: son idénticas en los
     dos brazos del pareo y por construcción no pueden sesgar la comparación.
  6. Selección de brazos byte-reproducible desde el worksheet; brazos
     disjuntos; conteos de la Adenda 1 (objetivo 17 · regresión 26 · total 43);
     las fichas nombradas del pre-registro §2 están; R8 coincide con un
     recuento independiente hecho acá; el alcance del veredicto de R6a
     (Adenda 1 §3) queda registrado en la selección.
  7. Caché/namespace propios sin colisión: db nueva; namespace propio ausente
     de TODAS las dbs existentes (lectura read-only) y distinto del de
     producción y del de ESQ-2.
  8. Tope duro USD 1,00 cableado: `chequear_tope` frena y el `create()` del
     cliente frena por proyección ANTES de tocar caché o red (instancia sin
     `__init__`: no se construye ningún cliente de API en el selftest).
  9. Tarifas/modelo: transcripción verbatim contra `runner_corpus.py:76-78`
     (leído como texto, sin importarlo).
 10. ENTRADA DE TEXTOS LARGOS (entrada 11 de la cola): >1024 bytes sin pérdida
     por multilínea y por archivo, alarma ante línea sospechosa, y round-trip
     por el JSON del worksheet sin truncar.
 11. Runner con stub, salida propia en `selftest_out/`: reanudación idempotente
     (corrida abortada → re-corrida completa → tercera no llama nada).
 12. Fichas pareadas del stub: cegadas (ninguna clave prohibida), marcas en
     null, orden determinístico por semilla, las dos extracciones presentes, y
     los dos agregados de la Adenda 1 §5 (DUDA con nota libre en las tres
     preguntas + observaciones por unidad).

Uso:  .venv/bin/python3 -B data/experiment/esq/code/selftest_esq3b.py
"""

from __future__ import annotations

import copy
import hashlib
import json
import re
import shutil
import sqlite3
import subprocess
import sys
import unicodedata
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_esq3b as cc          # noqa: E402
import prompt_esq3b as pr         # noqa: E402
import seleccion_esq3b as sel     # noqa: E402
import fichas_esq3b as fic        # noqa: E402
import entrada_larga as el        # noqa: E402
import prompt_e1                  # noqa: E402
import schema as schema_prod      # noqa: E402

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


def norm_palabras(s: str) -> list[str]:
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.replace("- ", "").replace("-\n", "")
    return re.sub(r"[^a-z0-9 ]", " ", s.replace("\n", " ")).split()


def main() -> int:  # noqa: C901 — selftest lineal, se lee de arriba abajo
    # ---- 1. candados de base ------------------------------------------------
    check("prefijo de PRODUCCIÓN == candado de ESQ-2",
          prompt_e1.prefijo_hash(False) == cc.PREFIJO_HASH_PRODUCCION_ESPERADO,
          prompt_e1.prefijo_hash(False))
    sellos = json.loads((cc.COBERTURA_DIR / "sellos_produccion_sha256.json"
                         ).read_text(encoding="utf-8"))
    dif = []
    for rel, sha in sellos["archivos"].items():
        p = cc.REPO_DIR / rel
        actual = sha256_de(p) if p.exists() else "AUSENTE"
        if actual != sha:
            dif.append(f"{rel}: {sha[:12]}→{actual[:12]}")
    check("producción + cobertura intactas por sha256 (22 sellos de ESQ-2)",
          not dif, f"{len(sellos['archivos'])} archivos; divergentes: {dif}")

    # ---- 2. prefijo retocado ------------------------------------------------
    a = pr.prefijo_sistema_retocado()
    b = pr.prefijo_sistema_retocado()
    check("prefijo retocado DETERMINÍSTICO (dos construcciones, mismos bytes)",
          a == b == pr.PREFIJO_SISTEMA_RETOCADO,
          f"sha256={pr.PREFIJO_SHA256_RETOCADO[:16]}…")
    check("prefijo retocado != prefijo de producción",
          pr.PREFIJO_SISTEMA_RETOCADO != prompt_e1.PREFIJO_SISTEMA,
          f"{len(prompt_e1.PREFIJO_SISTEMA)} → "
          f"{len(pr.PREFIJO_SISTEMA_RETOCADO)} chars")
    check("hash del prefijo retocado != el de producción y != el del canal abierto",
          pr.PREFIJO_HASH_RETOCADO not in (prompt_e1.prefijo_hash(False),
                                           prompt_e1.prefijo_hash(True)),
          pr.PREFIJO_HASH_RETOCADO)
    t = pr.PREFIJO_SISTEMA_RETOCADO
    check("R1 · tipo Potestad presente con la facultad discrecional de la autoridad",
          "**Potestad**" in t and "DISCRECIONAL de la autoridad" in t)
    check("R2 · tipo Condicion + predicado condicion_de en la tabla de firmas",
          "**Condicion**" in t
          and "| `condicion_de` | Condicion → {Excepcion, Obligacion, Restriccion} |" in t)
    check("R3 · tipo Definicion con la delimitación de la f. 37 (los actos "
          "definidos siguen en Operacion)",
          "**Definicion**" in t and "DELIMITACIÓN ESTRICTA" in t
          and "va en **Operacion**" in t)
    check("R4 · regla de omisión de meta-normativo, con justificación, y SIN "
          "tipo nuevo",
          "CONTENIDO META-NORMATIVO: NO SE EXTRAE" in t
          and "Justificación:" in t
          and "Interpretacion" not in t)
    check("R6a · predicado exceptua_operacion en la tabla de firmas",
          "| `exceptua_operacion` | Excepcion → Operacion |" in t)
    check("R7 · campo descripcion en las properties de Operacion",
          "Properties: tipo (string), descripcion (string" in t)
    check("R8 · dominio de aplica_a ampliado con Operacion y Excepcion",
          "| `aplica_a` | {Restriccion, Obligacion, Operacion, Excepcion, "
          "Potestad} →" in t)
    nuevos_r9 = [v for v in pr.OBLIGACION_TIPO_RETOCADO
                 if v not in ("presentacion_informativa", "calculo", "asignacion",
                              "comunicacion_a_cliente", "otra")]
    check("R9 · EXACTAMENTE dos valores nuevos en el enum de Obligacion.tipo "
          "(pre-registro §0)",
          nuevos_r9 == ["reporte_al_supervisor", "requisito_de_estructura"]
          and all(f'"{v}"' in t for v in nuevos_r9),
          str(nuevos_r9))
    check("conteos del prefijo actualizados (9 tipos / 14 predicados) y sin "
          "rastro de los viejos",
          "exactamente 9, ningún otro" in t and "exactamente 14, ningún otro" in t
          and "exactamente 6, ningún otro" not in t
          and "exactamente 12, ningún otro" not in t
          and "los 6 tipos de entidad o 12 predicados" not in t)
    check("el prefijo retocado NO trae el canal abierto",
          "tipo_propuesto" not in t and "predicado_propuesto" not in t
          and "CANAL ABIERTO" not in t)

    # ---- 3. matriz dominio/rango -------------------------------------------
    m, mp = pr.DOMAIN_RANGE_RETOCADO, schema_prod.DOMAIN_RANGE
    check("la matriz retocada cubre los 14 predicados del vocabulario",
          set(m) == set(pr.PREDICATES_RETOCADO) and len(m) == 14)
    vocab = set(pr.ENTITY_TYPES_RETOCADO) | {"Sujeto"}
    fuera = {p: (d | r) - vocab for p, (d, r) in m.items() if (d | r) - vocab}
    check("todos los extremos de la matriz están en el vocabulario retocado",
          not fuera, str(fuera))
    diff = {p: (sorted(m[p][0] - mp[p][0]), sorted(m[p][1] - mp[p][1]))
            for p in mp if m[p] != mp[p]}
    esperado = {
        "establecida_en": (["Condicion", "Definicion", "Potestad"], []),
        "aplica_a": (["Excepcion", "Operacion", "Potestad"], []),
    }
    check("el diff de la matriz contra producción es exactamente el del laudo "
          "(R1+R8 sobre establecida_en y aplica_a; nada más cambia)",
          diff == esperado, str(diff))
    check("ningún predicado de producción PIERDE dominio o rango",
          all(mp[p][0] <= m[p][0] and mp[p][1] <= m[p][1] for p in mp))
    casos_ok = [("Potestad", "establecida_en", "TextoOrdenado"),
                ("Operacion", "aplica_a", "Sujeto"),
                ("Excepcion", "aplica_a", "Sujeto"),
                ("Condicion", "condicion_de", "Obligacion"),
                ("Excepcion", "exceptua_operacion", "Operacion")]
    casos_no = [("Definicion", "condicion_de", "Obligacion"),
                ("Potestad", "regula", "Operacion"),
                ("Obligacion", "exceptua_operacion", "Operacion"),
                ("Condicion", "aplica_a", "Sujeto"),
                ("Restriccion", "predicado_inexistente", "Operacion")]
    check("firma_valida acepta las firmas nuevas del laudo",
          all(pr.firma_valida(*c) for c in casos_ok))
    check("firma_valida rechaza lo que el laudo NO aprobó",
          not any(pr.firma_valida(*c) for c in casos_no))

    # ---- 4. tool schema ----------------------------------------------------
    ts, tp = pr.TOOL_SCHEMA_RETOCADO, prompt_e1.TOOL_SCHEMA_E1
    e_new = ts["input_schema"]["properties"]["entities"]["items"]
    e_old = tp["input_schema"]["properties"]["entities"]["items"]
    r_new = ts["input_schema"]["properties"]["relations"]["items"]
    r_old = tp["input_schema"]["properties"]["relations"]["items"]
    check("enum de type = 9 tipos retocados; enum de predicate = 14",
          e_new["properties"]["type"]["enum"] == list(pr.ENTITY_TYPES_RETOCADO)
          and r_new["properties"]["predicate"]["enum"] == list(pr.PREDICATES_RETOCADO))
    check("catálogo de sujetos SIN tocar en el tool schema",
          r_new["properties"]["sujeto_id"]["enum"]
          == r_old["properties"]["sujeto_id"]["enum"]
          and r_new["properties"]["sujeto_propuesto_padre_sugerido"]["enum"]
          == r_old["properties"]["sujeto_propuesto_padre_sugerido"]["enum"])
    check("required y additionalProperties idénticos a producción",
          e_new["required"] == e_old["required"]
          and r_new["required"] == r_old["required"]
          and e_new["additionalProperties"] is False
          and r_new["additionalProperties"] is False
          and ts["input_schema"]["additionalProperties"] is False)
    check("el tool schema retocado no agrega ni saca campos",
          set(e_new["properties"]) == set(e_old["properties"])
          and set(r_new["properties"]) == set(r_old["properties"]))
    check("prompt_e1.TOOL_SCHEMA_E1 no fue mutado por la construcción del retocado",
          tp["description"].startswith("Extrae entidades y relaciones del chunk "
                                       "según el schema cerrado v2 (6 entidades")
          and e_old["properties"]["type"]["enum"] == list(schema_prod.ENTITY_TYPES))
    kw = pr.build_request_kwargs_retocado(cc.cargar_chunks_esq2(("ayccef",))[0],
                                          model=cc.MODEL_E1)
    check("request: system en bloques con cache_control ephemeral (D1) y nada "
          "variable antes del breakpoint",
          isinstance(kw["system"], list) and len(kw["system"]) == 1
          and kw["system"][0]["cache_control"] == {"type": "ephemeral"}
          and kw["system"][0]["text"] == pr.PREFIJO_SISTEMA_RETOCADO)
    check("request: tool_choice y max_tokens iguales a producción",
          kw["tool_choice"] == {"type": "tool", "name": pr.NOMBRE_TOOL}
          and kw["max_tokens"] == prompt_e1.MAX_OUTPUT_TOKENS)

    # ---- 5. no-filtración ---------------------------------------------------
    seleccion = sel.construir()
    ws = json.loads(cc.WORKSHEET_ESQ2.read_text(encoding="utf-8"))
    por_cid = {f["chunk_id"]: f for f in ws["fichas"]}
    # Adenda 1 / punto 6 del laudo del freno 1: la regla se extiende a LOS DOS
    # brazos. La formulación precisa es sobre el texto AGREGADO por el retoque:
    # una coincidencia que ya estaba en el prefijo de producción es idéntica en
    # los dos brazos del pareo (la vio también la extracción vieja), así que no
    # puede sesgar la comparación; una introducida por el retoque sí.
    pref_norm = " ".join(norm_palabras(pr.PREFIJO_SISTEMA_RETOCADO))
    prod_norm = " ".join(norm_palabras(prompt_e1.PREFIJO_SISTEMA))
    colisiones: dict[str, list] = {"objetivo": [], "regresion": []}
    preexistentes: dict[str, list] = {"objetivo": [], "regresion": []}
    for brazo in ("objetivo", "regresion"):
        for u in seleccion[brazo]["unidades"]:
            w = norm_palabras(
                por_cid[u["chunk_id"]]["texto_fuente"]["texto_propio"])
            for i in range(len(w) - 4):
                g = " ".join(w[i:i + 5])
                if g not in pref_norm:
                    continue
                destino = preexistentes if g in prod_norm else colisiones
                destino[brazo].append((u["chunk_id"], g))
    n_obj = len(seleccion["objetivo"]["unidades"])
    n_reg = len(seleccion["regresion"]["unidades"])
    check(f"NO-FILTRACIÓN (brazo OBJETIVO, {n_obj} u.): ninguna ventana de 5 "
          f"palabras aparece en el texto AGREGADO por el retoque",
          not colisiones["objetivo"], str(colisiones["objetivo"][:3]))
    check(f"NO-FILTRACIÓN (brazo REGRESIÓN, {n_reg} u.): ninguna ventana de 5 "
          f"palabras aparece en el texto AGREGADO por el retoque",
          not colisiones["regresion"], str(colisiones["regresion"][:3]))
    tot_pre = len(preexistentes["objetivo"]) + len(preexistentes["regresion"])
    check("coincidencias PREEXISTENTES (ya en el prefijo de producción, "
          "idénticas en los dos brazos del pareo): declaradas, no sesgan",
          True, f"{tot_pre} coincidencia(s): "
                f"{preexistentes['objetivo'] + preexistentes['regresion']}")

    # ---- 6. selección de brazos --------------------------------------------
    s1 = json.dumps(sel.construir(), ensure_ascii=False, indent=1)
    s2 = json.dumps(sel.construir(), ensure_ascii=False, indent=1)
    persistida = (cc.ORDEN_DIR / "seleccion_brazos_esq3b.json"
                  ).read_text(encoding="utf-8")
    check("selección BYTE-REPRODUCIBLE (dos derivaciones y el archivo "
          "persistido coinciden byte a byte)",
          s1 == s2 == persistida,
          f"sha256={hashlib.sha256(s1.encode()).hexdigest()[:16]}…")
    obj_cids = {u["chunk_id"] for u in seleccion["objetivo"]["unidades"]}
    reg_cids = {u["chunk_id"] for u in seleccion["regresion"]["unidades"]}
    check("brazos DISJUNTOS", not (obj_cids & reg_cids), str(obj_cids & reg_cids))
    por_n = {f["n"]: f["chunk_id"] for f in ws["fichas"]}
    nombradas = {26, 15, 39, 25, 46, 37, 19, 63, 38, 44, 62, 65, 32, 67}
    check("el brazo objetivo contiene las 14 fichas NOMBRADAS del pre-registro §2",
          {por_n[n] for n in nombradas} <= obj_cids,
          f"{len(nombradas)} nombradas + R8")
    # recuento independiente de R8 (no reusa derivar_r8)
    regs = cc.cargar_extracciones_esq2()
    r8_indep = sorted(
        cid for cid in por_cid
        if any(x.get("motivo") == "firma_invalida"
               and (x.get("elemento") or {}).get("predicate") == "aplica_a"
               for x in (regs[cid].get("validacion") or {}).get("rechazos") or []))
    check("R8 derivada == recuento independiente de tripletas aplica_a con "
          "firma_invalida",
          sorted(seleccion["r8_derivacion"]["unidades"]) == r8_indep,
          f"{len(r8_indep)} unidades: {r8_indep}")
    check("regla de regresión aplicada tal cual: todas las q1=si_completo + "
          "q2=ninguna fuera del objetivo están en el brazo",
          all(cid in reg_cids for cid in por_cid
              if por_cid[cid]["preguntas"]["q1_representado"]["marca"] == "si_completo"
              and por_cid[cid]["preguntas"]["q2_deformacion"]["firma"] == "ninguna"
              and cid not in obj_cids))
    check("conteos de la Adenda 1 §2: objetivo 17 · regresión 26 · total 43",
          len(obj_cids) == 17 and len(reg_cids) == 26
          and len(obj_cids) + len(reg_cids) == 43,
          f"objetivo={len(obj_cids)} regresión={len(reg_cids)} "
          f"total={len(obj_cids) + len(reg_cids)}")
    check("el completado de regresión usó azarosas y DESPUÉS dirigidas "
          "(Adenda 1 §2)",
          seleccion["regresion"]["completado_azarosas_q2_ninguna"] == 10
          and seleccion["regresion"]["completado_dirigidas_q2_ninguna"] == 4
          and seleccion["regresion"]["grupo1_si_completo_q2_ninguna"] == 12,
          f"12 + {seleccion['regresion']['completado_azarosas_q2_ninguna']} az "
          f"+ {seleccion['regresion']['completado_dirigidas_q2_ninguna']} dir")
    check("el techo alcanzable (26 < 35 nominal) queda DECLARADO en la "
          "selección persistida",
          bool(seleccion["anomalias_declaradas"]),
          f"regresión n={len(reg_cids)}")
    mapa = seleccion["objetivo"]["mapa_ficha_retoque"]
    check("Adenda 1 §3: f. 62 y f. 65 marcadas 'R6a:corrobora' y el alcance "
          "del veredicto de R6a queda registrado",
          mapa[por_n[62]] == ["R6a:corrobora"]
          and mapa[por_n[65]] == ["R6a:corrobora"]
          and mapa[por_n[44]] == ["R6a:principal"]
          and "NO cuentan para el veredicto de R6a"
          in seleccion["objetivo"]["alcance_veredicto_r6a"])

    # ---- 7. caché / namespace ----------------------------------------------
    ns = cc.namespace_esq3b()
    check("db propia NUEVA, distinta de producción y de la saga ESQ",
          str(cc.DB_ESQ3B) not in {str(p) for p in cc.DBS_AJENAS},
          str(cc.DB_ESQ3B.relative_to(cc.REPO_DIR)))
    check("namespace propio distinto del de producción y del de ESQ-2",
          ns != cc.namespace_produccion() and ns != cc.namespace_cobertura_esq2(),
          ns)
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
    check("el namespace propio NO existe en ninguna db ajena (lectura read-only)",
          not presentes, str(presentes))

    # ---- 8. tope duro -------------------------------------------------------
    freno = False
    try:
        cc.chequear_tope(0.98, 0.05, cc.TOPE_USD)
    except cc.TopeExcedido:
        freno = True
    check("chequear_tope frena al superar el tope USD 1,00", freno)
    try:
        cc.chequear_tope(0.10, 0.05, cc.TOPE_USD)
        paso = True
    except cc.TopeExcedido:
        paso = False
    check("chequear_tope deja pasar por debajo del tope", paso)
    fake = cc.ClienteEsq3b.__new__(cc.ClienteEsq3b)   # sin __init__: sin API
    fake.gasto_usd, fake.tope_usd, fake._proyeccion_usd = 0.99, cc.TOPE_USD, 0.05
    freno2 = False
    try:
        fake.create(doc="x", messages=[])
    except cc.TopeExcedido:
        freno2 = True
    except AttributeError:
        freno2 = False   # llegó a tocar la caché: el freno NO es lo primero
    check("create() del cliente frena por proyección ANTES de tocar caché o red",
          freno2)
    check("TOPE_USD del código == tope del pre-registro §5", cc.TOPE_USD == 1.00)

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

    # ---- 10. entrada de textos largos (entrada 11) --------------------------
    largo = ("A" * 700 + " ") * 5          # 5 líneas de ~700 bytes = ~3.5 kB
    lineas = [("A" * 700) for _ in range(5)] + ["."]
    it = iter(lineas)
    avisos: list[str] = []
    res = el.leer_texto_largo("x", lector=lambda _p: next(it),
                              salida=lambda s: avisos.append(str(s)))
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
    tmp = cc.SELFTEST_DIR / "esq3b_entrada_larga.txt"
    tmp.write_text(largo, encoding="utf-8")
    it3 = iter([f":f {tmp}"])
    res3 = el.leer_texto_largo("x", lector=lambda _p: next(it3),
                               salida=lambda s: None)
    check("entrada por archivo (`:f`): contenido íntegro, sin pasar por la "
          "línea de la terminal",
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

    # ---- 11. runner con stub, reanudación -----------------------------------
    out = cc.SELFTEST_DIR / "esq3b_stub"
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    jsonl = out / "pareado_esq3b.jsonl"
    py = sys.executable
    runner = str(CODE_DIR / "runner_esq3b.py")
    r1 = subprocess.run([py, "-B", runner, "--stub", "--salida", str(jsonl),
                         "--abortar-tras", "7"], capture_output=True, text=True)
    n1 = len(cc.cargar_jsonl_last_wins(jsonl))
    r2 = subprocess.run([py, "-B", runner, "--stub", "--salida", str(jsonl)],
                        capture_output=True, text=True)
    n2 = len(cc.cargar_jsonl_last_wins(jsonl))
    r3 = subprocess.run([py, "-B", runner, "--stub", "--salida", str(jsonl)],
                        capture_output=True, text=True)
    n3 = len(cc.cargar_jsonl_last_wins(jsonl))
    total_sel = len(seleccion["objetivo"]["unidades"]) + \
        len(seleccion["regresion"]["unidades"])
    check("stub: corrida abortada persiste lo hecho y sale con 9",
          r1.returncode == 9 and n1 == 7, f"rc={r1.returncode} n={n1}")
    check("stub: la re-corrida SALTEA lo persistido y completa la selección",
          r2.returncode == 0 and n2 == total_sel
          and "pendientes=%d" % (total_sel - 7) in r2.stdout,
          f"n={n2}/{total_sel}")
    check("stub: la tercera corrida no llama nada (idempotente)",
          r3.returncode == 0 and n3 == total_sel and "pendientes=0" in r3.stdout)
    check("stub: el gate de pareo read-only encontró el brazo base de TODAS "
          "las unidades en la db de ESQ-2 (USD 0)",
          f"[gate pareo USD 0] {total_sel} unidades" in r2.stdout
          or f"[gate pareo USD 0] {total_sel} unidades" in r1.stdout)
    chequeos = [r.get("chequeo_esquema_retocado")
                for r in cc.cargar_jsonl_last_wins(jsonl).values()]
    check("stub: el chequeo contra el esquema retocado acepta los tipos y "
          "predicados nuevos",
          all(c and c["entidades_ok"] == 4 and c["relaciones_ok"] == 2
              for c in chequeos),
          f"{len(chequeos)} registros")

    # ---- 12. fichas pareadas del stub --------------------------------------
    ws_out = out / "worksheet_pareado_esq3b.json"
    rc_f = fic.main(extracciones_jsonl=jsonl, salida=ws_out)
    doc = json.loads(ws_out.read_text(encoding="utf-8"))
    claves: set[str] = set()
    for f in doc["fichas"]:
        fic._claves(f, claves)
    check("fichas: generador OK y ninguna clave prohibida (cegado, entrada 10)",
          rc_f == 0 and not (claves & set(fic.CLAVES_PROHIBIDAS)),
          str(sorted(claves & set(fic.CLAVES_PROHIBIDAS))))
    check("fichas: una por unidad seleccionada, con las DOS extracciones",
          len(doc["fichas"]) == total_sel
          and all(f["extraccion_vieja"]["entities"] is not None
                  and f["extraccion_nueva"]["entities"] is not None
                  for f in doc["fichas"]))
    check("fichas: todas las marcas en null (el ejecutor no adjudica)",
          all(f["preguntas"][q]["marca"] is None
              for f in doc["fichas"] for q in ("q1_cambio", "q2_fidelidad",
                                               "q3_migracion")))
    check("Adenda 1 §5: DUDA declarada en las tres preguntas, con campo de "
          "nota libre, y observaciones por unidad",
          all("duda" in f["preguntas"][q]["pregunta"].lower()
              and "nota_duda" in f["preguntas"][q]
              and "observaciones" in f
              for f in doc["fichas"] for q in ("q1_cambio", "q2_fidelidad",
                                               "q3_migracion"))
          and "regla_duda" in doc and "observaciones_por_unidad" in doc)
    import leer_fichas_esq3b as lec
    check("instrumento: 'd' es marca válida y mapea a duda en las tres preguntas",
          all(lec.MARCAS[q].get("d") == "duda"
              for q in ("q1_cambio", "q2_fidelidad", "q3_migracion")))
    ws_out2 = out / "worksheet_pareado_esq3b_2.json"
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

    # ---- cierre -------------------------------------------------------------
    print("\n" + "=" * 78)
    if FALLAS:
        print(f"RESULTADO: {len(FALLAS)}/{N} checks FALLARON → {FALLAS}")
        return 1
    print(f"RESULTADO: {N}/{N} checks PASAN — freno 1 aprobado y Adenda 1 "
          f"(f1fe0d8) aplicada. El selftest no llama a la API y no gasta "
          f"nada; el costo de la corrida de la fase (d) vive en "
          f"esq3b/reporte_freno_final_esq3b.json.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
