from odoo import models, fields, api
import logging
_looger = logging.getLogger(__name__)
class LxbSubject(models.Model):
  _name = 'lxb.subject'
  _rec_name = 'name'
  _description = 'LXB Subject'
  
  name = fields.Char('科目名称', size=128, required=True)
  code = fields.Char('科目编码', size=256, required=True)
  type = fields.Selection([('theory', '理论'), ('practical', '实践')
                          ,('both', '理论实践结合'), ('other','其他')], 
                          string='类别', default='theory', required=True)
  subject_type = fields.Selection([('compulsory', '必修'), ('elective', '选修'),
                                    ], string='科⽬类型', default='compulsory', required=True)
  _sql_constraints = [('unique_subject_code','unique(code)','科目编码必须唯一！')]


 


  
  



  