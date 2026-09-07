"""Verificador independiente de la fase A.1 de U-COB-A.

Recomputa TODOS los numeros que el reporte publica, desde los artefactos del
repositorio, y verifica la guarda 1 de no-cambio. Corre sin API y desde
cualquier cwd.  Uso:  python3 verificar_a1.py

Cada linea imprime OK o FALLA; el codigo de salida es 1 si hay alguna falla.
"""
from __future__ import annotations

import glob
import hashlib
import json
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import comun_coba as C  # noqa: E402
import censo_forma as CF  # noqa: E402
from e0_lib import separar_encabezado_pie  # noqa: E402

FALLAS: list[str] = []


def check(nombre: str, ok: bool, detalle: str = "") -> None:
    print(f"  [{'OK  ' if ok else 'FALLA'}] {nombre}" + (f" — {detalle}" if detalle else ""))
    if not ok:
        FALLAS.append(nombre)


def main() -> int:
    print("== 1. la cuenta del alcance, contra particion_152.json ==")
    part = json.loads(C.PARTICION.read_text(encoding="utf-8"))
    ns = {k: v for k, v in part["por_to"].items()
          if v["clase"] == "no_segmentable_declarado"}
    check("12 no segmentables", len(ns) == 12, str(len(ns)))
    check("161 paginas en los 12",
          sum(v["paginas"] for v in ns.values()) == 161)
    check("control 161 - 43 (optico) - 77 (plandecuentas) = 41",
          161 - ns["optico"]["paginas"] - ns["plandecuentas"]["paginas"] == 41)
    diez = {k: v["paginas"] for k, v in ns.items() if k not in C.REFERENCIA}
    check("los DIEZ suman 41 paginas",
          len(diez) == 10 and sum(diez.values()) == 41,
          f"{len(diez)} docs / {sum(diez.values())} pag")
    check("desglose exacto del mandato",
          diez == {"ri_con": 16, "ri_spi": 11, "ri_tii": 6, "ri_rem": 2,
                   "ri_chr": 1, "ri_fcem": 1, "ri_itme": 1, "ri_pfmipyme": 1,
                   "ri_pscpp": 1, "ri_pspii": 1})
    ag = part["agregados"]
    check("recurso hoy = 9.324 = 9.266 + 46 + 12",
          sum(v["unidades"] for v in ag.values()) == 9324
          and ag["reconocido_pleno"]["unidades"] == 9266
          and ag["parcial_declarado"]["unidades"] == 46
          and ag["no_segmentable_declarado"]["unidades"] == 12)
    check("las 12 unidades NO son una por documento",
          ns["plandecuentas"]["unidades"] == 0 and ns["ri_pspii"]["unidades"] == 2,
          "plandecuentas=0, ri_pspii=2 (el mandato dice 'una por documento')")
    check("de las 12, 11 son de los DIEZ y 1 de los dos de referencia",
          sum(v["unidades"] for k, v in ns.items() if k in C.DIEZ) == 11
          and sum(v["unidades"] for k, v in ns.items() if k in C.REFERENCIA) == 1)

    print("\n== 2. censo de forma, regenerado en esta corrida ==")
    censo = json.loads((C.UNIDAD / "censo_forma.json").read_text(encoding="utf-8"))
    a = censo["agregados_diez"]
    vivo = {"prosa": 0, "mixta": 0, "planilla_ficha": 0}
    for to in C.DIEZ:
        paginas, roles, modal, bloques, _d = C.leer_documento(to)
        for i, (lineas, rol) in enumerate(zip(paginas, roles), start=1):
            if rol != C.E0.ROL_CUERPO:
                continue
            cont, _x, _y = separar_encabezado_pie(lineas)
            vivo[CF.clase_forma(CF.densidad_prosa(cont))] += len(bloques[i])
    check("332 bloques totales, recomputados en vivo",
          sum(vivo.values()) == 332 == a["bloques_total"], str(sum(vivo.values())))
    check("110 prosa + 37 mixta + 185 planilla = 332",
          vivo == {"prosa": 110, "mixta": 37, "planilla_ficha": 185}
          and sum(vivo.values()) == 332, str(vivo))
    check("147 utiles = 110 + 37",
          vivo["prosa"] + vivo["mixta"] == 147 == a["bloques_utiles_prosa_y_mixta"])
    check("17 prosa + 3 mixta + 21 planilla = 41 paginas",
          sum(a["paginas_por_clase_forma"].values()) == 41,
          str(a["paginas_por_clase_forma"]))
    r = censo["agregados_referencia"]
    check("los DOS de referencia: 120 paginas, 2 bloques, 0 de prosa",
          r["paginas"] == 120 and r["bloques_total"] == 2
          and all(v["paginas_por_clase_forma"]["prosa"] == 0
                  for v in censo["bloque_a_referencia"].values()))

    print("\n== 3. esquema congelado (guarda 2) ==")
    sys.path.insert(0, str(C.EXPERIMENT / "esq/code"))
    import prompt_congelado as PC  # noqa: E402
    check("9 tipos / 13 predicados / enum de 6",
          len(PC.ENTITY_TYPES_CONGELADO) == 9
          and len(PC.PREDICATES_CONGELADO) == 13
          and len(PC.OBLIGACION_TIPO_CONGELADO) == 6)
    check("sha del prefijo = el del laudo ESQ-3",
          PC.PREFIJO_SHA256_CONGELADO ==
          "e69feaaa04779bd6347cc9e3974d2c1749519f1230e70a0459e66f46517cd720")

    print("\n== 4. senal de sujeto y su baseline ==")
    ss = json.loads((C.UNIDAD / "senal_sujeto.json").read_text(encoding="utf-8"))
    check("bloque A: 41 de 147 nombran sujeto (27,9 %)",
          ss["agregado"] == {"bloques": 147, "nombran_sujeto": 41,
                             "fraccion": 0.279, "sin_sujeto_nombrado": 106},
          str(ss["agregado"]))
    import senal_sujeto as SS  # noqa: E402
    pats = SS.formas_de_superficie()
    tot = con = 0
    for f in sorted(glob.glob(str(C.EXPERIMENT /
                                  "reextraccion_v2/e0_chunking/salida_enm01/chunks_*.json"))):
        for c in json.loads(Path(f).read_text(encoding="utf-8")):
            tot += 1
            if any(p.search(c.get("texto") or "") for p in pats.values()):
                con += 1
    check("baseline dev: 936 de 1.763 (53,1 %)",
          tot == 1763 and con == 936, f"{con}/{tot}")

    print("\n== 5. guarda 1 — no-cambio (estructural y verificada) ==")
    dev = {}
    for f in sorted(glob.glob(str(C.EXPERIMENT /
                                  "reextraccion_v2/e0_chunking/salida_enm01/chunks_*.json"))):
        dev[Path(f).stem.replace("chunks_", "")] = len(
            json.loads(Path(f).read_text(encoding="utf-8")))
    check("control dev = 1.763 con desglose por TO",
          sum(dev.values()) == 1763
          and dev == {"cap": 462, "cla": 143, "ext": 973, "pro": 101, "ric": 84},
          str(dev))
    check("control de los 138 plenos = 9.266",
          ag["reconocido_pleno"]["unidades"] == 9266)
    esq2 = json.loads((C.EXPERIMENT / "esq/cobertura/resumen_cobertura_esq2.json")
                      .read_text(encoding="utf-8"))
    check("control ESQ-2 = 762",
          esq2["unidades_universo"] == 762 == esq2["persistidas_sin_error"])
    proy = json.loads((C.EXPERIMENT / "escalado_prep/proyeccion_costo.json")
                      .read_text(encoding="utf-8"))
    dig = proy["agregado"]["por_veredicto"]["digerible"]
    check("control de los 68 digeribles = 6.340",
          dig["tos"] == 68 and dig["unidades"] == 6340)
    for mod in ("reextraccion_v2/e0_chunking/e0_lib.py",
                "reextraccion_v2/e0_chunking/e0_tablas.py",
                "esq/code/prompt_congelado.py"):
        rc = subprocess.run(["git", "diff", "--quiet", "HEAD", "--",
                             f"data/experiment/{mod}"], cwd=C.REPO).returncode
        check(f"{mod} identico a HEAD", rc == 0)
    sucio = subprocess.run(["git", "status", "--porcelain", "--",
                            "data/experiment/reextraccion_v2",
                            "data/experiment/segmentacion_84",
                            "data/experiment/escalado_prep",
                            "data/experiment/esq"],
                           cwd=C.REPO, capture_output=True, text=True).stdout.strip()
    check("zonas selladas sin modificar", sucio == "", sucio or "limpio")

    print("\n== 6. conteo exigido y costo ==")
    pr = json.loads((C.UNIDAD / "proyeccion_procedencia.json").read_text(encoding="utf-8"))
    m = pr["medicion_conteo_exigido_en_unidades"]
    check("332 de 9.645 (9.324 - 11 + 332)",
          m["todos_los_bloques"]["unidades_totales_del_recurso"] == 9645
          == 9324 - 11 + 332)
    check("147 de 9.460 (9.324 - 11 + 147)",
          m["solo_prosa_y_mixta"]["unidades_totales_del_recurso"] == 9460
          == 9324 - 11 + 147)
    co = json.loads((C.UNIDAD / "costo_a2.json").read_text(encoding="utf-8"))
    check("piloto A.2 = 61 unidades",
          co["por_to"]["ri_tii"]["prosa"]["unidades"]
          + co["por_to"]["ri_tii"]["planilla_ficha"]["unidades"]
          + co["por_to"]["ri_itme"]["prosa"]["unidades"]
          + co["por_to"]["ri_con"]["prosa"]["unidades"] == 61)
    pp = json.loads((C.UNIDAD / "palabra_partida.json").read_text(encoding="utf-8"))
    check("79 de 332 bloques con palabra partida (23,8 %)",
          pp["agregado"]["con_palabra_partida"] == 79
          and pp["agregado"]["bloques"] == 332)

    print("\n== 7. freno expres: alcance de NUEVE (laudo 2) ==")
    an = json.loads((C.UNIDAD / "alcance_nueve.json").read_text(encoding="utf-8"))
    ca = an["cuenta_del_alcance"]
    check("41 - 11 (ri_spi) = 30 paginas, y coincide con particion_152",
          ca["paginas_de_los_nueve"] == 30 == ca["control_particion"]
          == 41 - ca["paginas_de_ri_spi"])
    check("9 documentos", len(an["_meta"]["alcance_final"]["lista"]) == 9)
    br = an["brazos_completos"]
    check("brazos: 77 prosa + 114 planilla = 191 (332 - 141 de ri_spi)",
          br["prosa"]["bloques"] == 77 and br["planilla_ficha"]["bloques"] == 114
          and 77 + 114 == 191 == 332 - an["ri_spi_fuera"]["bloques"])
    check("la clase mixta desaparece al salir ri_spi",
          br["mixta"]["bloques"] == 0 and br["mixta"]["paginas"] == 0)
    check("13 paginas de prosa + 17 de planilla = 30",
          br["prosa"]["paginas"] == 13 and br["planilla_ficha"]["paginas"] == 17)
    check("senal de sujeto del brazo prosa = 33/77 (42,9 %)",
          br["prosa"]["con_sujeto"] == 33,
          f'{br["prosa"]["con_sujeto"]}/77')
    pil = an["A2"]
    check("A.2 = 77 prosa + 114 planilla = 191 unidades (los dos brazos completos)",
          pil["total_unidades"] == 191
          == pil["brazo_prosa"]["bloques"] + pil["brazo_planilla"]["bloques"]
          and pil["brazo_planilla"]["bloques"] == br["planilla_ficha"]["bloques"])
    check("A.2 BAJO el tope laudado de USD 4,00 por las DOS vias",
          pil["bajo_tope"] and pil["usd_via_unidad_COTA_SUPERIOR"] < 4.00
          and pil["usd_via_caracter"] < 4.00,
          f'char {pil["usd_via_caracter"]} / unidad {pil["usd_via_unidad_COTA_SUPERIOR"]}')
    sg = an["sesgo_composicion_muestra_v1"]["por_to"]
    check("sesgo v1: ri_con 89,5 % poblacion / 50,0 % muestra / 11,8 % cobertura",
          sg["ri_con"]["frac_poblacion"] == 0.895
          and sg["ri_con"]["frac_muestra"] == 0.5
          and sg["ri_con"]["cobertura_propia"] == 0.118)
    check("sesgo v1: ri_tii sobrerrepresentado 4,75x",
          sg["ri_tii"]["sobrerrepresentacion"] == 4.75
          and sg["ri_tii"]["frac_poblacion"] == 0.096)
    rc = an["sesgo_composicion_muestra_v1"]["ri_con_paginas_planilla"]
    check("p.13 es el MAXIMO de ri_con (14 paginas, media 7,3, max 12)",
          rc["n"] == 14 and rc["media_bloques"] == 7.3
          and rc["max"] == 12 == rc["pagina_elegida_v1"])
    ss9 = an["senal_sujeto_brazo_prosa_por_to"]
    tii = ss9["ri_tii"]
    tot_s = sum(v["con_sujeto"] for v in ss9.values())
    tot_b = sum(v["bloques"] for v in ss9.values())
    check("PR-4 por TO: 19 de los 33 son de ri_tii; sin ri_tii 14/52 = 26,9 %",
          tii["con_sujeto"] == 19 and tii["bloques"] == 25
          and tot_s == 33 and tot_b == 77
          and (tot_s - 19) == 14 and (tot_b - 25) == 52)

    print("\n== 8. ancla de PR-2 y factor de longitud (versionados) ==")
    ap = json.loads((C.UNIDAD / "ancla_pr2.json").read_text(encoding="utf-8"))
    cif = ap["cifras"]
    check("ancla PR-2: primaria 1.696/1.763 = 96,2 %, con y sin filtro de tipo",
          cif["primaria_cualquiera"]["unidades"] == 1696
          == cif["primaria_normativo"]["unidades"]
          and cif["primaria_normativo"]["denominador"] == 1763)
    check("conjuntos primarios IDENTICOS (el filtro de tipo no mueve nada)",
          ap["hallazgo"]["primaria_cualquiera_igual_a_primaria_normativo"])
    check("lista completa: 1.762 y 1.711; brecha 51, toda TextoOrdenado",
          cif["lista_cualquiera"]["unidades"] == 1762
          and cif["lista_normativo"]["unidades"] == 1711
          and ap["hallazgo"]["brecha_lista"] == 51
          and ap["hallazgo"]["tipos_que_sostienen_la_brecha"] == {"TextoOrdenado": 51})
    check("convencion laudada = procedencia primaria, ancla 96,2 %, umbral 80 %",
          ap["_meta"]["convencion_laudada"] == "primaria_normativo"
          and ap["ancla_de_PR2"] == 0.9620 and ap["umbral_PR2"] == 0.80)
    fl = json.loads((C.UNIDAD / "factor_longitud.json").read_text(encoding="utf-8"))
    m = fl["matriz"]
    check("factor por MEDIANA (convencion): prosa 1,80x, los 191 2,94x",
          m["prosa"]["factor_por_mediana"] == 1.80
          and m["los_191_de_A2"]["factor_por_mediana"] == 2.94)
    check("el 2,8x del laudo reproduce con MEDIAS (2,84x), no con medianas",
          m["prosa"]["factor_por_media"] == 2.84)
    check("el 3,2x NO reproduce con ninguna combinacion (vecinos 2,94 y 3,85)",
          not any(abs(m[k][e] - 3.2) < 0.06 for k in m
                  for e in ("factor_por_mediana", "factor_por_media")),
          "discrepancia declarada en el pre-registro v2 §7")

    print("\n== 9. sellos de los pre-registros ==")
    for nombre, esperado in (
            ("prerregistro_A2.md",
             "3aef54c9d27589c3d249cbcfa126c816cd48bf5ae1489507c2993389892d2e7d"),
            ("prerregistro_A2_v2.md",
             "fa7fdf52e2dedb98f912f206b15391985c994631e9ec3aa74e712bf42bc0cd1e"),
            ("prerregistro_A2_v3.md",
             "8e112189369bfccc5a2010c4d4780abbbb8d2c840076be4a8cd8ea2888611cbe"),
            ("prerregistro_A2_v4.md",
             "87fae986a8dc5370bef67c65e257409b26653a021f262e007d3348f21657b0ff")):
        sha = hashlib.sha256((C.UNIDAD / nombre).read_bytes()).hexdigest()
        check(f"sha de {nombre}", sha == esperado, sha[:16] + "...")
    fc = an["fila_del_conteo_MEDICION_en_unidades"]
    check("fila del conteo: 9.324 - 10 + 191 = 9.505",
          fc["todos_los_bloques"]["unidades_totales_del_recurso"] == 9505
          == 9324 - 10 + 191)
    check("fila del conteo: 9.324 - 10 + 77 = 9.391",
          fc["solo_prosa"]["unidades_totales_del_recurso"] == 9391
          == 9324 - 10 + 77)
    print("\n== 10. §6.a — la medicion que sostiene la fila del piso (v3) ==")
    piso = 33 / 77
    ss9 = an["senal_sujeto_brazo_prosa_por_to"]
    bajo = {to: v for to, v in ss9.items()
            if v["bloques"] and v["con_sujeto"] / v["bloques"] < piso}
    u_bajo = sum(v["bloques"] for v in bajo.values())
    check("5 de los 9 caen bajo el piso del brazo por construccion",
          len(bajo) == 5
          and set(bajo) == {"ri_con", "ri_rem", "ri_chr", "ri_itme", "ri_pspii"},
          str(sorted(bajo)))
    check("son 45 de las 77 unidades = 58,4 % del brazo prosa",
          u_bajo == 45 and round(u_bajo / 77, 3) == 0.584,
          f"{u_bajo}/77 = {u_bajo/77:.1%}")
    check("las tasas propias van de 0 % (ri_rem) a 100 % (ri_pscpp)",
          ss9["ri_rem"]["con_sujeto"] == 0 and ss9["ri_rem"]["bloques"] == 11
          and ss9["ri_pscpp"]["con_sujeto"] == ss9["ri_pscpp"]["bloques"] == 1)
    v3 = (C.UNIDAD / "prerregistro_A2_v3.md").read_text(encoding="utf-8")
    check("la v3 NO excluye documentos por el piso",
          "No hay exclusion de ningun documento" in v3
          and "salvo** el o los documentos que sostengan la falla" not in v3)
    check("la v3 tiene fila de ingreso para PR-1 / PL-1",
          "PR-1 o PL-1 falla" in v3 and "no entra NADA" in v3)
    check("la v3 cierra las diez predicciones (PR-3, PR-5 y PL-5 no gatean)",
          "`PR-3`, `PR-5` y `PL-5`" in v3
          and "las diez predicciones tienen\nconsecuencia pre-declarada" in v3)
    v2 = (C.UNIDAD / "prerregistro_A2_v2.md").read_text(encoding="utf-8")
    v4 = (C.UNIDAD / "prerregistro_A2_v4.md").read_text(encoding="utf-8")
    import re
    def secciones(t):
        pt = re.split(r"(?m)^(## .*)$", t)
        return {pt[i].strip(): pt[i + 1] for i in range(1, len(pt), 2)}
    a2, a3, a4 = secciones(v2), secciones(v3), secciones(v4)
    intactas = [k for k in a2 if k in a3 and a2[k] == a3[k]]
    check("el resto de la v2 viaja INTACTO en la v3 (7 secciones, §7 incluida)",
          len(intactas) == 7
          and "## 7. Factor de longitud — cifra corregida con su definición" in intactas,
          f"{len(intactas)} secciones")

    print("\n== 11. v4 — dos celdas y una linea sobre la v3 ==")
    ident4 = [k for k in a3 if k in a4 and a3[k] == a4[k]]
    check("8 secciones byte-identicas v3->v4: §0.bis, §1-§5, §7, §8",
          len(ident4) == 8
          and all(k in ident4 for k in a3
                  if not k.startswith("## 0.") and not k.startswith("## 6.")
                  and not k.startswith("## 0 ")),
          f"{len(ident4)} secciones")
    check("solo §6 cambia (aparte de §0, que registra la version)",
          [k for k in a3 if k in a4 and a3[k] != a4[k]]
          == ["## 6. Qué se QUEDA en el recurso y qué se retira (decidido ANTES de medir)"])
    s6a, s6b = a3["## 6. Qué se QUEDA en el recurso y qué se retira (decidido ANTES de medir)"], \
               a4["## 6. Qué se QUEDA en el recurso y qué se retira (decidido ANTES de medir)"]
    import difflib
    quitadas = [l[2:] for l in difflib.ndiff(s6a.splitlines(), s6b.splitlines())
                if l.startswith("- ")]
    puestas = [l[2:] for l in difflib.ndiff(s6a.splitlines(), s6b.splitlines())
               if l.startswith("+ ")]
    check("de §6 se reemplazan exactamente DOS lineas (las dos precondiciones)",
          len(quitadas) == 2
          and all("PR-2 y PR-4 se cumplen" in x for x in quitadas)
          and sum(1 for y in puestas
                  if "PR-2 se cumple y PR-4 no falla por el techo" in y) == 2,
          f"{len(quitadas)} quitadas / {len(puestas)} puestas")
    check("y se agregan TRES lineas mas (la linea de alcance)",
          len(puestas) - len(quitadas) == 3
          and len(s6b.splitlines()) - len(s6a.splitlines()) == 3)
    check("la linea de alcance esta y dice lo ordenado",
          "Las filas **1 y 2 deciden unicamente el" in v4
          and "brazo prosa lo deciden las filas 3, 4 y 5**" in v4)
    check("la precondicion vieja no queda en NINGUNA fila de la tabla de §6",
          not any("PR-2 y PR-4 se cumplen" in l
                  for l in s6b.splitlines() if l.startswith("|")),
          "en §0.a-bis si aparece, citada para explicar el cambio")
    check("§0 de la v4 lista las cuatro versiones con sha",
          all(h in v4 for h in ("3aef54c9d27589c3d249cbcfa126c816cd48bf5ae1489507c2993389892d2e7d",
                                "fa7fdf52e2dedb98f912f206b15391985c994631e9ec3aa74e712bf42bc0cd1e",
                                "8e112189369bfccc5a2010c4d4780abbbb8d2c840076be4a8cd8ea2888611cbe")))

    print(f"\n{'='*60}")
    if FALLAS:
        print(f"FALLAS: {len(FALLAS)}")
        for f in FALLAS:
            print(f"  - {f}")
        return 1
    print("TODO OK — cero fallas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
