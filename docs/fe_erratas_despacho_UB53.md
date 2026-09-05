# Fe de erratas — el despacho fantasma de U-B5.3

**Estado: FIRMADA — Agustina Videla Rivero, 05/09/2026.** Redactada por la
instancia del plan, que origina el error y lo asume; la mesa revisora
asume no haberlo detectado en revisión.

## El hecho

El registro del proyecto afirmó desde el 04/09/2026 que la unidad U-B5.3
(reintento por `max_tokens`, cola entrada 1) estaba **«despachada y en
curso»**. Era falso: **el mandato nunca se despachó**. El bloque que lo
afirmaba fue redactado por la instancia del plan dando por ejecutada una
acción que solo la autora ejecuta, la autora lo pegó sin ejecutarla, y las
revisiones posteriores repitieron la afirmación. U-B5.3 se despacha recién
el **05/09/2026**, con este documento como registro de la corrección.

## Dónde se propagó la afirmación falsa

- **Laudo B5.5 firmado** (`docs/laudo_B5.5_alcance_corpus_y_catalogo.md`,
  commit `c0daef1`), checklist §6, entrada 1: «re-diferida con destino
  explícito — U-B5.3, **despachada y en curso**». Lo falso es el estado
  («despachada y en curso»); la sustancia del ítem — re-diferida con
  destino explícito, el escalado no arranca sin su cierre — era y sigue
  siendo cierta.
- **Laudo B5.4 fase 1 firmado** (`docs/laudo_B5.4_fase1_catalogo.md`,
  commit `dea56ba`), sección Firma: «U-B5.3 **sigue en vuelo**».
- **Plan** (`docs/plan_tesis.md`): fila B5.5 («entrada 1 re-diferida a
  B5.3 **en curso**») y bloque de la reunión del 04/09 (orden operativo
  que la daba en vuelo). Se corrigen con el pase que acompaña esta fe de
  erratas.
- **Mandato de U-B5.4** (texto de sesión): la frontera «U-B5.3 (en vuelo):
  PROHIBIDO tocar el call-site» — la prohibición era y sigue siendo
  correcta con independencia del estado del despacho; solo el rótulo de
  estado era falso.
- Mensajes de commit `c0daef1` y `dea56ba`: no se enmiendan (regla del
  proyecto); manda el estado de los archivos más esta fe de erratas.

Los dos laudos firmados no se editan: quedan con la afirmación errada y
esta fe de erratas los supersede en ese punto.

## Causa raíz y por qué la disciplina vigente no lo atrapó

La disciplina del circuito verifica afirmaciones **contra archivos del
repo**. Un despacho de mandato (como un commit no corrido o una firma no
dada) **no deja rastro en el repo hasta que su primer freno vuelve**: la
afirmación era inverificable por la vía habitual, y la única evidencia
admisible — la confirmación explícita de la autora — no existía ni fue
exigida. El mismo mecanismo produjo el episodio del commit de U-B5.1
(mensaje preparado, commit no corrido, detectado tarde por `git log`).

## Remedio sistémico

Regla nueva del circuito (CLAUDE.md §4.j, commiteada por separado):
ninguna acción de la autora se afirma como hecha sin su confirmación
explícita; hasta entonces se escribe como pendiente o preparada.

## Qué NO cambia

- La condición operativa del gate: **el escalado no arranca sin el cierre
  de U-B5.3** (laudo B5.5 §6, entrada 1).
- Las fronteras declaradas en los mandatos en vuelo.
- Ningún número, medición ni laudo sustantivo depende del estado del
  despacho.

## Firma

**Firma: Agustina Videla Rivero · Fecha: 05/09/2026.**
