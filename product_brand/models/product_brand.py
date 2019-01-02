from odoo import models,fields

class ProductBrand(models.Model):
    _name="product.brand"
    
    image=fields.Binary(string="Brand Logo",help="Product Image")
    name=fields.Char(string="Name",help="Product Name")
    no_of_brand=fields.Integer(string="No Of Brand",help="Number Of Brands")
    no_available_product=fields.Integer(string="No Of Available Product",help="Number Of Available Product")
    active=fields.Boolean(string="Active",help="Product is Active or not")
    tag_line=fields.Char(string="Tag Line",help="Company Tag Line")
    description=fields.Html(string="Description",help="Brand Description")