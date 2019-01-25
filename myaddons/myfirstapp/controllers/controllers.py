# -*- coding: utf-8 -*-
from odoo import http

# class Myfirstapp(http.Controller):
#     @http.route('/myfirstapp/myfirstapp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/myfirstapp/myfirstapp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('myfirstapp.listing', {
#             'root': '/myfirstapp/myfirstapp',
#             'objects': http.request.env['myfirstapp.myfirstapp'].search([]),
#         })

#     @http.route('/myfirstapp/myfirstapp/objects/<model("myfirstapp.myfirstapp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('myfirstapp.object', {
#             'object': obj
#         })