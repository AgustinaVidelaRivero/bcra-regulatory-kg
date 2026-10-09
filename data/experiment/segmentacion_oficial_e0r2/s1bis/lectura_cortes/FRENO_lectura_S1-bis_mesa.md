# FRENO — U-SEG-OFICIAL, lectura de cortes de S1-bis (mesa revisora, sesión nueva), 08/10/2026

USD 0, sin API. Nada commiteado. Escrituras: `s1bis/lectura_cortes/` (6 archivos nuevos) y el scratchpad.

**Entrada.** Paquete del FRENO S1-bis-b (copia permanente): 324 de 324 sha256 y tamaños iguales al `manifest.txt`. Criterio: texto firmado de `e543cb2` y la nota de `2faff14` (líneas 275 a 341). Log: `d7fc0205` en la punta.

**Sellos** (`sello_lectura_S1bis.txt`):
- etapa 1, `planilla_marcas_S1-bis-b_mesa.tsv` (111 filas): `dd2775afba5dced5147a8e920af77827121d4440a35e139483d62e5aac315cd7`, 18:40:56;
- etapa 2, `planilla_1_16_S1-bis-b_mesa.tsv` (35 filas), abierta después del sello 1: `5969e0ab9aed328fcc94c2832943af26c0c7fb243d89ff5c6e71461168995401`, 18:45:11.

**El piso no se alcanza.** 85 de 90 sin error de corte. Wilson al 95 %: [0,8765; 0,9760]. Se necesita 0,90 o más, es decir, 3 errores o menos. No hay dudosas, así que las dos variantes dan lo mismo. Ningún límite declarado cayó en la muestra, así que hay una sola cifra. Por modo: vigente 37/40, marcadores 10/10, sin raíz 38/40. Los 5 errores de corte, por subclase principal:
- `adfsp::1.1.10`: termina fuera y trae el cierre de 1.1.
- `snp_dd::S7::intersticial::17` y `::13`: falta texto propio. Son la descripción del campo 4 y el resto de la fila R95.
- `ri_ccna::D1F3::S0`: termina fuera y trae una «C» del formulario siguiente.
- `ri2_ae::S2::chapeau_seccion`: empieza fuera. Es el segundo renglón del título de la sección.

**Demás cifras** (`cifras_lectura_S1bis_mesa.json`; las recomputé contra las planillas y coinciden):
- Corpus, aproximación: 0,9297, con n efectivo 53,93 y Wilson [0,8293; 0,9730].
- Limpieza: 3 en el primer grupo (`ri_iepsp::S0` y `ri_ieccm::S0` son solo resto del encabezado; `ri_icpipsp::A1C3::S2`); 0 en ri_spi; 0 en el 1.16.
- ri_spi: 10 de 10.
- Juicios: los 9 leídos son correctos, más ri_pspii (correcto) y ri_tii (límite), precargados y sin tocar.
- Errores en TOs de la tanda 0: ninguno.
- Límites declarados en la muestra: ninguno.
- Censo del 1.16: 8 de 35 con error de corte; Wilson de la fracción con error [0,121; 0,390]. Siete tienen el patrón del hallazgo: `cajasc::11.4.4`, `cajasc::4.2.2.3`, `depaho::3.11.5.5`, `manori::1.4.1.3`, `manori::3.4.1.3`, `ri_oc::B.1.28` y `ri_oc::C.11`. El octavo, `ri_rml::1.2.3`, es otro corte: pierde sus dos últimos renglones en un «1.3.» que cae dentro del párrafo.
- Candidato del 1.16 que cayó en la muestra: `adfsp::1.1.10`, marcado error con ese mismo patrón.

**Lista para la autora** (`lista_para_la_autora_S1bis_mesa.{json,md}`): 41 casos.
- 8 errores del primer grupo: 5 de corte y 3 de limpieza.
- 0 juicios dudosos.
- 20 correctas sorteadas, de una población de 92.
- 8 marcados del 1.16.
- 5 correctos del 1.16 sorteados, de una población de 27.

Las imágenes de esos casos van en `paginas_lista_lectura_S1-bis/`.

**Casos que me costaron.**
- `ri_ccna::D1F3::S0`: el error es un solo carácter. Lo marqué por el criterio (3).
- `ri2_ae::S2::chapeau_seccion`: no hay chapeau en el PDF; la unidad es la cola del título. Elegí la subclase `empieza_fuera`.
- Las dos de snp_dd: consideré la regla del párrafo sin numerar. Las dos cortan dentro de un mismo bloque, sin blanco entre los renglones.
- El piso depende de esta adjudicación. Con 4 errores da 0,891 y sigue sin pasar; pasa solo si la autora revierte 2 de los 5.

**Observaciones fuera del corte de cada unidad**, en las notas:
- 6.2.1.10 de lingeef figura como cierre de 6.2.1 en la herencia.
- A.3.6.0 y B.5.8.0 de ri_spi figuran como intro.
- `ri_chr::S11` y `ri_rem::S9` parecen tomar el número del recuadro de encabezado.

**Declaraciones.**
1. El contexto inicial del arnés traía los mensajes de los últimos commits, que no pedí ni abrí. El de `2abb346` nombra tres unidades límite de corte de S1: `nmaeef::2.9`, `ri_ccna::D1A3L1::S0` y `ri_oc::B.2::intro`. Además cuenta, sin nombrarlas, las 10 de solo rótulo y las 21 intros de la tanda 0. Al listar la planilla vi que esas tres no estaban en la muestra (el script lo confirma). No influyó en las marcas: leí todas las unidades igual. El índice de memoria nombra reglas y TOs, no unidades. No seguí sus enlaces.
2. Otro actor cambió en el repo, durante esta sesión, `CLAUDE.md` (18:27:19) y `docs/plan_tesis.md` (18:27:39). No los escribió esta sesión.
3. Errores propios, con su causa:
   - El primer borrador de la nota de la fila 3 ubicaba mal la sangría. Lo corregí antes del sello, al releer el PDF.
   - Los tres ayudantes de trabajo llevaban una ruta absoluta con el nombre de la carpeta de usuario. Lo detectó el grep y los corregí antes de armar el paquete.

**Cierre.**
- Foto del repo antes: `30c5cf5b…` (48.443 archivos). Después: `2907d0a6…` (48.449). Hay 6 archivos nuevos, todos en `lectura_cortes/`, y los 2 cambios ajenos del punto 2 (`comparacion_fotos_lectura_S1-bis.txt`).
- `.pyc` sin `.venv/`: 2.213 antes y después.
- Grep de convenciones (`grep_convenciones_lectura_S1-bis.txt`): 0 en lo escrito en `lectura_cortes/` y 0 en los ayudantes ya corregidos.
- Paquete: `revision_USEG_OFICIAL_lectura_S1-bis/`, copiado con `ditto` a `~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/c8a66a04-f751-4bc5-93f9-e760aa1b79e0/scratchpad/revision_USEG_OFICIAL_lectura_S1-bis/`. La verificación de la copia contra su `manifest.txt` va en el mensaje de cierre, porque se hace después de cerrar el manifiesto.

PENDIENTE de la autora: revisar la lista y adjudicar. La cifra final sale después de la adjudicación. Con las marcas de la mesa no se alcanza el piso: según el despacho, la salida no se commitea y S2 no se despacha mientras no lo decida la autora.

FRENO.
