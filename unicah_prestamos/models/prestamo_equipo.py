from odoo import api, fields, models
from odoo.exceptions import ValidationError


class PrestamoEquipo(models.Model):
    _name = "unicah.prestamo.equipo"
    _description = "Préstamo de equipo universitario"
    _order = "fecha_prestamo desc, id desc"

    name = fields.Char(string="Referencia", required=True)
    solicitante_id = fields.Many2one(
        "res.partner", string="Solicitante", required=True, ondelete="restrict"
    )
    codigo_equipo = fields.Char(string="Código del equipo", required=True)
    descripcion_equipo = fields.Char(string="Descripción del equipo", required=True)
    fecha_prestamo = fields.Date(
        string="Fecha de préstamo", required=True,
        default=fields.Date.context_today,
    )
    fecha_devolucion = fields.Date(string="Fecha de devolución")
    dias_prestamo = fields.Integer(
        string="Días de préstamo",
        compute="_compute_dias_prestamo", store=True,
    )
    estado = fields.Selection(
        [("prestado", "Prestado"), ("devuelto", "Devuelto")],
        string="Estado", required=True, default="prestado",
    )
    observaciones = fields.Text(string="Observaciones")

    @api.depends("fecha_prestamo", "fecha_devolucion")
    def _compute_dias_prestamo(self):
        for record in self:
            if record.fecha_prestamo and record.fecha_devolucion:
                record.dias_prestamo = max(
                    (record.fecha_devolucion - record.fecha_prestamo).days, 0
                )
            else:
                record.dias_prestamo = 0

    @api.constrains("fecha_prestamo", "fecha_devolucion", "estado")
    def _check_fechas_y_estado(self):
        for record in self:
            if (
                record.fecha_prestamo and record.fecha_devolucion
                and record.fecha_devolucion < record.fecha_prestamo
            ):
                raise ValidationError(
                    "La fecha de devolución no puede ser anterior al préstamo."
                )
            if record.estado == "devuelto" and not record.fecha_devolucion:
                raise ValidationError(
                    "Para marcar el equipo como devuelto debe ingresar "
                    "la fecha de devolución."
                )
