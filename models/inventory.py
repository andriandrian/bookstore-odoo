from odoo import models, fields, api, _


class Inventory(models.Model):
    _name = "bookstore.inventory"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Book Inventory"
    _rec_name = 'ref'

    name = fields.Many2one('bookstore.book', string='Name', tracking=True)
    date = fields.Datetime(
        string='Date', default=fields.Datetime.now, tracking=True)
    invoice_date = fields.Datetime(
        string='Invoice Date', default=fields.Datetime.now, tracking=True)
    ref_rel = fields.Char(string='Reference',
                          readonly=True, related='name.ref')
    ref = fields.Char(string='Reference', readonly=True,
                      default=lambda self: _('New'))
    stock = fields.Integer(string='Stock', tracking=True, )
    unit_measure = fields.Selection([('piece', 'PCs'), ('dozen', 'Dozen')],
                                    string="Unit of Measure", default='piece', tracking=True, )
    company = fields.Many2one(
        'res.company', string='To', tracking=True, )
    stock_type = fields.Selection(
        [('in', 'In'),
         ('out', 'Out')],
        string="Type", default='in', tracking=True, )
    state = fields.Selection([('draft', 'Draft'),
                              ('shipped', 'Shipped'),
                              ('completed', 'Completed'),
                              ('cancel', 'Cancelled')], string="Status", default='draft', tracking=True, )
    transaction_id = fields.Integer(string='Transaction ID', tracking=True, )

    @api.model
    def create(self, vals):
        if vals.get('ref', _('New')) == _('New'):
            vals['ref'] = self.env['ir.sequence'].next_by_code(
                'bookstore.inventory') or _('New')
        res = super(Inventory, self).create(vals)
        return res

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
