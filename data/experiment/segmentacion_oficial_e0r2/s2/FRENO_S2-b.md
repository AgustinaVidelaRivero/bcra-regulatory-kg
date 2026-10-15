# U-SEG-OFICIAL — FRENO S2-b (15/10/2026)

Tramo 2 de S2: los puntos 1 a 4 del mandato, con los siete agregados del «seguí» de los tramos 2 y 3. Freno acá por respuesta de
la autora en la sesión («Frenás en S2-b»); el tramo 3 espera. USD 0, sin API. **Nada commiteado, ningún mensaje de commit
preparado; no escribí en la memoria.** Escribí solo en `s2/` y en el scratchpad. Artefacto: `cifras_segmentacion_oficial.md`;
procedimiento: `REPORTE_S2.md`, tramo 2.

## Paso 0 (con `$HOME` en lugar de la carpeta personal)

```
$ pwd
$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg
$ git log --format=%s -5
Segmentacion oficial: la primera parte de la etapa siguiente, revisada, con la E0 corregida y la composicion de la primera tanda
Evaluacion final: el reparto si cae la tanda final, decidido, y el orden del carril de la evaluacion
Evaluacion final: el numero de preguntas por potencia, el reparto si cae la tanda final y el sucesor en la tanda 1 con su tope
Segmentacion oficial: las definiciones para las cifras de la etapa siguiente, decididas, y una regla de control sellada
Calendario hacia la evaluacion final: la enmienda del protocolo firmada y las decisiones de calidad y de evaluacion
$ git status --porcelain -- data/experiment/reextraccion_v2/e0_chunking data/experiment/segmentacion_oficial_e0r2
?? data/experiment/segmentacion_oficial_e0r2/s1/e0/
?? data/experiment/segmentacion_oficial_e0r2/s1bis/e0/
?? data/experiment/segmentacion_oficial_e0r2/s1ter/e0/
$ shasum -a 256 data/experiment/reextraccion_v2/e0_chunking/e0_lib.py data/experiment/reextraccion_v2/e0_chunking/correr_e0.py data/experiment/reextraccion_v2/e0_chunking/e0_tablas.py
d89aab1a578252cd6296f03e8e8859644f008740cd493ef6d82e86c5009db298  data/experiment/reextraccion_v2/e0_chunking/e0_lib.py
78c54c4cd7dc47d592a2f9dcadc1bf97535af2d6ea0f67d67c8021010650cb5e  data/experiment/reextraccion_v2/e0_chunking/correr_e0.py
ab300a22b41f99e84ae65e8d8cd2bb5799636dffd58cfc1fda6bb3e0433bf53f  data/experiment/reextraccion_v2/e0_chunking/e0_tablas.py
$ ls data/experiment/segmentacion_oficial_e0r2
FRENO_S0-1.md
FRENO_S0-1bis.md
FRENO_S0-2.md
FRENO_S0-3.md
FRENO_S1.md
s0_1
s0_1bis
s0_2
s0_3
s0_4
s0_5
s0_6
s1
s1bis
s1quater
s1ter
s2
```

El último commit es el del tramo 1 (`2fcc8fb3`); `s2/` está en git (10 archivos, sin diferencias con HEAD).

## Lo del tramo (`cifras_segmentacion_oficial.md`, por sección)

**§1. Health-check de los 20 de la tanda 1 (agregado 5).**
- Ningún TO con cobertura no exacta ni ids repetidos: **no hay freno**.
- El health-check no reproduce `correr_e0` en 15 de los 20: da otras unidades que `unidades_por_to`, porque corre la escalera de
  `e0_lib` sin el driver de e0-r2. Lo declaro, y al lado van dos señales medidas sobre la E0 corregida.
- Señales del health-check: `cid` en snp_cheq, ceninf, lingeef, manori y efemin; páginas sin sección en ri_rml y cirmo3; unidades
  grandes en ri_ccna, ri_rml y manori. En la E0 corregida, de las dos que mido: páginas sin sección solo en ri_rml (las mismas 3), y
  una unidad grande, `ri_rml::Sbloque14`, que la partición por tamaño deja sin partir porque lleva una tabla serializada.
- Esas señales se registran y se declaran por TO y no excluyen: lo decidió la autora antes de ver este FRENO (nota del 15/10/2026 al
  pie del mandato, `:1036-1043`, en `c2b6cb60`, commit posterior al paso 0 de este tramo).

**§2. Punto 1, diferencias contra `b584_particion/`.** El control de R5, sin editar, deja 2.787 ids y 424 chunks en «otra»: su
`--atribuir` no conoce S0. Atribuidos por historia, con las E0 de `e1c9456` (el cierre, sin «otra») y de `9f6361e6` (C2), son
2.663 ids y 424 chunks de S0, y 47 ids ya presentes en el cierre (10 por K y 37 por la partición por tabla); C2 no aporta ninguno.
**«Otra» en 0.** C2 cambia solo la herencia de 93 unidades en 9 TOs (punto (h)); S0 cambia 112 TOs.

**§3. Punto 2, la escalera de R5.** Se reproducen las dos corridas con todas sus cifras. Con `92b45d6` salen las del FRENO R5: 205
ids de K en 19 TOs. Con `e1c9456` salen las del cierre: 93 en 16. **Con `e1c9456` se reproduce el cierre, no la corrida de R5**
(lo declaro). K-a′+K-b cambia nmaeef, ri_rml, snp_cheq y snp_dd. De los 43 textos que cambió, S0 movió después los ids de 32.
El punto (f) da 0 en los 152 (solo ric).

**§4. Punto 3.**
- Unidades: 10.478, con 9.095 terminales y 1.383 mini-chunks.
- Vía por modo: el modo legado de los 152 se conserva salvo ri_spi¹ (`sin_raiz_letra`).
- Partición por tamaño: 6 unidades partidas en 27 partes; 3 quedan sin partir, las 3 por tabla serializada.
- Tablas: la lectura corre en 152 TOs y encuentra tablas en 124. Son 916 tablas, de las que 467 se serializan; 324 unidades llevan
  una tabla serializada, en 55 TOs.
- Ids: 9 desambiguados en 4 TOs, ninguno en una página de índice.
- K conserva 334 renglones en 58 TOs.
- No segmentables: quedan 10, con 134 páginas y 17 unidades. ri_spi¹ y ri_con¹ van aparte.

**§5. Punto 4.**
- **4.a:** desarrollo 1.768 unidades (legado 1.763), validación 770 (762), universo 10.478 (9.324).
- **4.b:** sobre los 157, normativa general 10.571 puntos con 80,8 % de terminales (legado 10.157 y 80,9 %); régimen informativo
  1.064 con 87,7 % (legado 758 y 88,4 %). La legada reproduce las cifras que hoy cita la tesis, que no tenían artefacto en el repo.
- **4.c:** 3A da 44 + 2 en parte (legado 42 + 2), con ri_spi¹ y ri_con¹ adentro. 3B literal («sin unidades `S<n>`») da 41 y no mide
  lo mismo que 3A. **Lo declaro:** agrego una segunda lectura de 3B, «sin secciones no sintéticas», que da 52; difiere de 3A solo en
  4 TOs, más los no segmentables y los parciales. Es una interpretación mía.
- **4.d:** las 21 reglas del D3 legado, con el mismo criterio, sobre los 152; las de tablas actúan ahora en hasta 124 TOs. Van
  además 67 reglas de e0-r2 con rastro en la salida, cada una con su línea de código. Las reglas de S0 sin rastro van declaradas:
  medir su uso pide una ablación por regla, que S2 no corre.
- **4.e:** escritos en puntos, 138 documentos (10.242 unidades); fichas y listados, 2 (89); no segmentables, 10 (17); ri_spi¹ y
  ri_con¹, aparte (130). Van la fila de `e82e22f` y, aparte, la enmienda 8 (15 TOs, 1.189 unidades), ri2_pm (37) y U-BLOQUE-A (77).
- **4.f:**
  - S1-quater: 85 de 90 sin error de corte; la ponderada da 0,9855 [0,9057; 0,9979]. El piso, su declaración y la cifra de
    control van en un bloque marcado «Procedimiento interno, no para la tesis». Poner ahí la de control es una lectura mía.
  - Censo de renglones: corre igual con el script de S1-bis. Da 326 renglones en 191 páginas de 86 TOs (S1-bis daba 327).
- **4.g:** las 8 filas mínimas y las 3 marcas, con su texto:
  - M3 se resuelve con 4.d.
  - **M1 se resuelve en parte:** el texto del párrafo está en Overleaf y no identifico de qué documento habla. Va el dato de los 12;
    solo ri_spi¹ queda leído por puntos.
  - **M2 no se resuelve con S2:** los roles cambiaron en 12 páginas de 9 TOs, y el script de VERIF-FORMAS-SEG reconstruye los roles
    con el `e0_lib` legado. Recontar pide adaptarlo, y eso es otra unidad.

**§6. Detecciones de la release de E0 en la tanda 1 (agregado 3).**
- Límites de sub-documento: 14 que quedan como detección, en 5 TOs (manori 8, ri_rml 3, ri_gerc 1, ri_pgn 1, snp_tr 1). Antes eran
  17 en 6, con ri_oc. ri_ccna (16) y nmcief (10) están en la lista de la regla, que los aplica.
- Candidatos del 1.16, con el criterio del censo: 27 en 8 TOs (antes, 33 en 10). Con el detector corregido de S0-5a: 92 en 16.
- **ri_mmsef: 0 límites y 0 candidatos.**
- **Para la autora:** qué criterio del 1.16 declara el pre-registro v8, el del censo (el de las cifras de antes) o el del detector.

¹ ri_spi y ri_con, por su razón vigente (enmienda 8, decisiones 1 y 2); en la partición legada eran no segmentables (agregado 4; la
regla la confirmó la autora en la misma nota del mandato).

**Reproducción.** `lote_cifras_S2b.sh`, desde una copia nueva del repo con `s2/` adentro, rehace el health-check, la ablación, los 13 JSON de `cifras/` y el documento desde las salidas crudas: 17:05:39 a 17:07:35 (la segunda vez, después de agregar la nota del mandato al documento; la primera, 17:00:40 a 17:02:35), rc 0, **los 14 archivos iguales byte a byte**.

## Lo que no hice en este tramo, y por qué

- **La cobertura y los ids de cada TO de la tanda final (agregado 2):** van con el tramo 3, donde la tanda final se define
  (agregado 6). rdbcra (agregado 1) queda fuera de esa tanda final, sin investigarlo de nuevo.
- **Las 57 líneas `sin_unidad_ni_rol` del censo de renglones:** no las leo. El despacho pide la cifra.

## Error propio, con su causa (REPORTE, §2.4)

Al revisar la unidad grande de ri_rml imprimí en la sesión el dict `flags` de `ri_rml::Sbloque14`. Trae seis fragmentos cortos de
fórmula: `evidencia_tabular` y `evidencia_formula`. La causa: filtré por la unidad y no por los campos. Desde ahí imprimo solo
claves y cuentas.

## Repo, `.pyc` y convenciones

- Foto sha256 del repo sin `.git` antes del tramo: 16:16:52 a 16:17:05, 50.540 entradas. La de después, en el mensaje del FRENO
  (este archivo entra en ella).
- **Dos commits de la autora cayeron durante el tramo** (`6d9a6427`, 16:17:03, y `c2b6cb60`, 16:17:16, el primero durante la foto
  de antes): cambian 6 documentos de `docs/` y agregan `docs/mandatos/A2_1_sistema_por_fragmentos_preregistro_A2_2.md`. No son
  escrituras mías: los 7 están en el `--stat` de esos dos commits y son iguales a HEAD. Para S2 cambia la nota del mandato de arriba
  (health-check y regla de ri_spi y ri_con), que incorporé. Los datos que leen mis scripts no cambiaron: la reproducción corre desde
  una copia posterior a los dos commits y da los mismos archivos.
- `.pyc` fuera de `.venv/`, antes: 2.213 (286 entradas fuera de `.venv/` y `.venv-app/`).
- Grep de convenciones: `controles/grep_convenciones_S2b.txt`.

## Cierre

El paquete `revision_USEG_OFICIAL_FRENO_S2/`, actualizado con el tramo 2, con su `manifest.txt`. Su copia con `ditto` va a
`~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/6b38566a-94be-4076-8999-67efd2c6dfd3/scratchpad/revision_USEG_OFICIAL_FRENO_S2/`,
verificada contra el manifiesto, en el mensaje del FRENO. Nada commiteado, ningún mensaje de commit preparado (el commit lo arma la
mesa), nada escrito en la memoria.

FRENO.
