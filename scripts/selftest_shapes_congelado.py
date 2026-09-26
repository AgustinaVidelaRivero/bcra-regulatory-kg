#!/usr/bin/env python3
"""Selftest del perfil «congelado» de scripts/shapes_validator.py (U-B2.2 fase 2).

Solo stdlib. Los fixtures son sintéticos y mínimos, escritos acá mismo: un
grafo base que PASA todas las shapes del perfil (bloqueantes en PASS,
informativas en 0) y, por cada shape, al menos un contraejemplo construido
mutando una copia del base. Además: un caso que verifica que el candado del
sha frena, y tres corridas del CLI para los códigos de salida y el .json.

El vocabulario congelado se lee del módulo real (prompt_congelado.py) a
través del propio validador; no se copia nada acá.

Uso:
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/selftest_shapes_congelado.py

Sale con código 0 si todos los casos pasan, 1 si alguno falla. No escribe
nada fuera de un directorio temporal que se borra al terminar.
"""

import copy
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import traceback

sys.dont_write_bytecode = True

AQUI = os.path.dirname(os.path.abspath(__file__))
RUTA_VALIDADOR = os.path.join(AQUI, "shapes_validator.py")

_spec = importlib.util.spec_from_file_location("shapes_validator", RUTA_VALIDADOR)
sv = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(sv)

VOCAB = sv.cargar_vocabulario_congelado()

# --------------------------------------------------------------------------- #
# Fixtures                                                                    #
# --------------------------------------------------------------------------- #
TO_ARCHIVO = "TO_test.pdf"
ESQ_ARCHIVO = "esquema_test.json"


def prov(punto="1.1", to="tst", archivo=TO_ARCHIVO, rol="punto_propio"):
    return {"to": to, "archivo": archivo, "punto": punto, "rol_documental": rol}


def prov_esqueleto(punto="Punto 1"):
    return {"to": None, "archivo": ESQ_ARCHIVO, "punto": punto,
            "rol_documental": sv.ROL_DOCUMENTAL_ESQUELETO, "chunk_id": None, "paginas": []}


def nodo(nid, tipo, label=None, props=None, p=None):
    p = p if p is not None else prov()
    return {"id": nid, "type": tipo, "label": label or nid, "properties": dict(props or {}),
            "provenance": p, "provenances": [copy.deepcopy(p)]}


def arista(s, t, rel, p=None, **extra):
    p = p if p is not None else prov()
    e = {"source": s, "target": t, "relation": rel, "provenance": p, "provenances": [copy.deepcopy(p)]}
    e.update(extra)
    return e


def grafo_base():
    nodes = [
        nodo("TextoOrdenado_test", "TextoOrdenado", props={"archivo": TO_ARCHIVO}),
        nodo("Obligacion_a", "Obligacion", props={"tipo": "calculo"}, p=prov("1.1")),
        nodo("Obligacion_b", "Obligacion", props={"tipo": "otra"}, p=prov("1.2")),
        nodo("Operacion_x", "Operacion", p=prov("1.3")),
        nodo("Sujeto_clase_a", "Sujeto", props={"nivel": "clase"}, p=prov_esqueleto()),
        nodo("Sujeto_rol_r", "Sujeto", props={"nivel": "rol"}, p=prov_esqueleto()),
        nodo("Sujeto_propuesto_p", "Sujeto",
             props={"nivel": "propuesto", "cuarentena": "true", "padre_sugerido": "Sujeto_clase_a"},
             p=prov("1.4")),
        nodo("Comunicacion_c", "Comunicacion", p=prov("1.5")),
    ]
    edges = [
        arista("Obligacion_a", "TextoOrdenado_test", "establecida_en", p=prov("1.1")),
        arista("Obligacion_b", "TextoOrdenado_test", "establecida_en", p=prov("1.2")),
        arista("Operacion_x", "TextoOrdenado_test", "establecida_en", p=prov("1.3")),
        arista("Obligacion_a", "Sujeto_clase_a", "aplica_a", p=prov("1.1")),
        arista("Obligacion_b", "Sujeto_clase_a", "aplica_a", p=prov("1.2")),
        arista("Operacion_x", "Sujeto_clase_a", "aplica_a", p=prov("1.3")),
        arista("Obligacion_a", "Operacion_x", "regula", p=prov("1.1")),
        arista("Sujeto_clase_a", "Sujeto_rol_r", "miembro_de", p=prov_esqueleto(), rol_fuente="esqueleto"),
        arista("Sujeto_propuesto_p", "Sujeto_clase_a", sv.RELACION_PADRE_SUGERIDO, p=prov("1.4"),
               rol_fuente="cuarentena_flaggeada", properties={"flag": "padre_sugerido_no_laudado"}),
        arista("Obligacion_a", "Obligacion_b", "referencia", p=prov("1.1"),
               rol_fuente=sv.ROL_FUENTE_REFERENCIA_CRUZADA,
               properties={"destino": "tst::1.2", "via": "nodos_del_punto", "clase": "interna"}),
        arista("TextoOrdenado_test", "Comunicacion_c", "referencia", p=prov("1.5")),
    ]
    return {"nodes": nodes, "edges": edges}


CATALOGO = {
    "version": "test",
    "clases": [{"id": "Sujeto_clase_a", "nivel": "clase"}],
    "roles": [{"id": "Sujeto_rol_r", "nivel": "rol", "miembros": ["Sujeto_clase_a"]}],
    "excepciones_s15": {"total": 0, "por_causa": {}, "roles": []},
}


def nodo_por_id(g, nid):
    return next(n for n in g["nodes"] if n["id"] == nid)


def arista_por(g, rel, source=None):
    return next(e for e in g["edges"] if e["relation"] == rel and (source is None or e["source"] == source))


# --------------------------------------------------------------------------- #
# Arnés                                                                       #
# --------------------------------------------------------------------------- #
CASOS = []          # (nombre, ok, detalle)


def caso(nombre):
    def deco(fn):
        try:
            fn()
            CASOS.append((nombre, True, ""))
        except Exception:
            CASOS.append((nombre, False, traceback.format_exc()))
        return fn
    return deco


def evaluar(g, excepciones_ruta):
    return sv.evaluar_perfil_congelado(g, VOCAB, excepciones_ruta)


TMP = tempfile.mkdtemp(prefix="selftest_shapes_congelado_")
RUTA_CATALOGO = os.path.join(TMP, "catalogo_test.json")
with open(RUTA_CATALOGO, "w", encoding="utf-8") as _f:
    json.dump(CATALOGO, _f, ensure_ascii=False, indent=1)


def espera_bloqueante_fail(g, rid, contiene=None):
    res, ver, meta = evaluar(g, RUTA_CATALOGO)
    assert res[rid]["result"] == "FAIL", f"{rid} esperaba FAIL, dio {res[rid]['result']}: {res[rid]['resumen']}"
    assert ver == "NO PASA", f"veredicto esperaba NO PASA, dio {ver}"
    assert rid in meta["bloqueantes_en_fail"], meta["bloqueantes_en_fail"]
    otros = [r for r in meta["bloqueantes_en_fail"] if r != rid]
    assert not otros, f"el contraejemplo de {rid} rompió también {otros}"
    if contiene:
        assert any(contiene in d for d in res[rid]["detalle_md"]), \
            f"{rid}: ningún detalle contiene {contiene!r}: {res[rid]['detalle_md'][:3]}"
    return res


def espera_informativa(g, rid, result, conteo_clave, conteo_valor):
    res, ver, meta = evaluar(g, RUTA_CATALOGO)
    assert res[rid]["result"] == result, f"{rid} esperaba {result}, dio {res[rid]['result']}: {res[rid]['resumen']}"
    assert ver == "PASA", f"una informativa no puede cambiar el veredicto (dio {ver}; {meta})"
    assert res[rid]["conteos"][conteo_clave] == conteo_valor, \
        f"{rid}.{conteo_clave} esperaba {conteo_valor}, dio {res[rid]['conteos'][conteo_clave]}"
    return res


# --------------------------------------------------------------------------- #
# Casos                                                                       #
# --------------------------------------------------------------------------- #
@caso("base: todas las bloqueantes PASS, informativas en 0, veredicto PASA")
def _():
    res, ver, meta = evaluar(grafo_base(), RUTA_CATALOGO)
    assert ver == "PASA", (ver, meta, {r: res[r]["resumen"] for r in meta["bloqueantes_en_fail"]})
    for rid in sv.BLOQUEANTES_CONGELADO:
        assert res[rid]["result"] == "PASS", (rid, res[rid]["resumen"])
    for rid in sv.INFORMATIVAS_CONGELADO:
        assert res[rid]["result"] == "PASS", (rid, res[rid]["resumen"])
    assert list(res) == sv.ORDEN_SHAPES_CONGELADO


@caso("vocabulario: 9 tipos, 13 predicados, enum de 6, requisito_de_estructura retirado")
def _():
    assert len(VOCAB["entity_types"]) == 9
    assert len(VOCAB["predicates"]) == 13
    assert len(VOCAB["obligacion_tipo"]) == 6
    assert "requisito_de_estructura" in VOCAB["retirados"]
    assert "requisito_de_estructura" not in VOCAB["obligacion_tipo"]
    assert VOCAB["sha256_prefijo"] == sv.SHA256_PREFIJO_CONGELADO_ESPERADO


@caso("candado: un sha esperado distinto FRENA (CandadoShaError)")
def _():
    try:
        sv.cargar_vocabulario_congelado(sha_esperado="0" * 64)
    except sv.CandadoShaError:
        return
    raise AssertionError("el candado no frenó con un sha esperado distinto")


@caso("candado: un módulo inexistente FRENA (VocabularioCongeladoError)")
def _():
    try:
        sv.cargar_vocabulario_congelado(ruta=os.path.join(TMP, "no_existe.py"))
    except sv.VocabularioCongeladoError:
        return
    raise AssertionError("no frenó con un módulo inexistente")


# ---- S1 ----
@caso("S1 pasa: esqueleto, padre_sugerido y los 13 predicados son admitidos")
def _():
    res, _, _ = evaluar(grafo_base(), RUTA_CATALOGO)
    assert res["S1"]["result"] == "PASS"
    assert res["S1"]["conteos"]["relaciones_admitidas"] == 13 + 4 + 1


@caso("S1 falla: relación fuera del vocabulario")
def _():
    g = grafo_base()
    g["edges"].append(arista("Obligacion_a", "Operacion_x", "vinculada_con"))
    espera_bloqueante_fail(g, "S1", "vinculada_con")


# ---- S2 ----
@caso("S2 pasa: sin aristas colgantes")
def _():
    res, _, _ = evaluar(grafo_base(), RUTA_CATALOGO)
    assert res["S2"]["result"] == "PASS" and res["S2"]["conteos"]["colgantes"] == 0


@caso("S2 falla: arista hacia un nodo inexistente")
def _():
    g = grafo_base()
    g["edges"].append(arista("Obligacion_a", "Nodo_inexistente", "regula"))
    espera_bloqueante_fail(g, "S2", "Nodo_inexistente")


# ---- S3 ----
@caso("S3 pasa: matriz congelada + esqueleto + referencia cruzada + padre_sugerido")
def _():
    res, _, _ = evaluar(grafo_base(), RUTA_CATALOGO)
    c = res["S3"]["conteos"]
    assert res["S3"]["result"] == "PASS"
    assert c["referencias_cruzadas_admitidas"] == 1 and c["evaluadas_esqueleto"] == 1 \
        and c["evaluadas_padre_sugerido"] == 1


@caso("S3 falla: aplica_a hacia un no-Sujeto (matriz)")
def _():
    g = grafo_base()
    g["edges"].append(arista("Obligacion_a", "Operacion_x", "aplica_a"))
    espera_bloqueante_fail(g, "S3", "matriz congelada")


@caso("S3 falla: esqueleto entre no-Sujetos")
def _():
    g = grafo_base()
    g["edges"].append(arista("Obligacion_a", "Obligacion_b", "subclase_de"))
    espera_bloqueante_fail(g, "S3", "esqueleto solo Sujeto->Sujeto")


@caso("S3 falla: referencia nodo->nodo SIN rol_fuente=referencia_cruzada cae en la matriz")
def _():
    g = grafo_base()
    g["edges"].append(arista("Obligacion_a", "Obligacion_b", "referencia"))
    espera_bloqueante_fail(g, "S3", "referencia Obligacion")


@caso("S3 falla: padre_sugerido desde un Sujeto no propuesto")
def _():
    g = grafo_base()
    g["edges"].append(arista("Sujeto_clase_a", "Sujeto_rol_r", sv.RELACION_PADRE_SUGERIDO))
    espera_bloqueante_fail(g, "S3", "padre_sugerido solo propuesto")


@caso("S3 falla: padre_sugerido hacia un Sujeto propuesto")
def _():
    g = grafo_base()
    g["nodes"].append(nodo("Sujeto_propuesto_q", "Sujeto",
                           props={"nivel": "propuesto", "cuarentena": "true", "padre_sugerido": "Sujeto_propuesto_p"}))
    g["edges"].append(arista("Sujeto_propuesto_q", "Sujeto_propuesto_p", sv.RELACION_PADRE_SUGERIDO))
    espera_bloqueante_fail(g, "S3", "Sujeto_propuesto_q -> Sujeto_propuesto_p")


# ---- S4 ----
@caso("S4 pasa: provenance g3 con esqueleto de to nulo admitido")
def _():
    res, _, _ = evaluar(grafo_base(), RUTA_CATALOGO)
    assert res["S4"]["result"] == "PASS" and res["S4"]["conteos"]["violaciones"] == 0


@caso("S4 falla: falta la clave rol_documental")
def _():
    g = grafo_base()
    n = nodo_por_id(g, "Obligacion_a")
    del n["provenance"]["rol_documental"]
    del n["provenances"][0]["rol_documental"]
    espera_bloqueante_fail(g, "S4", "faltan claves ['rol_documental']")


@caso("S4 falla: to nulo en un rol_documental distinto de esqueleto")
def _():
    g = grafo_base()
    n = nodo_por_id(g, "Obligacion_a")
    n["provenance"]["to"] = None
    n["provenances"][0]["to"] = None
    espera_bloqueante_fail(g, "S4", "to vacío o no-string")


@caso("S4 falla: provenances vacía")
def _():
    g = grafo_base()
    nodo_por_id(g, "Obligacion_a")["provenances"] = []
    espera_bloqueante_fail(g, "S4", "provenances vacía")


@caso("S4 falla: provenance != provenances[0] (en una arista)")
def _():
    g = grafo_base()
    e = arista_por(g, "regula")
    e["provenances"] = [prov("9.9")]
    espera_bloqueante_fail(g, "S4", "provenance != provenances[0]")


# ---- S5 ----
@caso("S5 pasa: todos los punto no vacíos")
def _():
    res, _, _ = evaluar(grafo_base(), RUTA_CATALOGO)
    assert res["S5"]["result"] == "PASS"


@caso("S5 falla: punto vacío")
def _():
    g = grafo_base()
    n = nodo_por_id(g, "Operacion_x")
    n["provenance"]["punto"] = ""
    n["provenances"][0]["punto"] = ""
    espera_bloqueante_fail(g, "S5", "Operacion_x")


# ---- S6 ----
@caso("S6 pasa: archivos = TextoOrdenado ∪ esqueleto, sin nada codificado")
def _():
    res, _, _ = evaluar(grafo_base(), RUTA_CATALOGO)
    assert res["S6"]["result"] == "PASS"
    assert res["S6"]["conteos"]["archivos_texto_ordenado"] == 1
    assert res["S6"]["conteos"]["archivos_esqueleto_adicionales"] == 1


@caso("S6 falla: archivo que no es de ningún TextoOrdenado ni de esqueleto")
def _():
    g = grafo_base()
    n = nodo_por_id(g, "Operacion_x")
    n["provenance"]["archivo"] = "TO_otro.pdf"
    n["provenances"][0]["archivo"] = "TO_otro.pdf"
    espera_bloqueante_fail(g, "S6", "TO_otro.pdf")


# ---- S15 ----
@caso("S15 pasa: rol con miembro_de de una clase; lista declarada 0 = huérfanos 0")
def _():
    res, _, _ = evaluar(grafo_base(), RUTA_CATALOGO)
    assert res["S15"]["result"] == "PASS" and res["S15"]["conteos"]["huerfanos"] == 0


@caso("S15 falla: rol huérfano no declarado")
def _():
    g = grafo_base()
    g["edges"] = [e for e in g["edges"] if e["relation"] != "miembro_de"]
    espera_bloqueante_fail(g, "S15", "rol huérfano NO declarado: Sujeto_rol_r")


# ---- S19 ----
@caso("S19 pasa: clase y rol en catálogo, propuesto con cuarentena y padre_sugerido")
def _():
    res, _, _ = evaluar(grafo_base(), RUTA_CATALOGO)
    assert res["S19"]["result"] == "PASS" and res["S19"]["conteos"]["catalogo_ids"] == 2


@caso("S19 falla: Sujeto clase fuera del catálogo")
def _():
    g = grafo_base()
    g["nodes"].append(nodo("Sujeto_clase_fuera", "Sujeto", props={"nivel": "clase"}, p=prov_esqueleto()))
    espera_bloqueante_fail(g, "S19", "Sujeto_clase_fuera (nivel clase): id fuera del catálogo")


@caso("S19 falla: nivel inválido")
def _():
    g = grafo_base()
    # Sujeto aislado (sin aristas) para que el nivel inválido no arrastre S3/S15.
    g["nodes"].append(nodo("Sujeto_raro", "Sujeto", props={"nivel": "categoria"}, p=prov_esqueleto()))
    espera_bloqueante_fail(g, "S19", "Sujeto_raro: nivel='categoria'")


@caso("S19 falla: propuesto sin padre_sugerido")
def _():
    g = grafo_base()
    del nodo_por_id(g, "Sujeto_propuesto_p")["properties"]["padre_sugerido"]
    # la arista padre_sugerido queda incoherente (S22, informativa); la bloqueante es S19
    espera_bloqueante_fail(g, "S19", "sin properties.padre_sugerido")


@caso("S19 falla: sin --excepciones el catálogo es vacío")
def _():
    res, ver, meta = evaluar(grafo_base(), None)
    assert res["S19"]["result"] == "FAIL" and ver == "NO PASA"
    assert res["S19"]["conteos"]["fuera_de_catalogo"] == 2
    assert "no se pasó --excepciones" in (res["S19"]["conteos"]["catalogo_defecto"] or "")


# ---- S20 ----
@caso("S20 pasa: tipos dentro del enum congelado")
def _():
    res, _, _ = evaluar(grafo_base(), RUTA_CATALOGO)
    assert res["S20"]["result"] == "PASS"
    assert res["S20"]["conteos"]["retirados"]["total"] == 0
    assert res["S20"]["conteos"]["otros_fuera_del_enum"]["total"] == 0


@caso("S20 falla: valor RETIRADO (requisito_de_estructura) se cuenta como retirado")
def _():
    g = grafo_base()
    nodo_por_id(g, "Obligacion_a")["properties"]["tipo"] = "requisito_de_estructura"
    res = espera_bloqueante_fail(g, "S20", "valor RETIRADO")
    assert res["S20"]["conteos"]["retirados"]["total"] == 1
    assert res["S20"]["conteos"]["otros_fuera_del_enum"]["total"] == 0


@caso("S20 falla: otro valor fuera del enum se cuenta aparte")
def _():
    g = grafo_base()
    nodo_por_id(g, "Obligacion_b")["properties"]["tipo"] = "verificacion_informativa"
    res = espera_bloqueante_fail(g, "S20", "fuera del enum")
    assert res["S20"]["conteos"]["retirados"]["total"] == 0
    assert res["S20"]["conteos"]["otros_fuera_del_enum"]["total"] == 1


@caso("S20 falla: tipo ausente cuenta como otro valor fuera del enum")
def _():
    g = grafo_base()
    del nodo_por_id(g, "Obligacion_b")["properties"]["tipo"]
    res = espera_bloqueante_fail(g, "S20", "tipo=None")
    assert res["S20"]["conteos"]["otros_fuera_del_enum"]["total"] == 1


# ---- S7 ----
@caso("S7 pasa: (type, label) únicos")
def _():
    res, _, _ = evaluar(grafo_base(), RUTA_CATALOGO)
    assert res["S7"]["result"] == "PASS"


@caso("S7 falla (informativa): duplicado exacto no cambia el veredicto")
def _():
    g = grafo_base()
    g["nodes"].append(nodo("Operacion_x2", "Operacion", label="Operacion_x", p=prov("1.3")))
    g["edges"].append(arista("Operacion_x2", "TextoOrdenado_test", "establecida_en", p=prov("1.3")))
    g["edges"].append(arista("Operacion_x2", "Sujeto_clase_a", "aplica_a", p=prov("1.3")))
    espera_informativa(g, "S7", "FAIL", "grupos", 1)


# ---- S8 ----
@caso("S8 pasa: sin colisión de label entre types")
def _():
    res, _, _ = evaluar(grafo_base(), RUTA_CATALOGO)
    assert res["S8"]["result"] == "PASS"


@caso("S8 WARN (informativa): mismo label en dos types")
def _():
    g = grafo_base()
    nodo_por_id(g, "Operacion_x")["label"] = "Obligacion_a"
    espera_informativa(g, "S8", "WARN", "grupos", 1)


# ---- S9 ----
@caso("S9 pasa: ningún nodo con 'descripcion' y 'description' a la vez")
def _():
    res, _, _ = evaluar(grafo_base(), RUTA_CATALOGO)
    assert res["S9"]["result"] == "PASS" and res["S9"]["conteos"]["nodos_con_ambas_keys"] == 0


@caso("S9 falla (informativa): nodo con ambas keys, veredicto intacto")
def _():
    g = grafo_base()
    nodo_por_id(g, "Obligacion_a")["properties"].update({"descripcion": "x", "description": "y"})
    espera_informativa(g, "S9", "FAIL", "nodos_con_ambas_keys", 1)


# ---- S10 ----
@caso("S10 pasa: todo el dominio congelado de establecida_en tiene establecida_en")
def _():
    res, _, _ = evaluar(grafo_base(), RUTA_CATALOGO)
    assert res["S10"]["result"] == "PASS"
    assert "Operacion" in res["S10"]["conteos"]["por_tipo"], "S10 debe extenderse al dominio congelado"


@caso("S10 falla (informativa): Operacion sin establecida_en, veredicto intacto")
def _():
    g = grafo_base()
    g["edges"] = [e for e in g["edges"] if not (e["relation"] == "establecida_en" and e["source"] == "Operacion_x")]
    res = espera_informativa(g, "S10", "FAIL", "total_sin_establecida_en", 1)
    assert res["S10"]["conteos"]["por_tipo"]["Operacion"] == 1


# ---- S11 ----
@caso("S11 pasa: todo el dominio congelado de aplica_a tiene aplica_a")
def _():
    res, _, _ = evaluar(grafo_base(), RUTA_CATALOGO)
    assert res["S11"]["result"] == "PASS"
    assert "Excepcion" in res["S11"]["conteos"]["por_tipo"], "S11 debe extenderse al dominio congelado"


@caso("S11 WARN (informativa): Operacion sin aplica_a, veredicto intacto")
def _():
    g = grafo_base()
    g["edges"] = [e for e in g["edges"] if not (e["relation"] == "aplica_a" and e["source"] == "Operacion_x")]
    espera_informativa(g, "S11", "WARN", "total_sin_aplica_a", 1)


# ---- S12 ----
@caso("S12 pasa: sin Excepciones huérfanas")
def _():
    res, _, _ = evaluar(grafo_base(), RUTA_CATALOGO)
    assert res["S12"]["result"] == "PASS"


@caso("S12 falla (informativa): Excepcion sin exceptua, veredicto intacto")
def _():
    g = grafo_base()
    g["nodes"].append(nodo("Excepcion_e", "Excepcion", p=prov("1.6")))
    g["edges"].append(arista("Excepcion_e", "TextoOrdenado_test", "establecida_en", p=prov("1.6")))
    g["edges"].append(arista("Excepcion_e", "Sujeto_clase_a", "aplica_a", p=prov("1.6")))
    espera_informativa(g, "S12", "FAIL", "excepciones_sin_salida", 1)


# ---- S21 ----
@caso("S21 pasa: destino sin prefijo <to>:: está en el conjunto de puntos del destino")
def _():
    res, _, _ = evaluar(grafo_base(), RUTA_CATALOGO)
    assert res["S21"]["result"] == "PASS" and res["S21"]["conteos"]["referencias_cruzadas"] == 1


@caso("S21 pasa: coincidencia con provenances[1] (conjunto, no provenance[0])")
def _():
    g = grafo_base()
    nodo_por_id(g, "Obligacion_b")["provenances"].append(prov("1.9"))
    arista_por(g, "referencia", "Obligacion_a")["properties"]["destino"] = "tst::1.9"
    espera_informativa(g, "S21", "PASS", "incoherentes", 0)


@caso("S21 WARN (informativa): destino fuera del conjunto, desglosado por via")
def _():
    g = grafo_base()
    arista_por(g, "referencia", "Obligacion_a")["properties"]["destino"] = "tst::7.7"
    res = espera_informativa(g, "S21", "WARN", "incoherentes", 1)
    assert res["S21"]["conteos"]["incoherentes_por_via"] == {"nodos_del_punto": 1}


# ---- S22 ----
@caso("S22 pasa: padre_sugerido coherente con el origen en cuarentena")
def _():
    res, _, _ = evaluar(grafo_base(), RUTA_CATALOGO)
    assert res["S22"]["result"] == "PASS" and res["S22"]["conteos"]["aristas_padre_sugerido"] == 1


@caso("S22 WARN (informativa): destino distinto de properties.padre_sugerido")
def _():
    g = grafo_base()
    nodo_por_id(g, "Sujeto_propuesto_p")["properties"]["padre_sugerido"] = "Sujeto_rol_r"
    res = espera_informativa(g, "S22", "WARN", "incoherentes", 1)
    assert res["S22"]["conteos"]["destino_distinto"] == 1


@caso("S22 WARN (informativa): origen fuera de cuarentena")
def _():
    g = grafo_base()
    nodo_por_id(g, "Sujeto_propuesto_p")["properties"]["cuarentena"] = "false"
    res = espera_informativa(g, "S22", "WARN", "incoherentes", 1)
    assert res["S22"]["conteos"]["origen_sin_cuarentena"] == 1


# ---- S23 ----
@caso("S23 pasa: ningún aplica_a hacia propuestos")
def _():
    res, _, _ = evaluar(grafo_base(), RUTA_CATALOGO)
    assert res["S23"]["result"] == "PASS" and res["S23"]["conteos"]["aplica_a"] == 3


@caso("S23 WARN (informativa): aplica_a hacia un Sujeto propuesto, nunca bloqueante")
def _():
    g = grafo_base()
    g["edges"].append(arista("Obligacion_a", "Sujeto_propuesto_p", "aplica_a", p=prov("1.1")))
    res = espera_informativa(g, "S23", "WARN", "hacia_propuestos", 1)
    assert res["S3"]["result"] == "PASS", "aplica_a hacia Sujeto propuesto es válido por firma"


# ---- CLI ----
def correr_cli(g, *extra):
    ruta_kg = os.path.join(TMP, "kg_cli.json")
    with open(ruta_kg, "w", encoding="utf-8") as f:
        json.dump(g, f, ensure_ascii=False)
    ruta_out = os.path.join(TMP, "reporte_cli.md")
    for r in (ruta_out, os.path.splitext(ruta_out)[0] + ".json"):
        if os.path.exists(r):
            os.remove(r)
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    p = subprocess.run([sys.executable, RUTA_VALIDADOR, "--kg", ruta_kg, "--out", ruta_out, *extra],
                       capture_output=True, text=True, env=env)
    return p, ruta_out, os.path.splitext(ruta_out)[0] + ".json"


@caso("CLI: --perfil congelado sobre el base -> exit 0, .md y .json con veredicto PASA")
def _():
    p, md, js = correr_cli(grafo_base(), "--perfil", "congelado", "--excepciones", RUTA_CATALOGO)
    assert p.returncode == 0, (p.returncode, p.stdout[-800:], p.stderr[-800:])
    assert os.path.exists(md) and os.path.exists(js)
    with open(js, encoding="utf-8") as f:
        d = json.load(f)
    assert d["veredicto"] == "PASA" and d["perfil"] == "congelado"
    assert set(d["shapes"]) == set(sv.ORDEN_SHAPES_CONGELADO)
    assert d["vocabulario"]["sha256_prefijo"] == sv.SHA256_PREFIJO_CONGELADO_ESPERADO
    assert "VEREDICTO GLOBAL: PASA" in p.stdout


@caso("CLI: --perfil congelado con bloqueante en FAIL -> exit 1, .json NO PASA")
def _():
    g = grafo_base()
    g["edges"].append(arista("Obligacion_a", "Operacion_x", "vinculada_con"))
    p, md, js = correr_cli(g, "--perfil", "congelado", "--excepciones", RUTA_CATALOGO)
    assert p.returncode == 1, (p.returncode, p.stderr[-800:])
    with open(js, encoding="utf-8") as f:
        d = json.load(f)
    assert d["veredicto"] == "NO PASA" and d["bloqueantes_en_fail"] == ["S1"]


@caso("CLI: sin --perfil el código de salida sigue siendo 0 y no se escribe .json")
def _():
    g = grafo_base()
    g["edges"].append(arista("Obligacion_a", "Operacion_x", "vinculada_con"))
    p, md, js = correr_cli(g, "--excepciones", RUTA_CATALOGO)
    assert p.returncode == 0, (p.returncode, p.stderr[-800:])
    assert os.path.exists(md) and not os.path.exists(js)
    assert "S15" in p.stdout and "VEREDICTO" not in p.stdout


# --------------------------------------------------------------------------- #
# Salida                                                                      #
# --------------------------------------------------------------------------- #
def main():
    fallas = [(n, d) for n, ok, d in CASOS if not ok]
    for n, ok, d in CASOS:
        print(f"[{'ok ' if ok else 'FAIL'}] {n}")
        if not ok:
            print("      " + d.strip().replace("\n", "\n      "))
    print(f"\n{len(CASOS)} casos: {len(CASOS) - len(fallas)} ok, {len(fallas)} fallas")
    print(f"vocabulario: {VOCAB['modulo']} (sha256 prefijo {VOCAB['sha256_prefijo']})")
    # limpieza del temporal
    for raiz, dirs, archivos in os.walk(TMP, topdown=False):
        for a in archivos:
            os.remove(os.path.join(raiz, a))
        for d in dirs:
            os.rmdir(os.path.join(raiz, d))
    os.rmdir(TMP)
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(main())
