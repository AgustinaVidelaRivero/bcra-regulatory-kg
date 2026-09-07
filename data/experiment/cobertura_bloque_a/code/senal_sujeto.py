"""Guarda 2, medición de apoyo — ¿la unidad nombra a su sujeto obligado?

`aplica_a` (Obligacion|Restriccion|Excepcion|Operacion|Potestad → Sujeto) es
el predicado del esquema congelado que ancla una norma a quién la debe
cumplir. Con unidades chicas y sin espina, el sujeto puede quedar fuera de la
unidad (está en el título del documento o en una página anterior). Esta
medición cuenta, por documento, cuántos bloques nombran alguna entrada del
catálogo de sujetos del esquema congelado.

Es una COTA INFERIOR de superficie léxica, no una medición semántica: cuenta
menciones textuales de las 70 entradas del catálogo, no resuelve anáforas ni
sujetos heredados del encabezado. Sirve para dimensionar el problema, no para
resolverlo.

Uso:  python3 senal_sujeto.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import comun_coba as C  # noqa: E402
import censo_forma as CF  # noqa: E402
from e0_lib import separar_encabezado_pie  # noqa: E402

sys.path.insert(0, str(C.EXPERIMENT / "esq/code"))
import prompt_congelado as PC  # noqa: E402


def formas_de_superficie() -> dict[str, re.Pattern]:
    """`Sujeto_entidad_financiera` → patrón que casa 'entidad(es) financiera(s)'.
    Derivación mecánica del identificador del catálogo; sin sinónimos a mano."""
    pats = {}
    for s in PC.SUJETOS_CATALOGO:
        base = s[len("Sujeto_"):].replace("_", " ")
        if base in ("sujeto", "sujeto regulado", "estructura"):
            continue  # genéricos del vocabulario, no formas de superficie
        # plural tolerante en cada palabra de ≥4 letras
        partes = [re.escape(w) + ("e?s?" if len(w) >= 4 else "")
                  for w in base.split()]
        pats[s] = re.compile(r"\b" + r"\s+".join(partes) + r"\b", re.IGNORECASE)
    return pats


def main() -> int:
    pats = formas_de_superficie()
    out, tot_b, tot_c = {}, 0, 0
    for to in C.DIEZ:
        paginas, roles, modal, bloques, _d = C.leer_documento(to)
        n = con = 0
        hallados: dict[str, int] = {}
        for i, (lineas, rol) in enumerate(zip(paginas, roles), start=1):
            if rol != C.E0.ROL_CUERPO:
                continue
            cont, _x, _y = separar_encabezado_pie(lineas)
            if CF.clase_forma(CF.densidad_prosa(cont)) == "planilla_ficha":
                continue          # el modelo de prosa no aplica ahí
            for b in bloques[i]:
                n += 1
                ms = [s for s, p in pats.items() if p.search(b.texto)]
                if ms:
                    con += 1
                    for s in ms:
                        hallados[s] = hallados.get(s, 0) + 1
        out[to] = {
            "bloques_prosa_y_mixta": n,
            "bloques_que_nombran_sujeto": con,
            "fraccion": round(con / n, 3) if n else None,
            "sujetos_hallados": dict(sorted(hallados.items(),
                                            key=lambda kv: -kv[1])),
        }
        tot_b += n
        tot_c += con
        print(f"{to:14s} bloques={n:4d} nombran_sujeto={con:3d} "
              f"({con/n if n else 0:.0%})  {list(hallados)[:3]}")

    agregado = {"bloques": tot_b, "nombran_sujeto": tot_c,
                "fraccion": round(tot_c / tot_b, 3) if tot_b else None,
                "sin_sujeto_nombrado": tot_b - tot_c}
    print("\nAGREGADO:", json.dumps(agregado, ensure_ascii=False))
    salida = C.UNIDAD / "senal_sujeto.json"
    salida.write_text(json.dumps(
        {"_nota": "cota inferior por superficie lexica sobre el catalogo de "
                  "sujetos del esquema congelado; no resuelve anafora ni "
                  "sujeto heredado del encabezado. Solo bloques de paginas "
                  "de clase prosa o mixta.",
         "_catalogo": "prompt_congelado.SUJETOS_CATALOGO (70 entradas)",
         "agregado": agregado, "por_to": out}, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8")
    print(f"escrito: {salida.relative_to(C.REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
