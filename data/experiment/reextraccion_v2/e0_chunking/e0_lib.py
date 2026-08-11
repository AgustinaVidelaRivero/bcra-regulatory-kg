"""E0 — Chunking estructural determinístico (issue #9, diseño docs/diseno_reextraccion_v2.md §3-E0).

Deriva la estructura normativa de cada TO desde el CUERPO del PDF (nunca del
índice): puntos numerados jerárquicos x.y.z…, secciones, y prosa sin numerar
(chapeaus de sección, intros y cierres de punto) ANCLADA a su contenedor por
indentación. El índice se parsea por separado y solo se usa como contraste
(reporte de divergencias); no gobierna ningún corte.

Señal estructural central: la columna x0 de cada línea. En los TOs del BCRA la
escalera de indentación es estable (≈35pt por nivel): el label de un punto de
profundidad d arranca en la columna c_d, y su texto corre en c_{d+1}. Un
párrafo sin numerar cuya x0 coincide con la columna de texto de un ANCESTRO
del punto abierto es un cierre/intersticial de ese ancestro, no una
continuación del punto profundo (caso documentado: cierres del 2.7 de Exterior
y Cambios en x0≈104.9 = columna de texto del nivel 2, mientras la continuación
de 2.7.x corre en ≈140.3).

Validación de headers de punto (mata los falsos headers RX-03 de
docs/backlog_reextraccion.md): un candidato "N.N.…" solo abre punto si
(a) su primer componente es el número de la sección corriente,
(b) su padre está abierto y el último componente supera al último hermano
    visto (los saltos se aceptan y se REPORTAN, los duplicados se rechazan),
(c) su x0 es compatible con la escalera de columnas del TO (±TOL_X pt).
Todo candidato rechazado queda registrado con su motivo (nada se descarta en
silencio).

Correcciones post-parseo (dos reglas de principio, aplicadas sobre el árbol ya
construido, en este orden):

REGLA 1 — continuidad de enumeración en costuras: un segmento clasificado
intersticial de un padre, cuyo primer marcador de enumeración (romanos,
letras, números — 'vii)', 'h)', '3)') continúa la secuencia con la que termina
el texto propio del hermano terminal inmediatamente anterior, se reasigna como
continuación del texto propio de ese hermano; las líneas envueltas del ítem
(sin marcador, en columna más profunda que la del marcador) lo siguen. Caso
medido: los acápites vii)–x) de pro 2.3.1.1, que la deriva de columnas de la
p.9 hacía re-anclar como intersticiales de 2.3.1. Ver
`aplicar_continuidad_enumeracion` (detector de secuencias y límites en su
docstring).

REGLA 2 — cero cortes intra-palabra: ninguna frontera de segmento puede caer
en una palabra partida por guion de fin de línea ('presta-' / 'ciones…'): la
frontera se corre línea por línea hasta cerrar la palabra. Solo se corrige
DÓNDE cae la frontera; el des-silabeo del texto sigue siendo decisión de E1.
Ver `corregir_fronteras_intra_palabra` (detector y exclusiones en su
docstring).

MINI-CHUNKS (enmienda 01, docs/enmienda_01_diseno_reextraccion_v2.md §2.a):
los bloques estructurales de los nodos NO terminales (chapeau de sección,
intro, intersticial, cierre) se emiten además como unidades de extracción de
primera clase. Criterio de materialización (letra de §2.a): un bloque se
materializa si y solo si contiene texto además de su línea de título — los
tramos `encabezado` son la línea de label y tras descontarla no queda nada
(jamás materializan); los segmentos de prosa no contienen la línea de label y
materializan siempre que su texto normalizado no sea vacío. La heurística de
escala de la enmienda (una línea ≤140 chars ≈ título) queda descartada como
criterio: excluiría intros normativos de una línea (caso pro 2.7,
'deberán contar con sendos hipervínculos…'). Invariante resultante: todo
bloque de prosa de un ancestro con texto no vacío tiene exactamente un
responsable de extracción (su mini-chunk).

Agrupado: los segmentos intro (y el chapeau de sección) de una unidad son
contiguos por construcción (todos antes del primer hijo), ídem los cierre
(después del último); cada grupo se funde en UN mini-chunk — evita fragmentar
fórmulas y colas envueltas que el parser separó por cambio de columna. Los
intersticiales viven en huecos distintos entre hijos: uno por segmento, con
sufijo ::<n> (orden documental) cuando hay más de uno del mismo rol.
Id determinístico: <to>::<unidad_origen>::<rol>[::<n>] — función de la unidad
de origen y el rol documental, nunca del orden de emisión. Emisión
interleaved en orden documental: intro antes de los hijos, intersticial en su
hueco, cierre después. Ver `construir_chunks`.

Sin llamadas a LLM: código determinístico puro.
"""

from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

import pdfplumber

# ---------------------------------------------------------------- constantes

TO_KEYS = {
    "TO_capitales_minimos_actual.pdf": "cap",
    "TO_clasificacion_deudores_actual.pdf": "cla",
    "TO_exterior_cambios_actual.pdf": "ext",
    "TO_proteccion_usuarios_servicios_financieros_actual.pdf": "pro",
    "TO_regimen_informativo_contable_mensual_actual.pdf": "ric",
}

TOL_X = 3.0          # tolerancia de coincidencia de columnas (pt)
TOL_TOP = 2.0        # tolerancia de agrupamiento vertical de palabras en línea (pt)
GAP_COL = 15.0       # hueco horizontal mínimo (pt) para contar frontera de columna (tablas)

RE_MARCA_INDICE = re.compile(r"^-\s*[ÍI]ndice\s*[-–]?\s*$", re.IGNORECASE)
MARCA_TABLA_ORIGEN = "NORMA DE ORIGEN"
MARCA_HISTORIAL = "historial de la norma"
RE_SECCION = re.compile(r"^Secci[oó]n\s+(\d+)\s*\.\s*(.*)$")
RE_SECCION_EN_LINEA = re.compile(r"Secci[oó]n\s+(\d+)\s*\.\s*(.*)$")
GAP_TOP_TITULO = 16.0   # separación vertical máxima (pt) de la cola envuelta de un título de sección
RE_NUM_TOKEN = re.compile(r"^(\d+(?:\.\d+)*)\.$")   # primer token de un header de punto
# el BCRA a veces omite el punto final del label ('13.4.1 el pago…',
# '8.5.14.1 la norma…' — medidos en ext p.172 y p.117): se admite numeración
# sin punto final solo con profundidad ≥2 (un entero solo nunca es label)
RE_NUM_TOKEN_SIN_PUNTO = re.compile(r"^(\d+(?:\.\d+)+)$")
RE_PIE = [
    re.compile(r"^Vigencia:?$"),
    re.compile(r"^Versi[oó]n:.*P[aá]gina\s+\d+"),
    re.compile(r"^\d{1,2}/\d{1,2}/\d{2,4}$"),
    re.compile(r"^P[aá]gina\s+\d+$"),
]
RE_NUMERICO = re.compile(r"^-?[\d.,]+%?$")

MAX_RAIZ = 30        # un primer componente mayor es cita de Comunicación, no punto


# ------------------------------------------------------------------- líneas

@dataclass
class Linea:
    pagina: int          # 1-based
    top: float
    x0: float
    texto: str
    ngaps: int           # fronteras de columna (huecos > GAP_COL) dentro de la línea
    ultimo_numerico: bool
    primer_codigo: bool  # primer token arranca con ≥3 dígitos (fila código-partida)


def extraer_lineas(pdf_path: Path) -> list[list[Linea]]:
    """Extrae las líneas de cada página agrupando palabras por 'top' (±TOL_TOP).

    El texto de una línea es el join por espacio simple de sus palabras en
    orden x0. Este texto ES el corpus de E0: la verificación de cobertura se
    define sobre él.
    """
    paginas: list[list[Linea]] = []
    with pdfplumber.open(str(pdf_path)) as pdf:
        for pi, page in enumerate(pdf.pages, start=1):
            words = page.extract_words()
            grupos: list[tuple[float, list[dict]]] = []
            for w in words:
                for i, (t, ws) in enumerate(grupos):
                    if abs(t - w["top"]) <= TOL_TOP:
                        ws.append(w)
                        break
                else:
                    grupos.append((w["top"], [w]))
            lineas: list[Linea] = []
            for t, ws in sorted(grupos, key=lambda g: g[0]):
                ws = sorted(ws, key=lambda w: w["x0"])
                ngaps = sum(1 for a, b in zip(ws, ws[1:]) if b["x0"] - a["x1"] > GAP_COL)
                texto = " ".join(w["text"] for w in ws)
                lineas.append(Linea(
                    pagina=pi, top=round(t, 1), x0=round(ws[0]["x0"], 1),
                    texto=texto, ngaps=ngaps,
                    ultimo_numerico=bool(RE_NUMERICO.match(ws[-1]["text"])),
                    primer_codigo=bool(re.match(r"^\d{3}", ws[0]["text"])),
                ))
            paginas.append(lineas)
    return paginas


# ------------------------------------------------------------ roles de página

ROL_PORTADA = "portada"
ROL_INDICE = "indice"
ROL_TABLA = "tabla_norma_origen"
ROL_HISTORIAL = "historial"
ROL_CUERPO = "cuerpo"


def clasificar_paginas(paginas: list[list[Linea]]) -> list[str]:
    """portada = antes de la primera página de índice; índice = marcador
    '-Índice-' (variantes con espacio/guion largo) o continuación (página que
    sigue a una de índice con ≥2 líneas 'Sección N.'); tabla_norma_origen =
    contiene 'NORMA DE ORIGEN'; historial = desde la página cuyo primer
    contenido anuncia el historial de Comunicaciones de la norma (pegajoso
    hasta el próximo marcador explícito de otro rol); cuerpo = resto."""
    roles: list[str] = []
    visto_indice = False
    en_historial = False
    for lineas in paginas:
        textos = [l.texto.strip() for l in lineas]
        n_secc = sum(1 for t in textos if RE_SECCION.match(t))
        if any(MARCA_TABLA_ORIGEN in t.upper() for t in textos):
            rol = ROL_TABLA
            en_historial = False
        elif any(RE_MARCA_INDICE.match(t) for t in textos):
            rol = ROL_INDICE
            visto_indice = True
            en_historial = False
        elif any(MARCA_HISTORIAL in t.lower() for t in textos[:3]):
            rol = ROL_HISTORIAL
            en_historial = True
        elif en_historial:
            rol = ROL_HISTORIAL
        elif roles and roles[-1] == ROL_INDICE and n_secc >= 2:
            rol = ROL_INDICE  # continuación de índice sin marcador (caso ric p.2)
        elif not visto_indice:
            rol = ROL_PORTADA
        else:
            rol = ROL_CUERPO
        roles.append(rol)
    return roles


# ------------------------------------------------- encabezados y pies (cuerpo)

def _es_titulo_mayusculas(texto: str) -> bool:
    """Línea de encabezado corrido: sin minúsculas (títulos de TO, 'B.C.R.A.',
    la línea de aparato del ric '4. EXIGENCIA…')."""
    letras = [c for c in texto if c.isalpha()]
    return bool(letras) and not any(c.islower() for c in letras)


def separar_encabezado_pie(lineas: list[Linea], capturar_seccion: bool = True,
                           ) -> tuple[list[Linea], list[Linea], str | None]:
    """Devuelve (contenido, descartadas, seccion_corrida).

    Encabezado: dentro de las primeras 5 líneas, las que son título en
    mayúsculas, contienen 'B.C.R.A.' o —solo si capturar_seccion— son la línea
    corrida 'Sección N. …' (que se captura como metadata de página; en páginas
    de índice una línea 'Sección N.' es una ENTRADA, no encabezado). Pie:
    desde el final, las que matchean los patrones de RE_PIE."""
    descartadas: list[Linea] = []
    contenido = list(lineas)
    seccion_corrida: str | None = None

    # pie (desde el final)
    while contenido and any(p.match(contenido[-1].texto.strip()) for p in RE_PIE):
        descartadas.append(contenido.pop())

    # encabezado (desde el principio, zona de 5 líneas)
    quitadas = 0
    ultima_top_seccion: float | None = None
    while contenido and quitadas < 5:
        t = contenido[0].texto.strip()
        m = RE_SECCION.match(t)
        m_en_linea = RE_SECCION_EN_LINEA.search(t) if "B.C.R.A." in t else None
        if m and capturar_seccion and seccion_corrida is None:
            # la línea 'Sección N. …' puede contener 'B.C.R.A.' en su TÍTULO
            # (ric Sección 7), por eso se chequea antes que el descarte genérico
            seccion_corrida = t
            ultima_top_seccion = contenido[0].top
            descartadas.append(contenido.pop(0))
            quitadas += 1
        elif m_en_linea and capturar_seccion and seccion_corrida is None:
            # títulos largos: el PDF fusiona 'B.C.R.A. Sección N. …' en una línea
            seccion_corrida = t[m_en_linea.start():]
            ultima_top_seccion = contenido[0].top
            descartadas.append(contenido.pop(0))
            quitadas += 1
        elif "B.C.R.A." in t or _es_titulo_mayusculas(t):
            descartadas.append(contenido.pop(0))
            quitadas += 1
        elif seccion_corrida is not None and ultima_top_seccion is not None \
                and contenido[0].top - ultima_top_seccion <= GAP_TOP_TITULO \
                and not RE_NUM_TOKEN.match(t.split()[0] if t.split() else ""):
            # cola envuelta del título de sección ('dos.', '(SECOEXPO).'):
            # renglón inmediato (interlineado de encabezado, no de contenido).
            # Una línea que arranca con numeración NUNCA es cola de título:
            # es el primer punto de la página (ric: '6.1. Normas…' a 13pt).
            seccion_corrida = seccion_corrida + " " + t
            ultima_top_seccion = contenido[0].top
            descartadas.append(contenido.pop(0))
            quitadas += 1
        else:
            break
    return contenido, descartadas, seccion_corrida


# ----------------------------------------------------------------- estructura

@dataclass
class Nodo:
    tipo: str                    # 'seccion' | 'punto'
    numero: str                  # '3' para sección, '3.9.1' para punto
    titulo: str                  # texto de la línea de label tras el número
    pagina: int
    label_x0: float | None = None
    text_col: float | None = None
    col_hijos: float | None = None       # columna donde corren los labels de sus hijos
    linea_label: Linea | None = None
    segmentos: list[list[Linea]] = field(default_factory=list)
    hijos: list["Nodo"] = field(default_factory=list)
    padre: "Nodo | None" = None

    def profundidad(self) -> int:
        return self.numero.count(".") + 1 if self.tipo == "punto" else 0


@dataclass
class ResultadoParseo:
    to: str
    archivo: str
    secciones: list[Nodo]
    rechazos_header: list[dict]
    saltos_numeracion: list[dict]
    avisos: list[dict]
    accounting: dict
    lineas_contenido: int
    paginas_cuerpo: int
    lineas_huerfanas: int = 0
    reasignaciones_continuidad: list[dict] = field(default_factory=list)
    correccion_fronteras: dict = field(default_factory=dict)


def _componentes(num: str) -> list[int]:
    return [int(x) for x in num.split(".")]


def parsear_cuerpo(to: str, archivo: str, paginas: list[list[Linea]],
                   roles: list[str]) -> ResultadoParseo:
    secciones: list[Nodo] = []
    rechazos: list[dict] = []
    saltos: list[dict] = []
    avisos: list[dict] = []
    acc_descartes: list[dict] = []
    pila: list[Nodo] = []                # [seccion, punto, subpunto, …]
    n_contenido = 0
    n_paginas_cuerpo = 0
    n_huerfanas = 0

    def cerrar_hasta(nodo: Nodo | None) -> None:
        """Deja la pila abierta hasta `nodo` inclusive (None → vacía)."""
        while pila and (nodo is None or pila[-1] is not nodo):
            pila.pop()

    def anexar(nodo: Nodo, linea: Linea, nuevo_segmento: bool) -> None:
        if nuevo_segmento or not nodo.segmentos or nodo.segmentos[-1] is None:
            nodo.segmentos.append([linea])
        else:
            nodo.segmentos[-1].append(linea)

    for pi, (lineas, rol) in enumerate(zip(paginas, roles), start=1):
        if rol != ROL_CUERPO:
            continue
        n_paginas_cuerpo += 1
        contenido, descartadas, seccion_corrida = separar_encabezado_pie(lineas)
        for d in descartadas:
            acc_descartes.append({"pagina": d.pagina, "texto": d.texto})

        if seccion_corrida is None:
            avisos.append({"tipo": "pagina_cuerpo_sin_seccion", "pagina": pi,
                           "primeras_lineas": [l.texto for l in contenido[:3]]})
            # las líneas siguen el flujo del punto abierto (página de continuación
            # con encabezado anómalo); no se tiran.
        else:
            m = RE_SECCION.match(seccion_corrida)
            num_sec, titulo_sec = m.group(1), m.group(2).strip()
            actual = pila[0] if pila else None
            if actual is None or actual.numero != num_sec:
                # arranca una sección nueva
                if any(s.numero == num_sec for s in secciones):
                    avisos.append({"tipo": "seccion_reabierta", "numero": num_sec,
                                   "pagina": pi})
                cerrar_hasta(None)
                sec = Nodo(tipo="seccion", numero=num_sec, titulo=titulo_sec, pagina=pi)
                if secciones and _componentes(num_sec)[0] != _componentes(secciones[-1].numero)[0] + 1:
                    saltos.append({"tipo": "salto_seccion", "de": secciones[-1].numero,
                                   "a": num_sec, "pagina": pi})
                secciones.append(sec)
                pila.append(sec)

        if not pila:
            if contenido:
                n_huerfanas += len(contenido)
                avisos.append({"tipo": "contenido_antes_de_seccion", "pagina": pi,
                               "n_lineas": len(contenido),
                               "lineas": [l.texto for l in contenido[:3]]})
            continue

        seccion = pila[0]
        ultima_fue_label = False
        previa: Linea | None = None

        for linea in contenido:
            anterior, previa = previa, linea
            n_contenido += 1
            tokens = linea.texto.split()
            m_num = RE_NUM_TOKEN.match(tokens[0]) if tokens else None
            if not m_num and tokens:
                m_num = RE_NUM_TOKEN_SIN_PUNTO.match(tokens[0])

            if m_num:
                num = m_num.group(1)
                comp = _componentes(num)
                resto = linea.texto.split(None, 1)
                resto = resto[1] if len(resto) > 1 else ""
                # forma del resto: un punto real lleva título/texto en la línea
                # del label. Numeración sola ('9.3.13.') = referencia envuelta,
                # rechazo incondicional. Resto en minúscula puede ser referencia
                # envuelta (RX-03: 'en el marco de…') PERO también hay labels
                # reales en minúscula (ext 10.11.1 'el pago corresponda…'): se
                # acepta solo bajo secuencia ESTRICTA (sucesor inmediato) y
                # columna exactamente compatible, sin fallback de deriva.
                titulo_mayuscula = bool(resto) and bool(
                    re.match(r'^[A-ZÁÉÍÓÚÜÑ"“\'(«]', resto))
                motivo = None
                if comp[0] > MAX_RAIZ:
                    motivo = "raiz_mayor_a_max"
                elif not resto:
                    motivo = "resto_vacio_referencia_envuelta"
                elif str(comp[0]) != seccion.numero:
                    motivo = f"fuera_de_seccion_{seccion.numero}"
                elif len(comp) == 1:
                    motivo = "profundidad_1_es_seccion"
                else:
                    # padre abierto en la pila
                    padre_num = ".".join(str(c) for c in comp[:-1])
                    padre = None
                    for n in pila:
                        if n.tipo == "seccion" and len(comp) == 2:
                            padre = n
                            break
                        if n.tipo == "punto" and n.numero == padre_num:
                            padre = n
                            break
                    if padre is None:
                        motivo = f"padre_{padre_num}_no_abierto"
                    else:
                        hermanos = [h for h in padre.hijos if h.tipo == "punto"]
                        ultimo = _componentes(hermanos[-1].numero)[-1] if hermanos else 0
                        # contexto de lista: la línea previa abre o continúa una
                        # enumeración (':' de intro, ';' entre ítems). Los labels
                        # reales en minúscula viven en estas listas de condiciones
                        # (ext 10.11.x, 13.3.x, 13.4.x, 8.5.14.x — medidos).
                        contexto_lista = anterior is not None and bool(re.search(
                            r"[:;]\s*$|;\s*[yo]\s*$", anterior.texto.strip()))
                        if comp[-1] <= ultimo:
                            motivo = f"no_sucede_al_hermano_{ultimo}"
                        elif not titulo_mayuscula and comp[-1] != ultimo + 1 \
                                and not contexto_lista:
                            motivo = (f"resto_minuscula_y_salto_de_{ultimo}"
                                      f"_a_{comp[-1]}_sin_contexto_de_lista")
                        else:
                            # chequeo de columna, con fallback documentado: las
                            # columnas de label DERIVAN entre páginas (páginas
                            # provenientes de Comunicaciones con márgenes
                            # distintos), así que una columna incompatible solo
                            # rechaza si el resto de la línea NO parece título
                            # (los falsos headers RX-03 —referencias cruzadas a
                            # inicio de renglón— continúan una oración en
                            # minúscula: 'de las normas…', 'en el marco…').
                            columna_ok = True
                            detalle = ""
                            if hermanos:
                                if padre.col_hijos is not None \
                                        and abs(linea.x0 - padre.col_hijos) > TOL_X:
                                    columna_ok = False
                                    detalle = f"hermanos_en_{padre.col_hijos}"
                            elif padre.tipo == "punto":
                                if padre.text_col is not None:
                                    if abs(linea.x0 - padre.text_col) > TOL_X:
                                        columna_ok = False
                                        detalle = f"texto_del_padre_en_{padre.text_col}"
                                elif linea.x0 <= (padre.label_x0 or 0) + TOL_X:
                                    columna_ok = False
                                    detalle = f"label_del_padre_en_{padre.label_x0}"
                            # primer punto de una sección: sin restricción de
                            # columna (sección + secuencia bastan)
                            if not columna_ok:
                                if titulo_mayuscula:
                                    # deriva de columna tolerada solo con forma
                                    # de título; queda registrada como aviso
                                    avisos.append({
                                        "tipo": "aceptado_con_columna_derivada",
                                        "numero": num, "pagina": linea.pagina,
                                        "x0": linea.x0, "esperada": detalle,
                                        "texto": linea.texto[:90],
                                    })
                                elif contexto_lista:
                                    # label real en minúscula con columna derivada
                                    # dentro de una lista (caso medido: ext 13.3.1
                                    # 'el cliente accede…')
                                    avisos.append({
                                        "tipo": "aceptado_lista_minuscula",
                                        "numero": num, "pagina": linea.pagina,
                                        "x0": linea.x0, "esperada": detalle,
                                        "texto": linea.texto[:90],
                                    })
                                else:
                                    motivo = (f"resto_minuscula_y_columna_"
                                              f"{linea.x0}_incompatible_{detalle}")
                if motivo is None:
                    padre.col_hijos = padre.col_hijos if padre.col_hijos is not None else linea.x0
                    if comp[-1] != (ultimo + 1):
                        saltos.append({"tipo": "salto_hermano", "padre": padre.numero,
                                       "de": ultimo, "a": comp[-1], "pagina": linea.pagina})
                    cerrar_hasta(padre)
                    titulo = linea.texto[len(tokens[0]):].strip()
                    nodo = Nodo(tipo="punto", numero=num, titulo=titulo,
                                pagina=linea.pagina, label_x0=linea.x0,
                                linea_label=linea, padre=padre)
                    padre.hijos.append(nodo)
                    pila.append(nodo)
                    ultima_fue_label = True
                    continue
                else:
                    rechazos.append({"pagina": linea.pagina, "x0": linea.x0,
                                     "texto": linea.texto[:120], "motivo": motivo})
                    # sigue como prosa

            # prosa: anclar por columna
            profundo = pila[-1]
            # Primera continuación de un punto recién abierto: solo si corre
            # ESTRICTAMENTE más adentro que su label. Una línea a la altura del
            # label no es continuación del punto: es prosa del contenedor (la
            # columna de label de profundidad d es la columna de texto de d-1;
            # caso cierres del 2.7 de ext tras el 2.7.4 sin continuación).
            if ultima_fue_label and profundo.tipo == "punto" \
                    and profundo.text_col is None \
                    and linea.x0 > (profundo.label_x0 or 0) + TOL_X:
                profundo.text_col = linea.x0
                anexar(profundo, linea, nuevo_segmento=not profundo.segmentos)
                ultima_fue_label = False
                continue
            ultima_fue_label = False

            # re-anclaje a un ancestro: solo para líneas con forma de PROSA
            # (largo pleno y sin fronteras de columna). Las filas de tabla son
            # cortas o multi-columna y pueden caer por azar en la columna de un
            # ancestro (caso medido: tabla de aforos de cap p.108 en x0=103.3);
            # si re-anclaran, cerrarían puntos abiertos a mitad de tabla.
            es_prosa = linea.ngaps == 0 and len(linea.texto) >= 55
            ancla = None
            if es_prosa:
                for n in pila[:-1]:      # ancestros estrictos, del más superficial al más profundo
                    col = n.text_col
                    if col is not None and abs(linea.x0 - col) <= TOL_X:
                        ancla = n
                        break
            if ancla is not None and (profundo.text_col is None
                                      or abs(linea.x0 - profundo.text_col) > TOL_X):
                cerrar_hasta(ancla)
                anexar(ancla, linea, nuevo_segmento=True)
                continue

            # sección sin text_col aún (chapeau): la primera prosa la fija
            if profundo.tipo == "seccion" and profundo.text_col is None:
                profundo.text_col = linea.x0
            if profundo.tipo == "punto" and profundo.text_col is None:
                profundo.text_col = linea.x0
            nuevo = bool(profundo.segmentos) and profundo.segmentos[-1] \
                and abs(linea.x0 - profundo.segmentos[-1][-1].x0) > TOL_X
            anexar(profundo, linea, nuevo_segmento=nuevo)

    accounting = {
        "lineas_descartadas_encabezado_pie": len(acc_descartes),
        "detalle_descartes": acc_descartes,
    }
    return ResultadoParseo(
        to=to, archivo=archivo, secciones=secciones, rechazos_header=rechazos,
        saltos_numeracion=saltos, avisos=avisos, accounting=accounting,
        lineas_contenido=n_contenido, paginas_cuerpo=n_paginas_cuerpo,
        lineas_huerfanas=n_huerfanas,
    )


# ------------------------------------- Regla 1: continuidad de enumeración

# marcador de enumeración a inicio de línea: 'vii)', 'h)', '3)', '(ii)'.
# Solo minúsculas y solo con paréntesis de cierre: es la única forma de
# acápite usada en los 5 TOs (los estilos 'a.', 'I)', '1.-' no aparecen como
# ítems de enumeración y quedan fuera del detector — límite documentado).
RE_MARCADOR_ENUM = re.compile(r"^\(?([a-z]{1,5}|\d{1,2})\)\s+\S")


def _romano(n: int) -> str:
    out = ""
    for v, s in ((10, "x"), (9, "ix"), (5, "v"), (4, "iv"), (1, "i")):
        while n >= v:
            out, n = out + s, n - v
    return out


_ROMANOS = {_romano(n): n for n in range(1, 40)}


def _interpretaciones(token: str) -> set[tuple[str, int]]:
    """Familias de secuencia en las que el token es un valor: romano canónico
    minúscula (1–39), letra simple a–z (1–26), número (1–99). Un token puede
    vivir en varias ('i' es romano 1 y letra 9; 'x' romano 10 y letra 24): la
    ambigüedad se resuelve en `_es_sucesor`, que exige UNA familia común donde
    el candidato sea el sucesor inmediato."""
    out: set[tuple[str, int]] = set()
    if token in _ROMANOS:
        out.add(("romano", _ROMANOS[token]))
    if len(token) == 1 and "a" <= token <= "z":
        out.add(("letra", ord(token) - ord("a") + 1))
    if token.isdigit():
        out.add(("numero", int(token)))
    return out


def _es_sucesor(previo: str, candidato: str) -> bool:
    inter_c = _interpretaciones(candidato)
    return any((f, v + 1) in inter_c for f, v in _interpretaciones(previo))


def _ultimo_marcador_propio(nodo: Nodo) -> str | None:
    """Último marcador de enumeración a inicio de línea en el texto propio
    (label + segmentos) de un nodo. Límite: si el propio termina con una
    enumeración ANIDADA (ítems 'a)' dentro del acápite 'vi)'), el último
    marcador es el interno y una continuación del nivel externo no se
    detecta — falla hacia no reasignar, nunca hacia reasignar de más."""
    ultimo: str | None = None
    lineas: list[Linea] = [nodo.linea_label] if nodo.linea_label else []
    for s in nodo.segmentos:
        lineas.extend(s)
    for l in lineas:
        m = RE_MARCADOR_ENUM.match(l.texto.strip())
        if m:
            ultimo = m.group(1)
    return ultimo


def aplicar_continuidad_enumeracion(res: ResultadoParseo) -> list[dict]:
    """REGLA 1. Para cada hueco entre hijos consecutivos de un nodo: si los
    segmentos intersticiales que caen en ese hueco arrancan con un marcador
    que SUCEDE al último marcador del texto propio del hermano terminal
    inmediatamente anterior, se reasignan (segmento a segmento, en orden
    documental) como continuación del propio de ese hermano:

      * segmento cuyo primer renglón porta el marcador sucesor → se reasigna
        y el estado avanza con cada marcador line-initial del segmento que
        siga sucediendo;
      * segmento sin marcador cuyo primer renglón corre MÁS PROFUNDO que la
        columna del marcador (> TOL_X) → continuación envuelta del ítem, se
        reasigna con el estado sin avanzar;
      * cualquier otro segmento corta la cadena: nada posterior del hueco se
        reasigna (un marcador que reinicia en 'i)' es una enumeración nueva
        del padre, no una continuación).

    Alcance y límites (documentados): solo segmentos intersticiales (los
    'cierre' — tras el último hijo — son el mecanismo chapeau-perdido de U6 y
    quedan fuera); solo hermano anterior TERMINAL (si tiene hijos, su propio
    no es el texto que termina en la costura); familias romanos/letras/números
    con las formas de `RE_MARCADOR_ENUM`; enumeraciones anidadas: ver
    `_ultimo_marcador_propio`. Toda reasignación queda registrada con su
    evidencia."""
    reasignaciones: list[dict] = []

    def visitar(nodo: Nodo) -> None:
        for h in nodo.hijos:
            visitar(h)
        if not nodo.hijos:
            return
        marcas = [(h.pagina, h.linea_label.top if h.linea_label else 0.0)
                  for h in nodo.hijos]
        por_hueco: dict[int, list[list[Linea]]] = {}
        for s in nodo.segmentos:
            pos = (s[0].pagina, s[0].top)
            if pos < marcas[0] or pos > marcas[-1]:
                continue  # intro / cierre: fuera del alcance de la regla
            k = max(i for i, mp in enumerate(marcas) if mp < pos)
            por_hueco.setdefault(k, []).append(s)
        for k in sorted(por_hueco):
            hermano = nodo.hijos[k]
            if hermano.hijos:
                continue
            estado = _ultimo_marcador_propio(hermano)
            if estado is None:
                continue
            marc_x0: float | None = None
            for s in por_hueco[k]:
                primera = s[0]
                m = RE_MARCADOR_ENUM.match(primera.texto.strip())
                if m and _es_sucesor(estado, m.group(1)):
                    motivo = f"marcador '{m.group(1)}' sucede a '{estado}'"
                    for l in s:
                        mm = RE_MARCADOR_ENUM.match(l.texto.strip())
                        if mm and _es_sucesor(estado, mm.group(1)):
                            estado = mm.group(1)
                    marc_x0 = primera.x0
                elif m is None and marc_x0 is not None \
                        and primera.x0 > marc_x0 + TOL_X:
                    motivo = (f"continuación envuelta del ítem '{estado}' "
                              f"(x0 {primera.x0} > columna del marcador {marc_x0})")
                else:
                    break
                nodo.segmentos.remove(s)
                hermano.segmentos.append(s)
                reasignaciones.append({
                    "padre": nodo.numero if nodo.tipo == "punto" else f"S{nodo.numero}",
                    "destino": hermano.numero,
                    "pagina": primera.pagina, "x0": primera.x0,
                    "n_lineas": len(s), "motivo": motivo,
                    "primera_linea": primera.texto[:100],
                })

    for s in res.secciones:
        visitar(s)
    return reasignaciones


# --------------------------------- Regla 2: cero cortes intra-palabra

RE_GUION_FINAL = re.compile(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]-$")
RE_INICIO_MINUSCULA = re.compile(r"^[a-záéíóúüñ]")


def _recolectar_orden_documental(res: ResultadoParseo) -> list[tuple[Linea, tuple]]:
    """Todas las líneas de la estructura en orden documental (pagina, top, x0),
    cada una con su contenedor: ('label', nodo, i_seccion) o
    ('seg', nodo, segmento, i_seccion)."""
    entradas: list[tuple[Linea, tuple]] = []

    def rec(n: Nodo, i_sec: int) -> None:
        if n.linea_label is not None:
            entradas.append((n.linea_label, ("label", n, i_sec)))
        for s in n.segmentos:
            for l in s:
                entradas.append((l, ("seg", n, s, i_sec)))
        for h in n.hijos:
            rec(h, i_sec)

    for i, s in enumerate(res.secciones):
        rec(s, i)
    entradas.sort(key=lambda e: (e[0].pagina, e[0].top, e[0].x0))
    return entradas


def _clasificar_frontera(ult: Linea, prox_entrada: tuple | None, i_sec: int) -> str:
    """Clasifica la frontera que sigue a `ult` (última línea de un segmento):
    'intra_palabra' (corte a corregir), 'ok', o un motivo de exclusión
    auditable. Detector: la línea termina en letra+guion ASCII y la línea
    documental siguiente existe, no es label de nodo, está en la misma
    sección, tiene forma de prosa (sin fronteras de columna) y arranca en
    minúscula (el silabeo del BCRA continúa siempre en minúscula). Los guards
    sobre la línea SIGUIENTE matan los falsos positivos medidos: filas de
    rating 'AA- A- BBB- B-' y encabezados '-En millones de pesos-' (la fila
    siguiente arranca en dígito o mayúscula), cierres de aparte '-…-'
    seguidos de mayúscula, y celdas de tabla cuya continuación quedó
    desplazada por la linealización (la línea siguiente es otra fila o un
    código de partida). La línea que termina partida NO se filtra por ngaps
    propios: los renglones de definición de fórmula ('RM: … en la Sec-' →
    'ción 6.') tienen fronteras de columna y su continuación es genuina."""
    if not RE_GUION_FINAL.search(ult.texto.strip()):
        return "ok"
    if prox_entrada is None:
        return "sin_linea_siguiente"
    prox, cont = prox_entrada
    if cont[0] == "label":
        return "siguiente_es_label"
    if cont[-1] != i_sec:
        return "siguiente_en_otra_seccion"
    if prox.ngaps:
        return "excluida_siguiente_fila_tabla"
    if not RE_INICIO_MINUSCULA.match(prox.texto.strip()):
        return "excluida_inicio_no_minuscula"
    return "intra_palabra"


def detectar_fronteras_intra_palabra(res: ResultadoParseo) -> dict:
    """Cuenta las fronteras de segmento que caen intra-palabra (detector de
    `_clasificar_frontera`) sin corregir nada. Devuelve también las líneas
    sospechosas excluidas, para auditoría."""
    entradas = _recolectar_orden_documental(res)
    idx = {id(l): i for i, (l, _) in enumerate(entradas)}
    intra, excluidas = [], []
    vistos: set[int] = set()
    for l, cont in entradas:
        if cont[0] != "seg":
            continue
        seg = cont[2]
        if id(seg) in vistos or seg[-1] is not l:
            continue
        vistos.add(id(seg))
        i = idx[id(l)]
        prox = entradas[i + 1] if i + 1 < len(entradas) else None
        clase = _clasificar_frontera(l, prox, cont[3])
        unidad = cont[1].numero if cont[1].tipo == "punto" else f"S{cont[1].numero}"
        if clase == "intra_palabra":
            intra.append({"unidad": unidad, "pagina": l.pagina,
                          "ultima_linea": l.texto[-60:],
                          "siguiente": prox[0].texto[:60] if prox else None})
        elif clase != "ok":
            excluidas.append({"unidad": unidad, "pagina": l.pagina,
                              "clase": clase, "ultima_linea": l.texto[-60:]})
    return {"n_intra_palabra": len(intra), "fronteras": intra,
            "sospechosas_excluidas": excluidas}


def corregir_fronteras_intra_palabra(res: ResultadoParseo) -> dict:
    """REGLA 2. Corre cada frontera intra-palabra línea por línea: la línea
    documental siguiente (la que cierra la palabra) se mueve al final del
    segmento que terminaba partido, hasta punto fijo (si la línea movida
    también termina partida, la frontera se vuelve a correr). El donante que
    queda vacío se elimina. Solo cambia DÓNDE cae la frontera: ninguna línea
    se crea, se pierde ni se parte (la cobertura por identidad de objeto lo
    verifica). Los movimientos entre segmentos de un mismo nodo no alteran el
    texto propio (la concatenación es idéntica); los movimientos entre nodos
    corrigen costuras de re-anclaje que caían a mitad de palabra."""
    corridas: list[dict] = []
    guarda = 20000
    while guarda:
        guarda -= 1
        entradas = _recolectar_orden_documental(res)
        idx = {id(l): i for i, (l, _) in enumerate(entradas)}
        mov = None
        vistos: set[int] = set()
        for l, cont in entradas:
            if cont[0] != "seg":
                continue
            seg = cont[2]
            if id(seg) in vistos or seg[-1] is not l:
                continue
            vistos.add(id(seg))
            i = idx[id(l)]
            prox = entradas[i + 1] if i + 1 < len(entradas) else None
            if _clasificar_frontera(l, prox, cont[3]) == "intra_palabra":
                mov = (cont, prox)
                break
        if mov is None:
            break
        (_, nodo, seg, _), (prox_l, prox_cont) = mov
        _, nodo_don, seg_don, _ = prox_cont
        if seg_don[0] is not prox_l:
            # inconsistencia estructural: la línea siguiente no encabeza su
            # segmento; se registra y no se corrige (esperado: nunca)
            res.avisos.append({"tipo": "frontera_intra_palabra_no_corregible",
                               "pagina": prox_l.pagina, "texto": prox_l.texto[:80]})
            break
        seg_don.pop(0)
        seg.append(prox_l)
        if not seg_don:
            nodo_don.segmentos.remove(seg_don)
        corridas.append({
            "pagina": prox_l.pagina,
            "de_unidad": nodo_don.numero if nodo_don.tipo == "punto" else f"S{nodo_don.numero}",
            "a_unidad": nodo.numero if nodo.tipo == "punto" else f"S{nodo.numero}",
            "mismo_nodo": nodo_don is nodo,
            "linea_movida": prox_l.texto[:90],
        })
    return {"lineas_corridas": corridas, "n_corridas": len(corridas)}


# -------------------------------------------------------------------- índice

def parsear_indice(paginas: list[list[Linea]], roles: list[str]) -> list[dict]:
    """Entradas del índice: {tipo: seccion|punto|otro, numero, titulo, pagina}.
    Los títulos envueltos en varias líneas se re-unen (una línea sin numeración
    continúa la entrada previa)."""
    entradas: list[dict] = []
    for lineas, rol in zip(paginas, roles):
        if rol != ROL_INDICE:
            continue
        contenido, _desc, _sec = separar_encabezado_pie(lineas, capturar_seccion=False)
        for linea in contenido:
            t = linea.texto.strip()
            if RE_MARCA_INDICE.match(t):
                continue
            m_sec = RE_SECCION.match(t)
            tokens = t.split()
            m_num = RE_NUM_TOKEN.match(tokens[0]) if tokens else None
            if not m_num and tokens and re.match(r"^\d+(\.\d+)*$", tokens[0]) and len(tokens) > 1:
                m_num = re.match(r"^(\d+(?:\.\d+)*)$", tokens[0])  # índice sin punto final
            if m_sec:
                entradas.append({"tipo": "seccion", "numero": m_sec.group(1),
                                 "titulo": m_sec.group(2).strip(), "pagina": linea.pagina})
            elif m_num and int(m_num.group(1).split(".")[0]) <= MAX_RAIZ:
                entradas.append({"tipo": "punto", "numero": m_num.group(1),
                                 "titulo": t[len(tokens[0]):].strip(), "pagina": linea.pagina})
            elif entradas:
                entradas[-1]["titulo"] = (entradas[-1]["titulo"] + " " + t).strip()
            else:
                entradas.append({"tipo": "otro", "numero": None, "titulo": t,
                                 "pagina": linea.pagina})
    return entradas


# --------------------------------------------------------------- divergencias

def divergencias_indice_cuerpo(res: ResultadoParseo, indice: list[dict]) -> dict:
    """Comparación bidireccional a la granularidad que declara el índice."""
    idx_secciones = {e["numero"]: e for e in indice if e["tipo"] == "seccion"}
    idx_puntos = {e["numero"]: e for e in indice if e["tipo"] == "punto"}

    cuerpo_secciones = {s.numero: s for s in res.secciones}
    cuerpo_puntos: dict[str, Nodo] = {}

    def rec(n: Nodo):
        for h in n.hijos:
            cuerpo_puntos[h.numero] = h
            rec(h)
    for s in res.secciones:
        rec(s)

    anunciado_sin_cuerpo = []
    for num, e in idx_puntos.items():
        if num not in cuerpo_puntos:
            anunciado_sin_cuerpo.append({"numero": num, "titulo": e["titulo"],
                                         "pagina_indice": e["pagina"]})
    for num, e in idx_secciones.items():
        if num not in cuerpo_secciones:
            anunciado_sin_cuerpo.append({"numero": f"S{num}", "titulo": e["titulo"],
                                         "pagina_indice": e["pagina"]})

    profundidad_indice = max((n.count(".") + 1 for n in idx_puntos), default=0)
    en_cuerpo_sin_anunciar = []
    for num, n in cuerpo_puntos.items():
        if num.count(".") + 1 <= profundidad_indice and num not in idx_puntos:
            en_cuerpo_sin_anunciar.append({"numero": num, "titulo": n.titulo[:100],
                                           "pagina_cuerpo": n.pagina})
    for num, s in cuerpo_secciones.items():
        if num not in idx_secciones:
            en_cuerpo_sin_anunciar.append({"numero": f"S{num}", "titulo": s.titulo[:100],
                                           "pagina_cuerpo": s.pagina})

    def _clave(d):
        return [int(x) for x in d["numero"].lstrip("S").split(".")]
    return {
        "to": res.to,
        "profundidad_declarada_indice": profundidad_indice,
        "anunciado_sin_cuerpo": sorted(anunciado_sin_cuerpo, key=_clave),
        "en_cuerpo_sin_anunciar": sorted(en_cuerpo_sin_anunciar, key=_clave),
        "titulos_distintos": _titulos_distintos(idx_puntos, cuerpo_puntos),
    }


def _norm_titulo(t: str) -> str:
    t = unicodedata.normalize("NFKD", t.lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", " ", t).strip()


def _titulos_distintos(idx_puntos: dict, cuerpo_puntos: dict[str, Nodo]) -> list[dict]:
    out = []
    for num, e in idx_puntos.items():
        n = cuerpo_puntos.get(num)
        if n is None:
            continue
        ti, tc = _norm_titulo(e["titulo"]), _norm_titulo(n.titulo)
        if ti and tc and not (ti.startswith(tc[:25]) or tc.startswith(ti[:25])):
            out.append({"numero": num, "titulo_indice": e["titulo"][:90],
                        "titulo_cuerpo": n.titulo[:90]})
    return out


# ------------------------------------------------------------------- chunker

def _texto_segmento(seg: list[Linea]) -> str:
    return "\n".join(l.texto for l in seg)


def _paginas_de(lineas: list[Linea]) -> list[int]:
    return sorted({l.pagina for l in lineas})


def _flags_tabla_formula(lineas: list[Linea]) -> dict:
    """Heurísticas documentadas de detección (solo flag, sin tratamiento):

    contenido_tabular — señales de filas en columnas:
      * fuerte: línea con ≥2 fronteras de columna (huecos > GAP_COL pt), o
        marcador lexical 'Cuadro N' (modelos de información del ric);
      * débil: línea con ≥1 frontera y último token numérico (patrón
        'concepto … valor' de los cuadros de ponderadores), o con ≥1 frontera
        y primer token código (≥3 dígitos: filas 'código partida descripción').
      Flag si fuertes ≥ 3, o fuertes+débiles ≥ 5.

    formula — señales de expresión matemática:
      * línea con '=' (asignación de expresión, p.ej. 'C = (k x 0,08 x APR) + INC');
      * línea 'donde:' aislada (definición de términos de una expresión);
      * anuncio '…siguiente expresión:'.
    """
    fuertes = [l for l in lineas
               if l.ngaps >= 2 or re.match(r"^Cuadro \d", l.texto.strip())]
    debiles = [l for l in lineas
               if l.ngaps == 1 and (l.ultimo_numerico or l.primer_codigo)]
    tabular = len(fuertes) >= 3 or (len(fuertes) + len(debiles)) >= 5
    ev_tab = (fuertes + debiles)[:3]

    ev_for = []
    for l in lineas:
        t = l.texto.strip()
        if "=" in t or re.fullmatch(r"donde\s*:", t, re.IGNORECASE) \
                or re.search(r"siguiente\s+expresi[oó]n\s*:?\s*$", t, re.IGNORECASE):
            ev_for.append(l)
    formula = bool(ev_for)
    return {
        "contenido_tabular": tabular,
        "formula": formula,
        "evidencia_tabular": [l.texto[:90] for l in ev_tab] if tabular else [],
        "evidencia_formula": [l.texto[:90] for l in ev_for[:3]],
    }


def _rol_segmentos(nodo: Nodo) -> list[dict]:
    """Clasifica los segmentos de un nodo CON hijos por posición relativa:
    intro (antes del primer hijo), cierre (después del último), intersticial.
    La posición se determina por (página, top) de la primera línea del
    segmento contra las de los labels de los hijos."""
    if not nodo.hijos:
        return [{"rol": "contenido", "seg": s} for s in nodo.segmentos]
    marcas = []
    for h in nodo.hijos:
        ll = h.linea_label
        marcas.append((h.pagina, ll.top if ll else 0.0))
    primera, ultima = marcas[0], marcas[-1]
    out = []
    for s in nodo.segmentos:
        pos = (s[0].pagina, s[0].top)
        if pos < primera:
            rol = "intro"
        elif pos > ultima:
            rol = "cierre"
        else:
            rol = "intersticial"
        out.append({"rol": rol, "seg": s})
    return out


def _materializa_bloque(texto: str) -> bool:
    """Criterio de materialización de mini-chunks (enmienda 01 §2.a, letra):
    el bloque contiene texto además de su línea de título. Los tramos
    `encabezado` SON la línea de título (construida del label) y nunca llegan
    acá; para los segmentos de prosa —que no contienen la línea de label— el
    criterio se reduce a texto normalizado no vacío."""
    return bool("".join(texto.split()))


def construir_chunks(res: ResultadoParseo) -> list[dict]:
    chunks: list[dict] = []

    def _titulo_linea(a: Nodo) -> str:
        return (f"Sección {a.numero}. {a.titulo}" if a.tipo == "seccion"
                else f"{a.numero}. {a.titulo}")

    def herencia_de(nodo: Nodo) -> list[dict]:
        """Cadena de herencia: por cada ancestro (sección → … → padre),
        su título y sus segmentos no-terminales, cada tramo con provenance."""
        cadena: list[Nodo] = []
        n = nodo.padre
        while n is not None:
            cadena.append(n)
            n = n.padre
        cadena.reverse()
        tramos: list[dict] = []
        for a in cadena:
            unidad = a.numero if a.tipo == "punto" else f"S{a.numero}"
            tramos.append({"tipo": "encabezado", "unidad_origen": unidad,
                           "texto": _titulo_linea(a), "paginas": [a.pagina]})
            for item in _rol_segmentos(a):
                if item["rol"] == "contenido":
                    continue  # no ocurre: los ancestros tienen hijos
                rol = {"intro": "intro", "cierre": "cierre",
                       "intersticial": "intersticial"}[item["rol"]]
                seg = item["seg"]
                tramos.append({
                    "tipo": f"{'chapeau_seccion' if a.tipo == 'seccion' else rol}"
                            if a.tipo == "seccion" and rol == "intro"
                            else rol,
                    "unidad_origen": unidad,
                    "texto": _texto_segmento(seg),
                    "paginas": _paginas_de(seg),
                })
        return tramos

    def herencia_titulos(nodo: Nodo) -> list[dict]:
        """Cadena de títulos (tramos `encabezado`) desde la sección hasta el
        propio nodo inclusive: el contexto mínimo de orientación de un
        mini-chunk. Sin bloques de prosa: la prosa de cada ancestro tiene su
        propio mini-chunk responsable."""
        cadena: list[Nodo] = [nodo]
        n = nodo.padre
        while n is not None:
            cadena.append(n)
            n = n.padre
        cadena.reverse()
        return [{"tipo": "encabezado",
                 "unidad_origen": a.numero if a.tipo == "punto" else f"S{a.numero}",
                 "texto": _titulo_linea(a), "paginas": [a.pagina]}
                for a in cadena]

    def emitir_mini(nodo: Nodo, rol: str, segs: list[list[Linea]],
                    n_tramo: int | None) -> None:
        """Emite un mini-chunk desde uno o más segmentos contiguos del mismo
        rol de un nodo NO terminal (enmienda 01 §2.a). `n_tramo` numera los
        tramos múltiples de un mismo rol (solo intersticiales); None = único."""
        texto = "\n".join(_texto_segmento(s) for s in segs)
        if not _materializa_bloque(texto):
            return
        unidad = nodo.numero if nodo.tipo == "punto" else f"S{nodo.numero}"
        mini_id = f"{res.to}::{unidad}::{rol}" + (f"::{n_tramo}" if n_tramo else "")
        lineas = [l for s in segs for l in s]
        herencia = herencia_titulos(nodo)
        texto_herencia = "\n".join(t["texto"] for t in herencia)
        completo = (texto_herencia + "\n" + texto) if texto_herencia else texto
        chunks.append({
            "id": mini_id,
            "to": res.to,
            "archivo": res.archivo,
            "unidad": unidad,
            "titulo": f"[bloque {rol}] {nodo.titulo}",
            "tipo": "mini_chunk",
            "rol_bloque": rol,
            "paginas": _paginas_de(lineas),
            "texto": texto,
            "chars_propio": len(texto),
            "chars_completo": len(completo),
            "herencia": herencia,
            "flags": _flags_tabla_formula(lineas),
            "sha256_propio": hashlib.sha256(texto.encode("utf-8")).hexdigest(),
            "sha256_completo": hashlib.sha256(completo.encode("utf-8")).hexdigest(),
        })

    def emitir(nodo: Nodo) -> None:
        es_terminal = not nodo.hijos
        if es_terminal:
            lineas: list[Linea] = []
            if nodo.linea_label is not None:
                lineas.append(nodo.linea_label)
            for s in nodo.segmentos:
                lineas.extend(s)
            if nodo.tipo == "seccion":
                unidad = f"S{nodo.numero}"
                encabezado = f"Sección {nodo.numero}. {nodo.titulo}"
                texto_propio = "\n".join([encabezado] + [l.texto for l in lineas])
            else:
                unidad = nodo.numero
                texto_propio = "\n".join(l.texto for l in lineas)
            herencia = herencia_de(nodo)
            texto_herencia = "\n".join(t["texto"] for t in herencia)
            completo = (texto_herencia + "\n" + texto_propio) if texto_herencia else texto_propio
            flags = _flags_tabla_formula(lineas)
            chunks.append({
                "id": f"{res.to}::{unidad}",
                "to": res.to,
                "archivo": res.archivo,
                "unidad": unidad,
                "titulo": nodo.titulo,
                "tipo": "seccion_sin_puntos" if nodo.tipo == "seccion" else "punto_terminal",
                "paginas": _paginas_de(lineas) or [nodo.pagina],
                "texto": texto_propio,
                "chars_propio": len(texto_propio),
                "chars_completo": len(completo),
                "herencia": herencia,
                "flags": flags,
                "sha256_propio": hashlib.sha256(texto_propio.encode("utf-8")).hexdigest(),
                "sha256_completo": hashlib.sha256(completo.encode("utf-8")).hexdigest(),
            })
        else:
            # Nodo NO terminal: sus bloques estructurales se emiten como
            # mini-chunks (enmienda 01 §2.a) interleaved en orden documental —
            # intro/chapeau antes de los hijos, intersticiales en su hueco,
            # cierre después. La herencia de los hijos no cambia: el bloque
            # sigue viajando además como contexto.
            items = _rol_segmentos(nodo)
            intro_segs = [it["seg"] for it in items if it["rol"] == "intro"]
            cierre_segs = [it["seg"] for it in items if it["rol"] == "cierre"]
            intersticiales = [it["seg"] for it in items if it["rol"] == "intersticial"]
            rol_intro = "chapeau_seccion" if nodo.tipo == "seccion" else "intro"

            # hueco de cada intersticial: después del hijo k (mismas marcas
            # posicionales que _rol_segmentos)
            marcas = [(h.pagina, h.linea_label.top if h.linea_label else 0.0)
                      for h in nodo.hijos]
            por_hueco: dict[int, list[list[Linea]]] = {}
            for s in intersticiales:
                pos = (s[0].pagina, s[0].top)
                k = max(i for i, mp in enumerate(marcas) if mp < pos)
                por_hueco.setdefault(k, []).append(s)
            n_inter = len(intersticiales)
            contador_inter = 0

            if intro_segs:
                emitir_mini(nodo, rol_intro, intro_segs, None)
            for k, h in enumerate(nodo.hijos):
                emitir(h)
                for s in por_hueco.get(k, []):
                    contador_inter += 1
                    emitir_mini(nodo, "intersticial", [s],
                                contador_inter if n_inter > 1 else None)
            if cierre_segs:
                emitir_mini(nodo, "cierre", cierre_segs, None)

    for s in res.secciones:
        emitir(s)
    return chunks


# ------------------------------------------------------------------ cobertura

def verificar_cobertura(res: ResultadoParseo) -> dict:
    """Cero pérdida: toda línea de contenido del cuerpo pertenece a exactamente
    un lugar de la estructura (label de nodo o línea de un segmento).

    Método: se recorre el árbol contando líneas por identidad de objeto; el
    total debe igualar `lineas_contenido` del parseo, y ninguna línea puede
    aparecer dos veces (ids de objeto únicos)."""
    vistos: set[int] = set()
    duplicadas = 0
    total = 0

    def contar(l: Linea):
        nonlocal duplicadas, total
        if id(l) in vistos:
            duplicadas += 1
        vistos.add(id(l))
        total += 1

    def rec(n: Nodo):
        if n.linea_label is not None:
            contar(n.linea_label)
        for s in n.segmentos:
            for l in s:
                contar(l)
        for h in n.hijos:
            rec(h)

    for s in res.secciones:
        rec(s)
    return {
        "lineas_contenido_parseadas": res.lineas_contenido,
        "lineas_en_estructura": total,
        "lineas_duplicadas": duplicadas,
        "lineas_huerfanas": res.lineas_huerfanas,
        "cobertura_exacta": (total == res.lineas_contenido and duplicadas == 0
                             and res.lineas_huerfanas == 0),
    }


# ------------------------------------------------------------- serialización

def serializar_estructura(res: ResultadoParseo) -> dict:
    def ser(n: Nodo) -> dict:
        return {
            "tipo": n.tipo, "numero": n.numero, "titulo": n.titulo,
            "pagina": n.pagina, "label_x0": n.label_x0, "text_col": n.text_col,
            "segmentos": [
                {"rol": item["rol"], "paginas": _paginas_de(item["seg"]),
                 "chars": len(_texto_segmento(item["seg"])),
                 "texto": _texto_segmento(item["seg"])}
                for item in _rol_segmentos(n)
            ],
            "hijos": [ser(h) for h in n.hijos],
        }
    return {
        "to": res.to, "archivo": res.archivo,
        "paginas_cuerpo": res.paginas_cuerpo,
        "lineas_contenido": res.lineas_contenido,
        "secciones": [ser(s) for s in res.secciones],
        "rechazos_header": res.rechazos_header,
        "saltos_numeracion": res.saltos_numeracion,
        "avisos": res.avisos,
        "accounting": res.accounting,
        "reasignaciones_continuidad": res.reasignaciones_continuidad,
        "correccion_fronteras": res.correccion_fronteras,
    }


# ---------------------------------------------------------------- censo x.y

def inventario_nivel_mapa(res: ResultadoParseo) -> set[str]:
    """Unidades a la granularidad del mapa oráculo: puntos x.y del cuerpo, más
    'S<n>' para secciones sin puntos."""
    unidades: set[str] = set()
    for s in res.secciones:
        hijos_punto = [h for h in s.hijos if h.tipo == "punto"]
        if not hijos_punto:
            unidades.add(f"S{s.numero}")
        for h in hijos_punto:
            unidades.add(h.numero)
    return unidades
