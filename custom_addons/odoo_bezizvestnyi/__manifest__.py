# -*- coding: utf-8 -*-
{
    'name': "odoo_bezizvestnyi",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Расширение Quatations
    """,

    'author': "Bezizvestnyi(Chikov Mikhail)",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'license': 'LGPL-3',
    'application': True,
    'depends': ['base', 'sale_management', 'sale', 'hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

