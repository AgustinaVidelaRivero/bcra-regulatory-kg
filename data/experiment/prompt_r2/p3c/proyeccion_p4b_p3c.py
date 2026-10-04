"""
proyeccion_p4b_p3c.py — U-PROMPT-R2, P3c-1 (USD 0, sin API): proyección de costo de la prueba corta P4b propuesta, y
efecto del ajuste de P3c sobre la estimación de U-REEXT-T0.

P4b (propuesta del FRENO P3c-1): los dos brazos, el prefijo vigente (`3817de475c93`) y el de P3c, con la misma
e0-r2, sobre las unidades de P4b; más una pata de E3 sobre unas pocas unidades del brazo P3c. Tarifas por llamada,
medidas en P4 (`p4/salida/gasto_p4.json`): por llamada de E1 del brazo nuevo, la media de tokens de entrada sin caché
y de salida; el prefijo de P3c, con los tokens por carácter del prefijo medido en P4 (26.309 tokens para 55.105
caracteres); E3 y su reintento, por llamada de la pata de P4. Escenario alto: salida por 1,5 y E3 por 1,5.

U-REEXT-T0 (2.434 unidades): solo lo que cambia con P3c y se puede medir sin la API: las lecturas y escrituras de
caché del prefijo más largo y los caracteres de la línea de alcance nueva (con la calibración del mensaje de P1,
`p1/salida/censo_p1.json`, `calibracion.mensaje`). El efecto sobre la salida no se proyecta: lo mide P4b.

También cuenta, sin leer ningún texto, cuántos contenedores de lista de la tanda 0 (censo de U-DIAG-VINCULO) tienen una
cláusula con forma léxica de cada tipo de lista del punto b, sin los ya leídos: es solo un control de que hay de dónde
elegir; la elección de P4b es por lectura.

Escribe solo en --salida (proyeccion_p4b_p3c.json). Uso (desde la raíz de una copia):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p3c/proyeccion_p4b_p3c.py \
      --hashes HASHES_P3C --mensaje MENSAJE_P3C --salida DIR
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

P3C = Path(__file__).resolve().parent
sys.path.insert(0, str(P3C))
import mensaje_p3c_borrador as M  # noqa: E402  (los textos de la línea de alcance)

REPO = P3C.parents[3]
P4 = P3C.parent / "p4" / "salida"
CENSO_P1 = P3C.parent / "p1" / "salida" / "censo_p1.json"
CENSO_VINCULO = REPO / "reports" / "u_diag_vinculo" / "salidas" / "censo_anuncios.json"
E1 = {"in": 1.00, "out": 5.00, "cw": 1.25, "cr": 0.10}          # claude-haiku-4-5, USD por MTok
N_T0 = 2434
# Unidades de P4b por grupo (propuesta; ver diseno_p3c.md §9): a, b1 (ítems), b2 (ítems), encabezados de b, c, d, e,
# el ejemplo (cla::5.1.1::intro y cla::5.1.1.1) y f (cap::6.2.2.6).
GRUPOS = {"a": 4, "b1_items": 3, "b2_items": 3, "b_encabezados": 4, "c": 4, "d": 4, "e": 4, "ejemplo": 2, "f": 1}
PATA_E3 = 6
TIPO1 = re.compile(r"con excepci[oó]n de (los|las) siguientes|excepto (los|las) siguientes|salvo (los|las) siguientes|"
                   r"no comprende|se excluyen|quedan excluid|no se consideran", re.I)
TIPO2 = re.compile(r"excepto cuando|salvo cuando|salvo que|no (ser[aá]|resultar[aá]) (de aplicaci[oó]n|aplicable)|"
                   r"no regir[aá]", re.I)
AMPLIA = re.compile(r"exceptu|excluy|excluid|excepci|excepto|salvo|no comprend|no alcanz|no ser[aá]n? de aplicaci|"
                    r"no resultar", re.I)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hashes", type=Path, required=True)
    ap.add_argument("--mensaje", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    sal = a.salida.resolve()
    if REPO in sal.parents or sal == REPO:
        raise SystemExit("--salida no puede estar dentro del repo")
    g = json.loads((P4 / "gasto_p4.json").read_text(encoding="utf-8"))
    h = json.loads(a.hashes.read_text(encoding="utf-8"))
    msg = json.loads(a.mensaje.read_text(encoding="utf-8"))
    cal = json.loads(CENSO_P1.read_text(encoding="utf-8"))["calibracion"]["mensaje"]
    cs = g["e1_nuevo"]["cache_stats"]
    n4 = g["e1_nuevo"]["llamadas"]
    t_in, t_out = cs["tokens_in"] / n4, cs["tokens_out"] / n4
    pref_vig = cs["cache_write"]
    tok_car = pref_vig / h["congelado"]["caracteres"]
    pref_p3c = round(h["borrador"]["caracteres"] * tok_car)
    e3_llamada = (g["pata_e3"]["e3"]["gasto_usd_real"] / g["pata_e3"]["e3"]["llamadas"])
    e3_reint = g["pata_e3"]["e1_reintentos"]["gasto_usd_real"]
    n = sum(GRUPOS.values())

    def brazo(pref: int, k_out: float) -> float:
        return (pref * E1["cw"] + (n - 1) * pref * E1["cr"] + n * t_in * E1["in"] + n * t_out * k_out * E1["out"]) / 1e6

    esc = {}
    for nombre, k in (("central", 1.0), ("alto", 1.5)):
        b_vig, b_p3c = brazo(pref_vig, k), brazo(pref_p3c, k)
        e3 = PATA_E3 * e3_llamada * k + e3_reint * k
        esc[nombre] = {"brazo_vigente_usd": round(b_vig, 4), "brazo_p3c_usd": round(b_p3c, 4),
                       "pata_e3_usd": round(e3, 4), "total_usd": round(b_vig + b_p3c + e3, 4)}
    # U-REEXT-T0: lo que cambia con P3c, sin la salida
    d_pref = pref_p3c - pref_vig
    d_alcance_car = len(M.ALCANCE_NUEVO.format(sug="")) - len(M.ALCANCE_VIEJO.format(sug=""))
    u_alc = msg["e_linea_alcance"]["cambia_mensaje_e1"]
    t0 = {"prefijo_tokens_vigente": pref_vig, "prefijo_tokens_p3c_estimado": pref_p3c, "delta_prefijo_tokens": d_pref,
          "delta_lecturas_de_cache_usd": round((N_T0 - 5) * d_pref * E1["cr"] / 1e6, 4),
          "delta_escrituras_de_cache_usd": round(5 * d_pref * E1["cw"] / 1e6, 4),
          "delta_linea_alcance_caracteres": d_alcance_car, "unidades_con_linea_de_alcance": u_alc,
          "delta_linea_alcance_usd": round(u_alc * d_alcance_car * cal["tokens_por_caracter"] * E1["in"] / 1e6, 4),
          "nota": "el efecto sobre la salida de E1 (y con ella E3) no se proyecta: lo mide P4b"}
    t0["delta_total_sin_salida_usd"] = round(t0["delta_lecturas_de_cache_usd"] + t0["delta_escrituras_de_cache_usd"]
                                             + t0["delta_linea_alcance_usd"], 4)
    # pool de listas de excepciones, por forma léxica de la cláusula (solo conteo)
    cv = json.loads(CENSO_VINCULO.read_text(encoding="utf-8"))
    leidos_listas = {"ext::3.5.6::intro", "ext::13.4::intro", "ext::3.3.3::intro", "ctacte::6.2::intro",
                     "ctacte::5.1.2::intro", "cla::5.1.1::intro"}
    # las cinco que P4 leyó y descartó (p4/estrato_listas_excepciones.md, «Las que descarté»)
    descartadas_p4 = ("ext::3.5.4", "ext::2.6.1", "ext::7.8.4", "ext::2.7", "ext::3.16.2")
    cont = [c for c in cv["contenedores_tanda0"] if c["id"] not in leidos_listas
            and not any(c["id"] == d or c["id"].startswith(d + "::") for d in descartadas_p4)]
    pool = {"contenedores_tanda0_sin_leidos": len(cont),
            "forma_lexica_tipo1_lo_que_queda_afuera": sum(bool(TIPO1.search(c["clausula"])) for c in cont),
            "forma_lexica_tipo2_condiciones_de_una_excepcion": sum(bool(TIPO2.search(c["clausula"])) for c in cont),
            "forma_amplia_de_excepcion": sum(bool(AMPLIA.search(c["clausula"])) for c in cont),
            "particion_contenedores": len(cv["contenedores_particion"]),
            "particion_tipo1": sum(bool(TIPO1.search(c["clausula"])) for c in cv["contenedores_particion"]),
            "particion_tipo2": sum(bool(TIPO2.search(c["clausula"])) for c in cv["contenedores_particion"]),
            "particion_forma_amplia": sum(bool(AMPLIA.search(c["clausula"])) for c in cv["contenedores_particion"]),
            "particion_forma_amplia_tos": len({c["to"] for c in cv["contenedores_particion"]
                                               if AMPLIA.search(c["clausula"])}),
            "nota": "conteo léxico de control; la elección es por lectura, en P4b"}
    out = {"comando": "data/experiment/prompt_r2/p3c/proyeccion_p4b_p3c.py --hashes H --mensaje M --salida DIR",
           "p4b": {"grupos": GRUPOS, "unidades": n, "llamadas_e1": 2 * n, "pata_e3_unidades": PATA_E3,
                   "tarifa_p4": {"tokens_entrada_sin_cache_por_llamada": round(t_in, 1),
                                 "tokens_salida_por_llamada": round(t_out, 1), "e3_usd_por_llamada": round(e3_llamada, 5),
                                 "reintentos_e1_de_la_pata_usd": e3_reint},
                   "escenarios": esc, "tope_propuesto_usd": 1.5},
           "u_reext_t0": t0, "pool_listas_b": pool}
    sal.mkdir(parents=True, exist_ok=True)
    (sal / "proyeccion_p4b_p3c.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n",
                                                 encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
