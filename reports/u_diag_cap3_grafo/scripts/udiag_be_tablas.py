"""Tablas de las tareas b y e (y del grupo H) en markdown, leídas de las salidas JSON de esta unidad.
Uso: PYTHONDONTWRITEBYTECODE=1 <venv>/bin/python -B udiag_be_tablas.py
Escribe salida/tabla_b.md y salida/tabla_e.md.
"""
import json
import os

from udiag_comun import AQUI

OUT = os.path.join(AQUI, "salida")


def main():
    b = json.load(open(os.path.join(OUT, "procedencia_b.json"), encoding="utf-8"))
    lin = ["# Tarea b: nodos de contenido con el punto en un ancestro de su unidad", "",
           "Fuente: `procedencia_b.json` (`udiag_b_procedencia.py`). Clase de VERIF: la regla de VERIF-CAP3-COHERENCIA,"
           " tarea d. Diagnóstico: `verificar_tramo` del validador r2, holgura 2.", ""]
    for nombre in ("diez", "sincola"):
        r = b[nombre]["resumen"]
        lin += [f"## {nombre}: {r['poblacion']} nodos; clase de VERIF " +
                "; ".join(f"{k} {v}" for k, v in r["clase_verif"].items()), "",
                f"Los {r['tramo_fuera_del_parrafo_del_ancestro']} cuyo tramo no está en el párrafo del ancestro, por diagnóstico y por clase de VERIF:", "",
                "| diagnóstico | " + " | ".join(sorted(r["fuera_del_parrafo_diagnostico_por_clase_verif"])) + " | total |",
                "|---|" + "---:|" * (len(r["fuera_del_parrafo_diagnostico_por_clase_verif"]) + 1)]
        clases = sorted(r["fuera_del_parrafo_diagnostico_por_clase_verif"])
        for d, tot in r["fuera_del_parrafo_por_diagnostico"].items():
            lin.append(f"| {d} | " + " | ".join(str(r["fuera_del_parrafo_diagnostico_por_clase_verif"][c].get(d, 0)) for c in clases)
                       + f" | {tot} |")
        lin += ["", f"G restringida (G-r) en los {r['poblacion']}: cambia el punto {r['g_restringida_en_la_poblacion']['cambia_punto']} "
                f"({r['g_restringida_en_la_poblacion']['cambia_punto_por_tipo']}); solo el rol {r['g_restringida_en_la_poblacion']['cambia_solo_rol']}; "
                f"sin cambio {r['g_restringida_en_la_poblacion']['sin_cambio']}.", ""]
        for v in ("g_restringida_en_todos_los_nodos_de_contenido", "g_literal_en_todos_los_nodos_de_contenido"):
            g = r[v]
            lin.append(f"- {v}: cambian el punto {g['cambian_punto']} ({g['cambio_punto']}; por tipo "
                       f"{g['cambian_punto_por_tipo']}); solo el rol {g['cambian_solo_rol']}; ids que se fusionarían "
                       f"{g['ids_que_fusionarian_con_un_nodo_existente']}; pertenencias a subgrafos de hermanas que se "
                       f"pierden (§5.6) {g['pertenencias_a_subgrafos_de_hermanas_que_se_pierden']}.")
        lin.append("")
    open(os.path.join(OUT, "tabla_b.md"), "w", encoding="utf-8").write("\n".join(lin))
    e = json.load(open(os.path.join(OUT, "aisladas_e.json"), encoding="utf-8"))
    h = json.load(open(os.path.join(OUT, "tipo_operacion_h.json"), encoding="utf-8"))
    lin = ["# Tarea e: condiciones aisladas, definición vigente y redefinición", "",
           "Fuente: `aisladas_e.json` (`udiag_e_aisladas.py`). (A) Condicion sin ninguna arista de contenido: sin contar "
           "`establecida_en` ni la remisión (`remite_a`; en los grafos del perfil r1, `referencia` con `rol_fuente = "
           "referencia_cruzada`). (A-literal) sin esa última exclusión. (B) sin `condicion_de` saliente.", "",
           "| columna | grafo | sha256 | Condicion | vigente: sin ninguna arista | aislados de todo tipo | (A) | (A-literal) | (B) |",
           "|---|---|---|---:|---:|---:|---:|---:|---:|"]
    for g in e["grafos"]:
        lin.append(f"| {g['columna']} | {g['grafo']} | `{g['sha256'][:8]}…` | {g['condicion']} | "
                   f"{g['vigente_condicion_sin_ninguna_arista']} | {g['vigente_aislados_de_todo_tipo']} | "
                   f"{g['A_condicion_sin_arista_de_contenido']} | {g['A_literal_sin_establecida_en_ni_remite_a']} | "
                   f"{g['B_condicion_sin_condicion_de_saliente']} |")
    lin += ["", "# Grupo H: `Operacion.tipo`", "", "Fuente: `tipo_operacion_h.json` (`udiag_h_tipo_operacion.py`).", "",
            "| grafo | Operacion | distintos tal cual | en minúsculas | sin diacríticos | normalizados | con un solo nodo |",
            "|---|---:|---:|---:|---:|---:|---:|"]
    for nombre, x in h.items():
        lin.append(f"| {nombre} | {x['operaciones']} | {x['distintos_tal_cual']} | {x['distintos_minusculas']} | "
                   f"{x['distintos_minusculas_sin_tildes']} | {x['distintos_normalizados']} | "
                   f"{x['unicos_normalizados_con_un_solo_nodo']} |")
    lin += ["", "Los diez más frecuentes, normalizados (diez): " +
            "; ".join(f"{k} {v}" for k, v in h["diez"]["diez_mas_frecuentes_normalizados"])]
    open(os.path.join(OUT, "tabla_e.md"), "w", encoding="utf-8").write("\n".join(lin))
    print("ok")


if __name__ == "__main__":
    main()


def g_r_22():
    """Volcado de los cambios de punto de G-r en a9631a64, para leerlos (salida/g_r_22_cambios_de_punto.md)."""
    from udiag_comun import cargar_chunks, chunk_base
    d = json.load(open(os.path.join(OUT, "procedencia_b.json"), encoding="utf-8"))
    ch = cargar_chunks()
    lin = ["# Los 22 cambios de punto de G-r en a9631a64 (para leer)", ""]
    for i, f in enumerate([f for f in d["diez"]["filas"] if f["punto_g"] != f["punto"]], 1):
        c = chunk_base(f["chunk_id"], ch)
        anc = [h for h in c["herencia"] if h["unidad_origen"] == f["punto"]]
        lin += [f"## G{i}. {f['type']} «{f['label']}» `{f['chunk_id']}`: punto {f['punto']} → {f['punto_g']} "
                f"({f['lugar']}, {f['nivel']})",
                f"- tramo: {f['tramo']}",
                "- bloques del punto viejo: " + " | ".join(f"[{h['tipo']}] {h['texto'][:260]}" for h in anc),
                f"- texto propio: {c['texto'][:420]}", ""]
    open(os.path.join(OUT, "g_r_22_cambios_de_punto.md"), "w", encoding="utf-8").write("\n".join(lin) + "\n")
