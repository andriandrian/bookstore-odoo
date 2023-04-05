from datetime import date
from odoo import models, fields, api, _

class BookstoreEmployee(models.Model):
    _name = "bookstore.employee"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Employee Bookstore"

    name = fields.Char(string='Name', tracking=True)
    date_of_birth = fields.Date('Date of Birth')
    ref = fields.Char(string='Reference', default='New Reference')
    age = fields.Integer(string='Age', compute='_compute_age', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", default='male', tracking=True, required=True)
    active = fields.Boolean(string='Active', default=True)
    # address = fields.Text('Address', required=True)
    # phone = fields.Char('Phone', required=True)
    # email = fields.Char('Email', required=True)

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 1