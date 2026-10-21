# FRENO T4 — tanda final de B6.1, segundo tramo: las tasas, la atención y la ampliación (USD 0, sin API, sin commit)

Rigen el pre-registro firmado de la tanda final (`docs/preregistro_tanda_final.md`, firma en `4de7f2a7`), §6, con su versión derivada
para la lectura de T4 (`tanda_final/preregistro/preregistro_tanda_final_derivada_T4.md`, sha256 `26c29d9424ffaf634a02735a972ad29e7df8b06463b8ad430654d50d4d442fc2`), el «seguí» del segundo tramo, la regla de las dudosas (registro de
decisiones, §35) y lo que decidió la autora sobre el FRENO del paso 0. La lectura es la de la autora, sellada en
`t4/lectura_autora/sello_lectura_T4.txt` y controlada por la mesa (`t4/control_lectura_mesa/`). HEAD `abdc0998`.

**Resultado:**
- **Las aceptadas, ítems** (sección 3): 6 de 30 con error, contando las dudosas; tasa ponderada 0,2862, Wilson [0,1090; 0,5678]. Atención: no (p 0,2710). Freno: no.
- **Las aceptadas, no ítems** (sección 3): 7 de 30 con error, contando las dudosas; tasa ponderada 0,3674, Wilson [0,1661; 0,6287]. Atención: sí (p 0,0168). Freno: no.
- **La atención de RI** (sección 3): 5 de 30; tasa ponderada de RI 0,1843, p 0,2945: no salta.
- **La ampliación** (secciones 7 y 8): sí, por la atención de las aceptadas no ítems. Sorteé 30 unidades más de las que no se leyeron, armé su material, la lectura asistida y la planilla en blanco de la autora, y sumé sus unidades a `t3/muestras/unidades_a_la_vista_T4.json`, que pasa a sha256 `4b9605f2d76cee42b13597e35b0eb7652e9e2723b952d91e0e09da1f63745633`. Las tasas sobre las 60 van en el tercer tramo, después de la lectura de la autora.
- **La cola** (sección 4): 12 de 30 con error; tasa ponderada 0,3706, Wilson [0,2057; 0,5723]. La regla del 25 % se dispara: es cifra y vigilancia, no freno.
- **La observación (12)** (sección 6): 29 correctas de 30, Wilson [0,8333; 0,9941]; incorrectas por `capa_pipeline`: catálogo, 1.
- **Las vigilancias** (sección 5): (1), 7 sí de 30; (2), 6 vaciamientos de 30; (3), 5 duplicaciones de 30; (7), 2 sin apoyo de 6, leída entera.
- **La regla de las dudosas** (sección 2): hay 0 dudosas en la cola y las aceptadas, así que la sensibilidad da otra decisión en 0 de las seis (atención y freno de cada estrato, atención de RI y regla del 25 % de la cola).
- Toda cifra sale por script de sus archivos. Las tablas que copio de una salida van tal cual; mis aclaraciones van fuera de las tablas.
- Nada commiteado y ningún mensaje de commit preparado: los commits son de la autora y quedan PENDIENTES.

## 1. Paso 0

- **El primer paso 0 frenó** (12:16). La foto de después del primer tramo, que era su punto de comparación, había quedado solo en `/private/tmp` y se perdió, y había cambios fuera de los commits: 7 archivos `.DS_Store`. Ese FRENO, su salida y su control sustituto están en el paquete `revision_tanda_final_FRENO_T4_tramo2_paso0/` (manifiesto con sha256 `13c1b8bb5cb4307e1a5304d7eb273eeb5bb7ebe6f0f8ee36fdae03e90e7d740e`), en la carpeta permanente de esta sesión, con estos nombres:
  - `FRENO_T4_tramo2_paso0.md`: el FRENO, con el error propio en su sección 5;
  - `paso0_T4_tramo2_salida.txt`, de `paso0_t4_tramo2.sh`: la salida del paso 0;
  - `control_sustituto_foto_t4_tramo2.py` y su salida, `control_sustituto_foto_T4_tramo2.json`: el control sustituto (A a H).
- **Lo que decidió la autora sobre ese FRENO:**
  1. el control sustituto vale como la foto de ese paso 0. Lo que no cubre: el contenido de los no rastreados o ignorados que no cambiaron de fecha (los cubre por la fecha y la cuenta, no por su sha256, salvo los seis `kg.json`);
  2. los archivos que se llaman exactamente `.DS_Store` son ruido de Finder y quedan fuera de lo que cuenta; se listan con su ruta. Cualquier otro cambio fuera de lo admitido cuenta, y freno;
  3. el paso 0 se repite antes de las tasas, contra la foto de las 12:16:33 guardada en `t4t2_fotos/`;
  4. la foto de después se compara archivo por archivo con la de las 12:16:33 y se guarda también en `t4t2_fotos/`;
  5. este FRENO cita el paquete del paso 0 y el error propio con los nombres del paquete (sección 14, punto 1).
- **Los `.DS_Store` del primer paso 0** (sin abrirlos): `.DS_Store`, `data/.DS_Store`, `data/experiment/.DS_Store`, `data/experiment/tanda_final/.DS_Store`, `data/experiment/tanda_final/t3/muestras/material/.DS_Store`, `data/experiment/tanda_final/t4/.DS_Store`, `data/experiment/tanda_final/t4/lectura_autora/.DS_Store`.
- **El paso 0 repetido**, antes de las tasas. La salida, con la carpeta personal reemplazada por `$HOME` y la carpeta de trabajo por `<DIR DE TRABAJO>` (`paso0_bis_T4_tramo2_salida.txt`, de `paso0_bis_t4_tramo2.sh`, y la comparación de `foto_contra_t4_tramo2.py`, en el paquete):

```
== pwd
$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg
== git log -1 --format='%h %s'
abdc0998 Tanda final: la cuarta etapa, primer tramo, con la lectura de la autora sellada y controlada
== git status --porcelain --untracked-files=no (entre las dos rayas)
--
--
== las marcadas contra el sello
igual aceptadas_items_marcada.csv
igual aceptadas_no_items_marcada.csv
igual cola_marcada.csv
igual observacion_12_marcada.csv
igual vigilancia_1_marcada.csv
igual vigilancia_2_marcada.csv
igual vigilancia_3_marcada.csv
igual vigilancia_7_marcada.csv
== tres sha256
d7f7860fbf09f92443992aeb9915e22191582cfe2edaf5fd0a089baadd3ac555  data/experiment/tanda_final/t3/muestras/umbrales_t4_tf.json
26c29d9424ffaf634a02735a972ad29e7df8b06463b8ad430654d50d4d442fc2  data/experiment/tanda_final/preregistro/preregistro_tanda_final_derivada_T4.md
06a126ed487f4ab9fc41b14d4a8c2d757dcb0706d578edcfdc9382fc70d8af5e  data/experiment/tanda_final/t3/muestras/unidades_a_la_vista_T4.json
== la foto de las 12:16:33 (t4t2_fotos/foto_repo_antes_T4t2.json)
104bcb1cec522cda1f42f34e5521ade7040706e23787429642611a161a0789d8
== la foto nueva y su comparación archivo por archivo
2026-10-21 15:32:44 2026-10-21 15:32:57 58077 entradas
{
 "foto_antes": {
  "sha256": "104bcb1cec522cda1f42f34e5521ade7040706e23787429642611a161a0789d8",
  "inicio": "2026-10-21 12:16:33",
  "n": 58077
 },
 "foto_despues": {
  "sha256": "30730b4966ec6f9de184883ddba628f1bf15a16e64d3b9d41b2e9b414171198a",
  "inicio": "2026-10-21 15:32:44",
  "fin": "2026-10-21 15:32:57",
  "n": 58077,
  "sin_abrir": 45,
  "enlaces": 342
 },
 "admitido": [],
 "nuevos": {
  "DS_Store": 0,
  "admitido": 0,
  "fuera_de_lo_admitido": 0
 },
 "borrados": {
  "DS_Store": 0,
  "admitido": 0,
  "fuera_de_lo_admitido": 0
 },
 "cambiados": {
  "DS_Store": 0,
  "admitido": 0,
  "fuera_de_lo_admitido": 0
 },
 "ok": true
}
rc=0
== .pyc: líneas y diff contra los del paso 0 (12:16)
   11236
iguales
== pgrep -fl "runner_corpus.py|lanzar_t|correr_tanda"
rc=1
== pgrep -fl ensamblar_tanda0.py
rc=1
== hora
2026-10-21 15:32:58
```

- **Las horas de la autora, del sello** (`t4/lectura_autora/sello_lectura_T4.txt`): 20/10: cola 18:36:07, aceptadas ítems 23:34:38; 21/10: aceptadas no ítems 08:37:10, (2) 10:37:31, (7) 10:48:43, (1) 11:13:20, (3) 11:30:16, (12) 11:41:13. La última marcada es de las 11:41:13 del 2026-10-21, antes del primer paso 0.

## 2. La regla de las dudosas y cómo la apliqué

- **La regla** (pre-registro de la tanda final, §6; registro de decisiones, §35):
  - en la cola y en las dos de las aceptadas, una unidad «dudosa» cuenta como error para la tasa, la atención y el freno;
  - la misma cuenta con las dudosas fuera, sobre las decididas, va al lado como sensibilidad y no decide nada;
  - si la sensibilidad diera otra decisión de atención o de freno, se declara, y rige la primera.
- **Cómo la apliqué** (`scripts/tasas_t4t2_tf.py`): en cada celda, la regla cuenta k = «con error» + «dudosa» sobre las n leídas; la sensibilidad cuenta k = «con error» sobre n − «dudosa». Los pesos de las celdas son los mismos en las dos.
- **Las dudosas:** 0 en la cola, 0 en ítems y 0 en no ítems (tablas 2 y 6).
- **Lo que da la sensibilidad:** otra decisión en 0. No hay nada que declarar por el tercer punto de la regla.

## 3. Las aceptadas

#### Tabla 2. Las aceptadas por celda (`aceptadas.<estrato>.por_celda`; pesos de `t3/muestras/umbrales_t4_tf.json`)

| estrato | celda | N | peso | leídas | con error | sin error | dudosa |
|---|---|---:|---:|---:|---:|---:|---:|
| items | RI:sin_raiz | 62 | 0,0480 | 12 | 1 | 11 | 0 |
| items | RI:resto | 3 | 0,0023 | 3 | 1 | 2 | 0 |
| items | NG:sin_raiz | 45 | 0,0349 | 5 | 1 | 4 | 0 |
| items | NG:resto | 1.181 | 0,9148 | 10 | 3 | 7 | 0 |
| no_items | RI:sin_raiz | 322 | 0,0900 | 10 | 2 | 8 | 0 |
| no_items | RI:resto | 48 | 0,0134 | 5 | 1 | 4 | 0 |
| no_items | NG:sin_raiz | 107 | 0,0299 | 5 | 0 | 5 | 0 |
| no_items | NG:resto | 3.102 | 0,8667 | 10 | 4 | 6 | 0 |

#### Tabla 3. Las tasas de las aceptadas, la regla y la sensibilidad (`aceptadas.<estrato>.regla` y `.sensibilidad_sin_dudosas`)

| estrato | cuenta | errores | leídas | tasa ponderada | n ef. | Wilson | p de la atención | atención | freno por intervalos | atención de T3 desde | freno de T3 desde |
|---|---|---:|---:|---:|---:|---|---:|---|---|---:|---:|
| items | regla (dudosa = error) | 6 | 30 | 0,2862 | 11,888 | [0,1090; 0,5678] | 0,2710 | no | no | 0,3899 | 0,6481 |
| items | sensibilidad (dudosas fuera) | 6 | 30 | 0,2862 | 11,888 | [0,1090; 0,5678] | 0,2710 | no | no | 0,3899 | 0,6481 |
| no_items | regla (dudosa = error) | 7 | 30 | 0,3674 | 13,133 | [0,1661; 0,6287] | 0,0168 | sí | no | 0,2897 | 0,5440 |
| no_items | sensibilidad (dudosas fuera) | 7 | 30 | 0,3674 | 13,133 | [0,1661; 0,6287] | 0,0168 | sí | no | 0,2897 | 0,5440 |

items: la sensibilidad da otra decisión de atención, no; de freno, no. La distribución bajo H0: 3.432 valores, suma 1,000000 (`tasas/distribuciones_bajo_H0_t4_tramo2.json`, `aceptadas:items:regla`).

no_items: la sensibilidad da otra decisión de atención, no; de freno, no. La distribución bajo H0: 4.106 valores, suma 1,000000 (`tasas/distribuciones_bajo_H0_t4_tramo2.json`, `aceptadas:no_items:regla`).

#### Tabla 4. La ponderada total y la atención de RI (`aceptadas.total` y `atencion_RI`)

| cifra | cuenta | errores de leídas | tasa | n ef. | Wilson | p de la atención | atención |
|---|---|---|---:|---:|---|---:|---|
| ponderada total | regla | — | 0,3458 | 21,260 | [0,1819; 0,5570] | — | sin umbral |
| ponderada total | sensibilidad | — | 0,3458 | 21,260 | [0,1819; 0,5570] | — | sin umbral |
| atención de RI | regla | 5 de 30 | 0,1843 | 16,967 | [0,0661; 0,4191] | 0,2945 | no |
| atención de RI | sensibilidad | 5 de 30 | 0,1843 | 16,967 | [0,0661; 0,4191] | 0,2945 | no |

Atención de RI: 435 unidades RI aceptadas; pesos items:RI:sin_raiz 0,1425, items:RI:resto 0,0069, no_items:RI:sin_raiz 0,7402, no_items:RI:resto 0,1103; por celda, con la regla, items:RI:sin_raiz 1 de 12, items:RI:resto 1 de 3, no_items:RI:sin_raiz 2 de 10, no_items:RI:resto 1 de 5.

#### Tabla 5. NG `sin_raiz`, por celda y sin umbral (`NG_sin_raiz`)

| estrato | N | leídas | con error | sin error | dudosa | tasa con la regla | tasa sin las dudosas |
|---|---:|---:|---:|---:|---:|---:|---:|
| items | 45 | 5 | 1 | 4 | 0 | 0,2000 | 0,2000 |
| no_items | 107 | 5 | 0 | 5 | 0 | 0,0000 | 0,0000 |

Mis aclaraciones:
- **Los pesos** son los de `t3/muestras/umbrales_t4_tf.json`, que T3 calculó con las unidades de cada celda antes de leer. `tasas_t4t2_tf.py` controla que sean los de `t3/muestras/poblaciones_t4_t3f_tf.json` y que las n de cada celda sean las de la muestra.
- **La atención** es el test exacto unilateral al 5 % contra la tanda 0, con la distribución de la tasa enumerada entera por la función `distribucion` del script de la mesa, importado sin cambiarlo. Su salida al importarse es byte a byte su JSON (sí). Las distribuciones van en `tasas/distribuciones_bajo_H0_t4_tramo2.json`.
- **Los umbrales de T3** van en la tabla 3 como información. La decisión sale del p-valor, y las dos dicen lo mismo en cada estrato: en ítems, la tasa (0,2862) está debajo del umbral de la atención (0,3899) y el p pasa de 0,05; en no ítems, la tasa (0,3674) pasa el umbral (0,2897) y el p (0,0168) no pasa de 0,05.
- **El freno** es el de los intervalos: el límite inferior del Wilson de la tasa contra el superior del Wilson de la tanda 0, la misma comparación que hace `umbrales` en el script de la mesa. No salta en ningún estrato. La tasa de no ítems sobre las 60 y su freno van en el tercer tramo.
- **NG `sin_raiz`** (tabla 5): son 152 unidades aceptadas. Van con su cifra por celda y sin umbral, como en la tanda 1 (pre-registro de la tanda 1, `95b18217:619`).

## 4. La cola

#### Tabla 6. La cola por celda y su tasa (`cola`)

| celda | N | peso | leídas | con error | sin error | dudosa |
|---|---:|---:|---:|---:|---:|---:|
| RI:sin_raiz | 6 | 0,0750 | 6 | 1 | 5 | 0 |
| RI:resto | 2 | 0,0250 | 2 | 1 | 1 | 0 |
| NG:sin_raiz | 5 | 0,0625 | 5 | 4 | 1 | 0 |
| NG:resto | 67 | 0,8375 | 17 | 6 | 11 | 0 |

| cuenta | errores | leídas | tasa ponderada | n ef. | Wilson | la regla del 25 % se dispara |
|---|---:|---:|---:|---:|---|---|
| regla (dudosa = error) | 12 | 30 | 0,3706 | 23,100 | [0,2057; 0,5723] | sí |
| sensibilidad (dudosas fuera) | 12 | 30 | 0,3706 | 23,100 | [0,2057; 0,5723] | sí |

La sensibilidad da otra decisión de la regla del 25 %: no.

Mis aclaraciones:
- **La ponderada** usa los pesos de la cola de `umbrales_t4_tf.json`, con el n efectivo de Kish.
- **La regla del 25 %** se dispara con la regla de las dudosas y también sin ellas. Es cifra y vigilancia, no freno, como en la tanda 1 (pre-registro de la tanda 1, `95b18217:641`). Qué se hace con ella en la tanda final queda para la mesa y la autora (sección 11).

## 5. Las vigilancias (1), (2), (3) y (7)

#### Tabla 7. Las vigilancias (1), (2), (3) y (7), por celda (`vigilancias.<muestra>.por_celda`)

| muestra | celda | N | leídas | respuestas |
|---|---|---:|---:|---|
| vigilancia:1 | RI:sin_raiz | 105 | 10 | sí 3, no 7, no decidible 0 |
| vigilancia:1 | RI:resto | 17 | 5 | sí 2, no 3, no decidible 0 |
| vigilancia:1 | NG:sin_raiz | 59 | 5 | sí 0, no 5, no decidible 0 |
| vigilancia:1 | NG:resto | 2.011 | 10 | sí 2, no 8, no decidible 0 |
| vigilancia:2 | RI:sin_raiz | 98 | 13 | vaciamiento 3, no vaciamiento 10, no decidible 0 |
| vigilancia:2 | RI:resto | 2 | 2 | vaciamiento 1, no vaciamiento 1, no decidible 0 |
| vigilancia:2 | NG:sin_raiz | 5 | 5 | vaciamiento 1, no vaciamiento 4, no decidible 0 |
| vigilancia:2 | NG:resto | 187 | 10 | vaciamiento 1, no vaciamiento 9, no decidible 0 |
| vigilancia:3 | RI:sin_raiz | 12 | 10 | duplicación 2, distintos 8 |
| vigilancia:3 | RI:resto | 5 | 5 | duplicación 1, distintos 4 |
| vigilancia:3 | NG:sin_raiz | 3 | 3 | duplicación 0, distintos 3 |
| vigilancia:3 | NG:resto | 200 | 12 | duplicación 2, distintos 10 |
| vigilancia:7 | RI:sin_raiz | 1 | 1 | con apoyo 1, sin apoyo 0, no decidible 0 |
| vigilancia:7 | RI:resto | 0 | 0 | con apoyo 0, sin apoyo 0, no decidible 0 |
| vigilancia:7 | NG:sin_raiz | 0 | 0 | con apoyo 0, sin apoyo 0, no decidible 0 |
| vigilancia:7 | NG:resto | 5 | 5 | con apoyo 3, sin apoyo 2, no decidible 0 |

#### Tabla 8. Las tasas de las vigilancias, la cruda y la ponderada por celda (`vigilancias.<muestra>`)

| muestra | se vigila | por respuesta | fuera de la tasa | cruda | Wilson (cruda) | ponderada por celda | n ef. | Wilson (ponderada) |
|---|---|---|---|---|---|---:|---:|---|
| vigilancia:1 | sí | sí 7, no 23, no decidible 0 | no decidible 0 | 7 de 30, 0,2333 | [0,1179; 0,4093] | 0,2010 | 11,827 | [0,0627; 0,4858] |
| vigilancia:2 | vaciamiento | vaciamiento 6, no vaciamiento 24, no decidible 0 | — | 6 de 30, 0,2000 | [0,0951; 0,3731] | 0,1483 | 20,097 | [0,0516; 0,3579] |
| vigilancia:3 | duplicación | duplicación 5, distintos 25 | — | 5 de 30, 0,1667 | [0,0734; 0,3356] | 0,1670 | 14,423 | [0,0522; 0,4218] |
| vigilancia:7 | sin apoyo | con apoyo 4, sin apoyo 2, no decidible 0 | — | 2 de 6, 0,3333 | [0,0968; 0,7000] | — | — | leída entera, sin celdas |

Vigilancia (3): el grupo es de nodos con la misma unidad y el mismo tramo, así que no ve las duplicaciones con tramos distintos (registro de decisiones, §29; LEEME de la lectura de T4).

Mis aclaraciones:
- **La ponderación:** las cuatro muestras salieron por celdas, y van la cruda (k sobre las leídas, con el Wilson de esa n) y la ponderada por celda (con el Wilson del n efectivo de Kish), las dos, como en la tanda 1.
- **Las no decidibles:** en la (1) quedan fuera de la tasa, con su cuenta (registro de decisiones, §29), y son 0. En la (2) y en la (7) no hay ninguna: 0 y 0.
- **Los pesos:** los de la (1) y la (3) son los de `t3/muestras/poblaciones_t4t1_tf.json` (2.192 nodos Condicion y 220 grupos). Los de la (2), los de la extracción final de `umbrales_t4_tf.json` (292 unidades).
- **La (3)** lleva su declaración debajo de la tabla 8. El criterio de su lectura para el par deber y acto regulado es el de la §31 del registro de decisiones, fijado antes de leer.
- **La (7)** se leyó entera (6 aristas, sin celdas). Su Wilson es el de la cruda con esa n.

## 6. La observación (12)

#### Tabla 9. La observación (12), por celda (`observacion:12`; pesos de `t3/muestras/poblaciones_t4t1_tf.json`)

| celda | N | peso | leídas | correcta | no decidible | incorrecta |
|---|---:|---:|---:|---:|---:|---:|
| RI:sin_raiz | 1.657 | 0,0664 | 10 | 9 | 0 | 1 |
| RI:resto | 481 | 0,0193 | 5 | 5 | 0 | 0 |
| NG:sin_raiz | 766 | 0,0307 | 5 | 5 | 0 | 0 |
| NG:resto | 22.045 | 0,8836 | 10 | 10 | 0 | 0 |

Cruda: 29 correctas de 30, 0,9667, Wilson [0,8333; 0,9941]. Ponderada por celda: 0,9934, n ef. 12,694, Wilson [0,7576; 0,9999]. Las incorrectas, por `capa_pipeline`: catálogo, 1 (fichas `fichas_observacion_12.md#5`).

Mis aclaraciones:
- **La cuenta** es la de la enmienda de la observación 12 (`docs/enmienda_preregistro_tanda0_2026-09-27_observacion12.md:107-111`): correctas sobre 30, con las no decidibles aparte y en el denominador, y el Wilson sobre correctas / 30. La ponderada por celda va al lado porque la muestra salió por celdas.
- **Los pesos** son los del universo de la decisión 1.2 (24.949 aristas, `t3/muestras/poblaciones_t4t1_tf.json`), los mismos que trae `otras.observacion:12` de `umbrales_t4_tf.json` (24.949 aristas).

## 7. La atención, el freno y la ampliación

- **La atención:** ítems, no (p 0,2710); no ítems, sí (p 0,0168); RI, no (p 0,2945). Con las dudosas fuera, lo mismo: aceptadas:items no, aceptadas:no_items sí, RI no.
- **El freno:** ítems, no; no ítems, no.
- **La ampliación: sí,** de las aceptadas no ítems (sección 8). La atención de ítems y la de RI no saltan, así que no se sortea nada de ítems.

## 8. La ampliación de las aceptadas no ítems

Las tablas A1 a A5 son las de `t4/ampliacion/tablas_ampliacion_t4t2.md`, de `scripts/tablas_ampliacion_t4t2_tf.py` (rutas relativas a `t4/`). Las copio tal cual.

- **El sorteo** (`scripts/sorteo_ampliacion_t4t2_tf.py`): sobre las unidades del estrato que no se leyeron, con las cuotas y las reglas de celda de la tanda 1 (`celdas_t4_t3f.asignar`, sin cambios) y la cadena `tandafinal:{muestra}:{celda}:ampliacion:{base}` («seguí», punto 5; pre-registro, §6: «las ampliaciones con `:ampliacion:`»). La base es el sha256 de la versión para firmar del pre-registro (`5289b02f`), como en T3; el script controla que el texto firmado (`4de7f2a7`) traiga la base, la plantilla y «`:ampliacion:`», y que la salida de las tasas diga que salta solo la atención de no ítems.

#### Tabla A1. El sorteo de la ampliación, por celda (`ampliacion/muestras/aceptadas_no_items_ampliacion.json`; 2026-10-21T15:40:09-03:00; de `scripts/sorteo_ampliacion_t4t2_tf.py`)

| celda | N del estrato | leídas en el primer tramo | quedan | sorteadas | cómo | cadena |
|---|---:|---:|---:|---:|---|---|
| RI:sin_raiz | 322 | 10 | 312 | 10 | sorteo | `tandafinal:aceptadas:no_items:RI:sin_raiz:ampliacion:0897d609851ae712768f0c1b68c2a485d5d8d91903aca84f3b54df58664d488b` |
| RI:resto | 48 | 5 | 43 | 5 | sorteo | `tandafinal:aceptadas:no_items:RI:resto:ampliacion:0897d609851ae712768f0c1b68c2a485d5d8d91903aca84f3b54df58664d488b` |
| NG:sin_raiz | 107 | 5 | 102 | 5 | sorteo | `tandafinal:aceptadas:no_items:NG:sin_raiz:ampliacion:0897d609851ae712768f0c1b68c2a485d5d8d91903aca84f3b54df58664d488b` |
| NG:resto | 3.102 | 10 | 3.092 | 10 | sorteo | `tandafinal:aceptadas:no_items:NG:resto:ampliacion:0897d609851ae712768f0c1b68c2a485d5d8d91903aca84f3b54df58664d488b` |
| total | 3.579 | 30 | 3.549 | 30 | — | — |

Las cuotas son las de `celdas_t4_t3f.asignar` de la tanda 1 (sha256 `f0082e3cd588e855e65d024fc360d669abba6da134199bc0b06bfc2a63e40c29`) sobre lo que queda; notas de la asignación: ninguna. Base `0897d609851ae712768f0c1b68c2a485d5d8d91903aca84f3b54df58664d488b` (sha256 de la versión para firmar, `True`); pre-registro firmado `b760edf7d341290ad910de993f8a868be426abcf2cfd14459240ad5a2b940cc2`. Controles del sorteo: 4 de 4 pasan.

#### Tabla A2. Las dos corridas del sorteo (sha256 recalculado aquí)

| archivo | primera corrida | segunda corrida | iguales |
|---|---|---|---|
| `aceptadas_no_items_ampliacion.json` | `d8c8c337a96a9531c24a1d3a2673c264f8e137eaea897a88965c5fd75bca5726` | `d8c8c337a96a9531c24a1d3a2673c264f8e137eaea897a88965c5fd75bca5726` | True |
| `sorteo_ampliacion_t4t2_tf.json` | `e32c0dd710e3925d527964667c0473b44ef0969772fba373b2890b4185cad856` | `e32c0dd710e3925d527964667c0473b44ef0969772fba373b2890b4185cad856` | True |

La muestra de la primera corrida es la del índice: `True`. Horas de los índices: 2026-10-21T15:40:09-03:00 y 2026-10-21T15:40:09-03:00.

- **El material** (`scripts/material_ampliacion_t4t2_tf.py`, que es `t3/scripts/material_t4_t3f_tf.py` con la muestra de la ampliación): corrió sobre la copia del repo (sección 12), sin `ANTHROPIC_API_KEY`, y lo copié a `t4/ampliacion/material/` con su consola; los sha256 del repo son los de la copia. El control (`scripts/control_material_ampliacion_t4t2_tf.py`, el de T3 con el índice de la ampliación) da 0 claves vedadas.
- **La lectura asistida** (`scripts/anotar_ampliacion_t4t2.py` y `scripts/armar_lectura_ampliacion_t4t2.py`): como en el primer tramo, con los mismos criterios (`criterios_de_la_propuesta`; solo cambia la nota de las dudosas, que remite al tercer tramo). La leí yo (Claude Opus 5.5, `claude-opus-5-5`), sin API; las propuestas se escribieron de 15:44:11 a 15:50:41 del 2026-10-21. El borrador se escribió en el repo (`t4/ampliacion/lectura_asistida/borradores/`) y de ahí salen la lectura asistida, las omisiones y observaciones y la planilla de la autora.
- **La planilla de la autora:** `t4/ampliacion/lectura_autora/aceptadas_no_items_ampliacion.csv`, con las columnas de las del primer tramo (`id`, `celda`, `ficha`, `propuesta`, `justificacion`, `veredicto_autora` y `nota_autora`, las dos últimas vacías) y la ruta de cada ficha en `t4/ampliacion/material/aceptadas_no_items_ampliacion/fichas_aceptadas_no_items_ampliacion.md`.
- **La lista de unidades a la vista** (`scripts/unidades_a_la_vista_ampliacion_t4t2_tf.py`, con la regla de T3, copiada): corrió sobre la copia, controló que las ocho muestras de T3 den lo mismo que en la lista vigente y la reemplacé en el repo después de controlar que la vigente era la de HEAD. Es antes de cualquier sorteo de las FICHAS: no hubo ninguno.

#### Tabla A3. El material, la lectura asistida y la planilla de la autora (sha256 recalculado aquí)

| archivo | sha256 | igual al de su índice |
|---|---|---|
| `ampliacion/material/aceptadas_no_items_ampliacion/fichas_aceptadas_no_items_ampliacion.jsonl` | `9c396359c23ef4f854561301ef571d410ea8765847ea9aaa6d718b1f7fd84f5d` | True (`material/material_ampliacion_t4t2_tf.json`) |
| `ampliacion/material/aceptadas_no_items_ampliacion/fichas_aceptadas_no_items_ampliacion.md` | `c52d8351c92706b2f74d2b4f5c2caa321d827e8dc1ac2c74a7b1bd937214cec3` | True (`material/material_ampliacion_t4t2_tf.json`) |
| `ampliacion/material/aceptadas_no_items_ampliacion/planilla_aceptadas_no_items_ampliacion.csv` | `e5d18dc310b4be536c95647cb23ecddc3691728f9b7613b08d30eafbded477da` | True (`material/material_ampliacion_t4t2_tf.json`) |
| `ampliacion/lectura_autora/aceptadas_no_items_ampliacion.csv` | `e99eaa2c347fe95a345dc63b26208f8681e28c2daf894e120e947d2855ff2331` | True (`lectura_asistida/lectura_asistida_t4_ampliacion.json`) |
| `ampliacion/lectura_asistida/lectura_asistida_t4_ampliacion.json` | `58ce4f91c75b32bfb53adbf66b9f8acfe65818eb138fba68c29e58a9a54a2ead` | — |
| `ampliacion/lectura_asistida/omisiones_y_observaciones_t4_ampliacion.md` | `c43729757456d9cfbcd0355efdf1e678e9cdfe6de5fef4542be92c89da48cfcc` | — |
| `ampliacion/lectura_asistida/borradores/aceptadas_no_items_ampliacion.jsonl` | `efb477c8064b2250ecd0f94ecb666be09308229197c43a38ca3284cc5a474623` | — |

La forma de la planilla de la autora: UTF-8 sin BOM, True; sin «\r», True; columnas, True; filas, True; las dos columnas de la autora, vacías, True; ninguna celda empieza con «=», «+», «-» ni «@», True.

El control del material (`material/control_material_ampliacion_t4t2_tf.json`): 30 fichas, 0 claves vedadas, texto de la E0 en 30, 0 sin texto, 0 con el estado en el `.md`; ok: True. Hora del material: 2026-10-21T15:41:53-03:00, posterior a la del sorteo (2026-10-21T15:40:09-03:00): True.

#### Tabla A4. La lista de unidades a la vista (`../t3/muestras/unidades_a_la_vista_T4.json`; 2026-10-21T15:42:59-03:00)

| cifra | valor |
|---|---|
| sha256 anterior | `06a126ed487f4ab9fc41b14d4a8c2d757dcb0706d578edcfdc9382fc70d8af5e` (2026-10-20T14:09:45-03:00) |
| sha256 nuevo (recalculado aquí) | `4b9605f2d76cee42b13597e35b0eb7652e9e2723b952d91e0e09da1f63745633` |
| unidades a la vista antes | 3.695 |
| unidades que suma la ampliación | 221 |
| unidades a la vista después | 3.916 (`todas_las_muestras`: 3.916) |
| antes + suma = después | True |
| las ocho muestras de T3 dan lo mismo que en la lista anterior | True |
| el material de la ampliación que usa la lista es el de la tabla A3 | True |

#### Tabla A5. Las propuestas de la lectura asistida, por celda (`lectura_asistida/lectura_asistida_t4_ampliacion.json`; modelo Claude Opus 5.5, `claude-opus-5-5`; de 2026-10-21T15:44:11-03:00 a 2026-10-21T15:50:41-03:00)

Son propuestas, no veredictos: la autora lee la planilla y las tasas sobre las 60 van en el tercer tramo.

| celda | fichas | con error | sin error | dudosa |
|---|---:|---:|---:|---:|
| RI:sin_raiz | 10 | 1 | 8 | 1 |
| RI:resto | 5 | 1 | 4 | 0 |
| NG:sin_raiz | 5 | 2 | 3 | 0 |
| NG:resto | 10 | 3 | 7 | 0 |
| total | 30 | 7 | 22 | 1 |

| regla | propuestas | fichas |
|---|---:|---|
| `U-sostenida` | 22 | 1, 2, 4, 5, 6, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19, 21, 23, 24, 25, 27, 29, 30 |
| `U-no-sostenida` | 5 | 7, 12, 18, 22, 26 |
| `U-tipo` | 2 | 20, 28 |
| `U-fuera-del-texto` | 1 | 3 |

- **Lo que sigue (tercer tramo):** la autora lee la planilla; con su lectura sellada, las tasas sobre las 60 (las 30 leídas y las 30 de la ampliación), la atención y el freno. Lo que hace falta antes está en la sección 11, puntos 1 y 2.

## 9. Las cifras para la hoja de la revisión entre tandas

Van en `t4/tablas_t4_tramo2.md` (tabla 1), que genera `scripts/tablas_t4t2_tf.py` desde la salida de las tasas. La copio tal cual:

#### Tabla 1. Las cifras para la hoja de la revisión entre tandas (filas que esperan a T4)

| fila | tanda final | línea de base: tanda 1 (versión derivada) | tanda 0 | decisión | script y clave de la salida |
|---|---|---|---|---|---|
| aceptadas, ítems | 6 de 30 (6 con error y 0 dudosas); ponderada 0,2862, Wilson [0,1090; 0,5678] (n ef. 11,888); sin las dudosas, 6 de 30, 0,2862 [0,1090; 0,5678] | 9 de 30 con las dudosas como error; ponderada 0,2196, Wilson de Kish [0,0784; 0,4822]; atención: no; freno: no | 6 de 30, Wilson [0,0951; 0,3731] | atención: no (p 0,2710); freno: no | `scripts/tasas_t4t2_tf.py`, `tasas/tasas_t4_tramo2.json`, `aceptadas.items` |
| aceptadas, no ítems | 7 de 30 (7 con error y 0 dudosas); ponderada 0,3674, Wilson [0,1661; 0,6287] (n ef. 13,133); sin las dudosas, 7 de 30, 0,3674 [0,1661; 0,6287] | 3 de 30 con las dudosas como error; ponderada 0,0968, Wilson de Kish [0,0214; 0,3446]; atención: no; freno: no | 4 de 30, Wilson [0,0531; 0,2968] | atención: sí (p 0,0168); freno: no | `scripts/tasas_t4t2_tf.py`, `tasas/tasas_t4_tramo2.json`, `aceptadas.no_items` |
| aceptadas, ponderada total | 0,3458, Wilson [0,1819; 0,5570] (n ef. 21,260); sin las dudosas, 0,3458 [0,1819; 0,5570] | 0,1397, Wilson de Kish [0,0532; 0,3196] | 0,1616, Wilson [0,0888; 0,2760] (mismo método) | sin umbral | `scripts/tasas_t4t2_tf.py`, `tasas/tasas_t4_tramo2.json`, `aceptadas.total` |
| atención de RI | 5 de 30; ponderada de RI 0,1843, Wilson [0,0661; 0,4191] (n ef. 16,967); sin las dudosas, 5 de 30, 0,1843 | 7 de 30; ponderada de RI 0,1747; la atención no salta | bajo H0, 0,1433 (umbral de T3: 0,2918) | atención: no (p 0,2945) | `scripts/tasas_t4t2_tf.py`, `tasas/tasas_t4_tramo2.json`, `atencion_RI` |
| tasa de error de la cola | 12 de 30 (12 con error y 0 dudosas); ponderada 0,3706, Wilson [0,2057; 0,5723] (n ef. 23,100); sin las dudosas, 12 de 30, 0,3706 [0,2057; 0,5723] | 14 de 30 con las dudosas como error; ponderada 0,4386, Wilson de Kish [0,2751; 0,6166]; la regla del 25 % se dispara | 12 de 30, Wilson [0,246; 0,577] (reext_t0/t4/salida/tasas_t4.json) | regla del 25 %: se dispara (cifra y vigilancia, no freno) | `scripts/tasas_t4t2_tf.py`, `tasas/tasas_t4_tramo2.json`, `cola` |
| observación (12) | 29 correctas de 30 (0 no decidibles, en el denominador; 1 incorrecta: catálogo 1); Wilson [0,8333; 0,9941]; ponderada por celda 0,9934 [0,7576; 0,9999] | 27 correctas de 30, Wilson [0,7438; 0,9654] | 25 de 30, Wilson [0,664; 0,927], con el perfil anterior (pre-registro de la tanda 1, §5.2, como lo da tanda1/t4/scripts/tasas_t4t2.py) | sin umbral | `scripts/tasas_t4t2_tf.py`, `tasas/tasas_t4_tramo2.json`, `observacion:12` |
| vigilancia (1) | 7 sí de 30 (0 no decidibles, fuera de la tasa); cruda 0,2333, Wilson [0,1179; 0,4093]; ponderada por celda 0,2010 [0,0627; 0,4858] | 3 sí de 30 | no se midió en la tanda 0 | sin umbral | `scripts/tasas_t4t2_tf.py`, `tasas/tasas_t4_tramo2.json`, `vigilancias.vigilancia:1` |
| vigilancia (2) | 6 vaciamientos de 30; cruda 0,2000, Wilson [0,0951; 0,3731]; ponderada por celda 0,1483 [0,0516; 0,3579] | 15 vaciamientos de 30 | en la tanda 0 se midió la población, sin leer la muestra | sin umbral | `scripts/tasas_t4t2_tf.py`, `tasas/tasas_t4_tramo2.json`, `vigilancias.vigilancia:2` |
| vigilancia (3) | 5 duplicaciones de 30; cruda 0,1667, Wilson [0,0734; 0,3356]; ponderada por celda 0,1670 [0,0522; 0,4218] | 9 duplicaciones de 30 | no se midió en la tanda 0 | sin umbral | `scripts/tasas_t4t2_tf.py`, `tasas/tasas_t4_tramo2.json`, `vigilancias.vigilancia:3` |
| vigilancia (7) | 2 sin apoyo de 6; cruda 0,3333, Wilson [0,0968; 0,7000]; leída entera, sin celdas | 2 sin apoyo de 4 | en la tanda 0 se midió la población, sin leer la muestra | sin umbral | `scripts/tasas_t4t2_tf.py`, `tasas/tasas_t4_tramo2.json`, `vigilancias.vigilancia:7` |

- **La ampliación:** salta la atención de ítems, no; la de no ítems, sí; la de RI, no. Hay ampliación: sí. Con las dudosas fuera: aceptadas:items no, aceptadas:no_items sí, RI no.
- **Lo que salta va a la ampliación:** aceptadas:no_items. Su fila de la hoja queda con las 30 leídas: las tasas sobre las 60 (las 30 y las 30 de la ampliación) van en el tercer tramo, después de la lectura de la autora.
- **Las líneas de base:** la tanda 1, los valores T4.* de tanda_final/preregistro/preregistro_tanda_final_derivada_T4.huecos.json (versión derivada para la lectura); la tanda 0, al lado, la de cada fila de `lineas_de_base`.
- **Los controles de la entrada** (`scripts/tasas_t4t2_tf.py`): 41 de 41 pasan.

## 10. El cegamiento

- **Ninguna cifra de este tramo usa el estado de E3, `n_reintentos`, `reintentos_e3.jsonl`, `copias_nota_e3.jsonl`, las `marcas_e3` ni el gasto de los reintentos.** `tasas_t4t2_tf.py` lee solo las marcadas y su sello, las muestras, las poblaciones, los umbrales, la versión derivada y el script de la mesa. El material de la ampliación no trae el estado ni las marcas de E3 (tabla A3: 0 claves vedadas). No miré ningún desglose por estado de E3.
- **Por eso no escribí `t4/NO_ABRIR_conteos_t4_tramo2.json`:** no hay nada que lo use. La foto da 0 `NO_ABRIR_` en `t4/` (sección 12).
- **De la tanda 1** abrí sus cuatro scripts del segundo tramo (`tasas_t4t2.py`, `tablas_t4t2.py`, `freno_t4t2_foto.py` y `freno_t4t2_armar.py`) y listé los nombres de `tanda1/t4/scripts/`. Además, y lo declaro porque la cláusula dice «solo sus scripts del segundo tramo»:
  - leí e importo sin cambios `tanda1/t3/scripts/celdas_t4_t3f.py` (sha256 `f0082e3cd588e855e65d024fc360d669abba6da134199bc0b06bfc2a63e40c29`), que tiene las cuotas y las reglas de celda que pide el punto 5. Es código, sin cifras de la tanda 1, y es el que importa el T3 de la tanda final;
  - el control sustituto del primer paso 0 calculó el sha256 de los seis `kg.json` no rastreados contra su sello, dos de ellos de `tanda1/t3/acumulado/`. No los leyó como datos.
  - No abrí sus muestras, su material, sus planillas, su lectura ni sus cifras: las de base salen de la versión derivada.
- No abrí ningún `.env` ni ningún `NO_ABRIR_`, ni entré en las carpetas vedadas.

## 11. Para la autora y la mesa

1. **El convertidor no conoce la planilla de la ampliación.** `t4/lectura_autora/convertir_lectura_T4.py` tiene en `SHA_PLANILLAS` las 8 muestras del primer tramo y frena con cualquier otra. No lo toqué (el «seguí» lo veda). Para sellar la lectura de la ampliación hace falta decidir cómo: extenderlo o uno nuevo. Queda PENDIENTE de la mesa.
2. **El LEEME** (`t4/lectura_autora/LEEME_lectura_T4.md`) no nombra la ampliación. Las respuestas válidas son las de las aceptadas, y las columnas de la planilla, las mismas. Si hace falta una nota para la ampliación, es de la mesa.
3. **Las interpretaciones mías que más pueden pesar en la lectura de la ampliación** (los criterios son los del primer tramo):
   - **U-tipo con el futuro normativo:** la ficha 20 («el Banco Central… determinará si corresponde el pago…», tipada Potestad) y la 28 («El lapso a consultar será el que medie…», tipada Condicion). Es el mismo criterio de la ficha 30 de las aceptadas no ítems del primer tramo;
   - **la ficha 26** es la única en que miré texto que la ficha no muestra: el punto 1.4 del TO, para el desarrollo de la sigla FCEM. Sin esa lectura, el desarrollo agregado sería una observación, como en la ficha 6, y la propuesta, «sin error»;
   - **la ficha 22** depende de quién devuelve las operaciones, que el texto no nombra. Su observación da la otra lectura;
   - **la ficha 18:** la entidad financiera es donde se pide el cambio, no quien tiene la facultad. La propongo como «con error».
4. **La cola:** la regla del 25 % se dispara. Qué se hace con ella en la tanda final no es de este mandato.
5. **La fila de no ítems para la hoja** queda con las 30 leídas (tabla 1). Su cifra sobre las 60 es del tercer tramo.
6. **Dos textos de `lineas_de_base` en `tasas/tasas_t4_tramo2.json`** dicen «umbrales_t4_tf,json» (sección 14, punto 4). Las cifras están bien. Propongo corregir el script cuando se rehagan las tasas en el tercer tramo.
7. **`NO_ABRIR_conteos_t4_tramo2.json`** no existe (sección 10).

## 12. La foto del repo, los .pyc y el grep de convenciones

Lo genera `scripts/freno_t4t2_foto_tf.py` desde la foto de las 12:16:33 y la de después. Las dos quedan en `t4t2_fotos/`, en la carpeta permanente de esta sesión (`fuera_del_repo/scratchpads/<sesión>/scratchpad/`), fuera del repo y del paquete porque nombran todas las rutas del repo.

- **La foto** (`t1/foto_repo_tanda_final_t1.py`). La de las 12:16:33: 12:16:33 a 12:16:46 del 2026-10-21, 58.077 entradas, sha256 `104bcb1cec522cda1f42f34e5521ade7040706e23787429642611a161a0789d8`. Después: 15:59:42 a 15:59:56 del 2026-10-21, 58.116 entradas, 45 sin abrir y 342 enlaces, sha256 `5adabd72de14c5f62946e4595a539ed09cf27f5e01592d551f24564d8e6530b0`.
  - **39 nuevos:** 2 en `tanda_final/t4/, lo demás`; 20 en `tanda_final/t4/ampliacion/`; 11 en `tanda_final/t4/scripts/`; 6 en `tanda_final/t4/tasas/`.
  - **0 borrados:** ninguno.
  - **1 cambiados:** 1, el archivo del punto 5 (ampliación).
  - **Fuera de lo admitido:** 0.
  - **Los `NO_ABRIR_` en `t4/`:** 0 en las dos fotos.
  - **`unidades_a_la_vista_T4.json`** (`t3/muestras/`): con la ampliación cambia; sha256 `06a126ed487f4ab9fc41b14d4a8c2d757dcb0706d578edcfdc9382fc70d8af5e` a las 12:16:33 y `4b9605f2d76cee42b13597e35b0eb7652e9e2723b952d91e0e09da1f63745633` después; iguales: False.
- **Los `.pyc`:** 11.236 líneas en el paso 0 y 11.236 después; listas iguales: True.

**El sha256 de los archivos de este tramo, de la foto de después:**

| archivo | sha256 |
|---|---|
| `data/experiment/tanda_final/t4/ampliacion/consola_sorteo_ampliacion_corrida1.txt` | `c382d62101f7dc3b98904a721e338446034444c60d0db2f98f9bbc491a30afdc` |
| `data/experiment/tanda_final/t4/ampliacion/consola_tablas_ampliacion_t4t2_tf.txt` | `2c8402364eca04b883b1b3322ff1dc9229b855da0f5f6842b27e026aca1327e4` |
| `data/experiment/tanda_final/t4/ampliacion/consola_unidades_a_la_vista_ampliacion_t4t2_tf.txt` | `e376fe7f500b930aee132125956244d05d3871841b9e78d74d812e4c264e6505` |
| `data/experiment/tanda_final/t4/ampliacion/lectura_asistida/borradores/aceptadas_no_items_ampliacion.jsonl` | `efb477c8064b2250ecd0f94ecb666be09308229197c43a38ca3284cc5a474623` |
| `data/experiment/tanda_final/t4/ampliacion/lectura_asistida/consola_armar_lectura_ampliacion_t4t2.txt` | `f449ad169a11b734a4283dd883041431d03e390ff36a11fc7cb0d0af3ba2b41b` |
| `data/experiment/tanda_final/t4/ampliacion/lectura_asistida/lectura_asistida_t4_ampliacion.json` | `58ce4f91c75b32bfb53adbf66b9f8acfe65818eb138fba68c29e58a9a54a2ead` |
| `data/experiment/tanda_final/t4/ampliacion/lectura_asistida/omisiones_y_observaciones_t4_ampliacion.md` | `c43729757456d9cfbcd0355efdf1e678e9cdfe6de5fef4542be92c89da48cfcc` |
| `data/experiment/tanda_final/t4/ampliacion/lectura_autora/aceptadas_no_items_ampliacion.csv` | `e99eaa2c347fe95a345dc63b26208f8681e28c2daf894e120e947d2855ff2331` |
| `data/experiment/tanda_final/t4/ampliacion/material/aceptadas_no_items_ampliacion/fichas_aceptadas_no_items_ampliacion.jsonl` | `9c396359c23ef4f854561301ef571d410ea8765847ea9aaa6d718b1f7fd84f5d` |
| `data/experiment/tanda_final/t4/ampliacion/material/aceptadas_no_items_ampliacion/fichas_aceptadas_no_items_ampliacion.md` | `c52d8351c92706b2f74d2b4f5c2caa321d827e8dc1ac2c74a7b1bd937214cec3` |
| `data/experiment/tanda_final/t4/ampliacion/material/aceptadas_no_items_ampliacion/planilla_aceptadas_no_items_ampliacion.csv` | `e5d18dc310b4be536c95647cb23ecddc3691728f9b7613b08d30eafbded477da` |
| `data/experiment/tanda_final/t4/ampliacion/material/consola_material_ampliacion_t4t2_tf.txt` | `ea1038cd7e49ed9604852bc32f6fa9b9435d0871754439670db57e0533b78cfd` |
| `data/experiment/tanda_final/t4/ampliacion/material/control_material_ampliacion_t4t2_tf.json` | `ce606e9141b1ec814fdc5a38439c1763a1b905eb0df1d59954bcfbc0c6d6ce50` |
| `data/experiment/tanda_final/t4/ampliacion/material/material_ampliacion_t4t2_tf.json` | `7ed12b626018cedddb9a5375c3cb31c0fea355d4fd70b975b29858c071c9e68d` |
| `data/experiment/tanda_final/t4/ampliacion/muestras/aceptadas_no_items_ampliacion.json` | `d8c8c337a96a9531c24a1d3a2673c264f8e137eaea897a88965c5fd75bca5726` |
| `data/experiment/tanda_final/t4/ampliacion/muestras/sorteo_ampliacion_t4t2_tf.json` | `e32c0dd710e3925d527964667c0473b44ef0969772fba373b2890b4185cad856` |
| `data/experiment/tanda_final/t4/ampliacion/segunda_corrida_del_sorteo/aceptadas_no_items_ampliacion.json` | `d8c8c337a96a9531c24a1d3a2673c264f8e137eaea897a88965c5fd75bca5726` |
| `data/experiment/tanda_final/t4/ampliacion/segunda_corrida_del_sorteo/consola_sorteo_ampliacion_corrida2.txt` | `c382d62101f7dc3b98904a721e338446034444c60d0db2f98f9bbc491a30afdc` |
| `data/experiment/tanda_final/t4/ampliacion/segunda_corrida_del_sorteo/sorteo_ampliacion_t4t2_tf.json` | `e32c0dd710e3925d527964667c0473b44ef0969772fba373b2890b4185cad856` |
| `data/experiment/tanda_final/t4/ampliacion/tablas_ampliacion_t4t2.md` | `0cce66f7288732e969753a4f77b637877e23eabbfc056b2ae8a2c80ff509e3a8` |
| `data/experiment/tanda_final/t4/consola_tablas_t4t2_tf.txt` | `385fed1946c67a0487d27f31b22ecf86559c57cb596383fd66029cb71d5821d6` |
| `data/experiment/tanda_final/t4/tablas_t4_tramo2.md` | `0e17acbef0deeb0009ffcfe2e02ccc5a51044a99b4a65b41c94fb323be9dd595` |
| `data/experiment/tanda_final/t4/tasas/consola_tasas_t4t2_tf.txt` | `3622656380da2de61c4a8378d09367ed03627af48fcfe639431c282cefc045fa` |
| `data/experiment/tanda_final/t4/tasas/consola_verif_tasas_independiente_t4t2_tf.txt` | `e026237a8db9b0c11b0bf37d35c4133329615b9648fe5794a305ef7ec5eece0b` |
| `data/experiment/tanda_final/t4/tasas/distribuciones_bajo_H0_t4_tramo2.json` | `e1f4e1e517ae7f597400634f97aa9919c18db1836d73e7099ca2db824b8d9924` |
| `data/experiment/tanda_final/t4/tasas/tasas_t4_tramo2.json` | `cbe7f0def90a8431a9f158f55bfe731308596c5325aefd8b4e7ce5029e1a2e3c` |
| `data/experiment/tanda_final/t4/tasas/umbrales_t4_por_celdas_mesa_al_importar_t4t2_tf.json` | `9a81ead83e7d7d9765916e2ee72f346b494554146de4f9c2445a3cf1db46a009` |
| `data/experiment/tanda_final/t4/tasas/verif_tasas_independiente_t4t2_tf.json` | `bc5c99524ae19d286bea1600b97125352fd2ffe43f489f9e1179650a5faf1706` |

**Los scripts de este tramo** (`t4/scripts/`, sha256 de la foto de después):

| script | sha256 |
|---|---|
| `anotar_ampliacion_t4t2.py` | `f421b68ad7e7ff44416b91b50cfc6e1e78dfe59c9f1f4195cd62dd3489982684` |
| `armar_lectura_ampliacion_t4t2.py` | `2c9c794412a7d51d530b27f36492215e5132e600a4783b3a82ba8dc83e9da8b0` |
| `control_material_ampliacion_t4t2_tf.py` | `91d9cf8cecf3e1f4b9825f88552ea6caa26a9d15f671ff19d48e89efc8a23b15` |
| `freno_t4t2_foto_tf.py` | `e1996e3661292a0512f1b7c63109fa46ff53f0dc3909785c7a22fa8b637a3112` |
| `material_ampliacion_t4t2_tf.py` | `cb744fab87d9f3549ad45c4141481f461b07129b395eead637992d73639c8b40` |
| `sorteo_ampliacion_t4t2_tf.py` | `d26ca90be28a9cdd9782f0fa0bc5840f1bed0e8ed879b4664836798d036e2948` |
| `tablas_ampliacion_t4t2_tf.py` | `3a86291980306a501379e25e01103a599298864464614bf3a23854f3a6c906b5` |
| `tablas_t4t2_tf.py` | `a7f638085de4a818472e852a327d41e71affbb57f19dda78655fcf06c451ee58` |
| `tasas_t4t2_tf.py` | `11176b042416e966d4999d127fe0c9fd062c61696cb1bd2a65b9548d29c4b55e` |
| `unidades_a_la_vista_ampliacion_t4t2_tf.py` | `217d03db6bb1a6e40b18a29d25356bd43a44d315746b8bc3825104ac64e931f5` |
| `verif_tasas_independiente_t4t2_tf.py` | `5ebad731972075827833c4c0b0ee1d4fe29dff8568a3d9df3f8491702c3487c0` |

- **El grep de convenciones** (`t3/scripts/grep_convenciones_tf.py`, sin cambios, con `LC_ALL=en_US.UTF-8`) sobre los 40 archivos nuevos o cambiados de la foto: 0 coincidencias de los tokens del nombre y de los términos, 0 archivos con rutas absolutas, 0 tokens dentro de rutas absolutas; control positivo, 2. Su salida va en el paquete. Este FRENO y su script se escriben después de la foto: el control final del paquete confirma que son lo único nuevo desde ella y les pasa el grep.
- **La copia del repo** (para el material y la lista de la ampliación) es la del `rsync` de la cláusula más una exclusión que la cláusula no trae, `--exclude=/data/experiment/neo4j/volumen` (sección 14, punto 2). El control da 0 nombres vedados y 0 enlaces; el log del `rsync` tiene 336 líneas, todas «skipping non-regular file» (los enlaces que `--no-links` no copia). El control y el log van en el paquete. Ningún `git clone`.

## 13. El script de cada cifra

| cifras | script (`t4/scripts/`) | salida |
|---|---|---|
| las tasas, la atención, el freno, la sensibilidad, la ampliación (secciones 2 a 7) | `tasas_t4t2_tf.py` | `tasas/tasas_t4_tramo2.json`, `tasas/distribuciones_bajo_H0_t4_tramo2.json`, `tasas/consola_tasas_t4t2_tf.txt` |
| la verificación independiente de las tasas | `verif_tasas_independiente_t4t2_tf.py` | `tasas/verif_tasas_independiente_t4t2_tf.json`, su consola |
| las tablas 1 a 9 y las cifras para la hoja (secciones 3 a 6 y 9) | `tablas_t4t2_tf.py` | `tablas_t4_tramo2.md`, `consola_tablas_t4t2_tf.txt` |
| el sorteo de la ampliación y sus dos corridas | `sorteo_ampliacion_t4t2_tf.py` | `ampliacion/muestras/`, `ampliacion/segunda_corrida_del_sorteo/`, `ampliacion/consola_sorteo_ampliacion_corrida1.txt` |
| el material de la ampliación y su control | `material_ampliacion_t4t2_tf.py`, `control_material_ampliacion_t4t2_tf.py` | `ampliacion/material/` |
| la lista de unidades a la vista | `unidades_a_la_vista_ampliacion_t4t2_tf.py` | `../t3/muestras/unidades_a_la_vista_T4.json`, `ampliacion/consola_unidades_a_la_vista_ampliacion_t4t2_tf.txt` |
| la lectura asistida y la planilla de la autora | `anotar_ampliacion_t4t2.py`, `armar_lectura_ampliacion_t4t2.py` | `ampliacion/lectura_asistida/`, `ampliacion/lectura_autora/` |
| las tablas A1 a A5 (sección 8) | `tablas_ampliacion_t4t2_tf.py` | `ampliacion/tablas_ampliacion_t4t2.md` y su consola |
| la foto (sección 12) | `freno_t4t2_foto_tf.py` | la sección 12; su salida, en el paquete |
| el texto de este FRENO | `freno_t4t2_armar_tf.py` | este archivo |
| el paso 0 repetido (sección 1) | `paso0_bis_t4_tramo2.sh` y `foto_contra_t4_tramo2.py`, en el paquete | su salida, pegada |

- **Los controles de la entrada** de `tasas_t4t2_tf.py`: 41 de 41 pasan (están en la salida, `controles`).
- **La verificación independiente** recuenta las marcadas sin el código de la mesa y recalcula las tasas, los Wilson y los p-valores por convolución exacta con fracciones: 32 de 32 cifras iguales, 0 distintas.
- **Cómo salieron los scripts:** `tasas_t4t2_tf.py`, `tablas_t4t2_tf.py`, `freno_t4t2_foto_tf.py`, `material_ampliacion_t4t2_tf.py` y `armar_lectura_ampliacion_t4t2.py` los escribieron adaptadores con reemplazos exactos (`adaptar_*_t4_tramo2.py`, en el paquete) desde los de la tanda 1 o los del primer tramo y T3; `freno_t4t2_armar_tf.py` lo escribí desde el de la tanda 1. Los diffs enteros de los cuatro del «seguí» contra los de la tanda 1 van en el anexo.

## 14. Errores propios, con su causa

1. **La foto de después del primer tramo quedó solo en `/private/tmp` y se perdió.** Está declarado en la sección 5 de `FRENO_T4_tramo2_paso0.md`, del paquete `revision_tanda_final_FRENO_T4_tramo2_paso0/`; lo reemplazó el control sustituto (`control_sustituto_foto_t4_tramo2.py`, `control_sustituto_foto_T4_tramo2.json`), y la salida del paso 0 es `paso0_T4_tramo2_salida.txt`, de `paso0_t4_tramo2.sh`. La causa: dejé la foto fuera del paquete porque nombra todas las rutas del repo, y no la guardé en otro lugar permanente. Desde este tramo, las fotos van a `t4t2_fotos/`, en la carpeta permanente: la de las 12:16:33, la del paso 0 repetido, la de después y la final del paquete.
2. **La copia del repo lleva una exclusión que la cláusula no trae:** `--exclude=/data/experiment/neo4j/volumen`, la base de Neo4j, fuera de git. La agregué sin que el mandato la autorizara. Ninguno de los tres scripts que corrieron sobre la copia la lee (no nombran Neo4j), así que no cambia ninguna salida; el control de la copia dio 0 de todos modos. Lo declaro para que la mesa decida.
3. **La primera corrida del sorteo no arrancó.** La consola iba a `t4/ampliacion/`, que todavía no existía, y el shell frenó antes de correr el script; la segunda corrida, a la carpeta de trabajo, sí corrió (dio el mismo sha256 de la muestra). Borré esa salida, creé la carpeta y corrí las dos en orden: la del repo y la segunda, que copié a `t4/ampliacion/segunda_corrida_del_sorteo/`. Las tres dan los mismos bytes (tabla A2).
4. **Dos textos de `lineas_de_base` dicen «umbrales_t4_tf,json».** En `tasas_t4t2_tf.py`, el `.replace(".", ",")` de la coma decimal se aplica a toda la cadena, con el nombre del archivo (las líneas de `aceptadas:total` y `atencion_RI`). Las cifras están bien. No volví a correr las tasas: el índice del sorteo guarda el sha256 de su salida, y las tablas arman esas celdas desde los campos numéricos. Lo vi al armar las tablas.
5. **Tres controles de mis adaptadores frenaron antes de escribir.** El de `adaptar_tasas_t4_tramo2.py` y el de `adaptar_tablas_t4_tramo2.py` marcaban menciones legítimas de la tanda 1 (la ruta del script de la mesa y la del script de origen en la cabecera); el de `adaptar_foto_t4_tramo2.py` encontró un `endswith(".DS_Store")` que ningún reemplazo cubría. Corregí la lista o agregué el reemplazo y volví a correr; ningún destino estaba escrito.

## 15. Lo que no hice

- **T5 ni las FICHAS**, ni las tasas sobre las 60.
- **Lo que no toqué:** las marcadas, las exportaciones, el sello, las planillas del primer tramo, el LEEME, el convertidor y el control de la mesa; los grafos, los manifiestos, la E0, el código del pipeline, la fixture, `grafos.py`, Neo4j, el backlog y el registro de alcance. De `t3/` solo cambié `t3/muestras/unidades_a_la_vista_T4.json` (punto 5).
- **Commits y escrituras ajenas:** no commiteé ni preparé mensajes de commit; no escribí en la memoria, en `.claude/` ni en `.gitignore`.
- **El scratchpad:** nada que se necesite después queda solo en él. El paquete y su copia permanente llevan los scripts del paso 0 repetido, los adaptadores, la sección de la foto, el grep, el control y el log de la copia; las fotos van a `t4t2_fotos/`.
- Los heredocs, siempre con el delimitador entre comillas.

FRENO T4, segundo tramo. Espero la revisión de la mesa.

## Anexo. Los diffs enteros de los cuatro scripts contra los de la tanda 1

Con `difflib.unified_diff`, sin líneas de contexto (`n=0`): cada bloque trae todo lo que cambia.

### `tasas_t4t2.py` → `tasas_t4t2_tf.py` (139 líneas cambiadas)

```diff
--- tanda1/t4/scripts/tasas_t4t2.py
+++ tanda_final/t4/scripts/tasas_t4t2_tf.py
@@ -1,3 +1,6 @@
-"""B6.1, tanda 1, T4, segundo tramo, puntos 2 y 4: las tasas, la atención y el freno, sobre la lectura sellada de la autora, con el
-pre-registro firmado (§5.4 a y b, v8b y v8c; §5.4 bis, punto 2) y los umbrales que T3 calculó con los pesos reales antes de leer
-(t3/muestras/umbrales_t4_reales.json). Solo lee y calcula; corre sobre una copia. No lee el grafo, ni estados de E3, ni reintentos.
+"""B6.1, tanda final, T4, segundo tramo, puntos 4 y 5 del «seguí»: las tasas, la atención y el freno, sobre la lectura sellada de la
+autora, con el pre-registro firmado (docs/preregistro_tanda_final.md, firma en 4de7f2a7, §6), su versión derivada para la lectura
+(tanda_final/preregistro/preregistro_tanda_final_derivada_T4.md) y los umbrales que T3 calculó con los pesos reales
+(t3/muestras/umbrales_t4_tf.json). Es tanda1/t4/scripts/tasas_t4t2.py con las rutas, los nombres y los umbrales de la tanda final, y con
+las líneas de base de la versión derivada. Solo lee y calcula; escribe solo en <trabajo>, <salida.json> y <distribuciones.json>. No lee el
+grafo, ni estados de E3, ni reintentos.
@@ -7 +10 @@
-       - umbrales_t4_reales.json tiene el sha256 del mandato;
+       - umbrales_t4_tf.json tiene el sha256 del «seguí»; la versión derivada y su .huecos.json, los de T3;
@@ -9 +12 @@
-         (t3/scripts/umbrales_t4_t3f.py), y su salida al importarse es byte a byte su JSON. De él salen wilson, pmf, cola_sup,
+         (t3/scripts/umbrales_t4_tf.py), y su salida al importarse es byte a byte su JSON. De él salen wilson, pmf, cola_sup,
@@ -11,10 +14,12 @@
-       - cada marcada tiene, por celda, los mismos ids que su muestra (t3/muestras/ o t4/muestras/), y cada veredicto es válido;
-       - las N por celda de umbrales_t4_reales.json son las de t3/muestras/poblaciones_t4.json, y las n por celda son las de la muestra.
-  2. La regla de las dudosas (decisión de la autora del 18/10/2026): en la cola y en las dos de las aceptadas, «dudosa» cuenta como error
-     para la tasa, la atención y el freno. La misma cuenta con las dudosas fuera, sobre las decididas, va al lado como sensibilidad y no
-     decide nada; si diera otra decisión de atención o de freno, se declara, y rige la primera.
-  3. Las aceptadas, por estrato (§5.4 a, v8b): T = suma w_c k_c / n_c, con w_c = N_c / N (umbrales_t4_reales.json); Wilson al 95 % con
-     n_ef = 1 / suma w_c^2 / n_c; la atención, P(T' >= T) bajo H0 (cada celda en la tasa de la tanda 0 del estrato) con la distribución
-     de T' enumerada entera (`distribucion` de la mesa), y salta si es <= 0,05; el freno por intervalos, si el límite inferior del Wilson
-     de T pasa el superior del Wilson de la tanda 0 (la misma comparación que `umbrales` de la mesa). El freno por la atención sobre las
-     60 solo se mira en un tercer tramo, si hay ampliación.
+       - cada marcada tiene, por celda, los mismos ids que su muestra (t3/muestras/), y cada veredicto es válido;
+       - las N por celda de umbrales_t4_tf.json son las de t3/muestras/poblaciones_t4_t3f_tf.json (aceptadas, cola, (2) y (7)) y las de
+         t3/muestras/poblaciones_t4t1_tf.json ((1), (3) y (12)), y las n por celda son las de la muestra;
+       - cada línea de base de la tanda 1 (los valores T4.* del .huecos.json de la versión derivada) está tal cual en la versión derivada.
+  2. La regla de las dudosas (pre-registro, §6; registro, §35): en la cola y en las dos de las aceptadas, «dudosa» cuenta como error para
+     la tasa, la atención y el freno. La misma cuenta con las dudosas fuera, sobre las decididas, va al lado como sensibilidad y no decide
+     nada; si diera otra decisión de atención o de freno, se declara, y rige la primera.
+  3. Las aceptadas, por estrato: T = suma w_c k_c / n_c, con w_c = N_c / N (umbrales_t4_tf.json); Wilson al 95 % con
+     n_ef = 1 / suma w_c^2 / n_c; la atención, P(T' >= T) bajo H0 (cada celda en la tasa de la tanda 0 del estrato, la base del script
+     sellado) con la distribución de T' enumerada entera (`distribucion` de la mesa), y salta si es <= 0,05; el freno por intervalos, si
+     el límite inferior del Wilson de T pasa el superior del Wilson de la tanda 0 (la misma comparación que `umbrales` de la mesa). El
+     freno por la atención sobre las 60 solo se mira en un tercer tramo, si hay ampliación.
@@ -22,4 +27,4 @@
-     La atención propia de RI (v8c): t = suma v k / n en las cuatro celdas RI de los dos estratos, v = N_(s,c) / N_RI, con el test exacto
-     de `atencion_ri` de T3 (cada celda bajo H0 en la tasa de la tanda 0 de su estrato). NG sin_raiz, por celda y sin umbral.
-  4. La cola (§5.4 b, v8b): la ponderada por celda con los pesos de la cola, su Wilson con n_ef y la regla del 25 % (se dispara si el
-     límite superior pasa 0,25; enmienda de la cola humana, §1, punto 6), como cifra y vigilancia.
+     La atención propia de RI: t = suma v k / n en las cuatro celdas RI de los dos estratos, v = N_(s,c) / N_RI, con el test exacto de
+     `atencion_ri` de T3 (cada celda bajo H0 en la tasa de la tanda 0 de su estrato). NG sin_raiz, por celda y sin umbral.
+  4. La cola: la ponderada por celda con los pesos de la cola, su Wilson con n_ef y la regla del 25 % (se dispara si el límite superior
+     pasa 0,25), como cifra y vigilancia, no como freno.
@@ -30,4 +35,5 @@
-     incorrectas, por capa_pipeline. Los pesos de la (1), la (3) y la (12) son los de t4/muestras/poblaciones_t4_tramo1.json (la (12),
-     con el universo de la decisión 1.2 del 18/10/2026, no el de A4.1 que trae umbrales_t4_reales.json). La (7) se leyó entera, sin
-     celdas: solo la cruda.
-Uso: python3 -I -B tasas_t4t2.py <raíz> <trabajo> <salida.json> <distribuciones.json>
+     incorrectas, por capa_pipeline. Los pesos de la (1), la (3) y la (12) son los de t3/muestras/poblaciones_t4t1_tf.json (la (12), con
+     las aristas de extracción de la (10), sin remite_a). La (7) se leyó entera, sin celdas: solo la cruda.
+  6. Cada cifra con su línea de base: la de la tanda 1, de la versión derivada, con la de la tanda 0 al lado (la base del script de la
+     mesa, la de la cola de umbrales_t4_tf.json y las de la tanda 0 que dan los scripts del segundo tramo de la tanda 1).
+Uso: python3 -I -B tasas_t4t2_tf.py <raíz> <trabajo> <salida.json> <distribuciones.json>
@@ -51,4 +57,8 @@
-T1 = RAIZ / "data/experiment/tanda1"
-LA = T1 / "t4/lectura_autora"
-UMBRALES = T1 / "t3/muestras/umbrales_t4_reales.json"
-UMBRALES_SHA = "687c760a13a854194dc91ae82b7b5110e860dfcd52c39bea65d6d8faf6b4691f"
+TF = RAIZ / "data/experiment/tanda_final"
+LA = TF / "t4/lectura_autora"
+UMBRALES = TF / "t3/muestras/umbrales_t4_tf.json"
+UMBRALES_SHA = "d7f7860fbf09f92443992aeb9915e22191582cfe2edaf5fd0a089baadd3ac555"
+DERIVADA = TF / "preregistro/preregistro_tanda_final_derivada_T4.md"
+DERIVADA_SHA = "26c29d9424ffaf634a02735a972ad29e7df8b06463b8ad430654d50d4d442fc2"
+HUECOS = TF / "preregistro/preregistro_tanda_final_derivada_T4.huecos.json"
+HUECOS_SHA = "4a17612bcf069beee9b00f513c6b69b7f4b0fa81b7ba590052f79d318b3862e4"
@@ -63,8 +73,8 @@
-    "cola": ("cola", T1 / "t3/muestras/cola.json", ["con error", "sin error", "dudosa"]),
-    "aceptadas:items": ("aceptadas_items", T1 / "t3/muestras/aceptadas_items.json", ["con error", "sin error", "dudosa"]),
-    "aceptadas:no_items": ("aceptadas_no_items", T1 / "t3/muestras/aceptadas_no_items.json", ["con error", "sin error", "dudosa"]),
-    "vigilancia:2": ("vigilancia_2", T1 / "t3/muestras/vigilancia_2.json", ["vaciamiento", "no vaciamiento", "no decidible"]),
-    "vigilancia:7": ("vigilancia_7", T1 / "t3/muestras/vigilancia_7.json", ["con apoyo", "sin apoyo", "no decidible"]),
-    "vigilancia:1": ("vigilancia_1", T1 / "t4/muestras/vigilancia_1.json", ["sí", "no", "no decidible"]),
-    "vigilancia:3": ("vigilancia_3", T1 / "t4/muestras/vigilancia_3.json", ["duplicación", "distintos"]),
-    "observacion:12": ("observacion_12", T1 / "t4/muestras/observacion_12.json", None),
+    "cola": ("cola", TF / "t3/muestras/cola.json", ["con error", "sin error", "dudosa"]),
+    "aceptadas:items": ("aceptadas_items", TF / "t3/muestras/aceptadas_items.json", ["con error", "sin error", "dudosa"]),
+    "aceptadas:no_items": ("aceptadas_no_items", TF / "t3/muestras/aceptadas_no_items.json", ["con error", "sin error", "dudosa"]),
+    "vigilancia:2": ("vigilancia_2", TF / "t3/muestras/vigilancia_2.json", ["vaciamiento", "no vaciamiento", "no decidible"]),
+    "vigilancia:7": ("vigilancia_7", TF / "t3/muestras/vigilancia_7.json", ["con apoyo", "sin apoyo", "no decidible"]),
+    "vigilancia:1": ("vigilancia_1", TF / "t3/muestras/vigilancia_1.json", ["sí", "no", "no decidible"]),
+    "vigilancia:3": ("vigilancia_3", TF / "t3/muestras/vigilancia_3.json", ["duplicación", "distintos"]),
+    "observacion:12": ("observacion_12", TF / "t3/muestras/observacion_12.json", None),
@@ -85 +95,3 @@
-controles["umbrales_t4_reales.json tiene el sha256 del mandato"] = sha(UMBRALES) == UMBRALES_SHA
+controles["umbrales_t4_tf.json tiene el sha256 del «seguí»"] = sha(UMBRALES) == UMBRALES_SHA
+controles["la versión derivada tiene el sha256 de T3"] = sha(DERIVADA) == DERIVADA_SHA
+controles["el .huecos.json de la versión derivada tiene el sha256 de T3"] = sha(HUECOS) == HUECOS_SHA
@@ -87 +99 @@
-control_out = W / "umbrales_t4_por_celdas_mesa_al_importar_t4t2.json"
+control_out = W / "umbrales_t4_por_celdas_mesa_al_importar_t4t2_tf.json"
@@ -99,3 +111,3 @@
-POB3 = json.loads((T1 / "t3/muestras/poblaciones_t4.json").read_text(encoding="utf-8"))["muestras"]
-POB4 = json.loads((T1 / "t4/muestras/poblaciones_t4_tramo1.json").read_text(encoding="utf-8"))["muestras"]
-controles["las N por celda de umbrales_t4_reales.json son las de t3/muestras/poblaciones_t4.json"] = all(
+POB3 = json.loads((TF / "t3/muestras/poblaciones_t4_t3f_tf.json").read_text(encoding="utf-8"))["muestras"]
+POB4 = json.loads((TF / "t3/muestras/poblaciones_t4t1_tf.json").read_text(encoding="utf-8"))["muestras"]
+controles["las N por celda de umbrales_t4_tf.json son las de t3/muestras/poblaciones_t4_t3f_tf.json"] = all(
@@ -104,0 +117,6 @@
+controles["las N por celda de umbrales_t4_tf.json son las de t3/muestras/poblaciones_t4t1_tf.json"] = all(
+    U["otras"][m]["N_por_celda"] == POB4[m]["N_por_celda"] for m in ("vigilancia:1", "vigilancia:3", "observacion:12"))
+HU = json.loads(HUECOS.read_text(encoding="utf-8"))["valores"]
+DER = DERIVADA.read_text(encoding="utf-8")
+controles["las líneas de base de la tanda 1 (T4.*) están tal cual en la versión derivada"] = all(
+    HU[k]["valor"] in DER for k in HU if k.startswith("T4."))
@@ -132 +150 @@
-    controles[f"aceptadas:{s}: las n por celda son las de umbrales_t4_reales.json"] = \
+    controles[f"aceptadas:{s}: las n por celda son las de umbrales_t4_tf.json"] = \
@@ -134 +152 @@
-controles["cola: las n por celda son las de umbrales_t4_reales.json"] = L["cola"]["muestra"]["n_por_celda"] == U["cola"]["n_por_celda"]
+controles["cola: las n por celda son las de umbrales_t4_tf.json"] = L["cola"]["muestra"]["n_por_celda"] == U["cola"]["n_por_celda"]
@@ -136 +154 @@
-    controles[f"{m}: las N por celda de la muestra son las de poblaciones_t4_tramo1.json"] = \
+    controles[f"{m}: las N por celda de la muestra son las de poblaciones_t4t1_tf.json"] = \
@@ -139 +157 @@
-    controles[f"{m}: las N por celda de la muestra son las de umbrales_t4_reales.json"] = \
+    controles[f"{m}: las N por celda de la muestra son las de umbrales_t4_tf.json"] = \
@@ -183 +201 @@
-    "con las dudosas fuera, sobre las decididas, va al lado como sensibilidad y no decide nada (decisión de la autora del 18/10/2026)"),
+    "con las dudosas fuera, sobre las decididas, va al lado como sensibilidad y no decide nada (pre-registro, §6; registro, §35)"),
@@ -306 +324 @@
-                                    "distintos (decisión de la autora del 18/10/2026, punto 1.4; registro de decisiones, §29)")
+                                    "distintos (registro de decisiones, §29; LEEME de la lectura de T4)")
@@ -338,2 +356,2 @@
-    "pesos_de": "t4/muestras/poblaciones_t4_tramo1.json (universo de la decisión 1.2, 18.483 aristas); no los de A4.1 de umbrales_t4_reales.json",
-    "linea_de_base_tanda0": "25 de 30, Wilson [0,664; 0,927], con el perfil anterior (pre-registro, §5.2)"}
+    "pesos_de": "t3/muestras/poblaciones_t4t1_tf.json (las aristas de extracción de la (10), sin remite_a, en el grafo sin cola de la tanda)",
+    "linea_de_base_tanda0": "25 de 30, Wilson [0,664; 0,927], con el perfil anterior (pre-registro de la tanda 1, §5.2, como lo da tanda1/t4/scripts/tasas_t4t2.py)"}
@@ -346,3 +364,22 @@
-res["entradas"] = {"umbrales_t4_reales.json": UMBRALES_SHA, "umbrales_t4_por_celdas_mesa.py": sha(MESA),
-                   "poblaciones_t4.json (t3)": sha(T1 / "t3/muestras/poblaciones_t4.json"),
-                   "poblaciones_t4_tramo1.json (t4)": sha(T1 / "t4/muestras/poblaciones_t4_tramo1.json"),
+# 6. Las líneas de base: la tanda 1, de la versión derivada, y la tanda 0 al lado
+b0 = lambda s: f"{RU.BASE[s]['k']} de {RU.BASE[s]['n']}, Wilson [{RU.BASE[s]['wilson'][0]:.4f}; {RU.BASE[s]['wilson'][1]:.4f}]".replace(".", ",")  # noqa: E731
+t0 = U["tasa_ponderada_total"]["tanda0_con_el_mismo_metodo"]
+res["lineas_de_base"] = {
+    "fuente_tanda1": "los valores T4.* de tanda_final/preregistro/preregistro_tanda_final_derivada_T4.huecos.json (versión derivada para la lectura)",
+    "aceptadas:items": {"tanda1": HU["T4.aceptadas_items"]["valor"], "tanda0": b0("items") + " (BASE del script de la mesa)"},
+    "aceptadas:no_items": {"tanda1": HU["T4.aceptadas_no_items"]["valor"], "tanda0": b0("no_items") + " (BASE del script de la mesa)"},
+    "aceptadas:total": {"tanda1": HU["T4.ponderada_total"]["valor"],
+                        "tanda0": f"{t0['p']:.4f}, Wilson [{t0['wilson'][0]:.4f}; {t0['wilson'][1]:.4f}], mismo método (umbrales_t4_tf.json)".replace(".", ",")},
+    "atencion_RI": {"tanda1": HU["T4.atencion_RI"]["valor"],
+                    "tanda0": f"la tasa de RI bajo H0, con las tasas de la tanda 0: {U['atencion_RI']['tasa_de_RI_bajo_H0']:.4f} (umbrales_t4_tf.json)".replace(".", ",")},
+    "cola": {"tanda1": HU["T4.cola"]["valor"], "tanda0": U["cola"]["base_tanda0"]},
+    "vigilancias_y_12": {"tanda1": HU["T4.vigilancias_y_12"]["valor"],
+                         "tanda0": {"vigilancia:1": "no se midió en la tanda 0", "vigilancia:3": "no se midió en la tanda 0",
+                                    "vigilancia:2": "en la tanda 0 se midió la población, sin leer la muestra",
+                                    "vigilancia:7": "en la tanda 0 se midió la población, sin leer la muestra",
+                                    "observacion:12": res["observacion:12"]["linea_de_base_tanda0"],
+                                    "fuente": "tanda1/t4/scripts/tablas_t4t2.py (BASEV) y tasas_t4t2.py"}}}
+res["entradas"] = {"umbrales_t4_tf.json": UMBRALES_SHA, "umbrales_t4_por_celdas_mesa.py": sha(MESA),
+                   "preregistro_tanda_final_derivada_T4.md": DERIVADA_SHA, "preregistro_tanda_final_derivada_T4.huecos.json": HUECOS_SHA,
+                   "poblaciones_t4_t3f_tf.json (t3)": sha(TF / "t3/muestras/poblaciones_t4_t3f_tf.json"),
+                   "poblaciones_t4t1_tf.json (t3)": sha(TF / "t3/muestras/poblaciones_t4t1_tf.json"),
```

### `tablas_t4t2.py` → `tablas_t4t2_tf.py` (64 líneas cambiadas)

```diff
--- tanda1/t4/scripts/tablas_t4t2.py
+++ tanda_final/t4/scripts/tablas_t4t2_tf.py
@@ -1,4 +1,6 @@
-"""B6.1, tanda 1, T4, segundo tramo, puntos 6 y 8: las cifras para la hoja de la revisión entre tandas y las tablas del FRENO, por
-script, desde la salida de tasas_t4t2.py (<raíz>/data/experiment/tanda1/t4/tasas/tasas_t4_tramo2.json). Solo lee; escribe
-tanda1/t4/tablas_t4_tramo2.md bajo <raíz> y la imprime. Los números van con coma decimal; los intervalos, como [inferior; superior].
-Uso: python3 -I -B tablas_t4t2.py <raíz>
+"""B6.1, tanda final, T4, segundo tramo: las cifras para la hoja de la revisión entre tandas y las tablas del FRENO, por script, desde la
+salida de tasas_t4t2_tf.py (<raíz>/data/experiment/tanda_final/t4/tasas/tasas_t4_tramo2.json). Es tanda1/t4/scripts/tablas_t4t2.py con
+las rutas de la tanda final y, en la tabla 1, la línea de base de la tanda 1 (los valores T4.* de la versión derivada, que tasas_t4t2_tf.py
+guarda en `lineas_de_base`) al lado de la de la tanda 0. Solo lee; escribe tanda_final/t4/tablas_t4_tramo2.md bajo <raíz> y la imprime.
+Los números van con coma decimal; los intervalos, como [inferior; superior].
+Uso: python3 -I -B tablas_t4t2_tf.py <raíz>
@@ -7,0 +10 @@
+import re
@@ -13 +16 @@
-T4 = RAIZ / "data/experiment/tanda1/t4"
+T4 = RAIZ / "data/experiment/tanda_final/t4"
@@ -26,2 +29,7 @@
-w = [f"Salida: `tasas/tasas_t4_tramo2.json` ({X['hora']}, sha256 `{sha}`), de `scripts/tasas_t4t2.py`. Rutas relativas a "
-     "`data/experiment/tanda1/t4/`.", ""]
+LB = X["lineas_de_base"]
+# la tanda 1 de las vigilancias y de la (12) es un solo valor de la versión derivada: «(1) …; (2) …; (3) …; (7) …; (12) …»
+V1 = dict(re.findall(r"\((\d+)\) (.*?)(?=; \(\d+\) |$)", LB["vigilancias_y_12"]["tanda1"]))
+assert sorted(V1) == sorted(["1", "2", "3", "7", "12"]), V1
+V1 = {(f"vigilancia:{k}" if k != "12" else "12"): v for k, v in V1.items()}
+w = [f"Salida: `tasas/tasas_t4_tramo2.json` ({X['hora']}, sha256 `{sha}`), de `scripts/tasas_t4t2_tf.py`. Rutas relativas a "
+     "`data/experiment/tanda_final/t4/`.", ""]
@@ -31 +39,2 @@
-      "| fila | tanda 1 | línea de base | decisión | script y clave de la salida |", "|---|---|---|---|---|"]
+      "| fila | tanda final | línea de base: tanda 1 (versión derivada) | tanda 0 | decisión | script y clave de la salida |",
+      "|---|---|---|---|---|---|"]
@@ -34,0 +44 @@
+    lb1 = LB[f"aceptadas:{s}"]["tanda1"]
@@ -38,2 +48,2 @@
-             f"{iv(z['wilson'])} | {round(A[s]['p0_tanda0'] * 30)} de 30, Wilson {iv(A[s]['wilson_tanda0'])} | atención: {sn(r['atencion'])} "
-             f"(p {d(r['p_valor_atencion'])}); freno: {sn(r['freno_por_intervalos'])} | `scripts/tasas_t4t2.py`, {SAL}, `aceptadas.{s}` |")
+             f"{iv(z['wilson'])} | {lb1} | {round(A[s]['p0_tanda0'] * 30)} de 30, Wilson {iv(A[s]['wilson_tanda0'])} | atención: {sn(r['atencion'])} "
+             f"(p {d(r['p_valor_atencion'])}); freno: {sn(r['freno_por_intervalos'])} | `scripts/tasas_t4t2_tf.py`, {SAL}, `aceptadas.{s}` |")
@@ -43,2 +53,2 @@
-         f"{iv(t['sensibilidad_sin_dudosas']['wilson'])} | {d(t['tanda0_con_el_mismo_metodo']['p'])}, Wilson "
-         f"{iv(t['tanda0_con_el_mismo_metodo']['wilson'])} (mismo método) | sin umbral | `scripts/tasas_t4t2.py`, {SAL}, `aceptadas.total` |")
+         f"{iv(t['sensibilidad_sin_dudosas']['wilson'])} | {LB['aceptadas:total']['tanda1']} | {d(t['tanda0_con_el_mismo_metodo']['p'])}, Wilson "
+         f"{iv(t['tanda0_con_el_mismo_metodo']['wilson'])} (mismo método) | sin umbral | `scripts/tasas_t4t2_tf.py`, {SAL}, `aceptadas.total` |")
@@ -47 +57 @@
-         f"{d(r['n_efectivo_kish'], 3)}); sin las dudosas, {z['errores']} de {z['leidas']}, {d(z['tasa_ponderada_RI'])} | bajo H0, "
+         f"{d(r['n_efectivo_kish'], 3)}); sin las dudosas, {z['errores']} de {z['leidas']}, {d(z['tasa_ponderada_RI'])} | {LB['atencion_RI']['tanda1']} | bajo H0, "
@@ -49 +59 @@
-         f"`scripts/tasas_t4t2.py`, {SAL}, `atencion_RI` |")
+         f"`scripts/tasas_t4t2_tf.py`, {SAL}, `atencion_RI` |")
@@ -55,2 +65,2 @@
-         f"{C['base_tanda0']} | regla del 25 %: {'se dispara' if r['regla_del_25_se_dispara'] else 'no se dispara'} (cifra y vigilancia, no freno) | "
-         f"`scripts/tasas_t4t2.py`, {SAL}, `cola` |")
+         f"{LB['cola']['tanda1']} | {C['base_tanda0']} | regla del 25 %: {'se dispara' if r['regla_del_25_se_dispara'] else 'no se dispara'} (cifra y vigilancia, no freno) | "
+         f"`scripts/tasas_t4t2_tf.py`, {SAL}, `cola` |")
@@ -61,2 +71,2 @@
-         f"{d(O['ponderada_por_celda']['tasa'])} {iv(O['ponderada_por_celda']['wilson'])} | {O['linea_de_base_tanda0']} | sin umbral | "
-         f"`scripts/tasas_t4t2.py`, {SAL}, `observacion:12` |")
+         f"{d(O['ponderada_por_celda']['tasa'])} {iv(O['ponderada_por_celda']['wilson'])} | {V1['12']} | {O['linea_de_base_tanda0']} | sin umbral | "
+         f"`scripts/tasas_t4t2_tf.py`, {SAL}, `observacion:12` |")
@@ -65,2 +75 @@
-BASEV = {"vigilancia:1": "no se midió en la tanda 0", "vigilancia:3": "no se midió en la tanda 0",
-         "vigilancia:2": "en la tanda 0 se midió la población, sin leer la muestra", "vigilancia:7": "en la tanda 0 se midió la población, sin leer la muestra"}
+BASEV = {m: LB["vigilancias_y_12"]["tanda0"][m] for m in NOMV}
@@ -73,2 +82,2 @@
-             f"; cruda {d(x['cruda']['tasa'])}, Wilson {iv(x['cruda']['wilson'])}; {pond} | {BASEV[m]} | sin umbral | "
-             f"`scripts/tasas_t4t2.py`, {SAL}, `vigilancias.{m}` |")
+             f"; cruda {d(x['cruda']['tasa'])}, Wilson {iv(x['cruda']['wilson'])}; {pond} | {V1[m]} | {BASEV[m]} | sin umbral | "
+             f"`scripts/tasas_t4t2_tf.py`, {SAL}, `vigilancias.{m}` |")
@@ -80 +89,6 @@
-w.append(f"- **Los controles de la entrada** (`scripts/tasas_t4t2.py`): {sum(X['controles'].values())} de {len(X['controles'])} pasan.")
+if X["ampliacion"]["hay_ampliacion"]:
+    w.append("- **Lo que salta va a la ampliación:** " + ", ".join(k for k, v in X["ampliacion"]["salta"].items() if v) + ". Su fila de la "
+             "hoja queda con las 30 leídas: las tasas sobre las 60 (las 30 y las 30 de la ampliación) van en el tercer tramo, después de la "
+             "lectura de la autora.")
+w.append(f"- **Las líneas de base:** la tanda 1, {LB['fuente_tanda1']}; la tanda 0, al lado, la de cada fila de `lineas_de_base`.")
+w.append(f"- **Los controles de la entrada** (`scripts/tasas_t4t2_tf.py`): {sum(X['controles'].values())} de {len(X['controles'])} pasan.")
@@ -83 +97 @@
-w += ["", "#### Tabla 2. Las aceptadas por celda (`aceptadas.<estrato>.por_celda`; pesos de `t3/muestras/umbrales_t4_reales.json`)", "",
+w += ["", "#### Tabla 2. Las aceptadas por celda (`aceptadas.<estrato>.por_celda`; pesos de `t3/muestras/umbrales_t4_tf.json`)", "",
@@ -152 +166 @@
-w += ["", "#### Tabla 9. La observación (12), por celda (`observacion:12`; pesos de `muestras/poblaciones_t4_tramo1.json`)", "",
+w += ["", "#### Tabla 9. La observación (12), por celda (`observacion:12`; pesos de `t3/muestras/poblaciones_t4t1_tf.json`)", "",
```

### `freno_t4t2_foto.py` → `freno_t4t2_foto_tf.py` (60 líneas cambiadas)

```diff
--- tanda1/t4/scripts/freno_t4t2_foto.py
+++ tanda_final/t4/scripts/freno_t4t2_foto_tf.py
@@ -1,8 +1,10 @@
-"""B6.1, tanda 1, T4, segundo tramo: la sección de la foto del FRENO, por script, desde la foto del paso 0 y la de después
-(t2/foto_repo_tanda1_t2.py, crudas), las dos listas de .pyc y la salida de las tasas (si hubo ampliación). Solo lee; escribe <salida.md>
-(fuera del repo) y la imprime. Copia de freno_t4t1_foto.py con lo que admite el segundo tramo:
-  - lo nuevo, solo en tanda1/t4/; t3/muestras/unidades_a_la_vista_T4.json, solo si hubo ampliación; los .DS_Store van aparte
-    (indicación de la autora en el paso 0); lo demás es «fuera de lo admitido»;
-  - el NO_ABRIR_ del primer tramo, sin abrirlo: su tamaño y su hora en las dos fotos (la foto no lo abre);
-  - el sha256 de los archivos de este tramo y de cada script nuevo de tanda1/t4/scripts/, de la foto de después.
-Uso: python3 -I -B freno_t4t2_foto.py <foto_antes.json> <foto_despues.json> <pyc_antes.txt> <pyc_despues.txt> <tasas.json> <salida.md>
+"""B6.1, tanda final, T4, segundo tramo: la sección de la foto del FRENO, por script, desde la foto de las 12:16:33 (la del paso 0, que
+la autora fijó como punto de comparación) y la de después (t1/foto_repo_tanda_final_t1.py, crudas; las dos, en t4t2_fotos/, fuera del
+repo y del paquete), las dos listas de .pyc y la salida de las tasas. Solo lee; escribe <salida.md> (fuera del repo) y la imprime. Es
+tanda1/t4/scripts/freno_t4t2_foto.py con lo que admite el segundo tramo de la tanda final:
+  - lo nuevo, solo en tanda_final/t4/; t3/muestras/unidades_a_la_vista_T4.json, solo si hubo ampliación; los archivos que se llaman
+    exactamente .DS_Store van aparte, con su ruta (decisión de la autora sobre el FRENO del paso 0, punto 2); lo demás es «fuera de lo
+    admitido»;
+  - el primer tramo no escribió ningún NO_ABRIR_ en t4/: se controla que no haya ninguno en las dos fotos;
+  - el sha256 de los archivos de este tramo y de cada script nuevo de tanda_final/t4/scripts/, de la foto de después.
+Uso: python3 -I -B freno_t4t2_foto_tf.py <foto_antes.json> <foto_despues.json> <pyc_antes.txt> <pyc_despues.txt> <tasas.json> <salida.md>
@@ -9,0 +12 @@
+import hashlib
@@ -20,3 +23,2 @@
-T4 = "data/experiment/tanda1/t4"
-VISTA = "data/experiment/tanda1/t3/muestras/unidades_a_la_vista_T4.json"
-NA1 = f"{T4}/NO_ABRIR_conteos_t4.json"
+T4 = "data/experiment/tanda_final/t4"
+VISTA = "data/experiment/tanda_final/t3/muestras/unidades_a_la_vista_T4.json"
@@ -24 +26,2 @@
-    (f"{T4}/scripts/", "tanda1/t4/scripts/"), (f"{T4}/tasas/", "tanda1/t4/tasas/"), (f"{T4}/", "tanda1/t4/, lo demás")]
+    (f"{T4}/scripts/", "tanda_final/t4/scripts/"), (f"{T4}/tasas/", "tanda_final/t4/tasas/"),
+    (f"{T4}/ampliacion/", "tanda_final/t4/ampliacion/"), (f"{T4}/", "tanda_final/t4/, lo demás")]
@@ -32,2 +35,2 @@
-    if rel.endswith(".DS_Store"):
-        return ".DS_Store (paso 0)"
+    if Path(rel).name == ".DS_Store":
+        return ".DS_Store (ruido de Finder)"
@@ -40,5 +43,7 @@
-w = ["## 11. La foto del repo, los .pyc y el grep de convenciones", "",
-     "Lo genera `scripts/freno_t4t2_foto.py` desde la foto del paso 0 y la de después (las dos van en el paquete).", "",
-     f"- **La foto** (`t2/foto_repo_tanda1_t2.py`). Paso 0: {fa['inicio'][11:]} a {fa['fin'][11:]} del {fa['inicio'][:10]}, {mil(fa['n'])} "
-     f"entradas. Después: {fd['inicio'][11:]} a {fd['fin'][11:]} del {fd['inicio'][:10]}, {mil(fd['n'])} entradas, {fd['sin_abrir']} sin abrir "
-     f"y {fd['enlaces']} enlaces."]
+w = ["## 12. La foto del repo, los .pyc y el grep de convenciones", "",
+     "Lo genera `scripts/freno_t4t2_foto_tf.py` desde la foto de las 12:16:33 y la de después. Las dos quedan en `t4t2_fotos/`, en la "
+     "carpeta permanente de esta sesión (`fuera_del_repo/scratchpads/<sesión>/scratchpad/`), fuera del repo y del paquete porque "
+     "nombran todas las rutas del repo.", "",
+     f"- **La foto** (`t1/foto_repo_tanda_final_t1.py`). La de las 12:16:33: {fa['inicio'][11:]} a {fa['fin'][11:]} del "
+     f"{fa['inicio'][:10]}, {mil(fa['n'])} entradas, sha256 `{hashlib.sha256(FA.read_bytes()).hexdigest()}`. Después: {fd['inicio'][11:]} a {fd['fin'][11:]} del {fd['inicio'][:10]}, {mil(fd['n'])} entradas, {fd['sin_abrir']} sin abrir "
+     f"y {fd['enlaces']} enlaces, sha256 `{hashlib.sha256(FD.read_bytes()).hexdigest()}`."]
@@ -49 +54 @@
-    w.append(f"  - **{len(lista)} {nombre}:** " + ("; ".join(f"{n} en `{g}`" if g.startswith("tanda1") else f"{n}, {g}"
+    w.append(f"  - **{len(lista)} {nombre}:** " + ("; ".join(f"{n} en `{g}`" if g.startswith("tanda_final") else f"{n}, {g}"
@@ -53 +58 @@
-ds = [r for r in nuevos + cambiados if r.endswith(".DS_Store")]
+ds = [r for r in nuevos + cambiados if Path(r).name == ".DS_Store"]
@@ -55 +60,2 @@
-    w.append("  - **Los `.DS_Store` que aparecieron o cambiaron durante el tramo** (sin abrirlos; hora de la foto de después): " + "; ".join(
+    w.append("  - **Los `.DS_Store` que aparecieron o cambiaron durante el tramo** (ruido de Finder, fuera de lo que cuenta; sin abrirlos; hora "
+        "de la foto de después): " + "; ".join(
@@ -57,4 +63,4 @@
-w.append(f"  - **El `NO_ABRIR_` del primer tramo** (`{NA1}`), sin abrirlo: {mil(a[NA1]['bytes'])} bytes y hora "
-         f"{datetime.fromtimestamp(a[NA1]['mtime']).strftime('%Y-%m-%d %H:%M:%S')} en el paso 0; en la foto de después, igual: {a[NA1] == d[NA1]}.")
-w.append(f"  - **`unidades_a_la_vista_T4.json`** (`t3/muestras/`): sin ampliación no se toca; igual en las dos fotos: {a[VISTA] == d[VISTA]} "
-         f"(`{d[VISTA]['sha256'][:16]}…`).")
+na = [r for r in sorted(set(a) | set(d)) if r.startswith(f"{T4}/") and Path(r).name.startswith("NO_ABRIR_")]
+w.append(f"  - **Los `NO_ABRIR_` en `t4/`:** {len(na)} en las dos fotos" + (": " + ", ".join(f"`{r}`" for r in na) if na else "") + ".")
+w.append(f"  - **`unidades_a_la_vista_T4.json`** (`t3/muestras/`): " + ("con la ampliación cambia" if amp else "sin ampliación no se toca")
+         + f"; sha256 `{a[VISTA]['sha256']}` a las 12:16:33 y `{d[VISTA]['sha256']}` después; iguales: {a[VISTA] == d[VISTA]}.")
@@ -65 +71 @@
-    if k.startswith(f"{T4}/") and not k.startswith(f"{T4}/scripts/") and not k.endswith(".DS_Store"):
+    if k.startswith(f"{T4}/") and not k.startswith(f"{T4}/scripts/") and Path(k).name != ".DS_Store":
```

### `freno_t4t2_armar.py` → `freno_t4t2_armar_tf.py` (422 líneas cambiadas)

```diff
--- tanda1/t4/scripts/freno_t4t2_armar.py
+++ tanda_final/t4/scripts/freno_t4t2_armar_tf.py
@@ -1,4 +1,6 @@
-"""B6.1, tanda 1, T4, segundo tramo, punto 8: arma el FRENO T4 (segundo tramo) desde los archivos del repo y del trabajo, por script: toda
-cifra del texto sale de un JSON o de una tabla generada; las tablas van tal cual; el texto fijo no lleva cifras propias. Solo lee; escribe
-<salida.md> (fuera del repo). Copia de freno_t4t1_armar.py con las secciones de este tramo.
-Uso: python3 -I -B freno_t4t2_armar.py <repo> <paso0.md> <seccion_foto.md> <grep.json> <salida.md>
+"""B6.1, tanda final, T4, segundo tramo: arma el FRENO T4 (segundo tramo) desde los archivos del repo y del trabajo, por script: toda
+cifra del texto sale de un JSON o de una tabla generada; las tablas van tal cual; el texto fijo no lleva cifras propias. Es
+tanda1/t4/scripts/freno_t4t2_armar.py con las secciones de la tanda final, la ampliación y los diffs enteros de los cuatro scripts contra
+los de la tanda 1 (difflib, sin contexto). Solo lee; escribe data/experiment/tanda_final/t4/FRENO_T4_tramo2.md (frena si ya existe).
+Uso: python3 -I -B freno_t4t2_armar_tf.py <repo> <paquete del paso 0> <salida del paso 0 repetido> <seccion_foto.md> <grep.json>
+       <foto_contra_despues.json> <control_copia.json>
@@ -5,0 +8,2 @@
+import difflib
+import hashlib
@@ -12,2 +16,7 @@
-R, P0, FOTO, GREP, OUT = (Path(x) for x in sys.argv[1:6])
-T4 = R / "data/experiment/tanda1/t4"
+R, PQ0, P0B, FOTO, GREP, FC, CC = (Path(x) for x in sys.argv[1:8])
+R = R.resolve()
+TF = R / "data/experiment/tanda_final"
+T4 = TF / "t4"
+OUT = T4 / "FRENO_T4_tramo2.md"
+if OUT.exists():
+    raise SystemExit(f"FRENO: ya existe {OUT}")
@@ -14,0 +24 @@
+sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()  # noqa: E731
@@ -16,3 +26,4 @@
-U = L(R / "data/experiment/tanda1/t3/muestras/umbrales_t4_reales.json")
-POB4 = L(T4 / "muestras/poblaciones_t4_tramo1.json")["muestras"]
-grep = L(GREP)
+U = L(TF / "t3/muestras/umbrales_t4_tf.json")
+POB4 = L(TF / "t3/muestras/poblaciones_t4t1_tf.json")["muestras"]
+VER = L(T4 / "tasas/verif_tasas_independiente_t4t2_tf.json")["_resumen"]
+grep, fc, cc = L(GREP), L(FC), L(CC)
@@ -21,0 +33,10 @@
+tamp = (T4 / "ampliacion/tablas_ampliacion_t4t2.md").read_text(encoding="utf-8")
+pamp = {m.group(1): m.group(0).rstrip() for m in re.finditer(r"#### Tabla (A\d)\..*?(?=\n#### Tabla |\Z)", tamp, re.S)}
+assert sorted(pamp) == [f"A{i}" for i in range(1, 6)], sorted(pamp)
+M = "aceptadas_no_items_ampliacion"
+LA = L(T4 / "ampliacion/lectura_asistida/lectura_asistida_t4_ampliacion.json")
+mu = L(T4 / "ampliacion/muestras" / f"{M}.json")
+idx = L(T4 / "ampliacion/muestras/sorteo_ampliacion_t4t2_tf.json")
+vista = L(TF / "t3/muestras/unidades_a_la_vista_T4.json")["ampliacion"]
+CONV = (T4 / "lectura_autora/convertir_lectura_T4.py").read_text(encoding="utf-8")
+LEEME = (T4 / "lectura_autora/LEEME_lectura_T4.md").read_text(encoding="utf-8")
@@ -35 +55,0 @@
-assert not AMP["hay_ampliacion"], "con ampliación, este FRENO no sirve: faltan el sorteo, el material, las planillas y la lista nueva"
@@ -39 +59,2 @@
-# lo que el texto afirma sobre los umbrales de T3: la decisión por el p y por el umbral coinciden
+salta = [k for k, v in AMP["salta"].items() if v]
+# lo que el texto afirma: la decisión por el p y por el umbral de T3 coinciden; salta solo la de no ítems; la ampliación es de ese estrato
@@ -45,2 +66,4 @@
-assert all(not A[s]["regla"]["atencion"] for s in ESTR), "el texto de la sección 3 dice que la tasa está debajo del umbral"
-assert sum(X["NG_sin_raiz"][s]["N"] for s in ESTR) == 94  # pre-registro, 95b18217:619
+assert salta == ["aceptadas:no_items"] and AMP["hay_ampliacion"], "el texto de las secciones 7 y 8 es el de la ampliación de no ítems"
+assert not any(A[s]["regla"]["freno_por_intervalos"] for s in ESTR), "el texto de la sección 7 dice que no hay freno"
+assert mu["estrato"] == "aceptadas:no_items" and mu["n"] == 30 and idx["sha256"] == sha(T4 / "ampliacion/muestras" / f"{M}.json")
+assert vista["unidades_a_la_vista_antes"] + vista["unidades_que_suma_la_ampliacion"] == vista["unidades_a_la_vista_despues"]
@@ -48,5 +71,43 @@
-
-w = ["# FRENO T4 — tanda 1 de B6.1, segundo tramo: las tasas, la atención y la ampliación (USD 0, sin API, sin commit)", "",
-     "Rigen el pre-registro firmado (`docs/preregistro_tanda1.md`, firma en `95b18217`, con su nota del 17/10/2026 en `ca5b39fd`), §5.4 y",
-     "§5.4 bis, el «seguí» del segundo tramo y lo que decidió la autora sobre las dudosas. La lectura es la de la autora, sellada el",
-     "18/10/2026 y controlada por la mesa (`t4/control_lectura_mesa/`). HEAD `b4c42ebd`.", "",
+assert fc["ok"] and not any(fc[k]["fuera_de_lo_admitido"] for k in ("nuevos", "borrados", "cambiados"))
+assert cc["nombres_vedados"] == 0 and cc["enlaces"] == 0
+m_conv = re.search(r"SHA_PLANILLAS = \{(.*?)\}", CONV, re.S)
+conv_muestras = re.findall(r'"([a-z_0-9]+)":', m_conv.group(1))
+assert M not in conv_muestras and len(conv_muestras) == 8, conv_muestras
+assert "ampliaci" not in LEEME.lower()
+
+# las horas de la autora, del sello
+sello = [x.split() for x in (T4 / "lectura_autora/sello_lectura_T4.txt").read_text(encoding="utf-8").splitlines() if x.strip()]
+NOMM = {"cola": "cola", "aceptadas_items": "aceptadas ítems", "aceptadas_no_items": "aceptadas no ítems", "vigilancia_2": "(2)",
+        "vigilancia_7": "(7)", "vigilancia_1": "(1)", "vigilancia_3": "(3)", "observacion_12": "(12)"}
+horas = {}
+for h, f, fecha, hora, tz in sorted(sello, key=lambda x: (x[2], x[3])):
+    horas.setdefault(fecha, []).append(f"{NOMM[f.removesuffix('_marcada.csv')]} {hora}")
+ultima = max((x[2], x[3]) for x in sello)
+
+# el paquete del paso 0: sus archivos, con el sha256 de su manifiesto
+man = {ln.split()[1]: ln.split()[0] for ln in (PQ0 / "manifest.txt").read_text(encoding="utf-8").splitlines() if ln.strip()}
+P0N = ["FRENO_T4_tramo2_paso0.md", "paso0_T4_tramo2_salida.txt", "paso0_t4_tramo2.sh", "control_sustituto_foto_t4_tramo2.py",
+       "control_sustituto_foto_T4_tramo2.json"]
+assert all(man[n] == sha(PQ0 / n) for n in P0N), "el paquete del paso 0 no da los sha256 de su manifiesto"
+cs = L(PQ0 / "control_sustituto_foto_T4_tramo2.json")
+ds0 = cs["C_cuenta"]["nacidos_despues_fuera_de_los_commits"] + cs["D_modificados_despues_fuera_de_los_commits"]
+assert all(Path(r).name == ".DS_Store" for r in ds0)
+p0b = P0B.read_text(encoding="utf-8").rstrip("\n")
+HEAD = re.search(r"^== git log -1.*\n([0-9a-f]{8}) ", p0b, re.M).group(1)
+
+# los diffs de los cuatro scripts contra los de la tanda 1
+PARES = [("tasas_t4t2.py", "tasas_t4t2_tf.py"), ("tablas_t4t2.py", "tablas_t4t2_tf.py"), ("freno_t4t2_foto.py", "freno_t4t2_foto_tf.py"),
+         ("freno_t4t2_armar.py", "freno_t4t2_armar_tf.py")]
+diffs = []
+for a, b in PARES:
+    ta = (R / "data/experiment/tanda1/t4/scripts" / a).read_text(encoding="utf-8").splitlines()
+    tb = (T4 / "scripts" / b).read_text(encoding="utf-8").splitlines()
+    dl = list(difflib.unified_diff(ta, tb, f"tanda1/t4/scripts/{a}", f"tanda_final/t4/scripts/{b}", n=0, lineterm=""))
+    diffs.append((a, b, dl))
+
+w = ["# FRENO T4 — tanda final de B6.1, segundo tramo: las tasas, la atención y la ampliación (USD 0, sin API, sin commit)", "",
+     "Rigen el pre-registro firmado de la tanda final (`docs/preregistro_tanda_final.md`, firma en `4de7f2a7`), §6, con su versión derivada",
+     f"para la lectura de T4 (`tanda_final/preregistro/preregistro_tanda_final_derivada_T4.md`, sha256 "
+     f"`{X['entradas']['preregistro_tanda_final_derivada_T4.md']}`), el «seguí» del segundo tramo, la regla de las dudosas (registro de",
+     "decisiones, §35) y lo que decidió la autora sobre el FRENO del paso 0. La lectura es la de la autora, sellada en",
+     f"`t4/lectura_autora/sello_lectura_T4.txt` y controlada por la mesa (`t4/control_lectura_mesa/`). HEAD `{HEAD}`.", "",
@@ -60,4 +121,5 @@
-      f"{d(RI['regla']['tasa_ponderada_RI'])}, p {d(RI['regla']['p_valor_atencion'])}: no salta." if not RI["regla"]["atencion"] else
-      f"- **La atención de RI** (sección 3): salta.",
-      f"- **La ampliación** (sección 7): {sn(AMP['hay_ampliacion'])}. No salta ninguna atención, así que no sorteé nada y "
-      "`t3/muestras/unidades_a_la_vista_T4.json` no se tocó.",
+      f"{d(RI['regla']['tasa_ponderada_RI'])}, p {d(RI['regla']['p_valor_atencion'])}: no salta.",
+      f"- **La ampliación** (secciones 7 y 8): sí, por la atención de las aceptadas no ítems. Sorteé {mu['n']} unidades más de las que "
+      "no se leyeron, armé su material, la lectura asistida y la planilla en blanco de la autora, y sumé sus unidades a "
+      f"`t3/muestras/unidades_a_la_vista_T4.json`, que pasa a sha256 `{sha(TF / 't3/muestras/unidades_a_la_vista_T4.json')}`. Las tasas "
+      "sobre las 60 van en el tercer tramo, después de la lectura de la autora.",
@@ -65,2 +127 @@
-      f"Wilson {iv(C['regla']['wilson'])}. La regla del 25 % " + ("se dispara" if C["regla"]["regla_del_25_se_dispara"] else "no se dispara")
-      + ": es cifra y vigilancia, no freno.",
+      f"Wilson {iv(C['regla']['wilson'])}. La regla del 25 % se dispara: es cifra y vigilancia, no freno.",
@@ -71,2 +132,3 @@
-      f"- **La regla de las dudosas** (sección 2): la sensibilidad, con las dudosas fuera, da otra decisión en {len(otra)} de las seis "
-      "(atención y freno de cada estrato, atención de RI y regla del 25 % de la cola).",
+      f"- **La regla de las dudosas** (sección 2): hay {dud['cola'] + dud['items'] + dud['no_items']} dudosas en la cola y las aceptadas, así "
+      f"que la sensibilidad da otra decisión en {len(otra)} de las seis (atención y freno de cada estrato, atención de RI y regla del 25 % "
+      "de la cola).",
@@ -75 +137,26 @@
-w += [P0.read_text(encoding="utf-8").strip(), ""]
+
+# 1. Paso 0
+w += ["## 1. Paso 0", "",
+      "- **El primer paso 0 frenó** (12:16). La foto de después del primer tramo, que era su punto de comparación, había quedado solo en "
+      "`/private/tmp` y se perdió, y había cambios fuera de los commits: "
+      f"{len(ds0)} archivos `.DS_Store`. Ese FRENO, su salida y su control sustituto están en el paquete "
+      f"`revision_tanda_final_FRENO_T4_tramo2_paso0/` (manifiesto con sha256 `{sha(PQ0 / 'manifest.txt')}`), en la carpeta permanente "
+      "de esta sesión, con estos nombres:",
+      "  - `FRENO_T4_tramo2_paso0.md`: el FRENO, con el error propio en su sección 5;",
+      "  - `paso0_T4_tramo2_salida.txt`, de `paso0_t4_tramo2.sh`: la salida del paso 0;",
+      "  - `control_sustituto_foto_t4_tramo2.py` y su salida, `control_sustituto_foto_T4_tramo2.json`: el control sustituto (A a H).",
+      "- **Lo que decidió la autora sobre ese FRENO:**",
+      "  1. el control sustituto vale como la foto de ese paso 0. Lo que no cubre: el contenido de los no rastreados o ignorados que no "
+      "cambiaron de fecha (los cubre por la fecha y la cuenta, no por su sha256, salvo los seis `kg.json`);",
+      "  2. los archivos que se llaman exactamente `.DS_Store` son ruido de Finder y quedan fuera de lo que cuenta; se listan con su ruta. "
+      "Cualquier otro cambio fuera de lo admitido cuenta, y freno;",
+      "  3. el paso 0 se repite antes de las tasas, contra la foto de las 12:16:33 guardada en `t4t2_fotos/`;",
+      "  4. la foto de después se compara archivo por archivo con la de las 12:16:33 y se guarda también en `t4t2_fotos/`;",
+      "  5. este FRENO cita el paquete del paso 0 y el error propio con los nombres del paquete (sección 14, punto 1).",
+      f"- **Los `.DS_Store` del primer paso 0** (sin abrirlos): " + ", ".join(f"`{r}`" for r in sorted(ds0)) + ".",
+      "- **El paso 0 repetido**, antes de las tasas. La salida, con la carpeta personal reemplazada por `$HOME` y la carpeta de trabajo por "
+      "`<DIR DE TRABAJO>` (`paso0_bis_T4_tramo2_salida.txt`, de `paso0_bis_t4_tramo2.sh`, y la comparación de `foto_contra_t4_tramo2.py`, "
+      "en el paquete):", "", "```", p0b, "```", "",
+      "- **Las horas de la autora, del sello** (`t4/lectura_autora/sello_lectura_T4.txt`): " + "; ".join(
+          f"{f[8:10]}/{f[5:7]}: " + ", ".join(v) for f, v in horas.items()) + f". La última marcada es de las {ultima[1]} del {ultima[0]}, "
+      "antes del primer paso 0.", ""]
@@ -79 +166 @@
-      "- **Lo que decidió la autora** (va al registro de decisiones; su asiento es de la autora y queda PENDIENTE):",
+      "- **La regla** (pre-registro de la tanda final, §6; registro de decisiones, §35):",
@@ -83 +170 @@
-      "- **Cómo la apliqué** (`scripts/tasas_t4t2.py`): en cada celda, la regla cuenta k = «con error» + «dudosa» sobre las n leídas; la "
+      "- **Cómo la apliqué** (`scripts/tasas_t4t2_tf.py`): en cada celda, la regla cuenta k = «con error» + «dudosa» sobre las n leídas; la "
@@ -86,3 +173,2 @@
-      f"- **Lo que da la sensibilidad:** otra decisión en {len(otra)}" + (": " + ", ".join(otra) if otra else "") + ". No hay nada que "
-      "declarar por el tercer punto de la regla." if not otra else f"- **Lo que da la sensibilidad:** otra decisión en {', '.join(otra)}; rige "
-      "la primera.", ""]
+      (f"- **Lo que da la sensibilidad:** otra decisión en {len(otra)}. No hay nada que declarar por el tercer punto de la regla." if not otra
+       else f"- **Lo que da la sensibilidad:** otra decisión en {', '.join(otra)}; rige la primera."), ""]
@@ -91 +177,2 @@
-w += ["## 3. Las aceptadas (§5.4 a, con [v8b] y [v8c])", "",
+r_no = A["no_items"]["regla"]
+w += ["## 3. Las aceptadas", "",
@@ -94,2 +181,2 @@
-      "- **Los pesos** son los de `t3/muestras/umbrales_t4_reales.json`, que T3 calculó con las unidades de cada celda antes de leer. "
-      "`tasas_t4t2.py` controla que sean los de `t3/muestras/poblaciones_t4.json` y que las n de cada celda sean las de la muestra.",
+      "- **Los pesos** son los de `t3/muestras/umbrales_t4_tf.json`, que T3 calculó con las unidades de cada celda antes de leer. "
+      "`tasas_t4t2_tf.py` controla que sean los de `t3/muestras/poblaciones_t4_t3f_tf.json` y que las n de cada celda sean las de la muestra.",
@@ -100,2 +187,4 @@
-      "- **Los umbrales de T3** van en la tabla 3 como información. La decisión sale del p-valor, y las dos dicen lo mismo: en cada estrato, "
-      "la tasa está debajo del umbral de la atención y el p pasa de 0,05.",
+      "- **Los umbrales de T3** van en la tabla 3 como información. La decisión sale del p-valor, y las dos dicen lo mismo en cada estrato: "
+      f"en ítems, la tasa ({d(A['items']['regla']['tasa_ponderada'])}) está debajo del umbral de la atención "
+      f"({d(A['items']['umbrales_T3']['atencion_desde'])}) y el p pasa de 0,05; en no ítems, la tasa ({d(r_no['tasa_ponderada'])}) pasa el "
+      f"umbral ({d(A['no_items']['umbrales_T3']['atencion_desde'])}) y el p ({d(r_no['p_valor_atencion'])}) no pasa de 0,05.",
@@ -103,3 +192,4 @@
-      "comparación que hace `umbrales` en el script de la mesa. El freno por la atención sobre las 60 no se mira: no hay ampliación.",
-      f"- **NG `sin_raiz`** (tabla 5): son {mil(sum(X['NG_sin_raiz'][s]['N'] for s in ESTR))} unidades aceptadas, ceninf y nmcief. Van con "
-      "su cifra por celda y sin umbral, como dice el pre-registro (`95b18217:619`).", ""]
+      "comparación que hace `umbrales` en el script de la mesa. No salta en ningún estrato. La tasa de no ítems sobre las 60 y su freno van "
+      "en el tercer tramo.",
+      f"- **NG `sin_raiz`** (tabla 5): son {mil(sum(X['NG_sin_raiz'][s]['N'] for s in ESTR))} unidades aceptadas. Van con su cifra por celda "
+      "y sin umbral, como en la tanda 1 (pre-registro de la tanda 1, `95b18217:619`).", ""]
@@ -108 +198 @@
-w += ["## 4. La cola (§5.4 b, con [v8b])", "", partes[6], "",
+w += ["## 4. La cola", "", partes[6], "",
@@ -110,5 +200,3 @@
-      "- **La ponderada** usa los pesos de la cola de `umbrales_t4_reales.json`. NG `sin_raiz` no tiene unidades en la cola, así que su "
-      "celda no pesa ni se lee.",
-      f"- **La regla del 25 %** se dispara con la regla de las dudosas y también sin ellas. El pre-registro la fija como cifra y vigilancia, "
-      "no como freno (`95b18217:641`). Si se dispara, «se investiga la causa antes de la tanda 2, sin cambiar el grafo sin cola» "
-      "(`95b18217:634-635`). Esa investigación no es de este mandato: queda para la mesa y la autora (sección 10).", ""]
+      "- **La ponderada** usa los pesos de la cola de `umbrales_t4_tf.json`, con el n efectivo de Kish.",
+      "- **La regla del 25 %** se dispara con la regla de las dudosas y también sin ellas. Es cifra y vigilancia, no freno, como en la tanda 1 "
+      "(pre-registro de la tanda 1, `95b18217:641`). Qué se hace con ella en la tanda final queda para la mesa y la autora (sección 11).", ""]
@@ -119,2 +207,2 @@
-      "- **La ponderación:** las cuatro muestras salieron por celdas y el pre-registro no fija cómo se ponderan sus tasas. Van la cruda (k "
-      "sobre las leídas, con el Wilson de esa n) y la ponderada por celda (con el Wilson del n efectivo de Kish), las dos.",
+      "- **La ponderación:** las cuatro muestras salieron por celdas, y van la cruda (k sobre las leídas, con el Wilson de esa n) y la "
+      "ponderada por celda (con el Wilson del n efectivo de Kish), las dos, como en la tanda 1.",
@@ -124,3 +212,3 @@
-      f"- **Los pesos:** los de la (1) y la (3) son los de `t4/muestras/poblaciones_t4_tramo1.json` ({mil(POB4['vigilancia:1']['N'])} nodos "
-      f"Condicion y {mil(POB4['vigilancia:3']['N'])} grupos). Los de la (2), los de la extracción final de `umbrales_t4_reales.json` "
-      f"({mil(U['otras']['vigilancia:2']['N'])} unidades, decisión 1.3).",
+      f"- **Los pesos:** los de la (1) y la (3) son los de `t3/muestras/poblaciones_t4t1_tf.json` ({mil(POB4['vigilancia:1']['N'])} nodos "
+      f"Condicion y {mil(POB4['vigilancia:3']['N'])} grupos). Los de la (2), los de la extracción final de `umbrales_t4_tf.json` "
+      f"({mil(U['otras']['vigilancia:2']['N'])} unidades).",
@@ -138,4 +226,2 @@
-      "`t4/muestras/poblaciones_t4_tramo1.json`). El bloque `otras.observacion:12` de `umbrales_t4_reales.json` trae los de A4.1 "
-      f"({mil(U['otras']['observacion:12']['N'])} aristas), que no rigen desde esa decisión. La muestra vieja de `t3/` no se leyó.",
-      "- **La comparación con la tanda 0:** con las `remite_a` fuera, la (12) de la tanda 1 queda comparable con la de la tanda 0 "
-      "(registro de decisiones, §29). La línea de base es la de la tabla 1.", ""]
+      "`t3/muestras/poblaciones_t4t1_tf.json`), los mismos que trae `otras.observacion:12` de `umbrales_t4_tf.json` "
+      f"({mil(U['otras']['observacion:12']['N'])} aristas).", ""]
@@ -146,2 +232,2 @@
-      f"{sn(AMP['salta']['aceptadas:no_items'])} (p {d(A['no_items']['regla']['p_valor_atencion'])}); RI, {sn(AMP['salta']['RI'])} "
-      f"(p {d(RI['regla']['p_valor_atencion'])}). Con las dudosas fuera, tampoco salta ninguna: "
+      f"{sn(AMP['salta']['aceptadas:no_items'])} (p {d(r_no['p_valor_atencion'])}); RI, {sn(AMP['salta']['RI'])} "
+      f"(p {d(RI['regla']['p_valor_atencion'])}). Con las dudosas fuera, lo mismo: "
@@ -149,7 +235,38 @@
-      f"- **El freno:** ítems, {sn(A['items']['regla']['freno_por_intervalos'])}; no ítems, {sn(A['no_items']['regla']['freno_por_intervalos'])}.",
-      "- **La ampliación: no.** No sorteé nada ni armé material, lectura asistida ni planillas. `t3/muestras/unidades_a_la_vista_T4.json` "
-      "queda como lo dejó el primer tramo (sección 11). No hay tercer tramo de tasas.", ""]
-
-# 8. Para la hoja
-w += ["## 8. Las cifras para la hoja de la revisión entre tandas", "",
-      "Van en `t4/tablas_t4_tramo2.md` (tabla 1), que genera `scripts/tablas_t4t2.py` desde la salida de las tasas. La copio tal cual:", "",
+      f"- **El freno:** ítems, {sn(A['items']['regla']['freno_por_intervalos'])}; no ítems, {sn(r_no['freno_por_intervalos'])}.",
+      "- **La ampliación: sí,** de las aceptadas no ítems (sección 8). La atención de ítems y la de RI no saltan, así que no se sortea nada "
+      "de ítems.", ""]
+
+# 8. La ampliación
+la_h = LA["hora_de_la_lectura"][M]
+w += ["## 8. La ampliación de las aceptadas no ítems", "",
+      "Las tablas A1 a A5 son las de `t4/ampliacion/tablas_ampliacion_t4t2.md`, de `scripts/tablas_ampliacion_t4t2_tf.py` (rutas relativas a "
+      "`t4/`). Las copio tal cual.", "",
+      "- **El sorteo** (`scripts/sorteo_ampliacion_t4t2_tf.py`): sobre las unidades del estrato que no se leyeron, con las cuotas y las reglas "
+      "de celda de la tanda 1 (`celdas_t4_t3f.asignar`, sin cambios) y la cadena `tandafinal:{muestra}:{celda}:ampliacion:{base}` "
+      "(«seguí», punto 5; pre-registro, §6: «las ampliaciones con `:ampliacion:`»). La base es el sha256 de la versión para firmar del "
+      "pre-registro (`5289b02f`), como en T3; el script controla que el texto firmado (`4de7f2a7`) traiga la base, la plantilla y "
+      "«`:ampliacion:`», y que la salida de las tasas diga que salta solo la atención de no ítems.", "",
+      pamp["A1"], "", pamp["A2"], "",
+      "- **El material** (`scripts/material_ampliacion_t4t2_tf.py`, que es `t3/scripts/material_t4_t3f_tf.py` con la muestra de la "
+      "ampliación): corrió sobre la copia del repo (sección 12), sin `ANTHROPIC_API_KEY`, y lo copié a `t4/ampliacion/material/` con su "
+      "consola; los sha256 del repo son los de la copia. El control (`scripts/control_material_ampliacion_t4t2_tf.py`, el de T3 con el "
+      "índice de la ampliación) da 0 claves vedadas.",
+      "- **La lectura asistida** (`scripts/anotar_ampliacion_t4t2.py` y `scripts/armar_lectura_ampliacion_t4t2.py`): como en el primer "
+      f"tramo, con los mismos criterios (`criterios_de_la_propuesta`; solo cambia la nota de las dudosas, que remite al tercer tramo). La "
+      f"leí yo ({LA['modelo']['nombre']}, `{LA['modelo']['id']}`), sin API; las propuestas se escribieron de "
+      f"{la_h['primera_propuesta'][11:19]} a {la_h['ultima_escritura'][11:19]} del {la_h['primera_propuesta'][:10]}. El borrador "
+      "se escribió en el repo (`t4/ampliacion/lectura_asistida/borradores/`) y de ahí salen la lectura asistida, las omisiones y "
+      "observaciones y la planilla de la autora.",
+      f"- **La planilla de la autora:** `t4/ampliacion/lectura_autora/{M}.csv`, con las columnas de las del primer tramo (`id`, `celda`, "
+      "`ficha`, `propuesta`, `justificacion`, `veredicto_autora` y `nota_autora`, las dos últimas vacías) y la ruta de cada ficha en "
+      f"`t4/ampliacion/material/{M}/fichas_{M}.md`.",
+      "- **La lista de unidades a la vista** (`scripts/unidades_a_la_vista_ampliacion_t4t2_tf.py`, con la regla de T3, copiada): corrió sobre "
+      "la copia, controló que las ocho muestras de T3 den lo mismo que en la lista vigente y la reemplacé en el repo después de controlar que "
+      "la vigente era la de HEAD. Es antes de cualquier sorteo de las FICHAS: no hubo ninguno.", "",
+      pamp["A3"], "", pamp["A4"], "", pamp["A5"], "",
+      "- **Lo que sigue (tercer tramo):** la autora lee la planilla; con su lectura sellada, las tasas sobre las 60 (las 30 leídas y las 30 "
+      "de la ampliación), la atención y el freno. Lo que hace falta antes está en la sección 11, puntos 1 y 2.", ""]
+
+# 9. Para la hoja
+w += ["## 9. Las cifras para la hoja de la revisión entre tandas", "",
+      "Van en `t4/tablas_t4_tramo2.md` (tabla 1), que genera `scripts/tablas_t4t2_tf.py` desde la salida de las tasas. La copio tal cual:", "",
@@ -158,2 +275,2 @@
-# 9. Cegamiento
-w += ["## 9. El cegamiento", "",
+# 10. Cegamiento
+w += ["## 10. El cegamiento", "",
@@ -161,6 +278,12 @@
-      "ni el gasto de los reintentos.** `tasas_t4t2.py` lee solo las marcadas y su sello, las muestras, las poblaciones, los umbrales y el "
-      "script de la mesa. No miré ningún desglose por estado de E3.",
-      "- **Por eso no escribí `t4/NO_ABRIR_conteos_t4_tramo2.json`:** no hay nada que lo use, y no tiene contenido que yo pueda decidir sin "
-      "mirar lo que el cegamiento veda. Es mi lectura del punto 7 del mandato («lo que los use va a un archivo nuevo»); si la mesa lo leía de "
-      "otro modo, queda para su revisión.",
-      "- **El `NO_ABRIR_` del primer tramo** no se tocó ni se abrió: la foto da el mismo tamaño y la misma hora (sección 11).",
+      "ni el gasto de los reintentos.** `tasas_t4t2_tf.py` lee solo las marcadas y su sello, las muestras, las poblaciones, los umbrales, la "
+      "versión derivada y el script de la mesa. El material de la ampliación no trae el estado ni las marcas de E3 (tabla A3: 0 claves "
+      "vedadas). No miré ningún desglose por estado de E3.",
+      "- **Por eso no escribí `t4/NO_ABRIR_conteos_t4_tramo2.json`:** no hay nada que lo use. La foto da 0 `NO_ABRIR_` en `t4/` (sección 12).",
+      "- **De la tanda 1** abrí sus cuatro scripts del segundo tramo (`tasas_t4t2.py`, `tablas_t4t2.py`, `freno_t4t2_foto.py` y "
+      "`freno_t4t2_armar.py`) y listé los nombres de `tanda1/t4/scripts/`. Además, y lo declaro porque la cláusula dice «solo sus scripts del "
+      "segundo tramo»:",
+      f"  - leí e importo sin cambios `tanda1/t3/scripts/celdas_t4_t3f.py` (sha256 `{idx['celdas_t4_t3f_sha256']}`), que tiene las cuotas "
+      "y las reglas de celda que pide el punto 5. Es código, sin cifras de la tanda 1, y es el que importa el T3 de la tanda final;",
+      "  - el control sustituto del primer paso 0 calculó el sha256 de los seis `kg.json` no rastreados contra su sello, dos de ellos de "
+      "`tanda1/t3/acumulado/`. No los leyó como datos.",
+      "  - No abrí sus muestras, su material, sus planillas, su lectura ni sus cifras: las de base salen de la versión derivada.",
@@ -169,11 +292,22 @@
-# 10. Para la autora y la mesa
-w += ["## 10. Para la autora y la mesa", "",
-      "1. **La cola:** la regla del 25 % " + ("se dispara" if C["regla"]["regla_del_25_se_dispara"] else "no se dispara") + ". El "
-      "pre-registro dice que, si se dispara, «se investiga la causa antes de la tanda 2, sin cambiar el grafo sin cola» "
-      "(`95b18217:634-635`). No lo investigué: no es de este mandato.",
-      "2. **La regla de las dudosas** va al registro de decisiones. Su asiento queda PENDIENTE.",
-      "3. **Las vigilancias y la (12)** van con la cruda y con la ponderada por celda (tabla 1). Cuál va a la hoja lo decide la mesa.",
-      "4. **`NO_ABRIR_conteos_t4_tramo2.json`** no existe (sección 9).",
-      "5. **Las horas:** la última marcada es anterior a la hora que da la autora para la última conversión (sección 1).", ""]
-
-# 11. Foto y grep
+# 11. Para la autora y la mesa
+w += ["## 11. Para la autora y la mesa", "",
+      f"1. **El convertidor no conoce la planilla de la ampliación.** `t4/lectura_autora/convertir_lectura_T4.py` tiene en `SHA_PLANILLAS` "
+      f"las {len(conv_muestras)} muestras del primer tramo y frena con cualquier otra. No lo toqué (el «seguí» lo veda). Para sellar la "
+      "lectura de la ampliación hace falta decidir cómo: extenderlo o uno nuevo. Queda PENDIENTE de la mesa.",
+      "2. **El LEEME** (`t4/lectura_autora/LEEME_lectura_T4.md`) no nombra la ampliación. Las respuestas válidas son las de las aceptadas, "
+      "y las columnas de la planilla, las mismas. Si hace falta una nota para la ampliación, es de la mesa.",
+      "3. **Las interpretaciones mías que más pueden pesar en la lectura de la ampliación** (los criterios son los del primer tramo):",
+      "   - **U-tipo con el futuro normativo:** la ficha 20 («el Banco Central… determinará si corresponde el pago…», tipada Potestad) y la "
+      "28 («El lapso a consultar será el que medie…», tipada Condicion). Es el mismo criterio de la ficha 30 de las aceptadas no ítems del "
+      "primer tramo;",
+      "   - **la ficha 26** es la única en que miré texto que la ficha no muestra: el punto 1.4 del TO, para el desarrollo de la sigla FCEM. Sin "
+      "esa lectura, el desarrollo agregado sería una observación, como en la ficha 6, y la propuesta, «sin error»;",
+      "   - **la ficha 22** depende de quién devuelve las operaciones, que el texto no nombra. Su observación da la otra lectura;",
+      "   - **la ficha 18:** la entidad financiera es donde se pide el cambio, no quien tiene la facultad. La propongo como «con error».",
+      "4. **La cola:** la regla del 25 % se dispara. Qué se hace con ella en la tanda final no es de este mandato.",
+      "5. **La fila de no ítems para la hoja** queda con las 30 leídas (tabla 1). Su cifra sobre las 60 es del tercer tramo.",
+      "6. **Dos textos de `lineas_de_base` en `tasas/tasas_t4_tramo2.json`** dicen «umbrales_t4_tf,json» (sección 14, punto 4). Las cifras "
+      "están bien. Propongo corregir el script cuando se rehagan las tasas en el tercer tramo.",
+      "7. **`NO_ABRIR_conteos_t4_tramo2.json`** no existe (sección 10).", ""]
+
+# 12. Foto y grep
@@ -182 +315,0 @@
-props = g["propios_con_patron"]
@@ -184,16 +317,12 @@
-      f"- **El grep de convenciones** (`grep_convenciones_t4t2.py` y su salida, en el paquete) busca las palabras del `user.name` de git y "
-      f"las de origen conversacional (Slack, mail, correo, «como dijo», «pedido por», …) en los {g['archivos']} archivos nuevos o cambiados "
-      f"de la foto, sin los `.DS_Store`. El control positivo da la línea {', '.join(map(str, g['control_positivo_lineas']))}. "
-      + (f"Con el patrón, en los archivos que redacté: " + "; ".join(f"`{Path(k).name}`, {len(v)} línea(s)" for k, v in props.items())
-         + ": son las líneas de un script que describen el patrón del grep. " if props else "Con el patrón, en los archivos que redacté: ninguno. ")
-      + f"Las palabras del nombre, en ningún archivo: {not g['nombre_sin_rutas']}. "
-      + (f"Con el patrón en otros archivos: {', '.join(f'`{Path(k).name}`' for k in g['con_patron_sin_rutas'] if k not in props)}. "
-         if [k for k in g["con_patron_sin_rutas"] if k not in props] else "")
-      + f"Rutas con la carpeta personal o el scratchpad: {len(g['con_rutas_absolutas'])} archivo(s)"
-      + (f" ({', '.join(f'`{Path(k).name}`' for k in g['con_rutas_absolutas'])})" if g["con_rutas_absolutas"] else "")
-      + ". El grep del FRENO va en el mensaje de cierre.",
-      "- **La copia** del repo es la del `rsync` de la cláusula, más la exclusión del volumen de Neo4j, y su control dio 0 "
-      "(`rsync_copia_t4t2.log` en el paquete). Ningún `git clone`. Ningún heredoc sin el delimitador entre comillas.", ""]
-
-# 12. Scripts
-w += ["## 12. El script de cada cifra", "",
+      f"- **El grep de convenciones** (`t3/scripts/grep_convenciones_tf.py`, sin cambios, con `LC_ALL=en_US.UTF-8`) sobre los "
+      f"{g['archivos']} archivos nuevos o cambiados de la foto: {g['coincidencias']} coincidencias de los tokens del nombre y de los "
+      f"términos, {len(g['con_rutas_absolutas'])} archivos con rutas absolutas, {g['tokens_dentro_de_rutas_absolutas']} tokens dentro de "
+      f"rutas absolutas; control positivo, {g['control_positivo']}. Su salida va en el paquete. Este FRENO y su script se escriben después de "
+      "la foto: el control final del paquete confirma que son lo único nuevo desde ella y les pasa el grep.",
+      f"- **La copia del repo** (para el material y la lista de la ampliación) es la del `rsync` de la cláusula más una exclusión que la "
+      "cláusula no trae, `--exclude=/data/experiment/neo4j/volumen` (sección 14, punto 2). El control da "
+      f"{cc['nombres_vedados']} nombres vedados y {cc['enlaces']} enlaces; el log del `rsync` tiene {cc['log_lineas']} líneas, todas «skipping "
+      "non-regular file» (los enlaces que `--no-links` no copia). El control y el log van en el paquete. Ningún `git clone`.", ""]
+
+# 13. Scripts
+w += ["## 13. El script de cada cifra", "",
@@ -201,21 +330,70 @@
-      "| las tasas, la atención, el freno, la sensibilidad, la ampliación (secciones 2 a 7) | `tasas_t4t2.py` | "
-      "`tasas/tasas_t4_tramo2.json`, `tasas/distribuciones_bajo_H0_t4_tramo2.json`, `tasas/consola_tasas_t4t2.txt` |",
-      "| las tablas 1 a 9 y las cifras para la hoja (sección 8) | `tablas_t4t2.py` | `tablas_t4_tramo2.md` |",
-      "| la foto (sección 11) | `freno_t4t2_foto.py` | la sección 11 |",
-      "| el texto de este FRENO | `freno_t4t2_armar.py` | este archivo |",
-      "| la escritura en el repo | `escribir_en_el_repo_t4t2.py` | `escrituras_en_el_repo_t4t2.json`, en el paquete |",
-      "| el paso 0 (sección 1) | los comandos de la sección 1 y `verif_paso0_commits.py` | sus salidas, pegadas; el script, en el paquete |", "",
-      f"- **Los controles de la entrada** de `tasas_t4t2.py`: {sum(ctrl.values())} de {len(ctrl)} pasan (están en la salida, `controles`).",
-      "- **Una verificación independiente** (`verif_tasas_independiente_t4t2.py`, en el paquete, fuera del repo) recuenta las marcadas sin el "
-      "código de la mesa y recalcula las tasas, los Wilson y los p-valores por convolución exacta con fracciones. Da las mismas cifras: su "
-      "consola va en el paquete.", ""]
-
-# 13. Errores
-w += ["## 13. Errores propios, con su causa", "",
-      "1. **El control de entrada de `tasas_t4t2.py` frenó la primera corrida antes de contar.** Comparaba los ids de la (7) y de la (12) "
-      "con los de su muestra, y no daban.",
-      "   - La causa: en la muestra, una arista es la lista [origen, relación, destino]; en la planilla va con « | » "
-      "(`planillas_t4t1.py:93-94`). Comparé sin unir la lista.",
-      "   - Lo corregí uniéndola igual que la planilla, y la segunda corrida pasa todos los controles. No había escrito nada.", "",
-      "FRENO T4, segundo tramo. Espero la revisión de la mesa."]
-texto = "\n".join(w) + "\n"
+      "| las tasas, la atención, el freno, la sensibilidad, la ampliación (secciones 2 a 7) | `tasas_t4t2_tf.py` | "
+      "`tasas/tasas_t4_tramo2.json`, `tasas/distribuciones_bajo_H0_t4_tramo2.json`, `tasas/consola_tasas_t4t2_tf.txt` |",
+      "| la verificación independiente de las tasas | `verif_tasas_independiente_t4t2_tf.py` | `tasas/verif_tasas_independiente_t4t2_tf.json`, "
+      "su consola |",
+      "| las tablas 1 a 9 y las cifras para la hoja (secciones 3 a 6 y 9) | `tablas_t4t2_tf.py` | `tablas_t4_tramo2.md`, "
+      "`consola_tablas_t4t2_tf.txt` |",
+      "| el sorteo de la ampliación y sus dos corridas | `sorteo_ampliacion_t4t2_tf.py` | `ampliacion/muestras/`, "
+      "`ampliacion/segunda_corrida_del_sorteo/`, `ampliacion/consola_sorteo_ampliacion_corrida1.txt` |",
+      "| el material de la ampliación y su control | `material_ampliacion_t4t2_tf.py`, `control_material_ampliacion_t4t2_tf.py` | "
+      "`ampliacion/material/` |",
+      "| la lista de unidades a la vista | `unidades_a_la_vista_ampliacion_t4t2_tf.py` | `../t3/muestras/unidades_a_la_vista_T4.json`, "
+      "`ampliacion/consola_unidades_a_la_vista_ampliacion_t4t2_tf.txt` |",
+      "| la lectura asistida y la planilla de la autora | `anotar_ampliacion_t4t2.py`, `armar_lectura_ampliacion_t4t2.py` | "
+      "`ampliacion/lectura_asistida/`, `ampliacion/lectura_autora/` |",
+      "| las tablas A1 a A5 (sección 8) | `tablas_ampliacion_t4t2_tf.py` | `ampliacion/tablas_ampliacion_t4t2.md` y su consola |",
+      "| la foto (sección 12) | `freno_t4t2_foto_tf.py` | la sección 12; su salida, en el paquete |",
+      "| el texto de este FRENO | `freno_t4t2_armar_tf.py` | este archivo |",
+      "| el paso 0 repetido (sección 1) | `paso0_bis_t4_tramo2.sh` y `foto_contra_t4_tramo2.py`, en el paquete | su salida, pegada |", "",
+      f"- **Los controles de la entrada** de `tasas_t4t2_tf.py`: {sum(ctrl.values())} de {len(ctrl)} pasan (están en la salida, `controles`).",
+      f"- **La verificación independiente** recuenta las marcadas sin el código de la mesa y recalcula las tasas, los Wilson y los p-valores "
+      f"por convolución exacta con fracciones: {VER['iguales']} de {VER['cifras']} cifras iguales, {len(VER['distintas'])} distintas.",
+      "- **Cómo salieron los scripts:** `tasas_t4t2_tf.py`, `tablas_t4t2_tf.py`, `freno_t4t2_foto_tf.py`, `material_ampliacion_t4t2_tf.py` y "
+      "`armar_lectura_ampliacion_t4t2.py` los escribieron adaptadores con reemplazos exactos (`adaptar_*_t4_tramo2.py`, en el paquete) desde "
+      "los de la tanda 1 o los del primer tramo y T3; `freno_t4t2_armar_tf.py` lo escribí desde el de la tanda 1. Los diffs enteros de los "
+      "cuatro del «seguí» contra los de la tanda 1 van en el anexo.", ""]
+
+# 14. Errores
+w += ["## 14. Errores propios, con su causa", "",
+      "1. **La foto de después del primer tramo quedó solo en `/private/tmp` y se perdió.** Está declarado en la sección 5 de "
+      "`FRENO_T4_tramo2_paso0.md`, del paquete `revision_tanda_final_FRENO_T4_tramo2_paso0/`; lo reemplazó el control sustituto "
+      "(`control_sustituto_foto_t4_tramo2.py`, `control_sustituto_foto_T4_tramo2.json`), y la salida del paso 0 es "
+      "`paso0_T4_tramo2_salida.txt`, de `paso0_t4_tramo2.sh`. La causa: dejé la foto fuera del paquete porque nombra todas las rutas del "
+      "repo, y no la guardé en otro lugar permanente. Desde este tramo, las fotos van a `t4t2_fotos/`, en la carpeta permanente: la de las "
+      "12:16:33, la del paso 0 repetido, la de después y la final del paquete.",
+      "2. **La copia del repo lleva una exclusión que la cláusula no trae:** `--exclude=/data/experiment/neo4j/volumen`, la base de Neo4j, "
+      "fuera de git. La agregué sin que el mandato la autorizara. Ninguno de los tres scripts que corrieron sobre la copia la lee (no nombran "
+      "Neo4j), así que no cambia ninguna salida; el control de la copia dio 0 de todos modos. Lo declaro para que la mesa decida.",
+      "3. **La primera corrida del sorteo no arrancó.** La consola iba a `t4/ampliacion/`, que todavía no existía, y el shell frenó antes de "
+      "correr el script; la segunda corrida, a la carpeta de trabajo, sí corrió (dio el mismo sha256 de la muestra). Borré esa salida, creé "
+      "la carpeta y corrí las dos en orden: la del repo y la segunda, que copié a `t4/ampliacion/segunda_corrida_del_sorteo/`. Las tres "
+      "dan los mismos bytes (tabla A2).",
+      "4. **Dos textos de `lineas_de_base` dicen «umbrales_t4_tf,json».** En `tasas_t4t2_tf.py`, el `.replace(\".\", \",\")` de la coma "
+      "decimal se aplica a toda la cadena, con el nombre del archivo (las líneas de `aceptadas:total` y `atencion_RI`). Las cifras están "
+      "bien. No volví a correr las tasas: el índice del sorteo guarda el sha256 de su salida, y las tablas arman esas celdas desde los "
+      "campos numéricos. Lo vi al armar las tablas.",
+      "5. **Tres controles de mis adaptadores frenaron antes de escribir.** El de `adaptar_tasas_t4_tramo2.py` y el de "
+      "`adaptar_tablas_t4_tramo2.py` marcaban menciones legítimas de la tanda 1 (la ruta del script de la mesa y la del script de origen en "
+      "la cabecera); el de `adaptar_foto_t4_tramo2.py` encontró un `endswith(\".DS_Store\")` que ningún reemplazo cubría. Corregí la lista "
+      "o agregué el reemplazo y volví a correr; ningún destino estaba escrito.", ""]
+
+# 15. Lo que no hice
+w += ["## 15. Lo que no hice", "",
+      "- **T5 ni las FICHAS**, ni las tasas sobre las 60.",
+      "- **Lo que no toqué:** las marcadas, las exportaciones, el sello, las planillas del primer tramo, el LEEME, el convertidor y el control "
+      "de la mesa; los grafos, los manifiestos, la E0, el código del pipeline, la fixture, `grafos.py`, Neo4j, el backlog y el registro de "
+      "alcance. De `t3/` solo cambié `t3/muestras/unidades_a_la_vista_T4.json` (punto 5).",
+      "- **Commits y escrituras ajenas:** no commiteé ni preparé mensajes de commit; no escribí en la memoria, en `.claude/` ni en "
+      "`.gitignore`.",
+      "- **El scratchpad:** nada que se necesite después queda solo en él. El paquete y su copia permanente llevan los scripts del paso 0 "
+      "repetido, los adaptadores, la sección de la foto, el grep, el control y el log de la copia; las fotos van a `t4t2_fotos/`.",
+      "- Los heredocs, siempre con el delimitador entre comillas.", "",
+      "FRENO T4, segundo tramo. Espero la revisión de la mesa.", ""]
+
+# Anexo: los diffs
+w += ["## Anexo. Los diffs enteros de los cuatro scripts contra los de la tanda 1", "",
+      "Con `difflib.unified_diff`, sin líneas de contexto (`n=0`): cada bloque trae todo lo que cambia.", ""]
+for a, b, dl in diffs:
+    w += [f"### `{a}` → `{b}` ({len([x for x in dl if x.startswith(('+', '-')) and not x.startswith(('+++', '---'))])} líneas cambiadas)", "",
+          "```diff", *dl, "```", ""]
+texto = "\n".join(w).rstrip("\n") + "\n"
@@ -223 +401 @@
-print(f"{len(texto.splitlines())} líneas; secciones: {len(re.findall(r'^## ', texto, re.M))}")
+print(f"{len(texto.splitlines())} líneas; secciones: {len(re.findall(r'^## ', texto, re.M))}; {OUT.name} {sha(OUT)}")
```
