"""Tests unitarios de capa_deterministica.py (D2). Sin API, sin disco:
grafo sintético de D1 + casos_json sintéticos construidos acá."""

import copy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from harness import GraphIndex
from test_alcanzabilidad_test import _kg_sintetico, PREGUNTA
from capa_deterministica import aplicar_d2, aplicar_d3, aplicar_d4, aplicar_capa, VERSION_CAPA


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
    return aplicar_capa(caso, _index(), pregunta=PREGUNTA, consultas_agente=[],
                        tokens_expuestos=set())


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
