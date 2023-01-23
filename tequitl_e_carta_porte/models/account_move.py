from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    carta_porte_picking_id = fields.Many2one(
        comodel_name="stock.picking",
        string="Carta Porte",
        readonly=True,
        states={"draft": [("readonly", False)]},
        domain="[('l10n_mx_edi_status', 'in', (False, 'cancelled'))]",
    )

    def _l10n_mx_edi_get_cadena_xslts(self):
        res = super()._l10n_mx_edi_get_cadena_xslts()
        cadena_original_carta_porte = self.env["stock.picking"]._l10n_mx_edi_get_cadena_xslt()
        return res[0], cadena_original_carta_porte
