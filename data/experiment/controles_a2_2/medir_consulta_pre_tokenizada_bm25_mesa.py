"""Mesa, 16/10/2026: qué términos del índice BM25 del sistema por fragmentos no puede alcanzar una consulta pre-tokenizada como la del
brazo del grafo (harness._tokens: minúsculas, sin acentos, [a-z0-9]+; neo4j_index.py:121-128 y :169-170), y qué palabras vacías con tilde
dejan de serlo. Sostiene la decisión de la autora del 16/10/2026: la consulta del BM25 queda simétrica, con el mismo analizador en las dos
puntas, y la asimetría con el grafo se declara en el pre-registro de A2.2 con estas cifras.
Corre sobre copias del módulo y del índice, y controla sus sha256:
  python3 -I -B medir_consulta_pre_tokenizada_bm25_mesa.py <carpeta con una copia de bm25_fragmentos.py> <copia de indice_bm25.json> <salida.json>
El índice está fuera de git (data/experiment/banco_mcp/mcp_vector/indice/e0_r2b_desarrollo_bm25/indice_bm25.json); su sha256 lo declara
config_fragmentos_bm25_r2b.json."""
import hashlib, json, re, sys, unicodedata
from pathlib import Path
SHA_INDICE = "6b5da8b0940e6ae46214b93c541b384a710eb35688264c0138df2e7b4773fc25"
mod, ind_p, out = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
h = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert h(ind_p) == SHA_INDICE, "el índice no es el sellado en la config"
sys.path.insert(0, str(mod))
import bm25_fragmentos as b  # noqa: E402
ind = json.loads(ind_p.read_text(encoding="utf-8"))
df, ids, tf = ind["df"], ind["ids"], ind["tf"]
TOK = re.compile(r"[a-z0-9]+")
def strip(s): return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))
def pre(s): return TOK.findall(strip((s or "").lower()))
alc = lambda t: re.fullmatch(r"[a-z0-9]+", t) is not None
inal = sorted((t for t in df if not alc(t)), key=lambda t: (-df[t], t))
con_tilde = [t for t in inal if re.search(r"[^\x00-\x7f]", t)]
con_sep = [t for t in inal if not re.search(r"[^\x00-\x7f]", t)]
res = {"sha256_indice": SHA_INDICE, "sha256_bm25_fragmentos_py": h(mod / "bm25_fragmentos.py"),
       "vocabulario": len(df), "terminos_inalcanzables": len(inal), "de_ellos_con_caracteres_no_ascii": len(con_tilde),
       "de_ellos_ascii_con_separadores": len(con_sep), "pasajes": len(ids),
       "pasajes_con_algun_termino_inalcanzable": sum(1 for terms in tf if any(not alc(t) for t, _ in terms)),
       "ocurrencias_inalcanzables": sum(f for terms in tf for t, f in terms if not alc(t)), "ocurrencias_totales": ind["sum_total_term_freq"],
       "top20_no_ascii_por_df": [[t, df[t]] for t in con_tilde[:20]], "top10_separadores_por_df": [[t, df[t]] for t in con_sep[:10]],
       "palabras_vacias_con_tilde": sorted(w for w in b.STOP if re.search(r"[^\x00-\x7f]", w)),
       "ejemplos": {w: {"simetrica": b.analizar(w), "pre_tokenizada": b.analizar(" ".join(pre(w)))}
                    for w in ["días", "año", "años", "más", "según", "período", "1.234,56", "3.16", "crédito", "BCRA"]}}
out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print({k: v for k, v in res.items() if not isinstance(v, (list, dict))})
