"""U-R2-CODIGO, R1.e — verificación en código de los valores de un nodo contra
las tablas de su chunk (L-ESQ-R2 §1.4: «en los chunks con tabla, contra
e0_tablas»), como marca y sin corregir. Módulo reutilizable: lo usa
r1e_verificar_umbrales.py y queda disponible para el llenado de la lista de
umbrales (R3.f). USD 0, sin LLM.

Regla vigente (versión 4):
  1. Tablas del chunk: las tablas marcadas (no recuadro) de `tablas_<to>.json`
     de la E0 e0-r2 cuyo chunk es el de alguna procedencia del nodo.
  2. Estructura de una tabla: sus filas (segmentos en orden, sin las filas de
     encabezado repetido de las continuaciones); primera fila de datos = la
     primera con una celda numérica o de código (mismo criterio que la
     serialización); encabezado de la columna c = las celdas no vacías de la
     columna c en las filas anteriores, unidas por un espacio, salvo las filas
     cuya primera celda abarca toda la fila (rótulos).
  3. Valores del nodo: los tokens numéricos de dos o más caracteres
     (`\\d[\\d.,]*\\d`) de `properties.umbral` y de `properties.descripcion`,
     después de quitar las fechas dd/mm/aa(aa). Los de las celdas de datos,
     igual.
  4. Columnas que nombra el nodo: las columnas cuyo término clave aparece en
     la descripción o en el label, salvo una mención precedida, a una o dos
     palabras, por «salvo», «excepto», «excepción», «excluidos», «excluidas» o
     «no». Término clave de un encabezado = su primera palabra de tres o más
     letras que no es una palabra vacía, sin tildes y en minúsculas; se busca
     su raíz (la palabra sin sus dos últimas letras si tiene seis o más) al
     comienzo de una palabra.
  5. Veredicto por valor:
     - `fuera_de_tabla`: el valor no está en ninguna celda de datos;
     - `verificado`: está en una celda de datos de una columna que el nodo
       nombra;
     - `valor_en_otra_columna` (la MARCA, el caso de la inversión de
       cap::1.2): se cumplen las cinco condiciones siguientes:
       (a) la tabla se serializó en modo columnas (encabezado sin celdas
           combinadas);
       (b) el valor está en una sola celda de datos de la tabla;
       (c) el nodo nombra exactamente una columna;
       (d) no es la del valor;
       (e) en la fila del valor, la celda de la columna nombrada es numérica y
           tiene la misma forma que la del valor (dígitos reemplazados por 9:
           «2.500» y «5.000» dan «9.999»).
       Es decir, el nodo habla de una columna y trae el valor de otra columna
       paralela de la misma fila (no la relación clave → valor de una tabla
       como la de «k» por calificación);
     - `en_tabla_sin_veredicto`: el valor está en la tabla y no se cumple ni
       `verificado` ni la marca.
     El nodo queda marcado si alguno de sus valores es `valor_en_otra_columna`.
Historia (correcciones hechas después de ver la salida sobre los mismos
grafos, KG-Tanda0-Desarrollo-r1 y KG-Tanda0-Diez-r1; las tres versiones se
calibraron con los datos que verifican):
  - versión 1: la columna del nodo era la nombrada primero, y se buscaba la
    palabra entera; marcó 67 de 278 nodos evaluados en desarrollo, con
    marcas falsas como «coeficiente marginal de la categoría 1» = 12 %
    (cap::7.1.2);
  - versión 2: todas las columnas nombradas, por raíz y con exclusión; marcó
    45, en su mayoría falsas: la raíz de «No calificado» coincide con
    «calificación», códigos en columnas sin encabezado, fragmentos de fechas
    («24» de «abril/24») y valores repetidos en varias celdas (20 %);
  - versión 3: la marca exigía (a) a (d) y una celda hermana numérica;
    además de cap::1.2, marcó fragmentos de fechas de «Período» (cap::12.2),
    un código de partida tomado como cantidad (ric::5.1.3.x) y, en r1, la
    tabla de «k» por calificación (cap::2.1), donde el nodo enumera la
    correspondencia;
  - versión 4, la vigente: sin fechas y con la condición de forma de (e).
Límites declarados: no se comprueba que la fila del valor sea la de la
entidad que el nodo nombra; una tabla en modo posicional nunca da marca.
"""

from __future__ import annotations

import re
import unicodedata

RE_NUMERICO = re.compile(r"^(?=.*\d)[\d.,%()\-–/\s]+$")   # = e0_tablas.RE_NUMERICO
RE_CODIGO = re.compile(r"^\d{3}")                        # = correr_e0.RE_CODIGO_DATO
RE_TOKEN_NUM = re.compile(r"\d[\d.,]*\d")
RE_FECHA = re.compile(r"\b\d{1,2}/\d{1,2}/\d{2,4}\b")
VACIAS = {"de", "del", "la", "las", "los", "el", "en", "por", "con", "para", "que",
          "sin", "una", "uno", "hasta", "desde", "entre", "sus", "su"}
EXCLUSION = {"salvo", "excepto", "excepcion", "excluidos", "excluidas", "no"}


def _norm(t: str) -> str:
    t = unicodedata.normalize("NFD", t or "")
    return "".join(c for c in t if unicodedata.category(c) != "Mn").lower()


def _tx(c) -> str:
    return (c or "").strip()


def _es_dato(c) -> bool:
    t = _tx(c)
    return bool(t) and bool(RE_NUMERICO.match(t) or RE_CODIGO.match(t))


def tokens_numericos(texto: str) -> list[str]:
    return [m.group(0) for m in RE_TOKEN_NUM.finditer(RE_FECHA.sub(" ", texto or ""))]


def forma(texto: str) -> str:
    return re.sub(r"\d", "9", " ".join(_tx(texto).split()))


def termino_clave(encabezado: str) -> str | None:
    for w in re.findall(r"[^\W\d_]+", _norm(encabezado)):
        if len(w) >= 3 and w not in VACIAS:
            return w
    return None


def _raiz(clave: str) -> str:
    return clave[:-2] if len(clave) >= 6 else clave


def estructura(tabla: dict) -> dict:
    filas = []
    for si, s in enumerate(tabla["segmentos"]):
        rep = set(s.get("filas_encabezado_repetido") or [])
        filas.extend(f for fi, f in enumerate(s["filas"]) if not (si > 0 and fi in rep))
    n = max(len(f) for f in filas)
    i_dato = next((i for i, f in enumerate(filas) if any(_es_dato(c) for c in f)), len(filas))
    enc = [""] * n
    for f in filas[:i_dato]:
        if _tx(f[0]) and all(c is None for c in f[1:]):
            continue
        for k, c in enumerate(f):
            if _tx(c):
                enc[k] = (enc[k] + " " + " ".join(_tx(c).split())).strip()
    celdas = []                                   # (fila, columna, tokens, texto)
    for i, f in enumerate(filas[i_dato:], start=i_dato):
        for k, c in enumerate(f):
            if _tx(c):
                celdas.append((i, k, tokens_numericos(_tx(c)), _tx(c)))
    return {"tabla": tabla["id"], "encabezados": enc, "celdas": celdas,
            "modo": (tabla.get("serializacion") or {}).get("modo")}


def columnas_del_nodo(nodo: dict, est: dict) -> set[int]:
    texto = _norm(nodo.get("properties", {}).get("descripcion", "") + " "
                  + nodo.get("label", ""))
    palabras = re.findall(r"[^\W_]+", texto)
    out = set()
    for k, e in enumerate(est["encabezados"]):
        clave = termino_clave(e)
        if not clave:
            continue
        raiz = _raiz(clave)
        for i, w in enumerate(palabras):
            if w.startswith(raiz) and not (EXCLUSION & set(palabras[max(0, i - 2):i])):
                out.add(k)
                break
    return out


def _nombre(est: dict, k: int) -> str:
    return est["encabezados"][k] or f"col{k + 1}"


def verificar_nodo(nodo: dict, tablas_del_chunk: list[dict]) -> dict:
    props = nodo.get("properties", {})
    valores = []
    for campo in ("umbral", "descripcion"):
        for v in tokens_numericos(str(props.get(campo, "") or "")):
            if v not in valores:
                valores.append(v)
    ests = [estructura(t) for t in tablas_del_chunk]
    resultados = []
    for v in valores:
        hallado = [(est, [(i, k, tx) for i, k, toks, tx in est["celdas"] if v in toks])
                   for est in ests]
        hallado = [(est, pos) for est, pos in hallado if pos]
        if not hallado:
            resultados.append({"valor": v, "veredicto": "fuera_de_tabla"})
            continue
        veredicto, detalle = "en_tabla_sin_veredicto", []
        for est, pos in hallado:
            nombradas = columnas_del_nodo(nodo, est)
            detalle.append({"tabla": est["tabla"], "modo": est["modo"],
                            "celdas_del_valor": [{"fila": i, "columna": _nombre(est, k)}
                                                 for i, k, _ in pos],
                            "columnas_del_nodo": [_nombre(est, k) for k in sorted(nombradas)]})
            if nombradas & {k for _, k, _ in pos}:
                veredicto = "verificado"
                break
            if est["modo"] == "columnas" and len(pos) == 1 and len(nombradas) == 1:
                i, kv, _ = pos[0]
                (kn,) = tuple(nombradas)
                hermana = next((tx for ii, kk, _, tx in est["celdas"]
                                if ii == i and kk == kn), None)
                propia = next(tx for ii, kk, _, tx in est["celdas"] if ii == i and kk == kv)
                if hermana is not None and RE_NUMERICO.match(hermana) \
                        and forma(hermana) == forma(propia):
                    veredicto = "valor_en_otra_columna"
                    detalle[-1]["valor_de_la_columna_del_nodo_en_esa_fila"] = hermana
        resultados.append({"valor": v, "veredicto": veredicto, "detalle": detalle})
    return {"nodo": nodo["id"], "valores": resultados,
            "marca": any(r["veredicto"] == "valor_en_otra_columna" for r in resultados)}
