"""B6.1, tanda final, T3: arma el FRENO T3 final por script (pre-registro de la tanda final, §7: toda cifra del FRENO por script desde sus
archivos), con freno_t3_parcial_armar_tf.py como modelo, después de las decisiones de la autora sobre el FRENO T3 parcial. Las tablas que
vienen de una salida (tablas_ensamblados_tf.md, tabla_nombres_t3_tf.md, veredicto_gate_tf.md, tablas_contado_tf.md, tablas_t4_tf.md y la
sección de la foto) van tal cual; la salida del paso 0 y del control del comienzo de esta parte, tal como las dio la consola (con el
scratchpad y la carpeta personal reemplazados). Las demás cifras del texto se leen acá de sus JSON. Solo lee <t3> y lo que se le pasa;
escribe <salida.md> (fuera del repo).
Uso: python3 -I -B freno_t3_armar_tf.py <t3> <paso0.json> <paso0_seguir.txt> <seccion_foto.md> <foto.json>
       <grep redactado.json,grep generado.json> <escrituras.json,...> <apartados.json,...> <git_index antes.txt,git_index cierre.txt>
       <salida.md>
"""
import json
import sys
from pathlib import Path

T3 = Path(sys.argv[1]).resolve()
PASO0, SEGUIR, FOTO, FOTOJ, GREP, ESC, APA, GITIX, OUT = (Path(x) for x in sys.argv[2:11])
L = lambda p: json.loads(Path(p).read_text(encoding="utf-8"))  # noqa: E731
txt = lambda p: Path(p).read_text(encoding="utf-8").rstrip("\n")  # noqa: E731
mil = lambda n: f"{n:,}".replace(",", ".")  # noqa: E731
GD, SA, NE, CS, MU = T3 / "gate_decisiones", T3 / "salidas", T3 / "neo4j", T3 / "conteos_sin_leer", T3 / "muestras"
ve, fg, dg = L(GD / "veredicto_gate_tf.json"), L(GD / "fuera_del_grafo_tf.json"), L(GD / "diagnostico_clave_cache_tf.json")
cf, ep, cg = L(GD / "control_fixture_tf.json"), L(GD / "e0_partes_tf.json"), L(GD / "comparar_gate_tramo1_tf.json")
dc, nr = L(SA / "doble_corrida_tf.json"), L(T3 / "nombres_remision/tabla_nombres_t3_tf.json")
rc = L(T3 / "corridas/lote_t3_tf_rc.json") + L(T3 / "corridas/lote_t3_tf_tramo1_raya_rc.json")
sc = L(T3 / "selftests/clave_cache/resumen_sin_cuentas_t3.json")
sha_orig = txt(T3 / "selftests/clave_cache/sha256_selftest_clave_cache_originales_t3.txt")
dry, ccn = L(NE / "dry_registro_tf.json"), L(NE / "control_cola_neo4j_tf.json")
carga = {k: L(NE / k / "carga_neo4j_tanda0.json")["grafos"][k] for k in ("KG_TandaFinal_r2b", "KG_TandaFinal_r2b_sincola")}
equiv = {k: L(NE / k / "carga_neo4j_tanda0.json")["equivalencia"] for k in carga}
sha_c = [[x.split()[0] for x in txt(NE / n).splitlines()[1:]] for n in ("sha_cargador_antes.txt", "sha_cargador_despues.txt")]
d_arranque, d_cierre, d_antes = (txt(NE / "consolas" / n) for n in ("consola_docker_arranque.txt", "consola_docker_cierre.txt",
                                                                    "consola_docker_antes.txt"))
cs = L(CS / "contado_sin_leer_tf.json")
p1, p2, um = L(MU / "poblaciones_t4_t3f_tf.json"), L(MU / "poblaciones_t4t1_tf.json"), L(MU / "umbrales_t4_tf.json")
s1, s2, cm, vis = L(MU / "sorteos_t4_t3f_tf.json"), L(MU / "sorteos_t4t1_tf.json"), L(MU / "control_material_tf.json"), L(MU / "unidades_a_la_vista_T4.json")
cola = L(MU / "cola.json")
foto = L(FOTOJ)
grep, grep_gen = (L(x) for x in str(GREP).split(","))
_esc = [(Path(x).stem, L(x)) for x in str(ESC).split(",")]
esc = {"nuevos": sum(e["nuevos"] for _, e in _esc), "cambian": sum(e["cambian"] for _, e in _esc),
       "escritos": {k: v for _, e in _esc for k, v in e["escritos"].items()}, "por_etapa": {n: (e["nuevos"], e["cambian"]) for n, e in _esc}}
_apa = [(Path(x).stem, L(x)) for x in str(APA).split(",")]
gi_antes, gi_cierre = (Path(x).read_text(encoding="utf-8").split() for x in str(GITIX).split(","))
gi_igual = [x for x in gi_antes if len(x) == 16] == [x[:16] for x in gi_cierre if len(x) == 64]
P = L(PASO0)
paso0_estado = P["T3 step 0: repo state, commits, 78 routes"].strip("\n")
paso0_t1 = P["Regenerate T1 derived preregistro from 4de7f2a7, check inputs"].strip("\n")
paso0_docker = next(x for x in P["Inspect tanda1 T3 photo script and check Docker"].splitlines() if "Docker" in x)
paso0_vol = P["Check Neo4j volume unchanged since T2 by size and date"].strip("\n")
paso0_foto = P["Take T3 pre-snapshot, .pyc count, update checkpoint"].strip("\n")
seguir = txt(SEGUIR)
derivada = [T3.parents[0] / "preregistro" / n for n in ("preregistro_tanda_final_derivada_T4.md", "preregistro_tanda_final_derivada_T4.huecos.json")]
import hashlib  # noqa: E402
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()  # noqa: E731
na_sha = esc["escritos"]["data/experiment/tanda_final/t3/NO_ABRIR_conteos_t3.json"]["sha256"]
import subprocess  # noqa: E402
_rel_base = "data/experiment/tanda1/t3/conteos_sin_leer/contado_sin_leer_t3f.json"
_repo = T3.parents[3]
base_t1_igual = hashlib.sha256(subprocess.run(["git", "-C", str(_repo), "show", f"eb0711a1:{_rel_base}"], capture_output=True,
                                              check=True).stdout).hexdigest() == sha(_repo / _rel_base)
g = ve["grafos"]
acum = [k for k, v in fg["grafos"].items() if not v["tanda_sola"]]
sola = [k for k, v in fg["grafos"].items() if v["tanda_sola"]]
n_reg = {k: v["suite"]["regresiones"] for k, v in g.items()}
s31_repo = sorted(k for k, v in g.items() if "S31" in v["shapes_e0_del_grafo"]["bloqueantes_en_fail"])
partes = {n: e["corridas"][0]["reemplazos"] for n, e in ep["e0_con_partes"].items()}
raya = dc["raya_tramo1"]["tf_tramo1_raya"]
nf = nr["filas"]
dif_suite = sorted({n for k, r in cg.items() for n, v in r["archivos"].items() if not v["byte_a_byte"]})
dif_shapes = [k for k, r in cg.items() if all(v["byte_a_byte"] for n, v in r["archivos"].items() if n.startswith("shapes"))]
vt = vis["todas_las_muestras"]
unidades_e0 = cs["grafos"]["tf98"]["unidades_e0_r2b"]
c_cola = cs["grafos"]["tf98"]["cola"]

F = f"""# FRENO T3 — tanda final de B6.1: los ocho ensamblados, el gate (pasa con las decisiones de la autora), el registro y Neo4j, lo contado sin leer y la preparación de T4 (USD 0, sin API, sin commit)

Rigen el pre-registro de la tanda final FIRMADO (`docs/preregistro_tanda_final.md`, firma en `4de7f2a7`, con sus notas posteriores en
`27bfaeb5` y `86541475`), sus §2, §5, §6, §7 y §8 y la precisión de la firma, lo del pre-registro de la tanda 1 que este no reemplaza, el
«seguí» de T3 con sus tres correcciones y las cinco decisiones de la autora sobre el FRENO T3 parcial (sección 2), que mandan sobre el
«seguí». HEAD `eb5ad14b`. El FRENO parcial queda como `t3/FRENO_T3_parcial.md` (`f7abf9da…`), sin cambios. Toda cifra de este FRENO sale
de un script de `t3/scripts/` y de su salida; la sección 12 los lista.

**Resultado:**
- **Los ocho ensamblados** (punto 3) salen con rc 0 en las {len(rc)} corridas de los dos lotes, la doble corrida de cada uno da el mismo
  `kg.json`, los diez grafos sellados de las tandas 0 y 1 se reproducen byte a byte y el acumulado con el tramo 1 da las cifras de la prueba
  de la mesa (tablas E1 a E5). El tramo 1 va con la variante con la raya (decisión 2); su `kg.json` es el de la variante de T1.
- **El gate** (punto 4) **pasa**, con las decisiones de la §29 y la R23 y la V23 del selftest de claves declaradas no aplicables después de
  T2 (decisión 1): shapes pasa en los ocho con la E0 con las partes; la suite da 0 regresiones no declaradas que cuenten; los selftests de la
  cadena dan rc 0; sin la R23 y la V23, el de claves es igual a A3 en todo lo demás.
- **El registro y Neo4j** (punto 5): dos entradas nuevas en `grafos.py` y el registro de la vista; los dos grafos de la tanda, cargados con
  el envoltorio en memoria, con el gate 5 OK, la paridad 147 de 147 y 0 nodos con la marca de la cola en el sin cola. El cargador no cambió.
- **Lo contado sin leer** (punto 6): tablas C1 a C4, con la tanda 1 y la tanda 0 al lado, y la columna «Tanda final» del tablero.
- **La preparación de T4** (punto 7): las ocho muestras en dos corridas iguales; la cola, {cola['n']} = las {sum(cola['celdas'][c]['n'] for c in ('RI:sin_raiz', 'RI:resto', 'NG:sin_raiz'))} del tramo 1 enteras y {cola['celdas']['NG:resto']['n']} de
  NG resto; la versión derivada de la lectura, sin ningún `⟦T4.`.
- Nada commiteado y ningún mensaje de commit preparado.

## 1. Paso 0 (20/10/2026, desde las 10:02:13) y el control del comienzo de esta parte (13:51:19)

La salida, tal cual, con la carpeta personal como `$HOME` y el scratchpad como `<SCRATCHPAD>`.

```
{paso0_estado}
```

La versión derivada de T1, regenerada con el completador sobre el pre-registro de `4de7f2a7` (`git show` al scratchpad), y las entradas
en HEAD (los cuatro manifiestos de ensamblado de T1 y la E0 de los 98):

```
{paso0_t1}
```

Docker y el volumen de Neo4j del repo (por tamaño y fecha, contra la foto de después de T2), y la foto del repo antes, con la cuenta de los
`.pyc`:

```
{paso0_docker}
{paso0_vol}
{paso0_foto}
```

En la foto de antes: sus horas y sus entradas, la cuenta de los `.pyc`, el sha256 de la foto, el commit de HEAD y la escritura del
checkpoint. La salida de las entradas en HEAD termina con la cuenta de los renglones OK de `t1/sha256_para_T2.txt`.

Al empezar esta parte, después de las decisiones sobre el FRENO parcial: el estado del repo, los procesos, la foto contra la de después del
parcial y Docker (los dos renglones de `pgrep` son de un proceso que no lancé yo, que escribe fuera del repo; no lo toqué):

```
{seguir}
```

## 2. Lo decidido sobre el FRENO parcial y cómo lo apliqué

1. **El selftest de claves.** La R23 del perfil r2b y la V23 del sellado quedan declaradas no aplicables después de T2: su TO ya se extrajo y
   su clave está en la caché, no por el código de la clave. El gate se juzga sin ellas, con todo lo demás igual a A3. Lo comprobé por script
   (`diagnostico_clave_cache_tf.py`, sección 4.4): los campos que difieren de A3 son de la R23 o derivan de ella, y la fila del contraste que
   difiere es la {', '.join(f"{v['fila']} (de {v['variacion']})" for v in dg['filas_de_la_tabla_que_difieren'].values())}. No toqué el selftest.
2. **Los manifiestos del tramo 1:** la variante con la raya, por la regla de la §19 y la enmienda 9, punto 8, que nombra el pre-registro
   (§7). **Se declara que el «seguí» decía los manifiestos de T1.** Los dos grafos del tramo 1 se ensamblaron de nuevo con los manifiestos de
   la raya (`t3/prueba_raya_tramo1/manifiestos/`, la carpeta de la prueba del parcial, que pasan a regir): la primera corrida, en la carpeta
   final; la segunda es la de la prueba de la raya del parcial. El `kg.json` es el mismo que con los de T1 (tabla E4). Rehíce lo que depende
   del manifiesto: el gate del tramo 1 (shapes, byte a byte igual; en la suite solo cambia la ruta del manifiesto que nombra T6), sus
   intrínsecas (las mismas métricas) y la medición de los nombres (los cuatro manifiestos siguen la §19).
3. **El derivador adaptado del acumulado de 60** queda, declarado, con mi medición al lado de las cifras de la mesa (sección 3.1).
4. **Los umbrales del punto 7.3:** los del script de la mesa, importado sin cambios, con su tasa base, la de la tanda 0, como dice el §6. Las
   cifras del T4 de la tanda 1 van al lado como línea de base informativa (tabla T4 y `umbrales_t4_tf.json`).
5. **`unidades_a_la_vista_T4.json`:** la regla del «seguí», con la del T4 de la tanda 1 al lado (tabla T7).

Las tres correcciones del «seguí» siguen: las poblaciones de los elementos del grafo, sobre `ens_98_r2b_sincola` (su ruta y su sha256, en la
tabla T1); el mecanismo de (1), (3) y la (12), el del T4 de la tanda 1 (`poblaciones_t4t1_tf.py` y `sorteos_t4t1_tf.py`); y la cola, en 30,
con las 13 del tramo 1 enteras y 17 de NG resto (tabla T2).

## 3. Los ocho ensamblados (punto 3)

El mecanismo es el del T3 de la tanda 1, copiado y adaptado en `t3/scripts/`: `armar_acumulados_tf.py` arma por copia la E0 y la entrada
de los dos acumulados en una copia del repo (la del `rsync` del «seguí», con 0 nombres vedados y 0 enlaces); `cadena_t3_tf.sh` corre
`ensamblar_tanda0.py` con los argumentos de las corridas del T3 de la tanda 1; `correr_lote_t3_tf.py` corre las cadenas; `doble_corrida_tf.py`
compara. La tanda va con los manifiestos de T1; el tramo 1, con los de la raya; los dos, con `--entrada
data/experiment/reextraccion_v2/corpus_tanda_final/salida_r2b` y la E0 de los 98. La unidad con error de T2
(`ri_transpa::Sbloque1::chapeau_seccion`) falta en los grafos, como decidió la autora (registro, §44): no la toqué.

{txt(SA / 'tablas_ensamblados_tf.md')}

### 3.1 Los `nombres_remision` de los ensamblados nuevos, medidos (§7; registro, §19; enmienda 9, punto 8)

`medir_nombres_t3_tf.py` es la medición de la mesa (`nombres_remision/medir_nombres_remision_mesa.py`) con los cuatro corpus nuevos; el
contraste y el resumen son los de la mesa, sin cambios. Todo corrió sobre la copia. `tabla_nombres_t3_tf.py` pone las cifras de la mesa al
lado (las del 16/10/2026 del repo, y las de la enmienda 9, punto 8, `756a0394:81-84`, para el tramo 1 y el acumulado de 60):

{txt(T3 / 'nombres_remision/tabla_nombres_t3_tf.md')}

Iguales a la mesa en los cuatro: {nr['todas_iguales_a_la_mesa']}; la variante de cada manifiesto sigue la §19 en los cuatro:
{all(x['manifiesto_sigue_la_19'] for x in nf.values())}. El manifiesto del acumulado de 128 lo derivó `derivar_manifiesto_ensamblado_mesa.py` con el
contraste de la mesa. Para el de 60, ese derivador frena porque la medición del repo no tiene un corpus con esos TOs: lo derivé con
`derivar_manifiesto_ensamblado_tf.py`, que hace lo mismo con la variante que da la fuente que se le pasa (`756a0394:83-84`: 23 distintas, la
raya no entra) y escribe esa fuente en la `descripcion` (decisión 3). La medición de arriba da la misma cifra.

## 4. El gate (punto 4)

Sobre la copia del repo, con las decisiones del gate de la tanda 1 (registro, §29) y la decisión 1. Los `--out` van a `t3/gate/` (el
«seguí» lo pide así; en la tanda 1 fueron a las carpetas de los ensamblados).

{txt(GD / 'veredicto_gate_tf.md')}

### 4.1 Shapes

- Con la E0 con las partes (`e0_partes_tf.py`, que corre `reext_t0/t3/e0_con_partes.py` sin cambios, dos veces por E0): pasa en los ocho.
  La tanda final no tuvo unidades partidas (su E0 con las partes es la E0 del repo: {ep['controles']['tanda_final_igual_a_la_e0_del_repo']}); en los acumulados entran
  las partes de las tandas 0 y 1 ({', '.join(f'{u} en {len(v)} partes' for x in partes['acum128'].values() for u, v in x.items())}).
- Con la E0 de cada grafo: S31 falla en {len(s31_repo)} grafos, los acumulados, por las `remite_a` de las partes por corte de `ri_rml::Sbloque14`,
  de la tanda 1 (tabla V2). En los cuatro de la tanda final, S31 pasa también con la E0 del repo.
- El tramo 1 con la raya contra la variante de T1 (`comparar_gate_tramo1_tf.py`): shapes, byte a byte igual con las dos E0 ({len(dif_shapes)} de
  {len(cg)} carpetas); en la suite cambian solo {', '.join(f'`{n}`' for n in dif_suite)}, por la ruta del manifiesto que nombra T6.

### 4.2 La suite y la fixture

- **La fixture** (`editar_fixture_tf.py`, sobre la copia): ocho entradas nuevas al final de `estado_esperado`, copias de la entrada sellada
  del grafo anterior del mismo tipo de la tanda 1 (KG-Tanda1-Veinte-r2b para la tanda y el tramo 1; KG-Acumulado-Tandas0y1-r2b para los
  acumulados, completo o sin cola). El script controla que las expectativas de esas cuatro y de las dos de diez de la tanda 0 re-sellada son
  las mismas. El tramo 1 con la raya tiene el mismo `kg.json`, así que la fixture no cambió.
- **El control de la precisión de la firma, punto 3** (`control_fixture_tf.py`, contra `git show HEAD:`): {mil(cf['claves_de_HEAD'])} claves de HEAD,
  {cf['quitadas']} quitadas y {cf['cambiadas']} cambiadas; {mil(cf['claves_nuevas'])} claves nuevas, todas de las ocho entradas: {cf['son_las_ocho']}. Veredicto: {'OK' if cf['ok'] else 'CON FALLAS'}.
- **El resultado:** en los acumulados, {n_reg[acum[0]]} regresiones en cada uno, las tres del laudo y E4-a1 y E4-a4, declaradas; en la tanda y en el
  tramo 1, {n_reg[sola[0]]} en cada uno, todas fuera del grafo (`fuera_del_grafo_tf.py`). El cruce: en los cuatro, las no declaradas fuera del
  grafo son las no declaradas que su acumulado no da ({fg['cruce'][sola[0]]['cuantos'][0]} y {fg['cruce'][sola[0]]['cuantos'][1]} ítems, iguales: {all(x['iguales'] for x in fg['cruce'].values())}).

### 4.3 La reproducibilidad, los selftests de la cadena, las intrínsecas y los contadores

Las tablas E3 y V3. Los selftests de la cadena corrieron sobre un clon APFS de la copia (`selftests_tf.sh`, con 0 nombres vedados y 0
enlaces). El del catálogo pide `git show 4ef7650:<ruta>` (`derivar_catalogo_r2.py:103`): corrió con `GIT_DIR` en el `.git` del repo y
`GIT_OPTIONAL_LOCKS=0`, en lugar del `git clone` del T3 de la tanda 1, que trajo archivos `.env` y `NO_ABRIR_` al clon. El sha256 de
`.git/index` y de `.git/HEAD` antes de los selftests y al cerrar el parcial ({gi_cierre[0]} {gi_cierre[1]}), por sus primeros 16 caracteres:
iguales, {gi_igual}. Las intrínsecas con la E0 de cada grafo corren en los cuatro de la tanda final y frenan solas en los cuatro acumulados
(«Atribución gen 3 inválida»: las partes por corte no están en esa E0), como en la tanda 1.

### 4.4 El selftest de claves: la R23 y la V23, declaradas

- **Cómo corrió:** `selftest_clave_cache --salida-r2b data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b`, como en A3 y en T1, sobre el
  clon, con su JSON y su consola a archivos que no abrí; `selftest_claves_sin_cuentas_tf.py` (el de T1 con los nombres de T3) les sacó las
  cuentas con `alcance_e1/a3/scripts/clave_cache_sin_cuentas_a3.py` y las comparó con las de A3 sin cuentas. Los sha256 de las dos
  originales:

```
{sha_orig}
```

- **Lo que dio:** rc 1. Las dos salidas sin cuentas no son las de A3 (JSON igual: {sc['json_igual_al_de_a3_sin_cuentas']}; consola igual:
  {sc['consola_igual_a_la_de_a3_sin_cuentas']}), así que el script las renombró a `NO_ABRIR_` y no las abrí. Las rutas de los {len(dg['rutas_que_difieren_de_A3_sin_cuentas'])} campos del JSON
  que difieren, sin valores: {', '.join(f'`{r}`' for r in dg['rutas_que_difieren_de_A3_sin_cuentas'])}.
- **La causa** (`diagnostico_clave_cache_tf.py`, que lee solo esas rutas, el código del selftest y su tabla, el manifiesto de la tanda final
  y las dos E0; ni las salidas del selftest ni las bases de la caché):
  - todos esos campos son de la variación del TO nuevo o derivan de ella: {dg['todas_en_la_variacion_del_TO_nuevo_o_derivadas']}. Es `{', '.join(dg['funciones_con_clave_en_cache_e1'])}`, la única
    función del selftest con el campo `clave_en_cache_e1`: V23 en el perfil sellado y R23 en el r2b; la fila del contraste que difiere es la
    {', '.join(f"{v['fila']}, de {v['variacion']}" for v in dg['filas_de_la_tabla_que_difieren'].values())} (leída con `leer_tabla` y `RE_IDS_TABLA` del propio selftest);
  - supone que `{dg['UNIDAD_TO_NUEVO']}` (de la partición b584) no está en la caché de E1 (miss); `{dg['TO_NUEVO']}` es de la tanda final
    ({dg['lugar_en_orden_corrida']}.º de `orden_corrida`, tramo {dg['tramo']}), y su chunk es el mismo en la E0 de la tanda final y en b584: {dg['chunk_igual_en_las_dos']}. T2 lo extrajo con el
    perfil r2b, así que la clave de R23 está en la caché;
  - en T1 el selftest dio OK (FRENO T1, §4.1) porque T2 todavía no había extraído ese TO. El código de la clave (`llm_cache.py`,
    `cliente_e1.py` y `cliente_e3.py`) está entre las 78 rutas, que el paso 0 dio iguales; el selftest no está entre ellas y es el de HEAD.
- **Con la decisión 1:** sin la R23 y la V23, todo lo demás es igual a A3: {ve['clave_cache_sin_R23_y_V23']}. El cambio del TO de la variación lo hace la mesa
  aparte.
- **El cegamiento:** saber si una clave de E1 está en la base es un dato de la caché de E1; no di cuentas de claves ni nada de E3. Las dos
  salidas sin cuentas quedan como `NO_ABRIR_` en `t3/selftests/clave_cache/`, sin abrir; las dos originales, con las cuentas, quedan en el
  scratchpad, sin abrir, y van solo por su sha256.

## 5. El registro y Neo4j (punto 5)

- **`grafos.py`** (`editar_grafos_tf.py`, sobre la copia): dos entradas nuevas al final, `KG_TandaFinal_r2b` y `KG_TandaFinal_r2b_sincola`, con
  label, índice y `ev2_key` propios y `commit_sellado` «PENDIENTE»; el sha256, los nodos y las aristas salen de la doble corrida. Las selladas
  no cambian: el script controla el texto antes y después del ancla, y la corrida en seco, cada entrada sellada ({len(dry['grafos_py_selladas_iguales'])}, iguales:
  {all(dry['grafos_py_selladas_iguales'].values())}; solo dos nuevas: {dry['grafos_py_solo_dos_nuevas']}).
- **El registro de la vista** (`t3/registro_vista_r2b_tanda_final.py`, con el patrón del de la tanda 1), con el desglose de «punto sin nodos»
  del sin cola recomputado; la cola de la tanda final para ese desglose: {c_cola['cola']} unidades.
- **La corrida en seco** (`dry_registro_tf.py`, por el camino de imports del cargador, sin Neo4j): {'OK' if dry['ok'] else 'CON FALLAS'}; en los dos, sha256
  verificado y la vista con los conteos del registro ({'; '.join(f"{k}: {mil(v['vista_nodos'])} / {mil(v['vista_aristas'])}" for k, v in dry['grafos'].items())}); el desglose,
  igual a lo declarado: {all(v['igual_a_lo_declarado'] for v in dry['desglose'].values())}.
- **El cargador** (`cargar_neo4j_tanda0.py`) acepta en `--grafo` solo las claves `KG_Tanda0_*`. Como en el T3 de la tanda 1 (pre-registro, §7),
  `cargar_neo4j_tf.py` lo importa sin editarlo, deja en memoria `CLAVES_TANDA0` con las dos claves de la tanda final y llama a su `main()`
  una vez por clave. Su sha256, antes y después de la carga, en el repo y en la copia: `{sha_c[0][0][:16]}…` y `{sha_c[1][0][:16]}…`; iguales: {sha_c[0] == sha_c[1]}.
  Las salidas heredan los rótulos de la tanda 0 (`carga_neo4j_tanda0.json`, «PARIDAD (tanda 0)»), que no se corrigen.
- **La carga** (`neo4j/<clave>/carga_neo4j_tanda0.json`), desde la copia:"""
for k, x in carga.items():
    F += (f"\n  - {k}: sha256 verificado antes de cargar ({x['sha256_archivo'] == x['sha256_registro']}); {mil(x['carga_1']['nodos'])} nodos y "
          f"{mil(x['carga_1']['aristas_creadas'])} aristas, {x['carga_1']['aristas_colgantes']} colgantes; dos cargas con la misma huella: {x['idempotente']}; "
          f"`verificar_carga`: {x['verificar_carga_ok']}; `KG_Meta.kg_sha256` igual al archivo: {x['kg_meta_sha_igual_archivo']}, `commit_sellado` "
          f"«{x['kg_meta']['commit_sellado']}»; paridad {equiv[k]['paridad_total']}; **gate 5: {'OK' if x['ok'] else 'CON FALLAS'}**.")
F += f"""
- **El control de la cola** (`control_cola_neo4j_tf.py`, la copia del de la tanda 1 con las claves cambiadas): {'OK' if ccn['ok'] else 'CON FALLAS'}. En el sin cola,
  {ccn['grafos']['KG_TandaFinal_r2b_sincola']['neo4j_nodos_cola_humana_true']} nodos con la marca en Neo4j y {ccn['grafos']['KG_TandaFinal_r2b_sincola']['kg_nodos_con_marca']} en el `kg.json`; en el completo, llegan las {ccn['grafos']['KG_TandaFinal_r2b']['kg_nodos_con_marca']} marcas de
  nodo del `kg.json` ({ccn['grafos']['KG_TandaFinal_r2b']['neo4j_nodos_con_cola_humana_en_props_json']} en Neo4j).
- **Docker** (las consolas, en `neo4j/consolas/`). Al empezar respondía, con los contenedores de otro proyecto corriendo. Levanté el
  contenedor del repo con `docker compose up -d --wait` en `data/experiment/neo4j/` y, al terminar, lo detuve con `docker compose stop`. A
  diferencia de la tanda 1, no pedí el cierre de Docker: estaba corriendo antes y lo dejé como estaba. El contenedor del repo salió con el
  código 137 (`docker compose stop` lo terminó al pasar su espera), con la carga ya verificada. El arranque y el cierre:

```
{d_arranque}
```

```
{d_cierre}
```

## 6. Lo que se cuenta sin leer (punto 6)

`contado_sin_leer_tf.py`, sobre la copia, es el del T3 de la tanda 1 con los grafos de la tanda final (la tanda y el acumulado de las tres,
completos y sin cola); importa sin editarlas las funciones de la tanda 0 y del re-sellado. La línea de base es la de la tanda 1 (su
`contado_sin_leer_t3f.json`, igual al de `eb0711a1`: {base_t1_igual}), con la de la tanda 0 al lado. Las cuentas bajo el cegamiento van a
`t3/NO_ABRIR_conteos_t3.json`, sin abrir: sha256 `{na_sha}`. La columna «Tanda final» del tablero está en
`t3/conteos_sin_leer/columna_tanda_final_tablero_tf.md`; el tablero del repo no se tocó.

{txt(CS / 'tablas_contado_tf.md')}

## 7. La preparación de T4 (punto 7)

{txt(MU / 'tablas_t4_tf.md')}

- **El control del material** (`control_material_tf.py`, con el de material_t4t1.py sobre las ocho muestras): claves del estado o de las marcas
  de E3, {sum(v['claves_vedadas'] for k, v in cm.items() if k != 'ok')}; fichas sin texto, {sum(v['sin_texto'] for k, v in cm.items() if k != 'ok')}; `.md` con «"estado», {sum(v['estado_en_el_md'] for k, v in cm.items() if k != 'ok')}. No leí ninguna ficha.
- **La segunda corrida de los sorteos** (`muestras/segunda_corrida_de_los_sorteos/`) da las ocho muestras byte a byte iguales; los índices
  cambian solo en las horas.
- **La versión derivada de la lectura** (7.7), con el completador sobre el pre-registro de `4de7f2a7` y `--momento lectura_tramo1`: sin ningún
  `⟦T4.` (espera solo el hueco de T5), regenerada al final igual byte a byte. `preregistro/preregistro_tanda_final_derivada_T4.md`
  (`{sha(derivada[0])}`) y su `.huecos.json` (`{sha(derivada[1])}`).
- **Los dos momentos de lectura del §6 se juntan en uno**, porque T2 siguió de corrido y nada se leyó al cerrar el tramo 1: la atención propia
  de RI y la atención y el freno de cada estrato se calcularon acá, antes de leer nada. Va en lugar de la frase del §6 «se calculan después
  de leer las celdas del tramo 1».

## 8. El cegamiento (punto 8)

- No miré ni di el desglose de las aceptadas por estado de E3, `n_reintentos`, `reintentos_e3.jsonl`, `copias_nota_e3.jsonl`, las `marcas_e3`
  ni el gasto de los reintentos. La cola y su composición por estado van en la tabla C3, como en la tanda 1.
- De la salida de la extracción, ninguna cuenta por tipo de archivo. La entrada de los acumulados se registra solo por su total de archivos,
  sus bytes y el sha256 de su lista (tabla E5). La E0 con las partes informa las unidades partidas por corte, que son de E1.
- Los `NO_ABRIR_` de esta unidad: `t3/NO_ABRIR_conteos_t3.json` y los dos del selftest de claves (sección 4.4). No abrí ninguno, ni ningún
  `.env`, ni ninguna carpeta vedada.

{txt(FOTO).replace("## 7. La foto", "## 9. La foto", 1)}

**Lo que se escribió en el repo** (`escribir_en_el_repo_tf.py`, desde un staging armado en el scratchpad; antes, cada ruta nueva no existía
y cada archivo que cambia era el de HEAD; después, cada archivo es byte a byte el del staging): {', '.join(f'{n.replace("escritura_", "")} {mil(a)} nuevos' + (f' y {b} que cambia' if b else '') for n, (a, b) in esc['por_etapa'].items())};
escritos iguales al staging: {mil(sum(v['igual_al_staging'] for v in esc['escritos'].values()))} de {mil(len(esc['escritos']))}. Lo del parcial que se reemplazó (el tramo 1 y las salidas del gate)
salió antes con `escribir_en_el_repo_tf.py apartar`, que controla que cada archivo sea el que se escribió y no esté en HEAD: {', '.join(f'{n.replace("apartar_", "")} {mil(len(a["movidos"]))} de {mil(a["archivos"])}' for n, a in _apa)}; quedan en el
scratchpad. El FRENO parcial pasó a `t3/FRENO_T3_parcial.md`, con el mismo sha256. Escritos después de la foto de después: este FRENO y
`t3/resumen_fotos_T3.json`.

**El grep de convenciones** (`grep_convenciones_tf.py`, con `LC_ALL=en_US.UTF-8`; los tokens del nombre salen de `git config user.name`
en memoria y no quedan escritos; los términos, los del FRENO T1, §11), en dos grupos, sin los `NO_ABRIR_`:
- **Lo que redacté** (`t3/scripts/`, `t3/salidas/`, `t3/gate_decisiones/`, las tablas de lo contado y de T4, la tabla de los nombres, el
  registro de la vista, la fixture y `grafos.py`): {grep['archivos']} archivos; {grep['coincidencias']} renglones con coincidencias, en
  {' y '.join(f"`{x['archivo'].split('/')[-1]}` ({x['renglones']})" for x in grep['archivos_con_coincidencias'])}, que escriben los términos del grep para buscarlos o
  describirlos; tokens del nombre fuera de rutas, {grep['tokens_fuera_de_rutas']}. Rutas absolutas en {' y '.join(f"`{x['archivo'].split('/')[-1]}`" for x in grep['con_rutas_absolutas'])},
  que las nombran en sus controles. El renglón de control (el primer token y «slack») da {grep['control_positivo']} coincidencias, una por término.
- **Lo que escribieron los generadores** (los ensamblados, la E0 combinada, shapes, la suite, las intrínsecas, los selftests, Neo4j, las
  muestras y su material y las consolas): {mil(grep_gen['archivos'])} archivos de texto, con coincidencias en {len(grep_gen['archivos_con_coincidencias'])}. Los términos son texto de las normas
  ({', '.join(f'«{k}» {mil(v)}' for k, v in sorted(grep_gen['por_termino'].items(), key=lambda x: -x[1]))}). Los tokens del nombre: {mil(grep_gen['tokens_dentro_de_rutas_absolutas'])} dentro de rutas
  absolutas de la copia, que guardan los {sum(1 for x in grep_gen['con_rutas_absolutas'] if x['archivo'].endswith('reporte_ensamblado_r2.json'))} `reporte_ensamblado_r2.json`, como los sellados de la tanda 1 (el otro archivo con
  `/private/tmp`, {', '.join(f"`{x['archivo'].split('/')[-1]}`" for x in grep_gen['con_rutas_absolutas'] if not x['archivo'].endswith('reporte_ensamblado_r2.json'))}, cita la frase del texto firmado que dice que nada queda ahí), y
  {grep_gen['tokens_fuera_de_rutas']} fuera de ellas, en {len(grep_gen['archivos_con_tokens_fuera_de_rutas'])} archivos que copian texto de las normas
  ({', '.join(f'`{k}`' for k in sorted({(n.split('_')[0] + '_*') if '_' in n else n for n in (x['archivo'].split('/')[-1] for x in grep_gen['archivos_con_tokens_fuera_de_rutas'])}))}). Nada de eso lo escribí yo.
- Sobre este FRENO el grep corre después de escribirlo; su resultado va en el mensaje del FRENO.

## 10. Para la autora

1. **`unidades_a_la_vista_T4.json` deja a la vista {mil(vt['unidades_a_la_vista'])} de las {mil(unidades_e0)} unidades** de la tanda final con la regla del «seguí»
   (decisión 5); con la del T4 de la tanda 1, {mil(vt['informacion_con_la_regla_1_1_de_la_tanda_1'])}. La diferencia es la de las dos reglas: la del «seguí» suma las unidades de los
   nodos TextoOrdenado y de los Sujeto con más de una unidad de procedencia que muestran las fichas, y la 1.1 no (tabla T7). Es la lista
   de exclusión de U-MED-VERIF.
2. **La lectura de T4** tiene sus muestras, su material y sus planillas en blanco en `t3/muestras/`, y la versión derivada de la lectura en
   `preregistro/`. No leí ninguna muestra ni marqué nada.
3. **Para el commit:** los cuatro `kg.json` de más de 100 MB de `t3/acumulado/ens_*/r2/` quedan en el árbol sin rastrear y no van al commit;
   van su `.gz` y su sello (registro, §30), como en la tanda 1. Las consolas de los lotes con extensión `.log` las ignora git.
4. **El contenedor de Neo4j del repo** salió con el código 137 al detenerlo (sección 5). La carga ya estaba verificada; la próxima carga lo
   arranca de nuevo.

## 11. Errores propios, con su causa

1. **La primera corrida de `doble_corrida_tf.py` usó una copia vieja del script** (parcial). Corrí los scripts desde la copia del repo y
   copié `t3/scripts/` antes de agregarle la cuenta de la raya. Sincronicé los scripts (control por `cmp`) y la volví a correr.
2. **Dos carpetas vacías en el repo** (parcial). Llamé a `intrinsecas_tf.sh` con la carpeta de salida relativa; el script hace `mkdir -p` antes
   de entrar en la copia y creó `t3/intrinsecas_gen3/e0_del_grafo/` y `con_partes/` en el repo, vacías, sin correr ninguna métrica. Las borré
   con `rmdir`; el script ahora frena si la salida no es absoluta.
3. **La doble corrida comparaba el `.gz` después de comprimir.** Al rehacerla en esta parte, los cuatro acumulados dieron «mismos nombres:
   False» porque su primera corrida ya tenía el `kg.json.gz` y su sello, que agregó `comprimir_kg_tf.py` después de la comparación del
   parcial. `doble_corrida_tf.py` ahora deja esos dos archivos fuera de la comparación, y lo dice su docstring.
4. **Un glob apartó de más.** Para rehacer las intrínsecas del tramo 1 aparté `*Tramo1*`, que también tomó las del acumulado de 60
   («…Tandas0y1yTramo1…»). Las devolví a su lugar sin cambios (las mismas que en el parcial) antes de seguir.

## 12. Los scripts y sus salidas

Los scripts, en `t3/scripts/` (copias adaptadas de los de la tanda 1, con el modelo nombrado en cada docstring); las salidas, en `t3/`:
`salidas/`, `corridas/` (los dos lotes, sus registros y las consolas, con las rutas reemplazadas), `gate/`, `gate_decisiones/`,
`nombres_remision/`, `intrinsecas_gen3/`, `selftests/`, las consolas de `e0_con_partes/`, `neo4j/`, `conteos_sin_leer/` y `muestras/`; y
`registro_vista_r2b_tanda_final.py`. Los ensamblados, en `corpus_tanda_final/ens_*` y en `t3/acumulado/`, con los manifiestos, la E0 combinada y
los registros del armado; los manifiestos del tramo 1 que rigen, en `t3/prueba_raya_tramo1/manifiestos/`. Lo que cambia fuera de `t3/`:
la fixture y `grafos.py`, y la versión derivada de la lectura en `preregistro/`.

El paquete `revision_tanda_final_FRENO_T3/` va en el scratchpad, con su `manifest.txt`, y su copia con `ditto` en
`~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/afadde2e-6298-47fb-9777-7fcb43152d50/scratchpad/revision_tanda_final_FRENO_T3/`; la
verificación va en el mensaje del FRENO.

FRENO T3. Espero la revisión de la mesa y la de la autora.
"""
OUT.write_text(F, encoding="utf-8")
print(F)
