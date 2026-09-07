"""Evaluacion de las DIEZ predicciones del pre-registro v4 sellado + el cruce
2x2 de PR-4 exigido por la autorizacion de gasto.

Sin API: lee `a2_salida/extracciones_a2.jsonl` y mide. Uso: python3 medir_a2.py
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import comun_coba as C  # noqa: E402
import senal_sujeto as SS  # noqa: E402

NORMATIVOS = frozenset({"Operacion", "Restriccion", "Excepcion", "Obligacion",
                        "Potestad", "Condicion", "Definicion"})
RE_PARTIDA = re.compile(r"[a-záéíóúüñ]- [a-záéíóúüñ]")
SALIDA = C.UNIDAD / "a2_salida"


def rinde(fila: dict) -> bool:
    """RINDE = >=1 entidad de tipo normativo (definicion §1 del pre-registro)."""
    return any(e.get("type") in NORMATIVOS for e in fila.get("entidades") or [])


def main() -> int:
    filas = [json.loads(l) for l in
             (SALIDA / "extracciones_a2.jsonl").read_text(encoding="utf-8").splitlines()
             if l.strip()]
    chunks = {c["id"]: c for c in json.loads(
        (C.UNIDAD / "chunks_a2.json").read_text(encoding="utf-8"))}
    pats = SS.formas_de_superficie()
    brazos = {"prosa": [f for f in filas if f.get("brazo") == "prosa"],
              "planilla_ficha": [f for f in filas if f.get("brazo") == "planilla_ficha"]}

    out = {"_meta": {
        "sello_prerregistro_v4":
            "87fae986a8dc5370bef67c65e257409b26653a021f262e007d3348f21657b0ff",
        "unidades_medidas": len(filas),
        "definicion_rinde": ">=1 entidad de tipo normativo (7 tipos); "
                            "TextoOrdenado, Comunicacion y Sujeto no cuentan",
    }, "por_brazo": {}, "PR4_cruce_2x2": {}, "observaciones": {}}

    for nombre, fs in brazos.items():
        n = len(fs)
        ents = [e for f in fs for e in (f.get("entidades") or [])
                if e.get("type") in NORMATIVOS]
        tipos = Counter(e["type"] for e in ents)
        rech = Counter(r["motivo"] for f in fs for r in (f.get("rechazos") or []))
        # PR-1 / PL-1 dicen textual «cero emisiones de TIPO o de PREDICADO
        # fuera de los 9 y los 13». `firma_invalida` NO es eso: sus tipos y su
        # predicado SI estan en el vocabulario y lo que falla es la matriz
        # dominio/rango. Se cuenta aparte, como hallazgo.
        vocab = {m: c for m, c in rech.items()
                 if m in ("tipo_invalido", "predicado_invalido")}
        firmas = {m: c for m, c in rech.items() if m == "firma_invalida"}
        n_rinde = sum(1 for f in fs if rinde(f))
        con_aplica = sum(1 for f in fs
                         if any(r.get("predicate") == "aplica_a"
                                for r in (f.get("relaciones") or [])))
        partida = sum(1 for f in fs for e in (f.get("entidades") or [])
                      if RE_PARTIDA.search(str(e.get("label", ""))))
        out["por_brazo"][nombre] = {
            "unidades": n,
            "rinden": n_rinde,
            "tasa_rinde": round(n_rinde / n, 4) if n else None,
            "entidades_normativas": len(ents),
            "tipos": dict(tipos.most_common()),
            "frac_obligacion": round(tipos["Obligacion"] / len(ents), 4) if ents else None,
            "unidades_con_aplica_a": con_aplica,
            "frac_aplica_a": round(con_aplica / n, 4) if n else None,
            "rechazos_por_motivo": dict(rech.most_common()),
            "rechazos_de_vocabulario_PR1": vocab,
            "rechazos_firma_invalida_NO_es_PR1": firmas,
            "entidades_con_palabra_partida": partida,
            "stop_reason": dict(Counter(f.get("stop_reason") for f in fs)),
            "reintentos_por_corte": sum(1 for f in fs if f.get("reintento_por_corte")),
            "errores": sum(1 for f in fs if f.get("error")),
        }

    # ---- PR-4: cruce 2x2 (TAMIZ, no medicion) ----
    estratos = {"EMISION SIN MENCION LITERAL - PRIORIDAD 1 DE REVISION MANUAL": [],
                "MENCION LITERAL SIN EMISION - PRIORIDAD 2": [],
                "CONCORDANTE": [],
                "SILENCIO CONCORDANTE": []}
    por_to: dict[str, Counter] = {}
    for f in brazos["prosa"]:
        texto = chunks[f["chunk_id"]]["texto"]
        menciona = any(p.search(texto) for p in pats.values())
        emite = any(r.get("predicate") == "aplica_a" for r in (f.get("relaciones") or []))
        if not menciona and emite:
            k = "EMISION SIN MENCION LITERAL - PRIORIDAD 1 DE REVISION MANUAL"
        elif menciona and not emite:
            k = "MENCION LITERAL SIN EMISION - PRIORIDAD 2"
        elif menciona and emite:
            k = "CONCORDANTE"
        else:
            k = "SILENCIO CONCORDANTE"
        estratos[k].append({"chunk_id": f["chunk_id"], "to": f["to"],
                            "texto": texto[:160]})
        por_to.setdefault(f["to"], Counter())[k] += 1

    out["PR4_cruce_2x2"] = {
        "_naturaleza": "ES TAMIZ, NO MEDICION. Ninguna celda es un contador "
                       "limpio. Parte las unidades del brazo prosa en cuatro "
                       "estratos con prioridad de revision; se reporta con "
                       "estos rotulos, no con rotulos de correccion.",
        "_que_testea_la_marca_literal": "COINCIDENCIA LEXICA sobre el texto de "
            "la unidad contra las 70 entradas del catalogo de sujetos del "
            "esquema congelado — NO posicion de destinatario. Es cota inferior: "
            "no resuelve anafora ni sujeto heredado del encabezado, y una "
            "mencion no siempre es el destinatario de la norma. El piso de PR-4 "
            "(42,9 %) esta fijado sobre esta cota, con falsos positivos posibles.",
        "_ninguna_cifra_dispara_retiro": "el principio §1 se aplica sobre casos "
                                         "revisados, no sobre el tamano de un estrato",
        "agregado": {k: len(v) for k, v in estratos.items()},
        "por_to": {t: dict(c) for t, c in sorted(por_to.items())},
        "casos": {k: v for k, v in estratos.items()
                  if k.startswith(("EMISION", "MENCION"))},
    }

    # ---- PR-2 y PR-4 por TO (obligatorio, §4 del pre-registro) ----
    out["PR2_PR4_por_to"] = {}
    for to in sorted({f["to"] for f in brazos["prosa"]}):
        fs = [f for f in brazos["prosa"] if f["to"] == to]
        lit = sum(1 for f in fs
                  if any(p.search(chunks[f["chunk_id"]]["texto"]) for p in pats.values()))
        ap = sum(1 for f in fs if any(r.get("predicate") == "aplica_a"
                                      for r in (f.get("relaciones") or [])))
        out["PR2_PR4_por_to"][to] = {
            "unidades": len(fs),
            "rinden": sum(1 for f in fs if rinde(f)),
            "tasa_rinde": round(sum(1 for f in fs if rinde(f)) / len(fs), 3),
            "con_mencion_literal": lit,
            "tasa_literal_propia": round(lit / len(fs), 3),
            "con_aplica_a": ap,
            "tasa_aplica_a": round(ap / len(fs), 3),
        }

    # ---- observaciones: PL-5 (ri_tii p.3-4) y §5 (ri_pspii p.1) ----
    for nombre, sel in (("PL5_ri_tii_p3_p4",
                         lambda f: f["to"] == "ri_tii" and f["paginas"][0] in (3, 4)),
                        ("obs_ri_pspii_p1",
                         lambda f: f["to"] == "ri_pspii" and f["paginas"][0] == 1)):
        fs = [f for f in filas if sel(f)]
        ents = [e for f in fs for e in (f.get("entidades") or [])
                if e.get("type") in NORMATIVOS]
        out["observaciones"][nombre] = {
            "unidades": len(fs), "rinden": sum(1 for f in fs if rinde(f)),
            "entidades_normativas": len(ents),
            "tipos": dict(Counter(e["type"] for e in ents).most_common()),
        }

    # ---- PL-5: contraste con la lectura tabular sellada sobre ri_tii p.3-4 ----
    sys.path.insert(0, str(C.E0_DIR))
    import e0_tablas as T  # noqa: E402
    r = T.parsear_to(C.PDFS / "ri_tii.pdf", "ri_tii")
    filas_tab = sum(len(s_.get("filas", [])) for t in r["tablas_logicas"]
                    for s_ in t.get("segmentos", []) if s_["pagina"] in (3, 4))
    sel = [f for f in filas if f["to"] == "ri_tii" and f["paginas"][0] in (3, 4)]
    ents_prosa = [e for f in sel for e in (f.get("entidades") or [])
                  if e.get("type") in NORMATIVOS]
    out["PL5_contraste_lecturas"] = {
        "paginas": "ri_tii p.3-4",
        "tablas_logicas_b583": len(r["tablas_logicas"]),
        "filas_de_la_lectura_tabular": filas_tab,
        "unidades_de_prosa": len(sel),
        "entidades_bien_formadas_de_prosa": len(ents_prosa),
        "cumple": len(ents_prosa) < filas_tab,
    }

    # ---- PL-3: candidatos a RX-10, para revision manual ----
    out["PL3_candidatos_rx10"] = [
        {"chunk_id": f["chunk_id"],
         "texto": chunks[f["chunk_id"]]["texto"][:200],
         "labels": [str(e.get("label")) for e in (f.get("entidades") or [])
                    if e.get("type") in NORMATIVOS][:3]}
        for f in brazos["planilla_ficha"] if rinde(f)]

    salida = C.UNIDAD / "medicion_a2.json"
    salida.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n",
                      encoding="utf-8")
    for b, v in out["por_brazo"].items():
        print(f"{b:16s} rinde {v['rinden']}/{v['unidades']} = {v['tasa_rinde']:.1%} · "
              f"Obligacion {v['frac_obligacion']} · aplica_a {v['frac_aplica_a']} · "
              f"vocab fuera de lista {v['rechazos_de_vocabulario_PR1']} · "
              f"firmas invalidas {v['rechazos_firma_invalida_NO_es_PR1']}")
    print("\ncruce 2x2:", json.dumps(out["PR4_cruce_2x2"]["agregado"], ensure_ascii=False))
    print(f"escrito: {salida.relative_to(C.REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
