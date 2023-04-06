from odoo import models, fields, api, _


class Transaction(models.Model):
    _name = "bookstore.transaction"
    _description = "Book Transaction"

    name = fields.Char(string='Name', tracking=True)
    ref = fields.Char(string='Reference', default='New Reference')
    description = fields.Text(string='Description', tracking=True)
    active = fields.Boolean(string='Active', default=True)
    book_ids = fields.One2many(
        'bookstore.book.line', 'book_id', string='Books')
    date = fields.Datetime(
        string='Date', default=fields.Datetime.now, readonly=True)
    total = fields.Float(string='Total', compute='_compute_total', store=True)


# class TransactionBook(models.Model):
    # _name = "bookstore.transaction.book"
    # _description = "Book Transaction Book"

    # book_ids = fields.Many2one('bookstore.book', string='Book')
    # price = fields.Float('bookstore.book', string='Price')
    # qty = fields.Integer(string='Quantity')
