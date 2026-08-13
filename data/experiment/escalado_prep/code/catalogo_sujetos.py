"""Catálogo de sujetos del escalado: presión de fusión cross-TO y candidatos a
sujeto nuevo, por TO.

PROXY LÉXICO DETERMINÍSTICO, no adjudicación. Quién es sujeto de una norma lo
decide E1 (elige del catálogo cerrado de 65 entradas o emite
`sujeto_propuesto`), y E1 no se corre en esta unidad (costo autorizado USD 0).
Lo que sí se mide sin LLM es qué nombres de sujeto están escritos en el texto.

Tres señales, de más a menos dura:

  (A) COBERTURA DEL CATÁLOGO — menciones de las entradas de
      `data/experiment/grafo_v2/esquema_v2_clases.json` (label + alias). Todo
      TO que mencione un sujeto ya presente en el grafo v2 produce nodos que
      FUSIONAN por id canónico al ensamblar — el mecanismo está medido en
      `reextraccion_v2/corpus_v2/salida/reporte_ensamblado.json`
      (`merges_cross_to`), donde 21 de los 27 merges del corpus de 5 TOs son
      de tipo Sujeto. Es la señal que dimensiona la cuarentena de fusión.

  (B) SUJETO DEL PROPIO TÍTULO no cubierto por el catálogo — la mayoría de los
      TOs del BCRA se titulan por el sujeto que regulan. El título se marca
      como cubierto si alguna entrada NO abstracta del catálogo aparece en él
      con frontera de palabra; las raíces del árbol de clases quedan afuera del
      test porque marcarían cubierto cualquier título que diga 'sujetos'. Señal
      de alta precisión, muy pocos casos.

  (C) SINTAGMAS FRECUENTES no cubiertos — núcleo nominal tomado del propio
      catálogo ('entidades', 'proveedores', 'sociedades', …) más hasta dos
      modificadores, podados por derecha de artículos, preposiciones y formas
      verbales del registro normativo (ver COLA_INVALIDA), con ≥
      MIN_OCURRENCIAS apariciones. Screening: se reporta como candidato a
      adjudicar, nunca como hecho.

Cobertura del análisis: los TOs en los que E0 no engancha estructura producen
cero chunks y por lo tanto cero texto para (A) y (C); en esos casos solo (B)
es informativo. El campo `unidades_extraccion` de cada entrada permite
distinguirlos.

Normalización: minúsculas, sin diacríticos, sin puntuación, espacios
colapsados. Además de la forma publicada se busca una forma singularizada
mecánicamente (token de ≥5 chars terminado en 'es' → se le quitan 2; de ≥4
terminado en 's' → se le quita 1), porque las normas alternan 'las entidades
financieras' y 'la entidad financiera'.

Salidas: ../catalogo_sujetos.json, ../catalogo_sujetos_resumen.csv
"""

from __future__ import annotations

import csv
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).resolve().parent
PREP = AQUI.parent
REPO = PREP.parents[2]
E0_DRY = PREP / "e0_dry"
ESQUEMA = REPO / "data" / "experiment" / "grafo_v2" / "esquema_v2_clases.json"

MIN_OCURRENCIAS = 5
TOP_CANDIDATOS = 10
MAX_MODIFICADORES = 2

CONECTOR = r"(?:de|del|de la|de los|de las|no|y|o|en|a|al|con|para|por|que)"
PALABRA = r"[a-zñ]+"          # sin dígitos: los números nunca son parte del nombre


def norm(t: str) -> str:
    t = unicodedata.normalize("NFKD", t.lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9ñ ]+", " ", t)).strip()


def singular(t: str) -> str:
    out = []
    for w in t.split():
        if len(w) >= 5 and w.endswith("es"):
            out.append(w[:-2])
        elif len(w) >= 4 and w.endswith("s"):
            out.append(w[:-1])
        else:
            out.append(w)
    return " ".join(out)


# raíces abstractas del árbol de clases: ningún texto normativo nombra un
# sujeto llamándolo así, y usarlas para decidir cobertura marcaría como
# cubierto cualquier título que diga 'sujetos' o 'contrapartes'
RAICES_ABSTRACTAS = {"Sujeto_sujeto", "Sujeto_sujeto_regulado", "Sujeto_contraparte",
                     "Sujeto_estructura", "Sujeto_organismo_publico"}


def formas(texto_label: str) -> list[str]:
    """Formas buscables de un label. El catálogo publica el acrónimo y el
    desarrollo en un mismo string ('BCRA (Banco Central de la República
    Argentina)'): se indexan por separado, si no el desarrollo nunca matchea."""
    partes = [texto_label]
    partes += re.findall(r"\(([^)]+)\)", texto_label)
    partes.append(re.sub(r"\s*\([^)]*\)", "", texto_label))
    return [p for p in partes if p.strip()]


def cargar_catalogo() -> tuple[dict[str, str], set[str]]:
    esquema = json.loads(ESQUEMA.read_text(encoding="utf-8"))
    claves: dict[str, str] = {}
    nucleos: set[str] = set()
    for c in esquema["clases"]:
        for bruto in [c["label"], *c.get("alias", [])]:
            for f in formas(bruto):
                n = norm(f)
                if not n:
                    continue
                claves.setdefault(n, c["id"])
                claves.setdefault(singular(n), c["id"])
        cabeza = singular(norm(c["label"])).split()
        if cabeza and c["nivel"] == "clase":
            nucleos.add(cabeza[0])
    return claves, nucleos


# tokens que no pueden CERRAR el nombre de un sujeto: artículos, preposiciones,
# conjunciones, demostrativos y las formas verbales del registro normativo. El
# regex de candidatos no sabe dónde termina el sintagma y arrastra el verbo que
# sigue ('entidades deben tener'); se podan por derecha hasta que el sintagma
# cierre en una palabra que sí puede ser parte de un nombre.
COLA_INVALIDA = {
    "deben", "debe", "debera", "deberan", "deberia", "deberian", "podra", "podran",
    "puede", "pueden", "podria", "podrian", "tiene", "tienen", "tendra", "tendran",
    "sera", "seran", "es", "son", "esta", "estan", "estara", "estaran", "fue", "fueron",
    "haber", "hacer", "tener", "establecer", "cumplir", "informar", "remitir",
    "presentar", "operar", "cobrar", "aplicar", "considerar", "contar", "mantener",
    "registrar", "efectuar", "realizar", "obtener", "solicitar", "otorgar", "recibir",
    "se", "no", "que", "cuando", "cuyo", "cuya", "cuyos", "cuyas", "su", "sus",
    "la", "las", "los", "el", "un", "una", "unos", "unas", "lo",
    "del", "de", "y", "o", "u", "a", "al", "en", "con", "para", "por", "sobre",
    "ante", "desde", "hasta", "entre", "segun", "mismo", "misma", "mismos", "mismas",
    "dicho", "dicha", "dichos", "dichas", "tal", "tales", "este", "estos", "estas",
    "ese", "esa", "esos", "esas", "cada", "todo", "toda", "todos", "todas",
}


def podar(frase: str) -> str:
    t = frase.split()
    while t and t[-1] in COLA_INVALIDA:
        t.pop()
    return " ".join(t)


def cubierto(frase: str, claves: dict[str, str]) -> str | None:
    if frase in claves:
        return claves[frase]
    s = singular(frase)
    if s in claves:
        return claves[s]
    for k, cid in claves.items():
        if len(k.split()) < 2:
            continue
        # el sintagma contiene una entrada del catálogo, o es un prefijo de ella
        # ('banco central' recortado de 'banco central de la republica argentina')
        if k in frase or k in s or frase in k or s in k:
            return cid
    return None


def texto_de(ident: str) -> str:
    chunks = json.loads((E0_DRY / ident / f"chunks_{ident}.json").read_text(encoding="utf-8"))
    return "\n".join(c.get("texto", "") or "" for c in chunks)


def main() -> None:
    claves, nucleos = cargar_catalogo()
    re_cand = re.compile(
        rf"\b(?:{'|'.join(sorted(nucleos))})(?:s|es)?\b"
        rf"(?:\s+(?!{CONECTOR}\b){PALABRA}|\s+{CONECTOR}\s+{PALABRA}){{1,{MAX_MODIFICADORES}}}")

    inventario = {f["id"]: f for f in csv.DictReader(
        (PREP / "inventario_tos.csv").open(encoding="utf-8"))}
    conteos = json.loads((E0_DRY / "conteos_e0_dry.json").read_text(encoding="utf-8"))

    salida: dict[str, dict] = {}
    for ident in sorted(conteos):
        crudo = texto_de(ident)
        texto = norm(crudo)
        lineas = [l for l in crudo.split("\n") if l.strip()]

        presentes: dict[str, int] = {}
        for clave, cid in claves.items():
            # con frontera de palabra: `texto.count` daría falsos positivos por
            # subcadena (el alias 'SPE' aparecería dentro de 'respecto' y
            # 'especial', inflando esa clase a casi todos los TOs)
            n = len(re.findall(rf"\b{re.escape(clave)}\b", texto))
            if n:
                presentes[cid] = presentes.get(cid, 0) + n

        # (B) el título nombra un sujeto que el catálogo no tiene. Se decide por
        # cobertura, no por sintagma sintetizado: si alguna entrada NO abstracta
        # del catálogo aparece en el título, el título está cubierto.
        titulo = inventario[ident]["titulo_oficial"]
        tn = norm(titulo)
        cubre = sorted({cid for clave, cid in claves.items()
                        if cid not in RAICES_ABSTRACTAS
                        and re.search(rf"\b{re.escape(clave)}\b", tn)})
        m = re_cand.search(tn)
        sujeto_titulo = {
            "nucleo_detectado": m.group(0).strip() if m else None,
            "entradas_de_catalogo_en_el_titulo": cubre,
        }

        cand = Counter()
        for m in re_cand.finditer(texto):
            fr = podar(m.group(0).strip())
            if len(fr.split()) < 2 or cubierto(fr, claves):
                continue
            cand[fr] += 1
        top = [(f, n) for f, n in cand.most_common(TOP_CANDIDATOS * 5)
               if n >= MIN_OCURRENCIAS][:TOP_CANDIDATOS]
        ejemplos = {}
        for f, _ in top:
            for l in lineas:
                if f in norm(l):
                    ejemplos[f] = l.strip()[:200]
                    break

        salida[ident] = {
            "titulo_oficial": titulo,
            "categoria": inventario[ident]["categoria"],
            "unidades_extraccion": conteos[ident]["unidades_extraccion"],
            "sujetos_catalogo_presentes": dict(sorted(presentes.items(),
                                                      key=lambda kv: -kv[1])),
            "n_sujetos_catalogo": len(presentes),
            "sujeto_del_titulo": sujeto_titulo,
            "titulo_introduce_sujeto_nuevo": bool(
                sujeto_titulo["nucleo_detectado"]
                and not sujeto_titulo["entradas_de_catalogo_en_el_titulo"]),
            "candidatos_sujeto_nuevo": [
                {"frase": f, "ocurrencias": n, "ejemplo": ejemplos.get(f, "")}
                for f, n in top],
            "n_candidatos": len(top),
        }

    (PREP / "catalogo_sujetos.json").write_text(
        json.dumps(salida, ensure_ascii=False, indent=1), encoding="utf-8")

    with (PREP / "catalogo_sujetos_resumen.csv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["id", "titulo_oficial", "unidades_extraccion", "n_sujetos_catalogo",
                    "titulo_introduce_sujeto_nuevo", "sujeto_del_titulo",
                    "n_candidatos_sujeto_nuevo", "sujetos_catalogo_top5"])
        for ident, d in salida.items():
            w.writerow([ident, d["titulo_oficial"], d["unidades_extraccion"],
                        d["n_sujetos_catalogo"], d["titulo_introduce_sujeto_nuevo"],
                        d["sujeto_del_titulo"]["nucleo_detectado"] or "", d["n_candidatos"],
                        "; ".join(list(d["sujetos_catalogo_presentes"])[:5])])

    tot = Counter()
    for d in salida.values():
        for cid in d["sujetos_catalogo_presentes"]:
            tot[cid] += 1
    n_ids = len(set(claves.values()))
    print(f"TOs analizados: {len(salida)}")
    print(f"entradas del catálogo mencionadas en ≥1 TO nuevo: {len(tot)} de {n_ids}")
    print(f"TOs cuyo título nombra un sujeto fuera del catálogo: "
          f"{sum(1 for d in salida.values() if d['titulo_introduce_sujeto_nuevo'])}")
    print("entradas del catálogo por cantidad de TOs que las mencionan (top 20):")
    for cid, n in tot.most_common(20):
        print(f"  {n:4d} TOs  {cid}")


if __name__ == "__main__":
    main()
