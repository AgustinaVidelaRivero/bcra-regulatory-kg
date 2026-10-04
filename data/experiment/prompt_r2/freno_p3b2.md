# U-PROMPT-R2 — FRENO P3b-2 (implementación)

04/10/2026. HEAD `918b9c5` al empezar y `9068ab5` al cerrar. `9068ab5` es de la autora: trae al mandato las
decisiones para P3b-2 y no toca la cadena. USD 0, sin API y sin commit. El detalle de cada control está en `p3b2/` y
en el paquete de revisión.

**Fuentes.** Leí la nota de `9068ab5` al pie del mandato: coincide con el «seguí» de P3b-2.
- **Diferencia con el «seguí».** P3b-1 está commiteada en `023f9a0`, no en `918b9c5`. Ese hash es el diseño de C2
  de U-R2-CODIGO-2. Mandan los archivos.
- **Antes de editar** miré `git status` y `git log`: la implementación de C2 no estaba en curso. No la hay al cerrar.

## 1. El prefijo re-congelado

| | Valor |
|---|---|
| Hash canónico | `3817de475c93` (antes `14d6b63b508e`) |
| sha256 del system | `8d84364fc3b6f6b586ff09e11833a2328408ae6f93b081c8ae64a059ea839c8b` |
| Caracteres | 55.105 (antes 51.780) |
| Tool schema | sin cambio, `0c391f2b…` |
| Namespace de E1 | `e1_extraccion\|cv=e1-extractor-v1-p3817de475c93\|think=0` |

- **El parche:** los 12 reemplazos aprobados están en `e1_extractor/prompt_r2b_parche_p3b.json` (sha256
  `8679ea12…`), y se aplican sobre el prefijo de P2, con candado.
- **Candados:** `prompt_r2b.py`, `perfil_e1.py` y `selftest_manifiesto.py:503`. Esa línea es la que fijó P2 en
  `20b7f60`; el mandato pone el archivo entre las escrituras del perfil.
- **El mensaje de E1:**
  - lleva g y h: 1.053 ítems y 121 mini-chunks;
  - lleva la línea del recorte de E0, solo en un chunk con `herencia_recortada`. Ninguno de la tanda 0 la tiene
    todavía: la pone C2;
  - es igual al borrador aprobado en las 2.434 unidades, y al de P1 en las 1.260 que no cambian.
- **E3:** la NOTA de las omisiones va en `notas_r2` cuando la validación r2 declara `meta_normativo`,
  `fuera_de_tipos` o `relacion_sin_predicado`. El prefijo de E3 no cambia (`21a836c7de6d`).

## 2. Lo implementado, por decisión

| Decisión | Dónde | Qué hace (solo con la forma r2) |
|---|---|---|
| j, opción 1 | `ratchet_e3.evaluar_veredicto` | un `faltantes` como texto se lee con la regla de P3b-1 (`json.loads` o reparo); el veredicto lleva `lectura_faltantes` y la unidad, `marcas_e3.lectura_veredicto_e3` |
| k4 | `ratchet_e3.ciclo_ratchet` | aceptado tras un reintento con menos entidades o relaciones: `marcas_e3.reintento_con_menos_elementos` con los dos conteos |
| Defensa 1 | `ratchet_e3.bloque_feedback` | el aviso aprobado al final del feedback del reintento |
| Defensa 2 | `ratchet_e3.copias_nota`, `validador_r2`, `e2_lib` | la regla de P3b-1 marca la entidad, sin rechazar; la marca llega al nodo en `properties_no_definidas.copia_nota_e3`, y también queda en `copias_nota_e3.jsonl` |
| `todo` de la cola | `RegistroE3.cola_humana` | dice que la unidad entra marcada y se revisa por la muestra de la tanda |
| l | `validador_r2.derivar_comunicacion_tramo` | el tipo sale del tramo verificado: una Comunicación nombrada da su letra (también en una enumeración) y el número se controla contra el código; una norma externa da «externa»; si no, no se deriva |
| h | `validador_r2.verificar_tramo_entidad` | en un mini-chunk a mitad de oración, el tramo simple se verifica también en orden de lectura, contado aparte |
| Modalidad | `validador_r2.clasificar_modalidad` | `properties_no_definidas.modalidad_clasificada`, con una lista cerrada (`MODALIDAD_FORMAS`) |
| Unión de operaciones | `e2_lib.entity_slug_r2` | en la fase r2b, la Operacion se une por etiqueta dentro de su punto |
| Relación → arista | `e2_lib.ensamblar_r2` | en la fase r2b, `properties_no_definidas` pasa a la arista; la primera procedencia gana y la diferencia va a los conflictos |
| Claves nuevas aparte (decisión 7 del mandato, `9068ab5`) | `e2_lib`, `stats["p3b"]` | cuenta aparte los nodos con `modalidad`, `consecuencia`, `modalidad_clasificada` y `copia_nota_e3`, las aristas con la clave y las unidades con marcas que llegaron |

- **Cómo llega la fase a E2:** `ensamblar_r2(…, fase="r2a")`, por defecto la salida de siempre. Una línea en cada
  sitio de llamada: `ensamblar_tanda0.py:826` y `runner_corpus.py:1067`. Pasan `fase="r2b"` con un perfil de forma
  r2.
- **`runner_corpus.py` fuera de esa línea (agregado de la autora):** `vistos_por_e3`, líneas 945 a 951. Si la
  validación final trae la marca de la copia, la pasa en `vistos_e3["marcas"]`. Con los perfiles existentes la salida
  es la misma byte a byte, porque la clave no existe.
- **Lo que no llega a E2:** las marcas de j y k4 quedan en `finales.jsonl` (`validacion_final.marcas_e3`) y en
  `veredictos.jsonl`. El permiso del agregado era solo para la marca de la copia. k4 se cuenta por tanda desde
  `finales.jsonl`, y la cadena sintética lo muestra.
- **Comentario alineado:** la docstring del ratchet decía «nada ingresa al grafo» para la cola. Ahora dice que lo
  decide la cadena de ensamblado y que, en r1 y r2, entra marcado. Es lo que P3 dejó para el parche siguiente.

## 3. Controles

**Sellados** (`control_reproduccion_p3b2.py`, sobre una copia):
- los dos grafos r2a dan `99fe2bfa…` y `93a7af72…`;
- los tres ensamblados r1 dan 13 de 13: 10 archivos byte a byte y 3 iguales con la ruta normalizada;
- el repo no cambió.

**Unión de las operaciones** (`p3b2/salida/union_operaciones_p3b2.json`, con la lista y sus puntos):

| | Desarrollo | Diez |
|---|---|---|
| Operacion que juntan más de un punto | 37 → 89 nodos | 59 → 148 |
| Por TO | ext 29, cap 5, cla 3 | ext 29, ctacte 16, cap 5, pagjub 5, cla 3, polcre 1 |
| Uniones dentro de un mismo punto | 5, sin cambio | 5, sin cambio |
| Aristas que tocan esas operaciones (`remite_a`) | 589 (439) → 722 (510) | 711 (481) → 892 (559) |
| Aristas del grafo | 24.728 → 24.853 | 29.499 → 29.672 |
| Adjudicación de colisiones entre TOs | 1 → 0 | 3 → 0 |
| Conflictos reales de E4 | 135 → 51 | 195 → 57 |

- **Cada grupo es un nodo:** cada grupo (TO, punto) de procedencias de una Operacion sellada es un nodo del grafo
  nuevo, con el id de la regla y esas procedencias. Los demás nodos son iguales.
- **Aguas abajo, además:**
  - cambian 7 aristas `remite_a` que no tocan una Operacion. En las dos, la Condicion de `ext::13.4.7` deja de ser
    origen de la remisión a `ext::4.8.5`: la regla de atribución pasa de «todos los nodos del punto» a «contiene la
    unidad»;
  - el registro de remisiones pierde 4 filas en cada grafo. Las transiciones están en el JSON.
- **Los conflictos de E2 por TO** también bajan, en la misma tabla del JSON.

**No-filtración** (`nofiltracion_p3b2.py`, con la regla y la población de P3b-1, sobre los textos del código):
- 5.376 chunks;
- 0 choques de las 610 ventanas del prefijo y de las 267 de los literales, de las que 37 son de la línea del recorte;
- 0 bigramas o trigramas de los casos de control.

**Cadena sintética** (`cadena_sintetica_p3b2.py`):
- **Recorrido:** ratchet con stubs → `finales.jsonl` → `entrada_r2` → validador → E2 r2b → ensamblado r2b.
- **Resultado:** 20/20 en las dos corridas, con el mismo resumen y el mismo grafo (`c21263d452a8…`).
- **La cadena de P3** da 26/27 con el código nuevo. El caso que cambia es su «LÍMITE»: la arista ya lleva las
  `properties_no_definidas`. En HEAD da 27/27, igual a su resumen commiteado.

**Selftests,** sobre la copia de cierre:

| Selftest | Antes (HEAD) | Ahora |
|---|---|---|
| `selftest_prompt_r2b` | 23/23 | 34/34 |
| `selftest_e3` | 80/80 | 95/95 |
| `selftest_pyd_r2` | 332/332 | 343/343 |
| `selftest_e2` | 35/35 | 41/41 |

- **Los otros 15 selftests que importan algo tocado** dan lo mismo con y sin P3b-2 (las dos copias, en el
  paquete). Entre ellos, `selftest_manifiesto` da 44/49: los 5 fallos son los de P5 sobre una copia.
- **Fallan igual en las dos copias,** por el entorno:
  - `selftest_catalogo_unico` necesita git;
  - `selftest_dirigida_tanda0` encuentra la base de E1 de la copia con `-wal`.

**Repo y `.pyc`:**
- el repo no cambió durante el cierre;
- no hay `.pyc` nuevos;
- `git status`: solo mis escrituras, más los archivos de figuras de otra sesión que ya estaban al empezar.

## 4. Lectura de los 45 casos y costo

**Copia de la nota.** La regla quedó fijada antes de leer (`regla_lectura_copia_nota.md`), y la lectura está en
`lectura_copia_nota.md`.
- **Resultado:** 11 copias reales en 11 unidades, 34 coincidencias legítimas en 29 y 0 dudosas.
- **Qué traen las 11:** 4 traen contenido de la nota y 7 solo agregan un verbo o una nominalización.

**Costo** (`costo_p3b2.py`; deltas sobre la base de P1, con sus calibraciones):

| | Base | Con P3b |
|---|---:|---:|
| U-REEXT-T0, central | 49,13 | 50,74 |
| U-REEXT-T0 × 1,4 | 68,78 | **71,04** (tope fijado: 69) |
| P4 central / alto | 1,11 / 1,63 | 1,12 / 1,65 |

- **El mayor delta es la NOTA de E3:** USD 0,99, como cota alta en las 2.681 llamadas; la tanda 0 no trae
  categorías.
- **Sin la NOTA,** U-REEXT-T0 sería 49,75 y, con el factor, 69,66: también pasa el tope.
- **No estimado:** la salida de a, b y h. La mide P4.

## 5. Para la decisión de la autora

1. **El tope de U-REEXT-T0:** con el factor 1,4, la estimación pasa los USD 69 fijados.
2. **La política r2:** el paso `derivar_de_codigo_o_label` de `politica_campos_r2.json` lee el tramo con la forma
   r2. El texto de la política, sellado por su sha, sigue diciendo código o etiqueta. ¿Hace falta una nota?
3. **La lista cerrada de la modalidad (`MODALIDAD_FORMAS`)** es mía y no se midió. Hay prefijos amplios, como
   «cargo» y «baja», que P4 dirá si sobran.
4. **Las marcas de j y k4 en el reporte de E2:** llevarlas también por `vistos_por_e3` es el mismo cambio de dos
   líneas, sin autorizar.
5. **h cubre el tramo simple.** Un tramo de dos segmentos en un mini-chunk a mitad de oración no se lee en orden de
   lectura.

**Error propio, con su causa.** El freno de P3 (`4aa92c7`) dice que los tres ensamblados r1 dan «3 iguales con la
ruta normalizada».
- **Lo que daba su propio JSON:** 2 iguales y 1 distinto, `r1/reporte_ensamblado_r1.json`. La diferencia era solo de
  rutas: la entrada queda relativa en la reproducción y absoluta en el sellado.
- **La causa:** la normalización no quitaba la raíz, y escribí el conteo sin recomputarlo contra el JSON.
- **La corrección:** el control de P3b-2 normaliza también la raíz y da 13 de 13. El freno de P3 está commiteado y no
  lo edito.

**Pendiente de la autora:** las decisiones 1 a 5 y el commit de P3b-2.
