# U-PROMPT-R2 — FRENO de la clase «modalidad» del contador de `meta_normativo` (posterior a P3c-2)

04/10/2026. HEAD `599b304` (P3c-2 commiteada por la autora). Sin commit, sin API, sobre copias sin enlaces (regla l).
Decisión de la autora posterior al commit de P3c-2; la nota del mandato que la deja pendiente es la de `599b304`
(«De la revisión, PENDIENTE de decisión de la autora»). Cambian `pyd_r2/code/validador_r2.py` y
`pyd_r2/code/selftest_pyd_r2.py`, más este freno. La lista de modalidad de `freno_p3c2.md:107-108` queda reemplazada
por la de abajo.

## 1. La definición y las marcas

**La modalidad del prefijo** (prueba de la regla 9, reemplazo P3C-a3): «si algo se exige, se permite o se aconseja, o
si basta una entre varias opciones». Lo que se exige y lo que se permite ya lo cuentan deber y facultad. La clase
«modalidad» queda con tres subclases (`validador_r2.SUBCLASES_MODALIDAD`, `:331`), cada una con su contador
(`omisiones.meta_normativo_con_marca:modalidad.<subclase>`, `:1407`). La clase cuenta si marca alguna.

Sobre el tramo en minúsculas, sin tildes y con palabras enteras:
- **opción** (si basta una entre varias o se exigen todas): indistintamente, concurrentemente, cualquiera de,
  alguno de, alguna de, a opción de, alternativa(s), alternativamente. Salen de la definición y de los cuantificadores
  del prefijo («alguno de», «cualquiera de», «concurrentemente», en COMPOSICIÓN CON EL ENCABEZADO DE UNA LISTA), más
  «indistintamente» y «a opción de». «Alternativa(s)» y «alternativamente» estaban en la lista anterior y pasan acá.
- **consejo** (lo que se aconseja): se recomienda(n), se aconseja(n), buena(s) práctica(s), práctica(s) que se
  espera(n), y un verbo copulativo (es, sea, será, resulta, resulte, resultará, en singular o plural) seguido de
  recomendable(s), aconsejable(s), deseable(s) o conveniente(s). Salen de la definición y de la RECOMENDACIÓN de
  Obligacion en el prefijo («deseable», «conveniente», «práctica que se espera»).
- **forma** (el medio o la forma de un acto; un requisito de forma también es contenido normativo): mediante, por
  medio de, a través de, por intermedio de, por escrito, en forma, en soporte, por vía, modalidad(es). Son las marcas
  anteriores de medio o forma, sin cambios.
- **Fuera de la lista:** «o», «y» y «la totalidad», que el prefijo también nombra como cuantificadores, porque marcan
  disyunción o cantidad sin modalidad.

Ninguna marca nueva sale de un caso de P4. Sigue contando sin rechazar.

## 2. Selftest

`selftest_pyd_r2` (G16, 3 casos nuevos): da **398/398**.
- Una omisión por subclase y una de finalidad con «mediante» (`selftest_pyd_r2.py:1459`): opción 1, consejo 1 y forma
  2, y la clase cuenta las 4.
- **La finalidad con «mediante» cae en forma:** el contador la cuenta como `modalidad`, sin otra clase, y la subclase
  la separa. Es el falso positivo que la subclase deja ver; no se excluye.
- Las marcas de opción y de consejo de la decisión caen en su subclase.

## 3. P4 re-validada

Con `p3c2/revalidar_p4_p3c2.py` (sin cambios) y, para las subclases, los contadores del validador
(`conteo_subclases_p4.json`, en el paquete de revisión), sobre la salida guardada del brazo nuevo:

| Clase | P3c-2 | Ahora |
|---|---|---|
| deber | 5 | 5 |
| prohibición | 0 | 0 |
| facultad | 0 | 0 |
| condición | 4 | 4 |
| excepción | 2 | 2 |
| alcance | 3 | 3 |
| modalidad | 2 | 5 |
| — opción | | 5 |
| — consejo | | 0 |
| — forma | | 0 |
| **Omisiones marcadas, de 24** | **15** | **17** |

- **Detecta las 9 normativas,** como antes; `ctacte::8.3::intro` y `ctacte::8.4::intro` pasan de la lista anterior
  («alternativas») a opción («cualquiera de» y «alternativas»).
- **Marcadas fuera de las 9: 8.** Las 6 de antes, y `polcre::7.1::intro` suma opción («concurrentemente») a su
  condición. Entran dos nuevas: `cap::8.5.2` y `cap::8.5.3`, por «cualquiera de» («la falta de cumplimiento de
  cualquiera de estos límites…»), que la autora no contó entre las 9.
- **Marcas:** 19 en 17 omisiones (`cla::5.1.1.1` y `polcre::7.1::intro` traen dos).
- **Forma no marca ninguna en P4:** las dos de modalidad de P3c-2 eran «alternativas», hoy opción. Ninguna omisión
  queda marcada solo por forma.

## 4. Controles

Doble corrida sobre una copia sin enlaces (`control_modalidad.sh` y su log, en el paquete), con lo que cambia y los
controles de claves y de la cadena:
- **Iguales entre corridas** las 6 salidas comparadas: la re-validación, el conteo por subclase, las dos fixtures, el
  JSON del selftest de claves y la cadena r2a.
- **Ninguna clave cambia:** el JSON del selftest de claves es igual al del repo, con veredicto OK y contraste con la
  tabla OK; las fixtures de los mensajes de E1 y de E3 son iguales a las del repo, así que los candados no frenan.
- **Cadena r2a:** diez `70d51e42…` y desarrollo `fa4c1043…`.
- **Selftests:** `selftest_pyd_r2` 398/398, `selftest_e1` 80/80, `selftest_e3` 101/101, cadenas de P3 27/27 y de
  P3b-2 20/20.
- **El repo** no cambió durante el control (12.875 archivos). Ningún `.pyc` nuevo. Grep de convenciones vacío.

## 5. Para la autora

- **`p3c2/salida/revalidacion_p4_p3c2.json`**, commiteado con P3c-2, queda con las cifras de P3c-2 (15 de 24): esta
  corrección no lo regenera, porque no está entre sus escrituras. La salida nueva está en el paquete.
- **PENDIENTE:**
  - el commit de esta corrección;
  - el «seguí» de P4b, que cuenta el contador por brazo, con sus subclases.
