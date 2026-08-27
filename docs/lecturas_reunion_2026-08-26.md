# Insumos de lectura de la reunión de mentores del 26/08/2026

Registro de los materiales entregados como insumo de background y de related work, con la
justificación técnica de por qué cada uno entra. Rige la regla dura de la tesis: **no se cita lo
que no se leyó/verificado**; este archivo es una lista de lectura, no una bibliografía — una
entrada solo pasa a `docs/tesis/bibliografia.bib` después de verificarse contra la primera página
del PDF.

Encuadre que ordena toda la barrida: **esta tesis es una tesis de recurso**. El related work
relevante no se limita a extracción de conocimiento en dominio financiero; incluye trabajos que
**publican un KG como artefacto** en cualquier disciplina y lo que hoy se considera
metodológicamente exigible en un KG construido con LLMs. Método acordado: lectura en diagonal
primero, selección de 3–4 para lectura en serio después (unidad U-RW).

## 1. Background metodológico (tesis)

| # | Insumo | Por qué entra | Estado |
|---|---|---|---|
| L1 | Tesis sobre generación automática de preguntas basada en grafos de conocimiento para optimización de sistemas de recuperación aumentada (LCD, Exactas, UBA) — https://lcd.exactas.uba.ar/generacion-automatica-de-preguntas-basada-en-grafos-de-conocimiento-para-optimizacion-de-sistemas-de-recuperacion-aumentada/ | Antecedente metodológico directo: generación de preguntas sobre KG para evaluar RAG — toca el mismo problema que EV2 y la construcción de eval sets. | por leer |
| L2 | Tesis entregada como archivo (`Tesis.pdf`) | Segundo antecedente metodológico; referencia de estructura y de capítulo de background de KG (cierra el pedido de material de background). | por leer — archivo en poder de la autora |

## 2. Papers de recurso canónicos (KG pre-LLM)

| # | Insumo | Por qué entra | Estado |
|---|---|---|---|
| L3 | YAGO — DOI 10.1145/1242572.1242667 (WWW 2007) | Uno de los papers de KG más citados; **paper de recurso**, que es exactamente el género de esta tesis. Referencia de cómo se presenta un KG como artefacto (esquema, construcción, evaluación de calidad). | por leer |
| L4 | YAGO2 — Hoffart, Suchanek, Berberich, Weikum; *Artificial Intelligence* 194 (2013); DOI 10.1016/j.artint.2012.06.001 | Versión extendida y revisada de L3 (el enlace firmado de las notas de la reunión venció: era una URL de descarga con expiración de minutos). Identificado por DOI, no por el enlace muerto. | por leer |
| L5 | https://pure.mpg.de/rest/items/item_2077946/component/file_2077968/content | Insumo entregado en la reunión, del mismo repositorio institucional que la familia anterior. **Por identificar**: no se registra autoría ni título sin abrir el archivo. | por identificar |
| L6 | https://pure.mpg.de/rest/items/item_1819068_3/component/file_1840695/content | Ídem L5. **Por identificar**. | por identificar |

## 3. KG con LLMs en otras disciplinas (barrida de releases, U-RW)

| # | Insumo | Por qué entra | Estado |
|---|---|---|---|
| L7 | https://www.nature.com/articles/s41597-023-01960-3 | Release de KG en dominio médico. **Revisar con cuidado**: es de 2023, en el borde del cambio metodológico que trajeron los LLMs — sirve para separar lo pre-LLM de lo post-LLM. | por leer |
| L8 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12995551/ | Trabajo más actual del mismo dominio; contraste temporal con L7. | por leer |
| L9 | https://arxiv.org/abs/2510.20345 | Construcción de KG asistida por LLMs (*LLM empowered KG construction*): metodología directamente comparable con el pipeline E0–E5 de esta tesis. | por leer |
| L10 | https://www.dbpedia.org/about/ | Uno de los primeros KG publicados como recurso; interesa por sus **publicaciones recientes** (cómo un recurso veterano se adapta al escenario post-LLM). | por leer |

## 4. Perfiles a seguir (no son citas)

| # | Insumo | Por qué entra | Estado |
|---|---|---|---|
| L11 | https://scholar.google.com/citations?hl=en&user=ymKWDvoAAAAJ&view_op=list_works&sortby=pubdate | Perfil de autoría activa en construcción de KG; se usa como **puerta de entrada** para descubrir publicaciones recientes, no como fuente citable ni como referencia de autoridad. | pendiente de barrida |
| L12 | https://scholar.google.com/citations?hl=en&user=INQwsQkAAAAJ&view_op=list_works&sortby=pubdate | Ídem L11, segunda línea de trabajo del área. | pendiente de barrida |

## 5. Criterio de selección para la lectura en serio

De la barrida en diagonal se eligen 3–4 trabajos que cumplan, en este orden de prioridad:

1. **Presentan un recurso** (un KG publicado), no solo un método de extracción.
2. Son **post-LLM** o permiten contrastar el antes/después del cambio metodológico.
3. Declaran **cómo evaluaron** el recurso (calidad, cobertura, corrección), que es el punto donde
   esta tesis hace su aporte metodológico.
4. Vienen de **otra disciplina**: el objetivo declarado de la barrida es detectar sesgos y puntos
   ciegos propios del dominio financiero.

Salida esperada de U-RW: mapa de lecturas + lista de puntos metodológicos a los que esta tesis
debe responder, con marca de cuáles ya están cubiertos por el trabajo hecho y cuáles abren deuda.
