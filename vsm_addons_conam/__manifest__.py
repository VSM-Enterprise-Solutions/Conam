{
    'name': 'VSM Addons Conam',
    'version': '1.0',
    'summary': 'Módulo de Ajustes da conam',
    'description': """
        Este módulo é responsável pelos ajustes em crm e vendas.
    """,
    'author': 'VSM Enterprise Solutions',
    'depends': ['base', 'crm', 'sale'],
    'static': [
        'static/description/icon.png', 
    ],
    'data': [
        'views/crm_lead_meeting_inherit.xml',
        'views/sale_order_inherit.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
