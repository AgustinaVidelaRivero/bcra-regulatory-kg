# U-SEG-OFICIAL, S1-quater: la adjudicación, cerrada, con la cifra, la regresión y los documentos con error (registro de la mesa, 15/10/2026)

USD 0, sin API. Hoja de ruta de la mesa, §100 (pedido de la autora recibido el 15/10/2026 a las 11:18:20). Los scripts que deciden
son los sellados en el 59 (`ea7eabdd`) y en el 63 (`be437dc4`), sin cambios. Lo que agrega la mesa en esta carpeta (el control de forma
y dos lecturas de las salidas) no cambia ninguna salida ni ninguna cifra.

## 1. La pasada 2 de la autora, sellada

| Etapa | Planilla | sha256 (el de su sello) | Sello | Fecha de modificación |
|---|---|---|---|---|
| 1 | `adjudicacion_pasada_2_etapa_1.tsv` | `0497cf6eb59440938b58bdc135d9f95ea0116e989f3c0f8e7dfd366e6b094f34` | 15/10/2026 08:37:51 | 15/10 08:35:17 |
| 2 | `adjudicacion_pasada_2_etapa_2.tsv` | `1ce5d18b77a7bd808d49f7be6c39b5a2673a8b0324e904baac5742945e9ddc1c` | 15/10/2026 11:15:36 | 15/10 11:11:22 |

- Las dos planillas son de solo lectura y dan el sha256 de su sello, en la carpeta de la autora y en la copia de la mesa. Los dos sellos,
  tal cual, están en `sellos_autora_pasada_2/`.
- **Lo que leí de `fuera_del_repo/adjudicacion_s1quater/pasada_2/`,** con la autorización de la autora del 15/10/2026: solo esas dos
  planillas y sus dos sellos. No listé ni abrí nada más de esa carpeta.
- **Las otras entradas,** cada una controlada contra su sha256 sellado:
  - la pasada 1 de las dos etapas y sus sellos (`../registro_pasada_1_y_seleccion_S1quater_mesa.md`, §1), con la autorización de la
    autora del 14/10/2026 para esos cuatro archivos;
  - las dos planillas de la lectora (`../../lectura/sello_etapa_N_S1quater.txt`);
  - el orden, las poblaciones y la regresión del sorteo (`../../sorteo/sello_*_S1quater.txt`), fuera del repo, en el paquete del sorteo;
  - la lista de límites de S1-ter (`s1ter/poblaciones_S1ter.json`, `a1313bd6…`, `s1ter/sellos_S1ter.txt:38`);
  - la lista de las fichas cuyo texto vio un modelo (`../fichas_vistas_por_el_modelo_S1quater.json`, `4eabb6bf…`, sello del 63).

## 2. La declaración de la autora sobre la pasada 2, tal cual

> Una declaración: no cumplí mi decisión sellada del 14/10 de no usar ningún modelo en la pasada 2. Usé una sesión de Claude Code solo
> para cargar en mis planillas, tal cual, lo que yo le dictaba. Las marcas y las notas son mías. Por decisión mía, no se mide qué vio
> esa sesión. La cifra de control queda como está sellada, sin las 26 fichas de la pasada 1, y se declara que no cubre lo que haya visto
> la sesión de la pasada 2. La cifra que decide sigue siendo la de las 90.

- La decisión que no se cumplió es la tercera de `../decisiones_autora_antes_de_la_pasada_2_S1quater.md` (`a2538245…`, sellada el
  14/10/2026 a las 15:12:18): «en la pasada 2 no uso ningún modelo, ni para escribir la planilla».
- Por decisión de la autora, la mesa no midió esa sesión. Que las marcas y las notas son suyas queda como su declaración.
- La cifra de control no cubre lo que haya visto esa sesión.

## 3. El control de forma y la corrida

- **El control de forma** (`control_forma/`), a las 11:26:47: 10 de 10 ok. Es el paso 9 del paso a paso de la pasada 2. Por etapa:
  - el encabezado y las columnas de cada renglón;
  - sin comillas dobles en las columnas de la autora;
  - las fichas de la selección, en su orden;
  - las columnas `lectora_…` iguales a las de la selección, renglón por renglón;
  - los valores de `marca`, `la_que_sigue` y `herencia`.
  - Su prueba, con datos sintéticos, da 10 de 10: un caso bueno y nueve en contra.
- **La corrida** (`corrida/correr_cierre_S1quater_mesa.sh`), a las 11:27:27, sobre copias, con el Python 3.10.13 del `.venv` del repo:
  `armar`, `aplicar_adjudicacion_S1quater.py`, `cifras_lectura_S1quater.py`, `acuerdo_etapa_1_S1quater.py` y
  `cifra_control_sin_vistas_S1quater.py`.
  - Antes de correrlos, la corrida controla los 19 archivos sellados de la copia de HEAD.
  - Antes de la corrida, las dos pruebas selladas, repetidas sobre la copia, dan lo mismo que sus salidas selladas: 43 de 43 y 13 de 13.
  - Dos corridas dan los mismos bytes.
- **El sello de las salidas** (`corrida/sello_cierre_adjudicacion_S1quater_mesa.txt`): las nueve salidas, a las 11:27:40, antes de leer
  las cifras.

## 4. Las cifras

Fuente: `corrida/salida/cifras/cifras_lectura_S1quater_adjudicada.json` y `corrida/salida/control/cifra_control_sin_vistas_S1quater.json`.

- **La cifra que decide** (el piso, sobre las 90, sin ponderar): 85 de 90 sin error de corte. Hay 5 errores de corte y ninguna dudosa,
  así que los dos modos de las dudosas dan lo mismo. El límite inferior de Wilson al 95 % es 0,8765 (intervalo [0,8765; 0,9760]).
  **No llega al piso de 0,90.** Con 90, el piso se cumple con hasta 3 errores de corte (`docs/mandatos/USEG_OFICIAL_segmentacion_e0r2.md:313-316`).
- **Por estrato,** como fracción: vigente 40 de 40, marcadores 10 de 10, sin_raiz 35 de 40. Los cinco errores están en sin_raiz.
- **La cifra del corpus** (la ponderada por estrato, la que cita la tesis; mandato `:319-324`): 0,9855, con tamaño efectivo 51,56 y
  Wilson [0,9057; 0,9979]. Es una aproximación: trata la muestra ponderada como una simple de ese tamaño. No decide.
- **La cifra de control** (decisión de la autora del 14/10/2026; propuesta sellada en el 63): sin las 26 fichas de la etapa 1 cuyo texto
  vio un modelo en la pasada 1 (11 de vigente, 2 de marcadores y 13 de sin_raiz). Quedan 64, con 62 sin error de corte y ninguna dudosa,
  en los dos modos. Wilson [0,8930; 0,9914]. Tampoco llega a 0,90, y no decide. No cubre lo que haya visto la sesión de la pasada 2.
- **Los errores de corte, por subclase** (con la adicional): falta_texto_propio 4, termina_fuera 1, numero_equivocado 1 y
  trae_texto_de_otro_punto 1. Son 7 subclases en 5 errores.
- **La limpieza, aparte:** 1 en la etapa 1 y 0 en la etapa 2.
- **La tanda 0:** ninguna unidad de la etapa 1 es de un TO de la tanda 0, como dispuso la adenda 1.
- **Los límites declarados:** de los 72 de la lista de S1-ter, uno cae en la muestra, `ri_icpipsp::A1C3::S2`. Tiene marca `error` de
  corte y cuenta como error (decisión del 09/10/2026).
- **Unidades en las dos etapas:** ninguna.
- **El acuerdo de la etapa 1** (`corrida/salida/acuerdo/acuerdo_etapa_1_S1quater.json`; no decide):
  - la lectora y la pasada 1 de la autora dan la misma marca en 79 de 90;
  - por par (lectora, autora): correcta y correcta, 76; error y correcta, 11; error y error, 3;
  - las 3 que las dos marcaron como error tienen la misma clase.
- **Qué cambió la pasada 2** (`lectura_de_la_mesa/cambios_pasada_2_S1quater.json`; solo cuentas):
  - **etapa 1,** 62 fichas: 11 por la condición a y 62 por la c.
    - Cambiaron 2 marcas, las dos de correcta a error.
    - Cambiaron 2 clases, 4 subclases y 1 subclase adicional.
    - La nota cambió en las 62; en 58, es lo único que cambió.
  - **etapa 2,** 60 fichas: 7 por la a, 60 por la c y 13 por la d.
    - Ninguna marca cambió.
    - Cambiaron una vez la que sigue (con su clase y su subclase) y una vez la herencia.
    - La nota cambió en las 60; en 58, es lo único que cambió.

## 5. Qué se declara: la rama del plan B

La cifra que decide no llega al piso. Por eso rige la rama 2, tal como la fijó la autora antes de su pasada 1 (nota del 13/10/2026 al
pie de `docs/mandatos/USEG_OFICIAL_segmentacion_e0r2.md`; `docs/checklist_pre_escalado.md:81`):
- la salida de S1-quater se commitea con su cifra, declarada debajo del piso;
- S2 se despacha igual;
- la condición 7 del checklist queda **declarada, no cumplida**, con la cifra;
- no hay otra vuelta a S0 antes de la tanda 1;
- la tanda 1 sale con la lista de S2, con los reemplazos.

La cifra de control tampoco llega a 0,90. Se informa como control declarado y no cambia nada de lo de arriba.

## 6. Los documentos con un error de corte confirmado

Fuentes:
- `corrida/salida/cifras/…json`, `etapa_1.errores_de_corte` y `etapa_2.regresion_sin_cifra`;
- `corrida/salida/aplicar/registro_aplicar_adjudicacion_S1quater.json`, `cierres_confirmados` y `herencias_confirmadas`.

| Dónde | Qué | Documentos (unidades) |
|---|---|---|
| muestra (etapa 1) | marca `error` de corte | ri_icpipsp (3), ri_pnp (2) |
| regresión (etapa 2) | marca `error` de corte | ri_psprca (3), ri_oc (1) |
| regresión | error de corte en la unidad que sigue: se registra y no cuenta | ri_psprca (3), ri_oc (1), gerc (1), ri_spi (1) |
| regresión | herencia con error, sin clase: se registra y no cuenta | ri_oc (4), cedin, garant, polcre, ri2_ae, seguef, snp_psp (1 cada uno) |

- **Lo que entra en la regla del punto a de la nota del piso** («un documento con un error de corte confirmado en S1-quater no entra en
  la tanda 1»):
  - por la marca de la fila: ri_icpipsp, ri_pnp, ri_psprca y ri_oc;
  - **DECISIÓN DE LA AUTORA, PENDIENTE:** si también entran los errores de corte confirmados en la unidad que sigue (suman gerc y ri_spi)
    y las herencias con error, que no tienen clase (suman cedin, garant, ri2_ae, seguef y snp_psp; polcre es de la tanda 0, que ya no
    entra en la tanda 1).
    - **PROPUESTA DE LA MESA:** sí para la unidad que sigue, porque la autora confirmó que es de corte, y «no cuenta» habla de la cifra,
      no de los documentos. Para la herencia, no, y declararla: el TSV no le da clase, y la regla habla de errores de corte.
- **Con la lista de trabajo de la tanda 1** (el ejemplo del §7 del protocolo, con ri_pgn en lugar de ri_cc; pre-registro, §1.3):
  - de los 20, sale solo ri_oc (estrato 6, escalera de E0), por la marca de la fila en la regresión. Ninguno de los otros 19 está en
    las listas de arriba, con ninguna de las dos lecturas;
  - **el reemplazo de ri_oc: PENDIENTE de S2.** Es el siguiente candidato del estrato 6 que no esté en la lista y que no tenga un error de
    corte confirmado en S1-quater. Hoy no lo puedo calcular con un comando anclado: el orden del §7 lo da un script que no está en el
    repo (`perfil_tos_particion.json`, `docs/protocolo_entre_tandas.md:386-389`; NO VERIFICADO en el §1.3 del pre-registro). Lo fija S2,
    con el comando que lo reproduce.
  - No pueden ser sucesores ri_icpipsp, ri_pnp ni ri_psprca, y, según la decisión pendiente, gerc, ri_spi y los de la herencia.
- **Un documento reemplazado** no entra en ninguna tanda siguiente hasta que su error se corrija con una regla general del grupo 2 y esa
  corrección se mida (misma nota).

## 7. La regresión

La regresión no tiene cifra (diseño de S1-quater, §6). Su lista de marcas está en `etapa_2.regresion_sin_cifra`: 60 fichas, 56
correctas y 4 con error de corte, sin dudosas ni errores de limpieza. Las leí error por error
(`lectura_de_la_mesa/regresion_por_error_S1quater_mesa.py`, con salida en `regresion_por_error_S1quater.json`):
- **Los errores de S1-ter:** 40 distintos. La lista los cuenta por origen y da 41, porque la ficha E2-033 de S1-ter está dos veces, por
  la marca y por el cierre (`../../sorteo/revision_y_decisiones_sorteo_S1quater_mesa.md`, §3). Esa ficha de más es la de
  `cryl::4.2.2`, que da correcta.
- **Por clase:** 16 de corte (12 por la marca y 4 por la unidad que sigue), 1 de limpieza y 23 de herencia.
- **Persisten 8 de los 40:**
  - de los 16 de corte, 2. En ri_psprca, la unidad vieja de la corrección tiene tres unidades nuevas, y las tres tienen error de corte. En
    ri_oc, la unidad que sigue tiene error de corte;
  - el de limpieza no persiste;
  - de los 23 de herencia persisten 6, uno en cada uno de estos documentos: cedin, garant, polcre, ri2_ae, seguef y snp_psp.
- **No persisten 31:** 13 de corte, el de limpieza y 17 de herencia.
- **Uno no se puede leer:** la corrección sacó su unidad, `snp_cheq::8.4.4::intro` (ficha E1-090 de S1-ter, de corte), y no tiene unidad
  nueva. snp_cheq está en la lista de trabajo de la tanda 1, estrato 3. Como no tiene un error de corte confirmado en S1-quater, la regla
  no la saca.
- **Errores que la regresión encontró y no son del tipo de su origen:**
  - errores de corte en la unidad que sigue, en gerc y en ri_spi;
  - en ri_psprca, tres más en la unidad que sigue;
  - en ri_oc, uno en la unidad que sigue y cuatro herencias.
- **La tanda 0:** la herencia de polcre es de un TO de la tanda 0. No es de corte; se informa aparte, como pide el mandato para la tanda 0
  (`:327-328`).

## 8. Lo que queda PENDIENTE

- De la autora: la decisión del §6 (la unidad que sigue y la herencia).
- De S2: el reemplazo de ri_oc, con el comando que lo reproduce, y la lista final de la tanda 1.
- La E0 corregida que midió S1-quater (manifiesto `80adbd58…`) se commitea con esta cifra, por la rama 2. Ese commit es del paso que la
  sube, no de este registro.

## Los archivos de esta carpeta

- `sellos_autora_pasada_2/`: los dos sellos de la autora, tal cual.
- `control_forma/`: el control de forma de la mesa, su prueba y sus dos salidas.
- `corrida/`:
  - el script de la corrida y su salida de consola;
  - las nueve salidas (`salida/`);
  - el sello de las salidas.
- `lectura_de_la_mesa/`: la regresión error por error y los cambios de la pasada 2, cada uno con su script. No cambian ninguna salida.
