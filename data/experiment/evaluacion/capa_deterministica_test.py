"""Tests unitarios de capa_deterministica.py (D2). Sin API, sin disco:
grafo sintético de D1 + casos_json sintéticos construidos acá."""

import copy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from harness import GraphIndex
from loader import Node
from test_alcanzabilidad_test import _kg_sintetico, PREGUNTA
from capa_deterministica import (aplicar_d2, aplicar_d3, aplicar_d4, aplicar_d5,
                                 aplicar_d6, aplicar_capa, VERSION_CAPA,
                                 _sintoma_de_trace)


def _index():
    return GraphIndex(_kg_sintetico())


def _atrib(sintoma, causa, ubicacion, jerarquia="primaria"):
    return {
        "sintoma_capa1": sintoma,
        "causa_capa2": causa,
        "lado": "?",
        "jerarquia": jerarquia,
        "pata": "pata de prueba",
        "evidencia": {
            "afirmacion": {"quote": "x", "ubicacion": "respuesta final"},
            "nodo": {"quote": "y", "ubicacion": ubicacion},
            "fuente": {"quote": "z", "ubicacion": "pdf"},
        },
    }


def _caso(reps_atribs, voto=None):
    return {
        "id_falla": "sintetico/CQ-000",
        "run": "sintetico",
        "n_reps": len(reps_atribs),
        "voto": voto if voto is not None else {"resultado": "mayoria", "marca": "ORIGINAL"},
        "repeticiones": [
            {"formato_invalido": False, "errores_formato": [], "atribuciones": atribs}
            for atribs in reps_atribs
        ],
    }


def _d2(caso):
    # inyección sin disco: pregunta del set sintético, sin consultas del agente ni expuestos
    return aplicar_d2(caso, _index(), pregunta=PREGUNTA, consultas_agente=[],
                      tokens_expuestos=set())


def test_navegacion_con_portador_inalcanzable_se_corrige():
    # restriccion_r7 es inalcanzable desde la pregunta (probado en D1)
    caso = _caso([[_atrib("context_recall", "navegación", "restriccion_r7 (paso 3)")]])
    out = _d2(caso)
    a = out["repeticiones"][0]["atribuciones"][0]
    assert a["causa_capa2"] == "alcanzabilidad_kg"
    assert a["capa_d"]["emision_llm"] == "navegación"
    assert a["capa_d"]["decision_codigo"] == "alcanzabilidad_kg"
    assert a["capa_d"]["discrepancia"] is True
    assert a["capa_d"]["alcanzable"] is False
    ev = a["capa_d"]["evidencia_d1"]
    assert ev["consultas_en_top10"] == [] and ev["mejor_rank"] is None
    assert "consultas" not in ev  # la lista completa NO viaja


def test_alcanzabilidad_con_portador_alcanzable_se_corrige():
    # restriccion_exclusion es alcanzable desde la pregunta (probado en D1)
    caso = _caso([[_atrib("context_recall", "alcanzabilidad_kg", "restriccion_exclusion")]])
    out = _d2(caso)
    a = out["repeticiones"][0]["atribuciones"][0]
    assert a["causa_capa2"] == "navegación"
    assert a["capa_d"]["discrepancia"] is True
    assert a["capa_d"]["alcanzable"] is True
    assert a["capa_d"]["evidencia_d1"]["consultas_en_top10"]


def test_emision_correcta_sin_discrepancia():
    caso = _caso([[_atrib("context_recall", "navegación", "restriccion_exclusion")]])
    out = _d2(caso)
    a = out["repeticiones"][0]["atribuciones"][0]
    assert a["causa_capa2"] == "navegación"
    assert a["capa_d"]["decision_codigo"] == "navegación"
    assert a["capa_d"]["discrepancia"] is False


def test_sin_portador_extraible_triage_causa_intacta():
    caso = _caso([[_atrib("context_recall", "navegación", "un nodo cualquiera sin id")]])
    out = _d2(caso)
    a = out["repeticiones"][0]["atribuciones"][0]
    assert a["capa_d"] == {"modulo": "D2", "accion": "sin_portador_extraible", "triage": True}
    assert a["causa_capa2"] == "navegación"  # intacta
    assert out["resumen_capa_d"]["triage"] == 1
    assert out["resumen_capa_d"]["atribuciones_corregidas"] == 0


def test_par_fuera_de_frontera_intacto_sin_capa_d():
    caso = _caso([[
        _atrib("noise_sensitivity", "contenido_kg", "restriccion_r7"),
        _atrib("context_recall", "completitud_kg", "restriccion_exclusion"),
        _atrib("faithfulness", "alucinacion_agente", "sin id"),
    ]])
    out = _d2(caso)
    for a in out["repeticiones"][0]["atribuciones"]:
        assert "capa_d" not in a
    assert out["resumen_capa_d"] == {"reps_tocadas": [], "atribuciones_corregidas": 0,
                                     "discrepancias": 0, "triage": 0}


def test_recomputo_del_voto_cambia_mayoria_y_preserva_original():
    # 3 reps: rep1 y rep2 emiten navegación (portador INALCANZABLE → corrige a
    # alcanzabilidad); rep3 emite alcanzabilidad_kg directamente. Voto original
    # (sintético): mayoría navegación 2-1. Tras D2: alcanzabilidad_kg 3-0.
    voto_original = {"resultado": "mayoria", "marca": "ORIGINAL",
                     "pares_primarios_ganadores": [["context_recall", "navegación"]],
                     "votos_ganadores": 2}
    caso = _caso(
        [[_atrib("context_recall", "navegación", "restriccion_r7")],
         [_atrib("context_recall", "navegación", "restriccion_r7")],
         [_atrib("context_recall", "alcanzabilidad_kg", "restriccion_r7")]],
        voto=voto_original)
    out = _d2(caso)
    assert out["voto"] == voto_original  # el voto original queda INTACTO
    v = out["voto_capa_d"]
    assert v["resultado"] == "mayoria" and v["flag_voto_dividido"] is False
    assert v["pares_primarios_ganadores"] == [["context_recall", "alcanzabilidad_kg"]]
    assert v["votos_ganadores"] == 3
    assert out["resumen_capa_d"]["atribuciones_corregidas"] == 3
    assert out["resumen_capa_d"]["discrepancias"] == 2  # rep3 ya emitía alcanzabilidad


def test_rep_invalida_no_vota_ni_se_toca():
    caso = _caso([[_atrib("context_recall", "navegación", "restriccion_r7")],
                  [_atrib("context_recall", "navegación", "restriccion_r7")]])
    caso["repeticiones"].append(
        {"formato_invalido": True, "errores_formato": ["json roto"],
         "atribuciones": [_atrib("context_recall", "navegación", "restriccion_r7")]})
    out = _d2(caso)
    assert "capa_d" not in out["repeticiones"][2]["atribuciones"][0]
    assert out["voto_capa_d"]["reps_validas"] == [1, 2]
    assert out["voto_capa_d"]["votos_ganadores"] == 2


def test_determinismo():
    caso = _caso(
        [[_atrib("context_recall", "navegación", "restriccion_r7"),
          _atrib("noise_sensitivity", "contenido_kg", "restriccion_exclusion")],
         [_atrib("context_recall", "alcanzabilidad_kg", "restriccion_exclusion")]])
    out1 = aplicar_d2(copy.deepcopy(caso), _index(), pregunta=PREGUNTA,
                      consultas_agente=["garantías preferidas A"], tokens_expuestos={"x"})
    out2 = aplicar_d2(copy.deepcopy(caso), _index(), pregunta=PREGUNTA,
                      consultas_agente=["garantías preferidas A"], tokens_expuestos={"x"})
    assert out1 == out2


def test_insumos_faltantes():
    import pytest
    with pytest.raises(ValueError):
        aplicar_d2(_caso([[]]), _index())


# --------------------------------------------------------------------------- #
# D3 — validador de quotes de aplicacion_erronea                               #
# --------------------------------------------------------------------------- #
def _atrib_ae(quote, ubicacion, jerarquia="secundaria"):
    a = _atrib("noise_sensitivity", "aplicacion_erronea", ubicacion, jerarquia)
    a["evidencia"]["nodo"]["quote"] = quote
    return a


def test_d3_quote_verificable():
    # quote verbatim (módulo mayúsculas/acentos/espacios) de la descripcion de restriccion_r7
    caso = _caso([[_atrib_ae("los deudores CUBIERTOS con garantias   preferidas A",
                             "restriccion_r7 (paso 2)")]])
    out = aplicar_d3(caso, _index())
    a = out["repeticiones"][0]["atribuciones"][0]
    assert a["capa_d"] == {"modulo": "D3", "portador_id": "restriccion_r7",
                           "quote_verificado": True}
    assert a["causa_capa2"] == "aplicacion_erronea"  # D3 nunca cambia la causa


def test_d3_quote_no_verificable():
    caso = _caso([[_atrib_ae("este texto no vive en el nodo", "restriccion_r7")]])
    out = aplicar_d3(caso, _index())
    a = out["repeticiones"][0]["atribuciones"][0]
    assert a["capa_d"]["quote_verificado"] is False
    assert a["capa_d"]["accion"] == "quote_no_verificable"
    assert a["capa_d"]["triage"] is True
    assert a["causa_capa2"] == "aplicacion_erronea"


def test_d3_sin_portador():
    caso = _caso([[_atrib_ae("da igual", "un nodo sin id reconocible")]])
    out = aplicar_d3(caso, _index())
    a = out["repeticiones"][0]["atribuciones"][0]
    assert a["capa_d"] == {"modulo": "D3", "accion": "sin_portador_extraible", "triage": True}


def test_d3_ignora_otras_causas():
    caso = _caso([[_atrib("context_recall", "navegación", "restriccion_r7")]])
    out = aplicar_d3(caso, _index())
    assert "capa_d" not in out["repeticiones"][0]["atribuciones"][0]


# --------------------------------------------------------------------------- #
# D4 — reglas de triage (cada una disparando sola)                             #
# --------------------------------------------------------------------------- #
def _voto(ganadores, dividido=False, votos=2):
    return {"resultado": "frontera_no_determinada" if dividido else "mayoria",
            "flag_voto_dividido": dividido,
            "pares_primarios_ganadores": None if dividido else ganadores,
            "votos_ganadores": None if dividido else votos, "conteo": []}


def _caso_d4(atribs, voto):
    caso = _caso([atribs])
    caso["voto_capa_d"] = voto
    return caso


def test_d4_r1_exoneracion_total():
    out = aplicar_d4(_caso_d4([], _voto([])))
    assert out["triage_capa_d"]["triage"] is True
    assert out["triage_capa_d"]["motivos"] == ["exoneracion_total"]


def test_d4_r2_aplicacion_erronea_presente():
    out = aplicar_d4(_caso_d4([_atrib_ae("q", "restriccion_r7")],
                              _voto([["noise_sensitivity", "aplicacion_erronea"]])))
    assert out["triage_capa_d"]["motivos"] == ["aplicacion_erronea_bajo_revision"]


def test_d4_r3_propagacion():
    atrib = _atrib("context_recall", "navegación", "sin id")
    atrib["capa_d"] = {"modulo": "D2", "accion": "sin_portador_extraible", "triage": True}
    out = aplicar_d4(_caso_d4([atrib], _voto([["context_recall", "navegación"]])))
    assert out["triage_capa_d"]["motivos"] == ["modulo_deterministico_sin_decision"]


def test_d4_r4_voto_dividido():
    out = aplicar_d4(_caso_d4([_atrib("context_recall", "completitud_kg", "x")],
                              _voto(None, dividido=True)))
    assert out["triage_capa_d"]["motivos"] == ["voto_dividido"]


def test_d4_sin_disparo():
    out = aplicar_d4(_caso_d4([_atrib("context_recall", "completitud_kg", "x")],
                              _voto([["context_recall", "completitud_kg"]])))
    assert out["triage_capa_d"] == {"triage": False, "motivos": [], "flags": []}


def test_d4_requiere_voto_capa_d():
    import pytest
    with pytest.raises(ValueError):
        aplicar_d4(_caso([[]]))


def test_d4_rep_invalida_no_dispara():
    caso = _caso_d4([], _voto([["context_recall", "completitud_kg"]]))
    caso["repeticiones"].append(
        {"formato_invalido": True, "errores_formato": ["roto"],
         "atribuciones": [_atrib_ae("q", "restriccion_r7")]})
    out = aplicar_d4(caso)
    assert out["triage_capa_d"]["triage"] is False


# --------------------------------------------------------------------------- #
# Pipeline completo: aplicar_capa (D2 → D3 → D4)                               #
# --------------------------------------------------------------------------- #
def _caso_pipeline():
    # rep1: frontera navegación con portador INALCANZABLE (D2 corrige) + aplicacion_erronea
    #       con quote verificable (D3 ok, dispara R2)
    # rep2: frontera navegación ídem + aplicacion_erronea con quote NO verificable
    #       (D3 triage → R3)
    return _caso([
        [_atrib("context_recall", "navegación", "restriccion_r7"),
         _atrib_ae("Los deudores cubiertos con garantías preferidas A", "restriccion_r7")],
        [_atrib("context_recall", "navegación", "restriccion_r7"),
         _atrib_ae("texto inexistente en el nodo", "restriccion_r7")],
    ])


def _capa(caso):
    # síntoma inyectado con P no vacío: R6a no rige y las primarias context_recall quedan
    # intactas — el pipeline pre-D6 conserva su comportamiento en estos tests
    return aplicar_capa(caso, _index(), pregunta=PREGUNTA, consultas_agente=[],
                        tokens_expuestos=set(), outputs_completos=[],
                        sintoma_F=[], sintoma_P=["pata de prueba"])


def test_pipeline_completo_d2_d3_d4():
    out = _capa(_caso_pipeline())
    assert out["version_capa"] == VERSION_CAPA
    # D2 corrigió las dos primarias de frontera
    for rep in out["repeticiones"]:
        frontera = rep["atribuciones"][0]
        assert frontera["causa_capa2"] == "alcanzabilidad_kg"
        assert frontera["capa_d"]["modulo"] == "D2" and frontera["capa_d"]["discrepancia"]
    # D3 anotó las dos aplicacion_erronea sin cambiar la causa
    assert out["repeticiones"][0]["atribuciones"][1]["capa_d"]["quote_verificado"] is True
    ae2 = out["repeticiones"][1]["atribuciones"][1]
    assert ae2["capa_d"]["quote_verificado"] is False and ae2["capa_d"]["triage"] is True
    assert ae2["causa_capa2"] == "aplicacion_erronea"
    # voto recomputado sobre primarias corregidas
    v = out["voto_capa_d"]
    assert v["pares_primarios_ganadores"] == [["context_recall", "alcanzabilidad_kg"]]
    assert v["votos_ganadores"] == 2
    # D4: R2 (aplicacion_erronea presente) + R3 (triage de D3); ni R1 ni R4
    assert out["triage_capa_d"]["triage"] is True
    assert out["triage_capa_d"]["motivos"] == [
        "aplicacion_erronea_bajo_revision", "modulo_deterministico_sin_decision"]
    assert out["resumen_capa_d"]["atribuciones_corregidas"] == 2
    # el voto original sintético quedó intacto
    assert out["voto"] == {"resultado": "mayoria", "marca": "ORIGINAL"}


def test_pipeline_determinismo():
    out1 = _capa(_caso_pipeline())
    out2 = _capa(_caso_pipeline())
    assert out1 == out2


# --------------------------------------------------------------------------- #
# D5 — diligencia determinística de causas de ausencia                         #
# --------------------------------------------------------------------------- #
def _kg_d5():
    """Grafo sintético de D1 + candidatos para los barridos de D5."""
    kg = _kg_sintetico()
    kg.nodes.append(Node(id="restriccion_limite_200", type="Restriccion",
                         label="Límite doscientos",
                         properties={"umbral": "USD 200",
                                     "descripcion": "El límite se incrementa a USD 200"},
                         provenances=[]))
    kg.nodes.append(Node(id="norma_x9", type="Restriccion",
                         label="Norma equis",
                         properties={"umbral": "USD 300"},
                         provenances=[]))
    return kg


def _index_d5():
    return GraphIndex(_kg_d5())


def _atrib_d5(causa, quote_afirmacion, pata="pata de prueba", jerarquia="primaria"):
    a = _atrib("context_recall", causa, "sin id", jerarquia)
    a["evidencia"]["afirmacion"]["quote"] = quote_afirmacion
    a["pata"] = pata
    return a


def _d5(caso, index=None, consultas=None, outputs=None):
    return aplicar_d5(caso, index or _index_d5(), pregunta=PREGUNTA,
                      consultas_agente=consultas or [], tokens_expuestos=set(),
                      outputs_completos=outputs or [])


def test_d5_candidato_no_expuesto_alcanzable_dispara_r5():
    caso = _caso([[_atrib_d5("completitud_kg", "no está el límite de USD 200 para otras modalidades")]])
    out = _d5(caso, consultas=["límite doscientos"])
    cd = out["repeticiones"][0]["atribuciones"][0]["capa_d"]
    assert cd["modulo"] == "D5" and cd["literales"] == ["USD 200"]
    assert cd["candidatos_evaluados"] == 1 and cd["triage"] is True
    b = cd["banderas"][0]
    assert b == {"literal": "USD 200", "candidato_id": "restriccion_limite_200",
                 "alcanzable": True, "mejor_rank": b["mejor_rank"], "expuesto": False}
    assert b["mejor_rank"] is not None
    # R5 dispara
    out["voto_capa_d"] = _voto([["context_recall", "completitud_kg"]])
    final = aplicar_d4(out)
    assert "posible_portador_no_considerado" in final["triage_capa_d"]["motivos"]


def test_d5_candidato_no_expuesto_inalcanzable_tambien_bandera():
    caso = _caso([[_atrib_d5("alucinacion_agente", "el agente inventó un tope de USD 300")]])
    out = _d5(caso)
    cd = out["repeticiones"][0]["atribuciones"][0]["capa_d"]
    assert cd["banderas"] == [{"literal": "USD 300", "candidato_id": "norma_x9",
                               "alcanzable": False, "mejor_rank": None, "expuesto": False}]
    assert cd["triage"] is True  # la distinción alcanzable/no la lee el humano


def test_d5_candidato_expuesto_sin_bandera():
    caso = _caso([[_atrib_d5("completitud_kg", "no está el límite de USD 200")]])
    out = _d5(caso, outputs=['{"id": "restriccion_limite_200", "umbral": "USD 200"}'])
    cd = out["repeticiones"][0]["atribuciones"][0]["capa_d"]
    assert cd["banderas"] == [] and cd["triage"] is False
    assert cd["candidatos_evaluados"] == 1
    assert cd["candidatos_expuestos_descartados"] == 1


def test_d5_sin_literales():
    caso = _caso([[_atrib_d5("completitud_kg", "falta el dato del régimen, sin números")]])
    out = _d5(caso)
    cd = out["repeticiones"][0]["atribuciones"][0]["capa_d"]
    assert cd == {"modulo": "D5", "accion": "sin_literales", "banderas": []}
    # sin triage: ni R3 ni R5 disparan
    out["voto_capa_d"] = _voto([["context_recall", "completitud_kg"]])
    assert aplicar_d4(out)["triage_capa_d"]["triage"] is False


def test_d5_causa_fuera_del_gatillo():
    caso = _caso([[_atrib_d5("contenido_kg", "dice USD 200 donde el PDF dice USD 300")]])
    out = _d5(caso)
    a = out["repeticiones"][0]["atribuciones"][0]
    assert "capa_d" not in a and "capa_d5" not in a


def test_d5_no_cambia_causa_ni_pisa_capa_d():
    atrib = _atrib_d5("completitud_kg", "no está el USD 300")
    atrib["capa_d"] = {"modulo": "D2", "marca": "PREEXISTENTE"}
    caso = _caso([[atrib]])
    out = _d5(caso)
    a = out["repeticiones"][0]["atribuciones"][0]
    assert a["capa_d"] == {"modulo": "D2", "marca": "PREEXISTENTE"}  # no se pisa
    assert a["capa_d5"]["modulo"] == "D5" and a["capa_d5"]["literales"] == ["USD 300"]
    assert a["causa_capa2"] == "completitud_kg" and a["jerarquia"] == "primaria"


def test_d5_un_nivel_no_se_extrae():
    caso = _caso([[_atrib_d5("completitud_kg", "según el punto 1.1 y el 3.9 del TO"),
                   _atrib_d5("completitud_kg", "según el punto 1.1.2.2 del TO")]])
    out = _d5(caso)
    a1, a2 = out["repeticiones"][0]["atribuciones"]
    assert a1["capa_d"]["accion"] == "sin_literales"        # "1.1"/"3.9" descartados
    assert a2["capa_d"]["literales"] == ["1.1.2.2"]         # dos niveles sí


def test_d5_pipeline_completo_determinismo():
    caso = _caso([
        [_atrib("context_recall", "navegación", "restriccion_r7"),
         _atrib_d5("completitud_kg", "no está el límite de USD 200")],
        [_atrib_ae("Los deudores cubiertos con garantías preferidas A", "restriccion_r7")],
    ])
    def correr():
        return aplicar_capa(copy.deepcopy(caso), _index_d5(), pregunta=PREGUNTA,
                            consultas_agente=["límite doscientos"], tokens_expuestos=set(),
                            outputs_completos=[],
                            sintoma_F=[], sintoma_P=["pata de prueba"])
    out1, out2 = correr(), correr()
    assert out1 == out2
    assert out1["version_capa"] == VERSION_CAPA
    # D5 gatilló y D4 recogió R5 junto con los motivos previos
    assert "posible_portador_no_considerado" in out1["triage_capa_d"]["motivos"]
    assert "aplicacion_erronea_bajo_revision" in out1["triage_capa_d"]["motivos"]


def test_d5_coeficiente_decimal_se_extrae():
    caso = _caso([[_atrib_d5("alucinacion_agente", "0,08 es el coeficiente de capital mínimo"),
                   _atrib_d5("completitud_kg", "la alícuota es 8,5 por ciento")]])
    out = _d5(caso)
    a1, a2 = out["repeticiones"][0]["atribuciones"]
    assert a1["capa_d"]["literales"] == ["0,08"]
    assert a2["capa_d"]["literales"] == ["8,5"]


def test_d5_decimal_con_punto_sigue_sin_extraerse():
    # limitación simétrica documentada: "3.9"/"0.08" (punto) no se extraen
    caso = _caso([[_atrib_d5("completitud_kg", "el coeficiente 0.08 del punto 3.9")]])
    out = _d5(caso)
    assert out["repeticiones"][0]["atribuciones"][0]["capa_d"]["accion"] == "sin_literales"


def test_d5_decimal_pegado_a_miles_comportamiento_fijado():
    # Comportamiento FIJADO (documentado en el docstring): la guarda es por dígito
    # adyacente; en "1.100,50" el punto de miles no es dígito, así que se extrae el
    # tramo decimal posterior al último punto: "100,50" (no "1.100,50" ni nada).
    caso = _caso([[_atrib_d5("completitud_kg", "el tope es 1.100,50 pesos")]])
    out = _d5(caso)
    assert out["repeticiones"][0]["atribuciones"][0]["capa_d"]["literales"] == ["100,50"]


def test_outputs_completos_de_trace_helper(tmp_path):
    import json
    from test_alcanzabilidad import outputs_completos_de_trace, tokens_expuestos_de_trace
    from harness import _tokens
    traza = [{
        "run": "sintetico",
        "trace": {"question": PREGUNTA, "steps": [
            {"n": 1, "tool": "buscar_nodos",
             "input": {"consulta": "deudores clasificación", "limite": 10}},
            {"n": 2, "tool": "ver_nodo", "input": {"id": "restriccion_r7"}},
            {"n": 3, "tool": "tool_rara", "input": {}},
        ]},
    }]
    p = tmp_path / "traza.json"
    p.write_text(json.dumps(traza, ensure_ascii=False))
    outs = outputs_completos_de_trace(p, index=_index_d5())
    assert len(outs) == 2 and all(isinstance(o, str) for o in outs)   # tool_rara se omite
    assert "restriccion_r7" in outs[1]
    # tokens_expuestos_de_trace reescrita encima: mismos tokens que los outputs
    esperados = set(_tokens(outs[0])) | set(_tokens(outs[1]))
    assert tokens_expuestos_de_trace(p, index=_index_d5()) == esperados
    # hasta_paso limita
    outs1 = outputs_completos_de_trace(p, hasta_paso=1, index=_index_d5())
    assert len(outs1) == 1


# --------------------------------------------------------------------------- #
# D6 — consistencia síntoma↔atribución (v6.1-D)                                #
# --------------------------------------------------------------------------- #
def _atrib_q(sintoma, causa, quote_afirmacion, jerarquia="primaria"):
    a = _atrib(sintoma, causa, "restriccion_r7", jerarquia)
    a["evidencia"]["afirmacion"]["quote"] = quote_afirmacion
    return a


def _F(*claims):
    return [{"enunciado": e, "central": c, "verdict": "no_soportado"} for e, c in claims]


def test_sintoma_de_trace(tmp_path):
    import json
    traza = [{
        "run": "sintetico",
        "judge": {"step2": {
            "verificaciones": [
                {"enunciado": "claim central malo", "central": True, "verdict": "no_soportado"},
                {"enunciado": "claim ok", "central": True, "verdict": "verdadero"},
                {"enunciado": "claim secundario malo", "central": False, "verdict": "falso"},
            ],
            "cobertura_patas": [
                {"pata": "pata cubierta", "cobertura": "cubierta"},
                {"pata": "pata faltante", "cobertura": "no_cubierta"},
            ],
        }},
        "trace": {"question": PREGUNTA, "steps": []},
    }]
    p = tmp_path / "traza.json"
    p.write_text(json.dumps(traza, ensure_ascii=False))
    F, P = _sintoma_de_trace(p)
    assert F == [
        {"enunciado": "claim central malo", "central": True, "verdict": "no_soportado"},
        {"enunciado": "claim secundario malo", "central": False, "verdict": "falso"},
    ]
    assert P == ["pata faltante"]


def test_d6_r6a_dispara_con_sintoma_vacio_sin_reescribir():
    caso = _caso([[
        _atrib_q("context_recall", "completitud_kg", "algo que falta"),
        _atrib_q("noise_sensitivity", "sin_defecto", "claim correcto", jerarquia="sin_par"),
    ]])
    out = aplicar_d6(caso, [], [])
    a1, a2 = out["repeticiones"][0]["atribuciones"]
    assert a1["capa_d6"] == {"regla": "R6a", "accion": "atribucion_sin_sintoma"}
    assert "capa_d6" not in a2                       # sin_defecto no se marca
    assert a1["causa_capa2"] == "completitud_kg"     # causa intacta
    assert a1["jerarquia"] == "primaria"             # jerarquía intacta
    out["voto_capa_d"] = _voto([["context_recall", "completitud_kg"]])
    final = aplicar_d4(out)
    assert "atribucion_sin_sintoma" in final["triage_capa_d"]["motivos"]


def test_d6_r6a_no_dispara_con_cualquier_sintoma():
    caso = _caso([[_atrib_q("context_recall", "completitud_kg", "algo")]])
    con_f = aplicar_d6(copy.deepcopy(caso), _F(("un claim reprobado", False)), [])
    con_p = aplicar_d6(copy.deepcopy(caso), [], ["una pata no cubierta"])
    # con F no vacío la primaria context_recall sin pata se anota R6b, no R6a
    assert con_f["repeticiones"][0]["atribuciones"][0]["capa_d6"]["accion"] == "context_recall_sin_pata"
    assert "capa_d6" not in con_p["repeticiones"][0]["atribuciones"][0]


def test_d6_r6b_degrada_mapeada_solo_a_secundario():
    caso = _caso([[_atrib_q("noise_sensitivity", "contenido_kg",
                            "límite del 17% está vigente hasta el 30/06/26")]])
    F = _F(("Ese límite del 17% está vigente hasta el 30/06/26", False))
    out = aplicar_d6(caso, F, [])
    a = out["repeticiones"][0]["atribuciones"][0]
    assert a["jerarquia"] == "secundaria"
    assert a["capa_d6"] == {"regla": "R6b", "emision_llm": "primaria",
                            "decision_codigo": "secundaria",
                            "claim_mapeado": "Ese límite del 17% está vigente hasta el 30/06/26"}
    assert a["causa_capa2"] == "contenido_kg"        # la causa nunca se toca


def test_d6_r6b_no_degrada_mapeada_a_central():
    caso = _caso([[_atrib_q("noise_sensitivity", "contenido_kg",
                            "el criterio básico es la capacidad de pago")]])
    F = _F(("El criterio básico es la capacidad de pago en el futuro", True),
           ("otro claim secundario", False))
    out = aplicar_d6(caso, F, [])
    a = out["repeticiones"][0]["atribuciones"][0]
    assert a["jerarquia"] == "primaria" and "capa_d6" not in a


def test_d6_r6b_claim_no_mapeado_triage_sin_degradar():
    caso = _caso([[_atrib_q("faithfulness", "alucinacion_agente", "una glosa sin relación")]])
    F = _F(("un claim que no comparte texto", False))
    out = aplicar_d6(caso, F, [])
    a = out["repeticiones"][0]["atribuciones"][0]
    assert a["capa_d6"] == {"regla": "R6b", "accion": "claim_no_mapeado"}
    assert a["jerarquia"] == "primaria"              # sin mapeo no hay reescritura
    out["voto_capa_d"] = _voto([["faithfulness", "alucinacion_agente"]])
    final = aplicar_d4(out)
    assert "atribucion_no_verificable" in final["triage_capa_d"]["motivos"]


def test_d6_context_recall_intacta_con_pata():
    caso = _caso([[_atrib_q("context_recall", "alcanzabilidad_kg", "lo que sea")]])
    out = aplicar_d6(caso, _F(("claim", False)), ["pata no cubierta"])
    a = out["repeticiones"][0]["atribuciones"][0]
    assert a["jerarquia"] == "primaria" and "capa_d6" not in a


def test_d6_recomputo_final_degradacion_a_clave_vacia():
    # 2 reps, cada una con UNA primaria noise/contenido mapeada solo a un claim secundario:
    # tras D6 el voto final pasa de par-primario a CLAVE VACÍA; voto_pre_d6 lo preserva.
    quote = "límite del 17% está vigente hasta el 30/06/26"
    caso = _caso([[_atrib_q("noise_sensitivity", "contenido_kg", quote)],
                  [_atrib_q("noise_sensitivity", "contenido_kg", quote)]])
    F = _F(("Ese límite del 17% está vigente hasta el 30/06/26", False))
    out = aplicar_capa(caso, _index(), pregunta=PREGUNTA, consultas_agente=[],
                       tokens_expuestos=set(), outputs_completos=[],
                       sintoma_F=F, sintoma_P=[])
    assert out["version_capa"] == "v6.1-D(2026-07)"
    assert out["voto_pre_d6"]["pares_primarios_ganadores"] == [["noise_sensitivity", "contenido_kg"]]
    v = out["voto_capa_d"]
    assert v["pares_primarios_ganadores"] == [] and v["votos_ganadores"] == 2
    for rep in out["repeticiones"]:
        assert rep["atribuciones"][0]["jerarquia"] == "secundaria"
    assert out["triage_capa_d"]["triage"] is False or "atribucion_sin_sintoma" not in out["triage_capa_d"]["motivos"]


def test_d6_pipeline_orden_y_determinismo():
    quote = "límite del 17% está vigente hasta el 30/06/26"
    caso = _caso([[_atrib("context_recall", "navegación", "restriccion_r7"),
                   _atrib_q("noise_sensitivity", "contenido_kg", quote)],
                  [_atrib_q("faithfulness", "alucinacion_agente", "glosa sin relación")]])
    F = _F(("Ese límite del 17% está vigente hasta el 30/06/26", False))
    def correr():
        return aplicar_capa(copy.deepcopy(caso), _index(), pregunta=PREGUNTA,
                            consultas_agente=[], tokens_expuestos=set(),
                            outputs_completos=[], sintoma_F=F, sintoma_P=["pata x"])
    o1, o2 = correr(), correr()
    assert o1 == o2
    # orden: D2 corrigió la frontera ANTES de D6 (capa_d presente) y D6 degradó después
    r1a1, r1a2 = o1["repeticiones"][0]["atribuciones"]
    assert r1a1["capa_d"]["modulo"] == "D2" and r1a1["causa_capa2"] == "alcanzabilidad_kg"
    assert r1a2["capa_d6"]["decision_codigo"] == "secundaria"
    # la glosa no mapeada de la rep 2 fue a triage por R6b
    assert "atribucion_no_verificable" in o1["triage_capa_d"]["motivos"]
