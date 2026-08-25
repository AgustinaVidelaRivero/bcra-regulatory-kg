"""
selftest_nofuga_r1.py — Selftest NO-FUGA del worksheet ciego de U-B1.8 ($0),
OBLIGATORIO antes de entregar (autorización del freno 3; molde
ev2_adjudicacion/code/selftest_nofuga.py).

Verifica sobre los archivos PUBLICABLES (worksheet_adjudicacion_r1.{json,md} y
censo_worksheet_r1_ciego.md), como TEXTO plano:
  1. 0 marcadores de grafo/label/rep/veredicto/fragmentos del juez e ids
     EV2R1- / EV2E1- / EV2F- (lista del molde + los propios de la unidad);
  2. 0 apariciones de los 112 SUFIJOS opacos (los 10 hex de los 40 EV2R1- y
     los 72 EV2E1-, buscados SIN prefijo: un sufijo solo también fuga);
  3. 0 apariciones de los 40 ids de pregunta (EV2F-001..040);
  4. 0 sha256 de respuestas (ni completos ni sus primeros 12 hex);
  5. estructura: cada ficha del JSON expone SOLO las claves ciegas
     (n, id_ficha, to, to_nombre, ancla, pregunta, respuesta, criterios,
     observaciones) y cada criterio (indice, criterio, cita_textual,
     veredicto=None);
  6. consistencia interna: ids ADJ1- únicos, numeración 1..N, criterios
     por ficha == los del gold de su pregunta (vía tabla SOLO_MESA);
  7. PROVOCACIÓN: inyectar un marcador y un sufijo opaco en una copia del
     worksheet debe disparar la detección (el detector funciona).

Uso:  .venv/bin/python -B data/experiment/ev2_r1/code/selftest_nofuga_r1.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_r1 as cr                      # noqa: E402
import worksheet_r1 as wr                  # noqa: E402

_checks = []


def check(nombre, cond):
    _checks.append((nombre, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {nombre}")


# Marcadores del molde (comun_adj.MARCADORES_WORKSHEET) + propios de la unidad.
MARCADORES = [
    "ev2_base_v2", "ev2_base_v3", "ev2_base_run3", "reensamblado_v3", "grafo_v2",
    "run_3_ppf_core", "kg_path", "kg_sha256", "graph_fingerprint", "\"grafo\"",
    "'grafo'", "26fac8b49f6c08c1", "run3", "\"label\"", "ev2_enc_",
    "EV2R-", "EV2E-", "EV2F-", "EV2R1-", "EV2E1-",
    "\"rep\"", "\"veredicto_juez", "\"modales", "\"fragmento", "fragmentos_reps",
    "requiere_adjudicacion", "\"final", "id_opaco", "sha256", "\"origen",
    "heredado_base", "s7_pendiente", "muestra_correcto", "muestra_parcial",
    "\"id_pregunta\"", "SOLO_MESA", "veredictos_reps", "ids_reps",
    "ev2_r1_base", "ev2_r1_enc", "ev2_r1_eval", "salida_r1", "0226e947",
    "parcial_disparado", "auditoria_correcto",
]

# Subconjunto de IDENTIDAD para el censo ciego: el censo publica POR DISEÑO el
# resumen de población (orígenes, n de pares a adjudicar — igual que el censo
# del molde), pero jamás identidad de grafo/label/corrida ni ids/shas.
MARCADORES_IDENTIDAD = [
    "ev2_base_v2", "ev2_base_v3", "ev2_base_run3", "reensamblado_v3", "grafo_v2",
    "run_3_ppf_core", "kg_path", "kg_sha256", "graph_fingerprint",
    "26fac8b49f6c08c1", "run3", "ev2_enc_",
    "EV2R-", "EV2E-", "EV2F-", "EV2R1-", "EV2E1-",
    "id_opaco", "sha256", "SOLO_MESA",
    "ev2_r1_base", "ev2_r1_enc", "ev2_r1_eval", "salida_r1", "0226e947",
]

CLAVES_FICHA = {"n", "id_ficha", "to", "to_nombre", "ancla", "pregunta",
                "respuesta", "criterios", "observaciones"}
CLAVES_CRITERIO = {"indice", "criterio", "cita_textual", "veredicto"}


def fugas_en(texto: str, sufijos: list[str], qids: list[str],
             shas: list[str], marcadores: list[str] = MARCADORES) -> list[str]:
    out = [f"marcador:{m}" for m in marcadores if m in texto]
    out += [f"sufijo_opaco:{s}" for s in sufijos if s in texto]
    out += [f"id_pregunta:{q}" for q in qids if q in texto]
    out += [f"sha_respuesta:{s[:12]}…" for s in shas
            if s in texto or s[:12] in texto]
    return out


def main() -> int:
    print("== SELFTEST NO-FUGA del worksheet de r1 (U-B1.8, $0) ==")
    tabla = json.loads(wr.TABLA_FICHAS.read_text(encoding="utf-8"))
    base_tab = json.loads((cr.DESANON_DIR / "tabla_id_opaco_r1_SOLO_MESA.json")
                          .read_text(encoding="utf-8"))
    enc_tab = json.loads((cr.DESANON_DIR / "tabla_id_opaco_s7_r1_SOLO_MESA.json")
                         .read_text(encoding="utf-8"))
    sufijos = [f["id_opaco"].split("-", 1)[1] for f in base_tab["filas"]] \
        + [f["id_opaco"].split("-", 1)[1] for f in enc_tab["filas"]]
    qids = [f"EV2F-{i:03d}" for i in range(1, 41)]
    shas = sorted({f["sha256_respuesta"] for f in base_tab["filas"]}
                  | {f["sha256_respuesta"] for f in enc_tab["filas"]})
    check("universo de control: 112 sufijos opacos (40 base + 72 §7) y 40 qids",
          len(sufijos) == 112 and len(set(sufijos)) == 112 and len(qids) == 40)

    ws = json.loads(wr.WORKSHEET_JSON.read_text(encoding="utf-8"))
    publicables = {p.name: p.read_text(encoding="utf-8")
                   for p in (wr.WORKSHEET_JSON, wr.WORKSHEET_MD, wr.CENSO_CIEGO)}

    # 1–4) fugas por texto: lista completa en el worksheet; identidad en el
    # censo (que publica por diseño el resumen de población, como el molde)
    for nombre, texto in publicables.items():
        marc = MARCADORES_IDENTIDAD if nombre == wr.CENSO_CIEGO.name else MARCADORES
        fugas = fugas_en(texto, sufijos, qids, shas, marc)
        etiqueta = "identidad" if marc is MARCADORES_IDENTIDAD else "lista completa"
        check(f"{nombre}: 0 fugas ({etiqueta} + sufijos + qids + shas)", not fugas)
        if fugas:
            print(f"      -> {fugas[:8]}")

    # 5) estructura ciega del JSON
    ok_fichas = all(set(f) == CLAVES_FICHA for f in ws["fichas"])
    ok_crits = all(set(c) == CLAVES_CRITERIO and c["veredicto"] is None
                   for f in ws["fichas"] for c in f["criterios"])
    check("estructura: fichas solo con claves ciegas y veredictos en blanco",
          ok_fichas and ok_crits)

    # 6) consistencia interna contra la tabla SOLO_MESA
    mesa = {f["id_ficha"]: f for f in tabla["fichas"]}
    ids = [f["id_ficha"] for f in ws["fichas"]]
    check("ids ADJ1- únicos y numeración 1..N",
          all(i.startswith("ADJ1-") for i in ids) and len(set(ids)) == len(ids)
          and [f["n"] for f in ws["fichas"]] == list(range(1, len(ids) + 1)))
    check("cada ficha del worksheet existe en la tabla SOLO_MESA con el mismo n",
          all(f["id_ficha"] in mesa and mesa[f["id_ficha"]]["n"] == f["n"]
              for f in ws["fichas"]))
    check("criterios por ficha == n_criterios de su pregunta (tabla SOLO_MESA)",
          all(len(f["criterios"]) == mesa[f["id_ficha"]]["n_criterios"]
              for f in ws["fichas"]))
    check("respuesta de cada ficha == sha de la tabla SOLO_MESA",
          all(cr.sha256_texto(f["respuesta"]) == mesa[f["id_ficha"]]["sha256_respuesta"]
              for f in ws["fichas"]))

    # 7) PROVOCACIÓN: el detector reacciona
    sucio = publicables["worksheet_adjudicacion_r1.md"] + "\nEV2R1-deadbeef00"
    check("provocación 1: marcador EV2R1- inyectado detectado",
          any("marcador:EV2R1-" in x for x in fugas_en(sucio, sufijos, qids, shas)))
    sucio2 = publicables["worksheet_adjudicacion_r1.md"] + "\n" + sufijos[0]
    check("provocación 2: sufijo opaco solo (sin prefijo) detectado",
          any(x == f"sufijo_opaco:{sufijos[0]}"
              for x in fugas_en(sucio2, sufijos, qids, shas)))
    sucio3 = publicables["censo_worksheet_r1_ciego.md"] + "\n" + qids[0]
    check("provocación 3: id de pregunta inyectado detectado",
          any(x == f"id_pregunta:{qids[0]}"
              for x in fugas_en(sucio3, sufijos, qids, shas)))

    passed = sum(ok for _, ok in _checks)
    print(f"\n  {passed}/{len(_checks)} checks OK")
    print("  RESULTADO:", "PASS" if passed == len(_checks) else "FAIL")
    return 0 if passed == len(_checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
