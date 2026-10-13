# U-SEG-OFICIAL, S1-quater: adenda 3 al diseño, las unidades vistas al diseñar y revisar S0-6a fuera de la población (mesa, 12/10/2026)

USD 0, sin API. **Sellada antes del sorteo** (`sello_adenda_3_diseno_S1quater.txt`).
- **No se editan:** el diseño sellado (`diseno_S1quater.md`, en `3a52987f`), la adenda 1 (en `bf84214d`) y la adenda 2 (en `d093d0ec`).
  Esta adenda los cambia en lo que sigue.
- **Reemplaza a una versión anterior** de esta misma adenda, sellada a las 18:24:07 y nunca commiteada. Queda en el paquete de la mesa,
  en `reemplazados/`. Esta versión suma dos grupos (decisiones 1 y 2 de la autora, §80).
- **El §10 del diseño y esta adenda.** El §10 pide que un cambio después del sello sea una versión nueva, «sellada antes de que exista
  la E0 corregida». La E0 corregida de S0-6a ya existe.
  - **Por decisión de la autora del 12/10/2026,** la contradicción se acepta y se declara: esta adenda no usa la E0 corregida.
  - **De dónde sale la lista:** del registro de la sesión de la ejecutora de S0-6a, del selftest de su parche, del código de E0, del
    registro de la sesión de la mesa y de la E0 de S1-ter.
  - **Cómo se prueba:** sobre la E0 de S1-ter, como las adendas 1 y 2.

## 0. De dónde sale

- **Decisiones de la autora del 12/10/2026** (hoja de ruta de la mesa):
  - §79, decisión 7: «S1-quater: salen de la población las 4 unidades de diseño, las 9 que mostró la misma salida y las 11 vecinas del
    selftest. Va en una adenda 3 al diseño, sellada antes del sorteo, sin ids a la vista para mí.»
  - §80, decisión 1: «Las 3 listas de las 13 cuyas unidades no son de las 40 filas ni de las 286 leídas salen de S1-quater ya, en la
    adenda 3.»
  - §80, decisión 2: «Si en la revisión del §78 miraste el texto o la página de alguna otra unidad que no sea de las 40 filas ni de
    las 286, también entra en la adenda 3 y se declara en ella.»
- **Las 4 unidades de diseño** ya salen por la adenda 2.
- **La lista tiene 282 unidades de la E0 de S1-ter, en cuatro grupos sin repetir:**
  - **9 que mostró la salida de las guardas:**
    - son las unidades no leídas en S1-ter que la ejecutora de S0-6a vio en la salida de las 11:18:10 (hora local) de su sesión,
      la que miró antes de agregar las dos guardas de A, sin que motivaran las guardas;
    - son 4 de ri_oc, 3 de ri_spi y 2 de ceninf.
  - **5 vecinas del selftest:**
    - los 11 ids de documentos reales que agrega el selftest del parche de S0-6a (el `selftest_e0.py` que da
      `s0_6/parche/parche_e0_S0-6a.diff`, `a7b7ea50…`, aplicado al código de S0-5b: `83ae5576…`) y que no son filas ni leídas,
      llevados a la E0 de S1-ter: por su id si existe ahí; las claves nuevas, por el texto que controla el selftest;
    - entran 5 unidades no leídas: 1 de seguef, 1 de snp_cheq, 1 de gerc y 2 de ri_ccna;
    - los otros 6 ids son claves nuevas, o la clave nueva de una unidad leída, cuyo texto está en unidades leídas en S1-ter. Ya salen
      por el §3 del diseño, y la prueba lo controla.
  - **6 de las 3 listas de R5-a de unidades no leídas:**
    - son las 3 listas de `LISTAS_R5A_S0_5` (`correr_e0.py`) que S0-6a-bis compara con la página: 1 de adfsp y 2 de ri_oc;
    - por lista, el último ítem y el cierre de su lista, que es la unidad que le sigue en la E0 de S1-ter.
  - **262 que la mesa vio al revisar S0-6a:**
    - son unidades no leídas cuyo texto quedó a la vista de la mesa en sus rondas del §78 al §80. Las del §79 y el §80 entran por
      la misma regla de la autora: la unidad cuyo texto alguien lee sale de S1-quater y se declara;
    - **el criterio, mecánico:** un tramo distintivo de su texto propio aparece en lo que la sesión de la mesa imprimió o escribió en
      esas rondas. Un tramo distintivo son 6 tokens seguidos, que están en a lo sumo 2 unidades de la E0 de S1-ter; una unidad corta
      cuenta si su texto entero aparece seguido;
    - **es conservador:** si dos unidades comparten un tramo, las dos cuentan;
    - **las páginas y el texto que la mesa miró:** páginas de doce documentos para medir sangrías, la herencia corregida de las
      unidades leídas que cambian, listados de unidades y tramos del registro de la ejecutora;
    - **por documento:** adfsp 12, afiltr 1, apnf 7, autenf 1, ayccef 5, cajasc 2, ccbcra 1, cedin 1, ceninf 3, cirmo3 5, cryl 3,
      ctacte 2, ctavis 3, depaho 13, disres 1, dmrd 1, efemin 5, expaef 12, fabcra 1, finsec 2, garant 1, gerc 9, gescre 3, graloc 1,
      icmecma 2, lingeef 6, manori 7, manual 4, nmaeef 8, nmcief 2, opecam 3, pfmipyme 1, prevmi 1, pscpp 1, raapal 1, ratiofn 3,
      retype 1, ri2_ae 6, ri2_ci 2, ri2_cs 1, ri2_pm 4, ri_ccna 6, ri_dcpc 13, ri_ii_31_12_19 7, ri_laft 1, ri_nge 2, ri_niif 1,
      ri_oc 28, ri_pnp 1, ri_pspapt 3, ri_psprca 10, ri_rml 6, ri_secoexpo 1, ri_spi 3, ri_tar 1, ri_tvf 1, rmgcti 2, rrci 1,
      seguef 2, servco 2, snp_cheq 5, snp_dd 6, snp_debin 1, snp_psp 1, snp_spd 5, snp_tr 3, traval 2 (67 documentos).
- **Sus ids no van al repo.** Los trae una lista fuera del repo, en el paquete de la mesa:
  `~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/d0348a29-aaa4-4292-82f3-0c0149e3787e/scratchpad/hoja_de_ruta_tanda1_mesa/preparacion_S0-6a-bis_mesa/adenda_3_S1quater/NO_ABRIR_unidades_adenda_3_S1quater.json`
  (sha256 `7337f854c58f0d5fb962e18c843ed2350640221e63de1d7ac46eaab11429c500`).
  - La lista trae también, por grupo, de dónde sale cada unidad, y en el último grupo, el sha256 del script de medición y de la copia
    del registro, y las franjas.
  - El script de la versión 4 controla su sha256 antes de leerla.

## 1. Lo que cambia

- **§2 y §9, paso 3.1, del diseño: las poblaciones salen de `scripts/poblaciones_S1quater_v4.py`,** no de la versión 3.
  - **La única diferencia:** salen también las unidades de la lista, declaradas con su grupo y su motivo.
  - **Cómo salen:** como las leídas en S1-ter y las de diseño (§3 del diseño), por el mismo id o porque solapan su texto propio, con
    la misma alineación.
  - **Una unidad que sale por construcción, por leída o por la adenda 2** sale por eso, aunque también esté en la lista.
  - Los pesos se recalculan sobre las unidades que quedan.
  - La versión 3 queda como está, sellada, y no se usa.
- **No cambia nada más del diseño:** ni las semillas, ni los tamaños de los estratos, ni las fichas, ni los despachos, ni la regresión,
  ni la adjudicación.
- **Lo que esta adenda no cubre:**
  - **las unidades de diseño que declare S0-6a-bis fuera de las 3 listas:** van a una adenda 4, sellada antes del sorteo. Si no
    declara ninguna, no hay adenda 4, y se deja escrito (§80, decisión 3);
  - **las rondas de la mesa anteriores al §78 y las otras sesiones de la mesa:** no se midieron para esta adenda.

## 2. La prueba

- **El script:** `scripts/prueba_adenda_3_S1quater.py`.
  - Corre las versiones 3 y 4 sobre los mismos datos reales: la E0 de S1-ter en lugar de la corregida, controlada contra
    `s1ter/manifest_salida.json`.
  - Con la misma E0, cada unidad de la lista solapa solo consigo misma. Por eso la versión 4 tiene que dar lo mismo que la 3, menos
    exactamente las unidades de la lista que están en la población.
  - Controla también la cuenta por grupo, y que los 6 ids del selftest que no entran a la lista tengan su texto en unidades leídas en
    S1-ter.
- **El resultado:** 11 de 11 controles ok (`salida_prueba_adenda_3_S1quater.txt`). Dos corridas dan la misma salida.
  - Con la E0 de S1-ter, 272 de las 282 están en la población. De las otras 10, 8 son de documentos que no están en los estratos y 2
    son de la tanda 0, que sale por construcción (adenda 1).
- **La prueba en contra:**
  - **qué corre:** una versión 4 que no saca las unidades de la lista;
  - **qué tiene que dar:** MAL en los dos controles que miden la salida de la lista, y ok en los otros nueve;
  - **qué da:** eso, 9 de 11. Está en el paquete de la mesa.

## 3. Qué queda sellado con esta adenda

- Quedan sellados cuatro archivos:
  - este documento;
  - `scripts/poblaciones_S1quater_v4.py`;
  - `scripts/prueba_adenda_3_S1quater.py`;
  - `salida_prueba_adenda_3_S1quater.txt`.
- El sha256 de cada uno y la hora están en `sello_adenda_3_diseno_S1quater.txt`. La lista fuera del repo queda sellada por su sha256,
  en esta adenda y en el script de la versión 4.
