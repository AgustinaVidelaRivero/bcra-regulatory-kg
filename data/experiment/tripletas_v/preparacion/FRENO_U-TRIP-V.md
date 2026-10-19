# U-TRIP-V — FRENO (19/10/2026; USD 0, sin API, sin Neo4j; sin escribir en el repo y sin commit)

Preparación de la etapa V de la evaluación por tripletas. Rige el pre-registro FIRMADO (`docs/preregistro_evaluacion_tripletas.md`,
firma en `4afbe51`, texto firmado sha256 `8ce611ba…`), con sus notas al pie y sus enmiendas 1 (umbrales) y 2 (desambiguación, firmada
en `593e5db2`). Todo sale por script (`scripts/`), con su salida en `salidas/`. **No hay ningún juicio sobre ninguna arista**: ni en
las fichas, ni en este FRENO, ni en la consola.

## 1. Paso 0

Primera corrida (la carpeta personal, como `$HOME`):

```
$ pwd
$HOME/INGENIERIA IA/TESIS/fuera_del_repo/tripletas_v
$ find . -print | sort
.
./insumos
./insumos/items_U-MED-DESAMB_para_el_solapamiento.json
$ git -C "$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg" --no-optional-locks log -1 --format='%h %s'
a7d00025 Preguntas de la evaluacion final: el mandato firmado sin abstencion, con la caida por clase y cuatro preguntas por documento
$ git -C <repo> --no-optional-locks status --porcelain --untracked-files=no
(vacío)
$ shasum -a 256 insumos/items_U-MED-DESAMB_para_el_solapamiento.json
57eca4e3ae9b028d478b37dd71244fe7817ec3d105dbf4c58937723b5b70f8c1  insumos/items_U-MED-DESAMB_para_el_solapamiento.json
```

- **El título no era el del despacho:** HEAD era `a7d00025`, un commit después de `593e5db2`. Frené sin escribir nada.
- **Se siguió con `a7d00025`** por decisión de la autora: todo se lee con los blobs de ese HEAD.
- **El diff de nombres contra `593e5db2`** no toca ningún insumo:

  ```
  $ git diff --name-status 593e5db2 a7d00025
  A	docs/mandatos/UPREG_B63_preguntas_por_tipo.md
  M	docs/registro_decisiones_calidad_y_evaluacion_2026-10-15.md
  ```

- **HEAD no se movió mientras trabajé.** `00_control_insumos.py` corrió al empezar (14:21:37) y al cerrar (14:28:42).
  - Las dos veces: HEAD `a7d00025`, el status vacío y el diff `a7d00025..HEAD` vacío.
  - 0 commits nuevos que toquen el pre-registro, sus enmiendas, el kg.json, la E0, los PDF o `grafos.py`.

## 2. La copia y los blobs

- **El rsync** es el de la cláusula, a `<scratchpad>/copia/`, con salida en `<scratchpad>/copia.rsync.log` (en el paquete:
  `salidas/copia.rsync.log`).
  - rc 0.
  - El log tiene 336 líneas, todas `skipping non-regular file`. Son los enlaces de
    `data/experiment/ev2_corrida/navegabilidad/trazas_nav/ev2_base_{run3,v2,v3}/`: 120, 88 y 128.
- **El `find` de justo después,** antes de correr nada, da 0 para los cuatro nombres (`.env*`, `*.env`, `NO_ABRIR_*`, `*_SOLO_MESA*`) y
  0 enlaces.
- **Blobs:** 76 de 76 iguales en tres lados: la copia (`git hash-object`), `git ls-files -s` y `git ls-tree a7d00025`.
  - Son 19 archivos usados (los tres documentos que rigen, `grafos.py`, el grafo, el sellado anterior, el diff del re-sellado y su
    FRENO, la cadena de ensamblado y los precedentes) y los 57 rastreados de la E0.
  - El `kg.json` da `66e745f57397ab754cde09eb641e9f0d9ef6259ea7e6445d086ecbf1c36dcc6c`.
- **Los PDF no están en git** (`.gitignore:35`, `data/experiment/**/*.pdf`). No tienen blob: van por sha256 y son iguales byte a byte
  a los del repo.

  | PDF | sha256 |
  |---|---|
  | `TO_capitales_minimos_actual.pdf` | `f6ab71be7783c4192e67c13ee84f1fc585c6ae5e05aa074961c9c59429280bb8` |
  | `TO_clasificacion_deudores_actual.pdf` | `6e7f528d3fea7b756f15e1278eecd828f203f0651fc6f778212033de6a0883e2` |
  | `TO_exterior_cambios_actual.pdf` | `baea7264918877da132acca5f7ec6df1a3a33fd5be77109b90360a3d586bc130` |
  | `TO_proteccion_usuarios_servicios_financieros_actual.pdf` | `48564cc714daa9a8c8bbd7115dfe006307ca7cb1c3d78b106c52555fe75a12ec` |
  | `TO_regimen_informativo_contable_mensual_actual.pdf` | `754c888ae6034f63eb04991c5cad441435b6bf6f8e8fb3669fd2bb279c3b35d5` |

## 3. La población por predicado y la lista de fuera (§3.1)

**El grafo** es KG-Tanda0-Desarrollo-r2b-sincola-rs1 (`66e745f5…`, 6.711 nodos y 21.996 aristas, sellado en `4fe6ece`), el sello vigente
al sortear.

**N = 3.967, y no 3.983 como dice el texto firmado.**

| predicado | texto firmado (`2922b72d`) | grafo medido (`66e745f5`) | diferencia |
|---|---|---|---|
| `aplica_a` | 1.770 | 1.765 | −5 |
| `condicion_de` | 1.379 | 1.378 | −1 |
| `limita` | 267 | 266 | −1 |
| `regula` | 169 | 169 | 0 |
| `requiere` | 117 | 117 | 0 |
| `condiciona` | 85 | 85 | 0 |
| `exceptua_obligacion` | 69 | 65 | −4 |
| `exceptua` | 62 | 58 | −4 |
| `prohibe` | 54 | 53 | −1 |
| `ejecuta` | 11 | 11 | 0 |
| **total** | **3.983** | **3.967** | **−16** |

- **El recuento del texto firmado se reproduce** sobre `2922b72d`.
- **La diferencia sale del re-sellado único:** 83 aristas de contenido salen y 67 entran.
  - Todas tienen causa en el diff declarado del re-sellado
    (`resellado_t0/salidas/diff_contra_sellado/diff_declarado_contra_sellado_r2b_sincola_desarrollo.json`). Hay 0 sin causa.
  - Salen: R0 40, O2:G-r 24, O2:f′ 18 y O2:f 1.
  - Entran: R0 26, O2:G-r 24, O2:f′ 16 y O2:f 1.
  - O2 es el código de U-OMISIONES-COD y R0, las salidas de R0.
- **Las claves:** `fuente|predicado|destino`, 0 repetidas y 0 ids de nodo con «|».
- **Ninguna de las 3.967 lleva `rol_fuente`:** todas vienen de las relaciones de E1, por `e2_lib.ensamblar_r2`.

**Lista de fuera:** `establecida_en`, `instancia_de`, `miembro_de`, `modificada_por`, `padre_sugerido`, `parte_de`, `referencia`,
`remite_a` y `subclase_de`. Son los nueve del texto firmado. **No se agrega ninguno, y ninguno de contenido sale.**

La cadena que lo controla es `resellado_t0/scripts/cadena_rs1.sh`, grafo `r2b_sincola_desarrollo`:
`ensamblar_tanda0.py --manifiesto tanda0_ens_desarrollo_r2b_sincola_rs1.json --entrada salida_r2b --e0-r2 salida_tanda0_r2b
--sin-cola`. Lo que `correr_cadena_r2` deriva por código:
- el esqueleto: `subclase_de`, `miembro_de`, `instancia_de` y `parte_de` (`schema.RELACIONES_ESQUELETO`), más `padre_sugerido`
  (`inyectar_esqueleto_v3`);
- `remite_a` y `referencia` (`r1_referencias.detectar_y_resolver`; `modelos_r2.PREDICADOS_DERIVADOS`);
- `establecida_en` (`derivar_establecida_en`; `modelos_r2.PREDICADOS_DERIVADOS_DE_PROCEDENCIA`).

Los predicados del esquema de E1 (`modelos_r2.PREDICADOS`), sin `establecida_en`, `referencia` y `modificada_por`, son exactamente
las diez de contenido. El grafo no tiene ningún predicado fuera de las dos listas.

## 4. La asignación (§3.2), escrita antes de sortear

`salidas/asignacion_V.json` (sha256 `8633e9b4…`), escrita a las 14:22:41.

- **La regla:** proporcional, con un mínimo de 3 por predicado de 30 aristas o más; los de menos de 30 van a «otros», sin mínimo.
  - Los estratos que quedan por debajo de 3 se fijan en 3, y los 85 que quedan se reparten en proporción entre los demás.
  - El redondeo es por restos mayores. El empate se resuelve con `random.Random(f"{semilla}:empate")`, pero no hubo empate.
  - Suben por resto `aplica_a` (0,80) y `condicion_de` (0,64).

| estrato | N_h | W_h | n_h |
|---|---|---|---|
| `aplica_a` | 1.765 | 0,4449 | 42 |
| `condicion_de` | 1.378 | 0,3474 | 33 |
| `limita` | 266 | 0,0671 | 6 |
| `regula` | 169 | 0,0426 | 4 |
| `requiere` | 117 | 0,0295 | 3 |
| `condiciona` | 85 | 0,0214 | 3 |
| `exceptua_obligacion` | 65 | 0,0164 | 3 |
| `exceptua` | 58 | 0,0146 | 3 |
| `prohibe` | 53 | 0,0134 | 3 |
| otros (`ejecuta`) | 11 | 0,0028 | **0** |

- **«otros» queda sin muestra.** Así lo pide la letra del §3.2, y la autora lo decidió antes del sorteo.
  - Su cuota proporcional (0,26) redondea a 0.
  - p̂_w cubre 3.956 de 3.967 y se informa con las dos cotas de ese estrato.
  - Las de `ejecuta` entraban al pool solo si el sorteo las elegía, sin forzarlo; no salió ninguna.

## 5. El sello

**Sello:** `salidas/acta_sorteo_V.json`, sha256 `5d6a237e510bcf086db717061dd146eaa9b3181006cb7b1d300164436c720c55`.
`salidas/sello_sorteo_V.txt`: ese sha256 y la hora, 2026-10-19T14:23:55-03:00.
- **Semilla:** `B4-TRIPLETAS-V:sorteo:2026-10-07`.
  - **No está escrita en el repo:** `git log --all -S` y el grep en `docs/` y `data/experiment/` dan 0. Viene del despacho, y el
    acta lo declara.
- **El sorteo,** con Python 3.12.13 a las 14:23:55:
  - las 100: `Random(f"{semilla}:{estrato}").sample(sorted(claves), n_h)`;
  - el pool: `Random(f"{semilla}:pool").sample(sorted(resto), 20)`;
  - el orden: `Random(f"{semilla}:orden").shuffle(sorted(las 100))`; V001–V010 son el piloto, y V011–V100 los lotes 01 a 09.
- **Los sha256 sellados** (de `json.dumps(…, ensure_ascii=False, separators=(',', ':'))`):

  | qué | sha256 |
  |---|---|
  | la población (la lista) | `45cc64de5b8b25fd04c2590c857cb1776af2172f67ff3c2d5b95bf0630175894` |
  | `poblacion_V.json` | `0c83f18fb9e3409c736e0ecd341bc9d41cfa5426d994002df346577a35c34e31` |
  | las 100 (por estrato, en el orden del sorteo) | `97607733908d5bf0aad560e7736780d2c1cbdbbe7883c9f1b66299c1f55caec5` |
  | el pool | `4a87fd8cfbb81d35d6c07363cb03280be9e6e6d1ba39823d5a025365b94a5d81` |
  | el orden | `e061f6729ecd1ce5da8f7b471a76772c6e0debcd618be14b9e03f73fa4cb2252` |
  | los lotes | `14587dad2daab668c8f73786365faf60b9ea19ffb348a6aefee0f2d6a4b3f172` |

- **Cómo quedaron repartidas.**

  | | las 100 | el pool de 20 |
  |---|---|---|
  | por TO | ext 39, cap 32, pro 12, cla 11, ric 6 | ext 9, cap 7, pro 2, cla 1, ric 1 |
  | por predicado | las de la asignación | `aplica_a` 7, `condicion_de` 4, `regula` 3, `requiere` 3, `limita` 2, `prohibe` 1 |

## 6. Los solapamientos, en el acta (ninguna sale de la muestra)

**Con U-MED-DESAMB (enmienda 2, §1): 5,** 4 en las 100 y 1 en el pool.
- **El criterio:** el mismo predicado (`aplica_a` o `ejecuta`), el `chunk_id` del ítem entre las procedencias, y el `resuelto_a` del
  ítem como extremo Sujeto. El acta lo declara como la forma de contar «la misma norma como extremo de contenido».
- **Las cinco:**

  | ref | lote | ítem | `chunk_id` | sujeto |
  |---|---|---|---|---|
  | V012 | lote 01 | D020 | `cap::4.3.3.1` | `Sujeto_rol_alcance_capmin` |
  | V024 | lote 02 | D038 | `pro::3.2.1.1` | `Sujeto_proveedor_no_financiero_de_credito` |
  | V055 | lote 05 | D051 | `pro::2.3.1.4` | `Sujeto_rol_sujeto_obligado_proteccion` |
  | V089 | lote 08 | D054 | `pro::2.3.2.2` | `Sujeto_rol_sujeto_obligado_proteccion` |
  | P14 | pool | D037 | `ext::15.1` | `Sujeto_rol_entidad_autorizada_exterior` |

- Con el mismo predicado y el mismo chunk pero otro sujeto hay 0 (informativo).

**Con U-LECTURA-ACEPTADAS (pre-registro, `:41-42`): 2,** las dos en las 100 y ninguna en el pool.
- **El criterio:** la procedencia incluye una unidad de la muestra de `sellos_l0.json` (60), por `chunk_id` exacto.
- **Las dos:**
  - V025 (lote 02), `cap::3.1.3::cierre`;
  - V095 (lote 09), `cla::10.2.1`.

  Las dos son del estrato no_item de L0. Por la unidad base solamente no hay ninguna más.

**Ninguna de las siete está en el piloto.**

## 7. Las fichas y las hojas

**Las fichas** (`fichas/`), generadas a las 14:25:19, después del sello:
- `fichas_V.jsonl`, con las 120 (sha256 `2a1cb858…`);
- un `.md` por lote: `fichas_piloto.md`, `fichas_lote_01.md` … `fichas_lote_09.md` y `fichas_pool.md`;
- `fichas_V_cabecera.json`.

Cada ficha trae:
- **Los dos nodos:** id, tipo, etiqueta, descripción y propiedades.
- **El predicado.**
- **De la arista:** el calificador y sus propiedades no definidas, si los tiene. En `aplica_a` y `ejecuta`, además, el tramo del
  sujeto: la mención que la arista toma como sujeto, con su condición de literal.
- **La evidencia de cada procedencia,** que en las 120 es una sola:
  - el texto heredado y el propio de la unidad de E0;
  - los avisos de E0 que valen `true` (tabla o fórmula);
  - el tramo de cada extremo en esa unidad, con su condición de literal (exacta, tokens o no);
  - las páginas y la ruta del PDF con `#page=N`.

**Lo que la ficha no trae** (las marcas del pipeline, para que la mesa lo revise antes del piloto):
- **Propiedades del nodo:** `cuarentena`, `padre_sugerido`, `padre_por_defecto` y, si aparecen, `cola_humana`, `cola_chunks` y
  `estado_e3`.
- **Propiedades no definidas:** `copia_nota_e3`, `modalidad_clasificada` y las cuatro `umbral_no_cuantificable*`. Las demás
  (`modalidad`, `cuantificador`) van, marcadas como «no definida en el esquema».
- **Del nodo:** `originales`, `fuera_de_lista`, `rol_fuente`, `campos_heredados_v3` y `valores_no_tipados`.
- **En cada umbral** van valor, unidad, moneda, comparación, tipo de días, base, destino de la base y tramo. No van
  `regla_comparacion`, `origen`, `tramo_verificado`, `verificado_en_tabla`, `base_no_resuelta`, `base_via` ni `originales`.
- **De la arista:** `mencion_verificada` (su valor se muestra solo como la condición de literal del tramo del sujeto),
  `metodo_resolucion`, `sujeto_id_modelo`, `sujeto_mencion_modelo`, `coherencia_tipo_predicado` y `no_verificada_e3`.
- **Tampoco:** ni el estado de E3, ni los reintentos, ni las marcas de la cola, ni el estrato, ni el solapamiento.

**Las páginas de una procedencia `herencia_*`** son las del heredado de su punto, por la regla del ensamblado
(`ensamblar_tanda0.py:1247-1254`).
- Le pasa a 3 de las 120: V020, V038 y P20. Cambia algo solo en V038 (`ext::3.16.3.4`, punto 3.16.3), que va con las páginas 45 y 46
  mientras la unidad está en la 46.
- La ficha muestra las páginas de la procedencia y las de cada tramo heredado.

**Las hojas** (`lectura/`, vacías; no van en el paquete: van por su sha256 en el `manifest.txt`):
- `hoja_piloto.csv` y `hoja_lote_01.csv` … `hoja_lote_09.csv`:
  - en la cabecera, la hoja, el sha256 del acta, `hora_inicio` y `hora_fin`;
  - por fila: orden, ref, predicado, clave, `correcta` (sí, no o no decidible), `importancia` (esencial, útil o accesoria),
    `nota` y `observacion_umbral` (opcional, sin cifra).
- `hoja_pool.csv`, con las 20:
  - los cinco componentes (`comp_sujeto`, `comp_predicado`, `comp_valores`, `comp_calificadores` y `comp_modalidad`): sostenido,
    contradicho o no consta;
  - `requiere_adjudicacion`: sí o no;
  - los tres rasgos (`rasgo_conducta_exigible`, `rasgo_valor_concreto` y `rasgo_relacion_principal`): sí o no;
  - `nota`.
- `lectura/sellar_hoja.py` (sha256 `eb5e1ed0…`) es el sello de cada hoja:
  - controla la cabecera y las horas, las filas del lote sellado y que cada celda obligatoria tenga un valor permitido (sin
    importar mayúsculas ni tildes);
  - si pasa, escribe `sello_hoja_<lote>.txt` con el sha256, el nombre y la hora, como el sello de los calibradores de U-MED-DESAMB;
  - no pisa un sello que ya existe.
  - Lo probé sobre copias en el scratchpad, que después borré:
    - rechaza la hoja vacía (rc 1), un valor inválido y dos filas cambiadas de orden;
    - sella con valores permitidos, también si la hoja viene exportada con `;` y BOM;
    - no pisa un sello.
- **Para sellar,** desde `tripletas_v/lectura/`: `python3 sellar_hoja.py hoja_piloto.csv`.

## 8. Los controles (`salidas/05_controles.json`, todos OK)

- **El sorteo se reproduce con la semilla.** La población, recomputada desde el kg.json, da las mismas filas y el sha256 sellado. La
  asignación recomputada da los mismos n_h. Las 100, el pool, el orden y los lotes dan sus sha256.
- **Cada procedencia está en la E0, y cada página en su PDF.**
  - Las 120 procedencias están en la E0, con el mismo TO y archivo y las páginas según la regla de arriba.
  - Las 659 páginas (de las procedencias y de lo heredado) existen en su PDF. Según `pdfinfo`: cap 204, cla 60, ext 201, pro 40 y
    ric 59.
- **Ninguna ficha trae vacío un campo que la evidencia tenga.** Se controló la descripción, las propiedades, los umbrales, el texto
  propio, lo heredado, las páginas, el PDF, los tramos de cada extremo, el tramo del sujeto y el calificador.
- **Las 100 y el pool son disjuntos.**
- **Los controles negativos dan bien:**
  - 0 claves de marca o de juicio en las fichas;
  - las horas van en orden: asignación 14:22:41 < sorteo 14:23:55 = sello 14:23:55 < fichas 14:25:19;
  - las 11 hojas tienen las filas de su lote sellado, con las celdas de juicio y las horas vacías.

## 9. Errores propios

1. **Las fichas se generaron dos veces.**
   - La primera, a las 14:25:03, tenía una errata en el título de los `.md` («fichas de el …»). Las regeneré a las 14:25:19.
   - El `.jsonl` da el mismo sha256 en las dos (`2a1cb858…`). Solo cambiaron los títulos de los `.md`, y los de la primera se
     pisaron.
2. **La primera corrida de `05_controles.py` dio `ok: false`.**
   - El control comparaba las páginas de la procedencia con las de la unidad, sin la regla de las procedencias `herencia_*`
     (`ext::3.16.3.4`).
   - Corregí el control, no los datos, y la segunda corrida da OK. La consola de la primera se pisó.
3. **Para controlar el formato de los `.md`, leí en la consola la ficha P01 y parte de la P02 del pool.** No juzgué ninguna, y no
   leí ninguna ficha del gold.
4. **`codigo_sha256` del acta cubre los scripts que existían al sortear:** `comun_v.py`, `00`, `01` y `02`. Los `03` a `06` se
   escribieron después, y `05` se corrigió después de su primera corrida. Los sha256 de todos van en el `manifest.txt`.
5. **En las pruebas del sellado, el rc de dos casos salió vacío,** porque usé `PIPESTATUS` en zsh. El rc 1 del rechazo lo comprobé
   aparte.

## 10. Lo abierto para la mesa

- **Los campos de la ficha (§7), antes de que la autora abra el piloto.** Lo que más importa revisar:
  - que vaya el tramo del sujeto;
  - que vayan los avisos de E0;
  - la lista de lo que no va.
- **La semilla no está escrita en el repo:** viene del despacho.
- **La nota para el pre-registro:** el sorteo de la etapa V corrió sobre `66e745f5…`, con N = 3.967 y «otros» sin muestra.
