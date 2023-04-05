from odoo import models, fields, api, _

class BookstoreAppointment(models.Model):
    _name = "bookstore.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Bookstore Appointment"
    _rec_name = 'employee_id'

    employee_id = fields.Many2one(string="Employee", comodel_name='bookstore.employee')
    gender = fields.Selection(string="Gender", related='employee_id.gender')
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today)
    ref = fields.Char(string='Reference', default='New Reference')

    @api.onchange('employee_id')
    def onchange_employee_id(self):
        self.ref = self.employee_id.ref
