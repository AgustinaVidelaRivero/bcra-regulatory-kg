"""Recomputo de las cifras de PR-4 tras revisar los 11 CONCORDANTE y muestrear
15 de los 42 SILENCIO CONCORDANTE. Sin API. Uso: python3 recomputo_concordantes.py
"""
from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import comun_coba as C  # noqa: E402

SELLOS = {
    "criterio_destinatario.md":
        "f5066c12a906b2e3720e2b62d1cb9db2cb45bdcfc91bb91d46c77d3ab843204a",
    "adenda_criterio_concordantes.md":
        "b610151c47d27fc7c579b584ffd79588f62ff725c4c860b1aa202c555df9960a",
    "declaracion_censo_silencios.md":
        "7cc0ac9a35dcbfa5e0f01c02019cc32fd83b1e5ec579e6c45e541e1ee9ea7abb",
}


def main() -> int:
    for nombre, esperado in SELLOS.items():
        sha = hashlib.sha256((C.UNIDAD / nombre).read_bytes()).hexdigest()
        assert sha == esperado, f"{nombre} cambio: {sha}"

    rev = json.loads((C.UNIDAD / "revision_concordantes.json").read_text(encoding="utf-8"))
    conc = Counter(x["clase"] for x in rev["concordantes"])
    sil = rev["muestra_silencios"]["casos"]
    fn = sum(1 for x in sil if x["clase"] == "A")   # falso negativo de la marca
    n_sil, N_SIL = len(sil), 42
    assert n_sil == N_SIL, f"el censo debe cubrir las 42, hay {n_sil}"
    por_to_sil: dict[str, dict] = {}
    for x in sil:
        to = x["chunk_id"].split("::")[0]
        e = por_to_sil.setdefault(to, {"silencios": 0, "falsos_negativos": 0})
        e["silencios"] += 1
        e["falsos_negativos"] += (x["clase"] == "A")
    for e in por_to_sil.values():
        e["tasa"] = round(e["falsos_negativos"] / e["silencios"], 3)

    k = conc["B"]                       # unidades CONCORDANTE que resultan (B)
    dest_antes, emit_antes = 17, 13
    dest, emit = dest_antes - k, emit_antes - k

    aristas = [a for x in rev["concordantes"]
               for a in (x.get("aristas_que_se_retiran")
                         or ([x["arista_que_se_retira"]] if x.get("arista_que_se_retira") else []))]

    # censo completo: los falsos negativos son un CONTEO, no una estimacion
    dest_final = dest + fn
    emit_final = emit

    out = {
        "_sellos_verificados": SELLOS,
        "a_clasificacion_de_los_11": {
            "A_destinatario_y_arista_coinciden": conc["A"],
            "C_inferencia_legitima": conc["C"],
            "B_no_hay_destinatario": conc["B"],
            "total": sum(conc.values()),
            "nota": "la adenda no previo (C) para los CONCORDANTE; se declara "
                    "como defecto propio en el reporte",
        },
        "b_aristas_que_se_retiran": {
            "cantidad": len(aristas), "lista": aristas,
            "de_unidades": sorted({x["chunk_id"] for x in rev["concordantes"]
                                   if x.get("aristas_que_se_retiran")
                                   or x.get("arista_que_se_retira")}),
            "advertencia": "esta unidad NO retira nada: lista lo que se retira. "
                           "El ingreso es acto del ensamblado de la tanda",
        },
        "c_recomputo": {
            "k_unidades_B": k,
            "destinatarios_identificados": f"{dest_antes} - {k} = {dest}",
            "piso_recalculado": f"{dest}/77 = {dest/77:.1%}",
            "unidades_que_emiten_y_quedan": f"{emit_antes} - {k} = {emit}",
            "emitido": f"{emit}/77 = {emit/77:.1%}",
            "recuperacion": f"{emit}/{dest} = {emit/dest:.1%}",
            "antes_de_esta_revision": "13/17 = 76,5 %",
        },
        "d_censo_de_silencios": {
            "_estado": "CENSO de las 42, no muestra: la de 15 quedo SUPERSEDED "
                       "por sesgo de composicion (chunk_id ascendente es orden "
                       "alfabetico por documento y excluia a cinco de los nueve)",
            "leidos": n_sil, "de": N_SIL,
            "falsos_negativos": fn,
            "tasa_agregada": f"{fn}/{N_SIL} = {fn/N_SIL:.1%}",
            "por_documento": dict(sorted(por_to_sil.items())),
            "documentos_que_la_muestra_excluia": ["ri_pfmipyme", "ri_pscpp",
                                                  "ri_pspii", "ri_rem", "ri_tii"],
            "los_dos_falsos_negativos_estan_en": ["ri_pspii", "ri_rem"],
            "nota": "los dos caen en documentos que la muestra de 15 excluia "
                    "por construccion: el sesgo era real y mordio donde se "
                    "anticipo",
        },
        "e_recomputo_final": {
            "caso_de_la_declaracion": "Caso 2 — uno o mas (A)",
            "j_falsos_negativos": fn,
            "destinatarios_identificados": f"{dest} + {fn} = {dest_final}",
            "piso_final": f"{dest_final}/77 = {dest_final/77:.1%}",
            "emitido": f"{emit_final}/77 = {emit_final/77:.1%}",
            "recuperacion": f"{emit_final}/{dest_final} = {emit_final/dest_final:.1%}",
            "omisiones_del_extractor": f"{dest_final - emit_final} sobre "
                                       f"{dest_final} destinatarios",
            "trayectoria": ["13/17 = 76,5 % (antes de revisar los concordantes)",
                            "12/16 = 75,0 % (tras los 11, k=1)",
                            f"{emit_final}/{dest_final} = "
                            f"{emit_final/dest_final:.1%} (tras el censo de 42)"],
            "ETIQUETA": "MEDICION SOBRE CENSO, con desempate conservador "
                        "declarado que la sesga a la BAJA",
            "por_que_NO_es_cota_superior": {
                "el_denominador_esta_completo": "las 77 unidades del brazo "
                    "prosa estan clasificadas: 11 concordantes + 22 Prioridad 2 "
                    "+ 2 Prioridad 1 + 42 silencios = 77. La razon que si hacia "
                    "cota superior —denominador incompleto— DESAPARECIO con el "
                    "censo",
                "el_desempate_sesga_a_la_BAJA_no_a_la_alta": "retirar por duda "
                    "a un CONCORDANTE lo saca del numerador Y del denominador. "
                    "Si ri_tii::p5.b9 estuviera mal retirado seria 13/19 = "
                    "68,4 % — MAS ALTO que 66,7 %. La regla invertida empuja el "
                    "cociente hacia abajo",
            },
            "intervalo": {
                "extremo_inferior": f"{emit_final}/{dest_final} = "
                                    f"{emit_final/dest_final:.1%}",
                "caso_del_extremo_inferior": "las dos ambiguedades declaradas "
                    "cuentan como destinatarios (lectura vigente)",
                "extremo_superior": f"{emit_final}/{dest_final - 2} = "
                                    f"{emit_final/(dest_final-2):.1%}",
                "caso_del_extremo_superior": "si las DOS ambiguedades "
                    "declaradas entre los cuatro (A) de Prioridad 2 se "
                    "resolvieran al reves y salieran del denominador",
                "los_dos_casos_NOMBRADOS": [
                    "P2.04 · ri_tii::p1.b1 — «…abiertas en la misma entidad o "
                    "proveedor de servicios de pago informante»",
                    "P2.19 · ri_fcem::p1.b3 — «…remitidos a traves de la "
                    "entidad financiera por medio de la cual opere "
                    "habitualmente»",
                ],
                "publicado": f"{emit_final/dest_final:.1%} – "
                             f"{emit_final/(dest_final-2):.1%}",
                "ninguna_cota_abierta": True,
            },
        },
    }
    salida = C.UNIDAD / "recomputo_concordantes.json"
    salida.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n",
                      encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=1))
    print(f"\nescrito: {salida.relative_to(C.REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
