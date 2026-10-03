# Réplica independiente de U-DIAG-PROCESO

Esta carpeta guarda la segunda ejecución del mandato `docs/mandatos/UDIAG_proceso.md` (`f8cf89a`), hecha el
03/10/2026 por otra instancia, en paralelo con la entrega principal de `reports/u_diag_proceso/`. Es una
réplica independiente: mismo mandato, mismas fuentes, otra sesión (`a7ef8581`), con scripts, definiciones
y salidas propios. Su entrega había quedado solo en el paquete de revisión de esa sesión, fuera del repo,
porque la carpeta de entrega ya estaba en uso. NO VERIFICADO: que ninguna de las dos instancias haya leído
los archivos de la otra; la réplica declara que encontró la carpeta en uso y retiró de ahí los suyos.

## Qué hay

Los 26 archivos del paquete y su `manifest.txt`, copiados sin modificar el 03/10/2026. Control de la copia:
`shasum -a 256 -c` contra `manifest.txt` da 26 de 26, y el sha256 del propio manifiesto es `663bb797…`. El
reporte es `reporte_u_diag_proceso_FRENO_sesion_a7ef8581.md`; los comandos, en
`comandos_u_diag_proceso_sesion_a7ef8581.md`. El reporte cita sin ruta los archivos de esta carpeta.

## En qué coincide con la entrega principal

- La causa de la pérdida del contenido del encabezado (F1): E0 no le da unidad a la línea de título de un
  punto con hijos, y el prefijo le prohíbe al chunk de punto extraer del contexto heredado.
- La recomendación para F1: una regla de composición en el prefijo nuevo (F1-A en la principal, F1-b acá).
- Las 23 ausencias de categoría P de la tanda 0 no son el mismo fenómeno.
- En la tanda 0, 8 de los 10 encabezados en línea de título no tienen ningún nodo anclado.
- La prevalencia en la muestra azarosa de ESQ-2: 5/38 para F1 y 1/38 para el vínculo, con los mismos
  intervalos salvo redondeo; y 2.709 de las 9.324 unidades de la partición son ítems o encabezados de
  lista.
- La frase «la resuelve E3» está en la ficha 44, no en la 39.

## En qué difiere

- **Vínculo entre unidades.** La principal recomienda un enlazador en código para el destino heredado
  (VU-B) y la navegación de A1.8 para el destino en una unidad hermana. La réplica recomienda solo la
  navegación (V-b): con la regla de composición, el contenido del encabezado queda en el texto del nodo.
- **Grafo de control.** La réplica leyó KG-Tanda0-Diez-r2a (`99fe2bfa…`, `f8dedd4`), que se commiteó
  mientras corría; la principal usó las extracciones finales de la tanda 0 (`ad6d5ad`).
- **Costo de la regla de composición.** ≈ USD 0,13 en la principal y ≈ USD 0,50 en la réplica, dentro de
  U-REEXT-T0. Las dos cifras parten de tokens supuestos, no verificados.
- **Títulos terminados en «:» sin unidad propia en la partición: 87 contra 85.** La diferencia es de
  definición y está resuelta. La principal cuenta todo tramo heredado de tipo `encabezado` que termina en
  «:» y no tiene mini-chunk `::intro` (`../code/censo_estructural.py:45-47`; `../salidas/censo_estructural.json`,
  `particion_b584.n_chapeau_titulo_sin_unidad` = 87). La réplica excluye los encabezados de sección, los
  que tienen `unidad_origen` con «S» inicial (`censo_encabezados_udiag_a7ef8581.py:29`;
  `censo_particion_udiag_a7ef8581.json`, `total.A_titulo_con_dos_puntos_sin_intro` = 85). Las dos unidades
  que explican la diferencia son títulos de sección de regímenes informativos: `ri_psprca::S4` («4. Lugar
  de emisión de la tarjeta utilizada / de la entidad debitada:») y `ri_sef::S11` («11. Domicilio y
  teléfono:»). Recomputado sobre `data/experiment/segmentacion_84/b584_particion/` con las dos
  definiciones: 87 y 85, y esas dos unidades como única diferencia.

## Qué se decidió

Las decisiones tomadas sobre las dos entregas están en `docs/plan_tesis.md:398` y en la nota fechada del
03/10/2026 al pie de `docs/mandatos/UPROMPT_R2_prefijo_nuevo.md`.
