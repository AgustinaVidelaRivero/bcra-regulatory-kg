# U-B2.2 fase 2 — Hallazgos de la corrida 3 (perfil congelado sobre salida/kg.json, sha 8e2eadee…)

El mandato anticipaba S15 PASS y S4–S6 PASS. Resultado: S4, S5, S6 PASS
(también S1, S2, S3, S19); DOS bloqueantes en FAIL. Por regla del mandato
son HALLAZGO, no ajuste de la shape.

Comando:
  PYTHONDONTWRITEBYTECODE=1 python3 scripts/shapes_validator.py --perfil congelado \
    --kg data/experiment/reextraccion_v2/corpus_v2/salida/kg.json \
    --excepciones data/experiment/esq_v3_miembros/esquema_v3_clases.json \
    --out <scratchpad>/post/shapes_salida_8e2eadee_congelado.md
  código de salida: 1 (NO PASA)

## Hallazgo 1 — S15 FAIL: el grafo 8e2eadee… NO tiene esqueleto

Regla: S15 (todo rol tiene miembro_de o está declarado; la cuenta declarada
coincide con la medida). Casos: 5 roles huérfanos sin declarar + 1 cuenta
(declarada 12, medida 5) = 6 líneas de violación.

Evidencia: el grafo no contiene NINGUNA arista de esqueleto —
0 miembro_de, 0 subclase_de, 0 instancia_de, 0 parte_de (Counter de
`relation` sobre edges; comando en estado_arbol / consola). La descripción
«esqueleto v3» del mandato para este archivo no se corresponde con su
contenido: el commit b01eb18 (U-ESQ-V3) declara que salida/kg.json quedó
BYTE-IDÉNTICO (8e2eadee…), es decir, la inyección del esqueleto no se
aplicó a este grafo; el esqueleto (v2) vive solo en salida_r1/kg.json.

Tres ejemplos con path (índice en `nodes` de salida/kg.json):
  1. nodes[3324]  Sujeto_rol_alcance_capmin
     provenance {"to":"cap","archivo":"TO_capitales_minimos_actual.pdf","punto":"1.1","rol_documental":"punto_propio"}
  2. nodes[6174]  Sujeto_rol_entidad_autorizada_exterior
     provenance {"to":"ext","archivo":"TO_exterior_cambios_actual.pdf","punto":"1.2","rol_documental":"punto_propio"}
  3. nodes[1293]  Sujeto_rol_entidad_comprendida_reginf
     provenance {"to":"ric","archivo":"TO_regimen_informativo_contable_mensual_actual.pdf","punto":"1.1","rol_documental":"punto_propio"}
  (los otros dos: nodes[417] Sujeto_rol_sujeto_obligado_proteccion,
   nodes[910] Sujeto_rol_obligado_a_clasificar_clasificacion)

## Hallazgo 2 — S20 FAIL: un valor fuera del enum congelado

Regla: S20 (Obligacion.tipo ∈ enum de 6). Casos: retirados 0; otros fuera
del enum 1 (`verificacion_informativa`).

Único caso, con path:
  nodes[4178]  Obligacion_la_entidad_interviniente_debera_verificar_previamente_que_la_factura_comercial_e_3fc14d
  properties.tipo = "verificacion_informativa"
  provenance {"to":"ext","archivo":"TO_exterior_cambios_actual.pdf","punto":"10.4.3.1","rol_documental":"punto_propio"}
El mismo nodo persiste en r1 (nodes[1907] de salida_r1/kg.json, chunk
ext::10.4.3.1, página 142), así que la corrida 4 también lo reporta.

## Nota sobre S23 en la corrida 3

60 aplica_a hacia Sujetos propuestos (40 destinos) frente a 57 (38) en r1:
el mandato solo fija la cifra 57 para r1; la de 8e2eadee… se reporta tal
como da.
