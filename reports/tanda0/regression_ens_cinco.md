# Regression suite — data/experiment/reextraccion_v2/corpus_tanda0/ens_cinco/r1/kg.json

- kg: `data/experiment/reextraccion_v2/corpus_tanda0/ens_cinco/r1/kg.json` sha256 `4097d4fd3f300cb1c2cf09bef59e3ccb9a30b1de18334e6230102a5a3106d00a` — 1979 nodos / 3983 aristas; generación declarada 3 (formato detectado: 3)
- catálogo: `data/experiment/esq_v3_miembros/esquema_v3_clases.json` (versión 3.0, sha256 `dad88cc92afc53e922989cad84eb68b2ef142b66c221f2a566e7fb5da1bcfd36`); política de cuarentena: **flaggeada**
- esqueleto de referencia (T4): `/Users/agustinavidelarivero/INGENIERIA IA/TESIS/bcra-regulatory-kg/data/experiment/grafo_v2/reensamblado_v3/kg.json` sha256 `26fac8b49f6c08c1aa364b47273d36958d831f240d4e6b4ee7700b6a0bff3571`
- retriever: GraphIndex de data/experiment/evaluacion/harness.py (importado; sha256 `fd267e833866f86850e43130e627b08d78e05523b97484696de0ab0c8c9fba9e`), loader.load_graph_from_path adapter_key=None
- partición declarada: {'items': 46, 'convertibles': 19, 'con_condicion': 23, 'no_convertibles': 4, 'retriever': 15, 'por_grupo': {'i-BKL': 12, 'i-RT': 12, 'ii': 12, 'iii': 10}}

## Resumen: 46 ítems — resuelto 11 / persiste 22 / no_aplicable 13
Ranks sellados (retriever in-memory): consultas que coinciden con el sellado 3/19; objetivos 17/63; objetivos en ventana declarada 11; objetivos ausentes 41.

| Id | Grupo | Convertibilidad | Retr. | Forma | Estado | Detalle |
|---|---|---|---|---|---|---|
| BKL-0017 | i-BKL | convertible | sí | F1 + F4 ×2 + F5 ×3 (limite 10) | **persiste** | sin Obligacion anclada en cla 1.1 con la frase del criterio general |
| BKL-0006 | i-BKL | convertible | no | F3 (montos de la tabla) + F4 (exceptua → restantes) + F5 ×2 informativo (limite 10 / 13) | **no_aplicable** | sin nodos anclados en cap 1.2 con «exigencia básica»: tabla del 1.2 no extraída |
| BKL-0023 | i-BKL | convertible | no | F3 (properties.umbral) | **no_aplicable** | ninguna Restriccion anclada en cap 1.2 con la oración de compañías financieras |
| BKL-0019 | i-BKL | con condición | sí | F4 ×8 (subclase_de si laudada / padre_sugerido si flaggeada) + F4 ausente (excluida, laudada) | **no_aplicable** | ninguno de los 8 sujetos propuestos está en el grafo (por label ni por id de cuarentena) |
| BKL-0004 | i-BKL | convertible | sí | F1 ×9 + F4 (8 regula + 9 establecida_en) + F5 ×8 (7 consultas + proxy RT-C5-4; limite 10) | **persiste** | nodos 0/9 -> N1@6.5:0 N2@6.5.1:0 N3@6.5.2:0 N4@6.5.2.1:0 N5@6.5.2.2:0 N6@6.5.2.3:0 N7@6.5.3:0 N8@6.5.4:0 N9@6.5.5:0; sin N1: aristas no evaluables; objetivos en ventana=0/30 |
| BKL-0003 | i-BKL | convertible | sí | F1 + F4 ×2 + F4 ausente (a Sujeto) + F5 ×11 (N1 + controles rol/pnfc; limite 10) | **persiste** | Excepcion=0 []; objetivos en ventana=8/16 |
| BKL-0005 | i-BKL | convertible | sí | F3 (dos calificadores en descripcion) + F5 ×3 (limite 10) | **no_aplicable** | sin portador: ninguna Obligacion anclada en ric 7.1 con «para el cálculo del importe correspondiente al mes n» |
| BKL-0007 | i-BKL | convertible | no | = BKL-0017 (sin test propio) | **persiste** | = BKL-0017 (cerrada por referencia; defecto confirmado, no corrección aplicada): sin Obligacion anclada en cla 1.1 con la frase del criterio general |
| BKL-0026 | i-BKL | no convertible | no | ninguna (no convertible) | **no_aplicable** | no convertible: conducta del agente (paráfrasis invertida del verbatim con ver_nodo byte-idéntico, RT-C6-1 vs RT-C6-2, 3/3 en N=3); no es observable con una comprobación determinística sobre un kg.json (inventario_B21… |
| BKL-0027 | i-BKL | no convertible | no | ninguna (no convertible) | **no_aplicable** | no convertible: conducta del agente (pidió ver_vecinos salientes de un rol que solo tiene miembro_de entrantes, RT-C6-3); la estructura del rol se testea en RT-C6-3 (inventario_B21_fase1.md:108). defecto confirmado, n… |
| BKL-0028 | i-BKL | con condición | no | F1 sobre el catálogo parametrizado (ids «del exterior» separados; sin alias del exterior en los domésticos) + F1 en el grafo | **persiste** | catálogo v3: alias «del exterior» en ['Sujeto_entidad_financiera', 'Sujeto_banco', 'Sujeto_entidad_cambiaria']; ids separados []; presentes en el grafo []. defecto confirmado, no corrección aplicada. |
| BKL-0029 | i-BKL | con condición | no | F4 (miembro_de del rol de convca → id nuevo del catálogo) | **persiste** | ids candidatos en catálogo=[]; miembro_de del rol=['Sujeto_entidad_financiera']; residuo colectivo_operativo_sin_id=True. defecto confirmado, no corrección aplicada. |
| RT-C5-1 | i-RT | con condición | sí | F3 (valor: cinco categorías en N1) | **persiste** | sin N1 (Obligacion del 6.5 con el encabezado): el gold no está en el grafo |
| RT-C5-2 | i-RT | con condición | sí | F3 (valor: tres situaciones en N3) | **persiste** | sin N3 (nodo del 6.5.2 «seguimiento especial»): el gold no está en el grafo |
| RT-C5-3 | i-RT | con condición | sí | F3 (valor: «antes de los 60 días … mora» en N5) | **persiste** | sin N5 (nodo del 6.5.2.2): el gold no está en el grafo |
| RT-C5-4 | i-RT | convertible | sí | F3 (valor: primera vez / primera cuota / única vez en N6) | **persiste** | sin N6 (nodo del 6.5.2.3): el gold no está en el grafo |
| RT-C5-5 | i-RT | convertible | no | F2 (nodo con «riesgo medio» anclado en 7.2 exacto) + F3 (N1 sin niveles del 7.2) | **no_aplicable** | sin nodos con punto exactamente 7.2 de Clasificación: el proxy falla por ancla, no por contenido (inventario_B21_fase1.md:267, §5.7; decisión 5) |
| RT-C6-1 | i-RT | con condición | sí | F3 (valor en N1) | **persiste** | RT-C6-1: sin Excepcion anclada en pro 1.1.2.5 con «mutuales o cooperativas» |
| RT-C6-2 | i-RT | con condición | sí | F3 (valor en N1; = RT-C6-1) | **persiste** | RT-C6-2 (= RT-C6-1 en la parte de valor): sin Excepcion anclada en pro 1.1.2.5 con «mutuales o cooperativas» |
| RT-C6-3 | i-RT | con condición | sí | F4 ×n (miembro_de entrantes = miembros del rol en el catálogo) | **resuelto** | miembro_de entrantes=7 esperados(catálogo)=7; faltan=[] sobran=[] |
| RT-C6-4 | i-RT | convertible | no | F4 (emisoras --miembro_de--> rol) + F4 ausente (N1 ↔ Sujeto) | **resuelto** | emisoras→rol=True; N1=ausente (sub-check no aplicable) |
| RT-C7-1 | i-RT | convertible | sí | F3 (valor: ambos calificadores en el portador) | **no_aplicable** | RT-C7-1: sin portador del 7.1 (Obligacion con «para el cálculo del importe correspondiente al mes n») |
| RT-C7-2 | i-RT | convertible | sí | F3 (valor: calificador de la RPC) | **no_aplicable** | RT-C7-2: sin portador del 7.1 (Obligacion con «para el cálculo del importe correspondiente al mes n») |
| RT-C7-3 | i-RT | convertible | sí | F3 (valor: calificador de la franquicia) | **no_aplicable** | RT-C7-3: sin portador del 7.1 (Obligacion con «para el cálculo del importe correspondiente al mes n») |
| T1 | ii | convertible | no | F2 + F3 | **persiste** | anclados_3_9=0 puntos=[] con_usd_200=0 |
| T2 | ii | convertible | no | F1 (conteo) + F2 (conteo de puntos) | **persiste** | nodos_separados_ext=0 puntos_distintos=[] |
| T3 | ii | convertible | no | F2 + F3 | **persiste** | anclados_1_1_2_5=0 con_salvedad=0 de_los_cuales_excepcion=0 |
| T4 | ii | con condición | no | F1 + F4 (paridad de esqueleto contra --esqueleto-referencia, decisión 8) | **persiste** | esqueleto_esperados=70 faltan_nodos=0 aristas_esqueleto_en_grafo=117 (excluidas cuarentena_laudada=0) referencia=82 faltan_triplas=0 |
| T5 | ii | con condición | no | F4 + F3 (properties.evidencia) | **persiste** | n_muestra=30 fallas=30 (presente_con_otra_evidencia=0, ausente=30) |
| T6 | ii | con condición | no | F1 | **persiste** | n=5 fuera_del_esperado=['TextoOrdenado_ctacte_pdf', 'TextoOrdenado_docvig_pdf', 'TextoOrdenado_lingob_pdf', 'TextoOrdenado_pagjub_pdf', 'TextoOrdenado_polcre_pdf'] faltan=['TextoOrdenado_to_capitales_minimos_actual_pd… |
| T7 | ii | con condición | no | F3 + F4 + F4 ausente (política de cuarentena, decisión 3) | **persiste** | politica=flaggeada propuestos=11 aristas_padre_sugerido=11 malos=0 {} fuera_catalogo_no_propuestos=2 |
| I1 | ii | no convertible | no | ninguna (no convertible) | **no_aplicable** | no convertible: conservación de nodos Σ pre-merge − merges = finales exige los grafos pre-merge (salida/<to>/grafo_<to>.json) y los conteos de merge, que solo existen para la cadena r1 (inventario_B21_fase1.md:135) |
| I2 | ii | no convertible | no | ninguna (no convertible) | **no_aplicable** | no convertible: conservación de aristas, ídem I1 (inventario_B21_fase1.md:136) |
| I3 | ii | convertible | no | F1 (conteo: unicidad de ids y de triplas) | **resuelto** | nodes=1979 edges=3983 ids_duplicados=0 triplas_duplicadas=0 |
| I4 | ii | convertible | no | F4 (cero colgantes) | **resuelto** | colgantes=0 |
| I5 | ii | convertible | no | F2 (al menos una provenance por nodo y arista, adaptador) | **resuelto** | nodos_sin=0 aristas_sin=0 |
| E4-a1 | iii | con condición | no | F1 ausente (ningún propuesto residual resoluble por label_exacto) | **resuelto** | propuestos=11 con candidato label_exacto=0 resolubles no resueltos=0 [] |
| E4-a2 | iii | con condición | no | F1 ausente (alias_exacto) | **resuelto** | propuestos=11 con candidato alias_exacto=0 resolubles no resueltos=0 [] |
| E4-a3 | iii | con condición | no | F1 ausente (id_slug; e2_lib.slugify_full importado) | **resuelto** | propuestos=11 con candidato id_slug=0 resolubles no resueltos=0 [] |
| E4-a4 | iii | con condición | no | F1 ausente (label_singularizado) | **resuelto** | propuestos=11 con candidato label_singularizado=0 resolubles no resueltos=0 [] |
| E4-a5 | iii | con condición | no | F1 ausente (alias_en_parentesis) + F3 (padre_sugerido) | **resuelto** | propuestos=11 con candidato alias_en_parentesis=0 resolubles no resueltos=0 []; propuestos con padre_sugerido=11 |
| E4-a6 | iii | con condición | no | F1 ausente (claves ambiguas / alias_resueltos que re-resuelven sin ambigüedad) | **resuelto** | claves ambiguas del índice=4; propuestos residuales con motivo ambiguo=0/11; alias_resueltos re-resueltos=1/1 malos=[] |
| E4-a7 | iii | con condición | no | F3 (cuarentena=true normalizada) + F1 (todo Sujeto no propuesto ∈ catálogo) | **persiste** | propuestos=11 sin_cuarentena_true=0 con_id_de_catalogo=0 sujetos_fuera_catalogo_no_propuestos=2 |
| E4-a8 | iii | con condición | no | F3 (alias_resueltos en ids de catálogo) + F1 ausente + F4 ausente; parte pre-E4 no_aplicable | **persiste** | alias_resueltos en 0/3 ids de catálogo; propuestos resueltos aún presentes=0; provenances acumuladas y dedup: no observables sin el grafo pre-E4 (no_aplicable parcial) |
| E4-b | iii | con condición | no | F1 (= T6) + F3 (properties.archivo ∈ archivos de E0) | **persiste** | TextoOrdenado=5; con properties.archivo en el conjunto de E0: 0/5; fuera=[('TextoOrdenado_ctacte_pdf', 'ctacte.pdf'), ('TextoOrdenado_docvig_pdf', 'docvig.pdf'), ('TextoOrdenado_lingob_pdf', 'lingob.pdf'), ('TextoOrde… |
| E4-c | iii | con condición | no | ninguna directa (no observable sobre un kg.json) | **no_aplicable** | solo observable con el registro de conflictos (salida_r1/e4_conflictos.json) o los grafos pre-E4: los conflictos de properties no se persisten en el kg.json; el proxy débil (un solo valor de materia/version por TextoO… |

## Regresión contra la fixture
Sin `--esperado`: no se computa regresión.

## Consultas de rank (por ítem)
- [BKL-0004] «niveles clasificación deudores cartera comercial» (limite pedido 10): C5.N1: rank=None sellado=1 limite=10 ≠ [objetivo AUSENTE] | C5.N7: rank=None sellado=4 limite=10 ≠ [objetivo AUSENTE] | C5.N9: rank=None sellado=5 limite=10 ≠ [objetivo AUSENTE] | C5.N2: rank=None sellado=6 limite=10 ≠ [objetivo AUSENTE] | C5.N3: rank=None sellado=8 limite=10 ≠ [objetivo AUSENTE]
- [BKL-0004] «seguimiento especial deudores» (limite pedido 10): C5.N1: rank=None sellado=1 limite=10 ≠ [objetivo AUSENTE] | C5.N4: rank=None sellado=3 limite=10 ≠ [objetivo AUSENTE] | C5.N6: rank=None sellado=4 limite=10 ≠ [objetivo AUSENTE] | C5.N5: rank=None sellado=5 limite=10 ≠ [objetivo AUSENTE] | C5.N3: rank=None sellado=6 limite=10 ≠ [objetivo AUSENTE]
- [BKL-0004] «punto 6.5 niveles clasificación» (limite pedido 10): C5.N1: rank=None sellado=1 limite=10 ≠ [objetivo AUSENTE] | C5.N7: rank=None sellado=2 limite=10 ≠ [objetivo AUSENTE] | C5.N9: rank=None sellado=3 limite=10 ≠ [objetivo AUSENTE] | C5.N2: rank=None sellado=4 limite=10 ≠ [objetivo AUSENTE] | C5.N8: rank=None sellado=5 limite=10 ≠ [objetivo AUSENTE] | C5.N3: rank=None sellado=6 limite=10 ≠ [objetivo AUSENTE]
- [BKL-0004] «situaciones que integran el seguimiento especial» (limite pedido 10): C5.N3: rank=None sellado=7 limite=10 ≠ [objetivo AUSENTE]
- [BKL-0004] «cinco categorías cartera comercial» (limite pedido 10): C5.N1: rank=None sellado=1 limite=10 ≠ [objetivo AUSENTE] | C5.N7: rank=None sellado=7 limite=10 ≠ [objetivo AUSENTE] | C5.N9: rank=None sellado=8 limite=10 ≠ [objetivo AUSENTE] | C5.N2: rank=None sellado=9 limite=10 ≠ [objetivo AUSENTE] | C5.N4: rank=None sellado=10 limite=10 ≠ [objetivo AUSENTE]
- [BKL-0004] «en negociación o con acuerdos de refinanciación» (limite pedido 10): C5.N5: rank=None sellado=1 limite=10 ≠ [objetivo AUSENTE] | C5.N3: rank=None sellado=2 limite=10 ≠ [objetivo AUSENTE]
- [BKL-0004] «situación normal cartera comercial» (limite pedido 10): C5.N2: rank=None sellado=1 limite=10 ≠ [objetivo AUSENTE] | C5.N1: rank=None sellado=2 limite=10 ≠ [objetivo AUSENTE] | C5.N4: rank=None sellado=3 limite=10 ≠ [objetivo AUSENTE] | C5.N6: rank=None sellado=4 limite=10 ≠ [objetivo AUSENTE] | C5.N5: rank=None sellado=5 limite=10 ≠ [objetivo AUSENTE]
- [BKL-0004] «reclasificación en tratamiento especial refinanciación» (limite pedido 10): C5.N6: rank=None sellado=4 limite=10 ≠ [objetivo AUSENTE]
- [BKL-0003] «asociación mutual financiaciones proveedor no financiero crédito» (limite pedido 10): C6.N1: rank=None sellado=1 limite=10 ≠ [objetivo AUSENTE] | C6.rol: rank=None sellado=None limite=10 = | C6.pnfc: rank=1 sellado=2 limite=10 ≠
- [BKL-0003] «sujeto obligado protección usuarios servicios financieros» (limite pedido 10): C6.N1: rank=None sellado=1 limite=10 ≠ [objetivo AUSENTE] | C6.rol: rank=2 sellado=5 limite=10 ≠ | C6.pnfc: rank=7 sellado=None limite=10 ≠
- [BKL-0003] «proveedor no financiero crédito» (limite pedido 10): C6.N1: rank=None sellado=None limite=10 = [objetivo AUSENTE] | C6.rol: rank=None sellado=None limite=10 = | C6.pnfc: rank=1 sellado=1 limite=10 =
- [BKL-0003] «asociación mutual» (limite pedido 10): C6.N1: rank=None sellado=1 limite=10 ≠ [objetivo AUSENTE] | C6.rol: rank=None sellado=None limite=10 = | C6.pnfc: rank=None sellado=None limite=10 =
- [BKL-0003] «definición proveedor no financiero crédito PNFC» (limite pedido 10): C6.N1: rank=None sellado=None limite=10 = [objetivo AUSENTE] | C6.rol: rank=None sellado=None limite=10 = | C6.pnfc: rank=1 sellado=1 limite=10 =
- [BKL-0003] «proveedor no financiero crédito comercios empresas personas jurídicas» (limite pedido 10): C6.N1: rank=None sellado=None limite=10 = [objetivo AUSENTE] | C6.rol: rank=None sellado=None limite=10 = | C6.pnfc: rank=1 sellado=1 limite=10 =
- [BKL-0003] «exclusión excluido no alcanzado no incluido sujeto obligado» (limite pedido 10): C6.N1: rank=None sellado=4 limite=10 ≠ [objetivo AUSENTE] | C6.rol: rank=6 sellado=None limite=10 ≠ | C6.pnfc: rank=4 sellado=None limite=10 ≠
- [BKL-0003] «mutuales cooperativas sujeto obligado protección usuarios» (limite pedido 10): C6.N1: rank=None sellado=1 limite=10 ≠ [objetivo AUSENTE] | C6.rol: rank=1 sellado=2 limite=10 ≠ | C6.pnfc: rank=None sellado=None limite=10 =
- [BKL-0003] «excepción asociaciones mutuales cooperativas» (limite pedido 10): C6.N1: rank=None sellado=1 limite=10 ≠ [objetivo AUSENTE] | C6.rol: rank=None sellado=None limite=10 = | C6.pnfc: rank=None sellado=None limite=10 =
- [BKL-0003] «cooperativa que otorga financiaciones protección de usuarios» (limite pedido 10): C6.N1: rank=None sellado=1 limite=10 ≠ [objetivo AUSENTE] | C6.rol: rank=1 sellado=5 limite=10 ≠ | C6.pnfc: rank=None sellado=None limite=10 =
- [BKL-0003] «asociaciones mutuales proveedores no financieros de crédito» (limite pedido 10): C6.N1: rank=None sellado=1 limite=10 ≠ [objetivo AUSENTE] | C6.rol: rank=None sellado=None limite=10 = | C6.pnfc: rank=1 sellado=2 limite=10 ≠
