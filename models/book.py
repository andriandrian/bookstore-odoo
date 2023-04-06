from odoo import models, fields, api, _


class Books(models.Model):
    _name = "bookstore.book"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Book Bookstore"

    book_id = fields.Many2one('bookstore.transaction', string='Book')
    category_id = fields.Many2one('bookstore.category', string="Category")
    name = fields.Char(string='Name', tracking=True)
    author = fields.Char(string='Author', tracking=True)
    price = fields.Float(string='Price', tracking=True)
    description = fields.Text(string='Description', tracking=True)
    qty = fields.Integer(string='Quantity', tracking=True,
                         compute='_compute_quantity')
    category = fields.Selection([('fiction', 'Fiction'), ('non-fiction', 'Non-Fiction')],
                                string="Category", default='fiction', tracking=True, required=True)
    # ref = fields.Char(string='Reference', default='New Reference')
    ref = fields.Char(string='Reference', required=True,
                      readonly=True, default=lambda self: _('New'))
    prescription = fields.Html(string='Prescription')
    active = fields.Boolean(string='Active', default=True)

    @api.model
    def create(self, vals):
        if vals.get('ref', _('New')) == _('New'):
            vals['ref'] = self.env['ir.sequence'].next_by_code(
                'bookstore.book') or _('New')
        res = super(Books, self).create(vals)
        return res

    def inventory_action(self):
        action = self.env.ref('bookstore.action_bookstore_inventory').read()[0]
        action['domain'] = [('name', '=', self.id)]
        return action

    def _compute_quantity(self):
        for rec in self:
            rec.qty = sum(rec.env['bookstore.inventory'].search([('stock_type', '=', 'in'), ('name', '=', self.id)]).mapped(
                'stock')) - sum(rec.env['bookstore.inventory'].search([('stock_type', '=', 'out'), ('name', '=', self.id)]).mapped('stock'))
