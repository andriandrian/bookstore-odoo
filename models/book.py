from odoo import models, fields, api, _


class Books(models.Model):
    _name = "bookstore.book"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Book Bookstore"

    currency_id = fields.Many2one('res.currency', string='Currency',
                                  default=lambda self: self.env.user.company_id.currency_id.id)
    name = fields.Char(string='Name', tracking=True)
    author = fields.Char(string='Author', tracking=True)
    price = fields.Float(string='Price', tracking=True)
    description = fields.Text(string='Description', tracking=True)
    qty = fields.Integer(string='Quantity', tracking=True,
                         compute='_compute_quantity')
    category_id = fields.Many2one('bookstore.category', string="Category")
    ref = fields.Char(string='Reference', required=True,
                      readonly=True, default=lambda self: _('New'))
    prescription = fields.Html(string='Prescription')
    active = fields.Boolean(string='Active', default=True)

    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         "You already have a book with this name!"),
    ]

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

    def wizard_update_stock(self):
        return {
            'name': _('Update Stock'),
            'type': 'ir.actions.act_window',
            'res_model': 'bookstore.inventory',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_name': self.id},
        }

    def name_get(self):
        result = []
        for rec in self:
            name = '[' + rec.ref + '] ' + rec.name
            result.append((rec.id, name))
        return result
