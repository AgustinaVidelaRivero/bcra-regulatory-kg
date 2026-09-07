"""
verificador_f1.py — U-ESQ-V3: verificador propio de los artefactos de la
fase 1. Patrón N/N, USD 0, sin red, corrible desde cwd ajeno.

No verifica la ADJUDICACIÓN (que es de la autora): verifica que el material
sobre el que la autora va a decidir sea correcto, completo y recomputable —
que los colectivos vengan del módulo sellado y no de una lista tipeada acá,
que las citas apunten a chunks que existen, que los candidatos sean ids
reales del catálogo, que ningún candidato sea un rol, que los conteos de la
tabla cierren contra el JSON, y que todo el pipeline sea determinístico.

Uso:  python3 verificador_f1.py
"""

from __future__ import annotations

import hashlib
import json
import sys

import candidatos_miembros_v3 as CM
import comun_v3m as C

ok = 0
fallas: list[str] = []


def chk(cond: bool, etiqueta: str) -> None:
    global ok
    if cond:
        ok += 1
    else:
        fallas.append(etiqueta)


def main() -> int:
    v3 = C.cargar_v3()
    ix = C.catalogo_v3_index()
    d = json.loads((C.UNIDAD / "candidatos_miembros_v3.json").read_text(encoding="utf-8"))

    # --- B1. Candados del catálogo sellado (el material sale de ahí) ------- #
    chk(v3.PREFIJO_SHA256_V3 ==
        "35e88c2dd0a2920302c29005b08ab9689405606d4bd5fcf8fb7ce807b1a3c512",
        "B1.1 sha del prefijo v3")
    chk(v3.PREFIJO_HASH_V3 == "54a111e2175f", "B1.2 hash del prefijo v3")
    chk(len(ix) == 102, f"B1.3 catálogo v3 = 102 entradas (vio {len(ix)})")
    niveles = {n: sum(1 for v in ix.values() if v["nivel"] == n)
               for n in ("clase", "instancia", "rol")}
    chk(niveles == {"clase": 62, "instancia": 5, "rol": 35},
        f"B1.4 composición del catálogo (vio {niveles})")
    chk(len(v3.ROLES_V3) == 30, f"B1.5 ROLES_V3 = 30 (vio {len(v3.ROLES_V3)})")

    # --- B2. El defecto que la unidad cierra sigue ahí -------------------- #
    nuevos = [v3.rol_id_de(to) for to, _, _ in v3.ROLES_V3]
    tabla = v3.ROL_POR_TO_V3
    vacios = sum(1 for to, _, _ in v3.ROLES_V3
                 if tabla[f"{to}.pdf"]["miembros_ids"] == [])
    chk(vacios == 30, f"B2.1 los 30 roles nuevos con miembros_ids vacío (vio {vacios})")
    esq2 = C.esquema_v2()
    ids_v2 = {c["id"] for c in esq2["clases"]} | {r["id"] for r in esq2["roles"]}
    chk(not (set(nuevos) & ids_v2), "B2.2 ninguno de los 30 está en esquema_v2_clases.json")
    chk(len(esq2["roles"]) == 5 and len(esq2["clases"]) == 65,
        "B2.3 esquema v2 = 65 clases + 5 roles")

    # --- B3. Los 17 miembros vigentes y su tipo (base de S15) ------------- #
    nivel_v2 = {c["id"]: c["nivel"] for c in esq2["clases"]}
    miembros_v2 = [m for r in esq2["roles"] for m in r["miembros"]]
    chk(len(miembros_v2) == 17, f"B3.1 17 miembros dev (vio {len(miembros_v2)})")
    chk(all(nivel_v2.get(m) == "clase" for m in miembros_v2),
        "B3.2 los 17 miembros vigentes son todos de nivel clase")
    chk(all(m in nivel_v2 for m in miembros_v2),
        "B3.3 los 17 miembros existen como entrada del catálogo")

    # --- B4. Procedencia del material de la tabla ------------------------- #
    colectivos_json = [(r["to"], c["colectivo"])
                       for r in d["roles"] for c in r["candidatos"]]
    colectivos_sello = [(to, m) for to, _, ms in v3.ROLES_V3 for m in ms]
    chk(colectivos_json == colectivos_sello,
        "B4.1 los colectivos de la tabla son EXACTAMENTE los del módulo sellado, en orden")
    chk([r["to"] for r in d["roles"]] == [to for to, _, _ in v3.ROLES_V3],
        "B4.2 los 30 TOs y su orden vienen del módulo sellado")
    chk(all(r["label_rol"] == lab
            for r, (_, lab, _) in zip(d["roles"], v3.ROLES_V3)),
        "B4.3 los labels de rol vienen del módulo sellado")

    # --- B5. Las citas apuntan a chunks reales de e0_dry ------------------ #
    sin_chunk = [r["to"] for r in d["roles"] if not r["pasaje"]]
    chk(not sin_chunk, f"B5.1 las 30 citas resuelven a un chunk de e0_dry (fallan {sin_chunk})")
    malas = [r["to"] for r in d["roles"]
             if r["cita_chunk_id"].split("::", 1)[0] != r["to"]]
    chk(not malas, f"B5.2 cada cita pertenece a su propio TO (fallan {malas})")
    chk(all(C.chunk_de(r["cita_chunk_id"])["texto"] == r["pasaje"] for r in d["roles"]),
        "B5.3 el pasaje del JSON es el texto del chunk, sin editar")

    # --- B6. Los candidatos son ids reales, y nunca un rol ---------------- #
    cands = [c for r in d["roles"] for c in r["candidatos"] if c["candidato_id"]]
    chk(all(c["candidato_id"] in ix for c in cands),
        "B6.1 todo candidato es un id del catálogo v3")
    chk(all(ix[c["candidato_id"]]["nivel"] != "rol" for c in cands),
        "B6.2 ningún candidato es un rol (un rol no es miembro de otro rol)")
    chk(all(c["nivel_candidato"] == ix[c["candidato_id"]]["nivel"] for c in cands),
        "B6.3 el nivel reportado coincide con el del catálogo")
    chk(all(c["label_candidato"] == ix[c["candidato_id"]]["label"] for c in cands),
        "B6.4 el label reportado coincide con el del catálogo")
    chk(all(c["relacion"] == "mas_amplio" for c in cands
            if c["regla"].startswith("R5")),
        "B6.5 toda salida de R5 va etiquetada mas_amplio")
    chk(all(c["regla"].startswith("R5") for c in cands
            if c["relacion"] == "mas_amplio"),
        "B6.6 solo R5 produce mas_amplio")

    # --- B7. Las marcas cubren lo que dicen cubrir ------------------------ #
    for r in d["roles"]:
        cs = r["candidatos"]
        esperadas = []
        if len(cs) > 1:
            esperadas.append("MULTI_SUJETO")
        if any(not c["candidato_id"] for c in cs):
            esperadas.append("SIN_ID_EN_CATALOGO")
        if any(c["relacion"] == "mas_amplio" for c in cs):
            esperadas.append("APLANA_A_LA_MADRE")
        if any(c["nivel_candidato"] == "instancia" for c in cs):
            esperadas.append("CANDIDATO_INSTANCIA")
        chk(r["marcas"] == esperadas,
            f"B7 marcas de {r['to']}: {r['marcas']} != {esperadas}")

    # --- B8. Los casos que el mandato nombra están marcados --------------- #
    por_to = {r["to"]: r for r in d["roles"]}
    for to in ("rrci", "ccbcra"):
        chk("MULTI_SUJETO" in por_to[to]["marcas"],
            f"B8 {to} marcado MULTI_SUJETO (caso que el mandato nombra)")
    chk(len(por_to["rrci"]["candidatos"]) == 3, "B8.3 rrci con sus 3 colectivos")
    chk(len(por_to["ccbcra"]["candidatos"]) == 3, "B8.4 ccbcra con sus 3 colectivos")

    # --- B9. Los conteos del artefacto cierran ---------------------------- #
    k = CM.conteos(d)
    chk(k["colectivos"] == sum(len(r["candidatos"]) for r in d["roles"]),
        "B9.1 total de colectivos")
    chk(k["con_candidato"] + k["sin_id_en_catalogo"] == k["colectivos"],
        "B9.2 con candidato + sin id = total")
    chk(sum(k["por_relacion"].values()) == k["colectivos"],
        "B9.3 la partición por relacion suma el total")
    chk(k["por_relacion"]["—"] == k["sin_id_en_catalogo"],
        "B9.4 los sin relacion son exactamente los sin id")
    chk(k["roles_con_marca"] + k["roles_limpios"] == 30,
        "B9.5 roles con marca + limpios = 30")
    chk(d.get("conteos") == k, "B9.6 los conteos del JSON son los recomputados")

    # --- B10. Determinismo: reconstruir da lo mismo ----------------------- #
    d2 = CM.construir()
    d2["conteos"] = CM.conteos(d2)
    a = hashlib.sha256(json.dumps(d, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
    b = hashlib.sha256(json.dumps(d2, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
    chk(a == b, "B10.1 construir() es determinístico (sha del JSON)")
    chk(hashlib.sha256(CM.render_md(d).encode()).hexdigest() ==
        hashlib.sha256((C.UNIDAD / "tabla_adjudicacion_miembros_v3.md")
                       .read_text(encoding="utf-8").encode()).hexdigest(),
        "B10.2 la tabla .md es la que render_md produce")

    # --- B11. Guarda 1 del bloque: el conteo de la partición -------------- #
    part = json.loads((C.EXPERIMENT / "segmentacion_84" / "b584_particion" /
                       "particion_152.json").read_text(encoding="utf-8"))
    ag = part["agregados"]
    chk(ag["reconocido_pleno"]["unidades"] == 9266,
        f"B11.1 unidades de reconocidos plenos = 9.266 "
        f"(vio {ag['reconocido_pleno']['unidades']})")
    chk(sum(ag[k2]["tos"] for k2 in ag) == 152, "B11.2 la partición suma 152 TOs")
    chk(sum(ag[k2]["unidades"] for k2 in ag) == 9324,
        "B11.3 las unidades de la partición suman 9.324")

    # --- B12. Fronteras: nada sellado fue tocado -------------------------- #
    chk((C.ESQUEMA_V2).read_bytes() ==
        (C.EXPERIMENT / "grafo_v2" / "esquema_v2_clases.json").read_bytes(),
        "B12.1 esquema_v2_clases.json legible e intacto en su ruta")
    chk(not C.ESQUEMA_V3.exists(),
        "B12.2 esquema_v3_clases.json AÚN NO existe (es de la fase 2, post-adjudicación)")

    total = ok + len(fallas)
    print(f"verificador_f1: {ok}/{total}")
    for f in fallas:
        print("  FALLA:", f)
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(main())
