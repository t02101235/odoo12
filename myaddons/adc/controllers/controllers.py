# -*- coding: utf-8 -*-
from odoo import http

# class Adc(http.Controller):
#     @http.route('/adc/adc/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/adc/adc/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('adc.listing', {
#             'root': '/adc/adc',
#             'objects': http.request.env['adc.adc'].search([]),
#         })

#     @http.route('/adc/adc/objects/<model("adc.adc"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('adc.object', {
#             'object': obj
#         })