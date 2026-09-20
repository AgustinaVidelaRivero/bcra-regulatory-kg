# U-FIG-PROC-V — verificación de procedencia del mini-grafo de la figura del proceso

Fecha de la verificación: 18/09/2026. Solo lectura; este archivo es la única
escritura de la unidad. Costo de API: USD 0. Toda consulta corre desde la raíz
del repo con `PYTHONDONTWRITEBYTECODE=1`.

Objeto: `docs/tesis/figuras/figura_proceso_extraccion.png` (sin trackear en git:
`git status --short docs/tesis/figuras/` → `??`) y su generador
`generar_figura_proceso_extraccion.py`. El panel «Grafo» dibuja tres nodos
(«Restricción / punto 2.5.1», «Operación / punto 2.5.2», «Obligación / punto
3.4.2») y tres aristas: Restricción 2.5.1 —limita→ Operación 2.5.2, Operación
2.5.2 —requiere→ Obligación 3.4.2 y Restricción 2.5.1 —remite a→ Obligación 3.4.2.

## 0. Resultado en una línea

Las dos firmas de extracción están admitidas por la matriz congelada y la
arista de remisión corresponde al `rol_fuente = referencia_cruzada` de
`r1_referencias.py`; pero **ninguna de las tres aristas dibujadas existe en el
grafo**: no hay ningún nodo de tipo Restricción con procedencia en el punto
2.5.1 en ninguno de los cinco documentos. Los tres rótulos fueron elegidos a
mano y el propio generador los declara ficticios. El patrón completo sí existe
en el grafo (cinco cadenas, todas en el TO de Exterior y Cambios, sección 9.3);
el subgrafo de dividendos tiene el patrón sin la arista de remisión. Detalle en
§4. **FRENO**: la mesa elige el trío y recién entonces se redibuja.

## 1. Anclas y hashes

| Artefacto | Ruta | sha256 | Coincide con el mandato |
|---|---|---|---|
| `prompt_congelado.py` (archivo) | `data/experiment/esq/code/prompt_congelado.py` | `a5a4ba330a02b2b8ce885716e242dafabb84f62463d25c046dc6ff7d40f40710` | NO como sha de archivo (ver nota) |
| Texto del prefijo congelado que produce ese módulo | `pc.PREFIJO_SHA256_CONGELADO` | `e69feaaa04779bd6347cc9e3974d2c1749519f1230e70a0459e66f46517cd720` (25.652 chars, hash system+tools `1be8304e3d77`) | SÍ |
| `kg.json` | `data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json` | `0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a` | SÍ |
| Generador | NO está en el repo (ver §3) | `76aaedb1bea2574a8dd47692d271230d34f19d1da87c53bded60abdc2a695332` | coincide con el `manifest.txt` del paquete U-FIG-PROC |
| `control_contenido.md` | NO está en el repo (ver §3) | `80b71402e6a0bc032fc944ef9c94d56670337fb4b518a291f19d63b5df754959` | coincide con ese manifest |
| PNG en el repo | `docs/tesis/figuras/figura_proceso_extraccion.png` | `45b805d26e40538d8ee919935f1b8d60fc10cc4a85d74af2828fd62e68fd535f` | byte-idéntico al PNG del paquete U-FIG-PROC |
| Textos de puntos terminales (ext) | `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_ext.json` | `cbcd1a86f55ea49110610587873881c68c13a9d7975d3fd5e465f26302be2d12` | — |
| Estructura (unidades no terminales, ext) | `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/estructura_ext.json` | `0b0137d58decb66d66bbb6f60d0192071d2b2ee0c819ee95658f9f31881c6d53` | — |

Nota sobre `e69feaaa…`: el mandato lo llama «sha» de `prompt_congelado.py`. No es
el sha del archivo: es el sha256 del TEXTO del prefijo congelado que ese módulo
construye (`data/experiment/esq/laudo_esquema_congelado.md:137`;
`docs/tesis/mapa_fuentes_cap_esquema.md:270`). Lo recomputé:

```
PYTHONDONTWRITEBYTECODE=1 python3 -c "import sys;sys.path.insert(0,'data/experiment/esq/code');sys.path.insert(0,'data/experiment/reextraccion_v2/e1_extractor');sys.path.insert(0,'data/experiment/grafo_v2/code');import prompt_congelado as pc;print(pc.PREFIJO_SHA256_CONGELADO,pc.PREFIJO_HASH_CONGELADO,len(pc.PREFIJO_SISTEMA_CONGELADO))"
→ e69feaaa04779bd6347cc9e3974d2c1749519f1230e70a0459e66f46517cd720 1be8304e3d77 25652
```

El archivo en HEAD tiene el mismo sha que el de trabajo
(`git show HEAD:data/experiment/esq/code/prompt_congelado.py | shasum -a 256` →
`a5a4ba33…`), último commit que lo toca: `2593d4d`.

## 2. Ítem 1 — matriz y arista de remisión

### 2.a Firmas de extracción

`DOMAIN_RANGE_CONGELADO` (`data/experiment/esq/code/prompt_congelado.py:97-99`)
copia `DOMAIN_RANGE_V2` (`data/experiment/esq/code/prompt_esq3b_v2.py:100-103`),
que copia el literal `DOMAIN_RANGE_RETOCADO`
(`data/experiment/esq/code/prompt_esq3b.py:160-177`) sin la fila
`exceptua_operacion`. Filas del literal:

| Firma dibujada | Fila | Ancla | Veredicto |
|---|---|---|---|
| (Restricción, `limita`, Operación) | `"limita": ({"Restriccion"}, {"Operacion"})` | `prompt_esq3b.py:172` | ADMITIDA |
| (Operación, `requiere`, Obligación) | `"requiere": ({"Operacion"}, {"Obligacion"})` | `prompt_esq3b.py:174` | ADMITIDA |
| Restricción → Obligación (cualquier predicado) | ninguna fila | — | NO ADMITIDA por la matriz |
| `referencia` | `({"TextoOrdenado"}, {"Comunicacion"})` | `prompt_esq3b.py:163` | no cubre nodo→nodo |

Recomputado importando el módulo congelado (13 predicados):

```
PYTHONDONTWRITEBYTECODE=1 python3 -c "import sys; sys.path.insert(0,'data/experiment/esq/code'); import prompt_congelado as pc; M=pc.DOMAIN_RANGE_CONGELADO; print(len(M), M['limita'], M['requiere'], M['referencia'], sorted(p for p,(d,r) in M.items() if 'Restriccion' in d and 'Obligacion' in r))"
→ 13 ({'Restriccion'}, {'Operacion'}) ({'Operacion'}, {'Obligacion'}) ({'TextoOrdenado'}, {'Comunicacion'}) []
```

### 2.b Arista «remite a»

No es de la matriz. La produce la resolución de remisiones,
`data/experiment/reextraccion_v2/corpus_v2/r1_referencias.py`: la función
`agregar` arma la arista con `"relation": "referencia"` (`:231`) y
`"rol_fuente": "referencia_cruzada"` (`:234`); el encabezado declara que
«`referencia` nodo→nodo NO está en schema.DOMAIN_RANGE (solo
TextoOrdenado→Comunicacion); se declara, no se edita el esquema» (`:34-36`).
Provenance de la arista = la del nodo origen; `properties.evidencia` = fragmento
exacto (`:33-34`); el punto propio del nodo origen nunca es destino (`:32`).

En `kg.json`: 17.772 aristas; `rol_fuente` = `referencia_cruzada` 5.645,
`esqueleto` 82, `cuarentena_flaggeada` 41, sin `rol_fuente` 12.004
(5.645 + 82 + 41 + 12.004 = 17.772). Las 5.645 son todas de relación
`referencia`; la relación `referencia` suma 5.680, es decir 35 sin `rol_fuente`,
y esas 35 son todas TextoOrdenado→Comunicacion, la única firma que la matriz
admite para `referencia` (paquete: `salida_recomputo_tallies_UFIGPROCV.txt`).
Comando:

```
PYTHONDONTWRITEBYTECODE=1 python3 -c "import json,collections;kg=json.load(open('data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json',encoding='utf-8'));E=kg['edges'];print(len(E),dict(collections.Counter(e.get('rol_fuente') for e in E)),dict(collections.Counter(e['relation'] for e in E if e.get('rol_fuente')=='referencia_cruzada')),sum(1 for e in E if e['relation']=='referencia'))"
```

Las aristas de `kg.json` NO llevan campo `id` (`edges con 'id': 0`, mismo
comando con `sum('id' in e for e in E)`). En todo este reporte identifico cada
arista por su índice `[k]` en `kg['edges']` (0-based, orden del archivo) y por
la tupla (origen, relación, destino, rol_fuente). Los nodos sí llevan `id`.

## 3. Ítem 3 — origen de los tres rótulos

**Elegidos a mano; declarados ficticios por el generador y por el control.**
Ninguna consulta al grafo los produjo.

- Generador, bloque `NODOS` (`generar_figura_proceso_extraccion.py:121-129`):
  «Nodos de ejemplo del grafo de salida. **Los puntos son ficticios**: solo
  muestran que cada nodo conserva el punto del que proviene.» (`:121-122`);
  literales `"punto": "punto 2.5.1"` (`:126`), `"punto 3.4.2"` (`:127`),
  `"punto 2.5.2"` (`:128`).
- Generador, bloque `ARISTAS` (`:131-146`): las dos firmas de extracción se
  cotejan contra la matriz (`FIRMAS_ADMITIDAS`, `:140-143`; assert en `:335-336`)
  y la de remisión «no se coteja contra esa matriz» (`:136-139`). El cotejo es de
  FIRMAS (tipos), no de existencia de nodos ni aristas en el grafo.
- `control_contenido.md`, observación 4 (`:62-66`): «Los puntos “2.5.1”, “3.4.2”
  y “2.5.2” son **ficticios**; les antepuse la palabra “punto” para que el número
  se entienda sin el epígrafe.» Su §4.b (`:105-124`) sí consulta `kg.json`, pero
  solo para contar las aristas `referencia_cruzada` (5.645; 606
  Restricción→Obligación) y confirmar las tres de la figura existente
  (`figura_norma_a_grafo`): no busca los nodos 2.5.1 / 2.5.2 / 3.4.2.

Dónde están esos dos archivos: NO en el repo (`find . -name
"generar_figura_proceso_extraccion.py"` vacío; `git log --all --diff-filter=A
--name-only -- '*generar_figura_proceso*' '*control_contenido*'` vacío). Los
encontré en el paquete de revisión de U-FIG-PROC, fuera del repo:
el directorio `revision_UFIGPROC/` del scratchpad de la sesión `dbe32e3b-bee0-4676-b7ba-e4c985c0a2c4` (bajo el árbol de scratchpads de este proyecto en `/private/tmp/claude-501/`)
(cinco archivos; los sha de los dos coinciden con su `manifest.txt`; el PNG de
ese paquete es byte-idéntico al del repo, §1). Las líneas citadas son de esa
copia. `docs/tesis/main.tex` no incluye la figura todavía (`grep -n
"figura_proceso_extraccion" docs/tesis/main.tex` vacío).

## 4. Ítem 2 — nodos y aristas en el grafo

Consulta completa: paquete, `q_nodos_aristas_UFIGPROCV.py` y su salida
`salida_nodos_aristas_UFIGPROCV.txt`. Criterio: un nodo «tiene procedencia en el
punto p» si p aparece en CUALQUIERA de sus `provenances` (no solo en
`provenance[0]`, regla de `docs/plan_tesis.md:315`).

### 4.a Nodos con procedencia en 2.5.1, 2.5.2 o 3.4.2 — 33 en total

Recomputo: `cap` 9 + `cla` 18 + `ext` 5 + `pro` 1 = 33.

```
PYTHONDONTWRITEBYTECODE=1 python3 -c "import json,collections;kg=json.load(open('data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json',encoding='utf-8'));P={'2.5.1','2.5.2','3.4.2'};S=[n for n in kg['nodes'] if any(p.get('punto') in P for p in n.get('provenances') or [n['provenance']])];print(len(S),dict(collections.Counter(n['provenance']['to'] for n in S)));print(sorted((n['provenance']['to'],p,n['type']) for n in S for p in sorted({q.get('punto') for q in n.get('provenances') or [n['provenance']]}&P)))"
```

| TO | Documento | Punto | Tipo | Cantidad | Etiquetas (id abreviado) |
|---|---|---|---|---|---|
| cap | `TO_capitales_minimos_actual.pdf` | 2.5.1 | Obligación | 2 | «Aplicar mayor ponderador debida diligencia — Grupo 1» (`…4fac03`); «Aplicar ponderadores riesgo punto 2.12» (`…52eb2d`) |
| cap | ídem | 2.5.1 | Operación | 1 | «Aplicación ponderadores riesgo según grupo» (`…e364a5`) |
| cap | ídem | 2.5.1 | Sujeto | 2 | «Entidades financieras del grupo 1» (propuesto, 4 provenances); «Entidades alcanzadas (Capitales Mínimos)» (rol de alcance, 379 provenances) |
| cap | ídem | 2.5.1 y 2.5.2 | TextoOrdenado | 1 | «Texto Ordenado Capitales Mínimos» (461 provenances) |
| cap | ídem | 2.5.2 | Obligación | 2 | «Aplicación de ponderadores por operación» (`…d404f8`); «Aplicación del ponderador mayor» (`…14eefc`) |
| cap | ídem | 2.5.2 | Operación | 1 | «Aplicación de ponderadores de riesgo» (`Operacion_aplicacion_de_ponderadores_de_riesgo_98b663`) |
| cap | ídem | 2.5.2 | Sujeto | (el mismo rol de alcance de arriba) | — |
| cla | `TO_clasificacion_deudores_actual.pdf` | 3.4.2 | Excepción | 2 | «Excepción comunicación cambios — saldo bajo»; «Excepción evaluación capacidad repago — garantías preferidas A» |
| cla | ídem | 3.4.2 | Obligación | 15 | legajo del cliente y comunicación de cambios de clasificación (lista completa en la salida del paquete) |
| cla | ídem | 3.4.2 | TextoOrdenado | 1 | «Clasificación de Deudores» |
| ext | `TO_exterior_cambios_actual.pdf` | 3.4.2 | Restricción | 1 | «Monto total no supere distribución asamblea» (`…459761`) |
| ext | ídem | 3.4.2 | Operación | 1 | «Giro divisas utilidades dividendos exterior» (`…c53c4e`) |
| ext | ídem | 3.4.2 | Obligación | 1 | «Declaración jurada representante legal» (`…ed6cf9`; provenances 3.4.2 y 9.3.12.2) |
| ext | ídem | 3.4.2 | Sujeto | 1 | «Entidades autorizadas a operar en cambios (Exterior)» (rol, 646 provenances) |
| ext | ídem | 3.4.2 | TextoOrdenado | 1 | «Texto Ordenado de Exterior y Cambios» |
| pro | `TO_proteccion_usuarios_servicios_financieros_actual.pdf` | 3.4.2 | Sujeto | 1 | «Entidades financieras» (83 provenances) |

Lo que importa para la figura:

- **Restricción con procedencia en 2.5.1: NINGUNA, en ningún documento.** El
  único documento con nodos en 2.5.1 es `cap`, y allí hay Obligaciones,
  una Operación, Sujetos y el TextoOrdenado. La única Restricción del conjunto
  está en `ext` 3.4.2.
- Operación con procedencia en 2.5.2: una (`cap`, `…98b663`).
- Obligación con procedencia en 3.4.2: dieciséis (`cla` 15, `ext` 1).

### 4.b Aristas entre pares de esos 33 nodos — 42

Desglose por relación (recomputado sobre la salida del paquete):
`establecida_en` 24, `aplica_a` 8, `regula` 3, `exceptua_obligacion` 2,
`miembro_de` 2 (esqueleto), `padre_sugerido` 1 (cuarentena_flaggeada),
`limita` 1, `requiere` 1; 24 + 8 + 3 + 2 + 2 + 1 + 1 + 1 = 42.
**Aristas `referencia` entre pares del conjunto: 0.**

```
PYTHONDONTWRITEBYTECODE=1 python3 -c "import json,collections;kg=json.load(open('data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json',encoding='utf-8'));P={'2.5.1','2.5.2','3.4.2'};I={n['id'] for n in kg['nodes'] if any(p.get('punto') in P for p in n.get('provenances') or [n['provenance']])};A=[e for e in kg['edges'] if e['source'] in I and e['target'] in I];print(len(A),dict(collections.Counter(e['relation'] for e in A)))"
```

Las dos aristas de contenido que sobreviven entre pares están en `ext`, dentro
del punto 3.4.2:

- `[13054]` Restricción `…459761` (3.4.2) —`limita`→ Operación `…c53c4e` (3.4.2)
- `[11501]` Operación `…c53c4e` (3.4.2) —`requiere`→ Obligación `…ed6cf9` (3.4.2)

No hay ninguna arista, del tipo que sea, entre un nodo de 2.5.1 y uno de 2.5.2,
ni entre un nodo de 2.5.2 y uno de 3.4.2 (la única Operación de 2.5.2 recibe
`regula` de dos Obligaciones de su mismo punto, `[2984]` y `[8876]`, y no emite
`requiere`).

### 4.c Veredicto por arista dibujada

| Arista dibujada | Veredicto | Motivo |
|---|---|---|
| Restricción 2.5.1 —limita→ Operación 2.5.2 | **NO EXISTE** | no hay nodo Restricción en 2.5.1; ninguna arista 2.5.1→2.5.2 |
| Operación 2.5.2 —requiere→ Obligación 3.4.2 | **NO EXISTE** | la Operación de 2.5.2 está en `cap` y no emite `requiere`; las Obligaciones de 3.4.2 están en `cla` y `ext` |
| Restricción 2.5.1 —remite a→ Obligación 3.4.2 | **NO EXISTE** | no hay nodo Restricción en 2.5.1; 0 aristas `referencia` entre pares del conjunto |

Ningún caso es «EXISTE CON OTRO TIPO»: no existe arista alguna entre los
extremos dibujados. De los tres NODOS, dos existen leídos en su documento más
favorable (Operación 2.5.2 en `cap`; Obligación 3.4.2 en `cla` o `ext`) y uno no
existe en ningún documento (Restricción 2.5.1).

## 5. Ítem 4 — tríos reales con el patrón completo

Patrón buscado: Restricción —`limita`→ Operación —`requiere`→ Obligación, más
Restricción —`referencia` (`rol_fuente = referencia_cruzada`)→ esa misma
Obligación. Consulta: paquete, `q_trios_UFIGPROCV.py` /
`salida_trios_UFIGPROCV.txt`; detalle: `q_trios_detalle_UFIGPROCV.py` /
`salida_trios_detalle_UFIGPROCV.txt`; textos: `q_textos_UFIGPROCV.py` /
`salida_textos_UFIGPROCV.txt`.

Conteos (comando de recomputo abajo):

| Medida | Valor |
|---|---|
| Cadenas R —limita→ OP —requiere→ O | 318 (`ext` 251, `cap` 39, `cla` 18, `ric` 10; suma 318) |
| … de ellas con `referencia` R→O (patrón COMPLETO) | 5, todas en `ext` |
| … con `referencia` en sentido inverso O→R | 2 |
| Cadenas en el subgrafo de dividendos (`ext`, puntos 3.17.1.4, 3.4.1–3.4.3) | 1, SIN `referencia` R→O |
| Patrón completo relajando el predicado R→OP a {limita, prohibe, regula} | 5 (los mismos) |

```
PYTHONDONTWRITEBYTECODE=1 python3 -c "
import json,collections
kg=json.load(open('data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json',encoding='utf-8'));N={n['id']:n for n in kg['nodes']};E=kg['edges']
out=collections.defaultdict(list)
for i,e in enumerate(E): out[e['source']].append((i,e))
c=[];f=[]
for i1,e1 in enumerate(E):
  if e1['relation']!='limita' or N[e1['source']]['type']!='Restriccion' or N[e1['target']]['type']!='Operacion': continue
  for i2,e2 in out[e1['target']]:
    if e2['relation']!='requiere' or N[e2['target']]['type']!='Obligacion': continue
    r=[i3 for i3,e3 in out[e1['source']] if e3['relation']=='referencia' and e3['target']==e2['target']]
    c.append(e1['source']); f.append((i1,i2,r)) if r else None
print(len(c),dict(collections.Counter(N[x]['provenance']['to'] for x in c)),len(f),f)"
→ 318 {'ext': 251, 'cap': 39, 'cla': 18, 'ric': 10} 5 [(14243, 11358, [14252]), (14243, 11359, [14254]), (14243, 11360, [14257]), (14243, 11361, [14262]), (14243, 11362, [14266])]
```

### 5.a Las cinco cadenas completas comparten Restricción y Operación

Todas están en `TO_exterior_cambios_actual.pdf`, sección 9 («Seguimiento de
anticipos y otras financiaciones de exportación de bienes»), punto 9.3
(«Certificaciones de aplicación de cobros de exportaciones»). Los dos nodos
comunes:

- **R** = `Restriccion_la_emision_de_certificaciones_procede_en_la_medida_que_se_verifiquen_las_condici_0b63ed`,
  etiqueta «Condición verificación requisitos 9.3.1-9.3.13», `properties.tipo =
  limite_cualitativo`; UNA provenance: `ext::9.3::intro`, `rol_documental =
  bloque_intro`, página 124. Su punto es 9.3, pero el texto de origen es el
  segmento introductorio de una unidad NO terminal (está en
  `estructura_ext.json`, no en `chunks_ext.json`).
- **OP** = `Operacion_emision_de_certificaciones_de_aplicacion_bf0334`, etiqueta
  «Emisión de certificaciones de aplicación»; nodo FUSIONADO con SEIS
  provenances: `ext::9.3::intro` (p.124, bloque_intro), `ext::9.3.1::cierre`
  (p.125, bloque_cierre), `ext::9.3.4` (p.126), `ext::9.3.7` (p.126-127),
  `ext::9.3.8` (p.127), `ext::9.3.13` (p.128). `provenance[0].punto = 9.3`.
  Lleva `properties.cola_humana = "true"`, `estado_e3 = cola_humana`,
  `cola_chunks = ["ext::9.3.7"]`: el revisor lo dejó marcado para revisión
  humana.

Las cinco Obligaciones destino, con sus tres aristas (índices en `kg['edges']`):

| # | Obligación (id abreviado) | Punto de O | `limita` R→OP | `requiere` OP→O | `referencia` R→O | Observación |
|---|---|---|---|---|---|---|
| 1 | «Constancia de liberación de obligaciones contingentes» (`…ed32ee`) | 9.3.4 | `[14243]` | `[11362]` | `[14266]` (destino `ext::9.3.4`) | aristas sin flags |
| 2 | «Declaración jurada del exportador — deuda al 31/08/19» (`…409555`) | 9.3.7 | `[14243]` | `[11359]` | `[14254]` (destino `ext::9.3.7`) | `[11359]` lleva `cola_humana = "true"` |
| 3 | «Documentación de requisitos puntos 7.9. o 7.10.» (`…35d4ee`) | 9.3.8 | `[14243]` | `[11358]` | `[14252]` (destino `ext::9.3.8`) | aristas sin flags |
| 4 | «Constatación de vencimiento de cancelación» (`…cc1eda`) | 9.3.8 | `[14243]` | `[11360]` | `[14257]` (destino `ext::9.3.8`) | aristas sin flags |
| 5 | «Verificación de condiciones previstas en punto 9.3.1.» (`…23b724`) | 9.3.8 | `[14243]` | `[11361]` | `[14262]` (destino `ext::9.3.8`) | aristas sin flags |

Las cinco aristas `referencia` tienen la misma `evidencia`: «a medida que se
verifiquen las condiciones previstas en los puntos 9.3.1. al 9.3.13», `clase =
interna`, `via = nodos_del_punto`. Es decir: la remisión de R es UN RANGO
(9.3.1 al 9.3.13) que la resolución expandió a todos los nodos de cada punto
destino; R emite 61 aristas `referencia` en total (`salida_trios_detalle…`,
sección «Todas las aristas referencia desde R_0b63ed»). Cualquier trío de la
tabla dibuja una de esas 61.

### 5.b Tres tríos propuestos (puntos de destino distintos)

El mandato pide hasta tres tríos y «los ids de las cuatro aristas». El patrón
tal como lo enuncia tiene TRES aristas (limita, requiere, referencia); no
encuentro una cuarta en el patrón ni en la figura, así que reporto tres por trío
y dejo la discrepancia declarada (regla d). Todos en
`TO_exterior_cambios_actual.pdf`; textos = primeros 200 caracteres con espacios
normalizados (`salida_textos_UFIGPROCV.txt`; 9.3 sale de
`estructura_ext.json` → `secciones[8].hijos[2].segmentos[0]`, rol `intro`).

**Trío A** — R 9.3 → OP (fusionada; provenance[0] 9.3) → O 9.3.4. Aristas
`[14243]`, `[11362]`, `[14266]`.

- 9.3 (p.124, intro): «A solicitud del exportador, la entidad encargada del seguimiento emitirá las certificaciones de aplicación en la medida que se verifiquen las condiciones previstas en los puntos 9.3.1. al 9.3.13. La e»
- 9.3.4 (p.126): «9.3.4. Posfinanciaciones del exterior por descuentos y/o cesiones de créditos a la exportación. Se podrán emitir las certificaciones de aplicación de las divisas a la cancelación del capital y los int»
- Texto de O (`properties.texto`): «Las certificaciones sólo podrán emitirse en la medida que la entidad tenga constancia que el exportador ha sido liberado de sus obligaciones contingentes con el exterior»

**Trío B** — R 9.3 → OP → O 9.3.7. Aristas `[14243]`, `[11359]`, `[14254]`.
Advertencia: `[11359]` y el nodo OP están en cola humana por el chunk
`ext::9.3.7`.

- 9.3.7 (p.126-127): «9.3.7. Préstamos financieros con contratos vigentes al 31/08/19 cuyas condiciones prevean la atención de los servicios mediante la aplicación en el exterior del flujo de fondos de exportaciones para l»
- Texto de O: «La entidad debe contar con una declaración jurada del exportador detallando el monto pendiente de la deuda al 31/08/19 y las cancelaciones realizadas»

**Trío C** — R 9.3 → OP → O 9.3.8; tres Obligaciones candidatas en ese punto
(filas 3, 4 y 5 de la tabla). Aristas: `[14243]`, y según la Obligación,
`[11358]`/`[14252]`, `[11360]`/`[14257]` o `[11361]`/`[14262]`.

- 9.3.8 (p.127): «9.3.8. Endeudamientos financieros con el exterior admitidos en los puntos 7.9. o 7.10. La entidad podrá emitir las certificaciones de aplicación de las divisas a la cancelación del capital, intereses »
- Textos de O: fila 3 «la entidad debe contar con la documentación que le permita verificar el cumplimiento de los requisitos establecidos en los puntos 7.9. o 7.10., según corresponda»; fila 4 «la entidad deberá constatar que la cancelación tuvo lugar a partir de la fecha de vencimiento»; fila 5 «la entidad deberá verificar las condiciones indicadas en el punto 9.3.1.»

Dos advertencias para el redibujo, comunes a los tres: (i) la figura pone UN
punto debajo de cada nodo, y OP tiene seis; habrá que decidir cuál se rotula
(`provenance[0]` es 9.3, el mismo punto de R) o si se rotula «9.3 y otros»;
(ii) el punto de R (9.3) es un bloque introductorio de unidad no terminal, no un
punto terminal con chunk propio.

### 5.c Subgrafo de dividendos: el patrón más cercano

El mandato pedía priorizar 3.17.1.4 y 3.4.1–3.4.3. Allí NO hay trío completo.
Ocho nodos de contenido y diez aristas entre ellos
(`q_dividendos_UFIGPROCV.py` / `salida_dividendos_UFIGPROCV.txt`). Lo que hay:

- Cadena limita + requiere, sin remisión, íntegra en 3.4.2:
  `[13054]` Restricción «Monto total no supere distribución asamblea» (`…459761`,
  3.4.2) —`limita`→ Operación «Giro divisas utilidades dividendos exterior»
  (`…c53c4e`, 3.4.2) —`requiere` `[11501]`→ Obligación «Declaración jurada
  representante legal» (`…ed6cf9`, 3.4.2 y 9.3.12.2). No hay `referencia` R→O
  porque la remisión intra-punto está excluida por diseño (`r1_referencias.py:32`).
- Remisiones desde la Restricción de 3.17.1.4 «Requisitos puntos 3.4.1 a 3.4.3 —
  utilidades dividendos» (`…8355c7`, provenances 3.17.1.4 y 3.18.1.2): `[16672]`
  → Obligación 3.4.1 (`…999fbd`), `[16670]` → Obligación 3.4.2 (`…ed6cf9`),
  `[16671]` → Obligación 3.4.3 (`…6514f0`), más `[16673]`/`[16674]` → las
  Operaciones de 3.4.3 y 3.4.2 y `[16675]` → la Restricción de 3.4.2. Esa
  Restricción `limita` `[16669]` la Operación «Pagos utilidades dividendos
  accionistas no residentes» (`…59fccf`, 3.17.1.4), pero esa Operación no emite
  `requiere` hacia ninguna de las tres Obligaciones remitidas.

Patrón más cercano con CUATRO nodos (dos Restricciones distintas): Restricción
3.17.1.4 (`…8355c7`) —`referencia` `[16670]`→ Obligación 3.4.2 (`…ed6cf9`)
←`requiere` `[11501]`— Operación 3.4.2 (`…c53c4e`) ←`limita` `[13054]`—
Restricción 3.4.2 (`…459761`). Es coherente con la figura ya existente
`figura_norma_a_grafo`, que usa `…8355c7` y los destinos `…999fbd`, `…ed6cf9`,
`…6514f0` (`control_contenido.md:107-109`). Textos:

- 3.17.1.4 (p.50): «3.17.1.4. Pagos de utilidades y dividendos a accionistas no residentes en la medida que se verifiquen los requisitos previstos en los puntos 3.4.1. a 3.4.3.»
- 3.4.2 (p.17): «3.4.2. El monto total abonado por este concepto a accionistas no residentes, incluido el pago cuyo curso se está solicitando, no supere el monto en moneda local que les corresponda según la distribuci»
- 3.4.1 (p.17): «3.4.1. Las utilidades y dividendos correspondan a balances cerrados y auditados.»
- 3.4.3 (p.17): «3.4.3. La entidad deberá verificar que el cliente haya dado cumplimiento en caso de corresponder, a la declaración de la última presentación vencida del “Relevamiento de activos y pasivos externos” po»

## 6. FRENO

Tres aristas dibujadas: NO EXISTE, NO EXISTE, NO EXISTE. No redibujo. Opciones
sobre la mesa: (1) uno de los tríos A/B/C de §5.b (patrón completo, sección
9.3, con las dos advertencias); (2) el patrón de cuatro nodos de §5.c
(dividendos, coherente con `figura_norma_a_grafo`, pero con dos Restricciones y
sin el triángulo de tres nodos); (3) mantener el mini-grafo como ilustración
declaradamente esquemática, quitando los números de punto o marcándolos como
ejemplo. La elección es de la mesa.

## 7. Contradicciones con el mandato (regla d)

1. `e69feaaa…` no es el sha del archivo `prompt_congelado.py` (que es
   `a5a4ba33…`) sino el del texto del prefijo que produce (§1).
2. El generador y `control_contenido.md` no están en el repo; verifiqué las
   copias del paquete de revisión de U-FIG-PROC (§3).
3. El patrón pedido tiene tres aristas, no «cuatro» (§5.b).
4. Las aristas de `kg.json` no tienen `id`; uso índice en `kg['edges']` (§2.b).

## 8. Redibujo (misma unidad, 18/09/2026, tras la aprobación del reporte)

Decisión de la mesa: el panel «Grafo» pasa al patrón de cuatro nodos del
subgrafo de dividendos (§5.c); etiquetas de nodo las del grafo r1, acortadas
como en `figura_norma_a_grafo`; se descartan los tríos de 9.3 y el esquema sin
puntos. Escrituras: el generador, el PNG y esta sección.

### 8.a Generador

`docs/tesis/figuras/generar_figura_proceso_extraccion.py`, copiado del paquete
de U-FIG-PROC (origen sha `76aaedb1…`, §1) y modificado; sha del archivo en el
repo en la versión FINAL CERRADA (§8.h):
`fd301e81a2f26244b936e2ccac485a89fd4493540c2161f5dfc78b63a6ec71c1`
(703 líneas; el origen tenía 613; versiones intermedias: primer redibujo
`5121a248…`, retoque 1 revertido `076f58fe…`, lazos con fila de tipos
`dc0fcd4b…`, tres nodos con franja inferior `31773007…`). Diferencia contra el
origen: 222 líneas en 19 hunks (`diff origen repo | grep -c "^[<>]"` y
`grep -c "^[0-9]"`), todos dentro de:
docstring (nota sobre la consulta al grafo), imports (`hashlib`, `json`),
constantes `RAIZ`/`KG`/`KG_SHA256`, el bloque de datos del panel
(`NODOS_FIGURA`, `ARISTAS_FIGURA`, `NOMBRE_TIPO`, `provenances`,
`cargar_grafo`), las constantes de geometría del panel y `dibujar_grafo`, la
firma de `componer` y `main`. Paleta, tipografía, tamaños de letra, leyenda,
elementos (a)–(f), flechas de proceso y exportación a PNG: sin cambio. El
comentario «Los puntos son ficticios» (origen `:121-124`) y el bloque `NODOS`
tipeado (`:125-129`) ya no existen. (Los párrafos que siguen en 8.a–8.c
describen el primer redibujo de cuatro nodos; la versión final está en 8.g.)

Cómo toma los datos (`cargar_grafo`): lee `kg.json`, **frena si su sha256 no es
`0226e947…`**; cada nodo se busca por (documento `ext`, tipo, punto de
procedencia con `rol_documental = punto_propio`) y la búsqueda debe dar
exactamente un nodo, del que salen id, etiqueta y punto; cada arista se busca
por (id origen, relación, id destino) y debe existir exactamente una: las de
extracción con firma en `FIRMAS_ADMITIDAS` y sin `rol_fuente`, la de remisión
con `rol_fuente = referencia_cruzada`. El script imprime lo resuelto al correr
(salida completa en el paquete, `salida_generador_redibujo_UFIGPROCV.txt`).

### 8.b Los cuatro nodos (resueltos por el generador, no tipeados)

| Clave | Tipo | id | Etiqueta en el grafo | Etiqueta dibujada | Procedencia rotulada | Otras provenances |
|---|---|---|---|---|---|---|
| R1 | Restricción | `Restriccion_pagos_de_utilidades_y_dividendos_a_accionistas_no_residentes_en_la_medida_que_se_8355c7` | «Requisitos puntos 3.4.1 a 3.4.3 — utilidades dividendos» | «Requisitos para pagar dividendos» (la de `figura_norma_a_grafo`, `generar_figura_norma_a_grafo.py:61`) | `ext::3.17.1.4`, punto_propio, p. 50 | `ext::3.18.1.2`, punto_propio, p. 53 |
| R2 | Restricción | `Restriccion_el_monto_total_abonado_por_este_concepto_a_accionistas_no_residentes_incluido_el_459761` | «Monto total no supere distribución asamblea» | «No supera lo aprobado en asamblea» (nueva) | `ext::3.4.2`, punto_propio, p. 17 | — |
| OP | Operación | `Operacion_giro_divisas_utilidades_dividendos_exterior_c53c4e` | «Giro divisas utilidades dividendos exterior» | «Giro de dividendos al exterior» (nueva) | `ext::3.4.2`, punto_propio, p. 17 | — |
| O | Obligación | `Obligacion_la_entidad_debera_contar_con_una_declaracion_jurada_firmada_por_el_representante_ed6cf9` | «Declaración jurada representante legal» | «Declaración jurada del representante» (nueva) | `ext::3.4.2`, punto_propio, p. 17 | `ext::9.3.12.2`, punto_propio, p. 128 |

Sobre las etiquetas: la regla es la de `figura_norma_a_grafo` (tabla
`ETIQUETAS_CORTAS` por sufijo de id, máximo 40 caracteres). Tres son nuevas
porque esos nodos no están en aquella figura o porque la original no entra en
esta caja: la de `ed6cf9` tiene 38 caracteres, pero «representante legal» no
cabe en una línea de 122 unidades a 18 px y la partiría en cuatro líneas. El
generador frena si una etiqueta dibujada supera los 40 caracteres o las tres
líneas.

### 8.c Las tres aristas

| Arista dibujada | Índice en `kg['edges']` | Origen | Relación | Destino | `rol_fuente` | Detalle |
|---|---|---|---|---|---|---|
| «limita» (gris) | `[13054]` | `…459761` (R2) | `limita` | `…c53c4e` (OP) | ninguno | firma (Restricción, limita, Operación) admitida; provenance 3.4.2 |
| «requiere» (gris) | `[11501]` | `…c53c4e` (OP) | `requiere` | `…ed6cf9` (O) | ninguno | firma (Operación, requiere, Obligación) admitida; provenance 3.4.2 |
| «remite a» (naranja) | `[16670]` | `…8355c7` (R1) | `referencia` | `…ed6cf9` (O) | `referencia_cruzada` | `clase = interna`, `destino = ext::3.4.2`, `via = nodos_del_punto`; provenance 3.17.1.4 |

### 8.d Salida y reproducibilidad

| Medida | Antes (U-FIG-PROC) | Primer redibujo (4 nodos) | Con retoque 1 (revertido) | Lazos + fila de tipos (§8.f, superada) | 3 nodos con franja inferior (§8.g, superada) | **FINAL CERRADA** (§8.h) |
|---|---|---|---|---|---|---|
| sha256 del PNG | `45b805d26e40538d8ee919935f1b8d60fc10cc4a85d74af2828fd62e68fd535f` | `44e56349…` | `02f48bb5…` | `91141f17…` | `78db3cf9…` | `cec84227c57ba610acb3a1f65795e35085a62b5cb9a207e4609d6b96c445c8d6` |
| sha256 del SVG | `8b8ced5e98c388843554f55ee53662b29a7c1e5ab891cd7a331b804d552fa7a8` | `a4d041d5…` | `c983c81c…` | `9227513e…` | `a367ee36…` | `d27cb6dca65e98a808aa09f73dbd23593d4ebb6f5201d375f752e79fd43d0c43` |
| Lienzo (unidades) | 720 × 698 | 720 × 795 | 720 × 802 | 720 × 823 | 720 × 698 | **720 × 665** |
| PNG (px, 300 dpi) | 1506 × 1460 | 1506 × 1664 | 1506 × 1678 | 1506 × 1721 | 1506 × 1460 | **1506 × 1392** |
| Impresa | 12,75 × 12,36 cm | 12,75 × 14,08 cm | 12,75 × 14,20 cm | 12,75 × 14,57 cm | 12,75 × 12,36 cm | **12,75 × 11,78 cm** |
| Letra mínima impresa | 9,04 pt (18 px) | 9,04 pt (18 px) | 9,04 pt (18 px) | 9,04 pt (18 px) | 9,04 pt (18 px) | 9,04 pt (18 px), sin cambio |
| Textos medidos / fallas | — | 53 / 0 | 58 / 0 | 58 / 0 | 42 / 0 | 42 / 0 |

Tres corridas con `PYTHONHASHSEED` 0, 1 y 12345 producen el mismo SVG y el
mismo PNG (sha idénticos en las tres; comando y salida en el paquete,
`salida_tres_corridas_UFIGPROCV.txt`). `--verificar` con métricas reales de
Helvetica sobre la versión final: 42 textos medidos, 0 fallas (ninguno bajo
9 pt, fuera de su caja, fuera del lienzo ni superpuesto). Comando:

```
PYTHONDONTWRITEBYTECODE=1 python3 docs/tesis/figuras/generar_figura_proceso_extraccion.py --verificar
for s in 0 1 12345; do PYTHONHASHSEED=$s PYTHONDONTWRITEBYTECODE=1 python3 docs/tesis/figuras/generar_figura_proceso_extraccion.py >/dev/null; shasum -a 256 docs/tesis/figuras/figura_proceso_extraccion.png; done
```

### 8.e Desvíos y observaciones declarados en la primera versión del redibujo

1. **El lienzo creció** (698 → 795 unidades; 12,36 → 14,08 cm impresos; la
   versión de §8.f llegó a 823 y 14,57 cm por la fila nueva de la leyenda; la
   de §8.g vuelve a 698 y 12,36 cm; la FINAL CERRADA de §8.h queda en 665 y
   11,78 cm). Causa: cuatro nodos con tres líneas
   de etiqueta más el punto, a la letra mínima de 9 pt, dentro de un panel cuyo
   ancho (296 unidades) fija la fila (e)-(f)-(g). Nodos de 132 × 90 (antes
   116 × 50) en dos columnas y dos filas. Ancho, letra y paleta sin cambio.
2. **El tipo de nodo quedaba codificado solo por color** (la versión anterior
   lo explicaba con el rótulo del nodo, que era el nombre del tipo,
   `control_contenido.md:62-64`). Resuelto por la mesa en §8.f: fila «Tipo de
   nodo» en la leyenda.
3. **El SVG era un subproducto no autorizado** y lo había retirado del repo.
   Autorizado por la mesa en §8.f: queda en `docs/tesis/figuras/` junto al PNG,
   como los `.svg` de los demás generadores de la carpeta.
4. El generador lleva un candado de sha sobre `kg.json`: si el grafo vigente
   cambia, frena en vez de dibujar con datos no verificados.
5. Tres de los cuatro nodos rotulan el mismo punto (3.4.2): es lo que hay en el
   grafo, y muestra que un punto origina varios nodos.

### 8.f Retoques de la mesa, reversión del primero y versión final (18/09/2026)

Primera revisión del redibujo: nodos, aristas y verificación aprobados; tres
retoques. (1) «limita» y «remite a» como flechas rectas horizontales entre los
nodos de cada fila, rótulo centrado sobre la flecha, sin lazos. (2) Fila «Tipo
de nodo» en la leyenda con los cuatro tipos y sus colores, con la función de la
de `figura_norma_a_grafo`, antes de la fila de etapas. (3) El SVG queda en el
repo.

**Retoque 1: aplicado, revisado y REVERTIDO.** El rótulo no entra entre las
columnas: el ancho de nodo lo fija la línea «punto 3.17.1.4» en negrita (120,0
unidades a 18 px con métricas reales de Helvetica; `W_NODO` = 132 con 10 de
margen interno), y dos nodos de 132 en un contenedor de 296 dejan como máximo
24 unidades entre columnas, menos que el rótulo más corto («limita», 42,0) y
mucho menos que «remite a» en negrita (69,0). Achicar los nodos rompe la letra
mínima de 9 pt o parte palabras («representante», 111,0); ensanchar el
contenedor exige achicar (e) o (f), fuera de mandato. La versión con flechas
rectas (PNG `02f48bb5…`, SVG `c983c81c…`, generador `076f58fe…`) llevó los
rótulos por fuera de la banda de nodos, encima y debajo de las flechas; la
mesa la revisó y decidió revertir: separado de la flecha, el rótulo se lee peor
que sobre el tramo horizontal del lazo. Medidas:
`python3 -c "from PIL import ImageFont as F; f=lambda s,b: F.truetype('/System/Library/Fonts/Helvetica.ttc',180,index=1 if b else 0).getlength(s)/10; print(f('punto 3.17.1.4',1), f('limita',0), f('remite a',1), f('representante',0))"`
→ `120.0 42.0 69.0 111.0`.

**Versión final = trazado del primer redibujo + retoques 2 y 3.** «limita» y
«remite a» vuelven a los lazos con el rótulo sobre el tramo horizontal
(«limita» por encima de la fila de arriba, «remite a» por debajo de la de
abajo); «requiere» vertical sin cambio. Geometría del panel idéntica a la del
primer redibujo: `PAD_NODO` 8, `Y_NODOS` 40, `SEP_NODOS` 36, `BAJADA` 22,
`ALTO_GRAFO` 332; las constantes del retoque revertido (`ROTULO_ARRIBA`,
`ROTULO_ABAJO`) ya no existen. **Prueba de que la reversión es exacta:** una
copia de control del generador final con la leyenda de dos filas del primer
redibujo (único cambio; corre desde el scratchpad con la raíz del repo fijada)
produce el SVG `a4d041d5…` y el PNG `44e56349…` del primer redibujo, byte a
byte (paquete: `control_primer_redibujo_generar_UFIGPROCV.py`,
`control_primer_redibujo_salida_UFIGPROCV.txt`). La versión final difiere del
primer redibujo solo en la leyenda.

**Retoque 2 (conservado).** Fila «Tipo de nodo» como primera fila de la
leyenda: rótulo en negrita y una muestra de color por tipo (Restricción,
Obligación, Operación, Sujeto), en el orden y con la función de
`generar_figura_norma_a_grafo.py` (`dibujar_leyenda`), a los 18 px y con las
muestras de 24 × 16 de esta figura. La leyenda pasa de dos filas (68 de alto) a
tres (96): de ahí las 28 unidades más de lienzo respecto del primer redibujo
(795 → 823). Constantes `LEYENDA_TIPOS`, `TIPOS_LEYENDA`, `NOMBRE_TIPO`.

**Retoque 3 (conservado).** `docs/tesis/figuras/figura_proceso_extraccion.svg`
queda en el repo (sha en §8.d).

### 8.g Revisión final: vuelta a la composición original con procedencia real (18/09/2026)

**Decisión de la mesa.** El panel «Grafo» vuelve a la composición original de
U-FIG-PROC: tres nodos en triángulo con el nombre del tipo como rótulo y
«punto N» debajo, pero con procedencia real. Nodos: Restricción del punto
3.17.1.4 (`…8355c7`), Operación del punto 3.17.1.4 (`…59fccf`, la que
`figura_norma_a_grafo` rotula «Pago de dividendos a no residentes»,
`generar_figura_norma_a_grafo.py:33,63`) y Obligación del punto 3.4.2
(`…ed6cf9`). Aristas: Restricción —limita→ Operación (gris) y Restricción
—remite a→ Obligación (naranja, `referencia_cruzada`), ambas resueltas por
consulta a `kg.json`. Sin arista «requiere». Leyenda: la de dos filas
original, sin la fila «Tipo de nodo». Lienzo del tamaño original si entra.

**Motivo (síntesis de las tres revisiones).** El defecto que abrió esta unidad
era la procedencia ficticia de los rótulos (§3), no la composición. El redibujo
de cuatro nodos con etiquetas del grafo obligó a concesiones que la mesa fue
revisando una por una: etiquetas de tres líneas y nodos de 90 de alto, un
lienzo 14 % a 18 % más alto, una fila de tipos en la leyenda para explicar el
color, y rótulos de arista que no entran entre las columnas ni se leen bien
separados de la flecha (§8.e–8.f). Tres nodos reales del mismo subgrafo de
dividendos muestran lo que la figura tiene que mostrar (cada nodo conserva su
punto; la remisión resuelta es una arista) con la composición, el rótulo por
tipo, la leyenda y el lienzo de la versión original.

**Los tres nodos (resueltos por el generador, no tipeados; salida completa en
el paquete, `salida_generador_redibujo_UFIGPROCV.txt`):**

| Clave | Rótulo dibujado | id | Etiqueta en el grafo | Procedencia rotulada | Otras provenances |
|---|---|---|---|---|---|
| R | Restricción / punto 3.17.1.4 | `Restriccion_pagos_de_utilidades_y_dividendos_a_accionistas_no_residentes_en_la_medida_que_se_8355c7` | «Requisitos puntos 3.4.1 a 3.4.3 — utilidades dividendos» | `ext::3.17.1.4`, punto_propio, p. 50 | `ext::3.18.1.2`, punto_propio, p. 53 |
| O | Obligación / punto 3.4.2 | `Obligacion_la_entidad_debera_contar_con_una_declaracion_jurada_firmada_por_el_representante_ed6cf9` | «Declaración jurada representante legal» | `ext::3.4.2`, punto_propio, p. 17 | `ext::9.3.12.2`, punto_propio, p. 128 |
| OP | Operación / punto 3.17.1.4 | `Operacion_pagos_utilidades_dividendos_accionistas_no_residentes_59fccf` | «Pagos utilidades dividendos accionistas no residentes» | `ext::3.17.1.4`, punto_propio, p. 50 | — |

Cada búsqueda por (documento `ext`, tipo, punto con rol `punto_propio`) da
exactamente un nodo (comando: el propio generador frena si no; comprobación
independiente en el paquete, `salida_generador_redibujo_UFIGPROCV.txt`).

**Las dos aristas:**

| Arista dibujada | Índice en `kg['edges']` | Origen | Relación | Destino | `rol_fuente` | Detalle |
|---|---|---|---|---|---|---|
| «limita» (gris, diagonal a la derecha) | `[16669]` | `…8355c7` (R) | `limita` | `…59fccf` (OP) | ninguno | firma (Restricción, limita, Operación) admitida, `prompt_esq3b.py:172` |
| «remite a» (naranja, diagonal a la izquierda) | `[16670]` | `…8355c7` (R) | `referencia` | `…ed6cf9` (O) | `referencia_cruzada` | `clase = interna`, `destino = ext::3.4.2`, `via = nodos_del_punto` |

En `kg.json` no existe ninguna arista entre `…59fccf` y `…ed6cf9` en ningún
sentido (`[(i, e['relation']) for i, e in enumerate(E) if {e['source'],
e['target']} == {OP, O}]` → `[]`), así que la composición sin «requiere» es
además la única fiel para estos tres nodos.

**Generador.** El bloque de datos pasa a tres nodos y dos aristas;
`FIRMAS_ADMITIDAS` queda con la única firma de extracción dibujada; el rótulo
del nodo es `NOMBRE_TIPO[tipo]` en la primera línea y «punto N» en negrita en
la segunda, como en el origen; desaparecen `ETIQUETAS_CORTAS`, `MAX_ETIQUETA`,
`LINEAS_ETIQUETA` y las constantes de la fila de tipos de la leyenda; la
etiqueta que el nodo tiene en el grafo se imprime al correr y no se dibuja.
`dibujar_grafo` vuelve al trazado original (diagonales desde la Restricción
con el rótulo al costado) y frena si una arista no sale de la Restricción.
La leyenda vuelve al bloque original de dos filas (68 de alto). Candado de
sha sobre `kg.json` y comprobaciones de nodos y aristas: sin cambio.

**Geometría y un desvío declarado.** `Y_NODOS` 40, `H_NODO` 50, `SEP_NODOS`
52 como en el origen. **`W_NODO` pasa de 116 a 132** porque «punto 3.17.1.4»
en negrita mide 120,0 unidades a 18 px (métricas reales de Helvetica; el
origen dibujaba «punto 2.5.1») y no entra en los 106 útiles del nodo original;
los dos nodos de abajo quedan a 12 unidades entre sí (antes 44:
296 − 2 × 10 − 2 × W_NODO). En esta versión la franja de
33 unidades bajo los nodos que en el origen ocupaba el lazo de «requiere» se
conservó como margen inferior del panel (`BANDA_INFERIOR = 22 + 11`) para que
`ALTO_GRAFO` siguiera en 235 y el lienzo midiera exactamente lo que medía:
720 × 698, 1506 × 1460 px, 12,75 × 12,36 cm; la mesa la quitó en el ajuste
final (§8.h).

**Salida de esta versión (superada por §8.h).** PNG `78db3cf9…`, SVG
`a367ee36…` (completos en §8.d); tres corridas con `PYTHONHASHSEED` 0, 1 y
12345 con sha idénticos; `--verificar`: 42 textos, 0 fallas. Respecto del PNG
original `45b805d2…`: mismo lienzo y misma leyenda; cambian los puntos
rotulados (3.17.1.4, 3.4.2, 3.17.1.4 en lugar de 2.5.1, 3.4.2, 2.5.2), el
ancho de los nodos y la ausencia del lazo «requiere».

### 8.h Ajuste final y cierre de la unidad (18/09/2026)

La mesa aprobó como final la versión de §8.g con un ajuste cosmético: quitar la
franja vacía bajo los nodos del panel «Grafo». Cambio en el generador: la
constante `BANDA_INFERIOR` desaparece y `ALTO_GRAFO = Y_NODOS + 2 * H_NODO +
SEP_NODOS + 10` = 202 (antes 235); el panel termina 10 unidades debajo de la
fila inferior de nodos. Nada más cambia: nodos, aristas, rótulos, leyenda,
paleta y letra son los de §8.g.

| Medida | Valor final |
|---|---|
| Generador | `fd301e81a2f26244b936e2ccac485a89fd4493540c2161f5dfc78b63a6ec71c1` (703 líneas; 222 líneas en 19 hunks contra el origen) |
| PNG | `cec84227c57ba610acb3a1f65795e35085a62b5cb9a207e4609d6b96c445c8d6`, 1506 × 1392 px, 300 dpi |
| SVG | `d27cb6dca65e98a808aa09f73dbd23593d4ebb6f5201d375f752e79fd43d0c43`, lienzo 720 × 665 |
| Impresa | 12,75 × 11,78 cm (el original medía 12,36 de alto) |
| Reproducibilidad | tres corridas con `PYTHONHASHSEED` 0, 1 y 12345: mismo SVG y mismo PNG (`salida_tres_corridas_UFIGPROCV.txt`) |
| Verificación de medidas | 42 textos, 0 fallas, letra mínima 9,04 pt (`salida_generador_redibujo_UFIGPROCV.txt`) |

Comando de regeneración y verificación, desde la raíz del repo:

```
PYTHONDONTWRITEBYTECODE=1 python3 docs/tesis/figuras/generar_figura_proceso_extraccion.py --verificar
for s in 0 1 12345; do PYTHONHASHSEED=$s PYTHONDONTWRITEBYTECODE=1 python3 docs/tesis/figuras/generar_figura_proceso_extraccion.py >/dev/null; shasum -a 256 docs/tesis/figuras/figura_proceso_extraccion.png; done
```

Con este ajuste la unidad U-FIG-PROC-V queda CERRADA en lo que depende del
ejecutor. Escrituras en el repo: `docs/tesis/figuras/generar_figura_proceso_extraccion.py`,
`docs/tesis/figuras/figura_proceso_extraccion.png`,
`docs/tesis/figuras/figura_proceso_extraccion.svg` y este reporte. Commit:
PENDIENTE de la autora.

---

Grep de convenciones (nombres propios de personas y referencias a origen
conversacional) sobre este archivo: pegado en el reporte de cierre de la
unidad.
