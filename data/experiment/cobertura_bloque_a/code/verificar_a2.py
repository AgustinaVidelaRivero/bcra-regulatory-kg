"""Verificador independiente de la corrida A.2. Sin API.

Recomputa desde los artefactos: integridad de la corrida, cumplimiento de
cada prediccion contra su umbral SELLADO, y las cuentas del cruce 2x2.
Uso:  python3 verificar_a2.py
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import comun_coba as C  # noqa: E402

FALLAS: list[str] = []
SELLO_V4 = "87fae986a8dc5370bef67c65e257409b26653a021f262e007d3348f21657b0ff"


def check(nombre, ok, detalle=""):
    print(f"  [{'OK  ' if ok else 'FALLA'}] {nombre}" + (f" — {detalle}" if detalle else ""))
    if not ok:
        FALLAS.append(nombre)


def veredicto(nombre, ok, detalle):
    """Una prediccion NO es una falla del verificador: se reporta cumplida o
    fallada, y su consecuencia la fija §6 del pre-registro."""
    print(f"  [{'CUMPLE' if ok else 'FALLA '}] {nombre} — {detalle}")
    return ok


def main() -> int:
    print("== 1. integridad de la corrida ==")
    sha = hashlib.sha256((C.UNIDAD / "prerregistro_A2_v4.md").read_bytes()).hexdigest()
    check("el pre-registro v4 sigue sellado", sha == SELLO_V4, sha[:16] + "...")
    res = json.loads((C.UNIDAD / "a2_salida/resumen_corrida_a2.json")
                     .read_text(encoding="utf-8"))
    filas = [json.loads(l) for l in (C.UNIDAD / "a2_salida/extracciones_a2.jsonl")
             .read_text(encoding="utf-8").splitlines() if l.strip()]
    check("191 unidades extraidas", len(filas) == 191, str(len(filas)))
    check("77 prosa + 114 planilla",
          sum(1 for f in filas if f.get("brazo") == "prosa") == 77
          and sum(1 for f in filas if f.get("brazo") == "planilla_ficha") == 114)
    check("cero errores de llamada",
          sum(1 for f in filas if f.get("error")) == 0,
          str(sum(1 for f in filas if f.get("error"))))
    check("perfil v3 con su prefijo sellado",
          res["perfil"] == "v3_b54" and res["prefijo_hash"] == "54a111e2175f")
    check("gasto BAJO el tope de USD 4,00",
          res["gasto_usd"] < 4.00 and res["frenado_por_tope"] is None,
          f"USD {res['gasto_usd']}")
    check("toda unidad lleva granularidad_procedencia = pagina",
          all(f.get("granularidad_procedencia") == "pagina" for f in filas))

    m = json.loads((C.UNIDAD / "medicion_a2.json").read_text(encoding="utf-8"))
    pr, pl = m["por_brazo"]["prosa"], m["por_brazo"]["planilla_ficha"]

    print("\n== 2. predicciones del BRAZO PROSA (umbrales sellados) ==")
    veredicto("PR-1 cero TIPO o PREDICADO fuera de lista",
              not pr["rechazos_de_vocabulario_PR1"],
              f'{pr["rechazos_de_vocabulario_PR1"]} · aparte, firmas invalidas '
              f'(tipos y predicado SI del vocabulario, falla la matriz '
              f'dominio/rango): {pr["rechazos_firma_invalida_NO_es_PR1"]}')
    veredicto("PR-2 rinde >= 80 %", pr["tasa_rinde"] >= 0.80,
              f"{pr['rinden']}/{pr['unidades']} = {pr['tasa_rinde']:.1%}")
    dom = max(pr["tipos"], key=pr["tipos"].get) if pr["tipos"] else None
    veredicto("PR-3 Obligacion domina y >= 45 %",
              dom == "Obligacion" and (pr["frac_obligacion"] or 0) >= 0.45,
              f"dominante={dom} · {pr['frac_obligacion']}")
    veredicto("PR-4 aplica_a en (42,9 % ; 53,1 %)",
              0.429 < (pr["frac_aplica_a"] or 0) < 0.531,
              f"{pr['unidades_con_aplica_a']}/{pr['unidades']} = {pr['frac_aplica_a']:.1%}")
    veredicto("PR-5 >= 1 entidad con palabra partida",
              pr["entidades_con_palabra_partida"] >= 1,
              str(pr["entidades_con_palabra_partida"]))

    print("\n== 3. predicciones del BRAZO PLANILLA (censo de 114) ==")
    veredicto("PL-1 cero TIPO o PREDICADO fuera de lista",
              not pl["rechazos_de_vocabulario_PR1"],
              f'{pl["rechazos_de_vocabulario_PR1"]} · firmas invalidas: '
              f'{pl["rechazos_firma_invalida_NO_es_PR1"]}')
    veredicto("PL-2 rinde < 50 %", pl["tasa_rinde"] < 0.50,
              f"{pl['rinden']}/{pl['unidades']} = {pl['tasa_rinde']:.1%}")
    veredicto("PL-4 Obligacion < 25 %", (pl["frac_obligacion"] or 0) < 0.25,
              str(pl["frac_obligacion"]))

    print("\n== 4. cruce 2x2 de PR-4 (tamiz) ==")
    cr = m["PR4_cruce_2x2"]["agregado"]
    check("las cuatro celdas suman las 77 del brazo prosa",
          sum(cr.values()) == 77, f"{sum(cr.values())}")
    conc = cr["CONCORDANTE"]
    p2 = cr["MENCION LITERAL SIN EMISION - PRIORIDAD 2"]
    check("mencion literal = CONCORDANTE + PRIORIDAD 2 = 33",
          conc + p2 == 33, f"{conc} + {p2} = {conc + p2}")
    check("aplica_a = CONCORDANTE + PRIORIDAD 1",
          conc + cr["EMISION SIN MENCION LITERAL - PRIORIDAD 1 DE REVISION MANUAL"]
          == pr["unidades_con_aplica_a"])
    check("el cruce se reporta con rotulos de estrato, no de correccion",
          "ES TAMIZ, NO MEDICION" in m["PR4_cruce_2x2"]["_naturaleza"]
          and "COINCIDENCIA LEXICA" in m["PR4_cruce_2x2"]["_que_testea_la_marca_literal"])
    check("PR-2 y PR-4 reportados por TO (los 9)",
          len(m["PR2_PR4_por_to"]) == 9, str(len(m["PR2_PR4_por_to"])))

    print("\n== 5. adjudicacion de causa de PR-4 ==")
    aj = json.loads((C.UNIDAD / "adjudicacion_pr4.json").read_text(encoding="utf-8"))
    part = json.loads((C.UNIDAD / "particion_24_casos.json").read_text(encoding="utf-8"))
    crit = hashlib.sha256(
        (C.UNIDAD / "criterio_destinatario.md").read_bytes()).hexdigest()
    check("el criterio se sello y no cambio",
          crit == "f5066c12a906b2e3720e2b62d1cb9db2cb45bdcfc91bb91d46c77d3ab843204a",
          crit[:16] + "...")
    check("los 24 casos clasificados: 22 P2 + 2 P1",
          len(part["prioridad_2"]) == 22 and len(part["prioridad_1"]) == 2)
    from collections import Counter as Ct
    c2 = Ct(c["clase"] for c in part["prioridad_2"])
    check("P2: 18 (B) marca + 4 (A) modelo = 22",
          c2["B"] == 18 and c2["A"] == 4 and c2["B"] + c2["A"] == 22, str(dict(c2)))
    check("de los 4 (A), 2 son chapeau huerfano",
          aj["a_reparto_de_los_22"]
          ["(i) falla del MODELO — destinatario no emitido"]
          ["de_ellos_chapeau_huerfano"] == 2)
    check("P1: cero invencion (D)",
          Ct(c["clase"] for c in part["prioridad_1"]) == {"C": 2})
    check("las 14 de ri_tii: TODAS en prosa sin tabla",
          aj["b_ri_tii_contra_censo"]["reparto_clase_forma_x_tabla_b583"]
          == {"prosa / tabla=False": 14})
    ar = aj["c_arnes_contra_dev"]
    check("dev 100 % con titulo, A.2 0 % — diferencia de arnes total",
          ar["dev_con_titulo_no_vacio"].endswith("100.0%")
          and ar["A2_con_titulo_no_vacio"].startswith("0/191"))
    check("(iii-b) NO aplica: los rotulos de dev y A.2 son IDENTICOS",
          ar["rotulos_identicos"] and not ar["chunk_de_punto_es_valor_de_tipo"],
          ar["rotulo_que_imprime_dev"])
    check("(iii-a) dimensionada: 25/1763 = 1,4 % en dev",
          ar["iii_a_dev_unica_mencion_en_titulo"] == "25/1763 = 1.4%")
    pi = aj["recalculo_del_piso"]
    check("ETAPA 1 (superseded): piso 17/77 = 22,1 % y recuperacion 13/17 = 76,5 %",
          pi["piso_recalculado"] == "17/77 = 22.1%"
          and pi["con_destinatario_identificado"] == 17
          and pi["recuperacion_sobre_destinatarios_identificados"] == "13/17 = 76.5%",
          "cifras de la etapa 1; las vigentes son las de la etapa 3")

    print("\n== 6. (iii-a) rehecha y revision de los CONCORDANTE ==")
    ia = json.loads((C.UNIDAD / "iii_a_rehecha.json").read_text(encoding="utf-8"))
    check("(iii-a) correcta = 44/1763 = 2,5 %",
          ia["medicion_correcta"]["casos"] == 44
          and ia["medicion_correcta"]["texto"] == "44/1763 = 2.5%")
    check("las dos superseded quedan medidas y explicadas (25 y 187)",
          ia["superseded"]["titulo_si_texto_completo_no"]["casos"] == 25
          and ia["superseded"]["titulo_si_cuerpo_sin_linea1_no"]["casos"] == 187)
    tc = ia["titulo_contenido_en_texto_rama_de_A2"]
    check("1.477/1.477 = 100 % de la rama de A.2 tiene su titulo en su texto",
          tc["unidades_en_la_rama"] == 1477
          and tc["con_titulo_contenido_en_su_texto"] == 1477
          and tc["fraccion"] == 1.0)
    ad = hashlib.sha256(
        (C.UNIDAD / "adenda_criterio_concordantes.md").read_bytes()).hexdigest()
    check("la adenda con la regla INVERTIDA esta sellada",
          ad == "b610151c47d27fc7c579b584ffd79588f62ff725c4c860b1aa202c555df9960a",
          ad[:16] + "...")
    rc = json.loads((C.UNIDAD / "recomputo_concordantes.json").read_text(encoding="utf-8"))
    rev_conc = json.loads((C.UNIDAD / "revision_concordantes.json").read_text(encoding="utf-8"))
    a11 = rc["a_clasificacion_de_los_11"]
    check("los 11 CONCORDANTE: 8 (A) + 2 (C) + 1 (B) = 11",
          a11["A_destinatario_y_arista_coinciden"] == 8
          and a11["C_inferencia_legitima"] == 2
          and a11["B_no_hay_destinatario"] == 1 and a11["total"] == 11)
    check("se listan TRES aristas a retirar, de dos unidades",
          rc["b_aristas_que_se_retiran"]["cantidad"] == 3
          and len(rc["b_aristas_que_se_retiran"]["de_unidades"]) == 2)
    cr2 = rc["c_recomputo"]
    check("ETAPA 2 (superseded): k=1 -> 16/77 = 20,8 % y 12/16 = 75,0 %",
          cr2["k_unidades_B"] == 1
          and cr2["piso_recalculado"] == "16/77 = 20.8%"
          and cr2["emitido"] == "12/77 = 15.6%"
          and cr2["recuperacion"] == "12/16 = 75.0%")
    dc = hashlib.sha256(
        (C.UNIDAD / "declaracion_censo_silencios.md").read_bytes()).hexdigest()
    check("la declaracion previa al censo esta sellada",
          dc == "7cc0ac9a35dcbfa5e0f01c02019cc32fd83b1e5ec579e6c45e541e1ee9ea7abb",
          dc[:16] + "...")
    ms = rc["d_censo_de_silencios"]
    check("CENSO de las 42, no muestra",
          ms["leidos"] == 42 == ms["de"])
    check("2 falsos negativos = 4,8 %, en ri_pspii y ri_rem",
          ms["falsos_negativos"] == 2
          and ms["tasa_agregada"] == "2/42 = 4.8%"
          and ms["los_dos_falsos_negativos_estan_en"] == ["ri_pspii", "ri_rem"])
    check("los dos caen en documentos que la muestra de 15 excluia",
          all(t in ms["documentos_que_la_muestra_excluia"]
              for t in ms["los_dos_falsos_negativos_estan_en"]))
    check("tasa reportada POR DOCUMENTO (los 8 con silencios)",
          len(ms["por_documento"]) == 8
          and sum(v["silencios"] for v in ms["por_documento"].values()) == 42)
    rf = rc["e_recomputo_final"]
    check("Caso 2 de la declaracion: j=2 -> 18 destinatarios, 12/18 = 66,7 %",
          rf["j_falsos_negativos"] == 2
          and rf["piso_final"] == "18/77 = 23.4%"
          and rf["recuperacion"] == "12/18 = 66.7%")
    check("6 omisiones del extractor sobre 18 destinatarios",
          rf["omisiones_del_extractor"] == "6 sobre 18 destinatarios")
    check("ETIQUETA CORREGIDA: MEDICION SOBRE CENSO, no cota superior",
          rf["ETIQUETA"].startswith("MEDICION SOBRE CENSO")
          and "sigue_siendo_cota_superior" not in rf,
          rf["ETIQUETA"])
    pnc = rf["por_que_NO_es_cota_superior"]
    check("las 77 del brazo estan clasificadas: 11+22+2+42",
          "11 concordantes + 22 Prioridad 2 + 2 Prioridad 1 + 42 silencios = 77"
          in pnc["el_denominador_esta_completo"]
          and 11 + 22 + 2 + 42 == 77)
    check("el desempate sesga a la BAJA: 13/19 = 68,4 % seria MAS ALTO",
          "13/19 = 68,4 %" in pnc["el_desempate_sesga_a_la_BAJA_no_a_la_alta"]
          and round(13 / 19, 3) == 0.684)
    iv = rf["intervalo"]
    check("intervalo CERRADO 66,7 % - 75,0 %, sin cota abierta",
          iv["publicado"] == "66.7% – 75.0%" and iv["ninguna_cota_abierta"]
          and iv["extremo_inferior"] == "12/18 = 66.7%"
          and iv["extremo_superior"] == "12/16 = 75.0%")
    check("los DOS extremos trazables a casos NOMBRADOS",
          len(iv["los_dos_casos_NOMBRADOS"]) == 2
          and all(c in " ".join(iv["los_dos_casos_NOMBRADOS"])
                  for c in ("ri_tii::p1.b1", "ri_fcem::p1.b3")))
    aj2 = (C.UNIDAD / "adjudicacion_pr4.md").read_text(encoding="utf-8")
    check("el reporte NO afirma varianza del extractor",
          "varianza del extractor" not in aj2
          or "no se afirma varianza\ndel extractor" in aj2)
    check("lo medido va como frase, y la causa como OBSERVACION con su n",
          "6 de los 18 destinatarios identificados\nquedaron sin arista" in aj2
          and "OBSERVACIÓN, con su n" in aj2
          and "Son dos pares" in aj2
          and "Es otra unidad,\nno esta" in aj2)
    c05 = [x for x in rev_conc["concordantes"] if x["n"] == "C05"][0]
    check("el motivo de la 3a arista NO invoca la regla de desempate",
          c05["clase_de_la_arista_retirada"] == "B"
          and c05["subclase_de_la_arista_retirada"] == "B1"
          and "NO DUDA" in c05["motivo_del_retiro"])
    aj_md = (C.UNIDAD / "adjudicacion_pr4.md").read_text(encoding="utf-8")
    check("la conclusion de los DOS anclajes esta escrita, no como nota al pie",
          "LOS DOS ANCLAJES ESTABAN MAL ESPECIFICADOS" in aj_md
          and "ES SU PRODUCTO" in aj_md
          and "no era aplicable a bloques de página" in aj_md)
    check("la linea de metodo trae las DOS vias y su mecanismo comun",
          "(a) Por PREDICCIÓN" in aj_md and "(b) Por PROCEDIMIENTO" in aj_md
          and "DECLARAR\nANTES DE MIRAR" in aj_md
          and "no había número que pudiera fallar" in aj_md)
    check("la etiqueta (A) queda desambiguada por columna",
          "la etiqueta (A) está sobrecargada" in aj_md
          and "columna Prioridad 2" in aj_md
          and "columna CONCORDANTE" in aj_md
          and "ambos\n  clasificados (A)" not in aj_md)
    sellos = {
        "prerregistro_A2.md":
            "3aef54c9d27589c3d249cbcfa126c816cd48bf5ae1489507c2993389892d2e7d",
        "prerregistro_A2_v2.md":
            "fa7fdf52e2dedb98f912f206b15391985c994631e9ec3aa74e712bf42bc0cd1e",
        "prerregistro_A2_v3.md":
            "8e112189369bfccc5a2010c4d4780abbbb8d2c840076be4a8cd8ea2888611cbe",
        "prerregistro_A2_v4.md":
            "87fae986a8dc5370bef67c65e257409b26653a021f262e007d3348f21657b0ff",
        "criterio_destinatario.md":
            "f5066c12a906b2e3720e2b62d1cb9db2cb45bdcfc91bb91d46c77d3ab843204a",
        "adenda_criterio_concordantes.md":
            "b610151c47d27fc7c579b584ffd79588f62ff725c4c860b1aa202c555df9960a",
        "declaracion_censo_silencios.md":
            "7cc0ac9a35dcbfa5e0f01c02019cc32fd83b1e5ec579e6c45e541e1ee9ea7abb",
    }
    ok = all(hashlib.sha256((C.UNIDAD / n).read_bytes()).hexdigest() == h
             for n, h in sellos.items())
    check("los SIETE sellos de la unidad, intactos (4 pre-registros + criterio "
          "+ adenda + declaracion)", ok and len(sellos) == 7, f"{len(sellos)}/7")
    check("(iii-a) queda como PROPIEDAD DE POBLACION, no deficit de arnes",
          "NO ES UN DÉFICIT\nDE ARNÉS, ES UNA PROPIEDAD DE POBLACIÓN" in aj_md
          or "NO ES UN DÉFICIT DE ARNÉS, ES UNA PROPIEDAD DE POBLACIÓN" in aj_md)

    print(f"\n{'='*60}")
    if FALLAS:
        print(f"FALLAS DE VERIFICACION: {len(FALLAS)}")
        for f in FALLAS:
            print(f"  - {f}")
        return 1
    print("VERIFICACION OK — cero fallas (los veredictos de prediccion se leen arriba)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
