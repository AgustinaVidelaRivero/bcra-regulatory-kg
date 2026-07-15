"""Tests unitarios de test_alcanzabilidad.py (D1). Sin API, sin disco: grafo sintético."""

import copy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from loader import KnowledgeGraph, Node
from harness import GraphIndex
from test_alcanzabilidad import evaluar_alcanzabilidad, STOPWORDS_ES


def _kg_sintetico():
    """Grafo sintético de 6 nodos que ejercita los 4 escenarios del pedido."""
    nodes = [
        # 1) alcanzable por label desde la pregunta
        Node(id="restriccion_exclusion", type="Restriccion",
             label="Exclusión de deudores de clasificación",
             properties={"descripcion": "Deudores que no deben ser objeto de clasificación"},
             provenances=[]),
        # 2) inalcanzable: la regla vive SOLO en descripcion; label/id sin vocabulario de la pregunta
        Node(id="restriccion_r7", type="Restriccion",
             label="Norma siete",
             properties={"descripcion": "Los deudores cubiertos con garantías preferidas A no se clasifican"},
             provenances=[]),
        # 3) alcanzable solo vía token expuesto (no de la pregunta): 'moratoria'
        Node(id="restriccion_moratoria", type="Restriccion",
             label="Moratoria vigente",
             properties={"descripcion": "Suspensión transitoria de la clasificación"},
             provenances=[]),
        # 4) caso borde del token truncado: id termina en 'garanti'
        Node(id="restriccion_cubiertas_con_garanti", type="Restriccion",
             label="Prohibición por cobertura",
             properties={"descripcion": "Cubiertas totalmente con garantías preferidas A"},
             provenances=[]),
        # relleno
        Node(id="operacion_evaluacion", type="Operacion",
             label="Evaluación de capacidad de repago de deudores",
             properties={}, provenances=[]),
        Node(id="texto_ordenado", type="TextoOrdenado",
             label="Clasificación de Deudores",
             properties={}, provenances=[]),
    ]
    return KnowledgeGraph(run_key="sintetico", path=Path("<memoria>"), nodes=nodes, edges=[])


PREGUNTA = "¿Qué deudores no deben ser objeto de clasificación?"


def _index():
    return GraphIndex(_kg_sintetico())


def test_alcanzable_por_label():
    r = evaluar_alcanzabilidad("restriccion_exclusion", PREGUNTA, [], set(), _index())
    assert r["alcanzable"] is True
    # la pregunta entera ya lo alcanza (rank 2: el desempate por label más corto del
    # índice pone primero a "Clasificación de Deudores" con el mismo score — réplica fiel)
    entera = next(c for c in r["consultas"] if c["origen"] == "pregunta_entera")
    assert entera["en_top10"] and entera["rank"] == 2
    assert "deudores" in entera["tokens_matcheados"] and "clasificacion" in entera["tokens_matcheados"]


def test_inalcanzable_contenido_solo_en_descripcion():
    # label "Norma siete" e id "restriccion_r7": ningún token de la pregunta ni de los
    # n-gramas los matchea (la descripcion NO se indexa: GraphIndex toma label+id).
    r = evaluar_alcanzabilidad("restriccion_r7", PREGUNTA, [], set(), _index())
    assert r["alcanzable"] is False
    assert all(c["score"] == 0 and c["rank"] is None for c in r["consultas"])


def test_alcanzable_solo_via_token_expuesto():
    # 'moratoria' no está en la pregunta: solo llega si el agente lo usa en una consulta
    # (vocabulario aprendido de un output expuesto). Sin esa consulta, inalcanzable.
    sin_consulta = evaluar_alcanzabilidad("restriccion_moratoria", PREGUNTA, [], set(), _index())
    assert sin_consulta["alcanzable"] is False

    con_consulta = evaluar_alcanzabilidad(
        "restriccion_moratoria", PREGUNTA, ["moratoria clasificación"], {"moratoria"}, _index())
    assert con_consulta["alcanzable"] is True
    ganadora = next(c for c in con_consulta["consultas"] if c["en_top10"])
    assert ganadora["origen"] == "agente"
    # con el token declarado como expuesto, la consulta del agente queda DENTRO del
    # vocabulario ex ante...
    assert ganadora["tokens_fuera_vocabulario"] == []
    assert "moratoria" in con_consulta["vocabulario_ex_ante"]
    # ...y sin declararlo, la misma consulta queda marcada fuera de vocabulario
    # (mismo veredicto: los tokens_expuestos no cambian el conjunto de consultas).
    sin_declarar = evaluar_alcanzabilidad(
        "restriccion_moratoria", PREGUNTA, ["moratoria clasificación"], set(), _index())
    assert sin_declarar["alcanzable"] is True
    ganadora2 = next(c for c in sin_declarar["consultas"] if c["en_top10"])
    assert ganadora2["tokens_fuera_vocabulario"] == ["moratoria"]


def test_token_truncado_garanti_vs_garantias():
    # El id indexa 'garanti' (truncado); la consulta dice 'garantias' → ese token NO matchea.
    r = evaluar_alcanzabilidad(
        "restriccion_cubiertas_con_garanti", PREGUNTA,
        ["garantías preferidas A"], set(), _index())
    consulta = next(c for c in r["consultas"] if c["consulta"] == "garantías preferidas A")
    assert consulta["score"] == 0          # 'garantias' ≠ 'garanti'; 'preferidas'/'a' tampoco están
    assert consulta["rank"] is None
    assert consulta["tokens_matcheados"] == []
    # control positivo: con el token del propio id, sí matchea
    r2 = evaluar_alcanzabilidad(
        "restriccion_cubiertas_con_garanti", PREGUNTA,
        ["cubiertas con garanti"], set(), _index())
    directa = next(c for c in r2["consultas"] if c["consulta"] == "cubiertas con garanti")
    assert directa["score"] >= 2 and directa["en_top10"]


def test_determinismo():
    args = ("restriccion_exclusion", PREGUNTA,
            ["garantías preferidas A", "deudores clasificación"], {"moratoria"})
    r1 = evaluar_alcanzabilidad(*args, _index())
    r2 = evaluar_alcanzabilidad(*args, _index())
    assert copy.deepcopy(r1) == copy.deepcopy(r2)


def test_stopwords_no_generan_ngramas():
    r = evaluar_alcanzabilidad("restriccion_exclusion", PREGUNTA, [], set(), _index())
    for c in r["consultas"]:
        if c["origen"] == "ngrama_pregunta":
            assert not (set(c["consulta"].split()) & STOPWORDS_ES)


def test_portador_inexistente():
    import pytest
    with pytest.raises(ValueError):
        evaluar_alcanzabilidad("no_existe", PREGUNTA, [], set(), _index())
