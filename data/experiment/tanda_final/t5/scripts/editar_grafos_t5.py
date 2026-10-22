"""B6.1, tanda final, T5, punto 8 (el sello del tramo 1 como respaldo; enmienda 9 al protocolo entre tandas, §1, punto 1; pre-registro
firmado en 4de7f2a7, §7): las entradas de los dos grafos del tramo 1 en data/experiment/neo4j/grafos.py y el registro de su vista, con
t3/scripts/editar_grafos_tf.py copiado y adaptado, sobre una raíz (la copia del repo; el repo recibe después los mismos bytes):
  1. grafos.py: SOLO dos entradas nuevas al final de GRAFOS, KG_TandaFinal_Tramo1_r2b y KG_TandaFinal_Tramo1_r2b_sincola, con la forma de
     KG_TandaFinal_r2b, con label, índice y ev2_key propios y commit_sellado «PENDIENTE»; el sha256, n_nodos y n_aristas salen de
     tanda_final/t3/salidas/doble_corrida_tf.json (los de la tabla E1 de T3). Las selladas no se tocan: el texto anterior al ancla y el
     posterior quedan iguales (se controla).
  2. data/experiment/tanda_final/t5/registro_vista_r2b_tramo1.py: el registro EN MEMORIA de la vista runtime de los dos grafos, con el
     patrón de t3/registro_vista_r2b_tanda_final.py (sin editarlo), con el desglose de «punto sin nodos» del sin cola recomputado acá con
     el mismo código. La cola es la de la tanda final: las unidades con estado cola_humana* como última versión en
     corpus_tanda_final/salida_r2b/*/finales.jsonl (solo se guardan esas; los demás estados no se cuentan ni se reportan).
Uso: python3 -I -B editar_grafos_t5.py <raiz>
"""
import json
import sys
from pathlib import Path

RAIZ = Path(sys.argv[1]).resolve()
GRAFOS = RAIZ / "data/experiment/neo4j/grafos.py"
REG = RAIZ / "data/experiment/tanda_final/t5/registro_vista_r2b_tramo1.py"
TF = RAIZ / "data/experiment/reextraccion_v2/corpus_tanda_final"
dc = json.loads((RAIZ / "data/experiment/tanda_final/t3/salidas/doble_corrida_tf.json").read_text(encoding="utf-8"))["doble_corrida"]
# (carpeta, nombre canónico, clave de grafos.py, clave de la doble corrida, sin cola)
NUEVAS = [("ens_tramo1_r2b", "KG-TandaFinal-Tramo1-r2b", "KG_TandaFinal_Tramo1_r2b", "tf_tramo1", False),
          ("ens_tramo1_r2b_sincola", "KG-TandaFinal-Tramo1-r2b-sincola", "KG_TandaFinal_Tramo1_r2b_sincola", "tf_tramo1_sincola", True)]
info = {}
for carpeta, _, clave, k, _ in NUEVAS:
    v = dc[k]
    assert v["kg_sha256"][0] == v["kg_sha256"][1] and v["carpeta"].endswith(carpeta)
    info[clave] = {"sha": v["kg_sha256"][0], "n": (v["nodos"], v["aristas"])}

# ------------------------------------------------------------------------------------------------- 1. grafos.py
s = GRAFOS.read_text(encoding="utf-8")
ancla = ('        "indice_fulltext": "nodos_fulltext_kg_tandafinal_r2b_sincola",\n'
         '    },\n'
         '}\n'
         'CLAVES = list(GRAFOS.keys())\n')
assert s.count(ancla) == 1, "ancla de grafos.py no encontrada una sola vez"


def entrada(carpeta: str, canonico: str, clave: str, sin_cola: bool) -> str:
    n, a = info[clave]["n"]
    ev2 = "tandafinal_" + carpeta
    extra = "grafo del tramo 1 sin la cola humana; " if sin_cola else ""
    return (f'    "{clave}": {{\n'
            f'        "nombre_canonico": "{canonico}",\n'
            f'        "label": "{clave}",\n'
            f'        "path": EXPERIMENT_DIR / "reextraccion_v2" / "corpus_tanda_final" / "{carpeta}" / "r2" / "kg.json",\n'
            f'        "sha256": "{info[clave]["sha"]}",\n'
            f'        "commit_sellado": "PENDIENTE",\n'
            f'        "n_nodos": {n},\n'
            f'        "n_aristas": {a},\n'
            f'        "ev2_key": "{ev2}",\n'
            f'        "requiere_registro_dir": EXPERIMENT_DIR / "tanda_final" / "t5",\n'
            f'        "requiere_registro_modulo": "registro_vista_r2b_tramo1",\n'
            f'        "vista_runtime": "comun_ev2.cargar_runtime(\'{ev2}\') tras importar tanda_final/t5/registro_vista_r2b_tramo1 (registro en memoria, patrón comun_tanda0); tramo 1 de la tanda final de B6.1, sellado como respaldo (enmienda 9); {extra}r2b no se evalúa con EV2",\n'
            f'        "indice_fulltext": "nodos_fulltext_{clave.lower()}",\n'
            f'    }},\n')


nuevo = (ancla.replace('}\nCLAVES = list(GRAFOS.keys())\n', '')
         + '    # El tramo 1 de la tanda final de B6.1, sellado como respaldo (enmienda 9 al protocolo entre tandas, §1, punto 1; T5): sus\n'
           '    # dos grafos, completo y sin la cola humana, ensamblados en T3 con ensamblar_tanda0.py (cadena r2, --e0-r2) y los manifiestos\n'
           '    # de la raya. Su vista runtime la registra en memoria data/experiment/tanda_final/t5/registro_vista_r2b_tramo1.py (patrón de\n'
           '    # tanda_final/t3/registro_vista_r2b_tanda_final.py). commit_sellado: "PENDIENTE" hasta el commit siguiente al sello.\n'
         + "".join(entrada(c, cn, k, sc) for c, cn, k, _, sc in NUEVAS)
         + '}\nCLAVES = list(GRAFOS.keys())\n')
s2 = s.replace(ancla, nuevo)
i = s.index(ancla)
assert s2[:i] == s[:i] and s2.endswith(s[i + len(ancla):]), "el texto sellado de grafos.py cambió"
GRAFOS.write_text(s2, encoding="utf-8")
print("grafos.py: +2 entradas", [k for _, _, k, _, _ in NUEVAS])

# ------------------------------------------------------------------------------------------------- 2. el registro
# desglose de «punto sin nodos» (mismo código que resellado_t0/registro_vista_r2b_rs1.py, recomputado acá)


def unidades_de_la_cola() -> list:
    u = {}
    for f in sorted((TF / "salida_r2b").glob("*/finales.jsonl")):
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
d_sc, d_co = _desglose_dir(TF / "ens_tramo1_r2b_sincola", cola), _desglose_dir(TF / "ens_tramo1_r2b", cola)
DECL = {"tandafinal_ens_tramo1_r2b_sincola": {**d_sc, "grafo_completo": d_co}}
print("cola humana:", len(cola), "| desglose:", json.dumps(DECL, ensure_ascii=False))


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
    out = ["R2B_TRAMO1 = {"]
    for carpeta, _, clave, _, _ in NUEVAS:
        out += [f'    "tandafinal_{carpeta}": {{',
                f'        "path": ENS_TF / "{carpeta}" / "r2" / "kg.json",',
                f'        "sha256": "{info[clave]["sha"]}",',
                f'        "label": "r2b_tandafinal_{carpeta.removeprefix("ens_").removesuffix("_r2b").replace("_r2b_", "_")}_mem",',
                '    },']
    return "\n".join(out + ["}"])


REGISTRO = '''"""B6.1, tanda final, T5, punto 8 (el sello del tramo 1 como respaldo; enmienda 9, §1, punto 1): registro EN MEMORIA de la vista
runtime de los dos grafos del tramo 1 de la tanda final (completo y sin la cola), con el patrón de
data/experiment/tanda_final/t3/registro_vista_r2b_tanda_final.py y de data/experiment/tanda0/code/comun_tanda0.py, sin editarlos: agrega
las dos claves a la tabla TANDA0 en memoria y vuelve a llamar a su registro (idempotente). Lo importa data/experiment/neo4j/grafos.py
(cargar_vista_runtime) por los campos requiere_registro_dir y requiere_registro_modulo de las entradas KG_TandaFinal_Tramo1_r2b*. La vista es la de comun_tanda0.cargar_runtime_gen3; el kg.json no se
toca. r2b no se evalúa con EV2 (laudo de r2, §3, punto 6): esta vista sirve a la carga en Neo4j y a su verificación.

Declara además, para el grafo sin la cola, las citas irresolubles por «punto sin nodos» desglosadas como en el re-sellado: total; de
ellas, con destino en una unidad excluida del grafo evaluado por la regla de la cola; netas; y la cifra del grafo completo al lado. La
cola es la de la tanda final: las unidades con estado cola_humana* como última versión en corpus_tanda_final/salida_r2b/*/finales.jsonl,
o una
de sus partes (`<destino>::parteN`). La unidad de conteo es el ítem de `irresolubles` del registro de remisiones
(`<ensamblado>/r2/remisiones_registro.json`); el reporte del ensamblado (`remite_a.irresolubles_por_causa`) cuenta sin repetir; se
declaran las dos. `desglose_punto_sin_nodos(clave)` recomputa las cifras desde esos archivos (solo lectura) y `verificar_desglose()`
las compara con las declaradas. Lo generó data/experiment/tanda_final/t5/scripts/editar_grafos_t5.py.
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

@@R2B@@

# El grafo completo del grafo sin la cola, para la cifra «al lado».
GRAFO_COMPLETO = {"tandafinal_ens_tramo1_r2b_sincola": ENS_TF / "ens_tramo1_r2b"}

# Desglose declarado, recomputado con el código de abajo sobre los ensamblados del tramo 1.
@@DECL@@


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
    d = R2B_TRAMO1[clave]["path"].parents[1]
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


def registrar_r2b_tramo1() -> None:
    T0.TANDA0.update(R2B_TRAMO1)
    T0.registrar_tanda0()


registrar_r2b_tramo1()

if __name__ == "__main__":
    print(json.dumps(verificar_desglose(), ensure_ascii=False, indent=1))
'''
assert not REG.exists(), f"{REG} ya existe"
REG.write_text(REGISTRO.replace("@@R2B@@", fmt_r2b()).replace("@@DECL@@", fmt_decl()), encoding="utf-8")
print("registro de la vista escrito:", REG.relative_to(RAIZ))
