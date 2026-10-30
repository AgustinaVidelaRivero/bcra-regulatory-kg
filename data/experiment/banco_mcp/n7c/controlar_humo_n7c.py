#!/usr/bin/env python3
"""controlar_humo_n7c.py — El control del humo de B2 de N7c (USD 0): en el log R1 del intento final de cada sesión de la
entrada, las llamadas a ver_punto y, en cada salida que muestra un punto (las de error, «ver_punto: no existe…», no cuentan),
las tres marcas que suma la corrección:
  - la sección de N7c: un renglón que empieza con «Puntos relacionados (» o que es «Puntos relacionados: ninguno»;
  - la familia de N7c+: un renglón que empieza con «Puntos de la misma familia (» o que es «Puntos de la misma familia: ninguno»;
  - la cita de N7c+: el último renglón empieza con «Para citar este punto: » y trae « | ».
Lo esperado, por configuración: N7, ninguna de las tres; N7c, solo la sección; N7c+ (clave N7c_amp), las tres. Por sesión:
«pasa» si todas sus salidas de ver_punto traen lo esperado, «no pasa» si alguna no, y «no concluyente» si no llamó a ver_punto
(o no tiene log R1). Las sesiones y su intento final salen de la entrada y de la salida del corredor (correr_n7c: cargar_entrada
y estado), como las ve el corredor.
Escribe en <salida>/control_humo_n7c.json y no imprime nada de una pregunta ni de un punto: solo cuentas, configuraciones y
veredictos. Códigos: 0 todas pasan; 1 alguna no pasa; 2 ninguna falla pero alguna no es concluyente.
Uso: .venv/bin/python -B data/experiment/banco_mcp/n7c/controlar_humo_n7c.py --entrada <json> --sha256-entrada <hex> --salida <dir>
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
if str(AQUI) not in sys.path:
    sys.path.insert(0, str(AQUI))
import correr_n7c as C7                         # noqa: E402

CN = C7.CN
ESPERADO = {"N7": (False, False, False), "N7c": (True, False, False), "N7c_amp": (True, True, True)}


def marcas(salida: str) -> tuple[bool, bool, bool]:
    lineas = salida.split("\n")
    seccion = any(x.startswith("Puntos relacionados (") or x == "Puntos relacionados: ninguno" for x in lineas)
    familia = any(x.startswith("Puntos de la misma familia (") or x == "Puntos de la misma familia: ninguno" for x in lineas)
    cita = lineas[-1].startswith("Para citar este punto: ") and " | " in lineas[-1]
    return seccion, familia, cita


def controlar_sesion(log: Path | None, configuracion: str) -> dict:
    if log is None or not log.is_file():
        return {"veredicto": "no concluyente", "motivo": "sin log R1", "ver_punto": 0}
    llamadas = [json.loads(x) for x in log.read_text(encoding="utf-8").splitlines() if x.strip()]
    vp = [x for x in llamadas if x.get("evento") == "llamada" and x.get("tool") == "ver_punto"
          and isinstance(x.get("output_str"), str) and not x["output_str"].startswith("ver_punto:")]
    if not vp:
        return {"veredicto": "no concluyente", "motivo": "no llamó a ver_punto (o solo con error)", "ver_punto": 0}
    ms = [marcas(x["output_str"]) for x in vp]
    cuenta = {"ver_punto": len(vp), "con_seccion": sum(m[0] for m in ms), "con_familia": sum(m[1] for m in ms),
              "con_cita": sum(m[2] for m in ms)}
    ok = all(m == ESPERADO[configuracion] for m in ms)
    return cuenta | {"veredicto": "pasa" if ok else "no pasa"}


def controlar(e: dict, salida: Path) -> dict:
    st = CN.estado(e, salida)
    filas = []
    for sid, v in st["por_sesion"].items():
        conf = v["sesion"]["configuracion"]
        f = v["final"]
        log = Path(f["carpeta"]) / f"log_r1_{f['id']}.jsonl" if f else None
        filas.append({"sesion": sid, "configuracion": conf, "clase_final": f["clase"] if f else "sin correr",
                      **controlar_sesion(log, conf)})
    ver = [x["veredicto"] for x in filas]
    return {"unidad": "N7c, control del humo de B2", "esperado": {k: dict(zip(("seccion", "familia", "cita"), v))
                                                                  for k, v in ESPERADO.items()},
            "sesiones": filas, "pasan": ver.count("pasa"), "no_pasan": ver.count("no pasa"),
            "no_concluyentes": ver.count("no concluyente"),
            "codigo": 1 if "no pasa" in ver else 2 if "no concluyente" in ver else 0}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--entrada", type=Path, required=True)
    ap.add_argument("--sha256-entrada", required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args(argv)
    try:
        e = CN.cargar_entrada(a.entrada, a.sha256_entrada)
    except CN.Freno as f:
        print(f"FRENO (código {f.codigo}): {f.motivo}")
        return f.codigo
    r = controlar(e, a.salida.resolve())
    (a.salida / "control_humo_n7c.json").write_text(json.dumps(r, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for x in r["sesiones"]:
        print(f"{x['configuracion']}: {x['veredicto']} (clase {x['clase_final']}; ver_punto {x['ver_punto']}"
              + (f", sección {x['con_seccion']}, familia {x['con_familia']}, cita {x['con_cita']}" if "con_seccion" in x else "")
              + ")")
    print(f"control del humo: {r['pasan']} pasan, {r['no_pasan']} no pasan, {r['no_concluyentes']} no concluyentes; "
          f"código {r['codigo']}")
    return r["codigo"]


if __name__ == "__main__":
    raise SystemExit(main())
