"""Medicion de apoyo — palabras cortadas por guion de particion en los bloques.

El camino vigente CORRIGE las fronteras intra-palabra que el PDF introduce al
justificar («obli- gacion»): `e0_lib.corregir_fronteras_intra_palabra` las
llevo de 200 a 0 en `cap` (`e0_chunking/salida/conteos.json` §cap, campos
`fronteras_intra_palabra_antes` / `_despues`). Esa correccion opera sobre el
arbol de puntos (`ResultadoParseo`), de modo que el modelo de unidad de pagina
NO la hereda. Esta medicion cuantifica el arrastre.

Uso:  python3 palabra_partida.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import comun_coba as C  # noqa: E402

# guion de particion: minuscula + '- ' + minuscula (no casa '-APARTADO A',
# ni los guiones de enumeracion, ni '– ' de raya)
RE_PARTIDA = re.compile(r"[a-záéíóúüñ]- [a-záéíóúüñ]")


def main() -> int:
    por_to, tot, aff, occ = {}, 0, 0, 0
    ejemplos = []
    for to in C.DIEZ:
        _p, _r, _m, bloques, _d = C.leer_documento(to)
        n = a = o = 0
        for v in bloques.values():
            for b in v:
                n += 1
                ms = RE_PARTIDA.findall(b.texto)
                if ms:
                    a += 1
                    o += len(ms)
                    if len(ejemplos) < 5:
                        i = RE_PARTIDA.search(b.texto).start()
                        ejemplos.append({"to": to, "pagina": b.pagina,
                                         "offset": b.offset,
                                         "fragmento": b.texto[max(0, i - 45):i + 45]})
        por_to[to] = {"bloques": n, "con_palabra_partida": a,
                      "fraccion": round(a / n, 3) if n else None,
                      "ocurrencias": o}
        tot += n
        aff += a
        occ += o
        print(f"{to:14s} bloques={n:4d} con_palabra_partida={a:3d} "
              f"({a/n if n else 0:.1%}) ocurrencias={o:3d}")

    agregado = {"bloques": tot, "con_palabra_partida": aff,
                "fraccion": round(aff / tot, 4), "ocurrencias": occ}
    print("\nAGREGADO:", json.dumps(agregado, ensure_ascii=False))
    salida = C.UNIDAD / "palabra_partida.json"
    salida.write_text(json.dumps(
        {"_nota": "el modelo de unidad de pagina no hereda "
                  "e0_lib.corregir_fronteras_intra_palabra, que el camino "
                  "vigente si aplica sobre el arbol de puntos",
         "agregado": agregado, "por_to": por_to, "ejemplos": ejemplos},
        ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"escrito: {salida.relative_to(C.REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
