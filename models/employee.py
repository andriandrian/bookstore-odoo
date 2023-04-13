from datetime import date
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class BookstoreEmployee(models.Model):
    _name = "bookstore.employee"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Employee Bookstore"

    name = fields.Char(string='Name', tracking=True)
    date_of_birth = fields.Date('Date of Birth')
    age = fields.Integer(string='Age', compute='_compute_age', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')],
                              string="Gender", default='male', tracking=True, required=True)
    position = fields.Selection([('staff', 'Staff'), ('cashier', 'Cashier'), ('administrator', 'Administrator'), (
        'shippingstaff', 'Shipping and Receiving Staff')], string="Position", default='staff', tracking=True, required=True)
    active = fields.Boolean(string='Active', default=True)
    image = fields.Image(string="Image", max_width=1024, max_height=1024,
                         help="This field holds the image used as avatar for this Employee, limited to 1024x1024px")

    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth > fields.Date.today():
                raise ValidationError(
                    _('Date of birth must be less than today'))

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0
