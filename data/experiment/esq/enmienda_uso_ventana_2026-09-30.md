# Enmienda al laudo de esquema congelado — uso de la ventana única del §7 en el ciclo posterior a la tanda 0

**BORRADOR — PENDIENTE DE FIRMA DE LA AUTORA** · Fecha: 2026-09-30.

Enmienda con fecha al laudo `data/experiment/esq/laudo_esquema_congelado.md`
(FIRMADO 03/09/2026, sellado en `2593d4d`), §7, y a su enmienda del 25/09/2026
(`data/experiment/esq/enmienda_ventana_correccion_2026-09-25.md`, FIRMADA, sellada
en `c80b03f`, sha256 `3646f2ae…`). Ninguno de los dos se edita: esta enmienda vive
al lado y se lee junto con ellos. La acompaña la enmienda al pre-registro de la
tanda 0 de la misma fecha (`docs/enmienda_preregistro_tanda0_2026-09-30_ventana.md`).
Base: decisión de la autora del 30/09/2026 (`docs/checklist_pre_escalado.md`, X3;
`docs/plan_tesis.md`, fila B2.11).

## 1. Lo que dicen hoy el §7 y la enmienda del 25/09

El §7 del laudo (`laudo_esquema_congelado.md:169-174`) admite un solo ciclo de
corrección si aparece una clase nueva de falla de esquema, no de pipeline, con
laudo propio y re-extracción incluida, siempre antes de sellar el pre-registro de
B6.3. Sellado ese pre-registro, la ventana muere y toda corrección posterior es
release posterior (principio 9 del plan; laudo, línea 202).

La enmienda del 25/09 fija cuatro precisiones que esta enmienda toca:

1. **Qué la abre** (`enmienda_ventana_correccion_2026-09-25.md:67-74`): solo una
   falla de esquema que produzca falsedad en campo estructurado en material
   fresco. Una falla de pipeline, de catálogo, de índice o de ensamblado no la
   abre.
2. **Cómo se usa** (`:75-79`): un ciclo con laudo propio y re-extracción incluida
   (de la tanda 0 si se abre en la tanda 0), antes de sellar el pre-registro de
   B6.3.
3. **Una sola ventana** (`:80-82`): abrirla tras la tanda 0 consume la de la tanda
   1; no hay dos ciclos.
4. **Consecuencia sobre el conjunto que informó el esquema** (`:83-92`): si se abre
   tras la tanda 0, los cinco documentos de la tanda 0 dejan de ser vírgenes
   respecto del esquema y el conjunto fresco de B6.3 (a) los excluye igual que a
   los 15 ya excluidos.

## 2. Qué decide esta enmienda

1. **Uso.** La ventana única del §7 se usa en el ciclo de corrección posterior a
   la tanda 0 (plan, fila B2.11). Es el único ciclo: la tanda 1 corre sin ventana
   (precisión 3).
2. **Alcance del ciclo.** Para este único ciclo, el alcance se amplía más allá de
   la precisión 1. Entran:
   - todo lo que destapó la tanda 0, prompt de E1 incluido (checklist X2 a X9);
   - la validación en código, con Pydantic, de todas las listas cerradas: tipos
     de nodo, predicados, catálogo de sujetos y valores de propiedades, con una
     política por campo ante un valor fuera de lista;
   - los campos que hacen falta para reprocesar en código lo que no se puede
     mapear: la mención textual del sujeto y las omisiones con categoría y tramo
     literal;
   - el modelo de umbrales;
   - la matriz (X1, X11), el catálogo (la diferencia 6/5 entre el bloque del
     prompt y `esquema_v3_clases.json`, `BKL-0028`, `BKL-0029` y `BKL-0034`) y R6b
     (X10).
3. **Justificación técnica.** Estas correcciones cambian el prefijo o el formato de
   salida de E1 y, por eso, obligan a re-extraer. Hacerlas en un solo ciclo antes de
   escalar evita re-extraer después el corpus escalado (principio 12 del plan). La
   ventana es el único ciclo de corrección con re-extracción que el laudo admite
   antes de B6.3.
4. **Desvío declarado.** Varias de estas correcciones no son una falla de esquema
   que produzca falsedad en campo estructurado, en el sentido de la precisión 1.
   Por ejemplo, la validación en código o la mención del sujeto. Entran porque la
   autora lo decide así para este único ciclo, y queda declarado acá.
5. **Contenido.** El contenido del cambio de esquema lo lauda L-ESQ-R2 (plan,
   B2.11, unidad 5), enmienda fechada al laudo `2593d4d`, después de U-UMBRAL y
   U-LISTAS-NOMAP. Esta enmienda solo declara el uso de la ventana, su alcance y
   sus consecuencias.
6. **Re-extracción.** La de los diez TOs de la tanda 0 con el prefijo nuevo, sobre
   el corpus congelado (U-REEXT-T0, plan, B2.11, unidad 11), antes de sellar el
   pre-registro de B6.3 (precisión 2).

## 3. Consecuencias

1. **La tanda 1 corre sin ventana.** Si revela una falla de esquema, su corrección
   es release posterior declarada (laudo, §7 y línea 202; principio 9 del plan). El
   pre-registro de la tanda 1 lo declara (plan, fila B6.1).
2. **Los cinco documentos de la tanda 0** (`ctacte`, `lingob`, `polcre`, `pagjub`,
   `docvig`) pasan a haber informado el esquema. El conjunto fresco de B6.3 (a) los
   excluye igual que a los 15 (precisión 4). El pre-registro de B6.3 lo declara, y la
   exclusión se registra en `documentos_excluidos_esq.json`, o en el artefacto que
   B6.3 cite al construir su conjunto, con la fecha de esta enmienda una vez
   firmada (plan, fila B6.3).
3. **Vigilancias (1) a (9).** Se miden en la tanda 1 como estaba previsto. Con la
   ventana usada, su lectura ya no abre un ciclo: toda corrección que pidan es
   release posterior.

## 4. Qué no cambia

- El principio de gobierno del §1 del laudo.
- El texto del laudo y el de la enmienda del 25/09, que no se editan.
- El esquema congelado, que sigue vigente hasta que se firme L-ESQ-R2.
- Los grafos evaluados de la tanda 0 (KG-Tanda0-Desarrollo-r1, KG-Tanda0-Diez-r1 y
  el ensamblado de los cinco), que quedan sellados y no se corrigen (principio 9).
  El ciclo produce una versión posterior.

## Firma

PENDIENTE de la autora.
