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
        'security/ir.model.access.csv',
        'security/spe_record_rule.xml',
        'views/crm_lead_meeting_inherit.xml',
        'views/sale_order_inherit.xml',
        'views/crm_lead_quick_create.xml',
        'views/crm_lead_form_inherit.xml',
        'views/sale_order_inherit_spe.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'vsm_addons_conam/static/src/css/crm_lead_custom.css',
            'vsm_addons_conam/static/src/js/cnpj_mask.js',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
