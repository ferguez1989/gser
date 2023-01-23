from odoo import _, api, fields, models
from odoo.exceptions import UserError


class StockPicking(models.Model):
    _inherit = "stock.picking"

    invoice_carta_porte_id = fields.Many2one(
        comodel_name="account.move",
        readonly=True,
    )

    def l10n_mx_edi_action_send_delivery(self):
        self.ensure_one()
        if self.invoice_carta_porte_id:
            raise UserError(
                _(
                    "This picking is used as a Carta Porte in the invoice %s. Please, send the invoice instead."
                )
                % self.invoice_carta_porte_id.name
            )
        return self.l10n_mx_edi_action_send_delivery()
