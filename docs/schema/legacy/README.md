# Schemas legacy

Esta carpeta contiene versiones del esquema del KG anteriores al scope vigente. Se conservan como referencia histórica y porque varias decisiones siguen siendo aplicables.

## v0.1 (29 abril 2026)

Schema preliminar redactado bajo el scope previo del proyecto, centrado en justificación normativa de decisiones de credit scoring (clasificación de deudores, gestión crediticia, capitales mínimos). Originalmente vivía en `_archive_riesgo_crediticio/docs/schema/`.

- [v0.1.md](v0.1.md) — clases, relaciones, decisiones abiertas
- [v0.1-diagram.md](v0.1-diagram.md) — diagramas Mermaid (estructura del schema, ejemplo poblado, secuencia end-to-end)

### Por qué no es el schema vigente

1. **Scope desalineado con la PPF entregada.** v0.1 modela cartera comercial / consumo / vivienda y categorías de clasificación de deudores. La PPF amplía el scope a regulación BCRA general (operatoria cambiaria, capitales mínimos, garantías, tasas, protección al usuario, sistemas de pago, etc.).
2. **Viola la regla del mentor sobre nodos.** v0.1 modela `bcra:Punto` (con propiedad `numeracion = "6.5.3.2"`) como nodo de primer nivel del grafo. Lucho indicó explícitamente que los nodos deben ser entidades regulatorias reales, no jerarquía documental. La numeración debe vivir en propiedades de provenance de las tripletas, no en nodos propios.
3. **Le faltan tres de las siete entidades core de la PPF**: `Operación`, `Restricción`, `Excepción` no están modeladas. Las que sí están (`SujetoObligado`, `TipoFinanciacion`, `CategoriaClasificacion`, `Condicion`) están sesgadas al uso de scoring.

### Qué sobrevive a v0.2

Material a recuperar e iterar en el RFC v0.2 (en redacción):

- Distinción **clases estructurales** (documento) vs **clases semánticas** (contenido) vs **aplicabilidad**.
- Modelado de **versionado temporal** (la nota dice "v1 con propiedad simple, v2 con nodos versionados" — v0.2 debe modelar versionado explícito desde el inicio).
- Las **cuatro decisiones abiertas** (granularidad de Condicion, modelado de versionado, resolución de referencias externas, FIBO vs schema custom) siguen sin resolverse — entran al RFC v0.2 con sus opciones.
- El patrón de **ejemplo poblado con datos reales** del corpus para validar el schema antes de extraer.
