"""Entregable 5 — conteo exigido por la autora (adenda 2 §3.3):
cuántos elementos tendrían `granularidad_procedencia = pagina` y qué fracción
del recurso representan.

Separa con todas las letras lo MEDIDO de lo PROYECTADO:

  · unidades con procedencia a nivel de página  → MEDICIÓN (esta fase las contó)
  · elementos del grafo con esa granularidad    → PROYECCIÓN NO VERIFICADA
    (nada se extrajo todavía; la tasa elementos/unidad se toma del grafo
    vigente, que corrió con el esquema v2 de 7 tipos sobre chunks de otra
    forma y otro tamaño — los dos supuestos quedan declarados abajo)

Uso:  python3 proyeccion_procedencia.py
"""
from __future__ import annotations

import glob
import json
import statistics as st
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import comun_coba as C  # noqa: E402

# --- anclas MEDIDAS, cada una con el artefacto que la respalda ---
KG_VIGENTE = C.EXPERIMENT / "reextraccion_v2/corpus_v2/salida_r1/kg.json"
E0_DEV = C.EXPERIMENT / "reextraccion_v2/e0_chunking/salida_enm01"
CENSO = C.UNIDAD / "censo_forma.json"


def main() -> int:
    censo = json.loads(CENSO.read_text(encoding="utf-8"))
    particion = json.loads(C.PARTICION.read_text(encoding="utf-8"))
    ag = particion["agregados"]

    # ---- 1. el recurso HOY, recomputado contra particion_152.json ----
    recurso_hoy = sum(v["unidades"] for v in ag.values())
    unid_no_seg = ag["no_segmentable_declarado"]["unidades"]
    ns = {k: v for k, v in particion["por_to"].items()
          if v["clase"] == "no_segmentable_declarado"}
    unid_diez = sum(v["unidades"] for k, v in ns.items() if k in C.DIEZ)
    unid_ref = sum(v["unidades"] for k, v in ns.items() if k in C.REFERENCIA)

    # ---- 2. lo que el bloque A pondría en su lugar (MEDIDO en esta fase) ----
    a = censo["agregados_diez"]
    variantes = {
        "todos_los_bloques": a["bloques_total"],
        "solo_prosa_y_mixta": a["bloques_utiles_prosa_y_mixta"],
        "solo_prosa": a["bloques_por_clase_forma"]["prosa"],
    }

    # ---- 3. tasa elementos/unidad del grafo VIGENTE (ancla de la proyección) ----
    kg = json.loads(KG_VIGENTE.read_text(encoding="utf-8"))
    nodos_con_chunk = sum(1 for n in kg["nodes"]
                          if (n.get("provenance") or {}).get("chunk_id"))
    unidades_dev, largos_dev = 0, []
    for f in sorted(glob.glob(str(E0_DEV / "chunks_*.json"))):
        for c in json.loads(Path(f).read_text(encoding="utf-8")):
            unidades_dev += 1
            if c.get("texto"):
                largos_dev.append(len(c["texto"]))
    tasa = nodos_con_chunk / unidades_dev

    # tamaño comparado (el supuesto que más pesa en la proyección)
    largos_a = []
    for to in C.DIEZ:
        _p, _r, _m, bl, _d = C.leer_documento(to)
        largos_a += [b.n_chars for v in bl.values() for b in v]

    out = {
        "_meta": {
            "unidad": "U-COB-A fase A.1 — entregable 5 (conteo exigido)",
            "advertencia": "las cifras en unidades son MEDICION; las cifras en "
                           "elementos del grafo son PROYECCION NO VERIFICADA",
        },
        "medicion_recurso_hoy": {
            "unidades_totales": recurso_hoy,
            "desglose": {k: v["unidades"] for k, v in ag.items()},
            "comando": "python3 -c \"import json;d=json.load(open('data/experiment/"
                       "segmentacion_84/b584_particion/particion_152.json'));"
                       "print(sum(v['unidades'] for v in d['agregados'].values()))\"",
            "unidades_degeneradas_no_segmentables": unid_no_seg,
            "de_ellas_de_los_diez": unid_diez,
            "de_ellas_de_los_dos_de_referencia": unid_ref,
        },
        "medicion_bloque_a": {
            "documentos": a["documentos"], "paginas": a["paginas"],
            "unidades_por_variante": variantes,
            "paginas_por_clase_forma": a["paginas_por_clase_forma"],
        },
        "medicion_conteo_exigido_en_unidades": {},
        "ancla_de_la_proyeccion": {
            "grafo_vigente": "KG-Reextraido-r1",
            "sha256": "0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a",
            "nodos_con_chunk_id": nodos_con_chunk,
            "unidades_e0_dev": unidades_dev,
            "tasa_nodos_por_unidad": round(tasa, 4),
            "mediana_chars_chunk_dev": st.median(largos_dev),
            "mediana_chars_bloque_A": st.median(largos_a),
            "razon_de_tamano_A_sobre_dev": round(st.median(largos_a) / st.median(largos_dev), 3),
            "supuestos_declarados_NO_VERIFICADOS": [
                "tasa uniforme: se supone que un bloque del bloque A rinde los "
                "mismos elementos que un chunk del corpus de desarrollo; la "
                "mediana de caracteres dice que NO son comparables en tamano",
                "el grafo vigente corrio con el esquema v2 (7 tipos); el "
                "congelado tiene 9, de modo que la tasa es cota inferior",
                "el denominador del recurso escalado en ELEMENTOS no existe: "
                "la extraccion sobre los 152 no corrio (B5.7 pendiente)",
            ],
        },
        "proyeccion_NO_VERIFICADA_en_elementos": {},
    }

    for nombre, n_a in variantes.items():
        total_u = recurso_hoy - unid_diez + n_a
        out["medicion_conteo_exigido_en_unidades"][nombre] = {
            "unidades_con_granularidad_pagina": n_a,
            "unidades_totales_del_recurso": total_u,
            "fraccion": round(n_a / total_u, 4),
            "frase_para_la_tesis": f"{n_a} unidades de {total_u}",
        }
        out["proyeccion_NO_VERIFICADA_en_elementos"][nombre] = {
            "elementos_con_granularidad_pagina": round(n_a * tasa),
            "elementos_totales_proyectados": round(total_u * tasa),
            "fraccion": round(n_a / total_u, 4),
            "marca": "NO VERIFICADA",
        }

    salida = C.UNIDAD / "proyeccion_procedencia.json"
    salida.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n",
                      encoding="utf-8")
    print(f"escrito: {salida.relative_to(C.REPO)}\n")
    print(json.dumps(out["medicion_conteo_exigido_en_unidades"],
                     ensure_ascii=False, indent=1))
    print("\nancla:", json.dumps(
        {k: v for k, v in out["ancla_de_la_proyeccion"].items()
         if k != "supuestos_declarados_NO_VERIFICADOS"},
        ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
