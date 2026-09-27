# Tabla resumen y comparación contra el resultado esperado — U-B2.1 fase 1 (re-diagnóstico), pieza b

Todo conteo de este archivo se recomputó contra la tabla de la pieza a
(`inventario_B21_fase1.md`, sección 2, columnas «Conv.» y «Retr.») con el
comando de §3, ANTES de escribirse. El resultado esperado es el de la decisión 5
del mandato (`docs/mandatos/UB21_fase1_rediagnostico.md`), asentado en la fila
B2.1 del plan (`docs/plan_tesis.md`, HEAD `:324`). Toda diferencia se reporta
como HALLAZGO; ni el conteo ni la clasificación se ajustan.

## 1. Conteos (recomputados)

| Magnitud | Medido | Desglose |
|---|---|---|
| Ítems del inventario | **46** | 12 BKL + 12 RT + 12 (T1–T7, I1–I5) + 10 E4 = 46 |
| Grupo (i) BKL cerrados | 12 | BKL-0003, 0004, 0005, 0006, 0007, 0017, 0019, 0023, 0026, 0027, 0028, 0029 |
| Grupo (i) preguntas RT | 12 | RT-C5-1..5, RT-C6-1..4, RT-C7-1..3 |
| Grupo (ii) T1–T7 e I1–I5 | 12 | 7 + 5 |
| Grupo (iii) reglas de E4 | 10 | E4-a1..a8, E4-b, E4-c |
| Convertibles | **19** | BKL: 0017, 0006, 0023, 0004, 0003, 0005, 0007 (7) · RT: C5-4, C5-5, C6-4, C7-1, C7-2, C7-3 (6) · T1, T2, T3, I3, I4, I5 (6) · E4: 0 |
| Con condición | **23** | BKL: 0019, 0028, 0029 (3) · RT: C5-1, C5-2, C5-3, C6-1, C6-2, C6-3 (6) · T4, T5, T6, T7 (4) · E4: las 10 |
| No convertibles | **4** | BKL-0026, BKL-0027, I1, I2 |
| Suma 19 + 23 + 4 | 46 | cierra contra las 46 filas |
| Dependen del retriever | **15** | BKL: 0017, 0019, 0004, 0003, 0005 (5) · RT: C5-1, C5-2, C5-3, C5-4, C6-1, C6-2, C6-3, C7-1, C7-2, C7-3 (10) · grupos ii y iii: 0 |

Por grupo (convertible / con condición / no convertible / retriever):
BKL 7 / 3 / 2 / 5 · RT 6 / 6 / 0 / 10 · T–I 6 / 4 / 2 / 0 · E4 0 / 10 / 0 / 0.

Familias de condición sobre las 23 filas `con condición` (una fila puede estar
en más de una; recuento por enumeración, verificable contra la columna
«Condición» de la pieza a):
- catálogo parametrizado, 12: T7, E4-a1, E4-a2, E4-a3, E4-a4, E4-a5, E4-a6,
  E4-a7, E4-a8, BKL-0028, BKL-0029, RT-C6-3;
- consultas del proxy RT no registradas en el repo, 6: RT-C5-1, RT-C5-2,
  RT-C5-3, RT-C6-1, RT-C6-2, RT-C6-3;
- fixture o grafo de referencia, 6: T4, T5, T6, E4-a8, E4-b, BKL-0019;
- política de cuarentena por generación, 2: BKL-0019, T7;
- artefacto que no es un grafo o grafo que hoy no existe, 3: E4-c, BKL-0028,
  BKL-0029.
Unión de las cinco listas = las 23 filas (12 + 5 nuevas de la segunda + 5
nuevas de la tercera + 0 + 1 = 23). El adaptador de provenance gen 1/2/3 se
contó como infraestructura de la suite y no como condición (criterio §1 de la
pieza a): toda fila direccionada por ancla lo necesita, y además T1, T2, T3 e
I5 tal como están escritos fallan por formato sobre gen 1/2, y T7 por el
booleano de `cuarentena` en gen 2.

## 2. Comparación fila por fila contra el resultado esperado (decisión 5)

| # | Magnitud | Esperado (decisión 5) | Medido | coincide / HALLAZGO | Evidencia |
|---|---|---|---|---|---|
| 1 | Total de ítems | 46 | 46 | coincide | recuento §3: «filas: 46» |
| 2 | BKL cerrados (estado efectivo verificado) | 12: 0003, 0004, 0005, 0006, 0007, 0017, 0019, 0023, 0026, 0027, 0028, 0029 | 12, los mismos ids; 0 en `aplicado` sin `verificado` posterior; 17 `triaged` | coincide | `estado_backlog_B21_fase1_salida.txt` («CERRADOS … 12», «estado efectivo por valor: {'triaged': 17, 'verificado': 12}»); 74 líneas / 29 ids / 0 ids `RT-` |
| 3 | Preguntas RT | 12: RT-C5-1..5, RT-C6-1..4, RT-C7-1..3, en propuestas y retest C7 | 12, localizadas: `E4_enumeracion_65.md:227-247` (RT-1..5), `E3_salvedad_mutuales.md:151-179` (RT-1..4), `C7_retest_2026-08-03.md:78` (RT-1..3); ids `RT-C5-*`/`RT-C6-*` además en las trazas `posthoc_run/traces/rt_c5_c6/reensamblado_v3/` | coincide | `grep -n "RT-[1-5]" data/backlog/propuestas/E4_enumeracion_65.md data/backlog/propuestas/E3_salvedad_mutuales.md data/backlog/retests/C7_retest_2026-08-03.md`; `ls data/experiment/evaluacion/posthoc_run/traces/rt_c5_c6/reensamblado_v3/` |
| 4 | T1–T7 e I1–I5 | 12 | 12 | coincide | `r1_tests.py:1-15` (T1–T7), `r1_invariantes.py:7-12` (I1–I5) |
| 5 | Reglas de E4 | 10 | 10 (a1–a8, b, c; numeración de esta unidad, `inventario` §2.iii) | coincide en el total; la partición en 10 es de esta unidad (el mandato enumera 7 rótulos: 5 criterios, TextoOrdenado, filtro; a6–a8 salen del docstring `r1_e4.py:7-9,18-24`). La partición original NO está registrada en el repo. | `r1_e4.py:5-36` |
| 6 | Convertibles | 14 | **19** | **HALLAZGO** | recuento §3. Bajo el criterio declarado en la pieza a §1 (adaptador de provenance como infraestructura; «byte-idéntico» fuera de forma), 5 filas más quedan convertibles. Los ids que no pueden compararse uno a uno porque la clasificación del 15/09 no está registrada; candidatas a diferir (las que dependen solo del adaptador o de la regla «fuera de forma»): T1, T2, T3, I5, RT-C5-5, RT-C6-4, BKL-0007. Sin ajuste. |
| 7 | Con condición | 28 | **23** | **HALLAZGO** | recuento §3; es la contraparte de la fila 6 (19 + 23 = 42 = 14 + 28). |
| 8 | No convertibles | 4: BKL-0026, BKL-0027 (conducta del agente); I1, I2 (grafos pre-merge) | 4, los mismos ids y las mismas razones | coincide | `inventario` §2.i (0026, 0027) y §2.ii (I1, I2) |
| 9 | Dependen de retriever | 15 | 15 | coincide | recuento §3, lista: 0017, 0019, 0004, 0003, 0005, RT-C5-1..4, RT-C6-1..3, RT-C7-1..3. Criterio: el rank sostiene el PASS del cierre. BKL-0006 (C2) NO cuenta porque su paso (5) es «informativo, sin criterio de corte» (`C2_retest_2026-07-31.md:59`); si se contara, serían 16. Los ids de la lista del 15/09 no están registrados. |
| 10 | Contradicción 1: C4 (`subclase_de` laudada en KG-Refinado) contra T7 de r1 (`padre_sugerido` flaggeado) | registrada | medida: T7 FAIL sobre KG-Refinado con 19 malos = 8 «subclase_de desde propuesto» + 11 «sin cuarentena=true» | coincide (con matiz nuevo: gen 2 guarda `cuarentena` como booleano; `r1_tests.py:68` compara con la string `"true"`) | `sonda_T1_T7_cuatro_grafos_UB21_salida.txt` (KG-Refinado, T7); `sonda_anclas_C1_C7_UB21_salida.txt` (`C4.8_subclase_de_laudadas` PASS en KG-Refinado, `C4.8_padre_sugerido_flaggeadas` FAIL) |
| 11 | Contradicción 2: BKL-0024/0025 nombrados «cerrados» en el plan y `triaged` en el backlog | registrada | plan HEAD `:324` «cada BKL cerrado (C1–C7, BKL-0024/0025, RT-*)»; backlog: estado efectivo `triaged` (líneas 57 y 59) | coincide | `git show HEAD:docs/plan_tesis.md \| grep -n -o "cada BKL cerrado (C1–C7, BKL-0024/0025, RT-\*)"` → `324:`; `estado_backlog_B21_fase1_salida.txt` |
| 12 | Regla de estado efectivo del backlog: 74 líneas, 29 ids, 12 `verificado` | declarada | 74 / 29 / 12; orden de archivo = orden cronológico de los `ts` con estado (True) | coincide | `estado_backlog_B21_fase1_salida.txt` |
| 13 | sha256 de los 4 insumos y los 4 grafos | 8 declarados | 8 iguales | coincide | `inventario` §0; cada sonda verifica los 4 sha antes de correr |
| 14 | Tres sondas (la fase 1 original tuvo tres) | 3 | 3: `sonda_T1_T7_cuatro_grafos_UB21.py`, `sonda_anclas_C1_C7_UB21.py`, `sonda_ranks_buscar_nodos_UB21.py` (la tercera sondea la forma «rank en buscar_nodos» con el retriever in-memory) | coincide en número; el nombre de la tercera original no está registrado | este directorio |

## 3. Comando de recuento (pegado con su salida)

```
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
import re, collections
txt = open("reports/revision_UB21_diag/inventario_B21_fase1.md", encoding="utf-8").read()
sec = txt.split("## 2. Inventario")[1].split("## 3. Solapamientos")[0]
filas = []
for l in sec.splitlines():
    if not l.startswith("| "): continue
    c = [x.strip() for x in l.strip().strip("|").split("|")]
    if len(c) != 10 or c[0] in ("Id",) or set(c[0]) <= set("-"): continue
    idv = c[0].split(" ")[0]
    if not re.match(r"^(BKL-\d{4}|RT-C[567]-\d|T[1-7]|I[1-5]|E4-[abc]\d?)$", idv):
        print("FILA NO RECONOCIDA:", c[0]); continue
    grupo = ("i-BKL" if idv.startswith("BKL") else "i-RT" if idv.startswith("RT") else "ii" if idv[0] in "TI" else "iii")
    filas.append((grupo, idv, c[6], c[7].split(" ")[0]))
print("filas:", len(filas))
g = collections.Counter(f[0] for f in filas); print("por grupo:", dict(g))
cv = collections.Counter(f[2] for f in filas); print("convertibilidad:", dict(cv))
rt = collections.Counter(f[3] for f in filas); print("retriever:", dict(rt))
print("convertibles:", [f[1] for f in filas if f[2]=="convertible"])
print("con condicion:", [f[1] for f in filas if f[2]=="con condición"])
print("no convertibles:", [f[1] for f in filas if f[2]=="no convertible"])
print("dependen del retriever:", [f[1] for f in filas if f[3]=="sí"])
for grp in ("i-BKL","i-RT","ii","iii"):
    sub=[f for f in filas if f[0]==grp]
    print(grp, "n=",len(sub), "conv=",sum(1 for f in sub if f[2]=="convertible"), "cond=",sum(1 for f in sub if f[2]=="con condición"), "noconv=",sum(1 for f in sub if f[2]=="no convertible"), "retr=",sum(1 for f in sub if f[3]=="sí"))
ids=[f[1] for f in filas]; print("ids duplicados:", [i for i,n in collections.Counter(ids).items() if n>1])
PY
```

```
filas: 46
por grupo: {'i-BKL': 12, 'i-RT': 12, 'ii': 12, 'iii': 10}
convertibilidad: {'convertible': 19, 'con condición': 23, 'no convertible': 4}
retriever: {'sí': 15, 'no': 31}
convertibles: ['BKL-0017', 'BKL-0006', 'BKL-0023', 'BKL-0004', 'BKL-0003', 'BKL-0005', 'BKL-0007', 'RT-C5-4', 'RT-C5-5', 'RT-C6-4', 'RT-C7-1', 'RT-C7-2', 'RT-C7-3', 'T1', 'T2', 'T3', 'I3', 'I4', 'I5']
con condicion: ['BKL-0019', 'BKL-0028', 'BKL-0029', 'RT-C5-1', 'RT-C5-2', 'RT-C5-3', 'RT-C6-1', 'RT-C6-2', 'RT-C6-3', 'T4', 'T5', 'T6', 'T7', 'E4-a1', 'E4-a2', 'E4-a3', 'E4-a4', 'E4-a5', 'E4-a6', 'E4-a7', 'E4-a8', 'E4-b', 'E4-c']
no convertibles: ['BKL-0026', 'BKL-0027', 'I1', 'I2']
dependen del retriever: ['BKL-0017', 'BKL-0019', 'BKL-0004', 'BKL-0003', 'BKL-0005', 'RT-C5-1', 'RT-C5-2', 'RT-C5-3', 'RT-C5-4', 'RT-C6-1', 'RT-C6-2', 'RT-C6-3', 'RT-C7-1', 'RT-C7-2', 'RT-C7-3']
i-BKL n= 12 conv= 7 cond= 3 noconv= 2 retr= 5
i-RT n= 12 conv= 6 cond= 6 noconv= 0 retr= 10
ii n= 12 conv= 6 cond= 4 noconv= 2 retr= 0
iii n= 10 conv= 0 cond= 10 noconv= 0 retr= 0
ids duplicados: []
```

## 4. Resultados de las sondas que sostienen la comparación (resumen; salidas completas en este directorio)

| Sonda | Lo que midió | Resultado clave |
|---|---|---|
| `sonda_T1_T7_cuatro_grafos_UB21` | T1–T7 (`r1_tests.correr_tests`) e I3–I5 sobre los 4 grafos | r1 7/7 y recomputo byte-idéntico al sellado (dict completo); KG-Reextraído T1–T3 idéntico al sellado, T4/T5/T6 FAIL; KG-Refinado T1/T2/T3/T5 FAIL por formato gen 2, T4 FAIL (90 ≠ 82), T7 FAIL (contradicción 1); KG-Base solo T6/T7 (vacuo) PASS, I5 FAIL por formato |
| `sonda_anclas_C1_C7_UB21` | anclas de C1–C7 y BKL-0024/0025 direccionadas sin id (26 comprobaciones por grafo) | KG-Refinado: 25 de 26 PASS; la única FAIL es `C4.8_padre_sugerido_flaggeadas` (política gen 3, esperada); gen 3: C1 y C7 resueltos por el pipeline, C6 presente sin `establecida_en`, C2 invertido (RX-10 persiste), C3 sin nodo, C5 5/9, C4 0/8 laudadas y 3/8 flaggeadas en r1; KG-Base: C2 correcto, casi todo lo demás ausente (recuento por columna en `manifest.txt`) |
| `sonda_ranks_buscar_nodos_UB21` | 27 consultas selladas + posición en `ver_vecinos` (C4 e) con `GraphIndex` | KG-Refinado: 27/27 consultas con todos sus objetivos en el rank esperado y posición 6 de 145 (coincide); gen 3: 6/27, 16 objetivos ausentes; KG-Base: 0/27 |

Determinismo: cada sonda imprime el sha256 del JSON canónico de sus resultados;
segunda corrida de los cuatro scripts byte-idéntica (`cmp`, ver `manifest.txt`).
