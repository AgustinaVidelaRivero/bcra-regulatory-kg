"""B6.1, tanda final, T3: arma el FRENO T3 parcial por script (pre-registro de la tanda final, §7: toda cifra del FRENO por script desde
sus archivos), con data/experiment/tanda1/t3/scripts/freno_t3f_armar.py como modelo. Las tablas que vienen de una salida
(tablas_ensamblados_tf.md, tabla_nombres_t3_tf.md, veredicto_gate_tf.md y la sección de la foto) van tal cual; la salida del paso 0, tal
como la dio la consola (con el scratchpad y la carpeta personal reemplazados). Las demás cifras del texto se leen acá de sus JSON.
Solo lee <t3> y lo que se le pasa; escribe <salida.md> (fuera del repo).
Uso: python3 -I -B freno_t3_parcial_armar_tf.py <t3> <paso0.json> <seccion_foto.md> <foto.json> <grep redactado.json,grep generado.json>
       <escrituras.json,...> <git_index antes.txt,git_index cierre.txt> <salida.md>
  <paso0.json>: la salida de cada comando del paso 0, tal como la dio la consola, por su descripción.
  (las escrituras al repo, separadas por comas: se suman)
"""
import json
import re
import sys
from pathlib import Path

T3 = Path(sys.argv[1]).resolve()
PASO0, FOTO, FOTOJ, GREP, ESC, GITIX, OUT = (Path(x) for x in sys.argv[2:9])
L = lambda p: json.loads(Path(p).read_text(encoding="utf-8"))  # noqa: E731
txt = lambda p: Path(p).read_text(encoding="utf-8").rstrip("\n")  # noqa: E731
mil = lambda n: f"{n:,}".replace(",", ".")  # noqa: E731
GD, SA = T3 / "gate_decisiones", T3 / "salidas"
ve, fg, dg = L(GD / "veredicto_gate_tf.json"), L(GD / "fuera_del_grafo_tf.json"), L(GD / "diagnostico_clave_cache_tf.json")
cf, ep, cs = L(GD / "control_fixture_tf.json"), L(GD / "e0_partes_tf.json"), L(GD / "causa_s31_tf.json")
dc, kz, nr = L(SA / "doble_corrida_tf.json"), L(SA / "comprimir_kg_tf.json"), L(T3 / "nombres_remision/tabla_nombres_t3_tf.json")
rc = L(T3 / "corridas/lote_t3_tf_rc.json")
sc = L(T3 / "selftests/clave_cache/resumen_sin_cuentas_t3.json")
sha_orig = txt(T3 / "selftests/clave_cache/sha256_selftest_clave_cache_originales_t3.txt")
foto = L(FOTOJ)
grep, grep_gen = (L(x) for x in str(GREP).split(","))
_esc = [L(x) for x in str(ESC).split(",")]
esc = {"nuevos": sum(e["nuevos"] for e in _esc), "cambian": sum(e["cambian"] for e in _esc),
       "escritos": {k: v for e in _esc for k, v in e["escritos"].items()}, "etapas": len(_esc)}

# el paso 0: la salida de cada comando, tal como la dio la consola
P = L(PASO0)
paso0_estado = P["T3 step 0: repo state, commits, 78 routes"].strip("\n")
paso0_t1 = P["Regenerate T1 derived preregistro from 4de7f2a7, check inputs"].strip("\n")
paso0_docker = next(x for x in P["Inspect tanda1 T3 photo script and check Docker"].splitlines() if "Docker" in x)
paso0_vol = P["Check Neo4j volume unchanged since T2 by size and date"].strip("\n")
paso0_foto = P["Take T3 pre-snapshot, .pyc count, update checkpoint"].strip("\n")
gi_antes, gi_cierre = (Path(x).read_text(encoding="utf-8").split() for x in str(GITIX).split(","))
gi_igual = [x for x in gi_antes if len(x) == 16] == [x[:16] for x in gi_cierre if len(x) == 64]

g = ve["grafos"]
n_reg = {k: v["suite"]["regresiones"] for k, v in g.items()}
sola = [k for k, v in fg["grafos"].items() if v["tanda_sola"]]
acum = [k for k, v in fg["grafos"].items() if not v["tanda_sola"]]
cuentan = sorted({r for v in g.values() for r in v["suite"]["no_declaradas_que_cuentan"]})
s31_repo = sorted(k for k, v in g.items() if "S31" in v["shapes_e0_del_grafo"]["bloqueantes_en_fail"])
rige_falla = sorted(k for k, v in g.items() if v["shapes_rige"]["bloqueantes_en_fail"])
raya = dc["raya_tramo1"]["tf_tramo1_raya"]
nf = {k: x for k, x in nr["filas"].items()}
partes = {n: e["corridas"][0]["reemplazos"] for n, e in ep["e0_con_partes"].items()}

F = f"""# FRENO T3 (parcial) — tanda final de B6.1: los ocho ensamblados reproducen; el gate no pasa por el selftest de claves (20/10/2026, USD 0, sin API, sin commit)

Rigen el pre-registro de la tanda final FIRMADO (`docs/preregistro_tanda_final.md`, firma en `4de7f2a7`, con sus notas posteriores en
`27bfaeb5` y `86541475`), sus §2, §5, §6, §7 y §8 y la precisión de la firma, lo del pre-registro de la tanda 1 que este no reemplaza y el
«seguí» de T3, con sus tres correcciones. HEAD `eb5ad14b`. Toda cifra de este FRENO sale de un script de `t3/scripts/` y de su salida; la
sección 9 los lista.

**Resultado:**
- **Los ocho ensamblados** (punto 3) salen con rc 0 en las {len(rc)} corridas del lote, la doble corrida de cada uno da el mismo `kg.json`, los
  diez grafos sellados de las tandas 0 y 1 se reproducen byte a byte y el acumulado con el tramo 1 da las cifras de la prueba de la mesa
  (tablas E1 a E5). Los cuatro `kg.json` de los acumulados pasan de 100 MB y van con su `.gz`, que se restaura byte a byte.
- **El gate** (punto 4) **no pasa**, por una sola causa: el selftest de claves (`selftest_clave_cache`) da rc distinto de 0. La causa, por
  código y por datos, sin abrir sus salidas: su variación R23 supone que la unidad `{dg['UNIDAD_TO_NUEVO']}` no está en la caché de E1, y
  `{dg['TO_NUEVO']}` es un TO de la tanda final que T2 extrajo con el mismo chunk (sección 3.4). Lo demás del gate da lo esperado: con la E0
  con las partes, que rige para S31, shapes pasa en los ocho; la suite da {len(cuentan)} regresiones no declaradas que cuenten; los
  selftests de la cadena dan rc 0; la fixture solo suma las ocho entradas.
- Como dice el punto 4 del «seguí», **freno acá, sin los puntos 5 (el registro y Neo4j), 6 (lo que se cuenta sin leer) y 7 (la
  preparación de T4)**. Lo que sigue lo decide la autora. Dejé preparados sus scripts, sin correr sobre el repo (sección 5). Nada commiteado
  y ningún mensaje de commit preparado.

## 1. Paso 0 (20/10/2026, desde las 10:02:13)

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
checkpoint. La foto entera queda fuera del repo y del paquete porque nombra todas las rutas del repo; su resumen va en la sección 7. La
salida de las entradas en HEAD termina con la cuenta de los renglones OK de `t1/sha256_para_T2.txt`.

## 2. Los ocho ensamblados (punto 3)

El mecanismo es el del T3 de la tanda 1, copiado y adaptado en `t3/scripts/`: `armar_acumulados_tf.py` arma por copia la E0 y la entrada
de los dos acumulados en una copia del repo (la del `rsync` del «seguí», con 0 nombres vedados y 0 enlaces); `cadena_t3_tf.sh` corre
`ensamblar_tanda0.py` con los argumentos de las corridas del T3 de la tanda 1; `correr_lote_t3_tf.py` corre las {len(rc)} cadenas de a
tres; `doble_corrida_tf.py` compara. La tanda y el tramo 1 van con los cuatro manifiestos de T1, `--entrada
data/experiment/reextraccion_v2/corpus_tanda_final/salida_r2b` y la E0 de los 98. La unidad con error de T2
(`ri_transpa::Sbloque1::chapeau_seccion`) falta en los grafos, como decidió la autora (registro, §44): no la toqué.

{txt(SA / 'tablas_ensamblados_tf.md')}

### 2.1 Los `nombres_remision` de los ensamblados nuevos, medidos (§7; registro, §19; enmienda 9, punto 8)

`medir_nombres_t3_tf.py` es la medición de la mesa (`nombres_remision/medir_nombres_remision_mesa.py`) con los cuatro corpus nuevos; el
contraste y el resumen son los de la mesa, sin cambios (`contrastar_con_inventario_completo_mesa.py` y `resumir_medicion_mesa.py`). Todo
corrió sobre la copia. `tabla_nombres_t3_tf.py` pone las cifras de la mesa al lado (las del 16/10/2026 del repo, y las de la enmienda 9,
punto 8, `756a0394:81-84`, para el tramo 1 y el acumulado de 60):

{txt(T3 / 'nombres_remision/tabla_nombres_t3_tf.md')}

Iguales a la mesa en los cuatro: {nr['todas_iguales_a_la_mesa']}.

- **Los manifiestos de los acumulados.** El de 128 lo derivó `derivar_manifiesto_ensamblado_mesa.py` con el contraste de la mesa (corpus
  `acumulado_final`: 0 distintas, la raya entra; {nf['acumulado_final']['tos_con_nombres_en_el_manifiesto']} TOs con nombres). Para el de 60, ese
  derivador frena, porque la medición del repo no tiene un corpus con esos TOs (la de la enmienda 9, punto 8, está en el paquete de la mesa).
  Lo derivé con `derivar_manifiesto_ensamblado_tf.py`, que hace lo mismo con la variante decidida por la fuente que se le pasa
  (`756a0394:83-84`: 23 distintas, la raya no entra; {nf['acumulado_tramo1']['tos_con_nombres_en_el_manifiesto']} TOs con nombres), y escribe esa fuente en la
  `descripcion`. La medición de arriba la confirma.

## 3. El gate (punto 4)

Sobre la copia del repo, con las decisiones del gate de la tanda 1 (registro, §29): para S31 rige la E0 con las partes por corte, y se
informan las dos corridas; la suite se juzga sobre el acumulado, y en la tanda y en el tramo 1 lo «fuera del grafo» se informa aparte y no
cuenta; E4-a1 y E4-a4 siguen declaradas. Los `--out` van a `t3/gate/` (el «seguí» lo pide así; en la tanda 1 fueron a las carpetas de los
ensamblados).

{txt(GD / 'veredicto_gate_tf.md')}

### 3.1 Shapes

- Con la E0 con las partes (`e0_partes_tf.py`, que corre `reext_t0/t3/e0_con_partes.py` sin cambios, dos veces por E0): pasa en los ocho.
  La tanda final no tuvo unidades partidas (su E0 con las partes es la E0 del repo: {ep['controles']['tanda_final_igual_a_la_e0_del_repo']}); en los acumulados entran
  las partes de las tandas 0 y 1 ({', '.join(f'{u} en {len(v)} partes' for x in partes['acum128'].values() for u, v in x.items())}).
- Con la E0 de cada grafo: S31 falla en {len(s31_repo)} grafos ({', '.join(g[k]['nombre'] for k in s31_repo)}), por las `remite_a` de las partes por corte
  de `ri_rml::Sbloque14`, de la tanda 1 (tabla V2, `causa_s31_tf.json`). En los cuatro de la tanda final, S31 pasa también con la E0 del
  repo.
- Los FAIL y WARN que no bloquean son los mismos en los ocho y en los grafos de la tanda 1 (`tablas_gate_tf.json`, `no_pass`).

### 3.2 La suite y la fixture

- **La fixture** (`editar_fixture_tf.py`, sobre la copia): ocho entradas nuevas al final de `estado_esperado`, copias de la entrada sellada
  del grafo anterior del mismo tipo de la tanda 1 (KG-Tanda1-Veinte-r2b para la tanda y el tramo 1; KG-Acumulado-Tandas0y1-r2b para los
  acumulados, completo o sin cola), con el `kg`, el `kg_sha256` y el `registro_dir` nuevos. El script controla que las expectativas de esas
  cuatro y de las dos de diez de la tanda 0 re-sellada son las mismas, así que elegir una u otra solo cambia el rótulo.
- **El control de la precisión de la firma, punto 3** (`control_fixture_tf.py`, contra `git show HEAD:`): {mil(cf['claves_de_HEAD'])} claves de HEAD,
  {cf['quitadas']} quitadas y {cf['cambiadas']} cambiadas; {mil(cf['claves_nuevas'])} claves nuevas, todas de las ocho entradas: {cf['son_las_ocho']}; el orden de las selladas,
  igual: {cf['orden_de_las_selladas_igual']}. Veredicto: {'OK' if cf['ok'] else 'CON FALLAS'}.
- **El resultado:** en los acumulados, {n_reg[acum[0]]} regresiones en cada uno, las tres del laudo y E4-a1 y E4-a4, declaradas; en la tanda y en el
  tramo 1, {n_reg[sola[0]]} en cada uno, todas fuera del grafo (`fuera_del_grafo_tf.py`, con las anclas de cada ítem sacadas de su definición en
  `scripts/regression_kg.py`). El cruce: en los cuatro, las no declaradas fuera del grafo son las no declaradas que su acumulado no da ({fg['cruce'][sola[0]]['cuantos'][0]} y
  {fg['cruce'][sola[0]]['cuantos'][1]} ítems, iguales: {all(x['iguales'] for x in fg['cruce'].values())}).

### 3.3 La reproducibilidad, los selftests de la cadena, las intrínsecas y los contadores

Las tablas E3 y V3. Los selftests de la cadena corrieron sobre un clon APFS de la copia (`selftests_tf.sh`, con 0 nombres vedados y 0
enlaces). El del catálogo pide `git show 4ef7650:<ruta>` (`derivar_catalogo_r2.py:103`): corrió con `GIT_DIR` en el `.git` del repo y
`GIT_OPTIONAL_LOCKS=0`, en lugar del `git clone` del T3 de la tanda 1, que trajo archivos `.env` y `NO_ABRIR_` al clon. El sha256 de
`.git/index` y de `.git/HEAD` antes de los selftests y al cerrar T3 ({gi_cierre[0]} {gi_cierre[1]}), por sus primeros 16 caracteres: iguales,
{gi_igual}.

### 3.4 El selftest de claves: la causa por la que el gate no pasa

- **Cómo corrió:** `selftest_clave_cache --salida-r2b data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b`, como en A3 y en T1, sobre el
  clon, con su JSON y su consola a archivos que no abrí; `selftest_claves_sin_cuentas_tf.py` (el de T1 con los nombres de T3) les sacó
  las cuentas con `alcance_e1/a3/scripts/clave_cache_sin_cuentas_a3.py` y las comparó con las de A3 sin cuentas. Los sha256 de las dos
  originales:

```
{sha_orig}
```

- **Lo que dio:** el selftest terminó con rc 1. Las dos salidas sin cuentas no son las de A3 (JSON igual: {sc['json_igual_al_de_a3_sin_cuentas']}; consola igual:
  {sc['consola_igual_a_la_de_a3_sin_cuentas']}), así que el script las renombró a `NO_ABRIR_` y no las abrí. Doy solo las rutas de los
  {len(dg['rutas_que_difieren_de_A3_sin_cuentas'])} campos del JSON que difieren, sin valores:
  {', '.join(f'`{r}`' for r in dg['rutas_que_difieren_de_A3_sin_cuentas'])}.
- **La causa** (`diagnostico_clave_cache_tf.py`, que lee solo esas rutas, el código del selftest, el manifiesto de la tanda final y las dos
  E0; ni las salidas del selftest ni las bases de la caché):
  - todos esos campos son de la variación del TO nuevo o derivan de ella: {dg['todas_en_la_variacion_del_TO_nuevo_o_derivadas']}. Es `{', '.join(dg['funciones_con_clave_en_cache_e1'])}`, la única
    función del selftest con el campo `clave_en_cache_e1`: V23 en el perfil sellado y R23 en el r2b;
  - supone que una unidad de un TO de fuera de la tanda 0, `{dg['UNIDAD_TO_NUEVO']}` (de la partición b584), no está en la caché de E1 (miss);
  - `{dg['TO_NUEVO']}` es de la tanda final ({dg['lugar_en_orden_corrida']}.º de `orden_corrida`, tramo {dg['tramo']}), y su chunk es el mismo en la E0 de la tanda final y en
    b584: {dg['chunk_igual_en_las_dos']}. T2 lo extrajo con el perfil r2b, así que la clave de R23 está en la caché y R23 deja de dar miss.
  - En T1 el selftest dio OK (FRENO T1, §4.1) porque T2 todavía no había extraído ese TO. El código de la clave (`llm_cache.py`,
    `cliente_e1.py` y `cliente_e3.py`) está entre las 78 rutas, que el paso 0 dio iguales; el selftest no está entre ellas y es el de HEAD.
    Falla por un supuesto que T2 dejó de cumplir, no por el código de la clave.
- **El cegamiento:** saber si una clave de E1 está en la base es un dato de la caché de E1; no di cuentas de claves ni nada de E3. Las
  dos salidas sin cuentas quedan como `NO_ABRIR_` en `t3/selftests/clave_cache/`, sin abrir; las dos originales, con las cuentas, quedan
  en el scratchpad, sin abrir, y van solo por su sha256.

## 4. Para la autora

1. **El selftest de claves** (sección 3.4): decide cómo sigue el gate. Las opciones que veo, sin tocar código: declarar la R23 (y la V23
   del perfil sellado, que no cambió) como no aplicable después de T2, porque su TO ya se extrajo, y juzgar el selftest sin ella; o pedir a
   la mesa que cambie el TO de la variación por uno que no esté en ninguna tanda (`TO_NUEVO` y `UNIDAD_TO_NUEVO`,
   `selftest_clave_cache.py:132-133`), que es tocar el código del selftest (no está entre las 78 rutas). Lo demás del gate da lo esperado
   (tabla V1).
2. **Los manifiestos del tramo 1.** El «seguí» pide los cuatro manifiestos de T1, que no llevan la raya, y la §19 con la enmienda 9, punto 8,
   dice que en el tramo 1 solo «la raya entra, sin cambiar ninguna resolución». Corrí las dos: el `kg.json` es el mismo, completo y sin cola,
   aunque los `nombres_remision` cambian en {len(raya['tos_con_nombres_distintos_entre_los_manifiestos'])} de los 30 TOs (tabla E4). Mandan los archivos: la regla de la §19 da la raya;
   el grafo no cambia con ninguna.
3. **El derivador del acumulado de 60** (sección 2.1): el de la mesa no corre sin la medición en el repo, y usé una copia adaptada.
4. **Para el punto 7, cuando se decida seguir** (preparado, sin correr sobre el repo):
   - los umbrales: el script de la mesa, importado sin cambios como en el T3 de la tanda 1, mide la atención y el freno contra la tasa de
     la tanda 0 (su `BASE`), y el pre-registro de la tanda final da como línea de base la de la tanda 1. Las dejo las dos al lado;
   - `unidades_a_la_vista_T4.json`: la regla del «seguí» (de un nodo, todas las unidades de su procedencia) es la del T3 de la tanda 1; el T4
     de la tanda 1 usó una más chica (decisión del 18/10/2026, punto 1.1: sin el TextoOrdenado ni el Sujeto fusionado). Sigo la del «seguí» y
     doy la otra como información;
   - los dos momentos de lectura del §6 se juntan en uno, como lo pide el «seguí».

## 5. Lo que no hice: los puntos 5, 6 y 7

Por el freno del punto 4 no toqué `grafos.py` ni Neo4j, no conté nada sin leer y no armé poblaciones, umbrales, sorteos ni material. Están
listos en `t3/scripts/` y no corrieron: `editar_grafos_tf.py`, `dry_registro_tf.py`, `cargar_neo4j_tf.py`, `control_cola_neo4j_tf.py`,
`contado_sin_leer_tf.py`, `tablas_contado_tf.py`, `poblaciones_t4_t3f_tf.py`, `poblaciones_t4t1_tf.py`, `umbrales_t4_tf.py`, `sorteos_t4_t3f_tf.py`,
`sorteos_t4t1_tf.py`, `material_t4_t3f_tf.py`, `material_t4t1_tf.py`, `unidades_a_la_vista_tf.py` y `tablas_t4_tf.py`. La base de los
sorteos la controlé: `git show 5289b02f:docs/preregistro_tanda_final.md` da `0897d609…`.

La versión derivada de la lectura (7.7) no lee ningún grafo: la armé en el scratchpad con el completador sobre el pre-registro de
`4de7f2a7` y `--momento lectura_tramo1`, y queda sin ningún `⟦T4.` (solo espera el hueco de T5). No la pasé al repo, porque es del punto 7;
va en el paquete.

## 6. El cegamiento (punto 8)

- No miré ni di el desglose de las aceptadas por estado de E3, `n_reintentos`, `reintentos_e3.jsonl`, `copias_nota_e3.jsonl`, las `marcas_e3`
  ni el gasto de los reintentos.
- De la salida de la extracción, ninguna cuenta por tipo de archivo. La entrada de los acumulados se registra solo por su total de archivos,
  sus bytes y el sha256 de su lista (tabla E5). La E0 con las partes informa las unidades partidas por corte, que son de E1.
- No escribí `NO_ABRIR_conteos_t3.json`: lo escribe lo contado sin leer (punto 6), que no corrí. Los `NO_ABRIR_` de esta parte son los dos del
  selftest de claves (sección 3.4).
- No abrí ningún `.env` ni ningún `NO_ABRIR_`, ni ninguna carpeta vedada.

{txt(FOTO)}

**Lo que se escribió en el repo** (`escribir_en_el_repo_tf.py`, en {esc['etapas']} etapas, los ensamblados y el gate, desde un staging armado en el
scratchpad; antes, cada ruta nueva no existía y la fixture era la de HEAD; después, cada archivo es byte a byte el del staging):
{mil(esc['nuevos'])} archivos nuevos y {esc['cambian']} que cambia, la fixture; escritos iguales al staging: {mil(sum(v['igual_al_staging'] for v in esc['escritos'].values()))} de
{mil(len(esc['escritos']))}. Escritos después de la foto de después: este FRENO y `t3/resumen_fotos_T3.json`.

**El grep de convenciones** (`grep_convenciones_tf.py`, con `LC_ALL=en_US.UTF-8`; los tokens del nombre salen de `git config user.name`
en memoria y no quedan escritos; los términos, los del FRENO T1, §11), en dos grupos, sin los `NO_ABRIR_`:
- **Lo que redacté** (`t3/scripts/`, `t3/salidas/`, `t3/gate_decisiones/`, la tabla de los nombres y la fixture): {grep['archivos']} archivos;
  {grep['coincidencias']} renglones con coincidencias, en {' y '.join(f"`{x['archivo'].split('/')[-1]}` ({x['renglones']})" for x in grep['archivos_con_coincidencias'])}: los
  dos escriben los términos del grep, uno para buscarlos y el otro para describirlos; tokens del nombre fuera de rutas, {grep['tokens_fuera_de_rutas']}.
  Rutas absolutas en {' y '.join(f"`{x['archivo'].split('/')[-1]}`" for x in grep['con_rutas_absolutas'])}, que las nombran en sus controles. El renglón de
  control (el primer token y «slack») da {grep['control_positivo']} coincidencias, una por término.
- **Lo que escribieron los generadores** (los ensamblados, la E0 combinada, shapes, la suite, las intrínsecas, los selftests y las consolas):
  {mil(grep_gen['archivos'])} archivos de texto, con coincidencias en {len(grep_gen['archivos_con_coincidencias'])}. Los términos son texto de las normas
  ({', '.join(f'«{k}» {mil(v)}' for k, v in sorted(grep_gen['por_termino'].items(), key=lambda x: -x[1]))}). Los tokens del nombre: {grep_gen['tokens_dentro_de_rutas_absolutas']} dentro de
  rutas absolutas de la copia (las que guardan {len(grep_gen['con_rutas_absolutas'])} `reporte_ensamblado_r2.json`, como los sellados de la tanda 1) y
  {grep_gen['tokens_fuera_de_rutas']} fuera de ellas, en {len(grep_gen['archivos_con_tokens_fuera_de_rutas'])} archivos que copian texto de las normas
  ({', '.join(f'`{k}`' for k in sorted({(n.split('_')[0] + '_*') if '_' in n else n for n in (x['archivo'].split('/')[-1] for x in grep_gen['archivos_con_tokens_fuera_de_rutas'])}))}: las copias de la E0 y los registros
  de omisiones del ensamblado). Nada de eso lo escribí yo.
- Sobre este FRENO el grep corre después de escribirlo; su resultado va en el mensaje del FRENO.

## 8. Errores propios, con su causa

1. **La primera corrida de `doble_corrida_tf.py` usó una copia vieja del script.** Corrí los scripts desde la copia del repo y copié
   `t3/scripts/` antes de agregarle la cuenta de la raya; la salida salió sin esa cuenta. Sincronicé los scripts (control por `cmp`) y la volví
   a correr; la tabla E4 es la de la segunda.
2. **Dos carpetas vacías en el repo.** Llamé a `intrinsecas_tf.sh` con la carpeta de salida relativa, y el script hace `mkdir -p` antes de
   entrar en la copia: creó `t3/intrinsecas_gen3/e0_del_grafo/` y `con_partes/` en el repo, vacías, y ninguna métrica corrió (la consola
   apuntaba a una carpeta que no existía en la copia). Las borré con `rmdir`, que solo borra carpetas vacías, y las intrínsecas corrieron
   de nuevo con la salida absoluta, dentro de la copia, como en la tanda 1.

## 9. Los scripts y sus salidas

Los scripts, en `t3/scripts/` (copias adaptadas de los de la tanda 1, con el modelo nombrado en cada docstring); las salidas, en `t3/`:
`salidas/` (doble corrida, compresión, contadores de E1, tablas de los ensamblados), `corridas/` (el lote, su registro y las consolas, con las
rutas reemplazadas), `gate/` (shapes y suite de cada grafo, con las dos E0), `gate_decisiones/` (E0 con las partes, tablas, fuera del grafo,
S31, fixture, diagnóstico del selftest de claves y veredicto), `nombres_remision/`, `intrinsecas_gen3/`, `selftests/` y las consolas de
`e0_con_partes/`. Los ensamblados, en `corpus_tanda_final/ens_*` y en `t3/acumulado/`, con los manifiestos, la E0 combinada y los registros
del armado; la prueba de la raya, solo con sus manifiestos (`t3/prueba_raya_tramo1/manifiestos/`).

El paquete `revision_tanda_final_FRENO_T3/` va en el scratchpad, con su `manifest.txt`, y su copia con `ditto` en
`~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/afadde2e-6298-47fb-9777-7fcb43152d50/scratchpad/revision_tanda_final_FRENO_T3/`; la
verificación va en el mensaje del FRENO.

FRENO T3 (parcial). Espero la revisión de la mesa y la decisión de la autora.
"""
OUT.write_text(F, encoding="utf-8")
print(F)
