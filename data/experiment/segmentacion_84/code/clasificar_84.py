#!/usr/bin/env python3
"""B5.8.0 — Clasificación de los 84 «necesita reglas» por familia de formato.

Reglas de decisión VISIBLES y determinísticas sobre mediciones_84.json
(medir_84.py) y los artefactos sellados de escalado_prep/ (solo lectura).
Cero LLM. La taxonomía es la del mandato B5.8.0, con las subdivisiones de
la familia (b) declaradas abajo.

Familia primaria = la causa que hoy (E0 VIGENTE, post-B5.2) bloquea primero:
  a       compuerta de rol de página: sin página de índice, todo en portada
          (e0_lib.py:206-207) y sin candidato de marcador de índice.
  b_idx   marcador de ÍNDICE en formato no contemplado por el regex vigente
          (candidato fuerte medido), o ya contemplado por B5.2 pendiente de
          re-corrida (estado en la evidencia).
  b_sec   marcador de SECCIÓN en formato variante ('SECCIÓN N', romanos) —
          hay marcador, no matchea RE_SECCION.
  b_pts   estructura enganchada pero con rechazos/avisos/anuncios sobre
          umbral (C4/C5/C7/C8): reglas finas de numeración y marcador.
  c       llega a cuerpo y NO hay ninguna línea con formato de marcador de
          sección (ni variante detectada): falta la raíz, no el formato.
  d       estructura tabular dominante (≥40 % de palabras en tabla de
          contenido, o C6 como falla de mayor exceso relativo sobre su
          umbral): destino parser B5.8.3.
  e       otra / candidato a no segmentable (p. ej. sin texto extraíble).

Cortes convencionales declarados (sirven para contar, no deciden solos):
  TAB_DOMINANTE=40 %, TAB_PRESENTE=15 % (cortes del scoping U-B5.6-0 §1.4);
  FICHA=2 % líneas de campo, LISTA=30 % líneas de código (ídem);
  UMBRAL_MARGINAL: toda falla C* con valor ≤ 1,5× su umbral;
  DENS_ESPINA_MIN=0,5 labels/pág: por debajo, y con señal ficha/lista, la
  espina es un preámbulo y el cuerpo dominante NO es prosa de puntos
  (medido: manual 0,05 y ri2_pm 0,09 labels/pág contra ≥1,1 del resto de
  las familias a/c con espina).

Uso (desde cualquier cwd):
    python3 data/experiment/segmentacion_84/code/clasificar_84.py
"""

import csv
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
PREP = REPO / "data/experiment/escalado_prep"
SALIDA = REPO / "data/experiment/segmentacion_84"

TAB_DOMINANTE = 40.0
TAB_PRESENTE = 15.0
FICHA_PCT = 2.0
LISTA_PCT = 30.0
MARGINAL_FACTOR = 1.5
DENS_ESPINA_MIN = 0.5
DENSIDAD_NG = 3.1558     # unid/pág, 68 digeribles (resumen_escalado.md §3.1)
TARIFA_UNIDAD = 0.019437  # USD E1+E3 por unidad (resumen_escalado.md §1)

RE_VALOR_UMBRAL = re.compile(r"(\d+(?:\.\d+)?)\s*(?:/u|%|chars)?\s*>\s*(\d+(?:\.\d+)?)")


def cargar():
    med = json.load(open(SALIDA / "mediciones_84.json"))
    ver = json.load(open(PREP / "veredictos_generalizacion.json"))["por_to"]
    dry = json.load(open(PREP / "e0_dry/conteos_e0_dry.json"))
    inv = {r["id"]: r for r in csv.DictReader(open(PREP / "inventario_unidades.csv"))}
    return med, ver, dry, inv


def fallas_codigos(fallas):
    return {f.split(" ")[0] for f in fallas}


def falla_dominante(fallas):
    """Código C* con mayor exceso relativo valor/umbral (parseado de la
    falla sellada). None si no hay fallas C* parseables."""
    mejor, ratio = None, 0.0
    for f in fallas:
        if not f.startswith("C"):
            continue
        m = RE_VALOR_UMBRAL.search(f)
        if not m:
            continue
        r = float(m.group(1)) / float(m.group(2))
        if r > ratio:
            mejor, ratio = f.split(" ")[0], r
    return mejor


def es_marginal(fallas):
    """Toda falla C* queda dentro de 1,5× su umbral (H* no cuentan)."""
    hubo = False
    for f in fallas:
        if not f.startswith("C"):
            continue
        m = RE_VALOR_UMBRAL.search(f)
        if not m:
            return False
        hubo = True
        if float(m.group(1)) > MARGINAL_FACTOR * float(m.group(2)):
            return False
    return hubo


def clasificar_to(ident, m, v, d_dry, inv):
    fallas = v["fallas"]
    cods = fallas_codigos(fallas)
    cuerpo_v = m["paginas_cuerpo_vigente"]
    secc_cuerpo = m["secciones_vigente"]["en_cuerpo"]
    espina = m["espina"]["labels_total"]
    pct_tab = m["tablas"]["pct_palabras_tabla"]
    unidades_sel = int(inv["unidades_extraccion"])
    cuerpo_sel = d_dry["paginas_cuerpo"]

    sec_variante = any(k in m["sondas_seccion"]
                       for k in ("SECCION_MAYUSCULAS", "seccion_romana"))
    jer_alt = any(k in m["sondas_seccion"]
                  for k in ("capitulo", "titulo_jerarquico", "anexo", "parte"))

    ev = []  # evidencia citada (página / muestra verbatim)

    # --------------------------------------------------- familia primaria
    if m["tablas"]["palabras_total"] == 0:
        fam = "e"
        ev.append("sin texto extraíble (0 palabras en el PDF)")
    elif cuerpo_v == 0:
        if m["paginas_indice_vigente"] > 0:
            # la compuerta NO es el problema: el índice se reconoce y aun
            # así no queda ninguna página de cuerpo (historial/tabla de
            # origen consumen el resto)
            fam = "e"
            ev.append(f"índice reconocido ({m['paginas_indice_vigente']} pág) "
                      f"pero 0 páginas de cuerpo — roles vigentes: "
                      f"{m['roles_vigente']}")
        elif m["idx_laxo_fuerte"]:
            fam = "b_idx"
            s = m["idx_laxo_fuerte"][0]
            ev.append(f"candidato de índice no contemplado p.{s['pag']}: «{s['texto']}»")
        else:
            fam = "a"
            ev.append(f"{m['paginas']} páginas, roles vigentes "
                      f"{m['roles_vigente']} — sin página de índice")
    elif secc_cuerpo == 0:
        if sec_variante:
            fam = "b_sec"
            k = ("SECCION_MAYUSCULAS" if "SECCION_MAYUSCULAS" in m["sondas_seccion"]
                 else "seccion_romana")
            s = m["sondas_seccion"][k]["muestras"][0]
            ev.append(f"marcador variante ({k}) p.{s['pag']}: «{s['texto']}»")
        else:
            fam = "c"
            ev.append(f"{cuerpo_v} páginas de cuerpo vigentes, 0 líneas con "
                      f"formato de marcador de sección (ni variante)")
    elif unidades_sel == 0:
        # el E0 vigente ya lo engancha (gate + sección); el cero es del dry
        # sellado pre-B5.2 — pendiente de re-corrida
        fam = "b_idx" if cuerpo_sel == 0 else "b_sec"
        ev.append(f"regla B5.2 vigente ya lo engancha (cuerpo {cuerpo_sel}→"
                  f"{cuerpo_v}, secciones en cuerpo {secc_cuerpo}); "
                  f"re-corrida pendiente (B5.8.4)")
    elif pct_tab >= TAB_DOMINANTE or falla_dominante(fallas) == "C6":
        fam = "d"
        ev.append(f"{pct_tab} % de palabras en tabla de contenido; falla "
                  f"dominante {falla_dominante(fallas)}; fallas selladas: "
                  f"{sorted(cods)}")
    elif cods & {"C4", "C5", "C7", "C8"}:
        fam = "b_pts"
        dom = falla_dominante(fallas)
        f_dom = next((f for f in fallas if f.startswith(dom)), fallas[0])
        ev.append(f"estructura enganchada ({unidades_sel} unidades), falla "
                  f"dominante: {f_dom[:110]}")
    else:
        fam = "e"
        ev.append(f"sin causa asignable por reglas: fallas {sorted(cods)}")

    # ------------------------------------------------------- secundarias
    sec = []
    if fam != "d":
        if pct_tab >= TAB_DOMINANTE:
            sec.append("d_dominante")
        elif pct_tab >= TAB_PRESENTE:
            sec.append("d")
    if m["ficha_campo"]["pct_lineas"] >= FICHA_PCT:
        sec.append("ficha")
    if m["lista_codigo"]["pct_lineas"] >= LISTA_PCT:
        sec.append("lista_codigos")
    if espina == 0:
        sec.append("sin_espina")
    if fam not in ("b_idx",) and m["idx_laxo_fuerte"]:
        sec.append("b_idx")
    if fam not in ("b_sec",) and sec_variante:
        sec.append("b_sec")
    if jer_alt:
        sec.append("jerarquia_alternativa")
    if "C8" in cods:
        sec.append("c8_tramo_gigante")
    if fam == "b_pts" and es_marginal(fallas):
        sec.append("umbral_marginal")

    # ------------------------------------------- veredicto preliminar
    if fam == "e":
        veredicto = "candidato a NO segmentable — " + ev[0]
    elif fam == "a":
        ficha_lista = ("ficha" in sec or "lista_codigos" in sec)
        dens = espina / max(1, m["paginas"])
        if ficha_lista and espina >= 3 and dens < DENS_ESPINA_MIN:
            veredicto = ("parcialmente segmentable — preámbulo con espina "
                         "(B5.8.1); el cuerpo dominante es ficha/lista y "
                         "exige parser de registro (fuera de B5.8.1-3): "
                         "declarar en B5.8.4")
        elif pct_tab >= TAB_DOMINANTE and espina >= 3:
            veredicto = ("segmentable — B5.8.1 (espina de puntos) + "
                         "B5.8.3 (tabular dominante)")
        elif pct_tab >= TAB_DOMINANTE:
            veredicto = ("segmentable (tabular) — parser B5.8.3; "
                         "sin espina de puntos utilizable")
        elif espina >= 3:
            veredicto = ("segmentable con regla de familia a "
                         "(modo sin raíz de sección, B5.8.1)")
        elif pct_tab >= TAB_PRESENTE:
            veredicto = ("segmentable (tabular) — parser B5.8.3; "
                         "sin espina de puntos")
        elif "ficha" in sec or "lista_codigos" in sec:
            veredicto = ("candidato a NO segmentable en esta secuencia — "
                         "familia ficha/lista: exige parser de registro "
                         "(fuera de B5.8.1-3); declarar en B5.8.4")
        else:
            veredicto = (f"candidato a NO segmentable — espina insuficiente "
                         f"({espina} labels en {m['paginas']} pág), "
                         f"{pct_tab} % en tabla, sin marcadores")
    elif fam == "b_idx" and unidades_sel == 0 and cuerpo_v > 0 and secc_cuerpo > 0:
        veredicto = ("segmentable — regla vigente (B5.2); verificar "
                     "re-corrida en B5.8.4")
    elif fam == "b_sec" and unidades_sel == 0 and secc_cuerpo > 0:
        veredicto = ("segmentable — regla vigente (B5.2); verificar "
                     "re-corrida en B5.8.4")
    elif fam in ("b_idx", "b_sec"):
        veredicto = "segmentable con regla de familia b (marcador, B5.8.2)"
    elif fam == "c":
        if espina >= 3:
            veredicto = ("segmentable con regla de familia a/c "
                         "(raíz sintética de B5.8.1)")
        else:
            veredicto = (f"candidato a NO segmentable — cuerpo sin espina "
                         f"de puntos utilizable ({espina} labels) ni "
                         f"marcadores")
    elif fam == "d":
        veredicto = "segmentable (tabular) — parser B5.8.3"
    else:  # b_pts
        if "umbral_marginal" in sec:
            veredicto = ("segmentable hoy (umbral marginal) — adjudicar "
                         "en B5.8.4; afinado opcional B5.8.2")
        else:
            veredicto = ("segmentable con regla de familia b "
                         "(afinado de numeración/marcadores, B5.8.2)")

    return {
        "id": ident,
        "categoria": inv["categoria"],
        "titulo": inv["titulo_oficial"],
        "paginas": m["paginas"],
        "sellado": {"paginas_cuerpo": cuerpo_sel,
                    "secciones": d_dry["secciones"],
                    "unidades": unidades_sel,
                    "fallas": fallas},
        "vigente": {"paginas_cuerpo": cuerpo_v,
                    "paginas_indice": m["paginas_indice_vigente"],
                    "secciones_en_cuerpo": secc_cuerpo,
                    "espina_labels": espina,
                    "espina_raices": m["espina"]["raices_distintas"],
                    "pct_palabras_tabla": pct_tab,
                    "pct_lineas_ficha": m["ficha_campo"]["pct_lineas"],
                    "pct_lineas_codigo": m["lista_codigo"]["pct_lineas"]},
        "familia_primaria": fam,
        "secundarias": sec,
        "evidencia": ev,
        "muestras": {
            "idx_laxo_fuerte": m["idx_laxo_fuerte"][:3],
            "sondas_seccion": {k: v["muestras"][:2]
                               for k, v in m["sondas_seccion"].items()},
            "espina": m["espina"]["muestras"][:3],
        },
        "veredicto_preliminar": veredicto,
    }


def main():
    med, ver, dry, inv = cargar()
    universo = sorted(k for k, v in ver.items()
                      if v["veredicto"] == "necesita reglas")
    assert len(universo) == 84
    assert set(med) == set(universo), "mediciones incompletas"

    censo = {t: clasificar_to(t, med[t], ver[t], dry[t], inv[t])
             for t in universo}
    (SALIDA / "censo_84.json").write_text(
        json.dumps(censo, ensure_ascii=False, indent=1))

    from collections import Counter
    tally = Counter(c["familia_primaria"] for c in censo.values())
    tally_ri = Counter(c["familia_primaria"] for c in censo.values()
                       if c["categoria"] == "regimen_informativo")
    print("tally primaria (84):", dict(tally), "suma", sum(tally.values()))
    print("tally primaria RI (53):", dict(tally_ri), "suma", sum(tally_ri.values()))
    tally_ng = Counter(c["familia_primaria"] for c in censo.values()
                       if c["categoria"] == "normativa_general")
    print("tally primaria no-RI (31):", dict(tally_ng), "suma", sum(tally_ng.values()))

    # tabla de los 31 no-RI con estimaciones (insumo del RE-LAUDO, adenda §2.1)
    filas = []
    for t in universo:
        c = censo[t]
        if c["categoria"] != "normativa_general":
            continue
        cuerpo_est = c["vigente"]["paginas_cuerpo"] or c["paginas"]
        est_dens = round(DENSIDAD_NG * cuerpo_est)
        filas.append({
            "id": t, "titulo": c["titulo"], "paginas": c["paginas"],
            "familia": c["familia_primaria"],
            "unidades_hoy": c["sellado"]["unidades"],
            "espina_labels": c["vigente"]["espina_labels"],
            "cuerpo_base_estimacion": cuerpo_est,
            "unidades_est_densidad": est_dens,
            "usd_est_densidad": round(est_dens * TARIFA_UNIDAD, 2),
            "veredicto_preliminar": c["veredicto_preliminar"],
        })
    (SALIDA / "tabla_31_no_ri.json").write_text(
        json.dumps(filas, ensure_ascii=False, indent=1))
    tot_est = sum(f["unidades_est_densidad"] for f in filas)
    print(f"31 no-RI: unidades hoy {sum(f['unidades_hoy'] for f in filas)}, "
          f"espina {sum(f['espina_labels'] for f in filas)}, "
          f"est. densidad {tot_est} unid ≈ USD {tot_est*TARIFA_UNIDAD:.2f}")


if __name__ == "__main__":
    main()
