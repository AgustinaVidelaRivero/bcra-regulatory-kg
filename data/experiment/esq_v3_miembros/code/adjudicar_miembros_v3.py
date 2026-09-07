"""
adjudicar_miembros_v3.py — U-ESQ-V3 fase 2: aplica los laudos, genera
esquema_v3_clases.json y la tabla final con su fundamento fila por fila.

LOS LAUDOS, EXPRESADOS EN CÓDIGO (no transcritos a una tabla tipeada: la
decisión de cada fila se DERIVA de su clasificación medida en la fase 1 más
la regla laudada, y por eso el recompute es una verificación real):

  laudo (a) — NO SE APLANA. Una fila `mas_amplio` no produce `miembro_de`.
    Fundamento: la firma es miembro_de (Clase → Rol) y la regla de herencia 2
    hace que un `aplica_a` hacia el rol alcance a CADA MIEMBRO, desde donde la
    regla 1 desciende a TODA SUBCLASE. Aplanar no es imprecisión: hace que el
    grafo afirme que una norma D-SIB alcanza a toda entidad financiera y a
    cada una de sus subclases. Es falsedad en campo estructurado, y el
    principio §1 del laudo del esquema congelado manda RETIRAR eso, no
    aceptarlo con residuo. La regla 3 (bloqueo por excepción) no rescata
    ninguna: solo corta herencia cuando la excepción nombra una SUBCLASE, y
    las filas rechazadas son predicados calificadores (designación D-SIB,
    participación en el pago de beneficios, ofrecer cuentas a la vista,
    primer grado, sometimiento a la LEF), no subclases excluidas.

    EXCEPCIÓN LAUDADA, una sola: `convca` no es aplanamiento sino ENUMERACIÓN
    PARCIAL — el pasaje dice «a solicitud de las entidades financieras y otras
    habilitadas», donde las EF pertenecen al colectivo sin condición y lo que
    falta son las «otras», que no tienen id. Eso es omisión con residuo
    declarado, que el principio §1 acepta. La ambigüedad del parseo
    alternativo queda REGISTRADA en los residuos, no resuelta en silencio.

    `ctacor` fue propuesto como segunda excepción y quedó REVERTIDO: la
    verificación de esta unidad mostró que «del país» es recorte real (ver
    verificacion_reexaminaciones_f2.md). No produce miembro_de.

  laudo (b) — INSTANCIAS AFUERA, por firma del esquema. miembro_de es
    Clase → Rol; admitir una instancia es cambiar la firma del esquema
    congelado, que es laudo de la autora y jamás efecto de esta unidad.

  laudo (c) — la lista de excepciones de S15 se GENERA acá, con una causa por
    rol, y su cuenta es la que S15 compara contra lo medido.

GUARDA DURA: 34 aristas · 12 roles huérfanos · 6/5/1 por causa. Si el
recompute no da eso, el script FRENA sin escribir nada.

FRONTERAS: `esquema_v2_clases.json` se lee y NUNCA se escribe; el generador
verifica que los 5 roles dev y sus 17 miembros pasan byte-idénticos al
artefacto nuevo. El catálogo v3 sellado se importa, solo lectura. USD 0.

Uso:  python3 adjudicar_miembros_v3.py [--out DIR]
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import comun_v3m as C

# --------------------------------------------------------------------------- #
# Excepción laudada al laudo (a): el único TO cuyo colectivo `mas_amplio` se
# adjudica igual, por ser enumeración parcial y no aplanamiento.
# --------------------------------------------------------------------------- #
ENUMERACION_PARCIAL = {"convca"}

# Causas de la lista de excepciones de S15 (laudo (c)); el remedio viaja con
# cada una porque una lista sin causa dice cuántos faltan y no qué hacer.
REMEDIO = {
    "sin_id_en_catalogo": ("abrir id en el catálogo, que es re-sello del prefijo v3 "
                           "y unidad propia"),
    "aplanamiento_rechazado": "una clase más específica en el catálogo",
    "instancia_rechazada": ("cambiar la firma de miembro_de, que es laudo de la autora "
                            "sobre el esquema congelado"),
}

# Única adición del catálogo v3 que entra al árbol del artefacto nuevo, por
# ser el único miembro adjudicado ausente de esquema_v2_clases.json.
#
# EL PADRE SE INFIRIÓ, y así se declara. Ningún documento dice de qué es
# subclase la CEC: el bloque sellado la coloca en el grupo «## Sujetos
# regulados» y nada más. `Sujeto_sujeto_regulado` se elige POR ANALOGÍA con
# su contraste declarado —la definición v3 de la CEC dice expresamente «no es
# la entidad de contraparte central (CCP)», y el v2 cuelga
# `Sujeto_entidad_de_contraparte_central` directamente de esa raíz— y porque
# es el nodo GENERAL del grupo: el que OMITE en vez de afirmar falso. Un
# padre más específico afirmaría una pertenencia que ninguna norma declara.
# Que la analogía sea buena y el resultado seguro no la convierte en lectura.
ADICION_NECESARIA = {
    "id": "Sujeto_camara_electronica_de_compensacion",
    "nivel": "clase",
    "padre": "Sujeto_sujeto_regulado",
    "padre_inferido": True,
    "disjunta_con": [],
    "provenance": {"source_doc": "esquema_v3_clases.json",
                   "location": "adición del catálogo v3 (laudo B5.4 fase 1)"},
}

# Residuo declarado de convca, EN CAMPO y no solo en prosa (un residuo que
# vive en un párrafo es invisible para quien lea el recurso después).
RESIDUO_CONVCA = {
    "colectivo_operativo_del_to": "titulares de cuenta corriente en el BCRA",
    "colectivo_operativo_sin_id": True,
    "colectivo_faltante": "otras habilitadas a conversión cambiaria",
    "lectura_adoptada": ("llana: «las entidades financieras» y «otras habilitadas» son dos "
                         "colectivos coordinados. Laudo de la autora, no resolución de esta "
                         "unidad ni del TO, que no la resuelve"),
    "parseo_alternativo_registrado": ("«(EF y otras) habilitadas»: el calificador alcanzaría "
                                      "también a las EF y volvería a ser aplanamiento"),
    "anidacion_no_estricta": {
        "ancla": "ccbcra::1.1",
        "regla_general": ("las entidades financieras DEBEN mantener cuenta corriente en el "
                          "BCRA, de modo que el colectivo operativo del TO las contiene"),
        "subclase_afectada": "Sujeto_caja_de_credito",
        "motivo": ("la misma cláusula de ccbcra::1.1 hace la cuenta OPTATIVA para las cajas de "
                   "crédito (Ley 25.782), que son entidades financieras según el catálogo — de "
                   "modo que la anidación EF ⊆ titulares no es estricta"),
        "regla_3_no_mitiga": ("el bloqueo por excepción corta la herencia cuando una Excepcion "
                              "nombra una subclase, y esta la nombra — pero esa excepción vive "
                              "en ccbcra, NO en convca, así que no hay Excepcion en el alcance "
                              "de convca que la dispare. NO se fabrica una: inventar una "
                              "Excepcion para que la regla 3 corte sería afirmar en el grafo "
                              "algo que la norma de convca no dice"),
    },
    "remedio": ("abrir id para «titulares de cuenta corriente en el BCRA» — es un caso más del "
                "cubo de colectivos sin id, y por lo tanto re-sello del prefijo v3 y unidad "
                "propia (ítem de backlog)"),
}


def _location(chunk_id: str) -> str:
    """Location legible desde el chunk_id, con el patrón del artefacto v2
    («Punto 1.1.2», «Sección 2»). No inventa: reformatea la unidad."""
    partes = chunk_id.split("::")
    u = partes[1] if len(partes) > 1 else ""
    if u.startswith("S") and u[1:].isdigit():
        return f"Sección {u[1:]}"
    return f"Punto {u}"


def adjudicar() -> dict:
    v3 = C.cargar_v3()
    ix = C.catalogo_v3_index()
    cand = json.loads((C.UNIDAD / "candidatos_miembros_v3.json").read_text(encoding="utf-8"))

    roles, excepciones = [], []
    for r in cand["roles"]:
        filas = []
        for c in r["candidatos"]:
            sid = c["candidato_id"]
            if not sid:
                dec, fund = "sin_id_en_catalogo", (
                    "el colectivo que el pasaje nombra no tiene id en el catálogo v3; el "
                    "matcheo no sube al padre porque eso sería colapsar a la madre")
            elif c["nivel_candidato"] == "instancia":
                dec, fund = "rechazado_instancia", (
                    "laudo (b): miembro_de es Clase → Rol; admitir una instancia cambia la "
                    "firma del esquema congelado y eso es laudo de la autora sobre el esquema")
            elif c["relacion"] == "mas_amplio":
                if r["to"] in ENUMERACION_PARCIAL:
                    dec, fund = "aceptado_enumeracion_parcial", (
                        "laudo (a), excepción: no es aplanamiento sino enumeración parcial — el "
                        "colectivo pertenece sin condición y lo que falta son las «otras», que "
                        "no tienen id; omisión con residuo declarado, que el principio §1 acepta")
                else:
                    dec, fund = "rechazado_aplanamiento", (
                        "laudo (a): el candidato es la clase madre del colectivo; por la regla de "
                        "herencia 2 el grafo afirmaría la norma sobre toda la clase y, por la "
                        "regla 1, sobre cada subclase — falsedad en campo estructurado")
            elif c["relacion"] == "recorte_declarado":
                dec, fund = "aceptado_recorte_declarado", (
                    "el núcleo del colectivo coincide con el del id; la aclaración que el "
                    "colectivo trae no recorta el sujeto (sección, ley que lo define, o base de "
                    "observancia), verificada contra el pasaje")
            else:
                dec, fund = "aceptado_identico", (
                    "el colectivo y el label del id coinciden")
            filas.append({**c, "decision": dec, "fundamento": fund})

        miembros = sorted({f["candidato_id"] for f in filas
                           if f["decision"].startswith("aceptado")})
        rol = {
            "id": r["rol_id"], "to": r["to"], "label": r["label_rol"],
            "cita_chunk_id": r["cita_chunk_id"], "paginas": r["paginas"],
            "miembros": miembros, "filas": filas,
        }
        if not miembros:
            decs = {f["decision"] for f in filas}
            if decs == {"sin_id_en_catalogo"}:
                causa = "sin_id_en_catalogo"
            elif "rechazado_instancia" in decs and "rechazado_aplanamiento" not in decs:
                causa = "instancia_rechazada"
            else:
                causa = "aplanamiento_rechazado"
            rol["causa_sin_miembro"] = causa
            excepciones.append({"rol_id": r["rol_id"], "to": r["to"], "causa": causa,
                                "remedio": REMEDIO[causa],
                                "colectivos": [f["colectivo"] for f in filas]})
        roles.append(rol)

    por_causa = {k: sorted(e["to"] for e in excepciones if e["causa"] == k)
                 for k in REMEDIO}
    return {
        "unidad": "U-ESQ-V3", "fase": 2,
        "sello_v3": {"sha256": v3.PREFIJO_SHA256_V3, "hash": v3.PREFIJO_HASH_V3},
        "roles": roles,
        "excepciones": sorted(excepciones, key=lambda e: (e["causa"], e["to"])),
        "conteos": {
            "roles": len(roles),
            "aristas_miembro_de": sum(len(r["miembros"]) for r in roles),
            "roles_huerfanos": len(excepciones),
            "por_causa": {k: len(v) for k, v in por_causa.items()},
            "roles_por_causa": por_causa,
            "filas_por_decision": {
                d: sum(1 for r in roles for f in r["filas"] if f["decision"] == d)
                for d in sorted({f["decision"] for r in roles for f in r["filas"]})},
        },
        "_ix": ix,
    }


def verificar_guarda(a: dict) -> list[str]:
    """Guarda dura del laudo. Devuelve la lista de violaciones (vacía = pasa)."""
    k, f = a["conteos"], []
    if k["aristas_miembro_de"] != 34:
        f.append(f"aristas {k['aristas_miembro_de']} != 34")
    if k["roles_huerfanos"] != 12:
        f.append(f"roles huérfanos {k['roles_huerfanos']} != 12")
    esperado = {"sin_id_en_catalogo": 6, "aplanamiento_rechazado": 5,
                "instancia_rechazada": 1}
    if k["por_causa"] != esperado:
        f.append(f"descomposición por causa {k['por_causa']} != {esperado}")
    if sum(k["por_causa"].values()) != k["roles_huerfanos"]:
        f.append("la suma por causa no reproduce el total de huérfanos")
    if k["roles"] != 30:
        f.append(f"roles {k['roles']} != 30")
    return f


def construir_esquema_v3(a: dict) -> dict:
    """Artefacto nuevo. Base: esquema_v2_clases.json EN SOLO LECTURA.

    Decisiones declaradas (van escritas en el propio artefacto):
      - las 65 clases del v2 pasan TAL CUAL, sin una edición;
      - se agrega UNA sola entrada, la única adición del catálogo v3 que
        aparece como miembro adjudicado y falta en el v2 (la CEC). Nada más
        se agrega: el artefacto no redefine el árbol;
      - los 5 retiros del catálogo v3 NO se quitan del árbol. El retiro es del
        ENUM del prompt —qué puede elegir el extractor—, no del esqueleto, y
        quitarlos cambiaría el árbol sin laudo que lo pida;
      - los 5 roles dev pasan byte-idénticos, y eso se VERIFICA.
    """
    v2 = C.esquema_v2()
    clases = [dict(c) for c in v2["clases"]]
    ix = a["_ix"]
    ad = dict(ADICION_NECESARIA)
    entrada = {"id": ad["id"], "label": ix[ad["id"]]["label"], "nivel": ad["nivel"],
               "padre": ad["padre"], "padre_inferido": ad["padre_inferido"],
               "disjunta_con": ad["disjunta_con"],
               "alias": list(ix[ad["id"]]["alias"]), "provenance": ad["provenance"]}
    clases.append(entrada)

    roles = [dict(r) for r in v2["roles"]]
    for r in a["roles"]:
        nuevo = {"id": r["id"], "label": r["label"], "nivel": "rol",
                 "to": f"{r['to']}.pdf", "miembros": list(r["miembros"]),
                 "provenance": {"source_doc": f"{r['to']}.pdf",
                                "location": _location(r["cita_chunk_id"])}}
        if not r["miembros"]:
            nuevo["sin_miembro_adjudicable"] = r["causa_sin_miembro"]
        if r["to"] in ENUMERACION_PARCIAL:
            nuevo["residuo_declarado"] = dict(RESIDUO_CONVCA)
        roles.append(nuevo)

    return {
        "version": "3.0",
        "deriva_de": {
            "esquema_v2": "data/experiment/grafo_v2/esquema_v2_clases.json (SOLO LECTURA)",
            "catalogo_v3": {"modulo": "data/experiment/b54_catalogo_v3/code/prompt_v3_b54.py",
                            **a["sello_v3"]},
            "unidad": "U-ESQ-V3",
        },
        "notas_de_construccion": [
            "Las 65 clases del esquema v2 pasan sin una sola edición; el artefacto v2 no se "
            "toca y el grafo vigente sigue reproducible.",
            "Se agrega UNA entrada: Sujeto_camara_electronica_de_compensacion, el único miembro "
            "adjudicado que falta en el v2. La clase entra por el laudo B5.4 F1.4. SU PADRE SE "
            "INFIRIÓ, y lleva la marca padre_inferido: ningún documento declara de qué es "
            "subclase la CEC — el bloque sellado solo la coloca en el grupo «Sujetos regulados». "
            "Sujeto_sujeto_regulado se eligió POR ANALOGÍA con su contraste declarado (la "
            "definición v3 dice «no es la entidad de contraparte central (CCP)», y el v2 cuelga "
            "esa CCP directamente de esa raíz) y por ser el nodo GENERAL del grupo: el que OMITE "
            "en vez de afirmar falso. Que la analogía sea buena y el resultado seguro no la "
            "convierte en lectura.",
            "El rol de convca lleva su residuo_declarado EN CAMPO: el colectivo operativo del TO "
            "(«titulares de cuenta corriente en el BCRA», sin id), el faltante, la lectura "
            "adoptada con su parseo alternativo registrado, y la anidación no estricta con la "
            "subclase afectada (Sujeto_caja_de_credito) y por qué la regla 3 no la mitiga.",
            "Los 5 retiros del catálogo v3 NO se quitan del árbol: el retiro es del enum del "
            "prompt (qué puede elegir el extractor), no del esqueleto, y quitarlos cambiaría el "
            "árbol sin laudo que lo pida.",
            "Los 5 roles del esquema v2 y sus 17 miembros pasan byte-idénticos; el generador lo "
            "verifica y FRENA si alguno no pasa.",
            "Un rol sin miembro adjudicable lleva el campo sin_miembro_adjudicable con su causa "
            "y figura en excepciones_s15; no se le inventa un miembro.",
        ],
        "clases": clases,
        "roles": roles,
        "excepciones_s15": {
            "enunciado": ("roles sin miembro adjudicable, declarados con su causa; S15 exige "
                          "que la cuenta declarada coincida con la medida"),
            "total": len(a["excepciones"]),
            "por_causa": a["conteos"]["por_causa"],
            "remedios": REMEDIO,
            "roles": a["excepciones"],
        },
    }


def verificar_paridad_dev(esq3: dict) -> list[str]:
    """Los 5 roles dev y sus 17 miembros, byte-idénticos al artefacto sellado.
    Divergencia = FRENO: serían dos fuentes de la misma verdad en desacuerdo."""
    v2 = C.esquema_v2()
    f = []
    por_id = {r["id"]: r for r in esq3["roles"]}
    for r2 in v2["roles"]:
        r3 = por_id.get(r2["id"])
        if r3 is None:
            f.append(f"el rol dev {r2['id']} no está en el artefacto v3")
            continue
        if json.dumps(r2, ensure_ascii=False, sort_keys=True) != \
           json.dumps(r3, ensure_ascii=False, sort_keys=True):
            f.append(f"el rol dev {r2['id']} NO pasa byte-idéntico")
    n2 = sum(len(r["miembros"]) for r in v2["roles"])
    n3 = sum(len(por_id[r["id"]]["miembros"]) for r in v2["roles"] if r["id"] in por_id)
    if n2 != 17 or n3 != 17:
        f.append(f"miembros dev: v2={n2} v3={n3} (esperado 17 y 17)")
    ids2 = [c["id"] for c in v2["clases"]]
    ids3 = [c["id"] for c in esq3["clases"]]
    if ids3[:len(ids2)] != ids2:
        f.append("las 65 clases del v2 no pasan en su orden original")
    if len(ids3) != len(ids2) + 1:
        f.append(f"clases {len(ids3)} != {len(ids2)} + 1")
    return f


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=C.UNIDAD)
    args = ap.parse_args()

    a = adjudicar()
    viol = verificar_guarda(a)
    if viol:
        print("FRENO — la guarda dura del laudo no pasa; no se escribió nada:")
        for v in viol:
            print("  -", v)
        return 1

    esq3 = construir_esquema_v3(a)
    viol = verificar_paridad_dev(esq3)
    if viol:
        print("FRENO — los 5 roles dev no pasan byte-idénticos; no se escribió nada:")
        for v in viol:
            print("  -", v)
        return 1

    ix = a.pop("_ix")
    (args.out / "esquema_v3_clases.json").write_text(
        json.dumps(esq3, ensure_ascii=False, indent=1), encoding="utf-8")
    (args.out / "adjudicacion_final_v3.json").write_text(
        json.dumps(a, ensure_ascii=False, indent=1), encoding="utf-8")
    a["_ix"] = ix

    k = a["conteos"]
    print(f"aristas miembro_de : {k['aristas_miembro_de']}  (guarda 34)")
    print(f"roles huérfanos    : {k['roles_huerfanos']}  (guarda 12)")
    print(f"por causa          : {k['por_causa']}  (guarda 6/5/1)")
    print(f"filas por decisión : {k['filas_por_decision']}")
    print(f"roles dev byte-idénticos: 5/5 · miembros dev 17/17")
    print(f"-> {args.out / 'esquema_v3_clases.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
