from odoo import api, fields, models

class Habitacion(models.Model):

    _name='num.habitacion'

    x_numhab=fields.Char(string='Numero de Habitacion')
