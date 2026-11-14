# Examen II Parcial - Programación de Negocios

**Estudiante:** José Fúnez  
**Número de cuenta:** 1709200400244  
**Universidad:** UNICAH  
**Versión:** Odoo 20.0

> Importante: este proyecto es una base de código preparada para instalarse y probarse en la instalación local de Odoo. No incluye capturas de funcionamiento reales; deben obtenerse del entorno del estudiante.

## Estructura

- `tienda_unicah/`: partes 1 a 5. Extiende Contactos y Ventas con tipos de cliente, convenios de descuento, validaciones y cálculo de ahorro.
- `unicah_prestamos/`: parte 6. Registro de préstamos de equipos informáticos universitarios, herencia de contactos y validación de fechas.
- `GUIA_INSTALACION.md`: instalación paso a paso con Docker y comandos Git.
- `PRUEBAS_Y_CAPTURAS.md`: casos de prueba de las seis partes.
- `JUSTIFICACION_EXAMEN.md`: respuestas y propuesta para convertir a PDF tras pegar las capturas reales.

## Dependencias

- Odoo 20.0.
- `sale_management` para `tienda_unicah`.
- `contacts` para `unicah_prestamos`.

## Instalación

Ver `GUIA_INSTALACION.md`. No agregar contraseñas, bases de datos ni credenciales al repositorio.
