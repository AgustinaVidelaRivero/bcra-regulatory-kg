#!/usr/bin/env python3
"""B5.8.4 — adjudicación de la partición final contra criterios YA SELLADOS
(esta unidad no escribe reglas ni criterios nuevos). Cada fila cita su
criterio; fuentes selladas usadas en solo lectura:

  S1 veredictos_generalizacion.json — umbrales C4–C8 de la banda de
     referencia y veredicto digerible/necesita-reglas de los 152.
  S2 reporte_generalizacion.evaluar() — la implementación sellada de la
     evaluación C4–C8 (importada por path, sin editar), aplicada acá a las
     unidades EMITIDAS por la corrida b584 de cada b_pts.
  S3 censo_84.json / censo_84.md — familias, veredictos preliminares (los 5
     marginales «adjudicar en B5.8.4 sin regla nueva»; los candidatos a NO
     con su causa; los 2 parciales por cuerpo ficha/lista con el corte
     DENS_ESPINA_MIN de clasificar_84.py) y hallazgo 2 (ri_tsa).
  S4 conteos_b581/b582/b583.json — límites MEDIDOS por las sub-unidades
     (reinicios por anexo/apartado, débiles declarados, ficha_registro,
     vía tabular); acá se citan, no se re-miden.
  S5 healthcheck_e0.py — señales por TO; su veredicto es de LECTURA, no un
     gate (docstring sellado del módulo).
  S6 criterio de rendimiento de b581/b582 (campo `rinde` sellado):
     unidades de extracción > 0 y ≥ 1 raíz de lectura no sintética-0.

Produce: ../adjudicaciones_b584.json (filas 3.a–3.f del mandato, con
criterio citado) y ../particion_152.json (partición final por TO y
agregados). Reporte legible: generar_reporte_b584.py.

Uso (desde cualquier cwd):
    python3 data/experiment/segmentacion_84/b584_particion/code/adjudicar_b584.py
"""

from __future__ import annotations

import csv
import importlib.util
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[5]
PREP = REPO / "data/experiment/escalado_prep"
SEG = REPO / "data/experiment/segmentacion_84"
SALIDA = Path(__file__).resolve().parents[1]


def cargar_modulo(nombre: str, ruta: Path):
    spec = importlib.util.spec_from_file_location(nombre, ruta)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[nombre] = mod
    spec.loader.exec_module(mod)
    return mod


def leer(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def art(to: str, nombre: str):
    return leer(SALIDA / to / f"{nombre}_{to}.json")


# ---------------------------------------------------------------- carga
censo = leer(SEG / "censo_84.json")
veredictos = leer(PREP / "veredictos_generalizacion.json")
UMBRALES = veredictos["umbrales"]
por_to_sellado = veredictos["por_to"]
b581 = leer(SEG / "b581_sin_raiz/conteos_b581.json")
b582 = leer(SEG / "b582_marcadores/conteos_b582.json")
b583 = leer(SEG / "b583_tablas/conteos_b583.json")
conteos = leer(SALIDA / "conteos_b584.json")
categoria = {r["id"]: r["categoria"]
             for r in csv.DictReader(open(PREP / "inventario_unidades.csv",
                                          encoding="utf-8"))}
repgen = cargar_modulo("reporte_generalizacion",
                       PREP / "code/reporte_generalizacion.py")

assert len(conteos) == 152, f"corrida incompleta: {len(conteos)}/152"

digeribles = sorted(t for t, d in por_to_sellado.items()
                    if d["veredicto"] == "digerible")
los_84 = sorted(censo)

# grupos del alcance (regla i — mismo cruce del freno del mandato)
g1 = {t for t, d in b581.items()
      if d.get("unidades_extraccion", 0) > 0 and t != "ri_acsf"}
g2 = {t for t in b582 if t != "ri_tsa"}
g5 = {t for t, d in censo.items() if d["familia_primaria"] == "b_pts"}
g5_marginales = {t for t in g5 if "umbral_marginal" in censo[t]["secundarias"]}
g6 = {t for t, d in censo.items()
      if d["veredicto_preliminar"].startswith("candidato a NO segmentable")}
assert (len(g1), len(g2), len(g5), len(g6)) == (41, 7, 22, 12)


def evaluacion_c48(to: str) -> dict:
    """Evaluación C4–C8 con la implementación SELLADA (S2) sobre las
    unidades EMITIDAS por la corrida b584 (post sub-chunking de U-B5.3,
    que es mecanismo sellado del pipeline). El health-check (S5) computa
    además la señal de tamaño PRE-partición; ambas se declaran."""
    c = conteos[to]
    chunks = art(to, "chunks")
    indice = art(to, "indice")
    div = art(to, "divergencias")
    cob = art(to, "cobertura")
    corr = art(to, "correcciones")
    terminales = [x for x in chunks if x["tipo"] != "mini_chunk"]
    tabulares = [x for x in chunks if x["flags"]["contenido_tabular"]]
    diag = {
        "cobertura": cob,
        "rechazos_header": {"total": c["rechazos_header"],
                            "por_motivo": c["rechazos_por_motivo"]},
        "fronteras": {"intra_palabra_despues":
                      corr["fronteras_intra_palabra"]["despues"]},
        "indice": {"puntos_en_indice":
                   sum(1 for e in indice if e["tipo"] == "punto"),
                   "anunciado_sin_cuerpo": len(div["anunciado_sin_cuerpo"]),
                   "en_cuerpo_sin_anunciar": len(div["en_cuerpo_sin_anunciar"])},
        "tabular": {"pct_chunks_tabulares":
                    round(100 * len(tabulares) / len(chunks), 2) if chunks else 0.0,
                    "chunks_con_contenido_tabular": len(tabulares),
                    "chunks_con_formula":
                    sum(1 for x in chunks if x["flags"]["formula"])},
        "avisos": {"total": c["avisos"], "por_tipo": c["avisos_por_tipo"]},
        "escala": {"max_chars_propio_terminal":
                   max((x["chars_propio"] for x in terminales), default=0)},
        "saltos_numeracion": c["saltos_numeracion"],
    }
    cc = {"diagnostico": diag,
          "unidades_extraccion": c["unidades_extraccion"],
          "secciones": c["raices_de_lectura"],
          "chunks_terminales": c["chunks_terminales"]}
    veredicto, fallas, flags = repgen.evaluar(cc, UMBRALES)
    return {"veredicto_evaluar": veredicto, "fallas": fallas, "flags": flags}


def base(to: str) -> dict:
    c = conteos[to]
    fila = {
        "to": to,
        "categoria": "RI" if categoria[to] == "regimen_informativo" else "no-RI",
        "paginas": c["paginas"],
        "modo_lectura": c["modo_lectura"],
        "unidades": c["unidades_extraccion"],
        "raices": c["raices_de_lectura"],
        "rinde": c["rinde"],
        "cobertura_exacta": c["cobertura_exacta"],
        "salud": c["healthcheck_veredicto"],
    }
    if "tabular" in c:
        fila["tabular"] = c["tabular"]
    return fila


adj: dict = {"_fuentes": ["S1 veredictos_generalizacion.json (umbrales C4-C8)",
                          "S2 reporte_generalizacion.evaluar() sellado",
                          "S3 censo_84.json/md (B5.8.0)",
                          "S4 conteos_b581/b582/b583.json",
                          "S5 healthcheck_e0.py (lectura, no gate)",
                          "S6 criterio rinde de b581/b582"]}

# ---------------------------------------------------------- 3.a — 22 b_pts
filas_a = []
for to in sorted(g5):
    c = conteos[to]
    ev = evaluacion_c48(to)
    fallas_sell = [f for f in censo[to]["sellado"]["fallas"] if f.startswith("C")]
    marginal = to in g5_marginales
    # adjudicación: produce unidades por el camino VIGENTE (jamás entra a
    # las etapas nuevas — verificado), rinde (S6) y cobertura exacta; las
    # fallas C* remanentes y las señales de salud se DECLARAN (S5: lectura,
    # no gate; adenda §1: se declara, no se fuerza; S3: el censo ya lo
    # clasifica «segmentable»). El afinado de B5.8.2 no se construyó (cerró
    # con cero reglas b_pts, declarado a B5.8.4): queda como límite.
    reconocido = (c["rinde"] and c["cobertura_exacta"]
                  and not c["activado_por_cero_unidades"])
    # corrección de la revisión del freno (fila dictada por la autora sobre
    # la resolución R1): un b_pts que en la re-corrida sale DIGERIBLE por el
    # evaluar() sellado (cero fallas) y con salud sana quedó CURADO por las
    # reglas B5.2 vigentes — se adjudica pleno-digerible con el mismo
    # criterio sellado (S2 + S5), sin criterio nuevo. Caso medido: rmgcti.
    digerible = (ev["veredicto_evaluar"] == "digerible"
                 and not ev["fallas"]
                 and conteos[to]["healthcheck_veredicto"] == "sano")
    filas_a.append({
        **base(to),
        "familia": "b_pts",
        "marginal_censo": marginal,
        "vigente_confirmado": not c["activado_por_cero_unidades"],
        "fallas_selladas_censo": fallas_sell,
        "evaluar_b584": ev,
        "adjudicacion": ("reconocido_pleno_digerible" if reconocido and digerible
                         else "reconocido_con_senales_declaradas" if reconocido
                         else "REVISAR"),
        "criterio": (("curado por B5.2; evaluar sellado: digerible, cero "
                      "fallas, salud sana (S2 + S5; fila de la revisión del "
                      "freno) + " if digerible else "")
                     + ("S3 veredicto censal «segmentable hoy (umbral marginal) — "
                        "adjudicar en B5.8.4 sin regla nueva»" if marginal else
                        "S3 veredicto censal «segmentable con regla de familia b» "
                        "(afinado no construido: B5.8.2 cerró con cero reglas "
                        "b_pts, declarado a B5.8.4)")
                     + " + S2 evaluar() sobre unidades emitidas + S6 rinde + S5 "
                       "señales declaradas (lectura, no gate)"),
    })
adj["a_bpts"] = filas_a

# --- diferencias de fallas C* entre el sellado del censo y la re-corrida
# (resolución R1 de la revisión del freno): para todo b_pts cuyo conjunto de
# códigos C* cambió, se miden las causas desde los artefactos — el sellado
# del censo cita e0_dry (PRE-B5.2, sin sub-chunking); la re-corrida es el
# camino vigente de HEAD + sub-chunking de U-B5.3. La batería prueba que los
# caminos sellados (dev/68/ESQ) quedaron byte-idénticos: estos deltas viven
# SOLO en TOs «necesita reglas», nunca sellados.
dry = leer(PREP / "e0_dry/conteos_e0_dry.json")
difs_c = []
for f in filas_a:
    to = f["to"]
    cods_sell = {x.split(" ")[0] for x in f["fallas_selladas_censo"]}
    cods_new = {x.split(" ")[0] for x in f["evaluar_b584"]["fallas"]
                if x.startswith("C")}
    if cods_sell == cods_new:
        continue
    d = dry[to]["diagnostico"]
    c = conteos[to]
    chunks = art(to, "chunks")
    term = [x for x in chunks if x["tipo"] != "mini_chunk"]
    tab = [x for x in chunks if x["flags"]["contenido_tabular"]]
    causas = []
    if (dry[to]["secciones"] != c["raices_de_lectura"]
            or d["rechazos_header"]["total"] != c["rechazos_header"]
            or d["avisos"]["total"] != c["avisos"]):
        causas.append("parse_vigente_post_sellado_B5.2")
    if c["sub_chunking"]["particiones"] > 0:
        causas.append("sub_chunking_UB53")
    difs_c.append({
        "to": to,
        "c_sellado": sorted(cods_sell), "c_b584": sorted(cods_new),
        "causas": causas,
        "medicion": {
            "unidades": [dry[to]["unidades_extraccion"], c["unidades_extraccion"]],
            "secciones": [dry[to]["secciones"], c["raices_de_lectura"]],
            "rechazos": [d["rechazos_header"]["total"], c["rechazos_header"]],
            "avisos": [d["avisos"]["total"], c["avisos"]],
            "anunciado_sin_cuerpo": [d["indice"]["anunciado_sin_cuerpo"],
                                     c["anunciado_sin_cuerpo"]],
            "pct_tabular": [d["tabular"]["pct_chunks_tabulares"],
                            round(100 * len(tab) / len(chunks), 2) if chunks else 0.0],
            "max_chars_terminal": [d["escala"]["max_chars_propio_terminal"],
                                   max((x["chars_propio"] for x in term), default=0)],
            "particiones": c["sub_chunking"]["particiones"],
        },
    })
adj["a_diferencias_c_vs_censo"] = {
    "nota": ("por qué difieren: el sellado censal cita e0_dry PRE-B5.2 y sin "
             "sub-chunking; la re-corrida mide el camino vigente de HEAD "
             "(cambios de B5.2 posteriores al sellado) sobre las unidades "
             "EMITIDAS (post sub-chunking de U-B5.3, que hereda flags de "
             "forma conservadora y declarada). Los caminos sellados quedaron "
             "byte-idénticos (batería dev/68/ESQ): los deltas viven solo en "
             "TOs nunca sellados."),
    "filas": difs_c,
}

# ---------------------------------------------------------- 3.b — ri_tsa
c = conteos["ri_tsa"]
tsa_tablas = leer(SALIDA / "ri_tsa" / "resumen_ri_tsa.json")
paginas_tabla = set(tsa_tablas["paginas_con_tabla"])
portada = c["roles_pagina"].get("portada", 0)
paginas_portada = set(range(1, portada + 1)) if portada else set()
adj["b_ri_tsa"] = {
    **base("ri_tsa"),
    "verificacion_control_b582": {
        "esperado_S4": {k: b582["ri_tsa"][k] for k in
                        ("modo_lectura", "unidades_extraccion",
                         "raices_de_lectura", "healthcheck_veredicto")},
        "obtenido_b584": {"modo_lectura": c["modo_lectura"],
                          "unidades_extraccion": c["unidades_extraccion"],
                          "raices_de_lectura": c["raices_de_lectura"],
                          "healthcheck_veredicto": c["healthcheck_veredicto"]},
        "coincide": all(b582["ri_tsa"][k] == c[k] for k in
                        ("modo_lectura", "unidades_extraccion",
                         "raices_de_lectura", "healthcheck_veredicto")),
    },
    "que_queda_fuera": {
        "paginas_portada": portada,
        "portada_cubierta_por_tablas": len(paginas_portada & paginas_tabla),
        "portada_sin_via": sorted(paginas_portada - paginas_tabla)[:60],
        "tablas_logicas_total": tsa_tablas["tablas_logicas"],
    },
    "adjudicacion": "reconocido_con_limite_declarado",
    "criterio": ("S3 hallazgo 2 del censo (verificar re-corrida y qué queda "
                 "fuera) + S3 veredicto «segmentable — regla vigente (B5.2)» "
                 "+ S6 rinde + S4 vía tabular b583 para el material de las "
                 "páginas previas al índice"),
}

# ------------------------------------------------------- 3.c — reinicios
REINICIOS = {
    "nmaeef": ("S4 b582: reinicio de numeración por ANEXO medido (198 "
               "rechazos registrados), rinde 39 u/13 raíces — límite "
               "declarado sin regla en el cierre de B5.8.2"),
    "ri_tar": ("S4 b581: débil declarado sin forzar (1 raíz / 2 unidades; "
               "reinicio por apartado)"),
    "ri_transpa": ("S4 b581: débil declarado sin forzar (1 raíz / 2 "
                   "unidades; reinicio por apartado) + S4 b583: 21 tablas "
                   "lógicas parseadas por su vía"),
    "ri2_ae": ("S4 b581: reinicio por apartado medido en los rechazos "
               "(fuera_de_seccion dominante, 135), rinde 18 u/10 raíces"),
    "manual": ("S4 b581: preámbulo 19 u/2 raíces; el cuerpo dominante es "
               "ficha (1.830 pág declaradas ficha_registro)"),
}
filas_c = []
for to, limite in REINICIOS.items():
    c = conteos[to]
    # criterio de la frontera pleno/parcial: la definición sellada de
    # «parcial» del censo (S3, clasificar_84: cuerpo dominante ficha/lista
    # con espina-preámbulo por DENS_ESPINA_MIN) — no la granularidad.
    parcial_censo = censo[to]["veredicto_preliminar"].startswith("parcialmente")
    filas_c.append({
        **base(to),
        "limite_medido": limite,
        "adjudicacion": ("parcial_declarado" if parcial_censo
                         else "reconocido_con_limite_declarado"),
        "criterio": ("S3 definición sellada de parcial (cuerpo dominante "
                     "ficha/lista, DENS_ESPINA_MIN de clasificar_84)"
                     if parcial_censo else
                     "S3 veredicto censal segmentable + S6 rinde con "
                     "cobertura exacta: el documento entero queda leído en "
                     "unidades (granularidad gruesa por el reinicio, "
                     "declarada) — no es parcial por el criterio sellado")
        + "; el límite se cita de S4, no se re-mide (mandato 3.c)",
    })
adj["c_reinicios"] = filas_c

# ------------------------------------------- 3.d — familia parser de registro
filas_d = []
for to in sorted(conteos):
    fr = conteos[to]["roles_pagina"].get("ficha_registro", 0)
    if fr == 0 and to != "plandecuentas":
        continue
    fila = {"to": to, "paginas": conteos[to]["paginas"],
            "paginas_ficha_registro": fr,
            "tablas_logicas_parseadas":
                conteos[to].get("tabular", {}).get("parseadas", 0)}
    if to == "plandecuentas":
        fila["nota"] = ("familia ficha/lista completa del censo (S3); la "
                        "corrida b584 lo confirma con el rol derivado: "
                        f"{fr} páginas ficha_registro y 0 unidades de prosa")
    filas_d.append(fila)
adj["d_parser_registro"] = {
    "filas": filas_d,
    "declaracion": ("familia DECLARADA «parser de registro», fuera de la "
                    "secuencia B5.8.1-3 (S3: censo §4 y veredicto de "
                    "plandecuentas/manual/ri2_pm); el material ficha_registro "
                    "queda fuera del parseo de prosa con su evidencia por TO "
                    "(rol de página de B5.8.1) y su porción tabular rinde por "
                    "B5.8.3 donde existe"),
    "criterio": "S3 censo B5.8.0 §4 + S4 b581 (rol ficha_registro) + S4 b583",
}

# ------------------------------------------------- 3.e — 12 candidatos a NO
filas_e = []
for to in sorted(g6):
    c = conteos[to]
    salud_art = art(to, "healthcheck")
    filas_e.append({
        **base(to),
        "causa_censo": censo[to]["veredicto_preliminar"],
        "espina_labels_censo": censo[to]["vigente"]["espina_labels"],
        "evidencia_b584": {
            "modo_final": c["modo_lectura"],
            "unidades": c["unidades_extraccion"],
            "raices": c["raices_de_lectura"],
            "senales_salud": salud_art["veredicto"],
            "roles_pagina": c["roles_pagina"],
        },
        "declaracion": "no_segmentable_declarado",
        "criterio": ("S3 causa censal verbatim + corte sellado espina≥3 de "
                     "clasificar_84 (una salida con <3 raíces reales no es "
                     "segmentación reconocida: declarar, no forzar — adenda "
                     "§1) + S5 señales como evidencia"),
        # HALLAZGO reportado, no resuelto: 3 de los 12 emiten 1-2 unidades
        # degeneradas en modo sin_raiz y pasan el criterio S6 formal (rinde),
        # pero quedan del lado NO del corte sellado espina≥3; promoverlos
        # exigiría un criterio nuevo (precedencia de S6 sobre el censo), que
        # esta unidad no puede crear — la evidencia queda completa en la fila
        # y la decisión es de la autora.
        "hallazgo_rinde_tecnico": bool(c["rinde"]),
    })
adj["e_no_segmentables"] = filas_e

# ------------------------------------- 3.f — huecos B5.4 (docvig, fimipyme)
def busca_alcance(to: str) -> dict:
    indice = art(to, "indice")
    chunks = art(to, "chunks")
    div = art(to, "divergencias")
    idx = [e for e in indice if "alcanzad" in e.get("titulo", "").lower()]
    uni = [{"id": x["id"], "titulo": x["titulo"]} for x in chunks
           if "alcanzad" in x.get("titulo", "").lower()]
    asc = [e for e in div["anunciado_sin_cuerpo"]
           if "alcanzad" in str(e).lower()]
    return {"to": to, "modo_lectura": conteos[to]["modo_lectura"],
            "entradas_indice_alcance": idx, "unidades_alcance": uni,
            "anunciado_sin_cuerpo_alcance": asc,
            "unidades_totales": conteos[to]["unidades_extraccion"],
            "salud": conteos[to]["healthcheck_veredicto"]}

adj["f_huecos_b54"] = {
    "filas": [busca_alcance("docvig"), busca_alcance("fimipyme")],
    "nota": ("SOLO REPORTE (anticipa la vigilancia (6) de B6.1; el catálogo "
             "no se toca). Ambos TOs son digeribles: producen unidades por el "
             "camino vigente y la garantía estructural de B5.8.1/2 impide que "
             "las reglas nuevas los toquen (byte-identidad verificada en la "
             "batería) — cualquier hueco sellado persiste por construcción."),
}

# ------------------------------------------------------- partición final
particion: dict[str, dict] = {}
for to in sorted(conteos):
    c = conteos[to]
    if to in digeribles:
        clase, via = "reconocido_pleno", "vigente (sellada pre-B5.8)"
        criterio = "S1 veredicto digerible + batería byte-idéntica vs e0_dry"
    elif to in g6:
        clase, via = "no_segmentable_declarado", "—"
        criterio = "fila 3.e"
    elif censo[to]["veredicto_preliminar"].startswith("parcialmente"):
        clase, via = "parcial_declarado", f"{c['modo_lectura']} (preámbulo) + tabular/registro"
        criterio = "fila 3.c/3.d (S3 parcial censal)"
    elif to == "ri_acsf":
        clase, via = "reconocido_pleno", "tabular (B5.8.3)"
        criterio = ("S3 veredicto «segmentable (tabular)» + S4 b583 rinde "
                    "(1 tabla lógica; control negativo de b581 confirmado)")
    else:
        clase = "reconocido_pleno"
        via = c["modo_lectura"] + (" + tabular" if "tabular" in c else "")
        criterio = ("fila 3.a" if to in g5 else
                    "fila 3.b" if to == "ri_tsa" else
                    "fila 3.c" if to in REINICIOS else
                    "S4 rinde b581/b582 + S6 + S5 señales declaradas")
    particion[to] = {
        "clase": clase, "via": via, "criterio": criterio,
        "categoria": "RI" if categoria[to] == "regimen_informativo" else "no-RI",
        "paginas": c["paginas"],
        "unidades": c["unidades_extraccion"],
        "tablas_logicas": c.get("tabular", {}).get("parseadas", 0),
        "paginas_ficha_registro": c["roles_pagina"].get("ficha_registro", 0),
        "salud": c["healthcheck_veredicto"],
        "limite_declarado": to in {f["to"] for f in filas_c
                                   if f["adjudicacion"]
                                   == "reconocido_con_limite_declarado"}
        or to == "ri_tsa",
    }

agg: dict[str, dict] = {}
for clase in ("reconocido_pleno", "parcial_declarado", "no_segmentable_declarado"):
    tos = [t for t, d in particion.items() if d["clase"] == clase]
    agg[clase] = {
        "tos": len(tos),
        "paginas": sum(particion[t]["paginas"] for t in tos),
        "unidades": sum(particion[t]["unidades"] for t in tos),
        "tablas_logicas": sum(particion[t]["tablas_logicas"] for t in tos),
        "sanos": sum(1 for t in tos if particion[t]["salud"] == "sano"),
    }
assert sum(a["tos"] for a in agg.values()) == 152

# -------------------------------------------- tabla del re-laudo (tanda 2)
filas_relaudo = []
for to in los_84:
    if categoria[to] != "normativa_general":
        continue
    if particion[to]["clase"] == "no_segmentable_declarado":
        continue
    filas_relaudo.append({
        "to": to,
        "clase": particion[to]["clase"],
        "paginas": particion[to]["paginas"],
        "unidades_reales": particion[to]["unidades"],
        "tablas_logicas": particion[to]["tablas_logicas"],
        "salud": particion[to]["salud"],
        "salud_verde": particion[to]["salud"] == "sano",
    })
adj["tabla_relaudo_tanda2"] = {
    "nota": ("SOLO INFORMA (re-laudo de la autora del 06/09: incorporación "
             "en principio, corte final sobre unidades reales con "
             "health-check en verde por documento, re-presupuesto en B5.7)"),
    "filas": filas_relaudo,
    "total_unidades_reales": sum(f["unidades_reales"] for f in filas_relaudo),
    "con_salud_verde": sum(1 for f in filas_relaudo if f["salud_verde"]),
}

# --- resolución R2 de la revisión del freno: definición exacta del
# «rinden 142/152» del log. `rinde` es MEDICIÓN por TO (criterio S6 del
# runner, heredado verbatim de b581/b582): unidades emitidas > 0 Y ≥1 raíz
# de lectura real (el preámbulo sintético S0 no cuenta). La partición es
# ADJUDICACIÓN; el cruce clase × rinde se recomputa acá.
cruce = {}
for to in conteos:
    k = (particion[to]["clase"], conteos[to]["rinde"])
    cruce.setdefault(f"{k[0]}|rinde={k[1]}", []).append(to)
adj["resolucion_r2_rinden"] = {
    "definicion": ("rinde (S6, medición del runner) = unidades_extraccion > 0 "
                   "y raices_de_lectura > 0 (raíces no sintéticas-0)"),
    "rinden_total": sum(1 for t in conteos if conteos[t]["rinde"]),
    "cruce_clase_rinde": {k: len(v) for k, v in sorted(cruce.items())},
    "plenos_sin_rinde": sorted(t for t in conteos
                               if particion[t]["clase"] == "reconocido_pleno"
                               and not conteos[t]["rinde"]),
    "no_segmentables_con_rinde": sorted(
        t for t in conteos
        if particion[t]["clase"] == "no_segmentable_declarado"
        and conteos[t]["rinde"]),
    "lectura": ("142 = 137 reconocidos plenos con rinde=True + 2 parciales "
                "(manual, ri2_pm: rinden con su preámbulo) + 3 no "
                "segmentables con rinde técnico (el hallazgo de 3.e); "
                "138 plenos = 137 + ri_acsf (rinde=False en prosa: su única "
                "unidad E0 es el S0 sin raíz; reconocido por su vía TABULAR)"),
}

(SALIDA / "adjudicaciones_b584.json").write_text(
    json.dumps(adj, ensure_ascii=False, indent=1), encoding="utf-8")
(SALIDA / "particion_152.json").write_text(
    json.dumps({"por_to": particion, "agregados": agg},
               ensure_ascii=False, indent=1), encoding="utf-8")

print("partición:", {k: v["tos"] for k, v in agg.items()})
print("agregados:", json.dumps(agg, ensure_ascii=False, indent=1))
print("re-laudo tanda 2:", len(filas_relaudo), "TOs no-RI,",
      adj["tabla_relaudo_tanda2"]["total_unidades_reales"], "unidades reales,",
      adj["tabla_relaudo_tanda2"]["con_salud_verde"], "con salud verde")
from collections import Counter as _C
print("b_pts:", dict(_C(f["adjudicacion"] for f in filas_a)),
      "| plenos digeribles:", [f["to"] for f in filas_a
                               if f["adjudicacion"] == "reconocido_pleno_digerible"])
print("diferencias C* vs censo:", [(d["to"], d["causas"]) for d in difs_c])
print("R2:", adj["resolucion_r2_rinden"]["cruce_clase_rinde"])
