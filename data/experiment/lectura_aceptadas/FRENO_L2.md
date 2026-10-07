# FRENO L2 de U-LECTURA-ACEPTADAS, final de la unidad: cifras con la adjudicación, reporte y registro (07/10/2026; USD 0, sin API; sin commit)

**Precondiciones.** L0 y L1 en `6e611d6` (`git log`): los 11 archivos de `lectura_aceptadas/` con el sha256 del cierre de L1 (`sellos_l0.json` `640cb1f4…`, `veredictos_l1.jsonl` `ea932459…`, `fichas_l1.jsonl` `5fac796e…`); `git status` vacío en ellos, en el mandato y en `docs/insumos_escritura.md`; 2.213 `.pyc`. Fotos previas: 82 insumos a las 00:37:02 y el repo (23.437 archivos, 339 enlaces) a las 00:37:26.

**Adjudicación** (`adjudicacion_autora_l2.json`, sha256 `ad99a2f6…`): la lista del «seguí» («Las 10 confirmadas; las dudas quedan como observaciones»), las tres decisiones de la nota al pie y la arista A1 de `ext::3.17.3.4`, con la razón de la segunda lectura (la condición «beneficiario directo» condiciona la emisión de las certificaciones, no el tope). El script controla que la lista adjudicada sea la de las 10 de la primera lectura y que cada elemento esté en su ficha.

**Comando** (desde una copia sin enlaces; salidas en `lectura_aceptadas/`; la línea completa está en `reporte_l2.md`, §9): `l2_estimadores.py --sellos … --veredictos … --fichas … --adjudicacion … --adjudicacion-sha256 ad99a2f6… --tasas-t4 …/tasas_t4.json`. Salida:
`{"hora": "2026-10-07T00:41:45-03:00", "estratos": {"item": [6, 30, 0.2, [0.0951, 0.3731]], "no_item": [4, 30, 0.1333, [0.0531, 0.2968]]}, "W": {"item": 0.423922, "no_item": 0.576078}, "ponderado": [0.1616, 0.0927, [0.0689, 0.2543]], "conservador": [0.0709, 0.3291], "remite_a": [0, 167, 11, [0.0, 0.0225], [0.0, 0.2588]], "documentales": [4, {"punto del mismo TO": 2, "ley": 2}], "elementos_por_clase": {…}, "vigilancia_k_min": {"item": 17, "no_item": 14}}`

**Las tres cifras** (Wilson al 95 % con z = 1,959964, la fórmula de T4; pesos recomputados contando las filas de `sellos_l0.json`):
- (i) Ítems, 6 de 30 [0,0951; 0,3731]; no ítems, 4 de 30 [0,0531; 0,2968]; W₁ = 1.003/2.366 = 0,423922. **Ponderada, la tasa del grafo: 0,1616 ± 0,0927 = [0,0689; 0,2543]** (con 1,96, igual a cuatro decimales); conservadora [0,0709; 0,3291]. Cola de T4: 12 de 30 [0,2459; 0,5768]. Los cuatro intervalos se superponen con el de la cola; el p̂ ponderado queda por debajo de su límite inferior.
- (ii) `remite_a`: 0 de 167 no sostenidas, en 11 unidades (ítems: 46 en 6; no ítems: 121 en 5). Wilson por aristas [0; 0,0225] y por unidades [0; 0,2588]; las aristas no son independientes.
- (iii) Como observación: 4 nodos `Comunicacion` en 2 unidades, dos puntos del mismo TO en `cap::6.1.4.2` y dos leyes en `pro::S5`.

**Recomputación independiente** (otro código con las mismas fórmulas, desde `veredictos_l1.jsonl`, la adjudicación y el sello; salida en el paquete): las mismas cifras, que coinciden con `estimadores_l2.json` a 1e-12. Segunda corrida: `estimadores_l2.json` igual salvo la hora; `reporte_l2.md` difiere solo en la línea de la hora.

**Reporte** (`reporte_l2.md`, generado por el script con los mismos números): método, las tres cifras con sus intervalos y la tabla de las 10 con su elemento y su clase. Son 15 elementos: relación no sostenida, 5 en 4 unidades; causal de rechazo leída como prohibición, 5 en 2; permiso leído como deber, 2 en 2; sujeto equivocado, 1; rótulo y tipo invertidos, 1; deber acotado leído como prohibición, 1. Lleva también el descriptivo por estado y por TO, las omisiones aparte (19 ítems y 9 no ítems), las 9 dudas como observaciones, las 7 unidades sin nodos de contenido, el solapamiento con T4 (6 de 60: 3 con error y 3 sin error), la declaración de `cla::1.2.1` (sin error en las dos lecturas) y la vigilancia.

**Vigilancia** (reporte, §8; el pre-registro no se tocó): 60 unidades por tanda en dos estratos, con el mismo sorteo (la semilla la fija el pre-registro) y el mismo criterio; las tres cifras. Umbral de atención: el LI de Wilson de la tanda por encima del LS de la tanda 0. Ítems, más de 0,3731 (17 de 30 o más); no ítems, más de 0,2968 (14 de 30 o más); ponderado, con el conservador, más de 0,3291.

**Registro.** `docs/insumos_escritura.md` §7, ítem 5 nuevo: `git diff --numstat` da `11 0`; los ítems 1 a 4 quedan sin tocar.

**Para decidir:** el umbral ponderado lo escribí con el intervalo conservador, que es el único hecho con límites de Wilson. Si el pre-registro prefiere el ponderado del §5, el LS de la tanda 0 es 0,2543 (está anotado en el reporte).

**Error propio**, corregido antes de la corrida oficial. En la corrida de prueba, que fue al scratchpad, el reporte decía, con una frase escrita a mano, que el intervalo ponderado quedaba por debajo del de la cola. No es así: 0,2543 > 0,2459. Ahora la comparación la computa el script. Tenía también escritos a mano el «siete» de las unidades sin contenido y la hora de las fichas; ahora salen de los datos.

**Controles de cierre:** 81 de los 82 insumos con el mismo sha256 antes y después; el que cambia es `insumos_escritura.md`, que es la escritura autorizada. En el repo hay 5 archivos nuevos, todos en `lectura_aceptadas/`: `adjudicacion_autora_l2.json`, `l2_estimadores.py`, `estimadores_l2.json`, `reporte_l2.md` y este freno; el único cambiado es `insumos_escritura.md`; 0 quitados; enlaces iguales (339). 2.213 `.pyc`; la copia, sin enlaces ni `.pyc`. Grep de convenciones sobre lo escrito: vacío, con control positivo (en el paquete).

**Paquete:** `revision_ULECTURA_ACEPTADAS_FRENO_L2/` (scratchpad), con `manifest.txt`.

**Commit PENDIENTE de la autora. L2 es la última etapa de la unidad; su cierre queda PENDIENTE de la revisión y del commit. Freno final.**
