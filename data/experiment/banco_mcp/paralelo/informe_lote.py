#!/usr/bin/env python3
"""informe_lote.py — Una línea por sesión del registro de un lote (lanzar_lote_paralelo.py): estado, R3, costo R9, los
reintentos de la API y los 429 del stream, worker, tanda, horas, la fecha (la del reloj del lanzador al empezar) y la
versión del CLI de su system/init; y el total. Ninguna salida de tool.
Uso: informe_lote.py <registro_lote.json>
"""
from __future__ import annotations

import json
import sys


def main(argv: list[str]) -> int:
    r = json.load(open(argv[1], encoding="utf-8"))
    print(f"lote: P={r['P']} modo={r['modo']} tope={r['tope_usd']} freno={r['freno_usd']} código={r['codigo']} "
          f"acumulado R9={r['acumulado_R9_usd']} USD")
    if r.get("freno"):
        print("freno:", r["freno"])
    for s in r["sesiones"]:
        print(f"{s['id']:<28} {s['brazo']:<19} {s['estado']:<18} R3={'sí' if s.get('completa_R3') else 'no':<2} "
              f"R9={s.get('costo_R9_usd', 0):<9} reintentos={s.get('reintentos_api', '-'):<3} 429={s.get('errores_429', '-'):<3} "
              f"worker={s.get('worker', '-')} tanda={s['tanda']} inicio={s.get('inicio', '-')} fin={s.get('fin', '-')} "
              f"fecha={s.get('fecha') or '-'} cli={s.get('version_cli_init') or '-'}")
    tot_r = sum(s.get("reintentos_api", 0) for s in r["sesiones"])
    tot_4 = sum(s.get("errores_429", 0) for s in r["sesiones"])
    print(f"total: {tot_r} reintentos, {tot_4} con 429; orden de fin: {', '.join(r['orden_de_fin'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
