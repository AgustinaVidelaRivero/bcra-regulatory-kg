"""
censo_p1.py — U-PROMPT-R2, P1.c y P1.d (parte que sale del crudo guardado de la
tanda 0). USD 0: ninguna llamada a la API; solo lectura del repo.

Mide sobre el crudo guardado de E1 de la tanda 0 (corpus_tanda0/salida_dirigida,
last-wins por chunk_id, 2.434 unidades) y la E0 legada con la que se extrajo
(e0_chunking/salida_tanda0):
  1. calibración tokens ↔ caracteres: salida de E1 (JSON del tool call) y
     mensaje de usuario (sin caché), por regresión sobre las 2.434 unidades;
  2. tokens del prefijo (system + tool schema) del borrador r2, con la recta
     ajustada sobre cuatro prefijos medidos (produccion_dev 9.983; canal
     abierto P1ter 10.801; esq3b_v2 11.933; v3_b54 15.433);
  3. caracteres de salida que agregan o quitan los campos nuevos, por unidad:
     tramo de evidencia (decisión 15), umbrales como tramos (decisión 3),
     frecuencia (variantes A y B, decisión 20), mención del sujeto (decisión 4),
     omisiones con categoría y tramo (decisión 5), campos que salen
     (decisión 16), otras_propiedades (decisión 17);
  4. riesgo de corte contra 8.192 (primer intento) y 16.384 (reintento r2,
     cliente_e1.MAX_TOKENS_REINTENTO_CORTE_R2);
  5. costo por unidad y totales con la fórmula de caching (decisión 2 de
     docs/decisiones_caching_extraccion.md) y las tarifas de runner_corpus.py:18-19.

Las estimaciones van rotuladas: ninguna es una medición del prefijo nuevo, que
recién mide la pareada de P4. El mensaje nuevo (con el bloque de tablas) y la
NOTA de E3 se miden sobre la E0 e0-r2 versionada por la M1 de U-MED-R2A
(`f8dedd4`), con el borrador de p1/mensaje_r2_borrador.py.

Uso: python -B censo_p1.py <repo> <dir_borrador> <salida.json>
"""
from __future__ import annotations

import json
import re
import statistics as st
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

REPO = Path(sys.argv[1])
BORR = Path(sys.argv[2])
SALIDA = Path(sys.argv[3])
for p in ("data/experiment/b54_catalogo_v3/code", "data/experiment/esq/code",
          "data/experiment/reextraccion_v2/e1_extractor", "data/experiment/pyd_r2/code",
          "data/experiment/reextraccion_v2/e3_verificador"):
    sys.path.insert(0, str(REPO / p))
import perfil_e1  # noqa: E402
import prompt_v3_b54 as v3  # noqa: E402
import prompt_e1 as pe1  # noqa: E402
import prompt_esq3b_v2 as pv2  # noqa: E402
import validador_r2 as V  # noqa: E402
import reglas_comparacion as RC  # noqa: E402
import modelos_r2 as M  # noqa: E402

TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
CRUDO = REPO / "data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida"
E0 = REPO / "data/experiment/reextraccion_v2/e0_chunking/salida_tanda0"
PREC = {"in": 1.00, "out": 5.00, "cw": 1.25, "cr": 0.10}          # E1, USD/MTok (runner_corpus.py:18)
PREC_E3 = {"in": 2.00, "out": 10.00, "cw": 2.50, "cr": 0.20}      # E3 (runner_corpus.py:19)
J = lambda o: json.dumps(o, ensure_ascii=False)  # noqa: E731
H = 2  # holgura de la política r2 (politica_campos_r2.json, mencion_holgura_tokens)

perfil = perfil_e1.perfil("v3_b54")


def cargar_jsonl_last_wins(p: Path) -> dict:
    out = {}
    for l in p.open(encoding="utf-8"):
        if l.strip():
            r = json.loads(l)
            out[r["chunk_id"]] = r
    return out


def chunks_de(to: str) -> dict:
    d = json.loads((E0 / f"chunks_{to}.json").read_text(encoding="utf-8"))
    d = d if isinstance(d, list) else d.get("chunks", [])
    return {c["id"]: c for c in d}


# ------------------------------------------------------------------------- #
# Catálogo r2: labels y alias por id (para estimar la mención)               #
# ------------------------------------------------------------------------- #
cat = json.loads((REPO / "data/experiment/catalogo_unico/catalogo_sujetos_r2.json").read_text(encoding="utf-8"))
FORMAS = defaultdict(set)
for s in cat["sujetos"]:
    for k in ("label", "label_corto"):
        v = s.get(k)
        if isinstance(v, dict):
            v = v.get("valor")
        if isinstance(v, str) and v:
            FORMAS[s["id"]].add(v)
    al = s.get("alias") or []
    if isinstance(al, dict):
        al = al.get("valor") or []
    for a in al:
        a = a.get("valor") if isinstance(a, dict) else a
        if isinstance(a, str) and a:
            FORMAS[s["id"]].add(a)


def fold(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c)).lower()


ARTICULO = re.compile(r"(?:\b(?:las|los|la|el|del|al|a las|a los)\s+)$", re.I)
COLECTIVOS = ("las entidades financieras", "las entidades", "la entidad financiera", "la entidad",
              "los sujetos obligados", "el banco", "los bancos")


def mencion_estimada(sid: str | None, texto: str) -> tuple[int, str]:
    """Largo estimado de la mención que el modelo copiaría: la forma (label o
    alias) del id que aparezca en el texto, con su artículo; si no aparece, el
    primer colectivo del TO que aparezca; si tampoco, 15 caracteres."""
    ft = fold(texto)
    mejor = None
    for f in sorted(FORMAS.get(sid or "", ()), key=len, reverse=True):
        ff = fold(f)
        # singular/plural laxo: la forma sin la s final
        for cand in (ff, ff[:-1] if ff.endswith("s") else ff):
            i = ft.find(cand)
            if i >= 0:
                art = ARTICULO.search(ft[max(0, i - 8):i])
                largo = len(cand) + (len(art.group(0)) if art else 0)
                mejor = (largo, "forma_del_id")
                break
        if mejor:
            break
    if mejor:
        return mejor
    for c in COLECTIVOS:
        if fold(c) in ft:
            return len(c), "colectivo"
    return 15, "por_defecto"


# ------------------------------------------------------------------------- #
# Carga                                                                      #
# ------------------------------------------------------------------------- #
unidades = []
for to in TOS:
    regs = cargar_jsonl_last_wins(CRUDO / to / "extracciones_e1.jsonl")
    cs = chunks_de(to)
    for cid, r in regs.items():
        unidades.append((to, cid, r, cs.get(cid)))
n_sin_chunk = sum(1 for u in unidades if u[3] is None)

# ------------------------------------------------------------------------- #
# 1. Calibración de tokens                                                   #
# ------------------------------------------------------------------------- #
xo, yo, xi, yi = [], [], [], []
cw_unidades = []
for to, cid, r, c in unidades:
    ti = r.get("tool_input_crudo")
    u = r["usage"]
    if r.get("error") is None and ti is not None and r.get("stop_reason") == "tool_use":
        xo.append(len(J(ti)))
        yo.append(u["output_tokens"])
    if c is not None:
        xi.append(len(perfil.build_user_message(c)))
        yi.append(u["input_tokens"])
    if u["cache_write_tokens"]:
        cw_unidades.append(cid)


def recta(x, y):
    A = np.vstack([np.ones(len(x)), x]).T
    (a, b), *_ = np.linalg.lstsq(A, np.array(y, float), rcond=None)
    # errstate: el matmul de numpy en macOS (Accelerate) levanta avisos espurios de
    # overflow con matrices de esta forma; los valores son finitos (se controlan abajo).
    with np.errstate(all="ignore"):
        pred = A @ np.array([a, b])
    assert np.all(np.isfinite(pred))
    rel = np.abs(np.array(y) - pred) / np.maximum(np.array(y), 1)
    return float(a), float(b), float(np.median(rel)), float(np.percentile(rel, 90))


cal_out = recta(xo, yo)
cal_in = recta(xi, yi)
ratio_out = sum(yo) / sum(xo)

# ------------------------------------------------------------------------- #
# 2. Prefijo                                                                 #
# ------------------------------------------------------------------------- #
pref_pts = [(pe1.PREFIJO_SISTEMA, pe1.TOOL_SCHEMA_E1, 9983),
            (pe1.prefijo_sistema(True), pe1.TOOL_SCHEMA_E1_CANAL_ABIERTO, 10801),
            (pv2.PREFIJO_SISTEMA_V2, pv2.TOOL_SCHEMA_V2, 11933),
            (v3.PREFIJO_SISTEMA_V3, v3.TOOL_SCHEMA_V3, 15433)]
A3 = np.array([[1, len(s), len(J(t))] for s, t, _ in pref_pts], float)
y3 = np.array([k for *_, k in pref_pts], float)
c3, *_ = np.linalg.lstsq(A3, y3, rcond=None)
A2 = np.array([[1, len(s) + len(J(t))] for s, t, _ in pref_pts], float)
c2, *_ = np.linalg.lstsq(A2, y3, rcond=None)
ts_r2 = json.loads((BORR / "generados_d15_17/tool_schema_r2.json").read_text(encoding="utf-8"))
ts_hoy = json.loads((BORR / "generados_hoy/tool_schema_r2.json").read_text(encoding="utf-8"))
prefijos = {}
for var in ("A", "B"):
    s = (BORR / f"prefijo_r2_borrador_{var}.txt").read_text(encoding="utf-8")
    S, T = len(s), len(J(ts_r2))
    prefijos[var] = {"chars_system": S, "chars_tool_schema": T,
                     "tokens_recta_3p": round(float(c3 @ [1, S, T])),
                     "tokens_recta_2p": round(float(c2 @ [1, S + T]))}
prefijo_v3 = {"chars_system": len(v3.PREFIJO_SISTEMA_V3), "chars_tool_schema": len(J(v3.TOOL_SCHEMA_V3)),
              "tokens_medidos": 15433}
residuos3 = (y3 - A3 @ c3).round(1).tolist()
residuos2 = (y3 - A2 @ c2).round(1).tolist()

# controles del tool schema de borrador
pred_enum = None
ent_items = ts_r2["input_schema"]["properties"]["entities"]["items"]["anyOf"]
pred_enum = ts_r2["input_schema"]["properties"]["relations"]["items"]["properties"]["predicate"]["enum"]
control_ts = {
    "predicados": len(pred_enum), "remite_a_en_tool_schema": "remite_a" in J(ts_r2),
    "tramo_requerido_por_tipo": {e["properties"]["type"]["const"]: ("tramo" in e.get("required", []))
                                 for e in ent_items},
    "comunicacion_props": sorted(next(e for e in ent_items if e["properties"]["type"]["const"] == "Comunicacion")
                                 ["properties"]["properties"]["properties"]),
    "textoordenado_tiene_properties": "properties" in next(
        e for e in ent_items if e["properties"]["type"]["const"] == "TextoOrdenado")["properties"],
    "relacion_otras_propiedades": "otras_propiedades" in ts_r2["input_schema"]["properties"]["relations"]["items"]["properties"],
    "omision_campos": sorted(ts_r2["input_schema"]["properties"]["omisiones"]["items"]["properties"]),
}

# ------------------------------------------------------------------------- #
# 3. Deltas de salida por unidad                                             #
# ------------------------------------------------------------------------- #
RE_META = re.compile(r"no implica|no debe(?:n|rá|ran)? entenderse|no importar[áa]|no constituye|tiene(?:n)? por (?:objeto|finalidad)|"
                     r"con el objeto de|a fin de (?:que )?(?:promover|asegurar|garantizar|evitar)|entrar[áa]n? en vigencia|"
                     r"(?:regir[áa]n?|ser[áa]n? de aplicaci[oó]n) a partir|vigencia", re.I)
CLAVES_DEF = {t: set(c) for t, c in M.CLAVES_R2.items()}
TRAMO_OMISION_CHARS = 100          # supuesto central del tramo de una omisión (≥ 11 tokens; U-PYD)
NOTA_NUEVA_CHARS = 60              # nota de una omisión nueva (meta, fuera_de_tipos, sin predicado)
LIMITE_RELATIVO_CHARS = 70         # tramo de un límite relativo, sin cuantía
VENTANA_MARCADOR = 50              # caracteres antes de la cuantía que incluyen su marcador

# F1-A (decisión de la autora del 03/10/2026; U-DIAG-PROCESO): en un ítem de lista (chunk de punto cuyo
# último bloque heredado termina en «:», definición de reports/u_diag_proceso/code/censo_estructural.py), la
# norma compuesta agrega a la salida el segmento del encabezado en el `tramo` (unido por « […] ») y, si la
# descripción guardada no lo trae, la parte del encabezado que completa la norma. Tipos compuestos:
# Obligacion, Restriccion y Potestad; un ítem con contenido y sin ninguno de esos tipos cuenta una entidad
# compuesta. Condicion queda fuera (el encabezado de condiciones no compone). La baja de nodos de solo
# anuncio en las unidades de encabezado no se descuenta (cota alta).
TIPOS_COMPUESTOS = ("Obligacion", "Restriccion", "Potestad")
SEPARADOR = " […] "
RE_NUMERACION = re.compile(r"^\s*(?:[0-9]+\.)+\s*")


def segmento_encabezado(her: list[dict]) -> str:
    """La cláusula del encabezado que abre la lista: la última oración del último bloque heredado; si el
    bloque no tiene una oración propia y el anterior es la línea de título de la misma unidad sin cerrar,
    las dos partes (caso de la ficha 52)."""
    seg = " ".join(her[-1]["texto"].split())
    i = seg.rfind(". ", 0, len(seg) - 1)
    if i != -1:
        return seg[i + 2:]
    if len(her) >= 2 and her[-2]["unidad_origen"] == her[-1]["unidad_origen"] \
            and not her[-2]["texto"].rstrip().endswith("."):
        seg = RE_NUMERACION.sub("", " ".join(her[-2]["texto"].split())) + " " + seg
    return RE_NUMERACION.sub("", seg)


def es_item_censo(c: dict) -> bool:
    her = c.get("herencia") or []
    return c.get("tipo") != "mini_chunk" and bool(her) and " ".join(her[-1]["texto"].split()).endswith((":", "："))


det = []
agg = Counter()
niveles_evid = defaultdict(Counter)
chars_evid_tipo = defaultdict(list)
niveles_termino = Counter()
mencion_origen = Counter()
plazos = Counter()
plazos_por_to = Counter()
for to, cid, r, c in unidades:
    ti = r.get("tool_input_crudo")
    if ti is None or c is None:
        continue
    texto = V.texto_completo(c)
    d = Counter()
    ents = ti.get("entities") or []
    for e in ents:
        if not isinstance(e, dict):
            continue
        t = e.get("type")
        props = e.get("properties") or {}
        if not isinstance(props, dict):
            props = {}
        desc = props.get("descripcion") if isinstance(props.get("descripcion"), str) else ""
        # decisión 15: tramo de evidencia (no en TextoOrdenado)
        if t == "TextoOrdenado":
            d["sale_textoordenado_properties"] -= len(J({"properties": props})) - 2 + 2 if props else 0
        else:
            if t == "Comunicacion":
                lab = e.get("label") or ""
                largo = max(len(lab) + 10, 20)
                nivel = "comunicacion_cita"
            else:
                aguja = desc or (e.get("label") or "")
                nivel, minimo = V.verificar_tramo(aguja, texto, H)
                largo = len(minimo) if (nivel == "tokens" and minimo) else len(aguja)
            niveles_evid[t][nivel] += 1
            chars_evid_tipo[t].append(largo)
            d["tramo_evidencia"] += largo + len(', "tramo": ""')
            bajo = largo
            if t != "Comunicacion" and e.get("label"):
                nl, ml = V.verificar_tramo(e["label"], texto, None)
                if nl == "exacta":
                    bajo = min(largo, len(e["label"]))
                elif nl == "tokens" and ml:
                    bajo = min(largo, len(ml))
            d["tramo_evidencia_bajo"] += bajo + len(', "tramo": ""')
        if t == "Comunicacion":
            for k in ("tipo", "numero"):
                if k in props:
                    d["sale_comunicacion_tipo_numero"] -= len(J({k: props[k]})) - 2 + 2
        if t == "Definicion" and isinstance(props.get("termino"), str):
            niveles_termino[V.verificar_tramo(props["termino"], texto, H)[0]] += 1
        # otras_propiedades: claves fuera de la definición r2 (y de las heredadas v3)
        extra = [k for k in props if k not in CLAVES_DEF.get(t, set()) and k not in ("umbral", "plazo")]
        if extra and t != "TextoOrdenado":
            d["otras_propiedades_entidad"] += len(', "otras_propiedades": {}')
        # decisión 3: umbrales
        if t in M.TIPOS_CON_UMBRALES:
            vistos, elementos = set(), []
            fuentes = [desc] if desc else []
            for k in ("umbral", "plazo"):
                v = props.get(k)
                if isinstance(v, str) and v.strip():
                    d["sale_umbral_plazo_v3"] -= len(J({k: v})) - 2 + 2
                    if t == "Obligacion" and k == "plazo" and not any(
                            q.unidad in M.UNIDADES_TEMPORALES + M.UNIDADES_TEMPORALES_FUERA
                            for q in RC.detectar_cuantias(v)):
                        f = V.frecuencia_desde_tramo(v)
                        if f is not None:
                            plazos["frecuencia_en_lista"] += 1
                            d["frecuencia_A"] += len(J({"frecuencia": v})) - 2 + 2
                            d["frecuencia_B"] += len(J({"frecuencia": v})) - 2 + 2
                        else:
                            plazos["sin_cuantia_fuera_de_lista"] += 1
                            plazos_por_to[to] += 1
                            d["frecuencia_A"] += len(J({"frecuencia": v})) - 2 + 2
                        continue
                    fuentes.append(v)
            for fuente in fuentes:
                for q in RC.analizar(fuente, desc, c.get("titulo")):
                    clave = (q.valor, q.unidad, q.moneda)
                    if clave in vistos:
                        continue
                    vistos.add(clave)
                    ini = max(0, q.inicio - VENTANA_MARCADOR)
                    elementos.append(q.fin - ini)
            if (not elementos and t == "Restriccion" and props.get("tipo") == "limite_cuantitativo"):
                elementos.append(LIMITE_RELATIVO_CHARS)
                agg["limite_cuantitativo_sin_cuantia"] += 1
            if elementos:
                d["umbrales"] += len(', "umbrales": []') + sum(x + len('{"tramo": ""}, ') for x in elementos)
                agg["elementos_umbral"] += len(elementos)
                agg["entidades_con_umbrales"] += 1
    # decisión 4: mención
    for rel in ti.get("relations") or []:
        if not isinstance(rel, dict) or rel.get("predicate") not in ("aplica_a", "ejecuta"):
            continue
        agg["relaciones_sujeto"] += 1
        if isinstance(rel.get("sujeto_propuesto"), str):
            d["mencion"] += len('"sujeto_mencion"') - len('"sujeto_propuesto"')
            mencion_origen["sujeto_propuesto"] += 1
        else:
            largo, origen = mencion_estimada(rel.get("sujeto_id"), texto)
            mencion_origen[origen] += 1
            d["mencion"] += largo + len(', "sujeto_mencion": ""')
    # decisión 5: omisiones
    ons = ti.get("omisiones_no_prosa")
    d["omisiones_clave"] += len('"omisiones": []') - (len('"omisiones_no_prosa": []') if ons is not None else -2)
    for o in (ons or []):
        if isinstance(o, str) and o.strip():
            d["omisiones_v3_con_categoria_y_tramo"] += len('{"categoria": "tabla", "tramo": "", "nota": ""}') + TRAMO_OMISION_CHARS
            agg["omisiones_v3"] += 1
    val = r.get("validacion") or {}
    rech = val.get("rechazos") or []
    fuera_tipo = sum(1 for x in rech if x.get("motivo") == "type_invalido")
    sin_pred = 0
    for x in rech:
        if x.get("motivo") == "firma_invalida":
            el = x.get("elemento") or {}
            # recuperadas por la matriz r2 no cuentan como relación sin predicado
            det_ = str(x.get("detalle", ""))
            m = re.search(r"(\w+) --(\w+)--> (\w+)", det_)
            if m and M.firma_r2(m.group(1), m.group(2), m.group(3)):
                continue
            sin_pred += 1
    meta = 1 if RE_META.search(c.get("texto") or "") else 0
    agg["chunks_meta_proxy"] += meta
    agg["fuera_de_tipos_proxy"] += fuera_tipo
    agg["relacion_sin_predicado_proxy"] += sin_pred
    nuevas = meta + fuera_tipo + sin_pred
    d["omisiones_nuevas_proxy"] += nuevas * (len('{"categoria": "relacion_sin_predicado", "tramo": "", "nota": ""}, ')
                                             + TRAMO_OMISION_CHARS + NOTA_NUEVA_CHARS)
    if es_item_censo(c):
        agg["items"] += 1
        enc = segmento_encabezado(c["herencia"])
        enc_toks = set(V.norm_tokens(enc)) - {"de", "la", "el", "los", "las", "y", "o", "en", "a", "que", "del", "al"}
        comp = [e for e in ents if isinstance(e, dict) and e.get("type") in TIPOS_COMPUESTOS]
        if not comp and any(isinstance(e, dict) and e.get("type") not in ("TextoOrdenado", "Condicion") for e in ents):
            comp = [None]
        for e in comp:
            agg["entidades_compuestas"] += 1
            d["composicion_encabezado"] += len(enc) + len(SEPARADOR)
            desc_e = ((e or {}).get("properties") or {}).get("descripcion") if e else ""
            dt = set(V.norm_tokens(desc_e if isinstance(desc_e, str) else ""))
            if enc_toks and len(enc_toks & dt) / len(enc_toks) < 0.6:
                d["composicion_encabezado"] += len(enc)
                agg["descripciones_sin_encabezado"] += 1
            agg["chars_segmento_encabezado"] += len(enc)
    out_obs = r["usage"]["output_tokens"]
    det.append({"to": to, "chunk_id": cid, "out_obs": out_obs, "chars_obs": len(J(ti)),
                "reintento_corte": "reintento_corte" in r, "stop": r.get("stop_reason"),
                "delta": dict(d)})

# Escenarios de delta (caracteres): central y alto (con omisiones nuevas por proxy)
COMUNES = ("tramo_evidencia", "umbrales", "mencion", "omisiones_clave", "omisiones_v3_con_categoria_y_tramo",
           "sale_textoordenado_properties", "sale_comunicacion_tipo_numero", "sale_umbral_plazo_v3",
           "otras_propiedades_entidad", "composicion_encabezado")


def delta_chars(dd: dict, var: str, alto: bool, sin_evidencia: bool = False, ev_bajo: bool = False) -> int:
    s = sum(dd.get(k, 0) for k in COMUNES if not (sin_evidencia and k == "tramo_evidencia"))
    if ev_bajo and not sin_evidencia:
        s += dd.get("tramo_evidencia_bajo", 0) - dd.get("tramo_evidencia", 0)
    s += dd.get(f"frecuencia_{var}", 0)
    if alto:
        s += dd.get("omisiones_nuevas_proxy", 0)
    return s


a_out, b_out = cal_out[0], cal_out[1]
escenarios = {}
for nombre, var, alto, sinev, evb in (("A_central", "A", False, False, False), ("A_alto", "A", True, False, False),
                                      ("B_central", "B", False, False, False), ("B_alto", "B", True, False, False),
                                      ("A_bajo", "A", False, False, True),
                                      ("A_central_sin_evidencia", "A", False, True, False)):
    proy = []
    for x in det:
        dt = delta_chars(x["delta"], var, alto, sinev, evb) * b_out
        proy.append((x["chunk_id"], x["out_obs"], x["out_obs"] + dt, dt))
    out_obs_tot = sum(p[1] for p in proy)
    out_proj_tot = sum(p[2] for p in proy)
    cerca = lambda thr: sorted(((p[0], round(p[2])) for p in proy if p[2] >= thr), key=lambda z: -z[1])  # noqa: E731
    escenarios[nombre] = {
        "out_obs_total": out_obs_tot, "out_proyectado_total": round(out_proj_tot),
        "crecimiento_salida": round(out_proj_tot / out_obs_tot - 1, 4),
        "delta_tokens_por_unidad_media": round((out_proj_tot - out_obs_tot) / len(proy), 1),
        "unidades_>=6554(80%_de_8192)": len(cerca(0.8 * 8192)),
        "unidades_>=8192": cerca(8192),
        "unidades_>=13107(80%_de_16384)": cerca(0.8 * 16384),
        "unidades_>=16384": cerca(16384),
        "max_proyectado": max(round(p[2]) for p in proy),
    }

# desglose de deltas totales (caracteres) por campo
totales_campo = Counter()
for x in det:
    for k, v in x["delta"].items():
        totales_campo[k] += v

# ------------------------------------------------------------------------- #
# 4. Observado en la tanda 0: corte                                           #
# ------------------------------------------------------------------------- #
obs_max = sorted(((x["chunk_id"], x["out_obs"]) for x in det), key=lambda z: -z[1])[:12]
con_reintento = sorted(x["chunk_id"] for x in det if x["reintento_corte"])
# corte en el primer intento según el crudo de salida/ (antes de la dirigida)
cortes_salida = []
for to in TOS:
    for l in (REPO / f"data/experiment/reextraccion_v2/corpus_tanda0/salida/{to}/extracciones_e1.jsonl").open(encoding="utf-8"):
        rr = json.loads(l)
        err = rr.get("error") or ""
        # en la tanda 0 el reintento a 32.768 lo rechazó la SDK antes de enviarlo (BKL-0030):
        # el error registrado es el de la SDK, no max_tokens
        if "reintento_corte" in rr or err.startswith("max_tokens") or "Streaming is required" in err:
            cortes_salida.append((rr["chunk_id"], rr.get("error"), rr["usage"]["output_tokens"]))

# ------------------------------------------------------------------------- #
# 5. Costo                                                                   #
# ------------------------------------------------------------------------- #
n = len(det)
usage_tot = Counter()
for to, cid, r, c in unidades:
    for k, v in r["usage"].items():
        usage_tot[k] += v
costo_v3_crudo = (usage_tot["input_tokens"] * PREC["in"] + usage_tot["output_tokens"] * PREC["out"]
                  + usage_tot["cache_write_tokens"] * PREC["cw"] + usage_tot["cache_read_tokens"] * PREC["cr"]) / 1e6
n_escrituras = len(cw_unidades)

# E1 y E3 de la tanda 0, por fase cerrada (comando 1 de tabla_reprocesamiento.md §5)
fc = json.loads((REPO / "data/experiment/reextraccion_v2/corpus_tanda0/salida/estado_corpus.json").read_text())["fases_cerradas"]
g1 = sum(v["gasto_usd"] for k, v in fc.items() if k.endswith(":e1"))
n1 = sum(v["resumen"]["n"] for k, v in fc.items() if k.endswith(":e1"))
g3 = sum(v["gasto_usd"] for k, v in fc.items() if k.endswith(":e3"))
n3 = sum(v["resumen"]["n"] for k, v in fc.items() if k.endswith(":e3"))
# desglose de la fase E3: verificador y reintentos de E1 del ratchet
e3v = e1r = 0.0
e3_tok = Counter()
for to in TOS:
    rs = json.loads((REPO / f"data/experiment/reextraccion_v2/corpus_tanda0/salida/{to}/resumen_e3.json").read_text())
    e3v += rs["cliente_e3"]["gasto_usd_real"]
    e1r += rs["cliente_e1_reintentos"]["gasto_usd_real"]
    for k in ("tokens_in", "tokens_out", "cache_read", "cache_write"):
        e3_tok[k] += rs["cliente_e3"]["cache_stats"][k]
    e3_tok["llamadas"] += rs["cliente_e3"]["llamadas"]
    e3_tok["reintentos_e1"] += rs["cliente_e1_reintentos"]["llamadas"]

# ------------------------------------------------------------------------- #
# 6. Mensaje nuevo sobre la E0 e0-r2 (M1 de U-MED-R2A, f8dedd4) y NOTA de E3  #
# ------------------------------------------------------------------------- #
sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun_e1  # noqa: E402
import mensaje_r2_borrador as MB  # noqa: E402

E0R2 = REPO / "data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2"
chunks_r2 = {}
for to in TOS:
    d = json.loads((E0R2 / f"chunks_{to}.json").read_text(encoding="utf-8"))
    for c in (d if isinstance(d, list) else d.get("chunks", [])):
        chunks_r2[c["id"]] = c
assert set(chunks_r2) == {cid for _, cid, _, _ in unidades}, "ids de e0-r2 distintos de los del crudo"
# F1-A: el separador del tramo compuesto no aparece en el texto propio ni en el heredado de ninguna unidad,
# con ninguna de las dos E0 (si apareciera, partir el tramo por él sería ambiguo).
control_separador = {
    "separador": SEPARADOR.strip(),
    "e0_legada": sum(1 for _, _, _, c in unidades if c is not None and SEPARADOR.strip() in V.texto_completo(c)),
    "e0_r2": sum(1 for c in chunks_r2.values() if SEPARADOR.strip() in V.texto_completo(c)),
    "variante_tres_puntos_e0_r2": sum(1 for c in chunks_r2.values() if "[...]" in V.texto_completo(c)),
}
assert control_separador["e0_legada"] == 0 and control_separador["e0_r2"] == 0, "el separador aparece en el corpus"
delta_msg_chars = 0
delta_msg_por_id = {}
tab = Counter()
metas = Counter()
ev_impresas = ev_suprimidas = 0
nota_cambia, fuente_cambia, chunks_con_aviso = [], [], []
nota_delta_chars = 0
por_tabla = []
for to, cid, r, c in unidades:
    ch2 = chunks_r2[cid]
    m_lg = perfil.build_user_message(c)
    m_r2 = MB.build_user_message_r2(ch2, perfil.rol_por_to, comun_e1.puntos_admitidos, comun_e1.es_mini_chunk)
    delta_msg_chars += len(m_r2) - len(m_lg)
    delta_msg_por_id[cid] = len(m_r2) - len(m_lg)
    f = ch2.get("flags") or {}
    if (c.get("texto"), c.get("herencia")) != (ch2.get("texto"), ch2.get("herencia")):
        fuente_cambia.append(cid)
    if f.get("contenido_tabular"):
        tab["contenido_tabular"] += 1
    if f.get("formula"):
        tab["formula"] += 1
    if "tablas_e0" in f:
        tab["con_tablas_e0"] += 1
        ser = [x for x in f["tablas_e0"] if x.get("serializada")]
        tab["con_tabla_serializada"] += bool(ser)
        tab["residual_verdadero"] += bool(f.get("contenido_tabular_residual"))
        for x in f["tablas_e0"]:
            tab["tablas"] += 1
            tab["tablas_serializadas"] += bool(x.get("serializada"))
            if x.get("serializada"):
                metas["posicional"] += x["modo"] == "posicional"
                metas["con_celdas_propagadas"] += bool(x["celdas_propagadas"])
                metas["con_celdas_con_alcance"] += bool(x["celdas_con_alcance"])
                metas["con_combinadas_sin_propagar"] += bool(x["combinadas_sin_propagar"])
                metas["con_filas_subtitulo"] += bool(x["filas_subtitulo"])
                metas["con_aviso_de_riesgo"] += bool(x["combinadas_sin_propagar"] or x["filas_subtitulo"])
                por_tabla.append({"chunk_id": cid, "bloque": x["bloque"], "modo": x["modo"],
                                  "celdas_propagadas": x["celdas_propagadas"], "celdas_con_alcance": x["celdas_con_alcance"],
                                  "combinadas_sin_propagar": x["combinadas_sin_propagar"],
                                  "filas_subtitulo": x["filas_subtitulo"]})
    elif f.get("contenido_tabular"):
        tab["tabular_sin_clave_residual"] += 1
    if f.get("contenido_tabular"):
        vig = MB.evidencia_tabular_vigente(ch2)
        ev_impresas += len(vig)
        ev_suprimidas += len(f.get("evidencia_tabular") or []) - len(vig)
    if any(x.get("serializada") and MB.tiene_riesgo(x) for x in f.get("tablas_e0") or []):
        chunks_con_aviso.append(cid)
    n_lg, n_r2 = MB.nota_e3_sellada(c), MB.nota_e3_r2(ch2)
    if n_lg != n_r2:
        nota_cambia.append(cid)
        nota_delta_chars += len(n_r2 or "") - len(n_lg or "")
in_r2_total = usage_tot["input_tokens"] + cal_in[1] * delta_msg_chars
costo_e3_por_unidad_t0 = (e3v + e1r) / n3
mensaje_r2 = {
    "fuente": "e0_chunking/salida_tanda0_r2 (f8dedd4)",
    "delta_caracteres_total": delta_msg_chars,
    "delta_tokens_total": round(cal_in[1] * delta_msg_chars),
    "tokens_entrada_sellado_crudo": usage_tot["input_tokens"],
    "tokens_entrada_r2_estimados": round(in_r2_total),
    "tablas": dict(tab), "metadatos_tablas_serializadas": dict(metas), "por_tabla": por_tabla,
    "evidencia_tabular_impresa": ev_impresas, "evidencia_tabular_suprimida": ev_suprimidas,
    "chunks_con_fuente_e0_distinta": len(fuente_cambia),
}
nota_e3 = {
    "chunks_cuya_nota_cambia": nota_cambia, "n": len(nota_cambia),
    "chunks_con_aviso_de_riesgo": chunks_con_aviso, "n_con_aviso": len(chunks_con_aviso),
    "delta_caracteres_nota_total": nota_delta_chars,
    "costo_si_solo_cambiara_la_nota_usd": round(len(nota_cambia) * costo_e3_por_unidad_t0, 4),
    "costo_por_tokens_de_la_nota_usd": round(nota_delta_chars * cal_in[1] * PREC_E3["in"] / 1e6, 4),
    "base": "promedio de E3 por unidad de la tanda 0 (verificador + reintentos de E1 del ratchet) / 2.427",
}

costos = {}
for nombre, esc in escenarios.items():
    var = nombre[0]
    pref_tok = prefijos[var]["tokens_recta_3p"]
    cr = pref_tok * (n - n_escrituras)
    cw = pref_tok * n_escrituras
    inp = in_r2_total
    out = esc["out_proyectado_total"]
    e1 = (inp * PREC["in"] + out * PREC["out"] + cw * PREC["cw"] + cr * PREC["cr"]) / 1e6
    # E3: verificador con el mensaje que crece por lo que renderiza de los campos nuevos
    # (caracteres sin el sobrecosto JSON, aprox. 70 % del delta de salida) y reintentos de E1
    # del ratchet que crecen como la salida de E1.
    delta_render_chars = 0.7 * sum(max(0, delta_chars(x["delta"], var, nombre.endswith("alto"),
                                                      nombre.endswith("sin_evidencia"), nombre.endswith("bajo")))
                                   for x in det)
    e3_extra = delta_render_chars * cal_in[1] * PREC_E3["in"] / 1e6 * (e3_tok["llamadas"] / n)
    e3 = e3v + e3_extra + e1r * (1 + esc["crecimiento_salida"])
    costos[nombre] = {
        "e1_usd": round(e1, 4), "e3_usd": round(e3, 4), "total_usd": round(e1 + e3, 4),
        "por_unidad_usd": round((e1 + e3) / n, 6),
        "e1_por_unidad_usd": round(e1 / n, 6),
        "prefijo_tokens": pref_tok, "escrituras_de_cache": n_escrituras,
        "e3_extra_por_render_usd": round(e3_extra, 4),
    }

# Estimación del costo de la pareada de P4 (brazo nuevo, E1 solo; decisiones 18 y 19), por estrato:
# «con tabla serializada» sale de la E0 e0-r2 (f8dedd4); los demás, del crudo y de la E0 legada.
def costo_e1_r2(cid: str, delta_tok: float, pref_tok: int) -> float:
    to, r = crudo_por_id[cid]
    u = r["usage"]
    inp = u["input_tokens"] + cal_in[1] * delta_msg_por_id[cid]
    return (pref_tok * PREC["cr"] + inp * PREC["in"] + (u["output_tokens"] + delta_tok) * PREC["out"]) / 1e6


crudo_por_id = {cid: (to, r) for to, cid, r, c in unidades}
delta_por_id = {x["chunk_id"]: delta_chars(x["delta"], "A", False) * b_out for x in det}
chunk_por_id = {cid: c for to, cid, r, c in unidades}
estratos = {"con_tabla_serializada": [], "con_sujeto_propuesto": [], "con_cuantia": [],
            "con_omisiones_no_prosa": [], "sin_marca": []}
for cid, dlt in delta_por_id.items():
    c = chunk_por_id[cid]
    ti = crudo_por_id[cid][1].get("tool_input_crudo") or {}
    marcas = {
        "con_tabla_serializada": any(x.get("serializada") for x in (chunks_r2[cid].get("flags") or {}).get("tablas_e0") or []),
        "con_sujeto_propuesto": any(isinstance(x, dict) and x.get("sujeto_propuesto") for x in ti.get("relations") or []),
        "con_cuantia": bool(RC.detectar_cuantias(c.get("texto") or "")),
        "con_omisiones_no_prosa": bool(ti.get("omisiones_no_prosa")),
    }
    for k, v in marcas.items():
        if v:
            estratos[k].append(cid)
    if not any(marcas.values()):
        estratos["sin_marca"].append(cid)
pref_a = prefijos["A"]["tokens_recta_3p"]
p4 = {}
for k, ids in estratos.items():
    cs = sorted(costo_e1_r2(i, delta_por_id[i], pref_a) for i in ids)
    p4[k] = {"n": len(ids), "media_usd": round(st.mean(cs), 5), "p90_usd": round(cs[int(0.9 * len(cs))], 5),
             "max_usd": round(cs[-1], 4)}
# casos fijos de P4 (decisión 19 con los ids reales; decisión de la autora del 03/10/2026)
FIJOS_P4 = ("cap::1.2", "ric::9.2.1", "cla::5.1.1.1", "pro::1.1.2.5", "cap::6.2.2.6")
assert all(i in crudo_por_id for i in FIJOS_P4), "caso fijo sin crudo"
fijos = list(FIJOS_P4)
p4_fijos = round(sum(costo_e1_r2(i, delta_por_id[i], pref_a) for i in fijos), 4)
media_unidad_v3 = costo_v3_crudo / n
p4_total = {
    "sorteados_40_media": round(sum(8 * v["media_usd"] for v in p4.values()), 4),
    "sorteados_40_p90": round(sum(8 * v["p90_usd"] for v in p4.values()), 4),
    "fijos": p4_fijos, "fijos_ids": fijos,
    "fuera_de_muestra_8_nuevo": round(8 * costos["A_central"]["e1_por_unidad_usd"], 4),
    "fuera_de_muestra_8_sellado": round(8 * media_unidad_v3, 4),
    "escrituras_de_cache": round((pref_a + 15433) * PREC["cw"] / 1e6, 4),
}
# Casos de F1-A (decisión de la autora del 03/10/2026): las fichas 11, 13, 48, 52 y 64 de ESQ-2 y los tres
# incisos de la 64, en TOs del estrato fuera de muestra (ayccef, expaef, adrei): los dos brazos por la API,
# a la media por unidad (no hay crudo de esos chunks en la tanda 0). Se reportan aparte.
CASOS_F1 = ("ayccef::4.2.7.2", "expaef::6.6.2", "ayccef::3.4.1", "expaef::1.1.2.5", "adrei::4.3.1::intro",
            "adrei::4.3.1.1", "adrei::4.3.1.2", "adrei::4.3.1.3")
p4_total["casos_f1"] = list(CASOS_F1)
p4_total["casos_f1_nuevo"] = round(len(CASOS_F1) * costos["A_central"]["e1_por_unidad_usd"], 4)
p4_total["casos_f1_sellado"] = round(len(CASOS_F1) * media_unidad_v3, 4)
# Casos de control de la especie de BKL-0035 (decisión de la autora del 03/10/2026): encabezados de lista de la
# tanda 0 cuyo reintento de E3 creó el nodo de solo anuncio. Brazo sellado de la caché (USD 0); brazo nuevo por
# la API, desde el crudo, como los casos fijos.
CASOS_BKL0035 = ("ctacte::8.3::intro", "ctacte::8.4::intro", "ctacte::6.4.7::intro")
assert all(i in crudo_por_id for i in CASOS_BKL0035), "caso de BKL-0035 sin crudo"
p4_total["casos_bkl0035"] = list(CASOS_BKL0035)
p4_total["casos_bkl0035_nuevo"] = round(sum(costo_e1_r2(i, delta_por_id[i], pref_a) for i in CASOS_BKL0035), 4)
# Pata de E3 de P4 (decisión de la autora del 03/10/2026): E3 con la NOTA de los encabezados y la guarda ampliada
# sobre los tres casos de BKL-0035 y adrei::4.3.1::intro, con el prefijo de E3 sellado. Por llamada, la media de
# la tanda 0 (mensaje, salida, lectura del prefijo) más la NOTA; una escritura del prefijo de E3 por corrida.
# Central: solo la verificación (la guarda exime). Alto: además un reintento de E1 a la tarifa r2 y una
# re-verificación por unidad.
PATA_E3 = CASOS_BKL0035 + ("adrei::4.3.1::intro",)
pref_e3 = (e3_tok["cache_read"] + e3_tok["cache_write"]) / e3_tok["llamadas"]
nota_tok = cal_in[1] * len(MB.nota_e3_encabezado_r2({"tipo": "mini_chunk", "rol_bloque": "intro", "texto": ":"}))
llamada_e3 = ((e3_tok["tokens_in"] / e3_tok["llamadas"] + nota_tok) * PREC_E3["in"]
              + e3_tok["tokens_out"] / e3_tok["llamadas"] * PREC_E3["out"]) / 1e6
lectura_e3 = pref_e3 * PREC_E3["cr"] / 1e6
escritura_e3 = pref_e3 * PREC_E3["cw"] / 1e6
reintento_e1_r2 = e1r / e3_tok["reintentos_e1"] * costos["A_central"]["e1_por_unidad_usd"] / (costo_v3_crudo / n)
n_e3 = len(PATA_E3)
p4_total["pata_e3"] = list(PATA_E3)
p4_total["pata_e3_central"] = round(escritura_e3 + (n_e3 - 1) * lectura_e3 + n_e3 * llamada_e3, 4)
p4_total["pata_e3_alto"] = round(p4_total["pata_e3_central"] + n_e3 * (reintento_e1_r2 + lectura_e3 + llamada_e3), 4)
p4_total["pata_e3_base"] = {"prefijo_e3_tokens": round(pref_e3), "nota_tokens": round(nota_tok),
                            "llamada_usd": round(llamada_e3, 5), "lectura_usd": round(lectura_e3, 5),
                            "escritura_usd": round(escritura_e3, 5), "reintento_e1_r2_usd": round(reintento_e1_r2, 5)}
p4_total["central"] = round(p4_total["sorteados_40_media"] + p4_fijos + p4_total["fuera_de_muestra_8_nuevo"]
                            + p4_total["fuera_de_muestra_8_sellado"] + p4_total["escrituras_de_cache"]
                            + p4_total["casos_f1_nuevo"] + p4_total["casos_f1_sellado"]
                            + p4_total["casos_bkl0035_nuevo"] + p4_total["pata_e3_central"], 4)
p4_total["alto"] = round(p4_total["sorteados_40_p90"] + p4_fijos + p4_total["fuera_de_muestra_8_nuevo"]
                         + p4_total["fuera_de_muestra_8_sellado"] + p4_total["escrituras_de_cache"]
                         + p4_total["casos_f1_nuevo"] + p4_total["casos_f1_sellado"]
                         + p4_total["casos_bkl0035_nuevo"] + p4_total["pata_e3_alto"], 4)

TANDAS = {"U-REEXT-T0 (tanda 0)": 2434, "tanda 1 (ejemplo del §7)": 3292, "tanda 2: digeribles restantes": 5669,
          "tanda 2: no-RI plenos": 2008, "tanda 3: RI plenos": 976, "partición completa": 9324}
recalculo = {esc: {k: round(v * c["por_unidad_usd"], 2) for k, v in TANDAS.items()} for esc, c in costos.items()}
recalculo["tarifa_tanda0_0.0166"] = {k: round(v * 0.0166, 2) for k, v in TANDAS.items()}
res = {
    "estimacion_p4": {"por_estrato": p4, "total": p4_total},
    "recalculo_tandas_usd": recalculo,
    "unidades": n, "unidades_sin_chunk_en_e0": n_sin_chunk,
    "calibracion": {
        "salida": {"a": round(cal_out[0], 2), "tokens_por_caracter": round(cal_out[1], 5),
                   "error_rel_mediana": round(cal_out[2], 4), "error_rel_p90": round(cal_out[3], 4),
                   "ratio_global": round(ratio_out, 5), "n": len(xo)},
        "mensaje": {"a": round(cal_in[0], 2), "tokens_por_caracter": round(cal_in[1], 5),
                    "error_rel_mediana": round(cal_in[2], 4), "error_rel_p90": round(cal_in[3], 4), "n": len(xi)},
        "prefijo": {"recta_3p": [round(float(x), 6) for x in c3], "residuos_3p": residuos3,
                    "recta_2p": [round(float(x), 6) for x in c2], "residuos_2p": residuos2},
    },
    "prefijo_v3": prefijo_v3, "prefijo_r2_borrador": prefijos, "control_tool_schema_borrador": control_ts,
    "tool_schema_chars": {"hoy_generado": len(J(ts_hoy)), "borrador_d15_17": len(J(ts_r2)),
                          "v3_b54": len(J(v3.TOOL_SCHEMA_V3))},
    "evidencia_por_tipo": {t: {"niveles": dict(niveles_evid[t]), "n": len(chars_evid_tipo[t]),
                               "chars_media": round(st.mean(chars_evid_tipo[t]), 1),
                               "chars_mediana": st.median(chars_evid_tipo[t]),
                               "tokens_media": round(st.mean(chars_evid_tipo[t]) * cal_out[1], 1)}
                           for t in sorted(chars_evid_tipo)},
    "termino_definicion_niveles": dict(niveles_termino),
    "mencion_origen_estimacion": dict(mencion_origen),
    "plazos_obligacion_v3": dict(plazos), "plazos_sin_cuantia_por_to": dict(plazos_por_to),
    "agregados": dict(agg),
    "control_separador_f1a": control_separador,
    "delta_caracteres_por_campo_total": dict(totales_campo),
    "delta_tokens_por_campo_total": {k: round(v * cal_out[1]) for k, v in totales_campo.items()},
    "escenarios_salida": escenarios,
    "corte": {"max_observados": obs_max, "final_con_reintento_corte": con_reintento,
              "cortes_en_salida_previa_a_la_dirigida": cortes_salida},
    "costo_v3_recomputado_del_crudo_usd": round(costo_v3_crudo, 4),
    "tanda0_fases_cerradas": {"e1_usd": round(g1, 6), "n_e1": n1, "e3_usd": round(g3, 6), "n_e3": n3,
                              "e3_verificador_usd": round(e3v, 4), "e3_reintentos_e1_usd": round(e1r, 4),
                              "e3_tokens": dict(e3_tok)},
    "usage_crudo_total": dict(usage_tot),
    "mensaje_r2": mensaje_r2, "nota_e3": nota_e3,
    "costos": costos,
}
SALIDA.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
print(json.dumps({k: res[k] for k in ("unidades", "calibracion", "prefijo_r2_borrador", "tool_schema_chars",
                                      "costo_v3_recomputado_del_crudo_usd", "tanda0_fases_cerradas", "costos")},
                 ensure_ascii=False, indent=1))
