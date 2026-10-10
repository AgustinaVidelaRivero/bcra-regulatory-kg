"""U-OMISIONES-COD, grupo A, ítem e — selftest de la pieza aparte (`parche_pieza_e_sobre_O2.diff`): el clasificador de la
copia de la nota de E3 en el ensamblado. NO está aplicada: entra solo si la lectura de su precisión llega al piso (notas
del 10/10/2026 al pie de la v7). Este selftest corre en una COPIA con la pieza aplicada; sin ella, sale con 2.

  S  sintéticos: clase 3 (palabra de la nota ausente de la unidad), clase 1 (metalenguaje del verificador), negativo
     (las ventanas están en la unidad) y negativo por flexión (la palabra es una flexión de una de la unidad);
  R  con --salida-r2 y --lista-sellada: el registro `copias_nota_clasificadas.jsonl` de la cadena r2b de diez reproduce
     las 57 filas de la lista sellada en O1 (sha256 4c385529…), campo por campo (sin `dentro_de_las_64_de_T4`).

Uso, desde la raíz de la copia: PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B <ruta>/selftest_pieza_e.py
     [--salida-r2 DIR --lista-sellada JSON]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

RAIZ = Path.cwd().resolve()
sys.path.insert(0, str(RAIZ / "data" / "experiment" / "tanda0" / "code"))
import ensamblar_tanda0 as ENS  # noqa: E402

RES: list[tuple[str, bool, str]] = []


def check(nombre: str, ok: bool, detalle: str = "") -> None:
    RES.append((nombre, bool(ok), str(detalle)[:240]))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida-r2", type=Path, default=None)
    ap.add_argument("--lista-sellada", type=Path, default=None)
    a = ap.parse_args()
    if not hasattr(ENS, "clasificar_campo_copia_nota"):
        print("la pieza (e) no está aplicada en esta copia")
        return 2
    assert Path(ENS.__file__).resolve().is_relative_to(RAIZ)
    V = ENS.E4.modulo_validador_r2()
    sys.path.insert(0, str(RAIZ / "data" / "experiment" / "prompt_r2" / "p3b2"))
    import lista_copia_nota as L0  # noqa: PLC0415

    def ctx(unidad: str, notas: list[str], citas: list[str] = ()) -> dict:
        n = ENS.VENTANA_COPIA_NOTA_CLASIFICADOR
        u = V.norm_tokens(unidad)
        return {"toks_unidad": set(u), "toks_citas": {t for x in citas for t in V.norm_tokens(x)},
                "ventanas_notas": set().union(*(ENS._ventanas(V.norm_tokens(x), n) for x in notas)),
                "ventanas_unidad": ENS._ventanas(u, n), "ventanas_citas": ENS._ventanas(V.norm_tokens(" ".join(citas)), n)}
    c = ctx("La entidad deberá registrar el monto de cada operación.",
            ["Falta la obligación de registrar el cómputo de cada operación."])
    r = ENS.clasificar_campo_copia_nota("Obligación de registrar el cómputo", c, V, L0.VACIAS, L0.METALENGUAJE)
    check("e+ clase 3: «obligación» y «cómputo» vienen de la nota y no están en la unidad",
          r is not None and r["clase"] == 3 and r["palabras_de_la_nota"] == ["computo", "obligacion"], r)
    r = ENS.clasificar_campo_copia_nota("deberá registrar el monto", c, V, L0.VACIAS, L0.METALENGUAJE)
    check("e- las palabras del campo están en la unidad: sin detección", r is None, r)
    c = ctx("Las operaciones que no hayan podido liquidarse.", ["Faltan las operaciones liquidadas."])
    r = ENS.clasificar_campo_copia_nota("las operaciones liquidadas", c, V, L0.VACIAS, L0.METALENGUAJE)
    check("e- flexión: «liquidadas» es una flexión de «liquidarse»: sin detección", r is None, r)
    c = ctx("El cliente presentará la declaración.", ["El faltante de la unidad es la declaración del cliente."])
    r = ENS.clasificar_campo_copia_nota("faltante de la unidad: declaración", c, V, L0.VACIAS, L0.METALENGUAJE)
    check("e+ clase 1: metalenguaje del verificador («faltante», «unidad») copiado de la nota",
          r is not None and r["clase"] == 1 and set(r["metalenguaje"]) >= {"faltante", "unidad"}, r)
    c = ctx("Texto.", ["registrar el cómputo diario"], citas=["registrar el cómputo diario"])
    r = ENS.clasificar_campo_copia_nota("registrar el cómputo diario", c, V, L0.VACIAS, L0.METALENGUAJE)
    check("e- lo que está en la cita del faltante no es copia de la nota", r is None, r)
    if a.salida_r2 is not None and a.lista_sellada is not None:
        fil = [json.loads(x) for x in (a.salida_r2 / "copias_nota_clasificadas.jsonl").read_text(encoding="utf-8").splitlines()
               if x.strip()]
        sel = json.loads(a.lista_sellada.read_text(encoding="utf-8"))["detecciones"]
        clave = lambda x: json.dumps({k: v for k, v in x.items() if k != "dentro_de_las_64_de_T4"}, sort_keys=True,  # noqa: E731
                                     ensure_ascii=False)
        check("e en la cadena: el registro reproduce la lista sellada de O1, fila por fila",
              sorted(map(clave, fil)) == sorted(map(clave, sel)), f"{len(fil)} filas contra {len(sel)}")
    for nombre, ok, det in RES:
        print(f"  [{'PASS' if ok else 'FAIL'}] {nombre}" + ("" if ok else f" — {det}"))
    ok = sum(1 for x in RES if x[1])
    print(f"SELFTEST PIEZA E: {ok}/{len(RES)} {'PASS' if ok == len(RES) else 'FAIL'}")
    return 0 if ok == len(RES) else 1


if __name__ == "__main__":
    raise SystemExit(main())
