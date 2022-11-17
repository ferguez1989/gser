{
    'name': 'Servicio Rutas',
    'version': '13.0.0.4.0',
    'author': 'GSerrano Lagos de Moreno',
    'website': '',
    'license': 'LGPL-3',
    'depends': [
        "sale_management",
        "industry_fsm",
        "project",
        "fleet",
    ],
    'data': [
        # security
        # data
        # demo
        
        # # views
        'views/proyecto_ruta.xml',
        'views/servicio_externo_proyecto.xml',
        # reports
        'report/reports.xml',
        'report/ticket_viaje.xml',
        'report/ticket_cliente.xml',
        'report/proceso_lavado.xml',
        'report/cp_vertical.xml',
        'report/inspeccion_trans.xml',
    ],
}