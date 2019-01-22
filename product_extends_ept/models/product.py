from odoo import models, fields,api

class Product(models.Model):
    _inherit = 'product.ept'
    is_available = fields.Boolean(string="Is Available",help="Product is Available or Not")