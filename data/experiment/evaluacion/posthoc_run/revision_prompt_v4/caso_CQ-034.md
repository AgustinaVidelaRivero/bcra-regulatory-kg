# Caso CQ-034 — calibración del verificador v4 (commit `e35fe21`)

## Pregunta

> Una persona humana residente compra moneda extranjera para atesorar; ¿qué límite mensual aplica si la operación se cursa con débito en cuenta frente a si se realiza en efectivo, y qué límite general rige para otras modalidades de formación de activos externos?

## Ground-truth (lectura pre-registrada)

`completitud_kg` primaria.

## Estado del output

`parse_ok=False`: el JSON final es sintácticamente inválido y contiene campos fuera de contrato (`estructural_kg_nota`, `atribucion_pata1`, `categoria_extra`). No hubo truncamiento (`end_turn`; 8103 tokens out, techo 8192). Tool calls: 13. Dato de contexto: esta traza entró con 0 claims fallidos desagregados (el síntoma usó el fallback del contexto).

## Atribuciones legibles en el JSON roto

- `completitud_kg` / primaria — pata: Límite general que rige para otras modalidades de formación de activos externos (punto 3.9)
- `completitud_kg` / primaria — pata: Límite mensual con débito en cuenta / contraste efectivo (punto 3.8.1 y 3.9)

## Prosa previa al JSON (verbatim)

> Confirmado: el punto 3.10 (personas jurídicas, requiere conformidad previa) sí está capturado, pero el punto 3.9 (personas humanas, otras modalidades, límite USD 200) NO está en el grafo. El grafo capturó el 3.8 (atesoramiento) y el 3.10 (jurídicas) pero omitió el 3.9, que es justo el que responde el "límite general para otras modalidades" y el límite USD 200 con débito.
> 
> Tengo evidencia suficiente para atribuir.

## Campo `razonamiento` del JSON roto (verbatim)

> El juez aprobó la pata central (USD 100 en efectivo, punto 3.8/3.9). La respuesta falló porque el agente declaró no respondibles las otras dos patas (límite con débito en cuenta y límite general para otras modalidades), cuando el TO SÍ las responde: el punto 3.9.1 del PDF establece un límite general de USD 200 mensual para la compra de ME por personas humanas residentes para la formación de activos externos bajo otras modalidades, y el 3.9.2 aclara que esa operación se cursa con débito en cuenta, mientras que si se usa efectivo el tope es USD 100. Es decir, el contraste débito/efectivo y el límite general USD 200 conviven en el punto 3.9. Investigué si el grafo captura ese límite: tras cinco búsquedas documentadas con los términos plausibles (USD 200, 'doscientos', 'cliente no supere', 'punto 3.9', 'otras modalidades') no aparece ningún nodo que lo contenga; el único nodo de FAE es un stub ('tipo: formación de activos externos', punto 3.10) sin límites, y el único USD 200 del grafo es el de retiros de efectivo con tarjeta en países no limítrofes (tema ajeno). El grafo capturó el 3.8 (atesoramiento) y el 3.10 (personas jurídicas, conformidad previa) pero OMITIÓ el 3.9, que es justo el que responde las dos patas fallidas. El agente actuó fielmente: buscó ampliamente, citó bien el único límite existente (USD 100 efectivo) y reportó honestamente el vacío; no hay decisión errónea del agente, ni glosa no soportada, ni contenido citado incorrecto. La falla se rompe en el grafo: falta extraer el contenido del punto 3.9.1-3.9.2 (nodo portador del límite USD 200 mensual y del contraste débito/efectivo) que el PDF sí tiene. Por eso completitud_kg, primaria, en ambas patas fallidas (una misma omisión —el punto 3.9— rompe las dos).

## Búsquedas declaradas en el JSON roto (verbatim)

  - consulta: «límite USD 200 mes calendario formación activos externos personas humanas»
    resultado: 0 nodos pertinentes; USD 200 solo aparece en 'Límite adelanto países no limítrofes' (retiros de efectivo con tarjeta, tema distinto)
  - consulta: «USD 200 doscientos mes calendario conjunto conceptos»
    resultado: 0 nodos pertinentes; solo 'retiros de efectivo países no limítrofes' y otros límites ajenos
  - consulta: «cliente no supere equivalente USD 200 mes calendario conjunto entidades»
    resultado: 0 nodos pertinentes; ningún nodo con el texto del 3.9.1
  - consulta: «Punto 3.9 formación activos externos otras modalidades remisión ayuda familiar»
    resultado: 0 nodos que capturen el 3.9; solo el stub Operacion_formacion_de_activos_externos y excepciones de otros puntos
  - consulta: «formación activos externos otras modalidades ayuda familiar derivados límite»
    resultado: stub FAE + límites ajenos (activos líquidos USD 100.000, activos en cartera); ningún nodo del 3.9.1
  - consulta: «límite mensual débito cuenta USD 300»
    resultado: 0 nodos con límite de monto asociado a débito en cuenta

(El `final_raw` íntegro está en `posthoc_run/calibracion_verificador_v4/CQ-034.json`, campo `_meta.final_raw`.)
