"""B6.1, tanda 1, T3: las tablas del FRENO T3, por script, desde los archivos de data/experiment/tanda1/t3/ (decisión 1.5 del «seguí»:
toda cifra sale por script de sus archivos). Solo lee; escribe <raíz>/data/experiment/tanda1/t3/salidas/tablas_freno_t3.md y la imprime.
Uso: python3 -I -B freno_t3_tablas.py <raíz>   (la raíz del repo, o el staging con las mismas rutas)
"""
import json
import re
import sys
from pathlib import Path

RAIZ = Path(sys.argv[1]).resolve()
T3 = RAIZ / "data/experiment/tanda1/t3"
L = lambda p: json.loads((T3 / p).read_text(encoding="utf-8"))  # noqa: E731
out = []
w = out.append

ar = L("acumulado/armado_acumulado_t3.json")
w("### Tabla 0. El acumulado y el lote de cadenas (`acumulado/armado_acumulado_t3.json`, `acumulado/manifiestos/`, "
  "`corridas/lote_t3_rc.json`)\n")
w(f"- Armado: {ar['conteos']}; manifiesto de extracción `{ar['manifiesto']['sha256']}`; orígenes: "
  f"{ {k: v['sha256'][:8] for k, v in ar['manifiestos_de_origen'].items()} }.")
for n in ("acumulado_ens_treinta_r2b", "acumulado_ens_treinta_r2b_sincola"):
    m = L(f"acumulado/manifiestos/{n}.json")
    dist = re.search(r"aquí da (\d+)", m["descripcion"])
    w(f"- `{n}.json`: {len(m['tos'])} TOs, {sum(1 for t in m['tos'] if t['nombres_remision'])} con `nombres_remision`; la "
      f"variante con la raya da {dist.group(1) if dist else '?'} distintas en el contraste del acumulado; regla: "
      f"{'con la raya' if 'así que entra' in m['descripcion'] else 'v2, sin la raya'}.")
lote = L("corridas/lote_t3_rc.json")
w(f"- Lote de cadenas: {len(lote)} corridas, códigos de salida {sorted({x['rc'] for x in lote})}.\n")

dc = L("salidas/doble_corrida_t3.json")
nombre = {"t1_veinte": "KG-Tanda1-Veinte-r2b", "t1_veinte_sincola": "KG-Tanda1-Veinte-r2b-sincola",
          "acum_treinta": "KG-Acumulado-Tandas0y1-r2b", "acum_treinta_sincola": "KG-Acumulado-Tandas0y1-r2b-sincola"}
w("### Tabla 1. Los cuatro grafos y su doble corrida (`salidas/doble_corrida_t3.json`)\n")
w("| grafo | carpeta | nodos | aristas | sha256 del kg.json (corrida 1 = corrida 2) | archivos | distintos | doble corrida interna |")
w("|---|---|---:|---:|---|---:|---|---|")
for g, v in dc["doble_corrida"].items():
    igual = "=" if v["kg_sha256"][0] == v["kg_sha256"][1] else "≠"
    w(f"| {nombre[g]} | `{v['carpeta']}` | {v['nodos']} | {v['aristas']} | `{v['kg_sha256'][0]}` {igual} | {v['archivos'][0]} / "
      f"{v['archivos'][1]} | {', '.join(v['distintos']) or '—'} (igual con las rutas normalizadas: "
      f"{v['reporte_igual_con_las_rutas_normalizadas']}) | {v['doble_corrida_interna']} |")
w("\n### Tabla 2. Reproducibilidad (`salidas/doble_corrida_t3.json`, `cadenas`)\n")
w("| cadena | sha256 del kg.json | esperado | igual | doble corrida interna |")
w("|---|---|---|---|---|")
for c in dc["cadenas"]:
    w(f"| {c['grafo']} | `{c['kg_sha256']}` | `{c['esperado']}` | {c['igual']} | {c['doble_corrida_interna']} |")
w(f"\nVeredicto del control: {'OK' if dc['ok'] else 'CON FALLAS'}.")

tg = L("salidas/tablas_gate_t3.json")
w("\n### Tabla 3. Shapes (perfil r2, fase r2b; `salidas/tablas_gate_t3.json`)\n")
w("| grafo | E0 | veredicto | PASS / FAIL / WARN | bloqueantes en FAIL | no PASS | S31 |")
w("|---|---|---|---|---|---|---|")
pares = [("veinte", "veinte_con_partes"), ("veinte_sincola", "veinte_sincola_con_partes"), ("acumulado", "acumulado_con_partes"),
         ("acumulado_sincola", "acumulado_sincola_con_partes")]
for g, gx in pares:
    for etiqueta, s in (("la del grafo", tg["grafos"][g]["nuevo"]["shapes"]), ("con las partes (informativa)", tg["extra"][gx])):
        r = s["por_resultado"]
        w(f"| {g} | {etiqueta} | {s['veredicto']} | {r['PASS']} / {r['FAIL']} / {r['WARN']} | {', '.join(s['bloqueantes_en_fail']) or '—'} | "
          f"{', '.join(f'{k} {v[0]}' for k, v in s['no_pass'].items())} | {s['S31']} |")
an = tg["grafos"]["veinte"]["anterior"]["shapes"]
w(f"\nEl grafo anterior (KG-Tanda0-Diez-r2b-rs1): {an['veredicto']}, {an['por_resultado']}, no PASS "
  f"{', '.join(f'{k} {v[0]}' for k, v in an['no_pass'].items())}; S31: {an['S31']}.")

cs = L("salidas/causa_s31_t3.json")
w("\n### Tabla 3b. La causa de S31: `remite_a` con el chunk de procedencia fuera de la E0 del grafo (`salidas/causa_s31_t3.json`)\n")
w("| grafo | remite_a | fuera de la E0 | todas de partes por corte | por chunk |")
w("|---|---:|---:|---|---|")
for g, v in cs.items():
    w(f"| {g} | {v['remite_a']} | {v['con_chunk_de_procedencia_fuera_de_la_e0']} | {v['todos_son_partes_por_corte']} | "
      f"{', '.join(f'`{k}` {n}' for k, n in v['por_chunk'].items()) or '—'} |")

cr = L("salidas/clasificacion_regresiones_t3.json")
w("\n### Tabla 4. La suite (perfil r2, generación 3; `salidas/tablas_gate_t3.json` y `salidas/clasificacion_regresiones_t3.json`)\n")
w("| grafo | entrada | resuelto / persiste / no aplica | regresiones | declaradas | no declaradas, también en el acumulado | no declaradas, solo sin los TOs de la tanda 0 |")
w("|---|---|---|---:|---:|---:|---:|")
for g in ("veinte", "veinte_sincola", "acumulado", "acumulado_sincola"):
    su = tg["grafos"][g]["nuevo"]["suite"]; c = cr[g]["por_clase"]; r = su["resumen"]
    w(f"| {g} | {su['entrada']} | {r['resuelto']} / {r['persiste']} / {r['no_aplicable']} | {su['n_regresiones']} | "
      f"{c.get('declarada', 0)} | {c.get('no declarada, también en el acumulado', 0)} | {c.get('no declarada, solo sin los TOs de la tanda 0', 0)} |")
ra = tg["grafos"]["veinte"]["anterior"]["suite_resumen"]
w(f"\nEl grafo anterior (KG-Tanda0-Diez-r2b-rs1): {ra['resuelto']} / {ra['persiste']} / {ra['no_aplicable']}.")
w("\n### Tabla 5. Las regresiones no declaradas (`salidas/clasificacion_regresiones_t3.json`)\n")
w("| ítem | esperado → medido | clase | en los acumulados | detalle (de la tanda 1 sola) |")
w("|---|---|---|---|---|")
for f in cr["veinte"]["filas"]:
    if f["clase"] != "declarada":
        w(f"| {f['item']} | {f['esperado']} → {f['medido']} | {f['clase']} | {', '.join(f'{k} {v}' for k, v in f['en_los_acumulados'].items())} | "
          f"{f['detalle'][:160].replace('|', '/')} |")

w("\n### Tabla 6. Selftests (`selftests/`)\n")
w("| selftest | rc | última línea |")
w("|---|---|---|")
for p in sorted((T3 / "selftests").glob("*.txt")):
    t = p.read_text(encoding="utf-8", errors="replace").splitlines()
    rc = next((x for x in t if x.startswith("rc=")), "sin rc")
    ult = next((x for x in reversed(t) if x.strip() and not x.startswith(("rc=", "inicio ", "fin "))), "")
    w(f"| {p.stem} | {rc} | {ult.strip()[:110].replace('|', '/')} |")
cc = L("selftests/selftest_clave_cache_t3.json")
w(f"\n`selftest_clave_cache_t3.json`: veredicto {cc['veredicto']}.")

w("\n### Tabla 7. Intrínsecas de generación 3, informativas (`intrinsecas_gen3/`)\n")
w("| grafo | E0 | rc | M4 grado medio | M9 nodos aislados | M10 chunks mudos |")
w("|---|---|---|---:|---:|---|")
for v in ("e0_del_grafo", "con_partes"):
    for n in nombre.values():
        con = (T3 / f"intrinsecas_gen3/{v}/consola_{n}.txt").read_text(encoding="utf-8").splitlines()
        rc = next((x for x in con if x.startswith("rc=")), "sin rc")
        j = T3 / f"intrinsecas_gen3/{v}/{n}.json"
        if j.exists():
            m = json.loads(j.read_text(encoding="utf-8"))["metricas"]
            m10 = m["M10_chunks_mudos"]
            w(f"| {n} | {v} | {rc} | {m['M4_average_degree']['valor']} | {m['M9_nodos_aislados_y_componentes']['valor']['nodos_aislados']} | "
              f"{m10['numerador']} / {m10['denominador']} |")
        else:
            err = next((x for x in reversed(con) if "Error" in x or "FRENO" in x), "")
            w(f"| {n} | {v} | {rc} | — | — | — ({err.strip()[:120].replace('|', '/')}) |")

ce = L("salidas/contadores_e1_t3.json")
w(f"\n### Tabla 8. Contadores de E1 (`salidas/contadores_e1_t3.json`)\n\nTotal de los 20 TOs: {ce['total']}. TOs con algún valor "
  f"distinto de 0: {sorted(t for t, v in ce['por_to'].items() if any(v.values()))}.")

texto = "\n".join(out) + "\n"
(T3 / "salidas/tablas_freno_t3.md").write_text(texto, encoding="utf-8")
print(texto)
