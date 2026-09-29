# Observación (12) — fila para el reporte de la tanda 0

Formato: enmienda al pre-registro de la tanda 0 `8e13be3`, §2.1 («Cómo se
reporta») y §2.3 (paso 4bis): una fila sin predicción numérica, con la tasa
cruda, el intervalo de Wilson, la lista de incorrectas con su `capa_pipeline`
y la de no decidibles. Escrita el 29/09/2026 desde los artefactos sellados.

## Fuentes

- Muestra: `reports/tanda0/obs12_sorteo/muestra_obs12.md` (sha256
  `247beeac…`) y `muestra_obs12.json`, sellados en `e6a3169`. Ensamblado de la
  tanda 0 sola: `data/experiment/reextraccion_v2/corpus_tanda0/ens_cinco/r1/kg.json`
  (sha256 `4097d4fd…`). Universo n = 3.345 (3.983 aristas − 521 `referencia`
  − 117 de esqueleto), k = 30, semilla 20260927.
- Veredictos de la autora: `reports/tanda0/obs12_lectura/veredictos_obs12.csv`
  (sha256 `c11ebeab…`), sellados en `f51bb1f`, antes de este reporte.
- El sha anotado en `sha256_muestra_anotada.txt` es `247beeac…`, igual al de
  `git show e6a3169:reports/tanda0/obs12_sorteo/muestra_obs12.md | shasum -a 256`
  y al del archivo en el árbol (verificado el 29/09/2026).
- El campo `orden` del CSV es el número de sección de la muestra («## n ·
  índice i»); las 30 secciones coinciden en orden, índice y relación con
  `muestra_obs12.json#aristas`.

## Fila

| Observación | Predicción | Observado | Veredicto |
|---|---|---|---|
| (12) Aristas de extracción correctas contra el texto (A4.4), ensamblado de la tanda 0 sola | SIN LÍNEA DE BASE | **25 correctas de 30**; no decidibles: 0 (se cuentan aparte y no salen del denominador); intervalo de Wilson al 95 % sobre 25 / 30: **0,664–0,927**; 5 incorrectas: 4 `E1-prompt` y 1 `catálogo` | Sin veredicto: sin umbral ni banda (decisión 6) |

Desglose por relación, informativo (fracciones crudas sobre n chico): `establecida_en`
18 de 21, `aplica_a` 5 de 7, `regula` 2 de 2. La muestra no contiene ninguna
arista `condicion_de`.

## Incorrectas

| Orden | Índice del sorteo | Origen | Relación | Destino | Chunk | capa_pipeline | Nota de la autora (textual) | Backlog |
|---|---|---|---|---|---|---|---|---|
| 6 | 437 | `Excepcion_la_obligacion_no_aplicara_cuando_se_trate_de_modificaciones_en_el_numero_de_docu_bf163e` (Excepcion, «Constancias obligatorias — modificación número documento») | `establecida_en` | `TextoOrdenado_docvig_pdf` (TextoOrdenado) | `docvig::3.3::cierre` | `E1-prompt` | Inversion de polaridad: el texto dice que la entrega de las constancias NO es obligatoria EXCEPTO cuando se trate de modificaciones en el numero de documento, y la excepcion extraida afirma lo contrario, que la obligacion no aplica en ese caso. | `BKL-0032` |
| 16 | 1438 | `Obligacion_la_informacion_referida_a_estos_documentos_sera_dada_de_baja_cuando_la_entidad_f_85d60d` (Obligacion, «Dar de baja información de documentos según presentación al cobro») | `aplica_a` | `Sujeto_banco` (Sujeto) | `ctacte::7.3.1.5` | `E1-prompt` | El punto obliga al banco a INFORMAR al BCRA; la baja de la informacion en la Central esta en voz pasiva («sera dada de baja cuando la entidad financiera interviniente haya informado») y no es acto del banco, por lo que la obligacion extraida no le aplica; duda con catalogo y se imputa la etapa mas temprana. | `BKL-0033` |
| 20 | 1992 | `Obligacion_se_asegurara_de_que_la_alta_gerencia_implemente_procedimientos_para_promover_con_1b8439` (Obligacion, «Alta Gerencia implementar procedimientos conducta profesional») | `aplica_a` | `Sujeto_entidad_financiera` (Sujeto) | `lingob::2.3.2::intro` | `catálogo` | El obligado del punto es el Directorio (Seccion 2 y «A esos efectos, el Directorio:» del intro de 2.3), no la entidad como clase; lingob separa Directorio, Alta Gerencia y Comite de auditoria y colapsarlos pierde el destinatario. Si el catalogo no ofrece un sujeto de nivel organo, el defecto es de cobertura del catalogo: misma capa. | `BKL-0034` |
| 21 | 2027 | `Obligacion_se_demostrara_con_cualquiera_de_las_siguientes_alternativas_05c68a` (Obligacion, «Demostración de cancelación — alternativas») | `establecida_en` | `TextoOrdenado_ctacte_pdf` (TextoOrdenado) | `ctacte::8.3::intro` (provenances: `ctacte::8.3::intro`, `ctacte::8.4::intro`) | `E1-prompt` | La «obligacion» es el pie de lista «Se demostrara con cualquiera de las siguientes alternativas:», sin contenido normativo, y quedo anclada a dos puntos distintos (8.3::intro y 8.4::intro); la deduplicacion entre ambos es efecto de ensamblado, pero el error nace al acunar el nodo. | `BKL-0035` |
| 24 | 2519 | `Operacion_operar_con_directores_administradores_y_vinculados_967f5e` (Operacion, «Operar con directores, administradores y vinculados») | `establecida_en` | `TextoOrdenado_lingob_pdf` (TextoOrdenado) | `lingob::2.3.2.2` | `E1-prompt` | Truncamiento material: el punto describe operar con directores, administradores y vinculados «en condiciones mas favorables que las acordadas de ordinario a su clientela», dentro de 2.3.2 (situaciones a prevenir o limitar); sin ese calificador la operacion extraida es otra, licita y general. | `BKL-0036` |

Destino (enmienda §2.1, «Destino de cada incorrecta»): una entrada de backlog
por incorrecta, con su `capa_pipeline`. Ninguna es falsedad de esquema en
campo estructurado, así que ninguna se lee además por la vía de A8.

## No decidibles

Ninguna.

## Decisión de la autora sobre los tests

Las 30 aristas no se sellan como tests de la regression suite en esta lectura;
se revisa después de r2. Texto y razón: `decision_tests.txt` (sellado en
`f51bb1f`), transcrito en la fila B6.0 fase 2b del plan.

## Reproducción

```bash
python3 -c "
import json,csv,math
d=json.load(open('reports/tanda0/obs12_sorteo/muestra_obs12.json'))
r=list(csv.DictReader(open('reports/tanda0/obs12_lectura/veredictos_obs12.csv',encoding='utf-8')))
k=sum(x['veredicto']=='correcta' for x in r); nd=sum(x['veredicto']=='no decidible' for x in r); n=len(r); z=1.959963984540054
p=k/n; den=1+z*z/n; c=(p+z*z/(2*n))/den; h=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/den
print(k,n,nd,round(c-h,3),round(c+h,3))
for x in r:
    if x['veredicto']!='correcta':
        a=d['aristas'][int(x['orden'])-1]; print(x['orden'],a['indice'],a['relation'],a['chunk_id'],x['capa_pipeline'])
"
```
