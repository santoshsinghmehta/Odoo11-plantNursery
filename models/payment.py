# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import models,fields

class payment(models.Model):
    _name = 'nursery.payment'

    name = fields.Many2one("nursery.plant", required=True)
    plant_paymemnt=fields.Char("payment method")
