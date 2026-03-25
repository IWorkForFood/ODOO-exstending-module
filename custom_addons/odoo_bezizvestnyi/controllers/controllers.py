# -*- coding: utf-8 -*-
# from odoo import http


# class OdooBezizvestnyi(http.Controller):
#     @http.route('/odoo_bezizvestnyi/odoo_bezizvestnyi', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_bezizvestnyi/odoo_bezizvestnyi/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_bezizvestnyi.listing', {
#             'root': '/odoo_bezizvestnyi/odoo_bezizvestnyi',
#             'objects': http.request.env['odoo_bezizvestnyi.odoo_bezizvestnyi'].search([]),
#         })

#     @http.route('/odoo_bezizvestnyi/odoo_bezizvestnyi/objects/<model("odoo_bezizvestnyi.odoo_bezizvestnyi"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_bezizvestnyi.object', {
#             'object': obj
#         })

