# Una norma real, y lo que el grafo hizo con ella

Extracto del grafo vigente **KG-Reextraído-r1** para revisión externa. Generado por `scripts/extracto_grafo_ejemplo.py` desde los artefactos sellados; **nada acá está escrito a mano**.

- Unidad: `ext::7.6::intro` — punto **7.6** de «[bloque intro] Incumplidos en gestión de cobro.»
- Documento: `TO_exterior_cambios_actual.pdf` · página(s) [88]
- Grafo: `data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json` (6529 nodos / 17772 aristas)
- Esta unidad produjo **8 nodos** y **6 aristas internas**; además la alcanzan o salen de ella **21 aristas** hacia otras unidades.

## 1. El texto de la norma

Es lo que el extractor recibió, tal como está en el Texto Ordenado.

```text
Un permiso de embarque será registrado por la entidad de seguimiento en la condición de
“Incumplido en gestión de cobro” cuando se haya verificado que el incumplimiento se debe a
la falta de pago del importador, por haberse demostrado las situaciones previstas conforme a
los puntos 7.6.1. a 7.6.3.
En todos los casos la entidad deberá obtener la declaración jurada sobre el carácter genuino
de lo declarado, firmada por el exportador o quien ejerza su representación legal o un
apoderado con facultades suficientes para asumir este compromiso en nombre del exportador.
A excepción de los casos en que la falta de pago del importador se origine en un control de
cambios en el país del importador, la figura de “Incumplido en gestión de cobro” no podrá ser
aplicada por la entidad de seguimiento cuando se trate de operaciones con contrapartes
vinculadas.
Si una vez superados los inconvenientes existentes el importador efectuara el pago, el
exportador argentino o en su caso la compañía de seguros de crédito a la exportación deberá
ingresar las divisas dentro de los 20 (veinte) días hábiles de la fecha de puesta a disposición
de los fondos.
```

## 2. Los nodos que produjo

Cada nodo lleva su `type` del vocabulario cerrado y su `provenance`: documento, punto y página. Esa procedencia por elemento es la que permite auditar cualquier afirmación contra el PDF oficial.

| tipo | label | punto | página(s) |
|---|---|---|---|
| `Excepcion` | Excepción control de cambios en país importador | `7.6` | [88] |
| `Obligacion` | Ingreso divisas 20 días hábiles después puesta a disposición | `7.6` | [88] |
| `Obligacion` | Obtención declaración jurada carácter genuino | `7.6` | [88] |
| `Operacion` | Ingreso de divisas posterior a pago importador | `7.6` | [88] |
| `Operacion` | Registro de permiso de embarque en condición incumplida | `7.6` | [88] |
| `Restriccion` | Prohibición aplicación condición incumplida contrapartes vinculadas | `7.6` | [88] |
| `Restriccion` | Verificación incumplimiento por falta de pago importador | `7.6` | [88] |
| `Sujeto` | exportador argentino o compañía de seguros de crédito a la exportación | `7.6` | [88] |

## 3. Las aristas entre ellos

Las relaciones son del vocabulario cerrado, y cada una tiene una firma dominio/rango declarada en el esquema.

| origen (tipo) | relación | destino (tipo) |
|---|---|---|
| Excepción control de cambios en país importador (`Excepcion`) | **`exceptua`** | Prohibición aplicación condición incumplida contrapartes vinculadas (`Restriccion`) |
| Ingreso divisas 20 días hábiles después puesta a disposición (`Obligacion`) | **`aplica_a`** | exportador argentino o compañía de seguros de crédito a la exportación (`Sujeto`) |
| Ingreso divisas 20 días hábiles después puesta a disposición (`Obligacion`) | **`condiciona`** | Ingreso de divisas posterior a pago importador (`Operacion`) |
| Registro de permiso de embarque en condición incumplida (`Operacion`) | **`requiere`** | Obtención declaración jurada carácter genuino (`Obligacion`) |
| Prohibición aplicación condición incumplida contrapartes vinculadas (`Restriccion`) | **`prohibe`** | Registro de permiso de embarque en condición incumplida (`Operacion`) |
| Verificación incumplimiento por falta de pago importador (`Restriccion`) | **`limita`** | Registro de permiso de embarque en condición incumplida (`Operacion`) |

## 4. Aristas que cruzan a otras unidades

El grafo conecta más allá del punto: acá se ve la diferencia con un índice de fragmentos, donde cada fragmento queda aislado.

| origen (tipo) | relación | destino (tipo) | unidad del destino |
|---|---|---|---|
| Obtención declaración jurada carácter genuino (`Obligacion`) | **`aplica_a`** | Entidades autorizadas a operar en cambios (Exterior) (`Sujeto`) | `ext::1.2` |
| Obtención declaración jurada carácter genuino (`Obligacion`) | **`establecida_en`** | Texto Ordenado de Exterior y Cambios (`TextoOrdenado`) | `ext::1.1` |
| Remisión de certificación al BCRA (`Obligacion`) | **`referencia`** | Excepción control de cambios en país importador (`Excepcion`) | `ext::8.4.7` |
| Remisión de certificación al BCRA (`Obligacion`) | **`referencia`** | Obtención declaración jurada carácter genuino (`Obligacion`) | `ext::8.4.7` |
| Remisión de certificación al BCRA (`Obligacion`) | **`referencia`** | Ingreso divisas 20 días hábiles después puesta a disposición (`Obligacion`) | `ext::8.4.7` |
| Remisión de certificación al BCRA (`Obligacion`) | **`referencia`** | Ingreso de divisas posterior a pago importador (`Operacion`) | `ext::8.4.7` |
| Remisión de certificación al BCRA (`Obligacion`) | **`referencia`** | Registro de permiso de embarque en condición incumplida (`Operacion`) | `ext::8.4.7` |
| Remisión de certificación al BCRA (`Obligacion`) | **`referencia`** | Prohibición aplicación condición incumplida contrapartes vinculadas (`Restriccion`) | `ext::8.4.7` |
| Remisión de certificación al BCRA (`Obligacion`) | **`referencia`** | Verificación incumplimiento por falta de pago importador (`Restriccion`) | `ext::8.4.7` |
| Ingreso divisas 20 días hábiles después puesta a disposición (`Obligacion`) | **`establecida_en`** | Texto Ordenado de Exterior y Cambios (`TextoOrdenado`) | `ext::1.1` |
| Prohibición aplicación condición incumplida contrapartes vinculadas (`Restriccion`) | **`aplica_a`** | Entidades autorizadas a operar en cambios (Exterior) (`Sujeto`) | `ext::1.2` |
| Prohibición aplicación condición incumplida contrapartes vinculadas (`Restriccion`) | **`establecida_en`** | Texto Ordenado de Exterior y Cambios (`TextoOrdenado`) | `ext::1.1` |
| Verificación incumplimiento por falta de pago importador (`Restriccion`) | **`establecida_en`** | Texto Ordenado de Exterior y Cambios (`TextoOrdenado`) | `ext::1.1` |
| Verificación incumplimiento por falta de pago importador (`Restriccion`) | **`referencia`** | Falta de pago por situaciones en país importador (`Excepcion`) | `ext::7.6.1::intro` |
| Verificación incumplimiento por falta de pago importador (`Restriccion`) | **`referencia`** | Excepción: sin acciones legales iniciadas (`Excepcion`) | `ext::7.6.3::intro` |
| Verificación incumplimiento por falta de pago importador (`Restriccion`) | **`referencia`** | Acreditación con copia de escrito de demanda (`Obligacion`) | `ext::7.6.3::intro` |
| Verificación incumplimiento por falta de pago importador (`Restriccion`) | **`referencia`** | Aporte de documentación por exportador (`Obligacion`) | `ext::7.6.2::intro` |
| Verificación incumplimiento por falta de pago importador (`Restriccion`) | **`referencia`** | Legalización documentación — autoridad consular (`Obligacion`) | `ext::7.6.2::cierre` |
| Verificación incumplimiento por falta de pago importador (`Restriccion`) | **`referencia`** | Iniciación de acciones judiciales (`Operacion`) | `ext::7.6.3::intro` |
| Verificación incumplimiento por falta de pago importador (`Restriccion`) | **`referencia`** | Insolvencia posterior del importador extranjero (`Restriccion`) | `ext::7.6.2::intro` |
| exportador argentino o compañía de seguros de crédito a la exportación (`Sujeto`) | **`padre_sugerido`** | Sujetos regulados (`Sujeto`) | `—` |

---

Para regenerarlo: `python3 scripts/extracto_grafo_ejemplo.py --unidad ext::7.6::intro`
