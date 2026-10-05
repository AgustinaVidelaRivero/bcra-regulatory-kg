"""
seleccion_p4b.py — U-PROMPT-R2, P4b (USD 0, sin API): la elección de las unidades de la prueba corta, por lectura y con
semilla declarada, sobre la e0-r2 de C2 (`e0_chunking/salida_tanda0_r2b/`, los diez TOs de la tanda 0).

Grupos y tamaños: los del diseño de P3c-1 (`p3c/diseno_p3c.md`, §8) y del «seguí» de P4b: a 4 (uno, un régimen de
transición con condiciones), b1 3 ítems, b2 3 ítems, los 4 encabezados de esas listas, c 4, d 4, e 4, el ejemplo 2
(`cla::5.1.1::intro`, `cla::5.1.1.1`) y f 1 (`cap::6.2.2.6`).

Excluidas (todas las del «seguí» y algunas más, por precaución):
  - las 76 unidades de P4 (`p4/salida/muestra_p4.json`);
  - toda unidad nombrada en un documento de U-PROMPT-R2 (`data/experiment/prompt_r2/**/*.md`: los diseños y frenos de
    P1 a P3c-2, que incluyen los casos de control de P1 y de P3b-1, el diseño de P3c y la lectura de P4) o en lo que
    se leyó para escribir la regla f (las lecturas de U-DIAG-VINCULO que P4 ya excluía);
  - los contenedores y los ítems de las diez listas que P4 leyó (las cinco del estrato y las cinco descartadas,
    `p4/estrato_listas_excepciones.md`).

Pools, definidos en palabras y armados por forma, sin leer; el orden de lectura es
random.Random(f"{SEMILLA}:{pool}").shuffle sobre los ids ordenados:
  - a_transicion: texto propio con una forma de transición o de aplicabilidad temporal;
  - a: texto propio con una cláusula de alcance o de modalidad, o un anuncio con una norma (termina en «:» y trae un
    deber o una facultad);
  - listas: las listas de la e0-r2b (el bloque heredado que abre la lista de un ítem, `prompt_r2b.bloque_lista`)
    cuyo encabezado trae una negación o una forma de excepción o de exclusión (RX_LISTA), con su `::intro` y algún
    ítem fuera de las excluidas, sin `cla::5.1.1`; la lectura decide si son b1 (lo que queda afuera de una clase),
    b2 (las condiciones de una sola excepción) o ninguna, con las definiciones de COMPOSICIÓN del prefijo;
  - c: texto propio con una cuantía y dos o más marcas de supuesto;
  - d: ítems de lista cuyo encabezado tiene unidad propia (su `::intro`) y trae un deber, una prohibición o una
    facultad;
  - e: unidades de un TO con rol de alcance cuyo texto propio y heredado no trae ninguna forma de sujeto de la lista
    SUJETO_FORMAS y cuyo texto propio trae un deber, una prohibición o una facultad.
La lectura toma, en ese orden, los primeros que cumplen la definición del grupo, y registra cada descarte con su
razón (DECISIONES). Dentro de una lista elegida, los ítems se toman en el orden de
random.Random(f"{SEMILLA}:lista:{contenedor}").shuffle.

Uso (desde la raíz de una COPIA del repo):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p4b/seleccion_p4b.py --leer N --salida DIR
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p4b/seleccion_p4b.py --salida DIR
Con --leer escribe `lectura_candidatos_p4b.md` (los N primeros de cada pool, con su texto); sin él, `seleccion_p4b.json`.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
sys.path.insert(0, str(REPO / "data" / "experiment" / "pyd_r2" / "code"))
sys.path.insert(0, str(REX / "e1_extractor"))
import reglas_comparacion as RCMP  # noqa: E402
import prompt_r2b as PR  # noqa: E402
import perfil_e1  # noqa: E402

SEMILLA = "U-PROMPT-R2:P4b:2026-10-04"
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
E0 = REX / "e0_chunking" / "salida_tanda0_r2b"
FIJOS = {"ejemplo": ["cla::5.1.1::intro", "cla::5.1.1.1"], "f": ["cap::6.2.2.6"]}
TAMANOS = {"a_transicion": 1, "a": 3, "c": 4, "d": 4, "e": 4}
ITEMS_POR_TIPO = {"b1": 3, "b2": 3}   # ítems de b1 y de b2; los encabezados son los de las listas tomadas
LEIDOS_REGLA_F = ("reports/u_diag_vinculo/anexo_u_diag_vinculo.md", "reports/u_diag_vinculo/reporte.md",
                  "reports/u_diag_vinculo/salidas/lectura_precision.md",
                  "reports/u_diag_vinculo/salidas/muestra_precision_fichas.md",
                  "reports/u_diag_vinculo/salidas/censo_anuncios.txt", "reports/u_diag_vinculo/regla_deteccion.md")
# Listas que P4 leyó (p4/estrato_listas_excepciones.md): las cinco del estrato y las cinco descartadas.
LISTAS_P4 = ("ext::3.5.6", "ext::13.4", "ext::3.3.3", "ctacte::6.2", "ctacte::5.1.2",
             "ext::3.5.4", "ext::2.6.1", "ext::7.8.4", "ext::2.7", "ext::3.16.2")
RX_ID = re.compile(r"\b([a-z]{2,8}::(?:[0-9S][0-9.]*[0-9]|[0-9])(?:::[a-z]+)?)")

RX_TRANSICION = re.compile(r"transitori|r[eé]gimen de transici|per[ií]odo de transici|hasta (el|la) (\d|d[ií]a|fecha)|"
                           r"a partir del? (\d|d[ií]a|1°|1º)|desde el (\d|d[ií]a)|entrar[aá]n? en vigencia|"
                           r"vigencia", re.I)
RX_ALCANCE_MOD = re.compile(r"a los (fines|efectos) de|comprend|abarc|alcanzad|alcanza a|se aplicar[aá]n?\b|"
                            r"ser[aá]n? de aplicaci[oó]n|resultar[aá]n? aplicables?|indistintamente|concurrentemente|"
                            r"cualquiera de|a opci[oó]n de|se recomienda|es recomendable|se aconseja|buenas? pr[aá]cticas?",
                            re.I)
RX_NORMA = re.compile(r"\b(deber[aá]n?|deben?|podr[aá]n?|pueden?|no podr[aá]n?|se requerir[aá]n?|se requiere|"
                      r"obligad[oa]s?|prohib\w*|tendr[aá]n? que)\b", re.I)
RX_LISTA = re.compile(r"\bno\b|exceptu|excluy|excluid|excepci|excepto|salvo|deduc|con exclusi|a excepci|"
                      r"no se consider|no computa", re.I)
RX_SUPUESTO = re.compile(r"\b(cuando|siempre que|en tanto|en caso de|a condici[oó]n de|en la medida en que|si|"
                         r"de verificarse|en los casos en que|mientras)\b", re.I)
# Formas de sujeto: los nombres de sujeto más frecuentes del corpus; si alguna aparece, la unidad no es de e.
SUJETO_FORMAS = re.compile(r"\b(entidad|entidades|banco|bancos|compa[nñ][ií]as?|sujetos?|cajas? de cr[eé]dito|"
                           r"emisor(es|a|as)?|proveedor(es)?|cliente|clientes|usuario|usuarios|titular|titulares|"
                           r"BCRA|Banco Central|Superintendencia|SEFyC|fiduciari\w*|agentes?|casas? de cambio|"
                           r"operadores?|corresponsal\w*|deudor(es)?|depositante\w*|empresas?|instituci[oó]n\w*|"
                           r"intermediari\w*|participantes?|adheridos?|administrador\w*|directorio|gerencia|"
                           r"auditor\w*|responsables?|obligados?|personas?)\b", re.I)

# La lectura: cid → ("toma" o "descarta", razón; para listas, "b1", "b2" o "descarta"). Se completa al leer.
DECISIONES: dict[str, tuple[str, str]] = {
    # a_transicion: un régimen de transición con condiciones
    "ext::4.7::intro": ("descarta", "facultad con cortes de fecha en lo que abarca, y anuncio de requisitos; no es un "
                                    "régimen de transición"),
    "ext::3.15.2.6": ("descarta", "«vigencia» es la de la garantía: un plazo, no una transición"),
    "ext::3.17.3.2": ("descarta", "una fecha desde la que se cuentan montos; no es una transición"),
    "ext::3.5.3.1": ("descarta", "un supuesto de una excepción (ítem de una lista de b2); no es una transición"),
    "ext::3.6.1.2": ("descarta", "un miembro excluido de una prohibición; no es una transición"),
    "ext::3.13.1.5": ("descarta", "una operatoria con monto y plazo; «vigencia» es la de otra operatoria"),
    "ext::13.1.4": ("toma", "régimen de transición con condiciones: los servicios prestados o devengados hasta el "
                            "12/12/23 siguen otro régimen, si la operación encuadra en 13.4, y la suscripción de "
                            "BOPREAL, si se cumplen los requisitos de 4.5"),
    # a: una cláusula de alcance o de modalidad, o un anuncio con una norma
    "ext::6.1.1": ("toma", "alcance de una clase: «Comprende monedas y billetes emitidos por un estado extranjero»"),
    "cap::10.3.3.1": ("toma", "alcance: a qué créditos se aplica una calificación («se podrá aplicar a los créditos "
                              "quirografarios…»), con el anuncio «será de aplicación lo siguiente»"),
    "cap::11.4": ("toma", "alcance: «A los efectos de la determinación de la RPC» acota la facultad de computar "
                          "(prueba de P3C-a3: sin la frase, la norma valdría para más casos)"),
    # c: una norma con dos o más supuestos, uno con cuantía
    "pro::3.1.3": ("descarta", "cada deber trae un solo supuesto; la cuantía es el plazo de un deber, no un supuesto"),
    "cap::5.3.1.3": ("toma", "ponderador de 0 % para los pases si la contraparte es participante esencial y se "
                             "cumplen las condiciones a) a h), una con cuantía («no supere los cuatro días hábiles»)"),
    "cla::6.5.4.5": ("toma", "reclasificar en el nivel superior si se pagó, sin atrasos de más de 31 días, el 10 % "
                             "de lo refinanciado y si se observan las otras condiciones"),
    "pro::2.2.2": ("descarta", "la cuantía es la medida del deber («al menos el 10 % de los equipos»), no un supuesto"),
    "ext::3.12.1": ("descarta", "un supuesto sin cuantía; la cuantía es el plazo de un deber"),
    "cap::6.2.1.4": ("descarta", "los supuestos no tienen cuantía; el 80 % es la medida de la consecuencia"),
    "ext::10.4.2.5": ("toma", "conformidad previa del BCRA si el cliente no es persona humana, se constituyó hasta "
                              "365 días antes y el monto pendiente supera USD 5 millones"),
    "ext::8.4.2": ("descarta", "cada norma trae un solo supuesto, sin cuantía"),
    "ext::10.3.6": ("toma", "acceso para cancelar cartas de crédito si la documentación demuestra las condiciones de "
                            "su fecha; desde el 13/12/23, condiciones con plazos de 15 días corridos"),
    # d: ítem de una lista cuyo encabezado tiene unidad propia y enuncia una norma
    "ext::10.4.3.6": ("toma", "el encabezado enuncia la facultad de dar acceso si se cumplen los requisitos; el ítem "
                              "es uno de ellos"),
    "cla::6.5.3.1": ("descarta", "el encabezado describe una categoría con sus indicadores; «pueden» no es una "
                                 "facultad: no enuncia una norma"),
    "ext::4.1.4.7": ("toma", "el encabezado enuncia el deber de conformidad previa para los pagos; el ítem es uno de "
                             "los casos (su encabezado se leyó antes; el ítem, no)"),
    "polcre::2.1.15": ("toma", "el encabezado enuncia el deber de aplicar la capacidad de préstamo a los destinos; el "
                               "ítem es un destino, con su límite"),
    "cap::10.2.2.4": ("toma", "el encabezado enuncia el deber de cumplir los criterios; el ítem es uno, con su deber"),
    # e: TO con alcance; el texto propio y el heredado no nombran al sujeto
    "cap::6.3.2::intro": ("toma", "deber impersonal («deberán incluirse en el cómputo»); nadie nombrado"),
    "cap::3.2::intro": ("toma", "deber impersonal («se deberán tratar»), con alcance; nadie nombrado"),
    "cap::6.5.3.2": ("descarta", "nombra al sujeto («las entidades financieras», partido por guion de fin de línea)"),
    "cap::8.5::intro": ("descarta", "encabezado puro de lista: su deber se extrae en los ítems (P3C-a6); no mide la "
                                    "relación de sujeto en su unidad"),
    "ext::7.1.2": ("descarta", "nombra al sujeto («Los exportadores»)"),
    "ctacte::12.9": ("descarta", "nombra a mercados y cámaras compensadoras, legibles como sujeto"),
    "ctacte::5.5.8": ("descarta", "nombra a la entidad financiera y al girado"),
    "ctacte::1.5.6": ("descarta", "nombra a las partes como sujeto de un deber"),
    "cap::6.3.2.1": ("toma", "deberes impersonales sobre las posiciones; nadie nombrado"),
    "ext::9.5": ("descarta", "nombra al exportador (como dato de la certificación), legible como sujeto"),
    "polcre::5.3": ("toma", "prohibición impersonal con su excepción («No podrán registrarse tenencias…»); nadie "
                            "nombrado"),
    # listas (b1, b2 o descarta), con las definiciones de COMPOSICIÓN del prefijo
    "cla::6.5.3": ("descarta", "indicadores de una categoría; no hay exclusión"),
    "ext::4.6.1": ("descarta", "requisitos de un deber; no hay exclusión"),
    "ext::4.5": ("descarta", "requisitos de un deber; no hay exclusión"),
    "lingob::7.1": ("descarta", "contenidos recomendados; no hay exclusión"),
    "ctacte::6.1.3": ("descarta", "enumeración taxativa de una definición; no hay exclusión"),
    "ext::4.3.2": ("descarta", "mecanismos alternativos de un deber; no hay exclusión"),
    "ext::7.5.5": ("descarta", "condiciones de una facultad; no hay exclusión"),
    "ctacte::12.8": ("descarta", "la lista es de aspectos a cumplir; la excepción del encabezado no la introduce"),
    "ext::7.8.5": ("descarta", "lo que una operación permite; no hay exclusión"),
    "ext::9.3.12": ("descarta", "condiciones de una facultad; no hay exclusión"),
    "ext::10.6.6": ("descarta", "condiciones de un deber; «excluidos» es parte del nombre de un producto"),
    "ext::4.8.4": ("descarta", "supuestos alternativos de una facultad; no hay excepción"),
    "ext::13.2": ("descarta", "supuestos de una facultad; no hay excepción"),
    "ext::8.5.3": ("descarta", "condiciones de una facultad; no hay excepción"),
    "ext::3.14": ("descarta", "casos de una facultad; no hay excepción"),
    "ext::3.5.3": ("b2", "la norma (conformidad previa para el acceso anticipado) y una única salvedad, «excepto que el "
                         "deudor encuadre en alguna de las siguientes situaciones»; cada ítem es un supuesto"),
    "ext::4.6.2": ("descarta", "requisitos de un deber; no hay exclusión"),
    "ext::10.10.2": ("descarta", "supuestos de una facultad; no hay excepción"),
    "ext::10.4.1": ("descarta", "lo que una clase comprende; no hay exclusión"),
    "ctacte::6.1.2": ("descarta", "casos incluidos en una definición; no hay exclusión"),
    "pro::2.3.9": ("descarta", "cláusulas que se tienen por no escritas: una nulidad, no lo que queda afuera de una "
                               "clase ni una salvedad"),
    "ctacte::3.2": ("b1", "lo que queda afuera de una clase, en otra forma: «no valdrá como cheque»; la clase es el "
                          "cheque y cada ítem nombra una clase de títulos que queda afuera. Lectura dudosa: también "
                          "admite la de supuestos de una sola exclusión, sin norma con salvedad"),
    "ext::8.2": ("descarta", "casos en que el exportador puede cambiar de entidad; no hay exclusión"),
    "ctacte::4.5.1": ("descarta", "requisitos de un deber; no hay exclusión"),
    "lingob::2.2": ("descarta", "buenas prácticas; no hay exclusión"),
    "cap::7.3": ("descarta", "límites de una exigencia; no hay exclusión"),
    "ext::3.4": ("descarta", "condiciones de una facultad; no hay excepción"),
    "ext::3.9": ("descarta", "requisitos de una facultad; no hay excepción con supuestos"),
    "ext::3.15.2": ("descarta", "condiciones de una facultad; no hay excepción"),
}


def chunks(to: str) -> dict:
    return {c["id"]: c for c in json.loads((E0 / f"chunks_{to}.json").read_text(encoding="utf-8"))}


def excluidas() -> tuple[set, dict]:
    m = json.loads((REPO / "data/experiment/prompt_r2/p4/salida/muestra_p4.json").read_text(encoding="utf-8"))
    p4 = set(m["fijos"]) | set(m["f1"]) | set(m["pata_e3"])
    p4 |= {c for e in m["sorteo"].values() for c in e["elegidos"]}
    p4 |= {c for v in m["listas_excepciones"].values() for c in v["tomados"]}
    p4 |= {c for v in m["fuera_de_muestra"].values() for c in v}
    assert len(p4) == 76, len(p4)
    # Sin los documentos de P4b, que nombran la propia selección.
    docs = sorted(str(p.relative_to(REPO)) for p in (REPO / "data/experiment/prompt_r2").rglob("*.md")
                  if "p4b" not in p.relative_to(REPO / "data/experiment/prompt_r2").parts)
    docs += list(LEIDOS_REGLA_F)
    nombradas = set()
    for d in docs:
        nombradas |= set(RX_ID.findall((REPO / d).read_text(encoding="utf-8")))
    return p4 | nombradas, {"p4": len(p4), "nombradas": len(nombradas), "documentos": docs}


def en_lista_p4(cid: str) -> bool:
    to, _, resto = cid.partition("::")
    unidad = resto.split("::")[0]
    return any(f"{to}::{unidad}" == x or f"{to}::{unidad}".startswith(x + ".") for x in LISTAS_P4)


def orden(pool: str, ids) -> list:
    o = sorted(ids)
    random.Random(f"{SEMILLA}:{pool}").shuffle(o)
    return o


def pools(ch: dict, excl: set) -> dict:
    libres = {cid: c for cid, c in ch.items() if cid not in excl and not en_lista_p4(cid)
              and cid not in FIJOS["ejemplo"] + FIJOS["f"]}
    rol = perfil_e1.perfil("r2b").rol_por_to
    out = {"a_transicion": [], "a": [], "c": [], "d": [], "e": []}
    for cid, c in libres.items():
        t = c.get("texto") or ""
        her = " ".join(h.get("texto") or "" for h in c.get("herencia") or [])
        if RX_TRANSICION.search(t):
            out["a_transicion"].append(cid)
        if RX_ALCANCE_MOD.search(t) or (t.rstrip().endswith(":") and RX_NORMA.search(t)):
            out["a"].append(cid)
        if RCMP.detectar_cuantias(t) and len(RX_SUPUESTO.findall(t)) >= 2:
            out["c"].append(cid)
        i = PR.bloque_lista(c)
        if i is not None:
            h = c["herencia"][i]
            intro = f"{c['to']}::{h.get('unidad_origen')}::intro"
            if intro in ch and RX_NORMA.search(h.get("texto") or ""):
                out["d"].append(cid)
        if ((rol.get(c["archivo"]) or {}).get("rol_id") and not SUJETO_FORMAS.search(t + " " + her)
                and RX_NORMA.search(t)):
            out["e"].append(cid)
    return {k: orden(k, v) for k, v in out.items()}


def listas(ch: dict, excl: set) -> dict:
    heads: dict = {}
    for cid, c in ch.items():
        i = PR.bloque_lista(c)
        if i is not None:
            h = c["herencia"][i]
            heads.setdefault(f"{c['to']}::{h.get('unidad_origen')}", {"texto": h["texto"], "items": []})["items"].append(cid)
    out = {}
    for k, v in heads.items():
        libres = sorted(x for x in v["items"] if x not in excl)
        if (RX_LISTA.search(v["texto"]) and not en_lista_p4(k) and k != "cla::5.1.1" and f"{k}::intro" in ch
                and f"{k}::intro" not in excl and libres):
            out[k] = {"items": sorted(v["items"]), "libres": libres}
    return {k: out[k] for k in orden("listas", out)}


def tomar(nombre: str, ids: list, k: int) -> tuple[list, list]:
    """Los primeros k que la lectura toma, en el orden del pool; todo lo anterior al último tomado tiene decisión."""
    tomados, leidos = [], []
    for cid in ids:
        if len(tomados) == k:
            break
        if cid not in DECISIONES:
            raise SystemExit(f"{nombre}: {cid} sin decisión de lectura antes de completar el grupo")
        leidos.append(cid)
        if DECISIONES[cid][0] == "toma":
            tomados.append(cid)
    if len(tomados) < k:
        raise SystemExit(f"{nombre}: {len(tomados)} de {k}")
    return tomados, leidos


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--leer", type=int, default=None)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    sal = a.salida.resolve()
    if REPO in sal.parents or sal == REPO:
        raise SystemExit("--salida no puede estar dentro del repo")
    sal.mkdir(parents=True, exist_ok=True)
    ch = {}
    for to in TOS:
        ch.update(chunks(to))
    excl, info = excluidas()
    ps = pools(ch, excl)
    ls = listas(ch, excl)
    if a.leer is not None:
        md = ["# Candidatos de P4b, en el orden de lectura (sin leer al armar los pools)", ""]
        for p, ids in ps.items():
            md += [f"## {p} ({len(ids)} en el pool)", ""]
            for cid in ids[:a.leer]:
                c = ch[cid]
                md += [f"### `{cid}`", "", f"Heredado: {' / '.join((h.get('texto') or '')[:200] for h in c.get('herencia') or [])}",
                       "", "```", (c.get("texto") or "").strip()[:2500], "```", ""]
        md += [f"## listas ({len(ls)} en el pool)", ""]
        for k in list(ls)[:a.leer]:
            md += [f"### `{k}`", "", "Encabezado: " + " ".join(ch[f"{k}::intro"]["texto"].split()), ""]
            md += [f"- `{x}`: " + " ".join((ch[x].get("texto") or "").split())[:400] for x in ls[k]["libres"]] + [""]
        (sal / "lectura_candidatos_p4b.md").write_text("\n".join(md) + "\n", encoding="utf-8")
        print(json.dumps({"excluidas": len(excl), **{k: v for k, v in info.items() if k != "documentos"},
                          "pools": {k: len(v) for k, v in ps.items()}, "listas": len(ls)}, ensure_ascii=False))
        return 0
    grupos, leidos = {}, {}
    for g, k in TAMANOS.items():
        grupos[g], leidos[g] = tomar(g, ps[g], k)
    # listas: se leen en orden hasta agotar el pool; cada tipo toma ítems hasta ITEMS_POR_TIPO
    listas_tomadas = {"b1": [], "b2": []}
    leidos["listas"] = []
    for k in ls:
        if k not in DECISIONES:
            raise SystemExit(f"listas: {k} sin decisión de lectura")
        leidos["listas"].append(k)
        tipo = DECISIONES[k][0]
        if tipo in listas_tomadas and sum(len(x["items"]) for x in listas_tomadas[tipo]) < ITEMS_POR_TIPO[tipo]:
            o = list(ls[k]["libres"])
            random.Random(f"{SEMILLA}:lista:{k}").shuffle(o)
            falta = ITEMS_POR_TIPO[tipo] - sum(len(x["items"]) for x in listas_tomadas[tipo])
            listas_tomadas[tipo].append({"contenedor": k, "orden_items": o, "items": o[:falta]})
    for t in ("b1", "b2"):
        grupos[f"{t}_items"] = [c for x in listas_tomadas[t] for c in x["items"]]
    grupos["b_encabezados"] = [f"{x['contenedor']}::intro" for t in ("b1", "b2") for x in listas_tomadas[t]]
    grupos["ejemplo"], grupos["f"] = FIJOS["ejemplo"], FIJOS["f"]
    todas = [c for v in grupos.values() for c in v]
    assert len(todas) == len(set(todas)), "una unidad en dos grupos"
    assert not (set(todas) - set(FIJOS["ejemplo"] + FIJOS["f"])) & excl
    pata_e3 = grupos["b_encabezados"] + ["cla::5.1.1::intro"] + grupos["a_transicion"] + grupos["a"][:1]
    out = {"semilla": SEMILLA, "e0": str(E0.relative_to(REPO)),
           "comando": "data/experiment/prompt_r2/p4b/seleccion_p4b.py --salida DIR",
           "exclusion": {"unidades": len(excl), **info},
           "pools": {k: len(v) for k, v in ps.items()} | {"listas": len(ls)},
           "grupos": grupos, "unidades": len(todas),
           "listas_tomadas": listas_tomadas,
           "pata_e3": pata_e3,
           "lectura": {g: [{"id": c, "decision": DECISIONES[c][0], "razon": DECISIONES[c][1]} for c in ids]
                       for g, ids in leidos.items()},
           "chars_propio": {c: len(ch[c].get("texto") or "") for c in todas}}
    txt = json.dumps(out, ensure_ascii=False, indent=1) + "\n"
    (sal / "seleccion_p4b.json").write_text(txt, encoding="utf-8")
    print(json.dumps({"unidades": len(todas), "grupos": {g: len(v) for g, v in grupos.items()}, "pata_e3": pata_e3,
                      "sha256": hashlib.sha256(txt.encode()).hexdigest()}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
