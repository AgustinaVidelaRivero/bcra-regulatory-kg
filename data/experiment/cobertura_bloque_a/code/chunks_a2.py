"""Construye las 191 unidades de extraccion del bloque A (los NUEVE).

Deterministico, SIN API. Cada unidad es un bloque de prosa contiguo dentro de
una pagina (modelo laudado, adenda 2 §3.3), con procedencia = documento +
pagina + offset y el campo nuevo `granularidad_procedencia = "pagina"`.

DECISIONES DE CONSTRUCCION, declaradas porque afectan lo que el extractor ve:

1. `unidad` lleva la DIRECCION DE PAGINA (`p{N}.b{offset}`), no un numero de
   punto fabricado. `comun_e1.puntos_admitidos` devuelve exactamente
   `[chunk["unidad"]]` para un chunk sin herencia y de tipo distinto de
   `mini_chunk`, de modo que el conjunto cerrado de `punto` es esa direccion
   y solo esa: el extractor no puede anclar en una espina que no existe.

2. `titulo` va VACIO. Estos documentos no titulan sus bloques; poner algo
   seria fabricarlo.

3. `herencia` va VACIA. Sin espina no hay cadena de ancestros.

4. Los FLAGS los produce el detector de PRODUCCION `e0_lib._flags_tabla_formula`
   sobre las lineas del bloque — NO los elige esta unidad. Importa: el flag
   `contenido_tabular` hace que el prompt aplique su seccion CONTENIDO
   NO-PROSA, de modo que elegirlo a mano sesgaria PL-2 y PL-4 hacia su
   cumplimiento. Sale de donde sale siempre.

5. El mensaje de usuario es el de PRODUCCION sin tocar
   (`prompt_v3_b54.build_user_message_v3`). Consecuencia declarada: la linea
   «Tipo de unidad: chunk de punto» aparece tambien para estas unidades. No
   se edita el modulo de produccion para arreglarla; se reporta.

Uso:  python3 chunks_a2.py          (escribe chunks_a2.json y no llama a nadie)
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import comun_coba as C  # noqa: E402
import censo_forma as CF  # noqa: E402
from e0_lib import separar_encabezado_pie, _flags_tabla_formula  # noqa: E402

NUEVE = tuple(t for t in C.DIEZ if t != "ri_spi")


def construir() -> list[dict]:
    out: list[dict] = []
    for to in NUEVE:
        paginas, roles, modal, bloques, _d = C.leer_documento(to)
        for i, (lineas, rol) in enumerate(zip(paginas, roles), start=1):
            if rol != C.E0.ROL_CUERPO:
                continue
            contenido, _x, _y = separar_encabezado_pie(lineas)
            brazo = CF.clase_forma(CF.densidad_prosa(contenido))
            # lineas de cada bloque, para el detector de flags de produccion
            umbral = C.FACTOR_BLANCO * modal if modal > 0 else float("inf")
            grupos: list[list] = []
            for l in contenido:
                if grupos and (l.top - grupos[-1][-1].top) <= umbral:
                    grupos[-1].append(l)
                else:
                    grupos.append([l])
            grupos = [g for g in grupos
                      if " ".join(x.texto.strip() for x in g).strip()]
            assert len(grupos) == len(bloques[i]), (
                f"{to} p.{i}: {len(grupos)} grupos vs {len(bloques[i])} bloques")
            for b, g in zip(bloques[i], grupos):
                assert b.texto == " ".join(x.texto.strip() for x in g).strip()
                out.append({
                    "id": f"{to}::p{b.pagina}.b{b.offset}",
                    "to": to,
                    "archivo": f"{to}.pdf",
                    "unidad": f"p{b.pagina}.b{b.offset}",
                    "titulo": "",
                    "tipo": "bloque_pagina",
                    "paginas": [b.pagina],
                    "texto": b.texto,
                    "herencia": [],
                    "flags": _flags_tabla_formula(g),
                    "granularidad_procedencia": "pagina",
                    "brazo": brazo,
                    "n_chars": b.n_chars,
                    "n_lineas": b.n_lineas,
                })
    return out


def main() -> int:
    chunks = construir()
    por_brazo = {}
    for c in chunks:
        d = por_brazo.setdefault(c["brazo"], {"unidades": 0, "chars": 0, "flag_tab": 0})
        d["unidades"] += 1
        d["chars"] += c["n_chars"]
        d["flag_tab"] += bool(c["flags"]["contenido_tabular"])
    salida = C.UNIDAD / "chunks_a2.json"
    salida.write_text(json.dumps(chunks, ensure_ascii=False, indent=1) + "\n",
                      encoding="utf-8")
    print(f"unidades: {len(chunks)}")
    for k, v in sorted(por_brazo.items()):
        print(f"  {k:16s} {v['unidades']:4d} unidades · {v['chars']:6d} chars · "
              f"{v['flag_tab']:3d} con flag contenido_tabular")
    assert len(chunks) == 191, len(chunks)
    assert sum(1 for c in chunks if c["brazo"] == "prosa") == 77
    assert sum(1 for c in chunks if c["brazo"] == "planilla_ficha") == 114
    assert len({c["id"] for c in chunks}) == 191, "ids duplicados"
    print(f"escrito: {salida.relative_to(C.REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
