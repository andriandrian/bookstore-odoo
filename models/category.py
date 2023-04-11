from odoo import models, fields, api, _


class Categories(models.Model):
    _name = "bookstore.category"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Book Category"

    name = fields.Char(string='Name', tracking=True, required=True)
    description = fields.Text(string='Description', tracking=True)
    active = fields.Boolean(string='Active', default=True)
    ref = fields.Char(string='Reference', required=True,
                      readonly=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('ref', _('New')) == _('New'):
            vals['ref'] = self.env['ir.sequence'].next_by_code(
                'bookstore.category') or _('New')
        res = super(Categories, self).create(vals)
        return res
