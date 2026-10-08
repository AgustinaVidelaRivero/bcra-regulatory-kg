# U-UNION-ESTRECHA — FRENO U2-a (fichas, criterio y primera lectura, sellados; sin la cifra)

Primera lectura de una sesión aparte, que no diseñó la regla (mandato firmado en `21e55a0`, decisión 2 al firmar), sobre
el censo de las 29 uniones del marco (decisión de la autora del 08/10/2026, nota al pie del mandato). USD 0, sin API,
nada commiteado. Este freno no trae la cuenta de veredictos ni ningún veredicto: la segunda lectura de la mesa es a
ciegas.

## 1. Lo hecho

- **Controles de entrada.** `git log --oneline -- data/experiment/union_estrecha/regla_u1.md` muestra `57c2123` (el
  commit de U1). sha256 de `regla_u1.md` = `9f5028d1…164c` y de `salida/marco_u2_diez.json` = `69177a21…097c`: los dos
  iguales a los del despacho.
- **Fuentes del mandato.** Texto firmado leído con `git show 21e55a0:docs/mandatos/UUNION_ITEM_ENCABEZADO_regla_estrecha.md`
  (sha256 de esa salida `6959ca49…ee63`, 80 líneas); las notas al pie, con `git diff 21e55a0 HEAD` sobre el mismo archivo
  (una sola nota, la del 08/10/2026). De `freno_u1.md`, las secciones 2 y 3 (`:34-73`).
- **Copia sin enlaces** en el scratchpad, con `git show` de `ae76f08` (HEAD): el grafo `a9631a64` (`data/experiment/neo4j/grafos.py:138`,
  `KG_Tanda0_Diez_r2b`), los `chunks_<to>.json` de E0 r2b de los 10 TOs de la tanda 0 (iguales byte a byte a los del
  repo), `registro_u1_diez.json` (`47f44599…36bb`), `marco_u2_diez.json` y `grafos.py`. 0 enlaces.
- **Fichas** (`fichas_u2.py`; `python -I -B fichas_u2.py FUENTES SALIDA`): 29 fichas, `U01` a `U29` en el orden del
  marco, en `fichas_u2.json` y `fichas_u2.md`. Cada una trae la Condicion del ítem (id, descripción y sus tramos con la
  unidad de cada uno), el texto entero de la unidad del ítem (texto propio y herencia de E0), el nodo destino (id, tipo,
  descripción y tramos) y el texto entero de la unidad del encabezado, con su herencia. Sin campos de la regla y sin
  veredicto: del registro, el script usa `resultado` y `en_control_diagnostico` solo para controlar que cada id sea una
  unión y no esté en el control, y no los pasa a la ficha. 27 unidades de ítem y 16 de encabezado distintas. Dos
  corridas iguales byte a byte; `comandos_u2a.sh` lo reproduce sobre un directorio nuevo (sellos iguales, dos corridas
  iguales e iguales a las del repo, 0 enlaces, 0 `.pyc`, `git status` del repo igual antes y después).
- **Criterio** (`criterio_u2.md`): el del mandato, con ocho precisiones escritas antes de leer la primera ficha: se
  juzga la unión y no la extracción de los nodos; qué es la norma del encabezado; «condición de» acumulativa o
  alternativa; jerarquía (sublistas, aclaraciones, excepciones y notas de procedimiento); la Condicion es la de su tramo;
  el texto es solo el de la ficha (sin PDF, sin otras unidades, sin campos de la regla); el tramo que sostiene cada
  veredicto; las no decidibles cuentan como no correctas.
- **Sello antes de leer** (`sello_fichas_u2.txt`, 2026-10-08T10:54:03-0300): sha256 de `criterio_u2.md` (`86c7724c…986e`),
  `fichas_u2.py` (`5918f01a…9aa3`), `fichas_u2.json` (`888d0b76…a771`) y `fichas_u2.md` (`7ab2812e…356d`).
- **Primera lectura** (`lectura1_u2.json`): una entrada por ficha, con `veredicto`, `tramo` literal, `unidad_del_tramo` y
  `nota`. Control de forma antes de sellar: los 29 ids son los de las fichas y los 29 tramos son subcadena de la unidad
  declarada (herencia y texto propio, con los blancos normalizados). El script que arma el JSON y hace ese control quedó
  en el scratchpad y no va al paquete, porque contiene los veredictos.
- **Sello de la lectura** (`sello_lectura1_u2.txt`, 2026-10-08T10:58:04-0300): `lectura1_u2.json` = `8b23d250…631c`,
  con los cuatro sha de las fichas y el criterio repetidos e iguales. Después del sello no conté veredictos ni comparé
  nada.

## 2. Declaraciones (desvíos propios, con su causa)

1. **Vi el texto de una unión antes de escribir el criterio.** Para escribir el script inspeccioné el formato de las
   fuentes con una unión real: imprimí los dos chunks de la primera del marco (`ext::3.15.2::intro` y `ext::3.15.2.4`,
   la ficha `U01`) y su nodo destino, y los ids de unidad y destino de la segunda (`U02`). El criterio (mtime
   10:53:09) se escribió después de eso, aunque antes de generar las fichas y de leer ninguna. Causa: usé una fila real
   como muestra de formato en lugar de mirar solo las claves. Las precisiones son generales y ninguna nombra un caso; lo
   declaro para la adjudicación.
2. **Vi los nombres de los campos de la regla.** Al inspeccionar la estructura del registro vi los nombres de sus campos
   (entre ellos `candidatos`, `resultado` y la tabla `encabezados`, con forma, subforma, subordinante, marca de
   excepción, segmento y compatibles) y una entrada de esa tabla, de un bloque de cap que no está en el marco. No los
   usé para leer; las fichas no los traen.
3. **`freno_u1.md`:** además de §2 y §3 vi los títulos de sus cinco secciones (un `grep -n '^#'`, para ubicar las dos
   permitidas). No leí el cuerpo de §1, §4 ni §5.
4. **Lo que no abrí:** nada bajo `reports/u_diag_cap3_grafo/` (ni `lecturas/`, ni `lectura1_41_exceptua_operacion.json`,
   ni `salidas/`), `regla_u1.md` más allá de su sha256, el código de la regla y de la pre-medición, ni el paquete de U1.
   Leí, sin escribir, `sello_regla_u1.txt` y las primeras 50 líneas de `comandos_u1.sh` (para armar la copia con el mismo
   patrón) y `data/experiment/alcance_e1/scripts/foto_repo.py`, copiado al scratchpad para la foto del repo.
5. **`comandos_u2a.sh` no está en el sello:** lo escribí después de sellar la lectura, para que la mesa reproduzca las
   fichas; verifica el sello de las fichas, del criterio y del script antes de correr y no abre la lectura.

## 3. Controles

- **Repo: foto sha256 de todos los archivos (salvo `.git`)**, con una copia en el scratchpad de
  `data/experiment/alcance_e1/scripts/foto_repo.py`. Antes: 2026-10-08T10:50:51-0300, HEAD `ae76f08`, 47.753 archivos.
  Final: 2026-10-08T11:01:24-0300, 47.765 archivos. Fuera de `docs/`, la única diferencia son los 9 archivos nuevos de
  `data/experiment/union_estrecha/u2/`; ningún archivo existente fuera de `docs/` cambió ni se borró.
- **En `docs/` hubo cambios que no son de esta sesión.** Mientras esta sesión escribía solo en `u2/` y en el scratchpad,
  cambiaron 9 archivos (`checklist_pre_escalado.md`, `enmienda5_protocolo_entre_tandas_2026-10-06_grafo_evaluado_sin_cola.md`,
  `insumos_escritura.md`, `laudo_release_r2_pipeline.md`, `plan_tesis.md` y, en `mandatos/`,
  `UALCANCE_E1_cableado_registro_alcance.md`, `UCOMP_E1_comparacion_chica_modelo.md`, `UDIAG_vinculo.md` y
  `USINCOLA_T0_grafo_evaluado_sin_cola.md`; `git diff --stat`: +39 −10) y aparecieron 3
  (`enmienda6_protocolo_entre_tandas_2026-10-08_cambio_de_modelo_del_extractor.md`, `fe_erratas_forma_A_denominador.md`
  y `mandatos/UCOMP_E1_C4_lectura_pareada.md`), con mtimes de 10:56:02 a 11:01:16, y entre la foto de las 11:00:14 y la
  final seguían apareciendo. Los atribuyo a otra sesión que trabaja en paralelo sobre `docs/`; no abrí su contenido. El
  mandato de esta unidad no está entre ellos. El control «solo cambia `u2/`» se cumple para lo que escribió esta
  sesión, no para el repo entero: lo dejo a la vista de la autora.
- **`.pyc`:** 2.213 antes y después (`find` del repo sin `.git` ni `.venv`); 0 en el scratchpad.
- **`git status --porcelain`:** antes, las 8 entradas `??` de la foto de entrada; después, esas 8, `?? data/experiment/union_estrecha/u2/`
  y las 12 de `docs/` del punto anterior.
- **Grep de convenciones** (los patrones, en el paquete). Referencias al origen de una decisión (canales de mensajería,
  encuentros y atribuciones de autoría) sobre lo escrito en esta sesión (criterio, script, comandos,
  freno, sellos y lectura): 0. Rutas absolutas sobre los 9 archivos de `u2/`: 0. Control positivo: 1 y 1. Nombres de
  personas, revisando a mano las palabras con mayúscula inicial de lo escrito: 0 (la única que no es término técnico ni
  de la norma es «Wilson», el nombre del intervalo).
- **Paquete:** `revision_UUNION_ESTRECHA_FRENO_U2a/` en el scratchpad, con `manifest.txt`. No trae la lectura: trae su
  sello, que solo tiene el sha256.

## 4. Para el commit de la autora (PENDIENTE)

`data/experiment/union_estrecha/u2/`: `criterio_u2.md`, `fichas_u2.py`, `fichas_u2.json`, `fichas_u2.md`,
`sello_fichas_u2.txt`, `lectura1_u2.json`, `sello_lectura1_u2.txt`, `comandos_u2a.sh` y este `freno_u2a.md`. Si la
lectura no debe quedar a la vista de la mesa en el repo antes de su segunda lectura, la decisión de cuándo commitearla es
de la autora; el despacho dice que va en el repo y que la mesa no la abre hasta sellar la suya.

## 5. Lo que sigue (no es de esta sesión)

- Segunda lectura a ciegas de la mesa sobre las mismas fichas y el mismo criterio, sellada antes de comparar: PENDIENTE.
- Adjudicación de las divergencias por la autora: PENDIENTE.
- FRENO U2 con la cifra (correctas de 29, límite de Wilson y si pasa el piso de 27): PENDIENTE, después de la
  adjudicación.

FRENO U2-a.
