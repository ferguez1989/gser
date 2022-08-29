from odoo import fields, models, api

class servicioGSerprimario (models.Model):
    _inherit = ['project.task']

    #@api.multi
    #def name_get(self):
    #    res = []
    #    for rec in self:
    #        res.append((rec.model_id, '%s - %s' % (rec.no_economico, rec.license_plate)))
    #        #res.append((rec.model_id, '%s - %s' % (rec.no_economico, rec.license_plate)))
    #    return res

    status_viaje = fields.Selection([
        ('1','Programado'),
        ('2','Pendiente de gastos'),
        ('3','Pendiente de diesel'),
        ('4','Pendiente de carta porte'),
        ('5','En trayecto'),
        ('6','En validación'),
        ('7','Por facturar'),
        ('8','Por cobrar'),
        ('9','Finalizado'),
        ('10','Cancelado'),
        ('12','Rechazado'),],
        string="Estado de Viaje",
    )
    vehiculo = fields.Many2one(
        comodel_name='fleet.vehicle',
        ondelete='set null',
        index=True,
        string="Vehiculo",
    )
    anio_vehiculo = fields.Char(
        related ='vehiculo.model_year',
        string="Año vehículo",
    )
   
    remolque_1 = fields.Many2one(
        comodel_name ='fleet.vehicle',
        ondelete ='set null',
        index=True,
        string="Remolque 1",
    )
    remolque_2 = fields.Char(
        related ='remolque_1.no_economico',
        string="No. Economico Remolque",
    )
    
    tipo_ruta_viaje= fields.Selection(
       related = 'project_id.tipo_precio',
        string ="Tipo Ruta",
    )
    carga_viaje= fields.Selection(
        related = 'project_id.carga_ruta',
        string ="Carga",
    )  
    capacidad_viaje = fields.Selection(
        related ='project_id.capacidad_ruta',
        string ="Capacidad",
    ) 
    producto_viaje = fields.Selection(
        related ='project_id.producto_ruta',
        string ="Producto",
    ) 
    conductor = fields.Char(
        related ='vehiculo.driver_id.name',
        string ="Conductor",
    )  
    gasto_total_op_viaje= fields.Float(
        related ='project_id.gasto_totalOper',
        string ="Gastos del operador",
    )
    gasto_total_caseta_viaje= fields.Char(
        related ='project_id.email_facturacion',
        string ="Gastos de caseta",
    )   
    disel_viaje= fields.Float(
        related ='project_id.disel',
        string ="Diesel",
    )   
    km_viaje= fields.Float(
        related ='project_id.km_ruta',
        string ="Kilometraje",
    )   
    carga_combustible= fields.Selection([
        ('1','Grupo Serrano'),
        ('2','Gasolinera La Loma'),
        ('3','Otro'),],
        string="Carga de combustible",
    )
    pmanager = fields.Many2one(
        string ="Project Manager",
        comodel_name ='res.partner',
        ondelete ='set null',
        intex =True,
    )
    Cantidad = fields.Float(
        string ="Cantidad",
    )          
    Precio_ruta_Litro = fields.Float(
        string ="Precio ruta / litro",
    )    
    Subtotal   = fields.Float(
        string ="SubTotal",
    )     
    Iva = fields.Float(
        string ="IVA 16%",
    )    
    Retencion = fields.Float(
        string ="Retención 4%",
    )   
    Total_Facturar = fields.Float(
        string ="Total a Facturar",
    )
    Forma_pago = fields.Selection(
        string ="Forma de pago",
    )          
    No_Factura = fields.Char(
        string ="No. Factura",
    )    
    Fecha_Factura = fields.Char(
        string ="Fecha de factura",
    )
    Fecha_Pago = fields.Char(
        string ="Fecha pago",
    )

    
