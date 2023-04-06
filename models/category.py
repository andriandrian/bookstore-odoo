from odoo import models, fields, api, _


class Categories(models.Model):
    _name = "bookstore.category"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Book Category"

    name = fields.Char(string='Name', tracking=True)
    description = fields.Text(string='Description', tracking=True)
    active = fields.Boolean(string='Active', default=True)
