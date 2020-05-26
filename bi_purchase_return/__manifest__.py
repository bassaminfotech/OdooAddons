# -*- coding: utf-8 -*-
{
    'name': "Purchase Return",

    'summary': """
        Purchase Return Workflow""",

    'description': """
        Create a purchase return seperately and create corresponding deliveries
        and corresponding debit note.
    """,

    'author': "Bassam Infotech LLP",
    'website': "http://www.bassaminfotech.com",

    'category': 'Purchase',
    'version': '12.0.0.1',

    'depends': ['base', 'purchase', 'account'],

    'images': [
        'static/description/purchase_return.png',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/purchase_return.xml',
        'data/ir_sequence_data.xml',
    ],
}
