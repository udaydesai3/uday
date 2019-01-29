# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Sales extends ept',
    'version': '1.1',
    'category': 'Sales',
    'summary': 'Sales extends internal machinery',
    'description': """
This module contains all the common features of Sales Management and eCommerce.
    """,
    'depends': ['base','sale'],
    'data': ['views/res_partner_view.xml',
             'views/sale_order_ept_view.xml'

    ],
    'demo': [

    ],

    'installable': True,
    'auto_install': False
}
