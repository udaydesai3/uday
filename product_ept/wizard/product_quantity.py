from odoo import models, fields, api
from odoo.exceptions import Warning



class ProductQuantity(models.TransientModel):

    _name ='product.ept.wizard'

    product_wizard_id = fields.Many2one('product.ept',string="Product Name", required=True, readonly=True )
    update_on_hand_quantity = fields.Integer(string="New Quantity on Hand",default=1)

    @api.multi
    def update_onhand_quantity(self):
        """
        func: this method is used for to update on hand quantity
        param: no paramater
        return:
        """
        if self.update_on_hand_quantity <= 0:
            raise Warning("You can not set quantity to 0. It should be minimum 1 quantity")
        context = dict(self._context) or {}
        product_id = self.env['product.ept'].browse(context.get('active_id',False))
        product_id.update({'on_hand_quantity':self.update_on_hand_quantity})

