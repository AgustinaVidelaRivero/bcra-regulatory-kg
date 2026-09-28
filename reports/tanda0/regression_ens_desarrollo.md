# Regression suite — data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo/r1/kg.json

- kg: `data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo/r1/kg.json` sha256 `eab2fdd01dec4dad026d596a793919e666920fab127d7efb14b5b00857ae64ef` — 6378 nodos / 15007 aristas; generación declarada 3 (formato detectado: 3)
- catálogo: `data/experiment/esq_v3_miembros/esquema_v3_clases.json` (versión 3.0, sha256 `dad88cc92afc53e922989cad84eb68b2ef142b66c221f2a566e7fb5da1bcfd36`); política de cuarentena: **flaggeada**
- esqueleto de referencia (T4): `/Users/agustinavidelarivero/INGENIERIA IA/TESIS/bcra-regulatory-kg/data/experiment/grafo_v2/reensamblado_v3/kg.json` sha256 `26fac8b49f6c08c1aa364b47273d36958d831f240d4e6b4ee7700b6a0bff3571`
- retriever: GraphIndex de data/experiment/evaluacion/harness.py (importado; sha256 `fd267e833866f86850e43130e627b08d78e05523b97484696de0ab0c8c9fba9e`), loader.load_graph_from_path adapter_key=None
- partición declarada: {'items': 46, 'convertibles': 19, 'con_condicion': 23, 'no_convertibles': 4, 'retriever': 15, 'por_grupo': {'i-BKL': 12, 'i-RT': 12, 'ii': 12, 'iii': 10}}

## Resumen: 46 ítems — resuelto 22 / persiste 16 / no_aplicable 8
Ranks sellados (retriever in-memory): consultas que coinciden con el sellado 7/25; objetivos 25/69; objetivos en ventana declarada 17; objetivos ausentes 5.

| Id | Grupo | Convertibilidad | Retr. | Forma | Estado | Detalle |
|---|---|---|---|---|---|---|
| BKL-0017 | i-BKL | convertible | sí | F1 + F4 ×2 + F5 ×3 (limite 10) | **persiste** | nodo=1 ['Obligacion_los_clientes_de_la_entidad_tanto_residentes_en_el_pais_de_los']; establecida_en=True; aplica_a=True; consultas en ventana=2/3 (persiste solo por alcanzabilidad si lo demás cumple) |
| BKL-0006 | i-BKL | convertible | no | F3 (montos de la tabla) + F4 (exceptua → restantes) + F5 ×2 informativo (limite 10 / 13) | **no_aplicable** | sin nodos anclados en cap 1.2 con «exigencia básica»: tabla del 1.2 no extraída |
| BKL-0023 | i-BKL | convertible | no | F3 (properties.umbral) | **no_aplicable** | ninguna Restriccion anclada en cap 1.2 con la oración de compañías financieras |
| BKL-0019 | i-BKL | con condición | sí | F4 ×8 (subclase_de si laudada / padre_sugerido si flaggeada) + F4 ausente (excluida, laudada) | **persiste** | politica=flaggeada: padre_sugerido 1/4 presentes (de 8); Inversor: padre_sugerido→contraparte=si tgt_presente=True \|\| Entidades financieras del grup: padre_sugerido→entidad_financiera=NO tgt_presente=True \|\| Benef… |
| BKL-0004 | i-BKL | convertible | sí | F1 ×9 + F4 (8 regula + 9 establecida_en) + F5 ×8 (7 consultas + proxy RT-C5-4; limite 10) | **persiste** | nodos 8/9 -> N1@6.5:1 N2@6.5.1:1 N3@6.5.2:0 N4@6.5.2.1:1 N5@6.5.2.2:1 N6@6.5.2.3:1 N7@6.5.3:1 N8@6.5.4:4 N9@6.5.5:4; regula=0/8 establecida_en=8/9; objetivos en ventana=3/30 |
| BKL-0003 | i-BKL | convertible | sí | F1 + F4 ×2 + F4 ausente (a Sujeto) + F5 ×11 (N1 + controles rol/pnfc; limite 10) | **persiste** | Excepcion=1 ['Excepcion_excepto_que_se_trate_de_asociaciones_mutuales_o_cooperativas_7']; establecida_en=True exceptua_obligacion=False aristas_con_Sujeto=0; objetivos en ventana=9/16 |
| BKL-0005 | i-BKL | convertible | sí | F3 (dos calificadores en descripcion) + F5 ×3 (limite 10) | **resuelto** | portadores=1 con_ambos_calificadores=1 ['Obligacion_para_el_calculo_del_importe_correspondiente_al_mes_n_proceder']; consultas en ventana=3/3 |
| BKL-0007 | i-BKL | convertible | no | = BKL-0017 (sin test propio) | **persiste** | = BKL-0017 (cerrada por referencia; defecto confirmado, no corrección aplicada): nodo=1 ['Obligacion_los_clientes_de_la_entidad_tanto_residentes_en_el_pais_de_los']; establecida_en=True; aplica_a=True; consultas en ve… |
| BKL-0026 | i-BKL | no convertible | no | ninguna (no convertible) | **no_aplicable** | no convertible: conducta del agente (paráfrasis invertida del verbatim con ver_nodo byte-idéntico, RT-C6-1 vs RT-C6-2, 3/3 en N=3); no es observable con una comprobación determinística sobre un kg.json (inventario_B21… |
| BKL-0027 | i-BKL | no convertible | no | ninguna (no convertible) | **no_aplicable** | no convertible: conducta del agente (pidió ver_vecinos salientes de un rol que solo tiene miembro_de entrantes, RT-C6-3); la estructura del rol se testea en RT-C6-3 (inventario_B21_fase1.md:108). defecto confirmado, n… |
| BKL-0028 | i-BKL | con condición | no | F1 sobre el catálogo parametrizado (ids «del exterior» separados; sin alias del exterior en los domésticos) + F1 en el grafo | **persiste** | catálogo v3: alias «del exterior» en ['Sujeto_entidad_financiera', 'Sujeto_banco', 'Sujeto_entidad_cambiaria']; ids separados []; presentes en el grafo []. defecto confirmado, no corrección aplicada. |
| BKL-0029 | i-BKL | con condición | no | F4 (miembro_de del rol de convca → id nuevo del catálogo) | **persiste** | ids candidatos en catálogo=[]; miembro_de del rol=['Sujeto_entidad_financiera']; residuo colectivo_operativo_sin_id=True. defecto confirmado, no corrección aplicada. |
| RT-C5-1 | i-RT | con condición | sí | F3 (valor: cinco categorías en N1) | **persiste** | N1 ['Definicion_niveles_de_clasificacion_de_clientes_y_financiaciones_7e4fe7']: gold 0/5; faltan ['en situacion normal', 'con seguimiento especial', 'con problemas', 'con alto riesgo de insolvencia', 'irrecuperable'] |
| RT-C5-2 | i-RT | con condición | sí | F3 (valor: tres situaciones en N3) | **persiste** | sin N3 (nodo del 6.5.2 «seguimiento especial»): el gold no está en el grafo |
| RT-C5-3 | i-RT | con condición | sí | F3 (valor: «antes de los 60 días … mora» en N5) | **resuelto** | N5 ['Definicion_en_negociacion_o_con_acuerdos_de_refinanciacion_83b87e']: gold 2/2 |
| RT-C5-4 | i-RT | convertible | sí | F3 (valor: primera vez / primera cuota / única vez en N6) | **persiste** | N6 ['Potestad_reclasificacion_unica_en_tratamiento_especial_0534fb']: gold 1/3; faltan ['por primera vez dentro del ano calendario', 'primera cuota'] |
| RT-C5-5 | i-RT | convertible | no | F2 (nodo con «riesgo medio» anclado en 7.2 exacto) + F3 (N1 sin niveles del 7.2) | **no_aplicable** | sin nodos con punto exactamente 7.2 de Clasificación: el proxy falla por ancla, no por contenido (inventario_B21_fase1.md:267, §5.7; decisión 5) |
| RT-C6-1 | i-RT | con condición | sí | F3 (valor en N1) | **resuelto** | RT-C6-1: gold «mutuales o cooperativas» presente en ['Excepcion_excepto_que_se_trate_de_asociaciones_mutuales_o_cooperativas_7']; cláusula «por las financiaciones que otorguen» (informativa)=AUSENTE |
| RT-C6-2 | i-RT | con condición | sí | F3 (valor en N1; = RT-C6-1) | **resuelto** | RT-C6-2 (= RT-C6-1 en la parte de valor): gold «mutuales o cooperativas» presente en ['Excepcion_excepto_que_se_trate_de_asociaciones_mutuales_o_cooperativas_7']; cláusula «por las financiaciones que otorguen» (inform… |
| RT-C6-3 | i-RT | con condición | sí | F4 ×n (miembro_de entrantes = miembros del rol en el catálogo) | **resuelto** | miembro_de entrantes=7 esperados(catálogo)=7; faltan=[] sobran=[] |
| RT-C6-4 | i-RT | convertible | no | F4 (emisoras --miembro_de--> rol) + F4 ausente (N1 ↔ Sujeto) | **resuelto** | emisoras→rol=True; N1=presente, aristas con Sujeto=False |
| RT-C7-1 | i-RT | convertible | sí | F3 (valor: ambos calificadores en el portador) | **resuelto** | RT-C7-1 portador ['Obligacion_para_el_calculo_del_importe_correspondiente_al_mes_n_proceder']: gold 2/2 |
| RT-C7-2 | i-RT | convertible | sí | F3 (valor: calificador de la RPC) | **resuelto** | RT-C7-2 portador ['Obligacion_para_el_calculo_del_importe_correspondiente_al_mes_n_proceder']: gold 1/1 |
| RT-C7-3 | i-RT | convertible | sí | F3 (valor: calificador de la franquicia) | **resuelto** | RT-C7-3 portador ['Obligacion_para_el_calculo_del_importe_correspondiente_al_mes_n_proceder']: gold 1/1 |
| T1 | ii | convertible | no | F2 + F3 | **resuelto** | anclados_3_9=18 puntos=['3.9', '3.9.1', '3.9.2', '3.9.3', '3.9.4', '3.9.5'] con_usd_200=1 |
| T2 | ii | convertible | no | F1 (conteo) + F2 (conteo de puntos) | **persiste** | nodos_separados_ext=4 puntos_distintos=['3.11.3.2', '7.11.5', '7.5.3', '7.8.5.1', '7.9.5'] |
| T3 | ii | convertible | no | F2 + F3 | **resuelto** | anclados_1_1_2_5=3 con_salvedad=2 de_los_cuales_excepcion=1 |
| T4 | ii | con condición | no | F1 + F4 (paridad de esqueleto contra --esqueleto-referencia, decisión 8) | **persiste** | esqueleto_esperados=70 faltan_nodos=0 aristas_esqueleto_en_grafo=117 (excluidas cuarentena_laudada=0) referencia=82 faltan_triplas=0 |
| T5 | ii | con condición | no | F4 + F3 (properties.evidencia) | **persiste** | n_muestra=30 fallas=25 (presente_con_otra_evidencia=16, ausente=9) |
| T6 | ii | con condición | no | F1 | **resuelto** | n=5 fuera_del_esperado=[] faltan=[] |
| T7 | ii | con condición | no | F3 + F4 + F4 ausente (política de cuarentena, decisión 3) | **persiste** | politica=flaggeada propuestos=19 aristas_padre_sugerido=18 malos=0 {} fuera_catalogo_no_propuestos=4 |
| I1 | ii | no convertible | no | ninguna (no convertible) | **no_aplicable** | no convertible: conservación de nodos Σ pre-merge − merges = finales exige los grafos pre-merge (salida/<to>/grafo_<to>.json) y los conteos de merge, que solo existen para la cadena r1 (inventario_B21_fase1.md:135) |
| I2 | ii | no convertible | no | ninguna (no convertible) | **no_aplicable** | no convertible: conservación de aristas, ídem I1 (inventario_B21_fase1.md:136) |
| I3 | ii | convertible | no | F1 (conteo: unicidad de ids y de triplas) | **resuelto** | nodes=6378 edges=15007 ids_duplicados=0 triplas_duplicadas=0 |
| I4 | ii | convertible | no | F4 (cero colgantes) | **resuelto** | colgantes=0 |
| I5 | ii | convertible | no | F2 (al menos una provenance por nodo y arista, adaptador) | **resuelto** | nodos_sin=0 aristas_sin=0 |
| E4-a1 | iii | con condición | no | F1 ausente (ningún propuesto residual resoluble por label_exacto) | **resuelto** | propuestos=19 con candidato label_exacto=0 resolubles no resueltos=0 [] |
| E4-a2 | iii | con condición | no | F1 ausente (alias_exacto) | **resuelto** | propuestos=19 con candidato alias_exacto=0 resolubles no resueltos=0 [] |
| E4-a3 | iii | con condición | no | F1 ausente (id_slug; e2_lib.slugify_full importado) | **resuelto** | propuestos=19 con candidato id_slug=0 resolubles no resueltos=0 [] |
| E4-a4 | iii | con condición | no | F1 ausente (label_singularizado) | **resuelto** | propuestos=19 con candidato label_singularizado=0 resolubles no resueltos=0 [] |
| E4-a5 | iii | con condición | no | F1 ausente (alias_en_parentesis) + F3 (padre_sugerido) | **resuelto** | propuestos=19 con candidato alias_en_parentesis=0 resolubles no resueltos=0 []; propuestos con padre_sugerido=19 |
| E4-a6 | iii | con condición | no | F1 ausente (claves ambiguas / alias_resueltos que re-resuelven sin ambigüedad) | **resuelto** | claves ambiguas del índice=4; propuestos residuales con motivo ambiguo=0/19; alias_resueltos re-resueltos=3/3 malos=[] |
| E4-a7 | iii | con condición | no | F3 (cuarentena=true normalizada) + F1 (todo Sujeto no propuesto ∈ catálogo) | **persiste** | propuestos=19 sin_cuarentena_true=0 con_id_de_catalogo=0 sujetos_fuera_catalogo_no_propuestos=4 |
| E4-a8 | iii | con condición | no | F3 (alias_resueltos en ids de catálogo) + F1 ausente + F4 ausente; parte pre-E4 no_aplicable | **persiste** | alias_resueltos en 0/3 ids de catálogo; propuestos resueltos aún presentes=0; provenances acumuladas y dedup: no observables sin el grafo pre-E4 (no_aplicable parcial) |
| E4-b | iii | con condición | no | F1 (= T6) + F3 (properties.archivo ∈ archivos de E0) | **resuelto** | TextoOrdenado=5; con properties.archivo en el conjunto de E0: 5/5; fuera=[]; T6=resuelto |
| E4-c | iii | con condición | no | ninguna directa (no observable sobre un kg.json) | **no_aplicable** | solo observable con el registro de conflictos (salida_r1/e4_conflictos.json) o los grafos pre-E4: los conflictos de properties no se persisten en el kg.json; el proxy débil (un solo valor de materia/version por TextoO… |

## Regresión contra la fixture
Sin `--esperado`: no se computa regresión.

## Consultas de rank (por ítem)
- [BKL-0017] «criterio general clasificación deudores» (limite pedido 10): C1: rank=7 sellado=1 limite=10 ≠
- [BKL-0017] «qué clientes deben ser clasificados» (limite pedido 10): C1: rank=None sellado=1 limite=10 ≠
- [BKL-0017] «clasificación residentes en el exterior» (limite pedido 10): C1: rank=1 sellado=3 limite=10 ≠
- [BKL-0004] «niveles clasificación deudores cartera comercial» (limite pedido 10): C5.N1: rank=None sellado=1 limite=10 ≠ | C5.N7: rank=None sellado=4 limite=10 ≠ | C5.N9: rank=None sellado=5 limite=10 ≠ | C5.N2: rank=None sellado=6 limite=10 ≠ | C5.N3: rank=None sellado=8 limite=10 ≠ [objetivo AUSENTE]
- [BKL-0004] «seguimiento especial deudores» (limite pedido 10): C5.N1: rank=None sellado=1 limite=10 ≠ | C5.N4: rank=None sellado=3 limite=10 ≠ | C5.N6: rank=None sellado=4 limite=10 ≠ | C5.N5: rank=None sellado=5 limite=10 ≠ | C5.N3: rank=None sellado=6 limite=10 ≠ [objetivo AUSENTE]
- [BKL-0004] «punto 6.5 niveles clasificación» (limite pedido 10): C5.N1: rank=None sellado=1 limite=10 ≠ | C5.N7: rank=None sellado=2 limite=10 ≠ | C5.N9: rank=None sellado=3 limite=10 ≠ | C5.N2: rank=None sellado=4 limite=10 ≠ | C5.N8: rank=None sellado=5 limite=10 ≠ | C5.N3: rank=None sellado=6 limite=10 ≠ [objetivo AUSENTE]
- [BKL-0004] «situaciones que integran el seguimiento especial» (limite pedido 10): C5.N3: rank=None sellado=7 limite=10 ≠ [objetivo AUSENTE]
- [BKL-0004] «cinco categorías cartera comercial» (limite pedido 10): C5.N1: rank=None sellado=1 limite=10 ≠ | C5.N7: rank=None sellado=7 limite=10 ≠ | C5.N9: rank=None sellado=8 limite=10 ≠ | C5.N2: rank=None sellado=9 limite=10 ≠ | C5.N4: rank=None sellado=10 limite=10 ≠
- [BKL-0004] «en negociación o con acuerdos de refinanciación» (limite pedido 10): C5.N5: rank=1 sellado=1 limite=10 = | C5.N3: rank=None sellado=2 limite=10 ≠ [objetivo AUSENTE]
- [BKL-0004] «situación normal cartera comercial» (limite pedido 10): C5.N2: rank=3 sellado=1 limite=10 ≠ | C5.N1: rank=None sellado=2 limite=10 ≠ | C5.N4: rank=None sellado=3 limite=10 ≠ | C5.N6: rank=None sellado=4 limite=10 ≠ | C5.N5: rank=None sellado=5 limite=10 ≠
- [BKL-0004] «reclasificación en tratamiento especial refinanciación» (limite pedido 10): C5.N6: rank=2 sellado=4 limite=10 ≠
- [BKL-0003] «asociación mutual financiaciones proveedor no financiero crédito» (limite pedido 10): C6.N1: rank=None sellado=1 limite=10 ≠ | C6.rol: rank=None sellado=None limite=10 = | C6.pnfc: rank=1 sellado=2 limite=10 ≠
- [BKL-0003] «sujeto obligado protección usuarios servicios financieros» (limite pedido 10): C6.N1: rank=None sellado=1 limite=10 ≠ | C6.rol: rank=3 sellado=5 limite=10 ≠ | C6.pnfc: rank=None sellado=None limite=10 =
- [BKL-0003] «proveedor no financiero crédito» (limite pedido 10): C6.N1: rank=None sellado=None limite=10 = | C6.rol: rank=None sellado=None limite=10 = | C6.pnfc: rank=1 sellado=1 limite=10 =
- [BKL-0003] «asociación mutual» (limite pedido 10): C6.N1: rank=None sellado=1 limite=10 ≠ | C6.rol: rank=None sellado=None limite=10 = | C6.pnfc: rank=None sellado=None limite=10 =
- [BKL-0003] «definición proveedor no financiero crédito PNFC» (limite pedido 10): C6.N1: rank=None sellado=None limite=10 = | C6.rol: rank=None sellado=None limite=10 = | C6.pnfc: rank=1 sellado=1 limite=10 =
- [BKL-0003] «proveedor no financiero crédito comercios empresas personas jurídicas» (limite pedido 10): C6.N1: rank=None sellado=None limite=10 = | C6.rol: rank=None sellado=None limite=10 = | C6.pnfc: rank=1 sellado=1 limite=10 =
- [BKL-0003] «exclusión excluido no alcanzado no incluido sujeto obligado» (limite pedido 10): C6.N1: rank=None sellado=4 limite=10 ≠ | C6.rol: rank=None sellado=None limite=10 = | C6.pnfc: rank=None sellado=None limite=10 =
- [BKL-0003] «mutuales cooperativas sujeto obligado protección usuarios» (limite pedido 10): C6.N1: rank=None sellado=1 limite=10 ≠ | C6.rol: rank=1 sellado=2 limite=10 ≠ | C6.pnfc: rank=None sellado=None limite=10 =
- [BKL-0003] «excepción asociaciones mutuales cooperativas» (limite pedido 10): C6.N1: rank=1 sellado=1 limite=10 = | C6.rol: rank=None sellado=None limite=10 = | C6.pnfc: rank=None sellado=None limite=10 =
- [BKL-0003] «cooperativa que otorga financiaciones protección de usuarios» (limite pedido 10): C6.N1: rank=None sellado=1 limite=10 ≠ | C6.rol: rank=3 sellado=5 limite=10 ≠ | C6.pnfc: rank=None sellado=None limite=10 =
- [BKL-0003] «asociaciones mutuales proveedores no financieros de crédito» (limite pedido 10): C6.N1: rank=None sellado=1 limite=10 ≠ | C6.rol: rank=None sellado=None limite=10 = | C6.pnfc: rank=1 sellado=2 limite=10 ≠
- [BKL-0005] «esquema cálculo importe mes n disminución exigencia franquicia» (limite pedido 10): C7: rank=1 sellado=1 limite=10 =
- [BKL-0005] «responsabilidad patrimonial computable cálculo importe correspondiente al mes» (limite pedido 10): C7: rank=1 sellado=1 limite=10 =
- [BKL-0005] «franquicia importe correspondiente al mes n cálculo esquema» (limite pedido 10): C7: rank=1 sellado=1 limite=10 =
