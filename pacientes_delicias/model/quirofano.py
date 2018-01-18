from odoo import api, fields, models

class Quirofano(models.Model):

    _name='num.quirofano'

    id_quiro = fields.Integer(string='id')
    x_numquiro = fields.Char(string='Sala de Quirofano')
