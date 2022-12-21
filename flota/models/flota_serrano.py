from odoo import fields, models, api

class FlotaSerrano(models.Model):
    _inherit = "fleet.vehicle"                 
    tipo_vehiculo = fields.Selection([
        ('1','Tractocamion'),
        ('2','Unidad'),
        ('3','Torton'),
        ('4','Pickup'),
        ('5','Unidad'),
        ('6','Maquinaria Pesada'),
        ('7','Tanque'),
        ('8','Caja Seca'),
        ('9','Gondola'),
        ('10','Plataforma'),
        ('11','Cama Baja'),
        ('12','Caja Refrigerada'),
        ('13','Tanque Acero Inoxidable'), 
        ('14','Remolque'),],
        string="Tipo de vehiculo",
    )
    no_economico = fields.Char(
        string="No. economico",
    )   
    capacidad_remolque = fields.Char(
        string="Capacidad Remolque",
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
    file_otro = fields.Binary(
        string= "Otro",
    )