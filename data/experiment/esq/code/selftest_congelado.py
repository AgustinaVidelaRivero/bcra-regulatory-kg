"""
selftest_congelado.py — selftest de U-CONGELA ($0, sin API, sin escritura en
el repo). Patrón [PASS]/[FAIL] de la saga ESQ.

Guardas verificadas (laudo de esquema congelado §4):
  1. Candados de la CADENA verificados ANTES de construir: producción
     (ESQ-2), v1 (Adenda 1, `f0a421fb9466`) y v2 (`2c1b76d1685d`); y los
     frenos del constructor operan (candado falso, ancla duplicada, mención
     residual → RuntimeError).
  2. Anclas de los DOS reemplazos declarados: únicas en el texto v2, con los
     textos nuevos ausentes del v2 (son de esta materialización).
  3. Texto congelado: 0 menciones residuales de requisito_de_estructura;
     enum de 6 valores presente y consistente con el vocabulario; oraciones
     de reporte_al_supervisor y de «otra» INTACTAS verbatim; la delimitación
     negativa v2 ausente; el resto de las delimitaciones v2 intactas; el
     diff de longitud contra el v2 es EXACTAMENTE el de los dos reemplazos.
  4. Conteos del esquema congelado: 9 tipos / 13 predicados / 6 valores;
     matriz idéntica a la v2; firma_valida consistente.
  5. Tool schema BYTE-IDÉNTICO al v2 (igualdad estricta del canónico y del
     dict), sin alias (deepcopy) y sin haber mutado el schema v2.
  6. Determinismo: doble construcción con sha idéntico; sha256 y hash
     canónico estables; hash congelado distinto de v2/v1/producción/abierto.
  7. Request (D1): system en bloques con cache_control ephemeral, mensaje de
     usuario de producción sin tocar.

Uso:  .venv/bin/python3 -B data/experiment/esq/code/selftest_congelado.py
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_esq3b_v2 as cc      # noqa: E402  (solo lectura: chunk de prueba)
import prompt_congelado as pc    # noqa: E402
import prompt_esq3b_v2 as pr2    # noqa: E402
import prompt_esq3b as pr1       # noqa: E402
import prompt_e1                 # noqa: E402

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


def canonico(schema: dict) -> bytes:
    """Serialización canónica de un tool schema (la misma convención que el
    canónico del prefijo: sort_keys, sin espacios, UTF-8)."""
    return json.dumps(schema, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":")).encode("utf-8")


def main() -> int:  # noqa: C901 — selftest lineal, se lee de arriba abajo
    # ---- 1. candados de la cadena, ANTES de construir -----------------------
    check("candado de PRODUCCIÓN == el de ESQ-2",
          prompt_e1.prefijo_hash(False) == pc.PREFIJO_HASH_PRODUCCION_ESPERADO,
          prompt_e1.prefijo_hash(False))
    check("candado del prefijo V1 == Adenda 1 (f0a421fb9466)",
          pr1.PREFIJO_HASH_RETOCADO == pc.PREFIJO_HASH_V1_ESPERADO,
          pr1.PREFIJO_HASH_RETOCADO)
    check("CANDADO DEL V2 verificado antes de construir (2c1b76d1685d, "
          "laudo §4)",
          pr2.PREFIJO_HASH_V2 == pc.PREFIJO_HASH_V2_ESPERADO == "2c1b76d1685d",
          pr2.PREFIJO_HASH_V2)

    orig_hash = pr2.PREFIJO_HASH_V2
    try:
        pr2.PREFIJO_HASH_V2 = "000000000000"
        try:
            pc.prefijo_sistema_congelado()
            freno_candado = False
        except RuntimeError:
            freno_candado = True
    finally:
        pr2.PREFIJO_HASH_V2 = orig_hash
    check("el constructor FRENA si el candado v2 no coincide", freno_candado)

    orig_texto = pr2.PREFIJO_SISTEMA_V2
    try:
        pr2.PREFIJO_SISTEMA_V2 = orig_texto + pc.REEMPLAZOS_CONGELADO[0][1]
        try:
            pc.prefijo_sistema_congelado()
            freno_ancla = False
        except RuntimeError:
            freno_ancla = True
    finally:
        pr2.PREFIJO_SISTEMA_V2 = orig_texto
    check("el constructor FRENA ante un ancla NO única (texto base mutado)",
          freno_ancla)

    try:
        pr2.PREFIJO_SISTEMA_V2 = orig_texto + "\nrequisito_de_estructura"
        try:
            pc.prefijo_sistema_congelado()
            freno_residuo = False
        except RuntimeError:
            freno_residuo = True
    finally:
        pr2.PREFIJO_SISTEMA_V2 = orig_texto
    check("el constructor FRENA ante una mención residual tras los "
          "reemplazos", freno_residuo)
    check("tras restaurar, el constructor vuelve a producir el congelado",
          pc.prefijo_sistema_congelado() == pc.PREFIJO_SISTEMA_CONGELADO)

    # ---- 2. anclas de los DOS reemplazos declarados -------------------------
    v2 = pr2.PREFIJO_SISTEMA_V2
    check("exactamente DOS reemplazos declarados (laudo §4)",
          len(pc.REEMPLAZOS_CONGELADO) == 2,
          str([n for n, _, _ in pc.REEMPLAZOS_CONGELADO]))
    for nombre, viejo, nuevo in pc.REEMPLAZOS_CONGELADO:
        check(f"ancla ÚNICA en el texto v2: {nombre}",
              v2.count(viejo) == 1, f"{v2.count(viejo)} apariciones")
        check(f"texto nuevo AUSENTE del v2 (es de esta materialización): "
              f"{nombre}", nuevo not in v2)
    check("el pasaje eliminado por (2) es la delimitación negativa v2 "
          "COMPLETA (TEXTO_RE_NUEVO, por identidad de constante)",
          pr2.TEXTO_RE_NUEVO in pc.REEMPLAZOS_CONGELADO[1][1]
          and pr2.TEXTO_RE_NUEVO not in pc.REEMPLAZOS_CONGELADO[1][2])

    # ---- 3. texto congelado -------------------------------------------------
    t = pc.PREFIJO_SISTEMA_CONGELADO
    check("0 MENCIONES RESIDUALES de requisito_de_estructura en el texto "
          "final", t.count("requisito_de_estructura") == 0,
          f"{t.count('requisito_de_estructura')} menciones "
          f"(v2 tenía {v2.count('requisito_de_estructura')})")
    enum_derivado = ('("' + '"|"'.join(pc.OBLIGACION_TIPO_CONGELADO) + '")')
    check("enum de 6 valores presente EXACTAMENTE una vez y == derivado del "
          "vocabulario congelado",
          t.count(pc.REEMPLAZOS_CONGELADO[0][2]) == 1
          and pc.REEMPLAZOS_CONGELADO[0][2] == enum_derivado)
    check("el literal viejo de 7 valores AUSENTE",
          pc.REEMPLAZOS_CONGELADO[0][1] not in t)
    oracion_reporte = (
        "Sobre `tipo`: `reporte_al_supervisor` es el deber de informar al "
        "BCRA, a la Superintendencia o a otro organismo de control — NO se "
        "etiqueta `comunicacion_a_cliente`, que es el deber de informar al "
        "usuario o cliente; son destinatarios distintos y no se confunden."
    )
    oracion_otra = (
        "`otra` es el residuo: usalo cuando el deber no cae en ninguno de "
        "los anteriores, no como caja por defecto."
    )
    check("oración de reporte_al_supervisor INTACTA verbatim",
          oracion_reporte in t and oracion_reporte in v2)
    check("oración de «otra» INTACTA verbatim",
          oracion_otra in t and oracion_otra in v2)
    check("las dos oraciones quedaron contiguas (solo cayó el pasaje del "
          "medio)", (oracion_reporte + " " + oracion_otra) in t)
    check("la delimitación negativa v2 (TEXTO_RE_NUEVO) AUSENTE del "
          "congelado", pr2.TEXTO_RE_NUEVO not in t)
    for nombre, texto in pr2.DELIMITACIONES_NUEVAS_V2.items():
        if nombre == "RE-delimitacion-negativa":
            continue
        check(f"delimitación v2 conservada verbatim: {nombre}", texto in t,
              f"{len(texto)} chars")
    check("conteos del texto intactos (9 tipos / 13 predicados)",
          "exactamente 9, ningún otro" in t
          and "exactamente 13, ningún otro" in t
          and "los 9 tipos de entidad o 13 predicados" in t)
    check("sin canal abierto ni vocabulario retirado",
          "tipo_propuesto" not in t and "CANAL ABIERTO" not in t
          and "exceptua_operacion" not in t)
    delta = (len('"requisito_de_estructura"|')
             + len(" " + pr2.TEXTO_RE_NUEVO))
    check("diff de longitud v2 → congelado == EXACTAMENTE los dos "
          "reemplazos", len(v2) - len(t) == delta,
          f"{len(v2)} − {len(t)} = {len(v2) - len(t)} (esperado {delta})")
    check("prefijo congelado != v2, != v1, != producción",
          t != v2 and t != pr1.PREFIJO_SISTEMA_RETOCADO
          and t != prompt_e1.PREFIJO_SISTEMA)

    # ---- 4. vocabulario y matriz --------------------------------------------
    check("CONTEOS del esquema congelado: 9 tipos / 13 predicados / "
          "6 valores",
          len(pc.ENTITY_TYPES_CONGELADO) == 9
          and len(pc.PREDICATES_CONGELADO) == 13
          and len(pc.OBLIGACION_TIPO_CONGELADO) == 6)
    check("enum congelado == la lista del laudo §4, en su orden",
          pc.OBLIGACION_TIPO_CONGELADO == (
              "presentacion_informativa", "calculo", "asignacion",
              "comunicacion_a_cliente", "reporte_al_supervisor", "otra"))
    check("tipos y predicados == los del v2 (el retiro no toca ni tipos ni "
          "predicados)",
          pc.ENTITY_TYPES_CONGELADO == tuple(pr2.ENTITY_TYPES_V2)
          and pc.PREDICATES_CONGELADO == tuple(pr2.PREDICATES_V2))
    m, m2 = pc.DOMAIN_RANGE_CONGELADO, pr2.DOMAIN_RANGE_V2
    vocab = set(pc.ENTITY_TYPES_CONGELADO) | {"Sujeto"}
    fuera = {p: (d | r) - vocab for p, (d, r) in m.items() if (d | r) - vocab}
    check("matriz congelada == matriz v2, cubre los 13, extremos en "
          "vocabulario",
          set(m) == set(pc.PREDICATES_CONGELADO) and len(m) == 13
          and all(m[p] == m2[p] for p in m) and set(m) == set(m2)
          and not fuera, str(fuera))
    casos_ok = [("Potestad", "establecida_en", "TextoOrdenado"),
                ("Condicion", "condicion_de", "Obligacion"),
                ("Operacion", "aplica_a", "Sujeto"),
                ("Definicion", "establecida_en", "TextoOrdenado")]
    casos_no = [("Excepcion", "exceptua_operacion", "Operacion"),
                ("Definicion", "condicion_de", "Obligacion"),
                ("Potestad", "regula", "Operacion"),
                ("Restriccion", "predicado_inexistente", "Operacion")]
    check("firma_valida acepta las firmas vigentes y rechaza lo retirado",
          all(pc.firma_valida(*c) for c in casos_ok)
          and not any(pc.firma_valida(*c) for c in casos_no))

    # ---- 5. tool schema BYTE-IDÉNTICO al v2 ---------------------------------
    b_cong = canonico(pc.TOOL_SCHEMA_CONGELADO)
    b_v2 = canonico(pr2.TOOL_SCHEMA_V2)
    check("TOOL SCHEMA BYTE-IDÉNTICO al v2 (igualdad estricta del canónico)",
          b_cong == b_v2, f"{len(b_cong)} bytes")
    check("tool schema congelado == v2 también como dict",
          pc.TOOL_SCHEMA_CONGELADO == pr2.TOOL_SCHEMA_V2)
    check("copia profunda, no alias (mutar el congelado no tocaría el v2)",
          pc.TOOL_SCHEMA_CONGELADO is not pr2.TOOL_SCHEMA_V2)
    check("el schema v2 NO fue mutado por esta construcción (== reconstruido "
          "de cero)", b_v2 == canonico(pr2._tool_schema_v2()))
    check("la description del schema mantiene los conteos v2 (9 tipos, 13 "
          "predicados)",
          "9 tipos de entidad, 13 predicados"
          in pc.TOOL_SCHEMA_CONGELADO["description"])

    # ---- 6. determinismo y hashes -------------------------------------------
    a = pc.prefijo_sistema_congelado()
    b = pc.prefijo_sistema_congelado()
    check("DOBLE CONSTRUCCIÓN con bytes idénticos (determinismo)",
          a == b == pc.PREFIJO_SISTEMA_CONGELADO,
          f"sha256={pc.PREFIJO_SHA256_CONGELADO[:16]}…")
    check("sha256 del texto estable (recomputado == constante)",
          hashlib.sha256(pc.PREFIJO_SISTEMA_CONGELADO.encode("utf-8"))
          .hexdigest() == pc.PREFIJO_SHA256_CONGELADO)
    canon_re = json.dumps(
        {"system": pc.bloques_sistema_congelado(),
         "tools": [pc.TOOL_SCHEMA_CONGELADO]},
        sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    check("hash (system+tools) estable (canónico recomputado == constante)",
          canon_re == pc.PREFIJO_CANONICO_CONGELADO
          and hashlib.sha256(canon_re.encode("utf-8")).hexdigest()[:12]
          == pc.PREFIJO_HASH_CONGELADO, pc.PREFIJO_HASH_CONGELADO)
    check("hash congelado != v2, != v1, != producción, != canal abierto",
          pc.PREFIJO_HASH_CONGELADO not in (
              pr2.PREFIJO_HASH_V2, pr1.PREFIJO_HASH_RETOCADO,
              prompt_e1.prefijo_hash(False), prompt_e1.prefijo_hash(True)))

    # ---- 7. request (D1) ----------------------------------------------------
    chunk = cc.cargar_chunks_esq2(("ayccef",))[0]
    kw = pc.build_request_kwargs_congelado(chunk, model=cc.MODEL_E1)
    check("request: system en bloques con cache_control ephemeral (D1) y "
          "texto == prefijo congelado",
          isinstance(kw["system"], list) and len(kw["system"]) == 1
          and kw["system"][0]["cache_control"] == {"type": "ephemeral"}
          and kw["system"][0]["text"] == pc.PREFIJO_SISTEMA_CONGELADO)
    check("request: tools == [schema congelado] y tool_choice/max_tokens de "
          "producción",
          kw["tools"] == [pc.TOOL_SCHEMA_CONGELADO]
          and kw["tool_choice"] == {"type": "tool", "name": pc.NOMBRE_TOOL}
          and kw["max_tokens"] == prompt_e1.MAX_OUTPUT_TOKENS)
    check("request: mensaje de usuario == el de producción sin tocar",
          kw["messages"] == [{"role": "user",
                              "content": prompt_e1.build_user_message(chunk)}])

    # ---- cierre -------------------------------------------------------------
    print("\n" + "=" * 78)
    print(f"sha256 del TEXTO del prefijo congelado: "
          f"{pc.PREFIJO_SHA256_CONGELADO}")
    print(f"hash (system+tools) del prefijo congelado: "
          f"{pc.PREFIJO_HASH_CONGELADO}")
    if FALLAS:
        print(f"RESULTADO: {len(FALLAS)}/{N} checks FALLARON → {FALLAS}")
        return 1
    print(f"RESULTADO: {N}/{N} checks PASAN. El selftest no llama a la API, "
          f"no gasta nada y no escribe en el repo; los sha entran al laudo "
          f"§4 por acto de la mesa y la firma es de la autora.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
