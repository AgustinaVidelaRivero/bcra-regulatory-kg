# U-SEG-OFICIAL, S1-quater: adenda 1 al diseño, la tanda 0 fuera de la población (mesa, 12/10/2026)

USD 0, sin API. **Sellada antes de que exista la E0 corregida y antes del sorteo** (`sello_adenda_1_diseno_S1quater.txt`).
- El diseño sellado (`diseno_S1quater.md`, con su sello `sello_diseno_S1quater.txt`, en `3a52987f`) no se edita: esta adenda lo cambia
  en lo que sigue.
- El §10 del diseño lo permite: un cambio después del sello es una versión nueva, sellada antes de que exista la E0 corregida.

## 0. De dónde sale

- **Decisión de la autora del 12/10/2026.** Está en la adenda 2 a su nota de decisiones de la corrección de E0, §2, puntos 1, 3 y 5:
  `~/INGENIERIA IA/TESIS/fuera_del_repo/correccion_E0/decisiones_correccion_E0_adenda_2.md`
  (`1a25529306e6118bfa9696e1b6e7512e7190356c038f977f57c64770a119d9f1`). Dice tres cosas:
  - en S0-6a la tanda 0 sigue excluida de la corrección de E0, como fija el mandato firmado de U-SEG-OFICIAL;
  - S1-quater mide la E0 corregida, y los cinco documentos de la tanda 0 que están entre los 152 no la tienen. Por eso no entran en
    su población;
  - en la regresión, las filas de documentos de la tanda 0 se esperan «sigue con error: la tanda 0 queda fuera de S0-6a».
- **La población del diseño los incluye por construcción:** la regla de S1-ter no los saca.
  - Lo controló la mesa con `poblaciones_S1quater.py`, poniendo la E0 de S1-ter en lugar de la corregida: el estrato `vigente` trae
    unidades de esos cinco documentos, y los otros dos estratos no.
  - El comando y su salida están en el paquete de la mesa.

## 1. Lo que cambia

- **§2 y §9, paso 3.1, del diseño: las poblaciones salen de `scripts/poblaciones_S1quater_v2.py`,** no de la versión 1.
  - **La única diferencia** es que salen por construcción, declaradas con su motivo, las unidades de ctacte, lingob, polcre, pagjub y
    docvig.
  - Los pesos se recalculan sobre las unidades que quedan.
  - La versión 1 queda como está, sellada, y no se usa.
- **§3, la exclusión de las unidades leídas en S1-ter:** no cambia. Las de esos cinco documentos que leyó S1-ter salen ahora por
  construcción, que se evalúa antes.
- **§6, la regresión:** no cambia su armado.
  - Las filas de los errores confirmados de S1-ter que son de documentos de la tanda 0 se leen igual.
  - Se esperan «sigue con error: la tanda 0 queda fuera de S0-6a».
- **No cambia nada más del diseño:** ni las semillas, ni los tamaños de los estratos, ni las fichas, ni los despachos, ni la
  adjudicación.

## 2. La prueba

- **El script:** `scripts/prueba_adenda_1_S1quater.py`.
  - Corre las dos versiones sobre los mismos datos reales: la E0 de S1-ter en lugar de la corregida, controlada contra
    `s1ter/manifest_salida.json`.
  - Controla que la versión 2 dé lo mismo que la 1, salvo las unidades de esos cinco documentos.
- **El resultado:** 9 de 9 controles ok (`salida_prueba_adenda_1_S1quater.txt`). Dos corridas dan la misma salida.
- **La prueba en contra:** una versión 2 que deja afuera solo cuatro de los cinco documentos da MAL en cinco controles. Está en el
  paquete de la mesa.

## 3. Qué queda sellado con esta adenda

- Quedan sellados cuatro archivos:
  - este documento;
  - `scripts/poblaciones_S1quater_v2.py`;
  - `scripts/prueba_adenda_1_S1quater.py`;
  - `salida_prueba_adenda_1_S1quater.txt`.
- El sha256 de cada uno y la hora están en `sello_adenda_1_diseno_S1quater.txt`.
