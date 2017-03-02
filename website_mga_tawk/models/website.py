# -*- coding: utf-8 -*-
# Copyright 2017 Christophe CHAUVET
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class Website(models.Model):
    _inherit = 'website'

    tawk_siteid = fields.Char(
        'Tawk wite ID', help='The site ID from settings in tawk.to',
        default='')
    tawk_api_key = fields.Char(
        'Tawk API Key', help='API key to ensure the data you are sending'
        'is actually from you')
