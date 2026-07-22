"""Tests unitarios de s1_fuentes.py (S1). Sin API: el fetch se prueba con kg sintético
(provenances apuntando al corpus REAL read-only, para verificar contra localize de verdad)
y aplicar_s1 se prueba con el LLM MOCKEADO (respuestas inyectadas)."""

import copy
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from harness import GraphIndex
from loader import Node, KnowledgeGraph
from pdf_locate import localize
from s1_fuentes import (S1_VERSION, CAUSAS_GATILLO_S1, DOCS_CORPUS,
                        construir_paquete_fuentes, aplicar_s1, _comparativos_de_punto,
                        _referencias_de_pasaje, _comparativo_de_referencia,
                        _extraer_portador_s1)


# --------------------------------------------------------------------------- #
# Fixtures                                                                     #
# --------------------------------------------------------------------------- #
DOC_CAP = "TO_capitales_minimos_actual.pdf"
DOC_EXT = "TO_exterior_cambios_actual.pdf"


def _kg_s1():
    """Grafo sintético con provenances REALES (corpus read-only) y casos de estado."""
    nodes = [
        # portador con provenance parseable de 2 niveles (el 12.3 del piloto CQ-033)
        Node(id="restriccion_12_3", type="Restriccion",
             label="Límite exigencia capital operacional grupo B",
             properties={"valor": "17% del promedio"},
             provenances=[{"source_doc": DOC_CAP,
                           "location": "Punto 12.3. Para aquellas entidades financieras "
                                       "que sean reclasificadas desde el 01/01/2026"}]),
        # portador con provenance parseable de 3 niveles (ejercita el punto general)
        Node(id="restriccion_3_9_1", type="Restriccion",
             label="Límite mensual USD 200",
             properties={"valor": "USD 200 por mes calendario"},
             provenances=[{"source_doc": DOC_EXT, "location": "Punto 3.9.1."}]),
        # portador de 3 niveles con cadena de localización COMPLETA ok en el corpus
        # real (sondeado: CAP 2, 2.3 y 2.3.1 localizan ok) — para los tests del juicio S1
        Node(id="restriccion_2_3_1", type="Restriccion",
             label="Cómputo de la exigencia",
             properties={"valor": "base individual y consolidada mensual"},
             provenances=[{"source_doc": DOC_CAP, "location": "Punto 2.3.1."}]),
        # portador cuya localización FALLA en el corpus real (el 3.9.1 no existe en
        # Capitales — sondeado: localize fallida) — para el test de bloqueo por portador
        Node(id="nodo_portador_fallido", type="Restriccion",
             label="Portador ilocalizable",
             properties={}, provenances=[{"source_doc": DOC_CAP, "location": "Punto 3.9.1."}]),
        # anidación de ids (B4.2): "comision" ⊂ "comision_por_precancelacion"
        Node(id="comision", type="Concepto", label="Comisión",
             properties={}, provenances=[{"source_doc": DOC_CAP, "location": "Punto 2.3.1."}]),
        Node(id="comision_por_precancelacion", type="Restriccion",
             label="Comisión por precancelación",
             properties={"criterio": "cuarta parte del plazo o 180 días"},
             provenances=[{"source_doc": DOC_CAP, "location": "Punto 2.3.1."}]),
        # cascada de provenances (B4.2): la 1ª parsea pero NO localiza; la 2ª localiza
        Node(id="nodo_cascada", type="Restriccion", label="Cascada",
             properties={}, provenances=[{"source_doc": DOC_CAP, "location": "Punto 3.9.1."},
                                         {"source_doc": DOC_CAP, "location": "Punto 2.3.1."}]),
        # cascada donde NINGUNA provenance localiza
        Node(id="nodo_cascada_fallida", type="Restriccion", label="Cascada fallida",
             properties={}, provenances=[{"source_doc": DOC_CAP, "location": "Punto 3.9.1."},
                                         {"source_doc": DOC_CAP, "location": "Punto 3.9.2."}]),
        # portador con provenance NO parseable
        Node(id="nodo_encabezado", type="Concepto", label="Encabezado general",
             properties={}, provenances=[{"source_doc": DOC_CAP, "location": "Encabezado"}]),
        # portador sin provenances
        Node(id="nodo_sin_prov", type="Concepto", label="Sin provenance",
             properties={}, provenances=[]),
    ]
    return GraphIndex(KnowledgeGraph(run_key="sintetico", path=Path("<memoria>"),
                                     nodes=nodes, edges=[]))


def _atrib(causa, ubicacion, sintoma="noise_sensitivity", jerarquia="primaria"):
    return {
        "sintoma_capa1": sintoma, "causa_capa2": causa, "lado": "?",
        "jerarquia": jerarquia, "pata": "pata de prueba",
        "evidencia": {
            "afirmacion": {"quote": "afirmación x", "ubicacion": "respuesta final"},
            "nodo": {"quote": "nodo y", "ubicacion": ubicacion},
            "fuente": {"quote": "fuente z", "ubicacion": "pdf"},
        },
    }


def _caso(reps_atribs, ganadores=None):
    """caso_json con la forma de una salida _capa_d (voto_capa_d presente)."""
    return {
        "id_falla": "sintetico/CQ-000", "run": "sintetico", "n_reps": len(reps_atribs),
        "voto": {"resultado": "mayoria", "marca": "VOTO_ORIGINAL"},
        "repeticiones": [
            {"formato_invalido": False, "errores_formato": [], "atribuciones": atribs}
            for atribs in reps_atribs
        ],
        "voto_capa_d": {"resultado": "mayoria", "flag_voto_dividido": False,
                        "pares_primarios_ganadores":
                            ganadores if ganadores is not None
                            else [["noise_sensitivity", "contenido_kg"]],
                        "marca": "VOTO_CAPA_D"},
    }


def _fetch(caso, F=None, P=None):
    return construir_paquete_fuentes(caso, _kg_s1(),
                                     sintoma_F=F if F is not None else [],
                                     sintoma_P=P if P is not None else [])


# --------------------------------------------------------------------------- #
# 1. Fetch — portador parseable, pasaje y comparativos (contra localize REAL)  #
# --------------------------------------------------------------------------- #
def test_fetch_portador_dos_niveles_madre_omitida_y_referencias():
    caso = _caso([[_atrib("contenido_kg", "restriccion_12_3 (paso 3)")]])
    e = _fetch(caso)["atribuciones"][0]
    assert e["portador_id"] == "restriccion_12_3"
    assert e["punto_parseado"] == "12.3"
    assert e["pasaje_portador"]["localizacion_pdf"] == "ok"
    # el pasaje ARRANCA en el encabezado con la declaración de alcance
    assert e["pasaje_portador"]["pasaje"].startswith("12.3. Para aquellas entidades")
    # política NO BLOQUEANTE: portador ok → completo (aunque haya comparativos fallidos)
    assert e["estado"] == "completo"
    # madre nivel-1: SIEMPRE omitida con la nota fija, sin llamada a localize
    madre = [c for c in e["comparativos"] if c["tipo"] == "seccion_madre"]
    assert len(madre) == 1 and madre[0]["estado"] == "omitido"
    assert "carátula sin prosa" in madre[0]["nota"]
    assert "reporte_b3_s1.md hecho b" in madre[0]["nota"]
    assert "localizacion_pdf" not in madre[0]
    assert any("padre_inmediato_coincide" in n for n in e["notas_regla"])
    # referencias internas: la mención "punto 7.2" del pasaje queda capturada, tope 3
    refs = [c for c in e["comparativos"] if c["tipo"] == "referencia_interna"]
    assert 1 <= len(refs) <= 3
    assert "7.2" in [c["punto"] for c in refs]
    ref72 = next(c for c in refs if c["punto"] == "7.2")
    assert "punto 7.2" in ref72["mencion_verbatim"].lower()
    assert ref72["regla"] == "referencia_interna" and ref72["estado"] == "localizado"
    # estados propios de las intra verificados contra localize real
    for c in refs:
        if c["estado"] == "omitido_fuera_de_corpus":
            assert "localizacion_pdf" not in c    # jamás se llamó a localize
            continue
        real = localize(DOC_CAP, f"Punto {c['punto']}")
        assert c["localizacion_pdf"] == real["localizacion_pdf"]
        assert c["estado"] == ("localizado" if real["localizacion_pdf"] == "ok"
                               else "fallido")


def test_comparativo_no_localizado_no_bloquea():
    # unit: una referencia INTRA que falla localize (el 3.9.1 no existe en Capitales)
    c = _comparativo_de_referencia(
        {"punto": "3.9.1", "mencion_verbatim": "punto 3.9.1.",
         "doc_destino": None, "marcador_verbatim": None}, DOC_CAP)
    assert c["estado"] == "fallido" and c["regla"] == "referencia_interna"
    # paquete: el 12.3 trae comparativos NO localizados (madre omitida + menciones fuera
    # de corpus) y el paquete sigue COMPLETO — la política no bloquea por comparativos
    caso = _caso([[_atrib("contenido_kg", "restriccion_12_3")]])
    e = _fetch(caso)["atribuciones"][0]
    assert any(c["estado"] != "localizado" for c in e["comparativos"])
    assert e["estado"] == "completo"


def test_marcador_cross_doc_resuelve_en_el_documento_correcto():
    texto = "conforme al punto 6.5. del TO sobre Clasificación de Deudores, aplica"
    refs = _referencias_de_pasaje(texto)
    assert len(refs) == 1
    assert refs[0]["doc_destino"] == "TO_clasificacion_deudores_actual.pdf"
    assert refs[0]["marcador_verbatim"].startswith("del TO sobre Clasificación")
    c = _comparativo_de_referencia(refs[0], DOC_CAP)
    assert c["regla"] == "referencia_interna_cross_doc"
    assert c["doc_destino"] == "TO_clasificacion_deudores_actual.pdf"
    assert c["source_doc"] == "TO_clasificacion_deudores_actual.pdf"  # NO el del portador
    real = localize("TO_clasificacion_deudores_actual.pdf", "Punto 6.5")
    assert c["localizacion_pdf"] == real["localizacion_pdf"] == "ok"
    # variante "de las normas sobre" + des-hifenado de corte de línea
    refs2 = _referencias_de_pasaje(
        "lo previsto en el punto 2.1. de las normas sobre “Régimen informa-\ntivo contable mensual”")
    assert refs2[0]["doc_destino"] == "TO_regimen_informativo_contable_mensual_actual.pdf"


def test_marcador_fuera_de_corpus_jamas_intra():
    texto = ("como consecuencia de lo establecido en el punto 4.1. del TO sobre "
             "Autoridades de Entidades Financie-\nras, la exigencia")
    refs = _referencias_de_pasaje(texto)
    assert refs[0]["doc_destino"] == "fuera_de_corpus"
    c = _comparativo_de_referencia(refs[0], DOC_CAP)
    assert c["estado"] == "omitido_fuera_de_corpus"
    assert "localizacion_pdf" not in c and "pasaje" not in c   # NUNCA intra-documento
    assert "TO sobre Autoridades" in c["marcador_verbatim"]
    assert c["mencion_verbatim"] == "punto 4.1."


def test_marcador_lejano_no_captura():
    relleno = "x" * 120   # el marcador queda FUERA de la ventana fija de 100 chars
    texto = f"ver el punto 5.5. {relleno} del TO sobre Clasificación de Deudores"
    refs = _referencias_de_pasaje(texto)
    assert refs[0]["doc_destino"] is None and refs[0]["marcador_verbatim"] is None
    c = _comparativo_de_referencia(refs[0], DOC_CAP)
    assert c["regla"] == "referencia_interna"     # intra (regresión: sin marcador)
    assert "doc_destino" not in c


def test_portador_fallido_si_bloquea():
    caso = _caso([[_atrib("contenido_kg", "nodo_portador_fallido")]])
    e = _fetch(caso)["atribuciones"][0]
    assert e["estado"] == "localizacion_fallida"
    assert "comparativos" not in e


def test_fetch_portador_tres_niveles_general_localizado_madre_omitida():
    caso = _caso([[_atrib("completitud_kg", "restriccion_3_9_1")]])
    e = _fetch(caso)["atribuciones"][0]
    assert e["punto_parseado"] == "3.9.1"
    assert e["estado"] == "completo"
    tipos = [c["tipo"] for c in e["comparativos"]]
    assert tipos[0] == "seccion_madre" and e["comparativos"][0]["estado"] == "omitido"
    assert tipos[1] == "punto_general_un_nivel_arriba"
    g = e["comparativos"][1]
    assert g["punto"] == "3.9"
    real = localize(DOC_EXT, "Punto 3.9")
    assert g["localizacion_pdf"] == real["localizacion_pdf"]
    assert g["estado"] == ("localizado" if real["localizacion_pdf"] == "ok" else "fallido")
    # las referencias internas del paquete son EXACTAMENTE las del helper sobre el mismo
    # pasaje (consistencia; si el pasaje no tuviera referencias, no habría comparativos
    # de esa fuente)
    refs = [c for c in e["comparativos"] if c["tipo"] == "referencia_interna"]
    esperadas = _referencias_de_pasaje(e["pasaje_portador"]["pasaje"])
    assert [c["punto"] for c in refs] == [r["punto"] for r in esperadas]
    assert [c["mencion_verbatim"] for c in refs] == [r["mencion_verbatim"] for r in esperadas]


def test_referencias_simple_multiple_tope_dedup_y_vacio():
    # simple (sin marcador → intra: doc_destino None)
    assert _referencias_de_pasaje("ver el punto 3.9.1. para más detalle") == \
        [{"punto": "3.9.1", "mencion_verbatim": "punto 3.9.1.",
          "doc_destino": None, "marcador_verbatim": None}]
    # múltiple (enumeración con "y") + tope 3 en orden de aparición
    texto = ("según los puntos 1.2 y 3.4. se aplica lo del punto 5.6, "
             "la Sección 7. y el punto 8.9.")
    refs = _referencias_de_pasaje(texto)
    assert [r["punto"] for r in refs] == ["1.2", "3.4", "5.6"]
    assert refs[0]["mencion_verbatim"] == "puntos 1.2 y 3.4."
    # dedup por (punto, destino) — queda la primera mención
    assert [r["punto"] for r in
            _referencias_de_pasaje("punto 1.2 y de nuevo el punto 1.2.")] == ["1.2"]
    # variante Sección N.
    assert _referencias_de_pasaje("conforme a la Sección 4. del presente") == \
        [{"punto": "4", "mencion_verbatim": "Sección 4.",
          "doc_destino": None, "marcador_verbatim": None}]
    # pasaje sin referencias → vacío (paquete completo sin comparativos de esa fuente)
    assert _referencias_de_pasaje("texto sin menciones normativas de ese tipo") == []
    assert _referencias_de_pasaje("") == []


def test_regla_comparativos_pura():
    comps, notas = _comparativos_de_punto("12.3")
    assert [(c["tipo"], c["punto"]) for c in comps] == [("seccion_madre", "12")]
    comps, notas = _comparativos_de_punto("3.1.11.2")
    assert [(c["tipo"], c["punto"]) for c in comps] == [
        ("seccion_madre", "3"), ("punto_general_un_nivel_arriba", "3.1.11")]
    comps, notas = _comparativos_de_punto("7")
    assert comps == [] and any("sin_comparativos_por_regla" in n for n in notas)


# --------------------------------------------------------------------------- #
# 2. Fetch — estados explícitos                                               #
# --------------------------------------------------------------------------- #
def test_fetch_provenance_no_parseable_estado_explicito():
    caso = _caso([[_atrib("estructural_kg", "nodo_encabezado")]])
    e = _fetch(caso)["atribuciones"][0]
    assert e["estado"] == "provenance_no_parseable"
    assert e["provenances_verbatim"] == [{"source_doc": DOC_CAP, "location": "Encabezado"}]
    assert "pasaje_portador" not in e


def test_fetch_sin_provenances_estado_explicito():
    caso = _caso([[_atrib("contenido_kg", "nodo_sin_prov")]])
    e = _fetch(caso)["atribuciones"][0]
    assert e["estado"] == "provenance_no_parseable" and e["provenances_total"] == 0


def test_fetch_sin_portador_extraible():
    caso = _caso([[_atrib("contenido_kg", "un nodo que no existe en el kg")]])
    e = _fetch(caso)["atribuciones"][0]
    assert e["estado"] == "sin_portador_extraible" and e["portador_id"] is None


# --------------------------------------------------------------------------- #
# 3. Gatillo                                                                   #
# --------------------------------------------------------------------------- #
def test_gatillo_por_causas():
    caso = _caso([[
        _atrib("contenido_kg", "restriccion_12_3"),          # gatilla
        _atrib("navegación", "restriccion_12_3"),            # NO gatilla
        _atrib("alcanzabilidad_kg", "restriccion_12_3"),     # NO gatilla
        _atrib("aplicacion_erronea", "restriccion_12_3"),    # gatilla
        _atrib("sin_defecto", "restriccion_12_3"),           # NO gatilla (voto no vacío)
    ]])
    p = _fetch(caso, F=[{"enunciado": "e", "central": True, "verdict": "falso"}])
    assert [e["causa_capa2"] for e in p["atribuciones"]] == ["contenido_kg",
                                                             "aplicacion_erronea"]
    assert all(e["tipo_gatillo"] == "causa_gatillada" for e in p["atribuciones"])
    assert p["gatillo_caso"]["exoneracion_con_sintoma"] is False


def test_gatillo_exoneracion_con_sintoma():
    caso = _caso([[_atrib("sin_defecto", "restriccion_12_3", jerarquia="sin_par")]],
                 ganadores=[])   # clave ganadora VACÍA
    # con síntoma no vacío → gatilla la sin_defecto
    p = _fetch(caso, F=[{"enunciado": "claim reprobado", "central": True,
                         "verdict": "falso"}])
    assert p["gatillo_caso"]["exoneracion_con_sintoma"] is True
    assert [e["tipo_gatillo"] for e in p["atribuciones"]] == ["exoneracion_con_sintoma"]
    # con síntoma VACÍO → no gatilla nada
    p2 = _fetch(caso, F=[], P=[])
    assert p2["gatillo_caso"]["exoneracion_con_sintoma"] is False
    assert p2["atribuciones"] == []


def test_reps_invalidas_no_gatillan():
    caso = _caso([[_atrib("contenido_kg", "restriccion_12_3")]])
    caso["repeticiones"][0]["formato_invalido"] = True
    assert _fetch(caso)["atribuciones"] == []


def test_fetch_exige_voto_capa_d():
    caso = _caso([[]])
    del caso["voto_capa_d"]
    try:
        _fetch(caso)
        assert False, "debía levantar ValueError"
    except ValueError:
        pass


# --------------------------------------------------------------------------- #
# 4. aplicar_s1 con LLM mockeado                                               #
# --------------------------------------------------------------------------- #
class _MockClient:
    """Cliente mock: devuelve las respuestas inyectadas (texto JSON) en orden."""
    def __init__(self, respuestas):
        self._resp = list(respuestas)
        self.llamadas = []
        self.messages = self

    def create(self, **kw):
        self.llamadas.append(kw)
        texto = self._resp.pop(0)
        class _B:  # bloque de texto mínimo
            def __init__(self, t): self.text = t; self.type = "text"
        class _U:  # usage real de la API (B4.2)
            input_tokens = 1000
            output_tokens = 200
        class _R:
            def __init__(self, t): self.content = [_B(t)]; self.usage = _U()
        return _R(texto)


def _salida_s1(coinciden="no", causa="sin_defecto", sintoma="noise_sensitivity"):
    return json.dumps({
        "alcance_declarado_en_fuente": "Para aquellas entidades financieras que sean "
                                       "reclasificadas desde el 01/01/2026",
        "alcance_en_el_nodo": "Límite exigencia capital operacional grupo B",
        "coinciden": coinciden,
        "sintoma_del_par": sintoma,
        "causa_confirmada_o_corregida": causa,
        "justificacion_breve": "juicio de prueba",
    }, ensure_ascii=False)


def _salida_s1_exon(presente="no", causa="completitud_kg", quote="quote de la fuente"):
    return json.dumps({
        "respuesta_en_fuente": quote,
        "presente_en_grafo": presente,
        "causa_confirmada_o_corregida": causa,
    }, ensure_ascii=False)


def _caso_completo():
    """Caso con atribuciones gatilladas cuyo fetch da estado 'completo': portador 2.3.1 de
    Capitales (localiza ok; con la política B3b, completo = portador localizado)."""
    return _caso([[_atrib("contenido_kg", "restriccion_2_3_1")],
                  [_atrib("contenido_kg", "restriccion_2_3_1")],
                  [_atrib("navegación", "restriccion_12_3")]])


def test_aplicar_s1_corrige_y_preserva_votos():
    caso = _caso_completo()
    paquete = _fetch(caso)
    assert paquete["atribuciones"][0]["estado"] == "completo"  # precondición del mock
    votos_previos = {k: copy.deepcopy(caso[k]) for k in ("voto", "voto_capa_d")}
    client = _MockClient([_salida_s1("no", "sin_defecto"),
                          _salida_s1("no", "sin_defecto")])
    out = aplicar_s1(caso, _kg_s1(), paquete, n=1, client=client)

    a1 = out["repeticiones"][0]["atribuciones"][0]
    assert a1["capa_s1"]["corrigio"] is True
    assert a1["capa_s1"]["emision_v61d"]["causa_capa2"] == "contenido_kg"
    assert a1["causa_capa2"] == "sin_defecto"
    assert a1["capa_s1"]["salidas_s1"][0]["coinciden"] == "no"      # salida íntegra
    # votos previos INTACTOS + voto_s1 recomputado sobre causas post-S1
    assert out["voto"] == votos_previos["voto"]
    assert out["voto_capa_d"] == votos_previos["voto_capa_d"]
    assert out["voto_s1"]["conteo"]
    assert out["version_capa_s1"] == S1_VERSION
    assert out["resumen_s1"]["corregidas"] == 2
    assert out["triage_s1"]["triage"] is False
    # la atribución NO gatillada quedó intacta (sin capa_s1)
    assert "capa_s1" not in out["repeticiones"][2]["atribuciones"][0]
    # el caso de entrada no fue mutado
    assert "capa_s1" not in caso["repeticiones"][0]["atribuciones"][0]


def test_aplicar_s1_no_determinable_triage_y_causa_intacta():
    caso = _caso([[_atrib("contenido_kg", "restriccion_2_3_1")]])
    paquete = _fetch(caso)
    client = _MockClient([_salida_s1("no_determinable", "contenido_kg")])
    out = aplicar_s1(caso, _kg_s1(), paquete, n=1, client=client)
    a = out["repeticiones"][0]["atribuciones"][0]
    assert a["capa_s1"]["accion"] == "no_determinable" and a["capa_s1"]["triage"] is True
    assert a["causa_capa2"] == "contenido_kg"  # intacta: sin mayoría no hay reescritura
    assert out["triage_s1"]["motivos"] == ["fuente_no_verificable"]


def test_aplicar_s1_fetch_fallido_triage_sin_llamadas():
    caso = _caso([[_atrib("contenido_kg", "nodo_encabezado")]])
    paquete = _fetch(caso)
    assert paquete["atribuciones"][0]["estado"] == "provenance_no_parseable"
    out = aplicar_s1(caso, _kg_s1(), paquete, n=1, client=None)  # cero llamadas
    a = out["repeticiones"][0]["atribuciones"][0]
    assert a["capa_s1"]["accion"] == "fuente_no_verificable"
    assert a["capa_s1"]["estado_fetch"] == "provenance_no_parseable"
    assert out["triage_s1"]["motivos"] == ["fuente_no_verificable"]
    assert out["resumen_s1"]["fetch_fallido"] == 1


def test_aplicar_s1_n3_voto_propio():
    caso = _caso([[_atrib("contenido_kg", "restriccion_2_3_1")]])
    paquete = _fetch(caso)
    # 2 votos "sin_defecto" + 1 no_determinable → mayoría 2 ≥ umbral 2
    client = _MockClient([_salida_s1("no", "sin_defecto"),
                          _salida_s1("no_determinable", "contenido_kg"),
                          _salida_s1("no", "sin_defecto")])
    out = aplicar_s1(caso, _kg_s1(), paquete, n=3, client=client)
    a = out["repeticiones"][0]["atribuciones"][0]
    assert a["capa_s1"]["voto_s1_atrib"]["resultado"] == "mayoria"
    assert a["capa_s1"]["voto_s1_atrib"]["votos_ganadores"] == 2
    assert a["causa_capa2"] == "sin_defecto"
    assert len(client.llamadas) == 3
    # 1 decidida + 2 no → sin mayoría
    caso2 = _caso([[_atrib("contenido_kg", "restriccion_2_3_1")]])
    client2 = _MockClient([_salida_s1("no", "sin_defecto"),
                           _salida_s1("no_determinable", "x"),
                           json.dumps({"basura": True})])
    out2 = aplicar_s1(caso2, _kg_s1(), _fetch(caso2), n=3, client=client2)
    a2 = out2["repeticiones"][0]["atribuciones"][0]
    assert a2["capa_s1"]["accion"] == "no_determinable"
    assert a2["capa_s1"]["salidas_s1"][2].get("error", "").startswith("campos_faltantes")


def test_aplicar_s1_confirma_sin_corregir():
    caso = _caso([[_atrib("contenido_kg", "restriccion_2_3_1")]])
    paquete = _fetch(caso)
    client = _MockClient([_salida_s1("no", "contenido_kg")])
    out = aplicar_s1(caso, _kg_s1(), paquete, n=1, client=client)
    a = out["repeticiones"][0]["atribuciones"][0]
    assert a["capa_s1"]["corrigio"] is False and a["causa_capa2"] == "contenido_kg"


# --------------------------------------------------------------------------- #
# 5. Determinismo del fetch                                                    #
# --------------------------------------------------------------------------- #
def test_fetch_deterministico():
    caso = _caso([[_atrib("contenido_kg", "restriccion_12_3"),
                   _atrib("completitud_kg", "restriccion_3_9_1")]])
    p1 = _fetch(caso, F=[{"enunciado": "e", "central": False, "verdict": "falso"}])
    p2 = _fetch(caso, F=[{"enunciado": "e", "central": False, "verdict": "falso"}])
    assert json.dumps(p1, ensure_ascii=False, sort_keys=True) == \
           json.dumps(p2, ensure_ascii=False, sort_keys=True)


# --------------------------------------------------------------------------- #
# 6. B4.2 — maximal, cascada de provenances, usage persistido                  #
# --------------------------------------------------------------------------- #
def test_maximal_unico_resuelve_anidacion():
    ids = ["comision", "comision_por_precancelacion", "restriccion_12_3"]
    a = _atrib("contenido_kg", "comision_por_precancelacion (abierto en paso 3)")
    assert _extraer_portador_s1(a, ids) == ("comision_por_precancelacion", 2)
    # a nivel paquete: gatilla y llega a portador (no sin_portador_extraible)
    caso = _caso([[_atrib("contenido_kg", "comision_por_precancelacion (paso 3)")]])
    e = _fetch(caso)["atribuciones"][0]
    assert e["portador_id"] == "comision_por_precancelacion"
    assert e["n_ids_detectados"] == 2
    assert e["estado"] == "completo"


def test_matches_distintos_siguen_sin_desempate():
    ids = ["restriccion_12_3", "restriccion_3_9_1", "comision"]
    a = _atrib("contenido_kg", "restriccion_12_3 y restriccion_3_9_1 (ambos)")
    assert _extraer_portador_s1(a, ids) == (None, 2)
    caso = _caso([[_atrib("contenido_kg", "restriccion_12_3 y restriccion_3_9_1")]])
    e = _fetch(caso)["atribuciones"][0]
    assert e["estado"] == "sin_portador_extraible" and e["n_ids_detectados"] == 2


def test_cascada_primera_falla_segunda_localiza():
    caso = _caso([[_atrib("contenido_kg", "nodo_cascada")]])
    e = _fetch(caso)["atribuciones"][0]
    assert e["estado"] == "completo"
    assert e["provenance_usada_idx"] == 1
    assert e["punto_parseado"] == "2.3.1"
    ints = e["provenances_intentadas"]
    assert [i["idx"] for i in ints] == [0, 1]
    assert ints[0]["localizacion_pdf"] == "fallida" and ints[1]["localizacion_pdf"] == "ok"


def test_cascada_ninguna_localiza_fallido():
    caso = _caso([[_atrib("contenido_kg", "nodo_cascada_fallida")]])
    e = _fetch(caso)["atribuciones"][0]
    assert e["estado"] == "localizacion_fallida"
    assert len(e["provenances_intentadas"]) == 2
    assert all(i["localizacion_pdf"] == "fallida" for i in e["provenances_intentadas"])
    assert "pasaje_portador" not in e


def test_usage_persistido_en_capa_s1_y_resumen():
    caso = _caso([[_atrib("contenido_kg", "restriccion_2_3_1")]])
    paquete = _fetch(caso)
    client = _MockClient([_salida_s1("no", "sin_defecto")])
    out = aplicar_s1(caso, _kg_s1(), paquete, n=1, client=client)
    a = out["repeticiones"][0]["atribuciones"][0]
    assert a["capa_s1"]["usage_s1"] == [{"input_tokens": 1000, "output_tokens": 200}]
    assert out["resumen_s1"]["tokens_in_s1"] == 1000
    assert out["resumen_s1"]["tokens_out_s1"] == 200


# --------------------------------------------------------------------------- #
# 7. B4.3 — síntoma en el input, sintoma_del_par, rama de exoneración          #
# --------------------------------------------------------------------------- #
def test_input_incluye_sintoma():
    caso = _caso([[_atrib("contenido_kg", "restriccion_2_3_1")]])
    paquete = _fetch(caso)
    client = _MockClient([_salida_s1("no", "contenido_kg")])
    F = [{"enunciado": "el criterio es el que ocurra primero", "central": True,
          "verdict": "falso"}]
    P = ["pata no cubierta de prueba"]
    aplicar_s1(caso, _kg_s1(), paquete, n=1, client=client, sintoma_F=F, sintoma_P=P)
    prompt = client.llamadas[0]["messages"][0]["content"]
    assert "el criterio es el que ocurra primero" in prompt
    assert "pata no cubierta de prueba" in prompt
    assert "CENTRAL, verdict=falso" in prompt
    assert "sintoma_del_par" in prompt          # el esquema nuevo viaja en el prompt


def test_par_completo_corrige_sintoma_y_causa():
    caso = _caso([[_atrib("contenido_kg", "restriccion_2_3_1",
                          sintoma="noise_sensitivity")]])
    paquete = _fetch(caso)
    client = _MockClient([_salida_s1("no", "completitud_kg", sintoma="context_recall")])
    out = aplicar_s1(caso, _kg_s1(), paquete, n=1, client=client,
                     sintoma_F=[], sintoma_P=["p"])
    a = out["repeticiones"][0]["atribuciones"][0]
    assert a["capa_s1"]["par_post_s1"] == ["context_recall", "completitud_kg"]
    assert a["capa_s1"]["corrigio"] is True
    assert a["sintoma_capa1"] == "context_recall" and a["causa_capa2"] == "completitud_kg"
    assert a["capa_s1"]["emision_v61d"]["sintoma_capa1"] == "noise_sensitivity"


def test_sintoma_fuera_de_dominio_no_vota_con_anotacion():
    # B4.5: síntoma fuera de dominio → anotación fuera_de_dominio (verbatim), no vota
    caso = _caso([[_atrib("contenido_kg", "restriccion_2_3_1")]])
    client = _MockClient([_salida_s1("no", "contenido_kg", sintoma="banana")])
    out = aplicar_s1(caso, _kg_s1(), _fetch(caso), n=1, client=client)
    a = out["repeticiones"][0]["atribuciones"][0]
    fd = a["capa_s1"]["salidas_s1"][0]["fuera_de_dominio"]
    assert fd == [{"campo": "sintoma_del_par", "valor_verbatim": "banana"}]
    assert a["capa_s1"]["accion"] == "no_determinable"


def test_rama_exoneracion_usa_esquema_alternativo():
    caso = _caso([[_atrib("sin_defecto", "restriccion_2_3_1", jerarquia="sin_par")]],
                 ganadores=[])
    paquete = _fetch(caso, F=[], P=["pata sin cubrir"])
    assert paquete["gatillo_caso"]["exoneracion_con_sintoma"] is True
    client = _MockClient([_salida_s1_exon("no", "completitud_kg")])
    out = aplicar_s1(caso, _kg_s1(), paquete, n=1, client=client,
                     sintoma_F=[], sintoma_P=["pata sin cubrir"],
                     respuesta_agente="respuesta del agente de prueba")
    prompt = client.llamadas[0]["messages"][0]["content"]
    assert "pata sin cubrir" in prompt
    assert "respuesta del agente de prueba" in prompt
    assert "presente_en_grafo" in prompt         # esquema alternativo
    assert "alcance_declarado_en_fuente" not in prompt
    a = out["repeticiones"][0]["atribuciones"][0]
    assert a["capa_s1"]["esquema"] == "exoneracion"
    assert a["capa_s1"]["corrigio"] is True
    assert a["causa_capa2"] == "completitud_kg"
    assert a["sintoma_capa1"] == "context_recall"   # la rama se define por la pata
    assert a["capa_s1"]["salidas_s1"][0]["respuesta_en_fuente"] == "quote de la fuente"


def test_rama_exoneracion_confirma_sin_defecto():
    caso = _caso([[_atrib("sin_defecto", "restriccion_2_3_1", jerarquia="sin_par")]],
                 ganadores=[])
    paquete = _fetch(caso, F=[], P=["pata x"])
    client = _MockClient([_salida_s1_exon("si", "sin_defecto", quote=None)])
    out = aplicar_s1(caso, _kg_s1(), paquete, n=1, client=client,
                     sintoma_F=[], sintoma_P=["pata x"], respuesta_agente="r")
    a = out["repeticiones"][0]["atribuciones"][0]
    assert a["capa_s1"]["corrigio"] is False
    assert a["causa_capa2"] == "sin_defecto"


def test_esquema_causa_sigue_para_gatillo_de_causas():
    caso = _caso([[_atrib("contenido_kg", "restriccion_2_3_1")]])
    client = _MockClient([_salida_s1("no", "contenido_kg")])
    out = aplicar_s1(caso, _kg_s1(), _fetch(caso), n=1, client=client)
    a = out["repeticiones"][0]["atribuciones"][0]
    assert a["capa_s1"]["esquema"] == "causa"
    assert a["capa_s1"]["voto_s1_atrib"]["esquema"] == "causa"


# --------------------------------------------------------------------------- #
# 8. B4.3 r2 — regla mecánica de jerarquía para exoneraciones corregidas       #
# --------------------------------------------------------------------------- #
def test_exon_corregida_una_pata_promueve_a_primaria():
    # 2 reps con exoneración corregida → 2 primarias → el voto_s1 las CUENTA (mayoría 2)
    caso = _caso([[_atrib("sin_defecto", "restriccion_2_3_1", jerarquia="sin_par")],
                  [_atrib("sin_defecto", "restriccion_2_3_1", jerarquia="sin_par")]],
                 ganadores=[])
    paquete = _fetch(caso, F=[], P=["la única pata"])
    client = _MockClient([_salida_s1_exon("no", "completitud_kg"),
                          _salida_s1_exon("no", "completitud_kg")])
    out = aplicar_s1(caso, _kg_s1(), paquete, n=1, client=client,
                     sintoma_F=[], sintoma_P=["la única pata"], respuesta_agente="r")
    a = out["repeticiones"][0]["atribuciones"][0]
    assert a["jerarquia"] == "primaria" and a["pata"] == "la única pata"
    assert a["capa_s1"]["jerarquia_original"] == "sin_par"
    assert a["capa_s1"]["jerarquia_post_s1"] == "primaria"
    assert "nota" not in a["capa_s1"]
    # el voto_s1 ahora CUENTA estas primarias (mayoría 2/2)
    assert out["voto_s1"]["pares_primarios_ganadores"] == [["context_recall",
                                                            "completitud_kg"]]
    assert out["voto_s1"]["votos_ganadores"] == 2


def test_exon_corregida_dos_patas_conjunto_con_nota():
    caso = _caso([[_atrib("sin_defecto", "restriccion_2_3_1", jerarquia="sin_par")]],
                 ganadores=[])
    P = ["pata uno", "pata dos"]
    paquete = _fetch(caso, F=[], P=P)
    client = _MockClient([_salida_s1_exon("no", "completitud_kg")])
    out = aplicar_s1(caso, _kg_s1(), paquete, n=1, client=client,
                     sintoma_F=[], sintoma_P=P, respuesta_agente="r")
    a = out["repeticiones"][0]["atribuciones"][0]
    assert a["jerarquia"] == "primaria" and a["pata"] == P
    assert a["capa_s1"]["nota"] == "mecanica_sin_mapeo"


def test_exon_corregida_sobre_claims_jerarquia_por_centralidad():
    F_c = [{"enunciado": "afirmación x", "central": True, "verdict": "falso"}]
    # el quote de la atribución sintética ("afirmación x") mapea al claim CENTRAL → primaria
    caso = _caso([[_atrib("sin_defecto", "restriccion_2_3_1", jerarquia="sin_par")]],
                 ganadores=[])
    paquete = _fetch(caso, F=F_c, P=[])
    client = _MockClient([_salida_s1_exon("no", "contenido_kg")])
    out = aplicar_s1(caso, _kg_s1(), paquete, n=1, client=client,
                     sintoma_F=F_c, sintoma_P=[], respuesta_agente="r")
    a = out["repeticiones"][0]["atribuciones"][0]
    assert a["jerarquia"] == "primaria"
    assert a["capa_s1"]["mapeo_claims"] == ["afirmación x"]
    # solo secundarios (o sin mapeo) → secundaria
    F_s = [{"enunciado": "otra cosa sin relación", "central": False, "verdict": "falso"}]
    caso2 = _caso([[_atrib("sin_defecto", "restriccion_2_3_1", jerarquia="sin_par")]],
                  ganadores=[])
    client2 = _MockClient([_salida_s1_exon("no", "contenido_kg")])
    out2 = aplicar_s1(caso2, _kg_s1(), _fetch(caso2, F=F_s, P=[]), n=1, client=client2,
                      sintoma_F=F_s, sintoma_P=[], respuesta_agente="r")
    a2 = out2["repeticiones"][0]["atribuciones"][0]
    assert a2["jerarquia"] == "secundaria"


def test_correccion_de_causas_no_cambia_jerarquia():
    caso = _caso([[_atrib("contenido_kg", "restriccion_2_3_1", jerarquia="primaria")]])
    client = _MockClient([_salida_s1("no", "completitud_kg", sintoma="context_recall")])
    out = aplicar_s1(caso, _kg_s1(), _fetch(caso), n=1, client=client,
                     sintoma_F=[], sintoma_P=["p"])
    a = out["repeticiones"][0]["atribuciones"][0]
    assert a["capa_s1"]["corrigio"] is True
    assert a["jerarquia"] == "primaria"                 # intacta
    assert "jerarquia_original" not in a["capa_s1"]     # la regla no aplicó


# --------------------------------------------------------------------------- #
# 9. B4.5 — guardas determinísticas de dominio                                 #
# --------------------------------------------------------------------------- #
def test_causa_fuera_de_dominio_no_vota_con_anotacion():
    caso = _caso([[_atrib("contenido_kg", "restriccion_2_3_1")]])
    client = _MockClient([_salida_s1("no", "context_recall")])   # un SÍNTOMA como causa
    out = aplicar_s1(caso, _kg_s1(), _fetch(caso), n=1, client=client)
    a = out["repeticiones"][0]["atribuciones"][0]
    sal = a["capa_s1"]["salidas_s1"][0]
    assert sal["fuera_de_dominio"] == [{"campo": "causa_confirmada_o_corregida",
                                        "valor_verbatim": "context_recall"}]
    assert sal["causa_confirmada_o_corregida"] == "context_recall"  # verbatim preservado
    assert a["capa_s1"]["accion"] == "no_determinable"
    assert a["causa_capa2"] == "contenido_kg"                       # sin reescritura


def test_causa_fuera_de_dominio_en_rama_exoneracion():
    caso = _caso([[_atrib("sin_defecto", "restriccion_2_3_1", jerarquia="sin_par")]],
                 ganadores=[])
    client = _MockClient([_salida_s1_exon("no", "falta_grave")])
    out = aplicar_s1(caso, _kg_s1(), _fetch(caso, F=[], P=["p"]), n=1, client=client,
                     sintoma_F=[], sintoma_P=["p"], respuesta_agente="r")
    a = out["repeticiones"][0]["atribuciones"][0]
    assert a["capa_s1"]["salidas_s1"][0]["fuera_de_dominio"][0]["valor_verbatim"] == "falta_grave"
    assert a["capa_s1"]["accion"] == "no_determinable"
    assert a["causa_capa2"] == "sin_defecto" and a["jerarquia"] == "sin_par"


def test_valores_validos_intactos():
    caso = _caso([[_atrib("contenido_kg", "restriccion_2_3_1")]])
    client = _MockClient([_salida_s1("no", "completitud_kg", sintoma="context_recall")])
    out = aplicar_s1(caso, _kg_s1(), _fetch(caso), n=1, client=client)
    a = out["repeticiones"][0]["atribuciones"][0]
    assert "fuera_de_dominio" not in a["capa_s1"]["salidas_s1"][0]
    assert a["capa_s1"]["corrigio"] is True
    assert a["causa_capa2"] == "completitud_kg"


def test_navegacion_ambas_grafias_validas():
    from s1_fuentes import CAUSAS_VALIDAS
    assert "navegación" in CAUSAS_VALIDAS and "navegacion" in CAUSAS_VALIDAS
