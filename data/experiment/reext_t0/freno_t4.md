# FRENO T4 de U-REEXT-T0, primer tramo: sorteos, fichas y puntos 2 a 4 (06/10/2026; USD 0, sin API; sin commit)

**Precondiciones a–d** (salida completa: `UREEXT_T0_T4_precondiciones_abcd.txt`, en el paquete): `c9540c0` es el último commit de `reext_t0` y HEAD es `3da9c2a`; `git status` sin cambios en `data/experiment`, `scripts` ni `docs/mandatos`; los dos kg son `a9631a64…` y `6e756043…`, iguales a la fixture y a `grafos.py` (`commit_sellado` `bbc38dc`); `sellos_t4.json` es `7845d11a…`; la cola tiene 74 unidades, con `cap::4.2.1.2::parte1`. Trabajo sobre una copia sin enlaces simbólicos.

**Sorteos, antes de leer** (`t4/sorteos_t4.py --out …`; `t4/salida/sorteos_t4.json`, hora `2026-10-06T11:59:36-03:00`; dos corridas byte a byte iguales, las dos en el mismo segundo):
- Punto 1: 74 unidades en la cola (29 `cola_humana`, 43 `…veredicto_inutilizable` y 2 `…reextraccion_invalida`), igual a la cola del reporte del ensamblado. Muestra de 30, con la parte 1.
- Punto 8: 1.137 omisiones `meta_normativo` en `ens_diez_r2b/r2/omisiones.jsonl`: 733 sin marca del contador y 404 con marca. Se sortean 30 de cada grupo.

**Punto 2**, las 15 preguntas (`t1_preguntas_control.py --kg …ens_diez_r2b/r2/kg.json --e0 …salida_tanda0_r2b`, en la copia, y `t4/preguntas_t4.py`; salida en `preguntas_t4.md`). No son evaluación. r2b da 12 bien, 1 en parte, 2 falso y 0 no; r2a daba 8, 2, 3 y 2. Cambian 4: la 1 (falso → bien), la 7 (en parte → bien), y la 8 y la 14 (no → bien). Siguen en falso la 9 y la 12, y en parte la 5.

**Punto 3**, copia de la nota de E3 (`t4/lista_copia_nota_t4.py` y `t4/clasificacion_copia_nota_t4.py`), con la regla `1427b16c…` sin ajustes. Hay 86 casos en 64 unidades, y las 64 coinciden con `copias_nota_e3.jsonl`. Copia real 29, dudosa 3, coincidencia legítima 54 y metalenguaje 0; 27 unidades tienen al menos una copia real. El cotejo mecánico dio clase 3 en 37 casos, y la lectura no confirma 8. Referencia en r2a: 11 de 45.

**Punto 4**, tercer escalón (`t4/escalon3_t4.py`): 0 de los 2.445 registros de E1 tienen la marca `escalon_3`, y ningún `resumen_e1.json` trae la clave. Hubo 9 registros con reintento por corte, en 8 unidades, y todos pasaron con el segundo escalón (16.384).

**Fichas para adjudicar** (`t4/fichas_t4.py --salida …`; `t4/salida/fichas_punto{1,5,6,7,8}_*.md`; resumen en `resumen_lecturas_t4.json`). Doy cuentas de mi propuesta, sin tasas ni Wilson hasta la adjudicación:
- **1, cola humana:** 12 con error, 1 dudosa (`cap::6.2.2.4`) y 17 sin error, de 30. Las omisiones van aparte, en 6 unidades.
- **5, las 27 de P4b** (respuesta de E1; las 27 claves son las de P5). Por grupo: a_transicion 0/1, a 1/3, c 1/4, d 3/4, e 3/4, b1 ítems 0/3, b2 ítems 0/3, b encabezados 0/2, ejemplo 2/2, f 1/1. Contra P5: 4 respuestas son idénticas a una de P5 y 23 difieren de las dos; la marca cambia en 3 contra la corrida a y en 5 contra la b.
- **6, las listas:** b1 encabezados 1/3 e ítems 9/21; b2 encabezados 5/7 e ítems 0/32. `ctacte::3.2`, aparte: 0/1 y 0/5. Hay 3 dudosas.
- **7, grupo c.** Fase A, sobre el texto, registrada a las `12:22:15-03:00` en `grupo_c_fase_a.md`, antes de volcar ninguna extracción: leí 35 unidades; 30 tienen más de un supuesto y 5 se saltean. Fase B: cumple 1 de 30 (`ext::10.3.6`). Fallas: 26 con el supuesto dentro de la norma, 6 por fusión, 6 sin relación, 6 con el umbral en la norma, 3 por omisión y 2 incoherentes.
- **8, omisiones.** Sin marca: 19 de 30 son normativas, 0 habilitantes y 11 dudosas; con el tramo heredado hay 4, de las que 3 son normativas. Con marca: 25 de 30 son normativas, 3 habilitantes y 8 dudosas; con el tramo heredado hay 18, de las que 17 son normativas.

**Para decidir**:
- (i) **Contradicción entre los puntos 5 y 7.** En `ext::10.3.6` la marca de P5, que reuso en el punto 5, es «cumple». Con la regla estricta del punto 7 no cumpliría: el supuesto de la porción con pagos a la vista va dentro de la Excepcion.
- (ii) Conté como normativas, y dudosas, 5 remisiones sin marca, como «de acuerdo con el punto…». Sin ellas quedan 14 de 30.
- (iii) Conté las recomendaciones («es deseable», «se recomienda») como deber con fuerza de recomendación: son 6 con marca.
- (iv) El mandato no define «habilitante». Tomé la definición del pre-registro de ESQ-3b v2 (`40493c9`) y del §4 de la enmienda 7 (`44c6e1b`).
- (v) Hay 18 omisiones con marca con el tramo heredado: el ítem vuelve a registrar el texto de su encabezado.

**Errores propios**, corregidos antes de las cifras. En la fase B, el lector no traía los umbrales de la extracción final, que están en `umbrales_tramos`: lo vi en la tercera unidad, antes de marcar ninguna, y lo corregí; las lecturas de los puntos 1 y 6 no dependen del umbral. En el control de cierre, mi recorrido trató los enlaces simbólicos distinto que el registro de apertura y dio 339 cambios falsos: lo repetí con el mismo método.

**Controles**: los generadores corrieron dos veces sobre la copia y dieron archivos idénticos byte a byte. En el repo hay 30 archivos nuevos, los de `reext_t0/t4/` y este freno, y 0 cambiados o quitados. Hay 2.213 `.pyc`. No usé la clave de la API. El grep de convenciones está en el paquete, con su salida.

**Paquete:** `revision_UREEXT_T0_FRENO_T4/`, en el scratchpad. **Adjudicación PENDIENTE de la autora; commit PENDIENTE. Espero el «seguí» para el segundo tramo (tasas); T5 no empezó.**
