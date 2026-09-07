#!/usr/bin/env python3
"""B5.8.4 — corrida de partición final sobre los 152 TOs del corpus de
escalado con el código commiteado en HEAD, SIN reglas nuevas: escalera
completa vigente → marcadores (B5.8.2) → sin raíz (B5.8.1) — exactamente la
de `correr_b582.py` / `healthcheck_e0.health_check_to` — más el parser de
tablas (`e0_tablas.py`, B5.8.3) sobre los TOs que el criterio sellado de
B5.8.3 indica (familia tabular d/d_dominante del censo B5.8.0 ∪ TOs con
páginas `ficha_registro` declaradas por la corrida B5.8.1).

Health-check por TO para los 152 (restricción 3 del diseño B5.8 §2 lo exige
para todo candidato a «reconocido»; correrlo también sobre los candidatos a
NO segmentable produce la evidencia de su declaración — tarea 3.e del
mandato). Universo = los 152 PDFs de `escalado_prep/pdfs/` (solo lectura),
verificado contra censo_84.json ∪ digeribles de
`veredictos_generalizacion.json`.

Cero LLM, USD 0. Salidas (por TO, en ../<to>/): estructura, indice, chunks,
divergencias, cobertura, correcciones, sub_chunking (si aplica), healthcheck
y — en los TOs del objetivo tabular — tablas y resumen (formato de B5.8.3).
Consolidado: ../conteos_b584.json (reanudable: un TO ya presente no se
re-corre).

Uso (desde cualquier cwd):
    python3 data/experiment/segmentacion_84/b584_particion/code/correr_b584.py [--solo TO1,TO2]
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
SEG = REPO / "data/experiment/segmentacion_84"
CENSO = SEG / "censo_84.json"
CONTEOS_B581 = SEG / "b581_sin_raiz/conteos_b581.json"
VEREDICTOS = PREP / "veredictos_generalizacion.json"
SALIDA = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(E0_DIR))
import correr_e0  # noqa: E402  (solo subdividir_unidades_grandes; no se edita)
import e0_lib as E0  # noqa: E402
import e0_tablas as T  # noqa: E402
from healthcheck_e0 import health_check_to  # noqa: E402


def universo_152() -> list[str]:
    """Los 152 TOs del corpus de escalado, verificados: stems de los PDFs ==
    censo B5.8.0 (84) ∪ digeribles (68). Regla i: recomputado, no transcripto."""
    stems = sorted(p.stem for p in (PREP / "pdfs").glob("*.pdf"))
    censo = set(json.load(open(CENSO, encoding="utf-8")))
    ver = json.load(open(VEREDICTOS, encoding="utf-8"))["por_to"]
    digeribles = {t for t, d in ver.items() if d["veredicto"] == "digerible"}
    assert len(stems) == 152, f"{len(stems)} PDFs, no 152"
    assert set(stems) == censo | digeribles, "stems ≠ censo ∪ digeribles"
    assert not (censo & digeribles), "censo y digeribles no son disjuntos"
    return stems


def objetivo_tabular() -> list[str]:
    """El objetivo del parser de tablas, con el criterio sellado de B5.8.3
    (correr_b583.tos_objetivo): familia tabular d/d_dominante del censo ∪
    TOs con roles_pagina.ficha_registro > 0 en conteos_b581.json."""
    censo = json.load(open(CENSO, encoding="utf-8"))
    de_censo = {t for t, d in censo.items()
                if set(d.get("secundarias", [])) & {"d", "d_dominante"}}
    b581 = json.load(open(CONTEOS_B581, encoding="utf-8"))
    de_b581 = {t for t, d in b581.items()
               if d.get("roles_pagina", {}).get("ficha_registro", 0) > 0}
    return sorted(de_censo | de_b581)


def correr_tablas(ident: str, pdf: Path) -> dict:
    """Parser de tablas sobre un TO del objetivo, artefactos con el formato
    de B5.8.3 (tablas_<to>.json completo + resumen_<to>.json)."""
    t0 = time.time()
    res = T.parsear_to(pdf, ident)
    segundos = round(time.time() - t0, 1)

    d = SALIDA / ident
    d.mkdir(parents=True, exist_ok=True)
    (d / f"tablas_{ident}.json").write_text(
        json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")

    declaradas = [{"id": t["id"], "causas": t["causas"],
                   "pagina": t["segmentos"][0]["pagina"],
                   "pct_perdida_max": t["declaraciones"]["pct_perdida_max"]}
                  for t in res["tablas_logicas"] if t["estado"] == "declarada"]
    resumen = {
        "to": ident,
        "archivo": res["archivo"],
        "paginas": res["paginas"],
        **res["conteos"],
        "declaradas_detalle": declaradas,
        "costuras_candidatas": res["costuras_candidatas"],
        "descartadas_por_regla": res["descartadas_por_regla"]["conteos"],
        "paginas_con_tabla": sorted({s["pagina"] for t in res["tablas_logicas"]
                                     for s in t["segmentos"]}),
        "segundos": segundos,
    }
    (d / f"resumen_{ident}.json").write_text(
        json.dumps(resumen, ensure_ascii=False, indent=1), encoding="utf-8")
    return resumen


def correr_to(ident: str, con_tablas: bool) -> dict:
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
            # marcadores (idéntica a la histórica cuando roles_m == roles_v)
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

    tabular = correr_tablas(ident, pdf) if con_tablas else None

    terminales = [c for c in chunks if c["tipo"] != "mini_chunk"]
    raices = [s for s in res.secciones if not (s.sintetica and s.numero == "0")]
    motivos = collections.Counter(r["motivo"].split("_vs_")[0]
                                  for r in res.rechazos_header)
    avisos = collections.Counter(a["tipo"] for a in res.avisos)
    conteo = {
        "archivo": pdf.name,
        "paginas": len(paginas),
        "modo_lectura": res.modo_lectura,
        "activado_por_cero_unidades": activado,
        "marcadores_b582": marcadores,
        "roles_pagina": {r: roles.count(r) for r in sorted(set(roles))},
        "raices_de_lectura": len(raices),
        "raices_sinteticas": sum(1 for s in raices if s.sintetica),
        "preambulo": any(s.sintetica and s.numero == "0" for s in res.secciones),
        "chunks_terminales": len(terminales),
        "mini_chunks": len(chunks) - len(terminales),
        "unidades_extraccion": len(chunks),
        "sub_chunking": {"particiones": len(rep_sub["particiones"]),
                         "no_particionables": len(rep_sub["no_particionables"])},
        "rechazos_header": len(res.rechazos_header),
        "rechazos_por_motivo": dict(motivos.most_common(8)),
        "avisos": len(res.avisos),
        "avisos_por_tipo": dict(avisos.most_common(8)),
        "saltos_numeracion": len(res.saltos_numeracion),
        "anunciado_sin_cuerpo": len(div["anunciado_sin_cuerpo"]),
        "entradas_indice": len(indice),
        "cobertura_exacta": cob["cobertura_exacta"],
        "healthcheck_veredicto": salud["veredicto"],
        "healthcheck_modo": salud["modo_lectura"],
        "rinde": bool(chunks) and len(raices) > 0,
        "segundos": round(time.time() - t0, 1),
    }
    if tabular is not None:
        conteo["tabular"] = {
            "tablas_logicas": tabular["tablas_logicas"],
            "parseadas": tabular["parseadas"],
            "declaradas": tabular["declaradas"],
            "segmentos": tabular["segmentos"],
            "filas_total": tabular["filas_total"],
            "paginas_con_tabla": len(tabular["paginas_con_tabla"]),
            "rinde_tabular": tabular["rinde"],
        }
    return conteo


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo", help="ids separados por coma (default: los 152)")
    args = ap.parse_args()

    universo = universo_152()
    tabulares = set(objetivo_tabular())
    print(f"universo: {len(universo)} TOs; objetivo tabular (criterio B5.8.3 "
          f"recomputado): {len(tabulares)}", flush=True)
    if args.solo:
        universo = [t for t in universo if t in set(args.solo.split(","))]

    conteos_path = SALIDA / "conteos_b584.json"
    conteos = (json.loads(conteos_path.read_text(encoding="utf-8"))
               if conteos_path.exists() else {})
    for i, ident in enumerate(universo, 1):
        if ident in conteos:
            continue
        c = correr_to(ident, con_tablas=ident in tabulares)
        conteos[ident] = c
        conteos_path.write_text(json.dumps(conteos, ensure_ascii=False, indent=1),
                                encoding="utf-8")
        salud = c["healthcheck_veredicto"]
        print(f"[{i:3d}/{len(universo)}] {ident:16s} modo={c['modo_lectura']:10s} "
              f"raices={c['raices_de_lectura']:3d} unid={c['unidades_extraccion']:4d} "
              f"rinde={'SI' if c['rinde'] else 'NO'} "
              f"salud={'sano' if salud == 'sano' else ','.join(salud)} "
              f"({c['segundos']}s)", flush=True)

    rinden = sorted(t for t in conteos if conteos[t]["rinde"])
    print(f"\nrinden {len(rinden)}/{len(conteos)}; consolidado -> {conteos_path}")


if __name__ == "__main__":
    main()
