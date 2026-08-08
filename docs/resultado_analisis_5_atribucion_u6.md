# Resultado — Análisis de los 5 casos con atribución de fuente (U6)

Resultado del análisis pre-registrado en
`docs/preregistro_analisis_5_atribucion_u6.md` (sellado en commit d0bf8bf,
adjudicación humana y predicción previas a toda corrida). Corrida: verificador
v5.7 congelado, N=1 por caso, condición `n_seen = 0`, síntoma con atribución
de fuente prependido fuera del módulo sellado, 5 casos (U6-001, U6-003,
U6-010, U6-011, U6-019), label `analisis_5_atribucion` (db homónima).

## 1. Resultado y lectura laudada

- **Acuerdo de capa: 1/5** (lectura estricta, oficial por el laudo de
  `docs/resultado_piloto_singold_u6.md` §1) y **2/5** bajo la lectura de
  sensibilidad.
- **Acuerdo de causa fina: 1/5** (estricta) y **2/5** (sensibilidad).

Bajo la operacionalización pre-registrada (≤ 2/5 → sin señal), el resultado
es **SIN SEÑAL bajo ambas lecturas**. Mi predicción sellada — que el síntoma
más informativo mejoraría el acuerdo respecto del piloto — **no fue
soportada**. Reitero lo pre-registrado: ningún resultado con n=5 valida ni
invalida nada; este análisis es descriptivo y la rama laudada del piloto
(Motor 3 no validado, adjudicación manual permanente) queda intacta.

Tabla completa de la corrida (verbatim del reporte de corrida; la
adjudicación humana es la sellada en el §2 del pre-registro, previa a toda
corrida):

```
qid | verificador (primarias) | humana prim/sec | capa_estricta | capa_incluye | causa_todas | causa_alguna
U6-001 | navegación (secundaria: aplicacion_erronea) | completitud_kg/alucinacion_agente | no | no | no | no
U6-003 | navegación (secundaria: aplicacion_erronea) | navegación/completitud_kg | SÍ | SÍ | SÍ | SÍ
U6-010 | aplicacion_erronea (secundaria: provenance_imprecisa) | contenido_kg/alucinacion_agente | no | no | no | no
U6-011 | navegación (secundaria: frontera_no_determinada) [formato_invalido] | contenido_kg/aplicacion_erronea | no | no | no | no
U6-019 | completitud_kg + aplicacion_erronea (sin_par: sin_defecto) | completitud_kg/contenido_kg | no | SÍ | no | SÍ
TOTALES: capa estricta 1/5 · capa incluye 2/5 · causa todas 1/5 · causa alguna 2/5
```

## 2. Hallazgo transversal — la frontera KG↔agente se sostiene entre cohortes

El patrón direccional del piloto se repite bajo síntoma con atribución de
fuente: en **4/5 casos** (U6-001, U6-010, U6-011 y U6-019, este último con
primarias mixtas) el verificador atribuyó capa agente
(navegación/aplicacion_erronea) donde mi adjudicación sellada es de capa KG.
La divergencia en la frontera KG↔agente se sostiene en ambas cohortes de
síntoma — puro (piloto, 4/13 estricta) e informado con atribución de fuente
(este análisis, 1/5 estricta): es un rasgo del adjudicador automático, no un
efecto de la informatividad del síntoma. Esto es contexto descriptivo entre
dos cohortes chicas, sin inferencia alguna.

## 3. Incidente U6-011 — formato_invalido en la secundaria

La atribución secundaria de U6-011 salió con `formato_invalido`: el camino
noise_sensitivity → frontera_no_determinada no está permitido por el árbol de
decisión de la taxonomía (desde noise_sensitivity el árbol permite
aplicacion_erronea, contenido_kg, provenance_imprecisa o sin_defecto). La
primaria (navegación) es válida y computa en la tabla del §1. Lo registro
como **segunda observación de calibración del verificador**, junto a los dos
`sin_defecto` del piloto (U6-008 y U6-024,
`docs/resultado_piloto_singold_u6.md` §4), sin cambio en v5.7 (congelada).

## 4. Evidencia de investigación activa

Los 5 casos tuvieron entre 10 y 15 tool calls del verificador (mediana 11),
con uso de `leer_pasaje_pdf` en 5/5 casos y de `ver_paso_completo` en 4/5:
el desacuerdo del §1 no se explica por diagnóstico sin evidencia.

Desglose por caso (del reporte de corrida, verbatim; se reproduce desde las
salidas crudas y el resumen por caso persistidos bajo el label
`analisis_5_atribucion`):

```
qid | n_tools | ver_paso_completo | leer_pasaje_pdf | buscar_nodos | ver_nodo | ver_vecinos
U6-001 | 15 | 3 | 3 | 3 | 6 | 0
U6-003 | 10 | 2 | 4 | 1 | 3 | 0
U6-010 | 11 | 2 | 7 | 0 | 2 | 0
U6-011 | 13 | 2 | 5 | 3 | 2 | 1
U6-019 | 11 | 0 | 5 | 5 | 1 | 0
```

El único caso sin `ver_paso_completo` es U6-019, que compensó con 5 llamadas
a `buscar_nodos` y 5 a `leer_pasaje_pdf`.

## 5. Consumo

Consumo real de la corrida: **USD 7,11**, contra una estimación previa de
USD 7,03 (≈ 5/13 del costo del piloto, según la referencia del §4 del
pre-registro). En tokens: 1.158.484 de entrada (40,1% del remanente del tope
laudado: 2.888.420 = 6M − 3.111.580 consumidos por el piloto) y 52.532 de
salida (57,6% del remanente: 91.186 = 200K − 108.814), según el log de
corrida persistido con el label `analisis_5_atribucion`. El freno por
proyección contra el tope, previsto en el driver, nunca se activó.

## 6. Cierre del capítulo (issue #1)

Con este análisis, el issue #1 queda completo en sus tres piezas:

1. **Piloto sin-gold** (13 casos síntoma-puro): Motor 3 NO validado — acuerdo
   de capa 4/13 contra umbral pre-registrado 11/13; adjudicación manual
   permanente (`docs/resultado_piloto_singold_u6.md`, label
   `singold_piloto_u6`).
2. **N=3 de RT-C6-1**: inversión de generación sistemática, 3/3 incorrecta;
   asentada en BKL-0026 (labels `rt_c6_n3_r{1,2,3}`).
3. **Análisis de la cohorte con atribución de fuente** (este documento): sin
   señal bajo ambas lecturas; la informatividad del síntoma no movió el
   acuerdo (label `analisis_5_atribucion`).

Toda la evidencia de este análisis se reproduce desde las salidas crudas,
el resumen por caso y el log de corrida persistidos bajo el label
`analisis_5_atribucion` y su db homónima.
