# -*- coding: utf-8 -*-
# Copyright 2017 Christophe CHAUVET
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import models, fields


class WebsiteConfigSettings(models.TransientModel):
    _inherit = 'website.config.settings'

    tawk_siteid = fields.Char(
        related=['website_id', 'tawk_siteid'])
    tawk_api_key = fields.Char(
        related=['website_id', 'tawk_api_key'])
