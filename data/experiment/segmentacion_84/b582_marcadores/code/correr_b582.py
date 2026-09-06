#!/usr/bin/env python3
"""B5.8.2 — corrida de las reglas de marcador por familia sobre los TOs
objetivo (familias b_idx/b_sec del censo B5.8.0 cuyo veredicto remite a
B5.8.2, recomputados de censo_84.json; ri_tsa corre además como CONTROL
declarado: la regla B5.2 vigente ya lo engancha, se espera que produzca
unidades por el camino vigente y JAMÁS entre a las etapas nuevas — su
re-corrida adjudicada es de B5.8.4, acá solo verifica la compuerta).

Flujo por TO (garantía estructural heredada de B5.8.1): primero el camino
VIGENTE completo; solo con cero unidades se reintenta con las reglas de
marcador (clasificación con variantes de índice + gramática de sección
variante + banner de caja mixta; e0_lib, docstring del módulo); solo si esa
etapa también da cero se cae al modo sin raíz de B5.8.1 sobre la
clasificación de marcadores. Sub-chunking de U-B5.3 aplicado a las unidades
nuevas; health-check por TO con healthcheck_e0.health_check_to (que ejecuta
la misma escalera por su cuenta).

Cero LLM, USD 0. Salidas (por TO, en ../<to>/): estructura, indice, chunks,
divergencias, cobertura, correcciones, sub_chunking (si aplica),
healthcheck. Consolidado: ../conteos_b582.json.

Uso (desde cualquier cwd):
    python3 data/experiment/segmentacion_84/b582_marcadores/code/correr_b582.py [--solo TO1,TO2]
"""

from __future__ import annotations

import argparse
import collections
import json
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[5]
E0_DIR = REPO / "data/experiment/reextraccion_v2/e0_chunking"
PREP = REPO / "data/experiment/escalado_prep"
CENSO = REPO / "data/experiment/segmentacion_84/censo_84.json"
SALIDA = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(E0_DIR))
import correr_e0  # noqa: E402  (solo subdividir_unidades_grandes; no se edita)
import e0_lib as E0  # noqa: E402
from healthcheck_e0 import health_check_to  # noqa: E402

CONTROL_EXTRA = ["ri_tsa"]   # b_idx ya enganchado por B5.2; re-corrida en B5.8.4


def tos_objetivo() -> list[str]:
    """Los TOs de familias b_idx/b_sec cuyo veredicto preliminar REMITE a la
    regla de marcador de B5.8.2. El veredicto 'regla vigente (B5.2)…'
    (ri_tsa) no cuenta como remisión: su re-corrida es de B5.8.4. Regla i:
    la lista se recomputa acá, no se transcribe."""
    censo = json.load(open(CENSO, encoding="utf-8"))
    return sorted(t for t, d in censo.items()
                  if d["familia_primaria"] in ("b_idx", "b_sec")
                  and d["veredicto_preliminar"]
                  == "segmentable con regla de familia b (marcador, B5.8.2)")


def correr_to(ident: str) -> dict:
    t0 = time.time()
    pdf = PREP / "pdfs" / f"{ident}.pdf"
    paginas = E0.extraer_lineas(pdf)
    roles_v = E0.clasificar_paginas(paginas)

    def pipeline(res: "E0.ResultadoParseo") -> list[dict]:
        fr_antes = E0.detectar_fronteras_intra_palabra(res)
        res.reasignaciones_continuidad = E0.aplicar_continuidad_enumeracion(res)
        regla2 = E0.corregir_fronteras_intra_palabra(res)
        fr_despues = E0.detectar_fronteras_intra_palabra(res)
        res.correccion_fronteras = {"antes": fr_antes["n_intra_palabra"],
                                    "despues": fr_despues["n_intra_palabra"],
                                    **regla2}
        return E0.construir_chunks(res)

    # ---- etapa 1: camino vigente completo (la activación exige comprobarlo)
    roles = roles_v
    res = E0.parsear_cuerpo(ident, pdf.name, paginas, roles)
    chunks = pipeline(res)
    activado = not chunks
    marcadores = False
    if activado:
        # ---- etapa 2: reglas de marcador por familia (B5.8.2)
        roles_m = E0.clasificar_paginas(paginas, marcadores_b582=True)
        res_m = E0.parsear_cuerpo(ident, pdf.name, paginas, roles_m,
                                  marcadores_b582=True)
        chunks_m = pipeline(res_m)
        if chunks_m:
            res, chunks, roles, marcadores = res_m, chunks_m, roles_m, True
        else:
            # ---- etapa 3: modo sin raíz (B5.8.1) sobre la clasificación de
            # marcadores (con variantes de índice reconocidas, las páginas de
            # índice quedan FUERA del parseo de espina)
            marcadores = roles_m != roles_v
            roles = E0.roles_para_modo_sin_raiz(paginas, roles_m)
            res = E0.parsear_cuerpo(ident, pdf.name, paginas, roles,
                                    modo_sin_raiz=True)
            chunks = pipeline(res)

    indice = E0.parsear_indice(paginas, roles, marcadores_b582=marcadores)
    chunks, rep_sub = correr_e0.subdividir_unidades_grandes(chunks)
    div = E0.divergencias_indice_cuerpo(res, indice)
    cob = E0.verificar_cobertura(res)
    salud = health_check_to(pdf, to=ident)

    d = SALIDA / ident
    d.mkdir(parents=True, exist_ok=True)
    esc = lambda n, o: (d / f"{n}_{ident}.json").write_text(  # noqa: E731
        json.dumps(o, ensure_ascii=False, indent=1), encoding="utf-8")
    esc("estructura", E0.serializar_estructura(res))
    esc("indice", indice)
    esc("chunks", chunks)
    esc("divergencias", div)
    esc("cobertura", cob)
    esc("correcciones", {
        "reasignaciones_continuidad": res.reasignaciones_continuidad,
        "fronteras_intra_palabra": res.correccion_fronteras,
    })
    if rep_sub["particiones"] or rep_sub["no_particionables"]:
        esc("sub_chunking", rep_sub)
    esc("healthcheck", salud)

    terminales = [c for c in chunks if c["tipo"] != "mini_chunk"]
    raices = [s for s in res.secciones if not (s.sintetica and s.numero == "0")]
    motivos = collections.Counter(r["motivo"].split("_vs_")[0]
                                  for r in res.rechazos_header)
    return {
        "archivo": pdf.name,
        "paginas": len(paginas),
        "modo_lectura": res.modo_lectura,
        "activado_por_cero_unidades": activado,
        "marcadores_b582": marcadores,
        "roles_pagina": {r: roles.count(r) for r in sorted(set(roles))},
        "raices_de_lectura": len(raices),
        "raices_sinteticas": sum(1 for s in raices if s.sintetica),
        "secciones_por_numero": [s.numero for s in raices],
        "preambulo": any(s.sintetica and s.numero == "0" for s in res.secciones),
        "chunks_terminales": len(terminales),
        "mini_chunks": len(chunks) - len(terminales),
        "unidades_extraccion": len(chunks),
        "sub_chunking": {"particiones": len(rep_sub["particiones"]),
                         "no_particionables": len(rep_sub["no_particionables"])},
        "rechazos_header": len(res.rechazos_header),
        "rechazos_por_motivo": dict(motivos.most_common(8)),
        "saltos_numeracion": len(res.saltos_numeracion),
        "cobertura_exacta": cob["cobertura_exacta"],
        "healthcheck_veredicto": salud["veredicto"],
        "healthcheck_modo": salud["modo_lectura"],
        "rinde": bool(chunks) and len(raices) > 0,
        "segundos": round(time.time() - t0, 1),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo", help="ids separados por coma (default: objetivo + control)")
    args = ap.parse_args()

    objetivo = tos_objetivo()
    universo = objetivo + [t for t in CONTROL_EXTRA if t not in objetivo]
    if args.solo:
        universo = [t for t in universo if t in set(args.solo.split(","))]
    print(f"objetivo B5.8.2 (recomputado del censo): {len(objetivo)} TOs "
          f"+ control {CONTROL_EXTRA}", flush=True)

    conteos_path = SALIDA / "conteos_b582.json"
    conteos = (json.loads(conteos_path.read_text(encoding="utf-8"))
               if conteos_path.exists() else {})
    for i, ident in enumerate(universo, 1):
        if ident in conteos:
            continue
        c = correr_to(ident)
        conteos[ident] = c
        conteos_path.write_text(json.dumps(conteos, ensure_ascii=False, indent=1),
                                encoding="utf-8")
        print(f"[{i:2d}/{len(universo)}] {ident:10s} modo={c['modo_lectura']:10s} "
              f"raices={c['raices_de_lectura']:3d} unid={c['unidades_extraccion']:4d} "
              f"rinde={'SI' if c['rinde'] else 'NO'} "
              f"salud={c['healthcheck_veredicto'] if c['healthcheck_veredicto'] != 'sano' else 'sano'} "
              f"({c['segundos']}s)", flush=True)

    rinden = sorted(t for t in conteos if conteos[t]["rinde"])
    print(f"\nrinden {len(rinden)}/{len(conteos)}; consolidado -> {conteos_path}")


if __name__ == "__main__":
    main()
