# -*- coding: utf-8 -*-
# from odoo import http


# class LxbCore(http.Controller):
#     @http.route('/lxb_core/lxb_core', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lxb_core/lxb_core/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lxb_core.listing', {
#             'root': '/lxb_core/lxb_core',
#             'objects': http.request.env['lxb_core.lxb_core'].search([]),
#         })

#     @http.route('/lxb_core/lxb_core/objects/<model("lxb_core.lxb_core"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lxb_core.object', {
#             'object': obj
#         })
