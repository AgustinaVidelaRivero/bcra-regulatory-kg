"""Re-sellado único de la tanda 0 (mandato firmado el 15/10/2026, 67fe5b14), §3.2 y §3.3, con el patrón de
sincola_t0/sc2/editar_fixture_grafos_sc2.py, sobre una raíz (la copia del repo; el repo recibe después los mismos bytes):
  1. scripts/regression_kg_esperado.json: SOLO cuatro entradas nuevas al final de `estado_esperado`, con el sufijo -rs1
     sobre los nombres de hoy (decisión 1), copias de su entrada sellada (expectativas sin cambiar ninguna) con el kg, el
     kg_sha256 y el registro_dir del ensamblado nuevo y un rótulo propio. Antes de escribir verifica que la
     re-serialización del archivo es byte a byte igual (indent=1, ensure_ascii=False) y, después, que las entradas
     selladas quedan iguales (texto canónico de cada una).
  2. data/experiment/neo4j/grafos.py: SOLO cuatro entradas nuevas, con el sufijo _rs1 en la clave, el label, el índice
     fulltext y la ev2_key, y -rs1 en el nombre canónico (decisión 1), commit_sellado "PENDIENTE", insertadas al final
     del diccionario por reemplazo exacto de una ancla que aparece una sola vez.
  3. data/experiment/resellado_t0/registro_vista_r2b_rs1.py: el registro de la vista (patrón de
     sincola_t0/registro_vista_r2b_sincola.py), con el desglose de «punto sin nodos» de los dos sin la cola, recomputado
     acá con el mismo código y escrito como valores declarados.
Uso: python -I -B editar_fixture_grafos_rs1.py <raiz>
"""
import copy
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

RAIZ = Path(sys.argv[1]).resolve()
FIX = RAIZ / "scripts/regression_kg_esperado.json"
GRAFOS = RAIZ / "data/experiment/neo4j/grafos.py"
REG = RAIZ / "data/experiment/resellado_t0/registro_vista_r2b_rs1.py"
T0 = "data/experiment/reextraccion_v2/corpus_tanda0"
# (carpeta, nombre en la suite, clave de grafos.py, entrada sellada de la suite, sin cola)
GRAFOS_RS1 = [
    ("ens_desarrollo_r2b_rs1", "KG-Tanda0-Desarrollo-r2b-rs1", "KG_Tanda0_Desarrollo_r2b_rs1", "KG-Tanda0-Desarrollo-r2b", False),
    ("ens_diez_r2b_rs1", "KG-Tanda0-Diez-r2b-rs1", "KG_Tanda0_Diez_r2b_rs1", "KG-Tanda0-Diez-r2b", False),
    ("ens_desarrollo_r2b_sincola_rs1", "KG-Tanda0-Desarrollo-r2b-sincola-rs1", "KG_Tanda0_Desarrollo_r2b_sincola_rs1",
     "KG-Tanda0-Desarrollo-r2b-sincola", True),
    ("ens_diez_r2b_sincola_rs1", "KG-Tanda0-Diez-r2b-sincola-rs1", "KG_Tanda0_Diez_r2b_sincola_rs1",
     "KG-Tanda0-Diez-r2b-sincola", True),
]
ORIGEN = ("re-sellado único de la tanda 0 (mandato firmado el 15/10/2026, 67fe5b14; decisión 1 de su §8): ensamblado con "
          "el código de U-OMISIONES-COD (ded41d50) sobre las salidas de E1 y E3 de la tanda 0 tal como las deja R0 "
          "(1d690df3 y 2d0f5277)")


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


info = {}
for carpeta, suite, clave, base, sin_cola in GRAFOS_RS1:
    kg = RAIZ / T0 / carpeta / "r2" / "kg.json"
    d = json.loads(kg.read_text(encoding="utf-8"))
    info[clave] = {"sha": sha(kg), "n": (len(d["nodes"]), len(d["edges"])), "carpeta": carpeta}

# ------------------------------------------------------------------------------------------------- 1. la fixture
raw = FIX.read_text(encoding="utf-8")
fx = json.loads(raw)
assert json.dumps(fx, ensure_ascii=False, indent=1) + "\n" == raw, "la fixture no se re-serializa byte a byte"
ee = fx["estado_esperado"]
canon_antes = {k: json.dumps(v, ensure_ascii=False, sort_keys=True) for k, v in ee.items()}
for carpeta, suite, clave, base, sin_cola in GRAFOS_RS1:
    assert suite not in ee, f"{suite} ya existe"
    e = copy.deepcopy(ee[base])
    e_nuevo = {
        "_rotulo": (f"RE-SELLADO ÚNICO DE LA TANDA 0: la versión posterior de {base}, {ORIGEN}"
                    + (", sin la cola humana (ensamblar_tanda0.py --sin-cola)" if sin_cola else "")
                    + f". Las expectativas son las de la entrada {base} sellada, sin cambiar ninguna. Rótulo heredado: "
                    + e["_rotulo"]),
        "kg": f"{T0}/{carpeta}/r2/kg.json",
        "kg_sha256": info[clave]["sha"],
        "_kg_sha256": ("sha256 del ensamblado re-sellado: dos corridas en procesos distintos, byte a byte, sobre una copia "
                       "del repo; el archivo del repo es byte a byte el de la copia."),
        "registro_dir": f"{T0}/{carpeta}/r2",
        "_registro_dir": "el registro del ensamblado nuevo (no_mapeados_sujetos.jsonl, omisiones.jsonl, reporte_ensamblado_r2.json): se pasa a la suite con --registro-dir.",
    }
    for k, v in e.items():
        if k not in e_nuevo:
            e_nuevo[k] = v
    e_nuevo["evidencia"] = f"Expectativas heredadas de {base}. " + e["evidencia"]
    ee[suite] = e_nuevo
canon_despues = {k: json.dumps(v, ensure_ascii=False, sort_keys=True) for k, v in ee.items() if k in canon_antes}
assert canon_antes == canon_despues, "una entrada sellada cambió"
FIX.write_text(json.dumps(fx, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("fixture: +4 entradas", [s for _, s, _, _, _ in GRAFOS_RS1])

# ------------------------------------------------------------------------------------------------- 2. grafos.py
s = GRAFOS.read_text(encoding="utf-8")
ancla = ('        "indice_fulltext": "nodos_fulltext_kg_tanda0_diez_r2b_sincola",\n'
         '    },\n'
         '}\n'
         'CLAVES = list(GRAFOS.keys())\n')
assert s.count(ancla) == 1, "ancla de grafos.py no encontrada una sola vez"


def entrada(carpeta: str, suite: str, clave: str, sin_cola: bool) -> str:
    n, a = info[clave]["n"]
    ev2 = "tanda0_" + carpeta
    extra = "grafo evaluado de la tanda 0 sin la cola humana; " if sin_cola else ""
    return (f'    "{clave}": {{\n'
            f'        "nombre_canonico": "{suite}",\n'
            f'        "label": "{clave}",\n'
            f'        "path": EXPERIMENT_DIR / "reextraccion_v2" / "corpus_tanda0" / "{carpeta}" / "r2" / "kg.json",\n'
            f'        "sha256": "{info[clave]["sha"]}",\n'
            f'        "commit_sellado": "PENDIENTE",\n'
            f'        "n_nodos": {n},\n'
            f'        "n_aristas": {a},\n'
            f'        "ev2_key": "{ev2}",\n'
            f'        "requiere_registro_dir": EXPERIMENT_DIR / "resellado_t0",\n'
            f'        "requiere_registro_modulo": "registro_vista_r2b_rs1",\n'
            f'        "vista_runtime": "comun_ev2.cargar_runtime(\'{ev2}\') tras importar resellado_t0/registro_vista_r2b_rs1 (registro en memoria, patrón comun_tanda0); re-sellado único de la tanda 0; {extra}r2b no se evalúa con EV2",\n'
            f'        "indice_fulltext": "nodos_fulltext_{clave.lower()}",\n'
            f'    }},\n')


nuevo = (ancla.replace('}\nCLAVES = list(GRAFOS.keys())\n', '')
         + '    # Tanda 0, re-sellado único de los cuatro r2b (mandato firmado el 15/10/2026, 67fe5b14; decisión 1 de su §8: los\n'
           '    # nombres de U-SINCOLA-T0 con el sufijo _rs1): las versiones posteriores de los cuatro grafos de arriba, que\n'
           '    # siguen sellados, ensambladas con el código de U-OMISIONES-COD (ded41d50) sobre las salidas de E1 y E3 de la\n'
           '    # tanda 0 tal como las deja R0 (1d690df3 y 2d0f5277). Su vista runtime la registra en memoria\n'
           '    # data/experiment/resellado_t0/registro_vista_r2b_rs1.py (patrón de sincola_t0/registro_vista_r2b_sincola.py).\n'
           '    # commit_sellado: "PENDIENTE" hasta el segundo commit del sello de la autora (como en c9540c0 y 235a295).\n'
         + "".join(entrada(c, su, k, sc) for c, su, k, _, sc in GRAFOS_RS1)
         + '}\nCLAVES = list(GRAFOS.keys())\n')
GRAFOS.write_text(s.replace(ancla, nuevo), encoding="utf-8")
print("grafos.py: +4 entradas", [k for _, _, k, _, _ in GRAFOS_RS1])

# ------------------------------------------------------------------------------------------------- 3. el registro
# desglose de «punto sin nodos» (mismo código que sincola_t0/registro_vista_r2b_sincola.py, recomputado acá)
ENS = RAIZ / T0


def unidades_de_la_cola() -> list:
    u = {}
    for f in sorted((ENS / "salida_r2b").glob("*/finales.jsonl")):
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
                        "punto_sin_nodos": rep["irresolubles_por_causa"].get("punto_sin_nodos", 0)}}


cola = unidades_de_la_cola()
DECL = {}
for g in ("diez", "desarrollo"):
    d_sc, d_co = _desglose_dir(ENS / f"ens_{g}_r2b_sincola_rs1", cola), _desglose_dir(ENS / f"ens_{g}_r2b_rs1", cola)
    DECL[f"tanda0_ens_{g}_r2b_sincola_rs1"] = {**d_sc, "grafo_completo": d_co}
print("cola:", len(cola), "| desglose:", json.dumps(DECL, ensure_ascii=False))


def fmt_decl() -> str:
    lineas = ["PUNTO_SIN_NODOS = {"]
    for k, v in DECL.items():
        r, p, gc = v["registro"], v["reporte"], v["grafo_completo"]
        lineas += [f'    "{k}": {{',
                   f'        "registro": {{"entradas": {r["entradas"]}, "irresolubles": {r["irresolubles"]}, '
                   f'"punto_sin_nodos_total": {r["punto_sin_nodos_total"]},',
                   f'                     "con_destino_en_unidad_excluida": {r["con_destino_en_unidad_excluida"]}, '
                   f'"netas": {r["netas"]}}},',
                   f'        "reporte": {{"citas_irresolubles": {p["citas_irresolubles"]}, "punto_sin_nodos": {p["punto_sin_nodos"]}}},',
                   f'        "grafo_completo": {{"registro": {{"entradas": {gc["registro"]["entradas"]}, '
                   f'"irresolubles": {gc["registro"]["irresolubles"]}, "punto_sin_nodos_total": '
                   f'{gc["registro"]["punto_sin_nodos_total"]},',
                   f'                                        "con_destino_en_unidad_excluida": '
                   f'{gc["registro"]["con_destino_en_unidad_excluida"]}, "netas": {gc["registro"]["netas"]}}},',
                   f'                           "reporte": {{"citas_irresolubles": {gc["reporte"]["citas_irresolubles"]}, '
                   f'"punto_sin_nodos": {gc["reporte"]["punto_sin_nodos"]}}}}},',
                   '    },']
    return "\n".join(lineas + ["}"])


def fmt_r2b() -> str:
    out = ["R2B_RS1 = {"]
    for carpeta, _, clave, _, _ in GRAFOS_RS1:
        lab = carpeta.replace("ens_", "").replace("_r2b", "").replace("_sincola", "_sincola")
        out += [f'    "tanda0_{carpeta}": {{',
                f'        "path": T0.ENS_DIR / "{carpeta}" / "r2" / "kg.json",',
                f'        "sha256": "{info[clave]["sha"]}",',
                f'        "label": "r2b_{lab}_mem",',
                '    },']
    return "\n".join(out + ["}"])


REGISTRO = '''"""Re-sellado único de los grafos r2b de la tanda 0 (mandato firmado el 15/10/2026, 67fe5b14), §3.3: registro EN MEMORIA
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

@@R2B@@

# El grafo completo re-sellado de cada grafo sin la cola, para la cifra «al lado».
GRAFO_COMPLETO = {
    "tanda0_ens_diez_r2b_sincola_rs1": T0.ENS_DIR / "ens_diez_r2b_rs1",
    "tanda0_ens_desarrollo_r2b_sincola_rs1": T0.ENS_DIR / "ens_desarrollo_r2b_rs1",
}

# Desglose declarado, recomputado con el código de abajo sobre los ensamblados re-sellados.
@@DECL@@


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
'''
REG.parent.mkdir(parents=True, exist_ok=True)
assert not REG.exists(), f"{REG} ya existe"
REG.write_text(REGISTRO.replace("@@R2B@@", fmt_r2b()).replace("@@DECL@@", fmt_decl()), encoding="utf-8")
print("registro de la vista escrito:", REG.relative_to(RAIZ))
