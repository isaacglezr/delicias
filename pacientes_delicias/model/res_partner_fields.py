from odoo import api, fields, models

class New_fields_partner(models.Model):

    _inherit = "res.partner"

    x_NumExpediente = fields.Char(string='Expediente')
    x_medico = fields.Many2one('medicos.delicias', string="Doctor")
    x_Privado = fields.Many2one('num.habitacion', string="Privado")
