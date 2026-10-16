"""
t1_manifiesto.py — B6.1, tanda 1, T1, punto 2.3 (pre-registro firmado en 95b18217, §2, «Manifiesto de la tanda 1»):
arma `manifiestos/tanda1_20tos_r2b.json` con el formato de `tanda0_10tos_r2b.json`. USD 0, sin API.

- `tos`: las entradas de los 20 de la lista final (`segmentacion_oficial_e0r2/s2/lista_tanda1_S2.json`) tomadas del
  manifiesto de los 152 de S1-ter (`s1ter/manifiesto/segmentacion_oficial_e0r2_152.json`), en el orden de corrida, con
  un solo campo cambiado: `rol_alcance`, que pasa a ser el del perfil `r2b` vigente después de A2 (su `rol_por_to`, que
  junta la tabla de la release y el derivado `catalogo_unico/registro_alcance_r2b.json`; perfil_e1.py:236): el
  `rol_id` o, sin él, la lista exacta de `clase_ids`, y null si el perfil no tiene entrada (la regla de
  manifiesto_corpus._validar_roles_contra_catalogo).
- `nombres_remision`: el método de `reext_t0/t1_manifiestos.py`, que no los deriva: los deja como vienen en la entrada
  de origen. La de S1-ter los trae vacíos («nombres_remision no se fija acá (lo fija el ensamblado)»). El runner no
  los lee; los lee el ensamblado (r1_referencias.titulos_de_inventario).
- `orden_corrida`: de menor a mayor por unidades (desempate por id), para que el freno por modelo y el de
  proyección actúen con poco gasto.
- `limites`: tope 1,45 × 3.290 × 0,021115 = 100,7291 (§3); margen por unidad 0,35 (el de la tanda 0); estimado por TO
  con e1 = unidades × 0,010135 más las líneas de alcance del TO (`alcance_e1/a2/salidas/medicion_tanda1_a2.json`,
  `usd_agregados`) y e3 = unidades × 0,010980, con sus 6 decimales, sin redondear: redondeados a 4 por TO, los 40
  valores suman 69,6596 y no 69,6592. Sin redondear suman 69,659193, que a 4 decimales da 69,6592; la diferencia de
  0,000002 con 69,659191 (§3) es de A2, cuyas líneas por documento suman 0,190843 contra 0,190841 de su total (cada
  documento redondea sus tokens). Checkpoint cada 150 en lingeef y depaho; sin chequeos de hits.
- `sellos`: la forma de los de la tanda 0 con los valores del §2. Son literales de este script; el control de
  entradas (t1_control_entradas.py) los compara con lo que el código carga.

Corre desde la raíz de una COPIA del repo y escribe en la copia (el archivo se lleva al repo después, con su
sha256). Uso: PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/tanda1/t1/t1_manifiesto.py
      [--verificar]   (solo compara el archivo existente con el que armaría, no escribe)
"""
from __future__ import annotations

import argparse
import json
import sys
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path(__file__).resolve().parents[4]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
SEG = REPO / "data" / "experiment" / "segmentacion_oficial_e0r2"
SALIDA = REX / "manifiestos" / "tanda1_20tos_r2b.json"
LISTA = SEG / "s2" / "lista_tanda1_S2.json"
S1TER = SEG / "s1ter" / "manifiesto" / "segmentacion_oficial_e0r2_152.json"
MEDICION_A2 = REPO / "data" / "experiment" / "alcance_e1" / "a2" / "salidas" / "medicion_tanda1_a2.json"
E0_REL = "data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b"

U_ESPERADA = 3290
TARIFA_E1, TARIFA_E3 = Decimal("0.010135"), Decimal("0.010980")
TOPE_USD = 100.7291                       # 1,45 × 3.290 × 0,021115 = 100,7291075 (§3)
ESTIMADO_ESPERADO = Decimal("69.6592")    # 3.290 × 0,021115 + 0,190841 = 69,659191, a 4 decimales (§3)
MARGEN_UNIDAD_USD = 0.35
CHECKPOINT_CADA = {"lingeef": 150, "depaho": 150}
ORDEN_ESPERADO = ["ri_gerc", "ri_pgn", "ceninf", "ri_rml", "nmcief", "adrei", "opefci", "ri_dcpc", "snp_tr", "efemin",
                  "ri_mmsef", "manori", "expaef", "ri_ccna", "ayccef", "cirmo3", "snp_cheq", "cajasc", "depaho",
                  "lingeef"]

SELLOS = {
    "unidad": "B6.1, tanda 1 (T1, punto 2.3; pre-registro firmado en 95b18217)",
    "commit_codigo": "47c9f1b3",
    "e0": {"ruta": E0_REL, "commit": "PENDIENTE (lo fija el commit de la autora)", "archivos": None},
    "prefijo_e1": {
        "hash": "322c5a23e9b7",
        "sha256": "ccffa4e36ba26a4b63b5760a7657d4bb5f5357ccd2392fe2b67584e4c2efb775",
        "caracteres": 59909,
        "commit": "66cde30",
        "parche_p3c_sha256": "5e3761c16d13a83d2071cb05494aea04a2c862259d39c7333e40db490f11c678",
        "base_p3b2_sha256": "8d84364fc3b6f6b586ff09e11833a2328408ae6f93b081c8ae64a059ea839c8b",
    },
    "tool_schema_sha256": "0c391f2b23bb7c94ec2606bd0315f3e4589c16a3571eaaa210a27babaa0f8ba2",
    "namespace_e1": "e1_extraccion|cv=e1-extractor-v1-p322c5a23e9b7|think=0",
    "namespace_reintento_forma": "e1_extraccion|cv=e1-extractor-v1-p322c5a23e9b7-rforma1|think=0",
    "temperatura_e1": 0,
    "temperatura_reintento_forma": 1,
    "prefijo_e3_hash": "21a836c7de6d",
    "namespace_e3": "e3_verificacion|cv=e3-verificador-v1-p21a836c7de6d|think=0",
    "candados": {
        "tablas_forzadas_sha256": "98cc96b2fec4cd7febb1fba71df8490ea420c0c0419711a122daaf4f12c2bc67",
        "candado_mensaje_r2b_json_sha256": "6b758517cee0f2e36c26c54f0f6738b3d49d11d0cf3141c26cff166ce6820325",
        "mensaje_r2b_sha256": "eeb11b9a3bf699d5535fcf2bbe79541ba746ae7bdae3341af962840990a97362",
        "registro_alcance_r2b_json_sha256": "e06933e77a1ae819229d5f2a4b5886f71f6129c809032e1e557932fb8cb69ff4",
        "candado_mensaje_e3_json_sha256": "079d2489f37c4485920e932f8cb2bfd60992ecc68bbb80ba504d04e5a5f8065b",
        "mensaje_e3_sha256": "66bc865645e99be13cc284f7733f22080612a1342bb2210add71cb122dd15a13",
    },
}
DESCRIPCION = (
    "B6.1, tanda 1, T1, punto 2.3 (16/10/2026; pre-registro firmado en 95b18217, §2, «Manifiesto de la tanda 1»): los 20 "
    "TOs de la lista final (segmentacion_oficial_e0r2/s2/lista_tanda1_S2.json, 22f33a17…; U = 3.290), con sus entradas "
    "del manifiesto de los 152 de S1-ter (f59cdea0…) y rol_alcance del perfil r2b vigente después de A2 (rol_por_to, que "
    "junta la tabla de la release y el derivado catalogo_unico/registro_alcance_r2b.json, e06933e7…). nombres_remision: "
    "el método de reext_t0/t1_manifiestos.py, que no los deriva y los deja como vienen en la entrada de origen (vacíos en "
    "S1-ter, que dice que los fija el ensamblado; el runner no los lee). rutas.e0_salida es la E0 de los 20 generada en "
    "T1 con el código del gate (S0-6b, 80adbd58…). orden_corrida: de menor a mayor por unidades. tope_global_usd = "
    "1,45 × 3.290 × 0,021115 = 100,7291 (§3); estimado_usd por TO: e1 = unidades × 0,010135 más las líneas de alcance del "
    "TO (alcance_e1/a2/salidas/medicion_tanda1_a2.json), e3 = unidades × 0,010980, sin redondear; suma 69,659193, que a "
    "4 decimales da 69,6592. Sellos: los del §2 "
    "(código 47c9f1b3; candados del mensaje de E1 de A2 y del de E3 desde O2). Lo arma data/experiment/tanda1/t1/"
    "t1_manifiesto.py.")


def r6(x: Decimal) -> float:
    return float(x.quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP))


def armar() -> dict:
    lista = json.loads(LISTA.read_text(encoding="utf-8"))
    filas = {f["to"]: f for f in lista["filas"]}
    assert len(filas) == 20 and sum(f["unidades_extraccion"] for f in filas.values()) == U_ESPERADA
    orden = sorted(filas, key=lambda t: (filas[t]["unidades_extraccion"], t))
    assert orden == ORDEN_ESPERADO, orden
    s1t = {t["id"]: t for t in json.loads(S1TER.read_text(encoding="utf-8"))["tos"]}

    for sub in ("e1_extractor",):
        sys.path.insert(0, str(REX / sub))
    import perfil_e1                                      # noqa: PLC0415 — los candados del perfil corren acá
    rol_por_to = perfil_e1.perfil("r2b").rol_por_to

    tos = []
    for to in orden:
        e = json.loads(json.dumps(s1t[to]))
        ent = rol_por_to.get(e["archivo"])
        e["rol_alcance"] = None if ent is None else (ent.get("rol_id") or list(ent["clase_ids"]))
        tos.append(e)

    alc = json.loads(MEDICION_A2.read_text(encoding="utf-8"))["medicion_tanda1"]["por_documento"]
    estimado = {}
    for to in orden:
        n = filas[to]["unidades_extraccion"]
        e1 = n * TARIFA_E1 + Decimal(str(alc[to]["usd_agregados"])) if to in alc else n * TARIFA_E1
        estimado[to] = {"e1": r6(e1), "e3": r6(n * TARIFA_E3)}
    total = sum(Decimal(str(v["e1"])) + Decimal(str(v["e3"])) for v in estimado.values())
    assert total.quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP) == ESTIMADO_ESPERADO, total

    e0 = REPO / E0_REL
    sellos = json.loads(json.dumps(SELLOS))
    sellos["e0"]["archivos"] = sum(1 for p in e0.iterdir() if p.is_file())

    return {
        "version": "1",
        "nombre": SALIDA.stem,
        "descripcion": DESCRIPCION,
        "tos": tos,
        "orden_corrida": orden,
        "perfil_e1": "r2b",
        "rutas": {"e0_salida": E0_REL},
        "oraculo": {"mapa_territorio": None, "limitaciones_e0": []},
        "limites": {"tope_global_usd": TOPE_USD, "margen_unidad_usd": MARGEN_UNIDAD_USD, "estimado_usd": estimado,
                    "checkpoint_cada": CHECKPOINT_CADA, "chequeos_hits": []},
        "tests_respuesta_conocida": None,
        "sellos": sellos,
        "indice_fragmentos": None,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verificar", action="store_true")
    a = ap.parse_args()
    texto = json.dumps(armar(), ensure_ascii=False, indent=1) + "\n"
    igual = SALIDA.exists() and SALIDA.read_text(encoding="utf-8") == texto
    print(f"{SALIDA.name}: {'igual' if igual else 'distinto o ausente'}")
    if a.verificar:
        return 0 if igual else 1
    SALIDA.write_text(texto, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
