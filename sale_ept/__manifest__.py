{

    'name': 'Sale Ept',
    'version': '1.0',
    'depends': ['base','digest','sale'],
    'category': 'Sales',
    'summary': 'Sale Ept Module',
    'sequence': 3,
    'description': 'this module is used for to sale product ',
    'data': [
            'security/ir.model.access.csv',
            'views/quotation_details_views.xml',
            'views/customer_details_views.xml',
            'data/ir_sequence_data.xml',
            'wizard/sale_invoice_wizard_view.xml'

             ],
    'demo': [

    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
