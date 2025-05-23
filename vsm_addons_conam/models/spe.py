from odoo import models, fields

class SPE(models.Model):
    _name = 'spe.sociedade'
    _description = 'Sociedade para Propósito Específico'

    name = fields.Char(string='Nome da SPE', required=True)
    active = fields.Boolean(default=True)
    partner_id = fields.Many2one('res.partner', string='Cliente', required=True, default=lambda self: self.env.user.partner_id)

    def action_activate(self):
        self.write({'state': 'active'})

    def action_inactivate(self):
        self.write({'state': 'inactive'}) 