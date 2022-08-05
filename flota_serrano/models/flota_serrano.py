from odoo import fields, models, api
class FlotaSerrano(models.Model):
    _inherit = "sale.order"
    marca = fields.Char(string="Marca",)
    modelo = fields.Char(string="Modelo",)
    km = fields.Float(string="Kilometraje")
    rendimiento = fields.Float(default=2.2,string="Rendimiento",)
