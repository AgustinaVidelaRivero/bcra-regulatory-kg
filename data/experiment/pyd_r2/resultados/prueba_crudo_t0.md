# U-PYD P2 — validador r2 sobre el crudo guardado (r1 y tanda 0)

Comando: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/pyd_r2/code/prueba_crudo_t0.py`

Política: `data/experiment/pyd_r2/politica_campos_r2.json`, sha256 `e0c81cff7710e6b5b1c75640685ff22fea28fe35572f0dcd06db632e21d1d1eb`. Fuentes leídas en `3ffb99d` (firma del mandato) con candado de sha256; crudo con los sellos de N1 (43 archivos).

Capas: L0 = primer intento de E1 (`tool_input_crudo`); L0r = reintentos de E3 (`e1_reintentos.db`, immutable=1).

## 1. Volumen y rechazos

| grupo | capa | registros | entidades in | entidades out | relaciones in | relaciones out | rechazos por motivo |
|---|---|---|---|---|---|---|---|
| r1 | L0 | 1763 | 8010 | 8009 | 11827 | 11707 | entities_o_relations_invalidos 1, extremo_chunk_ausente 2, firma_invalida 108, punto_fuera_de_admitidos 1, ref_colgante 10 |
| r1 | L0r | 431 | 2685 | 2685 | 4360 | 4241 | entities_o_relations_invalidos 1, firma_invalida 116, predicado_invalido 2, ref_colgante 1 |
| desarrollo | L0 | 1763 | 7973 | 7973 | 11322 | 11023 | entities_o_relations_invalidos 3, firma_invalida 279, ref_colgante 14, sujeto_en_predicado_no_sujeto 4, sujeto_extremo_ausente 2 |
| desarrollo | L0r | 192 | 1149 | 1148 | 1865 | 1802 | firma_invalida 62, punto_fuera_de_admitidos 1, ref_colgante 1 |
| cinco | L0 | 671 | 2523 | 2521 | 3400 | 3346 | entities_o_relations_invalidos 1, extremo_chunk_ausente 3, firma_invalida 48, ref_colgante 1, sujeto_en_predicado_no_sujeto 2, type_invalido 2 |
| cinco | L0r | 63 | 266 | 266 | 358 | 344 | firma_invalida 14 |
| diez | L0 | 2434 | 10496 | 10494 | 14722 | 14369 | entities_o_relations_invalidos 4, extremo_chunk_ausente 3, firma_invalida 327, ref_colgante 15, sujeto_en_predicado_no_sujeto 6, sujeto_extremo_ausente 2, type_invalido 2 |
| diez | L0r | 255 | 1415 | 1414 | 2223 | 2146 | firma_invalida 76, punto_fuera_de_admitidos 1, ref_colgante 1 |

## 2. Valores fuera de lista por campo y tratamiento

Cada fila: valor original y tratamiento de la política r2 (normalizado, registrado con marca, rechazado).

| grupo | capa | campo | valor | tratamiento |
|---|---|---|---|---|
| r1 | L0 | predicado | 'aplicaA' | normalizado_forma 1 |
| r1 | L0 | predicado | 'exceptua_restriccion' | normalizado_alias 1 |
| r1 | L0 | Obligacion.tipo | 'verificacion' | normalizado_a_otra 1 |
| r1 | L0 | Obligacion.tipo | 'verificacion_informativa' | normalizado_a_otra 1 |
| r1 | L0 | Comunicacion.tipo | '' | externa_por_codigo_o_label 1, registrado_fuera_de_lista 1 |
| r1 | L0 | Comunicacion.tipo | 'Decreto' | externa_por_valor 1 |
| r1 | L0 | Comunicacion.tipo | 'LEY' | externa_por_valor 1 |
| r1 | L0 | Comunicacion.tipo | 'MINISTERIAL' | externa_por_codigo_o_label 1 |
| r1 | L0 | Comunicacion.tipo | 'Resolución' | externa_por_valor 1 |
| r1 | L0 | Comunicacion.tipo | 'decreto' | externa_por_valor 1 |
| r1 | L0 | Comunicacion.tipo | 'interna' | registrado_fuera_de_lista 2 |
| r1 | L0 | Comunicacion.tipo | 'normas' | registrado_fuera_de_lista 1 |
| r1 | L0 | Comunicacion.tipo | 'referencia' | registrado_fuera_de_lista 1 |
| r1 | L0 | Comunicacion.tipo | 'referencia a normas' | registrado_fuera_de_lista 1 |
| r1 | L0 | Comunicacion.tipo | 'referencia_normativa' | registrado_fuera_de_lista 2 |
| r1 | L0 | Obligacion.frecuencia | 'mensual y trimestral' | registrado_fuera_de_lista 1 |
| r1 | L0 | Obligacion.frecuencia | 'mensualmente' | normalizado_desde_tramo 1 |
| r1 | L0 | Obligacion.frecuencia | 'periodicidad mínima a indicarse' | registrado_fuera_de_lista 1 |
| r1 | L0 | Obligacion.frecuencia | 'periódicamente' | registrado_fuera_de_lista 1 |
| r1 | L0 | Obligacion.frecuencia | 'por operación' | registrado_fuera_de_lista 1 |
| r1 | L0 | Obligacion.frecuencia | 'por período informativo' | registrado_fuera_de_lista 1 |
| r1 | L0 | padre_sugerido | 'Sujeto_acreedor_del_exterior' | fuera_de_catalogo_anulado 1 |
| r1 | L0r | predicado | 'estableci_en' | rechazado 1 |
| r1 | L0r | predicado | 'establecia_en' | rechazado 1 |
| r1 | L0r | Obligacion.tipo | 'verificacion' | normalizado_a_otra 1 |
| r1 | L0r | Comunicacion.tipo | 'norma' | externa_por_codigo_o_label 1 |
| r1 | L0r | Comunicacion.tipo | 'otro' | registrado_fuera_de_lista 1 |
| r1 | L0r | Comunicacion.tipo | 'referencia' | registrado_fuera_de_lista 1 |
| r1 | L0r | Comunicacion.tipo | 'referencia_interna' | registrado_fuera_de_lista 1 |
| desarrollo | L0 | tipo_entidad | 'Restriction' | normalizado_alias 2 |
| desarrollo | L0 | predicado | 'establec\nida_en' | normalizado_forma 1 |
| desarrollo | L0 | Restriccion.tipo | 'limite_temporal' | registrado_fuera_de_lista 3 |
| desarrollo | L0 | Restriccion.tipo | 'obligacion_cualitativa' | registrado_fuera_de_lista 1 |
| desarrollo | L0 | Comunicacion.tipo | 'TO' | registrado_fuera_de_lista 1 |
| desarrollo | L0 | Comunicacion.tipo | 'referencia' | registrado_fuera_de_lista 3 |
| desarrollo | L0 | Obligacion.frecuencia | 'a cada requerimiento del usuario' | registrado_fuera_de_lista 1 |
| desarrollo | L0 | Obligacion.frecuencia | 'cuando corresponda' | registrado_fuera_de_lista 1 |
| desarrollo | L0 | Obligacion.frecuencia | 'mensual y trimestral' | registrado_fuera_de_lista 1 |
| desarrollo | L0 | Obligacion.frecuencia | 'según cálculo de capital' | registrado_fuera_de_lista 1 |
| desarrollo | L0 | padre_sugerido | 'Sujeto_entidad_financiera' | sin_mencion_descartado 1 |
| desarrollo | L0r | Comunicacion.tipo | 'otro' | registrado_fuera_de_lista 2 |
| desarrollo | L0r | Obligacion.frecuencia | 'en cada ciclo de clasificación' | registrado_fuera_de_lista 1 |
| cinco | L0 | tipo_entidad | 'Recomendacion' | rechazado 2 |
| cinco | L0 | predicado | 'establec ida_en' | normalizado_forma 1 |
| cinco | L0 | Obligacion.tipo | 'evaluacion' | normalizado_a_otra 1 |
| cinco | L0 | Obligacion.tipo | 'obtención_de_datos' | normalizado_a_otra 1 |
| cinco | L0 | Obligacion.tipo | 'pago' | normalizado_a_otra 1 |
| cinco | L0 | Comunicacion.tipo | 'Resolución' | externa_por_valor 1 |
| cinco | L0r | Comunicacion.tipo | '' | registrado_fuera_de_lista 1 |
| diez | L0 | tipo_entidad | 'Recomendacion' | rechazado 2 |
| diez | L0 | tipo_entidad | 'Restriction' | normalizado_alias 2 |
| diez | L0 | predicado | 'establec\nida_en' | normalizado_forma 1 |
| diez | L0 | predicado | 'establec ida_en' | normalizado_forma 1 |
| diez | L0 | Obligacion.tipo | 'evaluacion' | normalizado_a_otra 1 |
| diez | L0 | Obligacion.tipo | 'obtención_de_datos' | normalizado_a_otra 1 |
| diez | L0 | Obligacion.tipo | 'pago' | normalizado_a_otra 1 |
| diez | L0 | Restriccion.tipo | 'limite_temporal' | registrado_fuera_de_lista 3 |
| diez | L0 | Restriccion.tipo | 'obligacion_cualitativa' | registrado_fuera_de_lista 1 |
| diez | L0 | Comunicacion.tipo | 'Resolución' | externa_por_valor 1 |
| diez | L0 | Comunicacion.tipo | 'TO' | registrado_fuera_de_lista 1 |
| diez | L0 | Comunicacion.tipo | 'referencia' | registrado_fuera_de_lista 3 |
| diez | L0 | Obligacion.frecuencia | 'a cada requerimiento del usuario' | registrado_fuera_de_lista 1 |
| diez | L0 | Obligacion.frecuencia | 'cuando corresponda' | registrado_fuera_de_lista 1 |
| diez | L0 | Obligacion.frecuencia | 'mensual y trimestral' | registrado_fuera_de_lista 1 |
| diez | L0 | Obligacion.frecuencia | 'según cálculo de capital' | registrado_fuera_de_lista 1 |
| diez | L0 | padre_sugerido | 'Sujeto_entidad_financiera' | sin_mencion_descartado 1 |
| diez | L0r | Comunicacion.tipo | '' | registrado_fuera_de_lista 1 |
| diez | L0r | Comunicacion.tipo | 'otro' | registrado_fuera_de_lista 2 |
| diez | L0r | Obligacion.frecuencia | 'en cada ciclo de clasificación' | registrado_fuera_de_lista 1 |

## 3. Claves, valores y campos del ítem

| grupo | capa | campo | clave o valor | tratamiento |
|---|---|---|---|---|
| r1 | L0 | claves | Obligacion.plazo | heredada_v3 302 |
| r1 | L0 | claves | Obligacion.plazo_o_frecuencia | a_properties_no_definidas 4 |
| r1 | L0 | claves | Obligacion.umbral | a_properties_no_definidas 1 |
| r1 | L0 | claves | Restriccion.umbral | heredada_v3 362 |
| r1 | L0 | claves | TextoOrdenado.descripcion | a_properties_no_definidas 4 |
| r1 | L0 | claves | TextoOrdenado.tipo | a_properties_no_definidas 1 |
| r1 | L0 | valores | Comunicacion.codigo | vacio_a_ausente 3 |
| r1 | L0 | valores | Comunicacion.numero | vacio_a_ausente 3 |
| r1 | L0 | valores | Comunicacion.tipo | vacio_a_ausente 2 |
| r1 | L0 | valores | TextoOrdenado.version | vacio_a_ausente 186 |
| r1 | L0 | campos_del_item_relacion | source | extremo_sujeto_ignorado 4 |
| r1 | L0 | campos_del_item_relacion | source_id | a_campos_no_definidos 1 |
| r1 | L0 | campos_del_item_relacion | target | extremo_sujeto_ignorado 8 |
| r1 | L0r | claves | Obligacion.modalidad_deonica | a_properties_no_definidas 1 |
| r1 | L0r | claves | Obligacion.plazo | heredada_v3 102 |
| r1 | L0r | claves | Obligacion.plazo_o_condicion | a_properties_no_definidas 1 |
| r1 | L0r | claves | Obligacion.plazo_o_frecuencia | a_properties_no_definidas 1 |
| r1 | L0r | claves | Restriccion.umbral | heredada_v3 102 |
| r1 | L0r | claves | TextoOrdenado.descripcion | a_properties_no_definidas 5 |
| r1 | L0r | claves | TextoOrdenado.referencia | a_properties_no_definidas 1 |
| r1 | L0r | valores | TextoOrdenado.version | vacio_a_ausente 41 |
| r1 | L0r | campos_del_item_relacion | source | extremo_sujeto_ignorado 4 |
| desarrollo | L0 | claves | Obligacion.plazo | heredada_v3 312 |
| desarrollo | L0 | claves | Obligacion.plazo_frecuencia | a_properties_no_definidas 1 |
| desarrollo | L0 | claves | Obligacion.plazo_o_frecuencia | a_properties_no_definidas 1 |
| desarrollo | L0 | claves | Obligacion.umbral | a_properties_no_definidas 1 |
| desarrollo | L0 | claves | Operacion.etapa | a_properties_no_definidas 1 |
| desarrollo | L0 | claves | Potestad.tipo | a_properties_no_definidas 1 |
| desarrollo | L0 | claves | Potestad.umbral | a_properties_no_definidas 1 |
| desarrollo | L0 | claves | Restriccion.umbral | heredada_v3 254 |
| desarrollo | L0 | valores | Obligacion.frecuencia | vacio_a_ausente 1 |
| desarrollo | L0 | valores | TextoOrdenado.version | vacio_a_ausente 175 |
| desarrollo | L0 | campos_del_item_relacion | source | extremo_sujeto_ignorado 10 |
| desarrollo | L0 | campos_del_item_relacion | source_id | a_campos_no_definidos 1 |
| desarrollo | L0 | campos_del_item_relacion | source_sujeto | a_campos_no_definidos 2 |
| desarrollo | L0 | campos_del_item_relacion | target | extremo_sujeto_ignorado 78 |
| desarrollo | L0r | claves | Obligacion.plazo | heredada_v3 46 |
| desarrollo | L0r | claves | Obligacion.plazo_o_frecuencia | a_properties_no_definidas 5 |
| desarrollo | L0r | claves | Restriccion.umbral | heredada_v3 45 |
| desarrollo | L0r | valores | Obligacion.frecuencia | vacio_a_ausente 1 |
| desarrollo | L0r | valores | TextoOrdenado.version | vacio_a_ausente 9 |
| desarrollo | L0r | campos_del_item_relacion | target | extremo_sujeto_ignorado 21 |
| cinco | L0 | claves | Obligacion.destinatario | a_properties_no_definidas 2 |
| cinco | L0 | claves | Obligacion.plazo | heredada_v3 147 |
| cinco | L0 | claves | Obligacion.plazo_frecuencia | a_properties_no_definidas 1 |
| cinco | L0 | claves | Obligacion.referencia_normativa | a_properties_no_definidas 1 |
| cinco | L0 | claves | Restriccion.umbral | heredada_v3 27 |
| cinco | L0 | valores | Comunicacion.codigo | vacio_a_ausente 1 |
| cinco | L0 | valores | TextoOrdenado.version | vacio_a_ausente 394 |
| cinco | L0 | campos_del_item_relacion | source | extremo_sujeto_ignorado 4 |
| cinco | L0 | campos_del_item_relacion | source_id | a_campos_no_definidos 3 |
| cinco | L0 | campos_del_item_relacion | target | extremo_sujeto_ignorado 12 |
| cinco | L0r | claves | Obligacion.plazo | heredada_v3 17 |
| cinco | L0r | claves | Restriccion.umbral | heredada_v3 1 |
| cinco | L0r | valores | Comunicacion.codigo | vacio_a_ausente 1 |
| cinco | L0r | valores | Comunicacion.numero | vacio_a_ausente 1 |
| cinco | L0r | valores | Comunicacion.tipo | vacio_a_ausente 1 |
| cinco | L0r | valores | TextoOrdenado.version | vacio_a_ausente 28 |
| cinco | L0r | campos_del_item_relacion | target | extremo_sujeto_ignorado 4 |
| diez | L0 | claves | Obligacion.destinatario | a_properties_no_definidas 2 |
| diez | L0 | claves | Obligacion.plazo | heredada_v3 459 |
| diez | L0 | claves | Obligacion.plazo_frecuencia | a_properties_no_definidas 2 |
| diez | L0 | claves | Obligacion.plazo_o_frecuencia | a_properties_no_definidas 1 |
| diez | L0 | claves | Obligacion.referencia_normativa | a_properties_no_definidas 1 |
| diez | L0 | claves | Obligacion.umbral | a_properties_no_definidas 1 |
| diez | L0 | claves | Operacion.etapa | a_properties_no_definidas 1 |
| diez | L0 | claves | Potestad.tipo | a_properties_no_definidas 1 |
| diez | L0 | claves | Potestad.umbral | a_properties_no_definidas 1 |
| diez | L0 | claves | Restriccion.umbral | heredada_v3 281 |
| diez | L0 | valores | Comunicacion.codigo | vacio_a_ausente 1 |
| diez | L0 | valores | Obligacion.frecuencia | vacio_a_ausente 1 |
| diez | L0 | valores | TextoOrdenado.version | vacio_a_ausente 569 |
| diez | L0 | campos_del_item_relacion | source | extremo_sujeto_ignorado 14 |
| diez | L0 | campos_del_item_relacion | source_id | a_campos_no_definidos 4 |
| diez | L0 | campos_del_item_relacion | source_sujeto | a_campos_no_definidos 2 |
| diez | L0 | campos_del_item_relacion | target | extremo_sujeto_ignorado 90 |
| diez | L0r | claves | Obligacion.plazo | heredada_v3 63 |
| diez | L0r | claves | Obligacion.plazo_o_frecuencia | a_properties_no_definidas 5 |
| diez | L0r | claves | Restriccion.umbral | heredada_v3 46 |
| diez | L0r | valores | Comunicacion.codigo | vacio_a_ausente 1 |
| diez | L0r | valores | Comunicacion.numero | vacio_a_ausente 1 |
| diez | L0r | valores | Comunicacion.tipo | vacio_a_ausente 1 |
| diez | L0r | valores | Obligacion.frecuencia | vacio_a_ausente 1 |
| diez | L0r | valores | TextoOrdenado.version | vacio_a_ausente 37 |
| diez | L0r | campos_del_item_relacion | target | extremo_sujeto_ignorado 25 |

## 4. Marcas: BKL-0038, mención, omisiones, matriz

| grupo | capa | coherencia tipo–predicado | mención | omisiones fuera_de_tipos | omisiones v3 leídas | recuperadas por la matriz (no verificadas E3) | pendientes no mapeados |
|---|---|---|---|---|---|---|---|
| r1 | L0 | limita:coherente 955, limita:incoherente 3, prohibe:coherente 180 | ausente 3443, exacta 46, no 5, tokens 5 | 0 | 136 | — | mencion_no_verificada 5 |
| r1 | L0r | limita:coherente 330, prohibe:coherente 62 | ausente 1166, exacta 18, no 7, tokens 2 | 0 | 37 | — | mencion_no_verificada 7 |
| desarrollo | L0 | limita:coherente 288, limita:incoherente 1, prohibe:coherente 95 | ausente 2943, exacta 33, no 10, tokens 1 | 0 | 156 | Operacion 383, Potestad 208 | mencion_no_verificada 9 |
| desarrollo | L0r | limita:coherente 37, limita:incoherente 3, prohibe:coherente 18 | ausente 464, exacta 3 | 0 | 16 | Operacion 72, Potestad 48 | — |
| cinco | L0 | limita:coherente 55, prohibe:coherente 63 | ausente 1003, exacta 11, no 3, tokens 2 | 2 | 6 | Operacion 41, Potestad 23 | mencion_no_verificada 3 |
| cinco | L0r | limita:coherente 1, prohibe:coherente 15 | ausente 81, exacta 3 | 0 | 3 | Operacion 9, Potestad 3 | — |
| diez | L0 | limita:coherente 343, limita:incoherente 1, prohibe:coherente 158 | ausente 3946, exacta 44, no 13, tokens 3 | 2 | 162 | Operacion 424, Potestad 231 | mencion_no_verificada 12 |
| diez | L0r | limita:coherente 38, limita:incoherente 3, prohibe:coherente 33 | ausente 545, exacta 6 | 0 | 19 | Operacion 81, Potestad 51 | — |

Relaciones con la marca `incoherente` (BKL-0038), grupos r1 y diez:

| grupo | capa | chunk | relación | Restriccion.tipo | predicado | label |
|---|---|---|---|---|---|---|
| r1 | L0 | cap::5.3.1.2 | 19 | prohibicion | limita | Solvencia sin correlación positiva riesgo crédito |
| r1 | L0 | cla::7.2.4 | 12 | prohibicion | limita | Concurso preventivo — riesgo alto |
| r1 | L0 | ric::11.1.4 | 12 | prohibicion | limita | Suma pérdidas — no admite signo negativo |
| diez | L0 | cap::6.2.1.4 | 14 | prohibicion | limita | Sin exigencia capital riesgo específico — compensación íntegra |
| diez | L0r | cap::4.3.3.1 | 44 | prohibicion | limita | No aplicar plazo mínimo 20 días MPOR conjuntos neteo |
| diez | L0r | ext::3.5.6.6 | 12 | prohibicion | limita | Endeudamientos no computables en otros mecanismos cambiarios |
| diez | L0r | ext::3.5.6.6 | 13 | prohibicion | limita | Endeudamientos no computables en otros mecanismos cambiarios |

## 5. Controles

### C1. Fuera de lista contra N1

| grupo|capa | registros N1 | registros | fuera = N1 | totales = resumen_por_lista | fuera por campo |
|---|---|---|---|---|---|
| r1|L0 | 1763 | 1763 | True | True | Comunicacion.tipo 14, Obligacion.tipo 2, Restriccion.tipo 0, claves 10, predicado 2, sujeto_id 0, tipo_entidad 0 |
| r1|L0r | 431 | 431 | True | True | Comunicacion.tipo 4, Obligacion.tipo 1, Restriccion.tipo 0, claves 9, predicado 2, sujeto_id 0, tipo_entidad 0 |
| desarrollo|L0 | 1763 | 1763 | True | True | Comunicacion.tipo 4, Obligacion.tipo 0, Restriccion.tipo 4, claves 6, predicado 1, sujeto_id 0, tipo_entidad 2 |
| desarrollo|L0r | 192 | 192 | True | True | Comunicacion.tipo 2, Obligacion.tipo 0, Restriccion.tipo 0, claves 5, predicado 0, sujeto_id 0, tipo_entidad 0 |
| cinco|L0 | 671 | 671 | True | True | Comunicacion.tipo 1, Obligacion.tipo 3, Restriccion.tipo 0, claves 4, predicado 1, sujeto_id 0, tipo_entidad 2 |
| cinco|L0r | 63 | 63 | True | True | Comunicacion.tipo 1, Obligacion.tipo 0, Restriccion.tipo 0, claves 0, predicado 0, sujeto_id 0, tipo_entidad 0 |
| diez|L0 | 2434 | 2434 | True | True | Comunicacion.tipo 5, Obligacion.tipo 3, Restriccion.tipo 4, claves 10, predicado 2, sujeto_id 0, tipo_entidad 4 |
| diez|L0r | 255 | 255 | True | True | Comunicacion.tipo 3, Obligacion.tipo 0, Restriccion.tipo 0, claves 5, predicado 0, sujeto_id 0, tipo_entidad 0 |

### Reconciliación valor por valor

`origen n1`: valor fuera de lista en N1 y su tratamiento r2 (`cierra` = la suma del tratamiento r2 es el conteo de N1). `origen solo_r2`: lo que r2 trata y N1 no contaba fuera de lista.

| grupo | capa | campo | valor | N1 | tratamiento r2 | cierra | origen |
|---|---|---|---|---|---|---|---|
| r1 | L0 | predicado | 'aplicaA' | 1 | normalizado_forma 1 | True | n1 |
| r1 | L0 | predicado | 'exceptua_restriccion' | 1 | normalizado_alias 1 | True | n1 |
| r1 | L0 | Obligacion.tipo | 'verificacion' | 1 | normalizado_a_otra 1 | True | n1 |
| r1 | L0 | Obligacion.tipo | 'verificacion_informativa' | 1 | normalizado_a_otra 1 | True | n1 |
| r1 | L0 | Comunicacion.tipo | '' | 2 | externa_por_codigo_o_label 1, registrado_fuera_de_lista 1 | True | n1 |
| r1 | L0 | Comunicacion.tipo | 'Decreto' | 1 | externa_por_valor 1 | True | n1 |
| r1 | L0 | Comunicacion.tipo | 'LEY' | 1 | externa_por_valor 1 | True | n1 |
| r1 | L0 | Comunicacion.tipo | 'MINISTERIAL' | 1 | externa_por_codigo_o_label 1 | True | n1 |
| r1 | L0 | Comunicacion.tipo | 'Resolución' | 1 | externa_por_valor 1 | True | n1 |
| r1 | L0 | Comunicacion.tipo | 'decreto' | 1 | externa_por_valor 1 | True | n1 |
| r1 | L0 | Comunicacion.tipo | 'interna' | 2 | registrado_fuera_de_lista 2 | True | n1 |
| r1 | L0 | Comunicacion.tipo | 'normas' | 1 | registrado_fuera_de_lista 1 | True | n1 |
| r1 | L0 | Comunicacion.tipo | 'referencia' | 1 | registrado_fuera_de_lista 1 | True | n1 |
| r1 | L0 | Comunicacion.tipo | 'referencia a normas' | 1 | registrado_fuera_de_lista 1 | True | n1 |
| r1 | L0 | Comunicacion.tipo | 'referencia_normativa' | 2 | registrado_fuera_de_lista 2 | True | n1 |
| r1 | L0 | claves | 'Obligacion.plazo_o_frecuencia' | 4 | a_properties_no_definidas 4 | True | n1 |
| r1 | L0 | claves | 'Obligacion.umbral' | 1 | a_properties_no_definidas 1 | True | n1 |
| r1 | L0 | claves | 'TextoOrdenado.descripcion' | 4 | a_properties_no_definidas 4 | True | n1 |
| r1 | L0 | claves | 'TextoOrdenado.tipo' | 1 | a_properties_no_definidas 1 | True | n1 |
| r1 | L0 | Obligacion.frecuencia | 'mensual y trimestral' | — | registrado_fuera_de_lista 1 | — | solo_r2 |
| r1 | L0 | Obligacion.frecuencia | 'mensualmente' | — | normalizado_desde_tramo 1 | — | solo_r2 |
| r1 | L0 | Obligacion.frecuencia | 'periodicidad mínima a indicarse' | — | registrado_fuera_de_lista 1 | — | solo_r2 |
| r1 | L0 | Obligacion.frecuencia | 'periódicamente' | — | registrado_fuera_de_lista 1 | — | solo_r2 |
| r1 | L0 | Obligacion.frecuencia | 'por operación' | — | registrado_fuera_de_lista 1 | — | solo_r2 |
| r1 | L0 | Obligacion.frecuencia | 'por período informativo' | — | registrado_fuera_de_lista 1 | — | solo_r2 |
| r1 | L0 | campos_del_item_relacion | 'source' | — | extremo_sujeto_ignorado 4 | — | solo_r2 |
| r1 | L0 | campos_del_item_relacion | 'source_id' | — | a_campos_no_definidos 1 | — | solo_r2 |
| r1 | L0 | campos_del_item_relacion | 'target' | — | extremo_sujeto_ignorado 8 | — | solo_r2 |
| r1 | L0 | claves | 'Obligacion.plazo' | — | heredada_v3 302 | — | solo_r2 |
| r1 | L0 | claves | 'Restriccion.umbral' | — | heredada_v3 362 | — | solo_r2 |
| r1 | L0 | coherencia_tipo_predicado | 'limite_cualitativo→limita' | — | limita:coherente 595 | — | solo_r2 |
| r1 | L0 | coherencia_tipo_predicado | 'limite_cuantitativo→limita' | — | limita:coherente 360 | — | solo_r2 |
| r1 | L0 | coherencia_tipo_predicado | 'prohibicion→limita' | — | limita:incoherente 3 | — | solo_r2 |
| r1 | L0 | coherencia_tipo_predicado | 'prohibicion→prohibe' | — | prohibe:coherente 180 | — | solo_r2 |
| r1 | L0 | padre_sugerido | 'Sujeto_acreedor_del_exterior' | — | fuera_de_catalogo_anulado 1 | — | solo_r2 |
| r1 | L0 | valores | 'Comunicacion.codigo' | — | vacio_a_ausente 3 | — | solo_r2 |
| r1 | L0 | valores | 'Comunicacion.numero' | — | vacio_a_ausente 3 | — | solo_r2 |
| r1 | L0 | valores | 'Comunicacion.tipo' | — | vacio_a_ausente 2 | — | solo_r2 |
| r1 | L0 | valores | 'TextoOrdenado.version' | — | vacio_a_ausente 186 | — | solo_r2 |
| r1 | L0r | predicado | 'estableci_en' | 1 | rechazado 1 | True | n1 |
| r1 | L0r | predicado | 'establecia_en' | 1 | rechazado 1 | True | n1 |
| r1 | L0r | Obligacion.tipo | 'verificacion' | 1 | normalizado_a_otra 1 | True | n1 |
| r1 | L0r | Comunicacion.tipo | 'norma' | 1 | externa_por_codigo_o_label 1 | True | n1 |
| r1 | L0r | Comunicacion.tipo | 'otro' | 1 | registrado_fuera_de_lista 1 | True | n1 |
| r1 | L0r | Comunicacion.tipo | 'referencia' | 1 | registrado_fuera_de_lista 1 | True | n1 |
| r1 | L0r | Comunicacion.tipo | 'referencia_interna' | 1 | registrado_fuera_de_lista 1 | True | n1 |
| r1 | L0r | claves | 'Obligacion.modalidad_deonica' | 1 | a_properties_no_definidas 1 | True | n1 |
| r1 | L0r | claves | 'Obligacion.plazo_o_condicion' | 1 | a_properties_no_definidas 1 | True | n1 |
| r1 | L0r | claves | 'Obligacion.plazo_o_frecuencia' | 1 | a_properties_no_definidas 1 | True | n1 |
| r1 | L0r | claves | 'TextoOrdenado.descripcion' | 5 | a_properties_no_definidas 5 | True | n1 |
| r1 | L0r | claves | 'TextoOrdenado.referencia' | 1 | a_properties_no_definidas 1 | True | n1 |
| r1 | L0r | campos_del_item_relacion | 'source' | — | extremo_sujeto_ignorado 4 | — | solo_r2 |
| r1 | L0r | claves | 'Obligacion.plazo' | — | heredada_v3 102 | — | solo_r2 |
| r1 | L0r | claves | 'Restriccion.umbral' | — | heredada_v3 102 | — | solo_r2 |
| r1 | L0r | coherencia_tipo_predicado | 'limite_cualitativo→limita' | — | limita:coherente 232 | — | solo_r2 |
| r1 | L0r | coherencia_tipo_predicado | 'limite_cuantitativo→limita' | — | limita:coherente 98 | — | solo_r2 |
| r1 | L0r | coherencia_tipo_predicado | 'prohibicion→prohibe' | — | prohibe:coherente 62 | — | solo_r2 |
| r1 | L0r | valores | 'TextoOrdenado.version' | — | vacio_a_ausente 41 | — | solo_r2 |
| desarrollo | L0 | tipo_entidad | 'Restriction' | 2 | normalizado_alias 2 | True | n1 |
| desarrollo | L0 | predicado | 'establec\nida_en' | 1 | normalizado_forma 1 | True | n1 |
| desarrollo | L0 | Restriccion.tipo | 'limite_temporal' | 3 | registrado_fuera_de_lista 3 | True | n1 |
| desarrollo | L0 | Restriccion.tipo | 'obligacion_cualitativa' | 1 | registrado_fuera_de_lista 1 | True | n1 |
| desarrollo | L0 | Comunicacion.tipo | 'TO' | 1 | registrado_fuera_de_lista 1 | True | n1 |
| desarrollo | L0 | Comunicacion.tipo | 'referencia' | 3 | registrado_fuera_de_lista 3 | True | n1 |
| desarrollo | L0 | claves | 'Obligacion.plazo_frecuencia' | 1 | a_properties_no_definidas 1 | True | n1 |
| desarrollo | L0 | claves | 'Obligacion.plazo_o_frecuencia' | 1 | a_properties_no_definidas 1 | True | n1 |
| desarrollo | L0 | claves | 'Obligacion.umbral' | 1 | a_properties_no_definidas 1 | True | n1 |
| desarrollo | L0 | claves | 'Operacion.etapa' | 1 | a_properties_no_definidas 1 | True | n1 |
| desarrollo | L0 | claves | 'Potestad.tipo' | 1 | a_properties_no_definidas 1 | True | n1 |
| desarrollo | L0 | claves | 'Potestad.umbral' | 1 | a_properties_no_definidas 1 | True | n1 |
| desarrollo | L0 | Obligacion.frecuencia | 'a cada requerimiento del usuario' | — | registrado_fuera_de_lista 1 | — | solo_r2 |
| desarrollo | L0 | Obligacion.frecuencia | 'cuando corresponda' | — | registrado_fuera_de_lista 1 | — | solo_r2 |
| desarrollo | L0 | Obligacion.frecuencia | 'mensual y trimestral' | — | registrado_fuera_de_lista 1 | — | solo_r2 |
| desarrollo | L0 | Obligacion.frecuencia | 'según cálculo de capital' | — | registrado_fuera_de_lista 1 | — | solo_r2 |
| desarrollo | L0 | campos_del_item_relacion | 'source' | — | extremo_sujeto_ignorado 10 | — | solo_r2 |
| desarrollo | L0 | campos_del_item_relacion | 'source_id' | — | a_campos_no_definidos 1 | — | solo_r2 |
| desarrollo | L0 | campos_del_item_relacion | 'source_sujeto' | — | a_campos_no_definidos 2 | — | solo_r2 |
| desarrollo | L0 | campos_del_item_relacion | 'target' | — | extremo_sujeto_ignorado 78 | — | solo_r2 |
| desarrollo | L0 | claves | 'Obligacion.plazo' | — | heredada_v3 312 | — | solo_r2 |
| desarrollo | L0 | claves | 'Restriccion.umbral' | — | heredada_v3 254 | — | solo_r2 |
| desarrollo | L0 | coherencia_tipo_predicado | 'limite_cualitativo→limita' | — | limita:coherente 76 | — | solo_r2 |
| desarrollo | L0 | coherencia_tipo_predicado | 'limite_cuantitativo→limita' | — | limita:coherente 209 | — | solo_r2 |
| desarrollo | L0 | coherencia_tipo_predicado | 'limite_temporal→limita' | — | limita:coherente 3 | — | solo_r2 |
| desarrollo | L0 | coherencia_tipo_predicado | 'prohibicion→limita' | — | limita:incoherente 1 | — | solo_r2 |
| desarrollo | L0 | coherencia_tipo_predicado | 'prohibicion→prohibe' | — | prohibe:coherente 95 | — | solo_r2 |
| desarrollo | L0 | padre_sugerido | 'Sujeto_entidad_financiera' | — | sin_mencion_descartado 1 | — | solo_r2 |
| desarrollo | L0 | valores | 'Obligacion.frecuencia' | — | vacio_a_ausente 1 | — | solo_r2 |
| desarrollo | L0 | valores | 'TextoOrdenado.version' | — | vacio_a_ausente 175 | — | solo_r2 |
| desarrollo | L0r | Comunicacion.tipo | 'otro' | 2 | registrado_fuera_de_lista 2 | True | n1 |
| desarrollo | L0r | claves | 'Obligacion.plazo_o_frecuencia' | 5 | a_properties_no_definidas 5 | True | n1 |
| desarrollo | L0r | Obligacion.frecuencia | 'en cada ciclo de clasificación' | — | registrado_fuera_de_lista 1 | — | solo_r2 |
| desarrollo | L0r | campos_del_item_relacion | 'target' | — | extremo_sujeto_ignorado 21 | — | solo_r2 |
| desarrollo | L0r | claves | 'Obligacion.plazo' | — | heredada_v3 46 | — | solo_r2 |
| desarrollo | L0r | claves | 'Restriccion.umbral' | — | heredada_v3 45 | — | solo_r2 |
| desarrollo | L0r | coherencia_tipo_predicado | 'limite_cualitativo→limita' | — | limita:coherente 6 | — | solo_r2 |
| desarrollo | L0r | coherencia_tipo_predicado | 'limite_cuantitativo→limita' | — | limita:coherente 31 | — | solo_r2 |
| desarrollo | L0r | coherencia_tipo_predicado | 'prohibicion→limita' | — | limita:incoherente 3 | — | solo_r2 |
| desarrollo | L0r | coherencia_tipo_predicado | 'prohibicion→prohibe' | — | prohibe:coherente 18 | — | solo_r2 |
| desarrollo | L0r | valores | 'Obligacion.frecuencia' | — | vacio_a_ausente 1 | — | solo_r2 |
| desarrollo | L0r | valores | 'TextoOrdenado.version' | — | vacio_a_ausente 9 | — | solo_r2 |
| cinco | L0 | tipo_entidad | 'Recomendacion' | 2 | rechazado 2 | True | n1 |
| cinco | L0 | predicado | 'establec ida_en' | 1 | normalizado_forma 1 | True | n1 |
| cinco | L0 | Obligacion.tipo | 'evaluacion' | 1 | normalizado_a_otra 1 | True | n1 |
| cinco | L0 | Obligacion.tipo | 'obtención_de_datos' | 1 | normalizado_a_otra 1 | True | n1 |
| cinco | L0 | Obligacion.tipo | 'pago' | 1 | normalizado_a_otra 1 | True | n1 |
| cinco | L0 | Comunicacion.tipo | 'Resolución' | 1 | externa_por_valor 1 | True | n1 |
| cinco | L0 | claves | 'Obligacion.destinatario' | 2 | a_properties_no_definidas 2 | True | n1 |
| cinco | L0 | claves | 'Obligacion.plazo_frecuencia' | 1 | a_properties_no_definidas 1 | True | n1 |
| cinco | L0 | claves | 'Obligacion.referencia_normativa' | 1 | a_properties_no_definidas 1 | True | n1 |
| cinco | L0 | campos_del_item_relacion | 'source' | — | extremo_sujeto_ignorado 4 | — | solo_r2 |
| cinco | L0 | campos_del_item_relacion | 'source_id' | — | a_campos_no_definidos 3 | — | solo_r2 |
| cinco | L0 | campos_del_item_relacion | 'target' | — | extremo_sujeto_ignorado 12 | — | solo_r2 |
| cinco | L0 | claves | 'Obligacion.plazo' | — | heredada_v3 147 | — | solo_r2 |
| cinco | L0 | claves | 'Restriccion.umbral' | — | heredada_v3 27 | — | solo_r2 |
| cinco | L0 | coherencia_tipo_predicado | 'limite_cualitativo→limita' | — | limita:coherente 26 | — | solo_r2 |
| cinco | L0 | coherencia_tipo_predicado | 'limite_cuantitativo→limita' | — | limita:coherente 29 | — | solo_r2 |
| cinco | L0 | coherencia_tipo_predicado | 'prohibicion→prohibe' | — | prohibe:coherente 63 | — | solo_r2 |
| cinco | L0 | valores | 'Comunicacion.codigo' | — | vacio_a_ausente 1 | — | solo_r2 |
| cinco | L0 | valores | 'TextoOrdenado.version' | — | vacio_a_ausente 394 | — | solo_r2 |
| cinco | L0r | Comunicacion.tipo | '' | 1 | registrado_fuera_de_lista 1 | True | n1 |
| cinco | L0r | campos_del_item_relacion | 'target' | — | extremo_sujeto_ignorado 4 | — | solo_r2 |
| cinco | L0r | claves | 'Obligacion.plazo' | — | heredada_v3 17 | — | solo_r2 |
| cinco | L0r | claves | 'Restriccion.umbral' | — | heredada_v3 1 | — | solo_r2 |
| cinco | L0r | coherencia_tipo_predicado | 'limite_cuantitativo→limita' | — | limita:coherente 1 | — | solo_r2 |
| cinco | L0r | coherencia_tipo_predicado | 'prohibicion→prohibe' | — | prohibe:coherente 15 | — | solo_r2 |
| cinco | L0r | valores | 'Comunicacion.codigo' | — | vacio_a_ausente 1 | — | solo_r2 |
| cinco | L0r | valores | 'Comunicacion.numero' | — | vacio_a_ausente 1 | — | solo_r2 |
| cinco | L0r | valores | 'Comunicacion.tipo' | — | vacio_a_ausente 1 | — | solo_r2 |
| cinco | L0r | valores | 'TextoOrdenado.version' | — | vacio_a_ausente 28 | — | solo_r2 |
| diez | L0 | tipo_entidad | 'Recomendacion' | 2 | rechazado 2 | True | n1 |
| diez | L0 | tipo_entidad | 'Restriction' | 2 | normalizado_alias 2 | True | n1 |
| diez | L0 | predicado | 'establec\nida_en' | 1 | normalizado_forma 1 | True | n1 |
| diez | L0 | predicado | 'establec ida_en' | 1 | normalizado_forma 1 | True | n1 |
| diez | L0 | Obligacion.tipo | 'evaluacion' | 1 | normalizado_a_otra 1 | True | n1 |
| diez | L0 | Obligacion.tipo | 'obtención_de_datos' | 1 | normalizado_a_otra 1 | True | n1 |
| diez | L0 | Obligacion.tipo | 'pago' | 1 | normalizado_a_otra 1 | True | n1 |
| diez | L0 | Restriccion.tipo | 'limite_temporal' | 3 | registrado_fuera_de_lista 3 | True | n1 |
| diez | L0 | Restriccion.tipo | 'obligacion_cualitativa' | 1 | registrado_fuera_de_lista 1 | True | n1 |
| diez | L0 | Comunicacion.tipo | 'Resolución' | 1 | externa_por_valor 1 | True | n1 |
| diez | L0 | Comunicacion.tipo | 'TO' | 1 | registrado_fuera_de_lista 1 | True | n1 |
| diez | L0 | Comunicacion.tipo | 'referencia' | 3 | registrado_fuera_de_lista 3 | True | n1 |
| diez | L0 | claves | 'Obligacion.destinatario' | 2 | a_properties_no_definidas 2 | True | n1 |
| diez | L0 | claves | 'Obligacion.plazo_frecuencia' | 2 | a_properties_no_definidas 2 | True | n1 |
| diez | L0 | claves | 'Obligacion.plazo_o_frecuencia' | 1 | a_properties_no_definidas 1 | True | n1 |
| diez | L0 | claves | 'Obligacion.referencia_normativa' | 1 | a_properties_no_definidas 1 | True | n1 |
| diez | L0 | claves | 'Obligacion.umbral' | 1 | a_properties_no_definidas 1 | True | n1 |
| diez | L0 | claves | 'Operacion.etapa' | 1 | a_properties_no_definidas 1 | True | n1 |
| diez | L0 | claves | 'Potestad.tipo' | 1 | a_properties_no_definidas 1 | True | n1 |
| diez | L0 | claves | 'Potestad.umbral' | 1 | a_properties_no_definidas 1 | True | n1 |
| diez | L0 | Obligacion.frecuencia | 'a cada requerimiento del usuario' | — | registrado_fuera_de_lista 1 | — | solo_r2 |
| diez | L0 | Obligacion.frecuencia | 'cuando corresponda' | — | registrado_fuera_de_lista 1 | — | solo_r2 |
| diez | L0 | Obligacion.frecuencia | 'mensual y trimestral' | — | registrado_fuera_de_lista 1 | — | solo_r2 |
| diez | L0 | Obligacion.frecuencia | 'según cálculo de capital' | — | registrado_fuera_de_lista 1 | — | solo_r2 |
| diez | L0 | campos_del_item_relacion | 'source' | — | extremo_sujeto_ignorado 14 | — | solo_r2 |
| diez | L0 | campos_del_item_relacion | 'source_id' | — | a_campos_no_definidos 4 | — | solo_r2 |
| diez | L0 | campos_del_item_relacion | 'source_sujeto' | — | a_campos_no_definidos 2 | — | solo_r2 |
| diez | L0 | campos_del_item_relacion | 'target' | — | extremo_sujeto_ignorado 90 | — | solo_r2 |
| diez | L0 | claves | 'Obligacion.plazo' | — | heredada_v3 459 | — | solo_r2 |
| diez | L0 | claves | 'Restriccion.umbral' | — | heredada_v3 281 | — | solo_r2 |
| diez | L0 | coherencia_tipo_predicado | 'limite_cualitativo→limita' | — | limita:coherente 102 | — | solo_r2 |
| diez | L0 | coherencia_tipo_predicado | 'limite_cuantitativo→limita' | — | limita:coherente 238 | — | solo_r2 |
| diez | L0 | coherencia_tipo_predicado | 'limite_temporal→limita' | — | limita:coherente 3 | — | solo_r2 |
| diez | L0 | coherencia_tipo_predicado | 'prohibicion→limita' | — | limita:incoherente 1 | — | solo_r2 |
| diez | L0 | coherencia_tipo_predicado | 'prohibicion→prohibe' | — | prohibe:coherente 158 | — | solo_r2 |
| diez | L0 | padre_sugerido | 'Sujeto_entidad_financiera' | — | sin_mencion_descartado 1 | — | solo_r2 |
| diez | L0 | valores | 'Comunicacion.codigo' | — | vacio_a_ausente 1 | — | solo_r2 |
| diez | L0 | valores | 'Obligacion.frecuencia' | — | vacio_a_ausente 1 | — | solo_r2 |
| diez | L0 | valores | 'TextoOrdenado.version' | — | vacio_a_ausente 569 | — | solo_r2 |
| diez | L0r | Comunicacion.tipo | '' | 1 | registrado_fuera_de_lista 1 | True | n1 |
| diez | L0r | Comunicacion.tipo | 'otro' | 2 | registrado_fuera_de_lista 2 | True | n1 |
| diez | L0r | claves | 'Obligacion.plazo_o_frecuencia' | 5 | a_properties_no_definidas 5 | True | n1 |
| diez | L0r | Obligacion.frecuencia | 'en cada ciclo de clasificación' | — | registrado_fuera_de_lista 1 | — | solo_r2 |
| diez | L0r | campos_del_item_relacion | 'target' | — | extremo_sujeto_ignorado 25 | — | solo_r2 |
| diez | L0r | claves | 'Obligacion.plazo' | — | heredada_v3 63 | — | solo_r2 |
| diez | L0r | claves | 'Restriccion.umbral' | — | heredada_v3 46 | — | solo_r2 |
| diez | L0r | coherencia_tipo_predicado | 'limite_cualitativo→limita' | — | limita:coherente 6 | — | solo_r2 |
| diez | L0r | coherencia_tipo_predicado | 'limite_cuantitativo→limita' | — | limita:coherente 32 | — | solo_r2 |
| diez | L0r | coherencia_tipo_predicado | 'prohibicion→limita' | — | limita:incoherente 3 | — | solo_r2 |
| diez | L0r | coherencia_tipo_predicado | 'prohibicion→prohibe' | — | prohibe:coherente 33 | — | solo_r2 |
| diez | L0r | valores | 'Comunicacion.codigo' | — | vacio_a_ausente 1 | — | solo_r2 |
| diez | L0r | valores | 'Comunicacion.numero' | — | vacio_a_ausente 1 | — | solo_r2 |
| diez | L0r | valores | 'Comunicacion.tipo' | — | vacio_a_ausente 1 | — | solo_r2 |
| diez | L0r | valores | 'Obligacion.frecuencia' | — | vacio_a_ausente 1 | — | solo_r2 |
| diez | L0r | valores | 'TextoOrdenado.version' | — | vacio_a_ausente 37 | — | solo_r2 |

### C2. Relaciones recuperadas por la matriz ampliada

Filas P01 y P02 presentes en el reporte de U-ESTUDIO-MATRIZ: True.

| grupo | → | r2 (L0) | U-ESTUDIO-MATRIZ, columna A | coincide |
|---|---|---|---|---|
| diez | Operacion | 424 | 424 | True |
| diez | Potestad | 231 | 231 | True |
| desarrollo | Operacion | 383 | 383 | True |
| desarrollo | Potestad | 208 | 208 | True |
| cinco | Operacion | 41 | 41 | True |
| cinco | Potestad | 23 | 23 | True |

Fuentes de la población final: cache_reintentos 220, e1_compact_last_wins 71, e1_last_wins 2143.

| grupo | → | A | − L0 de las reintentadas | + L0r de las reintentadas | B calculada | B (tablero [c19]) | coincide | unidades con delta |
|---|---|---|---|---|---|---|---|---|
| diez | Operacion | 424 | 62 | 72 | 434 | 434 | True | 54 |
| diez | Potestad | 231 | 13 | 45 | 263 | 263 | True | 32 |
| desarrollo | Operacion | 383 | 58 | 63 | 388 | 388 | True | 47 |
| desarrollo | Potestad | 208 | 12 | 43 | 239 | 239 | True | 31 |

Unidades aceptadas tras reintento con delta distinto de cero:

| TO | chunk | →Op L0 | →Op L0r | Δ Op | →Pot L0 | →Pot L0r | Δ Pot |
|---|---|---|---|---|---|---|---|
| cap | cap::2.8.2 | 0 | 0 | 0 | 1 | 0 | -1 |
| cap | cap::3.1.2.2 | 5 | 0 | -5 | 0 | 5 | 5 |
| cap | cap::4.3.3.1 | 0 | 0 | 0 | 4 | 1 | -3 |
| cla | cla::2.2.4::intro | 1 | 0 | -1 | 0 | 0 | 0 |
| cla | cla::6.5.4.5 | 0 | 2 | 2 | 1 | 0 | -1 |
| cla | cla::6.5.5.9 | 0 | 1 | 1 | 0 | 0 | 0 |
| ctacte | ctacte::1.5.4.3 | 0 | 1 | 1 | 0 | 0 | 0 |
| ctacte | ctacte::5.1.3 | 0 | 1 | 1 | 0 | 0 | 0 |
| ctacte | ctacte::6.2.5 | 1 | 0 | -1 | 0 | 0 | 0 |
| ctacte | ctacte::8.2.1.1 | 0 | 2 | 2 | 0 | 0 | 0 |
| docvig | docvig::1.2.1 | 0 | 2 | 2 | 0 | 0 | 0 |
| docvig | docvig::3.1.4 | 1 | 2 | 1 | 0 | 0 | 0 |
| ext | ext::11.1.3::intro | 1 | 0 | -1 | 0 | 0 | 0 |
| ext | ext::13.3.6 | 0 | 1 | 1 | 0 | 0 | 0 |
| ext | ext::13.3.9 | 0 | 0 | 0 | 0 | 2 | 2 |
| ext | ext::13.6 | 1 | 2 | 1 | 0 | 0 | 0 |
| ext | ext::14.2.1.10 | 0 | 2 | 2 | 1 | 0 | -1 |
| ext | ext::14.2.1.2 | 0 | 0 | 0 | 0 | 2 | 2 |
| ext | ext::14.2.1.3 | 0 | 1 | 1 | 0 | 1 | 1 |
| ext | ext::14.2.1.4 | 0 | 0 | 0 | 0 | 2 | 2 |
| ext | ext::14.2.1.5 | 2 | 0 | -2 | 0 | 3 | 3 |
| ext | ext::14.2.1.6 | 0 | 0 | 0 | 0 | 1 | 1 |
| ext | ext::14.2.1::cierre | 0 | 0 | 0 | 1 | 2 | 1 |
| ext | ext::14.2.1::intro | 0 | 0 | 0 | 0 | 1 | 1 |
| ext | ext::14.5.3 | 3 | 2 | -1 | 0 | 0 | 0 |
| ext | ext::2.6.2.1 | 0 | 2 | 2 | 0 | 0 | 0 |
| ext | ext::2.9 | 0 | 0 | 0 | 0 | 1 | 1 |
| ext | ext::3.11.1.1 | 4 | 0 | -4 | 0 | 2 | 2 |
| ext | ext::3.11.1.2 | 0 | 0 | 0 | 0 | 1 | 1 |
| ext | ext::3.11.1.5 | 0 | 0 | 0 | 0 | 1 | 1 |
| ext | ext::3.11.1::intro | 0 | 0 | 0 | 0 | 1 | 1 |
| ext | ext::3.11.2.1 | 0 | 0 | 0 | 0 | 1 | 1 |
| ext | ext::3.11.3.1 | 1 | 0 | -1 | 0 | 2 | 2 |
| ext | ext::3.11.3.2 | 0 | 0 | 0 | 0 | 2 | 2 |
| ext | ext::3.14.5.5 | 1 | 2 | 1 | 0 | 0 | 0 |
| ext | ext::3.17.1.3 | 0 | 1 | 1 | 0 | 0 | 0 |
| ext | ext::3.17.3.4 | 0 | 0 | 0 | 0 | 1 | 1 |
| ext | ext::3.18.2.3 | 0 | 1 | 1 | 0 | 0 | 0 |
| ext | ext::3.3.3.3 | 1 | 0 | -1 | 0 | 0 | 0 |
| ext | ext::3.3.3.4 | 2 | 0 | -2 | 0 | 0 | 0 |
| ext | ext::3.4.4.4 | 2 | 0 | -2 | 0 | 0 | 0 |
| ext | ext::3.4.4.7 | 1 | 3 | 2 | 0 | 0 | 0 |
| ext | ext::3.5.3.4 | 2 | 0 | -2 | 0 | 0 | 0 |
| ext | ext::3.5.6.6 | 2 | 0 | -2 | 0 | 0 | 0 |
| ext | ext::3.5.6.9 | 1 | 0 | -1 | 0 | 0 | 0 |
| ext | ext::3.6.1.4 | 0 | 0 | 0 | 1 | 0 | -1 |
| ext | ext::4.4.2 | 0 | 1 | 1 | 0 | 0 | 0 |
| ext | ext::4.4.5 | 0 | 1 | 1 | 0 | 0 | 0 |
| ext | ext::4.7.3 | 0 | 1 | 1 | 0 | 0 | 0 |
| ext | ext::4.7.4.1 | 1 | 0 | -1 | 0 | 0 | 0 |
| ext | ext::4.7::intro | 1 | 3 | 2 | 0 | 0 | 0 |
| ext | ext::4.8.1.3 | 1 | 0 | -1 | 0 | 1 | 1 |
| ext | ext::4.8.1.5 | 1 | 1 | 0 | 0 | 1 | 1 |
| ext | ext::4.8.1::cierre | 1 | 0 | -1 | 0 | 1 | 1 |
| ext | ext::4.8.4.1 | 0 | 1 | 1 | 0 | 0 | 0 |
| ext | ext::4.8.4.2 | 1 | 3 | 2 | 0 | 0 | 0 |
| ext | ext::4.8.4.3 | 0 | 2 | 2 | 0 | 0 | 0 |
| ext | ext::7.1.1.3 | 0 | 2 | 2 | 0 | 0 | 0 |
| ext | ext::7.10.1.1 | 0 | 1 | 1 | 0 | 1 | 1 |
| ext | ext::7.11.1.1 | 0 | 0 | 0 | 0 | 1 | 1 |
| ext | ext::7.11.1.6 | 4 | 0 | -4 | 0 | 0 | 0 |
| ext | ext::7.3.11 | 0 | 0 | 0 | 0 | 3 | 3 |
| ext | ext::7.8.4.2 | 1 | 0 | -1 | 0 | 0 | 0 |
| ext | ext::7.9.1.10 | 2 | 3 | 1 | 0 | 0 | 0 |
| ext | ext::7.9.1.11 | 1 | 3 | 2 | 0 | 0 | 0 |
| ext | ext::7.9.2.1 | 2 | 0 | -2 | 0 | 0 | 0 |
| ext | ext::8.5.13.1 | 0 | 1 | 1 | 0 | 0 | 0 |
| ext | ext::8.5.13.2 | 0 | 1 | 1 | 0 | 0 | 0 |
| ext | ext::8.5.19::intro | 0 | 0 | 0 | 1 | 2 | 1 |
| ext | ext::8.5.20.2 | 0 | 1 | 1 | 0 | 0 | 0 |
| ext | ext::9.3.7 | 0 | 3 | 3 | 0 | 0 | 0 |
| pagjub | pagjub::2.6 | 2 | 1 | -1 | 0 | 1 | 1 |
| pro | pro::2.3.1.1 | 0 | 0 | 0 | 1 | 0 | -1 |
| pro | pro::2.3.4 | 0 | 1 | 1 | 0 | 0 | 0 |
| pro | pro::4.2.1.6 | 0 | 2 | 2 | 0 | 0 | 0 |

### C4. BKL-0038: población final contra el grafo ensamblado

| grupo | población final (r2) | grafo | coincide | chunks del grafo |
|---|---|---|---|---|
| desarrollo | 4 | 4 | True | cap::4.3.3.1, cap::6.2.1.4, ext::3.5.6.6, ext::3.5.6.6 |
| diez | 4 | 4 | True | cap::4.3.3.1, cap::6.2.1.4, ext::3.5.6.6, ext::3.5.6.6 |

### C3. Ningún elemento aceptado por v3 se pierde

| grupo|capa | perdidos | ganados (motivo del rechazo v3) | omisiones v3 | omisiones r2 desde v3 | v3 re-corrido = guardado (L0) |
|---|---|---|---|---|---|
| r1|L0 | 0 | relacion:firma_invalida 196, relacion:predicado_invalido 2 | 136 | 136 | igual 1763 |
| r1|L0r | 0 | relacion:firma_invalida 131, relacion:sujeto_extremo_invalido 4 | 36 | 37 | — |
| desarrollo|L0 | 0 | entidad:type_invalido 2, relacion:firma_invalida 591, relacion:padre_sugerido_sin_propuesto 1, relacion:predicado_invalido 1, relacion:ref_colgante 6, relacion:sujeto_extremo_invalido 1 | 156 | 156 | igual 1763 |
| desarrollo|L0r | 0 | relacion:firma_invalida 120 | 16 | 16 | — |
| cinco|L0 | 0 | relacion:firma_invalida 64, relacion:predicado_invalido 1 | 6 | 6 | igual 671 |
| cinco|L0r | 0 | relacion:firma_invalida 12 | 3 | 3 | — |
| diez|L0 | 0 | entidad:type_invalido 2, relacion:firma_invalida 655, relacion:padre_sugerido_sin_propuesto 1, relacion:predicado_invalido 2, relacion:ref_colgante 6, relacion:sujeto_extremo_invalido 1 | 162 | 162 | igual 2434 |
| diez|L0r | 0 | relacion:firma_invalida 132 | 19 | 19 | — |

