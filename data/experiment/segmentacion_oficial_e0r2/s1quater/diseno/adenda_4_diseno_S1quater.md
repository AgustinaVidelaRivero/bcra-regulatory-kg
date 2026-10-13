# U-SEG-OFICIAL, S1-quater: adenda 4 al diseño, las unidades vistas fuera de la población y la cobertura (mesa, 12-13/10/2026)

USD 0, sin API. **Sellada antes del sorteo** (`sello_adenda_4_diseno_S1quater.txt`).
- **No se editan:** el diseño sellado (`diseno_S1quater.md`, en `3a52987f`) ni las adendas 1 (en `bf84214d`), 2 (en `d093d0ec`) y 3
  (en `55d86819`). Esta adenda los cambia en lo que sigue.
- **Reemplaza al borrador** que la mesa preparó en su revisión del FRENO de S0-6a-bis, nunca sellado ni commiteado. Queda en el paquete
  de la mesa (`revision_FRENO_S0-6a-bis_mesa/adenda_4_S1quater/`).
- **El §10 del diseño y esta adenda.** Como en la adenda 3, la contradicción con el §10 («sellada antes de que exista la E0 corregida»)
  se acepta y se declara.
  - **De dónde sale la lista:** de los registros de las sesiones de la mesa y de la ejecutora, de los archivos del registro de S0-6a y
    S0-6a-bis, de la memoria de la mesa y de la E0 de S1-ter. No sale de la E0 corregida.
  - **La E0 corregida se usa solo para contar:** para la parte B de la prueba (la cobertura, decisión 8 de la autora) y para la población
    por estrato que pidió la autora (§82, punto 12), sin leer texto.

## 0. De dónde sale

- **Decisiones de la autora del 12/10/2026** (hoja de ruta de la mesa):
  - §81, decisión 10: «Las 108 unidades que viste en rondas anteriores al §78 de tu sesión salen de S1-quater en una adenda 4.»
  - §81, decisión 12: «Si en el §78 miraste alguna página como imagen, todas las unidades de esa página cuentan como vistas y van a la
    adenda 4.» No pasó.
  - §81, decisión 13: «A la adenda 4 va también toda unidad que la ejecutora declaró como de diseño (las de las 3 listas) y no esté en
    la adenda 3. […]» No hay ninguna.
  - §82, decisión 3: «Regla única para S1-quater: sale toda unidad que no sea fila ni leída en S1-ter cuyo texto haya visto la mesa o una
    ejecutora antes del sorteo, medida por script. Lo que no se puede medir (otras sesiones de la mesa) queda como límite declarado. Por
    esta regla salen en la adenda 4 las 89 unidades que la ejecutora vio antes del censo y las 41 que vio después.»
  - §82, decisión 8: «La cobertura: opciones 1 y 2 juntas, en el script v5 de la adenda 4.»
  - §82, decisión 9: «El §13 ter: opción 1. Las 97 unidades que muestran los archivos del registro salen en la adenda 4. […]»
  - §82, decisión 10: «La memoria: opción (c). Las 32 salen en la adenda 4, y limpiás esos archivos con un script que reemplace los ids
    y los tramos de unidades que no son de diseño por cuentas por documento, con respaldo antes. Se declara en la adenda 4 y en la hoja.»
- **La medición es la de la adenda 3.** Una unidad quedó a la vista si un tramo distintivo de su texto propio aparece en lo que una
  sesión imprimió o escribió (entradas y salidas de sus herramientas), o en un archivo. Un tramo distintivo son 6 tokens seguidos que
  están en a lo sumo 2 unidades de la E0 de S1-ter; una unidad corta cuenta si su texto entero aparece seguido. Es conservadora: si dos
  unidades comparten un tramo, las dos cuentan.
- **La lista tiene 801 unidades de la E0 de S1-ter, en 113 documentos,** en estos grupos. Una unidad queda en el primer grupo que la
  trae; los de la autora van primero. De cada grupo salen las filas, las leídas en S1-ter y las de las adendas 2 y 3.

  | grupo | de dónde sale | unidades medidas | sin repetir | documentos |
  |---|---|---|---|---|
  | vistas_por_la_mesa_antes_del_78 | la sesión de la mesa, desde su primer registro (10/10/2026, 14:29) hasta el pedido del §78 | 135 | 108 | 54 |
  | vistas_por_la_mesa_81 | la sesión de la mesa en el §81 (22:13:34 a 23:12:29 del 12/10) | 5 | 5 | 5 |
  | vistas_por_la_ejecutora_S0-6a-bis_antes_del_censo | la sesión de la ejecutora, del «seguí» (19:05:13) al censo (19:41:21) | 89 | 87 | 24 |
  | vistas_por_la_ejecutora_S0-6a-bis_despues_del_censo | la misma sesión, del censo al final | 41 | 29 | 9 |
  | mostradas_por_archivos_del_registro | los archivos abiertos (no `NO_ABRIR_`) del registro de S0-6a (commit 47) y de S0-6a-bis (commit 49) | 97 | 93 | 43 |
  | en_la_memoria_de_la_mesa | ids y tramos en la memoria de la mesa, escritos por sesiones anteriores | 32 | 29 | 21 |
  | vistas_por_la_ejecutora_S0-6a | la misma sesión de la ejecutora, antes del «seguí» de S0-6a-bis (la parte de S0-6a) | 610 | 450 | 80 |
  | vistas_por_la_mesa_82 | la sesión de la mesa en el §82, de las 23:37:55 a las 23:50:44 del 12/10 | 0 | 0 | 0 |
  | declaradas_de_diseno_por_la_ejecutora | §81, decisión 13 | — | 0 | 0 |
  | vistas_como_imagen_en_el_78 | §81, decisión 12 | — | 0 | 0 |

  - **«Unidades medidas»** son las que da la medición sin las filas, las leídas ni las de las adendas 2 y 3. En el primer grupo, 135
    menos las 27 que ya salen por la adenda 3 dan las 108 de la decisión 10.
  - **El grupo de la parte de S0-6a no lo nombró la autora.** Es la misma sesión de la ejecutora, antes del «seguí» de S0-6a-bis, y nadie
    la había medido: de esa parte, las adendas 2 y 3 sacaron solo las unidades de diseño de las guardas de A, las 9 que mostró la salida
    que miró para ellas y las 5 vecinas del selftest. La mesa lo suma al aplicar la regla de la decisión 3 tal como está escrita.
  - **43 de las 801 son de documentos que salen enteros por construcción** (la tanda 0, manual, ri_ao y plandecuentas). La lista las
    trae igual.
  - **Por documento:** actgar 1, adfsp 10, adrei 3, afiltr 9, apnf 3, autenf 1, ayccef 5, cajasc 18, cateloc 1, ccbcra 3, cedin 7,
    ceninf 13, cirmo3 3, cryl 4, ctacte 14, ctavis 4, depaho 13, depinv 4, disres 2, dmrd 4, docvig 3, efemin 36, expaef 16,
    fimipyme 3, finsec 2, garant 4, gerc 23, gescre 4, gracre 7, icmecma 3, incuca 1, inspag 2, lavdin 1, lingeef 20, lingob 5,
    manori 18, manual 15, nmaeef 23, nmcief 8, opecam 2, opefci 1, pfmipyme 2, plandecuentas 1, pognme 1, polcre 4, prevmi 2, pscpp 2,
    raapal 2, ratio 3, ratiofn 1, rdbcra 5, regpri 1, relact 3, repefe 2, reqcac 1, ri2_ae 10, ri2_ci 7, ri2_pm 10, ri_acsf 1, ri_ai 1,
    ri_ao 1, ri_bdp 1, ri_cc 8, ri_ccna 85, ri_ccpnp 1, ri_dcpc 57, ri_dsf 6, ri_gerc 1, ri_icpipsp 2, ri_iepsp 2, ri_iesinap 2,
    ri_ii_31_12_19 9, ri_itme 1, ri_laft 1, ri_mmsef 1, ri_msrl 4, ri_nge 2, ri_niif 4, ri_oc 93, ri_ot 2, ri_pgn 2, ri_pnp 1, ri_psp 2,
    ri_pspapt 3, ri_rml 11, ri_saofe 5, ri_secoexpo 2, ri_sef 1, ri_spi 9, ri_tar 2, ri_tii 1, ri_tsa 1, ribspc 3, rmgcti 3, rrci 2,
    secfin 1, seggar 12, seguef 13, servco 1, snp_atm 1, snp_cec 2, snp_cheq 15, snp_dd 11, snp_debin 3, snp_mep 2, snp_psp 6,
    snp_spd 5, snp_tr 6, snp_tr_nc 3, socgar 1, supcon 2, tasint 5, venliq 3.
- **La memoria de la mesa** (decisión 10), declarada:
  - antes de limpiarla, la mesa la respaldó entera, fuera del repo
    (`~/INGENIERIA IA/TESIS/fuera_del_repo/respaldo_memoria/NO_ABRIR_memoria_antes_de_limpiar_20261012_234344/`; trae texto de unidades
    y no se abre);
  - un script (en el paquete de la mesa) reemplazó, en 20 archivos, 20 apariciones de ids y 18 tramos de texto de las 32 unidades por
    «una unidad de <documento>» y «texto retirado de una unidad de <documento>». Al pie de cada archivo dejó las cuentas por documento;
  - después, la memoria no tiene ningún id ni tramo de esas 32. Quedan ids de filas, de leídas, de la tanda 0, de las adendas 2 y 3 y
    otros que no existen en la E0 de S1-ter, que no son de la población;
  - tres tramos de otras clases (dos de las adendas, uno de una fila) se fueron con los reemplazos, porque compartían el tramo con una
    de las 32.
- **Sus ids no van al repo.** Los trae una lista fuera del repo, en el paquete de la mesa:
  `~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/d0348a29-aaa4-4292-82f3-0c0149e3787e/scratchpad/hoja_de_ruta_tanda1_mesa/decisiones_S0-6a-bis_y_adenda_4_mesa/adenda_4_S1quater/NO_ABRIR_unidades_adenda_4_S1quater.json`
  (sha256 `7409d83dc7397d14927b46b955007ec717fe9cd13541d79f0922e45af41684a0`). Trae, por grupo, el origen y las franjas de cada
  medición. El script de la versión 5 controla su sha256 antes de leerla.

## 1. Lo que cambia

- **§2 y §9, paso 3.1, del diseño: las poblaciones salen de `scripts/poblaciones_S1quater_v5.py`,** no de la versión 4, que queda como
  está, sellada, y no se usa. Hay dos diferencias.
- **Salen también las unidades de la lista,** declaradas con su grupo y su motivo:
  - como las leídas en S1-ter y las de las adendas 2 y 3 (§3 del diseño), por el mismo id o porque solapan su texto propio, con la
    misma alineación;
  - una unidad que sale por construcción, por leída o por las adendas 2 o 3 sale por eso, aunque también esté en la lista;
  - los pesos se recalculan sobre las unidades que quedan.
- **La cobertura** (decisión 8: las opciones 1 y 2 de la revisión de la mesa del FRENO de S0-6a-bis, §13 bis):
  - un documento cuya alineación cubre menos del 95 % del texto viejo ya no frena;
  - **si no tiene nada que sacar** (ninguna leída ni unidad de las adendas 2 a 4), queda en la población como está (opción 1);
  - **si tiene algo que sacar,** además de la alineación sale toda unidad nueva que comparte con una de ellas un tramo distintivo de 6
    tokens, sin orden (opción 2). Es el mismo criterio de la medición (§0). Cada una sale declarada aparte (`solapa_sin_orden`), y el
    documento queda en la población;
  - en los demás documentos la exclusión es la de la versión 4;
  - **lo que la mesa generalizó:** la opción 2 se propuso para ri2_ae y ri_spi, que eran los únicos bajo el umbral con algo que sacar.
    Con esta lista, ri_sef y ri_ccpnp también tienen algo que sacar, y la versión 5 les aplica la opción 2. Leída al pie de la letra, la
    opción 1 los dejaría frenando.
- **Lo que S1-quater mide** (decisiones 5 y 6 de la autora del §82): la E0 corregida tal como está, con las cadenas de 10 o más títulos
  heredados de 7 documentos y con las divisiones que A abre en las tablas de códigos de ri_ii_31_12_19. Las dos quedan como límite
  declarado para la tanda 1; la corrección de las cadenas entra al grupo 2 (backlog).
- **No cambia nada más del diseño:** ni las semillas, ni los tamaños de los estratos, ni las fichas, ni los despachos, ni la regresión,
  ni la adjudicación.
- **Lo que esta adenda no cubre:**
  - **las otras sesiones de la mesa:** límite declarado (§81, decisión 11; §82, decisión 3);
  - **las sesiones anteriores a la corrección de E0** (las ejecutoras de S0-1 a S0-5b, y las corridas y lecturas de S1 a S1-ter): no se
    midieron. La regla se aplicó a las sesiones que diseñaron o revisaron la corrección que mide S1-quater. Si la autora decide medirlas,
    van en una adenda 5;
  - **lo que vea la mesa desde las 23:50:44 del 12/10 y lo que vea la ejecutora de S0-6b:** se mide con el mismo criterio y, si hay
    alguna unidad, sale en una adenda 5, sellada antes del sorteo.

## 2. La prueba

- **El script:** `scripts/prueba_adenda_4_S1quater.py`, en dos partes.
  - **A, sobre la E0 de S1-ter** (controlada contra `s1ter/manifest_salida.json`), como las pruebas de las adendas 1 a 3: corre las
    versiones 4 y 5 sobre los mismos datos. Con la misma E0, cada unidad de la lista solapa solo consigo misma y ningún documento queda
    bajo el umbral, así que la versión 5 tiene que dar lo mismo que la 4, menos exactamente las unidades de la lista que están en la
    población. Controla también la cuenta por grupo (`N_GRUPOS`).
  - **B, sobre la E0 corregida de S0-6a-bis,** controlada contra su manifiesto (`s0_6/bis/manifiestos/manifest_salida_e0_152_S0-6a-bis.json`,
    commit 49, `991ac178…`). La E0 está fuera del repo: corrió sobre la reproducción de la mesa, igual archivo por archivo al manifiesto.
    Controla que la versión 4 frene por cobertura en los documentos que la versión 5 declara bajo el umbral, que la versión 5 no frene y
    le dé a cada uno su tratamiento, y recalcula por su cuenta qué tiene que salir por la exclusión sin orden y por la alineación.
- **Lo que tiene que dar, fijado antes de correrla:** 15 de 15 controles ok, con la misma salida en dos corridas.
- **Lo que da:** eso (`salida_prueba_adenda_4_S1quater.txt`).
- **Las pruebas en contra** (en el paquete de la mesa):
  - **sin la lista:** una versión 5 que no saca las unidades de la lista. Tiene que dar MAL en los cuatro controles que miden qué sale (dos
    de la parte A y dos de la B) y ok en los otros once. Da eso: 11 de 15;
  - **sin la exclusión sin orden:** una versión 5 que no la aplica. Tiene que dar MAL en los dos controles de la parte B que la miden y ok
    en los otros trece. Da eso: 13 de 15.

## 3. La población sobre la E0 corregida (§82, punto 12; solo cuentas)

Con la versión 5 y esta lista sobre la E0 de S0-6a-bis:

| estrato | tamaño | documentos | unidades que quedan | peso | salen por esta adenda | quedarían sin esta adenda |
|---|---|---|---|---|---|---|
| vigente | 40 | 91 | 6.746 | 0,8728 | 460 | 7.206 |
| marcadores | 10 | 5 | 86 | 0,0111 | 82 | 168 |
| sin_raiz | 40 | 43 | 897 | 0,1161 | 436 | 1.333 |
| total | 90 | 139 | 7.729 | 1 | 978 | 8.707 |

- **Las 978 que salen por esta adenda** son unidades de la E0 corregida: una unidad de la lista puede solapar varias. De ellas, 521 salen
  solo por el grupo de la parte de S0-6a (191, 61 y 269 por estrato).
- **Ningún documento frena por cobertura.** Los cuatro bajo el umbral tienen algo que sacar y van por la opción 2:

  | documento | cobertura | salen solo por la exclusión sin orden |
  |---|---|---|
  | ri2_ae | 0,660 | 27 |
  | ri_spi | 0,700 | 8 |
  | ri_sef | 0,816 | 2 |
  | ri_ccpnp | 0,897 | 0 |

  - **Las 37** son las que, sin la opción 2, quedarían en la población.
  - **En las listas de salida,** 48 unidades tienen como única razón la exclusión sin orden: 40 por leídas en S1-ter, 3 por la
    adenda 3 y 5 por esta adenda. 11 de ellas salen igual, por la alineación, en otra lista.

## 4. Qué queda sellado con esta adenda

- Quedan sellados cuatro archivos:
  - este documento;
  - `scripts/poblaciones_S1quater_v5.py`;
  - `scripts/prueba_adenda_4_S1quater.py`;
  - `salida_prueba_adenda_4_S1quater.txt`.
- El sha256 de cada uno y la hora están en `sello_adenda_4_diseno_S1quater.txt`. La lista fuera del repo queda sellada por su sha256,
  en esta adenda y en el script de la versión 5.
