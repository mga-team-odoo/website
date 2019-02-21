# -*- coding: utf-8 -*-
# Copyright 2017 Christophe CHAUVET
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Live Chat Tawk.to',
    'version': '10.0.1.0.0',
    'category': 'Website',
    'sequence': 50,
    'complexity': "expert",
    'description': """Use tawk.to service to embedded Live Chat in Odoo
Replace the original chat module
""",
    'author': 'Mirounga',
    'website': 'http://mirounga.fr',
    'license': 'LGPL-3',
    'images': [],
    'depends': [
        'website',
    ],
    'data': [
        'views/website_config_settings.xml',
        'views/website.xml',
        'views/templates.xml',
    ],
    'demo': [],
    'installable': False,
    'application': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
