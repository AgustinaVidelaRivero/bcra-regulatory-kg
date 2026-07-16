# B1b — Censo de uso de `leer_pasaje_pdf` en las corridas congeladas

Fecha: 2026-07-16. SOLO LECTURA; única escritura: este archivo (zona gitignored). Sin API
(las dos llamadas ilustrativas del punto 2 son `pdf_locate.localize`, código puro local).
Solo hechos.

## 1. Uso por corrida × caso × rep

**Fuente del conteo:** los JSONs congelados NO persisten un conteo por tool, pero SÍ
persisten la **trayectoria completa del verificador** en `_meta.trayectoria_verificador`
(lista de pasos `{n, tool, input, output_truncado}` por rep) — el conteo por tool se deriva
de ahí. El agregado `detectores.tool_calls_usadas` (persistido) sirve de control de suma
(coincide en las 54 reps).

**Totales (las 3 corridas congeladas: gate2_v57 15 reps + piloto_v6 15 + validacion_v61 24
= 54 reps, 649 tool calls):**

| Tool | Invocaciones | % |
|---|---|---|
| **leer_pasaje_pdf** | **298** | **45,9%** |
| buscar_nodos | 124 | 19,1% |
| ver_nodo | 118 | 18,2% |
| ver_paso_completo | 93 | 14,3% |
| ver_vecinos | 16 | 2,5% |

**`leer_pasaje_pdf` es la tool más usada del verificador — se invocó en los 18 casos y en
las 54/54 reps (mínimo 2 por rep, máximo 21 — run_3/CQ-020 rep 3 del gate).** Tabla completa
por corrida × caso × rep (con el control `det.tool_calls_usadas`):

```
gate2_v57       run_3/CQ-017    r1  lpp= 6  {'leer_pasaje_pdf': 6, 'ver_paso_completo': 2, 'ver_nodo': 3, 'ver_vecinos': 1}  · det=12
gate2_v57       run_3/CQ-017    r2  lpp= 5  {'leer_pasaje_pdf': 5, 'ver_paso_completo': 4, 'ver_nodo': 4, 'buscar_nodos': 4}  · det=17
gate2_v57       run_3/CQ-017    r3  lpp= 6  {'leer_pasaje_pdf': 6, 'ver_paso_completo': 3, 'ver_nodo': 4}  · det=13
gate2_v57       run_3/CQ-020    r1  lpp=11  {'ver_nodo': 3, 'leer_pasaje_pdf': 11, 'buscar_nodos': 3, 'ver_paso_completo': 1}  · det=18
gate2_v57       run_3/CQ-020    r2  lpp=17  {'leer_pasaje_pdf': 17, 'buscar_nodos': 4, 'ver_nodo': 4, 'ver_paso_completo': 2, 'ver_vecinos': 1}  · det=28
gate2_v57       run_3/CQ-020    r3  lpp=21  {'leer_pasaje_pdf': 21, 'ver_nodo': 2, 'ver_paso_completo': 1, 'buscar_nodos': 3, 'ver_vecinos': 1}  · det=28
gate2_v57       run_3/CQ-025    r1  lpp= 5  {'leer_pasaje_pdf': 5, 'buscar_nodos': 2, 'ver_nodo': 2, 'ver_paso_completo': 3}  · det=12
gate2_v57       run_3/CQ-025    r2  lpp= 5  {'leer_pasaje_pdf': 5, 'buscar_nodos': 3, 'ver_nodo': 2, 'ver_paso_completo': 4}  · det=14
gate2_v57       run_3/CQ-025    r3  lpp= 6  {'leer_pasaje_pdf': 6, 'buscar_nodos': 3, 'ver_nodo': 2, 'ver_paso_completo': 1}  · det=12
gate2_v57       run_3/CQ-031    r1  lpp= 3  {'leer_pasaje_pdf': 3, 'buscar_nodos': 2, 'ver_nodo': 1, 'ver_paso_completo': 3}  · det=9
gate2_v57       run_3/CQ-031    r2  lpp= 3  {'leer_pasaje_pdf': 3, 'ver_nodo': 2, 'buscar_nodos': 2, 'ver_paso_completo': 3}  · det=10
gate2_v57       run_3/CQ-031    r3  lpp= 5  {'leer_pasaje_pdf': 5, 'ver_nodo': 2, 'buscar_nodos': 2, 'ver_paso_completo': 3}  · det=12
gate2_v57       run_3/CQ-034    r1  lpp= 7  {'leer_pasaje_pdf': 7, 'buscar_nodos': 5, 'ver_vecinos': 1, 'ver_paso_completo': 1}  · det=14
gate2_v57       run_3/CQ-034    r2  lpp= 4  {'leer_pasaje_pdf': 4, 'buscar_nodos': 4, 'ver_vecinos': 1, 'ver_nodo': 2, 'ver_paso_completo': 2}  · det=13
gate2_v57       run_3/CQ-034    r3  lpp= 2  {'leer_pasaje_pdf': 2, 'buscar_nodos': 4, 'ver_vecinos': 1, 'ver_paso_completo': 1}  · det=8
piloto_v6       run_3/CQ-016    r1  lpp= 2  {'leer_pasaje_pdf': 2, 'buscar_nodos': 1, 'ver_nodo': 2, 'ver_paso_completo': 1}  · det=6
piloto_v6       run_3/CQ-016    r2  lpp= 3  {'leer_pasaje_pdf': 3, 'buscar_nodos': 3, 'ver_nodo': 1, 'ver_paso_completo': 2}  · det=9
piloto_v6       run_3/CQ-016    r3  lpp= 4  {'leer_pasaje_pdf': 4, 'buscar_nodos': 2, 'ver_vecinos': 1, 'ver_nodo': 1, 'ver_paso_completo': 2}  · det=10
piloto_v6       run_3/CQ-018    r1  lpp= 9  {'leer_pasaje_pdf': 9, 'ver_nodo': 2, 'buscar_nodos': 1, 'ver_paso_completo': 1}  · det=13
piloto_v6       run_3/CQ-018    r2  lpp=11  {'leer_pasaje_pdf': 11, 'ver_paso_completo': 3}  · det=14
piloto_v6       run_3/CQ-018    r3  lpp= 9  {'leer_pasaje_pdf': 9, 'buscar_nodos': 1, 'ver_paso_completo': 1, 'ver_nodo': 1}  · det=12
piloto_v6       run_3/CQ-019    r1  lpp= 5  {'ver_nodo': 1, 'ver_paso_completo': 2, 'leer_pasaje_pdf': 5, 'buscar_nodos': 1}  · det=9
piloto_v6       run_3/CQ-019    r2  lpp= 4  {'ver_nodo': 1, 'ver_paso_completo': 1, 'leer_pasaje_pdf': 4}  · det=6
piloto_v6       run_3/CQ-019    r3  lpp= 2  {'ver_paso_completo': 1, 'ver_nodo': 2, 'leer_pasaje_pdf': 2}  · det=5
piloto_v6       run_3/CQ-024    r1  lpp= 7  {'leer_pasaje_pdf': 7, 'ver_paso_completo': 2, 'buscar_nodos': 5, 'ver_nodo': 3, 'ver_vecinos': 2}  · det=19
piloto_v6       run_3/CQ-024    r2  lpp= 7  {'leer_pasaje_pdf': 7, 'ver_paso_completo': 3, 'buscar_nodos': 3, 'ver_nodo': 2}  · det=15
piloto_v6       run_3/CQ-024    r3  lpp= 7  {'leer_pasaje_pdf': 7, 'buscar_nodos': 7, 'ver_nodo': 4, 'ver_paso_completo': 2}  · det=20
piloto_v6       run_3/CQ-033    r1  lpp= 2  {'leer_pasaje_pdf': 2, 'buscar_nodos': 1, 'ver_nodo': 2, 'ver_vecinos': 1, 'ver_paso_completo': 1}  · det=7
piloto_v6       run_3/CQ-033    r2  lpp= 2  {'leer_pasaje_pdf': 2, 'ver_nodo': 1, 'ver_paso_completo': 2, 'buscar_nodos': 1}  · det=6
piloto_v6       run_3/CQ-033    r3  lpp= 2  {'leer_pasaje_pdf': 2, 'ver_paso_completo': 1, 'ver_nodo': 1}  · det=4
validacion_v61  run_2/CQ-015    r1  lpp= 2  {'leer_pasaje_pdf': 2, 'ver_paso_completo': 1}  · det=3
validacion_v61  run_2/CQ-015    r2  lpp= 4  {'leer_pasaje_pdf': 4, 'ver_nodo': 2, 'buscar_nodos': 1, 'ver_paso_completo': 2}  · det=9
validacion_v61  run_2/CQ-015    r3  lpp= 2  {'leer_pasaje_pdf': 2, 'ver_paso_completo': 1, 'ver_nodo': 1}  · det=4
validacion_v61  run_2/CQ-018    r1  lpp=10  {'leer_pasaje_pdf': 10, 'ver_nodo': 3, 'ver_paso_completo': 1}  · det=14
validacion_v61  run_2/CQ-018    r2  lpp= 8  {'leer_pasaje_pdf': 8, 'buscar_nodos': 4, 'ver_nodo': 3, 'ver_paso_completo': 1}  · det=16
validacion_v61  run_2/CQ-018    r3  lpp=16  {'leer_pasaje_pdf': 16, 'buscar_nodos': 1, 'ver_paso_completo': 1, 'ver_nodo': 1}  · det=19
validacion_v61  run_2/CQ-019    r1  lpp= 3  {'leer_pasaje_pdf': 3, 'ver_nodo': 2, 'ver_vecinos': 1, 'ver_paso_completo': 4}  · det=10
validacion_v61  run_2/CQ-019    r2  lpp= 4  {'leer_pasaje_pdf': 4, 'buscar_nodos': 3, 'ver_nodo': 4, 'ver_paso_completo': 2, 'ver_vecinos': 1}  · det=14
validacion_v61  run_2/CQ-019    r3  lpp= 3  {'leer_pasaje_pdf': 3, 'ver_nodo': 3, 'buscar_nodos': 3}  · det=9
validacion_v61  run_2/CQ-025    r1  lpp= 3  {'ver_paso_completo': 1, 'leer_pasaje_pdf': 3, 'buscar_nodos': 4, 'ver_nodo': 3}  · det=11
validacion_v61  run_2/CQ-025    r2  lpp= 5  {'leer_pasaje_pdf': 5, 'ver_paso_completo': 2, 'buscar_nodos': 5, 'ver_nodo': 3, 'ver_vecinos': 1}  · det=16
validacion_v61  run_2/CQ-025    r3  lpp= 5  {'leer_pasaje_pdf': 5, 'ver_paso_completo': 1, 'buscar_nodos': 6, 'ver_nodo': 3}  · det=15
validacion_v61  run_4/CQ-014    r1  lpp= 2  {'leer_pasaje_pdf': 2, 'ver_nodo': 1}  · det=3
validacion_v61  run_4/CQ-014    r2  lpp= 2  {'leer_pasaje_pdf': 2, 'ver_nodo': 1, 'ver_paso_completo': 1}  · det=4
validacion_v61  run_4/CQ-014    r3  lpp= 2  {'leer_pasaje_pdf': 2, 'ver_paso_completo': 1, 'ver_nodo': 1}  · det=4
validacion_v61  run_4/CQ-017    r1  lpp= 6  {'leer_pasaje_pdf': 6, 'ver_nodo': 2, 'buscar_nodos': 1, 'ver_paso_completo': 1}  · det=10
validacion_v61  run_4/CQ-017    r2  lpp= 4  {'ver_paso_completo': 3, 'leer_pasaje_pdf': 4, 'buscar_nodos': 3, 'ver_nodo': 1}  · det=11
validacion_v61  run_4/CQ-017    r3  lpp= 5  {'leer_pasaje_pdf': 5, 'ver_paso_completo': 2, 'buscar_nodos': 3, 'ver_nodo': 1, 'ver_vecinos': 1}  · det=12
validacion_v61  run_4/CQ-019    r1  lpp= 6  {'leer_pasaje_pdf': 6, 'ver_nodo': 3, 'buscar_nodos': 3, 'ver_paso_completo': 1}  · det=13
validacion_v61  run_4/CQ-019    r2  lpp= 7  {'leer_pasaje_pdf': 7, 'buscar_nodos': 4, 'ver_nodo': 4, 'ver_vecinos': 1, 'ver_paso_completo': 1}  · det=17
validacion_v61  run_4/CQ-019    r3  lpp= 7  {'leer_pasaje_pdf': 7, 'buscar_nodos': 8, 'ver_nodo': 6, 'ver_vecinos': 1, 'ver_paso_completo': 2}  · det=24
validacion_v61  run_4/CQ-020    r1  lpp= 3  {'ver_paso_completo': 2, 'ver_nodo': 5, 'leer_pasaje_pdf': 3, 'buscar_nodos': 3}  · det=13
validacion_v61  run_4/CQ-020    r2  lpp= 3  {'ver_nodo': 4, 'ver_paso_completo': 1, 'leer_pasaje_pdf': 3, 'buscar_nodos': 3}  · det=11
validacion_v61  run_4/CQ-020    r3  lpp= 4  {'ver_paso_completo': 2, 'ver_nodo': 4, 'leer_pasaje_pdf': 4, 'buscar_nodos': 2}  · det=12
```

## 2. Comportamiento de la tool — dos llamadas ilustrativas (verbatim)

`pdf_locate.localize(source_doc, location, window=1400)` (pdf_locate.py:65), sin API. Los
outputs completos, verbatim — la pregunta de diseño (¿el pasaje incluye el
encabezado/apertura de la sección con su declaración de alcance, o entra directo al cuerpo?)
la responde el propio output:

### (a) `localize('TO_capitales_minimos_actual.pdf', 'Punto 12.3')`

```json
{
 "metodo": "punto",
 "ref": "Punto/Sección 12.3 (PDF pág 177)",
 "pasaje": "12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026 c omo con-\nsecuencia de lo establecido en el punto 4.1. del TO sobre Autoridades de Entidades Financie-\nras, la exigencia de capital por riesgo operacional para entidades del grupo 2 determinada a\ntravés de la aplicación de la  expresión descripta en el punto 7.2 . hasta el 30/06/26 no podrá\nsuperar:\nEl 17% en el caso de entidades del grupo B y el 14% en el caso de entidades del C –en fun-\nción de lo establecido, con vigencia hasta el 31/12/25, en la Sección 4. del TO sobre Autorida-\ndes de Entidades Financieras –, del promedio de los últimos 36 meses –anteriores al mes a\nque corresponda la determinación de la exigencia – de la exigencia de capital mínimo por ries-\ngo de crédito calculada según lo previsto en la Sección 2., expresada en moneda homogénea\ndel mes anterior al que se efectúa el cálculo.\nLos límites máximos establecidos precedentemente se reducirán a 11% y a 8%, respectiva-\nmente, cuando la entidad financiera cuente con calificación 1, 2 o 3 conforme a la valoración\notorgada por la SEFYC, en oportunidad de la úl tima inspección efectuada, respecto de todos\nlos siguientes aspectos: la entidad en su conjunto, sus sistemas informáticos y la labor de los\nresponsables de la evaluación de sus sistemas de control interno.\nB.C.R.A. CAPITALES MÍNIMOS DE LAS ENTIDADES FINANCIERAS\nSección 12.",
 "localizacion_pdf": "ok"
}
```

### (b) `localize('TO_clasificacion_deudores_actual.pdf', 'Punto 4.2')`

```json
{
 "metodo": "punto",
 "ref": "Punto/Sección 4.2 (PDF pág 15)",
 "pasaje": "4.2. Criterio básico de clasificación. \nEl criterio básico a ser utilizado para efectuar tal clasificación es la capacidad de pago en el fu-\nturo de la deuda o de los compromisos objeto de la garantía de la entidad financiera. \n4.3. Evaluación de la capacidad de pago. \n4.3.1. Al evaluar la capacidad de repago, el énfasis deberá ponerse en el análisis de los flujos \nde fondos realizado por la entidad. \n4.3.2. En segundo lugar, deberá considerarse la posibilidad de liquidación de activos no im-\nprescindibles para la operatoria de la empresa. \n4.4. Financiaciones cubiertas con garantías preferidas “A”. \nNo corresponderá la evaluación de la capacidad de repago respecto de las financiaciones que \nse encuentren respaldadas con tales garantías. \n4.5. Deudores que no deben ser objeto de clasificación. \nLos deudores cuyas financiaciones se encuentren cubiertas totalmente con garantías preferidas \n“A” no serán objeto de clasificación, sin perjuicio de su información según las normas que se \nestablezcan en los regímenes respectivos. \n4.6. Financiaciones –sin responsabilidad para el cedente– amparadas con seguros de crédito por \nriesgo comercial y con seguros de riesgo de crédito “con alcance de comprador público”. \nSe procederá a clasificar a la compañía de seguros en función de la mora según los criterios \naplicables para la cartera de consumo, teniendo en cuenta la fecha de vencimiento",
 "localizacion_pdf": "ok"
}
```

## 3. Política actual del prompt (verbatim)

**verificador.py, líneas 252-255** (checklist de cierre, regla 5 del método):

> ```
> 5. No cierres por COINCIDENCIA SUPERFICIAL. Que un nodo comparta palabras con la pregunta no \
> significa que la responda. Antes de cerrar, chequeá: (a) ¿leíste con leer_pasaje_pdf la fuente de \
> cada pata fallida?; (b) ¿abriste con ver_nodo el CONTENIDO de los nodos que vas a citar (no \
> solo su label/resumen)? Si alguna respuesta es "no", no concluyas todavía.
> ```

**verificador.py, líneas 286-293** (catálogo de tools):

> ```
> TOOLS (para la FASE B; cuáles y cuántas veces es tu criterio):
> - buscar_nodos / ver_nodo / ver_vecinos: exploran el MISMO grafo que usó el agente. Podés mirar \
> CUALQUIER nodo, no solo los que el agente vio. OJO: buscar_nodos indexa SOLO label e id (no las \
> descriptions).
> - leer_pasaje_pdf(source_doc, location): qué dice realmente el PDF fuente.
> - ver_paso_completo(paso): el contexto muestra outputs truncados; si necesitás saber qué vio \
> REALMENTE el agente en un paso, usá esta tool (re-ejecuta ese tool call y devuelve el output íntegro).
> ```

(La línea 276, ya ubicada en B1, refiere a ver_paso_completo en la prueba C1a — no a
leer_pasaje_pdf.)

**Además, la política viaja por referencia en la taxonomía ensamblada al prompt en runtime**
(`taxonomia.md`, dentro del rango que `taxonomia_section()` inyecta):

- línea 57 (tabla de `alucinacion_agente`, modo b): "constancia de búsqueda (campo
  `busquedas`) + verificación negativa contra el PDF (`leer_pasaje_pdf`)";
- línea 75 (árbol, rama faithfulness): "¿el PDF tiene el dato? (`leer_pasaje_pdf`)";
- línea 145 (herramientas del verificador): "**leer_pasaje_pdf** en un punto/página
  específico. Sirve para responder '¿qué dice realmente la fuente?'. Si la ubicación no
  ancla, devuelve `localizacion_pdf=\"fallida\"` como señal explícita."

---

*Fin de B1b. Hechos para el diseño de v7; sin propuesta. Frenado para revisión.*
