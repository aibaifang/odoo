from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

import logging
_logger = logging.getLogger(__name__)

class LxbTeacher(models.Model):
    _name = "lxb.teacher"
    _description = "教师"
    _inherits = {"res.partner": "partner_id"}

    partner_id = fields.Many2one('res.partner', required=True, ondelete='cascade', string='合作伙伴')
    birth_date = fields.Date(string='出生日期', required=True)
    gender = fields.Selection([('male', '男'), ('female', '女')], string='性别', required=True)
    nationality = fields.Many2one('res.country', string='国籍')
    emergency_contact = fields.Many2one('res.partner', string='紧急联系人')
    visa_info = fields.Char(string='银行卡', size=64)
    id_number = fields.Char(string='ID卡号', size=64)
    login = fields.Char(string='登录', related='partner_id.user_id.login', readonly=1)
    last_login = fields.Datetime(string='最后登录', related='partner_id.user_id.login_date', readonly=1)
    emp_id = fields.Many2one('hr.employee', string='员工',)
    company_id = fields.Many2one('res.company', string='公司', default=lambda self: self.env.user.company_id)
    teacher_subject_ids = fields.Many2many('lxb.subject', string='可授科目')
    @api.constrains('birth_date')
    def _check_birth_date(self):
        for record in self:
           # _logger.info(f"dfdfdfdf{record.birth_date}")
            if record.birth_date > fields.Date.today():
                raise ValidationError('出生日期不能晚于当前日期！')
    




