"""U-REEXT-T0, T3-bis: casos sintéticos de las correcciones del ensamblado r2b (decisiones 1 a 3 y las dos
ampliaciones tomadas en la sesión). Importa data/experiment/tanda0/code/ensamblar_tanda0.py como lo hace el
ensamblado (su propio sys.path) y llama a sus funciones; no escribe nada salvo el JSON de --out. USD 0, sin red.

  A. 1.a: el renombre cross-TO actualiza id_nodo solo en las filas del TO renombrado.
  B. 1.b: el propuesto con mención vacía («se», «cada una») se descarta con la marca; sus aristas se quitan y se
     listan; un propuesto con mención de contenido no se toca.
  C. 1.b: padre_sugerido hacia una instancia → su clase (marca padre_sugerido_instancia); instancia sin clase →
     se quita (marca padre_sugerido_descartado).
  D. 1.c: sin padre → rol de alcance del TO (marca padre_por_defecto); TOs con roles distintos o sin rol → listado.
  E. 2: la celda de una tabla con rótulo hereda la unidad («-En millones de pesos-»); sin rótulo, con valor, con
     otra comparación o con un tramo que no es celda, no cambia. Integrado en llenar_umbrales_r2 sobre cap::1.2 (E0
     r2b): r2b gana el valor, r2a no cambia.
  F. 3: marca umbral_no_cuantificable: sin cuantía → motivo «sin cuantía detectable»; cuantías solo en una tabla
     forzada a residual → motivo propio y sha de la lista; cuantías en otra tabla o en la descripción → sin marca;
     con lista → no se evalúa.

Uso (desde la raíz del repo o de una copia): python -B data/experiment/reext_t0/t3bis/pruebas_t3bis.py --out ARCHIVO
"""
from __future__ import annotations

import argparse
import json
import sys
import tempfile
from collections import OrderedDict
from copy import deepcopy
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(RAIZ / "data" / "experiment" / "tanda0" / "code"))
import ensamblar_tanda0 as ENS  # noqa: E402

RES: "OrderedDict[str, list]" = OrderedDict()


def check(grupo: str, nombre: str, cond: bool, detalle: str = "") -> None:
    RES.setdefault(grupo, []).append({"caso": nombre, "ok": bool(cond), "detalle": detalle[:600]})


def prov(to: str, cid: str, tramo: str | None = None) -> dict:
    p = {"to": to, "archivo": ENS.C.archivo_de_to(to), "punto": cid.split("::")[1], "chunk_id": cid,
         "rol_documental": "punto_propio"}
    if tramo:
        p["tramo"] = tramo
    return p


def sujeto(i: str, label: str, to: str, cid: str, **props) -> dict:
    p = prov(to, cid)
    return {"id": i, "type": "Sujeto", "label": label, "properties": {"nivel": "propuesto", "cuarentena": "true", **props},
            "provenance": p, "provenances": [p]}


def obligacion(i: str, to: str, cid: str, tramo: str) -> dict:
    p = prov(to, cid, tramo)
    return {"id": i, "type": "Obligacion", "label": i, "properties": {"descripcion": "x"}, "provenance": p, "provenances": [p]}


def aplica(src: str, tgt: str, to: str, cid: str, mencion: str) -> dict:
    p = prov(to, cid)
    return {"source": src, "target": tgt, "relation": "aplica_a", "provenance": p, "provenances": [p],
            "sujeto_mencion": mencion, "mencion_verificada": "exacta", "metodo_resolucion": "cuarentena"}


CAT = {"entrada_esqueleto": {
           "clases": [{"id": "Sujeto_organismo_publico", "nivel": "clase"},
                      {"id": "Sujeto_sefyc", "nivel": "instancia", "instancia_de": "Sujeto_organismo_publico"},
                      {"id": "Sujeto_instancia_huerfana", "nivel": "instancia", "instancia_de": None},
                      {"id": "Sujeto_banco", "nivel": "clase"}],
           "roles": [{"id": "Sujeto_rol_alcance_capmin"}, {"id": "Sujeto_rol_entidad_autorizada_exterior"}]},
       "rol_por_to": {ENS.C.archivo_de_to("cap"): {"rol_id": "Sujeto_rol_alcance_capmin"},
                      ENS.C.archivo_de_to("ext"): {"rol_id": "Sujeto_rol_entidad_autorizada_exterior"}}}


def grupo_a_d() -> None:
    kg = {"nodes": [
        sujeto("Sujeto_propuesto_la_entidad", "la entidad", "cap", "cap::1.1"),
        sujeto("Sujeto_propuesto_la_entidad__ext", "la entidad", "ext", "ext::2.1", colision_cross_to="true",
               padre_sugerido="Sujeto_rol_entidad_autorizada_exterior"),
        sujeto("Sujeto_propuesto_se", "se", "cap", "cap::12.3", padre_sugerido="Sujeto_sefyc"),
        sujeto("Sujeto_propuesto_cada_una", "cada una", "ext", "ext::7.3.11"),
        sujeto("Sujeto_propuesto_los_casos", "Los casos", "ext", "ext::13.6"),
        sujeto("Sujeto_propuesto_el_organo", "el órgano", "cap", "cap::12.4", padre_sugerido="Sujeto_sefyc"),
        sujeto("Sujeto_propuesto_huerfano", "el huérfano", "cap", "cap::12.5", padre_sugerido="Sujeto_instancia_huerfana"),
        dict(sujeto("Sujeto_propuesto_dos_tos", "las partes", "cap", "cap::3.1"),
             provenances=[prov("cap", "cap::3.1"), prov("ext", "ext::3.1")]),
        obligacion("Obligacion_12_3", "cap", "cap::12.3", "se considerará la última calificación"),
        obligacion("Obligacion_7_3_11", "ext", "ext::7.3.11", "cada una puede certificar"),
    ], "edges": []}
    kg["edges"] = [aplica("Obligacion_12_3", "Sujeto_propuesto_se", "cap", "cap::12.3", "se"),
                   aplica("Obligacion_7_3_11", "Sujeto_propuesto_cada_una", "ext", "ext::7.3.11", "cada una")]
    registro = [
        {"to": "cap", "chunk_id": "cap::1.1", "id_nodo": "Sujeto_propuesto_la_entidad", "estado": "cuarentena"},
        {"to": "ext", "chunk_id": "ext::2.1", "id_nodo": "Sujeto_propuesto_la_entidad", "estado": "cuarentena",
         "indice_relacion": 3},
        {"to": "cap", "chunk_id": "cap::12.3", "id_nodo": "Sujeto_propuesto_se", "estado": "cuarentena",
         "indice_relacion": 12},
        {"to": "ext", "chunk_id": "ext::7.3.11", "id_nodo": "Sujeto_propuesto_cada_una", "estado": "cuarentena",
         "indice_relacion": 10},
    ]
    r = ENS.normalizar_propuestos_r2b(kg, registro, {"ext": {"Sujeto_propuesto_la_entidad": "Sujeto_propuesto_la_entidad__ext"}},
                                      CAT)
    d = r["resumen"]["detalle"]
    ids = {n["id"] for n in kg["nodes"]}
    by = {n["id"]: n for n in kg["nodes"]}
    check("A", "la fila del TO renombrado pasa al id nuevo y la del primer TO no cambia",
          registro[0]["id_nodo"] == "Sujeto_propuesto_la_entidad"
          and registro[1]["id_nodo"] == "Sujeto_propuesto_la_entidad__ext" and len(d["filas_renombradas"]) == 1,
          json.dumps(d["filas_renombradas"], ensure_ascii=False))
    check("B", "«se» y «cada una» salen del grafo con sus aristas; «Los casos» y «las partes» quedan",
          "Sujeto_propuesto_se" not in ids and "Sujeto_propuesto_cada_una" not in ids and not kg["edges"]
          and "Sujeto_propuesto_los_casos" in ids and "Sujeto_propuesto_dos_tos" in ids)
    check("B", "sus filas quedan descartadas con la marca y las aristas quitadas, listadas con norma, unidad, mención "
               "y tramo", all(f["estado"] == "descartado" and f["motivo_descarte"] == ENS.MARCA_MENCION_VACIA
                              for f in registro[2:])
          and [(x["to"], x["chunk_id"], x["sujeto_mencion"], x["tramo_del_extremo"], x["indice_relacion"])
               for x in r["aristas_quitadas"]] == [("cap", "cap::12.3", "se", "se considerará la última calificación", 12),
                                                   ("ext", "ext::7.3.11", "cada una", "cada una puede certificar", 10)],
          json.dumps(r["aristas_quitadas"], ensure_ascii=False))
    check("B", "mencion_vacia: solo palabras de la lista cerrada",
          ENS.mencion_vacia("Se") and ENS.mencion_vacia("cada una") and not ENS.mencion_vacia("la entidad")
          and not ENS.mencion_vacia("Dichas evaluaciones") and not ENS.mencion_vacia(""))
    check("C", "padre hacia una instancia → su clase, con la marca de la instancia",
          by["Sujeto_propuesto_el_organo"]["properties"].get("padre_sugerido") == "Sujeto_organismo_publico"
          and by["Sujeto_propuesto_el_organo"]["properties"].get("padre_sugerido_instancia") == "Sujeto_sefyc")
    check("C", "instancia sin clase → padre quitado con la marca padre_sugerido_descartado; luego recibe el rol por defecto",
          by["Sujeto_propuesto_huerfano"]["properties"].get("padre_sugerido_descartado") == "Sujeto_instancia_huerfana"
          and by["Sujeto_propuesto_huerfano"]["properties"].get("padre_sugerido") == "Sujeto_rol_alcance_capmin"
          and by["Sujeto_propuesto_huerfano"]["properties"].get("padre_por_defecto") == "true")
    check("D", "sin padre → rol de alcance de su TO con la marca padre_por_defecto",
          by["Sujeto_propuesto_la_entidad"]["properties"].get("padre_sugerido") == "Sujeto_rol_alcance_capmin"
          and by["Sujeto_propuesto_los_casos"]["properties"].get("padre_sugerido") == "Sujeto_rol_entidad_autorizada_exterior"
          and by["Sujeto_propuesto_los_casos"]["properties"].get("padre_por_defecto") == "true")
    check("D", "un padre que ya está no se toca",
          by["Sujeto_propuesto_la_entidad__ext"]["properties"].get("padre_sugerido") == "Sujeto_rol_entidad_autorizada_exterior"
          and "padre_por_defecto" not in by["Sujeto_propuesto_la_entidad__ext"]["properties"])
    check("D", "TOs con roles distintos → sin padre y listado",
          "padre_sugerido" not in by["Sujeto_propuesto_dos_tos"]["properties"]
          and [x["id"] for x in d["sin_rol_de_alcance"]] == ["Sujeto_propuesto_dos_tos"])
    cat2 = deepcopy(CAT)
    cat2["rol_por_to"].pop(ENS.C.archivo_de_to("ext"))
    kg2 = {"nodes": [sujeto("Sujeto_propuesto_x", "los exportadores", "ext", "ext::1.1")], "edges": []}
    r2 = ENS.normalizar_propuestos_r2b(kg2, [], {}, cat2)
    check("D", "TO sin rol de alcance en el catálogo → sin padre y listado",
          "padre_sugerido" not in kg2["nodes"][0]["properties"] and r2["resumen"]["sin_rol_de_alcance"] == 1)


def grupo_e_f() -> None:
    M = ENS.E4.modulo_modelos_r2()
    V = ENS.E4.modulo_validador_r2()
    import reglas_comparacion as RCMP  # noqa: PLC0415 — pyd_r2/code, en el path por modulo_modelos_r2
    texto = ("1.2. Exigencia básica.\n[TABLA tst::tabla000 | página 4 | e0_tablas | columnas]\nRótulo: -En millones de pesos-\n"
             "Columnas: Bancos | Restantes\nFila 1: Bancos = 5.000 | Restantes = 2.500\n[FIN TABLA tst::tabla000]\n")
    bloques = ENS.bloques_con_rotulo([("tst::1.2", texto)])
    rel = {"tramo": "5.000", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador",
           "origen": "e1", "tramo_verificado": "exacta"}
    h = ENS.unidad_desde_rotulo(rel, bloques, RCMP, M, None, None, "no_determinada")
    check("E", "la celda «5.000» con rótulo «-En millones de pesos-» gana 5000000000 moneda ARS, con el tramo igual",
          bool(h) and (h["tramo"], h["valor"], h["unidad"], h["moneda"], h["comparacion"], h["tramo_verificado"])
          == ("5.000", "5000000000", "moneda", "ARS", "no_determinada", "exacta")
          and h["originales"] == {"regla_comparacion": "limite_relativo:sin_marcador",
                                  "unidad_desde_rotulo": "-En millones de pesos-", "tabla": "tst::tabla000",
                                  "chunk_id": "tst::1.2"}, json.dumps(h, ensure_ascii=False))
    sin_rotulo = ENS.bloques_con_rotulo([("tst::1.2", texto.replace("Rótulo: -En millones de pesos-\n", ""))])
    check("E", "sin rótulo, con valor, con un tramo que no es celda o con otra comparación: no cambia",
          sin_rotulo == []
          and ENS.unidad_desde_rotulo({**rel, "valor": "5000"}, bloques, RCMP, M, None, None, "no_determinada") is None
          and ENS.unidad_desde_rotulo({**rel, "tramo": "7.000"}, bloques, RCMP, M, None, None, "no_determinada") is None
          and ENS.unidad_desde_rotulo({**rel, "comparacion": "maximo_inclusivo"}, bloques, RCMP, M, None, None,
                                      "no_determinada") is None)
    # Integrado: llenar_umbrales_r2 sobre un nodo anclado en cap::1.2 de la E0 r2b (manifiesto r2b de desarrollo)
    man = ENS.MC.cargar(RAIZ / "data/experiment/reextraccion_v2/manifiestos/tanda0_ens_desarrollo_r2b.json")
    perfil = ENS.perfil_e1.perfil(man.perfil_e1)
    cat = ENS.E4.catalogo_r2()
    import runner_corpus as RC  # noqa: PLC0415 — en el path por ensamblar_tanda0
    _, pol = RC.validador_perfil_r2(perfil)
    salida = {}
    with tempfile.TemporaryDirectory() as tmp:
        plan = ENS.plan_redirecciones_r2(man, perfil, RAIZ / "data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b",
                                         Path(tmp) / "r2", cat, M)
        with ENS.redirigido(plan):
            for fase in ("r2b", "r2a"):
                p = prov("cap", "cap::1.2")
                kg = {"nodes": [{"id": "Restriccion_sintetica", "type": "Restriccion", "label": "x",
                                 "properties": {"tipo": "limite_cuantitativo", "descripcion": "Exigencia básica de bancos",
                                                "umbrales": [dict(rel)]}, "provenance": p, "provenances": [p]}],
                      "edges": []}
                r = ENS.llenar_umbrales_r2(kg, {}, {}, M, V, RCMP, pol, fase)
                salida[fase] = (kg["nodes"][0]["properties"]["umbrales"], r["resumen"])
    u_b, res_b = salida["r2b"]
    u_a, res_a = salida["r2a"]
    check("E", "integrado (cap::1.2, E0 r2b): r2b gana el valor y lo cuenta por TO y por nodo",
          len(u_b) == 1 and u_b[0].get("valor") == "5000000000" and res_b["unidad_desde_rotulo"]["elementos"] == 1
          and res_b["unidad_desde_rotulo"]["por_to"] == {"cap": 1}, json.dumps([u_b, res_b.get("unidad_desde_rotulo")],
                                                                              ensure_ascii=False))
    check("E", "integrado: r2a no cambia (sin valor, sin la clave del resumen)",
          u_a == [rel] and "unidad_desde_rotulo" not in res_a, json.dumps(u_a, ensure_ascii=False))

    def restr(i: str, desc: str, cid: str, umbrales=None) -> dict:
        p = prov("cap", cid, desc)
        props = {"tipo": "limite_cuantitativo", "descripcion": desc}
        if umbrales:
            props["umbrales"] = umbrales
        return {"id": i, "type": "Restriccion", "label": i, "properties": props, "provenance": p, "provenances": [p]}
    kg = {"nodes": [restr("R_sin", "Exigencia adicional de capital por riesgo gamma", "cap::6.6.3"),
                    restr("R_forzada", "Las compensaciones están sujetas a una escala", "cap::6.2.2.6"),
                    restr("R_otra_tabla", "Escala de otra tabla", "cap::9.9"),
                    restr("R_desc", "no podrá superar el 10%", "cap::9.8"),
                    restr("R_lista", "límite", "cap::9.7", umbrales=[h])], "edges": []}
    celdas = {"cap::6.2.2.6": [("cap::tabla037", ["Zona 1", "40%"])], "cap::9.9": [("cap::tabla999", ["30%"])],
              "cap::6.6.3": [("cap::tabla998", ["Opciones", "Delta"])]}
    r = ENS.marcar_umbral_no_cuantificable_r2b(kg, {}, celdas, RCMP)
    nd = {n["id"]: n.get("properties_no_definidas") or {} for n in kg["nodes"]}
    check("F", "sin cuantía (aunque haya celdas sin cuantía) → marca con «sin cuantía detectable» y el sha del detector",
          nd["R_sin"].get("umbral_no_cuantificable") is True
          and nd["R_sin"].get("umbral_no_cuantificable_motivo") == ENS.MOTIVO_SIN_CUANTIA
          and nd["R_sin"].get("umbral_no_cuantificable_detector_sha256") == r["resumen"]["detector_sha256"]
          and "umbral_no_cuantificable_tablas_forzadas_sha256" not in nd["R_sin"])
    check("F", "cuantías solo en cap::tabla037 (forzada a residual) → motivo propio y sha256 de la lista",
          nd["R_forzada"].get("umbral_no_cuantificable_motivo") == ENS.MOTIVO_TABLA_FORZADA
          and nd["R_forzada"].get("umbral_no_cuantificable_tablas_forzadas_sha256")
          == ENS.C.sha256_path(ENS.TABLAS_FORZADAS_R2B))
    check("F", "cuantías en otra tabla o en la descripción → sin marca, listadas; con lista → no se evalúa",
          not nd["R_otra_tabla"] and not nd["R_desc"] and not nd["R_lista"]
          and sorted(r["resumen"]["sin_marca_con_cuantia"]) == ["R_desc", "R_otra_tabla"]
          and r["resumen"]["marcados"] == 2, json.dumps(r["resumen"], ensure_ascii=False))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    grupo_a_d()
    grupo_e_f()
    total = sum(len(v) for v in RES.values())
    ok = sum(x["ok"] for v in RES.values() for x in v)
    for g, v in RES.items():
        for x in v:
            print(f"  [{'PASS' if x['ok'] else 'FAIL'}] {g} {x['caso']}" + ("" if x["ok"] else f" — {x['detalle']}"))
    print(f"pruebas T3-bis: {ok}/{total}")
    a.out.write_text(json.dumps({"total": total, "ok": ok, "grupos": RES}, ensure_ascii=False, indent=1) + "\n",
                     encoding="utf-8")
    return 0 if ok == total else 1


if __name__ == "__main__":
    sys.exit(main())
