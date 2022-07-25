from odoo import fields, models


class Product(models.Model):
    _inherit = "product.product"

    id_amazon = fields.Char(string="ID Amazon")
    id_ebay = fields.Char(string="ID Ebay")
