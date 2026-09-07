"""
selftest_esqv3.py — U-ESQ-V3 fase 2: selftest propio de la unidad.

Patrón N/N, USD 0, sin red, corrible desde cwd ajeno. Bloques:

  B1 artefacto      esquema_v3_clases.json: forma, ids únicos, integridad
                    referencial de miembros y padres, y la guarda del laudo
                    (34 aristas · 12 huérfanos · 6/5/1).
  B2 paridad dev    los 5 roles del esquema v2 y sus 17 miembros pasan
                    byte-idénticos, y las 65 clases pasan en su orden.
  B3 laudos         ninguna fila `mas_amplio` produce miembro_de salvo la
                    excepción laudada; ningún miembro es de nivel instancia
                    ni es un rol; toda decisión lleva fundamento.
  B4 S15            FALLA sobre un grafo sintético con rol huérfano; PASA
                    sobre el grafo vigente; FALLA si la cuenta declarada no
                    coincide con la medida; PASA con la lista correcta;
                    FALLA si un miembro no es clase.
  B5 integración    ensamblar() sin perfil es BYTE-IDÉNTICO al histórico;
                    con el artefacto v3 inyecta y el grafo resultante deja a
                    los 30 roles con las aristas adjudicadas.
  B6 determinismo   regenerar el artefacto da el mismo sha256.
  B7 entregable     la generalización cierra, sus tres cifras están rotuladas,
                    la adoptada coincide con la adjudicación y el comando de
                    regeneración vive dentro del propio artefacto.

Uso:  python3 selftest_esqv3.py
"""

from __future__ import annotations

import copy
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

import adjudicar_miembros_v3 as ADJ
import comun_v3m as C

ok = 0
fallas: list[str] = []

KG_VIGENTE = (C.EXPERIMENT / "reextraccion_v2" / "corpus_v2" / "salida_r1" / "kg.json")
VALIDADOR = C.REPO / "scripts" / "shapes_validator.py"


def chk(cond: bool, etiqueta: str) -> None:
    global ok
    if cond:
        ok += 1
    else:
        fallas.append(etiqueta)


def _correr_validador(kg: Path, excepciones: Path | None, out: Path) -> tuple[str, str]:
    """Devuelve (veredicto, resumen) de S15 leídos de la TABLA RESUMEN, que es
    la salida estable del validador (`S15    PASS    <resumen>`)."""
    cmd = [sys.executable, str(VALIDADOR), "--kg", str(kg), "--out", str(out)]
    if excepciones:
        cmd += ["--excepciones", str(excepciones)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    tabla = r.stdout.split("=== TABLA RESUMEN ===")[-1]
    for linea in tabla.split("\n"):
        if linea.startswith("S15"):
            partes = linea.split(None, 2)
            return partes[1], (partes[2] if len(partes) > 2 else "")
    return "SIN_SALIDA", (r.stdout + r.stderr)[-300:]


def _grafo_sintetico(roles_miembros: dict[str, list[str]],
                     nivel_miembro: str = "clase") -> dict:
    """Grafo mínimo: un nodo por rol, un nodo por miembro, y las aristas."""
    nodes, edges, vistos = [], [], set()
    for rol, miembros in roles_miembros.items():
        nodes.append({"id": rol, "type": "Sujeto", "label": rol,
                      "properties": {"nivel": "rol"},
                      "provenance": {"source_doc": "x.pdf", "location": "1.1"}})
        for m in miembros:
            if m not in vistos:
                nodes.append({"id": m, "type": "Sujeto", "label": m,
                              "properties": {"nivel": nivel_miembro},
                              "provenance": {"source_doc": "x.pdf", "location": "1.1"}})
                vistos.add(m)
            edges.append({"source": m, "target": rol, "relation": "miembro_de",
                          "provenance": {"source_doc": "x.pdf", "location": "1.1"}})
    return {"nodes": nodes, "edges": edges}


def main() -> int:
    esq3 = json.loads(C.ESQUEMA_V3.read_text(encoding="utf-8"))
    adj = json.loads((C.UNIDAD / "adjudicacion_final_v3.json").read_text(encoding="utf-8"))
    v2 = C.esquema_v2()
    ix = C.catalogo_v3_index()

    # ---------------------------- B1 artefacto ---------------------------- #
    chk(esq3.get("version") == "3.0", "B1.1 version 3.0")
    chk(len(esq3["roles"]) == 35, f"B1.2 35 roles (vio {len(esq3['roles'])})")
    ids = [c["id"] for c in esq3["clases"]] + [r["id"] for r in esq3["roles"]]
    chk(len(ids) == len(set(ids)), "B1.3 ids únicos entre clases y roles")
    ids_clase = {c["id"] for c in esq3["clases"]}
    colgantes = [(r["id"], m) for r in esq3["roles"] for m in r["miembros"]
                 if m not in ids_clase]
    chk(not colgantes, f"B1.4 todo miembro existe como clase del artefacto ({colgantes})")
    padres = [(c["id"], c["padre"]) for c in esq3["clases"]
              if c.get("padre") and c["padre"] not in ids_clase]
    chk(not padres, f"B1.5 todo padre existe ({padres})")
    aristas = sum(len(r["miembros"]) for r in esq3["roles"])
    chk(aristas == 17 + 34, f"B1.6 aristas totales 17 dev + 34 nuevas (vio {aristas})")
    exc = esq3["excepciones_s15"]
    chk(exc["total"] == 12, f"B1.7 12 excepciones declaradas (vio {exc['total']})")
    chk(exc["por_causa"] == {"sin_id_en_catalogo": 6, "aplanamiento_rechazado": 5,
                             "instancia_rechazada": 1},
        f"B1.8 descomposición 6/5/1 (vio {exc['por_causa']})")
    chk(len(exc["roles"]) == exc["total"], "B1.9 la lista tiene tantas filas como su total")
    chk(all(r.get("causa") in exc["por_causa"] for r in exc["roles"]),
        "B1.10 cada excepción lleva una causa conocida")
    chk(all(r.get("remedio") for r in exc["roles"]),
        "B1.11 cada excepción lleva su remedio")
    sin_m = {r["id"] for r in esq3["roles"] if not r["miembros"]}
    chk(sin_m == {r["rol_id"] for r in exc["roles"]},
        "B1.12 los roles sin miembro son exactamente los declarados")
    chk(all(r.get("sin_miembro_adjudicable") for r in esq3["roles"] if not r["miembros"]),
        "B1.13 todo rol sin miembro lleva su causa en el propio rol")
    # B1.14–B1.17: las dos declaraciones que el laudo del cierre exige EN CAMPO.
    cec = [c for c in esq3["clases"] if c["id"].endswith("camara_electronica_de_compensacion")]
    chk(len(cec) == 1 and cec[0].get("padre_inferido") is True,
        "B1.14 la CEC declara padre_inferido: el padre se infirió y así se dice")
    chk(cec and cec[0]["padre"] == "Sujeto_sujeto_regulado",
        "B1.15 el padre de la CEC es el nodo general del grupo (el que omite, no el que afirma)")
    cv = [r for r in esq3["roles"] if r["id"].endswith("convca")]
    res = cv[0].get("residuo_declarado") if cv else None
    chk(isinstance(res, dict) and res.get("colectivo_operativo_del_to"),
        "B1.16 convca lleva su residuo EN CAMPO, no solo en prosa")
    an = (res or {}).get("anidacion_no_estricta") or {}
    chk(an.get("subclase_afectada") == "Sujeto_caja_de_credito"
        and an.get("ancla") == "ccbcra::1.1" and an.get("regla_3_no_mitiga"),
        "B1.17 el residuo nombra la subclase afectada, su ancla y por qué la regla 3 no mitiga")
    chk(an.get("subclase_afectada") in ids_clase,
        "B1.18 la subclase afectada es un id real del artefacto")

    # --------------------------- B2 paridad dev --------------------------- #
    chk(not ADJ.verificar_paridad_dev(esq3), "B2.1 los 5 roles dev pasan byte-idénticos")
    por_id = {r["id"]: r for r in esq3["roles"]}
    chk(sum(len(por_id[r["id"]]["miembros"]) for r in v2["roles"]) == 17,
        "B2.2 los 17 miembros dev intactos")
    chk([c["id"] for c in esq3["clases"]][:65] == [c["id"] for c in v2["clases"]],
        "B2.3 las 65 clases del v2 pasan en su orden")
    chk(len(esq3["clases"]) == 66, f"B2.4 66 clases = 65 + la CEC (vio {len(esq3['clases'])})")
    chk(C.ESQUEMA_V2.read_bytes() ==
        (C.EXPERIMENT / "grafo_v2" / "esquema_v2_clases.json").read_bytes(),
        "B2.5 el artefacto v2 sigue intacto")

    # ----------------------------- B3 laudos ------------------------------ #
    filas = [f for r in adj["roles"] for f in r["filas"]]
    chk(len(filas) == 69, f"B3.1 las 69 filas (vio {len(filas)})")
    chk(all(f.get("fundamento") for f in filas), "B3.2 toda fila lleva fundamento")
    amp = [f for f in filas if f["relacion"] == "mas_amplio"]
    acept_amp = [f for f in amp if f["decision"].startswith("aceptado")]
    chk(len(amp) == 8, f"B3.3 8 filas mas_amplio (vio {len(amp)})")
    chk(len(acept_amp) == 1 and acept_amp[0]["decision"] == "aceptado_enumeracion_parcial",
        "B3.4 laudo (a): solo la excepción laudada acepta una fila mas_amplio")
    conv = [r for r in adj["roles"] if r["to"] == "convca"][0]
    chk(conv["miembros"] == ["Sujeto_entidad_financiera"],
        "B3.5 convca queda con EF (laudo a.2)")
    cta = [r for r in adj["roles"] if r["to"] == "ctacor"][0]
    chk(cta["miembros"] == ["Sujeto_casa_de_cambio"],
        "B3.6 ctacor NO lleva EF y conserva casa_de_cambio (re-examinación revertida)")
    chk("ctacor" not in {e["to"] for e in adj["excepciones"]},
        "B3.7 ctacor no figura entre las excepciones: no es huérfano")
    inst = [f for f in filas if f["nivel_candidato"] == "instancia"]
    chk(len(inst) == 2 and all(f["decision"] == "rechazado_instancia" for f in inst),
        "B3.8 laudo (b): los 2 candidatos instancia rechazados")
    todos_miembros = {m for r in esq3["roles"] for m in r["miembros"]}
    chk(all(ix.get(m, {}).get("nivel") != "instancia" for m in todos_miembros),
        "B3.9 ningún miembro es de nivel instancia")
    chk(all(ix.get(m, {}).get("nivel") != "rol" for m in todos_miembros),
        "B3.10 ningún miembro es un rol")
    chk(adj["conteos"]["aristas_miembro_de"] == 34, "B3.11 guarda: 34 aristas")
    chk(adj["conteos"]["roles_huerfanos"] == 12, "B3.12 guarda: 12 huérfanos")

    # ------------------------------- B4 S15 -------------------------------- #
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        # (i) grafo sintético con un rol huérfano, sin lista declarada -> FAIL
        g = _grafo_sintetico({"Sujeto_rol_a": ["Sujeto_c1"], "Sujeto_rol_huerfano": []})
        p = td / "kg_huerfano.json"
        p.write_text(json.dumps(g, ensure_ascii=False), encoding="utf-8")
        ver, res = _correr_validador(p, None, td / "r1.md")
        chk(ver == "FAIL", f"B4.1 S15 FALLA con un rol huérfano no declarado ({ver}: {res[:80]})")
        chk("1 sin declarar" in res, f"B4.2 S15 cuenta el huérfano ({res[:80]})")

        # (ii) el mismo grafo con su lista declarada correcta -> PASS
        exc_ok = {"excepciones_s15": {"total": 1, "por_causa": {"sin_id_en_catalogo": 1},
                                      "roles": [{"rol_id": "Sujeto_rol_huerfano",
                                                 "causa": "sin_id_en_catalogo"}]}}
        pe = td / "exc_ok.json"
        pe.write_text(json.dumps(exc_ok, ensure_ascii=False), encoding="utf-8")
        ver, res = _correr_validador(p, pe, td / "r2.md")
        chk(ver == "PASS", f"B4.3 S15 PASA con el huérfano declarado ({ver}: {res[:80]})")

        # (iii) cuenta declarada que no coincide con la medida -> FAIL
        exc_mal = copy.deepcopy(exc_ok)
        exc_mal["excepciones_s15"]["total"] = 2
        exc_mal["excepciones_s15"]["por_causa"] = {"sin_id_en_catalogo": 2}
        pm = td / "exc_mal.json"
        pm.write_text(json.dumps(exc_mal, ensure_ascii=False), encoding="utf-8")
        ver, res = _correr_validador(p, pm, td / "r3.md")
        chk(ver == "FAIL", f"B4.4 S15 FALLA si la cuenta declarada no coincide ({ver}: {res[:80]})")

        # (iv) miembro que no es clase -> FAIL
        g2 = _grafo_sintetico({"Sujeto_rol_a": ["Sujeto_i1"]}, nivel_miembro="instancia")
        p2 = td / "kg_instancia.json"
        p2.write_text(json.dumps(g2, ensure_ascii=False), encoding="utf-8")
        ver, res = _correr_validador(p2, None, td / "r4.md")
        chk(ver == "FAIL" and "1 miembros que no son clase" in res,
            f"B4.5 S15 FALLA si un miembro no es clase del árbol ({ver}: {res[:80]})")

        # (v) grafo VIGENTE -> PASS
        if KG_VIGENTE.exists():
            ver, res = _correr_validador(KG_VIGENTE, None, td / "r5.md")
            chk(ver == "PASS", f"B4.6 S15 PASA sobre el grafo vigente ({ver}: {res[:80]})")
            chk("5 roles, 17 aristas miembro_de" in res,
                f"B4.7 S15 mide los 5 roles y 17 aristas del vigente ({res[:80]})")
        else:
            fallas.append("B4.6/B4.7 el grafo vigente no está en su ruta")

        # ------------------------ B5 integración -------------------------- #
        sys.path.insert(0, str(C.EXPERIMENT / "reextraccion_v2" / "corpus_v2"))
        import ensamblar_corpus as EC  # noqa: PLC0415

        grafos = {"a": {"nodes": [{"id": "Obligacion_x", "type": "Obligacion",
                                   "label": "x", "properties": {},
                                   "provenances": [{"to": "a", "punto": "1.1"}]}],
                        "edges": []}}
        base = EC.ensamblar(grafos, ("a",), None)
        base2 = EC.ensamblar(copy.deepcopy(grafos), ("a",), None, None)
        chk(base["kg_json"] == base2["kg_json"] and base["sha256_kg"] == base2["sha256_kg"],
            "B5.1 ensamblar() sin esqueleto: el parámetro nuevo por default no cambia nada")
        chk("esqueleto_v3" not in base["reporte"],
            "B5.2 sin perfil, el reporte no gana claves")

        conv3 = EC.ensamblar(copy.deepcopy(grafos), ("a",), None, C.ESQUEMA_V3)
        chk(conv3["sha256_kg"] != base["sha256_kg"],
            "B5.3 con el artefacto v3 el grafo cambia (la inyección corrió)")
        chk("esqueleto_v3" in conv3["reporte"], "B5.4 el reporte declara la inyección")
        kg3 = json.loads(conv3["kg_json"])
        ent = {}
        for e in kg3["edges"]:
            if e["relation"] == "miembro_de":
                ent.setdefault(e["target"], []).append(e["source"])
        chk(len(kg3["nodes"]) == 1 + 66 + 35,
            f"B5.5 nodos = 1 del grafo + 66 clases + 35 roles (vio {len(kg3['nodes'])})")
        chk(sum(len(v) for v in ent.values()) == 51,
            f"B5.6 51 aristas miembro_de = 17 dev + 34 nuevas "
            f"(vio {sum(len(v) for v in ent.values())})")
        nuevos = [r for r in esq3["roles"] if r["id"].startswith("Sujeto_rol_alcance_")
                  and r["id"] != "Sujeto_rol_alcance_capmin"]
        chk(len(nuevos) == 30, f"B5.7 30 roles nuevos en el artefacto (vio {len(nuevos)})")
        chk(all(sorted(ent.get(r["id"], [])) == sorted(r["miembros"]) for r in nuevos),
            "B5.8 cada rol nuevo quedó con exactamente sus miembros adjudicados")
        chk(all(not ent.get(r["rol_id"]) for r in exc["roles"]),
            "B5.9 los 12 declarados quedaron sin arista, como declara el artefacto")
        # el grafo inyectado pasa S15 con su lista
        pk = td / "kg_v3.json"
        pk.write_text(conv3["kg_json"], encoding="utf-8")
        ver, res = _correr_validador(pk, C.ESQUEMA_V3, td / "r6.md")
        chk(ver == "PASS",
            f"B5.10 el grafo inyectado PASA S15 con su lista declarada ({ver}: {res[:90]})")
        chk("12 huérfanos (12 declarados, 0 sin declarar)" in res,
            f"B5.11 S15 reporta la lista con su cuenta ({res[:110]})")

    # --------------------------- B6 determinismo -------------------------- #
    a2 = ADJ.adjudicar()
    esq_b = ADJ.construir_esquema_v3(a2)
    sha_a = hashlib.sha256(C.ESQUEMA_V3.read_bytes()).hexdigest()
    sha_b = hashlib.sha256(
        json.dumps(esq_b, ensure_ascii=False, indent=1).encode("utf-8")).hexdigest()
    chk(sha_a == sha_b, "B6.1 regenerar el artefacto da el mismo sha256")
    chk(not ADJ.verificar_guarda(a2), "B6.2 la guarda dura vuelve a pasar al regenerar")

    # ---------------------- B7 entregable de generalización ---------------- #
    gen = json.loads((C.UNIDAD / "generalizacion_catalogo_v3.json").read_text(encoding="utf-8"))
    chk(gen["denominador"] == 69, f"B7.1 denominador 69 (vio {gen['denominador']})")
    chk(all(e["cierra"] for e in gen["escenarios"].values()),
        "B7.2 los tres escenarios cierran (veraz + descarte = total)")
    adopt = [e for e in gen["escenarios"].values() if e["adoptada"]]
    chk(len(adopt) == 1, f"B7.3 exactamente un escenario marcado ADOPTADA (vio {len(adopt)})")
    a0 = adopt[0]
    chk(a0["veraz"] == adj["conteos"]["aristas_miembro_de"],
        f"B7.4 la cifra adoptada ({a0['veraz']}) coincide con las aristas nuevas "
        f"({adj['conteos']['aristas_miembro_de']})")
    chk(a0["ausencia_de_concepto"] + a0["granularidad_equivocada"] == a0["descarte_total"],
        "B7.5 el descarte partido en dos suma el descarte total")
    chk(a0["granularidad_equivocada"] ==
        adj["conteos"]["filas_por_decision"].get("rechazado_aplanamiento", 0)
        + adj["conteos"]["filas_por_decision"].get("rechazado_instancia", 0),
        "B7.6 la granularidad equivocada es aplanamiento + instancia de la adjudicación")
    chk(a0["ausencia_de_concepto"] ==
        adj["conteos"]["filas_por_decision"].get("sin_id_en_catalogo", 0),
        "B7.7 la ausencia de concepto son los colectivos sin id de la adjudicación")
    chk(len(gen["escenarios"]) == 3, "B7.8 las tres cifras se conservan, no solo la adoptada")
    md = (C.UNIDAD / "generalizacion_catalogo_v3.md").read_text(encoding="utf-8")
    chk(gen["comando"] in md, "B7.9 el comando de regeneración está DENTRO del artefacto")
    chk("96,9" in md and "main.tex:679" in md,
        "B7.10 la advertencia de no-comparabilidad viaja con la cifra")

    total = ok + len(fallas)
    print(f"selftest U-ESQ-V3: {ok}/{total}")
    for f in fallas:
        print("  FALLA:", f)
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(main())
