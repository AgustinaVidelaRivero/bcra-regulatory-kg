# Adenda al criterio — revisión de los 11 CONCORDANTE y de la muestra de silencios

**Escrita y sellada ANTES de abrir un solo caso.** Extiende
`criterio_destinatario.md` (sha
`f5066c12a906b2e3720e2b62d1cb9db2cb45bdcfc91bb91d46c77d3ab843204a`), que se
aplica sin cambios en sus definiciones (A), (B) y sus seis subclases.

## 1. Qué se revisa y por qué

La adjudicación de PR-4 miró únicamente unidades donde el extractor **calló**,
y **ninguna de esas ingresa al grafo**. Lo que ingresa son las **13 aristas
`aplica_a`**, y **once** salen de unidades CONCORDANTE que nadie testeó contra
el criterio. Es **el único lugar de este material donde puede haber falsedad**:
si un CONCORDANTE es (B), la arista está puesta sobre algo que no obliga a
nadie.

## 2. LA REGLA DE DESEMPATE SE INVIERTE — su espíritu, no su letra

El criterio original dice «ante duda genuina se anota **(A)**». Allí (A) era la
lectura **desfavorable al instrumento**: contar una falla del extractor.

**En los CONCORDANTE esa misma etiqueta cambia de signo**: (A) sería la lectura
**favorable** — absolver la arista. Aplicar la letra invertiría la guarda. Por
lo tanto, para esta revisión:

> **ANTE DUDA GENUINA SOBRE UN CONCORDANTE, SE ANOTA (B) Y LA ARISTA SE
> RETIRA.**

Dos razones, las dos del principio §1 del laudo del esquema congelado:

1. Es la lectura **desfavorable al instrumento**, igual que la original.
2. Retirar de más produce **omisión**, que §1 acepta con residuo declarado;
   dejar de más produce **falsedad en campo estructurado**, que §1 manda
   **retirar**. Los dos errores no son simétricos.

## 3. Qué se clasifica, y qué se mira

Para cada uno de los **11 CONCORDANTE**: el pasaje de la unidad y **la arista
`aplica_a` efectivamente emitida** (su `source` y su `target`). La clase es:

- **(A)** el pasaje pone un sujeto en posición de destinatario **y la arista
  emitida apunta a ese sujeto** → la arista **queda**.
- **(B)** el pasaje no pone destinatario, **o** la arista apunta a un sujeto
  que no es el destinatario del pasaje → la arista **se retira**.

**Precisión que agrega esta adenda**: en los 22 de Prioridad 2 bastaba
preguntar si había destinatario, porque no había arista que juzgar. Acá hay
dos condiciones y **las dos deben cumplirse**: que exista destinatario **y**
que la arista apunte a él. Un pasaje con destinatario correcto y una arista a
otro sujeto es **(B)**.

## 4. Muestra de los SILENCIO CONCORDANTE

Se muestrean **15 de las 42** para medir la **tasa de falso negativo de la
marca** en el conjunto silencioso: unidades sin mención léxica y sin emisión
donde, leído el pasaje, **sí hay un destinatario**.

- **Selección**: las 15 primeras en orden de `chunk_id` ascendente — regla
  mecánica, fijada antes de mirar, sin criterio de contenido.
- **Clasificación**: (A) hay destinatario que la marca no vio → **falso
  negativo**; (B) no hay destinatario → la marca acertó al callar.
- **Misma regla de desempate invertida**: ante duda, **(B)** — que aquí es la
  lectura conservadora sobre la corrección estimada, porque **reduce** la tasa
  de falso negativo y por lo tanto **no infla** la corrección al 76,5 %.
- **No se extrapola** la tasa del conjunto emisor (2 de 13): ese conjunto está
  seleccionado y su tasa no se transfiere. Se mide donde se aplica.

## 5. Qué NO hace esta revisión

**No ingresa ni retira nada del grafo.** Produce la lista de aristas que se
retiran y las cifras recomputadas. El ingreso es acto del ensamblado de la
tanda, no de esta unidad.
