from odoo import models, fields, api, _


class Transaction(models.Model):
    _name = "bookstore.transaction"
    _description = "Book Transaction"

    name = fields.Char(string='Name', tracking=True)
    ref = fields.Char(string='Reference', default='New Reference')
    description = fields.Text(string='Description', tracking=True)
    active = fields.Boolean(string='Active', default=True)
    transaction_ids = fields.One2many(
        'bookstore.transaction.line', 'transaction_id', string='Books')
    date = fields.Datetime(
        string='Date', default=fields.Datetime.now, readonly=True)
    total = fields.Float(string='Total', compute='_compute_total')

    def _compute_total(self):
        self.total = sum(self.transaction_ids.mapped('subtotal'))

    # @api.multi
    # def print_report(self):
    #     return self.env.ref('')


class TransactionLine(models.Model):
    _name = "bookstore.transaction.line"
    _description = "Book Line"

    transaction_id = fields.Many2one('bookstore.transaction', string='Book')
    name = fields.Many2one('bookstore.book', string='Book')
    price = fields.Float(string='Price', related="name.price")
    qty = fields.Integer(string='Quantity')
    subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal')

    @api.onchange('qty')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.price * rec.qty

# class TransactionBook(models.Model):
    # _name = "bookstore.transaction.book"
    # _description = "Book Transaction Book"

    # book_ids = fields.Many2one('bookstore.book', string='Book')
    # price = fields.Float('bookstore.book', string='Price')
    # qty = fields.Integer(string='Quantity')
