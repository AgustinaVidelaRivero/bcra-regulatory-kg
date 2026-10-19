"""
01_poblacion_asignacion.py — U-TRIP-V, pasos a y b: la población de la etapa V (§3.1) y la asignación por estrato
(§3.2), escrita ANTES del sorteo. No abre ninguna ficha: lee las claves, los predicados y las procedencias (chunk_id) de
las aristas, y el código de la cadena de ensamblado.

Población (§3.1): las aristas del grafo de V cuyo predicado es una de las diez relaciones de contenido del esquema
(`aplica_a` adentro). La lista de fuera es la del texto firmado más todo predicado que la cadena de ensamblado derive;
ninguno de contenido sale. La cadena (resellado_t0/scripts/cadena_rs1.sh, grafo r2b_sincola_desarrollo) es
ensamblar_tanda0.py --manifiesto tanda0_ens_desarrollo_r2b_sincola_rs1.json --entrada salida_r2b --e0-r2
salida_tanda0_r2b --sin-cola; correr_cadena_r2 deriva, por código:
  - el esqueleto (inyectar_esqueleto_v3: RELACIONES_ESQUELETO de schema.py y padre_sugerido de r1_e5_esqueleto);
  - remite_a y referencia (r1_referencias.detectar_y_resolver; PREDICADOS_DERIVADOS de modelos_r2);
  - establecida_en (derivar_establecida_en; PREDICADOS_DERIVADOS_DE_PROCEDENCIA de modelos_r2).
Las aristas de contenido las arma e2_lib.ensamblar_r2 desde las relaciones de E1 (sin rol_fuente); este script lo
controla en el grafo: ninguna arista de contenido lleva rol_fuente.

Clave de una arista: `fuente|predicado|destino`. Si dos aristas comparten clave, o si un id de nodo contiene «|», FRENO.

Asignación (§3.2): proporcional al tamaño del estrato, con un mínimo de 3 por predicado de 30 aristas o más; los de menos
de 30 forman «otros». Método: se fijan en 3 los estratos con mínimo cuya cuota proporcional queda por debajo de 3, y el
resto de la muestra se reparte en proporción entre los demás, repitiendo hasta que ninguno quede por debajo; el redondeo
es por restos mayores (convención del proyecto) y un empate de restos se resuelve con random.Random(f"{SEMILLA}:empate").
«otros» no tiene mínimo (letra del §3.2).

Escribe --salida/poblacion_V.json y --salida/asignacion_V.json.
  python3 -I -B 01_poblacion_asignacion.py --copia <copia> --salida <dir>
"""
from __future__ import annotations

import argparse
import json
import math
import random
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun_v as V  # noqa: E402


def lista_de_fuera(copia: Path, predicados_grafo: set) -> dict:
    """La lista de fuera: la del texto firmado más lo que la cadena derive, con la evidencia leída del código."""
    m = V.constantes_py(copia / V.MODELOS_R2_REL, ("PREDICADOS", "PREDICADOS_SUJETO", "PREDICADOS_DERIVADOS",
                                                   "PREDICADOS_DERIVADOS_DE_PROCEDENCIA", "RELACIONES_ESQUELETO"))
    s = V.constantes_py(copia / V.SCHEMA_REL, ("RELACIONES_ESQUELETO",))
    e5 = V.constantes_py(copia / V.E5_REL, ("REL_PADRE_SUGERIDO",))
    ref = V.constantes_py(copia / V.REF_REL, ("PREDICADO_R2",))
    # literales de `"relation": ...` en el código de la cadena
    literales = {}
    for rel in (V.ENS_REL, V.REF_REL, V.E2_REL):
        txt = (copia / rel).read_text(encoding="utf-8")
        literales[rel] = sorted(set(re.findall(r'"relation":\s*([^,}\n]+)', txt)))
    derivados = {
        "esqueleto (inyectar_esqueleto_v3; schema.RELACIONES_ESQUELETO)": list(s["RELACIONES_ESQUELETO"]),
        "cuarentena de sujetos (inyectar_esqueleto_v3; r1_e5_esqueleto.REL_PADRE_SUGERIDO)": [e5["REL_PADRE_SUGERIDO"]],
        "remisiones (r1_referencias.detectar_y_resolver; modelos_r2.PREDICADOS_DERIVADOS, PREDICADO_R2)":
            sorted(set(m["PREDICADOS_DERIVADOS"]) | {ref["PREDICADO_R2"]}),
        "referencia TextoOrdenado → Comunicacion (r1_referencias, `\"relation\": \"referencia\"`)": ["referencia"],
        "establecida_en por procedencia (derivar_establecida_en; modelos_r2.PREDICADOS_DERIVADOS_DE_PROCEDENCIA)":
            list(m["PREDICADOS_DERIVADOS_DE_PROCEDENCIA"]),
    }
    todos_derivados = sorted({p for v in derivados.values() for p in v})
    esquema_e1 = list(m["PREDICADOS"])
    contenido_esquema = [p for p in esquema_e1 if p not in ("establecida_en", "referencia", "modificada_por")]
    if sorted(contenido_esquema) != sorted(V.CONTENIDO):
        raise SystemExit(f"FRENO: las relaciones de contenido del esquema {contenido_esquema} no son las diez del §3.1")
    choque = sorted(set(todos_derivados) & set(V.CONTENIDO))
    if choque:
        raise SystemExit(f"FRENO: la cadena deriva predicados de contenido: {choque} (ninguno de contenido sale)")
    fuera = sorted(set(V.FUERA_PREREGISTRO) | set(todos_derivados) | (predicados_grafo - set(V.CONTENIDO)))
    return {"esquema_e1_modelos_r2_PREDICADOS": esquema_e1, "contenido_del_esquema": contenido_esquema,
            "derivados_por_la_cadena": derivados, "literales_relation_en_el_codigo": literales,
            "fuera_preregistro": list(V.FUERA_PREREGISTRO),
            "agregados_a_la_lista_de_fuera": sorted(set(fuera) - set(V.FUERA_PREREGISTRO)),
            "fuera": fuera, "predicados_del_grafo_fuera_de_ambas_listas": sorted(
                predicados_grafo - set(V.CONTENIDO) - set(fuera))}


def asignar(N_h: dict, n: int) -> tuple[dict, list, dict]:
    con_minimo = {h for h in N_h if h != V.ESTRATO_OTROS and N_h[h] >= V.UMBRAL_ESTRATO}
    fijos, rondas = {}, []
    while True:
        libres = [h for h in N_h if h not in fijos]
        resto = n - sum(fijos.values())
        tot = sum(N_h[h] for h in libres)
        q = {h: resto * N_h[h] / tot for h in libres}
        bajo = sorted(h for h in libres if h in con_minimo and q[h] < V.MINIMO)
        rondas.append({"resto": resto, "cuotas": {h: round(q[h], 6) for h in libres}, "fijados_en_3": bajo})
        if not bajo:
            break
        for h in bajo:
            fijos[h] = V.MINIMO
    base = {h: math.floor(q[h]) for h in q}
    falta = resto - sum(base.values())
    restos = {h: q[h] - base[h] for h in q}
    rng = random.Random(f"{V.SEMILLA}:empate")
    desempate = {h: rng.random() for h in sorted(q)}
    orden = sorted(q, key=lambda h: (-round(restos[h], 12), desempate[h]))
    empates = [h for h in orden[:falta] if any(abs(restos[h] - restos[g]) < 1e-12 for g in orden[falta:])]
    for h in orden[:falta]:
        base[h] += 1
    asign = {h: (fijos.get(h) if h in fijos else base[h]) for h in N_h}
    return asign, rondas, {"restos": {h: round(restos[h], 6) for h in restos}, "falta": falta,
                           "suben_por_resto": orden[:falta], "empates_en_el_corte": empates}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--copia", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()

    kg, s_kg = V.cargar_kg(a.copia)
    ids = {n["id"] for n in kg["nodes"]}
    con_barra = sorted(i for i in ids if "|" in i)
    if con_barra:
        raise SystemExit(f"FRENO: ids de nodo con «|»: {con_barra[:5]}")
    predicados_grafo = {e["relation"] for e in kg["edges"]}
    fuera = lista_de_fuera(a.copia, predicados_grafo)

    cont = [e for e in kg["edges"] if e["relation"] in V.CONTENIDO]
    claves = [V.clave(e) for e in cont]
    rep = [k for k, c in Counter(claves).items() if c > 1]
    if rep:
        raise SystemExit(f"FRENO: {len(rep)} claves repetidas en la población: {rep[:5]}")
    con_rol = [V.clave(e) for e in cont if e.get("rol_fuente") or (e.get("properties") or {}).get("rol_fuente")]
    if con_rol:
        raise SystemExit(f"FRENO: aristas de contenido con rol_fuente (derivadas): {con_rol[:5]}")
    colgantes = [V.clave(e) for e in cont if e["source"] not in ids or e["target"] not in ids]
    if colgantes:
        raise SystemExit(f"FRENO: aristas colgantes: {colgantes[:5]}")

    N_pred = Counter(e["relation"] for e in cont)
    estrato_de = {p: (p if N_pred[p] >= V.UMBRAL_ESTRATO else V.ESTRATO_OTROS) for p in V.CONTENIDO}
    filas = sorted([[V.clave(e), e["relation"], estrato_de[e["relation"]],
                     [p["chunk_id"] for p in e["provenances"]], [p["to"] for p in e["provenances"]]] for e in cont],
                   key=lambda f: f[0])
    N = len(filas)
    N_h = Counter(f[2] for f in filas)
    estratos = sorted(N_h, key=lambda h: (h == V.ESTRATO_OTROS, -N_h[h], h))
    N_h = {h: N_h[h] for h in estratos}

    # la diferencia contra el texto firmado (3.983 en 2922b72d) y su causa
    previo = json.loads((a.copia / V.KG_PREVIO_REL).read_text(encoding="utf-8"))
    s_prev = V.sha_archivo(a.copia / V.KG_PREVIO_REL)
    if s_prev != V.KG_PREVIO_SHA256:
        raise SystemExit(f"kg previo con sha256 {s_prev}")
    cl_prev = {V.clave(e): e for e in previo["edges"] if e["relation"] in V.CONTENIDO}
    cl_now = {V.clave(e): e for e in cont}
    salen, entran = sorted(set(cl_prev) - set(cl_now)), sorted(set(cl_now) - set(cl_prev))
    diff = json.loads((a.copia / V.DIFF_RESELLADO_REL).read_text(encoding="utf-8"))
    decl = {(x["clave"], x["cambio"]): x for x in diff["lista"] if x["objeto"] == "arista"}
    def causa(k, cambio):
        x = decl.get((k, cambio))
        return {"clave": k, "causa": x["causa"] if x else None, "unidades_r0": (x or {}).get("unidades_r0")}
    filas_sale = [causa(k, "sale") for k in salen]
    filas_entra = [causa(k, "entra") for k in entran]
    N_prev = Counter(e["relation"] for e in cl_prev.values())
    diferencia = {
        "grafo_del_texto_firmado": {"nombre": "KG-Tanda0-Desarrollo-r2b-sincola", "sha256": s_prev,
                                    "ruta": V.KG_PREVIO_REL, "N": sum(N_prev.values()),
                                    "por_predicado": {p: N_prev[p] for p in V.CONTENIDO}},
        "texto_firmado_por_predicado": V.POBLACION_PREREGISTRO,
        "recuento_del_texto_firmado_reproduce": dict(N_prev) == V.POBLACION_PREREGISTRO,
        "grafo_medido": {"N": N, "por_predicado": {p: N_pred[p] for p in V.CONTENIDO}},
        "por_predicado_diferencia": {p: N_pred[p] - N_prev[p] for p in V.CONTENIDO},
        "salen": len(salen), "entran": len(entran),
        "salen_por_predicado": dict(Counter(k.split("|")[1] for k in salen)),
        "entran_por_predicado": dict(Counter(k.split("|")[1] for k in entran)),
        "causas_salen": dict(Counter(str(f["causa"]) for f in filas_sale)),
        "causas_entran": dict(Counter(str(f["causa"]) for f in filas_entra)),
        "sin_causa_declarada": [f["clave"] for f in filas_sale + filas_entra if f["causa"] is None],
        "fuente_de_las_causas": V.DIFF_RESELLADO_REL, "filas_salen": filas_sale, "filas_entran": filas_entra}

    poblacion = {
        "unidad": "U-TRIP-V, paso a: la población de la etapa V (§3.1); nada se lee todavía",
        "grafo": {"nombre": V.KG_NOMBRE, "ruta": V.KG_REL, "sha256": s_kg, "nodos": len(kg["nodes"]),
                  "aristas": len(kg["edges"]), "commit_sellado": "4fe6ece (grafos.py:216-223)"},
        "aristas_por_predicado_en_el_grafo": dict(Counter(e["relation"] for e in kg["edges"]).most_common()),
        "contenido": list(V.CONTENIDO), "lista_de_fuera": fuera,
        "N": N, "por_predicado": {p: N_pred[p] for p in V.CONTENIDO},
        "diferencia_con_el_texto_firmado": diferencia,
        "clave": "fuente|predicado|destino; sin repetidas (controlado)",
        "filas_formato": "[clave, predicado, estrato, [chunk_id de cada procedencia], [to de cada procedencia]], "
                         "ordenadas por clave",
        "sha256_lista": V.sha(V.canon(filas)),
        "sha256_claves": V.sha(("\n".join(f[0] for f in filas) + "\n").encode("utf-8")),
        "como_se_calcula_el_sha256": "sha256_lista: json.dumps(filas, ensure_ascii=False, separators=(',', ':')) en "
                                     "UTF-8; sha256_claves: las claves ordenadas, una por línea, con salto final",
        "filas": filas}
    s_pob = V.escribir_json(a.salida / "poblacion_V.json", poblacion)

    asign, rondas, redondeo = asignar(N_h, V.N_MUESTRA)
    if sum(asign.values()) != V.N_MUESTRA:
        raise SystemExit("la asignación no suma 100")
    sin_muestra = [h for h in asign if asign[h] == 0]
    asignacion = {
        "unidad": "U-TRIP-V, paso b: estratos y asignación (§3.2), escrita antes de sortear",
        "hora": V.hora(), "poblacion_V.json_sha256": s_pob, "sha256_lista_poblacion": poblacion["sha256_lista"],
        "N": N, "estratos": {h: {"N_h": N_h[h], "W_h": round(N_h[h] / N, 6), "W_h_fraccion": f"{N_h[h]}/{N}",
                                 "predicados": sorted(p for p in V.CONTENIDO if estrato_de[p] == h),
                                 "n_h": asign[h]} for h in estratos},
        "regla": "proporcional, mínimo 3 por predicado con 30 aristas o más; los de menos de 30 en «otros» (sin "
                 "mínimo); los que quedan por debajo de 3 se fijan en 3 y el resto se reparte en proporción entre los "
                 "demás, hasta que ninguno quede por debajo; redondeo por restos mayores, empate con "
                 "random.Random(f'{semilla}:empate')",
        "rondas": rondas, "redondeo": redondeo, "n": asign, "suma": sum(asign.values()),
        "estratos_sin_muestra": {h: {"N_h": N_h[h], "W_h": round(N_h[h] / N, 6),
                                     "predicados": sorted(p for p in V.CONTENIDO if estrato_de[p] == h)}
                                 for h in sin_muestra},
        "declaracion_estratos_sin_muestra": (
            "Letra del §3.2, decidida al sellar el 19/10/2026: «otros» no tiene mínimo y su cuota proporcional "
            "(0,26 sobre los 85 que quedan después de los mínimos) redondea a 0. Las 11 aristas de ejecuta "
            "(W = 11/3.967 = 0,0028) quedan sin muestra: p̂_w cubre 3.956 de 3.967 y se informa con las dos cotas de ese "
            "estrato (todas correctas y todas incorrectas). Las de ejecuta entran al pool de 20 solo si el sorteo las "
            "elige, sin forzarlo.") if sin_muestra else None,
        "semilla": V.SEMILLA}
    s_asig = V.escribir_json(a.salida / "asignacion_V.json", asignacion)

    print(json.dumps({"N": N, "por_predicado": poblacion["por_predicado"], "fuera": fuera["fuera"],
                      "agregados_a_la_lista_de_fuera": fuera["agregados_a_la_lista_de_fuera"],
                      "diferencia": {k: diferencia[k] for k in ("por_predicado_diferencia", "salen", "entran",
                                                                 "causas_salen", "causas_entran", "sin_causa_declarada",
                                                                 "recuento_del_texto_firmado_reproduce")},
                      "sha256_lista": poblacion["sha256_lista"], "poblacion_V.json": s_pob,
                      "estratos": {h: (N_h[h], asign[h]) for h in estratos}, "redondeo": redondeo,
                      "hora_asignacion": asignacion["hora"], "asignacion_V.json": s_asig}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
