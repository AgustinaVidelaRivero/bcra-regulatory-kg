"""Medición por sección de un documento con rol de alcance, para el pre-registro de la tanda 1 (mesa, 15/10/2026; depaho y snp_tr).

Por sección de primer nivel: las unidades, y en cuántas el texto propio o heredado nombra otro Sujeto con el criterio de B′. Solo cuentas
e ids de Sujeto; no imprime texto de unidades.
Criterio de B′ (mandato U-APLICA-ROL-ALCANCE, «LA REGLA» y decisión 1): el texto propio de la unidad más el heredado, normalizado
como r1_comun.norm; una clave del índice de E4 (generados_r2/indice_e4_r2.json) de criterio label_exacto, alias_exacto o
label_singularizado, no ambigua, como palabra entera (\b); «otro» = distinto del destino; la raíz Sujeto_sujeto no cuenta; los
miembros del rol cuentan como otro sujeto. Es una cota por unidad: B′ actúa sobre normas sin aplica_a, que salen de E1.
La E0 es la corregida: el archivo de chunks tiene que tener el sha256 que le da el manifiesto de S0-6b
(segmentacion_oficial_e0r2/s0_6/b/manifiestos/manifest_salida_e0_152_S0-6b.json); la salida guarda el sha256 de cada entrada.
Corre sobre una copia (CLAUDE.md §4.l): <copia del repo> es una copia, o una extracción con git archive de los tres archivos que lee.
Uso: python3 -I -B medir_por_seccion_Bprima_mesa.py <chunks_<to>.json> <copia del repo> <salida.json> <to> <destino>
"""
import json, re, sys
from collections import Counter, OrderedDict
from pathlib import Path

chunks, copia, salida = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
sys.path.insert(0, str(copia / "data/experiment/reextraccion_v2/corpus_v2"))
import r1_comun as C  # noqa: E402

TO, DESTINO = sys.argv[4], sys.argv[5]
RAIZ = "Sujeto_sujeto"
CRIT = ("label_exacto", "alias_exacto", "label_singularizado")
ind = json.loads((copia / "data/experiment/catalogo_unico/generados_r2/indice_e4_r2.json").read_text(encoding="utf-8"))
claves = sorted({(k, i) for crit, k, i in ind if crit in CRIT and k and i != "__AMBIGUO__"}, key=lambda x: (-len(x[0]), x[0]))
pats = [(re.compile(r"\b" + re.escape(k) + r"\b"), i) for k, i in claves]
rol = json.loads((copia / "data/experiment/catalogo_unico/generados_r2/rol_por_to_r2.json").read_text(encoding="utf-8"))[TO + ".pdf"] if TO + ".pdf" in json.loads((copia / "data/experiment/catalogo_unico/generados_r2/rol_por_to_r2.json").read_text(encoding="utf-8")) else {"rol_id": DESTINO, "miembros_labels": []}

def seccion(u: str) -> str:
    m = re.match(r"^S?(\d+)", u)
    return m.group(1) if m else "bloques"

def subseccion(u: str) -> str:
    p = u.split(".")
    return ".".join(p[:2]) if len(p) >= 2 else u

cs = json.loads(chunks.read_text(encoding="utf-8"))
por_sec, nombra_sec, sub3, nombra_sub3, ids_sec = Counter(), Counter(), Counter(), Counter(), {}
tipos = Counter()
for c in cs:
    u = c["unidad"]; s = seccion(u); tipos[c["tipo"]] += 1
    texto = C.norm(" ".join([c.get("texto") or ""] + [h.get("texto") or "" for h in c.get("herencia") or []]))
    otros = {i for p, i in pats if i not in (DESTINO, RAIZ) and p.search(texto)}
    por_sec[s] += 1
    if otros:
        nombra_sec[s] += 1
        ids_sec.setdefault(s, Counter()).update(otros)
    if s == "3":
        sub3[subseccion(u)] += 1
        if otros:
            nombra_sub3[subseccion(u)] += 1
orden = lambda c: OrderedDict(sorted(c.items(), key=lambda kv: [int(x) if x.isdigit() else 999 for x in kv[0].split(".")]))  # noqa: E731
import hashlib  # noqa: E402
_sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()  # noqa: E731
out = OrderedDict([
    ("fuente_chunks", str(chunks.name)),
    ("entradas_sha256", OrderedDict([("chunks", _sha(chunks)),
        ("indice_e4_r2.json", _sha(copia / "data/experiment/catalogo_unico/generados_r2/indice_e4_r2.json")),
        ("rol_por_to_r2.json", _sha(copia / "data/experiment/catalogo_unico/generados_r2/rol_por_to_r2.json")),
        ("r1_comun.py", _sha(copia / "data/experiment/reextraccion_v2/corpus_v2/r1_comun.py"))])),
    ("destino", DESTINO), ("unidades", len(cs)), ("tipos", dict(tipos)),
    ("rol_de_la_release", OrderedDict([("rol_id", rol["rol_id"]), ("miembros_labels", rol["miembros_labels"])])),
    ("unidades_por_seccion", orden(por_sec)),
    ("nombran_otro_sujeto_por_seccion", orden(nombra_sec)),
    ("no_nombran_otro_sujeto_por_seccion", orden(Counter({k: por_sec[k] - nombra_sec[k] for k in por_sec}))),
    ("seccion_3_unidades_por_subseccion", orden(sub3)),
    ("seccion_3_nombran_otro_sujeto_por_subseccion", orden(nombra_sub3)),
    ("seccion_3_no_nombran_por_subseccion", orden(Counter({k: sub3[k] - nombra_sub3[k] for k in sub3}))),
    ("sujetos_que_bloquean_por_seccion", OrderedDict((k, sorted(ids_sec[k].items(), key=lambda kv: (-kv[1], kv[0]))[:8]) for k in sorted(ids_sec))),
])
# Quién abre las cuentas en cada subsección de la 3, según su unidad de apertura (leída por la mesa: título y comienzo).
GRUPOS = OrderedDict([
    ("bancos comerciales de primer grado (3.1.1, p. 21; 3.5.1, p. 35)", ["3.1", "3.5"]),
    ("entidades financieras (3.2.1, p. 26; 3.4.1, p. 28; 3.6.1, p. 38; 3.8.1, p. 43; 3.9.1, p. 47; bloques de 3.11, 3.12 y 3.13, pp. 51, 54 y 57)",
     ["3.2", "3.4", "3.6", "3.8", "3.9", "3.11", "3.12", "3.13"]),
    ("entidades financieras del Grupo A (bloques de 3.14 y 3.15, pp. 59 y 60)", ["3.14", "3.15"]),
    ("sin entidad nombrada en la apertura (3.3, 3.7, 3.10, 3.16 y 3.17)", ["3.3", "3.7", "3.10", "3.16", "3.17"]),
])
if TO == "depaho":
  out["seccion_3_por_quien_abre"] = OrderedDict(
    (g, OrderedDict([("subsecciones", subs), ("unidades", sum(sub3[x] for x in subs)),
                     ("no_nombran_otro_sujeto", sum(sub3[x] - nombra_sub3[x] for x in subs))])) for g, subs in GRUPOS.items())
  assert sum(v["unidades"] for v in out["seccion_3_por_quien_abre"].values()) == por_sec["3"]
salida.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps({k: out[k] for k in ("unidades", "unidades_por_seccion", "nombran_otro_sujeto_por_seccion", "no_nombran_otro_sujeto_por_seccion")}, ensure_ascii=False))
print(json.dumps({k: out[k] for k in ("seccion_3_unidades_por_subseccion", "seccion_3_no_nombran_por_subseccion")}, ensure_ascii=False))
print(json.dumps(out["sujetos_que_bloquean_por_seccion"], ensure_ascii=False))
print(json.dumps(out.get("seccion_3_por_quien_abre"), ensure_ascii=False))
