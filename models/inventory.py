from odoo import models, fields, api, _


class Inventory(models.Model):
    _name = "bookstore.inventory"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Book Inventory"
    # _rec_name = 'book_id'

    name = fields.Many2one('bookstore.book', string='Name', tracking=True)
    date = fields.Datetime(
        string='Date', default=fields.Datetime.now, tracking=True)
    invoice_date = fields.Datetime(
        string='Invoice Date', default=fields.Datetime.now, tracking=True)
    # ref = fields.Char(string="Reference", related='bookstore_book.ref')
    ref = fields.Char(string='Reference', readonly=True, related='name.ref')
    # vendor = fields.Char(string='From', tracking=True)
    # to = fields.Char(string='To', tracking=True)
    stock = fields.Integer(string='Stock', tracking=True, required=True)
    unit_measure = fields.Selection([('piece', 'PCs'), ('dozen', 'Dozen')],
                                    string="Unit of Measure", default='piece', tracking=True, required=True)
    company = fields.Many2one(
        'res.company', string='To', tracking=True, required=True)
    state = fields.Selection([('draft', 'Draft'), ('done', 'Done')],
                             string="State", default='draft', tracking=True, required=True)
    stock_type = fields.Selection(
        [('in', 'In'),
         ('out', 'Out')],
        string="Type", default='in', tracking=True, required=True)
    state = fields.Selection([('draft', 'Draft'),
                              ('shipped', 'Shipped'),
                              ('completed', 'Completed'),
                              ('cancel', 'Cancelled')], string="State", default='draft', tracking=True, required=True)

    @api.onchange('book_id')
    def onchange_book_id(self):
        self.ref = self.book_id.ref

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_shipped(self):
        for rec in self:
            rec.state = 'shipped'

    def action_completed(self):
        for rec in self:
            rec.state = 'completed'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'
