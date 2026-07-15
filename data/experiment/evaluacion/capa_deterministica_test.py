"""Tests unitarios de capa_deterministica.py (D2). Sin API, sin disco:
grafo sintético de D1 + casos_json sintéticos construidos acá."""

import copy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from harness import GraphIndex
from test_alcanzabilidad_test import _kg_sintetico, PREGUNTA
from capa_deterministica import aplicar_d2


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
