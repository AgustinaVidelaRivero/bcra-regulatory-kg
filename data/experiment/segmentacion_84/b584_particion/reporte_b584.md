# B5.8.4 — Partición final del corpus (152/152)

Reporte regenerable con:

```bash
python3 data/experiment/segmentacion_84/b584_particion/code/correr_b584.py
python3 data/experiment/segmentacion_84/b584_particion/code/adjudicar_b584.py
python3 data/experiment/segmentacion_84/b584_particion/code/generar_reporte_b584.py
```

Corrida con el código commiteado en HEAD, SIN reglas nuevas (escalera vigente → marcadores → sin raíz + parser de tablas B5.8.3 en su objetivo sellado); adjudicaciones contra criterios YA sellados, citados por fila en `adjudicaciones_b584.json` (fuentes S1–S6 en su cabecera).

## 1. Partición final (152 = 68 previos + 84 adjudicados)

| clase | TOs | páginas | unidades E0 | tablas lógicas parseadas | health-check sano |
|---|--:|--:|--:|--:|--:|
| reconocidos plenos | 138 | 4183 | 9266 | 548 | 94 |
| parciales declarados | 2 | 2413 | 46 | 11 | 0 |
| no segmentables declarados | 12 | 161 | 12 | 0 | 3 |
| **suma** | **152** | **6757** | **9324** | **559** | **97** |

Recómputo de la tabla:

```bash
python3 -c "import json; p=json.load(open('data/experiment/segmentacion_84/b584_particion/particion_152.json')); print(json.dumps(p['agregados'], ensure_ascii=False, indent=1))"
```

Recómputo de los agregados desde `por_to` (verifica que la tabla suma):

```bash
python3 -c "import json,collections; p=json.load(open('data/experiment/segmentacion_84/b584_particion/particion_152.json'))['por_to']; t=collections.Counter(d['clase'] for d in p.values()); print(dict(t), sum(t.values()), sum(d['paginas'] for d in p.values()), sum(d['unidades'] for d in p.values()))"
```

### 1.1 Reconocidos plenos por vía de lectura

| vía | TOs | unidades | páginas |
|---|--:|--:|--:|
| marcadores | 3 | 230 | 79 |
| marcadores + tabular | 2 | 16 | 34 |
| sin_raiz | 24 | 550 | 319 |
| sin_raiz + tabular | 17 | 398 | 504 |
| tabular (B5.8.3) | 1 | 1 | 3 |
| vigente | 15 | 1458 | 782 |
| vigente (sellada pre-B5.8) | 68 | 6340 | 2009 |
| vigente + tabular | 8 | 273 | 453 |

```bash
python3 -c "import json,collections; p=json.load(open('data/experiment/segmentacion_84/b584_particion/particion_152.json'))['por_to']; t=collections.Counter(d['via'] for d in p.values() if d['clase']=='reconocido_pleno'); print(dict(t))"
```

## 2. La cuenta del alcance (regla i, re-recomputada)

84 TOs del censo = 41 (rinden por B5.8.1) + 7 (B5.8.2) + 1 (ri_tsa, regla vigente B5.2) + 1 (ri_acsf, vía tabular) + 22 (b_pts) + 12 (candidatos a NO) — partición disjunta, cero sin clasificar:

```bash
python3 -c "import json; c=json.load(open('data/experiment/segmentacion_84/censo_84.json')); b1=json.load(open('data/experiment/segmentacion_84/b581_sin_raiz/conteos_b581.json')); b2=json.load(open('data/experiment/segmentacion_84/b582_marcadores/conteos_b582.json')); g1={t for t,d in b1.items() if d['unidades_extraccion']>0 and t!='ri_acsf'}; g2={t for t in b2 if t!='ri_tsa'}; g5={t for t,d in c.items() if d['familia_primaria']=='b_pts'}; g6={t for t,d in c.items() if d['veredicto_preliminar'].startswith('candidato a NO')}; gs=[g1,g2,{'ri_tsa'},{'ri_acsf'},g5,g6]; assert all(not (a&b) for i,a in enumerate(gs) for b in gs[i+1:]); u=set().union(*gs); print([len(g) for g in gs], len(u), set(c)==u)"
```

## 3. Adjudicaciones (criterio citado por fila; detalle en `adjudicaciones_b584.json`)

### 3.a Los 22 b_pts — contra los umbrales C4–C8 del censo (evaluar() sellado sobre las unidades emitidas) + health-check

| TO | cat | pág | unid | fallas C* selladas (censo) | fallas C* corrida b584 | salud | marginal | adjudicación |
|---|---|--:|--:|---|---|---|---|---|
| cateloc | no-RI | 67 | 2 | C6,C8 | C6,C8 | unidades_anomalas_por_tamano | no | reconocido_con_senales_declaradas |
| cirmo3 | no-RI | 107 | 240 | C4,C5,C6 | C4,C5,C6 | paginas_sin_seccion | no | reconocido_con_senales_declaradas |
| garant | no-RI | 25 | 104 | C7 | C7 | cid | sí | reconocido_con_senales_declaradas |
| garopt | no-RI | 15 | 41 | C4,C5 | C4,C5 | paginas_sin_seccion | no | reconocido_con_senales_declaradas |
| horari | no-RI | 13 | 13 | C4 | C4 | sano | no | reconocido_con_senales_declaradas |
| inspag | no-RI | 60 | 71 | C4,C5,C7 | C4,C5,C7 | paginas_sin_seccion | no | reconocido_con_senales_declaradas |
| jafip | no-RI | 31 | 91 | C4 | C4 | sano | sí | reconocido_con_senales_declaradas |
| manori | no-RI | 99 | 18 | C4,C8 | C4,C8 | cid,unidades_anomalas_por_tamano | no | reconocido_con_senales_declaradas |
| opecam | no-RI | 32 | 56 | C5 | C5 | paginas_sin_seccion | no | reconocido_con_senales_declaradas |
| ratio | no-RI | 46 | 132 | C7 | C7 | sano | sí | reconocido_con_senales_declaradas |
| regpri | no-RI | 10 | 19 | C4 | C4 | sano | sí | reconocido_con_senales_declaradas |
| ri_ai | RI | 9 | 11 | C4,C7 | C4,C7 | paginas_sin_seccion | no | reconocido_con_senales_declaradas |
| ri_cc | RI | 118 | 36 | C4,C5,C7 | C4,C5,C6,C7 | paginas_sin_seccion,unidades_anomalas_por_tamano | no | reconocido_con_senales_declaradas |
| ri_gerc | RI | 8 | 15 | C4 | C4 | sano | no | reconocido_con_senales_declaradas |
| ri_pgn | RI | 19 | 19 | C6,C7 | C6,C7 | sano | sí | reconocido_con_senales_declaradas |
| ri_rml | RI | 77 | 32 | C4,C6,C7,C8 | C4,C6,C7 | paginas_sin_seccion,unidades_anomalas_por_tamano | no | reconocido_con_senales_declaradas |
| rmgcti | no-RI | 58 | 81 | C4,C5,C7 | — | sano | no | reconocido_pleno_digerible |
| snp_cheq | no-RI | 159 | 528 | C4 | C4 | cid | no | reconocido_con_senales_declaradas |
| snp_dd | no-RI | 68 | 56 | C4,C5,C7,C8 | C4,C5,C7 | paginas_sin_seccion,unidades_anomalas_por_tamano | no | reconocido_con_senales_declaradas |
| snp_mep | no-RI | 50 | 46 | C5,C8 | C5,C8 | unidades_anomalas_por_tamano | no | reconocido_con_senales_declaradas |
| snp_tr | no-RI | 62 | 89 | C4,C5 | C4,C5 | sano | no | reconocido_con_senales_declaradas |
| venliq | no-RI | 10 | 16 | C5 | C5 | cid,paginas_sin_seccion | no | reconocido_con_senales_declaradas |

Los 22 producen unidades por el camino VIGENTE (jamás entran a las etapas nuevas; columna `vigente_confirmado` en el JSON). El afinado opcional de B5.8.2 no se construyó (cerró con cero reglas b_pts): las fallas C* remanentes quedan DECLARADAS, no remediadas. El único `reconocido_pleno_digerible` quedó CURADO por las reglas B5.2 vigentes (evaluar sellado: digerible, cero fallas, salud sana — fila corregida en la revisión del freno).

```bash
python3 -c "import json,collections; a=json.load(open('data/experiment/segmentacion_84/b584_particion/adjudicaciones_b584.json'))['a_bpts']; print(len(a), dict(collections.Counter(f['adjudicacion'] for f in a)), sum(1 for f in a if f['marginal_censo']))"
```

### 3.b ri_tsa — verificación de la re-corrida (B5.2) y su partición

- Control S4 (b582) vs corrida b584: **COINCIDE** — modo `vigente`, 15 unidades, 9 raíces, salud paginas_sin_seccion.
- Hallazgo 2 del censo verificado: 61 páginas previas al índice quedan en rol `portada`; de ellas, **26 tienen tabla lógica parseada por la vía B5.8.3** (30 tablas lógicas en el TO); las 35 restantes quedan declaradas (lista en el JSON).
- Adjudicación: **reconocido_con_limite_declarado**.

### 3.c Reinicios por anexo/apartado (límite citado de b581/b582, no re-medido)

| TO | pág | unid | raíces | salud | límite medido (S4) | adjudicación |
|---|--:|--:|--:|---|---|---|
| nmaeef | 69 | 39 | 13 | unidades_anomalas_por_tamano | S4 b582: reinicio de numeración por ANEXO medido (198 rechazos registrados), rin… | reconocido_con_limite_declarado |
| ri_tar | 7 | 2 | 1 | sano | S4 b581: débil declarado sin forzar (1 raíz / 2 unidades; reinicio por apartado)… | reconocido_con_limite_declarado |
| ri_transpa | 23 | 2 | 1 | unidades_anomalas_por_tamano | S4 b581: débil declarado sin forzar (1 raíz / 2 unidades; reinicio por apartado)… | reconocido_con_limite_declarado |
| ri2_ae | 44 | 18 | 10 | unidades_anomalas_por_tamano | S4 b581: reinicio por apartado medido en los rechazos (fuera_de_seccion dominant… | reconocido_con_limite_declarado |
| manual | 2037 | 19 | 2 | cid | S4 b581: preámbulo 19 u/2 raíces; el cuerpo dominante es ficha (1.830 pág declar… | parcial_declarado |

### 3.d Familia declarada «parser de registro» (fuera de B5.8.1-3)

| TO | pág | pág ficha_registro | tablas lógicas parseadas |
|---|--:|--:|--:|
| manual | 2037 | 1830 | 11 |
| plandecuentas | 77 | 76 | 0 |
| ri2_pm | 376 | 345 | 0 |
| ri_laft | 45 | 27 | 8 |
| ri_transpa | 23 | 3 | 21 |

familia DECLARADA «parser de registro», fuera de la secuencia B5.8.1-3 (S3: censo §4 y veredicto de plandecuentas/manual/ri2_pm); el material ficha_registro queda fuera del parseo de prosa con su evidencia por TO (rol de página de B5.8.1) y su porción tabular rinde por B5.8.3 donde existe

```bash
python3 -c "import json; c=json.load(open('data/experiment/segmentacion_84/b584_particion/conteos_b584.json')); print({t: d['roles_pagina'].get('ficha_registro',0) for t,d in c.items() if d['roles_pagina'].get('ficha_registro',0)>0})"
```

### 3.e Los 12 candidatos a NO segmentable — declaración final

| TO | cat | pág | causa censal | modo final | unid | raíces | declaración |
|---|---|--:|---|---|--:|--:|---|
| optico | no-RI | 43 | candidato a NO segmentable — índice reconocido (4 pág) pero 0 páginas … | sin_raiz | 1 | 0 | no_segmentable_declarado |
| plandecuentas | RI | 77 | candidato a NO segmentable en esta secuencia — familia ficha/lista: ex… | sin_raiz | 0 | 0 | no_segmentable_declarado |
| ri_chr | RI | 1 | candidato a NO segmentable — espina insuficiente (1 labels en 1 pág), … | sin_raiz | 1 | 1 | no_segmentable_declarado |
| ri_con | RI | 16 | candidato a NO segmentable — espina insuficiente (0 labels en 16 pág),… | sin_raiz | 1 | 0 | no_segmentable_declarado |
| ri_fcem | RI | 1 | candidato a NO segmentable — espina insuficiente (0 labels en 1 pág), … | sin_raiz | 1 | 0 | no_segmentable_declarado |
| ri_itme | RI | 1 | candidato a NO segmentable — espina insuficiente (0 labels en 1 pág), … | sin_raiz | 1 | 0 | no_segmentable_declarado |
| ri_pfmipyme | RI | 1 | candidato a NO segmentable — espina insuficiente (0 labels en 1 pág), … | sin_raiz | 1 | 0 | no_segmentable_declarado |
| ri_pscpp | RI | 1 | candidato a NO segmentable — espina insuficiente (0 labels en 1 pág), … | sin_raiz | 1 | 0 | no_segmentable_declarado |
| ri_pspii | RI | 1 | candidato a NO segmentable — espina insuficiente (2 labels en 1 pág), … | sin_raiz | 2 | 2 | no_segmentable_declarado |
| ri_rem | RI | 2 | candidato a NO segmentable — espina insuficiente (2 labels en 2 pág), … | sin_raiz | 1 | 1 | no_segmentable_declarado |
| ri_spi | RI | 11 | candidato a NO segmentable — espina insuficiente (0 labels en 11 pág),… | sin_raiz | 1 | 0 | no_segmentable_declarado |
| ri_tii | RI | 6 | candidato a NO segmentable — espina insuficiente (0 labels en 6 pág), … | sin_raiz | 1 | 0 | no_segmentable_declarado |

```bash
python3 -c "import json; a=json.load(open('data/experiment/segmentacion_84/b584_particion/adjudicaciones_b584.json'))['e_no_segmentables']; print(len(a), sum(1 for f in a if f['declaracion']=='no_segmentable_declarado'))"
```

### 3.f Huecos de alcance de B5.4 (docvig, fimipyme) — SOLO REPORTE

- **docvig** (modo `vigente`, 31 unidades, salud sano): entradas de índice con «alcanzad»: ['Personas alcanzadas por programas especiales establecidos po']; unidades con «alcanzad» en el título: ['docvig::2.4']; anunciado_sin_cuerpo con «alcanzad»: ninguno.
- **fimipyme** (modo `vigente`, 51 unidades, salud sano): entradas de índice con «alcanzad»: ['Entidades alcanzadas.', 'Entidades alcanzadas. Las entidades financieras que estén co']; unidades con «alcanzad» en el título: ['fimipyme::4.3.2']; anunciado_sin_cuerpo con «alcanzad»: [{'numero': 'S1', 'titulo': 'Entidades alcanzadas. Las entidades financieras que estén comprendidas en el Grupo “A” –conforme a lo previsto en la', 'pagina_indice': 4}].

SOLO REPORTE (anticipa la vigilancia (6) de B6.1; el catálogo no se toca). Ambos TOs son digeribles: producen unidades por el camino vigente y la garantía estructural de B5.8.1/2 impide que las reglas nuevas los toquen (byte-identidad verificada en la batería) — cualquier hueco sellado persiste por construcción.

## 4. Tabla del re-laudo de tanda 2 (solo informa)

SOLO INFORMA (re-laudo de la autora del 06/09: incorporación en principio, corte final sobre unidades reales con health-check en verde por documento, re-presupuesto en B5.7)

| TO | clase | pág | unidades reales | tablas lógicas | health-check |
|---|---|--:|--:|--:|---|
| asomut | reconocido_pleno | 7 | 8 | 0 | sano |
| cateloc | reconocido_pleno | 67 | 2 | 0 | unidades_anomalas_por_tamano |
| cedin | reconocido_pleno | 22 | 65 | 0 | sano |
| ceninf | reconocido_pleno | 23 | 47 | 12 | cid |
| cirmo3 | reconocido_pleno | 107 | 240 | 0 | paginas_sin_seccion |
| consyr | reconocido_pleno | 11 | 32 | 0 | cid |
| dmrd | reconocido_pleno | 72 | 11 | 53 | cid,unidades_anomalas_por_tamano |
| garant | reconocido_pleno | 25 | 104 | 0 | cid |
| garopt | reconocido_pleno | 15 | 41 | 0 | paginas_sin_seccion |
| horari | reconocido_pleno | 13 | 13 | 0 | sano |
| inspag | reconocido_pleno | 60 | 71 | 0 | paginas_sin_seccion |
| jafip | reconocido_pleno | 31 | 91 | 0 | sano |
| manori | reconocido_pleno | 99 | 18 | 0 | cid,unidades_anomalas_por_tamano |
| micemp | reconocido_pleno | 8 | 7 | 0 | cid |
| nmaeef | reconocido_pleno | 69 | 39 | 0 | unidades_anomalas_por_tamano |
| nmcief | reconocido_pleno | 36 | 40 | 0 | sano |
| opecam | reconocido_pleno | 32 | 56 | 0 | paginas_sin_seccion |
| ratio | reconocido_pleno | 46 | 132 | 0 | sano |
| regpri | reconocido_pleno | 10 | 19 | 0 | sano |
| reqcac | reconocido_pleno | 10 | 3 | 0 | paginas_sin_seccion |
| ri2_ae | reconocido_pleno | 44 | 18 | 0 | unidades_anomalas_por_tamano |
| rmgcti | reconocido_pleno | 58 | 81 | 0 | sano |
| seggar | reconocido_pleno | 26 | 33 | 0 | sano |
| seguef | reconocido_pleno | 25 | 98 | 0 | sano |
| snp_cheq | reconocido_pleno | 159 | 528 | 0 | cid |
| snp_dd | reconocido_pleno | 68 | 56 | 18 | paginas_sin_seccion,unidades_anomalas_por_tamano |
| snp_mep | reconocido_pleno | 50 | 46 | 0 | unidades_anomalas_por_tamano |
| snp_tr | reconocido_pleno | 62 | 89 | 42 | sano |
| venliq | reconocido_pleno | 10 | 16 | 0 | cid,paginas_sin_seccion |
| verac | reconocido_pleno | 5 | 3 | 0 | sano |
| **30** | | | **2007** | | **12 sanos** |

```bash
python3 -c "import json; r=json.load(open('data/experiment/segmentacion_84/b584_particion/adjudicaciones_b584.json'))['tabla_relaudo_tanda2']; print(len(r['filas']), sum(f['unidades_reales'] for f in r['filas']), r['con_salud_verde'])"
```

## 5. Tabla por TO (los 152)

`unid` = unidades de extracción E0 de la corrida b584; `tab` = tablas lógicas parseadas (vía B5.8.3); `ficha` = páginas declaradas ficha_registro; señales de salud = health-check por TO (S5: lectura, no gate).

| TO | cat | clase | vía | pág | unid | tab | ficha | salud |
|---|---|---|---|--:|--:|--:|--:|---|
| actgar | no-RI | reconocido | vigente (sellada pre-B5.8) | 18 | 60 | 0 | 0 | cid |
| adfsp | no-RI | reconocido | vigente (sellada pre-B5.8) | 41 | 101 | 0 | 0 | cid |
| adrei | no-RI | reconocido | vigente (sellada pre-B5.8) | 19 | 70 | 0 | 0 | sano |
| afiltr | no-RI | reconocido | vigente (sellada pre-B5.8) | 40 | 70 | 0 | 0 | cid |
| apnf | no-RI | reconocido | vigente (sellada pre-B5.8) | 15 | 27 | 0 | 0 | sano |
| asomut | no-RI | reconocido | sin_raiz | 7 | 8 | 0 | 0 | sano |
| autenf | no-RI | reconocido | vigente (sellada pre-B5.8) | 25 | 75 | 0 | 0 | sano |
| ayccef | no-RI | reconocido | vigente (sellada pre-B5.8) | 47 | 196 | 0 | 0 | sano |
| cajasc | no-RI | reconocido | vigente (sellada pre-B5.8) | 68 | 289 | 0 | 0 | sano |
| cateloc | no-RI | reconocido | vigente | 67 | 2 | 0 | 0 | unidades_anomalas_por_tamano |
| ccbcra | no-RI | reconocido | vigente (sellada pre-B5.8) | 19 | 32 | 0 | 0 | sano |
| cedin | no-RI | reconocido | sin_raiz | 22 | 65 | 0 | 0 | sano |
| ceninf | no-RI | reconocido | sin_raiz + tabular | 23 | 47 | 12 | 0 | cid |
| cescar | no-RI | reconocido | vigente (sellada pre-B5.8) | 10 | 21 | 0 | 0 | sano |
| cirmo3 | no-RI | reconocido | vigente | 107 | 240 | 0 | 0 | paginas_sin_seccion |
| coltit | no-RI | reconocido | vigente (sellada pre-B5.8) | 13 | 39 | 0 | 0 | cid |
| consyr | no-RI | reconocido | sin_raiz | 11 | 32 | 0 | 0 | cid |
| convca | no-RI | reconocido | vigente (sellada pre-B5.8) | 8 | 13 | 0 | 0 | sano |
| cryl | no-RI | reconocido | vigente (sellada pre-B5.8) | 31 | 64 | 0 | 0 | sano |
| ctacor | no-RI | reconocido | vigente (sellada pre-B5.8) | 10 | 21 | 0 | 0 | cid |
| ctacte | no-RI | reconocido | vigente (sellada pre-B5.8) | 86 | 388 | 0 | 0 | sano |
| ctavis | no-RI | reconocido | vigente (sellada pre-B5.8) | 54 | 275 | 0 | 0 | sano |
| depaho | no-RI | reconocido | vigente (sellada pre-B5.8) | 107 | 437 | 0 | 0 | sano |
| depinv | no-RI | reconocido | vigente (sellada pre-B5.8) | 53 | 202 | 0 | 0 | sano |
| disres | no-RI | reconocido | vigente (sellada pre-B5.8) | 22 | 38 | 0 | 0 | cid |
| dmrd | no-RI | reconocido | sin_raiz + tabular | 72 | 11 | 53 | 0 | cid,unidades_anomalas_por_tamano |
| docvig | no-RI | reconocido | vigente (sellada pre-B5.8) | 14 | 31 | 0 | 0 | sano |
| efemin | no-RI | reconocido | vigente (sellada pre-B5.8) | 53 | 121 | 0 | 0 | cid |
| evacre | no-RI | reconocido | vigente (sellada pre-B5.8) | 7 | 18 | 0 | 0 | cid |
| expaef | no-RI | reconocido | vigente (sellada pre-B5.8) | 37 | 165 | 0 | 0 | sano |
| fabcra | no-RI | reconocido | vigente (sellada pre-B5.8) | 19 | 42 | 0 | 0 | sano |
| fclef | no-RI | reconocido | vigente (sellada pre-B5.8) | 12 | 28 | 0 | 0 | sano |
| fgarcp | no-RI | reconocido | vigente (sellada pre-B5.8) | 14 | 21 | 0 | 0 | sano |
| fimipyme | no-RI | reconocido | vigente (sellada pre-B5.8) | 25 | 51 | 0 | 0 | sano |
| finsec | no-RI | reconocido | vigente (sellada pre-B5.8) | 62 | 131 | 0 | 0 | sano |
| garant | no-RI | reconocido | vigente | 25 | 104 | 0 | 0 | cid |
| garopt | no-RI | reconocido | vigente | 15 | 41 | 0 | 0 | paginas_sin_seccion |
| gerc | no-RI | reconocido | vigente (sellada pre-B5.8) | 46 | 114 | 0 | 0 | sano |
| gescre | no-RI | reconocido | vigente (sellada pre-B5.8) | 35 | 59 | 0 | 0 | sano |
| gracre | no-RI | reconocido | vigente (sellada pre-B5.8) | 28 | 67 | 0 | 0 | sano |
| graloc | no-RI | reconocido | vigente (sellada pre-B5.8) | 30 | 100 | 0 | 0 | sano |
| horari | no-RI | reconocido | vigente | 13 | 13 | 0 | 0 | sano |
| icmecma | no-RI | reconocido | vigente (sellada pre-B5.8) | 27 | 47 | 0 | 0 | sano |
| incuca | no-RI | reconocido | vigente (sellada pre-B5.8) | 12 | 23 | 0 | 0 | cid |
| inspag | no-RI | reconocido | vigente | 60 | 71 | 0 | 0 | paginas_sin_seccion |
| jafip | no-RI | reconocido | vigente | 31 | 91 | 0 | 0 | sano |
| lavdin | no-RI | reconocido | vigente (sellada pre-B5.8) | 19 | 29 | 0 | 0 | cid |
| lingeef | no-RI | reconocido | vigente (sellada pre-B5.8) | 172 | 613 | 0 | 0 | cid |
| lingob | no-RI | reconocido | vigente (sellada pre-B5.8) | 24 | 139 | 0 | 0 | cid |
| manori | no-RI | reconocido | vigente | 99 | 18 | 0 | 0 | cid,unidades_anomalas_por_tamano |
| manual | RI | parcial | sin_raiz (preámbulo) + tabular/registro | 2037 | 19 | 11 | 1830 | cid |
| micemp | no-RI | reconocido | sin_raiz | 8 | 7 | 0 | 0 | cid |
| nmaeef | no-RI | reconocido | sin_raiz | 69 | 39 | 0 | 0 | unidades_anomalas_por_tamano |
| nmcief | no-RI | reconocido | sin_raiz | 36 | 40 | 0 | 0 | sano |
| opecam | no-RI | reconocido | vigente | 32 | 56 | 0 | 0 | paginas_sin_seccion |
| opefci | no-RI | reconocido | vigente (sellada pre-B5.8) | 33 | 77 | 0 | 0 | sano |
| optico | no-RI | no_segmentable | — | 43 | 1 | 0 | 0 | paginas_sin_seccion |
| ordcom | no-RI | reconocido | vigente (sellada pre-B5.8) | 22 | 65 | 0 | 0 | sano |
| osapsa | no-RI | reconocido | vigente (sellada pre-B5.8) | 12 | 12 | 0 | 0 | sano |
| pagjub | no-RI | reconocido | vigente (sellada pre-B5.8) | 16 | 52 | 0 | 0 | cid |
| pfmipyme | no-RI | reconocido | vigente (sellada pre-B5.8) | 14 | 52 | 0 | 0 | sano |
| pimf | no-RI | reconocido | vigente (sellada pre-B5.8) | 29 | 165 | 0 | 0 | sano |
| plandecuentas | RI | no_segmentable | — | 77 | 0 | 0 | 76 | paginas_sin_seccion |
| pognme | no-RI | reconocido | vigente (sellada pre-B5.8) | 14 | 17 | 0 | 0 | sano |
| polcre | no-RI | reconocido | vigente (sellada pre-B5.8) | 32 | 61 | 0 | 0 | sano |
| prevmi | no-RI | reconocido | vigente (sellada pre-B5.8) | 25 | 52 | 0 | 0 | sano |
| pscpp | no-RI | reconocido | vigente (sellada pre-B5.8) | 10 | 22 | 0 | 0 | sano |
| raapal | no-RI | reconocido | vigente (sellada pre-B5.8) | 20 | 40 | 0 | 0 | sano |
| ratio | no-RI | reconocido | vigente | 46 | 132 | 0 | 0 | sano |
| ratiofn | no-RI | reconocido | vigente (sellada pre-B5.8) | 29 | 133 | 0 | 0 | sano |
| rdbcra | no-RI | reconocido | vigente (sellada pre-B5.8) | 54 | 261 | 0 | 0 | sano |
| regpri | no-RI | reconocido | vigente | 10 | 19 | 0 | 0 | sano |
| relact | no-RI | reconocido | vigente (sellada pre-B5.8) | 20 | 38 | 0 | 0 | sano |
| repefe | no-RI | reconocido | vigente (sellada pre-B5.8) | 25 | 87 | 0 | 0 | cid |
| reqcac | no-RI | reconocido | marcadores | 10 | 3 | 0 | 0 | paginas_sin_seccion |
| retype | no-RI | reconocido | vigente (sellada pre-B5.8) | 13 | 40 | 0 | 0 | cid |
| ri2_ae | no-RI | reconocido | sin_raiz | 44 | 18 | 0 | 0 | unidades_anomalas_por_tamano |
| ri2_ci | no-RI | reconocido | vigente (sellada pre-B5.8) | 26 | 45 | 0 | 0 | sano |
| ri2_cs | RI | reconocido | sin_raiz + tabular | 31 | 7 | 47 | 0 | unidades_anomalas_por_tamano |
| ri2_pm | RI | parcial | sin_raiz (preámbulo) + tabular/registro | 376 | 27 | 0 | 345 | cid |
| ri_acsf | RI | reconocido | tabular (B5.8.3) | 3 | 1 | 1 | 0 | paginas_sin_seccion |
| ri_ai | RI | reconocido | vigente + tabular | 9 | 11 | 5 | 0 | paginas_sin_seccion |
| ri_ao | RI | reconocido | sin_raiz | 1 | 5 | 0 | 0 | sano |
| ri_bdp | RI | reconocido | sin_raiz | 3 | 3 | 0 | 0 | sano |
| ri_cc | RI | reconocido | vigente + tabular | 118 | 36 | 51 | 0 | paginas_sin_seccion,unidades_anomalas_por_tamano |
| ri_ccna | RI | reconocido | sin_raiz + tabular | 60 | 22 | 6 | 0 | unidades_anomalas_por_tamano |
| ri_ccpnp | RI | reconocido | sin_raiz + tabular | 11 | 6 | 15 | 0 | sano |
| ri_chr | RI | no_segmentable | — | 1 | 1 | 0 | 0 | sano |
| ri_con | RI | no_segmentable | — | 16 | 1 | 0 | 0 | paginas_sin_seccion |
| ri_cr | RI | reconocido | sin_raiz + tabular | 5 | 6 | 2 | 0 | sano |
| ri_dcpc | RI | reconocido | marcadores | 44 | 129 | 0 | 0 | sano |
| ri_dsf | RI | reconocido | sin_raiz + tabular | 31 | 51 | 2 | 0 | sano |
| ri_esd | RI | reconocido | sin_raiz + tabular | 3 | 3 | 2 | 0 | sano |
| ri_fcem | RI | no_segmentable | — | 1 | 1 | 0 | 0 | paginas_sin_seccion |
| ri_gerc | RI | reconocido | vigente + tabular | 8 | 15 | 4 | 0 | sano |
| ri_icpipsp | RI | reconocido | sin_raiz | 13 | 9 | 0 | 0 | sano |
| ri_ieccm | RI | reconocido | sin_raiz | 1 | 3 | 0 | 0 | sano |
| ri_iepsp | RI | reconocido | sin_raiz | 9 | 6 | 0 | 0 | sano |
| ri_iesinap | RI | reconocido | sin_raiz | 6 | 6 | 0 | 0 | sano |
| ri_ii_31_12_19 | RI | reconocido | sin_raiz | 21 | 86 | 0 | 0 | sano |
| ri_itme | RI | no_segmentable | — | 1 | 1 | 0 | 0 | paginas_sin_seccion |
| ri_laft | RI | reconocido | sin_raiz + tabular | 45 | 7 | 8 | 27 | sano |
| ri_mmsef | RI | reconocido | sin_raiz | 9 | 90 | 0 | 0 | sano |
| ri_msrl | RI | reconocido | marcadores + tabular | 20 | 11 | 5 | 0 | sano |
| ri_nge | RI | reconocido | sin_raiz | 3 | 30 | 0 | 0 | sano |
| ri_niif | RI | reconocido | sin_raiz + tabular | 86 | 13 | 64 | 0 | unidades_anomalas_por_tamano |
| ri_oc | RI | reconocido | sin_raiz + tabular | 28 | 128 | 53 | 0 | sano |
| ri_ot | RI | reconocido | sin_raiz | 6 | 30 | 0 | 0 | sano |
| ri_pfmipyme | RI | no_segmentable | — | 1 | 1 | 0 | 0 | paginas_sin_seccion |
| ri_pgn | RI | reconocido | vigente + tabular | 19 | 19 | 6 | 0 | sano |
| ri_pnp | RI | reconocido | sin_raiz + tabular | 44 | 23 | 23 | 0 | unidades_anomalas_por_tamano |
| ri_pscpp | RI | no_segmentable | — | 1 | 1 | 0 | 0 | paginas_sin_seccion |
| ri_psp | RI | reconocido | marcadores + tabular | 14 | 5 | 9 | 0 | sano |
| ri_pspapt | RI | reconocido | sin_raiz + tabular | 5 | 13 | 11 | 0 | sano |
| ri_pspii | RI | no_segmentable | — | 1 | 2 | 0 | 0 | sano |
| ri_psprca | RI | reconocido | sin_raiz + tabular | 6 | 12 | 9 | 0 | sano |
| ri_rcl | RI | reconocido | sin_raiz | 2 | 3 | 0 | 0 | sano |
| ri_rem | RI | no_segmentable | — | 2 | 1 | 0 | 0 | sano |
| ri_rml | RI | reconocido | vigente + tabular | 77 | 32 | 39 | 0 | paginas_sin_seccion,unidades_anomalas_por_tamano |
| ri_saofe | RI | reconocido | sin_raiz | 3 | 25 | 0 | 0 | sano |
| ri_secoexpo | RI | reconocido | sin_raiz + tabular | 21 | 20 | 7 | 0 | sano |
| ri_sef | RI | reconocido | sin_raiz + tabular | 10 | 27 | 3 | 0 | sano |
| ri_spi | RI | no_segmentable | — | 11 | 1 | 0 | 0 | paginas_sin_seccion |
| ri_tar | RI | reconocido | sin_raiz | 7 | 2 | 0 | 0 | sano |
| ri_tii | RI | no_segmentable | — | 6 | 1 | 0 | 0 | paginas_sin_seccion |
| ri_transpa | RI | reconocido | sin_raiz + tabular | 23 | 2 | 21 | 3 | unidades_anomalas_por_tamano |
| ri_tsa | RI | reconocido | vigente + tabular | 92 | 15 | 30 | 0 | paginas_sin_seccion |
| ri_tvf | RI | reconocido | sin_raiz | 5 | 2 | 0 | 0 | sano |
| ribspc | RI | reconocido | sin_raiz | 2 | 5 | 0 | 0 | sano |
| rmgcti | no-RI | reconocido | vigente | 58 | 81 | 0 | 0 | sano |
| rmrtsd | no-RI | reconocido | vigente (sellada pre-B5.8) | 20 | 31 | 0 | 0 | sano |
| rrci | no-RI | reconocido | vigente (sellada pre-B5.8) | 20 | 77 | 0 | 0 | sano |
| secfin | no-RI | reconocido | vigente (sellada pre-B5.8) | 10 | 22 | 0 | 0 | sano |
| seggar | no-RI | reconocido | sin_raiz | 26 | 33 | 0 | 0 | sano |
| seguef | no-RI | reconocido | marcadores | 25 | 98 | 0 | 0 | sano |
| servco | no-RI | reconocido | vigente (sellada pre-B5.8) | 14 | 40 | 0 | 0 | sano |
| snp_atm | no-RI | reconocido | vigente (sellada pre-B5.8) | 8 | 16 | 0 | 0 | sano |
| snp_cec | no-RI | reconocido | vigente (sellada pre-B5.8) | 34 | 121 | 0 | 0 | sano |
| snp_cheq | no-RI | reconocido | vigente | 159 | 528 | 0 | 0 | cid |
| snp_dd | no-RI | reconocido | vigente + tabular | 68 | 56 | 18 | 0 | paginas_sin_seccion,unidades_anomalas_por_tamano |
| snp_debin | no-RI | reconocido | vigente (sellada pre-B5.8) | 22 | 70 | 0 | 0 | sano |
| snp_mep | no-RI | reconocido | vigente | 50 | 46 | 0 | 0 | unidades_anomalas_por_tamano |
| snp_psp | no-RI | reconocido | vigente (sellada pre-B5.8) | 23 | 88 | 0 | 0 | sano |
| snp_spd | no-RI | reconocido | vigente (sellada pre-B5.8) | 32 | 129 | 0 | 0 | sano |
| snp_tr | no-RI | reconocido | vigente + tabular | 62 | 89 | 42 | 0 | sano |
| snp_tr_nc | no-RI | reconocido | vigente (sellada pre-B5.8) | 31 | 136 | 0 | 0 | sano |
| socgar | no-RI | reconocido | vigente (sellada pre-B5.8) | 14 | 12 | 0 | 0 | sano |
| supcon | no-RI | reconocido | vigente (sellada pre-B5.8) | 21 | 67 | 0 | 0 | sano |
| tasint | no-RI | reconocido | vigente (sellada pre-B5.8) | 29 | 67 | 0 | 0 | cid |
| traval | no-RI | reconocido | vigente (sellada pre-B5.8) | 15 | 28 | 0 | 0 | sano |
| venliq | no-RI | reconocido | vigente | 10 | 16 | 0 | 0 | cid,paginas_sin_seccion |
| verac | no-RI | reconocido | sin_raiz | 5 | 3 | 0 | 0 | sano |

```bash
python3 -c "import json; c=json.load(open('data/experiment/segmentacion_84/b584_particion/conteos_b584.json')); print(len(c), sum(d['unidades_extraccion'] for d in c.values()), sum(d['paginas'] for d in c.values()))"
```
