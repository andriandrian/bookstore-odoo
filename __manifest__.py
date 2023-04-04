# -*- coding: utf-8 -*-
{
    'name': "Bookstore",
    'summary': """Bookstore Management""",
    'description': """
        Bookstore Management
    """,
    'author': "Andrian",
    'website': "http://www.yourcompany.com",
    'category': 'Management',
    'sequence': -100,
    'version': '0.1',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/employee_views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
