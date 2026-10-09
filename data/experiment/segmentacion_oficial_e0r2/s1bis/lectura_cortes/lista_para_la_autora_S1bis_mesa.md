# U-SEG-OFICIAL — S1-bis: lista para la autora de la lectura de cortes (mesa revisora)

Versión legible de `lista_para_la_autora_S1bis_mesa.json`, generada después de los dos sellos de `sello_lectura_S1bis.txt` con `scripts/lista_para_la_autora_S1bis.py` sobre una copia (sha256 del script igual al del paquete del FRENO S1-bis-b). Planillas: `planilla_marcas_S1-bis-b_mesa.tsv` (`dd2775afba5dced5…`) y `planilla_1_16_S1-bis-b_mesa.tsv` (`5969e0ab9aed328f…`).

Las imágenes están en `paginas_S1-bis-b/` del paquete del FRENO S1-bis-b (copia permanente en `~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/0c0c6584-4c87-4d3c-b3b4-425c9ab87db2/scratchpad/revision_USEG_OFICIAL_FRENO_S1-bis-b/`); las de los casos de esta lista van también en el paquete de revisión de la lectura, en `paginas_lista_lectura_S1-bis/`.

## Contenido

| parte | casos |
|---|---|
| 1. Errores y dudosas del primer grupo y de ri_spi | 8 (5 de corte y 3 de limpieza; ninguna dudosa) |
| 2. Juicios dudosos | 0 |
| 3. Correctas sorteadas del primer grupo y de ri_spi (semilla `U-SEG-OFICIAL:cortes:S1-bis:revision`, población 92) | 20 |
| 4. Censo del 1.16: marcados y dudosos | 8 (todos de corte; ninguno dudoso) |
| 5. Censo del 1.16: correctos sorteados (semilla `U-SEG-OFICIAL:1_16:S1-bis:revision`, población 27) | 5 |

Total: 41 casos.

## 1. Errores y dudosas del primer grupo y de ri_spi

### adfsp::1.1.10

- ficha 3 de `fichas_lectura_S1-bis-b.md` (primer grupo); grupo G1-vigente; TO adfsp; páginas 4,5
- imagen: `paginas_S1-bis-b/adfsp_p4.png`, `paginas_S1-bis-b/adfsp_p5.png`
- marca de la mesa: **error · corte · termina_fuera + trae_texto_de_otro_punto**
- nota: pp. 4-5: la unidad sigue, en la p. 5, con los párrafos «En caso de que alguna entidad financiera deje de reunir los requisitos previstos precedentemente…» y «No se exigirán los requisitos previstos en los puntos 1.1.1. a 1.1.5.…». En la página están en la sangría de los rótulos 1.1.1 a 1.1.10 (la del cuerpo de 1.1), no en la del texto de 1.1.10, y hablan de todos los requisitos de 1.1: son el cierre de 1.1, no texto de 1.1.10.

Texto propio de la unidad (de la ficha):

```text
1.1.10. Presentar “Solicitud de participación”, conforme al modelo previsto en el punto 6.1., la
que deberá ser transcripta en el Libro de Actas de Directorio o libro equivalente, según
el tipo societario de la entidad.
En caso de que alguna entidad financiera deje de reunir los requisitos previstos precedente-
mente, será automáticamente desafectada de la nómina de entidades elegibles, debiendo con-
cluir el recupero de los préstamos, transfiriendo sus importes al Banco Central en tiempo y
forma.
No se exigirán los requisitos previstos en los puntos 1.1.1. a 1.1.5., a los bancos públicos cu-
yas operaciones se encuentren garantizadas por los Estados Nacional, provinciales, municipa-
les o de la Ciudad Autónoma de Buenos Aires.
```

### snp_dd::S7::intersticial::17

- ficha 12 de `fichas_lectura_S1-bis-b.md` (primer grupo); grupo G1-vigente; TO snp_dd; páginas 50
- imagen: `paginas_S1-bis-b/snp_dd_p50.png`
- marca de la mesa: **error · corte · falta_texto_propio**
- nota: p. 50 (Página 20 de la sección 7): la unidad es solo el renglón «4. Contador de registro de transacción original.»; en la página ese renglón va pegado, sin blanco, a su descripción sangrada «Este campo lleva el contador de registro de la transacción que está siendo rechazada (Para el caso de rechazo de débitos…)», que es el resto del mismo bloque del campo 4 y no está en la unidad.

Texto propio de la unidad (de la ficha):

```text
4. Contador de registro de transacción original.
```

### snp_dd::S7::intersticial::13

- ficha 19 de `fichas_lectura_S1-bis-b.md` (primer grupo); grupo G1-vigente; TO snp_dd; páginas 49
- imagen: `paginas_S1-bis-b/snp_dd_p49.png`
- marca de la mesa: **error · corte · falta_texto_propio**
- nota: p. 49 (Página 19 de la sección 7): la unidad es solo el primer renglón de la fila R95 de la tabla de códigos («R95 Reversión de En- … presente una»); le falta el resto de la misma fila: «tidad receptora presentada fuera de término» y «reversión de banco receptor fuera del término».

Texto propio de la unidad (de la ficha):

```text
R95 Reversión de En- Este código podrá ser utilizado por el banco originante en caso que la entidad receptora presente una
```

### ri_iepsp::S0

- ficha 59 de `fichas_lectura_S1-bis-b.md` (primer grupo); grupo G1-sin_raiz; TO ri_iepsp; páginas 1
- imagen: `paginas_S1-bis-b/ri_iepsp_p1.png`
- marca de la mesa: **error · limpieza · restos_encabezado**
- nota: p. 1: el único texto propio de la unidad, «“PROVEEDORES NO FINANCIEROS DE CRÉDITO”», es el tercer renglón del recuadro de encabezado de la página (título del TO, que se repite en el encabezado de la p. 2); el rótulo «Preámbulo» no está en el PDF. Antes de «1. Sujetos alcanzados.» la página no tiene texto de norma: la unidad está hecha solo de resto de encabezado. Los cortes (encabezado / punto 1) están bien.

Texto propio de la unidad (de la ficha):

```text
Preámbulo
“PROVEEDORES NO FINANCIEROS DE CRÉDITO”
```

### ri_ccna::D1F3::S0

- ficha 62 de `fichas_lectura_S1-bis-b.md` (primer grupo); grupo G1-sin_raiz; TO ri_ccna; páginas 33,34,35,36,37,38,39
- imagen: `paginas_S1-bis-b/ri_ccna_p33.png`, `paginas_S1-bis-b/ri_ccna_p34.png`, `paginas_S1-bis-b/ri_ccna_p35.png`, `paginas_S1-bis-b/ri_ccna_p36.png`, `paginas_S1-bis-b/ri_ccna_p37.png`, `paginas_S1-bis-b/ri_ccna_p38.png`, `paginas_S1-bis-b/ri_ccna_p39.png`
- marca de la mesa: **error · corte · termina_fuera + trae_texto_de_otro_punto**
- nota: pp. 33-39: el formulario «Solicitud de inscripción» (1 y Cont. 2 a 6) ocupa las pp. 33-38 y termina en «Fórm. 4368 C (II-2006)» (p. 38). La unidad agrega después una «C» suelta que es la primera letra del rótulo vertical «C O D I G O» del formulario siguiente, «Antecedentes del “socio responsable”» (p. 39). El resto de la p. 39 no está en la unidad. Es un solo carácter, pero el corte cae dentro del formulario siguiente.

Texto propio de la unidad (de la ficha):

```text
BANCO CENTRAL DE LA REPUBLICA ARGENTINA SOLICITUD DE INSCRIPCIÓN 1
SUPERINTENDENCIA DE ENTIDADES FINANCIERAS Y CAMBIARIAS
Gerencia de Control de Auditores
ORIGINAL RECTIFICACIÓN Nº ........(1)
REGISTRO DE ASOCIACIONES DE
PROFESIONALES UNIVERSITARIOS
Denominación:
Domicilio: Código Postal: Teléfono:
REGISTRO DE ASOCIACIONES DE PROFESIONALES UNIVERSITARIOS del Consejo Profesional de Ciencias Económicas de
T° F° Fecha: / /
Solicitamos la inscripción del Estudio de auditoría indicado precedentemente en el REGISTRO DE ASOCIACIONES DE
PROFESIONALES UNIVERSITARIOS (Circular CONAU - 1) comprometiéndonos, con carácter de Declaración Jurada, a comunicar a la
Superintendencia de Entidades Financieras y Cambiarias, Gerencia de Control de Auditores, cualquier modificación por incorporación o
retiro de alguno de nuestros socios.
El estudio de profesionales se obliga como fiador solidario, con renuncia a los beneficios de división y excusión, por las even-
tuales multas que se apliquen a cualquiera de sus integrantes, por el ejercicio de las tareas de auditoría externa en entidades financieras,
de acuerdo con lo establecido por los artículos 41 y 42 de la Ley de Entidades Financieras por infracciones al régimen normativo vigente
al momento de los hechos.
A continuación se proporcionan los datos de los socios, para su incorporación al referido registro.
Lugar y fecha:
Representante Legal (2)
Firma y aclaración
NOMINA DE LOS SOCIOS A INSCRIBIR:
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
CERTIFICACION DE FIRMAS
Lugar y fecha:
Firma y aclaración
(1) Marcar con “X” el cuadro que corresponda. Numerar secuencialmente las rectificaciones de la fórmula original. (2) A integrar por quien
jurídicamente se encuentre habilitado para asumir tales responsabilidades en nombre del Estudio, acreditando dicha facultad con la copia
certificada por escribano público del instrumento correspondiente. (3) Indicar según corresponda: L.E., L.C. o D.N.I.
Fórm. 4368 C (II-2006)
BANCO CENTRAL DE LA REPUBLICA ARGENTINA SOLICITUD DE INSCRIPCIÓN Cont. 2
SUPERINTENDENCIA DE ENTIDADES FINANCIERAS Y CAMBIARIAS
Gerencia de Control de Auditores
ORIGINAL RECTIFICACIÓN Nº ........(1)
REGISTRO DE ASOCIACIONES DE
PROFESIONALES UNIVERSITARIOS
Denominación:
Domicilio: Código Postal: Teléfono:
NOMINA DE LOS SOCIOS A INSCRIBIR:
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
CERTIFICACION DE FIRMAS
Lugar y fecha:
Firma y aclaración
(1) Marcar con “X” el cuadro que corresponda. Numerar secuencialmente las rectificaciones de la fórmula original. (2) A integrar por quien
jurídicamente se encuentre habilitado para asumir tales responsabilidades en nombre del Estudio, acreditando dicha facultad con la copia
certificada por escribano público del instrumento correspondiente. (3) Indicar según corresponda: L.E., L.C. o D.N.I.
Fórm. 4368 C (II-2006)
SOLICITUD DE INSCRIPCIÓN Cont. 3
BANCO CENTRAL DE LA REPUBLICA ARGENTINA
SUPERINTENDENCIA DE ENTIDADES FINANCIERAS Y CAMBIARIAS
Gerencia de Control de Auditores
ORIGINAL RECTIFICACIÓN Nº ........(1)
REGISTRO DE ASOCIACIONES DE
PROFESIONALES UNIVERSITARIOS
Denominación:
Domicilio: Código Postal: Teléfono:
NOMINA DE LOS SOCIOS A INSCRIBIR:
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
CERTIFICACION DE FIRMAS
Lugar y fecha:
Firma y aclaración
(1) Marcar con “X” el cuadro que corresponda. Numerar secuencialmente las rectificaciones de la fórmula original. (2) A integrar por quien
jurídicamente se encuentre habilitado para asumir tales responsabilidades en nombre del Estudio, acreditando dicha facultad con la copia
certificada por escribano público del instrumento correspondiente. (3) Indicar según corresponda: L.E., L.C. o D.N.I.
Fórm. 4368 C (II-2006)
SOLICITUD DE INSCRIPCIÓN Cont. 4
BANCO CENTRAL DE LA REPUBLICA ARGENTINA
SUPERINTENDENCIA DE ENTIDADES FINANCIERAS Y CAMBIARIAS
Gerencia de Control de Auditores
ORIGINAL RECTIFICACIÓN Nº ........(1)
REGISTRO DE ASOCIACIONES DE
PROFESIONALES UNIVERSITARIOS
Denominación:
Domicilio: Código Postal: Teléfono:
NOMINA DE LOS SOCIOS A INSCRIBIR:
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
CERTIFICACION DE FIRMAS
Lugar y fecha:
Firma y aclaración
(1) Marcar con “X” el cuadro que corresponda. Numerar secuencialmente las rectificaciones de la fórmula original. (2) A integrar por quien
jurídicamente se encuentre habilitado para asumir tales responsabilidades en nombre del Estudio, acreditando dicha facultad con la copia
certificada por escribano público del instrumento correspondiente. (3) Indicar según corresponda: L.E., L.C. o D.N.I.
Fórm. 4368 C (II-2006)
SOLICITUD DE INSCRIPCIÓN Cont. 5
BANCO CENTRAL DE LA REPUBLICA ARGENTINA
SUPERINTENDENCIA DE ENTIDADES FINANCIERAS Y CAMBIARIAS
Gerencia de Control de Auditores
ORIGINAL RECTIFICACIÓN Nº ........(1)
REGISTRO DE ASOCIACIONES DE
PROFESIONALES UNIVERSITARIOS
Denominación:
Domicilio: Código Postal: Teléfono:
NOMINA DE LOS SOCIOS A INSCRIBIR:
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
CERTIFICACION DE FIRMAS
Lugar y fecha:
Firma y aclaración
(1) Marcar con “X” el cuadro que corresponda. Numerar secuencialmente las rectificaciones de la fórmula original. (2) A integrar por quien
jurídicamente se encuentre habilitado para asumir tales responsabilidades en nombre del Estudio, acreditando dicha facultad con la copia
certificada por escribano público del instrumento correspondiente. (3) Indicar según corresponda: L.E., L.C. o D.N.I.
Fórm. 4368 C (II-2006)
SOLICITUD DE INSCRIPCIÓN Cont. 6
BANCO CENTRAL DE LA REPUBLICA ARGENTINA
SUPERINTENDENCIA DE ENTIDADES FINANCIERAS Y CAMBIARIAS
Gerencia de Control de Auditores
ORIGINAL RECTIFICACIÓN Nº ........(1)
REGISTRO DE ASOCIACIONES DE
PROFESIONALES UNIVERSITARIOS
Denominación:
Domicilio: Código Postal: Teléfono:
NOMINA DE LOS SOCIOS A INSCRIBIR:
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
Apellido y nombres:
Documento de identidad: Tipo (3): Número:
Matrícula: Tomo: Folio: Firma
CERTIFICACION DE FIRMAS
Lugar y fecha:
Firma y aclaración
(1) Marcar con “X” el cuadro que corresponda. Numerar secuencialmente las rectificaciones de la fórmula original. (2) A integrar por
quien jurídicamente se encuentre habilitado para asumir tales responsabilidades en nombre del Estudio, acreditando dicha facultad con
la copia certificada por escribano público del instrumento correspondiente. (3) Indicar según corresponda: L.E., L.C. o D.N.I.
Fórm. 4368 C (II-2006)
C
```

### ri_ieccm::S0

- ficha 70 de `fichas_lectura_S1-bis-b.md` (primer grupo); grupo G1-sin_raiz; TO ri_ieccm; páginas 1
- imagen: `paginas_S1-bis-b/ri_ieccm_p1.png`
- marca de la mesa: **error · limpieza · restos_encabezado**
- nota: p. 1 (el PDF tiene una sola página): el único texto propio de la unidad, «(COMUNICACIÓN “A” 7584)», es el tercer renglón del recuadro de encabezado (título del TO); «Preámbulo» no está en el PDF. Antes de «1. Sujetos alcanzados» no hay texto de norma. Mismo patrón que la fila 59.

Texto propio de la unidad (de la ficha):

```text
Preámbulo
(COMUNICACIÓN “A” 7584)
```

### ri_icpipsp::A1C3::S2

- ficha 77 de `fichas_lectura_S1-bis-b.md` (primer grupo); grupo G1-sin_raiz; TO ri_icpipsp; páginas 11,12
- imagen: `paginas_S1-bis-b/ri_icpipsp_p11.png`, `paginas_S1-bis-b/ri_icpipsp_p12.png`
- marca de la mesa: **error · limpieza · restos_encabezado**
- nota: p. 12: entre el ítem (iv) (fin de la p. 11) y el (v) la unidad trae «Requerimiento normativo Procedimiento aplicado» y «PROCEDIMIENTOS ANUALES», que son el encabezado de columnas y el rótulo que se repiten arriba de cada página de la tabla (pp. 10, 11 y 12). Los cortes (empieza en «2. Servicio de atención…», p. 11; termina en el ítem (vii), p. 12) están bien.

Texto propio de la unidad (de la ficha):

```text
2. Servicio de atención al usuario de servicios financie- (i) Verificar que el Directorio de la Sociedad haya
ros designado a un funcionario como responsable de
atención al usuario de servicios financieros en ca-
rácter de titular y por lo menos otro como suplente
según lo prescripto en el punto 3.1.1. “Responsa-
ble de atención al usuario de servicios financieros
(titular o suplente a cargo)” de las normas sobre
de “Protección de usuarios de servicios financie-
ros”.
(ii) Verificar que se hayan habilitado y se mantengan
actualizados (a) el Registro Centralizado de Con-
sultas y Reclamos (RCCR) a que se refiere el pun-
to 3.1.3. “Registro Centralizado de Consultas y
Reclamos (RCCR)”; (b) el Registro de Reintegros
de Importes (RRI) previsto en el punto 3.1.4. “Re-
gistro de Reintegros de Importes (RRI)”; y (c) el
Registro de Denuncias ante Instancias Judiciales
y/o Administrativas de Defensa del Consumidor
(RDJA) establecido en el punto 3.1.5. “Registro de
Denuncias ante las Instancias Judiciales y/o Ad-
ministrativas de Defensa del Consumidor (RDJA)”
de las normas sobre “Protección de usuarios de
servicios financieros”.
(iii) Constatar que se elabore y eleve al Directorio o
autoridad equivalente, con periodicidad como mí-
nimo trimestral, un reporte acerca de: (i) las con-
sultas y reclamos recibidos; (ii) las intervenciones
requeridas por denuncias tramitadas ante las ins-
tancias judiciales y/o administrativas de defensa
del consumidor que resulten competentes y (iii) los
reintegros de importes realizados, en cumplimien-
to de lo establecido en el punto 3.1.1.8. de las
normas sobre “Protección de usuarios de servicios
financieros”.
(iv) Verificar que el Directorio haya aprobado, previa
toma de conocimiento del Comité de Auditoría [pa-
ra el caso en que la Sociedad cuente con un Co-
mité de Auditoría], los pasos y recaudos a obser-
var para la atención de consultas y reclamos de
usuarios según lo establecido en el punto 3.1.2
“Manual de Procedimiento” de las normas sobre
“Protección de usuarios de servicios financieros”.
Requerimiento normativo Procedimiento aplicado
PROCEDIMIENTOS ANUALES
(v) Constatar que las normas y procedimientos esta-
blecidos por la Sociedad prevean las distintas al-
ternativas de presentaciones de consultas y re-
clamos de los usuarios de servicios financieros tal
lo previsto en el punto 3.1.6. “Recepción de las
presentaciones y tiempo de respuestas” de las
normas sobre “Protección de usuarios de servicios
financieros”, y en el punto 3.2.2. acerca de los
controles de los usuarios de los usuarios de servi-
cios financieros, y
(vi) Verificar que la Auditoría Interna de la Sociedad
complete al menos anualmente una evaluación in-
tegral de los procesos implementados a efectos
de dar cumplimiento a las normas sobre “Protec-
ción de usuarios de servicios financieros” [en caso
deque la Sociedad no cuente con un área de Audi-
toría Interna, el contador público independiente
deberá evaluar los controles del punto 3.2.1.3. no
comprendidos en las otras verificaciones prevista
en el presente informe.
(vii) Verificar que los datos de los responsables sean
publicados en la página web y plataforma de los
“Proveedores de servicio de pago”
```

### ri2_ae::S2::chapeau_seccion

- ficha 85 de `fichas_lectura_S1-bis-b.md` (primer grupo); grupo G1-sin_raiz; TO ri2_ae; páginas 5
- imagen: `paginas_S1-bis-b/ri2_ae_p5.png`
- marca de la mesa: **error · corte · empieza_fuera**
- nota: p. 5 (Página 3 del anexo I): el título de la sección ocupa dos renglones, «2. Condiciones para el ejercicio de la función, inscripción y permanencia en el "Registro» / «de Auditores":». La unidad (chapeau de la sección) es solo el segundo renglón del título, «de Auditores":»: empieza en medio del título y no cubre ningún párrafo, porque entre el título y «2.1.» no hay texto. La herencia del encabezado queda cortada en «el "Registro».

Texto propio de la unidad (de la ficha):

```text
de Auditores":
```

## 2. Juicios dudosos

Ninguno: los 9 juicios leídos quedaron como correctos (ri_pspii y ri_tii venían decididos y no se tocaron).

## 3. Correctas sorteadas del primer grupo y de ri_spi

### snp_psp::4.5.6

- ficha 9 de `fichas_lectura_S1-bis-b.md` (primer grupo); grupo G1-vigente; TO snp_psp; páginas 16
- imagen: `paginas_S1-bis-b/snp_psp_p16.png`
- marca de la mesa: **correcta**

### pagjub::2.7.5

- ficha 15 de `fichas_lectura_S1-bis-b.md` (primer grupo); grupo G1-vigente; TO pagjub; páginas 9
- imagen: `paginas_S1-bis-b/pagjub_p9.png`
- marca de la mesa: **correcta**

### snp_cheq::8.4.2.5

- ficha 23 de `fichas_lectura_S1-bis-b.md` (primer grupo); grupo G1-vigente; TO snp_cheq; páginas 149
- imagen: `paginas_S1-bis-b/snp_cheq_p149.png`
- marca de la mesa: **correcta**

### garant::3.1.11

- ficha 30 de `fichas_lectura_S1-bis-b.md` (primer grupo); grupo G1-vigente; TO garant; páginas 14
- imagen: `paginas_S1-bis-b/garant_p14.png`
- marca de la mesa: **correcta**

### snp_cheq::8.4.1.11

- ficha 33 de `fichas_lectura_S1-bis-b.md` (primer grupo); grupo G1-vigente; TO snp_cheq; páginas 147
- imagen: `paginas_S1-bis-b/snp_cheq_p147.png`
- marca de la mesa: **correcta**

### snp_spd::8.1.1.4

- ficha 37 de `fichas_lectura_S1-bis-b.md` (primer grupo); grupo G1-vigente; TO snp_spd; páginas 23
- imagen: `paginas_S1-bis-b/snp_spd_p23.png`
- marca de la mesa: **correcta**

### gerc::4.3.2

- ficha 38 de `fichas_lectura_S1-bis-b.md` (primer grupo); grupo G1-vigente; TO gerc; páginas 33,34
- imagen: `paginas_S1-bis-b/gerc_p33.png`, `paginas_S1-bis-b/gerc_p34.png`
- marca de la mesa: **correcta**
- nota: Observación fuera del criterio de corte: en la serialización de la tabla (p. 34) la primera fila («Por operaciones de negociación…» / «Se deberán utilizar las medidas…») queda fundida con los rótulos de columna; el texto está completo.

### ri_dcpc::3.6.5

- ficha 42 de `fichas_lectura_S1-bis-b.md` (primer grupo); grupo G1-marcadores; TO ri_dcpc; páginas 22
- imagen: `paginas_S1-bis-b/ri_dcpc_p22.png`
- marca de la mesa: **correcta**

### seguef::6.5.15

- ficha 43 de `fichas_lectura_S1-bis-b.md` (primer grupo); grupo G1-marcadores; TO seguef; páginas 17
- imagen: `paginas_S1-bis-b/seguef_p17.png`
- marca de la mesa: **correcta**

### ri_dcpc::3.2.2.1

- ficha 44 de `fichas_lectura_S1-bis-b.md` (primer grupo); grupo G1-marcadores; TO ri_dcpc; páginas 13,14
- imagen: `paginas_S1-bis-b/ri_dcpc_p13.png`, `paginas_S1-bis-b/ri_dcpc_p14.png`
- marca de la mesa: **correcta**

### seguef::2.3.2

- ficha 48 de `fichas_lectura_S1-bis-b.md` (primer grupo); grupo G1-marcadores; TO seguef; páginas 5
- imagen: `paginas_S1-bis-b/seguef_p5.png`
- marca de la mesa: **correcta**

### seguef::1.4

- ficha 50 de `fichas_lectura_S1-bis-b.md` (primer grupo); grupo G1-marcadores; TO seguef; páginas 3
- imagen: `paginas_S1-bis-b/seguef_p3.png`
- marca de la mesa: **correcta**

### seggar::S2

- ficha 52 de `fichas_lectura_S1-bis-b.md` (primer grupo); grupo G1-sin_raiz; TO seggar; páginas 3
- imagen: `paginas_S1-bis-b/seggar_p3.png`
- marca de la mesa: **correcta**

### nmaeef::S9

- ficha 53 de `fichas_lectura_S1-bis-b.md` (primer grupo); grupo G1-sin_raiz; TO nmaeef; páginas 11
- imagen: `paginas_S1-bis-b/nmaeef_p11.png`
- marca de la mesa: **correcta**

### ri_oc::B.3.1

- ficha 55 de `fichas_lectura_S1-bis-b.md` (primer grupo); grupo G1-sin_raiz; TO ri_oc; páginas 17
- imagen: `paginas_S1-bis-b/ri_oc_p17.png`
- marca de la mesa: **correcta**

### ri_mmsef::2.2.8.3.5

- ficha 64 de `fichas_lectura_S1-bis-b.md` (primer grupo); grupo G1-sin_raiz; TO ri_mmsef; páginas 4
- imagen: `paginas_S1-bis-b/ri_mmsef_p4.png`
- marca de la mesa: **correcta**

### ri_secoexpo::S16

- ficha 69 de `fichas_lectura_S1-bis-b.md` (primer grupo); grupo G1-sin_raiz; TO ri_secoexpo; páginas 3
- imagen: `paginas_S1-bis-b/ri_secoexpo_p3.png`
- marca de la mesa: **correcta**

### ri_mmsef::2.3.5.2

- ficha 81 de `fichas_lectura_S1-bis-b.md` (primer grupo); grupo G1-sin_raiz; TO ri_mmsef; páginas 6
- imagen: `paginas_S1-bis-b/ri_mmsef_p6.png`
- marca de la mesa: **correcta**

### seggar::S3::cierre

- ficha 82 de `fichas_lectura_S1-bis-b.md` (primer grupo); grupo G1-sin_raiz; TO seggar; páginas 4
- imagen: `paginas_S1-bis-b/seggar_p4.png`
- marca de la mesa: **correcta**

### ri_spi::C.1.2

- ficha 94 de `fichas_lectura_S1-bis-b.md` (primer grupo); grupo ri_spi; TO ri_spi; páginas 9
- imagen: `paginas_S1-bis-b/ri_spi_p9.png`
- marca de la mesa: **correcta**

## 4. Censo del 1.16: marcados y dudosos

### cajasc::11.4.4

- ficha 9 de `fichas_lectura_S1-bis-b.md` (censo del 1.16); grupo C116-tanda1; TO cajasc; páginas 61
- imagen: `paginas_S1-bis-b/cajasc_p61.png`
- marca de la mesa: **error · corte · termina_fuera + trae_texto_de_otro_punto**
- nota: p. 61: «Ello, sin perjuicio de lo que se haya establecido en forma específica en las restantes secciones de estas normas.» está al margen de los rótulos 11.4.1 a 11.4.4 (sangría del cuerpo de 11.4), no en la del texto de 11.4.4, y se refiere a toda la lista de operaciones no admitidas: es el cierre de 11.4.

Texto propio de la unidad (de la ficha):

```text
11.4.4. Garantías por intermediación en operaciones entre terceros.
Ello, sin perjuicio de lo que se haya establecido en forma específica en las restantes seccio-
nes de estas normas.
```

### cajasc::4.2.2.3

- ficha 10 de `fichas_lectura_S1-bis-b.md` (censo del 1.16); grupo C116-tanda1; TO cajasc; páginas 23
- imagen: `paginas_S1-bis-b/cajasc_p23.png`
- marca de la mesa: **error · corte · termina_fuera + trae_texto_de_otro_punto**
- nota: p. 23: «La vida promedio se computará…» está en la sangría de los acápites i) a iii) y es de 4.2.2.3; pero el último párrafo, «Los préstamos a que se refieren los puntos 4.2.2.1. y 4.2.2.3. podrán ser desembolsados en efectivo.», está al margen de los rótulos 4.2.2.x (sangría del cuerpo de 4.2.2) y nombra dos ítems: es el cierre de 4.2.2.

Texto propio de la unidad (de la ficha):

```text
4.2.2.3. Otros préstamos:
i) Hipotecarios: hasta 96 meses de vida promedio.
ii) Comerciales: hasta 60 meses de vida promedio.
iii) Otros: hasta 36 meses de vida promedio.
La vida promedio se computará al momento del otorgamiento de cada préstamo
y resultará del promedio ponderado del plazo de cada amortización a efectuar-
se ponderada por la proporción que el importe de la misma represente respecto
al importe total del préstamo.
Los préstamos a que se refieren los puntos 4.2.2.1. y 4.2.2.3. podrán ser des-
embolsados en efectivo.
```

### depaho::3.11.5.5

- ficha 16 de `fichas_lectura_S1-bis-b.md` (censo del 1.16); grupo C116-tanda1; TO depaho; páginas 52
- imagen: `paginas_S1-bis-b/depaho_p52.png`
- marca de la mesa: **error · corte · termina_fuera + trae_texto_de_otro_punto**
- nota: p. 52: «Los movimientos –cualquiera sea su naturaleza– no podrán generar saldo deudor.» está al margen de los rótulos 3.11.5.x (sangría del cuerpo de 3.11.5), no en la del texto de 3.11.5.5, y vale para todos los medios de extracción: es el cierre de 3.11.5.

Texto propio de la unidad (de la ficha):

```text
3.11.5.5. Transferencias efectuadas a través de medios electrónicos –ej.: cajero
automático o banca por Internet (home banking)–.
Los movimientos –cualquiera sea su naturaleza– no podrán generar saldo deudor.
```

### manori::1.4.1.3

- ficha 30 de `fichas_lectura_S1-bis-b.md` (censo del 1.16); grupo C116-tanda1; TO manori; páginas 30
- imagen: `paginas_S1-bis-b/manori_p30.png`
- marca de la mesa: **error · corte · termina_fuera + trae_texto_de_otro_punto**
- nota: p. 30: «La entidad financiera deberá desarrollar documentación respaldatoria de las bases de datos…» está al margen de los rótulos 1.4.1.1 a 1.4.1.3 (sangría del cuerpo de 1.4.1), no en la del texto de 1.4.1.3: es el cierre de 1.4.1.

Texto propio de la unidad (de la ficha):

```text
1.4.1.3. Cada entidad financiera podrá desarrollar su base de datos en la forma que
estime más conveniente siempre que se cumpla con los requisitos establecidos
en esta sección. Los campos que se detallan en el punto 1.4.2. como Informa-
ción de cuotas, más los campos que figuran en los formularios establecidos en
el punto 1.5., son los que mínimamente deben contener dichas bases, pudiendo
cada entidad financiera agregar aquellos que estime conveniente.
La entidad financiera deberá desarrollar documentación respaldatoria de las bases de
datos, incluyendo las definiciones de cada campo y de los códigos utilizados.
```

### manori::3.4.1.3

- ficha 31 de `fichas_lectura_S1-bis-b.md` (censo del 1.16); grupo C116-tanda1; TO manori; páginas 78
- imagen: `paginas_S1-bis-b/manori_p78.png`
- marca de la mesa: **error · corte · termina_fuera + trae_texto_de_otro_punto**
- nota: p. 78: «La entidad financiera deberá desarrollar documentación respaldatoria de las bases de datos…» está al margen de los rótulos 3.4.1.1 a 3.4.1.3 (sangría del cuerpo de 3.4.1), no en la del texto de 3.4.1.3: es el cierre de 3.4.1. Mismo caso que el candidato 30.

Texto propio de la unidad (de la ficha):

```text
3.4.1.3. Cada entidad financiera podrá desarrollar su base de datos en la forma que es-
time más conveniente siempre que se cumpla con los requisitos establecidos
en esta Sección. Los campos que se detallan en el punto 3.4.2. como “Informa-
ción de cuotas”, más los campos que figuran en los formularios establecidos en
el punto 3.5. son los que mínimamente deben contener dichas bases, pudiendo
cada entidad financiera agregar aquellos que estime conveniente.
La entidad financiera deberá desarrollar documentación respaldatoria de las bases de
datos, incluyendo las definiciones de cada campo y de los códigos utilizados.
```

### ri_oc::B.1.28

- ficha 32 de `fichas_lectura_S1-bis-b.md` (censo del 1.16); grupo C116-tanda1; TO ri_oc; páginas 16,17
- imagen: `paginas_S1-bis-b/ri_oc_p16.png`, `paginas_S1-bis-b/ri_oc_p17.png`
- marca de la mesa: **error · corte · termina_fuera + trae_texto_de_otro_punto**
- nota: pp. 16-17: la unidad sigue, en la p. 17, con «En el punto B.1.24 deben informarse:», «En el punto B.1.25 deben informarse:» y «La contrapartida de los movimientos… B.1.16. o B.1.17.», que están al margen izquierdo, al nivel del rótulo B.1 (no en la sangría de los ítems B.1.x), y explican otros ítems de la lista: son el cierre de B.1.

Texto propio de la unidad (de la ficha):

```text
B.1.28. Posición General de Cambios al cierre del día.
En el punto B.1.24 deben informarse:
− Los ingresos de fondos en las cuentas de corresponsalía de la entidad correspondientes a
transferencias de terceros, que fueron ingresadas en el día en los registros contables de la
entidad.
En el punto B.1.25 deben informarse:
− Las transferencias de terceros recibidas y contabilizadas en cuentas de corresponsalía, por
las cuales en el día informado se efectuó la concertación de cambio con el cliente, y/o se
procedió a la devolución de la transferencia al emisor de la transferencia, y/o se retransfirió
dentro de las posibilidades contempladas en la normativa cambiaria.
No se incluyen las transferencias por aplicaciones de los fondos de terceros en el marco de
la normativa vigente, que deben ser declaradas en el punto que corresponda.
La contrapartida de los movimientos relacionados con operaciones registradas en el Apartado A que
correspondan a los códigos de conceptos B26, S33, I09, I12, I13 y P28 se deberán informar en los
puntos B.1.16. o B.1.17. del presente Apartado, según corresponda.
```

### ri_oc::C.11

- ficha 33 de `fichas_lectura_S1-bis-b.md` (censo del 1.16); grupo C116-tanda1; TO ri_oc; páginas 18,19
- imagen: `paginas_S1-bis-b/ri_oc_p18.png`, `paginas_S1-bis-b/ri_oc_p19.png`
- marca de la mesa: **error · corte · termina_fuera + trae_texto_de_otro_punto**
- nota: pp. 18-19: la unidad agrega «Criterios de validación» y «Validación del Apartado A – Operaciones de cambios», que son los títulos con que empieza en la p. 19 el bloque de validaciones de los apartados A, B y C, no texto de C.11.

Texto propio de la unidad (de la ficha):

```text
C.11. Posición General de Cambios Total a la fecha de información. (Debe ser consistente con lo
informado en el punto B.1.28. para el último día de cada mes).
Criterios de validación
Validación del Apartado A – Operaciones de cambios
```

### ri_rml::1.2.3

- ficha 34 de `fichas_lectura_S1-bis-b.md` (censo del 1.16); grupo C116-tanda1; TO ri_rml; páginas 3,4,5,6
- imagen: `paginas_S1-bis-b/ri_rml_p3.png`, `paginas_S1-bis-b/ri_rml_p4.png`, `paginas_S1-bis-b/ri_rml_p5.png`, `paginas_S1-bis-b/ri_rml_p6.png`
- marca de la mesa: **error · corte · falta_texto_propio**
- nota: pp. 3-6: el texto de 1.2.3 (los códigos de las pp. 4 a 6, en la sangría del cuerpo, hasta el rótulo 1.2.4 de la p. 6) está en la unidad, pero la unidad se corta a mitad de frase en «…de acuerdo con el procedimiento descripto en el punto» y le faltan sus dos últimos renglones: «1.3. “Integración” de las presentes normas- o 210200/TP -cuando se trate de especies en dólares estadounidenses-.» (p. 6). El renglón empieza con «1.3.» dentro del párrafo. No es el patrón del hallazgo: el párrafo del cierre candidato está en la sangría del texto de 1.2.3.

Texto propio de la unidad (de la ficha):

```text
1.2.3. Conceptos comprendidos
El código 100000/M incluirá los depósitos y obligaciones por intermediación financiera a
la vista y a plazo en pesos y moneda extranjera, de acuerdo con los términos de la Sec-
ción 1. de las normas sobre “Efectivo mínimo”.
El código 300000/TP incluirá los depósitos a plazo fijo de títulos públicos nacionales o
instrumentos de regulación monetaria del BCRA teniendo en cuenta lo establecido en
las normas citadas.
Se informará un subcódigo por cada moneda o instrumento de deuda en que se en-
cuentren denominadas las obligaciones considerando las disposiciones del punto 1.1.
Los depósitos y obligaciones a plazo se informarán teniendo en cuenta sus plazos resi-
duales.
Plazos residuales
Los depósitos y obligaciones a plazo se clasificarán según los tramos de plazos residua-
les establecidos. Para ello, se tendrá en cuenta lo siguiente:
[TABLA ri_rml::tabla000 | página 3 | e0_tablas | posicional]
Fila 1: col1 = Pesos | col2 = Moneda extranjera
Fila 2: col1 = x = 1 a 5, donde: | col2 = x = 1 a 6, donde:
Fila 3: col1 = 1= Hasta 29 días | col2 = 1= Hasta 29 días
Fila 4: col1 = 2= 30 - 59 días | col2 = 2= 30 - 59 días
Fila 5: col1 = 3= 60 - 89 días | col2 = 3= 60 - 89 días
Fila 6: col1 = 4= 90 - 179 días | col2 = 4= 90 - 179 días
Fila 7: col1 = 5= 180 días o más | col2 = 5= 180 a 365 días
Fila 8: col2 = 6= más de 365 días.
[FIN TABLA ri_rml::tabla000]
Dichos plazos se calcularán computando la cantidad de días que restan hasta el venci-
miento de las obligaciones, contados desde cada uno de los días del mes, determinan-
do finalmente el promedio de las aludidas obligaciones así desagregadas.
Cuando se trate de plazo fijos en moneda extranjera (partida 10140X/M) se aplicará la
estructura de plazos residuales del mes anterior (n - 1).
En consecuencia, se efectuarán los siguientes cálculos:
Se sumarán los tramos de plazos informados en la posición del mes anterior (n-1) y se
determinarán los porcentajes de cada tramo sobre el total.
Se sumarán los tramos de plazos informados en la posición del mes bajo informe (n) y
se le aplicarán los porcentajes determinados en el mes anterior (n-1).
Dicho procedimiento se aplicará considerando en forma conjunta los depósitos a plazo
fijo (códigos 10140X/M, donde M = moneda extranjera).
Para los plazos fijos y para las restantes operaciones a plazo en pesos, se considerarán
para el cálculo de la exigencia del mes bajo informe, los tramos de plazos y promedios
informados en el periodo anterior y las tasas del periodo bajo informe.
Código 10141X/M
En el caso de extensión automática de plazo, se considerará en forma constante el plazo ex-
tendido (180 días o más, según lo pactado). Si el cliente opta por la revocación de la exten-
sión, se computará el plazo remanente hasta el vencimiento.
Código 101490/001
Se incluirán las inversiones a plazo instrumentadas en certificados nominativos intransferibles,
en pesos, correspondientes a titulares del sector público que cuenten con el derecho a ejercer
la opción de cancelación anticipada en un plazo inferior a 30 días contados desde su constitu-
ción.
Código 10145X/M
Se consignarán las obligaciones por líneas financieras del exterior instrumentadas me-
diante depósitos a plazo o adquisición de títulos valores de deuda de personas vincula-
das -punto 1.2.2. del TO sobre Grandes Exposiciones al Riesgo de Crédito- a las cuales
les corresponde la exigencia prevista en el punto 1.3.5. de las normas sobre “Efectivo
mínimo”.
Código 10171X/001
Se incluirá el importe de los depósitos reprogramados “CEDROS” y el correspondiente CER
devengado. Los plazos residuales de cada servicio de amortización se determinarán en forma
independiente.
Código 10180X/M
Se incluirán Títulos Valores de Deuda, comprendiendo las obligaciones negociables y las obli-
gaciones reestructuradas, a excepción de los saldos que corresponda imputar en la partida
10166X/001.
Los plazos residuales de las obligaciones de pago en cuotas de capital se computarán en for-
ma independiente para cada servicio de amortización con vencimiento dentro del año, contado
desde cada uno de los días de la posición al que corresponde el efectivo mínimo.
Código 10190X/001
Se informarán las cauciones bursátiles tomadoras -pasivas- en pesos, de acuerdo con lo previs-
to en el punto 1.3.13. de las normas sobre “Efectivo mínimo”.
Código 10206X/M
Se informará las obligaciones por líneas financieras del exterior no instrumentadas me-
diante depósitos a plazo o adquisición de títulos valores de deuda, de personas vincula-
das, -punto 1.2.2. del TO sobre Grandes Exposiciones al Riesgo de Crédito- a las cuales
les corresponde la exigencia prevista en el punto 1.3.6. de las normas sobre “Efectivo
mínimo”.
Las obligaciones originadas en líneas financieras del exterior que reúnan los requisitos
previstos en el punto 1.3.6., formalizadas hasta el 5/2 se informarán en la partida
102062/M, mientras que las formalizadas a partir del 6/2, se informarán en las partidas
102061/M y/ó 102062/M, según el plazo que corresponda.
Código 102100/M
Se consignarán los saldos sin utilizar de adelantos en cuenta corriente que correspondan a
acuerdos formalizados que no contengan cláusulas que habiliten a la entidad a disponer discre-
cional y unilateralmente la anulación de la posibilidad de uso de dichos márgenes.
Código 102150/M
Los bancos comerciales informarán el total de depósitos a la orden de entidades financieras no
bancarias.
Código 102090/010
Se incluirán las obligaciones a la vista por transferencias del exterior pendientes de liquidación
que excedan las 72 hs. hábiles de la fecha de su acreditación.
Códigos 101500/M, 102160/M y 300700/TP
Se informarán las obligaciones respecto de las cuales se hayan dispuesto aumentos puntuales
de exigencia por concentración de pasivos. Para su cómputo debe aplicarse la siguiente metodo-
logía:
a) En los códigos previstos para los depósitos (a la vista y a plazo) y otras obligaciones se regis-
trará el promedio mensual de saldos diarios incluyendo los depósitos que verifiquen una con-
centración excesiva de pasivos (en titulares y/o plazos), sobre los que se calculará la tasa de
efectivo mínimo normal para el período considerado.
b) En los códigos 101500/M, 102160/M y 300700/TP se consignará el promedio mensual de sal-
dos diarios de los depósitos y otras obligaciones que verifiquen alguno de los factores des-
criptos en el punto 1.6. de las normas sobre “Efectivo mínimo”. La exigencia a aplicar será la
que resulte de la diferencia entre la determinada para estas obligaciones y la normal calcula-
da según el apartado a). La entidad informará esas partidas con la exigencia incremental ya
calculada, con lo cual se considerará de esa manera para el cálculo de la exigencia total del
período.
Códigos 10160X/001 a 101650/001
- Códigos 10160X/001 y 10163X/001: se consignarán los importes correspondientes a las im-
posiciones en “UVA” y “UVI”, según corresponda, expresados en pesos en función del valor
de esas unidades calculado conforme lo establecido en el punto 1.9. de las normas sobre
“Depósitos e inversiones a plazo”.
- Código 10161X/001: inversiones a plazo de “UVA” para las modalidades previstas en los pun-
tos 2.2. a 2.5. de las normas sobre “Depósitos e inversiones a plazo”;
- Códigos 10162X/001 y 10164X/001: cuentas de ahorro en “UVA” y “UVI”, respectivamente,
según lo previsto en los puntos 2.6. y 2.7. de las citadas normas;
- Código 101650/001: depósitos a plazo fijo e inversiones a nombre de menores de edad por
fondos que reciban a título gratuito.
Código 10166X/001
Se informarán las colocaciones de títulos de deuda (incluidas las obligaciones negociables) cu-
yos instrumentos se encuentren denominados en Unidades de Vivienda actualizables por “ICC” -
Ley 27.271 (“UVI”) o en Unidades de Valor Adquisitivo actualizables por “CER” - Ley 25.827
(“UVA”).
Código 102400/M
Se informará el importe del defecto de aplicación de la capacidad prestable correspondiente a
los depósitos en moneda extranjera, determinado en el código 400/M.
Códigos 10120X/M, 11010X/M y 110500/M
Identificarán los depósitos a plazo fijo de títulos privados y públicos (excepto nacionales) y sus
saldos inmovilizados según lo previsto en las normas sobre “Efectivo mínimo”. Se admitirá su in-
tegración total o parcial con títulos públicos nacionales con cotización normal y habitual por im-
portes significativos en mercados del país; dicha aplicación se informará en el código 210100/TP
-cuando se trate de especies en pesos, de acuerdo con el procedimiento descripto en el punto
```

## 5. Censo del 1.16: correctos sorteados

### depaho::3.6.2.4

- ficha 19 de `fichas_lectura_S1-bis-b.md` (censo del 1.16); grupo C116-tanda1; TO depaho; páginas 39
- imagen: `paginas_S1-bis-b/depaho_p39.png`
- marca de la mesa: **correcta**
- nota: p. 39: el texto está bajo el rótulo «3.6.2.4. Otras monedas.», en su sangría; después viene 3.6.3.

### lingeef::10.3.2

- ficha 22 de `fichas_lectura_S1-bis-b.md` (censo del 1.16); grupo C116-tanda1; TO lingeef; páginas 149
- imagen: `paginas_S1-bis-b/lingeef_p149.png`
- marca de la mesa: **correcta**
- nota: p. 149: «Los resultados de las pruebas de estrés deben contribuir…» está en la sangría del texto de 10.3.2; después viene 10.4.

### lingeef::5.1.1.3

- ficha 25 de `fichas_lectura_S1-bis-b.md` (censo del 1.16); grupo C116-tanda1; TO lingeef; páginas 83,84
- imagen: `paginas_S1-bis-b/lingeef_p83.png`, `paginas_S1-bis-b/lingeef_p84.png`
- marca de la mesa: **correcta**
- nota: p. 84: «El riesgo de opción puede a su vez desglosarse en:» y los acápites i) y ii) están en la sangría del texto de 5.1.1.3; «Los tres subtipos de RTICI…», al margen de los rótulos, no está en la unidad (es el cierre de 5.1.1).

### lingeef::6.2.1.9

- ficha 28 de `fichas_lectura_S1-bis-b.md` (censo del 1.16); grupo C116-tanda1; TO lingeef; páginas 122,123
- imagen: `paginas_S1-bis-b/lingeef_p122.png`, `paginas_S1-bis-b/lingeef_p123.png`
- marca de la mesa: **correcta**
- nota: pp. 122-123: los párrafos y los acápites i) a v) están en la sangría del texto de 6.2.1.9; la unidad termina antes de 6.2.1.10. Observación fuera de esta unidad: en la herencia, 6.2.1.10 figura como cierre de 6.2.1 («6 2 1 10. Supervisar…»), aunque en la p. 123 es un punto numerado más de la lista.

### snp_tr::4.2

- ficha 35 de `fichas_lectura_S1-bis-b.md` (censo del 1.16); grupo C116-tanda1; TO snp_tr; páginas 55
- imagen: `paginas_S1-bis-b/snp_tr_p55.png`
- marca de la mesa: **correcta**
- nota: p. 55: «En línea con lo indicado en el párrafo anterior…» y sus guiones están en la sangría del texto de 4.2; la sección termina ahí.
