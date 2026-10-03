# Fe de erratas — la frase «la resuelve E3» está en la ficha 44, no en la 39

**Estado: FIRMADA por la autora el 03/10/2026.**

## El hecho

Dos documentos de ESQ, la tabla de resultados de ESQ-2 (aprobada por la autora, `bbac990`) y el laudo
ESQ-3a (firmado), atribuyen a la ficha 39 una frase que está en la ficha 44:

- la tabla de resultados de ESQ-2, fila «vínculo normativo cross-unidad»: «**E3** (f. 39: «la cross-unidad
  la resuelve E3»)» (`git show bbac990:data/experiment/esq/cobertura/tabla_resultados_esq2.md`, `:92`);
- el laudo ESQ-3a: «vínculo normativo cross-unidad (f. 39: «la resuelve E3»)»
  (`git show 0a76549:data/experiment/esq/laudo_ESQ-3a_retoques.md`, `:225`).

La frase está en las observaciones de la ficha 44 (`lavdin::3.3.5`): «…la cross-unidad la resuelve E3, la de
la familia marcada NO la resuelve ningún…»
(`data/experiment/esq/cobertura/fichas/worksheet_fichas_esq2.json:5412`). La ficha 39 (`lavdin::3.3.4.3`) no
la contiene: en todo el worksheet la frase aparece una sola vez, en la ficha 44.

## Qué se corrige

En las dos citas, donde dice «f. 39» se lee «f. 44». Los dos documentos no se editan: quedan con la
atribución errada y esta fe de erratas los supersede en ese punto.

## Dónde más aparece

En ningún otro archivo versionado al 03/10/2026 (`e7f7a2e`): fuera del worksheet, `git grep "resuelve E3"`
sobre `docs/`, `data/experiment/esq/`, `data/backlog/` y `reports/` solo devuelve esas dos líneas y la fila
de otra familia, que cita la ficha 71 (`tabla_resultados_esq2.md:84`). El mandato de U-DIAG-PROCESO ubica la frase en la ficha 44
(`docs/mandatos/UDIAG_proceso.md`, `f8cf89a`).

## Qué NO cambia

- Las fichas de la familia siguen siendo la 18, la 39, la 61 y la 72, con 1 de las 38 azarosas y 3
  dirigidas (`tabla_resultados_esq2.md:92`). La ficha 44 no se suma: registra la pérdida entre unidades
  como una segunda pérdida, fuera de la familia que marcó, por el límite de una familia por ficha.
- La ficha 39 sigue siendo la única azarosa de la familia.
- La atribución de la familia a E3 en la tabla y en el laudo no se toca acá. Que ninguna pieza del
  pipeline la resuelva hoy es un hallazgo aparte, de U-DIAG-PROCESO (`docs/plan_tesis.md:398`).

## Cómo se detectó

Al leer las diez fichas para U-DIAG-PROCESO. Las dos ejecuciones independientes de esa unidad llegaron a
lo mismo (`reports/u_diag_proceso/reporte_u_diag_proceso.md`, §2, y `replica_paralela/`). La causa del
cruce entre las dos fichas es NO VERIFICADA; las dos son del mismo TO y de la misma sección (3.3).

## Firma

FIRMADA por la autora el 03/10/2026.
