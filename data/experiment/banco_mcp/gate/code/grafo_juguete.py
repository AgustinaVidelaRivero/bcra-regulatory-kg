#!/usr/bin/env python3
"""grafo_juguete.py — Mini-grafo sintético PROPIO de U-A2.0-gate.

No usa Neo4j, no usa `kg.json` sellado, no abre material EV2. Es un grafo de
juguete de 9 nodos construido para que cada una de las cuatro clases de la
regla de atribución (`ev2_reporte/regla_atribucion.md` §4) sea alcanzable con
una secuencia corta de tool calls, más los bordes que el gate necesita.

Por qué usa `TO_exterior_cambios_actual.pdf` como `source_doc`: el parser de
anclas sellado (`sinteticas/comun.py:DOC2TO`) solo reconoce los cinco PDFs del
subset; una provenance con otro documento no produce ancla y el censo la
ignora. Es el mismo recurso que usa el selftest de A0.2 (`atribucion_fallas.
_mini_grafo`). El contenido es inventado: NO se abre ni se cita material real.

Mapa de anclas (to = 'ext'):
  ext:6.11  -> Obligacion_ancla_alfa      presente, hallable por búsqueda léxica
  ext:7.4   -> Restriccion_ancla_beta     presente, vocabulario disjunto (alcanzabilidad)
  ext:8.2   -> Obligacion_ancla_gamma     presente, aparece en búsqueda (vista_no_consultada)
  ext:10.1  -> Obligacion_ancla_delta     presente, output GRANDE (> cap de transporte)
  ext:3.3   -> SOLO el contenedor         => ausencia_kg (contenedor > 10 anclas, excluido)
  ext:9.9   -> nadie                      => ausencia_kg (ausencia total)

Aristas (para llegar al ancla por vecindad, sin verla nunca en una búsqueda):
  Operacion_puente_epsilon --aplica_a--> Obligacion_ancla_alfa
  Obligacion_ancla_alfa --restringido_por--> Restriccion_ancla_beta

Uso:
  python3 -B grafo_juguete.py --escribir <ruta.json>
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

DOC = "TO_exterior_cambios_actual.pdf"

# Tamaño del nodo grande: elegido para superar con margen el cap medido del
# transporte Bash de Claude Code (30.000 chars de stdout, ver
# inventario_campos.md §5). El texto es un relleno determinístico.
RELLENO_CHARS = 42000


def _prov(punto: str, cola: str = "texto sintético") -> list[dict]:
    return [{"source_doc": DOC, "location": f"Punto {punto}. {cola}"}]


def _relleno(n: int) -> str:
    """Relleno determinístico y sin acentos (estable byte a byte)."""
    base = ("parrafo sintetico de relleno para forzar un output por encima del "
            "cap de transporte medido; sin contenido regulatorio real. ")
    return (base * (n // len(base) + 1))[:n]


def construir() -> dict:
    nodes = [
        {"id": "Obligacion_ancla_alfa", "type": "Obligacion",
         "label": "Obligacion alfa de acreditacion de fondos",
         "properties": {"descripcion": "Contenido sintetico del ancla alfa (ext:6.11).",
                        "sujeto": "entidad alcanzada"},
         "provenances": _prov("6.11")},
        {"id": "Restriccion_ancla_beta", "type": "Restriccion",
         "label": "Restriccion beta sobre plazos de liquidacion",
         "properties": {"descripcion": "Contenido sintetico del ancla beta (ext:7.4)."},
         "provenances": _prov("7.4")},
        {"id": "Obligacion_ancla_gamma", "type": "Obligacion",
         "label": "Obligacion gamma de acreditacion complementaria",
         "properties": {"descripcion": "Contenido sintetico del ancla gamma (ext:8.2)."},
         "provenances": _prov("8.2")},
        {"id": "Obligacion_ancla_delta", "type": "Obligacion",
         "label": "Obligacion delta de registro extenso",
         "properties": {"descripcion": _relleno(RELLENO_CHARS)},
         "provenances": _prov("10.1")},
        {"id": "Operacion_puente_epsilon", "type": "Operacion",
         "label": "Operacion epsilon puente de acreditacion",
         "properties": {"descripcion": "Nodo puente: su vecino saliente es el ancla alfa."},
         "provenances": _prov("6.12")},
        {"id": "Excepcion_senuelo_zeta", "type": "Excepcion",
         "label": "Excepcion zeta de acreditacion de fondos",
         "properties": {"descripcion": "Señuelo lexico: compite con alfa en la busqueda."},
         "provenances": _prov("6.13")},
        {"id": "Procedimiento_senuelo_eta", "type": "Procedimiento",
         "label": "Procedimiento eta de acreditacion complementaria",
         "properties": {"descripcion": "Señuelo lexico: compite con gamma en la busqueda."},
         "provenances": _prov("8.3")},
        {"id": "Concepto_aislado_theta", "type": "Concepto",
         "label": "Concepto theta sin aristas",
         "properties": {"descripcion": "Nodo aislado: ver_vecinos devuelve listas vacias."},
         "provenances": _prov("11.5")},
        # Contenedor: porta 11 anclas distintas (> CONTENEDOR_MAX_ANCLAS = 10),
        # así que el censo lo excluye y ext:3.3 queda sin portador.
        {"id": "TextoOrdenado_contenedor", "type": "TextoOrdenado",
         "label": "Texto Ordenado sintetico contenedor",
         "properties": {"descripcion": "Contenedor: portador unico de ext:3.3."},
         "provenances": [{"source_doc": DOC, "location": f"Punto 3.{i}. contenedor"}
                         for i in range(1, 12)]},
    ]
    edges = [
        {"source": "Operacion_puente_epsilon", "target": "Obligacion_ancla_alfa",
         "relation": "aplica_a", "properties": {}, "provenances": _prov("6.12")},
        {"source": "Obligacion_ancla_alfa", "target": "Restriccion_ancla_beta",
         "relation": "restringido_por", "properties": {}, "provenances": _prov("6.11")},
        {"source": "Obligacion_ancla_gamma", "target": "Obligacion_ancla_alfa",
         "relation": "complementa_a", "properties": {}, "provenances": _prov("8.2")},
    ]
    return {"nodes": nodes, "edges": edges}


def sha256_de(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--escribir", type=Path, required=True)
    a = ap.parse_args()
    raw = construir()
    b = (json.dumps(raw, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    a.escribir.parent.mkdir(parents=True, exist_ok=True)
    a.escribir.write_bytes(b)
    print(f"{a.escribir}: {len(raw['nodes'])} nodos, {len(raw['edges'])} aristas, "
          f"{len(b)} bytes, sha256 {sha256_de(b)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
