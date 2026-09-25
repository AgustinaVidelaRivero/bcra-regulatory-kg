# Enmienda al laudo de esquema congelado — ventana de corrección única del §7 y la tanda 0

**FIRMADO por la autora — 2026-09-25** · Fecha: 2026-09-25.

Enmienda con fecha al laudo `data/experiment/esq/laudo_esquema_congelado.md`
(FIRMADO 03/09/2026, sellado en `2593d4d`), §7. El laudo **no se edita**: esta
enmienda vive al lado, como ya lo hace la fe de erratas
`fe_erratas_laudo_esquema_congelado_virgenes.md` (08/09/2026), y se lee junto
con ella. Resuelve el punto (c) de la fila B6.0 del plan
(`docs/plan_tesis.md:661`: «si la ventana de corrección única del §7 del laudo
congelado puede abrirse después de la tanda 0 o solo después de la tanda 1 — a
resolver como enmienda con fecha al laudo»). Pre-registro que la acompaña:
`docs/preregistro_tanda0.md` (borrador, misma fecha).

## 1. El §7, transcrito tal como está

`data/experiment/esq/laudo_esquema_congelado.md`, líneas 167-187:

> ## §7. Ventana de tanda 1 — política post-congelado con vigilancia PRE-DECLARADA
>
> Rige la opción (ii) del laudo ESQ-3a §8: la tanda 1 de B6 (20 TOs
> vírgenes) es el test de generalización; si revela una clase nueva de falla
> DE ESQUEMA (no de pipeline), se admite UN ciclo de corrección con laudo
> propio, re-extracción de la tanda 1 incluida, SIEMPRE ANTES de sellar el
> pre-registro de B6.3 — sellado ese pre-registro, la ventana muere y toda
> corrección posterior es release posterior (principio 9). **Ítems de
> vigilancia pre-declarados** (se miden en el reporte de tanda 1, con
> muestreo a definir en su mandato):
>
> 1. **Migraciones tipo-Condicion contra la guarda de modalidad** (enunciados
>    con deber explícito emitidos como Condicion).
> 2. **Conteo de vaciamientos** (unidades con extracción vacía cuyo texto
>    porta contenido normativo), contra las tasas de §3.
> 3. **Duplicación de contenido entre cajas** (mismo pasaje en ≥2 nodos).
> 4. **Rótulos de TO**: la unificación de nodos TO en el ensamblado se hace
>    por identidad documental (archivo/id), NUNCA por rótulo — regla que B5
>    hereda de este laudo.
> 5. Emisiones residuales de vocabulario retirado (debe ser 0 por
>    construcción; cualquier aparición es falla de integración).

Su fuente, `data/experiment/esq/laudo_ESQ-3a_retoques.md` §8 (línea 355 en
adelante), fija la misma política: «**Ventana única de corrección en la tanda
1 de B6** […] **Sellado ese pre-registro, la ventana muere** y rige el
congelado definitivo». La fe de erratas del 08/09/2026 (§5.i) propone la
redacción corregida de «20 TOs vírgenes» → «20 TOs digeribles […] test de
generalización **del esquema** […] **No es test de generalización del
catálogo de sujetos**»; esta enmienda no la altera.

## 2. Texto nuevo — decisión de la autora del 25/09/2026

**Enmienda al §7, con fecha 2026-09-25.** Se agrega, sin modificar el texto
original:

> La ventana de corrección única del §7 puede abrirse **después de la tanda 0**
> (B6.0: test de caja negra del esquema congelado sobre cinco documentos
> nuevos, `docs/preregistro_tanda0.md`) si aparece una falla de esquema que el
> principio de gobierno del §1 obligue a retirar. **Sigue siendo una sola
> ventana**: si se usa en la tanda 0, la tanda 1 ya no la tiene. Si se usa,
> los cinco documentos de la tanda 0 pasan a haber informado el esquema y el
> eval set fresco de B6.3 (a) los excluye igual que a los 15 (los cinco de
> desarrollo y los diez de ESQ-2). Esto se escribe como enmienda con fecha,
> sin modificar el texto original del laudo.

Precisiones que se derivan del texto anterior y de lo ya firmado, para que la
lectura no dependa de memoria:

1. **Qué la abre.** Solo una falla **de esquema** (tipos, predicados, matriz
   dominio/rango, enum de `Obligacion.tipo`, reglas de producción) que
   produzca **falsedad en campo estructurado en material fresco**, primera
   cláusula del §1. Una omisión visible o un error con tasa medida y balance
   favorable se acepta con residuo declarado (segunda cláusula) y no abre la
   ventana. Una falla de pipeline, de catálogo de sujetos, de índice de texto
   o de ensamblado no es de esquema y va a su destino de siempre (release r2
   por el principio 9, backlog, C1.7).
2. **Cómo se usa.** Igual que en el §7 original: un ciclo de corrección con
   laudo propio, re-extracción incluida (de la tanda 0 si se abre en la tanda
   0; de la tanda 1 si se abre en la tanda 1), siempre antes de sellar el
   pre-registro de B6.3. Sellado ese pre-registro, la ventana muere y toda
   corrección posterior es release posterior.
3. **Una sola ventana, en cualquiera de los dos momentos.** Abrirla tras la
   tanda 0 consume la de la tanda 1; no abrirla tras la tanda 0 la conserva
   intacta para la tanda 1. No hay dos ciclos.
4. **Consecuencia sobre el conjunto que informó el esquema.** Si la ventana se
   abre tras la tanda 0, los cinco documentos de la tanda 0 (`ctacte`,
   `lingob`, `polcre`, `pagjub`, `docvig`; `docs/preregistro_tanda0.md` A2)
   dejan de ser vírgenes respecto del esquema y el eval set fresco de B6.3 (a)
   los excluye igual que a los 15 ya excluidos. El registro de esa exclusión
   sigue el mecanismo de `documentos_excluidos_esq.json` (o el artefacto que
   B6.3 cite al construir su conjunto), con la fecha del laudo que abrió la
   ventana. Si la ventana no se abre, los cinco siguen fuera del conjunto que
   informó el esquema; respecto del catálogo de sujetos v3 nunca lo fueron
   (fe de erratas §3).
5. **Los ítems de vigilancia (1)-(5) del §7 y los (6)-(9) agregados por los
   laudos de B5.4** se miden también en la tanda 0, contra sus líneas de base
   y sin umbral (`docs/preregistro_tanda0.md` A4.3); el único criterio de
   retiro sigue siendo el principio de gobierno del §1.

## 3. Qué no cambia

- El principio de gobierno del §1, la lista de retoques del §2, los residuos
  del §3 y el esquema congelado del §4 (`1be8304e3d77` / `e69feaaa…`).
- La política del §7 para la tanda 1 cuando la ventana no se usó en la tanda 0.
- La muerte de la ventana con el sello del pre-registro de B6.3.
- El texto original del laudo, que queda intacto: sha256 al redactar esta
  enmienda `64c5da88bbc4d5698025d722b69253d3a97ce2a510e2f07b9de457184f7a23bf`
  (`shasum -a 256 data/experiment/esq/laudo_esquema_congelado.md`; mismo
  valor que registra la fe de erratas del 08/09/2026, línea 13).
  
Firmado por la autora el 25/09/2026, sellado en el commit de esta fecha.
