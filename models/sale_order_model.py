# -*- coding: utf-8 -*-

from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sales_va = fields.Monetary(
        comodel_name='project.project',  
        related='analytic_account_id.project_ids.sale_added_value_economic_ratio', 
        string='Sales VA',
        readonly=True, 
        store=True
    )

