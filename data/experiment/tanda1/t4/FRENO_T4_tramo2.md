# FRENO T4 — tanda 1 de B6.1, segundo tramo: las tasas, la atención y la ampliación (USD 0, sin API, sin commit)

Rigen el pre-registro firmado (`docs/preregistro_tanda1.md`, firma en `95b18217`, con su nota del 17/10/2026 en `ca5b39fd`), §5.4 y
§5.4 bis, el «seguí» del segundo tramo y lo que decidió la autora sobre las dudosas. La lectura es la de la autora, sellada el
18/10/2026 y controlada por la mesa (`t4/control_lectura_mesa/`). HEAD `b4c42ebd`.

**Resultado:**
- **Las aceptadas, ítems** (sección 3): 9 de 30 con error, contando las dudosas; tasa ponderada 0,2196, Wilson [0,0784; 0,4822]. Atención: no (p 0,3618). Freno: no.
- **Las aceptadas, no ítems** (sección 3): 3 de 30 con error, contando las dudosas; tasa ponderada 0,0968, Wilson [0,0214; 0,3446]. Atención: no (p 0,6454). Freno: no.
- **La atención de RI** (sección 3): 7 de 30; tasa ponderada de RI 0,1747, p 0,3510: no salta.
- **La ampliación** (sección 7): no. No salta ninguna atención, así que no sorteé nada y `t3/muestras/unidades_a_la_vista_T4.json` no se tocó.
- **La cola** (sección 4): 14 de 30 con error; tasa ponderada 0,4386, Wilson [0,2751; 0,6166]. La regla del 25 % se dispara: es cifra y vigilancia, no freno.
- **La observación (12)** (sección 6): 27 correctas de 30, Wilson [0,7438; 0,9654]; incorrectas por `capa_pipeline`: E1-prompt, 3.
- **Las vigilancias** (sección 5): (1), 3 sí de 30; (2), 15 vaciamientos de 30; (3), 9 duplicaciones de 30; (7), 2 sin apoyo de 4, leída entera.
- **La regla de las dudosas** (sección 2): la sensibilidad, con las dudosas fuera, da otra decisión en 0 de las seis (atención y freno de cada estrato, atención de RI y regla del 25 % de la cola).
- Toda cifra sale por script de sus archivos. Las tablas que copio de una salida van tal cual; mis aclaraciones van fuera de las tablas.
- Nada commiteado y ningún mensaje de commit preparado: los commits son de la autora y quedan PENDIENTES.

## 1. Paso 0 (18/10/2026, 17:02) y las horas de la autora

```
$ pwd
$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg
$ git log -1 --format='%h %s'
b4c42ebd Primera tanda: la lectura de la autora del primer tramo de la cuarta etapa, sellada y controlada
$ git log --format=%s -3
Primera tanda: la lectura de la autora del primer tramo de la cuarta etapa, sellada y controlada
Registro de decisiones: el cegamiento de la medicion del verificador en el mandato de la correccion de la procedencia
Registro de decisiones: los tipos y los nombres de la correccion de la procedencia, su ventana y el pre-registro de la ultima tanda
$ git status --porcelain --untracked-files=no | wc -l
       0
$ cat data/experiment/tanda1/t4/lectura_autora/sello_lectura_T4.txt
88526906a7443187192dc2cc50eacc82635ccf2b744cc075ffe3d6fa0851a723  aceptadas_items_marcada.csv  2026-10-18 15:06:08 -0300
dda313dc6add4592c66a6ea64ca4807403ef7f144658677850d46548cc275eb5  aceptadas_no_items_marcada.csv  2026-10-18 15:22:32 -0300
818850df2cb0a68018fcc23dbf886f1d8695e4b91e063668f156b949f5baafdb  cola_marcada.csv  2026-10-18 14:52:59 -0300
b1ffe65c7390c763b9f05890a198d58aa3346638f47964551cd03333187caa94  observacion_12_marcada.csv  2026-10-18 16:23:35 -0300
06521c23c60d02df673c79946d3af544fe35dedd6965cc0426df74cf6dcb788a  vigilancia_1_marcada.csv  2026-10-18 15:51:00 -0300
0317bac0a05c1960eb9db6332042c6d0a94e97bcf5668038f7ca91cfffef1d48  vigilancia_2_marcada.csv  2026-10-18 15:35:49 -0300
c3a268ea4d4daca0bda9ee46a5406c00739bd908ff45b900f24512a85f44ee31  vigilancia_3_marcada.csv  2026-10-18 16:03:25 -0300
a32e94f2fe099ba01e90a2b1f7817930e508287bcb27ca6c10f507ffe9dfb777  vigilancia_7_marcada.csv  2026-10-18 15:39:21 -0300
$ cd data/experiment/tanda1/t4/lectura_autora && shasum -a 256 *_marcada.csv
88526906a7443187192dc2cc50eacc82635ccf2b744cc075ffe3d6fa0851a723  aceptadas_items_marcada.csv
dda313dc6add4592c66a6ea64ca4807403ef7f144658677850d46548cc275eb5  aceptadas_no_items_marcada.csv
818850df2cb0a68018fcc23dbf886f1d8695e4b91e063668f156b949f5baafdb  cola_marcada.csv
b1ffe65c7390c763b9f05890a198d58aa3346638f47964551cd03333187caa94  observacion_12_marcada.csv
06521c23c60d02df673c79946d3af544fe35dedd6965cc0426df74cf6dcb788a  vigilancia_1_marcada.csv
0317bac0a05c1960eb9db6332042c6d0a94e97bcf5668038f7ca91cfffef1d48  vigilancia_2_marcada.csv
c3a268ea4d4daca0bda9ee46a5406c00739bd908ff45b900f24512a85f44ee31  vigilancia_3_marcada.csv
a32e94f2fe099ba01e90a2b1f7817930e508287bcb27ca6c10f507ffe9dfb777  vigilancia_7_marcada.csv
$ shasum -a 256 data/experiment/tanda1/t3/muestras/umbrales_t4_reales.json
687c760a13a854194dc91ae82b7b5110e860dfcd52c39bea65d6d8faf6b4691f  data/experiment/tanda1/t3/muestras/umbrales_t4_reales.json
$ git log --format='%h %s' 764768a4..HEAD
b4c42ebd Primera tanda: la lectura de la autora del primer tramo de la cuarta etapa, sellada y controlada
a36487ba Registro de decisiones: el cegamiento de la medicion del verificador en el mandato de la correccion de la procedencia
8d04f903 Registro de decisiones: los tipos y los nombres de la correccion de la procedencia, su ventana y el pre-registro de la ultima tanda
931b3484 Registro de decisiones y backlog: la correccion de la procedencia de los tramos heredados va a la re-aplicacion unica
8863327f Registro de decisiones: la vigilancia tres, las carpetas de lectura, los bloques que no ve el verificador y la lectura de sujetos
9b5e354a Medicion de la desambiguacion de sujetos: la lectura sellada de la autora, sus plantillas y el control de la mesa
e2615b36 Grafos acumulados de la primera tanda: comprimidos de forma determinista, con el script que los restaura y su prueba
7a389623 Registro de decisiones: la primera tanda hasta sus lecturas, la medicion del verificador, el agente y como se guardan los grafos
56450029 Primera tanda: los sorteos que faltaban, el material y la lectura asistida de sus muestras, primer tramo
$ python3 -B data/experiment/tanda1/t2/foto_repo_tanda1_t2.py . <scratchpad>/t4t2/foto_repo_antes_T4t2_cruda.json
2026-10-18 17:02:29 2026-10-18 17:02:41 52563 entradas
$ python3 -B data/experiment/tanda1/t2/foto_repo_tanda1_t2.py --comparar <foto final del primer tramo> <esta foto>
antes 52510, después 52563; nuevos 53, borrados 0, cambiados 5
$ python3 -I -B <scratchpad>/t4t2/verif_paso0_commits.py . <la comparación>
nuevos o cambiados en la foto, sin .DS_Store: 48; fuera de los commits: 0 []
archivos de los commits y de la foto comparados con HEAD: 109; distintos: 0 []
borrados en la foto: 0
.DS_Store nuevos o cambiados: 10
  2026-10-18 15:34:33    6148 bytes  nuevo  data/experiment/tanda1/.DS_Store  .gitignore:25:.DS_Store
  2026-10-18 14:13:56    6148 bytes  nuevo  data/experiment/tanda1/t3/muestras/.DS_Store  .gitignore:25:.DS_Store
  2026-10-18 14:14:19    6148 bytes  nuevo  data/experiment/tanda1/t3/muestras/material/.DS_Store  .gitignore:25:.DS_Store
  2026-10-18 16:35:52    8196 bytes  nuevo  data/experiment/tanda1/t4/.DS_Store  .gitignore:25:.DS_Store
  2026-10-18 16:21:21    8196 bytes  nuevo  data/experiment/tanda1/t4/lectura_autora/.DS_Store  .gitignore:25:.DS_Store
  2026-10-18 14:14:19    6148 bytes  nuevo  data/experiment/tanda1/t4/muestras/.DS_Store  .gitignore:25:.DS_Store
  2026-10-18 14:15:41    6148 bytes  nuevo  data/experiment/tanda1/t4/muestras/material/.DS_Store  .gitignore:25:.DS_Store
  2026-10-18 16:21:02   12292 bytes  cambiado  .DS_Store  .gitignore:25:.DS_Store
  2026-10-18 15:34:33    8196 bytes  cambiado  data/.DS_Store  .gitignore:25:.DS_Store
  2026-10-18 15:34:38   18436 bytes  cambiado  data/experiment/.DS_Store  .gitignore:25:.DS_Store
$ pgrep -fl "runner_corpus.py|ensamblar_tanda0.py|regression_kg.py|shapes_validator.py"
(rc=1)
$ find . -path ./.git -prune -o \( -name '*.pyc' -o -name '__pycache__' \) -print | sort | wc -l
   11236
```

- **La foto de comparación** es la final del primer tramo (`foto_repo_final_T4t1_cruda.json`, 12:42:58 a 12:43:08, después del FRENO T4
  del primer tramo), que va en el paquete con la de este paso 0 y la comparación.
- **Lo que trajeron los commits:** los nueve commits de `764768a4` a `b4c42ebd` tocan 109 archivos (`git diff --name-only 764768a4 HEAD`).
  La foto ve 48 como nuevos o cambiados, y los 109 son iguales a `git show HEAD:` byte a byte. Los otros 61 son los del primer tramo, que
  ya estaban en el disco con los mismos bytes: los 49 que escribió `escribir_en_el_repo_t4t1.py`, los 11 scripts y el FRENO.
  `verif_paso0_commits.py` y su salida van en el paquete.
- **Los diez `.DS_Store`** (siete nuevos y tres cambiados) no vienen de ningún commit y están ignorados por git (`.gitignore:25`). No los
  abrí, no los borré ni los moví.
  - Lo pregunté antes de escribir nada, como pide el paso 0. Según la autora, los dejó el Finder mientras leía y commiteaba (dato suyo:
    no lo verifiqué). Sus horas de modificación van de 14:13:56 a 16:35:52. La autora indicó seguir y declararlos con su ruta y su hora: están arriba.
  - La indicación vale solo para `.DS_Store`. Cualquier otro archivo nuevo, cambiado o borrado fuera de los commits seguía frenando.
- **Las marcadas y los umbrales:** las ocho marcadas tienen el sha256 de su línea del sello, y `umbrales_t4_reales.json` tiene el del
  mandato. `tasas_t4t2.py` lo vuelve a controlar antes de contar (sección 12).
- **`pgrep` salió vacío.** Los `.pyc` dan 11.236 líneas, la misma lista que al cierre del primer tramo (`cmp` sin diferencias).
- **Las horas de la autora** (dato suyo, del mandato): leyó de 14:12 a 16:20, y la última conversión y el sello quedaron a las 16:26.
  - Las horas de modificación de los archivos (`stat`): las exportaciones, de 14:51:41 a 16:20:27; las marcadas, de 14:52:59 a 16:23:35
    (la de cada una es la de su línea del sello); el sello, 16:26:06.
  - La hora del sello coincide con la que da la autora. La última marcada, la de la observación (12), es de las 16:23:35.

## 2. La regla de las dudosas y cómo la apliqué

- **Lo que decidió la autora** (va al registro de decisiones; su asiento es de la autora y queda PENDIENTE):
  - en la cola y en las dos de las aceptadas, una unidad «dudosa» cuenta como error para la tasa, la atención y el freno;
  - la misma cuenta con las dudosas fuera, sobre las decididas, va al lado como sensibilidad y no decide nada;
  - si la sensibilidad diera otra decisión de atención o de freno, se declara, y rige la primera.
- **Cómo la apliqué** (`scripts/tasas_t4t2.py`): en cada celda, la regla cuenta k = «con error» + «dudosa» sobre las n leídas; la sensibilidad cuenta k = «con error» sobre n − «dudosa». Los pesos de las celdas son los mismos en las dos.
- **Las dudosas:** 2 en la cola, 4 en ítems y 1 en no ítems (tablas 2 y 6).
- **Lo que da la sensibilidad:** otra decisión en 0. No hay nada que declarar por el tercer punto de la regla.

## 3. Las aceptadas (§5.4 a, con [v8b] y [v8c])

#### Tabla 2. Las aceptadas por celda (`aceptadas.<estrato>.por_celda`; pesos de `t3/muestras/umbrales_t4_reales.json`)

| estrato | celda | N | peso | leídas | con error | sin error | dudosa |
|---|---|---:|---:|---:|---:|---:|---:|
| items | RI:sin_raiz | 147 | 0,1294 | 10 | 1 | 7 | 2 |
| items | RI:resto | 13 | 0,0114 | 5 | 1 | 3 | 1 |
| items | NG:sin_raiz | 25 | 0,0220 | 5 | 2 | 3 | 0 |
| items | NG:resto | 951 | 0,8371 | 10 | 1 | 8 | 1 |
| no_items | RI:sin_raiz | 144 | 0,0681 | 10 | 1 | 8 | 1 |
| no_items | RI:resto | 143 | 0,0676 | 5 | 0 | 5 | 0 |
| no_items | NG:sin_raiz | 69 | 0,0326 | 5 | 0 | 5 | 0 |
| no_items | NG:resto | 1.760 | 0,8318 | 10 | 1 | 9 | 0 |

#### Tabla 3. Las tasas de las aceptadas, la regla y la sensibilidad (`aceptadas.<estrato>.regla` y `.sensibilidad_sin_dudosas`)

| estrato | cuenta | errores | leídas | tasa ponderada | n ef. | Wilson | p de la atención | atención | freno por intervalos | atención de T3 desde | freno de T3 desde |
|---|---|---:|---:|---:|---:|---|---:|---|---|---:|---:|
| items | regla (dudosa = error) | 9 | 30 | 0,2196 | 13,912 | [0,0784; 0,4822] | 0,3618 | no | no | 0,3827 | 0,6274 |
| items | sensibilidad (dudosas fuera) | 5 | 26 | 0,1209 | 12,486 | [0,0285; 0,3916] | 0,7330 | no | no | 0,3827 | 0,6274 |
| no_items | regla (dudosa = error) | 3 | 30 | 0,0968 | 14,130 | [0,0214; 0,3446] | 0,6454 | no | no | 0,2836 | 0,5365 |
| no_items | sensibilidad (dudosas fuera) | 2 | 29 | 0,0907 | 14,120 | [0,0192; 0,3374] | 0,7180 | no | no | 0,2836 | 0,5365 |

items: la sensibilidad da otra decisión de atención, no; de freno, no. La distribución bajo H0: 3.636 valores, suma 1,000000 (`tasas/distribuciones_bajo_H0_t4_tramo2.json`, `aceptadas:items:regla`).

no_items: la sensibilidad da otra decisión de atención, no; de freno, no. La distribución bajo H0: 3.366 valores, suma 1,000000 (`tasas/distribuciones_bajo_H0_t4_tramo2.json`, `aceptadas:no_items:regla`).

#### Tabla 4. La ponderada total y la atención de RI (`aceptadas.total` y `atencion_RI`)

| cifra | cuenta | errores de leídas | tasa | n ef. | Wilson | p de la atención | atención |
|---|---|---|---:|---:|---|---:|---|
| ponderada total | regla | — | 0,1397 | 25,817 | [0,0532; 0,3196] | — | sin umbral |
| ponderada total | sensibilidad | — | 0,1013 | 25,152 | [0,0322; 0,2759] | — | sin umbral |
| atención de RI | regla | 7 de 30 | 0,1747 | 23,906 | [0,0715; 0,3680] | 0,3510 | no |
| atención de RI | sensibilidad | 3 de 26 | 0,0842 | 21,868 | [0,0223; 0,2703] | 0,8262 | no |

Atención de RI: 447 unidades RI aceptadas; pesos items:RI:sin_raiz 0,3289, items:RI:resto 0,0291, no_items:RI:sin_raiz 0,3221, no_items:RI:resto 0,3199; por celda, con la regla, items:RI:sin_raiz 3 de 10, items:RI:resto 2 de 5, no_items:RI:sin_raiz 2 de 10, no_items:RI:resto 0 de 5.

#### Tabla 5. NG `sin_raiz`, por celda y sin umbral (`NG_sin_raiz`)

| estrato | N | leídas | con error | sin error | dudosa | tasa con la regla | tasa sin las dudosas |
|---|---:|---:|---:|---:|---:|---:|---:|
| items | 25 | 5 | 2 | 3 | 0 | 0,4000 | 0,4000 |
| no_items | 69 | 5 | 0 | 5 | 0 | 0,0000 | 0,0000 |

Mis aclaraciones:
- **Los pesos** son los de `t3/muestras/umbrales_t4_reales.json`, que T3 calculó con las unidades de cada celda antes de leer. `tasas_t4t2.py` controla que sean los de `t3/muestras/poblaciones_t4.json` y que las n de cada celda sean las de la muestra.
- **La atención** es el test exacto unilateral al 5 % contra la tanda 0, con la distribución de la tasa enumerada entera por la función `distribucion` del script de la mesa, importado sin cambiarlo. Su salida al importarse es byte a byte su JSON (sí). Las distribuciones van en `tasas/distribuciones_bajo_H0_t4_tramo2.json`.
- **Los umbrales de T3** van en la tabla 3 como información. La decisión sale del p-valor, y las dos dicen lo mismo: en cada estrato, la tasa está debajo del umbral de la atención y el p pasa de 0,05.
- **El freno** es el de los intervalos: el límite inferior del Wilson de la tasa contra el superior del Wilson de la tanda 0, la misma comparación que hace `umbrales` en el script de la mesa. El freno por la atención sobre las 60 no se mira: no hay ampliación.
- **NG `sin_raiz`** (tabla 5): son 94 unidades aceptadas, ceninf y nmcief. Van con su cifra por celda y sin umbral, como dice el pre-registro (`95b18217:619`).

## 4. La cola (§5.4 b, con [v8b])

#### Tabla 6. La cola por celda y su tasa (`cola`)

| celda | N | peso | leídas | con error | sin error | dudosa |
|---|---:|---:|---:|---:|---:|---:|
| RI:sin_raiz | 6 | 0,1429 | 6 | 2 | 3 | 1 |
| RI:resto | 5 | 0,1190 | 5 | 4 | 1 | 0 |
| NG:sin_raiz | 0 | 0,0000 | 0 | 0 | 0 | 0 |
| NG:resto | 31 | 0,7381 | 19 | 6 | 12 | 1 |

| cuenta | errores | leídas | tasa ponderada | n ef. | Wilson | la regla del 25 % se dispara |
|---|---:|---:|---:|---:|---|---|
| regla (dudosa = error) | 14 | 30 | 0,4386 | 28,646 | [0,2751; 0,6166] | sí |
| sensibilidad (dudosas fuera) | 12 | 28 | 0,3984 | 26,895 | [0,2376; 0,5847] | sí |

La sensibilidad da otra decisión de la regla del 25 %: no.

Mis aclaraciones:
- **La ponderada** usa los pesos de la cola de `umbrales_t4_reales.json`. NG `sin_raiz` no tiene unidades en la cola, así que su celda no pesa ni se lee.
- **La regla del 25 %** se dispara con la regla de las dudosas y también sin ellas. El pre-registro la fija como cifra y vigilancia, no como freno (`95b18217:641`). Si se dispara, «se investiga la causa antes de la tanda 2, sin cambiar el grafo sin cola» (`95b18217:634-635`). Esa investigación no es de este mandato: queda para la mesa y la autora (sección 10).

## 5. Las vigilancias (1), (2), (3) y (7)

#### Tabla 7. Las vigilancias (1), (2), (3) y (7), por celda (`vigilancias.<muestra>.por_celda`)

| muestra | celda | N | leídas | respuestas |
|---|---|---:|---:|---|
| vigilancia:1 | RI:sin_raiz | 94 | 10 | sí 1, no 9, no decidible 0 |
| vigilancia:1 | RI:resto | 102 | 5 | sí 1, no 4, no decidible 0 |
| vigilancia:1 | NG:sin_raiz | 42 | 5 | sí 0, no 5, no decidible 0 |
| vigilancia:1 | NG:resto | 1.163 | 10 | sí 1, no 9, no decidible 0 |
| vigilancia:2 | RI:sin_raiz | 81 | 10 | vaciamiento 10, no vaciamiento 0, no decidible 0 |
| vigilancia:2 | RI:resto | 7 | 5 | vaciamiento 3, no vaciamiento 2, no decidible 0 |
| vigilancia:2 | NG:sin_raiz | 4 | 4 | vaciamiento 0, no vaciamiento 4, no decidible 0 |
| vigilancia:2 | NG:resto | 106 | 11 | vaciamiento 2, no vaciamiento 9, no decidible 0 |
| vigilancia:3 | RI:sin_raiz | 5 | 5 | duplicación 1, distintos 4 |
| vigilancia:3 | RI:resto | 42 | 10 | duplicación 2, distintos 8 |
| vigilancia:3 | NG:sin_raiz | 1 | 1 | duplicación 1, distintos 0 |
| vigilancia:3 | NG:resto | 133 | 14 | duplicación 5, distintos 9 |
| vigilancia:7 | RI:sin_raiz | 1 | 1 | con apoyo 0, sin apoyo 1, no decidible 0 |
| vigilancia:7 | RI:resto | 0 | 0 | con apoyo 0, sin apoyo 0, no decidible 0 |
| vigilancia:7 | NG:sin_raiz | 1 | 1 | con apoyo 0, sin apoyo 1, no decidible 0 |
| vigilancia:7 | NG:resto | 2 | 2 | con apoyo 2, sin apoyo 0, no decidible 0 |

#### Tabla 8. Las tasas de las vigilancias, la cruda y la ponderada por celda (`vigilancias.<muestra>`)

| muestra | se vigila | por respuesta | fuera de la tasa | cruda | Wilson (cruda) | ponderada por celda | n ef. | Wilson (ponderada) |
|---|---|---|---|---|---|---:|---:|---|
| vigilancia:1 | sí | sí 3, no 27, no decidible 0 | no decidible 0 | 3 de 30, 0,1000 | [0,0346; 0,2562] | 0,1043 | 14,164 | [0,0242; 0,3532] |
| vigilancia:2 | vaciamiento | vaciamiento 15, no vaciamiento 15, no decidible 0 | — | 15 de 30, 0,5000 | [0,3315; 0,6685] | 0,5276 | 23,179 | [0,3354; 0,7120] |
| vigilancia:3 | duplicación | duplicación 9, distintos 21 | — | 9 de 30, 0,3000 | [0,1666; 0,4788] | 0,3199 | 22,658 | [0,1665; 0,5255] |
| vigilancia:7 | sin apoyo | con apoyo 2, sin apoyo 2, no decidible 0 | — | 2 de 4, 0,5000 | [0,1500; 0,8500] | — | — | leída entera, sin celdas |

Vigilancia (3): el grupo es de nodos con la misma unidad y el mismo tramo, así que no ve las duplicaciones con tramos distintos (decisión de la autora del 18/10/2026, punto 1.4; registro de decisiones, §29).

Mis aclaraciones:
- **La ponderación:** las cuatro muestras salieron por celdas y el pre-registro no fija cómo se ponderan sus tasas. Van la cruda (k sobre las leídas, con el Wilson de esa n) y la ponderada por celda (con el Wilson del n efectivo de Kish), las dos.
- **Las no decidibles:** en la (1) quedan fuera de la tasa, con su cuenta (registro de decisiones, §29), y son 0. En la (2) y en la (7) no hay ninguna: 0 y 0.
- **Los pesos:** los de la (1) y la (3) son los de `t4/muestras/poblaciones_t4_tramo1.json` (1.401 nodos Condicion y 181 grupos). Los de la (2), los de la extracción final de `umbrales_t4_reales.json` (198 unidades, decisión 1.3).
- **La (3)** lleva su declaración debajo de la tabla 8. El criterio de su lectura para el par deber y acto regulado es el de la §31 del registro de decisiones, fijado antes de leer.
- **La (7)** se leyó entera (4 aristas, sin celdas). Su Wilson es el de la cruda con esa n.

## 6. La observación (12)

#### Tabla 9. La observación (12), por celda (`observacion:12`; pesos de `muestras/poblaciones_t4_tramo1.json`)

| celda | N | peso | leídas | correcta | no decidible | incorrecta |
|---|---:|---:|---:|---:|---:|---:|
| RI:sin_raiz | 960 | 0,0519 | 10 | 10 | 0 | 0 |
| RI:resto | 1.743 | 0,0943 | 5 | 4 | 0 | 1 |
| NG:sin_raiz | 770 | 0,0417 | 5 | 4 | 0 | 1 |
| NG:resto | 15.010 | 0,8121 | 10 | 9 | 0 | 1 |

Cruda: 27 correctas de 30, 0,9000, Wilson [0,7438; 0,9654]. Ponderada por celda: 0,8916, n ef. 14,631, Wilson [0,6467; 0,9737]. Las incorrectas, por `capa_pipeline`: E1-prompt, 3 (fichas `fichas_observacion_12.md#13`, `fichas_observacion_12.md#20`, `fichas_observacion_12.md#30`).

Mis aclaraciones:
- **La cuenta** es la de la enmienda de la observación 12 (`docs/enmienda_preregistro_tanda0_2026-09-27_observacion12.md:107-111`): correctas sobre 30, con las no decidibles aparte y en el denominador, y el Wilson sobre correctas / 30. La ponderada por celda va al lado porque la muestra salió por celdas.
- **Los pesos** son los del universo de la decisión 1.2 (18.483 aristas, `t4/muestras/poblaciones_t4_tramo1.json`). El bloque `otras.observacion:12` de `umbrales_t4_reales.json` trae los de A4.1 (28.062 aristas), que no rigen desde esa decisión. La muestra vieja de `t3/` no se leyó.
- **La comparación con la tanda 0:** con las `remite_a` fuera, la (12) de la tanda 1 queda comparable con la de la tanda 0 (registro de decisiones, §29). La línea de base es la de la tabla 1.

## 7. La atención, el freno y la ampliación

- **La atención:** ítems, no (p 0,3618); no ítems, no (p 0,6454); RI, no (p 0,3510). Con las dudosas fuera, tampoco salta ninguna: aceptadas:items no, aceptadas:no_items no, RI no.
- **El freno:** ítems, no; no ítems, no.
- **La ampliación: no.** No sorteé nada ni armé material, lectura asistida ni planillas. `t3/muestras/unidades_a_la_vista_T4.json` queda como lo dejó el primer tramo (sección 11). No hay tercer tramo de tasas.

## 8. Las cifras para la hoja de la revisión entre tandas

Van en `t4/tablas_t4_tramo2.md` (tabla 1), que genera `scripts/tablas_t4t2.py` desde la salida de las tasas. La copio tal cual:

#### Tabla 1. Las cifras para la hoja de la revisión entre tandas (filas que esperan a T4)

| fila | tanda 1 | línea de base | decisión | script y clave de la salida |
|---|---|---|---|---|
| aceptadas, ítems | 9 de 30 (5 con error y 4 dudosas); ponderada 0,2196, Wilson [0,0784; 0,4822] (n ef. 13,912); sin las dudosas, 5 de 26, 0,1209 [0,0285; 0,3916] | 6 de 30, Wilson [0,0951; 0,3731] | atención: no (p 0,3618); freno: no | `scripts/tasas_t4t2.py`, `tasas/tasas_t4_tramo2.json`, `aceptadas.items` |
| aceptadas, no ítems | 3 de 30 (2 con error y 1 dudosa); ponderada 0,0968, Wilson [0,0214; 0,3446] (n ef. 14,130); sin las dudosas, 2 de 29, 0,0907 [0,0192; 0,3374] | 4 de 30, Wilson [0,0531; 0,2968] | atención: no (p 0,6454); freno: no | `scripts/tasas_t4t2.py`, `tasas/tasas_t4_tramo2.json`, `aceptadas.no_items` |
| aceptadas, ponderada total | 0,1397, Wilson [0,0532; 0,3196] (n ef. 25,817); sin las dudosas, 0,1013 [0,0322; 0,2759] | 0,1616, Wilson [0,0888; 0,2760] (mismo método) | sin umbral | `scripts/tasas_t4t2.py`, `tasas/tasas_t4_tramo2.json`, `aceptadas.total` |
| atención de RI | 7 de 30; ponderada de RI 0,1747, Wilson [0,0715; 0,3680] (n ef. 23,906); sin las dudosas, 3 de 26, 0,0842 | bajo H0, 0,1572 (umbral de T3: 0,2913) | atención: no (p 0,3510) | `scripts/tasas_t4t2.py`, `tasas/tasas_t4_tramo2.json`, `atencion_RI` |
| tasa de error de la cola | 14 de 30 (12 con error y 2 dudosas); ponderada 0,4386, Wilson [0,2751; 0,6166] (n ef. 28,646); sin las dudosas, 12 de 28, 0,3984 [0,2376; 0,5847] | 12 de 30, Wilson [0,246; 0,577] (reext_t0/t4/salida/tasas_t4.json) | regla del 25 %: se dispara (cifra y vigilancia, no freno) | `scripts/tasas_t4t2.py`, `tasas/tasas_t4_tramo2.json`, `cola` |
| observación (12) | 27 correctas de 30 (0 no decidibles, en el denominador; 3 incorrectas: E1-prompt 3); Wilson [0,7438; 0,9654]; ponderada por celda 0,8916 [0,6467; 0,9737] | 25 de 30, Wilson [0,664; 0,927], con el perfil anterior (pre-registro, §5.2) | sin umbral | `scripts/tasas_t4t2.py`, `tasas/tasas_t4_tramo2.json`, `observacion:12` |
| vigilancia (1) | 3 sí de 30 (0 no decidibles, fuera de la tasa); cruda 0,1000, Wilson [0,0346; 0,2562]; ponderada por celda 0,1043 [0,0242; 0,3532] | no se midió en la tanda 0 | sin umbral | `scripts/tasas_t4t2.py`, `tasas/tasas_t4_tramo2.json`, `vigilancias.vigilancia:1` |
| vigilancia (2) | 15 vaciamientos de 30; cruda 0,5000, Wilson [0,3315; 0,6685]; ponderada por celda 0,5276 [0,3354; 0,7120] | en la tanda 0 se midió la población, sin leer la muestra | sin umbral | `scripts/tasas_t4t2.py`, `tasas/tasas_t4_tramo2.json`, `vigilancias.vigilancia:2` |
| vigilancia (3) | 9 duplicaciones de 30; cruda 0,3000, Wilson [0,1666; 0,4788]; ponderada por celda 0,3199 [0,1665; 0,5255] | no se midió en la tanda 0 | sin umbral | `scripts/tasas_t4t2.py`, `tasas/tasas_t4_tramo2.json`, `vigilancias.vigilancia:3` |
| vigilancia (7) | 2 sin apoyo de 4; cruda 0,5000, Wilson [0,1500; 0,8500]; leída entera, sin celdas | en la tanda 0 se midió la población, sin leer la muestra | sin umbral | `scripts/tasas_t4t2.py`, `tasas/tasas_t4_tramo2.json`, `vigilancias.vigilancia:7` |

- **La ampliación:** salta la atención de ítems, no; la de no ítems, no; la de RI, no. Hay ampliación: no. Con las dudosas fuera: aceptadas:items no, aceptadas:no_items no, RI no.
- **Los controles de la entrada** (`scripts/tasas_t4t2.py`): 37 de 37 pasan.

## 9. El cegamiento

- **Ninguna cifra de este tramo usa el estado de E3, `n_reintentos`, `reintentos_e3.jsonl`, `copias_nota_e3.jsonl`, las `marcas_e3` ni el gasto de los reintentos.** `tasas_t4t2.py` lee solo las marcadas y su sello, las muestras, las poblaciones, los umbrales y el script de la mesa. No miré ningún desglose por estado de E3.
- **Por eso no escribí `t4/NO_ABRIR_conteos_t4_tramo2.json`:** no hay nada que lo use, y no tiene contenido que yo pueda decidir sin mirar lo que el cegamiento veda. Es mi lectura del punto 7 del mandato («lo que los use va a un archivo nuevo»); si la mesa lo leía de otro modo, queda para su revisión.
- **El `NO_ABRIR_` del primer tramo** no se tocó ni se abrió: la foto da el mismo tamaño y la misma hora (sección 11).
- No abrí ningún `.env` ni ningún `NO_ABRIR_`, ni entré en las carpetas vedadas.

## 10. Para la autora y la mesa

1. **La cola:** la regla del 25 % se dispara. El pre-registro dice que, si se dispara, «se investiga la causa antes de la tanda 2, sin cambiar el grafo sin cola» (`95b18217:634-635`). No lo investigué: no es de este mandato.
2. **La regla de las dudosas** va al registro de decisiones. Su asiento queda PENDIENTE.
3. **Las vigilancias y la (12)** van con la cruda y con la ponderada por celda (tabla 1). Cuál va a la hoja lo decide la mesa.
4. **`NO_ABRIR_conteos_t4_tramo2.json`** no existe (sección 9).
5. **Las horas:** la última marcada es anterior a la hora que da la autora para la última conversión (sección 1).

## 11. La foto del repo, los .pyc y el grep de convenciones

Lo genera `scripts/freno_t4t2_foto.py` desde la foto del paso 0 y la de después (las dos van en el paquete).

- **La foto** (`t2/foto_repo_tanda1_t2.py`). Paso 0: 17:02:29 a 17:02:41 del 2026-10-18, 52.563 entradas. Después: 17:23:48 a 17:24:00 del 2026-10-18, 52.572 entradas, 16 sin abrir y 342 enlaces.
  - **9 nuevos:** 1 en `tanda1/t4/, lo demás`; 5 en `tanda1/t4/scripts/`; 3 en `tanda1/t4/tasas/`.
  - **0 borrados:** ninguno.
  - **0 cambiados:** ninguno.
  - **Fuera de lo admitido:** 0.
  - **El `NO_ABRIR_` del primer tramo** (`data/experiment/tanda1/t4/NO_ABRIR_conteos_t4.json`), sin abrirlo: 3.207 bytes y hora 2026-10-18 12:34:56 en el paso 0; en la foto de después, igual: True.
  - **`unidades_a_la_vista_T4.json`** (`t3/muestras/`): sin ampliación no se toca; igual en las dos fotos: True (`5ec9753dc9f8caa5…`).
- **Los `.pyc`:** 11.236 líneas en el paso 0 y 11.236 después; listas iguales: True.

**El sha256 de los archivos de este tramo, de la foto de después:**

| archivo | sha256 |
|---|---|
| `data/experiment/tanda1/t4/tablas_t4_tramo2.md` | `8a0f9e4e9f9557f52b98730bae24d86d099c9ff453499a3d77adbe4c4078b5fe` |
| `data/experiment/tanda1/t4/tasas/consola_tasas_t4t2.txt` | `cee5f0413d3b2e071dfec302f80762bbaebc3ef2bce88b3c79c9dc118d68d296` |
| `data/experiment/tanda1/t4/tasas/distribuciones_bajo_H0_t4_tramo2.json` | `290585a3abd7463a162abf116331e547204ac60d247ff9cc627556b45ee54203` |
| `data/experiment/tanda1/t4/tasas/tasas_t4_tramo2.json` | `ac6e48a238226833053387cdcd7cf70397db18cdacefc22c92ee99557ff826a2` |

**Los scripts de este tramo** (`t4/scripts/`, sha256 de la foto de después):

| script | sha256 |
|---|---|
| `escribir_en_el_repo_t4t2.py` | `9384e1e13383291c6cd37533954a096920b6a76a98a4a0644dc16d5e01b629ea` |
| `freno_t4t2_armar.py` | `677831e8331d525d408297edb31239bd1dcdf99a10381d87008430caee3eea69` |
| `freno_t4t2_foto.py` | `f34d6cf88addf7c72f042f016b1ef927a9998b0baac71e6a1ef9f444de04fa12` |
| `tablas_t4t2.py` | `4ca69807b5c879e30a1390758b02e83b48a9f8365e6f8cfd48f9d9fdba0898ce` |
| `tasas_t4t2.py` | `a85b5da927a2c68576f8d42eada14fa8e3bcb33b08bed10fe57925120beddb5f` |

- **El grep de convenciones** (`grep_convenciones_t4t2.py` y su salida, en el paquete) busca las palabras del `user.name` de git y las de origen conversacional (Slack, mail, correo, «como dijo», «pedido por», …) en los 9 archivos nuevos o cambiados de la foto, sin los `.DS_Store`. El control positivo da la línea 2. Con el patrón, en los archivos que redacté: `freno_t4t2_armar.py`, 1 línea(s): son las líneas de un script que describen el patrón del grep. Las palabras del nombre, en ningún archivo: True. Rutas con la carpeta personal o el scratchpad: 0 archivo(s). El grep del FRENO va en el mensaje de cierre.
- **La copia** del repo es la del `rsync` de la cláusula, más la exclusión del volumen de Neo4j, y su control dio 0 (`rsync_copia_t4t2.log` en el paquete). Ningún `git clone`. Ningún heredoc sin el delimitador entre comillas.

## 12. El script de cada cifra

| cifras | script (`t4/scripts/`) | salida |
|---|---|---|
| las tasas, la atención, el freno, la sensibilidad, la ampliación (secciones 2 a 7) | `tasas_t4t2.py` | `tasas/tasas_t4_tramo2.json`, `tasas/distribuciones_bajo_H0_t4_tramo2.json`, `tasas/consola_tasas_t4t2.txt` |
| las tablas 1 a 9 y las cifras para la hoja (sección 8) | `tablas_t4t2.py` | `tablas_t4_tramo2.md` |
| la foto (sección 11) | `freno_t4t2_foto.py` | la sección 11 |
| el texto de este FRENO | `freno_t4t2_armar.py` | este archivo |
| la escritura en el repo | `escribir_en_el_repo_t4t2.py` | `escrituras_en_el_repo_t4t2.json`, en el paquete |
| el paso 0 (sección 1) | los comandos de la sección 1 y `verif_paso0_commits.py` | sus salidas, pegadas; el script, en el paquete |

- **Los controles de la entrada** de `tasas_t4t2.py`: 37 de 37 pasan (están en la salida, `controles`).
- **Una verificación independiente** (`verif_tasas_independiente_t4t2.py`, en el paquete, fuera del repo) recuenta las marcadas sin el código de la mesa y recalcula las tasas, los Wilson y los p-valores por convolución exacta con fracciones. Da las mismas cifras: su consola va en el paquete.

## 13. Errores propios, con su causa

1. **El control de entrada de `tasas_t4t2.py` frenó la primera corrida antes de contar.** Comparaba los ids de la (7) y de la (12) con los de su muestra, y no daban.
   - La causa: en la muestra, una arista es la lista [origen, relación, destino]; en la planilla va con « | » (`planillas_t4t1.py:93-94`). Comparé sin unir la lista.
   - Lo corregí uniéndola igual que la planilla, y la segunda corrida pasa todos los controles. No había escrito nada.

FRENO T4, segundo tramo. Espero la revisión de la mesa.
