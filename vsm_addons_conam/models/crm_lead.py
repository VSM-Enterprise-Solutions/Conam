from odoo import models, fields, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    tipo_servico = fields.Selection([
        ('licenciamento', 'Licenciamento Ambiental'),
        ('investigacao', 'Investigação e Reabilitação de Áreas Contaminadas'),
        ('estudos', 'Estudos Ambientais'),
        ('regularizacao', 'Regularização Ambiental de Imóveis Rurais'),
        ('outorga', 'Outorga de Uso da Água'),
        ('barragens', 'Classificação e Segurança de Barragens'),
        ('due_diligence', 'Due Diligence Ambiental'),
        ('fitorremediacao', 'Fitorremediação'),
        ('consultoria', 'Consultoria e Auditoria Ambiental'),
        ('monitoramento', 'Monitoramento Ambiental'),
        ('residuos', 'Gestão de Resíduos'),
        ('pca', 'Planos de Controle Ambiental (PCA)'),
        ('prad', 'Planos de Recuperação de Áreas Degradadas (PRAD)')
    ], string='Tipo de Serviço') 