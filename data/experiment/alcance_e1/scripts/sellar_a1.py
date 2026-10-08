"""
sellar_a1.py — U-ALCANCE-E1, A1 (USD 0): calcula los dos valores PROPUESTOS del candado del mensaje de E1 r2b sobre el
código y los datos de la copia que se pasa con --raiz (regla l), como sellar_p3c2.py de U-PROMPT-R2. No escribe en la copia
ni en el repo: imprime y guarda en --salida un JSON con los valores, que se copian a mano a las constantes.

  - CANDADO_MENSAJE_JSON_SHA256_ESPERADO: sha256 de e1_extractor/candado_mensaje_r2b.json;
  - MENSAJE_R2B_SHA256_ESPERADO: sha256 de los mensajes de sus unidades (prompt_r2b.sha256_mensajes);
  - y, de control, el sha256 del derivado del registro contra REGISTRO_ALCANCE_R2B_SHA256_ESPERADO.

Para calcular el valor que el propio candado compara, el módulo se ejecuta desde su fuente con la llamada al candado del
mensaje neutralizada y el sha de la fixture puesto (en memoria, nunca en el archivo). Con --verificar, en cambio, importa
el módulo tal como está y controla que los valores sellados coincidan.

Uso: PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B sellar_a1.py --raiz COPIA --salida DIR [--verificar]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import types
from pathlib import Path


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def ejecutar(nombre: str, ruta: Path, cambios: list[tuple[str, str]]) -> types.ModuleType:
    """Ejecuta el módulo desde su fuente con `cambios` (patrón de una línea entera → reemplazo), cada uno presente una
    sola vez; con el literal puesto o con un marcador, da lo mismo."""
    src = ruta.read_text(encoding="utf-8")
    for a, b in cambios:
        n = len(re.findall(a, src, flags=re.M))
        if n != 1:
            raise SystemExit(f"{nombre}: el fragmento a neutralizar aparece {n} veces")
        src = re.sub(a, lambda _m: b, src, flags=re.M)
    mod = types.ModuleType(nombre)
    mod.__file__ = str(ruta)
    sys.modules[nombre] = mod
    exec(compile(src, str(ruta), "exec"), mod.__dict__)
    return mod


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--raiz", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    ap.add_argument("--verificar", action="store_true")
    a = ap.parse_args()
    raiz = a.raiz.resolve()
    sal = a.salida.resolve()
    if raiz in sal.parents or sal == raiz:
        raise SystemExit("--salida no puede estar dentro de la copia")
    e1 = raiz / "data" / "experiment" / "reextraccion_v2" / "e1_extractor"
    sys.path.insert(0, str(e1))
    fixture = e1 / "candado_mensaje_r2b.json"
    derivado = raiz / "data" / "experiment" / "catalogo_unico" / "registro_alcance_r2b.json"
    v = {"CANDADO_MENSAJE_JSON_SHA256_ESPERADO": sha(fixture), "sha256_derivado": sha(derivado)}
    chunks = json.loads(fixture.read_text(encoding="utf-8"))["chunks"]
    if a.verificar:
        import prompt_r2b as R  # noqa: PLC0415 — con sus candados
        res = {"constantes": {k: getattr(R, k) for k in ("CANDADO_MENSAJE_JSON_SHA256_ESPERADO",
                                                          "MENSAJE_R2B_SHA256_ESPERADO",
                                                          "REGISTRO_ALCANCE_R2B_SHA256_ESPERADO")},
               "fixture_sha256": v["CANDADO_MENSAJE_JSON_SHA256_ESPERADO"], "derivado_sha256": v["sha256_derivado"],
               "mensaje_r2b": R.sha256_mensajes(chunks), "unidades_de_la_fixture": len(chunks),
               "importa_sin_frenar": True}
        res["coinciden"] = (res["constantes"]["CANDADO_MENSAJE_JSON_SHA256_ESPERADO"] == res["fixture_sha256"]
                            and res["constantes"]["MENSAJE_R2B_SHA256_ESPERADO"] == res["mensaje_r2b"]
                            and res["constantes"]["REGISTRO_ALCANCE_R2B_SHA256_ESPERADO"] == res["derivado_sha256"])
    else:
        R = ejecutar("prompt_r2b", e1 / "prompt_r2b.py", [
            (r'^CANDADO_MENSAJE_JSON_SHA256_ESPERADO = "[^"]*"$',
             f'CANDADO_MENSAJE_JSON_SHA256_ESPERADO = "{v["CANDADO_MENSAJE_JSON_SHA256_ESPERADO"]}"'),
            (r"^_candado_mensaje\(\)$", ""),
        ])
        v["MENSAJE_R2B_SHA256_ESPERADO"] = R.sha256_mensajes(chunks)
        v["unidades_de_la_fixture"] = len(chunks)
        v["derivado_igual_al_literal"] = v["sha256_derivado"] == R.REGISTRO_ALCANCE_R2B_SHA256_ESPERADO
        v["prefijo_hash"] = R.PREFIJO_HASH_R2B
        res = v
    sal.mkdir(parents=True, exist_ok=True)
    nombre = "verificacion_sellos_a1.json" if a.verificar else "sellos_a1.json"
    (sal / nombre).write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(res, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
