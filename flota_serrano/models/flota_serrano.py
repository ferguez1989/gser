from odoo import fields, models, api
class FlotaSerrano(models.Model):
    _inherit = "sale.order"
    marca = fields.Char(string="Marca",)
    modelo = fields.Char(string="Modelo",)
    km = fields.Float(string="Kilometraje")
    rendimiento = fields.Float(default=2.2,string="Rendimiento",)
    disel = fields.Float(compute='_compute_disel',)

    @api.depends("km", "rendimiento")
    def _compute_disel(self):
        for record in self:
            record.disel = record.km / record.rendimiento
    
    conductor = fields.Many2one(
        comodel_name='hr.employee',
        ondelete='set null',
        index=True,
    )