from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = ['sale.order']

    order_confirm_date = fields.Datetime(string="Order Confirm Date",help="Order Confirmation Date")

    @api.multi
    def action_confirm(self):
        super(SaleOrder,self).action_confirm()
        self.write({
            'order_confirm_date': fields.Datetime.now()
        })
        return True