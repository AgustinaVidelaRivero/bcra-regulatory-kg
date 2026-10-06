"""U-SINCOLA-T0, SC2, punto 2 (mandato 723680e; ensamblados de SC1-bis en 01046b6): registro EN MEMORIA de la vista
runtime de los dos grafos evaluados de la tanda 0 sin la cola humana, con el patrón de
data/experiment/reext_t0/t3bis/registro_vista_r2b.py y de data/experiment/tanda0/code/comun_tanda0.py, sin editarlos:
agrega las dos claves a la tabla TANDA0 en memoria y vuelve a llamar a su registro (idempotente). Lo importa
data/experiment/neo4j/grafos.py (cargar_vista_runtime) por los campos requiere_registro_dir y requiere_registro_modulo
de las entradas KG_Tanda0_*_r2b_sincola. La vista es la de comun_tanda0.cargar_runtime_gen3; el kg.json no se toca. r2b
no se evalúa con EV2 (laudo de r2, §3.1, punto 7): esta vista sirve a la carga en Neo4j y a su verificación.

Declara además, para cada grafo, las citas irresolubles por «punto sin nodos» desglosadas como fija la nota del
06/10/2026 al pie del mandato (revisión del FRENO SC1-bis, 01046b6): total; de ellas, con destino en una unidad excluida
del grafo evaluado por la regla de la cola (irresolubles por construcción y no por el detector); netas; y la cifra del
grafo completo (r2b sellado) al lado. La unidad de conteo es el ítem de `irresolubles` del registro de remisiones
(`<ensamblado>/r2/remisiones_registro.json`); el reporte del ensamblado (`remite_a.irresolubles_por_causa`) cuenta sin
repetir y por eso difiere en pocas unidades; se declaran las dos. «Destino en una unidad excluida»: el destino es una
unidad con estado cola_humana* como última versión en corpus_tanda0/salida_r2b/*/finales.jsonl, o una de sus partes
(`<destino>::parteN`). `desglose_punto_sin_nodos(clave)` recomputa las cifras desde esos archivos (solo lectura) y
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

R2B_SINCOLA = {
    "tanda0_ens_diez_r2b_sincola": {
        "path": T0.ENS_DIR / "ens_diez_r2b_sincola" / "r2" / "kg.json",
        "sha256": "e22fae1afc3cf37fbe5b49ee0b220d51d0ec5febc13abeb6ebf7b74226da34fb",
        "label": "r2b_diez_sincola_mem",
    },
    "tanda0_ens_desarrollo_r2b_sincola": {
        "path": T0.ENS_DIR / "ens_desarrollo_r2b_sincola" / "r2" / "kg.json",
        "sha256": "2922b72dca2c2bcb204a04f53fc89f265ac2c57e83e6aaab2ce1af8b82d413e4",
        "label": "r2b_desarrollo_sincola_mem",
    },
}

# El grafo completo (r2b sellado, c9540c0) de cada grafo evaluado, para la cifra «al lado».
GRAFO_COMPLETO = {
    "tanda0_ens_diez_r2b_sincola": T0.ENS_DIR / "ens_diez_r2b",
    "tanda0_ens_desarrollo_r2b_sincola": T0.ENS_DIR / "ens_desarrollo_r2b",
}

# Desglose declarado (06/10/2026), recomputado con desglose_punto_sin_nodos() sobre 01046b6.
PUNTO_SIN_NODOS = {
    "tanda0_ens_diez_r2b_sincola": {
        "registro": {"entradas": 1476, "irresolubles": 540, "punto_sin_nodos_total": 257,
                     "con_destino_en_unidad_excluida": 45, "netas": 212},
        "reporte": {"citas_irresolubles": 530, "punto_sin_nodos": 255},
        "grafo_completo": {"registro": {"entradas": 1515, "irresolubles": 503, "punto_sin_nodos_total": 213,
                                        "con_destino_en_unidad_excluida": 0, "netas": 213},
                           "reporte": {"citas_irresolubles": 495, "punto_sin_nodos": 213}},
    },
    "tanda0_ens_desarrollo_r2b_sincola": {
        "registro": {"entradas": 1263, "irresolubles": 456, "punto_sin_nodos_total": 217,
                     "con_destino_en_unidad_excluida": 43, "netas": 174},
        "reporte": {"citas_irresolubles": 446, "punto_sin_nodos": 215},
        "grafo_completo": {"registro": {"entradas": 1295, "irresolubles": 419, "punto_sin_nodos_total": 175,
                                        "con_destino_en_unidad_excluida": 0, "netas": 175},
                           "reporte": {"citas_irresolubles": 411, "punto_sin_nodos": 175}},
    },
}


def unidades_de_la_cola() -> list:
    """Las unidades con estado cola_humana* como última versión en salida_r2b/*/finales.jsonl (74 en la tanda 0)."""
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
    d = R2B_SINCOLA[clave]["path"].parents[1]
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


def registrar_r2b_sincola() -> None:
    T0.TANDA0.update(R2B_SINCOLA)
    T0.registrar_tanda0()


registrar_r2b_sincola()

if __name__ == "__main__":
    print(json.dumps(verificar_desglose(), ensure_ascii=False, indent=1))
