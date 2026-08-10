"""
sampler.py — Muestreo estratificado de subgrafos (§3 del diseño). Código puro,
determinístico, con semilla declarada. Cero LLM.

Estratos:
  E-A  aristas de 1 salto.
  E-B  caminos de 2-3 saltos; mitad del estrato con >=1 tramo recorrible SOLO
       vía arista entrante (sub-estrato `entrante`, blanco de BKL-0027).
  E-C  vecindarios de hub (umbral de grado justificado con la distribución real).
  E-D  pares cuasi-duplicados con variación (similitud label+descripcion,
       diferencia en valores/calificadores).
  E-E  uniforme aleatorio sobre TODOS los nodos (control no sesgado: la
       población no se filtra; lo inelegible se descarta CON registro).

Cada sample produce: subgrafo (nodos+aristas), gold en ANCLAS DE PROVENANCE
(doc + punto, de las provenances reales), y metadatos (estrato, semilla, ids
locales SOLO como referencia de depuración).

Exclusión de territorio quemado (regla dura del mandato): un sample se
descarta, con registro, si CUALQUIER ancla de CUALQUIER nodo de su subgrafo
no es apta según la regla laudada del mapa de 5 sets (incluye la regla de
parciales: descarte si el ancla abarca un subpunto quemado). Es la lectura
estricta: el subgrafo entero es la respuesta, no solo el nodo final.

Poblaciones de los estratos dirigidos (A-D) — exclusiones documentadas:
  - type == TextoOrdenado: contenedores estructurales; sus aristas
    (establecida_en 3007, referencia 674, modificada_por 29 — 46 % del total)
    codifican pertenencia/origen, no contenido normativo navegable, y su
    "vecindario" es el documento entero.
  - type == Comunicacion: nodos de la tabla de origen normativo; sus anclas
    son multi-punto y ruidosas (un nodo puede portar >20 puntos dispersos del
    TO), no identifican un punto normativo único — no sirven como gold.
  - rol_fuente == esqueleto: nodos de diseño sin provenance PDF (sin ancla).
En E-E NO se excluye nada a priori: el control muestrea el grafo completo y
los casos inelegibles quedan en el registro de descartes con su motivo.

Determinismo: random.Random con semilla derivada por estrato
(f"{semilla}:{estrato}"). Mismo kg.json + mismo mapa + misma semilla =>
mismo output byte a byte (verificado en selftest.py).
"""

from __future__ import annotations

import argparse
import json
import random
from collections import Counter
from pathlib import Path

from comun import (KG_VIGENTE, MAPA_5SETS, Quemado, anclas_de_nodo,
                   load_kg_raw, sha256_de, tokens_contenido)

SEMILLA_DEFECTO = "sinteticas-faseA-v2"
VOLUMEN_POR_ESTRATO = 20

# E-C — umbral de hub. Justificación con la distribución real de grados del
# grafo vigente (ver `distribucion_grados()` y el reporte de la unidad):
# mediana 2, p95 = 4, p99 = 11; el 1,2 % de los nodos conectados tiene grado
# >= 10 (51 nodos), y ahí viven los roles-hub del historial de fallas
# (Sujeto_rol_sujeto_obligado_proteccion = 168, el de BKL-0027;
# Sujeto_entidad_financiera = 151). Umbral elegido: GRADO >= 10 — captura la
# cola alta real (p99) sin admitir nodos de conectividad mediana, y deja una
# población de hubs suficiente para 20 samples tras exclusiones.
HUB_UMBRAL_GRADO = 10
# Familia enumerable dentro del hub: mayor grupo (relation, direccion) con
# tamaño en [FAMILIA_MIN, FAMILIA_MAX]. Piso 3: enumerar <3 no es enumeración.
# Techo 25: una respuesta de >25 miembros no es una pregunta contestable y
# desborda el cap de 40 vecinos/dirección de ver_vecinos junto al resto.
FAMILIA_MIN, FAMILIA_MAX = 3, 25

# E-D — parámetros del detector de cuasi-duplicados (método en `_pares_ed`).
ED_JACCARD_MIN = 0.5
ED_DIFF_MAX = 8
ED_DF_MAX = 200      # tokens con document-frequency mayor no generan candidatos
ED_MAX_INTENTOS = None  # sin tope: la población de pares es finita y chica
# Sub-cuota estratificada de E-D (corrección pre-sellado): fracción del
# volumen reservada a pares INTER-TO — 0,25 => 5 inter + 15 intra sobre el
# volumen objetivo de 20. La cuota se computa por volumen (round), así escala
# en corridas de otro tamaño (p. ej. el selftest).
ED_FRACCION_INTER = 0.25

EB_MAX_INTENTOS = 20000  # caminatas aleatorias por sub-estrato


# --------------------------------------------------------------------------- #
# Estructuras                                                                  #
# --------------------------------------------------------------------------- #
class Grafo:
    """Vista cruda del kg.json con índices para el muestreo."""

    def __init__(self, kg_raw: dict):
        self.nodes = kg_raw["nodes"]
        self.edges = kg_raw["edges"]
        self.por_id = {n["id"]: n for n in self.nodes}
        self.salientes: dict[str, list] = {}
        self.entrantes: dict[str, list] = {}
        for e in self.edges:
            self.salientes.setdefault(e["source"], []).append(e)
            self.entrantes.setdefault(e["target"], []).append(e)
        self.grado = Counter()
        for e in self.edges:
            self.grado[e["source"]] += 1
            self.grado[e["target"]] += 1
        # anclas por nodo (cacheadas)
        self._anclas: dict[str, list] = {}
        for n in self.nodes:
            self._anclas[n["id"]] = anclas_de_nodo(n)[0]

    def anclas(self, nid: str) -> list:
        return self._anclas.get(nid, [])

    def vecinos_undirected(self, nid: str) -> list:
        """[(vecino_id, edge, direccion)] con direccion 'saliente'|'entrante'."""
        out = [(e["target"], e, "saliente") for e in self.salientes.get(nid, [])]
        inn = [(e["source"], e, "entrante") for e in self.entrantes.get(nid, [])]
        return out + inn

    def existe_saliente(self, a: str, b: str) -> bool:
        return any(e["target"] == b for e in self.salientes.get(a, []))


def distribucion_grados(g: Grafo) -> dict:
    """Distribución real de grados (se vuelca al reporte de la unidad)."""
    vals = sorted(g.grado.values(), reverse=True)
    buckets = [(1, 1), (2, 2), (3, 4), (5, 9), (10, 19), (20, 39),
               (40, 79), (80, 159), (160, 10**9)]
    hist = {f"{lo}-{hi if hi < 10**9 else '+'}":
            sum(1 for v in vals if lo <= v <= hi) for lo, hi in buckets}
    def pct(p):
        return vals[int(len(vals) * p)] if vals else 0
    return {
        "nodos_total": len(g.nodes),
        "nodos_conectados": len(g.grado),
        "nodos_aislados": len(g.nodes) - len(g.grado),
        "grado_max": vals[0] if vals else 0,
        "p99": pct(0.01), "p95": pct(0.05), "p90": pct(0.10),
        "mediana": vals[len(vals) // 2] if vals else 0,
        "histograma": hist,
        "hubs_grado_ge_umbral": sum(1 for v in vals if v >= HUB_UMBRAL_GRADO),
        "umbral_hub": HUB_UMBRAL_GRADO,
    }


# --------------------------------------------------------------------------- #
# Sampler                                                                      #
# --------------------------------------------------------------------------- #
class Sampler:
    def __init__(self, kg_path: Path = KG_VIGENTE, mapa_path: Path = MAPA_5SETS,
                 semilla: str = SEMILLA_DEFECTO):
        self.kg_path = Path(kg_path)
        self.semilla = semilla
        self.g = Grafo(load_kg_raw(self.kg_path))
        self.quemado = Quemado(mapa_path)
        self.descartes: list[dict] = []

    # ---------------- elegibilidad ---------------- #
    def _elegible_dirigido(self, nid: str) -> str | None:
        """None si el nodo puede integrar subgrafos de A-D; sino el motivo."""
        n = self.g.por_id.get(nid)
        if n is None:
            return "nodo_inexistente"
        if n.get("type") == "TextoOrdenado":
            return "tipo_textoordenado"
        if n.get("type") == "Comunicacion":
            return "tipo_comunicacion"
        if n.get("rol_fuente") == "esqueleto":
            return "rol_fuente_esqueleto"
        if not self.g.anclas(nid):
            return "sin_ancla_pdf"
        return None

    # ---------------- gate de quemado + armado ---------------- #
    def _armar_sample(self, estrato: str, sub_estrato: str | None,
                      nodos_ids: list, aristas: list, respuesta_ids: list,
                      pregunta_sobre: dict, contador: int) -> dict | None:
        """Valida quemado y arma el registro del sample; None si se descarta."""
        anclas_todas = []
        for nid in nodos_ids:
            a = self.g.anclas(nid)
            if not a:
                self._descartar(estrato, nodos_ids, "sin_ancla_pdf", nid)
                return None
            anclas_todas.extend(a)
        ok, detalle = self.quemado.todas_aptas(anclas_todas)
        if not ok:
            motivos = "; ".join(
                f"{d['to']}:{d['ancla']} {d['motivo']}"
                for d in detalle if d["veredicto"] == "descartado")
            self._descartar(estrato, nodos_ids, f"quemado: {motivos}")
            return None

        anclas_respuesta, vistos = [], set()
        for nid in respuesta_ids:
            for a in self.g.anclas(nid):
                key = (a["to"], a["ancla"])
                if key not in vistos:
                    vistos.add(key)
                    anclas_respuesta.append(a)
        prefijo = estrato.replace("E-", "E")
        sample = {
            "sample_id": f"{prefijo}-{contador:03d}",
            "estrato": estrato,
            "sub_estrato": sub_estrato,
            "semilla": f"{self.semilla}:{estrato}",
            "subgrafo": {
                "nodos": [self._nodo_resumen(nid) for nid in nodos_ids],
                "aristas": [{"source": e["source"], "relation": e["relation"],
                             "target": e["target"]} for e in aristas],
            },
            "gold": {
                # El gold que viaja entre grafos: SOLO anclas (doc + punto).
                "anclas": [{"to": a["to"], "ancla": a["ancla"],
                            "source_doc": a["source_doc"],
                            "location_ejemplo": a["location"]}
                           for a in anclas_respuesta],
            },
            "metadatos": {
                "pregunta_sobre": pregunta_sobre,
                # ids locales del grafo vigente: SOLO referencia de depuración,
                # no viajan como gold (los ids no existen en otros grafos).
                "debug_ids_respuesta": list(respuesta_ids),
                "debug_ids_subgrafo": list(nodos_ids),
            },
        }
        return sample

    def _nodo_resumen(self, nid: str) -> dict:
        n = self.g.por_id[nid]
        props = n.get("properties") or {}
        desc = props.get("descripcion") or props.get("description") or ""
        return {"id": nid, "type": n.get("type"), "label": n.get("label"),
                "descripcion": str(desc)[:500],
                "properties_extra": {k: v for k, v in props.items()
                                     if k not in ("descripcion", "description")},
                "anclas": [{"to": a["to"], "ancla": a["ancla"]}
                           for a in self.g.anclas(nid)]}

    def _descartar(self, estrato: str, ids, motivo: str, nodo=None):
        self.descartes.append({"estrato": estrato, "candidato": list(ids),
                               "nodo": nodo, "motivo": motivo})

    # ---------------- E-A: aristas 1 salto ---------------- #
    def muestrear_ea(self, volumen: int = VOLUMEN_POR_ESTRATO) -> list:
        rng = random.Random(f"{self.semilla}:E-A")
        candidatas = [
            e for e in self.g.edges
            if self._elegible_dirigido(e["source"]) is None
            and self._elegible_dirigido(e["target"]) is None
        ]
        rng.shuffle(candidatas)
        samples = []
        for e in candidatas:
            if len(samples) >= volumen:
                break
            s = self._armar_sample(
                "E-A", None, [e["source"], e["target"]], [e],
                respuesta_ids=[e["target"]],
                pregunta_sobre={"dado": e["source"], "relacion": e["relation"],
                                "respuesta": e["target"]},
                contador=len(samples) + 1)
            if s:
                samples.append(s)
        return samples

    # ---------------- E-B: caminos 2-3 saltos ---------------- #
    def _caminata(self, rng: random.Random, exigir_entrante: bool):
        """Una caminata aleatoria elegible, o (None, motivo)."""
        inicio = rng.choice(self.g.nodes)["id"]
        if self._elegible_dirigido(inicio) is not None:
            return None, f"inicio_inelegible:{self._elegible_dirigido(inicio)}"
        largo = rng.choice([2, 3])
        camino, aristas, tramos = [inicio], [], []
        actual = inicio
        for _ in range(largo):
            opciones = [
                (v, e, d) for (v, e, d) in self.g.vecinos_undirected(actual)
                if v not in camino and self._elegible_dirigido(v) is None
            ]
            if not opciones:
                return None, "sin_vecinos_elegibles"
            v, e, d = rng.choice(opciones)
            # Detección del sub-estrato: el tramo actual→v NO existe como
            # arista saliente desde `actual`; solo se recorre vía entrante.
            solo_entrante = (not self.g.existe_saliente(actual, v))
            tramos.append({"de": actual, "a": v, "relation": e["relation"],
                           "direccion_arista": d,
                           "solo_via_entrante": solo_entrante})
            camino.append(v)
            aristas.append(e)
            actual = v
        tiene_entrante = any(t["solo_via_entrante"] for t in tramos)
        if exigir_entrante != tiene_entrante:
            return None, ("sin_tramo_entrante" if exigir_entrante
                          else "con_tramo_entrante")
        return {"camino": camino, "aristas": aristas, "tramos": tramos}, None

    def muestrear_eb(self, volumen: int = VOLUMEN_POR_ESTRATO) -> list:
        rng = random.Random(f"{self.semilla}:E-B")
        mitad = volumen // 2
        objetivos = [("saliente", volumen - mitad, False), ("entrante", mitad, True)]
        samples, vistos = [], set()
        for sub, cupo, exigir in objetivos:
            logrados, intentos = 0, 0
            while logrados < cupo and intentos < EB_MAX_INTENTOS:
                intentos += 1
                res, _motivo = self._caminata(rng, exigir)
                if res is None:
                    continue  # rechazo estructural: no se registra (es el mecanismo
                              # de búsqueda, no un descarte de candidato formado)
                clave = tuple(res["camino"])
                if clave in vistos:
                    continue
                vistos.add(clave)
                s = self._armar_sample(
                    "E-B", sub, res["camino"], res["aristas"],
                    respuesta_ids=[res["camino"][-1]],
                    pregunta_sobre={"dado": res["camino"][0],
                                    "camino": res["camino"],
                                    "tramos": res["tramos"],
                                    "respuesta": res["camino"][-1]},
                    contador=len(samples) + 1)
                if s:
                    samples.append(s)
                    logrados += 1
        return samples

    # ---------------- E-C: vecindarios de hub ---------------- #
    def muestrear_ec(self, volumen: int = VOLUMEN_POR_ESTRATO) -> list:
        rng = random.Random(f"{self.semilla}:E-C")
        hubs = [nid for nid, gr in self.g.grado.items()
                if gr >= HUB_UMBRAL_GRADO and self._elegible_dirigido(nid) is None]
        hubs.sort()          # orden estable antes del shuffle
        rng.shuffle(hubs)
        samples = []
        for hub in hubs:
            if len(samples) >= volumen:
                break
            grupos: dict[tuple, list] = {}
            for (v, e, d) in self.g.vecinos_undirected(hub):
                if self._elegible_dirigido(v) is None:
                    grupos.setdefault((e["relation"], d), []).append((v, e))
            candidatos = [(k, vs) for k, vs in grupos.items()
                          if FAMILIA_MIN <= len(vs) <= FAMILIA_MAX]
            if not candidatos:
                self._descartar("E-C", [hub],
                                "hub_sin_familia_enumerable_3_25")
                continue
            candidatos.sort(key=lambda kv: (-len(kv[1]), kv[0]))
            (relacion, direccion), familia = candidatos[0]
            vecinos = [v for v, _ in familia]
            s = self._armar_sample(
                "E-C", None, [hub] + vecinos, [e for _, e in familia],
                respuesta_ids=vecinos,
                pregunta_sobre={"hub": hub, "relacion": relacion,
                                "direccion": direccion,
                                "n_miembros": len(vecinos),
                                "grado_hub": self.g.grado[hub]},
                contador=len(samples) + 1)
            if s:
                samples.append(s)
        return samples

    # ---------------- E-D: pares cuasi-duplicados ---------------- #
    def _pares_ed(self):
        """Detección de pares cuasi-duplicados con variación.

        Método (documentado en el reporte de la unidad):
          1. Texto por nodo = label + descripcion; tokens de contenido
             (normalizados, sin stopwords).
          2. Bloqueo por token compartido con document-frequency <= ED_DF_MAX
             (tokens masivos no generan candidatos: costo O(pares reales)).
          3. Par candidato si: mismo type, Jaccard(tokens) >= ED_JACCARD_MIN,
             tokens no idénticos, y la VARIACIÓN es de valor/calificador:
             la diferencia simétrica contiene un token con dígito (plazo,
             porcentaje, número de comunicación) O tiene tamaño <= ED_DIFF_MAX
             (un calificador puntual, no un tema distinto).
          4. Orden determinístico por (-Jaccard, id_a, id_b).
        """
        toks: dict[str, set] = {}
        for n in self.nodes_ed():
            props = n.get("properties") or {}
            desc = props.get("descripcion") or props.get("description") or ""
            toks[n["id"]] = tokens_contenido(f"{n.get('label') or ''} {desc}")
        df = Counter()
        for ts in toks.values():
            df.update(ts)
        postings: dict[str, list] = {}
        for nid in sorted(toks):
            for t in toks[nid]:
                if df[t] <= ED_DF_MAX:
                    postings.setdefault(t, []).append(nid)
        vistos, pares = set(), []
        for t, ids in sorted(postings.items()):
            for i in range(len(ids)):
                for j in range(i + 1, len(ids)):
                    a, b = ids[i], ids[j]
                    if (a, b) in vistos:
                        continue
                    vistos.add((a, b))
                    if self.g.por_id[a]["type"] != self.g.por_id[b]["type"]:
                        continue
                    ta, tb = toks[a], toks[b]
                    if ta == tb:
                        continue
                    inter = len(ta & tb)
                    union = len(ta | tb)
                    if union == 0 or inter / union < ED_JACCARD_MIN:
                        continue
                    sd = ta ^ tb
                    tiene_valor = any(any(c.isdigit() for c in x) for x in sd)
                    if not (tiene_valor or len(sd) <= ED_DIFF_MAX):
                        continue
                    pares.append({"a": a, "b": b,
                                  "jaccard": round(inter / union, 3),
                                  "diff": sorted(sd)})
        pares.sort(key=lambda p: (-p["jaccard"], p["a"], p["b"]))
        return pares

    def nodes_ed(self):
        return [n for n in self.g.nodes
                if self._elegible_dirigido(n["id"]) is None]

    def _es_inter_to(self, p: dict) -> bool:
        aa, ab = self.g.anclas(p["a"]), self.g.anclas(p["b"])
        return bool(aa and ab and aa[0]["to"] != ab[0]["to"])

    def muestrear_ed(self, volumen: int = VOLUMEN_POR_ESTRATO) -> list:
        rng = random.Random(f"{self.semilla}:E-D")
        pares = self._pares_ed()
        rng.shuffle(pares)
        # Sub-cuota estratificada intra/inter-TO (config ED_FRACCION_INTER).
        cuota = {"inter_to": round(volumen * ED_FRACCION_INTER)}
        cuota["intra_to"] = volumen - cuota["inter_to"]
        conteo = {"inter_to": 0, "intra_to": 0}
        samples, usados = [], set()
        for p in pares:
            if len(samples) >= volumen:
                break
            sub = "inter_to" if self._es_inter_to(p) else "intra_to"
            if conteo[sub] >= cuota[sub]:
                continue   # cupo del sub-estrato lleno: mecanismo de búsqueda,
                           # no descarte de calidad — no se registra
            if p["a"] in usados or p["b"] in usados:
                self._descartar("E-D", [p["a"], p["b"]],
                                "nodo_ya_usado_en_otro_par")
                continue
            objetivo, distractor = (p["a"], p["b"]) if rng.random() < 0.5 \
                else (p["b"], p["a"])
            s = self._armar_sample(
                "E-D", sub,
                [objetivo, distractor], [],
                respuesta_ids=[objetivo],
                pregunta_sobre={"objetivo": objetivo, "distractor": distractor,
                                "jaccard": p["jaccard"],
                                "tokens_diferencia": p["diff"]},
                contador=len(samples) + 1)
            if s:
                samples.append(s)
                usados.add(p["a"])
                usados.add(p["b"])
                conteo[sub] += 1
        return samples

    # ---------------- E-E: uniforme ---------------- #
    def muestrear_ee(self, volumen: int = VOLUMEN_POR_ESTRATO) -> list:
        rng = random.Random(f"{self.semilla}:E-E")
        ids = sorted(self.g.por_id)   # población COMPLETA: control no sesgado
        rng.shuffle(ids)
        samples = []
        for nid in ids:
            if len(samples) >= volumen:
                break
            if not self.g.anclas(nid):
                self._descartar("E-E", [nid], "sin_ancla_pdf", nid)
                continue
            s = self._armar_sample(
                "E-E", None, [nid], [], respuesta_ids=[nid],
                pregunta_sobre={"nodo": nid},
                contador=len(samples) + 1)
            if s:
                samples.append(s)
        return samples

    # ---------------- corrida completa ---------------- #
    def muestrear_todo(self, volumen: int = VOLUMEN_POR_ESTRATO) -> dict:
        self.descartes = []
        estratos = {
            "E-A": self.muestrear_ea(volumen),
            "E-B": self.muestrear_eb(volumen),
            "E-C": self.muestrear_ec(volumen),
            "E-D": self.muestrear_ed(volumen),
            "E-E": self.muestrear_ee(volumen),
        }
        return {
            "config": {
                "kg_path": str(self.kg_path),
                "kg_sha256": sha256_de(self.kg_path),
                "mapa": str(MAPA_5SETS),
                "semilla": self.semilla,
                "volumen_objetivo_por_estrato": volumen,
                "hub_umbral_grado": HUB_UMBRAL_GRADO,
                "familia_rango": [FAMILIA_MIN, FAMILIA_MAX],
                "ed_jaccard_min": ED_JACCARD_MIN,
                "ed_diff_max": ED_DIFF_MAX,
                "ed_df_max": ED_DF_MAX,
                "ed_fraccion_inter": ED_FRACCION_INTER,
                "ed_cuota_inter_sobre_volumen":
                    round(volumen * ED_FRACCION_INTER),
            },
            "distribucion_grados": distribucion_grados(self.g),
            "samples": [s for ss in estratos.values() for s in ss],
            "conteo_por_estrato": {k: len(v) for k, v in estratos.items()},
            "descartes": self.descartes,
        }


def main():
    ap = argparse.ArgumentParser(description="Sampler estratificado (fase A).")
    ap.add_argument("--semilla", default=SEMILLA_DEFECTO)
    ap.add_argument("--volumen", type=int, default=VOLUMEN_POR_ESTRATO)
    ap.add_argument("--salida", default=str(Path(__file__).parent / "out" /
                                            "samples.json"))
    args = ap.parse_args()
    s = Sampler(semilla=args.semilla)
    res = s.muestrear_todo(args.volumen)
    out = Path(args.salida)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1)
    print(f"samples: {res['conteo_por_estrato']}  "
          f"descartes: {len(res['descartes'])}  -> {out}")


if __name__ == "__main__":
    main()
