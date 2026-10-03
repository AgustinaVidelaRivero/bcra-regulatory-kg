# U-DIAG-PROCESO — estado de cada ficha con el pipeline actual (sesión a7ef8581)

Fuentes. Las fichas vienen de `data/experiment/esq/cobertura/fichas/worksheet_fichas_esq2.json`, idéntico a `b2e9e90`; las líneas que cito son de ese archivo. Para e0-r2 corrí `r5_escalera_particion.py --correr` sobre una copia, en los seis TOs: `estado_fichas_e0r2_udiag_a7ef8581.json`. El código es el de HEAD `f8cf89a`, sin diferencias en el árbol (`git diff --quiet HEAD`) para `e0_lib.py`, `prompt_e1.py`, `comun_e1.py`, `comun_e3.py`, `prompt_e3.py` y `r1_referencias.py`.

Qué significa cada columna:
- «e0-r2 = ficha»: el texto propio y la herencia del chunk e0-r2 son iguales, byte a byte, a los de la ficha.
- «unidad del bloque»: el bloque de donde viene el contenido perdido, o al que apunta el vínculo, tiene su propio chunk en e0-r2.
- «citas»: lo que encuentra `detectar_menciones_r2` en el texto propio y en cada tramo heredado. Es el detector de las reglas (c) a (h); la regla (i) lo aplica sobre la herencia.

| ficha | muestra | chunk | e0-r2 = ficha | bloque perdido / destino del vínculo | unidad del bloque | citas | persiste | por qué |
|---|---|---|---|---|---|---|---|---|
| 11 | azarosa | ayccef::4.2.7.2 | sí | encabezado 4.2.7 «Tener calificación 1, 2 o 3 de la SEFyC, en todos los siguientes aspectos:» | no | solo «Sección 4. …» (el título de la propia sección) | sí | E0 no le da unidad a la línea de título; E1 no extrae de la herencia; E3 no exige títulos |
| 13 | azarosa | expaef::6.6.2 | sí | intro 6.6 «Se deberá comunicar de inmediato a la SEFyC:» | sí (`expaef::6.6::intro`) | solo el título de la sección | sí | la composición queda a criterio del modelo; E3 no recibe el bloque heredado |
| 48 | azarosa | ayccef::3.4.1 | sí | intro 3.4 «La solicitud de autorización deberá ser interpuesta…» | sí (`ayccef::3.4::intro`) | ídem | sí | ídem |
| 52 | azarosa | expaef::1.1.2.5 | sí | encabezado 1.1.2 (la oración se corta en el título) + intro 1.1.2 | intro sí (`expaef::1.1.2::intro`); línea de título no | ídem | sí | ídem; además, la primera mitad de la oración («Las entidades financieras podrán instalar sucursales en el exterior, a cuyo fin deberán») solo existe en el título |
| 64 | azarosa | adrei::4.3.1::intro | sí | el propio bloque «Las entidades financieras deben:» | es la unidad | ídem | sí, en E1 (misma entrada y mismo prefijo) | en la tanda 0, con E3, quedan sin nodo 4 de los 212 bloques así (`bloques_lista_en_grafo_diez_udiag_a7ef8581.json`) |
| 39 | azarosa | lavdin::3.3.4.3 | sí | → la Excepcion de 3.3.4 (bloque heredado) | sí (`lavdin::3.3.4::intro`) | ídem | sí | E1 solo relaciona dentro del chunk (`prompt_e1.py:133`); no hay predicado Obligacion→Excepcion (ficha 39, :4742) |
| 18 | dirigida | prevmi::1.3.3 | sí | → `prevmi::1.2` «Las pautas de previsionamiento … deberán aplicarse sobre las financiaciones comprendidas…» (hermano; mi lectura) | sí (es un punto terminal) | ídem | sí | el destino está fuera de la herencia y sin cita |
| 61 | dirigida | actgar::1.3.1::intro | sí | → `actgar::1.1` «… no podrán afectar sus activos en garantía sin previa autorización del BCRA» (hermano; mi lectura) | sí | ídem | sí | ídem |
| 72 | dirigida | ayccef::3.5.1.1 | sí | → `ayccef::3.5::intro` «Las autorizaciones … quedan condicionadas al cumplimiento … de las siguientes exigencias:» (heredado) | sí | ídem | sí | E1 solo relaciona dentro del chunk; `condicion_de`, también |
| 44 | dirigida (la cita el mandato) | lavdin::3.3.5 | sí | → `lavdin::3.1` (ficha 44, :5412) | sí | ídem | sí | el destino está fuera de la herencia y sin cita |

Observación al margen, fuera del alcance: el detector toma la línea de título «Sección N. <título>» de la herencia como una mención interna de la Sección N (las diez fichas, `citas_en_herencia_r2`). Con la regla (i), esa mención va solo a los nodos cuyo texto nombra la sección (`r1_referencias.py:1176-1225`, `nombra_unidad` en `:890-897`). En estas fichas no genera aristas. No medí cuántas genera en la tanda 0.
