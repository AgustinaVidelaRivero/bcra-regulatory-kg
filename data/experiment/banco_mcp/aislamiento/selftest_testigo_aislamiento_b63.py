#!/usr/bin/env python3
"""selftest_testigo_aislamiento_b63.py — El selftest del testigo con la configuración por parámetro (testigo_aislamiento_b63.py; etapa
b2 del runner de B6.3). USD 0 y sin lanzar ningún CLI ni ningún servidor: arma las sesiones con las funciones del testigo, sin correrlas.
  1. la configuración: sin parámetro, la de prueba de N6 (la de HEAD); con la de B6.3 y su sha256, la de B6.3; con otro sha256, frena;
  2. el plan: con la de N6, el de HEAD (sus tandas, los negativos sobre kg y fragmentos_bm25, el grafo en cada tanda); con la de B6.3,
     una sesión a la vez, dos vueltas por sus tres brazos, los negativos sobre el grafo y la principal de fragmentos, y ningún brazo
     exigido en cada tanda;
  3. la comparación con el init (comparar_con_init), sobre un init sintético con el comando que escribe el lanzador en modo init: el
     control positivo (la sesión tal cual da PASS, con ANTHROPIC_BASE_URL como único valor distinto) y los dos negativos (otro
     mcp_config, u otra variable en el entorno de la sesión: no da PASS, y el testigo no da PASS).
Uso, desde la raíz de una copia del repo: SELFTEST_TESTIGO_TMP=<carpeta> BANCO_VENV_VECTOR=<venv> <python del .venv> -B
  data/experiment/banco_mcp/aislamiento/selftest_testigo_aislamiento_b63.py
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
import tempfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parent
import testigo_aislamiento_b63 as T                         # noqa: E402  (de esta carpeta: se importa)

CONFIG_B63 = BANCO_DIR / "b63" / "v2" / "b2" / "config_agentes_b63.json"
if not os.environ.get("SELFTEST_TESTIGO_TMP"):
    raise SystemExit("falta SELFTEST_TESTIGO_TMP (la carpeta de trabajo; nada en la carpeta temporal del sistema)")
if os.environ.get("ANTHROPIC_API_KEY"):
    raise SystemExit("ABORTO: el selftest corre sin ninguna clave en el entorno")
TMP = Path(tempfile.mkdtemp(prefix="selftest_testigo_b63_", dir=os.environ["SELFTEST_TESTIGO_TMP"]))
os.environ.setdefault("NEO4J_URI", "bolt://127.0.0.1:47687")
RES: list[tuple[bool, str]] = []


def caso(nombre: str):
    def deco(f):
        try:
            ok, detalle = f()
        except BaseException as ex:                        # noqa: BLE001  (también SystemExit, para el control)
            ok, detalle = False, f"{type(ex).__name__}: {str(ex)[:160]}"
        RES.append((bool(ok), nombre + (f" — {detalle}" if detalle else "")))
        return f
    return deco


def sha(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


@caso("la configuración: sin parámetro, la de prueba de N6; con la de B6.3 y su sha256, la de B6.3; con otro sha256, frena")
def _():
    n6 = T.cargar_configuracion(None, None)
    b63 = T.cargar_configuracion(CONFIG_B63, sha(CONFIG_B63))
    try:
        T.cargar_configuracion(CONFIG_B63, "0" * 64)
        frena = False
    except SystemExit as ex:
        frena = "FRENO" in str(ex)
    return (sorted(n6["brazos"]) == ["fragmentos_bm25", "fragmentos_hibrida", "kg"]
            and sorted(b63["brazos"]) == ["fragmentos_denso", "fragmentos_hibrida", "kg"] and frena), None


@caso("el plan: con la de N6, el de HEAD; con la de B6.3, una sesión a la vez, dos vueltas por sus tres brazos y los negativos sobre el grafo y la principal de fragmentos")
def _():
    p6 = T.plan_de_la_configuracion(T.cargar_configuracion(None, None), True)
    pb = T.plan_de_la_configuracion(T.cargar_configuracion(CONFIG_B63, sha(CONFIG_B63)), False)
    return (p6["tandas"] == T.TANDAS and p6["negativos"] == T.NEGATIVOS_N6 and p6["en_cada_tanda"] == "kg"
            and pb["tandas"] == [["kg"], ["fragmentos_hibrida"], ["fragmentos_denso"]] * 2 and all(len(t) == 1 for t in pb["tandas"])
            and [b for b, _ in pb["negativos"]] == ["kg", "fragmentos_hibrida"] and pb["en_cada_tanda"] is None), \
        f"{len(pb['tandas'])} tandas de una sesión"


def init_sintetico(s: dict, init_dir: Path) -> None:
    """El comando de una sesión init del brazo, como lo escribe el lanzador en modo init: el argv con <prompt> y el JSON de MCP relativo,
    y el entorno de la sesión con la carpeta personal como $HOME, ANTHROPIC_BASE_URL al puerto cerrado y la clave por presencia."""
    casa = str(Path.home())
    entorno = {k: v.replace(casa, "$HOME") for k, v in s["env"].items()}
    entorno["ANTHROPIC_BASE_URL"] = "http://127.0.0.1:9"
    entorno["ANTHROPIC_API_KEY"] = "presente: sí"
    d = init_dir / f"B63-I1-r1-{s['brazo']}"
    d.mkdir(parents=True, exist_ok=True)
    argv = [("<prompt>" if x == s["prompt"] else (T.rel_repo(x) if x == s["mcp_json"] else x)) for x in s["cmd"]]
    (d / f"comando_B63-I1-r1-{s['brazo']}.json").write_text(json.dumps({"argv": argv, "env_declarado": {"entorno_de_la_sesion": entorno}},
                                                                       ensure_ascii=False) + "\n", encoding="utf-8")


@caso("la comparación con el init: la sesión tal cual da PASS; con otro mcp_config, o con otra variable en su entorno, no da PASS (el testigo no daría PASS)")
def _():
    cfg = T.cargar_configuracion(CONFIG_B63, sha(CONFIG_B63))
    init_dir, raiz = TMP / "init", TMP / "ses"
    out = {}
    for b in cfg["brazos"]:
        s = T.armar_sesion(cfg, b, f"TESTIGO-T1-1-{b}", "Pregunta de prueba del selftest: sin modelo.", TMP / "out" / b, raiz,
                           "http://127.0.0.1:9/captura/x")
        init_sintetico(s, init_dir)
        bien = T.comparar_con_init(s, init_dir)
        otro_b = next(x for x in cfg["brazos"] if x != b)
        otro_mcp = str(BANCO_DIR / cfg["brazos"][otro_b]["mcp_config"])
        otro = dict(s, cmd=[otro_mcp if x == s["mcp_json"] else x for x in s["cmd"]], mcp_json=otro_mcp)
        mas = dict(s, env=s["env"] | {"VARIABLE_DE_MAS_B63": "x"})
        out[b] = (bien["PASS"] and bien["distintos_fuera_de_los_de_cada_sesion"] == ["ANTHROPIC_BASE_URL"],
                  not T.comparar_con_init(otro, init_dir)["PASS"], not T.comparar_con_init(mas, init_dir)["PASS"])
    return all(all(v) for v in out.values()), f"{sum(all(v) for v in out.values())} de {len(out)} brazos"


def main() -> int:
    for ok, t in RES:
        print(("PASS " if ok else "FAIL ") + t)
    n = sum(ok for ok, _ in RES)
    print(f"selftest del testigo de B6.3: {n} de {len(RES)} en PASS")
    return 0 if n == len(RES) else 1


if __name__ == "__main__":
    raise SystemExit(main())
