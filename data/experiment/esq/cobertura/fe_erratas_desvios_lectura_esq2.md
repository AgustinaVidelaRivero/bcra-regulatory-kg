# Fe de erratas del documento de desvíos de lectura de ESQ-2 — §2, recuento de campos truncados

**FIRMADO por la autora — Agustina Videla Rivero, 08/09/2026.** Corrección
por declaración del documento firmado `data/experiment/esq/cobertura/desvios_lectura_esq2.md`
(firmado 02/09/2026, sellado en `685fc8a`). El documento firmado **no se
edita**: esta fe de erratas lo corrige al lado, con la evidencia, lo que el
firmado dice, lo que es cierto, y qué cambia y qué no.

Alcance: **solo el §2 (desvío (b), truncamiento)**. El §1 (desvío (a),
contaminación), la adenda del desvío (c) y las reglas fijadas en ambos
quedan intactos y vigentes.

## 1. Evidencia

El recuento del §2 se hizo por longitud **en caracteres**. La causa que el
propio §2 declara —el límite de línea del modo canónico de la terminal— opera
en **bytes**, no en caracteres, y las dos unidades no coinciden en un texto
castellano con acentos, comillas tipográficas y rayas.

Recomputado en bytes sobre el worksheet sellado
(`cobertura/fichas/worksheet_fichas_esq2.json`, sha256
`de933cb0b180b50787afadaa0415b709922cc1e2013649b621066a0f056bb7b6`,
commit `b2e9e90`), la banda del límite de línea contiene **37 campos**, no
los 35 que enumera la tabla firmada. Los dos que la tabla no lista son
**ficha 43 · `observaciones`** y **ficha 50 · `observaciones`**.

Comando de recómputo (desde la raíz del repo; el conjunto que imprime es el
de la banda, su mínimo y máximo en caracteres, y las dos fichas en disputa):

```bash
python3 -c "
import json
d=json.load(open('data/experiment/esq/cobertura/fichas/worksheet_fichas_esq2.json'))
r=[]
for x in d['fichas']:
    c=[('observaciones',x.get('observaciones'))]+[(q+'.'+k,v) for q,qv in x['preguntas'].items() if isinstance(qv,dict) for k,v in qv.items() if k!='pregunta']
    r+=[(x['n'],n,len(v),len(v.encode())) for n,v in c if isinstance(v,str) and v.strip()]
b=sorted(t for t in r if 1020<=t[3]<=1023)
print(len(b)); print(min(t[2] for t in b), max(t[2] for t in b)); print([(t[0],t[1]) for t in b if t[1]=='observaciones' and t[0] in (43,50)])
"
```

Salida: `37` · `992 1011` · `[(43, 'observaciones'), (50, 'observaciones')]`.

Las 35 filas de la tabla firmada se cotejan una a una contra el recómputo:
las 35 están en la banda, ninguna sobra, y la columna `len` de la tabla
coincide exactamente con la longitud **en caracteres** de cada campo. El
defecto es de recuento, no de contenido: lo que la tabla lista es correcto;
lo que le falta son dos filas.

### Dónde corta exactamente el límite

Distribución de longitudes en bytes de los campos de texto de las 75 fichas,
de 1015 bytes para arriba:

| bytes | campos |
|---:|---:|
| 1020 | 1 |
| 1021 | 1 |
| 1022 | 9 |
| 1023 | 26 |
| 1101 | 1 |

El pico de **26 campos en exactamente 1023 bytes** fija el corte: la terminal
conserva 1023 bytes de contenido de línea. Los 9 de 1022 y el de 1021 son el
mismo corte con un carácter multibyte a caballo de la frontera.

## 2. Lo que el firmado dice y lo que es cierto

| | firmado (§2) | cierto |
|---|---|---|
| conteo | «35 campos» (título del §2 y frase de apertura) | **36 campos** con evidencia de truncamiento |
| banda | «longitudes agrupadas en 1001–1011 caracteres» | **1020–1023 bytes**; en caracteres su propia tabla va de **992** a **1011** |
| causa | límite de línea del modo canónico (~1024 bytes) | sin cambio — se confirma, y se precisa en **1023 bytes de contenido** |

## 3. El conteo corregido: 35 → 36

**Entra ficha 43 · `observaciones`** (1003 caracteres / 1023 bytes, justo en
el corte). Su cola conservada termina a mitad de oración y con una comilla
abierta sin cerrar:

> «… Otras pérdidas no contabilizadas por el límite de una familia por ficha:
> la remisión "»

La ficha 43 **fue leída**: la tabla firmada ya lista su otro campo largo
(`43 · q2.por_que · 1004`), y sus marcas q1/q2 están completas en el
worksheet. No es un campo sin leer: es un campo leído cuya cola se perdió.

## 4. Ficha 50 · `observaciones`: límite del criterio, NO contada

La ficha 50 cae en la banda (1002 caracteres / 1020 bytes) y **no se cuenta
como truncada**, por dos razones independientes:

1. **Criterio textual.** Cierra con oración completa y punto final: «… y
   distinto de la ficha 14, donde Restriccion alojaba un deber positivo y
   limita invertía el sentido de la norma.» No hay corte a mitad de palabra
   ni de oración, que es la evidencia con la que se identificó a los demás.
2. **Aritmética del corte.** Bajo la causa declarada, con el corte fijado en
   1023 bytes, la longitud conservada `L` cumple `L + w > 1023`, donde `w` es
   el ancho en bytes del carácter que no entró. El texto de las 75 fichas no
   contiene ningún carácter de 4 bytes —su repertorio medido es 129.853
   caracteres de 1 byte, 1.979 de 2 y 217 de 3—, de modo que `w ≤ 3` y por lo
   tanto `L ≥ 1021`. **1020 bytes es inalcanzable** por este corte.

Se declara así, con las palabras del criterio: la ficha 50 es el **límite
inferior de la banda** y entra en ella por longitud, no por evidencia. Si
apareciera evidencia de truncamiento, el conteo pasaría a 37; hoy no la hay.

Por el mismo criterio queda **fuera** el único campo por encima de la banda,
**ficha 7 · `observaciones`** (1084 caracteres / 1101 bytes): excede el corte
de 1023 bytes, lo que muestra que no todo campo del worksheet pasó por el
límite de línea, y cierra con oración completa y punto.

## 5. La banda, re-declarada en bytes

El §2 declara la banda en caracteres («1001–1011»), unidad que no es la de la
causa y que además **no describe a su propia tabla**, cuyo mínimo en
caracteres es 992 (ficha 24) y cuyo máximo es 1011 (ficha 39).

Redacción corregida, que reemplaza a la del §2:

> Los campos afectados están cortados en **1020–1023 bytes** —el pico está en
> 1023, que es el contenido de línea que conserva el modo canónico de la
> terminal— lo que en caracteres se lee como un rango de **992 a 1011**,
> según cuántos caracteres multibyte tenga cada campo.

## 6. Qué NO cambia

- **Las marcas de las 75 fichas siguen intactas.** Ninguna se toca acá, como
  ninguna se tocaba en el documento firmado.
- **Las citas textuales obligatorias siguen completas.** Ningún `cita_textual`
  cae en la banda del corte.
- **El alcance de la pérdida no cambia.** Lo truncado sigue siendo prosa de
  análisis complementario: el campo que entra al conteo (`observaciones` de la
  ficha 43) es de la misma naturaleza que los 35 ya listados, y la ficha 43
  conserva q1, firma de q2 y cita textual. Ninguna marca ni cita obligatoria
  depende de un campo truncado.
- **La regla fijada en el §2 sigue vigente sin retoque**: la pérdida se
  declara y NO se reconstruye de memoria. Un campo más en el conteo es un
  campo más que se da por perdido, no un campo a reponer.
- **Los remedios diferidos** (entradas 10 y 11 de `docs/cola_mejoras_diferidas.md`)
  siguen igual; la entrada 11 (arreglo del instrumento para textos largos)
  queda además reforzada por la precisión del corte en 1023 bytes.
- **Los desvíos (a) y (c) y sus reglas** no se tocan.

## 7. Efecto sobre documentos que citan el número

`docs/tesis/main.tex`, §3.6, dice «truncó 35 campos de texto largo». Con esta
fe de erratas firmada, pasa a **36**. La corrección de la prosa del capítulo
es de la autora; acá solo se registra la dependencia.

## Firma

**FIRMADO por la autora — Agustina Videla Rivero, 08/09/2026.**
