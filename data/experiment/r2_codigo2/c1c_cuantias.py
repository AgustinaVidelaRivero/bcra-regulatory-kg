"""U-R2-CODIGO-2, C1.c — cuantías que `detectar_cuantias` no reconoce (USD 0, sin API ni Neo4j). Solo escribe --out.

`reglas_comparacion.detectar_cuantias` (pyd_r2/code/reglas_comparacion.py:185) no se edita: las extensiones
candidatas viven en este script y, para el contrafáctico, reemplazan la función en memoria durante la corrida.

Qué mide:
  1. Búsqueda: en el texto propio de los chunks de e0-r2 de los diez TOs, cada unidad de tiempo (día, mes, año,
     hora, «hs.», semana, minuto) que no cae dentro de una cuantía detectada y tiene una cifra, un número en letras o
     un ordinal en las cuatro palabras previas; agrupadas por forma.
  2. Extensiones candidatas, cada una medible por separado:
       h  «hs.», «hs», «hrs.»: unidad horas (fuera de lista, como «horas»);
       o  ordinal + unidad temporal («el quinto día hábil», «al tercer mes», «trigésimo sexto mes», «5° día»):
          valor = número del ordinal; «hábil»/«corrido» en singular o plural fijan `dias_tipo`;
       s  «hábil»/«corrido» en singular después de una cuantía de días ya detectada («1 día hábil»): `dias_tipo`;
       m  «N (letras) o más|menos <unidad>»: la cuantía con «o más»/«o menos» entre el paréntesis y la unidad.
  3. Censo sobre el texto de los diez TOs: cuántas cuantías nuevas detecta cada extensión.
  4. Contrafáctico sobre KG-Tanda0-Diez-r2a y KG-Tanda0-Desarrollo-r2a (cadena r2 en memoria, `c1_comun`), con las
     extensiones h, o y s (las del mandato y la que comparte su regla): elementos de umbral que cambian, por nodo, y
     plazos heredados que dejan de ir a `frecuencia`.

Uso, desde la raíz de una copia del repo:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/r2_codigo2/c1c_cuantias.py \
      --out data/experiment/r2_codigo2/salidas/c1c_cuantias.json
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter, OrderedDict

import c1_comun as K

K.ENS.E4.modulo_modelos_r2()            # pone pyd_r2/code en el path
import reglas_comparacion as RCMP       # noqa: E402

E0R2 = K.RAIZ / K.E0_R2
DETECTAR_ORIGINAL = RCMP.detectar_cuantias
EXTENSIONES_CONTRAFACTICO = "hos"

_P = RCMP._PAREN
_NUM = r"(\d+|" + RCMP._ALT_LV + r")"
RE_HS = re.compile(r"(?<![\w.,])" + _NUM + _P + r"\s*(hs|hrs?)\b\.?")
ORDINALES = {"primer": 1, "primero": 1, "primera": 1, "segundo": 2, "segunda": 2, "tercer": 3, "tercero": 3,
             "tercera": 3, "cuarto": 4, "cuarta": 4, "quinto": 5, "quinta": 5, "sexto": 6, "sexta": 6,
             "septimo": 7, "septima": 7, "octavo": 8, "octava": 8, "noveno": 9, "novena": 9, "decimo": 10,
             "decima": 10, "undecimo": 11, "undecima": 11, "duodecimo": 12, "duodecima": 12, "vigesimo": 20,
             "vigesima": 20, "trigesimo": 30, "trigesima": 30}
_DECENAS = ("decimo", "decima", "vigesimo", "vigesima", "trigesimo", "trigesima")
_UNIDADES_ORD = "|".join(sorted((k for k, v in ORDINALES.items() if v < 10), key=len, reverse=True))
_ALT_ORD = "|".join(sorted(ORDINALES, key=len, reverse=True))
RE_ORDINAL = re.compile(
    r"(?<![\w.,])(?P<ord>(?:" + "|".join(_DECENAS) + r")\s+(?:" + _UNIDADES_ORD + r")|" + _ALT_ORD
    + r"|\d+\s*[°º]|\d+[°ºo](?=\s))\s+(?P<u>dias?|mes(?:es)?|anos?|semanas?)\b(?:\s+(?P<cal>habil(?:es)?|corridos?))?")
RE_DIA_SINGULAR = re.compile(r"\s+(habil|corrido)\b")
RE_O_MAS = re.compile(r"(?<![\w.,])(\d+)" + _P + r"\s+o\s+(mas|menos)\s+(dias?|mes(?:es)?|anos?)\b"
                      r"(?:\s+(habiles|corridos))?")
UNIDAD = {"dia": "dias", "mes": "meses", "ano": "anios", "sem": "semanas", "hor": "horas"}


def _unidad(u: str) -> str:
    return UNIDAD[u[:3]]


def _valor_ordinal(o: str) -> int:
    o = " ".join(o.split())
    if re.match(r"\d", o):
        return int(re.match(r"\d+", o).group(0))
    partes = o.split()
    return sum(ORDINALES[p] for p in partes)


def _dias_tipo(cal: str | None) -> str | None:
    if not cal:
        return None
    return "habiles" if cal.startswith("habil") else "corridos"


def detectar_candidata(texto: str, ext: str = "hosm") -> list:
    """`detectar_cuantias` con las extensiones de `ext`; las cuantías nuevas no solapan las detectadas."""
    base = DETECTAR_ORIGINAL(texto)
    pleg = RCMP.plegar(texto)
    nuevas = []
    if "s" in ext:
        for c in base:
            if c.clase == "plazo" and c.unidad == "dias" and c.dias_tipo is None:
                m = RE_DIA_SINGULAR.match(pleg, c.fin)
                if m:
                    c.dias_tipo = _dias_tipo(m.group(1))
                    c.fin, c.texto = m.end(), texto[c.inicio:m.end()]
    if "h" in ext:
        for m in RE_HS.finditer(pleg):
            if RCMP._compuesto(pleg, m.start(1), m.group(1)):
                continue
            v = RCMP.parse_num(m.group(1))
            nuevas.append(RCMP.Cuantia(inicio=m.start(), fin=m.end(), texto=texto[m.start():m.end()], clase="plazo",
                                       valor=RCMP.dec_str(v) if v is not None else None, unidad="horas",
                                       fuera_de_lista=["unidad"]))
    if "o" in ext:
        for m in RE_ORDINAL.finditer(pleg):
            u = _unidad(m.group("u"))
            nuevas.append(RCMP.Cuantia(inicio=m.start(), fin=m.end(), texto=texto[m.start():m.end()], clase="plazo",
                                       valor=str(_valor_ordinal(m.group("ord"))), unidad=u,
                                       dias_tipo=_dias_tipo(m.group("cal")) if u == "dias" else None,
                                       fuera_de_lista=[] if u in ("dias", "meses", "anios") else ["unidad"]))
    if "m" in ext:
        for m in RE_O_MAS.finditer(pleg):
            u = _unidad(m.group(3))
            nuevas.append(RCMP.Cuantia(inicio=m.start(), fin=m.end(), texto=texto[m.start():m.end()], clase="plazo",
                                       valor=str(int(m.group(1))), unidad=u,
                                       dias_tipo=_dias_tipo(m.group(4)) if u == "dias" else None))
    todas = sorted(base + nuevas, key=lambda c: (c.inicio, -(c.fin - c.inicio)))
    out = []
    for c in todas:
        if out and c.inicio < out[-1].fin:
            continue
        out.append(c)
    return out


def _chunks_e0r2() -> list[tuple[str, dict]]:
    out = []
    for p in sorted(E0R2.glob("chunks_*.json")):
        to = p.stem.split("_", 1)[1]
        out += [(to, c) for c in json.loads(p.read_text(encoding="utf-8"))]
    return out


RE_UNIDAD_TIEMPO = re.compile(r"\b(dias?|mes(?:es)?|anos?|horas?|hs\b\.?|hrs?\b\.?|semanas?|minutos?)\b")
RE_PREVIO = re.compile(r"\d|^(?:" + _ALT_ORD + r"|" + RCMP._ALT_LV + r"|ciento|cientos|ultim[oa]s?)$")


def busqueda(chunks) -> dict:
    """Unidades de tiempo fuera de toda cuantía detectada, con cifra, número en letras u ordinal en las cuatro
    palabras previas, agrupadas por forma (las dos palabras previas y la unidad, con las cifras como N)."""
    formas, ejemplos = Counter(), {}
    for to, c in chunks:
        t = c["texto"] or ""
        p = RCMP.plegar(t)
        cub = [(x.inicio, x.fin) for x in DETECTAR_ORIGINAL(t)]
        for m in RE_UNIDAD_TIEMPO.finditer(p):
            if any(a <= m.start() < b for a, b in cub):
                continue
            toks = [x.strip("(),.;:–-*") for x in p[max(0, m.start() - 45):m.start()].split()[-4:]]
            if not any(RE_PREVIO.search(x) for x in toks if x):
                continue
            k = re.sub(r"\d+", "N", " ".join(toks[-2:] + [m.group(0)])).strip()
            formas[k] += 1
            ejemplos.setdefault(k, {"chunk_id": c["id"], "texto": " ".join(t[max(0, m.start() - 60):m.end() + 30].split())})
    return OrderedDict([("formas", len(formas)), ("apariciones", sum(formas.values())),
                        ("por_forma", [{"forma": k, "apariciones": v, "ejemplo": ejemplos[k]}
                                       for k, v in sorted(formas.items(), key=lambda kv: (-kv[1], kv[0]))])])


def censo_texto(chunks) -> dict:
    """Cuantías nuevas por extensión, sobre el texto propio de los chunks de e0-r2 de los diez TOs."""
    por_ext, filas, dias_tipo = Counter(), [], 0
    base_total = 0
    for to, c in chunks:
        t = c["texto"] or ""
        base = DETECTAR_ORIGINAL(t)
        base_total += len(base)
        claves = {(x.inicio, x.fin) for x in base}
        for e in "hom":
            for x in detectar_candidata(t, e):
                if (x.inicio, x.fin) not in claves and not any(a <= x.inicio < b for a, b in claves):
                    por_ext[e] += 1
                    filas.append({"extension": e, "to": to, "chunk_id": c["id"], "tramo": " ".join(x.texto.split()),
                                  "valor": x.valor, "unidad": x.unidad, "dias_tipo": x.dias_tipo})
        cand_s = {(x.inicio, x.valor, x.unidad): x for x in detectar_candidata(t, "s")}
        for x in DETECTAR_ORIGINAL(t):
            y = cand_s.get((x.inicio, x.valor, x.unidad))
            if y is not None and y.dias_tipo != x.dias_tipo:
                dias_tipo += 1
                filas.append({"extension": "s", "to": to, "chunk_id": c["id"], "tramo": " ".join(y.texto.split()),
                              "valor": y.valor, "unidad": y.unidad, "dias_tipo": y.dias_tipo})
    return OrderedDict([("chunks", len(chunks)), ("cuantias_detectadas_hoy", base_total),
                        ("nuevas_por_extension", {**{e: por_ext[e] for e in "hom"}, "s_dias_tipo_fijado": dias_tipo}),
                        ("filas", filas)])


def _umbrales(kg: dict) -> dict:
    return {n["id"]: n for n in kg["nodes"] if n["type"] in ("Restriccion", "Obligacion", "Condicion", "Excepcion")}


def contrafactico(nombre: str) -> dict:
    base = K.correr_r2(nombre)
    control = K.control_sha(nombre, base)

    def det(texto):
        return detectar_candidata(texto, EXTENSIONES_CONTRAFACTICO)
    contra = K.correr_r2(nombre, [(RCMP, "detectar_cuantias", det)])
    nb, nc = _umbrales(base["kg"]), _umbrales(contra["kg"])
    cambian, sale_de_frecuencia, elementos = [], [], Counter()
    for i in sorted(nb):
        a, b = nb[i], nc[i]
        ua, ub = a["properties"].get("umbrales") or [], b["properties"].get("umbrales") or []
        fa, fb = a["properties"].get("frecuencia"), b["properties"].get("frecuencia")
        if ua == ub and fa == fb and a.get("fuera_de_lista") == b.get("fuera_de_lista"):
            continue
        sa = [json.dumps(x, sort_keys=True, ensure_ascii=False) for x in ua]
        sb = [json.dumps(x, sort_keys=True, ensure_ascii=False) for x in ub]
        solo_a = [json.loads(x) for x in sa if x not in sb]
        solo_b = [json.loads(x) for x in sb if x not in sa]

        def ident(x):
            return (x.get("valor"), x.get("unidad"), x.get("origen"))
        modificados = []
        for x in list(solo_b):
            y = next((z for z in solo_a if ident(z) == ident(x)), None)
            if y is not None:
                solo_a.remove(y)
                solo_b.remove(x)
                modificados.append({"antes": {k: y.get(k) for k in sorted(set(x) | set(y)) if y.get(k) != x.get(k)},
                                    "despues": {k: x.get(k) for k in sorted(set(x) | set(y)) if y.get(k) != x.get(k)},
                                    "valor": x.get("valor"), "unidad": x.get("unidad")})
        campos = ("tramo", "valor", "unidad", "dias_tipo", "comparacion", "regla_comparacion", "comparacion_asumida",
                  "origen")
        elementos["agregados"] += len(solo_b)
        elementos["quitados"] += len(solo_a)
        elementos["modificados"] += len(modificados)
        elementos["agregados_con_comparacion_asumida"] += sum(1 for x in solo_b if x.get("comparacion_asumida"))
        fila = OrderedDict([("nodo", i), ("chunk_id", a["provenance"].get("chunk_id")),
                            ("frecuencia_r2a", fa), ("frecuencia_con_la_regla", fb),
                            ("plazo_heredado", (a.get("campos_heredados_v3") or {}).get("plazo")),
                            ("elementos_agregados", [{k: x.get(k) for k in campos} for x in solo_b]),
                            ("elementos_quitados", [{k: x.get(k) for k in campos} for x in solo_a]),
                            ("elementos_modificados", modificados)])
        cambian.append(fila)
        if fa is not None and fb is None:
            sale_de_frecuencia.append(fila)
    ra, rc = base["resumen"]["umbrales"], contra["resumen"]["umbrales"]
    return OrderedDict([
        ("control_sha_sin_cambio", control), ("sha256_kg_con_la_regla", contra["sha256"]),
        ("nodos_con_umbrales_que_cambian", len(cambian)),
        ("elementos", dict(elementos)),
        ("plazos_que_dejan_de_ir_a_frecuencia", len(sale_de_frecuencia)),
        ("resumen_umbrales_r2a", {k: ra[k] for k in ("elementos", "nodos_con_lista", "frecuencia_desde_plazo",
                                                     "frecuencia_fuera_de_lista")}),
        ("resumen_umbrales_con_la_regla", {k: rc[k] for k in ("elementos", "nodos_con_lista", "frecuencia_desde_plazo",
                                                              "frecuencia_fuera_de_lista")}),
        ("aristas_iguales", not K.diferencia_aristas(base["kg"], contra["kg"])["quitadas"]
         and not K.diferencia_aristas(base["kg"], contra["kg"])["agregadas"]),
        ("detalle", cambian)])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    chunks = _chunks_e0r2()
    casos = {"24 hs. hábiles": "Informar, dentro de las 24 hs. hábiles siguientes a la recepción",
             "quinto día hábil": "deberá efectuarse hasta el quinto día hábil posterior al vencimiento de cada período"}
    out = OrderedDict([
        ("casos_del_mandato", {k: {"hoy": [c.texto for c in DETECTAR_ORIGINAL(v)],
                                   "con_la_regla": [(c.texto, c.valor, c.unidad, c.dias_tipo)
                                                    for c in detectar_candidata(v, EXTENSIONES_CONTRAFACTICO)]}
                               for k, v in casos.items()}),
        ("busqueda_texto_diez_tos", busqueda(chunks)),
        ("censo_texto_diez_tos", censo_texto(chunks)),
        ("extensiones_del_contrafactico", EXTENSIONES_CONTRAFACTICO)])
    for nombre in K.GRAFOS:
        out[f"contrafactico_{nombre}"] = contrafactico(nombre)
    K.escribir_json(K.RAIZ / a.out, out)
    print(json.dumps(out["casos_del_mandato"], ensure_ascii=False))
    print(json.dumps({k: out["censo_texto_diez_tos"][k] for k in ("cuantias_detectadas_hoy", "nuevas_por_extension")}))
    for nombre in K.GRAFOS:
        r = out[f"contrafactico_{nombre}"]
        print(nombre, r["control_sha_sin_cambio"]["reproduce"], r["nodos_con_umbrales_que_cambian"], r["elementos"],
              r["plazos_que_dejan_de_ir_a_frecuencia"], r["aristas_iguales"])


if __name__ == "__main__":
    main()
