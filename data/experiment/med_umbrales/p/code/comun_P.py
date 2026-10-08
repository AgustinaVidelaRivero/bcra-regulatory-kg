"""
comun_P.py — U-MED-UMBRALES, etapa P (el piloto, §9 de la enmienda 1 al pre-registro de tripletas, FIRMADA en a0f9815):
lo común a los scripts del tramo P-a. Sin API. Solo lectura de los insumos.

Corre desde la raíz de una COPIA del repo (CLAUDE.md §4.l): REPO es la raíz que contiene a este archivo
(data/experiment/med_umbrales/p/code/comun_P.py), y todo insumo se lee bajo esa raíz. La copia se arma con
preparar_espejo_P.py (git show HEAD de cada insumo rastreado; copia con sha256 de los PDFs, que .gitignore:35 deja
fuera del repo).

Fuentes de cada pieza (anclas en HEAD 2a70b20):
  - grafo: KG-Tanda0-Diez-r2b-sincola, e22fae1a (data/experiment/neo4j/grafos.py, entrada KG_Tanda0_Diez_r2b_sincola);
  - E0: e0_chunking/salida_tanda0_r2b/chunks_<to>.json, con las partes por corte de
    corpus_tanda0/salida_r2b/<to>/particiones_por_corte.json (runner_corpus.chunks_con_partes, runner_corpus.py:569-579);
    las dos rutas son las del reporte del ensamblado del grafo (ens_diez_r2b_sincola/r2/reporte_ensamblado_r2.json,
    «e0_salida» y «entrada»);
  - texto de una unidad: propio más heredado, unidos por salto (validador_r2.texto_completo, validador_r2.py:232-235),
    que es el texto contra el que el ensamblado verifica el tramo (ensamblar_tanda0.py:628-634);
  - crudo de E1 de una unidad: el del intento que E3 aceptó, como runner_corpus.entrada_r2 (runner_corpus.py:1151-1185):
    extracciones_e1_compact.jsonl (last-wins, campo tool_input_crudo) si no hubo reintento o la unidad está en la cola;
    si hubo reintento, la fila (chunk_id, n_reintentos) de reintentos_e3.jsonl (leer_reintentos_companero,
    runner_corpus.py:1049-1058); si la fila no está en el compañero, el crudo está en e1_reintentos.db y acá se declara
    como no disponible (no se abre la base);
  - id del nodo de una entidad del crudo: la clave de fusión del ensamblado, e2_lib.entity_slug_r2 con fase r2b
    (e2_lib.py:845-871; el id es f"{type}_{slug}", e2_lib.py:1010), importada de la copia;
  - tramos de umbral de E1 de una entidad: su lista «umbrales» de tramos (el crudo). El ensamblado lee los
    umbrales_tramos que deja el validador (e2_lib.py:1013-1015); la ficha muestra lo que E1 devolvió, el crudo.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parents[5]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
KG = REX / "corpus_tanda0" / "ens_diez_r2b_sincola" / "r2" / "kg.json"
KG_SHA256 = "e22fae1afc3cf37fbe5b49ee0b220d51d0ec5febc13abeb6ebf7b74226da34fb"
E0 = REX / "e0_chunking" / "salida_tanda0_r2b"
SALIDA_R2B = REX / "corpus_tanda0" / "salida_r2b"
PDF_DEV = REPO / "data" / "experiment" / "subset"
PDF_NUEVOS = REPO / "data" / "experiment" / "escalado_prep" / "pdfs"
PYD = REPO / "data" / "experiment" / "pyd_r2" / "code"
E2 = REX / "e2_reduce"

ENMIENDA = "docs/enmienda1_preregistro_evaluacion_tripletas_2026-10-08_umbrales.md"
COMMIT_FIRMA = "a0f9815"
SHA_TEXTO_FIRMADO = "c77e92adface7f9fe7286c1019971fdedafc7af6afbafb7b185f87c38bf77e01"
SEMILLA_P = "51fbea50388e7481"   # printf 'U-MED-UMBRALES|P|<sha del texto firmado>' | shasum -a 256 | cut -c1-16

TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")  # orden del manifiesto
DEV = ("cap", "cla", "ext", "pro", "ric")
ESTRATOS = ("E-e1-sin", "E-e1-con", "E-desc-sin", "E-desc-con", "V-sin-cont", "V-con", "base resuelta", "V-vacío")
ESPERADO = {"E-e1-sin": 652, "E-e1-con": 76, "E-desc-sin": 88, "E-desc-con": 18, "V-sin-cont": 7, "V-con": 150,
            "base resuelta": 10, "V-vacío": 305}
ESPERADO_TOTAL, ESPERADO_CONTENIDO, ESPERADO_NUEVOS, ESPERADO_RESUELTAS = 1306, 1001, 143, 10

# Campos del elemento que la ficha del paso 1 nunca muestra (mandato P-a, punto 6; enmienda §5.2).
CAMPOS_OCULTOS = ("valor", "unidad", "moneda", "dias_tipo", "comparacion", "comparacion_asumida", "regla_comparacion",
                  "base", "base_destino", "base_via", "base_no_resuelta", "origen", "verificado_en_tabla",
                  "fuera_de_lista", "originales")


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def canon(x) -> bytes:
    return json.dumps(x, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def cargar_kg() -> tuple[dict, str]:
    b = KG.read_bytes()
    s = sha(b)
    if s != KG_SHA256:
        raise SystemExit(f"kg.json con sha256 {s}, no el sellado {KG_SHA256}")
    return json.loads(b), s


# ----------------------------------------------------------------------------------------------- marco y estratos
def es_validador(el: dict) -> bool:
    return str(el.get("regla_comparacion", "")).startswith("limite_relativo:")


def estrato(el: dict) -> str:
    """Regla del mandato P-a, punto 3, en este orden."""
    if es_validador(el):
        if el.get("valor") is None and el.get("base") is None and el.get("comparacion") == "no_determinada":
            return "V-vacío"
        if el.get("base") is not None:
            return "V-con"
        return "V-sin-cont"
    if el.get("base_via"):
        return "base resuelta"
    o = el.get("origen")
    if o == "e1":
        pref = "E-e1"
    elif o == "descripcion":
        pref = "E-desc"
    else:
        raise SystemExit(f"origen {o!r} fuera de lo previsto (e1, descripcion)")
    return f"{pref}-{'con' if el.get('base') is not None else 'sin'}"


def elementos(kg: dict):
    """(id, nodo, i, elemento) de cada elemento de umbral, con id «<id del nodo>#u<i>»."""
    for n in kg["nodes"]:
        for i, el in enumerate((n.get("properties") or {}).get("umbrales") or []):
            yield f"{n['id']}#u{i}", n, i, el


def marco(kg: dict) -> list[list]:
    """Filas [id, to, tipo del nodo, estrato], ordenadas por id."""
    filas = [[eid, n["provenance"].get("to"), n["type"], estrato(el)] for eid, n, _, el in elementos(kg)]
    filas.sort(key=lambda f: f[0])
    return filas


def indice_elementos(kg: dict) -> dict:
    return {eid: (n, i, el) for eid, n, i, el in elementos(kg)}


# --------------------------------------------------------------------------------------------- E0 y crudo de E1
def texto_completo(chunk: dict) -> str:
    """Igual a validador_r2.texto_completo (validador_r2.py:232-235)."""
    partes = [chunk.get("texto") or ""] + [h.get("texto") or "" for h in chunk.get("herencia") or []]
    return "\n".join(partes)


_CHUNKS: dict[str, dict] = {}


def chunks_to(to: str) -> dict[str, dict]:
    if to not in _CHUNKS:
        d = json.loads((E0 / f"chunks_{to}.json").read_text(encoding="utf-8"))
        lista = d["chunks"] if isinstance(d, dict) else d
        out = {c["id"]: c for c in lista}
        p = SALIDA_R2B / to / "particiones_por_corte.json"
        if p.exists():
            for cid, v in json.loads(p.read_text(encoding="utf-8")).items():
                for parte in v["partes"]:
                    out[parte["id"]] = parte
        _CHUNKS[to] = out
    return _CHUNKS[to]


def _jsonl_last_wins(p: Path, clave) -> dict:
    out = {}
    if p.exists():
        for x in p.read_text(encoding="utf-8").splitlines():
            if x.strip():
                r = json.loads(x)
                out[clave(r)] = r
    return out


_E1: dict[str, tuple] = {}


def _salida_to(to: str) -> tuple:
    if to not in _E1:
        d = SALIDA_R2B / to
        _E1[to] = (_jsonl_last_wins(d / "extracciones_e1_compact.jsonl", lambda r: r["chunk_id"]),
                   _jsonl_last_wins(d / "finales.jsonl", lambda r: r["chunk_id"]),
                   _jsonl_last_wins(d / "reintentos_e3.jsonl", lambda r: (r["chunk_id"], r["intento"])))
    return _E1[to]


def crudo_e1(to: str, cid: str) -> tuple[dict | None, str]:
    """(tool_input, fuente) del intento que E3 aceptó, con la regla de runner_corpus.entrada_r2."""
    regs, finales, comp = _salida_to(to)
    fin = finales.get(cid)
    if fin is not None:
        n = fin.get("n_reintentos") or 0
        cola = fin.get("validacion_final") is None
        if n and not cola:
            r = comp.get((cid, n))
            if r is None:
                return None, f"reintento_{n}: no está en reintentos_e3.jsonl (e1_reintentos.db, no se abre)"
            return r.get("tool_input"), f"reintento_{n}: reintentos_e3.jsonl"
    r = regs.get(cid)
    return ((r or {}).get("tool_input_crudo"), "extracciones_e1_compact.jsonl")


_E2LIB = None


def e2lib():
    global _E2LIB
    if _E2LIB is None:
        if str(E2) not in sys.path:
            sys.path.insert(0, str(E2))
        import e2_lib  # noqa: PLC0415 — de la copia, no del repo
        if Path(e2_lib.__file__).resolve().parents[4] != REPO:
            raise SystemExit(f"e2_lib importado de {e2_lib.__file__}, fuera de {REPO}")
        _E2LIB = e2_lib
    return _E2LIB


def rcmp():
    if str(PYD) not in sys.path:
        sys.path.insert(0, str(PYD))
    import reglas_comparacion as R  # noqa: PLC0415 — de la copia, no del repo
    if Path(R.__file__).resolve().parents[4] != REPO:
        raise SystemExit(f"reglas_comparacion importado de {R.__file__}, fuera de {REPO}")
    return R


def gid_entidad(e: dict, prov: dict) -> str:
    L = e2lib()
    return f"{e['type']}_{L.entity_slug_r2({'type': e['type'], 'label': e.get('label'), 'properties': e.get('properties') or {}}, prov, 'r2b')}"


def tramos_e1_nodo(n: dict) -> dict:
    """Tramos de umbral que E1 devolvió para el nodo: los de las entidades del crudo de cada procedencia cuyo id de
    fusión es el del nodo. Devuelve {'tramos': [(chunk_id, tramo)], 'fuentes': {chunk_id: fuente}, 'entidades': k}."""
    out, fuentes, k = [], {}, 0
    for p in n.get("provenances") or [n["provenance"]]:
        cid, to = p.get("chunk_id"), p.get("to")
        if not cid or cid in fuentes:
            continue
        ti, fuente = crudo_e1(to, cid)
        fuentes[cid] = fuente
        for e in (ti or {}).get("entities") or []:
            if e.get("type") != n["type"]:
                continue
            prov = {"to": to, "archivo": p.get("archivo"), "punto": e.get("punto") or p.get("punto")}
            if gid_entidad(e, prov) != n["id"]:
                continue
            k += 1
            for u in e.get("umbrales") or []:
                t = u.get("tramo") if isinstance(u, dict) else u
                if isinstance(t, str) and t.strip() and (cid, t) not in out:
                    out.append((cid, t))
    return {"tramos": out, "fuentes": fuentes, "entidades": k}


# ----------------------------------------------------------------------------------- ubicar un tramo en el texto
def plegar(s: str) -> str:
    """Minúsculas y sin diacríticos, carácter por carácter (mismo largo; igual criterio que reglas_comparacion.plegar)."""
    out = []
    for c in s:
        d = unicodedata.normalize("NFKD", c)
        b = "".join(x for x in d if not unicodedata.combining(x)).lower()
        out.append(b if len(b) == 1 else (c.lower()[:1] or c))
    return "".join(out)


_VAL = None


def validador():
    """validador_r2 de la copia: sus tokens de R-NORM son los que usa el ensamblado para verificar un tramo."""
    global _VAL
    if _VAL is None:
        if str(PYD) not in sys.path:
            sys.path.insert(0, str(PYD))
        import validador_r2 as V  # noqa: PLC0415 — de la copia, no del repo
        if Path(V.__file__).resolve().parents[4] != REPO:
            raise SystemExit(f"validador_r2 importado de {V.__file__}, fuera de {REPO}")
        _VAL = V
    return _VAL


def ocurrencias(texto: str, tramo: str) -> list[tuple[int, int]]:
    """Posiciones de `tramo` en `texto` con el nivel «exacta» de validador_r2.verificar_tramo (validador_r2.py:209-223):
    la secuencia de tokens de R-NORM del tramo, contigua en el texto. Devuelve el span en caracteres del texto."""
    V = validador()
    at = V.norm_tokens(tramo)
    if not at:
        return []
    tt = V.tokens_con_spans(texto)
    ts = [t for t, _, _ in tt]
    n = len(at)
    return [(tt[i][1], tt[i + n - 1][2]) for i in range(len(ts) - n + 1) if ts[i:i + n] == at]


def ventana_tokens(texto: str, tramo: str) -> tuple[int, int] | None:
    """Nivel «tokens» de verificar_tramo (validador_r2.py:224-229): la ventana mínima que contiene todos los tokens
    distintos del tramo, solo si no pasa del doble de esos tokens (tope propio de la ficha, declarado)."""
    V = validador()
    at = V.norm_tokens(tramo)
    tt = V.tokens_con_spans(texto)
    v = V._ventana_minima([t for t, _, _ in tt], set(at))
    if v is None or v[1] - v[0] > 2 * len(set(at)):
        return None
    return tt[v[0]][1], tt[v[1] - 1][2]


# Regla de corte de la cláusula (mandato P-a, punto 5): salto de línea, punto y coma, o punto seguido de espacio y de
# una mayúscula, un dígito de un nuevo punto o el fin del texto. El punto de una cifra («3.7.») o de una abreviatura
# seguido de minúscula no corta.
_RE_CORTE = re.compile(r"\n|;|\.(?=\s+(?:[A-ZÁÉÍÓÚÑ¿«(\"]|\d+\.\d)|\s*$)")


def clausula(texto: str, ini: int, fin: int) -> tuple[int, int]:
    a = 0
    for m in _RE_CORTE.finditer(texto, 0, ini):
        a = m.end()
    m = _RE_CORTE.search(texto, fin)
    b = m.start() + (1 if m and m.group() == "." else 0) if m else len(texto)
    return a, b


# ------------------------------------------------------------------------------------ ubicar un elemento en E0
_RE_SEPARADOR = re.compile(r"\s*\[\s*(?:…|\.\.\.)\s*\]\s*")   # validador_r2._RE_SEPARADOR_TRAMO (validador_r2.py:247)


def textos_nodo(n: dict) -> list[tuple[str, str, dict]]:
    """(chunk_id, texto completo, chunk) de cada procedencia del nodo, sin repetir."""
    out, vistos = [], set()
    for p in n.get("provenances") or [n["provenance"]]:
        cid, to = p.get("chunk_id"), p.get("to")
        ch = chunks_to(to).get(cid) if cid else None
        if ch is not None and cid not in vistos:
            vistos.add(cid)
            out.append((cid, texto_completo(ch), ch))
    return out


def _norm(s: str) -> str:
    return " ".join(plegar(s).split())


def _alinear_e1(n: dict, kg_elementos: list[dict], tramos: list[tuple[str, str]]) -> dict[int, tuple[int, int]]:
    """Índice del elemento → (índice del tramo de E1, ocurrencia de su cuantía dentro del tramo). El ensamblado arma
    los elementos de origen e1 recorriendo los tramos en orden y, en cada uno, las cuantías de
    reglas_comparacion.detectar_cuantias (ensamblar_tanda0.py:745-764); se alinea en el mismo orden."""
    R = rcmp()
    secuencia = []
    for j, (_, t) in enumerate(tramos):
        vistos: dict[str, int] = {}
        for c in R.detectar_cuantias(t):
            k = _norm(c.texto)
            secuencia.append((k, j, vistos.get(k, 0)))
            vistos[k] = vistos.get(k, 0) + 1
    out, pos = {}, 0
    for i, el in enumerate(kg_elementos):
        if es_validador(el) or el.get("origen") != "e1":
            continue
        k = _norm(el.get("tramo") or "")
        for q in range(pos, len(secuencia)):
            if secuencia[q][0] == k:
                out[i] = (secuencia[q][1], secuencia[q][2])
                pos = q + 1
                break
    return out


def ubicar(n: dict, i: int, el: dict) -> dict:
    """Dónde está el elemento en el texto de E0 de su nodo: {'chunk_id', 'spans' (en el texto completo), 'metodo',
    'nota', 'tramos_e1', 'tramo_e1_del_elemento'}. Nunca devuelve campos del umbral."""
    textos = textos_nodo(n)
    info = tramos_e1_nodo(n)
    out = {"chunk_id": None, "spans": [], "metodo": None, "nota": None, "tramos_e1": info["tramos"],
           "fuentes_e1": info["fuentes"], "tramo_e1_del_elemento": None}

    def buscar(tramo: str, ventana: bool = False):
        for cid, txt, _ in textos:
            occ = ocurrencias(txt, tramo)
            if occ:
                return cid, occ
        if ventana:
            for cid, txt, _ in textos:
                v = ventana_tokens(txt, tramo)
                if v:
                    out["nota_tokens"] = "ubicado por ventana de tokens (nivel «tokens»), no literal"
                    return cid, [v]
        return None, []

    if es_validador(el):
        segs = [s for s in _RE_SEPARADOR.split(el.get("tramo") or "") if s.strip()]
        for s in segs:
            cid, occ = buscar(s, ventana=True)
            if occ and (out["chunk_id"] in (None, cid)):
                out["chunk_id"] = cid
                out["spans"].append(occ[0])
        out["metodo"] = "tramo_del_elemento (validador)"
        out["tramo_e1_del_elemento"] = el.get("tramo")
        if len(out["spans"]) < len(segs):
            out["nota"] = f"{len(segs) - len(out['spans'])} de {len(segs)} segmentos del tramo no se ubican en E0"
        return out

    cuantia = el.get("tramo") or ""
    if el.get("origen") == "e1" and info["tramos"]:
        lst = (n.get("properties") or {}).get("umbrales") or []
        al = _alinear_e1(n, lst, info["tramos"]).get(i)
        if al is not None:
            j, q = al
            cid_t, t = info["tramos"][j]
            out["tramo_e1_del_elemento"] = t
            for s in [s for s in _RE_SEPARADOR.split(t) if s.strip()]:
                cid, occ = buscar(s, ventana=True)
                for a, b in occ:
                    txt = next(x for c, x, _ in textos if c == cid)
                    dentro = [(a + x, a + y) for x, y in ocurrencias(txt[a:b], cuantia)]
                    if len(dentro) > q:
                        out.update(chunk_id=cid, spans=[dentro[q]], metodo="cuantia_dentro_del_tramo_de_e1")
                        return out
                    q -= len(dentro)
                    if q < 0:
                        break
            out["nota"] = "el tramo de E1 del elemento no se ubica en E0; se busca la cuantía sola"
    cid, occ = buscar(cuantia)
    if occ:
        out.update(chunk_id=cid, spans=occ, metodo=("cuantia_desde_descripcion" if el.get("origen") == "descripcion"
                                                   else "cuantia_sola"))
        if len(occ) > 1:
            out["nota"] = ((out["nota"] + "; ") if out["nota"] else "") + f"la cuantía aparece {len(occ)} veces en el texto"
    else:
        out["metodo"] = "no_ubicada"
        out["nota"] = ((out["nota"] + "; ") if out["nota"] else "") + "la cuantía no se encuentra en el texto de E0"
    return out
