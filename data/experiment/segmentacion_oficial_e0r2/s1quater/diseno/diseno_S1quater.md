# U-SEG-OFICIAL, S1-quater: diseño de la medición de la E0 corregida (mesa, 11/10/2026)

USD 0, sin API. **Sellado antes de que exista la E0 corregida** (`sello_diseno_S1quater.txt`). No sortea: el sorteo corre sobre la E0
corregida.

## 0. De dónde sale

- **Decisión de la autora del 11/10/2026,** que cambia el plan B de S1-ter. Está registrada en la hoja de ruta de la mesa (§62) y en
  la nota del 11/10/2026 al pie de `docs/mandatos/USEG_OFICIAL_S0-5a_reglas_de_corte_E0.md`. Puntos 3 a 6:
  - los errores confirmados en la adjudicación de S1-ter se corrigen con reglas generales de E0, pase o no pase el piso;
  - la medición de la E0 actual no cambia, y su cifra se informa como la de E0 antes de la corrección;
  - la E0 corregida se mide con S1-quater: 90 unidades nuevas que no estén entre las leídas en S1-ter, con los mismos estratos, el
    mismo piso y la misma regla de las dudosas, a ciegas y con semillas selladas antes de la lectura. Las unidades con error de
    S1-ter se controlan aparte, como regresión, sin entrar en la cifra;
  - si S1-quater no llega al piso, rige el último paso del plan B.
- **Del plan B del 10/10/2026** (nota al pie del mismo mandato, `521e220a`) siguen:
  - los estratos (40 / 10 / 40);
  - la lectura a ciegas desde fuera del repo, solo de cortes;
  - las dos semillas: `U-SEG-OFICIAL:cortes:S1-quater` y `U-SEG-OFICIAL:cortes:S1-quater:revision`.
- **Todo lo demás es de S1-ter** y se cita por su archivo commiteado: las poblaciones, el sorteo, las fichas, el despacho, la
  adjudicación y la cifra.

## 1. Qué se mide

- La E0 corregida, con la lectura de cortes de 90 unidades.
- **El criterio** es el del mandato, tal cual (`docs/mandatos/USEG_OFICIAL_segmentacion_e0r2.md:284-292`).
- **El piso** es el de S1-ter (`USEG_OFICIAL_segmentacion_e0r2.md:315`).
- **Las dudosas:** decide la versión con las dudosas como error, y se informan las dos
  (`s1ter/adjudicacion/nota_piso_dudosas_S1ter.md`, `c86ff651`).
- **No entra en la cifra** la regresión (§6).

## 2. La población

Son las mismas poblaciones que S1-ter, sobre la E0 corregida (`scripts/poblaciones_S1quater.py`):

- **Los tres estratos:** salen del `modo_lectura` del manifiesto de TOs de S1-ter (`s1ter/manifiesto/segmentacion_oficial_e0r2_152.json`,
  sellado en el script). Son `vigente`, `marcadores` y `sin_raiz`, con las unidades de los TOs reconocidos plenos y, en `sin_raiz`,
  las de ri_spi.
- **La regla de construcción de S1-ter** (`s1ter/scripts/poblaciones_finales_S1ter.py`).
  - Salen, declaradas, las unidades de `manual`, `ri_ao`, `optico` y `plandecuentas`, y las de los TOs de vía por página.
  - También las de ri2_pm que cruzan una página de ficha de registro. Se calculan sobre la E0 corregida, con la regla de
    `s1ter/scripts/controles_S1ter.py`.
- **Salen las unidades ya leídas en S1-ter** (§3).
- **La E0 corregida** se controla contra el manifiesto de su corrida. Tiene que tener el formato de `s1ter/manifest_salida.json`
  (`sha256` con una entrada `e0/<archivo>` por archivo) y quedar sellado por su sha256 antes de correr nada.

## 3. Cómo se excluyen las unidades ya leídas, si la corrección cambia ids o cortes

- **Qué es «leída».** Son las unidades de la E0 de S1-ter cuyo texto propio mostró una ficha de S1-ter
  (`comun_S1quater.mostradas_S1ter`):
  - en la etapa 1, la unidad;
  - en la etapa 2, la unidad (o sus partes), sus unidades calificadas y la unidad que le sigue en el documento.
  - Se toman del orden de lectura sellado de S1-ter (`s1ter/tramo_b/orden_lectura_S1ter.json`) y de la E0 que leyó S1-ter
    (`s1ter/e0/`), controlada contra `s1ter/manifest_salida.json`.
- **Por qué no alcanza el id.** La corrección puede partir una unidad, unir dos, correr un corte o cambiar un número. Las unidades no
  guardan su posición en el documento: solo su id, sus páginas y su texto. Por eso la exclusión es por el texto.
- **Cómo se alinean las dos E0, documento por documento** (`comun_S1quater.alinear_to`):
  1. **Anclas:** las unidades con el mismo texto propio (`sha256_propio`) en las dos E0, en el orden del documento.
  2. **Entre dos anclas:** se alinean los tokens del texto propio de las unidades del medio (letras y dígitos, sin tildes, con el corte
     de renglón con guion unido).
- **Qué sale.** Sale toda unidad de la E0 corregida que cumpla una de estas dos condiciones:
  - tiene el mismo id que una unidad leída, aunque su texto haya cambiado;
  - comparte con una unidad leída un ancla o al menos un token alineado.

  Con eso salen las partes de una unidad leída, la unidad que la absorbe, y la vecina a la que se corrió un corte. Una unidad leída
  con otro id sale por su texto. El texto nuevo, que la E0 vieja no tenía, no solapa nada.
- **El freno.** Si en un documento la alineación cubre menos del 95 % de los tokens del texto viejo, el script frena antes de escribir.
  Lo decide la autora.
- **Lo que se declara.** Cada unidad que sale queda en el JSON de las poblaciones, con el motivo (mismo id o solapa con…). También
  queda la cobertura de cada documento.
- **Probado** (`scripts/prueba_S1quater.py`):
  - con la misma E0, salen exactamente las leídas y nada más;
  - con una E0 corregida inventada, salen las dos partes de una unidad leída partida y la vecina con el corte corrido;
  - en esa misma E0, una unidad no leída con otro id se queda.

## 4. Semillas y sorteo (`scripts/sorteo_S1quater.py`)

- **Cada estrato:** `random.Random(f"U-SEG-OFICIAL:cortes:S1-quater:{estrato}").sample(sorted(ids), n)`, con n = 40 / 10 / 40. Es la
  forma de S1-ter (`s1ter/scripts/sorteo_S1ter.py`). La cadena base está sellada en `521e220a`.
- **El orden de lectura de las 90:** `random.Random("U-SEG-OFICIAL:cortes:S1-quater:orden").sample(sorted(ids_90), 90)`, sin agrupar
  por estrato, como S1-ter. **Esta semilla es nueva y la sella este diseño.**
- **Los ids opacos:** `E1-001`… en la etapa 1 y `E2-001`… en la etapa 2, en el orden de lectura. No dicen nada del estrato ni de la
  población. El orden es la lista sellada y no va a la carpeta de la lectora.
- **La semilla `:revision`** queda registrada y, con la adjudicación de S1-ter (§8), sin uso, como su par de S1-ter.
- **Cada salida se sella antes de pasar a la siguiente:** poblaciones, regresión, muestra y orden, carpeta. Cada script exige el sha256
  de lo que lee.
- La prueba sortea solo una población inventada.

## 5. Las fichas y la carpeta de la lectora (`scripts/fichas_S1quater.py`)

- **Formato:** las fichas de S1-ter en su forma final (la de S1-ter-b2), armadas en una sola pasada. Sus constantes de formato son
  copia literal de `s1ter/scripts/fichas_S1ter.py` y `fichas_numero_S1ter.py`, controlada por la prueba.
  - **Etapa 1:** el id opaco, el número que le asignó la segmentación, las páginas con su imagen, el texto heredado y el texto propio.
  - **Etapa 2:** además, la unidad que sigue, con la imagen de cada una de sus páginas.
- **Probado:** con el orden y la E0 de S1-ter, el script reproduce byte a byte las dos carpetas finales de S1-ter (el `manifest.txt`
  de cada etapa da el sha256 de `s1ter/tramo_b2/fichas_numero_registro_S1ter.json`). También reproduce sus planillas vacías.
- **La carpeta:** `fuera_del_repo/lecturas_ciegas/lectura_segmentacion_s1quater/etapa_N/`. Lleva las fichas, las imágenes, el
  `manifest.txt` y la planilla vacía con su manifest (la opción 1 de S1-ter).
- **Antes de despachar:** el control a ciegas y la verificación de la carpeta de S1-ter (`s1ter/scripts/control_ciego_fichas_S1ter.py`
  y `verificar_carpeta_lectora_S1ter.py`), sin cambios.

## 6. La regresión (`scripts/regresion_S1quater.py`)

- **De dónde sale.** De la adjudicación final de S1-ter: las salidas de `s1ter/scripts/aplicar_adjudicacion_S1ter.py`, con sus sha256.
  Tiene un error confirmado:
  - la unidad de una ficha que quedó `error` (en la etapa 2, sus unidades calificadas);
  - la unidad que sigue, si la autora confirmó un error en ella;
  - las unidades calificadas de una ficha con un error confirmado en lo heredado.
- **Cómo se lleva a la E0 corregida.** Cada una se lleva con la misma alineación: son las unidades nuevas que solapan su texto. Si
  alguna no tiene unidad nueva que la solape, queda declarada.
- **Quién la lee.** La lectora, en la etapa 2, en el orden de los ids, con el formato de la etapa 2. El despacho no dice que es una
  regresión, como en S1-ter.
- **Qué se informa.** Por cada error de S1-ter, si la E0 corregida lo resolvió. No entra en la cifra.

## 7. El despacho de la lectora (`despacho/despacho_lectora_S1quater_etapa_1.md` y `_etapa_2.md`)

- **Base:** los despachos v3 de S1-ter, con el mismo criterio, tal cual, y las rutas de S1-quater. Una sesión por etapa, con el paso 0
  de `pwd`, el control de la carpeta, el checkpoint y el sello de la planilla con sha256 y hora.
- **Tres cambios,** por los incidentes de la lectura de S1-ter (`s1ter/lectura/incidentes_lectura_S1ter.md`):
  1. cada ficha se marca con sus imágenes abiertas, y su fila se escribe antes de pasar a la siguiente;
  2. ningún archivo fuera de la carpeta, tampoco en el scratchpad de la sesión: los archivos de trabajo van en la carpeta, con el
     prefijo `trabajo_`;
  3. la salida de los pasos 0 y 1 va pegada tal cual en el FRENO.
- **El modelo:** el mismo de S1-ter. Lo elige la autora al abrir la sesión, y la lectora lo informa en su FRENO.

## 8. La adjudicación y la cifra

- **Método:** el de S1-ter (`s1ter/adjudicacion/LEEME_adjudicacion_S1ter.md` y `metodo_adjudicacion_S1ter.md`).
  - Una pasada 1 de la autora sobre las 90 fichas, sin ver nada de la lectora y sellada.
  - Una pasada 2 sobre las fichas que cumplen la regla a–d.
  - El acuerdo con la lectora, calculado después.
- **Scripts:** los de S1-ter, con las rutas, las semillas y el orden de S1-quater. No dependen de la E0, así que se sellan antes de que
  la autora abra la pasada 1.
- **La cifra:** la calcula `s1ter/scripts/cifras_lectura_S1ter.py` sobre las planillas adjudicadas.

## 9. Lo que falta, en orden

1. La E0 corregida, con las reglas que decida la autora después de la pasada 2. Su corrida deja el manifiesto del §2, sellado.
2. La adjudicación final de S1-ter, sellada, con las salidas de `aplicar_adjudicacion_S1ter.py` (para el §6).
3. Sobre una copia, en este orden y sellando cada salida:
   1. las poblaciones;
   2. la regresión;
   3. el sorteo y el orden;
   4. las fichas;
   5. los controles a ciegas.
4. La carpeta de la lectora y el despacho de la etapa 1. Al sellarse la etapa 1, el de la etapa 2.
5. La adjudicación y la cifra (§8). Si no llega al piso, el último paso del plan B.

## 10. Qué queda sellado con este diseño

Este documento, los seis scripts de `scripts/`, los dos despachos de `despacho/` y la salida de la prueba
(`salida_prueba_S1quater.txt`). El sha256 de cada uno y la hora están en `sello_diseno_S1quater.txt`. Un cambio después del sello es
una versión nueva, sellada antes de que exista la E0 corregida.
