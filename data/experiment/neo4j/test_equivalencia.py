"""
test_equivalencia.py — Adaptador Neo4j vs GraphIndex in-memory, 30 consultas.

Compara el output de Neo4jIndex contra el GraphIndex del harness (ambos sobre
el MISMO grafo: reensamblado_v3 vía loader con adaptador nulo) para 30
consultas variadas:

  - 10 ver_nodo      -> se exige igualdad EXACTA (dict completo), incluido el
                        caso de id inexistente (mismo mensaje de error).
  - 10 ver_vecinos   -> igualdad EXACTA (orden incluido, vía r.orden), con
                        casos de dirección explícita, bidireccional, hub con
                        truncamiento (>40 vecinos) e id inexistente.
  - 10 buscar_nodos  -> las divergencias son ESPERABLES (full-text vs léxico
                        de label+id): se reportan estructuradas (totales,
                        solapamiento de ids del top, posiciones), NO se
                        "corrigen". Son la mejora/observación a documentar.

Salida: resumen por consulta en stdout + detalle JSON en
  test_equivalencia_resultados.json (junto a este script).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

NEO4J_DIR = Path(__file__).resolve().parent
EVAL_DIR = NEO4J_DIR.parent / "evaluacion"
sys.path.insert(0, str(EVAL_DIR))
sys.path.insert(0, str(NEO4J_DIR))

from loader import load_graph_from_path  # noqa: E402
from harness import GraphIndex  # noqa: E402
from conexion import abrir_driver  # noqa: E402
from neo4j_index import Neo4jIndex  # noqa: E402
from cargar_kg import KG_PATH  # noqa: E402

SALIDA_JSON = NEO4J_DIR / "test_equivalencia_resultados.json"

# --- 10 ver_nodo: ids reales variados (uno por type + casos con provenance
#     múltiple en el crudo + nota_fuente) y 1 inexistente -------------------
CASOS_VER_NODO = [
    "Obligacion_cumplir_requerimientos_informacion_bcra_2d1942",
    "Operacion_compra_simultanea_con_liquidacion_de_divisas_ed538c",
    "Restriccion_prohibicion_de_incremento_de_posicion_a_primera_perdida_b9fc82",
    "Comunicacion_a_6146",           # crudo trae 3 provenances (vista loader: 1)
    "Excepcion_otros_proveedores_no_financieros_de_credito_alcanzados_por_las_normas_sobre_prov_5f95b9",
    "Sujeto_rol_sujeto_obligado_proteccion",
    "TextoOrdenado_to_proteccion_usuarios_servicios_financieros_actual_pdf",
    "Sujeto_entidad_financiera",
    "Operacion_clasificacion_de_deudor_de_la_cartera_comercial_con_seguimiento_especial_6_5_2_s_1d1a4b",  # con nota_fuente
    "Nodo_Inexistente_XYZ",          # error dict idéntico esperado
]

# --- 10 ver_vecinos: (id, direccion) ---------------------------------------
CASOS_VER_VECINOS = [
    ("Sujeto_rol_sujeto_obligado_proteccion", "entrantes"),   # BKL-0027
    ("Sujeto_rol_sujeto_obligado_proteccion", "ambas"),
    ("Sujeto_entidad_financiera", "ambas"),                   # hub (truncamiento)
    ("Sujeto_entidad_financiera", "salientes"),
    ("Comunicacion_a_6312", "ambas"),
    ("Excepcion_otros_proveedores_no_financieros_de_credito_alcanzados_por_las_normas_sobre_prov_5f95b9", "ambas"),
    ("TextoOrdenado_to_exterior_cambios_actual_pdf", "entrantes"),  # hub máximo (1512 aristas)
    ("Operacion_compra_de_opciones_0f6162", "ambas"),
    ("Obligacion_cumplir_requerimientos_informacion_bcra_2d1942", "direccion_invalida"),  # cae a "ambas"
    ("Nodo_Inexistente_XYZ", "ambas"),                        # error dict
]

# --- 10 buscar_nodos: consultas variadas (divergencias esperables) ----------
CASOS_BUSCAR = [
    "efectivo mínimo",
    "tarjetas de crédito",
    "asociación mutual",
    "asociaciones mutuales o cooperativas",
    "excepto que se trate de asociaciones mutuales",   # verbatim solo-descripcion
    "sujetos obligados protección de usuarios",
    "liquidación de divisas exportaciones",
    "comunicacion a 6312",
    "posición global neta de moneda extranjera",
    "graduación del crédito",
]


def comparar_exacto(nombre, a, b, detalles):
    igual = a == b
    detalles.append({"caso": nombre, "igual": igual,
                     **({} if igual else {"in_memory": a, "neo4j": b})})
    print(f"  {'✓' if igual else '✗'} {nombre}" + ("" if igual else "  <-- DIVERGE"))
    return igual


def comparar_busqueda(consulta, a, b, detalles):
    """Divergencias esperables: se describen, no se juzgan como falla."""
    ids_a = [r["id"] for r in a.get("resultados", [])]
    ids_b = [r["id"] for r in b.get("resultados", [])]
    solap = len(set(ids_a) & set(ids_b))
    identico = a == b
    d = {
        "consulta": consulta,
        "identico": identico,
        "total_in_memory": a.get("total_con_match", a.get("total")),
        "total_neo4j": b.get("total_con_match", b.get("total")),
        "top_in_memory": ids_a,
        "top_neo4j": ids_b,
        "solapamiento_top": f"{solap}/{max(len(ids_a), len(ids_b), 1)}",
        "mismo_primer_resultado": (ids_a[:1] == ids_b[:1]),
    }
    detalles.append(d)
    marca = "=" if identico else "≠"
    print(f"  {marca} {consulta!r}: total {d['total_in_memory']} vs "
          f"{d['total_neo4j']}, solapamiento top {d['solapamiento_top']}, "
          f"1er resultado {'igual' if d['mismo_primer_resultado'] else 'DISTINTO'}")
    return identico


def main():
    kg = load_graph_from_path(KG_PATH, adapter_key=None)
    gi = GraphIndex(kg)
    driver = abrir_driver()
    ni = Neo4jIndex(driver)
    detalles = {"ver_nodo": [], "ver_vecinos": [], "buscar_nodos": []}

    try:
        print("== ver_nodo (10 casos, igualdad exacta exigida) ==")
        ok_nodo = sum(
            comparar_exacto(nid, gi.ver_nodo(nid), ni.ver_nodo(nid),
                            detalles["ver_nodo"])
            for nid in CASOS_VER_NODO
        )

        print("\n== ver_vecinos (10 casos, igualdad exacta exigida) ==")
        ok_vec = sum(
            comparar_exacto(f"{nid} [{d}]",
                            gi.ver_vecinos(nid, direccion=d),
                            ni.ver_vecinos(nid, direccion=d),
                            detalles["ver_vecinos"])
            for nid, d in CASOS_VER_VECINOS
        )

        print("\n== buscar_nodos (10 casos, divergencias esperables) ==")
        identicas = sum(
            comparar_busqueda(q, gi.buscar_nodos(q), ni.buscar_nodos(q),
                              detalles["buscar_nodos"])
            for q in CASOS_BUSCAR
        )
    finally:
        driver.close()

    resumen = {
        "ver_nodo_iguales": f"{ok_nodo}/{len(CASOS_VER_NODO)}",
        "ver_vecinos_iguales": f"{ok_vec}/{len(CASOS_VER_VECINOS)}",
        "buscar_nodos_identicas": f"{identicas}/{len(CASOS_BUSCAR)}",
    }
    SALIDA_JSON.write_text(
        json.dumps({"resumen": resumen, "detalles": detalles},
                   ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"\nRESUMEN: {resumen}")
    print(f"detalle -> {SALIDA_JSON.name}")

    # Criterio de aceptación: paridad exacta donde corresponde; en búsqueda
    # las divergencias no son falla (son el objeto de la migración).
    exit_ok = (ok_nodo == len(CASOS_VER_NODO) and ok_vec == len(CASOS_VER_VECINOS))
    sys.exit(0 if exit_ok else 1)


if __name__ == "__main__":
    main()
