"""
02_sorteo_acta.py — U-TRIP-V, pasos c, d y e: el sorteo, los solapamientos y el acta con su sello, ANTES de abrir ninguna
ficha. Solo usa las claves, los predicados, las procedencias (chunk_id) y el tipo de los extremos; no lee texto.

Sorteo (despacho, punto 4.c):
  - las 100: random.Random(f"{SEMILLA}:{estrato}").sample(sorted(claves del estrato), n_h);
  - el pool de 20, de lo que queda de la población: random.Random(f"{SEMILLA}:pool").sample(sorted(resto), 20);
  - el orden de lectura de las 100: random.Random(f"{SEMILLA}:orden").shuffle(lista ordenada); las 10 primeras son el
    piloto y las demás, nueve lotes de 10 (§3.5).
Solapamientos (no sale ninguna arista por esto):
  - U-MED-DESAMB (enmienda 2, §1): arista de las 100 o del pool, de predicado aplica_a o ejecuta, con el mismo predicado
    que un ítem, el chunk_id del ítem entre sus procedencias y el sujeto del ítem (`resuelto_a`) como su extremo Sujeto
    (destino en aplica_a, fuente en ejecuta). Es la forma de contar «la misma norma como extremo de contenido».
  - U-LECTURA-ACEPTADAS (pre-registro, :41-42): arista cuya procedencia incluye una unidad de la muestra de
    sellos_l0.json (sorteo.muestra), por chunk_id exacto.
Escribe --salida/acta_sorteo_V.json y --salida/sello_sorteo_V.txt (sha256 del acta y hora).
  python3 -I -B 02_sorteo_acta.py --copia <copia> --poblacion <poblacion_V.json> --asignacion <asignacion_V.json>
      --head <sha> --salida <dir>
"""
from __future__ import annotations

import argparse
import json
import random
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun_v as V  # noqa: E402


def sortear(filas: list, asign: dict) -> tuple[dict, list, list]:
    por_estrato: dict[str, list] = {}
    for f in filas:
        por_estrato.setdefault(f[2], []).append(f[0])
    muestra = {h: random.Random(f"{V.SEMILLA}:{h}").sample(sorted(por_estrato[h]), asign[h]) for h in asign}
    en = {k for v in muestra.values() for k in v}
    resto = sorted(f[0] for f in filas if f[0] not in en)
    pool = random.Random(f"{V.SEMILLA}:pool").sample(resto, V.N_POOL)
    orden = sorted(en)
    random.Random(f"{V.SEMILLA}:orden").shuffle(orden)
    return muestra, pool, orden


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--copia", type=Path, required=True)
    ap.add_argument("--poblacion", type=Path, required=True)
    ap.add_argument("--asignacion", type=Path, required=True)
    ap.add_argument("--head", required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()

    pob = json.loads(a.poblacion.read_text(encoding="utf-8"))
    asg = json.loads(a.asignacion.read_text(encoding="utf-8"))
    s_pob = V.sha_archivo(a.poblacion)
    if asg["poblacion_V.json_sha256"] != s_pob or V.sha(V.canon(pob["filas"])) != pob["sha256_lista"]:
        raise SystemExit("la población no da el sha256 que la asignación sella")
    if asg["sha256_lista_poblacion"] != pob["sha256_lista"]:
        raise SystemExit("la asignación no corresponde a esta población")
    kg, s_kg = V.cargar_kg(a.copia)
    if s_kg != pob["grafo"]["sha256"]:
        raise SystemExit("el grafo no es el de la población")
    tipo = {n["id"]: n["type"] for n in kg["nodes"]}
    filas = pob["filas"]
    info = {f[0]: f for f in filas}
    asign = asg["n"]

    hora_sorteo = V.hora()
    if datetime.fromisoformat(hora_sorteo) <= datetime.fromisoformat(asg["hora"]):
        raise SystemExit("la asignación no es anterior al sorteo")
    muestra, pool, orden = sortear(filas, asign)
    m2, p2, o2 = sortear(filas, asign)
    if (m2, p2, o2) != (muestra, pool, orden):
        raise SystemExit("el sorteo no se reproduce en el mismo proceso")
    en = {k for v in muestra.values() for k in v}
    if len(en) != V.N_MUESTRA or set(pool) & en or len(set(pool)) != V.N_POOL:
        raise SystemExit("las 100 y el pool no son 100 y 20 disjuntos")
    lotes = {"piloto": orden[:V.N_PILOTO]}
    for i in range(V.N_LOTES):
        lotes[f"lote_{i + 1:02d}"] = orden[V.N_PILOTO + i * V.TAM_LOTE: V.N_PILOTO + (i + 1) * V.TAM_LOTE]
    refs = {k: f"V{i + 1:03d}" for i, k in enumerate(orden)} | {k: f"P{i + 1:02d}" for i, k in enumerate(pool)}

    # solapamiento con U-MED-DESAMB (enmienda 2, §1)
    s_ins = V.sha_archivo(V.INSUMO_DESAMB)
    if s_ins != V.INSUMO_DESAMB_SHA256:
        raise SystemExit(f"insumo de U-MED-DESAMB con sha256 {s_ins}")
    items = json.loads(V.INSUMO_DESAMB.read_text(encoding="utf-8"))["items"]
    def sujeto_de(k):
        src, pred, tgt = k.split("|")
        return tgt if pred == "aplica_a" else src
    solap_desamb, candidatas_sin_sujeto = [], []
    for k in orden + pool:
        f = info[k]
        if f[1] not in V.PREDICADOS_SUJETO:
            continue
        suj = sujeto_de(k)
        if tipo[suj] != "Sujeto":
            raise SystemExit(f"{k}: el extremo Sujeto no es un Sujeto")
        for it in items:
            if it["predicado"] == f[1] and it["chunk_id"] in f[3]:
                fila = {"ref": refs[k], "clave": k, "en": "muestra" if k in en else "pool", "predicado": f[1],
                        "chunk_id": it["chunk_id"], "item": it["item"], "resuelto_a": it["resuelto_a"],
                        "sujeto_de_la_arista": suj}
                (solap_desamb if it["resuelto_a"] == suj else candidatas_sin_sujeto).append(fila)

    # solapamiento con U-LECTURA-ACEPTADAS (pre-registro, :41-42)
    p_l0 = a.copia / V.SELLOS_L0_REL
    l0 = json.loads(p_l0.read_text(encoding="utf-8"))
    unidades = {m["id"]: e for e, ms in l0["sorteo"]["muestra"].items() for m in ms}
    bases_l0 = {V.base_chunk(u) for u in unidades}
    solap_l0, solo_por_base = [], []
    for k in orden + pool:
        f = info[k]
        exactas = sorted(c for c in f[3] if c in unidades)
        if exactas:
            solap_l0.append({"ref": refs[k], "clave": k, "en": "muestra" if k in en else "pool", "predicado": f[1],
                             "unidades": exactas, "estrato_l0": [unidades[c] for c in exactas]})
        elif any(V.base_chunk(c) in bases_l0 for c in f[3]):
            solo_por_base.append({"ref": refs[k], "clave": k, "chunk_ids": f[3]})

    def det(ks):
        return [{"ref": refs[k], "clave": k, "predicado": info[k][1], "estrato": info[k][2], "chunk_ids": info[k][3],
                 "tos": info[k][4]} for k in ks]

    acta = {
        "unidad": "U-TRIP-V: acta del sorteo de la etapa V (sellada antes de abrir ninguna ficha)",
        "rige": {"preregistro": "docs/preregistro_evaluacion_tripletas.md (firma en 4afbe51, texto firmado sha256 "
                                "8ce611ba…), con sus notas al pie",
                 "enmienda_1": "docs/enmienda1_preregistro_evaluacion_tripletas_2026-10-08_umbrales.md",
                 "enmienda_2": "docs/enmienda2_preregistro_evaluacion_tripletas_2026-10-17_desambiguacion.md "
                               "(firmada en 593e5db2)"},
        "repo": {"head": a.head, "nota": "el despacho nombra 593e5db2; HEAD es a7d00025, un commit después, que agrega "
                 "docs/mandatos/UPREG_B63_preguntas_por_tipo.md y modifica "
                 "docs/registro_decisiones_calidad_y_evaluacion_2026-10-15.md; no toca ningún insumo. Todo se lee con "
                 "los blobs de a7d00025 (salidas/00_control_insumos_*.json)."},
        "grafo": {**pob["grafo"], "nota": "sello vigente al sortear (nota del 15/10/2026 al pie del pre-registro)"},
        "poblacion": {"N": pob["N"], "por_predicado": pob["por_predicado"], "contenido": pob["contenido"],
                      "lista_de_fuera": pob["lista_de_fuera"]["fuera"],
                      "agregados_a_la_lista_de_fuera": pob["lista_de_fuera"]["agregados_a_la_lista_de_fuera"],
                      "diferencia_con_el_texto_firmado": {
                          k: pob["diferencia_con_el_texto_firmado"][k] for k in (
                              "texto_firmado_por_predicado", "recuento_del_texto_firmado_reproduce",
                              "por_predicado_diferencia", "salen", "entran", "salen_por_predicado",
                              "entran_por_predicado", "causas_salen", "causas_entran", "sin_causa_declarada",
                              "fuente_de_las_causas")},
                      "declaracion_N": ("N = 3.967 en el grafo que se mide (66e745f5…), no 3.983 como dice el texto "
                                        "firmado (recuento sobre 2922b72d…, que se reproduce). La diferencia, −16, es "
                                        "del re-sellado único: salen 83 aristas de contenido y entran 67, todas con "
                                        "causa en el diff declarado del re-sellado (el código de U-OMISIONES-COD, "
                                        "grupos G-r, f y f′, y las salidas de R0); 0 sin causa."),
                      "poblacion_V.json_sha256": s_pob, "sha256_lista": pob["sha256_lista"],
                      "sha256_claves": pob["sha256_claves"], "filas_formato": pob["filas_formato"],
                      "como_se_calcula_el_sha256": pob["como_se_calcula_el_sha256"], "filas": filas},
        "asignacion": {k: asg[k] for k in ("hora", "N", "estratos", "regla", "rondas", "redondeo", "n", "suma",
                                           "estratos_sin_muestra", "declaracion_estratos_sin_muestra")},
        "asignacion_V.json_sha256": V.sha_archivo(a.asignacion),
        "sorteo": {
            "semilla": V.SEMILLA,
            "fuente_semilla": "la del despacho; no está escrita en el repo (git log --all -S y grep en docs/ y "
                              "data/experiment/: 0), declarado",
            "metodo": {"muestra": "random.Random(f'{semilla}:{estrato}').sample(sorted(claves del estrato), n_h)",
                       "pool": "random.Random(f'{semilla}:pool').sample(sorted(población menos las 100), 20)",
                       "orden": "lista = sorted(las 100); random.Random(f'{semilla}:orden').shuffle(lista); 10 de "
                                "piloto y nueve lotes de 10"},
            "python": sys.version.split()[0], "hora": hora_sorteo,
            "muestra": {h: det(muestra[h]) for h in asign},
            "sha256_muestra": V.sha(V.canon(muestra)),
            "pool": det(pool), "sha256_pool": V.sha(V.canon(pool)),
            "orden": orden, "sha256_orden": V.sha(V.canon(orden)),
            "lotes": lotes, "sha256_lotes": V.sha(V.canon(lotes)),
            "refs": {"muestra": "V001…V100 por el orden de lectura", "pool": "P01…P20 por el orden del sorteo del pool"},
            "como_se_calcula_el_sha256": "json.dumps(x, ensure_ascii=False, separators=(',', ':')) en UTF-8; muestra "
                                         "= {estrato: [claves en el orden del sorteo]}, pool = [claves en el orden del "
                                         "sorteo], orden = [claves en el orden de lectura], lotes = {lote: [claves]}",
            "muestra_por_predicado": dict(Counter(info[k][1] for k in en)),
            "pool_por_predicado": dict(Counter(info[k][1] for k in pool)),
            "muestra_por_to": dict(Counter(info[k][4][0] for k in en)),
            "pool_por_to": dict(Counter(info[k][4][0] for k in pool)),
            "disjuntos": not (set(pool) & en)},
        "solapamientos": {
            "U-MED-DESAMB": {
                "regla": "enmienda 2, §1: se declara y no se excluye",
                "criterio": "arista de las 100 o del pool, de predicado aplica_a o ejecuta, con el mismo predicado que "
                            "un ítem, el chunk_id del ítem entre sus procedencias y el sujeto del ítem (resuelto_a) "
                            "como su extremo Sujeto (destino en aplica_a, fuente en ejecuta). Es la forma de contar «la "
                            "misma norma como extremo de contenido».",
                "insumo": {"ruta": "insumos/items_U-MED-DESAMB_para_el_solapamiento.json", "sha256": s_ins,
                           "items": len(items)},
                "conteo": len(solap_desamb),
                "conteo_muestra": sum(1 for x in solap_desamb if x["en"] == "muestra"),
                "conteo_pool": sum(1 for x in solap_desamb if x["en"] == "pool"),
                "lista": solap_desamb,
                "informativo_mismo_predicado_y_chunk_con_otro_sujeto": candidatas_sin_sujeto},
            "U-LECTURA-ACEPTADAS": {
                "regla": "pre-registro :41-42: se declara y no se excluye",
                "criterio": "arista de las 100 o del pool cuya procedencia incluye una unidad de la muestra de "
                            "sellos_l0.json (sorteo.muestra, 60 unidades), por chunk_id exacto",
                "insumo": {"ruta": V.SELLOS_L0_REL, "sha256": V.sha_archivo(p_l0), "unidades": len(unidades)},
                "conteo": len(solap_l0),
                "conteo_muestra": sum(1 for x in solap_l0 if x["en"] == "muestra"),
                "conteo_pool": sum(1 for x in solap_l0 if x["en"] == "pool"),
                "lista": solap_l0,
                "informativo_solo_por_la_unidad_base": solo_por_base},
            "ninguna_sale": True},
        "insumos_sha256": {"kg.json": s_kg, "poblacion_V.json": s_pob,
                           "asignacion_V.json": V.sha_archivo(a.asignacion),
                           "sellos_l0.json": V.sha_archivo(p_l0), "items_U-MED-DESAMB": s_ins},
        "codigo_sha256": {p.name: V.sha_archivo(p) for p in sorted(Path(__file__).resolve().parent.glob("*.py"))}}
    s_acta = V.escribir_json(a.salida / "acta_sorteo_V.json", acta)
    hora_sello = V.hora()
    (a.salida / "sello_sorteo_V.txt").write_text(f"{s_acta}  acta_sorteo_V.json\n{hora_sello}\n", encoding="utf-8")

    print(json.dumps({"hora_sorteo": hora_sorteo, "hora_sello": hora_sello, "acta_sorteo_V.json": s_acta,
                      "sha256_muestra": acta["sorteo"]["sha256_muestra"], "sha256_pool": acta["sorteo"]["sha256_pool"],
                      "sha256_orden": acta["sorteo"]["sha256_orden"], "sha256_lotes": acta["sorteo"]["sha256_lotes"],
                      "muestra_por_predicado": acta["sorteo"]["muestra_por_predicado"],
                      "pool_por_predicado": acta["sorteo"]["pool_por_predicado"],
                      "muestra_por_to": acta["sorteo"]["muestra_por_to"], "pool_por_to": acta["sorteo"]["pool_por_to"],
                      "solap_desamb": [len(solap_desamb), acta["solapamientos"]["U-MED-DESAMB"]["conteo_muestra"],
                                       acta["solapamientos"]["U-MED-DESAMB"]["conteo_pool"]],
                      "desamb_informativo_otro_sujeto": len(candidatas_sin_sujeto),
                      "solap_l0": [len(solap_l0), acta["solapamientos"]["U-LECTURA-ACEPTADAS"]["conteo_muestra"],
                                   acta["solapamientos"]["U-LECTURA-ACEPTADAS"]["conteo_pool"]],
                      "l0_informativo_solo_base": len(solo_por_base)}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
