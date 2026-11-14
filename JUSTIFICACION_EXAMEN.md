# Justificación - Examen II Parcial de Programación de Negocios

**Estudiante:** José Fúnez  
**Número de cuenta:** 17009200400244  

> Inserta una captura REAL por cada parte antes de exportar a PDF; este documento describe lo desarrollado pero aún no prueba su funcionamiento.

## Parte 1. Datos universitarios del cliente

Se hereda `res.partner` para incorporar tipo de cliente, número de cuenta y carrera. La pestaña UNICAH permite identificar convenios sin duplicar la información de contactos. Número de cuenta y carrera aparecen solo para estudiantes.

**Evidencia:** [INSERTAR CAPTURA 1: CONTACTO ESTUDIANTE Y PESTAÑA UNICAH]

## Parte 2. Modelo de convenios

El nuevo modelo `tienda.convenio` guarda nombre, tipo de cliente, porcentaje, fechas y estado. Incluye permisos de lectura para vendedores y gestión completa para administradores, dos registros iniciales y acceso desde Ventas > Configuración.

**Pregunta: ¿Qué diferencia hay entre `_name` y `_inherit`?** `_name` define un modelo nuevo con su propia estructura; `_inherit` extiende un modelo existente cuando se usa sin `_name`.

**Pregunta: ¿Por qué `tienda.convenio` necesita `ir.access.csv` y `res.partner` no?** `tienda.convenio` es un modelo nuevo y necesita reglas explícitas de acceso. `res.partner` ya cuenta con acceso gestionado por los módulos base; la herencia agrega campos sin crear un modelo independiente.

**Evidencia:** [INSERTAR CAPTURA 2: CONVENIOS INICIALES Y ADMINISTRATIVO]

## Parte 3. Convenio en el pedido

Al seleccionar un cliente, se identifica un convenio activo dentro de sus fechas de vigencia, según el tipo de cliente. El botón aplica el descuento a las líneas de producto y publica un mensaje en el historial.

**Pregunta: ¿Qué aportan `store=True` y `readonly=False` a `convenio_id`?** `store=True` guarda el campo calculado en base de datos, de manera que puede consultarse, filtrarse y agruparse. `readonly=False` deja que el usuario cambie el convenio propuesto antes de aplicarlo.

**Pregunta: ¿Por qué se excluyen líneas con `display_type`?** Son secciones o notas que sirven para organizar la cotización, no productos con precio ni unidades a descontar.

**Evidencia:** [INSERTAR CAPTURA 3: DESCUENTO DE PRODUCTOS Y CHATTER]

## Parte 4. Validaciones

Se agrega una cuenta de exactamente 10 dígitos para estudiantes, descuentos mayores que cero y hasta 40 %, orden cronológico de fechas del convenio y límite máximo de 10 unidades por pedido estudiantil.

**Pregunta: Si la vista ya usa `required`, ¿por qué validar también en Python?** `required` en la vista actúa en esa interfaz, pero las operaciones desde importación, API, automatizaciones u otras vistas pueden no cumplirla. Python verifica reglas del lado servidor.

**Pregunta: ¿Qué pasaría si `action_confirm` no llamara a `super()`?** No se ejecutaría la confirmación estándar de Odoo: la cotización podría quedarse sin pasar correctamente al flujo normal de pedido, entregas y operaciones relacionadas.

**Evidencia:** [INSERTAR CAPTURA 4: MENSAJE DE VALIDACIÓN EN ODOO]

## Parte 5. Ahorro por convenio

Se calcula el ahorro como la suma de precio unitario por cantidad por descuento dividido entre 100 para las líneas de producto. Se presenta en formulario y lista, con total y opciones de filtrar/agrupación.

**Pregunta: ¿Qué campos se pusieron en `@api.depends` y qué pasaría si faltara uno?** Se usan `order_line.price_unit`, `order_line.product_uom_qty`, `order_line.discount` y `order_line.display_type`. Si faltara una dependencia, el cálculo almacenado podría no actualizarse cuando se cambie el campo omitido.

**Evidencia:** [INSERTAR CAPTURA 5: AHORRO EN LISTA Y FILTROS]

## Parte 6. Propuesta propia: préstamos de equipos informáticos

**1. Problema y usuarios.** Los préstamos de laptops, proyectores y otros equipos pueden registrarse manualmente o en hojas de cálculo, dificultando ubicar al responsable, comprobar fechas y conocer si el dispositivo fue devuelto. El personal de biblioteca, laboratorios y tecnología utilizaría el módulo.

**2. ¿Por qué Odoo?** Odoo centraliza estudiantes y docentes en Contactos, tiene permisos, formularios, vistas de lista y trazabilidad de registros. Reduce registros duplicados y permite evolucionar la solución sin crear otra plataforma independiente.

**3. Diseño.** Se crea el modelo `unicah.prestamo.equipo` con referencia, solicitante (`Many2one` a `res.partner`), código y descripción del equipo, fecha de préstamo, fecha de devolución, días de préstamo (campo calculado y almacenado), estado y observaciones. `res.partner` se hereda para mostrar los préstamos y su cantidad. Las reglas impiden devolver con fecha anterior al préstamo y exigir fecha de devolución cuando el estado es Devuelto. Incluye permisos en `security/ir.access.csv`, vistas de lista y formulario, acción y menú.

**4. Funcionamiento.** Registrar un préstamo, seleccionar un contacto existente, indicar el equipo y registrar la devolución; los días se calculan automáticamente como diferencia entre fechas.

**5. Mejoras de una segunda versión.** Registrar el inventario físico como modelo independiente, escanear códigos QR, manejar reservas y disponibilidad, definir responsables por departamento y emitir avisos por retrasos.

**Evidencia:** [INSERTAR CAPTURA 6: PRESTAMO Y DÍAS CALCULADOS]

## Verificación final

Antes de entregar: pegar capturas, completar número de cuenta y GitHub, comprobar cada parte en el entorno real, exportar a PDF y verificar tres o más commits.
