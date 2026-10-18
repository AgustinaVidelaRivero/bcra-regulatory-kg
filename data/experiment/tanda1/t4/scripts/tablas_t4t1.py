"""B6.1, tanda 1, T4, primer tramo, punto 9: las tablas del FRENO, por script, desde el árbol que se escribe en el repo (<raíz>, con
tanda1/t4/ y tanda1/t3/muestras/unidades_a_la_vista_T4.json): poblaciones, sorteos y su segunda corrida, material, lo que queda a la
vista, la lectura asistida y los archivos de la lectura de la autora. Solo lee; escribe tanda1/t4/tablas_t4_tramo1.md bajo <raíz> y la
imprime. El NO_ABRIR_ no se abre: de él, solo el sha256 del archivo.
Uso: python3 -I -B tablas_t4t1.py <raíz>
"""
import hashlib
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ = Path(sys.argv[1]).resolve()
T4 = RAIZ / "data/experiment/tanda1/t4"
M = T4 / "muestras"
L = lambda p: json.loads(Path(p).read_text(encoding="utf-8"))  # noqa: E731
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()  # noqa: E731
mil = lambda n: f"{n:,}".replace(",", ".")  # noqa: E731
CEL = ["RI:sin_raiz", "RI:resto", "NG:sin_raiz", "NG:resto"]
pob, sor, sor2 = L(M / "poblaciones_t4_tramo1.json"), L(M / "sorteos_t4_tramo1.json"), L(M / "segunda_corrida_de_los_sorteos/sorteos_t4_tramo1.json")
mat = L(M / "material/material_t4_tramo1.json")
vis = L(RAIZ / "data/experiment/tanda1/t3/muestras/unidades_a_la_vista_T4.json")
la = L(T4 / "lectura_asistida/lectura_asistida_t4_tramo1.json")
w = [f"#### Tabla 1. La población por celda (`muestras/poblaciones_t4_tramo1.json`, {pob['hora']})", "",
     "| muestra | elemento | N | " + " | ".join(CEL) + " | sha256 de los ids por celda |", "|---|---|---:|" + "---:|" * 4 + "---|"]
filas = [(m, x) for m, x in pob["muestras"].items()] + [("observacion:12, A4.1 tal cual (información)", pob["observacion_12_A41_tal_cual_informacion"])]
for m, x in filas:
    w.append(f"| {m} | {x['elemento']} | {mil(x['N'])} | " + " | ".join(mil(x["N_por_celda"][c]) for c in CEL) + f" | `{x['sha256_ids_por_celda']}` |")
ci = pob["composicion_informacion"]
w += ["", f"- **Lo que la decisión 1.2 resta de A4.1:** " + "; ".join(f"{k}, {mil(v)}" for k, v in ci["restadas_por_la_decision_1_2_sobre_A41"].items()) + ".",
      "- **La (12) nueva, por relación:** " + ", ".join(f"{k} {mil(v)}" for k, v in ci["observacion:12"]["relacion"].items()) + ".",
      "- **Los controles de `poblaciones_t4t1.py`:** " + "; ".join(
          f"{k}: {v if isinstance(v, (bool, str)) else v.get('igual')}" for k, v in pob["controles"].items() if k != "poblaciones_t4_T3_sha256") + "."]
w += ["", f"#### Tabla 2. Los sorteos (`muestras/sorteos_t4_tramo1.json`; base `{sor['base'][:8]}…`; poblaciones `{sor['poblaciones_t4_tramo1_sha256'][:8]}…`)", "",
      "| muestra | " + " | ".join(CEL) + " | total | cómo, por celda | notas | archivo | sha256 | hora |", "|---|" + "---:|" * 5 + "---|---|---|---|---|"]
for m, x in sor["muestras"].items():
    s = L(M / x["archivo"])
    como = ", ".join(f"{c} {s['celdas'][c]['como']}" for c in CEL)
    w.append(f"| {m} | " + " | ".join(str(s["celdas"][c]["n"]) for c in CEL) + f" | {s['n']} | {como} | {'; '.join(s['notas']) or '—'} | "
             f"`muestras/{x['archivo']}` | `{x['sha256']}` | {x['hora']} |")
iguales = {m: (M / x["archivo"]).read_bytes() == (M / "segunda_corrida_de_los_sorteos" / x["archivo"]).read_bytes() for m, x in sor["muestras"].items()}
sin_hora = lambda d: {k: ({kk: {a: b for a, b in vv.items() if a != "hora"} for kk, vv in v.items()} if k == "muestras" else v) for k, v in d.items()}  # noqa: E731
w.append(f"\nLa segunda corrida (`muestras/segunda_corrida_de_los_sorteos/`): las tres muestras byte a byte iguales, {all(iguales.values())}; "
         f"el índice igual salvo las horas, {sin_hora(sor) == sin_hora(sor2)}. `celdas_t4_t3f.py`: `{sor['celdas_t4_t3f_sha256'][:16]}…`, el de T3.")
w += ["", f"#### Tabla 3. El material (`muestras/material/material_t4_tramo1.json`, {mat['hora']})", "",
      "| muestra | fichas | fichas (.jsonl) | fichas (.md) |", "|---|---:|---|---|"]
for m, x in mat["muestras"].items():
    nom = m.replace(":", "_")
    a = x["archivos"]
    w.append(f"| {m} | {x['fichas']} | `{a[f'fichas_{nom}.jsonl']}` | `{a[f'fichas_{nom}.md']}` |")
c = mat["control"]
w.append(f"\nEl control, que relee lo escrito: {c['fichas']} fichas, {c['claves_vedadas']} claves vedadas, '\"estado' en los .md {c['estado_en_los_md']} "
         f"veces, texto de {c['texto_de']}, {c['sin_texto']} sin texto. La E0 con las partes es la de T3 (conjunto `{mat['e0_con_las_partes_conjunto'][:16]}…`).")
w += ["", f"#### Tabla 4. Lo que queda a la vista (`t3/muestras/unidades_a_la_vista_T4.json`, {vis['hora']})", "",
      "| muestra | material | fichas | unidades a la vista (regla 1.1) | por versión | nodos mostrados que no suman | con la regla de T3 (información) |",
      "|---|---|---:|---:|---|---|---:|"]
for m, x in vis["muestras"].items():
    ns = ", ".join(f"{k} {v}" for k, v in x["nodos_mostrados_que_no_suman"].items()) or "—"
    w.append(f"| {m} | `{x['material']}` | {x['fichas']} | {mil(x['unidades_a_la_vista'])} | {x['por_version']} | {ns} | "
             f"{mil(x['informacion_con_la_regla_de_T3'])} |")
t = vis["todas_las_muestras"]
w.append(f"| todas | — | — | {mil(t['unidades_a_la_vista'])} | {t['por_version']} | — | {mil(t['informacion_con_la_regla_de_T3'])} |")
w.append("\nPor qué suman, por muestra (una unidad puede sumar por más de una razón): " + "; ".join(
    f"{m}: " + ", ".join(f"{k} {v}" for k, v in x["por_razon"].items()) for m, x in vis["muestras"].items()) + ".")
w.append("Aristas de las fichas de (1) y de la (12) con su unidad de procedencia fuera de la lista (información): "
         + ", ".join(f"{m} {x['informacion_aristas_con_su_unidad_fuera_de_la_lista']}" for m, x in vis["muestras"].items()) + ".")
w += ["", f"#### Tabla 5. La lectura asistida: cuántas propuestas hay de cada respuesta (`lectura_asistida/lectura_asistida_t4_tramo1.json`, {la['hora']})", "",
      "| muestra | elementos | propuestas | con omisiones (aparte) | con observaciones (aparte) |", "|---|---:|---|---:|---:|"]
for m, x in la["muestras"].items():
    pr = ", ".join(f"{k} {x['propuestas'].get(k, 0)}" for k in x["respuestas_validas"] if x["propuestas"].get(k, 0)) or "—"
    w.append(f"| {m} | {x['elementos']} | {pr} | {x['con_omisiones']} | {x['con_observaciones']} |")
w.append(f"\nModelo: {la['lectura']['modelo']} (`{la['lectura']['id']}`); {la['lectura']['como']}.")
w += ["", "#### Tabla 6. Los archivos de la lectura de la autora y de la lectura asistida", "", "| archivo | sha256 |", "|---|---|"]
for rel in [f"lectura_autora/{m}.csv" for m in la["muestras"]] + ["lectura_autora/LEEME_lectura_T4.md", "lectura_autora/convertir_lectura_T4.py",
                                                                   "lectura_asistida/lectura_asistida_t4_tramo1.json",
                                                                   "lectura_asistida/omisiones_y_observaciones_t4_tramo1.md"]:
    w.append(f"| `t4/{rel}` | `{sha(T4 / rel)}` |")
w.append(f"| `t4/NO_ABRIR_conteos_t4.json` (no se abre) | `{sha(T4 / 'NO_ABRIR_conteos_t4.json')}` |")
texto = "\n".join(w) + "\n"
(T4 / "tablas_t4_tramo1.md").write_text(texto, encoding="utf-8")
print(texto)
