from odoo import models, fields


class ProductCategory(models.Model):
    _name = 'product.category.ept'
    
    name = fields.Char(string="Product Name",help="Name")
    no_of_brands = fields.Integer(string="No Of Brands",help="Number Of Brands")
    no_of_available_products = fields.Integer(string="No Of Available Products",help="Number Of Available Product")
    description = fields.Html(string="Description",help="Product Description")
