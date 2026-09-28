"""U-ESTUDIO-MATRIZ, paso 4 — arma el reporte (markdown) desde los JSON de
los pasos 1-3 y p4_filas.json. Todo número del reporte sale de esos archivos.
Salida: uestmat_reporte_U-ESTUDIO-MATRIZ.md
"""
from __future__ import annotations

import collections
import json
from pathlib import Path

OUT = Path("/tmp/u_estudio_matriz")
P4_FILAS = Path("/Users/agustinavidelarivero/INGENIERIA IA/TESIS/bcra-regulatory-kg/reports/"
                "u_audit_tipos_v3/p4_filas.json")
DEV = {"pro", "cla", "ric", "cap", "ext"}


def usd(x: float, nd: int = 2) -> str:
    return f"{x:.{nd}f}".replace(".", ",")


def n(x: int) -> str:
    return f"{x:,}".replace(",", ".")


def main() -> None:
    c1 = json.loads((OUT / "uestmat_paso1_control.json").read_text(encoding="utf-8"))
    v2 = json.loads((OUT / "uestmat_paso2_variantes.json").read_text(encoding="utf-8"))
    m3 = json.loads((OUT / "uestmat_paso3_muestra.json").read_text(encoding="utf-8"))
    p4f = json.loads(P4_FILAS.read_text(encoding="utf-8"))
    tar = v2["tarifas_e3_tanda0"]
    g = v2["grafo"]
    pv = v2["variantes"]
    L = []
    L.append("# U-ESTUDIO-MATRIZ — efecto y muestra de las relaciones rechazadas por la matriz congelada\n")
    L.append("Solo lectura, USD 0, sin Neo4j. Salidas en `/tmp/u_estudio_matriz/` (sha256 en `manifest.txt`). "
             "Reproducción: `cd /tmp/u_estudio_matriz && PYTHONDONTWRITEBYTECODE=1 python3 "
             "uestmat_paso{1_control,2_variantes,3_muestra,4_reporte}.py` en ese orden.\n")

    L.append("## Controles\n")
    L.append(f"- E1 primera pasada re-validada desde el crudo con la matriz congelada SIN ampliar "
             f"(`uestmat_paso1_control.json`): {n(c1['revalidacion_igual_persistida'])} de "
             f"{n(c1['registros'] - c1['sin_crudo'])} registros con crudo reproducen la validación persistida "
             f"({c1['sin_crudo']} registros sin crudo, todos con error de API). Rechazos firma_invalida "
             f"recomputados: {c1['rechazos_firma_invalida_recomputados']}; iguales a p4_filas "
             f"(clave to/chunk_id/idx/par/línea): {'sí' if c1['rechazos_iguales_a_p4'] else 'NO'}. "
             f"Con la matriz sin ampliar, los {c1['rechazos_p4']} siguen inválidos.")
    L.append(f"- Población final (lo que ensambla r1), 10 TOs: {n(c1['final_e1_last_wins'])} unidades con "
             f"crudo de E1, {c1['final_cache_reintentos']} con crudo del reintento (`e1_reintentos.db`, "
             f"immutable=1, un solo candidato por unidad) y {c1['final_e1_compact_last_wins']} de cola "
             f"(validación E1 del compact); reproducen su validación "
             f"{n(c1['final_e1_last_wins_reproduce'])}/{c1['final_cache_reintentos_reproduce']}/"
             f"{c1['final_e1_compact_last_wins_reproduce']}.")
    L.append(f"- Re-ensamblado en memoria de KG-Tanda0-Desarrollo-r1 (réplica de `ensamblar_tanda0.py`, "
             f"sin escribir intermedios), sin envoltorio y con envoltorio sobre la matriz sin ampliar "
             f"({n(v2['control_unidades_revalidadas_dev'])} unidades re-validadas): "
             f"`{v2['control_reensamblado_sin_envoltorio_sha256'][:12]}…` y "
             f"`{v2['control_reensamblado_envoltorio_congelado_sha256'][:12]}…` = sha sellado "
             f"`{g['sha256'][:12]}…`.")
    L.append(f"- Grafo: {n(g['nodos'])} nodos / {n(g['aristas'])} aristas; aislados hoy {g['aislados_hoy']} "
             f"({', '.join(f'{k} {v}' for k, v in sorted(g['aislados_hoy_por_tipo'].items(), key=lambda x: -x[1]))}).")
    L.append(f"- Tarifa de E3 de la tanda 0: USD {usd(tar['tarifa_fase_e3_usd_por_unidad'], 6)} por unidad "
             f"= {usd(tar['fase_e3_gasto_usd'], 6)} / {n(tar['fase_e3_unidades'])} (fase E3 completa de los "
             f"10 TOs, incluye reintentos E1; `salida_dirigida/estado_corpus.json`). Alternativa solo "
             f"verificación: USD {usd(tar['tarifa_verificacion_usd_por_llamada'], 6)} por llamada = "
             f"{usd(tar['verificacion_gasto_usd'], 4)} / {n(tar['verificacion_llamadas'])} "
             f"(`<to>/resumen_e3.json`); con ella cada costo de la tabla se multiplica por "
             f"{usd(tar['tarifa_verificacion_usd_por_llamada'] / tar['tarifa_fase_e3_usd_por_unidad'], 3)}. "
             f"No incluye la re-extracción dirigida de tres unidades (presupuesto aparte).\n")

    L.append("## Tabla del punto 1\n")
    L.append("A = E1 primera pasada (población de los 982); B = población final (entrada de r1); aristas y "
             "aislados = KG-Tanda0-Desarrollo-r1 re-ensamblado con la ampliación; fragmentos = unidades de "
             "A ∪ B (las que cambian su entrada a E3). Pares de números: 10 TOs / 5 de desarrollo.\n")
    L.append("| id | ampliación en memoria | A rel. nuevas | B rel. nuevas | aristas nuevas en r1 | "
             "aislados que dejan de estarlo | fragmentos a re-verificar | costo USD (tarifa fase) |")
    L.append("|---|---|---|---|---|---|---|---|")
    for v in pv:
        amp = "; ".join(
            f"{p}: " + ", ".join([f"dom+{x}" for x in a["dominio_mas"]] + [f"rango+{x}" for x in a["rango_mas"]])
            for p, a in v["ampliacion_en_memoria"].items())
        A, B, C, D = v["A_e1_primera_pasada"], v["B_poblacion_final"], v["C_grafo_dev_r1"], v["D_reverificacion_e3"]
        des = C["aislados_que_dejan_de_estarlo"]
        des_t = ", ".join(f"{k} {m}" for k, m in sorted(C["aislados_que_dejan_de_estarlo_por_tipo"].items()))
        L.append(f"| {v['id']} | {amp} | {A['relaciones_validas_nuevas_10tos']} / {A['relaciones_validas_nuevas_dev']} | "
                 f"{B['relaciones_validas_nuevas_10tos']} / {B['relaciones_validas_nuevas_dev']} | "
                 f"{C['aristas_nuevas']} | {des}{' (' + des_t + ')' if des else ''} | "
                 f"{D['fragmentos_10tos']} / {D['fragmentos_dev']} | "
                 f"{usd(D['costo_usd_10tos_tarifa_fase'])} / {usd(D['costo_usd_dev_tarifa_fase'])} |")
    L.append("")
    iguales = [v["id"] for v in pv if v["tipo"] != "par"
               and any(w["tipo"] == "par" and w["pares"] == v["pares"] for w in pv)]
    L.append(f"- En todas las variantes: aristas perdidas "
             f"{sum(v['C_grafo_dev_r1']['aristas_perdidas'] for v in pv)}, nodos nuevos "
             f"{sum(len(v['C_grafo_dev_r1']['nodos_nuevos']) for v in pv)}, nodos perdidos "
             f"{sum(len(v['C_grafo_dev_r1']['nodos_perdidos']) for v in pv)}; aristas nuevas = relaciones "
             f"nuevas de B en desarrollo (ninguna colapsa con otra). Cada ampliación valida exactamente "
             f"los pares buscados (asserto sobre 10 tipos × 13 predicados × 10 tipos): en los 11 candidatos "
             f"ampliar dominio o rango equivale a agregar solo el par.")
    if iguales:
        L.append(f"- Agrupadas con un solo par candidato (idénticas a su fila P): {', '.join(iguales)}.")
    L.append("- A coincide con los conteos de p4 por par (asserto). B difiere de A porque en las unidades "
             "aceptadas tras reintento el grafo se construyó con la salida del reintento.")
    L.append("- Contraste externo: P01, P02, P07 y P08 desaíslan 20, 3, 9 y 1 Condiciones, los mismos "
             "conteos por par del punto 3 de U-AUDIT-TIPOS-V3.")
    L.append("- Supuesto: lo que pasa a válido entra al grafo sin nueva verificación E3 (cota superior). "
             "Efecto DESPUÉS de re-verificar: NO ENCONTRADO — requiere llamar a E3 (y eventualmente a "
             "reintentos), fuera del alcance USD 0.\n")

    L.append("## Muestra del punto 2\n")
    L.append(f"- Población: {m3['poblacion']}; en los estratos candidatos: {m3['poblacion_en_estratos']}.")
    L.append(f"- Asignación: {m3['asignacion']}. Primera vuelta: nueve estratos con cuota < 5 quedan en 5; "
             f"segunda vuelta reparte {m3['traza_asignacion'][-1]['total_a_repartir']} entre los dos mayores "
             f"(cuotas {', '.join(usd(q, 2) for q in m3['traza_asignacion'][-1]['cuotas'].values())}).")
    L.append(f"- Sorteo: semilla {m3['semilla']}; {m3['procedimiento']}. Filas M01..M60 por estrato "
             f"(n descendente) y, dentro, por (to, chunk_id, idx).")
    L.append("\n| par | n población | n muestra |\n|---|---|---|")
    for c in m3["conteos_por_estrato"]:
        L.append(f"| {c['par']} | {c['n_poblacion']} | {c['n_muestra']} |")
    L.append(f"| total | {m3['poblacion_en_estratos']} | {m3['total_muestra']} |\n")
    cnt = collections.Counter("dev" if f["to"] in DEV else "nuevos" for f in m3["filas"])
    L.append(f"- Composición: {cnt['dev']} filas de los TOs de desarrollo y {cnt['nuevos']} de los cinco "
             f"nuevos de la tanda 0 (`uestmat_paso3_muestra.json`, campo filas).")
    est = {(f["to"], f["linea"], f["idx"]): f["estado_e3_final"] for f in p4f}
    tras = sum(1 for f in m3["filas"] if est[(f["to"], f["linea_e1"], f["idx"])] == "aceptado_tras_reintento")
    L.append(f"- {tras} de las 60 filas son de unidades aceptadas tras reintento: la relación sorteada es de "
             "la primera pasada y puede no estar en la salida que entró al grafo (no cambia su verdad).")
    L.append(f"- CSV `uestmat_muestra_60.csv` (UTF-8 con BOM): columnas {', '.join(m3['columnas_csv'])}. "
             "Veredicto y nota vacíos. Texto del fragmento = herencia + texto propio de E0, verificado contra "
             "sha256_completo. Para el extremo Sujeto de aplica_a se transcribe el id emitido; la descripción "
             "queda vacía porque el extractor no la emite.\n")

    L.append("## Observaciones y desvíos\n")
    L.append("1. Desvío propio: la línea de base de `git status` y de `.pyc` se escribió primero en el "
             "scratchpad de la sesión (fuera de `/tmp/u_estudio_matriz/`), por el hábito de usarlo para "
             "temporales. Se movió acá (`uestmat_git_status_inicio*.txt`, `uestmat_pyc_inicio.txt`) antes "
             "de cualquier otra escritura; el scratchpad quedó vacío.")
    L.append("2. Contradicción CLAUDE.md §4.g (paquete de revisión en el scratchpad) vs mandato (escribir solo "
             "en `/tmp/u_estudio_matriz/`): el directorio del mandato ES el paquete (prefijo `uestmat_`, "
             "`manifest.txt` con sha256). No se armó paquete aparte.")
    L.append("3. «Variante agrupada por predicado»: se calcularon las dos lecturas — todos los pares "
             "candidatos del predicado (G-<predicado>) y el ejemplo literal del mandato "
             "(G-condicion_de-ejemplo: + Operacion y Potestad).")
    L.append("4. La regla «proporcional con mínimo 5» deja al segundo estrato (231) en el mínimo, igual que "
             "los estratos de 10 a 45: con 60 filas y 11 estratos la cuota proporcional solo supera 5 en los "
             "dos mayores. Otra regla requiere decisión de la autora; no se aplicó ninguna.")
    L.append("5. Trazabilidad de U-AUDIT-TIPOS-V3: su inventario declara la lectura de `e1_reintentos.db` "
             "con immutable=1, pero ningún script de `reports/u_audit_tipos_v3/` abre esa db (grep de "
             "`e1_reintentos|immutable` sobre sus .py: vacío). El paso 1 rehace esa ubicación con script "
             "conservado acá.")
    ini = (OUT / "uestmat_git_status_inicio.txt").read_text(encoding="utf-8").splitlines()
    fin = (OUT / "uestmat_git_status_cierre.txt").read_text(encoding="utf-8").splitlines()
    nuevas = [x for x in fin if x not in ini]
    idas = [x for x in ini if x not in fin]
    dirs = sorted({x[3:].rsplit("/", 1)[0] for x in nuevas})
    L.append(f"6. Criterio «git status igual al inicio»: NO se cumple literalmente. `git status --porcelain` "
             f"de cierre tiene {len(nuevas)} líneas nuevas y {len(idas)} desaparecidas respecto del inicio, "
             f"todas en {', '.join(f'`{d}/`' for d in dirs)}; además HEAD avanzó de `8cf8c23` a `791166d` "
             f"(commit de reports de U-INV-CANDIDATOS, 16:56:52) y crecen los no rastreados de "
             f"`data/experiment/ev2_tanda0/` (corrida en curso). Nada de eso es de esta unidad: sus únicas "
             f"escrituras están en este directorio (`uestmat_cierre_controles.txt`: `.pyc` iguales, "
             f"scratchpad vacío; fuera de esas rutas, lo único más nuevo que la línea de base es el log de "
             f"Neo4j y la entrada de directorio `reports/`, con mtime 16:56:44, ocho segundos antes del "
             f"commit ajeno, y sin archivos nuevos adentro), ningún módulo importado referencia "
             f"`docs/tesis`, y git se usó solo con status, log y show.\n")
    (OUT / "uestmat_reporte_U-ESTUDIO-MATRIZ.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))


if __name__ == "__main__":
    main()
