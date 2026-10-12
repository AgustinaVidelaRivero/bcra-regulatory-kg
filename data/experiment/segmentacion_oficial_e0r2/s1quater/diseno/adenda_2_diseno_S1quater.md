# U-SEG-OFICIAL, S1-quater: adenda 2 al diseño, las unidades de diseño de S0-6a fuera de la población (mesa, 12/10/2026)

USD 0, sin API. **Sellada antes del sorteo** (`sello_adenda_2_diseno_S1quater.txt`).
- El diseño sellado (`diseno_S1quater.md`, en `3a52987f`) y la adenda 1 (en `bf84214d`) no se editan: esta adenda los cambia en lo que
  sigue.
- **El §10 del diseño y esta adenda.** El §10 pide que un cambio después del sello sea una versión nueva, «sellada antes de que exista
  la E0 corregida». La E0 corregida de S0-6a ya existe: está en el paquete de la ejecutora, fuera del repo, y la oficial la corre S0-6b.
  - **Lo que pide el mandato:** «con una adenda sellada antes del sorteo» (`docs/mandatos/USEG_OFICIAL_S0-6a_correccion_E0.md`, §2,
    sha256 `5edfd993…`).
  - **Para no apoyarse en la E0 corregida,** esta adenda no la usa: su lista sale del registro de la sesión de la ejecutora y de la E0
    de S1-ter, y su prueba corre sobre la E0 de S1-ter, como la de la adenda 1.
  - La mesa lo declara: que esto cumpla el §10 lo decide la autora.

## 0. De dónde sale

- **Decisión de la autora del 12/10/2026** (hoja de ruta de la mesa, §78, decisión 2): «La ejecutora agregó dos guardas a la regla A
  mirando unidades no leídas, y después las revirtió. Esas unidades cuentan como de diseño (regla de la §2 del mandato) y salen de la
  población de S1-quater, con una adenda al diseño sellada antes del sorteo.»
- **Lo que hizo la ejecutora:**
  - `data/experiment/segmentacion_oficial_e0r2/s0_6/DISENO_S0-6a.md`, §6 (sha256 `39512e7d…`);
  - el registro de su sesión (sha256 `9bedbe0a…`): agregó las dos guardas a las 11:19:07 y las revirtió a las 11:19:49 (hora local).
    Antes había mirado dos salidas, la de las 11:18:10 y la de las 11:19:17.
- **Cuáles son las unidades de diseño:** las de la E0 de S1-ter cuyo texto mostraron esas dos salidas y motivaron las guardas. Son 4,
  todas de ri_oc, regla A:
  - el preámbulo, que en la E0 de S1-ter es una sola unidad;
  - tres unidades del Anexo II: su título, la sección de los códigos de servicios y la última sección, que lleva la tabla de la p. 28.
- **Sus ids no van al repo.** Los trae una lista fuera del repo, en el paquete de la mesa:
  `~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/d0348a29-aaa4-4292-82f3-0c0149e3787e/scratchpad/hoja_de_ruta_tanda1_mesa/revision_FRENO_S0-6a_mesa/adenda_2_S1quater/NO_ABRIR_unidades_diseno_guardas_A_S0-6a.json`
  (sha256 `1703861cbbc7abd9b913797fed2a6a73485adc5d4d3aace3cc11aed555abae71`). El script de la versión 3 controla ese sha256 antes de
  leerla.
- **Lo que no entra:** esas dos salidas mostraron también 9 unidades no leídas que no motivaron las guardas (4 de ri_oc, 3 de ri_spi y
  2 de ceninf). No salen de la población. Están identificadas en el paquete de la mesa, y la autora decide si las quiere fuera.

## 1. Lo que cambia

- **§2 y §9, paso 3.1, del diseño: las poblaciones salen de `scripts/poblaciones_S1quater_v3.py`,** no de la versión 2.
  - **La única diferencia:** salen también, declaradas con su motivo, las unidades de diseño de S0-6a. Salen como las leídas en S1-ter
    (§3 del diseño): por el mismo id o porque solapan su texto propio, con la misma alineación.
  - Los pesos se recalculan sobre las unidades que quedan.
  - La versión 2 queda como está, sellada, y no se usa.
- **§3, la exclusión de las unidades leídas en S1-ter:** no cambia. Una unidad que sale por leída sale por eso, aunque también sea de
  diseño.
- **No cambia nada más del diseño:** ni las semillas, ni los tamaños de los estratos, ni las fichas, ni los despachos, ni la regresión,
  ni la adjudicación.

## 2. La prueba

- **El script:** `scripts/prueba_adenda_2_S1quater.py`.
  - Corre las versiones 2 y 3 sobre los mismos datos reales: la E0 de S1-ter en lugar de la corregida, controlada contra
    `s1ter/manifest_salida.json`.
  - Con la misma E0, cada unidad de diseño solapa solo consigo misma. Por eso la versión 3 tiene que dar lo mismo que la 2, menos
    exactamente las unidades de la lista.
- **El resultado:** 9 de 9 controles ok (`salida_prueba_adenda_2_S1quater.txt`). Dos corridas dan la misma salida.
- **La prueba en contra:** una versión 3 que no saca las unidades de diseño da MAL en dos controles. Está en el paquete de la mesa.

## 3. Qué queda sellado con esta adenda

- Quedan sellados cuatro archivos:
  - este documento;
  - `scripts/poblaciones_S1quater_v3.py`;
  - `scripts/prueba_adenda_2_S1quater.py`;
  - `salida_prueba_adenda_2_S1quater.txt`.
- El sha256 de cada uno y la hora están en `sello_adenda_2_diseno_S1quater.txt`. La lista fuera del repo queda sellada por su sha256,
  en esta adenda y en el script de la versión 3.
