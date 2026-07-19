"""Test sintético del camino (c) de D7 (diseño ciclo 2 §2c) — LAGUNA DE COBERTURA del
material quemado: en CQN-007 el LLM votó navegación las 3 veces, así que el camino
"LLM votó alcanzabilidad + puntero presente → CORRIGE a navegación con discrepancia"
no aparece en ninguna corrida real. Este test lo cubre con inyección pura (sin disco,
sin API). Espejo incluido: LLM votó navegación → discrepancia=False."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from test_alcanzabilidad_test import _kg_sintetico, PREGUNTA
from harness import GraphIndex
from capa_deterministica_v62 import aplicar_d2_v62


def _index():
    return GraphIndex(_kg_sintetico())


def _atrib(causa, ubicacion):
    return {
        "sintoma_capa1": "context_recall", "causa_capa2": causa, "lado": "?",
        "jerarquia": "primaria", "pata": "pata de prueba",
        "evidencia": {
            "afirmacion": {"quote": "x", "ubicacion": "respuesta final"},
            "nodo": {"quote": "y", "ubicacion": ubicacion},
            "fuente": {"quote": "z", "ubicacion": "pdf"},
        },
    }


def _caso(causa):
    return {
        "id_falla": "sintetico/CQ-000", "run": "sintetico", "n_reps": 1,
        "voto": {"resultado": "mayoria", "marca": "ORIGINAL"},
        "repeticiones": [{"formato_invalido": False, "errores_formato": [],
                          "atribuciones": [_atrib(causa, "restriccion_r7 (paso 3)")]}],
    }


# restriccion_r7 es D1-NEGATIVO desde la pregunta (probado en los tests de D1: la regla
# vive solo en description; label/id sin vocabulario de la pregunta).
PUNTEROS = {"restriccion_r7": {"paso": 5, "relacion": "aplica_a",
                               "nodo_consultado": "restriccion_exclusion"}}


def test_camino_c_llm_alcanzabilidad_d7_corrige_con_discrepancia():
    out = aplicar_d2_v62(_caso("alcanzabilidad_kg"), _index(),
                         pregunta=PREGUNTA, consultas_agente=[], tokens_expuestos=set(),
                         punteros=PUNTEROS)
    a = out["repeticiones"][0]["atribuciones"][0]
    assert a["causa_capa2"] == "navegación"          # la causa final es navegación
    assert a["capa_d"]["modulo"] == "D7"             # decidió el puntero estructural
    assert a["capa_d"]["discrepancia"] is True       # spec §2c: se CORRIGE, con discrepancia
    assert a["capa_d"]["emision_llm"] == "alcanzabilidad_kg"   # emisión preservada
    assert a["capa_d"]["puntero_estructural"] is True
    assert a["capa_d"]["evidencia"] == PUNTEROS["restriccion_r7"]
    assert a["capa_d"]["alcanzable"] is False        # D1 negativo (fila 2, no fila 1)


def test_espejo_llm_navegacion_d7_preserva_sin_discrepancia():
    out = aplicar_d2_v62(_caso("navegación"), _index(),
                         pregunta=PREGUNTA, consultas_agente=[], tokens_expuestos=set(),
                         punteros=PUNTEROS)
    a = out["repeticiones"][0]["atribuciones"][0]
    assert a["causa_capa2"] == "navegación"
    assert a["capa_d"]["modulo"] == "D7"
    assert a["capa_d"]["discrepancia"] is False      # el voto del LLM sobrevive
    assert a["capa_d"]["emision_llm"] == "navegación"


def test_fila_3_sin_puntero_sigue_como_hoy():
    # control: mismo portador D1-negativo, SIN puntero → alcanzabilidad_kg (fila 3, D2)
    out = aplicar_d2_v62(_caso("navegación"), _index(),
                         pregunta=PREGUNTA, consultas_agente=[], tokens_expuestos=set(),
                         punteros={})
    a = out["repeticiones"][0]["atribuciones"][0]
    assert a["causa_capa2"] == "alcanzabilidad_kg"
    assert a["capa_d"]["modulo"] == "D2"
    assert a["capa_d"]["discrepancia"] is True
