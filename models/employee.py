from odoo import models, fields, api, _

class Employee(models.Model):
    _name = "bookstore.employee"
    _description = "Employee Bookstore"

    name = fields.Char('Name', required=True)
    age = fields.Integer('Age', required=True)
    ref = fields.Char('Reference', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", required=True)
    active = fields.Boolean('Active', default=True)
    # address = fields.Text('Address', required=True)
    # phone = fields.Char('Phone', required=True)
    # email = fields.Char('Email', required=True)

