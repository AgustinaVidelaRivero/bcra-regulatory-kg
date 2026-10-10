# U-CONF-MATRIZ, C2-bis: el sello, C3 y la lista de C4 (mesa, 10/10/2026)

Repetición de C2 con un lector nuevo, por las decisiones de la autora del 09 y el 10/10/2026 (notas al pie de
`docs/mandatos/UCONF_MATRIZ_lectura_confirmacion.md`). La primera lectura (`c2/`, `c3/`, `FRENO_C3.md`) queda registrada como contaminada
y no decide: se abrió recién después del sello de esta, y solo para las discrepancias.

## El sello

- **La carpeta del lector:** `~/INGENIERIA IA/TESIS/fuera_del_repo/lecturas_ciegas/lectura_aristas_condicion/`.
  - De sus 92 archivos de partida (`manifest_carpeta_lector_C2bis.txt`), 91 siguen iguales. Cambia solo `planilla.jsonl`, que es la
    que el lector completa.
  - Archivo nuevo: `sello_planilla.txt`.
  - El script propio que el lector habría agregado (`volcar_planilla.py`) **no está en la carpeta**: no hay otro archivo nuevo. Queda
    declarado.
- **La planilla:** sha256 `abfde990d566533e7a78b21022b6564c466d6b8d24c92a611b49df135203e5b6`, igual al de `sello_planilla.txt`. Son 60
  filas, selladas el 2026-10-10T00:13:29-03:00. La copia está en `planilla_C2bis_sellada.jsonl`, con su sello al lado.

## C3

`python3 -B c3_C2bis_mesa.py <repo> planilla_C2bis_sellada.jsonl sello_planilla_C2bis.txt ../c2/planilla_c2.jsonl 4532495010434239514
2215609819628898327 c3_C2bis.json`. El par de cada ficha sale del acta sellada de C1, y el criterio es el del §2 del mandato.

| par | correctas | incorrectas | no decidibles | Wilson 95 %, inferior | criterio (≥ 0,75 y ≤ 6 no decidibles) |
|---|---:|---:|---:|---:|---|
| → Operacion | 26 | 4 | 0 | 0,7032 | no confirma |
| → Potestad | 29 | 1 | 0 | 0,8333 | confirma |

Son cifras de C3, antes de la revisión de la autora. La cifra final es la de C4.

## La lista de C4 (`lista_C4_C2bis.md`)

- **Entran:** las incorrectas y las no decidibles de esta lectura; 5 correctas por par, con las semillas selladas en la nota del mandato;
  y toda ficha en la que las dos lecturas no coinciden.
- **Son 15 fichas:**
  - → Operacion: 4 incorrectas y 5 correctas;
  - → Potestad: 1 incorrecta y 5 correctas.
  - Las 3 discrepancias con la primera lectura (F27, F34 y F45: «correcta» allá, «incorrecta» acá) ya están entre las incorrectas.

## Propuesta de clases para las incorrectas de → Operacion

Va porque, si en C4 el par no confirma, rige el §7: la relación no se retira, su cifra se declara y los errores se clasifican. La
propuesta es de la mesa, a partir de las notas; las clases las adjudica la autora.

- **Tramos contenidos entre los extremos, 3 de 4** (F27 y F34, en `ext::2.2.3`; F45, en `ctacte::8.2.1.1`): el tramo de E1 de un
  extremo está contenido en el del otro. En F27 y F34, el del destino está, literal, dentro del del origen. En F45, todas las palabras del
  tramo del origen están en el del destino, pero no en el mismo orden ni como frase literal.
  - En F27 y F34, el destino repite el supuesto del origen, y el consecuente queda solo en su descripción.
  - En F45, el origen es parte de la definición del destino.
  - Se puede detectar con código: inclusión literal de un tramo en el otro, o inclusión de sus palabras. Es candidata al grupo 2, después de medir
    su precisión sobre la población de la arista.
- **Condición de otro elemento del punto, 1 de 4** (F15, `ext::10.4.2.4`): el supuesto gobierna el plazo de la declaración jurada,
  no el acceso al mercado de cambios. No se puede detectar con código.

La incorrecta de → Potestad (F57, `cla::3.3.3`) es la cláusula «cuenten o no con garantías preferidas», que el texto declara
indiferente.
