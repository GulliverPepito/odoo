# -*- coding: utf-8 -*-
##############################################################################
#
# @ddfs. Copyright (c) 2017
#
##############################################################################
{
    'name': "social_media",

    'summary': """
        Social media extentions
    """,

    'description': """
        Social media extentions
    """,

    'author': "@ddfs",
    'website': "http://www.odoo.com",
    'category': 'Apps',
    'version': '0.1',

    # required modules
    'depends': ['website'],

    # always loaded
    'data': [
        'views/res_company_views.xml',
        'views/website_views.xml',
        'views/website_templates.xml',
    ],

    "sequence": 150
}
