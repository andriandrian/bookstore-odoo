from odoo import models, fields, api, _

class Books(models.Model):
    _name = "bookstore.book"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Book Bookstore"

    category_id = fields.Many2one('bookstore.category', string="Category")
    name = fields.Char(string='Name', tracking=True)
    author = fields.Char(string='Author', tracking=True)
    price = fields.Float(string='Price', tracking=True)
    description = fields.Text(string='Description', tracking=True)
    quantity = fields.Integer(string='Quantity', tracking=True)
    category = fields.Selection([('fiction', 'Fiction'), ('non-fiction', 'Non-Fiction')], string="Category", default='fiction', tracking=True, required=True)
    # category_id = fields.Many2one(string="Category", comodel_name='bookstore.category')
    ref = fields.Char(string='Reference', default='New Reference')
    prescription = fields.Html(string='Prescription')
    active = fields.Boolean(string='Active', default=True)
