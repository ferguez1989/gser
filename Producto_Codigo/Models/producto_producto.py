from odoo import fields, models

class Producto(models.Model):
    _inherit = "product.template"

    id_mkt = fields.Char(String="ID Market Place")