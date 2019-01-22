from odoo import models, fields,api

class ProductCategory(models.Model):
    _name = 'product.category.ept'    
    
    @api.multi
    def get_product(self):
        """ this method is used for to calculate the total product.     """
        products = self.mapped('product_id')
        self.product_count=len(products)
        
    @api.multi
    def action_view_product(self):
        products = self.mapped('product_id')
        action = self.env.ref('product_ept.product_ept_action').read()[0]
        if len(products) > 1:
            action['domain'] = [('id', 'in', products.ids)]
        elif len(products) == 1:
            action['views'] = [(self.env.ref('product_ept.product_ept_form').id, 'form')]
            action['res_id'] = products.ids[0]
        else:
            action = {'type': 'ir.actions.act_window_close'}
        return action
    
    name = fields.Char(string="Name",help="Name")    
    no_of_available_products = fields.Integer(string="No Of Available Products",help="Number Of Available Product")
    no_of_brand = fields.Char(string="No Of Brand",help="Number Of Available Brand")
    description = fields.Text(string="Description",help="Product Description")    
    product_id=fields.One2many('product.ept','category_id',string="Products")
    product_count = fields.Integer(string='Product Count', compute='get_product', readonly=True)
    type = fields.Selection([('stock able', 'Stock able'), ('service', 'Service'),('consumable','Consumable')], string='Type',help="Category Type")
    
    
    