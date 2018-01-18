from odoo import api, fields, models

class Pacientes_delicias(models.Model):
    _name='pacientes.delicias'
    
    x_paciente=fields.Many2one('res.partner', string='Paciente', required=True)
    x_FechaEntrada = fields.Datetime(string='Fecha de Ingeso')
    x_FechaSalida = fields.Datetime(string='Fecha de Alta')
    x_Expediente = fields.Char(string='Expediente')
    x_Doctor = fields.Many2one('medicos.delicias', string='Doctor')
    x_MediMaterial= fields.Many2many('product.product', string='Medicamento/Material')
    
    #Habitacion
    x_Habitacion = fields.Boolean(string='Requiere Habitacion')
    x_NumHabitacion = fields.Many2one('num.habitacion', string='Numero de Habitacion')
    
    #Quirofano
    x_Quirofano = fields.Boolean(string='Quirofano')
    x_NumQuirofano = fields.Many2one('num.quirofano', string='Sala de Quirofano')

    @api.onchange('x_paciente')
    def _onchange_employee_id(self):
        if self.x_paciente:
            self.x_Expediente = self.x_paciente.x_NumExpediente
