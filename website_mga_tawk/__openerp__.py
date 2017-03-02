# -*- coding: utf-8 -*-
# Copyright 2017 Christophe CHAUVET
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Live Chat Tawk.to',
    'version': '8.0.1.0.0',
    'category': 'Website',
    'sequence': 50,
    'complexity': "expert",
    'description': """Use tawk.to service to embedded Live Chat in Odoo
Replace the original chat module
""",
    'author': 'Mirounga',
    'website': 'http://mirounga.fr',
    'license': 'AGPL-3',
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
    'installable': True,
    'application': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
