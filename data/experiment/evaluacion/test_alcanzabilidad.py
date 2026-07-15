"""test_alcanzabilidad.py — módulo D1 de la capa determinística del verificador.

Prueba de alcanzabilidad léxica de un nodo portador, determinística y sin LLM.
Módulo NUEVO: solo importa de los congelados (loader.py, harness.py); no los modifica.

SEMÁNTICA PRE-REGISTRADA (verbatim del pedido de implementación)
----------------------------------------------------------------
- Vocabulario ex ante = tokens de la pregunta (usar EXACTAMENTE harness._tokens, la
  tokenización del índice) MENOS la lista fija STOPWORDS_ES definida como constante en el
  módulo (artículos, preposiciones, conjunciones frecuentes; lista cerrada, elegila estándar
  y dejala escrita) + los tokens_expuestos que reciba.
- Conjunto de consultas a simular: (a) las consultas_agente verbatim; (b) la pregunta entera;
  (c) todos los bigramas y trigramas contiguos de los tokens no-stopword de la pregunta.
  Generación determinística, sin LLM.
- Simulación: cada consulta contra harness.GraphIndex del grafo del run (loader.load_graph),
  limite=10, réplica exacta del scoring de buscar_nodos.
- Veredicto: alcanzable=True si el portador aparece en el top-10 de AL MENOS una consulta del
  conjunto; False si no. El dict devuelve además, por consulta: rank completo, score, tokens
  matcheados; y el vocabulario ex ante usado.

Notas de implementación (no alteran la semántica de arriba):
- Los `tokens_expuestos` NO generan consultas nuevas (el conjunto de consultas es exactamente
  (a)+(b)+(c)): integran el vocabulario ex ante, que se devuelve en el dict y se usa para
  anotar, por consulta, qué tokens quedaron FUERA del vocabulario ex ante
  (`tokens_fuera_vocabulario`) — la señal que permite juzgar si una consulta del agente usó
  vocabulario legítimo (pregunta + expuesto) o aprendido de otro lado.
- La réplica del scoring de `harness.GraphIndex.buscar_nodos` es literal:
  score = |tokens(consulta) ∩ tokens(label+id del nodo)|, orden (-score, len(label), id),
  top-`limite`. Un score 0 deja al nodo FUERA del ranking (rank = None).
- `run` acepta la clave del run (str, se carga vía loader.load_graph) o directamente un
  harness.GraphIndex ya construido (para tests con grafos sintéticos, sin tocar disco).
- Las consultas duplicadas (mismo string exacto) se simulan una sola vez, conservando el
  primer origen; la generación y el orden son determinísticos.
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import loader                      # congelado — solo import
from harness import GraphIndex, _tokens  # congelado — solo import

# --------------------------------------------------------------------------- #
# STOPWORDS_ES — lista CERRADA (artículos, preposiciones y conjunciones        #
# frecuentes del castellano). Los tokens del índice van en minúscula y sin     #
# acentos (harness._tokens), así que la lista se escribe igual.                #
# --------------------------------------------------------------------------- #
STOPWORDS_ES = frozenset({
    # artículos (y contracciones)
    "el", "la", "los", "las", "un", "una", "unos", "unas", "lo", "al", "del",
    # preposiciones
    "a", "ante", "bajo", "cabe", "con", "contra", "de", "desde", "durante",
    "en", "entre", "hacia", "hasta", "mediante", "para", "por", "segun",
    "sin", "so", "sobre", "tras",
    # conjunciones frecuentes
    "y", "e", "ni", "o", "u", "pero", "sino", "que", "si", "aunque",
    "porque", "pues", "como", "cuando",
})


# --------------------------------------------------------------------------- #
# Núcleo                                                                       #
# --------------------------------------------------------------------------- #
def _index_de(run):
    """run: clave de run (str) -> GraphIndex vía loader; o un GraphIndex ya armado."""
    if isinstance(run, GraphIndex):
        return run
    return GraphIndex(loader.load_graph(run))


def _simular_consulta(index, consulta, portador_id, limite=10):
    """Réplica exacta del scoring de GraphIndex.buscar_nodos, con rank completo del portador."""
    q = set(_tokens(consulta))
    scored = []
    for n in index.kg.nodes:
        score = len(q & index._node_tokens[n.id])
        if score:
            scored.append((score, len(n.label or ""), n.id))
    scored.sort(key=lambda t: (-t[0], t[1], t[2]))
    rank = next((i + 1 for i, (_, _, nid) in enumerate(scored) if nid == portador_id), None)
    score_p = len(q & index._node_tokens[portador_id])
    return {
        "total_con_match": len(scored),
        "rank": rank,                          # posición 1-based en el ranking completo; None si score 0
        "score": score_p,                      # tokens matcheados contra el portador
        "tokens_matcheados": sorted(q & index._node_tokens[portador_id]),
        "en_top10": rank is not None and rank <= limite,
    }


def _ngramas_contiguos(tokens, ns=(2, 3)):
    """Bigramas y trigramas contiguos (determinístico, en orden de aparición)."""
    out = []
    for n in ns:
        for i in range(len(tokens) - n + 1):
            out.append(" ".join(tokens[i:i + n]))
    return out


def evaluar_alcanzabilidad(portador_id, pregunta, consultas_agente, tokens_expuestos, run):
    """Evalúa la alcanzabilidad léxica del portador según la semántica pre-registrada
    del docstring del módulo. Función pura dado un grafo congelado: misma entrada →
    misma salida (sin LLM, sin azar, sin estado)."""
    index = _index_de(run)
    if portador_id not in index.by_id:
        raise ValueError(f"portador_id inexistente en el grafo: {portador_id!r}")

    tokens_pregunta = _tokens(pregunta)
    no_stopword = [t for t in tokens_pregunta if t not in STOPWORDS_ES]
    vocabulario_ex_ante = sorted(set(no_stopword) | set(tokens_expuestos or ()))

    # Conjunto de consultas: (a) agente verbatim, (b) pregunta entera, (c) n-gramas contiguos.
    plan = [(c, "agente") for c in (consultas_agente or [])]
    plan.append((pregunta, "pregunta_entera"))
    plan += [(c, "ngrama_pregunta") for c in _ngramas_contiguos(no_stopword)]

    vistos, consultas = set(), []
    vocab = set(vocabulario_ex_ante)
    for consulta, origen in plan:
        if consulta in vistos:
            continue
        vistos.add(consulta)
        r = _simular_consulta(index, consulta, portador_id, limite=10)
        r_out = {
            "consulta": consulta,
            "origen": origen,
            "tokens_fuera_vocabulario": sorted(
                t for t in set(_tokens(consulta)) if t not in vocab and t not in STOPWORDS_ES
            ),
            **r,
        }
        consultas.append(r_out)

    return {
        "portador_id": portador_id,
        "run": run if isinstance(run, str) else getattr(index.kg, "run_key", "<GraphIndex inyectado>"),
        "pregunta": pregunta,
        "alcanzable": any(c["en_top10"] for c in consultas),
        "vocabulario_ex_ante": vocabulario_ex_ante,
        "n_consultas_simuladas": len(consultas),
        "consultas": consultas,
    }


# --------------------------------------------------------------------------- #
# Helper: tokens expuestos desde una traza (re-ejecución determinística)       #
# --------------------------------------------------------------------------- #
def tokens_expuestos_de_trace(trace_path, hasta_paso=None, index=None):
    """Re-ejecuta determinísticamente los pasos de la traza (mismo mecanismo que
    verificador.py::_ver_paso_completo: mismo grafo congelado del run de la traza,
    mismo GraphIndex, mismos inputs) y devuelve el set de tokens (harness._tokens)
    de los outputs COMPLETOS de los pasos con n <= hasta_paso (todos si es None).

    El run se lee de la propia traza (elemento [0], clave 'run'). `index` opcional
    para reutilizar un GraphIndex ya construido del mismo run."""
    elem = json.load(open(trace_path))[0]
    steps = elem["trace"]["steps"]
    if index is None:
        index = _index_de(elem["run"])
    tokens = set()
    for s in steps:
        if hasta_paso is not None and s.get("n", 0) > hasta_paso:
            continue
        tool, inp = s.get("tool"), s.get("input") or {}
        if tool == "buscar_nodos":
            out = index.buscar_nodos(inp.get("consulta", ""), inp.get("limite", 10))
        elif tool == "ver_nodo":
            out = index.ver_nodo(inp.get("id", ""))
        elif tool == "ver_vecinos":
            out = index.ver_vecinos(inp.get("id", ""), inp.get("direccion", "ambas"))
        else:
            continue  # tool no re-ejecutable: no aporta tokens
        tokens |= set(_tokens(json.dumps(out, ensure_ascii=False)))
    return tokens


# --------------------------------------------------------------------------- #
# CLI                                                                          #
# --------------------------------------------------------------------------- #
def main(argv=None):
    ap = argparse.ArgumentParser(description="D1 — prueba determinística de alcanzabilidad léxica")
    ap.add_argument("--run", required=True, help="clave del run (p. ej. run_3)")
    ap.add_argument("--trace", required=True, help="path a la traza post-hoc del caso")
    ap.add_argument("--portador", required=True, help="id del nodo portador a evaluar")
    ap.add_argument("--hasta-paso", type=int, default=None,
                    help="límite de pasos para los tokens expuestos (default: todos)")
    args = ap.parse_args(argv)

    index = _index_de(args.run)
    elem = json.load(open(args.trace))[0]
    pregunta = elem["trace"]["question"]
    consultas_agente = [s["input"]["consulta"] for s in elem["trace"]["steps"]
                        if s.get("tool") == "buscar_nodos"]
    expuestos = tokens_expuestos_de_trace(args.trace, hasta_paso=args.hasta_paso, index=index)
    resultado = evaluar_alcanzabilidad(args.portador, pregunta, consultas_agente, expuestos, index)
    resultado["run"] = args.run
    resultado["trace"] = args.trace
    resultado["hasta_paso"] = args.hasta_paso
    resultado["n_tokens_expuestos"] = len(expuestos)
    print(json.dumps(resultado, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
