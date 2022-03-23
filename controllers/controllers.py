# -*- coding: utf-8 -*-
# from odoo import http


# class CustomSaleorder(http.Controller):
#     @http.route('/custom_saleorder/custom_saleorder/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_saleorder/custom_saleorder/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_saleorder.listing', {
#             'root': '/custom_saleorder/custom_saleorder',
#             'objects': http.request.env['custom_saleorder.custom_saleorder'].search([]),
#         })

#     @http.route('/custom_saleorder/custom_saleorder/objects/<model("custom_saleorder.custom_saleorder"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_saleorder.object', {
#             'object': obj
#         })
