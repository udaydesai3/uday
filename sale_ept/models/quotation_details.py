from odoo import fields, models, api, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _name = 'sale.order.ept'
    _description = 'Sale Order EPT'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
   
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
                             track_visibility='always',
                               default="draft")



    @api.multi
    @api.depends('sale_order_line_ids.product_id')
    def action_confirm(self):
        context = dict(self._context) or {}
        product_id = self.env['sale.order.line.ept']
        for order in self:
            print(order)
            for line in product_id:
                product_id = self.env['product.ept'].browse(line.id)
                print(line.ordered_qty)


        self.write({
            'state': 'sale',
            'confirmation_date': fields.Datetime.now()
        })

    @api.multi
    def action_cancel(self):
        return self.write({'state': 'cancel'})

    @api.multi
    def action_create_invoice(self):
        return {
            'name': _('Invoice Order'),
            'type': 'ir.actions.act_window',
            'res_model': 'invoices.ept.wizard',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
            'views': [[self.env.ref('sale_ept.sale_invoices_wizard_form_view').id, 'form']]
        }
    @api.multi
    def action_set_quotation(self):
        return self.write({'state': 'draft'})
    
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

    @api.multi
    def action_plus(self):
        self.ordered_qty +=1
    @api.multi
    def action_minus(self):
        self.ordered_qty -=1
        if self.ordered_qty == 0:
            raise UserError(_("You can not set 0 Quantity "))