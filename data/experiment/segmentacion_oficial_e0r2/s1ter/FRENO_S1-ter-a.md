# U-SEG-OFICIAL — FRENO S1-ter-a (10/10/2026)

Tramo a de S1-ter: el mandato FIRMADO en `e543cb2`, con sus notas al pie hasta `bbcfb45`, y las notas del mandato de S0-5a (`32c71ca`,
`84695b8`, `be88fdf`, `06110c5`, `3c5f003` y `521e220`), leídas en sus commits. USD 0, sin API; código de E0 de `af7ffdd`, sin editar.
Escribí solo `s1ter/` y el scratchpad. Nada commiteado. No sorteé, no leí ni marqué. Detalle y anclas: `REPORTE_S1-ter-a.md`; sha256 de
cada archivo en `manifest_salida.json` (`5e63dff2…`, todo salvo este freno).

**Entrada** (`precondiciones_S1ter.txt`): `af7ffdd` y `521e220` en el log, ancestros de HEAD (`c080914`); E0 del repo `bd2190ad…`,
`68bd74b5…` y `789630b5…`; los dos archivos de la mesa dan `a81ebf65…` y `5bec1dce…`; foto del repo (48.762 archivos) y 2.213 `.pyc`.

**Manifiesto** (`f59cdea0…`): contra el de S1-bis difieren solo los cuatro campos declarados (ruta `s1ter/e0`, commit `af7ffdd`,
unidad y descripción); las 152 filas son iguales. La clase de ri_spi sigue siendo la de la partición: la reclasificación rige en la
población.

**Corrida doble** (sobre una copia sin enlaces, 13:58:52 a 14:17:22, código 0): 768 y 768 archivos, **0 distintos**; **768 de 768
iguales** al manifiesto de S0-5a-bis (`176cbdc0…`) y al de S0-5b; **9.665 unidades**. Tanda 0: 25 de 25 archivos y 35 de 35 entradas de
agregados dentro de los 152, y la tanda 0 completa, 57 de 57 iguales a `salida_tanda0_r2b/`. Health-check, 107 sanos y 45 con señales,
igual que en S1-bis por TO; 0 TOs por punto en 0 chunks, 0 ids repetidos, cobertura 152 de 152. Vigencia, byte a byte igual a S1-bis.

**Censos.**
- Renglones (regla v2 de S1 con el cambio de S1-bis): **333** (260 + 73) en 188 páginas de 92 TOs; **28 sin explicación**. Son los
  327 y los 22 de S1-bis más 6 renglones nuevos, todos de ri_ccna, p. 39. **Límite medido del censo:** son las seis letras del rótulo
  vertical «CODIGO», que R5-e junta en un renglón dentro de `ri_ccna::D1F4::S0`; la regla compara renglón contra renglón y no los ve.
  No es texto perdido.
- 1.16: sobre la salida de S0-4b, el detector corregido da **317, los mismos ids y campos que la mesa** (121 y 316). Sobre la de S0-5b:
  **285 en 98 TOs**.
- Herencia: **28 unidades con recorte en 4 TOs** (S1-bis: 35 en 5; salen las 7 de snp_tr).

**Poblaciones, sin sortear** (`poblaciones_S1ter.json`, `a1313bd6…`, con el sha256 de los ids de cada una):
- **Cortes:** `vigente` 8.063 (0,8417), `marcadores` 192 (0,0200), `sin_raiz` 1.324 (0,1382), con las 92 de ri_spi en `sin_raiz`.
  - **La condición de ri_spi se cumple:** R5-c quita `ri_spi::SB::chapeau_seccion` y `ri_spi::SC::chapeau_seccion`
    (`s0_5/bis/censos/censo_por_regla_S0-5a-bis.md:67`), y las 4 unidades de C heredan el título entero, «C. DENUNCIAS POR
    INCUMPLIMIENTOS RELACIONADOS CON EL / APARTADO B» (las 53 de B, el suyo).
  - Límites declarados en la población: 56; se esperan 1,11 en la muestra. `ri_secoexpo::S17` está en `sin_raiz`.
- **1.16 (a):** 285 − 28 de los 35 que siguen siendo candidatos − 0 de los 3 de diseño = **257 en 97 TOs** (68 de la tanda 1, 21 de
  la tanda 0).
- **1.16 (b): 36.** Son las 32 listas de cierre y los 2 mixtos (las 34 con su cierre nuevo), `ri_oc::S2`, que ya no termina en «3.
  Aclaraciones», y una de las 51 de `ri_oc::3.1` a `3.51`, que heredan «3. Aclaraciones».
- **Regresión:** los 35 están en la salida; 27 iguales a S0-4b y 8 cambiadas (los 6 casos, `ri_oc::C.11` y `ri_rml::1.2.3`).
- **Declarado:** 99 de las 100 unidades que leyó S1-bis están en la población de cortes (84 sin cambios); se esperan 2,20 repetidas
  en la muestra de 90.

**Decisiones para la autora, antes del sorteo:**
1. **(a) y (b) se cruzan en 9 listas** que siguen siendo candidatas del detector: `apnf::1.3.1.2`, `cedin::7.1.3.2`, `depinv::1.9.2`,
   `efemin::2.3.2`, `evacre::2.1.2`, `finsec::5.1.2`, `finsec::5.2.5`, `gracre::6.7.2` y `ri_spi::C.1.3`. Si una sale en (a), se
   repite entre las 66 y el orden pide 66 ids distintos. Propongo sacarlas de (a), porque (b) las lee todas: (a) queda en **248**
   (`a2737e04…`).
2. **5 candidatos de (a) no están en la población de cortes:** `manual::2.3.2` y `manual::S4::parte1` (vía fuera), `ri_pspii::S2` (vía
   por página) y `ri2_pm::2.2.3` y `ri2_pm::3.5.5`, que son de sus unidades por punto. La E0 de los tres primeros no llega al grafo. Si
   salen, con lo del punto 1, (a) queda en **245** (`23a8f605…`). Según el texto del despacho, entran.
3. **Los dos mixtos de (b).** Dentro de su último ítem queda un límite medido: los Anexos I y II en `ri_spi::C.1.3`; los puntos 15 y 16
   del Anexo III y el Anexo IV en `ri2_ae::14.3`.
   - (i) Si la lectora marca un error de corte solo por ese resto, ¿se revierte R5-a en la lista? Volver a S0-4b no lo arregla y deshace
     el cierre.
   - (ii) El último ítem de `ri2_ae::14.3` está partido por tamaño en tres partes. R5-a movió texto solo de `parte1`, de 5.556 a 5.131
     caracteres, al cierre nuevo `ri2_ae::S14::cierre`. Propongo que su ficha muestre `parte1` y el cierre.

**Convivencia** (foto sha256 antes, 13:56:43, y después; `convivencia_S1-ter-a.txt` del paquete): 796 archivos nuevos, todos en
`s1ter/` (768 de `e0/`, sin rastrear, y 28 de registro, este freno incluido); ninguno cambiado ni borrado; HEAD sin cambios; ninguna
escritura de otra mano. `.pyc` fuera de `.venv`: 2.213 antes y después, la misma lista.
**Grep de convenciones** (script de S0-4, control positivo 16 de 16; `grep_convenciones_S1-ter-a.txt` del paquete): sobre el texto que
escribí (este freno, el informe, las precondiciones, los sellos, el control de la tanda 0 y los 10 scripts), 0 coincidencias: 0 nombres de
personas, 0 referencias al origen de una decisión y 0 rutas absolutas. En los JSON del registro solo coincide texto de los PDF: 9
coincidencias de un mismo término, todas en renglones de la norma. En `e0/`, 669 coincidencias de texto de la norma y, como en S1-bis, 14 nombres propios del corpus en cateloc y
cirmo3.
**Paquete:** `<scratchpad>/revision_USEG_OFICIAL_FRENO_S1-ter-a/`, 41 archivos más `manifest.txt`: el freno, el informe, el registro
de `s1ter/` con sus scripts, el tar.gz de `s1ter/e0/` y el de la tanda 0, las fotos, el grep, los logs y copia de los dos archivos de
la mesa. **Copia permanente** (CLAUDE.md §4.g), con `ditto`, en
`~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/64082b65-8548-487d-9ff4-27e8bb6283c5/scratchpad/revision_USEG_OFICIAL_FRENO_S1-ter-a/`,
verificada contra su `manifest.txt`: 41 de 41 iguales por sha256 y bytes, ninguno sin listar. El tar.gz de `e0/`, extraído, da 768 de 768
iguales a `manifest_salida.json`.

FRENO. Espero el «seguí» de la autora sobre las decisiones 1 a 3 para el tramo b. No sorteo ni armo fichas.
