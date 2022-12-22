from email.policy import default
from unittest.mock import DEFAULT
from odoo import fields, models, api
class servicio_externo_proyecto (models.Model):
    _inherit = ['project.task']
    allow_timesheets=fields.Boolean(
        default = False,
    )   
    estatus_viaje = fields.Selection([
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
        default='1',
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
    r1_no_economico = fields.Char(
        related ='remolque_1.no_economico',
        string="No. Economico r1",
    )
    remolque_2 = fields.Many2one(
        comodel_name ='fleet.vehicle',
        ondelete ='set null',
        index=True,
        string="Remolque 2",
    )
    r2_no_economico = fields.Char(
        related ='remolque_2.no_economico',
        string="No. Economico r2",
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
        related ='project_id.gasto_total_operador',
        string ="Gastos del operador",
    )
    gasto_total_caseta_viaje= fields.Float(
        related ='project_id.caseta_efectivo',
        string ="Gastos de caseta",
    )   
    diesel_viaje= fields.Float(
        related ='project_id.diesel',
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
        string ="Manager",
        comodel_name='res.users',
        default=lambda self: self.env.user.id
    )
    cantidad = fields.Float(
        string ="Cantidad",
    )          
    precio_ruta_litro = fields.Float(
        related ="project_id.precio",
        string ="Precio ruta / litro",
    )    
    subtotal   = fields.Float(
        compute='_compute_subtotal',
        string ="Subtotal",
    )     
    iva = fields.Float(
        compute='_compute_iva',
        string ="IVA 16%",
    )    
    retencion = fields.Float(
        compute ='_compute_iva',
        string ="Retención 4%",
    )   
    total_facturar = fields.Float(
        compute ='_compute_total_facturar',
        string ="Total a Facturar",
        store=True,
    )
    forma_pago = fields.Selection([
        ('1','Transferencia'),
        ('2','Efectivo'),],
        string ="Forma de pago",
    )          
    no_factura = fields.Char(
        #comodel_name='account.move',
        #ondelete='set null',
        #index=True,
        string ="No. Factura",
    )    
    fecha_factura = fields.Date(
        string ="Fecha de factura",
    )
    fecha_pago = fields.Date(
        string ="Fecha pago",
    )

    @api.depends("cantidad", "precio_ruta_litro")
    def _compute_subtotal(self):
        for record in self:
            record.subtotal = record.cantidad * record.precio_ruta_litro
    @api.depends("subtotal")
    def _compute_iva(self):
        for record in self:
            record.iva = record.subtotal * 0.16
            record.retencion = record.subtotal * 0.04
    @api.depends("subtotal", "iva", "retencion", "cantidad", "total_facturar")
    def _compute_total_facturar(self):
        for record in self:
            if record.total_facturar != 0:
                record.total_facturar = record.total_facturar
            else:
                record.total_facturar = (record.subtotal + record.iva) - record.retencion
                