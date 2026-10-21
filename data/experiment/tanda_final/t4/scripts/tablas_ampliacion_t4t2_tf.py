"""B6.1, tanda final, T4, segundo tramo, punto 5 del «seguí»: las tablas de la ampliación de las aceptadas no ítems para el FRENO, por
script: el sorteo por celda y sus dos corridas, el material y la planilla de la autora (sha256 recalculado aquí), la lista de unidades a
la vista antes y después, y las propuestas de la lectura asistida (no son veredictos: la autora lee en el tercer tramo). Solo lee;
escribe tanda_final/t4/ampliacion/tablas_ampliacion_t4t2.md bajo <raíz> y la imprime.
Uso: python3 -I -B tablas_ampliacion_t4t2_tf.py <raíz>
"""
import csv
import hashlib
import io
import json
import sys
from collections import Counter
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ = Path(sys.argv[1]).resolve()
TF = RAIZ / "data/experiment/tanda_final"
AMP = TF / "t4/ampliacion"
M = "aceptadas_no_items_ampliacion"
CEL = ["RI:sin_raiz", "RI:resto", "NG:sin_raiz", "NG:resto"]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()  # noqa: E731
mil = lambda n: f"{n:,}".replace(",", ".")  # noqa: E731
rel = lambda p: f"`{p.relative_to(TF / 't4').as_posix()}`"  # noqa: E731
leer = lambda p: json.loads(p.read_text(encoding="utf-8"))  # noqa: E731

MU, IDX = AMP / "muestras" / f"{M}.json", AMP / "muestras/sorteo_ampliacion_t4t2_tf.json"
MU2, IDX2 = AMP / "segunda_corrida_del_sorteo" / f"{M}.json", AMP / "segunda_corrida_del_sorteo/sorteo_ampliacion_t4t2_tf.json"
mu, idx, idx2 = leer(MU), leer(IDX), leer(IDX2)
MAT = AMP / "material"
mat, ctl = leer(MAT / "material_ampliacion_t4t2_tf.json"), leer(MAT / "control_material_ampliacion_t4t2_tf.json")
VISTA = TF / "t3/muestras/unidades_a_la_vista_T4.json"
vista = leer(VISTA)
LA = leer(AMP / "lectura_asistida/lectura_asistida_t4_ampliacion.json")
PLA = AMP / "lectura_autora" / f"{M}.csv"

w = ["Rutas relativas a `data/experiment/tanda_final/t4/`; salen de `scripts/tablas_ampliacion_t4t2_tf.py`.", "",
     f"#### Tabla A1. El sorteo de la ampliación, por celda ({rel(MU)}; {idx['hora']}; de `scripts/sorteo_ampliacion_t4t2_tf.py`)", "",
     "| celda | N del estrato | leídas en el primer tramo | quedan | sorteadas | cómo | cadena |", "|---|---:|---:|---:|---:|---|---|"]
for c in CEL:
    x = mu["celdas"][c]
    w.append(f"| {c} | {mil(mu['N_por_celda_del_estrato'][c])} | {mu['leidas_por_celda'][c]} | {mil(x['N'])} | {x['n']} | {x['como']} | "
             f"`{x['cadena']}` |")
w.append(f"| total | {mil(mu['N_del_estrato'])} | {sum(mu['leidas_por_celda'].values())} | {mil(sum(mu['N_por_celda_que_quedan'].values()))} | "
         f"{mu['n']} | — | — |")
w += ["", f"Las cuotas son las de `celdas_t4_t3f.asignar` de la tanda 1 (sha256 `{idx['celdas_t4_t3f_sha256']}`) sobre lo que queda; notas "
      f"de la asignación: {'; '.join(mu['notas']) if mu['notas'] else 'ninguna'}. Base `{mu['base']}` (sha256 de la versión para firmar, "
      f"`{idx['version_para_firmar_sha256'] == mu['base']}`); pre-registro firmado `{idx['preregistro_firmado_sha256']}`. Controles del "
      f"sorteo: {sum(idx['controles'].values())} de {len(idx['controles'])} pasan.", "",
      "#### Tabla A2. Las dos corridas del sorteo (sha256 recalculado aquí)", "",
      "| archivo | primera corrida | segunda corrida | iguales |", "|---|---|---|---|"]
for a, b in ((MU, MU2), (IDX, IDX2)):
    w.append(f"| `{a.name}` | `{sha(a)}` | `{sha(b)}` | {sha(a) == sha(b)} |")
w += ["", f"La muestra de la primera corrida es la del índice: `{sha(MU) == idx['sha256']}`. Horas de los índices: {idx['hora']} y {idx2['hora']}.",
      "", f"#### Tabla A3. El material, la lectura asistida y la planilla de la autora (sha256 recalculado aquí)", "",
      "| archivo | sha256 | igual al de su índice |", "|---|---|---|"]
for nom, s in mat["muestras"]["aceptadas:no_items:ampliacion"]["archivos"].items():
    p = MAT / M / nom
    w.append(f"| {rel(p)} | `{sha(p)}` | {sha(p) == s} (`material/material_ampliacion_t4t2_tf.json`) |")
w.append(f"| {rel(PLA)} | `{sha(PLA)}` | {sha(PLA) == LA['material'][M]['planilla_de_la_autora']['sha256']} "
         f"(`lectura_asistida/lectura_asistida_t4_ampliacion.json`) |")
for p in (AMP / "lectura_asistida/lectura_asistida_t4_ampliacion.json", AMP / "lectura_asistida/omisiones_y_observaciones_t4_ampliacion.md",
          AMP / "lectura_asistida/borradores" / f"{M}.jsonl"):
    w.append(f"| {rel(p)} | `{sha(p)}` | — |")
b = PLA.read_bytes()
filas = list(csv.reader(io.StringIO(b.decode("utf-8"), newline=""), delimiter=";"))
forma = {"UTF-8 sin BOM": not b.startswith(b"\xef\xbb\xbf"), "sin «\\r»": b"\r" not in b,
         "columnas": filas[0] == ["id", "celda", "ficha", "propuesta", "justificacion", "veredicto_autora", "nota_autora"],
         "filas": len(filas) - 1 == mu["n"], "las dos columnas de la autora, vacías": all(f[5] == "" and f[6] == "" for f in filas[1:]),
         "ninguna celda empieza con «=», «+», «-» ni «@»": not [x for f in filas for x in f if x[:1] in ("=", "+", "-", "@")]}
w += ["", "La forma de la planilla de la autora: " + "; ".join(f"{k}, {v}" for k, v in forma.items()) + "."]
c = ctl["aceptadas:no_items:ampliacion"]
w += ["", f"El control del material (`material/control_material_ampliacion_t4t2_tf.json`): {c['fichas']} fichas, {c['claves_vedadas']} claves "
      f"vedadas, texto de la E0 en {c['texto_de']['e0']}, {c['sin_texto']} sin texto, {c['estado_en_el_md']} con el estado en el `.md`; "
      f"ok: {ctl['ok']}. Hora del material: {mat['hora']}, posterior a la del sorteo ({idx['hora']}): {mat['hora'] > idx['hora']}.", "",
      f"#### Tabla A4. La lista de unidades a la vista (`../t3/muestras/unidades_a_la_vista_T4.json`; {vista['hora']})", "",
      "| cifra | valor |", "|---|---|"]
a = vista["ampliacion"]
w += [f"| sha256 anterior | `{a['lista_anterior_sha256']}` ({a['lista_anterior_hora']}) |",
      f"| sha256 nuevo (recalculado aquí) | `{sha(VISTA)}` |",
      f"| unidades a la vista antes | {mil(a['unidades_a_la_vista_antes'])} |",
      f"| unidades que suma la ampliación | {mil(a['unidades_que_suma_la_ampliacion'])} |",
      f"| unidades a la vista después | {mil(a['unidades_a_la_vista_despues'])} (`todas_las_muestras`: "
      f"{mil(vista['todas_las_muestras']['unidades_a_la_vista'])}) |",
      f"| antes + suma = después | {a['unidades_a_la_vista_antes'] + a['unidades_que_suma_la_ampliacion'] == a['unidades_a_la_vista_despues']} |",
      f"| las ocho muestras de T3 dan lo mismo que en la lista anterior | {a['las_ocho_muestras_de_T3_dan_lo_mismo_que_en_la_lista_anterior']} |",
      f"| el material de la ampliación que usa la lista es el de la tabla A3 | "
      f"{vista['material_ampliacion_t4t2_tf_sha256'] == sha(MAT / 'material_ampliacion_t4t2_tf.json')} |",
      "", f"#### Tabla A5. Las propuestas de la lectura asistida, por celda (`lectura_asistida/lectura_asistida_t4_ampliacion.json`; "
      f"modelo {LA['modelo']['nombre']}, `{LA['modelo']['id']}`; de {LA['hora_de_la_lectura'][M]['primera_propuesta']} a "
      f"{LA['hora_de_la_lectura'][M]['ultima_escritura']})", "",
      "Son propuestas, no veredictos: la autora lee la planilla y las tasas sobre las 60 van en el tercer tramo.", "",
      "| celda | fichas | con error | sin error | dudosa |", "|---|---:|---:|---:|---:|"]
P = LA["propuestas"][M]
for cc in CEL + [None]:
    xs = [p for p in P if cc is None or p["celda"] == cc]
    k = Counter(p["propuesta"] for p in xs)
    w.append(f"| {cc or 'total'} | {len(xs)} | {k['con error']} | {k['sin error']} | {k['dudosa']} |")
assert dict(Counter(p["propuesta"] for p in P)) == LA["cuentas"][M]
w += ["", "| regla | propuestas | fichas |", "|---|---:|---|"]
for r, n in sorted(LA["reglas_usadas"][M].items(), key=lambda x: (-x[1], x[0])):
    w.append(f"| `{r}` | {n} | " + ", ".join(str(p["n"]) for p in P if p["regla"] == r) + " |")
texto = "\n".join(w) + "\n"
(AMP / "tablas_ampliacion_t4t2.md").write_text(texto, encoding="utf-8")
print(texto)
