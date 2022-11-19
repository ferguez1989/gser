from odoo import fields, models, api
class proyecto_ruta (models.Model):
    # Referencia a modelo al cual vamos a heredar.
    _inherit = ['project.project']
    # Desabilihitar la parte de las hojas de trabajo
    #allow_timesheets=fields.Boolean(
    #    default = False,
    #)
    # Campos agregados al modelo de proyecto seccion principal
    estatus_ruta = fields.Selection([
        ('1','Activa'),
        ('2','Inactiva'),],
        string="Estatus Ruta",
    )
    # Campos relacional: la referencia indica el modelo de donde estamos mandando llamr los datos
    contacto_facturacion = fields.Many2one(
        comodel_name='res.partner',
        ondelete='set null',
        index=True,
        string="Contacto Facturación",
    )
    # Campo Char: campo para introducir texto
    email_facturacion = fields.Char(
        related ='contacto_facturacion.email',
        string="E-mail Facturación",
    )
    orden_venta = fields.Many2one(
        comodel_name='sale.order',
        ondelete='set null',
        index=True,
        string="Orden de Venta",
    )
    #Campos de la sección de Ruta.Ruta
    km_ruta = fields.Float(
        string="Kilometros",
    )
    carga_ruta = fields.Selection([
        ('1','Full'),
        ('2','Sencillo'),
        ('3','Caja seca'),
        ('4','Gondola'),
        ('5','Plataforma'),
        ('6','Torton'),
        ('7','N/A'),
        ('8','12'),],
        string="Carga",
    )
    capacidad_ruta = fields.Selection([
        ('1','25,000 Litros'),
        ('2','30,000 Litros'),
        ('3','35,000Litros'),
        ('4','36,000 Litros'),
        ('5','50,000 Litros'),
        ('6','54,000 Litros'),
        ('7','2 Tonelada'),
        ('8','10 Tonelada'),
        ('9','20 Tonelada'),
        ('10','30 Tonelada'),
        ('11','N/A'),],
        string="Capacidad",
    )
    ejes_ruta = fields.Selection([
        ('1','2 ejes'),
        ('2','3 ejes'),
        ('3','5 ejes'),
        ('4','6 ejes'),
        ('5','9 ejes'),],
        string="Ejes",
    )
    producto_ruta = fields.Selection([
        ('1','Aceite'),
        ('2','Aceite pollo'),
        ('3','Crema'),
        ('4','Cascarilla de arroz'),
        ('5','Leche'),
        ('6','Leche en polvo'),
        ('7','Lacteos'),
        ('8','Lodos planta tratamientos'),
        ('9','Pluma'),
        ('10','Refacciones'),
        ('11','Otros'),],
        string="Producto",
    )
    tipo_precio = fields.Selection([
        ('1','Ruta'),
        ('2','Litro'),
        ('3','Kilogramo')],
        string="Tipo de precio",
        index = True,
    )
    precio = fields.Float(
        string="Precio",
    )
    precio_diesel = fields.Float(
        default = 20.00,
        string="Precio Diesel",
    )
    rendimiento_diesel = fields.Float(
        compute='_calculo_rendimeinto',
        string="Rendimiento",
    )
    diesel = fields.Float(
        compute='_compute_diesel',
        string ='Diesel'
   )
    caseta_efectivo = fields.Float(
        string="Caseta Efectivo",
    )
    caseta_llave = fields.Float(
        string="Caseta Llave",
    )
    gastos_operador = fields.Float(
        string="Gasto Operador",
    )
    gasto_total_operador = fields.Float(
        compute='_compute_gastoopera',
        string="Gasto Total del Operador",
    )
    gasto_total = fields.Float(
        compute='_compute_gastoT',
        string="Gasto Total",
    )
    # Datos de origen
    recoge_en_origen = fields.Char(
        string="Se recoge en:",
    )
    direccion_origen= fields.Char(
        string="Dirección origen:",
    )
    pais_origen= fields.Many2one(
        string ="País origen:",
        comodel_name='res.country',
        ondelete='set null',
        index=True,
    )
    estado_origen= fields.Many2one(
        string ="Estado origen:",
        comodel_name='res.country.state',
        ondelete='set null',
        index=True,
    )
    ciudad_origen= fields.Char(
        string ="Ciudad origen:",
        comodel_name='res.city',
        ondelete='set null',
        index=True,
    )
    # Datos de destino
    entrega_destino = fields.Char(
        string="Se entrega en:",
    )
    direccion_destino= fields.Char(
        string="Dirección destino:",
    )
    pais_destino= fields.Many2one(
        string ="País destino:",
        comodel_name='res.country',
        ondelete='set null',
        index=True,
    )
    estado_destino= fields.Many2one(
        string ="Estado destino:",
        comodel_name='res.country.state',
        ondelete='set null',
        index=True,
    )
    ciudad_destino= fields.Char(
        string ="Ciudad destino:",
        #comodel_name='res.country.city',
        #ondelete='set null',
        #index=True,
    )
    # Datos Computados para el calculo de gastos
    @api.depends("diesel", "precio_diesel","caseta_llave","gastos_operador","caseta_efectivo")
    def _compute_gastoT(self):
        for record in self:
            record.gasto_total = (record.diesel * record.precio_diesel) + record.caseta_llave + record.caseta_efectivo + record.gastos_operador
    @api.depends("caseta_efectivo", "gastos_operador")
    def _compute_gastoopera(self):
        for record in self:
            record.gasto_total_operador = record.caseta_efectivo + record.gastos_operador
    @api.depends("km_ruta", "rendimiento_diesel")
    def _compute_diesel(self):
        for record in self:
            record.diesel = record.km_ruta / record.rendimiento_diesel
    @api.depends("carga_ruta","rendimiento_diesel")
    def _calculo_rendimeinto(self):
        for record in self:
            if record.carga_ruta == '1':
                record.rendimiento_diesel = 5
            else:
                record.rendimiento_diesel = 2.1
            