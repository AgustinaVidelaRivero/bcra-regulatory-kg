"""B6.1, tanda final, T4, primer tramo: las tablas del FRENO, por script, desde lo que está en t4/. Solo lee; escribe t4/tablas_freno_t4.md
y la imprime.
  - Tabla 1: por muestra, cuántas propuestas hay de cada respuesta (lectura_asistida_t4_tramo1.json, «cuentas»), con el total de fichas
    y la suma de las cuentas, que tiene que cerrar.
  - Tabla 2: las reglas usadas, por muestra («reglas_usadas»).
  - Tabla 3: las planillas de la autora, el LEEME y el convertidor, con su sha256 (recalculado aquí) y el que declara cada fuente: el
    JSON de la lectura para las planillas, el del «seguí» para el LEEME (9e224f09…) y SHA_PLANILLAS del convertidor, por su árbol
    sintáctico, sin correrlo.
  - Tabla 4: la prueba del convertidor (prueba_convertidor/prueba_convertidor_t4.json), caso por caso.
Uso: python3 -I -B tablas_freno_t4.py <repo>
"""
import ast
import hashlib
import json
import sys
from pathlib import Path

R = Path(sys.argv[1]).resolve()
T4 = R / "data/experiment/tanda_final/t4"
L = lambda p: json.loads(p.read_text(encoding="utf-8"))  # noqa: E731
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()  # noqa: E731
la = L(T4 / "lectura_asistida/lectura_asistida_t4_tramo1.json")
pr = L(T4 / "prueba_convertidor/prueba_convertidor_t4.json")
LEEME_SHA = "9e224f09213b0ca821bcbbf0af0c923c09251cb5bfd1f81d5b716697ea627525"
ORDEN = {"cola": ["sin error", "con error", "dudosa"], "aceptadas_items": ["sin error", "con error", "dudosa"],
         "aceptadas_no_items": ["sin error", "con error", "dudosa"], "vigilancia_2": ["vaciamiento", "no vaciamiento", "no decidible"],
         "vigilancia_7": ["con apoyo", "sin apoyo", "no decidible"], "vigilancia_1": ["sí", "no", "no decidible"],
         "vigilancia_3": ["duplicación", "distintos"], "observacion_12": ["correcta", "no decidible"]}
w = [f"#### Tabla 1. Las propuestas, por muestra y por respuesta (`lectura_asistida/lectura_asistida_t4_tramo1.json`; modelo "
     f"{la['modelo']['nombre']}, `{la['modelo']['id']}`; de {la['hora_de_la_lectura']['toda']['primera_propuesta'][11:19]} a "
     f"{la['hora_de_la_lectura']['toda']['ultima_escritura'][11:19]} del {la['hora_de_la_lectura']['toda']['primera_propuesta'][:10]})", "",
     "| muestra | fichas | propuestas por respuesta | suma |", "|---|---:|---|---:|"]
tot = 0
for m, cu in la["cuentas"].items():
    resp = ORDEN[m] + sorted(k for k in cu if k not in ORDEN[m])
    n = len(la["propuestas"][m])
    tot += n
    w.append(f"| {m} | {n} | " + "; ".join(f"{k} {cu.get(k, 0)}" for k in resp) + f" | {sum(cu.values())} |")
w.append(f"| total | {tot} | — | {sum(sum(c.values()) for c in la['cuentas'].values())} |")
w += ["", "#### Tabla 2. Las reglas de la propuesta usadas, por muestra (`reglas_usadas`; definidas en `criterios_de_la_propuesta`)", "",
      "| muestra | reglas |", "|---|---|"]
for m, rg in la["reglas_usadas"].items():
    w.append(f"| {m} | " + "; ".join(f"`{k}` {v}" for k, v in sorted(rg.items(), key=lambda x: -x[1])) + " |")
arbol = ast.parse((T4 / "lectura_autora/convertir_lectura_T4.py").read_text(encoding="utf-8"))
conv = next(ast.literal_eval(n.value) for n in arbol.body if isinstance(n, ast.Assign)
            and any(getattr(t, "id", "") == "SHA_PLANILLAS" for t in n.targets))
w += ["", "#### Tabla 3. Las planillas en blanco de la autora, el LEEME y el convertidor (sha256 recalculado aquí)", "",
      "| archivo | sha256 | igual al del JSON de la lectura | igual al de SHA_PLANILLAS del convertidor |", "|---|---|---|---|"]
for m in la["cuentas"]:
    p = T4 / "lectura_autora" / f"{m}.csv"
    h = sha(p)
    w.append(f"| `t4/lectura_autora/{m}.csv` | `{h}` | {h == la['material'][m]['planilla_de_la_autora']['sha256']} | {h == conv.get(m)} |")
h = sha(T4 / "lectura_autora/LEEME_lectura_T4.md")
w.append(f"| `t4/lectura_autora/LEEME_lectura_T4.md` | `{h}` | igual al del «seguí»: {h == LEEME_SHA} | — |")
w.append(f"| `t4/lectura_autora/convertir_lectura_T4.py` | `{sha(T4 / 'lectura_autora/convertir_lectura_T4.py')}` | — | "
         f"muestras en SHA_PLANILLAS: {len(conv)} |")
src = R / "data/experiment/tanda1/t4/lectura_autora/convertir_lectura_T4.py"
w.append(f"\nEl convertidor de la tanda 1 (`{src.relative_to(R)}`, `{sha(src)[:16]}…`) y el de la tanda final difieren solo en la primera "
         "línea del docstring («tanda 1» → «tanda final») y en los ocho valores de SHA_PLANILLAS (`diff`, sección 4 del FRENO).")
w += ["", f"#### Tabla 4. La prueba del convertidor (`prueba_convertidor/prueba_convertidor_t4.json`; {pr['python3']}; fuera del repo)", "",
      "| caso | código de salida (esperado) | lo que controla | ok |", "|---|---|---|---|"]
for c in pr["casos"]:
    w.append(f"| {c['caso']} | {c['rc']} ({c['espera_rc']}) | «{c['espera_texto']}» en la salida | {c['ok']} |")
w.append(f"\nEl repo, antes y después de la prueba: `t4/lectura_autora/` con los mismos sha256 ({pr['repo_sin_cambios']}); la copia, igual "
         f"al repo antes de probar ({pr['copia_igual_al_repo_antes_de_probar']}) y sin enlaces ({len(pr['enlaces_en_la_copia'])}); todos los "
         f"casos como se esperaba: {pr['todos_ok']}.")
texto = "\n".join(w) + "\n"
(T4 / "tablas_freno_t4.md").write_text(texto, encoding="utf-8")
print(texto)
