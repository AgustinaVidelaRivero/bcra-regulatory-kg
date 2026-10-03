# U-PROMPT-R2 — FRENO P1

03/10/2026, HEAD `28e06fb`. USD 0: ninguna llamada a la API. Sin commit: el commit es de la autora. El diseño
completo está en `data/experiment/prompt_r2/diseno_prefijo_r2.md`, y lo cito por sección. Según el mandato
(`git show b901f6d:docs/mandatos/UPROMPT_R2_prefijo_nuevo.md`, «FRENO P1»), en este freno la autora aprueba el
texto del prefijo y del mensaje, con las estimaciones de P1.c y P1.d, y decide el tope de P4 (decisión 18) y la
regla de `frecuencia` (decisión 20).

## 1. Lo que se aprueba

| Pieza | Dónde | Huella |
|---|---|---|
| Prefijo de E1, variante A | diseño §2 (lado a lado, R0 a R30); `p1/salida/prefijo_r2_borrador_A.txt` | 51.189 caracteres, sha256 `9f65faba…`, hash canónico `ade47e493b15` |
| Prefijo de E1, variante B | lo mismo, salvo R6; `prefijo_r2_borrador_B.txt` | 51.249 caracteres, `a4bf75f4…`, `d7b838f640c1` |
| Tool schema r2 con las decisiones 15 a 17 | diseño §3; `p1/salida/generados_d15_17/tool_schema_r2.json` | `0c391f2b…`; enums sin cambios, `abd197ac…` |
| Mensaje de E1 | diseño §4.1, §4.2 y §4.5; `p1/mensaje_r2_borrador.py`; ejemplos en `p1/salida/ejemplos_mensaje_r2.md` | — |
| NOTA de E3 de tablas y de encabezados | diseño §4.3 y §4.5 | el prefijo de E3 no cambia: `21a836c7de6d` |
| Estimación de P1.c y P1.d | diseño §7 y §8 | `p1/salida/censo_p1.json` |

Los hashes los calcula `p1/hashes_borrador.py`. Cambian con cada ajuste, hasta que P2 congele el texto.

## 2. Lo que decide la autora

1. **Regla de `frecuencia` (decisión 20; diseño §9).**
   - M2.c: 250 plazos van a `frecuencia` y 213 quedan fuera de la lista. M3.d no llegó.
   - Los fuera de lista son momentos sin cuantía y valores de relleno. Casi ninguno es una periodicidad
     (`p1/salida/frecuencia_r2a.json`).
   - **Recomiendo B**: `frecuencia` queda solo para la periodicidad, y el momento sin cuantía va a la
     descripción y al `tramo`. Cuesta lo mismo que A. La fila :74 del tablero bajará por construcción.
2. **Tope de P4 (decisión 18; diseño §7).** La estimación es USD 1,11 central y 1,63 alta. Incluye los casos de
   F1, los de `BKL-0035` y `BKL-0039` y la pata de E3 (0,06 a 0,14). **Recomiendo mantener USD 2.**
3. **Tope de U-REEXT-T0 (E1 a E3, 2.434 unidades; diseño §7).** La estimación central es USD 49,11, con un
   rango de 48,44 a 49,38. Por el factor 1,4 del precedente da 68,76. **Propongo USD 69.**
4. **Tandas del protocolo a la tarifa nueva (diseño §7):** 66,43 / 114,39 / 40,52 / 19,69; partición completa
   188,14. Las filas no se suman. Si las aprobás, van al protocolo como nota fechada.
5. **Puntos abiertos del §10.1 del diseño**, con mi recomendación:
   - **1.** Que el TextoOrdenado no lleve tramo: confirmar. Lo deriva el código (decisión 16), y un tramo no
     tendría qué fundar.
   - **2.** No-filtración de las decisiones 11 y 21, con los patrones descritos sin citar casos: ratificar.
     Es el precedente de ESQ-3b.
   - **3.** Que «externa» se derive de `codigo` en el código y el prompt admita normas externas como
     Comunicacion: confirmar.
   - **5.** El elemento sin valor del límite relativo: hacerlo en `validador_r2.py`, la única de las tres
     opciones que está entre las escrituras.
   - **8.** Que el catálogo diga «sujeto_propuesto»: dejar la aclaración de R15. Enmendar el JSON cambia el
     bloque que LN-8 protege, así que pide una unidad que lo autorice.
   - **10.** Extender la guarda de `ejecuta` a los 5 TOs de desarrollo: aprobar. Con el namespace nuevo ya no
     rige la razón para dejarlos sin ella.

6. **Cómo se reconoce una exención de la guarda ampliada** (diseño §4.5). La enmienda a LAUDO B (borrador)
   marca el faltante eximido solo con `estructural_no_bloqueante`, igual que LAUDO B tal como está. Con eso,
   el reporte de U-REEXT-T0 no distingue de forma directa qué unidades eximió la ampliación.
   **Propongo** que el faltante eximido por la ampliación lleve además `guarda_ampliada: true`, solo en la
   forma «r2», y que `runner_corpus.py` liste esas unidades con la cita y el tipo. Si lo aprobás, conviene
   sumarlo a la enmienda antes de firmarla.

## 3. Ya decidido en esta unidad (diseño §10.2)

- Punto 4: la traducción de la forma «r2» en `validador_e1.py`.
- Punto 18: el encabezado de lista por tipo, con el límite de las condiciones conjuntas en un título sin
  unidad.
- Punto 19: F1-A.
- Punto 20: la NOTA de E3 y la guarda ampliada con salvaguarda. El reporte de U-REEXT-T0 lista cada exención.
- Casos de P4: los fijos, los de F1, `ctacte::6.4.7::intro` y la pata de E3.
- Tablas: aviso de riesgo y lista de tablas forzadas a residual.

La instrucción de umbrales está ajustada con la columna r2a de M2 (diseño §4.6) y entra en la aprobación del
texto.

## 4. Controles

- **Doble corrida** de `p1/reproducir_p1.py` con espejos distintos: las salidas de `p1/salida/` dan byte a
  byte iguales.
- **No-filtración:**
  - 0 en las instrucciones nuevas y en el texto fijo del mensaje y de las dos NOTAS;
  - 19 ventanas de 5 palabras del bloque de catálogo, declaradas;
  - 5 bigramas o trigramas de control, también del bloque de catálogo.
- **Repo:** sha256 de los archivos rastreados y no ignorados fuera de `data/experiment/prompt_r2/`, antes y
  después; sin cambios de contenido.

## 5. Pendiente de la autora

- Commit de U-PROMPT-R2 P1 (`data/experiment/prompt_r2/`): PENDIENTE.
- Nota al pie del mandato sobre las escrituras de E3, enmienda a LAUDO B y entrada `BKL-0039`: en el árbol de
  trabajo. Commit, y firma de la enmienda: PENDIENTES.
- El «seguí» a P2: P2 congela el prefijo que se apruebe acá.
