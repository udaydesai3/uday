from odoo import api, fields, models, _

class Sale(models.Model):
    _inherit = ['res.partner']

    fax = fields.Char(string="Fax",help="Fax Number")
    linkedin = fields.Char(string="Linked In",help="Linked in Name")
    