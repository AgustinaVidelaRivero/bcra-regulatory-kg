# U-SEG-OFICIAL — FRENO S0-6a-bis (12/10/2026)

**Este archivo nombra unidades con error de corte y de herencia: ninguna lectura a ciegas lo abre, tampoco la de
S1-quater.** De las unidades que no son de las 40 filas ni de las 286 leídas, solo cuentas por regla y por documento.

Paso 0 (la ruta, con `$HOME` en lugar del directorio de la usuaria):

```
$ pwd
$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg
$ git log --oneline -1
d32f6db8 Segmentacion oficial: la correccion de E0 con reglas generales, en freno (diseno, parche, censos y controles)
$ git status --porcelain -- data/experiment/segmentacion_oficial_e0r2/s0_6
$ ls data/experiment/segmentacion_oficial_e0r2/s0_6/bis
ls: data/experiment/segmentacion_oficial_e0r2/s0_6/bis: No such file or directory
```

Mandato `docs/mandatos/USEG_OFICIAL_S0-6a_correccion_E0.md` leído en HEAD (`5edfd993…`), con los cambios del «seguí»;
los cuatro extractos de S0-6a (mismos sha256) y la clasificación de la mesa de los 70 (`b2cb4709…`); nada más del paquete
de la mesa ni de las carpetas prohibidas. USD 0, sin API. **Nada commiteado; el parche no se aplicó al repo; no escribí
en la memoria.** Escribí solo `s0_6/bis/`. Detalle: `REPORTE_S0-6a-bis.md`; diseño: `DISENO_S0-6a-bis.md`.

**Las seis decisiones** (DISENO, §1-§6; REPORTE, §2):
1. Se quedan B, D, F, G y la parte de A que mejora; H, I, J, K y E sin cambios.
2. C no mueve un párrafo cuyos renglones no comparten columna (a 3,0 pt o menos del x0 del segundo, salvo el primero),
   ni el grupo que arrastra, ni un grupo al que le sigue una tabla; lo mide por la columna que comparten (el x0 del
   segundo), no por el renglón más a la izquierda; la columna de un punto cuyo rótulo es un título vuelve a ser la de su
   texto. A no abre divisiones en una carátula (página 1 de cuerpo con a lo sumo 8 renglones, el tope de J). Tolerancia
   de C, 3,0 pt. Definiciones fijadas antes del censo (notas con hora, en el paquete).
3. Las 13 listas, con C ajustada, contra la página (D19, D21, D13 bis; REPORTE, §6):

   | documento | lista | de diseño | queda |
   |---|---|---|---|
   | apnf | 1.3.1.2 | sí | C |
   | cryl | 4.2.2 | sí | C |
   | depaho | 3.11.5.5 | sí | C |
   | manori | 1.1.6.5, 1.4.1.3, 3.4.1.3 | sí | C |
   | ri2_ae | 14.3 | sí | C |
   | ri_oc | B.1.28 | sí | R5-a por lista |
   | ri_rml | 1.4.2 | sí | R5-a por lista |
   | ri_spi | C.1.3 | sí | R5-a por lista |
   | adfsp | 1 lista | no | R5-a por lista |
   | ri_oc | 2 listas | no | R5-a por lista |

   C queda en 7 y R5-a por lista en 6 (3 de diseño y 3 que no lo son; las tres, fuera de S1-quater por la adenda 3, con
   sus ids en `NO_ABRIR_listas_r5a_detalle_S0-6a-bis.json`). **Bolsa:** una lista de R5-a es una corrección hecha para
   su documento (`docs/plan_tesis.md:782`, punto 4). De los seis documentos con una lista que queda, ri_oc y snp_mep ya
   tenían otra lista por documento en el código de E0 de S0-6a (ri_oc, dos de S0-4; snp_mep, la de la cola de título
   estricta de la regla 5 de S0); **adfsp, ri_rml, ri_spi y tasint no tenían ninguna, y salen de la bolsa por esto**, lo
   declaro. Es la cuenta sobre el código de E0; los cortes a mano y los laudos de casos los cuenta la mesa al sortear.
   **Lo declaro también:** con C ajustada, dos listas leídas que no son de las 13 (snp_mep 4.6.2 y
   tasint 3.3.2), donde C coincidía con R5-a en la primera corrida, dejan de coincidir con la página; les apliqué el
   mismo criterio (R5-a por lista). Lista residual: 8 de las 43 de `LISTAS_R5A_S0_5`, en `LISTAS_R5A_S0_6`
   (`correr_e0.py`), y C no las toca.
4. Herencia: la política no cambia. Tamaño (caracteres de `herencia` sumados sobre todas las unidades): S0-5b 3.895.361
   (9.665 unidades), primera corrida 8.634.124 (10.584), esta 5.546.286 (10.478). Siete documentos llevan 1.170.676 de
   esos 5.546.286 (S0-5b: 57.284): cadenas de divisiones de A anidadas (abajo, en las que me parecen un error de una
   regla). El efecto en el costo de E1 y en el tope de la tanda 1, **NO VERIFICADO** (lo calcula la mesa).
5. E1-008: regla L (interruptor `l`), de D15: un índice leído como cuerpo no corta la sucesión. **Cumple su aceptación**:
   E1-008 queda corregida (el Anexo IV de nmaeef abre 4.1.4 a 4.4.2, y 4.4.2 termina antes de 4.5.1) y no rompe ninguna
   unidad leída. **L es general**: con las demás reglas, cambia nmaeef y ri2_ae (su Anexo IV); ningún documento sale de
   la bolsa por L. Sola no cambia nada (actúa dentro de los sub-documentos de A); la medida es el efecto marginal (la
   final contra la final sin L), que agregué después del censo y declaro.
6. E2-002: regla M (interruptor `m`): la raíz 0 de un sub-documento de A aporta a la herencia solo su título (no corre
   en los sub-documentos de S0-4: E2-057 no cambia). E2-002 queda corregida (`ri2_ae::A3::14.3` hereda solo el título de
   la raíz 0 del Anexo III). M es general (cambia la herencia de 137 unidades en 6 documentos). E2-098: R5-a por lista
   en ri_oc B.1; queda corregida (rótulo impreso del Apartado B y el cierre de B.1, sin las notas de B.2 y B.3).

**Parche** `parche/parche_e0_S0-6a-bis.diff` (`a0f291c4…`), completo sobre el código de S0-5b (reemplaza al de S0-6a):
`e0_lib.py` `bd2190ad…` → `d89aab1a…` (+1132 −40), `correr_e0.py` `68bd74b5…` → `78c54c4c…` (+90 −11), `selftest_e0.py`
`789630b5…` → `eb4f11e6…` (+708 −15); en seco, rc 0 y los tres archivos finales byte a byte. **Diff contra el código del
parche de S0-6a** `parche/diff_contra_S0-6a_S0-6a-bis.diff` (`25da715d…`; e0_lib +166 −20, correr_e0 +35 −6, selftest
+173 −13). **Prototipo** `parche/interruptor_prototipo_S0-6a-bis.diff` (`9ffaa359…`, `S0_6_REGLAS` con las letras `a` a
`m`, y `S0_6_TANDA0`); no va al parche de S0-6b.

**Controles** (mandato, §6; REPORTE, §3):
- todas apagadas = S0-5b, 768 de 768 (9.665 unidades);
- los 152: prototipo con todas, código final y otra vez el prototipo, 768 de 768 iguales; con el código del parche, en
  una copia nueva del repo, dos veces más, 768 de 768 iguales entre sí y con la final; **10.478 unidades**; manifiesto
  `manifiestos/manifest_salida_e0_152_S0-6a-bis.json` (`991ac178…`); contra S0-5b, 256 de 768 archivos distintos, regla
  por regla en el censo;
- **tanda 0: 57 de 57, dos veces** (2.439 unidades); **los 25 de la tanda 0 en los 152: 25 de 25**; el censo da 0
  cambios en la tanda 0 y **ninguna clave de la tanda 0 se mueve**;
- `selftest_e0` **251/251** (188 de S0-5b y 63 de S0-6a y S0-6a-bis: los 51 de S0-6a, actualizados, y 12 nuevos: L,
  M, la carátula de A, el grupo y la tabla de C, R5-a por lista que queda; negativos regenerados, 154 leídas de 38 TOs);
  b52 39/39, b581 34/34, b582 59/59, b583 33/33; claves de la caché VEREDICTO OK, igual byte a byte a `923dd900…`;
  selftest de claves VEREDICTO OK (1.057 creadas, 244 quitadas, 1.821 cambiadas, exactamente las declaradas) y FALLA
  con la lista perturbada; continuidad: antes 88 (igual a S0-5b), después 70, selftest 14/14.
- repo: foto sha256 del repo entero (sin `.git`, sin otras exclusiones) antes y después; `.pyc` fuera de `.venv/`, 2.213
  antes; grep de convenciones sobre `s0_6/bis/`, 0 coincidencias (control positivo 16 de 16). La foto y los `.pyc` de
  después, en el mensaje del FRENO (este archivo entra en la foto);
- Tabla de reprocesamiento: fila F19d propuesta con anclas al código final (REPORTE, §14); de las 27 citas de la tabla,
  12 iguales, 14 se mueven y una no se encuentra entera (`correr_e0.py:140-210`, F19b), como en S0-6a.

**Censo por regla** (REPORTE, §7; `censos/`): la final cambia 115 TOs, 3.122 claves (1.057 creadas, 244 quitadas, 1.821
cambiadas). Generales todas salvo **G (solo lingeef), I y K (solo ri_ccna)**. L y M solas no cambian nada; con las demás,
L cambia nmaeef y ri2_ae, y M la herencia de 137 unidades en 6 documentos: las dos son generales. **Salen de la bolsa:
lingeef y ri_ccna** (reglas no generales) **y adfsp, ri_rml, ri_spi y tasint** (listas de R5-a que quedan). Claves por
regla y por documento, en cuentas (`censos/censo_por_regla_S0-6a-bis.md`); la lista entera, en el `NO_ABRIR_`.

**Las 40 filas** (REPORTE, §4): **39 corregidas** (las 36 de S0-6a, E1-008, E2-002 en la herencia y E2-098 en la
herencia) y la de la tanda 0 (E2-055), con error en la salida, como se espera, y corregida en `selftest_e0`.

**Las 70 de la mesa** (REPORTE, §5): aceptación 70 de 70: de las 27 que empeoraban, ninguna sigue como en la primera
corrida (23 vuelven a S1-ter y 4 quedan en un tercer estado); las 36 que mejoran y las 7 neutras siguen. Las 286
leídas: 212 iguales a S1-ter y 74 cambian (28 por una fila del TSV, 46 al FRENO); **las 46 son de las 70, ningún cambio
nuevo en una leída**. Las cuatro en un tercer estado:
- `ri_dcpc::3.7.6`: el corte de E1-010 y la herencia de S1-ter.
- `ri_oc::B.1.5` y `ri_oc::B.1::cierre`: vuelven a S1-ter salvo el rótulo impreso del Apartado B (D, lo que pide
  E2-098).
- `ri_ii_31_12_19::6.3` (regla A): ya no hereda la carátula y la Tabla Nº 1 vuelve a 6.5; sigue sin heredar las
  tablas de códigos de las pp. 16-21, que A pone en divisiones (ya en la primera corrida; S1-ter no juzgó su herencia).
  Esas divisiones me parecen un error de A; **lo dejo a la decisión de la mesa**.

**E1-008:** corregida por L (arriba). No queda como límite declarado.

**Lo que la nota deja en mis manos** (mandato, §7): sin cambios respecto de S0-6a (su DISENO, §4): la tolerancia de C
(3,0 pt), el motivo de E2-065, la causa de J, «Ello, siempre que…» de E1-081 y la aceptación de R5-e actualizada por K.
**Reemplazo por regla general en E2-007 y E2-058** (la adenda 1, §1): como en S0-6a, rigen A (E2-007) y A y D (E2-058);
y en ri_spi, por la decisión 3, el cierre de C.1 vuelve a R5-a por lista (C.1.3).

**Unidades que no son de las 40 ni de las 286 y me parecen un error de una regla** (solo cuentas; REPORTE, §12): A, 10
(adfsp 1, ri_cc 1, ri_ii_31_12_19 5, ri_oc 3); A, cadenas de 10 o más encabezados heredados, 247 (dmrd 3, ri2_cs 8,
ri_cc 28, ri_ccpnp 20, ri_con 30, ri_niif 110, ri_pnp 48; llevan 1.170.676 caracteres de herencia); E, 6 (ri_saofe);
I, 1 (ri_ccna). No cambié ninguna regla por ellas.

**Error propio** (de S0-6a; REPORTE, §13): en el §11 del informe de S0-6a y en su FRENO, dos entradas de A (ri_ccna)
nombran ids que no existen en la salida final de S0-6a (eran de una corrida intermedia y no los controlé contra la
final). Ahora la lista se controla con un script contra la E0 final. Los ids, en el `NO_ABRIR_`.

**Archivos `NO_ABRIR_`** (en el paquete, fuera del repo):
- `NO_ABRIR_antes_y_despues_S0-6a-bis.jsonl` `520f795094aac11b4b5b28f81f863972953600f5f58d88f4303ca510dda9f90d`
- `NO_ABRIR_antes_y_despues_S0-6a-bis.md` `6e22cb5d8d6ccec2a5ce10592adb9add9c5b5f2c59ef47e137fa4f92d2986cf9`
- `NO_ABRIR_cadenas_de_encabezados_A_S0-6a-bis.json` `1903852a3990268f1ebe61662031718c950139e67a183efd8e70a5e4f83d3f5e`
- `NO_ABRIR_censo_por_regla_S0-6a-bis.json` `5fc7bf863ddaf961f83704db39b2f77a3fcc14d743f1274a9d9e56fc43334655`
- `NO_ABRIR_claves_S0-6a-bis.json` `043fadba4c0072e6a93e2a5aa4ecc3d4bef46f97837e26e0eb5c9d985bb16db8`
- `NO_ABRIR_claves_S0-6a-bis_perturbada.json` `7587b06f96a2da2084f76f8cf4f2e2c311cfa051a326b7f50165f5ff5bbac97d`
- `NO_ABRIR_claves_control_S0-6a-bis.json` `f65d964028d29dc9e28cfb9b5c26888ea063eb6dda9428afac68b9d7e9af6af0`
- `NO_ABRIR_claves_control_negativo_S0-6a-bis.json` `6c5597b82e873eaceaa4217cd712dbacb694d9ce1548a0416ead7d2d036b3663`
- `NO_ABRIR_control_continuidad_antes_S0-6a-bis.json` `f75f7e7633f2c8a498f376e64d023b4b95082ddc6ac7ccb96f8c39e3da81aa80`
- `NO_ABRIR_control_continuidad_despues_S0-6a-bis.json` `5c96d6ad9c361b8f9c96275c5cf8befd91fc609d5a5c59540e84717138b95f4c`
- `NO_ABRIR_e0_152_S0-6a-bis.tar.gz` `5ee59af2ec0ad2d088e7529b6750ca6fe1c04702affef55f8876eec2836a6207`
- `NO_ABRIR_errores_de_regla_S0-6a-bis.json` `cac5534da80579f02c9e5861d37d65b735c660dc2de9badb023012d2d75ae65e`
- `NO_ABRIR_lista_continuidad_S0-6a-bis.md` `d2339751a0b391cc714063251cad692c21d24a99067a67a939a021f5d524ce6c`
- `NO_ABRIR_listas_r5a_detalle_S0-6a-bis.json` `3556af2c3adf6c6eca6c636d6eb55b740435e17867d1e8f69d40edc18dd783a3`
- `NO_ABRIR_notas_definiciones_S0-6a-bis.md` `0ba307427ccbbf0c604a8590a5407aff7ddc59d5c5b0355538d5015657e427f5`
- `NO_ABRIR_rechazos_e_detalle_S0-6a-bis.json` `9c47009ad96e45ff2338112df5a326e5e24295f140da77652d93174d72da1202`
- `NO_ABRIR_reemplazos_S0-6a-bis.json` `0d8fdd8052ce9a7270b49620c56dbbdaa2d9cd3ba3630955d6891830877864a2`
- `NO_ABRIR_tanda0_medicion_sin_exclusion_S0-6a-bis.json` `8edd03d81fccd8baa39ddd44a762ecd7b8c497c6cc030d98ef8a756fe85916ba`
- `NO_ABRIR_tanda0_medicion_sin_exclusion_S0-6a-bis.tar.gz` `72faee698dcf04251d2de672e6ea1b8f29cbd0ad8d8a9ba08a9570c2b3ae18ab`

**Paquete**: `revision_USEG_OFICIAL_FRENO_S0-6a-bis/`, con su `manifest.txt`, copiado con `ditto` a
`~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/3affae38-5acf-4382-b2ca-6d7f152ddb34/scratchpad/revision_USEG_OFICIAL_FRENO_S0-6a-bis/`;
la verificación de esa copia contra el `manifest.txt` va en el mensaje del FRENO.

**Mensaje de commit PREPARADO** (no corrí ningún commit):

```
Segmentacion oficial: la correccion de E0 ajustada, en freno (diseno, parche, censos y controles)
```

FRENO.
