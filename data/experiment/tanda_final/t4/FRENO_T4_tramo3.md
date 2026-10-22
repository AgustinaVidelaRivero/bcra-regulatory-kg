# FRENO T4 — tanda final de B6.1, tercer tramo: las aceptadas no ítems sobre las 60 y el freno por la atención sobre las 60 (USD 0, sin API, sin commit)

Rigen el pre-registro firmado de la tanda final (`docs/preregistro_tanda_final.md`, firma en `4de7f2a7`), §6, con su versión derivada
para la lectura de T4 (sha256 `26c29d9424ffaf634a02735a972ad29e7df8b06463b8ad430654d50d4d442fc2`), la regla del freno del script de la mesa y del pre-registro de la tanda 1 (§5.4, `95b18217:592-593`), el umbral de `t3/muestras/umbrales_t4_tf.json`, la regla de las dudosas (registro de decisiones, §35), lo que decidió la autora sobre el FRENO del segundo tramo (registro, §85) y el «seguí» del tercer tramo.
Las lecturas son las de la autora: las 30 del primer tramo, selladas el 2026-10-21 a las 08:37:10, y las 30 de la ampliación, selladas el 2026-10-21 a las 23:38:02 y controladas por la mesa (11 de 11). HEAD `a4911b53`.

**Resultado:**
- **Las aceptadas no ítems sobre las 60** (sección 4): 16 de 60 con error, contando las dudosas; tasa ponderada 0,3733, Wilson [0,2160; 0,5630] (n efectivo 26,266). Sobre las 30 del primer tramo era 0,3674.
- **El freno por la atención sobre las 60: sí.** La tasa (0,3733) pasa el umbral (0,2437); el p-valor sobre las 60 es 0,0009. La ampliación dejó cada celda con el doble de unidades, así que la regla se aplica tal cual.
- **El freno por intervalos: no.** El límite inferior del Wilson (0,2160) no pasa el superior del Wilson de la tanda 0 (0,2968).
- **Hay freno de T4 por las aceptadas no ítems** (sección 5): la regla da freno si se cumple cualquiera de los dos, y se cumple el de la atención sobre las 60. Qué sigue no es de esta unidad.
- **Las dudosas:** 0, así que la sensibilidad da la misma decisión.
- **La ponderada total y la atención de RI con las 60** (sección 6, información): 0,3502 y 0,1843 (p 0,2339); en el segundo tramo, 0,3458 y 0,1843.
- **Lo del segundo tramo** (sección 7), rehecho: 9 de 9 bloques iguales. En las líneas de base cambian solo los dos textos con el nombre del archivo, ya sin la coma.
- **La verificación independiente:** 62 de 62 cifras iguales.
- Toda cifra sale por script de sus archivos. Las tablas que copio de una salida van tal cual; mis aclaraciones van fuera de las tablas.
- Nada commiteado y ningún mensaje de commit preparado: los commits son de la autora y quedan PENDIENTES.

## 1. Paso 0

La salida, con la carpeta personal reemplazada por `$HOME` y la carpeta de trabajo por `<DIR DE TRABAJO>` (`paso0_T4_tramo3_salida.txt`, de `paso0_t4_tramo3.sh`, con la comparación de `paso0_foto_contra_commits_t4_tramo3.py`, en el paquete):

```
== pwd
$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg
== git log -3 --format='%h %s'
a4911b53 Tanda final: la cuarta etapa, la lectura de la autora de la ampliacion de las aceptadas no items, sellada y controlada
5b1d9082 Registro de decisiones: la tercera etapa del entorno de los agentes revisada, los selftests del banco antes de su commit, el gold del juez de precision que no pasa y el juez v2 como estudio aparte
46070985 Registro de decisiones: el cwd compartido tambien en paralelo, tres revisiones de la mesa, la ampliacion de la cuarta etapa de la tanda final con su convertidor y el calendario rehecho
== el título del TF4c en la historia
1
== git diff --name-only 4cc8f857 HEAD
data/experiment/tanda_final/t4/ampliacion/control_lectura_mesa/consola_control_lectura_T4_ampliacion.txt
data/experiment/tanda_final/t4/ampliacion/control_lectura_mesa/control_lectura_T4_ampliacion_mesa.py
data/experiment/tanda_final/t4/ampliacion/control_lectura_mesa/salida_control_lectura_T4_ampliacion.json
data/experiment/tanda_final/t4/ampliacion/lectura_autora/aceptadas_no_items_ampliacion_exportada.csv
data/experiment/tanda_final/t4/ampliacion/lectura_autora/aceptadas_no_items_ampliacion_marcada.csv
data/experiment/tanda_final/t4/ampliacion/lectura_autora/sello_lectura_T4_ampliacion.txt
docs/registro_decisiones_calidad_y_evaluacion_2026-10-15.md
== git status --porcelain --untracked-files=no (entre las dos rayas)
--
--
== las dos marcadas contra sus sellos
igual aceptadas_no_items_marcada.csv (2026-10-21 08:37:10)
igual ampliacion/aceptadas_no_items_ampliacion_marcada.csv (2026-10-21 23:38:02)
== tres sha256
d7f7860fbf09f92443992aeb9915e22191582cfe2edaf5fd0a089baadd3ac555  data/experiment/tanda_final/t3/muestras/umbrales_t4_tf.json
26c29d9424ffaf634a02735a972ad29e7df8b06463b8ad430654d50d4d442fc2  data/experiment/tanda_final/preregistro/preregistro_tanda_final_derivada_T4.md
4b9605f2d76cee42b13597e35b0eb7652e9e2723b952d91e0e09da1f63745633  data/experiment/tanda_final/t3/muestras/unidades_a_la_vista_T4.json
== la foto final del segundo tramo (t4t2_fotos/foto_repo_final_T4t2.json)
219efc15aa28c527f7edf73746b017d6150433fe3ab4d94a8ab13371510a3be2
== la foto nueva (t4t2_fotos/foto_repo_antes_T4t3.json) y su comparación con los commits abdc0998..HEAD
2026-10-22 10:44:11 2026-10-22 10:44:25 58130 entradas
{
 "foto_anterior": {
  "sha256": "219efc15aa28c527f7edf73746b017d6150433fe3ab4d94a8ab13371510a3be2"
 },
 "foto_nueva": {
  "sha256": "5d38f6f8c3c5f208df637011e5590d2f5fa7d9fb609a6aa307a4d6da158e8106",
  "n": 58130
 },
 "commits": "abdc0998..HEAD",
 "rutas_en_los_commits": 55,
 "por_estado_en_los_commits": {
  "A": 53,
  "M": 2
 },
 "rutas_de_los_commits_ya_iguales_en_disco": 42,
 "nuevos": 12,
 "borrados": 0,
 "cambiados": 7,
 "DS_Store": [
  ".DS_Store",
  "data/.DS_Store",
  "data/experiment/.DS_Store",
  "data/experiment/tanda_final/.DS_Store",
  "data/experiment/tanda_final/t4/.DS_Store",
  "data/experiment/tanda_final/t4/lectura_autora/.DS_Store"
 ],
 "nuevos_borrados_o_cambiados_fuera_de_los_commits": [],
 "rutas_de_los_commits_distintas_de_HEAD": [],
 "ok": true
}
rc=0
== .pyc: líneas y diff contra los del final del segundo tramo
   11236
iguales
== pgrep -fl "runner_corpus.py|lanzar_t|correr_tanda"
rc=1
== pgrep -fl ensamblar_tanda0.py
rc=1
== hora
2026-10-22 10:44:27
```

- **La foto nueva** (`t4t2_fotos/foto_repo_antes_T4t3.json`, sha256 `5d38f6f8c3c5f208df637011e5590d2f5fa7d9fb609a6aa307a4d6da158e8106`) contra la final del segundo tramo (`foto_repo_final_T4t2.json`): 12 nuevos, 7 cambiados y 0 borrados. 6 son `.DS_Store`, ruido de Finder que queda fuera de lo que cuenta (decisión de la autora sobre el FRENO del paso 0 del segundo tramo); los otros 13 son rutas de los commits `abdc0998..HEAD`. De las 55 rutas de esos commits, 42 ya estaban iguales en disco: son las del segundo tramo, que el TF4b commiteó sin cambios. Todas dan el sha256 de su blob en HEAD.
- **Los `.DS_Store`** (sin abrirlos): `.DS_Store`, `data/.DS_Store`, `data/experiment/.DS_Store`, `data/experiment/tanda_final/.DS_Store`, `data/experiment/tanda_final/t4/.DS_Store`, `data/experiment/tanda_final/t4/lectura_autora/.DS_Store`.
- **Las horas de la autora, de los sellos:** las 30 del primer tramo, 2026-10-21 08:37:10 (`t4/lectura_autora/sello_lectura_T4.txt`); las 30 de la ampliación, 2026-10-21 23:38:02 (`t4/ampliacion/lectura_autora/sello_lectura_T4_ampliacion.txt`).

## 2. Lo que decidió la autora sobre el FRENO del segundo tramo (registro de decisiones, §85)

1. La exclusión de `data/experiment/neo4j/volumen` en la copia del repo: aceptada y declarada.
2. El texto «umbrales_t4_tf,json» de `tasas_t4_tramo2.json` se corrige cuando se rehacen las tasas: lo corrige este tramo (sección 7).
3. Que la unidad haya abierto `tanda1/t3/scripts/celdas_t4_t3f.py` y calculado el sha256 de dos `kg.json` de `tanda1/t3/acumulado/` contra su sello: aceptado y declarado.
4. Para sellar la lectura de la ampliación, la mesa armó `t4/ampliacion/lectura_autora/convertir_lectura_T4_ampliacion.py` y `LEEME_lectura_T4_ampliacion.md`, que entraron con el commit del segundo tramo. No los toqué.

## 3. La regla

- **El freno** (script de la mesa, `data/experiment/controles_tanda1/umbrales_t4_por_celdas_mesa.py`, docstring, «Freno»; pre-registro de la tanda 1, `95b18217:592-593`): hay freno si el intervalo de la tasa no se solapa con el Wilson de la tanda 0, «o si la atención se confirma sobre las 60 (cada celda con el doble de unidades)».
- **El umbral:** `freno_por_atencion_sobre_60` de `aceptadas.no_items` en `t3/muestras/umbrales_t4_tf.json` (sha256 `d7f7860fbf09f92443992aeb9915e22191582cfe2edaf5fd0a089baadd3ac555`), con los pesos reales: 0,2437, p 0,0497.
- **Las dudosas** (pre-registro, §6; registro, §35): cuentan como error para la tasa, la atención y el freno; la cuenta sin ellas va al lado como sensibilidad y no decide nada.

## 4. Las aceptadas no ítems sobre las 60

#### Tabla 10. Las aceptadas no ítems sobre las 60, por celda (`aceptadas_no_items_sobre_60`; pesos de `t3/muestras/umbrales_t4_tf.json`)

Cada celda: primer tramo + ampliación = las 60.

| celda | N | peso | leídas | con error | sin error | dudosa | el doble |
|---|---:|---:|---|---|---|---|---|
| RI:sin_raiz | 322 | 0,0900 | 10 + 10 = 20 | 2 + 2 = 4 | 8 + 8 = 16 | 0 + 0 = 0 | sí |
| RI:resto | 48 | 0,0134 | 5 + 5 = 10 | 1 + 1 = 2 | 4 + 4 = 8 | 0 + 0 = 0 | sí |
| NG:sin_raiz | 107 | 0,0299 | 5 + 5 = 10 | 0 + 2 = 2 | 5 + 3 = 8 | 0 + 0 = 0 | sí |
| NG:resto | 3.102 | 0,8667 | 10 + 10 = 20 | 4 + 4 = 8 | 6 + 6 = 12 | 0 + 0 = 0 | sí |
| total | 3.579 | 1,0000 | 30 + 30 = 60 | 7 + 9 = 16 | 23 + 21 = 44 | 0 + 0 = 0 | sí |

#### Tabla 11. La tasa sobre las 60 y los dos frenos (`aceptadas_no_items_sobre_60.regla` y `.sensibilidad_sin_dudosas`)

El umbral de `t3/muestras/umbrales_t4_tf.json` (`aceptadas.no_items.umbrales.freno_por_atencion_sobre_60`): 0,2437, p 0,0497. El superior del Wilson de la tanda 0: 0,2968.

| cuenta | errores | leídas | tasa ponderada | n ef. | Wilson | umbral recalculado (igual al del JSON) | p sobre las 60 | freno por la atención sobre las 60 | freno por intervalos | freno |
|---|---:|---:|---:|---:|---|---|---:|---|---|---|
| regla (dudosa = error) | 16 | 60 | 0,3733 | 26,266 | [0,2160; 0,5630] | 0,2437 (sí) | 0,0009 | sí | no | sí |
| sensibilidad (dudosas fuera) | 16 | 60 | 0,3733 | 26,266 | [0,2160; 0,5630] | 0,2437 (sí) | 0,0009 | sí | no | sí |

El umbral y el p-valor dicen lo mismo: sí. La sensibilidad da otra decisión: no. La distribución bajo H0, con las n de la regla: 27.815 valores, suma 1,000000 (`tasas/distribuciones_bajo_H0_t4_tramo3.json`, `aceptadas:no_items:sobre_60:regla`).

Mis aclaraciones:
- **Los pesos** son los del segundo tramo (`umbrales_t4_tf.json`). Las 60 son las 30 de `t4/lectura_autora/aceptadas_no_items_marcada.csv` y las 30 de `t4/ampliacion/lectura_autora/aceptadas_no_items_ampliacion_marcada.csv`, cada una contra su sello; `tasas_t4t3_tf.py` controla además que las de la ampliación sean las de su muestra y que ninguna esté entre las 30 del primer tramo.
- **El doble por celda:** la ampliación salió con las mismas cuotas por celda que la primera muestra, así que cada celda tiene el doble (tabla 10). No hizo falta aplicar la regla con otras n.
- **El umbral:** con el doble, la distribución bajo H0 de la tasa sobre las 60 es la misma con la que la mesa calculó el umbral (los mismos pesos, las mismas n y la tasa de la tanda 0). `tasas_t4t3_tf.py` la enumera entera con `distribucion` de la mesa, recalcula el umbral (la menor tasa con P(T' ≥ t) ≤ 0,05) y controla que, redondeado, sea el del JSON. Decide con el umbral exacto, y el p-valor va al lado: los dos dicen lo mismo.
- **El freno por intervalos** usa el Wilson con el n efectivo de Kish de las 60 y el superior del Wilson de la tanda 0 de no ítems, como en el segundo tramo.

## 5. Los dos frenos y la decisión

- **Freno por la atención sobre las 60:** sí (tasa 0,3733, umbral 0,2437, p 0,0009).
- **Freno por intervalos:** no (inferior 0,2160, superior de la tanda 0 0,2968).
- **Freno de T4 por las aceptadas no ítems:** sí. Con las dudosas fuera, lo mismo.
- **Lo que no decido:** qué sigue después del freno. Las líneas de la regla (`95b18217:592-593`) fijan cuándo hay freno; lo que sigue es de la mesa y la autora (sección 10).

## 6. La ponderada total y la atención de RI con las 60 (información)

#### Tabla 12. La ponderada total y la atención de RI: el segundo tramo y con las 60 de no ítems (`aceptadas.total`, `atencion_RI` e `informacion_con_las_60`)

| cifra | no ítems con | cuenta | errores de leídas | tasa | n ef. | Wilson | p de la atención | decide |
|---|---|---|---|---:|---:|---|---:|---|
| ponderada total | 30 | regla | — | 0,3458 | 21,260 | [0,1819; 0,5570] | — | sin umbral |
| ponderada total | 60 | regla | — | 0,3502 | 37,773 | [0,2185; 0,5097] | — | información |
| ponderada total | 30 | sensibilidad | — | 0,3458 | 21,260 | [0,1819; 0,5570] | — | sin umbral |
| ponderada total | 60 | sensibilidad | — | 0,3502 | 37,773 | [0,2185; 0,5097] | — | información |
| atención de RI | 30 | regla | 5 de 30 | 0,1843 | 16,967 | [0,0661; 0,4191] | 0,2945 | atención: no |
| atención de RI | 60 | regla | 8 de 45 | 0,1843 | 32,978 | [0,0877; 0,3467] | 0,2339 | información |
| atención de RI | 30 | sensibilidad | 5 de 30 | 0,1843 | 16,967 | [0,0661; 0,4191] | 0,2945 | atención: no |
| atención de RI | 60 | sensibilidad | 8 de 45 | 0,1843 | 32,978 | [0,0877; 0,3467] | 0,2339 | información |

Mis aclaraciones:
- **No deciden nada:** la atención de RI se decidió en el segundo tramo, con su umbral de T3 para las n de entonces. Con las 60 van como información, con el mismo método.
- **La tasa de RI no cambia** con las 60 porque, en las dos celdas RI de no ítems, la proporción de errores de las 60 es la de las 30. Cambian el n efectivo, el Wilson y el p-valor.

## 7. Lo del segundo tramo, rehecho, y las líneas de base

- **`tasas_t4t3_tf.py` rehace todo lo del segundo tramo** y controla, al final, que cada bloque dé lo mismo que `tasas/tasas_t4_tramo2.json`: 9 de 9 (`regla_de_las_dudosas`, `z`, `aceptadas`, `atencion_RI`, `NG_sin_raiz`, `cola`, `vigilancias`, `observacion:12`, `ampliacion`). Los controles de entrada del segundo tramo, iguales: sí; los del tercero, 48 de 48.
- **Las líneas de base:** la coma decimal va ahora solo en los números. Cambian estos dos textos, y nada más:
  - `aceptadas:total.tanda0`: antes «0,1616, Wilson [0,0888; 0,2760], mismo método (umbrales_t4_tf,json)»; ahora «0,1616, Wilson [0,0888; 0,2760], mismo método (umbrales_t4_tf.json)».
  - `atencion_RI.tanda0`: antes «la tasa de RI bajo H0, con las tasas de la tanda 0: 0,1433 (umbrales_t4_tf,json)»; ahora «la tasa de RI bajo H0, con las tasas de la tanda 0: 0,1433 (umbrales_t4_tf.json)».

## 8. Las cifras para la hoja de la revisión entre tandas

Van en `t4/tablas_t4_tramo3.md` (tabla 1), que genera `scripts/tablas_t4t3_tf.py` desde la salida de las tasas, con la fila de no ítems sobre las 60. La copio tal cual:

#### Tabla 1. Las cifras para la hoja de la revisión entre tandas (filas que esperan a T4)

| fila | tanda final | línea de base: tanda 1 (versión derivada) | tanda 0 | decisión | script y clave de la salida |
|---|---|---|---|---|---|
| aceptadas, ítems | 6 de 30 (6 con error y 0 dudosas); ponderada 0,2862, Wilson [0,1090; 0,5678] (n ef. 11,888); sin las dudosas, 6 de 30, 0,2862 [0,1090; 0,5678] | 9 de 30 con las dudosas como error; ponderada 0,2196, Wilson de Kish [0,0784; 0,4822]; atención: no; freno: no | 6 de 30, Wilson [0,0951; 0,3731] | atención: no (p 0,2710); freno: no | `scripts/tasas_t4t3_tf.py`, `tasas/tasas_t4_tramo3.json`, `aceptadas.items` |
| aceptadas, no ítems, sobre las 60 | 16 de 60 (16 con error y 0 dudosas); ponderada 0,3733, Wilson [0,2160; 0,5630] (n ef. 26,266); sin las dudosas, 16 de 60, 0,3733 [0,2160; 0,5630]; sobre las 30 del primer tramo, 7 de 30, 0,3674 | 3 de 30 con las dudosas como error; ponderada 0,0968, Wilson de Kish [0,0214; 0,3446]; atención: no; freno: no | 4 de 30, Wilson [0,0531; 0,2968] | atención sobre las 30: sí (p 0,0168); freno por la atención sobre las 60: sí (umbral 0,2437, p 0,0009); freno por intervalos: no | `scripts/tasas_t4t3_tf.py`, `tasas/tasas_t4_tramo3.json`, `aceptadas_no_items_sobre_60` y `aceptadas.no_items` |
| aceptadas, ponderada total | con las 30 de no ítems, 0,3458, Wilson [0,1819; 0,5570] (n ef. 21,260); sin las dudosas, 0,3458 [0,1819; 0,5570]; con las 60 de no ítems (información), 0,3502, Wilson [0,2185; 0,5097] (n ef. 37,773) | 0,1397, Wilson de Kish [0,0532; 0,3196] | 0,1616, Wilson [0,0888; 0,2760] (mismo método) | sin umbral | `scripts/tasas_t4t3_tf.py`, `tasas/tasas_t4_tramo3.json`, `aceptadas.total` |
| atención de RI | con las 30 de no ítems, 5 de 30; ponderada de RI 0,1843, Wilson [0,0661; 0,4191] (n ef. 16,967); sin las dudosas, 5 de 30, 0,1843; con las 60 de no ítems (información), 8 de 45, 0,1843, p 0,2339 | 7 de 30; ponderada de RI 0,1747; la atención no salta | bajo H0, 0,1433 (umbral de T3: 0,2918) | atención: no (p 0,2945) | `scripts/tasas_t4t3_tf.py`, `tasas/tasas_t4_tramo3.json`, `atencion_RI` |
| tasa de error de la cola | 12 de 30 (12 con error y 0 dudosas); ponderada 0,3706, Wilson [0,2057; 0,5723] (n ef. 23,100); sin las dudosas, 12 de 30, 0,3706 [0,2057; 0,5723] | 14 de 30 con las dudosas como error; ponderada 0,4386, Wilson de Kish [0,2751; 0,6166]; la regla del 25 % se dispara | 12 de 30, Wilson [0,246; 0,577] (reext_t0/t4/salida/tasas_t4.json) | regla del 25 %: se dispara (cifra y vigilancia, no freno) | `scripts/tasas_t4t3_tf.py`, `tasas/tasas_t4_tramo3.json`, `cola` |
| observación (12) | 29 correctas de 30 (0 no decidibles, en el denominador; 1 incorrecta: catálogo 1); Wilson [0,8333; 0,9941]; ponderada por celda 0,9934 [0,7576; 0,9999] | 27 correctas de 30, Wilson [0,7438; 0,9654] | 25 de 30, Wilson [0,664; 0,927], con el perfil anterior (pre-registro de la tanda 1, §5.2, como lo da tanda1/t4/scripts/tasas_t4t2.py) | sin umbral | `scripts/tasas_t4t3_tf.py`, `tasas/tasas_t4_tramo3.json`, `observacion:12` |
| vigilancia (1) | 7 sí de 30 (0 no decidibles, fuera de la tasa); cruda 0,2333, Wilson [0,1179; 0,4093]; ponderada por celda 0,2010 [0,0627; 0,4858] | 3 sí de 30 | no se midió en la tanda 0 | sin umbral | `scripts/tasas_t4t3_tf.py`, `tasas/tasas_t4_tramo3.json`, `vigilancias.vigilancia:1` |
| vigilancia (2) | 6 vaciamientos de 30; cruda 0,2000, Wilson [0,0951; 0,3731]; ponderada por celda 0,1483 [0,0516; 0,3579] | 15 vaciamientos de 30 | en la tanda 0 se midió la población, sin leer la muestra | sin umbral | `scripts/tasas_t4t3_tf.py`, `tasas/tasas_t4_tramo3.json`, `vigilancias.vigilancia:2` |
| vigilancia (3) | 5 duplicaciones de 30; cruda 0,1667, Wilson [0,0734; 0,3356]; ponderada por celda 0,1670 [0,0522; 0,4218] | 9 duplicaciones de 30 | no se midió en la tanda 0 | sin umbral | `scripts/tasas_t4t3_tf.py`, `tasas/tasas_t4_tramo3.json`, `vigilancias.vigilancia:3` |
| vigilancia (7) | 2 sin apoyo de 6; cruda 0,3333, Wilson [0,0968; 0,7000]; leída entera, sin celdas | 2 sin apoyo de 4 | en la tanda 0 se midió la población, sin leer la muestra | sin umbral | `scripts/tasas_t4t3_tf.py`, `tasas/tasas_t4_tramo3.json`, `vigilancias.vigilancia:7` |

- **La ampliación:** salta la atención de ítems, no; la de no ítems, sí; la de RI, no. Hay ampliación: sí. Con las dudosas fuera: aceptadas:items no, aceptadas:no_items sí, RI no.
- **Las aceptadas no ítems sobre las 60** (las 30 del primer tramo y las 30 de la ampliación; cada celda con el doble: sí): freno por la atención sobre las 60, sí; freno por intervalos, no. Con las dudosas fuera, la sensibilidad da otra decisión: no. Su fila de la hoja es la de las 60 (tablas 10 y 11).
- **La ponderada total y la atención de RI con las 60** van como información, sin decisión, al lado de las del segundo tramo (tabla 12).
- **Las líneas de base:** la tanda 1, los valores T4.* de tanda_final/preregistro/preregistro_tanda_final_derivada_T4.huecos.json (versión derivada para la lectura); la tanda 0, al lado, la de cada fila de `lineas_de_base`.
- **Los controles de la entrada** (`scripts/tasas_t4t3_tf.py`): 48 de 48 pasan.
- **Lo del segundo tramo da lo mismo** (`lo_del_segundo_tramo`): 9 de 9 bloques iguales a `tasas/tasas_t4_tramo2.json`; en las líneas de base cambian solo `aceptadas:total.tanda0` y `atencion_RI.tanda0`.

## 9. El cegamiento

- **Ninguna cifra usa el estado de E3, `n_reintentos`, `reintentos_e3.jsonl`, `copias_nota_e3.jsonl`, las `marcas_e3` ni el gasto de los reintentos.** `tasas_t4t3_tf.py` lee las marcadas y sus sellos, las muestras, las poblaciones, los umbrales, la versión derivada, el script de la mesa y la salida del segundo tramo.
- **De la tanda 1** no abrí nada: ni muestras, ni material, ni planillas, ni cifras, ni scripts. El script de la mesa (`controles_tanda1/umbrales_t4_por_celdas_mesa.py`) lo importo sin cambiarlo, como en el segundo tramo, y leí su docstring, que es la regla del punto 2.
- No abrí ningún `.env` ni ningún `NO_ABRIR_` (la foto da 0 en `t4/`), ni entré en las carpetas vedadas.

## 10. Para la autora y la mesa

1. **El freno salta** por la atención sobre las 60 de las aceptadas no ítems. Qué sigue lo deciden la mesa y la autora.
2. **La fila de no ítems para la hoja** es ahora la de las 60 (tabla 1); la de las 30 queda dentro de la misma celda.
3. **Mis propuestas y la lectura de la autora en la ampliación** (información): coinciden en 24 de 30. Las propuestas daban 7 con error, 1 dudosa, 22 sin error; la lectura da 9 con error, 21 sin error. Las que cambian: ficha 3, de «dudosa» a «con error»; ficha 17, de «sin error» a «con error»; ficha 20, de «con error» a «sin error»; ficha 24, de «sin error» a «con error»; ficha 26, de «con error» a «sin error»; ficha 30, de «sin error» a «con error».
4. **La ponderada total y la atención de RI con las 60** van como información (sección 6).

## 11. La foto del repo, los .pyc y el grep de convenciones

Lo genera `scripts/freno_t4t3_foto_tf.py` desde la foto del paso 0 (`foto_repo_antes_T4t3.json`) y la de después. Las dos quedan en `t4t2_fotos/`, en la carpeta permanente de esta sesión (`fuera_del_repo/scratchpads/<sesión>/scratchpad/`), fuera del repo y del paquete porque nombran todas las rutas del repo.

- **La foto** (`t1/foto_repo_tanda_final_t1.py`). La del paso 0: 10:44:11 a 10:44:25 del 2026-10-22, 58.130 entradas, sha256 `5d38f6f8c3c5f208df637011e5590d2f5fa7d9fb609a6aa307a4d6da158e8106`. Después: 11:19:17 a 11:19:30 del 2026-10-22, 58.142 entradas, 45 sin abrir y 342 enlaces, sha256 `0c489c16d7c1b4ebc7fe174c41b3fe4ad2e4ae0e391b78fb2df18cce5bb4531f`.
  - **12 nuevos:** 2 en `tanda_final/t4/, lo demás`; 4 en `tanda_final/t4/scripts/`; 6 en `tanda_final/t4/tasas/`.
  - **0 borrados:** ninguno.
  - **0 cambiados:** ninguno.
  - **Fuera de lo admitido:** 0.
  - **Los `NO_ABRIR_` en `t4/`:** 0 en las dos fotos.
  - **`unidades_a_la_vista_T4.json`** (`t3/muestras/`): este tramo no la toca; sha256 `4b9605f2d76cee42b13597e35b0eb7652e9e2723b952d91e0e09da1f63745633` en el paso 0 y `4b9605f2d76cee42b13597e35b0eb7652e9e2723b952d91e0e09da1f63745633` después; iguales: True.
- **Los `.pyc`:** 11.236 líneas en el paso 0 y 11.236 después; listas iguales: True.

**El sha256 de los archivos de este tramo, de la foto de después:**

| archivo | sha256 |
|---|---|
| `data/experiment/tanda_final/t4/consola_tablas_t4t3_tf.txt` | `d73ddf3f1df70ab1cabe4081027a35284d3ad39a7c306032b7ca1f9c11ba2c4a` |
| `data/experiment/tanda_final/t4/tablas_t4_tramo3.md` | `34ed98afd74be2d365704bd47bd597a82943f023dcb4606a9f224b75d14373a9` |
| `data/experiment/tanda_final/t4/tasas/consola_tasas_t4t3_tf.txt` | `b43e6eff338a29fd5b19a1f737bd9cc54576418f7c2e2dadf9f1c15020776edb` |
| `data/experiment/tanda_final/t4/tasas/consola_verif_tasas_independiente_t4t3_tf.txt` | `30ad6e7f7f99f7562b1dcebafc0374b322b118d78861d2fc451f086441614bcf` |
| `data/experiment/tanda_final/t4/tasas/distribuciones_bajo_H0_t4_tramo3.json` | `abc653b967a33f2d8d8ef5b8032519e3218e79d387b7679c1e145c119782b868` |
| `data/experiment/tanda_final/t4/tasas/tasas_t4_tramo3.json` | `5979134e6339d4cb66c5c7b332ebdd839d57610d790323ed5da6499272f37b7f` |
| `data/experiment/tanda_final/t4/tasas/umbrales_t4_por_celdas_mesa_al_importar_t4t3_tf.json` | `9a81ead83e7d7d9765916e2ee72f346b494554146de4f9c2445a3cf1db46a009` |
| `data/experiment/tanda_final/t4/tasas/verif_tasas_independiente_t4t3_tf.json` | `972ab3afd2ed2666ca97284b72f8a6f0b9e4e39b45a48fb13fbab3a892011af3` |

**Los scripts de este tramo** (`t4/scripts/`, sha256 de la foto de después):

| script | sha256 |
|---|---|
| `freno_t4t3_foto_tf.py` | `a75c0fbabd827559b204136b2ba0665480501898bbf6d5f77e876958535e0899` |
| `tablas_t4t3_tf.py` | `6a79c960569befc55aa2794f9f8da32544b879644684e90bc88181ddb834f76a` |
| `tasas_t4t3_tf.py` | `dc319f9ae0e2456435b52654cdb2afc7b5d2563bb7a3d59514227e189200856d` |
| `verif_tasas_independiente_t4t3_tf.py` | `bbb8f0fb7acaec9c87ca73b6a844c954a5633bba5d39c551712631b2668ccf69` |

- **El grep de convenciones** (`t3/scripts/grep_convenciones_tf.py`, sin cambios, con `LC_ALL=en_US.UTF-8`) sobre los 12 archivos nuevos de la foto: 0 coincidencias de los tokens del nombre y de los términos, 0 archivos con rutas absolutas, 0 tokens dentro de rutas absolutas; control positivo, 2. Su salida va en el paquete. Este FRENO y su script se escriben después de la foto: el control final del paquete confirma que son lo único nuevo desde ella y les pasa el grep.
- **Un `__pycache__` que creé y borré antes de la foto** (sección 13, punto 1): la lista de `.pyc` de después es la del paso 0.
- **No hice copias del repo** en este tramo. Ningún `git clone`.

## 12. El script de cada cifra

| cifras | script (`t4/scripts/`) | salida |
|---|---|---|
| las tasas sobre las 60, los dos frenos, lo del segundo tramo rehecho, la ponderada total y la atención de RI con las 60 | `tasas_t4t3_tf.py` | `tasas/tasas_t4_tramo3.json`, `tasas/distribuciones_bajo_H0_t4_tramo3.json`, `tasas/consola_tasas_t4t3_tf.txt` |
| la verificación independiente | `verif_tasas_independiente_t4t3_tf.py` | `tasas/verif_tasas_independiente_t4t3_tf.json` y su consola |
| las tablas 1 a 12 y las cifras para la hoja | `tablas_t4t3_tf.py` | `tablas_t4_tramo3.md`, `consola_tablas_t4t3_tf.txt` |
| la foto (sección 11) | `freno_t4t3_foto_tf.py` | la sección 11; su salida, en el paquete |
| el texto de este FRENO | `freno_t4t3_armar_tf.py` | este archivo |
| el paso 0 (sección 1) | `paso0_t4_tramo3.sh` y `paso0_foto_contra_commits_t4_tramo3.py`, en el paquete | su salida, pegada |

- **Los controles de la entrada** de `tasas_t4t3_tf.py`: 48 de 48 pasan.
- **La verificación independiente** recuenta las dos marcadas sin el código de la mesa ni `tasas_t4t3_tf.py` y recalcula con fracciones exactas, también el p-valor y el umbral sobre las 60 por convolución: 62 de 62 cifras iguales, 0 distintas.
- **Cómo salieron los scripts:** los cuatro primeros los escribieron adaptadores con reemplazos exactos desde los del segundo tramo (`adaptar_*_t4_tramo3.py`, en el paquete); `freno_t4t3_armar_tf.py` lo escribí desde el del segundo tramo. Los diffs enteros de los cinco contra los del segundo tramo van en el anexo.

## 13. Errores propios, con su causa

1. **Escribí un `__pycache__` en `t4/scripts/`.** Para controlar la sintaxis de `freno_t4t3_foto_tf.py` corrí `python -m py_compile`, que escribe el `.pyc` aunque se pase `-B`. Lo vi enseguida con un `find`, y borré el archivo y la carpeta (los dos, solo míos y sin rastrear) antes de la foto de después. La lista de `.pyc` volvió a ser la del paso 0, y la de después lo confirma.

## 14. Lo que no hice

- **T5 ni las FICHAS.**
- **Lo que no toqué:** las marcadas, los sellos, las planillas, los convertidores, los LEEME y los controles de la mesa; nada de `t3/` ni de fuera de `t4/`.
- **Commits y escrituras ajenas:** no commiteé ni preparé mensajes de commit; no escribí en la memoria, en `.claude/` ni en `.gitignore`.
- **El scratchpad:** nada que se necesite después queda solo en él. El paquete y su copia permanente llevan el paso 0, los adaptadores, la sección de la foto y el grep; las fotos van a `t4t2_fotos/`.
- Los heredocs, siempre con el delimitador entre comillas.

FRENO T4, tercer tramo. Espero la revisión de la mesa.

## Anexo. Los diffs enteros de los cinco scripts contra los del segundo tramo

Con `difflib.unified_diff`, sin líneas de contexto (`n=0`): cada bloque trae todo lo que cambia.

### `tasas_t4t2_tf.py` → `tasas_t4t3_tf.py` (207 líneas cambiadas)

```diff
--- tanda_final/t4/scripts/tasas_t4t2_tf.py
+++ tanda_final/t4/scripts/tasas_t4t3_tf.py
@@ -1,39 +1,29 @@
-"""B6.1, tanda final, T4, segundo tramo, puntos 4 y 5 del «seguí»: las tasas, la atención y el freno, sobre la lectura sellada de la
-autora, con el pre-registro firmado (docs/preregistro_tanda_final.md, firma en 4de7f2a7, §6), su versión derivada para la lectura
-(tanda_final/preregistro/preregistro_tanda_final_derivada_T4.md) y los umbrales que T3 calculó con los pesos reales
-(t3/muestras/umbrales_t4_tf.json). Es tanda1/t4/scripts/tasas_t4t2.py con las rutas, los nombres y los umbrales de la tanda final, y con
-las líneas de base de la versión derivada. Solo lee y calcula; escribe solo en <trabajo>, <salida.json> y <distribuciones.json>. No lee el
-grafo, ni estados de E3, ni reintentos.
-
-  1. Los controles de la entrada, antes de contar:
-       - cada marcada tiene el sha256 de su línea del sello (t4/lectura_autora/sello_lectura_T4.txt);
-       - umbrales_t4_tf.json tiene el sha256 del «seguí»; la versión derivada y su .huecos.json, los de T3;
-       - el script de la mesa (data/experiment/controles_tanda1/umbrales_t4_por_celdas_mesa.py) se importa sin cambiarlo, como en T3
-         (t3/scripts/umbrales_t4_tf.py), y su salida al importarse es byte a byte su JSON. De él salen wilson, pmf, cola_sup,
-         distribucion, BASE (la tanda 0) y Z;
-       - cada marcada tiene, por celda, los mismos ids que su muestra (t3/muestras/), y cada veredicto es válido;
-       - las N por celda de umbrales_t4_tf.json son las de t3/muestras/poblaciones_t4_t3f_tf.json (aceptadas, cola, (2) y (7)) y las de
-         t3/muestras/poblaciones_t4t1_tf.json ((1), (3) y (12)), y las n por celda son las de la muestra;
-       - cada línea de base de la tanda 1 (los valores T4.* del .huecos.json de la versión derivada) está tal cual en la versión derivada.
-  2. La regla de las dudosas (pre-registro, §6; registro, §35): en la cola y en las dos de las aceptadas, «dudosa» cuenta como error para
-     la tasa, la atención y el freno. La misma cuenta con las dudosas fuera, sobre las decididas, va al lado como sensibilidad y no decide
-     nada; si diera otra decisión de atención o de freno, se declara, y rige la primera.
-  3. Las aceptadas, por estrato: T = suma w_c k_c / n_c, con w_c = N_c / N (umbrales_t4_tf.json); Wilson al 95 % con
-     n_ef = 1 / suma w_c^2 / n_c; la atención, P(T' >= T) bajo H0 (cada celda en la tasa de la tanda 0 del estrato, la base del script
-     sellado) con la distribución de T' enumerada entera (`distribucion` de la mesa), y salta si es <= 0,05; el freno por intervalos, si
-     el límite inferior del Wilson de T pasa el superior del Wilson de la tanda 0 (la misma comparación que `umbrales` de la mesa). El
-     freno por la atención sobre las 60 solo se mira en un tercer tramo, si hay ampliación.
-     La tasa ponderada total, p = suma W_s T_s con W_s = N_s / N, con el Wilson de n_ef = 1 / suma (W_s w_c)^2 / n_c de las ocho celdas.
-     La atención propia de RI: t = suma v k / n en las cuatro celdas RI de los dos estratos, v = N_(s,c) / N_RI, con el test exacto de
-     `atencion_ri` de T3 (cada celda bajo H0 en la tasa de la tanda 0 de su estrato). NG sin_raiz, por celda y sin umbral.
-  4. La cola: la ponderada por celda con los pesos de la cola, su Wilson con n_ef y la regla del 25 % (se dispara si el límite superior
-     pasa 0,25), como cifra y vigilancia, no como freno.
-  5. Las vigilancias (1), (2), (3) y (7) y la (12): la cuenta de cada respuesta y la tasa de la que se vigila, con su Wilson. Sus muestras
-     salieron por celdas y el pre-registro no fija su ponderación: van la cruda (k sobre las leídas, Wilson con esa n) y la ponderada por
-     celda (Wilson con n_ef), las dos. En la (1), las no decidibles fuera de la tasa, con su cuenta (registro de decisiones, §29). En la
-     (12), correctas sobre 30, con las no decidibles aparte y en el denominador (enmienda de la observación 12, :107-111); las
-     incorrectas, por capa_pipeline. Los pesos de la (1), la (3) y la (12) son los de t3/muestras/poblaciones_t4t1_tf.json (la (12), con
-     las aristas de extracción de la (10), sin remite_a). La (7) se leyó entera, sin celdas: solo la cruda.
-  6. Cada cifra con su línea de base: la de la tanda 1, de la versión derivada, con la de la tanda 0 al lado (la base del script de la
-     mesa, la de la cola de umbrales_t4_tf.json y las de la tanda 0 que dan los scripts del segundo tramo de la tanda 1).
-Uso: python3 -I -B tasas_t4t2_tf.py <raíz> <trabajo> <salida.json> <distribuciones.json>
+"""B6.1, tanda final, T4, tercer tramo: las tasas de las aceptadas no ítems sobre las 60 (las 30 del primer tramo y las 30 de la
+ampliación) y el freno por la atención sobre las 60, sobre la lectura sellada de la autora. Es t4/scripts/tasas_t4t2_tf.py (segundo
+tramo), que rehace todo lo del segundo tramo y controla que dé lo mismo, con lo que agrega el tercer tramo. Solo lee y calcula; escribe
+solo en <trabajo>, <salida.json> y <distribuciones.json>. No lee el grafo, ni estados de E3, ni reintentos.
+
+  1. Los controles de la entrada, antes de contar, los del segundo tramo y además:
+       - la marcada de la ampliación (t4/ampliacion/lectura_autora/aceptadas_no_items_ampliacion_marcada.csv) tiene el sha256 de su sello
+         (sello_lectura_T4_ampliacion.txt, una línea);
+       - tiene, por celda, los mismos ids que su muestra (t4/ampliacion/muestras/aceptadas_no_items_ampliacion.json), cada veredicto es
+         válido y ninguna unidad está entre las 30 del primer tramo.
+  2. La regla de las dudosas (pre-registro, §6; registro, §35), como en el segundo tramo.
+  3. Lo del segundo tramo, rehecho sin cambios: las aceptadas por estrato, la ponderada total, la atención de RI, NG sin_raiz, la cola, las
+     vigilancias y la (12). Al final se controla que cada bloque dé lo mismo que t4/tasas/tasas_t4_tramo2.json, y que en las líneas de
+     base cambien solo los dos textos con el nombre del archivo.
+  3 bis. Las aceptadas no ítems sobre las 60, con los mismos pesos de celda (umbrales_t4_tf.json): por celda, las del primer tramo, las
+     de la ampliación y las 60; T = suma w_c k_c / n_c y su Wilson con n_ef = 1 / suma w_c^2 / n_c; la sensibilidad sin las dudosas.
+       - El freno por la atención sobre las 60 (script de la mesa, docstring, «Freno»: «o si la atención se confirma sobre las 60 (cada
+         celda con el doble de unidades)»): contra el umbral `freno_por_atencion_sobre_60` de aceptadas.no_items en umbrales_t4_tf.json.
+         Se controla, celda por celda, que la ampliación deje el doble de unidades. Con el doble, la distribución bajo H0 con esas n es la
+         misma con la que la mesa calculó el umbral: se enumera entera (`distribucion` de la mesa), se recalcula el umbral exacto (la
+         menor tasa con P(T' >= t) <= 0,05) y se controla que, redondeado, sea el del JSON; el freno salta si T >= ese umbral, y el
+         p-valor sobre las 60 va al lado. Si una celda no tuviera el doble, la regla se aplicaría con las n reales, por el p-valor, y se
+         declararía.
+       - El freno por intervalos sobre las 60: el límite inferior del Wilson de T contra el superior del Wilson de la tanda 0.
+       - Como información, con lo del segundo tramo al lado: la ponderada total y la atención propia de RI con ítems en sus 30 y no ítems
+         en sus 60, con el mismo método.
+  4 a 6. La cola, las vigilancias, la (12) y las líneas de base, como en el segundo tramo. En las líneas de base, la coma decimal se
+     pone solo en los números (en el segundo tramo, el `.replace(".", ",")` tocaba también el nombre del archivo).
+Uso: python3 -I -B tasas_t4t3_tf.py <raíz> <trabajo> <salida.json> <distribuciones.json>
@@ -58,0 +49,3 @@
+LAA = TF / "t4/ampliacion/lectura_autora"
+MUESTRA_AMP = TF / "t4/ampliacion/muestras/aceptadas_no_items_ampliacion.json"
+TRAMO2 = TF / "t4/tasas/tasas_t4_tramo2.json"
@@ -94,0 +88,8 @@
+sello_amp = {}
+for linea in (LAA / "sello_lectura_T4_ampliacion.txt").read_text(encoding="utf-8").splitlines():
+    if linea.strip():
+        h, nombre, hora = re.split(r"\s{2,}", linea.strip())
+        sello_amp[nombre] = {"sha256": h, "hora": hora}
+controles["sello de la ampliación: 1 línea, la de su marcada"] = list(sello_amp) == ["aceptadas_no_items_ampliacion_marcada.csv"]
+controles["la marcada de la ampliación tiene el sha256 de su sello"] = \
+    sha(LAA / "aceptadas_no_items_ampliacion_marcada.csv") == sello_amp["aceptadas_no_items_ampliacion_marcada.csv"]["sha256"]
@@ -99 +100 @@
-control_out = W / "umbrales_t4_por_celdas_mesa_al_importar_t4t2_tf.json"
+control_out = W / "umbrales_t4_por_celdas_mesa_al_importar_t4t3_tf.json"
@@ -148,0 +150,21 @@
+
+
+def leer_ampliacion() -> dict:
+    """La marcada de la ampliación, por celda, contra los ids de su muestra; los veredictos, contra los válidos; y ninguna unidad
+    repetida con las 30 del primer tramo."""
+    with open(LAA / "aceptadas_no_items_ampliacion_marcada.csv", encoding="utf-8", newline="") as fh:
+        filas = list(csv.DictReader(fh, delimiter=";"))
+    m = json.loads(MUESTRA_AMP.read_text(encoding="utf-8"))
+    por_celda = {c: [f for f in filas if f["celda"] == c] for c in CELDAS}
+    controles["ampliación: la muestra es la del estrato de no ítems"] = m["estrato"] == "aceptadas:no_items"
+    controles["ampliación: los ids por celda son los de la muestra"] = all(
+        sorted(f["id"] for f in por_celda[c]) == sorted(m["celdas"][c]["elementos"]) for c in CELDAS) \
+        and len(filas) == m["n"] == sum(len(v) for v in por_celda.values())
+    controles["ampliación: las n por celda son las de la muestra"] = all(len(por_celda[c]) == m["n_por_celda"][c] for c in CELDAS)
+    controles["ampliación: los veredictos son válidos"] = all(f["veredicto_autora"] in ("con error", "sin error", "dudosa") for f in filas)
+    controles["ampliación: ninguna unidad está entre las 30 del primer tramo"] = \
+        not {f["id"] for f in filas} & {f["id"] for f in L["aceptadas:no_items"]["filas"]}
+    return {"filas": filas, "por_celda": por_celda, "muestra": m}
+
+
+LA60 = leer_ampliacion()
@@ -278,0 +301,71 @@
+
+# 3 bis. Las aceptadas no ítems sobre las 60: las 30 del primer tramo y las 30 de la ampliación, con los mismos pesos de celda
+cu30 = res["aceptadas"]["no_items"]["por_celda"]
+cuA = {c: {r: sum(1 for f in LA60["por_celda"][c] if f["veredicto_autora"] == r) for r in R_ERR} for c in CELDAS}
+for c in CELDAS:
+    cuA[c]["n"] = len(LA60["por_celda"][c])
+cu60 = {c: {r: cu30[c][r] + cuA[c][r] for r in R_ERR + ["n"]} for c in CELDAS}
+Ns = U["aceptadas"]["no_items"]["N_por_celda"]
+w = {c: F(Ns[c], sum(Ns.values())) for c in CELDAS}
+p0 = RU.BASE["no_items"]["k"] / RU.BASE["no_items"]["n"]
+sup0 = RU.BASE["no_items"]["wilson"][1]
+u60 = U["aceptadas"]["no_items"]["umbrales"]["freno_por_atencion_sobre_60"]
+doble = {c: cu60[c]["n"] == 2 * cu30[c]["n"] for c in CELDAS}
+s60 = {"N_por_celda": Ns, "pesos": {c: r4(w[c]) for c in CELDAS}, "por_celda_primer_tramo": cu30, "por_celda_ampliacion": cuA,
+       "por_celda": cu60, "cada_celda_con_el_doble": doble, "p0_tanda0": p0, "wilson_tanda0": [r4(x) for x in RU.BASE["no_items"]["wilson"]],
+       "umbral_del_freno_por_atencion_sobre_60": u60,
+       "como": ("la atención sobre las 60 se confirma si T >= el umbral (la menor tasa con P(T' >= t) <= 0,05 bajo H0, con cada celda con el "
+                "doble de unidades); el freno por intervalos, si el límite inferior del Wilson de T pasa el superior del Wilson de la tanda 0")}
+T60 = {}
+for nombre, kfun, nfun in (("regla", lambda c: cu60[c]["con error"] + cu60[c]["dudosa"], lambda c: cu60[c]["n"]),
+                           ("sensibilidad_sin_dudosas", lambda c: cu60[c]["con error"], lambda c: cu60[c]["n"] - cu60[c]["dudosa"])):
+    k = {c: kfun(c) for c in CELDAS}
+    n = {c: nfun(c) for c in CELDAS}
+    pq = ponderada(w, k, n)
+    pv, d = p_valor(w, n, p0, pq["T"])
+    sup = RU.cola_sup(d)
+    t_um = min(t for t in sup if sup[t] <= 0.05)
+    con_el_doble = all(n[c] == 2 * cu30[c]["n"] for c in CELDAS)
+    por_umbral = pq["T"] >= t_um
+    s60[nombre] = {"k_por_celda": k, "n_por_celda": n, "errores": sum(k.values()), "leidas": sum(n.values()),
+                   "tasa_ponderada": r4(pq["T"]), "tasa_ponderada_fraccion": str(pq["T"]), "n_efectivo_kish": round(float(pq["n_ef"]), 3),
+                   "wilson": wil(pq["T"], pq["n_ef"]), "cada_celda_con_el_doble": con_el_doble,
+                   "umbral_recalculado": r4(t_um), "umbral_recalculado_fraccion": str(t_um),
+                   "umbral_recalculado_es_el_del_json": r4(t_um) == u60["umbral_tasa_ponderada"] if con_el_doble else None,
+                   "p_valor_sobre_60": round(pv, 4), "freno_por_atencion_sobre_60": por_umbral if con_el_doble else pv <= 0.05,
+                   "el_umbral_y_el_p_valor_dicen_lo_mismo": por_umbral == (pv <= 0.05),
+                   "freno_por_intervalos": RU.wilson(float(pq["T"]), float(pq["n_ef"]))[0] > sup0,
+                   "puntos_de_la_distribucion": len(d), "suma_de_la_distribucion": round(sum(d.values()), 9)}
+    s60[nombre]["freno"] = s60[nombre]["freno_por_atencion_sobre_60"] or s60[nombre]["freno_por_intervalos"]
+    dist_out[f"aceptadas:no_items:sobre_60:{nombre}"] = tabla_dist(d)
+    T60[nombre] = (pq["T"], w, n)
+s60["la_sensibilidad_da_otra_decision"] = {
+    x: s60["regla"][x] != s60["sensibilidad_sin_dudosas"][x] for x in ("freno_por_atencion_sobre_60", "freno_por_intervalos", "freno")}
+res["aceptadas_no_items_sobre_60"] = s60
+# como información: la ponderada total y la atención de RI con ítems en sus 30 y no ítems en sus 60
+info = {"como": "ítems con sus 30 leídas y no ítems con las 60, con el método del segundo tramo; información, sin decisión",
+        "total": {"pesos_de_los_estratos": {s: r4(Ws[s]) for s in ESTR}}, "atencion_RI": {"N_RI": N_RI, "umbral_T3": ri["umbral_T3"]}}
+for nombre in ("regla", "sensibilidad_sin_dudosas"):
+    tv = {"items": Tvals[("items", nombre)], "no_items": T60[nombre]}
+    p = sum(Ws[s] * tv[s][0] for s in ESTR)
+    ne = 1 / sum(Ws[s] ** 2 * tv[s][1][c] ** 2 / tv[s][2][c] for s in ESTR for c in CELDAS if tv[s][2][c])
+    info["total"][nombre] = {"tasa_ponderada": r4(p), "n_efectivo_kish": round(float(ne), 3), "wilson": wil(p, ne)}
+    k, n = {}, {}
+    for s, c in celdas_ri:
+        b = res["aceptadas"]["items"][nombre] if s == "items" else s60[nombre]
+        k[(s, c)], n[(s, c)] = b["k_por_celda"][c], b["n_por_celda"][c]
+    con = [sc for sc in celdas_ri if n[sc]]
+    t = sum(v[sc] * F(k[sc], n[sc]) for sc in con)
+    d = {}
+    for ks in itertools.product(*[range(n[sc] + 1) for sc in con]):
+        tt = sum(v[sc] * F(kk, n[sc]) for sc, kk in zip(con, ks))
+        d[tt] = d.get(tt, 0.0) + math.prod(RU.pmf(kk, n[sc], p0s[sc[0]]) for sc, kk in zip(con, ks))
+    pv = sum(pr for tt, pr in d.items() if tt >= t)
+    ne = 1 / sum(v[sc] ** 2 / n[sc] for sc in con)
+    info["atencion_RI"][nombre] = {"k_por_celda": {f"{s}:{c}": k[(s, c)] for s, c in celdas_ri},
+                                   "n_por_celda": {f"{s}:{c}": n[(s, c)] for s, c in celdas_ri}, "errores": sum(k.values()),
+                                   "leidas": sum(n.values()), "tasa_ponderada_RI": r4(t), "n_efectivo_kish": round(float(ne), 3),
+                                   "wilson": wil(t, ne), "p_valor": round(pv, 4), "p_valor_hasta_0_05": pv <= 0.05,
+                                   "puntos_de_la_distribucion": len(d), "suma_de_la_distribucion": round(sum(d.values()), 9)}
+    dist_out[f"informacion_con_las_60:atencion_RI:{nombre}"] = tabla_dist(d)
+res["informacion_con_las_60"] = info
@@ -365 +458,2 @@
-b0 = lambda s: f"{RU.BASE[s]['k']} de {RU.BASE[s]['n']}, Wilson [{RU.BASE[s]['wilson'][0]:.4f}; {RU.BASE[s]['wilson'][1]:.4f}]".replace(".", ",")  # noqa: E731
+cm = lambda x: f"{x:.4f}".replace(".", ",")  # noqa: E731  (la coma decimal, solo en el número)
+b0 = lambda s: f"{RU.BASE[s]['k']} de {RU.BASE[s]['n']}, Wilson [{cm(RU.BASE[s]['wilson'][0])}; {cm(RU.BASE[s]['wilson'][1])}]"  # noqa: E731
@@ -372 +466 @@
-                        "tanda0": f"{t0['p']:.4f}, Wilson [{t0['wilson'][0]:.4f}; {t0['wilson'][1]:.4f}], mismo método (umbrales_t4_tf.json)".replace(".", ",")},
+                        "tanda0": f"{cm(t0['p'])}, Wilson [{cm(t0['wilson'][0])}; {cm(t0['wilson'][1])}], mismo método (umbrales_t4_tf.json)"},
@@ -374 +468 @@
-                    "tanda0": f"la tasa de RI bajo H0, con las tasas de la tanda 0: {U['atencion_RI']['tasa_de_RI_bajo_H0']:.4f} (umbrales_t4_tf.json)".replace(".", ",")},
+                    "tanda0": f"la tasa de RI bajo H0, con las tasas de la tanda 0: {cm(U['atencion_RI']['tasa_de_RI_bajo_H0'])} (umbrales_t4_tf.json)"},
@@ -388 +482,15 @@
-                   **{f"muestra {m}": sha(a) for m, (_, a, _) in MUESTRAS.items()}}
+                   **{f"muestra {m}": sha(a) for m, (_, a, _) in MUESTRAS.items()},
+                   "sello_lectura_T4_ampliacion.txt": sha(LAA / "sello_lectura_T4_ampliacion.txt"),
+                   "aceptadas_no_items_ampliacion_marcada.csv": sha(LAA / "aceptadas_no_items_ampliacion_marcada.csv"),
+                   "muestra aceptadas:no_items:ampliacion": sha(MUESTRA_AMP), "tasas_t4_tramo2.json": sha(TRAMO2)}
+# lo del segundo tramo da lo mismo: cada bloque igual, y en las líneas de base solo cambian los dos textos con el nombre del archivo
+t2 = json.loads(TRAMO2.read_text(encoding="utf-8"))
+BLOQUES = ("regla_de_las_dudosas", "z", "aceptadas", "atencion_RI", "NG_sin_raiz", "cola", "vigilancias", "observacion:12", "ampliacion")
+igual_t2 = {k: json.loads(json.dumps(res[k], ensure_ascii=False)) == t2[k] for k in BLOQUES}
+lb_dif = sorted(f"{k}.{x}" for k in res["lineas_de_base"] for x in (res["lineas_de_base"][k] if isinstance(res["lineas_de_base"][k], dict) else [None])
+                if (res["lineas_de_base"][k][x] if x else res["lineas_de_base"][k]) != (t2["lineas_de_base"][k][x] if x else t2["lineas_de_base"][k]))
+res["lo_del_segundo_tramo"] = {"bloques_iguales_a_tasas_t4_tramo2": igual_t2, "lineas_de_base_que_cambian": lb_dif,
+                               "controles_del_segundo_tramo_iguales": all(res["controles"][k] == v for k, v in t2["controles"].items())}
+assert all(igual_t2.values()), igual_t2
+assert lb_dif == ["aceptadas:total.tanda0", "atencion_RI.tanda0"], lb_dif
+assert "tf,json" not in json.dumps(res["lineas_de_base"], ensure_ascii=False)
@@ -420,0 +529,11 @@
+for nombre in ("regla", "sensibilidad_sin_dudosas"):
+    x = s60[nombre]
+    print(f"no ítems sobre las 60 [{nombre}] errores {x['errores']} de {x['leidas']} | k {x['k_por_celda']} n {x['n_por_celda']} | "
+          f"T {x['tasa_ponderada']} Wilson {x['wilson']} n_ef {x['n_efectivo_kish']} | umbral {x['umbral_recalculado']} (el del JSON: "
+          f"{x['umbral_recalculado_es_el_del_json']}) p {x['p_valor_sobre_60']} | freno por la atención sobre las 60 "
+          f"{x['freno_por_atencion_sobre_60']} | freno por intervalos {x['freno_por_intervalos']} | freno {x['freno']}")
+print("   cada celda con el doble:", s60["cada_celda_con_el_doble"], "| la sensibilidad da otra decisión:", s60["la_sensibilidad_da_otra_decision"])
+for nombre in ("regla", "sensibilidad_sin_dudosas"):
+    print(f"con las 60 [{nombre}] total", info["total"][nombre], "| RI", {k: info["atencion_RI"][nombre][k] for k in
+          ("errores", "leidas", "tasa_ponderada_RI", "wilson", "p_valor")})
+print("lo del segundo tramo:", res["lo_del_segundo_tramo"])
```

### `verif_tasas_independiente_t4t2_tf.py` → `verif_tasas_independiente_t4t3_tf.py` (91 líneas cambiadas)

```diff
--- tanda_final/t4/scripts/verif_tasas_independiente_t4t2_tf.py
+++ tanda_final/t4/scripts/verif_tasas_independiente_t4t3_tf.py
@@ -1,9 +1,12 @@
-"""B6.1, tanda final, T4, segundo tramo: verificación independiente de tasas_t4t2_tf.py. No importa el script de la mesa ni tasas_t4t2_tf.py:
-recuenta las marcadas por celda, toma los N por celda de umbrales_t4_tf.json y las tasas de la tanda 0 que da el script de la mesa (6 de 30
-en ítems y 4 de 30 en no ítems, leídas de su texto con una expresión regular), y recalcula con fracciones exactas:
-  - la tasa ponderada de cada estrato, su n efectivo de Kish y su Wilson (fórmula escrita aquí, z = 1,959964);
-  - el p-valor de la atención, P(T' >= T) bajo H0, por convolución exacta de las binomiales de cada celda (probabilidades en Fraction);
-  - el freno por intervalos: el límite inferior del Wilson de T contra el superior del Wilson de la tanda 0;
-  - la atención de RI, la ponderada total, la cola y su regla del 25 %, y las vigilancias y la (12), crudas.
-Compara cada cifra con la salida de tasas_t4t2_tf.py (t4/tasas/tasas_t4_tramo2.json) y escribe <salida.json>.
-Uso: python3 -I -B verif_tasas_independiente_t4t2_tf.py <raíz> <salida.json>
+"""B6.1, tanda final, T4, tercer tramo: verificación independiente de tasas_t4t3_tf.py. Es verif_tasas_independiente_t4t2_tf.py (segundo
+tramo) contra la salida del tercer tramo (t4/tasas/tasas_t4_tramo3.json), con las cifras nuevas. No importa el script de la mesa ni
+tasas_t4t3_tf.py: recuenta las marcadas por celda (también la de la ampliación), toma los N por celda y el umbral de umbrales_t4_tf.json y
+las tasas de la tanda 0 del texto del script de la mesa, y recalcula con fracciones exactas:
+  - lo del segundo tramo, como allí;
+  - las aceptadas no ítems sobre las 60 (las 30 del primer tramo y las 30 de la ampliación): las k y las n por celda, si cada celda tiene
+    el doble, la tasa ponderada, su n efectivo de Kish y su Wilson;
+  - el p-valor sobre las 60 por convolución exacta (probabilidades en Fraction), el umbral exacto (la menor tasa con P(T' >= t) <= 1/20)
+    y si es el de umbrales_t4_tf.json, el freno por la atención sobre las 60 (T >= umbral) y el freno por intervalos;
+  - la ponderada total y la atención de RI con ítems en sus 30 y no ítems en sus 60.
+Compara cada cifra con la salida de tasas_t4t3_tf.py y escribe <salida.json>.
+Uso: python3 -I -B verif_tasas_independiente_t4t3_tf.py <raíz> <salida.json>
@@ -22 +25 @@
-X = json.loads((TF / "t4/tasas/tasas_t4_tramo2.json").read_text(encoding="utf-8"))
+X = json.loads((TF / "t4/tasas/tasas_t4_tramo3.json").read_text(encoding="utf-8"))
@@ -37,0 +41,5 @@
+        return list(csv.DictReader(fh, delimiter=";"))
+
+
+def marcada_ampliacion() -> list:
+    with open(TF / "t4/ampliacion/lectura_autora/aceptadas_no_items_ampliacion_marcada.csv", encoding="utf-8", newline="") as fh:
@@ -143,0 +152,63 @@
+# el tercer tramo: las aceptadas no ítems sobre las 60
+f30, fA = marcada("aceptadas_no_items"), marcada_ampliacion()
+f60 = f30 + fA
+N = U["aceptadas"]["no_items"]["N_por_celda"]
+w = {c: F(N[c], sum(N.values())) for c in CEL}
+n30 = {c: sum(1 for x in f30 if x["celda"] == c) for c in CEL}
+B60 = X["aceptadas_no_items_sobre_60"]
+for nombre, err, fuera in (("regla", ("con error", "dudosa"), ()), ("sensibilidad_sin_dudosas", ("con error",), ("dudosa",))):
+    k = {c: sum(1 for x in f60 if x["celda"] == c and x["veredicto_autora"] in err) for c in CEL}
+    n = {c: sum(1 for x in f60 if x["celda"] == c and x["veredicto_autora"] not in fuera) for c in CEL}
+    T = sum(w[c] * F(k[c], n[c]) for c in CEL if n[c])
+    ne = 1 / sum(w[c] ** 2 / n[c] for c in CEL if n[c])
+    p0 = F(*BASE["no_items"])
+    d = conv(w, n, p0)
+    pv = sum(pr for tt, pr in d.items() if tt >= T)
+    acum, um = F(0), None
+    for tt in sorted(d, reverse=True):
+        acum += d[tt]
+        if acum > F(1, 20):
+            break
+        um = tt
+    doble = all(n[c] == 2 * n30[c] for c in CEL)
+    sup0 = wilson(float(p0), BASE["no_items"][1])[1]
+    b = B60[nombre]
+    comparar(f"sobre_60:{nombre}:k_por_celda", k, b["k_por_celda"])
+    comparar(f"sobre_60:{nombre}:n_por_celda", n, b["n_por_celda"])
+    comparar(f"sobre_60:{nombre}:errores", sum(k.values()), b["errores"])
+    comparar(f"sobre_60:{nombre}:cada_celda_con_el_doble", doble, b["cada_celda_con_el_doble"])
+    comparar(f"sobre_60:{nombre}:tasa_ponderada", round(float(T), 4), b["tasa_ponderada"])
+    comparar(f"sobre_60:{nombre}:n_efectivo", round(float(ne), 3), b["n_efectivo_kish"])
+    comparar(f"sobre_60:{nombre}:wilson", wilson(float(T), float(ne)), b["wilson"])
+    comparar(f"sobre_60:{nombre}:p_valor", round(float(pv), 4), b["p_valor_sobre_60"])
+    comparar(f"sobre_60:{nombre}:umbral", round(float(um), 4), b["umbral_recalculado"])
+    comparar(f"sobre_60:{nombre}:umbral_es_el_de_umbrales_t4_tf",
+             round(float(um), 4) == U["aceptadas"]["no_items"]["umbrales"]["freno_por_atencion_sobre_60"]["umbral_tasa_ponderada"],
+             b["umbral_recalculado_es_el_del_json"])
+    comparar(f"sobre_60:{nombre}:freno_por_atencion", T >= um if doble else float(pv) <= 0.05, b["freno_por_atencion_sobre_60"])
+    comparar(f"sobre_60:{nombre}:freno_por_intervalos", wilson(float(T), float(ne))[0] > sup0, b["freno_por_intervalos"])
+    Ts[("no_items_60", nombre)] = (T, w, n)
+comparar("sobre_60:dudosas", sum(1 for x in f60 if x["veredicto_autora"] == "dudosa"), sum(B60["por_celda"][c]["dudosa"] for c in CEL))
+comparar("sobre_60:ampliacion_por_celda_n", {c: sum(1 for x in fA if x["celda"] == c) for c in CEL}, {c: B60["por_celda_ampliacion"][c]["n"] for c in CEL})
+# la ponderada total y la atención de RI con las 60 (ítems con sus 30), con la regla
+T60, w60, n60 = Ts[("no_items_60", "regla")]
+p = Ws["items"] * Ts["items"][0] + Ws["no_items"] * T60
+ne = 1 / (sum(Ws["items"] ** 2 * Ts["items"][1][c] ** 2 / Ts["items"][2][c] for c in CEL if Ts["items"][2][c])
+          + sum(Ws["no_items"] ** 2 * w60[c] ** 2 / n60[c] for c in CEL))
+comparar("con_las_60:total:tasa_ponderada", round(float(p), 4), X["informacion_con_las_60"]["total"]["regla"]["tasa_ponderada"])
+comparar("con_las_60:total:wilson", wilson(float(p), float(ne)), X["informacion_con_las_60"]["total"]["regla"]["wilson"])
+dd, t_ri = {F(0): F(1)}, F(0)
+for s, filas in (("items", marcada("aceptadas_items")), ("no_items", f60)):
+    for c in RI:
+        vv = F(U["aceptadas"][s]["N_por_celda"][c], NRI)
+        nc = sum(1 for x in filas if x["celda"] == c)
+        kc = sum(1 for x in filas if x["celda"] == c and x["veredicto_autora"] in ("con error", "dudosa"))
+        t_ri += vv * F(kc, nc)
+        p0 = F(*BASE[s])
+        nd = {}
+        for t_, pr in dd.items():
+            for kk in range(nc + 1):
+                nd[t_ + vv * F(kk, nc)] = nd.get(t_ + vv * F(kk, nc), F(0)) + pr * math.comb(nc, kk) * p0 ** kk * (1 - p0) ** (nc - kk)
+        dd = nd
+comparar("con_las_60:RI:tasa", round(float(t_ri), 4), X["informacion_con_las_60"]["atencion_RI"]["regla"]["tasa_ponderada_RI"])
+comparar("con_las_60:RI:p_valor", round(float(sum(pr for t_, pr in dd.items() if t_ >= t_ri)), 4), X["informacion_con_las_60"]["atencion_RI"]["regla"]["p_valor"])
```

### `tablas_t4t2_tf.py` → `tablas_t4t3_tf.py` (114 líneas cambiadas)

```diff
--- tanda_final/t4/scripts/tablas_t4t2_tf.py
+++ tanda_final/t4/scripts/tablas_t4t3_tf.py
@@ -1,6 +1,6 @@
-"""B6.1, tanda final, T4, segundo tramo: las cifras para la hoja de la revisión entre tandas y las tablas del FRENO, por script, desde la
-salida de tasas_t4t2_tf.py (<raíz>/data/experiment/tanda_final/t4/tasas/tasas_t4_tramo2.json). Es tanda1/t4/scripts/tablas_t4t2.py con
-las rutas de la tanda final y, en la tabla 1, la línea de base de la tanda 1 (los valores T4.* de la versión derivada, que tasas_t4t2_tf.py
-guarda en `lineas_de_base`) al lado de la de la tanda 0. Solo lee; escribe tanda_final/t4/tablas_t4_tramo2.md bajo <raíz> y la imprime.
-Los números van con coma decimal; los intervalos, como [inferior; superior].
-Uso: python3 -I -B tablas_t4t2_tf.py <raíz>
+"""B6.1, tanda final, T4, tercer tramo: las cifras para la hoja de la revisión entre tandas y las tablas del FRENO, por script, desde la
+salida de tasas_t4t3_tf.py (<raíz>/data/experiment/tanda_final/t4/tasas/tasas_t4_tramo3.json). Es t4/scripts/tablas_t4t2_tf.py (segundo
+tramo) con la fila de las aceptadas no ítems sobre las 60 en la tabla 1, la ponderada total y la atención de RI con las 60 (información)
+al lado de las del segundo tramo, y las tablas 10 a 12 del tercer tramo. Solo lee; escribe tanda_final/t4/tablas_t4_tramo3.md bajo <raíz>
+y la imprime. Los números van con coma decimal; los intervalos, como [inferior; superior].
+Uso: python3 -I -B tablas_t4t3_tf.py <raíz>
@@ -17 +17 @@
-TASAS = T4 / "tasas/tasas_t4_tramo2.json"
+TASAS = T4 / "tasas/tasas_t4_tramo3.json"
@@ -27 +27 @@
-SAL = "`tasas/tasas_t4_tramo2.json`"
+SAL = "`tasas/tasas_t4_tramo3.json`"
@@ -29,0 +30 @@
+B60, I6 = X["aceptadas_no_items_sobre_60"], X["informacion_con_las_60"]
@@ -34 +35 @@
-w = [f"Salida: `tasas/tasas_t4_tramo2.json` ({X['hora']}, sha256 `{sha}`), de `scripts/tasas_t4t2_tf.py`. Rutas relativas a "
+w = [f"Salida: `tasas/tasas_t4_tramo3.json` ({X['hora']}, sha256 `{sha}`), de `scripts/tasas_t4t3_tf.py`. Rutas relativas a "
@@ -44,0 +46,12 @@
+    if s == "no_items":  # la fila de la hoja es la de las 60; la de las 30 va dentro de la misma celda
+        r6, z6, pc6 = B60["regla"], B60["sensibilidad_sin_dudosas"], B60["por_celda"]
+        ce6, du6 = sum(pc6[c]["con error"] for c in CEL), sum(pc6[c]["dudosa"] for c in CEL)
+        w.append(f"| {nom}, sobre las 60 | {r6['errores']} de {r6['leidas']} ({ce6} con error y {pl(du6, 'dudosa', 'dudosas')}); ponderada "
+                 f"{d(r6['tasa_ponderada'])}, Wilson {iv(r6['wilson'])} (n ef. {d(r6['n_efectivo_kish'], 3)}); sin las dudosas, {z6['errores']} de "
+                 f"{z6['leidas']}, {d(z6['tasa_ponderada'])} {iv(z6['wilson'])}; sobre las 30 del primer tramo, {r['errores']} de {r['leidas']}, "
+                 f"{d(r['tasa_ponderada'])} | {lb1} | {round(A[s]['p0_tanda0'] * 30)} de 30, Wilson {iv(A[s]['wilson_tanda0'])} | atención sobre "
+                 f"las 30: {sn(r['atencion'])} (p {d(r['p_valor_atencion'])}); freno por la atención sobre las 60: "
+                 f"{sn(r6['freno_por_atencion_sobre_60'])} (umbral {d(r6['umbral_recalculado'])}, p {d(r6['p_valor_sobre_60'])}); freno por "
+                 f"intervalos: {sn(r6['freno_por_intervalos'])} | `scripts/tasas_t4t3_tf.py`, {SAL}, `aceptadas_no_items_sobre_60` y "
+                 f"`aceptadas.no_items` |")
+        continue
@@ -49 +62 @@
-             f"(p {d(r['p_valor_atencion'])}); freno: {sn(r['freno_por_intervalos'])} | `scripts/tasas_t4t2_tf.py`, {SAL}, `aceptadas.{s}` |")
+             f"(p {d(r['p_valor_atencion'])}); freno: {sn(r['freno_por_intervalos'])} | `scripts/tasas_t4t3_tf.py`, {SAL}, `aceptadas.{s}` |")
@@ -51 +64 @@
-w.append(f"| aceptadas, ponderada total | {d(t['regla']['tasa_ponderada'])}, Wilson {iv(t['regla']['wilson'])} (n ef. "
+w.append(f"| aceptadas, ponderada total | con las 30 de no ítems, {d(t['regla']['tasa_ponderada'])}, Wilson {iv(t['regla']['wilson'])} (n ef. "
@@ -53,2 +66,3 @@
-         f"{iv(t['sensibilidad_sin_dudosas']['wilson'])} | {LB['aceptadas:total']['tanda1']} | {d(t['tanda0_con_el_mismo_metodo']['p'])}, Wilson "
-         f"{iv(t['tanda0_con_el_mismo_metodo']['wilson'])} (mismo método) | sin umbral | `scripts/tasas_t4t2_tf.py`, {SAL}, `aceptadas.total` |")
+         f"{iv(t['sensibilidad_sin_dudosas']['wilson'])}; con las 60 de no ítems (información), {d(I6['total']['regla']['tasa_ponderada'])}, "
+         f"Wilson {iv(I6['total']['regla']['wilson'])} (n ef. {d(I6['total']['regla']['n_efectivo_kish'], 3)}) | {LB['aceptadas:total']['tanda1']} | {d(t['tanda0_con_el_mismo_metodo']['p'])}, Wilson "
+         f"{iv(t['tanda0_con_el_mismo_metodo']['wilson'])} (mismo método) | sin umbral | `scripts/tasas_t4t3_tf.py`, {SAL}, `aceptadas.total` |")
@@ -56,2 +70,4 @@
-w.append(f"| atención de RI | {r['errores']} de {r['leidas']}; ponderada de RI {d(r['tasa_ponderada_RI'])}, Wilson {iv(r['wilson'])} (n ef. "
-         f"{d(r['n_efectivo_kish'], 3)}); sin las dudosas, {z['errores']} de {z['leidas']}, {d(z['tasa_ponderada_RI'])} | {LB['atencion_RI']['tanda1']} | bajo H0, "
+w.append(f"| atención de RI | con las 30 de no ítems, {r['errores']} de {r['leidas']}; ponderada de RI {d(r['tasa_ponderada_RI'])}, Wilson {iv(r['wilson'])} (n ef. "
+         f"{d(r['n_efectivo_kish'], 3)}); sin las dudosas, {z['errores']} de {z['leidas']}, {d(z['tasa_ponderada_RI'])}; con las 60 de no ítems (información), {I6['atencion_RI']['regla']['errores']} de "
+         f"{I6['atencion_RI']['regla']['leidas']}, {d(I6['atencion_RI']['regla']['tasa_ponderada_RI'])}, p {d(I6['atencion_RI']['regla']['p_valor'])} | "
+         f"{LB['atencion_RI']['tanda1']} | bajo H0, "
@@ -59 +75 @@
-         f"`scripts/tasas_t4t2_tf.py`, {SAL}, `atencion_RI` |")
+         f"`scripts/tasas_t4t3_tf.py`, {SAL}, `atencion_RI` |")
@@ -66 +82 @@
-         f"`scripts/tasas_t4t2_tf.py`, {SAL}, `cola` |")
+         f"`scripts/tasas_t4t3_tf.py`, {SAL}, `cola` |")
@@ -72 +88 @@
-         f"`scripts/tasas_t4t2_tf.py`, {SAL}, `observacion:12` |")
+         f"`scripts/tasas_t4t3_tf.py`, {SAL}, `observacion:12` |")
@@ -83 +99 @@
-             f"`scripts/tasas_t4t2_tf.py`, {SAL}, `vigilancias.{m}` |")
+             f"`scripts/tasas_t4t3_tf.py`, {SAL}, `vigilancias.{m}` |")
@@ -89,4 +105,7 @@
-if X["ampliacion"]["hay_ampliacion"]:
-    w.append("- **Lo que salta va a la ampliación:** " + ", ".join(k for k, v in X["ampliacion"]["salta"].items() if v) + ". Su fila de la "
-             "hoja queda con las 30 leídas: las tasas sobre las 60 (las 30 y las 30 de la ampliación) van en el tercer tramo, después de la "
-             "lectura de la autora.")
+w.append(f"- **Las aceptadas no ítems sobre las 60** (las 30 del primer tramo y las 30 de la ampliación; cada celda con el doble: "
+         f"{sn(all(B60['cada_celda_con_el_doble'].values()))}): freno por la atención sobre las 60, "
+         f"{sn(B60['regla']['freno_por_atencion_sobre_60'])}; freno por intervalos, {sn(B60['regla']['freno_por_intervalos'])}. Con las "
+         f"dudosas fuera, la sensibilidad da otra decisión: {sn(any(B60['la_sensibilidad_da_otra_decision'].values()))}. Su fila de la hoja es "
+         "la de las 60 (tablas 10 y 11).")
+w.append("- **La ponderada total y la atención de RI con las 60** van como información, sin decisión, al lado de las del segundo tramo "
+         "(tabla 12).")
@@ -94 +113,5 @@
-w.append(f"- **Los controles de la entrada** (`scripts/tasas_t4t2_tf.py`): {sum(X['controles'].values())} de {len(X['controles'])} pasan.")
+w.append(f"- **Los controles de la entrada** (`scripts/tasas_t4t3_tf.py`): {sum(X['controles'].values())} de {len(X['controles'])} pasan.")
+w.append(f"- **Lo del segundo tramo da lo mismo** (`lo_del_segundo_tramo`): "
+         f"{sum(X['lo_del_segundo_tramo']['bloques_iguales_a_tasas_t4_tramo2'].values())} de "
+         f"{len(X['lo_del_segundo_tramo']['bloques_iguales_a_tasas_t4_tramo2'])} bloques iguales a `tasas/tasas_t4_tramo2.json`; en las líneas "
+         f"de base cambian solo " + " y ".join(f"`{x}`" for x in X["lo_del_segundo_tramo"]["lineas_de_base_que_cambian"]) + ".")
@@ -116 +139 @@
-             f"(`tasas/distribuciones_bajo_H0_t4_tramo2.json`, `aceptadas:{s}:regla`).")
+             f"(`tasas/distribuciones_bajo_H0_t4_tramo3.json`, `aceptadas:{s}:regla`).")
@@ -175,0 +199,39 @@
+# 5. El tercer tramo: las aceptadas no ítems sobre las 60
+w += ["", "#### Tabla 10. Las aceptadas no ítems sobre las 60, por celda (`aceptadas_no_items_sobre_60`; pesos de `t3/muestras/umbrales_t4_tf.json`)",
+      "", "Cada celda: primer tramo + ampliación = las 60.", "",
+      "| celda | N | peso | leídas | con error | sin error | dudosa | el doble |", "|---|---:|---:|---|---|---|---|---|"]
+pt, pa, p6 = B60["por_celda_primer_tramo"], B60["por_celda_ampliacion"], B60["por_celda"]
+for c in CEL + [None]:
+    g = (lambda q, r: q[c][r]) if c else (lambda q, r: sum(q[x][r] for x in CEL))
+    cols = " | ".join(f"{g(pt, r)} + {g(pa, r)} = {g(p6, r)}" for r in ("n", "con error", "sin error", "dudosa"))
+    w.append(f"| {c or 'total'} | {mil(B60['N_por_celda'][c] if c else sum(B60['N_por_celda'].values()))} | "
+             f"{d(B60['pesos'][c]) if c else '1,0000'} | {cols} | {sn(B60['cada_celda_con_el_doble'][c]) if c else sn(all(B60['cada_celda_con_el_doble'].values()))} |")
+u6 = B60["umbral_del_freno_por_atencion_sobre_60"]
+w += ["", "#### Tabla 11. La tasa sobre las 60 y los dos frenos (`aceptadas_no_items_sobre_60.regla` y `.sensibilidad_sin_dudosas`)", "",
+      f"El umbral de `t3/muestras/umbrales_t4_tf.json` (`aceptadas.no_items.umbrales.freno_por_atencion_sobre_60`): {d(u6['umbral_tasa_ponderada'])}, "
+      f"p {d(u6['p_valor'])}. El superior del Wilson de la tanda 0: {d(B60['wilson_tanda0'][1])}.", "",
+      "| cuenta | errores | leídas | tasa ponderada | n ef. | Wilson | umbral recalculado (igual al del JSON) | p sobre las 60 | "
+      "freno por la atención sobre las 60 | freno por intervalos | freno |", "|---|---:|---:|---:|---:|---|---|---:|---|---|---|"]
+for nombre, et in (("regla", "regla (dudosa = error)"), ("sensibilidad_sin_dudosas", "sensibilidad (dudosas fuera)")):
+    r = B60[nombre]
+    w.append(f"| {et} | {r['errores']} | {r['leidas']} | {d(r['tasa_ponderada'])} | {d(r['n_efectivo_kish'], 3)} | {iv(r['wilson'])} | "
+             f"{d(r['umbral_recalculado'])} ({sn(r['umbral_recalculado_es_el_del_json'])}) | {d(r['p_valor_sobre_60'])} | "
+             f"{sn(r['freno_por_atencion_sobre_60'])} | {sn(r['freno_por_intervalos'])} | {sn(r['freno'])} |")
+w.append(f"\nEl umbral y el p-valor dicen lo mismo: {sn(B60['regla']['el_umbral_y_el_p_valor_dicen_lo_mismo'])}. La sensibilidad da otra "
+         f"decisión: {sn(any(B60['la_sensibilidad_da_otra_decision'].values()))}. La distribución bajo H0, con las n de la regla: "
+         f"{mil(B60['regla']['puntos_de_la_distribucion'])} valores, suma {d(B60['regla']['suma_de_la_distribucion'], 6)} "
+         f"(`tasas/distribuciones_bajo_H0_t4_tramo3.json`, `aceptadas:no_items:sobre_60:regla`).")
+w += ["", "#### Tabla 12. La ponderada total y la atención de RI: el segundo tramo y con las 60 de no ítems (`aceptadas.total`, `atencion_RI` "
+      "e `informacion_con_las_60`)", "",
+      "| cifra | no ítems con | cuenta | errores de leídas | tasa | n ef. | Wilson | p de la atención | decide |",
+      "|---|---|---|---|---:|---:|---|---:|---|"]
+for nombre, et in (("regla", "regla"), ("sensibilidad_sin_dudosas", "sensibilidad")):
+    t2, t6 = A["total"][nombre], I6["total"][nombre]
+    w.append(f"| ponderada total | 30 | {et} | — | {d(t2['tasa_ponderada'])} | {d(t2['n_efectivo_kish'], 3)} | {iv(t2['wilson'])} | — | sin umbral |")
+    w.append(f"| ponderada total | 60 | {et} | — | {d(t6['tasa_ponderada'])} | {d(t6['n_efectivo_kish'], 3)} | {iv(t6['wilson'])} | — | información |")
+for nombre, et in (("regla", "regla"), ("sensibilidad_sin_dudosas", "sensibilidad")):
+    r2, r6 = RI[nombre], I6["atencion_RI"][nombre]
+    w.append(f"| atención de RI | 30 | {et} | {r2['errores']} de {r2['leidas']} | {d(r2['tasa_ponderada_RI'])} | {d(r2['n_efectivo_kish'], 3)} | "
+             f"{iv(r2['wilson'])} | {d(r2['p_valor_atencion'])} | atención: {sn(r2['atencion'])} |")
+    w.append(f"| atención de RI | 60 | {et} | {r6['errores']} de {r6['leidas']} | {d(r6['tasa_ponderada_RI'])} | {d(r6['n_efectivo_kish'], 3)} | "
+             f"{iv(r6['wilson'])} | {d(r6['p_valor'])} | información |")
@@ -177 +239 @@
-(T4 / "tablas_t4_tramo2.md").write_text(texto, encoding="utf-8")
+(T4 / "tablas_t4_tramo3.md").write_text(texto, encoding="utf-8")
```

### `freno_t4t2_foto_tf.py` → `freno_t4t3_foto_tf.py` (32 líneas cambiadas)

```diff
--- tanda_final/t4/scripts/freno_t4t2_foto_tf.py
+++ tanda_final/t4/scripts/freno_t4t3_foto_tf.py
@@ -1,8 +1,8 @@
-"""B6.1, tanda final, T4, segundo tramo: la sección de la foto del FRENO, por script, desde la foto de las 12:16:33 (la del paso 0, que
-la autora fijó como punto de comparación) y la de después (t1/foto_repo_tanda_final_t1.py, crudas; las dos, en t4t2_fotos/, fuera del
-repo y del paquete), las dos listas de .pyc y la salida de las tasas. Solo lee; escribe <salida.md> (fuera del repo) y la imprime. Es
-tanda1/t4/scripts/freno_t4t2_foto.py con lo que admite el segundo tramo de la tanda final:
-  - lo nuevo, solo en tanda_final/t4/; t3/muestras/unidades_a_la_vista_T4.json, solo si hubo ampliación; los archivos que se llaman
-    exactamente .DS_Store van aparte, con su ruta (decisión de la autora sobre el FRENO del paso 0, punto 2); lo demás es «fuera de lo
-    admitido»;
-  - el primer tramo no escribió ningún NO_ABRIR_ en t4/: se controla que no haya ninguno en las dos fotos;
+"""B6.1, tanda final, T4, tercer tramo: la sección de la foto del FRENO, por script, desde la foto del paso 0 (t4t2_fotos/
+foto_repo_antes_T4t3.json) y la de después (t1/foto_repo_tanda_final_t1.py, crudas; las dos, en t4t2_fotos/, fuera del repo y del
+paquete), las dos listas de .pyc y la salida de las tasas. Solo lee; escribe <salida.md> (fuera del repo) y la imprime. Es
+t4/scripts/freno_t4t2_foto_tf.py con lo que admite el tercer tramo:
+  - lo nuevo, solo en tanda_final/t4/ (las tasas, las tablas, los scripts y el FRENO); nada de t3/, tampoco
+    t3/muestras/unidades_a_la_vista_T4.json; los archivos que se llaman exactamente .DS_Store van aparte, con su ruta; lo demás es
+    «fuera de lo admitido»;
+  - que no haya ningún NO_ABRIR_ en t4/ en las dos fotos;
@@ -10 +10 @@
-Uso: python3 -I -B freno_t4t2_foto_tf.py <foto_antes.json> <foto_despues.json> <pyc_antes.txt> <pyc_despues.txt> <tasas.json> <salida.md>
+Uso: python3 -I -B freno_t4t3_foto_tf.py <foto_antes.json> <foto_despues.json> <pyc_antes.txt> <pyc_despues.txt> <tasas.json> <salida.md>
@@ -22 +22 @@
-amp = json.loads(TASAS.read_text(encoding="utf-8"))["ampliacion"]["hay_ampliacion"]
+assert "aceptadas_no_items_sobre_60" in json.loads(TASAS.read_text(encoding="utf-8")), "no es la salida del tercer tramo"
@@ -25 +25 @@
-GRUPOS = ([(VISTA, "el archivo del punto 5 (ampliación)")] if amp else []) + [
+GRUPOS = [
@@ -43,2 +43,2 @@
-w = ["## 12. La foto del repo, los .pyc y el grep de convenciones", "",
-     "Lo genera `scripts/freno_t4t2_foto_tf.py` desde la foto de las 12:16:33 y la de después. Las dos quedan en `t4t2_fotos/`, en la "
+w = ["## 11. La foto del repo, los .pyc y el grep de convenciones", "",
+     "Lo genera `scripts/freno_t4t3_foto_tf.py` desde la foto del paso 0 (`foto_repo_antes_T4t3.json`) y la de después. Las dos quedan en `t4t2_fotos/`, en la "
@@ -47 +47 @@
-     f"- **La foto** (`t1/foto_repo_tanda_final_t1.py`). La de las 12:16:33: {fa['inicio'][11:]} a {fa['fin'][11:]} del "
+     f"- **La foto** (`t1/foto_repo_tanda_final_t1.py`). La del paso 0: {fa['inicio'][11:]} a {fa['fin'][11:]} del "
@@ -65,2 +65,2 @@
-w.append(f"  - **`unidades_a_la_vista_T4.json`** (`t3/muestras/`): " + ("con la ampliación cambia" if amp else "sin ampliación no se toca")
-         + f"; sha256 `{a[VISTA]['sha256']}` a las 12:16:33 y `{d[VISTA]['sha256']}` después; iguales: {a[VISTA] == d[VISTA]}.")
+w.append(f"  - **`unidades_a_la_vista_T4.json`** (`t3/muestras/`): este tramo no la toca; sha256 `{a[VISTA]['sha256']}` en el paso 0 "
+         f"y `{d[VISTA]['sha256']}` después; iguales: {a[VISTA] == d[VISTA]}.")
```

### `freno_t4t2_armar_tf.py` → `freno_t4t3_armar_tf.py` (588 líneas cambiadas)

```diff
--- tanda_final/t4/scripts/freno_t4t2_armar_tf.py
+++ tanda_final/t4/scripts/freno_t4t3_armar_tf.py
@@ -1,6 +1,6 @@
-"""B6.1, tanda final, T4, segundo tramo: arma el FRENO T4 (segundo tramo) desde los archivos del repo y del trabajo, por script: toda
-cifra del texto sale de un JSON o de una tabla generada; las tablas van tal cual; el texto fijo no lleva cifras propias. Es
-tanda1/t4/scripts/freno_t4t2_armar.py con las secciones de la tanda final, la ampliación y los diffs enteros de los cuatro scripts contra
-los de la tanda 1 (difflib, sin contexto). Solo lee; escribe data/experiment/tanda_final/t4/FRENO_T4_tramo2.md (frena si ya existe).
-Uso: python3 -I -B freno_t4t2_armar_tf.py <repo> <paquete del paso 0> <salida del paso 0 repetido> <seccion_foto.md> <grep.json>
-       <foto_contra_despues.json> <control_copia.json>
+"""B6.1, tanda final, T4, tercer tramo: arma el FRENO T4 (tercer tramo) desde los archivos del repo y del trabajo, por script: toda cifra
+del texto sale de un JSON o de una tabla generada; las tablas van tal cual; el texto fijo no lleva cifras propias. Es
+t4/scripts/freno_t4t2_armar_tf.py (segundo tramo) con las secciones del tercer tramo y los diffs enteros de los cinco scripts del tramo
+contra los del segundo (difflib, sin contexto). Solo lee; escribe data/experiment/tanda_final/t4/FRENO_T4_tramo3.md (frena si ya existe).
+Uso: python3 -I -B freno_t4t3_armar_tf.py <repo> <salida del paso 0> <foto_contra_commits.json> <seccion_foto.md> <grep.json>
+       <foto_contra_despues.json>
@@ -7,0 +8 @@
+import csv
@@ -12,0 +14 @@
+from collections import Counter
@@ -16 +18 @@
-R, PQ0, P0B, FOTO, GREP, FC, CC = (Path(x) for x in sys.argv[1:8])
+R, P0, FCC, FOTO, GREP, FC = (Path(x) for x in sys.argv[1:7])
@@ -20 +22 @@
-OUT = T4 / "FRENO_T4_tramo2.md"
+OUT = T4 / "FRENO_T4_tramo3.md"
@@ -25 +27,2 @@
-X = L(T4 / "tasas/tasas_t4_tramo2.json")
+X = L(T4 / "tasas/tasas_t4_tramo3.json")
+X2 = L(T4 / "tasas/tasas_t4_tramo2.json")
@@ -27,4 +30,4 @@
-POB4 = L(TF / "t3/muestras/poblaciones_t4t1_tf.json")["muestras"]
-VER = L(T4 / "tasas/verif_tasas_independiente_t4t2_tf.json")["_resumen"]
-grep, fc, cc = L(GREP), L(FC), L(CC)
-tablas = (T4 / "tablas_t4_tramo2.md").read_text(encoding="utf-8")
+VER = L(T4 / "tasas/verif_tasas_independiente_t4t3_tf.json")["_resumen"]
+CTRL_AMP = L(T4 / "ampliacion/control_lectura_mesa/salida_control_lectura_T4_ampliacion.json")
+grep, fc, fcc = L(GREP), L(FC), L(FCC)
+tablas = (T4 / "tablas_t4_tramo3.md").read_text(encoding="utf-8")
@@ -32,11 +35 @@
-assert sorted(partes) == list(range(1, 10)), sorted(partes)
-tamp = (T4 / "ampliacion/tablas_ampliacion_t4t2.md").read_text(encoding="utf-8")
-pamp = {m.group(1): m.group(0).rstrip() for m in re.finditer(r"#### Tabla (A\d)\..*?(?=\n#### Tabla |\Z)", tamp, re.S)}
-assert sorted(pamp) == [f"A{i}" for i in range(1, 6)], sorted(pamp)
-M = "aceptadas_no_items_ampliacion"
-LA = L(T4 / "ampliacion/lectura_asistida/lectura_asistida_t4_ampliacion.json")
-mu = L(T4 / "ampliacion/muestras" / f"{M}.json")
-idx = L(T4 / "ampliacion/muestras/sorteo_ampliacion_t4t2_tf.json")
-vista = L(TF / "t3/muestras/unidades_a_la_vista_T4.json")["ampliacion"]
-CONV = (T4 / "lectura_autora/convertir_lectura_T4.py").read_text(encoding="utf-8")
-LEEME = (T4 / "lectura_autora/LEEME_lectura_T4.md").read_text(encoding="utf-8")
+assert sorted(partes) == list(range(1, 13)), sorted(partes)
@@ -44,2 +36,0 @@
-ESTR = ["items", "no_items"]
-NOM = {"items": "ítems", "no_items": "no ítems"}
@@ -51,5 +42,6 @@
-A, RI, C, V, O, AMP = X["aceptadas"], X["atencion_RI"], X["cola"], X["vigilancias"], X["observacion:12"], X["ampliacion"]
-dud = {m: sum(b["por_celda"][c]["dudosa"] for c in CEL) for m, b in (("cola", C), ("items", A["items"]), ("no_items", A["no_items"]))}
-otra = [k for k, v in {**{f"aceptadas:{s}:{x}": A[s]["la_sensibilidad_da_otra_decision"][x] for s in ESTR for x in ("atencion", "freno_por_intervalos")},
-                       "atencion_RI": RI["la_sensibilidad_da_otra_decision"]["atencion"],
-                       "cola:regla_del_25": C["la_sensibilidad_da_otra_decision"]["regla_del_25"]}.items() if v]
+A, RI, B60, I6 = X["aceptadas"], X["atencion_RI"], X["aceptadas_no_items_sobre_60"], X["informacion_con_las_60"]
+r6, z6 = B60["regla"], B60["sensibilidad_sin_dudosas"]
+r3 = A["no_items"]["regla"]
+u6 = B60["umbral_del_freno_por_atencion_sobre_60"]
+dud = sum(B60["por_celda"][c]["dudosa"] for c in CEL)
+otra = [k for k, v in B60["la_sensibilidad_da_otra_decision"].items() if v]
@@ -57,44 +49,37 @@
-caps = "; ".join(f"{k}, {v['n']}" for k, v in O["incorrectas_por_capa_pipeline"].items())
-vg = lambda m, q: f"{V[m]['cruda']['k']} {q} de {V[m]['cruda']['n']}"  # noqa: E731
-salta = [k for k, v in AMP["salta"].items() if v]
-# lo que el texto afirma: la decisión por el p y por el umbral de T3 coinciden; salta solo la de no ítems; la ampliación es de ese estrato
-for s in ESTR:
-    r = A[s]["regla"]
-    assert (r["tasa_ponderada"] >= A[s]["umbrales_T3"]["atencion_desde"]) == r["atencion"] == (r["p_valor_atencion"] <= 0.05), s
-    assert (r["tasa_ponderada"] >= A[s]["umbrales_T3"]["freno_por_intervalos_desde"]) == r["freno_por_intervalos"], s
-assert (RI["regla"]["tasa_ponderada_RI"] >= RI["umbral_T3"]) == RI["regla"]["atencion"]
-assert salta == ["aceptadas:no_items"] and AMP["hay_ampliacion"], "el texto de las secciones 7 y 8 es el de la ampliación de no ítems"
-assert not any(A[s]["regla"]["freno_por_intervalos"] for s in ESTR), "el texto de la sección 7 dice que no hay freno"
-assert mu["estrato"] == "aceptadas:no_items" and mu["n"] == 30 and idx["sha256"] == sha(T4 / "ampliacion/muestras" / f"{M}.json")
-assert vista["unidades_a_la_vista_antes"] + vista["unidades_que_suma_la_ampliacion"] == vista["unidades_a_la_vista_despues"]
-assert C["regla"]["regla_del_25_se_dispara"] and C["sensibilidad_sin_dudosas"]["regla_del_25_se_dispara"], "el texto de la sección 4"
-assert fc["ok"] and not any(fc[k]["fuera_de_lo_admitido"] for k in ("nuevos", "borrados", "cambiados"))
-assert cc["nombres_vedados"] == 0 and cc["enlaces"] == 0
-m_conv = re.search(r"SHA_PLANILLAS = \{(.*?)\}", CONV, re.S)
-conv_muestras = re.findall(r'"([a-z_0-9]+)":', m_conv.group(1))
-assert M not in conv_muestras and len(conv_muestras) == 8, conv_muestras
-assert "ampliaci" not in LEEME.lower()
-
-# las horas de la autora, del sello
-sello = [x.split() for x in (T4 / "lectura_autora/sello_lectura_T4.txt").read_text(encoding="utf-8").splitlines() if x.strip()]
-NOMM = {"cola": "cola", "aceptadas_items": "aceptadas ítems", "aceptadas_no_items": "aceptadas no ítems", "vigilancia_2": "(2)",
-        "vigilancia_7": "(7)", "vigilancia_1": "(1)", "vigilancia_3": "(3)", "observacion_12": "(12)"}
-horas = {}
-for h, f, fecha, hora, tz in sorted(sello, key=lambda x: (x[2], x[3])):
-    horas.setdefault(fecha, []).append(f"{NOMM[f.removesuffix('_marcada.csv')]} {hora}")
-ultima = max((x[2], x[3]) for x in sello)
-
-# el paquete del paso 0: sus archivos, con el sha256 de su manifiesto
-man = {ln.split()[1]: ln.split()[0] for ln in (PQ0 / "manifest.txt").read_text(encoding="utf-8").splitlines() if ln.strip()}
-P0N = ["FRENO_T4_tramo2_paso0.md", "paso0_T4_tramo2_salida.txt", "paso0_t4_tramo2.sh", "control_sustituto_foto_t4_tramo2.py",
-       "control_sustituto_foto_T4_tramo2.json"]
-assert all(man[n] == sha(PQ0 / n) for n in P0N), "el paquete del paso 0 no da los sha256 de su manifiesto"
-cs = L(PQ0 / "control_sustituto_foto_T4_tramo2.json")
-ds0 = cs["C_cuenta"]["nacidos_despues_fuera_de_los_commits"] + cs["D_modificados_despues_fuera_de_los_commits"]
-assert all(Path(r).name == ".DS_Store" for r in ds0)
-p0b = P0B.read_text(encoding="utf-8").rstrip("\n")
-HEAD = re.search(r"^== git log -1.*\n([0-9a-f]{8}) ", p0b, re.M).group(1)
-
-# los diffs de los cuatro scripts contra los de la tanda 1
-PARES = [("tasas_t4t2.py", "tasas_t4t2_tf.py"), ("tablas_t4t2.py", "tablas_t4t2_tf.py"), ("freno_t4t2_foto.py", "freno_t4t2_foto_tf.py"),
-         ("freno_t4t2_armar.py", "freno_t4t2_armar_tf.py")]
+lo2 = X["lo_del_segundo_tramo"]
+# lo que el texto afirma
+assert all(B60["cada_celda_con_el_doble"].values()) and r6["cada_celda_con_el_doble"], "el texto dice que cada celda tiene el doble"
+assert r6["umbral_recalculado_es_el_del_json"] and r6["el_umbral_y_el_p_valor_dicen_lo_mismo"]
+assert r6["freno_por_atencion_sobre_60"] and not r6["freno_por_intervalos"] and r6["freno"], "el texto de las secciones 4 y 5"
+assert not otra and dud == 0, "el texto dice que no hay dudosas y que la sensibilidad decide lo mismo"
+assert all(lo2["bloques_iguales_a_tasas_t4_tramo2"].values()) and lo2["controles_del_segundo_tramo_iguales"]
+assert lo2["lineas_de_base_que_cambian"] == ["aceptadas:total.tanda0", "atencion_RI.tanda0"]
+assert fc["ok"] and not any(fc[k]["fuera_de_lo_admitido"] for k in ("nuevos", "borrados", "cambiados")) and fcc["ok"]
+assert VER["iguales"] == VER["cifras"] and not VER["distintas"]
+ri_igual = all(F_ == G_ for F_, G_ in ((B60["regla"]["k_por_celda"][c] * A["no_items"]["regla"]["n_por_celda"][c],
+                                         A["no_items"]["regla"]["k_por_celda"][c] * B60["regla"]["n_por_celda"][c]) for c in ("RI:sin_raiz", "RI:resto")))
+mesa_ok = [k for k, v in CTRL_AMP.items() if isinstance(v, dict) and "pasa" in v]
+p0txt = P0.read_text(encoding="utf-8").rstrip("\n")
+HEAD = re.search(r"^== git log -3.*\n([0-9a-f]{8}) ", p0txt, re.M).group(1)
+# las horas de la autora, de los dos sellos
+sellos = {}
+for p in (T4 / "lectura_autora/sello_lectura_T4.txt", T4 / "ampliacion/lectura_autora/sello_lectura_T4_ampliacion.txt"):
+    for ln in p.read_text(encoding="utf-8").splitlines():
+        if ln.strip():
+            h, f, fecha, hora, tz = ln.split()
+            sellos[f] = (fecha, hora)
+h30, h60 = sellos["aceptadas_no_items_marcada.csv"], sellos["aceptadas_no_items_ampliacion_marcada.csv"]
+# mis propuestas de la ampliación contra la lectura de la autora (información)
+with open(T4 / "ampliacion/lectura_autora/aceptadas_no_items_ampliacion_marcada.csv", encoding="utf-8", newline="") as fh:
+    marc = list(csv.DictReader(fh, delimiter=";"))
+cambios = [(i, x["propuesta"], x["veredicto_autora"]) for i, x in enumerate(marc, 1) if x["propuesta"] != x["veredicto_autora"]]
+cprop, caut = Counter(x["propuesta"] for x in marc), Counter(x["veredicto_autora"] for x in marc)
+# los .DS_Store del paso 0 y lo que trajeron los commits
+n_cambios = fcc["nuevos"] + fcc["cambiados"] + fcc["borrados"]
+de_commits = n_cambios - len(fcc["DS_Store"])
+assert de_commits == fcc["rutas_en_los_commits"] - fcc["rutas_de_los_commits_ya_iguales_en_disco"]
+
+# los diffs de los cinco scripts contra los del segundo tramo
+PARES = [("tasas_t4t2_tf.py", "tasas_t4t3_tf.py"), ("verif_tasas_independiente_t4t2_tf.py", "verif_tasas_independiente_t4t3_tf.py"),
+         ("tablas_t4t2_tf.py", "tablas_t4t3_tf.py"), ("freno_t4t2_foto_tf.py", "freno_t4t3_foto_tf.py"),
+         ("freno_t4t2_armar_tf.py", "freno_t4t3_armar_tf.py")]
@@ -103 +88 @@
-    ta = (R / "data/experiment/tanda1/t4/scripts" / a).read_text(encoding="utf-8").splitlines()
+    ta = (T4 / "scripts" / a).read_text(encoding="utf-8").splitlines()
@@ -105,4 +90,4 @@
-    dl = list(difflib.unified_diff(ta, tb, f"tanda1/t4/scripts/{a}", f"tanda_final/t4/scripts/{b}", n=0, lineterm=""))
-    diffs.append((a, b, dl))
-
-w = ["# FRENO T4 — tanda final de B6.1, segundo tramo: las tasas, la atención y la ampliación (USD 0, sin API, sin commit)", "",
+    diffs.append((a, b, list(difflib.unified_diff(ta, tb, f"tanda_final/t4/scripts/{a}", f"tanda_final/t4/scripts/{b}", n=0, lineterm=""))))
+
+w = ["# FRENO T4 — tanda final de B6.1, tercer tramo: las aceptadas no ítems sobre las 60 y el freno por la atención sobre las 60 "
+     "(USD 0, sin API, sin commit)", "",
@@ -110,27 +95,26 @@
-     f"para la lectura de T4 (`tanda_final/preregistro/preregistro_tanda_final_derivada_T4.md`, sha256 "
-     f"`{X['entradas']['preregistro_tanda_final_derivada_T4.md']}`), el «seguí» del segundo tramo, la regla de las dudosas (registro de",
-     "decisiones, §35) y lo que decidió la autora sobre el FRENO del paso 0. La lectura es la de la autora, sellada en",
-     f"`t4/lectura_autora/sello_lectura_T4.txt` y controlada por la mesa (`t4/control_lectura_mesa/`). HEAD `{HEAD}`.", "",
-     "**Resultado:**"]
-for s in ESTR:
-    r = A[s]["regla"]
-    w.append(f"- **Las aceptadas, {NOM[s]}** (sección 3): {r['errores']} de {r['leidas']} con error, contando las dudosas; tasa ponderada "
-             f"{d(r['tasa_ponderada'])}, Wilson {iv(r['wilson'])}. Atención: {sn(r['atencion'])} (p {d(r['p_valor_atencion'])}). Freno: "
-             f"{sn(r['freno_por_intervalos'])}.")
-w += [f"- **La atención de RI** (sección 3): {RI['regla']['errores']} de {RI['regla']['leidas']}; tasa ponderada de RI "
-      f"{d(RI['regla']['tasa_ponderada_RI'])}, p {d(RI['regla']['p_valor_atencion'])}: no salta.",
-      f"- **La ampliación** (secciones 7 y 8): sí, por la atención de las aceptadas no ítems. Sorteé {mu['n']} unidades más de las que "
-      "no se leyeron, armé su material, la lectura asistida y la planilla en blanco de la autora, y sumé sus unidades a "
-      f"`t3/muestras/unidades_a_la_vista_T4.json`, que pasa a sha256 `{sha(TF / 't3/muestras/unidades_a_la_vista_T4.json')}`. Las tasas "
-      "sobre las 60 van en el tercer tramo, después de la lectura de la autora.",
-      f"- **La cola** (sección 4): {C['regla']['errores']} de {C['regla']['leidas']} con error; tasa ponderada {d(C['regla']['tasa_ponderada'])}, "
-      f"Wilson {iv(C['regla']['wilson'])}. La regla del 25 % se dispara: es cifra y vigilancia, no freno.",
-      f"- **La observación (12)** (sección 6): {O['cruda']['correctas']} correctas de {O['cruda']['de']}, Wilson {iv(O['cruda']['wilson'])}; "
-      f"incorrectas por `capa_pipeline`: {caps}.",
-      f"- **Las vigilancias** (sección 5): (1), {vg('vigilancia:1', 'sí')}; (2), {vg('vigilancia:2', 'vaciamientos')}; (3), "
-      f"{vg('vigilancia:3', 'duplicaciones')}; (7), {vg('vigilancia:7', 'sin apoyo')}, leída entera.",
-      f"- **La regla de las dudosas** (sección 2): hay {dud['cola'] + dud['items'] + dud['no_items']} dudosas en la cola y las aceptadas, así "
-      f"que la sensibilidad da otra decisión en {len(otra)} de las seis (atención y freno de cada estrato, atención de RI y regla del 25 % "
-      "de la cola).",
-      "- Toda cifra sale por script de sus archivos. Las tablas que copio de una salida van tal cual; mis aclaraciones van fuera de las tablas.",
-      "- Nada commiteado y ningún mensaje de commit preparado: los commits son de la autora y quedan PENDIENTES.", ""]
+     f"para la lectura de T4 (sha256 `{X['entradas']['preregistro_tanda_final_derivada_T4.md']}`), la regla del freno del script de la mesa y "
+     "del pre-registro de la tanda 1 (§5.4, `95b18217:592-593`), el umbral de `t3/muestras/umbrales_t4_tf.json`, la regla de las dudosas "
+     "(registro de decisiones, §35), lo que decidió la autora sobre el FRENO del segundo tramo (registro, §85) y el «seguí» del tercer tramo.",
+     f"Las lecturas son las de la autora: las 30 del primer tramo, selladas el {h30[0]} a las {h30[1]}, y las 30 de la ampliación, selladas "
+     f"el {h60[0]} a las {h60[1]} y controladas por la mesa ({sum(CTRL_AMP[k]['pasa'] for k in mesa_ok)} de {len(mesa_ok)}). HEAD `{HEAD}`.",
+     "", "**Resultado:**",
+     f"- **Las aceptadas no ítems sobre las 60** (sección 4): {r6['errores']} de {r6['leidas']} con error, contando las dudosas; tasa "
+     f"ponderada {d(r6['tasa_ponderada'])}, Wilson {iv(r6['wilson'])} (n efectivo {d(r6['n_efectivo_kish'], 3)}). Sobre las 30 del primer "
+     f"tramo era {d(r3['tasa_ponderada'])}.",
+     f"- **El freno por la atención sobre las 60: sí.** La tasa ({d(r6['tasa_ponderada'])}) pasa el umbral ({d(r6['umbral_recalculado'])}); "
+     f"el p-valor sobre las 60 es {d(r6['p_valor_sobre_60'])}. La ampliación dejó cada celda con el doble de unidades, así que la regla "
+     "se aplica tal cual.",
+     f"- **El freno por intervalos: no.** El límite inferior del Wilson ({d(r6['wilson'][0])}) no pasa el superior del Wilson de la tanda 0 "
+     f"({d(B60['wilson_tanda0'][1])}).",
+     "- **Hay freno de T4 por las aceptadas no ítems** (sección 5): la regla da freno si se cumple cualquiera de los dos, y se cumple el "
+     "de la atención sobre las 60. Qué sigue no es de esta unidad.",
+     f"- **Las dudosas:** {dud}, así que la sensibilidad da la misma decisión.",
+     f"- **La ponderada total y la atención de RI con las 60** (sección 6, información): {d(I6['total']['regla']['tasa_ponderada'])} y "
+     f"{d(I6['atencion_RI']['regla']['tasa_ponderada_RI'])} (p {d(I6['atencion_RI']['regla']['p_valor'])}); en el segundo tramo, "
+     f"{d(A['total']['regla']['tasa_ponderada'])} y {d(RI['regla']['tasa_ponderada_RI'])}.",
+     f"- **Lo del segundo tramo** (sección 7), rehecho: {sum(lo2['bloques_iguales_a_tasas_t4_tramo2'].values())} de "
+     f"{len(lo2['bloques_iguales_a_tasas_t4_tramo2'])} bloques iguales. En las líneas de base cambian solo los dos textos con el nombre "
+     "del archivo, ya sin la coma.",
+     f"- **La verificación independiente:** {VER['iguales']} de {VER['cifras']} cifras iguales.",
+     "- Toda cifra sale por script de sus archivos. Las tablas que copio de una salida van tal cual; mis aclaraciones van fuera de las tablas.",
+     "- Nada commiteado y ningún mensaje de commit preparado: los commits son de la autora y quedan PENDIENTES.", ""]
@@ -140,40 +124,33 @@
-      "- **El primer paso 0 frenó** (12:16). La foto de después del primer tramo, que era su punto de comparación, había quedado solo en "
-      "`/private/tmp` y se perdió, y había cambios fuera de los commits: "
-      f"{len(ds0)} archivos `.DS_Store`. Ese FRENO, su salida y su control sustituto están en el paquete "
-      f"`revision_tanda_final_FRENO_T4_tramo2_paso0/` (manifiesto con sha256 `{sha(PQ0 / 'manifest.txt')}`), en la carpeta permanente "
-      "de esta sesión, con estos nombres:",
-      "  - `FRENO_T4_tramo2_paso0.md`: el FRENO, con el error propio en su sección 5;",
-      "  - `paso0_T4_tramo2_salida.txt`, de `paso0_t4_tramo2.sh`: la salida del paso 0;",
-      "  - `control_sustituto_foto_t4_tramo2.py` y su salida, `control_sustituto_foto_T4_tramo2.json`: el control sustituto (A a H).",
-      "- **Lo que decidió la autora sobre ese FRENO:**",
-      "  1. el control sustituto vale como la foto de ese paso 0. Lo que no cubre: el contenido de los no rastreados o ignorados que no "
-      "cambiaron de fecha (los cubre por la fecha y la cuenta, no por su sha256, salvo los seis `kg.json`);",
-      "  2. los archivos que se llaman exactamente `.DS_Store` son ruido de Finder y quedan fuera de lo que cuenta; se listan con su ruta. "
-      "Cualquier otro cambio fuera de lo admitido cuenta, y freno;",
-      "  3. el paso 0 se repite antes de las tasas, contra la foto de las 12:16:33 guardada en `t4t2_fotos/`;",
-      "  4. la foto de después se compara archivo por archivo con la de las 12:16:33 y se guarda también en `t4t2_fotos/`;",
-      "  5. este FRENO cita el paquete del paso 0 y el error propio con los nombres del paquete (sección 14, punto 1).",
-      f"- **Los `.DS_Store` del primer paso 0** (sin abrirlos): " + ", ".join(f"`{r}`" for r in sorted(ds0)) + ".",
-      "- **El paso 0 repetido**, antes de las tasas. La salida, con la carpeta personal reemplazada por `$HOME` y la carpeta de trabajo por "
-      "`<DIR DE TRABAJO>` (`paso0_bis_T4_tramo2_salida.txt`, de `paso0_bis_t4_tramo2.sh`, y la comparación de `foto_contra_t4_tramo2.py`, "
-      "en el paquete):", "", "```", p0b, "```", "",
-      "- **Las horas de la autora, del sello** (`t4/lectura_autora/sello_lectura_T4.txt`): " + "; ".join(
-          f"{f[8:10]}/{f[5:7]}: " + ", ".join(v) for f, v in horas.items()) + f". La última marcada es de las {ultima[1]} del {ultima[0]}, "
-      "antes del primer paso 0.", ""]
-
-# 2. Las dudosas
-w += ["## 2. La regla de las dudosas y cómo la apliqué", "",
-      "- **La regla** (pre-registro de la tanda final, §6; registro de decisiones, §35):",
-      "  - en la cola y en las dos de las aceptadas, una unidad «dudosa» cuenta como error para la tasa, la atención y el freno;",
-      "  - la misma cuenta con las dudosas fuera, sobre las decididas, va al lado como sensibilidad y no decide nada;",
-      "  - si la sensibilidad diera otra decisión de atención o de freno, se declara, y rige la primera.",
-      "- **Cómo la apliqué** (`scripts/tasas_t4t2_tf.py`): en cada celda, la regla cuenta k = «con error» + «dudosa» sobre las n leídas; la "
-      "sensibilidad cuenta k = «con error» sobre n − «dudosa». Los pesos de las celdas son los mismos en las dos.",
-      f"- **Las dudosas:** {dud['cola']} en la cola, {dud['items']} en ítems y {dud['no_items']} en no ítems (tablas 2 y 6).",
-      (f"- **Lo que da la sensibilidad:** otra decisión en {len(otra)}. No hay nada que declarar por el tercer punto de la regla." if not otra
-       else f"- **Lo que da la sensibilidad:** otra decisión en {', '.join(otra)}; rige la primera."), ""]
-
-# 3. Las aceptadas
-r_no = A["no_items"]["regla"]
-w += ["## 3. Las aceptadas", "",
-      partes[2], "", partes[3], "", partes[4], "", partes[5], "",
+      "La salida, con la carpeta personal reemplazada por `$HOME` y la carpeta de trabajo por `<DIR DE TRABAJO>` (`paso0_T4_tramo3_salida.txt`, "
+      "de `paso0_t4_tramo3.sh`, con la comparación de `paso0_foto_contra_commits_t4_tramo3.py`, en el paquete):", "", "```", p0txt, "```", "",
+      f"- **La foto nueva** (`t4t2_fotos/foto_repo_antes_T4t3.json`, sha256 `{fcc['foto_nueva']['sha256']}`) contra la final del segundo "
+      f"tramo (`foto_repo_final_T4t2.json`): {fcc['nuevos']} nuevos, {fcc['cambiados']} cambiados y {fcc['borrados']} borrados. "
+      f"{len(fcc['DS_Store'])} son `.DS_Store`, ruido de Finder que queda fuera de lo que cuenta (decisión de la autora sobre el FRENO del "
+      f"paso 0 del segundo tramo); los otros {de_commits} son rutas de los commits `{fcc['commits']}`. De las {fcc['rutas_en_los_commits']} rutas "
+      f"de esos commits, {fcc['rutas_de_los_commits_ya_iguales_en_disco']} ya estaban iguales en disco: son las del segundo tramo, que el "
+      "TF4b commiteó sin cambios. Todas dan el sha256 de su blob en HEAD.",
+      "- **Los `.DS_Store`** (sin abrirlos): " + ", ".join(f"`{r}`" for r in fcc["DS_Store"]) + ".",
+      f"- **Las horas de la autora, de los sellos:** las 30 del primer tramo, {h30[0]} {h30[1]} (`t4/lectura_autora/sello_lectura_T4.txt`); "
+      f"las 30 de la ampliación, {h60[0]} {h60[1]} (`t4/ampliacion/lectura_autora/sello_lectura_T4_ampliacion.txt`).", ""]
+
+# 2. Lo decidido
+w += ["## 2. Lo que decidió la autora sobre el FRENO del segundo tramo (registro de decisiones, §85)", "",
+      "1. La exclusión de `data/experiment/neo4j/volumen` en la copia del repo: aceptada y declarada.",
+      "2. El texto «umbrales_t4_tf,json» de `tasas_t4_tramo2.json` se corrige cuando se rehacen las tasas: lo corrige este tramo (sección 7).",
+      "3. Que la unidad haya abierto `tanda1/t3/scripts/celdas_t4_t3f.py` y calculado el sha256 de dos `kg.json` de `tanda1/t3/acumulado/` "
+      "contra su sello: aceptado y declarado.",
+      "4. Para sellar la lectura de la ampliación, la mesa armó `t4/ampliacion/lectura_autora/convertir_lectura_T4_ampliacion.py` y "
+      "`LEEME_lectura_T4_ampliacion.md`, que entraron con el commit del segundo tramo. No los toqué.", ""]
+
+# 3. La regla
+w += ["## 3. La regla", "",
+      "- **El freno** (script de la mesa, `data/experiment/controles_tanda1/umbrales_t4_por_celdas_mesa.py`, docstring, «Freno»; pre-registro "
+      "de la tanda 1, `95b18217:592-593`): hay freno si el intervalo de la tasa no se solapa con el Wilson de la tanda 0, «o si la atención "
+      "se confirma sobre las 60 (cada celda con el doble de unidades)».",
+      f"- **El umbral:** `freno_por_atencion_sobre_60` de `aceptadas.no_items` en `t3/muestras/umbrales_t4_tf.json` (sha256 "
+      f"`{X['entradas']['umbrales_t4_tf.json']}`), con los pesos reales: {d(u6['umbral_tasa_ponderada'])}, p {d(u6['p_valor'])}.",
+      "- **Las dudosas** (pre-registro, §6; registro, §35): cuentan como error para la tasa, la atención y el freno; la cuenta sin ellas va al "
+      "lado como sensibilidad y no decide nada.", ""]
+
+# 4. Las 60
+w += ["## 4. Las aceptadas no ítems sobre las 60", "", partes[10], "", partes[11], "",
@@ -181,18 +158,24 @@
-      "- **Los pesos** son los de `t3/muestras/umbrales_t4_tf.json`, que T3 calculó con las unidades de cada celda antes de leer. "
-      "`tasas_t4t2_tf.py` controla que sean los de `t3/muestras/poblaciones_t4_t3f_tf.json` y que las n de cada celda sean las de la muestra.",
-      "- **La atención** es el test exacto unilateral al 5 % contra la tanda 0, con la distribución de la tasa enumerada entera por la "
-      "función `distribucion` del script de la mesa, importado sin cambiarlo. Su salida al importarse es byte a byte su JSON "
-      f"({sn(ctrl['el script de la mesa, importado, da su JSON byte a byte'])}). Las distribuciones van en "
-      "`tasas/distribuciones_bajo_H0_t4_tramo2.json`.",
-      "- **Los umbrales de T3** van en la tabla 3 como información. La decisión sale del p-valor, y las dos dicen lo mismo en cada estrato: "
-      f"en ítems, la tasa ({d(A['items']['regla']['tasa_ponderada'])}) está debajo del umbral de la atención "
-      f"({d(A['items']['umbrales_T3']['atencion_desde'])}) y el p pasa de 0,05; en no ítems, la tasa ({d(r_no['tasa_ponderada'])}) pasa el "
-      f"umbral ({d(A['no_items']['umbrales_T3']['atencion_desde'])}) y el p ({d(r_no['p_valor_atencion'])}) no pasa de 0,05.",
-      "- **El freno** es el de los intervalos: el límite inferior del Wilson de la tasa contra el superior del Wilson de la tanda 0, la misma "
-      "comparación que hace `umbrales` en el script de la mesa. No salta en ningún estrato. La tasa de no ítems sobre las 60 y su freno van "
-      "en el tercer tramo.",
-      f"- **NG `sin_raiz`** (tabla 5): son {mil(sum(X['NG_sin_raiz'][s]['N'] for s in ESTR))} unidades aceptadas. Van con su cifra por celda "
-      "y sin umbral, como en la tanda 1 (pre-registro de la tanda 1, `95b18217:619`).", ""]
-
-# 4. La cola
-w += ["## 4. La cola", "", partes[6], "",
+      "- **Los pesos** son los del segundo tramo (`umbrales_t4_tf.json`). Las 60 son las 30 de `t4/lectura_autora/aceptadas_no_items_marcada.csv` "
+      "y las 30 de `t4/ampliacion/lectura_autora/aceptadas_no_items_ampliacion_marcada.csv`, cada una contra su sello; `tasas_t4t3_tf.py` "
+      "controla además que las de la ampliación sean las de su muestra y que ninguna esté entre las 30 del primer tramo.",
+      "- **El doble por celda:** la ampliación salió con las mismas cuotas por celda que la primera muestra, así que cada celda tiene el doble (tabla 10). "
+      "No hizo falta aplicar la regla con otras n.",
+      "- **El umbral:** con el doble, la distribución bajo H0 de la tasa sobre las 60 es la misma con la que la mesa calculó el umbral (los "
+      "mismos pesos, las mismas n y la tasa de la tanda 0). `tasas_t4t3_tf.py` la enumera entera con `distribucion` de la mesa, recalcula el "
+      "umbral (la menor tasa con P(T' ≥ t) ≤ 0,05) y controla que, redondeado, sea el del JSON. Decide con el umbral exacto, y el p-valor "
+      "va al lado: los dos dicen lo mismo.",
+      "- **El freno por intervalos** usa el Wilson con el n efectivo de Kish de las 60 y el superior del Wilson de la tanda 0 de no ítems, "
+      "como en el segundo tramo.", ""]
+
+# 5. La decisión
+w += ["## 5. Los dos frenos y la decisión", "",
+      f"- **Freno por la atención sobre las 60:** {sn(r6['freno_por_atencion_sobre_60'])} (tasa {d(r6['tasa_ponderada'])}, umbral "
+      f"{d(r6['umbral_recalculado'])}, p {d(r6['p_valor_sobre_60'])}).",
+      f"- **Freno por intervalos:** {sn(r6['freno_por_intervalos'])} (inferior {d(r6['wilson'][0])}, superior de la tanda 0 "
+      f"{d(B60['wilson_tanda0'][1])}).",
+      f"- **Freno de T4 por las aceptadas no ítems:** {sn(r6['freno'])}. Con las dudosas fuera, lo mismo.",
+      "- **Lo que no decido:** qué sigue después del freno. Las líneas de la regla (`95b18217:592-593`) fijan cuándo hay freno; lo que "
+      "sigue es de la mesa y la autora (sección 10).", ""]
+
+# 6. Total y RI
+w += ["## 6. La ponderada total y la atención de RI con las 60 (información)", "", partes[12], "",
@@ -200,114 +183,44 @@
-      "- **La ponderada** usa los pesos de la cola de `umbrales_t4_tf.json`, con el n efectivo de Kish.",
-      "- **La regla del 25 %** se dispara con la regla de las dudosas y también sin ellas. Es cifra y vigilancia, no freno, como en la tanda 1 "
-      "(pre-registro de la tanda 1, `95b18217:641`). Qué se hace con ella en la tanda final queda para la mesa y la autora (sección 11).", ""]
-
-# 5. Las vigilancias
-w += ["## 5. Las vigilancias (1), (2), (3) y (7)", "", partes[7], "", partes[8], "",
-      "Mis aclaraciones:",
-      "- **La ponderación:** las cuatro muestras salieron por celdas, y van la cruda (k sobre las leídas, con el Wilson de esa n) y la "
-      "ponderada por celda (con el Wilson del n efectivo de Kish), las dos, como en la tanda 1.",
-      f"- **Las no decidibles:** en la (1) quedan fuera de la tasa, con su cuenta (registro de decisiones, §29), y son "
-      f"{V['vigilancia:1']['fuera_de_la_tasa']['no decidible']}. En la (2) y en la (7) no hay ninguna: "
-      f"{V['vigilancia:2']['por_respuesta']['no decidible']} y {V['vigilancia:7']['por_respuesta']['no decidible']}.",
-      f"- **Los pesos:** los de la (1) y la (3) son los de `t3/muestras/poblaciones_t4t1_tf.json` ({mil(POB4['vigilancia:1']['N'])} nodos "
-      f"Condicion y {mil(POB4['vigilancia:3']['N'])} grupos). Los de la (2), los de la extracción final de `umbrales_t4_tf.json` "
-      f"({mil(U['otras']['vigilancia:2']['N'])} unidades).",
-      "- **La (3)** lleva su declaración debajo de la tabla 8. El criterio de su lectura para el par deber y acto regulado es el de la §31 "
-      "del registro de decisiones, fijado antes de leer.",
-      f"- **La (7)** se leyó entera ({V['vigilancia:7']['leidas']} aristas, sin celdas). Su Wilson es el de la cruda con esa n.", ""]
-
-# 6. La (12)
-w += ["## 6. La observación (12)", "", partes[9], "",
-      "Mis aclaraciones:",
-      "- **La cuenta** es la de la enmienda de la observación 12 (`docs/enmienda_preregistro_tanda0_2026-09-27_observacion12.md:107-111`): "
-      "correctas sobre 30, con las no decidibles aparte y en el denominador, y el Wilson sobre correctas / 30. La ponderada por celda va al "
-      "lado porque la muestra salió por celdas.",
-      f"- **Los pesos** son los del universo de la decisión 1.2 ({mil(POB4['observacion:12']['N'])} aristas, "
-      "`t3/muestras/poblaciones_t4t1_tf.json`), los mismos que trae `otras.observacion:12` de `umbrales_t4_tf.json` "
-      f"({mil(U['otras']['observacion:12']['N'])} aristas).", ""]
-
-# 7. Atención, freno y ampliación
-w += ["## 7. La atención, el freno y la ampliación", "",
-      f"- **La atención:** ítems, {sn(AMP['salta']['aceptadas:items'])} (p {d(A['items']['regla']['p_valor_atencion'])}); no ítems, "
-      f"{sn(AMP['salta']['aceptadas:no_items'])} (p {d(r_no['p_valor_atencion'])}); RI, {sn(AMP['salta']['RI'])} "
-      f"(p {d(RI['regla']['p_valor_atencion'])}). Con las dudosas fuera, lo mismo: "
-      + ", ".join(f"{k} {sn(v)}" for k, v in AMP["con_la_sensibilidad"].items()) + ".",
-      f"- **El freno:** ítems, {sn(A['items']['regla']['freno_por_intervalos'])}; no ítems, {sn(r_no['freno_por_intervalos'])}.",
-      "- **La ampliación: sí,** de las aceptadas no ítems (sección 8). La atención de ítems y la de RI no saltan, así que no se sortea nada "
-      "de ítems.", ""]
-
-# 8. La ampliación
-la_h = LA["hora_de_la_lectura"][M]
-w += ["## 8. La ampliación de las aceptadas no ítems", "",
-      "Las tablas A1 a A5 son las de `t4/ampliacion/tablas_ampliacion_t4t2.md`, de `scripts/tablas_ampliacion_t4t2_tf.py` (rutas relativas a "
-      "`t4/`). Las copio tal cual.", "",
-      "- **El sorteo** (`scripts/sorteo_ampliacion_t4t2_tf.py`): sobre las unidades del estrato que no se leyeron, con las cuotas y las reglas "
-      "de celda de la tanda 1 (`celdas_t4_t3f.asignar`, sin cambios) y la cadena `tandafinal:{muestra}:{celda}:ampliacion:{base}` "
-      "(«seguí», punto 5; pre-registro, §6: «las ampliaciones con `:ampliacion:`»). La base es el sha256 de la versión para firmar del "
-      "pre-registro (`5289b02f`), como en T3; el script controla que el texto firmado (`4de7f2a7`) traiga la base, la plantilla y "
-      "«`:ampliacion:`», y que la salida de las tasas diga que salta solo la atención de no ítems.", "",
-      pamp["A1"], "", pamp["A2"], "",
-      "- **El material** (`scripts/material_ampliacion_t4t2_tf.py`, que es `t3/scripts/material_t4_t3f_tf.py` con la muestra de la "
-      "ampliación): corrió sobre la copia del repo (sección 12), sin `ANTHROPIC_API_KEY`, y lo copié a `t4/ampliacion/material/` con su "
-      "consola; los sha256 del repo son los de la copia. El control (`scripts/control_material_ampliacion_t4t2_tf.py`, el de T3 con el "
-      "índice de la ampliación) da 0 claves vedadas.",
-      "- **La lectura asistida** (`scripts/anotar_ampliacion_t4t2.py` y `scripts/armar_lectura_ampliacion_t4t2.py`): como en el primer "
-      f"tramo, con los mismos criterios (`criterios_de_la_propuesta`; solo cambia la nota de las dudosas, que remite al tercer tramo). La "
-      f"leí yo ({LA['modelo']['nombre']}, `{LA['modelo']['id']}`), sin API; las propuestas se escribieron de "
-      f"{la_h['primera_propuesta'][11:19]} a {la_h['ultima_escritura'][11:19]} del {la_h['primera_propuesta'][:10]}. El borrador "
-      "se escribió en el repo (`t4/ampliacion/lectura_asistida/borradores/`) y de ahí salen la lectura asistida, las omisiones y "
-      "observaciones y la planilla de la autora.",
-      f"- **La planilla de la autora:** `t4/ampliacion/lectura_autora/{M}.csv`, con las columnas de las del primer tramo (`id`, `celda`, "
-      "`ficha`, `propuesta`, `justificacion`, `veredicto_autora` y `nota_autora`, las dos últimas vacías) y la ruta de cada ficha en "
-      f"`t4/ampliacion/material/{M}/fichas_{M}.md`.",
-      "- **La lista de unidades a la vista** (`scripts/unidades_a_la_vista_ampliacion_t4t2_tf.py`, con la regla de T3, copiada): corrió sobre "
-      "la copia, controló que las ocho muestras de T3 den lo mismo que en la lista vigente y la reemplacé en el repo después de controlar que "
-      "la vigente era la de HEAD. Es antes de cualquier sorteo de las FICHAS: no hubo ninguno.", "",
-      pamp["A3"], "", pamp["A4"], "", pamp["A5"], "",
-      "- **Lo que sigue (tercer tramo):** la autora lee la planilla; con su lectura sellada, las tasas sobre las 60 (las 30 leídas y las 30 "
-      "de la ampliación), la atención y el freno. Lo que hace falta antes está en la sección 11, puntos 1 y 2.", ""]
-
-# 9. Para la hoja
-w += ["## 9. Las cifras para la hoja de la revisión entre tandas", "",
-      "Van en `t4/tablas_t4_tramo2.md` (tabla 1), que genera `scripts/tablas_t4t2_tf.py` desde la salida de las tasas. La copio tal cual:", "",
-      partes[1], ""]
-
-# 10. Cegamiento
-w += ["## 10. El cegamiento", "",
-      "- **Ninguna cifra de este tramo usa el estado de E3, `n_reintentos`, `reintentos_e3.jsonl`, `copias_nota_e3.jsonl`, las `marcas_e3` "
-      "ni el gasto de los reintentos.** `tasas_t4t2_tf.py` lee solo las marcadas y su sello, las muestras, las poblaciones, los umbrales, la "
-      "versión derivada y el script de la mesa. El material de la ampliación no trae el estado ni las marcas de E3 (tabla A3: 0 claves "
-      "vedadas). No miré ningún desglose por estado de E3.",
-      "- **Por eso no escribí `t4/NO_ABRIR_conteos_t4_tramo2.json`:** no hay nada que lo use. La foto da 0 `NO_ABRIR_` en `t4/` (sección 12).",
-      "- **De la tanda 1** abrí sus cuatro scripts del segundo tramo (`tasas_t4t2.py`, `tablas_t4t2.py`, `freno_t4t2_foto.py` y "
-      "`freno_t4t2_armar.py`) y listé los nombres de `tanda1/t4/scripts/`. Además, y lo declaro porque la cláusula dice «solo sus scripts del "
-      "segundo tramo»:",
-      f"  - leí e importo sin cambios `tanda1/t3/scripts/celdas_t4_t3f.py` (sha256 `{idx['celdas_t4_t3f_sha256']}`), que tiene las cuotas "
-      "y las reglas de celda que pide el punto 5. Es código, sin cifras de la tanda 1, y es el que importa el T3 de la tanda final;",
-      "  - el control sustituto del primer paso 0 calculó el sha256 de los seis `kg.json` no rastreados contra su sello, dos de ellos de "
-      "`tanda1/t3/acumulado/`. No los leyó como datos.",
-      "  - No abrí sus muestras, su material, sus planillas, su lectura ni sus cifras: las de base salen de la versión derivada.",
-      "- No abrí ningún `.env` ni ningún `NO_ABRIR_`, ni entré en las carpetas vedadas.", ""]
-
-# 11. Para la autora y la mesa
-w += ["## 11. Para la autora y la mesa", "",
-      f"1. **El convertidor no conoce la planilla de la ampliación.** `t4/lectura_autora/convertir_lectura_T4.py` tiene en `SHA_PLANILLAS` "
-      f"las {len(conv_muestras)} muestras del primer tramo y frena con cualquier otra. No lo toqué (el «seguí» lo veda). Para sellar la "
-      "lectura de la ampliación hace falta decidir cómo: extenderlo o uno nuevo. Queda PENDIENTE de la mesa.",
-      "2. **El LEEME** (`t4/lectura_autora/LEEME_lectura_T4.md`) no nombra la ampliación. Las respuestas válidas son las de las aceptadas, "
-      "y las columnas de la planilla, las mismas. Si hace falta una nota para la ampliación, es de la mesa.",
-      "3. **Las interpretaciones mías que más pueden pesar en la lectura de la ampliación** (los criterios son los del primer tramo):",
-      "   - **U-tipo con el futuro normativo:** la ficha 20 («el Banco Central… determinará si corresponde el pago…», tipada Potestad) y la "
-      "28 («El lapso a consultar será el que medie…», tipada Condicion). Es el mismo criterio de la ficha 30 de las aceptadas no ítems del "
-      "primer tramo;",
-      "   - **la ficha 26** es la única en que miré texto que la ficha no muestra: el punto 1.4 del TO, para el desarrollo de la sigla FCEM. Sin "
-      "esa lectura, el desarrollo agregado sería una observación, como en la ficha 6, y la propuesta, «sin error»;",
-      "   - **la ficha 22** depende de quién devuelve las operaciones, que el texto no nombra. Su observación da la otra lectura;",
-      "   - **la ficha 18:** la entidad financiera es donde se pide el cambio, no quien tiene la facultad. La propongo como «con error».",
-      "4. **La cola:** la regla del 25 % se dispara. Qué se hace con ella en la tanda final no es de este mandato.",
-      "5. **La fila de no ítems para la hoja** queda con las 30 leídas (tabla 1). Su cifra sobre las 60 es del tercer tramo.",
-      "6. **Dos textos de `lineas_de_base` en `tasas/tasas_t4_tramo2.json`** dicen «umbrales_t4_tf,json» (sección 14, punto 4). Las cifras "
-      "están bien. Propongo corregir el script cuando se rehagan las tasas en el tercer tramo.",
-      "7. **`NO_ABRIR_conteos_t4_tramo2.json`** no existe (sección 10).", ""]
-
-# 12. Foto y grep
+      "- **No deciden nada:** la atención de RI se decidió en el segundo tramo, con su umbral de T3 para las n de entonces. Con las 60 van "
+      "como información, con el mismo método.",
+      ("- **La tasa de RI no cambia** con las 60 porque, en las dos celdas RI de no ítems, la proporción de errores de las 60 es la de las 30. "
+       "Cambian el n efectivo, el Wilson y el p-valor." if ri_igual else "- **La tasa de RI cambia** con las 60."), ""]
+
+# 7. Lo del segundo tramo
+lb2, lb3 = X2["lineas_de_base"], X["lineas_de_base"]
+w += ["## 7. Lo del segundo tramo, rehecho, y las líneas de base", "",
+      f"- **`tasas_t4t3_tf.py` rehace todo lo del segundo tramo** y controla, al final, que cada bloque dé lo mismo que "
+      f"`tasas/tasas_t4_tramo2.json`: {sum(lo2['bloques_iguales_a_tasas_t4_tramo2'].values())} de {len(lo2['bloques_iguales_a_tasas_t4_tramo2'])} "
+      f"(" + ", ".join(f"`{k}`" for k in lo2["bloques_iguales_a_tasas_t4_tramo2"]) + f"). Los controles de entrada del segundo tramo, iguales: "
+      f"{sn(lo2['controles_del_segundo_tramo_iguales'])}; los del tercero, {sum(ctrl.values())} de {len(ctrl)}.",
+      "- **Las líneas de base:** la coma decimal va ahora solo en los números. Cambian estos dos textos, y nada más:"]
+for k in lo2["lineas_de_base_que_cambian"]:
+    a, b = k.split(".")
+    w += [f"  - `{k}`: antes «{lb2[a][b]}»; ahora «{lb3[a][b]}»."]
+w += [""]
+
+# 8. Para la hoja
+w += ["## 8. Las cifras para la hoja de la revisión entre tandas", "",
+      "Van en `t4/tablas_t4_tramo3.md` (tabla 1), que genera `scripts/tablas_t4t3_tf.py` desde la salida de las tasas, con la fila de no "
+      "ítems sobre las 60. La copio tal cual:", "", partes[1], ""]
+
+# 9. Cegamiento
+w += ["## 9. El cegamiento", "",
+      "- **Ninguna cifra usa el estado de E3, `n_reintentos`, `reintentos_e3.jsonl`, `copias_nota_e3.jsonl`, las `marcas_e3` ni el gasto de "
+      "los reintentos.** `tasas_t4t3_tf.py` lee las marcadas y sus sellos, las muestras, las poblaciones, los umbrales, la versión derivada, "
+      "el script de la mesa y la salida del segundo tramo.",
+      "- **De la tanda 1** no abrí nada: ni muestras, ni material, ni planillas, ni cifras, ni scripts. El script de la mesa "
+      "(`controles_tanda1/umbrales_t4_por_celdas_mesa.py`) lo importo sin cambiarlo, como en el segundo tramo, y leí su docstring, que es la "
+      "regla del punto 2.",
+      "- No abrí ningún `.env` ni ningún `NO_ABRIR_` (la foto da 0 en `t4/`), ni entré en las carpetas vedadas.", ""]
+
+# 10. Para la autora y la mesa
+w += ["## 10. Para la autora y la mesa", "",
+      "1. **El freno salta** por la atención sobre las 60 de las aceptadas no ítems. Qué sigue lo deciden la mesa y la autora.",
+      "2. **La fila de no ítems para la hoja** es ahora la de las 60 (tabla 1); la de las 30 queda dentro de la misma celda.",
+      f"3. **Mis propuestas y la lectura de la autora en la ampliación** (información): coinciden en {len(marc) - len(cambios)} de {len(marc)}. "
+      f"Las propuestas daban " + ", ".join(f"{v} {k}" for k, v in sorted(cprop.items())) + "; la lectura da "
+      + ", ".join(f"{v} {k}" for k, v in sorted(caut.items())) + ". "
+      + ("Las que cambian: " + "; ".join(f"ficha {i}, de «{p}» a «{v}»" for i, p, v in cambios) + "." if cambios else ""),
+      "4. **La ponderada total y la atención de RI con las 60** van como información (sección 6).", ""]
+
+# 11. Foto y grep
@@ -315,2 +228 @@
-fotos = FOTO.read_text(encoding="utf-8").strip()
-w += [fotos, "",
+w += [FOTO.read_text(encoding="utf-8").strip(), "",
@@ -318,11 +230,9 @@
-      f"{g['archivos']} archivos nuevos o cambiados de la foto: {g['coincidencias']} coincidencias de los tokens del nombre y de los "
-      f"términos, {len(g['con_rutas_absolutas'])} archivos con rutas absolutas, {g['tokens_dentro_de_rutas_absolutas']} tokens dentro de "
-      f"rutas absolutas; control positivo, {g['control_positivo']}. Su salida va en el paquete. Este FRENO y su script se escriben después de "
-      "la foto: el control final del paquete confirma que son lo único nuevo desde ella y les pasa el grep.",
-      f"- **La copia del repo** (para el material y la lista de la ampliación) es la del `rsync` de la cláusula más una exclusión que la "
-      "cláusula no trae, `--exclude=/data/experiment/neo4j/volumen` (sección 14, punto 2). El control da "
-      f"{cc['nombres_vedados']} nombres vedados y {cc['enlaces']} enlaces; el log del `rsync` tiene {cc['log_lineas']} líneas, todas «skipping "
-      "non-regular file» (los enlaces que `--no-links` no copia). El control y el log van en el paquete. Ningún `git clone`.", ""]
-
-# 13. Scripts
-w += ["## 13. El script de cada cifra", "",
+      f"{g['archivos']} archivos nuevos de la foto: {g['coincidencias']} coincidencias de los tokens del nombre y de los términos, "
+      f"{len(g['con_rutas_absolutas'])} archivos con rutas absolutas, {g['tokens_dentro_de_rutas_absolutas']} tokens dentro de rutas "
+      f"absolutas; control positivo, {g['control_positivo']}. Su salida va en el paquete. Este FRENO y su script se escriben después de la "
+      "foto: el control final del paquete confirma que son lo único nuevo desde ella y les pasa el grep.",
+      "- **Un `__pycache__` que creé y borré antes de la foto** (sección 13, punto 1): la lista de `.pyc` de después es la del paso 0.",
+      "- **No hice copias del repo** en este tramo. Ningún `git clone`.", ""]
+
+# 12. Scripts
+w += ["## 12. El script de cada cifra", "",
@@ -330,56 +240,26 @@
-      "| las tasas, la atención, el freno, la sensibilidad, la ampliación (secciones 2 a 7) | `tasas_t4t2_tf.py` | "
-      "`tasas/tasas_t4_tramo2.json`, `tasas/distribuciones_bajo_H0_t4_tramo2.json`, `tasas/consola_tasas_t4t2_tf.txt` |",
-      "| la verificación independiente de las tasas | `verif_tasas_independiente_t4t2_tf.py` | `tasas/verif_tasas_independiente_t4t2_tf.json`, "
-      "su consola |",
-      "| las tablas 1 a 9 y las cifras para la hoja (secciones 3 a 6 y 9) | `tablas_t4t2_tf.py` | `tablas_t4_tramo2.md`, "
-      "`consola_tablas_t4t2_tf.txt` |",
-      "| el sorteo de la ampliación y sus dos corridas | `sorteo_ampliacion_t4t2_tf.py` | `ampliacion/muestras/`, "
-      "`ampliacion/segunda_corrida_del_sorteo/`, `ampliacion/consola_sorteo_ampliacion_corrida1.txt` |",
-      "| el material de la ampliación y su control | `material_ampliacion_t4t2_tf.py`, `control_material_ampliacion_t4t2_tf.py` | "
-      "`ampliacion/material/` |",
-      "| la lista de unidades a la vista | `unidades_a_la_vista_ampliacion_t4t2_tf.py` | `../t3/muestras/unidades_a_la_vista_T4.json`, "
-      "`ampliacion/consola_unidades_a_la_vista_ampliacion_t4t2_tf.txt` |",
-      "| la lectura asistida y la planilla de la autora | `anotar_ampliacion_t4t2.py`, `armar_lectura_ampliacion_t4t2.py` | "
-      "`ampliacion/lectura_asistida/`, `ampliacion/lectura_autora/` |",
-      "| las tablas A1 a A5 (sección 8) | `tablas_ampliacion_t4t2_tf.py` | `ampliacion/tablas_ampliacion_t4t2.md` y su consola |",
-      "| la foto (sección 12) | `freno_t4t2_foto_tf.py` | la sección 12; su salida, en el paquete |",
-      "| el texto de este FRENO | `freno_t4t2_armar_tf.py` | este archivo |",
-      "| el paso 0 repetido (sección 1) | `paso0_bis_t4_tramo2.sh` y `foto_contra_t4_tramo2.py`, en el paquete | su salida, pegada |", "",
-      f"- **Los controles de la entrada** de `tasas_t4t2_tf.py`: {sum(ctrl.values())} de {len(ctrl)} pasan (están en la salida, `controles`).",
-      f"- **La verificación independiente** recuenta las marcadas sin el código de la mesa y recalcula las tasas, los Wilson y los p-valores "
-      f"por convolución exacta con fracciones: {VER['iguales']} de {VER['cifras']} cifras iguales, {len(VER['distintas'])} distintas.",
-      "- **Cómo salieron los scripts:** `tasas_t4t2_tf.py`, `tablas_t4t2_tf.py`, `freno_t4t2_foto_tf.py`, `material_ampliacion_t4t2_tf.py` y "
-      "`armar_lectura_ampliacion_t4t2.py` los escribieron adaptadores con reemplazos exactos (`adaptar_*_t4_tramo2.py`, en el paquete) desde "
-      "los de la tanda 1 o los del primer tramo y T3; `freno_t4t2_armar_tf.py` lo escribí desde el de la tanda 1. Los diffs enteros de los "
-      "cuatro del «seguí» contra los de la tanda 1 van en el anexo.", ""]
-
-# 14. Errores
-w += ["## 14. Errores propios, con su causa", "",
-      "1. **La foto de después del primer tramo quedó solo en `/private/tmp` y se perdió.** Está declarado en la sección 5 de "
-      "`FRENO_T4_tramo2_paso0.md`, del paquete `revision_tanda_final_FRENO_T4_tramo2_paso0/`; lo reemplazó el control sustituto "
-      "(`control_sustituto_foto_t4_tramo2.py`, `control_sustituto_foto_T4_tramo2.json`), y la salida del paso 0 es "
-      "`paso0_T4_tramo2_salida.txt`, de `paso0_t4_tramo2.sh`. La causa: dejé la foto fuera del paquete porque nombra todas las rutas del "
-      "repo, y no la guardé en otro lugar permanente. Desde este tramo, las fotos van a `t4t2_fotos/`, en la carpeta permanente: la de las "
-      "12:16:33, la del paso 0 repetido, la de después y la final del paquete.",
-      "2. **La copia del repo lleva una exclusión que la cláusula no trae:** `--exclude=/data/experiment/neo4j/volumen`, la base de Neo4j, "
-      "fuera de git. La agregué sin que el mandato la autorizara. Ninguno de los tres scripts que corrieron sobre la copia la lee (no nombran "
-      "Neo4j), así que no cambia ninguna salida; el control de la copia dio 0 de todos modos. Lo declaro para que la mesa decida.",
-      "3. **La primera corrida del sorteo no arrancó.** La consola iba a `t4/ampliacion/`, que todavía no existía, y el shell frenó antes de "
-      "correr el script; la segunda corrida, a la carpeta de trabajo, sí corrió (dio el mismo sha256 de la muestra). Borré esa salida, creé "
-      "la carpeta y corrí las dos en orden: la del repo y la segunda, que copié a `t4/ampliacion/segunda_corrida_del_sorteo/`. Las tres "
-      "dan los mismos bytes (tabla A2).",
-      "4. **Dos textos de `lineas_de_base` dicen «umbrales_t4_tf,json».** En `tasas_t4t2_tf.py`, el `.replace(\".\", \",\")` de la coma "
-      "decimal se aplica a toda la cadena, con el nombre del archivo (las líneas de `aceptadas:total` y `atencion_RI`). Las cifras están "
-      "bien. No volví a correr las tasas: el índice del sorteo guarda el sha256 de su salida, y las tablas arman esas celdas desde los "
-      "campos numéricos. Lo vi al armar las tablas.",
-      "5. **Tres controles de mis adaptadores frenaron antes de escribir.** El de `adaptar_tasas_t4_tramo2.py` y el de "
-      "`adaptar_tablas_t4_tramo2.py` marcaban menciones legítimas de la tanda 1 (la ruta del script de la mesa y la del script de origen en "
-      "la cabecera); el de `adaptar_foto_t4_tramo2.py` encontró un `endswith(\".DS_Store\")` que ningún reemplazo cubría. Corregí la lista "
-      "o agregué el reemplazo y volví a correr; ningún destino estaba escrito.", ""]
-
-# 15. Lo que no hice
-w += ["## 15. Lo que no hice", "",
-      "- **T5 ni las FICHAS**, ni las tasas sobre las 60.",
-      "- **Lo que no toqué:** las marcadas, las exportaciones, el sello, las planillas del primer tramo, el LEEME, el convertidor y el control "
-      "de la mesa; los grafos, los manifiestos, la E0, el código del pipeline, la fixture, `grafos.py`, Neo4j, el backlog y el registro de "
-      "alcance. De `t3/` solo cambié `t3/muestras/unidades_a_la_vista_T4.json` (punto 5).",
+      "| las tasas sobre las 60, los dos frenos, lo del segundo tramo rehecho, la ponderada total y la atención de RI con las 60 | "
+      "`tasas_t4t3_tf.py` | `tasas/tasas_t4_tramo3.json`, `tasas/distribuciones_bajo_H0_t4_tramo3.json`, `tasas/consola_tasas_t4t3_tf.txt` |",
+      "| la verificación independiente | `verif_tasas_independiente_t4t3_tf.py` | `tasas/verif_tasas_independiente_t4t3_tf.json` y su consola |",
+      "| las tablas 1 a 12 y las cifras para la hoja | `tablas_t4t3_tf.py` | `tablas_t4_tramo3.md`, `consola_tablas_t4t3_tf.txt` |",
+      "| la foto (sección 11) | `freno_t4t3_foto_tf.py` | la sección 11; su salida, en el paquete |",
+      "| el texto de este FRENO | `freno_t4t3_armar_tf.py` | este archivo |",
+      "| el paso 0 (sección 1) | `paso0_t4_tramo3.sh` y `paso0_foto_contra_commits_t4_tramo3.py`, en el paquete | su salida, pegada |", "",
+      f"- **Los controles de la entrada** de `tasas_t4t3_tf.py`: {sum(ctrl.values())} de {len(ctrl)} pasan.",
+      f"- **La verificación independiente** recuenta las dos marcadas sin el código de la mesa ni `tasas_t4t3_tf.py` y recalcula con "
+      f"fracciones exactas, también el p-valor y el umbral sobre las 60 por convolución: {VER['iguales']} de {VER['cifras']} cifras "
+      f"iguales, {len(VER['distintas'])} distintas.",
+      "- **Cómo salieron los scripts:** los cuatro primeros los escribieron adaptadores con reemplazos exactos desde los del segundo tramo "
+      "(`adaptar_*_t4_tramo3.py`, en el paquete); `freno_t4t3_armar_tf.py` lo escribí desde el del segundo tramo. Los diffs enteros de los "
+      "cinco contra los del segundo tramo van en el anexo.", ""]
+
+# 13. Errores
+w += ["## 13. Errores propios, con su causa", "",
+      "1. **Escribí un `__pycache__` en `t4/scripts/`.** Para controlar la sintaxis de `freno_t4t3_foto_tf.py` corrí `python -m py_compile`, "
+      "que escribe el `.pyc` aunque se pase `-B`. Lo vi enseguida con un `find`, y borré el archivo y la carpeta (los dos, solo míos y sin "
+      "rastrear) antes de la foto de después. La lista de `.pyc` volvió a ser la del paso 0, y la de después lo confirma.", ""]
+
+# 14. Lo que no hice
+w += ["## 14. Lo que no hice", "",
+      "- **T5 ni las FICHAS.**",
+      "- **Lo que no toqué:** las marcadas, los sellos, las planillas, los convertidores, los LEEME y los controles de la mesa; nada de `t3/` "
+      "ni de fuera de `t4/`.",
@@ -388,2 +268,2 @@
-      "- **El scratchpad:** nada que se necesite después queda solo en él. El paquete y su copia permanente llevan los scripts del paso 0 "
-      "repetido, los adaptadores, la sección de la foto, el grep, el control y el log de la copia; las fotos van a `t4t2_fotos/`.",
+      "- **El scratchpad:** nada que se necesite después queda solo en él. El paquete y su copia permanente llevan el paso 0, los "
+      "adaptadores, la sección de la foto y el grep; las fotos van a `t4t2_fotos/`.",
@@ -391,4 +271,4 @@
-      "FRENO T4, segundo tramo. Espero la revisión de la mesa.", ""]
-
-# Anexo: los diffs
-w += ["## Anexo. Los diffs enteros de los cuatro scripts contra los de la tanda 1", "",
+      "FRENO T4, tercer tramo. Espero la revisión de la mesa.", ""]
+
+# Anexo
+w += ["## Anexo. Los diffs enteros de los cinco scripts contra los del segundo tramo", "",
```
