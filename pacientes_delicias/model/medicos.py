from odoo import api, fields, model

class Medicos(models.Model):

    _name = "medicos.delicias"

    x_DocName = fields.Char(string="Nombre")
    x_Especialidad = fields.Char(string="Especialidad")
    x_movil = fields.Char(string="Telefono")
