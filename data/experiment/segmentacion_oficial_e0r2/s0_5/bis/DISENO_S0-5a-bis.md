# U-SEG-OFICIAL — S0-5a-bis: diseño aplicado (09/10/2026)

Mandato `docs/mandatos/USEG_OFICIAL_S0-5a_reglas_de_corte_E0.md`, leído en `84695b89` (sha256 del texto en ese commit
`cbe0cb35…`), con sus notas al pie: la de la revisión de S0-5a (en `32c71ca`) y la segunda del 09/10/2026 (en
`84695b89`). Lista de R5-a v2 de la mesa (`lista_R5a_por_lista_v2_decision4_mesa.json`, sha256 `5bec1dce…`, el del
`manifest.txt` de su paquete). Y el agregado del 09/10/2026 (una regla por lista más, en ri_oc, en la misma vuelta),
con la lista de los 88 rechazos por columna profunda de la mesa (`lista_88_rechazos_columna_profunda_mesa.json`, sha256
`cf6796e7…`, el de su `manifest.txt`). USD 0, sin API. El código de E0 se cambió solo en una copia; el parche (`parche/`) es
sobre el código de S0-4b, el del repo, y reemplaza al de S0-5a. Comandos y cifras: `REPORTE_S0-5a-bis.md`.

## 1. De dónde parte

- Del código final de S0-5a (`4d0abc1a…`, `ed276d43…`, `9f2fbf28…`; parche de S0-5a `c6558ea0…`), sobre una copia del
  repo sin enlaces. Lo que cambia está detrás de los mismos interruptores de S0-5a más dos nuevos, `r5f` y `r5g`.
- **Dos vueltas.** La primera (código `c3310c97…` / `3d457122…`) tenía R5-a por lista, la guarda de tablas y R5-f, y
  pasó sus controles (salidas en `corridas_vuelta1/` del scratchpad, logs en el paquete). El agregado de ri_oc llegó
  mientras la cerraba: sumé R5-g y volví a correr todo con el código final; las cifras de `REPORTE_S0-5a-bis.md` son de
  la segunda vuelta.
- R5-a′, R5-b, R5-c, R5-d y R5-e no cambian.

## 2. Lo que cambia

### R5-a por lista (decisiones 1 y 4 de la autora)

- `aplicar_cierre_al_margen(listas=…)`: con `listas`, R5-a actúa solo sobre las listas dadas, que encuentra en el árbol
  por la clave de su último ítem (`<numero>`, o `<prefijo>::<numero>`), **sin el detector como alcance**; la lista
  entra aunque el detector no la marque. Sin `listas`, el comportamiento es el de S0-5a.
- `LISTAS_R5A_S0_5` (correr_e0), generada desde la lista v2: **43 listas** en 29 TOs.
  - **40 con el criterio de S0-5a** (los párrafos del último ítem que están al margen, con la misma tolerancia,
    `TOL_X`): los 9 casos y 31 de los 32 cierres.
  - **3 con un rango de renglones** (página, top y comienzo del texto del primero y del último):
    - `ri_rml::1.4.2`, p. 11, de «Para el punto 1.4.1.» (top 409,0) a «…671000/M-TP.» (top 698,8). Es uno de los 32
      cierres, pero el criterio de S0-5a empieza un párrafo tarde: «Para el punto 1.4.1.» sigue a una fórmula sin
      puntuación final, así que para el detector no abre párrafo. El rango es el que fija la lista v2 con la página;
    - `ri_spi::C.1.3`, los 11 renglones de la p. 9 (top 284,8 a 471,0);
    - `ri2_ae::14.3`, los 7 renglones de la p. 28 (top 664,2) a la p. 29 (top 126,0).
  - Un renglón del rango se reconoce por su página, su top a 0,5 pt o menos (`TOL_TOP_POR_LISTA`) y el comienzo de su
    texto. Si el primero o el último no está entre los renglones propios del ítem, R5-a no mueve nada en esa lista y lo
    registra (`r5a_por_lista_sin_rango`).
- Las 14 de `no_se_tocan` no están en la lista: quedan como en S0-4b.

### R5-a no mueve renglones de tablas (decisión 2)

- `aplicar_cierre_al_margen(excluir=…)`: un predicado de renglón. R5-a no mueve un párrafo ni un rango que tenga algún
  renglón que lo cumpla, y lo registra (`r5a_no_mueve_tabla`).
- `_excluir_tablas_r5a` (correr_e0) lo arma con las tablas que E0 detecta antes del parseo (`tablas_r9`): las que no
  son recuadro de prosa, que son las que se serializan, con la misma asignación geométrica que
  `asignar_lineas_a_tablas` (la página del segmento y el top dentro de su bbox, menos `TOL_TOP_TABLA`).
- **Diferencia con la letra del mandato**: el mandato dice «los renglones que serializa `e0_tablas`»; la guarda excluye
  también las tablas de dos filas de R-TC2, que se serializan igual. En las 43 listas no bloquea nada.

### R5-f, rótulos de punto por lista (decisión 4, saltos de la tanda 1)

- El mandato las llama «reglas por lista nuevas»; el nombre R5-f es mío, para el interruptor y el censo.
- `parsear_cuerpo(rotulos_por_lista=…)`: cada (página, top, número, padre) abre el punto `número`, hijo del padre dado
  o, si es None, del que indica el número (la sección, con un número de dos componentes), si ese padre está abierto en
  la pila. No pasa por las validaciones de siempre (número pegado al texto, texto en minúscula, hermano anterior, padre
  no abierto). El renglón no cambia: el título del punto es lo que sigue al número. Si el padre no está abierto, el
  renglón sigue como estaba y queda registrado (`rotulo_por_lista_r5f_sin_padre`).
- `ROTULOS_POR_LISTA_S0_5` (correr_e0):
  - ri_ccna, D1A1: 2.1.1 a 2.1.7 (p. 3), 2.1.8 (p. 4), 5.1 (p. 6) y 8.1 (p. 8); D1A2: 5.1 (p. 10);
  - snp_cheq: 3.3.6.2 (p. 38, top 218,2), colgado de 3.3.
- El renglón se reconoce como en los rangos de R5-a: página, top a 0,5 pt o menos, y que empiece con el número y un
  punto.

### R5-g, raíz por lista (agregado del 09/10/2026, ri_oc)

- `parsear_cuerpo(raices_por_lista=…)`, en el modo sin raíz (el de ri_oc): el renglón de cada (página, top, número)
  abre la raíz explícita aunque esté más adentro que la columna de las raíces (guarda G3); las otras guardas (banner,
  forma de título, sucesión, regla 8) siguen, y la columna de las raíces no cambia. Registra `raiz_por_lista_r5g`.
- `RAICES_POR_LISTA_S0_5` (correr_e0): ri_oc, «3. Aclaraciones» (p. 6, top 117,4, x0 85,0; la columna de las raíces es
  76,6). La p. 6 es de otra versión de la norma que la p. 5, con otro margen.
- Efecto: el renglón sale del texto propio de `ri_oc::S2`, y el encabezado S3, que era «3.» (la raíz implícita que
  abría «3.1.»), pasa a «3. Aclaraciones», que heredan las 51 unidades de 3.1 a 3.51. S3 no es una clave propia (no
  tiene texto propio): el encabezado está solo en la herencia.
- Los otros 87 rechazos con el mismo motivo, en 7 documentos fuera de la tanda 1, siguen igual.

## 3. Lo que no cambió del mandato, y lo que no sale como dice

1. **«41 enteras, como en S0-5a»**: 40 lo son, con el texto de S0-5a; la número 41, `ri_rml::1.4.2`, va por rango,
   porque el mandato fija su cierre desde un renglón que el criterio de S0-5a no toma como inicio de párrafo.
2. **El control de continuidad da un salto nuevo**: con 3.3.6.2 abierto, 3.3.6.1 aparece como hueco (i). Es el salto
   del PDF que la nota declara («el PDF salta 3.3.6 y 3.3.6.1»), no un error de corte, pero contradice la letra de
   «ningún salto nuevo». Lo declaro.
3. **«Una tabla de gescre o de gerc, que sigue serializada»**: las tablas de gescre no se serializan (son recuadros de
   prosa, en S0-4b también). El caso negativo del selftest usa `gerc::tabla005` y, además, las tres tablas que el R5-a
   de S0-5a dejaba de serializar (`manori::tabla014` y `tabla015`, `ri_spi::tabla001`).
4. `ri2_ae::14.3` sigue partido en tres (`::parte1` a `::parte3`): con 7 renglones menos, sigue pasando el umbral de
   partición. Las claves no cambian; el texto de las partes, sí.
