from odoo import models,fields,api

class ProductBrand(models.Model):
    _name="product.brand"

    image=fields.Binary(string="Brand Logo",help="Product Image")
    name=fields.Char(string="Name",help="Product Name")
    no_available_product=fields.Integer(string="No Of Available Product",help="Number Of Available Product")
    active=fields.Boolean(string="Active",help="Product is Active or not",default=True)
    tag_line=fields.Char(string="Tag Line",help="Company Tag Line")
    description=fields.Html(string="Description",help="Brand Description")
    categories_m2m_ids=fields.Many2many('product.category.ept','product_category_rel_brand','category_id','brand_id',string="Category")



