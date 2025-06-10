# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    project_address = fields.Char(
        string='Endereço do Projeto',
        help='Endereço onde o projeto será executado'
    )

    # Campos de endereço do projeto
    project_street = fields.Char(
        string='Rua do Projeto',
        help='Endereço da rua onde o projeto será executado'
    )
    project_street2 = fields.Char(
        string='Complemento do Projeto',
        help='Complemento do endereço do projeto (apartamento, bloco, etc.)'
    )
    project_city = fields.Char(
        string='Cidade do Projeto',
        help='Cidade onde o projeto será executado'
    )
    project_state_id = fields.Many2one(
        'res.country.state',
        string='Estado do Projeto',
        help='Estado onde o projeto será executado'
    )
    project_zip = fields.Char(
        string='CEP do Projeto',
        help='CEP do local onde o projeto será executado'
    )
    project_country_id = fields.Many2one(
        'res.country',
        string='País do Projeto',
        help='País onde o projeto será executado',
        default=lambda self: self.env.ref('base.br')
    )
    
    # Campo para observações sobre o endereço do projeto
    project_address_notes = fields.Text(
        string='Observações do Endereço',
        help='Observações adicionais sobre o endereço do projeto'
    )
    
    # Campo computado para exibir o endereço completo
    project_address_complete = fields.Char(
        string='Endereço Completo do Projeto',
        compute='_compute_project_address_complete',
        store=True,
        help='Endereço completo do projeto formatado'
    )
    
    @api.depends('project_street', 'project_street2', 'project_city', 
                 'project_state_id', 'project_zip', 'project_country_id')
    def _compute_project_address_complete(self):
        """Computa o endereço completo do projeto"""
        for record in self:
            address_parts = []
            
            if record.project_street:
                address_parts.append(record.project_street)
            
            if record.project_street2:
                address_parts.append(record.project_street2)
            
            if record.project_city:
                address_parts.append(record.project_city)
            
            if record.project_state_id:
                address_parts.append(record.project_state_id.name)
            
            if record.project_zip:
                address_parts.append(f'CEP: {record.project_zip}')
            
            if record.project_country_id:
                address_parts.append(record.project_country_id.name)
            
            record.project_address_complete = ', '.join(address_parts) if address_parts else ''
    
    @api.onchange('project_country_id')
    def _onchange_project_country_id(self):
        """Limpa o estado quando o país é alterado"""
        if self.project_country_id:
            self.project_state_id = False
    
 