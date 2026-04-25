# -*- coding: utf-8 -*-
{
    'name': 'Product Asset Management',
    'version': '19.0.1.0.0',
    'summary': 'Add Asset tab to product template after inventory',
    'sequence': 10,
    'description': """
        This module adds a new tab named 'Assets' in the product form view
        specifically after the Inventory tab.
    """,
    'category': 'Inventory',
    'author': 'Zahidul Islam', 
    'license': 'LGPL-3',
    'depends': [
        'base',
        'product',
        'stock',  
    ],
    'data': [
        'views/product_asset_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}