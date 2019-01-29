from odoo import models, fields, api


class SaleInvoices(models.TransientModel):

    _name ='invoices.ept.wizard'

    #down_payment_in_amount = fields.Boolean(string="DownPayment in Amount")
    #down_payment_in_percentage = fields.Boolean(string="Download in Percentage")
    down_payment_amount = fields.Integer(string="Down Payment Amount")