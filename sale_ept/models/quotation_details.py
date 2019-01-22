from odoo import fields, models, api, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _name = 'sale.order.ept'
    _description = 'Sale Order EPT'
    
   
    name = fields.Char(string='Quotation Number', required=True, copy=False, readonly=True, states={'draft': [('readonly', False)]}, index=True, default=lambda self: _('New'))
    partner_id = fields.Many2one('customer.details.ept', string="Customer", help="Customer Name")
    validity_date = fields.Date(string="Validity", help="validity date of the quotation")
    sale_order_line_ids = fields.One2many('sale.order.line.ept', 'sale_order_id')
    # amount_total = fields.Float(string='Total', store=True, readonly=True, compute='_amount_all')
    confirmation_date = fields.Datetime(string='Confirmation Date', readonly=True, help="Date on which the sales order is confirmed.") 
    state = fields.Selection([('draft', 'Quotation'),
                              ('sent', 'Quotation Sent'),
                              ('sale', 'Sales Order'),
                              ('cancel', 'Cancelled'),
                              ('done', 'Locked')],
                               default="draft") 
   
    @api.multi    
    def action_confirm(self):
        
        self.write({
            'state': 'sale',
            'confirmation_date': fields.Datetime.now()
        })

    @api.multi
    def action_cancel(self):
        return self.write({'state': 'cancel'})
    
    @api.model
    def create(self, vals):
        
        if vals.get('name', _('New')) == _('New'):
            if 'company_id' in vals:
                vals['name'] = self.env['ir.sequence'].with_context(force_company=vals['company_id']).next_by_code('sale.order.ept') or _('New')
            else:
                vals['name'] = self.env['ir.sequence'].next_by_code('sale.order.ept') or _('New')
        return super(SaleOrder, self).create(vals)
    
    @api.multi
    def unlink(self):
        for order in self:
            if order.state=='sale':
                raise UserError(_('You can not delete a sent quotation or a confirmed sales order. You must first cancel it.'))
        return super(SaleOrder,self).unlink()
    
    @api.multi
    def action_done(self):
        return self.write({'state': 'done'})
   
    @api.multi
    def action_unlock(self):
        self.write({'state': 'sale'})
    
class SaleOrderLine(models.Model):
    _name = "sale.order.line.ept"
    
    @api.depends('ordered_qty', 'unit_price')
    def _sub_total(self):
        for values in self:
            values.sub_total = values.ordered_qty * values.unit_price
    
        
    sale_order_id = fields.Many2one('sale.order.ept', string="Sale Order")
    product_id = fields.Many2one('product.ept', string="Product")
    ordered_qty = fields.Integer(string="Ordered Quantity", help="Ordered Quantity")
    unit_price = fields.Integer(string="Unit Price", help="Unit Price")
    sub_total = fields.Float(string="Sub Total", compute="_sub_total",store=False)
    amount_total = fields.Float(string="Total", compute="_sub_total")
    
    
    
    @api.multi
    @api.onchange('product_id')
    def onchange_get_product_price(self):
        product_id = self.env['product.ept'].search([('id', '=', self.product_id.id)])
        self.update({"unit_price":product_id.price})
        
