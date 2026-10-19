"""
t1_manifiesto_tanda_final.py — B6.1, tanda final, T1, punto 2.3 (pre-registro firmado de la tanda final, §1.1, con su
versión derivada de T1): arma `manifiestos/tanda_final_98tos_r2b.json` con el formato y el método del de la tanda 1
(`tanda1_20tos_r2b.json`, que armó `data/experiment/tanda1/t1/t1_manifiesto.py`). USD 0, sin API.

- `tos`: los 98 de S2c (`segmentacion_oficial_e0r2/s2/cifras/tanda_final_S2c.json`, `tanda_final.lista`), con sus
  entradas del manifiesto de los 152 de S1-ter (`s1ter/manifiesto/segmentacion_oficial_e0r2_152.json`), en el orden de
  corrida, con un solo campo cambiado: `rol_alcance`, que pasa a ser el del perfil `r2b` de A3 (su `rol_por_to`, que
  junta la tabla de la release y el derivado `catalogo_unico/registro_alcance_r2b.json`, c8dea08a…; perfil_e1.py): el
  `rol_id` o, sin él, la lista exacta de `clase_ids`, y null si el perfil no tiene entrada (la regla de
  manifiesto_corpus._validar_roles_contra_catalogo).
- `nombres_remision`: el método de `reext_t0/t1_manifiestos.py`, que no los deriva: los deja como vienen en la entrada
  de origen. La de S1-ter los trae vacíos («nombres_remision no se fija acá (lo fija el ensamblado)»). El runner no los
  lee; los lee el ensamblado (r1_referencias.titulos_de_inventario).
- `orden_corrida`: primero los 30 del tramo 1 y después los 68 del tramo 2
  (`tanda_final/preregistro/tramos_tanda_final.json`), cada tramo de menor a mayor por unidades (desempate por id).
- `limites`:
  - `tope_global_usd` = 1,45 × 4.951 × 0,021115 = 151,58352925, a cuatro decimales 151,5835 (despacho, punto 1.3);
  - `margen_unidad_usd` = 0,35; `checkpoint_cada` = 150 en ctavis, depinv y pimf; `chequeos_hits` vacío;
  - `estimado_usd` por TO, con `--estimado`:
    - `plano` (por defecto; la fórmula del despacho, punto 2.3, que da por tramo lo del §3 del pre-registro más las
      líneas de alcance): e1 = unidades × 0,010135 más las líneas de alcance del TO
      (`alcance_e1/a3/salidas/medicion_mensajes_tres_tandas_a3.json`, `tanda_final.por_documento`, `usd_agregados`) y
      e3 = unidades × 0,010980, a seis decimales;
    - `reparto` (la alternativa que queda para la autora): el total del plano repartido entre los 98 en proporción a
      los caracteres de su E0 completa (`chars_completo`), con el e1 y el e3 de cada TO en la proporción que tenían,
      como el manifiesto de la tanda 1 desde el 17/10/2026 (nota al pie de docs/preregistro_tanda1.md; registro de
      decisiones, §21, que deja pendiente para la tanda final «que su estimado se reparta igual desde el principio»). El
      total del TO va a seis decimales, el e1 a seis decimales y el e3 es el total del TO menos el e1; el resto del
      redondeo va al e3 del TO con más caracteres. Es el método que reproduce, TO por TO, el manifiesto commiteado de la
      tanda 1 (818a62cf…).
- `sellos`: la forma de los de la tanda 1, con los valores del §2: el commit del código (c66c7ecd) y el derivado de A3
  (c8dea08a…). Son literales de este script; el control de entradas (t1_control_entradas_tanda_final.py) los compara con
  lo que el código carga.

Corre sobre la raíz de una COPIA del repo (--raiz) y escribe solo --salida (por defecto, el manifiesto dentro de la
copia; el archivo se lleva al repo después, con su sha256). Lee la E0 de los 98 de <raíz>/E0_REL.
Uso: PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B t1_manifiesto_tanda_final.py --raiz <copia>
       [--estimado plano|reparto] [--salida <json>] [--info <json>] [--verificar]   (--verificar: solo compara, no escribe)
"""
from __future__ import annotations

import argparse
import json
import sys
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

sys.dont_write_bytecode = True
NOMBRE = "tanda_final_98tos_r2b"
E0_REL = "data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b"
SALIDA_REL = f"data/experiment/reextraccion_v2/manifiestos/{NOMBRE}.json"
TRAMOS_REL = "data/experiment/tanda_final/preregistro/tramos_tanda_final.json"
S2C_REL = "data/experiment/segmentacion_oficial_e0r2/s2/cifras/tanda_final_S2c.json"
S1TER_REL = "data/experiment/segmentacion_oficial_e0r2/s1ter/manifiesto/segmentacion_oficial_e0r2_152.json"
MEDICION_A3_REL = "data/experiment/alcance_e1/a3/salidas/medicion_mensajes_tres_tandas_a3.json"

U_ESPERADA = 4951
N_TRAMO_1, N_TRAMO_2 = 30, 68
TARIFA_E1, TARIFA_E3 = Decimal("0.010135"), Decimal("0.010980")
TARIFA = TARIFA_E1 + TARIFA_E3                  # 0,021115 (laudo, §1)
TOPE_USD = 151.5835                             # 1,45 × 4.951 × 0,021115 = 151,58352925 (despacho, 1.3)
COSTO_LINEAS_A3 = Decimal("0.209440")           # versión derivada de T1, A3.costo_lineas_usd
MARGEN_UNIDAD_USD = 0.35
CHECKPOINT_CADA = {"ctavis": 150, "depinv": 150, "pimf": 150}   # registro de decisiones, §41

SELLOS = {
    "unidad": "B6.1, tanda final (T1, punto 2.3; pre-registro de la tanda final firmado, §1.1 y §2)",
    "commit_codigo": "c66c7ecd",
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
        "registro_alcance_r2b_json_sha256": "c8dea08a2ffe2eeb401855f952cc80f26542da8ea2489eac7a6f83530b6857ca",
        "candado_mensaje_e3_json_sha256": "079d2489f37c4485920e932f8cb2bfd60992ecc68bbb80ba504d04e5a5f8065b",
        "mensaje_e3_sha256": "66bc865645e99be13cc284f7733f22080612a1342bb2210add71cb122dd15a13",
    },
}


def descripcion(metodo: str) -> str:
    est = ("e1 = unidades × 0,010135 más las líneas de alcance del TO (alcance_e1/a3/salidas/"
           "medicion_mensajes_tres_tandas_a3.json, tanda_final.por_documento) y e3 = unidades × 0,010980, a seis decimales"
           if metodo == "plano" else
           "el total del estimado plano (e1 = unidades × 0,010135 más las líneas de alcance del TO de alcance_e1/a3/salidas/"
           "medicion_mensajes_tres_tandas_a3.json; e3 = unidades × 0,010980) repartido entre los 98 en proporción a los "
           "caracteres de su E0 completa (chars_completo), con el e1 y el e3 de cada TO en la proporción que tenían, como "
           "el de la tanda 1 desde el 17/10/2026 (nota al pie de docs/preregistro_tanda1.md; registro de decisiones, §21)")
    return (
        "B6.1, tanda final, T1, punto 2.3 (18/10/2026; pre-registro de la tanda final firmado, §1.1, con su versión derivada "
        "de T1): los 98 TOs de S2c (segmentacion_oficial_e0r2/s2/cifras/tanda_final_S2c.json; U = 4.951), con sus entradas "
        "del manifiesto de los 152 de S1-ter (f59cdea0…) y rol_alcance del perfil r2b de A3 (rol_por_to, que junta la tabla "
        "de la release y el derivado catalogo_unico/registro_alcance_r2b.json, c8dea08a…). nombres_remision: el método de "
        "reext_t0/t1_manifiestos.py, que no los deriva y los deja como vienen en la entrada de origen (vacíos en S1-ter, que "
        "dice que los fija el ensamblado; el runner no los lee). rutas.e0_salida es la E0 de los 98 generada en T1 con el "
        "código del gate (S0-6b, 80adbd58…). orden_corrida: los 30 del tramo 1 y después los 68 del tramo 2 "
        "(tanda_final/preregistro/tramos_tanda_final.json), cada tramo de menor a mayor por unidades. tope_global_usd = "
        "1,45 × 4.951 × 0,021115 = 151,5835 (§3); estimado_usd por TO: " + est + ". Sellos: los del §2 (código c66c7ecd; "
        "derivado, candado y mensaje de E1 de A3; candado del mensaje de E3 desde O2). Lo arma data/experiment/tanda_final/"
        "t1/t1_manifiesto_tanda_final.py.")


def q6(x: Decimal) -> Decimal:
    return x.quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)


def armar(raiz: Path, metodo: str) -> tuple[dict, dict]:
    tramos = json.loads((raiz / TRAMOS_REL).read_text(encoding="utf-8"))
    s2c = json.loads((raiz / S2C_REL).read_text(encoding="utf-8"))["tanda_final"]
    t1, t2 = tramos["tramo_1_tos"], tramos["tramo_2_tos"]
    assert len(t1) == N_TRAMO_1 and len(t2) == N_TRAMO_2 and not set(t1) & set(t2), (len(t1), len(t2))
    assert sorted(set(t1) | set(t2)) == sorted(s2c["lista"]) and len(s2c["lista"]) == 98
    unidades = {**t1, **t2}
    assert sum(unidades.values()) == U_ESPERADA == s2c["unidades"]
    orden = sorted(t1, key=lambda t: (t1[t], t)) + sorted(t2, key=lambda t: (t2[t], t))

    e0 = raiz / E0_REL
    chunks = {to: json.loads((e0 / f"chunks_{to}.json").read_text(encoding="utf-8")) for to in orden}
    assert all(len(chunks[to]) == unidades[to] for to in orden), [t for t in orden if len(chunks[t]) != unidades[t]]
    chars = {to: sum(c["chars_completo"] for c in chunks[to]) for to in orden}

    s1t = {t["id"]: t for t in json.loads((raiz / S1TER_REL).read_text(encoding="utf-8"))["tos"]}
    sys.path.insert(0, str(raiz / "data" / "experiment" / "reextraccion_v2" / "e1_extractor"))
    import perfil_e1                                      # noqa: PLC0415 — los candados del perfil corren acá
    rol_por_to = perfil_e1.perfil("r2b").rol_por_to
    tos = []
    for to in orden:
        e = json.loads(json.dumps(s1t[to]))
        ent = rol_por_to.get(e["archivo"])
        e["rol_alcance"] = None if ent is None else (ent.get("rol_id") or list(ent["clase_ids"]))
        tos.append(e)

    alc = json.loads((raiz / MEDICION_A3_REL).read_text(encoding="utf-8"))["tanda_final"]["por_documento"]
    assert set(alc) <= set(orden) and len(alc) == 33
    plano = {}
    for to in orden:
        n = unidades[to]
        e1 = n * TARIFA_E1 + (Decimal(str(alc[to]["usd_agregados"])) if to in alc else Decimal(0))
        plano[to] = (q6(e1), q6(n * TARIFA_E3))
    total = sum(a + b for a, b in plano.values())
    if metodo == "plano":
        est = {to: [plano[to][0], plano[to][1]] for to in orden}
        resto, al_resto = Decimal(0), None
    else:
        c_tot = sum(chars.values())
        est = {}
        for to in orden:
            t = total * chars[to] / c_tot
            e1, e3 = plano[to]
            a = q6(t * e1 / (e1 + e3))
            est[to] = [a, q6(t) - a]
        resto = total - sum(a + b for a, b in est.values())
        al_resto = max(orden, key=lambda t: (chars[t], t))
        est[al_resto][1] += resto
    estimado = {to: {"e1": float(est[to][0]), "e3": float(est[to][1])} for to in orden}
    suma = sum(Decimal(str(v["e1"])) + Decimal(str(v["e3"])) for v in estimado.values())
    assert suma == total, (suma, total)

    sellos = json.loads(json.dumps(SELLOS))
    sellos["e0"]["archivos"] = sum(1 for p in e0.iterdir() if p.is_file())
    m = {
        "version": "1",
        "nombre": NOMBRE,
        "descripcion": descripcion(metodo),
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
    tope_exacto = Decimal("1.45") * U_ESPERADA * TARIFA
    info = {"metodo": metodo, "tos": len(orden), "tramo_1": orden[:N_TRAMO_1], "tramo_2": orden[N_TRAMO_1:],
            "unidades": sum(unidades.values()), "chars_completo": sum(chars.values()),
            "estimado_total_usd": str(total), "a_4_decimales": str(total.quantize(Decimal("0.0001"), ROUND_HALF_UP)),
            "u_por_tarifa_mas_lineas_a3_usd": str(U_ESPERADA * TARIFA + COSTO_LINEAS_A3),
            "diferencia_contra_u_por_tarifa_mas_lineas_a3": str(total - (U_ESPERADA * TARIFA + COSTO_LINEAS_A3)),
            "lineas_a3_por_documento_sumadas_usd": str(sum(Decimal(str(v["usd_agregados"])) for v in alc.values())),
            "resto_del_reparto_usd": str(resto), "resto_al_e3_de": al_resto,
            "tope_exacto": str(tope_exacto), "tope_usd": TOPE_USD,
            "tope_a_4_decimales_igual": Decimal(str(TOPE_USD)) == tope_exacto.quantize(Decimal("0.0001"), ROUND_HALF_UP),
            "e0_archivos": sellos["e0"]["archivos"],
            "con_alcance": sum(t["rol_alcance"] is not None for t in tos),
            "sin_alcance": sorted(t["id"] for t in tos if t["rol_alcance"] is None),
            "tramo_1_estimado_usd": str(sum(est[t][0] + est[t][1] for t in orden[:N_TRAMO_1])),
            "tramo_2_estimado_usd": str(sum(est[t][0] + est[t][1] for t in orden[N_TRAMO_1:]))}
    return m, info


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--raiz", type=Path, required=True)
    ap.add_argument("--estimado", choices=("plano", "reparto"), default="plano")
    ap.add_argument("--salida", type=Path, default=None)
    ap.add_argument("--info", type=Path, default=None, help="JSON con las cifras del armado (fuera de la copia)")
    ap.add_argument("--verificar", action="store_true")
    a = ap.parse_args()
    raiz = a.raiz.resolve()
    salida = (a.salida or raiz / SALIDA_REL).resolve()
    m, info = armar(raiz, a.estimado)
    texto = json.dumps(m, ensure_ascii=False, indent=1) + "\n"
    igual = salida.exists() and salida.read_text(encoding="utf-8") == texto
    print(f"{salida.name} ({a.estimado}): {'igual' if igual else 'distinto o ausente'}")
    if a.info:
        a.info.write_text(json.dumps(info, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    if a.verificar:
        return 0 if igual else 1
    if salida.name != f"{NOMBRE}.json":
        m["nombre"] = salida.stem                       # manifiesto_corpus.cargar exige nombre == nombre del archivo
        texto = json.dumps(m, ensure_ascii=False, indent=1) + "\n"
    salida.write_text(texto, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
