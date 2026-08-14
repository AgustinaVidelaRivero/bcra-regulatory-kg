# Reporte — eje de navegabilidad EV2 (corrida base, replay determinístico)

Unidad determinística, $0, sin ninguna llamada a API. Protocolo vinculante:
`docs/protocolo_corrida_ev2.md`. Trazas de la corrida base commiteada
(`data/experiment/ev2_corrida/trazas/`, commit bb89a8e). Métrica invocada sin
edición: `data/experiment/ev2_corrida/code/metrica_ev2.py` (agregación POR
ANCLA; replay estándar contra `trace.steps` + replay FUERTE con igualdad
exacta contra `steps_full`). Las trazas del eje de fidelidad (EV2F-*) no se
abrieron: filtrado por nombre de archivo en el driver.

Reproducción (desde `data/experiment/ev2_corrida/navegabilidad/`):

```
python3 -B replay_navegabilidad_ev2.py      # replay 3 labels -> resultados_navegabilidad_<label>.json
python3 -B agregados_navegabilidad_ev2.py   # agregados        -> agregados_navegabilidad.json
```

## 1. Verificaciones previas

sha256 de los tres grafos verificados contra los sellados
(`comun_ev2.verificar_grafos`, output del replay):

```
sha256 OK  v2:    8e2eadee57b48e00ccb51ade9a953ba1469001fe089c45d97c4307ccf2725581  data/experiment/reextraccion_v2/corpus_v2/salida/kg.json
sha256 OK  v3:    26fac8b49f6c08c1aa364b47273d36958d831f240d4e6b4ee7700b6a0bff3571  data/experiment/grafo_v2/reensamblado_v3/kg.json
sha256 OK  run_3: 12c226e22b8fdc8f46999cae7f1eb808930e71f5dfe803f3a4f637a88348c410  data/experiment/run_3_ppf_core/kg.json
```

Cuarteto de evaluación intocado (sha256 idénticos al inicio y al final de la
sesión; `shasum -a 256` en `data/experiment/evaluacion/`):

```
5aba8b7a0aa46e8d5c4c83b33884b8cae7d0a099884a7d3bc935de4d3097af8b  loader.py
fd267e833866f86850e43130e627b08d78e05523b97484696de0ab0c8c9fba9e  harness.py
7169145aaeb3f2d90a7e3873964378aa6520c5688fed136cf5a79ea63b589eaa  judge.py
fc86b0e48df464d01d87aa1d8067168d2d522f66ead53f594092a16484c22752  llm_cache.py
```

## 2. Replay determinístico

336/336 trazas de navegabilidad replayadas (v2 88, v3 128, run_3 120), ids
únicos por label, replay estándar Y replay fuerte OK en la totalidad:

| label | grafo | trazas replayadas | replay_ok todos | replay_fuerte_ok todos | divergencias |
|---|---|---|---|---|---|
| ev2_base_v2 | v2 | 88 | sí | sí | 0 |
| ev2_base_v3 | v3 | 128 | sí | sí | 0 |
| ev2_base_run3 | run_3 | 120 | sí | sí | 0 |

Fuente: `resultados_navegabilidad_<label>.json` (claves `replay_ok_todos`,
`replay_fuerte_ok_todos`; detalle por caso y por ancla dentro del mismo
archivo). Ningún caso con `n_anclas == 0`.

## 3. Definiciones (las de la métrica commiteada)

- **recall_micro**: `sum(n_vistas | n_consultadas) / sum(n_anclas)` sobre los
  casos de la celda (pooled por ancla).
- **recall_macro**: promedio simple de los recalls por caso de la celda.
- **brecha v-s-c**: anclas vistas en algún output pero jamás consultadas
  (`ver_nodo`/`ver_vecinos`).
- **Denominadores por grafo** = casos presentes según el censo commiteado
  (`censo/censo_navegabilidad_<grafo>.json`): v2 44, v3 64, run_3 60. Las
  ausencias NO cuentan como fallas de navegación (protocolo §2); van en §7.

Fuente de todos los números de §4–§7: `agregados_navegabilidad.json`.

## 4. Por grafo × variante (número central: brecha literal vs anti-léxica)

| grafo | variante | n_casos | n_anclas | vistas | consultadas | brecha v-s-c | recall vista micro | recall vista macro | recall consultada micro | recall consultada macro |
|---|---|---|---|---|---|---|---|---|---|---|
| v2 | literal | 44 | 48 | 29 | 19 | 10 | 0.6042 | 0.5909 | 0.3958 | 0.4205 |
| v2 | antilexica | 44 | 48 | 22 | 13 | 9 | 0.4583 | 0.4735 | 0.2708 | 0.2955 |
| v3 | literal | 64 | 71 | 71 | 68 | 3 | 1.0000 | 1.0000 | 0.9577 | 0.9609 |
| v3 | antilexica | 64 | 71 | 60 | 44 | 17 | 0.8451 | 0.8281 | 0.6197 | 0.6016 |
| run_3 | literal | 60 | 67 | 61 | 48 | 13 | 0.9104 | 0.9083 | 0.7164 | 0.7267 |
| run_3 | antilexica | 60 | 67 | 53 | 33 | 20 | 0.7910 | 0.8067 | 0.4925 | 0.5250 |

Brecha literal − antilexica (mismo denominador dentro de cada grafo; los
grafos NO se promedian entre sí):

| grafo | Δ recall vista micro | Δ recall vista macro | Δ recall consultada micro | Δ recall consultada macro |
|---|---|---|---|---|
| v2 (n=44+44) | 0.1459 | 0.1174 | 0.1250 | 0.1250 |
| v3 (n=64+64) | 0.1549 | 0.1719 | 0.3380 | 0.3593 |
| run_3 (n=60+60) | 0.1194 | 0.1016 | 0.2239 | 0.2017 |

## 5. Por grafo × estrato × variante

Recalls micro (pooled por ancla de la celda); macro por celda en
`agregados_navegabilidad.json` (clave `por_estrato_variante`).

### v2 (ev2_base_v2)

| estrato | variante | n_casos | n_anclas | vistas | consultadas | brecha v-s-c | recall vista micro | recall consultada micro |
|---|---|---|---|---|---|---|---|---|
| E-A | literal | 10 | 13 | 7 | 3 | 4 | 0.5385 | 0.2308 |
| E-A | antilexica | 10 | 13 | 5 | 2 | 3 | 0.3846 | 0.1538 |
| E-B | literal | 10 | 10 | 6 | 4 | 2 | 0.6000 | 0.4000 |
| E-B | antilexica | 10 | 10 | 7 | 4 | 3 | 0.7000 | 0.4000 |
| E-C | literal | 7 | 8 | 5 | 3 | 2 | 0.6250 | 0.3750 |
| E-C | antilexica | 7 | 8 | 2 | 1 | 1 | 0.2500 | 0.1250 |
| E-D | literal | 10 | 10 | 7 | 5 | 2 | 0.7000 | 0.5000 |
| E-D | antilexica | 10 | 10 | 6 | 4 | 2 | 0.6000 | 0.4000 |
| E-E | literal | 7 | 7 | 4 | 4 | 0 | 0.5714 | 0.5714 |
| E-E | antilexica | 7 | 7 | 2 | 2 | 0 | 0.2857 | 0.2857 |

### v3 (ev2_base_v3)

| estrato | variante | n_casos | n_anclas | vistas | consultadas | brecha v-s-c | recall vista micro | recall consultada micro |
|---|---|---|---|---|---|---|---|---|
| E-A | literal | 13 | 19 | 19 | 18 | 1 | 1.0000 | 0.9474 |
| E-A | antilexica | 13 | 19 | 18 | 15 | 3 | 0.9474 | 0.7895 |
| E-B | literal | 17 | 17 | 17 | 17 | 0 | 1.0000 | 1.0000 |
| E-B | antilexica | 17 | 17 | 15 | 14 | 1 | 0.8824 | 0.8235 |
| E-C | literal | 11 | 12 | 12 | 10 | 2 | 1.0000 | 0.8333 |
| E-C | antilexica | 11 | 12 | 11 | 5 | 6 | 0.9167 | 0.4167 |
| E-D | literal | 12 | 12 | 12 | 12 | 0 | 1.0000 | 1.0000 |
| E-D | antilexica | 12 | 12 | 8 | 6 | 3 | 0.6667 | 0.5000 |
| E-E | literal | 11 | 11 | 11 | 11 | 0 | 1.0000 | 1.0000 |
| E-E | antilexica | 11 | 11 | 8 | 4 | 4 | 0.7273 | 0.3636 |

### run_3 (ev2_base_run3)

| estrato | variante | n_casos | n_anclas | vistas | consultadas | brecha v-s-c | recall vista micro | recall consultada micro |
|---|---|---|---|---|---|---|---|---|
| E-A | literal | 13 | 19 | 17 | 14 | 3 | 0.8947 | 0.7368 |
| E-A | antilexica | 13 | 19 | 15 | 8 | 7 | 0.7895 | 0.4211 |
| E-B | literal | 17 | 17 | 16 | 14 | 2 | 0.9412 | 0.8235 |
| E-B | antilexica | 17 | 17 | 17 | 10 | 7 | 1.0000 | 0.5882 |
| E-C | literal | 10 | 11 | 9 | 6 | 3 | 0.8182 | 0.5455 |
| E-C | antilexica | 10 | 11 | 7 | 3 | 4 | 0.6364 | 0.2727 |
| E-D | literal | 10 | 10 | 9 | 6 | 3 | 0.9000 | 0.6000 |
| E-D | antilexica | 10 | 10 | 7 | 6 | 1 | 0.7000 | 0.6000 |
| E-E | literal | 10 | 10 | 10 | 8 | 2 | 1.0000 | 0.8000 |
| E-E | antilexica | 10 | 10 | 7 | 6 | 1 | 0.7000 | 0.6000 |

## 6. Cohortes (etiquetadas, jamás promediadas entre sí)

Núcleo limpio del eje sintético = estrato E-E; cohorte dirigida = E-A..E-D
(`docs/protocolo_corrida_ev2.md` §1). En v2 el núcleo limpio E-E son 7
samples presentes (de 11 aptos; 4 ausentes, §7).

| grafo | cohorte | variante | n_casos | n_anclas | vistas | consultadas | brecha v-s-c | recall vista micro | recall vista macro | recall consultada micro | recall consultada macro |
|---|---|---|---|---|---|---|---|---|---|---|---|
| v2 | núcleo limpio (E-E) | literal | 7 | 7 | 4 | 4 | 0 | 0.5714 | 0.5714 | 0.5714 | 0.5714 |
| v2 | núcleo limpio (E-E) | antilexica | 7 | 7 | 2 | 2 | 0 | 0.2857 | 0.2857 | 0.2857 | 0.2857 |
| v2 | dirigida (E-A..E-D) | literal | 37 | 41 | 25 | 15 | 10 | 0.6098 | 0.5946 | 0.3659 | 0.3919 |
| v2 | dirigida (E-A..E-D) | antilexica | 37 | 41 | 20 | 11 | 9 | 0.4878 | 0.5090 | 0.2683 | 0.2973 |
| v3 | núcleo limpio (E-E) | literal | 11 | 11 | 11 | 11 | 0 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| v3 | núcleo limpio (E-E) | antilexica | 11 | 11 | 8 | 4 | 4 | 0.7273 | 0.7273 | 0.3636 | 0.3636 |
| v3 | dirigida (E-A..E-D) | literal | 53 | 60 | 60 | 57 | 3 | 1.0000 | 1.0000 | 0.9500 | 0.9528 |
| v3 | dirigida (E-A..E-D) | antilexica | 53 | 60 | 52 | 40 | 13 | 0.8667 | 0.8491 | 0.6667 | 0.6509 |
| run_3 | núcleo limpio (E-E) | literal | 10 | 10 | 10 | 8 | 2 | 1.0000 | 1.0000 | 0.8000 | 0.8000 |
| run_3 | núcleo limpio (E-E) | antilexica | 10 | 10 | 7 | 6 | 1 | 0.7000 | 0.7000 | 0.6000 | 0.6000 |
| run_3 | dirigida (E-A..E-D) | literal | 50 | 57 | 51 | 40 | 11 | 0.8947 | 0.8900 | 0.7018 | 0.7120 |
| run_3 | dirigida (E-A..E-D) | antilexica | 50 | 57 | 46 | 27 | 19 | 0.8070 | 0.8280 | 0.4737 | 0.5100 |

## 7. Ausencias por grafo (fuera de la métrica; dato de fidelidad, protocolo §2)

Fuente: `censo/censo_navegabilidad_<grafo>.json` (censo commiteado, previo a
la corrida).

| grafo | n ausentes | ids ausentes |
|---|---|---|
| v2 | 20 | EA-013, EA-019, EA-020, EB-001, EB-003, EB-006, EB-014, EB-015, EB-016, EB-017, EC-002, EC-008, EC-012, EC-017, ED-002, ED-012, EE-001, EE-002, EE-013, EE-018 |
| v3 | 0 | — |
| run_3 | 4 | EC-014, ED-007, ED-017, EE-003 |

Presencias PARCIALES (casos evaluados con anclas individuales ausentes en el
grafo; esas anclas quedan fuera del denominador del caso, mismo protocolo):

| grafo | caso | anclas ausentes excluidas |
|---|---|---|
| v2 | EA-005::literal y EA-005::antilexica | ext:3.13, ext:4.6 |
| v2 | EA-016::literal y EA-016::antilexica | cap:2.6 |

## 8. Anomalías y notas de datos

1. **Divergencias de replay: 0** en 336/336 trazas (replay estándar y fuerte).
2. **EA-013::literal (run_3)** — traza con error 400 permanente del harness
   congelado documentado en el commit bb89a8e (`trace.error`:
   `BadRequestError ... 'messages.8: user messages must have non-empty
   content'`). La métrica se computó sobre sus 5 steps persistidos
   (`steps_full` = 5), como quedó ratificado: replay estándar y fuerte OK;
   resultado del caso: 1 ancla (ext:4.8), vista y consultada
   (recall_vista = recall_consultada = 1.0), sin brecha.
3. **Censo v3**: `n_provenances_sin_parsear: 1` (dato del censo commiteado,
   `censo/censo_resumen.json`); no afectó la resolución de ningún ancla gold
   (v3: 64/64 presentes completos).
4. Contenedores excluidos por el censo (regla sellada de resolución):
   v2 18, v3 20, run_3 0 (`censo/censo_resumen.json`).

## 9. Costo

USD 0. Ninguna llamada a API: replay y agregación puramente locales sobre
trazas persistidas y grafos verificados por sha256.
