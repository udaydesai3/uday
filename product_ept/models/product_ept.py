from odoo import models, fields,api
from odoo.exceptions import Warning ,UserError

class ProductEpt(models.Model):
    
    _name='product.ept'
    _description="Product EPT"
    #_inherit="product.template"
    #_order="date"
    
#    @api.depends('price', 'on_hand_quantity')
#    def _total_price(self):
#        for i in self:
#            i.total_price=i.price*i.on_hand_quantity
    
    @api.onchange('price','on_hand_quantity','type')
    def onchange_total_price(self):
        """
        func : this method is used for calculate total price.
        param : no parameter
        return :no return
        """
        result={}
        product_category = self.env['product.category.ept']
        
        self.total_price=self.price * self.on_hand_quantity
        if self.price < 100:
            raise Warning('Product Price should be minimum 100')        
        result['domain'] = {'category_id':[('type','=',self.type)]}
        return result
        
    
        
    @api.model
    def create(self,vals):
        product = super(ProductEpt, self).create(vals)
        return product
    
    @api.multi
    def write(self,values):
        return super (ProductEpt,self).write(values)
    
    @api.multi
    def unlink(self):
        return super(ProductEpt,self).unlink()
        
    image1=fields.Binary(string="Product Image",attachment=True)
    name=fields.Char(string="Product Name",help="Name",required="True")
    price=fields.Float(string="Price",help="Product Individual price",required="True")
    on_hand_quantity=fields.Integer(string="On Hand Quantity",help="Product Quantity",required="True")
    total_price = fields.Float(string='Total Price',help="Total Price")
    date=fields.Date(string="Date",help="Date")
    is_salable=fields.Boolean(string="Is Salable",help="Product is Salable or not")
    description=fields.Text(string="Description",help="Product Description")
    category_id=fields.Many2one('product.category.ept',string="Category")
    active=fields.Boolean(string="Active",help="Product is Active or not",default=True)
    type = fields.Selection([('stock able', 'Stock able'), ('service', 'Service'),('consumable','Consumable')],default="stock able", string='Type',help="Product Type")
    
    """_sql_constraints = [
        ('name_uniq', 'UNIQUE (name)',  'You can not give same product name !')
    ]"""
    
       