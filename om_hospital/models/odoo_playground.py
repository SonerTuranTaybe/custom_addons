# -*- coding: utf-8 -*-
8
from odoo import api, fields, models
from odoo.tools.safe_eval import safe_eval

class OdooPlayGround(models.Model):
    _name = "odoo.playground"
    _description = "Odoo PlayGround"