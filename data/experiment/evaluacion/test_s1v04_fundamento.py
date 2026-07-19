"""Tests sintéticos del requisito de fundamento (§4bis, unidad 2b). Sin API."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from harness import GraphIndex
from loader import Node, KnowledgeGraph
from s1_fuentes_v04 import _pasaje_funda, aplicar_s1_v04, UMBRAL_CONTENIDO


def _nodo(desc):
    return Node(id="nodo_x", type="Restriccion", label="Nodo X",
                properties={"description": desc}, provenances=[])


PASAJE = ("12.3. Para aquellas entidades financieras que sean reclasificadas desde el "
          "01/01/2026 como consecuencia de lo establecido en el punto 4.1, la exigencia "
          "de capital por riesgo operacional para entidades del grupo 2 no podrá superar "
          "el 17% del promedio de los últimos 36 meses de la exigencia por riesgo de crédito.")


def _entrada(pasaje):
    return {"pasaje_portador": {"pasaje": pasaje, "ref": "sintético (sin página)"},
            "provenance": {"source_doc": None, "location": "x"}}


def test_pasaje_que_funda():
    n = _nodo("la exigencia de capital por riesgo operacional para entidades del grupo 2 "
              "no podrá superar el 17% del promedio de los últimos 36 meses")
    funda, det = _pasaje_funda(n, _entrada(PASAJE))
    assert funda is True and det["span"] >= UMBRAL_CONTENIDO


def test_pasaje_que_no_funda():
    n = _nodo("los códigos de consolidación aplicables al régimen informativo de "
              "operaciones de cambio serán definidos por la Superintendencia en cada caso")
    funda, det = _pasaje_funda(n, _entrada(PASAJE))
    assert funda is False and det["span_maximo"] < UMBRAL_CONTENIDO


class _ClienteProhibido:
    """Falla si S1 intenta llamar: fuente_no_funda debe cortar ANTES de la llamada."""
    def __init__(self): self.messages = self
    def create(self, **kw): raise AssertionError("NO debía llamarse al LLM")


def test_fuente_no_funda_triage_sin_llamada():
    kg = GraphIndex(KnowledgeGraph(run_key="s", path=Path("<m>"),
                                   nodes=[_nodo("contenido cualquiera")], edges=[]))
    caso = {"id_falla": "s/CQ-0", "run": "s", "n_reps": 1,
            "voto": {"marca": "V"},
            "repeticiones": [{"formato_invalido": False, "atribuciones": [{
                "sintoma_capa1": "noise_sensitivity", "causa_capa2": "contenido_kg",
                "jerarquia": "primaria", "pata": "p",
                "evidencia": {"afirmacion": {"quote": "x", "ubicacion": "rf"},
                              "nodo": {"quote": "y", "ubicacion": "nodo_x"},
                              "fuente": {"quote": "z", "ubicacion": "pdf"}}}]}],
            "voto_capa_d": {"pares_primarios_ganadores": [["noise_sensitivity", "contenido_kg"]]}}
    paquete = {"gatillo_caso": {"exoneracion_con_sintoma": False},
               "atribuciones": [{"id_atribucion": "rep1_atrib1", "rep": 1, "atrib_idx": 1,
                                 "tipo_gatillo": "causa_gatillada",
                                 "estado": "fuente_no_funda",
                                 "portador_id": "nodo_x",
                                 "fundamento": {"span_maximo": 12, "umbral": UMBRAL_CONTENIDO}}]}
    out = aplicar_s1_v04(caso, kg, paquete, n=3, client=_ClienteProhibido(),
                         sintoma_F=[], sintoma_P=[])
    a = out["repeticiones"][0]["atribuciones"][0]
    assert a["capa_s1"]["accion"] == "fuente_no_funda"
    assert a["capa_s1"]["triage"] is True
    assert a["causa_capa2"] == "contenido_kg"            # sin reescritura
    assert out["triage_s1"]["motivos"] == ["fuente_no_funda"]
    assert out["resumen_s1"]["fuente_no_funda"] == 1
    assert out["resumen_s1"]["tokens_in_s1"] == 0        # CERO llamadas
