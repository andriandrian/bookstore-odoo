from odoo import models, fields, api, _

class BookstoreAppointment(models.Model):
    _name = "bookstore.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Bookstore Appointment"

    employee_id = fields.Many2one(string="Employee", comodel_name='bookstore.employee')
    appointment_time = fields.Datetime(string='Appointment Time')
    booking_date = fields.Date(string='Booking Date')