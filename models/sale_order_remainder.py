# -*- coding: utf-8 -*-

from odoo import models, _
from datetime import date


class SaleOrder(models.Model):
	_inherit = 'sale.order'


	def sale_order_remainder_action_email(self):
		for order in self.env['sale.order'].search([('state', '=', 'draft'), ('validity_date', '!=', False)]):
			if order and (date.today() - order.validity_date).days == 10:
				template_id = self.env.ref('custom_saleorder.sale_order_remainder_email_template')
				if template_id:
					template_id.send_mail(order.id, force_send=True)
			elif order and (date.today() - order.validity_date).days == 5:
				template_id = self.env.ref('custom_saleorder.sale_before_order_remainder_email_template')
				if template_id:
					template_id.send_mail(order.id, force_send=True)
			else:
				pass

