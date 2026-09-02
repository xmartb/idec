# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class HrSalaryRule(models.Model):
    _inherit = 'hr.salary.rule'

    integrar_isn = fields.Boolean('Incluir en ISN')
