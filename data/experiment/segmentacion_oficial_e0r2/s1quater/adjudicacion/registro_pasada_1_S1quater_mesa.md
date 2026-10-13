# U-SEG-OFICIAL, S1-quater: la pasada 1 de la adjudicación, armada (registro de la mesa, 13/10/2026)

USD 0, sin API. Este registro no lleva ninguna cifra ni marca de la lectura.

## Lo que hizo la autora

- **Los commits previos:** corrió `a3c079a2` (la nota del piso al mandato y al checklist) y `ea7eabdd` (los scripts de la adjudicación
  sellados), con sus pruebas en seco, y los pusheó.
- **El comando de la mesa** (`comando_pasada_1_S1quater_para_la_autora.sh`, sha256 `d08e38941d0279cd…`, 31 renglones):
  - controla el script de la pasada 1 y el sello de esta carpeta;
  - armó la pasada 1 en la carpeta de la autora, fuera del repo, desde el tar sellado de las fichas (`86275bfd…`), con las dos etapas
    enteras (`ETAPAS="1,2"`).
- **Lo que dio el comando,** según la autora:
  - etapa 1: 90 fichas y 95 imágenes, `manifest.txt` `ab08860228496a89…`, 98 OK y 0 no OK;
  - etapa 2: 60 fichas y 104 imágenes, `manifest.txt` `bfdf3c571fe3d6f8…`, 107 OK y 0 no OK.
- **Además, según la autora:** el repo no cambió, y sus 15 sellos dan.

## El control de la mesa

Sin abrir ni listar la carpeta de la autora.

- **El comando que corrió** es el del paquete de la mesa: el mismo sha256 y los mismos 31 renglones.
- **El registro de la mesa** (`orden_pasada_1_S1quater.json`, sha256 `eb3291adfcae5357…`, escrito a las 16:29:12 según la fecha del
  archivo) coincide con eso:
  - **etapa 1:** 90 fichas y 95 imágenes, `manifest.txt` `ab08860228496a89…`;
  - **etapa 2:** 60 fichas y 104 imágenes, `manifest.txt` `bfdf3c571fe3d6f8…`;
  - **las cuentas del manifest** (98 y 107) son las imágenes más las fichas, la planilla vacía y el LEEME de cada etapa;
  - **las entradas** son las selladas: el tar de las fichas `86275bfd…`, el orden de lectura `b794f85f…` y los `manifest.txt` de la
    carpeta de la lectora `110565d7…` y `37580fbc…`;
  - **el orden de cada etapa** es el que da su semilla, `U-SEG-OFICIAL:adjudicacion:S1-quater:{etapa}`, y usa solo ids opacos;
  - **ninguna marca.**
- **El registro con el orden queda fuera del repo** hasta que termine la adjudicación. Es una elección de la mesa, por analogía con
  la muestra y el orden de lectura, que la autora dejó fuera del repo hasta ese momento
  (`../sorteo/revision_y_decisiones_sorteo_S1quater_mesa.md:10`). Entra con el cierre, con el sha256 de arriba.
