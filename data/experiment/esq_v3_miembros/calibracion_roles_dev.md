# U-ESQ-V3 fase 1 — Calibración: los 5 roles dev y sus 17 miembros

Ejemplo trabajado de **la convención que el grafo vigente ya aplica**. Las 30 filas nuevas se adjudican contra esta vara.

Miembros: **7 + 2 + 6 + 1 + 1 = 17**, que son exactamente las 17 aristas `miembro_de` del grafo vigente. Por nivel: {'clase': 17} — **los 17 son de nivel `clase`; ninguno es instancia**. Ese hecho es el que fija la segunda cláusula de S15.

Fuente de los miembros: `data/experiment/grafo_v2/esquema_v2_clases.json` (SELLADO, solo lectura). Fuente de los pasajes: `data/experiment/escalado_prep/e0_dry_subset_ref/<to>/chunks_<to>.json`.

| rol_id | label | miembros | niveles | location |
|---|---|---:|---|---|
| `Sujeto_rol_sujeto_obligado_proteccion` | Sujetos obligados (Protección de usuarios) | 7 | clase | Punto 1.1.2 |
| `Sujeto_rol_entidad_autorizada_exterior` | Entidades autorizadas a operar en cambios (Exterior) | 2 | clase | Punto 1.1 |
| `Sujeto_rol_obligado_a_clasificar_clasificacion` | Obligados a clasificar deudores (Clasificación) | 6 | clase | Secciones 1 y 10 |
| `Sujeto_rol_entidad_comprendida_reginf` | Entidades comprendidas (Régimen Informativo) | 1 | clase | Sección 2 |
| `Sujeto_rol_alcance_capmin` | Entidades alcanzadas (Capitales Mínimos) | 1 | clase | Sección 1 |

## Rol por rol, con el pasaje del que salieron los miembros

### `Sujeto_rol_sujeto_obligado_proteccion` — Sujetos obligados (Protección de usuarios)
**TO:** TO_proteccion_usuarios_servicios_financieros_actual.pdf · **location declarada:** Punto 1.1.2

**Miembros adjudicados:**

- `Sujeto_entidad_financiera` — nivel `clase`
- `Sujeto_entidad_cambiaria` — nivel `clase`
- `Sujeto_fiduciario_de_fideicomiso_financiero` — nivel `clase`
- `Sujeto_empresa_no_financiera_emisora_de_tarjetas` — nivel `clase`
- `Sujeto_proveedor_no_financiero_de_credito` — nivel `clase`
- `Sujeto_pspcp` — nivel `clase`
- `Sujeto_psi_billetera_digital` — nivel `clase`

**Pasaje(s):**

`pro::1.1.2.1` · página(s) [3] · «Entidades financieras.»

```
1.1.2.1. Entidades financieras.
```

`pro::1.1.2.2` · página(s) [3] · «Operadores de cambio, por las operaciones comprendidas en las normas sobre»

```
1.1.2.2. Operadores de cambio, por las operaciones comprendidas en las normas sobre
“Exterior y cambios”.
```

`pro::1.1.2.3` · página(s) [3] · «Fiduciarios de fideicomisos acreedores de créditos cedidos por entidades finan-»

```
1.1.2.3. Fiduciarios de fideicomisos acreedores de créditos cedidos por entidades finan-
cieras.
```

`pro::1.1.2.4` · página(s) [3] · «Empresas no financieras emisoras de tarjetas de crédito y/o compra.»

```
1.1.2.4. Empresas no financieras emisoras de tarjetas de crédito y/o compra.
```

`pro::1.1.2.5` · página(s) [3] · «Otros proveedores no financieros de crédito alcanzados por las normas sobre»

```
1.1.2.5. Otros proveedores no financieros de crédito alcanzados por las normas sobre
“Proveedores no financieros de crédito”, excepto que se trate de asociaciones
mutuales o cooperativas, por las financiaciones que otorguen.
```

`pro::1.1.2.6` · página(s) [3] · «Proveedores de servicios de pago que ofrecen cuentas de pago (PSPCP).»

```
1.1.2.6. Proveedores de servicios de pago que ofrecen cuentas de pago (PSPCP).
```

`pro::1.1.2.7` · página(s) [3] · «Proveedores de servicios de pago que cumplen la función de iniciación (PSI) y»

```
1.1.2.7. Proveedores de servicios de pago que cumplen la función de iniciación (PSI) y
prestan el servicio de billetera digital.
Cuando un tercero desarrolle tareas relativas a servicios ofrecidos por los sujetos obliga-
dos o en su nombre, ambos serán responsables por el cumplimiento de las presentes
normas. Lo anterior deberá establecerse en los instrumentos que acuerden la realización
de dichas tareas.
```

### `Sujeto_rol_entidad_autorizada_exterior` — Entidades autorizadas a operar en cambios (Exterior)
**TO:** TO_exterior_cambios_actual.pdf · **location declarada:** Punto 1.1

**Miembros adjudicados:**

- `Sujeto_entidad_financiera` — nivel `clase`
- `Sujeto_entidad_cambiaria` — nivel `clase`

**Pasaje(s):**

`ext::1.1` · página(s) [7] · «En todas las operaciones de cambio, canje y/o arbitraje que se cursen por el mercado libre de»

```
1.1. En todas las operaciones de cambio, canje y/o arbitraje que se cursen por el mercado libre de
cambios, establecido por el artículo 1° del Decreto 260/02 según el texto establecido por el
artículo 132 de la Ley 27.444, en adelante “mercado de cambios”, deberán intervenir
entidades financieras o cambiarias autorizadas a operar en cambios por el Banco Central de
la República Argentina (BCRA), en adelante “entidades”.
```

### `Sujeto_rol_obligado_a_clasificar_clasificacion` — Obligados a clasificar deudores (Clasificación)
**TO:** TO_clasificacion_deudores_actual.pdf · **location declarada:** Secciones 1 y 10

**Miembros adjudicados:**

- `Sujeto_entidad_financiera` — nivel `clase`
- `Sujeto_proveedor_no_financiero_de_credito` — nivel `clase`
- `Sujeto_fiduciario_de_fideicomiso_financiero` — nivel `clase`
- `Sujeto_sociedad_de_garantia_reciproca` — nivel `clase`
- `Sujeto_fondo_de_garantia_publico` — nivel `clase`
- `Sujeto_pscpp` — nivel `clase`

**Pasaje(s):**

`cla::1.1` · página(s) [4] · «Criterio general.»

```
1.1. Criterio general.
Los clientes de la entidad (tanto residentes en el país, de los sectores público y privado, finan-
cieros y no financieros, como residentes en el exterior), por las financiaciones comprendidas,
deberán ser clasificados desde el punto de vista de la calidad de los obligados en orden al
cumplimiento de sus compromisos y/o las posibilidades que a este efecto se les asigne sobre la
base de una evaluación de su situación particular.
```

`cla::10.1` · página(s) [43] · «Proveedores no financieros de crédito.»

```
10.1. Proveedores no financieros de crédito.
Las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedo-
res no financieros de crédito alcanzados por las normas sobre “Proveedores no financieros de
crédito”, deberán clasificar a los respectivos deudores en función de su mora, según los crite-
rios aplicables para la cartera de “consumo o vivienda” y por aplicación de las disposiciones
previstas en el punto 7.3. (recategorización obligatoria).
```

### `Sujeto_rol_entidad_comprendida_reginf` — Entidades comprendidas (Régimen Informativo)
**TO:** TO_regimen_informativo_contable_mensual_actual.pdf · **location declarada:** Sección 2

**Miembros adjudicados:**

- `Sujeto_entidad_financiera` — nivel `clase`

**Pasaje(s):**

`ric::S2` · página(s) [4] · «Entidades comprendidas.»

```
Sección 2. Entidades comprendidas.
0 Entidad que no consolida, con filiales en el país y en el exterior.
1 Entidad que consolida, con filiales en el país y en el exterior.
Consolidado mensual (entidad financiera con filiales y subsidiarias significativas en el país
y en el exterior) – (con el alcance definido en el punto 6.2. de las normas sobre “Su-
2
pervisión consolidada”)
Consolidado mensual (entidad financiera con filiales y subsidiarias significativas en el país y
9 en el exterior -que no consolida con otras entidades financieras-) - (con el alcance defini-
do en el punto 6.2. de las normas sobre “Supervisión consolidada”)
Consolidado trimestral (entidad financiera con filiales, subsidiarias significativas y otros
3
entes en el país y en el exterior) – (código de consolidación suspendido desde
abril/24 según punto 6.1. de las normas sobre “Supervisión consolidada”, excepto
para Ratio de apalancamiento, -Sección 10.- que continuará presentado código 3
con el alcance definido en el punto 6.2. de las normas citadas).
Código 9
No se presentará la información consolidada mensual, debiendo consignar en su lugar una decla-
ración conteniendo los siguientes datos:
- Exigencia por riesgo de crédito (código 70100000).
- Cálculo del riesgo de tasa de interés en la cartera de inversión - Medida de riesgo EVE estan-
darizada (sólo para el último mes del trimestre) (código 70500000).
- Exigencia por riesgo de mercado para las posiciones del último día del mes (código
70800000).
- Exigencia por riesgo operacional (código 70300000).
- Responsabilidad patrimonial computable.
- En los casos que corresponda:
a) Defecto de integración por riesgos de crédito, de mercado y operacional.
b) Incremento de la exigencia de capitales mínimos por excesos en la relación de activos in-
movilizados y otros conceptos, grandes exposiciones al riesgo de crédito, financiamiento al
sector público no financiero, posiciones de derivados no cubiertos, financiaciones a clientes
vinculados y graduación del crédito, por excesos verificados en las posiciones no cubiertas
por “commodities” y por excesos a los límites ampliados de financiamiento al sector público
no financiero por financiaciones o tenencias de instrumentos de deuda de fideicomisos fi-
nancieros o fondos fiduciarios.
c) Detalle de las eventuales franquicias otorgadas y otras facilidades en caso de existir.
d) Reducción de exigencia de riesgo operacional y los datos para su determinación.
Código 3 (consolidación trimestral suspendida desde abril/24 aplicable según lo especifi-
cado en cada caso)
- La información tendrá frecuencia trimestral y se integrará con saldos al cierre del trimestre ba-
jo informe.
- Se incluirán los datos previstos para los códigos 0, 1 y 2, excepto en el caso de riesgo de
mercado y riesgo operacional, donde se informarán únicamente las partidas 70800000 y
70300000 y, de corresponder, 3600000Y y 37000000.
- Para determinar las citadas exigencias se tendrán en cuenta las instrucciones establecidas
para el cómputo mensual, en lo que resulte pertinente.
```

### `Sujeto_rol_alcance_capmin` — Entidades alcanzadas (Capitales Mínimos)
**TO:** TO_capitales_minimos_actual.pdf · **location declarada:** Sección 1

**Miembros adjudicados:**

- `Sujeto_entidad_financiera` — nivel `clase`

**Pasaje(s):**

`cap::1.1` · página(s) [4] · «Exigencia.»

```
1.1. Exigencia.
La exigencia de capital mínimo que las entidades financieras deberán tener integrada será
equivalente al mayor valor que resulte de la comparación entre la exigencia básica y la suma de
las determinadas por riesgos de crédito, de mercado –exigencia por las posiciones diarias de
los activos comprendidos– y operacional.
```

## Lectura de la calibración (lo que la vara dice y lo que no)

1. **La granularidad es la del pasaje.** `Sujeto_rol_sujeto_obligado_proteccion` tiene 7 miembros porque el punto 1.1.2 enumera siete colectivos; no se expandió a las subclases de entidad financiera ni se colapsó a `Sujeto_sujeto_regulado`.
2. **Un pasaje de un solo colectivo da un solo miembro.** Es el caso de reginf y capmin: un miembro cada uno, no una lista de conveniencia.
3. **Todos los miembros vigentes son clases.** No hay precedente de instancia como miembro de un rol — lo que no significa que esté prohibido, sino que **adjudicar la primera instancia sería estrenar la convención**, y por eso las filas con candidato `instancia` van marcadas en la tabla de adjudicación.
4. **El rol se queda con lo que el pasaje nombra.** Ningún rol dev tiene miembros que su pasaje no mencione.
5. **HAY precedente vigente de recorte absorbido, y conviene tenerlo a la vista al adjudicar las filas `mas_amplio`.** Dos de los siete subpuntos de pro traen un recorte que el miembro adjudicado no porta: `pro::1.1.2.3` dice «Fiduciarios de fideicomisos **acreedores de créditos cedidos por entidades financieras**» y el miembro es `Sujeto_fiduciario_de_fideicomiso_financiero` a secas; `pro::1.1.2.5` dice «Otros proveedores no financieros de crédito […] **excepto que se trate de asociaciones mutuales o cooperativas**» y el miembro es `Sujeto_proveedor_no_financiero_de_credito` entero. Es decir: cuando el catálogo no tiene id para el recorte, la convención vigente adjudicó **la clase más cercana que el catálogo sí tiene, sin fabricar id nuevo** — y el recorte quedó donde estaba, en el texto de la norma, alcanzable por procedencia. Esto no convierte el aplanamiento en la respuesta correcta por defecto, pero sí muestra que el grafo vigente ya lo hace en 2 de 17 miembros, y la decisión sobre las 8 filas `mas_amplio` de la tabla nueva se toma sabiéndolo.

