from odoo import models, fields

class CustomerDetails(models.Model):
    _name = 'customer.details.ept'
    _description = 'Customer Detail'
    
    name=fields.Char(string="Customer Name",help="Customer Name",required=True)
    image=fields.Binary(string="Customer Image",help="Customer Image")
    street=fields.Char()
    street2=fields.Char()
    city=fields.Char()
    customer_zip=fields.Char()
    vat = fields.Char()
    phone = fields.Char(string="Phone Number", help="Phone Number")
    mobile = fields.Char(string="Mobile number", help="Mobile Number")
    customer_email=fields.Char(string="Email", help="Email")
