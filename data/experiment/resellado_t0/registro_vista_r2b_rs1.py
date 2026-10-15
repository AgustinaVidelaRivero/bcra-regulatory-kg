"""Re-sellado único de los grafos r2b de la tanda 0 (mandato firmado el 15/10/2026, 67fe5b14), §3.3: registro EN MEMORIA
de la vista runtime de los cuatro grafos re-sellados (diez y desarrollo, completos y sin la cola), con el patrón de
data/experiment/sincola_t0/registro_vista_r2b_sincola.py y de data/experiment/tanda0/code/comun_tanda0.py, sin editarlos:
agrega las cuatro claves a la tabla TANDA0 en memoria y vuelve a llamar a su registro (idempotente). Lo importa
data/experiment/neo4j/grafos.py (cargar_vista_runtime) por los campos requiere_registro_dir y requiere_registro_modulo
de las entradas KG_Tanda0_*_rs1. La vista es la de comun_tanda0.cargar_runtime_gen3; el kg.json no se toca. r2b no se
evalúa con EV2 (laudo de r2, §3.1, punto 7): esta vista sirve a la carga en Neo4j y a su verificación.

Declara además, para los dos grafos sin la cola, las citas irresolubles por «punto sin nodos» desglosadas como en
U-SINCOLA-T0: total; de ellas, con destino en una unidad excluida del grafo evaluado por la regla de la cola; netas; y la
cifra del grafo completo re-sellado al lado. La cola es la de la tanda 0 tal como la deja R0: las unidades con estado
cola_humana* como última versión en corpus_tanda0/salida_r2b/*/finales.jsonl, o una de sus partes
(`<destino>::parteN`). La unidad de conteo es el ítem de `irresolubles` del registro de remisiones
(`<ensamblado>/r2/remisiones_registro.json`); el reporte del ensamblado (`remite_a.irresolubles_por_causa`) cuenta sin
repetir; se declaran las dos. `desglose_punto_sin_nodos(clave)` recomputa las cifras desde esos archivos (solo lectura) y
`verificar_desglose()` las compara con las declaradas.
"""
import json
import sys
from collections import Counter
from pathlib import Path

CODE_T0 = Path(__file__).resolve().parents[1] / "tanda0" / "code"   # data/experiment/tanda0/code
if str(CODE_T0) not in sys.path:
    sys.path.insert(0, str(CODE_T0))

import comun_tanda0 as T0   # noqa: E402  (registra la tanda 0 al importarse)

R2B_RS1 = {
    "tanda0_ens_desarrollo_r2b_rs1": {
        "path": T0.ENS_DIR / "ens_desarrollo_r2b_rs1" / "r2" / "kg.json",
        "sha256": "acb26dca0885e9ea83ab02637f15c1dac57885f0cf017c5fb16173ac7dfcac31",
        "label": "r2b_desarrollo_rs1_mem",
    },
    "tanda0_ens_diez_r2b_rs1": {
        "path": T0.ENS_DIR / "ens_diez_r2b_rs1" / "r2" / "kg.json",
        "sha256": "fda6c07dbb95602f5992f7e1ad9bf148ff1c2a72b9f69ff2ebbce891c15740ea",
        "label": "r2b_diez_rs1_mem",
    },
    "tanda0_ens_desarrollo_r2b_sincola_rs1": {
        "path": T0.ENS_DIR / "ens_desarrollo_r2b_sincola_rs1" / "r2" / "kg.json",
        "sha256": "66e745f57397ab754cde09eb641e9f0d9ef6259ea7e6445d086ecbf1c36dcc6c",
        "label": "r2b_desarrollo_sincola_rs1_mem",
    },
    "tanda0_ens_diez_r2b_sincola_rs1": {
        "path": T0.ENS_DIR / "ens_diez_r2b_sincola_rs1" / "r2" / "kg.json",
        "sha256": "61dd1b69ba03e40499845c40a6a8bec4c22d892ebe95823c7d5a569110f08738",
        "label": "r2b_diez_sincola_rs1_mem",
    },
}

# El grafo completo re-sellado de cada grafo sin la cola, para la cifra «al lado».
GRAFO_COMPLETO = {
    "tanda0_ens_diez_r2b_sincola_rs1": T0.ENS_DIR / "ens_diez_r2b_rs1",
    "tanda0_ens_desarrollo_r2b_sincola_rs1": T0.ENS_DIR / "ens_desarrollo_r2b_rs1",
}

# Desglose declarado, recomputado con el código de abajo sobre los ensamblados re-sellados.
PUNTO_SIN_NODOS = {
    "tanda0_ens_diez_r2b_sincola_rs1": {
        "registro": {"entradas": 1473, "irresolubles": 540, "punto_sin_nodos_total": 212,
                     "con_destino_en_unidad_excluida": 0, "netas": 212},
        "reporte": {"citas_irresolubles": 530, "punto_sin_nodos": 212},
        "grafo_completo": {"registro": {"entradas": 1510, "irresolubles": 503, "punto_sin_nodos_total": 213,
                                        "con_destino_en_unidad_excluida": 0, "netas": 213},
                           "reporte": {"citas_irresolubles": 495, "punto_sin_nodos": 213}},
    },
    "tanda0_ens_desarrollo_r2b_sincola_rs1": {
        "registro": {"entradas": 1259, "irresolubles": 455, "punto_sin_nodos_total": 174,
                     "con_destino_en_unidad_excluida": 0, "netas": 174},
        "reporte": {"citas_irresolubles": 445, "punto_sin_nodos": 174},
        "grafo_completo": {"registro": {"entradas": 1289, "irresolubles": 418, "punto_sin_nodos_total": 175,
                                        "con_destino_en_unidad_excluida": 0, "netas": 175},
                           "reporte": {"citas_irresolubles": 410, "punto_sin_nodos": 175}},
    },
}


def unidades_de_la_cola() -> list:
    """Las unidades con estado cola_humana* como última versión en salida_r2b/*/finales.jsonl."""
    u = {}
    for f in sorted((T0.ENS_DIR / "salida_r2b").glob("*/finales.jsonl")):
        for linea in f.read_text(encoding="utf-8").splitlines():
            if linea.strip():
                o = json.loads(linea)
                u[o["chunk_id"]] = o["estado"]
    return sorted(k for k, v in u.items() if str(v).startswith("cola_humana"))


def _desglose_dir(d: Path, cola: list) -> dict:
    reg = json.loads((d / "r2" / "remisiones_registro.json").read_text(encoding="utf-8"))
    rep = json.loads((d / "r2" / "reporte_ensamblado_r2.json").read_text(encoding="utf-8"))["remite_a"]
    items = [x for e in reg for x in e.get("irresolubles", [])]
    psn = [x for x in items if x["causa"] == "punto_sin_nodos"]

    def excluida(destino: str) -> bool:
        return any(c == destino or c.startswith(destino + "::") for c in cola)
    m = sum(1 for x in psn if excluida(x["destino"]))
    return {"registro": {"entradas": len(reg), "irresolubles": len(items), "punto_sin_nodos_total": len(psn),
                         "con_destino_en_unidad_excluida": m, "netas": len(psn) - m},
            "reporte": {"citas_irresolubles": rep["citas_irresolubles"],
                        "punto_sin_nodos": rep["irresolubles_por_causa"].get("punto_sin_nodos", 0)},
            "por_causa_registro": dict(sorted(Counter(x["causa"] for x in items).items()))}


def desglose_punto_sin_nodos(clave: str) -> dict:
    """Recomputa el desglose de `clave` (y el del grafo completo) desde los archivos. Solo lectura."""
    cola = unidades_de_la_cola()
    d = R2B_RS1[clave]["path"].parents[1]
    out = _desglose_dir(d, cola)
    out["grafo_completo"] = _desglose_dir(GRAFO_COMPLETO[clave], cola)
    out["unidades_de_la_cola"] = len(cola)
    return out


def verificar_desglose() -> dict:
    """Compara el desglose declarado con el recomputado; True por grafo si coinciden en todas las cifras declaradas."""
    res = {}
    for clave, decl in PUNTO_SIN_NODOS.items():
        rec = desglose_punto_sin_nodos(clave)
        igual = (rec["registro"] == decl["registro"] and rec["reporte"] == decl["reporte"]
                 and rec["grafo_completo"]["registro"] == decl["grafo_completo"]["registro"]
                 and rec["grafo_completo"]["reporte"] == decl["grafo_completo"]["reporte"])
        res[clave] = {"igual_a_lo_declarado": igual, "recomputado": rec}
    return res


def registrar_r2b_rs1() -> None:
    T0.TANDA0.update(R2B_RS1)
    T0.registrar_tanda0()


registrar_r2b_rs1()

if __name__ == "__main__":
    print(json.dumps(verificar_desglose(), ensure_ascii=False, indent=1))
