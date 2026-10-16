# U-SEG-OFICIAL — REPORTE de S2

Despacho de S2, versión 2 (15/10/2026), con las decisiones D-1 y D-2 de la autora y la decisión 6. USD 0, sin API. Nada
commiteado, ningún mensaje de commit preparado, nada escrito en la memoria. Escribí solo en
`data/experiment/segmentacion_oficial_e0r2/s2/` y en el scratchpad de la sesión.

## Tramo 1 (15/10/2026): la E0, la lista de la tanda 1 y U

### 1.1. Fuentes, leídas en su commit

| fuente | commit | control |
|---|---|---|
| `docs/mandatos/USEG_OFICIAL_segmentacion_e0r2.md` (S2, `:164-207`; notas del 13 y del 15/10/2026, `:925-1017`) | `4e4f3636` (HEAD) | árbol igual a HEAD |
| `docs/enmienda8_protocolo_entre_tandas_2026-10-15_calendario_hacia_B6.3.md`, firmada | `54902301` | sin cambios desde la firma (`git log` del archivo) |
| `docs/protocolo_entre_tandas.md`, §5 (`:159-191`) y §7 (`:253-295`) | firma en `a304b89` | §5 y §7 iguales a los de `a304b89` (`diff` de las dos secciones, vacío) |
| `data/experiment/catalogo_unico/registro_alcance_por_tanda.md` | `85ff21f9` | árbol igual a HEAD |
| `docs/plan_tesis.md:770` y `docs/checklist_pre_escalado.md:149` (R33) | `3c5f0034`, `aabe6986` | árbol igual a HEAD |

El pre-registro de la tanda 1 que cita el despacho (§1.3 y §3) es un borrador de la mesa fuera del repo: no lo leí. La lista de
trabajo la tomo del despacho y de `docs/mandatos/USEG_OFICIAL_segmentacion_e0r2.md:774-775`; la fórmula del tope, del despacho y de la
enmienda 8, §8.

### 1.2. La E0 corregida, una vez, en una copia

- **Copia:** `rsync` de la cláusula de los despachos, con un `--exclude='NO_ABRIR_*'` agregado por la cláusula de carpetas vedadas
  (el repo tiene un archivo con ese prefijo, abajo). rc 0. Después, por nombre: 0 `.env`, 0 `NO_ABRIR_`, 0 enlaces. `--no-links`
  dejó fuera 336 enlaces simbólicos (todos en `data/experiment/ev2_corrida/navegabilidad/trazas_nav/`; E0 no los usa). La copia no
  tiene el `.env.example` rastreado de `run_2_papers/code/`; ningún control compara la copia con el repo archivo por archivo.
- **Raíz mínima:** `s0_4/scripts/raiz_minima.sh <copia> <raíz> <copia>/data/experiment/reextraccion_v2/e0_chunking` (0 enlaces). El
  código de la raíz da los sha256 del paso 0 (`e0_lib.py` `d89aab1a…`, `correr_e0.py` `78c54c4c…`, `e0_tablas.py` `ab300a22…`).
  `correr_152.py` y `raiz_minima.sh` de la copia, iguales a los del repo (`d5d0c5e8…`, `68d90eb1…`).
- **Corrida:** `.venv/bin/python -B s0_1/scripts/correr_152.py --codigo <raíz> --salida <dir> --workers 8`, con
  `PYTHONDONTWRITEBYTECODE=1`, de 14:47:34 a 14:53:08, rc 0, «listo 152 TOs, 0 con error» (`controles/corrida_152_S2a.txt`).
- **Control** (`scripts/control_e0_contra_manifiesto_S2.py`; `controles/control_e0_S2a.json`): contra
  `s0_6/b/manifiestos/manifest_salida_e0_152_S0-6b.json` (`80adbd58…`, el del despacho), **768 de 768 archivos `e0/…` presentes y con
  su sha256 y sus bytes**, ninguno de más ni de menos; **152 TOs y 10.478 unidades**; `unidades_por_to` igual al del manifiesto.
  Veredicto OK.
- La salida queda en el scratchpad para el tramo 2. No va al paquete de revisión: tiene el texto de todas las unidades, es byte a
  byte la del manifiesto de S0-6b (rastreado en el repo) y el lote del §1.6 la regenera en unos 6 minutos, USD 0. Un tar.gz con el
  prefijo `NO_ABRIR_` habría que copiarlo con `ditto`, y la cláusula de carpetas vedadas prohíbe copiar archivos `NO_ABRIR_`.

### 1.3. Unidades de extracción

Son las entradas de `chunks_<to>.json` de la E0 corregida: chunks terminales y mini-chunks (`correr_e0.py:14`;
`escalado_prep/reporte_generalizacion.md:56`). El runner de la extracción las carga todas
(`reextraccion_v2/corpus_v2/runner_corpus.py:616`, `e1_extractor/comun_e1.py:40-49`). Para los 20 de la lista, la cifra es la misma
en las tres fuentes: `len(chunks_<to>.json)`, `unidades_por_to` del manifiesto de S0-6b y `chunks` de `conteos.json`
(`unidades_extraccion_igual_a_unidades_por_to: true` en `lista_tanda1_S2.json`). No declaro diferencia.

Un límite de la cifra: en la corrida, una unidad que E1 parta por corte se reemplaza por sus partes
(`runner_corpus.py:569-579`, `chunks_con_partes`). Esas partes no están en U.

### 1.4. La lista de la tanda 1

Sale ri_oc (enmienda 8, decisión 1: error de corte confirmado en S1-quater; 197 unidades, `sin_raiz`). Su sucesor en el estrato 6,
por D-1, es **ri_mmsef** (§1.5). ri_pgn queda en el estrato 2 por D-2 (decisión de la autora del 07/10/2026,
`registro_alcance_por_tanda.md:37`). **El orden del §7 no lo recomputé.**

Los 20, en la E0 corregida (`lista_tanda1_S2.json`, `filas`; clase: NG normativa general, RI régimen informativo, de
`escalado_prep/inventario_tos.csv`):

| estrato | TO | clase | modo (E0 corregida) | unidades | cobertura exacta | ids repetidos | fila en el registro de alcance |
|--:|---|---|---|--:|---|--:|---|
| 1 | ayccef | NG | `vigente` | 196 | sí | 0 | no (rol en el manifiesto de los 152: `Sujeto_entidad_financiera`) |
| 1 | expaef | NG | `vigente` | 165 | sí | 0 | no (rol en el manifiesto de los 152: `Sujeto_entidad_financiera`) |
| 1 | opefci | NG | `vigente` | 74 | sí | 0 | no (rol en el manifiesto de los 152: `Sujeto_entidad_financiera`) |
| 1 | adrei | NG | `vigente` | 70 | sí | 0 | no (rol en el manifiesto de los 152: `Sujeto_rol_alcance_adrei`) |
| 2 | ri_ccna | RI | `sin_raiz` | 169 | sí | 0 | tabla de la tanda 1, `:20` |
| 2 | ri_rml | RI | `vigente` | 46 | sí | 0 | tabla de la tanda 1, `:21` |
| 2 | ri_gerc | RI | `vigente` | 15 | sí | 0 | tabla de la tanda 1, `:22` |
| 2 | ri_pgn | RI | `vigente` | 21 | sí | 0 | tabla de la tanda 1, `:23`; candidatos, `:61` (decidido) |
| 3 | snp_cheq | NG | `vigente` | 265 | sí | 0 | tabla de la tanda 1, `:26` |
| 3 | ceninf | NG | `sin_raiz` | 39 | sí | 0 | tabla de la tanda 1, `:27` |
| 3 | cirmo3 | NG | `vigente` | 256 | sí | 0 | tabla de la tanda 1, `:28` |
| 3 | snp_tr | NG | `vigente` | 103 | sí | 0 | tabla de la tanda 1, `:29` |
| 4 | lingeef | NG | `vigente` | 613 | sí | 0 | no (rol en el manifiesto de los 152: `Sujeto_entidad_financiera`) |
| 4 | depaho | NG | `vigente` | 442 | sí | 0 | no (rol en el manifiesto de los 152: `Sujeto_rol_alcance_depaho`) |
| 4 | cajasc | NG | `vigente` | 287 | sí | 0 | no (rol en el manifiesto de los 152: `Sujeto_caja_de_credito_cooperativa`) |
| 5 | manori | NG | `vigente` | 152 | sí | 0 | tabla de la tanda 1, `:30` |
| 5 | efemin | NG | `vigente` | 119 | sí | 0 | no (rol en el manifiesto de los 152: `Sujeto_rol_alcance_efemin`) |
| 5 | nmcief | NG | `sin_raiz` | 55 | sí | 0 | tabla de la tanda 1, `:31` |
| 6 | ri_dcpc | RI | `marcadores` | 75 | sí | 0 | tabla de la tanda 1, `:25` |
| 6 | ri_mmsef (sucesor) | RI | `sin_raiz` | 128 | sí | 0 | solo en la tabla de candidatos, `:60` (candidato, no decidido) |

- **La columna del registro:** 11 TOs tienen su fila de decisión en la tabla de la tanda 1 (los 12 de esa tabla menos ri_oc); 8 no
  tienen fila y sí `rol_alcance` en el manifiesto de los 152 (`s1ter/manifiesto/segmentacion_oficial_e0r2_152.json`, `818c3a43`): son
  «los 8 del ejemplo que ya tenían alcance» (`registro_alcance_por_tanda.md:33-35`); ri_mmsef no tiene fila de decisión ni
  `rol_alcance`: figura entre los candidatos a la regla del título (`:60`, `Sujeto_entidad_financiera`). 11 + 8 + 1 = 20. Lo que
  sigue con el alcance lo hace A2 de U-ALCANCE-E1.
- **El par de la escalera (estrato 6):** ri_dcpc, `marcadores` en la E0 corregida y en la partición legada (`conteos_b584.json`,
  `modo_lectura`); ri_mmsef, `sin_raiz`. No hay nada que declarar sobre ri_dcpc.
- **Los 20 cumplen las dos condiciones de entrada que pide el despacho:** cobertura exacta y ningún id de chunk repetido
  (`docs/plan_tesis.md:770`; R33).

**U = 3.290 unidades de extracción** (`lista_tanda1_S2.json`, `U`): 505 + 251 + 663 + 1.342 + 326 + 203 por estrato; 2.836 en 14 TOs
de normativa general y 454 en 6 de régimen informativo (`por_categoria`); 2.824 en 15 TOs `vigente`, 391 en 4 `sin_raiz` y 75 en 1
`marcadores` (`por_modo_lectura`).

**El tope: 1,45 × 3.290 × 0,021115 = USD 100,7291** (`tope_usd`), unos USD 100,73.

Con la lista de trabajo (con ri_oc, sin sucesor), U sería 3.359 y el tope USD 102,8417 (`unidades_lista_de_trabajo`,
`tope_usd_lista_de_trabajo`). La enmienda 8, §8, dice «unos 102,9 con la lista de trabajo», sin ancla en el texto; con la E0
corregida da 102,84. Con el manifiesto de S0-6a (`s0_6/manifiestos/manifest_salida_e0_152_S0-6a.json`) la lista de trabajo da 3.394 y
103,91. No encuentro de dónde sale 102,9; es una cifra aproximada de la enmienda y no cambia nada de lo que fija este tramo.

### 1.5. El sucesor de ri_oc (D-1)

**La regla:** entre los elegibles con modo `sin_raiz` en la E0 corregida, el de más unidades de extracción, con desempate por id, que
no supere en más de 600 unidades a ri_oc. ri_oc tiene 197, así que **el tope es 797 unidades** (`d1.tope_unidades`).

**Los elegibles, en cascada disjunta sobre los 152** (`d1.cascada_disjunta_sobre_los_152`: cada TO cuenta solo en el primer motivo
que lo excluye, en el orden de las condiciones del despacho):

| motivo | excluidos | quedan |
|---|--:|--:|
| en la lista de trabajo (los 20, ri_oc incluido) | 20 | 132 |
| tanda 0 (ctacte, docvig, lingob, pagjub, polcre) | 5 | 127 |
| los 14 de fuera (`docs/protocolo_entre_tandas.md:163-166`) | 14 | 113 |
| ri_ao, ri_cc o ri2_pm (ri2_pm ya salió como parcial) | 2 | 111 |
| los 15 de las decisiones 1 y 2 de la enmienda 8 (los 4 restantes ya salieron) | 11 | 100 |
| cobertura no exacta (rdbcra) | 1 | 99 |
| ids de chunk repetidos | 0 | 99 |
| modo distinto de `sin_raiz` | 72 | 27 |

Suma de excluidos: 20 + 5 + 14 + 2 + 11 + 1 + 0 + 72 = 125; 152 − 125 = 27. Los 5 de desarrollo no están en los 152. Las listas de
los 14 de fuera las controla el script contra `particion_152.json` (clases `no_segmentable_declarado` y `parcial_declarado`).

**Los 27 elegibles, ordenados** (unidades; ninguno supera 797, así que el tope no actúa): 1. ri_mmsef 128, 2. ri_ii_31_12_19 91,
3. cedin 66, 4. ri_sef 38, 5. seggar 36, 6. ri_secoexpo 35, 7. consyr 34, 8. ri_ot 32, 9. ri_nge 30, 10. ri_dsf 28, 11. ri_laft 26,
12. ri_tar 18, 13. ri_pspapt 16, 14. ri_iepsp 13, 15. ri_iesinap 12, 16. ri_transpa 11, 17. asomut 8, 18. micemp 8, 19. ribspc 7,
20. ri_acsf 6, 21. ri_cr 6, 22. ri_tvf 6, 23. ri_esd 5, 24. verac 5, 25. ri_ieccm 4, 26. ri_rcl 4, 27. ri_bdp 3
(`d1.candidatos_ordenados`). El primero no tiene empate.

**El sucesor: ri_mmsef**, 128 unidades, régimen informativo, `sin_raiz`, cobertura exacta, 0 ids repetidos.

### 1.6. El comando

Desde la E0 corregida ya corrida:

```
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/segmentacion_oficial_e0r2/s2/scripts/lista_tanda1_S2.py --e0 <salida de E0 de los 152> --raiz <copia del repo> --out <json>
```

De punta a punta (copia sin `.env`, raíz mínima, los 152, control contra el manifiesto de S0-6b y la lista), en una carpeta nueva
fuera del repo:

```
zsh data/experiment/segmentacion_oficial_e0r2/s2/scripts/lote_tramo1_S2.sh <repo> <trabajo>
```

La lista corrió dos veces sobre la misma E0, la segunda con `PYTHONHASHSEED=7`: iguales byte a byte (`22f33a17…`).

**Prueba del lote de punta a punta** (después de escribir `s2/`): `zsh s2/scripts/lote_tramo1_S2.sh <repo> <trabajo>`, de 14:57:05 a 15:03:57, rc 0, con su propia copia (0 `.env`, 0 `NO_ABRIR_`; 336 enlaces no copiados) y su propia corrida de los 152. Su control contra el manifiesto de S0-6b y su `lista_tanda1_S2.json` son iguales byte a byte a los de este tramo (`cmp`).

### 1.7. Lo que este tramo encontró fuera de lo que pide, para la mesa

1. **rdbcra no tiene cobertura exacta en la E0 corregida:** 1.652 líneas en la estructura contra 1.646 parseadas, 6 duplicadas, 0
   huérfanas (`cobertura.json`, `rdbcra`). En la partición legada, `cobertura_exacta` es `true` (`conteos_b584.json`). Es `vigente`,
   así que no cambia el sucesor; sí importa para la tanda final (`docs/plan_tesis.md:770`). No rastreé desde qué corrida de S0 viene.
2. **ri_mmsef entra a la tanda 1 sin alcance decidido** (fila de candidato en `registro_alcance_por_tanda.md:60`; `rol_alcance` null
   en el manifiesto de los 152). Y sus detecciones de la release de E0 (límites de sub-documento y candidatos del hallazgo 1.16)
   estaban contadas fuera de la tanda 1 (criterio de tandas del protocolo, `:175-182`); el re-censo del tramo 3 es sobre la tanda
   final, que ya no lo incluye. Si se miden para la tanda 1, lo decide la autora.
3. **ri_spi en la tanda final de la enmienda 8:** las 344 unidades de la decisión 1 (§1 y decisión 1 de la versión para firmar)
   incluyen las 96 de ri_spi (248 sin él; `unidades_por_to` del manifiesto de S0-6b), pero el protocolo lo cuenta entre los 12 no
   segmentables de fuera (`:163-166`). No cambia el tramo 1 (ri_spi sale por los dos lados); el tramo 3 tiene que declarar cuál de
   las dos lecturas usa para contar la tanda final.
4. **El health-check de E0 por TO** (protocolo, §4, condición 5) no lo corrí: el despacho no lo pide para la lista.
5. **El modo `sin_raiz_letra`** lo tiene solo ri_spi (`modos_en_los_152`: 91 `vigente`, 55 `sin_raiz`, 5 `marcadores`, 1
   `sin_raiz_letra`). D-1 dice `sin_raiz` y lo leí literal; ri_spi sale igual por la enmienda 8.

### 1.8. Repo, `.pyc` y convenciones

- **Foto sha256 del repo entero, sin `.git`, antes** (`scripts/foto_repo_S2.py`): 14:46:03 a 14:46:14, 50.530 entradas, con 8 sin
  abrir (7 `.env*` y 1 `NO_ABRIR_`, solo por tamaño y fecha) y 342 enlaces (por su destino). La de después va en el mensaje del
  FRENO: este archivo entra en ella.
- **El archivo `NO_ABRIR_` del repo:** `data/experiment/med_umbrales/p/lote1/freno/NO_ABRIR_marcas_ejemplos_v0_lote1_mesa.json`
  (rastreado). No lo abrí: la copia lo excluye y la foto lo registra por tamaño y fecha.
- **`.pyc`:** 2.213 fuera de `.venv/` antes (243 fuera de `.venv/` y `.venv-app/`; con los `__pycache__`, 286 entradas).
- **Grep de convenciones:** `controles/grep_convenciones_S2a.txt`.

## Tramo 2 (15/10/2026): los puntos 1 a 4 del mandato

Con el «seguí» de los tramos 2 y 3 (siete agregados). En la sesión pregunté si al terminar el tramo 2 freno o sigo con el tramo
3: la autora contestó «Frenás en S2-b». Todo sobre copias hechas con el `rsync` de la cláusula más `--exclude='NO_ABRIR_*'`
(agregado 7; 0 `.env` y 0 `NO_ABRIR_` en cada una). Las cifras, con su archivo, su clave y su comando, están en
`cifras_segmentacion_oficial.md`; los JSON, en `cifras/`; los scripts, en `scripts/`. Acá va el procedimiento.

### 2.1. Paso 0 y fuentes

- Paso 0 de nuevo: el último commit es el del tramo 1 (`2fcc8fb3`), `s2/` está en git (10 archivos, sin diferencias con HEAD), los
  sha256 del código de E0 son los de `2374968a` y solo están los tres `e0/` sin rastrear. La salida, en el FRENO S2-b.
- Fuentes nuevas: `docs/enmiendas_adendas_1_y_2_laudo_B5.5_2026-10-04.md`, leída en `e82e22f` y, para la nota del 15/10/2026 sobre
  ri2_pm, en HEAD (`:147-152`); `docs/registro_decisiones_calidad_y_evaluacion_2026-10-15.md:161` (U-BLOQUE-A al grafo corregido);
  el registro del cierre de S1-quater y sus salidas; los reportes legados `reports/u_insumos_cap/` (`ded3494`) y
  `reports/u_cap3_datos/` (fuera de git), solo leídos.
- Leí los insumos con cuatro subagentes de solo lectura (control de R5; reporte legado; S1-quater y censos; marcas de 4.g), con las
  carpetas vedadas, los `NO_ABRIR_` y los `.env` excluidos y sin imprimir texto de unidades.

### 2.2. Corridas

| corrida | qué | horas | resultado |
|---|---|---|---|
| health-check de los 20 | `healthcheck_e0.py` de la raíz mínima | 16:15:33 a 16:16:52 | rc 0 |
| E0 de los 152 con el código de `92b45d6`, `e1c9456` y `9f6361e6` | `lote_e0_historicas_S2b.sh` | 16:26:06 a 16:43:35 | 152 TOs cada una, 0 con error |
| ablación de B5.8.2 | `ablacion_b582_S2.py`, 7 TOs × 4 | 16:32:36 a 16:34:10 | la base reproduce la E0 corregida en los 7 |
| tres controles de R5, caché de renglones, censo de renglones, detector 1.16, censo de sub-documentos | `lote_tramo2_S2b.sh` | 16:43:44 a 16:55:29 | rc 0 en cada paso |

El código de cada commit (sha256 de `e0_lib.py`, `correr_e0.py` y `e0_tablas.py`, de `git show`): `92b45d6` `0373a0c0…`,
`95ccf565…`, `ab300a22…`; `e1c9456` `964b417f…`, `95ccf565…`, `ab300a22…`; `9f6361e6` `9e049e58…`, `095720c2…`, `ab300a22…`. Las
corridas en secuencia: `manual` pide unos 5 GB por lectura.

### 2.3. Lo que resolví y cómo

- **Health-check** (agregado 5): ningún TO de la tanda 1 con cobertura no exacta ni ids repetidos, así que no hay freno. Las otras
  señales se registran y no excluyen (decisión de la autora, nota del 15/10/2026 al pie del mandato, `:1036-1043`, `c2b6cb60`). El
  health-check corre la escalera de `e0_lib` sin el driver de e0-r2 y da otras unidades en 15 de los 20. Las declaro, y al lado van
  dos señales medidas sobre la E0 corregida con la misma definición.
- **Punto 1:** el control de R5 sin editar deja 2.787 diferencias de ids y 424 chunks en «otra», porque su `--atribuir` no conoce S0.
  Los atribuí por historia con las E0 de `e1c9456` (el cierre, 0 en «otra») y de `9f6361e6`. Entre el cierre y la E0 corregida solo
  cambiaron C2 y S0 (`git log`). Resultado: 2.663 ids y 424 chunks de S0; 47 ids ya estaban en el cierre (10 de K, 37 de la
  partición por tabla); 0 de C2. **«Otra» en 0.**
- **Punto 2:** se reproducen las dos corridas, con las mismas cifras: con `92b45d6` las del FRENO R5 y con `e1c9456` las del
  cierre. `e1c9456` reproduce el cierre, no la corrida de R5. K-a′+K-b cambia 4 TOs. El punto (f) da 0 en los 152 (solo ric).
- **Punto 3 y 4:** las definiciones legadas se aplican sin adaptar y reproducen las cifras del reporte legado (control en 4.a).
  Las adaptaciones a e0-r2, declaradas en cada script: 3B en dos lecturas, criterios de tablas con los nombres de e0-r2, índice
  variante por ablación.
- **4.f:** el piso y su declaración, marcados como procedimiento interno. Censo de renglones con el script de S1-bis sin editar:
  corre igual.
- **Detecciones de la tanda 1** (agregado 3): censo de S0-4a y censo de renglones, con el código de la E0 corregida; ri_mmsef, 0 y 0.
- **ri_spi y ri_con** (agregado 4): por su razón vigente, con la nota ¹ en cada aparición del documento de cifras; la autora confirmó
  la regla en la misma nota.
- **Dos commits de la autora durante el tramo** (`6d9a6427` y `c2b6cb60`, 16:17): solo `docs/`; ver el FRENO S2-b.
- **rdbcra** (agregado 1): no lo investigo; queda para la tanda final del tramo 3.
- **Cobertura e ids de la tanda final** (agregado 2): van en el tramo 3, que es donde se define la tanda final (agregado 6).

### 2.4. Error propio, con su causa

Al revisar la unidad grande de ri_rml (`ri_rml::Sbloque14`), imprimí en la sesión el dict `flags` entero de ese chunk. Trae
`evidencia_tabular` y `evidencia_formula`, tres fragmentos cortos de fórmula cada uno, de una unidad que no es de diseño. La causa:
filtré por la unidad y no por los campos. Desde ahí, solo imprimo claves y cuentas. S1-quater ya está adjudicada; si esa unidad
importa para alguna lectura a ciegas posterior, lo decide la autora.

Antes de pasar los archivos al repo cacé y corregí en el scratchpad tres defectos de forma de mis scripts: un reemplazo de comas
que rompía los separadores de miles, f-strings con barras invertidas (Python 3.10) y la nota ¹ que faltaba en algunas listas.
Ninguno llegó al repo.

### 2.5. Reproducción

`lote_cifras_S2b.sh`, corrido desde una copia nueva del repo con `s2/` adentro, rehace el health-check, la ablación, los 13 JSON de
`cifras/` y `cifras_segmentacion_oficial.md` desde las salidas crudas: de 17:05:39 a 17:07:35 (la segunda vez, con la nota del mandato ya en el documento; la primera, de 17:00:40 a 17:02:35), rc 0, **los 13 JSON y el documento, iguales byte a byte** a los de `s2/` (`cmp`). Las salidas crudas (las E0 de los tres commits, los tres controles de R5 y los censos) son las de las corridas de §2.2; los controles de R5 de `92b45d6` y `e1c9456` reproducen las cifras de sus FRENOs (§3 del documento).

## Tramo 3 (15/10/2026): el re-censo de la release de E0 antes de la tanda final

Con el «seguí» del tramo 3 y sus cinco puntos. La sesión siguió en un scratchpad nuevo; las salidas crudas de los tramos 1 y 2
quedaron en el anterior, y las usé después de controlarlas (abajo). Las cifras, con su archivo, su clave y su comando, están en el
§7 de `cifras_segmentacion_oficial.md`; los JSON nuevos, en `cifras/` (`tanda_final_S2c.json`,
`resumen_healthcheck_tanda_final_S2c.json`); los scripts nuevos, en `scripts/` (`tanda_final_S2.py`, `lote_tramo3_S2c.sh`, y
`generar_cifras_S2.py` ampliado con el §7, que solo aparece si están los JSON del tramo 3).

### 3.1. Paso 0, fecha y salidas crudas

- Paso 0: los tres títulos pedidos, en orden (83, 82 y el de A2); `s2/` en git, 43 archivos, sin diferencias con HEAD. El tramo 2
  entró en `96d7d1ab`, igual a lo que entregué en el FRENO S2-b.
- Fecha: jueves 15/10/2026, 23:25, antes del domingo 18/10. No regeneré nada: controlé que las salidas sigan ahí.
  - La E0 corregida da los 768 archivos del manifiesto de S0-6b con su sha256 y 10.478 unidades (23:26:49,
    `control_e0_contra_manifiesto_S2.py`).
  - Los tres censos crudos del tramo 2 dan los sha256 de `censos_S2b.json`, `fuentes`; el de sub-documentos, con las claves
    ordenadas, da `899db5d1…`.
- Las copias (punto 1): cada una, con el `rsync` de la cláusula, y los cinco controles por nombre en 0 antes de correr nada
  (`.env`, `.env.*`, `*.env`, `NO_ABRIR_*` y enlaces simbólicos); también la raíz mínima, y al terminar, la copia, la raíz y la
  salida de la reproducción. No corrí `lote_tramo1_S2.sh` ni `lote_tramo2_S2b.sh`: sus salidas estaban y se controlaron.

### 3.2. La tanda final

La de la enmienda 8, §1, con la tanda 1 del tramo 1 y sin rdbcra, en cascada disjunta sobre los 152: tanda 0 (5), tanda 1 (20),
los de fuera del §5 sin razón vigente propia (12: los 10 no segmentables que siguen siéndolo, manual y ri2_pm), ri_ao (1, nota del
04/10/2026 al protocolo, `:432-438`), los 15 de la enmienda 8 (con ri_spi y ri_con por su razón vigente) y rdbcra (1).
**Quedan 98 TOs y 4.951 unidades: igual a la cuenta de la mesa** (nota del 15/10/2026 a la enmienda 8, `:178`). La suma cierra:
671 + 3.290 + 106 + 13 + 1.189 + 258 + 4.951 = 10.478.

### 3.3. Cobertura, ids y health-check

- Cobertura exacta e ids sin repetir en los 98, en la E0 corregida: no hay freno. Una fila por TO en el §7.
- Health-check de los 98 (23:28:28 a 23:30:13, rc 0): no reproduce `correr_e0` en 57; su propio parseo da cobertura exacta en los
  98. Las otras señales se registran y no excluyen.

### 3.4. El re-censo

- Límites de sub-documento: 33 como detección en 18 TOs, 11 de ellos en una página donde la regla A ya abre una división; 6 en
  ri_sef, que está en la lista de la regla y los aplica.
- Hallazgo 1.16: el censo de renglones, la principal, 51 en 31 TOs; el detector corregido, al lado, 134 en 60.
- No propongo una regla para el 1.16: sin leer los casos no puedo decir que una regla acotada sea de bajo riesgo (§7).
- `nmaeef::2.9` y la «Sección 1.» de ri_niif: fuera por la decisión 2 de la enmienda 8; solo se declaran.

### 3.5. Reproducción

`lote_tramo3_S2c.sh`, desde una copia nueva del repo con `s2/` adentro y controlada con los cinco patrones, de 23:32:11 a 23:35:54,
rc 0: los 15 JSON de `cifras/` y `cifras_segmentacion_oficial.md`, **16 de 16 iguales byte a byte**. Al terminar, la copia, la raíz
mínima y la salida dan 0 en los cinco controles. Sin los JSON del tramo 3, el generador ampliado da el documento de `96d7d1ab`
byte a byte.
