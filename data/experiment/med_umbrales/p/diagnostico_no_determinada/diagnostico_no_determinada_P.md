# Diagnóstico de la comparación `no_determinada` (U-MED-UMBRALES, etapa P, tramo P-a, punto 5)

Determinístico, sin lectura, sin veredicto y sin cifra para la tesis: propone candidatos a clase del §10.1 de la enmienda (FIRMADA en `a0f9815`). La clase la deciden la lectura del piloto y la autora. Generado por `code/diagnostico_no_determinada_P.py` desde `diagnostico_no_determinada_P.json`.

Acta: `data/experiment/med_umbrales/p/acta_sorteo_P.json` (sha256 `435fc76fcfd059c2…`). Grafo `e22fae1afc3cf37f…`.

## 1. Población

331 elementos con contenido y `no_determinada`, todos del ensamblado ({'ensamblado': 331}). Los 305 vacíos van aparte (§2.5).

- por regla: {'sin_marcador': 130, 'sin_marcador_plazo': 201}
- por estrato: {'E-e1-sin': 247, 'E-desc-con': 8, 'E-e1-con': 18, 'E-desc-sin': 55, 'base resuelta': 3}
- por unidad: {'porcentaje': 113, 'meses': 49, 'dias': 105, 'anios': 47, 'moneda': 13, 'veces': 4}
- por TO: {'cap': 123, 'cla': 28, 'ctacte': 23, 'ext': 114, 'lingob': 1, 'pagjub': 1, 'polcre': 7, 'pro': 11, 'ric': 23}
- cómo se ubicó la cuantía en E0: {'cuantia_dentro_del_tramo_de_e1': 265, 'cuantia_desde_descripcion': 58, 'no_ubicada': 6, 'cuantia_sola': 2}

Regla de corte de la cláusula: punto y coma; punto seguido de espacio y de una mayúscula, de un número de punto o del fin del texto; salto de línea solo si abre un ítem, si el renglón anterior termina en dos puntos o si une el texto propio con un bloque heredado (texto_P.clausula); un corte de renglón del PDF no corta; sobre el texto completo de la unidad, con los cortes de renglón unidos. Largo de la cláusula en caracteres: {'n': 325, 'mediana': 237, 'p90': 559, 'max': 2189}.

## 2. Familias del censo léxico sobre la cláusula

Por familia: {'iii': 73, 'ii': 120, 'i': 132, 'sin_clausula': 6}. Precedencia i > ii > iii.

- (i) un marcador de la tabla del §2.4 firmado: candidato *de implementación*;
- (ii) una forma fuera de la tabla: candidato *de la definición*;
- (iii) ningún marcador: la `no_determinada` probablemente es correcta (en los plazos, enmienda 3 a L-ESQ-R2);
- sin_clausula: la cuantía no se ubica en el texto de E0 de la unidad.

El censo es léxico: un marcador de la cláusula puede ser de otra cuantía de la misma oración, y una forma de (ii) puede no tener que ver con la cuantía. Por eso ninguna familia es un veredicto.

### Por estrato

| | i | ii | iii | sin_clausula | total |
|---|---:|---:|---:|---:|---:|
| E-desc-con | 7 | 0 | 1 | 0 | 8 |
| E-desc-sin | 25 | 10 | 14 | 6 | 55 |
| E-e1-con | 8 | 4 | 6 | 0 | 18 |
| E-e1-sin | 89 | 106 | 52 | 0 | 247 |
| base resuelta | 3 | 0 | 0 | 0 | 3 |

### Por unidad

| | i | ii | iii | sin_clausula | total |
|---|---:|---:|---:|---:|---:|
| anios | 14 | 28 | 5 | 0 | 47 |
| dias | 36 | 46 | 18 | 5 | 105 |
| meses | 18 | 21 | 9 | 1 | 49 |
| moneda | 3 | 1 | 9 | 0 | 13 |
| porcentaje | 58 | 23 | 32 | 0 | 113 |
| veces | 3 | 1 | 0 | 0 | 4 |

### Por regla

| | i | ii | iii | sin_clausula | total |
|---|---:|---:|---:|---:|---:|
| sin_marcador | 64 | 25 | 41 | 0 | 130 |
| sin_marcador_plazo | 68 | 95 | 32 | 6 | 201 |

### Por TO

| | i | ii | iii | sin_clausula | total |
|---|---:|---:|---:|---:|---:|
| cap | 50 | 33 | 40 | 0 | 123 |
| cla | 18 | 2 | 8 | 0 | 28 |
| ctacte | 11 | 8 | 4 | 0 | 23 |
| ext | 35 | 63 | 10 | 6 | 114 |
| lingob | 0 | 1 | 0 | 0 | 1 |
| pagjub | 0 | 0 | 1 | 0 | 1 |
| polcre | 4 | 2 | 1 | 0 | 7 |
| pro | 4 | 6 | 1 | 0 | 11 |
| ric | 10 | 5 | 8 | 0 | 23 |

### Por origen del elemento

| | i | ii | iii | sin_clausula | total |
|---|---:|---:|---:|---:|---:|
| descripcion | 33 | 10 | 15 | 6 | 64 |
| e1 | 99 | 110 | 58 | 0 | 267 |

## 3. Familia (i): marcadores y por qué la regla no los tomó

Marcadores de la tabla en la cláusula: {'hasta': 47, 'super-/exced- (minimo_estricto; negado, maximo_inclusivo)': 30, 'dentro de': 28, 'igual a / equivalente a': 17, 'pondera / ponderador / coeficiente / factor': 17, 'al menos / por lo menos': 14, 'mayor(es) a / al': 9, 'o mas / o menos pospuesto': 9, 'menos de / menos del': 6, 'como minimo / un minimo de': 6, 'inferior(es) a / al': 5, 'igual o superior / mayor / inferior / menor': 5, 'no inferior / no menos de': 3, 'como maximo': 2, 'mas de / mas del': 2}.

Causa, sobre el texto que leyó la regla: {'marcador_fuera_del_texto_leido': 108, 'forma_no_reconocida_por_las_reglas': 10, 'otra_cuantia_en_medio': 6, 'fuera_de_la_ventana_despues': 5, 'fuera_de_la_ventana_antes': 3}.

- por texto leído: {'tramo de E1': {'marcador_fuera_del_texto_leido': 83, 'forma_no_reconocida_por_las_reglas': 8, 'fuera_de_la_ventana_despues': 4, 'fuera_de_la_ventana_antes': 1, 'otra_cuantia_en_medio': 3}, 'descripción del nodo': {'otra_cuantia_en_medio': 3, 'marcador_fuera_del_texto_leido': 25, 'forma_no_reconocida_por_las_reglas': 2, 'fuera_de_la_ventana_antes': 2, 'fuera_de_la_ventana_despues': 1}}
- contra el contraste con la cláusula de E0 completa: {'marcador_fuera_del_texto_leido': {'no_determina': 71, 'sin_cuantia': 6, 'determina': 31}, 'otra_cuantia_en_medio': {'sin_cuantia': 1, 'no_determina': 5}, 'fuera_de_la_ventana_antes': {'determina': 1, 'no_determina': 2}, 'fuera_de_la_ventana_despues': {'no_determina': 5}, 'forma_no_reconocida_por_las_reglas': {'no_determina': 9, 'determina': 1}}

Anclas de cada causa en `data/experiment/pyd_r2/code/reglas_comparacion.py` (HEAD `2a70b20`):
- el texto que lee la regla es el tramo de E1 del nodo o, si E1 no dio tramo, la descripción (`data/experiment/tanda0/code/ensamblar_tanda0.py:723-727` y `:748`);
- `marcador_fuera_del_texto_leido`: el marcador está en la cláusula de E0 y no en ese texto;
- `limite_de_clausula_en_medio`: `:343-355` (límites «;», «:» y punto) y `:699-700` (la ventana no cruza la cláusula);
- `otra_cuantia_en_medio`: `:512` y `:516` (la ventana no cruza la cuantía anterior ni la siguiente), con `:701-702`;
- `fuera_de_la_ventana_antes` y `_despues`: `:110-111` (10 y 3 palabras) y `:512-519`;
- `forma_no_reconocida_por_las_reglas`: el marcador está dentro de la ventana y la regla no lo toma (formas de `SIMPLES`, `COMPUESTAS` y `ADYACENCIA`, `:367-403`), a revisar caso por caso;
- sin marcador, `no_determinada`: `:224-225` (valores por defecto de `Cuantia`) y `:612-618` (rama 6, enmienda 3).

Contraste (reglas_comparacion.analizar sobre la cláusula de E0 completa): {'total': {'no_determina': 277, 'sin_cuantia': 15, 'determina': 33}, 'por_familia': {'i': {'no_determina': 92, 'sin_cuantia': 7, 'determina': 33}, 'ii': {'no_determina': 120}, 'iii': {'no_determina': 65, 'sin_cuantia': 8}}}.

## 4. Familia (ii): formas fuera de la tabla

En la familia (ii): {'a partir de / luego de / despues de / transcurrido': 48, 'periodo de referencia (ultimos, anteriores, previos, siguientes, subsiguientes)': 47, 'maximo / minimo no pegado a la cuantia': 19, 'limite(s)': 10, 'sera(n) de': 7, 'entre … y …': 5, 'antes de': 3, 'mayor de / menor de (la calibracion P3 pide «a» o «al»)': 2, 'tope(s)': 1}.

En todas las cláusulas (también en las de (i)): {'a partir de / luego de / despues de / transcurrido': 68, 'periodo de referencia (ultimos, anteriores, previos, siguientes, subsiguientes)': 67, 'maximo / minimo no pegado a la cuantia': 35, 'entre … y …': 16, 'limite(s)': 11, 'sera(n) de': 8, 'antes de': 4, 'mayor de / menor de (la calibracion P3 pide «a» o «al»)': 2, 'tope(s)': 1}.

## 5. Candidatos a clase del §10.1 (sin veredicto)

1. **El texto que leyó la regla no trae el marcador que la cláusula sí trae** (causa `marcador_fuera_del_texto_leido`: 108; con la cláusula completa la regla fija un sentido en 31). Si la lectura lo confirma, la causa está en E1 (el tramo recorta el marcador) o en la descripción; el §10.2 la manda al backlog salvo que la autora decida que la regla lea la cláusula de E0, lo que cambia la definición (L-ESQ-R2 §1.3, punto 3).
2. **Una forma de la tabla que la regla no toma dentro de la ventana** (`forma_no_reconocida_por_las_reglas`: 10): candidato de implementación.
3. **Ventana** (`fuera_de_la_ventana_antes` y `_despues`: 8).
4. **Formas fuera de la tabla** (familia (ii): 120): candidatos de la definición, por forma (sección 4).
5. **Sin marcador** (familia (iii): 73): la `no_determinada` probablemente es correcta; por regla: {'sin_marcador': {'iii': 41, 'i': 64, 'ii': 25}, 'sin_marcador_plazo': {'ii': 95, 'i': 68, 'sin_clausula': 6, 'iii': 32}}.

## 6. Ejemplos (solo de fuera de la muestra)

A ciegas: 10 elementos de la población están en la muestra y 5 los daría la regla del lote 3; cuentan en los agregados y no aparecen ni en el listado ni en los ejemplos.

**(i), marcador fuera del texto leído, y la cláusula completa lo fija:**
  - `Condicion_deduccion_beneficios_decreto_277_22_del_monto_limite__si_el_cliente_es_beneficia_2fc5b9#u0` (ext, E-desc-sin, porcentaje): cuantía «30%»; cláusula: «…l concepto de utilidades y dividendos cursadas a través del mercado de cambios desde el 17/01/20, incluido el pago cuyo curso se está solicitando, no supere el 30% (treinta por ciento) del valor de los nuevos aportes de inversión extranjera directa en e…»
  - `Condicion_maximo_dos_refinanciaciones_en_12_meses__deudores_que_refinanciaron_sin_incurrir_4f432d#u1` (cla, E-e1-sin, meses): cuantía «12 meses»; cláusula: «…rrido en atrasos en el pago de sus servicios, podrán permanecer en esta categoría, cuando hayan accedido, como máximo, a dos refinanciaciones, en el término de 12 meses, contados desde la última refinanciación otorgada.»

**(i), marcador fuera del texto leído, y tampoco con la cláusula completa:**
  - `Condicion_cobertura_intereses_primeros_2_anos_por_endeudamiento_refinanciado__el_acceso_al_769757#u0` (ext, E-e1-sin, anios): cuantía «2 (dos) años»; cláusula: «…intereses devengados hasta la fecha de refinanciación y, en la medida que los nuevos títulos de deuda no registren vencimientos de capital durante los primeros 2 (dos) años, el monto equivalente a los intereses que se devengarían en los primeros 2 (dos) años por…»
  - `Condicion_cobertura_intereses_primeros_2_anos_por_postergacion_capital__el_acceso_al_merca_1f404f#u0` (ext, E-e1-sin, anios): cuantía «2 (dos) años»; cláusula: «…intereses devengados hasta la fecha de refinanciación y, en la medida que los nuevos títulos de deuda no registren vencimientos de capital durante los primeros 2 (dos) años, el monto equivalente a los intereses que se devengarían en los primeros 2 (dos) años por…»

**(i), forma que la regla no toma:**
  - `Condicion_fondos_de_endeudamientos_financieros_punto_3_5__los_fondos_estan_depositados_en__43ec48#u0` (ext, E-e1-sin, dias): cuantía «365 (trescientos sesenta y cinco) días corridos»; cláusula: «…mbre originados en endeudamientos financieros comprendidos en el punto 3.5. y su monto no supera el equivalente a pagar por capital e intereses en los próximos 365 (trescientos sesenta y cinco) días corridos.»
  - `Condicion_no_presentacion_de_descargo_en_plazo__cuando_la_entidad_no_presenta_su_descargo__8acede#u0` (cap, E-desc-sin, dias): cuantía «30 días corridos»; cláusula: «La entidad dispondrá de 30 días corridos contados desde la notificación de la determinación efectuada por la SEFyC a fin de formul…»

**(i), ventana:**
  - `Excepcion_excepcion_a_la_exigencia_de_conformidad_previa_del_bcra_para_acceso_al_mercado_d_795196#u0` (ext, E-desc-con, porcentaje): cuantía «25%»; cláusula: «13.4.7. el pago se concreta en el marco de lo dispuesto en el punto 4.8.5. por un cliente que suscribió BOPREAL Serie 1 por un monto igual o mayor al 25% (veinticinco por ciento) del total pendiente por sus deudas elegibles para los puntos 4.4…»
  - `Excepcion_las_exportaciones_de_bienes_efectuadas_por_un_vpu_adherido_al_rigi_por_un_proyec_71be79#u0` (ext, E-e1-sin, porcentaje): cuantía «0%»; cláusula: «i) 0% (cero por ciento) embarcada dentro del año de plazo.»

**(ii):**
  - `Condicion_ccp_deja_de_calificar_como_qccp__supuesto_en_que_una_entidad_de_contraparte_cent_cb0fdb#u0` (cap, E-e1-sin, meses): cuantía «tres meses»; cláusula: «En los casos en que una CCP deje de calificar como QCCP, durante los tres meses siguientes las operaciones podrán mantener el tratamiento del punto 4.3.3.»
  - `Condicion_cheques_emitidos_en_los_30_dias_anteriores_al_cierre__cheques_que_fueron_emitido_f5b70d#u0` (ctacte, E-e1-sin, dias): cuantía «30 días»; cláusula: «Cheques emitidos en los 30 días anteriores a la fecha de notificación del cierre de la pertinente cuenta.»

**(iii):**
  - `Condicion_cancelacion_menor_al_15_del_importe__aun_no_se_ha_cancelado_el_15_del_importe_in_bd97ff#u0` (cla, E-e1-sin, porcentaje): cuantía «15 %»; cláusula: «…ra que cuenten con la opinión del auditor externo de la entidad sobre la factibilidad del cumplimiento de la refinanciación, cuando aún no se haya cancelado el 15 % del importe involucrado en el citado acuerdo y siempre que dicho acuerdo se haya alcanzad…»
  - `Condicion_convenios_de_pago_situacion_juridica__se_considera_la_situacion_juridica_del_deu_23c0e1#u0` (cla, E-e1-con, porcentaje): cuantía «10 %»; cláusula: «…cordatos judiciales o extrajudiciales homologados (incluyendo los acuerdos preventivos extrajudiciales homologados) a vencer cuando aún no se haya cancelado el 10 % del importe involucrado en el citado acuerdo.»

