"""B6.1, tanda final, T3, punto 3: las tablas de los ensamblados para el FRENO, por script, desde los archivos de t3/ (la doble corrida,
la compresión, el lote, los registros del armado de los acumulados y la tabla de los `nombres_remision`). Solo lee; escribe
salidas/tablas_ensamblados_tf.md bajo <t3> y la imprime.
Uso: python3 -I -B tablas_ensamblados_tf.py <t3>
"""
import json
import sys
from pathlib import Path

T3 = Path(sys.argv[1]).resolve()
L = lambda p: json.loads(Path(p).read_text(encoding="utf-8"))  # noqa: E731
mil = lambda n: f"{n:,}".replace(",", ".")  # noqa: E731
dc, kz = L(T3 / "salidas/doble_corrida_tf.json"), L(T3 / "salidas/comprimir_kg_tf.json")
rc = L(T3 / "corridas/lote_t3_tf_rc.json")
rc_raya = L(T3 / "corridas/lote_t3_tf_tramo1_raya_rc.json")     # la primera corrida del tramo 1 con la raya
arm = {n: L(T3 / f"acumulado/armado_acumulado_{n}_tf.json") for n in ("128", "60")}
NOMBRE = {"tf98": "KG-TandaFinal-r2b", "tf98_sincola": "KG-TandaFinal-r2b-sincola", "tf_tramo1": "KG-TandaFinal-Tramo1-r2b",
          "tf_tramo1_sincola": "KG-TandaFinal-Tramo1-r2b-sincola", "acum128": "KG-Acumulado-Tandas0y1yFinal-r2b",
          "acum128_sincola": "KG-Acumulado-Tandas0y1yFinal-r2b-sincola", "acum60": "KG-Acumulado-Tandas0y1yTramo1-r2b",
          "acum60_sincola": "KG-Acumulado-Tandas0y1yTramo1-r2b-sincola"}
TOS = {"tf98": 98, "tf98_sincola": 98, "tf_tramo1": 30, "tf_tramo1_sincola": 30, "acum128": 128, "acum128_sincola": 128, "acum60": 60,
       "acum60_sincola": 60}
from datetime import datetime as D  # noqa: E402

minutos = lambda x: round((D.fromisoformat(x["fin"]) - D.fromisoformat(x["inicio"])).total_seconds() / 60, 1)  # noqa: E731
dur = {}
for x in rc:
    dur.setdefault(x["grafo"], []).append(minutos(x))
# el tramo 1 rige con la raya: su primera corrida es la del lote del tramo 1; la segunda, la de la prueba de la raya del primer lote
for g in ("tf_tramo1", "tf_tramo1_sincola"):
    r = g.replace("tf_tramo1", "tf_tramo1_raya")
    dur[g] = [minutos(next(x for x in rc_raya if x["grafo"] == r))] + dur[r]
w = [f"#### Tabla E1. Los ocho ensamblados (`salidas/doble_corrida_tf.json`, `salidas/comprimir_kg_tf.json`; el lote, "
     f"`corridas/lote_t3_tf_rc.json`: {len(rc)} corridas, rc distinto de 0 en {sum(1 for x in rc if x['rc'])}, de "
     f"{min(x['inicio'] for x in rc)[11:]} a {max(x['fin'] for x in rc)[11:]}; el del tramo 1 con la raya, "
     f"`corridas/lote_t3_tf_tramo1_raya_rc.json`: {len(rc_raya)} corridas, rc distinto de 0 en {sum(1 for x in rc_raya if x['rc'])}, de "
     f"{min(x['inicio'] for x in rc_raya)[11:]} a {max(x['fin'] for x in rc_raya)[11:]})", "",
     "| grafo | carpeta | TOs | nodos | aristas | `kg.json` (bytes) | sha256 del `kg.json` | dos corridas iguales | doble corrida interna | "
     "minutos (corrida 1, 2) |", "|---|---|---:|---:|---:|---:|---|---|---|---|"]
for g, v in dc["doble_corrida"].items():
    w.append(f"| {NOMBRE[g]} | `{v['carpeta']}` | {TOS[g]} | {mil(v['nodos'])} | {mil(v['aristas'])} | {mil(v['kg_bytes'])} | "
             f"`{v['kg_sha256'][0]}` | {v['kg_sha256'][0] == v['kg_sha256'][1] and v['mismos_nombres']} | {all(v['doble_corrida_interna'])} | "
             f"{', '.join(str(x).replace('.', ',') for x in dur[g])} |")
w.append("\nEn cada grafo, los archivos de las dos corridas son byte a byte iguales salvo `reporte_ensamblado_r2.json`, que guarda la ruta "
         "de su `--salida` y las de la raíz donde corrió; con esas rutas normalizadas, también es igual (" + ", ".join(
             f"{NOMBRE[g]} {v['reporte_igual_con_las_rutas_normalizadas']}" for g, v in dc["doble_corrida"].items()) + ").")
w += ["", f"#### Tabla E2. Los `kg.json` de más de 100 MB ({mil(kz['limite_bytes'])} bytes), comprimidos con `scripts/kg_gz.py`", "",
      "| grafo | `kg.json` (bytes) | `.gz` (bytes) | sha256 del `.gz` | zlib | restaurado byte a byte | `verificar --kg` |",
      "|---|---:|---:|---|---|---|---|"]
for g, r in kz["grafos"].items():
    if r["pasa_de_100_MB"]:
        w.append(f"| {NOMBRE[g]} | {mil(r['kg_bytes'])} | {mil(r['sello']['gz_bytes'])} | `{r['sello']['gz_sha256']}` | {r['sello']['zlib']} | "
                 f"{r['restaurado_igual_byte_a_byte']} | rc {r['verificar']['rc']} |")
w.append("\nLos demás quedan sin comprimir: " + ", ".join(f"{NOMBRE[g]} ({mil(r['kg_bytes'])} bytes)" for g, r in kz["grafos"].items()
                                                         if not r["pasa_de_100_MB"]) + ". Ningún otro archivo de los ensamblados pasa "
         "de 50 MB. Manda el sha256 del `kg.json` sin comprimir (tabla E1); el sello de cada `.gz` lo repite.")
w += ["", "#### Tabla E3. La reproducibilidad de los sellados (`salidas/doble_corrida_tf.json`, `cadenas`)", "",
      "| cadena | sha256 del `kg.json` | sello | igual | doble corrida interna |", "|---|---|---|---|---|"]
for c in dc["cadenas"]:
    w.append(f"| {c['grafo']} | `{c['kg_sha256']}` | `{c['esperado'][:16]}…` | {c['igual']} | {c['doble_corrida_interna']} |")
w.append("\nLos sellos: los seis de la tanda 0 de `resellado_t0/FRENO_resellado_T0.md:68-71` (las dos r2a, por su prefijo) y los cuatro "
         "de la tanda 1 de `tanda1/t3/FRENO_T3.md:32-35`.")
w += ["", "#### Tabla E4. El tramo 1 con la raya contra la variante con los manifiestos de T1, y el acumulado de 60 contra la prueba de la mesa", ""]
for g, v in dc["raya_tramo1"].items():
    d1 = v["variante_T1_doble_corrida"]
    w.append(f"- **{NOMBRE[g.replace('_raya', '')]}** (con la raya, la que rige) contra la variante con los manifiestos de T1 (la del FRENO "
             f"parcial): `kg.json` igual: {v['kg_igual']} (`{v['kg_sha256'][0][:16]}…`); archivos distintos: {', '.join(v['distintos']) or 'ninguno'}; "
             f"TOs con `nombres_remision` distintos entre los dos manifiestos: {len(v['tos_con_nombres_distintos_entre_los_manifiestos'])}. La "
             f"variante de T1, en sus dos corridas: `kg.json` igual {d1['kg_sha256'][0] == d1['kg_sha256'][1]}, distintos {', '.join(d1['distintos']) or 'ninguno'}.")
a = dc["acumulado_60_contra_la_mesa"]
for g in ("acum60", "acum60_sincola"):
    w.append(f"- **{NOMBRE[g]}**: {mil(a[g]['nodos'][0])} nodos y {mil(a[g]['aristas'][0])} aristas; la mesa (registro, §43), "
             f"{mil(a[g]['nodos'][1])} y {mil(a[g]['aristas'][1])}: igual {a[g]['igual']}.")
n = a["nombres_remision"]
w.append(f"- Los `nombres_remision` del manifiesto de T3 contra los de los manifiestos que usó la mesa ({', '.join(f'`{x}`' for x in n['manifiestos_de_la_mesa'])}): "
         f"{n['tos']} TOs, {n['tos_en_los_de_la_mesa']} en los de la mesa, {len(n['tos_con_nombres_distintos'])} distintos.")
w += ["", "#### Tabla E5. El armado de los acumulados (`acumulado/armado_acumulado_<n>_tf.json`)", "",
      "| acumulado | TOs (0 / 1 / final) | archivos de la E0 | archivos de la entrada | bytes de la entrada | todos iguales al origen | "
      "manifiesto de extracción |", "|---|---|---:|---:|---:|---|---|"]
for k, r in arm.items():
    c = r["conteos"]
    w.append(f"| {k} | {c['tos']} ({c['tanda0']} / {c['tanda1']} / {c['tanda_final']}) | {c['archivos_e0']} | {mil(c['archivos_entrada'])} | "
             f"{mil(c['bytes_entrada'])} | {c['todos_iguales_al_origen']} | `{r['manifiesto']['sha256'][:16]}…` |")
w.append("\nLa entrada combinada se registra solo por su total de archivos, sus bytes y el sha256 de su lista (cegamiento, punto 8): no "
         "va al repo, porque es la salida de la extracción por copia.")
texto = "\n".join(w) + "\n"
(T3 / "salidas/tablas_ensamblados_tf.md").write_text(texto, encoding="utf-8")
print(texto)
