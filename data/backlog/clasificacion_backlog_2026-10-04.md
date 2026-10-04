# Recuento del backlog (data/backlog/backlog.jsonl), 04/10/2026

39 entradas y 53 eventos. El estado es el último `estado` informado para cada id.

| BKL | Qué es | Estado en el archivo | Clase hoy | Ancla |
|---|---|---|---|---|
| BKL-0001 | ausencia en CapMin 2.8.3.3 (grafo v2) | triaged (retriage: resuelta por v3) | e | resuelta por v3 según el retriage; cierre formal contra el PDF pendiente y sin unidad. En KG-Tanda0-Diez-r2a hay 8 nodos anclados en cap::2.8.3.3, sin leer contra el PDF |
| BKL-0002 | ausencia en Exterior 3.5.3 (grafo v2) | triaged (retriage: resuelta por v3) | e | igual que BKL-0001; 35 nodos anclados en ext::3.5.3 y sus hijos en r2a |
| BKL-0003 | salvedad de mutuales, Protección 1.1.2.5 | verificado | b | cerrada en KG-Refinado (C6, retest 38/38). En r2a persiste: la Excepcion está, sin `exceptua` y sin la cláusula. Verifica: suite BKL-0003 y RT-C6-5; caso fijo pro::1.1.2.5 de P4 |
| BKL-0004 | enumeración del 6.5 de Clasificación | verificado | b | cerrada en KG-Refinado (C5). En r2a persiste: 8 de 9 nodos, 0 de 8 `regula`; RT-C5-1, 2 y 4. Sin corrección dirigida: si persiste en r2b, va al estado esperado que sella la autora (U-REEXT-T0, T1.5) |
| BKL-0005 | calificadores del 7.1 de RegInf | verificado | a | C7 (retest 27/27); suite «resuelto» en r2a (fixture, KG-Tanda0-Diez-r2a) |
| BKL-0006 | tabla invertida de cap::1.2 | verificado | b | cerrada en KG-Refinado (C2); reaparece en la generación 3 (nota del 30/09). Verifica: tablero de correcciones `:62`, suite BKL-0006, caso fijo cap::1.2 de P4; e0-r2 ya serializa la tabla |
| BKL-0007 | criterio general 1.1 de Clasificación (cerrada por referencia a 0017) | verificado | c | en r2a el nodo y sus aristas están; persiste solo por alcanzabilidad (2 de 3 consultas en ventana). Destino: búsqueda, A1.8 / U-NAV-DISENO, que no lo nombra |
| BKL-0008 | alcanzabilidad de tres restricciones de Exterior | triaged | c | plan `:380`: «alcanzabilidad → A1»; laudo de B2.4 pendiente; U-NAV-DISENO no lo nombra. En r2a el contenido está (juegos de azar 1 nodo, criptoactivos 6) |
| BKL-0009 | sujeto: descenso (CapMin 2.5) | triaged | b | remedio en el prefijo r2b (R15) y en código (R1), diseño de U-PROMPT-R2 §6.2 (`20b7f60`). Verifica el mecanismo: tablero `:65`, LN-3 y LN-4. Sin control por ítem; laudo de B2.4 pendiente (X9) |
| BKL-0010 | sujeto: descenso (Exterior 14.5) | triaged | b | ídem BKL-0009 |
| BKL-0011 | sujeto: descenso (RegInf 3.1) | triaged | b | ídem BKL-0009 |
| BKL-0012 | sujeto: término de otro TO (Exterior 13.4) | triaged | b | ídem BKL-0009 (R15) |
| BKL-0013 | sujeto: «las entidades» estrechado, 18 aristas de Exterior | triaged | b | ídem BKL-0009 (R15); el diseño declara que el código no alcanza: con R3 gana la sugerencia del modelo |
| BKL-0014 | sujeto: clase forzada (Exterior 14.1) | triaged | b | ídem BKL-0009 (R15) |
| BKL-0015 | sujeto: clase forzada (Exterior 3.17) | triaged | b | ídem BKL-0009 (R15) |
| BKL-0016 | sujeto: «los clientes» → exportador (Exterior 3.18) | triaged | b | ídem BKL-0009 (R1 en código) |
| BKL-0017 | criterio general 1.1 de Clasificación restaurado | verificado | c | cerrada en KG-Refinado (C1). En r2a, como BKL-0007: contenido presente, persiste por alcanzabilidad. Destino: A1.8 / U-NAV-DISENO |
| BKL-0018 | deslinde de régimen 7.2 contra 6.5 de Clasificación | triaged | e | plan `:380`: «anotación de régimen», sin unidad; RT-C5-5 da no_aplicable en la generación 3 |
| BKL-0019 | 8 `subclase_de` desde la cuarentena | verificado | d | cerrada en KG-Refinado (C4). En la generación 3 rige la política de cuarentena (`padre_sugerido`, sin `subclase_de`): la suite lo da «persiste» y así está sellado en la fixture de r2a (1 de 3 presentes, de 8); T7 resuelto. El crecimiento desde la cuarentena queda en U-RERESOL-CAT |
| BKL-0020 | propuesto «originante» sin padre | triaged | c | en r2a «originante» está en cuarentena (3 filas). Destino: regla de crecimiento del catálogo, R1 de U-RERESOL-CAT |
| BKL-0021 | propuesto «entidad nominada por el importador» sin padre | triaged | e | 0 filas en el registro de r2a; sin unidad. No reaparece o no se midió |
| BKL-0022 | huérfano léxico «grupo 2» | triaged | c | tools v2 lo dejan alcanzable (A1.2, `9141351`; nota `5078f51`); 0 filas «grupo 2» en r2a. Destino: A1.8 / U-NAV-DISENO |
| BKL-0023 | umbral de compañías financieras (rastro de BKL-0006) | verificado | b | cerrada en KG-Refinado (C3). En r2a la suite lo da «persiste» (bancos con 2.500). Se verifica con BKL-0006 |
| BKL-0024 | Exterior 3.9 ausente (run_3) | triaged | a | resuelto por el pipeline: T1 «resuelto» en r2a (18 nodos anclados en 3.9, uno con USD 200). El archivo no tiene el cierre |
| BKL-0025 | definición de usuario, Protección 1.1.1 (run_3) | triaged | a | resuelto por el pipeline: 3 Definicion ancladas en pro::1.1.1 en r2a. Sin ítem en la suite y sin cierre en el archivo |
| BKL-0026 | el agente invierte la norma con el nodo correcto a la vista | verificado | d | defecto confirmado 3 de 3, no corregible en el grafo; es el hallazgo «anclado no es correcto» (`docs/tablero.md`, H3; plan `:235`). A3.1 quedó descartada (`:349`) |
| BKL-0027 | vecinos solo salientes en un rol con entrantes | verificado | c | tools v2 lo sacan del espacio de acciones (A1.2, `9141351`). Destino: A1.8 / U-NAV-DISENO (tablero de correcciones `:57`) |
| BKL-0028 | alias «del exterior» en ids domésticos | verificado | a | catálogo r2 (`bd2122d`); suite «resuelto» en r2a. Residuo: la re-adjudicación del miembro de ctacor, en U-REEXT-T0 (nota del 01/10) |
| BKL-0029 | rol de convca sin su colectivo | verificado | a | catálogo r2 (`bd2122d`); suite «resuelto» en r2a (`miembro_de` → titular de cuenta corriente en el BCRA) |
| BKL-0030 | reintento por corte y partición | triaged | b | implementado en `26d274d` (selftest_r4 26/26). Cierre: cero errores definitivos por corte en la corrida. Verifica: tablero `:61`, contadores de T2 de U-REEXT-T0 |
| BKL-0031 | detector de casi duplicados y fusión de forma | triaged | e | paso 1 hecho (`26d274d`): 2.429 pares en diez, sin fundir. Pasos 2 (muestra adjudicada) y 3 (regla), sin unidad; checklist R4 espera decisión |
| BKL-0032 | polaridad invertida, docvig::3.3::cierre | triaged | b | regla R5 y ejemplo R24 del prefijo r2b (`20b7f60`, §6.1). Cierre sobre r2b; el borrador de U-REEXT-T0 no lo lista como control |
| BKL-0033 | sujeto de un acto ajeno, ctacte::7.3.1.5 | triaged | b | regla R15 del prefijo r2b. Ídem BKL-0032 |
| BKL-0034 | sin sujeto de nivel órgano, lingob::2.3.2::intro | triaged | b | L-ESQ-R2 §7.3, opción (ii); los tres ids están en el catálogo r2. En r2a las 3 Obligaciones siguen hacia entidad financiera. Verifica: entrada por id nuevo, U-REEXT-T0 T1.4.d |
| BKL-0035 | Obligacion de solo anuncio, ctacte::8.3 y 8.4 | triaged | b | regla 1 del prefijo r2b, NOTA de E3 y guarda. Verifica: U-REEXT-T0 T3.d |
| BKL-0036 | calificador amputado, lingob::2.3.2.2 | triaged | b | regla R3 y regla 8 del prefijo r2b. Ídem BKL-0032 |
| BKL-0037 | ids de chunk repetidos | triaged | a | regla L y runner que se detiene (`924ef4d`; selftest_r2 18/18). Recomputado sobre los 152 con e0-r2: 0 repetidos, 69 desambiguados. La partición oficial es de U-SEG-OFICIAL (checklist, condición 7) |
| BKL-0038 | `limita` desde una Restricción «prohibicion» | nuevo | b | control en código (`eb277ce`): 4 aristas marcadas «incoherente» en los dos r2a. Falta el conteo en r2b y la lectura de los 3 chunks, sin unidad |
| BKL-0039 | Obligacion de solo anuncio, ctacte::6.4.7::intro | triaged | b | como BKL-0035. Verifica: U-REEXT-T0 T3.d |

Por clase: (a) cerrado y verificado: 6; (b) resuelto por r2, a verificar en U-REEXT-T0: 20; (c) asignado a una unidad posterior: 6; (d) declarado como límite: 2; (e) SIN ASIGNAR: 5. Total 39.
Por estado: {"triaged": 26, "verificado": 12, "nuevo": 1}.

## Los cinco sin asignar, con propuesta

| BKL | Propuesta |
|---|---|
| BKL-0001 y BKL-0002 | Cierre en el laudo de B2.4 (checklist X9). Con un test determinístico por punto en la suite (cap::2.8.3.3 y ext::3.5.3), sumado en T1 de U-REEXT-T0, como se hizo con BKL-0024 (T1). |
| BKL-0018 | Laudo de B2.4. Es una anotación acoplada a BKL-0004: si BKL-0004 sigue en «persiste» en r2b, se decide junto con él. |
| BKL-0021 | Laudo de B2.4: cerrar como «no reaparece en la generación 3» si el registro de r2b tampoco trae la mención; si la trae, a la regla de crecimiento de U-RERESOL-CAT, como BKL-0020. |
| BKL-0031 | Pasos 2 y 3 a la revisión de fusionados posterior a U-REEXT-T0 (plan `:400`): la misma sesión de lectura decide la regla de fusión en los dos sentidos (lo que se junta de más y lo que queda duplicado). El detector se corre sobre los grafos r2b en T3 de U-REEXT-T0, como dato. |

## Lo que tendría que estar resuelto antes de la tanda 1 y no lo está

1. El laudo de B2.4 (checklist X9, que espera decisión de la autora). Los ocho ítems de asignación de sujeto
   (BKL-0009 a BKL-0016) tienen remedio en el prefijo r2b y en el código, pero ningún control los lee uno
   por uno. La tanda 1 lleva esa asignación a 20 documentos nuevos.
2. Controles que faltan en el borrador de U-REEXT-T0 para ítems de clase (b): las condiciones de cierre de
   BKL-0032, BKL-0033 y BKL-0036, leídas contra su chunk (hoy solo están BKL-0035 y BKL-0039, en T3.d); el
   conteo de BKL-0038 sobre r2b y la lectura de sus 3 chunks; la lectura de los ocho patrones de BKL-0009 a
   BKL-0016; y la re-adjudicación del miembro de ctacor (BKL-0028).
3. BKL-0004: persiste en r2a sin corrección dirigida. Si persiste en r2b, tiene que quedar en el estado
   esperado que la autora sella antes del gate, o declarado en el tablero.
4. BKL-0037: el código está, pero la partición oficial con e0-r2 es de U-SEG-OFICIAL, que sigue en borrador.
5. BKL-0030: su condición de cierre es cero errores definitivos por corte en la corrida. En la tanda 0 es
   alcanzable; en la tanda 1 la contradicen las 8 unidades de la clase A, que hoy quedaron en S0 de
   U-SEG-OFICIAL, punto 6.
6. BKL-0031: la decisión del paso 2 (checklist R4). No bloquea: una regla de fusión se re-aplica en código
   sobre el grafo acumulado.

## Estados del archivo que contradicen lo que pasó

Marcados abiertos y ya resueltos o implementados:
- BKL-0024 y BKL-0025: `triaged`; resueltos por el pipeline (ya anotado en el plan `:376`, cierre pendiente).
- BKL-0030: `triaged`; implementado en `26d274d`. Sin evento.
- BKL-0037: `triaged`; implementado en `924ef4d` y medido en 0. Sin evento.
- BKL-0038: `nuevo`, nunca pasó a `triaged`; decidido el 30/09 e implementado en `eb277ce`.
- BKL-0031: `triaged`; el paso 1 está hecho en `26d274d`. Sin evento.
- BKL-0034: `triaged`; decidido en L-ESQ-R2 §7.3 y aplicado al catálogo r2. Sin evento (BKL-0028 sí lo tiene).
- BKL-0032, BKL-0033 y BKL-0036: su campo `propuesta` dice «fuera de r2» y su `artefacto_objetivo` apunta al
  prefijo v3 sellado; entraron al ciclo el 30/09 (checklist X5) y su remedio está en el prefijo r2b.
- BKL-0001 y BKL-0002: `estado` triaged con `estado_retriage` resuelta_por_v3.

Marcados cerrados y hoy abiertos:
- BKL-0003, BKL-0004, BKL-0007, BKL-0017, BKL-0019 y BKL-0023: `verificado` sobre KG-Refinado; en la
  generación 3 la suite los da «persiste». Solo BKL-0006 tiene la nota de reaparición.
- BKL-0026 y BKL-0027: `verificado` quiere decir «defecto confirmado», no corregido.

Documentos desactualizados:
- `docs/tablero.md:308-319` cuenta 27 entradas (10 verificado, 2 resueltas por v3, 15 triaged). Con su misma
  regla hoy son 39: 12 verificado, 2 resueltas por v3, 24 triaged y 1 nuevo.
- Plan `:380` (B2.4): «15» con un desglose que suma 16 (ya anotado en `:376`); las entradas de sujeto son
  ocho, no nueve (diseño de U-PROMPT-R2, §6.2).
