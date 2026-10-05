"""
t1_preguntas_control.py — U-REEXT-T0, T1, punto 6 (mandato firmado en e2027dd): las 15 preguntas de control. Repite el
procedimiento de la revisión independiente (reports/u_revision_libre/freno_a.md:70-72, en 54f57cd): quince preguntas
escritas desde los PDF, una búsqueda que emula BM25 sobre label, descripción e id de los nodos, y la lectura del
resultado. No son evaluación ni se reportan como resultado (mandato, T4, punto 2). USD 0, sin agente ni API.

La lectura de la revisión no está versionada como código: acá queda fijada por pregunta, escrita desde la respuesta del
PDF (la columna «Respuesta del PDF» de la revisión) y no desde el grafo:
  - `ancla`: el punto de la respuesta (TO y punto, con o sin sub-puntos);
  - `juzgar`: la regla que decide, sobre los nodos de contenido anclados ahí, entre «bien», «en parte», «falso» y «no»
    (sin respuesta). Las reglas que necesitan el texto del punto lo leen de la E0 (--e0).
La búsqueda BM25 (k1 = 1,2, b = 0,75; tokens alfanuméricos sin acentos ni mayúsculas) se corre con la consulta de cada
pregunta y se informa el rango del primer nodo anclado en el punto de la respuesta, entre los 50 primeros. El veredicto
no depende del rango: la revisión juzgó lo que el grafo dice en el punto, y una búsqueda emulada no es el Lucene del
agente.

Primero se corre sobre KG-Tanda0-Diez-r2a y se compara con la revisión (bien 8, en parte 2, falso 3, no 2); toda
diferencia se declara pregunta por pregunta. En T4 se corre sobre KG-Tanda0-Diez-r2b.

Corre desde la raíz de una COPIA del repo y escribe solo --out (fuera de la copia).
  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/reext_t0/t1_preguntas_control.py \
      --kg data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2a/r2/kg.json \
      --e0 data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b --out DIR/preguntas.json [--comparar-revision]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import unicodedata
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
REVISION = {1: "falso", 2: "bien", 3: "bien", 4: "bien", 5: "en parte", 6: "bien", 7: "en parte", 8: "no", 9: "falso",
            10: "bien", 11: "bien", 12: "falso", 13: "bien", 14: "no", 15: "bien"}
FUENTE_REVISION = "reports/u_revision_libre/freno_a.md:70-91 (54f57cd)"
ROL_PRO = "Sujeto_rol_sujeto_obligado_proteccion"
# pro 1.1.2 del PDF: las siete clases de sujetos obligados, con su id del catálogo r2
SIETE_PRO = ("Sujeto_entidad_financiera", "Sujeto_entidad_cambiaria", "Sujeto_fiduciario_de_fideicomiso_financiero",
             "Sujeto_empresa_no_financiera_emisora_de_tarjetas", "Sujeto_proveedor_no_financiero_de_credito",
             "Sujeto_pspcp", "Sujeto_psi_billetera_digital")


def norm(s) -> str:
    s = unicodedata.normalize("NFD", str(s or ""))
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", s.lower().replace("“", '"').replace("”", '"')).strip()


def _vals(o):
    if isinstance(o, dict):
        for v in o.values():
            yield from _vals(v)
    elif isinstance(o, list):
        for v in o:
            yield from _vals(v)
    else:
        yield str(o)


def texto(n: dict) -> str:
    return norm(" | ".join([n.get("label") or ""] + list(_vals(n.get("properties") or {}))))


def tokens(s: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", norm(s).replace("_", " "))


class Grafo:
    def __init__(self, kg: dict):
        self.N, self.E = kg["nodes"], kg["edges"]
        self.by = {n["id"]: n for n in self.N}
        self.sal: dict = {}
        self.ent: dict = {}
        for e in self.E:
            self.sal.setdefault(e["source"], []).append(e)
            self.ent.setdefault(e["target"], []).append(e)

    def anclados(self, to: str, punto: str, prefijo: bool = False) -> list[dict]:
        out = []
        for n in self.N:
            if n.get("type") == "Sujeto":
                continue
            for p in n.get("provenances") or [n.get("provenance") or {}]:
                pt = str(p.get("punto") or "")
                if p.get("to") == to and (pt == punto or (prefijo and pt.startswith(punto + "."))):
                    out.append(n)
                    break
        return out

    def a(self, nid: str, rel: str) -> list[str]:
        return [e["target"] for e in self.sal.get(nid, []) if e["relation"] == rel]


def umbrales(n: dict) -> list[dict]:
    u = (n.get("properties") or {}).get("umbrales")
    return u if isinstance(u, list) else []


def tiene_valor(n: dict, valor: str, unidad: str | None = None) -> bool:
    return any(str(u.get("valor")) == valor and (unidad is None or u.get("unidad") == unidad) for u in umbrales(n))


def num(t: str, v: str) -> bool:
    return re.search(rf"(?<![\d.,]){re.escape(v)}(?![\d])", t) is not None


class BM25:
    def __init__(self, nodos: list[dict], k1: float = 1.2, b: float = 0.75):
        self.ids = [n["id"] for n in nodos]
        self.docs = [Counter(tokens(" ".join([n.get("label") or "", str((n.get("properties") or {}).get("descripcion") or ""),
                                              n["id"]]))) for n in nodos]
        self.len = [sum(d.values()) for d in self.docs]
        self.avg = sum(self.len) / max(1, len(self.len))
        df = Counter(t for d in self.docs for t in d)
        N = len(self.docs)
        self.idf = {t: math.log(1 + (N - f + 0.5) / (f + 0.5)) for t, f in df.items()}
        self.k1, self.b = k1, b

    def buscar(self, consulta: str, k: int = 50) -> list[str]:
        q = tokens(consulta)
        puntajes = []
        for i, d in enumerate(self.docs):
            s = 0.0
            for t in q:
                f = d.get(t, 0)
                if f:
                    s += self.idf[t] * f * (self.k1 + 1) / (f + self.k1 * (1 - self.b + self.b * self.len[i] / self.avg))
            if s > 0:
                puntajes.append((-s, self.ids[i]))
        puntajes.sort()
        return [i for _, i in puntajes[:k]]


def texto_e0(e0: Path, to: str, punto: str, prefijo: bool = False) -> str:
    p = e0 / f"chunks_{to}.json"
    if not p.exists():
        return ""
    return norm(" ".join(c["texto"] for c in json.loads(p.read_text(encoding="utf-8"))
                         if c["unidad"] == punto or (prefijo and c["unidad"].startswith(punto + "."))))


# ---------------------------------------------------------------------------- reglas de lectura, una por pregunta
def p1(G, ns, e0):
    bancos = [n for n in ns if n["type"] == "Restriccion" and "banco" in texto(n) and "restantes" not in texto(n)]
    if any(tiene_valor(n, "5000000000") or num(texto(n), "5.000") for n in bancos):
        return "bien", "Restriccion de bancos con 5.000 millones"
    if any(tiene_valor(n, "2500000000") or num(texto(n), "2.500") for n in bancos):
        return "falso", "la Restriccion de bancos dice 2.500 millones"
    return "no", "sin Restriccion de bancos con monto"


def p2(G, ns, e0):
    con = [n for n in ns if "trimestr" in texto(n)]
    return ("bien", "nodo con «trimestr» en cla 6.3.1") if con else ("no", "ningún nodo de cla 6.3.1 dice la periodicidad")


def p3(G, ns, e0):
    con = [n for n in ns if num(texto(n), "90") and num(texto(n), "180")]
    return ("bien", "nodo con 90 y 180 días en cla 7.2.3") if con else ("no", "ningún nodo de cla 7.2.3 con 90 y 180")


def p4(G, ns, e0):
    con = [n for n in ns if num(texto(n), "10") and "dias habiles" in texto(n)]
    exc = [n for n in ns if n["type"] == "Excepcion" and not (G.a(n["id"], "exceptua") or G.a(n["id"], "exceptua_obligacion"))]
    if not con:
        return "no", "ningún nodo de pro 3.1.6 con 10 días hábiles"
    return "bien", f"10 días hábiles en pro 3.1.6; Excepcion sin conectar: {len(exc)} (informativo)"


def p5(G, ns, e0):
    multa = [n for n in ns if (tiene_valor(n, "4", "porcentaje") or num(texto(n), "4 %") or "4%" in texto(n))]
    cuantias = any((tiene_valor(n, "100") or num(texto(n), "100")) and (tiene_valor(n, "50000") or "50.000" in texto(n))
                   for n in multa) and any(("2%" in texto(n) or "2 %" in texto(n) or tiene_valor(n, "2", "porcentaje"))
                                           and num(texto(n), "30") for n in ns)
    if not multa or not cuantias:
        return "no", "faltan las cuantías de la multa (4 %, 100 a 50.000; 2 % a los 30 días)"
    falso_sujeto = [n["id"] for n in multa if "Sujeto_banco" in G.a(n["id"], "aplica_a")]
    falsa_rel = [n["id"] for n in multa if G.a(n["id"], "limita")]
    if falso_sujeto or falsa_rel:
        return "en parte", f"cuantías bien; multa con aplica_a al banco: {len(falso_sujeto)}, con limita: {len(falsa_rel)}"
    return "bien", "cuantías bien, sin sujeto ni relación falsos"


def p6(G, ns, e0):
    a30 = any(num(texto(n), "30") and "dias" in texto(n) for n in ns)
    a24 = any(num(texto(n), "24") and "meses" in texto(n) for n in ns)
    if a30 and a24:
        suj = sum(1 for n in ns if "Sujeto_banco" in G.a(n["id"], "aplica_a"))
        return "bien", f"30 días y 24 meses en ctacte 8.8.1.1; normas con aplica_a al banco: {suj} (informativo)"
    return ("en parte" if a30 or a24 else "no"), f"30 días: {a30}; 24 meses: {a24}"


def p7(G, ns, e0):
    t_e0 = texto_e0(e0, "pagjub", "2.9.2")
    contenido = any(num(texto(n), "41") for n in ns) and any("debit" in texto(n) for n in ns) \
        and any("multa" in texto(n) for n in ns)
    if not contenido:
        return "no", "faltan el art. 41, el débito o la multa en pagjub 2.9.2"
    prohibe_e0 = "no podra" in t_e0 or "prohib" in t_e0
    # la descripción, no el texto del nodo entero: el `tipo` «prohibicion» también contiene «prohib»
    inventadas = [n["id"] for n in ns if n["type"] == "Restriccion"
                  and (n.get("properties") or {}).get("tipo") == "prohibicion"
                  and any(x in norm((n.get("properties") or {}).get("descripcion")) for x in ("no podra", "prohib"))] \
        if not prohibe_e0 else []
    if inventadas:
        return "en parte", f"contenido presente; prohibición que el texto del punto no dice: {len(inventadas)}"
    return "bien", "art. 41, débito y multa, sin prohibición inventada"


def p8(G, ns, e0):
    pas = [n for n in ns if "pasaporte" in texto(n)]
    if not pas:
        return "no", "ningún nodo de docvig 2.1.1.1 con el pasaporte"
    vecinos = {t for n in pas for e in G.ent.get(n["id"], []) for t in [e["source"]]}
    alcance = any("transitori" in texto(n) or "precari" in texto(n) for n in ns + [G.by[v] for v in vecinos if v in G.by])
    return ("bien", "pasaporte con el alcance (residencia transitoria)") if alcance else \
        ("no", "el pasaporte está, sin decir a quién se aplica (residencia transitoria o precaria)")


def p9(G, ns, e0):
    con = [n for n in ns if "codigo de gobierno societario" in texto(n) and "anual" in texto(n)]
    if not con:
        return "no", "ningún nodo de lingob 2.1.1 con la evaluación anual del código"

    def recomendacion(n):
        t = texto(n)
        mod = (n.get("properties_no_definidas") or {}).get("modalidad_clasificada")
        return "buena practica" in t or "recomend" in t or mod == "consejo"
    deber = [n for n in con if n["type"] in ("Obligacion", "Restriccion") and not recomendacion(n)]
    return ("falso", f"tipada como deber sin marca de buena práctica: {[n['type'] for n in deber]}") if deber else \
        ("bien", "la evaluación anual figura como buena práctica")


def p10(G, ns, e0):
    con = [n for n in ns if "esa moneda" in texto(n)]
    return ("bien", "«en esa moneda» en polcre S10") if con else ("no", "ningún nodo de polcre S10 dice la moneda")


def p11(G, ns, e0):
    con = [n for n in ns if num(texto(n), "365") and "exporta simple" in texto(n)]
    return ("bien", "365 días para EXPORTA SIMPLE en ext 7.1.1.5") if con else ("no", "sin el plazo en ext 7.1.1.5")


def p12(G, ns, e0):
    ric = G.anclados("ric", "6.3", True)
    clase = {}
    for v, pat in (("4.5", r"4,5 ?%"), ("6", r"(?<![\d,])6 ?%"), ("8", r"(?<![\d,])8 ?%")):
        nodos = [n for n in ns if re.search(pat, texto(n)) or tiene_valor(n, v, "porcentaje")]
        limite = [n for n in nodos if any(str(u.get("valor")) == v and u.get("unidad") == "porcentaje"
                                          and str(u.get("comparacion", "")).startswith("minimo") for u in umbrales(n))]
        calc = [n for n in nodos if n["type"] == "Definicion" or (n.get("properties") or {}).get("tipo") == "calculo"
                or any(u.get("comparacion") == "coeficiente" for u in umbrales(n))]
        clase[v] = "limite" if limite else ("calculo_o_definicion" if calc else ("otro" if nodos else "ausente"))
    det = f"cap 8.5: {clase}; nodos de ric 6.3: {len(ric)}"
    if all(c == "limite" for c in clase.values()):
        return "bien", det
    if any(c == "calculo_o_definicion" for c in clase.values()):
        return "falso", det
    if all(c == "ausente" for c in clase.values()):
        return "no", det
    return "en parte", det


def p13(G, ns, e0):
    con = [n for n in ns if ("dos veces" in texto(n) or num(texto(n), "2") and "veces" in texto(n)) and "3.7" in texto(n)]
    return ("bien", "dos veces el importe de referencia del 3.7 en cla 3.3.3") if con else ("no", "sin el tope en cla 3.3.3")


def p14(G, ns, e0):
    mod = sum(1 for e in G.E if e["relation"] == "modificada_por")
    pie = sum(1 for n in G.N if any(k in json.dumps(n.get("provenances") or [], ensure_ascii=False) for k in ('"pie', "vigencia")))
    if mod and pie:
        return "bien", f"modificada_por {mod}; nodos con el pie o la vigencia en la procedencia {pie}"
    return ("en parte" if mod or pie else "no"), f"modificada_por {mod}; nodos con el pie o la vigencia en la procedencia {pie}"


def p15(G, ns, e0):
    miembros = {e["source"] for e in G.ent.get(ROL_PRO, []) if e["relation"] == "miembro_de"}
    estan = [i for i in SIETE_PRO if i in miembros]
    if len(estan) == len(SIETE_PRO):
        return "bien", f"las siete clases son miembro_de {ROL_PRO}"
    return ("en parte" if estan else "no"), f"miembros presentes {len(estan)} de 7"


PREGUNTAS = [
    (1, "¿Cuál es la exigencia básica de capital de un banco?", "5.000 millones (cap 1.2)", ("cap", "1.2", False),
     "exigencia basica capital minimo bancos", p1),
    (2, "¿Cada cuánto se revisa un cliente comercial con 5 % o más de la RPC?", "Trimestral (cla 6.3.1)",
     ("cla", "6.3.1", False), "revision clientes 5 % rpc trimestre", p2),
    (3, "¿Qué atraso define «riesgo medio» en consumo?", "Más de 90 y hasta 180 días (cla 7.2.3)", ("cla", "7.2.3", False),
     "riesgo medio atrasos dias", p3),
    (4, "¿En qué plazo se resuelve un reclamo?", "10 días hábiles, con tres salvedades (pro 3.1.6)", ("pro", "3.1.6", False),
     "plazo resolucion reclamo dias habiles", p4),
    (5, "¿Cuál es la multa por un cheque rechazado sin fondos?", "4 %, de $100 a $50.000; 2 % si se cancela en 30 días "
     "(ctacte 6.5.1)", ("ctacte", "6.5.1", False), "multa rechazo cheque insuficiencia fondos", p5),
    (6, "¿Cuándo cesa la inhabilitación por multas impagas?", "A los 30 días de cancelar; si no, a los 24 meses "
     "(ctacte 8.8.1.1)", ("ctacte", "8.8.1.1", False), "cese inhabilitacion multas impagas", p6),
    (7, "¿Qué pasa si se falsea la rendición de cuentas?", "Art. 41 de la LEF, débito y multa (pagjub 2.9.2)",
     ("pagjub", "2.9.2", False), "falseamiento rendicion de cuentas declaracion jurada", p7),
    (8, "¿Qué documento presenta un extranjero con residencia transitoria nacido en el Mercosur?",
     "Pasaporte o documento de viaje (docvig 2.1.1.1)", ("docvig", "2.1.1.1", False),
     "extranjero residencia transitoria mercosur documento", p8),
    (9, "¿Es obligatorio que el Directorio evalúe cada año el código de gobierno societario?",
     "No: es una buena práctica (lingob 2.1.1)", ("lingob", "2.1.1", False), "directorio evalue anualmente codigo gobierno societario", p9),
    (10, "¿En qué moneda se computan los depósitos de la cuenta de regularización que no son en dólares?",
     "En esa moneda (polcre, sección 10)", ("polcre", "S10", False), "cuenta especial regularizacion monedas extranjeras", p10),
    (11, "¿Qué plazo hay para liquidar divisas de EXPORTA SIMPLE?", "365 días corridos (ext 7.1.1.5)",
     ("ext", "7.1.1.5", False), "exporta simple plazo liquidacion", p11),
    (12, "¿Cuáles son los límites mínimos de COn1, PNb y RPC?", "4,5 %, 6 % y 8 % de los APR (cap 8.5; ric 6.3)",
     ("cap", "8.5", True), "limites minimos con1 pnb rpc apr", p12),
    (13, "¿Hasta qué monto se agrupan créditos comerciales con los de consumo?",
     "Dos veces el importe de referencia del punto 3.7 (cla 3.3.3)", ("cla", "3.3.3", False),
     "agrupar financiaciones comerciales consumo importe referencia", p13),
    (14, "¿Qué Comunicación fijó la versión vigente de un punto y desde cuándo rige?", "El pie de cada página lo dice",
     None, "comunicacion version vigente vigencia", p14),
    (15, "¿Quiénes son sujetos obligados en protección de usuarios?", "Siete clases (pro 1.1.2)", ("pro", "1.1.2", True),
     "sujetos obligados proteccion usuarios", p15),
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--kg", type=Path, required=True)
    ap.add_argument("--e0", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--comparar-revision", action="store_true",
                    help="compara con el resultado de la revisión (solo tiene sentido sobre KG-Tanda0-Diez-r2a)")
    a = ap.parse_args()
    kg_b = a.kg.read_bytes()
    G = Grafo(json.loads(kg_b))
    bm = BM25(G.N)
    filas = []
    for n, preg, resp, ancla, consulta, fn in PREGUNTAS:
        ns = G.anclados(*ancla) if ancla else []
        res, det = fn(G, ns, a.e0)
        top = bm.buscar(consulta, 50)
        ids_ancla = {x["id"] for x in ns}
        rango = next((i + 1 for i, x in enumerate(top) if x in ids_ancla), None)
        fila = {"n": n, "pregunta": preg, "respuesta_pdf": resp,
                "ancla": None if ancla is None else f"{ancla[0]}::{ancla[1]}" + (" y sub-puntos" if ancla[2] else ""),
                "nodos_anclados": len(ns), "consulta_bm25": consulta, "rango_bm25_del_ancla": rango,
                "en_los_10_primeros": rango is not None and rango <= 10, "resultado": res, "detalle": det}
        if a.comparar_revision:
            fila["revision"] = REVISION[n]
            fila["coincide"] = REVISION[n] == res
        filas.append(fila)
    tot = Counter(f["resultado"] for f in filas)
    out = {"comando": "data/experiment/reext_t0/t1_preguntas_control.py", "kg": str(a.kg),
           "kg_sha256": hashlib.sha256(kg_b).hexdigest(), "e0": str(a.e0), "preguntas": filas,
           "totales": {k: tot.get(k, 0) for k in ("bien", "en parte", "falso", "no")},
           "nota": "no son evaluación ni se reportan como resultado (mandato de U-REEXT-T0, T4, punto 2)"}
    if a.comparar_revision:
        rv = Counter(REVISION.values())
        out["revision"] = {"fuente": FUENTE_REVISION, "totales": {k: rv.get(k, 0) for k in ("bien", "en parte", "falso", "no")}}
        out["difieren"] = [{"n": f["n"], "revision": f["revision"], "script": f["resultado"], "detalle": f["detalle"]}
                           for f in filas if not f["coincide"]]
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for f in filas:
        print(f"{f['n']:2d} {f['resultado']:9s} rev={f.get('revision', '-'):9s} rango={f['rango_bm25_del_ancla']} {f['detalle'][:110]}")
    print("totales:", out["totales"], "| revisión:", out.get("revision", {}).get("totales"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
