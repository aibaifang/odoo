from odoo import models, api, fields
class LxbClass(models.Model):
    _name = 'lxb.class'
    _description = '班级'

    code = fields.Char(string='班级编号' , size=16, required=True, 
                        readonly=True, default= lambda x:('_New'))
    name = fields.Char(string='班级名称', required=True)
    class_advisor = fields.Many2one('lxb.teacher', string='班主任', required=True)
    student_no = fields.Integer(string='学生人数', default=0, compute='_compute_student_no')
    student_ids = fields.One2many('lxb.student', 'class_id', string='学生列表')
    specific_site = fields.Text(string='具体位置')
    company_id = fields.Many2one('res.company', string="公司", required=True, 
                                default=lambda self: self.env.user.company_id.id)
    # schedule_id = fields.Many2one('lxb.schedule', string='约排课计划')

    @api.model
    def create(self, vals):
        if not vals.get('code') or vals.get('code') == '_New':
            vals['code'] = self.env['ir.sequence'].next_by_code('lxb.class')
        return super(LxbClass, self).create(vals)


    @api.depends('student_ids')
    def _compute_student_no(self):
        for record in self:
            record.student_no = record.student_ids.size() if record.student_ids else 0






