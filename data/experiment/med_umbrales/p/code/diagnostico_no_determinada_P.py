"""
diagnostico_no_determinada_P.py — U-MED-UMBRALES, etapa P, tramo P-a, punto 5 (§9.2 bis de la enmienda): diagnóstico
determinístico de la comparación `no_determinada` en los elementos con contenido. Sin lectura, sin veredicto y sin cifra:
propone candidatos a clase del §10.1; la clase la deciden la lectura y la autora.

  - Población: elementos de umbral que no son V-vacío y tienen comparacion == no_determinada.
  - Cláusula de cada elemento: la oración del texto completo de su unidad de E0 (propio y heredado, unidos por salto)
    que contiene la cuantía ubicada (comun_P.ubicar, con el span ajustado por texto_P.ajustar_cuantia), cortada con la
    regla de texto_P.clausula (punto y coma; punto seguido de espacio y de mayúscula, número de punto o fin; salto de
    línea solo si abre un ítem, si sigue a dos puntos o si une bloques), y mostrada con los cortes de renglón unidos
    (texto_P.para_mostrar). Si la cuantía aparece más de una vez (elementos de la descripción), se toma la primera y
    se marca.
  - Censo léxico sobre la cláusula plegada (minúsculas, sin tildes), en tres familias con precedencia (i) > (ii) > (iii):
      (i) un marcador de la tabla del §2.4 firmado (FORMAS_TABLA): candidato *de implementación*;
      (ii) una forma fuera de la tabla (FORMAS_FUERA, listadas con su conteo): candidato *de la definición*;
      (iii) ningún marcador: la no_determinada probablemente es correcta (enmienda 3 a L-ESQ-R2 en los plazos).
  - Para (i), por qué la rama de reglas_comparacion.py no tomó el marcador, sobre el texto que leyó la regla (el tramo de
    E1 del elemento o, si E1 no dio tramo, la descripción del nodo: ensamblar_tanda0.py:723-727 y :748):
      marcador_fuera_del_texto_leido; limite_de_clausula_en_medio (:343-355; la ventana no cruza la cláusula,
      :699-700); otra_cuantia_en_medio (:512 y :516, la ventana no cruza otra cuantía, :701-702);
      fuera_de_la_ventana_antes (:110 y :512-515, 10 palabras); fuera_de_la_ventana_despues (:111 y :516-519, 3
      palabras); forma_no_reconocida_por_las_reglas (el resto, a revisar contra SIMPLES/COMPUESTAS/ADYACENCIA, :367-403).
    Y un contraste: reglas_comparacion.analizar sobre la cláusula de E0 completa, para ver si con ese texto la regla
    fija un sentido para la misma cuantía.
  - A ciegas: los elementos de la muestra (acta_sorteo_P.json) y los que daría la regla del lote 3 entran solo a los
    agregados. Los ids del lote 3 se calculan en memoria, con la regla escrita en el acta, solo para dejarlos fuera del
    listado por elemento; no se escriben en ningún archivo.

Corre desde la raíz de la copia del repo y escribe solo en --salida.
  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/med_umbrales/p/code/diagnostico_no_determinada_P.py \
      --acta <acta_sorteo_P.json> --salida DIR
"""
from __future__ import annotations

import argparse
import json
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun_P as C  # noqa: E402
import texto_P as T  # noqa: E402

# (i) La tabla del §2.4 de la enmienda firmada (a0f9815), con la negación general de L-ESQ-R2 §1.3 («no» o «sin»
# delante de una simple, que la tabla trae como «no podrá superar», «sin exceder», «no inferior a»…). Sobre texto plegado.
FORMAS_TABLA = (
    ("super-/exced- (minimo_estricto; negado, maximo_inclusivo)", r"\bsuper(?!intend|vis|fic|avit)\w*|\bexced(?!ente)\w*"),
    ("mas de / mas del", r"\bmas del?\b"),
    ("mayor(es) a / al", r"\bmayor(?:es)? al?\b"),
    ("igual o superior / mayor / inferior / menor", r"\biguale?s? o (?:superior|mayor|inferior|menor)(?:es)?\b"),
    ("al menos / por lo menos", r"\bal menos\b|\bpor lo menos\b"),
    ("como minimo / un minimo de", r"\bcomo minim[oa]\b|\bun minimo de\b"),
    ("no inferior / no menos de", r"\bno inferior(?:es)?\b|\bno menos de\b"),
    ("o mas / o menos pospuesto", r"\bo (?:mas|menos)\b"),
    ("inferior(es) a / al", r"\binferior(?:es)? al?\b"),
    ("menos de / menos del", r"\bmenos del?\b"),
    ("menor(es) a / al", r"\bmenor(?:es)? al?\b"),
    ("hasta", r"\bhasta\b"),
    ("como maximo", r"\bcomo maxim[oa]\b"),
    ("dentro de", r"\bdentro del?\b"),
    ("igual a / equivalente a", r"\b(?:iguale?s?|equivalentes?) al?\b"),
    ("pondera / ponderador / coeficiente / factor", r"\bponder\w*|\bcoeficientes?\b|\bfactor(?:es)?\b"),
)
# «máximo»/«mínimo» pegados a la cuantía (con o sin «de»/«del»): de la tabla; no pegados, de FORMAS_FUERA.
ADYACENTE = re.compile(r"\b(?:maxim|minim)[oa]s?\s+(?:de\s+|del\s+)?$")
# (ii) Formas fuera de la tabla, las tres del mandato y las que aparecieron en el censo.
FORMAS_FUERA = (
    ("entre … y …", r"\bentre\b[^;\n]{0,60}?\d[^;\n]{0,60}?\by\b"),
    ("sera(n) de", r"\bser(?:a|an)\s+del?\b"),
    ("limite(s)", r"\blimites?\b"),
    ("tope(s)", r"\btopes?\b"),
    ("maximo / minimo no pegado a la cuantia", r"\bmaxim[oa]s?\b|\bminim[oa]s?\b"),
    ("mayor de / menor de (la calibracion P3 pide «a» o «al»)", r"\b(?:mayor|menor)(?:es)? del?\b"),
    ("a mas tardar", r"\ba mas tardar\b"),
    ("antes de", r"\bantes del?\b"),
    ("a partir de / luego de / despues de / transcurrido", r"\ba partir del?\b|\bluego del?\b|\bdespues del?\b|\btranscurrid\w*"),
    ("periodo de referencia (ultimos, anteriores, previos, siguientes, subsiguientes)",
     r"\bultim[oa]s\b|\banteriores\b|\bprevios\b|\bsiguientes\b|\bsubsiguientes\b"),
)
CAUSAS = ("marcador_fuera_del_texto_leido", "limite_de_clausula_en_medio", "otra_cuantia_en_medio",
          "fuera_de_la_ventana_antes", "fuera_de_la_ventana_despues", "forma_no_reconocida_por_las_reglas",
          "no_reproducida")


def marcadores(cl: str, antes_de_cuantia: str) -> tuple[list, list]:
    tabla = [n for n, p in FORMAS_TABLA if re.search(p, cl)]
    if ADYACENTE.search(antes_de_cuantia):
        tabla.append("maximo / minimo pegado a la cuantia")
    fuera = [n for n, p in FORMAS_FUERA if re.search(p, cl)]
    if "maximo / minimo pegado a la cuantia" in tabla and "maximo / minimo no pegado a la cuantia" in fuera:
        fuera.remove("maximo / minimo no pegado a la cuantia")
    return tabla, fuera


def reservados_lote3(acta: dict, filas: list) -> set[str]:
    """Los ids que daría la regla del lote 3 escrita en el acta, solo en memoria."""
    S = acta["semilla"]["P"]
    sorteados = set(acta["sorteo"]["lote1"]) | set(acta["sorteo"]["lote2"])
    out = set()
    for e in C.ESTRATOS:
        resto = sorted(f[0] for f in filas if f[3] == e and f[0] not in sorteados)
        out |= set(random.Random(f"{S}:{e}:lote3").sample(resto, min(2, len(resto))))
    resto_n = sorted(f[0] for f in filas if f[1] not in C.DEV and f[0] not in sorteados | out)
    out |= set(random.Random(f"{S}:TOs nuevos:lote3").sample(resto_n, min(4, len(resto_n))))
    return out


def causa_codigo(R, fuente: str, cuantia_el: str, desc, titulo) -> dict:
    """Por qué la regla no tomó un marcador de la tabla, sobre el texto que leyó."""
    cs = R.analizar(fuente, desc, titulo, "no_determinada")
    k = C._norm(cuantia_el)
    c = next((x for x in cs if C._norm(x.texto) == k), None)
    if c is None or c.comparacion != "no_determinada":
        return {"causa": "no_reproducida", "detalle": "la cuantía no sale no_determinada al re-analizar el texto leído "
                                                      "(el ensamblado leyó el tramo validado, que puede diferir del crudo)"}
    pleg = C.plegar(fuente)
    pos = []
    for n, p in FORMAS_TABLA:
        pos += [(m.start(), m.end(), n) for m in re.finditer(p, pleg)]
    if ADYACENTE.search(pleg[:c.inicio]):
        m = ADYACENTE.search(pleg[:c.inicio])
        pos.append((m.start(), m.end(), "maximo / minimo pegado a la cuantia"))
    if not pos:
        return {"causa": "marcador_fuera_del_texto_leido"}
    pos.sort(key=lambda x: min(abs(x[0] - c.fin), abs(c.inicio - x[1])))
    a, b, nombre = pos[0]
    lims = R.limites_de_clausula(fuente)
    lo, hi = (b, c.inicio) if b <= c.inicio else (c.fin, a)
    if any(lo <= p < hi for p in lims):
        return {"causa": "limite_de_clausula_en_medio", "marcador": nombre}
    if any(x is not c and lo <= x.inicio < hi for x in cs):
        return {"causa": "otra_cuantia_en_medio", "marcador": nombre}
    if b <= c.inicio:
        if len(R._palabras(fuente[a:c.inicio])) > R.VENTANA_ANTES:
            return {"causa": "fuera_de_la_ventana_antes", "marcador": nombre,
                    "palabras": len(R._palabras(fuente[a:c.inicio]))}
    elif len(R._palabras(fuente[c.fin:b])) > R.VENTANA_DESPUES:
        return {"causa": "fuera_de_la_ventana_despues", "marcador": nombre, "palabras": len(R._palabras(fuente[c.fin:b]))}
    return {"causa": "forma_no_reconocida_por_las_reglas", "marcador": nombre, "forma": fuente[a:b]}


def _tabla(d: dict, columnas=("i", "ii", "iii", "sin_clausula")) -> list[str]:
    filas = ["| | " + " | ".join(columnas) + " | total |", "|---|" + "---:|" * (len(columnas) + 1)]
    for k, v in d.items():
        filas.append(f"| {k} | " + " | ".join(str(v.get(c, 0)) for c in columnas) + f" | {sum(v.values())} |")
    return filas


def escribir_md(out: dict, ruta: Path) -> None:
    """El informe del diagnóstico, generado desde el JSON (CLAUDE.md §4.i: ninguna cifra se transcribe a mano)."""
    P = out["poblacion"]
    els = out["elementos_fuera_de_la_muestra"]

    def ejemplos(cond, n=2):
        return [r for r in els if cond(r)][:n]

    def linea(r):
        cl, cu = r.get("clausula", ""), r.get("cuantia", "")
        k = cl.find(cu)
        a, b = (max(0, k - 160), min(len(cl), k + len(cu) + 90)) if k >= 0 else (0, 250)
        trozo = ("…" if a > 0 else "") + cl[a:b] + ("…" if b < len(cl) else "")
        return f"  - `{r['id']}` ({r['to']}, {r['estrato']}, {r['unidad']}): cuantía «{cu}»; cláusula: «{trozo}»"

    L = ["# Diagnóstico de la comparación `no_determinada` (U-MED-UMBRALES, etapa P, tramo P-a, punto 5)", "",
         "Determinístico, sin lectura, sin veredicto y sin cifra para la tesis: propone candidatos a clase del §10.1 de la "
         "enmienda (FIRMADA en `a0f9815`). La clase la deciden la lectura del piloto y la autora. Generado por "
         "`code/diagnostico_no_determinada_P.py` desde `diagnostico_no_determinada_P.json`.", "",
         f"Acta: `{out['acta']['ruta']}` (sha256 `{out['acta']['sha256'][:16]}…`). Grafo `{out['grafo_sha256'][:16]}…`.",
         "", "## 1. Población", "",
         f"{P['N']} elementos con contenido y `no_determinada`, todos del {', '.join(P['por_autor'])} "
         f"({P['por_autor']}). Los 305 vacíos van aparte (§2.5).", "",
         f"- por regla: {P['por_regla']}",
         f"- por estrato: {P['por_estrato']}",
         f"- por unidad: {P['por_unidad']}",
         f"- por TO: {P['por_to']}",
         f"- cómo se ubicó la cuantía en E0: {P['por_ubicacion']}", "",
         f"Regla de corte de la cláusula: {out['regla_de_corte']}. Largo de la cláusula en caracteres: "
         f"{out['largo_clausula']}.", "",
         "## 2. Familias del censo léxico sobre la cláusula", "",
         f"Por familia: {out['por_familia']}. Precedencia {out['familias']['precedencia']}.", "",
         "- (i) un marcador de la tabla del §2.4 firmado: candidato *de implementación*;",
         "- (ii) una forma fuera de la tabla: candidato *de la definición*;",
         "- (iii) ningún marcador: la `no_determinada` probablemente es correcta (en los plazos, enmienda 3 a L-ESQ-R2);",
         "- sin_clausula: la cuantía no se ubica en el texto de E0 de la unidad.", "",
         "El censo es léxico: un marcador de la cláusula puede ser de otra cuantía de la misma oración, y una forma de "
         "(ii) puede no tener que ver con la cuantía. Por eso ninguna familia es un veredicto.", "",
         "### Por estrato", ""] + _tabla(out["familia_por_estrato"]) + ["", "### Por unidad", ""] + \
        _tabla(out["familia_por_unidad"]) + ["", "### Por regla", ""] + _tabla(out["familia_por_regla"]) + \
        ["", "### Por TO", ""] + _tabla(out["familia_por_to"]) + ["", "### Por origen del elemento", ""] + \
        _tabla(out["familia_por_origen"]) + [
         "", "## 3. Familia (i): marcadores y por qué la regla no los tomó", "",
         f"Marcadores de la tabla en la cláusula: {out['marcadores_i']}.", "",
         f"Causa, sobre el texto que leyó la regla: {out['causas_i']}.", "",
         f"- por texto leído: {out['causas_i_por_texto_leido']}",
         f"- contra el contraste con la cláusula de E0 completa: {out['causas_i_por_contraste']}", "",
         "Anclas de cada causa en `data/experiment/pyd_r2/code/reglas_comparacion.py` (HEAD `2a70b20`):",
         "- el texto que lee la regla es el tramo de E1 del nodo o, si E1 no dio tramo, la descripción "
         "(`data/experiment/tanda0/code/ensamblar_tanda0.py:723-727` y `:748`);",
         "- `marcador_fuera_del_texto_leido`: el marcador está en la cláusula de E0 y no en ese texto;",
         "- `limite_de_clausula_en_medio`: `:343-355` (límites «;», «:» y punto) y `:699-700` (la ventana no cruza la "
         "cláusula);",
         "- `otra_cuantia_en_medio`: `:512` y `:516` (la ventana no cruza la cuantía anterior ni la siguiente), con "
         "`:701-702`;",
         "- `fuera_de_la_ventana_antes` y `_despues`: `:110-111` (10 y 3 palabras) y `:512-519`;",
         "- `forma_no_reconocida_por_las_reglas`: el marcador está dentro de la ventana y la regla no lo toma (formas "
         "de `SIMPLES`, `COMPUESTAS` y `ADYACENCIA`, `:367-403`), a revisar caso por caso;",
         "- sin marcador, `no_determinada`: `:224-225` (valores por defecto de `Cuantia`) y `:612-618` (rama 6, "
         "enmienda 3).", "",
         f"Contraste (reglas_comparacion.analizar sobre la cláusula de E0 completa): {out['contraste_clausula_completa']}.", "",
         "## 4. Familia (ii): formas fuera de la tabla", "",
         f"En la familia (ii): {out['formas_ii']}.", "",
         f"En todas las cláusulas (también en las de (i)): {out['formas_fuera_en_todas']}.", "",
         "## 5. Candidatos a clase del §10.1 (sin veredicto)", ""]
    det = out["causas_i_por_contraste"].get("marcador_fuera_del_texto_leido", {})
    L += [f"1. **El texto que leyó la regla no trae el marcador que la cláusula sí trae** (causa "
          f"`marcador_fuera_del_texto_leido`: {out['causas_i'].get('marcador_fuera_del_texto_leido', 0)}; con la "
          f"cláusula completa la regla fija un sentido en {det.get('determina', 0)}). Si la lectura lo confirma, la "
          f"causa está en E1 (el tramo recorta el marcador) o en la descripción; el §10.2 la manda al backlog salvo que "
          f"la autora decida que la regla lea la cláusula de E0, lo que cambia la definición (L-ESQ-R2 §1.3, punto 3).",
          f"2. **Una forma de la tabla que la regla no toma dentro de la ventana** (`forma_no_reconocida_por_las_reglas`: "
          f"{out['causas_i'].get('forma_no_reconocida_por_las_reglas', 0)}): candidato de implementación.",
          f"3. **Ventana** (`fuera_de_la_ventana_antes` y `_despues`: "
          f"{out['causas_i'].get('fuera_de_la_ventana_antes', 0) + out['causas_i'].get('fuera_de_la_ventana_despues', 0)}).",
          f"4. **Formas fuera de la tabla** (familia (ii): {out['por_familia'].get('ii', 0)}): candidatos de la definición, "
          f"por forma (sección 4).",
          f"5. **Sin marcador** (familia (iii): {out['por_familia'].get('iii', 0)}): la `no_determinada` probablemente es "
          f"correcta; por regla: {out['familia_por_regla']}.", "",
          "## 6. Ejemplos (solo de fuera de la muestra)", "",
          f"A ciegas: {out['a_ciegas']['en_la_muestra']} elementos de la población están en la muestra y "
          f"{out['a_ciegas']['reservados_del_lote_3']} los daría la regla del lote 3; cuentan en los agregados y no "
          f"aparecen ni en el listado ni en los ejemplos.", ""]
    for titulo, cond in (
            ("(i), marcador fuera del texto leído, y la cláusula completa lo fija",
             lambda r: r["familia"] == "i" and r.get("causa") == "marcador_fuera_del_texto_leido"
             and r.get("con_la_clausula_de_e0") not in (None, "no_determinada")),
            ("(i), marcador fuera del texto leído, y tampoco con la cláusula completa",
             lambda r: r["familia"] == "i" and r.get("causa") == "marcador_fuera_del_texto_leido"
             and r.get("con_la_clausula_de_e0") == "no_determinada"),
            ("(i), forma que la regla no toma", lambda r: r.get("causa") == "forma_no_reconocida_por_las_reglas"),
            ("(i), ventana", lambda r: str(r.get("causa", "")).startswith("fuera_de_la_ventana")),
            ("(ii)", lambda r: r["familia"] == "ii"),
            ("(iii)", lambda r: r["familia"] == "iii")):
        L.append(f"**{titulo}:**")
        L += [linea(r) for r in ejemplos(cond)] or ["  - (ninguno fuera de la muestra)"]
        L.append("")
    ruta.write_text("\n".join(L) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--acta", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    acta = json.loads(a.acta.read_text(encoding="utf-8"))
    kg, s_kg = C.cargar_kg()
    if s_kg != acta["grafo"]["kg_sha256"]:
        raise SystemExit("el grafo no es el del acta")
    filas = C.marco(kg)
    if C.sha(C.canon(filas)) != acta["poblacion"]["sha256_lista"]:
        raise SystemExit("la población no es la del acta")
    muestra = set(acta["sorteo"]["lote1"]) | set(acta["sorteo"]["lote2"])
    reservados = muestra | reservados_lote3(acta, filas)
    R = C.rcmp()
    idx = C.indice_elementos(kg)
    pob = [(e, n, i, el) for e, (n, i, el) in sorted(idx.items())
           if C.estrato(el) != "V-vacío" and el.get("comparacion") == "no_determinada"]

    regs = []
    for e, n, i, el in pob:
        u = C.ubicar(n, i, el)
        r = {"id": e, "to": n["provenance"].get("to"), "tipo": n["type"], "estrato": C.estrato(el),
             "autor": "validador" if C.es_validador(el) else "ensamblado", "unidad": el.get("unidad"),
             "regla_comparacion": el.get("regla_comparacion"), "origen": el.get("origen"),
             "ubicacion": u["metodo"], "nota_ubicacion": u["nota"], "chunk_id": u["chunk_id"]}
        if not u["spans"]:
            r["familia"] = "sin_clausula"
            regs.append(r)
            continue
        txt, chk = next((t, ch) for cid, t, ch in C.textos_nodo(n) if cid == u["chunk_id"])
        ini, fin = T.ajustar_cuantia(txt, u["spans"][0], el.get("tramo") or "", C.plegar)
        ca, cb = T.clausula(txt, ini, fin, T.uniones(chk))
        cl = T.para_mostrar(txt[ca:cb])
        tabla, fuera = marcadores(C.plegar(cl), C.plegar(T.para_mostrar(txt[ca:ini])) + " ")
        r.update(clausula=cl, cuantia=T.para_mostrar(txt[ini:fin]), marcadores_tabla=tabla, formas_fuera=fuera,
                 ambigua=len(u["spans"]) > 1)
        r["familia"] = "i" if tabla else ("ii" if fuera else "iii")
        ch = C.chunks_to(r["to"]).get(u["chunk_id"]) or {}
        titulo = ch.get("titulo")
        desc = (n.get("properties") or {}).get("descripcion")
        if r["familia"] == "i":
            if el.get("origen") == "e1":
                fuente = u["tramo_e1_del_elemento"] or next(
                    (t for _, t in u["tramos_e1"] if C.ocurrencias(t, el.get("tramo") or "")), None)
                r["texto_leido_por_la_regla"] = "tramo de E1"
            else:
                fuente = desc
                r["texto_leido_por_la_regla"] = "descripción del nodo"
            if fuente:
                r.update(causa_codigo(R, fuente, el.get("tramo") or "", desc, titulo))
            else:
                r.update(causa="no_reproducida", detalle="no se encuentra el texto que leyó la regla")
        # contraste: la regla sobre la cláusula de E0 completa
        cs = R.analizar(cl, desc, titulo, "no_determinada")
        k = C._norm(el.get("tramo") or "")
        c = next((x for x in cs if C._norm(x.texto) == k), None)
        r["con_la_clausula_de_e0"] = None if c is None else c.comparacion
        regs.append(r)

    def agrupa(clave):
        d = defaultdict(Counter)
        for r in regs:
            d[str(r.get(clave))][r["familia"]] += 1
        return {k: dict(v) for k, v in sorted(d.items())}

    fam_i = [r for r in regs if r["familia"] == "i"]
    contraste = Counter(("determina" if r.get("con_la_clausula_de_e0") not in (None, "no_determinada")
                         else "no_determina" if r.get("con_la_clausula_de_e0") == "no_determinada" else "sin_cuantia")
                        for r in regs if r["familia"] != "sin_clausula")
    contraste_por_familia = defaultdict(Counter)
    for r in regs:
        if r["familia"] != "sin_clausula":
            v = r.get("con_la_clausula_de_e0")
            contraste_por_familia[r["familia"]]["determina" if v not in (None, "no_determinada")
                                                else "no_determina" if v == "no_determinada" else "sin_cuantia"] += 1
    out = {
        "unidad": "U-MED-UMBRALES, etapa P, tramo P-a, punto 5: diagnóstico de la comparación no_determinada "
                  "(sin lectura, sin veredicto, sin cifra)",
        "acta": {"ruta": "data/experiment/med_umbrales/p/acta_sorteo_P.json", "sha256": C.sha(a.acta.read_bytes())},
        "grafo_sha256": s_kg,
        "poblacion": {
            "N": len(regs),
            "por_autor": dict(Counter(r["autor"] for r in regs)),
            "por_regla": dict(Counter(r["regla_comparacion"] for r in regs)),
            "por_estrato": dict(Counter(r["estrato"] for r in regs)),
            "por_unidad": dict(Counter(str(r["unidad"]) for r in regs)),
            "por_to": dict(sorted(Counter(r["to"] for r in regs).items())),
            "por_ubicacion": dict(Counter(r["ubicacion"] for r in regs))},
        "regla_de_corte": "punto y coma; punto seguido de espacio y de una mayúscula, de un número de punto o del fin "
                          "del texto; salto de línea solo si abre un ítem, si el renglón anterior termina en dos puntos "
                          "o si une el texto propio con un bloque heredado (texto_P.clausula); un corte de renglón del "
                          "PDF no corta; sobre el texto completo de la unidad, con los cortes de renglón unidos",
        "familias": {"i": [n for n, _ in FORMAS_TABLA] + ["maximo / minimo pegado a la cuantia"],
                     "ii": [n for n, _ in FORMAS_FUERA], "precedencia": "i > ii > iii",
                     "regex_i": dict(FORMAS_TABLA), "regex_ii": dict(FORMAS_FUERA),
                     "adyacencia": ADYACENTE.pattern},
        "por_familia": dict(Counter(r["familia"] for r in regs)),
        "familia_por_estrato": agrupa("estrato"), "familia_por_unidad": agrupa("unidad"),
        "familia_por_regla": agrupa("regla_comparacion"), "familia_por_to": agrupa("to"),
        "familia_por_origen": agrupa("origen"),
        "marcadores_i": dict(Counter(m for r in fam_i for m in r["marcadores_tabla"]).most_common()),
        "formas_ii": dict(Counter(m for r in regs if r["familia"] == "ii" for m in r["formas_fuera"]).most_common()),
        "formas_fuera_en_todas": dict(Counter(m for r in regs if r["familia"] != "sin_clausula"
                                              for m in r["formas_fuera"]).most_common()),
        "causas_i": dict(Counter(r.get("causa") for r in fam_i).most_common()),
        "causas_i_por_texto_leido": {k: dict(Counter(r.get("causa") for r in fam_i if r.get("texto_leido_por_la_regla") == k))
                                     for k in ("tramo de E1", "descripción del nodo")},
        "causas_i_por_contraste": {k: dict(Counter(("determina" if r.get("con_la_clausula_de_e0") not in (None, "no_determinada")
                                                     else "no_determina" if r.get("con_la_clausula_de_e0") == "no_determinada"
                                                     else "sin_cuantia") for r in fam_i if r.get("causa") == k))
                                   for k in CAUSAS if any(r.get("causa") == k for r in fam_i)},
        "contraste_clausula_completa": {"total": dict(contraste),
                                        "por_familia": {k: dict(v) for k, v in sorted(contraste_por_familia.items())}},
        "ambiguas": sum(1 for r in regs if r.get("ambigua")),
        "largo_clausula": (lambda xs: {"n": len(xs), "mediana": xs[len(xs) // 2] if xs else None,
                                       "p90": xs[int(len(xs) * 0.9)] if xs else None, "max": xs[-1] if xs else None})(
            sorted(len(r["clausula"]) for r in regs if r.get("clausula") is not None)),
        "a_ciegas": {"en_la_muestra": sum(1 for r in regs if r["id"] in muestra),
                     "reservados_del_lote_3": sum(1 for r in regs if r["id"] in reservados - muestra),
                     "regla": "los elementos de la muestra y los que daría la regla del lote 3 solo cuentan en los "
                              "agregados; el listado por elemento los deja fuera"},
        "elementos_fuera_de_la_muestra": [r for r in regs if r["id"] not in reservados],
    }
    a.salida.mkdir(parents=True, exist_ok=True)
    (a.salida / "diagnostico_no_determinada_P.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n",
                                                              encoding="utf-8")
    escribir_md(out, a.salida / "diagnostico_no_determinada_P.md")
    print(json.dumps({k: out[k] for k in ("por_familia", "causas_i", "contraste_clausula_completa", "ambiguas", "a_ciegas")},
                     ensure_ascii=False))
    print(json.dumps(out["poblacion"], ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
