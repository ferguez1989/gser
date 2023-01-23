import base64

from lxml import etree
from odoo import _, models
from odoo.exceptions import UserError


class AccountEdiFormat(models.Model):
    _inherit = "account.edi.format"

    def _l10n_mx_edi_get_invoice_templates(self):
        res = super()._l10n_mx_edi_get_invoice_templates()
        return res

    def _l10n_mx_edi_export_invoice_cfdi(self, invoice):
        # Tequitl: base odoo method
        """Create the CFDI attachment for the invoice passed as parameter.

        :param move:    An account.move record.
        :return:        A dictionary with one of the following key:
        * cfdi_str:     A string of the unsigned cfdi of the invoice.
        * error:        An error if the cfdi was not successfuly generated.
        """

        # == CFDI values ==
        cfdi_values = self._l10n_mx_edi_get_invoice_cfdi_values(invoice)
        qweb_template, xsd_attachment = self._l10n_mx_edi_get_invoice_templates()

        # == Generate the CFDI ==
        cfdi = qweb_template._render(cfdi_values)
        decoded_cfdi_values = invoice._l10n_mx_edi_decode_cfdi(cfdi_data=cfdi)
        cfdi_cadena_crypted = (
            cfdi_values["certificate"].sudo().get_encrypted_cadena(decoded_cfdi_values["cadena"])
        )
        decoded_cfdi_values["cfdi_node"].attrib["Sello"] = cfdi_cadena_crypted

        # == Optional check using the XSD ==
        xsd_datas = base64.b64decode(xsd_attachment.datas) if xsd_attachment else None

        res = {
            "cfdi_str": etree.tostring(
                decoded_cfdi_values["cfdi_node"],
                pretty_print=True,
                xml_declaration=True,
                encoding="UTF-8",
            ),
        }

        # Tequitl: Remove XSD validation
        # if xsd_datas:
        #     try:
        #         with BytesIO(xsd_datas) as xsd:
        #             _check_with_xsd(decoded_cfdi_values["cfdi_node"], xsd)
        #     except (IOError, ValueError):
        #         _logger.info(_("The xsd file to validate the XML structure was not found"))
        #     except Exception as e:
        #         res["errors"] = str(e).split("\\n")

        return res

    def _vals_to_use_in_carta_porte(self, invoice):
        carta_porte_picking_id = invoice.carta_porte_picking_id
        mx_tz = self.env["account.move"]._l10n_mx_edi_get_cfdi_partner_timezone(
            carta_porte_picking_id.picking_type_id.warehouse_id.partner_id
            or carta_porte_picking_id.company_id.partner_id
        )
        date_fmt = "%Y-%m-%dT%H:%M:%S"
        return {
            "cfdi_date": carta_porte_picking_id.date_done.astimezone(mx_tz).strftime(date_fmt),
            "scheduled_date": carta_porte_picking_id.scheduled_date.astimezone(mx_tz).strftime(
                date_fmt
            ),
            "supplier": invoice.company_id,
            "customer": invoice.partner_id.commercial_partner_id,
            "moves": carta_porte_picking_id.move_lines.filtered(lambda ml: ml.quantity_done > 0),
            "weight_uom": self.env[
                "product.template"
            ]._get_weight_uom_id_from_ir_config_parameter(),
        }

    def _l10n_mx_edi_get_invoice_cfdi_values(self, invoice):
        """Return a dictionary with the values to render the CFDI template.

        :param invoice: An account.move record.
        :return:        A dictionary with the values to render the CFDI template.
        """
        res = super()._l10n_mx_edi_get_invoice_cfdi_values(invoice)

        if invoice.carta_porte_picking_id:
            if invoice.carta_porte_picking_id.state != "done":
                raise UserError(
                    _("The picking %s is not done, you can not generate the carta porte.")
                    % invoice.carta_porte_picking_id.name
                )
            if invoice.carta_porte_picking_id.invoice_carta_porte_id:
                raise UserError(
                    _("The picking %s already has a carta porte.")
                    % invoice.carta_porte_picking_id.name
                )
            values = self._vals_to_use_in_carta_porte(invoice)
            invoice.carta_porte_picking_id.invoice_carta_porte_id = invoice
            res.update(values)

        return res
