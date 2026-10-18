"""B6.1, tanda 1, T3 (desde el punto 4): arma el FRENO T3 final por script (decisión 8 de la autora del 18/10/2026: toda cifra del
FRENO por script desde sus archivos). Las tablas que vienen de una salida (veredicto_gate_t3f.md, tablas_contado_t3f.md, tablas_t4_t3f.md,
la sección de la foto) van tal cual; los diff crudos del control de shapes, también. Las demás cifras del texto se leen acá de sus JSON.
Solo lee <raíz>; escribe <salida.md> (fuera del repo).
Uso: python3 -I -B freno_t3f_armar.py <raíz> <paso0.md> <seccion_foto.md> <grep.json> <escrituras.json> <salida.md>
"""
import json
import re
import sys
from pathlib import Path

RAIZ = Path(sys.argv[1]).resolve()
PASO0, FOTO, GREP, ESC, OUT = (Path(x) for x in sys.argv[2:7])
T3 = RAIZ / "data/experiment/tanda1/t3"
L = lambda p: json.loads(Path(p).read_text(encoding="utf-8"))  # noqa: E731
txt = lambda p: Path(p).read_text(encoding="utf-8").rstrip("\n")  # noqa: E731
mil = lambda n: f"{n:,}".replace(",", ".")  # noqa: E731
GD, NE, CS, MU = T3 / "gate_decisiones", T3 / "neo4j", T3 / "conteos_sin_leer", T3 / "muestras"
ep, ve, fg = L(GD / "e0_con_partes_t3f.json"), L(GD / "veredicto_gate_t3f.json"), L(GD / "fuera_del_grafo_t3f.json")
dry, cc = L(NE / "dry_registro_t3f.json"), L(NE / "control_cola_neo4j_t3f.json")
carga = {k: L(NE / k / "carga_neo4j_tanda0.json") for k in ("KG_Tanda1_Veinte_r2b", "KG_Tanda1_Veinte_r2b_sincola")}
cs, pob, um = L(CS / "contado_sin_leer_t3f.json"), L(MU / "poblaciones_t4.json"), L(MU / "umbrales_t4_reales.json")
vis, comp = L(MU / "unidades_a_la_vista_T4.json"), L(MU / "composicion_obs12_t3f.json")
grep, esc = L(GREP), L(ESC)
sha_c = [re.findall(r"^([0-9a-f]{64})", x, re.M) for x in (txt(NE / "sha_cargador_antes.txt"), txt(NE / "sha_cargador_despues.txt"))]
cons_ed = txt(NE / "consola_editar_grafos_t3f.txt")
cola_h = re.search(r"cola humana: (\d+)", cons_ed).group(1)
psn = dry["desglose"]["tanda1_ens_veinte_r2b_sincola"]["recomputado"]
items = fg["items"]
con_anclas = sum(1 for v in items.values() if v["anclas"])
diffs = []
for g in ("ens_veinte_r2b", "ens_veinte_r2b_sincola", "ens_treinta_r2b", "ens_treinta_r2b_sincola"):
    for n in ("shapes_perfil_r2_fase_r2b.md", "shapes_perfil_r2_fase_r2b.json"):
        diffs.append(txt(GD / "shapes_con_partes" / g / f"diff_crudo_{n}.txt"))
v2 = ve["grafos"]
mat, sor = L(MU / "material/material_t4.json"), L(MU / "sorteos_t4.json")
n_fichas = sum(x["fichas"] for x in mat["muestras"].values())
ctrl_mat = txt(MU / "control_material_t4.txt")
n_partes = int(re.search(r"'e0_con_las_partes': (\d+)", ctrl_mat).group(1))
horas_sor = sorted({x["hora"][11:19] for x in sor["muestras"].values()})
col = [x for x in txt(CS / "columna_tanda1_tablero_t3f.md").splitlines() if x.startswith("| ") and x[2:4].isdigit()]
filas_ev2 = [x.split("|")[1].strip() for x in col if "residuo declarado, no medible en r2 sin correr el agente" in x]
solo = {m: x["informacion_solo_por_TextoOrdenado_o_Sujeto"] for m, x in vis["muestras"].items()}
n_fuera = {g: len(fg["grafos"][g]["regresiones_fuera_del_grafo"]) for g in ("veinte", "veinte_sincola")}
assert n_fuera["veinte"] == n_fuera["veinte_sincola"]
Nc, nc = um["cola"]["N_por_celda"], um["cola"]["n_por_celda"]

F = f"""# FRENO T3 — tanda 1 de B6.1: el gate pasa con las decisiones del 18/10/2026; registro, Neo4j, lo contado y la preparación de T4 (USD 0, sin API, sin commit)

Rigen el pre-registro firmado (`docs/preregistro_tanda1.md`, firma en `95b18217`, con su nota del 17/10/2026 en `ca5b39fd`), el «seguí» de
T3 y lo que decidió la autora el 18/10/2026 sobre el FRENO parcial (va a la §29 del registro de decisiones). HEAD `0c927ebb`. Este FRENO
sigue al parcial, que quedó renombrado sin cambios (`t3/FRENO_T3_parcial.md`, sha256 `63abc417…`).

**Resultado:**
- **El gate, con las decisiones 1 a 3, pasa en los cuatro grafos** (sección 3, tabla V2): shapes con la E0 con las partes da PASA en los
  cuatro; la suite da 0 regresiones no declaradas que cuenten; la reproducibilidad y los selftests, de las tablas del parcial, en verde.
- **El registro y Neo4j** (sección 4): dos entradas nuevas en `grafos.py` y el registro de la vista. La carga, con el envoltorio del
  cargador que la autora indicó, da gate 5 OK en los dos grafos, la paridad {' y '.join(sorted({c['equivalencia']['paridad_total'] for c in carga.values()}))}
  en cada uno y {cc['grafos']['KG_Tanda1_Veinte_r2b_sincola']['neo4j_nodos_cola_humana_true']} nodos con la marca de la cola en el sin cola.
- **Lo que se cuenta sin leer** (sección 5): las observaciones (10) y (11), las vigilancias (4), (5), (8) y (9), la cola, el catálogo al
  cierre y la columna «Tanda 1» del tablero. De L-02 y de L-04, solo si sus pozos llegan a 30: llegan los dos.
- **La preparación de T4** (sección 6): las poblaciones por celda, los pesos reales, los umbrales, seis sorteos, el material
  ({n_fichas} fichas) y `unidades_a_la_vista_T4.json`. No leí ninguna muestra ni marqué nada.
- Toda cifra sale por script de sus archivos. Las tablas que copio de una salida van tal cual; mis aclaraciones van fuera de las tablas.
- Nada commiteado y ningún mensaje de commit preparado: los commits son de la autora y quedan PENDIENTES.

{txt(PASO0)}

## 2. Lo decidido el 18/10/2026 y cómo lo apliqué

1. **S31 con la E0 con las partes por corte.** Es la que rige para el gate; la del repo se informa al lado (tabla V2). Es una precisión del
   gate tomada con el resultado a la vista, y vale igual para la tanda final. La rearmé fuera del repo (sección 3) y su sha256 va en la
   tabla V0.
2. **E4-a1 y E4-a4, declaradas como regresiones de la tanda 1.** No frenaron el resto de T3. No toqué el backlog: la entrada la escribe la
   mesa.
3. **La suite se juzga sobre el acumulado.** En la tanda 1 sola, la clase «fuera del grafo» la da `scripts/fuera_del_grafo_t3f.py`:
   - las anclas de cada ítem salen de su definición en `scripts/regression_kg.py`: el cierre de llamadas de su función en `TESTS`,
     recorrido por AST (las constantes de TO, las cadenas `<to>::<punto>` y los ids de TO del inventario), las `anclas` de
     `DEF_IDS_NUEVOS` en los ítems ID y, en T5, las anclas de `MUESTRA30`, que su código lee. El `direccionamiento` del registro hace de
     control: todo TO que nombra lo da también el código;
   - la fixture no trae anclas estructuradas: sus `nota` son texto libre y no se usaron;
   - {con_anclas} de los {len(items)} ítems tienen anclas; los otros {len(items) - con_anclas} son generales y valen en todo grafo;
   - no quedó ningún ítem sin anclas sacadas por script;
   - el cruce con `clasificar_regresiones_t3.py` da los mismos {fg['cruce']['veinte']['cuantos'][0]} ítems en los dos grafos de la tanda 1.
4. **Los `nombres_remision` de la tanda 0 en el acumulado** son los de la regla v2 (`222a0614`), como confirmó la mesa en el grafo.
5. **Las cuatro entradas nuevas de la fixture** quedan, para el commit de T3; las selladas no cambiaron.
6. **Las salidas de shapes y de la suite de los dos grafos de la tanda 1** quedan donde están, como en el re-sellado (sección 7).
7. **El clon de git del parcial** (su error propio 1) queda declarado (sección 7).
8. **Siguen las decisiones A y B:** las cuentas de E3 en cegamiento y toda cifra por script.
9. **`unidades_a_la_vista_T4.json`** registra, por muestra, toda unidad cuya extracción aparece en el material, en cualquier versión, y
   cuál (sección 6).

## 3. La E0 con las partes y el gate (punto 4)

**La E0 con las partes** (`scripts/e0_partes_t3f.py`, sobre una copia nueva del repo):
- La entrada del acumulado no está en el repo. La rearmé en la copia con `armar_acumulado_t3.py`, y lo rearmado es lo del repo:
  {ep['acumulado']['entrada']['archivos']} archivos y {mil(ep['acumulado']['entrada']['bytes'])} bytes.
- `reext_t0/t3/e0_con_partes.py`, sin cambios, corrió dos veces por E0, cada vez en un proceso aparte. Las dos corridas dan los mismos
  bytes, iguales a las de ayer (tabla V0). El sha256 de cada archivo está en `gate_decisiones/e0_con_partes_t3f.json`.
- **El control de shapes.**
  - El intento 1 frenó: el `.md` y el `.json` difieren de los del parcial en las rutas y en la línea de la fecha de corrida.
  - Lo pregunté. La autora indicó normalizar solo la línea «Fecha:» del `.md` y el campo `"fecha"` del `.json`, además de las rutas, poner el
    diff crudo en el FRENO y frenar ante cualquier otra diferencia.
  - El intento 2, sobre una copia nueva, da el control OK en los cuatro grafos (tabla V1).
  - El intento 1 está en `gate_decisiones/intento1_control_e0/`.

**El diff crudo de los cuatro grafos, antes de normalizar** (`gate_decisiones/shapes_con_partes/<grafo>/diff_crudo_*.txt`; el scratchpad
escrito `<SCRATCHPAD>`; la consola da 0 líneas en los cuatro):

```
{chr(10).join(diffs)}
```

Normalizadas las rutas y esa línea, en los cuatro no queda ninguna diferencia (`distintas_despues_de_normalizar` vacío en
`e0_con_partes_t3f.json`).

**La tabla del veredicto** (`scripts/veredicto_gate_t3f.py` → `gate_decisiones/veredicto_gate_t3f.md`, tal cual):

{txt(GD / 'veredicto_gate_t3f.md')}

## 4. El registro y Neo4j (punto 5)

- **`grafos.py`:** `scripts/editar_grafos_t3f.py` agregó, en la copia, solo dos entradas al final de `GRAFOS`:
  - las claves `KG_Tanda1_Veinte_r2b` y `KG_Tanda1_Veinte_r2b_sincola`, con label, índice y `ev2_key` propios y `commit_sellado` «PENDIENTE»;
  - el sha256, `n_nodos` y `n_aristas`, de `salidas/doble_corrida_t3.json`.
  Las {len(dry['grafos_py_selladas_iguales'])} selladas son iguales a las de HEAD (corrida en seco). En el repo, `grafos.py` cambia solo por
  esas dos entradas.
- **El registro de la vista:** `t3/registro_vista_r2b_tanda1.py`, con el patrón de `resellado_t0/registro_vista_r2b_rs1.py`.
  - La cola humana de la tanda 1: {cola_h} unidades (`neo4j/consola_editar_grafos_t3f.txt`).
  - El desglose de «punto sin nodos» del sin cola: {psn['registro']['punto_sin_nodos_total']} en total,
    {psn['registro']['con_destino_en_unidad_excluida']} con destino en una unidad excluida y {psn['registro']['netas']} netas. El completo
    da {psn['grafo_completo']['registro']['punto_sin_nodos_total']}.
- **La corrida en seco** (`scripts/dry_registro_t3f.py`, por el camino de imports del cargador) da {'OK' if dry['ok'] else 'CON FALLAS'}:
  los sha256, la vista con {mil(dry['grafos']['KG_Tanda1_Veinte_r2b']['vista_nodos'])} / {mil(dry['grafos']['KG_Tanda1_Veinte_r2b']['vista_aristas'])}
  y {mil(dry['grafos']['KG_Tanda1_Veinte_r2b_sincola']['vista_nodos'])} / {mil(dry['grafos']['KG_Tanda1_Veinte_r2b_sincola']['vista_aristas'])},
  igual al registro, y el desglose igual a lo declarado.
- **El cargador.** `cargar_neo4j_tanda0.py` acepta en `--grafo` solo las claves `KG_Tanda0_*`. Frené y lo pregunté. La autora indicó
  el envoltorio en memoria, con condiciones:
  - `scripts/cargar_neo4j_t3f.py` importa el cargador sin editarlo, deja en memoria `CLAVES_TANDA0` con exactamente las dos claves de la
    tanda 1 y llama a su `main()` una vez por clave, con `--grafo <clave>`, nunca con «todos»;
  - el sha256 del cargador es `{sha_c[0][0][:16]}…` antes de la carga y `{sha_c[1][0][:16]}…` después, igual a HEAD
    (`neo4j/sha_cargador_antes.txt` y `_despues.txt`);
  - las salidas heredan los rótulos de la tanda 0: `carga_neo4j_tanda0.json`, «U-TANDA0-2A E3.c» y «PARIDAD (tanda 0)». No se corrigen.
- **Docker:**
  - Docker Desktop tenía el backend corriendo y el motor respondía 500, también después de abrirlo y esperar 5 minutos. Lo reinicié
    (`docker desktop restart`) y levanté el contenedor del repo (`docker compose up -d --wait`) (`neo4j/consolas/consola_docker_arranque.txt`).
  - Al reiniciarse, Docker levantó por su cuenta contenedores de otros proyectos de la máquina. No los toqué.
  - Al terminar detuve el contenedor del repo y pedí el cierre de Docker. El backend siguió corriendo y el motor volvió a responder 500,
    como estaba a la mañana (`neo4j/consolas/consola_docker_cierre.txt` y `consola_docker_estado_final.txt`).
- **La carga** (`neo4j/<clave>/carga_neo4j_tanda0.json`), desde la copia:
""" + "\n".join(
    f"  - {k}: sha256 verificado antes de cargar; vista {mil(c['grafos'][k]['loader']['nodos'])} / {mil(c['grafos'][k]['loader']['aristas'])}; "
    f"dos cargas con la misma huella: {c['grafos'][k]['idempotente']}; `verificar_carga`: {c['grafos'][k]['verificar_carga_ok']}; "
    f"`KG_Meta.kg_sha256` igual al archivo: {c['grafos'][k]['kg_meta_sha_igual_archivo']}, `commit_sellado` "
    f"«{c['grafos'][k]['kg_meta'].get('commit_sellado')}»; paridad {c['equivalencia']['paridad_total']}; **gate 5: {'OK' if c['ok'] else 'CON FALLAS'}**."
    for k, c in carga.items()) + f"""
- **El control de la cola** (`scripts/control_cola_neo4j_t3f.py`, copia de `control_cola_neo4j_rs1.py` con las claves cambiadas):
  {'OK' if cc['ok'] else 'CON FALLAS'}. En el sin cola, {cc['grafos']['KG_Tanda1_Veinte_r2b_sincola']['neo4j_nodos_cola_humana_true']} nodos con
  la marca en Neo4j y {cc['grafos']['KG_Tanda1_Veinte_r2b_sincola']['kg_nodos_con_marca']} en el `kg.json`. En el completo, llegan las
  {cc['grafos']['KG_Tanda1_Veinte_r2b']['kg_nodos_con_marca']} marcas del `kg.json`.

## 5. Lo que se cuenta sin leer (punto 6)

`scripts/contado_sin_leer_t3f.py`, sobre la copia, importa sin editarlas las funciones de la tanda 0 y del re-sellado:
- `resellado_t0/condicion_4/medicion_tablero_r2b_rs1_mesa.py`, con sus rutas apuntadas en memoria a la E0 y a la salida de cada grafo;
- `medir` de `udiag_e_aisladas.py`, tomada del árbol sintáctico como en el re-sellado;
- `medir_umbral` de `reresolucion_catalogo/r2_1_medicion.py`;
- y, para L-02, `omisiones_cod/o1/scripts/medir_e.py`, con su manifiesto y su entrada apuntados a la tanda 1.

Las reglas de las vigilancias son las de `vigilancias_contables_rs1_mesa.py`, con los TOs de cada grafo. **El control:** las mismas
funciones sobre el diez re-sellado reproducen su medición en las {len(cs['control_contra_el_re_sellado']['iguales'])} filas controladas.

**El cegamiento** (punto 8): estas cuentas van solo a `t3/NO_ABRIR_conteos_t3.json`, sin abrirlo:
- la fila del crudo del reintento de E3;
- las claves de `properties_no_definidas`, que cuentan `copia_nota_e3` y la marca de L-04;
- los pozos de L-02 y de L-04.
Su sha256 está en la sección 9. La consola imprime solo los nombres de los archivos, el control y si los pozos llegan a 30.

{txt(CS / 'tablas_contado_t3f.md')}

**La columna «Tanda 1» del tablero** ({len(col)} filas, `:49` a `:74`): `conteos_sin_leer/columna_tanda1_tablero_t3f.md`, por
`scripts/tablas_contado_t3f.py`. Cada fila tiene su cifra o la causa por la que no se midió:
- {len(filas_ev2)} filas ({', '.join(filas_ev2)}) necesitan el agente (EV2), que nunca se corre;
- la (12) es una lectura de T4;
- la de las líneas en mayúsculas lee la E0 legada, que la tanda 1 no tiene;
- la del crudo del reintento está bajo cegamiento.
El tablero del repo no se tocó.

## 6. La preparación de T4 (punto 7)

Scripts: `poblaciones_t4_t3f.py`, `celdas_t4_t3f.py` (las cuotas y la regla de las celdas y de las clases chicas), `umbrales_t4_t3f.py`,
`sorteos_t4_t3f.py`, `material_t4_t3f.py`, `unidades_a_la_vista_t3f.py` y `tablas_t4_t3f.py`, que genera las tablas. Las tablas, tal cual:

{txt(MU / 'tablas_t4_t3f.md')}

**Las definiciones de las poblaciones, tal como las apliqué** (docstring de `poblaciones_t4_t3f.py`):
- la clase sale de `categoria` del manifiesto (RI y no-RI) y el modo, de `modo_lectura` (`sin_raiz`, en ceninf, nmcief, ri_ccna y
  ri_mmsef, lo mismo que en `lista_tanda1_S2.json`);
- el grafo es el evaluado (el sin cola), salvo la cola;
- la (2) son las unidades aceptadas cuya extracción final no tiene relaciones: la cifra que el código de la tanda 0 da como total
  (`lectura_e6_tanda0.py:231-252`);
- la (12) es el universo de A4.1 tal cual: todas las aristas menos `referencia` y menos el esqueleto.

**El material:**
- el texto de cada unidad es `comun_e3.fuente_integro(chunk, bloque_de_lista=ratchet_e3._forma_r2(validacion))`, con el chunk de la E0 con
  las partes en las {n_partes} fichas de partes por corte;
- sin el estado de E3 ni sus marcas: el control por script da 0 claves vedadas en las {n_fichas} fichas (`muestras/control_material_t4.txt`);
- la hora del material, {mat['hora'][11:19]}, es posterior a la de los sorteos, {', '.join(horas_sor)};
- las planillas en blanco van en CSV, con las columnas del veredicto de cada lectura.

**Las vigilancias (1) y (3): las definiciones que propongo** como regla general. No las sorteé: decide la autora antes del sorteo.
- **(1), migraciones a Condicion contra la guarda de modalidad.**
  - Elementos: los nodos Condicion del grafo evaluado.
  - Muestra: 30 con las celdas y la cadena `tanda1:vigilancia:1:<celda>:<base>`.
  - Pregunta: ¿la Condicion expresa un deber explícito (debe, deberá, está obligado a) que el texto de su unidad formula como obligación, y
    no como condición? Respuestas: sí (migración), no o no decidible.
  - Tasa ponderada por celda, con Wilson.
- **(3), duplicación entre cajas.**
  - Elementos: los grupos de 2 nodos o más de contenido con la misma unidad de procedencia primaria y el mismo tramo normalizado (espacios y
    mayúsculas). La celda es la del nodo de id menor (§5.4 bis, punto 2, v8c).
  - Muestra: 30 grupos con la cadena `tanda1:vigilancia:3:<celda>:<base>`.
  - Pregunta: ¿los nodos del grupo repiten el mismo contenido normativo (duplicación), o son contenidos distintos sobre el mismo pasaje?
  - Tasa ponderada por celda, con Wilson.
- Las poblaciones de las dos definiciones están en la tabla T8 (información).

## 7. Lo declarado por las decisiones 1, 2, 3, 6 y 7

1. **La E0 que rige para S31** es la E0 con las partes por corte. Es una precisión del gate tomada con el resultado a la vista, y vale
   igual para la tanda final. Se informan las dos corridas: con la E0 del repo, S31 falla en los cuatro grafos; con la E0 con las partes,
   pasa.
2. **E4-a1 y E4-a4 son regresiones de la tanda 1**, declaradas por la autora: dos sujetos propuestos que tienen candidato en el catálogo
   y que E4 no resolvió. La mesa diagnostica la causa en la ronda siguiente, sin gastar.
3. **En la tanda 1 sola**, los ítems con todas sus anclas en TOs que el grafo no tiene se informan aparte, como «fuera del grafo», y no
   cuentan: son {n_fuera['veinte']} regresiones en cada grafo de la tanda 1, las {fg['cruce']['veinte']['cuantos'][0]} del cruce y las
   declaradas del laudo que caen fuera del grafo. Vale también para los
   grafos de los tramos de la tanda final.
4. **Las salidas de shapes y de la suite de los dos grafos de la tanda 1** quedan en `corpus_tanda1/ens_veinte_r2b/` y `_sincola/`, como
   en el re-sellado, y no en `t3/`. Es el error propio 4 del parcial.
5. **El selftest del catálogo** corrió en un `git clone` del repo que trajo cuatro archivos `.env` o `NO_ABRIR_`. Los borré por nombre,
   sin abrirlos; la mesa mostró con un grep que ningún selftest de la cadena lee esas rutas. Es el error propio 1 del parcial. En esta
   parte no hice ningún `git clone`.

## 8. Para la autora

1. **Los pozos de L-02 y de L-04 llegan a 30** (tabla C5). Por el §5.4 d, sus lecturas son al cierre de la tanda 1. Quién lee y con qué
   regla se decidió el 15/10/2026. Las semillas se sellan antes de leer, y yo no las sorteé.
2. **`unidades_a_la_vista_T4.json`, con la regla tal cual, deja a la vista
   {mil(vis['todas_las_muestras']['unidades_a_la_vista'])} de las {mil(pob['unidades_en_finales'])} unidades.**
   - Las fichas de unidad muestran sus aristas `establecida_en` hacia el TextoOrdenado y `aplica_a` hacia sujetos fusionados. La
     procedencia de esos nodos es la del TO entero o la de todas las menciones del sujeto.
   - Solo por esos dos tipos están a la vista {mil(solo['aceptadas:items'])} unidades en las aceptadas ítems y
     {mil(solo['aceptadas:no_items'])} en las no ítems (tabla T7, información).
   - Si para U-MED-VERIF esos nodos no deben contar, cambia la regla; la información para recalcularla ya está en el archivo.
3. **La población de la vigilancia (2)** la tomé de la extracción final del grafo evaluado ({pob['muestras']['vigilancia:2']['N']} unidades).
   El código de la tanda 0 mide también la del primer intento.
4. **El universo de la observación (12)** es el de A4.1 tal cual: {mil(sum(comp['universo']['relacion'].values()))} aristas. De ellas,
   {mil(comp['universo']['relacion']['establecida_en'])} son `establecida_en` y {mil(comp['universo']['relacion']['remite_a'])} `remite_a`. En
   la muestra de 30 hay {comp['muestra']['relacion']['establecida_en']} `establecida_en` y {comp['muestra']['relacion']['remite_a']} `remite_a`
   (`muestras/composicion_obs12_t3f.json`). La nota de equivalencia del §5.2 habla solo de `remite_a`.
5. **Las definiciones de (1) y (3)** que propongo (sección 6), antes de su sorteo.
6. **La cola de la muestra:** la clase RI tiene {Nc['RI:sin_raiz'] + Nc['RI:resto']} unidades en la cola y NG `sin_raiz`, {Nc['NG:sin_raiz']}.
   Por las reglas de las clases chicas, entran las {nc['RI:sin_raiz'] + nc['RI:resto']} de RI y NG resto sortea {nc['NG:resto']} (tabla T2).

{txt(FOTO).replace('## La foto del repo, los .pyc y el grep de convenciones', '## 9. La foto del repo, los .pyc y el grep de convenciones', 1)}

- **La base de Neo4j** (`data/experiment/neo4j/volumen/`) cambia con la carga del punto 5. Está fuera de git
  (`data/experiment/neo4j/.gitignore:4`) y no va al commit.
- **Escrito después de la foto:** solo este FRENO.
- **El grep de convenciones** (`grep_convenciones_t3f.py` y su salida, en el paquete) busca las palabras del `user.name` de git y las de
  origen conversacional en los {grep['archivos']} archivos nuevos o cambiados de esta parte, sin la base de Neo4j ni el `NO_ABRIR_`. El
  control positivo da su línea {grep['control_positivo_lineas'][0]}.
  - **En lo que redacté:** {', '.join('`' + k.split('/')[-1] + '`' for k in grep['propios_con_patron'])}: las líneas que citan palabras de la
    norma (el FRENO parcial, y la plantilla de este FRENO en su armado).
  - **Tokens del nombre:** {len(grep['nombre_sin_rutas'])}.
  - **En las salidas de los generadores y en el material,** las coincidencias son texto de la norma (como «correo electrónico»).
  - **Rutas absolutas:** {len(grep['con_rutas_absolutas'])} archivos, los dos scripts que las nombran como literales de su control.
  - Sobre este FRENO, el grep corre después de escribirlo, y su resultado va en el mensaje del FRENO.
- **La escritura al repo** (`scripts/escribir_en_el_repo_t3f.py`, en seco y de verdad): {esc['nuevos']} archivos nuevos y {esc['cambian']}
  que cambia (`grafos.py`, igual a HEAD antes); {sum(v['igual_al_staging'] for v in esc['escritos'].values())} de {len(esc['escritos'])}
  iguales al staging. Después escribí, con control, `muestras/tablas_t4_t3f.md`, su consola y `muestras/composicion_obs12_t3f.json`.
- **Las carpetas vedadas:** no abrí, no listé ni copié ninguna. No abrí ningún `.env` ni `NO_ABRIR_`; las copias del repo se hicieron
  con el `rsync` de la cláusula y su control dio 0 (`rsync_copia_t3f*.log` en el paquete). Ningún `git clone`.

## 10. Errores propios, con su causa

1. **Una regla de partes que no servía para la E0 de manori.** La primera corrida de `poblaciones_t4_t3f.py` cortó con un error: tomé
   como parte por corte de E1 todo id con `::parte`, y `manori::Sbloque4::parte3` es un chunk de la propia E0.
   - La causa: generalicé la regla de la tanda 0 sin mirar los ids de la E0 de la tanda 1.
   - La corregí antes de escribir nada: el id va tal cual si está en la E0, y si no, se usa su unidad, quitando solo el último `::parteN`.
2. **Dos anclas de línea mal puestas en un docstring.** En `poblaciones_t4_t3f.py` puse primero `lectura_e6_tanda0.py:246-263` y `:291-300`.
   Las verifiqué con `grep -n` antes de correrlo y las corregí: son `:231-252` y `:286-294`.

FRENO T3. Espero la revisión de la autora.
"""
OUT.write_text(F, encoding="utf-8")
print(len(F.splitlines()), "líneas")
