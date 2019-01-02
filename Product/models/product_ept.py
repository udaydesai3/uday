from odoo import models, fields,api

class ProductEpt(models.Model):
    _name='product.ept'
    @api.depends('price', 'on_hand_quantity')
    def _total_price(self):
        for i in self:
            i.total_price=i.price*i.on_hand_quantity
        
    
    image=fields.Binary(string="Product Image")
    name=fields.Char(string="Product Name",help="Name")
    price=fields.Integer(string="Price",help="Product Individual price")
    on_hand_quantity=fields.Integer(string="On Hand Quantity",help="Product Quantity")
    total_price = fields.Float(compute='_total_price', string='Total Price',digits=0,help="Total Price")
    date=fields.Date(string="Date",help="Date")
    is_salable=fields.Boolean(string="Is Salable",help="Product is Salable or not")
    description=fields.Html(string="Description",help="Product Description")
    state = fields.Selection([('stock able', 'Stock able'), ('service', 'Service'),('consumable','Consumable')], string='Type',help="Product Type")
    