from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class LxbStudent(models.Model):
    _name = 'lxb.student'
    _description = '学生'
    _inherits = {'res.partner': 'partner_id'}

    birth_date = fields.Date('出生日期')
    gender = fields.Selection([('man', '男',), ('female', '女',), ('other', '其他',)], string="性别")
    nationality = fields.Many2one('res.country', string="国籍", default=lambda self: self.env.ref('base.cn').id)
    emergency_contact = fields.Many2one('res.partner', string="紧急联系人")
    class_id = fields.Many2one('lxb.class', string="班级")
    already_partner = fields.Boolean(string="是否为老学员")
    partner_id = fields.Many2one('res.partner', string="关联家长", required=True, ondelete='cascade')
    gr_no = fields.Char(string="学号", size=20, required=True)
    company_id = fields.Many2one('res.company', string="公司", default=lambda self: self.env.user.company_id)


    @api.constrains('birth_date')
    def _check_birth_date(self):
        for record in self:
            if record.birth_date > fields.Date.today():
                raise ValidationError("出生日期不能大于当前日期")
