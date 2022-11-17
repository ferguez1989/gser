from odoo import fields, models, api

class FlotaSerrano(models.Model):
    _inherit = "fleet.vehicle"                 
    tipo_vehiculo = fields.Selection([
        ('1','Unidad'),
        ('2','Remolque'),],
        string="Tipo de vehiculo",
    )    
    no_economico = fields.Char(
        string="No. economico",
    )
    #Parte del motor
    capacidad_tanque =fields.Integer(
        string="Capacidad del Tanque",
    )
    #Parte de modelo
    numero_poliza =fields.Char(
        string="Numero de poliza",
    )
    vigencia_poliza =fields.Date(
        string="Vig. de la poliza",
    ) 
    file_poliza = fields.Binary(
        string="Carga Poliza",
    )
    vigencia_fisico_mecanico =fields.Date(
        string="Vig. Fisico-Mecanico",
    ) 
    file_fisico_mecanico = fields.Binary(
        string="Carga Poliza F-Mecanico",
    )
    vigencia_emisiones =fields.Date(
        string="Vig.Emisiones",
    ) 
    file_emisiones = fields.Binary(
        string="Carga Emisiones",
    )
    file_circulacion = fields.Binary(
        string ="Carga Circulación",
    )
    file_factura = fields.Binary(
        string= "Carga de Factura",
    )