{
    'name': 'VSM Conam Address Project',
    'version': '16.0.1.0.0',
    'summary': 'Adiciona campos de endereço do projeto no CRM Lead',
    'description': """
        Este módulo adiciona campos de endereço do projeto no formulário do CRM Lead,
        permitindo capturar informações específicas do local onde o projeto será executado.
    """,
    'author': 'VSM',
    'website': '',
    'category': 'CRM',
    'depends': ['crm', 'base'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
} 