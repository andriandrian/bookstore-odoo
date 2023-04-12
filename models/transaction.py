from odoo import models, fields, api, _


class Transaction(models.Model):
    _name = "bookstore.transaction"
    _description = "Book Transaction"
    _rec_name = 'ref'

    currency_id = fields.Many2one('res.currency', string='Currency',
                                  default=lambda self: self.env.user.company_id.currency_id.id)
    name = fields.Char(string='Name', tracking=True)
    ref = fields.Char(string='Reference', required=True,
                      readonly=True, default=lambda self: _('New'))
    description = fields.Text(string='Description', tracking=True)
    active = fields.Boolean(string='Active', default=True)
    transaction_ids = fields.One2many(
        'bookstore.transaction.line', 'transaction_id', string='Books')
    date = fields.Datetime(
        string='Date', default=fields.Datetime.now, readonly=True)
    amount_total = fields.Float(
        string='Total', compute='_compute_amount_total')

    @api.model
    def create(self, vals):
        if vals.get('ref', _('New')) == _('New'):
            vals['ref'] = self.env['ir.sequence'].next_by_code(
                'bookstore.transaction') or _('New')
        res = super(Transaction, self).create(vals)
        return res

    # @api.multi
    # def print_report(self):
    #     return self.env.ref('bookstore.transaction_report_temp').report_action(self)

    def _compute_amount_total(self):
        for rec in self:
            rec.amount_total = sum(rec.transaction_ids.mapped('subtotal'))

    # @api.multi
    # def print_report(self):
    #     return self.env.ref('')


class TransactionLine(models.Model):
    _name = "bookstore.transaction.line"
    _description = "Book Line"

    currency_id = fields.Many2one('res.currency', string='Currency',
                                  default=lambda self: self.env.user.company_id.currency_id.id)
    transaction_id = fields.Many2one('bookstore.transaction', string='Book')
    name = fields.Many2one('bookstore.book', string='Book')
    price_rel = fields.Float(string='Price', related="name.price")
    qty = fields.Integer(string='Quantity')
    subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal')

    @api.onchange('qty')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.price_rel * rec.qty

# class TransactionBook(models.Model):
    # _name = "bookstore.transaction.book"
    # _description = "Book Transaction Book"

    # book_ids = fields.Many2one('bookstore.book', string='Book')
    # price = fields.Float('bookstore.book', string='Price')
    # qty = fields.Integer(string='Quantity')
