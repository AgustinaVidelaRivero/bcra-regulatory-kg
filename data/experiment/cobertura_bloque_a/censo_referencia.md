# Censo de los DOS declarados referencia — `optico` y `plandecuentas`

Unidad U-COB-A, fase A.1, entregable 4. **Estos dos documentos NO se extraen.**
Se censan para el registro, con su evidencia citada.

## 1. La adjudicacion que los declara referencia (fuente sellada)

`docs/adenda2_laudo_B5.5_cobertura.md` §1 (FIRMADA 07/09, commit `1ae387e`),
punto 3 verbatim:

> «**Diez de los doce** documentos declarados no segmentables contienen
> contenido prescriptivo. Solo `plandecuentas` y `optico` son referencia
> pura, y son exactamente los dos con densidad deontica **0,000** en las tres
> variantes del instrumento.»

Evidencia que la adenda §1 registra para esa adjudicacion: instrumento
deontico corregido por el futuro impersonal (5,58× → 1,56×) y **lectura a
ciegas de 32 paginas con pre-registro sellado y enmendado antes de leer**, con
resultado 23 prescriptivo / 9 referencia / 0 duda. La adjudicacion es de la
autora y es la fuente; esta unidad no la re-litiga y no busco los paquetes de
U-COB-EXCL.

## 2. Censo de forma (medicion propia, independiente de la de contenido)

`python3 code/censo_forma.py` → bloque `bloque_a_referencia` de
`censo_forma.json`.

| documento | paginas | roles de pagina | paginas de prosa | bloques del modelo de unidad | tablas logicas B5.8.3 |
|---|--:|---|--:|--:|--:|
| `optico` | 43 | 38 historial · 4 indice · 1 cuerpo | **0** | **2** | 0 |
| `plandecuentas` | 77 | 76 ficha_registro · 1 cuerpo | **0** | **0** | 0 |
| **total** | **120** | — | **0** | **2** | **0** |

Los dos unicos bloques que el modelo de unidad produce en 120 paginas son la
caratula de `optico` (p.1), citados integros:

```
[p.1 off.0 · 2 lineas · 42 car.] -Última comunicación incorporada: “A” 8462
[p.1 off.1 · 2 lineas · 29 car.] Texto ordenado a /202 30/07 6
```

Material de las paginas que dominan cada documento, citado:

```
optico p.6 (historial, 38 de sus 43 paginas):
  Comunicaciones que componen el historial de la norma
  Comunicaciones que dieron origen y/o actualizaron esta norma:
  “A” 3058: Texto ordenado de la presentación de informaciones al Banco Central
  en soportes ópticos. (B.O. del 20.1.00).

plandecuentas p.2 (ficha_registro, 76 de sus 77 paginas):
  B.C.R.A. PLAN DE CUENTAS
  100000 Activo
  110000 Efectivo y depósitos en bancos
  111000 En pesos - En el país
```

## 3. Convergencia de dos instrumentos independientes

La adjudicacion de la autora es **por contenido** (densidad deontica y lectura
a ciegas). El censo de esta fase es **por forma** (roles de pagina y modelo de
unidad de prosa). Son instrumentos distintos, y concluyen lo mismo:

- **2 bloques en 120 paginas** en los dos de referencia, contra **332 bloques
  en 41 paginas** en los diez que si se extraen — una diferencia de tres
  ordenes de magnitud por pagina (0,017 contra 8,1 bloques/pagina;
  `python3 -c "print(2/120, 332/41)"`).
- **Cero paginas de clase `prosa`** en los dos, contra 17 de 41 en los diez.
- `optico` es **88 % historial de comunicaciones** (38/43) y su unica pagina de
  cuerpo es la caratula: no tiene articulado que extraer.
- `plandecuentas` es **99 % ficha de registro** (76/77): es un plan de cuentas
  contable, la forma canonica del material del bloque B.

**Registro:** la medicion por forma de esta fase **no contradice** la
adjudicacion por contenido de la adenda §1; la respalda de manera
independiente. Los dos documentos quedan **declarados referencia y fuera de la
extraccion**, con sus 120 paginas contabilizadas en el registro y no en el
recurso.

## 4. Nota sobre el conteo del recurso

`optico` aporta **1** unidad degenerada a las 12 de la particion sellada y
`plandecuentas` aporta **0** (verificado contra `particion_152.json`). Esas dos
unidades **no se tocan**: el bloque A reemplaza solo las **11** de los diez
documentos que si se extraen. El detalle esta en `reporte_A1.md` §1, con su
consecuencia sobre el denominador del conteo exigido.
