from odoo import models, fields, api

class ResCompany(models.Model):
    _inherit = "res.company"

    signature = fields.Binary(string="Signature")
    accreditation = fields.Text(string="资格鉴定")
    approval_authority = fields.Text(string="核准")
    institue_type = fields.Selection([('group','集团总部'),
                                      ('direct','直营店'),
                                      ('join', '加盟店'), string="机构类型"])


    class ResUsers(models.Model):
        _inherit = "res.users"
        user_line = fields.One2many('lxb.student', 'user_id', string='学生信息')
        child_ids = fields.One2many('res.users', 'res_user_first_rell',
                                     'user_id', 'res_user_second_rell', string='childs')

        def create_user(self, records, user_group=None):
            for rec in records:
                if not rec.user_id:
                    user_vals={
                        'name': rec.name,
                        'login': rec.email or rec.name,
                        'partner_id': rec.partner_id.id
                    }
                    user_id = self.create(user_vals)
                    rec.user_id = user_id
                    if user_group:
                        user_group.users = user_group.users + user_id