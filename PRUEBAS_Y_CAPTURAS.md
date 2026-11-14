# Plan de comprobación y capturas de pantalla

Toma una captura por parte, con datos legibles y la pantalla de Odoo visible. El docente pide resultados reales.

## Parte 1 (10 pts)
- Crear contacto **Estudiante de prueba**: tipo **Estudiante**, cuenta **0801200012** (10 dígitos), carrera **Ingeniería en Sistemas**.
- Crear otro contacto **Docente de prueba**: tipo **Docente**.
- Resultado esperado: en **UNICAH** solo el estudiante ve cuenta y carrera.
- **Captura 1:** pestaña UNICAH del estudiante, idealmente otra captura adicional del docente.

## Parte 2 (10 pts)
- En **Ventas > Configuración > Convenios UNICAH** deben verse **Convenio estudiantil** 15 % y **Convenio docente** 10 %.
- Crear **Convenio administrativo**, tipo Administrativo, descuento 8 %, fecha desde hoy.
- **Captura 2:** lista de tres convenios.

## Parte 3 (10 pts)
- Activar **Descuentos** en configuración de Ventas.
- Crear cotización para el estudiante de prueba, incluir **una sección** y **dos productos** con cantidades que sumen hasta 10.
- Pulsar **Aplicar convenio**.
- Resultado esperado: los productos tienen 15 %, la sección no tiene descuento, el chatter indica aplicación.
- **Captura 3:** pedido con columnas descuento y mensaje de chatter.

## Parte 4 (10 pts)
- Probar número de cuenta de 8 cifras (error), convenio 50 % (error), convenio con fin anterior al inicio (error), estudiante con 12 unidades (error) y docente con 12 unidades (permite confirmar).
- **Captura 4:** al menos uno de los mensajes de error; conviene anexar los demás como evidencia adicional.

## Parte 5 (10 pts)
- En ventas, comprobar campo **Ahorro por convenio**: dos artículos de precio 100 y 200, ambos con cantidad 1 y descuento 15 %, generan ahorro de 45 (moneda de la compañía).
- La lista debe mostrar **Convenio**, **Ahorro por convenio** y suma al pie.
- Probar filtro **Con convenio** y agrupar **Por convenio**.
- **Captura 5:** listado filtrado/agrupado con columna ahorro.

## Parte 6 (10 pts)
- En **Préstamos UNICAH > Préstamos de equipos**, crear: Referencia **PREST-001**, solicitante Estudiante de prueba, código **LAP-001**, descripción **Laptop biblioteca**, fecha inicial 2026-11-10, final 2026-11-13, estado **Devuelto**.
- Resultado esperado: el campo **Días de préstamo** muestra **3**.
- Probar fecha final anterior a la inicial (error) y marcado Devuelto sin fecha final (error).
- En contacto estudiante revisar la pestaña **Préstamos UNICAH** y su conteo.
- **Captura 6:** préstamo completo con el valor calculado. Otra captura opcional de contacto heredado.

Al guardar una captura, usa nombres como `01_contacto_unicah.png` hasta `06_prestamo_equipo.png`. No usar capturas de ejemplo ni simular resultados.
