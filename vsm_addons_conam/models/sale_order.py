from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    spe_id = fields.Many2one('spe.sociedade', string='SPE', 
                            domain="[('active', '=', True)]",
                            help="Sociedade para Propósito Específico")
    cnpj_spe = fields.Char(string='CNPJ da SPE', size=18, help="CNPJ da Sociedade para Propósito Específico") 