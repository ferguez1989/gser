from odoo import fields, models

class datosEmpleados (models.Model):
    _inherit="hr.employee"
    #Documentacion personal
    """acta_nacimiento = fields.Binary(
        string="Acta de Nacimiento",
    )
    domicilio = fields.Binary(
        string="Comp. Domicilio",
    )
    estudios = fields.Binary(
        string="Comp. Estudios",
    )
    curp = fields.Binary(
        string="CURP",
    )
    rfc = fields.Binary(
        string="RFC",
    )
    ine = fields.Binary(
        string="INE",
    )
    #Seguro
    nseguridad_social = fields.Char(
        string="NSS",
    )
    alta_patronal = fields.Date(
        string="Fecha de alta patronal",
    )
    alta_imss = fields.Binary(
        string="Alta IMSS",
    )
    infonavit = fields.Binary(
        string="Comp. Infonavit",
    )
    #Contratos
    empleado_fecha_ingreso = fields.Date(
        string="Fecha de ingreso",
    )
    empleado_contrato = fields.Binary(
        string="Contrato",
    )
    empleado_reglamento = fields.Binary(
        string="Reglamento",
    )
    empleado_codigo_etica = fields.Binary(
        string="Codigo Etica",
    )
    empleado_baja_fecha = fields.Date(    
        string="Fecha Baja",
    )
    empleado_baja = fields.Binary(
        string="Baja",
    )
    empleado_motivo_baja = fields.Text(
        string="Motivo",
    )  
    no_antesedentes = fields.Binary(
        string="Carta Antecedentes",
    )   
    recomendacion1 = fields.Binary(
        string="Carta de recomendación 1",
    )
    recomendacion2 = fields.Binary(
        string="Carta de recomendación 2",
    )
    #Vehiculo
    licencia = fields.Binary(
        string="Licencia",
    )
    vigencia = fields.Date(
        string="Vigencia",
    )
    chofer_examen = fields.Binary(
        string="Examen de manejo",
    )
    vigencia_exam = fields.Date(
        string="Vigencia Examen",
    )
    #responsivas
    res_unidad = fields.Binary(
        string="Unidad",
    )
    res_llave_caseta = fields.Binary(
        string="Llave caseta",
    )
    res_llave_diesel = fields.Binary(
        string="Llave Diesel",
    )
    res_telefono = fields.Binary(
        string="Telefono",
    )
    res_equipo = fields.Binary(
        string="Equipo",
    )
    res_resguardo1 = fields.Binary(
        string="Resguardo 1",
    )
    res_resguardo2 = fields.Binary(
        string="Resguardo 2",
    )"""