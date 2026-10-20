"""
unidades_mismo_camino_tramo2.py — B6.1, tanda final, T2: qué unidades del tramo 2 pueden fallar como
`ri_transpa::Sbloque1::chapeau_seccion` (identificacion_error_ri_transpa.json). USD 0, sin API. Solo lee la E0 de la tanda final, el
manifiesto, el censo de T1 y la identificación; no lee ninguna salida del runner. Escribe --out.

El camino del error: el primer intento no corta en 8.192 y sale mal formado; los dos reintentos por forma van con el mismo max_tokens
(8.192), porque el techo de corte solo se usa si el primer intento cortó (runner_corpus.py, `kwargs_forma`), y si cortan, la unidad
queda con `salida_mal_formada_tras_reintento`: ese camino no escala el max_tokens ni parte la unidad. Para fallar así, una unidad
tiene que poder sacar más de 8.192 tokens en un reintento por forma. Con las razones de salida por carácter del censo de T1
(`reext_t0/freno_t2.md:12`: la mediana 1,1582 y la p90 1,5051 tokens por carácter propio), eso es más de 8.192 / 1,5051 = 5.443
caracteres propios con la p90 y más de 8.192 / 1,1582 = 7.073 con la mediana. La lista es de las unidades del tramo 2 sobre el umbral
de la p90 (el censo de T1 con el umbral del primer intento, y no el del reintento), con su tipo, si particionar_por_corte las parte y
si estaban en el censo de T1 (sección 6, sobre los 10.886 caracteres). Es una lista de exposición: para fallar, además, el primer
intento tiene que salir mal formado sin cortar.
Uso: <repo>/.venv/bin/python -B unidades_mismo_camino_tramo2.py --repo <raíz> --out <json>
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

sys.dont_write_bytecode = True
MAN = "data/experiment/reextraccion_v2/manifiestos/tanda_final_98tos_r2b.json"
E0 = "data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b"
CENSO = "data/experiment/tanda_final/t1/seco/censo_unidades_grandes_t1.json"
IDENT = "data/experiment/tanda_final/t2/identificacion_error_ri_transpa/identificacion_error_ri_transpa.json"
MAX_PRIMER, RAZON_MEDIANA, RAZON_P90 = 8192, 1.1582, 1.5051


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    r = a.repo.resolve()
    sys.path.insert(0, str(r / "data/experiment/reextraccion_v2/e0_chunking"))
    import correr_e0                                         # noqa: PLC0415
    man = json.loads((r / MAN).read_text(encoding="utf-8"))
    tramo1, tramo2 = man["orden_corrida"][:30], man["orden_corrida"][30:]
    censo = {d["chunk_id"]: d for d in json.loads((r / CENSO).read_text(encoding="utf-8"))["censo"]}
    ident = json.loads((r / IDENT).read_text(encoding="utf-8"))
    u_p90, u_med = MAX_PRIMER / RAZON_P90, MAX_PRIMER / RAZON_MEDIANA
    filas, total = [], {}
    for tramo, tos in (("tramo_1", tramo1), ("tramo_2", tramo2)):
        n = 0
        for to in tos:
            for c in json.loads((r / E0 / f"chunks_{to}.json").read_text(encoding="utf-8")):
                n += 1
                if c["chars_propio"] <= u_p90:
                    continue
                partes, informe = correr_e0.particionar_por_corte(c)
                filas.append({"tramo": tramo, "to": to, "unidad": c["id"], "tipo": c["tipo"], "chars_propio": c["chars_propio"],
                              "sobre_el_umbral_de_la_mediana": c["chars_propio"] > u_med,
                              "se_parte": partes is not None, "motivo_si_no_se_parte": None if partes else informe.get("motivo"),
                              "bloques_tabla": informe.get("bloques_tabla"),
                              "en_el_censo_de_T1": c["id"] in censo,
                              "mecanismo_en_el_censo_de_T1": censo[c["id"]]["mecanismo"] if c["id"] in censo else None})
        total[tramo] = n
    filas.sort(key=lambda f: (f["tramo"], -f["chars_propio"]))
    t2 = [f for f in filas if f["tramo"] == "tramo_2"]
    t1 = [f for f in filas if f["tramo"] == "tramo_1"]
    res = {"umbral_p90_chars": round(u_p90, 1), "umbral_mediana_chars": round(u_med, 1),
           "la_unidad_que_fallo": {k: ident[k] for k in ("unidad", "error")} | {"chars_propio": ident["caracteres"]["chars_propio"],
                                                                                "tipo": ident["tipo_unidad"]},
           "unidades": total,
           "tramo_2": {"expuestas_p90": len(t2), "expuestas_mediana": sum(f["sobre_el_umbral_de_la_mediana"] for f in t2),
                       "por_tipo": dict(Counter(f["tipo"] for f in t2)),
                       "mini_chunk_con_tabla": [f["unidad"] for f in t2 if f["tipo"] == "mini_chunk" and f["bloques_tabla"]],
                       "en_el_censo_de_T1": [f["unidad"] for f in t2 if f["en_el_censo_de_T1"]],
                       "por_to": dict(Counter(f["to"] for f in t2))},
           "tramo_1_para_comparar": {"expuestas_p90": len(t1), "expuestas_mediana": sum(f["sobre_el_umbral_de_la_mediana"] for f in t1),
                                     "fallo_una": ident["unidad"] in {f["unidad"] for f in t1}},
           "filas": filas}
    a.out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in res.items() if k != "filas"}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
