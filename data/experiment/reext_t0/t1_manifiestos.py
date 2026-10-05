"""
t1_manifiestos.py — U-REEXT-T0, T1, punto 1 (mandato firmado en e2027dd): los tres manifiestos r2b pasan a leer la
E0 de C2 de U-R2-CODIGO-2 (`e0_chunking/salida_tanda0_r2b/`, 9f6361e), llevan los sellos del prefijo re-congelado en
P3c-2 de U-PROMPT-R2 (66cde30) con la temperatura de P5 (53b7708), y el tope global de USD 80 (decisión 1 de la autora
al firmar). Es el primer paso de la unidad (decisión de la autora del 04/10/2026).

Cambia solo `rutas.e0_salida`, `sellos` y `limites.tope_global_usd`, y agrega al final de `descripcion` una oración
fechada que registra el cambio (sin ella, la descripción seguiría diciendo `salida_tanda0_r2` y USD 69). El resto del
manifiesto queda byte a byte; el formato es el del archivo (json.dumps con indent=1, ensure_ascii=False y salto final).

Los valores de `sellos` son literales de este script, tomados de «Lo que llega de las unidades anteriores» del mandato
y del código de 53b7708; el control del punto 2 (t1_control_entradas.py) los compara con lo que el código carga.

Uso (desde la raíz del repo): PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/reext_t0/t1_manifiestos.py
      [--verificar]   (solo compara, no escribe)
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
MAN = REPO / "data" / "experiment" / "reextraccion_v2" / "manifiestos"
ARCHIVOS = ("tanda0_10tos_r2b.json", "tanda0_ens_diez_r2b.json", "tanda0_ens_desarrollo_r2b.json")
E0_R2B = "data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b"
TOPE_USD = 80.0
SELLOS = {
    "unidad": "U-REEXT-T0 (T1, punto 1; mandato firmado en e2027dd)",
    "commit_codigo": "53b7708",
    "e0": {"ruta": E0_R2B, "commit": "9f6361e", "archivos": 57},
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
        "candado_mensaje_r2b_json_sha256": "4d69f7f4c8a542bf09d25c1bcc4343a06a70226240eb595e3d4285a516e0fa6d",
        "mensaje_r2b_sha256": "a9cb702c0d243582d27345b78d2595b44e6cf0f4d9a2560fdd262aaa92955a56",
        "candado_mensaje_e3_json_sha256": "e8fa5dc47408d5f311d5677886cf9e90ab54e1808c64bd4514f66507d2375a82",
        "mensaje_e3_sha256": "da17c22e6c988c6e2fea12e4369caf96d27fe8cbc98f8861f9470901410c6e01",
    },
}
NOTA = (" U-REEXT-T0, T1, punto 1 (05/10/2026; mandato firmado en e2027dd): rutas.e0_salida pasa a salida_tanda0_r2b "
        "(9f6361e), los sellos son los del prefijo re-congelado en P3c-2 de U-PROMPT-R2 (322c5a23e9b7, 66cde30) con la "
        "temperatura de P5 (53b7708), y tope_global_usd pasa a USD 80 (decisión de la autora al firmar).")


def nuevo(d: dict) -> dict:
    d = json.loads(json.dumps(d))
    if not d["descripcion"].endswith(NOTA):
        d["descripcion"] += NOTA
    d["rutas"]["e0_salida"] = E0_R2B
    d["limites"]["tope_global_usd"] = TOPE_USD
    d["sellos"] = SELLOS
    return d


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verificar", action="store_true")
    a = ap.parse_args()
    ok = True
    for nombre in ARCHIVOS:
        p = MAN / nombre
        actual = json.loads(p.read_text(encoding="utf-8"))
        n = nuevo(actual)
        texto = json.dumps(n, ensure_ascii=False, indent=1) + "\n"
        igual = texto == p.read_text(encoding="utf-8")
        print(f"{nombre}: {'ya aplicado' if igual else 'a escribir'} | e0={n['rutas']['e0_salida']} "
              f"| tope={n['limites']['tope_global_usd']} | prefijo={n['sellos']['prefijo_e1']['hash']}")
        if a.verificar:
            ok &= igual
        elif not igual:
            p.write_text(texto, encoding="utf-8")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
