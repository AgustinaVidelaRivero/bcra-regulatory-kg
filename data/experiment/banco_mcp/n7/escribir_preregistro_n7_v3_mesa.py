"""escribir_preregistro_n7_v3_mesa.py — mesa, §312 (27/10/2026; el de la §299 con la elección sobre las 26 de la decisión 9 y la lectura
tolerante del juez): el texto del pre-registro de N7 para que la autora lo lea y lo firme, escrito desde el registro de N7
(n7_configuracion_sellada.json, de armar_n7_v3_mesa.py), el análisis de N6 que rige y, si se pasa, el análisis sellado. Llena los huecos que el pre-registro de
B6.3 deja para N7 (H-3 a H-6) con lo que dice el registro, y nada más: toda cifra sale de los dos JSON, con su sha256. No decide nada.
  python3 -I -B escribir_preregistro_n7_v3_mesa.py <n7_configuracion_sellada.json> <analisis que rige> <salida .md> [<analisis sellado>]
"""
import hashlib
import json
import re
import sys
import textwrap
from pathlib import Path

reg_p, an_p, sal = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
sel_p = Path(sys.argv[4]) if len(sys.argv) > 4 else None
reg, an = json.loads(reg_p.read_text(encoding="utf-8")), json.loads(an_p.read_text(encoding="utf-8"))
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()  # noqa: E731
g, fr, r5, rg = reg["brazo_grafo"], reg["brazo_fragmentos"], reg["R5"], reg["regla_N4_5"]
X = g["configuracion_n6"]
ot = rg["otra_vez"]
d9 = str(ot.get("sobre", "")).startswith("las 26")
fid = an["regla"]["fidelidad_sin_FUERA_D9" if d9 else "fidelidad_30"]
sobre = "las 26 sin FUERA_D9 (decisión 9)" if d9 else "las 30"
vn = "V(26)" if d9 else "V(30)"
pct = lambda x: "—" if x is None else f"{x:.4f}".replace(".", ",")  # noqa: E731
L = []
w = L.append
w("# Pre-registro de N7: la configuración elegida en N6, para B6.3")
w("")
w(f"Escrito por `escribir_preregistro_n7_v3_mesa.py` desde `n7_configuracion_sellada.json` (`{sha(reg_p)[:16]}…`) y el análisis de N6")
w(f"(`{reg['analisis_n6']['ruta']}`, `{reg['analisis_n6']['sha256'][:16]}…`, la elección de `{reg['analisis_n6']['eleccion']}`). Lo")
w("firma la autora; el commit de la firma lo sella con su sha256, antes de la entrada sellada de B6.3.")
w("")
w("## 1. La regla de N4, §5, sobre lo medido en N6")
w("")
w(f"- **Sobre {sobre}.** **Candidatas:** {', '.join(ot['candidatas'])}. **Dentro de {vn}** ({pct(ot['V'])}): "
  f"{', '.join(ot['dentro_de_V'])}.")
w(f"- **El desempate** (menos veces al tope, después menos R9): {', '.join(rg['otra_vez']['orden_de_desempate'])}.")
w(f"- **La elegida: {X}**, con fidelidad {pct(fid.get(X))} sobre {sobre}. La regla, aplicada otra vez por la mesa sobre los agregados"
  " del análisis, da la misma elegida y el mismo orden.")
c30 = (an["regla"]["eleccion"] or {}).get("con_las_30")
if d9 and c30:
    w(f"- **Con las 30, al lado** (la decisión 9): la elegida es {c30['elegida']}, con el orden {', '.join(c30['orden_de_desempate'])}.")
ag = an.get("agregados") or {}
if ag:
    w(f"- **La lectura del juez:** los agregados de las {ag.get('n')} respuestas juzgadas, con las salidas que no se leían como JSON leídas con la"
      " lectura tolerante (decisión de la autora del 27/10/2026, recibida a las 23:26:23; registro, §151).")
if sel_p is not None:
    sel = json.loads(sel_p.read_text(encoding="utf-8"))
    es = sel["regla"]["eleccion"]
    w(f"- **Con la lectura sellada, al lado** (`{sha(sel_p)[:16]}…`): la elegida es {es['elegida']}"
      + (f", y con las 30, {es['con_las_30']['elegida']}" if es.get("con_las_30") else "")
      + (". Las dos lecturas eligen lo mismo." if es["elegida"] == X else ". Las dos lecturas difieren: se declara."))
w(f"- **El requisito de la jerarquía:** {(rg.get('requisito_jerarquia') or {}).get('por', '—')}.")
w("")
w("## 2. Lo que fija para B6.3")
w("")
w(f"- **H-3, el brazo del grafo:** la configuración {X}, con las familias {g['familias']}"
  f"{'' if g['carga_el_codificador'] else ', sin el codificador'}, servida por `{g['servidor']}` sobre el grafo evaluado")
w(f"  (`{g['grafo']}`, `{g['kg_sha256'][:16]}…`). Sus archivos, en `data/experiment/banco_mcp/n7/`:")
for k, v in g["archivos"].items():
    w(f"  - `{k}`, `{v[:16]}…`;")
if g.get("herramientas_esperadas"):
    w(f"  - las herramientas: {', '.join(t.replace('mcp__kg__', '') for t in g['herramientas_esperadas'])}.")
w(f"- **H-4, la principal del brazo de fragmentos:** {'la híbrida' if fr['principal']['afinidad'] == 'hibrida' else 'BM25'} "
  f"(F1 de N6: entra la híbrida, {'sí' if reg['F1']['entra_la_hibrida'] else 'no'}), `{fr['principal']['config']}` (`{fr['principal']['sha256'][:16]}…`).")
w(f"  El denso no cambia: `{fr['denso']['config']}` (`{fr['denso']['sha256'][:16]}…`).")
w(f"- **H-5, los índices:** el índice por punto del grafo evaluado, `{g['indice_puntos']['ruta']}`, con su manifiesto")
hb = g["hubs_esperados"] or {}
w(f"  `{g['indice_puntos']['sha256_manifiesto'][:16]}…`, y los hubs esperados al cargarlo: umbral {hb.get('umbral')}, {hb.get('n')} nodos,"
  f" `{str(hb.get('sha256'))[:16]}…`.")
sube = "sube a 45, 47 y 3,30" if r5["sube"] else "queda en 30, 32 y 1,80"
w(f"- **H-6, R5:** {sube}. Las sesiones de N6 de lo elegido que llegaron al tope:")
for c, t in r5["por_brazo"].items():
    frac = "" if t["fraccion"] is None else f" ({pct(t['fraccion'])})"
    w(f"  - {c}: {t['al_tope']} de {t['sesiones']}{frac};")
w("  la regla, confirmada por la autora el 27/10/2026 (15:04:04): más del 5 % de las sesiones de N6 de lo elegido, en cualquiera de")
w("  los dos brazos.")
w(f"- **La plantilla:** la de N6, `{reg['plantilla']['de_N6']}` (`{reg['plantilla']['sha256'][:16]}…`), en los dos brazos.")
w("")
w("## 3. Lo que queda pendiente")
w("")
if reg["pendiente"]:
    for p in reg["pendiente"]:
        w(f"- {p['que']}: {p['por']}.")
else:
    w("- Nada.")
w("")
w("## 4. Lo que se declara")
w("")
w("- N6 midió sobre el acumulado de las tandas 0 y 1; B6.3 corre sobre el grafo evaluado. N7 lleva la configuración elegida a ese grafo")
w("  sin cambiar sus herramientas, su bloque ni su plantilla.")
w("- La regla de R5 se lee sobre las sesiones de N6 de lo elegido en cada brazo, como lo confirmó la autora.")
if ag:
    w("- **La lectura tolerante es un desvío del análisis sellado de N6,** decidido por la autora antes de ver ninguna cifra (registro, §151),"
      " con su motivo, tal cual: «las salidas que fallan son las que copian un pasaje con comillas, así que sacarlas o contarlas como no"
      " cumplidas no es neutral entre configuraciones». El análisis sellado va al lado.")
if d9:
    w("- **La elección va sin FUERA_D9** (la decisión 9, desvío de N4): las cuatro preguntas que comparten texto con los ejemplos de la"
      " familia 6 salen de las comparaciones entre una configuración con esos ejemplos y una sin ellos; la versión con las 30 va al lado.")
if X not in ("T", "T-F1", "T-F2", "T-F3", "T-F4", "T-F5"):
    w(f"- **{X} no lleva la familia 6:** el brazo del grafo no lleva sus 3 ejemplos, así que el de fragmentos tampoco (decisión 10), y la"
      " unidad de los ejemplos de fragmentos no corre.")
cn1 = an.get("clases_n1") or {}
if cn1.get("estado") == "PENDIENTE":
    w("- **Las cuatro clases de N1** sobre los criterios no cumplidos quedan PENDIENTES: las clasifica la regla sellada de N1 (`db2cc290…`),"
      " que vive en una carpeta que el despacho de N6 veda. No entran en la regla de N4.")
# Los renglones de más de 140 caracteres se cortan en 136, con la sangría de su viñeta.
M = []
for x in L:
    if len(x) <= 140:
        M.append(x)
        continue
    sangria = re.match(r"^\s*(- )?", x).group(0)
    M += textwrap.wrap(x, 136, subsequent_indent=" " * len(sangria), break_long_words=False, break_on_hyphens=False)
L = M
sal.write_text("\n".join(L) + "\n", encoding="utf-8")
largos = [i for i, x in enumerate(L, 1) if len(x) > 140]
print(f"escrito {sal.name}: {len(L)} renglones; de más de 140 caracteres: {largos}")
