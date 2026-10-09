# U-SEG-OFICIAL — FRENO S0-5a (09/10/2026)

Mandato `docs/mandatos/USEG_OFICIAL_S0-5a_reglas_de_corte_E0.md` leído en `b60e2fc9` (`4f4ca6c9…`), con la nota del
control de continuidad. USD 0, sin API. **Nada commiteado; el parche no se aplicó al repo** (es S0-5b). Detalle:
`REPORTE_S0-5a.md`; diseño y desvíos: `DISENO_S0-5a.md`; censos: `censos/`.

**Antes**: HEAD `b60e2fc9` con el mandato y la nota; la nota del 09/10 (mediodía) en `bbcfb457`; E0 del repo `65a8c3b8…` /
`94d35349…` / `ec186071…`; foto sha256 del repo (48.242 archivos) y 2.213 `.pyc`.

**Lo hecho, sobre una copia del repo sin enlaces**: las seis reglas con su interruptor y su alcance; tolerancia de R5-a
fijada antes del censo, **`TOL_COL_R5A = TOL_X` = 3,0 pt**. Parche `parche/parche_e0_S0-5a.diff` (`c6558ea0…`; +724 −21
en los tres archivos), probado en seco sobre los archivos de partida: rc 0 y los tres sha256 finales (`4d0abc1a…`,
`ed276d43…`, `9f2fbf28…`).

**Controles** (REPORTE §2):
- todas apagadas = S0-4b, 768 de 768;
- todas prendidas, dos veces: 768 de 768 iguales entre sí, y el código final sin interruptor, igual: **9.665 unidades**
  (9.625 en S0-4b);
- tanda 0, código final, dos veces: **57 de 57**; los 25 de la tanda 0 dentro de los 152, 25 de 25;
- `selftest_e0` 169/169; b52 39/39, b581 34/34, b582 59/59, b583 33/33;
- claves de la caché: VEREDICTO OK, igual byte a byte a `923dd900…`;
- selftest de claves de S0-5a: VEREDICTO OK, y FALLA con la lista perturbada;
- selftest del control de continuidad: 14/14.

**Aceptación** (REPORTE §3): R5-a 9 de 9 casos, y los 27 correctos iguales (unidad entera). R5-a′:
`ri_oc::C.11` conserva 2 renglones y 75 van a `ri_oc::Sbloque1`; ninguna herencia de C.1 a C.11 tiene el bloque. R5-b:
los pares del censo de la mesa, ni uno más. R5-c 9 de 9 y 4 de 4. R5-d: ri_rml y snp_tr como pide la nota corregida;
los 4 encabezados siguen (`gerc::2.4.2` cambia solo la herencia, por el cierre que abre R5-a). R5-e: «CODIGO» junto,
sin letras sueltas.

**Censo por regla** (REPORTE §4; `censos/censo_por_regla_S0-5a.md`, `antes_y_despues_S0-5a.jsonl`):

| regla | TOs | creadas | quitadas | cambiadas |
|---|---|---|---|---|
| R5-a | 38 | 57 | 3 | 211 |
| R5-a′ | 1 | 1 | 1 | 11 |
| R5-b | 2 | 0 | 21 | 20 |
| R5-c | 4 | 0 | 9 | 105 |
| R5-d | 2 | 17 | 1 | 11 |
| R5-e | 1 | 0 | 0 | 2 |
| todas | 42 | 75 | 35 | 343 |

De los 453 eventos, 446 son de una regla sola; 7 son R5-a con R5-c (`manual::2.3`, `ri_spi::C.1`). Claves: la lista de
las 453, con su regla, en `censos/claves_S0-5a.json` (REPORTE §5).

**Para la decisión de la autora:**
1. **El alcance de R5-a.** Con el del mandato (las listas del detector), R5-a mueve 186 párrafos (997 renglones) en 57
   listas de 38 TOs, y todo lo que mueve lo heredan los hermanos del ítem. Fuera de los 9 casos, mi lectura a la vista
   del texto, sin la página y sin adjudicar (`censos/lectura_r5a_S0-5a.md`): **29 con forma de cierre, 13 que no son
   cierre, 6 dudosas.** Las 13: formularios y modelos de nota (apnf 1.3.2.5, cryl 12.2, gescre 1.2.8.2, inspag 3.3.2,
   manori 3.5.2), el cuerpo de un ítem (cirmo3 1.2.11.3 y 1.2.23.3, ri2_ae 14.3), un título partido (gerc 2.4.3), la
   sección 5 que E0 no abrió (ri2_ae 3.3), bloques con título u otra parte del documento (ri_ot 13.4, ri_pnp 5.7,
   ri_spi C.1.3). **En la tanda 1, fuera de los casos: 6 listas, 2 cierres (efemin 2.3.2, manori 1.1.6.5), 1 dudosa
   (ri_rml 1.4.2) y 3 que no son cierre (cirmo3 ×2, manori 3.5.2).** Opciones: R5-a por lista (los 9 y los que la
   autora confirme); o una guarda nueva, con un censo nuevo. No ajusté nada después del censo.
2. **R5-a mueve renglones de tablas** (error mío de diseño: la regla no excluye las tablas de `e0_tablas`). Dejan de
   serializarse 3 tablas (manori `tabla014` y `tabla015`, ri_spi `tabla001`; de 468 quedan 465), una pasa entera al
   cierre (ri_spi `tabla000`) y dos quedan repartidas entre el ítem y el cierre (gescre `tabla001`, gerc `tabla004`)
   (`censos/tablas_S0-5a.json`). Las cuatro listas son de las que leo como «no es cierre».
3. **Los candidatos de R5-a′ fuera de ri_oc**: 24 con el criterio de la regla (los 27 de la mesa no se reproducen: su
   heurística no está versionada). Mi lectura: 7 títulos de bloque, 2 bloques sin título, 3 dudosos, 12 falsos
   positivos; en la tanda 1, solo `ri_rml::1.2.3`, dudoso (`censos/lectura_candidatos_r5a2_S0-5a.md`). Fuera de ri_oc,
   R5-a lleva al cierre el bloque de 12 candidatos (10 de los 24 y los 2 que aparecen sobre S0-5a); con un padre
   punto, la regla no tiene adónde abrir el bloque.
4. **La clave de R5-a′**: `ri_oc::Sbloque1` (propuesta; el mandato no fija el número).
5. **Continuidad de la numeración** (`censos/lista_continuidad_S0-5a.md`): antes, 104 saltos en 15 TOs (los 25 del
   prototipo de la mesa, con su clase, y 79 de 6 TOs sin raíz que no recorre); después, 98: se cierran los 6 de la
   aceptación y no aparece ninguno. **Tanda 1, para regla por lista: 12** (ri_ccna 11, rótulos pegados en D1A1 y
   D1A2; snp_cheq 3.3.6, (i) con 3.3.6.2 tragado). Fuera de la tanda 1, a límite y grupo 2: 71; tanda 0: 1 (la
   remisión de ctacte).
6. **S1-ter no ve los falsos positivos de R5-a**: 42 de las 57 listas dejan de ser candidatas del detector del 1.16
   (sobre S0-5a: 277, sobre S0-4b: 317).

**Discrepancias con el mandato** (DISENO §3): pares (ii) de R5-b, 19 en el mandato y 18 en el censo de la mesa que cita
(mi salida une los 18, más 7+8 por (i′)); R5-a no recorre las listas de secciones del detector (no tienen un padre al
que mover el párrafo); R5-a′ solo con un padre sección; R5-d como veto; R5-e sobre el árbol.

**El control que ya existía** (pregunta de la autora; REPORTE §6): el censo del punto 7 de S0-1, corrido sobre una
copia, da 12 sobre S0-4b, la cifra de la nota. Solo mira los rechazos por «padre no abierto» (ve 1.3.4 a 1.3.6 de
snp_tr, no 1.4 ni 1.5), corrió en S0-1 y S0-1 bis y no después, y ningún script de U-SEG-OFICIAL lee los
`saltos_numeracion` que E0 registra.

**Límites declarados del §3** (REPORTE §8): `ri_iepsp::S0` y `ri_ieccm::S0`; el encabezado repetido en 7 unidades de
ri_icpipsp; `ri_secoexpo::S17` (5.271 caracteres); `ri_mmsef::2.2::intro` (465, una unidad); la tanda 0 fuera, donde R5-a
crearía 15 cierres en 7 TOs y cambiaría 63 unidades.

**Tabla de reprocesamiento**: fila F19c propuesta (REPORTE §9); su variación del selftest queda PENDIENTE para S0-5b.

**Repo** (foto sha256 a las 13:09:09, `s0_1/scripts/snapshot_repo.py`; REPORTE §11): 48.242 → 48.307 archivos;
64 nuevos en `s0_5/`, ninguno borrado; fuera de `s0_5/`, solo cambios ajenos a esta sesión (abajo). `.pyc` fuera de
`.venv/`: 2.213, la misma lista que al empezar. Grep de convenciones sobre `s0_5/` (63 archivos): 69 coincidencias, todas
en texto del corpus copiado en los censos (campos de formularios y prosa de las normas); ningún nombre, ninguna referencia al
origen de una decisión, ninguna ruta absoluta (`censos/grep_convenciones_S0-5a.txt`).

**Cambios ajenos a esta sesión** (no los escribí: en el registro de la sesión solo hay lecturas de esos archivos):
`docs/laudo_B2.4_sujetos.md`, `docs/plan_tesis.md` y `docs/tablero.md`, modificados a las 11:22, después de la foto
inicial (11:15:57); y `docs/mandatos/UOMISIONES_COD_release_codigo_ensamblado.md`, nuevo, de las 12:56.
Los cuatro están en commits que no son de esta sesión (`git log`): `3be6ebc3` (12:46, los tres de `docs/`) y
`39e2994f` (13:12, el mandato); HEAD es ahora `39e2994f`. El commit preparado agrega solo `s0_5/`.

**Paquete** `revision_USEG_OFICIAL_FRENO_S0-5a/` (82 archivos y `manifest.txt`; 131 MB): FRENO, informe y diseño; el
parche, los interruptores y el LEEME; los tres archivos finales de E0; los scripts y los censos de `s0_5/`; las fotos
del repo y los logs; y tres tar.gz con las salidas de E0 (la final de los 152, las seis reglas solas, y la tanda 0 dos
veces y sin la exclusión). Copia permanente con `ditto` en
`~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/0c0c6584-4c87-4d3c-b3b4-425c9ab87db2/scratchpad/revision_USEG_OFICIAL_FRENO_S0-5a/`:
**82 de 82 iguales a su `manifest.txt`** (sha256 y bytes), ninguno sin listar.

**Mensaje de commit PREPARADO** (no corrido; probado en un repo descartable: `git log --oneline` muestra solo el
título; sin ids de los 152 TOs ni de unidades, sin nombres de mecanismos):

```
git add data/experiment/segmentacion_oficial_e0r2/s0_5
git commit -m "U-SEG-OFICIAL S0-5a: reglas de corte de E0 en una copia, con sus censos (USD 0, sin API)" -m "Registro de S0-5a: el diseño, el informe y el FRENO; el parche de E0 para S0-5b, sin aplicar, con los dos interruptores de medición, que no van al repo; los scripts de los censos, de la aceptación, de las claves y de los controles nuevos, con sus selftests; y los censos, los controles y las listas para la decisión de la autora. La salida de E0 no entra al repo: queda en el paquete de revisión, con su manifiesto."
```
