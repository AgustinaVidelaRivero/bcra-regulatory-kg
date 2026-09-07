# Declaración previa al censo de los 42 SILENCIO CONCORDANTE

**Escrita y sellada ANTES de leer las 27 restantes.** Fija qué se concluye
según el resultado, para que la conclusión no se elija después de verlo.

## 1. Por qué se pasa de muestra a censo

La muestra de 15 era honesta como pre-registro —regla mecánica fijada antes de
mirar— y **produjo una muestra no representativa**. `chunk_id` ascendente es
orden alfabético por documento, de modo que las 15 salieron de `ri_chr` (3),
`ri_con` (9), `ri_fcem` (1) e `ri_itme` (2), y **excluyeron por construcción a
cinco de los nueve** documentos: `ri_pfmipyme`, `ri_pscpp`, `ri_pspii`,
`ri_rem` y `ri_tii`.

**Es el mismo sesgo de composición** que se corrigió en el brazo planilla al
pasar del pre-registro v1 al v2: una regla mecánica no evita el sesgo si el
orden que usa está correlacionado con el documento.

Y muerde donde importa: **`ri_rem` tiene 0/11 de tasa literal**, así que casi
todas sus once unidades caen en el conjunto silencioso — hasta 11 de los 42,
más de un cuarto, **en el documento donde un destinatario escondido es más
probable, y ninguna muestreada**.

**Se leen las 42. Censo, no muestra.** Con eso la cota inferior deja de ser
cota y no queda discusión de representatividad.

## 2. Método

Criterio sellado `criterio_destinatario.md`
(`f5066c12a906b2e3720e2b62d1cb9db2cb45bdcfc91bb91d46c77d3ab843204a`) con la
**regla de desempate invertida** de la adenda
(`b610151c47d27fc7c579b584ffd79588f62ff725c4c860b1aa202c555df9960a`): ante duda
genuina se anota **(B)** — la marca acertó al callar —, que es la lectura que
**no infla** la corrección.

- **(A)** = hay destinatario que la marca no vio → **falso negativo de la marca**
  → **es una omisión del extractor**: unidad con destinatario y sin arista.
- **(B)** = no hay destinatario → la marca acertó al callar.

Se reporta la tasa **por documento** además de la agregada. Las 15 ya leídas se
conservan con su clasificación y se completan con las 27 restantes.

## 3. QUÉ SE CONCLUYE SEGÚN EL RESULTADO — decidido antes de leer

### Caso 1 — **cero (A) en las 42**

- El denominador **queda en 16**; la recuperación es **12/16 = 75,0 % exacto**.
- **Deja de ser cota superior por la razón del muestreo.** Sigue siéndolo por
  la otra, que no desaparece: **el numerador es conservador** porque la
  clasificación de los CONCORDANTE retira ante duda.
- **(ii) falla de la MARCA queda como causa dominante sin discusión.**

### Caso 2 — **uno o más (A)**

- Cada (A) es **una unidad con destinatario y sin arista**, es decir **una
  omisión del extractor**: **sube el denominador y baja la recuperación**.
- Con *j* falsos negativos: denominador **16 + j**, recuperación **12/(16+j)**.
- **Empuja el balance de vuelta hacia (i) falla del MODELO.** Se reporta el
  **reparto por documento** y **no se redondea a una sola causa**.
- **La conclusión del capítulo se reescribe con ese número, no con el de hoy.**

## 4. Lo que NO cambia con ninguno de los dos resultados

1. **Las 3 aristas se retiran igual** (`ri_tii::p5.b9` ×2, `ri_pscpp::p1.b0` ×1).
2. **La aplicación de §6 está firme**: la prosa entra con residuo declarado, la
   planilla queda afuera y declarada.
3. **La conclusión de los dos anclajes mal especificados queda tal cual está
   escrita**: el piso contaba menciones léxicas como destinatarios y el techo se
   midió sobre una población que nombra a su destinatario en el encabezado; el
   intervalo pre-registrado no era aplicable a bloques de página, y eso se
   descubrió **porque** el ancla estaba sellada.

## 5. Lo que esta unidad no hace

**No retira ni ingresa nada. Lista.** El ingreso es acto del ensamblado de la
tanda.
