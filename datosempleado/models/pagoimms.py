from odoo import fields, models

class datosEmpleados (models.Model):
    _inherit="hr.plan"
    #Modulo para subir los pagos de imms
    pago_imms = fields.Binary(
        string="Pago de Seguro",
    )
    fecha_pago = fields.Date(    
        string="Fecha pago",
    )