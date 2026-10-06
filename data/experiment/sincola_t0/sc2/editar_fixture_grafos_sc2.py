"""U-SINCOLA-T0, SC2, puntos 1 y 2 (mandato 723680e; «seguí» de SC2 con las decisiones 1 y 2): sobre una raíz (copia del
repo primero; el repo después, con el mismo script):
  1. scripts/regression_kg_esperado.json: SOLO dos entradas nuevas en `estado_esperado`, KG-Tanda0-Diez-r2b-sincola y
     KG-Tanda0-Desarrollo-r2b-sincola, copias de su entrada r2b sellada (expectativas sin cambiar ninguna) con el kg, el
     kg_sha256 y el registro_dir del ensamblado sin cola y el rótulo de la decisión 1. Antes de escribir verifica que la
     re-serialización del archivo es byte a byte igual (indent=1, ensure_ascii=False) y, después, que las entradas
     selladas quedan byte a byte iguales (texto canónico de cada una).
  2. data/experiment/neo4j/grafos.py: SOLO dos entradas nuevas, KG_Tanda0_Desarrollo_r2b_sincola y
     KG_Tanda0_Diez_r2b_sincola (decisión 2), insertadas después de KG_Tanda0_Diez_r2b por reemplazo exacto.
  3. data/experiment/sincola_t0/registro_vista_r2b_sincola.py: el registro de la vista (patrón de
     reext_t0/t3bis/registro_vista_r2b.py) con el desglose de «punto sin nodos».
Uso: python -B editar_sc2.py <raiz>
"""
import copy
import hashlib
import json
import sys
from pathlib import Path

RAIZ = Path(sys.argv[1]).resolve()
FIX = RAIZ / "scripts/regression_kg_esperado.json"
GRAFOS = RAIZ / "data/experiment/neo4j/grafos.py"
REG = RAIZ / "data/experiment/sincola_t0/registro_vista_r2b_sincola.py"
T0 = "data/experiment/reextraccion_v2/corpus_tanda0"
SHA = {"diez": "e22fae1afc3cf37fbe5b49ee0b220d51d0ec5febc13abeb6ebf7b74226da34fb",
       "desarrollo": "2922b72dca2c2bcb204a04f53fc89f265ac2c57e83e6aaab2ce1af8b82d413e4"}
N = {"diez": (8503, 26129), "desarrollo": (6723, 22084)}
COLA = {"diez": 74, "desarrollo": 59}

# ----------------------------------------------------------------------------------------- 1. la fixture
raw = FIX.read_text(encoding="utf-8")
fx = json.loads(raw)
assert json.dumps(fx, ensure_ascii=False, indent=1) + "\n" == raw, "la fixture no se re-serializa byte a byte"
ee = fx["estado_esperado"]
canon_antes = {k: json.dumps(v, ensure_ascii=False, sort_keys=True) for k, v in ee.items()}
for g, G in (("diez", "Diez"), ("desarrollo", "Desarrollo")):
    nombre = f"KG-Tanda0-{G}-r2b-sincola"
    assert nombre not in ee, f"{nombre} ya existe"
    kg = RAIZ / T0 / f"ens_{g}_r2b_sincola" / "r2" / "kg.json"
    sha = hashlib.sha256(kg.read_bytes()).hexdigest()
    assert sha == SHA[g], f"sha de {kg}: {sha}"
    e = copy.deepcopy(ee[f"KG-Tanda0-{G}-r2b"])
    e_nuevo = {
        "_rotulo": (f"GRAFO EVALUADO DE LA TANDA 0 SIN LA COLA HUMANA (U-SINCOLA-T0: ensamblado en SC1-bis, 01046b6; "
                    f"decisión 4 del mandato 723680e; entrada sellada por la autora con el «seguí» de SC2 del 06/10/2026): el r2b de "
                    f"{'los diez TOs' if g == 'diez' else 'los cinco TOs de desarrollo'} re-ensamblado sin las {COLA[g]} unidades de la cola "
                    f"humana (ensamblar_tanda0.py --sin-cola, enmienda 1 en 1f7c159). Las expectativas son las de la entrada "
                    f"KG-Tanda0-{G}-r2b sellada, sin cambiar ninguna (SC1.5 dio 0 cambios de estado; las 3 regresiones declaradas "
                    f"RT-C5-3, RT-C6-1 y RT-C6-2 siguen iguales). Rótulo heredado: " + e["_rotulo"]),
        "kg": f"{T0}/ens_{g}_r2b_sincola/r2/kg.json",
        "kg_sha256": sha,
        "_kg_sha256": ("sha256 del ensamblado sin la cola (SC1.3: doble corrida byte a byte en la copia y en el repo igual a la copia; "
                       "01046b6)."),
        "registro_dir": f"{T0}/ens_{g}_r2b_sincola/r2",
        "_registro_dir": "el registro del ensamblado nuevo (no_mapeados_sujetos.jsonl, omisiones.jsonl, reporte_ensamblado_r2.json): se pasa a la suite con --registro-dir.",
    }
    for k, v in e.items():
        if k not in e_nuevo:
            e_nuevo[k] = v
    e_nuevo["evidencia"] = f"Expectativas heredadas de KG-Tanda0-{G}-r2b. " + e["evidencia"]
    ee[nombre] = e_nuevo
canon_despues = {k: json.dumps(v, ensure_ascii=False, sort_keys=True) for k, v in ee.items() if k in canon_antes}
assert canon_antes == canon_despues, "una entrada sellada cambió"
FIX.write_text(json.dumps(fx, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("fixture: +2 entradas", [k for k in ee if k.endswith("sincola")])

# ----------------------------------------------------------------------------------------- 2. grafos.py
s = GRAFOS.read_text(encoding="utf-8")
ancla = ('        "indice_fulltext": "nodos_fulltext_kg_tanda0_diez_r2b",\n'
         '    },\n'
         '}\n'
         'CLAVES = list(GRAFOS.keys())\n')
assert s.count(ancla) == 1, "ancla de grafos.py no encontrada una sola vez"


def entrada(g: str, G: str) -> str:
    n, a = N[g]
    return (f'    "KG_Tanda0_{G}_r2b_sincola": {{\n'
            f'        "nombre_canonico": "KG-Tanda0-{G}-r2b-sincola",\n'
            f'        "label": "KG_Tanda0_{G}_r2b_sincola",\n'
            f'        "path": EXPERIMENT_DIR / "reextraccion_v2" / "corpus_tanda0" / "ens_{g}_r2b_sincola" / "r2" / "kg.json",\n'
            f'        "sha256": "{SHA[g]}",\n'
            f'        "commit_sellado": "PENDIENTE",\n'
            f'        "n_nodos": {n},\n'
            f'        "n_aristas": {a},\n'
            f'        "ev2_key": "tanda0_ens_{g}_r2b_sincola",\n'
            f'        "requiere_registro_dir": EXPERIMENT_DIR / "sincola_t0",\n'
            f'        "requiere_registro_modulo": "registro_vista_r2b_sincola",\n'
            f'        "vista_runtime": "comun_ev2.cargar_runtime(\'tanda0_ens_{g}_r2b_sincola\') tras importar sincola_t0/registro_vista_r2b_sincola (registro en memoria, patrón comun_tanda0); grafo evaluado de la tanda 0 sin la cola humana; r2b no se evalúa con EV2",\n'
            f'        "indice_fulltext": "nodos_fulltext_kg_tanda0_{g}_r2b_sincola",\n'
            f'    }},\n')


nuevo = ('        "indice_fulltext": "nodos_fulltext_kg_tanda0_diez_r2b",\n'
         '    },\n'
         '    # Tanda 0, grafo evaluado sin la cola humana (U-SINCOLA-T0, SC2, punto 2; ensamblados en SC1-bis, 01046b6): los\n'
         '    # r2b re-ensamblados sin las 74 unidades de la cola humana (59 en desarrollo) con ensamblar_tanda0.py --sin-cola\n'
         '    # (enmienda 1, 1f7c159). Su vista runtime la registra en memoria data/experiment/sincola_t0/\n'
         '    # registro_vista_r2b_sincola.py (patrón de reext_t0/t3bis/registro_vista_r2b.py), que declara además el desglose de\n'
         '    # las citas irresolubles por «punto sin nodos». commit_sellado: "PENDIENTE" hasta que la autora selle los grafos en\n'
         '    # su commit siguiente (como en c9540c0).\n'
         + entrada("desarrollo", "Desarrollo") + entrada("diez", "Diez") +
         '}\n'
         'CLAVES = list(GRAFOS.keys())\n')
GRAFOS.write_text(s.replace(ancla, nuevo), encoding="utf-8")
print("grafos.py: +2 entradas")

# ----------------------------------------------------------------------------------------- 3. el registro de la vista
REGISTRO = '''"""U-SINCOLA-T0, SC2, punto 2 (mandato 723680e; ensamblados de SC1-bis en 01046b6): registro EN MEMORIA de la vista
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
'''
REG.parent.mkdir(parents=True, exist_ok=True)
assert not REG.exists(), f"{REG} ya existe"
REG.write_text(REGISTRO, encoding="utf-8")
print("registro de la vista escrito:", REG.relative_to(RAIZ))
