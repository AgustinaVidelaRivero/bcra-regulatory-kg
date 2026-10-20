"""B6.1, tanda final, T3, punto 5 (pre-registro firmado en 4de7f2a7, §7): registro EN MEMORIA de la vista runtime de los dos grafos
de la tanda final (completo y sin la cola), con el patrón de data/experiment/tanda1/t3/registro_vista_r2b_tanda1.py y de
data/experiment/tanda0/code/comun_tanda0.py, sin editarlos: agrega las dos claves a la tabla TANDA0 en memoria y vuelve a llamar a su
registro (idempotente). Lo importa data/experiment/neo4j/grafos.py (cargar_vista_runtime) por los campos requiere_registro_dir y
requiere_registro_modulo de las entradas KG_TandaFinal_r2b*. La vista es la de comun_tanda0.cargar_runtime_gen3; el kg.json no se
toca. r2b no se evalúa con EV2 (laudo de r2, §3, punto 6): esta vista sirve a la carga en Neo4j y a su verificación.

Declara además, para el grafo sin la cola, las citas irresolubles por «punto sin nodos» desglosadas como en el re-sellado: total; de
ellas, con destino en una unidad excluida del grafo evaluado por la regla de la cola; netas; y la cifra del grafo completo al lado. La
cola es la de la tanda final: las unidades con estado cola_humana* como última versión en corpus_tanda_final/salida_r2b/*/finales.jsonl,
o una
de sus partes (`<destino>::parteN`). La unidad de conteo es el ítem de `irresolubles` del registro de remisiones
(`<ensamblado>/r2/remisiones_registro.json`); el reporte del ensamblado (`remite_a.irresolubles_por_causa`) cuenta sin repetir; se
declaran las dos. `desglose_punto_sin_nodos(clave)` recomputa las cifras desde esos archivos (solo lectura) y `verificar_desglose()`
las compara con las declaradas. Lo generó data/experiment/tanda_final/t3/scripts/editar_grafos_tf.py.
"""
import json
import sys
from collections import Counter
from pathlib import Path

EXP = Path(__file__).resolve().parents[2]                    # data/experiment
CODE_T0 = EXP / "tanda0" / "code"
if str(CODE_T0) not in sys.path:
    sys.path.insert(0, str(CODE_T0))

import comun_tanda0 as T0   # noqa: E402  (registra la tanda 0 al importarse)

ENS_TF = EXP / "reextraccion_v2" / "corpus_tanda_final"

R2B_TANDA_FINAL = {
    "tandafinal_ens_98_r2b": {
        "path": ENS_TF / "ens_98_r2b" / "r2" / "kg.json",
        "sha256": "db2df7b7e707ef191d1df6fdb3638fd920cf4486afce13a7e889b9755155bc97",
        "label": "r2b_tandafinal_98_mem",
    },
    "tandafinal_ens_98_r2b_sincola": {
        "path": ENS_TF / "ens_98_r2b_sincola" / "r2" / "kg.json",
        "sha256": "c050f3c90ce5d32be759d2e5d05bbe2e131d9abf7811de097c97f4a1fe410cf7",
        "label": "r2b_tandafinal_98_sincola_mem",
    },
}

# El grafo completo del grafo sin la cola, para la cifra «al lado».
GRAFO_COMPLETO = {"tandafinal_ens_98_r2b_sincola": ENS_TF / "ens_98_r2b"}

# Desglose declarado, recomputado con el código de abajo sobre los ensamblados de la tanda final.
PUNTO_SIN_NODOS = {
    "tandafinal_ens_98_r2b_sincola": {
        "registro": {"entradas": 2408, "irresolubles": 1159, "punto_sin_nodos_total": 422,
                     "con_destino_en_unidad_excluida": 0, "netas": 422},
        "reporte": {"citas_irresolubles": 1135, "punto_sin_nodos": 417},
        "grafo_completo": {"registro": {"entradas": 2517, "irresolubles": 1180, "punto_sin_nodos_total": 441,
                                        "con_destino_en_unidad_excluida": 4, "netas": 437},
                           "reporte": {"citas_irresolubles": 1155, "punto_sin_nodos": 435}},
    },
}


def unidades_de_la_cola() -> list:
    """Las unidades con estado cola_humana* como última versión en corpus_tanda_final/salida_r2b/*/finales.jsonl."""
    u = {}
    for f in sorted((ENS_TF / "salida_r2b").glob("*/finales.jsonl")):
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
    d = R2B_TANDA_FINAL[clave]["path"].parents[1]
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


def registrar_r2b_tanda_final() -> None:
    T0.TANDA0.update(R2B_TANDA_FINAL)
    T0.registrar_tanda0()


registrar_r2b_tanda_final()

if __name__ == "__main__":
    print(json.dumps(verificar_desglose(), ensure_ascii=False, indent=1))
